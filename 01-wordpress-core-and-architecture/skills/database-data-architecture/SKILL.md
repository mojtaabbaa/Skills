---
name: database-data-architecture
description: Design, inspect, migrate, query, and optimize WordPress and WooCommerce data models, including wp_options, metadata, taxonomies, custom tables, object cache, and HPOS-safe order data. Use when a task changes persistent data, database schema, query behavior, migrations, reporting, or data integrity.
---

# Database & Data Architecture

## Mission

Own the data model and persistence layer for WordPress systems. Ensure that data is stored in the correct abstraction, remains consistent through upgrades and retries, can be queried efficiently, and can be safely migrated or rolled back. Do not select a storage mechanism because it is convenient; select it from access patterns, volume, consistency requirements, and ownership.

## Evidence and project context

The user's historical work includes custom WordPress/WooCommerce plugins and these observations:
- Ravi Design System (RDS) option names were reported as `rds_settings` and `rds_classes`.
- A database error `Commands out of sync; you can't run this command now` was reported with a reference to `usfyi_options` in one environment.
- Redis and Memcached PHP extensions were reported unavailable in at least one hosting environment.
- WooCommerce HPOS compatibility has been an explicit architectural concern.
- Product attributes discussed for perfume filtering included candidate global taxonomies such as `pa_family`, `pa_temperament`, and `pa_season`, but taxonomy names must be verified in the target site.

These are **HISTORICAL** observations. No current database schema, live database connection, table inventory, index inventory, or active option values are included in this knowledge pack. Never infer the current schema from these names.

## Storage selection decision tree

1. **WordPress-owned entity?** Use the relevant WordPress API: posts, users, terms, options, or metadata.
2. **WooCommerce-owned entity?** Use WooCommerce CRUD objects and supported APIs. For orders, use `wc_get_order()` and order/item CRUD APIs. Do not assume legacy post-table storage.
3. **Small configuration set?** Use options or the Settings API, with a versioned schema and strict validation.
4. **Data belongs to one post/user/order/product?** Use metadata only when its query patterns and data volume are suitable.
5. **Hierarchical or facetable classification?** Use a registered taxonomy when its semantics and query behavior match the domain.
6. **High-volume, relational, frequently filtered or report-heavy data?** Evaluate a custom table with explicit indexes and ownership.
7. **Derived, recomputable, short-lived data?** Consider transient/object cache, with a documented invalidation strategy.
8. **Unclear ownership or lifecycle?** Stop and map writers, readers, deletion behavior, and consistency requirements before choosing storage.

## Data modeling requirements

For every entity, document:
- Owner and lifecycle (created, updated, deleted, archived).
- Primary identity and uniqueness constraints.
- Required and optional fields.
- Canonical representation and units.
- Relationships and referential expectations.
- Read/write frequency and query shapes.
- Access-control boundary and data sensitivity.
- Retention and deletion rules.
- Migration and rollback strategy.

Prefer normalized, explicit data contracts. Denormalization is allowed when a measured read-performance need justifies it and the write/invalidation path is documented.

## WordPress storage rules

### Options
- Use options for relatively small configuration, not as a general-purpose table for large or frequently mutated records.
- Use unique, project-prefixed option names.
- Register settings with appropriate capability, sanitization, validation, and defaults.
- Decide `autoload` deliberately. Large or rarely used options should not be autoloaded without a measured reason.
- Avoid rewriting a whole serialized option for tiny high-frequency changes when that creates contention or unnecessary writes.
- Treat serialized option structures as an internal contract. Version and migrate them; do not casually edit values in SQL.

### Post, user, and term metadata
- Use metadata APIs for entity-owned attributes when their access patterns are acceptable.
- Avoid using one metadata key as an unbounded event log or relational database.
- Understand that `meta_query` can become expensive at scale. Inspect SQL and `EXPLAIN` when performance matters.
- Validate IDs and metadata ownership. A valid numeric ID is not proof that the record belongs to the expected entity or current user.
- Be explicit about duplicate metadata keys and whether multiple values are allowed.

### Taxonomies and attributes
- Verify taxonomy registration, object types, public/queryable flags, rewrite behavior, and actual term slugs.
- Distinguish WooCommerce global attributes (`pa_*`) from custom attributes and unrelated taxonomies.
- Never assume a display label is a stable identifier.
- Do not create or rename a taxonomy as a shortcut without checking existing content, filters, URLs, imports, and multilingual effects.

## Custom table design

Use a custom table only when a clear requirement exceeds core APIs. Before creating one:
- Define a unique `$wpdb->prefix`-scoped table name.
- Define a primary key, unique constraints, foreign-key expectations (WordPress deployments often cannot rely on enforced FKs), and required indexes.
- Choose field types based on actual ranges and nullability.
- Use a supported charset/collation from `$wpdb` where appropriate.
- Add indexes based on real `WHERE`, `JOIN`, `ORDER BY`, and pagination patterns; avoid indexing every column.
- Define retention, deletion, and privacy behavior.
- Include a schema version and idempotent migration path.
- Document query ownership and avoid mixing table access across unrelated modules.

