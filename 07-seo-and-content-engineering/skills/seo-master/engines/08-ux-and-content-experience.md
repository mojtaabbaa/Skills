# Engine 08: UX & Content Experience Analysis (Mobile-First Persian RTL)

Use this engine when auditing why a page, draft, category grid, price hub, or blog article has weak engagement, poor mobile readability, conversion friction, or when specifying lightweight interactive SEO/UX tools. Load target `brand-<project>` skill first.

> **Non-Fabrication Rule:** Never invent numeric bounce rates, conversion percentages, heatmap stats, or PageSpeed LCP/CLS scores unless the user provides live PageSpeed/analytics data or HTML.

---

## 1. Mobile-First Persian RTL Audit Heuristics (`360px` Baseline)

1. **First-Screen Satisfaction (`0–5` Seconds Above the Fold):**
   * **Category Hubs / Price Hubs (`Time-to-Grid` / `Time-to-Price`):** Does intro text exceed `80–130` words and push WooCommerce product cards or live `[price_table]` below the first mobile screen?
   * **Product PDPs (`Buyer Confidence Above Fold`):** Can a mobile shopper immediately see exact specs, honest status (fresh vs frozen, authentic guarantee, sizing/fit cues), and an unobstructed Add-to-Cart button?
   * **Blog Articles (`Direct-Answer Pacing`):** Is the core question resolved in lines `1–3` without a slow storytelling wall?
2. **Visual Scannability & Cognitive Fatigue:**
   * Flag prose walls exceeding **2–3 lines** without a list, table, or callout break.
   * Flag stacked headings (`H2 -> H3` with zero introductory direct answer).
   * Flag wide 4+ column tables that squash into 1-word vertical columns on `360px` phones -> require short crisp headers + responsive horizontal scroll (`overflow-x: auto`).
3. **Elementor Widget & Promo Embed Restraint:**
   * Overloading a ~1,800–2,000w article with `5–7+` mid-article promo banners or product carousels fractures reading flow, inflates DOM depth, and slows mobile scroll.
   * Cap mid-article contextual `[elementor-template]` / product embeds to **2–3 high-relevance placements** (plus 1 focused pre-conclusion E-E-A-T/CTA block) unless a project's `brand-*` skill specifies an exact dual-linking cadence.
4. **Commercial Archive UX Standards:**
   * Push out-of-stock (`ناموجود`) SKUs to the bottom of brand/category grids; sort by Popularity (`محبوب‌ترین`) rather than Newest when newest items are out of stock; lazy-load product thumbnails after card #8 so expanding grids (e.g., to 36 items) does not hurt mobile LCP.
   * Place quick-access horizontal scrollable `<a href>` anchor chips directly under H1 with reserved container height (`CLS = 0`).
   * Convert fake bold `<p>` subsections in Elementor into semantic `<h2>`/`<h3>` widgets.

---

## 2. Lightweight Interactive Shortcode / Calculator Engineering Spec

Whenever recommending an interactive UX/SEO tool (e.g., face-shape advisor, symptom checklist, sizing/ratio calculator) inside WordPress/Elementor:
1. **Zero Heavy Frameworks:** Pure semantic HTML, CSS, and vanilla JavaScript **`< 5 KB`** loaded with `defer` (no jQuery dependency or React/Vue bundle bloat).
2. **Server-Side Indexable HTML:** All questions, checkbox/input `<label>`s, and explanatory text MUST render in initial server PHP shortcode HTML so Googlebot indexes them natively.
3. **Zero Layout Shift (`CLS = 0`):** Reserve a fixed minimum height on the result box ahead of user interaction.
4. **Strict Privacy:** Execute calculations strictly client-side in browser memory (`no form submit`, `no DB storage` of health/biometric PII). At most fire anonymous GA4 tier events (`green|orange|red`).
5. **Accessibility & RTL QA:** Real `<input>` + `<label>` pairings, `inputmode="decimal"` for numeric fields, full keyboard navigation (`Tab`/`Space`), `aria-live="polite"` on result container, RTL mobile testing (iOS/Android), and before/after PageSpeed Mobile `LCP`/`CLS` check.

---

## 3. Prioritized UX Audit Deliverable Format

Group findings cleanly into three actionable tiers:
* **P0 — Critical (Conversion / Intent / Trust Killers):** Out-of-stock dominance, buried prices/Add-to-Cart, broken trust cues, severe mobile overflow, unverified misleading promises.
* **P1 — Important (Readability & Engagement Friction):** Walls of text, missing early comparison tables, Elementor embed fatigue, fake `<p>` headings, unclear category navigation.
* **P2 — Polish (Visual Rhythm & Micro-Copy):** Chip height `CLS`, alt text refinement, minor label clarity, spacing rhythm.
* Explicitly route copy rewrites to Engine 04/05 and PHP/CSS/DOM code fixes to Engine 10.
