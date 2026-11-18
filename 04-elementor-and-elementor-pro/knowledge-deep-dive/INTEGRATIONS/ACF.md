# Advanced Custom Fields (ACF) Integration

## 1. ACF Integration Architecture
Elementor Pro embeds native support for Advanced Custom Fields through its dedicated ACF module (`elementor-pro/modules/dynamic-tags/acf/`).
- No external bridge plugin is required.
- Detects whether ACF Free or ACF Pro is active via `class_exists( 'ACF' )`.
- Dynamically registers tag types in the Elementor controls dynamic menu.

---

## 2. Discovered ACF Dynamic Tags & Field Compatibility

| Dynamic Tag Slug | Target ACF Field Types | Supported Elementor Control Types |
|---|---|---|
| `acf-text` | Text, Textarea, Select, Radio, Button Group | `Controls_Manager::TEXT`, `TEXTAREA`, `WYSIWYG` |
| `acf-number` | Number, Range | `Controls_Manager::NUMBER`, `SLIDER` |
| `acf-image` | Image (Returns Array, ID, or URL) | `Controls_Manager::MEDIA` |
| `acf-file` | File (Returns URL or ID) | `Controls_Manager::URL`, Button Links |
| `acf-url` | URL, Page Link, Link | `Controls_Manager::URL` |
| `acf-date-time` | Date Picker, Date Time Picker, Time Picker | `Controls_Manager::TEXT`, `DATE_TIME` |
| `acf-color` | Color Picker | `Controls_Manager::COLOR` |
| `acf-gallery` | Gallery (ACF Pro) | `Controls_Manager::GALLERY` |

---

## 3. JSON Data Binding Schema for ACF Fields
To bind an Elementor Heading or Button to an ACF field named `event_start_date`:

```json
{
  "settings": {
    "title": "TBD",
    "__dynamic__": {
      "title": "[elementor-tag id=\"acf_91a2\" name=\"acf-date-time\" settings=\"%7B%22key%22%3A%22event_start_date%22%2C%22format%22%3A%22F%20j%2C%20Y%22%2C%22fallback%22%3A%22Date%20Announced%20Soon%22%7D\"]"
    }
  }
}
```

### Parameter Dictionary for `settings`:
- `key`: The ACF field key or name (e.g. `"event_start_date"`).
- `format`: PHP date formatting string (e.g. `"F j, Y"`).
- `before`: Prepend string (e.g. `"Date: "`).
- `after`: Append string.
- `fallback`: Default text shown when the custom field is empty.

---

## 4. ACF Repeater & Flexible Content Workflows
When ACF Pro Repeaters are used:
- Loop Builder can be configured to loop through ACF post objects or relational posts.
- For nested sub-fields within standard repeaters, utilize the Elementor Loop Grid with ACF relationship queries to render uniform repeated cards.
