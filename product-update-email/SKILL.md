---
name: product-update-email
description: Compile the recurring (usually monthly) customer product update email sent by a founder or CEO. Finds the last update sent, gathers everything shipped since from your release-notes channel, groups it into a few benefit-led sections plus an "Other improvements" list, and drafts a paste-ready .md file. Use when asked to draft, compile or put together the monthly product update, the customer product newsletter, the founder's customer update, the "what's new" email, or "the monthly update to customers". Checks coverage, avoids repeating the previous email and never announces anything that has not shipped. Pairs with claim-verification for any number or claim in the draft and copy-register-check for house style.
---

# Product Update Email

This skill compiles the recurring product update email that the sender (often a founder or CEO) sends to customers. The job is to find what has shipped since the last update, organise it the way the sender does, and produce a polished `.md` draft ready to paste into a doc or email tool.

## Why this skill exists

The update is a recurring piece of work with a fixed shape (same sender, same voice, same structure), but the content is determined by what shipped since the last one. That makes the work mechanical in some ways (find the last email, find what's new) and judgment-heavy in others (group features into sections, order by impact, write the prose). The skill encodes the mechanical parts so the attention goes into the writing.

## Inputs

Record these once (in `creative-strategy/references/inputs.md`, or here) so every run starts from the same places:

- **Sender name, title and email address:** `<fill in>`
- **Subject line pattern used so far:** `<fill in>` (for example "[Product] Product Update: ...")
- **Release-notes channel:** `<fill in>` (the Slack channel, changelog, or release-notes page where features are announced as they ship, plus its ID if your connector needs one)
- **Where the draft goes:** `<fill in>` (outputs folder, shared drive, etc.)
- **Sign-off block:** `<fill in>` (name, title, company, website)

The skill relies on two connectors:

- **Email** (for example a Gmail connector), to find the previous update email for the cutoff date and for tone and format calibration
- **Your release-notes channel** (for example a Slack connector), where shipped features are announced

Use them directly. If either is not connected, ask the user to paste the last email or the release notes rather than guessing.

## Step 1: Anchor on the last product update email

Search the sender's sent mail for the most recent product update:

- Query pattern: `from:<sender email> subject:"<subject line pattern>"`
- There will be duplicates (test sends, multiple recipient lists). Deduplicate by subject plus date and keep one copy per unique send.
- Fetch the **three most recent** unique updates. Read the most recent one in full. Skim the other two.

From the most recent email, extract:

1. The **send date**. Everything shipped after this is in scope for the new update.
2. The **tone and format**: how warm, how formal, which recurring constructions the sender uses ("We're excited...", "You can now...").
3. **What was already announced**, so nothing is repeated.

The two older emails are calibration material: read them to internalise how the sender structures sections, writes headings, opens and closes, and balances section depth. Do not copy phrases; match the voice.

## Step 2: Gather everything shipped since

Read every message in your release-notes channel posted **after the send date from Step 1**. Go through all of them; each post typically announces a shipped feature.

For each one, capture:

- Feature name
- What it does, framed as benefits (what the customer can now do, not the mechanics of how)
- Specifics worth mentioning: integrations touched, permission model changes, API scopes, plan availability, regions, and so on

Do not filter yet. Collect everything, then decide what is a headline feature and what is an "other improvement" in Step 3.

### Shipped means shipped

The release-notes channel mixes things that are live with things that are about to be. Only include a feature if it is **available to customers on the day the email goes out**. Treat these as out of scope unless someone confirms they are live:

- Posts saying something is "launching Monday", "rolling out next week", "coming soon" or "in beta for selected customers"
- Internal-only changes (tooling, refactors, admin features for your own staff)
- Features behind a flag that customers cannot turn on themselves

If a feature is partially rolled out (some regions, some plans), say so in the bullet or leave it for next month. When in doubt, ask the user rather than announcing it. An email that announces something customers then cannot find costs more trust than a missing bullet.

Likewise, do not invent numbers, customer names or outcomes that are not in the release posts. If a post includes a figure (speed improvement, adoption, time saved), check it with claim-verification or the person who posted it before it goes in.

## Step 3: Organise into sections

Group the collected features into **4 to 6 major sections** plus an **"Other improvements"** catch-all.

**Major sections** are either a single big feature or a thematic cluster (for example "A new documents experience" or "Workflows: more powerful than ever"). Each major section uses this exact shape:

```
**[Section heading]**

[IMAGE PLACEHOLDER: descriptive_name.png]

[1 to 2 sentence intro explaining the value to the reader.]

- **[Bold label]**; description of the specific capability;
- **[Bold label]**; another capability;
- **[Bold label]**; another capability;

[1 closing sentence reinforcing the benefit.]
```

**"Other improvements"** is a plain bullet list of smaller items that do not warrant their own section.

**Ordering:** lead with the biggest news. The first section should be the most exciting or impactful feature. Order the rest by how much customers will care, not chronologically.

## Step 4: Write the email

Use this structure, adjusted to whatever the calibration emails actually do:

```
Subject: [Subject line pattern]: [Top 3 to 4 features, comma-separated], and much more...

Hi {{first_name}},

[2 to 3 sentence intro summarising what's new. Energetic but not over the top; match the calibration emails. End with a short line that moves the reader on, such as "Read on."]

---

[Major feature section 1]

---

[Major feature section 2]

---

[... 4 to 6 sections total, separated by horizontal rules ...]

---

**Other improvements**

- Smaller item one;
- Smaller item two;
- Smaller item three;

---

[Closing line inviting feedback, e.g. "We hope you find these updates useful. If you have any feedback or challenges to share, reply to this email. We're here to help."]

[Sign-off block from Inputs]
```

If the previous emails use an emoji or other flourish in the subject line, keep it consistent; if they do not, do not add one.

## Voice and style

- **Founder voice.** Warm and direct, like the sender writing to customers they personally care about. Not corporate. Not hype.
- **Benefits over mechanics.** Lead with what the reader can now do. Keep technical detail for when it genuinely matters ("now supports SCIM provisioning" is worth saying; "refactored the notifications service" is not).
- **"We've..." and "You can now..."** constructions work well for this kind of email. Use whatever recurring constructions the calibration emails show.
- **Spelling convention.** Match the sender's (British or American) and keep it consistent throughout.
- **Bullet punctuation.** Match the calibration emails. A common house convention is that every bullet ends with a semicolon, including the last one. Whatever the convention, apply it to every bullet.
- **Quotes and dashes.** Match the punctuation conventions in previous emails (curly or straight quotes, dash style). Run copy-register-check if your house has register rules.
- **No jargon, no filler.** Cut "in order to", "leveraging", "seamlessly", "best-in-class", "revolutionise" and anything else on your house banned list.

## Step 5: Sanity check before saving

Before writing the file, pause and verify the draft against what you gathered. Drafting is generative and generative drafting drops things: a feature from the channel gets forgotten, the previous email gets echoed, a section's lead benefit drifts into a mechanic. A deliberate check catches this before the file lands.

Walk through each of these. If any fail, fix the draft, then re-check.

1. **Coverage.** List every feature you collected in Step 2. For each one, point to where it appears in the draft: a named section, a bullet within a section, or an "Other improvements" item. If any feature has no home, add it. If you deliberately excluded one (internal-only, not yet live, not customer-facing), note why. The default is that everything shipped gets mentioned somewhere.
2. **Shipped only.** For every item in the draft, confirm it is live for customers on the send date. Anything announced as upcoming, in limited beta, or flagged off comes out (or is clearly labelled, if the sender wants to tease it).
3. **No repetition from the previous email.** For each section and bullet, confirm the feature was not already announced in the most recent update. If it was, remove it.
4. **Subject and body alignment.** The 3 to 4 features named in the subject line must be the lead sections in the body, in the same order of prominence.
5. **Every major section has an image placeholder.** Count them. One per section, none in "Other improvements".
6. **Voice.** Spot-check spelling convention, bullet punctuation, quote and dash style, and banned words.
7. **Section count.** 4 to 6 major sections, not 8. If there are too many, the smaller ones collapse into "Other improvements".
8. **Claims.** Every number or outcome in the draft traces to a release post or a verified source.

Only once all eight pass: save the file.

## Output

Save the draft as a `.md` file to the outputs location from Inputs. Filename pattern: `product-update-YYYY-MM.md`, using the month of the send.

Image placeholders (`[IMAGE PLACEHOLDER: descriptive_name.png]`) stay as they are; they are cues for whoever pastes the draft into the doc or email tool to drop in the right screenshot.

After saving, present the file so the user can download it directly. Mention any items you excluded (and why) and any claims that still need checking.

## Success criteria

- Every customer-facing feature shipped after the last email's send date is covered somewhere in the draft.
- Nothing that has not shipped is announced as available.
- Nothing already announced in the previous email is repeated.
- Structure, headings and voice match the calibration emails.
- The `.md` is saved with the correct filename.
- Every major section has an image placeholder.
- The top 3 to 4 features in the subject line match the lead sections in the body.

## Things that commonly go wrong

- **Announcing things that have not shipped.** A "launching Monday" post in the channel is not a shipped feature. Check the status of anything announced near the send date.
- **Over-technical bullets.** If a bullet reads like a changelog entry, rewrite it as a customer benefit.
- **Too many sections.** If you have 8 or more major sections, some of them are really "other improvements". Be disciplined.
- **Repetition across sections.** If two sections both mention the same feature, merge them or move one to "Other improvements".
- **Marketing voice creep.** If a sentence sounds like it belongs on a landing page ("Revolutionise your workflow with..."), rewrite it as something a founder would actually write to a customer.
- **Missing the last email's cutoff.** Double-check the date. A week off either way means missing features or duplicating them.
- **Counting a test send as the last email.** Deduplicate and check the recipient list before trusting a date.
