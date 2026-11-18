# Elementor Core Architecture (Free v4.2.3)

## 1. Plugin Bootstrap & Singleton Pattern
Elementor Free bootstraps from `elementor/elementor.php`:
```php
define( 'ELEMENTOR_VERSION', '4.2.3' );
require ELEMENTOR_PATH . 'includes/plugin.php';
\Elementor\Plugin::instance();
```
`Elementor\Plugin` is a monolithic singleton providing access to all core subsystem managers:
- `$plugin->elements_manager`: Manages structural element types (`container`, legacy `section`, `column`).
- `$plugin->widgets_manager`: Manages interactive content widgets (`heading`, `image`, `button`, etc.).
- `$plugin->controls_manager`: Manages the registration and rendering of control types (`text`, `slider`, `choose`, etc.).
- `$plugin->documents`: Manages document abstraction for posts, pages, and library templates.
- `$plugin->kits_manager`: Manages the active design system kit (Global Colors, Global Fonts, Theme Style).
- `$plugin->breakpoints`: Manages responsive viewport thresholds.
- `$plugin->files_manager`: Manages generated CSS and asset caching.
- `$plugin->dynamic_tags`: Manages dynamic content replacement.
- `$plugin->frontend`: Orchestrates server-side markup generation and asset enqueues.
- `$plugin->editor`: Orchestrates the editor iframe, configuration data, and Backbone UI assets.

---

## 2. Element Class Hierarchy

```
\Elementor\Controls_Stack
   │
   ├── \Elementor\Core\Base\Document  (Document abstraction for WP Posts/Templates)
   │     ├── \Elementor\Core\DocumentTypes\Page
   │     ├── \Elementor\Core\DocumentTypes\Post
   │     └── \Elementor\Core\Kits\Documents\Kit (Site Settings)
   │
   └── \Elementor\Element_Base  (Visual nodes rendered in DOM)
         │
         ├── \Elementor\Includes\Elements\Container  (Flexbox / Grid Container)
         ├── \Elementor\Element_Section             (Legacy Section)
         ├── \Elementor\Element_Column              (Legacy Column)
         │
         └── \Elementor\Widget_Base                 (Content Widgets)
               ├── \Elementor\Widget_Heading
               ├── \Elementor\Widget_Image
               ├── \Elementor\Widget_Button
               └── [130+ other widgets]
```

### Key Responsibilities of Base Classes
1. **`Controls_Stack`**:
   - Manages the registration of tabs, sections, controls, and group controls.
   - Handles control condition evaluation (`condition` and `conditions` arrays).
   - Provides getter methods for settings (`get_settings_for_display()`, `get_settings()`).
   - Manages dynamic tag binding resolution (`__dynamic__`).
2. **`Element_Base`**:
   - Implements DOM wrapping logic (`before_render()`, `after_render()`).
   - Renders HTML wrapper tags, classes, and data attributes (`data-id`, `data-element_type`).
   - Manages children (`$this->children`) and recursive child rendering.
   - Manages advanced tab controls (margin, padding, z-index, animations, responsive visibility).
3. **`Widget_Base`**:
   - Declares widget metadata (`get_name()`, `get_title()`, `get_icon()`, `get_categories()`, `get_keywords()`).
   - Implements `render()`: PHP server-side HTML output.
   - Implements `content_template()`: JavaScript Underscore/Mustache template for instant client-side editor re-rendering.
4. **`Container`**:
   - Modern layout element (`elType: "container"`).
   - Can act as a root container (`isInner: false`) or a nested child container (`isInner: true`).
   - Registers layout controls (`Group_Control_Flex_Container` or `Group_Control_Grid_Container`).
   - Direct parent for widgets and other containers.

---

## 3. Element Lifecycle & Hook Execution
When an element renders on the frontend:

1. **Instantiation**:
   - Element is constructed with its persistent data: `new Widget_Heading( $data, $args )`.
   - `$data['id']`, `$data['settings']`, and `$data['elements']` are bound.
2. **Control Registration**:
   - `register_controls()` is invoked lazily on first access.
   - Action `elementor/element/{$element_name}/{$section_id}/before_section_start` fires.
   - Controls and responsive controls are appended to the stack.
   - Action `elementor/element/{$element_name}/{$section_id}/after_section_end` fires.
3. **Data Preparation**:
   - `get_settings_for_display()` parses:
     - Global tokens (`__globals__`): Resolves CSS variables or fallbacks.
     - Dynamic tags (`__dynamic__`): Executes tag callbacks and replaces placeholders.
4. **Rendering**:
   - `before_render()`: Prints `<div class="elementor-element elementor-element-{$id} e-con-full e-con" data-id="{$id}" data-element_type="container">`.
   - `render()` or `render_children()`: Prints inner content or iterates child nodes.
   - `after_render()`: Closes wrapper `</div>`.

---

## 4. Modern Experiments & Architectural Flags
In Elementor 4.x, modern architecture is controlled via the Experiments system (`Elementor\Core\Experiments\Manager`):
- **Flexbox Container (`container`)**: State: Active by default. Replaces sections and columns with flex containers.
- **Nested Elements (`nested-elements`)**: State: Active. Enables native widgets (Tabs, Accordion, Carousel) to contain nested sub-containers directly inside tabs or slides.
- **Optimized DOM Output (`optimized_dom_output`)**: Eliminates redundant wrapper divs (`elementor-widget-container`) when unnecessary.
- **Improved CSS Loading (`e_optimized_css_loading`)**: Enqueues widget-specific CSS stylesheets only on pages where that widget is present, drastically reducing CSS payload size.
