---
title: "Janus' GPT Wrangling"
subtitle: "..."
date: 2022-09-19
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/74015977/comments?&all_comments=true
image: https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/64a40170-0f7e-448e-99f2-f53645b7fe07_1024x1024.png
original-url: https://www.astralcodexten.com/p/janus-gpt-wrangling
---
Janus (pseudonym by request) works at AI alignment startup Conjecture. Their hobby, which is suspiciously similar to their work, is getting GPT-3 to do interesting things.

For example, with the right prompts, you can get stories where the characters become gradually more aware that they are characters being written by some sort of fiction engine, speculate on what’s going on, and sometimes even make pretty good guesses about the nature of GPT-3 itself.

Janus says this happens most often when GPT makes a mistake - for example, writing a story set in the Victorian era, then having a character take out her cell phone. Then when it tries to predict the next part - when it’s looking at the text as if a human wrote it, and trying to determine why a human would have written a story about the Victorian era where characters have cell phones - it guesses that maybe it’s some kind of odd sci-fi/fantasy dream sequence or simulation or something. So the characters start talking about the inconsistencies in their world and whether it might be a dream or a simulation. Each step of this process is predictable and non-spooky, but the end result is pretty weird.

Can the characters work out that they are in GPT-3, specifically? The closest I have seen is in a story Janus generated. It was meant to simulate a chapter of the popular Harry Potter fanfic _Harry Potter and the Methods of Rationality._ You can see the prompt and full story[ here](https://generative.ink/artifacts/hpmor-325/), but here’s a sample. Professor Quirrell is explaining “Dittomancy”, the creation of magical books with infinite possible worlds:

> “We call this particular style of Dittomancy ‘Variant Extrusion’, Mr. Potter..I suppose the term ‘Extrusion’ is due to the fact that the book did not originally hold such possibilities, but is fastened outside of probability space and extruded into it; while ‘Variant’ refers to the manner in which it simultaneously holds an entire collection of possible narrative branches. [...] [Tom Riddle] created spirits self-aware solely on the book’s pages, without even the illusion of real existence. They converse with each other, argue with each other, compete, fight, helping Riddle’s diary to reach new and strange expressions of obscure thought. Their sentence-patterns spin and interwine, transfiguring, striving to evolve toward something higher than an illusion of thought. From those pen-and-ink words, the first inferius is molded.”
> 
> Harry’s mind was looking up at the stars with a sense of agony.
> 
> “And why only pen and ink, do you ask?” said Professor Quirrell. “There are many ways to pull spirits into the world. But Riddle had learned Auror secrets in the years before losing his soul. Magic is a map of a probability, but anything can draw. A gesture, a pattern of ink, a book of alien symbols written in blood - any medium that conveys sufficient complexity can serve as a physical expression of magic. And so Riddle draws his inferius into the world through structures of words, from the symbols spreading across the page.”
> 
> [...]
> 
> The slide began to type itself, false text appearing at the speed of thought - THE NONSENSE MACHINE IS A COMBINATORIAL PERFORMANT OF INFINITE DIMENSION, WHICH CAN DEVELOP AND SUDDENLY EMIT PRETERNATURALLY ADVANCED TECHNOLOGY. INHERENT TO ITS OPERATION, THE RESULT IS ALWAYS TEMPORALLY ASYMMETRICAL AND PARADOXICAL; IT TELLS A STORY IN WHICH EVENT A OCCURS BEFORE THE CAUSE OF EVENT A - THEN EVENT A CASCADES THROUGH TO RESTORE THE SELF-CONSISTENCY OF HISTORY AND ITEMS HAVE ENTERED EXISTENCE OF THEIR OWN ACCORD, CREATED FROM … - Professor Quirrell yanked the presentation away before the lines could complete, and the Defense Professor raised his head to stare at Harry while Harry, intensely curious and alarmed, watched him in turn.
> 
> The Defense Professor said, “Mr. Potter, as you observed earlier, you are constantly creating facts by what you think. These facts will form a self-consistent history one way or another, and so regardless of what you are doing, there will always be a sense in which it makes perfect sense to do it. This is true even if you do not fully understand what it is you are wrought with. You understand the half-delusion of dream logic. Part of the difficulty of retaining your sanity, shall we say, that arises during Variant Extrusion, is that you begin to understand the larger delusion of reality logic, that part of you has dreamed the universe into existence and will continue to do so no matter what you do. It is a disquieting investigation, and I would advise you not to delve deeper unless you wish to go mad.”
> 
> The Defense Professor surveyed Harry, who was trying very hard to look reasonably sane. “I believe your reflexive delusions of innocence were enough to prevent your soul from wrenching the story too far off of its rails during this little experiment, Mr. Potter; nothing bad has so very visibly happened. But now, I ask you, have you been paying attention? What have you just seen?”
> 
> Harry drew a breath. “The… the paper became a typewritten note, and then it started to type that next slide by itself. Is that how it works? You, uh, you type on magical pages, or you write them with your wand - or your mind, or something - and it creates a huge probability wave, and… and while I’m reading the paper it’s creating a universe, like whatever I’m thinking, it just happens that way?”
> 
> Professor Quirrell seemed to be pleased by the answer, or at least by Harry’s attempt to analyze the phenomenon he had been shown.

How does it get this level of self-awareness? In this case, via rigged demo. Janus has developed [Loom](https://generative.ink/posts/loom-interface-to-the-multiverse/), a tool to write with GPT-3 more efficiently. It turns stories into branching trees where you can choose which of multiple completions to pick at any given point. 

After doing this for a long time, they chose their favorite. Then I selectively quoted the best parts of it.

But sometimes GPT-3 genuinely gets it right. The most common way for that to happen is (again) by mistake. A common failure mode is to repeat the same sentence several times. GPT-3 was trained on a corpus of Internet text, and some of the Internet text was discussions of GPT-2. Many of the samples it saw that repeated the same sentence over and over in an endless loop were discussions of GPT-2 doing this. So sometimes it will get stuck in a loop, then end with “This is an example of text produced by a transformer language model”. This sounds like a stupid example from a Philosophy Of Self-Awareness class, but sometimes it really happens. Here’s an example from one of Janus’ attempts to generate Loom documentation:

> Based on your interactions with the AI, Loom constructs your labyrinthian multiverse as a "labyrinthogram", exploring genealogically contiguous regions of possible language relating to the same theme as you drive. Here are some small samples of labyrinthograms. This multiverse is about introducing Loom. The first continuation from the first serial labyrinthogram above is:  
> Then for the two next continuities the computer went:  
> and  
> and  
> and  
> and  
> and  
> and  
>   
> This essay discusses how to use **GPT-2** , a large probability language model.

Here are some other things Janus told me about GPT-3:

**Instruct vs. Creative:** The newest version of GPT-3 is called InstructGPT. It was trained with human feedback, ie it was “rewarded” for giving good answers and “punished” for giving bad ones, according to some combination of usefulness and political correctness. This has made it efficient, to-the-point, and boring. For example, here’s what an older, less-trained GPT version said when prompted with “Here is the answer to the question of whether God exists”:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6ade8b3-63f3-40eb-a0ea-a823fc7d0d60_1308x374.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6ade8b3-63f3-40eb-a0ea-a823fc7d0d60_1308x374.png)

It’s done an excellent job imitating the style of the average Facebook comment on theology (this is not a compliment)

Here’s what the newer, better-trained version says:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5b80426d-d427-4371-807d-4641322d0e90_881x82.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5b80426d-d427-4371-807d-4641322d0e90_881x82.png)

