# 05 - WoodMart WooCommerce Ecosystem Integration

## Swatches & Variable Products
WoodMart transforms standard variation dropdowns into visual swatches (colors, images, and text buttons).

### Swatch Storage & Term Meta
- WoodMart stores swatch data in term metadata:
  - `woodmart_swatch_color`: Hex color code (e.g. `#ffffff`).
  - `woodmart_swatch_image`: Attachment ID for texture/image swatches.
  - `woodmart_swatch_size`: Size modifier for individual swatches.

### Programmatic Access to Swatches
```php
if ( function_exists( 'woodmart_has_swatches' ) && woodmart_has_swatches( $attribute_name ) ) {
    $swatches = woodmart_get_attribute_swatches( $attribute_name, $product_id );
    // Render custom swatch markup
}
```

## Quick View Modal Architecture
- Modal Container: `.wd-popup.wd-quick-view`
- AJAX Endpoint: `admin-ajax.php?action=woodmart_load_quick_view&id={product_id}`
- Lifecycle Hook:
  ```javascript
  $(document).on('woodmart-quick-view-displayed', function() {
      // Re-initialize custom scripts inside the quick view modal
      var $quickView = $('.wd-quick-view');
      // e.g. custom variation selectors, quantity +/- buttons
  });
  ```

## Wishlist & Compare Engine
WoodMart includes an ultra-lightweight, built-in Wishlist and Compare engine that eliminates the need for bulky third-party plugins (like YITH).
- Storage: Cookie-based for guests, user meta for authenticated users (`_woodmart_wishlist_products`).
- AJAX Actions:
  - `woodmart_add_to_wishlist`
  - `woodmart_remove_from_wishlist`
  - `woodmart_add_to_compare`
  - `woodmart_remove_from_compare`
- JavaScript Event:
  ```javascript
  $(document).on('woodmart_wishlist_save_success', function(event, response) {
      // Update custom header badge counters
      $('.my-custom-wishlist-count').text(response.count);
  });
  ```

## Sticky Add-to-Cart Bar
- Selector: `.wd-sticky-btn`
- Behavior: Appears at screen bottom on single product pages when the main add-to-cart button scrolls out of view.
- Synchronization Discipline: If your plugin modifies volume, fragrance size, or custom product add-ons, you must mirror the state changes to `.wd-sticky-btn` inputs so clicking the sticky button submits the exact selected options.
