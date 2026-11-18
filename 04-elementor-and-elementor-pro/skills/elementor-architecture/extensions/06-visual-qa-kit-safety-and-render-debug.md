# Extension 06: Visual QA, Global Kit Safety & 4-Bucket Render Diagnostics (Non-Atomic)

Consolidated from battle-tested production Elementor playbooks (`mwender/elementor-mcp-skill`, `Mekko-Digital/elementor-debug-render`, `Digitizers/siteagent-elementor-studio`, `respira-press`). Strictly scoped to **Classic & Flexbox/Grid Elementor builds** (zero Atomic V4 dependency).

---

## 1. Global Kit Safety Law & Revision Recovery

> [!CAUTION]
> **NEVER overwrite `_elementor_page_settings` on the active Elementor Kit post with a partial-payload tool!**
> Tools that replace `_elementor_page_settings` wholesale wipe `system_colors`, `system_typography`, `custom_colors`, and heading styles — reverting the entire site back to Elementor defaults (`#6EC1E4`, `#7A7A7A`, Roboto) in a single call!

### Safe Kit Write Rules
1. Always perform a **full read-modify-write** on `_elementor_page_settings` (read full array -> modify ONLY the target key -> write full array back) and immediately flush generated CSS (`wp elementor flush_css`).
2. Never pass system slot IDs (`primary`, `secondary`, `text`, `accent`) into `custom_colors` / `custom_typography` append endpoints (causes colliding `_id`s and broken `__globals__` resolution).
3. **Kit Corruption Recovery (If Site Suddenly Turns `#7A7A7A` / `#6EC1E4`):**
   ```bash
   KIT_ID=$(wp option get elementor_active_kit)
   wp post list --post_type=revision --post_parent=$KIT_ID --fields=ID,post_modified,post_title
   # Inspect candidate revision, then restore non-destructively:
   wp eval '$good = get_post_meta(<REVISION_ID>, "_elementor_page_settings", true); update_post_meta('"$KIT_ID"', "_elementor_page_settings", $good);'
   wp elementor flush_css
   ```

---

## 2. Recommended Defensive Kit Baseline CSS (Propose Before Applying)

This 10-line defensive CSS in **Site Settings -> Custom CSS** eliminates the #1 visual blemish in Elementor blog cards (uneven bottom padding caused by `<p>` margins inside `text-editor` widgets) and guarantees WCAG 2.2 keyboard focus outlines. Both selectors support **Optimized DOM Output** (no `.elementor-widget-container`) AND legacy DOM:

```css
/* skill-baseline: applied */
.elementor-widget-text-editor > p:last-child,
.elementor-widget-text-editor > .elementor-widget-container > p:last-child {
  margin-bottom: 0;
}
.elementor-widget-text-editor > p:first-child,
.elementor-widget-text-editor > .elementor-widget-container > p:first-child {
  margin-top: 0;
}
.elementor a:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
*(Always verify selector count `> 0` on a live page and get explicit owner confirmation before editing a live site's Global Kit.)*

---

## 3. Computed-Style DOM Diagnostics (`.e-con-inner` Rule Zero!)

Screenshots catch gross layout bugs, but **browser `eval` + `getComputedStyle`** catches silent CSS bugs in 5 seconds:

- **Rule Zero (`e-con-boxed` containers):** On boxed containers, flex/grid/gap/padding styles land on **`:scope > .e-con-inner`**, NOT the outer `.elementor-element-<id>`! Always inspect:
  ```js
  const el = document.querySelector('.elementor-element-<id>');
  const target = el.querySelector(':scope > .e-con-inner') || el;
  const cs = getComputedStyle(target);
  ({ dir: cs.flexDirection, align: cs.alignItems, gap: cs.gap, cols: cs.gridTemplateColumns, rows: cs.gridTemplateRows })
  ```
- **Check Global Kit CSS Variables:**
  ```js
  getComputedStyle(document.body).getPropertyValue('--e-global-color-text').trim()
  ```
  *(If it resolves to `#7A7A7A` unexpectedly, Kit CSS is stale or wiped -> flush CSS or inspect revisions!)*
- **Check Child `<em>` / `<span>` inside Headings:** Query `h2 em, h2 span` separately because `getComputedStyle(h2).color` misses inline highlight overrides.
- **Check Mobile Horizontal Overflow (`390px` viewport):**
  ```js
  document.documentElement.scrollWidth > document.documentElement.clientWidth
  ```
- **Dual-Viewport Visual QA:** Always inspect rendered drafts at BOTH **Desktop (`1440px`)** and **Mobile (`390px`)** after flushing CSS (`wp elementor flush_css` + page cache purge).

---

## 4. 4-Bucket Render Failure Triage (Non-Atomic)

When an Elementor post/page renders blank, stale, or broken, classify into the exact bucket first:

1. **Editor Canvas Blank (Controls Panel Visible):** Classic widget JS `content_template()` threw an error -> inspect Browser DevTools Console.
2. **Editor Preview Iframe Blank (`?elementor-preview=<id>`):** Server PHP `render()` fatal -> check PHP error log & active theme/plugin hooks (`elementor/widget/render_content`).
3. **Frontend-Only Broken or Stale (Preview Looks Fine):** Stale generated CSS, Element Cache, or Page-Asset list! Escalate in order:
   - Re-save post or run `wp elementor flush_css` (regenerates `_elementor_css` and asset manifest).
   - **Elementor Element Cache:** Keyed globally by option `_elementor_element_cache_unique_id` (`modules/element-cache/module.php`). Clear via **Elementor -> Tools -> Regenerate CSS & Data**, or toggle via `wp option update elementor_element_cache_ttl disable`.
   - Flush object cache (`wp cache flush`) and WP Rocket / LiteSpeed / Cloudflare URL cache.
4. **Both Preview AND Frontend Blank:** Corrupted `_elementor_data` JSON, missing `_elementor_edit_mode: "builder"`, or duplicate element IDs. Validate via `wp post meta get <id> _elementor_data | jq .`.

---

## 5. Production Publishing Safeguards (Long Blogs, SVGs & RTL)

- **Long Editorial Posts (`WP_MEMORY_LIMIT`):** Posts with 150–350+ Elementor widgets can hit 500 errors on 256MB hosts — recommend `WP_MEMORY_LIMIT = 512M`. After ANY HTTP 5xx during incremental MCP writes, **re-read the page structure first** to check for partial/duplicate writes before retrying!
- **SVG Uploads (`safe-svg` v2.4+ Role Gate):** If SVG upload fails even with Safe SVG active, check `wp option get safe_svg_upload_roles` (v2.4+ ships empty by default -> `wp option update safe_svg_upload_roles '["administrator"]' --format=json`). Always use Media Library attachment IDs (`{"id": 123, "url": "..."}`) rather than raw external image URLs.
- **Persian RTL (`fa_IR`) Verification:** Never fight Elementor's native RTL direction stylesheet (`is_rtl()`) by blindly adding `row-reverse`; inspect the live RTL render first and reserve `dir="ltr"` strictly for inline English SKUs, code, or URLs.
