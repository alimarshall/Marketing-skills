---
name: one-pagers
description: Build a single-page (or front-and-back) sales or marketing one-pager: a switching-fear leave-behind, a competitive battlecard distilled to one page, an objection-handling sheet, or a champion-enablement sheet. Use when the user asks for a "one-pager", "one-sheet", "leave-behind", "sell sheet" or a single-page comparison or summary, even without naming the format ("give reps something to hand a prospect evaluating Competitor A", "something the champion can forward internally"). Whenever a competitor is named or implied, checks that competitor's dossier and your capability baseline before any comparative claim goes on the page. Uses claim-verification and copy-register-check before handover, and the docx skill for the file.
---

# One-pagers

A one-pager only works if it says one thing, to one audience, and every claim on it survives contact with a sceptical reader. Sales one-pagers carry competitive and product claims, and those are exactly the claims that get caught in the room (a stat that reads as thin, a review framing that reads as defensive). So the point of this skill isn't just "make it look nice", it's "make it look nice using only claims that hold up".

## Inputs

Read `company-context.md` first (repo root, or search the workspace for it) and use the fields that apply to this skill. If the file or a line is missing, ask once, then offer to save the answer back to it. Never fill a gap with an assumption about the company. If `creative-strategy/references/inputs.md` is also filled in, it still applies; where the two differ, `company-context.md` wins.

Record these once in `creative-strategy/references/inputs.md` (the shared inputs contract), or fill them in here:

- One-pager design and style context (your brand layout file, if you keep one): `<fill in>`
- Competitor dossiers folder: `<fill in>`
- Capability baseline (including its list of contradicted or retired claims): `<fill in>`
- Fresher product-truth source (product wiki, release notes, roadmap notes): `<fill in>`
- Buyer-context docs (pain and emotion evidence): `<fill in>`
- Brand template or colours for the file: `<fill in>`

## Layout and copy principles

These are the general lessons that make one-pagers work. If you keep a project design-context file, read it too and treat it as binding where it is more specific.

- **Z-pattern scanning.** Readers skim top-left to top-right, diagonally down, then across the bottom. Put the headline top-left, the proof band across the top, and the CTA bottom-right where the eye lands last.
- **Two-column body.** Two sections side by side, each with three or four tightened bullets, reads faster than one long column.
- **About 40% white space.** If the page looks full, it is too full. Cut content before shrinking type or margins.
- **Two to four points per section, every word earning its place.** If a bullet needs a second line to make sense, it is two bullets or none.
- **Comparison tables for competitive pages.** Four to six rows, colour-coded, only rows where every cell is verified.
- **One shared caveat line** at the foot rather than a caveat on every bullet. Per-bullet hedging reads as nervous.
- **Process facts over small-sample ratios.** Don't headline a small-numerator ratio (for example "N of several hundred" customers doing something) as your strongest proof point; it invites "what about the rest?" instead of landing as confident. Concrete process facts (implementation timelines, response-time targets, what's shipped versus roadmap) carry more weight than stats that need a footnote.
- **State your own strength positively; no review-dunking.** Don't lead with a defensive review-floor stat (for example "no low-star reviews") or with a competitor's bad reviews. Lead with what your good reviews and customers actually praise, stated as your own strength. Dunking on a competitor reads as insecure and invites the reader to go and check.

## Before drafting anything

1. **Read the design and content context** (your file if you have one, plus the principles above).

2. **If a competitor is named or implied**, read that competitor's dossier before writing a single comparative sentence. Also check your capability baseline, especially any section listing claims that sound right but aren't accurate as stated (typical examples: a service tier described as universal when only some plans get it, a field-level capability that is really partial, a blanket uptime figure that isn't contractual). A one-pager that repeats one of those is worse than one that says less, because it'll get caught in the room. Use `capability-boundary-map` if you need to know where the product's real edges are.

3. **Check your fresher product-truth source** before finalising any product or positioning claim; product truth moves faster than any static file. If it contradicts the baseline or a dossier, it is usually the fresher source: flag the discrepancy rather than silently picking one, and pass the correction to `source-doc-writeback`.

4. **Handle named quotes carefully.** Anything sourced from call recordings, win/loss interviews, or named customer or prospect quotes is internal-use-only unless that specific account has signed off for external use; consent travels with the quote, and the restriction is often stated in the dossier itself. If the one-pager wants that kind of material, build it in two tiers: a prospect-safe page using aggregate stats and paraphrased findings, plus a clearly banner-flagged internal-only page (or appendix) carrying the named talking points, guardrails, and quotes. Never blend the two.

## Workflow

1. **Clarify scope in one pass, don't over-ask.** Who reads this (prospect, champion, internal rep)? What's the one fear, objection or message it needs to resolve? Is a specific competitor involved? If the user's ask already answers these, don't stop to ask; proceed and state your assumptions.
2. **Gather facts in this order:** design context (for structure and style), then competitor dossier and capability baseline if competitive, then the fresher product-truth source for anything product or positioning related, then buyer-context docs if the one-pager needs pain or emotion evidence.
3. **Draft using this structure:** eyebrow plus outcome-led headline; one or two sentences of framing; a stat or proof band (process facts over small-sample ratios); a two-column body (two sections of three or four tightened bullets); one shared caveat line; a comparison table if competitive (colour-coded, four to six rows); a CTA bar with a primary ask plus a lower-commitment fallback.
4. **Verify claims.** Run `claim-verification` on every product, competitor and numeric claim, and `copy-register-check` against your house register rules. Never invent a product fact, customer quote, stat or competitor capability to fill a slot; leave the slot out.
5. **Build the actual file.** Use the `docx` skill for Word-doc mechanics (page size, tables, bullets, its known gotchas). Don't just describe the one-pager in chat; produce the file.
6. **Verify the render.** Render the doc to PDF and then to an image, and actually look at it: check the layout isn't overflowing, text isn't clipped, and the comparison table reads cleanly. A page can look complete in the XML and render nearly empty.
7. **Flag internal-only pages explicitly** when the doc has them, and say so plainly when you hand it over: which page is safe to forward, which isn't.

## A note on tone

Confidence in a one-pager comes from concrete, verifiable process facts more than from stats that need a footnote to make sense. When in doubt about whether a claim is strong enough to headline versus better as supporting detail, prefer the one a sceptical reader can't immediately poke a hole in.
