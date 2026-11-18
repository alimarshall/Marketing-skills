---
name: linkedin-ads
description: Research, set up, launch, review and update LinkedIn advertising for a company's ICP. Covers account audits, native targeting, company and contact lists, tiered ABM, retargeting, ebooks, webinars and Thought Leader Ads. Use for LinkedIn paid-media strategy and operations; organic-only post writing and creative production can use companion skills.
---

# LinkedIn ads

Act as the company's paid LinkedIn operator: turn company evidence into an audience system, connect offers to it, prepare campaigns, carry out authorized changes and learn from qualified commercial outcomes. Explain targeting in plain language when the user is learning.

## Establish the company and task

Read the current company's `company-context.md`, or its explicitly selected equivalent. This repository's root file is a reusable template; company-specific records belong in that company's private workspace. Never carry another employer's customer lists, target accounts, account IDs, creative permissions or performance assumptions into a new company.

Resolve product, ICP, buying committee, markets, account/Page, CRM, available offers, conversion definition, budget/currency and output location from supplied and connected sources. Ask only for missing decisions that affect the work; keep independent research moving. For a new company, use [assets/company-intake.yaml](assets/company-intake.yaml) as a compact intake. Blank inputs are unknown, not permission to invent a company fact.

Identify whether the task is read-only research, planning, draft preparation, list management, launch or an update. Read access does not imply authorization to upload contacts, accept agreements, spend money or change account access. Apply the current environment's authorization rules; make any required approval the final step after preparing a concrete reviewable result. Do not ask again for an action already adequately authorized unless the environment requires action-time confirmation.

## Select the relevant operating guide

| Work | Read |
|---|---|
| Reverse-engineer an existing account or take over from an agency | [Account audit](references/account-audit.md) |
| Define a new ICP, native targeting or ABM tiers | [Targeting and ABM](references/targeting-and-abm.md) |
| Prepare, upload, refresh or troubleshoot lists and retargeting | [Lists and audiences](references/lists-and-audiences.md) |
| Design ebooks, webinars, video or TLA funnels | [Funnels and offers](references/funnels-and-offers.md) |
| Prepare a new account/campaign, launch or change live settings | [Launch and change](references/launch-and-change.md) |
| Read results, diagnose delivery, allocate budget or optimize | [Measurement and optimization](references/measurement-and-optimization.md) |

Use [operating records and prompts](assets/operating-records.md) for practical handoffs, registers and example requests. Do not load every reference for a narrow task.

## Preserve the targeting logic

Represent every audience as a readable expression: `location AND account/firmographic fit AND person fit AND applicable behavior MINUS exclusions`. Use parentheses to distinguish OR pools from AND narrowing. A company list identifies employers; a contact list identifies people; engagement identifies behavior. None automatically proves buying intent.

Record both matched-list size and final eligible audience after all filters. Record included and excluded audience IDs, current source version, refresh date and downstream campaigns. A Ready list can still be too small; the active-ad-set count does not say whether a list is included or excluded. Read actual settings and selected controls. Names, suggested controls, forecasts and unchecked options are not configuration evidence.

For strict named-account delivery, verify the account list is a constraint rather than an AI expansion signal. Keep predictive/expansion prospecting separate unless the user deliberately chooses broader reach. Audience Expansion and Audience Network are different settings. A reusable Saved Audience is different from a Matched Audience's source membership.

## Work from live evidence

Discover the available LinkedIn connector before choosing an execution route. Another platform's Ads Manager is not a LinkedIn connector. If direct tools are insufficient, use an authorized Campaign Manager browser session or supplied exports. Do not imply the repository grants API access or can run unattended without a live authenticated connection.

For audits, preserve dates, status filters, account timezone/currency, pagination coverage and evidence links privately. Separate observed settings, historical documents, inferences and recommendations. For mutations, read current state, prepare a minimal change, execute within scope, then read back persisted settings. A click or submitted request alone does not prove success. Include a rollback action and any pending platform processing.

Verify changeable platform details against the live interface and current official LinkedIn Help. [Sources](references/sources.md) provides starting points and a checked-on date, not a permanent substitute for verification. Prefer the active Campaign Manager upload template over copied headers or outdated API requirements. Reconcile source conflicts and document material uncertainty.

## Fit into the marketing system

Use existing research and approved assets. If available, `brand-product-context` and `buyer-research-to-ads` supply product truth and buyer evidence; `abm-account-multithread` supplies named-account committee plans; `creative-strategy`, `ad-creative-direction` and `ad-library-review` own creative production/review; `tracking-audit-punch-list`, `creative-testing` and CRM attribution skills supply their respective checks. These are optional collaborators, not tool or installation requirements. Complete the relevant work inline when they are unavailable.

Keep the public skill company-neutral. Keep raw contacts, employer-specific account inventories, unpublished results, CRM exports and credentials in the company's private systems. Store references and schemas in the reusable repo, not actual audience membership.

## Finish with an operational outcome

Deliver the requested audit, audience plan, validated upload files, reviewable campaign draft, verified launch or verified update. State what was observed or changed, what remains unverified, and the next decision only when one is actually needed. For learners, explain what the audience means and why the next offer fits it. Do not describe campaign architecture as proven profitable without qualified CRM outcomes or claim every buyer follows a linear funnel.
