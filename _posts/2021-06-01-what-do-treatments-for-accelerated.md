---
title: "What Do Treatments For Accelerated Aging Tell Us About Normal Aging?"
subtitle: "We can prevent young people from being old, but preventing old people from being old sounds also sounds useful."
date: 2021-06-01
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/37057161/comments?&all_comments=true
image: https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/19911f4c-d6cc-45f4-9735-98f1ab38e23a_736x490.jpeg
original-url: https://www.astralcodexten.com/p/what-do-treatments-for-accelerated
---
Progeria is a rare disease that makes people age unnaturally quickly. Babies born with progeria can lose their hair in toddlerhood, get wrinkles by grade school age, and die - apparently of old age - in their early teens. You can see a picture of a progeroid child [here](https://en.wikipedia.org/wiki/Progeria), though I don't recommend it.

There's been a lot of research on one important form - Hutchinson-Gilford Syndrome - and just last year, the FDA [approved the first treatment](https://www.fda.gov/news-events/press-announcements/fda-approves-first-treatment-hutchinson-gilford-progeria-syndrome-and-some-progeroid-laminopathies), a drug called lornafarnib. In the study, a few hundred children averaging around 7 years old took the drug for two years; 3% died during that time. In an ad hoc group of untreated comparison children, about 30% died during the same period. I'm a little confused by the methodology - it seems like the "comparison children" were chosen partly because they died too early to get into the trial, which sounds like a pretty major confounder - but everyone seems to treat this as reasonable so I will assume they adjusted for this in some way. If that's true, then lornafarnib cuts mortality by 90%.

That's great for the 300 or so children worldwide with Hutchinson-Gilford progeria (it's a really rare disease). But none of the discussion about this answered the question I wanted to know: can lornafarnib also prevent normal aging?

After looking into this more, I find some evidence the the answer is no, but also some reasons why maybe it's less clear cut than that?

Hutchinson-Gilford progeria (I'll just say "progeria" from here on, even though that's kind of inaccurate) is what's called a laminopathy. It's a disease of the _nuclear lamina_ , a weblike structure that helps support and give shape to the cell nucleus. The lamina is partly made of a protein called lamin A. Children with progeria have a mutation in the relevant gene; instead of producing lamin A, they produce a defective mutant protein called progerin. The cell tries to build the nuclear lamina out of defective progerin instead of normal lamin A, and as a result the cell nucleus is screwed up and can't maintain a normal shape.

So then aging happens? My sources don't seem to have a great explanation of this. The [UniProt database](https://www.uniprot.org/uniprot/P02545#:~:text=Prelamin%2DA%2FC%20can%20accelerate,genomic%20instability%2C%20and%20premature%20senescence) says that this "acts to deregulate mitosis and DNA damage signaling, leading to premature cell death and senescence". [This paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2765059/) goes a little further, saying that the screwiness in the nuclear lamina prevents DNA repair proteins from doing their job.

Many different processes cause aging, but one of those processes is accumulation of DNA damage. Sometimes this makes cells do their jobs less well. Other times it shifts them into a state euphemistically termed "senescence", where they realize something is wrong, chemically "scream" for the immune system to come kill them, but the immune system is overtaxed and so they just sit there screaming out more and more chemicals and poisoning everything around them. 

So a unified theory of progeria goes: the lamin mutation causes accumulation of defective protein in the nucleus, preventing DNA repair. This makes people accumulate DNA damage faster, and since DNA damage is a major cause of aging, it makes these people age more quickly.

Lornafarnib interferes with the production of the defective progerin protein. As best I can tell, it doesn't cause the cell to produce healthy lamin A - it just prevents the defective mutant version from accumulating. For whatever reason, the cells without lamin A do surprisingly okay as long as they don't have the defective mutant version. So this prevents most of the DNA repair problems, and so decreases premature aging.

All of this suggests lornafarnib shouldn't help prevent normal aging. After all, normal aging is caused by lots of processes including gradual expected accumulation of DNA damage - not just the downstream effects of one weird mutant protein.

...except that in doing this research I kept finding people saying that maybe some of aging is caused by this one weird mutant protein. I don't claim to fully understand [Scaffidi and Misteli](https://pubmed.ncbi.nlm.nih.gov/16645051/), but they write:

> Age-related nuclear defects are caused by sporadic use, in healthy individuals, of the same cryptic splice site in lamin A whose constitutive activation causes [Hutchinson-Gilford progeria]. Inhibition of this splice site reverses the nuclear defects associated with aging. These observations implicate lamin A in physiological aging.

[Musich and Zou](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2765059/) write, in a way that doesn't quite let me trace back their reasoning:

> It is quite likely that the same sporadic abnormal splicing of prelamin A mRNA is responsible for the genome instability in both HGPS and normal aging.

I don't really get what's going on here. I know that often, as age-related damage degrades DNA, a lot of weird malformed proteins pop up and accumulate - for example, the [beta amyloid plaques](https://en.wikipedia.org/wiki/Amyloid_beta) that might (or might not) be involved in Alzheimers. Maybe progerin is one of these proteins and causes some of the problems commonly associated with aging? But what percent of the problems? If it and 99 other defective proteins each cause 1%, not really a big deal. If it's 50%, bigger deal - but nothing is ever that easy.
