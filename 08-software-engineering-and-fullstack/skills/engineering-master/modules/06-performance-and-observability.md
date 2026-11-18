# Module 06: Performance Optimization & Observability

**Resolves Conflict C7 (Universal Layer):** Consolidated from `performance-optimization` + `observability-and-instrumentation` (pairs with `wordpress-master/modules/08` for WP/Woo caching and `fullstack-web-master/modules/01` for React/Next.js).

---

## 1. Core Web Vitals & Measurement Workflow

| Metric | Good | Needs Improvement | Poor |
| :--- | :---: | :---: | :---: |
| **LCP** (Largest Contentful Paint) | `<= 2.5s` | `<= 4.0s` | `> 4.0s` |
| **INP** (Interaction to Next Paint) | `<= 200ms` | `<= 500ms` | `> 500ms` |
| **CLS** (Cumulative Layout Shift) | `<= 0.1` | `<= 0.25` | `> 0.25` |

### Strict 5-Step Optimization Loop
1. **MEASURE:** Establish baseline using BOTH Synthetic (Lighthouse / DevTools Performance Trace) and RUM (`web-vitals` / CrUX). Never optimize on guesses.
2. **IDENTIFY:** Isolate the real bottleneck (N+1 DB query, blocking JS long task, unoptimized LCP image, bundle bloat `> 200KB gzip`, missing cache).
3. **FIX ONE THING:** Change one meaningful variable cleanly.
4. **VERIFY (`"Neutral = Revert"` Rule):** Re-measure under identical conditions. If the optimization produces no measurable win, **REVERT it** so you don't keep unnecessary complexity! Log every attempt (including reverted ones) in `PERF.md` or the PR description.
5. **GUARD:** Add Lighthouse CI, bundle-size checks, or query count assertions against regressions.

Deep anti-pattern catalog: [`references/optimization-patterns.md`](../references/optimization-patterns.md).

---

## 2. Observability & Instrumentation Discipline

1. **Define "Working" First:** Know exact SLOs (latency p95/p99, error rate, throughput) before adding telemetry.
2. **Pick the Right Signal:**
   - **Structured Logs (JSON):** Discrete events with correlation/request IDs, user/tenant ID (NEVER secrets or raw PII!).
   - **Metrics:** Counters, gauges, and histograms for dashboards & burn-rate alerts (keep label cardinality bounded — never put raw user IDs or URLs as metric labels!).
   - **Distributed Traces:** Propagate trace context across async queues, RPCs, and external calls.
3. **Actionable Alerts Only:** Every alert must tie to a real user-facing symptom and link to a concise runbook (zero noisy vanity alerts).
4. **Verify Telemetry:** Trigger an intentional error/request in staging to prove logs, metrics, and alerts actually fire before shipping.
