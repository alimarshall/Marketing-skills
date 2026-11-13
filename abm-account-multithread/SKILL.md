---
name: abm-account-multithread
description: Build a multithreaded ABM plan for one named target account. Pulls the account's CRM record, past calls and public signals (hiring, funding, leadership changes, tech stack), maps the real buying committee by name and role, gives each person a distinct reason to care, a proof point and an opening line, and sets the order to approach them. Use when someone says "multithread [account]", "ABM plan for [account]", "who should we talk to at [account]", "map the buying committee", "account plan", "we're single-threaded on [deal]", or "how do we get to the CFO/CISO at [account]". For vertical or industry-level persona maps (no named account), use vertical-persona-research. Not for writing the full outbound sequence copy itself.
---

# ABM account multithreading

Single-threaded deals die when the one contact goes quiet, loses the budget fight or leaves. Multithreading means each person in the buying group has their own reason to care, hears it in their own terms, and gets it from a channel and moment that suits them. The most common failure is sending the champion's pitch to the CFO with a different subject line. This skill stops that.

## Inputs

- CRM (account, contacts, deals, activity, owner): `<fill in>`
- Call recording platform: `<fill in>`
- Persona / vertical reference (from `vertical-persona-research`): `<fill in>`
- Customer proof files, with consent status: `<fill in>`
- Capability baseline: `<fill in>`
- Enrichment or people-data source, if any: `<fill in>`

## Workflow

### 1. Pull what we already know
- **CRM**: account record, every associated contact (title, last activity, owner), open and closed deals with stage history and loss reasons, recent emails and meetings.
- **Calls**: match by participant email domain, not by call title. List every call, who attended, and per person: what they cared about, objections, verbatim quotes with date.
- **Existing research**: if the account's industry already has a section in the vertical reference, start from it.

Write down who has engaged, who hasn't, and who has gone quiet.

### 2. Pull public signals
Two or three sources per signal, with link and date. Mark each verified or unverified.
- Hiring: open roles in the functions the product serves, and roles that signal a buying trigger (a new Head of X, a systems role).
- Funding, M&A, restructuring, new geographies.
- Leadership changes in the last 12 months.
- Tech stack signals relevant to integration or displacement.
- Public statements by the people on the committee (posts, talks, interviews). Professional and public only. Anything about personality or style is an inference, so label it.

### 3. Map the buying committee
One row per real person where known. Use a role placeholder where the seat is unfilled or unknown, and mark it as a gap to fill.

| Name | Title | Role in deal | Status | What they care about | Frustration to open on | Proof / stat | Opening angle | Channel |
|---|---|---|---|---|---|---|---|---|
| | | Champion | engaged / quiet / unknown | | | | | |
| | | Economic buyer | | | | | | |
| | | Technical gatekeeper | | | | | | |
| | | Finance approver | | | | | | |
| | | Influencer / end-user lead | | | | | | |

Rules:
- **Each person gets a different "why care".** If two rows have the same opening angle, rewrite one.
- **Ground every row** in that person's own words, their function's known priorities from the vertical reference, or a public signal. Never invent a priority.
- **Proof must fit the person.** Gatekeepers get approval and control evidence. Finance gets capacity and cost evidence. Use named-customer stats only where consent exists; otherwise use them internally to shape the angle.
- **Only reference capabilities that are in the baseline.**

### 4. Sequence the threads
- Who first, and why (usually the warmest engaged contact, or the person whose pain is most visible in public signals).
- What the champion needs to sell internally: one forwardable asset per stakeholder they'll face.
- Which objection each stakeholder will raise, and who on our side answers it (AE, SE, exec sponsor, a reference customer).
- Exec-to-exec moves: where a peer-level contact from our side is worth more than another rep email.
- Triggers that should change the plan: champion silence past a set number of days, a new hire in a key seat, a funding round.

### 5. Draft the openers
One short opener per thread: the hook built from their frustration or signal, the single proof point, and one low-commitment ask. Different structure per person, not the same template with names swapped. Hand longer sequences to an outbound or email skill.

### 6. Save it
One file per account: `ABM-<Account>-<YYYY-MM-DD>.md` with signals (sourced and dated), the committee map, sequencing, openers, and an "unknowns to fill" list. Write new contacts or roles back to the CRM only with the user's go-ahead.

## Checks before handover

- Every person, signal and quote has a source and date.
- No two threads share an opening angle.
- Named customer proof is used only with consent, or marked internal.
- Every capability mentioned is in the baseline.
- Gaps in the committee are listed, not filled with guesses.
