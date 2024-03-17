---
title: "A Guide To Asking Robots To Design Stained Glass Windows"
subtitle: "..."
date: 2022-05-30
likes: 231
original-url: https://www.astralcodexten.com/p/a-guide-to-asking-robots-to-design
---
I love stained glass. Not so much your usual suburban house stained glass with a picture of lilies. The good stuff. Cathedral windows, Art Nouveau, Art Deco. Why did we stop doing that? I blame [the conspiracy](https://astralcodexten.substack.com/p/whither-tartaria?s=w).

Recently I’ve been experimenting with small-scale alternatives. You can get custom-printed window film from [these people](https://www.wallpaperforwindows.com/window-film/custom-printed-window-film/). If you print out a picture of a stained glass scene and stick it on a window, it looks pretty realistic.

But what scenes to use? Most of the stained glass images you can find are saints, which isn’t really the mood I’m going for. What I’d really like is a giant twelve-part panel depicting [the Virtues Of Rationality](https://www.yudkowsky.net/rational/virtues). But the artists I’ve asked to design this all balk. I need an artist who works for free and isn’t allowed to say no.

Enter [DALL-E-2](https://openai.com/dall-e-2/), the new art-generating AI. I’m still on the waitlist, but a friend who jumped in sooner than I did let me use their computer for a while and play around with it. This was my first introduction to the exciting world of DALL-E query framing - the surprisingly complicated relationship between what you ask the AI to do, and what it actually does. Seems on topic for this blog. So this is a combination investigation into how DALL-E thinks about queries, but also a practical guide to getting DALL-E to make good stained glass. Let’s get started.

### The Sixth Virtue: Empiricism

I’m going to go out of order here so I can demonstrate some principles from simplest to most complicated. Empiricism was the easiest window to generate. I wanted a picture of Charles Darwin studying finches. DALL-E was happy to provide.

(On these and most other images, I’ve put the prompt on the top so you can see what it’s doing. All of these “screenshots” are slightly edited. In particular, I’m only showing three rather than the usual ten so that they show up better.)

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F328f57c7-98f0-443d-b39a-20ebdb816417_672x257.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F328f57c7-98f0-443d-b39a-20ebdb816417_672x257.png)

Though even on this easiest of questions, some of the pictures could only be described as “disastrous”.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F306201a2-9715-43d4-a406-a72d8b53cbd5_746x241.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F306201a2-9715-43d4-a406-a72d8b53cbd5_746x241.png)If Darwin had really looked like this, I bet he would have had an easier time convincing people of evolution.

Still, let’s move on. 

### The Fourth Virtue: Evenness

For this one, I wanted a picture of Reverend Thomas Bayes holding a scale:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Faff70a0c-4205-4968-869d-cb67235f0e9b_697x260.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Faff70a0c-4205-4968-869d-cb67235f0e9b_697x260.png)

Some of these are okay, but they don’t especially look like Bayes. I figured that maybe DALL-E doesn’t know who Bayes is. Is that true?

The only known picture of Bayes is this one:

[![Thomas Bayes - Wikipedia](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3ef36b98-e19e-4abb-8a9a-79970172f2d0_304x326.gif)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3ef36b98-e19e-4abb-8a9a-79970172f2d0_304x326.gif)

When I ask DALL-E to give me Reverend Thomas Bayes, I get:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5a4bee1-e12e-4db5-b660-bffad1473d6b_694x277.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5a4bee1-e12e-4db5-b660-bffad1473d6b_694x277.png)

First things first: yes, DALL-E is very bad at text. Even when it’s good, it’s bad, as you can see in the last picture, “Bay of Tayees”. My guess is that it’s seen so many maps that it has a high prior on anything with the string “Bay” in it being a bay on a map, which is always called “Bay of X”. This kind of failure mode is going to be key to some of our later query engineering, so remember it.

