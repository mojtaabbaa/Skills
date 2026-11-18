# Extension 03: Native Editorial Patterns, The 7 Deadly Sins & Atomic MCP/REST Publishing

Consolidated from the newest `elementor-editorial-pattern-architect` (13-pattern Interactive Dashboard version) + `wordpress-content-loading-automation` (3-step atomic `_elementor_edit_mode` protocol) — **100% brand-agnostic and stripped of hardcoded client defaults and internal script bugs**.

> [!IMPORTANT]
> **Brand Token Rule:** NEVER hardcode a specific client's colors, fonts, URLs, or ZWNJ rules. Always pull palette tokens, font family, orthography (`ZWNJ` vs `Zero-ZWNJ`), and active theme widgets from the active workspace's local **`.agents/skills/brand-*/SKILL.md`** skill and target Elementor Kit!

---

## 1. The "Anti-HTML-Dump" Cardinal Law & Complexity Classifier

**HTML Widget = `<script>` / True Interactive Embeds ONLY.** Never dump an article, card, badge, timeline, pricing box, or heading into an `html` widget or one monolithic `text-editor` blob. Decompose rich Persian articles into native Elementor Flexbox Containers (`elType: "container"`) and native Free/Pro widgets so every piece stays visually editable in the Elementor panel.

- **Decomposition Principle:** When a card needs refined typography, custom spacing, or multi-line badges, **3 separate native widgets (`icon` or `image` + `heading` + `text-editor`) inside a styled flex container** beat a rigid single `icon-box` widget AND beat an `html` widget every time!
- **Allowed Narrow Exceptions:**
  1. Comparison `<table>` inside `text-editor` wrapped in `<div style="overflow-x:auto;">` (keeps every cell editable as text while scrolling cleanly on 390px mobile).
  2. Standalone `<script>` / genuine interactive JS widget (charts, calculators) where no native Elementor widget exists.
- **Prototype-First Rule (For New Blog Templates & Bespoke Landings):** When designing a brand-new blog layout or commercial landing page for the first time, validate the visual direction in a lightweight HTML browser prototype (desktop `1440px` + mobile `390px`) BEFORE writing Elementor JSON — then save the approved spine as a reusable **Blog Playbook**.

---

## 1.5. Single Post Template vs. Per-Article `_elementor_data` Boundary

Never duplicate elements already rendered by the site's **Elementor Pro Theme Builder Single Post Template** (or active theme):
- **Owned by Single Post Template (Theme Builder):** `theme-post-title` (`<h1>`), `post-info` (date/category/reading time), `theme-post-featured-image`, global `table-of-contents`, `theme-post-content`, global `author-box`, `post-navigation`, `loop-grid` (related posts), `post-comments`.
- **Owned by Per-Article `_elementor_data` Body:** Direct Answer card, editorial H2/H3 sections, RTL timeline steps, comparison tables/cards, interactive tabs/toggles, metric scorecards, contextual product carousels, E-E-A-T reviewer callout (if not in global template), authoritative Sources (`icon-list`), FAQ Accordion (`accordion`), and inline commercial CTA banners.
- **Always inspect the target site's Single Post Template first** before placing H1, featured image, TOC, or author box inside `_elementor_data`.

---

## 2. The 7 Deadly Sins of Programmatic Elementor AST Generation

1. **Duplicate H1 Sin:** NEVER place a `heading` widget with `header_size: "h1"` inside single-post `_elementor_data` when the active theme/Theme Builder already renders the post title as `<h1>`. Start editorial headings at `h2`.
2. **Cramped 2-Column CTA Sin:** NEVER squish a 30% image column next to narrow Persian text inside a CTA banner. Use **full-width single-column centered luxury CTA banners** (`flex_direction: "column"`).
3. **Wrong Image Radius Sin:** ALWAYS use **`image_border_radius`** on `widgetType: "image"` — NEVER `border_radius` or `_border_radius`.
4. **Prefix & Flex-Trap Sin:** Containers use bare `margin`/`padding`/`z_index`/`flex_gap` + explicit `_title`; Widgets use `_margin`/`_padding`/`_z_index`; flex children with explicit width MUST set `content_width: "full"`; column containers MUST set `flex_align_items: "stretch"` (unless centered).
5. **Mobile Grid Collapse Sin:** Every multi-column desktop flex container (`width: 48.5%`, `31.5%`, or `23.5%`) MUST explicitly declare `width_mobile: {"unit": "%", "size": 100}` and parent `flex_direction_mobile: "column"` + responsive `typography_font_size_mobile` and `padding_mobile`.
6. **Out-of-Order Sources Sin:** Authoritative Sources (`icon-list` citations) MUST appear **STRICTLY BEFORE** the FAQ Accordion (`accordion`).
7. **Orthography Corruption Sin:** NEVER globally strip ZWNJ (`\u200c`)! Strip ZWNJ **ONLY** when the active workspace's local `.agents/skills/brand-*/SKILL.md` contract explicitly specifies Zero-ZWNJ; preserve standard Persian ZWNJ on all standard Persian sites.

---

## 3. The 18 Native Non-Atomic Editorial Patterns (Zero-HTML Luxury Blueprint)

Every top-level section MUST carry `"_title"` (for Navigator clarity) and clean Playbook slot naming:

