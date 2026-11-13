---
name: competitor-dossiers
description: Build a new competitor dossier from scratch, or update and clean up an existing one, in a fixed, shareable format with evidence-backed deal intelligence. Use for "build a dossier on X", "research competitor X", "update the X dossier", "fold this into the X dossier", "clean up the competitor pages", "battle card research on X", or "how do we compare to X".
---

# Competitor dossiers: build, update, clean up

One dossier per competitor, kept in a markdown source of truth (**[Repo]**) and mirrored to a wiki page (**[Wiki]**) that sales reads before a deal. Placeholders: **[Product]** (the product line this competitor competes with), **[Competitor]**, **[Call platform]**.

## Before you start
Read [`company-context.md`](../company-context.md) (repo root, or the copy in your workspace). It names the company, product lines, competitors and their tiers, tools (call platform, CRM, chat, wiki), where each research doc lives, house style and consent rules. Use those names and paths instead of the placeholders in this skill (**[Product]**, **[Competitor]**, **[Call platform]**, **[Wiki]**, **[Repo]**). If a line you need is blank, ask once and offer to write the answer back to `company-context.md`. Never hard-code a company, product, customer or path that isn't in that file or the request.

## Works with
- **Takes in:** call transcripts and the VOC library (from `buyer-research`), sales intel, vendor sources, the capability baseline (from `competitive-matrices`).
- **Produces:** one dossier per competitor.
- **Hands to:** `competitive-matrices` (re-rate the competitor's cells and our own), `one-pagers` and `creative-strategy` (battlecards, conquest angles). Kept current by `competitor-buyer-sweep`; product changes on our side arrive via `product-capability-refresh`.

## The format (keep it fixed)
1. **Header:** Website, Competes with (one product line), one-line Status. Then an italic line: internal use; quotes are from calls and not cleared externally.
2. **At a glance:** 5-7 bullets: who they are, who they sell to, where they beat us, where we beat them, how to position.
3. **Company snapshot** (table): founded, HQ, size, funding/valuation, revenue, customers, integrations count, review ratings. Current facts only.
4. **Positioning and narrative:** their story in their words.
5. **Product scope** (table): module and what it does.
6. **Where they win:** honest strengths.
7. **Where we win:** their weaknesses, evidenced.
8. **What their demos and docs reveal:** what their own materials give away.
9. **Competitive summary table:** | Area | [Competitor] | [Product] | Edge (them / us / even) |. Cover core product, usability, pricing, implementation, support, reporting, integrations/API, global, AI, and anything deal intelligence shows.
10. **AI and MCP** (wiki toggle): in-product AI (answers vs actions), agents, MCP server (exists? read/write? paid? who can use it?), Slack/Teams, then a comparison table.
11. **How to position against them:** talk track and objection responses.
12. **Deal intelligence** in four toggle groups: Why buyers leave them, or would / Why buyers choose or stay with them, and what they praise / Objections, lock-in and timing / Switching triggers and buying criteria. Each group holds themes as nested toggles: theme name, one or two sentences on the pattern and the number of distinct accounts, then verbatim quotes (Name, Role, Company, Mon YYYY).
13. **Internal notes** (toggle, last): Positioning over time, Comparison page angles.

Compare against one product line only. No Sources section. No dated notes anywhere.

## Building a new dossier
1. **Vendor sources:** homepage, product and pricing pages, docs/help centre, changelog/release notes, newsroom, developer docs, AI connector directories (for MCP), trust/security page.
2. **Independent sources:** G2/Capterra/TrustRadius/Trustpilot reviews, weighted to 2-3 star reviews (that's where the specific detail is); analyst coverage; funding and M&A news; job postings (where they're investing); Wayback snapshots for positioning over time.
3. **Your own evidence:** search call transcripts for the competitor's name (match accounts by email domain, not call title), the VOC library, Slack/sales channels, CRM win/loss reasons, and any battlecards.
4. Draft every section. Every comparative claim must trace to a source; every quote must be verbatim.
5. Run a verification pass with a fresh agent: each quote against its transcript, each fact against its source. Fix or cut anything that fails.
6. Mirror to the wiki.

## Updating a dossier
- **New quote that fits a theme:** add it under the theme and update the account count.
- **New topic:** for your top 3-4 competitors, 1-2 accounts go in an "Emerging signals" toggle at the end of the group, and 3+ accounts become a theme. For smaller competitors, add a new theme straight away.
- **Changed fact** (a launch, price change, acquisition): edit the right section in place (snapshot, scope, AI and MCP, summary table, At a glance) and replace the old statement. Don't keep both.
- **Sales intel vs vendor marketing:** if reps say a capability is X and the vendor says Y, write X. Mention the vendor claim once at most.
- **Conflicting buyers:** one line, "Mixed evidence: A says..., B says...".
- **Propagate:** check the capability matrix cell, differentiation claim, communication matrix angle and buyer research for the same point and update each.
- Mirror each edit to the wiki in place, inside the right toggle. Don't append blocks at the bottom.
- Log the run (date, source, what changed) in the sweep log only.

## Re-verifying AI and MCP (monthly, and after vendor conferences)
For each competitor, check docs, changelog, newsroom and connector directories for MCP status, read/write, permission model, who can use it and whether it's paid; in-product AI actions vs answers; agents; Slack/Teams. Report only changes. Apply the sales-first rule before rating.

## Cleaning up a messy dossier
1. Back up the original to `_archive/`.
2. Remove meta text: "added <date>", "UPDATE", "re-verified", "flagged for", "TBD", mirror notes, file references, changelogs, sweep counts, narration about who told whom.
3. Merge appended dated blocks into the right sections and themes. Remove duplicates; keep the newest fact.
4. Rebuild the summary table with current information.
5. Pilot one dossier and get sign-off before doing the rest (one agent per dossier, written brief, disjoint files).
6. Rebuild the wiki page; check toggles nest and banned strings are gone.

## Writing
Short plain sentences, no em dashes, no "not just X, Y" constructions. Each point says what they do, what we do, and who wins. Quotes are never tidied.

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
