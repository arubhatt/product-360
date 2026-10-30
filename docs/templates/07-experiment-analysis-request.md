<!-- Experiment analysis request · from Chapter 07 of The Product 360 Handbook -->

# Experiment analysis request · [Experiment name] · [Date]

Use this brief as the prompt to an AI harness or the request to an analyst. If it includes customer data, use an approved tool.

## The decision
- Decision this informs: [ship / iterate / stop / roll back]
- Decision maker: [name]

## The plan, as written before launch
- Hypothesis: [text, copied from the plan]
- Unit of randomization: [user / account / team / tenant]
- Expected split: [for example, 50/50]
- Primary metric (OEC) and definition: [metric]
- Guardrail metrics and definitions: [list]
- Minimum effect worth detecting: [value]
- Stopping rule and planned sample size: [rule]
- Pre-registered segments: [list, or "none"]

## Data
- Sources (connector or system names): [list]
- Date range: [start to end]
- Known data issues: [list]
- Exclusions (internal, test and sandbox accounts, bots): [list]
- Outlier rule (cap, median or none): [rule]

## Required outputs, in this order
0. Data preparation: each exclusion applied, with unit counts by group before and after; counts of missing and duplicated events by group.
1. Sample ratio mismatch check: observed versus expected split, and whether it fails. If it fails, stop and report likely causes; do not report effects.
2. Primary metric: effect size, confidence interval and significance, as planned.
3. Guardrails: status of each, with intervals.
4. Pre-registered segments only.
5. Plain-language summary in under 150 words.
6. Assumptions made about data and method.
7. Data-quality caveats.
8. What result would change the conclusion.

## Not allowed
- Changing the primary metric or its definition.
- Reporting new segments unless labeled "exploratory."
- Declaring a winner if the SRM check fails or the stopping rule wasn't met.

## Verification (completed by the requester)
- [ ] Group counts match the experiment platform.
- [ ] Primary metric and segments are the pre-registered ones.
- [ ] Harness critiqued its own analysis; issues raised: [list]
- [ ] For major decisions, a second pass reproduced the headline numbers.
