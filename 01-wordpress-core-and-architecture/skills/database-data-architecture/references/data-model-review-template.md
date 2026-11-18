# Data Model Review Template

## Entity / dataset
- Name:
- Owning plugin/module:
- Evidence status:
- Source files:

## Lifecycle
- Creation path:
- Read paths:
- Update paths:
- Delete/archive path:
- Background/cron paths:

## Storage decision
- WordPress API / WooCommerce CRUD / options / metadata / taxonomy / custom table / cache:
- Why this storage fits:
- Alternatives considered:

## Schema
| Field | Type | Required | Default | Constraints | Sensitivity | Notes |
|---|---|---|---|---|---|---|

## Query patterns
| Query | Filters | Sort | Expected volume | Frequency | Index/caching |
|---|---|---|---|---|---|

## Integrity and security
- Uniqueness and idempotency:
- Authorization:
- Validation:
- PII/retention:

## Migration and recovery
- Current schema version:
- Target schema version:
- Migration steps:
- Backup:
- Failure recovery:
- Rollback or forward-only recovery:

## Verification
- Fresh install:
- Upgrade:
- Concurrent execution:
- Query performance:
- HPOS mode:
- Cache behavior:
- Test evidence and date:
