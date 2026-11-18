# WordPress Plugin Architecture & Standard Structure

This guide defines the architectural standards, directory structure, and bootstrapping guidelines for modern WordPress plugin development.

---

## 1. Core Philosophy: Plugin vs Theme

* **Plugins (Functionality & Data):** Responsible for business logic, custom post types, custom tables, REST API endpoints, external integrations, user roles/capabilities, and features that should persist regardless of which theme is active.
* **Themes (Presentation & Styling):** Responsible purely for visual representation, templates, styling, layouts, and typography. A theme must NEVER contain critical business logic or register post types that users would lose upon switching themes.

---

## 2. Modern Standard Directory Layout

A production-ready WordPress plugin follows a modular, PSR-4 compliant structure:

```text
my-awesome-plugin/
├── assets/                       # Static public assets
│   ├── css/                      # Unminified CSS / SCSS
│   ├── js/                       # Source JS / TypeScript
│   └── images/                   # Icons, logos, banners
├── build/                        # Compiled production assets (via @wordpress/scripts / Vite)
├── includes/                     # PSR-4 namespaced PHP source files
│   ├── Admin/                    # Backend admin dashboards, settings, notices
│   │   ├── Menu.php
│   │   ├── Settings.php
│   │   └── Views/                # Admin HTML templates
│   ├── Api/                      # REST API endpoints & webhooks
│   │   └── RestController.php
│   ├── Frontend/                 # Shortcodes, frontend scripts, dynamic widgets
│   │   └── ShortcodeHandler.php
│   ├── Database/                 # Custom tables, migrations, $wpdb wrappers
│   │   └── Installer.php
│   ├── Models/                   # Data transfer objects and business entities
│   ├── Services/                 # External service integrations (Stripe, CRM, etc.)
│   └── Plugin.php                # Main orchestrator / bootstrap class
├── languages/                    # Internationalization (.pot, .po, .mo files)
├── templates/                    # Overridable frontend templates
├── tests/                        # Automated tests (PHPUnit / Pest / wp-env)
├── vendor/                       # Composer dependencies (git-ignored)
├── .editorconfig                 # Coding style rules
├── .gitignore                    # Ignored files (vendor/, build/, node_modules/, etc.)
├── composer.json                 # Composer definition with PSR-4 autoloading
├── my-awesome-plugin.php         # Lightweight plugin entry point
├── package.json                  # Frontend dependencies (@wordpress/scripts, etc.)
├── phpcs.xml.dist                # PHP_CodeSniffer WordPress standards config
├── README.md                     # Technical repository documentation
└── readme.txt                    # WordPress.org official plugin directory standard
```

---

## 3. The Lightweight Bootstrap File (`my-awesome-plugin.php`)

The entry file should contain **no business logic**. Its responsibilities are strictly:
1. Provide WordPress plugin header metadata.
2. Prevent direct execution access (`ABSPATH` check).
3. Define immutable path and version constants.
4. Verify environment prerequisites (PHP version, WordPress version, required extensions).
5. Load Composer's PSR-4 autoloader.
6. Register activation, deactivation, and uninstall hooks.
7. Initialize the main orchestrator class.

```php
<?php
/**
 * Plugin Name:       My Awesome Plugin
 * Plugin URI:        https://example.com/plugins/my-awesome-plugin
 * Description:       A modern, production-ready WordPress plugin with PSR-4 architecture.
 * Version:           1.0.0
 * Requires at least: 6.2
 * Requires PHP:      8.0
 * Author:            Your Company / Name
 * Author URI:        https://example.com
 * License:           GPL-2.0-or-later
 * License URI:       https://www.gnu.org/licenses/gpl-2.0.html
 * Text Domain:       my-awesome-plugin
 * Domain Path:       /languages
 */

// Block direct access
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// 1. Define Plugin Constants
define( 'MY_AWESOME_PLUGIN_VERSION', '1.0.0' );
define( 'MY_AWESOME_PLUGIN_FILE', __FILE__ );
define( 'MY_AWESOME_PLUGIN_PATH', plugin_dir_path( __FILE__ ) );
define( 'MY_AWESOME_PLUGIN_URL', plugin_dir_url( __FILE__ ) );
define( 'MY_AWESOME_PLUGIN_BASENAME', plugin_basename( __FILE__ ) );

// 2. Load Composer Autoloader
if ( file_exists( MY_AWESOME_PLUGIN_PATH . 'vendor/autoload.php' ) ) {
    require_once MY_AWESOME_PLUGIN_PATH . 'vendor/autoload.php';
}

// 3. Register Activation & Deactivation Hooks
register_activation_hook( __FILE__, [ 'MyAwesomePlugin\Database\Installer', 'activate' ] );
register_deactivation_hook( __FILE__, [ 'MyAwesomePlugin\Database\Installer', 'deactivate' ] );

// 4. Initialize Plugin on 'plugins_loaded'
function my_awesome_plugin_bootstrap(): void {
    // Check PHP version requirement
    if ( version_compare( PHP_VERSION, '8.0', '<' ) ) {
        add_action( 'admin_notices', function() {
            echo '<div class="notice notice-error"><p>' . 
                 esc_html__( 'My Awesome Plugin requires PHP 8.0 or higher.', 'my-awesome-plugin' ) . 
                 '</p></div>';
        });
        return;
    }

    // Launch main plugin singleton / orchestrator
    \MyAwesomePlugin\Plugin::get_instance();
}
add_action( 'plugins_loaded', 'my_awesome_plugin_bootstrap' );
```

