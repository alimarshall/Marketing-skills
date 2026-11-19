---
name: "call-research-trend-analysis"
description: "Tag every buyer company's sales-call transcripts on a fixed rubric (jobs, fears, frustrations, hopes, data issues), verify quotes, and turn it into shares and quarterly trends with a projected current quarter."
---

# Call research trend analysis

Use when someone asks "what % of buyers want X", "how has X changed over the year", "what are buyers scared of", "what jobs do they want the product to do", "add more categories", or wants a new data-led cut of sales-call research for posts, charts, sales enablement or campaigns.

## Works with

- **Takes in:** transcripts grouped per prospect company (call platform), the VOC library from buyer-research for emotion questions.
- **Produces:** a rubric, per-company tags with verified quotes, shares of companies per category and quarterly trends with a projected quarter.
- **Next:** research-data-charts (charts), vertical-persona-research (the same tagged evidence sliced by function, industry and role, so calls aren't mined twice), abm-account-multithread (one company's fears and hopes as openers), customer-proof-from-usage-reports (proof that answers the top fears), founder-pov-concepts and teach-then-sell-video-scripts (stats to quote), buyer-research (new themes worth adding). For a one-off themes summary of a batch of calls, use buyer-call-synthesis instead.

## Inputs

Read `company-context.md` first (repo root, or search the workspace for it) and use the fields that apply to this skill. If the file or a line is missing, ask once, then offer to save the answer back to it. Never fill a gap with an assumption about the company.
- **Your email domain(s):** used to tell your side of the call from the buyer's.
- **Transcripts grouped per company:** one file per prospect company holding all its relevant calls, with each line labelled as seller side or prospect side (e.g. `(SELLER)` / `(PROSPECT)`). Pull them from the call recorder (Gong, Chorus, Fathom and so on). If they don't exist yet, Step 0 builds them.
- **Grouping:** group by the prospect's email domain, never by call title. Keep only external calls of real length.
- **Company table:** one record per company with first call date, number of calls, relationship (prospect, customer, partner) and whether the call is substantive. Analyse substantive buyer conversations only.
- **Emotion questions:** an optional voice-of-customer (VoC) moments table (quote, emotion, theme, persona, company, date). If you don't have one, build it like a tagging pass: per call, the strongest 3 to 10 prospect moments with one emotion each (frustration, anxiety, skepticism, curiosity, confidence, excitement, relief, neutral), verified word for word. Drop neutral moments when reporting emotion shares. Separate existing customers from prospects when the question is about demo reactions.
- **Credentials:** never print or share API credentials.

## Method

**Step 0: build the evidence base (skip if it already exists).**
- Pull the call list for the date range with participants (name, email, title). Most APIs page with a cursor: save state after every page.
- Keep calls with at least one external participant whose domain isn't yours or a free-mail domain, longer than about 5 minutes, and matching the pipeline rule in `company-context.md`.
- Group by the external participants' email domain root (`acme.co.uk` and `acme.com` become one company when it's clearly the same business). Never group by call title.
- Pull transcripts in batches, map each speaker to a participant, and label each line `(SELLER)` if the speaker's domain is yours, otherwise `(PROSPECT)`.
- Write one file per company (every call with date, title and participants) and the company table. Substantive = the prospect speaks about their own situation (roughly 150+ words); no-shows, internal, vendor and recruiting calls are not substantive.

**Choosing categories for a new topic or market.** Start from existing buyer research, VoC themes, the capability catalogue and objection lists. If nothing exists, read about 15 varied companies, list every distinct item, and merge into 8 to 15 categories a stranger could apply the same way, plus `other`. Good starting lenses for any B2B product: jobs they want done, problems or frustrations today, fears about buying or rolling out, hopes or outcomes, why now, success measures, first use. Give each category a one-line definition with an include and exclude example.

1. **Check what's already tagged.** If existing tags answer the question, use them. Run a new pass only when the categories don't exist yet.
   - A keyword scan is fine for sizing, but it is never a chart number. Say so if you show one, because it counts mentions ("we're hiring 50 people") as needs.

