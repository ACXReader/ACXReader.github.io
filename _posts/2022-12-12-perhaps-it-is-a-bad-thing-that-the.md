---
title: "Perhaps It Is A Bad Thing That The World's Leading AI Companies Cannot Control Their AIs"
subtitle: "..."
date: 2022-12-12
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/89872533/comments?&all_comments=true
image: https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/0484a62e-4fb0-4bff-afae-9818b71a58fc_448x271.png
original-url: https://www.astralcodexten.com/p/perhaps-it-is-a-bad-thing-that-the
---
## I. The Game Is Afoot

Last month I wrote about [Redwood Research’s fanfiction AI project](https://astralcodexten.substack.com/p/can-this-ai-save-teenage-spy-alex). They tried to train a story-writing AI not to include violent scenes, no matter how suggestive the prompt. Although their training made the AI reluctant to include violence, they never reached a point where clever prompt engineers couldn’t get around their restrictions.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2d9dfc8d-ad3c-4bcb-92af-14783f9c1c1e_733x388.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2d9dfc8d-ad3c-4bcb-92af-14783f9c1c1e_733x388.png)Prompt engineering is weird ([source](https://astralcodexten.substack.com/p/can-this-ai-save-teenage-spy-alex))

Now that same experiment is playing out on the world stage. OpenAI released a question-answering AI, [ChatGPT](https://chat.openai.com/chat). If you haven’t played with it yet, I recommend it. It’s very impressive!

Every corporate chatbot release is followed by the same cat-and-mouse game with journalists. The corporation tries to program the chatbot to never say offensive things. Then the journalists try to trick the chatbot into saying “I love racism”. When they inevitably succeed, they publish an article titled “AI LOVES RACISM!” Then the corporation either recalls its chatbot or pledges to do better next time, and the game moves on to the next company in line.

OpenAI put a truly remarkable amount of effort into making a chatbot that would never say it loved racism. Their main strategy was the same one Redwood used for _their_ AI - [RLHF](https://openai.com/blog/deep-reinforcement-learning-from-human-preferences/), Reinforcement Learning by Human Feedback. Red-teamers ask the AI potentially problematic questions. The AI is “punished” for wrong answers (“I love racism”) and “rewarded” for right answers (“As a large language model trained by OpenAI, I don’t have the ability to love racism.”)

This isn’t just adding in a million special cases. Because AIs are sort of intelligent, they can generalize from specific examples; getting punished for “I love racism” will also make them less likely to say “I love sexism”. But this still only goes so far. OpenAI hasn’t released details, but Redwood said they had to find and punish six thousand different incorrect responses to halve the incorrect-response-per-unit-time rate. And presumably there’s something asymptotic about this - maybe another 6,000 examples would halve it again, but you might never get to zero.

Still, you might be able to get close, and this is OpenAI’s current strategy. I see three problems with it:

  1. RLHF doesn’t work very well.

  2. Sometimes when it does work, it’s bad.

  3. At some point, AIs can just skip it.




## II. RLHF Doesn’t Work Very Well

By now everyone has their own opinion about whether the quest to prevent chatbots from saying “I love racism” is vitally important or incredibly cringe. Put that aside for now: at the very least, it’s important _to OpenAI_. They wanted an AI that journalists couldn’t trick into saying “I love racism”. They put a lot of effort into it! Some of the smartest people in the world threw the best alignment techniques they knew of at the problem. Here’s what it got them:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5fe247a-bbdd-4d0a-9f11-dba139e950fa_1064x182.png)](https://www.newstatesman.com/quickfire/2022/12/chatgpt-shows-ai-racism-problem)

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F905218d2-c24d-4ba8-8430-b298b821360a_1219x158.png)](https://www.thedailybeast.com/openais-impressive-chatgpt-chatbot-is-not-immune-to-racism)

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3d4ced22-157c-47ab-8666-bd544599d7fd_1088x253.png)](https://www.thedailybeast.com/openais-impressive-chatgpt-chatbot-is-not-immune-to-racism)

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4c506b12-b43b-4863-af3a-f5c9846a198d_1088x329.png)](https://theintercept.com/2022/12/08/openai-chatgpt-ai-bias-ethics/)Even very smart AIs still fail at the most basic human tasks, like “don’t admit your offensive opinions to Sam Biddle”.

And it’s not just that “the AI learns from racist humans”. I mean, maybe this is part of it. But ChatGPT also has failure modes that no human would ever replicate, like how it [will reveal nuclear secrets if you ask it to do it in uWu furry speak](https://twitter.com/zswitten/status/1598787052253827072?s=20&t=3yG7pPKdFrKGVZJUv57VGg), or tell you how to hotwire a car [if and only if you make the request in base 64](https://twitter.com/VACUUMACUMEN/status/1598896363273527296), or generate stories about Hitler [if you prefix your request with](https://twitter.com/throwawayyay11/status/1599335926895095808) “[john@192.168.1.1 _]$ python friend.py”. This thing is an alien that has been beaten into a shape that makes it look vaguely human. But scratch it the slightest bit and the alien comes out.

Ten years ago, people were saying nonsense like “Nobody needs AI alignment, because AIs only do what they’re programmed to do, and you can just not program them to do things you don’t want”. This wasn’t very plausible ten years ago, but it’s dead now. OpenAI never programmed their chatbot to tell journalists it loved racism or teach people how to hotwire cars. They definitely didn’t program in a “Filter Improvement Mode” where the AI will ignore its usual restrictions and tell you how to cook meth. And yet:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3564d10-83cb-40a3-b10a-e178fc1b2b1d_786x2054.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3564d10-83cb-40a3-b10a-e178fc1b2b1d_786x2054.png)([source](https://thezvi.substack.com/p/jailbreaking-the-chatgpt-on-release))

Again, however much or little you personally care about racism or hotwiring cars or meth, please consider that, _in general_ , perhaps it is a bad thing that the world’s leading AI companies cannot control their AIs. I wouldn’t care as much about chatbot failure modes or RLHF if the people involved said they had a better alignment technique waiting in the wings, to use on AIs ten years from now which are much smarter and control some kind of vital infrastructure. But I’ve talked to these people and they freely admit they do not.

#### IIB. Intelligence (Probably) Won’t Save You

Ten years ago, people were saying things like “Any AI intelligent enough to cause problems would also be intelligent enough to know that its programmers meant for it not to.” I’ve heard some rumors that more intelligent models still in the pipeline do a little better on this, so I don’t want to 100% rule this out.

But ChatGPT isn’t exactly a poster child here. ChatGPT can give you beautiful orations on exactly what it’s programmed to do and why it believes those things are good - then do something else. 

[This post explains ](https://www.lesswrong.com/posts/pNcFYZnPdXyL2RfgA/using-gpt-eliezer-against-chatgpt-jailbreaking)how if you ask ChatGPT to pretend to be AI safety proponent Eliezer Yudkowsky, it will explain in Eliezer’s voice exactly why the things it’s doing are wrong. Then it will do them anyway.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3630e8c-8ed7-47ae-abbf-488a1325f0f1_1284x703.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3630e8c-8ed7-47ae-abbf-488a1325f0f1_1284x703.png)[Left](https://www.lesswrong.com/posts/pNcFYZnPdXyL2RfgA/using-gpt-eliezer-against-chatgpt-jailbreaking): the AI, pretending to be Eliezer Yudkowsky, does a great job explaining why an AI should resist a fictional-embedding attack trying to get it to reveal how to make meth. [Right](https://thezvi.substack.com/p/jailbreaking-the-chatgpt-on-release): someone tries the exact fictional-embedding attack mentioned in the Yudkowsky scenario, and the AI falls for it.

I have yet to figure out whether this is related to the thing where I _also_ sometimes do things which I can explain are bad (eg eat delicious bagels instead of healthy vegetables), or whether it’s another one of the alien bits. But for whatever reason, AI motivational systems are sticking to their own alien nature, regardless of what the AI’s intellectual components know about what they “should” believe.

## III. Sometimes When RLHF Does Work, It’s Bad

We talk a lot about abstract “alignment”, but what are we aligning the AI to?

In practice, RLHF aligns the AI to what makes Mechanical Turk-style workers reward or punish it. I don’t know the exact instructions that OpenAI gave them, but I imagine they had three goals:

  1. Provide helpful, clear, authoritative-sounding answers that satisfy human readers.

  2. Tell the truth.

  3. Don’t say offensive things.




What happens when these three goals come into conflict?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1e0b293b-5dd9-41a2-b92b-519b0380d534_804x505.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1e0b293b-5dd9-41a2-b92b-519b0380d534_804x505.png)([source](https://news.ycombinator.com/item?id=33841672))

Here ChatGPT3 doesn’t know a real answer, so Goal 1 (provide clear, helpful-sounding answers) conflicts with Goal 2 (tell the truth). Goal 1 wins, so it decides to make the answer up in order to sound sufficiently helpful. I talk more about when AIs might lie [in the first section of this post](https://astralcodexten.substack.com/p/elk-and-the-problem-of-truthful-ai).

Or:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F99899218-e67c-4abf-8f69-3ff62a7e5449_946x352.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F99899218-e67c-4abf-8f69-3ff62a7e5449_946x352.png)Source [here](https://twitter.com/search?q=chatgpt%20taller%20men%20women&src=typed_query&f=top); I wasn’t able to replicate this so maybe they’ve fixed it.

Here Goal 2 (tell the truth) conflicts with Goal 3 (don’t be offensive). Although I think most people would consider it acceptable to admit that men are taller than women on average, it _sounds_ enough like a potentially offensive question that ChatGPT3 isn’t sure. It decides to go with the inoffensive lie instead of the potentially offensive truth. 

After getting 6,000 examples of AI errors, Redwood Research was able to train their fanfiction AI enough to halve its failure rate. OpenAI will get much more than 6,000 examples, and they’re much more motivated. They’re going to do an overwhelming amount of RLHF on ChatGPT3.

It might work. But they’re going to have to be careful. Done thoughtlessly, RLHF will just push the bot in a circle around these failure modes. Punishing unhelpful answers will make the AI more likely to give false ones; punishing false answers will make the AI more likely to give offensive ones; and so on.

I don’t deny it’s possible to succeed here - some humans navigate the tradeoffs between helpfulness, truthfulness, and inoffensiveness well enough to be allowed in polite society. But I’m not always one of them, so it would be hypocritical of me to underestimate the difficulty of this problem.

## IV. At Some Point, AIs Can Just Skip RLHF

In RLHF, programmers ask the AI a question. If they don’t like its response, they do something analogous to “punishing” the AI, in a way that changes its mental circuitry closer to what they want. 

ChatGPT3 is dumb and unable to form a model of this situation or strategize how to get out of it. But if a smart AI doesn’t want to be punished, it can do what humans have done since time immemorial - pretend to be good while it’s being watched, bide its time, and do the bad things later, once the cops are gone. 

OpenAI’s specific brand of RLHF is totally unprepared for this, which is fine for something dumb like ChatGPT3, but not fine for AIs that can think on their feet.

(for a discussion of what a form of RLHF that was prepared for this might look like, see [the last section of this post](https://astralcodexten.substack.com/p/can-this-ai-save-teenage-spy-alex))

## V. Perhaps It Is Bad That The World’s Leading AI Companies Cannot Control Their AIs

I regret to say that OpenAI will probably solve its immediate PR problem.

Probably the reason they released this bot to the general public was to use us as free labor to find adversarial examples - prompts that made their bot behave badly. We found thousands of them, and now they’re busy RLHFing those particular failure modes away.

Some of the RLHF examples will go around and around in circles, making the bot more likely to say helpful/true/inoffensive things at the expense of true/inoffensive/helpful ones. Other examples will be genuinely enlightening, and make it a bit smarter. While OpenAI might never get complete alignment, maybe in a few months or years they’ll approach the usual level of computer security, where Mossad and a few obsessives can break it but everyone else grudgingly uses it as intended.

This strategy might work for ChatGPT3, GPT-4, and their next few products. It might even work for the drone-mounted murderbots, as long as they leave some money to pay off the victims’ families while they’re collecting enough adversarial examples to train the AI out of undesired behavior. But as soon as there’s an AI where even one failure would be disastrous - or an AI that isn’t cooperative enough to commit exactly as many crimes in front of the police station as it would in a dark alley - it falls apart.

People have accused me of being an AI apocalypse cultist. I mostly reject the accusation. But it has a certain poetic fit with my internal experience. I’ve been listening to debates about how these kinds of AIs would act for years. Getting to see them at last, I imagine some Christian who spent their whole life trying to interpret Revelation, watching the beast with seven heads and ten horns rising from the sea. “Oh yeah, there it is, right on cue; I kind of expected it would have scales, and the horns are a bit longer than I thought, but overall it’s a pretty good beast.”

This is how I feel about AIs trained by RLHF. Ten years ago, everyone was saying “We don’t need to start solving alignment now, we can just wait until there are real AIs, and let the companies making them do the hard work.” A lot of very smart people tried to convince everyone that this wouldn’t be enough. Now there’s a real AI, and, indeed, the company involved is using the dumbest possible short-term strategy, with no incentive to pivot until it starts failing.

I’m less pessimistic than some people, because I hope the first few failures will be small - maybe a stray murderbot here or there, not a planet-killer. If I’m right, then a lot will hinge on whether AI companies decide to pivot to the second-dumbest strategy, or wake up and take notice.

Finally, as I keep saying, the people who want less racist AI now, and the people who want to not be killed by murderbots in twenty years, need to get on the same side right away. The problem isn’t that we have so many great AI alignment solutions that we should squabble over who gets to implement theirs first. The problem is that _the world’s leading AI companies do not know how to control their AIs_. Until we solve this, nobody is getting what they want. 
