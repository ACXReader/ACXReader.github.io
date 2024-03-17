---
title: "Semaglutidonomics"
subtitle: "140 million obese Americans x $15,000/year for obesity drugs = . . . uh oh, that can't be right."
date: 2022-11-24
likes: 214
original-url: https://www.astralcodexten.com/p/semaglutidonomics
---
## The Story So Far

Semaglutide started off as a diabetes medication. Pharma company Novo Nordisk developed it in the early 2010s, and the FDA approved it under the brand names Ozempic® (for the injectable) and Rybelsus® (for the pill).

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb896d516-568b-4f72-9477-a6757e6a194e_463x351.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb896d516-568b-4f72-9477-a6757e6a194e_463x351.png)I think “Ozempic” sounds like one of those unsinkable ocean liners, and “Rybelsus” sounds like a benevolent mythological blacksmith.

Patients reported significant weight loss as a side effect. Semaglutide was a GLP-1 agonist, a type of drug that has good theoretical reasons to affect weight, so Novo Nordisk [studied this](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5573908/) and found that yes, it definitely caused people to lose a lot of weight. More weight than any safe drug had ever caused people to lose before. In 2021, the FDA approved semaglutide for weight loss under the brand name Wegovy®.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F13ec390a-e8fd-4680-8da1-eace4f42ba74_1159x645.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F13ec390a-e8fd-4680-8da1-eace4f42ba74_1159x645.png)“Wegovy” sounds like either a cooperative governance platform, or some kind of obscure medieval sin. 

