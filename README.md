# Marketing-skills

Brand-agnostic Claude skills for B2B SaaS product marketing. One shared rule: never invent a product fact, a customer quote, a stat or a competitor capability.

## The skills

| Skill | Job | Say |
|---|---|---|
| [`vertical-persona-research`](./vertical-persona-research) | Research buyers by vertical: jobs the product does per function, what each industry cares about, buying-committee personas for ABM, with quotes and proof mapped to each | "what jobs can it do for Finance", "what does FinTech care about", "personas for ABM in healthcare" |
| [`abm-account-multithread`](./abm-account-multithread) | Multithread one named account: CRM, calls and public signals into a real buying-committee map, a distinct angle and opener per person, and the order to approach them | "multithread Acme", "who should we talk to at Acme", "we're single-threaded" |
| [`customer-proof-from-usage-reports`](./customer-proof-from-usage-reports) | Turn a customer usage report into proof: figures saved verbatim, derived maths labelled, wording guardrails, consent flag, stats mapped per persona, slide bullets | "save these stats", "what can we say with this", "slides per persona from these numbers" |
| [`tracking-audit-punch-list`](./tracking-audit-punch-list) | Audit tag manager, ad conversions, analytics, pixels, consent and CRM tracking; return a P0/P1/P2 punch list in operator shorthand plus an ID table | "audit our tracking", "are conversions firing", "simplify this audit" |
| [`crm-channel-attribution-review`](./crm-channel-attribution-review) | Channel attribution from the CRM: closed-won and lead sources, brand vs non-brand paid, YoY and period-over-period funnel by channel, data gaps and deck lines | "which channels are working", "attribution for our last 100 deals", "qualified leads vs last period" |
| [`deal-source-verification`](./deal-source-verification) | Check whether deals tagged to a channel really came from it, from the emails, notes and calls behind each one; verdicts with dated quotes and recomputed numbers | "was this deal actually from an event", "check the events deals in the pipeline" |
| [`paid-media-roi-and-cac`](./paid-media-roi-and-cac) | Pull spend from LinkedIn and Google Ads by period and match it to CRM pipeline and wins: pipeline per £1, return on spend, cost per lead, media-only CAC | "LinkedIn ROAS", "what's our CAC", "events return on spend" |

## How they fit together

`vertical-persona-research` builds the industry and function view. `abm-account-multithread` applies it to one named account. `customer-proof-from-usage-reports` produces the proof both of them map to each persona. `tracking-audit-punch-list` makes sure the campaigns built on all of this can be measured.

`crm-channel-attribution-review` shows which channels produce pipeline and wins. `deal-source-verification` checks the deals those numbers rest on. `paid-media-roi-and-cac` puts spend against the result.

## Setup

Each skill has an **Inputs** section with `<fill in>` placeholders: your capability baseline, buyer research, CRM, call recording platform and proof files. Fill them in once. The skills need your documents because they don't make anything up.

## What the method insists on

- Match call-recording accounts by participant email domain, never by call title.
- Quotes are verbatim and attributed. Named quotes and customer stats are internal until the customer signs off.
- No stat gets reworded into a stronger claim than its source supports.
- Every job or capability claimed has to exist in the product's real capability catalogue.
