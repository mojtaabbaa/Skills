# Extension 03: Native Editorial Patterns, The 7 Deadly Sins & Atomic MCP/REST Publishing

Consolidated from the newest `elementor-editorial-pattern-architect` (13-pattern Interactive Dashboard version) + `wordpress-content-loading-automation` (3-step atomic `_elementor_edit_mode` protocol) — **100% brand-agnostic and stripped of hardcoded client defaults and internal script bugs**.

> [!IMPORTANT]
> **Brand Token Rule:** NEVER hardcode a specific client's colors, fonts, URLs, or ZWNJ rules. Always pull palette tokens, font family, orthography (`ZWNJ` vs `Zero-ZWNJ`), and active theme widgets from the active workspace's local **`.agents/skills/brand-*/SKILL.md`** skill and target Elementor Kit!

---

## 1. The "Anti-HTML-Dump" Cardinal Law

Never dump an entire article as one monolithic HTML blob inside a single `text-editor` widget. Decompose rich articles into native Elementor Flexbox Containers (`elType: "container"`) and interactive native widgets (`heading`, `text-editor`, `image`, `icon-box`, `icon-list`, `button`, `tabs`, `counter`, `progress`, `toggle`, `alert`, `testimonial`, `accordion`, plus active theme product carousels like `wd_products` when WoodMart is active).

---

## 2. The 7 Deadly Sins of Programmatic Elementor AST Generation

1. **Duplicate H1 Sin:** NEVER place a `heading` widget with `header_size: "h1"` inside single-post `_elementor_data` when the active theme/Theme Builder already renders the post title as `<h1>`. Start editorial headings at `h2`.
2. **Cramped 2-Column CTA Sin:** NEVER squish a 30% image column next to narrow Persian text inside a CTA banner. Use **full-width single-column centered luxury CTA banners** (`flex_direction: "column"`).
3. **Wrong Image Radius Sin:** ALWAYS use **`image_border_radius`** on `widgetType: "image"` — NEVER `border_radius` or `_border_radius`.
4. **Prefix Violation Sin:** Containers use bare `margin`/`padding`/`z_index`; Widgets use `_margin`/`_padding`/`_z_index`.
5. **Mobile Grid Collapse Sin:** Every multi-column desktop flex container (`width: 48.5%` or `23.5%`) MUST explicitly declare `width_mobile: {"unit": "%", "size": 100}` and parent `flex_direction_mobile: "column"`.
6. **Out-of-Order Sources Sin:** Authoritative Sources (`icon-list` citations) MUST appear **STRICTLY BEFORE** the FAQ Accordion (`accordion`).
7. **Orthography Corruption Sin:** NEVER globally strip ZWNJ (`\u200c`)! Strip ZWNJ **ONLY** when the active workspace's local `.agents/skills/brand-*/SKILL.md` contract explicitly specifies Zero-ZWNJ; preserve standard Persian ZWNJ on all standard Persian sites.

---

## 3. The 13 Native Interactive Editorial Patterns (Top-to-Bottom Blueprint)

