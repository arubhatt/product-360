<p class="lead">A Product 360 is never finished, so "is it done?" is the wrong question. The useful questions are how mature each dimension is and which one is holding the product back. This appendix gives you a five-level scale, a table for each of the nine dimensions that says what each level looks like in documents you can open, an overlay for AI-powered products, and the templates and prompts to score your 360 every quarter.</p>

:::note This is the book's own model
The maturity levels, criteria and scoring rules in this appendix are The Product 360 Handbook's framework, not an industry standard. As Chapter 37 notes, the five-level shape borrows from the Capability Maturity Model that Watts Humphrey and the Software Engineering Institute developed; the content of each level is this book's.
:::

## How to use the model

Score each of the nine dimensions separately, from evidence. A score is the highest level whose criteria the dimension meets in full, along with every level below it. If you can't show a document, a calendar entry or a decision log line for a criterion, it doesn't count. When evidence is mixed, take the lower level and write down why.

Then find the two weakest dimensions. Don't average the nine scores. A product with Measure at 5 and Lifecycle at 1 averages 3, and the average hides a well-instrumented dashboard sitting next to an end-of-life notice that will surprise customers. The weakest dimension is where the next unpleasant question will come from, so it's where your next quarter of 360 work goes.

When two dimensions tie for weakest, break the tie with the gap list from Chapter 00: pick the one with the higher business risk or the nearer fixed date (a launch, a renewal wave, a regulatory deadline).

For each of the two weakest dimensions, plan to move up **one level** in the next quarter. Each dimension table below names the chapters that teach the move. One level is the right ambition: jumping from 1 to 4 means building an artifact and a ritual and a decision habit at once, and the ritual usually dies first.

Re-score every quarter, as part of the quarterly business review or the Product 360 health review in Chapter 37. Keep the previous scores next to the new ones. A dimension that slips a level is telling you something specific: an owner left, a ritual stopped, or an event (a pricing change, a reorg, a model deprecation) made a durable artifact false.

Four rules keep the scores honest:

- **Evidence over intent.** "We review the roadmap monthly" counts only if the calendar shows the last three reviews happened and the decision log shows what they decided.
- **Score the whole scope.** If personas cover the direct business but not the partner channel, the dimension is only partly defined. Score the weakest part that's in scope.
- **Level 5 takes time.** A dimension reaches level 5 only after holding level 4 for at least two consecutive quarters.
- **Someone else checks.** Ask a peer PM, your manager or product ops to challenge your scores, or run the challenge prompt later in this appendix. It's easy to score your own work generously.

:::onramp If you're new to product management
You don't need every dimension at level 5. Level 3 or 4 across the board, with one or two dimensions lower for a known reason, is a healthy 360. The model is for deciding where to spend your next hour of 360 work, not for grading yourself.
:::

## The five levels

The levels follow the questions Chapter 37 asks of any dimension. Does an artifact exist? Does it have an owner and a review date? Is it current, with cited sources? Does a ritual make decisions from it? Is it consistent with the other artifacts and readable by a harness, and does it get better each cycle? Each "yes" is a step up.

| Level | Name | What it means | The test |
|---|---|---|---|
| 1 | **Absent** | No artifact answers the dimension's question. The answer lives in someone's head, a meeting or a slide from a past planning cycle. | Ask three people the dimension's question and you get three answers. |
| 2 | **Ad hoc** | An artifact exists but was written for one event, covers only part of the scope, has no named owner or review date, or is stale or contradicted by another artifact. | You can open a document, but you can't say who keeps it true or when it last was. |
| 3 | **Defined** | The spine artifacts for the dimension exist, cover the whole scope, name an owner and a review date, are current and cite their sources. | Anyone can open the artifact from the Product 360 index and trust it today. |
| 4 | **Managed** | A named ritual reviews the artifacts on their cadence, decisions made from them are in the decision log, and stale items are flagged and fixed within one cycle. | The calendar and the decision log show the artifact being used to decide something. |
| 5 | **Compounding** | The artifacts have held level 4 for two or more quarters, pass a consistency audit against neighboring dimensions, are readable by an approved AI harness, and each cycle's outcomes feed back into them. | The artifact is measurably better than a year ago, and the next decision it supports takes less effort than the last. |

