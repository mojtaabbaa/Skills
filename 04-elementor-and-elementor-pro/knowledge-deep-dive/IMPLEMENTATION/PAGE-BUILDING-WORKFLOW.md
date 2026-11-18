# Page Design and Construction Engine: 7-Step Workflow

## 1. Overview & Operational Mandate
Every page requested by a user or built for a project must follow this rigorous, 7-step engineering sequence.
Never jump straight into writing JSON or HTML. Deconstruct the requirements systematically.

---

## 2. The 7-Step Engineering Sequence

```
Step 1: Design Analysis
   ↓ (Deconstruct page type, content hierarchy, sections, responsive goals)
Step 2: Widget Selection
   ↓ (Map each section to authentic native Elementor widgets; NO HTML shortcuts)
Step 3: Container Architecture
   ↓ (Design Flexbox/Grid tree: root containers, child containers, direction, gaps)
Step 4: Native Styling
   ↓ (Configure colors, typography, borders, shadows via native controls; ZERO CSS)
Step 5: Responsive Construction
   ↓ (Configure mobile and tablet direction, spacing, typography scales, order)
Step 6: Data & Dynamic Content
   ↓ (Bind dynamic tags, WP query parameters, ACF fields, WooCommerce tokens)
Step 7: Validation & QA
   ↓ (5-stage verification: structure, zero-CSS audit, frontend, editor, visual)
```

---

## 3. Detailed Step Breakdown

### Step 1: Design Analysis
- **Determine Page Type**: Landing page, single blog article, archive catalog, single product, contact portal, account dashboard.
- **Identify Content Blocks**: Hero header, features list, social proof / testimonials, pricing table, interactive FAQ, call to action, footer.
- **Identify Brand Foundations**: Primary brand color, secondary tones, typography family, spacing rhythm (e.g. 8px grid system).

### Step 2: Widget Selection
- Match each content block to its exact native Elementor widget:
  - Hero Headline → `heading`
  - Action Trigger → `button`
  - Visual Feature Card → `icon-box` or `image-box`
  - Customer Testimonial → `testimonial` or `reviews`
  - Question / Answer → `accordion`
  - Article TOC → `table-of-contents`
  - Dynamic Post Grid → `loop-grid` or `posts`
  - Contact / Lead Capture → `form`
- **Strict Prohibition**: Never use an `html` widget or a large `text-editor` widget to construct a multi-element card or layout section.

### Step 3: Container Architecture
- Establish the container hierarchy:
  - Root Container: `content_width: "boxed"`, `boxed_width: 1200`, `flex_direction: "column"`, vertical padding `80px`.
  - Child Container (Grid / Row): `flex_direction: "row"`, `justify_content: "space-between"`, `gap: 32px`.
  - Child Containers (Cards): `flex_direction: "column"`, `align_items: "flex-start"`, local padding `32px`.

### Step 4: Native Styling
- Apply all visual rules via native controls:
  - Typography: Bind to Global Typography or configure font family, weight, and size.
  - Colors: Bind to Global Colors (`__globals__`) or set native hex/rgba values.
  - Cards: Apply native background color, border width, border color, border radius, and box shadow.
  - Hover States: Configure native hover background and scale animations.

### Step 5: Responsive Construction
- Review and apply overrides for `tablet` and `mobile`:
  - Containers: Change `flex_direction` from `row` to `column`.
  - Spacing: Scale padding down from `80px` to `40px` (tablet) and `24px` (mobile).
  - Typography: Scale H1 from `48px` to `36px` (tablet) and `28px` (mobile).
  - Order: Invert alternating rows with `flex_direction_mobile: "column-reverse"`.

### Step 6: Data & Dynamic Content
- If content originates from WordPress or WooCommerce:
  - Heading titles: Bind to `[elementor-tag name="post-title"]`.
  - Post meta: Use `post-info` widget.
  - Images: Bind to `[elementor-tag name="post-featured-image"]`.
  - Custom fields: Bind to `[elementor-tag name="post-custom-field"]` or ACF tags.

### Step 7: Validation & Deployment
- Run through the **5-Stage Quality Assurance Protocol**:
  1. Structural validation of `_elementor_data` JSON.
  2. Zero-CSS compliance scan.
  3. Live preview test via MCP / browser.
  4. Editor compatibility check.
  5. Responsive layout verification across desktop, tablet, and mobile.
