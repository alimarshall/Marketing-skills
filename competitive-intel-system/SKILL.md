---
name: competitive-intel-system
description: Build and maintain a complete competitive-intelligence and buyer-research system for a B2B product: a VOC quote library, buyer research (pains, aspirations, objections, personas), competitor dossiers, a product capability baseline, comparison and communication matrices, a differentiation reference, and a verification tracker, kept current from sales calls (Gong or similar), Slack/sales intel, vendor sites and product releases. Use when someone asks to build or refresh competitor dossiers, battle-card research, buyer research or VOC themes, "what are buyers saying", "update the competitor docs", "run the sweep", "check competitors' AI/MCP", "fold this Slack thread/deck/call into the research", "clean up the research docs", or "we shipped X, update the docs".
---

# Competitive intelligence and buyer research system

A repeatable way to build, maintain and clean a set of internal research docs that sales, marketing and product all read. It works for any product and any set of competitors. Fill the placeholders from `company-context.md`: **[Product]** (your product, or each product line if you have several), **[Competitors]**, **[Call platform]** (Gong, Chorus, etc.), **[Wiki]** (Notion, Confluence, etc.) and **[Repo]** (the markdown source of truth, e.g. an Obsidian vault or a git folder).

The core idea: every fact lives in one right place, is backed by evidence, and is written so a new sales rep can read it cold. Research notes, dates of additions and process commentary never go into the shared docs. They go into a sweep log.

---

## Before you start
Read [`company-context.md`](../company-context.md) (repo root, or the copy in your workspace). It names the company, product lines, competitors and their tiers, tools (call platform, CRM, chat, wiki), where each research doc lives, house style and consent rules. Use those names and paths instead of the placeholders in this skill (**[Product]**, **[Competitor]**, **[Call platform]**, **[Wiki]**, **[Repo]**). If a line you need is blank, ask once and offer to write the answer back to `company-context.md`. Never hard-code a company, product, customer or path that isn't in that file or the request.

## Works with
This is the hub for the research skills. Route to the specialist skill when a request is about one part:
- **Evidence:** `buyer-research` (VOC library, buyer research pages), `buyer-call-synthesis` (one-off themes and top quotes from a batch of calls), `use-case-evidence-research` (per use case or feature), `vertical-persona-research` (per function, industry, ABM persona), `call-research-trend-analysis` (tagged shares and quarterly trends, charted by `research-data-charts`), `customer-proof-from-usage-reports` (usage stats as proof).
- **Competitive:** `competitor-dossiers`, `competitive-matrices` (capability baseline, capability matrix, communication matrix, differentiation reference, verification tracker).
- **Upkeep:** `competitor-buyer-sweep` (weekly or ad-hoc sweep of new evidence), `product-capability-refresh` (we shipped X: internal truth), `claim-propagation-sweep` (stale claims in copy, ads, pages), `source-doc-writeback` (a source doc is wrong), `claim-verification` (can we say this).
- **Outputs built on this research:** `capability-pillar-research`, `pillar-landing-pages`, `positioning-brief`, `creative-strategy`, `one-pagers`, `research-led-content-plan`.
Any skill named here that isn't installed: do that step inline using the rules below.

## 1. The document set

Build these once, then keep them current. Each lives in the [Repo] as markdown and is mirrored to a [Wiki] page that people actually read.

| Doc | What it holds | Granularity |
|---|---|---|
| **VOC library** | Every attributed buyer/customer quote, one row each | Spreadsheet/CSV |
| **Buyer research** (per product line) | Pain pillars, aspiration/excitement pillars, cross-cutting objections, personas | Narrative, themed |
| **Use-case / job context** (optional, per agent, module or job) | The same research cut by use case: pains, hopes, excitement per use case | Narrative, themed |
| **Competitor dossiers** (one per competitor) | Who they are, where they win, where we win, AI, positioning, deal intelligence | Narrative, fixed format |
| **Capability baseline** (own product) | What [Product] really does today, what it doesn't, per feature area | Narrative per area |
| **Master capability matrix** | Rating per capability per vendor (Leader / Parity / Trails / Building / N/A) | Compressed index, short cells |
| **Communication matrix** | Per feature: description, buyer pain, outcome, proof, tier (lead / supporting / table stakes), competitive angle | Table |
| **Differentiation reference** | Numbered claims with proof, register variants, honest gaps ("where we trail") | Narrative |
| **Verification tracker** | Open questions and unconfirmed claims, status, owner | Spreadsheet, script-generated if possible |
| **Sweep log** | Dated run notes: window, sources, what changed where, decisions needed | The only place dated notes live |

