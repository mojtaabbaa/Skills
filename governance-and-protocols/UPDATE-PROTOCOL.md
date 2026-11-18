# Knowledge Update Protocol

Use this after a meaningful user correction, successful implementation, confirmed regression, or architecture decision.

## Classify the learning
- Put durable cross-project constraints in the relevant Antigravity rule or `.agents/AGENTS.md`.
- Put repeatable procedures in the relevant Skill's `SKILL.md`.
- Put project-specific facts, code maps, incidents, and examples in that Skill's `references/` or the active repository's `PROJECT_CONTEXT.md`.
- Put an architectural choice and rationale in the project's decision log.
- Do not create a new file if an existing record can be updated cleanly.

## Update only after evidence
Before recording a fix as confirmed, verify the active project/version and capture the exact test that passed. If a proposed solution was not tested, label it proposed. If one environment worked, do not generalize it to all sites.

## Suggested decision record
```md
## YYYY-MM-DD — Short decision title
- Project/version:
- Context/problem:
- Decision:
- Reason:
- Alternatives rejected:
- Files/interfaces affected:
- Tests/evidence:
- Risks/limitations:
- Status: proposed | implemented | tested | production-confirmed
```

## End-of-task memory capture
At the end of a substantial Antigravity session, use `/learn` with a narrow instruction describing what to retain. Review the proposed artifact before approval. Example:
`/learn update the Ravi Smart Filter reference with the verified AJAX request contract and the exact tests run; do not record any unverified guesses.`
