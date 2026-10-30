<!-- AI analysis verification checklist · from Chapter 19 of The Product 360 Handbook -->

# Verification checklist · [Analysis title] · [Date]

**Depth required:** Exploratory / Decision-grade / Board or pricing   **Verified by:** [name]   **Sign-off (if required):** [name, date]

| # | Check | How | Result (pass / fail / n.a.) | Notes |
|---|---|---|---|---|
| 1 | Reconcile to source | A headline number matches the system of record or the canonical value in the context pack | | |
| 2 | Method shown | Query, filters, joins and window explained in plain language; steps match the question | | |
| 3 | Spot-check | Three records traced from source to final number | | |
| 4 | Sanity bounds | Rates within 0 to 100%; segments sum to total; change from last published value explained | | |
| 5 | Time window | Exact start and end; time zone; complete periods; fiscal or calendar; late-arriving data | | |
| 6 | Definitions | Metric names, grain and deduplication match the dictionary | | |
| 7 | Denominator and mix | No averages of averages; segment split checked for reversal; churned or migrated accounts included | | |
| 8 | Run twice | Fresh session, same brief, same numbers within tolerance | | |
| 9 | Provenance | Every reported number carries source, window and timestamp | | |
| 10 | Stakes sign-off | Required sign-off obtained | | |

Exploratory depth requires checks 1, 2 and 5. Decision-grade requires 1 to 9. Board, pricing or forecast requires all ten.

## Failures found and fixes
| Check | What was wrong | Fix (prompt change, context pack update) |
|---|---|---|
| | | |

## Saved evidence
Method: [link]   Frozen dataset or export: [link]   Timestamp:
