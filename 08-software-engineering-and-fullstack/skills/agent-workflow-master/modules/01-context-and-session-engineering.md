# Module 01: Context Engineering, Session Hygiene & Graphify Navigation

Consolidated from `context-engineering` + `ai-assisted-development`.

---

## 1. The 5-Level Context Hierarchy

Curate context intentionally — too little causes hallucination, too much dilutes attention:
1. **Level 1 — Rules Files (`AGENTS.md`, global skills):** Always loaded, concise tech stack, commands, conventions, hard boundaries.
2. **Level 2 — Specs & Architecture Docs:** Loaded per feature/session (contracts, ADRs, schemas).
3. **Level 3 — Relevant Source Files:** Targeted reads of only the files directly touched or depended upon.
4. **Level 4 — Error Output & Test Results:** Exact failing traces and command outputs per iteration.
5. **Level 5 — Conversation History:** Compress/compact cleanly at task boundaries before quality degrades.

---

## 2. Context Budget & Confusion Management

- **Protect Until the End:** User constraints, target contracts, active file diffs, failing test output.
- **Cut or Compress First:** Repetitive logs, large unedited reference dumps, closed sub-tasks (summarize state cleanly using [`references/agent-context-transfer-template.md`](../references/agent-context-transfer-template.md)).
- **When Context Conflicts:** Newer explicit user instruction > current source code > project `AGENTS.md` > global skill defaults > historical notes. Surface contradictions explicitly instead of silently guessing.
- **Restartable Session Boundaries:** End major milestones with an explicit state summary (completed, verified, remaining, exact files touched).

---

## 3. Graphify Architecture Navigation Protocol

When a valid Graphify-generated codebase graph exists in a project:
1. Query the graph FIRST for callers, symbol dependencies, and blast radius before broad repo scans.
2. Distinguish extracted AST edges from inferred relationships.
3. Always verify high-impact edges directly in actual source files (a graph guides navigation; it never replaces source inspection or tests).
4. Full protocol: [`references/graphify-usage-protocol.md`](../references/graphify-usage-protocol.md).
