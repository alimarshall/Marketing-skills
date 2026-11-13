---
name: creative-testing
description: "Design the test plan and measurement setup for B2B SaaS paid ad creative, and read results honestly at modest budgets. Use when asked how to test ad creative, what to test first, how long to run it, whether an ad is winning, why it underperforms, whether creative is fatigued, how to measure LinkedIn or Meta impact, what to report, or to close the loop on a running concept. Triggers: 'is this ad working', 'how do we test these', 'should we kill this ad', 'our CTR dropped', 'how do we know LinkedIn is working', 'creative refresh'. Covers test design, ad naming, the diagnostic ladder, fatigue, attribution and incrementality, and the creative learning log. Pairs with creative-strategy, which produces the concepts; hand off to paid-ads for targeting and budget, ab-test-setup for experiments outside paid creative, analytics-tracking for tracking."
---

# Creative Testing and Measurement

Two jobs. Before a launch: design a test that can actually produce an answer at your budget. After a launch: read what happened without fooling yourself.

The failure this skill exists to prevent, in both directions: killing a good concept on nine conversions, and scaling a bad one because the number that moved was the one that was easiest to measure.

The constraint that shapes everything here is **volume**. LinkedIn B2B audiences produce an order of magnitude less data than Meta at the same spend. Median B2B creative CTR sits under half a percent, and only about a quarter of creatives convert at all. Statistical significance on a headline test is not available at this scale and pretending otherwise produces confident nonsense. What is available: concept-level reads, diagnostic reasoning, and honest measurement at the campaign level.

`creative-strategy` decides what to say. This skill decides what to learn from saying it.

---

## Inputs

This skill reads and writes the same documents as `creative-strategy`. Their locations are recorded once in `creative-strategy/references/inputs.md`; look them up there rather than asking each time. The ones this skill touches:

- **Creative learning log.** Append-only, one entry per concept that goes live. `creative-strategy` opens entries; this skill closes them.
- **Angle library.** Status per angle per product line. Its slugs are the load-bearing token in ad names. Template in `creative-strategy/references/angle-library.md`.
- **Account baseline.** Your own account's median CTR, dwell, engagement and CPL by format, derived from the learning log once there is enough history. Preferred over any published benchmark.
- **Creative brief** for the concepts under test, carrying each concept's hypothesis.
- **Platform benchmarks** in `creative-strategy/references/platform-specs.md`, used only until the account baseline exists.

If a document is missing, say so and run without it rather than inventing its contents. Never invent a result, a benchmark or a performance figure.

---

## Step 0: Which job

- **Planning a test** for concepts that have not launched. Steps 1 to 4.
- **Reading a result** for something that has been running. Steps 5 to 7.
- **Diagnosing a specific ad** that is underperforming. Steps 5 and 6, then back to `creative-strategy` if the fix is the argument rather than the execution.
- **Setting up measurement** for the programme as a whole. Step 8.

State which and proceed.

---

## Step 1: Establish what the budget can answer

Do this first, before designing anything. The most common way a B2B creative test fails is that it was never capable of producing a read.

Ask for, or work out: total budget, duration, number of variants intended, and the audience size.

Then apply the thresholds in `references/test-design.md`. The short version, and every figure is a practitioner heuristic rather than a proven law:

| Decision you want to make | What it needs per variant |
|---|---|
| Directional read on CTR and engagement | 1,000+ impressions, roughly $1,400 over four weeks |
| Directional read on cost per lead | 50+ conversions |
| A cost-per-lead call you would defend | 100+ conversions |
| Anything about lead quality or pipeline | 200+ leads, and 30 to 60 days for the conversion lag |

Divide the budget by the number of variants. If a variant does not clear the threshold for the decision being asked, say so plainly and offer the two honest options: fewer variants, or a decision made on a weaker signal and labelled as such.

**Never let a test launch that cannot answer its own question.** Naming that at the planning stage is cheap. Naming it after four weeks of spend is not.

---

## Step 2: Decide what is actually being tested

Concept-level or variable-level. They are different tests and conflating them is the second most common failure.

