# Responsive Controls & Breakpoint Engine

## 1. Breakpoint Architecture & Viewport System
Elementor manages responsive viewports through `\Elementor\Core\Breakpoints\Manager` (`elementor/core/breakpoints/manager.php`).

### Default Breakpoint Thresholds
- **`mobile`**: Max-width `767px` (Min: `320px`)
- **`tablet`**: Max-width `1024px` (Min: `768px`)
- **`desktop`**: Base styling (Applies from `1025px` upwards, or acts as universal fallback)
- **Additional Optional Breakpoints**:
  - `mobile_extra`: `880px`
  - `tablet_extra`: `1200px`
  - `laptop`: `1366px`
  - `widescreen`: Min-width `2400px`

### Cascade & Inheritance Model
Elementor utilizes a **Desktop-Down Cascade** for standard viewports and a **Desktop-Up Cascade** for widescreen:
```
  [Mobile] (max-width: 767px)
     ↑ inherits from
  [Tablet] (max-width: 1024px)
     ↑ inherits from
  [Desktop] (Base Stylesheet)
     ↓ inherits to
  [Widescreen] (min-width: 2400px)
```
If a control value is omitted for `tablet`, it inherits from `desktop`. If a value is omitted for `mobile`, it inherits from `tablet`.

---

## 2. Setting Key Suffix Convention
Whenever a control is registered with `'responsive' => true` via `$this->add_responsive_control()`, Elementor dynamically accepts breakpoint-specific suffixes:

| Viewport | Suffix | Example Control Setting Keys |
|---|---|---|
| Desktop | *(none)* | `margin`, `padding`, `width`, `align`, `flex_direction` |
| Tablet | `_tablet` | `margin_tablet`, `padding_tablet`, `width_tablet`, `align_tablet`, `flex_direction_tablet` |
| Mobile | `_mobile` | `margin_mobile`, `padding_mobile`, `width_mobile`, `align_mobile`, `flex_direction_mobile` |
| Laptop | `_laptop` | `margin_laptop`, `padding_laptop`, `width_laptop` |
| Widescreen | `_widescreen`| `margin_widescreen`, `padding_widescreen`, `width_widescreen` |

---

## 3. Responsive Layout Patterns: Row to Column Stacking
To create a layout that displays horizontally across Desktop and Tablet but stacks vertically on Mobile:

```json
{
  "flex_direction": "row",
  "flex_direction_tablet": "row",
  "flex_direction_mobile": "column",
  "justify_content": "space-between",
  "align_items": "center",
  "align_items_mobile": "stretch",
  "gap": {
    "unit": "px",
    "row": "32",
    "column": "32",
    "isLinked": true
  },
  "gap_mobile": {
    "unit": "px",
    "row": "20",
    "column": "20",
    "isLinked": true
  }
}
```

---

## 4. Responsive Device Visibility
Located under **Advanced → Responsive**, visibility controls hide or show specific elements per device without modifying layout data:
- `hide_desktop`: `'hidden'` or `''`
- `hide_tablet`: `'hidden'` or `''`
- `hide_mobile`: `'hidden'` or `''`

Example:
```json
{
  "hide_desktop": "",
  "hide_tablet": "",
  "hide_mobile": "hidden"
}
```
Elementor compiles this rule into:
```css
@media (max-width: 767px) {
  .elementor-element-abc1234 {
    display: none !important;
  }
}
```
This guarantees complete visual control without writing custom CSS media queries.
