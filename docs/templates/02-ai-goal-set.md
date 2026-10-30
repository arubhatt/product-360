<!-- AI feature goal set · from Chapter 02 of The Product 360 Handbook -->

# AI goal set · [Feature] · [Quarter]

**Task automated or augmented:** [describe]   **Automate or augment?** [choice and reason]

| Family | Measure | Definition and test set | Baseline | Threshold or target | Role (objective / guardrail) | Action if breached |
|---|---|---|---|---|---|---|
| Value | | | | | | |
| Quality | | Held-out set: [name, size, last refreshed] | | | | |
| Quality: severe errors | | | | | | |
| Trust | Acceptance rate | | | | | |
| Trust | Override or rejection rate | | | | | |
| Trust | Wrong-action rate | | | | | |
| Cost | Inference cost per unit of value | | | | | |
| Cost | Gross margin contribution | | | | | |

## Error costs
| Error | Example | Cost to the customer | Weighting |
|---|---|---|---|
| False positive | | | |
| False negative | | | |

## Triggers
- If [measure] crosses [threshold] for [period], then [model review / rollback / pause autonomy / escalate].

## Evidence for reviewers
Where the security reviewer, auditor or regulator can find each trust measure: [location]
