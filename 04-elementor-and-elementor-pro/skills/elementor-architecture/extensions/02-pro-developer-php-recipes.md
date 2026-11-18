# Extension 02: Elementor & Elementor Pro Developer PHP/JS Recipes

Consolidated from `elementor-pro-engineering` (including Loop Builder & Theme Builder Location references). Pairs directly with [`references/hooks-and-developer-api.md`](../references/hooks-and-developer-api.md) and [`references/widget-paradigms-and-rules.md`](../references/widget-paradigms-and-rules.md).

---

## 1. Registering a Custom Widget (`Widget_Base`)

Hook exclusively onto `elementor/widgets/register` (modern v3.5+ / v4.x API; never use deprecated `widgets_registered`):

```php
add_action( 'elementor/widgets/register', function( $widgets_manager ) {
    require_once __DIR__ . '/widgets/class-custom-card-widget.php';
    $widgets_manager->register( new \MyPlugin\Widgets\Custom_Card_Widget() );
} );
```

Key requirements inside the widget class:
- Declare `get_name()`, `get_title()`, `get_icon()`, `get_categories()`, `get_script_depends()`, `get_style_depends()`.
- Register controls in `protected function register_controls()` using `Controls_Manager::TAB_CONTENT`, `TAB_STYLE`, `TAB_ADVANCED` and mandatory `{{WRAPPER}}` selector prefix.
- Escape every rendered field in `protected function render()` (`esc_html`, `esc_attr`, `esc_url`, `wp_kses_post`).
- For Atomic V4 widgets (`Atomic_Widget_Base`) or Nested widgets (`Widget_Nested_Base`), follow [`rules/03-rules-widgets-engine-and-paradigms.md`](../rules/03-rules-widgets-engine-and-paradigms.md).

---

## 2. Custom Dynamic Tags (`elementor/dynamic_tags/register`)

Extend `\Elementor\Core\DynamicTags\Tag` (echoed output) or `\Elementor\Core\DynamicTags\Data_Tag` (returned array/value, e.g., images/URLs):

```php
add_action( 'elementor/dynamic_tags/register', function( $dynamic_tags_manager ) {
    require_once __DIR__ . '/tags/class-product-brand-tag.php';
    $dynamic_tags_manager->register( new \MyPlugin\DynamicTags\Product_Brand_Tag() );
} );
```

```php
namespace MyPlugin\DynamicTags;

use Elementor\Core\DynamicTags\Tag;
use Elementor\Modules\DynamicTags\Module as TagsModule;

class Product_Brand_Tag extends Tag {
    public function get_name()       { return 'myplugin-product-brand'; }
    public function get_title()      { return esc_html__( 'Product Brand', 'myplugin' ); }
    public function get_group()      { return [ 'woocommerce' ]; }
    public function get_categories() { return [ TagsModule::TEXT_CATEGORY ]; }

    public function render() {
        $terms = get_the_terms( get_the_ID(), 'product_brand' );
        if ( ! empty( $terms ) && ! is_wp_error( $terms ) ) {
            echo esc_html( $terms[0]->name );
        }
    }
}
```

---

## 3. Custom Elementor Pro Form Actions (`Action_Base`)

Register on `elementor_pro/forms/actions/register`:

```php
add_action( 'elementor_pro/forms/actions/register', function( $registrar ) {
    require_once __DIR__ . '/actions/class-custom-crm-action.php';
    $registrar->register( new \MyPlugin\Forms\Custom_CRM_Action() );
} );
```

```php
namespace MyPlugin\Forms;

use ElementorPro\Modules\Forms\Classes\Action_Base;
use Elementor\Controls_Manager;

class Custom_CRM_Action extends Action_Base {
    public function get_name()  { return 'custom_crm_action'; }
    public function get_label() { return esc_html__( 'Send to CRM', 'myplugin' ); }

    public function register_settings_section( $widget ) {
        $widget->start_controls_section( 'section_crm_settings', [
            'label'     => esc_html__( 'CRM Settings', 'myplugin' ),
            'condition' => [ 'submit_actions' => $this->get_name() ],
        ] );
        $widget->add_control( 'crm_api_endpoint', [
            'label' => esc_html__( 'API Endpoint', 'myplugin' ),
            'type'  => Controls_Manager::URL,
        ] );
        $widget->end_controls_section();
    }

    public function run( $record, $ajax_handler ) {
        $raw_fields = $record->get( 'fields' );
        $normalized = [];
        foreach ( $raw_fields as $id => $field ) {
            $normalized[ sanitize_key( $id ) ] = sanitize_text_field( $field['value'] );
        }
        $endpoint = esc_url_raw( $record->get_form_settings( 'crm_api_endpoint' )['url'] ?? '' );
        if ( empty( $endpoint ) ) {
            return;
        }
        $response = wp_remote_post( $endpoint, [
            'body'    => wp_json_encode( $normalized ),
            'headers' => [ 'Content-Type' => 'application/json' ],
            'timeout' => 10,
        ] );
        if ( is_wp_error( $response ) || wp_remote_retrieve_response_code( $response ) >= 400 ) {
            $ajax_handler->add_error_message( esc_html__( 'Failed to submit to CRM.', 'myplugin' ) );
        }
    }

    public function on_export( $element ) {
        unset( $element['crm_api_endpoint'] );
        return $element;
    }
}
```

---

## 4. Custom Query Filter Hook (`elementor/query/{$query_id}`)

Set `Query -> Query ID` in Posts / Portfolio / Loop Grid widget, then hook in PHP:

```php
add_action( 'elementor/query/featured_sale_products', function( $query ) {
    $meta_query   = $query->get( 'meta_query' ) ?: [];
    $meta_query[] = [ 'key' => '_special_offer', 'value' => 'yes', 'compare' => '=' ];
    $query->set( 'meta_query', $meta_query );
} );
```

---

## 5. Theme Builder Locations & Loop Builder Engineering

### Registering & Rendering Custom Theme Locations
```php
add_action( 'elementor/theme/register_locations', function( $location_manager ) {
    $location_manager->register_location( 'my_custom_sub_header', [
        'label'           => esc_html__( 'Sub Header', 'myplugin' ),
        'multiple'        => false,
        'edit_in_content' => true,
    ] );
} );

// In theme template:
if ( ! function_exists( 'elementor_theme_do_location' ) || ! elementor_theme_do_location( 'header' ) ) {
    get_template_part( 'template-parts/header' );
}
```

- **Template Types (`_elementor_template_type`):** `header`, `footer`, `single-post`, `product`, `product-archive`, `archive`, `loop-item`, `error-404`, `wp-page`, `wp-post`.
- **Display Conditions (`_elementor_conditions`):** e.g., `include/general`, `include/singular/product/in_cat:12`.

### Loop Builder Performance Rules
- **NEVER nest a Loop Grid inside another Loop Item template.**
- Use explicit image `width`/`height` + native `loading="lazy"` inside loop items (except above-the-fold LCP card!).
- When AJAX pagination (`Load on Click` / `Infinite Scroll`) replaces loop items, bind custom JS via `elementorFrontend.hooks` or delegated listeners.

---

## 6. Frontend JS Lifecycle Hook (`elementorFrontend.hooks`)

```javascript
jQuery(window).on('elementor/frontend/init', function () {
    elementorFrontend.hooks.addAction(
        'frontend/element_ready/myplugin_custom_card.default',
        function ($scope, $) {
            if ($scope.data('myplugin-initialized')) return;
            $scope.data('myplugin-initialized', true);
            // Idempotent widget init scoped strictly inside $scope
        }
    );
});
```
