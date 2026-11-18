# WordPress MCP Integration & Page Operations

## 1. Overview of MCP Tooling for Elementor
The WordPress MCP environment provides specialized tools designed to create, read, update, and validate Elementor pages natively, without raw SQL execution or fragile regex parsing.

### Available Page-Builder MCP Tools

| MCP Tool Name | Operation Type | Purpose in Elementor Workflow |
|---|---|---|
| `wp_create_page` | Write / Create | Initializes a new WordPress page and seeds initial Elementor document metadata (`_elementor_data`, `_elementor_edit_mode`, `_elementor_template_type`). |
| `wp_get_page_layout` | Read / Inspect | Reads the Elementor hierarchy, elements array, element addresses, stored settings, and concurrency version token. |
| `wp_list_layout_elements` | Discovery | Inspects the active Elementor runtime to return exact allowed fields, types, options, and defaults for any widget. |
| `wp_update_page_layout` | Atomic Mutation | Performs builder-safe atomic edits (`set_text`, `set_link`, `set_image`, `set_fields`, `insert`, `remove`, `move`, `duplicate`), maintaining revisions and cache. |
| `wp_delete_page` | Cleanup / Delete | Moves to trash or permanently deletes test pages. |

---

## 2. Operation 1: Creating a New Native Elementor Page
To create an authentic Elementor page directly via MCP, pass the metadata inside the `meta` parameter of `wp_create_page`:

```json
{
  "title": "Services Landing Page",
  "status": "publish",
  "meta": {
    "_elementor_edit_mode": "builder",
    "_elementor_template_type": "wp-page",
    "_elementor_data": "[{\"id\":\"hero_con\",\"elType\":\"container\",\"settings\":{\"content_width\":\"boxed\",\"flex_direction\":\"column\",\"padding\":{\"unit\":\"px\",\"top\":\"60\",\"right\":\"24\",\"bottom\":\"60\",\"left\":\"24\",\"isLinked\":false}},\"elements\":[{\"id\":\"hero_h1\",\"elType\":\"widget\",\"widgetType\":\"heading\",\"settings\":{\"title\":\"Enterprise Cloud Solutions\",\"header_size\":\"h1\",\"align\":\"center\"},\"elements\":[]}]}]"
  }
}
```

### Verified Runtime Behavior:
- WordPress registers the page ID.
- Elementor metadata persists with `show_in_rest` validation.
- On first visit to `/?page_id={$id}`, Elementor detects `_elementor_edit_mode = 'builder'` and automatically renders the native Flexbox container and heading widget.

---

## 3. Operation 2: Inspecting an Elementor Page (`wp_get_page_layout`)
To read a page's existing layout and obtain its concurrency token:

```json
{
  "post_id": 65191,
  "include_settings": true
}
```

### Response Schema:
```json
{
  "post_id": 65191,
  "builder": "elementor",
  "builder_version": "4.3.4",
  "version": "1ce3144764a20f9d",
  "element_count": 3,
  "editable": true,
  "elements": [
    {
      "address": "hero_con",
      "type": "container",
      "settings": { ... },
      "children_count": 2,
      "children": [
        {
          "address": "hero_h1",
          "type": "heading",
          "text": "Enterprise Cloud Solutions",
          "settings": { ... },
          "children_count": 0
        }
      ]
    }
  ]
}
```

---

## 4. Operation 3: Discovering Widget Fields (`wp_list_layout_elements`)
Never guess widget control field names. Query the live runtime directly:

```json
{
  "type": "button"
}
```

The response returns the exact field dictionary:
- `text`: text control, default "Click here"
- `link`: url control
- `size`: select control (`xs`, `sm`, `md`, `lg`, `xl`)
- `button_type`: select (`info`, `success`, `warning`, `danger`)
- `selected_icon`: icon control

---

## 5. Operation 4: Updating an Existing Elementor Page (`wp_update_page_layout`)
On existing Elementor pages, **direct updates to `_elementor_data` via `wp_update_post_meta` are prohibited** by the WordPress MCP server to prevent cache desynchronization and broken revisions.

Instead, execute atomic operations via `wp_update_page_layout` using the `version` string from `wp_get_page_layout`:

```json
{
  "post_id": 65191,
  "version": "1ce3144764a20f9d",
  "ops": [
    {
      "op": "set_text",
      "element": "hero_h1",
      "field": "title",
      "value": "Scalable Infrastructure Architecture"
    },
    {
      "op": "insert",
      "element_type": "button",
      "parent": "hero_con",
      "fields": {
        "text": "Explore Services",
        "size": "lg"
      }
    }
  ]
}
```

### Execution Guarantee:
- Operations are applied atomically in sequential order.
- Elementor's native save hooks run.
- A WordPress post revision is created.
- The CSS cache is invalidated and regenerated.
