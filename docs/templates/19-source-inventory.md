<!-- Source and connector inventory · from Chapter 19 of The Product 360 Handbook -->

# Source and connector inventory · [Product area] · [Date]

**Owner:** [PM]   **Reviewed with:** [data owner, security reviewer]   **Next review:** [Date]

| Source system | Category (analytics / warehouse / metrics layer / CRM / ticketing and docs / chat / files) | Access route (approved connector / export / none) | On approved list or registry? | Read-only tools available? | Write or send tools to switch off | Highest data tier (public / internal / confidential / restricted) | Region | Data owner | Freshness |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

## Gaps
- Sources we need but can't reach through an approved route:
- Metrics that exist in dashboards but not in the metrics layer:

## Trifecta check
Sources holding attacker-writable text (tickets, chat, email, web): [list]. These are never combined in one session with tools that can send data out.
