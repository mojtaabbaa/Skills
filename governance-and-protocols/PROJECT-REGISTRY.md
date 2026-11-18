# Project Registry — reconstructed context

This file prevents an AI agent from mixing site-specific assumptions. It is a registry of what is known from prior discussions, not a live inventory. Confirm each entry against the current repository before acting.

## Named product/site contexts

| Name | Known context | Confidence / limitation |
|---|---|---|
| `ravi-perfume.com` / Ravi Perfume | Perfume WooCommerce work; product-card UI, volume variations, price-per-ml, filter/plugin context | Project association is known; active theme/version and current plugin versions must be inspected. Do not automatically assume WoodMart is the active theme. |
| `staging.armanivision.com` | Staging environment discussed for an Armanivision site | Historical hostname; verify DNS, hosting, and active mapping. |
| `armanivision.com` | WordPress/server configuration and staging discussions | Historical configuration snapshots only; not current server truth. |
| `heydarian-meat.com`, `sina-machine.com`, `tebico24.com`, `rose1980.ir`, `sjavadatr.ir`, `pishrohesab.com`, `touspalace.com`, `adrincafe.ir`, `yassmojalal.ir`, `albertacashforcars.ca` | Sites mentioned in past WordPress work | No reliable per-site technical map is available in this knowledge snapshot. Do not infer theme, plugins, hosting, or current status. |

## Named custom systems

### Ravi Smart Filter
- Custom WooCommerce filter plugin with intended WoodMart compatibility.
- Version `0.4.52` was identified as a baseline in a prior discussion. It may not be current.
- The user inspected WoodMart AJAX behavior with WoodMart AJAX Spy; a request URL observed included `filter_category=women,men` and `_pjax=.wd-page-content`.
- Desktop: fixed right sidebar, immediate AJAX on selection, no Apply button.
- Mobile: full-screen panel, draft state, Apply commits and closes.
- Taxonomy candidates discussed: `pa_family`, `pa_temperament`, `pa_season`, `product_cat`, `product_brand`. They are candidates only; actual registration must be inspected.
- The user requires low request count, compact/ordered mobile layout, and four items per row in the Personality tab. Note-list visual details require the original reference image/design.
- Graphify was preferred for architecture navigation if a generated project graph is available. In one environment, Graphify CLI was not installed/run because PyPI DNS/network access failed. Do not claim graph analysis happened.

### Ravi Design System (RDS)
- Plugin name: Ravi Design System.
- Historical option names: `rds_settings`, `rds_classes`.
- Historical method: `build_css()`.
- Historical output path: `ravi-design-system/design-system.css`.
- Verify current source, write permissions, and actual generation lifecycle.

### Ravi Mega Menu
- Dynamic brand loading/search beyond the initial 12 entries was requested.
- Mega-menu height needed control.
- Fatal error reported in `Ravi_MM_Renderer::flush_memo()` during menu settings work.
- Later search updates were associated with 500 errors and single-product page loading problems.
- These are incident signatures, not proven root causes. Inspect the stack trace and source.

### Service portal
- User flow discussed: login/register → choose request type → Elementor multi-step form → pending approval → admin document review → role/access assignment.
- Members plugin was used for custom roles in that context.
- Consultation options historically included in-person and phone appointments, with values in toman and 30–40 minute duration. Confirm current amounts and workflow before reuse.

## Shared environment observations — historical only
- Hosting/platforms mentioned: Hostinger, LiteSpeed, DirectAdmin, cPanel, Cloudflare.
- PHP versions mentioned at different times/sites: 8.1.34, 8.3, 8.4.27. Never assume current PHP.
- Memory limits varied by site and time (160M, 512M, and another report of 4048M).
- Redis and Memcached PHP extensions were unavailable in one inspected environment.
- Prior issues included `Commands out of sync; you can't run this command now` near `usfyi_options`, PHP memory exhaustion, Duplicator message `Plugin 'unix_socket' is not loaded`, Cloudflare/WAF and robots.txt access issues, 403 menu updates during a host security incident, and file-upload restrictions.
- Performance tools mentioned: WP Rocket, Autoptimize, Perfmatters. A JavaScript concatenation setting broke mobile buttons in one configuration; treat as historical warning, not a universal incompatibility.

## Project isolation rule
When a task begins, identify one active site and one repository. If a request refers to a known plugin but the codebase does not contain it, ask for/procure the correct source rather than transplanting code from a different project. Do not assume a plugin/site mapping from matching brand names alone.
