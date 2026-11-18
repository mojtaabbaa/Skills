# Module 08: Web Accessibility Engineering (WCAG 2.2 AA/AAA)

Integrated from `web-accessibility` (WCAG 2.2) & `wcag-accessibility-checklist.md`. Ensures every UI, landing page, web app, and WordPress theme passes automated + manual keyboard/screen-reader accessibility without compromising visual craft.

---

## 1. Evidence-Led Audit Workflow

When a rendered page is available:
1. Run a live **Lighthouse Accessibility audit** (`lighthouse_audit` in Chrome DevTools MCP or `npx lighthouse <url> --only-categories=accessibility`). Use mobile navigation mode for public pages or snapshot mode when reloading would lose authenticated state.
2. Use failing audit nodes to pinpoint the exact component/template rather than grepping blindly.
3. Inspect the rendered **Accessibility Tree** (`take_snapshot`) for accessible names, roles, states, landmarks (`header`, `nav`, `main`, `footer`), and heading hierarchy (`H1 -> H2 -> H3`, never skipping levels).
4. Test the real flow with **keyboard only** (`Tab`, `Shift+Tab`, `Enter`, `Space`, `Escape`, Arrow keys), fix the source, and re-run both audit and manual interaction.
5. Remember: **a Lighthouse score of 100 is NOT full WCAG conformance** — manual keyboard, zoom (`200%`), and reduced-motion checks are mandatory.

---

## 2. WCAG 2.2 POUR Engineering Checklist

### A. Perceivable
- **Text Alternatives (1.1.1):**
  - Informative images: concise, descriptive `alt` text describing meaning (not "image of...").
  - Decorative images: `alt=""` with `role="presentation"` or `aria-hidden="true"`.
  - Icon-only buttons: ALWAYS provide `aria-label="..."` or `.visually-hidden` text, and set `aria-hidden="true"` on the `<svg>`.
- **Color Contrast (1.4.3, 1.4.6, 1.4.11):**
  - Normal text (`< 18px` or `< 14px bold`): **`>= 4.5:1`** (AA) / `7:1` (AAA).
  - Large text (`>= 18px` or `>= 14px bold`): **`>= 3:1`** (AA) / `4.5:1` (AAA).
  - UI controls, borders, icons & focus rings: **`>= 3:1`** against adjacent background.
  - **Never rely on color alone:** Error and status states must pair color + icon + text message (`aria-invalid="true"` + `aria-describedby`).
- **Media Alternatives (1.2):** Provide `<track kind="captions">` for video and transcripts for audio.

### B. Operable
- **Native Interactive Elements First (2.1):** Prefer `<button type="button">`, `<a href>`, `<input>`, `<select>`, `<dialog>`. Never put `onclick` on a `<div>`/`<span>` without `role="button"`, `tabindex="0"`, and `Enter`/`Space` keydown handling (and never double-bind `Enter`/`Space` onto a native `<button>`).
- **No Keyboard Traps & Skip Links (2.1.2, 2.4.1):** Users can Tab cleanly into and out of every component; modals trap focus and return focus to the trigger on `Escape`/close. First focusable element on the page should be a visible-on-focus Skip to Main Content link.
- **Focus Visible (2.4.7):** NEVER write `*:focus { outline: none; }` globally without a high-contrast `:focus-visible` replacement:
  ```css
  :focus-visible {
    outline: 2px solid currentColor;
    outline-offset: 2px;
  }
  ```
- **Focus Not Obscured (2.4.11 — WCAG 2.2):** Focused elements MUST NOT be hidden behind sticky headers, floating chat bars, or bottom sticky CTAs:
  ```css
  :target, :focus {
    scroll-margin-top: 88px;
    scroll-margin-bottom: 72px;
  }
  ```
- **Dragging Movements (2.5.7 — WCAG 2.2):** Every drag-and-drop or swipe-only control MUST have a single-pointer button/input alternative.
- **Target Size (2.5.8 — WCAG 2.2):** Minimum **`24×24px`** (AA legal floor), **`44×44px` recommended** for touch controls with **`>= 8px` spacing** between adjacent targets.
- **Reduced Motion (2.3.3):** Always respect `@media (prefers-reduced-motion: reduce)` by disabling non-essential animations/transitions while keeping content visible (never leave elements stuck at `opacity: 0`).

### C. Understandable
- **Page Language & Direction (3.1.1):** Always declare `<html lang="fa" dir="rtl">` (or `lang="en"`), and mark inline language switches (`<span lang="en" dir="ltr">...</span>`).
- **Consistent Help (3.2.6 — WCAG 2.2):** Repeated help channels (support link, phone, chat, FAQ) stay in the same relative order across pages.
- **Form Labels & Error Recovery (3.3.1, 3.3.2, 3.3.3):** Every input has a programmatic `<label for>` (placeholders are NOT labels). Announce validation errors with `role="alert"` / `aria-live="polite"`, link via `aria-describedby`, and move focus to the first invalid field on submit.
- **Redundant Entry (3.3.7 — WCAG 2.2):** Auto-populate or offer selection for info the user already entered in the same flow (e.g., billing -> shipping).
- **Accessible Authentication (3.3.8 — WCAG 2.2):** Never block password paste/autofill (`autocomplete="current-password"`), and support passkeys/OTP/email links without cognitive puzzle traps.

### D. Robust
- **Semantic HTML over ARIA (4.1.2):** Use native landmarks and controls first; add ARIA (`aria-expanded`, `aria-controls`, `aria-current="page"`, `role="tablist"`) only when native semantics don't cover the widget.
- **Live Regions (4.1.3):** Use `aria-live="polite"` (toasts/status updates) or `role="alert"` (urgent errors) so screen readers announce dynamic changes without stealing focus.

---

## 3. Priority Triage Before Ship

- **Critical (Fix Immediately):** Missing form labels, missing image `alt`, contrast failure (`< 4.5:1`), keyboard traps, missing `:focus-visible`.
- **Serious (Fix Before Launch):** Missing `lang`/`dir`, skipped headings, vague "click here" links, auto-playing media, missing skip link, focus obscured by sticky header.
- **Moderate (Fix Soon):** Icon buttons missing `aria-label`, inconsistent nav order, missing error identification, missing landmarks.
