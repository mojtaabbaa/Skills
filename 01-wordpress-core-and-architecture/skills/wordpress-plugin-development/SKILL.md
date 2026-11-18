---
name: wordpress-plugin-development
description: >-
  Expert guide and standard reference for developing modern, secure, and production-ready
  WordPress plugins. Covers architecture (PSR-4, OOP, modern project structure), security
  (sanitization, escaping, nonces, capabilities, SQL injection prevention), WordPress hooks
  (actions & filters), REST API, Settings API & Admin UI, database persistence ($wpdb, dbDelta),
  Gutenberg block integration, Interactivity API, and internationalization (i18n).
  Use this skill whenever the user asks to create, refactor, review, or debug WordPress plugins.
---

# Modern WordPress Plugin Development Skill

This skill guides the agent in designing, structuring, developing, refactoring, and auditing production-grade WordPress plugins according to modern WordPress standards (PHP 8.0+, WordPress 6.x+, PSR-4 autoloading, and strict security practices).

---

## 1. Core Principles & Philosophy

When developing or reviewing WordPress plugins, adhere to these fundamental principles:

1. **Separation of Concerns (Theme vs Plugin):**
   * **Plugins** own data, business logic, Custom Post Types (CPT), taxonomies, custom database tables, and REST endpoints.
   * **Themes** own visual design, layout, and presentation.
2. **Security First (The Golden Rule):**
   * **Never trust input:** Sanitize and validate every incoming value (`sanitize_text_field`, `absint`, `sanitize_email`, etc.).
   * **Never trust output:** Escape every rendered variable (`esc_html`, `esc_attr`, `esc_url`, `wp_kses_post`).
   * **Verify intent & identity:** Always verify Nonces (`wp_verify_nonce`, `check_ajax_referer`) and user permissions (`current_user_can`).
   * **Prevent SQL injection:** Strictly use `$wpdb->prepare()` or prepared helper methods (`$wpdb->insert()`, `$wpdb->update()`).
3. **Modern Modular Architecture:**
   * Favor PSR-4 autoloading (via Composer) over messy chains of manual `require_once`.
   * Separate logic into focused classes: Orchestrator (`Plugin`), Admin, API, Frontend, Database, and Services.
   * Keep the root bootstrap file (`my-plugin.php`) lightweight: only metadata headers, constant definitions, compatibility checks, and autoloader bootstrap.
4. **Clean Lifecycle Management:**
   * Manage activation (`register_activation_hook`) for table creation and options setup.
   * Manage deactivation (`register_deactivation_hook`) for clearing cron jobs and flushing rewrites.
   * Put data cleanup strictly in `uninstall.php` (never delete data on deactivation).

---

## 2. In-Depth Reference Manuals

For detailed implementations, code templates, and patterns, consult the subdocuments:

* **[Architecture & Standard Structure](./references/architecture-and-structure.md):**
  Standard directory layout, entrypoint bootstrap template, Composer PSR-4 setup, main Orchestrator class, and activation/deactivation/uninstall lifecycle.
* **[Security & Data Persistence](./references/security-and-data.md):**
  Comprehensive sanitization and escaping functions, Nonces (forms & AJAX), Capability checks, `$wpdb->prepare()` queries, custom table creation with `dbDelta()`, Options API, and Transients API.
* **[Hooks, REST API & Admin UI](./references/hooks-and-apis.md):**
  Actions vs Filters, registering REST API endpoints (`register_rest_route`) with permission callbacks, Admin menus (`add_menu_page`), Settings API, proper asset enqueuing (`wp_enqueue_script`/`style`), and Internationalization (`__()`, `_e()`, `esc_html__()`).
* **[Gutenberg Blocks & Modern Tooling](./references/gutenberg-and-modern-tools.md):**
  `@wordpress/scripts` workflow, `block.json` standard, Interactivity API, local development with `@wordpress/env` (`wp-env`), and PHP_CodeSniffer with WordPress-Extra rules.

---

## 3. Step-by-Step Plugin Development Workflow

When asked to build or scaffold a new WordPress plugin:

### Step 1: Requirements & Architecture Planning
* Determine whether the functionality belongs in a plugin (not a theme).
* Identify required Custom Post Types (CPTs), custom tables, REST endpoints, and admin setting pages.
* Choose a unique slug, namespace, and text domain (e.g. `slug: my-plugin`, `Namespace: MyPlugin\`, `Text Domain: my-plugin`).

### Step 2: Directory & Skeleton Scaffolding
Create the modern layout:
```text
my-plugin/
├── includes/
├── assets/
├── languages/
├── composer.json
├── my-plugin.php
└── uninstall.php
```

### Step 3: Configure Autoloading & Bootstrap
* Define the metadata header in `my-plugin.php`.
* Add `defined('ABSPATH') || exit;`.
* Check minimum PHP (>= 8.0) and WP (>= 6.2) versions.
* Configure `composer.json` with PSR-4 autoloading for `MyPlugin\` -> `includes/`.

### Step 4: Implement Core Components
* **Admin / Settings:** Implement using the Settings API (`register_setting`, `add_settings_field`).
* **REST API:** Register routes inside `rest_api_init` with robust `permission_callback` and argument validation.
* **Assets:** Enqueue scripts & styles on specific screens using `admin_enqueue_scripts` and `wp_enqueue_scripts`.
* **Database:** If custom tables are needed, run `dbDelta()` inside the activation handler.

### Step 5: Security & Quality Audit Checklist
Before delivering any plugin code, verify each item:
- [ ] Direct file access blocked (`defined('ABSPATH') || exit;`) in all PHP files.
- [ ] All `$_POST`, `$_GET`, and request parameters sanitized before use.
- [ ] All rendered variables escaped (`esc_html`, `esc_attr`, `esc_url`, `wp_kses_post`).
- [ ] Nonces created and verified on every form submission and AJAX request.
- [ ] Capabilities checked (`current_user_can(...)`) before running sensitive actions.
- [ ] All database queries wrapped in `$wpdb->prepare()`.
- [ ] All user-facing strings internationalized with matching text-domain.
- [ ] No residual debugging code or `var_dump()` calls.