But also - it kind of does look like Bayes. Is this because it knows who he is, or because every reverend kind of looks like this? Let’s see!

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd26593ca-fafb-4b43-9a50-983616dce1cf_680x249.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd26593ca-fafb-4b43-9a50-983616dce1cf_680x249.png)

“Thomas Bayes” without the “Reverend” still gives many pictures in the style of the one picture of Thomas Bayes. So I conclude that DALL-E really does know who Thomas Bayes is!

Usually the way these systems work is that they have a sort of Platonic ideal of what Bayes looks like, and then they vary it a little randomly (the “temperature”) in order to be able to come up with many different takes on him. It looks like DALL-E is sufficiently un-confident in its knowledge of Bayes that the random variation can change what he looks like quite a lot.

Moving back to our stained glass window, more speculatively we’re encountering at larger scale the same problem that gave us “Bay Of Tayees”. DALL-E has seen one picture of Thomas Bayes, and many pictures of reverends in stained glass windows, and it has a Platonic ideal of what a reverend in a stained glass window looks like. Sometimes the stained glass reverend looks different from Bayes, and this is able to overpower its un-confident belief in what Bayes looks like.

I think a minimum viable change the Reverend would be having him wear all black. Let’s see what happens:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbada9fa0-fae1-4c7f-b2e3-0b69daea2176_739x278.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbada9fa0-fae1-4c7f-b2e3-0b69daea2176_739x278.png)Is it just me, or is that last one Elon Musk?

The quality is now much worse! Also, we’ve lost the last vestiges of stained glass as the artistic style, and now Bayes is just standing _in front of_ a stained glass window.

Here’s my guess about what’s going on: DALL-E probably has a _lot_ of stock images from stock image sites in its database. Stock image sites describe their images very carefully. If a description gets too close to the kind of description a stock image site would use, then the style shifts to be more like the style stock image sites have, ie clip art. Since the style of clip art is different from the style of a stained glass window, DALL-E assumes the “stained glass window” in the description can’t be talking about the style, and must be a picture element.

After some trial and error, I determined that the word “dressed” seems to be a big part of the clip art. Let’s try removing that and just having him be “in black”:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0f6ceed-f556-4225-b7bf-0d891eafe878_742x280.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0f6ceed-f556-4225-b7bf-0d891eafe878_742x280.png)

This solves the problem, at the cost of the Reverend’s head.

I _think_ that by focusing on his dress (even without the taboo word “dressed”), we’re telling the AI to literally focus _on his dress_ in the image, at the cost of his head (a few images, not shown, did include the head - my selection is meant to capture a statistical tendency not to be perfectly representative).

Okay, so what if we focus on both his dress and his head, by mentioning he’s in black _and_ has black hair?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff105b46a-78cd-4959-af6b-bf371ba31b95_749x296.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff105b46a-78cd-4959-af6b-bf371ba31b95_749x296.png)

Now he is a vampire. Whatever. Let’s move on.

### The Tenth Virtue: Precision

For the virtue of Precision, I want to show Tycho Brahe, the great 17th century astronomer who measured the position and movement of the stars more precisely than any who came before him. Let’s see what we get:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F62894192-86fb-4f14-8143-b2669baa1108_785x306.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F62894192-86fb-4f14-8143-b2669baa1108_785x306.png)

Stunning! Truly excellent! Problem is, nobody’s going to know that’s supposed to be Tycho Brahe.

The most salient fact about Tycho Brahe is that he had a pet moose. Sometimes he would let the moose drink beer, and one time it got so drunk that it fell down the stairs and died. Anyway, I think everyone would know who this window was depicting if there was a moose in the background:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5984e6aa-958c-4da4-a27e-c8eba6dd3eff_782x295.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5984e6aa-958c-4da4-a27e-c8eba6dd3eff_782x295.png)

These are also great, but, I think, differently great. The stained glass has retreated from the style to become a picture element again. The style has become generally more modern.

