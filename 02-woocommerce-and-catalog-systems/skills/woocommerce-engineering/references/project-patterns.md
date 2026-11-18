# WooCommerce Project Patterns & Historical Requirements

## Product attributes and variations

Historical perfume product data included a global weight/volume attribute `pa_weight`, with values such as 30ml, 50ml, and 100ml. A specific product-card requirement was to select 30ml by default, remove the black underline from the variation selector, and keep the approved card layout unchanged.

A separate product behavior request required weight selection to update price without forcing the user to select a grind type. Do not conflate these two behaviors; the latter may belong to a different product category/store.

## Product-card constraints

For Ravi Perfume:
- Persian product title should render RTL.
- English product name should be left-aligned.
- Source title data could contain a separator such as `ولورا | Velora`; display should remove the separator while preserving the two language segments.
- Brand should appear as muted text after the title.
- Price on the right and add-to-cart action on the left.
- Hover description was to be removed.
- The approved design should not be redesigned casually.
- The site used Elementor/Elementor Pro; the user explicitly corrected an earlier mistaken WoodMart assumption for a separate project. Verify actual theme and markup before applying theme-specific selectors.

## Price-per-unit display

A display requirement used Persian text similar to:
`قیمت هر میل ۴۹,۶۰۰ تومان`

The formula must be based on the selected variation's effective payable price and its actual volume unit. Define rounding, currency unit, sale-price behavior, and whether fees/discounts are included before implementation.

## Cash and installment model

The user's intended behavior:
- Cash purchase uses a cash-specific price and cash gateway.
- Installment gateways use a different price.
- Variation labels should be human-readable (e.g. actual attribute values), not internal strings such as `متغیر #13939`.

Important: the exact final implementation and verified fix are not preserved here. The source ZIP or current plugin repository must be inspected before reusing code.

## Temporary checkout shutdown

The user requested:
- Remove all time-related fields from checkout.
- Remove payment gateways.
- Disable checkout button/non-clickable behavior in all cases.

Engineering interpretation:
- Remove or disable the relevant fields at the server-side checkout data layer.
- Prevent checkout processing server-side while disabled.
- Remove gateways through WooCommerce's gateway availability mechanism.
- Disable or replace the UI button only as a presentation layer.
- Provide a clear message and preserve admin access if requested.
- Ensure direct checkout URL, AJAX checkout, Store API/Blocks checkout, and express-payment paths are considered if installed.

## Out-of-stock ordering

Requirement: products with no stock should appear after in-stock products in shop and product category listings. Preserve selected sorting behavior among products in each stock group. Test pagination and AJAX loops.

## Product-specific payment restriction

A prior request referenced product ID `61965` and a specific gateway restriction. The exact gateway ID is not retained. Inspect the active gateway plugin and product before implementation.

## Packaging fee

A fee of 500,000 toman per product was discussed. The user wanted it displayed before subtotal. Confirm whether per item quantity or per distinct product line, tax handling, and refunds before coding.
