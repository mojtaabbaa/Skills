---
name: woocommerce-engineering
description: Implements and debugs WooCommerce product, variation, pricing, cart, checkout, payment gateway, stock, and order behavior with lifecycle-correct and HPOS-aware code. Use for any custom store or commerce-flow change.
---

# WooCommerce Engineering

## Mission
Preserve commerce correctness across product display, cart calculation, checkout, payment, order persistence, emails, refunds, and stock. A correct price label with a wrong payable amount is a defect, not a partial success.

## Activate when
Products, variations, attributes, swatches, stock sorting, pricing, discounts, fees, cart, checkout, gateways, order data, HPOS, product loops, or WooCommerce REST/Store API are involved.

## Required context loading
1. Read `../../knowledge/PROJECT-REGISTRY.md` and identify the exact store/project.
2. Read `references/project-patterns.md` for prior user requirements and unresolved history.
3. Inspect installed WooCommerce version, product type, active gateways, currency configuration, HPOS state, theme overrides, and current plugin source.
4. If implementing the feature in a custom plugin, also load `custom-wordpress-plugin-engineering`.

## Commerce invariants
- Identify the canonical price for each flow: catalog, selected variation, cart, cash, installment, gateway amount, order total, tax, and refund. Do not assume they are identical.
- UI-only price changes do not change cart or order price.
- Server-side validation is authoritative; JavaScript only improves interaction.
- Cart calculation can run repeatedly. Fee and price mutations must be idempotent.
- A customer must see a price/flow consistent with the amount actually charged and stored on the order.
- Do not apply a site's special rule globally to other sites or products.

## Procedure

### 1. Model the product correctly
Inspect the actual product object and type. Resolve parent/variation IDs, global `pa_*` attributes versus custom attributes, term slugs, purchasability, enabled state, stock status, and active variation price. Never derive variation identity from visible text alone.

### 2. Trace the full price path
For the requested price change, trace:
1. Product/variation data.
2. Catalog price display and structured data.
3. Add-to-cart validation.
4. Cart item data and price calculation.
5. Coupons, taxes, shipping, and fees.
6. Checkout validation and selected gateway.
7. Gateway amount passed to the provider.
8. Order total and line-item metadata.
9. Emails, account/order views, refunds, and admin reports.

State which steps the code changes. Keep integer/currency-unit handling explicit. Confirm toman/rial conversion and rounding from the actual site's settings and existing implementation.

### 3. Scope behavior narrowly
Filter by confirmed product IDs, categories, user capability/role, payment method, cart contents, or checkout context as required. Do not rely on a hard-coded username. A historic product ID is not proof that it is still the target product.

### 4. Use WooCommerce APIs
- Load products with `wc_get_product()` and use product/variation objects.
- Load orders with `wc_get_order()` and use CRUD APIs.
- Check HPOS support; never assume orders are stored as `shop_order` posts.
- Use documented cart/checkout/gateway hooks supported by the installed version.
- Inspect installed gateway source/settings to obtain actual gateway IDs and amount calculation path.
- Avoid direct writes to WooCommerce tables or price/order meta unless a clearly documented exceptional reason exists.

### 5. Fees and custom charges
Decide whether the amount is an order-level fee, shipping charge, or product line item. Define whether it is per quantity, per unique line, or per order; define taxability and refund treatment. Prevent duplicate fee insertion during repeated totals recalculation. Use line items if the charge must be attributed to each product.

### 6. Price visibility and catalog ordering
Price hiding must cover all relevant surfaces: product loop, single page, quick view, cart, structured data, REST/API, feeds, and customer-facing templates as required. Administrator visibility should use capabilities. Out-of-stock products should be ordered at query level while preserving chosen sorting among in-stock products and stable pagination.

### 7. Test end-to-end
Test simple and variable products, disabled/out-of-stock variations, quantities, multiple items, coupons, shipping/tax, guest/customer/admin, each relevant gateway, order creation, order totals, line item metadata, refresh/recalculation, and refunds if custom charges apply.

## Known historical user requirements
- Perfume volumes/attributes included 30ml, 50ml, and 100ml; `pa_weight` was mentioned in one project. Confirm actual registered attribute key before use.
- A specific product-card context required defaulting to 30ml; do not generalize this to all variable products.
- Another product flow required weight selection to update price without forcing grind-type selection. Treat that as a separate business rule unless repository evidence links them.
- Cash-specific price/gateway versus a different installment price/gateway was a recurring requirement. Exact final code is not preserved in this pack; inspect the current ZIP/repository and gateway plugin.
- A conditional gateway requirement historically referenced product ID `61965`; the exact gateway ID is not preserved.
- A packaging charge of 500,000 toman per product was discussed; confirm amount, quantity semantics, and tax/refund rules before reuse.
- The user requested a temporary checkout shutdown and gateway removal in a past task. Do not rely on a disabled button alone; block server-side checkout paths, including any Store API/Blocks/express path in use.
- Product cards must preserve approved layout unless asked otherwise; price on right/add-to-cart on left and Persian/English title direction were discussed for a particular perfume site.

## Risk controls
- Never silently change order totals after an order is created.
- Never trust browser-submitted prices or variation IDs without revalidation.
- Never assume gateway amount equals cart total; trace the installed gateway code.
- Never leave checkout in a broken state with no explanation if it is intentionally disabled.
- Do not alter payment status semantics, stock reduction, or order creation flow casually.

## Output contract
Provide the hook/lifecycle, exact scope, amount source and currency units, what persists to the order, gateway integration points, test cases, and rollback. Flag unknown gateway IDs, prices, attribute slugs, and final code history as unknown rather than inventing them.

## Related Skills
- `wordpress-development-architecture`
- `custom-wordpress-plugin-engineering`
- `advanced-woocommerce-filtering-ajax`
- `elementor-theme-integration`
