# WordPress MCP Operational Workflows for Elementor

## 1. Workflow 1: Initializing a New Elementor Page
When asked to build a new page from scratch:

### Step 1.1: Construct the Initial Elementor Document JSON
Prepare the root containers and primary widgets with all settings:
```json
[
  {
    "id": "root_section_1",
    "elType": "container",
    "isInner": false,
    "settings": {
      "content_width": "boxed",
      "flex_direction": "column",
      "padding": { "unit": "px", "top": "80", "right": "24", "bottom": "80", "left": "24", "isLinked": false }
    },
    "elements": [
      {
        "id": "main_heading",
        "elType": "widget",
        "widgetType": "heading",
        "settings": {
          "title": "Page Title Here",
          "header_size": "h1",
          "align": "center"
        },
        "elements": []
      }
    ]
  }
]
```

### Step 1.2: Call `wp_create_page` with Meta
Pass the serialized JSON inside `meta`:
```json
{
  "title": "About Us",
  "status": "publish",
  "meta": {
    "_elementor_edit_mode": "builder",
    "_elementor_template_type": "wp-page",
    "_elementor_data": "[{\"id\":\"root_section_1\",\"elType\":\"container\"...}]"
  }
}
```

---

## 2. Workflow 2: Inspecting an Existing Page
To view existing elements and prepare for edits:

### Step 2.1: Call `wp_get_page_layout`
```json
{
  "post_id": 12345,
  "include_settings": true,
  "depth": 6
}
```

### Step 2.2: Extract Critical Fields
From the response:
- Verify `"builder": "elementor"`.
- Verify `"editable": true`.
- Store the `"version"` token string (e.g. `"1ce3144764a20f9d"`).
- Locate the address (`id`) of the target element to modify or insert next to.

---

## 3. Workflow 3: Modifying Elements Safely (`wp_update_page_layout`)

### Step 3.1: Discover Field Names (If Unsure)
Call `wp_list_layout_elements`:
```json
{
  "type": "heading"
}
```

### Step 3.2: Dispatch Atomic Operations
Pass the stored `version` and the ordered array of `ops`:
```json
{
  "post_id": 12345,
  "version": "1ce3144764a20f9d",
  "ops": [
    {
      "op": "set_text",
      "element": "main_heading",
      "field": "title",
      "value": "Updated Heading Content"
    },
    {
      "op": "insert",
      "element_type": "button",
      "parent": "root_section_1",
      "fields": {
        "text": "Contact Our Team",
        "size": "lg"
      }
    }
  ]
}
```

### Step 3.3: Handle Version Changes
Upon success, the tool returns a new `version` token. Store this new token for any subsequent edits on the same page.
