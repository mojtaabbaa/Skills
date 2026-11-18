# Module 03: Adversarial Doubt-Driven Review & Multi-Agent Safety

Consolidated from `doubt-driven-development` + `ai-assisted-development` delegation safety rules.

---

## 1. The 4-Step Doubt-Driven Development (DDD) Loop

Use before finalizing high-stakes architectural plans, security-critical implementations, database migrations, or tricky bug fixes:

1. **CLAIM — Surface What Stands:** Explicitly list your design decision, key assumptions, invariants, and edge cases.
2. **EXTRACT — Smallest Reviewable Unit:** Package only the concrete diff/spec + explicit contract (never dump the whole noisy chat history so the reviewer isn't biased by your sunk-cost rationale!).
3. **DOUBT — Fresh-Context Adversarial Review:** Run a fresh-context review (e.g., a clean read-only subagent or isolated review pass) instructed strictly to **find flaws, missing edge cases, race conditions, security gaps, and broken invariants** — NOT to praise the code.
4. **RECONCILE — Fold Findings Back:** For every valid objection, fix the design/code and re-verify with tests; for rejected objections, record clear technical evidence why the invariant holds.

---

## 2. Multi-Agent & Tool Delegation Guardrails

- **Least Privilege:** Read-only research/review agents never receive write/deploy authority.
- **No Silent Irreversible Actions:** Subagents must NEVER silently deploy to production, delete data, run destructive migrations, or alter user permissions without parent/human authorization.
- **Honest Verification:** Distinguish executed checks from unexecuted assumptions in every handoff report.
