# marketing-skills

Claude skills for B2B SaaS product marketing. Positioning, paid creative, content planning, and the verification discipline that keeps all three honest.

Twenty-one skills, one shared spine: **never invent a product fact, a customer quote, a stat or a competitor capability.**

## The skills

### Positioning and messaging

| Skill | Job | Say |
|---|---|---|
| [`positioning-brief`](./positioning-brief) | Turn a PRD, spec, changelog or release note into positioning, what to lead with, messaging, and channel-ready copy. Produces a clean brief plus a separate context document | "we just shipped X", "what do we say about this", "what do we lead with" |

### Paid creative

| Skill | Job | Say |
|---|---|---|
| [`creative-strategy`](./creative-strategy) | Run creative strategy end to end: buyer research, avatar mapping, competitor ad-library teardown, positioning, angles by awareness state, hooks and creative mechanics, concepting, then a strategy brief, a production brief, ad copy variations and visual direction | "we need new LinkedIn ads", "what angle should we run", "tear down their ads", "brief the designer" |
| [`ad-avatars`](./ad-avatars) | Build a new ad avatar, or refresh the standing avatar library as new evidence lands | "build an avatar for the economic buyer", "refresh the avatars", "we have sign-off now" |
| [`creative-testing`](./creative-testing) | Design the test plan for paid creative and read results honestly at B2B budget scale: naming, the diagnostic ladder, fatigue, attribution, the learning log | "is this ad working", "how do we test these", "should we kill this ad" |
| [`chatgpt-ads`](./chatgpt-ads) | Operate ChatGPT Ads: setup, tracking, context hints, copy, bidding, weekly reads, keep or kill calls, competitor checks | "set up ChatGPT ads", "write context hints", "weekly ChatGPT ads read" |

### Pages and collateral

| Skill | Job | Say |
|---|---|---|
| [`capability-pillar-research`](./capability-pillar-research) | Regroup buyer research and the real capability catalogue into verb-based pillars rather than features or modules | "organise this by what the product actually does", "build the pillar docs" |
| [`pillar-landing-pages`](./pillar-landing-pages) | Split one positioning brief into a landing-page brief per pillar, each with its own URL, keyword research and hero-to-CTA copy | "a page for each pillar", "landing page per capability" |
| [`one-pagers`](./one-pagers) | Build a one-page leave-behind, battlecard, objection sheet or champion one-sheet where every claim survives a sceptical reader | "make a one-pager", "leave-behind for the migration conversation" |

### Comms

| Skill | Job | Say |
|---|---|---|
| [`product-update-email`](./product-update-email) | Compile the recurring customer product-update email: find the last one sent, find what shipped since, group and draft | "draft this month's product update" |
| [`employee-linkedin-posts`](./employee-linkedin-posts) | Ghostwrite LinkedIn posts for employees building a personal brand as practitioners in the buyer's field, never as salespeople. Ships with a fill-in company context template | "write me a LinkedIn post", "fix my LinkedIn headline" |

### Content planning

| Skill | Job | Say |
|---|---|---|
| [`research-led-content-plan`](./research-led-content-plan) | Build a multi-week content calendar from ranked buyer signals cross-checked against real product usage, rather than from a feature list | "plan a month of content", "what should we post", "social plan for the launch" |

### Buyer, account and proof research

| Skill | Job | Say |
|---|---|---|
| [`vertical-persona-research`](./vertical-persona-research) | Research buyers by vertical: jobs the product does per function, what each industry cares about, buying-committee personas for ABM, with quotes and proof mapped to each | "what jobs can it do for Finance", "what does FinTech care about", "personas for ABM in healthcare" |
| [`abm-account-multithread`](./abm-account-multithread) | Multithread one named account: CRM, calls and public signals into a real buying-committee map, a distinct angle and opener per person, and the order to approach them | "multithread Acme", "who should we talk to at Acme", "we're single-threaded" |
| [`customer-proof-from-usage-reports`](./customer-proof-from-usage-reports) | Turn a customer usage report into proof: figures saved verbatim, derived maths labelled, wording guardrails, consent flag, stats mapped per persona, slide bullets | "save these stats", "what can we say with this", "slides per persona from these numbers" |

### Measurement

| Skill | Job | Say |
|---|---|---|
| [`tracking-audit-punch-list`](./tracking-audit-punch-list) | Audit tag manager, ad conversions, analytics, pixels, consent and CRM tracking; return a P0/P1/P2 punch list in operator shorthand plus an ID table | "audit our tracking", "are conversions firing", "simplify this audit" |

### Verification and upkeep