1. **Direct Answer Golden Snippet Card (`slot: quick_answer`):** Elevated surface container (`1px` subtle border + `4px` right brand-accent border for RTL, `14px` radius, `flex_align_items: "stretch"`) -> `heading` (H2) + `text-editor` (40–50 word direct answer).
2. **Native Pill / Category / Status Badge (`slot: badge`):** Zero-HTML eyebrow pill using `button` widget (`size: "xs"`, `border_radius: 100px`, tinted RGBA accent bg, `text_padding: 6px 14px`, `_element_width: "auto"`, link `#` or category URL) — replaces HTML `<span>` pills cleanly!
3. **Editorial Heading with Inline Accent Emphasis (`<em>`):** Use inline `<em>` inside `heading` `title` (e.g., `"راهنمای <em>انتخاب حرفه‌ای</em> عینک"`) for typographic contrast without splitting one heading into multiple widgets.
4. **Vertical RTL Editorial Timeline / Step-by-Step Guide (`slot: timeline`):** Column container (`border_width: {right: "2"}`, `border_color: accent`, `padding: {right: "20"}`) holding step sub-containers (`content_width: "full"`, `flex_align_items: "stretch"`): top row (`flex_direction: "row"`, `flex_gap: 10`) with step `button` pill (`مرحله ۱` / `روز ۱ تا ۳`) + timeframe `text-editor` -> `heading` (H3) -> `text-editor` practical action. Far superior to plain `<ol>` for recovery timelines, brewing steps, or buying guides!
5. **Circular Gradient Icon Badge (Single-Widget Trick):** Style a single `image` widget directly (`_element_width: "initial"`, `_element_custom_width: 72–96px`, `_padding: 18–22px`, `_background_background: "gradient"`, `_border_radius: 50%`) — zero nested wrapper containers!
6. **E-E-A-T Author / Medical Reviewer / Expert Box (`slot: expert_box`):** Horizontal flex container (`flex_direction: "row"`, `flex_direction_mobile: "column"`, `flex_gap: 20`) -> circular avatar `image` (`image_border_radius: 50%`, **`_flex_size: "none"`**) + bio inner container (`content_width: "full"`, **`_flex_size: "grow"`, `_flex_grow: "1"`**, `flex_align_items: "stretch"`) with name `heading` (H4), role pill `button`, and credentials `text-editor`.
7. **Full-Width Single-Column Commercial CTA Banner (`slot: cta_banner`):** Gradient/brand-surface single-column container (`padding: 36px 32px`, `border_radius: 16px`, `flex_align_items: "center"`) -> `heading` (H3) + `text-editor` + `button` (with explicit `typography_line_height: 1.4`).
8. **Interactive Diagnostic Selector (`tabs`):** Horizontal `tabs` widget for comparing options, profiles, or user scenarios dynamically.
9. **Core Editorial Sections (`slot: body_section`):** Clean `heading` (H2/H3) + concise `text-editor` paragraphs (`line-height: 1.8–1.9`, max 2–3 lines) + `image` (`image_border_radius`) + responsive comparison tables (`<div style="overflow-x:auto;">`).
10. **Decomposed Feature / Comparison Cards Row (`slot: feature_grid`):** Outer boxed container (`flex_direction: "row"`, `flex_wrap: "wrap"`, `flex_direction_mobile: "column"`, `flex_gap: 20`) -> N card containers (**`content_width: "full"`**, `width: 48.5%` or `31.5%`, `width_mobile: 100%`, `flex_align_items: "stretch"`, `border_radius: 12px`, `padding: 24px`) holding separate `icon`/`image` + `heading` (H3) + `text-editor` (or `icon-list` checkmarks + `divider` + full-width `button` for Pricing/Package cards).
11. **Animated Statistical Metric Scorecards (`counter` Grid):** 2–4 column responsive flex row (`content_width: "full"` on children, `width: 23.5%` / `48.5%`, `width_mobile: 100%`) holding `counter` widgets for verified numbers.
12. **Visual Comparative Bars (`progress`):** Stacked `progress` widgets visualizing verified trade-offs or scores.
13. **Misconceptions vs. Reality Cards (`toggle`):** Expandable `toggle` cards (multiple panels open simultaneously).
14. **Critical Safety / Precaution Alert (`alert`):** High-contrast `alert` (`alert_type: "danger"` or `"warning"`, `show_dismiss: "none"`).
15. **Authoritative Literature Quote (`testimonial`):** Academic/clinical/standard citation block (`testimonial` widget).
16. **Live Commerce Product Carousel (`slot: product_carousel`):** Native theme/WooCommerce widget (`wd_products` on WoodMart, or Elementor Pro `woocommerce-products` / `loop-grid` on non-WoodMart themes).
17. **Strategic Internal Link Anchor (Read-More Box):** Dashed accent-border container -> `icon-list` with book icon linking to cornerstone hub.
18. **Authoritative Sources (`slot: sources` — `icon-list` with `nofollow: true`) -> STRICTLY FOLLOWED BY Native FAQ Accordion (`slot: faq` — `accordion` with `title_html_tag: "h3"`).**

### Reusable Per-Client Blog Playbook Contract
Once a client's first Elementor blog post is visually approved, freeze its **Section Spine + Named Slots** (`quick_answer` -> `body_section` -> `timeline` -> `feature_grid` -> `product_carousel` -> `cta_banner` -> `expert_box` -> `sources` -> `faq`) and **Style Contract** (`Confirmed` Global Kit tokens vs `Observed` theme defaults) inside that workspace's local `.agents/skills/brand-<project>/SKILL.md` so every future article snaps to the exact same studio standard!

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
