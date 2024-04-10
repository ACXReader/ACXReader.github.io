---
title: "All Medications Are Insignificant In The Eyes Of God And Traditional Effect Size Criteria"
subtitle: "..."
date: 2023-05-31
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/124313293/comments?&all_comments=true
image: https://substack-post-media.s3.amazonaws.com/public/images/1d5af9df-01c0-46f3-87cc-f56ef1bf9a80_3450x1946.webp
original-url: https://www.astralcodexten.com/p/all-medications-are-insignificant
---
SSRI antidepressants like Prozac were first developed in the 1980s and 1990s. The first round of studies, sponsored by pharmaceutical companies, showed they worked great! But skeptics found substantial bias in these early trials; several later analyses that corrected for this all [found](https://slatestarcodex.com/2014/07/07/ssris-much-more-than-you-wanted-to-know/) [effect sizes](https://slatestarcodex.com/2018/02/26/ssc-journal-club-cipriani-on-antidepressants/) (compared to placebo) of only 0.30. 

Is an effect size of 0.30 good or bad? The usual answer is “bad”. The UK’s National Institute for Clinical Excellence [used to say](https://sci-hub.st/https://onlinelibrary.wiley.com/doi/10.1002/da.22249) that treatments were only “clinically relevant” if they had an effect size of 0.50 or more. The US FDA apparently has a [rule of thumb](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3719483/) that any effect size below 0.50 is “small”. 

Others are even stricter. [Leucht et al](https://sci-hub.st/https://pubmed.ncbi.nlm.nih.gov/23357658/) investigate when doctors subjectively feel like their patients have gotten better, and find that even effect size 0.50 correlates to doctors saying they see little or no change. Based on this research, Irving Kirsch, author of some of the earliest credible antidepressant effect size estimates, [argues that](https://sci-hub.st/https://pubmed.ncbi.nlm.nih.gov/31554608/) “[the] thresholds suggested by NICE were not empirically based and are presumably too small”, and says that “minimal improvement” should be defined as an effect size of 0.875 or more. No antidepressant consistently attains this. He [wrote](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2253608/): 

> Given these data, there seems little evidence to support the prescription of antidepressant medication to any but the most severely depressed patients, unless alternative treatments have failed to provide benefit.

…sparking a decade of news articles like [Antidepressants Don’t Work - Official Study](https://www.independent.co.uk/life-style/health-and-families/health-news/antidepressant-drugs-don-t-work-ndash-official-study-787264.html) and [Why Antidepressants Are No Better Than Placebos](https://www.newsweek.com/why-antidepressants-are-no-better-placebos-71111). Since then everyone has gotten into a lot of fights about this, with inconclusive results.

Recently a Danish team affiliated with the pharma company Lundbeck discovered an entirely new way to get into fights about this. I found their paper, **[Determining maximal achievable effect sizes of antidepressant therapies in placebo-controlled trials](https://onlinelibrary.wiley.com/doi/10.1111/acps.13340)** , more enlightening than most other writing on this issue. They ask: what if the skeptics’ preferred effect size number is impossible to reach?

Consider the typical antidepressant study. You’re probably measuring how depressed people are using a test called HAM-D - on one version, the scale ranges from 0 to 54, anything above 7 is depressed, anything above 24 is severely depressed. Most of your patients probably start out in the high teens to low twenties. You give half of them antidepressant and half placebo for six weeks. By the end of the six weeks, maybe a third of your subjects have dropped out due to side effects or general distractedness. On average, the people left in the placebo group will have a HAM-D score of around 15, and the people left in the experimental group will have some other score depending on how good your medication is.

The Danes simulate several different hypothetical medications. The one I find most interesting is a medication that completely cures some fraction of the people who take it. They simulate “completely cures” by giving the patients a distribution of HAM-D scores similar to those of healthy non-depressed people. Here’s what they find:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4843bd5d-c579-4367-b01c-728ec49c81b8_2128x1454.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4843bd5d-c579-4367-b01c-728ec49c81b8_2128x1454.png)

The pictures from A to F are antidepressants that cure 0%, 20%, 40%, 60%, 80%, and 100% of patients respectively. And we’re looking at the ES - effect size - for each.

Only D, E, and F pass NICE’s 0.50 threshold. And only F passes Kirsch’s higher 0.875 threshold. So a drug that completely cured 40% of people who took it would be “clinically insignificant” for NICE. And even a drug that completely cured 80% of the people who took it would be clinically insignificant for Kirsch! Clearly this use of “clinically insignificant” doesn’t match our intuitive standards of “meh, doesn’t matter”. 

We can make this even worse. Suppose that instead of completely curing patients, the drug “only” makes their depression improve a bit - specifically, half again as much as the placebo effect. Here’s the same simulation:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b1ca8dd-be4a-413f-aa37-39994bd3492c_2128x1454.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b1ca8dd-be4a-413f-aa37-39994bd3492c_2128x1454.png)

Here we find that only E and F meet NICE’s criteria, and _nobody_ meets Kirsch’s criteria! A drug that significantly improves 60% of patients is clinically insignificant for NICE, and even a drug that significantly improves 100% of patients improve is clinically insignificant for Kirsch!

What’s gone wrong here? The authors point to three problems. 

First, most people in depression trials respond very well to the placebo effect. The minimum score on a depression test is zero, and even healthy non-depressed people rarely get zero points exactly. So if most of the placebo group is doing pretty well, there’s not a lot of room for the drug to make people do better than placebo. 

Second, this improvement in the placebo group is inconsistent; a lot do recover completely, but others don’t recover at all. That means there’s a large standard deviation in the placebo group. Effect size is measured as a percent of standard deviation. If standard deviation is very high, this artificially lowers effect size.

Third, many patients (often about 30%) leave the study partway through for side effects or other reasons. These people stop taking the medication. But intention-to-treat analysis leaves them in the final statistics. Since a third of the experimental group isn’t even taking the medication, this artificially lowers the medication’s apparent effect size.

I’m not sure about this, but I think NICE and Kirsch were basing their criteria off observations of single patients. That is, in one person, it takes a difference of 0.50 or 0.875 to notice much of a change. But studies face different barriers than single-person observations and aren’t directly comparable.

NICE has since walked back on their claim that only effect sizes higher than 0.50 are clinically relevant (although this is part of a broader trend for health institutes not to say things like this, so I don’t want to make too big a deal of it). As far as I know, Kirsch hasn’t. Still, I think that a broader look at medication effect sizes suggests that the Danish team’s effect size laxness is overall right, and the earlier effect size strictness was wrong. [Here’s a chart](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4592565/) by a team including Leucht, who did some of the original HAM-D research:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d72b785-a287-42ad-92e8-5b8a8d419ebd_717x922.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d72b785-a287-42ad-92e8-5b8a8d419ebd_717x922.png)

Some of our favorite medications, including statins, anticholinergics, and bisphosphonates, don’t reach the 0.50 level. And many more, including triptans, benzodiazepines (!), and Ritalin (!!) don’t reach 0.875.

This doesn’t even include some of my favorites. Zolpidem (“Ambien”) has effect size around [0.39](https://www.bmj.com/content/345/bmj.e8343) for getting you to sleep faster. Ibuprofen (“Advil”, “Motrin”) has effect sizes between from about [0.20](https://twitter.com/micahgallen/status/1656699188825014292) (for surgical pain) to [0.42](https://twitter.com/KordingLab/status/1656819213732806662) (for arthritis). All of these are around the 0.30 effect size of antidepressants. There’s no anti-ibuprofen lobby trying to rile people up about NSAIDs, so nobody’s pointed out that this is “clinically insignificant”. But by traditional standards, it is!

Statisticians have tried to put effect sizes in context by saying some effect sizes are “small” or “big” or “relevant” or “miniscule”. I think this is a valiant effort. But it makes things worse as often as it makes them better. Some effect sizes are smaller than we think; others are larger. Consider a claim that the difference between treatment and control groups was “only as big, in terms of effect size, as the average height difference between men and women - just a couple of inches” (I think I saw someone say this once, but I’ve lost the reference thoroughly enough that I’m presenting it as a hypothetical). That drug would be more than four times stronger than Ambien! The difference between study effect sizes, population effect sizes, and individual effect sizes only confuses things further.

I would downweight all claims about “this drug has a meaningless effect size” compared to your other sources of evidence, like your clinical experience.