- **Concept-level.** Different arguments, formats and hooks against each other. Large performance swings, so a signal emerges at low volume. **This is almost always the right test on LinkedIn.**
- **Variable-level.** One locked concept, one thing changed. Small swings, needs volume most B2B programmes do not have. Below a few thousand a week, do not bother.

Then set the order of leverage. Testing creative first is intuitive and usually wrong, because targeting and offer move results more than wording does:

1. **Audience.** The largest single effect, and published audits find around a third of B2B SaaS paid budget leaking to non-ICP audiences, worse in categories whose buyer job titles are noisy on the platform. Belongs to `paid-ads`, but it is upstream of creative and a weak result may be an audience artefact.
2. **Offer.** Demo, document, calculator, event. Changes who responds, not just how many.
3. **Creative concept.** What this skill is mostly for.
4. **Format.** Cheaper to vary than the argument, and a legitimate test in its own right.
5. **Placement and bidding.** Last, smallest.

Hold everything constant except the layer under test. Run variants **simultaneously**, not sequentially: sequential tests confound the creative difference with seasonality, competitor activity and platform shifts.

---

## Step 3: Write the test plan

Use the template in `references/test-design.md`. It states, per test: the hypothesis, the variants and what differs between them, what is held constant, the audience, the budget split, the duration, the primary metric and its threshold, the secondary metrics being watched, and, most importantly, **the decision each outcome triggers**.

That last field is the one people skip. Write down in advance what result would make you scale, kill, iterate or extend. A threshold decided after seeing the data is not a threshold.

Every concept in the plan carries its hypothesis forward from the creative brief. If a concept has no hypothesis that could turn out false, it is not a test, it is a launch.

---

## Step 4: Naming and instrumentation

Nothing in this skill works if the data cannot be sliced by the thing being tested. `references/learning-log.md` has the convention. Set it before launch, because it cannot be applied retroactively.

Campaign, ad set and ad names encode product line, funnel stage, audience, angle, format and concept ID, so that performance can be grouped by **angle** and by **format** across campaigns. Ads are named `{conceptID}_{angle}_{format}_{variant}`, with the concept ID matching the creative brief and the angle slug matching the angle library exactly. That grouping is the whole point: the interesting question is not which ad won, it is which argument won.

Also before launch: confirm conversion tracking fires, UTMs are consistent, the self-reported attribution field exists on the form, and the learning log entry is open for each concept.

---

## Step 5: Read the result

Work down the ladder in `references/diagnostics.md`. Stop at the first gate that failed, because everything below it is contaminated.

```
impressions → attention → engagement → click → landing → conversion → quality → pipeline
```

Each gate isolates a different part of the creative, which is what makes the ladder more useful than staring at CPL:

- **Attention failed** (low hook rate or 3-second view): the visual or the first line. Not the offer.
- **Engagement failed** (high hook, low hold or dwell): the hook overpromised. Fix the body, not the opener.
- **Click failed** (good dwell, low CTR): the offer or the CTA, or the ad was interesting without being actionable.
- **Landing failed** (good CTR, low conversion): message match between ad and page. The creative did its job.
- **Quality failed** (good conversion, no pipeline): the offer attracted the wrong buyer. A document downloader is not a demo request.

Benchmarks live in `creative-strategy/references/platform-specs.md`. Use your account baseline over published benchmarks wherever any history exists: the published spread for LinkedIn B2B CTR runs from roughly 0.47% median to over 1.4% depending on format and methodology, which is too wide to set a target from.

**Judge each format on the metric it was running on.** A document ad or a thought leader ad measured on CPL will always lose to a lead gen form, and defunding it on that basis is how a demand programme collapses into pure capture and then plateaus. Say which metric each concept is being judged on before showing the numbers.

---

## Step 6: Decide

Four outcomes. `references/diagnostics.md` has the full decision table.

- **Scale.** Clears the threshold set in Step 3, past the volume floor. Increase budget in increments rather than steps, and preserve accumulated social proof where the platform allows it.
- **Iterate.** The concept works, the execution is imperfect. Fix the specific gate that failed. Iteration briefs are short: 150 words on what is changing from the parent.
- **Kill.** Failed at the attention gate past the spend threshold. Reallocate rather than nursing it.
- **Not yet.** Below the volume floor. This is a legitimate and frequently correct answer, and it is the one most often skipped. Day-seven winners are regularly day-twenty-eight losers.

