---
name: software-architecture-code-governance
description: Govern software architecture, module boundaries, technical decisions, code quality, Git/versioning, testing, release management, and safe change control for WordPress plugins and related systems. Use for cross-module changes, refactors, new plugin architecture, releases, or architecture reviews.
---

# Software Architecture & Code Governance

## Mission

Keep the system understandable and changeable as features accumulate. Govern architecture and changes through explicit boundaries, evidence-based decisions, reviewable diffs, reproducible tests, and controlled releases. Prefer practical simplicity over ceremony, but never sacrifice data safety or maintainability for a quick patch.

## User-specific engineering principles

- Favor a small, direct, lightweight implementation when it satisfies the requirement.
- Avoid plugin sprawl, scattered snippets, unnamespaced hooks, redundant requests, and speculative abstractions.
- Preserve already-approved UI and established business behavior unless explicitly asked to change them.
- Do not guess selectors, taxonomy slugs, gateway IDs, class methods, plugin APIs, or database structures.
- Distinguish analysis-only requests from permission to change code.
- Provide exact file locations, dependencies, test evidence, and rollback instructions.
- Do not represent a proposed solution as tested or production-confirmed without evidence.

These are durable user-confirmed preferences from repeated project work; apply them unless a later explicit instruction changes the requirement.

## Architecture principles

### Separation of concerns
Keep responsibilities distinct:
- Presentation: templates, Elementor widgets, HTML/CSS, browser interaction.
- Application orchestration: use cases, request handlers, workflow coordination.
- Domain rules: pricing, eligibility, state transitions, booking rules, permissions.
- Infrastructure: database persistence, external APIs, SMS/email adapters, file storage.

Do not force every small plugin into a large layered framework. Use the smallest structure that preserves clear ownership and testability.

### Module boundaries
For each module define:
- Responsibility and non-responsibility.
- Public API/events/hooks.
- Data ownership.
- Dependencies and allowed dependency direction.
- Error contract.
- Test boundary.

Avoid cyclic dependencies and direct access to another module's private implementation. If two modules need the same behavior, extract a shared service only when the duplication is real and stable.

### WordPress-specific boundaries
- Plugin owns business logic and durable features.
- Theme owns theme-specific presentation/template behavior.
- Elementor owns page composition and widget configuration, not authoritative business rules.
- WooCommerce owns commerce lifecycle and entity persistence through supported APIs.
- Third-party plugin internals are dependencies, not code to patch directly.

## Decision records (ADR)

Record decisions when they materially affect data, compatibility, security, public APIs, module boundaries, or long-term maintenance.

Each ADR should include:
- ID, date, status, and owner.
- Context and constraints.
- Decision.
- Alternatives considered.
- Consequences and trade-offs.
- Migration/compatibility impact.
- Evidence and linked code/version.

Do not create an ADR for every trivial CSS adjustment. The objective is traceability, not paperwork.

## Change management

Before a change:
1. Capture repository status and current baseline.
2. Read relevant project and global instructions.
3. Define acceptance criteria and non-goals.
4. Locate all callers, hooks, templates, data readers/writers, and integrations.
5. Estimate blast radius and identify regression surfaces.
6. Choose the smallest coherent patch.
7. Define tests and rollback before risky edits.

During a change:
- Avoid unrelated formatting/refactoring.
- Keep public contracts stable or version/migrate them deliberately.
- Do not mix feature work with large dependency upgrades unless necessary.
- Keep generated files and build artifacts under control.
- Preserve existing local/uncommitted work; never overwrite it blindly.

After a change:
- Review the diff, not just the edited file.
- Run syntax/static checks and focused tests.
- Run broader regression tests for cross-cutting behavior.
- Record exactly what was and was not tested.
- Update version and knowledge records where appropriate.

## Git and source-control governance

- Inspect `git status` before editing.
- Do not discard, reset, clean, stash, or overwrite user changes without explicit authorization.
- Use feature branches for non-trivial work when repository policy allows.
- Use meaningful commits that describe one coherent change.
- Tag releases and retain a traceable mapping between ZIP/package and source commit.
- Do not commit secrets, production exports, customer uploads, or credentials.
- Require a clean or understood worktree before release packaging.
- If the workspace is not a Git repository, state that clearly and recommend initializing/cloning the correct repository before risky multi-file development. Do not run `git init` or create remote configuration without permission.

A prior Antigravity workspace named `Start` was reported as not being a Git repository. That observation applies to that workspace at that time; it is not a claim about every user project.

## Versioning and compatibility

Use an explicit versioning scheme for plugins and packages. Semantic versioning is a useful default where the project does not mandate another convention:
- PATCH: compatible bug fix.
- MINOR: backward-compatible feature.
- MAJOR: breaking public API/data contract change.

For WordPress plugins, keep plugin header version, internal version constant, schema version, asset version, ZIP name, and release notes consistent where applicable.

Maintain a compatibility matrix for:
- WordPress version.
- PHP version.
- WooCommerce version and HPOS mode.
- Elementor/Elementor Pro version.
- Active theme and version.
- Relevant plugin dependencies.
- Browser/device support where frontend behavior matters.

Do not claim support merely because activation succeeds.

## Testing governance

Choose tests based on risk:
- Syntax: PHP lint, JS syntax, JSON/YAML validation.
- Static: coding standards, type/static analysis where configured.
- Unit: deterministic domain logic.
- Integration: WordPress hooks, WooCommerce lifecycle, REST/AJAX, database.
- E2E/manual: user-facing workflows, desktop/mobile, checkout, admin approval.
- Performance: query count, response time, asset impact, Core Web Vitals where relevant.
- Security: authorization, input validation, escaping, CSRF/XSS/SQL injection paths.

Tests must verify behavior, not merely code execution. Include negative cases and failure paths.

## Definition of Done

A non-trivial change is done only when:
1. Acceptance criteria are met.
2. Scope and changed files are documented.
3. Existing behavior and regression surfaces are tested.
4. Security and data integrity are reviewed.
5. Performance impact is understood where relevant.
6. No unrelated changes are included.
7. Tests run and untested areas are reported honestly.
8. Rollback/recovery is documented for risky changes.
9. Plugin/package version and release notes are updated if required.
10. Project knowledge is updated with verified discoveries.

## Release and packaging

- Build ZIP from a clean, known source tree.
- Include only runtime files required by the plugin.
- Exclude `.git`, caches, temporary logs, local config, secrets, backups, and development-only dependencies unless intentionally required.
- Verify the ZIP root and plugin main file path.
- Verify activation and upgrade on staging.
- Record package checksum and source commit.
- Keep previous release artifact for rollback.

## Risk classification

| Risk | Examples | Minimum control |
|---|---|---|
| Low | Scoped CSS adjustment | Inspect selector scope; visual test |
| Medium | AJAX behavior, template hook, option change | Impact map; focused regression tests |
| High | Pricing, checkout, roles, uploads, schema migration | Staging, backup, security review, rollback, explicit approval |
| Critical | Production database deletion, payment/credential change, live deployment | Explicit approval, recovery plan, audit trail; no autonomous execution |

## Anti-patterns

- Large refactors hidden inside a small feature request.
- “Fixes” without acceptance criteria or reproduction evidence.
- Releasing a ZIP that cannot be traced to source revision.
- Modifying third-party plugin/core files.
- Ignoring an already dirty Git worktree.
- Calling a task complete after only reading or writing code.
- Overloading every prompt with all 15 Skills instead of selecting relevant expertise.