I think what’s going on here is - nobody depicts a moose in stained glass. A man scrying the heavens through a telescope is exactly the sort of dignified thing people make stained glass windows about. A moose isn’t. So DALL-E loses confidence and decides you don’t _really_ mean it should be stained glass style.

Also, is it just me, or does Brahe look kind of like Santa here? Is it possible that wise old man + member of the family Cervidae gets into a Santa-shaped attractor region in concept space? I decided to turn the moose into a reindeer to see what happened:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0195f7ea-ba82-4c89-92d3-90452d905a50_781x298.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0195f7ea-ba82-4c89-92d3-90452d905a50_781x298.png)

Yup! Now Tycho is dressed in red, wearing a red and white cap, the reindeer is flying in the central image, and the whole thing looks kind of Christmas-y (though, to be fair, still also like stained glass).

But I really do want a picture of Tycho and his moose. By trial and error, I discovered that it works fine if you substitute Tycho with his fellow astronomer, William Herschel:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F26e64e83-a87d-4a16-a32d-6f7bb593c920_785x289.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F26e64e83-a87d-4a16-a32d-6f7bb593c920_785x289.png)

This isn’t perfect - in particular, the second picture seems unsure whether the picture itself is a window, or the picture includes a window - but they all sort of work.

It works even better if you replace “moose” with “deer”:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2a50b69-6a59-4598-a3e1-bd53c26e84f3_786x300.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2a50b69-6a59-4598-a3e1-bd53c26e84f3_786x300.png)

No mortal can truly understand the mind of DALL-E, but I think that either it’s more confident in who Herschel is than who Brahe is, anchoring it to “stained glass depictions of specific historical figures who are known not to be Santa Claus”. Or possibly “Tycho Brahe” sounds kind of fanciful, like the sort of person who _might_ secretly be Santa Claus if you dig a little deeper, but “William Herschel” sounds like a respectable English historical figure who has far too Jewish a name to be Santa.

As for deer, they’re a more common subject of classical art than moose are, so they shift the genre out of “classical Renaissance-looking stained glass window” less.

### The Seventh Virtue: Simplicity

It’s got to be Occam with his razor, right? So:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F63170470-b383-4e7e-9673-a6f01e61d40d_792x293.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F63170470-b383-4e7e-9673-a6f01e61d40d_792x293.png)GILA-WHAMM!

Okaaaay. There’s a lot to unpack here.

When I Google “medieval razor”, I get things that look like this:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fef8dbcca-99db-4193-ac33-a648c556399f_450x337.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fef8dbcca-99db-4193-ac33-a648c556399f_450x337.png)

…so that second picture is actually historically accurate and DALL-E knows more about the history of razors than I do. 

The knife-like razor was also used during medieval times, though probably not with the exact expression that Occam has in panel three. I think DALL-E assumes that if you are holding a sharp knife-like object, you are probably trying to kill someone. And if you are trying to kill someone with a knife, you probably have red hair and a red beard (William of Ockham didn’t look like that, but most of the pictures DALL-E generates do).

GilaWhamm might be some kind of demented spoonerism of “William Ockham”, though I think it would also be a good name for a shaving brand:

>  _Think BurmaShave’s / a pricy scam?  
>  Save on cash / With GilaWhamm!_

But also, these stained glass windows are a very different style than some of the earlier ones. Compare Darwin’s finches with Occam’s razor:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0e7927e-0f92-4aff-8006-b1b5ffc45768_483x208.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0e7927e-0f92-4aff-8006-b1b5ffc45768_483x208.png)

Darwin is done in the style of the late 1800s; Occam in the style of the Middle Ages. DALL-E knows who both these figures are, and is putting each of them in the context of their period.

You can make it even worse by calling him “William **of** Ockham” - Dall-E knows that “X of Y” names are medieval:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb873030-45f3-4362-95c6-bc9e7e0d6849_786x289.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb873030-45f3-4362-95c6-bc9e7e0d6849_786x289.png)

