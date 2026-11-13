# Competitor creative teardown

How to find out what competitors are actually running, record it in a way that compounds, and turn a pile of ads into a positioning decision.

Two things to hold onto before starting.

**No ad library exposes performance for ordinary commercial ads.** Not spend, not CTR, not conversions. Anyone who tells you a teardown reveals what is working is selling something. What you get is longevity and repetition, which are hypothesis signals. Say so every time.

**The teardown is internal analysis.** Most B2B register rules forbid characterising other vendors in customer-facing copy, named, unnamed, or positively. Where yours does, that constraint stands here too: the teardown informs what you say. It never becomes what you say.

---

## 1. Pulling the ads

### LinkedIn Ad Library

The primary source, because it is where you advertise.

```
https://www.linkedin.com/ad-library/home
```

No login required. Search resolves to a LinkedIn **Page**, not free text, so you cannot keyword-search ad copy across advertisers. Search the company name, select the right Page, then filter in the sidebar by country, date range, ad format and language.

Company Page URLs follow `https://www.linkedin.com/company/<slug>`. Take the competitor set and their Page slugs from the competitor dossiers the user supplies, per `inputs.md`, and mark any slug you had to guess as unverified. Confirm the Page is the real corporate one and not a regional or careers Page before recording anything against it.

What it gives you:

- Full creative: image, video, carousel, document. Ad copy. Advertiser Page. Format. Countries served.
- **EEA-served ads only** carry an extra transparency layer under the DSA. **Verified live on 26 Aug 2026 against a B2B SaaS ad served in Germany.** What the ad-detail page actually shows:

  | Field | What you get |
  |---|---|
  | Advertiser and **payer** legal entity | Named in full, down to the legal suffix of the paying entity |
  | Ran from / to | Exact dates. This is your longevity signal, and it is better than a "started running" date |
  | Total impressions | A bucket, e.g. `< 1k` |
  | Impressions by country | Percentage split per country |
  | Language | **Named values**, e.g. "Targeting includes English" |
  | Location | **Named values**, including exclusions, e.g. "includes Germany, excludes Poland, France" |
  | Audience / Demographic / Company / Education / Job / Member Interests and Traits | **A tick or a dash only**, in a Targeted and an Excluded column. Whether the category was used. Not what was selected inside it. |

  **Do not overstate this, which is easy to do because every secondary write-up does.** You learn that a competitor targeted by Job and by Company and excluded on both. You do not learn which job titles, which seniorities, which industries or which headcount bands. There is no expandable row and no deeper view. Only Language and Location carry named values.

  What it is still good for, and it is worth the browser tab: the payer entity, exact run dates, a country split, and a **shape read** on how they buy. An advertiser ticking Job and Company but not Member Interests is running a firmographic buy, not an interest buy. One ticking Audience is running matched or saved audiences, which usually means an ABM list. Exclusions on Job and Company mean deliberate suppression, which is a more mature setup than most. That is real intelligence about method. It is not their targeting sheet.
- No spend, anywhere.

Hard limits worth knowing before you promise a historical analysis: ads are indexed from **1 June 2023** onward only, and each ad drops out roughly **one year after its last impression**. There is no deep archive. A competitor's 2022 strategy is not recoverable here.

### Meta Ad Library

Relevant now for competitor intelligence, and it becomes the primary source if and when you open Meta.

```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=<PAGE_ID>&search_type=page
```

Search the brand at `facebook.com/ads/library`, select the Page from autocomplete to resolve `view_all_page_id`, then set `country`, `ad_type=all` for standard commercial ads, and `active_status` to `active`, `inactive` or `all`.

Each ad card shows a **"Started running on"** date. That is the longevity signal. Browsing the full active set for a Page gives you the variant count. Coverage reaches back years, far deeper than LinkedIn.

There is an Ad Library API, but for non-political commercial ads it returns `impressions_index: -1` and no spend field, so it buys you bulk retrieval and nothing else. Not worth the app registration for a handful of competitors.

### Google Ads Transparency Center

Worth a pass when a competitor runs heavy search and you want to see the paid landing pages behind their positioning.

```
https://adstransparency.google.com/advertiser/{ADVERTISER_ID}?region={REGION}
https://adstransparency.google.com/advertiser/{ADVERTISER_ID}/creative/{CREATIVE_ID}?region={REGION}
```

