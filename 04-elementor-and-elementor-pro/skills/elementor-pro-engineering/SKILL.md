---
name: elementor-pro-engineering
description: Deep engineering for Elementor and Elementor Pro, covering Theme Builder locations, custom Widget development, Dynamic Tags, Form Actions, Custom Query Hooks, Loop Builder, Popups, and Flexbox container architecture.
---

# Elementor & Elementor Pro Engineering

## Mission
Architect, implement, and extend Elementor and Elementor Pro via documented developer APIs (Widgets, Dynamic Tags, Form Actions, Query Filters, Theme Builder Locations) while maintaining zero DOM bloat, high Core Web Vitals performance, and robust server-side security.

## Activate When
Creating custom Elementor widgets, adding custom Dynamic Tags, writing Elementor Pro Form custom actions (webhooks, CRM, notifications), hooking custom WP_Query filters (`elementor/query/{$query_id}`), creating Theme Builder template locations, debugging Elementor container layout shifts, or automating page-building payloads via MCP or REST API.

---

## 1. Architectural Foundation & Version Baseline

### Core Engine Stack
- **Elementor Free Baseline**: v3.20+ / v4.x (Container engine default, responsive controls framework, CSS generator, editor assets).
- **Elementor Pro Baseline**: v3.20+ / v4.x (Theme Builder, Form engine, Popup engine, Dynamic Tags, Loop Builder, WooCommerce builder).
- **Storage Model**:
  - `_elementor_edit_mode`: `'builder'`
  - `_elementor_template_type`: `'wp-page'`, `'header'`, `'footer'`, `'single'`, `'archive'`, `'loop-item'`, etc.
  - `_elementor_data`: Serialized JSON array of containers (`elType: 'container'`) and widgets (`elType: 'widget'`).
  - `_elementor_page_settings`: Array of document-level settings (custom CSS, title hiding, layout canvas/fullwidth).

---

## 2. Custom Elementor Widget Development Protocol

### Registration Hook
Register widgets exclusively on `elementor/widgets/register`:
```php
add_action( 'elementor/widgets/register', function( $widgets_manager ) {
    require_once __DIR__ . '/widgets/class-custom-product-card-widget.php';
    $widgets_manager->register( new \MyPlugin\Widgets\Custom_Product_Card_Widget() );
} );
```

### Essential Widget Class Architecture
```php
namespace MyPlugin\Widgets;

use Elementor\Widget_Base;
use Elementor\Controls_Manager;
use Elementor\Group_Control_Typography;
use Elementor\Group_Control_Border;

if ( ! defined( 'ABSPATH' ) ) exit;

class Custom_Product_Card_Widget extends Widget_Base {

    public function get_name() {
        return 'myplugin_product_card';
    }

    public function get_title() {
        return esc_html__( 'Custom Product Card', 'myplugin' );
    }

    public function get_icon() {
        return 'eicon-product-price';
    }

    public function get_categories() {
        return [ 'woocommerce-elements', 'general' ];
    }

    protected function register_controls() {
        // Content Section
        $this->start_controls_section(
            'section_content',
            [
                'label' => esc_html__( 'Content', 'myplugin' ),
                'tab'   => Controls_Manager::TAB_CONTENT,
            ]
        );

        $this->add_control(
            'product_id',
            [
                'label'   => esc_html__( 'Product ID', 'myplugin' ),
                'type'    => Controls_Manager::NUMBER,
                'dynamic' => [ 'active' => true ],
            ]
        );

        $this->end_controls_section();

        // Style Section
        $this->start_controls_section(
            'section_style',
            [
                'label' => esc_html__( 'Style', 'myplugin' ),
                'tab'   => Controls_Manager::TAB_STYLE,
            ]
        );

        $this->add_group_control(
            Group_Control_Typography::get_type(),
            [
                'name'     => 'title_typography',
                'selector' => '{{WRAPPER}} .myplugin-product-title',
            ]
        );

        $this->end_controls_section();
    }

    protected function render() {
        $settings = $this->get_settings_for_display();
        // Server-side safe rendering with escaping
        echo '<div class="myplugin-product-card">';
        echo '<h3 class="myplugin-product-title">' . esc_html( $settings['product_id'] ) . '</h3>';
        echo '</div>';
    }
}
```

---

## 3. Elementor Pro Dynamic Tags Protocol

### Registration Hook
Register Dynamic Tags on `elementor/dynamic_tags/register`:
```php
add_action( 'elementor/dynamic_tags/register', function( $dynamic_tags_manager ) {
    require_once __DIR__ . '/tags/class-product-brand-tag.php';
    $dynamic_tags_manager->register( new \MyPlugin\DynamicTags\Product_Brand_Tag() );
} );
```

