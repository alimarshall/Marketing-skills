---
name: claim-verification
description: Check that every factual claim in a piece of work is traceable, correctly scoped, and safe to publish before it ships. Use when reviewing marketing copy, a positioning brief, a sales deck, an RFP answer, a case study, a security questionnaire, or any document making claims about a product, a customer or a competitor. Triggers on "is this accurate", "can we say this", "check these claims", "fact-check this", "is this safe to publish", "did we verify this". Also run it as the last step of any workflow that produces customer-facing claims.
---

# Claim verification

Most bad marketing is not badly written. It is confidently written about something nobody checked. This skill is the layer that runs underneath any work making factual claims.

Four claim types carry risk, and each fails differently:

| Type | How it fails |
|---|---|
| **Product capability** | Says the product does something it cannot, or understates something that shipped months ago |
| **Customer evidence** | Uses a quote, name or logo without consent |
| **Statistics and dates** | Cites a number whose source has gone stale or never existed |
| **Competitor capability** | States something about another company that is out of date or was never verified |

## Step 1: Extract every claim

Go through the document and list each factual assertion separately. A sentence can contain three claims. Split them.

Ignore opinion and framing. Target anything a reader could check, contradict, or ask you to prove: what the product does, what it costs, who uses it, how fast, how many, what a competitor does, what a certification covers.

## Step 2: Trace each claim to a source

For every claim, record: **what it asserts**, **what source supports it**, **the date of that source**, and **whether it is safe externally**.

Three distinctions collapse constantly and must be kept separate:

1. **"Someone internal confirmed it works"** is not the same as **"it is safe to say publicly."** A capability can be live and still be un-announceable for pricing, security or roadmap reasons.
2. **"Engineering confirmed it is live"** is not the same as **"a customer has confirmed it works."** The second is what a case study needs. The first is what a capability claim needs. Do not let one stand in for the other.
3. **"It is on the roadmap"** is not **"it is shipped."** Shipped status is the single most consequential fact in any product claim.

A claim with no source is not a claim. It is a guess. Mark it and either cut it or downgrade it until the evidence supports it.

## Step 3: Rate evidence strength, and match the claim to it

Rate every claim that rests on research:

- **High.** Four or more independent accounts, recent, ideally unprompted. Safe to lead with.
- **Medium.** Two or three accounts, or one very strong named source. Safe as support.
- **Low.** One account, or inferred from adjacent evidence. Flag it. Do not build a headline on it.

Then match the claim's strength to the evidence's. If the proof is medium, shrink the claim until it is true at medium. This is almost always better than adding a hedge, because a hedge weakens a strong claim while a scoped claim stays strong.

Watch for the specific trap of **inferred demand**: a capability people would probably like, with no buyer actually asking for it. Two complaint stories are not a request. Say so rather than presenting the inference as a finding.

## Step 4: Check consent on everything attributable

For every customer quote, name, logo, metric or story: does explicit sign-off exist?

Default to no. Sales-call recordings, win/loss notes and internal interviews are internal-use material unless someone has cleared them. Published case studies and public sources are the exception.

**Never blend cleared and uncleared material in the same document.** Put a single prominent internal-only marker at the top of the research document, keep uncleared material out of anything customer-facing entirely, and check the customer-facing sections by search rather than by memory.

## Step 5: Check what must never be said

Every product has a list. Build it once and check against it every time. It usually contains:

- **Absolute safety or guarantee language** where an open security or reliability item exists. State the mechanism as fact. Never phrase it as a guarantee.
- **Capabilities that sound adjacent to real ones but are not exposed.** These are the ones that slip through, because they sound true.
- **Certification dates.** State the fact of certification. Pull the current period before publishing any date, since they refresh.
- **Anything a written questionnaire would answer differently.** If admins cannot restrict something, do not answer "yes" to a question asking whether they can.
- **Competitor characterisation**, where house rules forbid it. Watch for the silent-subject version: "most tools cannot do this" characterises competitors without naming one.

## Step 6: Mark and report

Label every piece of customer-facing copy **[SAFE]** or **[NEEDS VERIFY: what specifically]**. Never hand over a mixed set unlabelled.

Report as a per-item pass or fail with the offending line quoted verbatim. A summary saying "checks passed" is worth nothing. The quoted line is the deliverable.

Where a check could not be run, say which one and why, and mark it unchecked rather than passed. An honest gap is useful. A false clean is not.

## Step 7: Push corrections back to the source

Verification usually finds that a source document is wrong, not just that the copy is. Log those separately with the page and the specific line, and get them fixed at source. See `source-doc-writeback`.
