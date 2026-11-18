# WordPress Core Architecture & Elementor Integration

## 1. Core Post Lifecycle & Metadata Storage
WordPress Core (v7.1.4) handles content storage primarily through two database tables:
- `wp_posts`: Stores standard post attributes (`ID`, `post_title`, `post_content`, `post_status`, `post_type`, `post_date`, `post_modified`).
- `wp_postmeta`: Key-value storage indexed by `post_id` and `meta_key`.

### How Elementor Leverages `wp_postmeta`
Elementor does not maintain custom tables for page content; instead, it utilizes `wp_postmeta` keys:
1. `_elementor_edit_mode`: Flag indicating whether the page is managed by Elementor (`'builder'`).
2. `_elementor_template_type`: Identifies the document template type (`'wp-page'`, `'wp-post'`, `'header'`, `'footer'`, `'single-post'`, `'archive'`, `'product'`, `'loop'`).
3. `_elementor_data`: The serialized JSON tree representing the entire container and widget layout.
4. `_elementor_page_settings`: Document-level settings (page title display, layout type, custom CSS/background).
5. `_elementor_css`: Compiled stylesheet metadata and status (`status`, `time`, `css`).
6. `_elementor_controls_usage`: JSON tracking the widget and control usage statistics for the document.
7. `_elementor_conditions`: Display conditions array for Theme Builder and Popup Builder templates.

### The Plain Text Content Fallback
When Elementor saves a document (`Elementor\Core\Base\Document::save_elements()`), it also invokes:
```php
Plugin::$instance->db->save_plain_text( $post_id );
```
This renders a text-only representation of the widget content directly into `wp_posts.post_content`. This guarantees:
- Native WordPress search queries (`WP_Query` with `s=...`) index the text within Elementor widgets.
- RSS feeds, REST API content consumers, and plugins inspecting `post_content` receive meaningful text rather than an empty string or raw JSON.

---

## 2. REST API & Metadata Exposure
By default, WordPress protected meta keys (keys starting with an underscore `_`) are hidden from the REST API unless explicitly registered via `register_post_meta()` or `register_meta()`.

In Elementor (`Elementor\Core\Admin\Admin::register_post_meta()`):
- `_elementor_edit_mode`, `_elementor_template_type`, and `_elementor_data` are exposed in REST with `show_in_rest => true` when permissions allow.
- When creating or editing pages through REST API endpoints (`/wp/v2/pages`) or MCP tools, these keys can be read and written directly if user capabilities (`edit_posts` / `manage_options`) are satisfied.

---

## 3. Template Hierarchy Interception
WordPress loads templates based on template hierarchy (`index.php`, `singular.php`, `page.php`, `single.php`, `archive.php`).

Elementor integrates at two distinct levels:
1. **Content Filter Level**: For standard pages, Elementor hooks into `the_content` at priority `Frontend::THE_CONTENT_FILTER_PRIORITY` (default `999999`). It replaces the post content with the rendered builder markup (`Frontend::get_builder_content()`).
2. **Template Include Level**: For full-canvas layouts and Elementor Pro Theme Builder:
   - Filter: `template_include` (Priority `9999`) in `Elementor\Modules\PageTemplates\Module` and `ElementorPro\Modules\ThemeBuilder\Classes\Locations_Manager`.
   - When **Elementor Canvas** is selected: It overrides the theme's header, footer, and sidebar, loading a blank HTML shell (`elementor/modules/page-templates/templates/canvas.php`) containing only `wp_head()`, `the_content()`, and `wp_footer()`.
   - When **Elementor Full Width** is selected: It loads `header.php`, renders the Elementor content in a 100% wide container without theme container constraints, and loads `footer.php`.
   - When **Theme Builder Locations** are active: Theme Builder intercepts calls to `get_header()`, `get_footer()`, `get_sidebar()`, or template parts, replacing them with the assigned Elementor header/footer template.

---

## 4. Hook Lifecycle & Elementor Registration
Elementor initializes during standard WordPress hook execution:

```
muplugins_loaded
   ↓
plugins_loaded
   ↓ (Elementor Free bootstraps: Elementor\Plugin::instance())
   ↓ (Elementor Pro bootstraps: ElementorPro\Plugin::instance())
after_setup_theme
   ↓ (Theme features registered: add_theme_support('elementor'))
init
   ↓ (Post types registered: 'elementor_library', 'elementor_font')
   ↓ (elementor/init action fires)
   ↓ (elementor/widgets/register action fires)
   ↓ (elementor/controls/register action fires)
wp_loaded
   ↓
parse_request
   ↓
wp
   ↓ (Frontend document initialized for queried object)
template_redirect
   ↓ (Preview mode detection, Theme Builder location evaluation)
wp_enqueue_scripts
   ↓ (Elementor frontend styles & scripts enqueued)
the_content
   ↓ (apply_builder_in_content() replaces post_content with rendered elements)
wp_footer
   ↓ (Frontend JS initializers, lightbox markup printed)
```

---

## 5. Security & Capability Management
- Capability Check: `current_user_can( 'edit_post', $post_id )` is enforced on all save, autosave, and preview requests.
- Nonce Verification: Elementor editor AJAX requests use `wp_verify_nonce( $_REQUEST['_nonce'], 'elementor-ajax' )`.
- Unfiltered HTML: Only users with `unfiltered_html` capability are permitted to save custom HTML or scripts in the HTML widget or custom code modules.
- Output Escaping: All widget templates utilize WordPress escaping functions (`esc_html`, `esc_attr`, `esc_url`, `wp_kses_post`).
