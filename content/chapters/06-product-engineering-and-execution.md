<p class="lead">Strategy becomes product only when engineers build it, test it and put it in front of customers. This chapter covers the working agreements that make that happen well: how a PM partners with engineering, plans a sprint, writes a story an engineer (or a coding agent) can build from, triages bugs, treats technical debt as a product decision and releases safely. It also covers what changes in 2026, now that writing code is cheap and reviewing it isn't.</p>

## Why this matters

Most product failures in execution aren't failures of effort. The team worked hard and shipped something, but it was the wrong slice, it arrived late because nobody protected capacity for the escalations that always come, or it shipped with a quality problem that cost the account the team was building it for. Each of those traces back to a working agreement between product and engineering that was vague, missing or ignored.

As a senior PM you own outcomes across several teams, field date requests from sales and executives, and rarely see the code. Your leverage over execution comes from a few artifacts: the story and its acceptance criteria, the story map, the definitions of ready and done, the triage policy, the debt register and the release plan. Get them right and engineering can make good decisions without you in the room.

There's a 2026 reason too. With AI coding agents, generating code got much cheaper, while reviewing, verifying and safely releasing it did not. The bottleneck moves upstream, to the clarity of what you ask for, and downstream, to review capacity and release controls. You have direct influence over both.

This chapter covers the Build dimension of your Product 360. Chapter 11 goes deeper on delivery methodologies (Scrum, Kanban and their variants) and Chapter 10 on product specifications. Here the focus is the week-to-week work between a PM and the engineers building the product.

## Core concepts and frameworks

### The PM and engineering partnership

The cleanest statement of who owns what comes from the Scrum Guide, written by Ken Schwaber and Jeff Sutherland and last revised in 2020. In Sprint Planning, the Product Owner brings the *why* (a Sprint Goal) and proposes the *what*; the Developers decide the *how* and how much they can take on. Whatever process your team runs, that split holds up well:

| The PM owns | Engineering owns | Both own |
|---|---|---|
| The customer problem and the evidence for it | The design of the solution | The scope trade-off |
| The outcome and how it will be measured | The estimate and the plan | The slice that ships first |
| The order of work | The quality bar and how it's enforced | The risks and how to retire them |

The partnership breaks when either side crosses the line. A PM who dictates implementation loses the engineers' best ideas. A PM who accepts an estimate as a fixed fact, without negotiating scope, has stopped doing the job.

Ron Jeffries described how a requirement should flow between the two in a 2001 essay on what he called **Card, Conversation, Confirmation**. The *card* is a token, just enough text to identify the requirement. The *conversation* is the ongoing exchange between the customer (or the PM standing in for them) and the people building it, supported by examples. The *confirmation* is a set of acceptance tests, agreed at the start of the iteration and ideally executable. The point of the three Cs is that the written story isn't the specification. The conversation is, and the confirmation records what the conversation decided.

In enterprise and platform products, the "customer" in that conversation is often a developer, an administrator, a partner or a security reviewer. A PM who joins refinement, brings that customer's evidence and agrees the confirmation tests gets what the customer needs.

Use these signals to check the partnership's health (they're this book's synthesis, not research findings):

- Engineers can state the customer problem behind the work they're doing this week.
- Scope changes are negotiated, not dictated, in both directions.
- You can name the top three engineering risks on your product without looking them up.
- Technical debt and reliability work sit on the same roadmap as features.
- You attend demos and reviews rather than only reading status.

:::onramp If you're new to working with engineers
Spend your first month listening in refinement, planning, demos and incident reviews. Ask one question in each: "What would make this easier to build?" You'll learn the system's constraints faster than any architecture document could teach you.
:::

### Sprint planning, cadence and capacity

The Scrum Guide defines a Sprint as a fixed-length event of one month or less. Sprint Planning answers three questions: why this Sprint is valuable (the Sprint Goal), what can be done (the items selected with the Product Owner) and how the work will get done (which the Developers plan). The guide timeboxes Sprint Planning to at most eight hours for a one-month Sprint and less for shorter ones. Above the Sprint sits the **Product Goal**: a future state of the product that the team plans against.

The Sprint Goal is the PM's main tool in planning. A good one names an outcome or a learning ("an on-call engineer can approve a rollback from the incident view, end to end, in the staging tenant"), not a list of tickets. When work surprises the team mid-sprint, the goal tells everyone what to protect.

**Capacity** is where plans quietly fail. Plan against the person-days actually available after leave, on-call rotation, support duty and meetings. Then reserve explicit capacity for unplanned work: bugs, escalations and debt. There's no authoritative standard for how much to reserve. Treat it as a team choice, set from the team's own history of how much unplanned work arrived in recent sprints, and revisit it when that history changes.

Ryan Singer's *Shape Up*, written about how Basecamp works, offers a useful reframe. An **appetite** is a time budget: an estimate starts from a design and produces a number, while an appetite starts from a number and shapes the design to fit. Singer calls this fixed time, variable scope. Even in two-week sprints, "how much is this worth to us?" opens a scope conversation better than "how long will it take?"

Enterprise PMs usually run two clocks at once. The team cadence (one or two weeks) is internal. The customer-facing clock (a quarterly plan, a release train, a launch at an annual event) is external and often contractual. Your job is to keep each Sprint Goal tied to an outcome on the quarterly plan, and to protect capacity for large-account escalations so they don't silently eat the plan.

### Estimation: story points and the no-estimates debate

Ron Jeffries, writing in 2019, traced **story points** back to early Extreme Programming teams. They first estimated in time, then in "ideal days" (a pair working without interruption) multiplied by a load factor. Stakeholders found the day numbers confusing, so the team started calling them points. Points helped mainly to decide how much work fit in an iteration. Jeffries says he may have invented story points and regrets it. He considers points a weak basis for forecasting, calls comparing teams by velocity harmful, and prefers slicing stories small and avoiding estimates where possible, though teams that find points useful can keep them.

The **#NoEstimates** movement pushes further. Vasco Duarte's book *NoEstimates* recommends counting delivered items against the remaining backlog, forecasting from **throughput** (items finished per unit of time), managing scope continuously when the remaining items exceed forecast capacity, choosing the highest-impact items, planning around a sprint goal without sizing each item, and treating a budget as a box of time and investment.

Both camps agree on more than the argument suggests. Each says to slice work small and roughly similar in size, then forecast from what the team has actually delivered. The real disagreement is whether a numeric size per item adds information beyond the count. For a PM, the useful outputs are a **date range with a confidence level** and the **scope levers** that move it.

| Approach | What the team produces | What the PM gets | Watch out for |
|---|---|---|---|
| Story points and velocity | A size per item; points completed per sprint | A forecast in sprints; a planning conversation about size | Points turned into targets or used to compare teams |
| Throughput (no estimates) | A count of finished items per week | A probabilistic date range from history | Items of wildly different size, which break the count |
| Appetite (Shape Up) | A time box and a shaped scope | A fixed date with negotiable scope | Teams that never cut scope, so the box slips anyway |

