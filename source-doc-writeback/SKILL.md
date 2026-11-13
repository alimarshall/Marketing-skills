---
name: source-doc-writeback
description: When a fact gets newly verified or corrected (an engineering confirmation, a scope document, a spec, a shipped feature), sweep every internal document for the stale version and update it. Use for "update all our docs that reference X", "this changed, what else needs fixing", "propagate this correction", "our docs are out of date on Y". Also run it after any research or positioning pass that turned up contradictions between internal sources.
---

# Source document writeback

New ground truth arrives constantly. The failure this prevents is the correction living only in the conversation where it was learned, while five other documents keep steering other people's decisions with the old version.

A stale document is worse than a missing one, because people trust it.

Two failure shapes, equally damaging:

- **Overclaim.** A document says the product does something it cannot. This is what puts an impossible demo in a launch webinar and a wrong answer in an RFP.
- **Underclaim.** A document says something is unverified or not yet external when it shipped months ago. This is what makes teams sit on real capability and lose deals they could win.

Hunt for both. Underclaims are quieter and get found less often.

## Step 1: Write the ground truth down first

Before touching a single document, write the corrected facts as a numbered list, each with its source and date. Every edit later traces to one of these numbers. If you cannot write the fact cleanly, you do not understand it well enough to propagate it.

For each fact record: **what is now true**, **what documents might say instead**, **who or what confirmed it**, and **whether it is safe externally**. Keep three things separate that constantly collapse into one: confirmed to work, safe to say publicly, and confirmed by a customer.

**Where a correction splits a previously bundled claim, say so explicitly.** "A and B are both unverified" splitting into "A is impossible, B is fully supported" is two facts, and documents will need both halves. Bundled cautions are how a real capability stays suppressed for months.

## Step 2: Sweep for every document carrying the claim

Delegate this to a read-only search pass so the document dumps stay out of your working context. Give it the numbered ground truth verbatim, the list of documents already updated, and this instruction:

> Return page title, page ID, the **verbatim** stale string (exact and copy-pasteable, for use as a search-and-replace target), and one line on what is wrong and what it should say. Rank by severity: overclaims first, then understated live capability, then wording risks. Do not list pages that mention the subject accurately.

Search broadly. Run several queries: the feature name, its technical or protocol name, the endpoint or URL, the specific claims being corrected, and the stale phrasings themselves ("not yet external", "unverified", "TBD", "coming soon", "included at no extra cost").

**The documents that hide are the ones nobody thinks of as product documentation:** webinar run-of-show scripts, sales battlecards, roadmap checkboxes, risk registers, onboarding decks, help-centre articles, FAQ pages. These carry product claims and none of them surface under an obvious search.

## Step 3: Decide what you own

Edit documents the requester owns. For documents owned by another function, especially security risk registers and engineering roadmaps, report the verbatim stale string and the correction, and let the owner apply it.

Say plainly which you edited and which you did not, and why. Editing another team's risk assessment unasked costs more than leaving it stale for a day.

The exception is a stale item causing active harm right now, such as a public-facing script claiming something impossible. Flag that one at the top of the report regardless of who owns it, with the deadline attached.

## Step 4: Apply the edits

Use search-and-replace with the verbatim string from Step 2. Two rules that come from real failures:

1. **Watch the escaping.** Content fetched through an API often comes back escaped. A quotation mark inside the fetched text may display as `\"` while the actual document contains `"`. Passing the escaped form as the search target silently matches nothing, **and some tools return success anyway**.
2. **Verify every edit by re-fetching and searching for your new string.** Never trust a success response. Count occurrences of both the old and the new string. If the page is too large to fetch inline, save the output to a file and search that.

Date-stamp each correction inline: **"Corrected YYYY-MM-DD:"** plus what changed and what confirmed it. The next reader needs to know the line was deliberately revised rather than drifting.

Where a document has a changelog or "what changed" section, add an entry naming the row edited, the sources applied, and what the document was getting wrong. This is what stops the same correction being re-litigated in three months.

## Step 5: Add what is missing, not only fix what is wrong

A correction pass usually exposes something no document carries at all. The most valuable addition is a **boundaries entry**: what the thing cannot do, cannot reach, or must never be claimed, with the mechanism attached.

"No review endpoint exists, so the structure a cycle needs cannot be created" is checkable by the next person. "Do not claim cycles" is not, and it will be quietly ignored the first time someone wants to claim cycles.

Also add a pointer from each updated document to the single canonical reference for the subject, so future readers check one place.

## Step 6: Report

Three lists:

1. Documents edited, and what changed in each.
2. Documents flagged and left alone, with the owner and the reason.
3. Anything still needing a decision from a person.

Call out separately any correction that invalidates something already published, recorded or shipped. That one has a deadline the others do not.
