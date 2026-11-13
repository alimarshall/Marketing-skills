---
name: product-capability-refresh
description: Fold a shipped or materially changed feature of your own product into the standing capability and competitive-intelligence docs, everywhere it is referenced. Use when a feature ships, the product team posts a "what's new" or release note, or the user says "we just shipped X, update the capability docs", "fold this into our product context" or "update the matrices", and wants internal reference docs (not external copy) kept accurate. Distinct from positioning-brief, which decides what to say externally; this skill keeps the ground truth (capability baseline, matrices, differentiation reference, competitor dossiers) correct so every other skill works from it. Run before positioning-brief; pair with competitor-buyer-sweep for buyer reaction and capability-boundary-map for what the feature does not do.
---

## What this skill does

A competitive-intelligence practice usually runs on a small set of standing internal reference docs that everything else (positioning briefs, ad copy, one-pagers, sales enablement) treats as ground truth. When the product itself changes, ships a new version, or gets new detail from the product team, those docs need to change too, and they need to change in every place that references the affected capability, not just the one doc someone happened to update first. This skill is the checklist for doing that completely. It comes from a real fold-in: a major version of an AI assistant feature touched five different docs plus their mirrored copies, and the first pass missed three of them.

**This is not a positioning or messaging skill.** It does not decide what to say publicly about the change; that is `positioning-brief`. It keeps the internal record accurate: what the feature actually does, what it does not do yet, how it compares to the competitor capability it is usually discussed alongside, and which claims are now stale. Run this first when a feature ships, then hand off to `positioning-brief` if external copy is also needed.

## Inputs

Read `company-context.md` first (repo root, or search the workspace for it) and use the fields that apply to this skill. If the file or a line is missing, ask once, then offer to save the answer back to it. Never fill a gap with an assumption about the company. If `creative-strategy/references/inputs.md` is also filled in, it still applies; where the two differ, `company-context.md` wins.

Record your own paths in `creative-strategy/references/inputs.md`. This skill needs:

- **Capability baseline folder:** `<fill in>` (one file per tracked capability).
- **Features communication matrix:** `<fill in>`.
- **Master capability matrix:** `<fill in>`.
- **Product differentiation reference:** `<fill in>`.
- **Competitor dossiers:** `<fill in>`.
- **Mirrors:** the paired page for each doc above, if you keep mirrored copies (for example in Notion). Same doc set and mapping as `competitor-buyer-sweep`.
- **Public help centre or FAQ:** `<fill in>`.
- **Project memory file:** `<fill in>` (if one exists).

## Step 1: read the source material completely before writing anything

Get the actual product-team announcement, release note, PRD or changelog, not a secondhand description. If it lives in a wiki, fetch it directly. Read it end to end and extract:

- **What is genuinely new or changed**, in the product team's own words where possible.
- **What it explicitly does NOT do.** Release notes usually say this less clearly than what it does; look for it anyway, because it is the part most likely to get overclaimed in copy later. A regression (something the old version could do that the new one cannot) is just as important to capture as a new capability. `capability-boundary-map` is the fuller tool for this.
- **Any numbers that are temporary or likely to change** (usage caps, beta gating, rollout percentages). Flag these as dated facts, not durable claims.
- **The model, vendor or technical dependency**, if the source names one. Do not assume it is the same as a related but different feature. Two AI features in the same product can run on different models, and a claim that holds for one may not hold for the other; check rather than assume.

## Step 2: update the capability baseline doc

Every tracked capability has (or should have) a dedicated file in the capability baseline folder. Find or create the one for this feature. Structure it around:

1. **Product truth, as shipped.** The real, current feature set, sourced to the release note.
2. **What it does NOT do: read this before making any claim.** The regressions, gaps and not-yet-built items from Step 1. This section exists specifically to stop a future draft from overclaiming.
3. **Marketing angles the product team itself suggested,** if the release note offered any. Worth carrying forward as a starting point, not as verbatim copy.
4. **Own-docs and external-friction reality.** Check the public help centre or FAQ for this feature. If it is stale (wrong model name, "still in beta" language that is no longer true), say so explicitly. Own-docs drift is a common, recurring gap, and buyers and AI search engines read those pages.
5. **Verdict against current claims.** The most important section. Does this change close a gap against a named competitor, or does it narrow the gap without closing it? Be precise: "narrower gap on X, same gap on Y" is more honest and more useful than "we caught up". **Do not upgrade a competitive rating just because something shipped.** Check whether the specific dimension that mattered (not just the general capability) actually changed.