In B2B, sales and executives ask for dates. Give ranges with a confidence level and name the scope that moves the date. Commit externally only to what has a buffer; commit internally to the Sprint Goal. In 2026 you don't build the forecast by hand: ask your AI harness, through the tracker connector, to pull completed items from recent sprints and produce a throughput-based range with its assumptions stated.

### User stories that carry intent

The familiar template, "As a [type of user], I want [something], so that [reason]," came from Rachel Davies at Connextra, a UK company, in the early 2000s. Mike Cohn, who popularized it and credits her, lists its advantages: it puts who, what and why in a logical order, the first person makes it relatable, stakeholders can fill in the blanks, and it helps prioritization.

Cohn defines **acceptance criteria** as the details that show whether a story was completed correctly. They can be examples, rules, tests or brief notes, and they're the confirmation in Jeffries's three Cs. An **epic** is a large story kept before its details are known and split into smaller, finishable stories as it nears development.

Bill Wake's **INVEST** checklist, published in 2003, tests a story's shape:

- **Independent**: it doesn't overlap other stories and can be scheduled in any order.
- **Negotiable**: it's a placeholder for a conversation, not a contract.
- **Valuable**: it delivers value to the customer, which usually means slicing vertically through every layer rather than building one layer at a time.
- **Estimable**: the team understands it well enough to rank and schedule it.
- **Small**: Wake's original said a few person-weeks at most; modern teams aim far smaller.
- **Testable**: it's understood well enough to write a test for it.

Wake says a good story captures the essence, not the details.

A clearer format for acceptance criteria came from Dan North's 2006 article "Introducing BDD," which introduced behavior-driven development and the **Given-When-Then** template: *Given* some initial context, *When* an event occurs, *Then* ensure some outcomes. The Cucumber project later formalized it as **Gherkin**, with keywords such as Feature, Scenario, Given, When, Then, And, But and Scenario Outline. Cucumber's own guidance is worth following even if nobody automates the tests:

- Keep each example to three to five steps.
- *Given* sets up a known state; it isn't a user interaction.
- *When* describes the event without implementation detail.
- *Then* asserts only outcomes someone can observe, never internal state.

A second notation is worth knowing in 2026. **EARS** (the Easy Approach to Requirements Syntax), developed by Alistair Mavin and colleagues at Rolls-Royce and first published in 2009, writes requirements in five patterns, such as event-driven ("When [trigger], the system shall...") and unwanted behavior ("If [trigger], then the system shall..."). Its terseness suits the specs that coding agents read.

Enterprise stories need criteria that consumer stories often skip: tenant isolation, role-based permissions, the audit log entry, API versioning and the admin path versus the end-user path. Write a separate scenario for each permission boundary, because that's where enterprise defects hide.

:::key A story is three things
A short card that names the need, a conversation that works out the details, and acceptance criteria that confirm the result. If your team only has the card, it's guessing. If it only has a forty-page specification, it has skipped the conversation.
:::

### User story mapping

A flat backlog orders work by build sequence and does a poor job of explaining what the system does. Jeff Patton, who first described **user story mapping** in a 2005 *Better Software* article and set it out in detail in his 2008 essay "The New User Story Backlog is a Map," called the flat backlog "a bag of context-free mulch." It hides gaps, and splitting epics into small stories loses the context that made them make sense.

A story map fixes that by laying work out in two dimensions:

- Across the top, the **activities** users perform, in narrative order from left to right. This row is the **backbone**, and its items aren't ranked against each other.
- Under each activity, the **user tasks** that make it up.
- Under each task, the **stories** that deliver it, prioritized by vertical position: higher means sooner.
- Horizontal lines cut **release slices** across the map. The top slice is the **walking skeleton**: the smallest end-to-end version of the system, built first.

