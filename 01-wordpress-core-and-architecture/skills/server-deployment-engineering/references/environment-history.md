# Historical Server and Hosting Context

All values are HISTORICAL observations and may belong to different sites or dates. Verify before reuse.

## Hosting and web server
- Hostinger has been used.
- DirectAdmin and cPanel have appeared in administration workflows.
- LiteSpeed hosting has been used.
- Cloudflare has been used for DNS, proxying, and WAF/rules.
- PHP version changes in DirectAdmin were reported to affect the whole account in one setup. Confirm scope before changing a version.

## PHP versions and limits mentioned
- PHP 8.1.34 was reported in one context.
- PHP 8.4.27 was reported in another context.
- PHP 8.3 was tested in a separate troubleshooting period, with ionCube Loader compatibility concerns.
- Memory limits mentioned across separate environments included 160M, 512M, and a reported 4048M.
- Upload limit 2048M was mentioned for one site/environment.

Do not combine these values into a recommended baseline. Inventory each domain/account separately.

## Extensions and object cache
- Redis PHP extension: NO and Memcached PHP extension: NO were reported in one environment.
- A Memcached Object Cache attempt was discussed.
- Duplicator reported `Plugin 'unix_socket' is not loaded` during one operation.
- Verify active PHP SAPI, extension list, database client, and host support before changing configuration.

## Staging and migrations
- A staging domain `staging.armanivision.com` was discussed.
- A separate staging path/domain `wpvision.ir` appeared in a review related to `armanivision.com`; no redirect to staging was found in the `.htaccess` inspected at that time.
- SSL pending/provisioning was discussed on hosted sites.
- Persian filenames were reported corrupted after archive extraction in one migration context. For future archive operations, verify encoding, unzip tool, and filename handling before deleting originals.

## Server/security incidents
- PHP file upload was temporarily disabled by a host during a security event.
- WordPress menu updates returned 403 in the same general period.
- Cloudflare WAF/rules were associated with a Search Console `robots.txt` access issue.
- These do not prove a current security state or a single shared root cause.

## Operational rule
Never apply a server value from one site to another based only on memory. Record hostname, hosting account, PHP handler, exact setting path, before/after value, and rollback.
