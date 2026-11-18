---
name: woodmart-theme-engineering
description: Architects, customizes, and debugs the WoodMart theme for WooCommerce, covering theme options, WoodMart Core, Header Builder, AJAX shop & PJAX mechanics (.wd-page-content), product loops, swatches, mobile off-canvas drawers, RTL styling, and Elementor integration.
---

# WoodMart Theme Engineering

## Mission
Deliver seamless, high-performance, and upgrade-safe customizations for the WoodMart WooCommerce theme and its child theme without breaking PJAX lifecycle, native AJAX shop operations, swatches, quick view, or Elementor layouts.

## Activate When
Working on WoodMart theme overrides, WoodMart Core plugin interactions, Header Builder layouts, AJAX shop loops, mobile off-canvas filter drawers, product grid cards, swatch behaviors, sticky add-to-cart, performance settings, or resolving conflicts between WoodMart, WooCommerce, and Elementor / Elementor Pro.

---

## 1. WoodMart Architectural Baseline

### Core Structure & Components
- **Parent Theme**: `wp-content/themes/woodmart/` (Do not edit directly under any circumstance).
- **Child Theme**: `wp-content/themes/woodmart-child/` (Place template overrides, `functions.php`, and child assets here).
- **Companion Core Plugin**: `woodmart-core` (Provides custom post types like `woodmart_layout`, `woodmart_slide`, `woodmart_sidebar`, Elementor & WPBakery widget definitions, and theme options framework).
- **Theme Options Framework**: Stored in `wp_options` under `woodmart_options`. Accessed via `woodmart_get_opt( 'option_name', $default )`.

### Safe Extension Points
1. **Child Theme `functions.php`**: For lightweight filter/action hooks.
2. **Custom Domain Plugin**: For core business logic, custom AJAX filters, API endpoints, and database models.
3. **Template Overrides**: Placed under `woodmart-child/woocommerce/` or `woodmart-child/woodmart/` preserving exact directory hierarchy.
4. **Theme Actions**:
   - `woodmart_after_header`
   - `woodmart_before_shop_loop`
   - `woodmart_after_shop_loop`
   - `woodmart_shop_loop_buttons`
   - `woodmart_before_single_product_summary`
   - `woodmart_after_single_product_summary`

---

## 2. WoodMart AJAX Shop & PJAX Lifecycle

### Observed PJAX Architecture
WoodMart uses PJAX (PushState + AJAX) for smooth shop navigation and catalog filtering.
- **Request Trigger**: When pagination, sorting, or native filters are changed, WoodMart sends a GET request with `_pjax=.wd-page-content` (or configured container class).
- **Container Replacement**: Only the `.wd-page-content` or `.site-content` subtree is replaced, not the entire `<body>`.
- **Observed Request Shape**:
  ```text
  /shop/?filter_category=women,men&_pjax=.wd-page-content
  ```

### Critical PJAX JavaScript Events
When DOM replacement occurs via AJAX, standard `$(document).ready()` **does NOT re-fire**. You must hook into WoodMart's lifecycle events to re-bind custom listeners or re-init widgets:

```javascript
// Native jQuery PJAX completion
$(document).on('pjax:complete', function() {
    // Re-initialize custom scripts, sliders, tooltips, or sticky sidebars
    window.myCustomModule && window.myCustomModule.init();
});

// WoodMart specific AJAX success hooks
$(document).on('woodmart_ajax_success wdShopPageInit', function() {
    // Re-bind swatches, custom variation dropdowns, or lazy loaders
});

// After WoodMart quick-view modal opens
$(document).on('woodmart-quick-view-displayed', function() {
    // Initialize custom widgets inside the quick view modal
});
```

### Avoiding PJAX Double Requests & Conflicts
- **Single Handler Principle**: If a custom filter plugin manages catalog AJAX, either disable WoodMart's AJAX shop (`Theme Options -> Shop -> AJAX shop -> OFF`) or ensure the custom plugin intercepts before PJAX fires (`e.preventDefault()`, `e.stopImmediatePropagation()`).
- **Idempotent JS Bindings**: Use event delegation on stable document roots (`$(document).on('click', '.my-filter-item', ...)`), or remove existing listeners before binding to prevent duplicate API requests.

---

## 3. Elementor & WoodMart Integration Discipline

### WoodMart Elementor Widgets
WoodMart Core registers dedicated Elementor widgets prefixed with `wd_`:
- `wd_products` / `wd_products_tabs`: High-performance product grids with hover designs (base, alt, icons, quick, standard, button).
- `wd_categories`: Product category grids and carousels.
- `wd_carousel`: Swiper/Slick wrappers with built-in lazy loading and responsive break points.
- `wd_ajax_search`: Live search modal with SKU, price, and thumbnail queries.

