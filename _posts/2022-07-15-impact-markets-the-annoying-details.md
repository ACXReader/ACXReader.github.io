---
title: "Impact Markets: The Annoying Details"
subtitle: "..."
date: 2022-07-15
author: Scott Alexander
comments: https://www.astralcodexten.com/api/v1/post/63311485/comments?&all_comments=true
image: https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/8c4f3122-f6e7-4e9a-be1b-06821d1e8977_1020x522.png
original-url: https://www.astralcodexten.com/p/impact-markets-the-annoying-details
---
I said last year that I’d like to try running this year’s [ACX Grants](https://astralcodexten.substack.com/p/acx-grants-results) through impact markets. Since then, some people have expressed interest in the technical implementation, and - to nobody’s surprise more than my own - it’s starting to look like it could happen.

A reminder: impact certificates are like a VC funding ecosystem for charity. Charity founders with good ideas sell shares in their proposed projects. Profit-seeking investors buy shares of (“invest in”) projects that they expect to succeed. This funds the project; if it does succeed, altruistic people/foundations (“final oracular funders”) buy the impact, compensating the investors. 

For example, suppose I come up with a great idea to end malaria in Senegal. I need $1 million to make it work, and when it works it will be worth $5 million in benefits to the Senegalese. Ordinary charitable foundations don’t appreciate my genius, so I pitch it to VCs with biotech experience. They like it and buy 100% of the shares for $1 million. I take my million dollars, do the project, and cure malaria in Senegal. Foundations see that I have done a great thing with $5 million in benefits, so they give me $5 million. I pass this along to my investors, who make $5 million on a $1 million investment. They’re very happy, and incentivized to do more things like this in the future.

Why is this useful? Try running a grants program and you’ll find out! You, a person who is presumably very altruistic but not necessarily an expert in epidemiology, will be asked to make decisions about which diseases to cure how. If you get it wrong, you’ve wasted your donors’ money. You can ask epidemiologists for help, but it turns out there is no easy way to get in contact with a consensus of all the world’s epidemiologists - let alone with the all the developmental economists, political scientists, etc who might have useful insights. Very large charitable foundations will have hired these people or built relationships with them, but even they don’t always feel confident in their decision-making process.

In the current system, your job is to predict which charitable projects _will_ work. In an impact market, you (as the final oracular funder) only need to figure out which projects _did_ work, which is much easier: for example, penicillin obviously worked, and flying cars obviously didn’t. Then you buy the shares of those projects, and your job is done. Private investors still have to do the prediction behind the scenes, but they’re only risking their own money, not charitable dollars, and they’re properly incentivized to get the right answers.

This is how I’ve always explained it before - and you can read other explanations like [Paul Christiano’s](https://forum.effectivealtruism.org/topics/certificate-of-impact) or [Vitalik Buterin’s](https://medium.com/ethereum-optimism/retroactive-public-goods-funding-33c9b7d00f0c). This post isn’t about the theory. It’s about the annoying implementation details. It may not be very interesting to people who are neither effective altruists nor institution design wonks, sorry.

## **1: What Is The Basic Format Of The Market?**

**A: Simple Retroactive Funding**

Some charitable funder announces they will give money to good things that they like. If somebody does a good thing, the funder might give them money later. There isn’t necessarily any investing, certificates, or tokens.

Advantage: This is very simple, and can be done right now: in fact, a team [is already doing this](https://forum.effectivealtruism.org/posts/YdaugCRoko7ac4QCL/experiment-in-retroactive-funding-an-ea-forum-prize-contest) for good Effective Altruism Forum posts.

Disadvantage: This is a good start, but really just equivalent to giving prizes to good EA Forum posts. Absent someone else setting up an auxiliary structure, it doesn’t help useful projects get funded. At best, it encourages a few marginal people to do cheap things they might have done anyway.

**B: Block Impact Certificates**

A charity offers a single impact certificate representing a project. For example, if they need $1 million to cure malaria in Senegal, they sell a single certificate representing that project for $1 million. Then, when an final oracular funder decides the project is worth $5 million, they give $5 million to the holder of the certificate.

Advantage: Again, it's simple.

Disadvantage: Someone needs to have the entire $1 million in order to fund the project. There’s no way to split the costs, which makes it worse than eg stocks. When Tesla needs $1 billion in new funding, it doesn’t just ask billionaires. It sells (eg) one million shares of stock for $1000 each, and then people with much less than $1 billion can bet on their success.

**C: Fractionalized Impact Shares**

A charity offers splits its offering into many shares or tokens. For example, if they need $1 million to cure malaria in Senegal, they could sell 10,000 tokens for $100 each. Then, when a final oracular funder decides the project is worth $5 million, they compensate each token holder with 1/10,000th of the final reward, so $500.

Advantage: this allows people with much less than $1 million to invest, and creates a secondary market in tokens which people could probably do interesting things with.

Disadvantage: Suppose the charity wants $1 million because it will take $500,000 to build a medicine factory, and then they want to make $500,000 worth of medicine. If only $400,000 in tokens are sold, they can’t even build the factory, and the whole project is worthless. So an investor wouldn’t want to invest $400,000 unless they were sure that someone would produce the other $600,000. But since nobody can know that, people might not invest. Or they might invest, then get very angry when their investment turns ends up useless.

**D: Fractionalized Impact Shares With Assurance Contract**

As above, except instead of buying a token, investors commit to buy a certain amount of tokens _if_ all tokens get bought. For example, Alice might say “I commit to buying $400,000 of tokens, _if_ eventually we get to $1 million”. Bob might say “I commit to buying $300,000 of tokens, _if_ eventually we get to $1 million”. Carol might say “I commit to buying the final $300,000 in tokens”, and then everyone’s commitment “activates” and they all have to buy the tokens. You might be familiar with this as the mechanism behind Kickstarter campaigns.

Advantage: This solves the problem discussed above.

Disadvantage: It’s more complicated - but I think most people capable of buying certificates at all should be able to understand this, especially if it’s explained well on the marketplace’s website.

_My thoughts: The fractionalized shares with assurance contracts seem clearly the best. Some reviewers noted that in real venture capitalism, VCs are able to talk to each other to coordinate funding without a formal assurance contract. I think our market will involve smaller and less savvy players (at least at first), which would make the contract more useful._

## **2: What Is Being Sold?**

**A: Full Credit For The Impact Of The Project**

This is the traditional solution. If I cured malaria, and you previously bought an impact certificate equal to 100% of my “equity” in the project, then in theory you have the right to say you cured malaria, and I don’t.

Advantage: Elegance, everyone knows what's going on.

Disadvantage: It’s hard to enforce from a common sense point of view. “The credit for” doing something partly takes the form of accurate costly signals about my personal characteristics, which can't be transferred. 

For example, suppose I cure malaria by inventing a novel antimalarial drug. Part of “getting the credit” for this is people understanding that I am a brilliant biologist. They might use me as a role model for young scientists, ask my opinion on important science policy questions, or make me chair of the biology department at Harvard. There's no credible way to sell these benefits - just because I sell _you_ the impact certificate for curing malaria, doesn’t mean Harvard would be willing to make _you_ the department chair instead.

This is also going to make a lot of people mad when some photogenic kid from Kenya sweats and toils to builds a water pump for his community or something, and then some billionaire says no, _I_ built that water pump.

**B: Credit For Funding The Project**

I think this is what Ben Hoffman writes about [here](http://benjaminrosshoffman.com/minimum-viable-impact-purchases/).

Both the people who do the project (ie the founder who gets people to build the bednet factory, the scientist who discovers the malaria cure) and the people who fund the project deserve some share of credit in the success. In this model, impact markets would distribute the funding-related credit only. That is, I might pay $1 million for the impact of a project to cure malaria; when they succeed, I can sell it to a big foundation for $5 million. So long as I have the shares, I can claim that I funded the project; once the foundation has the shares, they can claim this (even though causally they were not the ones who give the project the funds). In either case, the founders and scientists retain the credit for founding the project and doing the science.

**C: Rules Around Equity**

We might (for example) say that in an average project, the actual team involved deserves half the credit, and the funders also deserve half the credit (or some other distribution). Then we might have a norm that the team can sell half the equity (representing the funding credit) but not the other half (representing a sort of inalienable moral credit that attaches to their hard work). 

Advantage: Matches common sense

Disadvantage: More complicated, less elegant, founders can't sell as much equity.

_My thoughts: There are good arguments for all of these. See below for more._

## **3: How Should The Market Handle Projects With Variable Funding Needs?**

Suppose a charity says “For $1 million, we can cure malaria in Senegal. But if we had $10 million, we could cure malaria in all of West Africa!”

This is a bad match for the token impact certificates with assurance contract discussed above; do we active the assurance contract at $1 million, or at $10 million?

**A: Activate The Contract** **At $1 Million, Then Keep Selling More Tokens**

This has the following problem: suppose that you are an investor who believes that the plan to cure malaria in Senegal will succeed (produce $5 million in value), but the grander plan to cure it elsewhere in Africa will fail (produce $0 in value). You buy the $1 million in original tokens, activating the contract. Then other, less savvy investors buy the $9 million in remaining tokens.

You turn out to be right about everything. The first project succeeds and produces $5 million in value; the second project fails and produces $0. A final oracular funder pays $5 million, distributed evenly among all token-holders. Your 1/10th of the total token supply gets you $500,000. So even though you were right about everything, you have turned a $1 million investment into only $500,000, and lost half your money.

Since this was your original prediction, you will never invest your original $1 million, even though you correctly predict that will be good!

In other words, under this method, proposing a grander secondary plan might prevent people from investing in your primary plan, even if your primary plan is good, which seems like a bad feature.

**B: Activate The Contract At $1 Million, Then Sell A Different Token For The Other Plan**

IE the charity sells $1 million worth of “cure malaria in Senegal” tokens. Then, if that contract activates, they offer another $9 million of “expand the plan to all of West Africa” tokens. Everyone knows which kind of token they are buying.

Advantage: This avoids the problem mentioned above.

Disadvantage: More complicated.

One extra advantage: it can handle different levels of needing assurance contracts. For example, if the plan is “$1 million to start off, and then for each $1 we get after that we can produce one additional bed net”, then you don’t need any assurance contract on the secondary tokens. If it’s $1 million to start off, and then for each additional $500,000 we can open a factory in another African country”, then maybe there should be an assurance contract on each extra $500,000, or - if this would get too complicated - on the full $10 million.

_My thoughts: Reviewers brought up that real venture capitalists solve this problem by having multiple funding rounds where they sell off different parts of their equity. For example, you might sell off 10% in the first round, achieve some amount, and then sell off another 10% for your next big expansion. I am nervous about this because I want to be able to pitch impact certificates to non-savvy people who may not be able to make good decisions about equity._

_One possible solution reviewers brought up would be to offer a “standard deal” like Y Combinator does. If you don’t want to think about impact certificates, you take the standard deal, convert some pre-arranged percent of your equity to certificates, and never think about it again. Then if you want to do something more complicated later, you can look into your options further._

## **4: Should Founders Be Getting Rich Off Impact Certificates?**

**A: Yes**

Jeff Bezos founded Amazon, sold off some of his equity for seed funding, and kept some other equity for himself. As Amazon grew, the equity appreciated in value, making him very rich.

We could imagine impact certificates working the same way. I start a charitable project, sell 50% of the impact equity for seed funding, and then succeed. My investors can sell their impact certificates to a final oracular funder for more than they paid, making a profit. But I can also sell off _my_ remaining equity to the same funders, making me a profit, potentially a very big one. For example, if I have a project that uses $1 million in funding to produces $5 million of value in the form of malaria cures, I can sell 50% of my equity to investors to get the $1 million I need. When it succeeds, a final oracular funder can pay $2.5 million to my investors, and an additional $2.5 million to me. Now I’m a multimillionaire for coming up with such a great charitable scheme.

Advantage: This encourages people to start charities; the more good they could do, the more it encourages them.

Disadvantage: This redirects at least some of “the surplus” from charities and beneficiaries to founders. That is, right now if a charitable project that costs $1 million produces $100 billion in value, then the founder gets some normal salary, and the funding charity and its beneficiaries have gotten an amazingly good deal. This is good for charities and beneficiaries. But if we allowed founders to capture more of the surplus, then maybe the founder would end up with $50 billion, and the charity and its beneficiaries would only get $50 billion, which seems much worse for them. Given that our goal here is to help beneficiaries (and by implication charities, since any money charities save goes to the beneficiaries eventually), this seems pretty bad.

Or to put it another way, if someone makes $50 billion off charity and uses it to buy a yacht, then some of your charitable donations are going to yachts, which seems worse than them going to feeding the hungry or curing the sick.

Or to put it yet _another_ way, if founders generally kept 50% of their equity, all charitable projects would be twice as expensive - the normal $X to fund the project, and then an additional $X to pay off the founder. If founders generally kept 75% of their equity, all projects would be 4x as expensive, and so on.

And to bring things closer to home: a reviewer mentions an certain excellent AI safety researcher. Given how much money is in this field, and how few excellent researchers there are, the big foundations might plausibly consider this person to be worth $10 million per year (that is, they would be happy to fund a program that spent $10 million per year to create another researcher of the same quality). But right now this person just earns an ordinary six figure AI engineer salary. If impact markets were “a success”, they might have to more than dectuple the amount they pay this person, with no change to their output.

**B. No**

Impact certificates could be used only to fill projects; need for funding, the same way grants are used now. Social norms would mandate that founders only ask for as much money as they needed for their project. This might include paying themselves a fair salary, but they wouldn’t be getting rich.

Advantage: Avoiding the problems mentioned above.

Disadvantage: There might be some situation where an especially brilliant person considers for-profit vs. charitable work and goes with for-profit because they won’t be able to internalize the value produced by their charity.

_My thoughts: Extremely split on this._

_Part of the point of impact markets is to spend some of the surplus on incentivizing more charity to exist._

_There are some innocuous ways to do this._ _For example, suppose that there are an unlimited number of malaria charities that want $1 million, and 25% of those will succeed and produce $5 million in benefits, with the other 75% producing nothing. So one way to produce $5 million in expectation is to spend $4 million funding four of these charities. Another way is to buy an impact certificate for a successful project from an investor. So suppose a savvy investor is twice as good at picking projects as the final oracular funder; she can pick a winner 50% of the time. So she pays $2 million to fund two projects, producing in expectation one successful impact certificate representing $5 million in benefits. Then it would seem that the investor and final oracular funder should agree to a price somewhere between $2 million and $4 million for the certificate; whatever number in this range they choose, both will make a profit over their next-best option. They can use normal negotiating tactics to figure out where in that range they fall, but nobody should lose money relative to the no-impact-certificates world._

_But if there are projects that everyone recognizes as good, then an impact marketplace will shift the surplus from final oracular funders (who are forced to pay prices more commensurate with their benefits) to someone else. If we let founders get rich, it shifts the surplus to founders. If we don’t let founders get rich, it shifts the surplus to fast investors who may not have added any value - that is, to the first people who snapped up the obviously-underpriced certificates. See Section 7 for more on this problem._

_I don’t have a good solution to this latter issue other than either not using impact markets, or allowing founders to get rich. I sketch a hack-ish solution in Section 11C._

## **5: How Do We Kickstart The Existence Of An Impact Market?**

How do we get an impact market to exist? Investors will only buy impact certificates if they expect that a final oracular funder will buy them, but we'll have a hard time convincing them when this has never happened before.

**A. Retroactive Prizes First, Then Impact Certificates**

Someone who wants to be a final oracular funder gets in the habit of giving out retroactive prizes. For example, out of the blue they find someone who helped fight malaria, and award them $1 million. They make it clear that if someone sells an impact certificate, they will give the prize to the certificate-holder rather than the original charity. Eventually this happens enough that people grow to expect and predict it, and they can sell impact certificates around it.

Advantage: It's simple and would probably work.

Disadvantage: It takes a long time, and a lot of granting prizes to projects that don’t need them (ie they would have been done anyway even without the prizes). Also, it kind of elides over the part where the impact certificate market gets set up. Is someone else doing this behind the scenes? What if they don’t?

**B: Committed Pot Of Money (aka The Original ACX Grants Plan)**

In the original ACX Grants plan, I solicit grant proposals, and probably get ~500 like last year. I promise to be Final Oracular Funder and give out prizes in one year’s time, and I commit a specific sum to this purpose (let’s say $1 million). I link everyone who’s interested to a market where people can buy shares in the project, and they do this, competing for my $1 million.

Advantage: This sure does set up a marketplace.

Disadvantage: Investors will have to predict (and maybe be sabotaged by) the behavior of other investors. If people only buy a total $1 million in tokens, then on average every investor will break even. Not every investor will in fact break even, because the whole point is that money will flow towards the good investors and away from the worse investors. But _on average_ they’ll break even.

But suppose you invest when there are $1 million of tokens sold, thinking that you are a slightly-better-than-average investor and so can probably do better than break even. Then later some other people come in and buy $9 million more worth of tokens. Now there are $10 million in tokens chasing $1 million in prizes, and on average each investor will only get 10% of their money back. Although some great investors could still come out ahead, it would be an unpleasant surprise to start out expecting to break even, only to learn later that you should actually only expect to get 10% of your money back.

**C: Pot Of Money Plus Cap**

As above, except that the amount of tokens that can be bought is some multiple of the amount of money in the pot - for example, only $1 million in tokens can be bought, so everyone knows they can on average expect to break even.

Advantage: Solves the problem above.

Disadvantage: It’s pretty limiting. Also, investors don’t have a god-given right to break even. Also, if _every_ project produces massive value, some of them will necessarily be under-rewarded - and knowing that makes them necessarily under-invested-in.

**D: Market Kickstart Plus Semi-Unlimited Pot Of Money**

Here we would kickstart the supply side of the market with a set of grant proposals as above, but the final oracular funder would be a very large charitable organization (eg Open Phil or the Future Fund), operating at a scale so far beyond the size of the market that they could commit to funding _every_ project that was good enough to deserve it.

Advantage: Solves the problems above.

Disadvantage: It places a lot of the buy/don’t-buy decision in the hands of a single oracular funder. For example, suppose that OpenPhil agreed to do this, but a few years later they got a new CEO who was more conservative than the previous CEO, and only funded about 2/3 as many projects. Now the chance of getting a return on your investment has gone down by 2/3 for a reason unrelated to its fundamentals. Or suppose someone invested in a malaria project, but OpenPhil pivoted away from tropical diseases and now there was no hope of getting any return. Seems like the sort of uncertainty that would discourage people from investing.

**E. Market Kickstart Plus Multiple Unlimited Pots Of Money**

This is more of the ideal. Have so many people making open-ended commitments to buy impact that changes in one or two of them don’t matter as much. This is how the stock market works: you can buy a stock with good fundamentals because there are so many people who buy stocks that you can abstract out concerns like “Warren Buffett is pivoting away from that industry”; there will always be _someone_ around to offer you a fair price.

Disadvantage: This seems less like a way of starting an impact market, and more like a final desired end state.

_My thoughts: I think the lower-down options are clearly better, but they’ll depend on how many people are willing to commit giant pots of money to this project._

## **6: Should The Market Use Cryptocurrency?**

**A: Centralized impact certificates and fiat currencies**

We could have a standard online marketplace where people buy impact certificates (block or fractionalized) from the site with dollars (or other fiat currencies). The site would track all purchases, and in the very unlikely event that the site ever got erased, everyone would remember it anyway (eg the charity would remember who funded them).

Advantage: Easy to set up and use.

Disadvantage: We don’t get the “coolness” boost of using crypto.

**B: Impact NFTs/token and cryptocurrencies**

Or we could have a crypto marketplace, like eg OpenSea’s NFT marketplace. The impact certificates could be NFTs (if block) or cryptographic tokens (if fractionalized), and people could buy or sell them using cryptocurrency.

Advantage: We're asking people to spend thousands of dollars on meaningless tokens with no direct personal use value, this is usually a hard sell, but people get excited about this kind of deal when you call it an "NFT". Also, many cryptocurrency users have lots of money and like investing it in experimental projects. Also, EA is friendly with FTX and they might be able to help set this up.

Disadvantage: This is harder for the technical people to set up (unless they’re FTX), harder for users to use unless they’re already familiar with crypto, and has a reputation for including scams.

I’m not concerned about environmental issues because we can just use a blockchain without those problems, but other people who don’t understand crypto might not understand that, and it might be bad PR for a charitable project.

_My thoughts: Crypto-literate reviewers say that crypto exchanges take fiat and handle transactions within themselves in a non-crypto way - but then the crypto exists in case someone wants to bring it to a different exchange. This seems like a best of both worlds scenario._

## **7: How Should The Market Price IPOs?**

**A: Sell Certificates/Shares for Exactly The Amount Needed To Fund The Project**

For example, if a project needed $1 million, it might sell 10,000 shares and price them at $100 each. Whoever was the first person to pay $100 for a share would get it. If all the shares sold out quickly, and someone else wanted one later, they would have to buy it from an existing owner (probably at a higher price).

Advantage: It’s easy to price shares, and project founders will get exactly the amount of money they want.

Disadvantage: All surplus goes to fast people. For example, suppose there is a $1 million project that will create $5 million in value, and everyone knows this. The first few people to see the shares will buy up all them at $100, then immediately sell them for $499 (or whatever), making a huge profit without doing any work.

Note that this isn’t just a question of “the project should have priced their shares higher”. It might be common knowledge that this project with $1 million in costs will create $5 million in value, but if we're asking project founders to honestly report their funding needs, then they will honestly say they need $1 million. In this model, there's no way to get the cost to $5 million without the founders lying.

**B: Auction Off The Certificates/Shares**

Certificates/shares would get auctioned off for some period of time, kind of like how NFTs are sold now.

I don't know how to use an auction process with fungible shares, although someone has probably solved this problem. A very easy version would be that the share price starts at $100, and if I try to buy 25 shares for $2500, instead I begin an auction with that as the starting price, which lasts some amount of time.

Advantage: Founders and projects deserve the surplus more than lucky/fast investors.

Disadvantage: Might be technically harder. If the founders get the surplus, then they might get rich, which has advantages and disadvantages (see Section 4). The project getting the surplus would be less morally fraught, but not all projects have room for arbitrary amounts of extra funding.

_My thoughts: Split on this one. I think the answer will depend on how we resolve the earlier question, “should founders be getting rich off impact certificates?” If yes, then clearly auctions are the way to go (or implied auctions where founders sell off impact at a high price). If no, I can’t think of a good solution to the “fast people get rich” problem._

## **8: How Should The Oracular Funder Buy Successful Projects?**

**A. By Buying A Certain Number Of Shares**

The same way as in the usual stock market. An investor who owns (for example) 10% of a project can negotiate a sale to the funder.

Advantage: Everyone understands stocks, and this is very simple.

Disadvantage: oracular funders might be semi-monopsonists who can play investors off against each other. This sounds like the kind of process that gets an impact certificate-related fight featured on _Money Stuff_.

**B. By Creating A Funding Floor**

Vitalik Buterin’s idea. A final oracular funder states that they value the project at (let’s say) $5 million, and as long as they continue to do so, they will buy any share in the project for $5 million/percent of the project.

Under this model, somewhat might “apply” to have a funder value a certain project. The funder will come up with a valuation, and then anyone (including the original applicant, or other shareholders) can sell their shares at that price.

Advantage: Makes people less concerned about monopsony.

Disadvantage: Might be slightly more complicated.

## **9: What Should The Final Oracular Funder’s Decision Process Be?**

How does a final oracular funder decide how much money a successful project is worth?

**A: Fund Based On Regular Charitable Decision-Making Procedure**

Presumably final oracular funders already have grantmaking procedures, and can ask themselves questions like “How much would we have paid to prospectively fund a project like this one, knowing that it would succeed as much as it did?”

Advantage: Easy (?)

Disadvantage: Opaque to everyone except the funder. If you’re paying $1 million for a project to cure malaria in Senegal that you think has a 50% chance of success, it matters a lot to you whether the oracular funder would pay $500,000 vs. $5 million upon successful completion. But there might not be enough of a published history of grants for you to know this, and it might not even be a question with a fixed answer: it might depend on which of several different grantmakers got it, or on whether they were in a good or bad mood that day, or any of several other confounders.

Although in theory oracular funders and investors are aligned insofar as the funders want to encourage future projects by paying fair prices for current ones, the alignment might break down - for example, the particular employee charged with evaluating how much money to pay for a successful project might be rewarded for “keeping costs down”, but not be punished for this having a vague long-run negative effect on impact markets. Even if this isn’t true, investors might _worry_ that it’s true, and so under-invest.

One reviewer suggested that final oracular funders go through a long list of past grants (for example, the 2021 ACX Grants) and publish how much money they would have paid for each; future investors can check the list and get a rough idea of what gets how much money.

**B: Fund Based On Some Sort Of Clear, Quantified Schedule**

For example, “we will pay $1000 for every life saved”.

Advantage: this is clear, objective, and removes investor uncertainty.

Disadvantage: Only works for highly legible projects. How do you quantify the lives saved by lobbying to prevent future pandemics (especially if the lobbying is successful, and a counterfactual pandemic quietly fails to happen)? How do you quantify the success of a CFAR-style educational intervention to "raise the sanity waterline"?

These aren't an unsolveable problem: final oracular funders could easily say "We will pay $500 for each person who has been successfully educated about rationality". But unless they specified every possible outcome, this would shift incentives in favor of commonly-considered, easily-specified outcomes. And outcomes they do specify risk Goodharting - a self-interested founder with these incentives will "educate" people the smallest amount possible to still qualify for the award.

**C: Fund Based On Some Kind Of Very Vague Schedule**

For example, “we will pay $500,000 for what we think of as an important insight into AI alignment, similar in magnitude to X or Y previous insights. We will pay $100,000 for what we think of as a minor but still useful insight, similar to Z previous insight.”

Or “we will pay $500,000 for what seems like a major decrease in malaria prevalence in this country. We will pay $100,000 for what seems like a smaller but still measurable decrease.”

Advantage: Strikes a balance between the previous two methods. 

Disadvantage: The oracular funder won't be able to predict all the different good things that might come out of charitable projects, and so it will either have to commit to making some things up post facto (as in A) or subtly discourage people from doing unusual things that can’t be measured on the usual metric (as in B).

**D: Offer Consultations On Funding Schedules**

The final oracular funder could have an officer who takes calls from potential investors and explains the amount of funding they would get for different levels of success. For example, you might say “I’m funding a project to save the endangered blue leopard, how much is that worth to you?” and they could answer “$500 per leopard saved, plus an extra 200% bonus if you save more than 1,000 of them”.

Advantage: this makes investment payoffs clear without preemptively demanding too much legibility.

Disadvantage: requires more work from final oracular funders, and is especially vulnerable to Goodharting ("But you _promised_ you would pay us $500 per leopard!")

**E: Have So Many Potential Funders That It Converges To A Market Price**

This whole system is partly predicated on the idea that funders will like knowing that they funded useful things - both because they are genuinely altruistic, and because they want to gain status and credibility by showcasing their charitable successes. If there are many oracular funders willing to buy impact certificates, then (absent collusion) they could potentially converge on a “market price”. 

That is, if the impact certificate cost an absurdly low amount, like $1, then people could buy “curing malaria in an entire country” for $1, and I (who would love to be able to brag about saving an entire country at parties) would outbid them and buy it for $2. But if the price were absurdly high - let’s say $100 billion - then nobody would buy it, because you could do more good some other way with that much money. So buyers and sellers will converge on a market price for impact certificates, people could mostly predict what that would be, and it would be fair in some sense.

Advantage: this is how we do everything else under capitalism, and it usually sort of works.

Disadvantage: This will require many independent funders and high liquidity, which might not be realistic while kickstarting a market (or ever). The EA ecosystem is tightly-knit, and even if oracular funders didn't explicitly collude, they would be starting from such similar values and such a cooperative stance towards each other that the equilibrium would probably _feel_ collusive. 

 _My thoughts: Guess this one is up to the final oracular funders_.

## **10: Who Are We Expecting To Have As Investors?**

**A: Institutional Types And VC Firms**

These are who we would eventually be hoping to attract, given that we are trying to encourage the creation of institution-level expertise in charity-picking. Also, they have the most money.

Disadvantage: We probably couldn't get them right away, and there aren’t that many who really understand effective altruism yet.

**B: Ordinary People**

Not _too_ ordinary - we still need for them to make more than $200,000/year and so qualify as accredited investors (see I-A below) - but random Google engineers who are interested in EA, that kind of thing.

Advantage: there are lots of them, including in EA. Some of them probably have a hidden talent in charity selection and it would be very useful to learn who those are.

Disadvantage: They would bring less intellectual firepower to the problem per entity than large firms. They would have less money, meaning that only smaller projects could get funded, and we would need to be more concerned about moral hazard (ie they lose all their money and then are sad). 

 _My thoughts: Institutional types probably won’t bite for a little while, so we'll need to be prepared for ordinary people._

## **11: Conclusion: What Kind Of Impact Market Should We Have?**

At this point after talking to reviewers I am leaning towards a fractionalized-share-with-assurance-contract design, implemented through a mixed fiat-crypto market, aimed at relatively ordinary people, kickstarted by a few very large oracular funders who come up with their own decision procedures.

I’m most uncertain about how to handle issues of founder equity, moral credit, founders getting rich, and splitting surpluses. Here are some designs I’ve been thinking about:

**A: The “Maximum Capitalism” Design**

Founders start with 100% equity, representing all the credit for their project. They can sell however much equity they want to investors, for however much money the investors are willing to pay. They can spend some of that money funding their project, and if they have any left over, they can keep it as profits. If they sell off 100% of the equity, then in some sense that we will have to hammer out socially, they “get no credit” for their project, no matter how hard they worked on it or how good a job they did.

The main advantages are elegance, ease of use insofar as everyone knows how capitalism works, and potential for good charity founders to get rich.

The main disadvantages are that it requires some financial savvy (unsavvy people can potentially lose all credit for their project in a way that will make them very unhappy), and it diverts a lot of the surplus to founders and investors rather than funders/beneficiaries.

**B: The “Project Funding Only” Design**

Founders sell off an amount of impact shares equal to the cost of their project / constant, where the cost of their project includes paying themselves a fair salary. Investors speculate on these. The investors may get rich if they are unusually good at spotting promising projects, but the founders won’t.

The main advantage is ease of use for non-financially-savvy founders, plus people feeling more comfortable knowing that charity founders aren’t getting rich and buying yachts with their donations. In some cases, the oracular funders and their beneficiaries will keep more of the surplus.

The main disadvantage is that in cases where projects are very beneficial and everyone knows this, whoever snaps up the shares first will get most of the surplus. This is clearly unfair.

**C: Hybrid Design: Some Kind Of Scaling Of Investor Equity**

I dislike both A and B enough that I am trying to think of hybrid designs that avoid both extremes.

Consider our typical example: a malaria project that requires $1 million and will produce $5 million in benefits. If we know that the desired solution is to sell $1 million worth of equity, but we want people to be “bidding” for it instead of just snapping it up and “scalping” it, we could have them bid for _smaller quantities_ rather than higher prices. For example, Bidder A could say “I’ll pay the $1 million for only 25% of the equity!”, and Bidder B could counter “No, I’ll pay it for only 21%!” Then Bidder B would win, pay $1 million, and when the final oracular funder bought it for $5 million, the investor would get $1.05 million - enough to make a fair profit, but most of the surplus would still go to the funder and beneficiaries.

The key would be that the original founder keeps 79% of the equity but - by agreement/collusion among oracular funders - can’t sell it. They can just keep it as moral credit for their hard work on the project. I don’t like the fact that it’s important they want to keep as much as possible but they have no real incentive to do so - maybe funders could give them 1% of what their equity entitles them to as a bonus, as they are buying other equity? I’m not sure; it’s kind of a hack.

The other problem would be the math. If there’s only one block certificate worth $1 million, it’s easy to imagine how the bidding works. If there are 1000 tokens for $1000 each, then bidding on an equity amount for each token sounds more complicated. This would be up to auction theorists and programmers to figure out a fair way to implement.

_My thoughts: I really hate all these options, and I’m posting this partly to see if other people have better ideas._

_Some reviewers who are also potential final oracular funders feel like they might be able to solve the all-surplus-goes-to-making-people-rich problem with A by just not paying that much money; I haven't fully thought through the downstream effects of that._

* * *

## **Appendix I: Legal Issues**

**A: Issues Around Unregistered Securities**

The lawyer I consulted on this project says that impact certificates are unregistered securities. But he also says that in the US, it’s legal to sell unregistered securities to accredited investors - meaning (more or less) people who make more than $200,000 a year. Any impact certificate market could probably operate legally in the US as long as it screened buyers to make sure they were above this number. I’m not sure about other countries.

**B: Issues Around Tax-Deductability**

The same lawyer said impact certificates would never be tax-deductible. That makes investing in impact certificates less financially efficient than donating to a regular charity, from a would-be investor/donor’s point of view.

One possible retort is that potential investors and potential donors are different people, plus it’s _more_ financially efficient because you might make money off of it, which you never do with normal charitable donations.

Maybe a better way to look at this is abstracting out the investor and comparing “final oracular funder donates directly to charity” vs. “final oracular funder gives money to investor, causing charity to get funded”. Here it becomes clear that it’s the oracular funder who’s losing out on the tax benefits. But do oracular funders (eg OpenPhil, Future Fund) pay taxes at all, or benefit from tax-deductability? I’m not clear on this.

**C: Issues Around Oracular Funders’ Nonprofit Status.**

Government bodies might think it’s weird for a tax-deductible charity, organized for the public good, to spend lots of its money in payouts to venture capitalists who are not themselves engaging in charity.

As far as I know there’s no legal precedent on this issue and we would just have to try it and see.

**D: Issues Around Governance And Principal-Agent Problems**

Suppose I invest $1 million in a project to cure malaria, on the assumption that it will work and an oracular funder will pay me back - and then the people involved are lazy and don’t even try to work on the malaria cure?

Realistically this is no worse than the current situation, where eg OpenPhil can fund someone to cure malaria and they can just not do it. If they deliberately embezzle the funds, it’s embezzlement and you can sue them. If they’re just really bad at their job, that seems like part of the risk you take in normal charity _and_ normal investments.

In normal investment, stocks (sometimes) grant a right to control a certain amount of corporate governance. In theory, impact markets could work the same way. I’m against this because it would be extremely hard to enforce; we would need to get Congress to pass laws about it or something. Also, sometimes shares in a company don’t connect to governance, and that usually seems to go fine.

**E: Issues Around Middlemen Holding Money**

If there is an impact marketplace, probably it would take investors’ money (or maybe their credit card details, if it’s using assurance contracts), then shortly afterwards give it to the charitable projects.

Does the step where the marketplace acts as a middleman between the investor and the charity give it any legal responsibilities? For example, are these two transactions both separate taxable events? (I think no, but would like confirmation).

## **Appendix II: Ethical Issues**

**A: Accidentally Encouraging High-Risk Negative-In-Expectation Projects**

Suppose I have a project where I spend $1 million to cure everyone in Senegal of malaria, creating $5 million in value. Also, there’s a 25% chance it has terrible side effects, giving everyone cancer and costing $100 million in lost value. So on average, the project produces $5 million + 0.25 * -$100 million = -$20 million in value: its expected costs are greater than benefits. A regular charity would avoid funding this, because they are altruistic and clearly don’t want to fund something that (in expectation) makes the world worse.

But a smart-but-amoral VC _would_ fund it. In 75% of cases, it produces $5 million in value, and charities (who just a see a happy malaria-free country) pay them that money. In 25% of cases, it creates -$100 million in value, and nobody buys the impact certificate, for a total value of $0 (they’re not obligated to pay the negative value; how would you force them?) So in expectation, they will make 0.75*5 = $3.75 million on a $1 million investment. So they _do_ invest in this net-negative project.

You could object that this is no worse than the situation with business investing now, but actually there are quite a lot of bad businesses that make the world worse, and since charities are explicitly trying to make the world better, they should hold themselves to a higher standard of not doing that.

[Ofer and Owen Cotton-Barrett have discussed this here](https://forum.effectivealtruism.org/posts/74rz7b8fztCsKotL6/impact-markets-may-incentivize-predictably-net-negative). Their conclusion is that final oracular funders should take this into account when deciding who to grant impact certificates to. This kind of softens the benefit of impact certificates - their whole point was supposed to be that funders shouldn’t _have to_ be smart people who can figure out the results of various plans - but at least figuring out whether there were potential bad effects sounds like a _somewhat_ easier problem than figuring out whether something will work.

This could also be handled at the market level, by refusing to list certificates/tokens in projects that were especially likely to be high negative-impact - although, again, this requires market officials to be smart, which is a strong requirement.

**B: Incentivizing Reward-Hacking**

Once an impact certificate marketplace is established, decisions of final oracular funders will determine whether savvy private investors get millions of dollars or not. That means that savvy private investors - who are very good at influencing things! who might have entire departments whose whole job it is to influence other large savvy organizations! - will want to gain power over organizations like Future Fund and OpenPhil and influence their grantmaking. A worst-case scenario for this might look like the current relationship between the US military and its defense contractors, where outright bribery is banned but the contractors use many other forms of soft influence to sway military decision-makers.

I have trouble imagining this really working with OpenPhil and Future Fund in their current forms, but part of the problem is that this provides a long-term incentive for private industry to try to twist them into other forms that are less resilient.

**C: People Could Lose A Lot Of Money**

The typical statistic is that nine out of ten startups fail. Of the 656 ACX Grants applications, I was only able to fund 38 (6%), though a few others got funded through other means. Future Fund has mentioned[ only funding 4%](https://forum.effectivealtruism.org/posts/paMYXYFYbbjpdjgbt/future-fund-june-2022-update) of its “open call” applicants. Unlike investing in regular stocks, where on average even if you can’t beat the market your stock will stay the same or even go up, the default outcome in buying impact certificates is that you lose all your money.

This is bad both because we don’t want people to lose all their money, and because this might create moral hazard on the part of final oracular funders to recoup some of people’s losses if they seem like an especially pitiful case.

I think we should promote a norm that people shouldn’t invest any money in impact certificates that they don’t want to lose. Otherwise, I’m not sure this is any worse than eg crypto, which already lets small investors lose all their money quickly.

**D. Using Impact Certificates For Evil**

For example, what if people use this technology to incentivize assassinating political figures they don’t like?

This concerns me least out of all the issues in this section. There is no advantage of retrospective assassination funding compared to prospective assassination funding. In fact, there’s a significant disadvantage: the prospective funding requires a conspiracy of two people (assassin and funder), whereas the retrospective funding requires a conspiracy of three (assassin, investor, and final oracular funder). Most investors would assume that most oracular funders wouldn’t support assassination, and on the very slim chance that an oracular funder publicly communicated the opposite, they could be immediately arrested for promoting assassination, the same as anyone else who publicly broadcasts “I WILL GIVE YOU $1 MILLION TO ASSASSINATE SOMEONE”.

Legal political movements that we disapprove of may eventually be able to use this technology, but this is a general side effect of any attempt to make charity more efficient, and most charity is not political.

* * *

(there’s another copy of this post at <https://forum.effectivealtruism.org/posts/6LppWMdN2NLHceGTr/impact-markets-the-annoying-details> to catch different potential readers; you might be interested checking the comments there too)