<figure class="fig" markdown="0">
<svg viewBox="0 0 690 380" role="img" aria-label="A user story map for supervised remediation: a backbone of five activities, user tasks beneath, and stories cut into three release slices">
  <text x="20" y="16" class="s">Backbone: activities in narrative order (not ranked)</text>
  <rect x="20" y="24" width="124" height="38" rx="8" fill="var(--a1)" fill-opacity=".16" stroke="var(--a1)" stroke-opacity=".6"/><text x="82" y="48" text-anchor="middle" class="t">Get paged</text>
  <rect x="152" y="24" width="124" height="38" rx="8" fill="var(--a1)" fill-opacity=".16" stroke="var(--a1)" stroke-opacity=".6"/><text x="214" y="48" text-anchor="middle" class="t">Understand</text>
  <rect x="284" y="24" width="124" height="38" rx="8" fill="var(--a1)" fill-opacity=".16" stroke="var(--a1)" stroke-opacity=".6"/><text x="346" y="48" text-anchor="middle" class="t">Decide</text>
  <rect x="416" y="24" width="124" height="38" rx="8" fill="var(--a1)" fill-opacity=".16" stroke="var(--a1)" stroke-opacity=".6"/><text x="478" y="48" text-anchor="middle" class="t">Act</text>
  <rect x="548" y="24" width="124" height="38" rx="8" fill="var(--a1)" fill-opacity=".16" stroke="var(--a1)" stroke-opacity=".6"/><text x="610" y="48" text-anchor="middle" class="t">Close and learn</text>
  <rect x="20" y="70" width="124" height="30" rx="6" class="box"/><text x="82" y="90" text-anchor="middle" class="s">Open incident</text>
  <rect x="152" y="70" width="124" height="30" rx="6" class="box"/><text x="214" y="90" text-anchor="middle" class="s">Read diagnosis</text>
  <rect x="284" y="70" width="124" height="30" rx="6" class="box"/><text x="346" y="90" text-anchor="middle" class="s">Review proposal</text>
  <rect x="416" y="70" width="124" height="30" rx="6" class="box"/><text x="478" y="90" text-anchor="middle" class="s">Run action</text>
  <rect x="548" y="70" width="124" height="30" rx="6" class="box"/><text x="610" y="90" text-anchor="middle" class="s">Record outcome</text>
  <line x1="20" y1="114" x2="672" y2="114" class="ln" stroke-dasharray="5 4"/>
  <text x="20" y="128" class="s" style="fill:var(--a2)">Release 1: walking skeleton</text>
  <rect x="20" y="136" width="124" height="44" rx="6" class="box"/><text x="82" y="154" text-anchor="middle" class="s">Page links to</text><text x="82" y="170" text-anchor="middle" class="s">the incident</text>
  <rect x="152" y="136" width="124" height="44" rx="6" class="box"/><text x="214" y="154" text-anchor="middle" class="s">Root cause with</text><text x="214" y="170" text-anchor="middle" class="s">cited evidence</text>
  <rect x="284" y="136" width="124" height="44" rx="6" class="box"/><text x="346" y="154" text-anchor="middle" class="s">Approve or reject</text><text x="346" y="170" text-anchor="middle" class="s">in one step</text>
  <rect x="416" y="136" width="124" height="44" rx="6" class="box"/><text x="478" y="154" text-anchor="middle" class="s">Roll back the</text><text x="478" y="170" text-anchor="middle" class="s">last deploy</text>
  <rect x="548" y="136" width="124" height="44" rx="6" class="box"/><text x="610" y="154" text-anchor="middle" class="s">Audit entry and</text><text x="610" y="170" text-anchor="middle" class="s">kill switch</text>
  <line x1="20" y1="196" x2="672" y2="196" class="ln" stroke-dasharray="5 4"/>
  <text x="20" y="210" class="s" style="fill:var(--a2)">Release 2</text>
  <rect x="20" y="218" width="124" height="44" rx="6" class="box"/><text x="82" y="236" text-anchor="middle" class="s">Page in chat</text><text x="82" y="252" text-anchor="middle" class="s">with summary</text>
  <rect x="152" y="218" width="124" height="44" rx="6" class="box"/><text x="214" y="236" text-anchor="middle" class="s">Show what the</text><text x="214" y="252" text-anchor="middle" class="s">agent ruled out</text>
  <rect x="284" y="218" width="124" height="44" rx="6" class="box"/><text x="346" y="236" text-anchor="middle" class="s">Show eligible</text><text x="346" y="252" text-anchor="middle" class="s">approvers</text>
  <rect x="416" y="218" width="124" height="44" rx="6" class="box"/><text x="478" y="236" text-anchor="middle" class="s">Restart and</text><text x="478" y="252" text-anchor="middle" class="s">scale actions</text>
  <rect x="548" y="218" width="124" height="44" rx="6" class="box"/><text x="610" y="236" text-anchor="middle" class="s">Draft the review</text><text x="610" y="252" text-anchor="middle" class="s">from the timeline</text>
  <line x1="20" y1="278" x2="672" y2="278" class="ln" stroke-dasharray="5 4"/>
  <text x="20" y="292" class="s" style="fill:var(--a2)">Later</text>
  <rect x="20" y="300" width="124" height="44" rx="6" class="box"/><text x="82" y="318" text-anchor="middle" class="s">Route by MSP</text><text x="82" y="334" text-anchor="middle" class="s">tenant</text>
  <rect x="284" y="300" width="124" height="44" rx="6" class="box"/><text x="346" y="318" text-anchor="middle" class="s">Approval policy</text><text x="346" y="334" text-anchor="middle" class="s">per service</text>
  <rect x="416" y="300" width="124" height="44" rx="6" class="box"/><text x="478" y="318" text-anchor="middle" class="s">Autonomous</text><text x="478" y="334" text-anchor="middle" class="s">allowlisted actions</text>
  <rect x="548" y="300" width="124" height="44" rx="6" class="box"/><text x="610" y="318" text-anchor="middle" class="s">Resolved incidents</text><text x="610" y="334" text-anchor="middle" class="s">feed retrieval</text>
  <text x="20" y="370" class="s" style="fill:var(--muted)">Left to right: the user's story. Top to bottom: priority. Each dashed line cuts a release.</text>
</svg>
<figcaption>A story map for Beacon's supervised remediation, seen from the on-call engineer's side. The walking skeleton is thin but complete: one action, one approval, one audit entry, end to end. A flat backlog would have let the team build all of "Act" before anyone could "Decide."</figcaption>
</figure>

In B2B, put more than one persona on the same backbone: the user, the approver, the administrator and sometimes the buyer. Many enterprise gaps sit in the hand-offs between them (who grants the permission the user needs, who reads the audit log the user generates). The story map is the delivery-side counterpart of Chapter 01's journey map: it turns a journey into release slices.

### Definition of Ready and Definition of Done

The Scrum Guide defines the **Definition of Done** as a formal description of the state of the Increment when it meets the quality measures required for the product. Work that doesn't meet it can't be released or shown at the Sprint Review; it goes back to the Product Backlog. The Definition of Done protects quality, and in 2026 it's also where you require human review of code that agents wrote.

The **Definition of Ready** isn't in the Scrum Guide, which says only that items the team can finish within one Sprint are ready for selection. The Agile Alliance describes it as explicit, visible criteria, usually based on INVEST, that a story must meet before it enters an iteration, and traces it to the Scrum community in 2008. A short one helps the team push back on vague work; a long one becomes a stage gate that blocks collaboration. Keep it to a handful of lines.

| | Definition of Ready (before work starts) | Definition of Done (before work counts) |
|---|---|---|
| Purpose | Stop vague work entering a sprint | Stop unfinished work reaching customers |
| Owner | PM and team together | Team, with the PM agreeing the product items |
| B2B items | Problem and evidence linked; acceptance criteria written; permission and tenancy cases listed; dependencies named with owners; telemetry defined; security or privacy review flagged | Code reviewed (including all agent-written code); acceptance scenarios pass; behind a flag if not for everyone; docs and release notes drafted; telemetry live; security checks pass; deployed to production |
| Failure mode | Becomes a gate that blocks discovery | Quietly skipped near a deadline |

### Issue and bug management

The PM's job in bug management is to get the right defects fixed in the right order, with as little arguing as possible. One distinction resolves most triage arguments. **Severity** is the technical impact of a defect on the system: does it crash, lose data, block a function or just look wrong? **Priority** is the business importance and urgency of fixing it. Severity is usually set by engineering or QA; priority is set by the PM. They often diverge. A crash in a rarely used admin export is high severity and may be low priority. A misspelled customer name on the login page of your largest account is low severity and high priority.

A common priority scale runs from P0 to P4. Google's Issue Tracker documentation, for example, defines P0 as needing immediate attention (a full outage or a critical function unavailable with no workaround), P1 as significant impact on many users with a painful workaround, P2 as the default to be fixed in a reasonable timescale, P3 as when able, and P4 as polish to be fixed eventually.

Two older ideas make triage faster.

- The **bug bar**, a Microsoft practice that Ben Armstrong described in 2004, is a list of conditions a bug must meet to be fixed in a given milestone or release: customer reported, application crash or data loss, for example. In triage, "Does it meet the bar?" ends the debate. The bar starts low early in a release cycle and rises as ship approaches, so late fixes are reserved for the defects that matter.
- The **error budget policy**, from the Google SRE Workbook (in an example policy by Steven Thurgood), turns reliability into a release rule. If a service has used up its error budget over the preceding four weeks, all changes and releases stop except P0 fixes and security fixes until it's back within its service level objective. The policy states that the freeze isn't a punishment. If a code bug or procedural error caused the overage, reliability work becomes mandatory.

In B2B, keep two kinds of service level agreement separate. Customer-facing support SLAs (response and resolution time by severity) are contractual and owned jointly with support. Internal fix SLAs ("P1 bugs fixed within N days") are a team agreement. Make sure the internal SLA is always shorter than the contractual one it supports, or the contract will be broken by arithmetic.