Advertiser IDs are prefixed `AR`, creative IDs `CR`. Search by **domain** rather than name: name search collides with agencies and resellers. Only verified advertiser accounts appear, and different domain variants show as separate entities. "Why you're seeing this ad" surfaces targeting hints. No spend or impression data.

**Retention is the trap here.** Commercial ads are retained for roughly 30 days outside the EU, and a year inside it. There is no historical archive for a non-EU search campaign, so a Google teardown is a snapshot of right now and needs re-pulling rather than citing from three weeks ago. Google is also moving to disclose who actually pays for an ad, which is worth checking for agency-run competitors.

### Coverage at a glance

| Library | Exposes | API | Retention | Targeting disclosure |
|---|---|---|---|---|
| LinkedIn | Creative, copy, advertiser and payer, format, countries, exact run dates | None | Indexed from 1 June 2023; drops ~1 year after last impression | EEA only. Language and Location named; Job, Company, Audience, Demographic, Education, Interests as tick-or-dash only |
| Meta | Creative, copy, page, run dates, platforms | Yes, but returns no performance for commercial ads and stops at the EU border | Active ads globally; EU 1 year | EU demographic breakdowns only |
| Google | Creative, verified advertiser, format, regions, last shown | No general API | ~30 days commercial, 1 year EU | Region, essentially nothing |
| TikTok | Creative, advertiser, dates, targeting, viewer counts | Application-gated, rarely approved for competitive research | 1 year after last shown | EU countries, includes real targeting |

Note also that Meta stopped selling political and social-issue ads in the EU in late 2025, so that archive is historical rather than live. It does not affect commercial teardowns.

### Running the pull

Drive a browser automation tool. Check what tabs are already open, open a new tab rather than reusing one, and work one competitor at a time.

1. Navigate to the library and search the competitor Page.
2. Filter to the relevant country and the last 90 days by default.
3. Read the page, then screenshot each distinct ad. Save into a dated folder in your swipe file, one file per ad, named `<competitor>-<n>.png`.
4. For LinkedIn, check the EEA view separately and capture the targeting disclosure where present.
5. Record each ad against the field list below as you go, not afterwards. Untagged context decays within the hour.

Do not click anything that could open a modal or a confirm dialog. If the browser tool stops responding after two or three attempts, stop and say so rather than retrying. Falling back to asking the user for screenshots is a fine outcome and much cheaper than a stuck session.

### Third-party tools: the answer is worse than expected

Checked again in August 2026, and the earlier note in this file was too generous. The position now:

| Tool | LinkedIn coverage |
|---|---|
| **Foreplay** | None. No LinkedIn integration at all. |
| **Motion** | Meta and TikTok. Its library and its benchmark data are Meta and TikTok. |
| **AdSpy** | None. Meta and Instagram only. |
| **BigSpy** | Unstable, with data gaps. Not reliable for systematic work. |
| **adlibrary.com** | Full LinkedIn coverage, including spend ranges and ad history. Mid-market pricing. |
| **Pathmatics / Sensor Tower** | Yes, including LinkedIn. Enterprise pricing only. |

Ahrefs and Semrush cover paid **search** only, no social creative.

Two consequences.

**The two tools the performance-creative world is built around do not cover this channel.** Any workflow borrowed from DTC creative strategy that assumes a Foreplay-style swipe pipeline does not run on LinkedIn. Yours has to be the native library plus a maintained swipe file, done by hand, which is exactly why the swipe file compounding matters so much.

**No third party can surface LinkedIn's first-party targeting parameters.** LinkedIn does not expose them in its API, so a paid tool can show format, duration and estimated spend and never job function or company size. The EEA disclosure on LinkedIn's own library is the only route to that data at any price. If your team is considering buying a tool, that is the caveat to lead with.

---

## 2. Recording each ad

Fixed fields. Same every time, so the swipe file stays queryable across runs.

