# WordPress Plugin Security & Data Persistence

Security is non-negotiable in WordPress plugin development. The WordPress security model follows the **Golden Rule**:
> **Never Trust User Input — Sanitize on Input, Escape on Output, Verify Permissions & Nonces on Execution.**

---

## 1. Input Sanitization & Validation

### Sanitization (Cleaning data before saving or using)
Always sanitize inputs from `$_POST`, `$_GET`, `$_REQUEST`, or REST API payloads:

| Data Type | Sanitization Function | Example Usage |
| :--- | :--- | :--- |
| Single-line string | `sanitize_text_field()` | `$name = sanitize_text_field( $_POST['user_name'] ?? '' );` |
| Multi-line string | `sanitize_textarea_field()` | `$bio = sanitize_textarea_field( $_POST['bio'] ?? '' );` |
| Email address | `sanitize_email()` | `$email = sanitize_email( $_POST['email'] ?? '' );` |
| Slug / Key | `sanitize_key()` | `$slug = sanitize_key( $_POST['key'] ?? '' );` |
| File Name | `sanitize_file_name()` | `$file = sanitize_file_name( $_FILES['upload']['name'] );` |
| URL | `esc_url_raw()` | `$website = esc_url_raw( $_POST['website'] ?? '' );` |
| HTML Content | `wp_kses()` / `wp_kses_post()` | `$content = wp_kses_post( $_POST['custom_html'] ?? '' );` |
| Positive Integer | `absint()` | `$id = absint( $_GET['id'] ?? 0 );` |

### Validation (Ensuring data conforms to constraints)
```php
if ( ! is_email( $email ) ) {
    return new \WP_Error( 'invalid_email', __( 'Please provide a valid email address.', 'my-plugin' ) );
}

if ( ! in_array( $status, [ 'pending', 'active', 'archived' ], true ) ) {
    return new \WP_Error( 'invalid_status', __( 'Invalid status value provided.', 'my-plugin' ) );
}
```

---

## 2. Output Escaping (Preventing XSS)

Never output dynamic variables directly into HTML without escaping:

* **`esc_html()`**: For standard text inside HTML elements:
  ```php
  <h2><?php echo esc_html( $post_title ); ?></h2>
  ```
* **`esc_attr()`**: For HTML tag attributes:
  ```php
  <input type="text" name="username" value="<?php echo esc_attr( $user_name ); ?>">
  ```
* **`esc_url()`**: For links and image sources:
  ```php
  <a href="<?php echo esc_url( $profile_url ); ?>">View Profile</a>
  ```
* **`esc_js()`**: For inline JavaScript string literals:
  ```php
  <button onclick="confirmAction('<?php echo esc_js( $message ); ?>')">
  ```
* **`esc_textarea()`**: For rendering text inside a `<textarea>` tag:
  ```php
  <textarea><?php echo esc_textarea( $description ); ?></textarea>
  ```
* **`wp_kses_post()`**: For rich HTML content allowed in standard posts:
  ```php
  <div class="content"><?php echo wp_kses_post( $custom_body_html ); ?></div>
  ```

---

## 3. Nonces & CSRF Prevention

Nonces (Numbers used Once) prevent Cross-Site Request Forgery attacks.

### In Forms:
```php
// Render form with nonce field
<form method="post" action="">
    <?php wp_nonce_field( 'my_plugin_save_action', 'my_plugin_nonce_field' ); ?>
    <input type="text" name="my_field" value="">
    <button type="submit">Save</button>
</form>

// Process form in PHP
if ( isset( $_POST['my_plugin_nonce_field'] ) ) {
    if ( ! wp_verify_nonce( sanitize_text_field( wp_unslash( $_POST['my_plugin_nonce_field'] ) ), 'my_plugin_save_action' ) ) {
        wp_die( esc_html__( 'Security check failed!', 'my-plugin' ), 403 );
    }
    // Proceed with authorized handling
}
```

