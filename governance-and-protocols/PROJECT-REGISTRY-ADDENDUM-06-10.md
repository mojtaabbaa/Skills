# Project Registry Addendum — Frontend, Debugging, Performance, Security, Server

This file extends the original project registry. Entries are historical context, not proof of current installation or configuration.

## Frontend and UI history
- Elementor and Elementor Pro used in multiple projects.
- Themes discussed: Astra, Hello Elementor, WoodMart; verify per site.
- Ravi Perfume product-card constraints: Persian/English mixed title, brand secondary label, price/add-to-cart alignment, default 30ml in the relevant selector, preserve approved design.
- Ravi Smart Filter responsive UI: desktop fixed sidebar/immediate AJAX; mobile full-screen panel with draft selections and Apply; Personality tab four items per row.
- Key Takeaways section relocation had a layout-shift problem; exact final implementation is not retained.
- Historical colors and fonts are catalogued in `frontend-engineering/references/known-ui-contracts.md`.

## Debugging history
- PHP memory exhaustion.
- DB message `Commands out of sync; you can't run this command now`, associated in logs with `usfyi_options`.
- Duplicator error `Plugin 'unix_socket' is not loaded`.
- Fatal involving `Ravi_MM_Renderer::flush_memo()`.
- A mega-menu search update was associated with 500 responses and single-product loading failures.
- Host temporarily disabled PHP file uploads; `nav-menus.php` returned 403.
- Elementor errors and cache/JS optimization regressions were reported.
- See `debugging-engineering/references/historical-incidents.md` for boundaries and cautions.

## Performance history
- WP Rocket, Autoptimize, and Perfmatters have been used.
- Google Fonts/Roboto and unpkg libphonenumber-js were reported as slow external requests in separate contexts.
- A local `libphonenumber-max.js` copy was uploaded.
- Autoptimize JS concatenation broke mobile buttons in one setup.
- LCP resource load delay around 2,990ms was reported; a slider image was implicated.
- One Elementor DOM snapshot: 4,623 total nodes, 1,265 divs, 228 Elementor elements, 130 widgets, 98 containers.
- Redis and Memcached PHP extensions were unavailable in at least one environment.

## Security history
- Cloudflare WAF/rules were associated with a robots.txt/Search Console access issue.
- Host file-upload restriction and 403 admin operation are documented in the debugging and security references.
- No current compromise or unresolved vulnerability is established by these historical observations.

## Server history
- Hostinger, DirectAdmin, cPanel, LiteSpeed, and Cloudflare have been used in different contexts.
- PHP 8.1.34, 8.3, and 8.4.27 were mentioned across different environments; memory/upload limits also varied.
- Staging and domain migration work included `staging.armanivision.com` and a `wpvision.ir` reference.
- See `server-deployment-engineering/references/environment-history.md`.

## Data discipline
For any current project, record its exact hostname, repo root, PHP/core/plugin/theme versions, hosting account, environment, and last verified date. Do not merge the above notes into one site profile.