1. **Direct Answer Golden Snippet Card:** Elevated surface container (`3–4px` right brand-accent border, `14px` radius) -> `heading` (H2) + `text-editor` (40–50 word direct answer).
2. **Full-Width Single-Column Commercial CTA Banner:** Gradient/brand-surface single-column container (`padding: 36px`, `border-radius: 16px`) -> `heading` (H3) + `text-editor` + `button`.
3. **Interactive Diagnostic Selector (`tabs`):** Horizontal `tabs` widget for comparing options, profiles, or user scenarios dynamically.
4. **Core Editorial Sections:** Clean `heading` (H2/H3) + concise `text-editor` paragraphs + `image` (`image_border_radius`) + responsive comparison tables (`<div style="overflow-x:auto;">`).
5. **Animated Statistical Metric Scorecards (`counter` Grid):** 2–4 column responsive flex row (`width: 23.5%` / `48.5%`, `width_mobile: 100%`) holding `counter` widgets for verified numbers.
6. **Visual Comparative Bars (`progress`):** Stacked `progress` widgets visualizing verified trade-offs or scores.
7. **Misconceptions vs. Reality Cards (`toggle`):** Expandable `toggle` cards (multiple panels open simultaneously).
8. **Critical Safety / Precaution Alert (`alert`):** High-contrast `alert` (`alert_type: "danger"` or `"warning"`, `show_dismiss: "none"`).
9. **Authoritative Literature Quote (`testimonial`):** Academic/clinical/standard citation block (`testimonial` widget).
10. **2-Col / 4-Col Feature Cards (`icon-box` Grid):** Responsive flex wrap grid of `icon-box` cards.
11. **Live Commerce Product Carousel:** Native theme/WooCommerce widget (`wd_products` on WoodMart, or Elementor Pro `woocommerce-products` / `loop-grid` on non-WoodMart themes).
12. **Strategic Internal Link Anchor (Read-More Box):** Dashed accent-border container -> `icon-list` with book icon linking to cornerstone hub.
13. **Authoritative Sources (`icon-list` with `nofollow: true`) -> STRICTLY FOLLOWED BY Native FAQ Accordion (`accordion` with `title_html_tag: "h3"`).**

---

## 4. The 8-Step Atomic WordPress + Elementor Publishing Lifecycle

1. **Ingest & Validate Draft:** Confirm H1, English slug, Meta Title (`<=60c`), Meta Description (`<=155c`), orthography per local `.agents/skills/brand-*/SKILL.md`, Sources before FAQ.
2. **Media Upload (WebP):** Upload optimized images via MCP (`wp_upload_media`) or REST (`/wp/v2/media`) with descriptive alt text; record attachment IDs.
3. **Draft Provisioning (NEVER Publish Directly!):** Create post strictly with `status: "draft"` via `wp_create_post` or `/wp/v2/posts`.
4. **SEO Meta Injection:**
   - **Rank Math:** `rank_math_title`, `rank_math_description`, `rank_math_focus_keyword`, `rank_math_robots`, `rank_math_canonical_url`.
   - **Yoast:** `_yoast_wpseo_title`, `_yoast_wpseo_metadesc`, `_yoast_wpseo_focuskw`.
5. **Compile Brand-Agnostic Elementor AST:** Use `scripts/article_to_elementor.py` (passing the active brand's `BrandThemeConfig` + `strip_zwnj` flag).
6. **CRITICAL — 3-Step Atomic `_elementor_edit_mode` Unlock/Write/Relock Protocol:**
   Easy MCP AI and Elementor block direct `_elementor_data` overwrites while `_elementor_edit_mode == 'builder'`. NEVER write `_elementor_data` and `_elementor_edit_mode: "builder"` in a single combined meta call! Always execute 3 sequential steps (using the target site's active MCP server name — never hardcode a single server):
   ```python
   # Step 6a: Unlock builder mode
   update_post_meta(post_id, {"_elementor_edit_mode": ""})
   # Step 6b: Write serialized JSON AST string
   update_post_meta(post_id, {"_elementor_data": json_ast_str})
   # Step 6c: Relock builder mode & template type
   update_post_meta(post_id, {
       "_elementor_edit_mode": "builder",
       "_elementor_template_type": "post"
   })
   ```
7. **Featured Image & Taxonomies:** Attach `_thumbnail_id`, categories, and tags.
8. **Cache Invalidation & Dual-Viewport QA:**
   - Clear Elementor generated CSS cache (`wp_clear_cache` / `\Elementor\Plugin::$instance->files_manager->clear_cache()`).
   - Purge WP Rocket URL cache (`wp_ability_wp_rocket_clear_url_cache` or `clear_website_cache` if global kit changed).
   - Verify HTTP `200 OK`, zero duplicate `<h1>`, Sources strictly above FAQ, and zero horizontal overflow on `390px` mobile and `1440px` desktop.
