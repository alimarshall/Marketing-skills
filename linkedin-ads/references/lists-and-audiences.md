# Lists and audiences

## Understand what each list means

| Object | Unit of membership | Typical purpose | Main failure |
|---|---|---|---|
| Company list | Matched employers and their eligible members | ABM, industry/technology clusters, pipeline support, exclusions | Wrong corporate entity or an unverified source label |
| Contact list | Matched people | Authorized CRM nurture, ebook/webinar registrants, attendee/no-show follow-up | Low matching and over-filtering |
| CRM company/contact audience | Company or person, depending on integration | Dynamic lifecycle inclusion/suppression | Broad or stale source rules; object type misunderstood |
| Retargeting audience | People satisfying a behavior in selected sources and time window | Nurture, objections, offer completion | New source campaigns omitted; thresholds too restrictive |
| Company-engagement segment | Companies meeting engagement criteria | Prioritize account-level plays | Mistaken for exact-person intent |
| Saved Audience | Reusable targeting configuration | Consistency across ad sets | Stale estimate or unexpected divergence from live ad-set settings |
| Predictive audience | Expanded prospects modeled from a seed | Reach expansion | Reported as if restricted to the original seed |

An event-company list reaches eligible employees of represented companies; it does not mean those employees attended. A competitor-customer list describes a claimed installed technology, not employment at the competitor. Record the source and observation date of that claim.

## Build a private source of truth

Keep the master list in an authorized CRM or private company workspace. Keep selection logic, source, date, owner, tier, evidence of fit, domain, canonical LinkedIn company URL and lifecycle state. A contact record additionally needs the relevant event/asset, registration/attendance state, permitted use and expiry/refresh policy. Store a pointer in the reusable repo, never the real rows.

Separate the master from the LinkedIn upload file. Internal research fields, tier, event notes and CRM IDs are not extra upload columns unless the current template explicitly supports them. Save the exact exported file/version and the matching result in the private audience register.

Deduplicate using a deliberate company identity (canonical Page URL and corporate entity; domain as supporting evidence) or contact identity. Inspect mergers, parent/subsidiary records, resellers and generic shared domains before collapsing them. Do not silently remove distinct entities sharing a parent domain.

## Upload procedure

1. Identify company versus contact upload and its business purpose. Resolve the destination account and authorized source.
2. Download the current template from Campaign Manager's audience creation flow. Preserve its headers; populate supported fields only. Use UTF-8 CSV, correct quoting and one entity per row. Do not assume a personal-profile URL is a supported contact identifier.
3. Check blank identities, duplicate rows, invalid/misaligned fields, hidden characters, placeholder values and file size. Use authorized personal/professional contact data; buying a tool does not establish permitted use.
4. Record source count and cleaning changes. Current UI guidance checked on 18 November 2026 requires at least 300 upload rows, at most 300,000 records and 20 MB for either list type. It also requires at least 300 matched member accounts for use in an active ad set. Verify these limits again before execution. LinkedIn's recommended volumes are larger than the minimum; they are not mandatory launch targets. [Company requirements](https://www.linkedin.com/help/lms/answer/a423102), [contact requirements](https://www.linkedin.com/help/lms/answer/a1489764).
5. Name the list by purpose, object type, market and source version. Upload via Plan → Audiences → Create audience → Matched Audience → Company / Contact (use equivalent current labels). Handle the agreement step under the environment's action-time rules. [Official upload flow](https://www.linkedin.com/help/lms/answer/a421822).
6. Verify status, match rate, matched/unmatched companies where available and final size. Allow up to 48 hours, occasionally longer; investigate after 72 hours using current troubleshooting guidance rather than repeatedly overwriting a Building list. Do not infer a match result immediately after upload.
7. Apply the correct audience ID in the intended inclusion or exclusion position, narrow as planned, inspect final eligible members and save/read back when authorized.

Do not fabricate rows to meet minimums. A 40-person webinar cohort may be useful for permitted CRM follow-up while being too small for standalone LinkedIn targeting. A small company set may be targeted through explicit Company selections if sufficient relevant members exist.

The UI accepts regular email addresses and hashes them locally, or accepts SHA-256 hashes in the email field. Direct API integrations have their own schemas, hashing and access requirements. Recheck the chosen route; do not copy API-only upload volume guidance into the UI workflow. Never print raw contact data in a public research artifact.

