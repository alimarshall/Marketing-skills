# Measurement and optimization

Use [budgets and testing](budget-and-testing.md) when setting initial daily/monthly allocations, test funding, evidence windows and stop/hold/scale rules. Its numeric ranges are planning assumptions to adapt to the current company.

## Define success at the right level

Use a measurement ladder: qualified reach → meaningful attention → qualified response → held meeting/evaluation → opportunity → revenue. Choose leading indicators for learning, and commercial outcomes for business decisions. A video view, ebook download and demo request are different events.

| Motion | Delivery diagnostics | Quality/commercial evaluation |
|---|---|---|
| Awareness/TLA | Eligible reach, penetration, frequency, CPM, engagement type | Target-company/role fit, attention, relevant warm-pool growth |
| Video | Views, watch distribution, completion, cost per view | Attention relative to duration, eligible matched pool, subsequent quality |
| Ebook | Form opens, completions, CPL, delivery | Valid contacts, ICP-fit share, accepted leads, meetings and pipeline |
| Webinar | Registration completion and cost, attendance | Target-account attendance, questions, qualified follow-up and meetings |
| Demo/trial | Completed action and cost | Qualified/held demos, evaluations, opportunity creation and CAC |
| ABM/pipeline support | Account reach, relevant committee coverage, saturation | Meetings, stage progression, win/loss and sales feedback |

Do not infer named-person exposure from aggregate reporting. ABM influenced pipeline is not automatically sourced pipeline, and attribution is not proof of incremental causation.

## Read the data without changing its meaning

Record date range, timezone/currency, filters, attribution model/windows and entity level. Distinguish all-time entity aggregation from the selected reporting period; verify export headers rather than assuming a label overrides dates. Note intraday drift when repeated reads differ slightly.

Compare like with like: objective, format, geography, audience temperature, offer and maturity. Engagement CTR includes actions that are not website visits. Sponsored Messaging has send/open/click behavior unlike feed ads. A free/experimental placement can show impressions without paid cost; inspect current billing/placement context before calling it an error.

Calculate weighted metrics from matching numerators and denominators:

```text
CTR = relevant clicks / relevant impressions
CPC = spend / relevant clicks
CPL = acquisition spend / captured leads
Cost per qualified lead = matching spend / qualified leads
Cost per held qualified meeting = matching spend / held qualified meetings
Account reach coverage = reached eligible target accounts / eligible target accounts
```

Use blank/unavailable rather than divide by zero. Do not average row CPCs/CPLs or divide all-funnel spend by one subset of leads and label it direct-response CPL. If reporting blended acquisition cost, label the scope explicitly. Platform summary cost metrics may use only eligible objective-specific spend; reconcile their definitions before recalculating.

## Conversion and CRM checks

Inventory conversion rules with event definition, source, linked campaigns, status, attribution window/model and deduplication method. Inspect whether a selected rule is active, inactive, unverified or simply has no recent activity. Inactive signals are a diagnostic, not conclusive proof of a broken integration.

Define separate milestones for content acquisition, registration, booking, held qualified meeting, opportunity and customer. A success event should reflect the real action; a visit to `/request-demo` is not a submitted demo. Keep product/domain attribution separate in a multi-product account. Verify CRM source, account/contact joins, stage history and test-lead transport.

Use the correct click/view windows for the sales cycle and disclose them. Do not add platform-attributed revenue to CRM sourced revenue as though they are separate deals. If browser and server events represent the same action, implement and verify supported event-ID deduplication; similarly named rules alone do not deduplicate. [Conversion windows](https://www.linkedin.com/help/lms/answer/a426359), [deduplication](https://www.linkedin.com/help/lms/answer/a5967630).

Measure ebook and webinar cohorts through meaningful sales-cycle lags. Define qualified criteria and owners with sales. Use CRM opportunity creation dates and lead/cohort dates deliberately instead of comparing this week's spend to all historical pipeline. For ABM, consider account-level holdouts or comparable cohorts where feasible, while noting selection bias and sample limits.

## Diagnose delivery before changing strategy

Read in this order when spend or reach is low:

1. Account/billing/review/access state and campaign/ad-set/ad enabled status.
2. Parent/child dates, daily/lifetime caps and remaining budget.
3. Audience status, final eligible members, exclusions and regional constraints.
4. Format/placement eligibility, TLA permission and source-post status.
5. Bid competitiveness and optimization-event availability.
6. Saturation, source-pool replenishment and auction/market effects.

Only then propose changes. Too-small warm pools cannot be repaired by a bid increase. An enabled campaign with an expired parent schedule does not need new creative to begin serving. Do not automatically apply platform recommendations that broaden the ICP.

## Make optimization decisions proportionate to evidence

Classify the issue before choosing a remedy:

| Finding | Interpretation to test | Next action |
|---|---|---|
| Relevant reach, little attention | Message/creative or objective mismatch | Test a stronger problem/benefit or suitable format |
| High attention, poor qualified traffic | Low-intent interaction or unclear next step | Inspect click types, destination and offer |
| Form opens, few submissions | Friction, weak value exchange or technical issue | Inspect form and delivery; test justified simplification |
| Cheap leads, poor ICP | Eligibility, offer or source-quality problem | Check actual roles/companies and CRM qualification |
| Qualified leads, few held meetings | Handoff, follow-up, timing or promise mismatch | Check owner, speed and follow-up quality |
| Meetings, few opportunities | Sales/product fit or buyer readiness | Review calls and qualification, not only ads |
| High frequency, shrinking response | Saturation or repeated offer | Refresh relevant creative, reduce pressure or replenish qualified reach |

Set an evidence window, a decision threshold and a spend ceiling before a test. Use the new company's economics to set thresholds. There is no universal seven-day winner, ideal CTR, funnel budget ratio or fixed percent budget increase. Change one major dimension at a time when learning is the purpose; document unavoidable combined changes.

For sparse B2B data, retain uncertainty. Zero opportunities from a tiny immature cohort is not a definitive failure; many unqualified leads can still warrant action. Scale because commercial quality and reachable supply support it, not because cheap top-funnel metrics look good.

## Operating rhythm

For a copyable review request, use the [weekly optimisation prompt](../WEEKLY-OPTIMISATION-PROMPT.md). It covers comparable periods, matured quality, prior-change follow-up, exact pause/scale/refresh and targeting/list proposals, and a private action plan. A review does not authorize live changes or create a schedule.

Suggested cadence, adapted to spend and activity:

- Around launch/event deadlines: verify delivery, budget pressure, approval, routing and dates.
- Weekly: compare spend and quality, inspect demographics/company delivery, frequency, warm-pool growth, suppression/sync health and sales feedback; record proposed changes with evidence.
- Monthly or by sales-cycle cohort: revisit account tiers, list quality, opportunity outcomes, sourced/influenced distinctions and creative/offer learning.
- After a major ICP/product/CRM change: rebuild affected targeting and source definitions rather than merely renaming campaigns.

Use the private learning log in [operating records](../assets/operating-records.md). A recurring review is a recommendation workflow unless the user explicitly authorizes particular changes. Do not infer permission to modify spend or send outreach from a standing reporting request.
