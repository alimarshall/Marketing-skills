# Build a similar LinkedIn program from scratch

Use this blueprint when a company wants the whole system built, rather than an audit or an isolated campaign. The worked example is fictional and the sequence is a planning recommendation. Adapt it to the company's evidence, audience supply, budget and sales capacity. Use [launch and change](launch-and-change.md) for current execution checks and [sources](sources.md) to recheck platform mechanics.

## 1. Translate the business into a build brief

Resolve the product, valuable customer problems, good-fit company traits, disqualifiers, markets, buying committee, sales cycle, available proof and success definition. Use the private [company intake](../assets/company-intake.yaml). Select one initial product, problem and market unless there is a reason to split. Agree the budget ceiling, period and follow-up owner.

Produce three decisions before building:

- **Who can buy:** company-fit rules and an approved account universe, or native company filters when a defensible list is unavailable.
- **Who needs to care:** problem owner, economic buyer and relevant evaluators, translated into titles or function plus seniority.
- **What happens after attention:** the next useful offer and a verified route to the website, form, event or sales team.

Fictional example: a workflow software business helps IT teams control access reviews. Its initial hypothesis is UK software companies with 200–2,000 employees. IT/security leaders own the problem, finance influences cost, and practitioners evaluate the workflow. These choices require validation; they are not a recommended ICP for every company. Translate 200–2,000 into the actual available size bands and record any approximation.

## 2. Build the account universe and source records

Research candidate companies from authorized CRM history, customer evidence, sales nominations and appropriate external company sources. Validate fit, country/market, corporate identity, domain, canonical LinkedIn Page and the reason to prioritize. Remove customers and open opportunities from new-logo acquisition where those motions are funded separately. Save a versioned master privately.

Tier by the work the company can actually deliver: a broad approved universe, a priority cluster with shared problems and sales coverage, and optional one-account plans for particularly valuable accounts. A tier label does not require a fixed number of accounts. A company list does not need each person's email to reach eligible committee members.

Create separate upload views from the master; use current LinkedIn templates and minimums from [lists and audiences](lists-and-audiences.md). Do not turn research columns into unsupported upload fields or pad a small list. Direct Company selection can suit a small named-account set if its final eligible audience is sufficient.

For the example, priority accounts are a subset of the broad universe. Give the priority cell precedence: exclude its company segment from the broad cell. This is a deliberate policy, not something inferred from the tier names. If sales cannot support a distinct priority story, start with one list instead.

## 3. Establish measurement, suppression and content

Before calling the program ready, connect the account/Page and website, set up the appropriate measurement path, define qualified lead/meeting criteria and verify lead routing. Agree which CRM rules define customers and open opportunities, whether they operate at company or person level, who maintains them and how changes reach LinkedIn. Use [launch and change](launch-and-change.md) for the complete preflight.

Prepare the minimum useful asset set: an approved problem/POV video or post, relevant proof or practical explanation, and a credible next action. Add a guide or webinar when it provides specific buyer value and somebody owns delivery and follow-up. A new program need not produce every format in the reference account.

Keep this source map in the private audience register. These are naming examples, not platform IDs:

| Audience record | Source and intended use |
|---|---|
| `COMPANY_CORE_v1` | Approved employer universe for acquisition |
| `COMPANY_PRIORITY_v1` | Priority employers; include in the priority cell, exclude from core if split |
| `COMPANY_CUSTOMERS_SYNC` | Verified customer-company rules; suppress new-logo campaigns |
| `COMPANY_PIPELINE_SYNC` | Verified open-opportunity companies; separate support motion where useful |
| `PEOPLE_VIDEO_TOPIC_90D` | Eligible selected-source viewers, chosen threshold, illustrative 90-day window |
| `PEOPLE_CONTENT_TOPIC_90D` | Relevant eligible document/form/ad behavior; keep source definitions explicit |
| `PEOPLE_SITE_RELEVANT_90D` | Relevant website visitors with a working measurement/consent path |
| `PEOPLE_OFFER_SUBMITTED` | Current offer submitters/registrants; suppress repeat acquisition |

Use only supported source types and windows in the live account. A naming label does not create a segment. New behavior audiences may start below usable size. Keep distinct source records for troubleshooting; combine related behaviors in a receiving audience when appropriate.

## 4. Turn it into campaigns and ad sets

Write the proposed hierarchy before creating anything. The following is a menu of cells to stage, not a requirement to launch all six. Keep exact IDs, budget, objective, format and targeting in the private campaign plan. Current platform labels can differ from older exports.

