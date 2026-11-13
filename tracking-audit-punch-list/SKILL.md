---
name: tracking-audit-punch-list
description: Audit marketing tracking and analytics on one or more websites (tag manager, ad-platform conversion tracking, analytics properties, pixels, consent management, CRM tracking, schema and SEO tags) and return a short P0/P1/P2 punch list in plain operator shorthand, plus a reference table of every tag, property and portal ID found. Use when someone says "audit our tracking", "is our ad tracking set up", "are conversions firing", "check GTM / GA4 / LinkedIn Insight / Meta Pixel", "why don't we have conversion data", "tracking punch list", or pastes a tracking audit and asks to "simplify it" or "rewrite it like I wrote it". For building a full tracking plan or implementing events, hand off to an analytics-tracking skill.
---

# Tracking audit punch list

Most tracking audits come back as consultant reports: long, hedged, and hard to act on. What a marketer actually needs is a priority-ordered list of what's broken, why it matters in one line, and the IDs needed to fix it. Ad spend without conversion tracking is the most expensive gap, so that leads.

## Inputs

Read `company-context.md` first (repo root, or search the workspace for it). This skill uses: site URLs and which brand each belongs to, known tag/analytics/ad/CRM IDs, ad platforms with spend, conversion pages and events, markets served, tracking audits folder.

If the file or a line is missing, ask once, then offer to save the answer to `company-context.md` (create it from the repo template if needed). Never fill a gap with an assumption about the company.

## Workflow

### 1. Inspect each site
For each URL, check the page source, the rendered DOM and network requests (a browser tool, or the user's exported audit). Record:
- **Tag manager**: present or not. If not, where tags are hardcoded (framework code, site-builder panels). No tag manager means every change needs a developer.
- **Ad conversion tracking**: Google Ads conversion tags and Enhanced Conversions; LinkedIn Insight Tag and whether conversions are defined in Campaign Manager; Meta Pixel and which events fire beyond PageView.
- **Analytics**: property ID present in code vs actually initialising and sending hits. Conversions marked, cross-domain set up, internal traffic filtered, ad account linked.
- **Consent**: a consent management platform present, Consent Mode v2 wired, and whether tags fire before consent.
- **CRM tracking**: tracking code and portal ID; whether several brands share one portal or tag and need separating.
- **SEO and schema** (lower priority): duplicate or missing structured data, missing social meta tags, thin sitemaps.

Separate "ID is in the code" from "confirmed firing". Never mark something working without seeing the request.

### 2. Prioritise
- **P0, fix now**: anything that leaves live or planned ad spend blind (no conversion tracking, no tag manager blocking the fixes, conversions undefined, analytics not confirmed collecting).
- **P1, next**: consent and legal risk, pixel events beyond PageView, analytics hygiene, a written event plan on a shared dataLayer, separating shared tags or portals by brand.
- **P2, later**: schema and SEO cleanup, tool choices, server-side tagging.

If several sites are in scope, say which goes first and why (usually the one with the least infrastructure or the most spend).

### 3. Write it in operator shorthand
Default register: how a marketer writes notes to themselves, not a report.
- Numbered items, a bold imperative title, then 1-2 short sentences: what's wrong, why it matters.
- First person, plain words, no hedging, no explanatory sub-clauses beyond the one "why".
- Keep every ID, page path and event name exactly as found, in code formatting.
- P2 can be one line listing several items.

Example item:
> 2. **Set up Google Ads conversion tracking.** Doesn't exist on either site. Any ad spend right now has zero conversion data, no Smart Bidding signal, no remarketing lists. Track `/request-demo` + `/thank-you`. Add Enhanced Conversions.

If the user pastes an existing audit and asks to simplify it, keep the findings and priorities and only change the register.

### 4. Add the ID reference table

| What | Value |
|---|---|
| Analytics property ID (per site) | |
| Ad platform tag / partner IDs | |
| CRM portal ID | |
| Conversion pages / events needed | |

Note when an ID is shared across brands.

### 5. Save it
Save as `<Brand(s)>-Ad-Tracking-Audit.md` with the date, the punch list, the ID table and a status line ("saved punch list, not yet actioned" or what has been done). Re-audits update the same file with a dated section showing what's now fixed.

## Works with

- **Measures what the other skills produce**: campaigns built from `vertical-persona-research` and `abm-account-multithread` can't be read without working conversion tracking, so run this before paid spend scales.
- **Hands off** implementation (event plan, dataLayer, tag setup) to an analytics-tracking skill, and test design to an A/B or creative-testing skill.
- **CRM portal splits** found here matter to `abm-account-multithread`, which relies on clean account and contact data.

Skills named here are optional. If one isn't installed, do that step inline and say so.

## Checks before handover

- Every "working" item was confirmed firing, not just found in code.
- Every ID is copied exactly.
- P0 is about ad spend and measurement, not nice-to-haves.
- No item runs past two sentences except where an ID list needs it.
