---
name: ad-avatars
description: "Build a new ad avatar, or refresh an existing ad avatar library, for B2B SaaS paid creative. Two modes: BUILD creates an avatar from buyer research, REFRESH folds new evidence into avatars that already exist. Use when the user asks to build, create, add, update, refresh, review or retire an ad avatar or the avatar library. Triggers on 'build an avatar for the economic buyer', 'refresh the avatars', 'update the avatar library after the research sweep', 'we have customer sign-off now', 'a test contradicted an avatar', 'add the founder seat', 'are the avatars still current', 'retire that avatar'. Also use to promote an avatar a campaign invented on the fly into the standing library. Pain-first, evidence-only, consent-tagged, additive: the library grows by dated entry and is never rewritten. Use the creative-strategy skill instead when the job is a campaign, angles, concepts or a brief and the avatars are only an input. Use ICP and persona work for company-level targeting, which is a different object."
---

# Ad avatars: build and refresh

An ad avatar exists to settle one decision: **what argument, in whose words, to a person in a specific state of knowing, scrolling a feed.** It is narrower and more behavioural than the things it gets confused with.

| Artefact | Answers |
|---|---|
| **ICP** | Which companies to sell to at all |
| **Sales persona** | Who is in the room, across a whole cycle |
| **Ad avatar** | Which line to write, and which lines backfire |

A sales persona that says "cares about compliance" is fine for a call plan and useless for a hook. It does not tell you what the person would say out loud.

**Where things live.** The avatar library, the pain bank and the buyer research this skill reads are all named in the companion `creative-strategy` skill's `references/inputs.md`. Fill that in once and both skills work. If it is not filled in, ask for the paths rather than guessing.

## Inputs

Read `company-context.md` first (repo root, or search the workspace for it) and use the fields that apply to this skill. If the file or a line is missing, ask once, then offer to save the answer back to it. Never fill a gap with an assumption about the company. If `creative-strategy/references/inputs.md` is also filled in, it still applies; where the two differ, `company-context.md` wins.

## Step 0: Which mode

Say which in one line, then proceed.

- **BUILD** if the avatar or the territory does not exist yet. A new committee seat, a new segment, a new product line, or promoting an avatar a campaign invented on the fly.
- **REFRESH** if the avatar exists and something changed. See Step 5 for the trigger list.
- **REVIEW** if nobody has asked for a change and the question is whether the library is still current. Read the gaps section and the evidence tiers, report, and change nothing without saying what and why.

If the request is a campaign, angle set, concept set or brief, this is the wrong skill. Hand to `creative-strategy`, which reads this library as an input.

## Step 1: Read, to the job

A mature avatar library runs to tens of thousands of words. Do not read it whole for a single-avatar job.

| Job | Read |
|---|---|
| Any job | The territory index and the coverage-and-gaps section |
| BUILD | Plus the two nearest existing avatars in full, so the new one is genuinely distinct |
| REFRESH | Plus the target avatar in full, and its rows in the pain bank |
| REVIEW | The index, the gaps, and every avatar's evidence tier line only |

Grep by avatar ID rather than reading sequentially. Stable IDs are what make a large library cheap to use.

**Ground truth, and only what the job needs.** Paths in `inputs.md`.

| Field you are filling | Source |
|---|---|
| Pain, how experienced, verbatim | Buyer pain research, voice-of-customer verbatims, the pain bank |
| Deepest want | Buyer aspiration research |
| Objections | Competitor dossiers, deal-intelligence sections; verification tracker gap rows |
| Triggers | The pain bank's trigger bucket; ranked pain themes |
| Committee seat, firmographics | The ICP and persona documents |
| Fresh material | Recent call notes, digests, or a research sweep |

Always read your voice and writing rules. They outrank anything here.

## Step 2: Pain-first, not persona-first

Invert the usual order.

1. **Name the pain or desire territory the research actually evidences.** Not the ones the product addresses. The ones buyers describe unprompted.
2. **Map which avatars hold it, and how each experiences it differently.** Personas are secondary: they are different working contexts feeling the same pain.

Many-to-many. Every pain by avatar cell is a distinct creative opportunity, because the same pain argued to a different seat is a different argument. A persona-first list produces demographic messaging, and demographic messaging is vague. A category statement names a market; an argument names a moment the person recognises.

Default to pain-first. Desire-first is the exception, for a claim with no acute functional problem behind it. Note which anchor an avatar is built on, because it changes what the hook is allowed to open with.

## Step 3: The eleven fields

In this order. An avatar is not finished until each is filled or explicitly marked unevidenced. Use consistent bold labels so the file stays greppable.

1. **Avatar label** plus a one-line working context. A name that travels: something a person recognises across three meetings, rather than a code. The label should describe the situation the person is in, not their job title.
2. **Who this is in targeting terms.** Job function, seniority, title patterns, company size in the ad platform's own bands, geography, industry. **State explicitly where a field is not selectable in the ad platform**, and name the workaround. This is where avatar work quietly fails: the most predictive attribute is often the one you cannot buy. The system a buyer already runs is frequently the single best predictor and is rarely targetable natively; the workaround is an install-base list uploaded as a matched audience.
3. **Role in the buying committee.** Champion, economic buyer, technical gatekeeper, blocker, end user.
4. **The pain they own**, with territory references, and **how this avatar experiences it differently** from the others holding it. The second half is the field that earns its keep.
5. **Deepest want**, in their terms rather than yours.
6. **What they will doubt, most likely first.**
7. **Trigger moment**, and whether it is targetable.
8. **Likely awareness states**, and in which audience. Usually problem-aware cold and product-aware in retargeting, which are two different ads.
9. **Verbatim language.** Two to five exact quotes, each with its source and consent tag.
10. **What NOT to say to them.** The framings that fall flat. Almost nobody keeps this field and it is what stops a retired framing returning in six months. Say where each entry came from: a buyer-stated rejection, a register rule, or measured creative failure. The third is the strongest and the rarest, because it requires performance history.
11. **Evidence tier**, with the account count stated. High = multiple named accounts, recent, verbatim. Medium = one or two accounts, or paraphrased in a synthesis document. Low = pattern-level or unattributed.

