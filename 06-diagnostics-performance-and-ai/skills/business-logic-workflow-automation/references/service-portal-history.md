# Service Portal — Historical Workflow Record

Evidence class: HISTORICAL. Confirm current implementation, role slugs, form IDs, pricing, and statuses in the source repository.

## Recorded flow

Login/register → select request/service type → Elementor multi-step form → pending approval → administrator manually reviews documents → administrator assigns role/access.

## Related components mentioned

- Elementor / Elementor Pro forms and pages.
- Members plugin for custom roles.
- Manual administrator review of uploaded documents.
- Admin-managed consultation time slots.

## Consultation details previously discussed

| Type | Historical price | Historical duration |
|---|---:|---|
| In-person | 2,000,000 toman | 30–40 minutes |
| Phone | 1,000,000 toman | 30–40 minutes |

These values are not verified as current. Confirm currency unit (toman/rial), whether price is per session, cancellation/refund policy, time zone, slot capacity, and whether payment occurs before or after approval.

## Questions to resolve from source/business owner

- What is the durable request record and primary key?
- Are form submissions linked to a user, request, or both?
- What are exact status slugs and allowed transitions?
- Which capability grants approval authority?
- Can rejected requests be resubmitted?
- How are uploads protected and deleted?
- How are time slots reserved against concurrent requests?
- When is access granted and revoked?
- What notifications are triggered and how is duplication prevented?