:::leader For product leaders
Set the severity definitions and the bug bar once for the portfolio and let teams add product-specific examples. When two teams define "P1" differently, escalations from shared customers turn into arguments about labels instead of fixes.
:::

### Technical debt as a product decision

Ward Cunningham introduced the debt metaphor in a 1992 experience report at the OOPSLA conference: "Shipping first time code is like going into debt." A little debt speeds development as long as it's paid back promptly with a rewrite. Every minute spent on not-quite-right code is interest. The danger comes when the debt isn't repaid.

Martin Fowler sharpened the economics. The cruft in a system is the debt; the extra effort it causes on every change is the interest. In his example, a feature that takes four days in clean code takes six in crufty code, so two days are interest. Paying down the principal is worth it only if more work will touch that area. Fowler's practical rule follows: pay down debt gradually, starting where the code changes most often, and leave alone stable code that rarely gets touched.

Fowler's 2009 **Technical Debt Quadrant** classifies debt on two axes: deliberate or inadvertent, and prudent or reckless.

| | Reckless | Prudent |
|---|---|---|
| **Deliberate** | The team takes shortcuts because it believes it can't afford clean code | The team knowingly takes on debt to make a release, with a plan to repay it |
| **Inadvertent** | The team doesn't know good design and makes a mess without realizing | After a year of work the team learns what the design should have been |

Prudent, deliberate debt is a legitimate trade, like cutting scope to hit a date, so the PM should help take it on and schedule its repayment. Reckless debt is a quality problem to stop at the source. Prudent, inadvertent debt is inevitable, because teams learn as they build.

To make debt visible to the business, name the interest in terms executives already track: slower lead time on a roadmap item, incidents traced to a fragile component, slower onboarding, a feature you can't ship until the debt is paid. A **tech debt register** records each item with its quadrant, the interest it costs, how often the area changes and a decision (pay now, schedule, accept or retire). Then rank with Fowler's rule: interest paid times change frequency.

### Release planning, feature flags and progressive delivery

Modern release planning treats **deploying** and **releasing** as different events. Deploying is an engineering event: code reaches production. Releasing is a product and customer event: someone can use it. Feature flags separate the two, and that separation gives the PM control over who sees what, and when.

Pete Hodgson's 2017 article on feature toggles, published on Martin Fowler's site, sorts them into four categories with very different lifespans:

| Toggle type | Purpose | Lifespan | PM's interest |
|---|---|---|---|
| **Release** | Hide unfinished work so the main branch can deploy any time | Short; remove after launch | Launch timing; removal tasks |
| **Experiment** | Show variants to different users | Long enough for a statistically valid result | Experiment design (Chapter 05) |
| **Ops** | Change system behavior quickly during an incident | Usually short; some kill switches stay | Who owns the kill switch |
| **Permissioning** | Give some customers features others don't get | Can last years | Packaging and entitlements (Chapter 15) |

Hodgson also warns about **toggle debt**, flags that outlive their purpose. His controls: add a removal task when you create a release toggle, give each toggle an expiry date, consider a test that fails after expiry, and cap the number of active toggles.

**Progressive delivery** builds on flags. The 2025 book *Progressive Delivery*, by James Governor, Kimberly Harrison, Heidi Waterhouse and Adam Zimman, frames the goal as delivering what users need, when they need it, at the least cost and risk to everyone. In practice that means rolling out in stages (internal users, design partners, an opt-in beta, customer cohorts, everyone), each with exit criteria that stop the rollout when they fail.

An enterprise **release plan** therefore names the flags, the stages and exit criteria, the kill-switch owner, customer communications, enablement, compliance artifacts, the rollback plan and a date range with a confidence level. Chapter 25 covers the go-to-market side of the same event.

### DORA metrics as context

The DORA research program publishes the most widely used measures of software delivery performance. Its current guidance lists five metrics. Three measure throughput: **change lead time** (from commit to production), **deployment frequency** and **failed deployment recovery time**. Two measure instability: **change fail rate** (deployments that need immediate intervention) and **deployment rework rate** (unplanned deployments caused by a production incident). DORA recommends applying them per application or service, not across a whole organization.

A PM reads these as context, not targets. Lead time tells you how fast a validated idea can reach customers. Change fail rate tells you how risky each release is, which matters when you're planning a customer-facing launch. If lead time is long, your learning loop is slow however good your discovery is. Never use DORA metrics to compare teams: they describe a system, and different systems aren't comparable.

## How to apply it

Here's a method for setting up, or resetting, the execution working agreements for a product area. Most of it happens in the first two sprints; after that it runs as habit.

1. **Agree the ownership split.** In one session with the engineering lead and designer, write down who owns the problem, the solution, the estimate, the quality bar and the scope trade-off. Start from the table in this chapter.
2. **Map before you backlog.** For the next significant outcome, build a story map with the trio and at least one engineer, across every persona involved, including approvers and administrators. Cut the walking skeleton first, then two more release slices.
3. **Write stories as the three Cs.** For each story in the first slice, write the card, hold the conversation in refinement and record the confirmation as Given-When-Then scenarios, including permission, error and tenancy cases. Split any story that fails INVEST's "Small" or "Testable."
4. **Publish a short Definition of Ready and Definition of Done.** Draft both with the team and add the B2B items (permissions, audit, telemetry, security review). If the team uses coding agents, the Definition of Done requires human review of their code.
5. **Plan against real capacity.** Before Sprint Planning, work out net capacity after leave, on-call and support duty, and set an explicit reserve for unplanned work from recent history. Bring a Sprint Goal that names an outcome, and let the engineers decide how much fits.
6. **Forecast with ranges.** When someone asks for a date, ask your harness for a throughput-based range from recent sprints. Answer with the range, the confidence level and the scope lever.
7. **Write the triage policy before you need it.** Define severity with examples from your product, a priority rule, the triage cadence, internal fix SLAs tighter than the contractual ones and a bug bar that rises toward each release.
8. **Open a tech debt register.** Ask engineering for the ten items that cost the most interest. Classify each by quadrant, record the evidence and the change frequency, decide what to pay now, and reserve capacity for it every sprint.
9. **Write the release plan alongside the first story.** Name the flags, stages, exit criteria and kill-switch owner before anyone writes code, so the flags are built in from the start.
10. **Read the delivery metrics monthly.** Review lead time and change fail rate with the engineering lead, to explain release risk and dates, never to grade the team.

Revisit the Definition of Done after any escaped defect, the bug bar at each release phase and the debt register every quarter.

## The AI lens

### Building AI-powered products

When the product itself is AI-powered, several execution practices change. Chapter 31 covers evals and AI specification in depth; these are the execution-level consequences.

