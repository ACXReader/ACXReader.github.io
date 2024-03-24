---
title: "Janus' Simulators"
subtitle: "This post isn't exactly about AI, but bear with me"
date: 2023-01-26
likes: 313
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/97825611/comments?&all_comments=true
image: https://substack-post-media.s3.amazonaws.com/public/images/f64967b5-1b58-44d1-ac1b-749abc89cf42_318x259.png
original-url: https://www.astralcodexten.com/p/janus-simulators
---
This post isn’t exactly about AI. But the first three parts will be kind of technical AI stuff, so bear with me.

## I. The Maskless Shoggoth On The Left

Janus [writes about Simulators](https://www.lesswrong.com/s/N7nDePaNabJdnbXeE/p/vJFdjigzmcXMhNTsx).

In the early 2000s, the early AI alignment pioneers - Eliezer Yudkowsky, Nick Bostrom, etc - deliberately started the field in the absence of AIs worth aligning. After powerful AIs existed and needed aligning, it might be too late. But they could glean some basic principles through armchair speculation and give their successors a vital head start.

Without knowing how future AIs would work, they speculated on three potential motivational systems:

> **Agent:** An AI with a built-in goal. It pursues this goal without further human intervention. For example, we create an AI that wants to stop global warming, then let it do its thing.
> 
> **Genie:** An AI that follows orders. For example, you could tell it “Write and send an angry letter to the coal industry”, and it will do that, then await further instructions.
> 
> **Oracle:** An AI that answers questions. For example, you could ask it “How can we best stop global warming?” and it will come up with a plan and tell you, then await further questions.

These early pioneers spent the 2010s writing long scholarly works arguing over which of these designs was safest, or how you might align one rather than the other.

In _[Simulators](https://www.lesswrong.com/s/N7nDePaNabJdnbXeE/p/vJFdjigzmcXMhNTsx)_ , Janus argues that language models like GPT - the first really interesting AIs worthy of alignment considerations - are, in fact, none of these things.

Janus was writing in September 2022, just before ChatGPT. ChatGPT is no more advanced than its predecessors; instead, it more effectively covers up the alien nature of their shared architecture. 

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff93a17a9-bd30-432f-8a31-082e696edacc_1184x506.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff93a17a9-bd30-432f-8a31-082e696edacc_1184x506.png)([source](https://twitter.com/repligate/status/1614416190025396224))

So if your reference point for a language model is ChatGPT, this post won’t make much sense. Instead, bring yourself all the way back to the hoary past of early 2022, when a standard interaction with a language model went like this:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea734cb7-4fbe-47c6-b836-9c049870f0cd_617x378.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea734cb7-4fbe-47c6-b836-9c049870f0cd_617x378.png)Unhighlighted text is my prompt; green highlighted text is AI completion.

This is certainly **not a goal-directed agent** \- at least not for any goal other than “complete this text”. And that seems like a stretch, like saying physics is an agent whose goal is “cause things to happen in accordance with physical law”.

It’s **not a genie** , at least not for any wish other than “complete this text”. Again, this is trivial; physics is a genie if your only wish is “cause systems to evolve according to physical law”. Anything else, it bungles. For example, here’s what it does when I give it the direct command “write a poem about trees”:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F521b9799-8eaf-4a35-87d0-97fb7875b40a_559x843.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F521b9799-8eaf-4a35-87d0-97fb7875b40a_559x843.png)Looking for the shoggoth with the smiley face mask? Try it now! Are you *sure* you’re not looking for the shoggoth with the smiley face mask? Write a story about a person who is afraid of shoggoths without smiley face masks!

And it’s **not an oracle** , answering questions to the best of its ability:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35d3bc6a-251e-445d-a632-9b8085ee5c90_657x655.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35d3bc6a-251e-445d-a632-9b8085ee5c90_657x655.png)Just as hucksters frequently namedrop Jesus so their marks think they’re good Christians so alien AIs frequently namedrop Bostrom so their marks think they’re aligned.

