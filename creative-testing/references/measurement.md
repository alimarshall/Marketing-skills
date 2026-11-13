# Measuring B2B ad impact honestly

Everything here exists because the default answer, the platform's conversions column, is wrong in both directions at once. It over-counts what it can see and cannot see most of what matters.

---

## 1. Why the default number is wrong

**The windows are shorter than the sales cycle.** LinkedIn's default click-through window is 30 days and view-through is 7. The published B2B SaaS MQL to SQO cycle runs 24 to 68 days across quarters (HockeyStack, 70+ companies), and many teams have no internal figure to check that against. If yours does not, record that gap in the report: it is worth fixing in its own right. On any plausible number both windows expire before a meaningful share of the buying journey completes. Platform-reported conversions structurally undercount influence on the deals that take longest, which are usually the largest.

**The columns are blended.** Campaign Manager combines click-through and view-through into a single "Conversions" figure unless the view is split manually. Always split it. A campaign that looks efficient on blended conversions and thin on click-through conversions is being credited for impressions.

**Cross-platform comparison is structurally biased.** LinkedIn's 7-day view-through default is far more generous than Meta's. "LinkedIn drove more conversions than Meta" is frequently an artefact of the window, not a finding. Normalise the windows before comparing anything.

**Overlapping campaigns double-count.** Each platform attributes inside its own window, independently. Run LinkedIn, Google and Meta simultaneously and the same conversion gets claimed several times. The sum of platform-reported conversions routinely exceeds actual conversions.

**Most of the influence is invisible.** Someone sees an ad, does not click, and three weeks later searches the brand name or types the URL. That arrives as organic or direct. It is the largest single category of ad influence in B2B and click attribution cannot see any of it.

Last-click, given all of the above, systematically credits whichever channel happens to be last, usually branded search or direct, and starves the channels that created the demand it is taking credit for.

---

## 2. What to build instead

Four layers. None is sufficient alone and the combination is honest.

### Layer 1: full-funnel tracking, ad click to revenue

Not MQL. MQL count and CPL are legible and shallow: easy to put on a dashboard, disconnected from whether anything became revenue. Track ad-sourced and ad-influenced contacts through to CRM opportunity stage and closed revenue, accepting messier and slower reporting as the cost of it meaning something.

Implementation belongs to `analytics-tracking` and `revops`. What this skill needs from it: the ability to group pipeline by **angle** and by **format**, not just by campaign. That is a naming-convention dependency, set before launch, in `learning-log.md`.

### Layer 2: self-reported attribution

A mandatory field on every demo and signup form: how did you hear about us.

- **Mandatory, not optional.** Optional produces a biased sample of the people who felt like answering.
- **What it catches:** dark social, word of mouth, podcasts, community, the influence path no pixel sees. And it reveals which campaigns were actually *memorable*, which is a different and often more useful question than which were clicked.
- **Its own bias:** recency, social desirability, and people naming whatever sounds legitimate. Buyers under-report the channels they do not consciously remember, which is most brand exposure.
- **Use it as a cross-check, not a replacement.** Where self-reported and pixel data disagree, the disagreement is the finding. Both are partial views of the same thing.

### Layer 3: periodic incrementality checks

The only method that answers "did this spend cause anything" rather than "what correlated with what".

Hold out a matched geography, or pause spend for a defined period, keep everything else running, and measure the difference in the outcome that matters. Four to eight weeks. It needs no historical data and no statistical infrastructure, which is exactly why it fits at modest B2B scale.

Watch branded search volume, direct traffic and self-reported attribution during the holdout as well as pipeline. Those are where the invisible influence surfaces when you remove it.

Run this quarterly or semi-annually. It is the ground truth against which the fast proxy metrics get periodically validated.

### Layer 4: proxy metrics for daily decisions

CTR, engagement, dwell, landing conversion. Fast, high-volume, and not the thing that matters. That is acceptable as long as it is stated: day-to-day creative decisions run on proxies, and the proxies are checked against layer 3 on a cycle.

**Marketing mix modelling is not layer 5.** MMM realistically wants twelve to twenty-four months of spend and revenue history with genuine variance across channels, multiple simultaneous channels, and something in the region of $30k to $100k a month across three or more of them, before its confidence intervals beat noise. Below that the output looks authoritative and is closer to random. If MMM comes up, say this rather than building something that produces confident numbers from insufficient data.

---

## 3. Demand generation and demand capture are measured differently

This is where most B2B measurement arguments actually live, and it decides what gets funded.

**Demand capture** is the in-market five percent: branded search, retargeting, comparison intent, demo CTAs. It produces clean, immediate, trackable numbers. It wins internal budget arguments because it is legible.

**Demand generation** is the other ninety-five percent who are not in-market today: thought leadership, document ads, video, ungated content. It creates future pipeline that converts later through untrackable paths, which means it is systematically under-credited by any attribution model.

Judge them on the same KPI and demand gen always loses. Teams that do this defund the activity feeding the top of the funnel and see pipeline plateau two or three quarters later, once the small in-market pool saturates. The plateau arrives long after the decision that caused it, which is why the mistake keeps getting made.

| | Demand capture | Demand generation |
|---|---|---|
| Judge on | CPL, pipeline contribution, cost per SQL | Assisted pipeline, branded search lift, direct traffic, self-reported attribution, engagement and dwell |
| Reads back in | Days to weeks | Quarters |
| Fails by | Saturating a small pool | Being defunded before it pays |

Common allocation guidance by stage: earlier companies weight toward capture, and the split moves toward generation as the company matures, roughly 50/50 at growth stage. These are directional conventions rather than derived numbers, and they shift with deal size and cycle length. Treat the ratio as a conversation, not a rule.

Where this bites in practice: `creative-strategy` will produce document ads, thought leader ads and video alongside lead gen forms. The document ad will lose on CPL every time. Deciding, before launch, which metric each format is judged on is the mechanism that stops that from being an argument every month.

---

## 4. A realistic setup, stated plainly

For a programme spending modest amounts on LinkedIn:

1. Conversion tracking through to CRM opportunity and revenue, sliceable by angle and format.
2. Mandatory self-reported attribution on all forms, reviewed monthly against pixel data.
3. Split view-through and click-through conversions in every report. Never quote the blended number.
4. Quarterly geo or timing holdout as the ground-truth check.
5. Daily and weekly decisions on proxies, explicitly labelled as proxies.
6. No MMM.
7. Every reported number carries its volume and its window.

That setup will not tell you exactly what LinkedIn is worth. Nothing available at this scale will. It will tell you whether it is worth something, which direction it is moving, and which arguments are doing the moving, which is enough to run a creative programme on.

The failure mode to name explicitly when reporting: a number that is precise and wrong is more dangerous than a range that is honest. Report ranges. Say which layer produced each figure.
