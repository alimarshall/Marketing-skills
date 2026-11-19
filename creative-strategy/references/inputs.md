# Inputs: what this skill needs you to supply

These skills invent nothing. Every claim in a brief traces to a document you own or gets flagged as unverified. That discipline is the whole point, and it means the skill is only as good as the inputs behind it.

This file is the contract. It says what to supply, what each document is for, and what the skill does when one is missing.

**Paths live in [`company-context.md`](../../company-context.md)** at the repo root, the single setup file every skill reads. The `Path` column below points there; the matching line has the same name (the claim verification tracker is "Verification tracker", the messaging matrix is "Communication matrix", brand voice is under "House style"). Fill in `company-context.md` once; nothing in this file needs editing.

---

## 1. Ground truth: supply these

### Product truth

| Document | Its job | Path |
|---|---|---|
| **Capability baseline** | What the product actually does, verified. Ideally with a section listing claims that sound right and are not. That section gets read before every headline. | see `company-context.md` |
| **Claim verification tracker** | What is not safe to say yet. Every number, timeline and gap claim passes through here before it reaches an ad. | see `company-context.md` |

Without the capability baseline the skill runs **degraded**: avatars, angles, teardown and concept reasoning, and no finished copy. Say so at the top of the brief rather than writing copy on unverified ground.

### Buyer evidence

This is where angles come from. Nowhere else.

| Document | Its job | Path |
|---|---|---|
| **Buyer pain research** | What hurts, in the buyer's own words, attributed to named accounts. The Push language. | see `company-context.md` |
| **Buyer aspiration research** | What they get excited about. The Pull language, and consistently the thinnest file in most teams. | see `company-context.md` |
| **Voice-of-customer verbatims** | Attributed quotes, ideally emotion-tagged. The single best source for hook language, because it is already in the buyer's words. | see `company-context.md` |
| **Ranked pain themes** | Frequency-ranked pains across a pipeline or account set. Frequency ranking is directly usable as angle prioritisation. | see `company-context.md` |
| **ICP and buyer personas** | Firmographics and committee seats. **Not ad avatars.** See `ad-avatars.md` for the difference. | see `company-context.md` |

**Know the bias in whatever you supply here.** Most teams' buyer research comes from one corpus shape: their own sales conversations. It is rich, and everyone in it is already talking to you. It contains nothing from people who never took the call and almost no unprompted language, because a discovery call is a prompted setting. For cold, problem-aware creative, unprompted language is exactly what is missing. `pain-mapping.md` names the review and forum corpora that fix it.

### Messaging decisions already made

| Document | Its job | Path |
|---|---|---|
| **Messaging or communication matrix** | Feature to pain to benefit to proof, tagged by priority. Check before proposing a new lead angle, so the brief does not silently re-tier something already decided. | see `company-context.md` |
| **Positioning briefs** | What was demoted and why. A capability demoted because it is table stakes can still be a strong ad angle at a different awareness state. | see `company-context.md` |

### Brand rules

| Document | Its job | Path |
|---|---|---|
| **Voice and register rules** | **This outranks every pattern in the skill.** The taxonomies here contain standard B2B moves that your brand may prohibit. | see `company-context.md` |
| **Writing rules** | Banned phrases, hedges, house punctuation, proof ranking, how you write about your category. | see `company-context.md` |

The skill does not restate these and does not override them. Where a rule blocks an angle, a hook tactic or a mechanic, the brief records the block and the reason rather than quietly working around it.

**Encode the collisions once.** `angle-library.md` and `hooks-and-mechanics.md` both carry a table of moves that are commonly constrained. On first use, fill those tables in against your own rules. That is the highest-value setup step in the whole skill, because it converts brand rules into creative decisions rather than leaving them as a review gate someone fails at the end.

### Competitors

