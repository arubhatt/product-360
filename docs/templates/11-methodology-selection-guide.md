<!-- Methodology selection guide · from Chapter 11 of The Product 360 Handbook -->

# Methodology selection guide · [Product] · [Team] · [Date]

**Owner:** [PM]   **Agreed with:** [tech lead, designer, team]   **Review by:** [Date]

## 1. The work (last two quarters, from the tracker)
- Share of work planned vs unplanned: [x]% / [y]%
- Share of work ordered (known solution) vs complex (learning required): [x]% / [y]%
- Typical item size: [hours / days / weeks]
- Examples of each category: [three links]

## 2. The main risk (Chapter 00's four risks)
Value / Usability / Feasibility / Viability, with evidence:

## 3. External commitments
| Commitment | Type (date, scope, service level) | Truly fixed? | Owner | Date |
|---|---|---|---|---|
| | | | | |

## 4. Coordination
- Teams sharing this codebase or backlog:
- Dependencies that could be removed by an API, contract or platform capability:

## 5. Verification strength
- Automated tests: strong / partial / weak
- Evals for AI behavior: strong / partial / weak / not applicable
- Share of changes written mainly by coding agents:

## 6. Default method
| Situation | Default |
|---|---|
| Ordered, fixed external date and scope | Plan-driven, iterative build inside gates |
| Complex, value risk high | Scrum with dual-track discovery |
| Interrupt-driven, service commitments | Kanban with WIP limits and an SLE |
| Fixed date, flexible scope | Appetite-bounded cycles (Shape Up style) or Scrum with appetites |
| Five or more teams, real dependencies | Remove dependencies first; then LeSS, or SAFe for portfolio governance |
| Agent-heavy, strong CI and evals | Continuous flow with a fixed review, retro and planning cadence |

**Chosen method:** [method]
**Why (one paragraph):**
**What would make us change it:** [specific trigger, e.g. unplanned work above an agreed share for two months]