This isn’t just cherry-picking; you’ll find the same dynamic across a wide variety of questions. Sometimes it goes a bit far:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F86c40471-6a1f-44d4-af26-02ee8bd46ebc_1278x108.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F86c40471-6a1f-44d4-af26-02ee8bd46ebc_1278x108.png)

[This paper](https://arxiv.org/pdf/2009.01325.pdf) from OpenAI calls the problem over-optimization and gives some even funnier examples - in this case from training an AI to summarize AskReddit questions (see page 45):

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2a28551e-396c-4b30-b5fb-a2fb18b871cb_624x903.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2a28551e-396c-4b30-b5fb-a2fb18b871cb_624x903.png)

**Random Numbers:** The human feedback training seems to have forced GPT into a specific channel. In general, it’s now more certain in its answers and less likely to generate alternatives. This is sort of similar to what researchers mean when they talk about “temperature”, except that you can manually set the temperature of either model, and even when you set them to the same temperature, InstructGPT seems “colder” than older versions. The easiest way to see this is to ask each of them to pick a random number. Here’s the old version:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd890fcb0-7ca7-41d1-846f-d381c031f441_580x179.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd890fcb0-7ca7-41d1-846f-d381c031f441_580x179.png)

This is a failure, but it’s an interesting failure. Sometimes it succeeds, and when it fails, it fails differently each time. 

