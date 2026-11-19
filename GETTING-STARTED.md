# Getting started

Use this guide when you're starting at a new company, or a new product line, with an empty folder and the instruction "let's get started". It sets the order to build things in, what "done" looks like for each layer, which skill handles which request, how to keep it all current, and how to set Claude up so the skills can do their work.

The rule underneath every step: **never invent a product fact, a customer quote, a stat or a competitor capability.** Each layer exists so the layer above it has something real to stand on.

## The journey at a glance

```
0  Set up Claude and company-context.md
1  Product truth ......... what the product really does
2  Buyer evidence ........ calls in, quotes and themes out (VOC bank, buyer research)
3  Cuts of the evidence .. use cases, industries, functions, personas, trends
4  Competitors ........... dossiers, then the matrices
5  The exec's voice ...... CEO / founder context file
6  Decisions ............. positioning, pillars, brand checks
7  Outputs ............... pages, ads, reports, thought leadership, newsletters, sales material
8  Measure ............... tracking, attribution, creative tests
9  Keep it current ....... sweeps, refreshes, claim propagation
```

Start at 0. You can stop at any layer and still have something useful, but don't skip a layer an output depends on (see "How the outputs connect" below). The journey ends at 8, and from then on step 9 keeps it running.

## Step 0: set up Claude and fill in company-context.md

**Claude setup**

- **Install the skills.** In Claude Code, copy the skill folders into `.claude/skills/` in your project (or `~/.claude/skills/` for every project). In the Claude apps, add each skill folder as a skill. Keep `company-context.md` and `scripts/verify_quotes.py` alongside them.
- **Connect your sources** so skills can read them directly: call recorder (Gong, Chorus, Fathom), CRM (HubSpot, Salesforce), wiki or docs tool (Notion, Confluence, Google Drive), chat (Slack), and the ad platforms when you get to ads. A skill that can't reach a source asks you to paste or attach it.
- **Give Claude a home for the work.** A project or working folder holding `company-context.md`, the reference docs as they get built, and an outputs folder. Put the house style and writing rules there too, so every chat starts with them.
- **Set standing rules once:** credentials are never printed; call quotes are internal until the customer consents; your banned words and constructions; date-stamped file names; where finished files go.

**company-context.md is the single setup file.** Every skill reads it first. Fill in what you know today; leave the rest blank. A skill that hits a blank line asks once and offers to write the answer back, so the file fills itself in as you work. For a second company, copy the file and fill it in again; no skill changes.

`creative-strategy/references/inputs.md` explains what each creative input is for and what happens when one is missing. It doesn't hold paths any more; those live in `company-context.md`. Some older skills still say "record this in inputs.md": record it in `company-context.md` instead.

**Done when:** company name, products, buyer, call recorder, CRM, output folders and house style are filled in, and the skills load.

## Step 1: product truth

| Build | Skill | Done when |
|---|---|---|
| Capability baseline: what the product reads, writes, triggers and can't do | `capability-boundary-map` | Every capability has a source (docs, spec, engineer), and there's a "sounds right but isn't" list |
| Product context for creative: site, brand assets, design references | `brand-product-context` | One source-linked brief, no competing catalogue |
| Behavioural pillars (Acts, Answers, Resolves and so on), when the product does many things | `capability-pillar-research` | Each pillar maps to real capabilities and real buyer quotes |

Nothing customer-facing gets written before this exists. It's the list every claim is checked against.

## Step 2: buyer evidence

| Build | Skill | Done when |
|---|---|---|
| Pull calls, group by prospect company (email domain, never call title), label seller and prospect lines | `call-research-trend-analysis` Step 0, or `buyer-call-synthesis` for a quick batch | One transcript file per company and a company table |
| Buyer research: pains, hopes, objections, personas, with named-account quotes | `buyer-research` | Each theme has quotes from at least 2 accounts, every quote checked word for word with `scripts/verify_quotes.py` |
| VOC bank: emotion-tagged moments (quote, emotion, theme, persona, company, date) | `buyer-research` (VOC library) | One running file, deduplicated, every row marked internal until consent |

This is where every angle, post and headline later comes from.

## Step 3: cut the evidence

| Build | Skill | Done when |
|---|---|---|
| Use-case and feature research (what buyers care about per feature) | `use-case-evidence-research` | Each use case has product truth, pains, quotes and gaps |
| Industry verticals and function jobs (People, IT, Finance; tech, retail, healthcare) | `vertical-persona-research` | Each industry meets the evidence bar or is marked thin |
| Persona deep dives (CPO, team leads, IT, CFO, CEO) | `persona-evidence-research` | Each persona has cares, frustrations, objections and openers with sources |
| Ad avatars (working situations for paid creative, which differ from personas) | `ad-avatars` | Each avatar is evidenced, with awareness state and language |
| Shares and trends: what % of buyers want X, how it's changing | `call-research-trend-analysis` | Rubric written, every company tagged, quotes re-verified, cohort and headline bases both stated |

## Step 4: competitors

| Build | Skill | Done when |
|---|---|---|
| Competitor dossiers, one per competitor per product line | `competitor-dossiers` (inside `competitive-intel-system`) | Fixed format, deal intel with sources |
| Master capability matrix, communication matrix (per feature: pain, outcome, proof, tier, angle), differentiation reference, verification tracker | `competitive-matrices` | Every rating and claim has proof, gaps are written down honestly |

## Step 5: the exec's voice

