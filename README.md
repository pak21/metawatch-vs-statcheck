# Metawatch vs Statcheck

[Warhammer 40,000](https://en.wikipedia.org/wiki/Warhammer_40,000) is a popular tabletop miniatures wargame published by Games Workshop. Within the game, there exist various "factions" representing the armies that can battle in the game. As with any game, there is a desire that the various factions are somewhat balanced in that each one has an equal chance of winning.

The excellent [Tactical Tortoise](https://www.youtube.com/@TacticalTortoise) (Trevy) made a video "[We need to talk about 40k Metawatch](https://www.youtube.com/watch?v=f4NsNqFjcDU)" comparing the win rates of the factions from two sources:

1. The offical [Metawatch statistics](https://www.warhammer-community.com/2023/02/16/warhammer-40000-metawatch-the-arks-of-omen-launch-the-latest-competitive-season/) from Games Workshop.
2. The unofficial [Stat Check statistics](https://www.stat-check.com/the-meta)

As Trevy notes in his video, these two sources draw from different sources - therefore we have to expect the results to differ somewhat. From a statistical point of view, the question we have to ask is "are these differences bigger than we would expect by chance?"

## Methodology

We start with the raw data from both Metawatch and Stat Check as linked above with two minor transformations to normalise the sets of factions to those chosen by Metawatch:

1. Aggregate the "codex compliant" Space Marines chapters (Iron Hands, Blood Angels, Ultramarines, Black Templars, Salamanders, White Scars, Imperial Fists, Crimson Fists and Raven Guard) from Stat Check into the one "Adeptus Astartes" faction.
2. Split the Ynnari subfaction from the larger Asuryani faction.

The data for this can be seen in [this Google sheet](https://docs.google.com/spreadsheets/d/1bYYOs1kir5o5B0znOQfikyMEZ_sqfxxJwXMHQMrrXjk/edit?usp=sharing) and in this repo as [`metawatch-vs-statcheck.csv`](metawatch-vs-statcheck.csv).

From this, we can apply the [Poisson means test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson_means_test.html) to see if the differences between the two reported win rates are significantly different. Two notes here:

1. We don't know the sample size for the Metawatch data; I've somewhat arbitrarily decided to estimate it as twice the Stat Check size, but the results aren't particularly dependent on this.
2. It is formally wrong to use the Poisson means test here; while we don't know the data used by Metawatch, it's pretty safe to assume that they do include the major tournaments used by Stat Check so this means the samples aren't independent. I'm not too worried about this today.

The script to do this analysis is [`analyze.py`](analyze.py).

## Results

Running the analysis script on the above data, we obtain the following p-values:

* Tyranids: 0.03
* Leagues of Votann: 0.08
* Chaos Knights: 0.11

and everything else at or above 0.30. For the non-stat heads in the audience, a result is generally considered significant only if the p-value is _below_ 0.05; this means that only the Tyranids difference is bigger than would be expected by chance. In particular, the Chaos Knights and Adeptus Custodes results noted by Trevy in his video would not be considered significant. (Stat heads: yes, I know I'm glossing over a lot of subtlety in p-values here. Don't flame me too much).

## Conclusion

There isn't a significant difference between the results from Metawatch and those from Stat Check.
