---
title: "Asterisk/Zvi on California's AI Bill"
subtitle: "..."
date: 2024-05-08
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/144429673/comments?&all_comments=true
image: https://substack-post-media.s3.amazonaws.com/public/images/0dcba83a-3b2d-488a-8db7-b851f22caec1_1021x687.png
original-url: https://www.astralcodexten.com/p/asteriskzvi-on-californias-ai-bill
---
California’s state senate is considering [SB1047](https://legiscan.com/CA/text/SB1047/2023), a bill to regulate AI. Since OpenAI, Anthropic, Google, and Meta are all in California, this would affect most of the industry.

If the California state senate passed a bill saying that the sky was blue, I would start considering whether it might be green, or colorless, or maybe not exist at all. And people on Twitter have been saying that this bill would ban open-source AI - no, all AI! - no, all technology more complicated than a toaster! So I started out skeptical.

But [Zvi Mowshowitz](https://thezvi.substack.com/p/q-and-a-on-proposed-sb-1047) ([summary article in ](https://asteriskmag.com/issues/06/why-is-everyone-suddenly-furious-about-ai-regulation)_[Asterisk](https://asteriskmag.com/issues/06/why-is-everyone-suddenly-furious-about-ai-regulation)_ , [long FAQ on his blog](https://thezvi.substack.com/p/q-and-a-on-proposed-sb-1047)) has looked at it more closely and found:

  * It’s actually a pretty good bill.

  * The reason it sounded like a bad bill before was that people were misrepresenting what it said.




The bill applies to “frontier models” trained on > 10^26 FLOPs - in other words, models a bit bigger than any that currently exist. GPT-4 doesn’t qualify, but GPT-5 probably will. It also covers any model equivalent to these, ie anything that uses clever new technology to be as intelligent as a current 10^26 FLOPs model without actually using that much compute. It places three[^1] types of regulation on these models:

**First** , companies have to train and run them in a secure environment where “advanced persistent threats” (eg China) can’t easily hack in and steal them[^2]. 

**Second,** as long as the model is on company computers, the company has to be able to shut it down quickly if something goes wrong.

**Third,** companies need to test to see if the model can be used to do something really bad. Its three categories of really bad things are:

  1. Create nukes or other weapons of mass destruction. This can’t be something dumb like linking the user to the Wikipedia page for uranium. It has to help human terrorists “in a way that would be significantly more difficult . . . without access to a covered model”.

  2. Cause > $500 million in damage through “cyberattacks” on critical infrastructure (this has to be a single event, not a hundred different $5 million hacks)

  3. Go rogue and commit some other crime that does > $500 million in damage[^3].




If the tests show that the model _can_ do these bad things, the company has to demonstrate that it _won’t_ , presumably by safety-training the AI and showing that the training worked. The kind of training AIs already have - the kind that prevents them from saying naughty words or whatever - would count here, as long as “the safeguards . . . will be sufficient to prevent critical harms.”

So the bill isn’t about regulating deepfakes or misinformation or generative art. It’s just about nukes and hacking the power grid.

There are some good objections and some dumb objections to this bill. Let’s start with the dumb ones:

_Some people think this would literally ban open source AI._ After all, doesn’t it say that companies have to be able to shut down their models? And isn’t that impossible if they’re open-source? No. The bill specifically says[^4] this only applies to the copies of the AI still in the company’s possession[^5]. The company is still allowed to open-source it, and they don’t have to worry about shutting down other people’s copies. 

_Other people think this would make it prohibitively expensive for individuals and small startups to tinker with open-source AIs_. But the bill says that only companies training giant foundation models have to worry about any of this. So if Facebook trains a new LLaMA bigger than GPT-5, they’ll have to spend some trivial-in-comparison-to-training-costs amount to test it in-house and make sure it can’t make nukes before they release it. But after they do that, third-party developers can do whatever they want to it - re-training, fine-tuning, whatever - without doing any further tests.

_Other people think all the testing and regulation would make AIs prohibitively expensive to train, full stop_. That’s not true either. All the big companies except Meta already do testing like this - here’s [Anthropic’s](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf), [Google’s,](https://arxiv.org/abs/2403.13793) and [OpenAI’s](https://arxiv.org/pdf/2303.08774) \- that already approximate the regulations. Training a new GPT-5 level AI is so expensive - hundreds of millions of dollars - that the safety testing probably adds less than 1% to the cost. No company rich enough to train a GPT-5 level AI is going to be turned off by the cost of asking it “hey can you create super-Ebola?”, and putting the answer into a nice legal-looking PDF. This isn’t the “create a moat for OpenAI” bill that everyone’s scared of[^6].

_Other people are freaking out over the “certification under penalty of perjury”_. In some cases, developers have to certify under penalty of perjury that they’re complying with the bill. Isn’t this crazy? Doesn’t it mean if you make a mistake about your AI, you could go to jail? This is extremely misunderstanding how law works. Perjury means you can’t deliberately lie, something which is hard to prove and so rarely prosecuted. More to the point, half of the stuff I do in an average day as a medical doctor is certified under penalty of perjury - filling out medical leave forms is the first one to come to mind. This doesn’t mean I go to jail if my diagnosis is wrong. It’s just the government’s way of saying “it’s on the honor system”.

What are some of the reasonable objections to this bill?

_Some people think the requirement to prove the AI safe is impossible or nearly so._ This is Jessica Taylor’s main point [here](https://unstablerontology.substack.com/p/thoughts-on-sb-1047), which is certainly correct for a literal meaning of “prove”. Zvi points out that it just says “reasonable assurance”, which is a legal term for “you jumped through the right number of hoops”. In this case probably the right number of hoops is doing the same kind of testing that OpenAI/Anthropic/Google are currently doing, or that AI safety testing organization METR recommends. The bill gestures at the National Institute of Standards and Technology a few times here, and NIST just named one of METR’s founders as their AI safety czar, so I would be surprised if things didn’t end going this direction. METR’s tests are possible and many AI models have successfully passed earlier versions.

_Other people are worried about a weird rule that you can’t train an AI if you think it’s going to be unsafe_. After some simple points about having a safety policy set up before training, the bill adds that you should:

> Refrain from initiating training of a covered model if there remains an unreasonable risk that an individual, or the covered model itself, may be able to use the hazardous capabilities of the covered model, or a derivative model based on it, to cause a critical harm.

This makes less sense than all the other rules - you can test a model post-training to see if it’s harmful, but this seems to suggest you should know something before it’s trained. Is this a fully general “if something bad happens, we can get angry at you”? I agree this part should be clarified. 

_Other people think the benchmarking clause is too vague._ The law applies to models trained with > 10^26 FLOPs, or any model that uses advanced technology to be equally as good despite less compute. Equally as good how? According to benchmarks. Which benchmarks? The law doesn’t say. But it does say that the Technology Department will hire some bureaucrats to give guidance on this. I think this is probably the only way to do this; it’s too easy to fake any given benchmark. Every AI company already compares their models to every other AI company on a series of benchmarks anyway, so this isn’t demanding they create some new institution. It’s just “use common sense, ask the bureaucrats if you’re in a gray area, a judge will interpret it if it comes to trial”. This is how every law works. 

_Other people complain that any numbers in the bill that make sense now may one day stop making sense._ Right now 10^26 FLOPs is a lot. But in thirty years, it might be trivial - within the range that an academic consortium or scrappy startup might spend to train some cheap _ad hoc_ AI. Then this law will be unduly restrictive to academics and scrappy startups. I assume that numbers will be updated when they no longer make sense - California’s minimum wage was originally $0.15 per hour - but if you think the government will drop the ball on this, it might affect AI versatility thirty years from now - if we’re still around.

_Other people note that this will *eventually* make open source impossible._ Someday AIs really _will_ be able to make nukes or pull off $500 million hacks. At that point, companies will have to certify that their model has been trained not to do this, and that it will stay trained. But if it were open-source, then anyone could easily untrain it. So after models become capable of making nukes or super-Ebola, companies won’t be able to open-source them anymore without some as-yet-undiscovered technology to prevent end users from using these capabilities. Sounds . . . good? I don’t know if even the most committed anti-AI-safetyist wants a provably-super-dangerous model out in the wild. Still, what happens after that? No cutting-edge open-source AIs ever again? I don’t know. In whatever future year foundation models can make nukes and hack the power grid, maybe the CIA will have better AIs capable of preventing nuclear terrorism, and the power company will have better AIs capable of protecting their grid. The law seems to leave open the possibility that in this situation, the AIs wouldn’t technically be capable of doing these things, and could be open-sourced. 

(or you could base your Build-A-Nuke-Kwik AI company in some state other than California.)

Finally - last week discussed Richard Hanania’s _[The Origin Of Woke](/p/book-review-the-origins-of-woke)_ , which claimed that although the original Civil Rights Act was good and well-bounded and included nothing objectionable, courts gradually re-interpreted it to mean various things much stronger than anyone wanted at the time. This bill tells the Department of Technology to offer guidance on what kind of tests AI companies should use. I assume their first guidance will be “the kind of safety testing that all companies except Meta are currently doing”, because those are good tests, and the same AI safety people who helped write those tests probably also helped write this bill. But Hanania’s book, and the process of reading this bill, highlight how vague and complicated all laws can be. The same bill could be excellent or terrible, depending on whether it’s interpreted effectively by well-intentioned people, or poorly by idiots. That’s true here too.

The best I can say against this objection is that this bill seems better-written than most. Many of the objections to its provisions seem to not understand how law works in general (cf. the perjury section) - the things they attack as impossible or insane or incomprehensibly vague are much easier and clearer than their counterparts in (let’s say) medicine or aerospace. Future AIs stronger than GPT-4 seem like the sorts of things which - like bad medicines or defective airplanes - could potentially cause damage. This sort of weak regulation that exempts most models and carves out a space for open-sourcing seems like a good compromise between basic safety and protecting innovation. I join people like Yoshua Bengio and Geoffrey Hinton in supporting it.

Regardless of your position, I urge you to pay attention to the conversation and especially to [read Zvi’s ](https://asteriskmag.com/issues/06/why-is-everyone-suddenly-furious-about-ai-regulation)_[Asterisk](https://asteriskmag.com/issues/06/why-is-everyone-suddenly-furious-about-ai-regulation)_[ article](https://asteriskmag.com/issues/06/why-is-everyone-suddenly-furious-about-ai-regulation) or [his longer FAQ on his blog](https://thezvi.substack.com/p/q-and-a-on-proposed-sb-1047). I think Zvi provides pretty good evidence that many people are just outright lying about - or at least heavily misrepresenting - the contents of the bill, in a way that you can easily confirm by [reading the bill itself](https://legiscan.com/CA/text/SB1047/2023). There will be many more fights over AI, and some of them will be technical and complicated. Best to figure out who’s honest now, when it’s trivial to check!

If you disagree, I’m happy to make bets on various outcomes, for example:

  * If this passes, will any big AI companies leave California? (I think no)

  * If this passes, will Meta stop open-sourcing their AIs in the near term, ie before the AIs can make nukes or hack the power grid? (I think no)

  * If this passes, will AI companies report spending a large percent of their budgets on compliance, far beyond what they do now? (I think no)




[^1]: It also demands that compute clusters implement some Know Your Customer laws, and creates an official State Compute Cluster for California. I’m ignoring these because nobody has expressed much of an opinion on them. The State Compute Cluster for California isn’t on anyone’s AI safety list, and I assume it’s part of some bargaining with some other interest group.

[^2]: And, incidentally, where the AI can’t break _out_.

[^3]: The difference between (2) and (3) is that (2) triggers if a malicious human tells the AI to do the hack, but (3) only triggers if the AI becomes sentient or something and commits the crime itself. 

[^4]: “Full shutdown means the cessation of operation of a covered model, including all copies and derivative models, on all computers and storage devices within custody, control, or possession of a person”, where “person” is elsewhere defined to mean corporation. I agree this is a little ambiguous, but _Asterisk_ talked to the state senator’s office and they confirmed that they meant the less-restrictive, pro-open-source meaning.

[^5]: Is this a loophole that makes the law useless? I think no - as we’ll see later, companies won’t be able to open-source certain models that are proven to have very dangerous capabilities. This part is probably aimed at those.

[^6]: AFAICT OpenAI and other big labs haven’t expressed a position on this bill, and I can’t guess what their position is.
