---
name: frontend-engineering
description: Designs, implements, and debugs performant, accessible, responsive frontend interfaces for WordPress, WooCommerce, Elementor, and custom plugins, including RTL/LTR and AJAX-driven components.
---

# Frontend Engineering

## Mission

Build frontend behavior and interfaces that preserve the site's approved design, integrate with WordPress/WooCommerce lifecycles, work across desktop and mobile, and remain maintainable. Treat the DOM, server-rendered markup, CSS cascade, JavaScript lifecycle, and network behavior as one system.

## When to use this Skill

Use it for HTML/CSS/JS changes, responsive UI, product cards, filters and drawers, Elementor widgets, interactive product controls, sticky elements, pagination, modal behavior, accessibility, RTL/LTR, and frontend performance investigations.

For backend business logic, load `wordpress-development-architecture` and/or `woocommerce-engineering`. For plugin architecture load `custom-wordpress-plugin-engineering`. For filtering lifecycle load `advanced-woocommerce-filtering-ajax`. For performance diagnosis load `performance-engineering` too.

## Context and evidence rules

- The user has repeatedly requested lightweight changes, minimal extra network requests, and preservation of already-approved UI.
- The Ravi Perfume product-card design has explicit historical requirements; see `references/known-ui-contracts.md`.
- Inter and Roboto were mentioned in design contexts; Roboto was intended for English blog pages only in one project. Never globally load or replace fonts based on that historical note.
- The user's sites have used Elementor/Elementor Pro and multiple themes. Confirm the target site's active theme and rendered template; never infer it from another project.
- Historical UI notes are not a substitute for the supplied Figma frame, screenshot, markup, or current CSS.

## Operating protocol

### 1. Inspect before styling or scripting

Record:
- Target URL/template and viewport(s).
- Active theme, child theme, Elementor template/widget, and relevant plugin versions.
- Actual rendered HTML and stable selectors.
- Existing CSS sources and specificity (theme, Elementor generated CSS, plugin styles, custom CSS).
- Existing JavaScript event handlers and events emitted by the platform/theme.
- Whether content is replaced by AJAX, hydrated after render, or moved by another script.
- Approved visual reference and what must remain unchanged.

Do not invent selectors, generated Elementor IDs, theme classes, data attributes, event names, or widget IDs.

### 2. Keep component boundaries clear

- Scope CSS beneath a stable component root owned by the feature.
- Use BEM-like or project-prefixed classes; avoid broad selectors such as `.button`, `.title`, `form`, `nav`, or `ul` when a component scope is possible.
- Keep presentation CSS separate from business logic.
- Prefer server-rendered markup for stable initial content; add JavaScript only for genuine interaction.
- Use data attributes for behavior hooks where suitable; do not couple behavior to visual class names unnecessarily.
- Do not make a CSS-only presentation change alter pricing, stock, permission, or order behavior.

### 3. JavaScript lifecycle and state

- Identify the real lifecycle: initial page load, Elementor frontend initialization, WooCommerce variation events, AJAX loop replacement, drawer open/close, or page navigation.
- Make initialization idempotent. Reinitialization must not add duplicate listeners.
- Use event delegation when the target subtree is replaced dynamically.
- Keep state in one canonical component model; avoid multiple competing sources of truth between DOM attributes, globals, and server responses.
- For async requests, handle loading, error, empty, success, stale-response, and cancellation states.
- Prefer `AbortController` or a request-sequence token when an older response could overwrite newer state.
- Clean up listeners, observers, and timers when component lifetime ends.
- Do not use repeated polling or broad `MutationObserver` instances as the first solution. If an observer is unavoidable, scope it narrowly, filter mutations, and disconnect when no longer needed.

### 4. CSS and responsive behavior

- Implement mobile-first or desktop-first based on the existing project convention; do not arbitrarily mix conventions in one component.
- Use explicit breakpoints derived from the supplied design and real content behavior.
- Check long Persian labels, English product names, translated strings, font loading, and dynamic content expansion.
- Avoid fixed heights unless overflow and dynamic content are explicitly handled.
- Use grid/flex constraints intentionally; verify `min-width: 0`, wrapping, alignment, and intrinsic sizing.
- Ensure sticky/fixed elements account for headers, admin bars, safe areas, and viewport changes.
- Prevent body scroll leakage when mobile drawers/modals are open; restore original scroll state on close.
- Preserve keyboard focus and visible focus styles.

### 5. RTL/LTR and mixed-language content

- Set direction at the smallest correct component boundary.
- Persian title text may need RTL while an English name or brand remains LTR.
- Use `dir="auto"` only when it produces the intended result; verify mixed punctuation, numbers, and separators.
- Use logical CSS properties (`margin-inline`, `padding-inline`, `inset-inline`, `text-align: start`) where practical.
- Do not reorder DOM for visual alignment unless reading order and accessibility remain correct.
- Do not translate or normalize stored product values just to solve visual direction.

### 6. Accessibility and interaction quality

- Use semantic elements and correct button types.
- Provide accessible names and labels.
- Support keyboard operation, focus visibility, Escape behavior for dialogs/drawers, and sensible focus restoration.
- Use `aria-expanded`, `aria-controls`, `aria-live`, and dialog semantics only when they describe actual behavior.
- Do not use ARIA as a substitute for native semantics.
- Check touch target size, contrast, zoom, and reduced-motion preferences.

### 7. Performance constraints

- Do not add a frontend library for a small interaction that can be implemented safely with existing project primitives.
- Enqueue assets only where the component is used.
- Avoid CDN dependencies unless explicitly required and operationally justified.
- Avoid duplicating dependencies already loaded by WordPress, WooCommerce, or Elementor.
- Do not add an extra AJAX request when the current response already contains the necessary data.
- Test under the site's actual optimization/cache configuration; script concatenation and delay/defer can change execution order.

## WordPress and Elementor integration notes

- Use WordPress enqueue APIs instead of hard-coded `<script>` or `<link>` tags where code is plugin/theme-owned.
- Respect Elementor's frontend initialization and editor/preview differences.
- Confirm whether Elementor Theme Builder or the active theme owns the template.
- For WooCommerce variations, use the actual variation form contract and events. Never trust client-side price as the purchase price.
- For AJAX-replaced product loops, use delegated events or explicit reinitialization hooks.
- For WoodMart, inspect the installed version, AJAX payload/response, replacement region, and native events before integrating.

## Delivery protocol

1. State the affected component and preserved behavior.
2. Identify exact files and insertion points.
3. Implement the smallest complete change.
4. Test target breakpoints, RTL/LTR, keyboard, touch, dynamic/AJAX states, and cache/minification.
5. Report actual tests and untested cases.
6. Provide rollback instructions for the change.

## Anti-patterns

- Styling based only on a screenshot without inspecting markup when implementation depends on selectors.
- Global CSS overrides that affect unrelated Elementor widgets.
- Inline script blocks scattered across page-builder content.
- Duplicate listeners after AJAX replacement.
- Unbounded observers or polling loops.
- Hiding required controls instead of fixing their lifecycle or layout.
- Moving DOM nodes after full load when the correct server/template location can be fixed; visible layout shift is a regression.
- Treating visual price text as authoritative commerce data.
