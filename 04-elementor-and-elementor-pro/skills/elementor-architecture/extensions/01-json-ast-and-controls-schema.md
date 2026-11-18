# Extension 01: Elementor JSON AST & Controls Schema Dictionary (`_elementor_data`)

Fills the serialization gap on top of the source-verified `elementor-architecture` Core (v4.2.3 / Pro v4.3.2). Use this reference whenever reading, generating, or patching raw `_elementor_data` JSON via MCP, REST API, or WP-CLI. **100% Brand-Agnostic** — always inject colors & font families from the target site's active Elementor Kit or global `brand-<project>` skill.

---

## 1. Core AST Structure & Flattening Rules

Every node inside `_elementor_data` follows this JSON schema:

```json
{
  "id": "a1b2c3d",
  "elType": "container",
  "isInner": false,
  "widgetType": "heading",
  "settings": {},
  "elements": []
}
```
*(Omit `widgetType` on containers; use `id` of 7 unique lowercase hex/alphanumeric characters.)*

### Binding Serialization Laws (Non-Atomic Classic & Flexbox/Grid)
1. **Tab Flattening Law:** Elementor does **NOT** nest controls under `content`, `style`, or `advanced` keys in `_elementor_data`. All controls across all three tabs flatten directly into `settings`.
2. **CRITICAL Container-vs-Widget Prefix Law (`common-base.php`):**
   - **On Containers (`elType: "container"`):** Bare keys (NO underscore): `margin`, `padding`, `z_index`, `css_classes`, `_element_id`, `animation`, `_title`.
   - **On Widgets (`elType: "widget"`):** Underscore-prefixed keys: `_margin`, `_padding`, `_z_index`, `_css_classes`, `_element_id`, `_animation`, `_element_width`, `_element_custom_width`.
   - *Violating this causes Elementor's CSS generator to silently store the key and drop the styling!*
3. **Mandatory `isInner`, `elements: []` & Navigator `_title` Law:**
   - Top-level section containers: `"isInner": false`, `"_title": "<Descriptive Section Label>"` (makes Elementor Navigator human-readable instead of 15 anonymous `"Container"` rows!).
   - Nested child containers: `"isInner": true`.
   - Every widget node MUST include `"isInner": false` and `"elements": []`.
   - Strict JSON hygiene: NO comments (`/* */` / `//`), NO trailing commas, unique 7–8 char hex IDs, and HEX/RGBA color values only (never bare `"white"` or `"black"`).
4. **Responsive Suffix Law:**
   - Desktop: `<control>` (e.g. `padding`, `width`, `flex_direction`, `typography_font_size`)
   - Tablet: `<control>_tablet`
   - Mobile: `<control>_mobile` (e.g. `width_mobile`, `flex_direction_mobile`, `typography_font_size_mobile`, `padding_mobile`)
5. **Mandatory Enable-Flag Law (Zero Silent Drops):**
   - Typography keys are ignored unless `<prefix>_typography: "custom"` is explicitly set.
   - Background colors/images/gradients are ignored unless `background_background: "classic" | "gradient" | "video"` is set first (same for `background_overlay_background: "classic"`).
   - Image CSS filters are ignored unless `css_filters_css_filter: "custom"` is set.
   - **Overlay Opacity Quirk:** `background_overlay_opacity` requires `{"unit": "px", "size": 0.45}` (yes, `unit: "px"` for a `0–1` float!).

---

## 1.5. The 6 Silent Flexbox/Grid & Zero-Cascade Layout Traps (Battle-Tested!)

> [!CAUTION]
> Elementor silently stores invalid or conflicting layout keys with ZERO error message. Obey these 6 laws on every container and widget:

1. **The `content_width: "boxed"` Flex-Child Collapse Trap:** Child containers inside a horizontal flex row (`flex_direction: "row"`) default to `content_width: "boxed"` (`e-con-boxed`), which forces `width: 100%` and collapses multi-column card grids into vertical stacks! **Fix:** Every flex child container with an explicit width (`48.5%`, `31.5%`, `340px`) MUST set **`content_width: "full"`** (the outer row wrapper may stay `"boxed"`).
2. **The Column Default `flex_align_items: "center"` Trap:** A column container (`flex_direction: "column"`) without explicit `flex_align_items` gets `"center"` injected by Elementor — breaking right-aligned Persian headings/paragraphs inside cards! **Fix:** ALWAYS explicitly set **`flex_align_items: "stretch"`** on column containers unless you genuinely want centered content (like a centered CTA).
3. **The `_flex_grow: "1"` Sibling-Collapse Trap:** When a horizontal row places a growing text column next to a fixed-width avatar/badge/icon, setting `_flex_grow: "1"` alone shrinks the badge to `0px`! **Fix:** Pair BOTH sides explicitly — growing column gets `_flex_size: "grow"` + `_flex_grow: "1"`, fixed sibling gets **`_flex_size: "none"`**.
4. **The `flex_gap` vs `gap` Silent-Drop Trap:** Elementor's CSS generator reads ONLY **`flex_gap`** (`--gap`/`--row-gap`), NEVER `gap`.
5. **The Grid Dual-Axis Object Trap:** On `container_type: "grid"`, ALWAYS pass BOTH `grid_columns_grid` (CSS string: `"repeat(3, 1fr)"`) AND **`grid_rows_grid` as an object** (`{"unit": "fr", "size": 1, "sizes": []}`). Passing a string or omitting `grid_rows_grid` makes Elementor render a phantom empty 2nd row!
6. **Zero-Cascade, Kit `20px` Widget Spacing & Inline Button Traps:**
   - **Zero Cascade:** Elementor widgets do NOT inherit CSS typography/color cleanly from parent containers — every `heading`, `text-editor`, and `button` MUST bind `__globals__` OR explicitly declare `typography_typography: "custom"`, font family, size, weight, line-height (`1.75–1.9` for Persian body), and color (otherwise ugly Kit `#6EC1E4` / `#7A7A7A` / `1.2` defaults leak in!).
   - **Kit `20px` Default Gap:** Elementor adds ~20px spacing between stacked widgets via `--widgets-spacing`; control vertical rhythm with container `flex_gap` instead of spacer widgets, and deploy the Kit trailing-`<p>` reset (`Extension 06`).
   - **Side-by-Side Buttons:** Set `_element_width: "auto"` + explicit `typography_line_height` on each button so two buttons sit inline instead of stacking full-width at `line-height: 1`.
   - **Persian RTL Locale (`fa_IR`) Guard:** When WordPress `WPLANG` is `fa_IR`, Elementor natively flips flex row start/end right-to-left — NEVER blindly add `row-reverse` on RTL sites without checking live render first!

---

## 2. Standard Control Value Object Schemas

- **Dimensions (`padding`, `margin`, `border_width`, `border_radius`, `image_border_radius`):**
  `{"unit": "px", "top": "24", "right": "24", "bottom": "24", "left": "24", "isLinked": true}`
- **Slider (`width`, `min_height`, `typography_font_size`, `percent`):**
  `{"unit": "px", "size": 22, "sizes": []}` (or `{"unit": "%", "size": 100}`)
- **Flex/Grid Gaps (`flex_gap`, `grid_gaps`):**
  `{"row": "16", "column": "20", "unit": "px", "isLinked": false}`
- **Media / Image (`image`, `bg_image`):**
  `{"url": "https://example.com/wp-content/uploads/img.webp", "id": 1234, "size": "", "alt": "...", "source": "library"}`
- **Icons (`selected_icon`, `icon`, `icon_active`):**
  FontAwesome: `{"value": "fas fa-shield-alt", "library": "fa-solid"}`
  SVG: `{"value": {"url": "https://.../icon.svg", "id": 71}, "library": "svg"}`
- **Typography Group (`<prefix>_typography`):** Set `<prefix>_typography: "custom"`, then `<prefix>_font_family`, `<prefix>_font_size`, `<prefix>_font_weight`, `<prefix>_line_height`.
- **Background Group:** `background_background: "classic" | "gradient"`, `background_color`, `background_color_b`, `background_gradient_type: "linear"`, `background_gradient_angle: {"unit": "deg", "size": 135}`.
- **Dynamic Tags (`__dynamic__`):**
  `"__dynamic__": {"link": "[elementor-tag id=\"3c1e433\" name=\"internal-url\" settings=\"%7B...%7D\"]"}`
- **Global Kit Binding (`__globals__`):**
  `"__globals__": {"title_color": "globals/colors?id=primary", "typography_typography": "globals/typography?id=primary"}`

---

## 3. Container Controls (`elType: "container"`)

- **Base:** `container_type` (`"flex"` | `"grid"`), `content_width` (`"boxed"` | `"full"`), `boxed_width` (slider), `width` (slider), `min_height`, `overflow` (`visible|hidden|auto`), `html_tag` (`div|section|article|aside|header|footer|main|nav`), `link`.
- **Flex (`Group_Control_Flex_Container`):** `flex_direction` (`row|column|row-reverse|column-reverse`), `flex_wrap` (`nowrap|wrap`), `flex_justify_content`, `flex_align_items`, `flex_gap`.
- **Flex Child (`Group_Control_Flex_Item`):** `_flex_align_self`, `_flex_order` (`start|end|custom`), `_flex_order_custom`, `_flex_size` (`none|grow|shrink|custom`), `_flex_grow`, `_flex_shrink`.
- **CSS Grid (`container_type: "grid"`):** `grid_columns_grid`, `grid_rows_grid`, `grid_gaps`, `grid_auto_flow`, `grid_justify_items`, `grid_align_items`.

---

## 4. High-Value Widget JSON Schemas & Control Traps

### `image` — CRITICAL `image_border_radius` Trap!
> [!CAUTION]
> On `widgetType: "image"`, the border radius control is explicitly registered in Elementor Core as **`image_border_radius`**. Passing generic `border_radius` or `_border_radius` is **silently ignored** by Elementor's CSS generator!

