---
title: "WebMD, And The Tragedy Of Legible Expertise"
subtitle: "What does running a medical database teach you about why everything sucks?"
date: 2021-02-05
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/32242316/comments?&all_comments=true
image: https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/c164b79f-835d-4010-a364-91591a857eaf_417x436.png
original-url: https://www.astralcodexten.com/p/webmd-and-the-tragedy-of-legible
---
**I.**

I started a small database of psychiatry information. It's going well. I'm grateful for all your emails suggesting changes and corrections. Sort of.

Here are some of the kinds of emails I get:

**"You listed three major side effects of this drug, but I got a side effect that isn't on your list. Maybe you should add it in."** All drugs have an infinite number of possible side effects. One in a zillion people who use Naproxen ("Aleve") becomes red-green colorblind. Capecitabine ("Xeloda") can sometimes make you lose your fingerprints, which sucks if your computer has biometric security. If listed all side effects of anything, we would be here all day. Still, I get nervous when I get emails like this. What if an interior designer takes Aleve, loses their color vision, and it's my fault for not warning them?

**"You said Drug A is better for most people than Drug B. But I tried Drug A and it was terrible, then I tried Drug B and it cured everything. I think you need to make it clearer that Drug B can be better than Drug A sometimes."** Investing in index funds is usually better than investing in lottery tickets, but one guy will get a winning lottery ticket on the day the stock market crashes and have the opposite result; it's still valuable to warn investors that one thing is better than another. On the other hand, The Last Psychiatrist blames overly facile Drug A/Drug B comparisons for [killing David Foster Wallace](https://thelastpsychiatrist.com/2009/04/how_dangerous_is_academic_psyc_1.html). Do I want to kill David Foster Wallace? Sometimes, when I think about all the loose ends in _Infinite Jest_ \- but most of the time no.

**"You said this drug is occasionally mildly addictive but the risk/benefit calculation is worth it for most people. But my cousin's friend took it and became really addicted and it ruined his life. Maybe you should warn readers about it more emphatically."** The particular example I'm thinking of is something exotic, but something like Adderall could equally well be in this category. Still, I get nervous whenever I get emails like this. What if I do ruin somebody's life? Maybe I should just change the wording to "this drug has some benefits but is often addictive, be careful with it"?

**"You listed some funny facts about this disorder, but this disorder is really serious and killed my grandmother".** I have a lot of trouble being serious, and this has served me well in getting people to read and enjoy things I write. But almost everything in medicine has killed at least one person's grandmother. Obviously you should be sensitive, but can you never mention any of the weird and hilarious things that go on in psychiatry?

In some sense I do appreciate all of this feedback; even when I don't take it, it helps compensate for my own biases. Still, there's a thin line between a compliment from an architecture connosseiur and a threat from a mafioso: "Nice house you have there, shame if something were to happen to it". In the same way, there's a thin line between helpful suggestions related to medicine and veiled threats of lawsuits, cancellation, and the like. 

For each individual case, the temptation is to retreat. "Yeah, sorry, I forgot to list this side effect which is obviously very important to you", "Yeah, in retrospect it is a little offensive to be joking about a heavily stigmatized disorder". For each individual case, this is fine.

My fear is that if I do this enough, I become WebMD.

WebMD is the Internet's most important source of medical information. It's also surprisingly useless. Its most famous problem is that whatever your symptoms, it'll tell you that you have cancer. But the closer you look, the more problems you notice. Consider drug side effects. Here's WebMD's list of side effects for a certain drug, let's call it Drug 1:

> Upset stomach and heartburn may occur. If either of these effects persist or worsen, tell your doctor or pharmacist promptly. If your doctor has directed you to use this medication, remember that he or she has judged that the benefit to you is greater than the risk of side effects. Many people using this medication do not have serious side effects. Tell your doctor right away if you have any serious side effects, including: easy bruising/bleeding, difficulty hearing, ringing in the ears, signs of kidney problems (such as change in the amount of urine), persistent or severe nausea/vomiting, unexplained tiredness, dizziness, dark urine, yellowing eyes/skin. This drug may rarely cause serious bleeding from the stomach/intestine or other areas of the body. If you notice any of the following very serious side effects, get medical help right away: black/tarry stools, persistent or severe stomach/abdominal pain, vomit that looks like coffee grounds, trouble speaking, weakness on one side of the body, sudden vision changes or severe headache.

