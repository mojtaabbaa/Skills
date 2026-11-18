# 03 - WoodMart & Elementor / Elementor Pro Integration

## Overview
WoodMart features deep native integration with Elementor Free and Elementor Pro. It provides custom Elementor widgets, custom container controls, dynamic tag integration, and responsive grid system enhancements.

## Dedicated WoodMart Elementor Widgets (`wd_` series)
WoodMart Core registers 40+ specialized Elementor widgets:
1. `wd_products`:
   - Grid and carousel modes for WooCommerce products.
   - Built-in pagination (AJAX, load more button, infinite scroll).
   - Card design templates: `default`, `alt`, `icons`, `quick`, `base`, `standard`, `button`.
2. `wd_categories`:
   - Visual category tiles, carousels, and masonry displays.
3. `wd_banner` & `wd_banner_carousel`:
   - Interactive banners with hover effects, countdown timers, and responsive typography.
4. `wd_title`:
   - Section heading with subtitles, decorative lines, and RTL-aligned icons.
5. `wd_extra_menu`:
   - Mega-menu list navigation tailored for sidebar layouts.

## Flexbox Containers (`.e-con`) & Sticky Filter Resolution
### The Critical Problem
In modern Elementor (Flexbox Container layout), placing a sticky sidebar widget inside an `.e-con` flex column can cause severe layout shrinkage:
- When a user filters products and the result count drops (e.g. from 24 products down to 1 product), the column height collapses.
- Elementor's sticky script (`position: fixed`) leaves an empty placeholder spacer. In flexbox without explicit constraints, the column collapses to its `min-content` width (~120px–160px).
- Elementor's resize listener measures the collapsed width and permanently freezes the widget width inline (`style="width: 135px;"`).

### The Battle-Tested Engineering Solution
1. **Defensive CSS Guard**:
   ```css
   /* Prevent flex container and sticky wrapper from collapsing below 260px */
   .woodmart-shop-sidebar-column,
   .woodmart-shop-sidebar-column .elementor-widget-wrap,
   .woodmart-shop-sidebar-column .elementor-sticky--active,
   .woodmart-shop-sidebar-column .elementor-sticky__spacer {
       min-width: 260px !important;
       flex-shrink: 0 !important;
       flex-basis: 260px !important;
   }
   ```
2. **Authoritative JS Width Lock**:
   On `pjax:complete` or custom filter AJAX completion, explicitly read parent column width and enforce it on the sticky element:
   ```javascript
   function stabilizeStickySidebar() {
       var $col = $('.woodmart-shop-sidebar-column');
       if ($col.length) {
           var colWidth = $col.outerWidth();
           $col.find('.elementor-sticky--active').css('width', colWidth + 'px');
       }
   }
   $(window).on('scroll resize', stabilizeStickySidebar);
   $(document).on('pjax:complete woodmart_ajax_success', stabilizeStickySidebar);
   ```

3. **Strictly Scope Elementor `runReadyTrigger`**:
   Never run `elementorFrontend.elementsHandler.runReadyTrigger($('body'))` after an AJAX update. Only run it on the product grid container:
   ```javascript
   elementorFrontend.elementsHandler.runReadyTrigger($('.wd-products-element'));
   ```
