# Rebuild an existing program and close handover gaps

Use this with the [account audit](account-audit.md) when the user wants to recreate an existing setup or replace an agency. A reusable method and example prompts are not an exact record of an account's implementation. Keep the reconstruction packet in the company's private workspace; publish only company-neutral procedures.

## Verify the implementation behind each label

Inventory all relevant parent campaigns, ad sets and ads, including paused, draft and non-delivering work. Record pagination and filters. Compare the strategy document's tier definitions with actual company constraints, roles, source lists, creative, destination and sales actions. A group called Tier 3 can contain single-company drafts; a group called Tier 2 can mix individual companies and a shared company list. Treat tier numbers as local labels until their meaning is verified.

Distinguish account prioritization, personalization level and funnel stage. Targeting one employer with generic ads is account-specific media delivery; it does not establish a bespoke account narrative, landing page or sales program. Inspect text, visual, destination and sales handoff independently. Do not assume every ad with an account name in its internal label mentions that company to the buyer.

Cover every materially different configuration in the requested scope. Group genuinely identical copies after checking their differences; do not infer all family members from one example when geography, functions, list type, objective or lifecycle policy changes. For each family, report inventory coverage separately from settings, creative and downstream-system coverage. A zero-spend recent period does not prove a historical campaign never ran.

Find the prior test backlog and agency reviews where available, but reconcile them against the current account. A proposed control, a Not Started experiment, an old sender issue or a claim that one format wins is historical context until current settings and results support it. Preserve hypotheses, implemented changes and measured learning separately.

## Capture one private reconstruction packet per configuration

Extend the [existing operating records](../assets/operating-records.md) with evidence and dependencies rather than starting parallel trackers.

| Layer | Evidence to preserve |
|---|---|
| Identity and lineage | Account, parent, ad-set, ad, Page and original sponsored-post IDs; exact current names; dates and evidence links |
| Status and spend controls | Parent/child/ad status and blocking reason; objective, optimization, frequency control where available, bid strategy/value, budget mode/amount, parent cap, remaining budget, dates/timezone and currency |
| Audience | Actual selected geography and residency mode, profile language, company/list IDs, titles or function/seniority, other filters, explicit AND/OR logic, all exclusions, expansion mode and dated eligible-size estimate |
| Distribution | Feed, Audience Network and any other selected placement; current brand-safety settings where applicable |
| Creative | Original post versus direct sponsored content versus TLA; author/permissions, copy, headline, CTA, description, media/source-file location, version, rights and actual preview |
| Serving and reuse | Ad rotation setting, existing post associations, shared audience dependencies, and the effect of editing a reused post |
| Destination and tracking | Base destination, account/ad-set/ad parameters, resolved preview link, approved URL convention, redirects/domain, form/event identifiers and hidden metadata |
| Measurement | Selected conversion IDs versus the optimized action, event definitions, attribution, deduplication and test evidence |
| Handoff | Asset delivery, registration/attendance truth, CRM field mapping, object/stage, consent handling, owner, follow-up and suppression update |
| Ongoing operation | Master source/query, matching exceptions, refresh owner, new-content enrollment, change history, review condition and rollback |

Inspect the actually selected creative in editors and previews; a route or old selection can open a different member of a multi-ad set. A screenshot proves the observed rendering, not ownership of the editable source asset. Obtain original media and production files where the task requires recreating them.

## Check the dependencies most often missing from the ad account

Use [source and handoff QA](source-and-handoff-qa.md) for the step-by-step checks behind list identity, upload lineage, CRM stage definitions, event denominators and audit completeness.

**List provenance:** find the authorized source file or exact CRM query behind each important inclusion and exclusion. Preserve company/contact object type, corporate-identity rules, lifecycle conditions, sync frequency, source owner and membership version. Ready status and match rate do not establish selection quality. If source rules cannot be inspected, mark membership reconstruction incomplete.

**Creative reuse and rotation:** inspect original post IDs and where each post is used before proposing edits. Direct sponsored content edits can affect other ad sets using that post; verify the current warning and associations. Reuse, create a new version or replace deliberately. Record performance optimization versus even rotation where supported. Even auction entry is not a guarantee of equal delivered impressions. A long creative inventory is not evidence that the budget can evaluate every variant.

