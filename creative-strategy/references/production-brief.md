# The production brief, copy variations, and QC

Two documents come out of a creative run, and collapsing them is why designers ask questions the brief already answered.

| Document | Audience | Answers |
|---|---|---|
| **Strategy brief** (`brief-template.md`) | Whoever approves the argument: the marketing lead, the founder, the brand owner | Why this argument, to whom, backed by what, and what was cut |
| **Production brief** (this file) | Whoever builds the asset, including future-you | Exactly what to make, at what spec, by when, and what "done" looks like |

The strategy brief carries the reasoning. The production brief carries no reasoning at all. A builder should never have to read an eight-section positioning argument to find an aspect ratio.

Write it to your team's marketing or campaign folder as `<YYYY-MM-DD>-creative-<slug>-production.md`, alongside the strategy brief.

**The sustainability constraint, stated up front.** The best-documented high-volume production shops report budgeting one to two hours per brief. If a production brief takes longer than that, the standard has migrated into the brief when it belongs in a checklist. Sections 6 and 7 exist to keep the brief short: the QC gates carry the quality bar so the brief does not have to restate it every time.

---

## 1. The asset list

One row per deliverable. This is the first thing in the production brief and often the only thing a builder reads twice.

| Field | Example |
|---|---|
| Asset ID | `C2-A` |
| Concept it serves | C2, the published-limitations statement card |
| Type | Static, single image |
| Platform and placement | LinkedIn feed, sponsored content |
| Dimensions and ratio | 1200 × 1200, 1:1 |
| File format and cap | PNG, under 5MB |
| Copy it carries | In-image headline, plus the feed copy set below |
| Dependency | None, or the named blocker |
| Owner | Named person |
| Due | Date |

**Asset IDs join to concept IDs, which join to the learning log.** `C2-A` and `C2-B` are two executions of concept C2. This is the join that most programmes break: the naming convention covers campaigns, ad sets, ads and UTMs, and stops before the creative files, so a designer's exports cannot be traced back to the concept they were briefed from. Name the files and the chain holds.

**File naming has to join to the ad naming, or the chain still breaks.** The `creative-testing` skill names ads and UTM content as `{conceptID}_{angle}_{format}_{variant}`, lowercase, underscore-separated, for example `C2_datatrust_simg_a`. The creative filename carries the same token set plus a date and a ratio:

```
<YYYY-MM-DD>_<conceptID>_<angle-slug>_<format>_<variant>_<ratio>.<ext>
2026-03-11_C2_datatrust_simg_a_1x1.png
```

Underscores, lowercase variant letter, and **the angle slug is not optional**: it is the load-bearing token in the log convention and dropping it is what makes a file unjoinable to its performance history. A typo in a slug silently splits an angle's history in two, so copy the slug from the log entry rather than retyping it.

---

## 2. Static assets

The wireframe is the brief. `visualisation.md` has the notation and the fidelity ladder; use it rather than prose. A wireframe states layout zones, what occupies each, the exact copy in each, at the correct aspect ratio, and it is cheap enough to throw away, which is the point.

Add to the wireframe, per asset:

- **Exact in-image copy**, with character counts. Not a description of the copy.
- **Visual register**: product screenshot, data visualisation, illustration, human, text-only. Named, because it is one of the six diversity dimensions and it drifts during production.
- **Two to four reference ads**, as images or links, with one line each on *what* to take from it. A reference with no note gets copied wholesale, including the parts you did not mean.
- **Dark mode check.** Feeds render in both. An asset with a white background and a transparent logo disappears in one of them.
- **Mobile legibility.** Assume a thumb-sized render. Smallest type has to survive it.

Two prohibitions that carry real exposure:

**Never generate or mock a product screenshot.** A fabricated UI is discovered by a journalist or by a competitor calling the named customer, and it is the most damaging category of marketing failure in this space. Screenshots come from the product.

**Never generate text inside an image and ship it.** Current top image models render headline-length text accurately and still degrade on small type and body blocks. Generate backgrounds, scenes and illustration; composite the type as a real layer in real layout tooling. Say which assets in the set used generation, and label concept-stage renders as rough, because stakeholders anchor on anything that looks finished.

**Brand assets.** The brief names the font files, colour tokens, logo lockup and template location, or it names the fact that they were not available. Unlocated brand assets are one of the most common causes of production stalls, so state the gap rather than leaving the builder to find it.

---

## 3. Video and Thought Leader assets

Video needs two things a static does not: a shot list and a line-by-line table.

**Shot list.** Bullet per shot, in order, each stating what is on screen and why it is there. Plus: hook variations, meaning two or three alternative opening three seconds as exact script lines, so the opener can be swapped without a reshoot.

**The line-by-line table.** Three columns, one row per beat. This is the single most useful convention in production briefing and it is what an editor actually needs.

| Voiceover / spoken | On-screen text | Visual |
|---|---|---|
| "Nine tools to update when one record changes." | 9 TOOLS | Slow pan across a list of app icons |
| "Here is the one that does it once." | (none) | Product screen, real capture, approval step visible |

Fill every cell or write `(none)`. An empty cell reads as an oversight and gets filled by whoever is editing at 6pm.

Also specify: total length, captions (mandatory, burnt in), aspect ratio per placement, whether audio carries information or only atmosphere, and where the product first appears.

