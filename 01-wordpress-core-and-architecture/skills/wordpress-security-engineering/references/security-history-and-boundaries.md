# Historical Security and Hosting Boundary Context

Evidence level: HISTORICAL. Do not infer a current compromise or vulnerability from these observations.

## Host upload restriction and admin 403
- A hosting provider temporarily disabled PHP file upload functionality during a reported security event.
- WordPress menu updates through `nav-menus.php` returned 403 around that period.
- The origin of the 403 was not conclusively documented. Possible enforcement layers include hosting policy, WAF, web server rules, or application authorization.
- Future investigation must correlate exact timestamps across browser response, web server, host security logs, Cloudflare events, and WordPress/PHP logs.
- Do not broadly disable security or re-enable restricted PHP functions without host confirmation and a narrow plan.

## Cloudflare and robots.txt
- Cloudflare WAF/rules were associated with Search Console reporting a robots.txt issue on a prior site.
- Verify the actual response status/body, CDN cache state, WAF event, and origin response.
- Do not change robots directives to fix a transport/security-layer denial unless the file contents are actually wrong.

## General security observations
- Sites have used Cloudflare and shared hosting. This does not mean every site has identical WAF, firewall, or file permission configuration.
- PHP versions, upload limits, and memory settings varied by environment.
- Do not store or repeat private credentials from logs or screenshots in project knowledge.

## Incident documentation
Record the responsible layer (application, WordPress, PHP, web server, host, CDN/WAF), evidence, scope of the exception, and expiry/review date for temporary mitigations.