## Interpret status and counts correctly

`Building` and `Updating` describe processing. `Ready` describes completed processing. Eligibility also depends on audience size and the ad set's remaining restrictions. `Archived`/`Expired` audiences need the corresponding restoration or source refresh. Website signal recency is not proof that a demo-success event fires correctly. [Status definitions](https://www.linkedin.com/help/lms/answer/a795242).

Keep these quantities separate: uploaded rows; matched companies or contacts; total matched members; final eligible members; unique reached members; counted engagements/views; qualified leads. They have different units. Do not sum retargeting segment counts: the same member may be in several pools.

## Create behavior audiences

Record behavior, threshold, lookback, selected source IDs and receiving campaigns. Current choices vary by source and account; use the current UI. Common sources:

- Website visitors to relevant paths; requires the correct Insight Tag and applicable consent behavior.
- Video viewers at a selected completion threshold, such as 25%, 50%, 75% or 97%. Choose threshold relative to video duration and desired volume. Views are not unique matched people. [Video audience instructions](https://www.linkedin.com/help/lms/answer/a427086/).
- Single image ad interactions or chargeable clicks from selected ad sets. Do not assume every organic text post/profile visit becomes a retargeting source. Inspect eligibility for the actual TLA format. [Single image audience instructions](https://www.linkedin.com/help/lms/answer/a713230).
- Document engagement/download behavior, Lead Gen Form openers/submitters and conversation-ad engagement, each with explicit source sets and lookbacks.
- Company Page engagement and eligible LinkedIn Event responses/attendance states. External webinar attendance needs CRM/event-platform data; a LinkedIn event response does not establish external attendance. [Event audience instructions](https://www.linkedin.com/help/lms/answer/a421211/).

For a form-completion reminder, use openers MINUS submitters. For an attended-webinar follow-up, use the verified attendee cohort, not all registrants. Define the behavior audiences before launch when useful, then verify they build; confirm what historic activity the platform actually includes.

## Refresh without breaking dependencies

Before updating a source, list all campaigns that include or exclude it and any predictive audiences seeded from it. Determine whether the task needs an in-place membership refresh or a new version for a controlled test. Replacing source membership in place can change several live campaigns at once. Recheck the platform's current replacement/append behavior; do not assume a reupload only adds rows.

For a new version, create and validate it, record a before/after membership comparison, then migrate all intended inclusions AND exclusions. Leave the old segment available until dependencies are checked. For a dynamic CRM audience, change its source rules only within scope, inspect the sync state and sample membership, and read back the LinkedIn result. [Edit audiences](https://www.linkedin.com/help/linkedin/answer/a422548?lang=en-US).

Add new video/document/TLA campaigns to the relevant retargeting sources. Shared naming does not enroll new campaigns automatically. Verify website path changes and CRM lifecycle changes after launches. Proposed cadence: inspect suppression/sync health weekly, review ABM membership monthly and after meaningful sales/ICP changes, and update webinar states around each event. Adjust to the company's activity; this is an operating recommendation, not a platform requirement.

## Diagnose common failures

| Symptom | Investigate first | Useful action |
|---|---|---|
| High match rate, tiny final audience | Geography, titles, exclusions and size bands | Correct unnecessary narrowing; retain ICP constraints |
| Low company match | Page URLs, domains, parent/subsidiary identity, stale source | Correct identities and review unmatched entities |
| Low contact match | Format, permitted identifiers, source quality, work-email mismatch | Improve supported identifiers; don't promise a match rate |
| Warm pool below minimum | Source selection, recency, threshold, volume | Pool related behaviors with OR, broaden lookback if relevant, or wait |
| New campaign never feeds warm pool | Selected source IDs | Add the actual campaign where authorized and eligible |
| Campaign loses reach after refresh | Membership replacement and exclusion dependencies | Compare versions; restore the prior source when appropriate |
| Customer leakage | Static snapshot vs current customer system, company vs person suppression | Refresh the intended suppression object and verify application |

EEA/Swiss matching is affected by member choices. Do not diagnose limited regional matching as automatically broken tracking. [Matched Audience guidance](https://www.linkedin.com/help/lms/answer/a420552/).
