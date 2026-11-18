# Responsive Design Engineering & Mobile Optimization

## 1. Viewport Hierarchy & Cascade Governance
Elementor operates on a **Desktop-Down Cascade**:
1. **Desktop (> 1024px)**: Full multi-column grids, horizontal navigation, expansive padding (`60px` to `120px`), large display typography (`40px` to `64px`).
2. **Tablet (768px – 1024px)**: Intermediate density, 2-column grids, moderate padding (`40px` to `60px`), heading scaling (`32px` to `40px`).
3. **Mobile (< 767px)**: Single-column vertical stacks, full-width touch targets, compact gutters (`16px` to `24px`), mobile typography (`24px` to `32px`).

---

## 2. Five Golden Rules of Elementor Responsive Construction

### Rule 1: Never Downscale Desktop Layouts Blindly
Do not simply reduce font size while leaving a 4-column row intact. Switch container direction to column:
```json
"flex_direction": "row",
"flex_direction_tablet": "row",
"flex_direction_mobile": "column"
```

### Rule 2: Invert Visual Hierarchy on Mobile (Order Manipulation)
In desktop layouts with alternating text/image rows (Z-pattern):
- Row 1: `[Image Left] [Text Right]`
- Row 2: `[Text Left] [Image Right]`

On mobile, standard stacking causes Row 2 to display Text before Image, breaking visual rhythm.
Use native responsive reverse or item order:
```json
"flex_direction_mobile": "column-reverse"
```
Or on the specific child element:
```json
"order_mobile": 1
```

### Rule 3: Enforce Minimum Touch Targets (48px)
All interactive elements (buttons, form inputs, accordion headers, pagination links) must satisfy minimum touch target guidelines on mobile without custom CSS:
- Button size set to `md` or `lg` with vertical padding of at least `14px`.
- Form field height and padding configured through native form style controls.

### Rule 4: Decouple Desktop Margins from Mobile
Large desktop horizontal margins (e.g. `margin-left: 100px`) will break mobile viewports, creating horizontal overflow and scrollbars. Always reset margins on mobile:
```json
"margin": { "unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "100", "isLinked": false },
"margin_mobile": { "unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": true }
```

### Rule 5: Utilize Device Visibility Prudently
Use `hide_mobile` or `hide_desktop` only for elements that have no mobile equivalent (such as complex interactive charts, heavy decorative animations, or secondary sidebars). Do not use visibility toggling to recreate entirely separate duplicate pages for desktop and mobile, as this doubles DOM size and hurts page load performance.
