# Output template: the creative strategy brief

One document per job. Write it to your team's marketing or campaign folder as `<YYYY-MM-DD>-creative-<slug>.md`, with the production brief as `<YYYY-MM-DD>-creative-<slug>-production.md` alongside it.

Sections 1 to 8 are the brief. Section 9 is the verification checklist and it is canonical: do not run a different one.

This is the **strategy brief**: the argument and the evidence, for whoever approves it. The **production brief** is a separate document with a separate template in `production-brief.md`. Do not merge them. A builder should not have to read a positioning argument to find an aspect ratio.

Not every section applies to every job. Drop what does not apply and say you dropped it, rather than padding. The "Notes on using it" section at the foot of this file says which sections each size of job needs. `SKILL.md` Scaling covers which *steps* to run, which is a different cut.

---

```markdown
# Creative brief: [what this is for]
**Brand or product:** [which one, or combined]
**Date:** YYYY-MM-DD
**Platform:** LinkedIn [formats]
**Audience and awareness state:** [who, and what they already know]
**Status of ground truth:** full | degraded (capability baseline unreachable) | [what was missing]

## 1. The read

Three or four sentences. What this campaign is for, who it is aimed at, what was
concluded, and what is being recommended. Written so someone who reads only this
section can brief someone else correctly.

## 2. Who this is for

The avatars in scope, from your avatar library (see `ad-avatars.md`). One to three.
Named, not described.

| Avatar | Committee seat | Awareness state, in which audience | Targetable? | Evidence tier |
|---|---|---|---|---|
| [label] | Champion | Problem-aware, cold ICP | Function and seniority yes, incumbent system no | High, 12 accounts |

**Seats addressed by this set:** [which]
**Seats not addressed, and the consequence:** [which, and what the set therefore cannot move]
**Where targeting cannot reach the avatar:** [and whether the copy is doing the qualifying instead]
**Consent position:** [what proof is available externally, and what is blocked]

## 3. What the buyer says

The evidence, in the buyer's words. Sorted by force, and tagged by avatar so coverage is visible.

| Force | Avatar | Verbatim or finding | Source | Signal | Consent |
|---|---|---|---|---|---|
| Push | [label] | "..." | Buyer research, [source and account] | 5 | INTERNAL ONLY |
| Pull | [label] | "..." | Buyer research, [source and account] | 3 | INTERNAL ONLY |
| Anxiety | [label] | "..." | Pain bank, [verbatim ID] | 4 | INTERNAL ONLY |
| Habit | [label] | [finding, no quote available] | Buyer research synthesis, theme 4 | 3 | n/a |

Verbatims quoted word for word from the source. Sources are the buyer-research
documents listed in `inputs.md`. Signal scored 1 to 5 per `pain-mapping.md`;
nothing scoring 1 appears here.

**Awareness state:** [which, and why]
**Market sophistication:** [where this claim sits, and what that allows]
**Discarded:** [any low-signal assertion dropped, named, so it is not re-proposed]
**Gaps:** what could not be evidenced, and what that means for what can be claimed.

## 4. What the field is running

Teardown date, competitors covered, and what could not be seen.

### Share of voice by angle

| Angle | [Competitor] | [Competitor] | [Competitor] | Read |
|---|---|---|---|---|
| ... | ●●● | ● | · | saturated |

### Reads

- **Saturated:** [angles buyers have learned to discount]
- **Contested:** [winnable with better proof or a sharper mechanism]
- **Open:** [nobody claiming it]
- **Claimed without proof:** [where the credibility gap is]
- **Likely winners, hypothesis only:** [longevity and variant repetition, stated as signals not evidence]

Full record in the swipe file, [date] section, per `competitor-teardown.md`.

## 5. Position

**Competitive alternatives**, ranked by what this buyer would actually do instead.
Include the status quo, the spreadsheet, the manual process, the incumbent nobody
has replaced, the hire they would make instead.

**Unique attributes**, checked against the capability baseline.

**Value, with proof attached.**

**Who cares disproportionately**, and how they are identifiable in targeting terms.

**Frame of reference.**

**Opponent tiers:** status quo / active consideration set / phantoms being ignored
and why.

**Defensible white space:** the intersection of what nobody claims and what your own
buyers describe unprompted. Name it explicitly. If the intersection is empty, say so.

## 6. Angles

### Taken forward

| # | Angle | Argument in one line | Evidence | Share of voice (pulled) | Awareness states | Proof | Register check |
|---|---|---|---|---|---|---|---|
| A1 | ... | "..." | High, 4 accounts | Open, YYYY-MM-DD | Problem, solution | Mechanism | Clear |

The awareness column carries the deployment read from `creative-matrix.md` section 2, and it goes into the angle library so the next run does not rebuild it. The share-of-voice cell carries its pull date or it is not citable.

### Cut, and why

| Angle | Cut on | Reason |
|---|---|---|
| ... | Evidence | No buyer evidence found. Either table stakes or a research gap |
| ... | Register | Characterises another vendor, which your rules forbid |
| ... | Proof | Claim requires a number the verification tracker has as unverified |

The register cuts stay in the document. They get proposed again otherwise.

## 7. Concepts

One block per concept. Three to five total.

### C1 · [name] · [angle] · [format]

- **Hypothesis:** one sentence. What is believed will happen and why.
- **Avatar and awareness state:** one of each, named. Not a list.
- **Mechanic:** [which of the eight, per hooks-and-mechanics.md, and why this argument needs that structure]
- **Format and why this shape:**
- **Hook (verbatim):** "..." [and the tactic it uses]
- **Visual:** [wireframe, per visualisation.md notation]
- **Visual register:** [screenshot / data / illustration / human / text-only]
- **Proof carried:** [what, and its strength]
- **Offer and CTA:**
- **Landing destination:** [URL, whether it exists yet, and whether the message matches]
- **Copy**

  | Slot | Copy | Chars | Limit | Pass |
  |---|---|---|---|---|
  | Intro text | "..." | 138 | 150 visible | yes |
  | Headline | "..." | 61 | 70 | yes |
  | In-image | "..." | | | |

- **Claims:** [SAFE] / [NEEDS VERIFY: what, and who decides]
- **Production:** what it takes to build, and by whom.

## 8. What this needs next

- **Test plan and measurement:** hand to the `creative-testing` skill. [What the priority test is]
- **Targeting, budget, campaign structure:** hand to your paid-media process. [Anything creative implies about the audience]
- **Copy variations at volume off a chosen angle:** per `production-brief.md` section 4.
- **Landing page work:** [any message-match gap found, and who owns the page]
- **Decisions needed from a human:** [the open conflicts this brief ran into]
- **Sign-offs needed:** [any quote requiring customer consent]

## 9. Verification

Run every line. Quote the offending copy on any fail.

**Grounding**
- [ ] Capability baseline read, including anything it records as contradicted
- [ ] Every number checked against the verification tracker
- [ ] No product fact, quote, stat or competitor capability invented
- [ ] Nothing claimed as live that has not shipped
- [ ] Nothing claimed that sits on a known product-reliability risk list
- [ ] Every angle traces to named buyer evidence, or is labelled as a gap

**Register**, per your brand and voice rules
- [ ] **Extend this block on first use with your brand's own register rules**, written
      out as checks, and keep them here so every run checks them
- [ ] Internal quotes consent-tagged, and no call-recording, win/loss or
      named-customer material in any customer-facing line
- [ ] No unsubstantiated superlative, and no unprovable claim of primacy
- [ ] No characterisation of another vendor, named, unnamed or positive, where your
      rules forbid it. Swap test run on every customer-facing line
- [ ] No dunking on competitors' reviews or on their customers
- [ ] No hedges
- [ ] No fluff. Every line states a fact, makes a claim, or moves it forward
- [ ] House punctuation respected, including no em dashes
- [ ] No banned phrase from your list
- [ ] Any never-lead list respected: the capabilities your positioning does not lead
      with, and any framing it forbids outright

**Craft**, per your writing rules
- [ ] Swap test: no line that still works with a competitor's name on it
- [ ] Falsifiable: no decorative claim
- [ ] Visualisable: instances, not categories
- [ ] Mechanism named where the claim needs one
- [ ] Proof strength matches claim strength
- [ ] No banned or weak phrase
- [ ] Category vocabulary correct: the nouns your brand uses and does not use, and
      the framings it requires around what the product decides and does not decide

**Awareness match**, per hooks-and-mechanics.md section 4
- [ ] Each concept names one avatar and one awareness state, not a list
- [ ] No cold concept opens with the product name
- [ ] No retargeting concept opens with a problem the viewer moved past
- [ ] Each hook opens with what its stated awareness state permits
- [ ] Market sophistication accounted for: no bare claim in a late market

**Platform**, per platform-specs.md
- [ ] Every character count stated and under limit
- [ ] Hook lands inside the first 150 characters
- [ ] Headline works alone
- [ ] In-image text legible at phone width, survives dark mode
- [ ] Captions specified for video
- [ ] No unverifiable superlative
- [ ] No competitor logo or name without escalation and approval

**Set quality and diversity**, per creative-matrix.md section 3. Thresholds, not preferences.
- [ ] Three to five concepts, and no two defeated by the same objection
- [ ] At least three distinct arguments
- [ ] At least two of the four forces
- [ ] At least two committee seats, and the unaddressed seats named
- [ ] At least two awareness states
- [ ] At least three mechanics or formats
- [ ] At least two visual registers, and no two visuals that merely look different
- [ ] Each concept has a hypothesis that could turn out false
- [ ] Landing destination exists and matches the promise, per concept
- [ ] Cuts recorded, with reasons, split into evidence and register
- [ ] The set was priced before it was written, and the arithmetic is in the brief
- [ ] Any cap on coverage stated out loud: nothing trimmed for budget or capacity without saying so

**Loop closed**
- [ ] Avatar library updated with any new or revised avatar
- [ ] Pain bank updated with new verbatims, consent-tagged
- [ ] Angle library updated, share-of-voice read carrying its pull date and the awareness states recorded
- [ ] Offer library updated, or created if this run named an offer that is not in it
- [ ] Account baseline updated, or created if this run produced a number for it
- [ ] Swipe file updated with today's teardown, including the blind spots
- [ ] Learning log entry opened for each concept going live
- [ ] Production brief written, with its dependency register filled and owned
- [ ] Both briefs written to the marketing or campaign folder and delivered as files
```

---

## Notes on using it

**Degraded mode.** If the capability baseline is unreachable, say so in the header and run sections 1 to 7, with section 7 carrying the concept reasoning and no copy tables. What the baseline records as contradicted is the only thing standing between a confident headline and a claim the product does not support, so the concepts can be argued and none of them can be written.

**Iteration briefs are short.** A refresh of a fatigued winner needs the header, section 7 for the new execution, and section 9. A hundred and fifty words on what is changing from the parent ad, not a rebuilt strategy. Most briefs in a running programme are this shape.

**Two tiers when consent requires it.** Where the argument needs internal-only material, build a prospect-safe version on aggregate findings and a banner-flagged internal version, clearly separated. Never blended.

**For a substantial brief, hand section 9 to a subagent with fresh eyes.** Give it the draft, this checklist, the capability baseline, the verification tracker and your brand and voice rules. Ask for per-item pass or fail with the offending line quoted. Self-verification on a document you just wrote catches the mechanical items and misses the register ones.
