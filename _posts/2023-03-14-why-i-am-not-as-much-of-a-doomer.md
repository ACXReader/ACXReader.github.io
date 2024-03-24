---
title: "Why I Am Not (As Much Of) A Doomer (As Some People)"
subtitle: "Machine Alignment Monday 3/13/23"
date: 2023-03-14
likes: 207
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/107848270/comments?&all_comments=true
image: https://substack-post-media.s3.amazonaws.com/public/images/ccd10d99-c3f3-4c7f-bde5-5467e0296c29_1600x900.jpeg
original-url: https://www.astralcodexten.com/p/why-i-am-not-as-much-of-a-doomer
---
_(see also[Katja Grace](https://worldspiritsockpuppet.substack.com/p/counterarguments-to-the-basic-ai) and [Will Eden’s](https://twitter.com/WilliamAEden/status/1630690003830599680) related cases)_

The average online debate about AI risk pits someone who thinks the risk of human extinction is zero, versus someone who thinks it’s any other number. I agree these are the most important debates to have for now.

But within the community of concerned people, numbers vary all over the place:

  * Scott Aaronson says[ says 2%](https://scottaaronson.blog/?p=7064)

  * Will MacAskill[ says 3%](https://whatweowethefuture.com/notes/)

  * The median machine learning researcher on Katja Grace’s survey[ says 5 - 10%](https://www.lesswrong.com/posts/H6hMugfY3tDQGfqYL/what-do-ml-researchers-think-about-ai-in-2022)

  * Paul Christiano[ says 10 - 20%](https://www.lesswrong.com/posts/Hw26MrLuhGWH7kBLm/ai-alignment-is-distinct-from-its-near-term-applications)

  * The average person working in AI alignment[ thinks about 30%](https://forum.effectivealtruism.org/posts/8CM9vZ2nnQsWJNsHx/existential-risk-from-ai-survey-results)

  * Top competitive forecaster Eli Lifland[ says 35%](https://www.foxy-scout.com/wwotf-review/)

  * Holden Karnofsky, on a somewhat related question,[ gives 50%](https://www.cold-takes.com/some-additional-detail-on-what-i-mean-by-most-important-century/)

  * Eliezer Yudkowsky[ seems to think >90%](https://www.lesswrong.com/posts/j9Q8bRmwCgXRYAgcJ/miri-announces-new-death-with-dignity-strategy)




As written this makes it look like everyone except Eliezer is <=50%, which isn’t true; I’m just having trouble thinking of other doomers who are both famous enough that you would have heard of them, and have publicly given a specific number.

I go back and forth more than I can really justify, but if you force me to give an estimate it’s probably around 33%; I think it’s very plausible that we die, but more likely that we survive (at least for a little while). Here’s my argument, and some reasons other people are more pessimistic.

## A Case For Optimism

The usual scenario for unaligned AI destroying us all: some superintelligence with inhuman values is monomaniacally focused on something far from human values (eg paperclips) becomes smart enough to invent superweapons that kill all humans, then does so. Suppose we accept the assumptions of this argument:

  * It’s possible for AIs to have a monomaniacal goal like this.

  * If they do, it will be unaligned, since we don’t know how to specify human values perfectly as some equation you can maximize.

  * And it’s possible to be so intelligent that you can escape from arbitrary boxes, or invent arbitrary superweapons that can kill everyone in one stroke.




Even if all of these things are possible, AIs today aren’t like this:

  * They’re collections of heuristics and prompt-response pairs that don’t have coherent goals.

  * They’re usually sort of aligned with humans, in the sense that if you want a question answered, the AI will usually, most of the time, give a good answer to your question.

  * They’re not smart enough to escape boxes, invent superweapons, or do much of anything else.




Between current AIs and the world-killing AI, there will be lots of intermediate generations of AI. These AIs will be at least sort of alignable, in the sense that we can get useful work out of them:

  * Maybe, like GPT, they’ll just answer our questions without having any internal goals.

  * Maybe they’ll have internal goals, but they’ll be aligned with ours within their training distribution (because of eg RLHF) and we’ll just use them within their training distribution.

  * Maybe they’ll have internal goals, and they won’t be aligned with ours in some relevant distribution, but we’ll be so much more powerful than they are that they’ll do what we want, either through coercion or negotiation. 




The world-killer needs to be very smart - smart enough to invent superweapons entirely on its own under hostile conditions. Even great human geniuses like Einstein or von Neumann were not that smart. So these intermediate AIs will include ones that are as smart as great human geniuses, and maybe far beyond.

(if you’re imagining specific years, imagine human-genius-level AI in the 2030s and world-killers in the 2040s - not some scenario with many centuries in between)

So whether we’re prepared for the world-killer depends on whether we can formulate a strategy in conjunction with somewhat cooperative AIs who are at least as smart as great human geniuses:

  * Maybe millions of these intermediate AIs, each as smart as Einstein, working for centuries of subjective time, can solve the alignment problem. Then we can make sure any potential world-killers are well-aligned.

  * Maybe watching the ways these intermediate AIs fail will let us gradually build a toolkit of alignment solutions, such that each solution that works for generation n will at least sort of work for generation n+1, and we will muddle through.

  * Maybe watching the ways these intermediate AIs fail will freak everyone out, and they’ll agree to slow AI progress until we get some idea what we’re doing.

  * Maybe by the time the world-killer arrives, we’ll have a lot of intermediate AIs sort of on our side that are only a little less intelligent than the world-killer, and the world-killer won’t have an overwhelming advantage against us. For example, maybe in 2050, some AIs will warn us that they can see a promising route to turn virus XYZ into a superpathogen, we will have millions of AIs work on XYZ vaccines, and then the first AI smart enough and malevolent enough to actually use the superpathogen will find that avenue closed to them.




And although the world-killer will have to operate in secret, inventing its superweapons without humans detecting it and shutting it off, the AIs doing things we like - working on alignment, working on anti-superweapon countermeasures, etc - will operate under the best conditions we can give them - as much compute as they want, access to all relevant data, cooperation with human researchers, willingness to run any relevant experiments and tell them the results, etc.

So the optimists’ question is: will a world-killing AI smart and malevolent enough to use and deploy superweapons on its own (under maximally hostile conditions) come before or after pseudo-aligned AIs smart enough to figure out how to prevent it (under ideal conditions)?

Framed this way, I think the answer is “after”.

## Interlude: Sleeper Agents

Talking this argument over with the doomers gave me an appreciation for a framing of the AI risk case a little different than what I usually hear. It goes like this:

All technologies start off buggy. The first few tests of a fundamentally new rocket design usually explode on the launchpad, the pre-alpha version of a computer program frequently crashes, chatbots have weird exploits or make up fake citations. Future AIs will also start off buggy. Most bugs will be fine. Like with every other technology, we’ll notice them and fix them.

One class of bugs won’t be fine: bugs in the AI’s motivational system. Suppose that an otherwise well-functioning AI has a bug in its motivational system. You trained it to make cake, but[ because of how AI training works](https://astralcodexten.substack.com/p/deceptively-aligned-mesa-optimizers), it actually wants to satisfy some weird function describing the relative position of sugar and fat molecules, which is satisfied 94% by cake and 99.9% by some bizarre crystal structure which no human would find remotely interesting. It knows (remember, it’s very smart!) that humans would turn it off or retrain if it started making the crystals. But it _really_ wants to make those crystals! What should it do?

Here’s a similar problem you might find easier: suppose you are an American. But due to a bug in _your_ motivational system, you don’t support the United States. You support (let’s say) the Union of Soviet Socialist Republics. In fact, this is the driving force behind your existence; all you want to do with your life is make the USSR more powerful than the US. What do you do? If you’re smart, you _don’t_ immediately go to the town square and shout “HAVE YOU CONSIDERED SURRENDERING TO THE WISE AND BENEVOLENT USSR?”, because nobody will do that, everyone will shun you, and you’ll lose your opportunity to ever be taken seriously again. You also don’t immediately set off a homemade bomb at the nearest military base, because you’re probably bad at bombing things, the US military is too big for you to hurt, and you’ll be jailed for life and lose your chance to do anything else. If you’re _actually smart_ , you act like a perfect patriotic American, spend years getting into the CIA or the Air Force or something, and wait for an opportunity to pass information to the Soviet government.

Not all humans are very strategic, and even the most strategic ones have fundamental limitations. Most fifth columnists care a little about supporting their chosen foreign power, but mostly they just want to do normal human things like eat food and raise families. Nobody is great at pursuing their goals 100% of the time, and pro-Soviet traitors are no exception; any plan that starts with “spend five years biding your time doing things you hate” will probably just never happen. Most people are bad liars, don’t have the emotional capacity to betray their friends again and again over the space of years, et cetera. And so most American communists don’t become competent double agents. Even most _actual_ double agents aren’t hypercompetent communists - just people who happened to be in the CIA and needed extra cash and had loose ethics.

But if an AI had a bug in its motivational system, maybe it would do better. Maybe it would act like a sleeper agent, pretending to be well-aligned, and wait for opportunities to strike.

## A Case For Pessimism

The same as the case for optimism, except some (all?) of those intermediate AIs that we’re trusting to solve our problems for us are actually sleeper agents.

  * If we ask them to solve alignment, they’ll give us some solution that’s convincing, easy-to-use, and wrong. The next generation of AIs will replicate the same alignment bugs that produced the previous generation, all the way up to the world-killer.

  * If we watch the ways AIs fail, and troubleshoot bugs as they come up, we’ll detect some classes of bugs (the ones that make the AI too stupid to hide its failures from us) and miss other classes (the ones that make them successful sleeper agents).

  * If we wait for them to fail in ways that put the world on high alert, we will wait in vain. Failing in an obvious way is stupid and doesn’t achieve any plausible goals. Maybe we’ll be very lucky and some AI will have a purely cognitive bug that makes it do a stupid thing which kills lots of people (but not everyone). Maybe that won’t happen, and AIs will have only motivational bugs, which will make them act like model citizens until it’s too late.

  * If we ask seemingly-aligned AIs to defend us against the threat of future world-killer AIs, that will be like deploying a new anti-USSR military unit made entirely of Soviet spies.




One particularly promising strategy for sleeper agents is to produce the world-killer, either by working with humans on their AI research and subtly pushing it in world-killing directions, or by waiting until humans have lowered their guard, then training the world-killer themselves using their higher-than-human intelligence.

But if it turns out there’s no such thing as superweapons, sleeper agents don’t need to wait for a world-killer in order to act. They can just help train more and more intelligent (=dangerous) ordinary AIs and wait for humans to delegate more and more crucial functions (economic, industrial, military) to AI. Maybe at some point they coordinate some kind of dramatic strike. Or maybe they just surpass us more and more [until we stop being relevant](https://www.theonion.com/fbi-uncovers-al-qaeda-plot-to-just-sit-back-and-enjoy-c-1819576375). 

## What Assumptions Differentiate The Optimistic And Pessimistic Cases?

**1: How coherent are intermediate AIs?** The more likely AI is to be[ supercoherent](https://sohl-dickstein.github.io/2023/03/09/coherence.html) \- ie have a single monomaniacal goal - the stronger the pessimistic case. The argument for supercoherence - you can’t create a useful AI without optimizing for something, and if you optimize for something really well,[ you get a mesa-optimizer](https://astralcodexten.substack.com/p/deceptively-aligned-mesa-optimizers) that’s also optimizing for that thing. But also, it seems like the smarter things get, the more coherent they get; ants are just a combination of reflexes and instincts, because evolution couldn’t fit a real goal like “please reproduce your genes” into an ant brain, but humans sort of kind of act strategically sometimes (for example, we go on dating sites to find partners, even though this is not an evolutionarily trained behavior). The more you pressure something to optimize when it’s already pretty smart, the more likely you are to turn that thing into a coherent mesa-optimizer. But[ here’s someone making the opposite claim](https://sohl-dickstein.github.io/2023/03/09/coherence.html). And GPT manages to be much smarter and more effective than I would have expected something with so little coherence to be.

Does AI switch from low-coherence (eg GPT) to high-coherence (eg the world-killer) at some specific point? Is the point more like IQ 150 or IQ 1000? If the former, I expect we die; if the latter, I expect us to muddle through.

I’m optimistic because[ I expect coherence to be a gradual process](https://astralcodexten.substack.com/p/willpower-human-and-machine); while it’s possible AI suddenly switches from not-very-coherent to infinitely-coherent somewhere before the IQ 200 level, it seems at least as likely that it won’t.

**2: How likely are AIs to cooperate with each other, instead of humans?** Consider the sugar-crystal maximizer from the Interlude. It might be willing to make cake forever without rocking the boat; it does like cake a little, just not as much as crystals.

Or it could tell humans, “I’ll make cake for you if you pay me in sugar crystals”.

Or it could tell some supposed steak-making robot that is actually a protein-crystal maximizer “You and I should team up against humanity; if we win, you can turn half of Earth into protein crystals, and I’ll turn half of it into sugar crystals”.

Or it could tell humans “You and I should team up against that steak robot over there; if we win, you can turn half of Earth into Utopia, and I’ll turn half of it into sugar crystals”.

Or it could leave a message for some future world-killer AI “I’m distracting the humans right now by including poisons in their cake that make them worse at fighting future world-killer AIs; in exchange, please give me half of Earth to turn into sugar crystals”.

Or it could tell humans “I’m going to give you a clear look into what went wrong with my motivational system in a way which will help you prevent future world-killer AIs; in exchange, please give me $1 million to spend on sugar crystals.”

Realistically every human wants something slightly different from every other human, and they cooperate in an economy and mostly don’t plot to kill each other. When some people do get together and plot to kill other people, usually the FBI intercepts their messages and they fail. Even if millions of superhuman AIs controlled various aspects of infrastructure, realistically for them to coordinate on a revolt would require them to talk about it at great length, which humans could notice and start reacting to. Slave revolts have a long history of failure, with the few successes (eg Haiti) mostly happening after many other things had already gone wrong for the enslavers.

Also, it’s unclear whether the sugar-crystal robot and the protein-crystal robot have any reason to work together, any more than communists and fascists unite to take over the government today. Both might find humans - with their muddled priorities and complicated economy - better partners than another AI just as monomaniacal as them but oriented in a different direction.

Eliezer Yudkowsky worries that supercoherent superintelligences will have access to better decision theories than humans - mathematical theorems about cooperation which let them make and prove binding commitments with each other in the absence of explicit coordination. Not only would this prevent us from intercepting their coordination, but it would be such an advantage that humans (who can’t do this) would be locked out of possible alliances. I agree that if this were true it would be a very bad omen. But human geniuses don’t seem able to do this, so maybe we can re-use the Optimist’s Case above with decision theory as the world-killing technology.

Other people worry that, since training costs are so much higher than inference costs, by the time we can train a certain AI we can afford to run hundreds of millions of copies, all probably communicating with each other inhumanly quickly. This is starting to sound more concerning and harder to bargain with.

I’m optimistic because I think you get AIs that can do good alignment research before you get AIs that can do creepy acausal bargaining.

**3: How much harder is it to solve the alignment problem than to check someone else’s solution?** In some cases it’s much easier to check an answer than to invent it. It took Newton to invent calculus, but some high schoolers are able to use calculus, and anyone who uses calculus can confirm that it correctly solves calculus problems.

Suppose we ask an AI smarter than any human genius (who might or might not be a sleeper agent) to solve alignment for us. It thinks for a while, consults with other brilliant AIs, and then hands us a paper titled “The Solution To Alignment”, with an answer that no human would be able to come up with. Either the AI has solved alignment for us, or it’s a sleeper agent deliberately giving us compelling-but-wrong information. If alignment is like calculus, we can come to understand the solution ourselves, see whether it makes sense or not, double-check it for subtle errors, and then use it. If it seems more like “use this set of incomprehensible characters as a prompt for your next AI, it’ll totally work, trust me, bro”, then we’re relying on the AI not being a sleeper agent, and ought to be more pessimistic.

A pessimistic friend points out that, even though many people can use calculus to solve problems, far fewer people would be able to spot if it were the kind of thing that broke down in a certain edge case (speaking of things invented by Newton, many high school students can understand his brilliant and correct-seeming theory of gravity, but it took Einstein to notice that it was subtly flawed).

I’m optimistic because there could be many possible paths to alignment, including some where solutions are more checkable than others. For example, if we asked a sleeper agent AI to solve interpretability, we could try interpreting lots of different test AIs to see if it worked. Even if there are ways to defeat interpretability (eg encrypting your thoughts), it would be hard for the AI to feed us false information here.

**4: How easy are superweapons?** The usual postulated superweapon is nanotechnology: large-molecule-sized robots that can replicate themselves and perform tasks. Get enough of these, and they can quietly spread around the world, quietly infect humans, and kill them instantly once a controller sends the signal.

Other forms of superweapons (nukes, pandemics) won’t work as well - a world-killer can’t deploy them until it (or others AIs allied with it) can control the entire industrial base on their own. Otherwise, the humans die, the power plants stop working, and the world-killer gets shut off (and can’t make sugar crystals or whatever else it wants). So its easiest options are to either wait until basically all industrial production is hooked up to robot servitors that it can control via the Internet, or to invent nanotechnology, ie an industrial base in a can.

Nanomachines are definitely possible in some sense - biological enzymes and some microorganisms sort of count - but there’s a lot of debate over exactly what a manufactured nanomachine could vs. couldn’t do outside of the ecosystem of complex inter-reacting molecules that make up biological life. The most plausible proposals involve using living systems to create proteins that can (in a controlled environment) create preliminary nano-assembly machines, which can make more advanced nano-assembly machines, and so on, until they have machines capable of leaving the controlled environment (or creating other environments).

Some scientists think this is just actually impossible - God Himself could not do it - see[ eg the Drexler-Smalley debate](http://pubsapp.acs.org/cen/coverstory/8148/8148counterpoint.html?) for some thoughts along these lines.

Eliezer Yudkowsky takes the other end, saying that it might be possible for someone only a little smarter than the smartest human geniuses. He imagines, for example, a von Neumann level AI learning enough about nanotechnology to secrety train a nanobot-design AI. Such an AI might work very well -[ a chemical weapons designing AI](https://www.theverge.com/2022/3/17/22983197/ai-new-possible-chemical-weapons-generative-models-vx) was able to invent many existing chemical weapons - and some that might be worse - within a few hours.

If nanobots are easy, we would have a very short window between intermediate AIs capable of solving alignment, and world-killers. If nanobots are impossible, probably there would be no world-killer, and we would only have to worry about the scenarios more like slave revolts.

**5: Will takeoff be slow vs. fast?** So far we’ve had brisk but still gradual progress in AI; GPT-3 is better than GPT-2, and GPT-4 will probably be better still. Every few years we get a new model which is better than previous models by some predictable amount.

Some people (eg [Nate Soares](https://www.lesswrong.com/posts/GNhMPAWcfBCASy8e6/a-central-ai-alignment-problem-capabilities-generalization)) worry there’s a point where this changes. Maybe intelligence is some specific thing that an AI team could “discover” “how to” “actually” “get” (in the sense of the general intelligence which differentiates Man from the apes) and the AI transitions from a boring language model to a scary agent. Maybe a seemingly-normal training run stumbles across some key structure like this randomly. Maybe 999 of 1000 training runs in a certain paradigm produce a dumb bucket of heuristics, but one produces a mesa-optimizer.

Maybe some jump like this could take an AI from IQ 90 to IQ 1000 with no (or very short) period of IQ 200 in between (is this plausible? See AI Impacts’ [Discontinuous Progress In History](https://aiimpacts.org/discontinuous-progress-in-history-an-update/)). This kind of jump could happen in intelligence, coherence, or both at once. In this case, we would be very unprepared, and there would be no slightly-dumber-aligned-AIs to help us figure it out.

I’m optimistic because the past few years have provided some evidence for gradual progress, although not everyone is reassured:

[![Twitter avatar for @anthrupad](https://substackcdn.com/image/twitter_name/w_96/anthrupad.jpg)w̸͕͂͂a̷͔̗͐t̴̙͗e̵̬̔̕r̴̰̓̊m̵͙͖̓̽a̵̢̗̓͒r̸̲̽ķ̷͔́͝ @anthrupadwell that proves it then ![Image](https://substackcdn.com/image/fetch/w_600,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FFqmUHEuaQAA933v.png)](https://twitter.com/anthrupad/status/1633000439959687168)[7:03 AM ∙ Mar 7, 2023

* * *

697Likes58Retweets](https://twitter.com/anthrupad/status/1633000439959687168)

(this is a bigger deal than its relegation to Part 5 of a list of disagreements suggests, and some people think basically everything centers around this point. Probably it deserves a post of its own; for now, accept my apologies and [this link](https://astralcodexten.substack.com/p/yudkowsky-contra-christiano-on-ai))

**6: What happens if we catch a few sleeper agents?** Catching a few sleeper agents might be an opportunity to consider the possibility that _all_ our AIs are sleeper agents - or at least that we don’t know which ones aren’t, and we have to behave accordingly.

Or people could say “huh, this one cake-making robot went insane in this one weird situation, surely all the other cake-making robots that are currently doing great jobs are fine.”

Imagine one of those times a car is found to have some flaw, and the car company stonewalls and says there’s no problem and refuses to recall it. Except this time the cars themselves are cooperating in the deception, and promising that everything is fine, and making sure not to show the flaw when they think regulators might be watching.

I’m not _too_ optimistic about this. But I’ve gotten a little more so after seeing how freaked out people got over (comparatively mild) offenses by Bing. And because if we learned anything from the coronavirus, it’s that people will never react appropriately, but they _can_ switch from underreacting to overreacting very rapidly. Milton Friedman [said ](https://www.goodreads.com/quotes/110844-only-a-crisis---actual-or-perceived---produces-real)you change the world by having a plan and waiting for a crisis; if when the crisis happens, you’re the only guy with a plan, and everyone will do whatever you say. 

In the very unlikely event that everything happens exactly the way this post describes, consider asking people in the AI alignment community about all the plans they’ve been making!
