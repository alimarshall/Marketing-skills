---
name: competitor-buyer-sweep
description: Recurring sweep that keeps your competitive-intelligence and buyer-research docs current, merging new buyer language and competitor mentions into the right section in place (no dated notes) and propagating each finding to every doc that shares the same ground. Use when the user says "run the buyer sweep", "check for new competitor mentions", "update competitor analysis" or "update buyer research", shares a non-call source (case study interview, sales battlecard, competitor site or FAQ), or asks to fold in or re-verify a competitor claim. Can run on a schedule against your call recorder (for example Gong). For inward product changes use product-capability-refresh; for regrouping research by verb use capability-pillar-research; for claim checks use claim-verification.
---

## What this skill does

Keeps your competitive-intelligence and buyer-research documentation current. It scans for new buyer-language signals (sales and customer calls, named competitor mentions) since the last sweep, or folds in a specific source the user hands over directly (a case study interview, a sales battlecard, a competitor's own site), and adds anything genuinely new to the standing reference docs, additively, in the docs' established house style. This is a maintenance sweep, not a one-off research project: most runs find a modest amount of new material, not a rebuild.

**Scheduled and on-demand runs.** The call-recorder half of this process can run on a schedule (for example weekly) against your call recorder, such as Gong. Use this skill for on-demand, mid-conversation runs ("run the buyer sweep now") and for any non-call source, which a scheduled job usually cannot reach. If you run both, keep the shared steps in sync (the Step 3 target-doc list, the Step 4 classification, the Step 4.5 propagation check): if you improve one, update the other to match.

## Inputs

Record your own paths in `creative-strategy/references/inputs.md`. This skill needs:

- **Sweep log:** `<fill in>` (dated entries, one per run).
- **Call recorder access:** `<fill in>` (where the API credentials live, the API base URL for your workspace).
- **Product-line screen:** `<fill in>` (if several products share one call-recorder workspace: the account domains and call-title keywords that mark each product line, and the default).
- **Tracked competitors:** `<fill in>` (per product line).
- **The target doc set:** paths for each doc in Step 3, and the paired mirror page for each if you keep one (for example in Notion).
- **Verification tracker:** `<fill in>` (spreadsheet of documented product gaps, if you keep one).
- **Project memory file:** `<fill in>` (if one exists).

## Step 0: get the date range (call-recorder path only)

Read the sweep log first. Its last dated entry marks the end of the previous run's window; start from there through today. If unclear, fall back to a lookback slightly longer than your run interval (for a weekly run, about 9 days) so nothing falls in a gap. Skip this step entirely for a non-call source and go straight to Step 3.

## Step 1: identify the source and get access

Two source types; handle whichever applies.

**Call recorder (the recurring case):** use your recorder's API directly for bulk survey work. For Gong, that is the REST API with Basic Auth (base64 of `AccessKeyId:AccessKeySecret`) against your workspace's base URL, called from a script (for example Python `requests`). Connector or MCP wrappers are usually built for single-call lookups, not bulk surveys; do not spend time looking for one. The `gong-transcripts` skill, if you have it, holds the credential handling.

**Non-call (the user hands you something directly, or asks you to check something live):** treat any of the following as a first-class evidence source, equally valid, just tagged differently in the docs:

- A case study or customer interview transcript. Tag findings "case study interview, not call recording" in the docs.
- A sales battlecard or other internal competitive doc the user shares or names.
- A live check of a competitor's own website, FAQ or product pages, when the user asks you to verify or re-verify a specific claim about what a competitor does. Fetch the page directly (web fetch or browser tools), quote the live text verbatim, and date the citation with today's date, not the date of whatever earlier research first made the claim. **Re-verify, do not just re-cite:** if an existing doc cites a competitor's own site or FAQ and it has been more than a few weeks, or the user questions it, treat that as a live-check trigger. Competitor pages change.
- A direct correction or steer from the user about a specific fact.

For a non-call source, skip Steps 0 and 2 and the call-specific parts of Step 3. Go straight to reading the source, identifying which target docs it touches (Step 3 list), and classifying (Step 4).

## Step 2: pull the call window and screen for relevance (call-recorder path only)

Query the recorder for the date range from Step 0. For Gong, use `/v2/calls/extensive` with a parties-only content selector first, and pull full transcripts only for calls worth mining; this keeps the survey cheap.

If several products share one workspace, screen every call for product line using the product-line screen from Inputs (external party email domains and call title keywords). Anything that matches nothing defaults to the default product line unless the content says otherwise.

Prioritise:

- calls mentioning a tracked competitor by name
- calls from an account not yet covered in the research
- demo, kickoff, QBR, churn and renewal calls

## Step 3: read every target doc before editing

Read all of them before making a single edit, so you know what each already says. A typical set, by role:

Shared across product lines:

1. **Competitor dossiers**, one per tracked competitor, plus any hub page that indexes them.
2. **Product differentiation reference:** the numbered differentiation claims.
3. **Features communication matrix:** per-capability description and competitive-angle cells, per product line.
4. **Master capability matrix:** keep this one a stable compressed index. Short cell updates only, never verbatim quotes.

Per product line:

5. **Buyer research:** buyer context and buyer interests and aspirations docs.
6. **Jobs and industries reference:** jobs to be done by vertical or industry.
7. **Per-capability or per-agent buyer context docs**, if the product is organised that way.
8. **Pillar-regrouped buyer context:** the same research regrouped by verb-based pillar (see `capability-pillar-research`). Keep it in sync with #7: same underlying evidence, different grouping.

Also check the verification tracker, if you keep one. Append a new row if a genuinely new, previously undocumented product gap surfaces.

## Step 4: classify and merge findings in place

The docs are read cold by sales and marketing, so they stay finished: findings are merged into the right section, never appended as dated notes.

- **Fits an existing theme or claim:** add the quote under that theme (or as proof under that claim) and update the account count in its pattern line. Skip it if it says nothing the existing quotes don't.
- **New topic, high-volume doc** (the top competitor dossiers and the buyer research pages listed in `company-context.md`): 1-2 distinct accounts go as one bullet in the "Emerging signals" toggle at the end of the right group or pillar (topic label, account, verbatim quote). At 3+ distinct accounts, promote it to a theme with a pattern line and all its quotes, and remove the bullets from Emerging signals.
- **New topic, any other doc:** add it straight in as a theme with a pattern line naming the account(s).
- **Changed fact** (a competitor launch, price change, acquisition, or a capability you got wrong): edit the right section in place (snapshot, scope, AI and MCP, summary table, where they win / where we win, at a glance) and replace the outdated statement. Don't keep both.
- **Genuinely new product gap:** add a row to the verification tracker.
- **Nothing new:** skip silently.

House style, non-negotiable:

- **Never write meta text into shared docs:** no "added <date>", "<date> additions", "UPDATE", "fresh evidence added", "re-verified", "flagged for", "TBD", "conflict flagged", running counts, mirror notes, file references, changelogs, or narration about who told whom. Those go in the sweep log and the summary.
- **Sales intel beats vendor marketing.** If reps say a competitor capability is X and the vendor's docs say Y, write X. Mention the vendor claim once at most, never as the basis of a rating.
- Never fabricate a quote or stat. Verify anything specific by re-reading the source before using it (run `scripts/verify_quotes.py` if installed); fabrications do slip into research docs, and this is where they get caught.
- Call quotes are internal use only until the customer signs off. The doc carries one consent line at the top; don't tag every bullet.
- Genuine conflicts between buyers get one plain line: "Mixed evidence: A says..., B says...".
- If you keep mirrored copies (for example a Notion page per doc), mirror every edit in the same pass, in the same position, inside the right toggle. Re-fetch the mirror page before editing, because tables and punctuation often store as normalised blocks that will not match raw markdown. Never append blocks at the bottom of a mirror page. If the mirror has a manual edit the source doesn't, keep it and edit around it.
- Follow your house register rules (run `copy-register-check` if in doubt).

## Step 4.5: propagate to every sibling doc that shares the same ground, not just the first one you touch

This is the step that most often gets skipped, and the one most worth double-checking before calling a fold-in done. A single competitive finding (a new pain point, a re-verified claim, a corrected fact) is rarely relevant to only one doc. Before finishing:

1. Name every doc in the Step 3 list that references the same competitor **and** the same capability or claim area, not just the one you started in. A finding about, say, a competitor's AI assistant is likely relevant at once to that competitor's dossier, the master capability matrix's AI assistant row, the differentiation reference's claim about that assistant, the features communication matrix's competitive-angle cell for it, and the capability baseline file for your own equivalent feature.
2. Check each one explicitly. Do not assume a doc is current just because a sibling doc was recently touched. A finding added in one thread or session does not automatically appear in another doc's text, even when both cover the same competitor and the same feature.
3. If a doc is missing the finding, add it there too, in that doc's own established style and tier: a compressed-index doc gets a short cell note, a narrative doc gets the fuller version with the quote.
4. Say explicitly, in your summary to the user, which docs you checked and confirmed already current, and which ones you found missing the finding and updated. "Checked X, Y and Z, all three needed the update, W already had it" is the useful version of this report, not "updated the relevant docs".

This step exists because of a real failure pattern: a finding about a competitor's AI producing wrong answers, gathered from a case study interview, was correctly added to that competitor's dossier and the master capability matrix the day it was gathered, but not to the differentiation reference, the features communication matrix or the capability baseline file, all of which covered exactly the same head-to-head ground. It surfaced only when someone asked for a double check.

## Step 5: close the loop

- Append a new dated entry to the sweep log (the only place dated notes live): the date range covered (or "non-call source: [what it was]" if this run was not call-driven), what was found, what was added and where (including the Step 4.5 propagation results), and anything flagged.
- Update the project memory file if one exists.
- Report a summary under 150 words: what changed, what did not, which docs were checked for propagation, and anything needing a decision.

A clean sweep with nothing new is a fine, plainly stated outcome. Do not pad the report.

## Works with

- **Feeds:** `competitor-dossiers` (deal intelligence, facts), `buyer-research` (VOC library and pillars), `use-case-evidence-research` and `vertical-persona-research` (the same evidence cut by use case or vertical), `competitive-matrices` (cells, claims, angles, tracker).
- **Hands off:** our own product changed → `product-capability-refresh`; copy, ads or pages now state an old fact → `claim-propagation-sweep`; a source doc is wrong → `source-doc-writeback`.
- **Hub:** `competitive-intel-system` holds the doc set and how it connects.
