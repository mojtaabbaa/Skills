# Extension 05: ACF & WooCommerce Integrations, Verified Limitations & 5-Stage QA Validation

Consolidated from reverse-engineered Elementor Core v4.2.3 & Pro v4.3.2 deep-dive references (`ACF.md`, `WOOCOMMERCE.md`, `KNOWN-LIMITATIONS.md`, `VALIDATION-PROTOCOL.md`).

---

## 1. Advanced Custom Fields (ACF) Dynamic Binding Schema

Elementor Pro embeds native ACF support (`elementor-pro/modules/dynamic-tags/acf/`) with zero bridge plugins:

| Dynamic Tag Slug | Supported ACF Field Types | Target Elementor Controls |
| :--- | :--- | :--- |
| `acf-text` | Text, Textarea, Select, Radio, Button Group | `TEXT`, `TEXTAREA`, `WYSIWYG` |
| `acf-number` | Number, Range | `NUMBER`, `SLIDER` |
| `acf-image` | Image (Array, ID, or URL) | `MEDIA` |
| `acf-file` | File (URL or ID) | `URL`, Button links |
| `acf-url` | URL, Page Link, Link | `URL` |
| `acf-date-time` | Date Picker, Date Time Picker, Time Picker | `TEXT`, `DATE_TIME` |
| `acf-color` | Color Picker | `COLOR` |
| `acf-gallery` | Gallery (ACF Pro) | `GALLERY` |

### Dynamic Tag JSON Binding Example (`__dynamic__`)
```json
{
  "settings": {
    "title": "TBD",
    "__dynamic__": {
      "title": "[elementor-tag id=\"acf_91a2\" name=\"acf-date-time\" settings=\"%7B%22key%22%3A%22event_start_date%22%2C%22format%22%3A%22F%20j%2C%20Y%22%2C%22fallback%22%3A%22Date%20Announced%20Soon%22%7D\"]"
    }
  }
}
```
- **Repeaters & Flexible Content:** Pair Elementor Pro **Loop Builder / Loop Grid** with ACF post-object or relationship queries for repeatable card layouts.

---

## 2. WooCommerce & HPOS Integration (Elementor Pro 4.3.2)

- **Full HPOS Compliance:** Elementor Pro 4.3.2 declares full compatibility with WooCommerce High-Performance Order Storage (`custom_order_tables`) — never query legacy `wp_postmeta` for orders.
- **Theme Builder Locations:** `single-product` (`Documents\Product`) and `product-archive` (`Documents\Product_Archive`).
- **26 Dedicated Widgets & 13 Dynamic Tags:**
  - Single product essentials: `woocommerce-product-images`, `woocommerce-product-title`, `woocommerce-product-rating`, `woocommerce-product-price`, `woocommerce-product-short-description`, `woocommerce-product-stock`, `woocommerce-product-add-to-cart`, `woocommerce-product-meta`, `woocommerce-product-data-tabs`, `woocommerce-product-related`.
  - Commerce shell: `woocommerce-menu-cart` (header slide-out drawer), `woocommerce-cart`, `woocommerce-checkout`.
  - Bind any standard widget via Dynamic Tags (`woocommerce-add-to-cart` on Button URL, `product-image` on Image, `product-price` on Heading).

---

## 3. Verified Native Limitations & Strict Exception Protocol

Four confirmed native boundaries in Elementor Free 4.2.3 / Pro 4.3.2:
1. **Arbitrary CSS `clip-path: polygon(...)`:** Use native Shape Dividers or SVG via Image widget first.
2. **Multi-Branch Conditional Form Logic:** Split into focused forms or combine with Elementor Display Conditions on containers.
3. **Runtime Arithmetic Expressions in Dynamic Tags:** Pre-compute derived values server-side into custom postmeta, then render via Dynamic Tag.
4. **Arbitrary `::before` / `::after` `content` Strings:** Use Background Overlay, Divider icon, or child Icon / Text Path widget instead.

**Exception Protocol:** When a brief genuinely hits one of these 4 boundaries: (1) identify the exact limitation, (2) verify native alternatives, (3) notify user & get approval, (4) isolate any authorized custom CSS in a single documented block while keeping all other sections Zero-Custom-CSS.

---

## 4. 5-Stage Production QA Validation Protocol

Before marking any Elementor page or template production-ready:
1. **Stage 1 — Structural & JSON Validation:** Valid JSON; every root element has `elType: "container"`, `isInner: false`; unique 7–8 hex `id`/`_id` on every element & repeater item; authentic registered `widgetType` slugs; widgets have `elements: []`.
2. **Stage 2 — Zero-Custom-CSS Audit:** Confirm no unauthorized `custom_css`, `<style>` inside text/HTML controls, inline `style="..."`, or `html` widgets imitating native cards/buttons.
3. **Stage 3 — Frontend Rendering:** `the_content` renders compiled Elementor markup; `post-{id}.css` or inline `<style id="elementor-post-{id}">` exists in `<head>`; all `[elementor-tag ...]` shortcodes resolve cleanly.
4. **Stage 4 — Visual Editor Compatibility:** Elementor editor opens with zero JS/React console errors; every container/widget is selectable, editable, and saves cleanly to `wp_postmeta`.
5. **Stage 5 — Responsive & Visual QA:** Verify Desktop (`1440px`/`1200px`), Tablet (`1024px`/`768px`), and Mobile (`375px`/`414px`) — single-column mobile stack, `>= 44–48px` tap targets, zero horizontal overflow.

---

## 5. Production PHP Boilerplate References

Clean, ready-to-adapt Elementor Pro extension classes bundled in `references/sample-php/`:
- `references/sample-php/class-custom-product-card-widget.php` — Custom `Widget_Base` with typography, border & box-shadow group controls.
- `references/sample-php/class-custom-form-webhook-action.php` — Custom Elementor Pro `Action_Base` webhook form handler.
- `references/sample-php/class-custom-product-brand-tag.php` — Custom Elementor Pro `DynamicTags\Tag` implementation.
