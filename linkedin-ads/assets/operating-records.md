# Private operating records and example prompts

Create these records only as needed in the current company's private workspace. Extend existing records rather than imposing duplicate trackers. Use real IDs and sources; unknown fields stay explicit.

## Audience register

One row per audience. For complex Boolean logic or many dependencies, use a linked detail record.

| Audience ID/name | Company/product | Purpose and motion | Company/contact/behavior/predictive | Source location/query/version | Source owner/date | Rows and cleaning notes | Status/match rate | Matched members as of | Final ad-set members as of | Include/exclude/seed dependencies | Threshold/window/source IDs | Refresh/expiry action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Record membership changes by ID/version and account; names are readable labels. Do not put raw email addresses in this register when a protected source pointer is sufficient.

## Campaign plan and persisted state

One row per ad set, with linked creative/form records as necessary:

| Account/parent/ad-set IDs | Name | Business motion | Objective/optimization | Format | Audience expression | Include IDs | Exclude IDs | Expansion mode | Placements | Budget/currency/parent limits | Dates/timezone | Bid | Ad/source-post/form IDs | Destination/tracking | Conversion IDs | Routing owner | Success/review condition | Persisted status/evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Lifecycle/exclusion matrix

| Cohort | Cold acquisition | Same-offer acquisition | Warm nurture | Pipeline support | Customer expansion | Source and refresh owner |
|---|---|---|---|---|---|---|
| Cold qualified companies/people | Include when in scope | Include when offer fits | Only after relevant qualification/behavior | Exclude until opportunity stage | Exclude | |
| Ebook submitters | Policy-dependent | Exclude from this ebook | Include relevant next steps | Only if opportunity exists | Only if customer | |
| Webinar registrants | Policy-dependent | Exclude from acquisition invitations | Reminders/related content | Stage-dependent | Customer policy-dependent | |
| Attendees/no-shows | Policy-dependent | Exclude obsolete invites | Different follow-up by real attendance | Stage-dependent | Customer policy-dependent | |
| Open opportunities | Exclude if separately funded | Sales-coordinated | Include or exclude deliberately | Include | Exclude unless expansion opportunity | |
| Customers | Exclude for new-logo motion | Depends on product/expansion purpose | Dedicated customer path | Separate expansion pipeline | Include if relevant | |
| Employees/irrelevant employers | Exclude | Exclude | Exclude | Exclude | Exclude | |

Adapt this policy to the company. Do not blindly apply account-wide customer suppression to a product expansion motion.

## Offer handoff record

| Offer ID | Product/buyer/problem | Approved asset/version | Format and form/event IDs | Destination/thank-you/delivery | Registration truth | Attendance truth | Required fields/metadata | CRM object/stage/owner | Suppression source | Follow-up action and owner | End-to-end test |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Change log

| Timestamp/timezone | Account/entity IDs | Reason and evidence | Authorized scope | Before → after | Shared dependencies | Verification | Rollback | Review date/outcome |
|---|---|---|---|---|---|---|---|---|

## Learning log

| Hypothesis | Audience/offer/creative versions | Variable tested | Spend ceiling and evidence window | Primary quality metric | Delivery diagnostics | Mature CRM outcomes | Uncertainty/confounders | Decision and next test |
|---|---|---|---|---|---|---|---|---|

## Example prompts

### Take over an existing account

> Read the linkedin-ads skill in this repository and our private company-context file. Audit the linked LinkedIn account read-only. Inventory audiences and campaign structure, inspect representative actual targeting settings, map sources through offers into CRM outcomes, and identify what is missing for an agency handover. Separate observed settings from names, old strategy documents and recommendations. Save the company-specific audit privately.

### Set up for a different company

> Use this repository's linkedin-ads skill for the company at [website], with [private company-context path]. Research our ICP and buying committee, use our CRM evidence, and propose the smallest useful launch structure within [budget, currency and period]. Build the audience/exclusion matrix and account-list criteria, map available offers, define measurement and list missing inputs. Prepare reviewable drafts and validated list exports. Keep company data private and state any access or launch steps still needed.

### Prepare an ABM list

> Use the linkedin-ads skill and the authorized master account list at [private location]. Build separate [tiers/clusters] from our fit rules and sales coverage. Preserve source evidence and corporate identities, validate against the current LinkedIn company CSV template, and produce upload files plus the private audience register. Show overlap/exclusion decisions and expected final persona/geography filtering. Do not upload until that action is within my authorized scope.

### Launch an ebook

> Use the linkedin-ads skill to prepare an ebook campaign for [buyer/problem] using [approved asset]. Decide cold versus warm targeting, objective/format and form versus website delivery within [budget]. Prepare the ads, form mapping, delivery, same-offer suppression, CRM owner and test plan. Show previews and a concrete launch checklist. Treat ebook capture and sales qualification as different milestones.

### Build a video TLA funnel

> Use the linkedin-ads skill with [eligible public post URLs] and our current ICP. Verify sponsorship permissions and format eligibility, prepare the paid audience, video-viewer source selections and an appropriate threshold/window. Plan relevant proof or learning content for the warm audience and a qualified evaluation path. Include how new posts/campaigns will be enrolled in the source audiences and how to handle pools below minimum size.

### Run a webinar program

> Use the linkedin-ads skill for [topic/date/timezone]. Build the necessary cold, warm and pipeline invitation audiences, registrant suppression and separate attendee/no-show follow-up. Identify registration and attendance truth, draft ads/forms and verify CRM handoff. Use [budget] and [approved assets]. Prepare the expiry/reschedule plan and keep native LinkedIn responses separate from external attendance.

### Review and recommend changes

> Use the linkedin-ads skill to review [account] for [period] against the comparable prior period and mature CRM cohorts. Inspect delivery, audience quality, source refresh, combined frequency, lead qualification and pipeline. Explain what we know and cannot yet infer. Return the few highest-impact recommendations with exact entity IDs, before/after settings, evidence, expected effect and rollback. This request is a review, not authorization for live changes.

### Execute a defined update

> Use the linkedin-ads skill. In [account], update only [named entities/IDs] from [current settings] to [specific settings], within [spend/date limits]. Read live state first, inspect shared audience dependencies, apply the smallest authorized change, read it back and update the private change log. Preserve unrelated settings and show any processing/review state accurately.

Reading a prompt here does not authorize its example action. Actual user instructions and the current environment determine execution permissions.