| Document | Its job | Path |
|---|---|---|
| **Competitor dossiers** | Read only for competitors actually named or clearly implied. The deal-intelligence section first: who appears on real shortlists. | see `company-context.md` |
| **Advertiser page slugs** | The ad-library page for each tracked competitor, confirmed as the corporate page rather than a regional or careers one. | see `company-context.md` |
| **Shared-gap list** | Where you and a competitor have the same weakness. These are precisely the claims a conquest angle reaches for first. | see `company-context.md` |

---

## 2. Standing docs: the skill creates and maintains these

These compound. Create each on first run using the shape described in the reference that owns it, then append dated entries. **Never rewrite history.** A retired reading with its reasoning attached is what stops the same idea being proposed again next quarter.

| Doc | Holds | Owned by |
|---|---|---|
| **Avatar library** | One entry per ad avatar against the eleven fields, plus a pain and desire territory index and a coverage-and-gaps section | `ad-avatars.md`, and the `ad-avatars` skill |
| **Pain bank** | Two physically separate halves: a pattern layer of the five buckets per avatar with signal scores, and a verbatim layer of exact quotes with source and consent tag. Then the pain by avatar matrix | `pain-mapping.md` |
| **Angle library** | Every angle territory: the argument in one line, its evidence tier, the share-of-voice read **with the date it was pulled**, the awareness states it has been deployed at, the register check, and a status | `angle-library.md` |
| **Swipe file** | One dated section per teardown: ads against the field list, screenshots, claim clusters, the share-of-voice grid, the pull depth, and what you could not see | `competitor-teardown.md` |
| **Learning log** | One entry per concept that goes live: hypothesis, what shipped, dates, spend, impressions, the metrics, what it taught, whether the angle survives | The `creative-testing` skill |
| **Account baseline** | Click-through rate, dwell, engagement and cost per lead, by format and by audience, updated when a campaign closes | The `creative-testing` skill |
| **Offer library** | One row per offer: what it is, the awareness state it fits, the friction it asks for, which avatars it is credible to, whether the asset exists, what it has produced | `creative-matrix.md` section 6 |

Two of these are the ones teams skip, and both cost you later. **Without an account baseline** the first diagnostic question, did this ad ever beat the account median, has nothing to read, and every judgement falls back on published benchmarks whose ranges are too wide to aim at. **Without an offer library** every angle test runs against a fixed and unexamined constant, so a flat result may be an offer problem misread as a creative one.

**Check the learning log can hold a result before the first result lands.** A log with columns for hypothesis and outcome and nowhere to put dates, spend, impressions and the conversion metric will be rebuilt in a hurry at exactly the wrong moment.

---

## 3. Access and freshness

- **Where two sources disagree, say so.** Do not silently pick. Note which you used and flag the discrepancy for whoever owns the documents.
- **Where a mirror exists** (a wiki copy of a file, a database view of a tracker), record which is authoritative. Mirrors drift.
- **Name your single points of failure.** If one document has no backup and the skill degrades without it, write that down here so the degradation is expected rather than discovered.
- **Share-of-voice reads decay fast.** A read older than 30 days gets re-pulled, not cited. See `competitor-teardown.md`.

---

## 4. Reading budget

The standing docs grow. Reading everything before writing an angle will spend most of a session, so read to the job.

| Job | Read |
|---|---|
| **Any run** | The capability baseline's contradicted-claims section. The verification tracker rows touching your claims. The avatar library's territory index and gaps section. The pain bank's matrix and gaps section. |
| **Segment or launch brief** | Add the full entries for the one to three avatars in scope, and the pain-bank buckets for those avatars only. |
| **Refresh of a fatigued winner** | The learning log entry and the verification tracker. Nothing else. |
| **A quarter of creative, or a new segment** | Everything, and expect it to take a session on its own before any concepting. |

Structure the standing docs by stable IDs (avatar IDs, verbatim IDs, angle IDs) and grep for them rather than reading sequentially. That is what makes a large library usable rather than expensive.
