# Widget Reference: WooCommerce Builder Widgets

## 1. Product Price (`woocommerce-product-price`)
- **Origin**: Elementor Pro
- **Class**: `\ElementorPro\Modules\Woocommerce\Widgets\Product_Price`
- **Settings Data Contract**:
  ```json
  {
    "align": "left",
    "align_mobile": "center",
    "price_color": "#059669",
    "typography_typography": "custom",
    "typography_font_size": { "unit": "px", "size": 32 },
    "typography_font_weight": "700",
    "sale_price_color": "#dc2626",
    "sale_price_typography_typography": "custom",
    "sale_price_typography_font_size": { "unit": "px", "size": 32 },
    "sale_price_typography_font_weight": "700",
    "regular_price_color": "#9ca3af",
    "regular_price_typography_typography": "custom",
    "regular_price_typography_font_size": { "unit": "px", "size": 20 },
    "regular_price_typography_text_decoration": "line-through"
  }
  ```
- **Zero-CSS Replacements**:
  - Replaces CSS `.price del`, `.price ins`, currency symbol alignment, and strike-through styling.

---

## 2. Product Add to Cart (`woocommerce-product-add-to-cart`)
- **Origin**: Elementor Pro
- **Class**: `\ElementorPro\Modules\Woocommerce\Widgets\Product_Add_To_Cart`
- **Settings Data Contract**:
  ```json
  {
    "button_text_color": "#ffffff",
    "button_background_color": "#2563eb",
    "button_background_hover_color": "#1d4ed8",
    "button_border_radius": { "unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": true },
    "quantity_border_border": "solid",
    "quantity_border_width": { "unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": true },
    "quantity_border_color": "#d1d5db",
    "quantity_border_radius": { "unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": true },
    "quantity_padding": { "unit": "px", "top": "10", "right": "14", "bottom": "10", "left": "14", "isLinked": false }
  }
  ```
- **Zero-CSS Replacements**:
  - Replaces WooCommerce native button overrides, quantity spinner styling, and spacing between quantity and cart button.

---

## 3. Product Images (`woocommerce-product-images`)
- **Origin**: Elementor Pro
- **Class**: `\ElementorPro\Modules\Woocommerce\Widgets\Product_Images`
- **Settings Data Contract**:
  ```json
  {
    "sale_flash": "show",
    "sale_flash_border_radius": { "unit": "px", "top": "4", "right": "4", "bottom": "4", "left": "4", "isLinked": true },
    "image_border_border": "solid",
    "image_border_width": { "unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": true },
    "image_border_color": "#e5e7eb",
    "image_border_radius": { "unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": true },
    "thumbnails_spacing": { "unit": "px", "size": 12 },
    "thumbnails_border_radius": { "unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": true }
  }
  ```
