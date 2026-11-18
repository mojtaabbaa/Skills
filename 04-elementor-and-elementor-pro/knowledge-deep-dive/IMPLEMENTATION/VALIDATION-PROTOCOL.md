# Quality Assurance & 5-Stage Validation Protocol

## 1. Quality Assurance Protocol Overview
Before any page is declared complete, tested, or production-ready, it must pass all five stages of this validation protocol.

---

## 2. Stage 1: Structural & JSON Validation
- **JSON Validity**: `_elementor_data` must parse cleanly as valid JSON without trailing commas or unescaped quotes.
- **Top-Level Root**: Array of objects where every root element has `elType: "container"` and `isInner: false`.
- **Unique Hex IDs**: Every element and repeater row must possess a unique 7 or 8 hex character `id` or `_id`. No duplicate IDs are permitted.
- **Widget Slugs**: Every widget node must have an authentic `widgetType` matching the registered inventory (e.g. `heading`, `image`, `button`, `icon-box`, `form`, `loop-grid`).
- **Child Elements**: Every widget node must have an empty `elements: []` array. Every container node must have an `elements` array containing valid child nodes.

---

## 3. Stage 2: Zero-Custom-CSS Audit
Inspect the entire serialized payload. The page fails Stage 2 if ANY of the following are found:
- `custom_css`: Present with any non-empty value.
- `<style`: Present inside any text, HTML, or code control.
- `style="`: Present in any rendered attribute.
- `.custom-class`: Present as an arbitrary CSS override.
- An `html` widget used to imitate native buttons, cards, or layouts.

---

## 4. Stage 3: Frontend Rendering Validation
- **Content Filter**: Confirm that `the_content` replaces raw text with Elementor's compiled markup.
- **Stylesheet Generation**: Confirm that `post-{$post_id}.css` or inline `<style id="elementor-post-{$post_id}">` is printed in the page `<head>`.
- **Dynamic Tags Resolution**: Confirm that all `[elementor-tag ...]` placeholders evaluate to actual strings/images on the frontend rather than showing raw shortcode syntax.
- **Asset Enqueue**: Confirm that required JavaScript dependencies (e.g. Swiper, Waypoints) are enqueued only when corresponding widgets are present.

---

## 5. Stage 4: Editor Compatibility Validation
- Open the page in the Elementor visual editor:
  - The editor panel must load without JavaScript exceptions or React errors.
  - Every container must be selectable and highlightable.
  - Every widget must display its corresponding controls panel (Content, Style, Advanced).
  - Modifying a control in the panel must immediately update the live preview iframe.
  - Clicking "Update" must succeed and save changes back to `wp_postmeta`.

---

## 6. Stage 5: Visual & Responsive QA
- **Desktop (1440px / 1200px)**: Grid columns align, spacing adheres to design specifications, typography hierarchy is distinct.
- **Tablet (1024px / 768px)**: 3-column rows transition gracefully to 2-column rows or wrapped items without horizontal scrollbars.
- **Mobile (375px / 414px)**: All multi-column containers stack into a single column (`flex_direction: "column"`), touch targets meet minimum 48px guidelines, and horizontal overflow is zero.
