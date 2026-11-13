---
name: capability-boundary-map
description: Turn a scope document, permissions table, API spec or feature matrix into a plain-language map of what a product can read, what it can change, and what it cannot touch, for use as the claim-safety reference before anything ships. Use when someone shares a technical spec and asks what can be claimed, or when copy, a deck, an RFP answer or a security questionnaire needs a checkable boundary. Triggers on "what can it actually do", "can we say it does X", "what are the limits", "build a capability map", "what is not exposed".
---

# Capability boundary map

Marketing claims fail at the edges. The middle of a capability is well understood by everyone. The edge, where something sounds adjacent to a real capability but is not exposed, is where the wrong claim gets made and where a technical buyer catches it.

This skill turns a technical source into a document a non-technical person can check a claim against in thirty seconds.

## Step 1: Get the authoritative source, and read it properly

The source is whatever defines access at the system level: a permissions or scopes table, an API endpoint list, a feature-flag matrix, an entitlements document.

**Prefer the system-level source over a product document.** A product page describes intent. A scopes table describes what is actually reachable.

Two extraction traps:

- **Formatting that carries meaning gets lost in text extraction.** Strikethrough, greyed-out rows, colour coding and annotations often mark removed or unavailable items, and plain text extraction drops all of it. If the source is a PDF or an image-heavy document, render it and look at it. A row struck through is a materially different fact from a row present.
- **Absence is a finding.** An endpoint or permission that does not appear anywhere is not an oversight to gloss over. It is the boundary. Search for the thing you expect to find and record that it is missing.

## Step 2: Sort into three buckets, grouped the way a buyer thinks

Not by endpoint. By the thing a person would ask about.

1. **Can read and change.** Group by domain: people records, documents, workflows, billing, whatever the product's areas are. Note the permission or scope each requires, since that is what a security reviewer will ask.
2. **Can read only.** The distinction matters more than people expect, and it is the first thing a competitor comparison turns on.
3. **Cannot reach at all.** Split this into *removed* (was available, now explicitly disabled) and *never exposed*. Removed is a stronger statement than never exposed, and copy must reflect it.

Count each bucket. The counts are usable proof points and they make staleness obvious later.

## Step 3: Resolve every "sounds adjacent" case explicitly

This is where the value is. For each capability that sounds like it should be reachable, write down whether it is and what the mechanism is.

The pattern to hunt: a domain where **individual records are writable but the orchestrating structure is not.** You can change one record, so it feels like you can run the process. You cannot, because the process needs a structure that is not exposed.

Write the mechanism, not just the verdict. **"No review endpoint exists, so the structure a cycle needs cannot be created"** is checkable by the next person. **"Cannot run cycles"** is a rule someone will quietly break.

Also resolve the reverse case: something a previous document said was unavailable, which the source shows is fully supported. Record the correction with the same specificity.

## Step 4: Watch for words that point at the wrong thing

A common wording risk: the copy uses a word that is also the name of a module which is not exposed. The capability may be genuinely real (the numbers come from the underlying records) while the word points a technical buyer at a product that is not reachable.

Flag these as wording risks rather than false claims, and propose the reword. The distinction matters, because "this claim is false" and "this word is ambiguous" get fixed by different people.

## Step 5: Write the three sections copy actually uses

Close the map with a section a writer can lift from directly:

- **Safe to say.** The full accurate description, in plain language, phrased as it would appear in copy.
- **Safe to say and underused.** Things the map revealed that no existing positioning material mentions. This section is usually the most valuable output.
- **Never say.** The specific claims that are false, with the mechanism attached.
- **Watch the phrasing on.** The ambiguous words from Step 4.

## Step 6: Make it the standing reference

State at the top what this document is for: check it before any capability claim goes into copy, a deck, an RFP answer or a security questionnaire.

Date it and name the source, including any detail about how the source was read (rendering a document to catch strikethrough, for example) so the next person can reproduce it.

Then point the other product documents at it, so there is one place to check rather than four. See `source-doc-writeback` for propagating what this map corrects.