| Skill | Job | Say |
|---|---|---|
| [`claim-verification`](./claim-verification) | Check that every factual claim is traceable, correctly scoped and safe to publish | "can we say this", "check these claims", "is this safe to publish" |
| [`copy-register-check`](./copy-register-check) | Check finished copy against a house style rule set using a literal search rather than a read-through | "run the copy sweep", "check this against our style guide" |
| [`capability-boundary-map`](./capability-boundary-map) | Turn a scope document, permissions table or API spec into a plain-language map of what the product can read, change and cannot touch | "what can it actually do", "what are the limits", "can we claim X" |
| [`source-doc-writeback`](./source-doc-writeback) | A fact changed, so find every internal document carrying the old version and fix it | "update all our docs that reference X", "propagate this correction" |
| [`competitor-buyer-sweep`](./competitor-buyer-sweep) | Recurring sweep that folds new buyer language and competitor mentions into the standing research docs, additively. Can run on a schedule against a call recorder | "run the buyer sweep", "check for new competitor mentions" |
| [`product-capability-refresh`](./product-capability-refresh) | A feature shipped or changed, so fold it into the capability baseline and every doc that shares that ground | "we just shipped X, update the capability docs" |

## Using these for any company

Every skill reads [`company-context.md`](./company-context.md) first: the company, products, capability baseline, evidence sources, output folders and house style. Fill it in once. For a different company, copy the file and fill it in for that company. No skill hard-codes a brand, product, customer or tool, so nothing else changes. If a line is blank, the skill asks once and offers to save the answer back.

### The buyer research loop

`vertical-persona-research` builds the function and industry view and the industry buying-committee maps. `abm-account-multithread` starts from that map for a named account, and writes new persona insight back. `customer-proof-from-usage-reports` turns usage reports into guardrailed stats that both of them pull into their proof sections. `tracking-audit-punch-list` makes sure the campaigns built on all of this can be measured. Each skill has a **Works with** section naming its inputs and hand-offs; any skill named there that isn't installed is done inline.

## How they fit together

`creative-strategy` reads the avatar library as an input. `ad-avatars` maintains it. Keeping them separate stops a campaign run from quietly rewriting the research it is standing on.

`positioning-brief` decides what to say about a product change. `creative-strategy` turns a settled message into ads. `research-led-content-plan` turns research into a calendar. Running creative off an unsettled position is the most common way a campaign burns a month.

`capability-boundary-map` is what the other five check claims against. `claim-verification` and `copy-register-check` are the last two steps of any workflow producing customer-facing copy. `source-doc-writeback` is what you run when verification finds that a source document, rather than the copy, is the thing that is wrong.

`competitor-buyer-sweep` keeps the outward-facing research current and `product-capability-refresh` keeps the inward-facing product truth current. Everything else reads from those two. `capability-pillar-research` feeds `pillar-landing-pages`, and `creative-testing` closes the loop on what `creative-strategy` and `chatgpt-ads` put live.

A few skills hand off to general marketing skills that are not in this repo (`paid-ads`, `page-cro`, `ad-creative`, `ab-test-setup`, `analytics-tracking`, `gong-transcripts`). They work without them; the hand-off just names where that job goes if you have one installed.

## Setup: two edits, once

These skills invent nothing, which means they need your documents.

1. **Fill in [`creative-strategy/references/inputs.md`](./creative-strategy/references/inputs.md)** with your own paths: capability baseline, claim verification tracker, buyer research, messaging matrix, brand voice and writing rules, competitor dossiers. That file is the contract for the whole repo, and it also tells you what a skill does when a document is missing. `positioning-brief` reads the same list.
2. **Fill in the constraint tables** in [`angle-library.md`](./creative-strategy/references/angle-library.md) and [`hooks-and-mechanics.md`](./creative-strategy/references/hooks-and-mechanics.md) against your own brand rules. Both ship as templates listing the angles and hook tactics that are *commonly* constrained in B2B, with the category of constraint that usually blocks each. Filling them in is the highest-value setup step in the whole thing, because it converts brand rules into creative decisions rather than leaving them as a review gate someone fails at the end.

Several newer skills also carry their own short **Inputs** section with `<fill in>` placeholders, and `employee-linkedin-posts` ships `references/company-context.md` as a template to fill in. Record paths in `inputs.md` where you can, so there is one list.

`copy-register-check` also needs your banned-construction list. If one does not exist, build it from the last three rounds of editorial feedback. The rules people actually enforce are the ones they keep correcting.

Nothing else needs changing.

## Layout

