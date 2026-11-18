# Graphify Usage Protocol

## Purpose

Use a generated project graph to navigate architecture and assess impact efficiently. The graph is a derived index, not the source of truth.

## Required sequence
1. Confirm the graph exists and identify the commit/source revision from which it was generated.
2. Query relevant symbols and relationships.
3. Label graph evidence as EXTRACTED or INFERRED according to the graph tool's semantics.
4. Open and inspect source files for important findings.
5. Compare graph revision with current repository state; regenerate or distrust stale sections after significant changes.
6. Record queries and verified source paths for the handoff.

## Do not
- Claim Graphify was used if no graph/tool execution occurred.
- Treat an inferred edge as a confirmed function call.
- Treat graph absence as proof that code does not exist.
- Perform broad refactoring based solely on graph output.

## Historical note

Graphify was preferred in a prior Ravi Smart Filter discussion. The CLI was not installed or run in that environment because package-index DNS/network access failed. Current availability must be checked anew.
