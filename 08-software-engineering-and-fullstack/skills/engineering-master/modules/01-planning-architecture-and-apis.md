# Module 01: Planning, Architecture, API Design & ADRs

Consolidated from `planning-and-task-breakdown`, `incremental-implementation`, `api-and-interface-design`, `documentation-and-adrs`, and `software-architecture-code-governance`.

---

## 1. Planning & Vertical Slicing Discipline

Before modifying multiple files or non-trivial modules:
1. **Map Dependencies First:** Identify boundaries, upstream contracts, data schema impact, and rollback surfaces.
2. **Slice Vertically (Preferred):** Each slice cuts cleanly through schema -> logic -> API -> UI -> test so every slice compiles and delivers verifiable value independently (use Contract-First or Risk-First slicing when integrating external systems).
3. **Implementation Rules:**
   - **Simplicity First & Scope Discipline:** Solve the real requirement without speculative abstractions or unrelated drive-by refactors.
   - **Keep It Compilable:** Every increment leaves the repo green (`build` + `typecheck` + `tests`).
   - **Checkpoints:** After every 2–3 tasks, pause and verify assumptions against actual runtime behavior.
   - **Feature Flags:** Hide incomplete multi-PR features behind explicit flags rather than long-lived diverging branches.

---

## 2. Stable API & Interface Design Rules

- **Hyrum's Law & The One-Version Rule:** Every observable behavior becomes an implicit dependency; prefer additive, backward-compatible evolution over breaking changes.
- **Contract First:** Define explicit request/response types, pagination format (cursor preferred for mutable lists), and consistent machine-readable error envelopes (`code`, `message`, `details`, `requestId`) BEFORE writing handlers.
- **Validate at Boundaries:** Parse and validate all external payloads with strict schemas (e.g., Zod / PHP allowlists) at the entry edge; reject unknown or malformed fields.
- **Idempotency Keys:** Support idempotency keys on state-mutating POST endpoints (payments, bookings, webhooks) so retries never duplicate transactions.

---

## 3. Architecture Decision Records (ADRs)

Record an ADR whenever a decision is hard to reverse (database choice, auth model, caching strategy, cross-module boundary, major dependency). Match the repo's existing convention or use [`references/adr-template.md`](../references/adr-template.md): **Status, Date, Context, Decision, Alternatives Considered, Consequences**.