```
positioning-brief/SKILL.md          the 9-step workflow, brief plus context split
claim-verification/SKILL.md         claim extraction, evidence tiering, consent, never-say
copy-register-check/SKILL.md        greppable rules, the manual pass, cut rather than rephrase
capability-boundary-map/SKILL.md    read / write / not-exposed, and the adjacent-sounding cases
source-doc-writeback/SKILL.md       ground truth first, sweep, ownership, verified edits
research-led-content-plan/SKILL.md  signals, usage cross-check, themes, calendar, signal-to-post map

creative-strategy/
  SKILL.md                        the 12-step workflow
  assets/ad-mockup.html           renders concepts as feed previews, with the fold and dark mode
  references/
    inputs.md                     what you supply, what each document is for, the reading budget
    ad-avatars.md                 the avatar method, as a campaign run consumes it
    pain-mapping.md               five-bucket extraction, signal scoring, the pain x avatar matrix
    hooks-and-mechanics.md        the layer stack, the hook tactics, the eight creative mechanics
    creative-matrix.md            awareness deployment, the diversity check, volume, offers
    production-brief.md           designer-facing brief, file naming, copy variations, QC gates
    competitor-teardown.md        ad-library mechanics, the SOV grid, staleness rules
    angle-library.md              the angle taxonomy and the angles you probably cannot use
    format-library.md             18 static formats, carousel, document, video, thought leader
    platform-specs.md             specs and the four constraints that actually shape writing
    brief-template.md             the 9-section strategy brief and its verification checklist
    research-method.md            four forces, the awareness ladder, scoring filters
    visualisation.md              the fidelity ladder and wireframe notation

ad-avatars/
  SKILL.md                        BUILD, REFRESH and REVIEW modes

creative-testing/
  SKILL.md                        test design, naming, reading results, closing the loop
  references/                     test-design, diagnostics, measurement, learning-log

chatgpt-ads/SKILL.md                operator method; fast-moving platform facts flagged to re-verify
competitor-buyer-sweep/SKILL.md     scheduled or on-demand sweep, additive writes, propagation
product-capability-refresh/SKILL.md ship-to-docs propagation, the docs a first pass usually misses
capability-pillar-research/SKILL.md verb pillars, quotes cross-checked against the capability catalogue
pillar-landing-pages/SKILL.md       one brief per pillar: URL, keywords, hero to CTA
one-pagers/SKILL.md                 one audience, one argument, layout rules, claim tags
product-update-email/SKILL.md       last-sent cutoff, shipped means shipped, grouping, sanity checks

vertical-persona-research/SKILL.md  function, industry and ABM persona lenses, call mining, evidence bar
abm-account-multithread/SKILL.md    committee map, one angle per thread, sequencing, openers
customer-proof-from-usage-reports/SKILL.md  verbatim capture, guardrail table, persona mapping
tracking-audit-punch-list/SKILL.md  P0/P1/P2 in shorthand, confirmed-firing rule, ID table

employee-linkedin-posts/
  SKILL.md                        intake, content lanes, post mix, profile guidance
  references/company-context.md   fill-in template: buyer field, proof points, language rules
```

## What the method insists on

**Never invent a product fact, a customer quote, a stat or a competitor capability.** Every claim in a brief is traceable or flagged. Quotes are reproduced word for word from the source file, never from working notes, because the tidied version always reads better and that is exactly the problem.

**Consent travels with the quote.** Anything from a sales call, win/loss or a named customer is internal-use-only until sign-off exists. It can shape an angle and sit in a brief under that banner. It cannot be the ad.

**Three things get confused and must stay separate.** Confirmed to work, safe to say publicly, and confirmed by a customer. A capability can be live and un-announceable. An engineer confirming it works is not a case study.

**Angle before execution, and test angles against each other.** A strong angle survives a weak hook. Running five hooks off one angle and calling it creative testing tells you about wording and nothing about the argument.

**Unclaimed is not defensible.** White space found only in a teardown is a guess. Cross it against your own buyer research, then apply the swap test: could a competitor say this truthfully too?

**A verification claim is worth nothing without the output.** The sweep counts when it is run mechanically over the finished text, after the last edit, and reports what it found including the zeroes. This is the single most repeated failure across every skill here.

**Price the set before you write it.** Budget divided by variants divided by weeks, against what the decision actually needs. A twelve-concept set handed to a budget that can read three is a wasted week.

## Two things it is deliberately honest about

**No ad library exposes performance for ordinary commercial ads.** Not spend, not click-through, not conversions. What a teardown gives you is longevity and variant repetition, which are hypothesis signals. `competitor-teardown.md` also documents, verified against a live ad, exactly how much the EU transparency layer does and does not disclose, because most secondary write-ups overstate it.

**There is no platform or industry creative-diversity score.** The six-dimension check in `creative-matrix.md` is defined in this repo and labelled as such, rather than dressed up as a standard.

## Volume: pick the right branch

The high-volume performance-creative canon and low-volume B2B reality are two disciplines sharing a job title, and averaging them produces guidance that fits neither. `creative-matrix.md` section 4 branches: sharply targeted B2B audiences at high CPMs get two ads per campaign, two full weeks minimum, and a call at 80 to 85 per cent confidence, because waiting for 95 at that volume means never deciding. The weekly conveyor and the concept-count tables belong to the other branch.
