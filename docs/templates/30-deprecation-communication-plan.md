<!-- Deprecation communication plan · from Chapter 30 of The Product 360 Handbook -->

# Deprecation communication plan · [Offering, feature or API] · [Date]

**Owner:** [PM or PMM]   **Canonical page:** [location of the deprecation registry or lifecycle page]

## Audiences and channels
| Audience | What they need to know | Channel | Sender | First contact |
|---|---|---|---|---|
| Economic buyers | Dates, business impact, commercial terms | Account team call, email | Account executive | Pre-brief |
| Admins and champions | Dates, migration steps, tooling | Email, in-product banner, webinar | Product | Announcement |
| Developers | Deprecated endpoints, replacements, dates | Changelog, docs, Deprecation and Sunset headers, SDK warnings | Engineering | Announcement |
| Partners (resellers, MSPs) | All of the above, earlier, plus tenant tooling | Partner briefing, partner portal | Partner team | Pre-brief, before public notice |
| Internal (sales, customer success, support) | Talk track, FAQ, escalation path | Enablement session, internal page | PM and PMM | Before pre-briefs |

## Sequence
| When | Message | Audience |
|---|---|---|
| T minus [n] weeks | Internal enablement | Internal |
| T minus [n] weeks | Pre-brief | Top accounts and partners |
| T (announcement) | Public notice with every date and the successor | All |
| Fixed intervals (e.g., quarterly, then monthly) | Reminder with migration progress and next date | Accounts not yet migrated |
| [n] days before each milestone | Milestone warning | Affected accounts |
| Final warning | Last call with consequences | Accounts not yet migrated |
| After retirement | Confirmation and data deletion notice | All affected |

## Programmatic signals
- [ ] Deprecation and Sunset headers on deprecated endpoints
- [ ] Deprecated tags in schemas and SDKs, with runtime warnings
- [ ] Status field in the API or console
- [ ] Entry in the deprecation registry with earliest removal date

## Key messages (approved by legal)
1.
2.
3.

## Feedback loop
Customer replies and tickets summarized weekly by theme; owner: [name].
