# Dynamic Content & Custom Taxonomy Architecture

## 1. Dynamic Content Infrastructure
Dynamic Content in Elementor replaces static hardcoded values with real-time data fetched from WordPress core, registered Custom Post Types (CPTs), custom taxonomies, user sessions, or HTTP request parameters.

---

## 2. Custom Post Types (CPT) Integration
Elementor treats all public custom post types registered via `register_post_type()` as first-class citizens:
- In Elementor Settings (**Elementor → Settings → General**): Any CPT can be enabled for editing.
- In Theme Builder: Single Post templates can target specific CPTs (e.g. `Single Portfolio`, `Single Event`, `Single Service`).
- In Loop Builder: `Group_Control_Query` allows selecting any registered CPT as the post source for the Loop Grid.

---

## 3. Dynamic Query Modeling (`Group_Control_Query`)
When configuring dynamic listings in the `posts` or `loop-grid` widget:

```json
{
  "_query_post_type": "event",
  "query_include": ["terms"],
  "query_include_term_ids": [105, 108],
  "query_exclude": ["current_post"],
  "query_orderby": "meta_value_num",
  "query_meta_key": "event_timestamp",
  "query_order": "asc"
}
```

### Supported Query Filters:
- **Taxonomy Queries**: Filter by category, tag, or custom taxonomy slugs (`product_cat`, `event_category`).
- **Author Queries**: Filter by specific user IDs or exclude current author.
- **Date Queries**: Past day, past week, past month, past year, or custom date ranges.
- **Exclusions**: Exclude current post (prevents self-referencing in related articles), manual post IDs, or sticky posts.
- **Query ID**: Allows external developers to hook into the query via the `elementor/query/{$query_id}` action hook for custom SQL clauses or complex joins.

---

## 4. Request Parameters & Query Strings
The `request-parameter` dynamic tag enables personalization based on URL GET/POST parameters:
- Tag Name: `request-parameter`
- Settings:
  ```json
  "__dynamic__": {
    "title": "[elementor-tag id=\"req_01\" name=\"request-parameter\" settings=\"%7B%22parameter_type%22%3A%22get%22%2C%22param_name%22%3A%22utm_source%22%2C%22fallback%22%3A%22Partner%22%7D\"]"
  }
  ```
- **Use Case**: Dynamic landing page headlines: `"Welcome, [utm_campaign] Visitor!"`.
