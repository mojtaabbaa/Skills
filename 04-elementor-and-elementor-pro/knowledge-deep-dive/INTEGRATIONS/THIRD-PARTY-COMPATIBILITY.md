# Third-Party Compatibility & Environment Discipline

## 1. Theme Compatibility & Boundaries
Elementor operates cleanly across well-architected WordPress themes:

### A. Hello Elementor (Official Minimal Theme)
- Completely unopinionated blank slate.
- No theme styling collisions or CSS overrides.
- Recommended baseline for 100% Elementor-native projects.

### B. Astra / GeneratePress
- Enforces theme hooks: `astra_header_after`, `astra_entry_content_before`.
- Elementor Pro Theme Builder automatically takes ownership of headers and footers when conditions match.

### C. WoodMart & Complex Commercial Themes
- **Known Risk Area**: WoodMart uses custom AJAX product loop fragments (`_pjax=.wd-page-content`), custom quick-view modals, and product swatches.
- **Discipline Rule**:
  - Never assume WoodMart is active unless inspected.
  - When modifying Elementor layouts on WoodMart, do not delete theme wrapper hooks (`woodmart_before_shop_loop`, `woocommerce_after_shop_loop_item`).
  - Do not bind custom JavaScript to unstable WoodMart CSS classes (`.wd-builder-on`, `.woodmart-hover-base`).

---

## 2. Performance, Caching & Minification Plugins

### A. WP Rocket
- **Remove Unused CSS (RUCSS)**: If enabled, WP Rocket scans the page and generates a critical CSS snippet. If an Elementor layout update is deployed, clear the WP Rocket Used CSS cache immediately, otherwise users will see the old stylesheet.
- **JavaScript Minification & Deferral**: Deferring `elementor-frontend.js` is safe; however, concatenating JS files can break Swiper or Waypoints timing. Exclude `frontend.js` from JS concatenation if sliders fail to initialize.

### B. LiteSpeed Cache (LSCache)
- CSS Minification: Elementor's CSS generator already minifies post stylesheets (`post-{$id}.css`). Redundant re-minification is unnecessary.
- Cache Purge: Purge LSCache after updating `_elementor_data` or Theme Builder conditions.

### C. Autoptimize
- Ensure "Also aggregate inline CSS" is turned OFF. When enabled, it captures Elementor's dynamic inline CSS and creates bloated aggregate stylesheets.

---

## 3. SEO Plugins Integration (Rank Math & Yoast)
- **Breadcrumbs**: Both Rank Math (`[rank_math_breadcrumb]`) and Yoast (`[wpseo_breadcrumb]`) integrate natively with Elementor Pro's `breadcrumbs` widget.
- **Sitemaps**: Rank Math and Yoast automatically index Elementor custom library posts if public; ensure `elementor_library` is excluded from XML sitemaps to prevent indexing template fragments.
- **Content Analysis**: Rank Math parses Elementor JSON content directly via its `RankMath\Elementor` content analyzer module.
