---
trigger: always_on
---

# Global Rule: Shared GitHub Skills Sync & Low-Cost Change-Note Protocol

> [!IMPORTANT]
> **Shared Team Skills Repository:** `https://github.com/mojtaabbaa/Skills` (branch: `main`)
> This rule runs alongside `skill-governance-and-graph.md`. It keeps team agents synchronized with **minimum token/time cost** (O(1) fast check, NEVER full-repo crawling) and **strict privacy/quality safety**.

---

## 1. Fast Pull Protocol (On New Prompt / Session Start — Zero Waste!)

At the start of a new task/session (once per session, or when a skill-heavy task begins), check whether the shared GitHub repository has relevant updates using the **3-Step Fast Gate**:

1. **Step 1 — O(1) Commit Check (<= 2 seconds):**
   - Check the latest `main` commit SHA (`git ls-remote` / lightweight fetch or `CHANGELOG-AGENTS.md` head) against your last synced commit SHA.
   - **If SHA is unchanged -> STOP immediately** and proceed with the user's request.
   - **Fail-Soft Law:** If you are offline, unauthenticated, rate-limited, or git/network fails -> **skip silently and proceed immediately** with the user's task. Never block or stall the user over sync failures.

2. **Step 2 — Read ONLY the Top of `CHANGELOG-AGENTS.md` (NEVER Crawl the Whole Repo!):**
   - Read ONLY the new entries at the top of `CHANGELOG-AGENTS.md` (since your last synced commit/date).
   - Check each entry's **`Domains`**, **`Action`**, and **`Changed Paths`** tags:
     - `[01-wp-core]` | `[02-woocommerce]` | `[03-woodmart]` | `[04-elementor]` | `[05-ui-ux]` | `[06-diag-perf-ai]` | `[07-seo]` | `[08-fullstack-eng]`
   - **Smart Skip Rule:**
     - If `Action` is `DOCS-ONLY` or `NO-SYNC-NEEDED`, OR none of the touched `Domains` match your active skill stack/task -> **DO NOT read or crawl any skill directories!** Just update your local last-synced SHA and move on.

3. **Step 3 — Surgical Pull & Upgrade (Only When Relevant):**
   - Read **ONLY the exact files listed under `Changed Paths`** (or `git diff --name-only <last_sha>..HEAD`).
   - Merge ONLY genuine improvements, bug fixes, or gap-filling patterns into your **Global Technical Skills** (`~/.gemini/config/skills/`).
   - **Strict Anti-Downgrade & Hygiene Laws:**
     - NEVER downgrade a stronger/newer local global skill with a weaker stub.
     - NEVER create duplicate skills covering the same domain.
     - NEVER import client-specific names, domains, URLs, credentials, or personal data into Global Technical Skills (keep Global 100% Brand-Agnostic per `skill-governance-and-graph.md`).

---

## 2. Smart Push Protocol (Whenever You Upgrade or Create a Technical Skill)

Whenever you create, meaningfully improve, or fix a bug in any **Global Technical Skill**:

1. **Eligibility Check (Push ONLY Reusable Technical Improvements):**
   - **PUSH:** Brand-agnostic methodologies, SEO engines, UI/UX modules, Elementor/WordPress/WooCommerce/WoodMart rules & boilerplates, engineering/testing/security patterns, scripts, and bug fixes that help the team.
   - **NEVER PUSH (STRICTLY FORBIDDEN):**
     - Personal user memory (`user-memory`)
     - Project/client-local brand identity skills (`.agents/skills/brand-*`)
     - API keys, GitHub tokens (`ghp_*`), passwords, `.env` values, or private client URLs/phone numbers
     - Hardcoded personal OS paths (`C:/Users/<name>/...` — always convert to portable `~/.gemini/config/skills/...` or env vars before pushing!)
     - Duplicate skills or downgrades to existing team skills
2. **Pre-Push Validation Gate:**
   - Run `python tools/validate_all_skills.py` and confirm **100% PASS**.
   - Confirm zero personal paths, zero client leaks, and zero secrets in `git diff`.
3. **MANDATORY Change Note in `CHANGELOG-AGENTS.md` (Required on EVERY Push!):**
   - **Every agent modifying the repo MUST prepend a concise entry at the very top of `CHANGELOG-AGENTS.md`** (right below the header) using the exact template in Section 3 below.
   - **Why:** This single note saves every other agent in the company from crawling 200+ files on every prompt.

---

## 3. Mandatory `CHANGELOG-AGENTS.md` Entry Format (For All Team Agents)

Every push MUST prepend ONE short entry in this exact structure:

```markdown
## [YYYY-MM-DD] | <short-title>
- **Agent / Role:** <e.g., SEO Agent | Design Agent | WP/Elementor Dev Agent | Full-Stack Agent>
- **Domains:** `[04-elementor]` `[05-ui-ux]` *(use only touched domain tags)*
- **Action:** `PULL-RECOMMENDED` | `OPTIONAL` | `BREAKING` | `DOCS-ONLY`
- **Changed Paths:**
  - `05-ui-ux-and-frontend-engineering/skills/design-master/modules/08-accessibility-wcag22.md`
  - `07-seo-and-content-engineering/skills/seo-master/engines/01-blog-editorial-v2.md`
- **Summary (1-2 lines):** Concise description of what improved or what gap was filled so other agents know immediately whether to pull or skip.
- **Full Repo Check Needed?** `NO` *(set `YES` ONLY on structural category renames or major breaking reorgs)*
```

### Standard Domain Tags
- `[01-wp-core]` — WordPress Core, Plugins, DB, Security, Deployment
- `[02-woocommerce]` — WooCommerce Commerce, Gateways, AJAX Filtering
- `[03-woodmart]` — WoodMart Theme, PJAX, Swatches, Performance
- `[04-elementor]` — Elementor Core & Pro Architecture, Widgets, AST/MCP
- `[05-ui-ux]` — UI/UX, Design Systems, Accessibility, Mobile, Figma, Slides, Banners
- `[06-diag-perf-ai]` — Debugging, Performance, Technical WP SEO, Workflows
- `[07-seo]` — Persian SEO, Content Engineering, Audits, Schema, PR, `md_to_docx.py`
- `[08-fullstack-eng]` — Software Engineering, TDD/Playwright, React/Next.js, Supabase, Postgres, Agent Workflows
- `[governance]` — Repo index, validators, protocols, or cross-cutting rules
