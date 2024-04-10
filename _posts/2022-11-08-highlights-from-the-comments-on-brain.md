---
title: "Highlights From The Comments On Brain Waves"
subtitle: "..."
date: 2022-11-08
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/83156610/comments?&all_comments=true
image: https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/2e93b9f7-17c8-42f5-a0a1-ccbb93ed4f2e_255x255.webp
original-url: https://www.astralcodexten.com/p/highlights-from-the-comments-on-brain
---
[original post [here](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain)]

* * *

**On What Kind Of Thing Brain Waves Are:**

Loweren [writes](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9874786): 

> In my undergrad biology program we visited a brain research lab near Moscow. The brain scientist gave us a brief intro to Fourier transforms, which made me understand how beautiful they are - something that 2 years of undergrad math classes didn't manage to do.
> 
> Then he explained the brain waves to us like this:
> 
> "Imagine you are standing outside the football stadium. You don't see what's happening inside, but you hear the chatter of the crowd. All the individual words blend together into indistinct mess and although there's definitely a local information transfer going on, from the outside you can't make out anything specific.
> 
> Then imagine one of the teams scored a goal. The crowd behavior is now very different! The fans of the winning team start to cheer and sing. You can easily pick this up from outside and infer what's happening. This is because the individuals behave in a globally coordinated manner, so their signals amplify each other in tune.
> 
> From this perspective, brain waves are a byproduct of globally coordinated neuronal activity, and it's the first one we historically learned to pick up. They appear when neurons stop chatting with each other and start chanting in unison."
> 
> Then he plopped some probes on my head and announced I have beautiful epileptic spikes (I'm not an epileptic)

* * *

**On Grandmother Neurons:**

Doug Summers Stay [writes](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9875103):

> I was in a workshop with some people who studied "Grandmother neurons." The story is that a particular neuron only fires when you see your grandmother. This is a false. The true story goes something like this: Imagine encoding memories as combinations of 88 piano keys (neurons). If you used a binary encoding, you could store 2^88 memories, but if you got one note wrong, it would be a totally different memory. If you stored one memory per key, you could only store 88 memories. The brain actually uses sparse codes-- a memory encoded as a chord, only using up to 10 keys played at once (since we only have 10 fingers) This can store "88 choose 10" which is about 4 billion memories. So when the scientists measure a hundred randomly sampled neurons, it just so happens that one particular neuron only participates in the chord for the grandmother in the tests. Does it participate in other chords? Yes, but they are all for images the scientist didn't test. Are there other cells involved in the chord for the grandmother? Yes, but the scientists didn't stick a measuring device next to those neurons (it's hard to do and if you stick in too many probes they damage the tissue).

NotPeerReviewed [asks](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9883988):

> I may be missing something - don’t all of these encoding schemes suffer from the “one note different means a totally different memory” problem?

Xpym [answers](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9885730):

> The natural solution would be to have similar chords refer to neighboring areas in the cluster of thingspace, like encodings for grandma and grandpa to differ by a single note.

NotPeerReviewed [says ](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9883988)“Kind of like word embeddings, then [-] that makes sense.” And gugu [says](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9875483):

> This also seems much more intuitive and efficient + it falls in line well with what apparently happens in Machine Learning for example in word encodings: Each word/concept will rather be represented by some vector in the space of activations, the "neurons"/dimensions themselves meaning different things.

* * *

**On Waves In AI:**

Mirrormere [writes](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9875170):

> Arguably, even AI models have "waves". It is just that with the currently dominant paradigm of transformer models there is only a single wave going from input to output and no oscillations or recurrences. This used to be different, recurrent models like LSTMs, Neural Turing Machines and other older ideas could be described as oscillating. It just turned out that these recurrent models are hard to train with current methods and to scale to large amounts of data. Interestingly, recurrent models are thought to be better at reasoning tasks and algorithmic learning, something that transformer models are bad at ("bad" here meaning in comparison to their other skills like memorization and language understanding).

And [Grum](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9877061):

> Any recurrent network definitely shows oscillatory behaviour - I used to train GRUs (simpler variant of lstm) a while back for sound generation. Part of the difficulty of using them was how unstable they could be - things would work really well for a few seconds, then just degrade into noisy or weird feedback loops..showing classic chaotic behaviour. I managed to get some small ones running in realtime on fft data, with live input bled in from a microphone and the state feeding back into itself. You could drive it in and out of different stable points with different inputs, much like microphone feedback in a room if you've ever played around with that.
> 
> I think this is prevalent in almost any recurrent system, which raises the question of how our brains don't just collapse into noise or get stuck in endless loops...they're kind of finely balanced to be able to skirt around the edges of various attractors, moving from place to place.

[B Civil](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9882215):

> _> which raises the question of how our brains don't just collapse into noise or get stuck in endless loops..._
> 
> I would submit that this does happen with some people. Think obsessive/compulsive behavior and other kinds of neurosis.
> 
> What’s that tune you can’t get out of your head?
> 
> I have no scientific knowledge on this subject but in it’s broad terms it makes intuitive sense to me.

* * *

**On The Case Against Brain Waves Being Important**

Justin L [writes](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9878202):

> Hey all. - I'm a working neuroscientist who's spent some time thinking through some of these issues.
> 
> I would say that there's a significant proportion of the field that is, shall we say, "skeptical" of the Buzsaki-style view on oscillations. Everyone agrees that the oscillations exist, and that changes in the oscillations are often correlated with changes in brain state, but making *causal* statements about their impact has proven much more difficult. There are certainly some suggestive data in the hippocampus pointing towards the importance of things like theta-band power and sharp wave ripples, but even there you get inconvenient data points like the fact that bats have a completely normal, functioning hippocampus with no apparent theta band oscillations: <https://www.sciencedirect.com/science/article/pii/S0092867418312297>
> 
> More broadly, it's hard to shake the feeling that the brain has some natural resonances for various states - sleep/unconsciousness is low frequency, low activity is ~alpha/beta, high activity is ~gamma. A statement like:
> 
> "Ask someone to think about a certain topic, and cells representing that topic will form a neuronal assembly (ie they will start oscillating together at the same frequency) in gamma rhythm."
> 
> is really just saying that those cells are active, and neurons in an active brain area tends to follow a gamma rhythm. In fact, I'm reasonably confident that if you were to look at the internal activity of cells in the same area that do NOT represent that topic, they would also be following the same gamma rhythm, just with less tonic input and thus less spiking activity.
> 
> People like to study oscillations because they're brain-wide phenomena that are (relatively) easy to detect in humans with non-invasive methods like EEG. However, anyone who's looked at neural activity using more finely-tuned, invasive methods (e.g. single neuron electrophysiology) knows that individual neurons close by each other can be tuned to very different sets of variables, and that when you average signals from large populations of neurons you lose a lot of useful information.
> 
> To be clear, I think everyone in the field agrees that neurons act together in assemblies, that patterns of activity that are shared across neural populations are important, and that sometimes these population patterns of activity can oscillate. The problem is that there are many, many, many of these subnetworks active at any given time, and that when you average them all together you get a signal that's easy to measure, but is limited in its ability to explain anything beyond basic brain function. You have 86 billion neurons in your brain. You should be skeptical of theories that tell you just 4-5 frequency bands are the secret to understanding it.

[Excavationist](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9881369):

> Thank you for writing this so that I didn't have to.
> 
> One thing I might add: it's very difficult for me even to imagine how a network of interconnected neurons, some of which are spontaneously active, could fail to give rise to oscillations. This to me is the best reason to think that EEG signals don't have much explanatory power over and above the neuronal spikes upon which they supervene.
> 
> One last point of clarification that may be helpful to non-neuroscientists: it may be useful to distinguish "brain rhythms" at different levels of analysis. I can imagine someone reading this and thinking that hippocampal theta is pretty much like visual cortex event-related potentials (ERPs). These are completely different phenomena measured using completely different methods! Hippocampal theta is measured as a local field potential (LFP), which usually means actually sticking electrodes in the brain and then low-pass filtering the signal. One step up from that is intra-cranial EEG, in which electrodes are placed on the surface of the cortex (in neurosurgical contexts). And finally you have good old-fashioned EEG, where you wear a cap over the head, like in a psychology lab, and measure electrical signals that originate over many centimeters and are difficult/impossible to conclusively localize. This is where people see ERPs.
> 
> I'm not a reductionist at all costs by any means, but generally I think it's safe to say that the actual causal relevance of each of these "rhythms" decreases as you ascend the hierarchy. Hippocampal LFP stands out as potentially interesting because of phenomena like phase precession of place cells, but Justin L aptly points out that this is by no means a necessary feature of place coding in general.

[Paul B](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9881301):

> _> Everyone agrees that the oscillations exist, and that changes in the oscillations are often correlated with changes in brain state, but making *causal* statements about their impact has proven much more difficult._
> 
> One argument I heard against this that struck me went along the lines of: "People have this gripe about oscillations being causal and many intuitively see oscillations as epiphenomenal. However, the same people take, at face value, that increases in brain activity has causal effects. Why is this? There is no stronger philosophic argument for activations rather rather than oscillations

Justin L [again](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9954603):

> So, it's relatively easy to show how activity in motor areas causally leads to changes in muscle activity / movement. And, more generally, if Neuron A is synaptically connected to Neuron B, we have a very rich understanding of the electrical and molecular mechanisms that explain why an increase in activity of Neuron A causally increases the probability of activity in Neuron B. In so far as a mind is the product of 100 trillion neural connections, we know that each of those individual connections represents a causal chain that propagates increases in brain activity. There's lots of other very suggestive evidence, but these basic facts are, I think, why most neuroscientists feel comfortable hanging their hats on the idea that changes in behavior are tied to changes in neural activity somewhere.
> 
> In contrast, the structures of neural oscillations are (in most cases) set by emergent properties of densely connected neural networks. There's been amazing progress in trying to model these kinds of networks, but in truth we're still in the pre-statistical-mechanics era of neuroscience. We know a lot about individual neurons and neural connections, but we still don't have a well-accepted theoretical framework that allows us to understand how large populations of neurons interact and compute. This ignorance makes it hard to make confident statements about the causal impact of oscillations, or really of any other network-level phenomenon.
> 
> The philosophic argument for neural activation is that we understand its causality in very simple networks. The argument against oscillations is simply a lack of evidence, pending better models of network activity.

* * *

**On Other Things That Aren’t Named For The Reason You Think:**

Larry Baum [writes](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9885277):

> In an analogy to the origin of the names of white, pink, and brown noise, the laboratory technique to separate and study DNA of different lengths is named southern blotting for its developer, Ed Southern. The similar method of separating RNA is called northern blotting, and for protein it's called western blotting. Once, I accidentally reversed the electrodes when doing a western blot, so that the protein ended up lost in the buffer instead of on the blot paper, which I guess could be an eastern blot. But apparently there are many things called eastern blots now: <https://en.wikipedia.org/wiki/Eastern_blot>

The subreddit people have more examples of this, for example [ulyssessword](https://www.reddit.com/user/ulyssessword):

> “Schwarzschild" translates from German as "Black Shield", and the [Schwarzschild radius](https://en.wikipedia.org/wiki/Schwarzschild_radius) is the size of the event horizon surrounding a black hole. It is named after Karl Schwarzschild, who was the first to describe it mathematically.

And [DizzleMizzles](https://www.reddit.com/r/slatestarcodex/comments/y98gwb/book_review_rhythms_of_the_brain/it5dewy/):

> The vector describing the direction in which an electromagnetic field's energy flow is pointing is called the Poynting vector, after John Henry Poynting.

* * *

**On Other Interesting Facts About Brain Waves:**

Kevin Binz [writes](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9876060):

> You've hit on my favorite topic! I too found his stuff on pink noise difficult to parse.
> 
> Brain waves become significantly more exciting when you do a deep dive into specific oscillators.
> 
> 1\. Sharp-wave ripples (SWRs, 80-140 Hz) play an essential role in memory recall.
> 
> > Girardeau et al (2009) provides loss of function evidence that suppression of sleep SWRs dramatically impairs subsequent memory recall for spatial tasks. This finding is nicely complemented by several gain of function experiments. Fernandez-Ruiz et al (2019) were able to prolong ripple duration, and showed that prolongation improved performance, and conversely that shortening impaired performance. This may explain why novel situations naturally evince longer duration ripples.
> 
> <https://kevinbinz.com/2021/12/30/sharp-wave-ripples-and-memory-retrieval/>
> 
> There's a longer version of this video in supplementary materials of the paper.
> 
> 2\. The SPEAR model, which associates peak of theta wave with past encoding vs trough with future predictions is one of the most extraordinary facts I know.
> 
> <https://kevinbinz.com/2021/12/09/the-theta-gamma-neural-code/>
> 
> 3\. The link between respiration-entrained rhythms and volition.
> 
> <https://kevinbinz.com/2022/07/24/the-rhythms-of-anxiety/>
> 
> 4\. How gamma-beta implement feedforward and feedback signals (in shallow and deep layers of cortex respectively), fully consistent with active inference models. Very strong recommendation for Earl Miller's laboratory. 

* * *

**On Phi:**

Measure [writes](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9879264):

> Instead of 2.17, the golden ratio φ=1.618... is best for anti-resonance. This is because φ is maximally difficult to rationally approximate.

And Drake Thomas [explains](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9883829):

> Every real number can be approximated by an ever-closer series of rationals, since the rationals are dense in the real numbers (e.g. the square root of two is approximated by the fractions 1/1, 14/10, 141/100, 1414/1000, 14142/10000, ...). The question is how good of an approximation you can get for rational numbers with denominators up to some bound.
> 
> This turns out to be related to the size of the terms in the continued fraction expansion of a number - larger terms in the continued fraction expansion yield better approximations of your chosen value. (The unusually-good-for-its-complexity rational approximation of pi as 355/113 exists because of an unusually large term early in the continued fraction expansion of pi as [3; 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, ...]. If we round the 1/292 term portion of the continued fraction to zero, we get 3+1/(7+1/(15+1/1)) = 355/113.)
> 
> The golden ratio's continued fraction expansion is all 1's, so in this sense it has the worst rational approximations of any real number. In practice, people tend to care about the asymptotics of this approximation quality, which leads to the notion of <https://mathworld.wolfram.com/IrrationalityMeasure.html>. More concrete implications between the terms of the continued fraction and the badness of rational approximations in this sense are mentioned at this MathOverflow thread: <https://mathoverflow.net/questions/89600/numbers-with-known-irrationality-measures>

* * *

**On Conduction Delay In Silico:**

Jared [writes](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9876571):

> _> And the waves solve wetware-specific problems, like conduction delay (silicon chips operate at the speed of light) and synchronization (computers have internal clocks, or can synchronize with atomic clocks via the Internet)._
> 
> Silicon chips definitely deal with conduction delay. The speed of light is very fast, but at 4 GHz electric signals (moving at roughly 2/3 the speed of light) can only travel 5 cm in one clock cycle. Traveling 1 cm uses 20% of the cycle, etc. Computers also have to deal with various types of synchronization issues for a variety of reasons.
> 
> However, the logic here was flawed from the start, because artificial neural networks are a mathematical model simulated on a computer and the properties of the computational substrate of a simulation don't carry through into the simulation. And so ANNs indeed do not have to deal with conduction delays and synchronization issues the same way that biological neural networks do, but the reason does not have anything to do with the low-level details of silicon chips.
> 
> In an ANN, there is simply a list of neurons, a record of which neurons are connected to which others, and an assignment of weights to these connections. There is normally not an assignment of lengths to the connections. Therefore there can be no conduction delay, for example. You could create a nonstandard ANN with lengths and simulated conduction delays if you wanted, as that freedom is the nature of simulation. The conduction delays in the wires within the silicon chip don't inherently create conduction delays in the ANN, because the connections in the ANN are not wires in the ANN, they are numerical data upon which the silicon chip performs calculations. Just like the flatness of the silicon chip doesn't prevent simulated 3D environments, etc.
> 
> This may seem piddly, but it's important to keep in mind that the properties of an ANN come from the properties of the mathematical model, not from the properties of wiring in silicon chips.

* * *

**On Synchrony**

FeepingCreature [helps me understand the synchrony perspective](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9883719):

> I guess it makes sense to me as a clock. You have your neuronal system, you do a thought, the thought gets fed to the output of your cluster, and then you you briefly force all neurons to high so they get dampened to zero, refreshing the state for the next thought cycle.

Alexander Buhl [describes an even more unexpected domain that this is like](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9884346):

> Delays that need to be combined into a coherent whole is the entirety of multiplayer game network coding. People clicking buttons, sending them with variable delays along with a "happened at time t" attached to a server which then has to retroactively figure out who hit and who missed and then send that back in time. Ask game network engineers for a books worth of problems and solutions over the last 40 years :)
> 
> Games also use frames, discreet moments in time, to make physics and simulations doable at all. Too low a framerate and you notice the choppiness. Also if your monitor frequency and game frame frequency are nice multiples, it looks good, if not, it's choppy as well. Many analogues!

* * *

**On Buzsaki’s Next Book:**

Grum writes:

> [RotB author Gyorgy Buzsaki’s new] book seems to get at the idea that the brain is a self-coherent system, which is stable in and of itself without needing to be "driven" by sensory events. Anyway the summary [here] can do a better job than me, for the lazy its all summarised from about 1:02
> 
> <https://brainsciencepodcast.com/bsp/2020/172-buzsaki>

* * *

**On Crypto:**

Scroobius [writes](https://astralcodexten.substack.com/p/book-review-rhythms-of-the-brain/comment/9958078):

> An idea I've toyed around with is the idea of "blockchain protocols as the clock rhythm for distributed consciousness"
> 
> Like, you've got a bunch of computers running the same algorithm. Every so often, a new block gets pushed to the chain, and becomes common knowledge. This constitutes one "frame" of distributed consciousness, and contains some kind of consolidation or average of the input of all the constituent nodes.
> 
> Inside those nodes, you can have arbitrary subroutines operating in parallel wavelengths, but the outermost blockchain is like a [conductor | yearly census | drummer boy's marching beat | pulse | bible]

A while back, I was trying to think of what kind of object could match our intuitive understanding of conscious identity. It’s not matter, because all the atoms in our body get replaced once every whatever, but we still think of ourselves as the same people. It’s not information, because even if 6-year-old-me and 6-year-old-you are more similar than 6-year-old-me and adult-me, 6-year-old-me and adult-me are still the same person, and 6-year-old-me and 6-year-old-you aren’t. Whatever kind of object we are needs to satisfy a bunch of seemingly impossible desiderata, like “it’s not material”, “it’s not information stored in any particular location”, “it’s forced to point to a single unique spot”, “the pointer remains the same even when the object at the spot changes”, etc.

The only thing I can think of that satisfies all of those properties is an NFT. I think the simulators created our universe as a framing device for a limited edition of 100 billion NFTs representing different humans. Humans with rare features like red hair or heterochromia cost more. If a human achieves some kind of amazing accomplishment, their value goes up, so you can buy ones who you think are undervalued and make money later.

I was saving this one for another Bay Area House Party post, but you can have it now.
