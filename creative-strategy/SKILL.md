---
name: creative-strategy
description: "Run creative strategy end to end for B2B SaaS paid ads, LinkedIn first and Meta ready. Takes a campaign, launch, segment or refresh from buyer research and ad-avatar mapping through competitor ad-library teardown, positioning, angles by awareness state, hooks and creative mechanics, and concepting, out to a strategy brief, a production brief, ad copy variations and visual direction. Use when the user asks for ad concepts, ad angles, a creative or production brief, campaign creative direction, ad copy variations, visual direction, 'what should our ads say', 'what are competitors running', an ad library teardown, a swipe file, or a creative refresh. Triggers on 'we need new LinkedIn ads', 'what angle should we run', 'tear down their ads', 'brief the designer'. Grounded in the product and buyer documents named in references/inputs.md, never invented claims. Use the ad-avatars skill to build or refresh the avatar library itself."
---

# Creative strategy

Creative strategy is the work between "we should run ads" and "here is the file". It decides which buyer, in which state of knowing, is told which argument, in which shape, backed by which proof. The ad is the last five percent.

The failure this skill exists to prevent: a set of pretty, on-brand ads that make an argument no buyer asked for, in a lane four competitors already own, using a claim nobody verified.

**Never invent a product fact, a customer quote, a stat, or a competitor capability.** Every claim in a brief is traceable or flagged. A concept set that says less and holds up beats one that says more and gets pulled after legal review.

Four rules carry more weight here than anywhere else:

1. **Angle before execution.** A strong angle survives a weak hook. A clever hook cannot rescue a flawed angle. Most teams test three executions of one angle and call it creative testing.
2. **Unclaimed is not the same as defensible.** White space found only in a competitor teardown is a guess. White space corroborated by your own buyer research is a position. Then apply the swap test: could a competitor say this truthfully too?
3. **Price the set before you write it.** The arithmetic in `creative-matrix.md` section 4 comes before concepting, not after. A twelve-concept set handed to a budget that can read three is a wasted week.
4. **Your brand's register rules outrank every pattern in this skill.** The angle taxonomy, the hook taxonomy and the mechanics list all contain standard B2B moves that many brands prohibit. Read the collision tables before writing a word.

**First run:** fill in `references/inputs.md` with your own document paths, and fill in the constraint tables in `angle-library.md` and `hooks-and-mechanics.md` against your own brand rules. Those two edits are what turn a generic method into yours.

## Inputs

Read `company-context.md` first (repo root, or search the workspace for it) and use the fields that apply to this skill. If the file or a line is missing, ask once, then offer to save the answer back to it. Never fill a gap with an assumption about the company. If `creative-strategy/references/inputs.md` is also filled in, it still applies; where the two differ, `company-context.md` wins.

## Step 0: Scope it in one pass

Work this out without stopping to ask unless genuinely ambiguous, then state the read in one line and proceed.

- **Which product or brand**, where more than one exists, and whether this is a combined pitch. Check your brand architecture rules before combining.
- **What the ads are for.** A launch, an always-on demand-gen line, competitor conquest, an event, retargeting, a segment push, or a refresh of a fatigued winner. A refresh is a different job and skips most of this workflow. See Scaling.
- **Which avatars and which awareness state.** One to three avatars, named from the standing library. A job title is not an audience.
- **Which platform and format family.** Specs in `platform-specs.md`.
- **What the budget is.** Needed for Step 7. If unknown, say so and carry the arithmetic as a range.
- **Is there performance history?** If ads have run, the learning log is a first-class input and this becomes an iteration job rather than a blank page.

## Step 1: Load the ground truth

`references/inputs.md` is the contract: what to supply, what each document is for, the reading budget, and what degraded mode looks like. Read in this order, and only what the job needs:

