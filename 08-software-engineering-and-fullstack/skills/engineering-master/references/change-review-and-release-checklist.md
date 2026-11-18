# Change Review and Release Checklist

## Before implementation
- [ ] Requirement and non-goals are explicit.
- [ ] Analysis-only vs code-change permission is clear.
- [ ] Current branch/commit and worktree status captured.
- [ ] Relevant Skills and project context loaded.
- [ ] Callers, hooks, data paths, and integrations mapped.
- [ ] Risk level assigned.
- [ ] Acceptance tests and rollback defined.

## During implementation
- [ ] Diff is scoped and minimal.
- [ ] No unrelated files changed.
- [ ] Public contracts and schema changes are documented.
- [ ] Authorization and validation are server-side.
- [ ] Errors are observable and actionable.
- [ ] No secret or customer data leaked.

## Before release
- [ ] PHP/JS/config syntax checks run.
- [ ] Relevant unit/integration/E2E checks run.
- [ ] Negative and failure paths tested.
- [ ] WordPress/PHP/WooCommerce/HPOS/theme/plugin compatibility checked.
- [ ] Responsive/RTL behavior checked where applicable.
- [ ] Performance regression checked where relevant.
- [ ] Git diff and package contents reviewed.
- [ ] Version and release notes updated.
- [ ] Backup and rollback path ready.
- [ ] Staging verification completed.
- [ ] Production deployment explicitly authorized.

## Release record
- Version:
- Source commit:
- ZIP/package checksum:
- Date:
- Files/modules changed:
- Tests run and results:
- Tests not run:
- Known limitations:
- Rollback procedure:
