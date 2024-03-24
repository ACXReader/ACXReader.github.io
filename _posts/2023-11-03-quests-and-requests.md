---
title: "Quests And Requests"
subtitle: "Projects that need incubating"
date: 2023-11-03
likes: 125
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/138508657/comments?&all_comments=true
image: https://substack-post-media.s3.amazonaws.com/public/images/00d1b4d4-b3e2-4895-9fbf-362a767da030_492x319.png
original-url: https://www.astralcodexten.com/p/quests-and-requests
---
I’ll be starting a new round of ACX Grants sometime soon. I can’t guarantee I’ll fund all these projects - some of them are more like vanity projects than truly effective. But I might fund some of them, and others might be doable without funding. So if you’re feeling left out and want a cause to devote your life to, here are some extras.

## 1\. Replicate brain entrainment learning results. 

**Skills needed:** familiarity with EEG   
**Budget:** A few thousand dollars for machines, some large amount of your time?  
**Payoff:** People can learn things several times faster?

In 2022, [a team at Cambridge found](https://jacobshapiro.substack.com/p/teaching-at-the-brains-tempo) that experimental subjects learned faster when stimuli were presented at their brain’s unique alpha rhythm. The scientists monitored their brain waves to figure out exactly what each subject’s alpha rhythm was (usually a pattern of flashes about a dozen times per second), then presented a flashing pattern that hit the trough of each alpha wave, then asked subjects to solve tough visual recognition problems. They found the alpha entrainment helped them learn faster:

![](https://substackcdn.com/image/fetch/w_520,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F734bb5c1-3c06-44e6-9eea-17565db207d2_536x444.png)

Jacob Shapiro has [a good writeup of the experiment here](https://jacobshapiro.substack.com/p/teaching-at-the-brains-tempo) which asks the obvious next questions: what’s going on here, and can this be used to boost normal school-style learning? The most exciting interpretation would be that people have a hard time focusing because it requires maintaining a complicated brain wave rhythm for a long period and the brain’s internal metronome isn’t perfect. If an external metronome maintains the rhythm for you, you can focus longer and harder. 

I can’t tell if this is the Cambridge team’s own theory, or if they’re arguing something about visual disinhibition at the alpha trough that makes the specific kinds of problems they were presenting easier. But it shouldn’t be too hard to figure out how far this generalizes. Jacob claims that consumer-grade EEG headbands ($250 - $500) could potentially be used to replicate this result.

Someone should figure out whether this can be used for the sorts of things normal people want to learn - memorizing facts from a textbook, solving math problems, improving your chess game, that sort of thing. They might be able to figure it out by reading the original research carefully with a good neuroscience background and understanding its implications. Or they might need to use an EEG to do the experiment and see. I wouldn’t recommend this for someone who doesn’t already have extensive EEG experience. But if someone does have that experience, surely this is one of the most exciting things they could be doing with it.

## 2\. Open source polygenic score for educational attainment

**Skills needed:** statistical genetics, ability to access databases  
**Budget:** Some medium amount of your time?  
**Payoff:** Bring embryo selection to the masses; probably other things

“Educational attainment” (EA) means how much schooling you complete (high school dropout? College graduate? PhD? Etc). It’s used as a common proxy for IQ in psychological research, since most people don’t know their IQ, but do know how much education they’ve completed. EA and IQ correlate well enough that it’s rarely worth examining them separately.

EA is “massively polygenic”, meaning it’s the product of hundreds or thousands of different genes. If you have someone’s genome and want to predict their EA, you need a polygenic algorithm which will look at each of those thousands of genes and add or subtract the right amount for each of them.

Several teams have created predictors like this which can explain ~25% of the variance in individual EA. They’ve done studies with them and proven lots of interesting things. But as far as I know, none of them are open source. There’s no program you can download and run your genome through to get back an EA prediction. 

Separately, people are starting to use “polygenic embryo selection”. They do IVF, get ~10 embryos, genotype each, and implant whichever one seems to have the best genes. Usually “best genes” are defined in terms like “least likely to get cancer”. There are several companies that will genotype your embryos and tell you which ones are least likely to get cancer. If you want cancer-free embryos, capitalism has you covered.

Currently no publicly-advertising companies will tell you your embryos’ EA, so you can’t select for educational attainment/IQ (I’ve heard rumors that there might be a black market in this, but it’s hard-to-find and expensive). But all the normal cancer-risk companies will give you your embryos’ genotypes if you ask for them. If you had an open-source polygenic EA predictor, you could figure out which one had highest EA and select it yourself (at current tech levels, this means probably +3-5 IQ points, [see here for more](https://www.lesswrong.com/posts/yT22RcWrxZcXyGjsA/how-to-have-polygenically-screened-children)).

An open-source EA predictor would let people do this on their own without turning to a black market, and probably accelerate research more generally in ways I can’t predict right now.

Companies make predictors like these all the time (the cancer risk companies have done it for cancer), so it can’t be too hard for someone with the relevant skills. It’s possible that there are already some EA predictors floating around the open Internet that I just haven’t heard about. In that case, your job would be to make it usable by an ordinary consumer (drag and drop a file with your 23andMe results?) and put it somewhere people can find it.

## 3\. Things like John Green’s anti-tuberculosis campaign

**Skills needed:** knowledge of pharma landscape, fame or ability to interface with famous people  
**Budget:** Some large amount of your time?  
**Payoff:** Lower costs of life-saving drugs

Author and Internet celebrity John Green recently [campaigned against tuberculosis](https://www.mmm-online.com/home/channel/author-john-green-takes-jj-to-task-for-plans-to-extend-patent-on-tb-drug/).

His particular big victory was convincing some pharma companies not to enforce patents for their anti-tuberculosis drugs in developing countries. How did one person accomplish this? The best theory I can come up with is that pharma companies don’t care relatively less about their profits in developing markets (where there’s not much money anyway) compared to their public image in First World markets, so if you launch a good enough First World based campaign to get pharma companies to change their developing-world policies, even a medium-level celebrity can make them change course.

I’m inspired by this. Also, I’m a medium-level celebrity. So far I’m having trouble finding good leverage points (my latest interest is Coalition to Modify NOTA, see [here](/p/my-left-kidney)), but I bet people who actually know this space could find better ones.

Your job if you took this quest would be to figure out other leverage points like this, figure out how to run a corporate pressure campaign, and then run the corporate pressure campaign. Probably this would work better if you got celebrities on board. Getting me on board would be easy mode, but John Green has 40x more Twitter followers than I do, so you might need to look further afield.

## 4\. My crazy idea for language teaching

**Skills needed:** speak a foreign language  
**Budget:** Some large amount of your time?  
**Payoff:** Test a potential new language instruction technique

I make no guarantees this will work, it’s just something I’ve been thinking about for the past fifteen years and wish someone would test already. Here’s what I wrote in my old blog in 2012:

> imagine this - I'm going to use Japanese here because it's the only language I could even remotely try to use as an example without making a total fool of myself, and I'll thank you for not correcting the inevitable errors. The course is a novel. Could be any novel, but I imagine for cutesiness reasons you'd want to use a classic from the culture you're studying, like _The Tale of Genji_ or _Death Note_.  
>   
> The first chapter is just the first chapter of the novel in English. It would contain normal English sentences like "Ryuk taught Light the secrets of the Death Note."  
>   
> The second chapter is still in English, but it's a weird English with a sentence structure a bit more reminiscent of the foreign language. It might change to something like "Ryuk the secrets of the Death Note to Light taught". (I'm keeping the sentence the same to make it obvious what's going on here, but of course in the real book it would be the second chapter, not just a repetition of the first).  
>   
> The next chapter would do the same thing, but get a little more foreign, maybe "About Ryuk, secret of Death Note to Light taught"  
>   
> And gradually it would get a little more so: "Ryuk-about, Death Note-of secret Light-to taught."  
>   
> There would be enough of this that sentences with Japanese syntax would become as quickly and effortlessly readable as sentences with English syntax. And the hope is that the reader would keep going because they'd be enjoying the story, and after a little while adjusting the weird sentence structure would be a comparatively slight barrier to further progress.  
>   
> Then some of the grammatical particles would switch to full on foreign. Now it's "Ryuk-_wa_ , Death Note-_no_ secret Light-_e_ taught." Gradually we'd get through all of the horrible little verb bits where my language studies have previously crashed and burned: "Ryuk-_wa_ , Death Note-_no_ secret-_o_ Light-_e_ teach-_mashita_."   
>   
> I _might_ grudgingly allow little footnotes at the bottom like "This is the first time you've seen _-mashita_. It's just the standard past tense ending for verbs", but even that might be an unacceptable surrender to the grammar-memorization-industrial complex.  
>   
> Finally, and very gradually, it would start replacing English words with Japanese words. Just simple ones at first, ones that were obvious from context, and of course there would be a glossary in the back of the book you could look them up in if you had trouble.   
>   
> Finally, the last chapter would just be completely in Japanese: _"Ryuk wa Desu Noto no himitsu o Light e oshiemashita."_ It would probably be very deliberately simplified Japanese, but still, if you can read a book chapter in Japanese that seems like a pretty good success condition for an Intro Japanese textbook.  
>   
> (and of course Japanese is a bad example here because you'd have to learn the writing system separately. I'd have preferred the example in Spanish, but I'm not confident enough in my Spanish even to do a simple example sentence.)

I can’t think of any reason this wouldn’t work. I would do it myself except I don’t know any foreign language to the degree where I would feel comfortable teaching it to others. 

DJKeown on the subreddit [suggested using GPT for this](https://www.reddit.com/r/slatestarcodex/comments/158p4oy/scotts_old_old_language_learning_idea_and_gpt4/), but Spanish speakers weren’t impressed by its translation and I doubt it would really work.

## 5\. Automatic Implicit Association Test generator

**Skills needed:** web/software skills, maybe psychology knowledge?  
**Budget:** Some medium amount of your time?  
**Payoff:** Platform that could produce interesting measurements of biases.

The Implicit Association Test is a technique for measuring unconscious bias. 

The classic version, intended to show racial bias, works something like this. A computer presents you with words and pictures. The words could be good (“happy”, “beautiful”) or bad (“angry”, “disgusting”). The pictures could be photos of white people or of black people. 

Your task is to press either “A” or “L” (or any two keys, the exact letters don’t matter) as fast as you can. You press “A” for (good word or white person) and “L” for (bad word or black person). After you’ve done this for a while, you switch; now “A” is (good word or black person) and “L” is (bad word or white person).

If, like most people, you have a racial bias towards white-good / black-bad, it’s much easier for your mind to represent the nice consistent categories (good word or white person) and (bad word or black person), compared to the unnatural gerrymandered categories (good word or black person) and (bad word or white person). So most people will have faster reaction times on the first half of the test. The reaction time difference is a measure of how strong your racial bias is.

This all sounds very complicated when I try to explain it, but it feels viscerally obvious after you try it, [which you can do here](https://implicit.harvard.edu/implicit/takeatest.html) (click United States, then “I consent” at the bottom, then “Skin-tone IAT”).

People stopped being as interested in the IAT a few years ago after learning they couldn’t really use it to accuse their enemies of being racist. The “unconscious racial bias” of the test doesn’t really track how people vote or act or how politically correct they are. It doesn’t even consistently find that whites have more anti-black bias than blacks do. This makes sense to me - I don’t think it’s so much “blacks are worse because they are an inferior race” as “every time I hear about black people in the news it’s something depressing about how poor and oppressed they are, so it’s easy to associate them with negative adjectives”. Still, the hope was always to prove that some outgroup was racist, and when it fell apart, IAT interest waned.

But we still have this weird, magical-seeming test that can measure people’s unconscious biases, even the ones they’re trying to hide. Surely this has to be interesting somehow!

(see for example [this story](https://slatestarcodex.com/2013/04/22/implicit-association-tests-and-suicidality/) about people who tried to use it to predict suicide)

I don’t have a specific use case in mind so much as a vague sense that there must be more we can do with this. I propose an OKCupid of IATs, where anyone can make an IAT with a few clicks and share it with their friends (in the same sense that anyone could make and share personality tests on OKCupid). I’m not sure what people would do with this or what they would find, but I expect it to be fascinating.

Online IATs are tough because there are technical challenges to measuring sub-second reaction times. Still, Project Implicit at Harvard has done it, and maybe you could too.

This might be a good place to use AI: you can tell it to generate a hundred photos of white people and a hundred photos of black people (or whatever) and it’s probably easier than finding those yourself.

## 6\. A good dating site

**Skills needed:** web/software skills, influence with hundreds of women (I admit these two skillsets are inversely correlated)  
**Budget:** Some large amount of your time, a few thousand dollars in hosting costs?  
**Payoff:** Dates!

![](https://substackcdn.com/image/fetch/w_702,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00da0cfb-ad8f-4b54-8a49-596a4ef90f82_603x110.png)

Alyssa has a point.

Probably everyone wants different things here, but my demands would be:

  * Answer a few dozen to a few hundred questions, get a match % with other users

  * Emphasis on text, so you could [describe yourself and learn things about potential matches](/p/in-defense-of-describable-dating) instead of having to make an impulsive swipe decision based on their photo.

  * Some financial structure ensuring that it doesn’t have perverse incentives and won’t become a Tinder clone.




Some added bonuses:

  * A checkbox/swipe feature like on Reciprocity or Tinder, where if you were too chicken to ask someone out directly, you could click a box saying you liked them, and if they clicked the same box on you, you would match. I’m a little skeptical of these for reasons described [here](https://slatestarcodex.com/2019/04/10/pain-as-active-ingredient-in-dating/), but maybe you could fix it by having separate “excited to date this person” and “willing to try dating this person if they were excited about dating me” levels of box-tick.

  * Some way of preventing men from spamming women with messages, either by limiting them to a few messages per time period, or [more creative solutions](https://slatestarcodex.com/2018/01/18/practically-a-book-review-luna-whitepaper/), or by helping women filter on their end.

  * Matchmaking by friends.




I’ve wanted this along with everyone else since 2016, but since then some things have happened to make me less optimistic about this as a quest to request / project to incubate.

  1. [Manifold.love](https://manifold.love/) started up a few weeks ago. This isn’t exactly what I want - it doesn’t have the questions/matches, and its text questions are pretty specific and not conducive to getting people to really describe themselves. Still, it’s a clever and well-thought-out dating site that’s probably consuming most of this community’s dating site energy for the near future, and it would be both unwise and unfair to try to compete with it right now.

  2. [elcric_krej on the subreddit reminds us](https://www.reddit.com/r/slatestarcodex/comments/16a9g9r/look_at_the_real_world_the_reason_nobody_is/) that, as fun as it is to speculate about how to design the perfect dating app, the overwhelming challenge for all dating apps is getting the first thousand users (especially women). A cool mechanism design with no plan to make people use it is worth exactly $0.

  3. An acquaintance who _does_ have influence with hundreds of women and a great plan to solve the scaling problem has expressed interest in addressing this problem once she’s done with other projects, and I wouldn’t want a less qualified person to yank it away from her. I don’t know if I have permission to give more details.




This one is less a request for people to step up and incubate this project so much as trying to produce common knowledge of all of this and be open to anyone who wants to start coordinating.

## 7\. A foundation to promote classical art and architecture

**Skills needed:** art/design knowledge, social skills, administrative/entrepreneurial skills  
**Budget:** Some large amount of money from an outside funder, some large amount of your time?  
**Payoff:** A more beautiful world

Poll after poll shows that Americans prefer classical art and architecture, here used as a catchall term for styles that old-fashioned, ornate, symmetric, elegant, etc - eg neo-classical, Gothic revival, Art Nouveau, Art Deco. In the rare cases when someone builds something like this, people love it and it becomes an instant tourist attraction. But 99% of the time, we get the same Brutalist cubes, modernist blobs, starchitect [crumpled paper](https://twitter.com/blader/status/1670900940709429254), or lowest-common-denominator five-over-one apartments.

I’ve been [trying to figure out why for a while](/p/whither-tartaria). Some of it is cost, some of it is regulation, and some of it is elite opinion. But every so often someone successfully builds something classical and proves that it’s still possible in theory:

![](https://substackcdn.com/image/fetch/w_459,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f6152c1-3558-4115-8627-de55cae6db38_1278x1170.png)A Hindu temple that opened last month in New Jersey.

As far as I know, proponents of classical architecture don’t have an aegis organization the same way charter city proponents have[ CCI](https://chartercitiesinstitute.org/) or pro-progress types have [Roots of Progress](https://rootsofprogress.org/). Plenty of billionaires complain about the decay of art and architecture on Twitter, so there must be money available for something like this. All it needs is a founder.

An classical architecture aegis organization would:

  * Talk with architects, city planners, construction companies, and end clients to figure out what the major barriers to older architectural styles are.

  * Create a directory of people interested in these styles, so that a client who wants a more ornate building can easily find an architect who will design it for them and artisans who can build it.

  * Fund fellowships to help artists and architects learn older styles, and promote their work.

  * If regulatory issues are a major chokepoint, figure out the friendliest jurisdictions and the best strategies for changing the regulations, then lobby.

  * If cost issues are the major chokepoint, figure out if 3D printing, economies of scale, or novel materials can bring prices down.

  * If all of this is too ambitious, come up with a roadmap for how to start with small achievable victories and build up to cathedrals and concert halls. For example, maybe we should start by getting someone to produce [the sort of Art Nouveau furniture everyone wistfully lists on their Pinterest](https://www.pinterest.com/pin/114138171777415822/) before grudgingly accepting reality and buying IKEA. If that works, we can leverage what we’ve learned and the publicity we’ve gained to start working on bigger targets.




## 8\. A good primer on political change

**Skills needed:** understanding political change, writing a primer  
**Budget:** A medium amount of your time? Or maybe you already have one of these?  
**Payoff:** More political change.

Surely this exists. Surely this is already a book (or at least a blog post) and you just need to tell me the name of it. Still, I would really appreciate knowing that name!

Sometimes you have a good idea for political change (again, I’ll bring up the [Coalition to Modify NOTA](/p/my-left-kidney)). Probably some people disagree with it, but not too many people, and it’s not some issue like abortion where everyone thinks about it all the time and is at total loggerheads. It’s just some good idea that there should be a law about, but there isn’t. What’s the strategy for turning it into law?

Presumably the first step is convincing a member of Congress or the administrative state. How do you do this? On a very broad level, you should get articles in newspapers, sign petitions, and hold some protests. But suppose you do this. How do you translate this into support? Do you write a letter to your Congressman saying “Dear Senator: I have held eight protests this year and have two thousand signatures on my petition. That seems like a sufficient number of protests and signatures that you need to do something now.” Do the Congressmen just see the protests themselves and take the appropriate action? What if there are already polls saying that most Americans support your idea? Do you still have to do the media campaign / protests thing, or can you just send your Congressman the polls?

Once you have a Congressman on your side, what happens next? I often hear about good ideas that get a Congressman on their side, the Congressman proposes a bill, and it dies in committee even though probably lots of people would have supported it if it had been voted upon. Is there a way to avoid this? Is this your Congressman’s problem, or your problem?

If you want to convince the administrative state to make/repeal some regulation, do you write a letter to the appropriate official? How do you know who that is? Do they care about letters? Do they care how many protests you’ve organized? 

Probably these are stupid questions, and the people who understand these issues can explain exactly why they’re stupid and what smart questions I should be asking instead. But these people are rare, their time is valuable, and I would like one of them to have written a book so I can absorb their knowledge. Have they? If not, would someone consider writing it?

## Begging the questing

I probably can’t fund all of these ideas. But if you’re interested in taking one of them, mention it in the comments. At the very least you can connect with like-minded people. And I might be able to give you publicity and shop you around to funders.

If you know why one of these ideas is actually really stupid and won’t work / shouldn’t be tried, please comment about that too.
