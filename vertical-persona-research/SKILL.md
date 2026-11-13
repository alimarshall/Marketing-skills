---
name: "vertical-persona-research"
description: "Research and document buyers by vertical for any B2B product: what jobs the product can do for a function (People, IT, Finance, etc.), what an industry cares about most, the personas in each industry's buying committee for ABM multithreading, plus real quotes, notes and customer proof mapped to each. Use for \"what jobs can [product] do for X\", \"what does [industry] care about\", \"which industries can we support\", \"personas for ABM at [industry/account]\", \"multithread this account\", \"map these customer stats to each vertical\", or \"slides per vertical\". Brand-agnostic; grounded in call transcripts, CRM and existing research, never invented."
---

# Vertical & Persona Research

Use this to turn scattered buyer evidence into clear, reusable reference material, sorted by one of three lenses:

1. **Function / job vertical**: what the product does for a team (People, IT, Finance, Ops, Legal, AI transformation leader). Output: a job list, plus the persona context for that function.
2. **Industry vertical**: what a sector (FinTech, Healthcare, Legal, Energy, etc.) cares about most, its frustrations and objections, the product features it reacts to, and quotes from named accounts.
3. **Persona / buying committee (ABM)**: who sits in the buying group at a target industry or account, what each person cares about, and how to open with each one. This is for multithreaded outreach.

All three lenses use the same evidence base, so build it once and slice it three ways.

---

## Works with

- **Takes in:** the product's capability or jobs catalogue, buyer research and VOC library, CRM industry data, customer proof.
- **Produces:** a jobs-per-function view, an industry view and a buying-committee persona map, each with quotes and proof.
- **Next:** abm-account-multithread (applies the persona map to one named account), customer-proof-from-usage-reports (maps stats to each persona), use-case-ad-variations (role and situation wording for hints), pillar-landing-pages.

## Step 0: Check what already exists

Before researching, look for an existing reference file (search the workspace and notes vault for "jobs", "industries", "verticals", "personas", "buyer context", "ICP"). If one exists:
- Answer from it if it covers the request.
- If not, extend it in place (add a dated section) rather than creating a sibling file.

Only re-derive from scratch if nothing exists or the user asks for a fresh pass.

## Step 1: Pin down the inputs

Establish these, asking only for what you can't find yourself:
- **Product** and its **real capability catalogue**: tool integrations, shipped features, real production jobs or workflows. This is the ground truth. Every job you write has to fit inside it.
- **Lens**: function, industry, persona/ABM, or a mix.
- **Sources available**: call recording platform (Gong or similar), CRM (HubSpot or similar), existing buyer research docs, ICP or persona docs, case studies, customer usage reports, Slack threads, product release notes.
- **Evidence bar**: default is **at least 2 named accounts** per industry section. If the user sets a different bar, use theirs.
- **Output destination**: a persistent reference file (always), plus a wiki or Notion page, a deck or a doc if asked.

## Step 2: Gather evidence

### 2a. Capability ground truth
Read the capability or tool catalogue first. List what the product can actually read, write, trigger, route and approve. Anything outside this list does not become a job, however often buyers ask for it. Note those asks as feature requests instead.

