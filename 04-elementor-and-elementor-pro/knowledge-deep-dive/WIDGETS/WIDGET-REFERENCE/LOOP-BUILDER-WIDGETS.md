# Widget Reference: Loop Builder Widgets

## 1. Loop Grid (`loop-grid`)
- **Origin**: Elementor Pro
- **Class**: `\ElementorPro\Modules\LoopBuilder\Widgets\Loop_Grid`
- **Settings Data Contract**:
  ```json
  {
    "template_id": 65100,
    "columns": 3,
    "columns_tablet": 2,
    "columns_mobile": 1,
    "posts_per_page": 6,
    "_query_post_type": "post",
    "query_include": ["terms"],
    "query_include_term_ids": [501],
    "query_orderby": "date",
    "query_order": "desc",
    "pagination_type": "load_more_on_click",
    "load_more_spinner": "yes",
    "load_more_button_text": "Load More Articles",
    "row_gap": { "unit": "px", "size": 32 },
    "column_gap": { "unit": "px", "size": 24 }
  }
  ```
- **Alternate Template Injection**:
  Allows injecting a distinct template at specific positions (e.g. inject template `65200` at position `2`, spanning `2` columns):
  ```json
  {
    "alternate_template": "yes",
    "alternate_templates": [
      {
        "_id": "alt_1",
        "template_id": 65200,
        "position": 2,
        "column_span": 2
      }
    ]
  }
  ```

---

## 2. Taxonomy Filter (`taxonomy-filter`)
- **Origin**: Elementor Pro
- **Class**: `\ElementorPro\Modules\LoopFilter\Widgets\Taxonomy_Filter`
- **Settings Data Contract**:
  ```json
  {
    "selected_element": "loop_grid_articles",
    "taxonomy": "category",
    "show_empty_taxonomies": false,
    "show_first_item": "yes",
    "first_item_title": "All Topics",
    "direction": "row",
    "alignment": "center",
    "item_spacing": { "unit": "px", "size": 8 },
    "item_typography_typography": "custom",
    "item_typography_font_size": { "unit": "px", "size": 14 },
    "item_typography_font_weight": "500",
    "item_color": "#4b5563",
    "item_background_color": "#f3f4f6",
    "item_color_active": "#ffffff",
    "item_background_color_active": "#2563eb",
    "item_border_radius": { "unit": "px", "top": "20", "right": "20", "bottom": "20", "left": "20", "isLinked": true }
  }
  ```
- **Zero-CSS Replacements**:
  - Eliminates custom AJAX filtering scripts, active pill highlights, category tabs, and loading animations.
