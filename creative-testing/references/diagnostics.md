# Diagnostics: reading what actually happened

The point of the ladder is that each gate isolates a different part of the creative. CPL alone tells you something is wrong. The ladder tells you which part to change.

Work down it and **stop at the first gate that failed.** Everything below a broken gate is contaminated by it: a low conversion rate downstream of a broken hook is not evidence about the offer.

---

## 1. The ladder

| Gate | Metric | What it tests | If it fails, change |
|---|---|---|---|
| Attention | 3-second view rate, hook rate, thumbstop | Did the first frame or first line stop the scroll | The visual, the first line, the pattern interrupt. Not the offer |
| Engagement | Hold rate, dwell time, completion percentiles | Did the body sustain what the hook promised | Pacing, clarity, length. Not the opener |
| Click | CTR | Was acting on it worth doing now | Offer, CTA, or relevance to who saw it |
| Landing | Landing page view rate, bounce | Did the click deliver what the ad promised | Message match, load speed, mobile experience |
| Conversion | Form or demo conversion rate | Did the page turn interest into action | Form friction, page value proposition, offer fit for the stage |
| Quality | MQL to SQL rate | Did it attract the right buyer | Targeting, or the offer itself. A downloader is not a buyer |
| Pipeline | Opportunities, revenue | Did it become real | Usually not a creative problem by this point |

### Reading combinations

The diagnostic value is mostly in the combinations, not the individual numbers.

| Pattern | Reading | Action |
|---|---|---|
| High attention, low hold | The hook overpromised what the body delivered | Rework the body. Keep the hook |
| Low attention, everything else fine on the few who stayed | A good ad nobody saw | Change the visual and the first line only. The argument is working |
| High dwell, low CTR | Interesting without being actionable, or the wrong awareness state | Sharpen the CTA, or accept it as a top-funnel asset and stop judging it on CTR |
| High CTR, low landing conversion | Ad and page are telling different stories | Fix message match. The creative did its job |
| High conversion, no pipeline | The offer attracted the wrong buyer | Change the offer, not the execution |
| Everything mediocre, nothing bad | Usually the argument, not the ad | Back to `creative-strategy`. This is the hardest one to accept |

Two format-specific cautions:

- **Thought leader ads cannot be judged on CTR.** "See more" expansions on long posts register as clicks, which inflates the number in a way that is not comparable to any other format. Judge on engagement rate and dwell.
- **Document ads and video have no form fill by design.** Judging them on CPL guarantees they lose to a lead gen form, and defunding them on that basis is the standard route to a pure demand-capture programme that plateaus once the in-market pool saturates. Decide the metric before showing the numbers.

---

## 2. Benchmarks, and how much to trust them

Full tables in `creative-strategy/references/platform-specs.md`. The honest summary for reading a result:

- LinkedIn B2B creative CTR sits around **0.47% median** in the most methodologically transparent study available, with the top decile above 0.74% and best performers above 1.4%. Aggregator sources put the blended figure closer to 0.74%. The spread between sources is wider than the difference between a good ad and a bad one.
- **Only about a quarter of creatives convert at all.** Most creative work moves top-funnel metrics and nothing else. This is normal, not failure.
- Format matters more than wording: document ads roughly 1.38% CTR, carousel 0.78%, video 0.71%, single image 0.54%.
- Dwell time median around 4.2 seconds, top decile above 6.8.

**Prefer your own account history over any of this.** Once there are twenty ads of history in the learning log, the account's own median (the account baseline) is a better benchmark than any published figure, because it holds audience, brand and category constant.

Video hook and hold benchmarks in wide circulation (thumbstop in the high teens to high twenties, hold rates around a fifth) are Meta-context numbers from vendor content, not controlled studies. They are directionally useful if and when you run Meta. They should not be imported into a LinkedIn report as targets.

---

## 3. The decision table

Apply only past the volume floor from `test-design.md`.

| State | Decision | How |
|---|---|---|
| Clears the pre-set threshold, past the floor | **Scale** | Increase budget in increments rather than steps. Preserve accumulated engagement where the platform allows duplicating from the original post rather than creating fresh |
| Concept works, one gate weak | **Iterate** | Fix that gate only. Short iteration brief, 150 words on what changes from the parent |
| Failed at the attention gate past the spend floor | **Kill** | Reallocate. Do not nurse it |
| Below the volume floor | **Not yet** | State the date it will have a read. Day-seven winners are regularly day-twenty-eight losers |
| Was working, now declining | **Fatigue check** | Section 4 before anything else |
| All variants mediocre | **Back to strategy** | The argument, not the execution |

The most under-used row is **not yet**. It is the correct answer more often than any other and it is the one nobody wants to write.

---

## 4. Fatigued or bad

The distinction that saves the most money, because the two look similar in a dashboard and want opposite responses.

**A fatigued ad worked and is now declining under audience over-exposure.** The concept is validated. The fix is a fresh execution of the same concept.

**A bad ad never worked.** The fix is a new concept. Re-skinning it produces a second bad ad.

The fatigue signature is three things happening **together**:

1. Frequency climbing past roughly 2.5 to 3 on prospecting, or 4 to 6 on retargeting
2. CTR down 15 to 25 percent against its own trailing two-week average, with 30 percent-plus as the action threshold
3. CPM rising

Any one alone is not proof. CPM rises for auction reasons unrelated to the creative. CTR wobbles at low volume. Frequency climbs on a small ABM list by design. It is the simultaneity that identifies fatigue.

The test that settles it: **did this ad ever beat the account median?** If yes and it is declining with frequency climbing, it is fatigue. If it never did, frequency is irrelevant and the ad was always weak.

These thresholds come from Meta-context practice. The mechanism transfers to LinkedIn; the exact numbers may not, particularly on small ABM audiences where frequency is high by design. Recalibrate against the learning log as history accumulates.

---

## 5. What is not a creative problem

Worth ruling out before a concept gets blamed and a good angle gets retired.

- **Audience leakage.** Published audits put non-ICP waste across B2B SaaS at around a third, worse in categories with noisy buyer job titles. If the audience is leaking, every creative in it underperforms and the result says nothing about the argument.
- **Frequency concentration.** On a company list, delivery concentrates on the most available inventory: a small subset of accounts absorbs the impressions while most of the target list never sees the ad. Looks like fatigue, is a distribution problem.
- **Bidding.** Maximum delivery in a thin, expensive audience pays a premium with no ceiling. Raises cost per result with no creative cause.
- **Attribution window.** LinkedIn blends 7-day view-through and 30-day click-through into one conversions column by default. A creative that looks better may just be catching more view-through.
- **Sales cycle.** The published B2B benchmark MQL to SQO cycle runs 24 to 68 days. Use your own figure if you have one, and say so if you do not. Anything judged on pipeline inside 30 days is being judged on incomplete data.
- **Landing page.** A page change mid-flight invalidates a creative comparison. Check for one before explaining a drop.

All of these belong to `paid-ads`, `analytics-tracking` or `page-cro`. Naming them correctly is part of reading the result honestly, and it protects angles from being retired for someone else's reason.

---

## 6. Writing the read

Under 200 words. This order:

1. **What we are doing about it.** Scale, kill, iterate, wait. Lead with the decision.
2. **The gate that decided it.** One line, with the number.
3. **What it taught us about the angle**, not about the ad. This is what goes in the learning log.
4. **What is still inconclusive**, and the date it will not be.

State the metric each format was judged on before the numbers. State the volume behind every number. A CTR quoted without impressions is not information.

If the honest answer is that nothing reached a readable volume, say that as the whole report. It is a real finding about the budget, and it belongs in the next test plan.
