<!-- AI PRD addendum · from Chapter 31 of The Product 360 Handbook -->

# AI PRD addendum · [Feature] · v[n] · [Date]

Attach to the standard PRD. Every section is required for AI-powered features.

## 1. Why AI
- The user problem (link to PRD):
- Why a rule-based solution isn't enough:
- Cost-of-error table:

| Error type | Example | Cost to user | Cost to business | Detectable by user? |
|---|---|---|---|---|
| False positive | | | | |
| False negative | | | | |
| Harmful or inappropriate output | | | | |
| Wrong action (agents) | | | | |

## 2. Pattern and autonomy
- Pattern: augmented model / chain / routing / parallel / orchestrator / evaluator-optimizer / agent
- Why the simpler patterns weren't enough:
- Autonomy per action class:

| Action class | Reversibility (cheap / costly / irreversible) | Autonomy (L1 to L5) | Approval and confirmation design |
|---|---|---|---|
| | | | |

- Stopping conditions and budgets: max steps [n], max tokens [n], max time [n], max spend per task [$]
- Escalation path when a limit is hit:

## 3. Quality (link to eval plan)
- Failure taxonomy (top modes):
- Capability eval targets:
- Regression eval threshold (target near 100%):
- Consistency target (pass^k):
- Accountable domain expert:

## 4. Models and data
- Models and providers (link to model register):
- Fallback when the provider is unavailable or degraded:
- Grounding sources and how they're permissioned:
- Personal and customer data handled, retention, residency:
- Training and feedback use permitted by contracts: yes / no / with consent
- Feedback signals captured and where they're stored:

## 5. Cost and latency (link to AI cost model)
- Cost per task at expected volume:
- Gross-margin floor:
- Latency budget: time to first token [ms], end to end [s]
- Cost levers in use: routing / caching / workflow caching / budgets

## 6. Trust and failure UX
- How capability and limits are communicated:
- Sources and confidence display:
- "I don't know" state:
- Correction, undo and regenerate:
- AI disclosure:
- Graceful degradation:
- Anti-rubber-stamping design (for approvals):

## 7. Risk and regulation (link to AI risk assessment)
- Our role: provider / deployer
- Likely risk tier and jurisdictions:
- Transparency and documentation duties:
- Security threats considered: prompt injection, data exfiltration, credential misuse

## 8. Rollout
| Stage | Entry criteria (evals and production evidence) | Who sees it | Exit criteria |
|---|---|---|---|
| Shadow | | | |
| Assisted | | | |
| Supervised | | | |
| Autonomous (allowlisted actions) | | | |

- Kill switch: who can pull it, and how fast it takes effect:
