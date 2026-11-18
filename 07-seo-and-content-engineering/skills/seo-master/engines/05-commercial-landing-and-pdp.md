# Engine 05: Commercial Landings, Category Pages & WooCommerce PDPs

Use this engine for writing high-converting transactional and commercial Persian copy: WooCommerce product pages (PDPs), dual-intent B2B/B2C category pages, wholesale landings, and high-trust service landing pages. Load target `brand-<project>` skill first for verified store policies, guarantees, orthography, and URLs.

---

## 1. Track A: Two-Part WooCommerce Product Description (PDP)

### Critical Guardrails (Anti-Hallucination & Anti-Boilerplate)
1. **Verify SKU Specs Before Stating:** Never invent technical specs (`CAT`, `UV400`, `Polarized`, `Made in Italy`, raw mm dimensions, frozen-vs-fresh status, marinade ingredients) unless explicitly supplied. Log omitted unverified specs cleanly in a QA checklist when requested.
2. **Prevent Variant Cannibalization:** When two SKUs share one model code, embed the exact color/variant code inside the Focus Keyword, SEO Title, Meta Description, and H2 #1.
3. **Prevent Boilerplate Fatigue Across Large Catalogs:** Differentiate every SKU along 5 concrete axes: (1) Exact physical/material/anatomical build, (2) Real usage/wardrobe/culinary scenarios, (3) Verified craft/prep nuance, (4) Honest stock/fresh-vs-frozen/flash-photo caveats, (5) Contextual cross-sell links (pair companion SKUs & parent category symmetrically).

### Blueprint 1: Standard E-Commerce PDP (Short + Full)
* **Short Description (Above Add-to-Cart — `60–120` words):** Crisp scannable verdict + `4–5` fast spec bullets (type/cut/material, primary use case, fresh/authentic/prep status, verified store guarantee) — never bury the Add-to-Cart button.
* **Full Description (Below Fold — `300–600` words):** Detailed fit/texture/performance explanation, practical usage/care/storage tips, companion cross-links, and `3` SKU-specific buyer FAQs.

### Blueprint 2: Luxury / Branded Two-Part PDP (Product + Brand Heritage)
1. **Section 1 — `بخش ۱: توضیحات محصول` (`~440–485` words):**
   * Intro paragraph with exact Focus Keyword in Sentence 1 (sensory + design summary, zero hype).
   * `## طراحی و استایل [نام محصول]` (silhouette, color depth, suitability, relative scale — do NOT robotically repeat raw WooCommerce spec-table numbers).
   * `## متریال / ساختار و مشخصات` (only verified materials/origin/specs).
   * `## مناسب چه کسانی و چه موقعیت‌هایی` (`1–2` symmetric category links).
   * `## خرید از [نام برند]` (verified shipping/installments/returns/authenticity caveats + homepage/brand archive links).
2. **Section 2 — `بخش ۲: درباره برند` (`~305–360` words):**
   * Grounded strictly in **3-Tier Brand Heritage Source Hierarchy**:
     * **Tier 1 (Wins all conflicts):** Official brand heritage / parent-group releases (e.g., Prada Group, Trussardi Heritage, De Rigo, LVMH/Thélios, Kering Eyewear, EssilorLuxottica).
     * **Tier 2:** Reputable trade journalism (Optometry Today, MIDO, VisionPlus, Optical Journal, Vision Monday).
     * **Tier 3 (Disallowed):** Competing retail shops, affiliate blogs, or unverified legacy SEO copy.
   * Tie brand heritage directly to THIS SKU's exact design DNA + natural internal navigation links + `2–3` primary external source links.
3. **SEO Metadata & 4 Angle Image `alt`s:** Title (`<=60c`), Meta (`<=155c`), and 4 distinct descriptive `alt` tags (front, 3/4 detail, side/material, top view) + QA Checklist (`ادعاهای حذف شده`, counts, orthography pass).

---

## 2. Track B: Dual-Intent Category & Commercial Hub Pages

### Two-Zone Layout (Mobile Conversion Protection):
* **Zone 1 — Above the Product Grid (`80–150` words MAX):**
  * Clean H1 matching commercial + geographic intent.
  * `2–3` crisp sentences positioning category variety, key quality differentiators, and verified local trust — keeping WooCommerce product cards or live `[price_table]` immediately visible on mobile screens!
* **Zone 2 — Below the Product Grid (Read-More Buyer Guide — `600–1,200` words):**
  * Practical buyer comparison across variants/cuts/origins *inside* this category so unsure shoppers click the right SKU.
  * Dual-intent balance when relevant: **B2C angle** (home usage, sensory/practical tips) + **B2B angle** (wholesale supply, consistency, bulk inquiry).
  * `3–6` high-intent commercial FAQs synced word-for-word with `FAQPage` JSON-LD (Engine 07).
  * **De-Bloat Rule:** Never dump 3,000+ words of encyclopedic blog essays here — summarize overlapping informational topics in 1 paragraph and link OUT to dedicated blog guides!

---

## 3. Track C: Pure B2B Wholesale & High-Trust Service Landings

* **B2B Tone Calibration:** `45%` Technical/Operational Specs (batch consistency, capacity, tolerances, quality control) | `30%` Applied Economics (margin stability, operational efficiency, real workflow) | `15%` Consultative (tasting/testing, expert review, custom sizing/formulation) | `5%` Comparative (direct factory/roastery/lab vs middlemen) | `5%` Mild Commercial (MOQ, logistics SLAs, transparent terms). Zero poetic fluff or fake urgency (`فقط امروز!`).
* **Service Landing Blueprint:**
  1. **Direct Feasibility + Honest Caveat Opening:** Confirm immediately that the service/online order works cleanly, then name the exact technical caveats buyers must respect (builds instant authority over pushy competitors).
  2. **Transparent Step-by-Step Operational Flow (`3–5` numbered steps):** Show real human/expert verification, laboratory/factory accountability, and realistic turnaround expectations.
  3. **Objection & Technical Clarity Table:** Demystify confusing buyer parameters (e.g., prescription fields `SPH/CYL/PD`, MOQ/pricing tiers, cut/material criteria) + common buyer mistakes.
  4. **Verified Infrastructure Proof:** Ground trust strictly in verified physical assets/labs/factories/logistics from `brand-<project>`.
  5. **Grounded Conclusion + Checkout-Anxiety FAQ (`4–6` Qs):** Resolve real purchase hesitations cleanly without fabricating delivery speed or fake guarantees.
