<!-- AI incident response plan · from Chapter 33 of The Product 360 Handbook -->

# AI incident response plan · [Product] · v[n] · [Date]

Extends the company security incident process. Link: [process]

## AI-specific triggers
- Confident wrong output affecting many users or a high-impact decision
- Unsafe or unintended agent action
- Prompt injection or tool misuse that changed system behavior
- Personal or confidential data exposed through outputs
- Fairness or bias finding
- Unannounced behavior change after a model or provider update

## Severity
| Level | Definition for this product | Example | Response time |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Controls available
| Use case | Kill switch or degrade option | Who can trigger | Time to effect |
|---|---|---|---|
| | | | |

## Roles
- Incident lead: [name]
- PM (customer impact, comms, eval follow-up): [name]
- Applied AI (diagnosis, model or prompt rollback): [name]
- Security, privacy, legal: [names]

## Clocks to check (confirm with counsel)
- Contractual notification commitments: [summary]
- GDPR personal data breach notification, if personal data is involved
- EU AI Act Article 73 serious incident reporting, for high-risk systems once applicable
- Other: [jurisdiction or customer specific]

## Customer communication
- First notice within [time], containing: what happened, what we changed, what customers should do, when we will update next.

## After the incident
- [ ] Root cause (data, retrieval, prompt, model, tool, UX, process)
- [ ] New eval cases added and passing
- [ ] System card and impact assessment updated
- [ ] Decision log entry
- [ ] Tabletop scheduled for the next quarter
