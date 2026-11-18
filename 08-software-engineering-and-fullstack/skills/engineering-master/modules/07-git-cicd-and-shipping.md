# Module 07: Git Workflow, CI/CD & Production Launch Discipline

Consolidated from `git-workflow-and-versioning`, `ci-cd-and-automation`, and `shipping-and-launch`.

---

## 1. Git Workflow & Atomic Commit Standards

- **Trunk-Based Development:** Keep `main` always deployable; use short-lived focused feature branches (`feat/...`, `fix/...`, `refactor/...`).
- **Atomic, Focused Commits:** Each commit represents one coherent, compilable change (never mix unrelated formatting, refactors, and feature changes in one commit!).
- **Intent-Driven Commit Messages:** Explain *why* the change was made, not merely what the diff already shows.
- **Clean History & Safety:** Inspect `git status` and `git diff` before staging; NEVER commit `.env`, secrets, build artifacts, or scratch logs; NEVER force-push shared `main` branches.

---

## 2. CI/CD Quality Gate Pipeline

Automate fast-to-slow verification gates on every PR:
1. **Static Gates (Fast):** Lint, format check, TypeScript `tsc --noEmit` / `php -l`, dependency lockfile audit.
2. **Automated Tests:** Unit tests -> integration/DB tests -> critical-path E2E (`Playwright`) + preview deployment.
3. **Build & Artifact Verification:** Confirm production build succeeds cleanly (and for WordPress plugins, validate forward-slash ZIP structure).
4. **Feedback Loop:** Pipe concrete failing CI logs directly back to fix root causes rather than bypassing checks.

---

## 3. Production Shipping & Staged Rollout Checklist

Before launching any major release or migration:
- [ ] **Code & Tests:** Green CI, clean diff review, rollback tested.
- [ ] **Security:** Secrets in env/vault, headers/RLS/permissions verified, dependency audit clean.
- [ ] **Performance & Accessibility:** CWV baseline checked, responsive mobile/desktop & RTL verified.
- [ ] **Observability:** Structured logging, error tracking, and health endpoint active.
- [ ] **Staged Rollout:** Use feature flags / canary percentages (`internal -> 5% -> 25% -> 100%`) with explicit abort thresholds (error-rate spike or latency regression -> instant flag off / rollback).
- [ ] **Human Sign-Off:** Obtain explicit user confirmation before pushing live production deploys or irreversible DB migrations.
