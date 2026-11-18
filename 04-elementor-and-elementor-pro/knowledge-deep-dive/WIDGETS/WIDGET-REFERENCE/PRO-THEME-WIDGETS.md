# Widget Reference: Pro Theme Builder Widgets

## 1. Post Title (`post-title`)
- **Origin**: Elementor Pro
- **Class**: `\ElementorPro\Modules\ThemeBuilder\Widgets\Post_Title`
- **Dynamic Context**: Automatically queries `get_the_title()` of the queried object.
- **Settings Data Contract**:
  ```json
  {
    "header_size": "h1",
    "align": "left",
    "title_color": "#0f172a",
    "typography_typography": "custom",
    "typography_font_family": "Inter",
    "typography_font_size": { "unit": "px", "size": 42 },
    "typography_font_size_mobile": { "unit": "px", "size": 28 },
    "typography_font_weight": "800",
    "typography_line_height": { "unit": "em", "size": 1.25 }
  }
  ```

---

## 2. Post Info (`post-info`)
- **Origin**: Elementor Pro
- **Class**: `\ElementorPro\Modules\ThemeElements\Widgets\Post_Info`
- **Settings Data Contract**:
  ```json
  {
    "icon_list": [
      {
        "_id": "meta_author",
        "type": "author",
        "show_avatar": "yes",
        "avatar_size": 24
      },
      {
        "_id": "meta_date",
        "type": "date",
        "date_format": "default",
        "show_icon": "yes",
        "icon": { "value": "far fa-calendar-alt", "library": "fa-regular" }
      },
      {
        "_id": "meta_comments",
        "type": "comments",
        "show_icon": "yes",
        "icon": { "value": "far fa-comment", "library": "fa-regular" }
      }
    ],
    "layout": "inline",
    "space_between": { "unit": "px", "size": 16 },
    "text_color": "#64748b",
    "icon_color": "#94a3b8",
    "typography_typography": "custom",
    "typography_font_size": { "unit": "px", "size": 14 }
  }
  ```
- **Zero-CSS Replacements**:
  - Replaces custom flex metadata rows, avatar round borders, icon-to-text gaps, and inline date formatting.

---

## 3. Post Content (`post-content`)
- **Origin**: Elementor Pro
- **Class**: `\ElementorPro\Modules\ThemeBuilder\Widgets\Post_Content`
- **Function**: Renders `the_content()` of the queried post within a Single Post/Page Theme Builder template.
- **Rule of Engagement**: Essential placeholder inside single templates. Must never be placed in standard pages.

---

## 4. Author Box (`author-box`)
- **Origin**: Elementor Pro
- **Class**: `\ElementorPro\Modules\ThemeElements\Widgets\Author_Box`
- **Settings Data Contract**:
  ```json
  {
    "source": "current",
    "show_avatar": "yes",
    "avatar_size": { "unit": "px", "size": 80 },
    "avatar_border_radius": { "unit": "%", "size": 50 },
    "author_name_tag": "h4",
    "show_bio": "yes",
    "show_link": "yes",
    "link_text": "View All Articles",
    "box_border_border": "solid",
    "box_border_width": { "unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": true },
    "box_border_color": "#e2e8f0",
    "box_border_radius": { "unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": true },
    "box_padding": { "unit": "px", "top": "24", "right": "24", "bottom": "24", "left": "24", "isLinked": true }
  }
  ```
