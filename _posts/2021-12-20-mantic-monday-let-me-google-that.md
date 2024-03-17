---
title: "Mantic Monday: Let Me Google That For You"
subtitle: "Plus options, prisons, obesity, and human sacrifice"
date: 2021-12-20
likes: 41
original-url: https://www.astralcodexten.com/p/mantic-monday-let-me-google-that
---
### Let Me Google That For You

New from Google this month: [Creating A Prediction Market On Google Cloud](https://cloud.google.com/blog/topics/solutions-how-tos/design-patterns-in-googles-prediction-market-on-google-cloud). Google announces that they’ve been running an internal prediction market for the past year, with “over 175,000 predictions from over 10,000 Google employees”.

[![1 Predictive analytics.jpg](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa715dfc3-a889-4bf5-809a-a71211b58cc3_800x466.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa715dfc3-a889-4bf5-809a-a71211b58cc3_800x466.jpeg)

Most of it’s classified because they’re predicting stuff about Google’s corporate secrets, but some friendly Googlers were at least willing to walk me through the article and clarify pieces I didn’t understand.

The market, called Gleangen, is actually the second prediction market Google’s tried. The first, in 2007, was called Prophit - the team included occasional ACX commenter Patri Friedman, who’s since moved into the charter city space.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6a726314-adbb-43b5-acf0-8d93921b7bf7_647x272.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6a726314-adbb-43b5-acf0-8d93921b7bf7_647x272.png)([source](https://liberdon.com/@patrissimo/105152785611761192))

Prophit wound down because the founders left and nobody really knew what to do with; you can read about some of their findings [here](http://www.eecs.harvard.edu/cs286r/courses/fall10/papers/GooglePredictionMarketPaper.pdf). In 2020, with all the uncertainty around coronavirus, some Googlers decided to try again. Gleangen is the result. 

Unlike most prediction markets, anybody can create a question on Gleangen. This usually goes badly: most people are terrible at writing questions with objective resolutions. Google manages by having a dedicated team of moderators who go over everything and amend it when needed. The market pays out in play money and the right to be [on a leaderboard](https://news.ycombinator.com/item?id=28538693#28540607).

So far it’s not doing much else. The Googlers I talked to saw no evidence that company executives were paying much attention to it when making decisions. Why not? Hal Varian, Google’s chief economist, said in a [Conversation](https://conversationswithtyler.com/episodes/hal-varian/) with Tyler Cowen:

>  **COWEN:** Why doesn’t business use more prediction markets? They would seem to make sense, right? Bet on ideas. Aggregate information. We’ve all read Hayek.
> 
>  **VARIAN:** Right. And we had a prediction market [referring to Prophit in 2007]. I’ll tell you the problem with it. The problem is, the things that we really wanted to get a probability assessment on were things that were so sensitive that we thought we would violate the SEC rules on insider knowledge because, if a small group of people knows about some acquisition or something like that, there is a secret among this small group.
> 
> You might like to have a probability assessment of whether that would go through. But then, anybody who looks at the auction is now an insider. So there’s a problem in you have to find things that (a) are of interest to the company but (b) do not reveal financially critical information. That’s not so easy to do.

Is anyone doing anything with the market’s predictions? The most popular use case seems to be Google employees trying to get a sense of when they’ll have to work from home vs. come into the office, though there also seem to be a few cases of individuals consulting it for other career-relevant decisions.

There aren’t a lot of great ways to test Gleangen’s accuracy, but the article at least included a basic calibration graph:

[![3 Predictive analytics.jpg](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe308b9fc-0245-4e30-89b5-8e7a36f45a50_700x254.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe308b9fc-0245-4e30-89b5-8e7a36f45a50_700x254.jpeg)

With the lack of graph labels, I’m having trouble telling if this represents overconfidence or underconfidence, but it’s definitely _something_. If this was a real-money market I would expect someone to have arbitraged this out.

The article ends by suggesting if you contact Google maybe they’ll help you build an internal prediction market for your organization. They’re pretty vague about it, but you can read the [application form](https://docs.google.com/forms/d/e/1FAIpQLSdCXkcgB13FWhdCvOM81m1BNA5VkBKdrt0Pah8k7B5M66EmAg/viewform) to at least get a sense of what they’re thinking.

### Looking For Options

Continuing a thread here from the last few posts:

Suppose you want to predict something in 2100. It’s hard. Nobody wants to lock their money up for 80 years to get a 5% or 10% or even a 100% rate of return. You can slightly alleviate the problem by having the prediction market put the money in index funds while you wait, but anyone with hopes of beating the market probably wants to beat it by more than 5% per hundred years.

One option we talked about last time is chained prediction markets. A prediction market today on what a market will say in 2025 on what a market will say in 2030 about what a market will say in […] about what a market will say in 2100. The active ingredient of this seems to be magnifying small fluctuations: if the event is 50% likely today, you can bet on whether it will be between 45%-49.9% likely in 2025 vs. 50% - 55% likely, or whatever.

Many people pointed out that this is equivalent to having a single prediction market operating from now until 2100, where you can buy options at any time (ie an option that the prediction market will be above 51% in one year). That seems right.

My next question is: is there a structure where options directly move the market? The whole point of prediction markets is that their prices correspond to the chance of something happening. But if nobody is buying shares directly and all the action is in options trading on the side, that won’t work. Here I admit I don’t know much about markets or options - is there some way to combine regular trading and options trading into a single price, so that we could get the advantages of options trading, but traders would still be betting on the regular market and increasing our predictive accuracy?

### Prison Conditions

One of Robin Hanson’s original dreams for prediction markets was conditional markets that could help set policy. For example “If we choose a left-wing Education Minister, what will test scores be in five years?” vs. “If we choose a right-wing Education Minister, what will test scores be in five years?” and then we have a good guess as to whether the left-wingers or right-wingers have better education policy on this axis.

I rarely see people trying this, but here’s an exception from Metaculus (h/t [Nathan Young](https://policyforecast.substack.com/p/uk-policy-forecast-4-prisons-london)):

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F792e86c8-c9ad-42e3-bb92-bc489090910a_724x503.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F792e86c8-c9ad-42e3-bb92-bc489090910a_724x503.png)

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd95adbeb-9630-4d31-b110-784cf3d24f5f_769x495.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd95adbeb-9630-4d31-b110-784cf3d24f5f_769x495.png)

So the market predicts that Conservatives will put slightly more people in prison than Labor.

I don’t think this is interesting? Conservatives are right-wing and probably do the Tough On Crime thing. Labour is left-wing and probably does the End Mass Incarceration thing. You’re not really learning anything you wouldn’t have guessed otherwise. But it’s a proof of concept. You could do this for GDP growth, school test scores, and all the other things where we all agree what the good outcome is.

I don’t know, maybe you wouldn’t learn anything there either. If Conservatives had better GDP growth, maybe leftists would say “of course, they’re the more capitalist party, they trade off environmental damage and inequality for a slightly hotter economy”. If Labour had better test scores, maybe rightists would say “of course, they’re the more socialist party, they’ll tax you dry and throw some of the money at schools but it will still be inefficient.” But it would be an interesting experiment, and maybe put the size of the tradeoff into relief. I bet a lot of people would care a lot if the conservatives could produce 0.01% higher GDP growth vs. 5%.

### Fat Tails

Nutritionist Stephan Guyenet has a great article out on the new generation of weight loss drugs. He thinks that semaglutide is only the beginning, and we’re entering a brave new world of diet pills that really work.

Why am I mentioning this here? [His essay is on Metaculus](https://www.metaculus.com/notebooks/8702/the-promise-and-impact-of-the-next-generation-of-weight-loss-drugs/). It’s the latest in their line of “fortified essays”, a new genre they’re trying to create of argument backed by prediction markets and crowd forecasting.

So for example, when Stephan talks about the promise of two new research chemicals, tirzepatide and bimagrumab, he’s able to punctuate his points with these graphs:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5c0fe029-18be-424e-9111-007c98364e06_819x223.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5c0fe029-18be-424e-9111-007c98364e06_819x223.png)

Note the “community predicts” and “author predicts” captions at the bottom. In this case, we can tell that Guyenet is sticking to the market’s consensus in everything he says (or that the market blindly believes Guyenet, which is also valuable to know). If he wanted to go out on a limb and disagree with the market, he could do that too.

Sometimes these predictions add some pretty relevant context. For example, after going into great detail about how many exciting new weight loss drugs we’re going to have soon, and supporting each of his points with a forecasting tournament that shows Metaculans agree with him, he ends on this note:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F898f0b42-9728-4274-b76e-cb03aa1e92bb_409x307.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F898f0b42-9728-4274-b76e-cb03aa1e92bb_409x307.png)

Metaculus [thinks](https://www.metaculus.com/questions/8634/american-obesity-percentage-in-2032/) that despite all this great science, more Americans than ever will be obese in ten years (for context, 43% are obese today). 

Guyenet defies the market here. His distribution peaks around 35%, so he really believes things are going to get better (though you can tell he has low confidence, and also assigns decent probability to things getting worse). If I’m still writing these newsletters in ten years, remind me to revisit this!

You can read more fortified essays about [solar power](https://www.metaculus.com/notebooks/8938/solar-power-current-challenges-encouraging-progress/), [monetary policy](https://www.metaculus.com/notebooks/8340/beyond-benchmark-rates-how-modern-central-banks-tighten-monetary-policy/), and [interstellar objects](https://www.metaculus.com/notebooks/8812/the-%25CA%25BBoumuamua-paradox-and-the-nature-of-interstellar-objects/), among others.

By the way, if you’re a journalist, I think one of the most useful things you could do in this space right now would be to publish a fortified-style essay in a major publication. If you’re nervous getting in touch with Metaculus and would prefer that I introduce you, send me an email at scott@slatestarcodex.com.

### This Week In Markets

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2c62f48-a54b-47d0-850c-b41087332ab7_762x390.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2c62f48-a54b-47d0-850c-b41087332ab7_762x390.png)

Metaculus thinks hospital admissions this winter (ie from Omicron) will peak mid to late January. Since it takes a week or two for a COVID case to end up in the hospital, this implies Omicron infections will peak mid-January. 

That peak at the end is weird-looking and shows up on many Metaculus questions. I think this is something like all dates after April 1 getting crammed into April 1 for the graph, and even though very few people think it will be after April 1, that’s still a really high number of guesses when it’s all concentrated into an individual day. It’s weird and I wish they would find a way not to do that.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F29fb7757-c370-4bca-9fe3-c5956b80b4f9_767x443.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F29fb7757-c370-4bca-9fe3-c5956b80b4f9_767x443.png)

Colleges are ditching the SAT as an admissions criterion in favor of what opponents would describe as doubling down on legacy admissions, class-based connections, and racism. How far will this process go? Right now, 16% of top colleges don’t require test scores. Metaculus expects that by 2030 it will be 70%.

If we look at the distribution, we get a clearer view:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37895685-cea8-4f0b-b060-fd33e65c387e_763x293.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37895685-cea8-4f0b-b060-fd33e65c387e_763x293.png)

Lots of people think it will be 100%, with a long tail of people predicting various other things.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5ee958ec-4a64-43be-ac1d-47476863ab6f_768x379.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5ee958ec-4a64-43be-ac1d-47476863ab6f_768x379.png)

Will small modular nuclear reactors provide more than 1% of any country’s energy in 2030? Metaculus thinks probably not.

### Shorts

 **1:** Richard Hanania [interviews Robin Hanson](https://richardhanania.substack.com/p/futarchy-robin-hanson-on-how-prediction), inventor of prediction markets.

 **2:** Interesting new prediction market [Futuur](https://futuur.com/), I haven’t investigated it yet but I appreciate their silly pictures representing possible outcomes:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa240a599-867a-497e-ab04-73abacd80472_478x291.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa240a599-867a-497e-ab04-73abacd80472_478x291.png)

 **3:** Wikipedia: [Cimbrian Seeresses](https://en.wikipedia.org/wiki/Cimbrian_seeresses). “The seeresses led prisoners of war up a platform where they cut their throats and watching the blood stream down into a cauldron they made predictions about the future.” I’m tempted to disapprove of this, but first I want to know if they made it onto the Metaculus leaderboard.
