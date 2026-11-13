---
name: buyer-call-synthesis
description: Distill a batch of sales or customer calls (Gong, Chorus, Zoom recordings, or any call-recording platform) into the main recurring themes, ranked by how often and how strongly they show up, plus the strongest verbatim quote for each. Use when someone asks to "pull the themes from these calls," "what are buyers actually saying," "give me the top quotes on X," "synthesize the last quarter of calls," or wants a batch of raw call transcripts turned into a short, usable summary rather than read one by one. Distinct from a single-call summary (decisions, next steps, objections for one call): this skill works across many calls at once to find patterns.
---

# Buyer Call Synthesis

## Before you start
Read [`company-context.md`](../company-context.md) (repo root, or the copy in your workspace). It names the company, product lines, competitors and their tiers, tools (call platform, CRM, chat, wiki), where each research doc lives, house style and consent rules. Use those names and paths instead of the placeholders in this skill (**[Product]**, **[Competitor]**, **[Call platform]**, **[Wiki]**, **[Repo]**). If a line you need is blank, ask once and offer to write the answer back to `company-context.md`. Never hard-code a company, product, customer or path that isn't in that file or the request.

## Works with
- **Takes in:** a batch of call transcripts (from the call platform in `company-context.md`).
- **Produces:** a short themes-and-top-quotes summary for one question.
- **Hands to:** `buyer-research` (add verified quotes to the VOC library and the right pillar), `competitor-dossiers` (competitor mentions), `use-case-evidence-research` (use-case evidence). For repeatable quarterly trend numbers use `call-research-trend-analysis` instead.

## What this skill does

Sales and customer-success teams generate far more call recordings than anyone reads. This skill takes a batch of calls, ranging from a dozen to several hundred, and distills them into a small number of recurring themes (pain points, objections, feature requests, competitor mentions, moments of delight, whatever the ask is scoped to), each backed by how many distinct accounts raised it and the single strongest verbatim quote that captures it. The output is meant to be read in five minutes and trusted, not a transcript dump with a summary bolted on top.

This is not the same job as summarizing one call (participants, decisions, next steps, objections for that specific conversation), it's finding the signal that only appears once you look across many calls at once, and that no single-call summary can surface on its own.

## Step 0: scope the pull before touching any transcripts

Nail these down first, asking if genuinely unclear:

- **What population of calls.** A date range, a named list of accounts, a call type (demos only, renewals only, churn/cancellation calls), or a specific segment (calls mentioning a named competitor, calls from a specific persona or industry).
- **What you're listening for.** Pain points and objections, feature requests, competitor mentions, positive-signal / aspiration language, or a specific named question ("how do buyers describe onboarding friction"). A synthesis run with no scoping question tends to produce a shallow, generic theme list, narrow it even if the person asking hasn't.
- **How the output will be used.** Feeding a positioning brief, a product roadmap conversation, a case study search, or a one-off "what are people saying" check. This changes how much proof and attribution detail the output needs.

## Step 1: pull the calls and get access to full transcripts, not just metadata

Connect to whatever call-recording platform your team uses. Most platforms distinguish a lightweight metadata/parties call from a full-transcript call, pull metadata first to screen for relevance (title, participants, account, call type), then pull full transcripts only for the calls that actually match your Step 0 scope. Pulling full transcripts for every call in a large date range wastes calls and context for no benefit if most of them are irrelevant.

If your workspace covers multiple product lines, brands, or business units, screen calls by external-party email domain (not just call title, titles are unreliable and will silently miss real accounts) to route each call to the right line before including it in the synthesis.

## Step 2: read for theme, not for line-by-line detail

Work through the transcripts looking specifically for language that recurs across different accounts, not for anything interesting a single account said once. A pain point mentioned by one account in passing is a data point; the same pain point independently raised by five accounts in different words is a theme. Track, per candidate theme, which accounts raised it and roughly how (a passing mention, a named blocker, something that came up unprompted versus in response to a direct question).

Distinguish, as you go:

- **A theme with real breadth** — raised independently by multiple, distinct accounts, in their own words, not prompted by a leading question from the salesperson.
- **A theme with real depth but narrow breadth** — one or two accounts, but described with unusual specificity or intensity (a named dollar cost, a named workaround, a strong emotional reaction). Worth surfacing, but labelled as a single-account or narrow finding rather than a broad pattern, don't inflate it into "buyers are saying" language.
- **Noise** — a one-off comment with no specificity, or something clearly prompted by how the salesperson phrased a question rather than something the buyer volunteered.

