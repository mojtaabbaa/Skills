# Business Rule / Workflow Specification

## Overview
- Workflow name:
- Business owner:
- Project/site:
- Evidence status:
- Current implementation location:

## Actors and permissions
| Actor | Capabilities | Objects accessible | Restrictions |
|---|---|---|---|

## States and transitions
| Current state | Trigger | Preconditions | Authorized actor | Next state | Side effects |
|---|---|---|---|---|---|

## Business rules
| Rule ID | Condition | Outcome | Priority/precedence | Source of truth |
|---|---|---|---|---|

## Data contract
- Request/entity ID:
- Required fields:
- Optional fields:
- Uploaded files:
- Currency/units/timezone:

## Failure and replay behavior
- Duplicate submission:
- Duplicate webhook:
- Notification failure:
- External API failure:
- Booking conflict:
- Admin correction:

## Audit and privacy
- Events logged:
- Personal data stored:
- Retention:
- Access restrictions:

## Acceptance tests
- Happy path:
- Invalid/unauthorized actor:
- Illegal transition:
- Duplicate/retry:
- Concurrent action:
- Cancellation/refund:
- Data export/deletion:
