# Elementor Document Data Structure & JSON Serialization Reference

## 1. Top-Level Post Meta Architecture
An Elementor-powered page relies on five primary post meta entries in `wp_postmeta`:

| Meta Key | Format | Type | Description |
|---|---|---|---|
| `_elementor_edit_mode` | String | Scalar | Must be set to `"builder"` to signal that Elementor owns the content. |
| `_elementor_template_type` | String | Scalar | Document type: `"wp-page"`, `"wp-post"`, `"header"`, `"footer"`, `"single-post"`, `"archive"`, `"product"`, `"loop"`. |
| `_elementor_data` | String | JSON | Serialized array of top-level containers/sections and their recursive children. |
| `_elementor_page_settings` | String/Null | JSON | Page-level settings: page title visibility, custom background, page layout template. |
| `_elementor_conditions` | Array/JSON | Array | Display condition strings for Theme Builder / Popup Builder templates. |

---

## 2. Element Tree Schema (`_elementor_data`)

The root of `_elementor_data` is a JSON Array containing top-level elements:

```json
[
  {
    "id": "7a3b4c1",
    "elType": "container",
    "isInner": false,
    "settings": { ... },
    "elements": [
      {
        "id": "2d5e8f0",
        "elType": "container",
        "isInner": true,
        "settings": { ... },
        "elements": [
          {
            "id": "9c1b7a4",
            "elType": "widget",
            "widgetType": "heading",
            "settings": { ... },
            "elements": []
          }
        ]
      }
    ]
  }
]
```

### Element Properties Specification

1. **`id` (String, Required)**:
   - 7 or 8 hex character unique identifier (e.g. `"3c53913f"`).
   - Generated in PHP via `\Elementor\Utils::generate_random_string()` (`substr(md5(uniqid()), 0, 7)`).
   - In JavaScript: `elementorCommon.helpers.getUniqueId()`.
2. **`elType` (String, Required)**:
   - `"container"`: Flexbox or Grid Container.
   - `"widget"`: Interactive content element.
   - Legacy: `"section"` and `"column"` (supported for backward compatibility, but modern construction must always use `"container"`).
3. **`isInner` (Boolean, Required for Containers)**:
   - `false`: For root/top-level containers.
   - `true`: For nested child containers inside another container.
   - Omitted or removed for widgets.
4. **`widgetType` (String, Required for Widgets)**:
   - The registered slug of the widget (e.g. `"heading"`, `"image"`, `"button"`, `"form"`, `"loop-grid"`, `"woocommerce-products"`).
5. **`settings` (Object, Required)**:
   - Key-value dictionary storing control values for that element.
6. **`elements` (Array, Required)**:
   - For containers: Array of child container objects or widget objects.
   - For widgets: Empty array `[]`.

---

## 3. Control Setting Data Contracts

### A. Scalar Controls (Text, Select, Switcher, Choose)
Stored as primitive strings or numbers:
```json
"title": "Welcome to Our Platform",
"header_size": "h1",
"align": "center",
"show_badge": "yes"
```

### B. Slider Control (Sizes, Spacing, Width)
Stored as an object with `unit` and `size`:
```json
"width": {
  "unit": "%",
  "size": 75
},
"min_height": {
  "unit": "vh",
  "size": 80
}
```

### C. Dimensions Control (Margin, Padding, Border Radius)
Stored as an object with 4 sides, unit, and link flag:
```json
"padding": {
  "unit": "px",
  "top": "40",
  "right": "24",
  "bottom": "40",
  "left": "24",
  "isLinked": false
},
"border_radius": {
  "unit": "px",
  "top": "12",
  "right": "12",
  "bottom": "12",
  "left": "12",
  "isLinked": true
}
```

### D. Media Control (Images, Icons, Video)
Stored as an object with `url` and attachment `id`:
```json
"image": {
  "id": 1420,
  "url": "https://example.com/wp-content/uploads/2026/11/hero-banner.webp"
}
```

### E. URL / Link Control
Stored as an object with `url`, `is_external`, `nofollow`, and `custom_attributes`:
```json
"link": {
  "url": "https://example.com/pricing",
  "is_external": false,
  "nofollow": false,
  "custom_attributes": ""
}
```

### F. Repeater Control (Tabs, Accordions, Icon Lists, Testimonials)
Stored as an array of item objects, where each item must contain an `_id`:
```json
"tabs": [
  {
    "_id": "item_1a2b3c",
    "tab_title": "Feature Overview",
    "tab_content": "Detailed overview of the platform features."
  },
  {
    "_id": "item_4d5e6f",
    "tab_title": "Technical Specs",
    "tab_content": "High performance technical specifications."
  }
]
```

---

## 4. Responsive Settings Serialization
Responsive controls append breakpoint suffixes to their base setting key:
- Desktop: Base key (e.g. `margin`, `padding`, `width`, `align`, `flex_direction`).
- Tablet: `<key>_tablet` (e.g. `margin_tablet`, `padding_tablet`, `align_tablet`, `flex_direction_tablet`).
- Mobile: `<key>_mobile` (e.g. `margin_mobile`, `padding_mobile`, `align_mobile`, `flex_direction_mobile`).

Example of a responsive Flexbox container configuration:
```json
"flex_direction": "row",
"flex_direction_tablet": "row",
"flex_direction_mobile": "column",
"padding": {
  "unit": "px",
  "top": "60",
  "right": "32",
  "bottom": "60",
  "left": "32",
  "isLinked": false
},
"padding_mobile": {
  "unit": "px",
  "top": "32",
  "right": "16",
  "bottom": "32",
  "left": "16",
  "isLinked": false
}
```

---

## 5. Design System Tokens & Dynamic Tags Serialization

### A. Global Tokens (`__globals__`)
When a setting is linked to a Global Color or Global Font from the active Kit, it is referenced inside the `__globals__` object using Elementor's internal data URI format:
```json
"settings": {
  "title_color": "",
  "__globals__": {
    "title_color": "globals/colors?id=primary",
    "typography_typography": "globals/typography?id=primary"
  }
}
```

### B. Dynamic Tags (`__dynamic__`)
When a field is linked to dynamic WordPress data, the raw setting is left empty or as a fallback, and the dynamic shortcode is placed inside `__dynamic__`:
```json
"settings": {
  "title": "",
  "__dynamic__": {
    "title": "[elementor-tag id=\"5281358\" name=\"post-title\" settings=\"%7B%7D\"]"
  }
}
```
The dynamic tag syntax:
`[elementor-tag id="{unique_id}" name="{tag_slug}" settings="{url_encoded_json_settings}"]`
This allows dynamic tags to accept arguments (e.g. before/after text, fallback strings, date formats).
