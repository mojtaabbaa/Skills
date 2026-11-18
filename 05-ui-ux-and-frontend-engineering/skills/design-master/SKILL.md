---
name: design-master
description: >-
  Unified global Design & UI/UX Master Skill merging UI/UX design intelligence (79 styles,
  192 palettes, 74 font pairings, 119 UX guidelines, 22 stacks via BM25 search), anti-AI-slop
  aesthetic craft & visual critique, 3-layer design token architecture (Primitive -> Semantic ->
  Component), modern Tailwind CSS v4 & shadcn/ui styling, brand visual identity systems
  (logo 55 styles, CIP 50 deliverables, SVG icons 15 styles), unified HTML presentations/slides
  (8 BM25 slide CSVs + Chart.js + AIDA/PAS/FAB), and banners/social/canvas graphic design.
  PURE DESIGN & UI/UX ONLY (excludes WordPress/Elementor/backend implementation). Always pair
  with the active workspace's local `.agents/skills/brand-*/SKILL.md` skill when designing for
  an existing client brand.
---

# Design Master — Unified Global Design & UI/UX Engine

This skill is the single global source of truth for **pure visual design, UI/UX intelligence, design systems, tokens, styling, visual branding, presentations, banners, social graphics, and art direction**.

> [!IMPORTANT]
> **Strict Scope & Client Brand Precedence:**
> 1. **Pure Design & UI/UX Scope:** This skill governs visual direction, UX architecture, tokens, typography, components, slides, banners, and brand graphics. It does **NOT** govern WordPress/Elementor PHP/DOM/AJAX backend engineering.
> 2. **Client Brand Identity Wins First:** If the active workspace contains a local brand skill (`.agents/skills/brand-*/SKILL.md`), load that local brand skill FIRST — its verified palette, fonts, orthography, and photography rules override generic defaults.
> 3. **Stack Guard:** Only apply Tailwind CSS / shadcn / React styling rules (`Module 04`) when the target project uses that stack. Never inject Tailwind/React assumptions into WordPress/Elementor visual briefs unless explicitly requested.

---

## 1. Conflict Resolution Laws (Binding Across All Modules)

Every historical contradiction across the 8 merged design skills is permanently resolved by these rules:

| Conflict Domain | Binding Global Standard |
| :--- | :--- |
| **Aesthetic vs. Templates (`frontend-design` vs `ui-ux-pro-max` vs `canvas`)** | **3-Layer Pipeline:** (1) Use `Module 01` (`ui-ux-pro-max` BM25) for domain research, accessibility, palettes, and typography baselines -> (2) Pass EVERY UI output through `Module 02` (`frontend-design` Anti-Slop Taste Gate) to kill generic SaaS defaults and excess motion -> (3) Use `Canvas 90/10` (`Module 07`) **ONLY** for posters, visual manifestos, and art-direction graphics (never dashboards/apps). |
| **Token Source of Truth (`5 competing models`)** | **Clear Hierarchy:** For full multi-page apps/design systems -> `design-system/<slug>/MASTER.md` (decisions) + 3-layer `assets/design-tokens.json` / `assets/design-tokens.css` (code truth; zero raw hex inside components). For single-page/prototype builds -> compact 4–6 semantic CSS variables (`--bg`, `--surface`, `--accent`, `--ink`, `--muted`). |
| **Color Space & Tailwind Version** | **Tailwind CSS v4 (`@import "tailwindcss";` + `@theme` + OKLCH/HEX)** is the default standard (`Module 04`). Legacy Tailwind v3 (`tailwind.config.ts` + space-separated HSL) is retained strictly as a compatibility reference (`references/tokens/tailwind-v3-legacy-integration.md`). |
| **Iconography Standard** | **Context-Matched:** General web/product UI -> **Phosphor Icons** (`@phosphor-icons/react`, fallback Heroicons). Inside a **shadcn/ui** codebase -> **Lucide** (`lucide-react`) for ecosystem consistency. Brand marks / editorial custom graphics -> **Custom inline SVG**. NEVER use emojis as UI icons. |
| **Slides & Presentations** | **Single Unified Engine (`Module 06`):** Combines the 8 BM25 slide CSVs & scripts + Chart.js HTML templates + AIDA/PAS/FAB copywriting formulas. |
| **Image Generation & Rendering** | **Antigravity-Native First:** Use Antigravity's native **`image-generator`** subagent for AI imagery/logos/banners/mockups (do NOT fail on missing `GEMINI_API_KEY` or legacy `ai-artist` / `gemini-2.5-flash-image`). For HTML-to-PNG social/banner export on Windows, use Playwright/Puppeteer or Edge/Chrome headless Windows paths (never macOS `/Applications/...`). |
| **Brand Naming Separation** | `Module 05` is the **generic visual brand design framework** (creating/auditing brand systems). Existing project identities live in each workspace's local `.agents/skills/brand-*/SKILL.md` skill. |

---

## 2. Persian & RTL Visual Design Baseline (Always Active For Persian UI)

