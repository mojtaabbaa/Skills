# Module 05: Brand Visual Identity, Logo Design, CIP & SVG Icon Studio

Consolidated from generic `brand` (visual guidelines & Node sync/validation scripts) + `design` (Logo 55 styles, Corporate Identity Program 50 deliverables, and SVG Icon 15 styles).

> [!IMPORTANT]
> **Disambiguation From Client `brand-*` Skills (Conflict C9 Resolved):**
> - **This module** is the generic methodology for *designing, documenting, auditing, or generating* visual brand identity systems from scratch.
> - When working on an existing project with its own local brand identity skill (`.agents/skills/brand-*/SKILL.md`), **that local brand skill is the absolute source of truth** for brand facts, verified hex colors, fonts, and rules.

---

## 1. Brand Visual Guidelines & Asset Sync Framework

Starter template for new brand guidelines (`docs/brand-guidelines.md`):
- [`templates/brand-guidelines-starter.md`](../templates/brand-guidelines-starter.md)

### Global Brand Automation Scripts (Fixed Antigravity Paths)
```bash
# Inject project docs/brand-guidelines.md context into current workflow
node "~/.gemini/config/skills/design-master/scripts/brand/inject-brand-context.cjs"

# Sync docs/brand-guidelines.md palette/typography -> assets/design-tokens.json & .css
node "~/.gemini/config/skills/design-master/scripts/brand/sync-brand-to-tokens.cjs"

# Extract & format color palette definitions
node "~/.gemini/config/skills/design-master/scripts/brand/extract-colors.cjs"

# Validate visual assets against brand guidelines
node "~/.gemini/config/skills/design-master/scripts/brand/validate-asset.cjs" <asset-path>
```

*Note:* For visual color extraction from an existing logo or screenshot, inspect the image directly with Antigravity's native `read_file` multimodal vision instead of legacy external multimodal scripts.

---

## 2. Logo Design Studio (55 Styles × 55 Industries × 55 Palettes)

Search the verified logo intelligence CSVs (`data/logo/styles.csv`, `industries.csv`, `colors.csv`) before crafting concepts:

```bash
# Search logo styles, industry norms, or color psychology
python "~/.gemini/config/skills/design-master/scripts/logo/search.py" "specialty coffee luxury" --domain style
python "~/.gemini/config/skills/design-master/scripts/logo/search.py" "optical eyewear" --domain industry
python "~/.gemini/config/skills/design-master/scripts/logo/search.py" "burgundy gold luxury" --domain color
```

### Rendering Logos (Conflict C8 Resolved)
1. **Primary Method (Antigravity Native — Zero API Key Friction):** Build an engineered prompt using [`references/branding-studio/logo-prompt-engineering.md`](../references/branding-studio/logo-prompt-engineering.md) and delegate directly to Antigravity's native **`image-generator`** subagent (`invoke_subagent` with `TypeName: "image-generator"`).
2. **Optional Batch CLI Fallback:** `scripts/logo/generate.py` is preserved if the user explicitly wants scripted Gemini API batch generation with `GEMINI_API_KEY`.

---

## 3. Corporate Identity Program — CIP Studio (50 Deliverables)

Search the 50 CIP deliverables (`business cards, letterheads, packaging, signage, apparel, vehicles, social kits...`), 20 industries, 20 styles, and 20 mockup contexts (`data/cip/*.csv`):

```bash
python "~/.gemini/config/skills/design-master/scripts/cip/search.py" "packaging signage stationery" --domain deliverable
python "~/.gemini/config/skills/design-master/scripts/cip/search.py" "luxury retail" --domain style

# Render generated CIP mockup PNGs into a polished client presentation HTML deck
python "~/.gemini/config/skills/design-master/scripts/cip/render-html.py" --input <mockups-dir> --output cip-presentation.html
```

- Generate individual CIP mockup visuals using **`image-generator`** subagent (referencing the brand logo & exact hex palette), guided by [`references/branding-studio/cip-deliverable-guide.md`](../references/branding-studio/cip-deliverable-guide.md) and [`references/branding-studio/cip-prompt-engineering.md`](../references/branding-studio/cip-prompt-engineering.md).

---

## 4. Custom SVG Icon Design (15 Styles × 12 Categories)

- Catalog in `data/icon/styles.csv`: 15 icon styles (`outlined, filled, duotone, rounded, sharp, minimal, geometric, hand-drawn, neon, gradient, glassmorphic, pixel, isometric, sticker, monochrome`).
- **Best Practice:** For standard UI controls, use Phosphor or Lucide (`Module 01/04`). Craft **clean inline SVGs** (`viewBox="0 0 24 24"`, explicit `stroke-width`, `currentColor`, multi-size `16/24/32/48px`) for bespoke brand icons, feature marks, and custom empty-state illustrations. (`scripts/icon/generate.py` is preserved for optional API batch generation.)

---

## 5. Deep References (Load On Demand)

- Brand System: [`visual-identity.md`](../references/brand/visual-identity.md) | [`color-palette-management.md`](../references/brand/color-palette-management.md) | [`typography-specifications.md`](../references/brand/typography-specifications.md) | [`logo-usage-rules.md`](../references/brand/logo-usage-rules.md) | [`voice-framework.md`](../references/brand/voice-framework.md) | [`messaging-framework.md`](../references/brand/messaging-framework.md) | [`asset-organization.md`](../references/brand/asset-organization.md) | [`consistency-checklist.md`](../references/brand/consistency-checklist.md) | [`approval-checklist.md`](../references/brand/approval-checklist.md)
- Logo & CIP Studio: [`logo-style-guide.md`](../references/branding-studio/logo-style-guide.md) | [`logo-color-psychology.md`](../references/branding-studio/logo-color-psychology.md) | [`logo-prompt-engineering.md`](../references/branding-studio/logo-prompt-engineering.md) | [`cip-deliverable-guide.md`](../references/branding-studio/cip-deliverable-guide.md) | [`cip-style-guide.md`](../references/branding-studio/cip-style-guide.md) | [`cip-prompt-engineering.md`](../references/branding-studio/cip-prompt-engineering.md)
