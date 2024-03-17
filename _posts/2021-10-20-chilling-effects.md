---
title: "Chilling Effects"
subtitle: "In what sense do 10% of people die of the cold? And why is heat-related death most common in Greenland?"
date: 2021-10-20
likes: 105
original-url: https://www.astralcodexten.com/p/chilling-effects
---
_[Epistemic status: Extremely confused! Low confidence in all of this]_

 **I.**

On [the recent global warming post](https://astralcodexten.substack.com/p/highlights-from-the-comments-on-kids), a commenter argued that at least fewer people would die of cold. I was prepared to dismiss this on the grounds that it couldn’t possibly be enough people to matter, but, um:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2ce8e12-9192-4161-9315-e616edb004f8_1060x444.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2ce8e12-9192-4161-9315-e616edb004f8_1060x444.png)

There are only about sixty million deaths per year total, so if this is true then almost 10% of all deaths are due to cold. That sounds…extremely untrue, right?

You can find the source here ([study](https://www.thelancet.com/journals/lanplh/article/PIIS2542-5196\(21\)00081-4/fulltext), [popular article](https://www.downtoearth.org.in/news/climate-change/extreme-temperatures-kill-5-million-a-year-20-year-study-77875)). The study confirms that it is claiming that 8.52% of all deaths are cold-related (plus an additional ~1% heat-related). It separates the world into a grid of 0.5 degree x 0.5 degree squares. It uses a bunch of assumptions and interpolations to get a dataset of daily average temperatures and mortality rates for each square over ten years. Then it calculates a function of how mortality varies with respect to temperature. The lowest point of that function, usually a pretty normal temperature, gets dubbed “the minimum mortality temperature” or “MMT”. Then they calculate how many extra deaths happen compared to the counterfactual where it was always the MMT, and they get five million. Where are these deaths?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F905e89c9-b477-434b-9ed1-65efcaa51c57_1000x343.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F905e89c9-b477-434b-9ed1-65efcaa51c57_1000x343.png)

People are most likely to die of extreme cold in Sub-Saharan Africa, and most likely to die of extreme heat in Greenland, Norway, and various very high mountains. You’re reading that right - the cold deaths are centered in the warmest areas, and vice versa.

This has got to all be wrong, right? 10% of Africans freezing to death, a substantial number of Greenlanders dying of the heat? The paper doesn’t have any answers. It just presents its mathematical model and runs away. So what’s going on?

 **II.**

When you’re skeptical of complicated models, sometimes it helps to go back to the rawest data you can find. So here’s a graph of mortality rates in New York City over time. It was published to put the coronavirus in context, but we can use it to look at seasonal effects:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fad859ab1-dfb2-4b4d-a022-e571a0913f4d_1210x541.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fad859ab1-dfb2-4b4d-a022-e571a0913f4d_1210x541.png)(source: [NYT](https://www.nytimes.com/interactive/2020/04/10/upshot/coronavirus-deaths-new-york-city.html). I have truncated the vertical axis edited it so it takes up less space)

Deaths definitely go up every winter, from about 4000 to 4500. So yeah, this is about 10% extra deaths during the cold season. Why?

Before we go further - are the deaths coming from the cold, or the winter? That is, if it’s a colder-than-normal day in the winter, do deaths go up even higher than normal? If it’s winter, but it’s still pretty warm out, are there still excess deaths?

The papers I read disagreed pretty intensely about this. [This study from London 1997-2012](https://journals.lww.com/epidem/Fulltext/2016/07000/The_Excess_Winter_Deaths_Measure__Why_Its_Use_Is.6.aspx) concludes:

> Most of the excess winter deaths are driven by cold: The excess winter deaths index decreased from 1.19 to 1.07 after excluding deaths attributable to low temperatures. Over 40% of cold-attributable deaths occurred outside of the December–March period, leading to bias in the excess winter deaths measure.

But [this study](https://oro.open.ac.uk/57830/8/57830.pdf) from London 1951 - 2011 says:

> We found that the association of year-to-year variation in [excess winter deaths] with the number of cold days in winter (< 5ºC), evident until the mid 1970s, has disappeared, leaving only the incidence of influenza-like illnesses to explain any of the year-to-year variation in EWDs in the last decade. Whilst excess winter deaths evidently do exist, winter cold severity no longer predicts the numbers affected.

You can see further debate between these groups [here ](https://www.nature.com/articles/nclimate2302)and [here](https://www.nature.com/articles/nclimate2302), but rather than get bogged down in the math, I want to take a common sense perspective.

There _has_ to be a winter component separate from the cold component. I mentioned before that these studies begin by finding an MMT - a “minimum mortality temperature” - and then figuring out how quickly mortality increases to either side of that minimum.

But MMT [is very different](https://ehp.niehs.nih.gov/doi/pdf/10.1289/ehp.1509692?noaccount=true) in different regions. In Sweden, it’s 18C (64F). In Florida, it’s 27C (81F). The only constant is that it seems to be about 80% of the way through the temperature distribution of a region - so if some city ranges from 0 to 100 degrees, its MMT will probably be around 80; if some other city ranges from 25 to 125, its MMT will be 105. In very hot places, it sometimes gets a bit less than 80%, but never below 60% or so.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2b06bb29-85d7-4149-a007-72fcc292cb6c_676x856.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2b06bb29-85d7-4149-a007-72fcc292cb6c_676x856.png)Mortality rate by temperature in selected cities ([source](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4521077/))

You could argue that this is at least partly because of cultural adaptation. The “effective temperature”, the one that’s reaching your blood vessels and your heart, depends on things like how many layers of clothing you wear, how often you go outside, how much air conditioning you use, et cetera. So for example, in the figure above, Stockholm doesn’t get any increased mortality from the cold, no matter how cold it gets. Plausibly that’s because they’ve organized their lives and built environment around surviving cold winters. One study failed to find any excess cold-weather deaths in Siberians even at temperatures as low as -52C (-62F).

But it can’t all be cultural adaptation, can it? Look at Bangkok in the figure above. They start getting excess cold-weather mortality at around 27C (81F). Grant that they have no adaptation for cold weather at all and none of their houses have heating and whatever. They _still_ should be doing fine at 81F! A [study from Kuwait ](https://www.sciencedirect.com/science/article/pii/S0048969720328060)finds that the Kuwaitis start getting increased mortality when the temperature gets below 35C (95F). It doesn’t matter how unprepared you are, that temperature shouldn’t kill you.

The only logical explanation is that this is an artifact of mortality being higher in the winter. In Kuwait, temperatures below 35C/95F mean you’re in the winter half of the year.

Why is mortality higher in the winter (as opposed to in the cold)? Probably flu and other respiratory illnesses. We still don’t really know why flu is seasonal (it doesn’t seem to be about cold _per se_ ) but it definitely is. Observed cases of flu only make up a small fraction of excess winter deaths, I think even only a small fraction of excess seasonal-as-opposed-to-cold deaths. I find this suspicious, and I wonder if there are a bunch of less obvious seasonal viruses going around causing deaths that don’t get recorded as “seasonal viruses”. Or: we know that sometimes people can get strokes and heart attacks as complications of the flu - maybe we don’t notice the flu, or coroners don’t record it, and it just gets marked as a stroke or heart attack.

[Other studies](https://www.sciencedirect.com/science/article/pii/S0160412018308997) find cold related mortality, separate from winter-related mortality. What could cause this?

The majority of this cold-related death is cardiovascular. Heart attacks [are more common during the winter](https://www.bhf.org.uk/informationsupport/heart-matters-magazine/news/behind-the-headlines/cold-weather-and-heart-attacks). The effect is pretty big; lower the temperature 20 degrees C (or 35 degrees F) and heart attack risk goes up about 15%. Why? The most common story is that surface blood vessels constrict in colder weather, which increases blood pressure and makes the heart work harder. But it’s probably more complicated than this - for whatever reason (maybe partly downstream of the blood vessel constriction?) cooling causes [increases in](https://pubmed.ncbi.nlm.nih.gov/6437575/) blood viscosity, platelet number, and coagulability - ie your blood is more likely to clot, including the kinds of clots that cause heart attacks and strokes. This seems to take a while; studies show that the effect of cold peaks about two weeks after it starts being cold. 

Since heart attacks and strokes are among the most common causes death, a 15% increase is huge. And this is a real effect of cold, not just of winter. So cold weather _has to_ have some independent effect, meaning I side with the team that finds that it does. Probably both winter (through influenza) and cold (through heart attacks) contribute to excess winter/cold mortality. I’m sympathetic to the confusion around this in the models; it’s probably hard to distinguish “winter” from “long period of protracted cold with a lag”. Or “heart attack directly from the cold” vs. “heart attack as a complication of the flu, which happens during the cold season”.

Okay, but why are cold-related deaths most common in Africa? And why are heat-related deaths most common in Greenland?

 **III.**

It’s actually worse than this. There are more cold-related deaths the warmer and more tropical you get, and they’re worst of all in Africa, but I think these two findings are for different reasons.

First, the warmer-and-more tropical thing. See eg [this paper](https://www.demogr.mpg.de/books/drm/003/2.pdf), where the key graph is:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7216887c-ec19-4c36-b714-ffc31c609bbf_723x647.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7216887c-ec19-4c36-b714-ffc31c609bbf_723x647.png)

Again, everyone’s answer for this is “adaptation”. The worse your climate, the more likely you are to have good central heating, sheltered bus stops, and parents who nag their kids to put a hat on before they go out. I’m not entirely convinced by this story. Shouldn’t this mean that everywhere has the _same_ level of excess death from the cold? Why would cold places adapt so hard that they did _better_ than warm places? I don’t know, but this is what everybody says.

What about sub-Saharan Africa? This can’t just be adaptation. Sure, they’re not prepared for the cold. But it never _gets_ cold there. The lowest recorded temperature in Kampala, Uganda [was](https://en.wikipedia.org/wiki/Kampala) 12C (54F). Most years it doesn’t even get _that_ low! Who’s dying from that?

I think cold-related deaths are most common in Africa because of the flu. Flu hits sub-Saharan Africa [really hard](https://medcraveonline.com/IJVV/influenza-associated-morbidity-and-mortality-in-sub-saharan-africa.html), much harder than the developed world. Partly this is because it’s very poor and lacks good health care. And partly it’s because it has many other diseases - especially HIV/AIDS - which weaken people’s immune systems and constitutions to the point where the flu can finish them off. Flu hits in the winter in not-completely-equatorial areas, and all year in equatorial areas. I don’t know if anyone has ever proven whether flu is worse in random non-seasonal cold snaps in equatorial areas, but [it would make sense if it was](https://journals.asm.org/doi/10.1128/JVI.02186-10). Even though most cold-weather deaths in temperate areas are heart attacks, I don’t know of any studies showing this is true in equatorial Africa, so I think probably this is all flu cases.

I realize it’s awkward to propose two different mechanisms for the general heat/cold-death relationship and the African extreme, but I don’t have any better ideas.

Okay, what about heat deaths? Why are they most common in Greenland, Tibet, and the Andes?

The only treatment of Greenland I can find is in [this article](https://books.google.co.uk/books?id=_YvvYpu0LPcC&pg=PA28&lpg=PA28&dq=greenland+death+rate+seasonal&source=bl&ots=ZOEjGpdE7p&sig=ACfU3U2sOMsGy5CUGKNFrp1AzFwkJW7UmA&hl=en&sa=X&ved=2ahUKEwiyotrsldfzAhVPgFwKHYISCqM4ChDoAXoECAsQAw#v=onepage&q=greenland%20death%20rate%20seasonal&f=false), which states that mortality is highest in the summer in Greenland for two reasons. First, it is the traditional hunting season, and there are lots of ways to die while hunting. Second, nobody visits Greenland in the winter, and when visitors (mostly tourists and Danish colonial officials) return in the summer, they bring new diseases. The effect is decreasing as traditional hunting gives way to modern going-to-the-supermarket, and as Inuit become more resistant to Western diseases. Seems plausible, I guess.

I can’t find anything on Tibet or the Andes. The obvious connection is that these are both very high mountains, so I don’t know, something something altitude? The way evaporation works means [it’s easier to dehydrate at high altitudes](https://hydrapak.com/blogs/beyond-adventure/high-altitude-hydration), and dehydration is a common cause of summer heat death, so maybe this checks out? Please let me know if you have any better data or theories on this.

 **IV.**

So let’s get back to the original question? Will global warming increase heat-related death? Will it decrease cold-related death? And which effect will predominate?

I originally expected that the beneficial cold-related effects would be more important; after all, almost 10x more people die of cold than of heat. If global warming halved cold-related deaths while doubling heat-related ones (completely made up numbers), then naively that would be enough to flip its overall effect on humanity from very bad to pretty good. It would save millions of lives per year, even after sea level rise and famines and so on.

Most scientists in the field don’t think this is true.

I’m getting this partly from people who have done sophisticated mathematical models of this, for example [Bressler et al](https://www.nature.com/articles/s41598-021-99156-5), who say that:

> In the absence of income-based adaptation, the global mortality rate in 2080–2099 is expected to increase by 1.8% [95% CI 0.8–2.8%] under a lower-emissions RCP 4.5 scenario and by 6.2% [95% CI 2.5–10.0%] in the very high-emissions RCP 8.5 scenario relative to 2001–2020. When the reduced sensitivity to heat associated with rising incomes, such as greater ability to invest in air conditioning, is accounted for, the expected end-of-century increase in the global mortality rate is 1.1% [95% CI 0.4–1.9%] in RCP 4.5 and 4.2% [95% CI 1.8–6.7%] in RCP 8.5 […] For all 23 countries, Gasparrini et al. predict an increase in heat-related excess mortality and a decrease in cold-related excess mortality under climate change scenarios, **with most countries experiencing a net increase in mortality.**

See also [this paper](https://d1wqtxts1xzle7.cloudfront.net/48786976/Winter_mortality_in_a_warming_climate_A_20160912-15125-18bphz.pdf?1473733137=&response-content-disposition=inline%3B+filename%3DWinter_mortality_in_a_warming_climate_a.pdf&Expires=1634257200&Signature=PpmUvfqr6FBKWMsR~92qwlXzo7tstyk6NRA3XtWmytJu1tgYLZe49OnTznTb3tCKHNncx2-nRhkeVlYjCFCcFMRAz6yrqfFbbsOoxtIussBP3p6JjtsfgoO8m3VZGEYYArojHBT5Ha-NdPvvj5ucqONtrcKGcAZKvuQvNdD2Vkplz74jzkA9-ziZsVsvBvm5lO9rff7zGEO3QW0flYF6606X5ouq2fUqHPM4fUI2pWlm~mIWTuhXJhlY1Ag5VfWRdvtuJwN3dQ9qb6wXN9S2yaLg9Pb0bZFumDWLTNCmHz12xkJfjCwxeExlrQb4KZW-newrJc4mDKsglHti-RldKQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA), which is the closest thing to a useful summary by people with a smidgeon of curiosity that I could find in this space.

Why is the naive view wrong? 

I’m not really impressed with the people working in this field. Most people don’t clearly say that excess winter deaths are a combination of season-related (from the flu) and cold-related (from cardiovascular) deaths, even though something like this has to be true. I can’t find anyone who says that flu seems to be a bigger deal in Africa than in Europe, even though something like that has to be true too. I can’t find anyone expressing even a smidgeon of curiosity about the Greenland question, which is why I had to cite a Greenland-specific journal from 1986 for the answer. A lot of these studies and analyses just take the temperature record from London and generalize. So I don’t want to say I 100% trust these people and the naive view is definitely wrong.

But some of these analyses do make a good point. Given that warmer cities have higher winter mortality than colder cities, it doesn’t seem likely that making the colder cities have more warm-city-typical temperatures will help very much. I find this hard to analyze because I still don’t really get why cold cities over-adapt and end up with even lower mortality than the warm ones.

We still don’t really understand why the flu is seasonal. But it doesn’t seem to be a direct effect of the cold and there’s no clear reason to think global warming will help.

Global warming _should_ theoretically help prevent the excess winter heart attacks, which are a direct effect of cold weather. But then why don’t we see any effect from excess winter heart attacks in very cold places like Stockholm or Siberia? Overall I’m not convinced of this one either.

Everyone says that global warming _will_ worsen mortality from heat. I’m a bit confused by this also, because just as hot places have worse cold-related mortality, [cold places have worse heat-related mortality](https://academic.oup.com/aje/article/155/1/80/134292). I can’t really find anyone taking this seriously and saying that, as colder cities get warmer, their heat-related mortality will decrease. 

One more thing: is all of this is mostly killing very frail people who are on the verge of death anyway? Like, with the heart attack victims - sure, if you have lots of risk factors, your inevitable heart attack is more likely to come on a cold day than a warm one. But it’s not like these people would live forever if the temperature stayed high, is it?

There’s a cute study to this effect by [Auliciems and Frost](https://link.springer.com/article/10.1007/BF01212767) modeling this as a “pool of susceptible individuals”. I think the idea is something like if an extreme weather event kills lots of people one year, the next year extreme weather events will kill fewer people than normal, because a lot of the vulnerable people are already dead. Their experiment finds some limited support for this hypothesis.

I’m going to end here - even though I don’t have a firm conclusion, I’m not going to be able to top a study on cold-related deaths by a guy named Frost.