| Field | What to capture |
|---|---|
| Date recorded | The run date |
| Competitor | Page name as it appears |
| Platform and format | LinkedIn single image / video / carousel / document / thought leader / text; Meta feed, story, reel |
| Core claim | The one-sentence promise, in their words |
| Angle | Mapped to `angle-library.md`, or a new territory named |
| Awareness stage targeted | Unaware / problem / solution / product / most aware |
| Persona addressed | Who the copy and visual speak to |
| Offer and CTA | Demo, trial, calculator, report, webinar, pricing |
| Proof used | Named customer, logos, metric, review badge, analyst, none |
| Visual style | Product screenshot, UGC or talking head, illustrated, data-viz, meme, quote card, comparison table |
| First seen / days running | From the library's date stamp |
| Variant count | How many live executions carry this same core claim |
| Landing page | URL, and whether it is a homepage, a dedicated campaign page, or a comparison page |
| EEA targeting disclosure | Job function, seniority, industry, geography, where available |
| Screenshot | Filename |
| Note | Anything that does not fit. Especially: does this contradict what their dossier says they lead on |

That last one earns its place. A competitor whose ads argue something different from what their dossier says they sell is either repositioning or testing, and both are worth knowing early.

---

## 3. Clustering

Do not analyse ad by ad. Analyse claim by claim.

1. **Group every ad by its core claim, ignoring execution.** Forty ads across a set of competitors typically collapse to a couple of dozen real arguments, and often to fewer than ten per competitor. Most brands run very few actual angles and many executions of each.
2. **The collapse ratio is itself a finding.** A competitor with twenty ads and two claims has found something and is scaling it. A competitor with twenty ads and fifteen claims is still searching, or is spending brand budget with no thesis.
3. Name each cluster in the angle vocabulary from `angle-library.md`. If a cluster does not map, that is a new territory: name it, define it, and add it to the library.

---

## 4. Share-of-voice grid

Angles as rows, competitors as columns. Mark which competitors are running which angle, and how many live ads each has behind it.

```
                          Comp A  Comp B  Comp C  Comp D  Comp E  Comp F   Read
Consolidate the stack       ●●●     ●       ●●      ●●●     ●●      ·      saturated
Speed to value              ●●      ●●      ·       ●       ·       ·      contested
Risk and compliance         ·       ·       ●●●     ●       ●●●     ●●     saturated (EU)
AI that acts                ●       ·       ·       ●       ·       ●      contested, moving
Data you cannot trust       ·       ·       ·       ●       ·       ●      open
Containment / permissions   ·       ·       ·       ·       ·       ·      open
```

Read it three ways:

- **Saturated** (three or more): buyers have learned to discount this. Not forbidden, but it must be carried by proof nobody else has, or it is wallpaper.
- **Contested** (one or two): winnable if your proof is stronger or your mechanism is more specific.
- **Open** (zero): a candidate. Only a candidate.

Then run the two questions that matter more than the grid itself.

**What does everybody claim with no evidence behind it?** A claim made across the field with no proof attached is a credibility gap. Making the same claim *with* real proof is often stronger than finding a new claim, because the buyer already believes the claim matters and has stopped believing anyone about it.

**What is open because it is worthless?** Empty is not the same as valuable. Before pursuing open space, find it in your own buyer research. If buyers do not talk about it unprompted, the space is empty because nobody wants it.

---

### Staleness: date every read, and mean it

A share-of-voice read is a measurement, and it decays. One territory in a standing angle library flipped from **open to contested between two pulls on the same day**, because the second pass found four advertisers the first missed. If a read can move that much in an afternoon, an undated read quoted in a brief three weeks later is a liability rather than evidence.

Three rules:

- **Every grid carries the date it was pulled and the countries covered.** A grid without both is not citable.
- **A read older than 30 days gets re-pulled, not cited.** A read between 30 and 90 days can be cited as context with its date stated. Older than 90 days is history.
- **State the pull depth.** How many advertisers, how many ads each, which filters. A shallow pull that found nothing is not the same finding as a deep pull that found nothing, and the first one is what produced the open-to-contested flip.

## 5. Detecting likely winners

Two signals, both weak, both worth using because they are all there is.

- **Longevity.** An ad running 30, 60, 90, 120 days without being killed suggests it is paying for itself, because losers get pulled fast. Confounders: brand campaigns run on schedule regardless of performance; some teams simply do not prune; an always-on evergreen ad may be running out of neglect.
- **Variant repetition.** The same core claim across four or five executions and formats suggests a found angle being scaled, not a blind test. This is the stronger of the two signals, because it implies a decision was made.

