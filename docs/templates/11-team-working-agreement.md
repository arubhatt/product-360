<!-- Team working agreement · from Chapter 11 of The Product 360 Handbook -->

# Team working agreement · [Team] · v[n] · [Date]

**Method:** [Scrum / Kanban / cycles / hybrid]   **Signed off by:** [team members]   **Review date:** [Date]

## Cadence
- Planning or betting: [when, how long]
- Daily coordination: [when, 15 minutes]
- Review with customers or customer-facing staff: [when, who is invited]
- Retrospective: [when]

## Workflow and WIP limits
| State | Entry policy | WIP limit |
|---|---|---|
| Ready | | |
| In progress | | |
| In review | | |
| Evals and security | | |
| Ready to release | | |

## Definition of Done
- [ ] Tests pass, including tests not written solely by an agent
- [ ] Evals updated and passing (AI features)
- [ ] Cost per task within budget (features that call models)
- [ ] Security review complete where required
- [ ] Documentation and release note written
- [ ] Customer-facing teams told what changed

## Coding agents
- Agents may change: [code areas]
- Agents may not change: [eval suites, test configuration, approval gates, security controls]
- Human review required: [one reviewer by default; two for these areas]
- Size guideline for agent-generated changes: [e.g. reviewable in one sitting]
- An agent disabling or deleting a test is treated as a defect.

## Interrupt work
- How escalations enter: [channel, triage owner]
- Classes of service: Expedite (may exceed WIP; criteria) / Standard / Fixed date
- Service level expectation: [x]% of [item type] finish within [n] days

## Decision rights
| Decision | Decides | Consulted |
|---|---|---|
| What problem to solve next | PM | Team, design, tech lead |
| How to solve it | Team | PM, design |
| Scope cuts inside an appetite | Team with PM | Stakeholders informed |
| Release readiness | Tech lead | PM, security |

## Meeting norms
[Start and end times, async defaults, recording, decisions written down]
