# Engine 07: Commercial & Technical FAQs and JSON-LD Structured Data

Use this engine when authoring visible FAQ sections paired with JSON-LD structured data, or designing/auditing `FAQPage`, `CollectionPage`, `BlogPosting`, `BreadcrumbList`, `Product`, and `LocalBusiness`/`Store` schemas on WordPress + WooCommerce + Rank Math. Load target `brand-<project>` skill first for exact orthography (`ZWNJ` vs `Zero-ZWNJ`) and verified business facts.

---

## 1. Universal Structured Data Golden Rules

1. **Strict Word-for-Word Parity Rule:** Every single Question (`name`) and Answer (`acceptedAnswer.text`) inside `FAQPage` JSON-LD MUST match the visible on-page HTML text **100% word-for-word** (same orthography, zero hidden promotional copy, zero discrepancies).
2. **One Primary Owner — ZERO Duplicate Schemas:** Never emit two `FAQPage`, two `BreadcrumbList`, or two `Article`/`BlogPosting` graphs on the same URL.
   * If Rank Math FAQ Block emits `FAQPage`, do **NOT** paste a second manual `<script type="application/ld+json">` block! Use manual JSON-LD strictly as a fallback when Rank Math FAQ Block is not used or fails to emit.
   * If the active theme and Rank Math both print `BreadcrumbList`, log a technical task to disable the theme's duplicate breadcrumb schema and keep Rank Math as the single owner.
3. **Zero Fabricated Schema Properties:** NEVER fabricate ratings (`AggregateRating`), review counts, prices, stock availability, unverified phone numbers (e.g., incomplete landlines), unverified opening hours, or unverified branch URLs inside JSON-LD.
4. **Dynamic Templates Belong in PHP/Rank Math (Not Static Elementor Text):** `CollectionPage` + `ItemList` on brand/category archives MUST be populated dynamically from page-1 visible products via Rank Math/theme code — NEVER hardcoded statically inside Elementor text widgets.
5. **Product Schema vs. Price Table Sync:** Ensure WooCommerce `Product` `Offer.price`, `priceCurrency` (`IRR` / normalized Toman), and `availability` (`InStock`/`OutOfStock`) match live visible prices and any custom `[price_table]` shortcode. Do not emit installment-only or display-only numbers as the canonical offer price.

---

## 2. Commercial + Technical FAQ Authoring Pattern
Effective money-page/category FAQs combine two mandatory halves (`4–6` concise Qs total, `1–2` crisp sentences per answer):
1. **Technical / Buying Clarity Qs (`2–3` Qs):** Answer real shopper confusions (standards, sizing/fit, material/cut differences, authentic vs fake).
2. **Commercial Trust Qs (`2–3` Qs):** Answer exact checkout anxieties using ONLY verified store guarantees from `brand-<project>` (authenticity warranty, shipping carriers & exact delivery window, free-shipping threshold, exchange/return rules, installment options).

---

## 3. Verified Copy-Ready JSON-LD Blueprints

### A. `FAQPage` (Manual Fallback Only — Check Orthography Per `brand-*`!)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "متن دقیق سوال منطبق با متن قابل مشاهده صفحه",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "متن دقیق پاسخ منطبق با متن قابل مشاهده صفحه بدون متن مخفی تبلیغاتی."
      }
    }
  ]
}
</script>
```

### B. `BlogPosting` Contract (Rank Math / Custom Graph Reference)
* Required fields: `@type: "BlogPosting"`, `@id: "<url>#article"`, `headline`, `description`, `mainEntityOfPage`, `image`, `datePublished`, `dateModified` (sync with `<meta property="article:modified_time">`), `inLanguage: "fa-IR"`, `author` (`Organization` or verified named `Person`), `publisher` (`Organization` with verified logo), `articleSection`, and optional `citation: [...]` array of verified clinical/authority URLs.

### C. `CollectionPage` + `ItemList` Contract (Brand / Category Archives)
* Required fields: `@type: "CollectionPage"`, `url`, `name`, `description`, `inLanguage: "fa-IR"`, `isPartOf: { "@id": "<home>#website" }`, optional `about: { "@type": "Brand", "name": "..." }`, and `mainEntity: { "@type": "ItemList", "itemListElement": [ { "@type": "ListItem", "position": 1, "url": "<product-url>" } ] }`.

### D. Unified `@graph` Anchoring (`LocalBusiness`/`Store` + `WebSite` + `WebPage`)
* Connect entities cleanly via consistent `@id` anchors (`#organization` / `#store`, `#website`, `#webpage`) rather than emitting isolated orphaned JSON-LD blocks.

---

## 4. Mandatory Post-Publish Validation Checklist
Always append/verify these 4 checks after deploying any schema:
1. **Google Rich Results Test** (`https://search.google.com/test/rich-results`): `0` errors, `0` duplicate schema blocks.
2. **Schema Markup Validator** (`https://validator.schema.org/`): Valid `@context`, `@type`, `@id`, and clean Persian UTF-8 strings.
3. **Visible Parity Check:** Visible breadcrumb trail and visible FAQ text match emitted JSON-LD verbatim.
4. **Link Hygiene Check:** Every `url` / `citation` starts cleanly with `https://` without leading spaces, double `http://`, or `?utm_source=`.
