# Elementor Engineering Knowledge System — Master Index

## Master Index & Navigation

This master index connects all technical specifications, reverse-engineering analyses, widget/control indexes, design matrices, and implementation guides across the knowledge base.

---

## 1. Source Architecture Analysis (`SOURCE-ANALYSIS/`)

| Document | Focus & Scope | Primary Source Evidence |
|---|---|---|
| [WORDPRESS-ARCHITECTURE.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/SOURCE-ANALYSIS/WORDPRESS-ARCHITECTURE.md) | WP Core lifecycle, post metadata, REST API meta registration, template hierarchy, hooks | `wordpress/wp-includes/post.php`, `meta.php`, `rest-api/` |
| [ELEMENTOR-ARCHITECTURE.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/SOURCE-ANALYSIS/ELEMENTOR-ARCHITECTURE.md) | Free plugin bootstrap, manager registries, element lifecycle, `Element_Base`, `Widget_Base` | `elementor/includes/plugin.php`, `managers/widgets.php`, `base/element-base.php` |
| [ELEMENTOR-PRO-ARCHITECTURE.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/SOURCE-ANALYSIS/ELEMENTOR-PRO-ARCHITECTURE.md) | Pro modules, Theme Builder, Loop Builder, Form submission pipeline, Popups | `elementor-pro/plugin.php`, `modules/theme-builder/`, `modules/forms/` |
| [RENDERING-ENGINE.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/SOURCE-ANALYSIS/RENDERING-ENGINE.md) | `the_content` filter interception, CSS file compilation, cache lifecycle, inline CSS fallback | `elementor/includes/frontend.php`, `core/files/css/post.php`, `base.php` |
| [DOCUMENT-DATA-STRUCTURE.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/SOURCE-ANALYSIS/DOCUMENT-DATA-STRUCTURE.md) | `_elementor_data`, `_elementor_edit_mode`, `_elementor_page_settings`, element JSON schema | `elementor/core/base/document.php`, `includes/elements/container.php` |
| [EDITOR-ARCHITECTURE.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/SOURCE-ANALYSIS/EDITOR-ARCHITECTURE.md) | Editor iframe, Marionette views, Backbone models, `$e.data` command bus | `elementor/assets/js/editor-modules.js`, `core/editor/` |
| [MCP-INTEGRATION.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/SOURCE-ANALYSIS/MCP-INTEGRATION.md) | MCP tools contract: `wp_create_page`, `wp_get_page_layout`, `wp_update_page_layout` | MCP tool schemas, live server execution tests on `wpvision.ir` |

---

## 2. Widget Taxonomy & Catalog (`WIDGETS/`)

| Document | Focus & Scope | Widget Counts |
|---|---|---|
| [WIDGET-INVENTORY.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/WIDGETS/WIDGET-INVENTORY.md) | Master searchable inventory of all 133 widgets (slug, title, category, origin, purpose) | 133 total (38 Free, 95 Pro) |
| [FREE-WIDGETS.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/WIDGETS/FREE-WIDGETS.md) | Detailed analysis of all 38 Free widgets, control groups, responsive capabilities | 38 Free widgets |
| [PRO-WIDGETS.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/WIDGETS/PRO-WIDGETS.md) | Detailed analysis of all 95 Pro widgets across 25 Pro modules | 95 Pro widgets |
| [WIDGET-REFERENCE/BASIC-WIDGETS.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/WIDGETS/WIDGET-REFERENCE/BASIC-WIDGETS.md) | Deep breakdown: Heading, Image, Text Editor, Button, Divider, Spacer, Icon, Google Maps | 8 core basic widgets |
| [WIDGET-REFERENCE/GENERAL-WIDGETS.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/WIDGETS/WIDGET-REFERENCE/GENERAL-WIDGETS.md) | Deep breakdown: Accordion, Tabs, Icon Box, Image Box, Counter, Progress, Testimonial | 16 general widgets |
| [WIDGET-REFERENCE/PRO-THEME-WIDGETS.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/WIDGETS/WIDGET-REFERENCE/PRO-THEME-WIDGETS.md) | Deep breakdown: Post Title, Content, Excerpt, Featured Image, Author Box, Breadcrumbs | 18 Theme Builder widgets |
| [WIDGET-REFERENCE/WOOCOMMERCE-WIDGETS.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/WIDGETS/WIDGET-REFERENCE/WOOCOMMERCE-WIDGETS.md) | Deep breakdown: Products, Product Price, Add to Cart, Product Images, Cart, Checkout | 26 WooCommerce widgets |
| [WIDGET-REFERENCE/LOOP-BUILDER-WIDGETS.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/WIDGETS/WIDGET-REFERENCE/LOOP-BUILDER-WIDGETS.md) | Deep breakdown: Loop Grid, Loop Carousel, Taxonomy Filter, Alternate Template injection | 3 Loop Builder widgets |

---

## 3. Controls & Data Modeling (`CONTROLS/`)

| Document | Focus & Scope | Key Elements |
|---|---|---|
| [CONTROL-INVENTORY.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/CONTROLS/CONTROL-INVENTORY.md) | Exhaustive catalog of all 42 atomic control types and 16 group control types | `Controls_Manager` constants |
| [CONTROL-TYPES.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/CONTROLS/CONTROL-TYPES.md) | API specs, parameter arrays, default structures for Slider, Choose, Color, Dimensions | `Base_Data_Control`, `Base_UI_Control` |
| [GROUP-CONTROLS.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/CONTROLS/GROUP-CONTROLS.md) | Typography, Background, Border, Box-Shadow, Text-Shadow, Flex-Container, Flex-Item | `Group_Control_Base` subclasses |
| [RESPONSIVE-CONTROLS.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/CONTROLS/RESPONSIVE-CONTROLS.md) | Breakpoint suffixes (`_tablet`, `_mobile`), media queries, visibility toggles | `Breakpoints\Manager` |
| [DYNAMIC-CONTROLS.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/CONTROLS/DYNAMIC-CONTROLS.md) | Dynamic tags data format: `__dynamic__` object and `[elementor-tag]` shortcodes | `Core\DynamicTags\Manager` |