**Thought Leader Ads are a different job.** No headline, no CTA button, up to 3,000 characters, and they promote an organic post from a person's profile rather than a purpose-built asset. So the production brief for a TLA is: the post copy in full, the first 150 **characters** treated as the hook because that is where the post truncates, the creator named, the permission step confirmed, and any media as a secondary asset. Any video attached follows `format-library.md` on production values: informally framed but properly lit beats both a slick corporate reel and genuinely amateur footage. Links in the post body and heavy calls to action in the post text both hurt. And the permission mechanic is a dependency with a human on the end of it, so it belongs in the register in section 5.

---

## 4. Copy variations

Once the angle and mechanic are locked, the copy job is bounded. Run it here rather than handing off.

**A note on the handoff.** A general-purpose bulk-copy tool is fine for mechanics: waves, variant counts, CSV output. It is not an authority on your channel or your voice. Your own platform specs in `platform-specs.md` and your own writing rules override anything it produces, including character limits, format coverage and example angles. Use it for mechanics where the volume justifies it, and never run it as an unattended downstream step.

**What to vary, and what to hold.** Vary one layer at a time or the result is unreadable.

- **Copy variants** hold the visual constant and vary intro text and headline.
- **Visual variants** hold intro and headline identical and change the image only.
- **Offer variants** hold the message and swap what is being offered.

**Per LinkedIn single-image concept, produce:**

- Intro text: 3 to 5 variants. First 150 characters must carry the argument on their own, because that is where it truncates.
- Headline: 3 to 5 variants at 70 characters or under. Each has to work independently, since headline and intro get read as a pair by some viewers and separately by others.
- Description: 1 to 2, and note that it renders on desktop only.
- In-image copy where the format uses it.
- CTA: a preset on most formats. Check before writing one.

**Every line ships with its character count and a pass or fail against the limit.** A variant over the limit is not a variant, it is a rewrite request.

**Every claim is marked `[SAFE]` or `[NEEDS VERIFY: what]`.** Never hand over a mixed set without the labels. A verification gap discovered at upload time costs a day; discovered after launch it costs a retraction.

**Variant versioning.** Copy variants get the asset ID plus a numeral: `C2-A-01`. When a variant is revised after review it takes a new numeral rather than overwriting, so the learning log can distinguish "this line lost" from "this line was replaced".

---

## 5. The dependency register

The thing that stalls a creative programme is rarely weak creative. It is briefs outrunning production and approvals: concepts sitting unlaunched on a page that does not exist, a screenshot nobody captured, an engineering confirmation, an amplification budget, and a sign-off.

So every production brief ends with a register. Four columns, and the second two are the ones that make it work.

| Blocker | What unblocks it | Owner | Date asked |
|---|---|---|---|

Rules: one named person per row, never a team. A date the ask was made, so an unanswered ask is visible as an unanswered ask. And a blocker that has been open across two briefs gets escalated in the covering message rather than logged a third time.

**Consent sign-off gets its own row every time it applies**, because it is usually the highest-value unblock available and it tends to be owned by nobody by default. Any customer name, quote or number in a set is blocked until sign-off exists. Naming it as a row with an owner is the difference between a standing complaint and a request.

---

## 6. QC gates

Two gates. They carry the quality standard so the brief can stay short.

**Gate 1, pre-build handover.** Before the builder starts.

- Asset list complete, every row has dimensions, a format and an owner
- Exact copy present, not described, with character counts and pass or fail
- Every claim labelled `[SAFE]` or `[NEEDS VERIFY]`
- Reference assets attached, each with a note on what to take
- Dependencies logged with owners, and none of them silently assumed resolved
- Brand assets located, or their absence stated

**Gate 2, pre-launch.** After the asset exists, before it goes live. This is the gate almost everyone skips.

- **Does the finished asset still express the hypothesis it was briefed from?** Production drifts. If it no longer matches, either request the edit or revise the hypothesis, and record which you did. An asset launched against a hypothesis it no longer tests produces an unreadable result.
- Does the hook match the awareness state of the audience it is targeting?
- Renders correctly in light and dark, at mobile size, with the 150-character truncation applied
- Captions present and burnt in, on any video
- Landing destination exists, and its message matches the ad's
- Tracking parameters correct, and the angle slug spelled the same as in the log
- Nothing in the asset is a generated product UI
- Register sweep: no vendor characterisation where your rules forbid it, no unsubstantiated superlative, no hedges, no em dashes

For a full set, hand Gate 2 to a subagent with fresh eyes, the checklist, your capability baseline, your verification tracker and your brand and voice rules. Ask for per-item pass or fail with the offending line quoted. Fresh eyes catch the register and attribution failures a self-review argues its way past, which is exactly the class of defect that is expensive after launch and cheap before it.

---

## 7. Closing the loop

The production brief's last job is to make the result recordable.

Every asset that launches gets a row in the learning log with its concept ID, its asset ID, the hypothesis it tests, and the campaign and ad names it runs under.

**Check the log will actually hold a result before the first result lands.** A table with columns for hypothesis, status, result and what it taught has nowhere to put dates live, spend, impressions, click-through rate or cost per lead. The per-concept entry shape defined by the `creative-testing` skill holds all of that: opened and closed dates, a `Ran:` line with dates, spend and impressions, a result block with dwell, engagement and conversion counts, and an angle status. Use that one shape, so two skills are not writing to two schemas for one file. Fix it before the first result lands rather than after.

**The diagnostic ladder needs an account median to read against**, and that is the number it needs most. Keep an account baseline beside the learning log: click-through rate, dwell, engagement rate and cost per lead, by format and by audience, updated whenever a campaign closes. Create it on the first run that produces a number to put in it.

Then update the standing docs additively and dated: the angle library with any new territory and its status, the swipe file with the teardown, the learning log with the concepts entering test.
