---
title: "Highlights From The Comments On Diseasonality"
subtitle: "..."
date: 2021-12-23
likes: 44
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/45706834/comments?&all_comments=true
image: https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/cb0b7c7c-fa85-4d26-b76c-7d2e89b78359_750x511.png
original-url: https://www.astralcodexten.com/p/highlights-from-the-comments-on-diseasonality
---
The main highlight was an email I got from a reader who prefers to remain anonymous, linking me to [Projecting The Transmission Dynamics Of SARS-CoV2](https://sci-hub.st/10.1126/science.abb5793). This paper is head and shoulders above anything I found during my own literature review and just comes out and _says_ everything painfully tried to piece together. Either my research skills suck, the epidemiology literature is a bunch of disparate subthreads with wildly differing levels of competence, or both.

The authors (including Marc Lipsitch who some of you might know from Twitter) are writing in May 2020, trying to predict the future course of COVID. To that end, they investigate the past course of two other coronaviruses called OC43 and HKU1, which cause mild colds. These show a seasonal pattern. Why? 

Here’s my understanding, which might not be exactly right: they find that immunity to these other coronaviruses wanes in about a year. They also find that the normal collection of seasonal factors - temperature, humidity, maybe UV, etc - have a multiplicative effect on R. Remember, when R is below 1, the disease gradually dies out; when above 1, it gets worse. At any given time, some percent of people have immunity. Let’s say at some particular time that’s 90%, and maybe that implies an R of 0.5. As time goes on, immunity declines - 85%, 80%, etc - and r creeps up - 0.6, 0.7, etc. Then winter hits, and R goes up by some multiple - the paper says in their particular case it’s a factor of 2, so R of 0.7 becomes 1.4. Now the disease spreads. There’s a seasonal miniepidemic, the disease infects vulnerable people, immunity climbs back to near 100%, R sinks below 1, and the mini-epidemic ends. Then more time passes, immunity declines again, and the cycle repeats.

[EDIT: **demost_** [explained](https://astralcodexten.substack.com/p/diseasonality/comment/3918284) most of this better in a comment on the original post]

The authors write that depending on how long it takes COVID immunity to wane, its outbreaks could be “annual, biennal, or sporadic”.

The same reader sent me a link to [this Twitter thread](https://twitter.com/BallouxFrancois/status/1405939503068598274) by Professor Francois Balloux, who writes:

> Population immunisation will increase through vaccination and infection to reach an equilibrium probably around 95%, pushed down by waning immunity, new births and viral immune escape, and pushed up by (re-)infection and vaccination. Viral transmissibility may still slightly increase above its current [as of June 2021] value (R0 ~ 6.0), but will likely soon hit a buffer and it is now in the ballpark figure of the higher transmissibilities reported for the four endemic 'common cold' coronaviruses in circulation. Sensible people won't wish to maintain social distancing measures for much longer than required. As such, we may soon have three forces out of the system. Whatever their eventual value may be doesn't matter for the dynamic of the system once they've reached an 'equilibrium'. 
> 
> Seasonality will obviously remain. Even if it affects SARSCoV2 transmissibility only moderately, it should start driving the system, pushing R >1 in winter. At this stage, SARSCoV2 will have joined the >200 other seasonal endemic respiratory virus in circulation globally. I wish to reassure those who worry I'm predicting a scenario of eternal carnage that (re-)infections following previous rounds of infection / vaccination are most unlikely to cause severe disease in the vast majority of cases.

This last sentence reminds me of [a discussion](https://astralcodexten.substack.com/p/open-thread-187/comment/2729763) I had with Bram C at the most recent Berkeley meetup. He noted that most diseases are less severe when you get them as a young child, for unclear reasons (chicken pox is the most obvious example). You get most respiratory viruses for the first time as a young child. When you get them a second time, you already have partial immunity from the first time - it’s like COVID with one vaccination. In fact, in the simplified case where everyone in the population is at the same level of immunity, you will have only just reached the point where the virus can infect you at all (after all, if there was an earlier point, the virus would have infected you then). So normally, children (who are weirdly resilient) are the only people who get the full force of a disease, and everyone else gets a weak watered-down version. COVID is worse than other coronaviruses partly because adults are facing its full force. Once every adult has had it a few times (or had a few rounds of shot-and-booster) it may be more like all the other coronaviruses and so very mild. And a hundred years from now, the only immuno-naive people to get COVID will be young children, who will do fine.

(something like this might also be why the Native Americans had such a hard time with European diseases)

But the rest of you had interesting thoughts too, starting with:

**Metacelsus** [writes](https://astralcodexten.substack.com/p/diseasonality/comment/3912809):

> The entrainment / waning immunity mechanism can't explain chickenpox seasonality, since people generally don't get chickenpox (primary VZV infection) twice. So something else must be going on.

But **Ivan Fyodorovich** [responds ](https://astralcodexten.substack.com/p/diseasonality/comment/3912845)that new people are getting born every year. So imagine that in summer, R is 0.7, and in winter it’s 1.4. The new people aging into chickenpox age will get it in winter.

But then we have the same question as before - if it’s wintry all the time in Alaska, what happens there? My guess is - chickenpox spreads faster until there aren’t enough susceptible people left, then waits until new people are born, and then when there are enough of them, there will be an epidemic, and because winter multiplies R it will be in the winter.

**Sniffnoy** [notes ](https://astralcodexten.substack.com/p/diseasonality/comment/3913781)that technically, chickenpox is spring seasonal. I don’t know if this is just “winter seasonal but slow so it peaks in the spring” or something more complicated. **Eric Rall** [points out](https://astralcodexten.substack.com/p/diseasonality/comment/3914177) that we’re all missing something obvious and maybe childhood diseases track _the school year_. Maybe chickenpox would naturally peak in the winter, but gets delayed by winter vacation, and then comes back when kids return to school in January and has to build from there? There’s [some argument downthread](https://astralcodexten.substack.com/p/diseasonality/comment/3915138) about what countries with different school years tell us.

**10240**[writes](https://astralcodexten.substack.com/p/diseasonality/comment/3914962)**:**

> This hypothesis (that seasonality results from a combination of temperature and herd immunity from previous infections) doesn't actually depend on immunity only lasting about a year. And indeed, most people don't get a flu every year, nor every kind of cold; more like once in 10 years.
> 
> Assume that the transmission rate is a product of a factor negatively correlated with temperature, and a factor positively correlated with how long ago you last had the same disease. At equilibrium, the long-term average of the transmission rate is 1. So, in temperate regions, r<1 in the summer, and r>1 in the winter (except if the current year's epidemic has already sufficiently increased the level of immunity to push r below 1—eyeballing the US flu death charts, they seem to peak in early January in the worst years, but later, in the spring, in years with low rates).
> 
> In this model, warmer regions should have less flu overall, since a longer interval between incidences corresponds to a long-term average r of 1. Maybe Alaskans get a flu, say, once in 8 years on average, Floridians every 12 years (still seasonally) and Panamans every 15 years (without seasonality).

That last paragraph sounds fascinating but I’m not sure I understand why it’s true; can someone explain?

**Rafal Smigrodski** [writes](https://astralcodexten.substack.com/p/diseasonality/comment/3915323):

> The mention of wildfire is most apt:
> 
> The most destructive wildfires, or crown-fires, are uncommon under natural circumstances, when the much less destructive ground-fires predominate. Crown-fires do however happen often in actively-managed (or mismanaged) forests, where clueless or ideologically driven forest service suppress fires for decades, which leads to abnormal accumulation of deadfall (fallen branches, trees lying on the ground), and eventually there is so much of this dead dry mass that a randomly started fire becomes too hot to suppress and it destroys everything, down to the root.
> 
> Covidiocy manifesting as lockdowns and masking has so many similarities to the policy of fire suppression. Smart, evidence-based medicine, like vaccinations and targeted quarantines of select vulnerable populations, is very much like scientific forest management, with its prescribed burns.
> 
> I bet the differences in efficacy, measured in dead trees or dead people, will be similar.

I’m having trouble figuring out how to analyze this point. After thinking about it, maybe the problem is I don’t have a good sense of why fires ever stop. Assuming there is at least one continuous line of trees connecting (eg) Maine to Georgia, why didn’t every forest fire burn the entire East Coast to a crisp back before there were human firefighters?

**Jason Crawford** [writes](https://astralcodexten.substack.com/p/diseasonality/comment/3914007):

> To make things slightly more complicated, not all seasonal viruses peak in winter. When the US suffered from annual polio epidemics in the first half of the 20th century, they would come in summer. I'm not sure why this is (or if anyone knows), although I think it was spread by water and one factor might have been swimming in shared pools.

**Brock** [answers](https://astralcodexten.substack.com/p/diseasonality/comment/3919724): 

> Yes, in temperate zones polio was seasonal with peak in summer/autumn. But it's not a respiratory virus, and it spreads via the fecal-oral route. I'd guess that swimming was the seasonality factor for polio.

That’s a pretty good answer! No mystery why fecal-orally transmitted viruses spread differently than respiratory ones.

**Alex G** [does her homework](https://astralcodexten.substack.com/p/diseasonality/comment/3930697) and runs a simulation:

> my intuition is that you get seasonality under very broad assumptions (r0>1 and varies seasonally, immunity wanes on the order of at least a year) and the difference is made up by more people needing to get ill to get to herd immunity.
> 
> rt should be 1 on average in the long run
> 
> I think if we're comparing Alaska in the summer (rt<1) vs Florida in the winter (rt>1) the exponential growth/decay in cases should probably swamp the larger number of cases you'd get in Florida averaged over a year
> 
> […]
> 
> [![Twitter avatar for @pawnofcthulhu](https://substackcdn.com/image/twitter_name/w_96/pawnofcthulhu.jpg)alex @pawnofcthulhu](https://twitter.com/pawnofcthulhu/status/1468801244793765892)
> 
> [Ok I think my intuition is correct here ](https://twitter.com/pawnofcthulhu/status/1468801244793765892)[astralcodexten.substack.com/p/diseasonality](https://astralcodexten.substack.com/p/diseasonality)
> 
> ![Image](https://substackcdn.com/image/fetch/w_600,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FFGI6pn_VkAUk1xU.jpg)
> 
> [4:34 AM ∙ Dec 9, 2021](https://twitter.com/pawnofcthulhu/status/1468801244793765892)

**Mycelium** [says](https://astralcodexten.substack.com/p/diseasonality/comment/3963509):

> In South East Asia, we have two flu seasons a year - a summer season and a winter season - for EXACTLY the reason you mention - in the summer, people coop themselves up at home with the air-conditioning on full blast.
> 
> In the west, shade is adequate to cool you in the summer, so you don't need to close the windows and turn on the A/C. In South East Asia, the muggy air retains heat, requiring air-conditioning and reduced airflow.

As Tyler Cowen would say, solve for the equilibrium!
