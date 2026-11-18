# Historical Performance Context

All values below are historical reports, not current site measurements.

## Optimization stack mentioned
- WP Rocket
- Autoptimize
- Perfmatters
- LiteSpeed hosting in some environments
- Cloudflare in several hosting setups

Do not assume all are installed or enabled on the same site. Inspect active plugins and actual cache layers.

## External resource observations

### Google Fonts / Roboto
- Requests to `fonts.googleapis.com` for Roboto were identified as a slowdown in one project.
- Roboto was requested for English blog pages only in a design context.
- Check whether the font is actually used, whether a local file exists, and which pages need it before removing or self-hosting.

### libphonenumber-js from unpkg
- `unpkg.com` loading of libphonenumber-js was reported as slow.
- The user uploaded a local `libphonenumber-max.js` copy.
- Verify version, license, file integrity, and actual usage before replacing any current dependency.

## JavaScript optimization regression
- Enabling JavaScript concatenation in Autoptimize broke mobile buttons in one configuration.
- Desktop performance was acceptable while mobile performance remained poor in a separate period.
- Any future concatenation, defer, delay, or minification change must test mobile interactions and dependency order.

## LCP observation
- A resource-load delay around 2,990ms was discussed in one investigation.
- A slider image was implicated.
- The exact URL, image, test device, and final improvement are not preserved. Re-profile the current LCP element.

## Elementor DOM snapshot
A user-reported snapshot for one page/project:
- totalNodes: 4623
- divs: 1265
- elementorElements: 228
- widgets: 130
- containers: 98

This is not a universal site baseline. DOM count is a clue, not proof of the bottleneck. Measure scripting, style recalculation, layout, paint, and network separately.

## Object cache limitations
- Redis PHP extension: NO was reported in one environment.
- Memcached PHP extension: NO was reported in one environment.
- A Memcached Object Cache attempt was discussed.
- Verify PHP extensions, server daemon, WordPress object-cache drop-in, and host support before attempting to enable object caching.

## Known hosting variation
PHP versions and memory limits varied across sites and dates. Never copy a PHP setting from one site to another without checking actual compatibility and hosting scope.
