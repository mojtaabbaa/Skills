# WordPress Hooks, REST API & Admin Architecture

---

## 1. WordPress Hooks System: Actions vs Filters

WordPress uses an event-driven architecture governed by hooks.

### Actions (`add_action`, `do_action`)
Actions run at specific lifecycle milestones or events. They perform operations and do not return data.

```php
// Firing a custom action (in your code or theme)
do_action( 'my_plugin_before_process_order', $order_id, $customer_data );

// Hooking into an action
add_action( 'my_plugin_before_process_order', 'my_custom_listener', 10, 2 );
function my_custom_listener( int $order_id, array $customer_data ): void {
    // Perform operations (log, send email, etc.)
}
```

### Filters (`add_filter`, `apply_filters`)
Filters intercept and modify data before it is rendered or saved. They **must always return the value**.

```php
// Exposing a filterable value
$button_text = apply_filters( 'my_plugin_submit_button_text', __( 'Submit Now', 'my-plugin' ) );

// Hooking into a filter to modify the value
add_filter( 'my_plugin_submit_button_text', function( string $text ): string {
    return __( 'Complete Order', 'my-plugin' );
});
```

---

## 2. WordPress REST API (`register_rest_route`)

Modern plugins expose secure REST endpoints for SPAs, mobile apps, or headless frontends.

### Best Practices:
* Always use a vendor/version namespace (e.g. `myplugin/v1`).
* **Never omit `permission_callback`**: In WordPress 5.5+, missing a permission callback throws a warning or error.
* Use `WP_REST_Request` and return `WP_REST_Response` or `WP_Error`.

```php
namespace MyAwesomePlugin\Api;

class RestController {

    public function register(): void {
        add_action( 'rest_api_init', [ $this, 'register_routes' ] );
    }

    public function register_routes(): void {
        register_rest_route( 'myplugin/v1', '/items', [
            [
                'methods'             => \WP_REST_Server::READABLE, // GET
                'callback'            => [ $this, 'get_items' ],
                'permission_callback' => '__return_true', // Public endpoint
            ],
            [
                'methods'             => \WP_REST_Server::CREATABLE, // POST
                'callback'            => [ $this, 'create_item' ],
                'permission_callback' => [ $this, 'check_manage_permission' ],
                'args'                => [
                    'title' => [
                        'required'          => true,
                        'type'              => 'string',
                        'sanitize_callback' => 'sanitize_text_field',
                        'validate_callback' => function( $param ) {
                            return ! empty( trim( $param ) );
                        },
                    ],
                ],
            ],
        ] );
    }

    public function check_manage_permission(): bool {
        return current_user_can( 'manage_options' );
    }

    public function get_items( \WP_REST_Request $request ): \WP_REST_Response {
        $items = [ [ 'id' => 1, 'name' => 'Demo Item' ] ];
        return rest_ensure_response( $items );
    }

    public function create_item( \WP_REST_Request $request ): \WP_REST_Response|\WP_Error {
        $title = $request->get_param( 'title' );
        // Save logic...
        return new \WP_REST_Response( [ 'success' => true, 'title' => $title ], 201 );
    }
}
```

---

## 3. Admin Menus & Settings API

### 1. Registering Menu & Submenu:
```php
namespace MyAwesomePlugin\Admin;

class Menu {
    public function register(): void {
        add_action( 'admin_menu', [ $this, 'add_admin_menu' ] );
    }

    public function add_admin_menu(): void {
        add_menu_page(
            __( 'Plugin Settings', 'my-awesome-plugin' ),
            __( 'My Plugin', 'my-awesome-plugin' ),
            'manage_options',
            'my-awesome-plugin',
            [ $this, 'render_main_page' ],
            'dashicons-admin-generic',
            30
        );

        add_submenu_page(
            'my-awesome-plugin',
            __( 'Logs & Analytics', 'my-awesome-plugin' ),
            __( 'Logs', 'my-awesome-plugin' ),
            'manage_options',
            'my-awesome-plugin-logs',
            [ $this, 'render_logs_page' ]
        );
    }

    public function render_main_page(): void {
        require_once MY_AWESOME_PLUGIN_PATH . 'includes/Admin/Views/settings-page.php';
    }
}
```

