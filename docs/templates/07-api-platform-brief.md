<!-- API and platform product brief · from Chapter 07 of The Product 360 Handbook -->

# API and platform product brief · [Interface or service name] · v[n] · [Date]

**Owner:** [PM]   **Tech lead:** [name]   **Status:** Draft / In review / Published

## Customers
| Customer type | Who specifically | Their job to be done | Volume expected |
|---|---|---|---|
| External developers | | | |
| Partners | | | |
| Internal teams | | | |
| AI agents (via API or MCP server) | | | |

## The interface promise
- Resources and operations offered: [list]
- Events or webhooks emitted: [list]
- What we promise never to change without a new version: [list]
- Observable behaviors we know callers depend on (Hyrum's Law check): [list]

## Versioning and deprecation
- Versioning scheme: [date-based / numbered / other]
- What counts as a breaking change: [definition]
- Deprecation notice period and migration support: [policy]

## Reliability
- SLIs and SLO targets: [list]
- SLA, if any, and its consequences: [terms]
- Error budget policy: [what happens when it's spent]

## Limits and access
- Rate limits and quotas, by customer tier: [table]
- Authentication method and scopes: [list]
- Least-privilege defaults: [description]

## Agent readiness
- Operations agents may call: [list]
- Operations that require a human approval: [list]
- Agent rate limits and attribution (which human each agent acts for): [policy]
- MCP server: yes / no / planned. Tool descriptions owned by: [name]

## Commercials
- Pricing or internal chargeback unit: [unit]
- Cost to serve per unit: [estimate]

## Adoption and success
- Adoption metric: [active integrations, time to first successful call, share of target teams using it]
- Health metrics: [error rate, breakage reports, support tickets per integration]

## Documentation and onboarding
- Reference docs, samples and quickstart: [links]
- Time to first successful call target: [time]

## Open questions
1.
2.
