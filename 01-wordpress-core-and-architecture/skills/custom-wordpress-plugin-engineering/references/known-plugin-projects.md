# Known Custom Plugin Projects

This reference captures project names and known behavior from prior discussions. It intentionally does not invent class names, file paths, or implementation details not present in the available record.

## Ravi Smart Filter

- Custom WooCommerce filtering plugin intended to work with WoodMart and WooCommerce.
- The user inspected WoodMart AJAX behavior using WoodMart AJAX Spy.
- A request URL observed during debugging included parameters similar to `?filter_category=women,men&_pjax=.wd-page-content`.
- Desktop behavior requirement: fixed right-side filter sidebar; filters update via AJAX on change; no Apply button.
- Mobile behavior requirement: full-screen filter panel with an Apply button; pressing Apply closes the panel and applies the selected state.
- Avoid extra requests; prefer direct and lightweight behavior.
- Taxonomy candidates discussed:
  - Family / خانواده بویایی: `pa_family`
  - Temperament / طبع: `pa_temperament`
  - Season / فصل: `pa_season`
  - Gender: `product_cat`
  - Brand: `product_brand`
- The user explicitly said taxonomy names must not be guessed. The settings UI should allow taxonomy type selection and searching.
- Mobile staged filters had spacing problems; options consumed too much vertical space.
- A specific mobile layout requirement: note lists should follow the reference layout; the Personality tab should show four items per row. The exact final markup/CSS is not included in this pack.
- A baseline version `0.4.52` was identified in later project discussion. Treat this as the known baseline at that point, not necessarily current.
- Graphify was preferred for architecture navigation when a Graphify-generated project graph exists. The CLI was not installed/run in the referenced environment because PyPI DNS/network access failed. Do not claim a graph exists or that Graphify analysis was completed unless the artifact is supplied.

## Ravi Design System (RDS)

- Custom plugin named Ravi Design System.
- Database option names mentioned: `rds_settings` and `rds_classes`.
- CSS generation method mentioned: `build_css()`.
- Generated CSS path mentioned: `ravi-design-system/design-system.css`.
- Verify current plugin source, path, write permissions, and generation lifecycle before changing it.

## Ravi Mega Menu

- Custom plugin named Ravi Mega Menu.
- A feature request involved dynamic brand loading rather than limiting the menu to 12 brands.
- Search should search the full brand dataset, not only the initial 12 displayed brands.
- Mega menu height needed to remain controlled.
- A fatal error was reported in `Ravi_MM_Renderer::flush_memo()` after a menu-selection interaction in WordPress menu settings.
- Do not infer the root cause from the method name. Inspect stack trace and implementation.
- A later update to mega-menu search was associated with 500 errors and single-product page loading failures. Treat this as a regression incident requiring source-level tracing, not as proof of a particular cause.

## Other custom features

- Shortcode for product features on single-product pages.
- Sticky add-to-cart dropdown behavior for product volumes.
- Elementor upload-field styling and image-upload icon/link.
- Custom service portal flow: login/register → select request type → Elementor form → pending approval → admin document review → role/access assignment.
- Consultation booking with admin-managed time slots; historical types were in-person (2,000,000 toman) and phone (1,000,000 toman), with 30–40 minute duration. Confirm values before reuse.

## Required project-history discipline

For each plugin, maintain:
- Current version and baseline
- Exact source repository/ZIP
- Module map
- Options and database schema
- Hooks and AJAX/REST contracts
- Theme/plugin integration points
- Known regressions
- Confirmed fixes and tests
- Open issues
- Release notes
