# Knowledge Update Protocol Addendum — Skills 06–10

When a meaningful frontend, debugging, performance, security, or infrastructure change is completed:

1. Identify the owning project and exact deployed/source version.
2. Capture the original symptom or requirement.
3. Record evidence before changes where feasible (screenshots, trace, waterfall, logs, config export, test output).
4. Record exact files/settings changed and why.
5. Record actual tests; never invent a test result.
6. Record regressions considered and untested areas.
7. Update the relevant Skill reference and project-specific context.
8. Mark the record as CURRENTLY VERIFIED, USER-CONFIRMED, HISTORICAL, INFERRED, or UNKNOWN.
9. Add a date and source/version so later agents can judge staleness.
10. If a prior note is superseded, mark it SUPERSEDED and link to the newer record; do not silently erase history.

## Required evidence by domain
- Frontend: exact DOM/template, screenshots or design source, viewport, browser console/network, responsive and accessibility tests.
- Debugging: reproducible steps, timestamp-correlated logs, stack trace, request/response, isolated experiment, regression result.
- Performance: comparable before/after conditions, metric source, bottleneck evidence, functional regression matrix.
- Security: threat boundary, capability/permission path, validation/escaping proof, negative tests, severity evidence.
- Server: hostname/environment, backup/restore proof, DNS/SSL/server settings, deploy record, post-deploy checks, rollback.
