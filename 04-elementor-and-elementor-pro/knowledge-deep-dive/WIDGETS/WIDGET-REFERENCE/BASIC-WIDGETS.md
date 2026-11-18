# Widget Reference: Basic Widgets

## 1. Heading (`heading`)
- **Origin**: Elementor Free
- **Class**: `\Elementor\Widget_Heading` (`elementor/includes/widgets/heading.php`)
- **DOM Output**: `<{{{ header_size }}} class="elementor-heading-title elementor-size-{{{ size }}}">{{{ title }}}</{{{ header_size }}}>`
- **Settings Data Contract**:
  ```json
  {
    "title": "Build Faster with Elementor Native Architecture",
    "header_size": "h1",
    "size": "default",
    "align": "left",
    "align_tablet": "center",
    "align_mobile": "center",
    "title_color": "#111827",
    "typography_typography": "custom",
    "typography_font_family": "Inter",
    "typography_font_size": { "unit": "px", "size": 48 },
    "typography_font_size_mobile": { "unit": "px", "size": 32 },
    "typography_font_weight": "700",
    "typography_line_height": { "unit": "em", "size": 1.2 },
    "text_stroke_text_stroke_type": "yes",
    "text_stroke_stroke": { "unit": "px", "size": 1 },
    "text_stroke_stroke_color": "#000000"
  }
  ```
- **Zero-CSS Replacements**:
  - Eliminates media queries for heading typography scaling (`typography_font_size_mobile`).
  - Eliminates CSS `text-shadow` and `webkit-text-stroke`.
  - Eliminates text alignment utility classes (`align_mobile: "center"`).

---

## 2. Image (`image`)
- **Origin**: Elementor Free
- **Class**: `\Elementor\Widget_Image` (`elementor/includes/widgets/image.php`)
- **Settings Data Contract**:
  ```json
  {
    "image": {
      "id": 1420,
      "url": "https://wpvision.ir/wp-content/uploads/2026/11/product-hero.webp"
    },
    "image_size": "large",
    "align": "center",
    "width": { "unit": "%", "size": 100 },
    "max_width": { "unit": "px", "size": 800 },
    "height": { "unit": "px", "size": 450 },
    "object_fit": "cover",
    "border_radius": {
      "unit": "px",
      "top": "16",
      "right": "16",
      "bottom": "16",
      "left": "16",
      "isLinked": true
    },
    "box_shadow_box_shadow_type": "yes",
    "box_shadow_box_shadow": {
      "horizontal": 0,
      "vertical": 12,
      "blur": 24,
      "spread": 0,
      "color": "rgba(0,0,0,0.08)"
    }
  }
  ```
- **Zero-CSS Replacements**:
  - Replaces CSS `object-fit: cover` and fixed aspect-ratio height calculations.
  - Replaces custom CSS box-shadows and responsive rounded corners.

---

## 3. Button (`button`)
- **Origin**: Elementor Free
- **Class**: `\Elementor\Widget_Button` (`elementor/includes/widgets/button.php`)
- **Settings Data Contract**:
  ```json
  {
    "text": "Get Started Today",
    "link": {
      "url": "https://wpvision.ir/get-started",
      "is_external": false,
      "nofollow": false
    },
    "size": "md",
    "selected_icon": {
      "value": "fas fa-arrow-right",
      "library": "fa-solid"
    },
    "icon_align": "row-reverse",
    "icon_indent": { "unit": "px", "size": 8 },
    "typography_typography": "custom",
    "typography_font_weight": "600",
    "button_text_color": "#ffffff",
    "background_color": "#2563eb",
    "hover_color": "#ffffff",
    "button_background_hover_color": "#1d4ed8",
    "border_radius": {
      "unit": "px",
      "top": "8",
      "right": "8",
      "bottom": "8",
      "left": "8",
      "isLinked": true
    },
    "button_box_shadow_box_shadow_type": "yes",
    "button_box_shadow_box_shadow": {
      "horizontal": 0,
      "vertical": 4,
      "blur": 12,
      "spread": 0,
      "color": "rgba(37,99,235,0.2)"
    },
    "hover_animation": "grow"
  }
  ```
- **Zero-CSS Replacements**:
  - Replaces hover color transitions, background color changes, grow scale animations, icon spacing, and shadow changes.
