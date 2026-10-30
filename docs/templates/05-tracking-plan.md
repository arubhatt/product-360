<!-- Tracking plan and event spec · from Chapter 05 of The Product 360 Handbook -->

# Tracking plan · [Product or feature] · v[n] · [Date]

**Owner:** [PM]   **Engineering owner:** [Name]   **Data reviewer:** [Name]   **Status:** Draft / Implemented / Validated

## Questions this plan must answer
1. [Question] → Metric: [metric name]
2.
3.

## Conventions
- Event names: Object + past-tense Action, Proper Case (for example, "Report Exported").
- Property names: snake_case.
- Variable detail goes in properties, never in event names.
- Every event carries: account_id, user_id, actor_type (human / agent / automation), [workspace_id or partner_id if relevant].
- Trust- or revenue-critical events fire server-side.

## Events
| Event name | Fires when (exact moment) | Question it answers | Metric(s) it feeds | Event properties (name: type) | Source (server/client) | Owner | Status | Privacy note |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | Proposed / Implemented / Validated | |

## User and account properties
| Property | Level (user/account/workspace/partner) | Type | Allowed values | Source |
|---|---|---|---|---|
| | | | | |

## AI events (AI features only)
Each AI output event also carries: model_version, prompt_or_agent_version, sources_retrieved, tool_calls, latency_ms, cost, and the human decision (accepted / edited / rejected / reverted).

## Privacy and security
- Customer content (logs, tickets, prompts, documents) is never sent as a property unless approved by [reviewer] on [date].
- Personal data in properties: [none / list with approval].

## Validation
- [ ] Every critical path run in test and checked against this plan
- [ ] Every event has account_id
- [ ] No duplicate or near-duplicate events against the existing taxonomy
- [ ] Changes logged below

## Change log
| Date | Change | Reason | By |
|---|---|---|---|
