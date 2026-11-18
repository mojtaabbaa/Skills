---
name: elementor-theme-integration
description: Integrates custom WordPress/WooCommerce features with Elementor, Elementor Pro, theme templates, dynamic queries, frontend lifecycle, and responsive RTL/LTR UI. Use for Elementor widgets, forms, templates, product loops, or theme-specific rendering.
---

# Elementor & Theme Integration

## Mission
Connect custom functionality to Elementor and the active theme without brittle DOM coupling, duplicate initialization, layout shifts, broken AJAX interactions, or misplaced business logic.

## Activate when
Elementor/Elementor Pro widgets, Theme Builder, forms, dynamic tags/queries, templates, product cards, theme hooks, template overrides, responsive layout, custom CSS/JS, or theme/builder interaction are involved.

## Required context loading
1. Read `../../knowledge/PROJECT-REGISTRY.md` and identify the exact website.
2. Read `references/theme-builder-and-ui-history.md`.
3. Confirm active theme/child theme and versions. The user's projects have used Astra, Hello Elementor, and WoodMart; one prior correction explicitly said a particular project was not WoodMart. Never infer the current theme from another project.
4. Inspect the exact template, widget, generated DOM, Elementor conditions, theme override, script load order, and cache/minification setup.
5. Load WordPress, WooCommerce, filtering, or plugin Skill as relevant.

## Integration rules
- Keep business rules and persistence in a custom plugin/domain module; use Elementor mainly for presentation and page composition.
- Prefer documented Elementor widget/control/dynamic-tag/query hooks over output scraping.
- Check Elementor availability and version before registering integrations.
- Enqueue assets only for the affected widget/template/page.
- Scope selectors to a plugin-owned component root; prefer stable classes/data attributes over generated Elementor IDs.
- Use delegated events or a documented lifecycle hook when AJAX replaces DOM content.
- Make initialization idempotent. Prevent duplicate listeners and observers.
- Avoid global MutationObservers, polling, `setInterval`, and repeated DOM scans unless no reliable lifecycle event exists; narrow any required observer to the smallest subtree.
- Never rely on client-side form conditions for access control or sensitive workflow validation.

## Theme-specific discipline
- Astra / Hello Elementor: inspect template hierarchy, theme hooks, Theme Builder ownership, header/footer override, and asset duplication.
- WoodMart: inspect the actual installed version, product-loop markup, AJAX replacement region, swatches, quick view, filter events, sticky add-to-cart, and template overrides. Treat internal classes/events as version-sensitive.
- Never declare theme compatibility merely because the plugin activates. Test the feature path and interactions.

## DOM and layout lifecycle
Before moving or replacing an element, determine who owns it: theme, Elementor, plugin, or a client script. Prefer rendering at the correct location server-side. If a client-side move is unavoidable, use a deterministic lifecycle and reserve final space to prevent layout shift. Do not wait for full page load as a generic fix if it creates visible movement.

For JavaScript:
- Inspect real markup first.
- Bind once; use stable root selectors.
- Handle re-render/AJAX replacement explicitly.
- Guard against missing elements and duplicate setup.
- Keep state in one component owner rather than reconstructing it from scattered DOM classes.
- Avoid adding a new request when existing data/response already contains what is needed.

For CSS:
- Scope selectors, test specificity against theme/Elementor CSS, support RTL/LTR, avoid unnecessary fixed heights, and preserve approved layouts.
- Match the reference design rather than making unsolicited redesign decisions.
- Validate mobile and desktop independently.

## Performance history to check
Historical tools/settings included WP Rocket, Autoptimize, and Perfmatters. Past observations included slow Google Fonts/Roboto requests, slow `unpkg.com` libphonenumber-js (a local `libphonenumber-max.js` was uploaded), Autoptimize JS concatenation breaking mobile buttons, worse mobile than desktop, LCP resource-load delay around 2,990ms associated with a slider image, WP Rocket Remove Unused CSS use, and an Elementor DOM snapshot of 4,623 total nodes. These observations are not current diagnoses. Re-profile before reusing a fix.

## Known UI/project history
- Ravi Perfume product card: Persian title RTL, English product name left-aligned, pipe separator removed for display, brand muted after title, price on right, add-to-cart on left, hover description removed, default 30ml requested in that context, black variation underline removed. Preserve the approved card layout. The historical design's exact typography values are not available here.
- Elementor service portal: login/register → request-type gateway → multi-step Elementor form → pending approval → manual admin document review → role/access assignment. Validate all permissions server-side.
- Elementor upload field styling and upload icon/link were discussed.
- A Key Takeaways section was being repositioned by theme/script behavior; a footer-based relocation eventually placed it correctly but caused visible movement until full load. Exact final code is not retained. Inspect current theme lifecycle rather than copying an unverified snippet.
- Sticky add-to-cart dropdown behavior for product volumes was discussed; inspect current variation markup/events.

## Validation
Check editor preview and frontend, logged-in and guest, mobile and desktop, RTL/LTR, AJAX refresh, keyboard/touch interaction, cache/minify/RUCSS, console/network logs, duplicate rendering, and CLS/layout shift. Re-check the approved visual reference before declaring done.

## Related Skills
- `wordpress-development-architecture`
- `woocommerce-engineering`
- `custom-wordpress-plugin-engineering`
- `advanced-woocommerce-filtering-ajax`
