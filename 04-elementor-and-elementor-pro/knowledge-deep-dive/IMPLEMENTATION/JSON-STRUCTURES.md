# Elementor Document JSON Schemas & Ready-to-Use Templates

## 1. Minimal Valid Root Container Schema
Every valid Elementor document must contain an array of root elements:

```json
[
  {
    "id": "e_root_01",
    "elType": "container",
    "isInner": false,
    "settings": {
      "content_width": "boxed",
      "boxed_width": { "unit": "px", "size": 1200 },
      "flex_direction": "column",
      "justify_content": "center",
      "align_items": "center",
      "padding": {
        "unit": "px",
        "top": "80",
        "right": "24",
        "bottom": "80",
        "left": "24",
        "isLinked": false
      },
      "padding_mobile": {
        "unit": "px",
        "top": "40",
        "right": "16",
        "bottom": "40",
        "left": "16",
        "isLinked": false
      }
    },
    "elements": []
  }
]
```

---

## 2. Hero Section Template (Heading + Subtitle + Buttons)

```json
{
  "id": "hero_section",
  "elType": "container",
  "isInner": false,
  "settings": {
    "content_width": "boxed",
    "boxed_width": { "unit": "px", "size": 1140 },
    "flex_direction": "column",
    "justify_content": "center",
    "align_items": "center",
    "gap": { "unit": "px", "row": "24", "column": "24", "isLinked": true },
    "padding": { "unit": "px", "top": "100", "right": "20", "bottom": "100", "left": "20", "isLinked": false },
    "background_background": "gradient",
    "background_color": "#0f172a",
    "background_color_b": "#1e293b",
    "background_gradient_type": "linear",
    "background_gradient_angle": { "unit": "deg", "size": 180 }
  },
  "elements": [
    {
      "id": "hero_badge",
      "elType": "widget",
      "widgetType": "button",
      "settings": {
        "text": "NEW RELEASE v4.3 • EXPLORE ARCHITECTURE",
        "size": "xs",
        "button_text_color": "#38bdf8",
        "background_color": "rgba(56, 189, 248, 0.1)",
        "border_border": "solid",
        "border_width": { "unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": true },
        "border_color": "rgba(56, 189, 248, 0.3)",
        "border_radius": { "unit": "px", "top": "20", "right": "20", "bottom": "20", "left": "20", "isLinked": true },
        "align": "center"
      },
      "elements": []
    },
    {
      "id": "hero_heading",
      "elType": "widget",
      "widgetType": "heading",
      "settings": {
        "title": "Engineering High-Performance WordPress with Elementor Native",
        "header_size": "h1",
        "align": "center",
        "title_color": "#ffffff",
        "typography_typography": "custom",
        "typography_font_family": "Inter",
        "typography_font_size": { "unit": "px", "size": 52 },
        "typography_font_size_tablet": { "unit": "px", "size": 38 },
        "typography_font_size_mobile": { "unit": "px", "size": 30 },
        "typography_font_weight": "800",
        "typography_line_height": { "unit": "em", "size": 1.15 }
      },
      "elements": []
    },
    {
      "id": "hero_subtitle",
      "elType": "widget",
      "widgetType": "text-editor",
      "settings": {
        "editor": "<p>Eliminate custom CSS. Leverage native flexbox containers, global design systems, dynamic tags, and compiled stylesheets directly from Elementor's core architecture.</p>",
        "align": "center",
        "text_color": "#94a3b8",
        "typography_typography": "custom",
        "typography_font_size": { "unit": "px", "size": 18 },
        "typography_line_height": { "unit": "em", "size": 1.6 }
      },
      "elements": []
    },
    {
      "id": "hero_actions_row",
      "elType": "container",
      "isInner": true,
      "settings": {
        "flex_direction": "row",
        "flex_direction_mobile": "column",
        "justify_content": "center",
        "align_items": "center",
        "gap": { "unit": "px", "row": "16", "column": "16", "isLinked": true }
      },
      "elements": [
        {
          "id": "btn_primary",
          "elType": "widget",
          "widgetType": "button",
          "settings": {
            "text": "Start Free Trial",
            "size": "md",
            "button_text_color": "#ffffff",
            "background_color": "#0284c7",
            "button_background_hover_color": "#0369a1",
            "border_radius": { "unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": true },
            "hover_animation": "grow"
          },
          "elements": []
        },
        {
          "id": "btn_secondary",
          "elType": "widget",
          "widgetType": "button",
          "settings": {
            "text": "View Documentation",
            "size": "md",
            "button_text_color": "#f8fafc",
            "background_color": "transparent",
            "border_border": "solid",
            "border_width": { "unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": true },
            "border_color": "#334155",
            "border_radius": { "unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": true }
          },
          "elements": []
        }
      ]
    }
  ]
}
```

---

## 3. 3-Column Feature Cards Row Template

```json
{
  "id": "features_row",
  "elType": "container",
  "isInner": true,
  "settings": {
    "flex_direction": "row",
    "flex_direction_tablet": "row",
    "flex_direction_mobile": "column",
    "justify_content": "space-between",
    "align_items": "stretch",
    "gap": { "unit": "px", "row": "24", "column": "24", "isLinked": true }
  },
  "elements": [
    {
      "id": "card_01",
      "elType": "container",
      "isInner": true,
      "settings": {
        "basis_type": "custom",
        "basis": { "unit": "%", "size": 31 },
        "basis_mobile": { "unit": "%", "size": 100 },
        "padding": { "unit": "px", "top": "32", "right": "24", "bottom": "32", "left": "24", "isLinked": true },
        "background_background": "classic",
        "background_color": "#ffffff",
        "border_border": "solid",
        "border_width": { "unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": true },
        "border_color": "#f1f5f9",
        "border_radius": { "unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": true },
        "box_shadow_box_shadow_type": "yes",
        "box_shadow_box_shadow": { "horizontal": 0, "vertical": 4, "blur": 16, "spread": 0, "color": "rgba(0,0,0,0.04)" }
      },
      "elements": [
        {
          "id": "card_01_box",
          "elType": "widget",
          "widgetType": "icon-box",
          "settings": {
            "selected_icon": { "value": "fas fa-bolt", "library": "fa-solid" },
            "view": "stacked",
            "shape": "circle",
            "primary_color": "#0284c7",
            "secondary_color": "#e0f2fe",
            "title_text": "Sub-Second Rendering",
            "description_text": "Pre-compiled CSS and minimal DOM trees deliver exceptional Google Lighthouse and Core Web Vitals scores.",
            "position": "top"
          },
          "elements": []
        }
      ]
    }
  ]
}
```
