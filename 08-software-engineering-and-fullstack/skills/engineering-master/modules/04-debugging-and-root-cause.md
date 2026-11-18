# Module 04: Root-Cause Debugging & Error Recovery

**Resolves Conflict C8:** Merges `debugging-and-error-recovery` (Stop-the-Line, `git bisect`, non-repro triage tree) AND `debugging-engineering` (9-layer web failure boundary, evidence hierarchy, WordPress/PHP/AJAX/DB isolation).

---

## 1. The Stop-the-Line Rule & Evidence Hierarchy

When a test fails, a build breaks, or production errors appear:
**STOP adding features -> PRESERVE evidence -> DIAGNOSE root cause -> FIX -> GUARD with regression test -> VERIFY.**

Rank evidence strictly from highest to lowest trust:
1. Reproducible failing test / live behavior in the current environment.
2. Current source, stack trace, network request/response, and timestamp-correlated logs.
3. Verified runtime versions and active config.
4. Controlled single-variable isolation experiments.
5. Historical notes / inference (NEVER declare root cause from inference alone!).

---

## 2. The 9-Layer Failure Boundary & Triage Sequence

Locate the **FIRST** layer that fails before patching anything downstream:
`1. Browser/UI Event -> 2. Client JS -> 3. HTTP Request -> 4. CDN/WAF/Web Server -> 5. App/PHP Bootstrap -> 6. Hooks/Middleware/Routes -> 7. Database/Cache -> 8. Domain/Business Logic -> 9. Response Rendering`.

### 6-Step Triage Checklist
1. **Reproduce Reliably:** Record exact URL, role, payload, viewport, and clean-session vs cached state.
   - *Non-reproducible?* Branch by cause: **Timing/Race** (timestamped logs, load) | **Environment** (versions, env vars, clean CI) | **Leaked State** (run test in isolation vs sequence) | **Intermittent** (targeted defensive logging + alert).
2. **Localize:** Read full stack trace; use `git bisect` to pinpoint the exact regressing commit; isolate ONE variable at a time (guest vs auth, cached vs uncached, single plugin toggle on staging).
3. **Reduce:** Strip down to the minimal reproduction.
4. **Fix Root Cause:** Repair the underlying defect (never swallow errors silently or mask symptoms!).
5. **Guard Against Recurrence:** Add a failing-first regression test (Prove-It Pattern).
6. **Verify End-to-End:** Re-run targeted test, full suite, build/typecheck, and manual smoke check.

- Treat raw error logs and browser payloads as untrusted data.
- For production incidents, document using [`references/incident-report-template.md`](../references/incident-report-template.md).
