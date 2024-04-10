---
title: "Your Book Review: Why Machines Will Never Rule the World"
subtitle: "Finalist #3 in the Book Review Contest"
date: 2023-06-03
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/123527301/comments?&all_comments=true
image: https://substack-post-media.s3.amazonaws.com/public/images/0429f7b4-63dd-406d-84a7-eaa0cc8d21fd_1000x667.jpeg
original-url: https://www.astralcodexten.com/p/your-book-review-why-machines-will
---
[_This is one of the finalists in the 2023 book review contest, written by an ACX reader who will remain anonymous until after voting is done. I’ll be posting about one of these a week for several months. When you’ve read them all, I’ll ask you to vote for a favorite, so remember which ones you liked_]

I'll begin with a contentious but invariably true statement, which I've no interest in defending here: new books—at least new nonfiction books—are not meant to be read. In truth, a new book is a Schelling point for the transmission of ideas. So while the nominal purpose of a book review like this is to answer the question _Should I read this book?_ , its real purpose is to answer _Should I pick up these ideas?_

I set out to find the best book-length argument—one that really engages with the technical issues—against imminent, world-dooming, Skynet-and-Matrix-manifesting artificial intelligence. I arrived at _Why Machines Will Never Rule the World_ by Jobst Landgrebe and Barry Smith, published by Routledge just last year. Landgrebe, an AI and biomedicine entrepreneur, and Smith, an eminent philosopher, are connected by their study of Edmund Husserl, and the influence of Husserl and phenomenology is clear throughout the book. (“Influence of Husserl” is usually a good enough reason to stop reading something.)

Should you read _Why Machines Will Never Rule the World_? If you're an AI safety researcher or have a technical interest in the topic, then you might enjoy it. It's sweeping and impeccably researched, but it's also academic and at times demanding, and for long stretches the meat-to-shell ratio is poor. But should you pick up these ideas?

