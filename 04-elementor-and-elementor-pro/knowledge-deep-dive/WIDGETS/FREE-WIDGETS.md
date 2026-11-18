# Elementor Free Widget Catalog (38 Widgets)

## 1. Core Built-In Free Widgets

### 1. Heading (`heading`)
- **Class**: `\Elementor\Widget_Heading` (`includes/widgets/heading.php`)
- **Category**: `basic`
- **Key Controls**:
  - `title` (text, dynamic-enabled)
  - `link` (url, dynamic-enabled)
  - `size` (select: `default`, `small`, `medium`, `large`, `xl`, `xxl`)
  - `header_size` (select: `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `div`, `span`, `p`)
  - `align` (choose, responsive: `left`, `center`, `right`, `justify`)
  - Style: `title_color` (color, global-enabled), `typography` (group-typography), `text_stroke` (group-text-stroke), `text_shadow` (group-text-shadow), `blend_mode` (select)
- **Responsive Controls**: `align`, `align_tablet`, `align_mobile`, typography size/line-height.
- **Zero-CSS Capability**: Eliminates custom CSS for responsive typography scaling, line heights, letter-spacing, text stroke, and shadows.

### 2. Image (`image`)
- **Class**: `\Elementor\Widget_Image` (`includes/widgets/image.php`)
- **Category**: `basic`
- **Key Controls**:
  - `image` (media: attachment id and url, dynamic-enabled)
  - `image_size` (group-image-size: thumbnail, medium, large, full, custom)
  - `align` (choose, responsive: left, center, right)
  - `caption_source` (select: none, attachment, custom)
  - `link_to` (select: none, file, custom)
  - Style: `width` (slider, responsive: px, %, vw), `max_width` (slider, responsive), `height` (slider, responsive), `object_fit` (select: fill, cover, contain), `border_radius` (dimensions, responsive), `box_shadow` (group-box-shadow), `css_filters` (group-css-filter), hover opacity and transitions.
- **Zero-CSS Capability**: Eliminates custom CSS for responsive image widths, aspect ratios, object-fit cropping, hover zoom, and border radiuses.

### 3. Text Editor (`text-editor`)
- **Class**: `\Elementor\Widget_Text_Editor` (`includes/widgets/text-editor.php`)
- **Category**: `basic`
- **Key Controls**:
  - `editor` (wysiwyg, dynamic-enabled)
  - `drop_cap` (switcher: creates typographic drop-cap on first letter)
  - `align` (choose, responsive: left, center, right, justify)
  - `text_columns` (select, responsive: 1, 2, 3, 4, 5, 6 columns)
  - `column_gap` (slider, responsive: px, em)
  - Style: `text_color` (color, global-enabled), `typography` (group-typography).
- **Rule of Engagement**: Must ONLY be used for paragraphs and rich editorial copy. MUST NEVER be used as a container to inject raw HTML cards, buttons, or layouts.

### 4. Button (`button`)
- **Class**: `\Elementor\Widget_Button` (`includes/widgets/button.php`)
- **Category**: `basic`
- **Key Controls**:
  - `button_type` (select: default, info, success, warning, danger)
  - `text` (text, dynamic-enabled)
  - `link` (url, dynamic-enabled)
  - `size` (select: xs, sm, md, lg, xl)
  - `selected_icon` (icons, fontawesome or custom SVG)
  - `icon_align` (choose: row, row-reverse)
  - `icon_indent` (slider: spacing between icon and text)
  - Style: `typography` (group-typography), `text_color` / `button_background_color` (normal & hover), `border_border` (border type), `border_radius` (dimensions, responsive), `button_box_shadow` (group-box-shadow), `hover_animation` (grow, shrink, pulse, bob, etc.).
- **Zero-CSS Capability**: Completely replaces custom CSS buttons, hover state color shifts, transitions, icon positioning, and pill border radiuses.

### 5. Video (`video`)
- **Class**: `\Elementor\Widget_Video` (`includes/widgets/video.php`)
- **Category**: `basic`
- **Key Controls**:
  - `video_type` (select: youtube, vimeo, dailymotion, hosted)
  - `youtube_url` / `hosted_url` (text, dynamic-enabled)
  - `autoplay`, `mute`, `loop`, `controls`, `modestbranding`
  - `aspect_ratio` (select: 1:1, 3:2, 4:3, 9:16, 16:9, 21:9)
  - `show_image_overlay` (switcher with custom play icon and lazy loading).

### 6. Divider (`divider`)
- **Class**: `\Elementor\Widget_Divider` (`includes/widgets/divider.php`)
- **Category**: `basic`
- **Key Controls**:
  - `style` (select: solid, double, dotted, dashed, curved, zigzag, slashes, wavy, etc.)
  - `weight` (slider: px), `width` (slider, responsive: % or px), `alignment` (choose, responsive)
  - `add_element` (select: none, text, icon).

### 7. Spacer (`spacer`)
- **Class**: `\Elementor\Widget_Spacer` (`includes/widgets/spacer.php`)
- **Category**: `basic`
- **Key Controls**:
  - `space` (slider, responsive: px, vh, em).
- **Rule of Engagement**: Use container padding and gaps (`gap`) as primary layout spacing. Use Spacer only for deliberate empty vertical offsets.

### 8. Google Maps (`google-maps`)
- **Class**: `\Elementor\Widget_Google_Maps` (`includes/widgets/google-maps.php`)
- **Category**: `basic`
- **Key Controls**:
  - `address` (text, dynamic-enabled), `zoom` (slider: 1 to 20), `height` (slider, responsive: px).

### 9. Icon (`icon`)
- **Class**: `\Elementor\Widget_Icon` (`includes/widgets/icon.php`)
- **Category**: `basic`
- **Key Controls**:
  - `selected_icon` (icons), `view` (default, stacked, framed), `shape` (circle, square), `link` (url)
  - Style: `size` (slider, responsive), `padding` (slider), `rotate` (slider), `border_width`, `border_radius`.

### 10. Icon Box (`icon-box`)
- **Class**: `\Elementor\Widget_Icon_Box` (`includes/widgets/icon-box.php`)
- **Category**: `general`
- **Key Controls**:
  - `selected_icon`, `title_text`, `description_text`, `position` (choose, responsive: left, top, right)
  - Style: Icon spacing, color, hover animation, Title typography/color, Description typography/color.

### 11. Image Box (`image-box`)
- **Class**: `\Elementor\Widget_Image_Box` (`includes/widgets/image-box.php`)
- **Category**: `general`
- **Key Controls**:
  - `image`, `title_text`, `description_text`, `position` (choose, responsive: left, top, right).

### 12. Star Rating & Rating (`star-rating`, `rating`)
- **Classes**: `\Elementor\Widget_Star_Rating`, `\Elementor\Widget_Rating`
- **Category**: `general`
- **Key Controls**: `rating_scale` (0-5 or 0-10), `rating` (number, dynamic-enabled), `icon` (star, heart), `title` (text).

### 13. Image Carousel (`image-carousel`)
- **Class**: `\Elementor\Widget_Image_Carousel` (`includes/widgets/image-carousel.php`)
- **Category**: `general`
- **Key Controls**:
  - `carousel` (gallery), `slides_to_show` (select, responsive: 1 to 10), `slides_to_scroll` (select, responsive)
  - `navigation` (arrows, dots, both, none), `autoplay`, `pause_on_hover`, `infinite`.

### 14. Basic Gallery (`image-gallery`)
- **Class**: `\Elementor\Widget_Image_Gallery` (`includes/widgets/image-gallery.php`)
- **Category**: `general`
- **Key Controls**:
  - `wp_gallery` (gallery), `gallery_columns` (select, responsive: 1 to 10), `gap` (slider, responsive).

### 15. Icon List (`icon-list`)
- **Class**: `\Elementor\Widget_Icon_List` (`includes/widgets/icon-list.php`)
- **Category**: `general`
- **Key Controls**:
  - `icon_list` (repeater: `text`, `selected_icon`, `link`)
  - `view` (choose, responsive: traditional vertical or inline horizontal)
  - Style: Space between items, icon color/size, text typography/color.

### 16. Counter (`counter`)
- **Class**: `\Elementor\Widget_Counter` (`includes/widgets/counter.php`)
- **Category**: `general`
- **Key Controls**:
  - `starting_number` (number), `ending_number` (number), `prefix` (text), `suffix` (text), `duration` (number in ms), `title` (text).

### 17. Progress Bar (`progress`)
- **Class**: `\Elementor\Widget_Progress` (`includes/widgets/progress.php`)
- **Category**: `general`
- **Key Controls**:
  - `title` (text), `percent` (slider: 0 to 100), `inner_text` (text), `progress_type` (primary, success, warning, danger).

### 18. Testimonial (`testimonial`)
- **Class**: `\Elementor\Widget_Testimonial` (`includes/widgets/testimonial.php`)
- **Category**: `general`
- **Key Controls**:
  - `testimonial_content` (textarea), `testimonial_image` (media), `testimonial_name` (text), `testimonial_job` (text), `image_position` (choose: top, aside, left, right).

### 19. Tabs (`tabs`)
- **Class**: `\Elementor\Widget_Tabs` (`includes/widgets/tabs.php`)
- **Category**: `general`
- **Key Controls**:
  - `tabs` (repeater: `tab_title`, `tab_content`), `type` (horizontal, vertical).

### 20. Accordion & Toggle (`accordion`, `toggle`)
- **Classes**: `\Elementor\Widget_Accordion`, `\Elementor\Widget_Toggle`
- **Category**: `general`
- **Key Controls**:
  - `tabs` (repeater: `tab_title`, `tab_content`), `selected_icon`, `selected_active_icon`.
  - Accordion enforces a single open item; Toggle allows multiple simultaneous open items.

### 21. Social Icons (`social-icons`)
- **Class**: `\Elementor\Widget_Social_Icons` (`includes/widgets/social-icons.php`)
- **Category**: `general`
- **Key Controls**:
  - `social_icon_list` (repeater: `social_icon`, `link`), `shape` (rounded, square, circle), `color` (official or custom).

### 22. Alert (`alert`)
- **Class**: `\Elementor\Widget_Alert` (`includes/widgets/alert.php`)
- **Category**: `general`
- **Key Controls**:
  - `alert_type` (info, success, warning, danger), `alert_title`, `alert_description`, `show_dismiss`.

### 23. Audio / SoundCloud (`audio`)
- **Class**: `\Elementor\Widget_Audio` (`includes/widgets/audio.php`)
- **Category**: `general`
- **Key Controls**: `link` (SoundCloud URL), `visual` (artwork view), `auto_play`, `buy_button`.

### 24. Shortcode (`shortcode`)
- **Class**: `\Elementor\Widget_Shortcode` (`includes/widgets/shortcode.php`)
- **Category**: `general`
- **Key Controls**: `shortcode` (text, executes native WordPress shortcode).

### 25. HTML (`html`)
- **Class**: `\Elementor\Widget_Html` (`includes/widgets/html.php`)
- **Category**: `general`
- **Key Controls**: `html` (code).
- **Rule of Engagement**: Strictly restricted. Only permitted for third-party embeds (e.g. Google Analytics snippet, Calendly embed) when authorized. NEVER to be used to build buttons, text cards, or layouts.

### 26. Menu Anchor (`menu-anchor`)
- **Class**: `\Elementor\Widget_Menu_Anchor` (`includes/widgets/menu-anchor.php`)
- **Category**: `general`
- **Key Controls**: `anchor` (string ID for URL hash linking, e.g. `#contact`).

### 27. Sidebar (`sidebar`)
- **Class**: `\Elementor\Widget_Sidebar` (`includes/widgets/sidebar.php`)
- **Category**: `general`
- **Key Controls**: `sidebar` (select: registered WordPress widget sidebars).

### 28. Read More (`read-more`)
- **Class**: `\Elementor\Widget_Read_More` (`includes/widgets/read-more.php`)
- **Category**: `general`
- **Key Controls**: Cuts off blog post content for archive summaries.

---

## 2. Modern Container-Based Free Module Widgets

### 29. Nested Tabs (`nested-tabs`)
- **Class**: `\Elementor\Modules\NestedTabs\Widgets\NestedTabs` (`modules/nested-tabs/widgets/nested-tabs.php`)
- **Category**: `layout`
- **Key Architecture**: Each tab content area is an actual **Elementor Container** (`elType: "container"`). Any widget (Image, Form, Video, Heading, Inner Container) can be placed directly inside each tab.
- **Key Controls**: `tabs` (repeater), tab orientation, responsive layout (switches from horizontal tabs to accordion on mobile).

### 30. Nested Accordion (`nested-accordion`)
- **Class**: `\Elementor\Modules\NestedAccordion\Widgets\NestedAccordion` (`modules/nested-accordion/widgets/nested-accordion.php`)
- **Category**: `layout`
- **Key Architecture**: Each accordion item's body is an actual **Elementor Container**.

### 31. Text Path (`text-path`)
- **Class**: `\Elementor\Modules\Shapes\Widgets\TextPath` (`modules/shapes/widgets/text-path.php`)
- **Category**: `general`
- **Key Controls**: `text`, `path` (wave, arc, circle, oval, spiral, or custom SVG), `align`, `typography`, `text_color`.

### 32. Contact Buttons (`contact-buttons`)
- **Class**: `\Elementor\Modules\FloatingButtons\Widgets\Contact_Buttons`
- **Category**: `general`
- **Key Controls**: Floating bottom corner chat/call actions (WhatsApp, Phone, Email, Messenger).

### 33. Floating Bars (`floating-bars-var-1`)
- **Class**: `\Elementor\Modules\FloatingButtons\Widgets\Floating_Bars_Var_1`
- **Category**: `general`
- **Key Controls**: Fixed sticky announcement/coupon bar at top or bottom of viewport.

### 34. Link In Bio (`link-in-bio`)
- **Class**: `\Elementor\Modules\LinkInBio\Widgets\Link_In_Bio`
- **Category**: `general`
- **Key Controls**: Mobile-first social profile card with links, avatar, bio, and social icons.

### 35. Component Instance (`component-instance`)
- **Class**: `\Elementor\Modules\Components\Widgets\Component_Instance`
- **Category**: `components`
- **Key Controls**: Renders a reusable atomic component with customizable overridable properties.