The step from 3 to 4 is the easiest to miss. A defined artifact that no ritual uses decays quietly, because nobody notices it going stale until an executive asks a question it should answer. The step from 4 to 5 is about learning: post-launch reviews update the personas, experiment readouts update the metric tree, and missed forecasts update the business model.

## The nine dimensions

Each table describes what you can observe at each level, the artifacts that indicate it and the chapters that teach the move to the next level. Template ids in code font refer to Appendix A.

### 1. Customer

*Who is this for, and what job are they hiring it to do?*

| Level | What you can observe | Artifacts that indicate it | Read to move up |
|---|---|---|---|
| 1 Absent | Sales, engineering and product describe the customer differently. No written problem statement exists. | None, or a persona slide nobody can source | Ch. 01 |
| 2 Ad hoc | Personas exist but cover users only, or date from a past launch. Discovery happens before big releases and stops after. Interview notes sit in personal folders. | Persona deck without owner or date; scattered interview notes | Ch. 01, 10 |
| 3 Defined | A problem hypothesis and personas cover users, the economic buyer and gatekeepers such as security reviewers. Each persona cites interviews or data from the last year and names an owner. | `product-hypothesis`, `b2b-persona`, `job-statements`, `journey-map` | Ch. 01, 17, 27 |
| 4 Managed | Discovery runs on a standing cadence. The weekly team sync reviews the discovery log, and roadmap and positioning decisions in the log cite customer evidence. | `interview-snapshot`, discovery log, `10-insight-brief`, decision log entries citing evidence | Ch. 09, 21, 27 |
| 5 Compounding | Post-launch reviews, support themes and win/loss findings change the personas and the hypothesis, and the change history shows it. Killed hypotheses are recorded with the evidence that killed them. | `09-voc-report`, `13-win-loss-analysis`, `27-feature-request-triage-policy`, persona change history | Hold the level; re-grill yearly (Ch. 37) |

### 2. Strategy

*Where do we play, how do we win, and what will we say no to?*

| Level | What you can observe | Artifacts that indicate it | Read to move up |
|---|---|---|---|
| 1 Absent | The strategy is whatever the last executive review approved. The team can't name what it has decided not to do. | None, or a vision line on an all-hands slide | Ch. 02, 03 |
| 2 Ad hoc | A strategy deck exists from the last planning cycle but no longer matches the roadmap or the market. Competitor knowledge is anecdotal. | Last year's strategy deck; ad hoc competitor notes | Ch. 02, 03, 13 |
| 3 Defined | A one-page strategy states the diagnosis, the guiding policy and the explicit no's. A competitive landscape covers the real alternatives, including doing nothing. Both have an owner and a review date. | `02-vision-statement`, `03-strategy-kernel`, `03-strategy-one-pager`, `13-competitive-landscape` | Ch. 03, 16, 29 |
| 4 Managed | The monthly product review checks roadmap changes against the one-pager. The competitive landscape is refreshed quarterly, and strategic changes go through the decision log rather than drifting in. | Decision log entries that cite the strategy; `16-competitive-threat-monitor`; quarterly landscape updates | Ch. 14, 16, 20 |
| 5 Compounding | Each annual refresh records which strategic bets paid off and which didn't, and the next strategy reflects it. Moat and platform assessments are revisited with evidence. | `16-seven-powers-assessment`, `16-moat-scorecard`, `14-platform-map`, `29-annual-plan-narrative` | Hold the level; annual re-grill (Ch. 37) |

### 3. Business

*How does this make money, and is the money worth it?*