1. **Capability baseline**, including its contradicted-claims section. Every time, before any headline.
2. **Verification tracker.** Before any stat, timeline or gap claim reaches a headline.
3. **Standing creative docs**: the avatar library, the pain bank, the angle library, the swipe file, the learning log. These carry what you already know, already tried and already retired. Skipping them is how a retired angle comes back.
4. **Buyer research**, where the avatar library is thin.
5. **Messaging matrix.** Do not silently re-tier something already decided.
6. **Competitor dossiers**, only for competitors actually named or clearly implied.
7. **Voice and writing rules**, always. This skill does not restate them and does not override them.

If the capability baseline is unreachable, say so at the top of the brief and run degraded: avatars, angles, teardown and concept reasoning only, no finished copy.

## Step 2: Fix the avatars

`ad-avatars.md` has the method. An ad avatar is not the ICP and not the sales persona, and reaching for those is the most common way this step goes wrong.

Read the standing library and select the avatars in scope. Build a new one only if the segment genuinely has none, in which case it gets promoted into the library at the end of the run rather than evaporating. The `ad-avatars` skill owns building and refreshing.

Three things carry forward into the brief:

- **Which committee seats the set will address**, and which it will not.
- **Which avatar attributes are not targetable**, because that decides whether the copy has to do the qualifying the targeting cannot.
- **The consent position.** What proof is cleared for external use, and what is blocked. This governs whether proof-led and social-proof concepts are available at all.

## Step 3: Map the pains

`pain-mapping.md` has the extraction method, the signal scoring and the matrix. `research-method.md` has the four forces, the awareness ladder and the scoring filters.

The short version: extract into five buckets per avatar (pains, triggers, objections, transformations, standout language), score each 1 to 5 for signal and discard the 1s, keep the pattern layer and the verbatim layer physically separate, and build the pain by avatar matrix.

Read the matrix both ways. Down the rows for broadly held pains, which are lead-angle candidates. Across the columns for empty seats, which is the check almost nobody runs and the reason so many B2B sets are coherent and still cannot move a stalled deal.

Quote word for word from the source file, never from working notes. Tag consent on every quote. If a pain in the input has no evidence in the research, write it as a finding, not an angle.

## Step 4: Tear down what competitors are running

Before generating angles, not after. Seeing the field first is what stops the team proudly landing on the angle three competitors already saturated.

`competitor-teardown.md` has the library mechanics, the per-ad field list and the analysis method. Summary:

1. **Pull the ads live.** Drive a browser to the ad library for each competitor in scope. Screenshot and record, do not just read.
2. **Check the EEA view separately** for any European-active competitor, even for a campaign elsewhere. It is the only place any platform discloses targeting at all, and the reference is precise about how much it does and does not give you.
3. **Record every ad against the fixed field list.** Same fields every time or the swipe file stops being queryable.
4. **Cluster by claim, not execution.** Forty ads usually collapse to a handful of real arguments. The collapse ratio is itself a finding.
5. **Build the angle share-of-voice grid, and date it.** Reads go stale fast. A read older than 30 days gets re-pulled, not cited.
6. **Infer likely winners** from longevity and variant repetition only, and say plainly that these are hypothesis signals. No ad library exposes performance for ordinary commercial ads.
7. **Append to the standing swipe file** with today's date, including what you could not see.

The teardown is internal analysis. Where your register rules prohibit characterising competitors in customer-facing copy, none of its characterisation may cross into an ad.

## Step 5: Position, internally then against

Internal first. Competitive creative built on unsettled internal positioning just amplifies the confusion.

1. **Competitive alternatives**, not competitors. What does this buyer do if you do not exist? The spreadsheet, the manual process, the incumbent nobody has replaced, the headcount they would hire instead, doing nothing. Status quo wins more of these deals than any named vendor and almost nobody advertises against it.
2. **Unique attributes**, checkable against the capability baseline.
3. **Value with proof attached.** Ask "so what?" three times. The first answer is still a feature.
4. **Who cares disproportionately**, from the avatar library, in targeting terms.
5. **Frame of reference.** Almost always an existing frame. Do not invent a category in an ad.