When designing Persian (`fa`) / RTL interfaces, apply these non-negotiable standards alongside the selected module:
- **Typography:** Default to verified high-craft Persian UI fonts (`Vazirmatn`, `Anjoman`/`anjoamn`, `PelakFA`, `Ravi`, `IRANSansX`, `Dana`, `Peyda`, `Yekan Bakh`). Always load `dir="rtl"` and `lang="fa"`, never rely on system Tahoma/Arial for display UI.
- **Line Height & Rhythm:** Persian script needs generous vertical breathing room — Body `line-height: 1.75–1.9`, Headings `line-height: 1.35–1.5`, crisp weight hierarchy (`400` body, `600–700` subheads/UI labels, `800` display).
- **Logical Spacing & Mirroring:** Use CSS logical properties (`margin-inline`, `padding-inline`, `text-align: start`, `inset-inline`). Mirror directional icons (arrows, chevrons, back/next, progress bars), while keeping non-directional icons (checkmarks, search, play, clocks) unmirrored.
- **Mixed BiDi & Numbers:** Keep English brand names, URLs, emails, and SKUs cleanly `dir="ltr"` inline; use tabular numerals (`font-variant-numeric: tabular-nums`) in tables, prices, and dashboards.

---

## 3. Progressive Module Router (Load ONLY What the Task Needs)

All global paths anchor at `~/.gemini/config/skills/design-master/`.

| Task Type | Load Module | Bundled Data / Scripts |
| :--- | :--- | :--- |
| **UI/UX research, palette, font pairing, UX audit, WCAG, stack guidelines** | [`modules/01-ui-ux-intelligence.md`](modules/01-ui-ux-intelligence.md) | `scripts/ui-ux/search.py`, `data/ui-ux/*` (68-file DB) |
| **Visual polish, anti-AI-slop review, bold aesthetic direction, UI microcopy** | [`modules/02-aesthetic-craft-anti-slop.md`](modules/02-aesthetic-craft-anti-slop.md) | Taste Gate & 2-pass visual critique rules |
| **Design tokens (3-layer), component specs, states/variants, token validation** | [`modules/03-design-system-and-tokens.md`](modules/03-design-system-and-tokens.md) | `scripts/tokens/*.cjs`, `templates/design-tokens-starter.json` |
| **shadcn/ui (Radix), Tailwind CSS v4 `@theme`, dark mode, responsive utilities** | [`modules/04-ui-components-and-styling.md`](modules/04-ui-components-and-styling.md) | `scripts/ui-styling/*.py`, `references/ui-styling/*` |
| **Brand guidelines, logo design (55 styles), CIP (50 items), SVG icons (15 styles)** | [`modules/05-brand-visual-identity.md`](modules/05-brand-visual-identity.md) | `scripts/brand/*.cjs`, `scripts/logo/*`, `scripts/cip/*`, `data/{logo,cip,icon}/*` |
| **Pitch decks, HTML slides, Chart.js data decks, slide copywriting** | [`modules/06-presentations-and-slides.md`](modules/06-presentations-and-slides.md) | `scripts/slides/*.py`, `data/slides/*.csv` (8 CSVs), `references/slides/*` |
| **Social photos, ad/hero/print banners (22 styles, 300 DPI), Canvas posters** | [`modules/07-banners-social-and-canvas.md`](modules/07-banners-social-and-canvas.md) | `references/graphics/banner-sizes-and-styles.md`, `canvas-design-system.md` |
| **WCAG 2.2 AA/AAA accessibility audits, keyboard focus, ARIA, screen readers** | [`modules/08-accessibility-wcag22.md`](modules/08-accessibility-wcag22.md) | `references/templates/wcag-accessibility-checklist.md` |
| **Mobile-first UX, thumb zones, Fitts' Law, iOS HIG / Android M3, RN/Flutter** | [`modules/09-mobile-ux-and-touch.md`](modules/09-mobile-ux-and-touch.md) | Touch ergonomics, platform matrix & anti-patterns |
| **Figma MCP to 1:1 production code workflow, asset & token mapping** | [`modules/10-figma-to-code-workflow.md`](modules/10-figma-to-code-workflow.md) | 7-step `get_design_context` + `get_screenshot` parity flow |

---

## 4. Universal Pre-Delivery Design Checklist

Before delivering any UI, visual spec, slide deck, or brand asset:
1. **No AI Slop:** Passed `Module 02` checks (distinct palette, clean hierarchy, zero generic SaaS template clutter, zero decorative filler).
2. **Contrast & Readability:** Text >= `4.5:1` WCAG AA, large text/UI >= `3:1`, visible keyboard focus states, `min 44x44px` mobile touch targets.
3. **Zero Overflow:** Clean responsive behavior across `375px`, `768px`, `1024px`, and `1440px` without horizontal scroll.
4. **Honest Assets:** Crisp vector icons (never emojis), real aspect ratios, no broken image placeholders, verified client brand tokens when applicable.
