---
title: "Carbon Costs Quantified"
subtitle: "..."
date: 2021-08-25
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/40347952/comments?&all_comments=true
image: https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/ecf2e2db-a771-401e-b2a2-175fe794c73d_550x422.jpeg
original-url: https://www.astralcodexten.com/p/carbon-costs-quantified
---
This post tries to quantify how much carbon is produced by various activities, lifestyle changes, and actors. 

I can’t stress enough how approximate and unreliable these numbers are. The reason I made this chart and other people didn’t isn’t because I’m smarter or harder-working than they are. It’s because I’m less responsible, and more willing to use numbers that are kind of grounded in wild guesses, and technically shouldn’t be compared to each other. My defense is they’re probably mostly order-of-magnitude correct, and [I believe](https://slatestarcodex.com/2013/05/02/if-its-worth-doing-its-worth-doing-with-made-up-statistics/) having probably mostly order-of-magnitude correct estimates is better than having no estimates at all.

Explanations below:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F68cf8e49-2d6f-4d34-b4a2-2a3464fc754d_818x849.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F68cf8e49-2d6f-4d34-b4a2-2a3464fc754d_818x849.png)Check the sources for explanations of how I calculated some of these.

**Lbs CO2** is self-explanatory - except that in a few cases, especially those involving beef, it also includes other greenhouse gases, converted to CO2 at equivalent levels of global warming contribution.

**Avg US person-years** is what fraction of the average American's yearly carbon emissions that much CO2 represents. So for example 0.25 means it's one-quarter of the average American's yearly emissions, and 50 means it emits 50 times as much CO2 as the average American.

**$ offset** is how much money it would cost to offset that much carbon, by eg planting trees. Offset cost is controversial, so I've included two numbers - optimistic and pessimistic. 

