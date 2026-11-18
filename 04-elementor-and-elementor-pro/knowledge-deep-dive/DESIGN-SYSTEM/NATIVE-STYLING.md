# Native Styling Capability Matrix (Zero Custom CSS Standard)

## 1. Zero Custom CSS Engineering Standard
The core principle of this engineering system is **Zero Custom CSS**.
Every style, layout, hover animation, responsive behavior, and visual treatment must be achieved through Elementor's native controls.

---

## 2. Comprehensive Design Requirement to Native Control Matrix

| # | Design Requirement | Anti-Pattern (PROHIBITED) | Native Elementor Solution | Exact Control Keys & Settings |
|---|---|---|---|---|
| 1 | Horizontal Layout (Row) | `display: flex; flex-direction: row;` in CSS | Container + Direction Control | `container_type: "flex"`, `flex_direction: "row"` |
| 2 | Vertical Layout (Stack) | `display: flex; flex-direction: column;` | Container + Direction Control | `container_type: "flex"`, `flex_direction: "column"` |
| 3 | Center Content Horizontally | `margin: 0 auto; text-align: center;` | Container Justify / Align Controls | `justify_content: "center"`, `align_items: "center"` |
| 4 | Space Between Items | `justify-content: space-between;` | Container Justify Content | `justify_content: "space-between"` |
| 5 | Element Gap / Spacing | `.item { margin-right: 20px; }` | Container Gaps Control | `gap: { "unit": "px", "row": "20", "column": "20" }` |
| 6 | Boxed Layout (1140px max) | `max-width: 1140px; margin: auto;` | Container Content Width | `content_width: "boxed"`, `boxed_width: { "unit": "px", "size": 1140 }` |
| 7 | Full Width Container | `width: 100vw; width: 100%;` | Container Content Width | `content_width: "full_width"` |
| 8 | Multi-Column Wrap | `flex-wrap: wrap;` in CSS | Container Flex Wrap Control | `flex_wrap: "wrap"` |
| 9 | Grid Layout (3 columns) | `display: grid; grid-template-columns:...`| Container Grid Layout | `container_type: "grid"`, `grid_columns_grid: { "unit": "fr", "size": 3 }` |
| 10 | Responsive Stacking | `@media (max-width:767px) { flex-col }` | Responsive Direction Control | `flex_direction: "row"`, `flex_direction_mobile: "column"` |
| 11 | Responsive Padding | `@media ... { padding: 15px }` | Responsive Dimensions Control | `padding: { ... }`, `padding_mobile: { ... }` |
| 12 | Linear Gradient Background | `background: linear-gradient(135deg...)` | Group Control Background | `background_background: "gradient"`, `background_gradient_type: "linear"`, `background_gradient_angle: { "size": 135 }` |
| 13 | Background Image Overlay | `::before { background: rgba(0,0,0,0.5) }`| Background Overlay Control | `background_overlay_background: "classic"`, `background_overlay_color: "rgba(0,0,0,0.5)"`, `background_overlay_opacity: { "size": 0.5 }` |
| 14 | Parallax Background | `background-attachment: fixed;` | Background Attachment Control | `background_attachment: "fixed"` |
| 15 | Rounded Corners (Pill/Card)| `border-radius: 12px;` | Border Radius Control | `border_radius: { "unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": true }` |
| 16 | Circular Avatar | `border-radius: 50%;` | Border Radius Control | `border_radius: { "unit": "%", "top": "50", "right": "50", "bottom": "50", "left": "50", "isLinked": true }` |
| 17 | Card Drop Shadow | `box-shadow: 0 10px 25px rgba(0,0,0,0.1);`| Group Control Box Shadow | `box_shadow_box_shadow_type: "yes"`, `box_shadow_box_shadow: { "horizontal": 0, "vertical": 10, "blur": 25, "spread": 0, "color": "rgba(0,0,0,0.1)" }` |
| 18 | Text Shadow | `text-shadow: 0 2px 4px rgba(0,0,0,0.3);` | Group Control Text Shadow | `text_shadow_text_shadow_type: "yes"`, `text_shadow_text_shadow: { "horizontal": 0, "vertical": 2, "blur": 4, "color": "rgba(0,0,0,0.3)" }` |
| 19 | Responsive Typography | `@media (max-width:767px) { font-size:... }`| Responsive Typography Size | `typography_font_size: { "unit": "px", "size": 48 }`, `typography_font_size_mobile: { "unit": "px", "size": 32 }` |
| 20 | Button Hover State | `button:hover { background: #... }` | Native Button Hover Tab | `button_background_hover_color: "#1d4ed8"`, `hover_color: "#ffffff"` |
| 21 | Button Hover Grow Anim | `button:hover { transform: scale(1.05) }` | Native Hover Animation | `hover_animation: "grow"` |
| 22 | Image Aspect Ratio Cropping | `object-fit: cover; height: 300px;` | Image Height + Object Fit | `height: { "unit": "px", "size": 300 }`, `object_fit: "cover"` |
| 23 | Sticky Header | `position: sticky; top: 0;` in CSS | Pro Motion FX Sticky | `sticky: "top"`, `sticky_on: ["desktop", "tablet", "mobile"]` |
| 24 | Entrance Animations | `@keyframes fadeInUp { ... }` | Native Effects Section | `animation: "fadeInUp"`, `animation_duration: "normal"`, `animation_delay: 200` |
| 25 | SVG Dividers / Waves | Custom SVG code or background image | Native Shape Divider | `shape_divider_bottom: "waves"`, `shape_divider_bottom_color: "#ffffff"` |
| 26 | Z-Index Layering | `z-index: 10;` in CSS | Advanced Z-Index Control | `z_index: 10` |
| 27 | Absolute / Fixed Pinning | `position: absolute; top: 20px;` | Advanced Positioning Control | `position: "absolute"`, `_offset_orientation_h: "start"`, `_offset_x: { "unit": "px", "size": 20 }` |
| 28 | CSS Blur / Grayscale Filter | `filter: grayscale(100%);` in CSS | Group Control CSS Filter | `css_filters_css_filter: "custom"`, `css_filters_saturate: { "size": 0 }`, `css_filters_blur: { "size": 4 }` |
| 29 | Blend Modes | `mix-blend-mode: multiply;` | Native Blend Mode Control | `blend_mode: "multiply"` or `overlay_blend_mode: "overlay"` |
| 30 | Device Visibility Toggling | `@media (max-width: 767px) { display:none }`| Responsive Visibility | `hide_mobile: "hidden"` |

---

## 3. Strict Audit Standard: Detecting Violations
Any generated Elementor document containing the following strings is deemed **in violation of the zero-CSS standard**:
- `custom_css`: Any value inside widget or container settings.
- `<style>`: Any inline style block inside an HTML widget or Text Editor widget.
- `style="..."`: Any manual HTML inline style attribute.
- `.custom-class { ... }`: CSS code snippets inserted in page settings or site customizer.