## Step 4: The three rules that make it worth reading

**Never invent.** Every pain, quote, objection and trigger traces to a named source, cited inline. No source means `No evidence found in current research` and move on. A thin avatar with real evidence beats a rich invented one, and the empty fields are what the next research pass is for.

**Quote word for word from the source file, never from working notes.** Including transcription artefacts. If you cannot reproduce it exactly, do not use it. The tidied version always reads better, which is exactly why this rule exists.

**Consent travels with the quote.** Anything from a sales call, cold call, win/loss interview or a named customer is internal-use-only unless the source records explicit sign-off. The tag goes into the avatar, into the brief, and stops at the ad. An internal-only quote can shape an angle and sharpen a hook. It cannot be the ad.

Then the register rules. Where your brand prohibits characterising competitors, that holds even inside this document: buyers will characterise incumbents in their own words and you record it as a finding, and it still cannot cross into copy. Where your brand caps how far pain-led framing may go, note per avatar where that bites. Follow your house rules on punctuation and banned phrases.

## Step 5: REFRESH

The mode that usually gets skipped, so it gets the detail. The failure here is not inventing. It is **rewriting**: someone tidies away a contradiction, or quietly upgrades an evidence tier, and the document loses the thing that made it valuable, which is the record of what you used to believe and why you stopped.

### What triggers one

| Trigger | What changes |
|---|---|
| A research sweep surfaced new material | New verbatims, new triggers, possibly a new territory or a re-tier |
| A test result contradicted a stated objection or a "what NOT to say" entry | Field 6 or 10, and this is the only route to evidence-based field 10 entries |
| A campaign invented an avatar on the fly | Promote it with all eleven fields, or it evaporates |
| **Customer sign-off landed** | Consent tags flip on specific quotes. Often the highest-value refresh available, because it unblocks proof-led and social-proof creative across the whole programme at once |
| A targeting attribute became buyable | Field 2 on every avatar it touches, and the workaround note comes out |
| New segment, product line or geography | Usually BUILD, sometimes a field-2 extension |
| Nothing, and it has been a couple of quarters | Re-tier evidence rather than letting High stand by default |
| A gap got closed | Edit that gap entry to say what closed it and when, and leave the entry in place |

### How to write the change

The library grows by dated additive entry and is **never rewritten**. Five rules:

- **Add, do not replace.** New evidence goes in as a dated addition under that avatar. The old reading stays visible, including where it turned out to be wrong.
- **Record contradictions, do not smooth them.** Keep both readings. A retired reading with its reasoning attached is what stops the same idea being proposed again next quarter.
- **Retire with a reason and a date.** Never delete.
- **New avatars append in their section** and get a new row in the territory index. The index is not rewritten.
- **Never silently re-tier.** A tier change is a dated entry with its reason.

### Always produce a changelog

A diff on a large file is unreadable, so the refresh is not done until you report, both in the chat and at the top of the file's entry:

- Which avatars changed, and which field in each
- Any tier change, with the reason
- Any consent tag that flipped, and what that unblocks
- Any gap closed, and any gap newly discovered
- What you looked for and did not find

## Step 6: Coverage, and the gaps section

The gaps section is the most useful part of the document for whoever commissioned it, and the part that decays fastest. Every job updates it.

It records: which buying-committee seats have no evidenced avatar, which pains have no verbatim language, which avatars are weaker than their tier suggests, and what research would close each. Be specific and unflattering. A library that addresses only the champion seat cannot move a deal that stalls at the gatekeeper or the signer, which is where B2B deals actually stall, and the gaps section is where that gets said out loud.

After a BUILD, check the new avatar against the others: if it would be defeated by the same objection as an existing one, or if a concept written for it would work unchanged for another, it is not a distinct avatar. Merge it or say why it stands.

## Step 7: Verify

Run before writing to the file, and hand a substantial change to a subagent with fresh eyes.

- Every claim cites a named source
- Every quote reproduced exactly, checked against the source, not against notes
- Every quote consent-tagged, defaulting to internal-use-only
- Field 2 states what is not targetable, with the workaround
- Field 4 says how *this* avatar experiences the pain differently
- Field 10 says where each entry came from
- Evidence tier states the account count
- Register sweep against your own voice and writing rules
- Additive only: nothing overwritten, nothing deleted, no silent re-tier
- Territory index and gaps section both updated
- Changelog written

## Output

Edit the avatar library in place, additively. Tell the user the file and the changelog. If the library is not reachable, write the entry locally, deliver it, and say clearly that it has not been folded in yet.

Where a refresh surfaces something that belongs in buyer research rather than in an avatar, flag it for whoever maintains that research instead of editing it from here.

## Handoffs

| Next question | Where |
|---|---|
| Angles, concepts, a brief, a campaign | the `creative-strategy` skill |
| The pain bank, verbatims and the pain by avatar matrix | `creative-strategy`, `references/pain-mapping.md` |
| Fresher buyer material | whoever maintains the research documents |
| Company-level ICP and sales personas | your ICP and persona process |
| Targeting, budget, campaign structure | your paid-media process |
