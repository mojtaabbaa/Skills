# WoodMart Theme Options, Hooks & Filters Reference

## Core Function: `woodmart_get_opt()`
Retrieves theme settings configured in WoodMart Theme Settings.
```php
/**
 * Safely get WoodMart option with fallback
 *
 * @param string $opt_name Option key
 * @param mixed  $default  Fallback value
 * @return mixed
 */
$ajax_shop_enabled = function_exists('woodmart_get_opt') 
    ? woodmart_get_opt('ajax_shop', true) 
    : false;
```

Common Option Keys:
- `ajax_shop`: (boolean) Enable/disable AJAX on shop page.
- `ajax_scroll`: (boolean) Scroll to top after AJAX shop pagination.
- `shop_pagination`: ('pagination', 'more-btn', 'infinit') Type of pagination.
- `products_columns`: (int) Number of columns on desktop.
- `products_columns_mobile`: (int) Columns on mobile (usually '1' or '2').
- `product_design`: ('default', 'alt', 'icons', 'quick', 'base', 'standard') Card hover style.
- `quick_view`: (boolean) Enable quick view modal.
- `mobile_bottom_nav`: (boolean) Enable mobile bottom toolbar.

---

## Key WoodMart PHP Action Hooks

### Header & Navigation
- `woodmart_before_header`: Pre-header markup.
- `woodmart_after_header`: Right below header, before breadcrumbs/page title.
- `woodmart_header_builder`: Custom header rendering.

### Shop Loop & Archives
- `woodmart_before_shop_loop`: Pre-shop loop (used for filters, toolbar, orderby).
- `woodmart_after_shop_loop`: Post-shop loop (used for pagination, load more).
- `woodmart_shop_loop_buttons`: Action inside product cards for quick view, wishlist, compare.
- `woodmart_before_shop_page`: Before main shop container.
- `woodmart_after_shop_page`: After main shop container.

### Single Product
- `woodmart_before_single_product_summary`: Image gallery container.
- `woodmart_after_single_product_summary`: Tabs, related products, upsells.
- `woodmart_before_add_to_cart_form`: Right before add to cart button.
- `woodmart_sticky_atc_content`: Inside sticky add-to-cart bar.

---

## Key WoodMart PHP Filter Hooks

### Product Grid & Layout
- `woodmart_product_categories_args`: Modifies query arguments for category widgets.
- `woodmart_product_element_classes`: Adds CSS classes to product card containers.
- `woodmart_hover_image_size`: Filter thumbnail sizes used in hover previews.
- `woodmart_swatches_attribute_name`: Filter attributes converted to swatches.

### Header & Off-Canvas
- `woodmart_mobile_menu_args`: Customizes mobile off-canvas menu elements.
- `woodmart_toolbar_buttons`: Customizes icons/buttons in mobile bottom navigation.
