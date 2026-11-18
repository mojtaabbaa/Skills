# Module 04: Modern UI Styling — Tailwind CSS v4 & shadcn/ui (Radix)

Consolidated from `ui-styling` (excluding `canvas-design-system.md`, which lives in `Module 07`).

> [!IMPORTANT]
> **Stack Activation Boundary:** Activate this module **ONLY** when designing/styling modern React, Next.js, Vue/Vite, or Tailwind CSS interfaces. Do NOT force Tailwind CSS or shadcn/ui onto WordPress/Elementor/WoodMart projects.

---

## 1. Tailwind CSS v4 First (CSS-First `@theme` Standard)

Tailwind CSS v4 replaces `tailwind.config.js` with CSS-first `@theme` declarations and perceptually uniform **OKLCH** color scales (Conflict C4 resolved):

```css
@import "tailwindcss";

@theme {
  --color-brand-50: oklch(0.97 0.02 250);
  --color-brand-500: oklch(0.58 0.20 250);
  --color-brand-900: oklch(0.24 0.12 250);

  --font-display: var(--font-vazirmatn), "Vazirmatn", system-ui, sans-serif;
  --font-body: var(--font-vazirmatn), "Vazirmatn", system-ui, sans-serif;

  --radius-card: 1rem;
  --radius-control: 0.75rem;
}
```

- Use CSS logical utilities (`ms-*`, `me-*`, `ps-*`, `pe-*`, `start-*`, `end-*`, `text-start`) for seamless Persian RTL & English LTR layouts.
- Prefer container queries (`@container`, `@md:grid-cols-2`) for reusable cards/widgets alongside viewport breakpoints (`sm`, `md`, `lg`, `xl`).
- Keep `dark` mode semantic tokens cleanly paired via `.dark` class (`next-themes`) or `color-scheme: dark`.

---

## 2. shadcn/ui (Radix & Base UI Primitives) Critical Composition & Styling Rules

Upgraded with latest `shadcn/ui` v2 production rules:

- **Inspect Before Coding:** Check `components.json` / `npx shadcn@latest info --json` (`aliases`, `isRSC`, `base`: `radix` vs `base`, `iconLibrary`, `tailwindVersion`, `tailwindCssFile`) before adding or importing components.
- **Use Components, Not Custom Markup:**
  - Callouts -> `Alert`; Empty states -> `Empty`; Dividers -> `Separator`; Loading placeholders -> `Skeleton`; Status tags -> `Badge`; Loading buttons -> `Button` (`disabled`) + `Spinner` + `data-icon` (never invent `isLoading`/`isPending` prop).
  - Chat / AI UI -> compose `MessageScroller`, `Message`, `Bubble`, `Attachment`, `Marker`, `Trace` instead of hand-rolled scroll/bubble divs.
- **Strict Styling & Tailwind Discipline:**
  - Use semantic tokens (`bg-primary`, `bg-background`, `text-muted-foreground`) — **NEVER** raw palette colors (`bg-blue-500`) or manual `dark:` overrides when semantic tokens exist.
  - Use `flex gap-*` / `flex-col gap-*` — **NO** `space-x-*` or `space-y-*`.
  - Use `size-10` instead of `w-10 h-10`; use `truncate` shorthand; use `cn()` for conditional classes; NEVER add manual `z-index` overrides on `Dialog`/`Sheet`/`Popover`.
- **Component Structure & Accessibility Guarantees:**
  - **Forms:** Use `FieldGroup` + `Field` + `FieldLabel` + `FieldDescription`; use `data-invalid` on `Field` + `aria-invalid` on the input; use `FieldSet` + `FieldLegend` for radio/checkbox groups; use `InputGroup` + `InputGroupInput`/`InputGroupAddon` for inputs with buttons; use `ToggleGroup` for 2–7 option toggles.
  - **Required Wrappers:** Always keep `SelectItem` inside `SelectGroup`, `DropdownMenuItem` inside `DropdownMenuGroup`, `TabsTrigger` inside `TabsList`, `AvatarFallback` inside `Avatar`, and `DialogTitle`/`SheetTitle`/`DrawerTitle` (use `sr-only` if visually hidden) inside overlays.
  - **Base vs Radix Triggers:** Use `asChild` for Radix UI projects and `render` prop for Base UI projects.
  - **Icons inside Components:** Use `data-icon="inline-start"` or `"inline-end"` without manual `size-4`/`w-4 h-4` classes (components size icons via CSS). Match project `iconLibrary` (`lucide-react` default inside shadcn).
- **Safe Upstream Updates:** Always run `npx shadcn@latest add <comp> --dry-run` and `--diff <file>` before updating existing local components; NEVER run `--overwrite` without explicit user approval.

---

## 3. Helper Scripts & Deep References

```bash
# Install / scaffold shadcn components via Python helper
python "~/.gemini/config/skills/design-master/scripts/ui-styling/shadcn_add.py" button card dialog

# Generate legacy Tailwind config when working in a Tailwind v3 repo
python "~/.gemini/config/skills/design-master/scripts/ui-styling/tailwind_config_gen.py"
```

- [`references/ui-styling/tailwind-v4-customization.md`](../references/ui-styling/tailwind-v4-customization.md) — `@theme`, OKLCH color scales, custom fonts, breakpoints, shadows
- [`references/ui-styling/tailwind-utilities.md`](../references/ui-styling/tailwind-utilities.md) — Layout, grid, flex, spacing, typography, dark mode patterns
- [`references/ui-styling/tailwind-responsive.md`](../references/ui-styling/tailwind-responsive.md) — Mobile-first breakpoints & container queries
- [`references/ui-styling/shadcn-components.md`](../references/ui-styling/shadcn-components.md) — Component catalog & composition patterns
- [`references/ui-styling/shadcn-theming.md`](../references/ui-styling/shadcn-theming.md) — `next-themes`, CSS variable theming, dark mode toggle
- [`references/ui-styling/shadcn-accessibility.md`](../references/ui-styling/shadcn-accessibility.md) — WCAG AA/AAA, ARIA, keyboard & screen-reader patterns
