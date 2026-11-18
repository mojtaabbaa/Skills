# Engine 10: Technical SEO for WordPress, WooCommerce, Rank Math & Cloudflare

Use this engine whenever diagnosing or implementing technical SEO changes: crawlability, indexability, `robots.txt`, Cloudflare WAF crawler access, XML sitemaps, canonicals, 301 redirects, Rank Math breadcrumbs/duplicate meta tags, WooCommerce faceted URLs, Persian/RTL slug stability, and Core Web Vitals/DOM hygiene.

> **Mission & Evidence Rule:** Protect crawlability, indexability, URL stability, and semantic correctness. Separate display changes from URL changes, distinguish what the site emits from what Google ultimately indexes, and NEVER claim guaranteed ranking increases from a technical fix alone. Never fabricate live PHP/HTML state you have not inspected!

---

## 1. Mandatory 8-Step Technical SEO Investigation Order

1. **Scope & Canonical Host:** Identify exact domain, environment (`production`/`staging`), canonical protocol (`https://`), `www` vs non-`www`, trailing slash, and language/RTL setup.
2. **HTTP & Crawl Surface:** Inspect HTTP status codes, redirect chains/loops, response headers (`X-Robots-Tag`), `robots.txt`, `/sitemap_index.xml`, `<link rel="canonical">`, and raw rendered HTML.
3. **WordPress & Plugin Layer:** Inspect permalink structure, rewrite rules, Rank Math (or active SEO plugin) settings, active theme (`header.php`), WooCommerce, Elementor, JetEngine, and custom `wp_head` snippets.
4. **Indexation Blockers:** Check for accidental `noindex`, password protection, maintenance mode, `robots.txt` disallows, or staging indexation leaks.
5. **Raw HTML vs. Rendered DOM:** Compare `view-source:` against post-JS DOM to spot client-side metadata/schema mutation or blocked CSS/JS assets.
6. **URL Hygiene & Bloat:** Audit internal links, pagination (`/page/2/`), search (`?s=`), archive/variant paths, WooCommerce faceted filters (`?filter_*`, `?orderby=`, `?min_price=`), and duplicate encoded paths.
7. **Structured Data & Breadcrumbs:** Validate single-owner JSON-LD and visible-vs-schema breadcrumb alignment (Engine 07).
8. **Search Console Ground Truth:** Separate local technical tests from Google Search Console URL Inspection / Page Indexing evidence.

---

## 2. `robots.txt`, Crawl Controls & Cloudflare WAF

* **`robots.txt` != Deindexing / Security:** `robots.txt` controls *crawling*, NOT security and NOT guaranteed deindexing. Never use `Disallow` when deindexing is required — Googlebot must be able to crawl a page to see `<meta name="robots" content="noindex">` or `X-Robots-Tag: noindex`.
* **Never Blindly Block Rendering Assets:** Audit wildcards like `Disallow: *jet-engine*` or plugin paths — wildcards can accidentally block CSS/JS assets needed by Googlebot WRS! Verify via Search Console **Test Live URL -> Page Resources**.
* **Pagination Trap (`Disallow: */page/*`):** Blocking `/page/2/` can orphan deeper category products and blog archives unless all products load on page 1 or have alternative HTML crawl paths.
* **Cloudflare WAF & Edge vs. Origin Diagnostics:**
  * Always inspect the actual HTTP response of `https://<canonical-host>/robots.txt` (`curl -I`), NOT just the WordPress editor preview.
  * Check Cloudflare WAF, Managed Challenge, Bot Fight Mode, cache, and redirect rules whenever Search Console reports `robots.txt` fetch failures or HTTP `403`/`418`/`5xx`.
  * Compare edge response vs origin response; NEVER broadly whitelist spoofable User-Agent strings — use Cloudflare's verified-bot controls or IP/rDNS validation.

---

## 3. Canonical URLs, 301 Redirects & Persian/RTL Slug Stability

