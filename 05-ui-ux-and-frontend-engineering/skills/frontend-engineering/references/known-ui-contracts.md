# Known UI Contracts and Historical Frontend Context

Evidence level: HISTORICAL unless a current project artifact or explicit current instruction confirms it.

## Ravi Perfume product card

Historical requirements:
- Preserve the approved product-card design; do not redesign it without an explicit request.
- Remove hover description when the relevant card implementation calls for it.
- Persian product title is RTL; English name is LTR/left aligned.
- Source title may contain a `|` separator, e.g. Persian title plus English name. Display requirement was to remove the visible separator while retaining the two name segments.
- Brand appears as muted secondary text after the title.
- Price on the right, add-to-cart control on the left.
- Default selected volume in the relevant card flow: 30ml.
- Remove the unwanted black underline on the volume/variation selection control.
- Desktop typography values were specified in the original conversation but are not preserved in the current knowledge record. Do not invent them; recover the design source or ask for the exact measurements.

The active theme was corrected in a separate task and was not WoodMart. Verify target site/theme before applying WoodMart selectors.

## Ravi Smart Filter responsive UI

Historical requirements:
- Desktop: fixed sidebar on the right, filters apply immediately via AJAX, no Apply button.
- Mobile: full-screen filter panel; user changes draft selections and presses Apply to commit and close the panel.
- Mobile Personality tab: four items per row.
- A staged mobile-filter area previously had excessive vertical spacing and occupied too much of the screen.
- A note-list arrangement was expected to match a supplied screenshot. The exact visual reference is not embedded in this text record; do not guess its details.
- Some options had become compressed together. The intended outcome was structured spacing, not merely shrinking all items.

For current filter behavior, load `advanced-woocommerce-filtering-ajax` as well.

## Design tokens and assets mentioned

Historical colors used across different projects include:
- `#FF6B38`, `#F6CB20`, `#D71304`, `#C20F2D`
- `#282828`, `#828043`, `#005336`, `#F3F2EC`, `#02311f`
- `#FED80D`, `#0B2E71`

Do not treat this list as one global palette. Confirm which site/design system owns a token.

Image and visual preferences from prior tasks:
- Common aspect ratios included 7:5, 16:9, and 1:1.
- Common target dimensions included 1536×1024 and 1920×1080.
- Minimal visuals, often no text overlay; transparent PNG assets were requested in some contexts.

## RTL/LTR implementation reminders

- Mixed Persian/English product titles need component-level direction handling.
- Use logical CSS properties where possible.
- Preserve source text and stored values; solve layout direction at rendering time.
- Verify number grouping and punctuation around mixed-direction text.

## Key Takeaways relocation

A post-page section called Key Takeaways was being moved by theme or other page scripts. A footer-based relocation approach improved position, but the user observed the element moved only after full page load, creating layout shift. The exact final implementation is not retained. Inspect the current theme/template lifecycle before reproducing any relocation script.
