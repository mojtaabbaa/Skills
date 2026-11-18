# Module 07: Banners, Social Photos & Canvas Art Direction

**Resolves Conflicts C2, C6, C7 & C8:** Unifies `banner-design`, `design`'s banner & social-photos workflows, and `ui-styling`'s `canvas-design-system.md` into one conflict-free visual graphics module — wired cleanly to **Antigravity's native `image-generator` subagent** and **Windows-safe HTML-to-PNG export**.

---

## 1. Mode Selection (Pick the Right Mode First)

| Mode | When to Use | Primary Production Pipeline |
| :--- | :--- | :--- |
| **A. Digital & Print Banners (22 Styles)** | Website hero banners, Google/Meta ad sets, social covers (YouTube/LinkedIn/X/FB), print roll-ups/posters (`300 DPI`, CMYK, bleed) | Brand tokens + 22 art styles ([`banner-sizes-and-styles.md`](../references/graphics/banner-sizes-and-styles.md)) -> **`image-generator`** subagent OR pixel-exact HTML/CSS -> PNG |
| **B. Social Photos (HTML -> Retina PNG)** | Crisp typography-heavy Instagram posts (`1080×1080`), Carousels (`1080×1350`), Stories/Reels (`1080×1920`), YouTube thumbnails (`1280×720`), LinkedIn/X cards | Self-contained fixed-viewport HTML/CSS (brand fonts & colors, 80% central safe zone) -> headless browser / Playwright screenshot export |
| **C. Canvas Art Direction (`90% Visual / 10% Text`)** | Posters, visual manifestos, exhibition pieces, coffee-table book pages, conceptual brand art | 2-phase Canvas manifesto + museum-grade composition ([`canvas-design-system.md`](../references/graphics/canvas-design-system.md)). **NEVER apply to dashboards or text-heavy web apps!** |

---

## 2. Canonical Platform & Print Dimensions

### Social Media & Content Graphics
| Platform | Format | Size (px) | Ratio | Safe Zone / Notes |
| :--- | :--- | :---: | :---: | :--- |
| **Instagram** | Square Post | `1080 × 1080` | `1:1` | Keep key text in central 80%; visual-first (`<20%` text) |
| **Instagram** | Carousel / Portrait | `1080 × 1350` | `4:5` | Highest mobile feed real estate |
| **Instagram / TikTok / Reels** | Story / Cover | `1080 × 1920` | `9:16` | Keep top `250px` & bottom `340px` clear of UI overlays |
| **YouTube** | Thumbnail | `1280 × 720` | `16:9` | Readable at 50% thumbnail zoom; high contrast focal point |
| **YouTube** | Channel Banner | `2560 × 1440` | `16:9` | Safe text zone: central `1546 × 423` |
| **LinkedIn / Facebook** | Feed Post / OG Card | `1200 × 630` | `~1.91:1` | Crisp editorial headline + clean data/brand visual |
| **X (Twitter)** | Post Image | `1200 × 675` | `16:9` | Test contrast in both light & dark feed modes |
| **Pinterest** | Pin | `1000 × 1500` | `2:3` | Vertical editorial visual + concise title overlay |
| **Web Hero** | Desktop / Mobile | `1920 × 800` / `750 × 1000` | Wide / Tall | Reserve clear negative space for H1 + CTA contrast |

### Print Banner Specifications (Preserved From `banner-design`)
- **Resolution:** Strictly `300 DPI` minimum at final physical dimensions (`150 DPI` acceptable only for large-format outdoor banners viewed > 2m away).
- **Color Profile:** Specify **CMYK** print conversion notes (avoid neon RGB colors that wash out in CMYK).
- **Bleed & Safe Margin:** Include `3mm–5mm` bleed on all sides (`10mm+` for roll-ups/billboards); keep all logos/text inside safe margin.

---

## 3. Antigravity-Native Rendering & Windows Export Pipeline

### Path 1: AI-Generated Art / Photography / Hero Banners
- Delegate directly to Antigravity's native **`image-generator`** subagent (`invoke_subagent`, `TypeName: "image-generator"`).
- Include exact aspect ratio, brand palette hex codes, chosen art direction style (from the 22 styles in `banner-sizes-and-styles.md`), lighting/material cues, and explicit text-free or clean-negative-space instruction when Persian typography will be overlaid via HTML/CSS.
- **Brand Guardrail:** NEVER generate AI photography for real facilities when the active workspace's local brand skill forbids AI photography of real facilities.

### Path 2: Pixel-Exact HTML/CSS -> PNG Export (Windows-Safe — Fixed Conflict C7)
For Persian typography banners & Instagram carousels where pixel-crisp Persian fonts (`Vazirmatn`, `Anjoman`, `PelakFA`, `Ravi`) are essential:
1. Build self-contained HTML with exact `width`/`height`, `overflow: hidden`, `dir="rtl" lang="fa"`, and embedded brand CSS tokens.
2. Export via **Playwright** (`deviceScaleFactor: 2` for 2× Retina sharpness, wait `networkidle` + font load) OR **Windows Chrome/Edge Headless**:

```powershell
# Windows Edge or Chrome headless screenshot (replaces broken macOS /Applications path!)
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" `
  --headless --disable-gpu --hide-scrollbars `
  --window-size=1080,1080 --virtual-time-budget=5000 `
  --screenshot="output.png" "file:///C:/path/to/design.html"
```

3. **Visual QA Pass:** Inspect every exported PNG using Antigravity's `read_file` tool (verify Persian font rendered, zero clipping, WCAG AA `>= 4.5:1` contrast, balanced safe zone). Fix HTML and re-export until flawless.

---

## 4. Deep Graphics References (Load On Demand)

- [`references/graphics/banner-sizes-and-styles.md`](../references/graphics/banner-sizes-and-styles.md) — Complete platform dimension specs & all 22 art direction styles
- [`references/graphics/canvas-design-system.md`](../references/graphics/canvas-design-system.md) — 5 visual art movements (Concrete Poetry, Chromatic Language, Analog Meditation, Organic Systems, Geometric Silence) & 2-pass museum-grade refinement protocol
