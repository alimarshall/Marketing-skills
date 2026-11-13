---
name: "deal-source-verification"
description: "Check whether CRM deals tagged to a channel (events, paid, partner) really came from it, by reading the emails, notes and call summaries behind each deal; give each a verdict with dated quotes, recompute the channel numbers (confirmed, probable, unclear) and list the tags to fix. Use for \"was this deal actually from an event\", \"check the other events deals in the pipeline\", \"is this really a LinkedIn deal\", or before presenting channel pipeline or ROI that rests on a few large deals."
---

# Deal source verification

Rep-set source fields are often wrong. An event invite used as an outreach opener gets tagged "Events". An inbound demo request gets tagged to whoever followed up. This checks the activity trail behind each deal and gives a verdict.

## Inputs

- CRM and the deals or channel to check: `<fill in>`
- The counting rule for the channel (agree it before checking, see step 1): `<fill in>`
- Where activity lives (CRM emails, notes, meetings, call recording summaries): `<fill in>`

## Workflow

### 1. Agree the rule first
Write it down before checking anything. Example for events:
- Counts: someone from the prospect attended or met the team at the event (booth, dinner, breakfast, conference) and that conversation led to the deal.
- Does not count: the invite was only the opener and they didn't attend (declined but took a 1:1), or the deal came from a separate inbound request.

The user may override single verdicts (e.g. "registered then cancelled can stay"). Record overrides and apply them consistently.

### 2. Check each deal
1. Read the deal: source fields, create date, stage, amount, owner.
2. Find associated contacts. Read their source fields, first conversion form and how the record was created (import, integration, form).
3. Read emails, notes and meetings on the deal and its contacts from before and around the create date. Request only the properties you need, small limits, and full text only for threads that matter: first replies, "great to meet you at", "thanks for coming", attendance replies, RFP requests.
4. Call recording summaries in meeting records often say how the conversation started.
5. Watch for misleading signals: automated "missed you at" sequences, invites sent to a different person at the same company, nurture touches sent after the deal already existed.

For many deals, split them across parallel subagents with the same rule and output format.

### 3. Give a verdict per deal
- Verified / Probably / Unclear / Not from this channel
- What it actually was: founder outbound, SDR outbound, inbound demo request, partner intro, existing relationship
- Which event or campaign, with date
- One or two short verbatim quotes with dates, copied from the source
- For Unclear: the one question to ask the rep

### 4. Recompute
Rebuild the channel numbers three ways: confirmed only, plus probable, plus unclear. Show period-over-period and YoY for each. Say that earlier periods are unaudited unless they were checked the same way.

### 5. List the fixes
Which CRM tags should change and to what. Don't edit records unless the user approves each change.

## Output

Short block per deal (verdict, what it was, evidence), a recomputed table, the tag fixes, and a deck line using confirmed numbers only. Plain language, no em dashes. Quotes are internal evidence; don't use them externally without consent.

## Works with

- `crm-channel-attribution-review` produces the channel numbers this checks.
- `paid-media-roi-and-cac` uses the confirmed pipeline for return on spend.