## Step 3: update the shared matrices

Two docs cover every capability across all competitors. Both need the same update, each in its own format:

- **Features communication matrix:** find the row for this capability (by tier, if your matrix is tiered). Update the description cell with the real shipped feature set, and the competitive-angle cell with the sharpened comparison from Step 2's verdict. Replace the old text in place. At most, bump the one-line version note at the top; no dated changelog paragraphs.
- **Master capability matrix:** find the row in the relevant table. Update only your own product's cell. Leave the competitor's cell alone unless something about them changed too, and never overwrite a manual annotation the user added to a cell: that is protected content. This doc is a deliberately compressed index, so keep the edit short.

## Step 4: check whether the differentiation reference needs a note

The product differentiation reference holds the numbered differentiation claims. Most product updates are NOT a standalone new claim; they are detail behind an existing claim. If so, edit that claim in place so it states the current truth, including what did NOT change: which claims this update should not be read as strengthening. No dated notes. This is the typical case for an incremental major version: real progress, but explicitly not enough to change the standing claim about the competitor's capability.

## Step 5: check the relevant competitor dossier

If the update changes a head-to-head comparison (it usually does; most tracked capabilities are tracked because of a named competitor comparison), update that competitor's dossier too, in its competitive summary table and its weaknesses or genuine differentiators sections as appropriate. Do not assume the comparison shifted in your favour just because you shipped something. Check the actual dimension that mattered.

## Step 6: propagate before calling it done

This is the step most likely to get skipped, and the one that caused the real gap this skill was built from (three docs missed on the first pass). Before finishing, explicitly list every doc that references this capability or this competitor comparison, not just the ones you started with, and confirm each one either already reflects the update or now does.

The default five to check every time:

1. the capability baseline file
2. the features communication matrix
3. the master capability matrix
4. the differentiation reference
5. the relevant competitor dossier

A feature with its own positioning history may also need a per-capability, per-agent or per-pillar buyer context doc checked if one exists (see `capability-pillar-research`).

## Step 7: mirror the edits

If every doc has a mirrored copy (for example a Notion page), update each mirror in the same pass. Use the same doc-to-mirror mapping as `competitor-buyer-sweep`. Re-fetch each mirror page before editing: content normalises differently there (tables become HTML-like blocks, punctuation may be stored differently from the source markdown), so construct your edits against what is actually stored, not what the source would produce. If a mirror page has a manual edit or annotation that does not match what the source would generate, treat it as the user's own edit and leave it alone; append your update alongside it instead of overwriting.

## Step 8: log it and report back

Add a dated entry to the sweep log and the project memory file (if they exist; the only places dated notes belong) covering what shipped, which docs changed and how, and the verdict from Step 2 (what closed, what did not). Report back concisely: what changed, which docs were touched (and which were checked and already current), and the one-line honest verdict on competitive positioning. Do not bury the verdict in a long recap.

## When this overlaps with competitor-buyer-sweep

Both skills touch the same doc set. The difference is the trigger and the direction of the update: `competitor-buyer-sweep` looks outward for new buyer or competitor evidence and folds it in; this skill looks inward at a change to your own product and updates how it is represented everywhere it is compared. If a single session needs both (a feature ships, and you also want a fresh call-recording pass on how buyers are reacting to it), run this skill first, then `competitor-buyer-sweep`.

## Works with

- **Updates:** `competitive-matrices` docs (capability baseline, capability matrix, communication matrix, differentiation reference, verification tracker) and the comparison sections of `competitor-dossiers`.
- **Then hand to:** `claim-propagation-sweep` to find copy, ads, landing-page briefs and sales assets that still state the old fact; `use-case-evidence-research` and `capability-pillar-research` if a use-case doc or pillar describes the feature; `positioning-brief` if the change needs new external messaging.
- **Hub:** `competitive-intel-system`. Same house rules: edit in place, no dated notes in shared docs, shipped means shipped.