Then position against. Sort competitors into **status quo**, **active consideration set** (who actually appears on real shortlists) and **phantoms** (who could compete but does not show up in deals). Position against the first two. Naming a phantom educates the market about a rival for free.

Cross the teardown grid against your own buyer research. An angle is defensible white space only when no competitor credibly claims it **and** your own buyers describe it unprompted. Write that intersection down explicitly.

If the positioning turns out to be unsettled rather than merely unexpressed, stop and settle it. Say so rather than papering over it with creative.

## Step 6: Generate the angles

`angle-library.md` is the taxonomy, grouped by the four forces, with a table of moves that are commonly constrained and how to resolve them rather than drop them.

- Generate across all four forces and across the committee seats, not just the practitioner. Surface **eight to fifteen distinct angle territories** before narrowing. Distinct means a different argument. If two candidates would be defeated by the same objection, they are one territory.
- Run each through three filters in order: **evidence** (which research backs it, how many accounts, how recent), **differentiation** (where it sits on the share-of-voice grid), **proof** (what you can actually show).
- Check the sources pain mining misses: the demotions from prior positioning work, the gaps you admit, and trigger events. Trigger events are the only angles that answer "why now" and among the few directly targetable.
- **Score and rank, evidence first.** Then cut to **three to five**. Say what you cut, separating evidence cuts from register cuts. The register cuts will be proposed again in six months.
- Proof strength scales with claim strength. If the proof is not there, shrink the claim until it is.

## Step 7: Deploy across awareness, and price the set

`creative-matrix.md` sections 2 and 4.

**Deploy.** The angle stays the same; what changes is how it is expressed. Grid each surviving angle against the five awareness states and record what the ad opens with, the audience, and the format that fits. Name the cells you cannot fill and why, because that converts a creative problem into a specific unblock. This is the cheapest expansion available: one angle correctly deployed populates a funnel without inventing a second argument.

**Then price it.** Budget divided by variants divided by weeks, against what the decision needs. If the arithmetic fails there are two honest options, fewer variants or a smaller question. Do this before writing concepts. Adding budget belongs to whoever owns it.

## Step 8: Concept

An angle is an argument. A concept is that argument made specific and briefable: one avatar, one awareness state, one mechanic, one hook, one format, one proof.

`hooks-and-mechanics.md` has the layer stack, the hook tactics with their constraint notes, and the eight creative mechanics. `format-library.md` has the format taxonomy and its fit notes.

**Set size, and which number wins.** The set is **three to five concepts in total**, not three to five per angle. One concept per angle is the default and a second is earned. Where the numbers conflict, the arithmetic in `creative-matrix.md` section 4 is the authority and it is tighter than both: at low volume a campaign carries two ads, so a five-concept set is a sequence across campaigns rather than one test.

For each concept, state:

- **Hypothesis.** One sentence: what you believe will happen and why. This is what the test is actually testing.
- **Avatar and awareness state.** One of each, named. A concept that would work for any avatar is a category statement.
- **Angle** it expresses, and the evidence behind it.
- **Mechanic.** The structural move. Vary the mechanic before you vary the wording.
- **Hook**, written word for word. Not "an attention-grabbing opener".
- **Format**, with the reason this argument needs this shape.
- **Visual idea**, concrete enough to picture, and its visual register.
- **Proof carried**, and its strength.
- **Offer, CTA and landing destination**, and whether the message matches it. Pick from the offer library; where one does not exist yet, use the offer-type table in `creative-matrix.md` section 6, check the asset actually exists, and name it as a dependency if it does not. An invented offer is the easiest accidental breach of the no-inventing rule.

**Then run the diversity check** in `creative-matrix.md` section 3, all six dimensions, before anything goes in a brief. A set of three to five should span at least three arguments, two forces, two seats, two awareness states, three mechanics or formats, and two visual registers. Below that it is a wording test in a concept test's clothes.

