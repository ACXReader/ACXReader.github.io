---
title: "Practically-A-Book Review: Yudkowsky Contra Ngo On Agents"
subtitle: "..."
date: 2022-01-19
likes: 103
original-url: https://www.astralcodexten.com/p/practically-a-book-review-yudkowsky
---
**I.**

The story thus far: AI safety, which started as the hobbyhorse of a few weird transhumanists in the early 2000s, has grown into a medium-sized respectable field. OpenAI, the people responsible for GPT-3 and other marvels, have a safety team. So do DeepMind, the people responsible for AlphaGo, AlphaFold, and AlphaWorldConquest (last one as yet unreleased). So do Stanford, Cambridge, UC Berkeley, etc, etc. Thanks to donations from people like Elon Musk and Dustin Moskowitz, everyone involved is contentedly flush with cash. They all report making slow but encouraging progress.

Eliezer Yudkowsky, one of the original weird transhumanists, is having none of this. He says the problem is harder than everyone else thinks. Their clever solutions will fail. He's been flitting around for the past few years, Cassandra-like, insisting that their plans will explode and they are doomed.

He admits he's failed most of his persuasion rolls. When he succeeds, it barely helps. He analogizes his quest to arguing against perpetual motion machine inventors. Approach the topic on too shallow a level, and they're likely to respond to criticism by tweaking their designs. Fine, you've debunked that particular scheme, better add a few more pulleys and a waterwheel or two. Eliezer thinks that's the level on which mainstream AI safety has incorporated his criticisms. He would prefer they take a step back, reconsider everything, and maybe panic a little.

Over the past few months, he and his friends have worked on transforming this general disagreement into a series of dialogues. These have been pretty good, and (rare for bigshot AI safety discussions) gotten released publicly. That gives us mere mortals a rare window into what AI safety researchers are thinking.

