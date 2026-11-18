---
name: business-logic-workflow-automation
description: Model and implement business rules, approval workflows, multi-step forms, role-based access, booking, notifications, and cross-plugin processes in WordPress and WooCommerce. Use when a feature has states, approvals, actors, deadlines, pricing rules, or multi-step transactions.
---

# Business Logic & Workflow Automation

## Mission

Translate business requirements into explicit, testable state transitions and server-enforced rules. Protect business invariants across WordPress, WooCommerce, Elementor forms, user roles, payment gateways, and background processing. A workflow is not complete merely because its screens look correct.

## Known historical user workflows

A service portal flow was described as:
1. User logs in or registers.
2. User selects a request/service type on a gateway page.
3. User completes an Elementor multi-step form.
4. Request enters a pending-approval state.
5. Administrator manually reviews submitted documents.
6. Administrator assigns the required role/access.

Additional historical details:
- Custom roles were created using the Members plugin.
- Consultation types included in-person and phone options.
- Historical prices were 2,000,000 toman in-person and 1,000,000 toman by phone.
- Historical consultation duration was 30–40 minutes.
- Administrative time slots were part of the consultation-booking concept.

These values and implementation details are HISTORICAL. Verify current prices, roles, form IDs, state names, slot logic, and plugin versions before reuse.

Other historical WooCommerce business rules include separate cash and installment prices/gateways, product-specific gateway restrictions (one request referred to product ID `61965`), a packaging charge discussed as 500,000 toman, and temporarily disabling checkout. These are separate requirements from different contexts; never combine them into one global rule without confirmation.

## First principle: write the rule before the code

For every business behavior, document:
- Actor: visitor, customer, staff, manager, administrator, external service.
- Trigger: form submission, payment event, status change, schedule, webhook, manual action.
- Preconditions: identity, capability, required data, current state, availability.
- Decision rule: exact condition and precedence.
- State transition: old state → new state.
- Side effects: email, SMS, role change, order update, access grant, calendar slot reservation.
- Failure behavior: retry, rollback, compensation, manual review.
- Audit evidence: who did what, when, and why.

Do not encode ambiguous business language as assumptions. If a monetary rule, role boundary, refund consequence, or approval condition is ambiguous, surface the exact ambiguity before implementing it.

## State-machine design

- Enumerate states and transitions explicitly.
- Define terminal states and whether they can be reopened.
- Define allowed transition actors and permissions.
- Reject illegal transitions server-side.
- Use stable machine identifiers separate from Persian display labels.
- Track transition timestamps and responsible actor where operationally required.
- Prevent a state change from being performed twice with duplicate side effects.
- Define cancellation, expiry, rejection, resubmission, and escalation states where relevant.

Example approval states (illustrative only):
`draft → submitted → pending_review → approved | rejected → access_granted`

Do not impose this exact state model if the existing project uses a different contract.

## Access control and roles

- Use capabilities as the authorization source; roles are groupings of capabilities, not the security decision itself.
- Verify `current_user_can()` on every privileged server-side operation.
- Never rely on hidden buttons, disabled fields, URL obscurity, or client-side conditions.
- A nonce verifies request intent, not permission.
- Validate that the requested object belongs to the current user or that the actor has authority over it.
- Separate “can view”, “can edit”, “can approve”, “can assign role”, and “can export” permissions.
- Prevent self-approval when the business process requires separation of duties.
- Log sensitive administrative transitions without exposing unnecessary personal data.

## Forms and multi-step submissions

- Treat browser-submitted values as untrusted, including hidden fields and step state.
- Validate required fields and cross-field dependencies server-side at final submission.
- Define draft persistence and expiry behavior.
- Store an immutable submission snapshot when later edits to the profile/product must not rewrite what was submitted.
- Validate file type, size, ownership, storage permissions, and retrieval authorization for uploaded documents.
- Use a durable request ID; do not rely solely on an Elementor submission ID unless the integration contract proves it stable and sufficient.
- Make repeated submission idempotent or deliberately create a new revision.
- Define how partial submissions are resumed and how abandoned drafts are cleaned up.

## Workflow side effects and reliability

Email, SMS, role changes, gateway calls, and booking reservations are side effects. For each side effect:
- Define when it runs relative to the state commit.
- Prevent duplicate execution on retries or duplicate webhooks.
- Persist a stable event/operation identifier where practical.
- Handle failures without leaving the primary record in an impossible state.
- Retry transient failures with bounded attempts and observability.
- Use compensating actions for side effects that cannot be rolled back atomically.
- Do not send notifications before the state change is durable.
- Do not assume a WordPress request or WP-Cron job will execute exactly once.

For critical multi-step workflows, consider an outbox/event table or durable job queue, but only after measuring the need and reviewing existing infrastructure.

## Booking and scheduling

- Store timestamps in a canonical timezone-aware representation (typically UTC) and display in the business timezone.
- Define slot duration, buffer, capacity, blackout dates, lead time, cancellation window, and rescheduling rules.
- Prevent double booking with a server-side concurrency-safe reservation mechanism.
- A “slot looks available” result in the browser is not a reservation.
- Use atomic/unique constraints or locking where required to ensure only one booking can claim a limited slot.
- Define expiry of unpaid or unconfirmed holds.
- Ensure cancellations release capacity exactly once.

## WooCommerce commercial rules

- Define price source, eligibility, timing, currency unit, tax behavior, coupon interaction, fee calculation, refund behavior, and gateway compatibility.
- Apply authoritative price changes on the server and ensure product display, cart, checkout, gateway amount, order total, emails, and refunds remain consistent.
- Distinguish order-level fees from per-line charges.
- Make fee insertion idempotent because totals can be recalculated repeatedly.
- Scope rules by product, variation, cart contents, customer capability, or gateway as specified.
- Verify product ID and gateway ID against the current environment; historical numeric IDs and labels are not portable identifiers.

## Auditability and privacy

- Record who performed a sensitive transition, when, previous/new state, and relevant reason.
- Minimize stored personal data; define retention and deletion behavior.
- Restrict uploaded documents and exports to authorized roles.
- Avoid logging full form payloads, passwords, payment tokens, or identity documents.
- Include a clear admin timeline or trace when the workflow requires operational support.

## Architecture boundaries

- Keep business rules in a domain/service layer or custom plugin, not buried in Elementor presentation settings.
- Treat Elementor as form/UI integration, not as the authoritative business rules engine.
- Keep WooCommerce payment and order transitions aligned with WooCommerce lifecycle semantics.
- Isolate integrations (SMS, email, booking, external API) behind focused adapters where complexity warrants it.
- Avoid plugin coupling through undocumented globals or direct database writes.

## Workflow delivery checklist

1. Business rule and state diagram documented.
2. Actors and capabilities mapped.
3. Server-side validation implemented.
4. Duplicate/replay behavior defined.
5. Failure/retry/compensation defined.
6. Audit record and privacy requirements addressed.
7. Notifications and external integrations tested.
8. Timezone and concurrency tested for bookings.
9. Commercial totals tested through order creation and refund paths.
10. Admin and customer flows tested separately.

## Anti-patterns

- Treating an Elementor form's visible steps as a secure workflow.
- Assigning roles from client-submitted fields.
- Approving requests through a URL parameter alone.
- Double-booking because availability was checked only in JavaScript.
- Sending duplicate SMS/email after retries.
- Applying a fee on every totals recalculation.
- Mixing historical prices or IDs from different sites.
- Storing uploaded documents in publicly guessable URLs.
