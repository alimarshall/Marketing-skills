---
name: positioning-brief
description: Turn product input (a PRD, spec, changelog, release note or feature list) into positioning, the features worth leading with, messaging for each, and channel-ready copy. Use when someone shares a product change and asks how to position it, what to lead with, which features to highlight, what the angle is, or asks for a positioning brief, PMM brief or GTM brief. Triggers on "we just shipped X", "what do we say about this", "value prop for this feature", "what do we lead with". Decides WHAT to say about a product change. Hand off to a copywriting skill to write a page once the message is set, and to a launch skill for channels and sequencing.
---

# Positioning brief

Positioning is a set of decisions about what is true, who cares, what they would do instead, and what you can prove. It is not a tagline and it is not a feature list. This skill runs those decisions in order and then writes the words.

The failure it exists to prevent: confident copy for a claim nobody verified, aimed at a buyer nobody checked, against a competitor nobody actually loses to.

**Never invent a product fact, a customer quote, a statistic, or a competitor capability.** Everything traceable, or flagged. A brief that says less and holds up beats one that says more and gets caught.

## Inputs

Read `company-context.md` first (repo root, or search the workspace for it) and use the fields that apply to this skill. If the file or a line is missing, ask once, then offer to save the answer back to it. Never fill a gap with an assumption about the company. If `creative-strategy/references/inputs.md` is also filled in, it still applies; where the two differ, `company-context.md` wins.

## Step 0: Scope it in one pass

Settle three things without stopping to ask unless genuinely ambiguous:

- **Which product or brand**, if the company runs more than one.
- **What altitude.** A single feature, a feature set, a release, or a repositioning. This sets how much of the workflow runs.
- **Whether it has shipped.** Shipped, in build, designing, or proposed. This is the most consequential fact in the brief because it governs what may be claimed. Check it. Do not infer it from the document you were handed.

State the read in one line and proceed.

## Step 1: Load the ground truth

If this repo's `creative-strategy` skill is installed, its `references/inputs.md` is the shared contract naming your own document paths. Read them from there rather than keeping a second list.

Read what already exists, in this order, and only what is relevant:

1. **Capability reference.** What the product actually does, and any list of claims that sound right and are not true.
2. **Differentiation or claims document.** The claims already made and the proof behind each.
3. **Verification log.** What is not safe to say yet. Check this before any statistic or timeline enters the brief.
4. **Buyer research.** The pain language, in buyers' own words.
5. **Buyer aspirations or win/loss.** The positive-signal counterpart. What buyers get excited about.
6. **Existing messaging hierarchy.** Whatever already tags features as lead, supporting or table stakes. Do not silently re-tier something that has already been decided. If the new input changes it, say so explicitly.
7. **Competitor material**, only if a competitor is named or clearly implied.

**Where sources disagree, say so rather than picking silently.** A person's direct confirmation from engineering or product beats every stale document. If the core capability reference is unavailable, say so at the top of the brief and run degraded: positioning and reasoning only, no channel copy.

## Step 2: Distil the input

For each capability, complete the four-link chain. The skipped link is where the generic benefit statement comes from.

| Link | Question | Source |
|---|---|---|
| **Feature** | What exists in the product? | The input and the capability reference |
| **Capability** | What can someone now do that they could not? | Derived, plainly |
| **Value** | What outcome does that create? | Derived, and it must be falsifiable |
| **Pain** | What buyer struggle does it resolve? | **Buyer research only.** Never invented. |

If a capability has no pain link in the research, it does not get to lead. Write that as a finding: *"No buyer evidence found. Either table stakes, or a gap in our research."*

Also record for each: who it is for, what they do today instead, and what proof exists.

## Step 3: Position it

Work these in order. The order is load-bearing. Starting at the category or the tagline is the standard way to get this wrong.

1. **Competitive alternatives.** What would this buyer do if you did not exist? Include the status quo, the spreadsheet, the manual process, the homegrown build, and doing nothing. These win more deals than named vendors do. Exclude any competitor who does not actually appear on your shortlists.
2. **Unique attributes.** What you have that those alternatives lack. Checkable against the capability reference.
3. **Value, with proof attached.** Ask "so what?" three times. The first answer is still a feature.
4. **Who cares disproportionately.** Not who could use it, but who cares more than average, and what makes them identifiable from the outside.
5. **Frame of reference.** The category or comparison that makes the value obvious. Almost always an existing frame. Do not invent a category unless asked to.

Then write **one positioning paragraph** a salesperson could say out loud, and run the three tests below on it.

