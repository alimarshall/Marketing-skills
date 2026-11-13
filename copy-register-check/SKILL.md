---
name: copy-register-check
description: Mechanically check finished copy against a house style rule set, using a literal search rather than a read-through. Use when a house style guide bans specific constructions, phrases or punctuation and copy needs checking before it ships. Triggers on "check this against our style guide", "run the copy sweep", "did we catch all the X", "does this match our voice rules", "banned phrases". Also run it as the final step of any workflow producing customer-facing copy, after the last edit.
---

# Copy register check

A style rule that is only checked by reading is not checked. The characteristic failure is not missing the rule. It is asserting the sweep was clean when it was never actually run.

This skill exists to make the check mechanical, so the output is a list of found strings rather than a claim of cleanliness.

## Step 1: Get the rule set as literal strings

House style rules come in two shapes. Only one is greppable.

**Greppable rules** are literal strings or simple patterns: a banned punctuation mark, a banned phrase, a specific spelling, a forbidden product name. Collect them into a list.

Typical entries: em dashes, "not just", "not only", "isn't just", "rather than", "instead of", "in order to", "leverage", "seamless", "robust", "cutting-edge", "delve", "utilize", specific competitor names, deprecated product names, retired figures and timelines.

**Judgement rules** need a read: tone, whether a claim is hedged, whether a sentence characterises a competitor through a silent subject. These get a manual pass. Do not pretend a grep covers them.

If the rule set does not exist yet, build it from the last three rounds of editorial feedback. The rules people actually enforce are the ones they keep correcting.

## Step 2: Run the search on the finished file, after the last edit

Order matters. Running the sweep and then editing invalidates it. This is the most common way a sweep passes and the violation ships anyway.

Use a literal search tool over the file. Case-insensitive. Whole file, including headings, table cells, image alt text, slide labels and captions, which is where these hide.

Report the count for every rule, **including the zeroes**. "0 matches for 'not just'" is the evidence. "Sweep clean" is not.

## Step 3: Manual pass for the patterns a search cannot catch

Some constructions have no fixed string. Read for these specifically:

- **Split antithesis across sentences.** "Getting the number is easy. Knowing it is right is the hard part." No banned substring, same banned shape.
- **Negation then correction.** "This is not a reporting tool. It is a decision layer."
- **"X, not Y" with arbitrary X and Y.** No fixed string to search for.
- **Silent-subject competitor characterisation.** Insert "our competitors" as the implied subject of the sentence. If it reads cleanly, the sentence is characterising them.
- **Absolute language in a hedged domain.** "always", "never", "any", "fully", "completely", "exactly" attached to a safety, permission or coverage claim.

## Step 4: Cut rather than rephrase

A banned construction usually survives rephrasing because the underlying shape is what the rule targets. "It shows the work, not just the answer" becomes "It shows the work behind the answer" only if you change the idea, not the wording. If a rewrite keeps the two-part contrast, it has not been fixed.

Where cutting genuinely loses meaning, say so and offer two alternatives rather than shipping the violation with an apology attached.

## Step 5: Report, and flag anything already in flight

The report is: rule, count, and every matched line quoted with its location. Then the manual-pass findings.

If a violation was already published, already in a design file, or already in a recorded asset, flag that separately and loudly. A fix in the source document does not fix the slide deck someone built from it last week.

## A note on repeat failures

If the same rule keeps getting violated, the problem is upstream. The construction is probably load-bearing in how the writer naturally phrases the idea, which means the fix is a positive rule ("say it this way") rather than another prohibition. Add the replacement pattern to the style guide rather than the ban alone.
