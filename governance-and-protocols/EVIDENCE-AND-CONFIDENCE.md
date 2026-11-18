# Evidence and Confidence Rules

## Evidence classes

Use these labels in internal notes and when reporting material technical conclusions:

- **CURRENTLY VERIFIED** — inspected in the active repository/runtime during this task, or confirmed by a test actually run now.
- **USER-CONFIRMED** — explicitly stated by the user; may still be time-sensitive.
- **HISTORICAL** — recorded in previous discussions or an old environment snapshot; must be rechecked before reuse.
- **INFERRED** — plausible interpretation, not directly proven. State the evidence and validate it.
- **UNKNOWN** — insufficient evidence. Do not fill the gap with a guess.

## Confidence rules
1. A file name or class name remembered from a conversation does not prove it exists in the current checkout.
2. A version number in a project note does not prove that version is installed now.
3. A browser URL/payload observed once is not necessarily a stable API contract.
4. A successful syntax check is not proof of correct application behavior.
5. Plugin activation is not proof of feature compatibility.
6. A visual match in one viewport is not proof of responsive correctness.
7. A code proposal is not a tested implementation. A tested implementation is not necessarily production-confirmed.
8. Do not label code “final”, “verified”, or “production-ready” without direct evidence.

## Required implementation record
For each meaningful feature/fix, record:
- Project/site and repository.
- Date and environment (local/staging/production).
- Core/PHP/WooCommerce/theme/plugin versions if relevant.
- Requirement and acceptance criteria.
- Files/hooks/classes/settings/tables changed.
- Previous behavior and root cause (if debugging).
- Final design/implementation and why it was chosen.
- Tests actually performed and results.
- What remains untested/unknown.
- Rollback path.
- Evidence class.

## Conflict resolution
When sources conflict, use this order:
1. Latest explicit user instruction.
2. Current source code and runtime behavior.
3. Current tests/logs/configuration.
4. Project-specific documentation with a recent date.
5. Historical knowledge pack.
6. General best practice.

If an old note conflicts with current code, update the note after confirming the new reality. Never silently merge both interpretations.
