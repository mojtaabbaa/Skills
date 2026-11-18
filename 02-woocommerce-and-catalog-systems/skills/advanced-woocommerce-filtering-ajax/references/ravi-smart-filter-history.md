# Ravi Smart Filter — Project Knowledge

## Scope

A custom WooCommerce filter plugin intended for WoodMart compatibility. The user has emphasized performance, direct behavior, and accurate configuration rather than adding redundant layers.

## Baseline and tooling

- Version `0.4.52` was identified as a baseline in a project discussion.
- Graphify was preferred as an architecture-navigation workflow if a Graphify-generated graph is available.
- Expected Graphify workflow: query the graph first for architecture/impact analysis; distinguish EXTRACTED edges from INFERRED edges; verify important findings in source code.
- Graphify CLI was not installed or run in the referenced environment because DNS/network access to PyPI failed. Do not claim Graphify analysis has been completed.

## Observed theme interaction

The user enabled WoodMart AJAX Spy and inspected an AJAX filter URL resembling:
`/shop/?filter_category=women,men&_pjax=.wd-page-content`

This demonstrates an observed request shape during debugging only. It does not establish the full WoodMart API, required parameters, or stable compatibility contract.

## Filter taxonomy configuration

Candidate mapping:
- `pa_family` — family / olfactory family
- `pa_temperament` — temperament
- `pa_season` — season
- `product_cat` — gender/category in the specific proposed mapping
- `product_brand` — brand

Important constraint: the user explicitly required that taxonomy names not be guessed. The settings interface should support choosing taxonomy type and searching registered taxonomies. Validate object types and terms at runtime.

## Responsive interaction requirements

Desktop:
- Sidebar fixed on the right.
- AJAX update on filter change.
- No Apply button.

Mobile:
- Full-screen filter panel.
- Apply button.
- Apply commits selected filters and closes the panel.

Additional mobile UI details:
- A staged filter area displayed excessive vertical spacing and occupied too much of the page.
- Note lists were required to match the supplied reference layout.
- The Personality tab should display four items per row.
- Some options had become compressed together; the desired layout was structured, not simply reduced in width.

## Non-negotiable engineering constraints

- Avoid extra requests.
- Keep the implementation lightweight.
- Preserve the existing approved behavior and visual design unless specifically asked to change it.
- Inspect source and current version before editing.
- Do not infer final code structure from conversation summaries.
- Packaging ZIP files on Windows must strictly enforce forward slashes ('/') in internal archive entry paths to prevent extraction failure in WordPress unzip_file().

- Desktop sidebar width stability with Elementor Pro Sticky: In Elementor Flexbox Containers (`.e-con`), when a sticky widget or shortcode becomes active (`position: fixed`), its empty spacer in a flex column without an explicit `min-width` and `flex-shrink: 0` causes the column to shrink to `min-content` (e.g. ~115px-165px) when filtered results are sparse (such as 1 product). Elementor's sticky scroll listener measures this shrunken spacer and freezes the widget's inline width. Fix requires: (1) CSS defensive min-width (260px) and `flex-shrink: 0` on the filter column, sticky wrapper, and spacer; (2) JS authoritative column width lock across scroll, window resize, and PJAX; (3) scoping Elementor `runReadyTrigger` strictly to product column elements so Sticky handlers are never re-initialized on the preserved live sidebar.
