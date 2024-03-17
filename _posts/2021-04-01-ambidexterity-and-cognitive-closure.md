---
title: "Ambidexterity And Cognitive Closure"
subtitle: "Are ambidextrous people really less authoritarian? Or just less conformist?"
date: 2021-04-01
likes: 71
original-url: https://www.astralcodexten.com/p/ambidexterity-and-cognitive-closure
---
Back in a more superstitious time, people believed left-handers were in league with the Devil. Now, in this age of Science, we realize that was unfair. Yes, left-handers are _statistically more likely_ to be in league with the Devil. But so are right-handers! It's only the ambidextrous who are truly pure!

At least this is the conclusion I take from Lyle & Grillo (2020) [Why Are Consistently-Handed Individuals More Authoritarian: The Role Of Need For Cognitive Closure](https://sci-hub.se/https://www.tandfonline.com/doi/abs/10.1080/1357650X.2020.1765791). It discusses studies finding that consistently-handed people (ie people who are not ambidextrous) are more likely to support authoritarian governments, demonstrate prejudice against "immigrants, homosexuals, Muslims, Mexicans, atheists, and liberals", and support violations of the Geneva Conventions in hypothetical scenarios.

The authors link this to a construct called "need for cognitive closure", ie being very sure you are right and unwilling to consider alternate perspectives. They argue that something about the interaction of brain hemispheres regulates cognitive closure, and that ambidextrous people, with their weak hemispheric dominance, get less of it. They study 235 undergraduates and find results that generally confirm this hypothesis: their ambidextrous subjects support less authoritarian and racist beliefs, and this is partly mediated by their scores on a Need For Closure measure.

I was really suspicious of all of this, so I decided to see if I could replicate these results on data from previous SSC Surveys. I chose [the 2019 survey](https://slatestarcodex.com/2019/01/13/ssc-survey-results-2019/), which collected data from 8,171 people and included a question on handedness. 

The survey did not outright contain the question "how authoritarian are you?", but it did have a lot of questions about politics. I preregistered (in my head, so you'll just have to trust me) four questions I thought might make good proxies for authoritarianism. 

First, a question asking respondents to rank their support for Donald Trump on a 1 - 5 scale. Previous studies have linked support for Trump to "right-wing authoritarianism", and although I have concerns about that exact construct, I thought it was in the spirit of the original research.

Second, a question asking respondents to rank their support for more open immigration, on a 1 - 5 scale. I figured that was a fair proxy for prejudice against immigrants, Mexicans, and Muslims. Although there were other questions about race on the survey, I chose this one because it also has an element of whether the government should clamp down on people.

Third, a question asking respondents what their political affiliation was, filtered for whether they answered "libertarian". Without getting into the weeds of exactly which political affiliations are more authoritarian than others, libertarianism seems pretty against that kind of thing.

Fourth, the same question, filtered for whether they answered "neoreactionary". Although "authoritarian" was not an available option, neoreaction is a philosophy based on highly centralized government. The explanation on the survey described it as "for example Singapore: prosperity, technology, and stability [are] more important than democratic process". This seemed as close to an "are you authoritarian" question as I was going to get.

I expected to find nothing, laugh, and move on. Contrary to my expectations, three of the four analyses were significant or marginally significant. Even more contrary to my expectations, they were all in the opposite of the predicted direction.

On the Trump item, the consistently-handed gave Trump a 1.63 star rating; the ambidextrous gave him 1.85. So ambidextrous people were more likely to support Donald Trump, p = 0.049 (I realize how bad that p-value looks, but [check the publicly available data yourself](https://slatestarcodex.com/2019/01/13/ssc-survey-results-2019/) if you don't believe me - though you may get slightly different results since a few people asked that they be excluded from the public data).

On the immigration item, the consistently-handed gave open immigration a 3.40/5 star rating; the ambidextrous gave it 3.22. So ambidextrous people were less likely to support open immigration, p = 0.008.

On the libertarian item, 21% of consistently-handed people identified as libertarian, compared to 19% of ambidextrous people. This was not a significant difference, p = 0.48.

On the neoreaction item, 5.2% of consistently-handed people identified as neoreactionary, compared to 9.4% (!) of ambidextrous people. This was marginally significant at p = 0.052. I hate marginal significance as much as you do, dear reader, but in the context of everything else I will take this seriously.

After this I did a non-preregistered exploration of percent ambidextrous by political position. From most to least, here's what I got:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9dba5be4-8af4-4d7b-9e59-48ea22732f8b_459x305.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9dba5be4-8af4-4d7b-9e59-48ea22732f8b_459x305.png)Total sample size of 8,106. The largest category, Social Democratic, had n = 2486; the smallest category, Marxist, had n = 144.

ANOVA says the differences here are statistically significant, p = 0.01, which is also the impression I get just looking at the table. But if anything, more authoritarian philosophies seem to have more ambidextrous proponents. 

So why did I get the opposite results from the original study?

The first possibility is always that one of us made a coding error, and accidentally coded ambidextrous people as not-ambidextrous and vice versa. If one of us did that, it was probably me. I make coding errors all the time. I tried really hard to double- and triple- check that I didn't make one here, but no promises.

The second possibility is that I ran into a [Lizardman Effect](https://slatestarcodex.com/2013/04/12/noisy-poll-results-and-reptilian-muslim-climatologists-from-mars/). Ambidexterity, supporting Donald Trump, and being Marxist were all uncommon positions in my survey. The sort of uncommon answers that trolls might endorse to confuse people, or that somebody who wasn’t taking the survey seriously might put down randomly in a rush to finish. We should expect a very small level of correlation between all uncommon positions just because of this effect. I’m eyeballing this as bigger than the Lizardman Effect alone usually gets us, but I don’t know how to prove that.

The third possibility is that the relationship between need for cognitive closure and authoritarianism is more complicated than the paper gives it credit for.

The paper didn't say exactly where it did the study, but some minimal detective work suggests three sites: the University of Louisville Kentucky, a second university in Louisville Kentucky I couldn't identify, and Schreiner University, a private Christian college in Texas. All these places are probably full of people raised in very right-wing, authoritarian, racially conservative backgrounds. If you were raised in a right-wing/authoritarian/racially-conservative background, and you have high need for cognitive closure, then you stay right-wing/authoritarian/racially-conservative. If you have more cognitive flexibility, then you flirt with forbidden ideas like leftism, personal liberty, and racial tolerance.

The SSC survey population comes from all over the world, but it's centered in the San Francisco Bay Area. If you grow up in the San Francisco Bay Area, then maybe flirting with forbidden ideas means you end up more likely to support Donald Trump, rather than less (cf. [the cellular automaton theory of fashion](https://slatestarcodex.com/2014/04/22/right-is-the-new-left/)). This isn't to say that low-need-for-cognitive-closure necessarily turns Californians right-wing. It could also turn them Marxist (the most ambidextrous political position on the survey). It just means they're more likely to end up somewhere far away from the local norm.

A fourth possibility: if you have need for cognitive closure, you only seek out information that agrees with you. If you have high need for cognitive closure, you seek out information that disagrees with you. This blog is probably very disagreeable for Marxists, and very agreeable for liberals and libertarians, which matches which of our readers are most likely to be ambidextrous. This would be a very easy hypothesis to test - just find a blog that disagrees with me about everything, and have them ask these same questions.

I would like to think that low-need-for-cognitive-closure is a value of this blog. Does that mean we have more ambidextrous people than normal? If we were being responsible, we would admit we can't tell, because different surveys will ask this question different ways, plus other studies have mostly been on children and we are adults. If we are being irresponsible, than yes, we do - about 2.4% of survey respondents were ambidextrous, compared to [1.1% of the general population](https://www.sciencedaily.com/releases/2010/01/100125094511.htm).

Finally, why would ambidexterity affect need for cognitive closure? 

I'm not sure how much I trust an explanation based on hemispheres. Sure, it's the most salient aspect of ambidexterity. But ambidexterity itself is a sort of failure of cognitive closure; just as the study subjects were able to maintain the option to switch between multiple political perspectives instead of settling into one, so ambidextrous children are able to maintain the option to switch between both hands instead settling on just one.

I predict that need for cognitive closure will turn out to be related to the constructs I tried to look at in [Why Are Transgender People Immune To Optical Illusions?](https://slatestarcodex.com/2017/06/28/why-are-transgender-people-immune-to-optical-illusions/) and [Can We Link Perception And Cognition?](https://slatestarcodex.com/2017/07/14/can-we-link-perception-and-cognition/) Both of these described how various categories of socially nonconformist people had unusual results on various optical illusions. I've checked against the same categories of nonconformist people, and they all have higher ambidexterity than normal. Gay people are twice as likely as straight people to be ambidextrous; autistic people 2.1x more likely than allistic people; trans people 3x more likely than cis people. And so on.

Right now my totally ungrounded irresponsible speculation is that need-for-cognitive-closure is one of the most basic parameters of the brain. At every level, it seems to determine something like "settle quickly on one obvious-seeming correct answer" vs. "start off open to anything and possibly end somewhere crazy". What your politics are, which sex to be attracted to, what your gender identity should be, which hand to write with - these are all questions where you're being asked to pick a side. Even more, they're questions where one of the sides has a big neon sign saying "TRY THIS ONE!" If you have high need-for-cognitive-closure, you'll go with the neon sign and defend your choice to the death. If you have low need-for-cognitive-closure, you could end up going anywhere at all or remaining permanently agnostic. This doesn't mean that people with these unusual conditions "choose" to have them. It means the involuntary neural processes that flip these switches are using the same brain parameters as every other system.

(one problem with this theory: trans people have higher ambidexterity than nonbinary people. I would expect nonbinary, as a kind of "failure to choose", to be an obvious match for ambidexterity, which is a failure to choose hands. Similarly, people who completely failed to see the Hollow Mask Illusion were more abnormal than those who got inconsistent results on it. I don't have a good explanation for this, except to think of non-binary as kind of trans-lite rather than a genuine lack of choice)

Of note, ambidextrous people were more likely to have every mental illness in my dataset, and [peer-reviewed studies confirm this](https://www.sciencedaily.com/releases/2010/01/100125094511.htm). So I'll make another very strong irresponsible speculation: what if low need-for-cognitive-closure is related to the much-sought [general factor of mental illness](https://www.nature.com/articles/s41398-018-0217-4)? In this theory, it's not just rejecting the obvious answer in questions like "what politics should I have?" and "what sex should I be attracted to?". It also determines how the brain answers questions like "where should this neuron go?" or "how strong should the connection between these two brain lobes be?" The more likely you are to choose "nonstandard" answers, the more mentally ill you will be. 

Why would evolution want anything other than the maximum need for cognitive closure? My guess is that lower closure permits (though does not guarantee) higher intelligence. But that's a third unfounded speculation, and I'll stop there before they take my speculating license away.