### VOC library schema
One row per quote. Suggested columns: `id, quote, product, type, theme, outlook_angle, sector, speaker, role, company, persona, emotion, intensity (1-3), competitor, context, source_type (sales call, customer call, cold call, case study, review site, survey), date, usage (internal only / case study, check sign-off / public source)`.
Types: Pain, Objection, Benefit, Desired outcome, Buying criteria, Fear/risk, Switching trigger, Why they left, Why they chose a competitor, Perception, Outlook, Proof/metric.

---

## 2. Formats

### Competitor dossier (fixed section order)
1. Header: Website, Competes with (one product line only), Status, then one italic line: internal use, quotes not cleared externally.
2. At a glance (5-7 bullets: who, who they sell to, where they beat us, where we beat them, how to position).
3. Company snapshot (table).
4. Positioning and narrative.
5. Product scope (table).
6. Where they win.
7. Where we win.
8. What their demos and docs reveal.
9. Competitive summary table: | Area | Competitor | [Product] | Edge (them / us / even) |.
10. AI and MCP (wiki toggle): their in-product AI, agents, MCP (exists? read/write? paid? who can use it?), Slack/Teams, then a small comparison table.
11. How to position against them (talk track, objection responses).
12. Deal intelligence, four toggle groups: Why buyers leave them, or would (pain) / Why buyers choose or stay with them, and what they praise / Objections, lock-in and timing / Switching triggers and buying criteria. Inside each, themes as nested toggles: bold theme name, one or two sentences on the pattern and how many accounts raise it, then verbatim quotes (Name, Role, Company, Mon YYYY).
13. Internal notes (toggle, at the bottom): Positioning over time, Comparison page angles.

No Sources section. Compare against one product line only: a competitor to your core product is compared with that product, and a competitor to a separate product line (e.g. an AI add-on) is compared with that line. A competitor that genuinely competes with both can carry both.

### Buyer research
Consent note and two-line intro at top. Pain pillars, then aspiration/excitement pillars, each a toggle heading with themes as nested toggles (pattern line with account count, then quotes). Each pillar ends with its "Key buyer language" line and, if needed, an "Emerging signals" toggle. "Cross-cutting objections" is a toggle with each objection as a nested theme (pattern, evidence, how to respond). Persona tables and register notes (e.g. delight-coded vs precision-coded buyers) stay as normal content. No theme numbers.

### Use-case context (per agent, module or job)
Same structure as buyer research, one page or section per use case: Pains today, What they hope to have, What excites them, Objections specific to this use case, Proof and quotes. Cross-reference the capability baseline so the hopes are checked against what the product actually does.

---

## 3. Evidence rules

1. **Quotes are verbatim.** Copy from the transcript or source file, never from your notes. Re-read the source before using any quote. Spot-check additions programmatically against raw transcripts. Fabricated or tidied quotes are the most damaging failure in this system.
2. **Sales intel beats vendor marketing.** If reps say a competitor capability is X and the vendor's docs say Y, X is the working fact. Mention the vendor claim at most once, never as the basis of a rating.
3. **Newest evidence wins.** Replace the outdated statement; don't keep both.
4. **Own-product truth comes from what shipped** (release channels, product team notes, the product itself), and the product owner's direct correction beats any doc. A confirmed decision (e.g. an implementation timeline) gets written everywhere at once.
5. **Consent.** Internal call quotes are internal use only. Naming a customer externally needs their sign-off. Case-study and public sources are the exception.
6. **Conflicts between buyers:** one plain line, "Mixed evidence: A says..., B says...". No commentary.
7. **Thin is fine if labelled by count.** One account is one account; say so in the pattern line.
8. **Paraphrased sales intel** (Slack, deal-bot posts) goes in as a short account line, not as a quote.

---

## 4. Themes and the emerging-signals rule

- A finding that fits an existing theme goes under it; update the account count.
- For high-volume docs (your top three or four competitors and the buyer research pages), a new topic raised by 1-2 distinct accounts goes in an **Emerging signals** toggle at the end of the group or pillar. At 3+ distinct accounts it is promoted to a theme and removed from Emerging signals.
- For low-volume docs (minor competitors), skip Emerging signals: every topic is its own theme. Agree which docs use the threshold with the owner before applying it, and don't apply it retroactively without asking.
- Count distinct companies, not quotes. Order themes by account count, largest first.

---

## 5. Never write into the shared docs

