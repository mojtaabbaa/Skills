# Source Code Traceability & Evidence Ledger

## 1. Core Post Lifecycle & Metadata Storage
- **File**: `elementor/core/base/document.php`
  - `const ELEMENTOR_DATA_META_KEY = '_elementor_data';` (Line 44)
  - `const BUILT_WITH_ELEMENTOR_META_KEY = '_elementor_edit_mode';` (Line 46)
  - `const TYPE_META_KEY = '_elementor_template_type';` (Line 42)
  - `const PAGE_META_KEY = '_elementor_page_settings';` (Line 43)
  - `public function save( $data )` (Lines 812–850)
  - `protected function save_elements( $elements )` (Lines 1380–1420)
  - `public function is_built_with_elementor()` (Lines 943–945)

---

## 2. Frontend Rendering & CSS File Generation
- **File**: `elementor/includes/frontend.php`
  - Priority filter: `add_filter( 'the_content', [ $this, 'apply_builder_in_content' ], self::THE_CONTENT_FILTER_PRIORITY );` (Line 324)
  - Method: `public function apply_builder_in_content( $content )` (Lines 1094–1116)
  - Method: `public function get_builder_content( $post_id, $with_css = false )` (Lines 1134–1175)
- **File**: `elementor/core/files/css/post.php`
  - Class: `\Elementor\Core\Files\CSS\Post` extends `Base` (Lines 22–80)
  - Meta key: `const META_KEY = '_elementor_css';` (Line 29)
  - Prefix: `const FILE_PREFIX = 'post-';` (Line 27)
- **File**: `elementor/core/files/css/base.php`
  - Method: `public function enqueue()` (Lines 203–240)
  - Method: `public function update()` (Line 132)

---

## 3. Container & Layout Engine
- **File**: `elementor/includes/elements/container.php`
  - Class: `\Elementor\Includes\Elements\Container` extends `Element_Base` (Lines 27–60)
  - Type: `public static function get_type() { return 'container'; }` (Line 50)
  - Control registration: `protected function register_controls()`
- **File**: `elementor/includes/controls/groups/flex-container.php`
  - Class: `\Elementor\Group_Control_Flex_Container` extends `Group_Control_Base`
  - Fields: `direction`, `justify_content`, `align_items`, `flex_wrap`, `gap`
- **File**: `elementor/includes/controls/groups/flex-item.php`
  - Class: `\Elementor\Group_Control_Flex_Item` extends `Group_Control_Base`
  - Fields: `basis_type`, `basis`, `align_self`, `order`

---

## 4. Controls System & Registry
- **File**: `elementor/includes/managers/controls.php`
  - Class: `\Elementor\Controls_Manager`
  - Control type constants: `TEXT`, `NUMBER`, `SLIDER`, `DIMENSIONS`, `CHOOSE`, `COLOR`, `MEDIA`, `REPEATER`, `GAPS`
- **Directory**: `elementor/includes/controls/` (42 atomic control classes)
- **Directory**: `elementor/includes/controls/groups/` (11 core group controls)

---

## 5. Dynamic Tags Framework
- **File**: `elementor/core/dynamic-tags/manager.php`
  - `const TAG_LABEL = 'elementor-tag';` (Line 16)
  - `const DYNAMIC_SETTING_KEY = '__dynamic__';` (Line 22)
  - `public function tag_to_text( Base_Tag $tag )` (Lines 141–143)
  - `public function tag_text_to_tag_data( $tag_text )` (Lines 113–127)

---

## 6. Global Design System (Kit)
- **File**: `elementor/core/kits/documents/kit.php`
  - Class: `\Elementor\Core\Kits\Documents\Kit`
  - Tabs: `global-colors`, `global-typography`, `settings-layout`, `theme-style-typography`
- **File**: `elementor/core/kits/documents/tabs/global-colors.php`
  - Constants: `COLOR_PRIMARY = 'globals/colors?id=primary';`, `COLOR_SECONDARY = 'globals/colors?id=secondary';`
- **File**: `elementor/assets/js/editor-modules.js`
  - Model: `_this.globals = new Backbone.Model(_this.settings.get('__globals__'));` (Line 180)
  - Resolution: `var globalValue = this.attributes.__globals__[controlGlobalKey];` (Line 1023)

---

## 7. Elementor Pro Subsystems
- **Theme Builder**: `elementor-pro/modules/theme-builder/`
  - Locations Manager: `classes/locations-manager.php`
  - Conditions Manager: `classes/conditions-manager.php`
  - Conditions Meta: `_elementor_conditions` in `classes/conditions-cache.php` (Line 113)
- **Loop Builder**: `elementor-pro/modules/loop-builder/`
  - Widgets: `widgets/loop-grid.php`, `widgets/loop-carousel.php`
  - Filter: `elementor-pro/modules/loop-filter/widgets/taxonomy-filter.php`
- **Forms**: `elementor-pro/modules/forms/`
  - Widget: `widgets/form.php`
  - Handler: `classes/ajax-handler.php`
- **WooCommerce**: `elementor-pro/modules/woocommerce/`
  - Widgets: 26 specialized WooCommerce widgets in `widgets/`
  - Tags: 13 WooCommerce dynamic tags in `tags/`
