# Historical Database and Data Observations

Evidence class: HISTORICAL unless explicitly reverified in the current repository/environment.

## RDS option storage

The Ravi Design System project was described as using WordPress options:
- `rds_settings`
- `rds_classes`

A CSS generation method `build_css()` and a generated file `ravi-design-system/design-system.css` were also mentioned. This does not establish the current option schema, serialized keys, autoload flags, or write lifecycle. Inspect the plugin source and current database before changing them.

## Database synchronization error

A prior log reported:
`Commands out of sync; you can't run this command now`
with a reference to `usfyi_options`.

Do not assume the option itself caused the error. The message can arise from how the database client/result sets are handled, nested queries, or an extension/library interaction. Investigate the full stack trace, exact query sequence, database driver, plugin callback, and reproduction path. Avoid “fixes” that delete the option or increase resources without evidence.

## Object cache availability

Redis and Memcached PHP extensions were reported unavailable in at least one environment. Verify `extension_loaded()`, WordPress object-cache drop-in status, and actual backend connectivity in the target environment. A configured service in a hosting panel is not proof that PHP can use it.

## Taxonomy and attribute candidates

Historical filtering discussions included:
- `pa_family`
- `pa_temperament`
- `pa_season`
- `product_cat`
- `product_brand`
- `pa_weight`

These are candidates observed in a project discussion, not a universal schema. Query actual registered taxonomies and product attribute definitions before using them.

## HPOS

HPOS was explicitly discussed as a compatibility requirement. No current HPOS setting or compatibility test result is included here. Inspect WooCommerce settings and test with the actual order storage mode.

## Current unknowns

No live database dump, schema export, index listing, current option values, or current migration source was available when this knowledge pack was assembled.
