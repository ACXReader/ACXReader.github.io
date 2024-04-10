---
title: "The Mystery Of Internet Survey IQs"
subtitle: "..."
date: 2024-03-20
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/136151229/comments?&all_comments=true
image: https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2cfc82a-1d04-4b3a-9e6b-0ac0f213a00d_674x558.png
original-url: https://www.astralcodexten.com/p/the-mystery-of-internet-survey-iqs
---
I have data from two big Internet surveys, [Less Wrong 2014](https://www.lesswrong.com/posts/YAkpzvjC768Jm2TYb/2014-survey-results) and [Clearer Thinking 2023](https://twitter.com/SpencrGreenberg/status/1681775113065070592). Both asked questions about IQ:

  * The average LessWronger reported their IQ as 138.

  * The average ClearerThinking user reported their IQ as 130.




These are implausibly high. Only 1/200 people has an IQ of 138 or higher. 1/50 people have IQ 130, but the ClearerThinking survey used crowdworkers (eg Mechanical Turk) who should be totally average.

Okay, fine, so people lie about their IQ (or foolishly trust fake Internet IQ tests). Big deal, right? But these don’t look like lies. Both surveys asked for SAT scores, which are known to correspond to IQ. The LessWrong average was 1446, [corresponding to](https://www.iqcomparisonsite.com/satiq.aspx) IQ 140. The ClearerThinking average was 1350, [corresponding to](https://www.iqcomparisonsite.com/satiq.aspx) IQ 134. People seem less likely to lie about their SATs, and least likely of all to optimize their lies for getting IQ/SAT correspondences right.

And the Less Wrong survey asked people what test they based their estimates off of. Some people said fake Internet IQ tests. But other people named respected tests like the WAIS, WISC, and Stanford-Binet, or testing sessions by Mensa (yes, I know you all hate Mensa, but their IQ tests are considered pretty accurate). The subset of about 150 people who named unimpeachable tests had slightly _higher_ IQ (average 140) than everyone else.

Thanks to Spencer Greenberg of ClearerThinking, I think I’m finally starting to make progress in explaining what’s going on.

## Problem #1: The Biggest SAT → IQ Conversion Site Is Wrong

Thanks to Sebastian Jensen [for pointing this out!](https://www.sebjenseb.net/p/converting-sat-and-act-to-iq) He writes:

> A search of ‘SAT to IQ’ on google results in being presented with the website ‘iqcomparisonsite.com’. This man has directly converted the SAT percentiles to IQ scores, which is not what should be done. Tests like the ACT and SAT correlate with IQ at about 0.8-0.85 [[rca]](https://randomcriticalanalysis.com/2015/06/18/on-sat-act-iq-and-other-psychometric-test-correlations/), [[my analysis]](https://twitter.com/sebjenseb/status/1670608674291855361), [[emil article]](https://emilkirkegaard.dk/en/2020/03/intelligence-and-pisa-timss-etc-at-the-individual-level/), [[scholarly article]](https://journals.sagepub.com/doi/abs/10.1111/j.0956-7976.2004.00687.x). The general factor of academic achievement and IQ correlate at about 0.81-0.88 [[psychometric test]](https://sci-hub.ru/10.1016/j.intell.2012.01.009), [[GCSE grades]](https://www.sciencedirect.com/science/article/abs/pii/S0160289606000171). This discrepancy occurs because they measure different abilities - an IQ test will test many different abilities, while the SAT/ACT only tests verbal/mathematical ability.
> 
> In addition, these percentiles are very outdated as the average SAT score has [changed](https://www.researchgate.net/figure/Change-in-Total-SAT-Score-US_fig1_333384662) over time due to changes in the content of the test.
> 
> Instead, the ideal way to do this is to take the percentiles from the current versions of the SAT and then convert those into z-scores and then regress those z-scores by the mean by the estimated regression coefficient.

Using Sebastian’s updated tables, we find that the average Less Wrong IQ as predicted by SATs goes down from 140 → 132, and the ClearerThinking IQ goes down from 134 → 124. 

So people probably exaggerated their IQs somewhat, and unrelatedly we were using an SAT → IQ conversion that exaggerated IQs, and so the numbers falsely appeared to match. Okay! It’s a start!

## Interlude: The ClearerThinking IQ Test

The ClearerThinking survey included a battery of cognitive tests of exactly the sort that could usually be used to determine IQ. Unfortunately none of them were normed, so we know how all the 3700 subjects did relative to each other, but not where the 100 point is.

Spencer was able to norm them to the general population based on education level. That is, he asked his sample about their educational attainment (college degree, PhD, etc) and found they were a little more educated than the US average. Since the US average IQ is 100, his sample should have an average a little higher than this. He was able to calculate how much higher. Then he mapped a bell curve to everyone in his sample’s performance on his tests. Since he had 3700 people, he was able to do this relatively smoothly.

He found an average IQ of 110, which originally surprised me, because I thought his sample was supposed to be random crowdworkers, who should be close to the US average of 100.

But in fact, his survey was a combination of 1900 crowdworkers and 1800 people who saw it on social media - eg friends and friends-of-friends of Spencer. Separating this out by group, we find that the crowdworkers have an average normed-IQ of 100, and the social media referrals have an average normed-IQ of 120, making the overall average of 110.

This seems pretty trustworthy, since it correctly estimates the crowdworkers (completely average) as 100. Spencer studied math at Columbia, his friends and friends-of-friends are pretty smart, and I think the 120 estimate for them is also okay.

But there’s still a problem here. Using an accurate SAT score → IQ calculator, we determined that the ClearerThinking average should be 124. But using real cognitive tests, it looks like it’s 110. What went wrong?

## Problem #2: Only The Smartest People Report Their SATs

Using Spencer’s cognitive test results, we can compare people who did vs. didn’t take the SAT. We find:

  * People who didn’t take the SAT (remember, this includes current high schoolers) have tested-IQ 110.

  * People who took the SAT but “don’t remember” their score have tested-IQ 104.

  * People who took the SAT and do remember their score have tested-IQ 116.




Either smarter people are more likely to remember their SAT scores, or people who did well on the SAT are more likely to make a point of remembering!

Since the only reported SAT scores come from people who remember them, this means that SAT scores overestimate the full-sample IQ, at least in this case.

We previously had a gap between the 124 IQ from SAT conversion and the 110 observed IQ. This resolves about half of the gap, bringing it down to 124 predicted vs. 116 observed.

## Problem #3: Something Is Wrong With Self-Reported IQ Test Scores

The ClearerThinking sample has a tested-IQ of 110. But the subset of people who report having taken a past IQ test say they got an average score of 131. What’s going on?

It could either be that only the smartest people remember their IQ test scores (as with SATs), or that these people are lying/misremembering/deluded. Which is it?

The tested-IQ of this subgroup who report their scores is 114. So although they are a little smarter than the overall sample, most of the difference seems to be coming from some kind of falsehood/delusion.

But it’s a surprisingly well-behaved falsehood/delusion. Self-reported IQ test score correlates 0.54 with tested IQ. So people are getting their rank order mostly right, they’re just wrong about the specific number. 

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2cfc82a-1d04-4b3a-9e6b-0ac0f213a00d_674x558.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2cfc82a-1d04-4b3a-9e6b-0ac0f213a00d_674x558.png)

It looks like up to about 140, self-reported IQ and normed IQ rise together, and then the relationship breaks down. Sure enough, looking at the subset of self-reported IQ scores below 140, the correlation with tested IQ rises to .6, and looking at the subset _above_ 140, the correlation is nonsignificant __ at _-_ 0.02. I don’t want to assert that the breakpoint is exactly 140, but I do think the test stops working somewhere in the 130 - 140 range.

But this can’t be the whole problem. Notice that people who reported getting scores around 100 on previous IQ tests overwhelmingly got scores _less than_ 100 on this one.

So are people just taking terrible Internet IQ tests that inflate their score about 20 points?

The ClearerThinking sample didn’t ask people what IQ test they took, but the LessWrong sample did. It found approximately the same score from WAIS, WISC, Stanford-Binet, and Mensa - all of which were about 10 points above what you would predict from SAT scores.

So I think there are two things going on:

  * The main problem in the LessWrong sample, and the far right end of the ClearerThinking sample, is that even official IQ tests are gobbledygook over 135. Any numbers above this should be rounded down to 135, no matter how venerable the test involved.

  * The main problem in most of the ClearerThinking sample is that people took unreliable Internet IQ tests.




## Conclusion

We have three ways of estimating IQ in these samples: demographic norming based on education levels, self-reports from past IQ tests, and self-reported SAT scores converted into IQ. All of these contradict each other.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7412252e-bbb0-4125-9d55-d7eb2730485b_592x102.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7412252e-bbb0-4125-9d55-d7eb2730485b_592x102.png)

The self-report numbers are probably wrong because some people use bad tests, and other people use good tests that can’t measure above 135 accurately.

The SAT numbers are probably wrong because of selection: smarter people are more likely to take the SAT and remember their score. This probably becomes less important in overall smarter samples, where most people have taken the SAT and nobody has a score which is truly embarrassing.

The demographically normed numbers are . . . maybe not wrong? They’re the lowest of the three, which is tempting since our original problem was unbelievably high numbers. Still, I’m not completely comfortable with them for a few reasons.

First, Spencer did his demographic norming properly, but I extended it to the Less Wrong survey just by eyeballing.

Second, they won’t apply to people who have a mismatch between their intelligence and education level, eg smart slackers. The Internet seems full of these, and the demographic method will underestimate their intelligence.

Third, it has a ceiling effect: you can’t get more education than being a PhD, so it will underestimate the intelligence of a sample where a significant percent of subjects have PhDs or other advanced degrees.

Based on these, I would guess the ClearerThinking sample is around **111** , right where the demographic norms method puts it. And the LessWrong sample is around **128** , somewhere between the demographic norms method and the SAT method.

I don’t think either of these are too implausible. 1/30 people have IQs of 128 or above. Most people don’t read long articles online about statistics. 1/30 sounds like as good an estimate as any other for the sort of person who would find that comprehensible and interesting. 

Each year, I collect data on readers, including self-reported intelligence scores, which I use for various psychological experiments. Based on this research, I plan to either ask for reliable test scores only and lop off everything above 135 - or just subtract 10-15 points from whatever you give me.
