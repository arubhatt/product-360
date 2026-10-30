<!-- Technical design review checklist (PM questions) · from Chapter 07 of The Product 360 Handbook -->

# Technical design review · [Design doc title] · [Date]

**Reviewer:** [PM]   **Doc owner:** [Tech lead]   **Linked PRD:** [link]   **Decision needed by:** [Date]

## 1. Problem and outcome
- [ ] The doc's context and goals match the PRD's problem and outcome metric.
- [ ] Notes:

## 2. Non-goals
- [ ] Every non-goal is acceptable to customers, sales, support and partners.
- [ ] Non-goals that need to be communicated externally: [list]

## 3. Who calls this
- [ ] Callers are named: human users / developers / internal teams / AI agents / partners.
- [ ] For each caller, what changes for them: [notes]

## 4. Alternatives considered
- [ ] At least one cheaper, simpler or more reversible option was weighed.
- [ ] The reason for rejecting each alternative is stated.

## 5. Data
- [ ] What is stored, where (region), for how long, under which tenant: [answer]
- [ ] Residency and retention match customer commitments.

## 6. Reliability
- [ ] Proposed SLIs and SLOs: [list]
- [ ] Error budget and what happens when it's spent.
- [ ] Failure behavior: what each user sees when a dependency is down.

## 7. Compatibility
- [ ] Observable behaviors that change for existing callers (ordering, timing, defaults, error text): [list]
- [ ] Versioning and migration plan for breaking changes.

## 8. Security and privacy
- [ ] Least-privilege access and scopes.
- [ ] Audit logging, including actions taken by agents and who approved them.
- [ ] Revocation path (kill switch, token revocation).

## 9. Cost
- [ ] Unit cost per request and per customer outcome, at expected and peak usage: [numbers]
- [ ] Margin impact: [estimate]

## 10. Observability and rollback
- [ ] How we'll know it works in production: [signals]
- [ ] How we undo it, including undoing a failed rollback.

## 11. Reversibility
- [ ] Decisions that are hard to reverse (public interface, data model, pricing unit) are flagged: [list]

## 12. Decisions to record
| Decision | ADR number | Status |
|---|---|---|
| | | |

## The regret question
What would make us regret this design in a year? [answer]

## Outcome
Approve / Approve with changes / Revise and re-review. Changes requested: [list]
