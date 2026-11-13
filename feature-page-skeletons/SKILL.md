---
name: "feature-page-skeletons"
description: "Build landing page skeletons for product features, use cases or capability pillars from buyer research, VoC and verified product truth, on one template ending in security, support and CTA."
---

# Feature and use-case page skeletons

Turns buyer research and real product capability into a set of landing page skeletons for any B2B product. The skeletons cover one feature, a set of use cases (one page each) or a set of capability pillars.

Use it for: "a page for [feature]", "use case pages", "a page per agent", "pillar pages", "add [new feature] to the use case pages", or "same template for [feature]".

## Inputs

Read `company-context.md` first (repo root, or search the workspace for it) and use the fields that apply to this skill. If the file or a line is missing, ask once, then offer to save the answer back to it. Never fill a gap with an assumption about the company.

## 1. Gather evidence

For a set of pages, run steps 1 to 3 in parallel per group of pages, with one shared brief.

1. **Product truth first.** Check the product docs, roadmap, changelog, help centre and recent product syncs. Build a table with these columns:
   - capability
   - status: LIVE, ROADMAP, NOT BUILT or UNCLEAR
   - detail
   - source and date

   Then write a "safe to claim" list and a "never claim" list. The help centre often lags the product, so flag where it does.
2. **Buyer research.** Use the per-use-case research where it exists, plus the main pains and aspirations research. For each page, record:
   - evidence strength: strong, real but narrow, or thin, with account counts
   - who buys
   - pain in their words (paraphrased)
   - what they hope for
   - objections
   - competitors named
3. **VoC library and call recordings.** Filter by topic and count distinct companies per theme. Review-site quotes about the feature, with role and date, can go on the page.
4. **Proof.** List the published case-study figures and check each against its live source. Mark any figure that can't be verified.
5. **Keywords.** Volume and difficulty for 2 to 3 terms per page. Give pages that overlap different terms, so they don't compete.

## 2. The template (same order on every page)

| # | Block | Notes |
|---|---|---|
| 0 | SEO frame | URL, title tag, meta description, keywords |
| 1 | Hero | H1 under 10 words, subhead under 20, CTA, one cleared proof point |
| 2 | The dream state | One full-width statement: an H2 and one line on what good looks like, written from what buyers hope for, in the live site's voice. Pain stays in the research header |
| 3 | What it does | 3 to 4 cards in plain verbs, LIVE capabilities only |
| 4 | See it in action | 2 to 3 concrete moments (chat mocks or before and after), with design notes |
| 5 | Works with your systems, or a spec table | Honest about what's live; a neutral two-column spec table suits a single feature |
| 6 | Proof | Cleared figures only; otherwise write [proof needed] and name the candidate |
| 7 | FAQ | Real buyer objections you can answer honestly |
| 8 | Permissions and security | Shared block, plus one line per page |
| 9 | Implementation and support | Shared block: 3 visual cards, stats, quotes, plus one line per page |
| 10 | Final CTA | Specific to the page, e.g. "Bring your onboarding checklist to a demo" |

Above each page, write an internal research header with:
- evidence strength
- buyer
- pain in their words
- what they hope for
- positioning in one sentence
- watch-outs
- fixes needed outside the page

At the top of the file, add a "which pages to build first" table ranked by evidence, with a recommendation per page: build, build as supporting, fold into another page, or wait.

## 3. Voice and claims

- **Match the live site.** Read the current homepage and the key pages before writing, and reuse their recurring phrases. When a page contradicts the site (a timeline, a security claim), list it as a conflict for the owner to resolve.
- **Headlines carry the buyer's experience, not the mechanism's vocabulary.** Technical facts go in the body.
- **Only LIVE capabilities get stated as fact.** Roadmap items stay off the page.
- **Never say the product replaces people.** It hands unclear cases to a person.
- **New features.** When one ships, add its page next to its closest sibling and link them both ways. Move the overlapping keyword to the more specific page. Update the sibling page, the shared product-truth appendix and any pillar page that should link to it.
- **Copy:** run the team's writing-tells checklist before handing over. No em dashes, no "not X, Y" or "rather than" contrasts, no reflex rule of three, no AI vocabulary, plain language.
- **Customer language** from calls is paraphrased. Named customers need consent.

## 4. Output

One markdown file per set of pages. Each file holds, in this order:
1. the build-order table
2. the template
3. the rules
4. the shared security and support blocks
5. the keyword table
6. one section per page
7. an appendix with the product-truth table and global watch-outs

End your reply with the evidence strength per page, what was removed for overclaiming, and the [VERIFY] items that matter most.
