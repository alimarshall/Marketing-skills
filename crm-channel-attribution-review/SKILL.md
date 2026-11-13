---
name: "crm-channel-attribution-review"
description: "Review B2B channel attribution from the CRM: closed-won and lead source fields, brand vs non-brand paid search, year-on-year and period-over-period funnel by channel (leads, disqualified %, SQL %, deal size, win rate, cycle), with a data-gaps list and deck lines. Use for \"look at attribution for our last 100 closed-won deals\", \"which channels are working\", \"YoY by channel\", \"qualified leads last 6 months vs previous\", \"what percentage gets to SQL\", \"average deal size by channel\", or \"make inbound ads all of paid\"."
---

# CRM channel attribution review

Answers "which channels are actually working" from the CRM. Every number comes from the CRM pull, never from memory or assumption.

## Inputs

- CRM and the account to use: `<fill in>`
- Rep-set source fields (e.g. Source Group, Source of Deal): `<fill in>`
- Pipelines that count as new business, and any to exclude (renewals, expansions): `<fill in>`
- Brand campaign or keyword naming in paid search (e.g. `{brand}`, your company name): `<fill in>`
- Channel definitions you want grouped (e.g. Paid = all ads + PPL + paid first touch): `<fill in>`

## Workflow

### 1. Settle the scope
- Window: last N closed-won deals, or a date range.
- For trends use three equal periods: last 6 months, previous 6 months, same 6 months last year. For YoY revenue use last 12 months vs the 12 before.
- New business only by default. Say what was excluded.

### 2. Find the fields before querying
Search the CRM schema for real property names, then pull enum options so labels are right. Typical set:
- Rep-set source fields
- Platform traffic source: original and latest, plus drill-down 1 and 2
- Stage-entered dates for SQL and every later stage, per pipeline
- Amount in home currency, create date, close date, pipeline, deal stage
- On contacts: original/latest source, first conversion form, UTMs, ad click IDs

Page through results. Large responses go to a file and get analysed with a script, not read by eye.

### 3. Analyse per channel
- Deals, revenue, share of revenue, average and median deal, median sales cycle
- Leads created, % disqualified, % reaching SQL or later, average and median qualified deal, closed won so far
- Win rate on qualified deals that have closed

Rules:
- Qualified date = the earliest stage-entered date at SQL or any later stage. Deals skip stages.
- Split paid search into brand and non-brand from the campaign or keyword in the drill-down fields. Brand paid mostly reflects people who already knew you.
- When asked for one Paid bucket: rep-tagged ads/PPL deals plus deals whose first tracked visit was a paid ad. Say which deals moved in from other groups.
- Treat "Offline" sources (CRM UI, extension, integration, import) as sales activity, not marketing. Flag integrations that overwrite the true first touch.
- When one or two deals drive a channel, show the figure with and without them.

### 4. List the data gaps
- Catch-all values ("Inbound - Other") with no detail
- Source values named after a person, or blank source groups
- Integrations overwriting first touch
- Empty campaign attribution fields
- No access to property history or attribution reports (name the missing permission or scope)

### 5. State the caveats every time
- Recent cohorts are immature: open leads mean SQL rates and wins for the latest period will rise.
- Counting by created date and by qualified date give different totals. Say which each table uses.
- Amounts are rep estimates until closed.
- Anything not checked deal by deal is "as tagged in the CRM". Use `deal-source-verification` for the big ones.

## Output

1. One-line answer first.
2. Tables per channel and period. Percentages over "X in Y".
3. What it shows, in short bullets.
4. Caveats and data gaps.
5. A one or two sentence deck line.
6. Optional CSV of deal-level fields with CRM links.

Plain language, no em dashes. Never edit CRM records without explicit approval.

## Works with

- `deal-source-verification` to check the deals a channel's numbers rest on.
- `paid-media-roi-and-cac` to turn these outcomes into return on spend and CAC.
