# Module 03: Design System & 3-Layer Token Architecture

Consolidated from `design-system` (tokens, component specifications, states/variants, and token generation/validation scripts). Slide generation & slide CSVs previously buried here have been cleanly moved to **`Module 06` (`06-presentations-and-slides.md`)**.

---

## 1. Three-Layer Token Architecture (Strict Separation)

Never hardcode raw HEX/RGB/px values directly inside production UI components when working inside a systematized design system. Enforce the 3-layer cascade:

```text
Layer 3: Component Tokens  (--button-bg, --card-padding, --input-radius)
            ↓ references
Layer 2: Semantic Tokens   (--color-primary, --surface-card, --text-muted, --space-section)
            ↓ references
Layer 1: Primitive Tokens  (--palette-slate-900, --space-4, --radius-md, --font-size-base)
```

- **Layer 1 — Primitives:** Raw, context-free scales (color ramps `50–950`, spacing scale on `4px/8px` grid, typography sizes/weights, radii, shadows, z-index). Rarely changes.
- **Layer 2 — Semantics:** Intent-driven aliases (`--bg-canvas`, `--bg-surface`, `--text-primary`, `--border-subtle`, `--accent-primary`, `--status-success/warning/error`). **Theme switching (Light <-> Dark) ONLY remaps Layer 2!**
- **Layer 3 — Components:** Scoped overrides for complex components (`--btn-primary-bg`, `--card-border`, `--modal-shadow`) referencing Layer 2 tokens.

### Unified Color Format Rule (Conflict C3 & C4 Resolved)
- **Modern Web / Tailwind v4 Projects:** Prefer **OKLCH** or clean **HEX** CSS variables inside `@theme` / `:root` (see `Module 04`).
- **Legacy Tailwind v3 Projects:** Use space-separated HSL (`217 91% 60%`) wrapped in `hsl(var(--primary))` only when Tailwind v3 opacity modifiers are required (see [`references/tokens/tailwind-v3-legacy-integration.md`](../references/tokens/tailwind-v3-legacy-integration.md)).

---

## 2. Token Starter Template & Automation Scripts

Starter JSON template:
- [`templates/design-tokens-starter.json`](../templates/design-tokens-starter.json)

Run the global token scripts from your project root:

```bash
# Generate assets/design-tokens.css from tokens JSON
node "~/.gemini/config/skills/design-master/scripts/tokens/generate-tokens.cjs" -c assets/design-tokens.json

# Validate codebase for hardcoded hex/px violations outside tokens
node "~/.gemini/config/skills/design-master/scripts/tokens/validate-tokens.cjs" -d src/

# Embed CSS tokens cleanly into standalone HTML deliverables (slides, prototypes, banners)
node "~/.gemini/config/skills/design-master/scripts/tokens/embed-tokens.cjs" input.html
```

---

## 3. Component Specification & State Matrix Standard

Every reusable UI component spec MUST define all 5 dimensions:
1. **Anatomy:** Container, icon/leading slot, label/content, trailing slot, helper/error message.
2. **Variants:** Primary, Secondary, Outline, Ghost, Destructive/Danger.
3. **Sizes:** `sm` (`32px`), `md` (`40px` default), `lg` (`48px`), `icon` (square, min `40–44px` on touch).
4. **All Interactive States:** `default`, `hover`, `active/pressed`, `focus-visible` (high-contrast 2px ring), `disabled` (`opacity-50`, non-interactive), `loading` (spinner + preserved width to avoid layout shift), `error/invalid` (`aria-invalid="true"`).
5. **Spacing & Elevation Contract:** Consistent padding ratios (e.g., horizontal padding = `1.5x–2x` vertical padding on buttons), border radii mapped to semantic tokens (`--radius-sm/md/lg`).

---

## 4. Deep Technical References (Load On Demand)

- [`references/tokens/token-architecture.md`](../references/tokens/token-architecture.md) — Complete 3-layer CSS variable architecture
- [`references/tokens/primitive-tokens.md`](../references/tokens/primitive-tokens.md) — Color, spacing, typography, radius, and shadow primitive scales
- [`references/tokens/semantic-tokens.md`](../references/tokens/semantic-tokens.md) — Light/Dark semantic mapping rules
- [`references/tokens/component-tokens.md`](../references/tokens/component-tokens.md) — Per-component token naming convention
- [`references/tokens/component-specs.md`](../references/tokens/component-specs.md) — Detailed specs for buttons, inputs, cards, modals, badges, tables
- [`references/tokens/states-and-variants.md`](../references/tokens/states-and-variants.md) — Complete state machine & accessibility state mapping
- [`references/tokens/tailwind-v3-legacy-integration.md`](../references/tokens/tailwind-v3-legacy-integration.md) — Legacy Tailwind v3 `tailwind.config.ts` bridge (only for v3 codebases)
