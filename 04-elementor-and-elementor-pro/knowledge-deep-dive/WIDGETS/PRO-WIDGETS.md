# Elementor Pro Widget Catalog (95 Widgets Across 25 Modules)

## 1. Posts, Queries & Portfolios (`modules/posts/`)

### 1. Posts (`posts`)
- **Class**: `\ElementorPro\Modules\Posts\Widgets\Posts`
- **Category**: `pro-elements`
- **Skins**: `classic`, `cards`, `custom`
- **Key Controls**:
  - `posts_per_page` (number), `columns` (responsive: 1-6)
  - `query` (`Group_Control_Posts` / `Group_Control_Query`): post types, tax queries, author, date, ordering, exclude current post.
  - Cards Skin: Badge taxonomy, avatar, reading time, card border-radius, box-shadow.
  - Pagination: numbers, prev/next, load more on click, infinite scroll.

### 2. Portfolio (`portfolio`)
- **Class**: `\ElementorPro\Modules\Posts\Widgets\Portfolio`
- **Category**: `pro-elements`
- **Key Controls**: Filter bar by taxonomy, masonry layout, item overlay with title and tags.

---

## 2. Forms & User Management (`modules/forms/`)

### 3. Form (`form`)
- **Class**: `\ElementorPro\Modules\Forms\Widgets\Form`
- **Category**: `pro-elements`
- **Key Controls**:
  - `form_fields` (repeater): `field_type`, `field_label`, `placeholder`, `required`, `column_width` (responsive: 20%, 25%, 33%, 50%, 66%, 75%, 100%), `field_value`.
  - Multi-Step: `step` field type with step indicators (number, icon, progress bar).
  - Actions After Submit: `email`, `email2`, `redirect`, `webhook`, `mailchimp`, `slack`, `discord`.
  - Style: Row gap, column gap, field typography/background/border/radius, button styling, error/success message typography and colors.
- **Zero-CSS Capability**: Eliminates custom CSS for form grids, multi-column inputs, step transitions, focus states, and validation message styling.

### 4. Login (`login`)
- **Class**: `\ElementorPro\Modules\Forms\Widgets\Login`
- **Category**: `pro-elements`
- **Key Controls**: Username/password labels, remember me checkbox, logged-in message, redirect after login/logout, lost password link, register link.

---

## 3. Menus & Navigation (`modules/nav-menu/`, `modules/mega-menu/`, `modules/search/`, `modules/off-canvas/`)

### 5. Nav Menu (`nav-menu`)
- **Class**: `\ElementorPro\Modules\NavMenu\Widgets\Nav_Menu`
- **Category**: `pro-elements`
- **Key Controls**:
  - `menu` (select: WP Menus), `layout` (horizontal, vertical, dropdown)
  - `pointer` (underline, overline, double line, framed, background, text)
  - `animation` (fade, slide, grow, drop-in)
  - Mobile Dropdown: breakpoint (`mobile`, `tablet`, `none`), full-width toggle, animated hamburger.

### 6. Mega Menu (`mega-menu`)
- **Class**: `\ElementorPro\Modules\MegaMenu\Widgets\Mega_Menu`
- **Category**: `pro-elements`
- **Key Controls**: Container-based mega menu. Each dropdown item opens an editable **Elementor Container** capable of hosting multi-column links, banners, product cards, and forms.

### 7. Search (`search`)
- **Class**: `\ElementorPro\Modules\Search\Widgets\Search`
- **Category**: `pro-elements`
- **Key Controls**: Live search with instant AJAX dropdown results, search post types, thumbnail display, excerpt preview.

### 8. Off-Canvas (`off-canvas`)
- **Class**: `\ElementorPro\Modules\OffCanvas\Widgets\Off_Canvas`
- **Category**: `pro-elements`
- **Key Controls**: Slide-out drawer or overlay triggered by button or selector. Hosts an Elementor container layout.

---

## 4. Sliders, Carousels & Media (`modules/slides/`, `modules/carousel/`, `modules/nested-carousel/`, `modules/video-playlist/`, `modules/lottie/`)

### 9. Slides (`slides`)
- **Class**: `\ElementorPro\Modules\Slides\Widgets\Slides`
- **Category**: `pro-elements`
- **Key Controls**: Hero banner slider with background image, title, description, CTA button, animated Ken Burns effect, transition effects (fade, slide).

