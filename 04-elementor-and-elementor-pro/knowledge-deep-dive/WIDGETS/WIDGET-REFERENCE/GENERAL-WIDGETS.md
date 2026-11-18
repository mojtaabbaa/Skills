# Widget Reference: General Widgets

## 1. Icon Box (`icon-box`)
- **Origin**: Elementor Free
- **Class**: `\Elementor\Widget_Icon_Box` (`elementor/includes/widgets/icon-box.php`)
- **Settings Data Contract**:
  ```json
  {
    "selected_icon": {
      "value": "fas fa-shield-alt",
      "library": "fa-solid"
    },
    "view": "stacked",
    "shape": "circle",
    "title_text": "Enterprise Security",
    "description_text": "SOC-2 certified cloud infrastructure with automated penetration testing.",
    "position": "top",
    "position_tablet": "top",
    "position_mobile": "top",
    "primary_color": "#2563eb",
    "secondary_color": "#eff6ff",
    "icon_size": { "unit": "px", "size": 28 },
    "icon_padding": { "unit": "px", "size": 18 },
    "title_color": "#111827",
    "title_typography_typography": "custom",
    "title_typography_font_size": { "unit": "px", "size": 20 },
    "title_typography_font_weight": "600",
    "description_color": "#4b5563",
    "description_typography_typography": "custom",
    "description_typography_font_size": { "unit": "px", "size": 15 },
    "description_typography_line_height": { "unit": "em", "size": 1.6 }
  }
  ```
- **Zero-CSS Replacements**:
  - Eliminates custom card markup, circular icon backgrounds, icon-to-title spacing, and responsive alignment.

---

## 2. Icon List (`icon-list`)
- **Origin**: Elementor Free
- **Class**: `\Elementor\Widget_Icon_List` (`elementor/includes/widgets/icon-list.php`)
- **Settings Data Contract**:
  ```json
  {
    "icon_list": [
      {
        "_id": "item_f1",
        "text": "99.99% Guaranteed SLA Uptime",
        "selected_icon": { "value": "fas fa-check-circle", "library": "fa-solid" }
      },
      {
        "_id": "item_f2",
        "text": "Dedicated 24/7 Support Engineering",
        "selected_icon": { "value": "fas fa-check-circle", "library": "fa-solid" }
      },
      {
        "_id": "item_f3",
        "text": "Automated Daily Disaster Recovery Backups",
        "selected_icon": { "value": "fas fa-check-circle", "library": "fa-solid" }
      }
    ],
    "view": "traditional",
    "space_between": { "unit": "px", "size": 12 },
    "icon_align": "left",
    "icon_color": "#10b981",
    "icon_size": { "unit": "px", "size": 18 },
    "text_color": "#374151",
    "text_typography_typography": "custom",
    "text_typography_font_size": { "unit": "px", "size": 16 }
  }
  ```
- **Zero-CSS Replacements**:
  - Replaces CSS `ul`/`li` custom reset styling, `list-style: none`, green checkmark inline styling, and vertical item spacing.

---

## 3. Accordion (`accordion`) & Nested Accordion (`nested-accordion`)
- **Origin**: Free
- **Settings Data Contract (Classic Accordion)**:
  ```json
  {
    "tabs": [
      {
        "_id": "faq_1",
        "tab_title": "How does automated migration work?",
        "tab_content": "Our migration agents transfer database records, postmeta, attachments, and configurations seamlessly."
      },
      {
        "_id": "faq_2",
        "tab_title": "What payment gateways are supported?",
        "tab_content": "We support Stripe, PayPal, WooCommerce Payments, Authorize.net, and custom regional gateways."
      }
    ],
    "selected_icon": { "value": "fas fa-chevron-down", "library": "fa-solid" },
    "selected_active_icon": { "value": "fas fa-chevron-up", "library": "fa-solid" },
    "title_color": "#111827",
    "tab_active_color": "#2563eb",
    "title_background": "#f9fafb",
    "border_border": "solid",
    "border_width": { "unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": true },
    "border_color": "#e5e7eb",
    "border_radius": { "unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": true }
  }
  ```
- **Zero-CSS Replacements**:
  - Replaces JavaScript accordion toggling, active border colors, open/close chevron animations, and panel padding.
