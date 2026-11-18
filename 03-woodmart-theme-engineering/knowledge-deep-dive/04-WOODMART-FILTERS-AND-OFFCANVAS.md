# 04 - WoodMart Filters, Off-Canvas Drawers & Mobile UX

## Native Filter Ecosystem in WoodMart
WoodMart provides multiple filtering components:
1. **Sidebar Filter Widgets**:
   - `WOODMART WooCommerce Layered Nav`: Attribute filtering with swatches, search inputs, and item counts.
   - `WOODMART Price Filter`: Slider and range inputs.
   - `WOODMART Sort By`: Custom drop-down for catalog orderby.
   - `WOODMART Stock Status`: In-stock / On-sale toggle filters.
2. **Shop Filters Area (Top Filters)**:
   - Expandable bar above product loop (`.wd-shop-filters-area`).
3. **Mobile Off-Canvas Drawer**:
   - Hidden off-canvas drawer that slides in from screen edge on mobile/tablet viewports.

## Mobile Off-Canvas Drawer Mechanics

### Key Selectors & Classes
- Drawer Wrapper: `.wd-filter-sidebar.wd-sidebar-hidden` (or `.wd-off-canvas-sidebar`)
- Open Buttons: `.wd-open-filter`, `.wd-off-canvas-btn`, `.wd-toolbar-link.wd-tools-filter`
- Close Trigger / Backdrop: `.wd-close-side`, `.wd-back-drop`
- Body State Class: `body.wd-off-canvas-opened` (locks background scrolling)

### Mobile Drawer Best Practices for Custom Filter Systems
- **Draft vs. Committed State**:
  - On desktop, changing a filter selection triggers an immediate AJAX request (no Apply button).
  - On mobile, instant fetching is disorienting and wastes battery/data. Selections should update local UI checkboxes only (draft state).
  - An **"Apply Filters"** button commits selections, closes the drawer via `$('.wd-close-side').trigger('click')`, and executes the AJAX query.
  - A **"Reset"** button resets all draft selections.
  - Closing the drawer without clicking Apply reverts selections to the currently active query state.

```javascript
// Example: Closing WoodMart off-canvas sidebar programmatically after filter submit
function closeWoodmartMobileDrawer() {
    if ($('body').hasClass('wd-off-canvas-opened')) {
        $('.wd-close-side').trigger('click');
    }
}
```

## Term Count Recalculation & Empty Option Hiding
When user selects a filter (e.g. Season: "Winter"), other filter options should accurately show remaining matching product counts.
- **AND vs. OR Logic**:
  - Attributes within the same taxonomy typically use `IN` (OR logic).
  - Separate taxonomies (e.g., Season AND Brand) use `AND` logic in `tax_query`.
- **Query Optimization**: Calculate counts in a single consolidated SQL query using `GROUP BY term_taxonomy_id` rather than running individual `WP_Query` calls for every term.
