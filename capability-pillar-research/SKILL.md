---
name: capability-pillar-research
description: "Regroup buyer research and a product's real capability or jobs catalogue into verb-based behavioural pillars (for example Acts, Answers, Resolves, Collaborates, Analyzes) instead of organising by feature, module or agent. Use whenever the user wants research organised by what the product actually does, asks for pillar or capability docs, wants a jobs-per-function breakdown (People, IT, Finance), or is about to write positioning or landing pages for a multi-capability product. Always cross-checks buyer quotes against the real capability catalogue, since quotes alone undersell scope. Second step of a four-skill set: takes use-case-evidence-research output, feeds pillar-landing-pages."
---

# Capability-pillar research

Turns buyer research and product documentation into a small set of verb-based pillar docs, one per behaviour the product performs (for an AI agent product, for example: Acts, Answers, Resolves, Collaborates, Analyzes). Each pillar doc becomes the ground truth for positioning and landing pages, so get it right before any copy is written.

## Inputs

Read `company-context.md` first (repo root, or search the workspace for it) and use the fields that apply to this skill. If the file or a line is missing, ask once, then offer to save the answer back to it. Never fill a gap with an assumption about the company.

## Works with

- **Takes in:** the per-use-case evidence docs from use-case-evidence-research (preferred), or raw buyer research plus the product's real capability or jobs catalogue.
- **Produces:** one pillar doc per verb, with an honest strength rating for each pillar.
- **Next:** pillar-landing-pages, or a positioning brief. Run claim-propagation-sweep when a capability listed in a pillar changes.

## Why pillars, not features or modules

Buyers experience a product as things it does for them. Grouping by verb ("it acts on my data", "it answers my questions") surfaces the emotional and competitive story better than module names, and maps cleanly onto positioning and pages later: each pillar can become its own message, page and set of proof points.

## The lesson that makes or breaks this: two sources, not one

Buyer research is a sample of what came up in specific conversations. It always undersells the product's real scope. Pillar docs built from quotes alone read smaller than the product is, and the copy built on them feels thin however many edits it gets.

Always pull from both:
1. **Buyer evidence:** pains, delight, objections, buyers' own language (ideally the verified docs from use-case-evidence-research).
2. **The real capability or jobs catalogue:** the tool list, feature catalogue or "what the product can do" reference the product team uses, sorted by the function it serves (People, IT, Finance, Legal, or the product's own split).

If the catalogue doesn't exist as a document, build it first (use-case-evidence-research step 1) or ask where it lives. A pillar doc built from quotes only is a first draft.

## Process

1. **Confirm or derive the pillar set.** Use the user's pillars if named. Otherwise group the capability catalogue by core verb and find the handful of verbs that cover almost everything.
2. **Sort every capability into its pillar** by its core verb, not by which team asked for it or which page it might sit on. "Generates and routes an offer letter for signature" is Acts (it executes a transaction), even if it's demoed in a helpdesk conversation.
3. **Sort buyer evidence per pillar.** Note account and persona, and whether each statement is a direct ask or an inferred data point ("IT is named as one of several fragmented systems" is weaker than "an IT stakeholder asked for this").
4. **Write one doc per pillar:**
   - **What this pillar is:** one plain paragraph.
   - **The real jobs behind it:** from the catalogue, by function. This counters the quotes-undersell-scope problem; don't skip it.
   - **Why it needs to exist:** the pain, grounded in buyer evidence.
   - **Recurring themes in buyer conversations:** numbered themes, quotes nested under each, and a "How to use this" line turning the theme into a positioning instruction.
   - **Jobs per function:** directly evidenced versus indirectly evidenced, kept visibly separate.
   - **Personas:** persona, before, after, the KPI they'd track. Skip personas without evidence.
   - **Where this shows up:** which product areas or pages the evidence concentrates in, and where it's thin or absent.
5. **Rate each pillar's evidence strength** (strong, real but concentrated, thin) and say why. Whoever writes pages from these needs to know which pillars can carry a hero claim.
6. **Verify and publish:** run the quote check, then save and mirror as in use-case-evidence-research step 5.

## Done when

- Every pillar cites real capabilities from the catalogue, not only quotes.
- Every quote has a source and passes the quote check.
- Direct-ask and inferred evidence are separate.
- At least one pillar is rated weaker than the others, if that's true. If every pillar reads equally strong, the honesty pass didn't happen.

## Shared rules (identical across the four skills in this set)

1. **Evidence before copy.** Every product claim, stat and quote traces to a named source. Never invent a capability, number, customer story or quote. If the evidence isn't there, say so.
2. **Shipped means shipped.** State a capability's status (shipped, in progress, planned) only as the source states it. Buyer requests the product can't meet go under hopes or wants, never under capabilities.
3. **Quotes are verbatim and buyer-side.** Copy exact words; cut with "..." but never change them. Never quote the vendor's own staff as a buyer. Before finishing, run the quote check (the script ships with use-case-evidence-research as `verify_quotes.py`) and fix or drop anything not found.
4. **Claim tags.** Mark copy and claims SAFE, NEEDS VERIFY: (what would settle it), or INTERNAL ONLY (named customer material without sign-off). Carry tags forward from one skill's output into the next; don't strip them.
5. **Thin evidence is said plainly.** Count distinct accounts, not quotes. Never pad a weak area to match a strong one.
6. **Finished docs, not change logs.** No "updated", "added", "new", version numbers, sweep or session references in docs meant to be read as references. Version history holds that.
7. **External-safe mode** (when the user says external, for ads, for customers, keep it clean): job title and company only, no personal names; no dates; competitor names inside quotes replaced with a neutral bracket such as "[the old tool]"; no notes about sign-off, sources or usage. Tell the user in your reply that customer quotes still need sign-off.
8. **Voice.** Plain and direct. No em dashes. No hedge words. Don't characterise competitors beyond what buyers say themselves. No filenames in the body of a doc.

## How the four skills work together

1. **use-case-evidence-research**: collects and verifies the evidence (product capabilities, buyer pains, hopes, reactions) per use case or feature.
2. **capability-pillar-research**: regroups that evidence by verb (what the product does) when positioning by behaviour rather than feature.
3. **pillar-landing-pages**: turns the positioning into one page brief per pillar or feature, using only claims from steps 1-2.
4. **claim-propagation-sweep**: runs whenever a product fact changes, across everything steps 1-3 produced, and feeds corrections back into the evidence docs.

Outputs of one step are the inputs of the next. If you're asked for a later step and the earlier output doesn't exist, build the earlier step first (or tell the user it's missing) rather than writing from memory.
