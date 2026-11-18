# Elementor, Theme, and UI Integration History

## Themes and builder

Known themes across projects:
- Astra
- Hello Elementor
- WoodMart

Elementor and Elementor Pro are recurring. Theme-specific implementation must be based on the actual active theme for the target site. A prior correction explicitly established that one project was not using WoodMart.

## Product-card presentation: Ravi Perfume

Requirements recorded:
- Remove hover description.
- Match the approved Figma frame.
- Persian title RTL; English name left-aligned.
- Data may contain a pipe separator (`|`) between Persian and English names; display should remove the pipe while retaining both segments.
- Brand displayed as muted text after title.
- Price on right, add-to-cart button on left.
- Default volume selection 30ml.
- Remove black underline on variation selector.
- Desktop typography sizes were specified in the original task but are not preserved in this summary.
- Preserve the approved design; do not redesign the card without explicit instruction.

## Elementor DOM and performance snapshot

A user-reported DOM snapshot:
- totalNodes: 4623
- divs: 1265
- elementorElements: 228
- widgets: 130
- containers: 98

Use as a historical baseline only. DOM node count alone does not prove the cause of poor performance; profile layout, scripting, style recalculation, network, and LCP separately.

## Font and script loading observations

- `fonts.googleapis.com` Roboto requests were identified as a slowdown.
- `unpkg.com` libphonenumber-js was slow; user uploaded `libphonenumber-max.js` locally.
- Autoptimize JavaScript concatenation broke mobile buttons in one configuration.
- WP Rocket and Autoptimize were both used.
- Mobile performance remained worse than desktop in one investigation.
- An LCP resource-load delay of about 2,990ms was discussed; a slider image was implicated.
- WP Rocket Remove Unused CSS was enabled and unused CSS was removed.

Do not re-enable concatenation or defer/delay strategies without testing interactive controls and critical rendering.

## Key Takeaways relocation issue

A blog post section was being moved by the theme or another script. A previous footer-based relocation approach corrected placement, but the user reported that the position only became correct after full load, causing visible movement. The desired fix was deterministic placement without layout shift. The exact final code is not preserved; inspect current theme behavior and DOM before reimplementing.

## Service portal

Known flow:
1. Login/register.
2. Select request/service type on a gateway page.
3. Complete Elementor form.
4. Enter pending approval state.
5. Admin manually reviews submitted documents.
6. Admin assigns role/access.

Custom roles were created using the Members plugin. Forms were multi-step. Consultation options historically included:
- In-person: 2,000,000 toman
- Phone: 1,000,000 toman
- Duration: 30–40 minutes

Confirm current prices, roles, and form implementation before reuse.
