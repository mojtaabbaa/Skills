# Elementor PHP & JavaScript API Reference

## 1. Core PHP Action Hooks

| Action Hook Name | Arguments | Description |
|---|---|---|
| `elementor/init` | *(none)* | Fires after Elementor is fully initialized and all components are registered. |
| `elementor/widgets/register` | `\Elementor\Widgets_Manager $widgets_manager` | Recommended hook to register new custom widgets (`$widgets_manager->register(...)`). |
| `elementor/controls/register` | `\Elementor\Controls_Manager $controls_manager` | Recommended hook to register new atomic or group controls. |
| `elementor/elements/categories_registered` | `\Elementor\Elements_Manager $elements_manager` | Fires after element categories are registered. |
| `elementor/dynamic_tags/register` | `\Elementor\Core\DynamicTags\Manager $dynamic_tags` | Registers custom dynamic tags. |
| `elementor/editor/after_save` | `int $post_id, array $editor_data` | Fires immediately after an Elementor document saves data to the database. |
| `elementor/frontend/after_enqueue_styles` | *(none)* | Fires after Elementor frontend styles are enqueued. |
| `elementor/frontend/after_register_scripts` | *(none)* | Fires after Elementor frontend scripts are registered. |
| `elementor/document/save/data` | `array $data, \Elementor\Core\Base\Document $document` | Fires before saving document data. |
| `elementor/css-file/before_enqueue` | `\Elementor\Core\Files\CSS\Base $css_file` | Fires before a compiled CSS file is enqueued. |

---

## 2. Core PHP Filter Hooks

| Filter Hook Name | Arguments | Return Type | Description |
|---|---|---|---|
| `elementor/widgets/is_widget_enabled` | `bool $should_register, \Elementor\Widget_Base $widget` | `bool` | Allows selectively disabling widgets before registration. |
| `elementor/document/load/data` | `array $data, \Elementor\Core\Base\Document $document` | `array` | Filters document element data during loading. |
| `elementor/frontend/builder_content_data` | `array $data, int $post_id` | `array` | Filters the builder elements tree before rendering. |
| `the_content` (Priority `999999`) | `string $content` | `string` | Replaces post content with compiled Elementor builder output. |
| `template_include` (Priority `9999`) | `string $template` | `string` | Intercepts template selection for Canvas, Full Width, or Theme Builder. |
| `elementor_pro/forms/render/item/{$type}` | `array $item, int $item_index, \ElementorPro\Modules\Forms\Widgets\Form $form` | `array` | Filters individual form field markup before rendering. |

---

## 3. Core JavaScript Frontend & Editor APIs

| JavaScript API / Object | Scope | Description |
|---|---|---|
| `elementorFrontend.hooks` | Frontend | Action/filter hook bus for frontend element lifecycle (`addAction`, `addFilter`). |
| `elementorFrontend.hooks.addAction('frontend/element_ready/{widgetType}', handler)` | Frontend | Triggers when a widget is mounted or re-rendered via AJAX. |
| `$e.run( command, args )` | Editor | Unified command runner (e.g. `$e.run('document/save/default')`). |
| `$e.data` | Editor | REST/Data API manager for fetching models, collections, and global tokens. |
| `elementor.elements.toJSON()` | Editor | Extracts the full active element hierarchy as a serialized JavaScript object array. |
| `elementorCommon.helpers.getUniqueId()` | Editor | Generates a unique 7-character hexadecimal element ID. |
