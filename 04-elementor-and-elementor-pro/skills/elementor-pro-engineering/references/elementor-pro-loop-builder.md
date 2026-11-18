# Elementor Pro Loop Builder Reference

## Overview
Loop Builder (`Loop Grid` and `Loop Carousel` widgets) allows designers to create custom repeating item templates for post types and WooCommerce products.

## Custom Query & Dynamic Tags in Loop Items
1. **Loop Item Post Type**: `elementor_library` with `_elementor_template_type = 'loop-item'`.
2. **Dynamic Tags**: Used inside loop items to fetch data from the current post in the loop context (e.g., Post Title, Featured Image, WooCommerce Price, Custom Field / ACF).
3. **Alternating Templates**: Elementor Loop Grid supports applying different templates to specific positions (e.g. template A for position 1, template B for position 2).

## Enhancing Loop Performance
- **Avoid Nested Loops**: Never place a Loop Grid widget inside another Loop Item template.
- **Lazy Load Images**: Ensure images inside loop items have native `loading="lazy"` and explicit width/height to avoid cumulative layout shift (CLS).
- **Pagination via AJAX**: Elementor Pro Loop Grid supports native AJAX pagination (`Numbers + Previous/Next` or `Load on Click`). Ensure any custom JS initialized on loop items hooks into `elementor/frontend/init` and respects AJAX replacement.
