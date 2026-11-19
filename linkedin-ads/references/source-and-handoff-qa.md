# Validate sources and downstream handoffs

Use this when taking over an account or preparing a rebuild. A campaign can be reproducible in Campaign Manager while its source membership, lead routing or commercial measurement remains unverified. Keep all completed records in the current company's private workspace.

## Make audit coverage trustworthy

1. Record every entity in the requested scope, its parent, status, ID and actual detail link. Include drafts and historical work when requested. Reconcile pagination and filters before declaring the inventory complete.
2. Open saved settings and wait for the relevant audience controls to finish loading. Capture each selected inclusion, narrowing group and exclusion. A visible page heading does not establish that asynchronous list membership or forecast widgets have loaded.
3. Preserve the raw observation and extraction date. Mark unresolved loading indicators, blank controls, unavailable sections and invalid forecasts as unknown. Never turn a partial page or `NaN` forecast into a complete configuration or an audience estimate.
4. Track inventory, settings, ads/previews, source files and downstream tests separately. Give counts and an exception list. A representative sample can explain a motion; it cannot establish that every sibling has identical settings.
5. Save checkpoints as you work. If the platform rate-limits access, stop requests, retain the exact unfinished scope and resume after a cooldown. Use supported exports if they contain the required fields. A performance export alone does not reconstruct targeting. Do not bypass an access restriction or repeatedly open parallel sessions to defeat it.

## Establish which list actually produced the audience