**The three tests, run on the paragraph and on every headline:**

- **Swap test.** Put a competitor's name on it. If it still reads as true, it is not positioning, it is category description.
- **Falsify test.** Could this claim be shown to be false? If not, it is unfalsifiable and technical buyers will discount it.
- **Visualise test.** Can the reader picture the specific thing? Replace abstractions with the actual list, the actual action, the actual number.

## Step 4: Pick what leads

Tier every capability:

- **Lead.** Differentiated against the real alternatives, evidenced in buyer research, and provable. Very few things qualify.
- **Supporting.** Real value, reinforces the lead, does not carry the headline.
- **Table stakes.** Needed to avoid losing, never persuasive. Comparison page and RFP, not the hero.

Rank the leads on three factors, evidence strength first: **buyer evidence** (how many accounts, how recent, how senior), **differentiation**, **proof strength**. Show the reasoning.

**Aim for three to five leads, and if fewer clear the bar, deliver fewer and say so.** "One lead, two supporting" is a legitimate brief. Never promote a supporting item to fill the slate.

Name what you demoted and why. The demotions are often the most useful part of the brief.

**If nothing survives the swap test, that is the finding, and it goes at the top.** A release can be a very good parity release. Say so, explain that the copy below is the best available for a parity release, and route the differentiation claim to whichever product or capability actually holds it. Do not paper over it with a headline that only sounds differentiated.

**Set the launch weight.** Five questions: does this change how buyers evaluate you, open a new segment, neutralise a competitor advantage, drive expansion, or require market education? Few yeses means a feature page and a changelog, not a campaign.

## Step 5: Write the messaging

For each lead: a headline, a one-line sub, the mechanism ("because…"), the proof, and only the persona variants that genuinely differ.

- **Name the mechanism.** A benefit without one is unfalsifiable and gets discounted, especially by technical and security buyers. The shape is "[outcome] because [how it works]".
- **Match proof strength to claim strength.** If the proof is not there, shrink the claim until it is.
- **One story, branched proof.** Same mechanism for every seat in the buying committee. Only the evidence and the units change.

## Step 6: Channel-ready copy

Default set unless told otherwise: page hero (H1 and sub), feature block headlines and subs, ad angles, and a short announcement paragraph.

Mark each piece **[SAFE]** or **[NEEDS VERIFY: what]**. Never hand over copy mixing the two without labelling.

If the copy includes a page hero, check whether a previous hero exploration already ruled options out. Re-proposing a rejected headline is the most common failure here.

## Step 7: Split the output into two documents

This is the default shape. A brief carrying both the decisions and the research behind them is unusable by the person who has to act on it.

**The brief** is what someone picks up and works from: in one line, positioning, what to lead with, messaging, channel-ready copy, decisions needed. Roughly 1,500 to 2,500 words. Constraints stay inline where they govern what gets written or designed, phrased as instructions. No verbatims, no evidence ratings, no methodology, no notes about what an earlier draft got wrong.

**The context document** carries everything else: the evidence behind each lead with the source quotes, audience evidence, any competitive check run, the tests run and what they killed, the constraints with their sources, a reading list, and the checks.

Each document points at the other in a one-line footer.

Mark consent-restricted material once, prominently, at the top of the context document, and never let a restricted quote reach the brief's channel copy.

## Step 8: Verify

Run the claim and register checks mechanically rather than asserting them. See the `claim-verification` and `copy-register-check` skills if they are available.

At minimum: every claim traceable, shipped status accurate, statistics checked against the verification log, swap test run on every headline with results reported, consent checked on every quote, and a literal grep for house style violations run **after** the last edit.

For a substantial brief, hand verification to a reviewer with fresh eyes. Give them the draft, the checklist, the capability reference and the verification log, and ask for per-item pass or fail with the offending line quoted.

## Step 9: Write the corrections back

A positioning pass almost always finds internal documents that are stale, contradictory, or claiming something the product cannot do. List them in the decisions section with the page and the specific line, and use the `source-doc-writeback` skill to fix them. Do not leave a correction sitting only in the brief.

## Scaling

- **A single small feature or a changelog line.** Steps 0, 1 (capability reference and verification log only), 2, 5, 6 (announcement only), 8. One page, no context document. The split earns its keep above roughly 1,500 words.
- **A feature set or a launch.** The full workflow, both documents.
- **A repositioning or a new product line.** The full workflow, plus flag that message testing with real buyers should follow. This produces a hypothesis, not a validated position.
