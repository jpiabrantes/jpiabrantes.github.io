---
template: post
title: The Origins of Society with Multi-Agent RL
slug: the-origins-of-society-with-marl
draft: true
date: 2025-09-23T09:16:15.151Z
description: |-
What environmental conditions led to complex human society? We propose two key properties: cooperation beyond identical kin and valuable public goods. To test this hypothesis, we introduce a multi-agent RL environment where AI agents must collaborate to protect shared resources, recreating the primordial conditions that may have sparked human civilization.
category: colaboration-tech
---

## Introduction

Humanity’s defining trait is large-scale collaboration. This isn’t just the main thesis of the popular book Sapiens, but it is also a key insight for reproducing human-like intelligence in silico. We didn’t develop collaboration because we had human-like intelligence. We achieved our intelligence because we had to collaborate. To create an environment where agents form societies, or in other words large-scale collaboration, we first need to understand the key environmental conditions that made social cooperation an evolutionary advantage.

## The Two Key Properties for Society to Emerge

Large-scale cooperation with identical kin (i.e., identical DNA), as seen in bees and ants, is relatively easy. Every bee in a hive shares the same ultimate goal: protecting and reproducing the genes it shares with the others. Since they share 100% of the genes, they are 100% aligned. This is similar to how every cell in your body is aligned to help you survive and reproduce. When everyone is naturally aligned, collaboration is effortless; but when that’s not the case, collaboration requires the emergence of multiple interesting social behaviours such as identity recognition, status hierarchies, reputation tracking, communication, and promises, to name a few. Additionally, there is compelling evidence that emotions such as love, friendship and grief have evolved independently in social species such as elephants, dolphins, whales and humans[1]. These emotions help solve the challenges of frequent social interaction within a species.

We have already identified the first key property for the emergence of human-like intelligence: **collaboration beyond identical kin**. But what drives social species to cooperate — and why did humans take it to an entirely new level?

The answer is **valuable public goods** such as territories.

Territories are essential to social animals. They serve as a place to store resources, raise vulnerable offspring, and safely sleep. Just as the cellular membrane makes the cell possible, the territorial frontier makes society possible. In both cases, the boundaries are needed to coordinate the parts and tell them which regions need to be maintained and which do not; where order should be preserved and where entropy may rise.

A territory is a public good shared amongst friendly individuals (most often kin) and coveted by competing groups. Even in humanity’s hunter-gatherer period, groups stored communal resources within their territory, which they collectively used and maintained. These included shelter and tools for hunting, gathering, and processing materials like wood and fibers for clothing. However, the groups were small (20–50 people) and nomadic, which meant they had to move frequently and carry their possessions with them, limiting the amount of goods they could maintain.

Farming made territories much more valuable. Farming demanded months of labor for each harvest, and since the goods couldn’t be easily carried, they had to be stored and protected. This was the start of a social arms race. Groups that could cooperate in bigger numbers were rewarded as they could more easily attack or defend the immense wealth stored in farms. But bigger groups bring new problems: kinship ties grow weaker, and members can no longer interact repeatedly with everyone, undermining simple strategies like tit-for-tat. The more value farms held, the more evolution favored bigger groups — and the more sophisticated social intelligence had to become. Success depended not only on the social behaviors described earlier but also on innovations such as arithmetic for accounting and taxation.

We’ve now identified the two key properties that an environment must have for the emergence of human-like intelligence:

1. Other agents with non-identical kin.
2. Benefits for agents that collaborate in larger groups (for example, the existence of public goods).

Building, maintaining, and distributing public goods, amongst non-identical kin is a never ending challenge. So much so, that in modern times we are still struggling with this. Pursuing this research direction promises not only to reproduce the origin of society but also to reveal better ways for humans to live and cooperate in groups.

## Territorial: The Primordial Social Soup

Traditionally, multi-agent environments are in the binary cooperative setting: agents are grouped into teams, agents from the same team fully cooperate while agents from different teams don’t cooperate at all (i.e., cooperation is either one or zero). In our previous work ([blogpost](https://abranti.com/mimicking-evolution-with-reinforcement-learning.html), [paper](https://arxiv.org/abs/2004.00048)), we extended the concept of team to the concept of family and moved from binary cooperation into continuous degrees of cooperation, proportional to the kinship relation amongst agents.

Remarkably, this alone already led to the emergence of more complex cooperative behaviors. For instance, in our multi-agent environment, reproduction required two agents to be adjacent. But this proximity created a serious risk: while mating, they became easy targets for attackers, who could kill them and seize their resources.

Avoiding other agents entirely was not a viable strategy either. Those who kept too much distance eventually died of old age without reproducing.

To overcome this dilemma, agents developed an emergent behavior: they maintained distance most of the time, but when fertile and well-fed, they converged on a shared “Schelling area” to quickly mate before dispersing again. This breeding ground minimized vulnerability by limiting exposure during mating, while also ensuring that agents ready to reproduce could find each other efficiently.

Yet one key property was still missing: benefiting agents who collaborate in larger groups. That is exactly what our new environment, **Territorial**, introduces.

Territorial is a 2D grid world with a new game mechanic that **creates the need and the ability to store resources in a territory**. Each agent needs to consume food in order to survive and reproduce. This food grows on specific world tiles, but only during the Summer season. In Winter, food does not grow and agents have to rely on their storage. Agents can only carry a limited amount of food with them, so the remaining food needs to be somewhere in the 2D grid - accessible to anyone. We also give agents the ability to build stone walls so they can more easily mark and protect their territories.

Note that these mechanics are incredibly unique! In strategic games like Age of Empires, Starcraft or Dota, the gathered resources (gold, wood, stone, etc) are not stored in any physical location and are infinitely safe and magically available wherever they are needed. This automatically solves all of the social challenges that come with having others protecting and carrying the resources that one has gathered. Property rights is a key emergent milestone in human society, but in our virtual environments it is simply hardcoded.

Territorial is one possible instantiation of an environment that respects the two key properties described above. Some other instantiations, that honor those same two properties, could equally well give rise to complex social behaviour. However, Territorial can easily be extended to explore many hypotheses about cooperation and social behaviour. For example:

- If agents could obtain resources more quickly by polluting everyone’s air, could they evolve mechanisms to prevent collective intoxication?
- What collaboration challenges can be solved with spoken language?
- What becomes possible with written systems — will they develop contracts, taxes or even laws?
- What if agents have access to private communication channels between them (end-to-end encryption)?