### In AJAX Requests:
```php
// Localize nonce in PHP
wp_localize_script( 'my-script-handle', 'myPluginData', [
    'ajax_url' => admin_url( 'admin-ajax.php' ),
    'nonce'    => wp_create_nonce( 'my_ajax_action_nonce' ),
] );

// Verify in PHP AJAX handler
add_action( 'wp_ajax_my_action', 'handle_ajax_action' );
function handle_ajax_action() {
    check_ajax_referer( 'my_ajax_action_nonce', 'security' );
    
    // Capability check
    if ( ! current_user_can( 'manage_options' ) ) {
        wp_send_json_error( [ 'message' => 'Unauthorized' ], 403 );
    }
    
    wp_send_json_success( [ 'data' => 'OK' ] );
}
```

---

## 4. User Authorization & Capability Checks

Never assume a user is authorized because they are logged in. Always test capabilities:

```php
if ( ! current_user_can( 'manage_options' ) ) {
    wp_die( esc_html__( 'You do not have permission to access this page.', 'my-plugin' ), 403 );
}

// For editing a specific post:
if ( ! current_user_can( 'edit_post', $post_id ) ) {
    wp_die( esc_html__( 'Unauthorized to edit this post.', 'my-plugin' ), 403 );
}
```

---

## 5. Database Interaction (`$wpdb`) & SQL Injection Prevention

Direct queries must always use prepared statements via `$wpdb->prepare()`.

### Querying Data:
```php
global $wpdb;

$user_status = 'active';
$limit       = 10;
$table_name  = $wpdb->prefix . 'my_plugin_subscribers';

// Use %s for strings, %d for integers, %f for floats
$results = $wpdb->get_results(
    $wpdb->prepare(
        "SELECT id, email, created_at FROM {$table_name} WHERE status = %s ORDER BY id DESC LIMIT %d",
        $user_status,
        $limit
    )
);
```

### Inserting and Updating Data:
Use helper methods that automatically prepare arguments:
```php
// Insert
$wpdb->insert(
    $table_name,
    [
        'email'      => $sanitized_email,
        'status'     => 'active',
        'created_at' => current_time( 'mysql' ),
    ],
    [ '%s', '%s', '%s' ]
);

// Update
$wpdb->update(
    $table_name,
    [ 'status' => 'inactive' ],
    [ 'id'     => $id ],
    [ '%s' ],
    [ '%d' ]
);
```

### Creating Custom Tables (`dbDelta`):
```php
public static function create_custom_tables(): void {
    global $wpdb;

    $table_name      = $wpdb->prefix . 'my_plugin_logs';
    $charset_collate = $wpdb->get_charset_collate();

    // dbDelta requirements:
    // 1. Each field on its own line
    // 2. PRIMARY KEY on its own line with 2 spaces after KEY
    // 3. INDEX syntax strictness
    $sql = "CREATE TABLE {$table_name} (
        id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
        user_id bigint(20) unsigned NOT NULL DEFAULT 0,
        action_name varchar(100) NOT NULL DEFAULT '',
        details longtext NULL,
        created_at datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
        PRIMARY KEY  (id),
        KEY user_id (user_id)
    ) {$charset_collate};";

    require_once ABSPATH . 'wp-admin/includes/upgrade.php';
    dbDelta( $sql );
}
```

---

## 6. Options API vs Transients API

* **Options API (`get_option`, `update_option`, `add_option`, `delete_option`)**:
  * For persistent settings and plugin configurations.
  * Best practice: Store plugin settings as a single associative array rather than dozens of separate rows in `wp_options`.
  * Set `$autoload = false` if the setting is only needed in the admin dashboard:
    ```php
    add_option( 'my_plugin_settings', $defaults, '', 'no' );
    ```

* **Transients API (`set_transient`, `get_transient`, `delete_transient`)**:
  * For caching expensive API responses or query results with an expiration time.
  * Example:
    ```php
    $cache_key = 'my_plugin_weather_data';
    $data      = get_transient( $cache_key );

    if ( false === $data ) {
        $response = wp_remote_get( 'https://api.example.com/data' );
        if ( ! is_wp_error( $response ) ) {
            $data = json_decode( wp_remote_retrieve_body( $response ), true );
            set_transient( $cache_key, $data, 12 * HOUR_IN_SECONDS );
        }
    }
    ```
