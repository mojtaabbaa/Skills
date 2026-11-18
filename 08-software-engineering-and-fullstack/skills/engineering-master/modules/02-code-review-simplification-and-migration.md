# Module 02: Code Review, Safe Simplification & Deprecation/Migration

Consolidated from `code-review-and-quality`, `code-simplification`, and `deprecation-and-migration`.

---

## 1. The Five-Axis Code Review Protocol

Before merging any change (human- or agent-authored), review across all 5 axes:
1. **Correctness:** Edge cases, null/empty handling, off-by-one, async race conditions, error propagation, idempotency.
2. **Readability & Simplicity:** Clear naming, shallow nesting, early returns, zero dead code or opaque cleverness.
3. **Architecture & Boundaries:** Single responsibility, clean module ownership, no leaky abstractions or circular dependencies.
4. **Security:** Input validation, authorization (not just authentication), output escaping, zero leaked secrets/PII (see `Module 05`).
5. **Performance:** No N+1 queries, unbounded loops, unnecessary re-renders, or missing pagination/indexes (see `Module 06`).

Prefer **structural remedies** (type safety, invariants, helper extraction) over brittle one-off `if` patches. Use [`references/change-review-and-release-checklist.md`](../references/change-review-and-release-checklist.md) for release sign-off.

---

## 2. Code Simplification (Chesterton's Fence)

When refactoring for clarity **without changing behavior**:
1. **Understand Before Touching:** Never delete code you cannot explain — trace callers, tests, and historical intent first.
2. **Preserve Behavior Exactly:** Lock existing behavior with tests BEFORE refactoring.
3. **Clarity Over Cleverness:** Flatten nested conditionals via guard clauses, extract cohesive helpers, keep scope strictly bounded to the touched area.
4. **Verify After Every Step:** Re-run tests/typecheck after each small simplification.

---

## 3. Safe Deprecation & Migration Protocol

Code is a liability — remove obsolete systems safely using a 4-stage lifecycle:
1. **Build & Verify Replacement:** Ensure parity and migration tooling exist first.
2. **Announce & Document:** Publish deprecation notice with target removal date and clear before/after migration guide (distinguish *advisory* vs *compulsory* deprecation).
3. **Dual-Run / Measure Usage:** Instrument old path callers so you know with evidence when traffic hits zero.
4. **Remove Cleanly:** Delete dead code, feature flags, and fallback shims once migration is verified complete.
