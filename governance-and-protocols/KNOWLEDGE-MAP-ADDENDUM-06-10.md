# Knowledge Map Addendum — Skills 06–10

This addendum extends the first five-skill WordPress Engineering Knowledge Pack. It does not replace the original `KNOWLEDGE-MAP.md`.

| Skill | Main scope | Load alongside |
|---|---|---|
| `frontend-engineering` | HTML/CSS/JS, responsive UI, RTL/LTR, accessibility, Elementor frontend lifecycle | Elementor, WooCommerce, Filtering, Performance |
| `debugging-engineering` | Evidence-first diagnosis, logs, stack traces, HTTP/AJAX/database/plugin failures | The domain Skill for the failing subsystem |
| `performance-engineering` | CWV, frontend/backend profiling, assets, caching, query cost | Frontend, WordPress, WooCommerce, Elementor, Server |
| `wordpress-security-engineering` | Authz, validation, escaping, SQL, AJAX/REST, uploads, commerce trust | WordPress, Plugin, WooCommerce, Server, Debugging |
| `server-deployment-engineering` | Hosting, DNS, SSL, PHP/database config, migrations, backup, deployment | Debugging, Security, Performance, Plugin |

## Routing principles
- A visual defect uses Frontend + the relevant builder/theme Skill.
- A slow interaction uses Performance + Frontend + the relevant backend/query Skill.
- A 403/500 or fatal error uses Debugging + the affected subsystem Skill; add Security/Server when evidence points to those layers.
- A deployment or migration uses Server + Plugin/WordPress; add Security and Debugging for permission or runtime incidents.
- A security-sensitive code change uses Security + the domain Skill that owns the endpoint or business rule.

## Boundary principle
Do not load every Skill for every task. Load the narrowest set that covers the behavior and its trust/performance/deployment boundaries. Current source and the user's latest explicit instruction outrank historical notes.
