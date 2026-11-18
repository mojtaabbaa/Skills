---
name: wordpress-security-engineering
description: Secures WordPress, WooCommerce, custom plugins, AJAX/REST endpoints, uploads, authentication, data handling, dependencies, and hosting integrations.
---

# WordPress Security Engineering

## Mission

Reduce exploitable attack surface while preserving legitimate site behavior. Security decisions must be based on trust boundaries, capabilities, validation, safe output, and least privilege. Do not confuse a visual restriction, nonce, WAF rule, or hidden control with actual authorization.

## When to use this Skill

Use it for plugin development/review, security hardening, admin/AJAX/REST endpoints, payment and pricing logic, file uploads, user roles, authentication, database queries, vulnerability reports, WAF/Cloudflare issues, and deployment permissions.

Load the relevant WordPress, Plugin, WooCommerce, Debugging, and Server Skill when the task crosses those areas.

## Threat-model first

For each feature identify:
- Assets: customer data, credentials, orders, price/discount data, uploaded files, settings, and site integrity.
- Actors: guest, customer, shop manager, administrator, integration/webhook, and unauthenticated attacker.
- Entry points: URL/query parameters, form fields, cookies, AJAX, REST, webhooks, uploads, imports, cron, and admin actions.
- Trust boundaries: browser to server, user role to privileged operation, plugin to third-party service, and CDN/WAF to origin.
- Abuse cases: unauthorized action, data disclosure, injection, stored/reflected XSS, CSRF, file upload abuse, privilege escalation, replay, and resource exhaustion.

## WordPress request security

### Authentication and authorization
- Authenticate the actor through the supported WordPress mechanism.
- Use `current_user_can()` or the relevant capability check for authorization.
- Check object-level permissions where a user may access only their own order/post/file.
- Do not authorize based on username, role label alone, hidden UI, request origin, or a nonce.
- A nonce helps mitigate CSRF; it does not prove identity or grant permission.

### Input validation and sanitization
- Validate type, shape, range, allowed values, length, and ownership.
- Use allowlists for action names, sort keys, taxonomy names, status transitions, and gateway IDs.
- Sanitize according to data type, but do not mistake sanitization for validation.
- Reject unexpected nested arrays and malformed payloads.
- Treat all browser-submitted price, variation, role, user ID, metadata, and permission values as untrusted.

### Output escaping
- Escape at final output context: HTML, attribute, URL, JavaScript, or textarea.
- Avoid concatenating untrusted content into inline scripts or style attributes.
- Preserve safe handling for Persian/English text and URLs; direction does not affect escaping requirements.

### SQL and data storage
- Use `$wpdb->prepare()` for query values.
- Allowlist dynamic table/column/order identifiers; placeholders do not safely parameterize identifiers.
- Prefer WordPress APIs where possible.
- Protect secrets and sensitive customer data from logs, HTML, options exposed through REST, and debug endpoints.
- Use least-privilege database and filesystem permissions supported by the host.

## AJAX and REST security

- For admin-ajax, verify nonce where relevant and independently check capability/object ownership.
- Register authenticated and unauthenticated actions intentionally; do not expose privileged operations to `nopriv` handlers.
- For REST routes, implement a meaningful `permission_callback`.
- Validate schema and reject unknown fields.
- Return only the data necessary for the caller.
- Rate-limit or otherwise constrain expensive public endpoints where abuse is plausible.
- Avoid reflecting raw exception messages or stack traces to public callers.

## WooCommerce security

- Recalculate all important commercial values server-side.
- Never trust frontend price, discount, variation, fee, stock, or gateway availability as authoritative.
- Verify product/variation relationship, purchasability, stock, customer permissions, and cart state.
- Preserve order ownership checks and HPOS-safe data access.
- Do not leak order details through guessable IDs or insufficient permission checks.
- Validate webhook signatures/tokens using the provider's documented method and protect against replay/idempotency issues.

## File upload security

- Restrict uploads by capability, nonce/authentication, size, file extension, verified MIME/type, and destination.
- Use WordPress upload APIs where appropriate.
- Do not trust filename extension or client MIME alone.
- Avoid executing uploaded files; use storage paths that are not executable where host configuration allows.
- Generate safe filenames and prevent path traversal.
- Scan or quarantine high-risk files when required by the threat model and available infrastructure.
- Do not broadly re-enable host-disabled upload behavior without understanding the security policy and intended upload flow.

## Plugin and dependency security

- Keep dependencies minimal and maintained.
- Verify package source, integrity, version, and license.
- Avoid secrets in source control or browser bundles.
- Protect admin settings and destructive actions with capability checks and nonces.
- Make migrations and uninstall behavior explicit.
- Avoid exposing diagnostic tools publicly.

## WAF, CDN, and hosting boundaries

- A WAF 403 is not proof that the WordPress application denied access; inspect edge and origin logs.
- Test `robots.txt`, REST, AJAX, uploads, and admin operations from both CDN and origin when authorized.
- Do not turn off the WAF globally to solve one false positive. Use a narrow rule exception with documented scope and expiry when justified.
- Do not make origin services publicly accessible as a shortcut.

## Review checklist

Use `references/security-review-checklist.md`. For security bugs, coordinate with Debugging Skill and preserve relevant evidence without exposing exploit details beyond the required defensive analysis.

## Disclosure and response

- State severity and affected component only when evidence supports it.
- Separate confirmed vulnerability from possible exposure.
- Recommend patch/mitigation and verification steps.
- Avoid publishing secrets, tokens, customer data, or weaponizable exploit chains unnecessarily.
- Record remediation, regression tests, and rollback.

## Anti-patterns

- Nonce-only authorization.
- Client-side-only price or permission checks.
- Trusting extension/MIME supplied by browser.
- Dynamic SQL identifiers from request data.
- Public REST callbacks that return privileged data.
- Global WAF disablement.
- Logging passwords, payment tokens, or personal customer data.
- Disabling security controls to make a feature work without a threat-modelled exception.
