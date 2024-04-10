---
title: "Followup: Quests And Requests"
subtitle: "..."
date: 2023-11-10
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/138719190/comments?&all_comments=true
image: https://substack-post-media.s3.amazonaws.com/public/images/bc87bf10-79c4-4efb-adb3-c8e5bd9fc278_800x525.png
original-url: https://www.astralcodexten.com/p/followup-quests-and-requests
---
Thanks to everyone who commented on [Quests And Requests](/p/quests-and-requests).

There was a predictable failure mode: lots of people said “I have relevant expertise and would be willing to help with #X”, and then those comments just sat there. Many fewer people said “I’m going to be team lead on #X and start contacting everyone else who was interested”.

In case it’s not clear: I’m not planning on “picking” people to lead each of these projects (though if you email me at scott@slatestarcodex.com asking for help, I might give it to you). I’m just putting them out there as things people might want to self-pick for.

Another predictable failure mode: many people said they were willing to help, and people should contact them, then didn’t leave any contact details. If you’re a would-be project leader, and want to get in touch with one of the help-offerers who didn’t provide an email, you should probably try responding to their comment and seeing if they get a notification. If not, email me at scott@slatestarcodex.com, and I’ll find their email in the system, ask them if I have permission to share it with you, and share it with you if they say yes.

Here’s the current status of each project, AFAICT:

**1 (EEG):**[Gustav Nilsonne](/p/quests-and-requests/comment/43151568), an expert in the field, said the study was unlikely to replicate. I still think it would be worth trying. Some EEG experts have volunteered to help but no one has taken point. [Luke Miles claims that](https://www.lesswrong.com/posts/diohDcgu3YdSbHd3j/go-flash-blinking-lights-at-printed-text-right-now) instead of the (costly, difficult) process of finding your EEG rhythm, you can just flash lights at yourself in various plausible rhythms until you find which one speeds your learning, and claims to have had success with this method. I consider this very speculative and likely to be placebo, but it’s another thing someone should try to replicate.

**2 (Open-source polygenic score):** I had two knowledgeable people who I trust email me offering to do this. Right now I’m talking with both and trying to figure out what each brings to the table and whether I should choose one or convince them to collaborate. Overall optimistic here!

**3 (Anti-TB campaign):** Many people commented that John Green didn’t invent this out of whole-cloth, he took a campaign by some existing charities and signal-boosted it. Sounds great, someone let me know if there’s a good campaign by existing charities that I should signal-boost.

**4 (Language learning technique):** Several people linked to groups that are already trying this. I was most excited by [Weeve](https://shop.weeve.ie/pages/shop), but there’s also [Prismatext](https://prismatext.com/), [The Adventures Di Pinocchio](https://www.jamez.it/project/the-adventures-di-pinocchio/), and [DonQuixote.fun](https://donquixote.fun/). If any of you try any of those, let me know how it goes.

**5 (Generate implicit association tests):** Nobody seemed too interested in this one, which is fair - it’s a pretty hard task for questionable payoff.

**6 (OKCupid-style dating site):**_Everyone_ seemed interested in this one. Two people say they’ve already been working on this for a while and collected teams: [Shreeda Segan ](/p/quests-and-requests/comment/43002642)and [Dendwrite](/p/quests-and-requests/comment/42983377). Shreeda is a friend of a friend and I can vouch for her; I don’t know Dendwrite but he also seems pretty committed. Read their comments to see what help they need and how to contact them if you can provide it.

**7 (Foundation to support classical architecture):**[The National Civic Art Society](https://www.civicart.org/) and [Institute For Classical Art and Architecture](https://www.classicist.org/) seem to already be something like this. Commenter Victor Thorne seemed interested in collecting people to work on this, but didn’t leave an email - maybe you can respond to his comment [here](/p/quests-and-requests/comment/43021102).

**8 (Primer on political change):** Many people had opinions on this, but nobody seems like they’re going to actually write the primer, sorry.

Here’s a more detailed list of comments on each project. I’ve started with practical comments (eg people volunteering or discussing existing implementations). The theoretical comments (about whether they’re a good idea, or discussing hypothetical feature wish lists) are towards the end.

## 1: Comments On EEG Focus

**Jona Sassenhagen[writes](/p/quests-and-requests/comment/42982588):**

> I could help out anyone taking #1.
> 
> I don’t have the bandwidth to do it myself, but a lot of experience analyzing EEG data and could help out with analysis or connect to people who could.
> 
> One idea would also be to reach out to the folks at MUSE (choosemuse.com) and ask them if they’re willing to help with infrastructure and even finding somebody to do this.

**Andrew X Stewart[writes](/p/quests-and-requests/comment/43012471):**

> I also have a lot of professional experience working with EEG data, and possibly access to hardware. Happy to collaborate on this, and organize efforts if needed.

**Martyna sp[writes](/p/quests-and-requests/comment/43035917):**

> I would be interested in helping out with this project. My experience with EEG only comes from a university intro class but recently I've been looking for projects where I could delve deeper into it. With some guidance, I'd be happy to take up any work throughout this project.

**Alain Daigle[writes](/p/quests-and-requests/comment/42989264):**

> I'm an EEG expert and re #1: To get a clear answer to this question you would need a large sample size, probably larger than the initial experiment (~N= 80), especially if performed with consumer grade EEG systems that have lower signal to noise ratio. Also, presenting stimuli at the ms precision required by this experiment, at a participant specific alpha frequency is not trivial. One possibility to ensure the success of this replication would be to team up with the #EEGManyLabs project, a group of researchers teaming up to replicate high profile EEG experiments.

**Gustav Nilsonne[writes](/p/quests-and-requests/comment/43151568):**

> #1 is very unlikely to hold up in my opinion, sorry.
> 
> The main result as shown in figure 2 of the paper (the graph included in the blog post) compares three groups. I downloaded the processed data from the Apollo repository and was able to reproduce exactly the results reported by the authors. However, these results rely entirely on omitting the fourth group, which was the control group.
> 
> In figure 2, we see that the "T-Match" group had a learning rate of about 0.03; the "T-Nonmatch" group had a learning rate of about 0.00, and the "P-match" group had a learning rate of about 0.01. In the supplementary figure S2.1 we find the control group and we can see that it had a learning rate of about 0.01.
> 
> Because the control group data were omitted also from the file that I used to replicate the analysis, I was not able to try it while including the control group. (The description of the control group in the methods section is unclear, but as best as I can tell the experiment was designed with 2x2 factors for 4 groups and should be analysed accordingly.)
> 
> This kind of research has enormous analytical flexibility. There are many ways to operationalise learning in the data from this experiment. The results were weak, with one of the main comparisons showing a p-value of 0.045 - just barely below the conventional threshold of 0.05. The preexisting analytical flexibility, nonstandard analysis, and barely statistically significant p-value would already cause me to bet heavily against reproducibility of the reported results. Additionally, the research was not preregistered and it was also heavily underpowered with 20 participants per cell.
> 
> I suggest that a first step for anyone wanting to dig deeper into this would be to request the raw data and re-run the analyses while including the control group. Other robustness checks would also be indicated, including different ways to operationalise the main outcome of learning. But in my opinion even that would likely be a waste of everybody's time.
> 
> My background: I am a researcher in neuroscience and metascience, involved in the EEGManyLabs project already mentioned by another commenter, and I co-lead the EEGManyPipelines project, which is a large-scale big team science project on analytical robustness of EEG data.

**rhyime[writes](/p/quests-and-requests/comment/43008083):**

> Looking at the article, at least the flickering is supposed to force the alignment of the person's rhythm, so it is a prepared stimulus with millisecond precision, not something that needs realtime updates based on EEG. And if the crucial part is just figuring out the frequency, as a signal-processing task this can tolerate quite a bit of noise.
> 
> All these avoidance of hard issues does not help a failed reproduction to be a meaningful outcome, though…

**quiet_NaN[writes](/p/quests-and-requests/comment/43034150):**

> I think getting to a millisecond timing is not all that difficult. An off-the-shelf microcontroller board (e.g. RasPi Zero, Arduino) should be sufficient for that, no need for FPGAs.
> 
> However, I have not the first clue about EEG. My idea would be to use one of these ~10$ breakout boards for one channel ECG (yes, I know) chips, wire them up to the analog digital converter input of the microcontroller, put both electrodes on my head somewhere (under my naive assumption that the main difference between EEG and ECG is simply where the electrodes are placed on the body) and plot the resulting signal, hoping that I see something which looks like alpha waves.
> 
> Then perhaps run a Fourier transform on the signal in real time, figure out the principal frequency and phase of the wave and turn on the stimulus with whatever phase-delay is appropriate.

## 2: Comments On Open-Source Polygenic Scores

I got several comments explaining very lucidly why this was impossible, and several other comments offering to do it. Someone I trust emailed me with an offer to do it, which I’m probably going to take them up on. Most projects fail, so I wouldn’t mind having a backup. I’m posting everyone’s comments here, including the comments on why it’s impossible, in the hopes that the “it’s impossible” and the “I’ll do it!” commenters can resolve their differences and give me a better perspective on options.

**Gene Smith writes:**

I have some advice for anyone interested in tackling #2:

> On pan.ukbb.broadinstitute.org/ there's a phenotype catalog, among which is fluid intelligence. There's like ~6800 SNPs significantly associated with it in the database. I believe you can actually download this set of SNPs!
> 
> The file is almost 2GB, so you need to put it into a database like SQLite and run commands to figure out stuff about it. Also, I bellieve the data all comes from a meta-analysis of fluid intellligence, which didn't use clumping alogirhtms to reduce false positives.
> 
> What I mean by this is that variants physically close on the genome will often be quite strongly correlated with one another, meaning one may mistakenly think that a particular variant is causing an observed difference in phenotype values when the real effect is cause by a neighboring variant.
> 
> It's possible one could obtain a data set of which variants are correlated with each other and use that to reduce the number of false positives.
> 
> You would then only need a relatively small validation set; perhaps 1000 genotypes + phenotypes, to validate the predictor.
> 
> We might be able to source this from the SSC community itself: get a bunch of people to take a standard IQ test or something and see what percentage of variance we could explain with the constructed predictor.
> 
> I am hesitant to take on this project myself because I have other projects I am already working on, but if anyone with a decent background in statistics or computational biology or just programming is interested in taking this on, feel free to reach out to me. I can put you in contact with some others who are interested in working on this. My email is [morewronger@gmail.com](mailto:morewronger@gmail.com).
> 
> In regards to the post, I also have one general comment:
> 
> _> “EA and IQ correlate well enough that it’s rarely worth examining them separately.”_
> 
> I take your general point that EA is a better-than-nothing proxy for intelligence if you have no other phenotype, but I don't belive to be true in general. If it were, we would expect both traits to be equally hertiable, which they are not (intelligence is substantially more hertiable than educational attainment). We would also expect both to show the same degree of "genetic nurture" effects, which is a way of saying that the genes of the parents have a large influence on the educational attainment of the child. But that's not what we see: there is significantly more genetic nurture involved in educational attainment than intelligence.
> 
> You can see further evidence that these phenotypes are not the same in studies like this one from Malanchini et al., who isolate specific genes that contribute to educational attainment: "We found that genetic effects associated with cognitive skills accounted for between 21% and 36% of the total variance in academic achievement"
> 
> Link: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10103958/pdf/nihpp-2023.04.03.535380v3.pdf>
> 
> Researchers have used educational attainment as a more politically acceptable proxy for intelligence in the past, but GWAS are now reaching scales at which these two traits diverge.

**Petar[writes](/p/quests-and-requests/comment/42983538):**

> I am a data scientist, and I wanted to work on #2. However, the best datasets, e.g. the UK Biobank, are locked for "legitimate researchers" and take particular care NOT to allow this specific thing. If I tell them that I have no degree and I want to use the dataset for correlating genes with IQ, they won't even answer my email.
> 
> So what I'm getting at is - if anyone reading this is associated with a research institution and wants to make this happen (apply for access to UK Biobank), I am willing to do the data side of this for free. [petar.istev@gmail.com](mailto:petar.istev@gmail.com).

See the followup subthread for more on the exact rules around this, especially [Sun Kitten’s comments](/p/quests-and-requests/comment/43027472).

**Metacelsus**([blog](https://denovo.substack.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata)) **writes:**

> Many papers already release the statistical data needed to reconstruct the scores. See for example the supplementary information in <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3935975/>
> 
> And plink is software you can use to calculate scores based on genotype.
> 
> That being said, this is still pretty tricky to get right, and I think there is substantial room for improvement in terms of open-source polygenic scoring.

**Peter Berggren (**[blog](https://nonmailableliveanimals.substack.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata)**) writes:**

> Not a statistical geneticist, but I think this article:
> 
> <https://www.nature.com/articles/s41588-022-01016-z>
> 
> also gives enough information to reconstruct the scores

**alphagrue[writes](/p/quests-and-requests/comment/43002727):**

> I'd potentially be interested in implementing #2 (PGS scores). I have previously applied educational attainment PGS scores to 1k genomes data, though I'm not a geneticist (I'm a data scientist/software engineer). My sense is that getting this up and running for 23andme data would be pretty easy, but I'm somewhat less clear about the data currently available from embryo testing companies (so I would need to look into that).

**Peter Berggren[writes](https://nonmailableliveanimals.substack.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata):**

> I'd be interested in #2, but I'm not in a good position to do this on my own (because I'm a CS/economics/data science student with no genomics experience whatsoever). However, I think my programming and statistics experience may be useful on the project. Anyone else want to collaborate with me on this?

**Antelope[writes](/p/quests-and-requests/comment/43008832):**

> I've looked into doing this myself. I think the project as currently formulated is valuable, but unlikely to accelerate research.
> 
> Here are my current unorganized thoughts:
> 
> 1\. The raw data for making EA polygenic predictors is locked behind various institutional barriers (i.e. you need to be a tenured professor to even ask for UK biobank access), so open-source people are limited to using summary stats of the latest EA GWAS's. But even the summary stats aren't being released in full for the latest EA GWAS's, case in point being EA4, which releases only the top 10,000 SNP betas as far as I remember in their PGS model, which is also likely where you got the (incorrect?) 25% variance explained from (EA4 paper says, "explains 12–16% of EA variance."). 3-5 points of IQ gain seems like an optimistic calculation for open-source because of this, and the fact that there's frequently problems with implantation/viability).
> 
> 2\. I think using said GWAS summary stats for your own PGS is already implemented at [pgscatalog.org](http://pgscatalog.org). There seems to be a workflow for scoring your own genotype data using the available GWAS's in the catalog. EA is available here, but due to reasons stated above, the avilable PGS weights aren't very good. Of course, this is far from layman-usable, so making an interface would be helpful I think (in particular, I think a slider adjusting how much you value various traits would be useful).
> 
> 3\. An even more high-value project might be to collect high-quality genotype-IQ data independently (1 million data points is an estimate of what's needed), or find contacts in existing biobanks amenable to sharing their data/listening to suggestions of what phenotypes to measure (asking directly for IQ would be difficult, but even adding a few mildly g-loaded items could provide a large increase in signal as opposed to just EA).
> 
> After saying all that, if anyone is planning on working on #2, I'd be willing to provide any help I can, although I'm not a specialist in this area. Contact me at [kakyo083@gmail.com](mailto:kakyo083@gmail.com) (not my personal email - i'd prefer to remain at least somewhat anonymous - so it might take a bit for me to read anything).

## 3: Comments On John Green’s Anti-TB Campaign

**Will Van Treuren[writes](/p/quests-and-requests/comment/43021717):**

> If anyone is thinking of tackling #3, I'd be interested in chatting. I founded a startup that is doing a small amount of antibiotic development outside our main focus. More antibiotics are an unalloyed good, and I think the patent extension mechanisms are generally bad, but probably there are some very important choices to be made in how this campaign is structured and what it targets.

**Erusian[writes](/p/quests-and-requests/comment/42986185):**

> One person did not accomplish this. This was part of a concerted campaign by MSF, Stop TB, and a few other organizations to let the patents expire. I'm actually kind of annoying that John Greene gets credit. Not because he doesn't deserve any credit but because MSF and other such organizations deserve much more. Anyway, eventually J+J allowed to procure generic versions of the drug in certain countries. It did not ultimately surrender the patent.
> 
> If you really want to do this the play would be to go ask MSF or other organizations what drugs they spend the most money on and then go to places like J+J and get them to agree to supply such drugs at cost to such organizations. And then possibly set up a production pipeline depending on whether they supply it themselves or simply give you the right to produce it. A good mission but not a simple one or really something that can be done without the confluence of influence, social connections, medical knowledge, and non-profit connections.
> 
> Still, a worthy effort.

Erusian again, in response to the (I think valid) question of whether pressuring companies to give up patents might decrease their profits and so their incentives to develop further drugs:

> Pressuring them to give up their patents might have bad long term effects. The negative effects of being asked to give up the small potential profit of selling into certain countries while maintaining their full rights seems much less likely to have bad effects. If they feel the deal is bad they can simply leave it. And to be honest it's not like they're making a lot of money off TB drugs in Tanzania or wherever anyway. The goodwill they get from the charity is probably worth more than the potential profit (and if it isn't they can say no).

This is my assessment too.

**Tyler[writes](/p/quests-and-requests/comment/42994023):**

> John Green + The Stop TB Partnership’s campaign against Johnson & Johnson is very similar to how EA animal groups like The Humane League (disclaimer: I used to work there) have run their corporate campaigns, although they’ve been successful without celebrity support for the most part - instead relying on grassroots support and funding.
> 
> I think corporate campaigns should work in basically any industry where (1) corporate reputation matters; and (2) corporate decision-making diverges from popular opinion. I’m a little nervous about doing this against pharma companies making drugs for neglected diseases since it could disincentivize them from making new drugs for that class of diseases (where the financial upside is already pretty low to begin with), but I am excited about some other opportunities.
> 
> Specifically, I’ve been working on a brand/web platform that I’m hoping to use for corporate campaigns in support of AI safety (mostly asking for smaller incremental concessions from AI labs - like stricter pre-deployment evaluations or greater investment in safety research). It’s still very young and pretty… homemade, and we haven’t begun our first campaign quite yet (waiting to build up more support), but If you’d like to check it out, it’s [www.themidasproject.com](http://www.themidasproject.com)

Thanks! Yeah, EA’s animal activism campaigns have been under-covered (including by me) but really impressively effective.

## 4: Comments On Language Learning

**Alzy[writes](/p/quests-and-requests/comment/43204203):**

> Re: language learning, an Irish company called Weeve does this (almost) exactly as described.
> 
> They sell printed books:
> 
> <https://shop.weeve.ie/pages/shop>
> 
> And there is a an app / Chrome extension so you can do it while browsing the web:
> 
> [weeve.ie](https://weeve.ie)

Thanks! Many people linked companies that do this, but this one is the first one I’m going to look into, since it seems to be doing a lot of things right - for example, it has sequential courses, and doesn’t try to force you to use their app for everything.

**Robin Goins[writes](/p/quests-and-requests/comment/42987944):**

> Re: language learning, that seems to already exist as a company: [prismatext.com](http://prismatext.com)

Another one that looks good, though it does force you to download and do everything through their app, so I probably won’t be checking it out.

**Mark (**[blog](https://doppelkorn.substack.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata)**)[writes](/p/quests-and-requests/comment/42983568):**

> FL-Teacher here (German). I remember your "crazy idea for language teaching" and "can’t think of any reason this would work" ;) - See: Foreign language teaching in US-schools (+other countries) is pretty broken (as Bryan Caplan declares so often), and this may explain why you people come up with most of the "crazy new ideas" for FLT (during my Master, I learned about a couple of them, including a group-therapy-approach). Thing is: FLT is not broken. With good course-material, a reasonable schedule and a competent teacher: it actually works mostly fine.
> 
> As I am a) kinda qualified - b) underworked - c) an "embarrassing fanboy" d) actually believing this approach might have some use with German for English-speakers (Japanese: ... less so ...)
> 
> my g m a i l is m k r o d e

**deusexmachine[writes](/p/quests-and-requests/comment/42985751):**

> I am a native German speaker, and have a background in teaching and education (not FL, though), as well as in translation. I am interested in this project as well. If you want to connect, let me know as a comment and I can shoot you an email.

**Timothy (**[blog](https://piecesofknowledge.substack.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata)**) writes:**

> for 4. My crazy idea for language teaching.
> 
> How do we get in contact with the person doing this project? Are they just reading the comments?
> 
> Anyway, I am fluent in German and English I would be happy to do this kind of translation for a book and maybe eventually a short story. Just contact me if interested.

**Dave**([blog](https://hallofdreams.org/)) **writes:**

> I started writing an attempt at idea . . . but it became much too long for a Substack comment, so I spun it off into a [blog post here](https://hallofdreams.org/posts/metamorphoses/). I took the first paragraph of every book in Ovid's _Metamorphoses_ and did the gradual partial translation, along with the Latin version and the literal English version for comparison.
> 
> Overall, having written it, I don't think the idea would work as-is. I listed a number of reasons why the idea wouldn't work for Latin specifically, but you listed several reasons why it wouldn't work for Japanese (the different writing system being the most obvious one), and I suspect that every language would have its own idiosyncratic reasons why English word order with loan words wouldn't work. It's not that you can learn _nothing_ about another language by substituting words, but that the nuances of the grammar are going to be harder to learn outside their normal context than in.

**Mark Neznansky (**[blog](https://markneznansky.substack.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata)**)[writes](/p/quests-and-requests/comment/42982671):**

> I've recently bumped into the idea at one Giacomo Miceli's website: <https://www.jamez.it/project/the-adventures-di-pinocchio/>
> 
> I've written him to ask about the prospects but never got an answer. His other finished projects suggest he is up the challenge skillwise, I suppose labour is the only thing left to invest. Perhaps if you wrote him as well he would be more inclined to follow through.

**Yorwba writes:**

> 4 sounds a lot like [donquixote.fun](http://donquixote.fun/) (which has content in Spanish, Italian, German and French) except that it progresses one sentence at a time. (When I last saw it, it was actually using Don Quixote as the text, but people didn't like the archaic language <https://news.ycombinator.com/item?id=26601643> )

**Tzvi[writes](/p/quests-and-requests/comment/42989290):**

> The book: "the avion my uncle flew" does the language idea. It starts in english and finishes in french.
> 
> <https://www.amazon.com/Avion-Uncle-Puffin-Newbery-Library/dp/0140364870>

Thanks, I have ordered this. It looks like there are several children’s books of this type. I just don’t know how you would scale up from there to really being good at the language.

**Doug Summers-Stay[writes](/p/quests-and-requests/comment/42982958):**

> On language learning (#4) -- There are web plugins that substitute foreign vocabulary words into your webpages as you read, with a slider for how far down the vocabulary list you want to replace. Since most of the page is still in English, you pick up the meaning of the words by context. Since I mostly just want to be able to read foreign languages, and the hardest part of that is vocabulary (you can mostly just ignore word-ending changes) I find this pretty useful.

Toucan <https://chrome.google.com/webstore/detail/toucan-by-babbel-language/lokjgaehpcnlmkebpmjiofccpklbmoci> is one. There are a few different ones out there.

## 5: Comments On An Implicit Association Test Site

**Imajication[writes](/p/quests-and-requests/comment/43122157):**

> #5 Really excites me because it was similar to something I worked on for myself a while ago, though it was more like a super-CBT/affirmation tool: a game where you try to choose the positive fill in the blank answer quickly, theoretically training you to have more positive automatic thoughts.
> 
> The "theoretically" their is obviously doing a lot of work, but I usually felt a bit better after playing it.
> 
> This post motivated me to brush it off and get it working again:
> 
> <https://implicit-associator-acx.s3.amazonaws.com/HappyGame.html> (works best on mobile)
> 
> This is a pure-front-end-web-app with all the sentences hard-coded. I don't see any issue with getting accurate timing: the timing could be done client side (as others have said) and I really think even a web-app like this would be high-fidelity enough for human-scale interactions. The only issue is security. I don't think you could make a web-app that's secure against someone cheating if they really wanted to. If we're measuring biases people might be trying to hide, this would be an issue. The solution would be to make a native app of some sort. I'd probably use one of the tools which lets you build native apps for iPhone and Android.
> 
> As others have stated, a CRUD for creating the tests wouldn't be hard, though we'd have to think about how exactly the configurability would work. And then there would be adding identification and authorization, which I would probably implement with AWS Cognito.
> 
> AI integration would be an interesting feature, both for generating images and for creating phrases or gathering a certain class of words ("Give me a bunch of phrases that are reflective of crime").
> 
> [valmikirao+acx@gmail.com](mailto:valmikirao+acx@gmail.com), if you want to talk about developing this more.

I’ very skeptical of this, but I appreciate the level of lateral thinking and ambition that went into producing it!

## 6: Comments On A Good Dating Site

**Shreeda Segan[writes](/p/quests-and-requests/comment/43002642):**

> Hello!
> 
> I'm currently working with a small team on the dating site. Alyssa had an excellent tweet, I'm in contact with her, and she recently retweeted my bid to get more team-members on board. (<https://twitter.com/freeshreeda/status/1719118204297966003>)
> 
> I also think I understand the problem pretty well as it was the research topic of my choice for a recent fellowship with Ethereum Foundation ([summerofprotocols.com](http://summerofprotocols.com)). Happy to chat through the problem and/or share my research with people in private.
> 
> We're looking for more frontend and design support. Also donations to help us cover infra costs. We're keenly aware that the tech is not going to be the big thing — it's the network of daters that joins. We think we can do a better job of marketing such a product than things like [twitterdatingapp.com](http://twitterdatingapp.com) (which we think is good as an MVP and product but bad at branding).
> 
> DM me on Twitter (@freeshreeda) or email me (shreedashreeda at gmail dot com) if interested!

Oh, thank goodness, finally someone is actually leading a thing and giving contact details. Shreeda is a friend of a friend and I wish her the best.

**Dendwrite (**[blog](https://dendwrite.substack.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata)**) writes:**

> I have a team that is working on the dating site more or less as Scott described (for everyone, not just rationalists). I have a data science/machine learning background so we will try to take a data-driven approach to solving the social engineering problems. If you're interested in getting involved (especially re: funding) contact me at tmoldwin[at]gmail .

**Mark Neznansky (**[blog](https://markneznansky.substack.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata)**)[writes](/p/quests-and-requests/comment/42982864):**

> Another key feature that distinguished 2011 OKCupid from what followed is the thumbnail display of profiles, sorted by match percentage. It enabled you to "browse" instead of being pushed into making a binary decision one random profile at a time.

## 7: Comments On A Foundation To Promote Classical Architecture

**Victor Thorne[writes](/p/quests-and-requests/comment/43020992):**

> I am very interested in 7- trying to start a thread of people who are.

**Perry[writes](/p/quests-and-requests/comment/42989295):**

> Re: 7, I'm a landscape architect in the Washington DC area and would be happy to consult with anyone pursuing this quest. I have familiarity with design review (and the approvals process) at the municipal and county level, building code, the public response part of the design process, value engineering, etc., and can help get someone started navigating all that. These things vary by municipality, state, and market, but I can help you figure out where to start. Most of my relevant experience is in multifamily housing (apartments/condos/townhomes) and commercial (stores, restaurants, shopping centers, strip malls). I also have experience in single family homes and parks but I think those are less of a focal area for this hypothetical foundation.
> 
> You'd really want to get an architect and building contractor on board ASAP, and probably also a land use attorney, since I'm a landscape and land planning professional and not an architecture expert. But I might be able to help you get started.
> 
> Email me at why0hat at Gmail dot com if you want to talk!

**Joseph Addington (**[blog](https://progressandpoverty.substack.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata)**) writes:**

> There actually is already an organization that promotes classical architecture in government buildings, at least, the National Civic Art Society: <https://www.civicart.org>.
> 
> I doubt I have the connections or expertise to head up any kind of broader promotion of traditional architecture, but I’d be more than happy to assist with such an initiative, which seems a very worthy and achievable one.

Thanks, this looks great and very close to what I want, though I can’t tell how limited it is to government buildings.

**Jim writes:**

> _> “As far as I know, proponents of classical architecture don’t have an aegis organization the same way charter city proponents have CCI or pro-progress types have Roots of Progress."_
> 
> Actually, they do: The Institute of Classical Architecture and Art: <https://www.classicist.org/>
> 
> The academic center of the traditional architecture movement is the University of Notre Dame: <https://architecture.nd.edu/>
> 
> _> “Some of it is cost, some of it is regulation, and some of it is elite opinion."_
> 
> Neither cost nor regulation is an important contributor to the problem. Elite opinion, especially in architecture schools, is by far the most important factor.
> 
> Regarding cost:
> 
> A) exterior ornament is a less important driver of building cost than structural and mechanical building systems. Those latter items scale more or less linearly with building size. So the main determinants of a building's cost are its location (since construction labor costs vary by region), its function (which drive the structural and mechanical code requirements) and its floor area. The use of limestone cornices rather than glass curtain walls is much less important than these factors.
> 
> B) Modernist detailing is deceptively expensive, so the apparent simplicity doesn't actually save money. And I'm talking about normal modernist buildings here, and not even touching the crazy Frank Gehry-tier "starchitect" buildings like MIT's Stata Center, which tend to be fiendishly difficult to build, expensive, and prone to defects.
> 
> Regarding regulation:
> 
> The building industry is highly regulated, but the most of the regulation deals with building use and size (zoning) and structure, fire protection, electrical safety, etc. (life safety). These regulations have considerable influence on what can be built and how much it costs, but they have virtually no impact on the decision to go with Midcentury Modern rather than Georgian Classical.
> 
> Actually, in the specific jurisdictions where regulation directly addresses aesthetics, the influence usually _*favors*_ traditional design. These are jurisdictions where there are historic commissions or architectural review boards. They often require that new buildings or renovations fit in with the existing pre-WWII urban fabric. This does produce more traditional architecture (or, at least, prevents the destruction of old traditional architecture) in these specific neighborhoods.
> 
> The preferences of the faculty of most architecture schools, and therefore of most graduates of these schools, is what proliferates modernist architecture. Visit the websites of these schools and look at their galleries of student work and their academic design publications, and you will have your answer.

**Tristan[writes](/p/quests-and-requests/comment/43007241):**

> I think I have pretty good insight on why all new buildings look like smooth blobs. I'm a design student, have spent 100's of hours studying form development. When I look at the AI generated frank gehry my first reaction is "wow, that's a pretty cool building". It seems like spending 100's of hours studying form development and such perhaps makes you think that really sophisticated blobs are the way to go. This is a problem because most people have not spent the time training their brains to recognize really sophisticated blobs and prefer classic architecture.
> 
> Over the past 100 years or so architects have gone from rich dudes who were unusually good at drawing and had basically the same taste as everyone else to design students who have spent 1000 hours trying to draw increasingly sophisticated blobs to score a chance at getting into a top architecture firm, and no longer have the same aesthetic taste as everyone else. Architects also gradually changed from being service people to being artists, who think they know more then their clients and impose their preferred artistic vision on whatever projects they work on.
> 
> Even if architects now have increasingly differing aesthetic tastes from everyone else, why gravitate towards sophisticated blobs? it could be that it's a basic quirk of human psychology that you prefer more basic shapes if you think about it for an unusual amount of time. Alternatively, this could be basically a trapped prior issue. Architects are all taught by architects, once 51% of architecture teachers prefer sophisticated blobs, you get a death spiral.
> 
> As to how you could get to 51% of architects preferring modern styles, it's probably a combination of economic incentives and projects shifting from client led to architect led. Classic architecture requires 100's of skilled crafts people for the elaborate bricklaying, engraving, etc. Architects are trained in form development not bricklaying, so the buildings they design are going to gravitate towards being dominated by one or two pleasing forms, not the 1000's of small details that compose classic cathedrals.

It seems several people agree on this story. I’m most interested in the question of why the market isn’t resolving it. Every building is built by some specific person or group, whether that’s the government building a courthouse, a developer building homes, a congregation building a church, or a business building a new HQ. None of these people are architects, so why don’t they demand architects implement their preferences instead of the architect’s own?

**Ben Southwood (**[blog](https://www.bensouthwood.co.uk/?utm_source=substack&utm_medium=web&utm_content=comment_metadata)**)[writes](/p/quests-and-requests/comment/42988469):**

> You should talk to Samuel Hughes (I'm sure you know him from Twitter: <https://twitter.com/scp_hughes>) about #7, in part because he is also quite au fait with some of the distributed answers to #8, and is already working on this question. He was the researcher for the UK's Building Better, Building Beautiful Commission, which was sort of like a consensus-based committee attempt to make progress on this question.
> 
> Though I have to say that I think 'classical architecture' and 'traditional architecture' are probably the wrong framing. What we want is popular architecture (which they are a type of, but not the only type of): <https://worksinprogress.co/issue/making-architecture-easy>
> 
> Hopefully you saw our previous work on this question too (<https://worksinprogress.co/issue/against-the-survival-of-the-prettiest> and <https://worksinprogress.co/issue/in-praise-of-pastiche>)

I don’t know if I like the “popular architecture” reframing. I agree that the important thing is that buildings should be good, and that classical architecture is only one kind of potentially good building. But I also think that “classical” short-circuits a lot of tedious debate over what kind of buildings are or aren’t good, and is an easy Schelling category that captures most of what people mean by “good building” without forcing a debate over “well my architecture should be popular too”.

**Michael Schepak[writes](/p/quests-and-requests/comment/43015840):**

> As far as architecture is concerned, this Facebook group is about reviving human based architecture and reviving classical design styles [https://m.facebook.com/groups/Klassisknyproduktion/?ref=share&mibextid=S66gvF](https://m.facebook.com/groups/Klassisknyproduktion/?ref=share&mibextid=S66gvF)

**J.E. Rumbelow (**[blog](https://jamieonsoftware.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata)**)[writes](/p/quests-and-requests/comment/42985026):**

> I'm the cofounder of [Tract](https://buildwithtract.com/), a startup trying to make it easier to reason about planning risk. One of the things I'd like to prototype, and which might dovetail rather nicely with §7, is a modern approach to visual preferences survey: a 'Tinder for buildings', somewhere local communities can vote on and discuss various architectural styles. We can use generative AI methods to slot new facades into existing streetscapes, analyse the data, and see if we can find meaningful clusters that pin down quantitively what a 'local vernacular' actually consists of.

Somebody who knows things should look at this and tell me whether it’s stupid or brilliant.

**Kiefer Kazimir[writes](/p/quests-and-requests/comment/42983245_metadata):**

> I also wanted to point out that [my Substack](https://onthearts.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata) is something an attempt to educate people on the breadth and history of art and aesthetics, as most art /architecture magazines are very uncritical of contemporary aesthetics and art styles. Any change in this area starts with education, as “I like old architecture” or “art used to be more beautiful” is generally too vague to be actionable.
> 
> For example, [here’s a guide to distinguishing Art Nouveau from Art Deco](https://onthearts.com/p/art-nouveau-vs-art-deco).

Go ahead and read his blog and get educated, but I do disagree with his claim that vague isn’t actionable. Vagueness is perfectly fine for a popular movement. Pro-choice people want “yay abortion rights”, and know nothing about different abortion methods, or the laws on how many weeks you can do each, or how many feet protesters have to stand away from abortion clinics. 

In practice, most people’s real opinions are about “classical architecture” vs. “modern architecture”, and if you demand they know the difference between a neo-Palladian balustrade and a Georgian Renaissance buttress before expressing their preference, it will just mean that nobody ever expresses a preference. 

The pro-choice movement works because there are some small number of wonks who can say “What we want is X method of abortion to be protected by Y legal infrastructure as defined in Z court case” and then everyone else goes “Yeah, do what they said!” because those people are endorsed by NARAL or something and the average activist assumes their plan is good. I think ordinary people should be comfortable saying “Yay classical architecture!” and letting smart people (maybe including Kiefer) figure out the details.

## 8: Comments On A Primer About Political Change

**Spencer Orenstein Lequerica (**[blog](https://thebrownbarge.substack.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata)**)[writes](/p/quests-and-requests/comment/43018490):**

> On 8: I have worked for ~13 years in various levels of federal politics and been involved with both congressional and executive changes. When I worked as a congressional staffer my office was ranked the most effective legislative office by a (sort of not that rigorous, but not entirely fake) project by political scientists at UVA and Vanderbilt. I’ve also worked in the think tank world. Would be interested in collaborating on this primer if anyone else wants to work on it together.

**Zoomer Antimillenarian[writes](/p/quests-and-requests/comment/43029346):**

> (8) is something I'd like to work on, with a little help from you setting up some interviews.
> 
> As far as I can tell, a lot of (8) is already written but it's scattered between many different sources, and between many different specialties. Different people handle appealing to voters, mass activism, lobbying and intra-elite activism, mass litigation strategies, and so on (this is far from exhaustive).
> 
> The real hole here is that there's no good, trustworthy, reliable, and *current* book to tie together the trustworthy sources, go over the basics of how political change can be accomplished and how the process works, and offer a sober but actionable set of strategies and courses of action.
> 
> I'd like to discuss details with you over Twitter DMs (I'm @surcomplicated) or email (DM me and I'll trade emails with you if you want) but what you could really do for me is set me up with a few interview subjects to make sure I get the details of their sides of things right. Different people handle issue polling than handle litigation than handle intra-elite activism and lobbying than handle protesting in the streets and so on. The job here is fundamentally to take expert knowledge in these (in practice) separate specialties and weave it together into a general primer on how you change things, and while there's plenty of written expert material on these specialties interviews can paper over any holes that remain.

**jumpingjacksplash[writes](/p/quests-and-requests/comment/42983751):**

> Isn’t the answer to 8 just lobbying? In practical terms, get a bunch of money and hire a k-street outfit that draws from whatever regulator or political tendencies in congress are on your side.
> 
> In gears-level terms, you need to connect your reform to the interests of the people who can make it happen, then increase its salience. For congress, that’s donations and lobby connections to reps who have sway and/or are on the relevant committees. For regulators, that’s industry connections and and getting plum bookers to make it a hobby horse through connections.
> 
> The missing moods in your take are image/action distinctions and patronage. In the US, where individual politicians fates aren’t wholly tied to their parties, get lots of credit for grandstanding (sponsoring bills, endorsing things), not much for doing things (passing laws). Make something popular, and everyone will introduce laws to do it but no-one will achieve anything because that’s too far downstream of anything you get credit for with the electorate if you’re not the president.
> 
> Patron-client relations are how things actually work; in summary, people align with someone important and do them favours, on the basis that that person (more likely, their other clients) will do things for them. The patron is basically a co-ordinator, much of whose influence comes from their clients.
> 
> Lobbyists are patrons for profit; they can donate to campaigns (politicians) and find people jobs (everyone, including civil servants), as well as acting as a favour clearing house in the normal way. They don’t have to promise anyone anything, but you know they’ve got your back because you’re their client (in the patronage sense, not the customer who foots the bill).

All of this is fine advice. But it feels like I am asking for a textbook on electrical engineering, and Jack is saying “Isn’t the answer just circuits? Just connect a power source through wires, and the current will flow through and power your devices.” Everything he says is right and useful, it’s just that I’m asking for the long version of what he’s giving the summary of. I expect this is because he’s knowledgeable enough that it’s hard for him to imagine other people lacking the relevant details (for example, I don’t know what k-street is, what bookers are, etc).

**AshLael[writes](/p/quests-and-requests/comment/42986370):**

> Re: 8 - the answer is highly variable depending on the precise situation.
> 
> For example, during the Turnbull and Morrison governments, there was a lot of policy inertia. The government didn't have a lot of vision or purpose and was consumed with its own internal squabbles. Stuff percolated up through the public service but it wasn't really anything far-reaching or ambitious. The best avenue to change was to get a politician on side to fight for your issue and really make a stink about it.
> 
> But with the Albanese government I have been surprised to discover that getting a politician on side to yell about your issue - while obviously still really nice to have of course - is not so necessary. They have initiated a lot of substantial legislative changes and a bunch of big reviews and most of these processes are open to public comment. So you can get a surprising amount of progress by engaging with these processes. You send in a 5 page submission saying "hey your exposure draft is great but there are these 4 problems with it and we think they could be alleviated in this way and also we think it would be great to also address this related issue that your current bill doesn't look at". And sometimes you convince them.
> 
> So these are very different situations in the same country and political system. And perhaps as the Albanese government ages more policy inertia will set in. The situation may be different again in other countries. But in all cases a level of specific knowledge is needed about the system, issue, and political pressures that certain actors face.
> 
> For someone in Scott's particular situation, one tactic I would recommend is identifying the specific person you need to get the change made, and writing public posts and going on podcasts saying "it would be excellent and a testament to their wisdom if person X did Y". It's important to highlight Person X by name because Person X almost certainly uses a media monitoring service that alerts them about anything that gets said about them in the media, and prominent blogs and podcasts are very much a part of that. These people are often shockingly vain and notice when they get specific attention - Person X is among the top 0.01% of people interested in Person-X-related content. So by using their name in public you get a shortcut to put your argument in front of their eyes.

**Counterblunder writes:**

> Re #8: I briefly dated someone who is very involved in political activism scenes, and according to her the model that is super popular right now is called the "momentum model": <https://www.momentumcommunity.org/momentum-model>, original book here: <http://thisisanuprising.org/> . Although this might be more on the "social change" (i.e., get society to shift on controversial issues) rather than targeted political change for ideas that are already mostly accepted.

Yeah, I think some combination of “social change is oversupplied compared to political change” and “my personal use cases are probably bottlenecked more by political than social change”.

**ColdButtonIssues (**[blog](https://coldbuttonissues.substack.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata)**) writes:**

> This book exists. It's called Organizing for Social Change and is put out by a lefty organizer training group called MidWest Academy. Of course, the tactics can also be used by conservatives and libertarians. It's very practical!

I will check it out, but again, I think “organizing” and “social change” are oversupplied and not exactly what I want to know about.

That is, my guess is that there are a lot of people who love the idea of holding protests and putting up posters, and are very good at these things. But I expect most of this doesn’t connect to anything valuable; they hold the protest, there’s a lot of shouting, and nobody knows what to do after that. And protests and organizing are mostly good for, I don’t know, overthrowing the capitalist order, and not for getting a sentence changed in page 1069 of the security regulations bill (even if that sentence is actually contributing to some of what people hate about the capitalist order). There has to be some other part where you contact some representative, raise the idea that this part of the security bill should be changed, and then _maybe,_ if they say no for some very specific reason, you hold a protest and arrange for them to hear about it. But everyone seems to want to jump to becoming an expert in organizing the protest, and that doesn’t seem like the most heavily bottlenecked part to me.

**Peregrine Journal (**[blog](https://peregrinejournal.substack.com/?utm_source=substack&utm_medium=web&utm_content=comment_metadata)**) writes:**

> +1 to number 8. Political change is accompanied by a bunch of idiosyncratic features like the single issue rule. so once you get a lobbyist to support your boutique cause of, say, increasing funding for law libraries, your next step is to simply propose a bill for funding law libraries.
> 
> Haha, no, that would never get traction.
> 
> Your next move is to sit and wait for a bill on a vaguely related topic, such as on educational funding, the legal profession, or maybe inner city youth programs or something you can just squint and draw a connection to. Then you push like crazy to get your bit added to the larger bill and hope you tied your trailer to a star.
> 
> These are not stupid questions at all, the system is full of absurd corners like this and I too want this collected in a book somewhere.
> 
> This is notably complicated by the various forms of political change in the country, to include lawmaking and executive orders, but also the quiet dominance of administrative rulemaking. A proper treatment would balance the impact of all of these.
> 
> I don't think your questions are stupid at all, I think you have a great instinct for the non-obvious corners in lots of areas, including here. My dream version of this book would include a series of interviews, one with a professional lobbyist, one with a congressional staffer, one with an administrative law judge or maybe someone who has run a notice and comment process for an executive agency, one with a lawyer who has had to interpret EOs maybe in the intel community or adjacent, a longtime DC journalist, then some coverage or state and local lawmaking and where they fit in. My book's corpulent title would be something like "The civics they never taught you: The unwieldy billion and one paths to making new laws in America (and why none of them really work but maybe that's mostly ok)."
> 
> I would love to quit my job and go on an interview tour but I have a family to support and lack any reputation that would land me any of these interviews. How do you hire somebody to write a book to spec?

**Erusian[writes](/p/quests-and-requests/comment/42986299):**

> You know, I'm increasingly convinced this is just some kind of weird local knowledge. I feel like my government is pretty responsive but this is because I know who to reach out to or where to show up for public hearings or whatever. Anyone else could do this if they had that same knowledge but most people... just don't bother, I guess? It's weird. Government is really important. And local governments especially. And it's not really that hard to access.
> 
> I think the issue is that people want to outsource the work but also hate principal-agent problems. But mostly complain instead of doing anything about. Basically, if you have such access the incentive is to monetize it or serve as a specialized intermediary instead of putting it out to the general public. Both for venal reasons and because, to be honest, most people you teach don't bother to follow through. Also, most of it isn't learned from a book but from a series of experiences.
> 
> Anyway, to answer:
> 
> _> Presumably the first step is convincing a member of Congress or the administrative state. How do you do this?_
> 
> Step one is getting into a room with them. Step two is just normal persuasion. Step two is the harder part. Step 3 is even harder: getting them to prioritize it.
> 
> _> you should get articles in newspapers, sign petitions, and hold some protests._
> 
> Eh, maybe? What you really need to convince them of is one of two things: either that it's correct (either in a moral or technical sense) or that it will win them votes. Ideally both. Keep in mind they have their own ideas of what wins/loses votes and what's right/wrong. Protests or whatever are just an honest signal of #2.
> 
> _> Is there a way to avoid this? Is this your Congressman’s problem, or your problem?_
> 
> It's your job to make it a battle leadership chooses to fight and to smooth it as much as possible for them. This gets into the process of whipping. Your job as an interest group is to convince leadership and then make the whipping process as easy as possible. The easier it is the less whipping that needs to be done and so the more likely leadership is to do it.
> 
> _> If you want to convince the administrative state to make/repeal some regulation, do you write a letter to the appropriate official? How do you know who that is? Do they care about letters? Do they care how many protests you’ve organized?_
> 
> The administrative state is regulation bound. You can convince them but only through strict procedures. Comment periods, briefs, etc. Politicians get to take initiative but bureaucrats generally don't. They act according to the rules or follow orders. They specifically do not want you convincing individual bureaucrats and to instead deal with the institution. They don't care how many protests you've organized but their bosses might.
> 
> Anyway, serious question: if EA is really so full with money and talent and wants to do some good why doesn't it just get someone appointed ambassador to some poor African country? It's not like there's a lot of competition or that anyone would object to the ambassador running around trying to get charity done. A lot of them are supposed to be conduits for aid there anyway. And it's a good chance to grow connections among elites and know who's trustworthy etc.

Some of this brushes against the parts I don’t understand. Yeah, whipping the rank and file sounds like the way to get something passed. But as hard as it is to get an audience with your congressman, surely it’s even harder to get an audience with the Majority Whip. So what’s the plan here?

As for EA: I don’t make strategy and don’t know if anyone’s ever debated this, but my answers would be - “EA” is not a unified actor and it’s not clear what org would take point on this process, getting someone made an ambassador seems like a lot of work and string-pulling for a mostly sinecure position that doesn’t have much direct power, EA isn’t very good at lobbying except in a few areas (like AI) where it’s invested a lot in capacity, and EA doesn’t claim to have any amazing ideas for revolutionizing foreign policy (including foreign policy in development countries). I don’t know, maybe someone should be doing this; like I said, I don’t think there’s currently an org with the money and talent and PR and lobbying to make this work.

**Rep. Tristan Roberts[writes](/p/quests-and-requests/comment/42990722):**

> #8. A good primer on political change -- written from the inside
> 
> I've been writing my own case study on the journey from being an informed citizen w/ ideas to an involved citizen who has taken an idea into a bill that's been signed into law.
> 
> I try approach the Legislature, and writing about it, with "beginner's mind," because I like learning. I started an email newsletter/blog when I began my first campaign for state office last year. It's a behind-the-scenes journal to keep constituents informed.
> 
> I've received remarkable feedback from a diverse slice of voters who tell me that they feel far more informed about how things work, and they find it very readable. Example posts are below.
> 
> I do this newsletter as an unpaid part of my job to inform Vermonters, but I'd love to turn it into a book that provides answers to your questions.
> 
> We gavel in January 3rd and run through May. I have several policy areas where I'm trying to make some change. As a first-term state legislator, I don't have a lot of influence. I'm not a 6-term veteran who chairs a powerful committee. I'm a farmer, writer, and sustainability professional.
> 
> This makes things more interesting to me because if the policies that I care about get anywhere in 2024, it'll be more based on merit than seniority. I'm sure there are useful lessons in the memoirs of retired power brokers. But I'll give you a timely and accessible chronicle on what is working and what isn't working today on the question, "What’s the strategy for turning a good idea into law?"
> 
> That's what I can offer this project. I already have a lot into it, and I have an approach, but I'd love to work with a team and to be challenged on my assumptions. I feel strongly that everything gets better with collaboration.
> 
> If you have any inkling that you feel like-minded and want to contribute useful constraints/questions, writing or other media, editing, etc. -- let's talk!
> 
> I'm not waiting for financial backing to move forward with this project, but I am looking for a financial model and source of investment to bring this content to a wider audience. I'd be grateful for any support, or pointers on finding grants.
> 
> Thanks for reading this comment. Have an awesome rest of your day!
> 
> -Tristan [tristan@tristanroberts.org](mailto:tristan@tristanroberts.org)
> 
> P.S. Examples:
> 
> what's better, delegate model or trustee model of representation? <https://tristanroberts.org/news/trust-through-agreement-and-trust-through-disagreement>
> 
> how to deal with toxicity on social media while forming a local caucus? <https://tristanroberts.org/news/how-should-i-respond-to-fpf>
> 
> finding hope in what's working locally <https://tristanroberts.org/blog/do-you-have-hope-for-our-kids>
> 
> how does a legislator decide what's a constitutional gun law, when experts disagree? <https://tristanroberts.org/news/a-law-without-the-governors-signature>
> 
> how bicameralism's inefficiencies are a feature, not a bug: <https://tristanroberts.org/news/no-to-excuses-yes-to-second-chances>
> 
> Better yet, get updates like these in real-time: <https://pages.tristanroberts.org/signup> :-)

**Colin C[writes](/p/quests-and-requests/comment/42985834):**

> The problem with #8 is that there are orders of magnitude more "good ideas" for new laws than there is legislative capacity. In the current system, most of those good ideas don't even get the attention of someone in Congress. But if someone figured out the "cheat code" and publicized it, congresspeople would be overwhelmed, and they'd develop new filters for getting their attention.
> 
> Scott's idea sounds kind of like Search Engine Optimization - there's thousands of websites competing for the first few Google results, and as soon as someone figures out a way to game the system, Google changes the algorithm and that game no longer works. It's an arms race between you, all your competitors, and Google.
> 
> Someone else pointed out that the current system is lobbying is already designed to address this issue. And the general public is always complaining about lobbyists - making them more effective would just make the public even more mad, and nudge us even more toward vetocracy.

This is an interesting way to think about the problem, thanks!
