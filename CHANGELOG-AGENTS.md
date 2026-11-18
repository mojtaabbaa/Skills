# Agent Skills Change Log (`CHANGELOG-AGENTS.md`)

> **READ THIS FIRST (O(1) Fast Sync Protocol for All AI Agents):**
> Do **NOT** crawl the entire repository on every prompt! Read ONLY the newest entries below since your last synced commit.
> - If no entry touches your active **`Domains`**, or `Action` is `DOCS-ONLY` -> **SKIP immediately** (save tokens & time).
> - If a relevant domain changed -> read **ONLY** the paths listed under **`Changed Paths`** and merge cleanly without duplicates or downgrades.
> - **Mandatory Rule for Contributors:** Every agent that pushes any change to this repo MUST prepend a new entry at the top of this file using the standard format below.

---

## [2026-11-18] | Upgrade `elementor-architecture` (Non-Atomic Flexbox/Grid Traps, 18 Luxury Blog Patterns, Kit Safety, Render Debug & Compiler v2)
- **Agent / Role:** Elementor & Design Systems Agent
- **Domains:** `[04-elementor]`
- **Action:** `PULL-RECOMMENDED`
- **Changed Paths:**
  - `04-elementor-and-elementor-pro/skills/elementor-architecture/SKILL.md`
  - `04-elementor-and-elementor-pro/skills/elementor-architecture/extensions/01-json-ast-and-controls-schema.md`
  - `04-elementor-and-elementor-pro/skills/elementor-architecture/extensions/03-editorial-patterns-and-mcp-publish.md`
  - `04-elementor-and-elementor-pro/skills/elementor-architecture/extensions/06-visual-qa-kit-safety-and-render-debug.md`
  - `04-elementor-and-elementor-pro/skills/elementor-architecture/scripts/article_to_elementor.py`
- **Summary (1-2 lines):** Closed 10 Non-Atomic Elementor blog-design & publishing gaps: 6 silent Flexbox/Grid CSS-generator traps, Zero-Cascade & Kit 20px rules, 18 native zero-HTML editorial components (RTL timeline, pill badges, E-E-A-T expert card, decomposed cards), Single-Post Template boundary, Navigator `_title`, Global Kit corruption safety & revision recovery, `.e-con-inner` DOM diagnostics, 4-bucket render triage, and `article_to_elementor.py` v2 with built-in AST `validate()`.
- **Full Repo Check Needed?** `NO`

---

## [2026-11-18] | Add `CHANGELOG-AGENTS.md` & Team GitHub Sync Protocol
- **Agent / Role:** Skills Architect / SEO & Platform Agent
- **Domains:** `[governance]`
- **Action:** `DOCS-ONLY`
- **Changed Paths:**
  - `CHANGELOG-AGENTS.md`
  - `governance-and-protocols/GITHUB-SYNC-RULE.md`
- **Summary (1-2 lines):** Added central low-cost `CHANGELOG-AGENTS.md` change-note ledger and portable team agent sync rule (`GITHUB-SYNC-RULE.md`) so agents check updates in O(1) without full-repo crawling.
- **Full Repo Check Needed?** `NO`

---

## [2026-11-18] | Add Persian SEO Master, Upgraded Design/Elementor Masters & Full-Stack/Engineering Categories (`ecbad98`)
- **Agent / Role:** SEO, Design & Platform Engineering Agent
- **Domains:** `[04-elementor]` `[05-ui-ux]` `[07-seo]` `[08-fullstack-eng]` `[governance]`
- **Action:** `PULL-RECOMMENDED`
- **Changed Paths:**
  - `04-elementor-and-elementor-pro/skills/elementor-architecture/`
  - `05-ui-ux-and-frontend-engineering/skills/design-master/`
  - `07-seo-and-content-engineering/skills/seo-master/`
  - `08-software-engineering-and-fullstack/skills/engineering-master/`
  - `08-software-engineering-and-fullstack/skills/fullstack-web-master/`
  - `08-software-engineering-and-fullstack/skills/agent-workflow-master/`
  - `tools/validate_all_skills.py`, `MASTER-INDEX.md`, `README.md`
- **Summary (1-2 lines):** Added full 10-engine brand-agnostic Persian `seo-master` + `md_to_docx.py`, source-verified Elementor v4.2.3/Pro v4.3.2 `elementor-architecture` (with Atomic V4 `e-*`, 12 rulebooks & CLI tools), upgraded 10-module `design-master` (with full BM25 UI/UX, Slides & Branding Studio DBs + WCAG 2.2, Mobile UX & Figma-to-Code), and Category 08 (`engineering-master`, `fullstack-web-master`, `agent-workflow-master`). All 48/48 skills pass validation.
- **Full Repo Check Needed?** `NO`
