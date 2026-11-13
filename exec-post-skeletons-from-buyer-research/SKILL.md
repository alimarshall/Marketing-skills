---
name: exec-post-skeletons-from-buyer-research
description: Turn buyer research and a VoC library into LinkedIn post skeletons for a founder or exec, one per buyer pain, each with evidence, the exec's take, hooks and an ending.
---

# Exec post skeletons from buyer research

Builds a bank of LinkedIn post skeletons for a founder or exec, grounded in what buyers actually say. You get one skeleton for each buyer pain or sub-pain, grouped by pillar. Each skeleton carries buyer evidence, the exec's take on each point, hook options, an ending and "to confirm" flags. Works for any company.

Use when someone asks for "post angles on the buyer pains", "skeletons for [exec]", "thought leadership ideas from the buyer research", "go down this list of pains and give me posts", or wants something to share with the exec for a keep, edit or cut pass.

Skeletons come first, always. Write full posts only when the person asks for them after seeing the skeletons.

## Before you start: company context

Read [`company-context.md`](../company-context.md) at the repo root. You need the house style and capability baseline from it, plus the **Thought leadership** section: the exec, where their spoken and written material lives, their context file, positioning guardrails, approved framing for customer conversations, numbers cleared for publishing, and where the skeleton doc should live. If a line you need is blank, ask once and offer to save the answer back to that file.

## Works with

- **Takes in:** the exec's context file (from exec-tl-context-file), buyer research and a VoC library (from buyer-research or vertical-persona-research), the capability baseline.
- **Produces:** a shareable doc of post skeletons by pillar, plus questions for the exec.
- **Next:** claim-verification for any number or capability a post relies on, copy-register-check on any skeleton that becomes a full post. Any skill named here that isn't installed is done inline.

## Inputs (read before writing)

1. **Buyer research**, organised as pillars and sub-pains, with quotes and the number of accounts behind each.
2. **A VoC or quote library** (CSV or similar) with theme, sentiment and company columns, so you can count across companies.
3. **The exec's substance**: transcripts, recorded calls, interviews, brand-session notes. This tells you what they think.
4. **The exec's written form**: manifestos, published posts, a writing-style guide. This tells you how they write.
5. **Positioning guardrails**: what the product is and isn't (for example "works on top of the system of record, never replaces it"), what's live versus roadmap, and the house rules.

If the exec's voice material or the positioning guardrails are missing, ask before drafting.

## Step 1: Synthesise before you write

Ask "what are all these things, combined, saying?"

- Count across the VoC library: the share of companies raising each theme, sentiment split by theme (frustration, excitement, anxiety), and how themes shift across the period, for example first half against second half.
- Write five to eight numbered findings that together tell one story about where the buyer is now. Every skeleton should trace back to one of them.
- Use percentages, never "X in Y". Treat exaggerated numbers from calls as colour, never as stats.

## Step 2: Group the sub-pains

- Go pillar by pillar and cover every sub-point in the research.
- Merge near-duplicate sub-points into one skeleton, for example "maintenance burden" with "stalled internal bots". Note which sub-points each skeleton covers.
- Expect three to eight skeletons per pillar.

## Step 3: Write each skeleton in this exact format

```
### [Code]. [Title written as the post's idea]

Who it's for: [named roles]
Concept: [one or two sentences: the one idea the post makes]

Points
1. [Point heading.] [Buyer evidence written as a pattern across conversations.]
   Your take: "[the exec's take, written in their composed register]" (Builds on [which of their known views])
2. ...
(three or four points)

Hooks
- ([hook type]) "[opening line]"
- ([hook type]) "[opening line]"

Ending: "[closing line]"
To confirm: [only where a line depends on a capability, a number or a call the exec hasn't made]
```

Useful hook types are observation, concession, pattern, number, reframe, advice and confession.

## Rules for evidence

- **Patterns only.** Never quote or name a prospect or customer in a post, even anonymised, without consent. Write "in our conversations with [buyer role] this year" or "buyers describe...". Don't paraphrase a single memorable quote so closely that it still reads as that person's quote.
- **Evidence-tight.** Every point needs a source in the research. No causal leaps. If you find yourself writing "X made Y visible" or "because of AI...", check that a buyer actually said it.
- **Capability honesty.** Use the present tense only for what's live. Anything on the roadmap or still being built gets a "to confirm" flag, or the post becomes an observation post with no product claim.
- **Positioning.** Never drift into a framing the company has ruled out. Check every take against the guardrails.

## Rules for the exec's take

- Take the substance from the spoken material and the form from the written material. Never transcribe speech patterns (fillers, circling, "kind of") into written copy.
- Use their composed register: declarative sentences, "we believe", "we've seen" or "I suspect" before a contestable claim, and human control in the same sentence as any autonomy claim.
- No rhetorical questions in takes or hooks if the exec doesn't use them.
- Concede first, then move to the structural point. Write what's been observed, never prophecy.
- Lift their own lines verbatim where they fit, and label them.
- Never characterise competitors.
- If a take is a stretch and you can't trace it to something they said, cut it.

## Make it shareable with the exec

- Open the doc with a short "how to use this" section: what each part of a skeleton is, and what you want back (keep, edit or cut, and corrections to takes).
- Follow it with the synthesis, written externally.
- Take out internal jargon, account names and team shorthand.
- Frame takes as "suggested takes" for the exec to rewrite.
- End with questions for the exec: which ones go first, which numbers they're comfortable publishing, personal stories, comfort with self-critical posts, positions to state, capabilities to confirm, and anything missing.

## Delivery

Use a living doc the exec can comment on, where available. Plant section placeholders first: intro, synthesis, one per pillar, and questions. Fill one section per write so the person can watch it fill.

## Before handing over

- Sweep every line for contrast constructions ("not X, Y", "isn't X. It's Y", "rather than", "instead of", "less like... more like") and rewrite them as plain statements.
- No em dashes. Use the spelling convention of the exec's market.
- Run the AI-writing-tells checks: no reflex rule of three, no uplift lines, no summary sentences that repeat the point.
- Check every percentage against the count.
- Close with one line and the link, with no recap.
