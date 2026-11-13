---
name: "pillar-landing-pages"
description: "Split one product positioning brief into several landing-page briefs, one per capability, pillar or sub-product, each with its own URL, its own keyword research and full hero-to-CTA copy. Use whenever the user wants a separate landing page per feature or pillar, says each of these needs its own page, or wants to expand a positioning doc into page-level briefs. Builds only on existing evidence (never invents claims), runs fresh keyword research per page, and flags pages whose evidence is thinner than their siblings. Third step of a four-skill set: takes capability-pillar-research and use-case-evidence-research output; claim-propagation-sweep keeps it current."
---

# Pillar landing pages

Expands one positioning brief covering several capabilities, pillars or sub-products into standalone landing-page briefs, one per pillar, each with its own URL, keyword targeting and copy from hero to final CTA.

## Works with

- **Takes in:** a positioning brief, the pillar docs from capability-pillar-research, and the evidence docs from use-case-evidence-research. Approved claims and lead features come from competitive-matrices, customer stats from customer-proof-from-usage-reports. Every claim on every page must trace back to these.
- **Produces:** one page brief per pillar, with claim tags carried through, plus a combined parent page if asked.
- **Next:** copywriting and design. Each page is also the landing page for the matching ad group in use-case-ad-variations, so keep the page headline and the ad's claim in step. Run claim-propagation-sweep across these briefs whenever a product fact changes.

If the pillar or evidence docs don't exist, build them first rather than writing pages from memory.

## Why this differs from one combined page

A combined page lets the strongest two or three capabilities carry it while weaker ones are folded in. Splitting into N pages removes that safety valve: every pillar gets equal real estate whether or not it has equal evidence. A thin pillar can have its own page, but the page must be honest about it.

## Process, per pillar

1. **URL.** A consistent parent path with the pillar as the last segment, so the pages read as a family.
2. **Keyword research for this pillar,** not the product's umbrella term reused everywhere. Pull volume, difficulty and CPC (check the tool's currency units; some APIs return CPC in cents). Flag:
   - **Keywords that clash with the brand's positioning** (the best keyword is "ticketing system" but the product argues against ticket queues): keep it to title, meta and a supporting heading, or flag for a human.
   - **Terms whose search results are dominated by another format** (listicles, comparisons): recommend a different asset for that term instead of forcing the product page to compete.
3. **Title tag and meta description** from the primary keyword.
4. **Positioning summary:** 3-5 sentences from the source brief, the pillar's core claim and strongest evidence.
5. **The page,** structured the same across the family:
   - **Hero** (H1, sub, CTA): the pillar's sharpest specific claim, naming the mechanism.
   - **Proof strip:** 3-4 short, sourced claims. If a stat exists but isn't cleared, say so; don't use it or silently drop it.
   - **2-4 body sections** from this pillar's real evidence: what it does (from the capability catalogue), why it beats the obvious alternative, the objection this pillar must answer.
   - **Trust or security section,** placed high if the pillar touches permissions, compliance or AI-safety objections.
   - **Honest-scope section,** only when the pillar's evidence is thinner than its siblings.
   - **Cross-links** to the sibling pages.
   - **Final CTA.**
6. **Tag every claim** (shared rule 4) and run the quote check on any customer quotes used.
7. **Page-specific open items** at the end of each brief: unconfirmed numbers, customers pending approval, or a real question about whether the pillar deserves its own page.

## Done when

- Every page has its own keyword research.
- Every hero and proof claim traces to the source docs.
- Uneven evidence is visible in at least one honest-scope note, if the pillars are uneven.
- Pages cross-link to each other.

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

The wider marketing-skills set builds on the same docs: buyer-research feeds step 1, competitive-matrices holds the approved claims, and use-case-ad-variations, teach-then-sell-video-scripts and education-video-prep turn the evidence into ads and video. Claim tags mean the same thing in every skill.
