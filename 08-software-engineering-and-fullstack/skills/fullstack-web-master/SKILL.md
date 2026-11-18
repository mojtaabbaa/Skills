---
name: fullstack-web-master
description: >-
  Unified global Modern Full-Stack Web Engineering Master Skill merging official Vercel React &
  Next.js performance guidelines (72 prioritized rules across waterfalls, bundle size, SSR/RSC,
  re-renders, and hydration), official Supabase platform engineering (CLI, MCP, Auth, RLS, Edge
  Functions, Realtime, Storage, declarative & imperative migrations), and official Supabase
  Postgres Best Practices (33 deep rules across indexing, RLS performance, locking, connection
  pooling, pagination, and EXPLAIN ANALYZE). Activate ONLY in React/Next.js/Supabase/Postgres
  projects (NEVER in WordPress/Elementor workspaces).
---

# Fullstack Web Master — React, Next.js, Supabase & PostgreSQL Engineering

Single global source of truth for modern TypeScript/React/Next.js and Supabase/PostgreSQL application engineering.

> [!IMPORTANT]
> **Stack Activation Guard:** Activate this skill **ONLY** in modern React, Next.js, TypeScript, Supabase, or PostgreSQL projects. NEVER apply React/Next.js/Supabase patterns to WordPress/PHP/Elementor sites!

---

## Progressive Module Router (Load ONLY What the Task Needs)

| Domain | Load Module | Preserved Official Rulebases |
| :--- | :--- | :--- |
| **React & Next.js Performance (Waterfalls, Bundles, RSC, Re-renders, Hydration)** | [`modules/01-vercel-react-nextjs.md`](modules/01-vercel-react-nextjs.md) | `references/vercel-react-rules/*` (All **72** official Vercel rules) |
| **Supabase Platform (CLI, MCP, Auth, Storage, Realtime, Edge Functions, Migrations)** | [`modules/02-supabase-platform.md`](modules/02-supabase-platform.md) | Official Supabase workflow & schema change protocols |
| **PostgreSQL Architecture, Indexing, RLS Performance, Locking & Connection Pooling** | [`modules/03-postgres-best-practices.md`](modules/03-postgres-best-practices.md) | `references/postgres-rules/*` (All **33** official Supabase Postgres rules) |

---

## High-Priority Cross-Cutting Rules (Always Enforce)

1. **Eliminate Async Waterfalls First (`CRITICAL`):** Start independent promises early (`Promise.all()`), defer `await` into branches where needed, and stream slow subtrees with React `<Suspense>`.
2. **Avoid Barrel-File Bundle Bloat (`CRITICAL`):** Import directly from concrete icon/component paths or configure `optimizePackageImports`; dynamic-import heavy client charts/editors.
3. **Database & RLS Discipline (`CRITICAL`):** Always enable Row-Level Security (RLS) on user-facing Postgres tables, index every column referenced in RLS policies & foreign keys, wrap `auth.uid()` inside `(SELECT auth.uid())` for per-statement evaluation, and verify heavy queries with `EXPLAIN (ANALYZE, BUFFERS)`.
4. **Verify Before Shipping:** Pair with [`engineering-master`](../engineering-master/SKILL.md) for TDD, Playwright E2E testing, STRIDE security checks, and CI/CD gates.
