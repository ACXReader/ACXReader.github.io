---
title: "Ivermectin: Much More Than You Wanted To Know"
subtitle: "..."
date: 2021-11-17
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/43667275/comments?&all_comments=true
image: https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/f2bf1ed1-cac8-43ee-8c41-ce46d99884a5_990x470.png
original-url: https://www.astralcodexten.com/p/ivermectin-much-more-than-you-wanted
---
I know I’m two months late here. Everyone’s already made up their mind and moved on to other things.

But here’s my pitch: this is one of the most carefully-pored-over scientific issues of our time. Dozens of teams published studies saying ivermectin definitely worked. Then most scientists concluded it didn’t. What a great opportunity to exercise our study-analyzing muscles! To learn stuff about how science works which we can then apply to less well-traveled terrain! Sure, you read the articles saying that experts had concluded the studies were wrong. But did you really develop a gears-level understanding of what was going on? That’s what we have a chance to get here!

### The Devil’s Advocate

Any deep dive into ivermectin has to start here:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F462aa7ae-f0b8-4d47-a192-77cc37a7ef1b_912x657.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F462aa7ae-f0b8-4d47-a192-77cc37a7ef1b_912x657.png)

This is from [ivmmeta.com](https://ivmmeta.com/), part of a sprawling empire of big professional-looking sites promoting unorthodox coronavirus treatments. I have no idea who runs it - they’ve very reasonably kept their identity secret - but my hat is off to them. Each of these study names links to a discussion page which extracts key outcomes and offers links to html and pdf versions of the full text. These same people have another 35 ivermectin studies with different inclusion criteria, subanalyses by every variable under the sun, responses and counterresponses to everyone who disagrees with them about every study, _and_ they’ve done this for twenty-nine other controversial COVID treatments. Putting aside the question of accuracy and grading only on presentation and scale, this is the most impressive act of science communication I have ever seen. The WHO and CDC get billions of dollars in funding and neither of them has been able to communicate _their_ perspective anywhere near as effectively. Even an atheist can appreciate a cathedral, and even an ivermectin skeptic should be able to appreciate this website.

What stands out most in this image (their studies on early treatment only; there are more on other things) is all the green boxes on the left side of the table. A green box means that the ivermectin group did better than placebo (a red box means the opposite). This isn’t adjusted for statistical significance - indeed, many of these studies don’t reach it. The point of a meta-analysis is that things that aren’t statistically significant on their own can become so after you pool them with other things. If you see one green box, it could mean the ivermectin group just got a little luckier than the placebo group. When you see 26 boxes compared to only 4 red ones, you know that _nobody_ gets that lucky.

Acknowledging that this is interesting, let’s detract from it a little.

First, this presentation can exaggerate the effect size (represented by how far the green boxes are to the left of the gray line in the middle representing no effect). It focuses on the most dire outcome in every study - death if anybody died, hospitalization if anyone was hospitalized, etc. Most studies are small, and most COVID cases do fine, so most of these only have one or two people die or get hospitalized. So the score is often something like “ivermectin, 0 deaths; placebo, 1 death”, which is an infinitely large relative risk, and then the site rounds it down to some very high finite number. This methodology naturally produces very big apparent effects, and the rare studies where ivermectin does worse than placebo are equally exaggerated (one says that ivermectin patients are 600% more likely to end up hospitalized). 

But this doesn’t change the basic fact that ivermectin beats placebo in 26/30 of these studies.

Second, this presents a pretty different picture than you would get reading the studies themselves. Most of these studies are looking at outcomes like viral load, how long until the patient tests negative, how long until the patient’s symptoms go away, etc. Many of these results are statistically insignificant or of low effect size.

I went through these studies and tried to get some more information for my own reference:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4e9f8e07-6611-4797-b775-8c2e529ed69c_1453x511.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4e9f8e07-6611-4797-b775-8c2e529ed69c_1453x511.png)Click to expand. # is how many people were in the smallest relevant group (eg if there were 20 people in placebo and 10 in ivermectin, it was 10). Dose is ivermectin dose x number of days. Tested w/ is what drugs were given alongside ivermectin; compare is what drugs were in the “placebo” group (I excluded some very common things like paracetamol). %-PCR7 is what percent of patients had a negative PCR test (indicating recovery) after 7 days (though if 7 wasn’t available, I accepted anything from 6-12); the (I) and (P) are ivermectin and placebo groups. R is the ratio - green if statistically significant, red otherwise. DaysPCR is how many days it took to get a negative PCR test. Days to -sym are how many days it took symptoms to resolve. -outc is some serious negative outcome in the study, either clinical worsening, hospitalization, or death. I was inconsistent which one I chose, trying to pick whichever I thought struck a balance between high sample size and severity. Since this was almost never significant, I made it blue if it favored ivermectin and orange if it favored placebo (which it never did; there is no orange). Lowest p is the lowest p-value in the study for one of the headline results. 1o+ is whether the primary outcome was positive or not. I made this very quickly and unprincipledly and I am sure there are a lot of errors; please forgive me.

Of studies that included any of the endpoints I recorded, ivermectin had a statistically significant effect on the endpoint 13 times, and failed to reach significance 8 times. Of studies that named a specific primary endpoint, 9 found ivermectin affected it significantly, and 12 found it didn’t.

But that’s still pretty good. And “doesn’t affect to a statistically significant degree” doesn’t mean it doesn’t work. It might just mean your study is too small for a real and important effect to achieve statistical significance. That’s why people do meta-analyses to combine studies. And the ivmmeta people say they did that and it was really impressive. All of this is still basically what things would look like if ivermectin worked.

But of course we can’t give every study one vote. We’ve got to actually look at these and see which ones are good and which ones are bad. So, God help us, let’s go over all thirty of the ivermectin studies in this top panel of ivmmeta.com.

(if you get bored of this, scroll down to the section called “The Analysis”)

### The Studies

