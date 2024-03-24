---
title: "[LINK] Unifying Predictive Coding With Backpropagation"
date: 2021-04-14
likes: 46
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/35138549/comments?&all_comments=true
image: https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/45478ba7-4e2e-4a8e-97d6-2bba593704db_1053x632.png
original-url: https://www.astralcodexten.com/p/link-unifying-predictive-coding-with
---
_[epistemic status: I know a little about the predictive coding side of this, but almost nothing about backpropagation or the math behind the unification. I am posting this mostly as a link to people who know more.]_

This is a link to / ad for a great recent Less Wrong post by lsusr, [Predictive Coding Has Been Unified With Backpropagation](https://www.lesswrong.com/posts/JZZENevaLzLLeC3zn/predictive-coding-has-been-unified-with-backpropagation), itself about a recent paper [Predictive Coding Approximates Backprop Along Arbitrary Computation Graphs](https://arxiv.org/pdf/2006.04182.pdf).

Predictive coding is the most plausible current theory of how the brain works. I’ve written about it elsewhere, especially [here](https://slatestarcodex.com/2017/09/05/book-review-surfing-uncertainty/).

Backpropagation is an algorithm involved in most modern machine learning / AI. If you create a neural net and “train it” by feeding it problems and answers, the backpropagation algorithm tells you how to make the answers “flow backward” through the model to produce the set of weights that would have made the model predict them. Hopefully this makes the model generally good at solving that class of problem, and then you can feed it new problems you want it to solve.

We’re pretty sure the brain doesn’t directly use backpropagation. Real backpropagation requires, well, propagation going backwards. But neurons can only send information one way; Neuron A sends to Neuron B, but not vice versa. On the other hand, the brain seems to do a lot of the same things artificial neural networks do, with a suspiciously similar structure. So researchers have long suspected the brain was doing some kind of approximation of backpropagation that ended up in the same place.

A series of [recent](https://watermark.silverchair.com/neco_a_00949.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAnwwggJ4BgkqhkiG9w0BBwagggJpMIICZQIBADCCAl4GCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM-4CKWKZ4c-N3hFz0AgEQgIICL70v4JRKExQc5I8hdYX3OrvGuGu5nQTPpyb_G7COCYtyFKvQEr2Iru-VG2fY_tzv0SiIpKT-inlaWLDWSWBipcxEwpnMESEFu-URDp4_yk2NREeUUjdktK8TZy_-S_jgy50hZlIsNQccEpKmpDp5eXW3QX6Sbcqq8gRY5_nlPSsZN_Re7FPzNZl7cq8mHzk5uXZtBZdE5YqSrtfeLv8ZH5nC71wzfwKByGkTJH7XIqBJc9KFKz0h06-CYSRv-x7bANKwrrD7K88Wi4IGZ0SsOt1r7qtwuoS7h0YuE_KxK3pDNPTeqOerPZijIRn3D0x_MFcUIig_1PQjCDZAnalwAzRAxRGMlUC44NQfBRDXuA1Ticp5z_UJkp2njaMO4gkmAoND0f6OqAr9rVd__0wTKHdNVXPuO6PbSRxcRbrBGC5FPlQ4Xx_UN5vmdSZvKpVxpJf3-M55x-XSrAEJars1ODElwmspnZuLu0prCPZSALDNkS2IJ7eX5Jp-Uu_fY1WYB4RMBuZ9gkk7zKbkwmraEFhTozgLoURvzeEmohD8JNCQxRUOEoXnzRHUKLRvBhjXIWZkaMUDqC2M8R7DUSQlBE4FBH1L7p9W9E3iR1_DS6Akj-JOSxEqFBxPPKNdK2MEgzhEdMyTt-6x19pH7_kPPjk7sFRcA2bdxlGEHjx9KWYQb9U0zVEf4ZvODsNr-NGYIfeh48iEHJS2G9bBj8g2ot5YTGzq2l0z9vKcSaUM31M) [papers ](https://papers.nips.cc/paper/2018/file/1dc3a89d0d440ba31729b0ba74b93a33-Paper.pdf)helps flesh this out. Predictive coding can approximate backpropagation without needing backwards information transfer. The [most recent paper](https://arxiv.org/pdf/2006.04182.pdf) shows that you can do this for arbitrary computational graphs. lsusr [writes](https://www.lesswrong.com/posts/JZZENevaLzLLeC3zn/predictive-coding-has-been-unified-with-backpropagation):

> There are two big implications of this.
> 
>   * This paper permanently fuses artificial intelligence and neuroscience into a single mathematical field.
> 
>   * This paper opens up possibilities for neuromorphic computing hardware.
> 
> 


I’m not sure I am as excited as they are; AI and neuroscience have always been a single field in some spiritual sense, and they continue to be very different fields in practice. And I’m not sure what good more neuromorphic computers would be - lsusr suggests “a computer that doesn’t break when you cut it in half”, but it sounds easier to just avoid letting your computer end up in a situation where that might matter.

But there’s been a debate over how much existing neural nets are already pretty similar to the brain, vs. the brain is doing fundamentally more advanced things that we don’t understand at all. This line of research provides some evidence that artificial and natural intelligence are already more similar than we thought.

The paper: <https://arxiv.org/pdf/2006.04182.pdf>  
The article: <https://www.lesswrong.com/posts/JZZENevaLzLLeC3zn/predictive-coding-has-been-unified-with-backpropagation>
