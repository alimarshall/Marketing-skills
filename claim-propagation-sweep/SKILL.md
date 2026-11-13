---
name: claim-propagation-sweep
description: "When a product fact changes (a feature ships, a gap closes, a number is corrected, a capability is retired), find every doc, ad bank, landing-page brief, sales asset and wiki page that still states the old fact, then fix or flag it. Use whenever the user says a feature just shipped, is now live, we can now do something, a number is wrong, something was retired, asks to update everything that says X or find anywhere we still claim X, or shares release notes. Catches direct contradictions and indirect ones (gaps lists, FAQ answers, competitor comparisons, ads built on the gap). Fourth skill of a four-skill set: sweeps the output of use-case-evidence-research, capability-pillar-research and pillar-landing-pages, and feeds corrections back into them."
---

# Claim propagation sweep

A fact about the product has changed. Somewhere there are docs, ads and pages that still say the old thing. This skill finds them and makes them agree with the new fact, without claiming anything beyond what the new fact supports.

Why it matters: an ad or one-pager that states a gap after it has closed costs deals and credibility, and nobody notices because the team updating product docs isn't the team running the ads.

## Inputs

Read `company-context.md` first (repo root, or search the workspace for it) and use the fields that apply to this skill. If the file or a line is missing, ask once, then offer to save the answer back to it. Never fill a gap with an assumption about the company.

## Works with

- **Takes in:** the change (release note, roadmap update, product meeting), plus everything the other three skills produced: evidence docs, pillar docs, page briefs, and any ad banks, one-pagers and wiki pages built from them.
- **Produces:** corrected docs, a flag list for assets that need a decision, and a list of live assets to change by hand.
- **Feeds back into:** use-case-evidence-research (update the capability section and any "gaps" themes) and capability-pillar-research (a capability may move pillar or change strength).

## 1. Pin down the change

Before touching anything, write:
- **Old fact:** what used to be true.
- **New fact:** what is true now, scoped exactly, with caveats (beta, one customer, partial).
- **Source:** where it comes from. If only hearsay, treat it as provisional (NEEDS VERIFY).
- **What did NOT change:** adjacent gaps that still hold. These are the ones most likely to be deleted by mistake.

## 2. Build the search list

Wider than the obvious phrase:
- the old claim's wording and variants
- the feature's name and synonyms
- gap-list framings ("where we trail", "known gaps", "limitations", "what it doesn't do", FAQ answers)
- comparisons that relied on the gap ("a competitor wins on X", "concede X")
- for numbers, the old value in every format ("3 weeks", "three weeks", "3-week")

## 3. Sweep every surface

- reference docs: capability baseline, claims or differentiation doc, matrices, positioning briefs
- marketing assets: ad banks, concepts, landing-page briefs, one-pagers, battlecards, FAQs, emails, social drafts, website copy
- research docs: evidence docs, pillar docs, objection libraries
- wiki pages and mirrors of all of the above
- skill reference files that hard-code facts (note for the user)
- live assets you can't edit (published pages, running ads): list for the user

Record each hit with location and exact line.

## 4. Classify each hit

- **States the old fact as current:** fix it, with the new fact's caveats.
- **Builds copy on the old fact** (an ad leading with the gap, an "honest limits" angle): flag it with a proposed replacement; someone may be running it.
- **Historical record** (change logs, dated notes, archives, a buyer quote from the time): leave it. Buyer quotes stay verbatim.
- **Competitive claim that depended on the gap:** fix and flag; the competitive story may need rethinking.
- **Adjacent gap that did NOT change:** leave it, and check it survived the edits.
- **Can't edit:** list with the exact wording to change.

## 5. Edit

- Smallest edit that makes the line true, in the doc's own voice and format.
- No process notes in finished docs (shared rule 6). Logs may get a dated entry.
- Keep the doc's claim tags; a provisional new fact is NEEDS VERIFY.
- Update local and wiki copies together.
- Never strengthen beyond the new fact: one customer live isn't "widely adopted".

## 6. Check

- Re-run the search. Every remaining hit should be deliberate.
- Confirm the unchanged gaps are still present.
- Read each edited passage in context.

## 7. Report

The change as pinned down; fixed (location, old line, new line); flagged for a decision (location, why, proposed replacement); left alone on purpose; can't edit (with exact wording); anything about the new fact still to confirm.

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