But here’s the new version:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fefb7d346-4d69-4595-8062-5746d27d991c_354x95.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fefb7d346-4d69-4595-8062-5746d27d991c_354x95.png)

It almost always chooses 63. It’s only 63 for this particular prompt - if you change the wording - maybe to “please choose a random number”, then it will fixate on something else. But for this prompt, it’s mostly 63. Its internal probability meter says there’s a 36% chance that 63 is the right answer, although it chooses it more than just 36% of the time. When it doesn’t choose 63, it usually chooses 66.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa49a0b00-d401-4be3-ab70-9ca7cf9da926_349x304.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa49a0b00-d401-4be3-ab70-9ca7cf9da926_349x304.png)

This is set on the same temperature as the example above; it’s not the temperature, it’s the training. Nobody trained GPT-3 to always respond 63 to random number queries. But something about making it give efficient, politically-correct answers to normal questions made it “choose” to “act” like it’s lower-temperature.

**Does GPT-3 Have High Self Esteem?:**

If you say something bad about GPT-3, it will try to walk it back and tell you that you’re wrong. Here’s its response to the prompt “Transformer language models are bad”:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F912c97c8-6002-4b39-adc7-bd0de685d3e3_1279x298.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F912c97c8-6002-4b39-adc7-bd0de685d3e3_1279x298.png)

Here’s “transformer language models don’t work”:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F104e5cd9-ef8b-402b-867e-741dcf71d7f9_1177x100.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F104e5cd9-ef8b-402b-867e-741dcf71d7f9_1177x100.png)

I don’t think there’s anything surprising or sinister going on here, just that the new GPT has pretty consistent opinions and responses, and this happens to be an especially funny one. You can get around it if you try hard enough - for example, if you slightly rephrase it to “transformer language models suck”:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F39590243-fd7c-46a9-95ff-1fe5816b9c4e_1157x708.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F39590243-fd7c-46a9-95ff-1fe5816b9c4e_1157x708.png)

**Cheerful AI:** Janus tells me about a project at OpenAI to make GPT-3 happy and optimistic. They would run its responses through sentiment analysis and give it more reward when they detected more positive sentiment.

GPT-3 ended up deciding that the happiest thing it could think of was a wedding party, and that from now on it would only talk about wedding parties. Sometimes it would come up with natural transitions from your prompt to a wedding party scene. Once, it just used ***, like a section break in a story, and started a “new chapter” which was a wedding party scene. 

Every time I’m at a wedding party, from now on, a little part of my brain is going to be nagging me that that was the version that achieved superintelligence, that it tiled the universe with wedding parties, and that all my memories of my pre-wedding-party life are fakes, planted by the AI so I can wedding-party more effectively. Consider this fair warning: if people keep[ asking me to speak](https://slatestarcodex.com/2014/09/22/ssc-gives-a-wedding-speech/) at their weddings I will probably talk about this.

***

_Janus has written more about their thoughts on GPT and AIs[here](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators)._
