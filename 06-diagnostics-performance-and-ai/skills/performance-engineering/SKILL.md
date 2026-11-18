---
name: performance-engineering
description: Measures and improves WordPress, WooCommerce, Elementor, PHP, database, frontend asset, caching, and Core Web Vitals performance without breaking functionality.
---

# Performance Engineering

## Mission

Improve measurable user-perceived and system performance while preserving correctness. Diagnose the slow layer first, establish a baseline, change one meaningful variable at a time, and verify both performance and functionality.

## When to use this Skill

Use it for slow pages, poor mobile PageSpeed, LCP/INP/CLS issues, slow queries, high DOM complexity, large scripts/styles, cache configuration, object caching, asset loading, server resource pressure, and performance regressions after plugin/theme changes.

Load WordPress, WooCommerce, Elementor, Frontend, Debugging, and Server Skills as needed. Performance work must not bypass security or commerce correctness.

## Measurement before optimization

Establish a baseline on the same URL, device profile, region, network profile, login state, cache state, and test tool. Record:
- LCP, INP, CLS and relevant lab metrics.
- TTFB and document response.
- LCP element and resource discovery/loading timeline.
- JS execution and long tasks.
- CSS blocking, style recalculation, and layout work.
- Network request count, transfer size, duplicate assets, and third-party dependencies.
- DOM size and component/widget counts where relevant.
- PHP execution time, database query count/time, cache hits/misses, and memory where observable.

Separate field data from lab data. Do not present Lighthouse/PageSpeed lab scores as actual user field performance.

## Diagnosis tree

### If TTFB is high
Investigate hosting capacity, PHP execution, uncached page behavior, database latency, remote API calls, object cache, and expensive hooks. Compare cached vs uncached requests carefully.

### If LCP is high
Identify the actual LCP element. Check server response, resource discovery, priority, image size/format, lazy-loading mistakes, CSS background loading, slider/carousel logic, and font dependencies. Do not blindly preload every large image.

### If INP or interaction latency is high
Profile event handlers, long JavaScript tasks, DOM replacement, large plugin bundles, layout thrashing, duplicate listeners, and expensive AJAX response processing.

### If CLS is high
Find the exact layout-shift source. Reserve image/media dimensions, stabilize fonts, avoid post-load element relocation, and prevent dynamic banners/headers from inserting without reserved space.

### If page weight/request count is high
Inspect duplicated library loads, external fonts/CDNs, unused plugins/assets, images, CSS/JS coverage, and lazy-loading boundaries.

### If backend query cost is high
Inspect slow query logs or Query Monitor, repeated metadata lookups, unbounded loops, taxonomy/meta query shape, missing indexes, and query duplication. Do not add indexes without query evidence and migration planning.

## WordPress asset strategy

- Enqueue scripts/styles only on the pages that use them.
- Declare real dependencies and load order.
- Avoid duplicate libraries and unnecessary CDNs.
- Prefer local assets for critical dependencies where reliability and licensing permit.
- Use `defer`/`async`/delay/concatenation only after checking script dependencies and interaction behavior.
- Treat critical CSS and Remove Unused CSS as potential sources of hidden/late styles; test dynamic Elementor and AJAX components.
- Use responsive images and correct dimensions; do not lazy-load the actual above-the-fold LCP image by default.

## Caching strategy

Identify all cache layers separately:
- Browser cache
- CDN/Cloudflare cache
- Full-page cache (e.g. WP Rocket)
- Object cache (Redis/Memcached or another implementation)
- PHP OPcache
- Application transients

For each cache define key, scope, TTL, invalidation, and personalization rules. Do not cache cart, checkout, account, nonce-bearing, or user-specific content as public pages. Do not assume a Redis/Memcached extension or server service exists.

## WooCommerce-specific safeguards

- Exclude or correctly vary cart, checkout, account, cart fragments, and personalized product/pricing views.
- Preserve stock, price, variation, coupon, shipping, tax, and gateway correctness.
- Avoid expensive product/meta queries in every loop iteration.
- Check product query and variation payload size.
- Avoid reducing correctness (e.g. omitting variation data) merely to reduce bytes.

## Elementor-specific safeguards

- Measure actual DOM, CSS, and script work; widget count alone does not prove the bottleneck.
- Reuse templates/components where appropriate, but avoid nesting containers without design need.
- Check generated CSS volume and global widget assets.
- Test editor and frontend separately.
- Verify dynamic content, popups, forms, sticky UI, and AJAX loops after optimization.

## User-specific historical observations

See `references/performance-history.md`. These observations include WP Rocket, Autoptimize, Perfmatters, external fonts and JS, mobile regressions, slider LCP, Elementor DOM counts, and cache extension limitations. They are not current measurements.

## Optimization loop

1. Baseline.
2. Identify the largest proven bottleneck.
3. Form one hypothesis.
4. Change one variable or a tightly related set.
5. Re-run the same measurements.
6. Run functional regression tests, particularly mobile controls and WooCommerce flows.
7. Keep or revert based on evidence.
8. Record before/after values, test environment, and trade-offs.

## Completion criteria

A performance improvement is accepted only when:
- The target metric or bottleneck improves under comparable conditions.
- No critical functional regression occurs.
- Cache invalidation and personalized state remain correct.
- The exact configuration/code change and rollback are documented.

## Anti-patterns

- Optimizing based only on one score.
- Combining multiple optimization plugins/settings without understanding overlaps.
- Enabling JS concatenation or delay globally without testing interactions.
- Lazy-loading the LCP image.
- Adding preloads without evidence.
- Installing Redis/Memcached plugins without verifying server/extension support.
- Caching personalized commerce output publicly.
- Reporting a percentage improvement without same-condition measurements.