---

## 4. Design System & Native Styling (`DESIGN-SYSTEM/`)

| Document | Focus & Scope | Key Elements |
|---|---|---|
| [GLOBAL-STYLES.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/DESIGN-SYSTEM/GLOBAL-STYLES.md) | Default Kit, system colors (Primary, Secondary, Text, Accent), custom palettes | `Kit` document, `__globals__` format |
| [NATIVE-STYLING.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/DESIGN-SYSTEM/NATIVE-STYLING.md) | Zero-CSS styling matrix: converting common visual requirements to native controls | Gradients, shadows, borders, transitions |
| [CONTAINER-ARCHITECTURE.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/DESIGN-SYSTEM/CONTAINER-ARCHITECTURE.md) | Flexbox & Grid containers, direction, wrap, justify, align, gaps, nesting rules | `Includes\Elements\Container` |
| [RESPONSIVE-DESIGN.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/DESIGN-SYSTEM/RESPONSIVE-DESIGN.md) | Desktop, tablet, mobile layouts, responsive typography scales, responsive reordering | Flex direction & order responsive controls |

---

## 5. Implementation & Workflows (`IMPLEMENTATION/`)

| Document | Focus & Scope | Key Elements |
|---|---|---|
| [PAGE-BUILDING-WORKFLOW.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/IMPLEMENTATION/PAGE-BUILDING-WORKFLOW.md) | 7-step repeatable engineering sequence: analysis, widget selection, layout, styling | Systematic procedural workflow |
| [JSON-STRUCTURES.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/IMPLEMENTATION/JSON-STRUCTURES.md) | Exact valid JSON payloads for containers, child containers, and widgets | Fully copy-pasteable JSON schemas |
| [WIDGET-SELECTION-GUIDE.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/IMPLEMENTATION/WIDGET-SELECTION-GUIDE.md) | Decision matrices for choosing the exact native widget for any design requirement | Free vs Pro decision trees |
| [MCP-WORKFLOWS.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/IMPLEMENTATION/MCP-WORKFLOWS.md) | Step-by-step procedures for creating, reading, updating, and validating pages via MCP | MCP tool call sequences |
| [VALIDATION-PROTOCOL.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/IMPLEMENTATION/VALIDATION-PROTOCOL.md) | 5-stage validation checklist (Structural, Zero-CSS, Frontend, Editor, Visual) | Acceptance verification rules |

---

## 6. Ecosystem Integrations (`INTEGRATIONS/`)

| Document | Focus & Scope | Key Elements |
|---|---|---|
| [WOOCOMMERCE.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/INTEGRATIONS/WOOCOMMERCE.md) | WooCommerce Builder, HPOS compatibility, product templates, checkout/cart | `Modules\Woocommerce` |
| [ACF.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/INTEGRATIONS/ACF.md) | Advanced Custom Fields integration via dynamic tags (text, image, URL, repeater) | `Modules\DynamicTags\Acf` |
| [DYNAMIC-CONTENT.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/INTEGRATIONS/DYNAMIC-CONTENT.md) | Custom Post Types, taxonomies, author/user data, date/time, request parameters | `Modules\DynamicTags\Tags` |
| [THIRD-PARTY-COMPATIBILITY.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/INTEGRATIONS/THIRD-PARTY-COMPATIBILITY.md) | Hello Elementor, Astra, WoodMart, WP Rocket, Autoptimize, object caching | Theme hooks, script enqueues |

---

## 7. Testing & Quality Assurance (`TESTING/`)

| Document | Focus & Scope | Key Elements |
|---|---|---|
| [TEST-CASES.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/TESTING/TEST-CASES.md) | Complete executable JSON documents for Tests A through H | Full landing page, article, archive, shop |
| [KNOWN-LIMITATIONS.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/TESTING/KNOWN-LIMITATIONS.md) | Verified technical limitations of native Elementor & approved exception paths | CSS variables, custom SVG clip paths |
| [REGRESSION-TESTING.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/TESTING/REGRESSION-TESTING.md) | Regression checklists for modifying existing pages without collateral damage | Element address preservation |

---

## 8. Evidence & Traceability (`EVIDENCE/`)

| Document | Focus & Scope | Key Elements |
|---|---|---|
| [SOURCE-REFERENCES.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/EVIDENCE/SOURCE-REFERENCES.md) | Exact file paths, line numbers, and method signatures for every finding | Source trace log |
| [API-REFERENCES.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/EVIDENCE/API-REFERENCES.md) | Comprehensive table of PHP classes, methods, and JavaScript APIs | API reference dictionary |
| [VERSION-COMPATIBILITY.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/EVIDENCE/VERSION-COMPATIBILITY.md) | Exact version matrix: WP 7.1.4, Elementor Free 4.2.3, Elementor Pro 4.3.2 | Deprecations & requirements |
| [CONFIDENCE-REPORT.md](file:///c:/Users/hp/Desktop/Elementor%20&%20Wordpress/elementor-engineering-knowledge/EVIDENCE/CONFIDENCE-REPORT.md) | Confidence level ratings (CURRENTLY VERIFIED, USER-CONFIRMED, UNVERIFIED) | Audit audit scorecard |
