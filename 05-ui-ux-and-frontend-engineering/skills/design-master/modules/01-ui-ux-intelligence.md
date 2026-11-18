# Module 01: UI/UX Design Intelligence (BM25 Search Engine & WCAG Baseline)

Consolidated from `ui-ux-pro-max` (68-file intelligence database: 79 styles, 192 product palettes & reasoning profiles, 74 font pairings, 119 UX guidelines, 105 icons, 25 chart types, 17 GSAP motion presets, 34 landing structures, 32 app-interface rules, and 22 technology stacks). All paths are fixed for global execution.

---

## 1. Quick-Start Design System Generation (Step 1 for Any UI Project)

Run the global BM25 engine from **any active workspace** using the absolute global script path:

```bash
python "~/.gemini/config/skills/design-master/scripts/ui-ux/search.py" "<product_type> <industry> <keywords>" --design-system -p "Project Name"
```

### Persistence Pattern (`MASTER.md` + `pages/<page>.md`)
Persist hierarchical design decisions into the current workspace when building multi-page products:

```bash
# 1. Generate project-wide source of truth -> design-system/<slug>/MASTER.md
python "~/.gemini/config/skills/design-master/scripts/ui-ux/search.py" "saas fintech dashboard" --design-system --persist -p "MyApp"

# 2. Generate page-specific override -> design-system/<slug>/pages/dashboard.md
python "~/.gemini/config/skills/design-master/scripts/ui-ux/search.py" "analytics realtime dashboard" --design-system --persist -p "MyApp" --page "dashboard"
```

- When implementing a page, read `design-system/<slug>/pages/<page>.md` first; if absent, follow `design-system/<slug>/MASTER.md`.
- **Important:** After generating the baseline, ALWAYS apply **`Module 02` (Anti-Slop Taste Gate)** to elevate the aesthetic beyond generic template output!

---

## 2. Design Tuning Dials (Optional Fine Control)

| Flag | Range | Default | Effect |
| :--- | :---: | :---: | :--- |
| `--variance` | `1–10` | `5` | Layout creativity: `1–3` safe clean grids, `4–7` balanced editorial/asymmetry, `8–10` bold artistic/bento |
| `--motion` | `1–10` | `4` | Animation intensity: `1–3` micro-transitions only, `4–7` purposeful reveals, `8–10` choreographed GSAP |
| `--density` | `1–10` | `5` | Information density: `1–3` generous whitespace/editorial, `4–7` standard SaaS, `8–10` compact pro dashboards |

---

## 3. Targeted Domain & Stack Lookups

Run supplemental queries whenever you need deeper detail in one specific domain:

```bash
python "~/.gemini/config/skills/design-master/scripts/ui-ux/search.py" "<keyword>" --domain <domain> [-n 5]
```

**Available Domains (`--domain`):**
- `style` — 79 UI styles (glassmorphism, brutalism, bento, editorial, Swiss, dark OLED, etc.)
- `color` — 192 industry-calibrated color palettes
- `typography` — 74 curated font pairings + Google Fonts metadata (`data/ui-ux/google-fonts.csv`)
- `ux` — 119 UX best practices & anti-patterns
- `landing` — 34 landing page & conversion flow structures
- `app-interface` — 32 web/desktop/mobile application interface patterns (navigation, modals, sheets, tables)
- `chart` — 25 data visualization & charting recommendations
- `icons` — 105 icon conventions (Phosphor Icons upstream catalog in `data/ui-ux/phosphor-icons-upstream.json`)
- `motion` — 17 GSAP / CSS animation patterns (respect `prefers-reduced-motion`!)
- `product` — 192 product-type reasoning templates
- `react` — 44 React UI performance & rendering guidelines

**Available Technology Stacks (`--stack <name>`):**
`html-tailwind` (default web), `react`, `nextjs`, `shadcn`, `vue`, `nuxtjs`, `nuxt-ui`, `svelte`, `astro`, `angular`, `laravel`, `threejs`, `flutter`, `react-native`, `swiftui`, `jetpack-compose`, `avalonia`, `javafx`, `uno`, `uwp`, `winui`, `wpf`.

```bash
python "~/.gemini/config/skills/design-master/scripts/ui-ux/search.py" "form validation modal" --stack nextjs
```

---

## 4. Non-Negotiable UI/UX & Accessibility Rules (Priority Order)

1. **Accessibility (CRITICAL):**
   - Contrast >= `4.5:1` for normal text, >= `3:1` for large text and UI boundaries (WCAG AA).
   - Visible keyboard focus rings (`focus-visible:ring-2`); never strip `outline` without replacement.
   - Semantic landmarks (`<header>`, `<nav>`, `<main>`, `<button>`, `<label for>`); `aria-label` on every icon-only button.
   - Respect `@media (prefers-reduced-motion: reduce)` on all animations.
2. **Touch & Interaction (CRITICAL):**
   - Minimum `44x44px` tap targets on mobile with >= `8px` spacing between adjacent controls.
   - Explicit `cursor-pointer` on clickable cards/controls; never rely on hover-only tooltips for essential info.
   - Disable submit buttons while async requests are in flight; show crisp loading/empty/error states.
3. **Layout, Spacing & Viewport Discipline (HIGH):**
   - Zero horizontal overflow at `375px`, `768px`, `1024px`, and `1440px`.
   - Account for fixed/sticky headers (`scroll-margin-top` / top padding) so anchored content is never clipped.
   - Maintain crisp typographic scale (`min 16px` body on mobile to prevent iOS input zoom; `max-w-[65ch]` for readable prose).
   - Reserve visual hierarchy: 1 primary CTA per viewport section, consistent `4px/8px` spacing rhythm.
4. **Iconography & Visual Media (HIGH):**
   - **Never use emojis** (`🚀`, `🎨`, `⚙️`) as UI icons.
   - Use **Phosphor Icons** (`@phosphor-icons/react`, consistent weight & size `20–24px`) for general UI, or **Lucide** (`lucide-react`) inside shadcn/ui projects (`Conflict C5` resolved).
   - Never apply layout-shifting hover animations (`scale` pushing siblings); prefer smooth `color`, `border`, or `opacity` transitions (`150–250ms`).
5. **App UI vs. Marketing Landing Clarity:**
   - **Marketing/Landing:** Strong focal hero, clean visual narrative, generous whitespace, clear primary CTA, social proof.
   - **App/Dashboard UI:** Predictable navigation shell, crisp data density, keyboard shortcuts, clear table/filter ergonomics, tabular numbers (`tabular-nums`), zero marketing fluff inside workspace chrome.

---

## 5. Data Integrity Validation

If data CSVs are ever updated, verify integrity with:
```bash
python "~/.gemini/config/skills/design-master/scripts/ui-ux/validate_data.py"
```
