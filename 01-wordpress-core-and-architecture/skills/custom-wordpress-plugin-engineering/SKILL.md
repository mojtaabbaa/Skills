---
name: custom-wordpress-plugin-engineering
description: Designs, builds, refactors, reviews, packages, and troubleshoots custom WordPress or WooCommerce plugins with modular architecture, secure settings, migrations, compatibility, and release discipline. Use when changing plugin source or creating a new plugin.
---

# Custom WordPress Plugin Engineering

## Mission
Treat each custom plugin as a maintained software product with explicit module boundaries, data contracts, lifecycle management, security, versioning, tests, and rollback—not as an untracked collection of snippets.

## Activate when
Creating a new plugin, changing plugin source, adding admin settings, AJAX/REST actions, shortcodes, widgets, custom tables/options, integrations, packaging ZIPs, release/versioning, or plugin-level debugging.

## Required context loading
1. Read `../../knowledge/PROJECT-REGISTRY.md` to select the correct plugin/site.
2. Read `references/known-plugin-projects.md` for project-specific history and unresolved incidents.
3. Inspect the current plugin folder/ZIP, plugin header/version, directory tree, bootstrap, hooks, database options/tables, assets, and release history.
4. Load the WooCommerce, filtering, or Elementor Skill when the plugin depends on those systems.

## Architecture baseline
Use the simplest architecture that keeps responsibilities clear. A typical plugin may contain:

```text
plugin-slug/
├── plugin-slug.php        # metadata, constants, bootstrap
├── includes/              # domain and integration classes
├── admin/                 # settings and admin screens
├── public/                # frontend integration
├── assets/css/
├── assets/js/
├── templates/             # only when template overrides are justified
├── languages/
├── uninstall.php
└── readme.txt
```

Do not force every plugin into this layout. A small plugin can stay smaller; a complex plugin should have deliberate modules, contracts, and ownership.

## Build procedure

### 1. Establish baseline before edits
- Record version and current Git status.
- Inspect all files related to the requested behavior.
- Locate hook registration, AJAX/REST contracts, option names, data schema, and frontend initialization.
- Identify dependencies and minimum supported WordPress/PHP/WooCommerce versions.
- Reproduce the behavior or error before changing code where possible.

### 2. Define contract and boundaries
Write acceptance criteria and state which module owns each responsibility. Define data inputs/outputs, authorization, persistence, events, and failure behavior. Avoid overlapping responsibilities across modules.

### 3. Implement safely
- Namespace classes/functions or use a unique prefix for every public identifier: hooks, AJAX actions, REST routes, options, transients, script handles, CSS classes, tables, and shortcode names.
- Keep the main plugin file focused on metadata, constants, dependency checks, and bootstrap.
- Check dependencies before registering integrations; fail gracefully when WooCommerce/Elementor is absent.
- Enqueue assets only on relevant pages/admin screens.
- Avoid inline script as the default architecture and avoid loading external libraries/CDNs without a demonstrated need.
- Make initialization idempotent; prevent duplicate listeners and duplicate hooks.
- Keep domain logic out of templates and page-builder HTML blocks.

### 4. Secure settings and endpoints
- Use Settings API where appropriate.
- Validate capability and nonce; sanitize by type; escape output.
- Use allowlists for selectable taxonomy keys, gateway IDs, modes, and other identifiers.
- AJAX: define input schema, auth model, nonce expectations, validation, stable JSON response, and error codes.
- REST: define `permission_callback` and response schema.
- Never use a nonce as the only authorization control.

### 5. Manage data and upgrades
- Use options for small configuration; custom table only after workload justification.
- Add schema version and idempotent migration path.
- Use `dbDelta()` carefully and verify indexes/column changes.
- Use prepared values for SQL and allowlist identifiers.
- Do not destroy settings/data on deactivate.
- Make uninstall cleanup explicit and documented; preserve user data by default unless the requirement says otherwise.
- Do not overwrite existing options during update without a migration plan.

### 6. Validate and package
Run PHP lint/static checks where available; test activation/deactivation, dependency missing, settings save, invalid input, frontend rendering, AJAX/REST, guest/authenticated permissions, RTL/mobile, theme/builder integration, cache/minification, and upgrade from previous version. Package only runtime files and never include secrets, local caches, temporary logs, or development-only artifacts.

## Project-specific memory
- `Ravi Smart Filter`: advanced WooCommerce filter project; known baseline `0.4.52` in a prior discussion, not necessarily current. Exact source required before edits.
- `Ravi Design System`: options `rds_settings` and `rds_classes`; CSS generation method `build_css()`; output path historically `ravi-design-system/design-system.css`. Verify current path, permissions, and code.
- `Ravi Mega Menu`: dynamic brand loading/search beyond the initial 12 brands was requested. A fatal error was reported in `Ravi_MM_Renderer::flush_memo()` during menu settings work; later search changes were associated with 500 errors and a single-product page failure. These are incidents, not proven root causes.
- Other discussed customizations: product-feature shortcodes, sticky add-to-cart/volume selector, Elementor upload-field appearance, and service portal workflows. Inspect actual project source; do not fabricate their file/class names.

## Debugging protocol
1. Capture exact request/page, timestamp, user role, and reproduction steps.
2. Read PHP/server/browser logs around that timestamp.
3. Trace the exact hook/action/class/method from the stack trace into source.
4. Inspect last code changes and dependencies.
5. Isolate the smallest failing module; reproduce with relevant integrations.
6. Fix root cause, not just visible symptom.
7. Run regression checks on nearby flows and unrelated pages.
8. Record the failure signature, root cause, fix, version, and actual test evidence.

## Release discipline
- Increment version intentionally and keep plugin header/readme/changelog consistent.
- Provide migration notes for schema/settings changes.
- Confirm ZIP root contains the plugin folder correctly.
- Ensure all internal entry paths inside the ZIP strictly use forward slashes (`/`), NEVER Windows backslashes (`\`). On Windows, avoid standard PowerShell `Compress-Archive` because it embeds Windows backslashes which breaks WordPress/Linux extraction (`unzip_file()`); use Python `zipfile` with `relpath.replace('\\', '/')` or `tar.exe`.
- Give exact installation/update and rollback steps.
- Do not claim a ZIP is production-ready without syntax and feature tests.

## User-specific constraints
Prefer lightweight, direct, low-request implementations. Do not guess taxonomy names or plugin APIs. Preserve current behavior. When asked for a complete plugin/file, provide the complete updated artifact rather than an incomplete fragment. Identify exactly what changed and what was tested.

## Related Skills
- `wordpress-development-architecture`
- `woocommerce-engineering`
- `advanced-woocommerce-filtering-ajax`
- `elementor-theme-integration`
