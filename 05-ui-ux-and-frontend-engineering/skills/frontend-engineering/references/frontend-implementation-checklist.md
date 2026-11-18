# Frontend Implementation Checklist

## Before coding
- [ ] Confirm target site, page, template, theme, builder, and versions.
- [ ] Inspect real markup and stable component root.
- [ ] Capture existing CSS/JS sources and relevant events.
- [ ] Identify approved design constraints and behavior that must not change.
- [ ] Determine whether AJAX replaces the component subtree.
- [ ] Confirm RTL/LTR and mobile/desktop requirements.

## During implementation
- [ ] Scope CSS to the component.
- [ ] Use semantic markup and accessible labels.
- [ ] Keep one canonical state model.
- [ ] Make JS initialization idempotent.
- [ ] Avoid duplicate requests/listeners and broad observers.
- [ ] Handle loading, empty, error, stale, and success states.
- [ ] Respect platform and builder lifecycle.

## Before delivery
- [ ] Test desktop and mobile breakpoints.
- [ ] Test long labels and mixed Persian/English content.
- [ ] Test keyboard and touch interactions.
- [ ] Test after AJAX replacement and variation change.
- [ ] Test with cache/minification enabled where applicable.
- [ ] Check console and network panel.
- [ ] Report what was actually tested and what was not.