## Step 3: rank and select the top themes

Don't report everything you found, rank by a combination of breadth (how many distinct accounts), recency (favor calls from the requested window over older stragglers if the request implied a current snapshot), and specificity (a theme expressed in concrete, vivid language beats one expressed only in vague generalities). Aim for the smallest number of themes that actually covers the material, typically somewhere between four and eight for a normal-sized batch. A synthesis with fifteen "themes" has usually failed to actually synthesize.

For each theme selected, note explicitly:
- The number of distinct accounts it came from (not the number of mentions, one account raising it three times in one call is still one account).
- Whether it was volunteered or prompted.
- Any pattern in which kind of account raises it (a segment, an industry, a persona, a deal stage), only if it's a genuine pattern, not a guess dressed up as one.

## Step 4: pick the strongest quote for each theme, verified

For each theme, select the single quote that most sharply and concretely captures it, favor specific, concrete language over vague paraphrase-able statements. Then verify it word for word against the actual transcript text before using it, never reconstruct a quote from memory or from your own notes taken while reading, this is the step most likely to introduce a fabricated or subtly altered quote, and it is checkable in seconds against the source.

Attribute every quote with enough context to be useful and honest: account name (or "internal use only, name withheld" if it can't be shared externally), rough date, and role/title if known. Flag clearly, next to each quote, whether it's cleared for external use (a public case study, a reference customer who's agreed to be quoted) or internal-only (a standard sales call, no consent obtained). Default to internal-only unless you have explicit confirmation otherwise, this determines whether the quote can go in public-facing marketing material or only in internal decks and briefs.

## Step 5: write the output

A short, scannable document, not a transcript-length report:

1. **One-line scope statement** — what calls, what window, what question this was synthesizing for.
2. **Themes, ranked**, each as: a one-sentence statement of the theme, the account count and breadth/depth note from Step 3, and the verified quote with its attribution and use-clearance flag.
3. **Anything notable but too thin to call a theme** — a single sentence per item, explicitly labelled thin, so it isn't lost but also isn't overstated.
4. **What this batch did NOT show**, if relevant, if the request was looking for something specific (a particular objection, a particular competitor) and it simply wasn't there, say so plainly rather than stretching a weak match to fill the gap. A clear negative finding is more useful than a padded one.

## Step 6: hand off cleanly

If this synthesis is feeding another process, a positioning brief, a competitive-intelligence sweep, a case-study search, name that explicitly and flag which quotes are already cleared for external use versus which would need separate sign-off before appearing anywhere public. If a theme surfaced a product gap or a competitive claim worth adding to a standing reference doc, say so and hand off to whatever skill your team uses to maintain that doc, don't fold it in yourself unless that's explicitly part of this run's scope.

## Shared rules (same across the research skills)
1. **Evidence before claims.** Never invent a product fact, number, quote or competitor capability. Missing evidence is a finding, said plainly.
2. **Shipped means shipped.** State a capability's status only as the source states it.
3. **Quotes are verbatim and buyer-side.** Copy exact words, attribute (Name, Role, Company, Mon YYYY), and check against the raw transcript before publishing (`scripts/verify_quotes.py` if installed).
4. **Source precedence.** Product owner's correction > shipped product and release notes > internal product docs > sales intel > vendor marketing. Sales intel beats a competitor's own claims. Newest evidence wins: replace the old statement.
5. **Claim tags.** SAFE, NEEDS VERIFY: (what would settle it), INTERNAL ONLY (named customer material without sign-off). Carry tags forward between skills.
6. **Count distinct accounts.** On the high-volume docs listed in `company-context.md`, 1-2 accounts go in "Emerging signals" and 3+ become a theme. Elsewhere a new topic is a theme.
7. **Finished docs, not change logs.** No "added <date>", "UPDATE", "flagged for", "TBD", mirror notes, file references or changelogs in shared docs. Dated run notes go in the sweep log only.
8. **Consent.** Call quotes are internal by default; naming a customer externally needs sign-off.
9. **Propagate and mirror.** When a fact changes, update every doc that states it, in the repo and the wiki copy, in place.
10. **Voice.** Follow the house style in `company-context.md`; default to short plain sentences, no em dashes, no "not just X, Y" contrasts.
