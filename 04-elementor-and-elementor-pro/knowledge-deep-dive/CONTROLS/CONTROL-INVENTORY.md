# Master Control Inventory & Registration Taxonomy

## Complete Controls Index
Discovered directly in `elementor/includes/managers/controls.php`, `elementor/includes/controls/`, and `elementor-pro/modules/`:
- **Total Atomic Control Types**: 42
- **Total Group Control Types**: 16

---

## 1. Atomic Control Types (`Controls_Manager`)

| # | Control Constant | Slug | Class Name | Output / Data Type |
|---|---|---|---|---|
| 1 | `TEXT` | `text` | `Control_Text` | String |
| 2 | `NUMBER` | `number` | `Control_Number` | Numeric (int/float) |
| 3 | `TEXTAREA` | `textarea` | `Control_Textarea` | Multiline string |
| 4 | `SELECT` | `select` | `Control_Select` | String (selected option key) |
| 5 | `SELECT2` | `select2` | `Control_Select2` | String or Array (single or multiple) |
| 6 | `SWITCHER` | `switcher` | `Control_Switcher` | String (`'yes'` or `''`) |
| 7 | `BUTTON` | `button` | `Control_Button` | UI Trigger button |
| 8 | `HIDDEN` | `hidden` | `Control_Hidden` | String (hidden config) |
| 9 | `HEADING` | `heading` | `Control_Heading` | UI Section Heading |
| 10 | `RAW_HTML` | `raw_html` | `Control_Raw_Html` | UI HTML description |
| 11 | `NOTICE` | `notice` | `Control_Notice` | UI Info/Warning Alert box |
| 12 | `DEPRECATED_NOTICE`| `deprecated_notice` | `Control_Deprecated_Notice` | UI deprecation warning |
| 13 | `ALERT` | `alert` | `Control_Alert` | UI Banner alert |
| 14 | `POPOVER_TOGGLE` | `popover_toggle` | `Control_Popover_Toggle` | Boolean popover trigger |
| 15 | `SECTION` | `section` | `Control_Section` | UI Accordion Section |
| 16 | `TAB` | `tab` | `Control_Tab` | UI Tab delimiter |
| 17 | `TABS` | `tabs` | `Control_Tabs` | UI Tabs wrapper (Normal/Hover) |
| 18 | `DIVIDER` | `divider` | `Control_Divider` | UI Horizontal separator |
| 19 | `COLOR` | `color` | `Control_Color` | Hex/RGBA string or Global Token |
| 20 | `MEDIA` | `media` | `Control_Media` | Object (`url`, `id`) |
| 21 | `SLIDER` | `slider` | `Control_Slider` | Object (`unit`, `size`, `sizes`) |
| 22 | `DIMENSIONS` | `dimensions` | `Control_Dimensions` | Object (`unit`, `top`, `right`, `bottom`, `left`, `isLinked`) |
| 23 | `CHOOSE` | `choose` | `Control_Choose` | String (icon segmented choice) |
| 24 | `VISUAL_CHOICE` | `visual_choice` | `Control_Visual_Choice` | String (image card picker) |
| 25 | `WYSIWYG` | `wysiwyg` | `Control_Wysiwyg` | HTML rich text |
| 26 | `CODE` | `code` | `Control_Code` | Code string (ACE editor) |
| 27 | `FONT` | `font` | `Control_Font` | Font family name |
| 28 | `IMAGE_DIMENSIONS`| `image_dimensions` | `Control_Image_Dimensions` | Object (`width`, `height`) |
| 29 | `WP_WIDGET` | `wp_widget` | `Control_WP_Widget` | WordPress core widget adapter |
| 30 | `URL` | `url` | `Control_URL` | Object (`url`, `is_external`, `nofollow`, `custom_attributes`) |
| 31 | `REPEATER` | `repeater` | `Control_Repeater` | Array of row objects (`_id`, fields) |
| 32 | `ICON` | `icon` | `Control_Icon` | FontAwesome legacy icon slug |
| 33 | `ICONS` | `icons` | `Control_Icons` | Object (`value`, `library`) |
| 34 | `GALLERY` | `gallery` | `Control_Gallery` | Array of attachment objects (`id`, `url`) |
| 35 | `STRUCTURE` | `structure` | `Control_Structure` | Legacy column layout string |
| 36 | `DATE_TIME` | `date_time` | `Control_Date_Time` | ISO Date/Time string |
| 37 | `BOX_SHADOW` | `box_shadow` | `Control_Box_Shadow` | Object (`horizontal`, `vertical`, `blur`, `spread`, `color`, `position`) |
| 38 | `TEXT_SHADOW` | `text_shadow` | `Control_Text_Shadow` | Object (`horizontal`, `vertical`, `blur`, `color`) |
| 39 | `ANIMATION` | `animation` | `Control_Animation` | Entrance animation name |
| 40 | `HOVER_ANIMATION`| `hover_animation`| `Control_Hover_Animation` | Hover animation name |
| 41 | `EXIT_ANIMATION` | `exit_animation` | `Control_Exit_Animation` | Exit animation name |
| 42 | `GAPS` | `gaps` | `Control_Gaps` | Object (`unit`, `row`, `column`, `isLinked`) |

