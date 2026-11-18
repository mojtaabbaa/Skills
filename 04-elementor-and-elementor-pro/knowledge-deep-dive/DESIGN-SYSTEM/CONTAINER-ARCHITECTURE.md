# Container Architecture: Flexbox, Grid & Layout Engineering

## 1. Architectural Evolution: Sections vs Containers
Elementor previously relied on a 3-layer DOM hierarchy:
`Section (section) → Column (column) → Widget (widget)`

In modern Elementor (v3.18+ / v4.x), this is completely superseded by the **Flexbox & Grid Container** (`Elementor\Includes\Elements\Container`).
- **Clean DOM**: Eliminates redundant nested `elementor-container`, `elementor-row`, and `elementor-column-wrap` divs.
- **True CSS Flexbox & Grid**: Native controls directly map to CSS flexbox and grid properties on the container node.
- **Arbitrary Nesting**: Containers can hold widgets directly or nest child containers indefinitely.

---

## 2. Container Types & Structural Flags

### A. Root Container (`isInner: false`)
- Directly placed at the top level of `_elementor_data`.
- Acts as a section on the page.
- Typically controls full-width backgrounds, maximum page content width (`content_width: "boxed"` or `"full_width"`), top/bottom section padding, and responsive outer gutters.

### B. Child / Inner Container (`isInner: true`)
- Placed inside a root container's `elements` array.
- Acts as a sub-column, card, flex row, or grid cell.
- Manages local alignment, horizontal grouping, and card styling (borders, shadows, padding).

---

## 3. Flexbox Layout Controls & Data Schema

### A. Direction (`flex_direction`)
- `'row'`: Horizontal left-to-right (RTL sensitive: right-to-left).
- `'column'`: Vertical top-to-bottom stack.
- `'row-reverse'`: Horizontal reversed.
- `'column-reverse'`: Vertical reversed.
- **Responsive Stacking Standard**: Set `"flex_direction": "row"`, `"flex_direction_mobile": "column"`.

### B. Justify Content (`justify_content`)
Controls distribution along the primary axis:
- `'flex-start'`: Packed at the start.
- `'center'`: Centered along the main axis.
- `'flex-end'`: Packed at the end.
- `'space-between'`: First item at start, last item at end, equal spacing between.
- `'space-around'`: Equal space around every item.
- `'space-evenly'`: Identical spacing before, between, and after all items.

### C. Align Items (`align_items`)
Controls alignment along the cross axis:
- `'flex-start'`: Aligns to the cross-axis top/start.
- `'center'`: Vertically centered in row mode, horizontally centered in column mode.
- `'flex-end'`: Aligns to the cross-axis bottom/end.
- `'stretch'`: Stretches child elements to fill container height (default for equal-height cards).
- `'baseline'`: Aligns text baselines across items.

### D. Wrap (`flex_wrap`)
- `'nowrap'`: All items stay in one line (causes overflow or shrinking).
- `'wrap'`: Items wrap onto multiple lines when total width exceeds container.
- `'wrap-reverse'`: Wrapped lines flow in reverse direction.

### E. Gaps (`gap`)
Directly replaces manual margins between siblings:
```json
"gap": {
  "unit": "px",
  "row": "32",
  "column": "24",
  "isLinked": false
}
```

---

## 4. Grid Container Controls (`container_type: "grid"`)
When `container_type` is set to `"grid"`:
- `grid_columns_grid`: Slider object (e.g. `1` to `12` fractional columns, or custom `fr`/`px`).
- `grid_rows_grid`: Slider object.
- `grid_gaps`: Row and column gap dimensions.
- Child items can span multiple columns or rows natively via `grid_column` and `grid_row` controls without writing CSS `grid-column: span 2`.

---

## 5. Nesting Discipline & DOM Complexity Governance
To prevent DOM bloat and ensure fast Core Web Vitals:
1. **Rule of 2 Levels**: A typical layout should never exceed 2 levels of nesting:
   `Root Container (Section) → Child Container (Row / Card) → Widgets`
2. **Never Create Single-Child Wrapper Containers**: If a container only holds one widget and has no background, border, or distinct layout rule, remove the container and place the widget directly in the parent container.
3. **Use Gaps Instead of Nested Spacers**: Never drop Spacer widgets between siblings inside a container; set the container's `gap` control instead.
