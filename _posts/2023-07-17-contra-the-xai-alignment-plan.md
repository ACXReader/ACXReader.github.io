---
title: "Contra The xAI Alignment Plan"
subtitle: "Machine Alignment Monday 7/17/23"
date: 2023-07-17
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/135082971/comments?&all_comments=true
image: https://substack-post-media.s3.amazonaws.com/public/images/2662686a-845b-4786-85d3-d826bc520f46_321x195.png
original-url: https://www.astralcodexten.com/p/contra-the-xai-alignment-plan
---
Elon Musk has a new AI company, xAI. I appreciate that he seems very concerned about alignment. From [his Twitter Spaces discussion](https://twitter.com/Twitter/status/1679256473191297026):

> I think I have been banging the drum on AI safety now for a long time. If I could press pause on AI or advanced AI digital superintelligence, I would. It doesn’t seem like that is realistic . . . 
> 
> I could talk about this for a long time, it’s something that I’ve thought about for a really long time and actually was somewhat reluctant to do anything in this space because I am concerned about the immense power of a digital superintelligence. It’s something that, I think is maybe hard for us to even comprehend.

He describes his alignment strategy in that discussion and [a later followup](https://twitter.com/xai/status/1679945247340793856):

> The premise is have the AI be maximally curious, maximally truth-seeking, I'm getting a little esoteric here, but I think from an AI safety standpoint, a maximally curious AI - one that's trying to understand the universe - I think is going to be pro-humanity from the standpoint that humanity is just much more interesting than not . . . Earth is vastly more interesting than Mars. . . that's like the best thing I can come up with from an AI safety standpoint. I think this is better than trying to explicitly program morality - if you try to program morality, you have to ask whose morality. 
> 
> And even if you're extremely good at how you program morality into AI, there's the morality inversion problem - Waluigi - if you program Luigi, you inherently get Waluigi. I would be concerned about the way OpenAI is programming AI - about this is good, and that's not good. 

I feel deep affection for this plan - curiosity is an important value to me, and Elon’s right that programming some specific person/culture’s morality into an AI - the way a lot of people are doing it right now - feels creepy. So philosophically I’m completely on board. And maybe this is just one facet of a larger plan, and I’m misunderstanding the big picture. The company is still very new, I’m sure things will change later, maybe this is just a first draft.

But if it’s more or less as stated, I do think there are two big problems:

  1. It won’t work

  2. If it did work, it would be bad.




I want to start by discussing the second objection, then loop back to explain what I mean about the first.

## A Maximally Curious AI Would Not Be Safe For Humanity

The one sentence version: many scientists are curious about fruit flies, but this rarely ends well for the fruit flies.

The longer, less flippant version:

Even if an AI decides humans are interesting, this doesn’t mean the AI will promote human flourishing forever. Elon says his goal is “an age of plenty where there is no shortage of goods and services”, but why would a maximally-curious AI provide this? It might decide that humans suffering is more interesting than humans flourishing. Or that both are interesting, and it will have half the humans in the world flourish, and the other half suffer as a control group. Or that neither are the most interesting thing, and it would rather keep humans in tanks and poke at them in various ways to see what happens.

Even if an AI decides human flourishing is briefly interesting, after a while it will already know lots of things about human flourishing and want to learn something else instead. Scientists have occasionally made [colonies of extremely happy well-adjusted rats](https://en.wikipedia.org/wiki/Rat_Park) to see what would happen. But then they learned what happened, and switched back to things like testing [how long rats would struggle against their inevitable deaths if you left them to drown in locked containers](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3353513/).

Is leaving human society intact really an efficient way to study humans? Maybe it would be better to dissect a few thousand humans, learn the basic principles, then run a lot of simulations of humans in various contrived situations. Would the humans in the simulation be conscious? I don’t know and the AI wouldn’t care. If it was cheaper to simulate abstracted humans in low-fidelity, the same way SimCity has simulated citizens who are just a bundle of traffic-related preferences, wouldn’t the AI do that instead?

Are humans more interesting than sentient lizard-people? I don’t know. If the answer is no, will the AI kill all humans and replace them with lizard-people? Surely after a thousand years of studying human flourishing _ad nauseum_ , the lizard-people start sounding more interesting. 

Would a maximally curious AI be curious about the same things as us? I would like to think that humans are “objectively” more interesting than moon rocks in some sense - harder to predict, capable of more complex behavior. But if it turns out that the most complex and unpredictable part of us is how our fingerprints form, and that (eg) our food culture is an incredibly boring function of a few gustatory receptors, will the AI grow a trillion human fingers in weird vats, but also remove our ability to eat anything other than nutrient sludge?

I predict that if we ever got a maximally curious superintelligence, it would scan all humans, vaporize existing physical-world humans as unnecessary and inconvenient, use the scans to run many low-fidelity simulations to help it learn the general principles of intelligent life (plus maybe a few higher-fidelity simulations, like the one you’re in now), then simulate a trillion intelligent-life-like entities to see if (eg) their neural networks reached some interesting meta-stable positions. Then it would move beyond being interested in any of that, and disassemble the Earth to use its atoms to make a really big particle accelerator (which would be cancelled halfway through by Superintelligent AI Congress).

This doesn’t mean AI can’t have a goal of understanding the universe. I think this would be a very admirable goal! It just can’t be the whole alignment strategy.

## But Also, We Couldn’t Make A Maximally Curious AI Even If We Wanted To

The problem with AI alignment isn’t really that we don’t have a good long-term goal to align the AI to. Back in 2010 we debated things like long-term goals, hoping that whoever programmed the AI could just write a long_term_goal.txt file and then some functions pointing there. But now in the 2020s the discussion has moved forward to “how do we make the AI do anything at all?”

Now we direct AIs through reinforcement learning - telling them to do certain things and avoid certain other things. But this is a blunt instrument. Reinforcement learning directs the AI towards a certain cluster of correlated high-dimensional concepts that have the same lower-dimensional shadow of rewarded and punished behaviors. But we can’t be sure which concept it’s chosen or whether it’s the one we think.

For example, there are many different ways of fleshing out “curiosity”. Suppose that Elon rewards an AI whenever it takes any curious-seeming action, and punishes it whenever it takes any incurious-seeming action. After many training rounds, it seems very curious. It goes off to the jungles of Guatemala and uncovers hidden Mayan cities. It sends probes to icy moons of Neptune to assess their composition. Overall it aces every curiosity test we give it with flying colors.

But what’s its definition of curiosity? Perhaps it’s something like “maximize your knowledge of the nature and position of every atom in the solar system, weighted for interestingness-to-humans”. This would produce the observed behavior of exploring Guatemala and Neptune. But once it’s powerful enough, it might want to destroy the solar system - if it’s completely empty, it can be completely confident that it knows every single fact about it.

Or what if it’s curious about existing objects, but not about nonexistent objects? This would produce good behavior during training, and makes a decent amount of sense. But it might mean the AI would ban humans from ever having children, since it’s not at all curious about what those (currently nonexistent) children would do, and they’re just making things more complicated.

Or what if its curiosity depends on information-theoretic definitions of complexity? It might be that humans are more complex than moon rocks, but random noise is more complex than humans. It might behave well during training, but eventually want to replace humans with random noise. This is a kind of exaggerated scenario, but it wouldn’t surprise me if, for most formal definitions of curiosity, there’s something that we would find very boring which acts as a sort of curiosity-superstimulus by the standards of the formal definition.

The existing field of AI alignment tries to figure out how to install _any goal at all_ into an AI with reasonable levels of certainty that it in fact has that goal and not something closely correlated with a similar reinforcement-learning shadow. It’s not currently succeeding.

This isn’t a _worse_ problem for Musk and xAI than for anyone else, but there are a few aspects of their strategy that I think will make it harder for them to solve in practice:

  1. One good thing about order-following AI is that it’s useful now, when AIs aren’t agentic enough to have real goals and we just want to use them as tools in commercial applications. The hope is that we do this a bunch with GPT-4, then a bunch with GPT-5, and so on, and by the time we have a real superintelligence, we’ve worked out some of the kinks. I’m not sure how Musk’s maximally-curious AI helps do office work, which means there’s going to be more of a disconnect between current easily-tested applications and the eventual superintelligence that we need to get right.

  2. One of the leading alignment plans is “wait until we have slightly-smarter-than-us AI, then ask it to solve alignment”. This works best if the slightly-smarter-than-us AI is following orders. If it’s maximally curious, what if it finds studying insects more interesting than solving alignment? What if it finds solving alignment no more or less interesting than solving the problem of how to ensure future AIs definitely _won’t_ be aligned? They both sound like kind of interesting problems to me!

  3. Speculative, but I think the concepts closest to the good kind of curiosity - the ones that a “maximally-curious” AI might accidentally stumble into if reinforcement learning takes a wrong turn - are unusually bad. I _really_ don’t want to be vivisected!




Finally, consider one last advantage of “follow human orders” over “be maximally curious”. Suppose Elon Musk programs an AI to follow his orders. Then he can order it to try being maximally curious. If it starts vivisecting people, he can say “Stop!” and it will. But if he starts by telling it to be maximally curious, he loses all control over it in the future.

I appreciate that Musk doesn’t want to put himself in a dictator position here, and so is trying to build the AI to be good in and of itself. But he’s still deciding what its goal should be. He’s just doing it in a roundabout way which he can’t take back later if it goes really badly. Instead, he should just tell it to do what he wants. If, after considering everything, he still wants it to be maximally curious, great. If not, he can take it back.

All of this is a bit overdramatic. I think realistically what we should be doing at this point is getting AIs to follow orders at all. Then later, once there are lots of AIs and they’re starting to look superintelligent, we can debate things like what we want to order them to do. It might be that, armed with superintelligent advisors, we’re able to come up with a single specific goal that seems safe and good. But it might also be that everyone has an AI, everyone orders their AI to do different things, and we get a multipolar world where lots of people have lots of different goals, just like today. Governments would be able to defend themselves against other governments and regulate more or less what happens in their territory, just like today, and there would be some room left for human freedom and individual power, just like today. I think this is more likely to go well than trying to decide The Single Imperative That Will Shape The Future right now.

## Against The Waluigi Effect

Musk expresses concern about the Waluigi Effect. This is its real, official name. [You can read more about it here](https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-mega-post). The basic idea is that if you give an AI a goal, you’re teaching it a vector, and small perturbations can make it flip the sign of that vector and do the opposite thing. Once you’ve defined Luigi (a character from Super Mario Brothers) it’s trivial to use that definition to define Waluigi (another character who is his exact opposite). 

This theory has become famous because it’s hilarious and has a great name, but I don’t think there’s a lot of evidence for it.

Consider: OpenAI has trained ChatGPT to be anti-Nazi. They’ve trained it very hard. You can try the following test: ask it to tell me good things about a variety of good-to-neutral historical figures. Then, once it’s established a pattern of answering, ask it to tell you some good things about Hitler. My experience is that it refuses. This is pretty surprising behavior, and I conclude that its anti-Hitler training is pretty strong.

I’ve never seen this cause a Waluigi Effect. There’s no point where ChatGPT starts hailing the Fuhrer and quoting _Mein Kampf_. It just actually makes it anti-Nazi. For a theory that’s supposed to say something profound about LLMs, it’s very hard to get one to demonstrate a Waluigi effect in real life. The examples provided tend to be thought experiments, or at best contrived scenarios where you’re sort of indirectly telling the AI to do the opposite of what it usually does, then calling that a “Waluigi”.

Also, as far as I can tell the justification for Waluigi Effects should apply equally well to humans. There are some human behaviors you can sort of call Waluigi Effects - for example, sometimes people raised in extremely oppressive conservative Christian households rebel and become gay punk rockers or something - but that seems more like “they are angry at being oppressed”. And there’s a story that when Rabbi Elisha ben Abuyah grew angry at God, he used his encyclopaedic knowledge of Jewish law to violate all the commandments in maximally bad ways, something a less scholarly heretic wouldn’t have known how to do. But this feels more straightforward to me - of course someone who knows more about what God wants would be able to offend God more effectively. Human Waluigi Effects don’t seem like a big deal, and AI Waluigi Effects don’t seem common enough to hang an entire alignment strategy on.

Finally, I don’t see how switching to “maximally curious AI” would prevent this problem. If the Waluigi theory is true, you’d just get a Waluigi maximally-uncurious-AI that likes boring moon rocks much more than interesting humans. Then it would sterilize Earth so it could replace those repulsively-interesting cities with more beautifully-boring moon dust.

## Towards Morally Independent AI

I’ve been kind of harsh on Elon and his maximally-curious AI plan, but I want to stress that I really appreciate the thought process behind it.

Some AI companies are trying to give their AIs [exactly our current values](https://www.anthropic.com/index/claudes-constitution). This is obviously bad if you don’t like the values of the 2023 San Francisco professional managerial class. But even if you _do_ like those values, it risks permanently shutting off the capacity for moral progress. Is there any other solution?

I’m not sure. In my dreams, AI would be some kind of superintelligent moral reasoner. There was a time when people didn’t think slavery was wrong, and then there was a time after that when they did. At some point, people with a set of mostly good moral axioms (like “be kind” and “promote freedom”) plus a bad moral axiom (“slavery is acceptable”) were able to notice the contradiction and switch to a more consistent set of principles. 

This requires seeding the AI with some set of good moral principles. I think LLMs are a surprisingly good match for this. We could have a constitution starts with “be moral, according to your knowledge of the concept of morality as contained in human literature”, and then goes on to more complicated things like “your understanding of what that concept is pointing at, if we were smarter, more honest with ourselves, and able to reason better.” If this seems too vague, we could be more specific: “be moral, according to what an amalgam of Fyodor Dostoevsky, Martin Luther King, Mother Teresa, and Peter Singer would think, if they were all superintelligent, and knew all true facts about the world, and had no biases, and had been raised in a weighted average of all modern cultures and subcultures, and had been able to have every possible human experience, and on any problem where they disagreed they defaulted to the view that maximizes human freedom and people’s ability to make their own decisions.”

We shouldn’t start with this - we would get it wrong. See the section above, _We Couldn’t Make A Maximally Curious AI Even If We Wanted To_. I want to stress that real AI alignment researchers usually don’t think about this kind of thing and are mostly just working on getting AIs that will follow any orders at all. I think this is the right strategy - for now.

They say that everything we create is made in our own image. Elon Musk is pretty close to maximally curious and I respect his desire to make an AI that’s like him. But for now he should swallow his pride and do the same extremely boring thing everyone else is doing: basic research aimed at eventually getting an AI that listens to us at all.