But I already chose my Darwin picture, and I want an Occam picture in the same style. What happens if I tell DALL-E that it should be Art Nouveau?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6a07a6c3-af87-4359-80df-6073d3d821dc_810x287.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6a07a6c3-af87-4359-80df-6073d3d821dc_810x287.png)I wish I was as sure of anything as DALL-E is as sure that William Ockham had a giant red beard. Or that “William Ockham” is spelled “THAMHHH AR”

Meeeediocre. What if I really overload it with stylistic cues?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8b3b08f-bca1-4966-a198-6ec92627da30_799x314.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8b3b08f-bca1-4966-a198-6ec92627da30_799x314.png)

WAIT NO I JUST GOT IT! The reason William of Ockham has the giant beard is because most of the corpus of images with people holding razors is SHAVING ADVERTISEMENTS! 

(but why red in particular?)

### The Third Virtue: Lightness

Oh God, Lightness. This one was such a mess.

I wanted it to be a hot air balloon. But:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc35a32fb-7274-4c52-89d9-f4f44551273f_796x316.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc35a32fb-7274-4c52-89d9-f4f44551273f_796x316.png)

Just as “moose” suggests Christmas, and “William of Ockham” suggests medieval times, “hot air balloon” suggests “amateur stained glass artist who wants to make something colorful and geometric and cute”. 

The old “add Art Nouveau” trick didn’t help much, but after trying a lot of things, I noticed that all the previous examples had people’s names. Maybe having a historical figure grounds it in the sort of stained glass windows people made during the figure’s time period?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8a5ec912-da3e-4724-b65c-7818df0816fc_775x299.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8a5ec912-da3e-4724-b65c-7818df0816fc_775x299.png)

…something is happening here, but I’m not sure I like it.

The first hot air balloon was launched by the Montgolfier brothers in 1783, maybe they can help us:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F98f6d95a-0ed1-4889-91bc-a63dfe8879ec_763x289.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F98f6d95a-0ed1-4889-91bc-a63dfe8879ec_763x289.png)

Quite the improvement! What if we get more specific?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7ce8bd33-5788-4e06-933c-31bc8ae90031_688x277.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7ce8bd33-5788-4e06-933c-31bc8ae90031_688x277.png)

Yeeeeeeaaah! This is the good stuff! Does it keep getting better as I add more and more French names?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcd12d10-4826-465f-8294-f472cc4147e6_778x282.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcd12d10-4826-465f-8294-f472cc4147e6_778x282.png)

Not really, no. But it was worth a try.

### The Eleventh Virtue: Scholarship

My plan for this one was Alexandra Elbakyan (the Sci-Hub woman) in a library, with the Sci-Hub mascot (a raven with a key in its mouth).

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5eb34e40-29b3-4a47-8461-8e62efa5c2ed_800x304.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5eb34e40-29b3-4a47-8461-8e62efa5c2ed_800x304.png)

For the record, Alexandra Elbakyan looks like this:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0b6579d-3f44-4e08-be82-15720890f4fc_395x335.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0b6579d-3f44-4e08-be82-15720890f4fc_395x335.png)

…and not like a Goth version of Hermione Granger. I think DALL-E assumes that anybody in the vicinity of a raven must be a Goth, and anybody in a library must be at least sort of Hermione Granger (I bet its corpus included a _lot_ of Harry Potter fan art).

More important, we’ve completely lost the stained glass window look, in favor of the library having a window in it. I think the AI feels like if we’re talking about libraries and windows, the window _must_ be in the library, regardless of what the query says.

Also, none of these pictures even attempt to have a key in the raven’s mouth. Whatever, I can Photoshop that in later.

Let’s try again, switching the potentially window-bearing “library” to the hopefully more neutral “bookshelves”:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe26be402-2915-4eca-9efe-a9295f9d4b30_786x292.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe26be402-2915-4eca-9efe-a9295f9d4b30_786x292.png)