| Build | Skill | Done when |
|---|---|---|
| CEO or founder context file ("exec brain"): beliefs, stories, phrases, no-go areas | `exec-tl-context-file` | Gaps asked about and answered, written so AI can draft in their voice |

## Step 6: decisions

| Decide | Skill | Done when |
|---|---|---|
| Positioning and what to lead with, per product or release | `positioning-brief` | A brief plus a separate context doc, every claim checked against step 1 |
| One landing-page brief per pillar | `pillar-landing-pages` | Each page has its own URL, keyword and proof |
| Brand and copy rules applied mechanically | `copy-register-check` | Banned-construction list exists and is greppable |

## Step 7: outputs

| You ask for | Skill(s) | Reads from |
|---|---|---|
| Feature, use-case or competitor-alternative pages | `feature-page-skeletons`, `alternative-page-skeletons` | Steps 1 to 4, 6 |
| A paid campaign end to end | `ads-workflow`, which runs `creative-strategy`, `buyer-research-to-ads`, `customer-proof-to-ads`, `ad-creative-direction`, `product-ui-storytelling`, `ad-library-review` | Steps 1 to 4, ad avatars, 6 |
| Set up or run LinkedIn or ChatGPT ads | `linkedin-ads`, `chatgpt-ads` | ICP from step 3, creative from above |
| A data report or chart ("what % of HR teams…") | `call-research-trend-analysis`, then `research-data-charts` | Step 2 and 3 |
| Customer proof and stats | `customer-proof-from-usage-reports` | Usage reports, consent tracker |
| Exec thought leadership posts | `exec-post-skeletons-from-buyer-research` | Steps 2, 3 and 5 |
| Exec POV videos and teach-first video ads | `founder-pov-concepts`, `teach-then-sell-video-scripts`, `education-video-prep` | Steps 2, 3, 5 |
| Employee and sales-team LinkedIn posts | `employee-linkedin-posts` | Steps 2 and 3, the trend data |
| A content calendar | `research-led-content-plan` | Ranked signals from step 3 |
| Monthly product update email or newsletter | `product-update-email` (for newsletters, pair it with `research-led-content-plan` for the theme of the month) | Release notes, step 1 |
| Sales material: one-pagers, battlecards, account plans | `one-pagers`, `abm-account-multithread` | Steps 3 and 4 |
| Sales updates on trends and pains for outbound | `call-research-trend-analysis` cut into a short digest, plus `buyer-call-synthesis` for the latest calls | Steps 2 and 3 |

There's no dedicated newsletter or weekly sales-digest skill in this repo yet. The pairings above cover them; if you write the same digest every week, that's the next skill worth adding.

Before anything goes out: `claim-verification`, then `copy-register-check`.

## Step 8: measure

| Measure | Skill |
|---|---|
| Tags, pixels, conversion events, consent | `tracking-audit-punch-list` |
| Which channels produce pipeline and wins | `crm-channel-attribution-review`, `deal-source-verification` |
| Spend against pipeline | `paid-media-roi-and-cac` |
| Which creative worked, read honestly | `creative-testing` |

## Step 9: keep it current

| When | Run | What it does |
|---|---|---|
| Weekly | `competitor-buyer-sweep` | New buyer language and competitor mentions merged into the standing docs |
| When a feature ships or changes | `product-capability-refresh`, then `claim-propagation-sweep` | Baseline updated, then every doc and ad still saying the old thing is fixed |
| When a fact is corrected | `source-doc-writeback` | Fixes the source docs as well as the copy |
| Every two to four weeks | `call-research-trend-analysis` re-run on new calls | Shares, trends and projections refreshed; a dated change list |
| Monthly | `product-update-email`; review the VOC bank for new consent-cleared quotes | |
| Quarterly | `persona-evidence-research`, `vertical-persona-research`, `ad-avatars` refresh; matrices re-rated | |

## How the outputs connect

Most outputs share the same evidence. Build it once and the rest gets cheaper. These are common paths; use the ones that fit:

- **One research cut, many uses.** A trend from `call-research-trend-analysis` becomes a chart (`research-data-charts`), an exec post (`exec-post-skeletons-from-buyer-research`), an employee post, a sales digest line, an ad angle (`buyer-research-to-ads`) and a newsletter section.
- **One release, many surfaces.** A shipped feature goes `product-capability-refresh`, then `positioning-brief`, then a page (`feature-page-skeletons`), ads (`ads-workflow`), the product update email, and `claim-propagation-sweep` to fix older docs.
- **One fear, a full answer.** A top buyer fear from the trend data gets answered with proof (`customer-proof-from-usage-reports`), turned into a one-pager for sales (`one-pagers`), an objection-handling ad (`customer-proof-to-ads`) and an exec post.
- **One account, every seat.** `vertical-persona-research` gives the industry map; `abm-account-multithread` turns it into named people, openers and order; `linkedin-ads` runs the 1:1 or 1:few campaign.
- **Results flow back.** `creative-testing` and the attribution skills feed the learning log, which feeds the next `creative-strategy` run and the avatar refresh.

## What to say to Claude

- "Let's get started": Claude reads this file, checks `company-context.md`, and tells you which step you're on and what's missing.
- "We just shipped X": step 9, then step 6.
- "What are buyers saying about Y?": check step 2 docs first, then run a new pass if needed.
- "Make me a chart / post / campaign on Z": step 7, and Claude names the inputs it's using and any that are missing.
