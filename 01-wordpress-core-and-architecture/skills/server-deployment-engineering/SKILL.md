---
name: server-deployment-engineering
description: Plans and operates WordPress hosting, PHP/database configuration, DNS, SSL, Cloudflare, staging, migrations, backups, deployment, monitoring, and rollback.
---

# Server & Deployment Engineering

## Mission

Deploy WordPress and custom plugins safely across local, staging, and production environments. Treat the hosting provider, DNS/CDN, web server, PHP runtime, database, filesystem, cache, and application as separate layers with explicit dependencies and rollback paths.

## When to use this Skill

Use it for hosting setup, domain/subdomain routing, DNS records, SSL, Cloudflare, LiteSpeed, Hostinger, DirectAdmin, cPanel, PHP versions/extensions/limits, database configuration, migration, backups, staging, file permissions, cron, deployment, and incident recovery.

Load Debugging for active failures, Security for WAF/permissions/uploads, Performance for caching/resource issues, and Plugin Engineering for release packaging/migrations.

## Environment inventory

Before changing anything, collect:
- Site/domain and environment (local/staging/production).
- Hosting provider, control panel, web server, and account boundaries.
- DNS provider, Cloudflare proxy status, relevant records, and TTL.
- SSL issuer/status and HTTPS redirect behavior.
- PHP version, handler, extensions, memory/upload/post/time limits, OPcache.
- Database engine/version, database name/prefix, and access method.
- WordPress/core/plugin/theme versions.
- Filesystem paths, ownership, permissions, and available disk/inodes.
- Cache layers and exclusions.
- Cron mechanism and last successful execution.
- Current backup and restore test status.

Do not assume that two domains on one account share isolated PHP configuration. Hosting control panels can apply settings at account or domain scope.

## DNS and subdomains

- Confirm authoritative DNS provider and current records before editing.
- A subdomain may need to exist in the source hosting/control panel, destination hosting/control panel, or both depending on provider routing. Do not assume creating a DNS record creates the site/vhost on the destination server.
- Create the required virtual host/site mapping on the destination server.
- Point the authoritative DNS record to the correct destination IP/hostname.
- Validate A/AAAA/CNAME, proxy status, propagation, Host header routing, and origin response.
- Avoid conflicting A and CNAME records for the same name.
- Confirm SSL issuance at the destination and Cloudflare origin mode before enforcing redirects.

## SSL and Cloudflare

- Identify whether Cloudflare is DNS-only or proxied.
- Confirm origin certificate and edge SSL mode.
- Avoid redirect loops from duplicate HTTPS enforcement at CDN, server, and WordPress levels.
- Test HTTP-to-HTTPS, canonical domain, subdomain, REST/AJAX, and `robots.txt`.
- Cache and WAF rules must not block admin, checkout, account, AJAX, REST, or upload paths.
- Make narrow WAF exceptions only with evidence and a review/expiry plan.

## PHP and hosting configuration

- Verify active PHP version per domain/account, not only the control-panel selector.
- Check required extensions and versions against WordPress/WooCommerce/plugins.
- Understand hosting scope: account-wide, domain-specific, FPM pool, or `.user.ini`/`.htaccess`.
- Do not increase memory, execution time, or upload limits indiscriminately.
- Confirm PHP-FPM/LSAPI handler and OPcache behavior when relevant.
- After changing PHP version, test frontend, admin, cron, AJAX, uploads, payment, and scheduled tasks.
- Back up configuration before changing `.htaccess`, `.user.ini`, PHP selector settings, or web server rules.

## Database and migration

- Back up database and files, then verify backup integrity.
- Record WordPress URL, home URL, table prefix, serialized data implications, and environment-specific secrets.
- Use migration tools or serialization-aware replacements for URLs; do not perform unsafe raw string replacement in serialized values.
- Check database collation/charset and PHP extensions/driver compatibility.
- Confirm plugins that depend on database drivers or authentication plugins.
- Validate uploads, media URLs, permalinks, cron, email, payment callbacks, and search indexing after migration.
- Do not delete source environment until destination verification and rollback window are complete.

## Deployment and rollback

1. Confirm current source version and clean change set.
2. Create a backup and record restore procedure.
3. Deploy to staging or a clone.
4. Run syntax, activation, integration, and functional tests.
5. Confirm configuration/secrets are environment-specific.
6. Deploy during a controlled window.
7. Verify key journeys and logs.
8. Monitor for errors.
9. Keep previous package/backup and a tested rollback path.

Do not use direct production edits as the default workflow. If emergency hotfixing is unavoidable, record exact changes and reconcile them back into source control immediately.

## File permissions and ownership

- Use least privilege supported by the host.
- Avoid blanket `777` permissions.
- Verify the PHP/web server user and deployment user.
- Make writable only directories that require writes, such as uploads or plugin-generated assets, with scope appropriate to the host.
- A plugin's generated CSS or cache directory should fail safely if unwritable; do not weaken all filesystem permissions to make one file write succeed.

## Cron and background tasks

- Determine whether WP-Cron is traffic-driven or replaced by a system cron.
- If `DISABLE_WP_CRON` is enabled, verify an actual external scheduler exists and runs on time.
- Monitor failed scheduled actions and WooCommerce Action Scheduler backlog.
- Avoid scheduling duplicate recurring events on every request.

## User-specific historical environment context

See `references/environment-history.md`. It includes LiteSpeed, Hostinger, DirectAdmin, cPanel, Cloudflare, PHP versions, memory limits, upload limits, SSL, staging, migration, and cache extension observations. These are historical and must be revalidated per site.

## Required deployment checklist

Use `references/deployment-checklist.md`. Report environment, changed records/settings, backup verification, tests, monitoring, and rollback.

## Anti-patterns

- Pointing DNS before the destination vhost/site mapping exists.
- Assuming a subdomain DNS record alone provisions the destination site.
- Changing PHP version without confirming account/domain scope.
- Enforcing redirects at multiple layers without checking for loops.
- Migrating serialized WordPress data with unsafe text replacement.
- Disabling WP-Cron without a working external cron.
- Setting filesystem permissions to 777.
- Deploying without a restorable backup.