---

## 4. Composer & PSR-4 Autoloading Setup (`composer.json`)

To eliminate messy manual `require_once` statements, configure PSR-4 autoloading:

```json
{
  "name": "vendor/my-awesome-plugin",
  "description": "Modern WordPress plugin with clean architecture",
  "type": "wordpress-plugin",
  "license": "GPL-2.0-or-later",
  "require": {
    "php": ">=8.0"
  },
  "require-dev": {
    "wp-coding-standards/wpcs": "^3.0",
    "phpunit/phpunit": "^9.5"
  },
  "autoload": {
    "psr-4": {
      "MyAwesomePlugin\\": "includes/"
    }
  },
  "config": {
    "optimize-autoloader": true,
    "sort-packages": true,
    "allow-plugins": {
      "dealerdirect/phpcodesniffer-composer-installer": true
    }
  }
}
```

---

## 5. Main Orchestrator Class (`includes/Plugin.php`)

```php
<?php

namespace MyAwesomePlugin;

use MyAwesomePlugin\Admin\Menu;
use MyAwesomePlugin\Admin\Settings;
use MyAwesomePlugin\Api\RestController;
use MyAwesomePlugin\Frontend\ShortcodeHandler;

final class Plugin {

    private static ?Plugin $instance = null;

    public static function get_instance(): self {
        if ( null === self::$instance ) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    private function __construct() {
        $this->load_textdomain();
        $this->init_components();
    }

    private function load_textdomain(): void {
        add_action( 'init', function() {
            load_plugin_textdomain(
                'my-awesome-plugin',
                false,
                dirname( MY_AWESOME_PLUGIN_BASENAME ) . '/languages'
            );
        });
    }

    private function init_components(): void {
        // Shared & REST API
        ( new RestController() )->register();

        // Backend Admin
        if ( is_admin() ) {
            ( new Menu() )->register();
            ( new Settings() )->register();
        }

        // Frontend
        if ( ! is_admin() || wp_doing_ajax() ) {
            ( new ShortcodeHandler() )->register();
        }
    }

    private function __clone() {}
    public function __wakeup() {
        throw new \Exception( "Cannot unserialize singleton" );
    }
}
```

---

## 6. Lifecycle Management: Activation, Deactivation & Uninstallation

1. **Activation (`register_activation_hook`):**
   * Create custom tables via `dbDelta()`.
   * Set default options via `add_option()`.
   * Flush rewrite rules **only** if custom post types/taxonomies are registered (`flush_rewrite_rules(false)`).
2. **Deactivation (`register_deactivation_hook`):**
   * Clear scheduled cron jobs (`wp_clear_scheduled_hook()`).
   * Flush rewrite rules.
   * **NEVER delete user data, options, or tables upon deactivation!**
3. **Uninstallation (`uninstall.php`):**
   * WordPress checks for `uninstall.php` in the root folder when the user clicks **Delete**.
   * Only delete custom options, transients, and tables here, preferably respecting an admin opt-in ("Delete data on uninstall").
   * **Always check `WP_UNINSTALL_PLUGIN` constant:**

```php
<?php
// uninstall.php
if ( ! defined( 'WP_UNINSTALL_PLUGIN' ) ) {
    exit;
}

// 1. Delete Options
delete_option( 'my_awesome_plugin_settings' );

// 2. Drop Custom Tables if configured
global $wpdb;
$table_name = $wpdb->prefix . 'my_awesome_plugin_data';
$wpdb->query( "DROP TABLE IF EXISTS {$table_name}" );
```
