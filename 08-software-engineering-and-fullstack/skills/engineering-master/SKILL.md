---
name: engineering-master
description: >-
  Unified global Software Engineering, Architecture, Quality, Testing, Debugging, Security,
  Performance & DevOps Master Skill merging task planning & vertical slicing, stable API/interface
  design & ADRs, 5-axis code review & Chesterton's Fence simplification, deprecation & migration,
  TDD & Playwright/DevTools browser QA (with `with_server.py`), Stop-the-Line root-cause
  debugging, OWASP/STRIDE/LLM05 security hardening, CWV/RUM performance & observability, and
  trunk-based Git, CI/CD & staged rollout shipping.
---

# Engineering Master — Unified Global Software Engineering & Operations Engine

Language- and framework-agnostic engineering standard governing planning, architecture, APIs, code review, refactoring, testing, root-cause debugging, security hardening, performance, observability, Git, CI/CD, and production launches.

Pair with platform specialists when relevant: [`wordpress-master`](../wordpress-master/SKILL.md), [`elementor-architecture`](../elementor-architecture/SKILL.md), or [`fullstack-web-master`](../fullstack-web-master/SKILL.md).

---

## Progressive Module Router (Load ONLY What the Task Needs)

| Engineering Need | Load Module | Bundled References / Scripts |
| :--- | :--- | :--- |
| **Task breakdown, vertical slicing, API contracts, ADRs & architecture governance** | [`modules/01-planning-architecture-and-apis.md`](modules/01-planning-architecture-and-apis.md) | `references/adr-template.md` |
| **5-axis code review, safe simplification, refactoring & deprecation/migration** | [`modules/02-code-review-simplification-and-migration.md`](modules/02-code-review-simplification-and-migration.md) | `references/change-review-and-release-checklist.md` |
| **TDD (Red-Green-Refactor), Playwright E2E (`with_server.py`) & DevTools QA** | [`modules/03-testing-tdd-and-browser-qa.md`](modules/03-testing-tdd-and-browser-qa.md) | `scripts/with_server.py`, `examples/*` |
| **Root-cause debugging (Stop-the-Line, 9-layer failure boundary, `git bisect`)** | [`modules/04-debugging-and-root-cause.md`](modules/04-debugging-and-root-cause.md) | `references/incident-report-template.md` |
| **STRIDE threat modeling, OWASP Top 10, 3-tier boundaries, SSRF, supply chain & LLM05** | [`modules/05-security-and-hardening.md`](modules/05-security-and-hardening.md) | `references/hardening-patterns.md` |
| **CWV/RUM performance (`Neutral = Revert`, `PERF.md`) & structured observability** | [`modules/06-performance-and-observability.md`](modules/06-performance-and-observability.md) | `references/optimization-patterns.md` |
| **Trunk-based Git, atomic commits, CI/CD gates, feature flags & staged launch** | [`modules/07-git-cicd-and-shipping.md`](modules/07-git-cicd-and-shipping.md) | — |

---

## Universal Engineering Non-Negotiables

1. **Evidence Before Assertion:** Never claim a bug is fixed, a test passes, or performance improved without actual executed command output or measurements.
2. **Smallest Verifiable Slice:** Deliver thin, compilable, tested vertical slices rather than sprawling unverified rewrites.
3. **Stop-the-Line on Failures:** When a test or build fails unexpectedly, stop adding features, preserve evidence, find the root cause, fix it, and add a regression guard before resuming.
4. **Human Approval for High-Risk Actions:** Always confirm before production deploys, destructive migrations, auth/permission rewrites, or data deletion.
