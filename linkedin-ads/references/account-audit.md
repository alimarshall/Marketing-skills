# Reverse-engineer an account and take over operations

## Define the inspection boundary

Read-only is the default for research. Record the business/account/Page identities, observed date, reporting range, timezone/currency, permissions visible and evidence route. Business Manager ID and advertising account ID are different. If the supplied URL lists multiple accounts, identify the correct one from evidence rather than assuming the first row.

Use the available connector if sufficient; otherwise inspect the authenticated UI or exports. Document filters and pagination. Counts in an overview, status tabs and a filtered table can differ. Do not claim an exhaustive audit when only a sample of ad sets was opened. Label inventory coverage separately from detailed-settings coverage.

## Build four linked inventories

### Campaigns, ad sets and ads

Capture the hierarchy and entity IDs, status plus reason, objective, format, funnel job, offer, audience name, parent/child budgets, schedules, bid/optimization goal, placements and tracking. Include current spenders, active-but-not-delivering entities, strategically relevant paused history and draft activity separately. A live-looking toggle can be blocked by the parent; a paused historical test is not automatically a failed test.

Read current settings for representative cells covering native prospecting, company-list prospecting, one-company and clustered ABM, engagement/video TLA, ebook/document acquisition, warm nurture, webinar cold/warm/pipeline and demo activation where present. Expand the sample when a naming family contains different logic.

Do not reverse-engineer targeting from names alone. Inspect checked values, not all available options. Record contradictions between name and settings, such as Manager+ that includes Senior, or a named employee band that differs from the selected facets.

### Matched and Saved Audiences

Inventory names/IDs, source type, status, match rate, latest audience count, modified date, ownership, active associations and whether used as inclusion, exclusion or predictive seed. Capture all pages or state the limit. For key lists, find the source file/CRM rule, refresh owner, match exceptions and final campaign size. A high match rate does not establish source accuracy or ICP quality.

For behavior audiences inspect the actual source selections, lookback, threshold and downstream campaigns. Confirm new content feeds the expected warm pool. A cohort named for an event might contain companies, contacts, registrants or attendees; determine which before interpreting it.

### Offers, forms and creative permissions

Map offer → ad → form/event/landing page → delivery → CRM → follow-up owner. Check assets, consent/privacy-policy URLs, form questions/metadata, actual registration/attendance source, author permission for TLAs and any sender permission for messaging. Inspect destination and handoff behavior where possible. Do not send permission requests, post content or submit real leads merely to research the account.

### Measurement and commercial outcomes

Read conversion rules, status, event source/definition, linked campaigns, windows/model, CRM sync and available lead/opportunity outcomes. Keep selected inactive rules separate from the optimized event. Distinguish a received website signal from verified successful conversion firing.

Capture a dated performance sample to explain the setup's behavior, not to pronounce a winner without enough evidence. Use cost per qualified outcome and account progression where available. State if CRM or mature cohort data cannot be inspected.

## Reconstruct the operating model

Write an evidence-linked map showing:

```text
source systems/files
  → company/contact/behavior audiences
  → audience expressions and exclusions
  → objectives + offers + formats
  → form/event/website actions
  → CRM stages + sales/customer handoff
  → source refresh and optimization decisions
```

Explain which motions acquire new logos, educate cold accounts, nurture warm individuals, support existing opportunities and expand customers. Show where audiences overlap intentionally or unexpectedly. Do not assume a campaign-folder name proves a sequential funnel.

For every major conclusion distinguish:

- **Observed:** exact current selected settings or source records, with date/link.
- **Documented intention:** strategy/agency notes; may be historical or unimplemented.
- **Inference:** an interpretation of how observed pieces work together.
- **Recommendation:** what should change and why; not a claim it was already done.

Internal decks may contain unsupported benchmarks or claims that a format always outperforms another. Treat them as research leads, not established facts. Do not copy fixed budget splits, tier sizes, sales timelines or generic ROI claims into another company's system.

## Takeover gap list

Find the missing operating knowledge rather than only counting campaigns:

| Dependency | Questions the audit should resolve |
|---|---|
| Account selection | Who approves fit and tiers? Where is the evidence and current master list? |
| List production | Which system/query produces each upload? Does reupload replace membership? |
| CRM audiences | Company or contact object? Exact stage/association rules? Sync owner/frequency? |
| Exclusions | Which rules are global, product-specific, motion-specific or offer-specific? |
| Creative | Source files, authors/sponsorship permissions, approved claims, current versions? |
| Lead/event handling | Which system is registration/attendance truth? Who owns delivery and follow-up? |
| Measurement | Which event is primary? What does qualified mean? Which CRM outcome is reliable? |
| Changes | What was changed, why, by whom, when, and with what result/rollback? |

Ask the user only for gaps that available sources cannot resolve. Missing original uploads and CRM source rules prevent a complete reconstruction of membership; describe this directly rather than guessing from audience labels.

## Produce two separate deliverables

1. A private account-specific report with evidence, inventory coverage, exact targeting examples, funnel map, issues, unknowns and next actions.
2. A company-neutral operating guide containing the transferable decision rules, procedures, schemas and prompt examples.

Never publish the private audit, lists, contacts, internal links, account IDs or unpublished results to a public skill repository. For a new-company migration, explain which decisions can be reused and which data/assets must be rebuilt. An operating guide makes future work repeatable; it does not establish access, budget authorization or guaranteed profitability.
