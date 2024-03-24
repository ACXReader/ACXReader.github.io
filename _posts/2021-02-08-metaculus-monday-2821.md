---
title: "Metaculus Monday 2/8/21"
subtitle: "Two more prediction markets, plus AI"
date: 2021-02-08
likes: 62
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/32257019/comments?&all_comments=true
image: https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/64c0705b-004a-4b01-861b-a00c1513fb5e_248x248.png
original-url: https://www.astralcodexten.com/p/metaculus-monday-2821
---
Thanks to everyone who commented last week with prediction markets I missed. Two of them seemed to be especially interesting.

**[Polymarket](https://polymarket.com/)** is another cryptocurrency-based prediction market. It's got about two dozen contracts open, and some of them are pretty big - $5 million plus! With that kind of money, we ought to be seeing some really good predicting! We're...not. Either there's a 6% chance that Donald Trump will be president again by March 31, or something's gone wrong. 

Probably it's the second one. I tried to bet against Trump, but getting money into the market was pretty hard. You need USDCoins, a stablecoin related to Ethereum. Polymarket tries to let you buy them directly, but their app wanted me to give them a security code which never showed up, so I gave up on this. Instead I bought some USDC at Coinbase and tried to send them over. But along with the usual Ethereum gas fees, they have something called a relayer, which is supposed to collect my money and put it in my account. And it's apparently heavily backed up, and after two days my money is nowhere to be seen (though I believe them [when they say](https://polymarket.medium.com/polymarket-relayer-community-announcement-31ac3b64c09d) that they're trying their hardest and it will probably percolate through the Ethereum network someday). Maybe everyone's having these kinds of issues and this is why the Trump contract hasn't adjusted? I'm not sure. I will keep you updated if my money ever materializes.

**[Kalshi](https://kalshi.com/)** is "the first regulated futures exchange dedicated to trading on event outcomes". As far as I can tell they actually did it. They got the government to agree to let them run a prediction market, regulated as investing rather than gambling. There will be a $25,000 max on contracts, so it might not be enough for the real whales, but that's still thirty times higher than existing prediction markets and enough to probably be a sea change. I talked to a representative who said they'll be "focused on creating markets in a few key categories such as climate, economics, geopolitics, energy, education, government, space, COVID, and technology", but that they remain open to potentially expanding to all sorts of other areas ([except onions,](https://en.wikipedia.org/wiki/Onion_Futures_Act) which apparently have a very specific carve-out as something which it is illegal to have futures markets about, somebody please write a cyberpunk novel revolving around this). So far they're still setting things up, but they describe themselves as "ramping quickly towards launch". I am super psyched about this and will keep you all updated.

Getting back to **[Metaculus](https://www.metaculus.com/questions/)** , let’s look at what they’ve got on AI:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F29d3cefe-10fa-400d-accb-e8a417313844_1043x214.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F29d3cefe-10fa-400d-accb-e8a417313844_1043x214.png)

First, some history. In 2016, DeepMind’s AlphaGo beat first Fan Hui, a medium-level professional Go player, and then Lee Sedol, a top professional Go player. This was one of the more unexpected events in AI history; everyone thought it would be a few more years before Go AIs were ready for prime time. We can see this on Metaculus; their prediction that a Go program would beat a professional went from 30% before the Fan Hui match to 90% afterwards (there was some debate on whether the Fan Hui match was official enough to count, so it wasn’t 100, but everyone agreed that beating Fan Hui meant the program could probably beat other people in more official settings.  
  
After that people thought it was moderately likely AlphaGo could beat Lee Sedol too, and they were right.

Prediction markets clearly aren’t magic; they didn’t expect AlphaGo’s victory over Hui any more than anyone else did (maybe a little more than some other people? they did give it 30%). But it’s interesting being able to quantify the exact degree to which people thought it was unlikely at the time, and when exactly that changed. 

Imagine how great this sort of thing will one day be for historians. With enough skill, you can sort of wring prediction markets out of history - [the price of Confederate bonds in early 1863 ](https://www.nber.org/system/files/working_papers/w13567/w13567.pdf)implied that investors thought the South had a 42% chance of winning the Civil War. But future historians will be spoiled; the numbers will be right there for them.

Moving on:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F24018e51-5fc6-47a7-8842-dcc96ff01564_868x178.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F24018e51-5fc6-47a7-8842-dcc96ff01564_868x178.png)

Well, that escalated quickly!

[The question](https://www.metaculus.com/questions/3479/when-will-the-first-artificial-general-intelligence-system-be-devised-tested-and-publicly-known-of/) defines “first AGI” as an AI system that can pass the Turing Test, get a score of 600+ on the math SAT, do well on the Winograd Challenge (a set of language comprehension problems), and play the classic AI test video game Montezuma’s Revenge, without needing excessive training data, and in some kind of unified way (ie it isn’t just four different ad hoc AIs cobbled together). This is an easier problem than “be fully human level intelligent”, but it would have to have some kind of impressive general intelligence to succeed at so many unlike domains. 

Metaculus predicts it’ll happen in 2036, but notice the shape of the curve (same curve shown as cumulative probability below):

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F60698b44-9657-4dd0-abfb-fe014a7c3d4c_930x310.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F60698b44-9657-4dd0-abfb-fe014a7c3d4c_930x310.png)

10% chance it happens within a few years, and another 10% chance it takes more than a century. 50% range is between 2029 and 2059. 

Moving on:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1ab0ae9-c05e-4c39-ac43-3ce0e2083630_527x237.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1ab0ae9-c05e-4c39-ac43-3ce0e2083630_527x237.png)

This strikes me as a much bolder prediction than the above. The [situation they’re imagining](https://www.metaculus.com/questions/384/human-machine-intelligence-parity-by-2040/) is that a group of smart human expert interviewers communicates by text with two parties. One party is an AI pretending to be a smart human scientist, the other party is an actual smart human scientist. Both groups have Internet access (but can’t cheat by emailing other humans for help). So basically a Turing Test. If the interviewers can’t figure out which is which, that’s “human-machine intelligence parity”.

This still wouldn’t necessarily mean AIs can take over from humans; humans can do lots of things other than answer questions. But it suggests users weren’t kidding when they predicted AGI by 2036.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2d46185-7df2-4f78-ad4c-3305385f3010_1019x214.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2d46185-7df2-4f78-ad4c-3305385f3010_1019x214.png)

[These ](https://www.metaculus.com/questions/736/will-there-be-a-complete-4-year-interval-in-which-world-output-doubles-before-the-first-1-year-interval-in-which-world-output-doubles/)are kind of weird ones, but they’re in line with the way that a lot of AI risk experts have been talking about takeoff speed. Regarding the one on the left: they’re assuming that a superintelligence would massively increase world GDP, because a superintelligence could probably invent cheap fusion, nanobots, etc. So in a hard takeoff scenario - where it’s business as usual and then someone invents a complete recursively self-improving superintelligence in their basement - we would go from normal GDP growth to sudden extreme GDP growth really fast. In a slower takeoff scenario, we’d go from IQ 100 AIs to IQ 110 AIs to IQ 120 AIs […] and never have a sharp transition to superintelligence. Here there would be a gradual speedup in GDP growth ending with the kind of super-high growth you’d expect from fusion and nanobots.

Right now world GDP doubles every 20 years. So this is asking whether we will see a period of merely super-high GDP growth (doubling every 4 years) before we see a period of absurdly high GDP growth (doubling every 1 year). A yes answer means superintelligence won’t come as a complete surprise and takeoff won’t be too fast. Forecasters lean towards yes, but not especially confidently.

The one on the right is pretty weird. Right now world GDP is 80 trillion dollars. It’s forecast to reach maybe 200 trillion dollars by 2050. Forecasters have already said they’re expecting AGI in the 2035 - 2040 range. So this is saying they’re expecting world GDP to be much, much higher than business as usual. Presumably some AI-related advance short of AGI would cause an unprecedented world economic boom. I am pretty skeptical of this because there have been a lot of weird unprecedented things in economic history and they have never caused that severe a discontinuity. Looking at the distribution, I see most people agree with me and are predicting somewhere in the 100 - 200 trillion range, but other people are saying really far out there things and it all averages out.

Less weird, and closer to home:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fae9db53d-6588-4e6a-aefc-eb8bfcd27bbf_478x221.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fae9db53d-6588-4e6a-aefc-eb8bfcd27bbf_478x221.png)

The framing is confusing - a yes answer to [this question](https://www.metaculus.com/questions/5118/will-robin-hanson-win-a-bet-that-the-gpt-line-of-language-models-will-generate--1bn-in-customer-revenue-by-2025/) means that GPT will _not_ produce this much revenue this quickly. Forecasters seem pretty split here. I agree this isn’t a very obvious question and that $1 billion is a reasonably point at which to be 50-50.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1929770d-a9f2-40d4-a9eb-ef09b157c3b8_404x182.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1929770d-a9f2-40d4-a9eb-ef09b157c3b8_404x182.png)

[This is](https://www.metaculus.com/questions/5587/ai-ny-times-best-seller-before-2030/) a pretty wild thing to expect before 2030. I can imagine that AI becomes good enough that a gimmick “this book is by an AI!” book isn’t unreadable, and maybe people buy it for the novelty value. I think I’d still put this closer to 20% than 35%.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4aeb74dd-f8e3-4e91-aab2-52bd5923093d_400x180.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4aeb74dd-f8e3-4e91-aab2-52bd5923093d_400x180.png)

[This is another](https://www.metaculus.com/questions/1394/will-ai-progress-surprise-us/) fun “pushing the envelope of what you can do with prediction markets” one. It refers back to the question about human-machine intelligence by 2040, and asks whether the Metaculus average prediction on that question will triple within a month (the math around what it means for odds to triple is complicated; one example would be going from 60% to 81.8%). This suggests that some sort of surprising thing happened that immediately changed the views of many Metaculus forecasters. It’s another way of getting at the incremental progress vs. sudden takeoff question. A really interesting way. You can do a lot once you have a prediction market quantifying your odds of something!

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5f5a6984-c6c3-4849-b57d-20de3facee80_879x210.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5f5a6984-c6c3-4849-b57d-20de3facee80_879x210.png)

I don’t know anything about these, sorry. I’m including them kind of as penance. I’m an ignorant and easily-excited person, so I’m focusing on the dramatic questions like when AI will achieve general intelligence or quadruple the economy. But you can also find a lot of Metaculus bread-and-butter questions about when such-and-such a system will meet such-and-such a benchmark, or how many parameters it will take, or things like that. If you are a reputable down-to-earth AI scientist, please don’t let me keep you from checking Metaculus. There are enough questions about object recognition benchmarks and so on to satisfy even the most dignified and well-grounded people.

See [a list of all of Metaculus’ AI-related questions here.](https://www.metaculus.com/questions/?search=cat:comp-sci--ai-and-machinelearning)
