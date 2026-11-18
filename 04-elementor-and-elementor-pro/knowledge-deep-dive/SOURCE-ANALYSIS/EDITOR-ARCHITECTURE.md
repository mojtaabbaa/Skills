# Elementor Editor Architecture & Client-Side Engine

## 1. Dual-Window Architecture & Preview Iframe
Elementor's visual editor utilizes a dual-window sandboxed architecture:
- **Top Window (`window.top`)**: Hosts the Elementor Editor UI panel, navigation tree, widget catalog, settings controls, and revision history.
- **Preview Iframe (`window` inside iframe)**: Hosts the actual WordPress frontend page, rendering live HTML, theme styles, and enqueued scripts.

Communication between the panel and iframe occurs via direct JavaScript reference (`elementor.$previewContents`, `elementorFrontend`) and postMessage channels.

---

## 2. Client-Side Framework & MVC Architecture
The editor panel is built on **Marionette.js** and **Backbone.js**:
- **Backbone Models (`elementor.modules.elements.models.Element`)**:
  - Each container and widget is represented by an active Backbone model.
  - Attributes mirror the database schema: `id`, `elType`, `widgetType`, `settings`, `elements`.
  - Setting changes immediately trigger model change events: `change:settings:{controlName}`.
- **Marionette Views (`elementor.modules.elements.views.Element`)**:
  - Live preview DOM elements are managed by Marionette item views.
  - Controls panel is rendered by `elementor.modules.controls.views.Control`.

---

## 3. The `$e` Command Bus & Data API
Elementor includes a unified, declarative command architecture accessible via the global `$e` object:
- **`$e.run( command, args )`**: Executes actions (e.g. `$e.run( 'document/elements/create', { ... } )`, `$e.run( 'document/save/default' )`).
- **`$e.data`**: Manages REST/AJAX data synchronization:
  - Format: `$e.data.get( 'globals/colors' )`
  - Command Extraction: `commandExtractArgs( valueToParse )` resolves strings like `globals/colors?id=primary`.
- **`$e.components`**: Extensible registry for editor modules (Theme Builder, Site Settings, Finder, History).

---

## 4. Instant Live Preview: `content_template()`
To avoid slow round-trip server requests during dragging, typing, or styling, Elementor widgets provide a JavaScript template method: `content_template()`.

Example from `Widget_Heading`:
```php
protected function content_template() {
    ?>
    <#
    var title = settings.title;
    if ( '' !== settings.link.url ) {
        title = '<a href="' + settings.link.url + '">' + title + '</a>';
    }
    #>
    <{{{ settings.header_size }}} class="elementor-heading-title elementor-size-{{{ settings.size }}}">
        {{{ title }}}
    </{{{ settings.header_size }}}>
    <?php
}
```
- `<# ... #>` evaluates JavaScript logic on the client.
- `{{{ data }}}` outputs unescaped HTML.
- `{{ data }}` outputs escaped text.

When a user types in the Title control, Marionette instantly executes `content_template()` client-side, updating the iframe DOM in under 5 milliseconds.

---

## 5. Document Save Lifecycle in the Editor
When the user clicks "Update" or "Publish" in the editor:
1. `$e.run( 'document/save/default' )` is triggered.
2. The complete element tree is extracted from the Backbone models:
   ```javascript
   var data = elementor.elements.toJSON();
   ```
3. An AJAX request is dispatched to `admin-ajax.php`:
   - Action: `elementor_ajax`
   - Actions payload:
     ```json
     {
       "action": "save_builder",
       "data": {
         "status": "publish",
         "elements": [ ... ],
         "settings": { ... }
       }
     }
     ```
4. On the server, `Elementor\Core\Base\Document::save()` receives the payload, invokes `save_elements()`, updates `wp_postmeta`, regenerates plain text content, and compiles the CSS file.
