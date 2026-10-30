<!-- Experiment design doc · from Chapter 05 of The Product 360 Handbook -->

# Experiment design · [Name] · [Date]

**Owner:** [PM]   **Analyst:** [Name]   **Decision maker:** [Name]   **Status:** Draft / Approved / Running / Read out

## 1. Decision this informs
[What we will do differently depending on the result.]

## 2. Hypothesis
We believe [change] for [segment] will [move OEC by at least X] because [reason]. We will know when [metric and threshold].

## 3. Unit of randomization
User / account / tenant / other: [choice]. Why: [interference risk, how the experience is shared].

## 4. Metrics
- OEC: [one metric or weighted combination, with definition]
- Secondary metrics: [list]
- Guardrails: [metric: must not degrade by more than X]

## 5. Power and duration
- Baseline and variance of the OEC: [values and source]
- Minimum detectable effect: [value]
- Sample size per arm: [n]
- Duration: [whole weeks]
- Variance reduction: [pre-period adjustment used? yes / no]
- Stopping rule: fixed duration / sequential method [name]. No early stopping on the OEC.

## 6. Population and ramp
Included: [who]. Excluded: [who and why]. Ramp: [percent by date].

## 7. Validity checks
- [ ] Sample ratio check before readout
- [ ] Pre-period or A/A comparison of arms
- [ ] Novelty or primacy watch: read results by week
- [ ] Data quality: event volumes by arm

## 8. Decision rule (written before launch)
| Result | Decision |
|---|---|
| OEC up, guardrails pass | |
| OEC up, a guardrail fails | |
| No detectable change | |
| OEC down | |

## 9. Risks and communication
Privacy review: [status]. Customer notice required by contract? [yes / no]. Safety: [any action that must not be randomized].

## If we cannot run a controlled experiment
Method chosen: [staged rollout with holdout / matched comparison / time series / offline replay / design partners]. Assumption we are making: [state it]. What else could explain a change: [list].