- **Acceptance criteria become thresholds plus cases.** One Given-When-Then scenario can't confirm a probabilistic behavior. Pair deterministic scenarios (permissions, audit entries, refusal when evidence is missing) with an eval criterion: the share of a named eval set that must pass. "Then the proposed root cause is correct" isn't testable; "the diagnosis eval set passes at or above the agreed threshold" is.
- **Ready and done grow.** An AI story isn't ready until its risk class is assigned and its eval cases exist. It isn't done until the evals pass, cost per task is within budget and compliance documentation is updated.
- **Some bugs are distributions.** One hallucination is an anecdote; a cluster of the same failure in one segment is a defect with a severity. Add each confirmed failure to the eval set so the fix stays fixed.
- **Model changes are releases.** A new model version, prompt or retrieval index can change behavior as much as code. Put it behind a flag and roll it out in stages with exit criteria.
- **Kill switches move into the first slice.** For an agent that takes actions, a global ops toggle that disables actions is part of the minimum viable product.

### Doing the work with AI: coding agents and the PM

Most engineering teams in 2026 work alongside AI coding agents. The evidence on what that does to throughput is mixed in an instructive way.

- **Adoption is near universal; trust isn't.** The 2025 DORA report, announced by Nathen Harvey and Derek DeBellis, surveyed nearly 5,000 respondents: 90% used AI at work and more than 80% believed it had raised their productivity, while 30% had little or no trust in AI-generated code. In the Stack Overflow 2025 Developer Survey, more developers distrusted AI accuracy (46%) than trusted it (33%), and two-thirds cited solutions that were almost right but not quite.
- **Throughput rises; stability doesn't follow.** DORA found AI adoption now has a positive relationship with throughput and product performance but still a negative one with delivery stability. Its framing is that AI amplifies a team's existing strengths and dysfunctions.
- **Felt speed and measured speed differ.** In METR's early-2025 randomized trial, 16 experienced open-source developers working on 246 real issues took 19% longer with AI allowed, though they had expected a 24% speedup and afterwards believed they'd gained about 20%. METR's February 2026 update pointed toward speedups with newer tools but called its own estimates unreliable and very weak evidence of size. Don't quote a single productivity number from this work.
- **Review becomes the constraint.** Faros AI, a vendor analyzing telemetry from more than 10,000 developers, reported in 2025 that high-adoption teams merged 98% more pull requests, while review time rose 91%, pull request size 154% and bugs per developer 9%. The data is correlational and from one vendor's customers, but it matches the DORA picture.
- **Delegation is still partial.** Anthropic's December 2025 study of its own engineers (self-reported, and from the company that makes Claude) found that more than half could fully delegate no more than a fifth of their work, and that they handed off tasks that were easy to verify or low in stakes.

Read together: code generation got cheaper, while review, verification and stability didn't keep pace. That moves the constraint to two places a PM controls.

**Upstream, spec quality is now a throughput lever.** Ambiguity a human engineer would resolve in a quick conversation becomes a wrong implementation at agent speed. **Spec-driven development** emerged as a named practice in 2025 in response. GitHub's Spec Kit, introduced by Den Delimarsky, splits work into Specify (user journeys and success criteria), Plan (architecture and constraints), Tasks (small, independently testable items) and Implement (the agent works the tasks while people review focused changes). Birgitta Böckeler, writing on Martin Fowler's site, found that such tools produced repetitive documents tedious to review and were overkill for small changes (one turned a small bug into four stories with sixteen acceptance criteria), and that agents still ignored instructions. Thoughtworks's Technology Radar placed the practice in its "Assess" ring in November 2025.

The workable position sits between the two. Stories, acceptance criteria and the Definition of Ready are now agent inputs as well as human ones, so write them to be unambiguous, and keep them proportionate. The three Cs still apply; the conversation now includes reviewing the agent's plan with the engineer before code is written.

**Downstream, review capacity is a planning input.** Slice smaller, because every slice becomes a change someone must read. Write acceptance scenarios before implementation, so reviewers check behavior against an agreed confirmation. Reserve review capacity in Sprint Planning, require human review in the Definition of Done, and lean on progressive delivery and kill switches so a defect that slips through stays small. Watch change fail rate and deployment rework rate as the stability signals.

:::ai The PM's leverage with coding agents
When code is cheap, pushing for more output is the wrong instinct. Your leverage is clarity of intent, slice size and the quality gates around release. A sharp acceptance scenario is worth more than it used to be, because an agent won't ask the clarifying question a person would.
:::

Your harness helps with the PM side of execution too. With connectors to the tracker, CI system, support desk and CRM, ask for a draft triage agenda ("new bugs this week, grouped by suspected root cause, with linked customer tickets and ARR at risk"), a throughput forecast with its assumptions, or the merged changes that lacked acceptance tests. The harness prepares evidence. You decide priority, scope and what ships.

## The Beacon case: shipping supervised remediation

:::example Where Beacon starts
Beacon Agents, supervised remediation, is due to launch at Northlight Live. Chapter 01's discovery split the bet: diagnosis ships first, and supervised action follows only with audit logs, scoped credentials and a kill switch. You're the newly arrived Principal PM, with 3 PMs, 1 designer, about 35 engineers across 5 teams and 2 applied AI engineers. Then a customer rolls back the wrong service after Beacon proposes a hallucinated root cause.
:::

**The story map.** The trio maps supervised remediation across three personas on one backbone. Dana (on-call engineer) gets paged, reads the diagnosis, reviews the proposed step, approves it, watches the outcome and closes the incident. Priya (SRE lead) configures the allowlist, sets the approval policy and reviews the audit trail. Sam (security reviewer) grants least-privilege connector scopes and exports the audit log. Putting Sam on the same map exposes a gap the flat backlog hid: Sam couldn't revoke a connector scope without opening a support ticket. The walking skeleton for Northlight Live is thin on purpose: one action (roll back the last deploy), a human approval gate, an audit entry and a kill switch. Restart, scale, autonomous allowlisted actions and multi-tenant approvals for Leo's MSP customers move to later slices.

**The story.** The first story reads:

> As an on-call engineer, I want to approve or reject Beacon's proposed rollback in one step from the incident view, so that I can restore service without leaving the page.

Its scenarios cover the happy path (Dana holds the responder role and approves; the rollback runs; the timeline records who approved and on what evidence), the permission boundary (without approval rights for that service, Approve is disabled and eligible approvers are shown) and, after the incident, an evidence rule the engineers write in EARS for the agent spec: *If the diagnosis cites no change event, then Beacon shall not propose a rollback.*

**Ready and done.** The Definition of Ready gains two lines (action risk class assigned; eval cases added for this action). The Definition of Done gains four (audit log entry verified; kill switch tested; AI Act documentation field updated; human review of agent-written code).

**The incident and the bug bar.** The hallucinated root cause is classified severity 1, because it touched the safety of a production action, and P0 for affected tenants. It also changes the bug bar: any defect that can cause an unapproved or wrongly targeted action now meets the bar at every phase, including launch week. The severity and priority distinction works the other way too: a cosmetic error in the diagnosis summary for a top-ten account is low severity but gets high priority.

