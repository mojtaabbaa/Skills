---
name: advanced-woocommerce-filtering-ajax
description: Builds and debugs advanced WooCommerce catalog filters, taxonomy/attribute queries, AJAX product loops, filter state, pagination, responsive drawers, and WoodMart integration. Use for custom filters or AJAX catalog behavior.
---

# Advanced WooCommerce Filtering & AJAX

## Mission
Deliver a fast, deterministic catalog-filtering system that returns the correct products and count, preserves state and pagination, works on desktop/mobile, and integrates with the actual theme without duplicate requests or race conditions.

## Activate when
Product filters, taxonomy/attribute selection, AJAX loops, query clauses, sort/pagination interaction, filter URL state, desktop sidebars, mobile drawers, or WoodMart filter integration are involved.

## Required context loading
1. Read `../../knowledge/PROJECT-REGISTRY.md`.
2. Read `references/ravi-smart-filter-history.md`.
3. Locate the actual plugin version/source; `0.4.52` is a historical baseline only.
4. Inspect active theme and version, current filter markup, browser Network requests, AJAX handler, product query, and pagination rendering.
5. Load `custom-wordpress-plugin-engineering`, `woocommerce-engineering`, and `elementor-theme-integration` when the implementation crosses those domains.

## Known project requirements
- Desktop: fixed right-side sidebar; changing a filter applies immediately through AJAX; no Apply button.
- Mobile: full-screen filter panel; controls edit a draft state; Apply commits selections and closes the panel.
- Avoid extra requests and redundant fetching.
- Preserve existing filter/business behavior and approved visuals.
- Taxonomy configuration must be discovered/selected, not guessed.
- Historic candidate mapping (verify every entry in the current site): `pa_family` (family), `pa_temperament` (temperament), `pa_season` (season), `product_cat` (gender/category mapping used in one proposal), `product_brand` (brand).
- Historic mobile layout requests: reduce excess vertical spacing; note list should match supplied design reference; Personality tab should have four items per row. Do not invent the exact note-list markup without the design reference.

## Before writing the query
Document the contract:
- Allowed filter keys and registered taxonomy mapping.
- Accepted term IDs/slugs and normalization rules.
- OR/AND semantics within each taxonomy and across taxonomies.
- Behavior for empty/invalid selections.
- Archive/category/search scope.
- Stock/catalog visibility/language constraints.
- Sort order and pagination rules.
- Count/result consistency.
- Whether URL state is enabled or deliberately suppressed.

Never use user-visible labels as taxonomy identifiers. Verify taxonomy registration, object types, queryability, and term slugs at runtime or settings-save time. Reject unknown keys/terms rather than trusting raw request input.

## Query design
- Prefer WooCommerce/WordPress product-query extension points for the installed version/theme.
- Build clauses from validated normalized state, not raw request parameters.
- Preserve the main archive context, catalog visibility, stock rules, language filters, product type, and active sort.
- Ensure result count and product loop use the same effective query.
- Reset page to 1 when the filter state changes.
- Keep pagination and sorting state when filters stay unchanged.
- Avoid global query hooks that affect related products, widgets, search suggestions, admin, REST, or unrelated queries.
- Do not add duplicate `tax_query` or contradictory meta clauses.

## AJAX contract and performance
Use one canonical endpoint/request contract. Include only required context, validated selections, sort, and page. Define a stable response schema for result HTML/data, count, pagination, normalized state, and error messages.

- One user action should produce one intended request.
- Reuse already-loaded taxonomy metadata; do not refetch static terms on every selection.
- Debounce only if it materially helps rapid controls; avoid sluggish UI.
- Abort or ignore stale requests so an old response cannot overwrite a newer state.
- Prevent duplicate event handlers after loop replacement; use delegated events or explicit idempotent initialization.
- Preserve scroll/focus/expanded panels appropriately after replacing the product region.
- Do not publicly cache personalized results.
- Measure query count/latency before introducing caches or data denormalization.

## State model
- Desktop: selected state is applied state; each change requests results.
- Mobile: separate draft state from applied state. Opening panel initializes draft from applied state. Apply commits draft, requests results, and closes panel after the action is accepted. Define whether closing without Apply discards or preserves draft state; do not leave this ambiguous.
- Clear/reset must reset both UI state and query state consistently.
- Sort/page changes preserve the applied filter state.
- Rapid changes must not create stale response races.
- URL synchronization is opt-in; a separate historical request explicitly wanted no URL change. Confirm current project requirement before modifying query parameters/history.

## Theme integration
WoodMart AJAX Spy was used to inspect theme behavior. A URL observed during debugging resembled `?filter_category=women,men&_pjax=.wd-page-content`. This is evidence of one observed request only, not a stable public API. Inspect actual payload, response, selectors, events, and installed WoodMart version. Do not let native theme filters and the custom plugin both fire for one interaction unless deliberately coordinated.

## Responsive UI checks
Desktop fixed right sidebar and immediate apply. Mobile full-screen drawer and explicit Apply. Ensure proper touch targets, scroll locking, safe-area handling, keyboard/focus behavior, RTL, and bounded viewport scrolling. Do not solve crowded options by blindly shrinking every item; use the supplied design geometry and the defined four-column Personality requirement where applicable.

## Debugging sequence
1. Reproduce on a named archive and known filter selection.
2. Capture request URL/method/payload/status/response/timing.
3. Find the exact server handler and query-building code.
4. Log normalized state and query clauses in debug mode only.
5. Verify taxonomies and term slugs.
6. Compare with native theme query behavior.
7. Check duplicate event bindings, overlapping requests, and stale responses.
8. Validate loop, count, pagination, sorting, reset, and responsive state.

## Acceptance tests
No filter; one filter; multiple filters; OR/AND combinations; invalid taxonomy/term; reset; desktop immediate apply; mobile draft/apply/cancel; rapid changes; stale response; sorting; pagination; category/search context; zero results; stock visibility; RTL; keyboard/touch; and no unrelated product loops affected.

## Related Skills
- `wordpress-development-architecture`
- `woocommerce-engineering`
- `custom-wordpress-plugin-engineering`
- `elementor-theme-integration`
