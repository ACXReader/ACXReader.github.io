import argparse
import json
import os
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from time import sleep

from bs4 import BeautifulSoup
import html2text
import requests
from xml.etree import ElementTree as ET
from tqdm import tqdm
import dateparser
import atexit

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service
from urllib.parse import urlparse

from config import EMAIL, PASSWORD

# Set to True if you want to login to Substack and convert paid for posts
USE_PREMIUM: bool = False
# Substack you want to convert to markdown
BASE_SUBSTACK_URL: str = "https://map.simonsarris.com/"
BASE_DIR_NAME: str = "_posts"  # Name of the directory we'll save the files to
JSON_DATA_DIR: str = "."
NUM_POSTS_TO_SCRAPE: int = 0  # Set to 0 if you want all posts
TIMES_TO_RETRY: int = 5
RETRY_SLEEP_TIME: float = 5


def extract_main_part(url: str) -> str:
    # Parse the URL to get the netloc, and split on '.'
    parts = urlparse(url).netloc.split('.')
    # Return the main part of the domain, while ignoring 'www' if
    return parts[1] if parts[0] == 'www' else parts[0]
    # present


class BaseSubstackScraper(ABC):
    def __init__(self, base_substack_url: str, save_dir: str):
        if not base_substack_url.endswith("/"):
            base_substack_url += "/"
        self.base_substack_url: str = base_substack_url
        self.writer_name: str = extract_main_part(base_substack_url)

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
            print(f"Created directory {save_dir}")
        self.save_dir: str = save_dir
        self.keywords: List[str] = [
            "about", "archive", "podcast"]
        self.existing_data: List[str] = []
        self.premium_articles: List[str] = []
        self.post_urls: List[str] = self.get_new_post_urls()
        atexit.register(self.save)

    def get_new_post_urls(self) -> List[str]:
        """
        This method reads the sitemap.xml file and returns a list of all new URLs in the file
        """
        sitemap_url = f"{self.base_substack_url}sitemap.xml"
        response = requests.get(sitemap_url)

        if response.ok:
            root = ET.fromstring(response.content)
            urls = [element.text for element in root.iter(
                '{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
            urls = self.filter_urls(urls, self.keywords)
            if os.path.exists("./posts_list.json"):
                with open("./posts_list.json", 'r', encoding='utf-8') as file:
                    self.existing_data += json.load(file)
                urls = [data for data in urls if data not in self.existing_data]
            if not self.premium and os.path.exists("./premium_list.json"):
                with open("./premium_list.json", 'r', encoding='utf-8') as file:
                    self.premium_articles += json.load(file)
                urls = [data for data in urls if data not in self.premium_articles]
            return urls
        else:
            print(f'Error fetching sitemap: {response.status_code}')
            return []

    @staticmethod
    def filter_urls(urls: List[str], keywords: List[str]) -> List[str]:
        """
        This method filters out URLs that contain certain keywords
        """
        return [url for url in urls if all(keyword not in url for keyword in keywords)]

    @staticmethod
    def html_to_md(html_content: str) -> str:
        """
        This method converts HTML to Markdown
        """
        if not isinstance(html_content, str):
            raise ValueError("html_content must be a string")
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.body_width = 0
        return h.handle(html_content)

    @staticmethod
    def save_to_file(filepath: str, content: str) -> None:
        """
        This method saves content to a file. Can be used to save HTML or Markdown
        """
        if not isinstance(filepath, str):
            raise ValueError("filepath must be a string")

        if not isinstance(content, str):
            raise ValueError("content must be a string")

        if os.path.exists(filepath):
            print(f"File already exists: {filepath}")
            return

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)

    @staticmethod
    def get_filename_from_url(url: str, filetype: str = ".md") -> str:
        """
        Gets the filename from the URL (the ending)
        """
        if not isinstance(url, str):
            raise ValueError("url must be a string")

        if not isinstance(filetype, str):
            raise ValueError("filetype must be a string")

        if not filetype.startswith("."):
            filetype = f".{filetype}"

        return url.split("/")[-1] + filetype

    @staticmethod
    def combine_metadata_and_content(title: str, subtitle: str, date: str, like_count: str, url: str, content) -> str:
        """
        Combines the title, subtitle, and content into a single string with Markdown format
        """
        if not isinstance(title, str):
            raise ValueError("title must be a string")

        if not isinstance(content, str):
            raise ValueError("content must be a string")

        # jekyll front matter
        metadata = "---\n"
        # very annoying!!!
        title = title.replace("\"", "\\\"")
        metadata += f"title: \"{title}\"\n"
        if subtitle:
            subtitle = subtitle.replace("\"", "\\\"")
            metadata += f"subtitle: \"{subtitle}\"\n"
        metadata += f"date: {date}\n"
        metadata += f"likes: {like_count}\n"
        metadata += f"original-url: {url}\n"
        metadata += "---\n"

        return metadata + content

    def extract_post_data(self, soup: BeautifulSoup, url: str) -> Tuple[str, str]:
        """
        Converts substack post soup to markdown, returns metadata and content
        """
        title = soup.select_one("h1.post-title").text.strip()
        subtitle_element = soup.select_one("h3.subtitle")
        subtitle = subtitle_element.text.strip() if subtitle_element else ""

        date_selector = ".pencraft.pc-display-flex.pc-gap-4.pc-reset .pencraft"
        date_element = soup.select_one(date_selector)
        date = "0000-00-00"
        if date_element:
            # jekyll compatible date
            date = dateparser.parse(
                date_element.text.strip()).strftime("%Y-%m-%d")

        like_count_element = soup.select_one("a.post-ufi-button .label")
        like_count = like_count_element.text.strip(
        ) if like_count_element else "0"

        content = str(soup.select_one("div.available-content"))
        md = self.html_to_md(content)
        md_content = self.combine_metadata_and_content(
            title, subtitle, date, like_count, url, md)
        return date, md_content

    @abstractmethod
    def get_url_soup(self, url: str) -> str:
        raise NotImplementedError

    def scrape_posts(self, num_posts_to_scrape: int = 0) -> None:
        """
        Iterates over all posts and saves them as markdown files
        """
        count = 0
        total = num_posts_to_scrape if num_posts_to_scrape != 0 else len(
            self.post_urls)
        for url in tqdm(self.post_urls, total=total):
            success = self.process_post(url)
            if success:
                self.existing_data.append(url)
                count += 1
                if num_posts_to_scrape != 0 and count == num_posts_to_scrape:
                    break
            else:
                total += 1
        self.save()

    def save(self) -> None:
        """
        Saves a list of downloaded files to prevent reprocessing
        """
        with open("./posts_list.json", 'w', encoding='utf-8') as f:
            json.dump(self.existing_data, f, ensure_ascii=False, indent=4)
        with open("./premium_list.json", 'w', encoding='utf-8') as f:
            json.dump(self.premium_articles, f, ensure_ascii=False, indent=4)

    def process_post(self, url: str) -> bool:
        """
        Process a single post
        """
        for _ in range(TIMES_TO_RETRY):
            try:
                soup = self.get_url_soup(url)
                if soup is None:
                    return False
                date, md = self.extract_post_data(soup, url)
                filename = self.get_filename_from_url(url, filetype=".md")
                filepath = os.path.join(
                    self.save_dir, date + "-" + filename)
                self.save_to_file(filepath, md)
                return True
            except Exception as e:
                print(f"Error scraping post: {e}, url: {url}")
                sleep(RETRY_SLEEP_TIME)
        return False


class SubstackScraper(BaseSubstackScraper):
    def __init__(self, base_substack_url: str, save_dir: str):
        self.premium = False
        super().__init__(base_substack_url, save_dir)

    def get_url_soup(self, url: str) -> Optional[BeautifulSoup]:
        """
        Gets soup from URL using requests
        """
        try:
            page = requests.get(url, headers=None)
            soup = BeautifulSoup(page.content, "html.parser")
            if soup.find("h2", class_="paywall-title"):
                print(f"Skipping premium article: {url}")
                self.premium_articles.append(url)
                return None
            return soup
        except Exception as e:
            raise ValueError(f"Error fetching page: {e}") from e


class PremiumSubstackScraper(BaseSubstackScraper):
    def __init__(
            self,
            base_substack_url: str,
            save_dir: str,
            headless: bool = False,
            edge_path: str = '',
            edge_driver_path: str = '',
            user_agent: str = ''
    ) -> None:
        self.premium = True
        super().__init__(base_substack_url, save_dir)

        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        if edge_path:
            options.binary_location = edge_path
        if user_agent:
            # Pass this if running headless and blocked by captcha
            options.add_argument(f'user-agent={user_agent}')

        if edge_driver_path:
            service = Service(executable_path=edge_driver_path)
        else:
            service = Service(EdgeChromiumDriverManager().install())

        self.driver = webdriver.Edge(service=service, options=options)
        self.login()

    def login(self) -> None:
        """
        This method logs into Substack using Selenium
        """
        self.driver.get("https://substack.com/sign-in")
        sleep(3)

        signin_with_password = self.driver.find_element(
            By.XPATH, "//a[@class='login-option substack-login__login-option']"
        )
        signin_with_password.click()
        sleep(3)

        # Email and password
        email = self.driver.find_element(By.NAME, "email")
        password = self.driver.find_element(By.NAME, "password")
        email.send_keys(EMAIL)
        password.send_keys(PASSWORD)

        # Find the submit button and click it.
        submit = self.driver.find_element(
            By.XPATH, "//*[@id=\"substack-login\"]/div[2]/div[2]/form/button")
        submit.click()
        sleep(30)  # Wait for the page to load

        if self.is_login_failed():
            raise Exception("Warning: Login unsuccessful. Please check your email and password, or your account status.\n"
                            "Use the non-premium scraper for the non-paid posts. \n"
                            "If running headless, run non-headlessly to see if blocked by Captcha.")

    def is_login_failed(self) -> bool:
        """
        Check for the presence of the 'error-container' to indicate a failed login attempt.
        """
        error_container = self.driver.find_elements(By.ID, 'error-container')
        return len(error_container) > 0 and error_container[0].is_displayed()

    def get_url_soup(self, url: str) -> BeautifulSoup:
        """
        Gets soup from URL using logged in selenium driver
        """
        try:
            self.driver.get(url)
            return BeautifulSoup(self.driver.page_source, "html.parser")
        except Exception as e:
            raise ValueError(f"Error fetching page: {e}") from e


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Scrape a Substack site.')
    parser.add_argument('-u', '--url', type=str,
                        help='The base URL of the Substack site to scrape.')
    parser.add_argument('-d', '--directory', type=str,
                        help='The directory to save scraped posts.')
    parser.add_argument('-n', '--number', type=int, default=0,
                        help='The number of posts to scrape. If 0 or not provided, all posts will be scraped.')
    parser.add_argument('-p', '--premium', action='store_true',
                        help='Include -p in command to use the Premium Substack Scraper with selenium.')
    parser.add_argument('--headless', action='store_true',
                        help='Include -h in command to run browser in headless mode when using the Premium Substack '
                             'Scraper.')
    parser.add_argument('--edge-path', type=str, default='',
                        help='Optional: The path to the Edge browser executable (i.e. "path_to_msedge.exe").')
    parser.add_argument('--edge-driver-path', type=str, default='',
                        help='Optional: The path to the Edge WebDriver executable (i.e. "path_to_msedgedriver.exe").')
    parser.add_argument('--user-agent', type=str, default='',
                        help='Optional: Specify a custom user agent for selenium browser automation. Useful for '
                             'passing captcha in headless mode')

    return parser.parse_args()


def main():
    args = parse_args()

    if args.directory is None:
        args.directory = BASE_DIR_NAME

    if args.url:
        if args.premium:
            scraper = PremiumSubstackScraper(
                args.url, headless=args.headless, save_dir=args.directory)
        else:
            scraper = SubstackScraper(args.url, save_dir=args.directory)
        scraper.scrape_posts(args.number)

    else:  # Use the hardcoded values at the top of the file
        if USE_PREMIUM:
            scraper = PremiumSubstackScraper(
                base_substack_url=BASE_SUBSTACK_URL,
                save_dir=args.directory,
                edge_path=args.edge_path,
                edge_driver_path=args.edge_driver_path
            )
        else:
            scraper = SubstackScraper(
                base_substack_url=BASE_SUBSTACK_URL, save_dir=args.directory)
        scraper.scrape_posts(num_posts_to_scrape=NUM_POSTS_TO_SCRAPE)


if __name__ == "__main__":
    main()
