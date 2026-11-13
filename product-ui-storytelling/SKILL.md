---
name: product-ui-storytelling
description: Create or revise believable product UI sequences for ads and marketing visuals using the company’s actual interface. Use to show requests, actions, approvals, results and connected workflows without inventing product behavior.
---

# Product UI Storytelling

Show the product doing the work promised by the ad. A decorative chat exchange or a sales claim inside a bubble is not a demonstration.

## Ground the experience

Inspect the company's current UI through approved screenshots, product access, design files or code references. Prefer reusable real assets/components when available. Code structure can establish appearance, but does not alone establish a deployed capability. Never trigger live customer workflows merely to obtain a marketing screenshot.

Separate two checks: does the interface resemble the real product, and does the depicted action actually exist? Confirm actions, channels, connected systems, permissions and completion states from supplied or verified product context. If uncertain, use a supported narrower example or present the sequence as an explicitly identified concept in review notes.

## Write a stateful sequence

Start with a specific user request containing enough context to act. Show a useful product action, any required decision or approval, and a meaningful result or next owner. Two or three readable turns may suffice; let the use case determine length. Avoid tiny narration that lists every internal step.

Examples of state distinctions:

- Draft prepared → human review → document sent → signed only when signing is supported and has occurred in the depicted scenario.
- Change proposed → named approver decision → record updated; never skip a required approval.
- Question answered versus request triaged, assigned, followed up and resolved; routing is not resolution.
- Report retrieved versus report generated or exported; a displayed chart does not prove forecasting.

Use fictional names and values for constructed examples. Keep sensitive real records out of creative. Do not invent performance results through example data. Place review-only caveats outside the customer-facing artwork unless a visible qualification is necessary for accuracy.

## Reproduce the interface grammar

Follow the actual product's sender labels, alignment, avatars, agent icons, spacing, result cards and response grouping. Determine alignment from the depicted viewpoint and channel: a native product chat, Slack conversation and Teams thread have different conventions. Do not universalize one prior client's left/right alignment rule.

Group consecutive product responses consistently. Keep agent labels associated with their messages. Show a connected-system mark inside the relevant sourced UI element when that is how the product represents it. A Slack example should visibly follow Slack conventions rather than resemble an unrelated floating chat.

For an ad adaptation, preserve recognizable structure while increasing legibility. Show only useful controls and fields; avoid excessive box-within-box framing. Transparent treatments must preserve contrast and not imply unsupported interaction. Position UI around faces and inspect text at mobile size. Product-specific styling takes precedence over a generic glass effect.

## Handoff and review

Return the sequence, sources, state assumptions and final result, plus assets if requested. Identify reconstructed or simplified UI in the review record. Ask `ad-creative-direction` to integrate it into the composition when available. Keep source mappings and captions synchronized through `ad-library-review`. Do not claim actual execution based on a constructed ad sequence.