Check regional availability before copying historical facets. Member Groups cannot target members in the EEA or Switzerland, and some other audience types have limited reach there. Replace unsupported criteria with verified buyer-fit attributes and re-estimate eligibility; do not enable expansion merely to conceal an invalid strict-ABM audience. A summary disabled by a validation error needs the saved criteria and warning recorded explicitly. [LinkedIn targeting guidance](https://www.linkedin.com/help/lms/answer/a417950), checked 19 November 2026.

For every material company or contact audience, complete this private mapping:

| Field | Required evidence |
|---|---|
| Source | Authorized system/file, exact tab or query, object type and source owner |
| Selection | ICP/intent/lifecycle conditions, exclusions, product and market scope |
| Version | Export timestamp, nonblank eligible rows, normalization rules and file checksum |
| Transformation | Column mapping, deduplication key, rejected records and reviewed corrections |
| Upload | Exact audience ID, upload/update date, source method and membership policy |
| Matching | Processing state, matched entities/members, match exceptions and dated eligible reach |
| Use | Ad sets using the audience, inclusion versus exclusion, and other audiences combined with it |
| Maintenance | Refresh owner, cadence or trigger, failed-sync alert and removal/suppression process |

A similarly named spreadsheet is a candidate source until upload history, owner confirmation or an exact export establishes lineage. Spreadsheet grid dimensions are not record counts. Source account rows, matched companies, matched members and eligible audience are different denominators.

Before preparing a company upload:

- Confirm canonical company identity, official domain and the correct LinkedIn company page. A search-results URL is not a company-page URL. Check parent versus subsidiary, regional pages, product pages and unrelated namesakes.
- Keep internal annotations out of company-name fields. Preserve legal/trading-name decisions in a review column rather than silently inventing identifiers.
- Check missing identifiers, duplicate domains, multiple brands sharing one domain and acquired companies. Resolve ambiguity against reliable evidence; keep unresolved rows in an exceptions file.
- Record the confidence, evidence date and source for technographic or intent signals. A vendor flag that marks nearly every company is weak selection evidence until independently validated.
- Use the current platform template. Populate supported upload fields only; retain research, sales notes and contact details privately in the master source.

For contact lists, verify the lawful source and current matching fields, normalize identifiers, deduplicate people and map employment changes. Do not treat a lead-research export or Sales Navigator list as an upload-ready, permission-cleared contact audience.

For strict ABM, validate that the final expression constrains delivery to the approved companies and intended roles. A large matched-member total does not establish committee coverage; a short list of named contacts does not establish a deliverable advertising audience.

Before launch or reuse, compare approved versus saved geography, employer pages/list IDs, person facets, exclusions and expansion mode. List every extra or missing value explicitly. A draft named for one account can still contain other employers or only country targeting. Do not treat those additions as intentional, remove them from the evidence snapshot or silently reproduce them in the new build. Resolve the intended constraint in the proposed configuration, then read it back after saving.

## Rebuild CRM rules from their definitions

Inspect the actual CRM query or integration configuration when accessible. Capture contact versus company versus deal object, pipeline/product, association rules, lifecycle states, active versus static membership, time conditions, sync schedule and ownership. Identify how contacts inherit account status, what happens when a deal closes or reopens, and whether another product's customer status should suppress this motion.

Map the current company's definitions before building conversion or suppression rules:

| Event | Define explicitly |
|---|---|
| Form submission or registration | Deduplication, consent, valid contact and required metadata |
| Meeting booked | Booking versus attended, cancellation and no-show handling |
| Sales acceptance | Responsible owner, acceptance/rejection evidence and response deadline |
| Qualified opportunity | Actual qualification criteria and eligible CRM stages |
| Pipeline value | Product, currency, amount basis, attribution window and double-count controls |
| Won/lost/disqualified | Entry criteria, reason fields, effective date and audience consequences |

Never assume a stage called MQL is qualified pipeline, or that a selected conversion with the same label uses the current CRM definition. Stage probabilities are not automatically a forecasting or media-allocation model. Check definitions separately for each product and pipeline. Report missing acceptance, qualification or loss-reason data as a measurement limitation rather than manufacturing certainty.

## Validate the offer-to-sales path

Build a private dependency row per offer with: ad/post ID, form/event/page ID, destination and confirmation, asset version, field mapping, CRM object, deduplication, owner, expected follow-up, suppression update, test date and evidence.

For an ebook, test asset access and whether explicit sales interest changes routing. For a webinar, distinguish invited, registered, attended, no-show and cancelled. Confirm which system supplies each state; reconcile unique people and companies before calculating rates. Cross-listed event rows are not unique attendees, and aggregate company conversion should not use a person denominator.

For messaging, inspect every branch and terminal destination. A preview that cannot render a branch leaves that branch unverified. For TLAs, check actual post-specific sponsorship state and author control; a strategy note proposing a general permission is not evidence that a particular post is approved.

For historical Sponsored Messaging, recheck the current optimization goal, bid mode and billing basis before estimating costs or reusing a bid. Product updates can change optimization behavior while leaving billing unchanged. Preserve the saved state and current platform notice separately; do not derive cost per send, click, lead or conversion from a bid label alone.

Use supported test modes and authorized test identities. Inspect existing records read-only where a test would send a message or create an unintended production lead. Mark the path untested if appropriate test access is unavailable. Do not infer successful CRM delivery from a visible form, confirmation page or active conversion status.

## Give ABM handoffs an owner and a trigger

Before reconstructing a creative, check the format-specific path:

| Format | Additional readback |
|---|---|
| Carousel | Preserve card order, image, headline and each card destination. Compare each card's promise with its page. Check the main destination and attached form independently; never assume a change to the main URL updates the cards. |
| Text | Verify image, headline, description and whether the destination is a website or a LinkedIn Page. |
| Spotlight and Follower | Record background image, member-profile personalization, company image/name, optional description, CTA and destination where supported. Inspect the actual supported placement preview. A draft format selection without ads is not an implemented creative. |
| Article/newsletter | Identify the actual publishing Page/person, original post and article/newsletter destination. If the editor is blank, inspect the observed original-post link; keep unavailable editor controls marked as unverified. |
| Message/Conversation | Confirm available reporting fields before defining KPIs. A visible response button does not guarantee that its action is reportable. Preserve sent, opened, clicked and submitted counts with their actual denominators and attribution definitions. |



For each 1:1 or 1:few wave, identify the account brief, buying committee, role-specific value hypothesis, approved proof and sales owner before preparing media. Agree which signal causes an action, who receives it, the response target and how the outcome is recorded. Synchronize ads with outreach, introductions, events and procurement material where the plan requires it.

Keep proposed program gates separate from actual results. A planned webinar attendance target, future meeting or forecasted close is not an observed outcome. If committee coverage, a source list, a named introduction or a critical asset is missing, show the dependency and adapt the proposed launch sequence. Do not copy another company's week-by-week timetable or gate thresholds.

Close with a source map, a tested-handoff register and a remaining-dependencies list. Link these private records from the company's private operating brief, never from the public skill repository. Use [rebuild and handover](rebuild-and-handover.md) to report readiness and [launch and change](launch-and-change.md) to execute authorized changes.
