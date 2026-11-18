# WordPress Security Review Checklist

## Identity and permissions
- [ ] Authentication requirement defined.
- [ ] Capability check implemented.
- [ ] Object ownership/tenant boundary checked.
- [ ] Nonce used where relevant, but not as authorization.

## Inputs and outputs
- [ ] Inputs schema-validated and bounded.
- [ ] Allowlists used for actions, taxonomy, sort, gateway, and status values.
- [ ] SQL uses prepared values and allowlisted identifiers.
- [ ] Output escaped for final context.
- [ ] Error responses do not leak internal details.

## AJAX/REST/webhooks
- [ ] Public vs authenticated entry points intentional.
- [ ] REST permission callback is meaningful.
- [ ] Request size and cost are bounded.
- [ ] Webhook signature and replay/idempotency behavior verified.

## WooCommerce
- [ ] Price, stock, variation, discount, and fee recalculated server-side.
- [ ] Order ownership and HPOS-safe access checked.
- [ ] Gateway amount and persisted order total are consistent.

## Uploads and files
- [ ] User capability and request token checked.
- [ ] File type, MIME, size, and destination validated.
- [ ] Filename/path traversal prevented.
- [ ] Uploaded content cannot execute where infrastructure supports restriction.

## Operations
- [ ] Secrets excluded from source, output, and logs.
- [ ] Dependency versions and provenance checked.
- [ ] WAF exceptions narrow and documented.
- [ ] Backups and rollback exist for schema/security changes.
- [ ] Tests cover guest, customer, manager, and administrator paths as relevant.