## Step 9: Visualise

`visualisation.md` has the fidelity ladder and the tooling. Keep concept-stage fidelity deliberately low so the debate stays on the argument, and go high fidelity only on the chosen direction.

Default: an **ad wireframe** per concept, in the notation in that reference, at the right aspect ratio. Enough for a decision, cheap enough to throw away.

Escalate to a rendered mockup only when the concept will be shown outside the team, when the layout is the idea, or when asked. `assets/ad-mockup.html` renders concepts as feed previews at correct dimensions with the real copy, including the character truncation and dark mode.

Never generate or mock a product screenshot. Never ship AI-generated text inside an image: generate backgrounds and scenes, composite type as a real layer. Label concept-stage artifacts as rough, because stakeholders anchor on anything that looks finished.

## Step 10: Write the two briefs and the copy

**The strategy brief** uses `brief-template.md`. It carries the argument, the evidence, the teardown, the cuts and the reasoning, for whoever approves it.

**The production brief** uses `production-brief.md`. It carries the asset list, the exact copy with character counts, the wireframes or line-by-line tables, file naming that joins to concept IDs, the dependency register, and the two QC gates. It carries no reasoning. A builder should never have to read a positioning argument to find an aspect ratio.

**Copy variations** are produced here, per `production-brief.md` section 4. Every line ships with its character count and a pass or fail against the limit. Every claim is marked **[SAFE]** or **[NEEDS VERIFY: what]**.

## Step 11: Verify

Run the checklist in `brief-template.md` section 9 and Gate 2 in `production-brief.md` section 6. Those are the canonical ones. Do not invent a different one.

For a full concept set, hand verification to a subagent with fresh eyes. Give it the draft, both checklists, the capability baseline, the verification tracker and your register rules. Ask for per-item pass or fail with the offending line quoted. Self-verification on a document you just wrote catches the mechanical items and misses the register ones.

## Output

Write to your marketing or campaign folder as `<YYYY-MM-DD>-creative-<slug>.md`, with the production brief as `-production.md` alongside. Deliver the files. Do not render a full brief only in chat.

Then update the standing docs in the same pass, additively and dated:

- **Avatar library**: any new or revised avatar, its evidence tier, its gaps.
- **Pain bank**: new verbatims with consent tags, new triggers, matrix changes.
- **Angle library**: any new territory, its evidence tier, its status, its dated share-of-voice read, the awareness states deployed.
- **Swipe file**: everything pulled in Step 4, including the blind spots.
- **Learning log**: the concepts entering test, so the loop can be closed when results land.
- **Offer library** and **account baseline**: created or updated if this run produced anything for them.

## Handoffs

| Next question | Where |
|---|---|
| Build or refresh an avatar | the `ad-avatars` skill |
| How to test this and read the result | the `creative-testing` skill |
| Targeting, budget, campaign structure | your paid-media process |
| The product message itself is unsettled | product positioning, before any creative |
| The landing page the ads point at | landing page copy and conversion work |
| Fresher buyer material | whoever maintains the research documents |

## Scaling

- **Refresh of a fatigued winner.** Steps 0, 1 (learning log and verification tracker only), 8, 10. Same concept, new execution. Do not rebuild the strategy for a re-skin, and confirm first that it is fatigue rather than a creative that never worked.
- **One campaign or launch.** The full workflow, teardown limited to the two or three competitors that actually appear in those deals.
- **A quarter of creative, or a new segment.** The full workflow, all tracked competitors, plus a standing angle roadmap sequencing what gets tested when, built off the awareness deployment grid.
- **Opening a higher-volume channel.** Same workflow. What changes is feed context, not method: polish is penalised, native is rewarded, video carries far more weight, and volume thresholds finally become reachable, which is the point at which variable-level testing and the high-volume cadence literature start to apply. See `creative-matrix.md` section 4.