Weight loss pills have a bad reputation. But Wegovy is a big step up. It doesn’t work for everybody. But it works for 66-84% of people, depending on your threshold. 

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4b4ffd4-3d5b-445c-961d-f562ca14ac0f_818x220.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4b4ffd4-3d5b-445c-961d-f562ca14ac0f_818x220.png)([Source](https://khn.org/wp-content/uploads/sites/2/2022/09/Morgan-Stanley_Unlocking-the-Obesity-Challenge.pdf))

Of six major weight loss drugs, only two - Wegovy and Qsymia - have a better than 50-50 chance of helping you lose 10% of your weight. Qsymia works partly by making food taste terrible; it can also cause cognitive issues. Wegovy feels more natural; patients just feel full and satisfied after they’ve eaten a healthy amount of food. You can read the gushing anecdotes [here](https://chadnauseam.com/random/semaglutide-has-changed-the-world/) (plus some extra anecdotes [in the comments](https://www.reddit.com/r/slatestarcodex/comments/y40owh/semaglutide_has_changed_the_world/)). Wegovy patients also [lose more weight](https://www.drugtopics.com/view/a-review-of-fda-approved-medications-for-chronic-weight-management) on average than Qsymia patients - 15% compared to 10%. It’s just a really impressive drug.

Until now, doctors didn’t really use medication to treat obesity; the drugs either didn’t work or had too many side effects. They recommended either diet and exercise (for easier cases) or bariatric surgery (for harder ones). Semaglutide marks the start of a new generation of weight loss drugs that are more clearly worthwhile.

## Modeling Semaglutide Accessibility

40% of Americans are obese - that’s 140 million people. Most of them would prefer to be less obese. Suppose that a quarter of them want semaglutide. That’s 35 million prescriptions. Semaglutide costs about $15,000 per year, multiply it out, that’s about $500 billion.

Americans currently spend $300 billion per year total on prescription drugs. So if a quarter of the obese population got semaglutide, that would cost almost twice as much as all other drug spending combined. It would probably bankrupt half the health care industry.

So . . . most people who want semaglutide won’t get it? Unclear. America’s current policy for controlling medical costs is to buy random things at random prices, then send all the bills to an illiterate reindeer-herder named Yagmuk, who burns them for warmth. Anything could happen!

 _Right now_ , only about 50,000 Americans take semaglutide for obesity. I’m basing this off [this report](https://www.fiercepharma.com/pharma/novos-wegovy-supply-rebound-track-second-half-2022-execs-break-out-first-ever-sales-figures) claiming “20,000 weekly US prescriptions” of Wegovy; since it’s taken once per week, maybe this means there are 20,000 users? Or maybe each prescription contains enough Wegovy to last a month and there are 80,000 users? I’m not sure, but it’s somewhere in the mid five digits, which I’m rounding to 50,000.

That’s only 0.1% of the potential 35 million. The next few sections of this post are about why so few people are on semaglutide, and whether we should expect that to change. I’ll start by going over my model of what determines semaglutide use, then look at a Morgan Stanley projection of what will happen over the next decade.

 **Step 1: Awareness**

I model semaglutide use as _interest * awareness * prescription accessibility * affordability_. I already randomly guessed interest at 25%, so the next step is awareness. How many people are aware of semaglutide?

The answer is: a lot more now than when I first started writing this article! [Novo Nordisk’s Wegovy Gets Surprise Endorsement From Elon Musk](https://www.fiercepharma.com/marketing/novo-nordisks-wegovy-gets-surprise-endorsement-twitters-soon-be-new-owner-elon-musk), says the headline. And here’s Google Trends:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F366df26d-e420-431d-8034-e2c4a6a8de60_1149x471.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F366df26d-e420-431d-8034-e2c4a6a8de60_1149x471.png)

Semaglutide is now as searched-for on Google as Prozac or Viagra. Even if this is a temporary Musk-related spike, even pre-Musk it was getting a little above half their level. But Google Trends doesn’t exactly track awareness; few people search for Prozac these days precisely because everyone already knows what it is. So all this tells us is that there’s a lot of buzz around semaglutide.

Suppose for the sake of argument that 5% of obese people have heard of this drug.

 **Step 2: Prescription Accessibility**

The FDA says Wegovy is indicated for obesity, defined as BMI ≥ 30, or for people with BMI ≥ 27 and certain medical conditions. Does that mean that if you have that BMI, your doctor will give you a prescription? 

I think most doctors will want patients to try diet and exercise first. My experience as a doctor is that most obese people have already considered diet and exercise. Sometimes if you have a very compelling reason and a very well-thought out plan you can get them to try again. But usually they are obese because diet and exercise are hard for them, or don’t work for them, or some other reason besides “they never thought of it”.

Still, I hear lots of stories about patient-doctor fights here. I assume this will happen with Wegovy too. Every doctor will have their own threshold for what amount of “already tried diet and exercise” is enough to justify a Wegovy prescription, and sometimes patients won’t meet that threshold.

The history of medicine includes the following story many times: there’s some condition that doctors recommend lifestyle changes for. Then an exciting new medication comes out that treats the condition effectively. Over a generation or so, doctors go from demanding the lifestyle change, to gesturing at the lifestyle change before prescribing the medication, to mostly just prescribing the medication. We saw this with cholesterol and statins, with hypertension and ACE inhibitors, with depression and SSRIs. You can form your own opinion on whether this is good or bad, but we’re probably in the very beginning of this process with obesity. Opinions will be all over the map for a while before the inevitable pharma company victory makes everyone agree that semaglutide is first-line therapy.

…except that this time, Silicon Valley is short-circuiting the process with fly-by-night telemedicine companies that guarantee you’ll get the drugs you want. For example, [NextMed](https://www.joinnextmed.com/weight_loss) charges $138/month ($99 first month only!) for a guaranteed GLP-1 agonist prescription, plus “support and messaging with expert doctors”. The DEA sometimes shuts these groups down when they start playing around with controlled substances (eg addictive drugs like Adderall), but Wegovy isn’t controlled, and the government probably doesn’t care that much here. These services guarantee that people with money will be able to circumvent conservative doctors and access a prescription.

Only 75% of Americans have PCPs at all. If we assume half of them will eventually be able to get a Wegovy prescription from their doctor, that’s 37.5%.

 **Step 3: Affordability**

Semaglutide costs $15,000/year. Well-off people like Elon Musk might be able to pay that out-of-pocket, but most people will probably need insurance coverage. Right now this is spotty.

Medicare doesn’t cover obesity drugs. This isn’t a reaction to the threat of semaglutide-related cost explosions - they’re not that smart. I think Medicare laws were just written in the old days when people were less likely to think of obesity as a disease.

Is it time for change? Some Congressmen have proposed [a very noble-sounding law](https://www.obesityaction.org/troa/) telling Medicare and Medicaid to start covering weight loss drugs. I‘m sure this is out of deep compassion for America’s obese population and not because it would make pharma companies one billion zillion dollars.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1dbb9e98-6e07-4237-988e-3b7a61af3e5a_1381x834.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1dbb9e98-6e07-4237-988e-3b7a61af3e5a_1381x834.png)One of the Congressmen even has the last name “Kind!” Some pharma lobbyist probably got a bonus for that one.

Private insurers mostly have to cover whatever Medicare does, but they can choose whether or not to include extra non-Medicare-covered drugs. Some have chosen to cover semaglutide under some conditions. Others would prefer not to cover it, but can be scared into covering it by the magic words “medical necessity”. Overall I don’t understand the laws here beyond that maybe they’ll cover it and maybe they won’t.

Here, too, it might be time for change. The _New York Times_ [is publishing articles](https://www.nytimes.com/2022/05/31/health/obesity-drugs-insurance.html) trying to convince us that private insurances not covering semaglutide is an outrage.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0f24b293-27de-462a-84fd-bed2ba7cf07f_1723x831.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0f24b293-27de-462a-84fd-bed2ba7cf07f_1723x831.png)Here in the tiny gray text, I want to take a second to complain about this article. It notes that Wegovy (semaglutide for obesity) costs more per prescription than Ozempic (semaglutide for diabetes), and calls this “a gross inequity”, accusing Novo Nordisk of “charg[ing] people more for the same drug because of their obesity”. But the obesity prescription is higher dose than the diabetes prescription! Milligram per milligram, Wegovy costs *less* than Ozempic! A steelmanned version of the NYT might object - don’t most of the costs come from the intellectual property and not the manufacturing, so that dose shouldn’t matter? Yes, but if you made the obesity version cost too much less per milligram than the diabetes version, then diabetics would cheat the system by buying the obesity version and splitting it into smaller doses! 

Insurances that do cover it may require extra documentation that the patient has tried lots of diet and exercise, maybe including some official diet-and-exercise program like WeightWatchers. They might also want documentation that patients have tried cheaper earlier-generation weight loss drugs without success.

Even when insurances do cover semaglutide, copays may be very high. I have a pretty minimal insurance and it looks like if I got semaglutide my copay would be about $500/month until I reach my out of pocket limit. Harsh. People with better insurances might get hit less hard, but I don’t think anyone will be picking this up for cheap.

Let’s say only 5% of people who clear all previous hurdles can afford the drug.

 **How Many People Get Semaglutide?**

140 million obese Americans * 25% interested * 5% know of semaglutide’s existence * 37.5% can get prescriptions * 5% can afford it = 33,000, which is a pretty good match for the 50,000 estimated prescriptions. I didn’t even fudge the numbers to come out right, it just happened. 

## The Coming Decade

As a service to pharma investors, Morgan Stanley [modeled the economic future of obesity medications over the next decade](https://khn.org/wp-content/uploads/sites/2/2022/09/Morgan-Stanley_Unlocking-the-Obesity-Challenge.pdf). Their headline result: semaglutide and various semaglutide-copycat-drugs will be a $30 billion market by 2030. That’s less than the $500 billion disaster I was afraid of! But still almost 10% of all US drug spending!

Here are two core analyses from the report:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0906b28a-1ad4-421d-a055-87ed95db59ce_918x261.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0906b28a-1ad4-421d-a055-87ed95db59ce_918x261.png)

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb966f730-6b24-48e1-98b1-e710cda9264c_903x656.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb966f730-6b24-48e1-98b1-e710cda9264c_903x656.png)

The first analysis asks “what if doctors medicalized obesity as comprehensively as they’ve medicalized hypertension and high cholesterol?” That is: what if we put in a society-wide effort to get every obese person to a doctor, and after only a little diet and exercise, the doctor puts them on a medication? They find that the US obesity market would multiply by a factor of 25, to about $87 billion/year.

The second analysis is a more realistic projection for the next decade. Two things stand out. First, the number of patients on Wegovy or related medications goes from an estimated 46,910 now (pretty close to my 50,000 estimate!) to 11.3 million in 2030. Second, the cost per prescription goes from $15,000/year to about $4,000 year. Let’s look at this second change in more detail.

Right now semaglutide is literally in a class of its own for weight loss. But remember, it started as a GLP-1 agonist diabetes drug. And there are other GLP-1 agonists already in use for diabetes. Novo Nordisk’s competitor Eli Lilly owns a closely related molecule, tirzepatide (Mounjaro®). They’ve already done studies showing it _also_ works very well for weight loss - if anything even better than semaglutide - and they’re expected to get FDA approval to market it as a weight loss medication next year. Although capitalism fans might expect the presence of two competing drugs to immediately drive down prices, [this is mysteriously not how things work in health care](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6667132/) and prices will probably stay the same in the short term. But several other companies are working on semaglutide-like drugs, some will be cheaper to produce than semaglutide, and Morgan Stanley expects that this stronger level of competition will eventually drive costs down to $350/month ($4,000/year) by 2030. 

[![Male Mongoose/Appearances | The Lion Guard Wiki | Fandom](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc201f05a-7d1f-4738-911f-11d0d051adf9_2880x1562.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc201f05a-7d1f-4738-911f-11d0d051adf9_2880x1562.png)“Mounjaro” sounds like the playful animal sidekick in a Disney movie.

From a purely economic perspective, semaglutide costs the health system money (because it’s expensive) but also saves the health system money (because we don’t have to pay for obesity consequences like diabetes and heart attacks). Which effect wins out? According to the [Institute for Clinical and Economic Review](https://icer.org/wp-content/uploads/2022/03/ICER_Obesity_Evidence_Report_083122.pdf), benefits would outweigh costs if semaglutide cost less than about $8,000/year. Since it costs $15,000 year now, it’s not cost effective. But if Morgan Stanley’s model comes true and it costs $4,000/year in 2030, then it _will_ be cost effective. So at some point, Medicare (and so insurance companies) may start covering it more out of self-interest. I can’t tell whether the model takes this into account or not.

(there’s also a third-level effect where it costs the health system money again, because it prevents people from dying of obesity-related complications, and dead people stop needing expensive health care. I think health economists are supposed to ignore this level.)

11.3 million prescriptions at $4,000/year comes to $45 billion, but Morgan Stanley expects that not everyone will fill their prescriptions consistently or stay on the medication the same amount of time, leading to their $31 billion figure. 

### Towards The Glorious Post-Obesity Transhuman Future

The Morgan Stanley report shows that even the greediest pharma investors, openly plotting to medicalize obesity, can’t bring themselves to believe in more than 11 million US semaglutide patients by 2030. That’s less than 10% of the US obese population. 

Isn’t that kind of disappointing? We’ve got > 100 million people dealing with a condition that not only makes them unhealthy, but also causes them psychological distress, and makes lots of people low-grade disappointed in and repulsed by our society. And we’ve got an effective drug that treats the condition. And we’re going to use it on less than 10% of the people involved?

In 2032, semaglutide goes off-patent. It will probably take a few years to sort out legal issues and ramp up generic production, but by the mid-2030s, its price will go way down. I [don’t think there are technical barriers](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6708477/) to getting it down as low as $10 - $100 per month. By then, maybe there will be even more exciting branded weight loss drugs for wealthy people to choose from. But at the very least, semaglutide itself should become much more widely available even to poor or uninsured patients.

I’m not sure what will happen. Will there be an inflection point, where so many people use semaglutide that obesity becomes unusual again, and then the remaining obese people start using it just to fit in? Will obesity become an optional fashion statement, like shaving your head or getting a tattoo? Or will semaglutide end up disappointing us in some way, like so many promising drugs have before?

I come at semaglutide from a transhumanist perspective. I want to hack genetics and biology until everyone is as tall as they want, as strong as they want, as smart as they want, and whatever gender they want. If you want wings, you should be able to have wings. And yes, part of this vision is everyone having the weight they want. 

I’m not sure this _will_ happen, but for the first time I can see a clear path to how it _might_.

### Postscript 1: Should You Take Semaglutide?

I can’t answer this, please ask your doctor.

But I do want to add that there are potential side effects I haven’t mentioned in this post, including nausea, gastrointestinal problems, pancreatitis, and kidney problems. 

Semaglutide has been accused of slightly increasing risk of pancreatic and thyroid cancers. Studies have found trends in this direction, but these conditions are so rare that even over thousands of patients over many years, the increase hasn’t yet reached clear statistical significance. The current consensus position is that it may increase thyroid cancer by a tiny amount not relevant to most patients, and that it probably doesn’t increase pancreatic cancer. I think my father has looked over these data more and is less sure than other people about the lack of pancreatic cancer risk, but he can’t get the resources he needs to prove anything, and I can’t remember his exact argument.

More broadly: like all medications, semaglutide has benefits and risks, and you shouldn’t blindly take it after reading one blog article.

### Postscript 2: Is There A Way To Cheat The System To Get Semaglutide For Lower Cost?

Health care is much like airline tickets: everyone pays a different price for everything and there’s usually a secret way to get what you want for much less money. Is this true of semaglutide?

Pharma company Novo Nordisk [offers a Savings Card](https://www.wegovy.com/coverage-and-savings/wegovy-savings-and-support.html) that they say brings the price down to as low as $25 per month. I’m a little suspicious of this - pharma company offers are rarely as good as they sound - but I don’t notice any obvious tricks in this one and it should probably be your first bet.

[This startup](https://www.joincalibrate.com/faqs) claims that they can get insured people semaglutide for a $25/month copay “after their deductible is met” by negotiating with the insurance company very effectively. I can’t imagine how that works or what they have to negotiate with, but they seem pretty convinced, so I would welcome more information.

Otherwise, you don’t have many great options. Although there are two older forms of semaglutide not FDA-approved for weight loss - Ozempic and Rybelsus - these are both more expensive, milligram per milligram, than Wegovy itself. 

Canada is also of no help. The usual Canadian pharmacies don’t seem to carry Wegovy, and charge [about the same amount for Ozempic](https://www.buycanadianinsulin.com/product/ozempic/) as American pharmacies do.

[This article in Drug Discovery Trends](https://www.drugdiscoverytrends.com/semaglutide-supply-shortfall-fuels-demand-for-alternatives/) says that compounding pharmacies have been selling semaglutide for $300/month, less than a quarter of the sticker price. This is a bit confusing: compounding pharmacies are small local operations permitted to dispense unusual medications by mixing existing ones together in nonstandard ways. They’re arguing that they can legally dispense the semaglutide because they’re mixing it with vitamins, which, fine, but how are they getting it in the first place? [Everyone else seems as confused as I am](https://www.advisory.com/daily-briefing/2022/07/12/bootleg-semaglutide):

> "Nobody knows how [compounding pharmacies are] getting it," said Karl Nadolsky, an endocrinologist at **Spectrum Health**. "Who's making it? [The pharma company that makes it] Novo [Nordisk]'s not giving it to them. They're the ones with the rights to the molecule, so how is anybody getting semaglutide?"

Has nobody asked compounding pharmacists about this? Do they have a conspiracy of silence? Does the FDA sometimes send their goons in to extract the information, but the compounding pharmacists compound sleeping gas / smoke grenades and vanish into the night? Anyway, the usual authorities warn you not to take compounded semaglutide under any circumstances, but they’re the same people who tell you never to buy drugs from a Canadian pharmacy because they might be adulterated. You can decide how much you want to trust them.

### Postscript 3: What About Europe And The Rest Of The World?

Countries that are not the US usually negotiate with pharmaceutical companies over price. Because of some combination of “negotiation works” and “they are free-riding off Americans’ hard work”, they usually get much lower prices. What does semaglutide cost elsewhere?

This is hard to find out because government health agencies sometimes keep their prices secret, plus Wegovy mostly isn’t available in other countries yet. 

The only information I could find was from Britain, which is in the process of making Wegovy available to patients. It looks like [NHS will](https://www.thetimes.co.uk/article/hse-weighs-up-impact-of-obesity-drug-that-costs-250-a-month-x3x3cnlt6) “restrict the expensive drug’s availability to very obese people attending specialist weight-loss clinics”, but that it might be possible to get it from [private clinics](https://my-bmi.co.uk/wegovy-cost/) for £199/month = £2400/year.

Wegovy has been approved in the EU but doesn’t seem to have made it there yet. I can’t find any information about any other country. Non-weight-loss-indicated versions of semaglutide are available in many countries, but I wouldn’t expect their health care systems to be flexible about redirecting it for weight.

Canadian regulators have approved Wegovy, but it doesn’t seem to be available there yet. I haven’t seen any evidence that Ozempic costs less in Canada than it does in the US, and I’m not sure why. Maybe the pharma companies have figured out that anything that happens in Canada gets imported into the US, and they’re playing hardball this time. I don’t know whether Canadians will be able to get it for cheaper than Americans or not.

### Postscript 4: Predictions

(all predictions are conditional on no singularity or global catastrophe)

  1. 10 million Americans on semaglutide (or yet-to-be-approved equally good or superior alternatives) by 2030: **75%**

  2. Medicare covers semaglutide (or an alternative) in 2030: **40%**

  3. Semaglutide (or an alternative) costs less than $100/month in 2030: **25%**

  4. Semaglutide (or an alternative) costs less than $100/month (inflation-adjusted) without insurance in 2040: **66%**

  5. US obesity half or less of current rate in 2050: **30%**



