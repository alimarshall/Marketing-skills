---
name: chatgpt-ads
description: Run and optimise B2B campaigns on ChatGPT Ads (OpenAI Ads Manager): account setup, tracking, campaign structure, context hints, ad copy, bidding, weekly performance reads, keep or kill calls and monthly competitor checks. Use when the user says "set up ChatGPT ads", "write context hints", "new ChatGPT ad group", "why is this ad not delivering", "weekly ChatGPT ads read", "should we keep ChatGPT ads" or "what are competitors running on ChatGPT". Draws concepts and claims from creative-strategy, checks copy with copy-register-check and claim-verification, and hands test design and result reads to creative-testing.
---

# ChatGPT Ads operator

Use for anything on ChatGPT Ads: new ads or ad groups, context hints, bids and budgets, tracking, weekly performance reads, keep or kill calls, and checks on what competitors are running.

## Inputs

Read `company-context.md` first (repo root, or search the workspace for it) and use the fields that apply to this skill. If the file or a line is missing, ask once, then offer to save the answer back to it. Never fill a gap with an assumption about the company. If `creative-strategy/references/inputs.md` is also filled in, it still applies; where the two differ, `company-context.md` wins.

Record your own paths in `creative-strategy/references/inputs.md`. This skill needs:

- **Operator playbook:** `<fill in>` (your own running notes on this channel: platform facts as you last verified them, your thresholds, what you have learned).
- **Current campaign brief:** `<fill in>` (latest version; covers the ads, lanes, waves and claim status).
- **Approved-claims list and capability baseline:** `<fill in>` (including the baseline's list of contradicted or retired claims).
- **Competitor creative swipe file:** `<fill in>`.
- **Creative learning log:** `<fill in>` (the one `creative-testing` maintains).
- **CRM where pipeline quality is judged:** `<fill in>`.
- **Your thresholds:** conversion-campaign trigger `<fill in>`, day-90 stop rule `<fill in>`, comparison channel for cost per qualified demo `<fill in>`.

## Read first

1. The operator playbook.
2. The current campaign brief.
3. For any new copy, also read the `creative-strategy` skill's brand and claim rules, the capability baseline's contradicted list, and the latest approved-claims list.

Platform facts change fast. Anything below marked **(verify against current OpenAI Ads docs)** is a platform detail that was true when this skill was written and may have moved. Before relying on a spec, limit or feature, re-check the OpenAI help centre's ChatGPT Ads collection and the OpenAI Ads developer docs. When something has changed, update your playbook with the date.

## How the channel works

- **The auction.** A relevance-weighted auction (described publicly as second-price; verify against current OpenAI Ads docs). Inputs are the conversation, the landing page, the title, the copy and the context hints. Relevance matters as much as bid.
- **No reports on where ads ran.** There is no search-term or conversation report (verify against current OpenAI Ads docs). You cannot see the prompts that triggered an ad, so hints, landing pages and downstream quality are the only levers you can read.
- **Who sees ads.** Only users on the free and lower-priced consumer tiers; paid business, enterprise and education tiers do not see ads (verify against current OpenAI Ads docs). This matters for B2B: some of your buyers are on plans that never see ads.
- **Inventory by market.** Inventory has been thin in some markets since launch, and early public B2B tests were weak. Check delivery in your market before committing budget, and be ready to add a larger market if yours is thin.

## Setup rules

- **One account per brand.** Currency and time zone are locked at setup (verify against current OpenAI Ads docs), so choose them deliberately.
- **Tracking.** Use the Pixel and the Conversions API (CAPI) together, deduplicated by event ID.
  - Fire a scheduled-appointment event on demo booked (this is the event to optimise to) and a lead event on form submit. Use the platform's standard event names (verify against current OpenAI Ads docs).
  - Capture the platform's click reference parameter and pass it through CAPI (verify the parameter name against current OpenAI Ads docs).
  - CAPI accepts only recent events, a short window of days (verify against current OpenAI Ads docs). Qualified-lead and pipeline quality are therefore judged in your CRM, never in Ads Manager.
- **Attribution.** 30-day click, view-through off. Keep it conservative; you cannot see placements, so view-through credit is unverifiable.
- **UTMs.** `utm_source=chatgpt`, with the campaign ID and ad ID macros (verify macro syntax against current OpenAI Ads docs). Keep "ChatGPT ad" as a separate how-did-you-hear option from "AI assistant", or self-reported attribution will blur paid with organic AI discovery.
- **Crawlers.** Landing pages must allow the OpenAI ads crawler and should allow the OpenAI search crawler (verify current user-agent names against OpenAI docs). Use one stripped page per ad group whose headline matches the ad.

## Structure rules

- **Campaigns.** One per brand × region × objective. Objectives cannot be edited (verify against current OpenAI Ads docs), so a new objective means a new campaign. There is a minimum daily budget per campaign, and daily spend can overshoot the daily budget (verify current figures against OpenAI Ads docs).
- **Ad groups.** One theme per ad group, with 3 to 8 hints each.
- **Ads.** 2 to 4 ads per ad group, each a different argument, not a reword. Rewords teach you nothing.
- **Before building.** Write everything in a doc first, because there are no drafts. Ads cannot move between groups. Any creative edit restarts review, so batch edits weekly (all verify against current OpenAI Ads docs).
- **Custom audiences.** Inclusion lists need a large minimum matched size (verify against current OpenAI Ads docs), which most B2B lists will not reach. Use them as exclusions instead: current customers and open opportunities.
- **Negative phrases.** Check whether the account has them yet. If it does, block adjacent categories you do not serve and buyer segments outside your ICP (for example a small-business tier you do not sell to).

## Context hints

- **Form.** Natural phrases, one idea each, naming role, company stage and situation. Never keyword lists, never delivery instructions, never exclusions (they do not work as targeting).
- **Situations.** Favour choosing and recommendation situations ("choosing a [category] tool that...") over how-to. Public testing suggests they draw ads more often; treat that as direction only for B2B.
- **Length.** Keep hints short. Very long hint text has been seen to kill delivery.

## Copy rules

- **Specs** (verify against current OpenAI Ads docs).
  - Title: a short character range with a hard limit; aim for the middle of it.
  - Body: a hard character limit around 100; aim well under it.
  - Image: a minimum square size, common formats (JPEG, PNG, WebP). Export larger than the minimum.
  - Show a character count on every line you draft.
- **Claims.** Mark every claim [SAFE] or [NEEDS VERIFY]. Use only approved claims or public case-study wording, paraphrased at the same specificity. No invention and no conflation. Run `claim-verification` on anything not already on the approved list.
- **Trademarks.** OpenAI allows only trademarks you own or are authorised to use (verify against current OpenAI Ads policy). Never put "ChatGPT" in copy, and do not name other vendors in ads without clearance. Images must not imitate the ChatGPT interface.
- **House rules.** Check every line against your house register rules and run `copy-register-check`. Never characterise other vendors in copy.
- **Lanes against the main competitor.** Look at what your main competitor actually runs on the channel (from the monthly check below), then pick lanes they are not in. A pattern that works:
  - named proof in the title or copy, where they run generic claims
  - a concrete differentiator they lack, stated as what the buyer can do
  - segment qualifiers (company size, stage) in the hints only, not the copy
  - stay out of adjacent-category prompts you do not serve
  - Recheck that competitor's dossier regularly: a lane built on their gap dies the day they close it.
- **AI product lanes.** If you sell an AI product, always name an action it takes, never just an answer it gives; the reader is already inside an assistant that can "just answer". Check which lanes are open and which a competitor already owns before committing a group to one.

## Bidding

- **Launch.** Optimise for clicks (CPC) with a manual max bid. Start at a modest bid, raise it in small daily steps until the budget spends, and stop at a cap you set in advance. Hold for two weeks before judging.
- **Moving to conversions.** Once you have a minimum number of demo-booked events in a 30-day window (set your own threshold; OpenAI publishes none as far as this skill knows, so verify against current OpenAI Ads docs), open a Conversions campaign. Run it alongside the Clicks campaign for two weeks before pausing the old one.

## Weekly read

Report per ad group: impressions, CTR, average CPC, spend, demo-booked events, CRM demos, ICP-graded demos, plus one note on what changed.

| Symptom | Likely cause | Fix |
|---|---|---|
| No impressions after 24h | Bid too low (the platform warns below a floor; verify against current OpenAI Ads docs), hints too narrow, or in review | Raise bid, broaden hints, check review |
| CTR well under your market benchmark | Hints matching the wrong conversations | Rewrite hints before copy |
| Clicks but no demos | Landing page or offer mismatch | Match headline to ad, cut navigation, check form |
| Demos but wrong size or segment | Hints pulling out-of-ICP or adjacent-category conversations | Tighten hints, add negatives, exclude customers |
| Platform clicks far above analytics sessions | Tracking gap | Check pixel, click reference, consent |

Record your market CTR benchmark in the playbook once you have one; do not borrow another market's.

**Checkpoints:**

- **Day 30:** creative read. Add a larger market if delivery in yours is thin.
- **Day 60:** pipeline read in the CRM.
- **Day 90:** keep or stop. Stop if ICP-graded demos account-wide are below the floor you set at launch. Keep if cost per ICP demo is at or below your comparison channel's. Set both rules before launch, not at day 90.

Hand the read itself to `creative-testing` when the question is whether an ad is winning or fatigued.

## Competitor checks (monthly)

- **Where to look.** Public ChatGPT ad libraries (third-party trackers have appeared; verify which are current and reliable) under your category and its adjacent categories. Note how many cards each page shows, so you know whether you have seen everything.
- **Access.** Do not create accounts on the user's behalf. Some advertiser creatives and gap lists are login-gated, so ask the user to sign in if they are needed.
- **Logging.** Record findings in the swipe file with the date.
- **Lane check.** Recheck the main competitor's dossier for any change to the gap your lanes depend on.

## After every change

Log new ads and their hypotheses in the creative learning log. Update the brief's version note, and the playbook (with a date) if a platform fact changed.
