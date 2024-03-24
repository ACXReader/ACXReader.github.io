---
title: "Highlights From The Comments On Motivated Reasoning And Reinforcement Learning"
subtitle: "..."
date: 2022-02-11
likes: 34
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/48285380/comments?&all_comments=true
image: https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/83e12a5a-c404-4fe3-b039-13a428458942_680x510.jpeg
original-url: https://www.astralcodexten.com/p/highlights-from-the-comments-on-motivated
---
**I. Comments From People Who Actually Know What They’re Talking About**

Gabriel [writes](https://astralcodexten.substack.com/p/motivated-reasoning-as-mis-applied/comment/4822086):

> The brain trains on magnitude and acts on sign.
> 
> That is to say, there are two different kinds of "module" that are relevant to this problem as you described, but they're not RL and other; they're both other. The learning parts are not precisely speaking reinforcement learning, at least not by the algorithm you described. They're learning the whole map of value, like a topographic map. Then the acting parts find themselves on the map and figure out which way leads upward toward better outcomes.
> 
> More precisely then: The brain learns to predict value and acts on the gradient of predicted value.
> 
> The learning parts are trying to find both opportunities and threats, but not unimportant mundane static facts. This is why, for example, people are very good at remembering and obsessing over intensely negative events that happened to them -- which they would not be able to do in the RL model the post describes! We're also OK at remembering intensely positive events that happened to us. But ordinary observations of no particular value mostly make no lasting impression. You could test this by a series of 3 experiments, in each of which you have a screen flash several random emoji on screen, and each time a specific emoji is shown to the subject, you either (A) penalize the subject such as with a shock, or (B) reward the subject such as with sweet liquid when they're thirsty, or (C) give the subject a stimulus that has no significant magnitude, whether positive or negative, such as changing the pitch of a quiet ongoing buzz that they were not told was relevant. I'd expect subjects in both conditions A and B to reliably identify the key emoji, whereas I'd expect quite a few subjects in condition C to miss it.
> 
> By learning associates with a degree of value, whether positive or negative, it's possible to then act on the gradient in pursuit of whatever available option has highest value. This works reliably and means we can not only avoid hungry lions and seek nice ripe bananas, but we also do compare two negative or two positives and choose appropriately: like whether you jump off a dangerous cliff to avoid the hungry lion, or whether you want to eat the nice ripe banana yourself or share it with your lover to your mutual delight. The gradient can be used whether we're in a good situation or a bad one. You could test this by adapting the previous experiment: associate multiple emoji with stimuli of various values (big shock, medium shock, little shock, plain water, slightly sweet water, more sweet water, various pitch changes in a background buzz), show two screens with several random emoji, and the subject receives the effect of the first screen unless they tap the second. I'd expect subjects to learn to act reliably to get the better of the two options, regardless of sign, and to be most reliable when the magnitude difference is large.
> 
> For an alternative way of explaining this situation, see Fox's comment, which I endorse.
> 
> OK, now to finally get around to motivated reasoning. The thoughts that will be promoted to your attention for action are those that are the predicted to lead to the best value. You can roughly separate that into two aspects as "salience = probability of being right * value achieved if right". Motivated reasoning happens when the "value achieved if right" dominates the "probability of being right". And well, that's pretty much always, in abstract issues where we don't get clear feedback on probabilities. The solution for aspiring skeptics is to heap social rewards on being right and using methods that help us be more right. Or to stick to less abstract claims. You could test this again by making the emojis no longer a certainty of reward/penalty, but varying probabilities.
> 
> Source: I trained monkeys to do neuroscience experiments.

That comment by [Fox](https://astralcodexten.substack.com/p/motivated-reasoning-as-mis-applied/comment/4819605) is:

> The underlying intuition here about reinforcement learning is incorrect.
> 
> _> Plan → higher-than-expected hedonic state → do plan more_
> 
> No, it's: higher (relative to other actions) hedonic future state *conditioned on current state*. The conditioning is crucial. Conditioned on there being a lion, RL says you should run away because it's better than not running away.
> 
> It gets tricky with partial observability, because you don't know the state on which you have to condition. So instead, says RL theory (not so much practice, which is a shame), you can condition on your belief-state, *but only if it's the Bayesian belief-state*. If you're not approximately Bayesian, you get into the kind of trouble the post mentions.
> 
> But being Bayesian is the RL-optimal thing to do. You get to the best belief state possible: if there's a lion, you want to believe there's a lion, litany-of-Tarsky style. The visual cortex could, in principle, be incentivized to recognized lions through RL.
> 
> I suspect people don't open IRS letters not because their RL is fundamentally broken, but because their reward signal is broken. They truly dislike IRS letters, and the pain it causes to open one is truly more than their expected value. People probably also underestimate the probability and cost of a bad IRS letter, but that's due to poor estimation, not poor deduction from that estimation.
> 
> Perhaps it's easier to see in organizations, where you can tell the components (individuals) apart. It's sometimes hard to tell apart the bearer-of-bad-news from the instigator-of-bad-news. This disincentivizes bearers, who might be mistaken for instigators. With enough data, you can learn to tell them apart. Until you do, disincentivizing bearers to the extent that they really could be instigators is the optimal thing to do.

I agree that if we were perfect Bayesian reasoners, the knowledge that there was now a 5% chance of there being a lion would propagate throughout all brain regions and they could condition on this immediately.

And yet a few days ago, I (on a diet) visited some friends who sometimes leave delicious brownies on their counter. I worried that if I saw the brownies, I would eat them, so I tried not to look at the counter. But part of me felt bad that I was passing up the opportunity to eat delicious brownies, so my split-second reaction as I walked through their kitchen was to compromise by looking towards the _edge_ of their counter to check for brownies, but to deliberately exclude from my vision the part of the counter where the brownies were most likely to be.

This makes me think that the parts of my brain doing active inference are not quite perfect Bayesians making perfect updates.

[Steve Byrnes](https://astralcodexten.substack.com/p/motivated-reasoning-as-mis-applied/comment/4817879):

> I pretty much agree with everything you said.
> 
> One of 5 or so places in the brain that can get a dopamine burst when a bad thing happens (opposite of the usual) is closely tied to inferotemporal cortex (IT). I talked about it in "Example 2C" here - <https://www.lesswrong.com/posts/jrewt3rLFiKWrKuyZ/big-picture-of-phasic-dopamine#Example_2C__Visual_attention> Basically, as far as I can tell, IT is "making decisions" about what to attend to within the visual scene, and it's being rewarded NOT for "things are going well in life", but rather for "something scary or exciting is happening". So from IT's own narrow perspective, noticing the lion is very rewarding. (Amusingly, "noticing a lion" was the example in my blog post too!)
> 
> Turning to look at the lion is a type of "orienting reaction", I think. I'm not entirely sure of the details, but I think orienting reactions involve a network of brain regions one of which is IT. The superior colliculus (SC) is involved here too, and SC is ALSO not part of the "things are going well in life" RL system—in fact, SC is not even in the cortex at all, it's in the brainstem.
> 
> So yeah, basically, looking at the lion mostly "isn't reinforceable", or to the extent that it is "reinforceable", it's being reinforced by a different reward signal, one in which "scary" is good, as far as I understand right now.
> 
> Deciding to open an email, on the other hand, has basically nothing to do with IT or superior colliculus, but rather involves high-level decision-making (dorsolateral prefrontal cortex maybe?), and that bran region DOES get driven by the main "things are going well in life" reward signal.

But check out [the rest of](https://astralcodexten.substack.com/p/motivated-reasoning-as-mis-applied/comment/4823160) the comment subthread for some pushback against and clarification of this model. 

**II. Arguments That The Long-Term Rewards Of Spotting The Lion Outweigh The Short-Term Drawbacks**

Here are three comments that I think say about the same thing from different angles.

[Phil](https://astralcodexten.substack.com/p/motivated-reasoning-as-mis-applied/comment/4817922):

> Not sold on the "visual-cortex-is-not-a-reinforcement-learner" conclusion. If the objective is to maximize total reward (the reinforcement learning objective), then surely having your day ruined by spotting a tiger is better than ignoring the tiger and having your day much more ruined by being eaten by said tiger. (i.e.: visual cortex is "clever" and has incurred some small cost now in order to save you a big cost). Total reward is the same reason humans will do any activities with delayed payoffs.

[KJZ](https://astralcodexten.substack.com/p/motivated-reasoning-as-mis-applied/comment/4823531):

> Rather than a purely "is reinforceable" vs "isn't reinforceable" distinction I suspect the difference has more to do with the relevant timescales for reinforcement. In the foot injury case, we'd have a very fast gait correction reinforcement loop trying to minimize essentially instantaneous pain. In the lion country case it sounds like something slightly longer timescale -- we make a plan to go to lion country and then learn maybe a few hours later that the plan went poorly so we shouldn't make such plans again. In the taxes case it's much longer term, it might take years before the IRS manages to garnish your wages, though you'll still eventually likely get real consequences. Politics on the other hand, often cost/reward is so diffuse and long-term that I suspect the only reason anyone is ever right about difficult policy issues is because the cognitive processes that correctly evaluate them happen to be useful for other reasons. The vision example I think is a mistake of timescale; a vision system which learned to not see something unpleasant would get a much worse net reward when you don't avoid the lion you could have seen and subsequently get mauled.
> 
> I'm coming at this from the ML side so I'm out of my depth biologically, but perhaps we have different relevant biological RL processes with different timescales? Eg, pain for ultra-short timescale reinforcement, dopamine for short-to-medium timescale reinforcement, and some higher-level cognitive processes for medium-to-long timescale reinforcement.\

[Mike](https://astralcodexten.substack.com/p/motivated-reasoning-as-mis-applied/comment/4818286): 

> I think all of the supposed discrepanices with modeling the brain as a hedonic reinforcement learning model can be explained with standard ML and economics. If you do a lot of research on epistemic facts related to your political beliefs, the first order consequence is often that you spend hours doing mildly unpleasant reading, then your friends yell at you and call you a Nazi. In the case of doing your taxes or the lion, that unpleasantness is modulated by the much larger unpleasantness of being sued by the IRS and/or eaten alive by a lion. So there's a normal tradeoff between costs (filing taxes is boring, seeing lions is scary) and benefits (not being sued or devoured).

I feel like we can thought-experiment our way out of this. Suppose I invest in Bitcoin, then check its price every day. There is a little up arrow or down arrow next to some number and percent. Some days it’s a green up arrow and I feel good and smart and rich. Other days it’s a red down arrow and I feel bad and dumb and poor. None of this ever gets confirmed by any kind of ground truth, because I am HODLing and will never sell my Bitcoins until I retire. So how come I don’t start hallucinating that the arrow is green and points up? Every time I’ve “taken the action” of seeing a green upward-pointing arrow, I’ve felt better; every time I’ve taken the opposite action, I’ve felt worse!

You can no longer appeal to the “the ultimate reinforcement is whether you got mauled by a lion or not”, because I’ve never sold my Bitcoin and gotten any form of reinforcement more final than checking the arrow (if you want, imagine that I get hit by a truck at age 64 and _never_ sell the Bitcoin). 

I don’t want to say “epistemics are protected from reinforcement learning” is the only way out of this. It could be that the visual cortex gets reinforced at the level of broad principles, and any change that caused you to flip the direction and color of the arrow would have to change really fundamental things that would make your vision worse in other ways. But it doesn’t seem like “ultimate reinforcement” is what’s preventing this from happening, since there is none.

Also, behavioral reinforcement learning is nowhere near this good. You might think that the short-term reward of eating brownies wouldn’t change behavior because the _real_ reward we should be considering is the reward of being healthy and looking good. But this works very inconsistently, as opposed to the “see lions as lions” thing which works all the time.

**III. Am I Ignoring The Many Practical Reasons For People To Have Motivated Reasoning?**

[Melvin](https://astralcodexten.substack.com/p/motivated-reasoning-as-mis-applied/comment/4818536):

> I think you're thinking about this too much from a model where everybody is a good-faith Mistake Theorist.
> 
> In a mistake theory model, it's a mystery why people fail to update their beliefs in response to evidence that they're wrong. If the only penalty for being wrong is the short term pain of realising that you'd been wrong, then what you've written makes sense.
> 
> I think that most people tend to be conflict theorists at heart, though, using mistake theory as a paper-thin justification for their self interest. When I say "Policy X is objectively better for everybody", what I mean is "Policy X is better for me and people I like, or bad for people I hate, and I'm trying to con you into supporting it".
> 
> There's no mystery, in this model, why people are failing to update their "Policy X is objectively better" argument based on evidence that Policy X is objectively worse; they never really cared whether Policy X was objectively better in the first place, they just want Policy X.

I commented:

> I think there are three things: honest mistakes, honest conflicts, and bias - with this last being a state in which you "honestly believe" (at least consciously) whatever is most convenient for you.
> 
> If a rich person says the best way to help the economy is cutting taxes on rich people, or a poor person says the best way to help the economy is to stimulate spending by giving more to the poor, it's possible that they're thinking "Haha, I'm going to pull one over on the dumb people who believe me". 
> 
> But it also seems like even well-intentioned rich/poor people tend to be more receptive to the arguments that support their side, and genuinely believe them.
> 
> I don't think honest mistakes or honest conflicts need much of an explanation, but bias seems interesting and important and worth figuring out.

XPYM [asks](https://astralcodexten.substack.com/p/motivated-reasoning-as-mis-applied/comment/4828007):

> Is the conventional explanation unsatisfactory? That people are more convincing when they argue for their position honestly, and so it's beneficial for them to become biased in ways that favor their interests.

This answers the “why” question but not the “how” question. If you wonder why animals can see, the answer is “it’s useful for spotting food and predators and stuff”. If you wonder _how_ animals can see, the answer is a giant ophthalmology textbook and lots of stuff about rods and cones. 

One of the ideas that’s had the biggest effect on me recently is thinking about how small the genome is and how poorly it connects to the brain. It’s all nice and well to say “high status leaders are powerful, so people should evolve a tendency to suck up to them”. But in order to do that, you need some specific thing that happens in the genome - an adenine switched to a guanine, or something - to give people a desire to suck up to high-status leaders. Some change in the conformation of a protein has to change the wiring of the brain in some way such that people feel like sucking up to high-status leaders is a good idea. This isn’t impossible - evolution has managed weirder things - but it’s _so, so hard_. Humans have like 20,000 genes. Each one codes for a protein. Most of those proteins do really basic things like determine how flexible the membrane of a kidney cell should be. You _can’t_ just have the “how you behave towards high status leaders” protein shift into the “suck up to them” conformation, that’s not how proteins work!

You should penalize theories really heavily for every piece of information that has to travel from the genome to the brain. It certainly should be true that people try to spin things in self-serving ways: this is [Trivers’ theory of self-deception and consciousness as public relations agent](https://www.lesswrong.com/posts/DSnamjnW7Ad8vEEKd/trivers-on-self-deception). But that requires communicating an entire new philosophy of information processing from genome to brain. _Unless_ you could do it with reinforcement learning, which you’ve already got.

My take on the motivated-reasoning-as-misapplied-reinforcement-learning theory is something like “we always knew people had to be doing self-deception somehow, I was previously puzzled by how this got implemented, but it turns out it’s a trivial corollary of this other much more fundamental program”.

**IV. Miscellaneous**

[qbolec](https://astralcodexten.substack.com/p/motivated-reasoning-as-mis-applied/comment/4818714):

> How did AlphaStar learn to overcome the fear of checking what's covered by the fog of war?

[Daniel Speyer](https://astralcodexten.substack.com/p/motivated-reasoning-as-mis-applied/comment/4819473):

> Having separate reinforcement and epistemic learners would be the elegant solution. There's also the ugly hack, which is to make "there might be a lion" even scarier than "there is a lion" so that checking is hedonically rewarded with "at least now I know". Successful horror movie directors can confirm evolution went for the ugly hack, as usual.

[NLeseul](https://astralcodexten.substack.com/p/motivated-reasoning-as-mis-applied/comment/4824365):

> One observation: You can't avoid a lion trying to eat you by refusing to look at it. But you might be able to avoid another lecture from your neighbor Ug Bob about how you haven't made the proper blood sacrifices to Azathoth in a while, if you refuse to make eye contact with him and keep walking.
> 
> That is to say, huge parts of our brains developed in order to process social reality. And social reality, unlike physical reality, actually does change based on what information you have (and what information other people know you have, or what information you know other people know you have...). So controlling the timing of when you are seen by people around you to acquire certain information likely does have some degree of survival benefit. And the parts of our brains that learned how to do that are probably the ones that are involved in reading letters from the IRS today.

[tcheasdfjkl](https://astralcodexten.substack.com/p/motivated-reasoning-as-mis-applied/comment/4837036):

> To me the difference between the lion case and the taxes case is something like - how quickly are you going to get feedback on your decision/beliefs? In the lion case, you can't actually avoid learning in short order if there is a lion, because it will probably eat you. In the taxes case, you can avoid it for a pretty long time! Short-term bias is a pretty normal factor in how humans make decisions and it seems pretty applicable here too.
