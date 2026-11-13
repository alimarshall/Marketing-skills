---
name: persona-evidence-research
description: Build or refresh deep research on each buyer persona (e.g. CPO/CHRO, the day-to-day team leads under them, CTO/IT, CFO, CEO) from call recordings and the VOC library - their pains, fears, excitements, needs to move forward, objections, goals and triggers, grouped into themes with verbatim quotes - plus content and ad angles, language that lands and what not to say, so marketing can write content and ads per persona. Use for "research each persona", "what does the CFO care about", "fears and excitements by persona", "persona research with quotes", "content for each persona", "update the persona pages with new calls", or "we need more evidence on the CTO".
---

# Persona evidence research

One research page per buyer persona, built from what buyers actually said. Each page answers: what do they fear, what excites them, what do they need before they move, and which words of theirs can we use. It feeds content, ads, landing pages and sales collateral for one persona at a time.

## Before you start

Read `company-context.md` (repo root or workspace). This skill uses: product(s) in scope and product lines, capability baseline, call recording platform and access, CRM, VOC library, internal email domains, how to tell product lines apart on calls, the persona reference doc and its wiki page, settled decisions, house style, consent rules. If a line is missing, ask once and offer to save the answer back.

Then check what exists (Step 0 of `vertical-persona-research`): an existing persona or jobs reference and its wiki page. Extend it; never start a parallel doc.

Agree the persona list with the user. A useful default for a B2B product sold to one function:
- The function's executive (economic buyer), e.g. CPO/CHRO, VP.
- The day-to-day leads and operators under them (usual champion and user).
- The technical gatekeeper: CTO, CIO, CISO, IT, security, business systems, AI enablement.
- The finance approver: CFO, VP Finance, controller.
- The CEO / founder / COO (final sign-off, sets any AI mandate).

## Step 1: Survey calls and tag speakers by persona

1. Pull every call in the window with participants (parties only, no transcripts yet). Save state after each page so a timeout loses nothing.
2. Classify each call by product line using the rule in company-context (call title keyword, owner, or account email domains). Never classify an account by call title alone.
3. For each external participant (not an internal domain, not free mail), map their job title to a persona with regexes. Check titles containing the function's own words first (e.g. "people", "HR") so "VP People Operations" lands with the function, not the CEO bucket. Use word boundaries: "coordinator" must not match "coo", "director" must not match "cto".
4. Count calls and distinct accounts per persona and product line. Executives join few calls on a specialist product. If an exec persona has fewer than about 10 accounts, widen the window or include the sibling product line's calls, and say so in the method note.

## Step 2: Build evidence packs

1. Pull transcripts in batches (most APIs take up to 100 call IDs per request).
2. Per persona, write a pack holding only that persona's own speech, each line labelled `Name (Title, company)`, with the previous speaker's line as context marked "context only".
3. Build a second-hand pack: lines where any buyer talks ABOUT their CFO, IT/security team, CEO, founder or board ("our CFO wants...", "IT will block..."). This is often the richest evidence for exec personas.
4. Add the VOC library rows for each persona. Map its types to the categories below and drop rows already covered by a call quote. For exec personas, keep only VOC rows whose speaker title really is that exec.
5. Split packs into chunks of about 400KB at call boundaries.

## Step 3: Extract with parallel subagents

One subagent per chunk, all launched in one message. Brief each with a written file (goal, personas, categories, rules, output format) instead of retyping it.

Categories:
- **Pain**: what is hard or broken today.
- **Fear**: worries and risks (AI accuracy, data exposure, cost, failed rollout, credibility, jobs).
- **Excitement**: what they reacted to or hope for.
- **Need**: what they need to see or have to move forward (proof, security answers, integrations, pricing clarity, approvals, timeline).
- **Objection**: pushback or reasons to delay.
- **Goal**: success and mandate.
- **Trigger**: why they look now.

Rules for subagents: the quote is an exact substring of that speaker's text, one or two full sentences, no stitching, no "...", never the seller's words. Attribute speaker, title, company, date, call ID, product line. Second-hand lines carry the persona being described and `secondhand: true`. Maximum 6 quotes per company per category, to keep breadth. Output a JSON array.

## Step 4: Verify every quote

