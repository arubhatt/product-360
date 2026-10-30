<!-- User story with acceptance criteria · from Chapter 06 of The Product 360 Handbook -->

# Story · [Verb phrase title] · [Tracker ID]

**Epic:** [Epic or outcome]   **Persona:** [Persona]   **Owner:** [PM]   **Status:** Draft / Ready / In progress / Done

## Story
As a [role in context], I want [capability], so that [outcome].

## Context and evidence
- Customer evidence: [quotes, ticket IDs, interview snapshots]
- Metric this should move: [metric and expected direction]
- Why now: [link to Sprint Goal or quarterly outcome]

## Acceptance criteria (Given-When-Then, three to five steps each)
Scenario: [Happy path]
  Given [known state]
  When [event]
  Then [observable outcome]

Scenario: [Permission boundary: role without rights]
  Given [user lacks role or scope]
  When [event]
  Then [what they see instead]

Scenario: [Error or missing input]
  Given [failure state]
  When [event]
  Then [safe, observable outcome]

Scenario: [Tenancy: data from another tenant or customer]
  Given [...]
  When [...]
  Then [...]

## Rules in EARS form (optional, for agent specs)
- When [trigger], the [system] shall [response].
- If [unwanted condition], then the [system] shall [response].

## Non-functional
Latency: [ ]   Audit log entry: [ ]   Data residency: [ ]   Accessibility: [ ]   API versioning: [ ]

## AI behavior (AI features only)
Eval set: [name]   Pass threshold: [ ]   Cost per task ceiling: [ ]   Risk class: [ ]

## Out of scope
- [Explicit exclusions]

## Telemetry
Event that proves use: [ ]   Event that proves value: [ ]

## Open questions
| Question | Owner | Due |
|---|---|---|
| | | |

## INVEST check
Independent [ ]  Negotiable [ ]  Valuable [ ]  Estimable [ ]  Small [ ]  Testable [ ]