"added <date>", "<date> additions", "UPDATE", "fresh evidence added", "re-verified", "standing rule", "flagged for <person>", "TBD-VERIFY", "conflict flagged", "Goes in pillar X", running counts, mirror notes, file references, changelogs, "logged in the tracker", narration about who told whom. These go in the sweep log and the summary to the owner. A version line at the top of a reference doc is the one allowed exception.

Writing: short plain sentences, no em dashes, no "not just X, Y" or "X rather than Y" constructions, no AI filler. Each point says what they do, what we do, and who wins.

---

## 6. Workflows

### A. Initial build
1. Pull the call corpus. Survey external party email domains to find the most-discussed accounts; match accounts by domain, never by call title.
2. Mine transcripts in parallel (one subagent per batch of accounts), extracting attributed quotes into the VOC library.
3. Synthesise buyer research pillars (pain and aspiration) and objections from the library.
4. Research each competitor (vendor site, docs, changelog, pricing, reviews weighted to 2-3 stars, job postings, positioning history, call mentions) into a dossier. One subagent per competitor.
5. Build the capability baseline from product docs and release channels, then the matrices and differentiation reference on top.
6. Run a verification pass with a fresh subagent: every quote and every comparative claim against its source.

### B. Weekly sweep (schedule it)
1. Window = last sweep log entry to today (fallback 9 days).
2. Pull calls (parties first, transcripts only for calls worth mining). Screen product line by domain. Prioritise calls naming a tracked competitor, new accounts, and demo/kickoff/renewal/churn calls.
3. Match external-speaker lines naming a competitor against existing docs (6-word window match) so you only add net-new quotes.
4. Merge in place (section 4 rules). Mirror to the wiki in the same pass.
5. Propagate (workflow F). Log. Report under 150 words.

### C. Ad-hoc source fold-in
Slack thread, sales deck screenshots, a case study interview, a battlecard, a rep's comment. Classify (first-hand vs secondhand, sales vs marketing), apply the evidence rules, merge in place, propagate, log.

### D. Competitor AI/MCP re-verification (monthly, and after big vendor events)
Check each vendor's docs, changelog, newsroom and the AI connector directories for: vendor-built MCP server (status, read/write, permission model, who can use it, paid?), in-product AI actions vs answers, agents, Slack/Teams. Report only what changed against the current baseline. Then apply the sales-first rule before rating. Re-check after the competitors' annual conferences.

### E. VOC library cross-check
Programmatically compare every library quote tagged to a competitor against that dossier, and every own-product quote against the differentiation reference and communication matrix. Missing quotes get merged into the matching theme or claim. Use this to find claims with lots of fresh proof (candidates for promotion) and repeated loss reasons with no claim answering them.

### F. Propagation (after any notable finding)
List every doc covering the same competitor and capability (dossier, matrix cell, differentiation claim, communication matrix angle, capability baseline, verification tracker) and update each in its own format. A finding added to one doc does not appear in its siblings by itself.

### G. Product change refresh ("we shipped X")
Read the release note fully: what's new, what it explicitly does not do, temporary numbers. Update the capability baseline, then every matrix cell, claim, comparison table and dossier line that described the old state (grep for words like "pending", "not live", the feature name). Be honest in the verdict: narrower gap vs closed gap.

### H. Cleanup / restructure
1. Back up every file to an `_archive/` folder first.
2. Pilot the new format on one doc and get the owner's review before fanning out.
3. Fan out with one subagent per doc (or small group) using a written brief file they all read.
4. Rebuild the wiki pages, then verify toggles nest and banned strings are gone.

---

## 7. Practical lessons

- Large wiki pages often exceed tool limits; save the fetch to a file and read it in chunks, and construct edits against the stored text, not the markdown you'd expect.
- Edit wiki pages in place inside the right toggle with exact-match replacements; don't append blocks at the bottom.
- Parallel subagents writing to the same file collide. Give each agent disjoint files, and unique temp folders.
- Scheduled tasks drift from the format unless their prompts carry the full rules. Keep the on-demand skill and every scheduled prompt in sync.
- Check before acting on surprises: a competitor capability that contradicts sales, a quote attributed to the wrong company, a figure that keeps changing. Surface it to the owner rather than resolving it silently.
- Sales materials go stale fastest. When a competitor fact flips (e.g. "they have no MCP" stops being true), tell the owners of any sales pages that repeat it.

## 8. Report format
Under 150 words: window or source, what changed where, themes added or promoted, anything needing a decision. "Nothing new" is a valid result.

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
