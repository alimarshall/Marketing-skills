# Test design at B2B budget scale

Designing a creative test that can actually produce an answer when the channel gives you a few hundred clicks a month.

Every number here is a practitioner heuristic aggregated from published guidance, not a controlled result. Use them as floors for a conversation about what the budget can buy, not as thresholds with statistical standing.

---

## 1. What the budget can answer

Work this out before designing anything.

| Decision | Per variant | Why |
|---|---|---|
| Directional read on CTR, engagement, dwell | 1,000+ impressions, roughly $1,400 over 4 weeks | Enough to separate a clear winner from a clear loser, not enough to separate two similar ones |
| Directional read on cost per lead | 50+ conversions | Below this, single conversions move the number by a fifth |
| A CPL call you would defend to someone sceptical | 100+ conversions | |
| Anything about lead quality or pipeline | 200+ leads, 30 to 60 days | The conversion lag is longer than the test |

Spend floor per creative: roughly **$100 to $150** before drawing any conclusion. Below that, the result is noise wearing a number.

**Duration**, allowing for the platform's own optimisation to settle:

| Test type | Run for |
|---|---|
| Creative concept | 3 to 4 weeks |
| Audience | 4 to 6 weeks |
| Bidding | ~6 weeks, to clear the learning period |
| Pipeline outcome | 30 to 60 days after the last conversion |

Do not react in the first 48 to 72 hours. Delivery is still stabilising.

**The arithmetic to run out loud.** Budget divided by variants divided by weeks, against the threshold for the decision being asked. If it does not clear, there are exactly two honest options: fewer variants, or a decision made on a weaker signal and labelled as such in the report. A third option, running it anyway and reporting the result as if it meant something, is how a team convinces itself the channel does not work.

---

## 2. Concept-level or variable-level

| | Concept-level | Variable-level |
|---|---|---|
| What varies | Different argument, format, hook | One element inside a locked concept |
| Effect size | Large | Small |
| Volume needed | Reachable on LinkedIn | Usually not |
| When | Almost always, at modest B2B budgets | After a concept has won, at Meta-scale volume |

Below a few thousand a week, variable-level testing on LinkedIn is not worth running. It consumes budget to produce a difference smaller than the noise.

The corollary, which is the operating stance at modest B2B scale: **maximise distinct creative volume and diversity, and judge on directional trend plus pattern-matching across attempts, rather than pretending to statistical power you do not have.** This is a reasonable heuristic given real constraints, not a proven law, and it should be stated as such when reporting.

The evidence that makes it reasonable: research from the Ehrenberg-Bass Institute's B2B work found creative execution accounts for roughly 47% of an ad's sales impact, and that a large majority of B2B ads studied were effectively wasted spend through a formulaic pattern. If creative quality is that large a lever, exploring more of the creative space beats measuring a small part of it precisely.

---

## 3. Order of leverage

Test in this order, not in order of what is most fun to change.

| Rank | Layer | Rough share of the effect | Owned by |
|---|---|---|---|
| 1 | Audience | Largest | `paid-ads` |
| 2 | Offer | Large | `creative-strategy` |
| 3 | Creative concept | Moderate | `creative-strategy` |
| 4 | Format | Moderate, cheap to vary | `creative-strategy` |
| 5 | Placement, bidding | Smallest | `paid-ads` |

Two notes that matter more than they look.

**Audience first is not a formality.** Published audit work puts non-ICP budget leakage across B2B SaaS at around a third, and worse in categories whose buyers carry inconsistent or ambiguous job titles. LinkedIn's self-reported job function and seniority fields can be unusually noisy for some buyers; check how clean they are for yours before trusting a job-title audience. A creative result read on a leaky audience is a measurement of the wrong population, and a weak concept result may be an audience artefact. Check the audience before concluding anything about the argument.

**Offer changes who responds, not just how many.** A document ad and a demo request pull different people from the same audience. Comparing them on the same metric is a category error, not a test.

---

## 4. The rules that keep a test readable

- **Simultaneous, not sequential.** Running A this week and B next confounds the creative with the week. Seasonality, competitor auction pressure and platform changes all move within a fortnight.
- **One layer at a time.** Changing the visual and the headline and the CTA produces a result you cannot attribute.
- **Equal budget, equal audience.** Uneven splits produce uneven learning-period effects.
- **Disable platform creative auto-enhancement** while testing. If the platform alters the asset, the asset measured is not the asset built.
- **Do not peek and stop.** Checking daily and calling it the moment it looks good is the classic way to manufacture a false positive.
- **Watch the multiple-comparison trap.** Run enough variants and one will look like a winner by chance. With six variants and no volume, the top performer is frequently just the luckiest.
- **Do not compare across audience temperatures.** Cold and retargeting numbers are different populations, not different creatives.

---

## 5. The test plan template

```markdown
# Test plan: [name]
**Date:** YYYY-MM-DD   **Product line:** [name]
**Brief:** [link to the creative brief this comes from]

## Question
One sentence. What decision does this test exist to make?

## Layer under test
Audience | Offer | Concept | Format | Placement

## Hypothesis
[From the creative brief.] We believe [X] will [do Y] because [Z].
Falsifiable: what result would prove this wrong?

## Variants

| ID | Concept | Angle | Format | What differs |
|---|---|---|---|---|
| C1 | ... | ... | Single image | Baseline |
| C2 | ... | ... | Document | Format and argument |

## Held constant
Audience, budget split, bid strategy, landing page, offer, run dates.

## Setup
- Audience: [definition, estimated size]
- Budget: $X total, $Y per variant per day
- Duration: X weeks, [start] to [end]
- Naming: [per learning-log.md convention]
- Tracking: conversion action, UTMs, self-reported attribution field confirmed live

## Can this answer its question?
$Y per variant per week × X weeks = $Z per variant.
Expected impressions ~N, expected conversions ~M.
Threshold for the decision above: [from section 1].
**Verdict:** clears / does not clear. If it does not: [fewer variants | weaker signal, labelled].

## Metrics
- Primary: [metric], threshold [value]
- Secondary watched: [list]
- Explicitly not judged on: [e.g. document ad not judged on CPL]

## Decisions in advance

| If | Then |
|---|---|
| C2 beats C1 on [primary] by more than [X] past the volume floor | Scale C2, iterate C1's [gate] |
| Both below [floor] | Kill both, the angle is the problem, back to creative-strategy |
| Neither reaches the volume floor by [date] | Extend to [date] or consolidate budget onto two variants |

## Review date
[Date]. Not before.
```

---

## 6. Sustaining a pipeline

Testing is a pipeline, not an event. A useful rule of thumb from performance practice: only one to three creatives in ten become genuine winners, so the production rate has to assume most attempts fail.

The healthy standing shape, scaled down for modest B2B spend:

- A small number of validated concepts running
- A similar number tested and ready to launch
- A similar number in production

Production runs ahead of the decay curve, not reactively after an ad dies. Reserve a standing share of budget, in the region of 10 to 20 percent, for testing at all times, so there is always a validated concept ready when a winner fatigues. The alternative, which is what happens by default, is a scramble every time performance drops, and a scramble produces iterations of a tired angle rather than a new one.

Refresh cadence scales with spend. At modest B2B budgets a creative may live weeks rather than days, and the fatigue signals in `diagnostics.md` are a better trigger than a calendar.
