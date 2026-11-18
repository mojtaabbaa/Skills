# WooCommerce & Elementor Pro Integration

## 1. WooCommerce Integration Architecture
Elementor Pro embeds an extensive WooCommerce engine (`elementor-pro/modules/woocommerce/`):
- **HPOS Compatibility**: Elementor Pro 4.3.2 declares full compatibility with WooCommerce High-Performance Order Storage (HPOS / Custom Order Tables). It does not query legacy postmeta for order retrieval.
- **Theme Builder Locations**: Registers `single-product` and `product-archive` locations.
- **Dedicated Widgets**: 26 specialized WooCommerce widgets.
- **Dynamic Tags**: 13 product-specific dynamic data tags.

---

## 2. Template Architecture: Single Product & Shop Archives

### A. Single Product Document (`Documents\Product`)
Replaces `single-product.php` with a modular visual canvas:
- Main 2-column layout:
  - Left Container: `woocommerce-product-images` (Product gallery with zoom lens and thumbnail slider).
  - Right Container:
    - `woocommerce-product-title` (H1)
    - `woocommerce-product-rating` (Stars + reviews count link)
    - `woocommerce-product-price` (Regular & sale price formatting)
    - `woocommerce-product-short-description` (Summary copy)
    - `woocommerce-product-stock` (In-stock indicator)
    - `woocommerce-product-add-to-cart` (AJAX cart button & quantity selector)
    - `woocommerce-product-meta` (SKU, categories, tags)
  - Bottom Container:
    - `woocommerce-product-data-tabs` (Description, Additional Information, Reviews)
    - `woocommerce-product-related` (Related products grid)

### B. Product Archive Document (`Documents\Product_Archive`)
Replaces `archive-product.php` and taxonomy archives (`product_cat`, `product_tag`):
- `woocommerce-archive-description`: Category hero title & banner description.
- `woocommerce-archive-products`: Main catalog grid with sorting dropdown, pagination, and sale badges.

---

## 3. Cart, Checkout & Mini-Cart

### A. Menu Cart (`woocommerce-menu-cart`)
- Embedded in headers: Displays a cart bag/basket icon with a dynamic item counter badge.
- Slide-Out Drawer: On click or hover, slides out a mini-cart panel showing cart line items, subtotal, and checkout buttons without page reloads.

### B. Cart Page (`woocommerce-cart`)
- Modern 2-column visual Cart replacing the legacy shortcode `[woocommerce_cart]`.
- Column 1: Order items table with thumbnail, product link, unit price, quantity spinner, line total, and coupon code input.
- Column 2: Cart Totals card, shipping calculator, tax calculation, and "Proceed to Checkout" button.

### C. Checkout Page (`woocommerce-checkout`)
- Modern 2-column visual Checkout replacing `[woocommerce_checkout]`.
- Column 1: Billing details, shipping details, and additional order notes.
- Column 2: "Your Order" summary table, payment gateway selection (Credit Card, PayPal, COD), terms acceptance checkbox, and "Place Order" button.

---

## 4. WooCommerce Dynamic Tags in Any Widget
Any standard Elementor widget can bind directly to product data using WooCommerce dynamic tags:
- Setting a Button link to dynamic tag `woocommerce-add-to-cart` turns any button into a 1-click cart action.
- Setting an Image widget to `product-image` pulls the current product thumbnail automatically.
- Setting a Heading widget to `product-price` displays live formatted pricing with currency symbols.
