---
title: "Mantic Monday: Scoring Rule Controversy"
subtitle: "..."
date: 2021-03-01
likes: 46
original-url: https://www.astralcodexten.com/p/mantic-monday-scoring-rule-controversy
---
**Metaculus scoring rule controversy**

Zvi considered using some Metaculus markets for his weekly coronavirus roundup, but was [turned off by the scoring rules](https://www.lesswrong.com/posts/PQACEuWpkSyRgHC4p/covid-2-11-as-expected). 

Ross Rheingans-Yoo [writes about the issue here](https://blog.rossry.net/metaculus/). Everyone agrees Metaculus’ scoring rule is “proper”, a technical term meaning that it correctly incentivizes you to choose the probability you think is true. Zvi and Ross’s objection is that it doesn’t correctly incentivize you about whether to bet at all, or how much effort to put into betting. 

For example, on many questions, you can make guaranteed-positive bets - you’ll gain points on the prediction even if you were maximally wrong. If you were trying to maximize your Metaculus points, you would bet on all of these questions. If you were trying to maximize your Metaculus points in a limited amount of time, you might even bet on them without investigating at all. The person who spends one second picking a random number on a thousand questions will get more points than someone who spends an hour researching a really good answer to one question.

This is the opposite of a real prediction market like PredictIt, where you only make money if you beat the average person betting on the question. If you spent one second picking a random number on a thousand PredictIt markets, you would lose lots of money. If you spent an hour researching a really good answer to one question, you would have a chance to beat the market and win. 

So PredictIt incentivizes you to add information - to only bet when you are smarter than the market’s previous consensus. Metaculus incentivizes you to subtract information - even if the market was previously smart, dumb people should come in, shift it in a random direction, and move on.

In response to these concerns, Metaculus founder Anthony Aguirre published [A Primer On The Metaculus Scoring System](https://metaculus.medium.com/a-primer-on-the-metaculus-scoring-rule-eb9a974cd204). His argument is: the more predictions people make, the more useful Metaculus is. Having a very slightly positive-sum scoring rule (ie one where on average you gain points by making a prediction) encourages people to make lots of predictions. Because of how the positive-sum rule is implemented, on some very specific questions you will always get points even if you’re maximally wrong (although not always). You’ll still get many more points if you’re right. This most effectively produces the desired result: users make many predictions, but also try hard to get them right. 

If you are spamming the questions to maximize points, the best strategy is to spam the existing prediction - ie if everyone else’s predictions average 35.8%, you should predict 35.8%. That means spammers don’t hurt accuracy; the prediction stays where it already was. It does make the prediction seem unnaturally confident (“a thousand people all said it was exactly 35.8%!”) but they are working on ways to prevent this. 

I find this a bit reassuring, but I still feel disincentivized to participate when I think about how my careful guesses net me less points than doing some sort of boring spamming strategy I’m not really going to do. I don’t think Metaculus considers accurately ranking people by predictive skill an especially high priority compared to actually important things like getting good predictions, and that’s fine, but it kind of sucks for people who were motivated by a competitive streak (but who aren’t _quite_ competitive enough to work out the best way to spam questions).

 **In the long run, are we all dead?**

Last week a commenter asked: how do you make a prediction market for something 50 years out? 100 years out?

First problem: if you win in 100 years, aren't you too dead to enjoy the money? Some corporations might last 100 years, but their CEO and stockholders probably want good returns during their lifetimes, so that doesn't help much.

This is a genuinely hard problem, but one answer is that you can make a profit before the predicted event happens. Suppose you're betting on the question "will global temperatures go up by at least 2 degrees between 2021 and 2121?". You buy a "yes" share for 50 cents, based on your model saying temperature will go up 0.05 degrees per year. Someone else buys a "no" share for 50 cents, based on their model saying temperature will go up 0.01 degrees per year. In the ten years between now and 2031, temperature goes up 0.05 degrees every year. The price of your "yes" share goes to 80 cents, since people have gotten more convinced that temperature will have increased at least 2 degrees by 2121. You sell it to someone else who has a different case (maybe that even your current model is underestimating the risk of global warming) and pocket your 30 cent profit after only 10 years.

This only works if information trickles out over time - as opposed to becoming clear just before the end date. Most real questions are a combination of both. So for example, "which party will win the 2100 presidential election?" might change a little over the next 80 years as (for example) demographic change makes one or another party permanently stronger or weaker. Maybe it could change even more if one of the parties collapses and is replaced by a different party. But most of the signal will come in 2099 when we see who the candidates are and how they poll. Problems where almost all the new information happens in the far future are a bad match for prediction markets.

If we have this sort of problem, how could we solve it? Maybe we should drop the simplifying assumption that people are only motivated by money or reputational gain. Metaculus has lots of predictions about 2100 and beyond, and lots of people have made forecasts for them. Because Metaculus collects people's win-loss records on recent predictions, they can ask their model "What do the subset of people who are most often right about near-term predictions think of this long-term prediction?" This isn't perfect, but it might be better than nothing.

Second problem: if you bet on a 50-50 outcome and get proven right in 2121, you've made 100% returns over 100 years. The stock market could easily make 10,000% returns over that time period, so why would you ever play the prediction markets instead?

[This paper](http://ubplj.org/index.php/jpm/article/view/592) in the _Journal Of Prediction Markets_ (which apparently exists!) suggests what I think is the obvious solution. The prediction market puts your investment in an index fund. When you win, they give you your winnings, modified by the amount they've grown in the index fund over that time. Doing this is better than not doing it, but I'm still not convinced it gets you to 2121. If the stock market goes up 5% per year on average, then in 100 years you make 131x returns. If you add in a prediction market where you corrected a 5% mispricing, that brings your returns up to 138x. But if instead you put your energy into finding stocks that went up 6% per year on average, you would make 339x returns. I don't know how many people are going to care about getting 138x returns instead of 131x returns in 100 years, especially when there's an opportunity cost of trying to beat the market some other way.

I think probably prediction markets will lose a lot of reliability and precision beyond a few decades. Here's a pessimistic way to think about this: even if we somehow found a way to make the incentives line up perfectly, could this perfect prediction market really predict things beyond a few decades anyway? A lot of the trouble seems to be fixing eg 5% mispricings. But if your plan requires knowing the value of some parameter to within 5% several decades from now, probably you should get a different plan.

Or here's a more optimistic way to think about this: if we can get good short-term and medium-term prediction markets, we'll learn a lot about forecasting and who's good at it. Then we can ask those same people to make long-term predictions pro bono, or for a flat fee. Even if there were some industry that (for some reason) couldn't issue stock or participate on the stock market, I would trust Wall Street to be able to apply the techniques it's learned playing the stock market to predict trends in that industry too. In the same way, whatever the prediction market's version of Wall Street is will probably be good at things beyond just playing prediction markets.

 **Short Links**

Someone alerted me to the [Foresight Exchange](http://foresightexchange.com), an old-school prediction market operating since 1996! I’m trying to make sense of their “[Will The US Government Collapse By 2025?](http://foresightexchange.com/fx-bin/Claim?claim=USgn)” question, which records some interesting changes in perception of US government stability between 1996 and today. But why is it still at 20%? I’m not sure about this, but I think it’s because one of the valid signs of collapse was “US dollar becomes so devalued that gold is worth $2500/ounce” - gold is currently worth $1700/ounce, and 20% chance for $2500 by 2025 seems plausible. Let this be a lesson to be very careful about what numbers you put in a prediction you’re going to have to judge 30 years later.

[Metaforecast](https://metaforecast.org/) is a prediction market search engine. So if you want to see what every prediction market has to say about Trump, you can search “Trump” and get all relevant markets. In theory. In practice it still has a way to go in terms of delivering relevant things and avoiding irrelevant things.

This week in Metaculus: [69% chance](https://www.metaculus.com/questions/6506/10x-abortion-in-poland-by-2030/) Polish abortion rate will dectuple by 2030 (why? they seem pretty conservative; is their conservatism that precarious?) [70% chance](https://www.metaculus.com/questions/4816/will-derek-chauvin-be-acquitted-of-all-murder-charges/) the officer accused of killing George Floyd will get acquitted of murder. [45% chance](https://www.metaculus.com/questions/6656/tether-in-2021/) Tether will collapse by the end of 2021. 
