# WoodMart PJAX & AJAX Events Reference

## PJAX Architecture Overview
WoodMart integrates jQuery PJAX (`jquery.pjax.js`) to provide seamless catalog pagination, ordering, and category transitions without full browser page reloads.

### Key Observed Parameters
- `_pjax`: CSS selector of the container element to replace. Standard WoodMart selector is `.wd-page-content` (or `.main-page-wrapper`).
- Query String: Retains standard WooCommerce parameters (`orderby`, `paged`, `min_price`, `max_price`, attribute taxonomy filters `filter_*`).

```text
GET /shop/?orderby=date&paged=2&_pjax=.wd-page-content
HTTP/1.1
X-PJAX: true
X-PJAX-Container: .wd-page-content
```

## Lifecycle Event Sequences

### 1. Catalog AJAX Start
Fired before the PJAX/AJAX request leaves the browser:
```javascript
$(document).on('pjax:start', function(xhr, options) {
    // Show custom loader or skeleton screen
    $('.my-custom-loader').addClass('is-active');
});

$(document).on('pjax:send', function(xhr, options) {
    // Cancel any pending secondary debounce timers
});
```

### 2. Catalog AJAX Success & DOM Ingestion
Fired when HTML arrives and is injected into the container:
```javascript
$(document).on('pjax:complete pjax:end', function() {
    // 1. Hide loaders
    $('.my-custom-loader').removeClass('is-active');
    
    // 2. Re-trigger custom layout routines
    if (typeof window.reinitCustomTooltips === 'function') {
        window.reinitCustomTooltips();
    }
});

// Specific WoodMart Shop Page Re-initialization Event
$(document).on('wdShopPageInit', function() {
    // WoodMart internal modules (swatches, quick view, hover images) re-init here
});

// WoodMart General AJAX Completion
$(document).on('woodmart_ajax_success', function() {
    // Fired on filter, search, and catalog responses
});
```

### 3. Quick View Modal Lifecycle
WoodMart displays quick view modals via AJAX:
```javascript
// Before modal opens
$(document).on('click', '.open-quick-view', function() {
    // ...
});

// Once modal content is fetched and rendered in the DOM
$(document).on('woodmart-quick-view-displayed', function() {
    var $modal = $('.wd-popup.wd-quick-view');
    // Initialize custom volume selectors or quantity buttons inside modal
});
```

### 4. Swatches & Variation Changes
```javascript
// On swatch click
$(document).on('click', '.wd-swatch', function() {
    var $this = $(this);
    var attributeName = $this.data('attribute');
    var attributeValue = $this.data('value');
    // Note: WoodMart automatically syncs this with the hidden WooCommerce <select>
});
```

## Defensive Rules for Custom Plugin Integrations
1. **Never Re-run Document Ready**: Never call `$(document).ready()` handlers manually; factor re-usable initialization into idempotent functions (`initCustomComponents()`) with a `data-initialized="true"` guard.
2. **Scoping Elementor Hooks**: If using Elementor inside the shop loop, invoke `window.elementorFrontend.elementsHandler.runReadyTrigger($container)` **strictly** targeting the updated grid elements, never `$('body')` or the sidebar.