Combine them. A claim that is both long-running and heavily varied is the best available hypothesis about what is working in the category. Then say the word hypothesis out loud in the brief. It goes into your test queue as a prioritised guess, not as a proven pattern to copy.

---

## 6. Reading strategy from the mix

Beyond individual angles, the shape of a competitor's creative portfolio tells you what they think they are doing.

| What you see | What it usually means |
|---|---|
| Many long-lived ads on one narrow angle | A working wedge. Assume it is defended and priced accordingly. |
| Many short-lived ads across many angles | Still searching for positioning, or spending brand budget with no thesis |
| Heavy comparison and "vs" creative | They see a specific rival as the primary alternative in-market. Check whether it is you. |
| Sudden format shift (static to document, brand handle to thought leader) | A channel-level bet, often after a hire or an agency change |
| Persona-split creative running in parallel | A mature buying-committee strategy. Worth matching. |
| Heavy EEA targeting disclosure concentrated on one function and one seniority band | Confirms the ICP they are actually buying, which is often narrower than their website suggests |
| Nothing at all in the library | They may be running organic and outbound only, or Page-level targeting is off. Note it rather than assuming absence of spend. |

---

## 7. Positioning against, once you have the grid

The grid tells you where the lanes are. Three rules decide whether to drive into one.

**Sort competitors into three tiers first.**

- **Status quo**: the spreadsheet, the manual process, the incumbent system nobody has got round to replacing, the headcount they would hire instead, doing nothing. This wins more deals than any named vendor and almost nobody advertises against it.
- **Active consideration set**: who actually appears on your shortlists, per the deal intelligence in the competitor dossiers the user supplies, see `inputs.md`.
- **Phantoms**: who could compete and does not show up in deals. Do not position against them. Naming a phantom in an ad teaches the market that an alternative exists, at your expense.

**Naming a competitor in an ad.** Works when you are the credible challenger to a known incumbent, when the viewer is already comparing (bottom of funnel, retargeting, comparison-intent), and when the point of difference is provable. It backfires when the claim cannot be substantiated, and when the competitor is much larger, where a direct callout legitimises them more than you.

**The constraints on comparative creative are usually tighter than the law's**, and the tightest of them are your own:

1. Many B2B brands prohibit characterising competitors in customer-facing copy, named or unnamed. Where yours does, most conventional "vs" formats are unavailable and you state your own strength positively instead. If a genuinely comparative ad is wanted, that is a decision to escalate to whoever owns the register, not one to make inside a brief. Apply the swap test to every customer-facing line: insert "our competitors" as the silent subject and see whether the sentence still works. If it does, it is out.
2. Register rules commonly also forbid dunking on competitor reviews or paraphrasing their negative reviewer language. Check yours before a conquest angle reaches for either.
3. A competitor pain-to-feature mapping, where the user supplies one per `inputs.md`, will often carry explicit "shared gap, do not use as a differentiator" callouts. Those are precisely the claims a conquest angle reaches for first.

On top of that: LinkedIn's ads policy has no dedicated comparative clause, but its trademark and deception rules apply. Naming a competitor in text is generally tolerated when factual and non-confusing. Using their **logo** is the highest-risk move because it implies affiliation. Unverifiable superlatives are the most common rejection trigger. Under US law truthful, substantiated comparative advertising is protected, but the substantiation has to exist before the ad runs, and competitors monitor exactly these ads. Keep a dated screenshot of any competitor claim being compared against, because their pricing and features change and your ad can go stale into a false claim.

---

## 8. Closing the run

Append a dated section to your swipe file containing: the date range and countries covered, which competitors were pulled and which could not be, every ad recorded against the field list, the claim clusters, the share-of-voice grid as at today, and the white-space read with its buyer-research corroboration.

Note explicitly what you could not see: competitors with no ads in the library, non-EEA campaigns with no targeting disclosure, anything that dropped out of the one-year window. A teardown that quietly omits its blind spots reads as complete when it is not.

If the run surfaces something that belongs in a competitor dossier rather than a swipe file, a genuine positioning shift rather than a creative one, flag it for whoever maintains the dossiers rather than editing the dossier here.
