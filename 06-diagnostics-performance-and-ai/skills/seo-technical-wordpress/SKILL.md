---
name: seo-technical-wordpress
description: Diagnose and implement technical SEO for WordPress, WooCommerce, Rank Math, structured data, breadcrumbs, canonical URLs, robots.txt, XML sitemaps, indexing, multilingual and RTL sites. Use when changing crawlability, metadata, schema, internal navigation, URL rules, or search-engine diagnostics.
---

# SEO & Technical WordPress

## Mission

Protect crawlability, indexability, URL stability, and semantic correctness while implementing technical SEO changes. Separate display changes from URL changes and distinguish what the site emits from what search engines ultimately index. Never promise ranking outcomes from a technical change alone.

## Known historical user requirements and incidents

- A Rank Math breadcrumb request required changing the visible breadcrumb label from “Blog” to “بلاگ” without changing the underlying slug.
- Cloudflare WAF/rules were associated with a Search Console robots.txt access problem in one historical incident.
- Rank Math and breadcrumb/schema customization have appeared in prior work.
- The user has worked with Persian and English content, RTL/LTR layouts, and WordPress sites with multiple page builders/themes.

These are historical details. Verify the current SEO plugin, URL structure, robots response, Cloudflare rules, sitemap output, and Search Console state before reusing a remedy.

## Technical SEO investigation order

1. Identify the exact domain, environment (production/staging), canonical host, protocol, and language setup.
2. Inspect HTTP status, redirects, response headers, robots.txt, XML sitemap, canonical tags, and rendered HTML.
3. Inspect WordPress permalink settings, rewrite rules, Rank Math (or other SEO plugin) settings, and relevant theme/plugin filters.
4. Check for `noindex`, password protection, maintenance mode, robots disallow rules, and accidental staging indexability.
5. Compare rendered source with DOM after JavaScript to detect metadata or structured data altered client-side.
6. Check internal links, pagination, archive/search pages, product variants, faceted URLs, and duplicate paths.
7. Validate structured data and breadcrumb hierarchy.
8. Use Google Search Console evidence to distinguish crawl, indexing, enhancement, and ranking issues.

## Robots.txt and crawl controls

- `robots.txt` controls crawling, not access security and not guaranteed deindexing.
- Do not block CSS/JS resources required to render important pages without evidence and risk analysis.
- Do not use robots disallow as a substitute for `noindex` when the requirement is deindexing; the crawler must be able to fetch a page to see its meta/header noindex directive.
- Check the actual HTTP response, not just the file visible in the WordPress editor.
- Confirm the file is available on the canonical host and returns a successful status without authentication, challenge page, or unexpected redirect.
- Inspect Cloudflare WAF, managed challenge, bot protection, cache, redirect, and transform rules where they could affect verified crawlers.
- Do not broadly whitelist user-agent strings; validate IP/rDNS or use provider-supported verified-bot controls where appropriate.

## Canonical URLs and redirects

- Preserve existing permalink/slug unless a URL change is explicitly requested and approved.
- A canonical tag is a hint, not a redirect and not a guaranteed indexing command.
- Ensure canonical points to the intended indexable URL with correct protocol, host, trailing slash, language path, and pagination strategy.
- Avoid canonicals to unrelated pages or category roots for substantially distinct content.
- If a URL must change, define a one-to-one 301 redirect map, update internal links and sitemap, check chains/loops, and retain old URLs long enough for migration.
- Do not change taxonomy slugs to fix a breadcrumb label.

## Breadcrumbs and Rank Math

When only the visible breadcrumb name needs changing:
- Change the presentation label through the SEO plugin's supported filter or taxonomy/name mapping.
- Preserve the underlying term slug, permalink, canonical URL, and hierarchy.
- Inspect both rendered breadcrumb HTML and `BreadcrumbList` JSON-LD.
- Ensure the visible trail and schema trail agree.
- Test singular posts, archives, products, product categories, and custom post types separately.

Historical example: “Blog” should display as “بلاگ” while the slug remains unchanged. Do not generalize that display label or target slug to every site.

## Structured data

- Use one primary owner for each schema entity/type when possible; avoid duplicate or contradictory JSON-LD from theme, Rank Math, WooCommerce, and custom code.
- Validate required fields, identifiers, URLs, images, offers, currency, availability, and relationships against the actual page.
- Product schema must reflect real product/variation pricing and stock state; do not publish an installment or display-only price as the canonical offer unless it is truly the offer represented.
- Breadcrumb schema must represent the visible hierarchy and valid URLs.
- Do not fabricate ratings, review counts, price, availability, author data, or business details.
- Test rendered JSON-LD using current official validation tools; distinguish syntax validity from eligibility for a search feature.

## XML sitemaps and indexation

- Confirm sitemap index and child sitemaps return expected status and content type.
- Include only canonical, indexable URLs intended for search.
- Exclude noindex, redirected, duplicate, private, preview, and staging URLs as appropriate.
- Do not submit huge parameterized/faceted URL spaces without a crawl strategy.
- Check lastmod accuracy; do not update every URL's lastmod on every request.
- Verify multilingual alternate relationships and language-specific canonicals where WPML or another multilingual plugin is present.

## WooCommerce-specific considerations

- Define indexation policy for products, variations, categories, brands, attributes, filters, sort parameters, cart/checkout/account pages, and internal search.
- Avoid index bloat from faceted filters and arbitrary parameter combinations.
- Ensure product canonical and structured data are consistent with purchasable product state.
- Do not hide all price text in the DOM while emitting contradictory product offers in schema.
- Preserve pagination discoverability and canonical strategy.
- Ensure out-of-stock product visibility and structured availability are consistent with the business policy.

## Persian, RTL, and multilingual content

- Keep URL slugs stable unless an approved migration requires change.
- Separate display translations from taxonomy identifiers and stored values.
- Ensure language-specific title, description, canonical, hreflang, breadcrumb, and schema are internally consistent.
- Do not translate a slug or rewrite URL merely because a display label changes.
- Avoid duplicate pages caused by inconsistent trailing slash, URL encoding, or language parameters.

## Diagnostic commands and evidence

Use appropriate tools available in the environment, for example:
- `curl -I https://example.com/robots.txt` to inspect status/headers.
- Fetch the full robots.txt and sitemap response bodies.
- Inspect `view-source:` or raw HTTP HTML for canonical, robots meta, hreflang, and JSON-LD.
- Compare edge response (Cloudflare) with origin response when authorized and available.
- Use Search Console URL Inspection and Page Indexing reports when the user provides access/evidence.

Record exact URL, timestamp, status code, headers, body excerpt, and tool used. Do not infer Googlebot's view from a normal browser session alone.

## Change safety

Before changing SEO output, record baseline URLs and metadata. For URL-affecting changes, prepare redirect and rollback plans. Test production and staging separately. Never expose staging or private content to crawlers accidentally.

## Acceptance tests

- Canonical URL correct and unique.
- Robots response accessible and intentional.
- Sitemap contains intended canonical URLs only.
- No accidental noindex/disallow.
- Breadcrumb HTML and schema are consistent.
- Structured data has no fabricated or contradictory values.
- Redirects have no loops or chains.
- Language alternates and canonical paths are coherent.
- Faceted URLs follow the documented crawl policy.
- Search Console evidence is reported separately from local technical tests.

## Anti-patterns

- Changing a slug to change only a visible label.
- Disallowing a page in robots.txt and expecting it to be deindexed.
- Broad Cloudflare bot exemptions without validation.
- Generating duplicate schema from several plugins.
- Indexing every filter/sort parameter.
- Claiming an SEO ranking increase as a proven result of a code change.
