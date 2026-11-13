# Visualising a concept

Turning an angle into something a person can react to, before anyone spends design hours on it.

The whole discipline is **fidelity control**. Concept stage is disposable, cheap and plural. Brief stage is one locked direction with real copy and full spec. Production is the file. Skipping to high fidelity at concept stage is the most common failure, and its cost is specific: the conversation moves to typography and away from whether the argument is any good.

---

## 1. The ladder

| Stage | Fidelity | Made with | Purpose |
|---|---|---|---|
| **Wireframe** | Layout zones, exact copy, no styling | The notation below, written in the doc | Is the argument clear, is there one idea, does the copy fit |
| **Concept render** | Grayscale or rough visual, real copy in place | `assets/ad-mockup.html`, AI image for scene backgrounds | Show three to five distinct directions to react to |
| **Production comp** | Real brand, final imagery, correct dimensions | Designer, or Figma template, or the mockup renderer with brand assets | The asset, or the thing the designer executes from |

Default to the wireframe. Escalate only when the concept goes outside the team, when the layout itself is the idea (a diagram, a comparison table, a permission model), or when asked.

---

## 2. Wireframe notation

Plain text, in the brief. Enough to build from, cheap enough to throw away. Zones top to bottom, exact copy in quotes, everything else described.

```
CONCEPT 3  |  Containment  |  LinkedIn single image 1200x1200  |  IT / security, product-aware

INTRO TEXT (150 visible / 600 cap)
  "Every automated action is scoped to a permission you set, and logged
   against the record it touched."                                     [99 chars]
  ...then: what it reads, what it does, where a human stays. [3 lines]

IMAGE
  ┌──────────────────────────────────────┐
  │  [top 20%]  headline, 2 lines max    │   "Read-only. Or reversible.
  │             ~48pt equivalent          │    Or ask first. You set it."
  │                                       │
  │  [middle]   4-step dial, left to      │   Read-only > Reversible >
  │             right, current step       │   Notify > Approval required
  │             highlighted               │
  │                                       │
  │  [bottom]   one line, small           │   "Every action logged against
  │             + wordmark bottom-right   │    the record."
  └──────────────────────────────────────┘
  Dark-mode safe: mid-tone background, no pure white panel.

HEADLINE (70)
  "You decide how much the system can do on its own"                   [48 chars]

CTA
  Learn more (preset)

LANDING
  /security  : matches, page leads with the permission model     [SAFE]

PROOF CARRIED
  Mechanism only. No metric. [SAFE]
```

The test of a wireframe is the same as the test of a brief: can someone who was not in the room build the intended thing. Directional adjectives fail it. "Make it feel confident" is not a specification. A locked headline, a layout, a legibility note and a dark-mode constraint is.

---

## 3. Rendering a concept set

`assets/ad-mockup.html` renders a set of concepts as LinkedIn feed previews. Edit the `CONCEPTS` array at the top of the file, set `ADVERTISER` to the brand being previewed, open it in a browser, screenshot or print to PDF.

It is deliberately plain, and it does three things worth having:

- Renders at correct aspect ratios so a 1200x1200 is judged as a square, not as a slide.
- Shows the **150-character truncation** live, with the "see more" fold in the right place. Copy that reads well in a doc and buries its hook past the fold is the single most common thing this catches.
- Toggles light and dark mode, which catches the second most common thing.

It is not a design tool. It will not make a bad layout look good. That is the point at this stage.

For anything beyond it: Figma community ad templates are component-based with swappable text layers and are the fastest path to a production comp without custom design. For many variants off one locked layout, an HTML-to-image pipeline or a templating service does it programmatically, which is the right approach for iteration briefs (same layout, new headline) and the wrong approach for new concepts.

---

## 4. AI image generation, honestly

Useful as a sketching layer. Unreliable as a typesetter.

**The text-in-image reality as of 2026.** Short headlines of roughly one to six words are now reliably legible from the better models. Full sentences, body copy, and precise brand-font matching are still failure-prone, and accuracy degrades sharply past about sixty characters. Professional workflows composite real text as a layer on top of a generated background rather than trusting the model to render copy. Do the same.

**What each is for**, with the caveat that this list dates fast:

| Need | Reach for | Weakness |
|---|---|---|
| Short bold headline treatment, poster-like | Ideogram | Degrades past a few words; weaker at photoreal |
| Iterative editing, consistency across a batch | Nano Banana Pro (Gemini image) | Less distinctive stylisation |
| Complex layouts, infographics, embedded text | GPT-Image | Slower and pricier in reasoning mode |
| Scene or background imagery, on-brand batch | FLUX | Best tier gated |
| Editable vector output for templates | Recraft | Not a text specialist |
| Commercially safest training data and indemnity | Adobe Firefly | Lower artistic ceiling |

**The trap.** An AI rough looks finished. Stakeholders anchor on it as if a decision has been made about the visual, when the only decision on the table is the angle. Keep concept-stage renders visibly rough, label them "concept only", or use the wireframe instead. Say plainly in the brief which artifacts are roughs.

**Never generate a product screenshot.** A convincing fake UI showing a state the product does not have is the exact failure mode that gets found by a journalist or a competitor calling the named customer. Use real screenshots, cropped, from a real environment.

---

## 5. Video concepts

If the concept is video, the wireframe becomes a two-column A/V table: scene number, visual (framing, on-screen text, b-roll), audio (VO or dialogue, music, SFX). Assume roughly 130 words per minute for voiceover when timing a script.

For a talking-head or testimonial-style piece, brief talking points rather than a verbatim script. Natural delivery outperforms a read, and a script produces a read.

Specify captions in the brief, not as an afterthought in production. They are mandatory on LinkedIn and they are part of the frame composition, not an overlay added later.

---

## 6. Presenting a set

Three to five directions, genuinely distinct. Not eight variations of one.

For each: the visual, then the angle in one sentence, then the hypothesis, then the evidence behind it. **Lead with the strategic rationale, not the picture.** A set presented picture-first gets reviewed on aesthetics, which is the wrong conversation and the hardest one to steer back.

Order the set by evidence strength rather than by which one you like. State what was cut and why, briefly. A set of five with three visible cuts reads as a decision. A set of five with no cuts reads as everything that came to mind.