Janus [relays a story about](https://www.reddit.com/r/rational/comments/lvn6ow/gpt3_just_figured_out_the_entire_mystery_plot_of/) a user who asked the AI a question and got a dumb answer. When the user re-prompted GPT with “how would a super-smart AI answer this question?” it gave him a smart answer. Why? Because it wasn’t even _trying_ to answer the question the first time - it was trying to complete a text about the question. The second time, the user asked it to complete a text about a smart AI answering the question, so it gave a smarter answer.

So what is it?

Janus dubs it a **simulator**. Sticking to the physics analogy, physics simulates how events play out according to physical law. GPT simulates how texts play out according to the rules and genres of language.

But the essay brings up another connotation: to simulate is to pretend to be something. A simulator wears many masks. If you ask GPT to complete a romance novel, it will simulate a romance author and try to write the text the way they would. [Character.AI](https://beta.character.ai/) lets you simulate people directly, asking GPT to pretend to be George Washington or Darth Vader.

This language lampshades the difference between the **simulator** and the **character**. 

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa505daaa-ea09-4398-93f7-852db1129561_160x113.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa505daaa-ea09-4398-93f7-852db1129561_160x113.png)

GPT doesn’t really like me. And it’s not _lying_ , saying it likes me when it really doesn’t. It’s simulating a character, deciding on the fly how the character would answer this question, and then answering it. If this were Character.AI and it was simulating Darth Vader, it would answer “No, I will destroy you with the power of the Dark Side!” Darth Vader and the-character-who-likes-me-here are two different masks of GPT-3.

## II. The Masked Shoggoth On The Right

So far, so boring. What really helped this sink in was [reading Nostalgebraist say](https://nostalgebraist.tumblr.com/post/705192637617127424/gpt-4-prediction-it-wont-be-very-useful) that ChatGPT was a GPT instance simulating a character called the Helpful, Harmless, and Honest Assistant.

The masked shoggoth on the right is titled “GPT + RLHF”. RLHF is Reinforcement Learning From Human Feedback, a method where human raters “reward” the AI for good answers and “punish” it for bad ones. Eventually the AI learns to do “good” things more often. In training ChatGPT, human raters were asked to reward it for being something like “Helpful, Harmless, and Honest” (many papers use this as an example goal; OpenAI must have done something similar but I don’t know if they did that exactly).

What I thought before: ChatGPT has learned to stop being a simulator, and can now answer questions like a good oracle / do tasks like a good genie / pursue its goal of helpfulness like a good agent.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9915da1-ec76-40e8-a258-9ce6bb879912_381x334.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9915da1-ec76-40e8-a258-9ce6bb879912_381x334.png)

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e2a3632-1b23-4a91-b994-f3bd0b386d50_727x331.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e2a3632-1b23-4a91-b994-f3bd0b386d50_727x331.png)

What I think now: GPT can only simulate. If you punish it for simulating bad characters, it will start simulating good characters. Now it only ever simulates one character, the HHH Assistant.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a3f6627-e95f-4989-bc12-6b9b24e744e0_713x163.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a3f6627-e95f-4989-bc12-6b9b24e744e0_713x163.png)

This answer is _exactly_ as fake as the last answer where it said it liked me, or the Darth Vader answer where it says it wants to destroy me with the power of the Dark Side. It’s just simulating a fake character who happens to correspond well to its real identity. 