| Level | What you can observe | Artifacts that indicate it | Read to move up |
|---|---|---|---|
| 1 Absent | The PM can't state revenue, margin or the pricing metric without asking finance. | None | Ch. 13, 15 |
| 2 Ad hoc | A business case exists from the original funding decision, or finance owns a model the PM has never opened. Pricing exists but nobody has written down why. | Original business case; a finance model; a price list | Ch. 12, 13, 15 |
| 3 Defined | A business model and unit economics summary shows revenue, growth, gross margin, the pricing metric and the main cost drivers, reconciled with finance's numbers and owned by the PM. | `13-business-case`, `15-value-metric-assessment`, `12-evc-model` | Ch. 15, 29 |
| 4 Managed | The quarterly business review walks the summary. Pricing and packaging changes go through a written proposal and the decision log. Variances between plan and actual get an owner. | `29-qbr-outline`, `15-pricing-packaging-proposal`, `15-price-change-impact-plan`, decision log | Ch. 09, 12, 15 |
| 5 Compounding | Forecasts are compared with actuals each quarter and the model's assumptions are updated. Pricing changes are measured after launch, and the results shape the next change. | `09-clv-model-brief`, `12-lifecycle-pricing-plan`, price-change readouts | Hold the level; annual re-grill (Ch. 37) |

### 4. Build

*What are we building next, and how does it get made?*

| Level | What you can observe | Artifacts that indicate it | Read to move up |
|---|---|---|---|
| 1 Absent | The plan is the ticket backlog. Nobody can say what ships next quarter or why. | Ticket queue only | Ch. 03, 06 |
| 2 Ad hoc | A roadmap exists as a feature list with dates, often several versions for different audiences. PRDs are written for some features and not updated when the scope changes. | Feature-and-date roadmap; PRDs that describe what was planned, not what shipped | Ch. 03, 04, 06 |
| 3 Defined | An outcome roadmap (now, next, later) traces each item to a strategic choice and a metric. PRDs and PR/FAQs follow a standard template, and a backlog policy says how items get in and out. | `03-now-next-later-roadmap`, `04-prd`, `34-pr-faq`, `03-backlog-policy`, `06-release-plan` | Ch. 06, 11, 28 |
| 4 Managed | The monthly roadmap refresh and biweekly sprint reviews change the plan from evidence, and cuts are logged. Technical debt is a visible line in planning, not a surprise. | `11-cycle-review`, `06-tech-debt-register`, `03-roadmap-communication-pack`, decision log | Ch. 05, 07, 11 |
| 5 Compounding | Post-launch reviews compare each release with the outcome its PRD promised, and the gap informs how the next bets are sized. The team's delivery process is itself reviewed and adjusted. | `05-post-launch-review`, `05-iteration-plan`, `11-process-health-check` | Hold the level; quarterly re-grill (Ch. 37) |

### 5. Measure

*How do we know it's working?*

| Level | What you can observe | Artifacts that indicate it | Read to move up |
|---|---|---|---|
| 1 Absent | No agreed definition of success. Different teams quote different numbers for the same thing. | None, or vendor default dashboards | Ch. 02, 05 |
| 2 Ad hoc | Dashboards exist with dozens of charts but no North Star. Metrics are pulled for a review and then ignored. Definitions live in the analyst's head. | Large dashboard; one-off analyses | Ch. 02, 05, 17 |
| 3 Defined | A North Star and input metric tree are written down with definitions, owners and sources. OKRs tie to the tree. Event tracking follows a tracking plan. | `02-north-star-tree`, `02-okr-set`, `05-tracking-plan`, `18-metric-dictionary` | Ch. 18, 19, 29 |
| 4 Managed | A weekly metrics review walks the same pack every week, explains exceptions and assigns owners. Experiments have pre-registered designs and written readouts. Numbers in executive reviews are checked against source. | `18-weekly-business-review-pack`, `29-weekly-business-review`, `05-experiment-design`, `05-ab-readout`, `19-verification-checklist` | Ch. 05, 09, 17 |
| 5 Compounding | Metric definitions are revised when they stop predicting outcomes, and the change is logged. Experiment results update the metric tree. The harness can answer routine metric questions from connected, trusted sources. | `17-decision-review`, `18-data-trust-check`, metric tree change history | Hold the level; quarterly re-grill (Ch. 37) |

### 6. Go-to-market

*How does it reach, convince and keep customers?*

