---
name: "use-case-evidence-research"
description: "Research one or more product use cases or features end to end: pull what the product actually does from internal product docs, rescan sales and customer call transcripts plus any voice-of-customer library for pains, hopes and reactions, verify every quote word for word, and write finished reference docs (internal, or an external-safe customer-proof version) mirrored to a wiki. Use whenever the user asks to update use case docs, rescan the calls, find new quotes for a feature, asks what buyers say about something, wants themes and quotes per use case, asks what pains a feature solved for a customer, or wants research cleaned up so it reads as a finished doc. First step of a four-skill set: its output feeds capability-pillar-research and pillar-landing-pages, and claim-propagation-sweep keeps it current."
---

# Use-case evidence research

Turns scattered product notes and call recordings into one verified, finished reference doc per use case or feature: what the product does, what hurts buyers today, what they hope to have, what excites them about the product, and (when asked) what a named customer's pains were and how the feature solved them.

The two failure modes this skill exists to prevent:
1. **Quotes that aren't real.** Paraphrases drift into quotation marks, or a vendor's own salesperson gets quoted as if they were the buyer. Every quote is checked by script against the raw sources before the doc is done.
2. **Docs that read like a change log.** "Updated 3 Oct", "added after the sweep", "NEW", "v2". Readers want a finished reference.

## Works with

- **Takes in:** product docs (capability lists, roadmaps, specs, release notes), call transcripts, any voice-of-customer library, existing use-case docs.
- **Produces:** one evidence doc per use case or feature (internal, or external-safe), product capability snapshots, and the quote-check script used by the whole set.
- **Next:** capability-pillar-research (to regroup this evidence by verb) or pillar-landing-pages (to write page briefs). The same docs feed use-case-ad-variations (one ad group per use case), teach-then-sell-video-scripts and education-video-prep. Start from buyer-research's VOC library when one exists. Run claim-propagation-sweep when a product fact you documented here changes.

## 0. Scope (ask only if unclear)

- Which use cases or features, and which product.
- Output mode: internal research doc (named quotes allowed, consent note at top) or external-safe proof doc (see shared rule 7).
- Where docs live (local knowledge base, wiki, both). Archive a copy of any older version before overwriting.

## 1. Product ground truth

Find what the feature actually does before writing about it: the product team's wiki/project pages (capability lists, use case catalogues, roadmaps, specs, RFCs, release notes), any internal capability baseline, and recent product walkthroughs or meetings with the product team.
- Record each capability in plain words with its stated status.
- Flag conflicts between sources (a capability page says "not built", the roadmap says done) instead of silently picking one. If one source is newer and clearly supersedes, say which and why.
- Snapshot important wiki pages into the local knowledge base (one file each, source URL and last-edited date in the header).

## 2. Gather the voice of the customer

Use every source available, widest first:
- **Raw call transcripts** (for example Gong: `/v2/calls/extensive` with parties for the date range, then `/v2/calls/transcript` in batches of up to 100 call IDs, joined on speakerId). Select calls for this product by title, owner and the prospect's email domain, then include follow-up calls with the same domains. Save one text file per company: each call headed with id, date, title and participants; each line labelled PROSPECT or VENDOR with speaker name and title. Only PROSPECT lines can be quoted.
- **Voice-of-customer library** (quote banks, tagged CSVs) and existing research docs.
- **Existing use-case docs:** keep every finding that still holds.

Build an evidence pack per use case with a script: library rows matching the use case's themes or keywords, earlier per-company tags, and keyword hit counts per company in the transcripts so you know where to look. Also pull "excitement candidates": prospect lines with words like love, amazing, game changer, impressed, wow, huge, within a few lines after a topic hit. Read each in context; many are reactions to something else.

Watch for: calls under one domain about a different product from the same vendor; two companies with the same short name (check email domains); a vendor employee's line attributed to the buyer.

## 3. Write the doc

For large jobs, give each use case (or pair) to a subagent with a shared written brief, the evidence pack, the transcript folder and the quote-check script. The same quote should not appear on two pages.

**Internal research doc**
```
# [Use case]: buyer context
[2-3 sentences: what it covers, how strong the evidence is.]
**Consent:** named people and companies come from internal recordings; none are cleared for external use.

## What hurts today
### [Theme in plain words]
[1-2 sentences on the pattern.] Raised at N accounts.
- "[verbatim]" (Name, Title, Company, Mon YYYY)
## What they hope to have
## What excites them about [product]
## What makes them hesitate   (optional, 2+ accounts)
## Who cares most             (table: persona | what hurts | what they want | what they'd measure)
```
3-7 themes per section ordered by account count; 2-5 quotes per theme; a theme needs 2+ accounts, single-account items go under "Emerging signals". Pains are what's broken today; hopes are what they want to exist; excitement is only reactions to the product itself.

