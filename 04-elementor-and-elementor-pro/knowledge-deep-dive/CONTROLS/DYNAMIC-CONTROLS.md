# Dynamic Controls & Dynamic Tags Engine

## 1. Dynamic Tags Architecture
Elementor's Dynamic Tags framework (`\Elementor\Core\DynamicTags\Manager`) provides runtime data binding, connecting widget controls directly to WordPress database values, custom fields, and WooCommerce properties.

### The Dynamic Setting Key
When an element uses dynamic tags, the base setting value serves as a static fallback, while the active binding is recorded in the `__dynamic__` key:
```json
{
  "settings": {
    "title": "Fallback Heading Title",
    "__dynamic__": {
      "title": "[elementor-tag id=\"d9a8c71\" name=\"post-title\" settings=\"%7B%7D\"]"
    }
  }
}
```

---

## 2. Dynamic Tag Shortcode Syntax
The tag string follows the contract:
`[elementor-tag id="{id}" name="{tag_name}" settings="{url_encoded_json_settings}"]`

- `id`: Unique 7-character hexadecimal string.
- `name`: The registered slug of the dynamic tag.
- `settings`: URL-encoded JSON object holding tag parameters.

### Tag Parameter Capabilities:
Most text-based dynamic tags accept formatting arguments:
- `before`: Text prepended before the dynamic value (e.g. `"By: "`).
- `after`: Text appended after the dynamic value (e.g. `" min read"`).
- `fallback`: Custom text displayed if the dynamic value is empty or not found.

Example with URL-encoded settings (`{"before":"Last Updated: ","fallback":"Recently"}`):
```json
"__dynamic__": {
  "title": "[elementor-tag id=\"4b2e1f9\" name=\"post-date\" settings=\"%7B%22before%22%3A%22Last%20Updated%3A%20%22%2C%22fallback%22%3A%22Recently%22%7D\"]"
}
```

---

## 3. Discovered Dynamic Tags Catalog

### A. WordPress Post & Page Tags
- `post-title`: Post/Page Title (`get_the_title()`).
- `post-excerpt`: Post Excerpt (`get_the_excerpt()`).
- `post-date`: Publish or modified date with customizable format string.
- `post-time`: Publish or modified time.
- `post-id`: Numeric Post ID.
- `post-url`: Permalink URL (`get_permalink()`).
- `post-custom-field`: Retrieves any custom field from `wp_postmeta` by `custom_key`.
- `post-featured-image`: Attachment object of the post thumbnail.
- `post-gallery`: Post gallery attachments.
- `post-terms`: Comma-separated list of terms from any taxonomy (`category`, `post_tag`, custom).

### B. WordPress Author & User Tags
- `author-name`: Display name of the post author.
- `author-info`: Author biographical information (Bio).
- `author-profile-picture`: Author Gravatar image.
- `author-url`: URL to author's archive page.
- `user-info`: Current logged-in user property (Username, Display Name, Email, First Name, ID).
- `user-profile-picture`: Current logged-in user avatar.

### C. Site Identity & URL Tags
- `site-title`: Blog name from `get_bloginfo('name')`.
- `site-tagline`: Blog tagline from `get_bloginfo('description')`.
- `site-logo`: Customizer site logo attachment.
- `site-url`: Home URL (`home_url()`).
- `page-title`: Title of the current page.

### D. WooCommerce Product Tags (`modules/woocommerce/tags/`)
- `product-title`: Product title.
- `product-price`: Formatted product price (regular, sale, or range).
- `product-rating`: Numeric review rating or star count.
- `product-sale`: Sale badge text or percentage discount.
- `product-short-description`: Product summary excerpt.
- `product-sku`: Product SKU code.
- `product-stock`: Stock quantity and availability status.
- `product-terms`: Product categories, tags, or custom WooCommerce attributes.
- `product-image`: Main product image.
- `product-gallery`: Product gallery attachments.
- `woocommerce-add-to-cart`: Dynamic add to cart URL for simple/variable products.

### E. Advanced Custom Fields (ACF) Tags (`modules/dynamic-tags/acf/`)
- `acf-text`: Text, textarea, or select field.
- `acf-image`: Image field (returns image attachment object).
- `acf-url`: Link or page link field.
- `acf-number`: Number or range field.
- `acf-date-time`: Date picker, date time, or time picker field.
- `acf-file`: File upload field URL.
- `acf-gallery`: ACF Gallery field.
- `acf-color`: ACF Color picker value.