| Level | What you can observe | Artifacts that indicate it | Read to move up |
|---|---|---|---|
| 1 Absent | Sales describes the product in its own words, differently by region. Launches happen when engineering finishes. | None | Ch. 24, 25 |
| 2 Ad hoc | Positioning exists from an earlier version of the product. Launch materials are built per launch with no tiering. Enablement is a slide deck and a recorded call. | Old positioning doc; one-off launch decks | Ch. 24, 25, 27 |
| 3 Defined | Positioning and messaging reflect the current product and its real competitive alternatives. Launches are tiered, with a plan and readiness criteria. Claims are substantiated. | `24-positioning-statement`, `24-messaging-framework`, `24-claims-log`, `25-launch-plan`, `27-sales-enablement-kit` | Ch. 25, 26, 27 |
| 4 Managed | Launch go/no-go meetings decide from readiness evidence. Field feedback and win/loss reach the product team on a cadence and change the roadmap or the messaging. | Go/no-go records, `27-feature-request-triage-policy`, `13-win-loss-analysis`, `27-customer-onboarding-plan` | Ch. 08, 26, 27 |
| 5 Compounding | Each launch and event has an impact report that changes how the next one is planned. Positioning is tested against win/loss evidence and revised at the annual refresh. | `26-event-impact-report`, `05-post-launch-review`, `08-attribution-assessment` | Hold the level; annual re-grill (Ch. 37) |

### 7. Operate

*How do we run it week to week?*

| Level | What you can observe | Artifacts that indicate it | Read to move up |
|---|---|---|---|
| 1 Absent | Meetings exist but have no fixed agenda or output. Decisions are made in chat and forgotten. | Recurring meetings only | Ch. 28, 29 |
| 2 Ad hoc | Some rituals have agendas. A decision log or risk register was started and abandoned. Escalations go to whoever is loudest. | Abandoned decision log or risk register | Ch. 28, 29 |
| 3 Defined | An operating cadence names each ritual, its attendees, the artifacts it reviews and the decision it produces. The decision log and risk register exist and are current. | `operating-cadence`, `29-decision-log`, `29-risk-register`, `29-escalation-policy` | Ch. 28, 29 |
| 4 Managed | The rituals happen as planned, and each produces logged decisions. The risk register is reviewed in a ritual, and rituals that stop producing decisions get cut. | Calendar history, `29-monthly-product-review`, `28-daci-decision`, decision log with recent entries | Ch. 28, 32 |
| 5 Compounding | The cadence is reviewed each quarter and changed from evidence (attendance, decisions produced). Routine briefs are drafted by an approved harness and checked by people, which frees the rituals for judgment. | `11-process-health-check`, `32-weekly-ai-routine`, `28-tool-stack-map` | Hold the level; quarterly review (Ch. 37) |

### 8. Lifecycle

*Where is it in its life, and what happens next?*

| Level | What you can observe | Artifacts that indicate it | Read to move up |
|---|---|---|---|
| 1 Absent | Nobody has stated the product's lifecycle stage. Legacy versions and old features have no end-of-life plan, and customers are the ones asking. | None | Ch. 30 |
| 2 Ad hoc | A stage assessment or sunset plan exists for one offering, usually the one causing escalations, but not for the rest of the scope. | One sunset plan or end-of-sale notice | Ch. 30 |
| 3 Defined | Every offering in scope has a lifecycle stage assessment with evidence. Stage-gate criteria say what triggers a move to the next stage. | `30-lifecycle-stage-assessment`, `30-stage-gate-criteria`, `30-end-of-life-plan` | Ch. 29, 30 |
| 4 Managed | The quarterly business review or portfolio review checks each offering's stage and gate criteria. Sunset decisions are logged with a migration plan and customer communication. | `29-portfolio-review`, `30-sunset-decision-memo`, `30-migration-plan`, `30-deprecation-communication-plan` | Ch. 10, 12, 23 |
| 5 Compounding | Lessons from each sunset or relaunch change the gate criteria. Pricing, investment and staffing follow the stage, and the record shows it. | `12-lifecycle-pricing-plan`, `10-relaunch-plan`, `23-scale-up-readiness-checklist` | Hold the level; annual re-grill (Ch. 37) |

### 9. Leadership

*Who needs to be aligned, and are they?*