### Tag Class Architecture
Extends `\Elementor\Core\DynamicTags\Tag` or `\Elementor\Core\DynamicTags\Data_Tag`:
```php
namespace MyPlugin\DynamicTags;

use Elementor\Core\DynamicTags\Tag;
use Elementor\Modules\DynamicTags\Module as TagsModule;

class Product_Brand_Tag extends Tag {

    public function get_name() {
        return 'myplugin-product-brand';
    }

    public function get_title() {
        return esc_html__( 'Product Brand', 'myplugin' );
    }

    public function get_group() {
        return [ 'woocommerce' ];
    }

    public function get_categories() {
        return [ TagsModule::TEXT_CATEGORY ];
    }

    public function render() {
        $product_id = get_the_ID();
        $terms = get_the_terms( $product_id, 'product_brand' );
        if ( ! empty( $terms ) && ! is_wp_error( $terms ) ) {
            echo esc_html( $terms[0]->name );
        }
    }
}
```

---

## 4. Elementor Pro Custom Form Actions

### Architecture
Elementor Pro forms support custom actions after submission (e.g. CRM sync, SMS gateway, loyalty points).
Register on `elementor_pro/forms/actions/register`:
```php
add_action( 'elementor_pro/forms/actions/register', function( $form_actions_registrar ) {
    require_once __DIR__ . '/actions/class-custom-crm-action.php';
    $form_actions_registrar->register( new \MyPlugin\Forms\Custom_CRM_Action() );
} );
```

### Form Action Class Architecture
```php
namespace MyPlugin\Forms;

use ElementorPro\Modules\Forms\Classes\Action_Base;
use Elementor\Controls_Manager;

class Custom_CRM_Action extends Action_Base {

    public function get_name() {
        return 'custom_crm_action';
    }

    public function get_label() {
        return esc_html__( 'Send to CRM', 'myplugin' );
    }

    public function register_settings_section( $widget ) {
        $widget->start_controls_section(
            'section_crm_settings',
            [
                'label' => esc_html__( 'CRM Settings', 'myplugin' ),
                'condition' => [
                    'submit_actions' => $this->get_name(),
                ],
            ]
        );

        $widget->add_control(
            'crm_api_endpoint',
            [
                'label' => esc_html__( 'API Endpoint', 'myplugin' ),
                'type' => Controls_Manager::TEXT,
            ]
        );

        $widget->end_controls_section();
    }

    public function run( $record, $ajax_handler ) {
        $raw_fields = $record->get( 'fields' );
        $normalized = [];
        foreach ( $raw_fields as $id => $field ) {
            $normalized[ $id ] = sanitize_text_field( $field['value'] );
        }

        // Perform HTTP POST or business logic
        $response = wp_remote_post( 'https://api.example.com/lead', [
            'body' => json_encode( $normalized ),
            'headers' => [ 'Content-Type' => 'application/json' ],
            'timeout' => 10,
        ] );

        if ( is_wp_error( $response ) || wp_remote_retrieve_response_code( $response ) !== 200 ) {
            $ajax_handler->add_error_message( esc_html__( 'Failed to submit to CRM.', 'myplugin' ) );
        }
    }

    public function on_export( $element ) {}
}
```

---

## 5. Custom Query Filter Hook: `elementor/query/{$query_id}`

For Elementor Posts Widget, Portfolio Widget, or Loop Grid:
In the widget setting `Query -> Query ID`, enter a custom identifier (e.g. `featured_sale_products`).
In PHP, hook directly:
```php
add_action( 'elementor/query/featured_sale_products', function( $query ) {
    $meta_query = $query->get( 'meta_query' ) ?: [];
    $meta_query[] = [
        'key'     => '_special_offer',
        'value'   => 'yes',
        'compare' => '=',
    ];
    $query->set( 'meta_query', $meta_query );
} );
```

---

## 6. Frontend JS Lifecycle Hooks

When Elementor renders widgets or handles popups/AJAX:
```javascript
jQuery(window).on('elementor/frontend/init', function() {
    // Hook widget-specific initializers
    elementorFrontend.hooks.addAction('frontend/element_ready/myplugin_product_card.default', function($scope, $) {
        // $scope is the jQuery wrapped widget root
        var productId = $scope.find('.myplugin-product-card').data('product-id');
        // Initialize interactive tooltips, carousels, or click events
    });
});
```

---

## Related Skills
- `skills/elementor-theme-integration`
- `skills/woodmart-theme-engineering`
- `skills/custom-wordpress-plugin-engineering`
- `skills/performance-engineering`