**The date conversation.** Marcus, a VP of IT Operations at a customer waiting for Beacon Agents, wants a firm date. You ask the harness for a throughput forecast from the last eight sprints of the teams building Act. The range straddles the Northlight Live date. Instead of promising the date, you name the lever: the rollback-only slice lands with a buffer if "scale" stays out of the launch. Northlight Live announces an opt-in beta, with general availability given as a range.

**The release plan.** Beacon Agents ships behind a release toggle and a permissioning toggle. Stages run from dogfooding on Northlight Observe's own on-call rotation, to five design partners, to the opt-in beta, to general availability by region, with the EU last because AI Act documentation must be complete first. Every stage shares the exit criteria: diagnosis acceptance rate at or above target, zero wrong-target actions, approval-to-action latency within target and no rise in support tickets. A global ops toggle is the kill switch, owned by the on-call engineering lead.

**The debt register.** Three items lead it. The Beacon Classic correlation engine is prudent, deliberate debt from the 2024 spin-out, paid down through the sunset. Connector authentication code duplicated across all five teams is reckless, inadvertent debt in frequently changed code, so Fowler's rule puts it first. Gaps in the eval harness are debt whose interest the team already paid, in the hallucination incident.

**The coding agents.** Beacon's engineers use coding agents, and pull request volume and review time both climbed. With the engineering leads you change four practices: smaller stories, Given-When-Then scenarios written before any agent starts, review capacity reserved in Sprint Planning, and change fail rate read monthly as the stability signal. Your first question to the harness, through the tracker and CI connectors: "Which changes merged last month lacked acceptance tests, and which incidents followed them?" The answer goes into the next retrospective, not into anyone's performance review.

## Product 360 artifacts

```template id="06-user-story" title="User story with acceptance criteria"
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
```

```template id="06-story-map" title="User story map"
# Story map · [Outcome or capability] · [Date]

**Outcome:** [What changes for the customer when this is done]   **Personas on this map:** [User, approver, admin, buyer]

## Backbone (activities, left to right in narrative order; not ranked)
| [Activity 1] | [Activity 2] | [Activity 3] | [Activity 4] | [Activity 5] |
|---|---|---|---|---|

## User tasks (under each activity)
| [Task] | [Task] | [Task] | [Task] | [Task] |
|---|---|---|---|---|
| [Persona] | [Persona] | [Persona] | [Persona] | [Persona] |

## Release 1: walking skeleton (thinnest end-to-end slice)
| [Story] | [Story] | [Story] | [Story] | [Story] |
|---|---|---|---|---|

Release goal: [ ]   Target window: [range]   Exit criteria: [ ]

## Release 2
| [Story] | [Story] | [Story] | [Story] | [Story] |
|---|---|---|---|---|

Release goal: [ ]

## Later
| [Story] | [Story] | [Story] | [Story] | [Story] |
|---|---|---|---|---|

## Hand-offs between personas (where enterprise gaps hide)
| From | To | What passes between them | Covered by story |
|---|---|---|---|
| | | | |

## Gaps found while mapping
- [ ]
```

```template id="06-definition-of-ready-done" title="Definition of Ready and Definition of Done"
# Definition of Ready and Done · [Team] · v[n] · [Date]

**Agreed by:** [PM, engineering lead, designer, QA]   **Review after:** any escaped defect, or quarterly

## Definition of Ready (keep it short; drop any line that never catches anything)
- [ ] Problem and customer evidence linked
- [ ] Acceptance criteria written as Given-When-Then, including error cases
- [ ] Permission, role and tenancy cases listed
- [ ] Dependencies named, each with an owner
- [ ] Design attached, or marked "no UI"
- [ ] Telemetry events defined
- [ ] Fits in one sprint (passes INVEST "Small")
- [ ] Security, privacy or compliance review need flagged
- [ ] AI features: risk class assigned and eval cases added

## Definition of Done
- [ ] Code reviewed by a person, including every agent-written change
- [ ] Automated tests pass, including the acceptance scenarios
- [ ] Behind a flag if not released to all customers; flag has a removal task and expiry date
- [ ] Docs and release notes drafted
- [ ] Telemetry live and checked in production
- [ ] Security checks pass
- [ ] Deployed to production (dark if needed)
- [ ] No new P0 or P1 bugs open against it
- [ ] AI features: evals pass at threshold; cost per task within budget; compliance documentation updated
- [ ] Actions that change customer systems: audit entry verified; kill switch tested
```

```template id="06-bug-triage-policy" title="Bug triage policy"
# Bug triage policy · [Product] · v[n] · [Date]

**Owner:** [PM]   **Engineering owner:** [Lead]   **Applies to:** [Products, services]

## Severity (technical impact; set by engineering or QA)
| Level | Definition | Example from this product |
|---|---|---|
| S1 | Outage, data loss, security exposure or unsafe action; no workaround | |
| S2 | Major function broken; painful workaround | |
| S3 | Minor function broken; reasonable workaround | |
| S4 | Cosmetic or polish | |

## Priority (business urgency; set by the PM)
Priority = severity, adjusted for customers affected, contractual exposure, workaround and strategic accounts.
| Priority | Meaning | Internal fix SLA | Contractual SLA it protects |
|---|---|---|---|
| P0 | Drop everything | [hours] | [ ] |
| P1 | Next in line, this sprint | [days] | [ ] |
| P2 | Default; planned | [weeks] | |
| P3 | When able | None | |
| P4 | Polish; eventually | None | |

Rule: every internal SLA is shorter than the contractual SLA it supports.

## Triage cadence
When: [day, time, frequency]   Attendees: PM, engineering lead, QA, support lead   Prep: harness drafts agenda from tracker and support connectors

## Bug bar by release phase
| Phase | Meets the bar |
|---|---|
| Early build | All S1 to S3; S4 if cheap |
| Stabilization | S1, S2; any customer-reported bug |
| Release candidate | S1; data loss; security; [product-specific always-fix conditions] |

Always meets the bar: [for example, any defect that can cause an unapproved or wrongly targeted action]

## Escalations from named accounts
Path: [support → account team → PM → engineering lead]   Who can override priority: [role]

## Regressions
Definition: [a defect in behavior that previously passed]   Treatment: [one priority level higher by default]

## Reporting (monthly)
Open P0 and P1 count and age; escaped defects; reopen rate; SLA misses; top root-cause clusters
```