2. **Write a rubric file before tagging.** It covers:
   - **Who counts:** prospect-side speech about their own company only. Sellers pitching don't count. A prospect only agreeing ("yeah") doesn't count. Ignore mislabelled seller lines.
   - **Categories:** fixed lists plus `other`, so results add up across companies. A mention alone isn't a need.
   - **Quotes:** every item needs a verbatim quote of 35 words or fewer that is an exact substring of one prospect line.
   - **Strictness:** be strict; when unsure, mark false.
   - **Output shape:** JSON, one object per company. Keep the speaker's name, title, call ID and date on every quote, so other skills can use it per person.

3. **Batch and run.**
   - Split the companies into about 6 batches balanced by file size.
   - Run one subagent per batch in parallel. Give each one the work folder, the rubric, its batch list and an output path. Ask it to run a quote check, fix failures, and reply with a one-line summary.
   - Only use heavier orchestration tools if the user explicitly opts in.

4. **Re-verify centrally.**
   - Merge the outputs and confirm every company is present.
   - Re-check every quote against that company's prospect lines yourself, and drop items whose quote fails.
   - Spot-read about 10 random quotes in the broadest category, and say if the tagging is generous.

5. **Aggregate.**
   - Share of companies = companies with at least one item in a category ÷ total companies. Each company counts once.
   - Also report the top (first-listed) item per company and the share of companies with any item at all.
   - Read the `other` details and summarise the interesting long tail in words.

6. **Trends over time.**
   - Group companies by the quarter of their first call. Leave out quarters with tiny counts.
   - Report each quarter and the change from the first to the last full quarter.
   - **Current-quarter projection:**
     - Fit a line through the full quarters, extend it to the current quarter, and clamp it to 0–100.
     - Blend that with the quarter-to-date share: projected = w × quarter-to-date share + (1 − w) × fitted value, where w = companies so far this quarter ÷ average companies per full quarter, capped at 1.
     - Needs at least 3 full quarters. With fewer, show the quarter-to-date figure only and label it partial.
     - Label the result "projected". Warn when it lands at 0 to 2%: that is the trend line running out, not a forecast.
   - **Check that a falling line is real.**
     - Compare average calls per company and average categories per company across the quarters.
     - If companies are simply naming fewer things, say so and offer the mix view: each category's share of all items mentioned that quarter, which adds to 100%.
     - The mix view is an honest way to show what's gaining attention.

7. **Cross-cuts that make good stories:**
   - What they hope the product will do vs the first thing they'd trust it to do.
   - Already using a similar tool vs not.
   - Customers of a major incumbent vs everyone else.
   - Top-down mandate or company initiative vs none.
   - Demo reactions: prospects only, with existing customers kept separate.

## Honesty rules
- **Don't make data look better than it is.** No cropped axes and no cherry-picked windows. When asked to make something look like it's rising, offer honest reframes: the mix view, a ranking with no time axis, or a "shorter, more focused list" story.
- **Small groups:** flag jumps in a single quarter. For small samples, prefer "7 in 10" over a precise percentage.
- **Denominators:** keep them honest in copy. "Share of companies we spoke to" is exact. "Share of conversations" is fine for social posts, but explain it if asked.
- **Quotes:** call quotes are internal. Paraphrase them externally, and never name the person or company without consent.
- **Exaggerations:** numbers buyers exaggerate in passing ("34 steps") are not statistics.

## Outputs
- **Working files:** keep the rubric and raw merged JSON together in a working folder, so the cut can be re-run.
- **Findings doc:** append a dated section to one running findings doc rather than starting a new file each time. It holds tables, the long tail and paraphrase-ready quotes marked internal.
- **Charts:** use the research-data-charts skill.
- **Reply in chat:** a short table of headline numbers, two or three things that stand out, and the caveats.

## Shared conventions

- Find inputs in the workspace first: the files other skills in this set produce (capability baseline, buyer research, VOC library, evidence docs, customer proof files, dossiers, matrices, approved claims). Ask only for what's missing. Never fill a gap with assumptions about the company.
- Never invent a capability, stat, quote or competitor fact. Quotes are verbatim; named customer material stays internal until the customer signs off.
- Claim tags are SAFE, NEEDS VERIFY: (what settles it) or INTERNAL ONLY. Keep the tags you receive and pass them on.
- The user's own writing rules and brand voice override the defaults in this skill.
