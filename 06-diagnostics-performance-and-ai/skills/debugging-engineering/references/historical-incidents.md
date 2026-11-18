# Historical WordPress Incident Register

All entries below are HISTORICAL observations. They may belong to different sites, versions, and dates. Do not merge them into one incident or assume they are still active.

## PHP and WordPress errors

### PHP Fatal: memory exhaustion
- Symptom: PHP fatal error indicating memory limit exhausted.
- Historical memory limit values mentioned across different sites/times included 160M, 512M, and a reported 4048M.
- No universal root cause is recorded. Investigate the stack trace, request, query volume, loops, image processing, and plugin workload before changing limits.

### Elementor error / product page failing to load
- Elementor errors and single-product page loading failures were mentioned in separate troubleshooting periods.
- A mega-menu search update was associated with HTTP 500 errors and single-product page failures in one later report.
- Association does not prove causation. Correlate exact deployment, stack trace, and affected page.

### Ravi Mega Menu fatal
- Method recorded: `Ravi_MM_Renderer::flush_memo()`.
- Context: fatal error after interaction with menu selection in WordPress menu settings.
- Root cause and final fix are not preserved. Inspect the exact class, stack trace, object lifecycle, and memo/cache implementation.

## Database error

### `Commands out of sync; you can't run this command now`
- Reported in a database log with reference to `usfyi_options`.
- This message can involve MySQL client result-set/connection-state handling, but the specific cause in this site is not established.
- Inspect the exact SQL, client/driver path, result consumption, plugin database abstractions, and timestamp-correlated stack/logs. Do not infer a specific plugin defect from the option name.

## Duplicator/migration error

### `Plugin 'unix_socket' is not loaded`
- Reported during a Duplicator operation.
- Environment-specific. Inspect database client/driver and hosting support. Do not alter database authentication plugins blindly.

## Admin/server security errors

### PHP file upload disabled and `nav-menus.php` 403
- The host temporarily disabled PHP file upload functionality during a reported security incident.
- WordPress menu updates returned 403 in that period.
- Possible layers include host policy, WAF, PHP restrictions, or authorization. The exact cause needs correlated server/security logs.

### Cloudflare robots.txt/Search Console issue
- Cloudflare WAF/rules were associated with robots.txt access problems reported by Search Console.
- Validate actual response status, body, cache, bot rules, and origin response before changing robots directives.

## AJAX and custom plugin regressions

### Mega Menu search update causing 500
- A plugin update involving search was associated with 500 responses and single-product page load failures.
- Exact commit, changed files, and root cause are not retained.
- Compare before/after source and reproduce with request logs.

## Environment limitations

- Redis PHP extension and Memcached PHP extension were reported unavailable in at least one hosting environment.
- Do not assume object cache support without checking current PHP extensions, server service, and WordPress drop-in.

## Incident hygiene

For future entries include: site/project, exact version, timestamp/timezone, reproduction, full redacted stack trace, request ID if available, changed files, root cause evidence, fix, regression tests, and rollback.
