---
name: "research-data-charts"
description: "Build social-ready charts from buyer research in a brand palette: small-multiples trend charts with a projected quarter, two-panel bar charts, and a clean header and footer."
---

# Research data charts

Use when someone wants a chart from buyer or customer research for LinkedIn, a deck or a report ("make a graph", "chart this", "over time", "in our brand colours").

## Works with

- **Takes in:** tagged shares and trends from call-research-trend-analysis, or any table of research figures, plus the brand palette.
- **Produces:** social-ready PNG charts.
- **Next:** founder-pov-concepts and social posts that quote the same figures.

## Process
- **Before you build:** read a general data-viz skill first if one is installed.
- **Build:** use matplotlib and render a PNG.
- **Check:** look at the PNG yourself before sending it.
- **Deliver:** save it to the user's chosen folder with a dated file name, e.g. `<YYYY-MM-DD>-<name>-chart.png`.

## Palette
Ask for the brand palette, or find it in the brand or design docs. Map it to these roles:
- **Background:** a light neutral, with dark text and a muted secondary text colour.
- **Gridlines:** very light.
- **Accent:** the one point the chart makes, such as the top bar or rising lines.
- **Default:** a calm mid-tone for other bars and flat lines.
- **Falling lines:** a dark tone, so falls read as "down" rather than "bad".
- **De-emphasised:** a pale tone for a deliberately small or contrarian bar.

Check that text colours meet 4.5:1 contrast on the background, and never use the accent for small text. No em dashes anywhere in chart text.

## Header and footer
- **Title:** big and bold (about 42pt on a 23-inch-wide figure), in plain words, e.g. "How buyers' fears are changing" or "What's on buyers' wishlist".
- **Credibility line (dark text, about 17pt):** the scale of the research in a professional tone, e.g. "Based on 300+ conversations with [audience] and 2,700+ emotional moments captured in our buyer research." Only mention sources the chart actually uses.
- **Measure line (secondary text, about 15pt):** what is measured and the period, e.g. "Percentage of conversations in which each theme was raised, [year]. Change reflects the first three quarters; the last is projected."
- **Footer, two short lines only:** the colour key, then "Source: [Company] buyer research".
- **Leave off:** raw call or company counts, method notes, and anything like "biggest rises first".

## Small-multiples trend chart
Use one small line chart per item in a 5-column grid, sorted by change (biggest rise first). It reads better than a dumbbell chart for 10 to 20 items.

**Each panel:**
- An optional small caps tag above, e.g. FEAR or FRUSTRATION when two types share a chart.
- The bold item name.
- A big coloured change figure ("+11 pts"), with "7% → 18%" beside it.
- The line: solid with markers across the full quarters, then a dashed segment to an open-circle point labelled "[Qn] proj." with its value printed beside it. The projection method is in the call-research-trend-analysis skill.

**Colour by change:**
- Accent if the item rose by the threshold or more.
- Dark tone if it fell by the threshold or more.
- Default tone otherwise.
- Thresholds: 5 points for share-of-companies charts, 2 points for mix charts (shares that add to 100%).

**Layout:**
- Use the same y-axis on every panel (0/30/60%, or 0/10/20% for mix charts), with light gridlines and no spines.
- Size the figure at about 23 × 19 inches for 4 rows, or 23 × 15.5 for 3 rows.
- Make each panel about 72% of its column width and 44% of its row height, so titles never touch the axis labels of the row above.
- **Centre the grid:** after rendering, measure where the non-background pixels start and end, then shift the panels until the left and right margins match within a few pixels.

## Two-panel bar chart
Use this for pairs like fears vs frustrations or problems vs hopes.
- **Bars:** horizontal and sorted. The top bar is in the accent, the rest in the default tone, and a deliberately small or contrarian bar in the pale tone.
- **Headings:** each panel has a bold heading and a one-line subheading, e.g. "88% voiced at least one".
- **Values:** print percentages at the bar ends, with no x-axis.
- **Takeaway:** optionally add one line above the footer, written as a plain finding with no "X, not Y" antithesis.

## Iterating
- Expect fast, small rounds of edits: spacing, wording, colours.
- Keep the chart script in a working folder so each change is a one-line edit: re-render, look, deliver.
- Keep the previous version available, because the user may say "go back".
- If a requested change would mislead (for example, making falling lines look like they rise), say so and offer an honest alternative before building.
- After each delivery, reply in one or two lines with what changed.

## Shared conventions

- Find inputs in the workspace first: the files other skills in this set produce (capability baseline, buyer research, VOC library, evidence docs, customer proof files, dossiers, matrices, approved claims). Ask only for what's missing. Never fill a gap with assumptions about the company.
- Never invent a capability, stat, quote or competitor fact. Quotes are verbatim; named customer material stays internal until the customer signs off.
- Claim tags are SAFE, NEEDS VERIFY: (what settles it) or INTERNAL ONLY. Keep the tags you receive and pass them on.
- The user's own writing rules and brand voice override the defaults in this skill.