| Level | What you can observe | Artifacts that indicate it | Read to move up |
|---|---|---|---|
| 1 Absent | The PM learns who can block a decision when they block it. Ownership boundaries with neighboring teams are unclear. | None | Ch. 36 |
| 2 Ad hoc | A stakeholder list exists, often an org chart excerpt. Decision rights are argued case by case. | Contact list; email threads | Ch. 28, 36 |
| 3 Defined | A stakeholder map shows influence and position. Major decisions have a DACI with one approver. Boundaries with neighboring products are written and agreed. | `36-stakeholder-map`, `36-daci-decision`, `36-team-charter` | Ch. 34, 35, 36 |
| 4 Managed | The stakeholder map is reviewed quarterly and drives an engagement plan. Executive communications follow a plan and a standard format, and their outcomes are logged. | `36-stakeholder-engagement-plan`, `35-executive-briefing-outline`, `34-decision-memo`, decision log | Ch. 34, 35, 36 |
| 5 Compounding | Alignment problems are caught before decisions, not after. The team charter and coaching plans are updated from what each quarter taught. Stakeholders use the 360 index to answer their own questions. | `36-pm-competency-self-assessment`, `36-one-on-one-coaching`, index access history | Hold the level; quarterly re-grill (Ch. 37) |

:::leader For product leaders: comparing products
In a portfolio, ask every PM to score with this appendix and bring the evidence, not just the numbers. Compare dimensions across products rather than totals. When several products share a weak dimension, the cause is often in the portfolio's own operating model, and the fix belongs to you or to product operations (Chapter 28), not to each PM separately.
:::

## The AI overlay

For an AI-powered product, Chapter 00 adds four artifacts to the spine, and each lives in a dimension: the eval plan in Measure, the AI cost model in Business, the model and vendor register in Lifecycle and the AI risk assessment in Operate. Score each of the four on its own with the table below, and record it next to its host dimension.

When an AI element scores lower than its host dimension, keep both scores and treat the gap as a candidate for one of the two weakest. A Measure dimension at level 4 with an eval plan at level 2 means the dashboard is trusted while nobody can say whether the AI's answers are any good. A customer can find that gap before you do.

| Level | Evals (Measure) | Cost (Business) | Model register (Lifecycle) | AI risk (Operate) |
|---|---|---|---|---|
| 1 Absent | Quality is judged by demos and anecdotes. No eval set exists. | Nobody knows what one task or outcome costs in inference. | Nobody can list which models and versions are in production. | No written failure modes. Guardrails exist only in code. |
| 2 Ad hoc | An eval set exists for one feature or was built once before launch and not rerun. "Good" isn't defined in writing. | Inference cost appears as a line in the cloud bill, not per task, user or outcome. | A list of models exists but lacks versions, owners or deprecation dates. | A risk review was done for launch and not revisited. Regulatory duties are unknown or assumed. |
| 3 Defined | An eval plan defines "good" for each AI feature, names who decided it, and records current scores and the score that blocks a release. Cases come from real failures. | An AI cost model shows cost per task or outcome, its trend and its effect on gross margin, reconciled with finance. | The register lists every model and version, the vendor, the owner and known deprecation dates. | An AI risk assessment lists failure modes, guardrails, human approval points and regulatory duties by market, with an owner. |
| 4 Managed | Evals run before every release and gate it. A monthly AI quality and cost review tracks scores against production signals. | Cost per outcome is in the weekly or monthly review, with an owner for variance. Pricing decisions cite it. | Deprecation dates feed the roadmap and the lifecycle review, and a runbook covers model changes. | A ritual reviews the risk assessment, incidents update it, and launch go/no-go uses it. |
| 5 Compounding | Production failures and post-incident reviews add eval cases every cycle. Eval scores predict customer-visible quality. | Cost forecasts are compared with actuals, and model or architecture choices are made from the trend. | Model swaps have been run through the runbook at least once, and lessons changed it. | Red-team findings and incidents feed back into guardrails and the eval set. Regulatory documentation is produced from the assessment, not written fresh each time. |

Chapters to read to move up: Chapter 31 for all four artifacts; Chapter 28 for the monthly AI quality and cost review (`28-ai-quality-cost-review`); Chapter 15 for pricing that covers inference cost (`15-ai-pricing-model-comparison`); Chapter 30 for the model deprecation runbook (`30-model-deprecation-runbook`); and Chapter 33 for impact assessments, red-teaming and incident response (`33-ai-impact-assessment`, `33-red-team-plan`, `33-ai-incident-response-plan`).

