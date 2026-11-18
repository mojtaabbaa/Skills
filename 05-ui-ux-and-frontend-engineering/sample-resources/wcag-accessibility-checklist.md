# WCAG 2.2 Accessibility (a11y) Engineering Checklist

## 1. Color Contrast & Visual Perception
- [ ] Text contrast ratio is at least 4.5:1 for normal text (WCAG AA).
- [ ] Large text (18pt / 24px or bold 14pt / 18.66px) has at least 3:1 contrast.
- [ ] Active UI components and focus rings have at least 3:1 contrast against adjacent background.
- [ ] Information is never conveyed by color alone (e.g. error states include an icon or text message).

## 2. Touch & Pointer Targets
- [ ] All interactive buttons, links, swatches, and toggles have a minimum target size of 44x44px.
- [ ] Sufficient spacing exists between touch targets to prevent accidental mis-taps.

## 3. Keyboard Navigation & Screen Readers
- [ ] Visible focus outlines are never disabled (`outline: none` without replacement is forbidden).
- [ ] Interactive modal dialogs trap focus while open and release focus upon close.
- [ ] All `<img>` tags have descriptive `alt` attributes or `alt=""` for decorative images.
- [ ] ARIA attributes (`aria-expanded`, `aria-hidden`, `aria-controls`) reflect real runtime state.