### 10. Media Carousel (`media-carousel`)
- **Class**: `\ElementorPro\Modules\Carousel\Widgets\Media_Carousel`
- **Category**: `pro-elements`
- **Key Controls**: Effect (slide, fade, cube, coverflow), image or video slides, lightbox overlay.

### 11. Testimonial Carousel & Reviews (`testimonial-carousel`, `reviews`)
- **Classes**: `\ElementorPro\Modules\Carousel\Widgets\Testimonial_Carousel`, `\ElementorPro\Modules\Carousel\Widgets\Reviews`
- **Category**: `pro-elements`
- **Key Controls**: Skin (default, bubble), reviewer image, name, title, star rating, icon badge.

### 12. Nested Carousel (`nested-carousel`)
- **Class**: `\ElementorPro\Modules\NestedCarousel\Widgets\Nested_Carousel`
- **Category**: `pro-elements`
- **Key Controls**: Container-based Swiper slider. Every slide is an isolated Elementor Container.

### 13. Video Playlist (`video-playlist`)
- **Class**: `\ElementorPro\Modules\VideoPlaylist\Widgets\Video_Playlist`
- **Category**: `pro-elements`
- **Key Controls**: YouTube or self-hosted video playlist with collateral sidebar tabs and watch indicators.

### 14. Lottie (`lottie`)
- **Class**: `\ElementorPro\Modules\Lottie\Widgets\Lottie`
- **Category**: `pro-elements`
- **Key Controls**: Lottie JSON animation URL or file, trigger (viewport, click, hover, scroll), loop, speed, reverse.

---

## 5. Interactive & Marketing Widgets

### 15. Hotspot (`hotspot`)
- **Class**: `\ElementorPro\Modules\Hotspot\Widgets\Hotspot`
- **Key Controls**: Image with multiple pinpoint hotspots, animated glow pulse, tooltip content, link.

### 16. Price List & Price Table (`price-list`, `price-table`)
- **Classes**: `\ElementorPro\Modules\Pricing\Widgets\Price_List`, `\ElementorPro\Modules\Pricing\Widgets\Price_Table`
- **Key Controls**: Features list, pricing currency, period, ribbon badge, CTA button, highlighted feature items.

### 17. Flip Box (`flip-box`)
- **Class**: `\ElementorPro\Modules\FlipBox\Widgets\Flip_Box`
- **Key Controls**: Front & back card faces, 3D flip animation (flip, slide, push, zoom, fade), icon, title, description, button.

### 18. Call to Action (`call-to-action`)
- **Class**: `\ElementorPro\Modules\CallToAction\Widgets\Call_To_Action`
- **Key Controls**: Image card with ribbon badge, title, description, button, hover zoom, and color overlays.

### 19. Table of Contents (`table-of-contents`)
- **Class**: `\ElementorPro\Modules\TableOfContents\Widgets\Table_Of_Contents`
- **Key Controls**: Automatic extraction of page headings (H2-H6), exclude selectors, hierarchical indentation, minimize toggle, smooth scroll.

### 20. Countdown (`countdown`)
- **Class**: `\ElementorPro\Modules\Countdown\Widgets\Countdown`
- **Key Controls**: Due date (fixed target) or Evergreen (timer reset per user session), days/hours/minutes/seconds blocks, action on expire (hide, redirect, message).

### 21. Animated Headline (`animated-headline`)
- **Class**: `\ElementorPro\Modules\AnimatedHeadline\Widgets\Animated_Headline`
- **Key Controls**: Style: Highlighted (SVG circle, underline, curly, zigzag) or Rotating (typing, clip, flip, swirl, wave).

### 22. Code Highlight (`code-highlight`)
- **Class**: `\ElementorPro\Modules\CodeHighlight\Widgets\Code_Highlight`
- **Key Controls**: Prism.js syntax highlighter, language selection, theme (dark, prism, okaidia, solarized), line numbers, copy-to-clipboard button.

### 23. Progress Tracker (`progress-tracker`)
- **Class**: `\ElementorPro\Modules\ProgressTracker\Widgets\Progress_Tracker`
- **Key Controls**: Reading scroll progress indicator (horizontal bar or circular), tracker percentage.

