# 06 - WoodMart Performance & Asset Optimization

## Performance Architecture Overview
WoodMart is one of the most optimized multipurpose WooCommerce themes, but its performance depends on correct settings configuration and avoiding third-party caching anti-patterns.

## 1. WoodMart Built-in CSS Generator
- **Location**: `Theme Settings -> Performance -> CSS`
- **Functionality**: Generates a unified, trimmed stylesheet containing only the CSS rules for features actively enabled on your store (e.g. if Portfolio or Header Banner is disabled, their CSS is excluded).
- **Rule**: Whenever you install a major WoodMart update or toggle theme modules, re-generate this CSS file.

## 2. JavaScript Modular Loading Architecture
WoodMart uses an on-demand modular JS loader (`woodmartThemeModule`).
- Rather than loading a monolithic 500KB script, WoodMart loads small chunks (e.g. `swatches.min.js`, `quickView.min.js`, `cartWidget.min.js`) only when the corresponding DOM elements exist on the page.
- **Anti-Pattern Warning**: Aggressive JS concatenation (e.g., Autoptimize or WP Rocket's "Combine JavaScript files") frequently breaks this on-demand loading mechanism.
  - **Best Practice**: Keep JS concatenation **OFF** when using HTTP/2 or HTTP/3; rely instead on WoodMart's granular scripts + minification + defer.

## 3. Font Loading & Persian Typography Optimization
- **Google Fonts Bottleneck**: Disabling external Google Fonts calls (`Theme Settings -> Typography -> Custom fonts`) prevents external round-trips to `fonts.googleapis.com` and `fonts.gstatic.com`.
- **Local Persian Fonts**:
  - Preload `.woff2` files using `<link rel="preload" as="font" type="font/woff2" crossorigin>` in `wp_head`.
  - Use `font-display: swap;` in `@font-face` definitions to prevent invisible text during load (FOIT).

## 4. Caching Plugin Compatibility Rules (WP Rocket / LiteSpeed)
- **Remove Unused CSS (RUCSS)**: Ensure WoodMart dynamic selectors (`.wd-swatch.active`, `.wd-off-canvas-opened`, `.wd-popup`) are added to the RUCSS Safelist so critical UI states aren't stripped.
- **Delay JS Execution**: If using delay JS execution, exclude:
  - `woodmartTheme`
  - `jquery`
  - `woodmart-theme`
  - Any custom AJAX filter script handle
  This ensures filters and sticky headers respond immediately without requiring user interaction.

## 5. Image & Thumbnail Optimization
- Set WooCommerce catalog thumbnail sizes (`Appearance -> Customize -> WooCommerce -> Product Images`) to match the exact display dimensions of your WoodMart grid columns.
- Ensure all product catalog images use WebP / AVIF format with explicit `width` and `height` attributes to maintain CLS = 0.