---

## 2. Group Control Types (`Group_Control_Base`)

| # | Group Control Name | Type Slug | Source Class File | Child Controls Injected |
|---|---|---|---|---|
| 1 | Typography | `typography` | `groups/typography.php` | `typography`, `font_family`, `font_size`, `font_weight`, `text_transform`, `font_style`, `text_decoration`, `line_height`, `letter_spacing`, `word_spacing` |
| 2 | Background | `background` | `groups/background.php` | `background`, `color`, `image`, `position`, `attachment`, `repeat`, `size`, `bg_width`, `color_stop`, `color_b`, `color_b_stop`, `gradient_type`, `gradient_angle`, `video_link` |
| 3 | Border | `border` | `groups/border.php` | `border`, `width`, `color` |
| 4 | Box Shadow | `box-shadow` | `groups/box-shadow.php` | `box_shadow_type`, `box_shadow` |
| 5 | Text Shadow | `text-shadow` | `groups/text-shadow.php` | `text_shadow_type`, `text_shadow` |
| 6 | Text Stroke | `text-stroke` | `groups/text-stroke.php` | `text_stroke_type`, `stroke`, `stroke_color` |
| 7 | Image Size | `image-size` | `groups/image-size.php` | `size`, `custom_dimension` |
| 8 | CSS Filter | `css-filter` | `groups/css-filter.php` | `blur`, `brightness`, `contrast`, `saturate`, `hue` |
| 9 | Flex Container | `flex-container` | `groups/flex-container.php` | `direction`, `justify_content`, `align_items`, `wrap`, `align_content`, `gap` |
| 10 | Flex Item | `flex-item` | `groups/flex-item.php` | `basis_type`, `basis`, `align_self`, `order`, `grow`, `shrink` |
| 11 | Grid Container | `grid-container` | `groups/grid-container.php` | `grid_columns_grid`, `grid_rows_grid`, `grid_gaps` |
| 12 | Query (Pro) | `posts` / `query` | `modules/query-control/` | `post_type`, `include`, `include_term_ids`, `exclude`, `orderby`, `order`, `date` |
| 13 | Related (Pro) | `related` | `modules/query-control/` | `related_fallback`, `related_by` |
| 14 | Taxonomy (Pro) | `taxonomy` | `modules/query-control/` | `taxonomy`, `terms` |
| 15 | Motion FX (Pro) | `motion-fx` | `modules/motion-fx/` | `motion_fx_scrolling`, `vertical_scroll`, `horizontal_scroll`, `transparency`, `blur`, `rotate`, `scale`, `mouse_track`, `tilt` |
| 16 | Transform | `transform` | `modules/transform/` | `rotate`, `scale`, `skew`, `translate`, `flip` |