| Proposed campaign / ad set | Eligibility expression | Offer and optimization job | Launch condition |
|---|---|---|---|
| Education / Core | Target member geography AND core companies AND buyer roles MINUS priority companies, customers, pipeline and irrelevant employers | Eligible executive video TLA or company video; buy relevant attention using a supported objective | Fit, content, permissions, source audiences and measurement ready |
| Education / Priority | Geography AND priority companies AND relevant committee MINUS customers and pipeline | Cluster-specific problem/proof; select supported objective/format | Distinct narrative, sales coverage, enough eligible members and budget |
| Content acquisition / Guide | Geography AND chosen cold or warm ICP MINUS customers, separately funded pipeline and this guide's submitters | Useful guide with tested form or website delivery | Offer and routing ready; enough budget to assess quality |
| Nurture / Relevant warm people | Geography AND (topic video viewers OR relevant content engagers OR relevant site visitors) AND buyer fit where needed MINUS customers, separately funded pipeline and current-offer submitters | Proof, deeper learning or a related webinar | Warm pool is usable after filtering and message remains relevant |
| Evaluation / High intent | Verified relevant intent or chosen direct-response ICP MINUS completed converters, customers and separately funded pipeline | Demo/evaluation; optimize toward a supported, verified success action | Success event and follow-up work; scale supports a separate cell |
| Pipeline support / Committee | Geography AND open-opportunity companies AND relevant committee MINUS closed-won accounts | Peer proof, technical validation or a sales-coordinated invitation | Sales identifies the objection and owns the next action |

If using native prospecting, substitute defensible company facets for the account-list constraint. Do not OR a broad native audience with the company list and still call delivery restricted ABM. For sequential reporting, decide whether warm members should be excluded from cold cells; otherwise document intentional overlap. Exclusions for submitters apply to the relevant acquisition offer, not every future message.

For the example, start with Core education and, if it changes the decision and is affordable, a separate Priority cell. Prepare the warm sources immediately; activate nurture once the final eligible pool supports it. A guide can be the initial acquisition offer if it is the stronger starting asset. Existing first-party warm audiences may allow nurture at launch. Add pipeline support only when there are opportunities and a useful sales plan.

## 5. Connect the actual funnel dependencies

```text
Approved companies + relevant people
  -> eligible video/TLA with source ad-set IDs recorded
  -> selected-source viewer/engagement audiences
  -> related proof, guide or webinar when the pool is usable
  -> verified qualified response and appropriate follow-up

Guide submission
  -> asset delivery + correct CRM record and owner
  -> suppress the same acquisition offer
  -> relevant nurture; qualify separately for sales

Webinar registration
  -> suppress acquisition invitations + permitted reminders
  -> actual attendee / no-show reconciliation
  -> different recording, content and sales follow-up

Open opportunity
  -> separate company committee support where useful
  -> stage/objection-specific proof coordinated with sales
```

Use [funnels and offers](funnels-and-offers.md) for each format's mechanics. Register every new eligible video/TLA source in its intended audience definition; do not rely on matching names. Test the form-to-CRM path and asset access. External event attendance needs a verified event/CRM source. Retargeting does not guarantee an individual sees steps in this order, and some buyers will proceed directly to evaluation.

## 6. Stage launch by evidence and budget

Use [budgets and testing](budget-and-testing.md) for starting daily/monthly ranges by motion and ABM tier, actual-flight totals, evidence windows and scaling rules. Recalculate for the company's audience capacity and economics rather than treating the ranges as fixed defaults.

| Stage | Build or verify | Move on when |
|---|---|---|
| Foundation | Fit, account ownership, source lists, suppression, measurement, routing, approved assets | Required sources and primary success path are verified |
| Initial acquisition | The few cold/ABM or content cells needed for the first decision; behavior sources defined | Delivery reaches relevant companies/roles within the authorized limits |
| Nurture | Related warm offer and offer-specific suppression | Final eligible pool is sufficient and the offer/hand-off is ready |
| Conversion and expansion | Evaluation, event follow-up or pipeline support as justified | Quality, sales capacity and reachable supply support additional spend/cells |

These are readiness gates, not a promise to unlock a new funnel every seven days. If the account has no warm pool, do not fund empty retargeting cells. If contact match is poor, fix source quality before adding filters. If the budget cannot support separate tier/persona/format cells, consolidate the cells while preserving understandable logic.

Estimate media needs with explicit assumptions: `eligible members x planned reach fraction x planned frequency / 1,000 x assumed CPM`. For example, 10,000 eligible members, 50% reach, four impressions per reached member and an assumed 80 currency units CPM gives 1,600 currency units for that modeled exposure. This is arithmetic, not a LinkedIn benchmark, campaign minimum or delivery forecast; the live auction and actual reach can differ. Budget a test around the evidence needed for a decision and qualified-outcome economics. Keep the total concurrent plan inside the authorized ceiling.

## 7. Hand over a working operating system

The finished build should contain the company's private ICP decisions, approved master list and upload versions, audience register, targeting/exclusion matrix, campaign hierarchy with IDs, approved creatives/source posts, offer routing, measurement evidence, budgets/dates and current statuses. Save the change log, review date and rollback. Use [operating records](../assets/operating-records.md) rather than creating duplicate trackers.

After launch, check delivery and routing, then review actual company/role quality, combined frequency, source-pool growth, qualified responses and mature CRM outcomes. Add complexity when the evidence supports it. A draft is complete when reviewable; a launch is complete only when the authorized launch condition is verified. This blueprint alone does not authorize live changes.

When asked to build a similar system, deliver the adapted configuration and assets within the user's scope, not just a conceptual diagram or this generic example. State any missing access, source rules or company decisions that prevent the remaining work.
