# 01 - WoodMart Architecture & Core Structure

## Overview
WoodMart is an enterprise-grade WooCommerce theme developed by XTemos, designed specifically for e-commerce performance, responsive UX, and extensive visual customization.

## Directory & Package Anatomy
```text
wp-content/themes/woodmart/
├── css/                     # Compiled stylesheets (base, shop, RTL, responsive)
├── inc/                     # Core PHP classes, admin, integration, theme setup
│   ├── classes/             # OOP controllers (Theme, Layout, Swatches, etc.)
│   ├── integrations/        # Elementor, WPBakery, WooCommerce, WPML integrations
│   ├── modules/             # Layouts, Header Builder, AJAX search, Pre-orders
│   ├── admin/               # Redux/XTemos Theme Settings panels
│   └── template-tags.php    # Public helper functions (woodmart_get_opt, etc.)
├── js/                      # Frontend JavaScript modules
│   ├── scripts/             # Modular JS components (ajaxSearch, swatches, pjax)
│   └── libs/                # Bundled libraries (magnific-popup, isotope, slick)
├── woocommerce/             # WooCommerce template overrides
├── header.php
├── footer.php
├── functions.php
└── style.css
```

## The Companion Plugin: `woodmart-core`
WoodMart functions in tandem with its companion plugin `woodmart-core`.
- **Responsibilities**:
  1. Registers Custom Post Types:
     - `woodmart_layout` (Custom layouts for Header, Single Product, Shop Archive, Checkout)
     - `woodmart_slide` (Slider elements)
     - `woodmart_sidebar` (Custom dynamic widget areas)
     - `woodmart_size_guide` (Sizing tables)
  2. Registers Elementor Widgets & WPBakery Shortcodes.
  3. Manages API communication with XTemos activation servers.

## Theme Settings Storage: Redux / XTemos Framework
- Storage location: Stored in `wp_options` under the option key `woodmart_options`.
- Data Format: A large associative array indexed by setting slugs.
- Access API:
  ```php
  // Always verify existence before invoking
  if ( function_exists( 'woodmart_get_opt' ) ) {
      $val = woodmart_get_opt( 'key_name', 'default_value' );
  }
  ```

## Safe Customization Principles
1. **Never Modify Parent Files**: Any edit in `wp-content/themes/woodmart/` is destroyed on the next theme update.
2. **Use Child Theme**: Place CSS tweaks in `woodmart-child/style.css` and lightweight hooks in `woodmart-child/functions.php`.
3. **Template Overrides**: Copy specific templates from `woodmart/woocommerce/` to `woodmart-child/woocommerce/` keeping the exact directory structure intact.
