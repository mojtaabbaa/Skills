# Elementor Pro Architecture (v4.3.2)

## 1. Plugin Bootstrap & Module Subsystem
Elementor Pro extends Elementor Core through a dedicated modular system:
- File: `elementor-pro/elementor-pro.php`
- Bootstrap: `\ElementorPro\Plugin::instance()`
- Minimum Core Requirement: Elementor 4.0 (Recommended 4.2+)
- Main class: `ElementorPro\Plugin` extends `ElementorPro\Base\App`

### Module Loading Pattern
Elementor Pro operates via autonomous modules located under `elementor-pro/modules/`. Each module inherits from `ElementorPro\Base\Module_Base` and defines its own widgets, controls, dynamic tags, and lifecycle hooks:
```php
abstract class Module_Base {
    abstract public function get_name();
    public function get_widgets() { return []; }
    public function get_component_type() { return 'module'; }
}
```

---

## 2. Core Pro Modules & Architectural Subsystems

### A. Theme Builder (`modules/theme-builder/`)
Replaces WordPress theme templates entirely with visual Elementor documents.
- **Locations Manager (`Classes\Locations_Manager`)**:
  - Registers theme locations: `header`, `footer`, `single`, `archive`.
  - Checks if a location has an assigned active template before theme output:
    ```php
    elementor_theme_do_location( 'header' );
    ```
- **Conditions Manager (`Classes\Conditions_Manager`)**:
  - Manages display conditions stored in `_elementor_conditions` post meta on template library posts.
  - Resolves condition hierarchies: `Entire Site` (`include/general`), `Singular` (`include/singular/page`, `include/singular/post`), `Archives` (`include/archive`).
  - Cache: `Conditions_Cache` stores a serialized map of condition-to-template IDs in the `elementor_pro_theme_builder_conditions` option for fast runtime lookup without queries.

### B. Loop Builder (`modules/loop-builder/`)
Allows designers to build custom repeated item templates for post archives and product grids.
- **Loop Document (`Documents\Loop`)**:
  - Template post type: `elementor_library` with `_elementor_template_type = 'loop'`.
  - Built using Containers and dynamic widgets (`post-title`, `post-featured-image`, `custom-field`).
- **Loop Grid Widget (`Widgets\Loop_Grid`)**:
  - Queries posts via `Group_Control_Query` (`post_type`, taxonomies, author, date, manual inclusion/exclusion).
  - Iterates posts, sets global `$post`, and renders the designated Loop Template for each item.
  - Supports **Alternate Templates**: Injects distinct templates at specified intervals (e.g. ad banners or featured cards every 4 items).
- **Loop Carousel Widget (`Widgets\Loop_Carousel`)**:
  - Extends Swiper slider engine to cycle through rendered loop items.
- **Taxonomy Filter Widget (`Widgets\Taxonomy_Filter`)**:
  - AJAX filtering interface that updates connected Loop Grids without full page reload.

### C. Forms Subsystem (`modules/forms/`)
Full visual form builder and processing pipeline.
- **Form Widget (`Widgets\Form`)**:
  - Field types: `text`, `email`, `textarea`, `url`, `tel`, `radio`, `select`, `checkbox`, `acceptance`, `number`, `date`, `time`, `file`, `password`, `html`, `hidden`, `step` (multi-step form).
- **Form Submission Pipeline (`Classes\Form_Record`, `Classes\Ajax_Handler`)**:
  - AJAX endpoint: `action=elementor_pro_forms_send_form`.
  - Lifecycle: Nonce validation → Honeypot verification → Field validation & sanitization → File upload handling → Execution of Actions After Submit.
- **Actions After Submit**:
  - Core actions: `email`, `email2`, `redirect`, `webhook`, `popup`, `mailchimp`, `drip`, `activecampaign`, `getresponse`, `convertkit`, `slack`, `discord`.
  - Submissions Storage: Form entries are stored in custom tables (`wp_e_submissions` and `wp_e_submissions_values`) for admin auditing and CSV export.

### D. Popup Builder (`modules/popup/`)
Modal, slide-in, notification bar, and full-screen overlay engine.
- **Popup Document (`Document`)**:
  - Template type: `popup`.
  - Stored in `wp_posts` with `post_type: 'elementor_library'`.
- **Triggers**:
  - On Page Load (with delay), On Scroll, On Scroll To Element, On Click, After Inactivity, On Page Exit Intent.
- **Timing & Advanced Rules**:
  - Show after X page views, show after X sessions, show up to X times, when arriving from specific search engines, hide for logged-in users, show on specific devices.

### E. Dynamic Tags Engine (`modules/dynamic-tags/`)
Provides dynamic context binding for any text, URL, image, or media control across Free and Pro widgets.
- Extended by:
  - ACF Module (`modules/dynamic-tags/acf/`)
  - Pods Module (`modules/dynamic-tags/pods/`)
  - Toolset Module (`modules/dynamic-tags/toolset/`)
  - WooCommerce Module (`modules/woocommerce/tags/`)

### F. Motion Effects (`modules/motion-fx/`)
Hardware-accelerated visual transforms applied natively via data attributes:
- **Scrolling Effects**: Vertical Scroll, Horizontal Scroll, Transparency, Blur, Rotate, Scale.
- **Mouse Effects**: Mouse Track, 3D Tilt.
- **Sticky Controls**: Sticky to Top/Bottom, offset, effects offset, stay in column.
- Rendered via CSS transforms on the container/widget wrapper without custom JavaScript.
