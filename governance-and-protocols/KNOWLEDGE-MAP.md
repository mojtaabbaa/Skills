# Knowledge Map

## Skills and their ownership

| Concern | Primary Skill | Secondary Skills |
|---|---|---|
| WordPress hooks, core APIs, metadata, roles, REST/AJAX, cron | `wordpress-development-architecture` | Plugin Engineering |
| Products, variations, prices, cart, checkout, gateway, order, stock | `woocommerce-engineering` | Plugin Engineering, Elementor |
| Plugin structure, settings, DB schema, migrations, packaging, releases | `custom-wordpress-plugin-engineering` | WordPress, WooCommerce |
| Taxonomy filters, query clauses, AJAX state, sorting, pagination, mobile panel | `advanced-woocommerce-filtering-ajax` | WooCommerce, Plugin Engineering, Elementor |
| Elementor widgets/templates/forms, theme overrides, rendering, CSS/JS lifecycle | `elementor-theme-integration` | WordPress, WooCommerce, Plugin Engineering |

## Cross-domain routing examples

- Change cash/installment pricing inside a plugin: WooCommerce + Plugin Engineering; add WordPress architecture if hooks/security are nontrivial.
- Change Ravi Smart Filter query and UI: Filtering + Plugin Engineering + WooCommerce; add Elementor/Theme Integration if rendered by Elementor or a theme loop.
- Change a product card's variation selector: WooCommerce + Elementor/Theme Integration; Plugin Engineering if implemented in a custom plugin.
- Add an Elementor form approval workflow: Elementor/Theme Integration + Plugin Engineering + WordPress Architecture; include security and workflow validation.
- Fix a PHP fatal in a custom plugin: Plugin Engineering + WordPress Architecture; load domain Skill based on the affected feature.

## Progressive disclosure
Read the Skill entry point first. Then read only the reference files it names for the current issue. Read the project registry before relying on any historical site or plugin detail. Avoid dumping all reference files into context for an unrelated task.

## Future expansion
Skills 06–15 should be added as new focused folders, not merged into one monolithic instruction file. The Master Skill should route tasks and point to the right references; it should not duplicate the technical content of all Skills.