Key controls: `image`, `image_size`, `align`, `width`, `space`, `opacity`, `image_border_radius` (dimensions).

### `heading` & `text-editor`
- `heading`: `title`, `header_size` (`h2|h3|h4|div|p` — NEVER `h1` inside single-post `_elementor_data` if the theme outputs H1!), `align`, `title_color`, `typography_*`, `link`.
- `text-editor`: `editor` (clean HTML `<p>...</p>`), `align`, `text_color`, `typography_*`.

### `button`
- `text`, `link` (`{"url": "...", "is_external": false, "nofollow": false}`), `align`, `button_text_color`, `background_color`, `button_hover_text_color`, `background_hover_color`, `typography_*`, `border_radius`, `text_padding` (dimensions).

### `icon-box` & `icon-list`
- `icon-box`: `selected_icon`, `title_text`, `description_text`, `position` (`right|left|top`), `title_size`, `primary_color`, `title_color`, `description_color`, `title_typography_*`, `description_typography_*`.
- `icon-list`: `view` (`default|inline`), `icon_list` (repeater: `{"_id", "text", "link", "selected_icon"}`), `icon_color`, `icon_size`, `text_color`, `text_color_hover`, `icon_typography_*`.

### Interactive & Data Widgets (`accordion`, `tabs`, `toggle`, `counter`, `progress`, `alert`, `testimonial`, `divider`)
- **`accordion`:** `tabs` (`[{"_id", "tab_title", "tab_content"}]`), `title_html_tag` (`h3`), `icon`, `icon_active`, `icon_align` (`left|right`), `title_color`, `tab_active_color`, `title_background`, `content_color`, `content_background_color`, `title_typography_*`, `content_typography_*`, `border_width`, `border_color`.
- **`tabs`:** `type` (`horizontal|vertical`), `tabs` (`[{"_id", "tab_title", "tab_content"}]`), `tab_color`, `tab_active_color`, `tab_background_color`, `tab_active_background_color`, `content_color`, `content_background_color`, `tab_typography_*`, `content_typography_*`, `border_width`, `border_color`.
- **`toggle` (multiple open):** Same `tabs` repeater + `icon`, `icon_active`, `icon_align`, `title_color`, `tab_active_color`, `title_background`, `content_color`, `content_background_color`, `title_typography_*`, `content_typography_*`.
- **`counter`:** `starting_number`, `ending_number`, `prefix`, `suffix`, `duration` (ms, e.g. `1500`), `thousand_separator` (`"yes"|""`), `title`, `number_color`, `title_color`, `typography_number_*`, `typography_title_*`.
- **`progress`:** `title`, `percent` (slider `%`), `display_percentage` (`show|hide`), `inner_text`, `progress_type` (`""|info|success|warning|danger`), `bar_color`, `bar_bg_color`, `bar_height`, `bar_border_radius`, `title_color`, `percentage_color`, `typography_title_*`.
- **`alert`:** `alert_type` (`info|success|warning|danger`), `alert_title`, `alert_description`, `show_dismiss` (`show|none`), `title_color`, `description_color`, `typography_title_*`, `typography_description_*`.
- **`testimonial`:** `testimonial_content`, `testimonial_name`, `testimonial_job`, `testimonial_image`, `testimonial_image_position` (`aside|top`), `testimonial_alignment`, `content_color`, `name_color`, `job_color`, `content_typography_*`, `name_typography_*`, `job_typography_*`.
- **`divider`:** `style` (`solid|double|dotted|dashed|groove`), `weight` (slider), `color`, `width` (slider), `align`, `gap` (slider).
- **`call-to-action` (Pro):** `skin` (`classic|cover`), `bg_image`, `title`, `description`, `button`, `link`, `link_click` (`box|button`), `min-height`, `min-height_mobile`, `title_color`, `overlay_color`.

### WoodMart Custom Elementor Widgets (Only When WoodMart Is Active!)
- **`wd_title`:** `title`, `subtitle`, `after_title`, `align`, `title_custom_color`, `subtitle_custom_color`, `title_typography_*`, `subtitle_typography_*`.
- **`wd_products`:** `layout` (`carousel|grid`), `post_type` (`product|bestselling|sale`), `taxonomies` (`["<term_id>"]`), `items_per_page`, `slides_per_view` (`{"unit":"px","size":4}` + `_tablet` / `_mobile`), `spacing`, `products_color_scheme` (`dark|light|inherit`), `products_with_background`, `products_background`, `hide_out_of_stock` (`"yes"`), `pagination` (`arrows|bullets|links`), `scroll_carousel_init` (`"yes"`).
- **`wd_blog`:** `blog_design` (`masonry|default|mask|meta-image`), `items_per_page`, `orderby`, `slides_per_view`, `autoplay`.

---

## 5. Live Source Verification CLI

Whenever any widget control name is uncertain, NEVER guess — inspect the real Elementor v4.2.3 / Pro v4.3.2 PHP source directly:

```bash
python "~/.gemini/config/skills/elementor-architecture/scripts/inspect_widget.py" <widget_name>
```