**[Elgazzar et al:](https://www.researchgate.net/publication/346876366_Efficacy_and_Safety_of_Ivermectin_for_Treatment_and_prophylaxis_of_COVID-19_Pandemic) **This one isn’t on the table above, but we can’t start talking about the others until we get it out of the way. 600 Egyptian patients were randomized into six groups, including three that got ivermectin. The ivermectin groups did substantially better: for example, 2 vs. 20 deaths in ivermectin group 3 vs. non-ivermectin group 4. There were various other equally impressive outcomes.

Unfortunately, it’s all false. Some epidemiologists and reporters were able to obtain the raw data (it was password-protected, but the password was “1234”), and it was pretty bizarre. Some patients appeared to have died before the trial started; others were arranged in groups of four such that it seemed like the authors had just copy-pasted the same four patients again and again. Probably either the study never happened, or at least the data were heavily edited afterwards. You can read more [here](https://gidmk.medium.com/is-ivermectin-for-covid-19-based-on-fraudulent-research-5cc079278602). A lot of the apparent benefit of ivermectin in meta-analyses disappeared after taking out this paper (though remember, this isn’t even on the table at the top of the post, so it doesn’t directly affect that).

Since the Elgazzar debacle, a group of researchers including Gideon Meyerowitz-Katz, Kyle Sheldrake, James Heathers, Nick Brown, Jack Lawrence, etc, have been trying to double-check as many other ivermectin studies as possible. At least three others - Samaha, Carvallo, and Niaee - have similar problems and have been retracted.

Those studies were all removed before I screenshotted the table above, and they’re not on there. But everybody is pretty paranoid right now and looking for fraud a lot harder than they might be in normal situations. Moving on:

**[Chowdury et al](https://ejmo.org/10.14744/ejmo.2021.16263/) :** Bangladeshi RCT. 60 patients in Group A got low-dose ivermectin plus the antibiotic doxycycline, 56 in Group B got hydroxychloroquine (another weird COVID treatment which most scientists think doesn’t work) plus the antibiotic azithromycin. No declared primary outcome. Ivermectin group got to negative PCR a little faster than the other (5.9 vs. 7 days) but it wasn’t statistically significant (p = 0.2). A couple of other non-statistically-significant things happened too. 2 controls were hospitalized, 0 ivermectin patients were. 

This is a boring study that got boring results, so nobody has felt the need to assassinate it, but if they did, it would probably focus on both groups getting various medications besides ivermectin. None of these other medications are believed to work, so I don’t really care about this, but you could tell a story where actually doxycycline works great at addressing associated bacterial pneumonias, or where HCQ causes lots of side effects and that makes the ivermectin group look good in comparison, or whatever.

**[Espitia-Hernandez et al:](https://www.biomedres.info/biomedical-research/effects-of-ivermectinazithromycincholecalciferol-combined-therapy-on-covid19-infected-patients-a-proof-of-concept-study-14435.html) **Mexican trial which is probably not an RCT - all it says is that “patients were voluntarily allocated”. 28 ended up taking a cocktail of low-dose ivermectin, vitamin D, and azithromycin; 7 were controls. On day ten, everyone (!) in the experimental group was PCR negative; everyone (!) in the control group was still positive. Also, symptoms in the experimental group lasted an average of three days; in the control group, more like 10. These results make ivermectin look amazingly super-good, probably better than any other drug for any other disease, except maybe stuff like vitamins for treatment of vitamin deficiency.

Any issues? We don’t know how patients were allocated, but they discuss patient characteristics and they don’t look different enough to produce this big an effect size. The experimental group got a lot of things other than ivermectin, but I would be equally surprised if vitamin D or azithromycin cured COVID this effectively. It [deviated from its preregistration](https://clinicaltrials.gov/ct2/show/NCT04399746) in basically every way possible, but you shouldn’t be able to get “every experimental patient tested negative when zero control patients did” by garden-of-forking-paths alone! 

But this has to be false, right? Even the other pro-ivermectin studies don’t show effects nearly this big. In all other studies combined, ivermectin patients took an average of 8 days to recover; in Espitia-Hernandez, they took 3. Also, it’s pretty weird that the entire control group had positive PCRs on day 10 - in most other studies, a majority of people had negative PCRs by day 7 or so, regardless of whether they were control or placebo. Everything about this is so shoddy that I can easily believe something went wrong here.

I don’t have a great understanding of this one but I don’t trust it at all. Luckily it is small and non-randomized so it will be easy to ignore going forward.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fda0f378f-c7e9-446c-909b-b870b062fd39_589x444.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fda0f378f-c7e9-446c-909b-b870b062fd39_589x444.png)I’m not saying this is related, but I’m not saying it *isn’t* related either.

**[Carvallo et al:](https://www.longdom.org/open-access/safety-and-efficacy-of-the-combined-use-of-ivermectin-dexamethasone-enoxaparin-and-aspirina-against-covid19-the-idea-protocol-70290.html) **This one has all the disadvantages of Espitia-Hernandez, plus it’s completely unreadable. It’s hard to figure out how many patients there were, whether it was an RCT or not, etc. It looks like maybe there were 42 experimentals and 14 controls, and the controls were about 10x more likely to die than the experimentals. Seems pretty bad.

On the other hand, [another Carvallo paper was retracted](https://www.buzzfeednews.com/article/stephaniemlee/ivermectin-covid-study-suspect-data) because of fraud: apparently the hospital where the study supposedly took place said it never happened there. I can’t tell if this is a different version of that study, a pilot study for that study, or a different study by the same guy. Anyway, it’s too confusing to interpret, shows implausible results, and is by a known fraudster, so I feel okay about ignoring this one.

**[Mahmud et al:](https://journals.sagepub.com/doi/10.1177/03000605211013550) **RCT from Bangladesh. 200 patients received ivermectin plus doxycycline, 200 received placebo. Everything was written up very nicely in real English, by people who were clearly not on 34 lbs of meth at the time. They designated a primary outcome, “number of days required for clinical recovery”, and found a statistically significant difference at p < 0.001:

[![
                        figure
                    ](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1ff4783b-1473-4413-9230-8b15a5549208_500x469.gif)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1ff4783b-1473-4413-9230-8b15a5549208_500x469.gif)Okay, fine, they misspelled “recovery” once. But they spelled it right the other time! That puts it in the top 50% for ivermectin papers!

The fraud-hunters have examined this paper closely and are unable to find any signs of fraud.

[![Twitter avatar for @K_Sheldrick](https://substackcdn.com/image/twitter_name/w_96/K_Sheldrick.jpg)Kyle Sheldrick @K_SheldrickI have made a second comment on @PubPeer on the Mahmud trial of ivermectin in covid patients. I have now reviewed the individual patient data master sheet. I did not find any irregularities and the summary data matches the published data. ](https://twitter.com/K_Sheldrick/status/1416353592773017602)[pubpeer.comPubPeer - Ivermectin in combination with doxycycline for treating COVI...There are comments on PubPeer for publication: Ivermectin in combination with doxycycline for treating COVID-19 symptoms: a randomized trial (2021)](https://pubpeer.com/publications/E1D65711EF28D14517731BEACB89C8#2)[11:06 AM ∙ Jul 17, 2021

* * *

12Likes2Retweets](https://twitter.com/K_Sheldrick/status/1416353592773017602)

[![Twitter avatar for @GidMK](https://substackcdn.com/image/twitter_name/w_96/GidMK.jpg)Health Nerd @GidMK8/n Let's compare to another paper - Mahmud (2020) is a study that everyone would agree is at low risk of bias. It is just incredibly well done Also, it found a benefit for ivermectin ](https://twitter.com/GidMK/status/1412635825771192320)[![](https://substackcdn.com/image/fetch/w_600,h_314,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff828d9f9-cc58-441c-b4ca-f4a2cffb40e0_600x314.jpeg)journals.sagepub.comSAGE Journals: Your gateway to world-class research journalsSubscription and open access journals from SAGE Publishing, the world’s leading independent academic publisher.](https://journals.sagepub.com/doi/10.1177/03000605211013550?url_ver=Z39.88-2003&rfr_id=ori:rid:crossref.org&rfr_dat=cr_pub%20%200pubmed)[4:53 AM ∙ Jul 7, 2021

* * *

53Likes7Retweets](https://twitter.com/GidMK/status/1412635825771192320)

I think this paper is legitimate and that its findings need to be seriously considered. Serious consideration doesn’t always meant they’re true - sometimes if we have strong evidence otherwise we can dismiss things without understanding why. And there’s always the chance it was a fluke, right? Can something have a p-value less than 0.001 and still be a fluke? 

**[Szenta Fonseca et al:](https://www.sciencedirect.com/science/article/pii/S1477893920304026) **This is a chart review from Brazil. Researchers looked at various people who had been treated for COVID in an insurance company database, saw whether they got ivermectin or not, and saw whether the people who got it did better or worse. About a hundred people got it, and a few hundred others didn’t. The people who got it did not do any better than anyone else, and you’ll notice this is one of the rare red boxes on the table above.

But we shouldn’t take this study seriously. Nobody took any effort to avoid selection bias, so it’s very possible that sicker people were given more medication (including ivermectin), which unfairly handicaps the ivermectin group. Also, it’s hard to tell from the paper who was on how much of what, and the discussion of ivermectin seems like kind of an afterthought after discussing lots of other meds in much more depth. This is another one I feel comfortable ignoring.

**[Cadegiani et al:](https://www.sciencedirect.com/science/article/pii/S2052297521000792) **A crazy person decided to put his patients on every weird medication he could think of, and 585 subjects ended up on a combination of ivermectin, hydroxychloroquine, azithromycin, and nitazoxanide, with dutasteride and spironolactone "optionally offered" and vitamin D, vitamin C, zinc, apixaban, rivaraxoban, enoxaparin, and glucocorticoids "added according to clinical judgment". There was no control group, but the author helpfully designated some random patients in his area as a sort-of-control, and then synthetically generated a second control group based on “a precise estimative based on a thorough and structured review of articles indexed in PubMed and MEDLINE and statements by official government agencies and specific medical societies”.

Patients in the experimental group were twice as likely to recover (p < 0.0001), had negative PCR after 14 vs. 21 days, and had 0 vs. 27 hospitalizations. 

Speaking of low p-values, some people did fraud-detection tests on another of Cadegiani’s COVID-19 studies and got values like p < 8.24E-11 in favor of it being fraudulent. 

And, uh, he’s also studied whether ultra-high-dose antiandrogens treated COVID, and found that they did, cutting mortality by 92% . But the trial is under suspicion, with [a BMJ article](https://www.bmj.com/content/375/bmj.n2819) calling it “[the worst] violations of medical ethics and human rights in Brazil’s history” and “an ethical cesspit of violations”.

[update 2022: this section originally contained more accusations against Cadegiani. Alexandros Marinos does [a deeper dive](https://doyourownresearch.substack.com/p/the-misportrayal-of-dr-flavio-cadegiani?s=r) with information not available at the time I wrote this, and finds some of them were overstated or false by implication]

Anyway, let’s not base anything important on the results of this study, mmkay?

[![flavi-1](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7fe429e5-dba6-4b59-b46f-a2345b6acaf4_1080x720.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7fe429e5-dba6-4b59-b46f-a2345b6acaf4_1080x720.jpeg)A defiant Flavio Cadegiani. Imagine a guy who looks like this telling you to take ultra-high-dose antiandrogens.

**[Ahmed et al:](https://www.sciencedirect.com/science/article/pii/S1201971220325066)** And we’re back in Bangladesh. 72 hospital patients were randomized to one of three arms: ivermectin only, ivermectin + doxycycline, and placebo. Primary endpoint was time to negative PCR, which was 9.7 days for ivermectin only and 12.7 days for placebo (p = 0.03). Other endpoints including duration of hospitalization (9.6 days ivermectin vs. 9.7 days placebo, not significant). This looks pretty good for ivermectin and does not have any signs of fraud or methodological problems.

If I wanted to pick at it anyway, I would point out that the ivermectin + doxycycline group didn’t really differ from placebo, and that if you average out both ivermectin groups (with and without doxycycline) it looks like the difference would not be significant. I had previously committed to considering only ivermectin alone in trials that had multiple ivermectin groups, so I’m not going to do this. I can’t find any evidence this trial was preregistered so I don’t know whether they waited to see what would come out positive and then made that their primary endpoint, but virological clearance is a pretty normal primary endpoint and this isn’t that suspicious. 

It’s impossible to find any useful commentary on this study because Elgazzar (the guy who ran the most famous fraudulent ivermectin study) had the first name Ahmed, everyone is talking about Elgazzar all the time, and this overwhelms Google whenever I try to search for Ahmed et al.

For now I’ll just keep this as a mildly positive and mildly plausible virological clearance result, in the context of no effect on hospitalization length or most symptoms. 

**[Chaccour et al:](https://www.thelancet.com/journals/eclinm/article/PIIS2589-5370\(20\)30464-8/fulltext) **24 patients in Spain were randomized to receive either medium-dose ivermectin or placebo. The primary outcome was percent of patients with negative PCR at day 7; secondary outcomes were viral load and symptoms. The primary endpoint ended up being kind of a wash - everyone still PCR positive by day 7 so it was impossible to compare groups. Ivermectin trended toward lower viral load but never reached significance. Weirdly, ivermectin _did_ seem to help symptoms, but only anosmia and cough towards the end (p = 0.03), which you would usually think of as lingering post-COVID problems. The paper says:

> Given these findings, consideration could be given to alternative mechanisms of action different from a direct antiviral effect. One alternative explanation might be a positive allosteric modulation of the nicotinic acetylcholine receptor caused by ivermectin and leading to a downregulation of the ACE-2 receptor and viral entry into the cells of the respiratory epithelium and olfactory bulb. Another mechanism through which ivermectin might influence the reversal of anosmia is by inhibiting the activation of pro-inflammatory pathways in the olfactory epithelium. Inflammation of the olfactory mucosa is thought to play a key role in the development of anosmia in SARS-CoV-2 infection

This seems kind of hedge-y. If you’re wondering where things went from there, Dr. Chaccour is now a passionate anti-ivermectin activist:

[![Twitter avatar for @carlos_chaccour](https://substackcdn.com/image/twitter_name/w_96/carlos_chaccour.jpg)Dr. Carlos Chaccour 🦟🔚💊 @carlos_chaccourVery thorough work by @Finneganporter in @BusinessInsider The roots of #ivermectin mania: How South America incubated a fake-medicine craze that took the US by storm ](https://twitter.com/carlos_chaccour/status/1457417685210390528)[![](https://substackcdn.com/image/fetch/w_600,h_314,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F88d08e70-c9e2-46d4-a5df-96807b6c3a13_2000x1000.jpeg)businessinsider.inThe roots of ivermectin mania: How South America incubated a fake-medicine craze that took the US by stormThe popularity of unproven anti-parasitic drug ivermectin as a COVID-19 treatment is surging. Its use has roots in South America, where it was hyped by populist](https://www.businessinsider.in/international/news/the-roots-of-ivermectin-mania-how-south-america-incubated-a-fake-medicine-craze-that-took-the-us-by-storm/articleshow/87554081.cms)[6:40 PM ∙ Nov 7, 2021

* * *

9Likes2Retweets](https://twitter.com/carlos_chaccour/status/1457417685210390528)

[![Twitter avatar for @carlos_chaccour](https://substackcdn.com/image/twitter_name/w_96/carlos_chaccour.jpg)Dr. Carlos Chaccour 🦟🔚💊 @carlos_chaccourLong-term consequences (***to poor, rural people in developing countries***) of the misuse of ivermectin data. The old story of actions having consequences that stretch beyond the perpetrators. ](https://twitter.com/carlos_chaccour/status/1450371233971900419)[thelancet.comDEFINE_ME](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099\(21\)00630-7/fulltext)[8:00 AM ∙ Oct 19, 2021

* * *

7Likes3Retweets](https://twitter.com/carlos_chaccour/status/1450371233971900419)

So I guess he must think of this trial as basically negative, although realistically it’s 24 people and we shouldn’t put too much weight on it either way.

**[Ghauri et al:](https://ijclinmedcasereports.com/pdf/IJCMCR-RA-00320.pdf) **Pakistan, 95 patients. Nonrandom; the study compared patients who happened to be given ivermectin (along with hydroxychloroquine and azithromycin) vs. patients who were just given the latter two drugs. There’s some evidence this produced systematic differences between the two groups - for example, patients in the control group were 3x more likely to have had diarrhea (this makes sense; diarrhea is a potential ivermectin side effect, so you probably wouldn’t give it to people already struggling with this problem). Also, the control group was twice as likely to be getting corticosteroids, maybe a marker for illness severity. Primary outcome was what percent of both groups had a fever: on day 7 it was 21% of ivermectin patients vs. 65% of controls, p < 0.001. No other outcomes were reported.

I don’t _hate_ this study, but I think the nonrandom assignment (and observed systematic differences) is a pretty fatal flaw. 

I can’t find anyone else talking about this one. At least no one seems to be saying anything bad.

**[Babaloba et al:](https://academic.oup.com/qjmed/advance-article/doi/10.1093/qjmed/hcab035/6143037) **Be warned: if I have to refer to this one in real-life conversation, I will expand out the “et al” and call it “Babalola & Alakoloko”, because that’s really fun to say. This was a Nigerian RCT comparing 21 patients on low-dose ivermectin, 21 patients on high-dose ivermectin, and 20 patients on a combination of lopinavir and ritonavir, a combination antiviral which later studies found not to work for COVID and which might as well be considered a placebo. Primary outcome, as usual, was days until a negative PCR test. High dose ivermectin was 4.65 days, low dose was 6 days, control was 9.15, p = 0.035. 

[![2-way repeat measures of analysis of variance \(RAMOVA\) SARS CoV-2 PCR ASSAY X axis: 1=84hrs, 2=168hrs, 3= 252hrs, 4=336hrs.](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0238280a-236e-47f5-9db6-7c35c07c5fc2_520x393.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0238280a-236e-47f5-9db6-7c35c07c5fc2_520x393.jpeg)Figure 2 is apparently a photograph of the computer screen where they did this calculation.

Gideon Meyerowitz-Katz, part of the team that detects fraud in ivermectin papers, is not a fan of this one:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5271fbd-b82a-4e34-9787-8b3aa6e8d2f6_595x522.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5271fbd-b82a-4e34-9787-8b3aa6e8d2f6_595x522.png)

He doesn’t say there what means, but elsewhere he tweets this figure:

[![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9be5d50-858b-4c3a-bef7-a312df762eda_638x549.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9be5d50-858b-4c3a-bef7-a312df762eda_638x549.png)It’s always a bad sign when your study features in an image with “NUMEROUS IMPOSSIBLE NUMBERS” in red at the top.

I think his point is that if you have 21 people, it’s impossible to have 50% of them have headache, because that would be 10.5. If 10 people have a headache, it would be 47.6%; if 11, 52%. So something is clearly wrong here. Seems like a relatively minor mistake, and Meyerowitz-Katz stops short of calling fraud, but it’s not a good look.

I’m going to be slightly uncomfortable with this study without rejecting it entirely, and move on.

**[Ravakirti et al:](https://journals.library.ualberta.ca/jpps/index.php/JPPS/article/view/32105) **Here we’re in Eastern India - not exactly Bangladesh again, but a stone’s throw away from it. In this RCT patients were randomized into an ivermectin group (57) and a placebo group (58). Primary outcome was negative PCR on day 6, because doing it on day 7 like everyone else would be too easy. As with several other groups, this was a bad move; too few people had it to make a good comparison; it was 13% of intervention vs. 18% of placebo, p = 0.3. Secondary outcomes were also pretty boring, except for the most important: 4 people in the placebo group died, compared to 0 in ivermectin (p = 0.045). 

On the one hand, this is one outcome of many, reaching the barest significance threshold. Another fluke? Still, there are no real problems with this study, and nobody has anything to say against it. Let’s add this one to the scale as another very small and noisy piece of real evidence in ivermectin’s favor.

**[Bukhari et al:](https://www.medrxiv.org/content/10.1101/2021.02.02.21250840v1) **Now we’re in Pakistan. 50 patients were randomized to low-dose ivermectin, another 50 got standard of care including vitamin D. There was no placebo, but primary outcome was number of days to reach negative PCR, which it seems hard for placebo to affect much, so I don’t care. 5 controls and 9 ivermectin patients left the hospital against medical advice and could not be followed up, which is bad but not necessarily study-ruining. They never measured their supposed primary outcome of “days to reach negative PCR” directly, but they did measure how many people had negative PCR on various days, and ivermectin had a clear advantage - for example, on day 7, it was 37/50 for IVR and only 20/50 for control. Even if we assume all the lost-to-followup patients had maximally bad-for-the-hypothesis results, that’s still a positive finding.

Nobody else has much to say about this one, certainly no accusations that they’ve found anything suspicious. Keep.

**[Mohan et al:](https://www.sciencedirect.com/science/article/pii/S1341321X21002397) **India. RCT. 40 patients got low-dose ivermectin, 40 high-dose ivermectin, and 45 placebo. Primary outcomes were time to negative PCR, and viral load on day 5. In the results, they seem to have reinterpreted “time to negative PCR” as the subtly different “percent with negative PCR on some specific day”. High-dose ivermectin did best (47.5% negative on day 5) and placebo worst (31% negative), but it was insignificant (p = 0.3). There was no difference in viral load. All groups took about the same amount of time for symptoms to resolve. More placebo patients had failed to recover by the end of the study (6) than ivermectin patients (2), but this didn’t reach statistical significance (p = 0.4).

Overall a well-done, boring, negative study, although ivermectin proponents will correctly point out that, like basically every other study we have looked at, the trend was in favor of ivermectin and this could potentially end up looking impressive in a meta-analysis.

**[Biber et al:](https://c19ivermectin.com/biber.html) **This is an RCT from Israel. 47 patients got ivermectin and 42 placebo. Primary endpoint was viral load on day 6. I am having trouble finding out what happened with this; as far as I can tell it was a negative result and they buried it in favor of more interesting things. In a "multivariable logistic regression model, the adjusted odds ratio of negative SARS-CoV-2 RT-PCR negative test" favored ivermectin over placebo (p = 0.03 for day 6, p = 0.01 for day 8), but this seems like the kind of thing you do when your primary outcome is boring and you’re angry.

Gideon Meyerowitz-Katz is not a fan:

[![Twitter avatar for @GidMK](https://substackcdn.com/image/twitter_name/w_96/GidMK.jpg)Health Nerd @GidMKThis study is a common citation of ivermectin believers, has been reported widely, and I think is a great teaching tool in how little effort it takes to be critical about research findings 1/n ![Image](https://substackcdn.com/image/fetch/w_600,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FE-qTSjBUUAEG0Wa.png)![Image](https://substackcdn.com/image/fetch/w_600,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FE-qTU6HVkAMvZav.jpg)](https://twitter.com/GidMK/status/1435128867027501056)[6:32 AM ∙ Sep 7, 2021

* * *

882Likes276Retweets](https://twitter.com/GidMK/status/1435128867027501056)

He notes that the study excluded people with high viral load, but [the preregistration](https://clinicaltrials.gov/ct2/show/NCT04429711?term=NCT04429711&draw=2&rank=1) didn’t say they would do that. Looking more closely, he finds they did that because, if you included these people, the study got no positive results. So probably they did the study, found no positive results, re-ran it with various subsets of patients until they did get a positive result, and then claimed to have “excluded” patients who weren’t in the subset that worked.

I’m going to toss this one.

**[Elalfy et al:](https://onlinelibrary.wiley.com/doi/10.1002/jmv.26880) **What even is this? Where am I? 

As best I can tell, this is some kind of Egyptian trial. It might or might not be an RCT; it says stuff like “Patients were self-allocated to the treatment groups; the first 3 days of the week for the intervention arm while the other 3 days for symptomatic treatment”. Were they self-allocated in the sense that they got to choose? Doesn’t that mean it’s not random? Aren’t there seven days in a week? These are among the many questions that Elalfy et al do not answer for us.

The control group (which they seem to think can also be called “the white group”) took zinc, paracetamol, and maybe azithromycin. The intervention group took zinc, nitazoxanide, ribavirin, and ivermectin. There were very large demographic differences between the groups of the sort which make the study unusable, which they mention and then ignore. From there, they follow this normal and totally comprehensible flowchart:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4d3559ee-a058-44cc-9b38-09b78a0f5035_1352x1070.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4d3559ee-a058-44cc-9b38-09b78a0f5035_1352x1070.png)

There is no primary outcome assigned, but viral clearance rates on day seven were 58% in the yellow group compared to 0% in the white group, which I guess is a strong positive result.

This table…

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbffceed7-c84a-45c1-abfe-1fb2706dc383_483x674.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbffceed7-c84a-45c1-abfe-1fb2706dc383_483x674.png)

…looks very impressive, in terms of the experimental group doing better than the control, except that they don’t specify whether it was _before_ the trial or _after_ it, and at least one online commentator thinks it might have been before, in which case it’s only impressive how thoroughly they failed to randomize their groups.

Overall I don’t feel bad throwing this study out. I hope it one day succeeds in returning to its home planet.

**[Lopez-Medina et al:](https://jamanetwork.com/journals/jama/fullarticle/2777389) **Colombian RCT. 200 patients took ivermectin, another 200 took placebo. They originally worried the placebo might taste different than real ivermectin, then solved this by replacing it with a different placebo, which is a pretty high level of conscientiousness. Primary outcome was originally percent of patients whose symptoms worsened by two points, as rated on a complicated symptom scale when a researcher asked them over the phone. Halfway through the study, they realized nobody was worsening that much, so they changed the primary outcome to time until symptoms got better, as measured by the scale.

In the ivermectin group, symptoms improved that much after 10 days; in the placebo group, after 12, p = 0.53. By the end of the study, symptoms had improved in 82% of ivermectin users and 79% of controls, also insignificant. 4 patients in the ivermectin group needed to be hospitalized compared to 6 in the placebo group, again insignificant.

This study is bigger than most of the other RCTs, and more polished in terms of how many spelling errors, photographs of computer screens, etc, it contains. It was published in _JAMA_ , one of the most prestigious US medical journals, as opposed to the crappy nth-tier journals most of the others have been in. When people say things like “sure, a lot of small studies show good results for ivermectin, but the bigger and more professional trials don’t”, this is one of the two big professional trials they’re talking about.

Ivermectin proponents make some good arguments against it. In order to get as big as it did, Lopez-Medina had to compromise on rigor. Its outcome is how people self-score their symptoms on a hokey scale in a phone interview, instead of viral load or PCR results or anything like that. Still, this is basically what we want, right? In the end, we want people to feel better and less sick, not to get good scores on PCR tests. 

Also, it changed its primary outcome halfway through; isn’t that bad? I think _maybe_ not; the reason we want a preregistered primary outcome is so that you don’t change halfway through to whatever outcome shows the results you want. The researchers in this study did a good job explaining why they changed their outcome, the change makes sense, and their original outcome would also have shown ivermectin not working (albeit less accurately and effectively). I don’t know of any evidence that they knew (or suspected) final results when switching to this new outcome, and it seems like the most reasonable new outcome to switch to.

Finally, their original placebo tasted different from ivermectin (though they switched halfway through). This is one of the few studies where I actually care about placebo, because people are self-rating their symptoms. But realistically most of these people don’t know what ivermectin is supposed to taste like. Also, they did a re-analysis and found there was no difference between the people who got the old placebo and the new one.

I’m making a big deal of this because ivmmeta.com - the really impressive meta-analysis site I’ve been going off of - puts a special warning letter underneath their discussion of this study, urging us not to trust it. They don’t do this for any of the other ones we’ve addressed so far - not the one by the guy whose other studies were all frauds, not the one where 50% of 21 people had headaches, not the unrandomized one where the groups were completely different before the experiment started, not even the one by the guy accused of crimes against humanity. Only this one. This makes me a lot less charitable to ivmmeta than I would otherwise be; I think it’s hard to choose this particular warning letter strategy out of well-intentioned commitment to truth. They just really don’t like this big study that shows ivermectin doesn’t work.

Also, the warning itself irritates me, and includes paragraphs like:

> RCTs have a fundamental bias against finding an effect for interventions that are widely available — patients that believe they need treatment are more likely to decline participation and take the intervention [Yeh], i.e., RCTs are more likely to enroll low-risk participants that do not need treatment to recover (this does not apply to the typical pharmaceutical trial of a new drug that is otherwise unavailable). This trial was run in a community where ivermectin was available OTC and very widely known and used.

Nobody else worries about this, and there are a million biases that non-randomized studies have that would be super-relevant when discussing those, but somehow when they’re pro-ivermectin the site forgets to be this thorough.

I think a better pro-ivermectin response to this study is to point out that all the trends support ivermectin. Symptoms took 10 days to resolve in the ivermectin group vs. 12 in placebo; 4 ivermectin patients were hospitalized vs. 6 placebo patients, etc. Just say that this was an unusually noisy trial because of the self-report methodology, and you’re confident that these small differences will add up to significance when you put them into a meta-analysis.

**[Roy et al:](https://www.medrxiv.org/content/10.1101/2021.03.08.21252883v1) **We’re back in East India, and back to non-randomized trials. 56 patients were retrospectively examined; some had been given ivermectin + doxycycline, others hydroxychloroquine, other azithromycin, and others symptomatic treatment only. We don’t get any meaningful information about how this worked, but we are told that they did not differ in “clinical well-being reporting onset timing”. Whatever.

**[Chahla et al:](https://www.researchsquare.com/article/rs-495945/v1) **The first of many Argentine trials. 110 patients received medium-dose ivermectin; 144 were kept as a control (no placebo). This was “cluster randomized”, which means they randomize different health centers to either give the experimental drug or not. This is worse than regular randomization, because there could be differences between these health centers (eg one might have better doctors who otherwise give better treatment, one might be in the poor part of town and have sicker patients, etc). They checked to see if there were any differences between the groups, and it sure looks like there were (the experimental group had twice as many obese people as the controls), but as per them, these differences were not statistically significant. Note that if this did make a difference, it would presumably make ivermectin look worse, not better.

The primary outcome was given as “increase discharge from outpatient care with COVID-19 mild disease”. This favored the treatment; only 2/110 patients in the ivermectin group failed to be discharged, compared to 20 patients in the control group. 

But, uh, these were at different medical centers. Can’t different medical centers just have different discharge policies? One discharges you as soon as you seem to be getting better, the other waits to really make sure? This is an utterly crap endpoint to do a cluster randomized controlled trial on. If you’re going to do cRCT, which is never a _great_ idea, you should be using some extremely objective endpoint that doctors and clinic administrators can’t possibly affect, like viral load according to some third-party laboratory, using the same third-party laboratory for both clinics. 

This is such a bad idea that I can’t help worrying I’m missing or misunderstanding something. If not, this is dumb and bad and should be ignored.

**[Mourya et al:](https://ijhcr.com/index.php/ijhcr/article/view/1263) **We’re back in India. This is a nonrandomized study comparing 50 patients given ivermectin to 50 patients given hydroxychloroquine. No primary outcome was named, but they focus on PCR negativity. Only 6% of patients in the hydroxychloroquine group were negative, compared to 90% of patients in the ivermectin group! 

On what day did they do the test? Uh, kind of random, and they admit that “in [the hydroxychloroquine group], mean time difference from the date of initiation of treatment and second test was significantly longer (7.24±2.75 days) as compared to 5.22±1.21 days in [the ivermectin group] (p=0.021).” Since they assessed these groups at different times, we shouldn’t draw any conclusions from them getting different results. _Except_ that as far as I can tell this should _handicap_ ivermectin, making it especially impressive that it did better.

But also, the ivermectin group was made mostly of people who had been asymptomatic at the beginning (70%), and the hydroxychloroquine group had almost no asymptomatic cases (8%) . They were giving the ivermectin to healthy people and the hydroxychloroquine to sick people! They admit deep in the discussion that this “may be a confounding factor”.

So basically they got totally different groups of people, tested them at totally different times, and the two sets of test results differed. So what? So this is why normal people do RCTs instead of whatever the heck this is, that’s what.

**[Loue et al:](https://www.clinmedjournals.org/articles/jide/journal-of-infectious-diseases-and-epidemiology-jide-7-202.php?jid=jide) **…this one isn’t going to be an RCT either. Loue tells a story about a cluster of COVID cases at the French nursing home where he works. He asked people if they wanted to try ivermectin; 10 did and 15 didn’t. 1 ivermectin patient died, compared to 5 non-ivermectin patients. 

The non-ivermectin group looked a bit sicker than the ivermectin group in the inevitable [Table 1](https://www.clinmedjournals.org/articles/jide/jide-7-202-table1.html), though it’s hard to tell. One interesting possible confounder (not mentioned, but I’m imagining it) is that demented patients probably couldn’t consent to ivermectin and ended up in the control group. This is another case of “I’m not going to trust anything that isn’t an RCT”. 

**[Merino et al:](https://osf.io/preprints/socarxiv/r93g4/) **Another (sigh) non-RCT. Mexico City tried a public health program where if you called a hotline and said you had COVID, they sent you an emergency kit with various useful supplies. One of those supplies was ivermectin tablets. 18,074 people got the kit (and presumably some appreciable fraction took the ivermectin, though there’s no way to prove that). Their control group is people from before they started giving out the kits, people from after they stopped giving out the kits, and people who didn’t want the kits. 

There are differences in who got COVID early in the epidemic vs. later, and in people who did opt for medical kits vs. didn’t. To correct these, the researchers tried to adjust for confounders, something which - as I keep trying to hammer home again and again - [never works](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0152719).

They found that using the kit led to a 75% or so reduction in hospitalization, though they were unable to separate out the ivermectin from the other things in the kit (paracetamol and aspirin), or from the placebo effect of having a kit and feeling like you had already gotten some treatment (if I understand right, the decision to go to the hospital was left entirely to the patient).

I think this study is a moderate point in favor of giving people kits in order to prevent hospital overcrowding, but I’m not willing to accept that it tells us much about ivermectin in particular.

**[Faisal et al:](http://theprofesional.com/index.php/tpmj/article/view/5867/4523) **This one was published in _The Professional Medical Journal_ (mispelled as “Profesional Medical Journal” in its URL), so you know it’s going to be good!

It describes itself as “a cross-sectional study”, but later says it “randomized patients into two groups”, which would make it an RCT - I think they might just be using the term “cross-sectional” different from the standard American usage. A hospital in Pakistan got 50 patients on ivermectin + azithromycin, and another 50 on azithromycin alone. Primary outcome was not mentioned, and the data were presented confusingly, but a typical result is that only 4% of the ivermectin group had symptoms lasting more than 10 days, whereas 16% of the control group did, p < 0.01.

They do a really weird thing where they compare how long it took symptoms to resolve between IVM and control groups _within each bin._ That is, if I’m understanding correctly, they ask “of the people who took between 3-5 days for symptoms to resolve, did they resolve faster for IVM or control?”. This is an utterly bizarre analysis to perform, although it doesn’t affect the fact that their other results still seem to favor ivermectin. Maybe I’m confused about what’s going on here.

I’ve mostly been letting people off easy on no placebo, but I as far as I can tell (not very far) this paper seems to be going off whether patients reported continuing to have symptoms to the hospital doing the study, and I think that _is_ potentially susceptible to placebo effects. Additionally, there’s no preregistration, and even though they talk a lot about doing PCR tests they don’t present the results.

This is by no means the worst study here but I still think it’s pretty low quality and I don’t trust it.

**[Aref et al:](https://www.dovepress.com/clinical-biochemical-and-molecular-evaluations-of-ivermectin-mucoadhes-peer-reviewed-fulltext-article-IJN) **This one is published in the _International Journal Of Nanomedicine_ , even though I’m pretty sure that isn’t a real thing. In this case the “nanomedicine” is a new nasal spray version of ivermectin which is so confusing I cannot for the life of me figure out what dose they are giving these patients.

This Egyptian study gives 57 patients intranasal ivermectin plus hydroxychloroquine, azithromycin, oseltamavir, and some vitamins; another 57 patients get all that stuff except the ivermectin. Primary outcome is not stated, but they look at various symptoms, all of which look better in the ivermectin group:

[![https://www.dovepress.com/cr_data/article_fulltext/s313000/313093/img/IJN_A_313093_t0003.jpg](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6de79b6-091b-4c13-b7be-715c9bb194a7_986x810.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6de79b6-091b-4c13-b7be-715c9bb194a7_986x810.jpeg)

95% of ivermectin patients got negative PCRs at some time point, compared to 75% of controls, p = 0.004. 

I am pretty suspicious of this study, not least because it comes from Egypt which has an _awful_ reputation for fake studies, and it returns extreme results that I wouldn’t expect even if ivermectin was actually a wonder drug. But I cannot find any particular thing wrong with it, nor did anyone else I looked at, so I will grudgingly let it stand.

**[Krolewiecki et al:](https://www.sciencedirect.com/science/article/pii/S258953702100239X) **Another Argentine study. This one is a real RCT. 30 patients received ivermectin, 15 were the control group (no placebo, again). Primary outcome was difference in viral load on day 5. The trend favored ivermectin but it was not statistically significant, although they were able to make it statistically significant if they looked at a subset of higher-IVM-plasma-concentration patients. They did not find any difference in clinical outcomes.

A pro-ivermectin person could point out that in the subgroup with the highest ivermectin concentrations, the drug seemed to work. A skeptic could point out that this is exactly the kind of subgroup slicing that you are not supposed to do without pre-registering it, which I don’t think this team did. I agree with the skeptic. 

**[Vallejos et al:](https://bmcinfectdis.biomedcentral.com/articles/10.1186/s12879-021-06348-5) **Another Argentine study. It’s big (250 people in each arm). It’s an RCT. It tries to define a primary outcome (“Primary outcome: the trial ended when the last patient who was included achieved the end of study visit”), but that’s not what “primary outcome” means, and they don’t offer an alternative.

Other outcomes: no difference in PCR on days 3 or 12. Hospitalization is nonsignificantly better in the ivermectin group (14 vs. 21, p = 0.2), but death is nonsigificantly better in the placebo group (3 vs. 4, p = 0.7). This isn’t even the kind of nonsignificant that might contribute to an exciting meta-analysis later. This is just a pure null result. I cannot find any problem with this study, and neither can anyone else I checked.

This is the biggest RCT we’ve seen so far, so we should take it seriously.

**[TOGETHER Trial:](https://rethinkingclinicaltrials.org/news/august-6-2021-early-treatment-of-covid-19-with-repurposed-therapies-the-together-adaptive-platform-trial-edward-mills-phd-frcp/) **Speaking of big RCTs…

This one hasn’t been published yet. There’s a video of a talk about it, but I am not going to watch it, because it is a video, so I am getting information secondhand from eg [here](https://www.wired.com/story/better-data-on-ivermectin-is-finally-on-its-way/). Apparently, it compares 677 people (!) randomized to ivermectin to 678 people randomized to placebo. 86 ivermectin patients ended up in the hospital compared to 95 placebo patients, p-value not significant.

This was a really big professional trial done by bigshot researchers from a major Canadian university, and the medical establishment is taking it much more seriously than any of these others. When it comes out, it will probably get published in a top journal. When discussing Lopez-Medina, I wrote:

> When people say things like “sure, a lot of small studies show good results for ivermectin, but the bigger and more professional trials don’t”, this is one of the two big professional trials they’re talking about.

This is the other one.

Not coincidentally, it’s also the other trial that ivmmeta.com has a warning letter underneath telling you to disregard. Their main concern is that instead of truly randomizing patients to ivermectin vs. placebo, they did a time-dependent randomization that meant during some weeks more patients were getting one or the other. This is a problem because the trial takes place in Brazil, where different variants were more common at different times. Here’s their image:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1f65fd44-58b9-4489-a934-02a5a7330499_706x768.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1f65fd44-58b9-4489-a934-02a5a7330499_706x768.png)

On the one hand, I have immense contempt for ivmmeta for letting all those other awful studies pass and then pulling out all the stops to try to nitpick this one. I have no idea if their proposed randomization failure really happened. And no doubt the reason they’re even able to investigate this is that this study is really careful and transparent - most of them don’t tell you anything about their randomization method. I would be shocked if other studies don’t have all these problems and worse.

On the other hand, the point isn’t to be fair, it’s to be right. And this is a potential confounder. Not a huge one. But a potential one.

I guess all we can do is try to bound the damage. Even if the confounding is 100% real and bad, there’s no way to make this study consistent with the crazy super-pro-ivermectin results of studies like Espitia-Hernandez and Aref. And even if we deny any confounding, we see the same slight pro-ivermectin trend - 86 hospitalizations vs. 95 - that we’ve seen in so many other studies.

Nothing is going to make me believe that this isn’t in the top 33% of studies we’ve been looking at, so let’s add it as grist for the meta-analysis (though maybe not quite as much grist as its vast size indicates) and move on, angrily.

**[Buonfrate et al:](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3918289) **An Italian RCT. Patients were randomized into low-dose ivermectin (32), placebo (29), or high-dose ivermectin (32). Primary outcome was viral load on day 7. There was no significant difference (average of 2 in ivermectin groups, 2.2 in placebo group). 

They admit that they failed to reach the planned sample size, but did a calculation to show that even if they had, the trial could not have returned a positive result. Clinically, an average of 2 patients were hospitalized in each of the ivermectin arms, compared to 0 in the placebo arm - which bucks our previously-very-constant pro-ivermectin trend.

**[Mayer et al:](https://zenodo.org/record/5525362) **Not an RCT. Patients in an Argentine province were offered the opportunity to try ivermectin; 3266 said yes and become the experimental group, 17966 said no and became the control group. There were many obvious differences between the groups, but they all seemed to handicap ivermectin. There was a nonsignificant trend toward less hospitalization and significantly less mortality (1.5% vs. 2.1%, p = 0.03).

While looking into this study, I learned the term “[immortal time bias](https://www.bmj.com/content/340/bmj.b5087)”. This means a period in between selection for the study and the beginning of study recording where patient outcomes are not counted. I think the problem here is that if you signed up for the system on Day X, and if you got sick before they could give you ivermectin, you were in the control group. See [this Twitter thread](https://twitter.com/nickmmark/status/1444125469578653702), I have not confirmed everything he says.

This only hardens my resolve to stay away from non-RCTs.

**[Borody et al:](https://www.covidstrategies.org/combination-therapy-for-covid-19-based-on-ivermectin-in-an-australian-population/) **Our last paper!

…is it a paper? I can’t find it published anywhere. It mostly seems to be on news sites. Doesn’t look peer-reviewed. And it starts with “Note that views expressed in this opinion article are the writer’s personal views”. Whatever. 600 Australians were treated with ivermectin, doxycycline, and zinc. The article compares this to an “equivalent control group” made of “contemporary infected subjects in Australia obtained from published Covid Tracking Data”; this is not how you control group, @#!% you.

Then it gets excited about the fact that most patients had better symptoms at the end of the ten-day study period than the beginning (untreated COVID resolves in about ten days). _Why are these people wasting my time with this?_ Let’s move on.

### The Analysis

If we remove all fraudulent and methodologically unsound studies from the table above, we end up with this:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2d8a451b-b1fc-44e5-ae67-b1506e491762_914x657.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2d8a451b-b1fc-44e5-ae67-b1506e491762_914x657.png)

Gideon Meyerowitz-Katz, who investigated many of the studies above for fraud, tried a similar exercise. I learned about his halfway through, couldn’t help seeing it briefly, but tried to avoid remembering it or using it when generating mine (also, I did take the result of his fraud investigations into account), so they should be considered _not quite_ independent efforts. His looks like this:

[![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F17d5827a-38da-4a99-beb3-c3018df5c633_920x604.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F17d5827a-38da-4a99-beb3-c3018df5c633_920x604.png)

He nixed Chowdhury, Babaloba, Ghauri, Faisal, and Aref, but kept Szenta Fonseca, Biber (?), and Mayer. There was correlation of 0.45, which I guess is okay.

I asked him about his decision-making, and he listed a combination of serious statistical errors and small red flags adding up. I was pretty uncomfortable with most of these studies myself, so I will err on the side of severity, and remove all studies that _either_ I _or_ Meyerowitz-Katz disliked. We end up with the following short list:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc692fec8-a450-4579-b337-c72bec060970_912x298.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc692fec8-a450-4579-b337-c72bec060970_912x298.png)

We’ve gone from 29 studies to 11, getting rid of 18 along the way. For the record, we eliminated 2/19 for fraud, 1/19 for severe preregistration violations, 10 for methodological problems, and 6 because Meyerowitz-Katz was suspicious of them.

…but honestly this table still looks pretty good for ivermectin, doesn’t it? Still lots of big green boxes.

Meyerowitz-Katz accuses ivmmeta of cherry-picking what statistic to use for their forest plot. That is, if a study measures ten outcomes, they sometimes take the most pro-ivermectin outcome. Ivmmeta.com counters that they used a consistent and reasonable (if complicated) process for choosing their outcome of focus, that being:

> If studies report multiple kinds of effects then the most serious outcome is used in calculations for that study. For example, if effects for mortality and cases are both reported, the effect for mortality is used, this may be different to the effect that a study focused on. If symptomatic results are reported at multiple times, we used the latest time, for example if mortality results are provided at 14 days and 28 days, the results at 28 days are used. Mortality alone is preferred over combined outcomes. Outcomes with zero events in both arms were not used (the next most serious outcome is used — no studies were excluded). For example, in low-risk populations with no mortality, a reduction in mortality with treatment is not possible, however a reduction in hospitalization, for example, is still valuable. Clinical outcome is considered more important than PCR testing status. When basically all patients recover in both treatment and control groups, preference for viral clearance and recovery is given to results mid-recovery where available (after most or all patients have recovered there is no room for an effective treatment to do better). If only individual symptom data is available, the most serious symptom has priority, for example difficulty breathing or low SpO2 is more important than cough.

I’m having trouble judging this, partly because Meyerowitz-Katz says ivmmeta has corrected some earlier mistakes, and partly because there really is some reasonable debate over how to judge studies with lots of complicated endpoints. By this point I had completely forgotten what ivmmeta did, so I independently coded all 11 remaining studies following something in between my best understanding of their procedure and what I considered common sense. The only exception was that when the most severe outcome was measured in something other than patients (ie average number of virus copies per patient), I defaulted to one that was measured in patients instead, to keep everything with the same denominator. My results mostly matched ivmmeta’s, with one or two exceptions that I think are within the scope of argument or related to my minor deviations from their protocol.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff36db98e-e653-44da-906c-20312b1689a3_468x205.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff36db98e-e653-44da-906c-20312b1689a3_468x205.png)Placebo vs. ivermectin groups sometimes differed in size, which I’ve adjusted for and rounded off.

Probably I’m forgetting some reason I can’t just do simple summary statistics to this, but whatever. It is p = 0.15, not significant.

This is maybe unfair, because there aren’t a lot of deaths in the sample, so by focusing on death rather than more common outcomes we’re pointlessly throwing away sample size. What happens if I unprincipledly pick whatever I think the most reasonable outcome to use from each study is? I’ve chosen “most reasonable” as a balance between “is the most severe” and “has a lot of data points”:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd189a844-daf2-4199-bb2e-830d4fc64415_468x206.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd189a844-daf2-4199-bb2e-830d4fc64415_468x206.png)

Now it’s p = 0.04, seemingly significant, but I had to make some unprincipled decisions to get there. I don’t think I specifically replaced negative findings with positive ones, but I can’t prove that even to myself, let alone to you.

_[**UPDATE 5/31/22:** A reader writes in to tell me that the t-test I used above is overly simplistic. A Dersimonian-Laird test is more appropriate for meta-analysis, and would have given 0.03 and 0.005 on the first and second analysis, where I got 0.15 and 0.04. This significantly strengthens the apparent benefit of ivermectin from ‘debatable’ to ‘clear’. I discuss some reasons below why I am not convinced by this apparent benefit.]_

(how come I’m finding a bunch of things on the edge of significance, but the original ivmmeta site found a lot of extremely significant things? Because they combined ratios, such that “one death in placebo, zero in ivermectin” looked like a nigh-infinite benefit for ivermectin, whereas I’m combining raw numbers. Possibly my way is statistically illegitimate for some reason, but I’m just trying to get a rough estimate of how convinced to be)

So we are stuck somewhere between “nonsignificant trend in favor” and “maybe-significant trend in favor, after throwing out some best practices”.

This is normally where I would compare my results to those of other meta-analyses made by real professionals. But when I look at them, they all include studies later found to be fake, like Elgazzar, and unsurprisingly come up with wildly positive conclusions. There are about six in this category. One of them [later revised their results to exclude Elgazzar](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8415517/) and still found strong efficacy for ivermectin, but they still included Niaee and some other dubious studies.

The only meta-analysis that doesn’t make these mistakes is [Popp](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD015017.pub2/full) (a Cochrane review), which is from before Elgazzar was found to be fraudulent, but coincidentally excludes it for other reasons. It also excludes a lot of good studies like Mahmud and Ravakirti because they give patients other things like HCQ and azithromycin - I chose to include them, because I don’t think they either work or have especially bad side effects, so they’re basically placebo - but Cochrane is always harsh like this. They end up with a point estimate where ivermectin cuts mortality by 40% - but say the confidence intervals are too wide to draw any conclusion. 

I think this basically agrees with my analyses above - the trends really are in ivermectin’s favor, but once you eliminate all the questionable studies there are too few studies left to have enough statistical power to reach significance.

Except that everyone is still focusing on deaths and hospitalizations just because they’re flashy. Mahmud et al, which everyone agrees is a great study, found that ivermectin decreased days until clinical recovery, p = 0.003? 

So what do you do?

This is one of the toughest questions in medicine. It comes up again and again. You have some drug. You read some studies. Again and again, more people are surviving (or avoiding complications) when they get the drug. It’s a pattern strong enough to common-sensically notice. But there isn’t an undeniable, unbreachable fortress of evidence. The drug is really safe and doesn’t have a lot of side effects. So do you give it to your patients? Do you take it yourself?

Here this question is especially tough, because, uh, if you say anything in favor of ivermectin you will be cast out of civilization and thrown into the circle of social hell reserved for Klan members and 1/6 insurrectionists. All the health officials in the world will shout “horse dewormer!” at you and compare you to Josef Mengele. But good doctors aren’t supposed to care about such things. Your only goal is to save your patient. Nothing else matters.

I am telling you that Mahmud et al is a good study and it got p = 0.003 in favor of ivermectin. You can take the blue pill, and stay a decent respectable member of society. Or you can take the horse dewormer pill, and see where you end up.

In a second, I’ll tell you my answer. But you won’t always have me to answer questions like this, and it might be morally edifying to observe your thought process in situations like this. So take a second, and meet me on the other side of the next section heading.

…

…

…

…

…

### The Synthesis

Hopefully you learned something interesting about yourself there. But my answer is: worms!

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F505c5ac4-3fe8-47a4-8505-dab80601b44d_416x198.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F505c5ac4-3fe8-47a4-8505-dab80601b44d_416x198.png)

As several doctors and researchers have pointed out (h/t especially [Avi Bitterman](https://twitter.com/AviBittMD) and [David Boulware](https://twitter.com/boulware_dr)), the most impressive studies come from places that are _teeming with worms._ Mahmud from Bangladesh, Ravakirti from East India, Lopez-Medina from Colombia, etc.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fac9e4f34-f9cc-40f2-9d83-da4e7178fad7_772x330.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fac9e4f34-f9cc-40f2-9d83-da4e7178fad7_772x330.png)

Here’s the prevalence of roundworm infections by country ([source](https://journals.sagepub.com/doi/full/10.1177/2058739220959915)). But alongside roundworms, there are threadworms, hookworms, blood flukes, liver flukes, nematodes, trematodes, all sorts of worms. Add them all up and somewhere between half and a quarter of people in the developing world have at least one parasitic worm in their body.

Being full of worms may impact your ability to fight coronavirus. [Gluchowska et al](https://doi.org/10.3390/jcm10112533) write:

> Helminth [ie worm] infections are among the most common infectious diseases. Bradbury et al. highlight the possible negative interactions between helminth infection and COVID-19 severity in helminth-endemic regions and note that alterations in the gut microbiome associated with helminth infection appear to have systemic immunomodulatory effects. It has also been proposed that helminth co-infection may increase the morbidity and mortality of COVID-19, because the immune system cannot efficiently respond to the virus; in addition, vaccines will be less effective for these patients, but **treatment and prevention of helminth infections might reduce the negative effect of COVID-19**. During millennia of parasite-host coevolution helminths evolved mechanisms suppressing the host immune responses, which may mitigate vaccine efficacy and increase severity of other infectious diseases.

Treatment of worm infections might reduce the negative effect of COVID-19! And ivermectin is a deworming drug! You can see where this is going…

The most relevant species of worm here is the roundworm _Strongyloides stercoralis_. Among the commonest treatments for COVID-19 is corticosteroids, a type of immunosuppresant drug. The types of immune responses it suppresses do more harm than good in coronavirus, so turning them off limits collateral damage and makes patients better on net. But these are also the types of immune responses that control _Strongyloides_. If you turn them off even very briefly, the worms multiply out of control, you get what’s called “ _Strongyloides_ hyperinfection”, and pretty often you die. According to [the WHO](https://www.who.int/news/item/17-12-2020-a-parasitic-infection-that-can-turn-fatal-with-administration-of-corticosteroids):

> The current COVID-19 pandemic serves to highlight the risk of using systemic corticosteroids and, to a lesser extent, other immunosuppressive therapy, in populations with significant risk of underlying strongyloidiasis. Cases of strongyloidiasis hyperinfection in the setting of corticosteroid use as COVID-19 therapy have been described and draw attention to the necessity of addressing the risk of iatrogenic strongyloidiasis hyperinfection syndrome __ in infected individuals prior to corticosteroid administration.
> 
> Although this has gained importance in the midst of a pandemic where corticosteroids are one of few therapies shown to improve mortality, its relevance is much broader given that corticosteroids and other immunosuppressive therapies have become increasingly common in treatment of chronic diseases (e.g. asthma or certain rheumatologic conditions).

So you need to “address the risk” of _strongyloides_ infection during COVID treatment in roundworm-endemic areas. And how might you address this, WHO?

> Treatment of chronic strongyloidiasis with ivermectin 200 µg/kg per day orally x 1-2 days is considered safe with potential contraindications including possible _Loa loa_ infection (endemic in West and Central Africa), pregnancy, and weight <15kg.
> 
> Given ivermectin’s safety profile, the United States has utilized presumptive treatment with ivermectin for strongyloidiasis in refugees resettling from endemic areas, and both Canada and the European Centre for Disease Prevention and Control have issued guidance on presumptive treatment to avoid hyperinfection in at risk populations. Screening and treatment, or where not available, addition of ivermectin to mass drug administration programs should be studied and considered.

This is serious and common enough that, if you’re not going to screen for it, it might be worth “add[ing] ivermectin to mass drug administration programs” in affected areas! 

Dr. Avi Bitterman [carries](https://twitter.com/AviBittMD/status/1461076939192602628) the hypothesis to the finish line:

[![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5da21781-249c-4e59-b616-9f23d83cc044_2048x1184.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5da21781-249c-4e59-b616-9f23d83cc044_2048x1184.jpeg)

[![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdcd6e4b2-37f7-4602-93d5-2581c3b27a60_700x432.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdcd6e4b2-37f7-4602-93d5-2581c3b27a60_700x432.png)

[![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7fd6e8f4-093e-4e02-bce7-363615146c9c_2228x1346.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7fd6e8f4-093e-4e02-bce7-363615146c9c_2228x1346.jpeg)

[![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0425847-198a-4bd3-a63b-149f15d147ba_700x432.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0425847-198a-4bd3-a63b-149f15d147ba_700x432.png)First two images are with all relevant studies; second two are a sensitivity analysis that removes some of the most dubious.

The good ivermectin trials in areas with low _Strongyloides_ prevalence, like Vallejos in Argentina, are mostly negative. The good ivermectin trials in areas with high _Strongyloides_ prevalence, like Mahmud in Bangladesh, are mostly positive.

Worms can’t explain the viral positivity outcomes (ie PCR), but Dr. Bitterman suggests that once you remove low quality trials and worm-related results, the rest looks like simple publication bias:

[![Twitter avatar for @AviBittMD](https://substackcdn.com/image/twitter_name/w_96/AviBittMD.jpg)Avi Bitterman, MD @AviBittMDStrongyloides superinfection doesn't explain viral positivity outcomes of Ivermectin. That's just explained by plain old publication bias. ![Image](https://substackcdn.com/image/fetch/w_600,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FFDfFUMeXIAAOrCN.jpg)![Image](https://substackcdn.com/image/fetch/w_600,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FFDfFU7dXsAE3wEa.jpg)![Twitter avatar for @TjabbeT](https://substackcdn.com/image/twitter_name/w_40/TjabbeT.jpg)Tjabbe Tjibsma @TjabbeT@EdoajoEric This doesn't explain shorter time to viral clearance or dose dependent effect in an ivm arm in some trials.](https://twitter.com/AviBittMD/status/1456850086399520776)[5:05 AM ∙ Nov 6, 2021

* * *

9Likes2Retweets](https://twitter.com/AviBittMD/status/1456850086399520776)

This is still just a possibility. Maybe I’m over-focusing too hard on a couple positive results and this will all turn out to be nothing. Or who knows, maybe ivermectin does work against COVID a little - although it would have to be very little, fading to not at all in temperate worm-free countries. But this theory feels right to me.

It feels right to me because it’s the most troll-ish possible solution. Everybody was wrong! The people who called it a miracle drug against COVID were wrong. The people who dismissed all the studies because they F@#king Love Science were wrong. Ivmmeta.com was wrong. Gideon Meyerowitz-Katz was…well, he was right, actually, I got the worm-related meta-analysis graphic above from his Twitter timeline. Still, an excellent troll.

Also, the best part is that I ignorantly asked, in my description of Mahmud et al above:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9972491b-25b0-4c06-8aca-86fce102ae63_666x147.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9972491b-25b0-4c06-8aca-86fce102ae63_666x147.png)

And it was! It was a fluke! A literal, physical, fluke! For my whole life, God has been placing terrible puns in my path to irritate me, and this would be the worst one ever! So it _has_ _to_ be true!

### The Scientific Takeaway

About ten years ago, when the replication crisis started, we learned a certain set of tools for examining studies.

Check for selection bias. Distrust “adjusting for confounders”. Check for p-hacking and forking paths. Make teams preregister their analyses. Do forest plots to find publication bias. Stop accepting p-values of 0.049. Wait for replications. Trust reviews and meta-analyses, instead of individual small studies. 

These were good tools. Having them was infinitely better than not having them. But [even in 2014](https://slatestarcodex.com/2014/04/28/the-control-group-is-out-of-control/), I was writing about how many bad studies seemed to slip through the cracks even when we pushed this toolbox to its limits. We needed new tools.

I think the methods that Meyerowitz-Katz, Sheldrake, Heathers, Brown, Lawrence and others brought to the limelight this year are some of the new tools we were waiting for.

Part of this new toolset is to check for fraud. About 10 - 15% of the seemingly-good studies on ivermectin ended up extremely suspicious for fraud. Elgazzar, Carvallo, Niaee, Cadegiani, Samaha. There are ways to check for this even when you don’t have the raw data. Like:

  * [The Carlisle-Stouffer-Fisher method](https://pubmed.ncbi.nlm.nih.gov/28786843/): Check some large group of comparisons, usually the Table 1 of an RCT where they compare the demographic characteristics of the control and experimental groups, for reasonable p-values. Real data will have p-values all over the map; one in every ten comparisons will have a p-value of 0.1 or less. Fakers seem bad at this and usually give everything a nice safe p-value like 0.8 or 0.9.

  * [GRIM](https://jamesheathers.medium.com/the-grim-test-a-method-for-evaluating-published-research-9a4e5f05e870) \- make sure means are possible given the number of numbers involved. For example, if a paper reports analyzing 10 patients and finding that 27% of them recovered, something has gone wrong. One possible thing that could have gone wrong is that the data are made up. Another possible thing is that they’re not giving the full story about how many patients dropped out when. But _something_ is wrong.




But having the raw data is much better, and lets you notice if, for example, there are just ten patients who have been copy-pasted over and over again to make a hundred patients. Or if the distribution of values in a certain variable is unrealistic, like [the Ariely study](http://datacolada.org/98) where cars drove a number of miles that was perfectly evenly distributed from 0 to 50,000 and then never above 50,000.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fceb0bb9b-045c-41b3-a3ea-4974bef9eb2d_1024x630.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fceb0bb9b-045c-41b3-a3ea-4974bef9eb2d_1024x630.png)[Source](http://datacolada.org/98). Real data would follow something like a bell curve.

This is going to require a social norm of always sharing data. Even better, journals should require the raw data before they publish anything, and should make it available on their website. People are going to fight _hard_ against this, partly because it’s annoying and partly because of (imho exaggerated) patient privacy related concerns. Somebody’s going to try make some kind of gated thing where you have to prove you have a PhD and a “legitimate cause” before you can access the data, and that person should be fought tooth and nail (some of the “data detectives” who figured out the ivermectin study didn’t have advanced degrees). I want a world where “I did a study, but I can’t show you the data” should be taken as seriously as “I determined P = NP, but I can’t show you the proof.”

The second reason I think this, aside from checking for fraud, is checking for mistakes. I have no proof this was involved in ivermectin in particular. But I’ve been surprised how often it comes up when I talk to scientists. Someone in their field got a shocking result, everyone looked over the study really hard and couldn’t find any methodological problems, there’s no evidence of fraud, so do you accept it? A lot of times instead I hear people say “I assume they made a coding error”. I believe them, because I have made a bunch of stupid errors. Sometimes you make the errors for me - an early draft of [this post](https://slatestarcodex.com/2020/01/28/assortative-mating-and-autism/) of mine stated that there was an strong positive effect of assortative mating on autism, but when I double-checked it was entirely due to some idiot who filled out the survey and claimed to have 99999 autistic children. In this very essay, I almost said that a set of ivermectin studies showed a positive result because I was reading the number for whether two lists were correlated rather than whether a paired-samples t-test on the lists was significant. I think lots of studies make these kinds of errors. But even if it’s only 1%, these will make up much more than 1% of published studies, and _much_ more than 1% of important ground-breaking published studies, because correct studies can only prove true things, but false studies can prove arbitrarily interesting hypotheses (did you know there was an increase in the suicide rate on days that Donald Trump tweeted?!?) and those are the ones that will get published and become famous.

So if the lesson of the original replication crisis was “read the methodology” and “read the preregistration document”, this year’s lesson is “read the raw data”. Which is a bit more of an ask. Especially since most studies don’t make it available.

### The Sociological Takeaway

I’ve been thinking about this one a lot too.

Ivermectin supporters were really wrong. I enjoy the idea of a cosmic joke where ivermectin sort of works in some senses in some areas. But the things people were claiming - that ivermectin has a 100% success rate, that you don’t need to take the vaccine because you can just take ivermectin instead, etc - have been untenable not just since the big negative trials came out this summer, but even by the standards of the early positive trials. Mahmud et al was big and positive and exciting, but it showed that ivermectin patients recovered in about 7 days on average instead of 9. I think the conventional wisdom - that the most extreme ivermectin supporters were mostly gullible rubes who were bamboozled by pseudoscience - was basically accurate.

Mainstream medicine has reacted with slogans like “believe Science”. I don’t know if those kinds of slogans ever help, but they’re especially unhelpful here. A quick look at ivermectin supporters shows their problem is they believed Science _too much_.

[![Twitter avatar for @Bannisterious](https://substackcdn.com/image/twitter_name/w_96/Bannisterious.jpg)Andrew Bannister @Bannisterious@jonno_bosch I work in hospitality so I need things to return to normal ASAP. I am using Ivermectin as a prophylactic. Hugely influenced by Carvallo trail and Chala trail which showed huge protection](https://twitter.com/Bannisterious/status/1360262698089480210)[4:21 PM ∙ Feb 12, 2021](https://twitter.com/Bannisterious/status/1360262698089480210)

[![Twitter avatar for @fatlas6](https://substackcdn.com/image/twitter_name/w_96/fatlas6.jpg)fatlas @fatlas6@mtskullcrusher @HereComeTheJud @therealjosexy @joeycadre @PeegeRiley @dcwickedestcity @blaireerskine Read Raad. Or Mahmud. Or ICON study from Florida. Or Mexico City hospitalizations study. Or Niaee. Or... Or just type "ivermectin covid" in Google Scholar and read.](https://twitter.com/fatlas6/status/1433544005866844190)[9:34 PM ∙ Sep 2, 2021](https://twitter.com/fatlas6/status/1433544005866844190)

[![Twitter avatar for @TriciaVonne](https://substackcdn.com/image/twitter_name/w_96/TriciaVonne.jpg)Tricia @TriciaVonneWell...now, all of a sudden...Ivermectin is cool to take for COVID (as long as it is taken with Doxycycline)? 🧐 But...I thought Ivermectin was "horse dewormer"...smh ![Image](https://substackcdn.com/image/fetch/w_600,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FFDppqp3WUAIRW3c.jpg)![Image](https://substackcdn.com/image/fetch/w_600,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FFDppq6iWYAEMRH_.jpg)![Image](https://substackcdn.com/image/fetch/w_600,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FFDpprL3XsAIQkn7.jpg)](https://twitter.com/TriciaVonne/status/1457593623810396163)[6:19 AM ∙ Nov 8, 2021

* * *

6Likes2Retweets](https://twitter.com/TriciaVonne/status/1457593623810396163)

They have a very reasonable-sounding belief, which is that if dozens of studies all say a drug works really well, then it probably works really well. When they see dozens of studies saying a drug works really well, and the elites saying “no don’t take it!”, their _extremely natural_ conclusion is that it works really well but the elites are covering it up. 

Sometimes these people even have a specific theory for why elites are covering up ivermectin, like that pharma companies want you to use more expensive patented drugs instead. This theory is _extremely plausible_. Pharma companies are always trying to convince people to use expensive patented drugs instead of equally good generic alternatives. Ivermectin believers probably heard about this from the many, many good articles by responsible news outlets, discussing the many, many times pharma companies have tried to trick people into using more expensive patented medications. Like [this ACSH article about Nexium](https://www.acsh.org/news/2017/01/18/nexium-dark-side-pharma-10546). Or [my article on esketamine](https://slatestarcodex.com/2019/03/11/ketamine-now-by-prescription/). Given that dozens of studies said a drug worked, and elites continued to deny it worked, and there are well-known times where elites lie about drugs in order to make money, it was an _incredibly reasonable_ inference that this was one of those times. 

If you have a lot of experience with pharma, you know who lies and who doesn’t, and you know what lies they’re willing to tell and which ones they shrink back from. As far as I know, no reputable scientist has ever come out and _said ‘_ esketamine definitely works better than regular ketamine’. The regulatory system just _heavily implied_ it. 

I claim that with ivermectin, even the people who don’t usually lie were saying it was ineffective, and they were saying it more directly and decisively than liars usually do. But most people can’t translate Pharma → English fluently enough to know where the space of “things people routinely lie about and nobody worries about it too much” ends. So they _incredibly reasonably_ assume anything could be a lie. And if you don’t know which statements about pharmaceuticals are lies, “the one that has dozens of studies contradicting it” is a pretty good heuristic!

If you tell these people to “believe Science”, you will just worsen the problem where they trust dozens of scientific studies done by scientists using the scientific method over the pronouncements of the CDC or whoever.

So “believe experts”? That would have been better advice _in this case_. But the experts have beclowned themselves again and again throughout this pandemic, from the first stirrings of “anyone who worries about coronavirus reaching the US is dog-whistling anti-Chinese racism”, to the Surgeon-General tweeting “Don’t wear a face mask”, to government campaigns focusing entirely on hand-washing (HEPA filters? What are those?) Not only would a recommendation to trust experts be misleading, I don’t even think you could make it work. People would notice how often the experts were wrong, and your public awareness campaign would come to naught.

But also: one of the data detectives who exposed some fraudulent ivermectin papers was a medical student, which puts him somewhere between pond scum and hookworms on the Medical Establishment Totem Pole. Some of the people whose studies he helped sink were distinguished Professors of Medicine and heads of Health Institutes. If anyone interprets “trust experts” as “mere medical students must not publicly challenge heads of Health Institutes”, then we’ve accidentally thrown the fundamental principle of science out with the bathwater. But Pierre Kory, spiritual leader of the Ivermectin Jihad, is a distinguished critical care doctor. What heuristic tells us “Medical students should be allowed to publicly challenge heads of Health Institutes” but _not “_ Distinguished critical care doctors should be allowed to publicly challenge the CDC”?

Then what about “believe statisticians”? I’ve never heard anyone propose this before, but re-centering the mystique of scientific-expertise in study-analyzers and study-aggregators rather than object-level scientists is…one way you could go, I guess. Statisticians admittedly sort of failed us here: the first several meta-analyses said ivermectin worked. But the statistical _process_ \- the idea that studies are raw materials, but it takes skill to turn them into the finished good of scientific knowledge - sort of comes out looking good. If we need to summarize our takeaway in a slogan of exactly two words, one of which is “trust”, you could do worse than this one.

(am I secretly suggesting that we make _rationality_ higher status? Maybe, although rationalists did no better here during the early phase of “looks promising so far” than anyone else, and it was researchers digging into the nitty-gritty of the data who really solved this.)

Or maybe this is the wrong level on which to think about this. Maybe there isn’t and can’t be a simple heuristic you can teach everyone in school or via a PR campaign which will lead to them having making good health decisions in an adversarial information environment, without having any negative effects anywhere else. But you also don’t want people to make bad health decisions. So what do you do?

### The Political Takeaway

All of this is complicated by the impression many people (including me) have, that ivermectin boosterism and vaccine denialism are closely linked. The ivermectin evidence is complicated. There’s room for doubt. I can maybe see room for doubt on some marginal vaccine-related issues like how seriously to take the occasional reports of myocarditis in teens. But the basic issue - that the vaccine works really well and is incredibly safe for adults - seems beyond question. Yet people keep questioning it.

I think it’s important to address ivermectin support on its own terms - as a potentially plausible scientific theory in a debris field of confusing evidence, which should be debated to the usual standards of scientific debate. I’ve tried to do that above. But this picture wouldn’t be complete without acknowledging the overlap with vaccine denial - a segment of people who are completely crazy and wrong and who happen to have fixated on this mildly interesting question as opposed to some other one with even less evidence.

I’ve been trying to figure out a model where ivermectin support _and_ vaccine denialism both make visceral sense to me, and here’s what I’ve got:

Imagine that in 2025, an alien invasion fleet reaches Earth. But it got hit by a supernova on the way, the spaceships are partly disabled, and they’re only able to conquer some out-of-the-way place - let’s say Australia. There’s a few cycles of conflict and cease-fire, a few cities get nuked, and finally we settle into an uneasy peace.

Over the next few years, humanity grudgingly admits the invaders into the world community. They get a seat in the United Nations. We sort of cooperate with them on projects that are important to both sides, like stopping climate change. We still hate them, but only at the level of ordinary international rivalries, like USA/USSR.

In 2035, the aliens announce that a quantum memetic plague from the Andromeda Sector has reached Earth. Billions of people will die unless we let them put an immunity-granting cybernetic implant in all humans’ brain. The aliens admit we haven’t always been friends, and honestly they would still like to conquer us someday. But this plague is an ancient enemy of all sentient beings, they dealt with it on their homeworld eons ago, and they want to help us out here.

Humans apparently don’t have the ability to detect quantum memetic plagues, but mortality rates for over-65s do seem weirdly high this year, something like 10x worse than a normal flu season.

Do you let the aliens put an implant in your brain, or not?

[![The US government report on UFOs has landed, but what have movies and TV  taught us to believe? - ABC News](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F598d7d6c-de95-4b94-b13a-3c8a452b0409.jp2)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F598d7d6c-de95-4b94-b13a-3c8a452b0409.jp2)If it helps, the aliens look like this. Surely anyone with a brain that size must know what they’re talking about, right? ([source](https://www.abc.net.au/news/2021-06-26/ufos-in-pop-culture-us-government-report/100227066))

Fine, you don’t have to decide immediately. The brain implants aren’t even ready yet. Some human scientists suggest wearing face masks in the interim. The aliens say no, that will never work, that’s not how you deal with quantum memetic plagues, if you do anything other than wait for the brain implants you’re anti-science idiots who are wasting precious time and will kill millions of people. Human nations try face masks anyway…and they clearly and conspicuously work. The aliens say whatever, we’re still the advanced spacefaring civilization here, maybe it works for humans but that’s not the point, the point is you’ve got to let us put implants in your brains.

Some human scientists suggest reopening vital services. The aliens say no, millions will die, this is “mass human sacrifice”, humans apparently must care nothing about their families’ lives. The humans try reopening anyway, and…it goes kind of okay? Maybe the death rate goes up 10% to 20% or so, hard to say? The aliens say whatever, maybe their calculations were off by a few orders of magnitude, the point is, you have to let us put implants in your brain or you’ll all die.

Then some human scientists suggest vaccinating against the plague. The aliens say this is idiotic, vaccines originally come from cowpox, even the _word_ “vaccine” comes from Latin _vaccus_ meaning “cow”, are you saying you want _cow medicine_ instead of actual brain implants which alien Science has proven will work? They make lots of cartoons displaying humans who want vaccines as having cow heads, or rolling around in cow poop. Meanwhile, the first few dozen studies show vaccines work great. Many top human leaders, including war heroes from the struggle against the aliens, get vaccines and are seen going out in public, looking healthy and happy.

The aliens say that human science is hopelessly flawed because of complicated statistical concepts that inferior life forms like us don’t even have _words for._ You need to ignore all the studies and meta-analyses showing that vaccines definitely work, and let the aliens give you brain implants instead.

So do you let the aliens put an implant in your brain, or not?

Obviously you think long and hard before doing this. And obviously this is an extended metaphor for vaccine denialism. So what’s the difference between the metaphor (where you’re presumably anti-implant) and the real world (where you’re presumably pro-vaccine?)

For me, it’s a combination of:

  1. The aliens are hostile, so I don’t trust them no matter how smart they are

  2. If the aliens are so smart, why did they get their last few predictions wrong?

  3. I can’t even begin to understand the aliens’ argument…what is a “quantum memetic plague”? Why would brain implants treat it? What are the statistical concepts that can’t be explained in human language, and why would they only affect these studies and no others?

  4. I have no idea what you can and can’t do with cybernetic implants, and it seems totally possible they could mind control me or something.




All of these come down to a more basic problem, which is that these are _hostile aliens_. Let’s start with the second word first.

Because they’re alien, I can’t trust they’re on my side. 

Because they’re alien, their predictions feel like a black box. I don’t know if their previous predictions were 50% confidence or 99% confidence, or whether the stupid aliens made the last few predictions but it’s the smart aliens making this new prediction, or whether they’re even telling the truth when they describe previously fighting this plague on their homeworld and learning best practices. 

Because they’re alien, all the words they use like “quantum memetic plague” and “brain implant” feel not only beyond my understanding, but _unfairly_ beyond my understanding, something that neither I nor anyone I trust could ever double-check. 

And because they’re alien, I have no idea how their technology works, and it could do all sorts of sinister things.

I’m not an immunologist. I don’t have the specific expertise it would take to evaluate whether vaccines work. But one of my friends in medical school decided to do a joint MD-PhD in immunology. I didn’t follow her lead, because I didn’t want to spend my entire twenties and thirties in soul-sucking research labs trying to remember thirty different kinds of interleukins. But when I ask myself “why am I not an immunologist?” the answer is something like “because I dislike intense misery” and not “because immunologists are an alien species and I cannot possibly imagine myself becoming one”. 

More generally, I come from a social class where becoming an immunologist is considered a reasonable thing that might happen. Several of my friends and family members are experts in various fields (even for very loose definitions of “expert” like a really excellent social worker who other social workers trust). Even more generally, I know some basics of biology. I know why vaccines should work in theory. I know that even if somebody wanted to control you by sneaking a microchip into a vaccine, that’s impossible with current technology. I know enough about politics and economics to know it’s really unlikely that some cabal of elites has developed super-futuristic technology in secret. And I know a lot of smart people who I could ask these questions to if I were confused, and they could tell me all the stuff above.

John Steinbeck said that socialism never took root in America because even the poor see themselves as “temporarily-embarrassed millionaires” rather than as members of the class of Poor People. If you’re Poor People, and they’re Rich People, maybe you’re on opposite sides and should fight. If you’re temporarily-embarrassed millionaires, and they’re normal millionaires, maybe you’re on the same side and you can trust them. 

In the same way, I think of myself as a temporarily-embarrassed immunologist. I don’t know all the interleukins. But I would like to believe that if I really wanted, either I or at least people I know and trust could learn immunology to a standard where we could double-check the work of the vaccine scientists.

I’ve written before about [filter bubbles](https://slatestarcodex.com/2014/09/30/i-can-tolerate-anything-except-the-outgroup/). About half of Americans are young-earth creationists. I have nothing against these people, I don’t deliberately ostracize them - yet none of my closest hundred friends are in this category. There’s about an 0.5^100 = 10^-31 chance that would happen by coincidence. Some powerful combination of class, cultural, and geographic barriers prevent me from meeting them.

Imagine someone with an equally strong bubble filtering against scientists. Such a person wouldn’t feel like a temporarily-embarrassed immunologist. They would feel like immunologists are some sort of dark and terrible figures from a shadow dimension they could never reach. They would seem like aliens.

And now let’s return to that first word, “hostile”. [95% of biology professors are Democrats](https://www.nas.org/academic-questions/31/2/homogenous_the_political_affiliations_of_elite_liberal_arts_college_faculty). Plus medical organizations keep rubbing [more and more salt in the wound](https://marginalrevolution.com/marginalrevolution/2021/11/the-danger-of-demanding-woke-physicians.html). If you’re a conservative, or even have conservative tendencies, these aliens surely qualify as suspicious and probably anti-Earthling. “99% of hostile aliens agree: vaccines are right for you!” Now we’re back to it not sounding so convincing.

In a world where scientists seemed like hostile aliens, I would hesitate to take the vaccine. Again, ivermectin optimism isn’t exactly like vaccine denialism - it’s a less open-and-shut question, you can still make a plausible argument for it. But it’s some of the same people and follows the same dynamics. If we want to make people more willing to get vaccines, or less willing to take ivermectin, we have to make the scientific establishment feel less like an enclave of hostile aliens to half the population. 

Do that, and people will mostly take COVID-related advice, for the same reason they mostly take advice around avoiding asbestos or using sunscreen - both things we’ve successfully convinced people to do even without having a perfect encapsulation of the scientific method or the ideal balance between evidence and authority.

But I don’t really know how to do that, and any speculation would be too political even for a section titled “The Political Takeaway”.

### The Summary

  * Ivermectin doesn’t reduce mortality in COVID a significant amount (let’s say d > 0.3) in the absence of comorbid parasites: **85-90% confidence**

  * Parasitic worms are a significant confounder in some ivermectin studies, such that they made them get a positive result even when honest and methodologically sound: **50% confidence**

  * Fraud and data processing errors are of similar magnitude to p-hacking and methodological problems in explaining bad studies (95% confidence interval for fraud: **between >1% and 5%** as important as methodological problems; 95% confidence interval for data processing errors: **between 5% and 100% as important**)

  * Probably “Trust Science” is not the right way to reach proponents of pseudoscientific medicine: **???% confidence**



