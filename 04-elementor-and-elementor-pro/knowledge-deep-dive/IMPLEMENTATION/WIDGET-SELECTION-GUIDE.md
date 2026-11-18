# Widget Selection Guide & Architectural Decision Matrices

## 1. Decision Matrix: Content Display & Cards

| Use Case | Recommended Widget | Alternative Native Widget | Anti-Pattern (NEVER USE) | Reason for Recommendation |
|---|---|---|---|---|
| Simple Feature Card (Icon + Title + Text) | `icon-box` | Container holding `icon`, `heading`, `text-editor` | HTML widget with `<div class="card">` | `icon-box` provides integrated positioning (top/left/right), uniform padding, and native icon hover states in a single lightweight element. |
| Rich Card with Button & Ribbon | Container with child widgets | `call-to-action` | Text Editor with HTML markup | A child container provides full flexbox control over internal padding, border radius, box shadow, and independent child styling without custom CSS. |
| Customer Testimonial | `testimonial` | `reviews` or Container | Text Editor blockquote | Native testimonial widgets support photo upload, circular avatar styling, rating stars, and semantic citation tags. |
| FAQ Accordion | `accordion` | `nested-accordion` | Custom jQuery accordion script | `accordion` provides built-in accessibility (ARIA expanded), keyboard navigation, and schema metadata. |
| Multi-tabbed Content with Rich Elements | `nested-tabs` | `tabs` | External tab plugins | `nested-tabs` provides full Flexbox containers inside each tab pane, allowing forms, maps, videos, or galleries to reside inside tabs. |

---

## 2. Decision Matrix: Dynamic Content & Lists

| Use Case | Recommended Widget | Alternative Native Widget | Anti-Pattern | Reason for Recommendation |
|---|---|---|---|---|
| Standard Blog Archive (Grid/Cards) | `posts` | `loop-grid` | WP shortcodes / classic PHP loop | `posts` provides built-in pagination, tax filters, cards skin, avatar badges, and load-more buttons. |
| Custom Designed Loop Item (E-commerce / CPT) | `loop-grid` | `posts` with custom skins | Custom PHP template files | `loop-grid` allows visual drag-and-drop construction of the exact repeating card template using containers and dynamic tags. |
| Live Product Filter by Category | `taxonomy-filter` | `nav-menu` | Fragile 3rd-party AJAX plugins | `taxonomy-filter` natively links to Loop Grids and executes AJAX queries without page reloads. |
| Single Post Template Body | `post-content` | `text-editor` | Hardcoded content | `post-content` dynamically pulls the queried post's `the_content` while preserving theme builder encapsulation. |
| Article Navigation (Prev/Next) | `post-navigation` | Two `button` widgets | Raw HTML `<a>` tags | Automatically queries adjacent chronological posts in the current category/taxonomy. |

---

## 3. Decision Matrix: Navigation & Layout Structures

| Use Case | Recommended Widget | Alternative Native Widget | Anti-Pattern | Reason for Recommendation |
|---|---|---|---|---|
| Main Header Menu | `nav-menu` | `mega-menu` | Shortcode menu | Native responsive hamburger toggle, full-width mobile drawer, and animated pointer indicators. |
| Rich Multi-Column Mega Menu | `mega-menu` | `nav-menu` | Third-party mega menu plugin | Container-based mega menu renders native Elementor containers directly inside dropdowns. |
| In-Page Smooth Scroll Target | `menu-anchor` | Raw `<div id="...">` | JavaScript scroll scripts | Native anchor widget handles admin preview alignment and offset calculations. |
| Mobile Side Drawer | `off-canvas` | Popup Builder | External modal scripts | Designed specifically for slide-in panels, shopping drawers, and mobile side navigation. |
