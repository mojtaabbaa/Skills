---
name: wordpress-development-architecture
description: Engineers WordPress sites and customizations using core APIs, hooks, secure request handling, database patterns, compatibility checks, and low-regression implementation. Use for WordPress PHP, themes, hooks, queries, REST, AJAX, cron, admin, migrations, or site-level architecture.
---

# WordPress Development & Architecture

## Mission
Deliver safe, maintainable WordPress changes grounded in the current repository and runtime. Treat this as the platform skill; load WooCommerce, plugin, filtering, or Elementor skills when the task crosses those boundaries.

## Activate when
WordPress core APIs, PHP hooks, theme behavior, post types, taxonomies, metadata, users/roles, admin, REST, AJAX, cron, database access, migration, or general WordPress architecture are involved.

## Required context loading
1. Read `../../knowledge/PROJECT-REGISTRY.md` to avoid mixing sites and projects.
2. Read `references/architecture-and-environment.md` for historical environment and incident context.
3. Read the active repository's `AGENTS.md`, `.agents/AGENTS.md`, README, plugin/theme headers, Composer files, and relevant source before changing code.
4. If the task concerns commerce, custom plugin architecture, filtering, or Elementor, load the corresponding sibling Skill and its specific reference file. Do not load all five full references by default.

## Non-negotiable operating rules
- Current source code, runtime configuration, and explicit user instructions outrank this historical knowledge pack.
- Never infer that two site names, themes, plugin versions, or settings belong to the same project. Resolve the active site/repository first.
- Treat every historical value as time-bound unless its evidence status says otherwise. Recheck WordPress/PHP/WooCommerce/theme/plugin versions and hosting extensions.
- Inspect before editing: `git status`, project tree, plugin/theme headers, bootstrap, relevant hooks, existing customizations, logs, and tests.
- Preserve approved UI and existing business behavior. Make the smallest complete change that satisfies the requirement.
- Do not edit WordPress core or third-party plugin/theme files. Use documented extension points, a project-owned plugin, or a child theme when justified.
- Never guess hook names, selectors, table schemas, taxonomy slugs, AJAX action names, gateway IDs, or plugin APIs. Search the installed source and verify.
- Separate business logic from presentation. Use Elementor/theme templates for composition, not as the default home for domain logic.
- No unnecessary dependencies, CDNs, network requests, global observers, polling, or duplicate AJAX requests.

## Decision workflow

### 1. Identify execution context
Determine whether the code runs in frontend, admin, REST, `admin-ajax.php`, cron, CLI, webhook, or WooCommerce lifecycle. Identify the current page/template, user role, post type/product type, and expected state.

### 2. Choose the correct extension layer
- Site-wide business logic: project-owned plugin.
- Reusable domain feature: dedicated custom plugin/module.
- Theme-specific markup/style: child theme or theme integration module.
- One-off temporary experiment: snippet only when scope and rollback are clear.
- Page composition: Elementor, provided the behavior does not belong in domain logic.

### 3. Use platform APIs
Prefer WordPress APIs (`WP_Query`, metadata, taxonomy, user, options, REST, Settings API) over raw SQL. Use `$wpdb` only when necessary, prepared values with `$wpdb->prepare()`, and allowlisted identifiers. For WooCommerce entities, use WooCommerce CRUD APIs and load the WooCommerce Skill.

### 4. Secure every boundary
- Sanitize inputs according to type, then validate business meaning.
- Escape output at render time (`esc_html`, `esc_attr`, `esc_url`, or context-appropriate escaping).
- Use nonces for request intent and `current_user_can()` for authorization. A nonce is not permission.
- REST routes need a deliberate `permission_callback`.
- AJAX handlers must validate method, required fields, nonce where applicable, capabilities, and value allowlists.
- Never expose secrets or customer-sensitive data in HTML, errors, or logs.

### 5. Implement safely
Use a unique namespace/prefix. Keep functions small and responsibility-specific. Make repeated hooks safe and idempotent. Avoid global mutable state and broad filters that alter unrelated queries. Preserve backward compatibility or explicitly document the breaking change.

### 6. Validate and report
Run available syntax/static checks, relevant tests, and targeted manual checks. Test positive, negative, guest/authenticated, admin/customer, mobile/desktop, cache, and AJAX paths as relevant. State precisely what was and was not tested.

## WordPress-specific technical checks
- Verify supported PHP syntax against the actual minimum PHP version.
- Verify multisite behavior only when the project supports it.
- Check whether `WP_Query` filters also affect widgets, related products, admin, REST, or secondary loops.
- Use `wp_safe_redirect()` for safe redirects; validate destinations.
- Avoid expensive work on every request; consider cron, caching, or precomputation only after measuring.
- Use options for small configuration; custom tables only when volume and query patterns justify them.
- Make migrations versioned, repeatable, and reversible where possible.
- Treat transients/object cache as disposable; design invalidation.
- Respect RTL and mixed Persian/English output at component level.

## Failure and rollback protocol
If a change triggers a fatal/500, disable only the affected feature/module first where possible. Capture timestamp, request path, PHP error, stack trace, plugin versions, and last changed file. Do not randomly deactivate unrelated plugins or change PHP versions before evidence points there. Provide a rollback instruction that restores the previous known-good code/configuration.

## Output contract
For code tasks, return: (1) diagnosis/assumptions, (2) exact files and hooks affected, (3) complete implementation and install location, (4) security/performance/compatibility risks, (5) validation checklist, and (6) rollback. Do not claim production success without production evidence.

## Related Skills
- `woocommerce-engineering`
- `custom-wordpress-plugin-engineering`
- `advanced-woocommerce-filtering-ajax`
- `elementor-theme-integration`