### 2b. Existing research docs
Mine the existing buyer-context, pain, aspiration, ICP and persona docs. These are often organised by persona or company stage, not industry. To get an industry view, **re-classify each named account by its actual industry** (check the company's site or CRM industry field) and regroup the quotes.

### 2c. Call transcript mining (when fresh evidence is needed)
Use this method on the call platform's API:

1. **Survey**: page through all calls in the date range (most APIs use cursor pagination, not page numbers or offsets). **Save state after every page** so a timeout doesn't lose progress, and cap pages per run.
2. **Match accounts by participant email domain, not by call title.** Matching on titles silently misses real accounts. Build a domain-frequency table (calls per external domain) to see who you actually talk to.
3. **Filter** for the lens. For functions, match participant job titles (CFO, Controller, IT Director, CISO, Head of People). For industries, use the domain list you re-classified. For a product line, use calls whose title or attendees mark that pipeline.
4. **Build manifests** (call ID lists) per group and hand transcript reading to parallel subagents, one group each. Give each one the goal, the capability catalogue, and the output format: verbatim quote, speaker name and title, company, date, call ID, and the theme it supports.
5. **Pull transcripts in batches** (often up to 100 IDs per request). Respect rate limits; a typical limit is about 3 requests a second and 10k a day.
6. **Verify quotes** against the transcript text before using them. Never paraphrase inside quotation marks.

### 2d. Customer proof
If customer usage reports or case-study numbers exist, capture them exactly as worded, along with the reporting window and definitions. Calculated numbers (per week, ratios) are labelled as your own maths.

## Step 3: Evidence rules

- **No invented claims, quotes, accounts or capabilities.** If a section doesn't meet the evidence bar, say so in the internal notes and leave it out or mark it thin. Don't pad it.
- **Separate a function as user from a function as stakeholder.** For example, IT and Finance often appear as governance or approval gates inside another team's workflow, not as daily users. Write their jobs and messaging to match the role they actually play.
- **Cross-list accounts** that span two verticals (a fintech software vendor can sit in both Tech and FinTech), and say so.
- **Internal vs external**: call quotes are for internal use. Named quotes or customer stats only go external with the customer's permission (published case studies are the exception). Flag this on every deliverable that has names in it.
- **Don't upgrade wording.** If a report says "handled without a ticket", don't turn it into "resolved" or "automated". If counts include failed or pending items, say "approved", not "completed".
- **Keep evidence-strength notes in the internal methodology section.** If the user wants clean deliverables, strip labels like "thin" or "gap" from the deck, wiki or doc versions, but keep them in the reference file's methodology part, unless the user asks for them to be removed everywhere.

## Step 4: Write it up, one template per lens

### Function / job vertical
```
### [Function] ([persona name, e.g. Finance approver / IT gatekeeper])
Who they are: role, seniority, where they sit in the deal (user, champion, approver, blocker).
What they care about: 3-5 points.
Frustrations: 3-5 points, with quotes where available.
Objections: what they push back on, and the proof that answers it.
Jobs [product] can do: 10-20 bullets (style below).
Quotes: verbatim, speaker title, company, date.
```

### Industry vertical
```
### [Industry]
Accounts: [named accounts meeting the evidence bar], cross-listed where relevant.
What they care about most: 3-5 priorities specific to the sector (regulation, shift workers, multi-entity, audit, rapid hiring...).
Frustrations: with quotes.
Features they react to: the product capabilities that landed on calls, with the reaction.
Objections and concerns.
How to talk to them: 2-3 lines on angle and vocabulary.
Proof: case studies or stats from accounts in this sector.
```

### Persona / ABM multithreading map
For a target industry or a named account, map the buying committee:

| Role | Typical titles | What they care about | Frustration to open on | Proof / stat | Opening angle | Jobs to show |
|---|---|---|---|---|---|---|
| Champion | The function lead who runs the work day to day (e.g. Head of Operations) | ... | ... | ... | ... | ... |
| Economic buyer | The executive who owns the budget (e.g. COO, CPO, CRO) | ... | ... | ... | ... | ... |
| Technical gatekeeper | IT Director, CISO | ... | ... | ... | ... | ... |
| Finance approver | CFO, Controller, Head of Procurement | ... | ... | ... | ... | ... |
| End users | The people who use it daily | ... | ... | ... | ... | ... |

Then add:
- **Sequencing**: who to approach first, who the champion needs help selling to, and which objections each person raises.
- **One message per thread**: each person gets a different reason to care. Don't send the same pitch to every role.
- **Account-specific signals** (for named accounts): hiring, funding, tool stack, leadership changes, recent calls in the CRM or call platform.

### Mapping customer proof to verticals (for slides or one-pagers)
For each function or persona, choose the stats that answer *their* question:
- Operators or champions: volume handled, self-serve rate, adoption.
- IT or security: approval model, escalation, runs on the existing stack, controls. Don't claim audit or compliance features unless confirmed.
- Finance: volume handled without adding headcount, approvals not stalling, scale. Note any input still needed for the FTE or cost maths.
- Exec or transformation leader: adoption proof, the product doing work (not just answering), a board-ready narrative.

Default is 3 slides per vertical: headline claim, then 3-4 stat bullets, then an optional speaker note.

## Step 5: Writing style

- **Job bullets**: `**Bold action title**: one sentence on what it does end to end.` Lead with a strong, specific verb (Route, Chase, Generate, Build, Answer, Automate). Avoid vague verbs used alone, like "flag", "help" or "manage".
- **Don't apply blanket rewrites.** Judge each line separately. Plain phrasing that already works stays as it is.
- Short, concrete and grounded. No hedging, no filler, and no "not just X, but Y" constructions.
- Follow any house voice or style rules in the workspace (banned words, punctuation rules, naming conventions). Check for them before drafting.
- Internal technical notes (audits, punch lists) can be terse shorthand. Customer-facing material follows the brand voice.

## Step 6: Save it so it's reusable

Always write or extend one **persistent reference file** with:
- **Part 0, Methodology**: sources, date range, how accounts were matched, the evidence bar, and what was thin or missing (internal).
- **Part 1, Functions/jobs**, **Part 2, Industries**, **Part 3, Personas/ABM maps**, **Part 4, Customer proof by vertical**.
- **Part 5, Writing style rules**, including any line-level feedback from the user.
- A dated note at the top of each new section.

Then mirror the result to the wiki, deck or doc if asked, and add a pointer from any index or memory file so the next request starts at Step 0.

## Wiki / Notion pitfalls

- For toggles in Notion markdown, put `<details>` and `<summary>…</summary>` on **separate lines**.
- Replacing a whole page's content can fail if it would delete a child page. Keep the child page reference in the new content.
- A failed exact-match text replace usually means escaping differences. Append at the end instead.
- Some parent pages are readable but not writable. If a create fails with "not found", use a parent you know you can write to.

## Quality check before handing over

- Every job fits inside the capability catalogue.
- Every industry section meets the evidence bar, or is marked thin in the internal notes.
- Every quote is verbatim and attributed, and external use is flagged as needing consent.
- Each persona in an ABM map has a distinct angle and proof point.
- No stat is reworded into a stronger claim than its source supports.

## Shared conventions

- Find inputs in the workspace first: the files other skills in this set produce (capability baseline, buyer research, VOC library, evidence docs, customer proof files, dossiers, matrices, approved claims). Ask only for what's missing. Never fill a gap with assumptions about the company.
- Never invent a capability, stat, quote or competitor fact. Quotes are verbatim; named customer material stays internal until the customer signs off.
- Claim tags are SAFE, NEEDS VERIFY: (what settles it) or INTERNAL ONLY. Keep the tags you receive and pass them on.
- The user's own writing rules and brand voice override the defaults in this skill.
