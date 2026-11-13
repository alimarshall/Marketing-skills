---
name: customer-proof-from-usage-reports
description: Turn a customer's product usage report (adoption, volume, deflection, actions, approvals) into reusable customer proof without overclaiming. Saves the figures exactly as worded with their window and definitions, labels derived maths, sets wording guardrails, flags consent, maps each stat to the persona or vertical it answers, and drafts slide, one-pager or case-study bullets. Use when someone pastes or links a usage report, QBR stats, "launch to date" numbers or a metrics export and says "save this", "what can we say with this", "make slides from these stats", "map this to each persona", "case study numbers", or "customer proof". Not for fact-checking finished copy or for propagating a corrected number.
---

# Customer proof from usage reports

A usage report is the strongest proof a B2B product has, and the easiest to damage. The numbers are real, so they get trusted, and then one rewrite turns "handled without a ticket" into "resolved automatically" and a sceptical buyer, or the customer, catches it. This skill keeps the numbers exactly as strong as the report and gets the most use out of them.

## Inputs

Fill in once:

- Where customer proof files are saved: `<fill in>`
- Persona / vertical reference (who the buyers are, what each cares about): `<fill in>`
- Capability baseline, including claims known to be incomplete or retired: `<fill in>`
- Consent or approval tracker for named-customer use: `<fill in>`

## Workflow

### 1. Capture the report verbatim
Save a dated file per customer per report: `<Customer>-Usage-Stats-<Mon-YYYY>.md`. Include:
- Reporting window, exactly as stated, including time zone and whether the end is exclusive.
- Link to the raw data.
- Every table, with labels as written.
- Every definition and footnote ("engagement follows the usage page definition", "counts include approved, processing, completed and failed"). These are what stop the overclaim later, so never drop them.
- Which metrics are separate measures and must not be added together (e.g. an actions table vs a deduplicated approvals count).

### 2. Derive, and label it
Add a "Derived numbers (my maths)" section: per-week or per-month rates, ratios (tickets per conversation, actions per conversation, share user-approved vs auto-approved), and the biggest single job by volume. Show the inputs for each. Never let a derived number travel without the label.

Cross-check derived rates against any earlier figure the customer gave on a call. If they line up, say so. If they don't, flag the gap and don't pick one.

### 3. Set the wording guardrails
For each headline metric, write the safe phrase and the upgrade to avoid:

| Report says | Safe in copy | Don't write |
|---|---|---|
| handled without creating a ticket | handled without a ticket | resolved, automated, deflected by AI |
| approved actions (incl. failed/processing) | approved actions | completed actions, tasks done |
| engaged (per a defined usage rule) | engaged | active daily, adopted |
| auto-approved | auto-approved | fully autonomous |

Also note anything sales will want to say that the report doesn't support (time saved, cost saved, FTE avoided) and name the missing input (minutes per request, loaded cost per FTE).

Check every claim against the capability baseline. If a stat implies a feature the baseline says is incomplete (an audit log, a compliance control), don't attach that implication.

### 4. Flag consent
Named-customer figures are internal until the customer signs off. Put that line at the top of every deliverable that uses them, and record in the approval tracker what has been requested and what is approved. Published case-study figures are the exception.

### 5. Map stats to the people who care
Each persona asks a different question of the same report. Default mapping:

- **Operator / champion** (runs the function day to day): volume handled, self-serve rate, the specific requests people bring, adoption, new-starter adoption.
- **Technical gatekeeper** (IT, security): the approval model (user-approved vs auto-approved), how escalation works, runs on the stack they already have, no new tool to roll out. Usually the weakest lens if the report has no IT-specific workflows. Say so internally.
- **Finance**: volume absorbed without adding headcount, approvals no longer stalling, scale across users. Cost maths only if the missing input exists.
- **Executive / transformation leader**: adoption at scale, the product doing work rather than only answering, one board-ready narrative.

Pick the 3-4 stats per persona that answer their question. Don't send every number to everyone.

### 6. Draft the outputs asked for
- **Slides**: default 3 per persona or vertical. Headline claim, 3-4 stat bullets, an optional speaker note for context or a missing input.
- **One-pager bullets**: attach the guardrail table.
- **Case study**: stat block plus the before-state from call evidence. Fact-check before anything leaves the building.

### 7. Save and link
Append drafted outputs to the same stats file under a dated heading, with the mapping logic. Add a pointer from the persona or vertical reference so "what proof do we have for X" finds it.

## Checks before handover

- Every number matches the report character for character, or is labelled derived.
- Every definition and caveat from the report is in the saved file.
- No phrase is stronger than the guardrail table allows.
- The consent line is on every deliverable with a customer name.
- Missing inputs for cost or time claims are named, not estimated.
