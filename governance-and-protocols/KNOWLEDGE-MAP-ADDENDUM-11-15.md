# Knowledge Map Addendum — Skills 11–15

Pack: Skills 11–15, version 1.3.0.

## Complete 15-skill index

| # | Skill | Primary domain | Typical dependencies |
|---:|---|---|---|
| 01 | `wordpress-development-architecture` | WordPress APIs, hooks, lifecycle, roles | 03, 09, 11, 15 |
| 02 | `woocommerce-engineering` | Products, pricing, cart, checkout, orders | 03, 11, 12, 15 |
| 03 | `custom-wordpress-plugin-engineering` | Plugin structure, lifecycle, settings, releases | 01, 02, 09, 11, 15 |
| 04 | `advanced-woocommerce-filtering-ajax` | Product filter/query/AJAX | 02, 06, 08, 11, 15 |
| 05 | `elementor-theme-integration` | Builder/theme integration | 02, 06, 08, 12 |
| 06 | `frontend-engineering` | CSS, JS, responsive UI, accessibility | 04, 05, 08, 09 |
| 07 | `debugging-engineering` | Incident analysis and root cause | Relevant domain Skill(s) |
| 08 | `performance-engineering` | Runtime, query, assets, Core Web Vitals | 04, 06, 11, 10 |
| 09 | `wordpress-security-engineering` | Trust boundaries, auth, validation, privacy | 01, 02, 03, 11, 12, 10 |
| 10 | `server-deployment-engineering` | Hosting, DNS, PHP, deployment | 08, 09, 15 |
| 11 | `database-data-architecture` | Persistence, schema, query, cache | 01, 02, 03, 08, 09 |
| 12 | `business-logic-workflow-automation` | State machines, approvals, bookings, side effects | 02, 03, 05, 09, 11 |
| 13 | `seo-technical-wordpress` | Crawl, canonical, schema, sitemap | 01, 05, 06, 08 |
| 14 | `ai-assisted-development` | Agent operation, context, delegation, MCP | All relevant Skills; especially 15 |
| 15 | `software-architecture-code-governance` | Architecture decisions, change control, releases | All affected Skills |

## Skill selection rule

Load one primary Skill and only the supporting Skills whose domain is materially affected. Load Skill 15 for cross-module/refactor/release decisions; load Skill 07 for active incidents; load Skill 14 for agent orchestration/context transfer. Do not preload all 15 Skills by default.

## Knowledge layers

- Skills: reusable methods and guardrails.
- Knowledge references: historical project patterns and templates.
- Project context: current repository facts and active constraints.
- ADRs: durable design decisions and trade-offs.
- Incident reports: failures, evidence, root causes, verified fixes.
- Release records: versions, source commit, package, tests, rollback.

A historical discussion must never overwrite a currently verified repository fact.
