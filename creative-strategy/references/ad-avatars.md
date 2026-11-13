# Ad avatars: the person the ad is actually addressed to

An ad avatar is not an ICP and not a sales persona. Your team probably has both already, and reaching for them here is the most common way this step goes wrong.

| Artefact | Answers | Lives in |
|---|---|---|
| **ICP** | Which companies should we sell to at all | Your ICP and buyer-persona documents, per `inputs.md` |
| **Sales persona** | Who is in the room, what they care about across a whole cycle | The same documents, plus any persona template your team keeps |
| **Ad avatar** | Which argument, in whose words, to a person in a specific state of knowing, scrolling a feed | Your avatar library, built and refreshed by the `ad-avatars` skill |

The ad avatar is narrower, more behavioural, and disposable in a way the other two are not. It exists to make one decision. A sales persona that says "cares about compliance" is fine for a call plan and useless for a hook, because it does not tell you what the person would actually say out loud.

---

## 1. Build pain-first, not persona-first

The standard order is: pick a persona, then list their pains. Invert it.

**Step 1. Name the pain and desire territories the research actually evidences.** Not the ones the product addresses. The ones buyers describe unprompted, in the buyer research and the voice-of-customer material listed in `inputs.md`.

**Step 2. Map which avatars hold each territory, and how each one experiences it differently.** Personas are secondary here: they are different working contexts experiencing the same pain.

The mapping is many-to-many. One pain runs across several avatars. One avatar carries several pains. **Every pain × avatar cell is a distinct creative opportunity**, because the same pain argued to a different seat is a different argument, not a reworded one.

Why this order and not the other: a persona-first list produces demographic messaging, and demographic messaging is vague. "AI for operations teams" is a category statement. "You are the help desk, and it is in your DMs" is an argument. The second one came out of a pain territory, not out of a job title.

**Anchor choice.** Default to pain-first. Desire-first is the exception, for a claim with no acute functional problem behind it. Those cases are real but narrow: a trust-through-visibility argument, or an ambition framing your register requires you to lead with. Note which anchor an avatar's set is built on, because it changes what the hook is allowed to open with.

---

## 2. The field set

Eleven fields. The standing avatar library carries them in this order and a new avatar is not finished until each one is either filled or explicitly marked as unevidenced.

1. **Avatar label** plus a one-line working context. Give it a name a person would recognise across three meetings. A vivid working label travels; "Persona 2B" does not.
2. **Who this is in targeting terms.** Job function, seniority, title patterns, company-size band, geography, and any firmographic or trigger signal. **State explicitly where a field is not selectable in Campaign Manager.** This is where most avatar work quietly fails: the most predictive attribute is often the one you cannot buy.
3. **Role in the buying committee.** Champion, economic buyer, technical gatekeeper, blocker, end user.
4. **The pain they own**, and how this avatar experiences it differently from the others holding it. The second half is the field that earns its keep.
5. **Deepest want**, in their terms rather than yours.
6. **What they will doubt.** Objections, most likely first.
7. **Trigger moment**, and whether it is targetable.
8. **Likely awareness states**, and in which audience you would find them there. An avatar is usually problem-aware cold and product-aware in retargeting, and those are two different ads.
9. **Verbatim language.** Two to five exact quotes with source and consent tag.
10. **What not to say to them.** The framings the research shows fall flat.
11. **Evidence tier**, with the account count stated.

### The fields that carry the most weight

**Field 2, honestly filled.** The attribute that best predicts an avatar is frequently the incumbent system they already run, and that attribute is not selectable on LinkedIn. Writing that down is what forces the real conversation: either buy install-base data and run it as a Matched Audience company list, or accept that the targeting is broader than the research supports and let the creative do the qualifying. Which brings us to:

**Field 4 and the demographic call-out.** When targeting cannot reach the avatar, the first line of the ad can. Naming the audience in the copy ("Finance leads at 200-person companies:") is the cheapest qualifier available and it belongs to the creative layer, not the targeting layer. See `hooks-and-mechanics.md`.

**Field 10.** Almost nobody keeps this and it is the field that stops a retired framing coming back in six months. Record where each entry came from. Until there is paid-performance history, entries are built from buyer-stated rejections and register rules rather than from measured creative failure, and that is a weaker basis. Say which when you cite it.

---

## 3. Where the content comes from

Nothing in an avatar is authored. Retrieval and sorting only.

| Field | Pull from |
|---|---|
| Pain, how experienced, verbatim | Buyer-context research, voice-of-customer and pain language, the pain bank |
| Deepest want | Buyer interests and aspirations research |
| Objections | Competitor dossiers and their deal-intelligence sections; verification tracker gap rows |
| Trigger moments | The pain bank's trigger bucket; any pipeline pain synthesis |
| Committee seat, firmographics | The ICP and persona documents |
| Frequency ranking | Any already-ranked pain synthesis |

`inputs.md` lists the documents this skill expects you to supply, and what each one is for.

If a field has no source, write `No evidence found in current research` and move on. A thin avatar with real evidence beats a rich invented one, and the empty fields are what the next research pass is for.

---

## 4. Consent, which is not optional here

Everything from call recordings, cold calls, win/loss or a named customer is **INTERNAL USE ONLY** unless the source doc records explicit sign-off. Assume internal until the sign-off is written down somewhere you can point at.

The tag travels with the quote into the avatar, into the brief, and stops at the ad. An internal-only quote can shape an angle, sharpen a hook and sit in the brief's evidence section under its banner. It cannot be the ad. Where a brief needs both, build the two tiers separately per your brand and voice rules and never blend them.

The practical consequence is worth stating out loud in any brief that hits it: a competitor can run named logos with hard numbers in the same feed you are running unattributed claims in. That is a consent problem, not a creative one, and creative cannot fix it.

---

## 5. Using avatars in a run

**Scoping.** Name the avatars in scope in Step 0 of the workflow. One to three. A brief addressed to "leaders" is addressed to nobody.

**Read to the job.** The library gets large. Every run reads the territory index and the gaps section; only the avatars in scope get read in full. Structure the file by avatar ID so one can be pulled without loading the others.

**Concepting.** Each concept names one avatar and one awareness state. Not a list of two or three, one. A concept that would work for any avatar is a category statement, and it will test as noise.

**Coverage check before you cut.** Lay the surviving concepts against the avatar list. If every concept aims at the champion seat, the set cannot move a deal that stalls at the gatekeeper or the signer, which is where B2B deals actually stall. This check is in the brief template's set-quality section and it is the one most often skipped, because a champion-only set always looks coherent.

**Then run the same check on the library itself.** Where a seat appears inside several pain rows as the person who anchors the decision but has no evidenced avatar of its own, every set built off the library speaks to the champion and not the signer. Name that seat in the brief rather than letting it pass, because it is a research gap with a creative consequence.

---

## 6. Maintaining the library

The avatar library compounds. Dated additive entries, never a rewrite.

Add or revise an avatar when: a buyer-research sweep surfaces a new territory or a new seat; a test result contradicts a stated objection or a "what not to say" entry; a segment brief invents an avatar on the fly, in which case it gets promoted into the library at the end of the run rather than evaporating.

Two staleness rules. An avatar whose evidence is older than roughly two quarters gets its tier reviewed, not automatically kept. An avatar with no verbatim language is a hypothesis with a name, and should be labelled as one.

Retire rather than delete, with the reason and the date, so the reasoning survives the avatar.