Run a script over the merged output: normalise whitespace and curly quotes, then check each quote is a substring of the named speaker's own transcript text on that call (see `scripts/verify_quotes.py`). Drop failures. Report the pass count. Map email domains to proper company names; a domain root like "co" from `.co.uk` is a bug.

## Step 5: Cluster into themes

One subagent per persona gets a compact list (`id | category | rough theme | company | role | short quote`) and returns:
- canonical themes per category (merge near-duplicates hard; 5-12 per big category), each with a one-line pattern in plain words
- an assignment of every item to a theme
- the persona header: who they are and their role in the deal; top fears, excitements and needs; 8-12 short verbatim phrases for ads; 6-10 content angles, each with a hook and the themes it draws on; what not to say

Then check by script: every item assigned, every label exists, every "language" phrase appears verbatim in a quote, no hook invents a number or a capability outside the capability baseline, and no banned constructions from house style ("not just X, Y", "X rather than Y", em dashes) outside quotes. Fix any before building.

## Step 6: Count and build

- Count **distinct accounts** per theme, never quotes.
- 3 or more accounts: the theme gets its own toggle with the pattern and up to 5 quotes from different companies (call quotes before VOC quotes, direct speakers before second-hand, newest first).
- 1 or 2 accounts: one line in that category's **Emerging signals** toggle, with its best quote.
- Order themes by account count.
- Second-hand quotes are labelled "describing their exec team".

Page layout per persona:
1. Internal-use callout with the evidence base (quotes, accounts).
2. Who they are.
3. At a glance: top fears, what excites them, what they need to move forward.
4. Content and ad angles table: angle, hook, themes it is built on.
5. Language that lands.
6. What not to say.
7. Evidence by theme: one toggle per category (Pains today, Fears and worries, What excites them, What they need to move forward, Objections and pushback, Goals and how they define success, Why they look now), with theme toggles inside.

The parent page keeps a summary table (persona, role in deal, top fear, top excitement, top need, evidence), links to each persona page, the jobs the product can do per persona, and any industry notes.

## Step 7: Save and mirror

- Source of truth: one markdown file in the repo with an internal method section (sources, window, matching rules, evidence bar, customers vs prospects caveat) and all persona sections.
- Wiki: one child page per persona under the persona reference page (a single page gets too big). In Notion use `<toggle heading="h3">` for categories and `<toggle heading="h4">` for themes; `<details>` is not supported. Large pages: create with the header, then append one category toggle per call.
- Point the index or README and the jobs reference at the new file.
- Back up any page you restructure first. No dated "added" notes or file references in the shareable pages; run notes go in the sweep log.

## Refreshing

Re-run Steps 1-6 for calls since the last run, add new items, re-cluster against the existing theme list (new labels only when nothing fits), recount, and update pages in place. A topic that reaches 3 accounts moves from Emerging signals to a theme.

## Rules

- Never invent a quote, account, number or capability. Thin personas are shown as thin (fewer themes, more emerging signals), never padded.
- Call quotes are internal use. Naming a customer externally needs their sign-off. Existing customers and prospects are separated before a quote is used as a demo reaction.
- Separate a role as user from a role as approver: IT and Finance usually gate a deal they do not use day to day. Write their angles for that role.
- Hooks stay inside what the product does today (check the capability baseline) and state settled decisions the way company-context does.

## Works with

- **Reads from** `buyer-research` (the VOC library and themes), `buyer-call-synthesis` (call mining method) and `competitive-intel-system` (the hub).
- **Sits beside** `vertical-persona-research`, which slices the same evidence by function and industry; this skill goes deep per persona.
- **Feeds** `abm-account-multithread` (one angle per person in the committee), `creative-strategy` and `ad-avatars` (avatars per persona), `research-led-content-plan`, `exec-post-skeletons-from-buyer-research`, `pillar-landing-pages` and `one-pagers`.
- **Checks with** `claim-verification` and `copy-register-check` before any hook goes external, and `claim-propagation-sweep` when a product fact changes.

Skills named here are optional. If one isn't installed, do that step inline and say so.

## Checks before handover

- Every quote verified against the source; pass count reported.
- Theme counts are distinct accounts; themes under 3 accounts sit in Emerging signals.
- No hook or angle claims a capability or number the product does not have.
- No banned constructions outside quotes; no dated notes or file references in shareable pages.
- Consent flagged on every page with names.
