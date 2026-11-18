# Knowledge Update Protocol Addendum — Skills 11–15

## When to update
Update persistent knowledge only when a discovery or change is durable and useful beyond the immediate chat: a verified architecture fact, accepted decision, reproducible incident, tested implementation pattern, compatibility constraint, or release outcome.

## Required evidence fields
Every non-trivial new record must include:
- Project/repository and environment.
- Date and source revision/version.
- Evidence class: CURRENTLY VERIFIED, USER-CONFIRMED, HISTORICAL, INFERRED, or UNKNOWN.
- Source path/symbol/config/log supporting the claim.
- Owner and scope.
- Verification method and test result.

## Where to store
| Discovery | Destination |
|---|---|
| Cross-project method | Relevant global Skill/reference |
| Current fact about one repository | Project context file in that repository |
| Architecture choice with trade-offs | ADR |
| Failure and verified root cause | Incident report |
| Schema change | Database migration notes + project context |
| Business rule/state change | Workflow specification |
| SEO URL/crawl policy | Technical SEO audit/context |
| Agent prompt or delegation method | AI-assisted development reference |
| Release outcome | Release record and changelog |

## Update sequence
1. Check whether the fact already exists.
2. Confirm whether it is current, project-specific, and supported by evidence.
3. Update the narrowest correct file; avoid copying the same fact into multiple sources.
4. Update the index/registry only when the change affects discoverability or project identity.
5. Record unresolved points separately; do not fill gaps with guesses.
6. Review relative links and Skill names after moving files.
7. Re-run syntax/frontmatter/link validation if the Skill itself changed.

## Never do
- Convert an inference into a confirmed fact.
- Promote a proposed code snippet to a verified pattern without tests.
- Delete historical incident context merely because the code has changed; mark it superseded/resolved and link the fix.
- Store secrets, access tokens, passwords, personal documents, or unnecessary customer data.
- Rewrite a stable Skill for a one-off project exception; put the exception in project context.
- Update a version baseline without evidence from source or release metadata.
