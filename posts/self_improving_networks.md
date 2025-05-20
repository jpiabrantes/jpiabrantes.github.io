---
template: post
title: Self-Improving Networks
subtitle: The Deep Link Between AI and Markets
draft: False
description: >-
    There is are a few underlying pricincples that make AI and Markets self-improving networks.
date: 2025-05-15
---
AI is about self-improving neural networks, and markets are about self-improving networks of traders. Self-improving Networks, of any kind, have a lot in common - they follow the same design principles to get better with experience. They also overlap, most tasks traditionally tackled by AI can be reframed as market design problems (examples on this later) - and AI itself is increasingly trading on markets.

However, these two types of networks are also very different in nature. AI improves with more centralisation: the bigger model, with more data and more compute wins. Whereas markets improve with more decentralisation: the market with more participants, more diversity of ideas and lower barriers to entry wins.

In a decentralised World those who find an important truth, by luck or skill, can feed it to the market, and as the world gains from this new knowledge, so does the individual. This dynamic is at the heart of every story worth telling: [the hero’s journey](https://en.wikipedia.org/wiki/Hero%27s_journey), where discovery benefits both the seeker and the society. 

But in a centralised world, only the AI God knows and does it all. In such a world, what will humans dream about? What stories will they have left to tell?

Hopefully, we will never find out. Hopefully, we start giving more thought on how to create more and better Markets.

## The Recipe for Self-Improving Networks

To cook self-improving networks, we need three ingredients:

1. **Objective:** A metric to optimise (maximise or minimise)
2. **Attribution:** A method to measure the contribution of each node to the metric being optimised
3. **Adjustment:** Increase (or decrease) the influence of each node on the metric according to their positive (or negative) contribution

Here are a few examples:

|                         | Neural Networks     | Drivers Network (Uber)         | Supply Chain                        |
|-------------------------|--------------------|-------------------------------|-------------------------------------|
| **Nodes of the Network**| Neurons            | Drivers                       | Suppliers                           |
| **Objective**           | Loss function      | Service Quality               | Profit                              |
| **Attribution**         | Backpropagation    | User Ratings & Performance Metrics | Quality Control                |
| **Adjustment**          | Weight update      | Show Good Drivers More Often  | Bad Suppliers Get Replaced by Competition |


In AI, gradients flow through the network, adjusting the influence of each neuron based on its contribution - just as, in markets, money flows between traders, rewarding merit.

## Prediction Markets = Supervised Learning

Prediction markets have been designed to solve the classical Supervised Learning tasks such as classification and regression. The math makes it so that the market price is linked to its estimated probability. Traders can profit by making trades that move the market from an inaccurate estimate to an accurate one. But, once the market estimate is correct, no one can make it "more correct", and so no one will be able to profit anymore. 

These markets can handle a variety of tasks: classification ("Who will be the next U.S. president?"), regression ("How many cars will Tesla produce next year?), and even conditional predictions ("if Elon is fired, how many cars will Tesla build next year?"). Conditional markets are especially useful for decision-making, as they predict the effects of actions before they are taken. I won't go much into prediction markets as they are already well covered in other places [[1]](https://www.youtube.com/watch?v=4yZKGbq1YmA), [[2]](https://mason.gmu.edu/~rhanson/futarchy2013.pdf) and [[3]](https://timroughgarden.org/f16/l/l18.pdf).

## Supply Chain = Reinforcement Learning

A less widely recognized idea is the deep connection between markets and Reinforcement Learning (RL). RL is the AI paradigm focused on understanding and automating sequential decision-making through interaction with an environment. It is widely regarded as the most general framework for modeling intelligence, as it includes perception, planning, and action under uncertainty. Let's first look at the standard RL problem for a single agent with discrete actions, and then reformulate it as a decentralized supply chain problem.

At time $t$, an RL agent is in state $s_t$ and chooses an action $a_t$, leading to a new state $s_{t+1}$ and a reward $r_t$.

Over time, the agent learns a value function $Q(s_t, a_t)$ that estimates total future rewards from taking action $a_t$ in state $s_t$. Once that function is learned accurately, it guides the agent to take the best action at each state, which is given by $a^* = \arg\max_a{Q(s_t, a_t)}$.

Analogously, in a **supply chain**, the process begins with raw materials (initial state $s_0$). At each stage, multiple suppliers submit bids to purchase the current state of the product ($s_t$). The highest bidder is selected and applies its transformation (action), resulting in a new state $s_{t+1}$. This transformed product is then sold to the suppliers in the next stage. The supplier's reward is the value added, measured as the difference between the selling price of $s_{t+1}$ and the purchase cost of $s_t$. Eventually, the final product is sold to the customer, completing the process.

To maximise profit, each supplier must learn an optimal bidding function $B(s_t)$ that outputs how much to bid for each state $s_t$. Remarkably, if we use a [Vickrey auction](https://en.wikipedia.org/wiki/Vickrey_auction) (highest bidder wins, but only pays the second highest price), the optimal bidding strategy for the supplier performing the transformation $a$ matches the optimal $Q(s, a)$ from RL. Therefore, the auction automatically selects the best action for each state by choosing the supplier with the highest bid; $a^* = \arg\max_a{Q(s_t, a_t)}$.

## Centralisation vs Decentralisation in Self-Improving Networks

I believe the Supply Chain formulation clearly highlights the commonalities and differences between a centralised and decentralised approach to self-improving networks.

On one hand, in the decentralised approach every supplier needs to learn its own bidding function. This is often redundant and wasteful, as similar learning processes are repeated independently across many suppliers. In contrast, the centralised Q-function enables faster learning by aggregating experiences across all states and actions, exploiting common patterns, and reducing redundant computation.

On the other hand, the centralised approach is static, as it is designed to work with a fixed set of known actions. Whereas, the decentralised approach allows a changing number and variety of suppliers to enter, exit and change through innovation. This extra flexibility makes the decentralised approach incredibly robust and adaptable to evolving environments.

## Markets for Generative AI

In the past, RL shined on games like Atari and Chess where the set of actions is known and fixed. In the age of Generative AI, action spaces have become infinite: including endless variations of text, code and function calls. This is the age when markets will shine.

To give a concrete example. Imagine a user posts a request offering &#36;10 for the best response: “Plan a three-day tour of Lisbon”. This is our initial state ($s_0$). Multiple models believe that they can add value to this state and submit bids. Certainly, the Trip Advisor model is confident it knows a lot about Lisbon and submits a high bid. However, at this stage, the model that best understands the user's tastes and preferences has the most value to contribute. Turns out, our user keeps a diary in Notion, giving the Notion model extra confidence to submit a high bid and make it win the auction. The next state reads as the additional information:

```text
the user has the following preferences:
- avoid tourist traps, sightseeings or anything mainstream
- prefers to explore activities that locals themselves do
- preference to skill-based or learning activities over passive entertainment (e.g. watching a show)
- favourite skill-based activity is surfing
- favourite learning activity is exploring local industry's history
```

The added value is enormous! If other models had also acquired $s_0$, transformed it, and presented their outputs to the next-stage bidders, those bidders would likely offer higher bids for the Notion model's output. In the second stage, the Trip Advisor model lost confidence, it is too mainstream, locals don't use it. Grok wins this round. It has real time access to the Portuguese discussions and discovers local surf spots, the local shoe factory tours, lists the top local restaurants, and cafes. And so the process continues. Subsequent models in the supply chain might incorporate traffic and transportation forecasts, surf conditions, hotel availability, and more. Eventually, a final-stage model purchases the current state with the sole purpose of presenting the completed tour to the user. The closer this final bid is to the full &#36;10, the more confident the model is that the user will accept its version of the itinerary. The user, or his personal AI, then looks at the top 10 offers (ordered by the value of the last bid), picks their favourite and releases the &#36;10. Earlier suppliers are compensated according to their bids.

## Final Thoughts

There are many markets to be designed for this age and time. They are not only more appropriate for the current technology but they will also lead to a better future!

P.S. I am aggregating a list of interesting market designs to solve real world problems. If you know of any please send me an email or a DM on twitter. This list will probably lead to more blog posts :)



## References 
Some pointers to work on decentralised RL with local economic transactions:

[1] [Chang, Michael, et al. "Decentralized reinforcement learning: Global decision-making via local economic transactions." International Conference on Machine Learning. PMLR, 2020.
](https://proceedings.mlr.press/v119/chang20b.html)

[2] [Schmidhuber, Jurgen. "A local learning algorithm for dynamic feedforward and recurrent networks." Connection Science 1.4 (1989): 403-412.](https://people.idsia.ch/~juergen/bucketbrigade/)

Some pointers to work on Prediction Markets:

[1] [Introduction to Prediction Markets, Robin Hanson](https://www.youtube.com/watch?v=4yZKGbq1YmA)

[2] [Hanson, Robin. "Shall we vote on values, but bet on beliefs?." Journal of Political Philosophy 21.2 (2013): 151-178.](https://mason.gmu.edu/~rhanson/futarchy2013.pdf)

[3] [Roughgarden, Tim. Lecture #18: Prediction Markets. CS269I: Incentives in Computer Science, Stanford University, 30 Nov. 2016.](https://timroughgarden.org/f16/l/l18.pdf)