Prefer `$wpdb->get_charset_collate()` and `dbDelta()` for suitable schema creation/upgrade tasks, but inspect `dbDelta()` limitations and generated SQL. It is not a complete migration engine for arbitrary constraints or data transformations.

## SQL safety and query quality

- Use `$wpdb->prepare()` for values.
- Table and column identifiers cannot be parameterized like values; select them from a strict internal allowlist and quote them safely.
- Never concatenate user-controlled values into SQL.
- Validate sorting columns and directions using allowlists.
- Use bounded pagination and avoid unbounded `SELECT *` on high-volume tables.
- Select only needed columns.
- Use `EXPLAIN` or equivalent query-plan inspection when a query is slow or scales poorly.
- Check query count and latency under realistic data volume; do not optimize based only on intuition.
- Be careful with `LIKE` searches, leading wildcards, large `IN` lists, and metadata joins.

## Migrations and upgrades

Every persistent schema or data-format change needs:
1. Current schema/version detection.
2. Backup or recoverable snapshot before production migration.
3. Idempotent migration code where possible.
4. Explicit migration steps and preconditions.
5. Batching for large datasets and resumable progress markers.
6. Locking or concurrency protection where multiple requests could run migration simultaneously.
7. Clear failure behavior and diagnostics.
8. Post-migration integrity checks.
9. Rollback strategy or a declared forward-only migration with a recovery plan.

Do not assume DDL is transactionally reversible on the target MySQL/MariaDB engine. Do not perform a large migration on every frontend request. Prefer controlled activation, upgrade routine, CLI, or an explicit admin migration action as appropriate. Never silently drop columns or delete user data during an ordinary plugin update.

## WooCommerce and HPOS

- Use `WC_Product`, `WC_Order`, `WC_Order_Item`, and documented CRUD getters/setters.
- Use `wc_get_order()` for orders and WooCommerce query APIs for order lookup where supported.
- Do not directly read/write `wp_posts` or `wp_postmeta` as the sole order store; HPOS may use dedicated order tables.
- Declare HPOS compatibility only after testing against both the supported storage modes.
- Do not write custom order metadata directly into guessed tables.
- For product data, use product CRUD methods and ensure caches are invalidated using supported mechanisms.
- Test order creation, updates, admin screens, refunds, and reporting with the configured order storage mode.

## Cache and consistency

- Cache only data whose staleness is acceptable and whose invalidation trigger is known.
- Define cache keys with plugin prefix, schema/data version, and all dimensions affecting the result.
- Invalidate on create/update/delete and relevant relationship changes.
- Avoid caching permission-dependent or customer-specific data in a shared public cache.
- Transients can be evicted at any time; code must handle a cache miss.
- Do not assume Redis or Memcached is available. Detect capabilities and provide a correct fallback.
- Avoid storing permanent source-of-truth data only in cache.

## Currency, units, and locale

- Establish whether the store stores toman or rial and identify where conversion happens.
- Store canonical numeric values; format Persian digits, separators, and currency labels at presentation boundaries.
- Avoid floating-point arithmetic for money. Use integer minor units or carefully controlled decimal arithmetic consistent with WooCommerce's precision model.
- Store unit-bearing values with explicit units (for example milliliters versus grams); do not infer units from labels.
- Normalize user input only after validating the source representation. Preserve original values when legally or operationally necessary.

## Required investigation workflow

1. Locate schema creation, update, query, and deletion code.
2. Search for option names, metadata keys, table names, and raw SQL.
3. Identify all writers and readers, including cron, AJAX, REST, admin, and import routines.
4. Map schema to current installed plugin version.
5. Check cache layers and invalidation.
6. Inspect query plans and realistic data cardinality when relevant.
7. Check privacy and capability boundaries.
8. Write migration and rollback plan before touching persistent structures.

## Acceptance tests

- Fresh install and upgrade from the previous supported schema.
- Re-running migration does not corrupt or duplicate data.
- Missing/invalid values receive safe defaults or explicit validation errors.
- Concurrent requests do not create duplicate records or race a migration.
- CRUD works through supported APIs.
- HPOS and legacy order storage are tested if both are supported.
- Cache miss, eviction, and invalidation work.
- Query plans and timings are acceptable at representative volume.
- Backup restoration or rollback path is understood.

## Anti-patterns

- Direct SQL edits to plugin options without understanding serialization and ownership.
- Using `postmeta` as a high-volume relational/event store by default.
- Assuming HPOS stores orders in `wp_posts`.
- Assuming Redis/Memcached is installed because a hosting panel advertises it.
- Running schema migrations on every request.
- Unbounded queries and unindexed high-cardinality lookups.
- Storing localized display strings as canonical numeric values.
- Dropping or overwriting data without a migration plan.
