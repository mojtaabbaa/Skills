# WordPress Architecture & Environment Reference

## Confirmed project direction from prior discussions

A perfume WooCommerce project was planned with a strong foundation while keeping its first phase intentionally simple and avoiding unnecessary custom APIs. The preferred architecture sequence was:

1. Infrastructure
2. WordPress
3. Theme / page builder
4. Design system
5. Features
6. Performance, security, testing, and deployment

The user explicitly wanted to avoid:
- Plugin sprawl
- Scattered snippets
- Unnamespaced hooks
- Inline JavaScript as a default architecture
- Direct WordPress core or database edits
- Production-first development

These are durable preferences and should guide future recommendations.

## Historical recommended baseline (not a claim about every current site)

A prior architecture recommendation discussed:
- PHP 8.3+
- MySQL 8+ or MariaDB 10.11+
- HTTPS
- Redis object cache where available and properly configured
- Cloudflare
- Staging before production
- WooCommerce HPOS awareness
- WooCommerce APIs such as `wc_get_order()` for order retrieval
- Excluding Cart, Checkout, and My Account from full-page caching
- Elementor as presentation layer, with business logic in a custom plugin
- AJAX with nonce, authorization, validation, sanitization, and explicit error handling

Revalidate all version and infrastructure requirements against the current hosting provider and plugin compatibility matrix.

## Important operational history

- Cloudflare WAF/rules were associated with a Search Console robots.txt access issue.
- SSL provisioning/pending state was discussed on hosted sites.
- Persian filenames were reported corrupted after archive extraction in one migration context.
- DirectAdmin/PHP configuration limitations were encountered, including PHP version changes affecting an entire hosting account.
- A 500 error and database message `Commands out of sync; you can't run this command now` were reported with a reference to `usfyi_options`.
- PHP fatal memory exhaustion occurred in prior troubleshooting.
- Duplicator reported `Plugin 'unix_socket' is not loaded` in one environment.
- Redis and Memcached extensions were unavailable in at least one environment.
- A security incident temporarily caused PHP file upload to be disabled by the host; menu updates returned 403 in that period.

These are incident records, not universal causes. Always inspect current logs and environment before applying a fix.

## WordPress data and API rules

- Use WordPress metadata, taxonomy, user, options, and query APIs where suitable.
- Use WooCommerce CRUD APIs for WooCommerce entities.
- Check HPOS compatibility before writing order data or querying order tables.
- Do not query WooCommerce order records using assumptions about legacy `shop_order` post storage.
- Use `$wpdb` only when the API is insufficient and query safety is explicit.
- Treat serialized options and plugin-owned schemas as plugin contracts; do not edit them casually.

## Deployment checklist

- Confirm staging and production hostnames.
- Confirm DNS A/AAAA/CNAME records and proxy status.
- Confirm SSL certificate and HTTPS redirect behavior.
- Confirm PHP version and extensions on the actual domain/account.
- Confirm database engine/version and backup.
- Confirm cache layers and exclusions.
- Confirm WP-Cron configuration and whether an external cron is configured.
- Confirm file ownership/permissions and upload restrictions.
- Test admin operations, frontend requests, AJAX, and scheduled jobs after deployment.