### 24. Payments: PayPal Button & Stripe Button (`paypal-button`, `stripe-button`)
- **Classes**: `\ElementorPro\Modules\Payments\Widgets\Paypal_Button`, `\ElementorPro\Modules\Payments\Widgets\Stripe_Button`
- **Key Controls**: Checkout type (product, donation, subscription), currency, price, billing address capture, success/cancel redirects.

---

## 6. Loop Builder Widgets (`modules/loop-builder/`, `modules/loop-filter/`)

### 25. Loop Grid (`loop-grid`)
- **Class**: `\ElementorPro\Modules\LoopBuilder\Widgets\Loop_Grid`
- **Category**: `loop-builder`
- **Key Controls**:
  - `template_id`: The ID of the `elementor_library` template (type: `loop`).
  - `query`: Dynamic `WP_Query` builder (Post types, Taxonomies, Date, Author, Exclusions).
  - `columns` (responsive: 1-6), `posts_per_page`.
  - `alternate_template`: Injects a secondary template at specified positions (e.g. ad banners or large cards).
  - Pagination: Numbers, Prev/Next, Infinite Scroll, Load More Button.

### 26. Loop Carousel (`loop-carousel`)
- **Class**: `\ElementorPro\Modules\LoopBuilder\Widgets\Loop_Carousel`
- **Category**: `loop-builder`
- **Key Controls**: Swiper carousel cycling through loop template items.

### 27. Taxonomy Filter (`taxonomy-filter`)
- **Class**: `\ElementorPro\Modules\LoopFilter\Widgets\Taxonomy_Filter`
- **Category**: `loop-builder`
- **Key Controls**: AJAX filter pills connected to a target Loop Grid. Supports single/multiple selection without page reloads.

---

## 7. Theme Builder Widgets (`modules/theme-builder/`, `modules/theme-elements/`)
- `post-title`: Dynamic H1-H6 title of queried post.
- `post-excerpt`: Dynamic excerpt text.
- `post-content`: Embeds full post content in Single templates.
- `post-featured-image`: Dynamic post featured image.
- `author-box`: Author gravatar, display name, biography, and archive button.
- `post-comments`: Native WordPress comment stream and reply form.
- `post-info`: Meta list (Author, Date, Time, Comments count, Taxonomy terms) with custom icons.
- `post-navigation`: Prev/Next post links with post title and arrows.
- `archive-title`: Dynamic archive title (Category: X, Tag: Y, Author: Z).
- `archive-posts`: Native archive query loop with pagination.
- `site-logo`: Customizer logo linked to home.
- `site-title`: Site title with home link.
- `breadcrumbs`: Integrates Rank Math or Yoast breadcrumbs.
- `search-form`: Search input form.
- `sitemap`: Visual hierarchical sitemap.

---

## 8. WooCommerce Builder Widgets (`modules/woocommerce/`)
- `woocommerce-products`: Catalog grid with orderby, categories, sale filters.
- `woocommerce-archive-products`: Main shop archive loop.
- `woocommerce-product-title`: Product H1 title.
- `woocommerce-product-images`: Product gallery with zoom lens and thumbnails slider.
- `woocommerce-product-price`: Regular and sale price formatted with currency symbol.
- `woocommerce-product-add-to-cart`: Quantity input and AJAX add-to-cart button.
- `woocommerce-product-rating`: Star reviews and review anchor link.
- `woocommerce-product-stock`: Stock availability badge.
- `woocommerce-product-meta`: SKU, category pills, tag pills.
- `woocommerce-product-content`: Full product description.
- `woocommerce-product-short-description`: Product summary excerpt.
- `woocommerce-product-data-tabs`: Native WooCommerce tabs (Description, Attributes, Reviews).
- `woocommerce-product-additional-information`: Technical attributes table.
- `woocommerce-product-related`: Related products slider/grid.
- `woocommerce-product-upsell`: Upsell products grid.
- `woocommerce-menu-cart`: Header cart counter and slide-out mini cart drawer.
- `woocommerce-cart`: 2-column visual Cart page.
- `woocommerce-checkout`: 2-column visual Checkout page with gateway selection.
- `woocommerce-my-account`: Account portal.
- `woocommerce-purchase-summary`: Order received / thank you page.
- `woocommerce-notices`: Floating/inline WooCommerce notices container.
