---
name: "paid-media-roi-and-cac"
description: "Pull ad spend from LinkedIn Campaign Manager and Google Ads by period, match it to CRM pipeline and wins, and report pipeline per pound spent, return on spend, cost per lead and media-only CAC by channel, plus events break-even when costs are missing. Use for \"LinkedIn costs and ROAS\", \"Google Ads ROAS\", \"what's our CAC\", \"pipeline per pound spent\", \"events return on spend\", or \"is paid working\"."
---

# Paid media ROI and CAC

Turns ad platform spend plus CRM outcomes into channel economics. Never invent spend: if a cost is missing, say so and give a break-even instead.

## Inputs

- Ad account links (LinkedIn Campaign Manager, Google Ads, others): `<fill in>`
- Account currencies and the conversion rate finance uses: `<fill in>`
- Event costs per event, or who holds them: `<fill in>`
- Channel definitions matching the CRM analysis: `<fill in>`

## Workflow

### 1. Find spend
Check in this order and say what was found:
1. CRM campaign spend fields (often empty).
2. Ad platforms directly, using the user's browser access:
   - LinkedIn Campaign Manager: Campaigns tab, custom date range, include Archived and Deleted in the status filter so old spend is complete. Read the totals row: spent, leads, cost per lead.
   - Google Ads: Campaigns page, custom date range (check the date format), read the "Total: Account" row: cost, conversions, cost per conversion.
3. Strategy docs, budgets, Slack and finance for events and anything not in an ad platform.

Use the same periods as the CRM analysis: last 6 months, previous 6, same 6 last year, plus 12-month totals. Convert currencies at a stated rate.

### 2. Match to CRM outcomes
Per channel and period:
- Qualified pipeline (by qualified date) and the part still open
- Leads created and % disqualified
- Customers and revenue won (12-month window by close date)

Keep one channel definition throughout, e.g. LinkedIn = rep-tagged LinkedIn ads deals plus deals whose first tracked visit was LinkedIn paid; Google = paid search first touch or rep-tagged Google. Split Google brand vs non-brand.

### 3. Calculate
- Pipeline per £1 = qualified pipeline ÷ spend for the same period
- Return on spend = revenue won ÷ spend (first-year deal value)
- Media-only CAC = ad spend ÷ customers won. No salaries, agency fees or tools; label it.
- Cost per lead from the platform's own figures, and platform conversions as reported
- Blended media CAC = all ad spend ÷ all new customers
- Events without costs: break-even = revenue won over the year; pipeline return = pipeline ÷ cost, to fill in later

### 4. Read it honestly
- Pipeline per £1 can rise while closed revenue lags. Name the deals that would change the picture if they close.
- Show any single deal that dominates a channel, with and without it.
- Brand search revenue mostly reflects existing awareness.
- Flag tracking gaps (no conversion value in the ad platform, missing pixels) that understate a channel.

## Output

Spend table by period and channel, an economics table (spend, customers, revenue, return, CAC, average deal), a pipeline per £1 table, short notes per channel, caveats (currency rate, media-only definition, deal values assumed annual), and a deck line per channel. Close any browser tabs you opened. Plain language, no em dashes.

## Works with

- `crm-channel-attribution-review` for the pipeline and wins by channel.
- `deal-source-verification` to confirm the big deals before calculating return.
- `tracking-audit-punch-list` when the platforms aren't recording conversions.
