<!-- Bug triage policy · from Chapter 06 of The Product 360 Handbook -->

# Bug triage policy · [Product] · v[n] · [Date]

**Owner:** [PM]   **Engineering owner:** [Lead]   **Applies to:** [Products, services]

## Severity (technical impact; set by engineering or QA)
| Level | Definition | Example from this product |
|---|---|---|
| S1 | Outage, data loss, security exposure or unsafe action; no workaround | |
| S2 | Major function broken; painful workaround | |
| S3 | Minor function broken; reasonable workaround | |
| S4 | Cosmetic or polish | |

## Priority (business urgency; set by the PM)
Priority = severity, adjusted for customers affected, contractual exposure, workaround and strategic accounts.
| Priority | Meaning | Internal fix SLA | Contractual SLA it protects |
|---|---|---|---|
| P0 | Drop everything | [hours] | [ ] |
| P1 | Next in line, this sprint | [days] | [ ] |
| P2 | Default; planned | [weeks] | |
| P3 | When able | None | |
| P4 | Polish; eventually | None | |

Rule: every internal SLA is shorter than the contractual SLA it supports.

## Triage cadence
When: [day, time, frequency]   Attendees: PM, engineering lead, QA, support lead   Prep: harness drafts agenda from tracker and support connectors

## Bug bar by release phase
| Phase | Meets the bar |
|---|---|
| Early build | All S1 to S3; S4 if cheap |
| Stabilization | S1, S2; any customer-reported bug |
| Release candidate | S1; data loss; security; [product-specific always-fix conditions] |

Always meets the bar: [for example, any defect that can cause an unapproved or wrongly targeted action]

## Escalations from named accounts
Path: [support → account team → PM → engineering lead]   Who can override priority: [role]

## Regressions
Definition: [a defect in behavior that previously passed]   Treatment: [one priority level higher by default]

## Reporting (monthly)
Open P0 and P1 count and age; escaped defects; reopen rate; SLA misses; top root-cause clusters