Then the distinction that saves the most money: **fatigued or bad.** A fatigued ad worked and is declining under frequency. The fix is a fresh execution of the same concept. A bad ad never worked. The fix is a new concept. Teams that conflate them spend quarters re-skinning a weak argument. The fatigue signature and the thresholds are in `references/diagnostics.md`.

---

## Step 7: Close the loop

The part that makes the next round better, and the part that gets dropped.

Close the concept's entry in the creative learning log, per `references/learning-log.md`: what shipped, the hypothesis, what happened, what it taught, and whether the angle survives.

Then update the angle library with the status change: `In test` becomes `Winner` or `Retired, reason`. **Write the reason.** A retired angle without a recorded reason gets proposed again within two quarters by someone who was not there.

Promote a repeated pattern into a default. Two or three independent wins on the same format or structure stops being a result and becomes a house pattern that new briefs start from. That promotion, from result to codified pattern to brief input, is the mechanism by which creative gets systematically better rather than randomly lucky.

Refresh the account baseline when new closed entries move it.

Report in under 200 words: what to scale, what to kill, what to iterate, what is still inconclusive and when it will not be. A clean result with nothing to change is a fine, plainly stated outcome.

---

## Step 8: Measurement setup

`references/measurement.md` is the full treatment. What a realistic setup looks like at modest B2B spend:

1. **Full-funnel tracking**, ad click through to CRM opportunity and revenue. Not MQL, which is legible and shallow.
2. **A mandatory self-reported attribution field** on every demo and signup form, cross-checked against pixel data. It catches the influence that click tracking structurally cannot see, and it has its own bias, so it complements rather than replaces.
3. **Periodic incrementality checks** rather than modelling. Geo or timing holdouts over four to eight weeks. Marketing mix modelling wants twelve to twenty-four months of history and roughly $30k to $100k a month across three or more channels to beat noise, which is usually out of reach and should be said rather than attempted.
4. **Accept proxy metrics for day-to-day decisions.** CTR, engagement, dwell, landing conversion. Then validate them against an incrementality check quarterly. That is the honest structure: fast proxies, periodically ground-truthed.

Three facts to keep in front of anyone reading a LinkedIn ads report:

- LinkedIn's default view-through window is **7 days** and click-through is **30 days**, blended into one "Conversions" column unless split manually. Meta's view-through default is far shorter, so any cross-platform comparison is structurally biased toward LinkedIn.
- The published B2B SaaS MQL to SQO cycle runs 24 to 68 days across quarters (HockeyStack, 70+ companies). Use your own cycle-time figure if you have one. If you do not, say so in the report and use the benchmark as an order-of-magnitude prior only. Either way it is usually longer than both attribution windows, so platform-reported conversions structurally undercount.
- Much of LinkedIn's real influence arrives later as direct or organic traffic. Account-level pipeline timing against ad exposure is a better read than click attribution, and it is the one worth building toward.

---

## Handoffs

| Next question | Skill |
|---|---|
| The concept was the problem, we need new angles | `creative-strategy` |
| An avatar was contradicted by a result | `ad-avatars` |
| Audience, budget, bidding, campaign structure | `paid-ads` |
| More copy variations off a winning angle | `ad-creative` |
| The landing page is the failing gate | `page-cro`, `copywriting` |
| Formal experiment design beyond creative | `ab-test-setup` |
| Tracking implementation, GA4, UTMs, events | `analytics-tracking` |
| Lead-to-pipeline handoff and lead quality definitions | `revops` |

## Scaling

- **One ad, one question.** Step 6's decision table alone. Two minutes, not a report.
- **A test round.** Steps 1 to 4, then 5 to 7 when results land.
- **A quarterly review.** All steps, plus a pattern pass across the learning log: what has won more than once, what has failed more than once, and what that says about the angle library rather than about any individual ad.
