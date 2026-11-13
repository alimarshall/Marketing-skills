---
name: "alternative-page-skeletons"
description: "Build evidence-backed \"[Competitor] alternative\" landing page skeletons from sales, CS and buyer data, positioned on your strengths. Use over competitor-alternatives when internal sales evidence should drive the page."
---

# Alternative page skeletons

Builds SEO "[Competitor] alternative" pages for any B2B product. Every page uses one shared template, and every claim is backed by evidence. The pages win on how you are better, never on the competitor's faults.

Use it for: "competitor landing pages", "[X] alternative page", "vs pages", "prep a page for [competitor]", or "add [competitor] to the competitor pages".

## Inputs

Read `company-context.md` first (repo root, or search the workspace for it) and use the fields that apply to this skill. If the file or a line is missing, ask once, then offer to save the answer back to it. Never fill a gap with an assumption about the company.

## 1. Gather evidence (sources in this order)

Run the internal sources in parallel where you can. Record what each source says, with its date.

1. **Existing competitor dossier, capability matrix and differentiation reference.** Read them first, so you only report what's new.
2. **Sales and CS docs** (wiki, battlecards, enablement pages, implementation notes, win/loss reviews). Sales has the strongest feel for where you win. When sales contradicts marketing's research, sales wins, and you record the correction.
3. **CRM.** Pull deals tagged with the competitor: count won, lost and open, deal size, company size, and closed-lost reasons. Note how many losses actually went to that competitor, and which accounts mention it but aren't tagged.
4. **Call recordings and the VoC library.** Find every account that named the competitor, and count distinct companies per theme:
   - why buyers consider the competitor
   - why they don't choose it
   - why they choose you
   - company size
   - which features they compare
5. **Public sources**, each with a URL and access date:
   - the competitor's site, pricing, changelog and docs
   - review sites, with dated verbatim quotes
   - comparison and listicle pages already ranking
6. **Keywords.** UK and US volume and difficulty for: "[competitor] alternative(s)", "[competitor] competitors", "[competitor] pricing", "[competitor] reviews" and "[competitor] vs".
7. **Your own product truth.** Check every capability you plan to claim against product docs and the roadmap. Tag each one LIVE, ROADMAP, NOT BUILT or UNCLEAR. Only LIVE goes on the page.

## 2. Turn the sales view into positive positioning

Write a table with these columns:
- how sales describes the competitor (internal only)
- what the page says instead (a positive claim about you)
- the features to lead with

Sales' language ("clunky", "Frankenstein", "overengineered") never appears on the page, and neither does anything that paraphrases it.

## 3. The template (same 10 blocks on every page)

| # | Block | Notes |
|---|---|---|
| 0 | SEO frame | URL, title tag (under 60 characters), meta description (under 155), H1 keyword |
| 1 | Hero | H1 under 10 words, subhead under 20, one CTA, proof strip |
| 2 | Why teams choose you | 3 cards, each a positive claim from the positioning table |
| 3 | Feature deep dives | 2 to 4 blocks: the features sales leads with for this competitor |
| 4 | AI or differentiator block | Shared block, plus one line tuned per page; supports the positioning and never leads the hero |
| 5 | Side by side table | Neutral, dated, sourced rows only, with your strengths first |
| 6 | Customer story | The published story that matches this competitor's main pain or your positioning |
| 7 | Switching block | Shared. Three visual cards (supported migration, a named person, roadmap influence), then review-site stats, then linked quotes. No timeline |
| 8 | FAQ | Only questions you can answer honestly |
| 9 | Final CTA | Specific to the page |

Above each page, write an internal header with the angle, the reader, the evidence counts, win/loss, watch-outs and fixes needed outside the page.

## 4. Rules

- **Say how you're better.** Competitor facts appear only as neutral, dated rows in the table. Concede where they lead, in the FAQ.
- **Can't answer it? Leave it off.** No cost FAQ unless you can state your own price. Never write a table row that needs a [VERIFY] to be true.
- **Features you don't build yourself** (payroll, ATS, devices): frame them as "the provider you choose, connected". Never use a row that reads as a weaker built-in version.
- **Customer stories:** match each story to the pain or positioning, never just reuse your best-known one. Call and VoC quotes stay internal. Review-site quotes go on with a link. Named customers need consent.
- **Plan detail** (which tier includes what) appears once, as small print.
- **Competitor-specific messages:** if a sales rep or loss note says a message confused buyers, keep that message off the page.
- **Don't build on a message about to go stale**, such as a capability your own roadmap is about to ship.
- **Copy:** run the team's writing-tells checklist before handing over. No em dashes, no "not X, Y" or "rather than" contrasts, no AI vocabulary, plain language, percentages over "X in Y".
- **Re-check competitor facts** the week each page ships.

## 5. Output

One markdown file, containing:
- the positioning table
- the template
- the shared blocks
- the customer-story matching table
- one section per competitor

When adding a competitor later, insert its page and update the shared tables. Then sweep the existing pages for any claim the new product-truth check has contradicted.

End with these lists, in this order:
- what changed from the dossier
- what's deliberately left off the page
- the things to check before publishing