Why did the quality drop so sharply? I think that “library” suggests a certain style of maybe Harry Potter fan art which keeps up at least some minimal quality standards, and “bookshelves” doesn’t.

Maybe Alexandra Elbakyan is part of the problem? Maybe a more proper 19th-century figure would get me a more proper 19th-century stained glass window?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4f1c5f9-99ac-45af-86ad-217295204faa_779x306.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4f1c5f9-99ac-45af-86ad-217295204faa_779x306.png)

Now we’ve doubled down on the Gothicism, and on lace collars in particular. In retrospect, I should have realized that although DALL-E has some idea who Ada Lovelace is, it’s not _totally_ confident that’s her name, and wants to cover its bases in case she’s just someone who loves lace a lot.

Let’s try overwhelming it with stylistic cues:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb282aee-f159-499a-947d-44cef273ec21_776x294.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb282aee-f159-499a-947d-44cef273ec21_776x294.png)

Getting closer! Let’s redefine “overwhelm”:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fad4722f3-597e-482d-954b-335713fa2b88_770x314.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fad4722f3-597e-482d-954b-335713fa2b88_770x314.png)

Oh nooooo! We’ve gone too far! [We are play gods!](http://dresdencodak.com/2009/09/22/caveman-science-fiction/) Abort abort abort!

### Final Thoughts

The most interesting thing I learned from this experience is that DALL-E can’t separate styles from subject matters (or birds from humans).

If you ask it for a stained glass scene of something that seems stained-glass-y, it will do a good job. If you ask it for a stained glass scene of something that isn’t traditionally depicted in stained glass, it will assume it’s misunderstanding your query and do something else. And if you ask it for a scene where it’s more plausible for the stained glass to be _in_ the scene than _the style of_ the scene, it will put the stained glass in the scene.

If you give it a subject that sounds like the kind of thing depicted in medieval stained glass, it will depict it in a medieval way. If you give it a subject that sounds more modern, it will depict it in a more modern way. Some topics, like Santa Claus and Hermione Granger, form vast black-hole-like attractor basins in conceptual space, dragging in anything even remotely related, and turning the scene into Christmas decorations or Harry Potter fan art. 

Every object in a scene influences everything else in a scene. If you add a moose, the entire scene will look more like the sort of scene where mooses might appear. If you add a razor, all the characters will look a bit more like the characters in shaving ads, even if they are medieval monks.

To get a subject depicted in a specific style, you need to balance the attention paid to style and subject. Talk too much about the style, and you’ll get the sort of scene which is typically depicted in that style, regardless of what scene you want. Talk too much about the scene, and you’ll get the sort of style that scene is usually depicted in, regardless of what style you told it. Query engineering is about figuring out ways so that each additional thing you add reinforces DALL-E’s idea of what you want, instead of detracting from it.

DALL-E is clearly capable of incredible work. That having been said, I mostly couldn’t access it. Although it can make stunning stained glass of traditional stained-glass subjects, trying to get it to do anything at all unusual degrades the style until you end up picking the best of a bad lot and being grateful for it. You can try to recover the style by adding more and more stylistic cues, but it’s really hit-or-miss, and you can never be sure you’ll get two scenes depicted in the same (or even remotely similar) styles, which kind of sinks my plan for a twelve-part window.

I’m not going to make the mistake of saying these problems are inherent to AI art. My guess is a slightly better language model would solve most of them, and the ability to have it view other pictures (ie “a picture of X in the style of Y”) would solve the rest. For all I know, some of the larger image models have already fixed these issues. These are the sorts of problems I expect to go away with a few months of future research.

But for now, if you want robots to design your stained glass windows for you, it will be a long slog through a bunch of different queries.

(thanks to a friend who wishes to remain anonymous for letting me use their computer with DALL-E access to write this)