* **Preserve Slugs By Default:** NEVER change a live permalink/slug just to fix a visible display label or translation!
* **Canonical Rules:** Canonical is a *hint*, not a redirect. Ensure self-referencing canonicals match exact protocol, host, trailing slash, language path, and pagination (`/page/2/` -> canonical `/page/2/`). Never canonicalize substantially distinct pages to a category root.
* **URL Migration Protocol:** When an approved URL change is required, create a 1-to-1 `301` redirect map, update all internal links and sitemaps, eliminate redirect chains/loops, and keep redirects active long-term.
* **Persian Percent-Encoding Consistency:** Ensure UTF-8 Persian slugs (e.g., `/قیمت-محصول-نمونه/` vs percent-encoded equivalents, and historical quirks like `-2` suffixes or spelling typos) canonicalize consistently with trailing slash matching Rank Math sitemaps.

---

## 4. Rank Math Diagnostics: Breadcrumbs & Duplicate `<meta name="description">`

### A. Breadcrumb Presentation Label Without Changing Slug
* When changing a visible breadcrumb label (e.g., changing `"Blog"` -> `"بلاگ"` while keeping `/category/blog/` untouched):
  1. Modify ONLY the presentation label via Rank Math's supported filter (`rank_math/frontend/breadcrumb/items`) or taxonomy display mapping.
  2. Preserve the underlying term slug, permalink, canonical URL, and hierarchy.
  3. Confirm BOTH visible breadcrumb HTML AND `BreadcrumbList` JSON-LD match verbatim across singular posts, archives, products, and CPTs.

### B. Duplicate `<meta name="description">` Triage Protocol
When `view-source:` shows 2+ `<meta name="description">` tags:
1. Check line placement relative to `<!-- Search Engine Optimization by Rank Math ... -->`.
2. Isolate the second emitter: theme/child-theme `header.php`, custom `wp_head` snippet (WPCode / `functions.php`), JetEngine/Elementor SEO toggle, or secondary OG/SEO plugin.
3. **Clean Fix:** Remove/disable the duplicate raw `<meta>` output and hook custom overrides cleanly into `rank_math/frontend/description` filter (test on staging with backup first!).

---

## 5. XML Sitemaps & WooCommerce Indexation Policy

* **Sitemap Hygiene:** Confirm `/sitemap_index.xml` and child sitemaps return HTTP `200` + XML content type, include ONLY indexable canonical URLs (no `noindex`, redirects, private, preview, or staging URLs), and maintain accurate `lastmod` timestamps (never update every URL's `lastmod` on every request).
* **WooCommerce Crawl Policy:**
  * Explicitly define indexation for: Products (`index`), Variations, Categories/Brands (`index`), Facet Filters/Sort Parameters (`?orderby=`, `?min_price=`, `?filter_*`, `?rating_filter=`, `?s=` -> `noindex,follow` or crawl-controlled), Cart/Checkout/My-Account/Add-to-Cart (`noindex` + disallow `?add-to-cart=`).
  * Ensure product canonicals, out-of-stock visibility policy, and `Product` JSON-LD `Offer` state agree with visible DOM pricing.
  * For multilingual sites (WPML/Polylang), verify reciprocal `hreflang` alternates and language-specific canonicals.

---

## 6. Technical SEO Audit Report Template & Acceptance Tests

```markdown
## Scope & Evidence
- Domain / Environment / Date:
- Stack (WP / Theme / Builder / SEO Plugin / CDN):
- Evidence Sources (`curl -I`, `view-source:`, GSC URL Inspection):

## Crawl, Canonical, Sitemap & Schema Findings
| Priority | Area | URL / Pattern | Evidence | Root Cause | Proposed Fix | Rollback Plan |
|---|---|---|---|---|---|---|
```

### Mandatory Acceptance Tests Before Sign-Off:
- [ ] Canonical URL is unique, self-consistent, and matches trailing slash/HTTPS.
- [ ] `robots.txt` returns HTTP `200` on canonical host without WAF challenge or accidental asset blocks.
- [ ] XML sitemap contains canonical indexable URLs only; zero `noindex`/redirected leaks.
- [ ] Zero duplicate `<meta name="description">` tags or duplicate JSON-LD schema blocks.
- [ ] Breadcrumb HTML and `BreadcrumbList` JSON-LD agree without altering underlying slugs.
- [ ] Zero redirect chains or loops; WooCommerce faceted/cart/search URLs obey crawl policy.
- [ ] Baseline recorded, staging tested, and rollback plan documented before production deploy.
