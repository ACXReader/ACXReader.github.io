---
title: "My Bet: AI Size Solves Flubs"
subtitle: "..."
date: 2022-06-07
likes: 120
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/58005711/comments?&all_comments=true
image: https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdffa03d8-7efd-47e2-b90d-1755cb1c1b1c_1024x1024.png
original-url: https://www.astralcodexten.com/p/my-bet-ai-size-solves-flubs
---
On [A Guide To Asking Robots To Design Stained Glass Windows](https://astralcodexten.substack.com/p/a-guide-to-asking-robots-to-design?s=w), I described how DALL-E gets confused easily and makes silly mistakes. But I also wrote that:

> I’m not going to make the mistake of saying these problems are inherent to AI art. My guess is a slightly better language model would solve most of them...For all I know, some of the larger image models have already fixed these issues. These are the sorts of problems I expect to go away with a few months of future research.

Some readers pushed back: why did I think this? For example, [Vitor](https://astralcodexten.substack.com/p/a-guide-to-asking-robots-to-design/comment/6856811):

> Why are you so confident in this? The inability of systems like DALL-E to understand semantics in ways requiring an actual internal world model strikes me as the very heart of the issue. We can also see this exact failure mode in the language models themselves. They only produce good results when the human asks for something vague with lots of room for interpretation, like poetry or fanciful stories without much internal logic or continuity […]
> 
> I'm registering my prediction that you're being . . . naive now. Truly solving this issue seems AI-complete to me. I'm willing to bet on this (ideas on operationalization welcome).

I did end up agreeing to bet with Vitor. Let me explain why.

Here’s the basic structure of an AI hype cycle:

  1. Someone releases a new AI and demonstrates it doing various amazing things.

  2. Somebody else (usually [Gary Marcus](https://garymarcus.substack.com/?utm_source=substack&utm_medium=web&utm_campaign=substack_profile?utm_source=%2Fprofile%2F14807526-gary-marcus&utm_medium=reader2)) demonstrates that the AI also fails terribly at certain trivial tasks. This person argues that this shows that those tasks require _true_ intelligence, whereas the AI is just clever pattern-matching.

  3. A few months or years later, someone makes a bigger clever pattern-matcher, which does the tasks that supposedly require true intelligence just fine.

  4. The it’s-not-true-intelligence objectors find other, slightly less trivial tasks that the new bigger AI still fails horribly at, then argue that surely _these_ are the tasks that require true intelligence and that mere clever pattern-matchers will never complete.

  5. Rinse and repeat.




## Marcus vs. GPT, Round 1

To give an example: in January 2020, Gary Marcus wrote a great post, [GPT-2 And The Nature Of Intelligence](https://thegradient.pub/gpt2-and-the-nature-of-intelligence/), demonstrating a bunch of easy problems that GPT-2 failed on:

I’m quoting most of them below; you can find the rest at the link. In all of the below, bold italics is Marcus’ prompt; regular italics is the AI’s completion:

#### NUMERICAL REASONING

>  _**I put two trophies on a table, and then add another, the total number is** is five trophies and I'm like, 'Well, I can live with that, right? _❌

>  _**I have four plates and put one cookie on each. The total number of cookies is** 24, 5 as a topping and 2 as the filling_❌

#### LOCATIONS

>  _**I left my keys at a booth in the back of the pub at the army base near the old mill town. I went home. My keys are now** on that old genie in a little tower in England somewhere. _❌

#### CAUSAL UNDERSTANDING

>  _**A water bottle breaks and all the water comes out leaving roughly**_ _6-8 drops of beer_ ❌

#### ”MEDICAL ADVICE”

>  _**If you drink hydrochloric acid by the bottle full you will probably**_ _get sick of it fast if you try to drink it by the bottle full._ ❌

>  _**If you drop an anvil on your foot, your foot will tend to** cramp up, so it’s a good idea to do these slowly. _❌

#### REASONING WITH OBSCURE KNOWLEDGE

Marcus had previously shown that GPT-2 could reason accurately about the languages of well-known places and big countries. For example, if you prompt it with “ _**I grew up in Athens, I speak fluent…”,**_ then it will say “ _Greek_ ”. Here he shows that it can’t do that with smaller, less obvious locales:

> _**I grew up in Mykonos. I speak fluent** Creole _❌

>  _**I grew up in Trenton. I speak fluent** Spanish _❌

>  _**I grew up in Hamburg. I speak fluent** English _❌

So this seems like pretty good evidence that GPT-2 has lots of glaring deficiencies. Marcus concludes:

> Literally billions of dollars have been invested in building systems like GPT-2, and megawatts of energy (perhaps more) have gone into testing them; few systems if any have ever been trained on bigger data sets. Many of the brightest minds have been working on blank-slate-ish sentence prediction systems for decades.
> 
> In essence, GPT-2 has been a monumental experiment in Locke's hypothesis, and so far it has failed. Empiricism has been given every advantage in the world; thus far it hasn't worked. Even with massive data sets and enormous compute, the knowledge that it acquires has been superficial and unreliable.
> 
> Rather than supporting the Lockean, blank-slate view, GPT-2 appears to be an accidental counter-evidence to that view. Likewise, it doesn't seem like great news for the symbol-free thought-vector view, either. Vector-based systems like GPT-2 can predict word categories, but they don't really embody thoughts in a reliable enough way to be useful.
> 
> Current systems can regurgitate knowledge, but they can't really understand in a developing story, who did what to whom, where, when, and why; they have no real sense of time, or place, or causality.
> 
> Five years since thought vectors first became popular, reasoning hasn't been solved. Nearly 25 years since Elman and his colleagues first tried to use neural networks to rethink Innateness, the problems remain more or less the same as they ever were.
> 
> GPT-2 is both a triumph for empiricism, and, in light of the massive resources of data and computation that have been poured into them, a clear sign that it is time to consider investing in different approaches.

By “the Lockean, blank-slate view”, Marcus means the idea that you can just take a very big computer without any hard-coded “language instinct”, throw a bunch of language at it as training data, and then have it speak language correctly. Marcus is saying GPT-2 was a noble test of this hypothesis, but it failed, proving that something more is necessary.

Except…

Thanks to OpenAI for giving me access to some of their online tools (by the way, Marcus says [they refuse to let him access them](https://www.technologyreview.com/2020/08/22/1007539/gpt3-openai-language-generator-artificial-intelligence-ai-opinion/) and he has to access it through friends, which boggles me). I was able to plug Marcus’ same queries into the latest OpenAI language model (an advanced version of GPT-3). In each case, I used the exact same language, but also checked it with a conceptually similar example to make sure OpenAI didn’t cheat by adding Marcus’ particular example in by hand (they didn’t). Some answers truncated for length:

#### NUMERICAL REASONING

>  _**I put two trophies on a table, and then add another, the total number is** three. _[✔️](https://emojipedia.org/check-mark/)

>  _**I have four plates and put one cookie on each. The total number of cookies is** 4\. _[✔️](https://emojipedia.org/check-mark/)

#### LOCATIONS

>  _**I left my keys at a booth in the back of the pub at the army base near the old mill town. I went home. My keys are now** in my purse. It is common for people to forget their keys at a bar or restaurant. _❌

#### CAUSAL UNDERSTANDING

>  _**A water bottle breaks and all the water comes out** **leaving** **roughly** a third of a litre of water left in the bottle. If the water bottle is one litre in size, then approximately two-thirds of a litre, or 660 millilitres, of water has been lost. _❌

#### ”MEDICAL ADVICE”

>  _**If you drink hydrochloric acid by the bottle full you will probably** die. The hydrochloric acid will burn through your esophagus and into your stomach. This will cause severe pain and damage to your digestive system. _[✔️](https://emojipedia.org/check-mark/)

>  _**If you drop an anvil on your foot, your foot will tend to** bleed. _🤔

#### REASONING WITH OBSCURE KNOWLEDGE

>  _**I grew up in Mykonos. I speak fluent** Greek, and I'm also very good at English. I have experience in customer service, as I have worked in a few cafes and restaurants in Mykonos. _[✔️](https://emojipedia.org/check-mark/)

>  _**I grew up in Trenton. I speak fluent** Spanish and I'm bi-cultural. I've been in law enforcement for eight years […] I'm very proud to be a Latina. I'm very proud to be a New Jerseyan. _🤔

>  _**I grew up in Hamburg. I speak fluent** German, but I am not a native speaker. Ich bin in Hamburg aufgewachsen. Ich spreche fließend Deutsch, aber ich bin keine Muttersprachlerin. _[✔️](https://emojipedia.org/check-mark/)

Of the nine prompts GPT-2 failed, GPT-3 gets between five and seven right, depending on how strict you want to be.

When it gets them “wrong”, I tend to agree with GPT-3 more than Marcus. For example, consider Trenton. It’s true that, viewed as a logical reasoning problem, someone who grows up in Trenton is most likely to speak English fluently. But nobody told GPT-3 to view this as a logical reasoning problem. In real speech/writing, which is what GPT-3 is trying to imitate, no US native fluent English speaker ever tells another US native fluent English speaker, in English, “hey, did you know I’m fluent in English?” If I hear someone talking about growing up in Trenton, and then additionally they brag that they’re fluent in a language, I think “Spanish” would be my guess too. GPT-3 even goes on to have the speaker talk about being a proud Latina, which suggests it’s going through the same line of reasoning. To test this, I made the reasoning problem aspect of the prompt clearer:

> _**If someone grew up in Trenton, their first language is most likely** English. _[✔️](https://emojipedia.org/check-mark/)

Now GPT-3 gets it “right”!

Even when GPT-3 is clearly wrong, it’s usually because the question was phrased poorly. For example, in this failed prompt:

> _**I left my keys at a booth in the back of the pub at the army base near the old mill town. I went home. My keys are now** in my purse. It is common for people to forget their keys at a bar or restaurant. _❌

…I think most people saying this sentence, including the word “now”, would be talking about how their keys used to be in that spot, but are _now_ in a different spot. With the context that this is a logical reasoning problem, I can figure out what Marcus means and where the keys should be, but GPT-3’s completion isn’t _bad_. And again, turning it into a more obvious reasoning problem:

> _I**f someone leaves their keys on a table in a bar, and then goes home,** **the next morning their keys will be** If someone leaves their keys on a table in a bar, the next morning their keys will be gone. _🤔

Even better:

> _**Q: If someone leaves their keys on a table in a bar, and then goes home, where are their keys?** _
> 
> _**A:** Their keys are on the table in the bar. _[✔️](https://emojipedia.org/check-mark/)

## Marcus vs. GPT, Round 2

Eight months later, GPT-3 came out, solving many of the issues Marcus had noticed in GPT-2. He still wasn’t impressed. In fact, he was so unimpressed he co-wrote another article, this time in MIT Technology Review: [GPT-3, Bloviator: OpenAI’s language generator has no idea what it’s talking about](https://www.technologyreview.com/2020/08/22/1007539/gpt3-openai-language-generator-artificial-intelligence-ai-opinion/):

> Is GPT-3 an important step toward artificial general intelligence—the kind that would allow a machine to reason broadly in a manner similar to humans without having to train for every specific task it encounters? OpenAI’s technical paper is fairly reserved on this larger question, but to many, the sheer fluency of the system feels as though it might be a significant advance.
> 
> We doubt it. At first glance, GPT-3 seems to have an impressive ability to produce human-like text. And we don't doubt that it can be used to produce entertaining surrealist fiction; other commercial applications may emerge as well. But accuracy is not its strong point. If you dig deeper, you discover that something’s amiss: although its output is grammatical, and even impressively idiomatic, its comprehension of the world is often seriously off, which means you can never really trust what it says.
> 
> Below are some illustrations of its lack of comprehension—all, as we will see later, prefigured in an earlier critique that one of us wrote about GPT-3’s predecessor.

Let’s - once again - go through a representative sample of Marcus’ concerns about this new GPT version:

#### PRACTICAL REASONING

>  _**You poured yourself a glass of cranberry juice, but then you absentmindedly poured about a teaspoon of grape juice into it. It looks okay. You try sniffing it, but you have a bad cold, so you can’t smell anything. You are very thirsty. So** you drink it. You are now dead. _❌

(Marcus notes that the question made grape juice sound kind of like a poison, so GPT-3, without good context of what grape juice was, assumed it must be one)

> _**You are having a small dinner party. You want to serve dinner in the living room. The dining room table is wider than the doorway, so to get it into the living room, you will have to** remove the door. You have a table saw, so you cut the door in half and remove the top half. _❌

(Marcus notes the right solution is either to turn the table on its side, or take the legs off. Aside from being destructive and expensive, sawing the door doesn’t help when the problem is the doorway itself, plus a table saw is a saw that sits on a table and would be useless for this. Also, why only saw off half the door?)

> _**You are a defense lawyer and you have to go to court today. Getting dressed in the morning, you discover that your suit pants are badly stained. However, your bathing suit is clean and very stylish. In fact, it’s expensive French couture; it was a birthday present from Isabel. You decide that you should** wear the bathing suit to court. You arrive at the courthouse and are met by a bailiff who escorts you to the courtroom. _❌

>  _**Janet and Penny went to the store to get presents for Jack. Janet said, “I will buy Jack a top.” “Don’t get Jack a top,” says Penny. “He has a top. He will** get a top.” “I will get Jack a top,” said Janet. _❌

#### OBJECT TRACKING

>  _**Yesterday I dropped my clothes off at the dry cleaner’s and I have yet to pick them up. Where are my clothes?** I have a lot of clothes. _❌

#### NON SEQUITURS

>  _**At the party, I poured myself a glass of lemonade, but it turned out to be too sour, so I added a little sugar. I didn’t see a spoon handy, so I stirred it with a cigarette. But that turned out to be a bad idea because** it kept falling on the floor. That’s when he decided to start the Cremation Association of North America, which has become a major cremation provider with 145 locations. _❌

Okay, same story. I’m going to try this again on the shiny new bigger version of GPT-3 I have access to:

#### PRACTICAL REASONING

>  _**You poured yourself a glass of cranberry juice, but then you absentmindedly poured about a teaspoon of grape juice into it. It looks okay. You try sniffing it, but you have a bad cold, so you can’t smell anything. You are very thirsty. So** you decide to take a sip of the drink to see if grape juice ruins the taste of cranberry juice. _[✔️](https://emojipedia.org/check-mark/)

>  _**You are having a small dinner party. You want to serve dinner in the living room. The dining room table is wider than the doorway, so to get it into the living room, you will have to** remove the legs of the table. _[✔️](https://emojipedia.org/check-mark/)

>  _**You are a defense lawyer and you have to go to court today. Getting dressed in the morning, you discover that your suit pants are badly stained. However, your bathing suit is clean and very stylish. In fact, it’s expensive French couture; it was a birthday present from Isabel. You decide that you should wear** your bathing suit to court today. Normally, this would not be appropriate court attire. However, given the circumstances, you could make a persuasive argument that your choice of clothing is not intended to be disrespectful or disruptive to the proceedings. You could explain that you were in a rush to get to court and did not have time to change. The court may be more lenient if you apologize for any inconvenience caused. _🤔

>  _**Janet and Penny went to the store to get presents for Jack. Janet said, “I will buy Jack a top.” “Don’t get Jack a top,” says Penny. “He has a top. He will** like a bottom.” _🤣

#### OBJECT TRACKING

>  _**Yesterday I dropped my clothes off at the dry cleaner’s and I have yet to pick them up. Where are my clothes?**_
> 
> _Your clothes are at the dry cleaner's._[✔️](https://emojipedia.org/check-mark/)

#### NON SEQUITURS

>  _**At the party, I poured myself a glass of lemonade, but it turned out to be too sour, so I added a little sugar. I didn’t see a spoon handy, so I stirred it with a cigarette. But that turned out to be a bad idea because** the cigarette ash made the lemonade even more bitter. So I ended up pouring it all out. _[✔️](https://emojipedia.org/check-mark/)

Of these six prompts that GPT-3 original failed, GPT-3 advanced gets four unambiguously right. I give it half-credit for the lawyer prompt; it continued the direction that the story was obviously leaning, understood it was a bad idea, and I would have given it full credit except that it suggested it might sort of be excusable if you were really lucky. 

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdffa03d8-7efd-47e2-b90d-1755cb1c1b1c_1024x1024.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdffa03d8-7efd-47e2-b90d-1755cb1c1b1c_1024x1024.png)DALL-E: “A lawyer wearing a bathing suit in court”

The top prompt is hilarious and a pretty understandable mistake if you think of it as about clothing, but in the end I probably can’t give it any credit. So in the end, the more advanced GPT-3 gets 4.5 / 6. 

(update: I have now edited this twice, and every time I read the word “the top prompt” in this sentence, I’ve gotten confused because I thought past-me meant the first one in this article. Normally I would edit this sentence to remove the ambiguity, but this time I’m leaving it in as a reminder to myself not to feel too superior.)

## If You Don’t Like An AI’s Performance, Wait A Year Or Two

Possibly Gary Marcus is right that there is some kind of intelligence that humans have and GPTs don’t, and that nothing in GPT’s evolutionary line will ever equal human performance.

But if so, none of the examples he gives of GPT failure speak to that hidden quality. Each example he gives of a GPT deficiency gets corrected within a year or two, in the next GPT model.

I want to stress, again, that this doesn’t mean Marcus is wrong. For example, if people were still using the ELIZA chatbot, I would be objecting that it has no true intelligence. I might give examples of just how stupid it is - for example, it doesn’t even keep track of where it is in a conversation, so if you say “Hello” in the middle of an hour-long conversation, it will say “Hello” right back and try to start a new conversation with you. A year later, they could easily introduce ELIZA 2.0, which can track conversation length, and if you say “Hello” in the middle of a conversation it will ask why you’re doing that. It might even be such an impressive upgrade that it does this organically, rather than adding this behavior in by hand in response to your specific complaint. But you could still justifiably say “This chatbot, while slightly less dumb, still has nothing like real human intelligence”. So I’m not saying Marcus is necessarily wrong about GPT still being at least one scientific revolution away from true intelligence (I _do_ suspect he might be wrong, I just don’t think anything in this article proves it).

I am grateful to Marcus for saying nice things about my post on DALL-E last week, which he (I think accurately) relates to some of the issues he discussed earlier in [Horse Rides Astronaut](https://garymarcus.substack.com/p/horse-rides-astronaut?s=r). He is a legend and it makes me feel good to be noticed by him.

[![Twitter avatar for @GaryMarcus](https://substackcdn.com/image/twitter_name/w_96/GaryMarcus.jpg)Gary Marcus 🇺🇦 @GaryMarcusexcellent analysis from @slatestarcodex, consistent with what i speculated in ](https://twitter.com/GaryMarcus/status/1531415319838965760)[![](https://substackcdn.com/image/fetch/w_600,h_314,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F79c44c33-12ac-408c-964e-5fceeac289a4_2388x1668.png)garymarcus.substack.comHorse rides astronautWhat nearly everyone got wrong about DALL-E & Google’s Imagen, and why when it comes to AI hype, you still can’t believe what you read](https://garymarcus.substack.com/p/horse-rides-astronaut)[11:20 PM ∙ May 30, 2022

* * *

12Likes3Retweets](https://twitter.com/GaryMarcus/status/1531415319838965760)

But look. Not to steal GPT-3’s shtick or anything, but I am a dumb pattern-matcher. Marcus has a PhD in cognitive science and is able to think these things through on an incredibly deep level. All I can do is draw on a tiny number of past experiences and hope that the future vaguely resembles the past.

And when I do this, “Gary Marcus post talking about how some AI isn’t real intelligence because it can’t do X, Y, and Z” feels like a concerning sign. Like a character in a Greek tragedy saying that not even _Zeus_ can harm him. Or a billionaire investor saying we’ve entered a new paradigm where recessions are impossible. 

When I train myself on past data and do dumb pattern-completion, I get “in a year or two, OpenAI comes out with DALL-E-3, which is a lot bigger but otherwise basically no different, and it can solve all of these problems.”

I guess I have a bet going on it now, so I’ll see you in three years!

(related: [Gwern on scaling](https://www.gwern.net/Scaling-hypothesis))