```template id="06-release-plan" title="Release plan"
# Release plan · [Release name] · [Date]

**Outcome:** [What changes for customers]   **PM:** [ ]   **Engineering lead:** [ ]   **Date range:** [earliest to latest] at [confidence]

## Scope
In: [ ]   Out: [ ]   Scope lever if the date is at risk: [ ]

## Flags
| Flag | Type (release / experiment / ops / permissioning) | Owner | Removal task | Expiry |
|---|---|---|---|---|
| | | | | |

## Rollout stages
| Stage | Who sees it | Entry criteria | Exit criteria | Earliest date |
|---|---|---|---|---|
| Internal | [ ] | | | |
| Design partners | [ ] | | | |
| Opt-in beta | [ ] | | | |
| Cohort or percentage | [ ] | | | |
| General availability | [ ] | | | |
| Regions held back | [ ] and why | | | |

## Exit criteria metrics
Error rate: [ ]   Latency: [ ]   Acceptance or adoption metric: [ ]   Support tickets: [ ]   Change fail rate: [ ]

## Kill switch and rollback
Kill-switch owner: [name, role]   Rollback plan: [ ]   Rehearsed on: [date]

## Customer communications
Release notes: [ ]   Admin notices: [ ]   Deprecation notices: [ ]   Status page: [ ]

## Enablement
Support: [ ]   Sales: [ ]   Partners: [ ]   Customer success: [ ]

## Compliance artifacts
[Security documentation, AI documentation, data processing terms, as applicable]

## Decision log
| Date | Decision | Made by | Reason |
|---|---|---|---|
| | | | |

```

```template id="06-tech-debt-register" title="Technical debt register"
# Technical debt register · [Product] · [Date]

**Owner:** [PM and engineering lead]   **Review:** quarterly, and before each roadmap cycle

| ID | Area or service | Description | Quadrant (deliberate or inadvertent; prudent or reckless) | Interest being paid (evidence) | Change frequency of the area | Principal (effort range) | Risk if left (security, compliance, scale) | Proposed fix and first slice | Owner | Decision (pay now / schedule / accept / retire) | Review date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TD-1 | | | | | | | | | | | |

## Ranking rule
Rank by interest paid times change frequency. Pay down where the code changes most. Leave stable, rarely touched code alone.

## Evidence of interest (use the business's terms)
- Slower lead time on roadmap items: [ ]
- Incidents traced to this area: [ ]
- Escalations or SLA misses: [ ]
- Roadmap items blocked: [ ]
- Onboarding drag for new engineers: [ ]

## Capacity reserved for debt this quarter
[Share or person-days, set from history], agreed by [ ]
```

```template id="06-sprint-plan" title="Sprint plan and capacity"
# Sprint plan · [Team] · Sprint [n] · [Dates]

## Sprint Goal (an outcome, not a ticket list)
[One sentence]   Links to quarterly outcome: [ ]   Product Goal: [ ]

## Capacity
| Person | Days available | Less leave | Less on-call or support duty | Net days |
|---|---|---|---|---|
| | | | | |

Total net capacity: [ ]
Reserve for unplanned work (bugs, escalations): [set from the last few sprints]
Reserve for debt: [from the register]
Reserve for review of agent-written changes: [ ]
Capacity for planned stories: [ ]

## Selected items
| Item | Persona | Ready? | Size or count | Notes |
|---|---|---|---|---|
| | | | | |

## Forecast (if asked for dates)
Throughput over recent sprints: [ ]   Date range: [ ] at [confidence]   Scope lever: [ ]

## Risks and dependencies
| Risk or dependency | Owner | Mitigation |
|---|---|---|
| | | |

```

## Prompts

```prompt title="Turn a feature request into INVEST stories with Gherkin criteria"
Goal: Get a first draft of build-ready stories that engineers and coding agents can work from.
Paste in: the feature request or epic, the persona, the customer evidence behind it and any known constraints (permissions, tenancy, audit, compliance). Use an approved tool if the evidence includes customer data.

Act as a senior PM writing stories for an enterprise B2B product.

1. Split this epic into the smallest vertical slices that each deliver customer value through every layer. Explain each split in one line.
2. For each slice, write a story: "As a [role in context], I want [capability], so that [outcome]."
3. Write acceptance criteria as Gherkin scenarios of three to five steps: a happy path, each permission boundary, each error case and any tenancy case. "Given" sets a known state, not a user action; "Then" asserts only observable outcomes.
4. Add non-functional criteria (latency, audit entry, data residency, accessibility) where relevant, and an explicit out-of-scope list.
5. Check each story against INVEST and flag any that fail, with the reason.
6. List the open questions I need to answer before the stories are ready.

Don't invent customer evidence or constraints I haven't given you. Mark assumptions as assumptions.

[epic, persona, evidence, constraints]

Check the output: read every "Then" line and confirm someone could observe it in the product. Make sure every role in the permission model has a scenario. Delete any story that's a technical layer rather than a customer slice.
```

```prompt title="Draft a story map from a journey"
Goal: Lay out the backbone and a walking skeleton before the backlog fills up.
Paste in: the journey map or workflow description, the personas involved (including approvers and administrators) and the outcome the release must deliver.

Build a user story map for [outcome] in [product].

1. Write the backbone: the activities users perform, left to right in narrative order. Don't rank them.
2. Under each activity, list the user tasks, labeled with the persona who performs them.
3. Propose a walking skeleton: the thinnest set of stories that delivers the outcome end to end. Then propose Release 2 and Later slices.
4. List every hand-off between personas (permission grants, approvals, audit reviews) and whether a story covers it.
5. List gaps: tasks with no stories, and personas whose tasks are missing.

Present the map as a table with activities as columns.

[journey, personas, outcome]

Check the output: walk the walking skeleton as each persona. If any persona can't complete their part, the skeleton isn't complete. Confirm the hand-off list includes administrators and security reviewers.
```

```prompt title="Forecast a date range from throughput"
Goal: Answer "when will it be done?" with a range and a scope lever instead of a guess.
Paste in (or connect the harness to): the tracker data for completed items over recent sprints, the remaining items in scope and the target date.

Using the completed items for [team] over the last [N] sprints, and the remaining scope for [release]:

1. Report throughput per sprint (count of finished items) and how much it varied.
2. Flag items that are much larger than typical, which make a count-based forecast unreliable.
3. Forecast a date range for the remaining scope at two confidence levels, and state every assumption (team size, unplanned work, holidays).
4. Say how likely the target date [date] is under these assumptions.
5. Identify the scope cuts that would bring the likely date before the target, smallest cut first.

Show the method in plain language. Don't present a single date.

Check the output: compare the throughput figures with what the team remembers. If a big item or a holiday sprint is distorting the count, rerun without it. Share the range and the lever, not the arithmetic.
```

