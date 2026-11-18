# Module 06: Unified Presentations & Strategic HTML Slides Engine

**Resolves Conflict C1 (3-Way Slides Fragmentation):** Merges all three previously fractured slide implementations into ONE cohesive engine:
1. The **8 BM25 Slide Decision CSVs** + Python search/generator/validator scripts (formerly buried inside `design-system`).
2. The **Chart.js HTML Presentation Template, Layout Patterns, Copywriting Formulas (AIDA/PAS/FAB), and Slide Strategies** (formerly duplicated byte-for-byte between `slides` and `design`).

---

## 1. The 8-Database BM25 Slide Intelligence Engine (`data/slides/*.csv`)

Query the global slide decision engine before designing any deck (pitch deck, investor deck, sales deck, product launch, keynote, quarterly review):

```bash
# Search slide strategy, layouts, typography, color logic, copywriting, or Chart.js chart types
python "~/.gemini/config/skills/design-master/scripts/slides/search-slides.py" "investor pitch SaaS growth" --domain strategy
python "~/.gemini/config/skills/design-master/scripts/slides/search-slides.py" "revenue comparison metrics" --domain chart
python "~/.gemini/config/skills/design-master/scripts/slides/search-slides.py" "problem solution split" --domain layout
python "~/.gemini/config/skills/design-master/scripts/slides/search-slides.py" "persuasive hook CTA" --domain copy
```

**Available Slide Databases (`data/slides/`):**
- `slide-strategies.csv` — Deck archetypes & narrative arcs
- `slide-layouts.csv` & `slide-layout-logic.csv` — Structural slide grids & visual flow rules
- `slide-charts.csv` — 25 Chart.js visualization mappings (bar, line, doughnut, radar, waterfall, KPI cards)
- `slide-copy.csv` — High-impact headlines & copywriting formulas (AIDA, PAS, FAB, Rule of 3)
- `slide-typography.csv` — Slide display/body/KPI sizing hierarchy
- `slide-color-logic.csv` — High-contrast dark/light slide palette rules
- `slide-backgrounds.csv` — Atmospheric background treatment logic

---

## 2. Automated Slide Generation & Token Validation

All slide scripts resolve `assets/design-tokens.*` and output paths relative to the **active project workspace (`Path.cwd()`)**:

```bash
# Generate a token-compliant HTML slide deck from structured specs
python "~/.gemini/config/skills/design-master/scripts/slides/generate-slide.py" --help

# Validate generated HTML slides against design tokens (zero raw unapproved hex/spacing)
python "~/.gemini/config/skills/design-master/scripts/slides/slide-token-validator.py" <slide.html>
python "~/.gemini/config/skills/design-master/scripts/slides/html-token-validator.py" <slide.html>

# Fetch curated stock slide background visuals
python "~/.gemini/config/skills/design-master/scripts/slides/fetch-background.py" --help
```

---

## 3. Core Slide Design Laws (Non-Negotiable)

1. **One Core Idea Per Slide:** Never cram 2 competing messages onto one frame. Max 3–5 scannable points or 1 focal chart + 1 takeaway headline.
2. **Chart.js Data Clarity:** Use crisp Chart.js canvases with legible axis labels, highlighted focal series (1 brand accent color vs muted neutral comparison series), and concise annotation callouts.
3. **Viewport-Locked 16:9 Discipline:** Every slide renders cleanly at `1920x1080` (and degrades smoothly on smaller viewports) with zero clipped text, generous safe margins (`>= 64px`), and keyboard navigation (`ArrowRight`/`ArrowLeft`/`Space`).
4. **Persian RTL Decks:** Set `dir="rtl" lang="fa"`, load `Vazirmatn` / `Anjoman` / brand font, align charts/legends cleanly for RTL readers, and use Persian numerals where appropriate.
5. **Anti-Slop Pass (`Module 02`):** Avoid repetitive bullet walls; alternate visual rhythm (Hero -> Metric Scorecard -> Split Visual -> Chart -> Comparison -> Closing CTA).

---

## 4. Deep Slide References (De-Duplicated Canonical Set)

- [`references/slides/slides-html-template.md`](../references/slides/slides-html-template.md) — Full self-contained HTML5 + Chart.js presentation scaffold
- [`references/slides/slides-layout-patterns.md`](../references/slides/slides-layout-patterns.md) — Hero, Split, Bento/Grid, Comparison, Timeline, Quote, KPI layouts
- [`references/slides/slides-copywriting-formulas.md`](../references/slides/slides-copywriting-formulas.md) — AIDA, PAS, FAB, Before-After-Bridge slide copy frameworks
- [`references/slides/slides-strategies.md`](../references/slides/slides-strategies.md) — Strategic sequencing by audience & presentation goal
