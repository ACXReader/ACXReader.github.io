---
title: "Skills Plateau Because Of Decay And Interference"
subtitle: "..."
date: 2022-08-18
likes: 167
original-url: https://www.astralcodexten.com/p/skills-plateau-because-of-decay-and
---
_**Followup to:** **[Why Do Test Scores Plateau](https://slatestarcodex.com/2017/01/13/why-do-test-scores-plateau/) ; [Ritalin Works But School Isn’t Worth Paying Attention To](https://astralcodexten.substack.com/p/study-ritalin-works-but-school-isnt)**_

## Why Do Skills Plateau?

Economist Philip Frances finds that creative artists, on average, [do their best work in their late 30s](https://www.washingtonpost.com/news/wonk/wp/2016/06/23/when-you-will-most-likely-hit-your-creative-peak-according-to-science/). Isn’t this strange? However good a writer is at age 35, they should be even better at 55 with twenty more years of practice. Sure, middle age might bring some mild proto-cognitive-impairment, but surely nothing so dire that it cancels out twenty extra years!

A natural objection is that maybe they’ve maxed out their writing ability; further practice won’t help. But this can’t be true; most 35 year old writers aren’t Shakespeare or Dickens, so higher tiers of ability must be possible. But you can’t get there just by practicing more. If acheivement is a function of talent and practice, at some point returns on practice decrease near zero.

The same is true for doctors. Young doctors (under 40) [have slightly better cure rates](http://www.bmj.com/content/357/bmj.j1797) than older doctors (eg 40-49). The linked study doesn’t go any younger (eg under 35, under 30…). However, [Goodwin et al](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5801052/) find that only first-year doctors suffer from inexperience; by a doctor’s second year, she’s doing about as well as she ever will. Why? Wouldn’t you expect someone who’s practiced medicine for twenty years to be better than someone who’s only done it for two?

We find the same phenomenon in formal education; on [a standardized test of book learning for student doctors](https://slatestarcodex.com/2017/01/13/why-do-test-scores-plateau/), there’s a big increase the first year of training, a smaller increase the second year, and by year 4-5 the increase is basically indistinguishable from zero (even though some doctors remain better than others). And [here I talk about](https://astralcodexten.substack.com/p/study-ritalin-works-but-school-isnt) a slightly different phenomenon: ADHD children given Ritalin study harder and better, but haven’t learned any more vocabulary words at the end of a course (even though they haven’t learned all the vocabulary).

After a lot of looking through the psychological literature, I’ve found two hypotheses which, combined, mostly satisfy my curiosity.

## The Decay Hypothesis

The first explanation is a “dynamic equilibrium of forgetting”.

Suppose that you forget any fact you haven’t reviewed in X amount of time (X might be shorter or longer depending on your intelligence/memory/talent). And suppose that an average doctor sees 5 diseases ~weekly, another 5 diseases ~monthly, and another 5 diseases ~yearly. A bad doctor might forget anything she sees less than once a week, a mediocre doctor might forget anything she sees less than once a month, and a great doctor might forget anything she sees less than once a year. So the bad doctor will end up knowing about 5 diseases, the mediocre doctor 10, and the great doctor 15. They will master these diseases quickly, and no matter how long they continue practicing medicine, they will never get better.

This has to be some of the story. People have investigated this hypothesis, and there are well-defined curves for how long people will remember things after different numbers of repetitions; this is the principle behind spaced repetition systems like Anki or SuperMemo.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc56fa6fc-bfb7-4aaf-8c1a-1c6ec1b35a53_671x493.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc56fa6fc-bfb7-4aaf-8c1a-1c6ec1b35a53_671x493.png)Sample forgetting curve, source [here](https://www.researchgate.net/figure/Alteration-of-the-forgetting-curve-through-repetition-according-to-Ebbinghaus-1885-and_fig3_261952026).

Still, some things don’t feel like Decay. The curve above suggests you should remember things for longer each time you review them, eventually remembering them the whole rest of your life. But if this were true, doctors would gradually add to their stock of forever-knowledge and get better with time. Meanwhile, I still remember a wildly uneven set of facts from my high school history classes, even though I’ve rarely reviewed any of them since then. Something else must be going on.

## The Interference Hypothesis

An acquaintance relates that, using flashcards, he can learn twenty words of some language (I forget which, let’s say Spanish) per day. If he studies more than twenty, too bad, he’ll only remember twenty.

But if he studies two language (let’s say Spanish and Chinese), he can learn twenty Spanish vocab words _plus_ twenty Chinese vocab words. The cap is per language, not absolute!

This suggests an interference hypothesis: once there are too many similar things in memory, they all kind of blend together and it’s hard to learn new things in the same space. It might still be easy to learn some other topic, though. However fast you can comfortably learn Spanish, you can take a karate class at the same time and learn karate and that won’t interfere.

Something like this feels intuitively true to me. I find remembering the difference between gold and silver easier than remembering the difference between yttrium and ytterbium. In fact, I remember the basics of inorganic chemistry, and the basics of organic chemistry, but not the details of either. Why do I even remember the basics? Why not forget all of it? Why is getting an introductory understanding of twenty fields easier than getting a masterly understanding of one? 

Wikipedia has [a good summary of experiments](https://en.wikipedia.org/wiki/Interference_theory) showing that memory inteference is a real phenomenon, but I can’t tell if their page is treating it as a curiosity or as the fundamental explanation for why we can’t keep learning a field forever and eventually become as gods by the time we’re 50 or 60. But I think it’s a big part of that.

This feels more convincing after learning about neural nets. The ability of neural nets to consider finely-grained concepts depends on their parameter count; the more parameters, the more distinctions they can draw. A common problem is “catastrophic forgetting”, where too high a learning rate causes a net to overfit to “remember” the most recent example, making it less good at remembering previous examples. Human memory seems to lack this failure mode, but maybe its ordinary forgetting is a tamer subspecies of the same problem.

Also, neural networks sure do show interference. I wrote a little bit about this at [A Guide To Asking Robots To Design Stained Glass Windows](https://astralcodexten.substack.com/p/a-guide-to-asking-robots-to-design), where for example any picture with a reindeer in it became a Christmas-y picture of Santa:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0195f7ea-ba82-4c89-92d3-90452d905a50_781x298.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0195f7ea-ba82-4c89-92d3-90452d905a50_781x298.png)

In this model, a bad doctor can only remember five diseases before she starts getting confused about which disease had which symptom; a good doctor might be able to handle ten, and a great doctor fifteen. And all the doctors could then learn Spanish or karate without it affecting their medical knowledge at all.

## Is That All?

These two hypotheses leave me much less puzzled by skill plateaus, but don’t entirely explain all patterns of remembering and forgetting. There seems to be something like an interestingness effect - I will never forget where I was when I heard about 9-11, but I very much forget where I was on 9-12, 9-13, etc. The decay hypothesis doesn’t explain this. Does interference? Maybe - it could be that 9-12, 9-13, etc all blend together and give me no obvious retrieval cues, whereas 9-11 was unique and so un-interfere-with-able. If devastating terrorist attacks happened once a month, each as bad as 9-11, probably I wouldn’t remember it.

But there are weird edge cases. I remember having a Baby’s First Hebrew Word Book as a child. It was mostly useful words like “cow” and “tree”, but for some reason “Master of Ceremonies” was in there also. I remember being angry that they were wasting my time with such a stupid word, and exerting deliberate effort not to learn it. Guess which one Hebrew word from that book I still remember? Is that because its uselessness set it apart and prevented anything else from interfering with it?

What about mnemonic devices? In the [Dominic System](https://en.wikipedia.org/wiki/Dominic_system), you remember long numbers by associating each digit with a letter - for example, 1 is always A, 2 is always B, and so on. 314159 becomes CADAEI. Then you convert it to people with initials - Chester Arthur, a District Attorney, Elizabeth I (I never claimed to be good at initial → people conversion). Then you form subject-verb-object sentences, treating the middle person as an action, ie “Chester Arthur prosecutes Elizabeth I”. Presumably the image of Chester Arthur suing Elizabeth I is easier to remember than the digits 314159, and if you forget the digits then you can unpack the sentence until you get them again. Does this work because there are fewer things similar to this image, to interfere with it? Actually, does it work at all? If you remember that, and then you remember some other number with the image of Chuck Norris shooting a rocket at Marie Curie, at some point do you start forgetting whether it was Chuck Norris or Elizabeth I who was shooting the rocket?

Is there some way to exploit the interference hypothesis to remember things better? Suppose you were teaching a friend Spanish, and she was struggling to learn more than 20 words per day. Could you ask her to learn a second language, but secretly it’s just more Spanish words, and at the end you tell her she was learning extra Spanish all along? Has the conspiracy already gotten there before me, and that’s what “Portuguese” is?

Finally, I conflated two things in the previous section: a limit on how much you can learn total (eg the doctor who practices for many years) and a limit on how much you can learn per day (eg twenty words of Spanish vocabulary a day). I have no evidence for the latter except the testimony of one acquaintance, and maybe the corroborating evidence from the Ritalin study. Still, if there’s a maximum amount you can learn per day (or, more likely, a diminishing returns curve) that sounds useful to know, doesn’t it? Psych undergrads asking me for study ideas, here’s your chance!
