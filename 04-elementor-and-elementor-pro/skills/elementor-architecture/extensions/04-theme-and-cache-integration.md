# Extension 04: Elementor Theme, AJAX & Caching Integration Discipline

Consolidated from `elementor-theme-integration` (brand-agnostic). Governs safe runtime integration between Elementor/Elementor Pro, active WordPress themes, WooCommerce AJAX loops, and optimization plugins.

---

## 1. Confirm Active Theme Ownership First (Never Assume!)

Target WordPress sites use multiple themes (**Astra**, **Hello Elementor**, **WoodMart**, and custom themes). NEVER assume WoodMart selectors or classes on a site without inspecting the active theme first:
- Confirm whether **Elementor Theme Builder** or the **active theme** owns Header, Footer, Single Post, Single Product, and Shop Archive templates.
- Keep business rules, pricing, permissions, and persistence in a **custom plugin/domain module** — use Elementor strictly for presentation and layout composition.

---

## 2. DOM Ownership, Layout Stability (CLS) & JS Lifecycle

1. **Server-Side Placement First:** Before moving any element with JavaScript, confirm whether Theme Builder, a theme hook, or Elementor template priority can place it server-side. Moving DOM nodes after full `window.load` causes visible CLS regression.
2. **Stable Scoped Selectors:** Scope custom CSS and JS beneath a plugin-owned class or `data-*` attribute — NEVER couple critical logic to fragile generated `.elementor-element-XXXXXXX` IDs unless intentionally targeting one saved template.
3. **Idempotent AJAX Reinitialization:**
   - When WoodMart PJAX, WooCommerce variation forms, or Elementor Loop AJAX replace DOM subtrees, use **delegated events** on stable ancestors or scoped `elementorFrontend.elementsHandler.runReadyTrigger($newContainer)` (NEVER re-trigger the entire document!).
   - Guard initialization with a `data-initialized` flag so repeated AJAX calls never stack duplicate listeners.
   - Avoid broad `MutationObserver` or `setInterval` polling loops; narrow observers to the smallest subtree and disconnect on cleanup.
4. **Server-Side Authority on Elementor Forms:** Never treat client-side conditional field visibility or hidden steps as authorization or workflow security — validate roles, permissions, and state transitions server-side.

---

## 3. Caching, Minification & RUCSS Pitfalls (Elementor + WP Rocket / Autoptimize)

- **WP Rocket Remove Unused CSS (RUCSS):** Frequently strips dynamic CSS needed by Elementor off-canvas drawers, popups, tabs, accordions, or AJAX-injected cards. Always safelist dynamic state classes and test guest mobile sessions after enabling RUCSS.
- **JS Concatenation / Delay JS (Autoptimize / WP Rocket):** Aggressively combining or delaying Elementor frontend scripts (`elementor-frontend`, `swiper`, WoodMart scripts) can break mobile menus, accordions, sticky add-to-cart, and interactive tabs. Exclude critical interactive handles or verify after every change.
- **LCP & DOM Profiling:** Never blame Elementor DOM node count blindly — profile TTFB, LCP image discovery (never lazy-load the hero LCP image!), third-party CDN fonts/scripts, and long JS tasks separately.
- **Pre-Delivery Validation Matrix:** Verify Editor Preview vs live Frontend, Guest vs Logged-in, Mobile (`375–390px`) vs Desktop (`1440px`), RTL/LTR direction, AJAX refresh, keyboard navigation, and active cache/minify layers.