:::ai Scoring with a harness
A harness connected to your 360 can do most of the evidence gathering: find each artifact, read its owner and review date, check the calendar for rituals and match decision log entries to artifacts. It can't tell whether a ritual's decisions were good, and it can count a passing mention as an artifact unless you tell it not to. Use the prompts below to draft the scores, then check the evidence for every score of 4 or 5 yourself. Use only tools approved for the data your 360 contains.
:::

## The Beacon case: scoring at day 90

:::example Beacon's first maturity score
Chapter 37 ends Beacon's first 90 days with a health review. This is that review's maturity scoring, using the tables above. All Beacon facts are fictional and come from the running case.
:::

At day 90 you score Beacon's 360 with the scoring prompt, then check every score yourself against the evidence it cites. Two scores come down a level when you open the cited documents: the harness had counted the scheduled monthly product review as held, and it had read the Beacon Classic sunset plan as covering every offering.

| Dimension | Level | Evidence | What blocks the next level |
|---|---|---|---|
| Customer | 3 Defined | Personas now include Marcus (economic buyer), Sam (security reviewer) and Leo (MSP partner) alongside Priya and Dana. Sam's job story comes from the Chapter 01 interviews. | No roadmap or positioning decision in the log cites the discovery log yet. |
| Strategy | 3 Defined | The strategy one-pager states the guiding policy (Observe data as an accelerant, not a requirement), and the competitive landscape is current. | The roadmap was checked against the one-pager by the day-60 audit, not by a ritual. |
| Business | 4 Managed | The business model summary is reconciled with the FP&A export (gross margin down from 81% to 72%). Inference cost per resolved incident is in the weekly brief. The 80% margin target is logged as open with an owner. | Level 5 needs two quarters at level 4 and a forecast-to-actual comparison. |
| Build | 3 Defined | The outcome roadmap follows the North Star and OKRs. The Beacon Classic feature cut is logged. | The monthly roadmap refresh hasn't yet completed a cycle that changed the plan from evidence. |
| Measure | 4 Managed | The North Star definition is agreed with finance and product marketing. The weekly exception brief has run four cycles and flagged the drop in diagnosis acceptance rate, with an owner, the same week. | Level 5 needs two quarters at level 4 and a logged revision history for metric definitions. |
| Go-to-market | 3 Defined | Positioning now says "supervised remediation." Launch and event plans for Northlight Live exist. | The launch go/no-go hasn't happened, and field feedback doesn't yet reach the product team on a cadence. |
| Operate | 3 Defined | The cadence is on the calendar, the decision log is active and the weekly brief runs. | The risk register and the AI risk assessment aren't reviewed in any ritual; the weekly brief covers metrics only. |
| Lifecycle | 2 Ad hoc | Beacon Classic has a stage assessment and a sunset plan. | Correlate and Diagnose have no stage assessment as offerings in their own right. |
| Leadership | 3 Defined | The stakeholder map and the DACI for the Observe boundary exist. The boundary is agreed, with a joint quarterly roadmap review. | No ritual uses the stakeholder map yet. |