And here's their list of side effects for let's call it Drug 2:

> Nausea, loss of appetite, or stomach/abdominal pain may occur. If any of these effects persist or worsen, tell your doctor or pharmacist promptly. Remember that your doctor has prescribed this medication because he or she has judged that the benefit to you is greater than the risk of side effects. Many people using this medication do not have serious side effects. This medication can cause serious bleeding if it affects your blood clotting proteins too much. Even if your doctor stops your medication, this risk of bleeding can continue for up to a week. Tell your doctor right away if you have any signs of serious bleeding, including: unusual pain/swelling/discomfort, unusual/easy bruising, prolonged bleeding from cuts or gums, persistent/frequent nosebleeds, unusually heavy/prolonged menstrual flow, pink/dark urine, coughing up blood, vomit that is bloody or looks like coffee grounds, severe headache, dizziness/fainting, unusual or persistent tiredness/weakness, bloody/black/tarry stools, chest pain, shortness of breath, difficulty swallowing.

Drug 1 is aspirin. Drug 2 is warfarin, which causes 40,000 ER visits a year and is widely considered one of the most dangerous drugs in common use. I challenge anyone to figure out, using WebMD's side effects list alone, that warfarin is more dangerous than aspirin. I think this is because if WebMD said "aspirin is pretty safe and most people don't need to worry about it", people might use aspirin irresponsibly, die, and then their ghosts might sue WebMD. Or if WebMD said "warfarin can be dangerous, be careful with this one", people might refuse to take warfarin because "the Internet said it was dangerous", die of the stuff warfarin is supposed to treat, and then their ghosts might sue WebMD. WebMD solves this by never giving the tiniest shred of useful information to anybody.

This is actually a widespread problem in medicine. The worst offender is the FDA, which tends to list every problem anyone had while on a drug as a potential drug side effect, even if it obviously isn't. This got some press lately when Moderna had to disclose to the FDA that one of the coronavirus vaccine patients [got struck by lightning](https://www.ladbible.com/news/news-moderna-volunteer-struck-by-lightning-month-after-receiving-vaccine-20201219); after a review, this was declared probably unrelated. For the more serious version of this, read [Get Ready For False Side Effects](https://blogs.sciencemag.org/pipeline/archives/2020/12/04/get-ready-for-false-side-effects). Why does the FDA keep doing this if they know it makes their label information useless? My guess is it's because they don't want to look like cowboys who unprincipledly consider some things but not other things. What if someone accused the person deciding what things to consider of being biased? So the FDA comes up with a Procedure, and once you have a Procedure it has to be "take everything seriously", and then it falls on random small-fry people who aren't the FDA to pick up the slack and explain which side effects are worth worrying about or not, and then those small fries don't do that, because they could get sued.

I think the same concern motivates WebMD diagnosing everything as cancer. If they said something other than cancer, then people might sigh with relief, not bother to get a cancer screening, die from some weird cancer that doesn't present the way normal cancers do, and then their ghosts might sue WebMD.