### Flexbox Container & Sticky Sidebar Discipline
- In Elementor Flexbox Containers (`.e-con`), when a sticky widget or shortcode becomes active (`position: fixed`), its empty spacer in a flex column without an explicit `min-width` and `flex-shrink: 0` causes the column to shrink to `min-content` (e.g. ~115px-165px) when filtered results are sparse (such as 1 product).
- **The WoodMart + Elementor Fix**:
  1. **CSS**: Enforce defensive `min-width: 260px;` and `flex-shrink: 0;` on the filter column, sticky wrapper, and spacer.
  2. **JS**: Lock authoritative column width across scroll, window resize, and PJAX.
  3. **Scope Ready Triggers**: When refreshing product results via AJAX, strictly scope Elementor's `runReadyTrigger` to the product grid container element—never run it globally on the entire page or sidebar, which causes Sticky scroll listeners to double-bind and freeze shrunken widths.

---

## 4. Mobile Off-Canvas Filter Drawer & Navbar

### Class Contracts & Selectors
- **Drawer Trigger Button**: `.wd-open-filter`, `.wd-off-canvas-btn`
- **Sidebar Drawer Container**: `.wd-filter-sidebar`, `.wd-sidebar-hidden`
- **Backdrop Overlay**: `.wd-close-side`, `.wd-back-drop`
- **Bottom Navbar Integration**: WoodMart includes a mobile bottom navigation bar (`.wd-toolbar`). The shop filter button in this toolbar triggers the off-canvas drawer.

### Custom Mobile Filter Panel Behavior
- Mobile filters should operate on a **draft state**: selections edit temporary checkboxes/radios without immediate network requests.
- An explicit **Apply Button** commits the draft state, closes the off-canvas drawer (`$('.wd-close-side').trigger('click')`), and fires the single AJAX query.
- Cancel or clicking the backdrop overlay discards uncommitted draft selections and reverts the UI to the current active query state.

---

## 5. Swatches, Quick View & Variation Lifecycle

### Swatches
- WoodMart replaces standard WooCommerce variation dropdowns with HTML swatches (`.wd-swatches-grid`, `.wd-swatch`).
- When customizing variations, use `woodmart_swatches_list()` or hook into `woocommerce_dropdown_variation_attribute_options_html` with priority > 20.
- Ensure custom JS listens to `change` events on the hidden underlying `<select>` element that WooCommerce native scripts rely on.

### Sticky Add-to-Cart
- WoodMart provides a sticky add-to-cart bar (`.wd-sticky-btn`) on single product pages.
- If variations or volume options (e.g. 30ml, 50ml, 100ml) are customized, synchronize state bidirectionally between the main product summary and the sticky bar to avoid cart item mismatches.

---

## 6. RTL & Persian Typography Harmonization

### Bi-directional Rules
- WoodMart has first-class RTL support via `rtl.css`.
- Dual-language product titles (e.g. Persian main title + English secondary title):
  - Ensure container has `dir="rtl"` with `text-align: right` for Persian.
  - Wrap English titles in `<span dir="ltr" class="en-title">...</span>` with `text-align: left` and appropriate LTR typography font stack (e.g., Roboto / Inter).
  - Strip formatting delimiters (like pipe `|`) from display templates while preserving both language strings in data attributes or postmeta.

---

## 7. Performance & Caching Governance

1. **CSS Generator**: Use WoodMart's built-in CSS generator (`Theme Options -> Performance -> CSS`) to compile only enabled components into a single custom stylesheet.
2. **JS Scripts**:
   - Avoid aggressive JavaScript concatenation (Autoptimize / WP Rocket) if mobile buttons or sticky headers fail; WoodMart dynamically loads modular chunks via `woodmartThemeModule`.
   - Preload primary fonts (e.g., Vazirmatn / Dana / Roboto) locally; do not call external Google Fonts APIs in production environments.
3. **Product Image Sizing**: Ensure catalog thumbnails match the exact aspect ratio configured in WoodMart (`Theme Options -> Shop -> Product Styles -> Image size`).

---

## Related Skills
- `skills/elementor-theme-integration`
- `skills/advanced-woocommerce-filtering-ajax`
- `skills/woocommerce-engineering`
- `skills/custom-wordpress-plugin-engineering`
- `skills/performance-engineering`
