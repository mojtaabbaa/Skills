# WordPress Deployment Checklist

## Before deployment
- [ ] Correct project/site and environment confirmed.
- [ ] Git status and source version reviewed.
- [ ] Backup of files and database created.
- [ ] Backup restoration method verified.
- [ ] PHP version/extensions and database compatibility confirmed.
- [ ] DNS/vhost/SSL/CDN routing confirmed.
- [ ] Secrets and environment-specific configuration checked.
- [ ] Cache and WAF exclusions reviewed.

## Deployment
- [ ] Deploy package to staging first where possible.
- [ ] Apply database migrations with version tracking.
- [ ] Verify file ownership and minimal permissions.
- [ ] Purge relevant cache layers.
- [ ] Confirm cron/external scheduler.

## Post-deployment verification
- [ ] Homepage and key landing pages.
- [ ] Login/register/account.
- [ ] Product archive and single product.
- [ ] Variations, cart, checkout, gateway, order creation.
- [ ] Forms, uploads, AJAX, REST, and admin operations.
- [ ] Email and webhooks/callbacks.
- [ ] SSL, canonical URLs, robots.txt, sitemap.
- [ ] PHP/server logs and browser console.
- [ ] Scheduled actions and cron.

## Rollback
- [ ] Previous code/package retained.
- [ ] Database rollback or forward-fix plan exists.
- [ ] DNS/SSL/WAF settings can be restored.
- [ ] Restore owner and decision authority identified.
- [ ] Rollback trigger and verification steps documented.

## Deployment record
- Site/environment:
- Date/time:
- Source version:
- Files changed:
- DNS/server/config changes:
- Backup identifier and restore check:
- Tests run:
- Unverified areas:
- Rollback procedure:
- Monitoring owner/window:
