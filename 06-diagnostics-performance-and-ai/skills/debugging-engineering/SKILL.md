---
name: debugging-engineering
description: Diagnoses WordPress, PHP, WooCommerce, Elementor, AJAX, database, and plugin-conflict failures using reproducible evidence, logs, traces, and controlled isolation.
---

# Debugging Engineering

## Mission

Find the actual cause of a defect before changing code. Debugging is an evidence-gathering process, not a sequence of speculative patches. Preserve production stability, isolate the smallest failing layer, and record the root cause and proof of the fix.

## When to use this Skill

Use it for PHP Fatal/Warning/Notice errors, HTTP 400/403/404/500, broken admin operations, AJAX failures, blank product pages, WooCommerce calculation anomalies, database errors, Elementor rendering failures, plugin conflicts, regression analysis, and intermittent behavior.

Load the most relevant domain Skill too: WordPress, WooCommerce, Plugin Engineering, Filtering/AJAX, Elementor, Performance, Security, or Server Deployment.

## Evidence hierarchy

Prefer, in order:
1. Reproducible behavior in the current environment.
2. Current source, stack trace, request/response payload, and logs tied to the same timestamp.
3. Version and configuration evidence from the actual site.
4. Controlled experiments that isolate one variable.
5. Historical project notes.
6. Inference.

Do not call a suspected cause a root cause until a test distinguishes it from plausible alternatives.

## Standard triage protocol

### 1. Stabilize and define impact
- Identify production vs staging and whether customers/admins are affected.
- Determine whether the failure is continuous, intermittent, role-specific, page-specific, or action-specific.
- If production is at risk, stop further changes and capture current state.
- Do not disable broad plugin sets or alter PHP/database settings without a rollback plan.

### 2. Reproduce precisely
Record:
- Exact URL, user role, product/post ID, action sequence, and viewport.
- Date/time with timezone.
- Expected vs actual result.
- Frequency and whether a clean session reproduces it.
- Whether cache, CDN, or logged-in state changes the result.

### 3. Gather evidence
- PHP error log and WordPress debug log.
- Web server error/access logs.
- Browser console.
- Network request method, URL, payload, status, response body, and duration.
- Relevant database error and query context.
- Plugin/theme/core/PHP versions.
- Recent deploys, updates, snippets, and configuration changes.

Use the timestamp to correlate evidence. An unrelated error in the same log file is not necessarily the cause.

### 4. Build a failure boundary
Determine the first layer that fails:
- Browser/UI event
- JavaScript execution
- HTTP request construction
- CDN/WAF/web server
- PHP bootstrap
- Plugin/theme hook execution
- Database operation
- WooCommerce business logic
- Response rendering

Do not patch a downstream layer if the request never reaches it.

### 5. Isolate one variable at a time
- Compare same request with/without cache only when safe.
- Compare admin vs customer and authenticated vs guest.
- Compare one plugin/theme version at a time in staging.
- Use a minimal reproduction or temporary diagnostic logging.
- Avoid changing PHP version, memory limit, cache, and plugin versions simultaneously.
- Record each experiment and result.

### 6. Prove root cause and fix
A root-cause claim needs:
- A reproducible trigger or strong trace.
- Source line/hook/query/configuration responsible.
- An experiment that supports the causal link.
- A fix that removes the failure without introducing collateral changes.
- Regression tests for nearby behavior.

### 7. Close the incident
Report symptom, root cause, evidence, exact files/settings changed, tests run, untested areas, and rollback. Update the project-specific incident history only after facts are established.

## WordPress/PHP debugging

- Use `WP_DEBUG` and `WP_DEBUG_LOG` deliberately in staging; do not expose errors publicly.
- Check PHP-FPM/web server logs as well as `debug.log`; some fatal errors occur before WordPress logging is initialized.
- Read the complete stack trace, not only the last line.
- Confirm line numbers against the exact deployed file version.
- Distinguish memory exhaustion from an actual infinite loop or oversized query.
- Check autoload order, missing classes, incompatible method signatures, and plugin dependency checks.
- Do not suppress errors with `@` as a fix.

## AJAX and browser debugging

For each failing request capture:
- Initiating interaction and JavaScript stack.
- HTTP method, endpoint/action, payload, nonce presence (never disclose the nonce value), cookies/auth context.
- Status code, response headers, body, timing, and redirect chain.
- PHP handler/action and server log correlation.

Typical interpretation, not proof:
- 400: malformed/missing/invalid request or application validation.
- 403: authorization, nonce, WAF, host policy, or server rule.
- 404: route/action not registered, rewrite issue, or wrong endpoint.
- 500: PHP/server failure; obtain logs before changing code.
- 200 with wrong content: contract, query, rendering, or stale-response issue.

Never assume an HTTP status alone identifies the cause.

## Database debugging

- Identify exact query and connection state.
- Inspect whether a result set/cursor was fully consumed before issuing another query.
- Understand whether a plugin uses custom database access or the WordPress `$wpdb` API.
- Do not run destructive SQL while diagnosing.
- Back up before repairing data.
- Treat table prefixes and option names as site-specific.

## Plugin/theme conflict debugging

- Inspect hooks and execution order.
- Check duplicate callbacks and multiple integrations handling the same event.
- Compare theme-native and custom plugin request flows.
- Use staging or a narrowly scoped diagnostic toggle.
- Do not edit vendor/third-party files as a permanent fix.

## Historical incident register

See `references/historical-incidents.md`. These entries are symptoms and observations only. Their root causes are not established unless explicitly stated there.

## Required incident report format

Use `references/incident-report-template.md`. Maintain an explicit distinction between CONFIRMED ROOT CAUSE, LIKELY CAUSE, and UNRESOLVED HYPOTHESIS.

## Anti-patterns

- Applying a generic fix based only on an error string.
- Treating correlation as causation.
- Disabling security, WAF, or all plugins in production as a first step.
- Increasing memory limits without checking why memory is exhausted.
- Changing multiple variables in one experiment.
- Claiming resolution without retesting the original reproduction steps.
