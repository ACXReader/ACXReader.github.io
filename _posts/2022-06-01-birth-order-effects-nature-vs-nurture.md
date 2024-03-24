---
title: "Birth Order Effects: Nature vs. Nurture"
subtitle: "..."
date: 2022-06-01
likes: 109
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/56983266/comments?&all_comments=true
image: https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/92f7e4b6-4f9f-4fdc-93d5-89aa0946883c_1040x600.jpeg
original-url: https://www.astralcodexten.com/p/birth-order-effects-nature-vs-nurture
---
### Introduction

Thanks to everyone who waited two years for me to get around to this.

In 2018, thanks to the 8,000 of you who filled out the Slate Star Codex Reader Survey, I discovered that higher birth order siblings were much more likely to read this blog than later-borns:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F877a273a-c3d1-4f78-b239-634b0bc1b4f7_493x346.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F877a273a-c3d1-4f78-b239-634b0bc1b4f7_493x346.png)Source [here](https://slatestarcodex.com/2018/01/08/fight-me-psychologists-birth-order-effects-exist-and-are-very-strong/); thanks to Emile for the graph

That is, of people with exactly one sibling who read this blog, about 72% of those are the older of the two children in their family, compared to only 29% who are the younger of the two (where by chance we would expect 50-50). 

This was surprising, because at the time lots of studies had shown there weren’t really birth order effects (that is, firstborn siblings had no major personality differences compared to laterborns). I theorized that maybe for some reason it was easier to find by looking in a heavily-selected group of people and asking members about their birth order, compared to getting a random sample and trying to correlate birth order with things. Sure enough, later amateur research revealed strong birth order effects in [physics Nobelists](https://www.lesswrong.com/posts/QTLTic5nZ2DaBtoCv/birth-order-effect-found-in-nobel-laureates-in-physics) and [great mathematicians](https://www.lesswrong.com/posts/tj8QP2EFdP8p54z6i/historical-mathematicians-exhibit-a-birth-order-effect-too) (and potentially [Harvard philosophy students](https://bakadesuyo.com/2012/04/are-80-of-harvard-students-first-born-childre/)). Given that readers of this blog are highly-educated (about 37% have masters or PhDs) and mostly in STEM (41% programmers of some sort), plausibly birth order affects something about intelligence, education, or STEM orientation (somebody should check literature and peace Nobelists!) 

[Followup research](https://www.lesswrong.com/posts/YnXd7zfGGZfMD9QtA/age-gaps-and-birth-order-reanalysis) by Less Wrong user “Bucky” determined that the effect fell off with age gaps; the closer in age you are to your sibling, the stronger an effect birth order has:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4995a838-7372-40dc-8e51-1b35c811bd43_523x388.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4995a838-7372-40dc-8e51-1b35c811bd43_523x388.png)

I continue to be confused by this extremely strong effect which most of what we know about psychology says shouldn’t exist. So in 2020, I asked my readership [some even more complicated questions about their family situations](https://docs.google.com/forms/d/e/1FAIpQLScGVSQbvDiqGMoTQbOP4Fyj07rQ3c50i58cuNIy8rpY0QIa8A/formResponse), in the hopes of teasing out why this is happening.

I’ll be honest - I think I over-reached here. I’m not very good at statistics, and this is a weird statistical problem: the dependent variable is whether the case ended up in the sample at all! I wasn’t able to figure out a good way to use most of the data you gave me. And the stuff I did use, I mostly made work by slicing and dicing so much that the sample size got pretty low, even when I started from 8,000 survey respondents. I’m publishing this in the hopes that it will inspire someone else will more domain knowledge to do a sophisticated re-analysis. But for now, here’s what I’ve got.

### Confirming Old Results With The 2020 Dataset

The 2020 dataset also shows a strong birth order effect in people who read this blog. 

In 2018, among people with exactly one sibling, respondents were 2.51x more likely to be the older sibling than the younger (72%). In 2020, the number was 2.39x (71%).

Change with age gap is shown below:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8042c21d-a6b7-48f9-bbcc-daf8c136953c_497x339.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8042c21d-a6b7-48f9-bbcc-daf8c136953c_497x339.png)Note truncated y-axis

This seems to be broadly similar to the 2018 results. There was an anomaly in 2018 where some categories seemed to drop off surprisingly quickly between 7 and 8 years, which I thought might be meaningful. But [Bucky’s analysis](https://www.lesswrong.com/posts/YnXd7zfGGZfMD9QtA/age-gaps-and-birth-order-reanalysis) showed this was probably a coincidence, and indeed it doesn’t show up in the new data.

### Does Sex Matter For Birth Order Effects?

I wondered if there might be a smaller birth order effect for people with opposite-sex siblings. One possible explanation for the birth order effect is children trying to get out of the “shadow” of their older sibling and differentiate themselves in some way. But children are already pretty different from an opposite-sex sibling and might feel less pressure in that situation.

But this doesn’t seem to be true. The percent firstborns in sibships of two on the survey was 70% among people with a same-sex sibling, and 71% among people with an opposite-sex sibling; no real difference.

### Do Biological Or Social Factors Produce Birth Order Effects?

All previous results are for biological siblings. But it might be worth asking the question separately for biological vs. social siblings. One could imagine either biological or social causes of the birth order effect. For example, some biologists speculate that pregnancy depletes choline, that it takes a long time for choline stores to recover, and that a second child born within that window will have less choline available to build their nervous system, which could be bad. But also: maybe if you have an older sibling, your parents can’t pay as much attention to you when you’re a kid, and you learn less.

This was very hard to test for. Again, I wasn’t able to use traditional statistical tests because I’m trying to determine whether someone was in the sample at all, rather than whether two variables are related. It was easy to check normal birth order because I could compare people with exactly one older sibling to people with exactly one younger. It was harder to do with things like adoption in the mix, because that could introduce a bias: are parents more likely to adopt out their first child (because that’s when they’re most unprepared for parenting)? Are adoptive parents more likely to adopt when they already have children of their own (because they’re comfortable with child-rearing) or less likely (because they really want kids and can’t have them biologically)? I had no way of getting controls for these questions and so I couldn’t do a lot of the analyses I wanted. But I did two relatively weak analyses instead:

First, I took the entire set of people in weird situations - people who said their number of social siblings was not the same as their number of biological siblings. In this group of 174 people, biological firstborns made up only 61% of respondents with one sibling, notably less than the 71% in the entire sample. That suggests that the unusual social situations are having an effect. You shouldn’t update on the fact that it’s still higher than 50%, because some of the people’s weird social situations don’t affect their status as social firstborns.

Second, I tried to compare people who were firstborn under a biological definition but not a social definition, to people in the opposite situation. There were 40 people in the sample who were biological but not social firstborns, and 60 people who were social but not biological firstborns. Again, this suggests that social firstborn-ness is more important as an explanation than biological firstbornness, although it doesn’t rule out the latter having some effect.

I additionally tried to compare two different types of social firstbornness - one where no older siblings lived in the house when you were growing up, and one where your parents had never parented another child. There weren’t many people discordant on these two measures (29 vs. 20 respectively), but for what it’s worth, the ratio was in favor of the first type.

Since I wasn’t very confident in my analytical abilities here, I asked Bucky, who knows more and who did good work analyzing the last dataset, to look into this (we worked independently and didn’t tell each other our results until we were done). He writes:

> _It seems to me that the effect is entirely caused by social siblings._
> 
> _I filtered for only people with 1+ biological but 0 social siblings. There were 24 oldest biological children in this group vs 21 2nd children (or 25 youngest children with a large overlap between 2nd oldest and youngest groups). This significantly differed from the ~0.7 fraction of older children in the general surveys (p <0.05 or p<0.01 depending on whether I use the 2nd oldest or youngest as the comparison) and is close to a 1:1 ratio._
> 
> _I then filtered for only people with 0 biological but 1+ social siblings. There were 51 oldest social children and 23 2nd children (or 26 youngest children again with large overlap). This differs significantly from a 1:1 ratio (p <0.001 or p<0.01) and matches pretty well with the 70% of the Birth order effect._
> 
> _I tried doing some filtering by age gap (2-7 years) and the results were compatible with the same result, although the sample sizes got too small to really conclude anything._
> 
> _For dealing with answers left blank I treated them as 0 unless it looked like the whole section had been missed out. If I ignored any respondents who left something blank I got similar results (smaller sample size but ratios are even further in favour of the social hypothesis)._
> 
> _I checked for categorisation errors by looking at respondents’ descriptions of their families and they mainly matched pretty well with the numbers given so I think the data should be considered reliable. I did chuck a couple of results out which seemed unreliable and there was one row which was a repeat so your numbers might not match up exactly (plus you have the non-public data)._
> 
> _There are a couple of confounders in the analysis such as whether e.g. oldest children are more likely to be adopted or how much you know about your birth family depending on how old one was when the family unit changed etc. I don’t see a realistic way to account for these but I also can’t see any of them being big enough to explain the difference in the results._
> 
> _Hopefully this matches up with what you found!_

I think this suggests birth order effects are social rather than biological.

### So What Causes Birth Order Effects?

Based on this analysis, it seems unlikely they are biological. Based on my very weak sub-analysis, and on their tendency to decay with larger age gaps, it seems they have more to do with the social presence of a sibling in the house than with any changes in parenting style (ie your parents learn to parent differently). Two explanations that satisfy both those criteria:

  1. Parents are able to devote their full attention to parenting their first child, but only half of their attention to parenting their second. Firstborns get more quality time with their parents during the first few years of childhood.

  2. Siblings try to differentiate themselves from each other. So for example, since the older sibling will always be smarter than the younger when they’re both young children, maybe the younger sibling is more interested in excelling in areas other than school (like trying to cultivate a specific talent that the firstborn doesn’t have).




You may be able to think of others besides these.

One problem with (1) - wouldn’t you expect smaller effects as age gaps get lower? If it’s about having quality time alone with Mom, someone with a sibling one year younger than themselves only got one year of quality time; someone with a sibling five years younger got five years. But it looks like the birth order effect is stronger for someone with a one-year-age-gap sibling than a five-year one. Either the first year is very important, or I’m missing something.

A problem with (2) - I would expect the effect to be weaker with different-sex siblings in this case - less direct competition - but it isn’t.

If (1) is true, you might expect a strong effect against twins; after all, twins get unusually little of their mother’s attention in the first year. Are twins also under-represented in this dataset?

I think yes. 1.9% of respondents are twins. But [in the US as a whole](https://www.cdc.gov/nchs/products/databriefs/db80.htm):

[![https://www.cdc.gov/nchs/images/databriefs/51-100/db80_fig3.gif](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff114148c-eff3-4458-b7ca-aa7541c10738_560x285.gif)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff114148c-eff3-4458-b7ca-aa7541c10738_560x285.gif)

The average SSC reader is white and 33 years old, so we should expect a twinning rate of 2.4%. But in fact it should be a bit higher than this, because the two strongest risk factors for twinship are maternal age and maternal propensity to use IVF. Maternal age is highly correlated [with education](http://www.slate.com/articles/life/twins/2011/08/are_twins_taking_over.html) (it often means a mother waited to finish a degree before having children) and our readership is nothing if not [eager to use new birth-related technologies](https://astralcodexten.substack.com/p/welcome-polygenically-screened-babies?s=w). So we should expect to have significantly more twins than average. But in fact we have fewer. This isn’t a giant difference, but I think it supports the hypothesis at least a little.

Some previous studies suggested that twins just did worse in general, probably because it was too crowded in the womb and they got fewer resources each. More modern studies [fail to find that](https://eric.ed.gov/?id=EJ814952), at least on later life outcomes. But it’s possible that this is another effect which is too subtle to find in generic studies, but shows up in heavily-selected populations. If so, that would mean this section provides no extra evidence for anything.

### Implications

If birth order effects are due to parental investment, it would be pretty surprising. The current scientific consensus is that parental investment in the early years of life doesn’t really increase IQ or educational attainment during adulthood. That is, the shared environment has minimal to no effect on later life outcomes (see eg Bryan Caplan’s book _[Selfish Reasons To Have More Kids](https://www.npr.org/2011/04/22/135612560/selfish-reasons-for-parents-to-enjoy-having-kids)_). It’s generally agreed that people can put away the Advanced Baby Einstein Educational Toys and just chill.

This research challenges those assumptions. If it’s right, the difference in parental attention between an only child and a child with siblings seems to have noticeable effects later in life.

How do we reconcile this with twin studies? One potentially trollish answer is that all twin studies are necessarily done on twins, so the one component of the shared environment that they _can’t_ vary is whether their subjects have siblings or not! But this doesn’t really get us out of the problem. Some parents give their children much more parental attention and investment than others, regardless of sibling number, and you would expect this to show up in the twin studies as a positive shared environmental effect on those children. It doesn’t.

One possibility is that it doesn’t show up for the same reason birth order effects don’t usually show up: they only matter in heavily selected samples.

### Call For Further Research

I wasn’t able to do a very good job on this, partly because of my own limitations, and partly because of the limitations of the dataset.

One potential way to improve on this would be to run very large surveys of the population, such that we could capture the kind of person who does read SSC/ACX and the kind of person who doesn’t, and then do more traditional statistical tests on them.

Another would be to try to find other features in this survey which correlate with birth order, although this would be conditioning on a collider (their presence in the survey at all).

Finally, other people might be able to extract more signal out of this than I was. If you’re interested, you can find the raw data, the original question list, and a description of how to use them [here](https://slatestarcodex.com/2020/01/20/ssc-survey-results-2020/). Note that a few people refused permission for me to republish their data, so you will probably get slightly different numbers than I did.
