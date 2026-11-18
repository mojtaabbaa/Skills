# Regression Testing & Safe Editing Protocol

## 1. Regression Risk in Elementor Document Editing
When editing an existing Elementor page, sloppy edits or raw database updates can cause:
1. **Layout Corruption**: Unintended deletion of closing tags or broken container hierarchies.
2. **Loss of Widget Settings**: Overwriting an entire `settings` object instead of modifying specific target keys.
3. **Broken Revisions**: Directly altering `_elementor_data` without updating the WordPress post revision history or invalidating the CSS cache (`_elementor_css`).
4. **ID Collisions**: Copying element trees with duplicate `id` values, causing editor selection glitches and CSS rule conflicts.

---

## 2. Safe Editing Checklist

Before committing any modification to an existing Elementor page:

- [ ] **Step 1: Read Complete Layout**: Call `wp_get_page_layout` with `depth: 8` and `include_settings: true`.
- [ ] **Step 2: Map Element Hierarchy**: Identify the exact element address (`id`) of the target widget or container.
- [ ] **Step 3: Capture Version Token**: Store the current `version` string from `wp_get_page_layout` to ensure optimistic concurrency locking.
- [ ] **Step 4: Formulate Atomic Operations**: Use `wp_update_page_layout` with targeted ops (`set_text`, `set_link`, `set_fields`, `insert`, `remove`).
- [ ] **Step 5: Execute with Dry Run First**: For complex structural mutations, run `dry_run: true` to confirm syntax validity before applying changes.
- [ ] **Step 6: Verify Concurrency & Revisions**: Confirm that `changed: true`, `saved: true`, and a valid `revision_id` are returned.
- [ ] **Step 7: Re-Inspect Layout**: Call `wp_get_page_layout` immediately after editing to verify that surrounding elements remain intact.
