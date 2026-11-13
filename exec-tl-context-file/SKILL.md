---
name: exec-tl-context-file
description: Audit everything you have on a founder or exec, find the gaps for thought leadership, ask the right questions, then build one context file AI can write LinkedIn posts from.
---

# Exec thought leadership context file

Builds the single source an AI (or a ghostwriter) uses to write thought leadership for a named founder, exec or marketer. It runs in two passes: a coverage audit with questions, then the context file itself. Works for any company and any person.

Use for "run through everything we have on [person] and tell me what's missing", "what questions do we still need answered for good TL copy", "save everything for [person] as a context file", or before starting a LinkedIn programme for someone new.

## Before you start: company context

Read [`company-context.md`](../company-context.md) at the repo root for the company, buyer research, house style and the **Thought leadership** section: who the exec is, their LinkedIn profile, where their spoken and written material lives, and where the context file should be saved. If a line you need is blank, ask once and offer to save the answer back to that file.

## Works with

- **Takes in:** the exec's transcripts, written material and published posts, plus the company's buyer research and positioning.
- **Produces:** a coverage audit with open questions, then one dated context file for the exec.
- **Next:** exec-post-skeletons-from-buyer-research (plans posts from the file), employee-linkedin-posts for other team members. Any skill named here that isn't installed is done inline.

## Pass 1: coverage audit

### Gather

- **Transcripts and recorded calls** (substance: what they think).
- **POV docs, manifestos and published long-form writing** (form: how they write).
- **Published LinkedIn posts.** Pull the actual posts with dates and reactions, comments and reposts. Read-only browsing is fine. Find the real profile slug by searching if the obvious one fails.
- **Brand or strategy session notes**, earlier TL plans, voice guides and feedback they've given on drafts.
- **The company's buyer research and positioning**, so the person's pillars connect to what buyers care about.

### Score coverage

For each area, mark it covered, thin or missing, and say where the evidence sits:

- Beliefs and worldview
- Positions they've confirmed
- Positions you're inferring
- Personal stories
- Proof numbers they're allowed to use
- Voice (written form against spoken form)
- Structures and hooks that have worked
- Boundaries (topics, competitors, customers, numbers)
- Time available and approval process
- Spelling convention

### Ask

Give the person a numbered list of the questions that are still open, ordered by how much each answer would improve the copy. Typical gaps:

- Personal stories with specifics.
- Positions you've inferred but they haven't confirmed.
- Lines on sensitive partners or competitors.
- Which internal numbers they'll publish.
- Approved aggregate framing for customer conversations.
- Spelling, and time to review.

When the person answers, propose positioning and pillars with rough weightings, for example 35/35/20/10, plus three to five opinions per pillar. Mark what they confirmed and what is still a proposal.

## Pass 2: build the context file

One markdown file, with these sections in this order:

1. **How to use this (AI instructions):** which section to read for which task, and the order of precedence when sources conflict.
2. **Programme:** goal, audience, cadence, who approves.
3. **Who they are:** role, history and credibility, in plain facts.
4. **Beliefs:** core beliefs with evidence, how their view has shifted this year, confirmed positions, positions from sessions, and positions still to confirm (labelled clearly).
5. **Pillars:** each with weighting, audience and example angles.
6. **Performance table:** published posts by type, with reactions, comments and reposts, the medians, and what has worked. Note gaps in posting.
7. **Voice:** written register rules. State outright that spoken patterns are for substance only.
8. **Structures, hooks, endings and formatting.**
9. **Boundaries and house rules:** competitors, customer quotes (consent rules), capability honesty, banned constructions, spelling.
10. **Data:** which numbers can be used, with source and framing.
11. **Process:** drafting, review, the pre-post checklist.
12. **Conflicts resolved:** where sources disagreed and which one wins.
13. **Open questions.**
14. **Sources:** every file used, with location.

## Rules

- Every belief or position needs a source. Put inferred positions under "to confirm" and never present them as confirmed.
- Keep spoken quotes internal. The file can cite them as evidence, but posts must never transcribe them.
- Never name customers or prospects or quote them in any example post line.
- No em dashes or contrast constructions in the file's own example lines, and the AI-writing-tells rules apply.
- Save it where the team keeps brand files, with the date in the filename. Tell the person what's still open in one line.