### 2. Using WordPress Settings API:
```php
namespace MyAwesomePlugin\Admin;

class Settings {
    public function register(): void {
        add_action( 'admin_init', [ $this, 'init_settings' ] );
    }

    public function init_settings(): void {
        register_setting( 'my_plugin_option_group', 'my_plugin_options', [
            'type'              => 'array',
            'sanitize_callback' => [ $this, 'sanitize_options' ],
            'default'           => [ 'api_key' => '', 'enable_logging' => 0 ],
        ] );

        add_settings_section(
            'my_plugin_main_section',
            __( 'General Settings', 'my-awesome-plugin' ),
            function() { echo '<p>' . esc_html__( 'Configure your plugin details below.', 'my-awesome-plugin' ) . '</p>'; },
            'my-awesome-plugin'
        );

        add_settings_field(
            'my_plugin_api_key',
            __( 'API Key', 'my-awesome-plugin' ),
            [ $this, 'render_api_key_field' ],
            'my-awesome-plugin',
            'my_plugin_main_section'
        );
    }

    public function render_api_key_field(): void {
        $options = get_option( 'my_plugin_options', [] );
        $value   = $options['api_key'] ?? '';
        echo '<input type="password" name="my_plugin_options[api_key]" value="' . esc_attr( $value ) . '" class="regular-text">';
    }

    public function sanitize_options( array $input ): array {
        $output = [];
        $output['api_key'] = sanitize_text_field( $input['api_key'] ?? '' );
        $output['enable_logging'] = ! empty( $input['enable_logging'] ) ? 1 : 0;
        return $output;
    }
}
```

---

## 4. Proper Asset Enqueuing

Never inject CSS/JS tags directly into templates. Use `wp_enqueue_script` and `wp_enqueue_style`.

* Use `admin_enqueue_scripts` for backend.
* Use `wp_enqueue_scripts` for frontend.
* Pass dependencies (`[ 'jquery' ]` or `[ 'wp-element' ]`).
* Include dynamic versioning (plugin version or `filemtime`) for cache busting.

```php
add_action( 'wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'my-plugin-frontend',
        MY_AWESOME_PLUGIN_URL . 'assets/css/frontend.css',
        [],
        MY_AWESOME_PLUGIN_VERSION
    );

    wp_enqueue_script(
        'my-plugin-frontend',
        MY_AWESOME_PLUGIN_URL . 'assets/js/frontend.js',
        [ 'wp-i18n' ],
        MY_AWESOME_PLUGIN_VERSION,
        [ 'in_footer' => true ]
    );

    // Pass data safely to JavaScript
    wp_localize_script( 'my-plugin-frontend', 'myPluginSettings', [
        'apiUrl' => esc_url_raw( rest_url( 'myplugin/v1/' ) ),
        'nonce'  => wp_create_nonce( 'wp_rest' ),
    ] );
});
```

---

## 5. Internationalization (i18n) & Localization (l10n)

Always prepare all user-facing strings for translation:

* Simple translation: `__( 'Hello World', 'my-awesome-plugin' )`
* Direct echo: `_e( 'Save Changes', 'my-awesome-plugin' )`
* Escaped translation (Recommended):
  * `esc_html__( 'Text only', 'my-awesome-plugin' )`
  * `esc_html_e( 'Text only', 'my-awesome-plugin' )`
  * `esc_attr__( 'Attribute value', 'my-awesome-plugin' )`
* Plurals:
  ```php
  printf(
      esc_html( _n( '%d item found', '%d items found', $count, 'my-awesome-plugin' ) ),
      $count
  );
  ```
* Contextual strings:
  ```php
  _x( 'Post', 'verb: to post something', 'my-awesome-plugin' );
  _x( 'Post', 'noun: a blog post', 'my-awesome-plugin' );
  ```