“Optimistic” is closest to the existing consensus, and is the price at which most companies will sell you offsets. I took [Native Energy](https://native.eco)'s $15/ton as my guide, but there are lots of places with more or less the same price. They usually work by paying people in Third World countries not to cut down trees; since trees remove carbon from the atmosphere, this ought to offset emissions. But there are [a lot of ways this can go wrong](https://features.propublica.org/brazil-carbon-offsets/inconvenient-truth-carbon-credits-dont-work-deforestation-redd-acre-cambodia/). The Third World people can accept the money, then cut down the trees anyway. Or they can take money for not cutting down trees that they never intended to cut down. Or they can take money from multiple people for not cutting down the same tree. Or they can lie and there were never any trees at all. Offset companies try to watch for these failure modes, but a lot of people are skeptical. Also, even when this represents the true price of offsetting the marginal unit of carbon, it might not scale. You will run out of trees to protect long before you run out of carbon to offset.

“Pessimistic” comes from [Climeworks](https://climeworks.com/), a company that builds giant reverse-factories which take carbon out of the air. If you’re maximally skeptical about any charity's ability to offset CO2, these are the people for you - they can literally hand you a bottle full of the carbon they removed, so you don't need to take anything on faith. But they charge as much as $1000/ton (I think other places charge less, more like $250-500/ton, but they’re still kind of experimental and you personally cannot buy offsets there). You’ll notice there’s more than a whole order of magnitude between the optimistic and pessimistic estimates - welcome to climate economics.

**Cost or value** is kind of hand-wavey. For some things, it's the price of the item - for example, for "train trip LA -> NYC", it's the cost of a cross-country train ticket; for "eat a cheeseburger", it's the price of a Quarter Pounder at McDonalds. Other times it's about making money - for "mine one Bitcoin", it's the value of one Bitcoin (which may be wildly different now than when I wrote this, sorry). For corporations, it's their yearly revenue; for countries, it's their yearly GDP. This isn't very principled and I'm sorry. I included this so I could calculate the %Cost statistic below.

**%Cost** is what percent of the cost/value of something it would take to offset its carbon (I used the geometric mean of the optimistic and pessimistic offset estimates for this, so a little over $100/ton; people could reasonably complain that if you believe normal offsets work, these numbers are all an order of magnitude too pessimistic). A lower number is “better”. If something’s %Cost is 10, it means that it would take 10% of the cost of item to offset the carbon produced. I gave various things whose cost is entirely based on electricity a %Cost of 45, which is the general %Cost of electricity - it will be less in places with more renewables, and higher in places with more fossil fuels. Some of these numbers are kind of arbitrary, and the whole category has weird implications - for example, if the airline company doubled the price of every ticket, their %Cost would go down, and they would look more carbon-efficient. I wouldn't make too much out of these numbers, and I’ve left them in grey to emphasize this.

**Sources** are listed at the bottom of this post. 

This table can’t tell you what your ethical duties are. I'm concerned it will make some people feel like whatever they do is just a drop in the bucket - all you have to do is spend 11,000 hours without air conditioning, and you'll have saved the same amount of carbon an F-35 burns on one airstrike! But I think the most important thing it could convince you of is that if you were previously planning on letting yourself be miserable to save carbon, you should buy carbon offsets instead. Instead of boiling yourself alive all summer, spend between $0.04 and $2.50 an hour to offset your air conditioning use.

But you may not want to literally offset your carbon. I use “offset” here to mean a donation that removes a linear and quantifiable amount of carbon from the atmosphere per dollar. But this is probably a less effective use of money than donating the same amount to a generic anti-climate-change charity. [Clean Air Task Force](https://www.catf.us/) is the one I’ve heard a lot of smart people recommend, though I also donate to speculative carbon removal work like [Project Vesta](https://www.projectvesta.org/). Depending on your philosophy of what offsetting means and when it’s acceptable, you might want to calculate how much it _would_ take to offset your carbon use, then donate it somewhere else instead.

What are the responsibilities of an ordinary citizen facing the threat of climate change? I support [light yokes](https://slatestarcodex.com/2018/11/16/the-economic-perspective-on-moral-standards/); if I had to advise people based on what I learned making this table, I would suggest:

  * Try to stay informed.

  * Elect politicians who take the problem seriously, especially ones who support carbon taxes, cap-and-trade, vehicle emission standards, nuclear and renewable power, closing coal plants as soon as practically possible, and (when ethical) encouraging other countries to do the same. 

  * If you’re otherwise ambivalent between companies (eg Coke vs. Pepsi), patronize ones that try hard to reduce or offset their carbon footprint. 

  * Offset your carbon emissions if you can afford it

  * Consider donating 10% of your income to effective charities, which might include effective climate-related charities like Clean Air Task Force.




I think if you're doing these things, you don't need to obsess too much about which new technology or activity is secretly a Climate Villain, or give up too many of the things that you enjoy. I’ll try to have some more posts soon fleshing out why I think this.

**Sources**

**1.** https://www.science20.com/science_mom/i_wanna_go_green_so_show_me_the_math

**2.** https://www.igs.com/energy-resource-center/energy-101/how-much-electricity-do-my-home-appliances-use

**3.** https://www.energuide.be/en/questions-answers/how-much-power-does-a-computer-use-and-how-much-co2-does-that-represent/54/

**4.** https://www.mentalfloss.com/article/546289/easy-ways-to-reduce-your-carbon-footprint

**5.** http://www.openthefuture.com/cheeseburger_CF.html

**6.** https://native.eco/for-individuals/calculators/#Travel

**7.** https://www.sabaparking.co.uk/news/blog/planes-trains-and-automobiles-the-carbon-most-efficient-way-to-travel

**8.** https://www.buybitcoinworldwide.com/how-many-bitcoins-are-there/, https://www.vox.com/2019/6/18/18642645/bitcoin-energy-price-renewable-china . Like everything else that uses electricity, this is much worse in areas that use fossil fuels and much better in areas that use renewables.

I’d originally included a line for the carbon price of a single Bitcoin transaction, but this was too controversial and philosophically complicated. Individual Bitcoin transactions don’t themselves release carbon, but the Bitcoin network as a whole does, and it exists to support transactions, so in theory you can divide the network cost by the number of transactions to get a per-transaction carbon number, which is something like 1,000 lbs - half the emission cost of a cross-country flight. But many Bitcoin users now use something called the Lightning Network, which is different from the regular blockchain and doesn’t consume much more carbon than other Internet transactions. So one way to look at this is that on-chain transactions are carbon-expensive, and Lightning transactions are cheap. But since neither of them actually costs carbon, I felt weird asserting this, and I just dropped the whole category.

**9.** https://www.edmunds.com/about/press/leaf-blowers-emissions-dirtier-than-high-performance-pick-up-trucks-says-edmunds-insidelinecom.html

**10.** https://iopscience.iop.org/article/10.1088/1748-9326/4/2/024008/pdf . I'm using their on-peak time because I'm assuming the average 20 mile bus trip is a commute. The paper claims that under some reasonable ways of thinking about things, taking the bus off-peak is actually more polluting than taking a car, because we're imagining eg an entire bus with you as the only passenger, which requires more carbon than an entire car with you as the only passenger. This seems a little hokey, because the bus is going to run its route whether you're on it or not, but it's a natural consequence of dividing the carbon cost of the bus by number of passengers and assigning you your "share", which seems like the right way to handle peak times. Since I've used their peak numbers, this methodological dispute doesn't affect my table.

**11.** https://www.carbonbrief.org/factcheck-what-is-the-carbon-footprint-of-streaming-video-on-netflix

**12.** https://www.theregister.com/2020/11/04/gpt3_carbon_footprint_estimate/

**13.** https://www.statista.com/statistics/531531/carbon-emissions-worldwide-walmart/, https://corporate.walmart.com/our-story/our-locations. Divide ~20 million tons per year by ~10,000 stores.

**14.** https://www.treehugger.com/spacex-launch-puts-out-much-co-flying-people-across-atlantic-4857958

**15**. https://www.sciencefocus.com/future-technology/how-many-cars-equal-the-co2-emissions-of-one-plane/

**16.** https://www.thetimes.co.uk/article/co2-challenge-that-towers-over-tall-buildings-9x3jzn5s3

**17.**[removed]

**18.** https://grist.org/article/the-department-of-defense-wants-to-protect-itself-from-climate-change-threats-its-helping-to-spur/, https://paullaherty.com/2015/01/10/calculating-aircraft-co2-emissions/ . I am assuming a mission involves using all the fuel in the fuel tank.

**19.** http://www3.cec.org/islandora/en/item/2165-north-american-power-plant-air-emissions-en.pdf . The coal number is from Bowen, the largest coal plant in the US. The natural gas number is from Martin, a comparably-sized natural gas plant. 

**20.** https://www.vox.com/2014/7/2/5865109/study-going-vegetarian-could-cut-your-food-carbon-footprint-in-half. I rounded up quite a bit to adjust for Americans eating more meat than British people.

**21.** https://www.carbonbrief.org/factcheck-how-electric-vehicles-help-to-tackle-climate-change, https://www.caranddriver.com/research/a32880477/average-mileage-per-year/

**22.** https://native.eco/for-individuals/calculators/, where SUV is "light truck" and generic car is "medium gasoline automobile", using the 13500 mile/year number.

**23.** https://www.ccfpd.org/Portals/0/Assets/PDF/Facts_Chart.pdf

**24.** Sources conflict a lot here, probably because a lot depends on what you hold constant (eg if you move from the suburbs to the city while keeping the same sized house and car, you might not save much carbon, but realistically city-dwellers have smaller houses and cars). The extreme low estimate is represented by https://www.bloomberg.com/news/articles/2013-08-22/suburbs-might-be-just-as-green-as-cities , which is not sure suburbanites emit any more carbon at all, because suburban households are larger and so their carbon expenses (like heating, cars, etc) are divided over more people when producing a per capita estimate. But a very literal estimate - taking the average carbon output of an urbanite vs. a suburbanite - produces high numbers more like the one I listed. For example, https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_carbon_dioxide_emissions claims that Washington DC inhabitants produce only 4 tons of carbon yearly, much less than the US standard of 16; NYC claims its residents only produce 6 tons. I've backed off slightly from these estimates to reflect uncertainty and the fact that most cities are less dense than NYC and DC.

**25.** Most media treatments of this question say that having a child produces 60 tons extra carbon per year, which is strange - the average adult produces only 20, so why would children be three times as polluting as adults? I eventually tracked down the source of this estimate to https://sci-hub.st/https://www.sciencedirect.com/science/article/abs/pii/S0959378008001003 , which is a paper arguing that your children will someday have children of their own, and those children will have children of _their_ own, and so on, and all of this should be counted against you personally for deciding to have the first child in the chain. If the chain continued indefinitely, it would cost infinite carbon, but the authors conveniently assume that fertility rates will gradually decline, and everything will converge to some large but finite number of people. Then they calculate how much carbon all those people will produce under various implausible assumptions about the far future, divide it by your 80-something year lifespan, and say having a child produces 60 tons extra carbon per year of your life. 

I can see reasons you might want to think that way, but I can see much better reasons you _wouldn't_ want to think that way, so I will be trying to figure out the actual amount of carbon produced by an actual child in an actual year. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0231105 suggests households with children produce about 1500 lbs more carbon than those without. Each child-having household has on average two children, so even though it's probably not completely linear let's say 750 lbs/kid. Americans produce about 3x as much carbon as Swedes, so assuming this stays constant I would expect US children to produce 2250 lbs. That matches the numbers on the graph at https://green.blogs.nytimes.com/2011/11/10/if-you-act-your-age-whats-your-carbon-footprint/ . So I think the amount of carbon emitted by a child is around 2250 lbs on average.

Is it unfair to make this our final number? After all, eventually that child will grow up and produce more carbon, and it will still be your fault for giving birth to them. I am optimistic that in 2040 when your children are grown up enough to produce normal adult levels of carbon, normal adult levels of carbon will be much lower and offset prices will be much cheaper. If, when your child is an adult, average carbon emissions are 7.5 tons/person (half of today), and direct air capture carbon offsets cost $50/ton (5% as much as today, see [here ](https://sci-hub.st/https://www.sciencedirect.com/science/article/pii/S0959652619307772)for source of prediction that this will happen) then when your child is an adult, the offset should cost if anything less than it does now. Also, when your child is an adult, they will be making money themselves and you can at least hope they will offset their own carbon.

**26.** https://www.bloomberg.com/news/articles/2020-10-05/exxon-carbon-emissions-and-climate-leaked-plans-reveal-rising-co2-output

**27.** https://apnews.com/article/95986c4ba779f1d35ac4ca2afdd745c3

**28.** https://services.google.com/fh/files/misc/google_2019-environmental-report.pdf

**29.** https://grist.org/article/u-s-military-emits-more-co2-than-most-countries/

**30.** https://www.engineeringnews.co.za/article/ford-hits-carbon-emissions-reduction-target-eight-years-early-2018-07-27/rep_id:4136 . Good information on Ford was hard to find, but I'm calculating this based on their claim that they reduced emissions by 3.2 million metric tons and this corresponds to reaching their goal of decreasing emissions by 32%. That suggests their original emission level was 10 million tons and so their remaining level is 6.8 million tons. This is just their manufacturing emissions - it doesn't count emissions from the cars they make.

**31.** https://www.tesla.com/ns_videos/tesla-impact-report-2019.pdf . This seems bizarrely low, but https://www.bloomberg.com/news/articles/2019-04-17/tesla-s-first-impact-report-puts-hard-number-on-co2-emissions seems to confirm that it's much less than other companies'. 

**32.** https://apnews.com/article/384fdb5ee7654667b53ddb49efce8023

**33.** https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions

**34.** https://www.sciencedaily.com/releases/2019/06/190613104533.htm

**35.** https://www.mta.info/press-release/mta-headquarters/mta-prevents-greenhouse-gases-17-million-metric-tons-annually

**36.** https://ourworldindata.org/co2-emissions

**37.** https://www.iea.org/commentaries/the-carbon-footprint-of-streaming-video-fact-checking-the-headlines

**38.** [removed]

**39.** https://www.theguardian.com/science/2021/jul/19/billionaires-space-tourism-environment-emissions , https://www.space.com/virgin-galactic-raises-space-ticket-price

**40:** https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle
