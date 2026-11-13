# Platform specs and benchmarks

LinkedIn is the primary channel here, Meta the secondary one. Everything here is validated against at delivery: every line of copy ships with a character count and a pass or fail.

**Specs drift.** Platforms change limits without announcement, and the figures below were compiled in August 2026 from third-party spec aggregators and LinkedIn's developer documentation, because LinkedIn's own help pages block automated fetching. Treat them as working values. If a campaign is about to spend real money, confirm the current limit in Campaign Manager before building the asset.

---

## 1. LinkedIn: creative specs

| Format | Image / video | Ratio | File | Max size | Intro text | Headline | Description |
|---|---|---|---|---|---|---|---|
| **Single image** | 1200x1200 (1200x628 also accepted) | 1:1, 1.91:1 | JPG, PNG, static GIF | 5 MB | 150 chars visible before "see more", 600 hard cap | 70 chars | 100 chars, desktop only |
| **Video** | 1920x1080 or 1080x1080, min 640x360 | 16:9, 1:1, 4:5, 9:16 | MP4 | 200 MB | Same 150 / 600 | 70 chars | 100 chars |
| **Carousel** | 1080x1080 per card | 1:1 | JPG, PNG | 10 MB per card | Same 150 / 600 | 45 chars per card | n/a |
| **Document** | Page-based, portrait or square | Portrait, square | PDF, DOC, DOCX, PPT, PPTX | 100 MB | Same 150 / 600 | 70 chars | n/a |
| **Thought Leader** | Inherits the organic post | Native | Native | Native | **Up to 3,000 chars** | none | none |
| **Conversation** | Banner 300x250 | n/a | JPG, PNG, GIF | 2 MB | Opening message ~500 chars | Up to 5 CTAs, ~25 chars each | n/a |
| **Text ad** | 100x100 | 1:1 | JPG, PNG | 2 MB | n/a | 25 chars | 75 chars |
| **Spotlight** | 100x100 logo, 300x250 background | 1:1 | JPG, PNG | 2 MB | n/a | 50 chars | 70 chars, CTA ~18 chars |
| **Lead gen form** | Overlay on the above | n/a | n/a | n/a | Headline under 60 chars, offer detail up to 160 chars | n/a | n/a |

Legacy or changing: single-CTA **Message Ads** are being phased out in favour of Conversation Ads. Standalone **Article Ads** are marked legacy in LinkedIn's marketing API docs, with newsletter promotion the current vehicle.

CTA is a preset dropdown on most formats rather than free text. Check the format before writing one.

### The rules that actually constrain the writing

- **150 characters, then the fold.** The truncation is really "about two rendered lines on mobile", which varies with character width, but 150 is the working number. Everything load-bearing goes before it: the hook, the specific, the reason to keep reading. Never the CTA at the end of a paragraph.
- **70-character headline.** Sits below the image and is frequently the only line a scroller reads after the visual.
- **Mobile first.** Over half of engagement is mobile. Design text in the image at roughly 40pt equivalent so it survives a 1200x1200 rendered at phone width. If it needs pinching, it does not exist.
- **Dark mode.** LinkedIn has a dark UI. Hard-coded white backgrounds clip and dark text vanishes. Design so the asset survives both, or use a background that is neither.
- **Silent by default.** A large majority of video plays run with no sound. Burned-in captions are mandatory.
- **Text in image is fine here.** Unlike Meta, LinkedIn does not penalise text-heavy statics, and analyst-style graphics perform well because the audience is reading.

---

## 2. LinkedIn: benchmarks

Every number here is directional. Account-specific factors, audience size, bid strategy, creative quality and seasonality swamp the "typical" figure, and published benchmarks for the same metric range across an order of magnitude depending on methodology. Use these to sanity-check, never to set a target in a plan without saying where the number came from.

The two most methodologically transparent sources found are worth preferring over aggregator roundups: an independent study of 761 B2B creatives with a stated 1,000-impression threshold, and a 70-company, $28M-spend analysis. Both are cited below.

| Metric | Value | Source, year |
|---|---|---|
| CTR, median across 761 B2B creatives (thought leader excluded) | 0.47% median, top quartile 0.59%+, top decile 0.74%+, best 1.46%+ | Cognism creative study, 2026 |
| CTR by format | Document ~1.38%, carousel ~0.78%, video ~0.71%, single image ~0.54% | Digital Applied, 2026 |
| CTR, blended B2B SaaS | 0.74% average | Digital Applied 2026, HockeyStack 2026 |
| Engagement rate, standard | 0.90% median, top decile 1.81%+ | Cognism, 2026 |
| Engagement rate, thought leader | 1.72% median, top decile 6.21%+ | Cognism, 2026 |
| Dwell time | 4.21s median, top decile 6.81s+ | Cognism, 2026 |
| Creative-level conversion rate | 3.03% median, top quartile 8.33%+. Only about 25% of creatives convert at all | Cognism, 2026 |
| CPC | $6.04 average, wider sources give $5 to $16 | Digital Applied 2026, HockeyStack 2026 |
| CPM | $31 to $38 | Digital Applied, Meet-Lea, 2026 |
| CPL | ~$79 average | LinkedIn Marketing Solutions composite, 2026 |
| Lead gen form conversion vs landing page | 8.2% native form vs ~2.4% landing page | Digital Applied, 2026 |
| MQL to SQO cycle | 24 days to 68 days across quarters | HockeyStack, 2025 |
| Non-ICP budget leakage | 32% average across B2B SaaS, **HR Tech worst at 37%** | GrowthSpree audit, 56 accounts, $9.4M spend, 2026 |

That last row deserves attention. HR tech is the worst-leaking category in the sample, which shows how noisy LinkedIn's job-function and seniority fields can be for one specific buyer profile. Check whether your own category appears in a leakage study before assuming the average applies to it. It is a targeting problem rather than a creative one, so it belongs to `paid-ads`, but it is worth knowing that a weak result may be an audience artefact rather than a creative failure.

Thought Leader Ad CTR figures circulating at 5 to 8 percent are vendor-sourced and almost certainly selection-biased. The independent study explicitly excluded thought leader ads from its CTR analysis because "see more" expansions on long posts inflate click counts. Treat any thought leader CTR comparison as unreliable and judge the format on engagement and dwell instead.

---

## 3. Meta, for when it opens

Secondary channel. Enough here to brief against when it opens. These are standard published values rather than figures the research behind this skill verified, so confirm every one in Ads Manager before the first build.

| Element | Limit |
|---|---|
| Primary text | 125 chars visible, up to 2,200 |
| Headline | 40 chars recommended |
| Description | 30 chars recommended |
| Feed image | 1080x1080 (1:1) or 1080x1350 (4:5) |
| Stories and Reels | 1080x1920 (9:16) |
| Video | MP4. 15 to 30s, shorter generally better for cold feed placements. This is LinkedIn precedent, there is no Meta-specific read here |

What actually changes when you get there, beyond the numbers:

- **Polish is penalised harder.** The native, unproduced look matters more on Meta than on LinkedIn, and text-heavy statics that work on LinkedIn generally do not travel.
- **Video is weighted much more heavily**, and hook rate at three seconds becomes a primary diagnostic rather than a nice-to-have.
- **Volume thresholds become reachable.** Meta's learning phase wants roughly 50 conversions per ad set per week. On LinkedIn at B2B budgets that is usually out of reach; on Meta it is not, which means variable-level testing becomes worth running rather than a waste of budget.
- **Advantage+ and dynamic creative** will auto-combine components and find the best mix. That outsources variable-level testing to the platform and costs you visibility into why something won. Disable creative auto-enhancements while testing, or the asset being measured is not the asset that was built.
- **Targeting is far weaker for B2B.** The audience precision that makes LinkedIn expensive is what makes it worth the price. Meta creative has to do the qualifying that LinkedIn targeting does, which pushes ICP call-out and identity angles up the list.

---

## 4. Validation checklist before delivery

For every piece of copy in a brief:

- [ ] Character count stated, and under the limit for its slot
- [ ] Intro text hook lands inside the first 150 characters
- [ ] Headline works alone, without the image
- [ ] In-image text legible at phone width
- [ ] Asset survives light and dark mode
- [ ] Captions specified for any video
- [ ] CTA exists as a preset for that format, or is written as free text only where the format allows it
- [ ] No banned or hedging phrase from your register and writing rules, per `inputs.md`
- [ ] No unverifiable superlative, which is the most common LinkedIn rejection trigger
- [ ] No competitor logo, and no competitor name unless it has been escalated and approved
- [ ] Every number traced to the verification tracker, marked [SAFE] or [NEEDS VERIFY]
- [ ] Landing destination matches what the ad promised
