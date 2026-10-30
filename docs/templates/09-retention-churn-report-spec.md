<!-- Retention and churn report spec · from Chapter 09 of The Product 360 Handbook -->

# Retention and churn report spec · [Product] · v[n] · [Date]

**Owner:** [PM]   **Agreed with:** [Finance lead], [Customer success lead]   **Cadence:** Quarterly   **Next review:** [Date]

## Decisions this report supports
1. [For example: where to invest retention effort next quarter]
2. [For example: whether the onboarding change worked]

## Definitions (fixed; change only with a version bump)
| Term | Definition | Source system |
|---|---|---|
| Customer | [Contracting entity / account] | [CRM] |
| Cohort start | [Contract signature / go-live] | |
| Contract churn | [Non-renewal / termination] | |
| Usage churn | [No active users for N days / usage below X% of baseline] | [Telemetry] |
| Active | [Definition] | |
| Revenue base | [Contracted ARR / billed / consumed] | [Billing] |
| NRR | Revenue now from customers active 12 months ago ÷ their revenue 12 months ago | |
| GRR | As NRR, excluding expansion, cross-sell and price increases (max 100%) | |

## Segments
[Three to six: ACV band, channel, industry, region, onboarding path, migration status]
Minimum cohort size for reporting a rate: [N accounts]

## Sections
1. **Headline**: NRR, GRR and logo retention, overall and by segment, with counts.
2. **NRR bridge** by segment: starting revenue, + expansion, − contraction, − churn.
3. **Contract survival curves** by segment, current customers treated as censored.
4. **Usage survival curves** by segment, with the gap to contract survival.
5. **Hazard view**: where in the lifecycle risk concentrates.
6. **Cohort triangles**: logo, user and revenue retention.
7. **Churn reasons**: coded from exit interviews and notes, linked to revenue lost.
8. **What changed since last quarter** and why.
9. **Implications**: decisions proposed, with size of prize and confidence.

## Checks before publishing
- [ ] Totals reconcile to finance ARR within [x]%
- [ ] Definitions echoed back by the analysis and match this spec
- [ ] Five sample accounts spot-checked in source systems
- [ ] No rate shown without its count
- [ ] Sensitivity to the inactivity threshold tested

## Change log
| Version | Date | Change | Approved by |
|---|---|---|---|
| | | | |
