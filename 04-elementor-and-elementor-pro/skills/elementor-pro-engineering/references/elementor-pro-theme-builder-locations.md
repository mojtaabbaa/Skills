# Elementor Pro Theme Builder Locations Reference

## Overview
Theme Builder allows Elementor Pro to override entire theme template segments (Header, Footer, Single Post, Single Product, Archive, 404, Search).

## Registering Custom Locations in Theme/Plugin
If building custom theme templates or child themes:
```php
add_action( 'elementor/theme/register_locations', function( $location_manager ) {
    $location_manager->register_location(
        'my_custom_sub_header',
        [
            'label'           => esc_html__( 'Sub Header', 'myplugin' ),
            'multiple'        => false,
            'edit_in_content' => true,
        ]
    );
} );
```

## Rendering a Theme Builder Location
To output the user-designed Elementor template at a specific location:
```php
if ( ! function_exists( 'elementor_theme_do_location' ) || ! elementor_theme_do_location( 'header' ) ) {
    // Fallback to default theme header
    get_template_part( 'template-parts/header' );
}
```

## Elementor Pro Template Types & Post Meta
- `_elementor_template_type`:
  - `header`: Header template
  - `footer`: Footer template
  - `single-post`: Single post template
  - `product`: Single WooCommerce product
  - `product-archive`: WooCommerce Shop / Category archive
  - `archive`: Generic blog/tax archive
  - `loop-item`: Custom loop builder card
  - `error-404`: 404 page
- `_elementor_conditions`: Array defining conditional display rules (e.g. `include/general`, `include/singular/product/in_cat:12`).