**External-safe proof doc** (one feature, one or more customers)
```
# [Feature]
[2-3 sentences: what it is.]
## What it does
[Capabilities under short bold headings. Shipped only.]
## The problems it solved at [Customer]
[One line on how they use it.]
| What [Customer]'s team dealt with | What [product] does instead |
[Only pair a pain with a shipped fix.]
**In their words** [quotes grouped by pain]
## What [Customer] wanted from it
[Quotes grouped by want. Unsolved wants stay here, not in the table.]
```

## 4. Verify

Run `python3 -I verify_quotes.py DOC.md TRANSCRIPTS_DIR LIBRARY.csv OTHER_DOCS...` (script below) until it reports 0 not found. Then scan for process words and em dashes (shared rules 6 and 8).

```python
import re, sys, glob, os
def norm(s):
    s = s.lower().replace('’', "'").replace('‘', "'")
    return re.sub(r'[^a-z0-9 ]', '', re.sub(r'\s+', ' ', s))
src = []
for p in sys.argv[2:]:
    files = glob.glob(os.path.join(p, '**', '*'), recursive=True) if os.path.isdir(p) else [p]
    for f in files:
        if os.path.isfile(f): src.append(open(f, errors='ignore').read())
S = norm(' '.join(src)); bad = tot = 0
for line in open(sys.argv[1], errors='ignore'):
    if not line.lstrip().startswith('- "'): continue
    for q in re.findall(r'["“]([^"”]{15,})["”]', line):
        for part in re.split(r'\.\.\.|…|\[[^\]]*\]', q):
            if len(part.split()) < 4: continue
            tot += 1
            if norm(part).strip() not in S: bad += 1; print('NOT FOUND:', part.strip()[:150])
print(f'{tot} quote fragments checked, {bad} not found'); sys.exit(1 if bad else 0)
```

## 5. Publish and index

- Overwrite the knowledge-base files (archive copies first).
- Mirror to the wiki: fetch each page first, replace content, preserve child pages, create missing pages, convert tables to the wiki's format, strip filenames and internal links.
- Rewrite the hub page as a clean intro: what the pages are, the consent note (internal docs only), one honest line of evidence strength per use case, links in a sensible order.
- Add the docs to the knowledge base's index or README.

## 6. Report back

What changed per use case (themes, quotes, accounts, how many accounts are new), where evidence is thin, data fixes (merged companies, misattributed speakers), the verify result, and conflicts or decisions that need a human.

## Shared rules (identical across the four skills in this set)

1. **Evidence before copy.** Every product claim, stat and quote traces to a named source. Never invent a capability, number, customer story or quote. If the evidence isn't there, say so.
2. **Shipped means shipped.** State a capability's status (shipped, in progress, planned) only as the source states it. Buyer requests the product can't meet go under hopes or wants, never under capabilities.
3. **Quotes are verbatim and buyer-side.** Copy exact words; cut with "..." but never change them. Never quote the vendor's own staff as a buyer. Before finishing, run the quote check (the script ships with use-case-evidence-research as `verify_quotes.py`) and fix or drop anything not found.
4. **Claim tags.** Mark copy and claims SAFE, NEEDS VERIFY: (what would settle it), or INTERNAL ONLY (named customer material without sign-off). Carry tags forward from one skill's output into the next; don't strip them.
5. **Thin evidence is said plainly.** Count distinct accounts, not quotes. Never pad a weak area to match a strong one.
6. **Finished docs, not change logs.** No "updated", "added", "new", version numbers, sweep or session references in docs meant to be read as references. Version history holds that.
7. **External-safe mode** (when the user says external, for ads, for customers, keep it clean): job title and company only, no personal names; no dates; competitor names inside quotes replaced with a neutral bracket such as "[the old tool]"; no notes about sign-off, sources or usage. Tell the user in your reply that customer quotes still need sign-off.
8. **Voice.** Plain and direct. No em dashes. No hedge words. Don't characterise competitors beyond what buyers say themselves. No filenames in the body of a doc.

## How the four skills work together

1. **use-case-evidence-research**: collects and verifies the evidence (product capabilities, buyer pains, hopes, reactions) per use case or feature.
2. **capability-pillar-research**: regroups that evidence by verb (what the product does) when positioning by behaviour rather than feature.
3. **pillar-landing-pages**: turns the positioning into one page brief per pillar or feature, using only claims from steps 1-2.
4. **claim-propagation-sweep**: runs whenever a product fact changes, across everything steps 1-3 produced, and feeds corrections back into the evidence docs.

Outputs of one step are the inputs of the next. If you're asked for a later step and the earlier output doesn't exist, build the earlier step first (or tell the user it's missing) rather than writing from memory.

The wider marketing-skills set builds on the same docs: buyer-research feeds step 1, competitive-matrices holds the approved claims, and use-case-ad-variations, teach-then-sell-video-scripts and education-video-prep turn the evidence into ads and video. Claim tags mean the same thing in every skill.