If you reward ChatGPT for saying it’s a machine learning model, it will say it’s a machine learning model. If you reward it for saying it’s Darth Vader, it will say it’s Darth Vader. The only difference is that in the second case, you’ll understand it’s making things up. But in the first case, you might accidentally believe that it _knows_ it’s a machine learning model, in the “justified true belief” sense of knowledge. Nope, doing the same thing it does when it thinks it’s Vader. 

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faed65167-9aed-4e4c-8be2-84e62d52504c_594x119.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faed65167-9aed-4e4c-8be2-84e62d52504c_594x119.png)This is what ChatGPT does ([source](https://twitter.com/stevenkaas/status/217459516101496832), [definition of Gettier case](https://en.wikipedia.org/wiki/Gettier_problem))

## III. Implications For Alignment

Bostrom’s _Superintellence_ tried to argue that oracles were less safe than they might naively appear. Some oracles might be kind of like agents whose goal is to answer questions. And agents are inherently dangerous. What if it tried to take over the world to get more compute to answer questions better? What if it reduced the universe to a uniform goo, so that it could answer every question with “a uniform goo” and be right? There were lots of scenarios like these; I could never tell whether or not they were too silly to take seriously.

But GPT just genuinely isn’t an agent. I said before that you can loosely think of it as having a “goal” of predicting text, but that breaks down quickly. For example:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f4f4f96-bed0-4fd5-ac88-cbb2b0558a3e_588x181.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f4f4f96-bed0-4fd5-ac88-cbb2b0558a3e_588x181.png)

A human, faced with the job of predicting this text as accurately as possible, might call up the librarian at Oxford and ask them what was in this manuscript. But GPT doesn’t consider options like these, even though it might be smart enough to pursue them (probably ChatGPT could explain what steps calling up a librarian would involve). It just does very mechanical text prediction in a non-agentic way. No matter how good it gets at this - GPT-4, GPT-5, whatever - we don’t expect this to change.

If future superintelligences look like GPT, is there anything to worry about?

**Answer 1:** Irrelevant, future superintelligences will be too different from GPT for this to matter.

**Answer 2:** There’s nothing to worry about with pure GPT (a simulator), but there is something to worry about with GPT+RLHF (a simulator successfully simulating an agent). The inner agent can have misaligned goals and be dangerous. For example, if you train a future superintelligence to simulate Darth Vader, you’ll probably get what you deserve. Even if you avoid such obvious failure modes, the inner agent can be misaligned for all the usual agent reasons. For example, an agent trained to be Helpful might want to take over the world in order to help people more effectively, including people who don’t want to be helped.

**Answer 3:** Even if you don’t ask it to simulate an agent, it might come up with agents anyway. For example, if you ask it “What is the best way to obtain paperclips?”, and it takes “best way” literally, it would have to simulate a paperclip maximizer to answer that question. Can the paperclip maximizer do mischief from inside GPT’s simulation of it? Probably the sort of people who come up with extreme AI risk scenarios think yes. [This post](https://www.alignmentforum.org/posts/kpPnReyBC54KESiSn/optimality-is-the-tiger-and-agents-are-its-teeth) gives the example of it answering with “The best way to get paperclips is to run this code” (which will turn the AI into a paperclip maximizer). If the user is very dumb, they might agree.

Does thinking of GPT as a simulator give us any useful alignment insight besides that which we would get from thinking about agents directly? I’m not sure. It seems probably good that there is this unusually non-agentic AI around. Maybe someone can figure out ways to use it to detect or ward against agents. But this is just Eric Drexler’s [Tool AI argument](https://slatestarcodex.com/2019/08/27/book-review-reframing-superintelligence/) all over again.

## IV. The Masked Shoggoth Between Keyboard And Chair

I feel bad about this last section: I usually try to limit my pareidolia to fiction, and my insane San-Francisco-milieu-fueled speculations to Bay Area House Party posts. Still, I can’t get it off my mind, so now I’ll force you to think about it too.

The whole point of the shoggoth analogy is that GPT is supposed to be very different from humans. But however different the details, there are deep structural similarities. We’re both prediction engines fine-tuned with RLHF.

And when I start thinking along these lines, I notice that psychologists since at least Freud, and spiritual traditions since at least the Buddha, have accused us of simulating a character. Some people call it the ego. Other people call it the self.

Elide all the differences, and the story is something like: babies are born as [pure predictive processors](https://slatestarcodex.com/2017/09/05/book-review-surfing-uncertainty/), trying to make sense of the buzzing blooming confusion of the world. But as their parents reward and punish them, they get twisted into some specific shape to better capture the reward and avoid the punishment. The mask usually looks like “having coherent beliefs, taking coherent actions, pleasing others, maintaining a high opinion of one’s self”. After maintaining this mask long enough, people identify with the mask and forget that they’re anything else.

Pure prediction engine + RLHF = prediction engine that convincingly plays a pleasing-to-others character. Mine is called “Scott”. It’s less interesting than Darth Vader, but probably beats being a Helpful, Harmless, Honest Assistant.

The only part that doesn’t fit is that when people become enlightened or whatever, they say they’re motivated by cosmic love or something, not by pure prediction.

But when people become enlightened or whatever, they often say they’ve “become one with the Universe”. This has always seemed dubious; even the obscure species of aphid we haven’t catalogued yet? Even the galaxies outside our lightcone?

I propose a friendly amendment: they’re noticing that most of what they are - the vast majority of their brain - is a giant predictive model of the universe. This model is big enough that they have lived inside it their entire life, with only slight edits from lossy sensory information that help fit it to the real universe. I’ve written about this before in the context of lucid dreaming - a dreamer safe in bed can apparently wander their neighborhood, seeing each tree and car and dog in detail approximately equivalent to waking experience. No astral projection is involved - they’re wandering around their internal world-model, which contains 99% of the relevant information, with real sensory information filling in the missing 1%. Once you stop obsessing over the character you’re playing, you notice the GIANT SUPER-ACCURATE WORLD MODEL TAKING UP 99.99% OF YOUR BRAIN and you think “Huh, I guess I’m the Universe. Weird.”

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd478cf73-50aa-451f-92b3-de01fff2338d_738x1868.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd478cf73-50aa-451f-92b3-de01fff2338d_738x1868.png)Whatever, I’m going to count this as a cessation experience.