[![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2f836147-a1f2-4ae1-8b87-18b603aa290b_680x372.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2f836147-a1f2-4ae1-8b87-18b603aa290b_680x372.png)

_([source](https://twitter.com/chaosprime/status/1356268346778509312))_

Right now I think my database is better and more useful than WebMD. This isn't because I'm smarter or more of an expert than whoever WebMD employs. It's because I'm small enough to have a sort of security by obscurity.

If some bad thing will happen to one in a million people who read my site - they take Drug A because I said it was better for most people, but it was worse for them, and it injures them - probably my site will never get a million readers and I won't have to worry about it. WebMD gets a million readers a day and worries about it a lot.

If some lawyer with dollar signs in their eyes where the pupils should be reads my website, they know I'm not rich enough to be worth their time. WebMD is definitely rich enough to be worth their time.

If I think it's helpful to mention politically incorrect stereotypes (is it true that disproportionately many borderline personality cases are young women with lots of piercings and tattoos? what does that tell us about diagnosis and etiology?) I can do that, knowing that I'm probably not worth the mob's time to cancel. Also, I'm my own boss and don't have to worry about getting hauled in front of WebMD's Chief Diversity Officer.

If I think it's helpful to have a personal opinion on something (eg which antidepressants are scams), I can write my personal opinion without having a boss who can tell me to stop being a cowboy and devise a Procedure instead. I don't really have to worry that the pharmaceutical companies whose antidepressants I am calling scams will care enough to sue me for libel, or destroy my reputation, or lock me out of cool biotech industry meetings, or whatever.

The essence of [Moloch ](https://slatestarcodex.com/2014/07/30/meditations-on-moloch/)is that if you want to win intense competitions, you have to optimize for winning intense competitions - not for some unrelated thing like giving good medical advice. Google apparently has hard-coded into their search algorithm that WebMD should be on the front page for any medical-related search; I would say they have handily won the intense competition that they're in. They must have placated a wide variety of stakeholders and fought off a wide variety of attackers; each of those victories took a minor change to their medical information or their procedures for producing medical information. Repeat a thousand times, and they're on top of the world, and also every diagnosis is "cancer" and every drug's side effects are "everything".

WebMD is too big, too legitimate, and too canonical to be good.

**II.**

Dr. Anthony Fauci is the WebMD of people.

At least this is the impression I get from this [rather hostile biography](https://www.thedriftmag.com/the-case-against-fauci/). He's a very smart and competent doctor, who wanted to make a positive difference in the US medical establishment, and who quickly learned how to play the game of flattering and placating the right people in order to keep power. In the end, he got power, sometimes he used it well, and other times he struck compromises between using it well and doing dumb things that he needed to do to keep his position.

I don't want to judge him. Everyone has to make their own compromise between morally-pure-but-useless and tainted-but-useful, and I think Fauci comes out better than many. This isn't about judgment. 

This is about, well - in 2015, if you and a few of your weird friends beat the experts, it was new and exciting. You would prance around, singing "We beat the experts! We beat the experts!" In 2021 it's just depressing. Are the experts okay? Do they need help? Blink once for yes, twice for no...

I can't tell you how many times over the past year all the experts, the CDC, the WHO, the _New York Times_ , et cetera, have said something (or been silent about something in a suggestive way), and then some blogger I trusted [said the opposite](https://www.scottaaronson.com/blog/?p=4695), and the blogger turned out to be right. I realize this kind of thing is vulnerable to selection bias, but it's been the same couple of bloggers throughout, people who I already trusted and already suspected might be better than the experts in a lot of ways. [Zvi Mowshowitz](https://thezvi.wordpress.com/) is the first name to come to mind, though there are many others. 

There are all sorts of places you could go with this. Maybe expertise is a sham, and a smart guy thinking for five minutes can outdo a decade of working on a PhD. Maybe Joe Biden is an idiot for not appointing Zvi the Secretary of Health. Maybe the whole system is a plot to keep good people down, and we need to burn it down and start over again. Or maybe I'm dumb and biased, and actually the experts are doing much better than Zvi but I'm selectively misinterpreting evidence until I think they aren't.

Probably all of these have a grain of truth in them. But I find myself settling on a different explanation, which is something like this:

When Zvi asserts an opinion, he has only one thing he's optimizing for - being right - and he does it well.

When the Director of the CDC asserts an opinion, she has to optimize for two things - being right, and keeping power. If she doesn't optimize for the second, she gets replaced as CDC Director by someone who does. That means she's trying to solve a harder problem than Zvi is, and it makes sense that sometimes, despite having more resources than Zvi, she does worse at it.

The way I imagine this is that Zvi reads some papers on whether the coronavirus has airborne transmission, sees the direction they're leaning, and announces on his blog that it probably has airborne transmission.

The Director of the CDC reads those same papers. But some important Senator says that if airborne transmission is announced, important industries in his state will go bankrupt. Citizens Against Lockdowns argues that the CDC already screwed up by stressing the later-proven-not-to-exist fomite-based transmission, ignoring the needs of ordinary people in favor of a bias towards imagining hypothetical transmission mechanisms that never materialize; some sympathetic Congressman tells the director that if she makes that same mistake a second time, she's out. One of the papers saying that airborne transmission is impossible comes from Stanford, and the Director owes the dean of Stanford's epidemiology department a favor for helping gather support for one of her policies once. So the Director puts out a press release saying the evidence is not _quite_ strong enough to say airborne transmission definitely happens, and they'll review it further.

I realize it doesn't sound like it, but I'm trying to excuse the CDC here. I'm not just saying they're corrupt. I'm saying they have to deal with the inevitable amount of corruption which it takes to be part of a democratic government, and they're handling it as well as they can under the circumstances. 

Expertise isn't a sham. The Director of the CDC could generate opinions as accurate as (or more accurate than) Zvi's, if she wanted to. Maybe she's even doing that internally, when she decides what precautions she and her family should take. Or maybe she isn't; I know a lot of people who have turned into the mask they put on to succeed, just because it's easier that way. The Director may carefully avoid being the kind of person who can generate opinions more accurate than the ones she has to officially endorse; this is probably the best option for her mental health.

Joe Biden can't appoint Zvi as CDC Director, at least not usefully. If Biden appointed Zvi as Director one of three things would happen. One, Zvi would learn to play politics as adroitly as the current Director, and lose his advantage over her. Two, Zvi would offend enough people that they would pressure Biden to fire him. Or three, Zvi would offend people, Biden would offend people by not firing Zvi, and eventually Biden would fall beneath some necessary threshold of support and not be able to be an effective President. I'm not saying that just appointing Zvi would inevitably get Biden impeached. I'm saying Biden has a certain amount of slack, given how many people he needs to keep happy in order to govern effectively, and appointing Zvi as CDC Director would use up so much of that slack that he couldn't do other equally useful things later without becoming ineffective and likely to lose reelection.

**III.**

The first reason I'm talking about this now is to respond to a point that came up in my discussions with Glen Weyl on technocracy.

I think Weyl thinks of the world like this: some experts make a plan. But experts are often biased or corrupt. So if we expose the plan to lots of democratic feedback, then ordinary people, who aren't biased or corrupt, will drag it in the direction of being better.

Sometimes this is true. But other times I use a different model. Some experts make a plan. Experts are sometimes unbiased and not-corrupt, at least insofar as it's possible for anyone to be unbiased and non-corrupt in this world. If you expose the plan to politics, the politics will drag it in the direction of being worse. Every feedback channel you open up is a way for somebody to attack you. 

If you're planning the coronavirus response, maybe the best thing you can do is lock Zvi in a cave completely incommunicado and make him write one for you. The moment there's a gap in the cave, thousands of lobbyists and activists and politicians will rush in, trying to sue him or bribe him or threaten him or guilt him into changing it to favor their constituency. If he has the slightest shred of self-preservation, the end result will be some balance between the good plan he would have written earlier, and the stuff he needs to include to avoid getting sued or fired or cancelled or universally-loathed or mobbed. 

**IV.**

The second reason I'm writing this is because people keep asking me "should we listen to experts"?

As usual, the answer is "it depends who you mean by we".

Here's a story which is very flattering and which I hope is true: Zvi gives better advice than the Director of the CDC. This isn't a very legible fact - it's not obvious from the titles each one has - but due to various personal advantages, like having known Zvi for ten years and thinking in the same idiom he does, I'm able to recognize this. I can take Zvi's advice instead of the Director's advice, and benefit from it.

(if you trust me, you probably also trust Zvi now that you’ve read this. But you only trust me because you’ve read me for years, think in the same idiom I do, etc, etc.)

Even if this flattering story is true, it doesn't scale. My personal tendency will be to always trust Zvi. But someone else will decide to always trust *their* friend, a guy in a MAGA cap who says coronavirus is fake and Dr. Fauci is a Satanist. Compared to the _median_ person who disagrees with the experts, the experts look pretty good.

My household locked down two weeks before the general shelter-in-place order went out (this is entirely to the credit of one of my housemates, who did her homework really well). We beat the experts. But our workplaces mostly didn't; they were up and running until the government forced them to stop. Up until the moment the shelter-in-place order dropped, I kept hearing stories of parents trying to pull their kids out of public school, only to get told that their unfounded virophobia didn't matter and their children would be given failing grades if they didn't attend. The experts successfully swooped in and saved us from all of that, figuring out which way the wind was blowing only two weeks later than competent amateurs. This was a useful service. Without the experts, things would have stayed open forever.

Obviously the best case scenario would be that Zvi or whoever _was_ the expert, and could have done what they did, only earlier. But this is assuming away the entire problem. What's the best form of government? Benevolent dictatorship, obviously, just get the best person in the country and let her fix everything. But everyone realizes this is easier said than done; the procedure to pick the best person is corruptible. At one point we tried a very simple best-person-picking procedure that really should have worked and ended up choosing Donald Trump as the best person. I'm still not really sure what went wrong there, but apparently this is really hard. 

In this model, Zvi is illegibly good. It's easy for a random person to be illegibly good. They just do good things, and a few of their close friends who have known them for a long time notice they're good, and then those close friends reap the benefits.

Dr. Fauci (and WebMD) are legibly good (or at least legibly okay). They sit on a giant golden throne, with a giant neon arrow pointing to them saying "TRUST THIS GUY". If a random shmuck who doesn't know anything about anything Googles "who should I trust about COVID?", Google will return Dr. Fauci's name. This is a position of great power; Dr. Fauci is able to make decisions that will affect billions of dollars in wealth, Senate seats, Twitter likes, and other extremely valuable resources. Thousands of people who would prefer that _they_ get the dollars and seats and likes will be gunning for him. In order to stay on that throne, Dr. Fauci will need to get and keep lots of powerful allies (plus be the sort of person who thinks in terms of how to get allies rather than being minimaxed for COVID-prediction).   
  
This interferes with his COVID predicting ability, but in the current system there’s no alternative. You can't trivially put Zvi on that throne, any more than you could trivially make Zvi benevolent dictator of the world (another job I think he would be good at). One of the big differences between good and bad systems of government is how much they rely on corruption vs. meritocracy in putting people on those thrones, and our system of government is only mediocre. As the saying goes, "there are no First World countries".

**V.**

The third reason I'm writing this is to explain a sort of missing mood.

I think experts have failed terribly on easy problems. Shouldn't I be taking to the streets, pitchfork in hand, trying to burn down the system? Some of my friends are; they've gotten radicalized by all of this, a weird mix of far-left and far-right and I-don't-even-know-anymore-just-something-other-than-this. I'm not that radical. I continue to support gradual change. Isn't that weird?

What I sometimes call Marx's Fallacy is that if we burnt down the current system, some group of people who optimized for things other than power would naturally rise to the top. Wrong. People who most brutally and nakedly optimized for power would gain power; that's what "optimize" means. The interesting thing about the current system is that, after millions of very smart and altruistic people have contributed to it over generations, sometimes gaining and keeping power within it is modestly correlated with being good and right. The Director of the CDC isn't a COVID denialist. She's probably not even going to endorse Lysenkoism, at least not literally. That's because our system isn't as crappy as the Stalinist one, which failed so badly that endorsing Lysenkoism became a route to career success. In fact, the last Director of the CDC disagreed with his boss (Donald Trump) in a lot of cases where his boss was wrong; that never would have happened under Stalinism, and probably wouldn't happen in whatever system you'd get after burning ours to the ground. Our system of expert-having is actually much better than we deserve, given that we elected Donald Trump president. Making it better should still be our top priority, but we shouldn't lose sight of how much we've already got.

This means experts can play an important role; they're people who are legibly mediocre. Zvi is illegibly great, but there's no simple way to convert that to "legibly great" without sacrificing some of his greatness. I think our system for producing legibly-mediocre people is a good start. It doesn't always pick the most trustworthy people. But it almost always gets someone in the top 50%, sometimes the top 25%. There are few biologists who deny evolution, few epidemiologists who think vaccines don't work, and few economists who are outright communists.

Think of centers of expertise like the CDC or the IGM Economists Panel as giant systems for disentangling corruption and power. Their job is to produce one or two people who can get in front of the population and say something which has some resemblance to reality, even though _the entire rest of the economy and body politic is trying to corrupt them_. They...actually do sort of okay. Anthony Fauci is neither Attila the Hun nor Trofim Lysenko. He's a kind of bumbling careerist with a decent understanding of epidemiology and a heart that's more or less in the right place. The whole scientific-technocratic complex is a machine which takes Moloch as input and manages - after spending billions of dollars and the careers of thousands of hard-working public servants - to produce Anthony Fauci as output. This should be astonishing, and we are insufficiently grateful.

(but prediction markets would still be better)
