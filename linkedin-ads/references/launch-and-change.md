# Setup, launch and change

## New-company foundation

Establish the ad account, owning Business Manager if used, associated company Page, relevant member permissions, billing owner, currency/timezone and responsible company team. The company should retain control of its assets and access. Inspect which roles are needed for campaign edits, Page sponsorship, lead retrieval and CRM integration rather than assuming one login covers everything. Handle payment, agreements and access grants under current environment rules.

Map the company website, registration and booking domains, privacy policy, CRM and campaign IDs. Install/verify the correct measurement path within authorized scope. Tag presence is not proof that the desired success event works. Define the primary conversion and quality criteria before choosing optimization. Build customer, internal and other appropriate suppressions plus the initial account universe and behavior sources. Avoid importing a previous employer's infrastructure or data.

## Build a reviewable campaign plan

Use one row per ad set with objective, format, audience expression, exact list/source IDs, exclusions, budget/currency, parent limits, dates/timezone, bid/optimization goal, creative/source-post IDs, destination, tracking, conversion rule IDs and lead-routing owner. Include the expected audience scale, success criterion and a review/stop condition. Save it privately using [operating records](../assets/operating-records.md).

Naming should describe reality without becoming the source of truth. A workable convention is `period | market | product | motion | audience | objective | offer | format`; shorten for platform limits. Record audience estimates as dated fields rather than treating a trailing count in the name as current reach. Use IDs to join reporting because names can change.

Set budget at the intended control level. A parent campaign end date, lifetime budget, pause or account hold can prevent an enabled ad set from delivering. Inspect parent and child settings together. A recommended bid is an estimate, not an instruction to increase spend.

## Prepare in the current Campaign Manager

1. Confirm account and Page; inspect existing campaigns and draft assets so the task does not create duplicates.
2. Choose the appropriate parent campaign and current Classic/automated creation route. Understand the hierarchy: current UI may say Campaign → Ad set → Ad, while legacy URLs/exports still say campaign group → campaign → creative.
3. Set the objective and supported format, then translate the written audience expression. Inspect selected values and checkboxes, including geography mode, language, list inclusion/exclusion and expansion controls.
4. Set placements deliberately. LinkedIn Audience Network controls distribution to partner sites; Audience Expansion changes audience eligibility. Do not conflate them. Start with an interpretable placement plan; test broader distribution separately when useful.
5. Set budget, run dates, optimization goal and bid strategy. Use end dates for time-bound invitations. Check all ancestor limits and planned simultaneous spend, not just one ad set's daily budget.
6. Add approved creative, forms, source posts and URLs. Verify TLA author permission and member-post eligibility. Reuse the original sponsored post appropriately; do not assume a TLA can be duplicated like an ordinary ad. [Create TLAs](https://www.linkedin.com/help/lms/answer/a5965137).
7. Set conversion tracking and URL parameters supported by the live UI. Confirm final resolved destinations and preserve existing query strings. Use consistent source/medium naming across the company's reporting; log legacy variants instead of rewriting history. Prefer stable ad-set/ad IDs alongside readable names. Native form reporting needs its own CRM mapping; UTMs alone do not establish native-form attribution.
8. Save drafts or paused entities where supported and authorized. Collect previews and IDs. Stop at any required approval or agreement step after the result is ready to review.

## Preflight with evidence

| Check | Evidence required |
|---|---|
| Correct company/account | Readback of account/Page and intended entity IDs |
| Audience means what the plan says | Current summary, selected source IDs, exclusions and final eligible size |
| Lists usable | Ready/appropriate current status and sufficient matched/final audience |
| Intentional overlap | Inclusion/exclusion matrix and combined frequency plan |
| Offer works | Accurate dates/timezone, destination, form, thank-you and asset delivery |
| Lead routing works | Test lead visible in the correct CRM record with asset/campaign mapping and owner |
| Primary event works | Observed success event or verified CRM event, not a conversion page visit alone |
| Spend bounded as intended | Parent/child budget and schedule readback in the correct currency/timezone |
| Creative authorized | Approved claims, rights and any source-post permission |

Do not require a fictional live purchase or submit real prospect data to test. Use the platform's supported test-lead flow and authorized test data; distinguish successful transport from actual customer qualification. A missing nonessential secondary metric need not block an otherwise measurable launch; an unverified primary success path must be disclosed and resolved before declaring readiness.

## Launch within scope and verify

Authorization should identify the account, entities, purpose, dates and spend limits sufficiently to act. A request to audit or create a playbook is not a launch instruction. When approval is required, show the concrete plan/previews and exact action; do not ask a vague permission question before doing preparation.

After an authorized launch, read back persisted settings, parent/child status and review state. Report Pending review, Building, Scheduled or Active accurately. An enabled toggle is not proof of impressions, and impressions are not proof of qualified results. Check initial delivery and event/lead routing when available. If the requested completion condition is delivery, keep following through to that condition or a concrete blocker.

## Update with a minimal diff

Read live settings before using an old plan. Prepare a concise before → after comparison and expected effect, including affected campaigns and shared audiences. Preserve unrelated settings and creative IDs. Useful examples:

- **New account cohort:** clean/match the new source, inspect eligibility, then change intended inclusions and competing exclusions together.
- **New creative:** retain the approved audience/budget, add the intended ads, and enroll eligible new source campaigns in warm audiences.
- **Budget change:** record old/new totals across all active siblings and parent caps; do not increase spend simply to clear an alert.
- **Webinar reschedule:** update creative, event/landing page, reminders and all schedules coherently; do not leave stale dates in one format.
- **Audience refresh:** inspect shared dependencies before changing a source that several campaigns include or exclude.

Execute only the authorized changes; reread the saved values and status. Log timestamp, IDs, reason, before/after, verification, review date and rollback. For changes that need a fresh campaign because a setting is immutable, prepare the replacement without silently enabling both. Keep old measurement history intact and label the new cohort/test.

## Rollback and recovery

Preserve the previous audience source/version and campaign configuration before material changes. A rollback may mean restoring prior targeting, reverting a source version, restoring the old budget or pausing a newly launched replacement. Explain that rollback cannot unspend delivered budget or revoke already viewed ads.

For errors, inspect actual state before retrying to avoid duplicate uploads/campaigns. If a connector call partially succeeds, use returned IDs and readback. After repeated failure at the same step, retain the prepared work and report the exact blocker. Never claim launch or a saved change from a button click alone.
