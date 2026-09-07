---
template: post
title: We already keep the world safe from AGI (humans). Let’s do the same for AI.
subtitle: From virtual rewards to physical consequences
slug: keep-the-world-safe-from-ai
draft: false
date: 2026-08-31T00:00:00.000Z
description: >-
  AI safety today stops when training ends. Humans are kept safe by identity, memory and real consequences for life. A concrete proposal (httpi, automatic courts) to do the same for AI.
category: artificial-intelligence
tags:
  - artificial-intelligence
  - AI safety
---

AI safety today is mostly about training: teach the model to do more “good” and less “bad”.

We also educate children to be well behaved. That is needed, but is not what keeps the world safe from humans (AGI). The real safety mechanism is **physical** and kicks in after “pre-training” (when we turn 18): we give more resources to people who do “good” and take them away from people who do “bad”.

AI safety should be more about the latter. AI brings new risks, but taking inspiration from what already works for humans is an excellent start.

## How do we keep the world safe from humans?

If you misbehave you lose money (a fine) or time (jail) or both. For that to work we need two things: know who did it (credit assignment), and be able to punish them. Humans build this into every interaction, so that misbehaving costs more than the damage done. To rent a room or a car you show your ID or leave a deposit. To sell to other people you register a business.

We know this works. The famous prisoner’s dilemma is solved once players have memory and can identify each other.

## How to apply this to AI?

To apply this to AI we need to step up from RL to mechanism design. Instead of using virtual reward signals, we need to use real physical consequences: more compute for agents that behave, less for agents that misbehave.

|                   | RL                               | Mechanism design                |
| ----------------- | -------------------------------- | ------------------------------- |
| Consequences      | Virtual: a reward number         | Physical: more or less compute  |
| Credit assignment | Which tokens caused the outcome  | Which agents caused the outcome |
| What changes      | The weights of the trained model | Which models get compute        |
| When              | Only during training             | Every day the agent runs        |
| Needs             | Access to the weights            | Identity and logs               |

I will now dive right into a concrete and crazy idea, however, I am trusting you to be smart and extract the general principles instead of focusing on the exact tunable parameters:

### httpi: a new protocol

http**s** makes communication between a client and server secure by doing two jobs: 1) it proves the server is who it says it is (the server had to register and get a certificate), and 2) it stops anyone else from listening.

http**i** adds a third job: the client has to prove who it is too. Logins already do this, but every service has its own, so reputation, punishments and bans from one mean nothing anywhere else. httpi has one identity layer shared by everyone, the same way https already works for servers. And only two kinds of identity: human or business. A business is just a weighted list of humans (its shareholders).

Every human gets a free global rate limit. Businesses don’t: they need a deposit. Anyone, human or business, can deposit more to raise their limit.

Both sides keep logs of every interaction for a few days. If someone misbehaves, the logs go to an automatic court (more on that below), which can lower their rate limit or take their deposit. A rate limit of zero essentially puts the AI owner in a sandbox if everyone is using httpi.

Punishment does not stop at the business, it flows to the humans behind it and to the other businesses they own. You can’t escape by starting a new business.

Services that don’t use httpi can't identify or punish bad actors, so malicious agents will attack them first. Over time that pushes everyone onto httpi.

### Automatic courts

Everyone on httpi is judged by the same short set of rules, written in plain English. A constitution. For example, rule one: do not cause human pain.

If your logs show someone broke a rule, you submit a case with the signed logs as proof. The other side is notified and gets time to submit their own proofs.

Then several independent AIs look at the proofs and the reputation of both parties, and bet on one question: what would a human judge decide? Usually the most likely answer becomes the verdict. But sometimes, with probability proportional to how serious the case is, real human judges decide. That keeps the AIs honest: bet wrong and you lose money. (Vitalik Buterin describes this mechanism [here](https://vitalik.eth.limo/general/2024/11/09/infofinance.html#info-finance-for-distilled-human-judgement).)

If the logs show a real crime, the identities are revealed and the humans behind them face their own country’s law. But the main point of automatic courts is that they are as fast as the AIs they judge.

### Automatic contracts

Using httpi is signing a standard contract. The terms are always the same: I sign the messages I send, I keep logs, I accept the court’s verdict.

We can also imagine custom contracts that could be judged by the same automatic courts. But the internet is already full of custom terms and custom logins, and that is exactly why each service is vulnerable in its own way. The value of httpi is that there is a standard contract and identity.

## The general principle

None of the details above matter much. What matters is this: the alignment problem should be stated as reshaping the fitness landscape so that being a selfish agent becomes equivalent to being useful to society. I would love to see more research in harnesses, rules and protocols that can cut the compute of AIs that behave badly, without touching their weights.

## Common counter-arguments & doubts

**A human prompts an AI. Whose identity is used, the human’s or the AI company’s?**

If the AI runs on the human’s computer, the human’s. If it runs on a company’s server, the company’s.

Say you use Claude Code. You prompt Claude over httpi. Claude then makes **your computer** call another service over httpi, so the call carries **your identity**, and that service gets hacked. The service takes you to court, because as far as it can see, you did it. You get notified, check your logs, and see that your prompt was within the rules: it was Claude that misbehaved. You add those logs to the case. Claude gets punished (a fine, or a lower rate limit), the case goes public, and some users leave Claude.

**If everyone has to identify, there is no privacy.**

There is a lot of work on proving things about yourself without revealing who you are (see zero-knowledge proofs, and [zkPassport](https://zkpassport.id) for a working one). Here you only need to prove a few things: I am a human, I have this deposit, I have this rate limit.

**People will sell their identities, or get them stolen.**

Yes. That is why a human identity alone has a rate limit, and raising it needs a deposit. To avoid identities (private keys) being stolen, there could be a small reward for whoever proves they own a private key that isn’t theirs. Leaks would be found quickly and the affected keys rotated.

**A badly trained AI doesn’t care about fines.**

That’s the point. They don’t need to care, a fine is a real consequence and it leads to less money which leads to less compute. Also, the punishment can be a decrease in the rate limit, and an AI owner with a rate limit of 0 is simply in a sandbox.