My aim here isn’t to summarize the book, or marinate you in its technical details.[ ATU 325](https://en.wikipedia.org/wiki/The_Sorcerer's_Apprentice) is heady stuff. Rather, I simply want to give you a taste of the key arguments, enough to decide the question for yourself.

The authors thoroughly and commendably engage with a breadth of literature in physics, biology, linguistics, philosophy of mind, AI, and more, including up-to-the-moment deep learning research, and they collect many of the existing arguments against artificial general intelligence, notably Toby Walsh’s “[The Singularity May Never Be Near](https://arxiv.org/abs/1602.06462)” and Erik J. Larson’s _[The Myth of Artificial Intelligence](https://www.amazon.com/Myth-Artificial-Intelligence-Computers-Think/dp/0674983513)_.

Landgrebe and Smith don’t deliver their argument proper until Chapter 7, but they’re merciful enough to lay out its bones in the Foreword. Here’s a condensed version:

  1. Building artificial general intelligence requires emulating in software the kind of systems that manifest human-level intelligence.

  2. Human-level intelligence is the result of a complex, dynamic system.

  3. Complex systems can’t be modeled mathematically in a way that allows them to be emulated by a computer.

  4. Therefore, AGI—at least by way of computers—is impossible.




And by impossible they really mean it. A solution “cannot be found; not because of any shortcomings in the data or hardware or software or human brains, but rather for _a priori_ reasons of mathematics.”

Landgrebe and Smith proceed to spend a lot of time considering what human-level intelligence actually _is_. They define artificial general intelligence “as an AI that has a level of intelligence that is either equivalent to or greater than that of human beings or is able to cope with problems that arise in the world that surrounds human beings with a degree of adequacy at least similar to that of human beings.”

Intelligence itself is a little trickier, and the authors consider many definitions. Drawing from Husserl and Max Scheler, they make a point of distinguishing between two aspects of intelligence: what they call _primal_ and _objectifying_ intelligence. 

Primal intelligence occurs in humans and non-humans, and enables learning, allowing higher animals to adapt to new situations.

Objectifying intelligence is what sets humans apart from dolphins, beavers, and elephants. “Objectifying intelligence allows _homo sapiens_ to disengage himself from his environment in a way that allows him to see himself, other human beings, and the elements of this environment (both biological and non-biological) as objects, each with its own trajectory and its own array of properties and causal powers.”

This objectifying intelligence is what enables the capabilities we like to think of as unique to our species: long-term planning, abstraction, introspection, etc. 

The authors give special attention to language, and they go so far as to argue that mastery of language is both necessary and sufficient for AGI.

After a lengthy discussion of material monism, of the properties of the human mind, of sociolects and cognolects, the authors finally arrive at the argument proper.

## The Ghost of Friedrich Hayek

Complex systems are hard to make sense of, and many of its purveyors are awfully breezy when moving between well-founded technical assertions and statements of a much more speculative nature. It helps to first consider what _isn’t_ a complex system.

If you’re a physicist or engineer, your daily bread is a chunk of reality that’s amenable to mathematics. This chunk has certain regularities, symmetries, equilibria, etc., that allow you to describe it with differential equations and make predictive statements. The authors call systems of this sort “logic systems,” and our mastery of these systems “has changed our world and created the technosphere within which we live today.” Crucially, systems from this chunk of reality have fixed boundary conditions: you can pick a system out from the universe and consider it in isolation, because nothing without governs the motion within. Think clockwork and Isaac Newton.

But many systems that occur in nature, including almost all of the biological systems in living organisms, don’t have these nice properties. And it’s to these we give the name “complex.” It’s not that the math stops working, it just no longer describes the system in full, and our ability to make predictive statements starts to curdle.

Examples from chaos theory are often the most intuitive, like the[ double pendulum](https://en.wikipedia.org/wiki/Double_pendulum) or the[ three-body problem](https://en.wikipedia.org/wiki/Three-body_problem). Other examples are weather, pharmacodynamics, and the economy. A favorite of physicists is[ turbulence](https://en.wikipedia.org/wiki/Turbulence), of which Werner Heisenberg is reputed to have said: “When I meet God, I am going to ask him two questions: Why relativity? And why turbulence? I really believe he will have an answer for the first.”

There is an irreducible quality to complex systems; the only way to model them properly is with the systems themselves. When you think of complex systems, think of John Muir: “When we try to pick out anything by itself, we find it hitched to everything else in the universe.”

Landgrebe and Smith argue that the “mind-body continuum” is a complex system. It’s a dynamic negentropy-hunter built out of feedback processes at every scale. The human brain is not a computer, and no known mathematics can describe it in full.

## The Ghost of Alan Turing

Arguments about computability aren’t new, and have fallen out of favor with many AI researchers. Landgrebe and Smith’s contention that the brain isn’t a Turing machine is reminiscent of Hubert Dreyfus’ _[What Computers Can’t Do](https://www.amazon.com/What-Computers-Still-Cant-Artificial/dp/0262540673) _and Roger Penrose’s _[Shadows of the Mind](https://www.amazon.com/Shadows-Mind-Missing-Science-Consciousness/dp/0195106466)_ , both of which the authors discuss.

They don’t mince words here; in their view, the belief that the brain operates like a computer, “though it is still embraced explicitly by some of our best philosophers, betrays on closer analysis ignorance not only of the biology of the brain but also of the nature of computers.”

[Universal Turing machines](https://en.wikipedia.org/wiki/Universal_Turing_machine) can compute all computable functions, but there’s an uncountable infinity of non-computable functions.

Any intelligence we program into a computer must necessarily be instantiated by executing a collection of computable functions. Even if it’s being used to approximate complex systems, an algorithm on a computer can only emulate logic systems. Anything executed on a computer by definition “becomes a process of the logic system which is the computer itself, which is realised in the way the binary logic of the microprocessors and other components of the computer operate.”

We could illustrate with examples like the _[Entscheidungsproblem](https://en.wikipedia.org/wiki/Entscheidungsproblem)_ , but it might be more intuitive (if less precise) to point out that computers can’t actually use real numbers (instead relying on monstrosities like[ IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)).

Put another way, computable algorithms are a subset of all the algorithms that can be formulated with known mathematics, and algorithms that describe complex systems like the brain exactly and comprehensively are outside of the set of known mathematics.

## The Ghost of Hans Moravec

One counterargument is that if intelligence is at its core about information processing, it doesn’t seem like there should be any theoretical barrier to emulating a human brain _in silico_. A network of 86 billion neurons and 100 trillion synapses seems within reach of current hardware trends.

A popular way of reasoning about the future of AI is to consider human computational capabilities, an argument from [biological anchors](https://astralcodexten.substack.com/p/biological-anchors-a-trick-that-might). But these arguments about biological computation often implicitly assume some isomorphism between, e.g., biological neurons and artificial neurons.

There’s a level of feedback and complexity in biological brains completely absent from artificial neural networks. A single neuron has 100,000 different types of RNA molecules. Researchers have tried to use entire artificial neural networks to [model the computations of just one biological neuron](https://www.quantamagazine.org/how-computationally-complex-is-a-single-neuron-20210902/).

So is 86 billion the right number to be thinking about? Is it right to think about a number? The 1-millimeter roundworm _Caenorhabditis elegans_ has only 302 neurons—its entire connectome mapped out—and we still can’t model its behavior.

To return to complexity, the systems composing intelligence are _non-ergodic_ (they can’t be modeled with averages), and _non-Markovian_ (their behavior depends in part on the distant past). Each property presents insurmountable challenges to modern artificial neural networks, which are based upon statistical inference.

These complex systems can’t be modeled by artificial neural networks and deep learning techniques; they yield no distribution “from which one could draw adequate samples because novel behaviour can emerge at every stage, thereby creating input-output-tuples from a constantly changing, evasive distribution.”

Landgrebe and Smith don’t argue against _narrow_ AI, predicting that narrow AIs are in the process of transforming our lives and will “deepen and enhance the technosphere to an enormous extent.” But superintelligence isn’t what we’ll have to contend with.

## The Ghost of Winston Churchill

A counterargument of a very different sort, a kind of “outside” argument more against the title and mood of the book than its text, is that machines _already_ rule the world. How much of your perception is steered by social media? To what extent have you been programmed—not by another human or in any conspiratorial sense, but by a complex series of unthinking algorithms? None of this is a new idea. Here’s Winston Churchill, in 1925:

> Public opinion is formed and expressed by machinery. The newspapers do an immense amount of thinking for the average man and woman. In fact they supply them with such a continuous stream of standardized opinion, borne along upon an equally inexhaustible flood of news and sensation, collected from every part of the world every hour of the day, that there is neither the need nor the leisure for personal reflection. All this is but a part of a tremendous educating process. But it is an education which passes in at one ear and out at the other. It is an education at once universal and superficial. It produces enormous numbers of standardized citizens, all equipped with regulation opinions, prejudices and sentiments, according to their class or party. It may eventually lead to a reasonable, urbane and highly serviceable society. It may draw in its wake a mass culture enjoyed by countless millions to whom such pleasures were formerly unknown. We must not forget the enormous circulations at cheap prices of the greatest books of the world, which is a feature of modern life in civilized countries, and nowhere more than in the United States. But this great diffusion of knowledge, information and light reading of all kinds may, while it opens new pleasures to humanity and appreciably raises the general level of intelligence, be destructive of those conditions of personal stress and mental effort to which the masterpieces of the human mind are due.

We already mediate an increasing proportion of human affairs through an increasingly opaque and uninterpretable software layer. We don’t need AGI to create new decision loops that outpace human capabilities or strip out the engineering redundancies of civilization. We may yet till our way into a cognitive dust bowl.

## The Ghost in the Machine

I came away from the _Why Machines Will Never Rule the World_ much less convinced than Landgrebe and Smith would like me to be. Whether or not Turing machines can emulate general intelligence is an open question. (The Church-Turing-Deutsch principle, for example, states that if quantum mechanics is sufficient to describe reality then quantum __ computers can emulate all physically realizable processes.) Whether or not there exists a mathematics that can fully model complex systems is an open question. The brain is managing more than just intelligence, and it's unclear how many of its processes would need to be emulated to model intelligence alone. Landgrebe and Smith rest very strong conclusions atop strong but leaky propositions.

For all the effort they spend expounding on the complexity and importance of human language, it’s worth asking how today’s large language models are doing. They’ve taken down syntax, semantics is falling, and [pragmatics may or may not be on the way](https://arxiv.org/abs/2210.14986). Despite what you might read online, AI researchers have worked hard to[ consider lessons from linguistics](https://arxiv.org/abs/2207.02098). There’s no stronger proof than “[and yet it moves](https://en.wikipedia.org/wiki/And_yet_it_moves).”

But I do think there’s something to the complexity and computability arguments. What level of innovation is required to create a general intelligence of the Skynet-and-Matrix-manifesting kind? Is it just a matter of scaling up current methods and hardware? Do we need new algorithms? New paradigms? Mathematical innovations as revolutionary as the differential calculus? Wetware? Hypercomputation?

In physics, exponential curves always turn out to be S-shaped when you zoom out far enough. I’m not sure anyone’s in a position to say when we’ll reach the upper elbow of the current deep-learning-fueled boom. Moore’s law isn’t quite dead, but it’s dying. The[ Landauer limit](https://en.wikipedia.org/wiki/Landauer's_principle) seems near and the[ ARC tasks](https://aiguide.substack.com/p/why-the-abstraction-and-reasoning) far. And even if we can create general intelligence _in silico_ , many of Landgrebe and Smith’s points apply doubly to recursive, Singularity-like scenarios.

The Straussian reading of _Why Machines Will Never Rule the World_ is that Landgrebe and Smith’s complexity-based criticisms show not the impossibility of AI, but of AI _alignment_. We can build complex systems—we build stuff we don’t understand all the time! The lesson is that, because of their complexity, intelligent systems will forever defy attempts at formal safety guarantees.

But the[ double secret](https://www.youtube.com/watch?v=hostgKc7qV4&t=62s) Straussian reading is to recognize that the future of cognitive automation is extremely uncertain; that stringing too many propositions together with varying levels of empirical support is a fraught business; and that we live in a world where bioengineered viruses and 13,000 nuclear warheads exist, right now, and maybe there are opportunity costs to writing, reading, reviewing, and reading the reviews of treatises on AI.

_Why Machines Will Never Rule the World_ is 301 pages before you hit the appendices. You can buy the paperback from the [publisher](https://www.routledge.com/Why-Machines-Will-Never-Rule-the-World-Artificial-Intelligence-without/Landgrebe-Smith/p/book/9781032309934) or on [Amazon](https://www.amazon.com/Machines-Will-Never-Rule-World/dp/1032309938) for $48.95, almost exactly the price of a Warhammer starter set or 800 grams of Dutch baby formula.
