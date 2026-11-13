# Naming conventions and the creative learning log

Two artifacts that have to exist before launch, because neither can be applied retroactively.

---

## 1. Naming

The point is not tidiness. The point is that the interesting question is **which argument won**, not which ad won, and that question can only be answered if performance can be grouped by angle and by format across campaigns and quarters.

If naming is inconsistent, every quarterly review reduces to "this specific ad did well", which teaches nothing that transfers.

### Convention

```
Campaign:  {brand}_{stage}_{objective}_{YYYY-QN}
Ad set:    {audience}_{geo}_{bid}
Ad:        {conceptID}_{angle}_{format}_{variant}
```

| Token | Values |
|---|---|
| `brand` | A short code per product line, plus one for campaigns covering all of them, e.g. `CORE`, `AI`, `ALL`. Record your codes in `creative-strategy/references/inputs.md` |
| `stage` | `TOFU`, `MOFU`, `BOFU`, `RTG`, `ABM` |
| `objective` | `awareness`, `engagement`, `traffic`, `leadgen`, `conversions` |
| `audience` | Short slug matching the saved audience name exactly |
| `geo` | `UK`, `EU`, `US`, `INTL` |
| `bid` | `maxdel`, `costcap`, `manual` |
| `conceptID` | `C1`, `C2`, matching the creative brief |
| `angle` | Slug from your angle library (template in `creative-strategy/references/angle-library.md`), e.g. `switchcost`, `datatrust`, `capacity`, `triggerevent` |
| `format` | `simg`, `carousel`, `doc`, `video`, `tla`, `conv`, `spotlight` |
| `variant` | `a`, `b`, `c` for executions of the same concept |

```
CORE_MOFU_leadgen_2026-Q3
  opsleads-50-500_UK_costcap
    C2_datatrust_simg_a
    C2_datatrust_simg_b
    C4_capacity_doc_a
```

Rules that matter more than the format itself:

- **The angle slug is the load-bearing token.** It must match the angle library exactly. A typo silently splits an angle's performance history in two.
- **Never rename a live ad.** Reporting joins on the name. Renaming orphans the history.
- **Same concept, same conceptID, forever.** Including refreshes. A refresh is `C2_datatrust_simg_c`, not a new concept ID. That is how fatigue-versus-bad becomes answerable later.
- **UTMs mirror the ad name.** `utm_content={conceptID}_{angle}_{format}_{variant}` so CRM-side analysis can group the same way the platform does.

### Pre-launch checklist

- [ ] Naming applied to campaign, ad set and every ad
- [ ] Angle slugs match the angle library exactly
- [ ] UTMs mirror the ad names
- [ ] Conversion action confirmed firing
- [ ] View-through and click-through windows noted for the report
- [ ] Self-reported attribution field live on the destination form
- [ ] Learning log entry opened for every concept

---

## 2. The creative learning log

Wherever `creative-strategy/references/inputs.md` says it lives. Append-only, dated. One entry per concept that goes live.

`creative-strategy` opens the entry at launch. This skill closes it when the result lands. An open entry with no result after its review date is itself a finding: something launched and nobody looked.

### Entry shape

The example below is illustrative: the product, audience and every figure are invented to show the shape, not drawn from any real account.

```markdown
## C4 · capacity · document ad · [product line]
**Opened:** YYYY-MM-DD   **Closed:** YYYY-MM-DD
**Brief:** [filename of the creative brief]
**Ad names:** AI_TOFU_engagement_2026-Q3 / opsleads-200-2000_UK_costcap / C4_capacity_doc_a

**Hypothesis**
Operations leaders will engage with a scoped account of what the automated work
actually covers, because the objection we keep hearing is control rather than
capability.
Falsifiable: if dwell sits at or below the account baseline, the argument is not
the draw and the format is not carrying it.

**Judged on:** dwell time and engagement rate. Explicitly not CPL.

**Ran:** [start] to [end], $[spend], [N] impressions

**Result**
Dwell well above the account baseline (state both figures). Engagement rate
(state it). A few dozen landing page views and a handful of demo requests.
Below the conversion volume floor, so no CPL read and none claimed.

**What it taught us**
About the angle: the capacity argument held attention above baseline across two
audiences. Supports promoting it from Untested to Winner on engagement evidence,
not on conversion evidence. Say which.
About the format: document ads earn dwell that single image does not. Worth
testing a second angle in the same format before concluding it is the format.
Confounded: the audience was also new this round. Not a clean read.

**Angle status:** Untested → Winner (engagement evidence only)
**Next:** C4 variant b, same angle, single image, to separate angle from format.
```

Every figure in a real entry carries its volume and its window. A dwell time without impressions behind it is not a result.

The two fields that carry the value:

- **What it taught us about the angle**, separately from what it taught us about the ad. An ad result is worth one decision. An angle result is worth every future brief.
- **Confounded.** Write down what else changed. Almost every real test has one. Recording it stops a contaminated result being cited as clean evidence a year later.

---

## 3. Closing the loop into the angle library

Your angle library (location in `creative-strategy/references/inputs.md`) holds status per angle per product line. Update it in the same pass as the log entry.

| Status | Means |
|---|---|
| `Untested` | Identified, evidenced, never run |
| `In test` | Live, no read yet, with a review date |
| `Winner` | Beat account median on its stated metric, with the metric named |
| `Retired` | Failed, or ruled out. **With the reason written down** |

Two disciplines.

**Name the evidence type in a Winner.** "Winner on engagement" and "winner on cost per SQL" are different claims and get used differently in the next brief. An angle promoted on engagement evidence should not be cited later as proven on pipeline.

**Always write the retirement reason.** A retired angle without one gets proposed again within two quarters by someone who was not there, and there is no way to tell whether it failed on the argument, the execution, the audience, or a landing page that has since been rebuilt. The reason is what makes retirement a decision rather than a gap.

---

## 4. Promoting a result into a pattern

Two or three independent wins on the same format or structure stops being a result and becomes a house pattern.

Record promoted patterns at the top of the learning log, and reference them from the next brief so new concepts start there rather than rediscovering them. This is the actual mechanism by which a creative programme improves: **test result → recorded learning → codified pattern → default input to the next brief.** Without the promotion step, a team accumulates a long log and the same hit rate it started with.

Independent means different angle, different audience, or different quarter. The same concept winning twice in a row is one win observed twice.

Review the promoted patterns quarterly, and demote any that stop holding. A pattern that was true at one budget or one awareness state does not automatically survive a change in either.
