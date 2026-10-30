<!-- Model deprecation runbook · from Chapter 30 of The Product 360 Handbook -->

# Model deprecation runbook · [Product]

**Owner:** [PM]   **Applied AI lead:** [name]   **Last reviewed:** [Date]

## Standing preparation (before any notice)
- [ ] Model register: every model dependency by feature, provider, channel, region, version or alias, and customer tier
- [ ] Each provider's published lifecycle states, notice periods and "not sooner than" dates recorded
- [ ] Subscriptions to provider notices; status fields checked on a schedule
- [ ] Eval suite per feature, including regression sets from past incidents
- [ ] Model abstraction so a swap is a configuration change plus evals
- [ ] Decision per feature: pinned version or alias, and why

## When a notice arrives
| Step | Action | Owner | Done |
|---|---|---|---|
| 1 | Log the notice: model, channel, region, retirement date | | |
| 2 | Set the internal deadline at least [30] days before retirement | | |
| 3 | List affected features, customers and contracts (including AI risk documentation commitments) | | |
| 4 | Shortlist candidate replacements | | |
| 5 | Run the eval suite on representative data; compare quality, latency and cost together | | |
| 6 | Adjust prompts, tools and parameters for the chosen candidate | | |
| 7 | Shadow or canary with a limited set of accounts | | |
| 8 | Notify customers if behavior, data handling, region or price changes; update AI documentation | | |
| 9 | Cut over with a tested rollback path | | |
| 10 | Record results; update the model register and documentation | | |

## Candidate comparison
| Candidate | Quality (eval pass rate) | Regression set result | Latency | Cost per task | Data handling or region change | Decision |
|---|---|---|---|---|---|---|
| | | | | | | |

## Escalation
If no candidate meets the quality bar before the internal deadline: [options, e.g., degrade the feature gracefully, restrict it to supervised mode, request a provider extension where offered, notify customers].
