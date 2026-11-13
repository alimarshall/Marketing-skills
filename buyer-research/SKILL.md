---
name: "buyer-research"
description: "Build and maintain buyer research and a VOC (voice of customer) quote library for a B2B product from sales and customer call transcripts: pain pillars, aspiration and excitement pillars, cross-cutting objections, personas, per-use-case context, all with verbatim quotes. Use for \"what are buyers saying\", \"build buyer research\", \"pull themes and quotes\", \"buyer pains and what excites them\", \"VOC library\", \"update the buyer research\", \"pains per use case\", \"rescan the calls\", or \"clean up the buyer research page\"."
---

# Buyer research and the VOC library

Placeholders: **[Product]** (one buyer research page per product line), **[Call platform]**, **[Repo]**, **[Wiki]**.

## Works with

- **Takes in:** call transcripts (call platform), sales channel intel, CRM win/loss notes.
- **Produces:** the VOC quote library, one buyer research page per product line (pain and aspiration pillars, objections, personas) and optional per-use-case context.
- **Next:** use-case-evidence-research (evidence per use case), vertical-persona-research (personas by industry), call-research-trend-analysis (shares and trends), and the content skills (use-case-ad-variations, teach-then-sell-video-scripts, education-video-prep, founder-pov-concepts). competitor-dossiers draws its deal intelligence from the same library. competitive-intel-system runs this as one layer of the full doc set.

## 1. VOC library (the raw layer)
A spreadsheet with one row per verbatim quote. Columns: `id, quote, product, type, theme, outlook_angle, sector, speaker, role, company, persona, emotion, intensity (1-3), competitor, context, source_type, date, usage`.
- Types: Pain, Objection, Benefit, Desired outcome, Buying criteria, Fear/risk, Switching trigger, Why they left, Why they chose a competitor, Perception, Outlook, Proof/metric.
- Usage: Internal only (default for calls) / Case study, check sign-off / Public source.
- Add to it every week from new calls. Dedupe by checking whether the quote's text already exists.

## 2. Mining calls
1. Pull calls for the window. Get parties first, then full transcripts only for calls worth mining (demos, discovery, kickoffs, QBRs, renewals, churn).
2. Screen by product line and match accounts by external email domain, never by call title.
3. Keep only external speakers. Extract exact text. Attribute (Name, Role, Company, Mon YYYY).
4. For large volumes, use one subagent per batch of accounts with a written brief, then merge.
5. Verify programmatically: every quote must match the raw transcript (normalised, ellipsis-aware) and an external speaker on that call.

## 3. Buyer research page (per product line)
- Consent note and a two-line intro at the top.
- **Pain pillars:** what buyers fear and want relief from.
- **Aspiration and excitement pillars:** what they hope for and which features earned a real, unprompted reaction.
- Each pillar is a wiki toggle with themes as nested toggles: the theme, a pattern line ("Raised by N accounts"), then verbatim quotes. End each pillar with "Key buyer language" and, if needed, an "Emerging signals" toggle.
- **Cross-cutting objections** toggle: each objection as a theme with the pattern, evidence and how to respond.
- **Personas** table (pain, what they need to hear, language that lands) and register notes (e.g. delight-coded vs precision-coded buyers).
- No theme numbers. No dated notes.

## 4. Use-case context (optional)
The same evidence cut by use case (agent, module or job): pains today, what they hope to have, what excites them, objections specific to this use case, proof. Check hopes against the product capability baseline so the doc never promises what the product doesn't do.

## 5. Updating
- A quote that fits a theme goes under it; update the account count.
- A new topic from 1-2 accounts goes in that pillar's "Emerging signals". At 3+ distinct accounts it becomes a theme.
- Count distinct companies, not quotes. Order themes by account count.
- Paraphrased intel (Slack, deal-bot posts, rep notes) goes in as a short account line, not a quote.
- Mirror every edit to the wiki in place, inside the right toggle. Log runs in the sweep log only.
- Propagate: a buyer pain that maps to a product claim goes to the differentiation reference; a competitor complaint goes to that competitor's dossier.

## 6. Cleaning up
Back up first. Remove "added <date>", "<date> additions", "INTERNAL USE ONLY" per item, "Goes in pillar X", mirror notes, file references, sweep counts. Merge appended blocks into themes. Remove duplicate quotes. Rebuild the wiki page with toggles and check for banned strings.

## Rules
- Quotes are verbatim and checked against the source. Never tidy or invent.
- Internal call quotes are internal use only; naming a customer externally needs sign-off.
- Short plain sentences, no em dashes, no "not just X, Y" constructions.

## Shared conventions

- Find inputs in the workspace first: the files other skills in this set produce (capability baseline, buyer research, VOC library, evidence docs, customer proof files, dossiers, matrices, approved claims). Ask only for what's missing. Never fill a gap with assumptions about the company.
- Never invent a capability, stat, quote or competitor fact. Quotes are verbatim; named customer material stays internal until the customer signs off.
- Claim tags are SAFE, NEEDS VERIFY: (what settles it) or INTERNAL ONLY. Keep the tags you receive and pass them on.
- The user's own writing rules and brand voice override the defaults in this skill.
