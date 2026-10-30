<!-- Eval plan · from Chapter 31 of The Product 360 Handbook -->

# Eval plan · [Feature] · [Date]

**Owner:** [PM or domain expert]   **Engineering owner:** [Name]   **Last run:** [Date]   **Gates releases:** yes / no

## Error analysis
- Traces reviewed: [n] on [dates], from [source]
- Reviewers:
- Failure taxonomy:

| # | Failure mode | Description | Example trace | Frequency in sample | Severity (H/M/L) |
|---|---|---|---|---|---|
| 1 | | | | | |

## Eval suite
| Suite | Type | # tasks | Grader (code / model judge / human) | Target | Current |
|---|---|---|---|---|---|
| [Failure mode 1] | Capability | | | | |
| [Existing behaviors] | Regression | | | ≥ 98% | |
| Should refuse or say "I'm not sure" | Capability | | | | |
| Consistency | pass^[k] | | | | |

## Judge validation (for each model judge)
| Judge | Failure mode | Human labels | True positive rate | True negative rate | Last validated |
|---|---|---|---|---|---|
| | | | | | |

## Run policy
- Runs on: every prompt change / model change / provider change / release
- Regression failure policy: block release / require approval from [name]
- Production sampling: [n] traces per [week], reviewed by [name]
- New failures from production become eval cases within [n] days

## History
| Date | Change | Capability score | Regression score | Notes |
|---|---|---|---|---|
| | | | | |
