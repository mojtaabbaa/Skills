# Caching, Delay JS & RUCSS Safelist Rules

## WP Rocket & LiteSpeed Cache Whitelist

### 1. Delay JavaScript Execution Exclusions
Ensure the following script handles and keywords are NEVER delayed or deferred:
```text
woodmartTheme
woodmart-theme
jquery.js
jquery.min.js
elementorFrontend
elementorFrontendConfig
ccbConfig
woodmartFilterConfig
```

### 2. Remove Unused CSS (RUCSS) Safelist
Add the following dynamic CSS selectors to the RUCSS Safelist to prevent visual degradation after AJAX calls:
```css
.wd-page-content
.wd-loading
.wd-off-canvas-opened
.wd-filter-sidebar
.wd-close-side
.wd-back-drop
.wd-swatch.active
.wd-sticky-btn
.elementor-sticky--active
.elementor-sticky__spacer
.ccb-enhanced-card
```