```prompt title="Prepare a bug triage agenda"
Goal: Walk into triage with the evidence assembled, so the meeting is spent on decisions.
Paste in (or connect the harness to): new and reopened bugs since the last triage, linked support tickets, account data (ARR, contract tier, contractual SLAs) and your triage policy. Use an approved tool for customer data.

Using our triage policy, prepare a triage agenda for [product]:

1. Group new bugs by suspected root cause or component. Flag duplicates.
2. For each group, propose a severity using our definitions, with one line of evidence.
3. Show customer impact: number of accounts, linked tickets, ARR at risk and any contractual SLA clock running.
4. Propose a priority, and flag every case where priority and severity diverge, with the reason.
5. Flag any bug that meets our "always meets the bar" conditions, and any internal fix SLA about to be missed.
6. List the decisions needed from the meeting.

Don't set final priorities. Recommend, and show the evidence.

Check the output: open three bugs and confirm the grouping and severity are right. Verify ARR figures against the source system before quoting them to anyone.
```

```prompt title="Build a tech debt register from engineering evidence"
Goal: Turn a list of complaints about the code into ranked product decisions.
Paste in (or connect the harness to): the engineering team's list of debt items, incident reviews from the last two quarters, change history by service and any roadmap items engineering says are blocked.

For [product], build a technical debt register:

1. For each item, record the area, a one-line description and its quadrant (deliberate or inadvertent; prudent or reckless), with a reason.
2. Record the interest being paid, with evidence: incidents traced to the area, slower lead time, escalations, blocked roadmap items.
3. Record how often the area changes, from the change history.
4. Rank by interest paid times change frequency. Flag stable, rarely changed areas as candidates to accept.
5. For the top five, propose the smallest first slice of repayment and the roadmap item it would unblock.

Cite the incident or change record for every claim. Write "no evidence yet" where the material doesn't support a field.

Check the output: review the top five with the engineering lead. If an item ranks high only because it's annoying rather than costly, move it down.
```

```prompt title="Review a story for agent readiness"
Goal: Catch ambiguity before a coding agent turns it into the wrong implementation.
Paste in: the story, its acceptance criteria, the Definition of Ready and any relevant system context the team has approved for sharing.

Act as a skeptical senior engineer about to hand this story to a coding agent.

1. List every ambiguity an agent would have to guess about: undefined terms, missing states, unstated permissions, unspecified errors.
2. Rewrite the acceptance criteria so each one has a single interpretation. Where a rule is better expressed in EARS ("When...", "If..., then...", "While..."), add it.
3. Check the story against INVEST and our Definition of Ready, and list failures.
4. Say whether the story is small enough that a person can review the resulting change in one sitting. If not, propose a split.
5. List the questions I must answer before this is ready.

Don't add requirements I haven't stated. Mark anything you inferred.

Check the output: read the rewritten criteria with the engineer who'll review the agent's work. If the rewrite needs more than a page for a small change, the spec has grown out of proportion; cut it back.
```

```prompt title="Draft a progressive release plan"
Goal: Plan who sees a release, when, and what stops it, before code is written.
Paste in: the outcome, the scope, the customer segments and regions involved, compliance constraints and the metrics the team trusts.

Draft a release plan for [release] in [product]:

1. Propose the feature flags needed and the type of each (release, experiment, ops, permissioning), with an owner, removal task and expiry date.
2. Propose rollout stages from internal users to general availability, including any regions held back and why.
3. For each stage, give entry and exit criteria using these metrics: [metrics].
4. Name the kill switch, its owner and the rollback plan.
5. List customer communications, enablement and compliance artifacts needed at each stage.
6. Give a date range with a confidence level, and the scope lever if it slips.

Check the output: confirm every stage has an exit criterion someone can measure today. Confirm the kill-switch owner is on call during the rollout. Make sure no release toggle lacks a removal date.
```

## Anti-patterns

:::warn Tickets over the wall
The PM writes detailed tickets and skips refinement. Engineers build exactly what the tickets say, which isn't what the customer needed. Join refinement and agree the acceptance tests together.
:::

:::warn Velocity as a target
Story points become a performance measure, or teams get compared by velocity. Points inflate, forecasts get worse and trust erodes. Use points or throughput only to plan and forecast within one team, and talk about outcomes with everyone else.
:::

:::warn The date without a range
A single date goes to sales or an executive with no confidence level and no scope lever. When it slips, the PM loses credibility and the team loses the weekend. Give a range, the confidence and the scope that moves it.
:::

:::warn Debt as a separate backlog nobody owns
Technical debt lives in an engineering-only list, negotiated sprint by sprint, while the roadmap fills with features. The interest keeps compounding until a roadmap item becomes impossible. Put debt on the same roadmap, show the interest in business terms and reserve capacity for it.
:::

:::warn More code, same review
Coding agents multiply the number of changes, and nobody adjusts review capacity, slice size or the Definition of Done. Defects escape, change fail rate rises and the team concludes the agents don't work. Plan review capacity, slice smaller and require human review of agent-written code.
:::

:::warn The spec as a novel
In response to coding agents, the team writes long specifications for every small change. Reviewing the specs becomes the new bottleneck, and the agents still ignore parts of them. Keep specs proportionate: a crisp story, a few unambiguous scenarios and the rules that matter.
:::

## Checklist

- [ ] The ownership split between product and engineering is written down and agreed.
- [ ] The current outcome has a story map that includes every persona, with a walking skeleton and release slices.
- [ ] Every story in the next sprint passes INVEST and has Given-When-Then criteria covering permissions, errors and tenancy.
- [ ] A short Definition of Ready and Definition of Done are published, with B2B and AI items, and the Definition of Done requires human review of agent-written code.
- [ ] Sprint Planning uses net capacity after leave and on-call, with explicit reserves for unplanned work, debt and review.
- [ ] Every Sprint Goal names an outcome tied to the quarterly plan.
- [ ] External dates are given as ranges with a confidence level and a named scope lever.
- [ ] A bug triage policy defines severity and priority separately, with internal fix SLAs shorter than contractual ones and a bug bar by release phase.
- [ ] A tech debt register exists, classified by quadrant and ranked by interest times change frequency, with capacity reserved for repayment.
- [ ] Every release has a plan with flags, stages, exit criteria, a kill-switch owner and a rollback plan.
- [ ] Every release toggle has a removal task and an expiry date.
- [ ] For AI features, acceptance criteria include eval thresholds and model changes ship behind flags.
- [ ] Lead time and change fail rate are reviewed monthly as context, never to compare teams.

## Key takeaways

- The PM owns the problem, the outcome and the order of work; engineering owns the solution, the estimate and the quality bar; both own the scope trade-off.
- A story is a card, a conversation and a confirmation. Write acceptance criteria as observable Given-When-Then scenarios, with a scenario for every permission boundary in an enterprise product.
- Story maps keep the whole user journey visible and make the walking skeleton obvious, including the hand-offs between personas that flat backlogs hide.
- Forecast from what the team has actually finished, and answer date questions with a range, a confidence level and a scope lever.
- Separate severity from priority, set a bug bar that rises toward release, and treat technical debt as a product decision ranked by the interest it charges where the code changes most.
- Decouple deployment from release with feature flags, and roll out in stages with exit criteria and a kill switch.
- With coding agents, code is cheap and review isn't. Put your effort into clear intent, small slices and the quality gates around release.
