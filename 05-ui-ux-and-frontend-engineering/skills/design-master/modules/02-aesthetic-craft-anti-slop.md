# Module 02: Aesthetic Craft, Taste Gate & Anti-AI-Slop Manifesto

Consolidated from `frontend-design` v2, `taste-skill` 2.5, `claude-design-skill`, and `canvas-design`. This module acts as the **Mandatory Taste Filter** over `Module 01` research output, ensuring every UI, landing page, or visual prototype looks intentionally art-directed by a senior studio rather than generated from a default AI template.

---

## 0. Pre-Design Protocols (Before Placing a Single Pixel)

1. **Priority #0 — Fact Verification Before Designing:** When a brief references a real product, brand, version, or recent release you are unsure about, verify facts via official docs/search FIRST rather than designing around invented specs.
2. **Design Direction Advisor (For Vague Briefs):** When a user says "design something nice" without a clear style, **do NOT improvise generic defaults**. Propose **3 genuinely different aesthetic directions** (distinct schools, not 3 slight variations of minimalism) with 1-sentence pitch, reference archetype, 3 vibe keywords, and concrete hero treatment so the user chooses before full build.
3. **Core Asset Protocol (Assets Beat Palettes):** For branded designs, **real logos, authentic product photography, and real UI screenshots are first-class citizens**; colors and fonts are auxiliary. Missing an asset? Use an honest labeled placeholder (`[hero: real product photo]`) rather than a fake AI-drawn SVG substitute.
4. **Business-Kind Visual Gate (From `taste-skill`):**
   - **Tech / SaaS / AI / Gaming / Hardware:** Real product UI (`app-frame`), crisp pulsing/structured diagrams, controlled dark heroes, and at most **1 signature shader/WebGL effect** where earned.
   - **Physical Places & Local Businesses (Cafes, Bakeries, Clinics, Shops, Restaurants, Agencies):** **Lead with authentic photography, flat clean grounds, crisp typography, and real service details.** NEVER put sci-fi shaders, cyberpunk glows, dark SaaS dashboards, or decorative WebGL scenes on a local shop, clinic, or cafe.
   - **Physical Products:** Show the product BIG and whole (never shrunk inside a tiny grey rounded box on a grey background); show a new authentic angle per section; never repeat the same photo twice; **no explanatory captions under hero/editorial photos**.

---

## 1. Visual Direction & Planning Before Coding

Before writing a single line of CSS/markup, explicitly lock down 5 concrete aesthetic decisions:
1. **Aesthetic Personality:** Name a distinct, domain-authentic visual world (e.g., *editorial monochrome journal*, *Swiss precision instrument*, *warm tactile roastery*, *dark high-contrast gaming control room*, *quiet optical atelier*) — NEVER "modern clean SaaS".
2. **Compact Signature Palette:** Commit to a crisp 4–6 token palette (`canvas`, `surface`, `ink`, `muted`, `accent`, `border`) using `oklch()` or exact verified brand hexes, with **1 dominant mood + 1 sharp accent** rather than timid, evenly distributed rainbow colors.
3. **Typography Contrast:** Pair an expressive, characterful display typeface with a refined, ultra-legible body typeface (in Persian: e.g., `Gramaphone` + `Ravi`, `Anjoman` bold/regular contrast, `Peyda`/`PelakFA` display + `Vazirmatn` body). Keep body line lengths `< 80ch` and apply `text-wrap: pretty` / `text-wrap: balance`.
4. **Spatial Composition:** Break predictable identical-card monotony using **one section per screen rhythm**, equal left/right content edges, asymmetrical splits, strong typographic grids, purposeful negative space, or crisp hairline borders (`1px solid`) instead of heavy drop-shadow boxes everywhere. Limit card nesting to **2 boxes deep max**.
5. **One Orchestrated Motion Moment:** Design **at most 1–2 high-impact moments** (e.g., clean hero entrance on load + quiet hover micro-feedback: card lift `2px`, photo zoom `1.02–1.03` inside frame, button press) rather than sprinkling generic fade-in-on-scroll wrappers on every section.