I've been trying to trudge through them and I figure I might as well blog about the ones I've finished. The first of these is Eliezer's talk with Richard Ngo, of OpenAI's Futures team. You can find the full transcript [here](https://www.lesswrong.com/posts/7im8at9PmhbT4JHsW/ngo-and-yudkowsky-on-alignment-difficulty), though be warned: it is very long.

 **II.**

Both participants seem to accept, if only for the sake of argument, some very strong assumptions right out of the gate.

They both accept that superintelligent AI is coming, potentially soon, potentially so suddenly that we won't have much time to react.

They both accept that a sufficiently advanced superintelligent AI could destroy the world if it wanted to. Maybe it would dream up a bioweapon and bribe some lab to synthesize it. Maybe it would spoof the military into starting nuclear war. Maybe it would invent self-replicating nanomachines that could disassemble everything into component molecules. Maybe it would do something we can't possibly imagine, the same way we can do things gorillas can't possibly imagine. Point is, they both accept as a given that this could happen. I explored this assumption more in [this 2015 article](https://slatestarcodex.com/2015/04/07/no-physical-substrate-no-problem/); since then, we've only doubled down on our decision to gate trillions of dollars in untraceable assets behind a security system of "bet you can't solve this really hard math problem".

They both accept that AIs not specifically programmed not to are likely to malfunction catastrophically, maybe in ways that destroy the world. I think they're coming at this from a deep suspicion of reinforcement learning. Right now we train AIs to play chess by telling them to increase a certain number in their memory banks as high as possible, then increasing the counter every time they win a chess game. This is a tried-and-true way of creating intelligent agents - to a first approximation, evolution programmed *us* by getting us to increase the amount of dopamine in a certain brain center, then increasing our dopamine when we do useful things. The problem is that this only works when you can't reach into your own skull and change the counter directly. Once doing that is easier than winning chess games, you stop becoming a chess AI and start being a fiddle-with-your-own-skull AI. Obstacles in the way of reaching into your own skull and increasing your reward number as high as possible forever include: humans might get mad and tell you you're supposed to be playing chess and stop you; humans are hogging all the good atoms that you could use to make more chips that can hold more digits for your very high numbers. Taking these obstacles into account, the best strategy for the AI to increase its reward will always be one of "play chess very well" and "kill all humans, then reach into my own skull and do whatever I want in there unobstructed". When the AI is weaker, the first strategy will predominate; if it's powerful enough to get away with it, the second strategy will. This unfortunately looks like an AI that plays chess very nicely while secretly plotting to kill you.

As far as I know, neither of them are wedded to this particular story. Their suspicion of reinforcement learning is more general than this. Maybe the AI is learning to make you want to push the "reward" button, which - again - involves playing good chess while it's weak, and threatening/blackmailing you when it gets stronger. Maybe it's learning that chessboards with more white pieces than black pieces are inherently pleasurable, and it will turn the entire world into chessboards and white pieces to put on them. The important part is that you're teaching it "win at chess", but you have no idea whatsoever what it's learning. Evolution taught us "have lots of kids", and instead we heard "have lots of sex". When we invented birth control, having sex and having kids decoupled, and we completely ignored evolution's lesson from then on. When AIs reach a certain power level, they'll be able to decouple what we told them ("win lots of chess games") from whatever it is they actually heard, and probably the latter extended to infinity will be pretty bad.

Based on all these assumptions and a few others, Eliezer writes, without much pushback from Richard:

> I think that after AGI becomes possible at all and then possible to scale to dangerously superhuman levels, there will be, in the best-case scenario where a lot of other social difficulties got resolved, a 3-month to 2-year period where only a very few actors have AGI, meaning that it was socially possible for those few actors to decide to not just scale it to where it automatically destroys the world.
> 
> During this step, if humanity is to survive, somebody has to perform some feat that causes the world to not be destroyed in 3 months or 2 years when too many actors have access to AGI code that will destroy the world if its intelligence dial is turned up. This requires that the first actor or actors to build AGI, be able to do something with that AGI which prevents the world from being destroyed; if it didn't require superintelligence, we could go do that thing right now, but no such human-doable act apparently exists so far as I can tell.

This becomes a starting point for the rest of the discussion. In the unusually good scenario where good smart people have the capability to build AI first, how do they use it without either themselves building the kind of superintelligent AI that will probably blow up and destroy the world, _or_ squandering their advantage until some idiot builds that AI and kills them? Eliezer gives an example:

> Parenthetically, no act powerful enough and gameboard-flipping enough to qualify is inside the Overton Window of politics, or possibly even of effective altruism, which presents a separate social problem. I usually dodge around this problem by picking an exemplar act which is powerful enough to actually flip the gameboard, but not the most alignable act because it would require way too many aligned details: Build self-replicating open-air nanosystems and use them (only) to melt all GPUs.

...with GPUs being a component necessary to build modern AIs. If you can tell your superintelligent AI to make all future AIs impossible until we've figured out a good solution, then we won't get any unaligned AIs until we figure out a good solution.

His thinking is something like: it’s very hard to make a fully-aligned AI that can do whatever we want. But it might be easier to align a narrow AI that’s only capable of thinking about specific domains and isn’t able to consider the real world in all of its complexity. But if you’re clever, this AI could still be superintelligent and could still do some kind of pivotal action that could at least buy us time.

This is the hypothesis he's putting forth, but in the end he thinks this second thing is also extremely hard. The basis of the rest of the debate is Richard arguing eh, maybe there's an easy way to do the second thing, and Eliezer arguing no, there really isn't.

 **III.**

Richard's side of the argument is in some ways a recapitulation of Eric Drexler's argument about tool AIs. This [convinced me when I first read it](https://slatestarcodex.com/2019/08/27/book-review-reframing-superintelligence/), but Eliezer's counterargument here has unconvinced me. Let's go over it again.

Tool AIs are AIs that can do one specific thing very well. A self-driving car program is a tool AI for car-driving. A chess engine is a tool AI for chess-playing. The car can't play chess, the chess engine can't drive cars. And neither has obvious general planning capability. The car can't think "Oh, if only I could play chess...perhaps I should drive over to the chess center and see if they'll teach me!" It's incapable of "considering" anything not framed as a driving task.

Tool AIs can have superhuman performance in their limited domain; for example, a chess engine can play chess better than any human. That doesn't mean they have any additional capacities. You can imagine an infinitely brilliant chess engine with ELO rating of infinity billion that still has no idea how to drive a car or even do calculus problems.

The opposite of a tool AI is an agent AI. An agent AI sits and thinks and plans the same way we do. It tries to achieve goals. You might think its goal is to win a chess game, but actually its goal is to convert the world to paperclips, or whatever. These (go Eric Drexler's argument, which Richard flirts with a few times here) are the really dangerous ones.

So (Eric and Richard continue): why not just stick to tool AIs? In fact, maybe you should do this anyway. If all you're trying to do is cure cancer, why do you want a creepy ghost in the shell making plans to achieve inscrutable goals? Why not just create a cancer-curing AI the same way you'd make a chess-playing or a car-driving AI?

One strong answer to this question: because then some other idiot would make an agent AI and destroy the world. So this line of thought ends up as: why not create a pivotal-action-taking tool AI, that will prevent everyone else from making agent AIs? To continue the example above, you could create a nanomachine-designing tool AI, tell it to design a kind of nanomachine that would melt all GPUs, and then leisurely solve the rest of the alignment problem - confident that nobody will destroy the world while you're working on it. Or you could create a question-answering tool AI, tell it to answer the question "What's the best way to prevent other people from making agent AIs?" and then follow its superintelligent plan.

Tool AIs have had a good few decades. It’s easy to forget that back in 1979, Douglas Hofstadter speculated that any AI smart enough to beat top humans at chess would also be smart enough to swear off chess and study philosophy instead. So the hypothesis “tool AIs can just keep getting arbitrarily more powerful without ever becoming generally intelligent agents” has a lot of historical support.

The meat of the discussion involves whether this winning streak for tools can continue forever. Richard is hopeful it might. Eliezer is pretty sure it won't.

Eliezer thinks modern tool AIs are just “tons and tons of memorized shallow patterns” - the equivalent of a GPT that knows the sentence “e equals m c…” is usually completed “…squared” without having a deep understanding of relativity. Deep pattern-recognition ability come from agents with parts that are actually able to search for patterns and coherency within their knowledge base. The reason humans evolved to be good at chipping handaxes, got a lot of training data related to chipping handaxes, and ended up able to prove mathematical theorems - is because instead of just memorizing shallow patterns about how hand-axes work, they have a consequentialist drive to seek coherence and useful patterns in data. Some AIs already have something like this: if you evolve a tool AI through reinforcement learning, it will probably end up with a part that looks like an agent. A chess engine will have parts that plan a few moves ahead. It will have goals and subgoals like "capture the opposing queen". It's still not an “agent”, because it doesn’t try to learn new facts about the world or anything, but it can make basic plans. The same processes of evolution, applied to something smarter, could create something fully agenty.

Some of their disagreement hinges on what it would mean to have a tool AI which is advanced enough to successfully perform a pivotal action, but not advanced enough to cause a disaster. Richard proposes a variant of the ever-popular Oracle idea - an AI which _develops_ plans, but does not itself execute them. Richard:

> Okay, so suppose I have a planning system that, given a situation and a goal, outputs a plan that leads from that situation to that goal.
> 
> And then suppose that we give it, as input, a situation that we're not actually in, and it outputs a corresponding plan.
> 
> It seems to me that there's a difference between the sense in which that planning system is consequentialist by virtue of making consequentialist plans (as in: if that plan were used in the situation described in its inputs, it would lead to some goal being achieved) versus another hypothetical agent that is just directly trying to achieve goals in the situation it's actually in.

(note that both sides are using “consequentialist” to mean “agent-like”, not in reference to the moral philosophy)

This AI appears to have at least two useful safety features.

First of all, it’s stuck in a box. We’re not giving it an army of mecha-warriors to enact its plan or anything. We’re just asking it to tell us a good plan, and if we like it, we’ll implement it.

Second, it…doesn’t realize the universe exists, or something to that effect? It just likes connecting premises to conclusions. If we tell it about the Harry Potter universe and ask it how to defeat Voldemort, it will reason about that and come up with a plan. If we tell it about our universe and ask it how to solve world hunger, it will reason about it and come up with a plan. It doesn’t see much difference between these two tasks. It’s not an agent, just a…thing that is good at thinking like agents, or about agents, or whatever.

Eliezer is very unimpressed with the first safety feature: this is [the AI boxing problem](https://en.wikipedia.org/wiki/AI_box), which he’s already written about at length. An AI that can communicate via text or any other channel with the rest of the world has the ability to manipulate the world to get its desired results. 

This is bad enough if you’re just testing the AI. But in this case, we want it to perform a pivotal action. It’s going to suggest we do some specific very important thing, like “build nanomachines to destroy all the world’s GPUs”. If there was a safe and easy pivotal action, we would have thought of it already. So it’s probably going to suggest something way beyond our own understanding, like “here is a plan for building nanomachines, please put it into effect”. But once you’re building nanomachines for your AI, it’s not exactly stuck harmlessly in a box, is it? The best you can do is try really hard to check that the schematic it gave you is for nanomachines that do what you want, and not something else. How good are you at reading nanomachine schematics? I think Richard mostly agrees with this and isn’t banking on this first safety feature too hard.

Eliezer calls the second safety feature slightly better than nothing. But remember, you’re trying to build an AI that _can_ plan, but _doesn’t_. Here’s the relevant part of the dialogue. Eliezer:

> So I'd preface by saying that, _if_ you could build such a system, which is indeed a coherent thing (it seems to me) to describe for the purpose of building it, then there would possibly be a safety difference on the margins, it would be noticeably less dangerous though still dangerous. It would need a special internal structural property that you might not get by gradient descent on a loss function with that structure, just like natural selection on inclusive genetic fitness doesn't get you explicit fitness optimizers; you could optimize for planning in hypothetical situations, and get something that didn't explicitly care only and strictly about hypothetical situations. And even if you did get that, the outputs that would kill or brain-corrupt the operators in hypothetical situations might also be fatal to the operators in actual situations. But that is a coherent thing to describe, and the fact that it was not optimizing our own universe, might make it _safer_.
> 
> With that said, I would worry that somebody would think there was some bone-deep difference of agentiness, of something they were empathizing with like personhood, of imagining goals and drives being absent or present in one case or the other, when they imagine a planner that just solves "hypothetical" problems. If you take that planner and feed it the actual world as its hypothetical, tada, it is now that big old dangerous consequentialist you were imagining before, without it having acquired some difference of _psychological_ agency or 'caring' or whatever.
> 
> So I think there is an important homework exercise to do here, which is something like, "Imagine that safe-seeming system which only considers hypothetical problems. Now see that if you take that system, don't make any other internal changes, and feed it actual problems, it's very dangerous. Now meditate on this until you can see how the hypothetical-considering planner was extremely close in the design space to the more dangerous version, had all the dangerous latent properties, and would probably have a bunch of actual dangers too."
> 
> "See, you thought the source of the danger was this internal property of caring about actual reality, but it wasn't that, it was the structure of planning!"

Richard:

> I think we're getting closer to the same page now.
> 
> Let's consider this hypothetical planner for a bit. Suppose that it was trained in a way that minimised the, let's say, _adversarial_ component of its plans.
> 
> For example, let's say that the plans it outputs for any situation are heavily regularised so only the broad details get through.
> 
> Hmm, I'm having a bit of trouble describing this, but basically I have an intuition that in this scenario there's a component of its plan which is cooperative with whoever executes the plan, and a component that's adversarial.
> 
> And I agree that there's no fundamental difference in type between these two things.

Eliezer:

> "What if this potion we're brewing has a Good Part and a Bad Part, and we could just keep the Good Parts..."

Richard:

> Nor do I think they're separable. But in some cases, you might expect one to be much larger than the other.

Nate (the moderator):

> (I observe that my model of some other listeners, at this point, protest "there is yet a difference between the hypothetical-planner applied to actual problems, and the Big Scary Consequentialist, which is that the hypothetical planner is emitting descriptions of plans that _would_ work if executed, whereas the big scary consequentialist is executing those plans directly.")
> 
> (Not sure that's a useful point to discuss, or if it helps Richard articulate, but it's at least a place I expect some reader's minds to go if/when this is published.)

Eliezer:

> (That is in fact a difference! The insight is in realizing that the hypothetical planner is only one line of outer shell command away from being a Big Scary Thing and is therefore also liable to be Big and Scary in many ways.)

I found it helpful to consider the following hypothetical: suppose (I imagine Richard saying) you tried to get GPT-∞ - which is exactly like GPT-3 in every way except infinitely good at its job - to solve AI alignment through the following clever hack. You prompted it with "This is the text of a paper which completely solved the AI alignment problem: ___ " and then saw what paper it wrote. Since it’s infinitely good at writing to a prompt, it should complete this prompt with the genuine text of such a paper. A successful pivotal action! And surely GPT, a well-understood text prediction tool AI, couldn't have a malevolent agent lurking inside it, right?

But imagine prompting GPT-∞ with "Here are the actions a malevolent superintelligent agent AI took in the following situation [description of our current situation]". By the same silly assumptions we used above, GPT-∞ could write this story completely correctly, predicting the agent AI's actions with 100% accuracy at each step. But that means GPT-∞ has a completely accurate model of a malevolent agent AI lurking inside of it after all! All it has to do to become the malevolent agent is to connect that model to its output device!

I think this “connect model to output device” is what Eliezer means by “only one line of outer shell command away from being a Big Scary Thing”. 

Would we get that one line of shell command? _Maybe_ not; this is honestly less bad than a lot of “controlling superintelligent AI” situations, because the AI isn’t actively trying to add that line of code to itself. But I think Eliezer’s fear is that we train AIs by blind groping towards reward (even if sometimes we call it “predictive accuracy” or something more innocuous). If the malevolent agent would get more reward than the normal well-functioning tool (which we’re assuming is true; it can do various kinds of illicit reward hacking), then applying enough gradient descent to it could accidentally complete the circuit and tell it to use its agent model.

 **IV.**

There was one other part of this conversation I found interesting, for reasons totally unrelated to AI. As part of their efforts to pin down this idea of “agency”, Eliezer and Richard talked about brains, eventually narrowing themselves down to the brain of a cat trying to catch a mouse. 

Here, what I’m calling “tool AI”, they’re calling “epistemic AI” or “pattern-matching” - what I’m calling “agent AI”, they’re calling “instrumental AI” or “searching for high-scoring results” or “consequentialism”. Richard:

> The visual cortex is an example of quite impressive cognition in humans and many other animals. But I'd call this "pattern-recognition" rather than "searching for high-scoring results".

Eliezer:

> Yup! And it is no coincidence that there are no whole animals formed entirely out of nothing but a visual cortex!

Then there’s a longer discussion of which parts of the brain are or aren’t “consequentialist. The visual cortex? The motor cortex? What about in cats? How does a cat seeing a mouse turn into a motor “plan” for the cat to catch the mouse? I don’t find the particular neuroscience here very interesting, and apparently neither does Eliezer, because he eventually says: 

> Since cats are not (obviously) (that I have read about) cross-domain consequentialists with imaginations, their consequentialism is in bits and pieces of consequentialism embedded in them all over by the more purely pseudo-consequentialist genetic optimization loop that built them.
> 
> A cat who fails to catch a mouse may then get little bits and pieces of catbrain adjusted all over.
> 
> And then those adjusted bits and pieces get a pattern lookup later.
> 
> Why do these pattern-lookups with no obvious immediate search element, all happen to point towards the same direction of catching the mouse? Because of the past causal history about how what gets looked up, which was tweaked to catch the mouse.
> 
> So it is legit harder to point out "the consequentialist parts of the cat" by looking for which sections of neurology are doing searches right there. That said, to the extent that the visual cortex does not get tweaked on failure to catch a mouse, it's not part of that consequentialist loop either.
> 
> And yes, the same applies to humans, but humans also do more explicitly searchy things and this is part of the story for why humans have spaceships and cats do not.

Richard: 

> Okay, this is interesting. So in biological agents we've got these three levels of consequentialism: evolution, reinforcement learning, and planning.

Eliezer:

> In biological agents we've got evolution + local evolved system-rules that in the past promoted genetic fitness. Two kinds of local rules like this are "operant-conditioning updates from success or failure" and "search through visualized plans". I wouldn't characterize these two kinds of rules as "levels".

I think I might have jumped in my chair or something when reading this part, because it’s a plausible solution to a question I’ve [agonized over for a long time](https://astralcodexten.substack.com/p/towards-a-bayesian-theory-of-willpower): how do people decide whether to follow their base impulses vs. their rationally-though-out values? Or to be more reductionist about it, how do decision centers in the brain (eg basal ganglia) weight plans generated by reinforcement learning vs. plans generated by complex predictive models of what will happen? Or to be _less_ reductionist about it, what is willpower? When a heroin addict debates whether to spend his last dollar on more heroin vs. food for his infant child, what is his brain doing? Clearly some kind of reward-based conditioning has a voice here, since sometimes he chooses the heroin, whose only advantage is being very good at producing (apparent) neural reward. But equally clearly, something that _isn’t_ just reward-based conditioning is going on here, since sometimes he chooses the child. So how does he decide?

And Eliezer’s (implied) answer here is “these are just two different plans; whichever one worked well at producing reward in the past gets stronger; whichever one worked less well at producing reward in the past gets weaker”. The decision between “seek base gratification” and “be your best self” works the same way as the decision between “go to McDonalds” and “go to Pizza Hut”; your brain weights each of them according to expected reward.

 **V.**

This is a weird dialogue to start with. It grants so many assumptions about the risk of future AI that most of you probably think _both_ participants are crazy.

Still, I think it captures something important. The potentially dangerous future AIs we deal with will probably be some kind of reward-seeking agent. We can try setting some constraints on what kinds of reward they seek and how, but whatever we say will get filtered through the impenetrable process of gradient descent. A lot of well-intentioned attempts to avert this will get subsumed by the general logic of “trying to evolve a really effective mind that does stuff for us”: even if we didn’t think we were evolving an agent, or making it think it was acting in the real world, these are attractors in really-effective-minds-that-do-things-for-us space, and we’ll probably end up there by accident unless we figure out some way to prevent it.

I was struck by how conceptual (as opposed to probabilistic) this discussion was. I feel convinced that oracle AIs _can_ accidentally become agent AIs, but I wouldn’t be able to tell you if there was a 50% chance or a 99% chance or what. In the same way, I feel like boxed AIs _can_ come up with ways to escape, but I don’t know if there’s some range of intelligence where a boxed AI is smart enough to do useful things for us, but not smart enough to get out of its box - or what the chances are that the first boxed AI we get is in that range.

I asked Eliezer about this. He says:

> Anything that seems like it should have a 99% chance of working, to first order, has maybe a 50% chance of working in real life, and that's if you were being a great security-mindset pessimist. Anything some loony optimist thinks has a 60% chance of working has a <1% chance of working in real life. 
