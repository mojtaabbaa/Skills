# Group Controls: Architecture, Sub-Fields & JSON Schemas

## 1. Group Control Overview
Group controls (`\Elementor\Group_Control_Base`) bundle multiple atomic controls together to apply complex CSS standards (typography styles, multi-layer backgrounds, box shadows, flexbox layout rules) through a single API registration call.

---

## 2. Group Control Specifications

### A. Group_Control_Typography (`groups/typography.php`)
- **Registration**:
  ```php
  $this->add_group_control(
      Group_Control_Typography::get_type(),
      [
          'name' => 'title_typography',
          'selector' => '{{WRAPPER}} .title',
      ]
  );
  ```
- **Generated Sub-Fields**:
  - `{name}_typography`: `'custom'` or `''`
  - `{name}_font_family`: Font name (e.g. `'Inter'`, `'Roboto'`)
  - `{name}_font_size`: Slider object with unit (`px`, `rem`, `em`, `vw`)
  - `{name}_font_weight`: `'100'` through `'900'`, `'normal'`, `'bold'`
  - `{name}_text_transform`: `'uppercase'`, `'lowercase'`, `'capitalize'`, `'none'`
  - `{name}_font_style`: `'normal'`, `'italic'`, `'oblique'`
  - `{name}_text_decoration`: `'underline'`, `'overline'`, `'line-through'`, `'none'`
  - `{name}_line_height`: Slider object with unit (`px`, `em`, `rem`)
  - `{name}_letter_spacing`: Slider object (`px`, `em`)
  - `{name}_word_spacing`: Slider object (`px`, `em`)
- **JSON Serialization in `settings`**:
  ```json
  "title_typography_typography": "custom",
  "title_typography_font_family": "Inter",
  "title_typography_font_size": { "unit": "px", "size": 36 },
  "title_typography_font_size_tablet": { "unit": "px", "size": 28 },
  "title_typography_font_size_mobile": { "unit": "px", "size": 24 },
  "title_typography_font_weight": "700",
  "title_typography_line_height": { "unit": "em", "size": 1.2 },
  "title_typography_letter_spacing": { "unit": "px", "size": -0.5 }
  ```

---

### B. Group_Control_Background (`groups/background.php`)
- **Types**: Classic (color/image) or Gradient (linear/radial)
- **Classic Sub-Fields**:
  - `{name}_background`: `'classic'`
  - `{name}_color`: Hex or RGBA string
  - `{name}_image`: Media object (`id`, `url`)
  - `{name}_position`: `'center center'`, `'top left'`, etc.
  - `{name}_attachment`: `'scroll'`, `'fixed'` (parallax effect)
  - `{name}_repeat`: `'no-repeat'`, `'repeat'`
  - `{name}_size`: `'cover'`, `'contain'`, `'auto'`, `'custom'`
- **Gradient Sub-Fields**:
  - `{name}_background`: `'gradient'`
  - `{name}_color`: First color stop
  - `{name}_color_stop`: Slider (0-100%)
  - `{name}_color_b`: Second color stop
  - `{name}_color_b_stop`: Slider (0-100%)
  - `{name}_gradient_type`: `'linear'` or `'radial'`
  - `{name}_gradient_angle`: Slider (0-360 degrees)
- **JSON Serialization (Linear Gradient)**:
  ```json
  "background_background": "gradient",
  "background_color": "#1e3a8a",
  "background_color_stop": { "unit": "%", "size": 0 },
  "background_color_b": "#3b82f6",
  "background_color_b_stop": { "unit": "%", "size": 100 },
  "background_gradient_type": "linear",
  "background_gradient_angle": { "unit": "deg", "size": 135 }
  ```

---

### C. Group_Control_Border (`groups/border.php`)
- **Sub-Fields**:
  - `{name}_border`: `'solid'`, `'double'`, `'dotted'`, `'dashed'`, `'groove'`, `''` (none)
  - `{name}_width`: Dimensions object (top, right, bottom, left)
  - `{name}_color`: Color string
- **JSON Serialization**:
  ```json
  "border_border": "solid",
  "border_width": { "unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": true },
  "border_color": "#e5e7eb"
  ```

---

### D. Group_Control_Box_Shadow (`groups/box-shadow.php`)
- **Sub-Fields**:
  - `{name}_box_shadow_type`: `'yes'`
  - `{name}_box_shadow`: Object with `horizontal`, `vertical`, `blur`, `spread`, `color`, `position` (`outline` or `inset`)
- **JSON Serialization**:
  ```json
  "box_shadow_box_shadow_type": "yes",
  "box_shadow_box_shadow": {
    "horizontal": 0,
    "vertical": 8,
    "blur": 20,
    "spread": -2,
    "color": "rgba(0, 0, 0, 0.08)",
    "position": "outline"
  }
  ```

---

### E. Group_Control_Flex_Container (`groups/flex-container.php`)
Used natively on `Container` elements to drive Flexbox layouts without manual CSS:
- **Sub-Fields**:
  - `direction`: `'row'`, `'column'`, `'row-reverse'`, `'column-reverse'`
  - `justify_content`: `'flex-start'`, `'center'`, `'flex-end'`, `'space-between'`, `'space-around'`, `'space-evenly'`
  - `align_items`: `'flex-start'`, `'center'`, `'flex-end'`, `'stretch'`, `'baseline'`
  - `flex_wrap`: `'nowrap'`, `'wrap'`, `'wrap-reverse'`
  - `align_content`: `'flex-start'`, `'center'`, `'flex-end'`, `'stretch'`, `'space-between'`, `'space-around'`
  - `gap`: Gaps object (`row`, `column`, `unit`, `isLinked`)
- **JSON Serialization**:
  ```json
  "flex_direction": "row",
  "flex_direction_mobile": "column",
  "justify_content": "space-between",
  "align_items": "center",
  "flex_wrap": "wrap",
  "gap": { "unit": "px", "row": "24", "column": "24", "isLinked": true }
  ```

---

### F. Group_Control_Flex_Item (`groups/flex-item.php`)
Controls the positioning of a widget or child container inside a parent Flexbox container:
- **Sub-Fields**:
  - `align_self`: `'auto'`, `'flex-start'`, `'center'`, `'flex-end'`, `'stretch'`
  - `order`: Slider (`px` integer for CSS `order`)
  - `size`: Slider or dimensions for flex-grow and flex-shrink
  - `basis_type`: `''` (default) or `'custom'`
  - `basis`: Slider object (`px`, `%`, `vw`) for `flex-basis`
- **JSON Serialization**:
  ```json
  "align_self": "center",
  "order_mobile": 2,
  "basis_type": "custom",
  "basis": { "unit": "%", "size": 48 },
  "basis_mobile": { "unit": "%", "size": 100 }
  ```