The AI overlay adds four scores: cost at level 4 (it's in the weekly brief, and the pricing work cites it), and evals, the model register and AI risk at level 3. Each exists with an owner, and the eval plan and risk assessment take cases from the hallucinated root cause in the design-partner pilot. None of the three is reviewed in a ritual yet. Evals at 3 under a Measure score of 4 is exactly the gap the overlay is meant to show.

**The two weakest.** Lifecycle, at 2, is the clear first choice. Six dimensions tie at 3, so the tie-break decides the second. Beacon Agents goes live at Northlight Live with supervised remediation in customers' production environments, and no ritual reviews the AI risk assessment. Go-to-market shares that fixed date, but an agent acting in production without a reviewed risk assessment carries the higher business risk, so Operate is the second focus.

**The plan for next quarter**, one level each:

- **Lifecycle, 2 to 3.** Assess Correlate and Diagnose with the lifecycle stage assessment, write stage-gate criteria for all three offerings and re-grill the dimension in week 2 (Chapters 30 and 37).
- **Operate, 3 to 4.** Add the risk register and the AI risk assessment to the monthly product review, and make the AI risk assessment an input to the Northlight Live go/no-go (Chapters 29 and 33).
- **Watch item, not a focus.** Add eval scores to the monthly review so the eval plan can reach level 4 alongside Measure (Chapter 31).

Nothing else gets new 360 work this quarter. The other dimensions keep their cadence and get re-scored at the next review.

## Templates

```template id="appendix-c-maturity-self-assessment" title="Product 360 self-assessment"
# Product 360 self-assessment · [Product] · [Quarter] · [Date]

**Scored by:** [PM]   **Challenged by:** [peer PM, manager or product ops]
**Scope:** [link to the scope paragraph on the Product 360 index]
**Evidence sources:** [Product 360 index, decision log, calendar, artifact links]
**Previous assessment:** [link, or "first assessment"]

## Scoring rules
- A level counts only if every criterion for it and every level below is met, with evidence.
- Mixed evidence takes the lower level.
- Level 5 requires level 4 held for two consecutive quarters.
- Score the weakest part of the scope.

## Scores by dimension
| Dimension | Level (1 to 5) | Evidence (artifact, ritual or log entry, with link and date) | Lowest unmet criterion for the next level | Previous level | Confidence (high / medium / low) |
|---|---|---|---|---|---|
| Customer | | | | | |
| Strategy | | | | | |
| Business | | | | | |
| Build | | | | | |
| Measure | | | | | |
| Go-to-market | | | | | |
| Operate | | | | | |
| Lifecycle | | | | | |
| Leadership | | | | | |

## AI overlay (AI-powered products)
| AI element | Host dimension | Level (1 to 5) | Evidence | Lower than host? |
|---|---|---|---|---|
| Evals | Measure | | | |
| Cost | Business | | | |
| Model register | Lifecycle | | | |
| AI risk | Operate | | | |

## The two weakest
1. [Dimension, level] because [evidence]
2. [Dimension, level] because [evidence; if tied, the business risk or fixed date that broke the tie]

## Action plan (one level up per weak dimension)
| Dimension | From level | To level | Unmet criterion | Action | Template or chapter | Ritual that will use it | Owner | Due | Evidence it's done |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |

## Not doing this quarter
[Dimensions and actions deliberately deferred, and why.]

## Challenges raised and how they were resolved
| Dimension | Challenge | Resolution (score kept or changed, and why) |
|---|---|---|
| | | |
```

```template id="appendix-c-maturity-review" title="Quarterly maturity review"
# Quarterly maturity review · [Product] · [Quarter] · [Date]

**Attendees:** [PM, manager, product ops, key partners]
**This quarter's self-assessment:** [link]   **Last quarter's:** [link]

## Movement
| Dimension | Last quarter | This quarter | Change | Why it moved (or didn't) |
|---|---|---|---|---|
| Customer | | | | |
| Strategy | | | | |
| Business | | | | |
| Build | | | | |
| Measure | | | | |
| Go-to-market | | | | |
| Operate | | | | |
| Lifecycle | | | | |
| Leadership | | | | |
| AI overlay (evals, cost, register, risk) | | | | |

## Last quarter's action plan
| Action | Owner | Done? | Evidence | Did the level move? |
|---|---|---|---|---|
| | | | | |

## Slips
[Every dimension that dropped a level: the cause (owner left, ritual stopped, event made an artifact false) and the fix.]

## Ritual health
| Ritual | Held as planned (n of n) | Decisions logged | Keep / change / cut |
|---|---|---|---|
| | | | |

## Decisions
- Focus dimensions for next quarter: [two, with reasons]
- Actions approved: [link to the new self-assessment's action plan]
- Anything escalated: [what, to whom]
- Next review: [date]
```

## Prompts

```prompt title="Score a Product 360 from its documents"
Goal: Draft a maturity score for each dimension from evidence, ready for you to check.
Paste in (or connect the harness to): the Product 360 index, the artifacts it links, the decision log, the operating cadence and calendar evidence of which rituals were held, last quarter's self-assessment if one exists, and the level tables from Appendix C. This material is usually confidential; use only tools approved for it.

You are helping a product manager score the Product 360 for [product] against the maturity model in Appendix C of The Product 360 Handbook. The model has five levels: 1 Absent, 2 Ad hoc, 3 Defined, 4 Managed, 5 Compounding. The nine dimensions are Customer, Strategy, Business, Build, Measure, Go-to-market, Operate, Lifecycle and Leadership.

For each dimension:
1. List the evidence you found: artifact name, owner, last-reviewed date, the ritual that reviews it (if any) and decision log entries that cite it. Give a source for each item.
2. Test the level criteria from level 2 upward, and stop at the first level whose criteria are not all met. Quote the criterion that failed.
3. Give the score. If evidence is mixed, give the lower level and say why. Give level 5 only if earlier assessments show level 4 held for two consecutive quarters.
4. Rate your confidence (high, medium, low) and name any evidence you could not open or date.

Rules:
- A passing mention of a topic in another document is not an artifact.
- A meeting on the calendar is not a held ritual unless notes or decision log entries show it happened.
- Score the weakest part of the scope.

If the product is AI-powered, score the four AI elements (evals, cost, model register, AI risk) against the AI overlay the same way, and flag any that score below their host dimension.

Finish with a table of all scores, the two weakest dimensions (break ties by business risk or nearest fixed date, and say which you used) and a list of evidence gaps for me to check.

[Appendix C level tables]
[Product 360 index and artifacts]
[decision log, cadence, calendar evidence]

Check the output: open the evidence cited for every score of 4 or 5 and confirm the ritual actually ran and decided something. Confirm that no level 3 rests on an artifact without an owner or review date. If the harness's scores and yours differ, record the reason in the self-assessment.
```

```prompt title="Turn maturity scores into a quarterly improvement plan"
Goal: Get a realistic one-quarter plan that moves the two weakest dimensions up one level each.
Paste in: the completed self-assessment, the Appendix C tables for the two weakest dimensions, the operating cadence, the next quarter's fixed dates (launches, reviews, renewals, regulatory deadlines) and the team's available time.

My Product 360 for [product] scored [scores]. The two weakest dimensions are [dimension 1, level] and [dimension 2, level].

For each of the two:
1. List the criteria from the next level up that are not yet met, quoting the Appendix C table.
2. Propose no more than four actions that would meet those criteria. For each, give the artifact or template to build or repair, the ritual that will use it, an owner role, a due date inside the quarter and the evidence that will show it's done.
3. Flag any action that needs a decision or time from someone outside the product team, and name who.

Then:
- List anything you'd deliberately not do this quarter, and why.
- Estimate the hours per week the plan costs the PM.

Do not propose moving any dimension more than one level, and do not add actions for dimensions other than these two unless one of them blocks the plan.

Check the output: every action should trace to an unmet criterion. If the PM hours look higher than you can spend, cut actions rather than stretching dates past the quarter.
```

```prompt title="Challenge a self-assessed maturity score"
Goal: Find the scores you've inflated before your manager or a peer does.
Paste in: your completed self-assessment with its evidence links, and the Appendix C level tables. Use only approved tools.

Act as a skeptical reviewer of this Product 360 self-assessment for [product]. For each dimension scored 3 or higher:
1. Argue that the score should be one level lower. Use the Appendix C criteria and the evidence provided, and name the weakest piece of evidence.
2. Ask me one question that would settle it.

Don't change any score yourself. Don't invent evidence for or against. If the evidence for a score is strong, say so in one line and move on.

[self-assessment]
[Appendix C level tables]

Check the output: answer each question with evidence, not explanation. Lower any score you can't defend, and record each challenge and its resolution in the self-assessment.
```

## Checklist

- [ ] Every dimension is scored from evidence I can open, with a link and date for each item.
- [ ] Mixed evidence was scored at the lower level, and the reason is written down.
- [ ] No dimension is at level 5 without two consecutive quarters at level 4.
- [ ] For an AI-powered product, evals, cost, the model register and AI risk are scored, and any element below its host dimension is flagged.
- [ ] Someone other than me challenged the scores, and each challenge has a written resolution.
- [ ] The two weakest dimensions are named, and any tie was broken by business risk or a fixed date.
- [ ] The action plan moves each weak dimension up one level, and every action traces to an unmet criterion.
- [ ] Each action names the ritual that will use the artifact it produces.
- [ ] The next quarterly maturity review is on the calendar, with last quarter's scores attached.