**Format-specific settings:** for Conversation ads, preserve the actual sender and signature, personalization tokens and fallbacks, opening message, every CTA/button and branch, terminal messages, linked forms and each destination. For Message ads, capture the sender, subject/body, CTA and destination/form. For TLAs, capture the actual author, original post, sponsorship state and eligible retargeting source. For Spotlight or other dynamic formats, inspect the dynamic fields, image/logo, headline, CTA and destination. A headline and targeting screenshot do not reconstruct these experiences.

**Tracking composition:** compare the base destination, configured parameter fields and actual preview link. Inspect duplicate keys, conflicting values, repeated encoding, spaces/non-ASCII names, preserved query strings and CRM-added parameters. A hypothetical URL with both `utm_medium=paid` and `utm_medium=paid_social` needs an explicit convention and a check of what analytics/CRM actually records; do not assume every parser selects the same value. Determine which system owns each parameter before changing it. Prefer stable entity IDs alongside names. Keep native form metadata and CRM mapping separate from website UTMs.

LinkedIn confirms that configured parameters combine with existing destination parameters rather than replacing them. Its hierarchy change also distinguishes campaign, ad-set and ad macros. Verify the current supported macros and record which entity each reporting field identifies. [Official URL parameter guidance](https://www.linkedin.com/help/lms/answer/a5968064), checked 19 November 2026.

**Offer lifecycle:** inspect the full path after a click or form submission, including confirmation, asset access, qualification, CRM delivery and follow-up ownership. Webinar invites require registration suppression, event cutoff and real attendee/no-show data. Inspect actual sources rather than assuming an external attendance integration exists. Use authorized test data and supported test flows; do not submit real prospect details just to audit.

Use the actual saved-ad preview and available placement views to inspect rendering and the link. A preview is a representation, not a guarantee of identical delivery on every device. Messaging formats have different preview/test routes; do not send a test message as an unrequested side effect of inspection. [Official preview guidance](https://www.linkedin.com/help/lms/answer/a424528/preview-your-ad-in-campaign-manager), checked 19 November 2026.

**Permissions and infrastructure:** identify who owns the account, Page, source posts, lead retrieval, CRM integration, website/tag manager and source assets. Record the access needed for the requested work and any dependency that cannot be transferred to a new company. Do not grant access or send author/sender permission requests as a side effect of read-only research.

**Delivery and commercial quality:** inspect parent holds/end dates, draft validation failures and final audience eligibility before interpreting an enabled toggle. Review delivered company/role demographics, saturation and qualified CRM outcomes when available. Proposed targeting is not proof of actual delivery; delivery is not proof of incremental pipeline.

## State readiness precisely

For each motion, mark the following separately with an evidence link, unknown or blocker:

1. **Method documented:** the decision process and build steps exist.
2. **Settings captured:** the requested configuration and creative dependencies have been read and recorded.
3. **Sources reproducible:** original list/query, assets, permissions and refresh ownership are verified.
4. **Handoff tested:** the intended event, offer delivery and CRM route work with authorized test evidence.
5. **Live outcome verified:** the authorized launch/delivery condition and subsequent quality checks are observed.

Do not describe all five as complete because a generic playbook exists. For another company, rebuild its lists, roles, proof, permissions, URLs, event IDs and economics. Preserve the transferable reasoning; correct confirmed defects and stale settings in the proposed new build rather than reproducing them silently. Keep the original snapshot intact and distinguish observed behavior from the recommended replacement.

## Finish the handover

Deliver a private coverage matrix, reconstruction packets, source/dependency map and prioritized unresolved-work list. Explain which gaps can be closed from LinkedIn, which require CRM/event/website/source-file access, and which need a business decision. Finish all accessible independent work before asking for the missing dependency. Use [launch and change](launch-and-change.md) for authorized draft preparation, launch and readback.

Example request:

> Use the linkedin-ads account audit and rebuild-and-handover guides. Reconstruct each distinct configuration in [campaign scope], including actual tier meaning, targeting, creative/post reuse, rotation, complete tracking URLs and downstream handoffs. Inventory the full scope and state what was inspected in detail. Save private reconstruction packets and identify any source rules, permissions, assets or tests still missing. Do not change the live account during the audit.
