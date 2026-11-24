---
name: product-update-email
description: Compile the recurring (usually monthly) customer product update email sent by a founder or CEO. Finds the last update sent, gathers everything shipped since from your release-notes channel, groups it into a few benefit-led sections plus an "Other improvements" list, and drafts a paste-ready .md file in a clear, understated founder voice. Use when asked to draft, compile or put together the monthly product update, the customer product newsletter, the founder's customer update, the "what's new" email, or "the monthly update to customers". Checks coverage, avoids repeating the previous email (including its opening), flags any research source it could not reach and never announces anything that has not shipped. Pairs with claim-verification for any number or claim in the draft and copy-register-check for house style.
---

# Product Update Email

This skill compiles the recurring product update email that the sender (often a founder or CEO) sends to customers. The job is to find what has shipped since the last update, organise it the way the sender does, and produce a polished `.md` draft ready to paste into a doc or email tool.

## Why this skill exists

The update is a recurring piece of work with a fixed shape (same sender, same voice, same structure), but the content is determined by what shipped since the last one. That makes the work mechanical in some ways (find the last email, find what's new) and judgment-heavy in others (group features into sections, order by impact, write the prose). The skill encodes the mechanical parts so the attention goes into the writing.

## Inputs

Read `company-context.md` first (repo root, or search the workspace for it) and use the fields that apply to this skill. If the file or a line is missing, ask once, then offer to save the answer back to it. Never fill a gap with an assumption about the company. If `creative-strategy/references/inputs.md` is also filled in, it still applies; where the two differ, `company-context.md` wins.

Record these once (in `creative-strategy/references/inputs.md`, or here) so every run starts from the same places:

- **Sender name, title and email address:** `<fill in>`
- **Subject line pattern used so far:** `<fill in>` (for example "[Product] Product Update: ...")
- **Release-notes channel:** `<fill in>` (the Slack channel, changelog, or release-notes page where features are announced as they ship, plus its ID if your connector needs one)
- **Archive of past sends:** `<fill in>` (optional: a shared doc or folder where each month's final email is kept, useful when the email connector is not available)
- **Where the draft goes:** `<fill in>` (outputs folder, shared drive, etc.)
- **Sign-off block:** `<fill in>` (name, title, company, website)

The skill relies on two connectors:

- **Email** (for example a Gmail connector), to find the previous update email for the cutoff date and for tone and format calibration
- **Your release-notes channel** (for example a Slack connector), where shipped features are announced

Use them directly. If the email connector is not available, use the archive of past sends. If neither is reachable, or the release-notes channel is not connected, ask the user to paste the last email or the release notes rather than guessing.

### Say which sources you could not reach

Keep a short list of every source you tried and whether you could read it: the email connector, the archive, the release-notes channel, any threads or linked docs a release post points to. When a source is unavailable, say so plainly in your handover ("I couldn't open the email connector, so the cutoff comes from the archive doc, which may not match the actual send date"). Never describe the draft as fully verified when part of the research was out of reach.

## Step 1: Anchor on the last product update email

Search the sender's sent mail for the most recent product update:

- Query pattern: `from:<sender email> subject:"<subject line pattern>"`
- There will be duplicates (test sends, multiple recipient lists). Deduplicate by subject plus date and keep one copy per unique send.
- Fetch the **three most recent** unique updates. Read the most recent one in full. Skim the other two.

If you are working from the archive instead, take the three most recent sent emails from it, and treat drafts or alternative versions in the archive as unsent unless the user confirms otherwise.

From the most recent email, extract:

1. The **send date**. Everything shipped after this is in scope for the new update.
2. The **tone and format**: how warm, how formal, which recurring constructions the sender uses ("We've...", "You can now...").
3. **What was already announced**, so nothing is repeated.

From all three, put the **introductions side by side**. Note how each one opens, what its first sentence does, and any phrases or sentence shapes they share ("This month, we've...", "We've had a big few weeks"). The new introduction must open differently from all three.

The two older emails are calibration material: read them to internalise how the sender structures sections, writes headings, opens and closes, and balances section depth. Do not copy phrases; match the voice.

## Step 2: Gather everything shipped since

Read every message in your release-notes channel posted **after the send date from Step 1**. Go through all of them; each post typically announces a shipped feature. Open the threads under each post too: availability, plan limits, permissions and corrections often sit in the replies.

For each one, capture:

- Feature name
- What it does, framed as benefits (what the customer can now do, not the mechanics of how)
- Specifics worth mentioning: integrations touched, permission model changes, API scopes, plan or add-on availability, regions, where to switch it on in settings, and so on

Do not filter yet. Collect everything, then decide what is a headline feature and what is an "other improvement" in Step 3.

### Shipped means shipped

The release-notes channel mixes things that are live with things that are about to be. Only include a feature if it is **available to customers on the day the email goes out**. Treat these as out of scope unless someone confirms they are live:

- Posts saying something is "launching Monday", "rolling out next week", "coming soon", "later today" or "in beta for selected customers"
- Internal-only changes (tooling, refactors, admin features for your own staff)
- Features behind a flag that customers cannot turn on themselves

If a feature is partially rolled out (some regions, some plans), say so in the bullet or leave it for next month. When in doubt, ask the user rather than announcing it. An email that announces something customers then cannot find costs more trust than a missing bullet.

If a feature has already had its own dedicated announcement email, ask the user whether to give it a full section, shorten it to a line, or leave it out.

Likewise, do not invent numbers, customer names or outcomes that are not in the release posts. If a post includes a figure (speed improvement, adoption, time saved), check it with claim-verification or the person who posted it before it goes in.

## Step 3: Organise into sections

Group the collected features into **4 to 6 major sections** plus an **"Other improvements"** catch-all. In a light month with only a few small launches, fewer sections is better than padding; say so in your handover.

**Major sections** are either a single big feature or a thematic cluster. Each major section uses this shape:

```
**[Section heading]**

[IMAGE PLACEHOLDER: descriptive_name.png]

[1 to 2 sentence intro: what customers can now achieve, and what it opens up.]

- **[Short label]:** specific capability, with the detail that matters;
- **[Short label]:** another capability;
- **[Short label]:** another capability;

[Availability, permissions or setup line, if the feature needs one.]

[Optional: 1 closing sentence, only if it adds something the intro and bullets have not said.]
```

**"Other improvements"** is a plain bullet list of smaller items that do not warrant their own section.

**Ordering:** lead with the biggest news. The first section should be the most significant or impactful feature. Order the rest by how much customers will care, not chronologically.

## Step 4: Write the email

Use this structure, adjusted to whatever the calibration emails actually do:

```
Subject: [Subject line pattern]: [Top 3 to 4 features, comma-separated], and much more...

Hi {{first_name}},

[2 to 3 sentence introduction. A fresh narrative about where the product is going this month, built from what shipped and different from the last three openings. End with a short line that moves the reader on, such as "Read on."]

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

### The introduction

- Read the three introductions you compared in Step 1 before writing. Do not reuse their first words, their sentence shapes or their framing.
- Tell a short story about the month: what customers can now do that they could not before, and where that takes them. Name the lead feature, then summarise the rest by product area.
- Do not list every feature. The introduction sets up the email; the sections do the announcing.

### Headings

- Make each heading specific and benefit-led: it should tell the reader what they gain, in the product's own terms.
- Use "Introducing [Feature]" only for a genuinely new product or module, not for an extension of something that already exists.
- Balance product clarity with customer ambition. A reader should know which part of the product the section covers and why it matters to them.
- No slogans, puns or clever wordplay.

### Section intros

- One or two sentences. Say what customers can now achieve and what it opens up for them: deeper understanding, better use of the data they already hold, new things they can build or automate.
- When the heading already introduces the feature, do not announce it again. Move straight to what it makes possible.

### Bullets

- Every bullet starts with a short, descriptive bold label followed by a colon (two to four words, such as "Dynamic task assignments:").
- After the label, describe the capability specifically: what it does, where it works and any limit worth knowing.
- Keep the bullet punctuation convention from the calibration emails (for example a semicolon at the end of every bullet, including the last) and apply it to every bullet.
- Do not repeat in a bullet what the label, heading or intro already said.

### Product detail to keep

Simple does not mean vague. Keep the details customers need to use the feature or to know whether it applies to them:

- Plan, add-on or region availability
- Who can see or manage it (permissions, roles)
- Where to switch it on or configure it
- What happens to existing data or settings
- Anything that is off by default or needs the customer to ask for it

Put these in a bullet or a plain line after the bullets. Never cut them to make a section shorter.

### Closing sentences

A section does not need a closing line. Add one only when it says something new, such as what the change sets up next. Drop any closer that restates the bullets or reaches for a summary.

## Voice and style

- **Founder voice.** A confident, thoughtful founder writing directly to customers: simple, clear, elevated and natural. Mature, understated and approachable. Elevated does not mean elaborate. Not corporate, not hype.
- **Progress and possibility.** Show how customers can go further, do more, deepen their understanding and make better use of the data they already have. Avoid generic efficiency messaging ("save time", "less admin") unless the time saved is the actual point and it is specific.
- **Benefits over mechanics, without losing accuracy.** Lead with what the reader can now do. Keep technical detail for when it genuinely matters ("now supports SCIM provisioning" is worth saying; "refactored the notifications service" is not). Never sacrifice product accuracy for simplicity.
- **"We've..." and "You can now..."** constructions work well for this kind of email. Use whatever recurring constructions the calibration emails show, and vary them so consecutive sentences do not start the same way.
- **Spelling convention.** Match the sender's (British or American) and keep it consistent throughout.
- **Bullet punctuation.** Match the calibration emails. A common house convention is that every bullet ends with a semicolon, including the last one. Whatever the convention, apply it to every bullet.
- **Quotes.** Match the quote style in previous emails (curly or straight). Run copy-register-check if your house has register rules.
- **No em dashes.** Never use them, whatever the previous emails did. Use a comma, colon, full stop or parentheses instead, chosen to fit the sentence.
- **No jargon, no filler.** Cut "in order to", "leveraging", "seamlessly", "best-in-class", "revolutionise", "game-changing", "powerful" as a stock adjective, and anything else on your house banned list.
- **No forced enthusiasm.** Cut exclamation marks outside the sign-off, "exciting", "thrilled" and marketing slogans.
- **No unnecessary adjectives.** If an adjective does not change the meaning, remove it.
- **Read it as one piece.** Before finalising, read the entire email from subject line to sign-off as one continuous piece of writing, not as a set of separately written sections. Fix repeated words, repeated sentence shapes and any point made twice.

## Editorial calibration

These examples show the intended style. They are patterns to adapt to the company and product in question, not text to reuse.

**Opening style:**

> "We're continuing to expand what's possible with [Product]. With the introduction of [Feature], you can now build a richer picture of your workforce, connect your job framework to everyday operations, and go deeper with your reporting. Alongside this, we've introduced new capabilities across [Product areas]. Read on."

This shows the tone, not a reusable opening. Find a fresh narrative every month based on what has shipped and what previous emails have already said.

**Headings** that balance product clarity with customer ambition:

- Introducing [Major new feature]
- Better understand employee turnover
- Dive deeper into reports with [AI assistant]
- More flexible Workflows, powered by your people data

**Section opening:**

> "Bring structure and consistency to how you manage roles across your organisation. With [Feature], your job framework becomes part of your people data, opening up new possibilities for workforce planning, reporting and automation."

When the heading already introduces the feature, the body moves on to what it makes possible instead of announcing it again.

**Bullets:**

- **Dynamic task assignments:** Assign tasks to someone's People partner, skip-level manager or any other relationship field;
- **More precise rules:** Combine multiple conditions within a single relationship rule, such as contract type and place of work;

Write with this level of specificity.

**Overall direction:** communicate progress, possibility and customer ambition. Avoid generic efficiency messaging, forced enthusiasm, repetitive sentence structures, unnecessary adjectives, marketing slogans and formulaic section endings.

## Step 5: Sanity check before saving

Before writing the file, pause and verify the draft against what you gathered. Drafting is generative and generative drafting drops things: a feature from the channel gets forgotten, the previous email gets echoed, a section's lead benefit drifts into a mechanic. A deliberate check catches this before the file lands.

Walk through each of these. If any fail, fix the draft, then re-check.

1. **Coverage.** List every feature you collected in Step 2. For each one, point to where it appears in the draft: a named section, a bullet within a section, or an "Other improvements" item. If any feature has no home, add it. If you deliberately excluded one (internal-only, not yet live, not customer-facing, already had its own email), note why. The default is that everything shipped gets mentioned somewhere.
2. **Shipped only.** For every item in the draft, confirm it is live for customers on the send date. Anything announced as upcoming, in limited beta, or flagged off comes out (or is clearly labelled, if the sender wants to tease it).
3. **No repetition from the previous email.** For each section and bullet, confirm the feature was not already announced in the most recent update. If it was, remove it.
4. **Fresh opening.** Compare the new introduction with the last three. If it shares an opening phrase, sentence shape or framing with any of them, rewrite it.
5. **No repetition within the email.** Check that the introduction, headings, section intros and bullets do not announce the same thing twice. Each layer should add something.
6. **Subject and body alignment.** The 3 to 4 features named in the subject line must be the lead sections in the body, in the same order of prominence.
7. **Every major section has an image placeholder.** Count them. One per section, none in "Other improvements".
8. **Product details kept.** Every section that needs one states its availability, permissions and setup steps.
9. **Voice.** Spot-check spelling convention, bullet labels and punctuation, quote style and banned words. Search the draft for em dashes; there must be none. Cut any section closer that repeats the bullets.
10. **Section count.** 4 to 6 major sections, not 8. If there are too many, the smaller ones collapse into "Other improvements".
11. **Claims.** Every number or outcome in the draft traces to a release post or a verified source.
12. **Sources.** Your list of sources says which ones you read and which you could not reach.

Then read the whole email once more as a single piece of writing. Only once all twelve pass: save the file.

## Output

Save the draft as a `.md` file to the outputs location from Inputs. Filename pattern: `product-update-YYYY-MM.md`, using the month of the send.

Image placeholders (`[IMAGE PLACEHOLDER: descriptive_name.png]`) stay as they are; they are cues for whoever pastes the draft into the doc or email tool to drop in the right screenshot.

After saving, present the file so the user can download it directly. Mention any items you excluded (and why), any claims that still need checking, and any research source you could not reach.

## Success criteria

- Every customer-facing feature shipped after the last email's send date is covered somewhere in the draft.
- Nothing that has not shipped is announced as available.
- Nothing already announced in the previous email is repeated.
- The introduction opens differently from the last three.
- No feature is announced twice across the introduction, headings and body.
- Structure, headings and voice match the calibration emails and the editorial calibration above.
- Availability, permissions and setup details are kept wherever they apply.
- The draft contains no em dashes.
- The `.md` is saved with the correct filename.
- Every major section has an image placeholder.
- The top 3 to 4 features in the subject line match the lead sections in the body.
- Any research source that could not be reached is named in the handover.

## Things that commonly go wrong

- **Announcing things that have not shipped.** A "launching Monday" post in the channel is not a shipped feature. Check the status of anything announced near the send date.
- **Over-technical bullets.** If a bullet reads like a changelog entry, rewrite it as a customer benefit.
- **Oversimplified bullets.** The opposite failure: a bullet so general it loses the product detail. Keep the specifics that make it accurate.
- **Too many sections.** If you have 8 or more major sections, some of them are really "other improvements". Be disciplined.
- **Repetition across sections.** If two sections both mention the same feature, merge them or move one to "Other improvements".
- **Saying it three times.** The introduction names a feature, the heading names it again and the section intro announces it a third time. Let each layer do a different job.
- **The same opening every month.** "This month, we've..." three months running. Compare against the last three introductions every time.
- **Formulaic section endings.** A closing line on every section that restates the bullets. Cut it.
- **Marketing voice creep.** If a sentence sounds like it belongs on a landing page ("Revolutionise your workflow with..."), rewrite it as something a founder would actually write to a customer.
- **Em dashes.** They slip in during drafting. Search for them before saving.
- **Claiming full verification.** If the email connector or a linked doc was unavailable, say so. Do not imply every source was checked.
- **Missing the last email's cutoff.** Double-check the date. A week off either way means missing features or duplicating them.
- **Counting a test send as the last email.** Deduplicate and check the recipient list before trusting a date.