---

## 2. The Anti-AI-Slop Blacklist (Strictly Forbidden Defaults)

Actively reject these cliché telltale patterns unless the user or an existing `brand-*` skill explicitly demands them:

- **Cliché Default Palettes (5 Modern AI Tells):**
  - Do NOT default to warm cream `#F4F1EA` + terracotta/warm-clay `#D97757` on every editorial page.
  - Do NOT default to generic purple/violet/lavender SaaS gradients on white backgrounds.
  - Do NOT default to near-black `#0B0B0B` + bright acid-green/vermilion cyberpunk glow plastered across dark screens.
  - Do NOT default to fake broadsheet zero-radius hairline grids or identical rounded SaaS cards with identical `rgba(0,0,0,.1)` shadows on every brief.
- **Cliché Typographic & Layout Chrome:**
  - NO tracked-out `ALL-CAPS` eyebrow pills (`✨ REVOLUTIONIZING X`) stamped above every heading.
  - NO highlighting a single random word in every headline in italic/accent color as a lazy tic.
  - NO meta strings compulsively joined with middle dots (`A · B · C`), `WORD — fragment` labels, or `→` appended to every single link/button.
  - NO generic 3-column rounded-white-card feature grids with gradient icon circles or left-border accent stripes on every card.
  - NO decorative `01 / 02 / 03` oversized ghost numbers unless the content is genuinely an ordered sequence.
  - NO filler dummy sections, lorem ipsum, invented stats, or fake testimonials to pad empty space.
- **Cliché Motion Noise:**
  - NO fade-and-slide-up scroll animations on every card, row, or section (`animate-on-scroll` fatigue).
  - NO tilt cards, auto-advancing carousels, timed tabs, parallax on body text, or scroll-jacking.
  - NO distracting infinite pulsing/bouncing badges (anything moving > 5s needs a pause control; respect `prefers-reduced-motion`).

---

## 3. UI Microcopy & Editorial Discipline

Visual craft breaks immediately if copy feels robotic — words are interface architecture, not decoration:
- **User Perspective Over System Jargon:** Write what the user does ("مدیریت اعلان‌ها", not "کانفیگ وب‌هوک"). Keep headings concrete with real nouns (<= 8 words).
- **Consistent Active-Voice Verbs:** CTAs state exact outcome ("ذخیره تغییرات" / "Save changes", not "Submit" / "Click Here"). Keep identical vocabulary across the whole flow: button **"Publish"** -> toast **"Published"**.
- **Specific Over Generic:** Replace placeholder fluff ("Elevate your workflow", "Seamless solutions", "بهترین تجربه برای شما") with real domain nouns, concrete constraints, and verifiable outcomes.
- **Constructive Error & Empty States:** Errors explain what broke and how to fix it (no fake apologies, no vague "Something went wrong"); empty states invite a clear first action.

---

## 4. Mandatory 2-Pass Self-Critique Protocol

Never ship the first aesthetic draft unchecked. Run a fast Pass-2 critique (and inspect in a real browser whenever available):
1. **The Squint Test:** Blur your eyes — is there an unmistakable primary focal point, clear 3-level hierarchy, equal left/right edges, and calm visual breathing room?
2. **The Subtraction Test (Chanel Rule):** Before shipping, remove 20% of unnecessary borders, shadows, eyebrows, badges, or wrapper boxes to make the design sharper and more confident.
3. **The Swap Test:** If you swapped the brand logo for a random startup, would the layout look generic? If yes, tighten typography scale, layout rhythm, and domain-specific photography/detail until it unmistakably belongs to THIS product.
4. **The Contrast, A11y & RTL Check:** Verify WCAG 2.2 contrast (`Module 08`), touch targets `>= 44px` (`Module 09`), zero horizontal overflow at `320px/390px/768px/1440px`, and natural Persian RTL flow.
