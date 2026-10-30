<p class="lead">Product operations is the function that makes good product decisions cheaper to reach. It owns the trusted numbers, the flow of customer evidence and the operating rhythm, so that product managers spend their time deciding instead of assembling. This chapter covers what the function does, when to create it, how to run the cadence it owns, how to set decision rights, how to shape the 2026 tool stack around an AI harness, and how to tell whether any of it is working.</p>

## Why this matters

Watch a product organization grow from three PMs to fifteen and a familiar set of symptoms tends to appear. The quarterly business review shows three different numbers for the same metric, because each team pulled it from a different system with a different definition. Customer feedback arrives through support, customer success, sales, partners and the community forum, and each PM keeps a private spreadsheet of what they heard. Planning season becomes six weeks of deck building. Nobody is sure who gets the final say on a pricing change. Leaders start asking for "one quick report", and a senior PM loses a Thursday building it.

Each of these looks like an operations problem, and each one degrades strategy. When the numbers disagree, the meeting argues about the data instead of the decision. When evidence is scattered, the loudest customer wins. When the calendar is improvised, decisions slip until the engineering plan has already been set by default. Melissa Perri described product operations in 2019 as removing the obstacles to evidence-based decisions, and that is still the clearest test: does this function make it faster and safer for product people to decide well?

You may never run a product ops team, but as a Senior or Principal PM you will benefit from one, suffer from a bad one or be asked to set one up. You will certainly own an operating cadence (Chapter 00 introduced it), negotiate decision rights, and choose how your team's AI harness reaches the systems where evidence lives. In 2026 that last choice has real consequences: which connectors can write, which skills encode your templates, and who watches the cost and quality of the AI features you ship.

This chapter belongs to the Operate dimension of the Product 360. It covers the machinery: the function, the calendar, the decision rights and the stack. Chapter 29 covers what happens inside the governance forums and business reviews this chapter schedules.

## The product operations model

### Three pillars (Perri and Tilles)

Melissa Perri and Denise Tilles wrote the standard treatment of the function in *Product Operations: How Successful Companies Build Better Products at Scale* (2023). Their argument is that product management stops scaling once a company has many teams, unless something supplies the inputs that strategy, prioritization and execution depend on. They organize those inputs into three pillars:

1. **Data and insights.** One trusted source for business and product metrics, connecting financial outcomes (revenue, retention, cost) to what the teams ship. Chapter 00 of this book calls this pillar *business and data insights*, because in B2B the business numbers are the point: ARR, net revenue retention and gross margin by product are what earn product ops its credibility with Finance.
2. **Customer and market insights.** A standing flow of research, feedback, win-loss notes and market intelligence, routed to the teams that need it instead of hoarded by whoever heard it first.
3. **Process and governance.** The product operating model: the planning calendar, the rituals, the templates, the decision rights and the tools that make them run.

Their book also describes setting up a product management operating model and introducing a product ops team into an existing organization, with examples from companies including Stripe, Uber, athenahealth and Fidelity.

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 330" role="img" aria-label="Product operations: three pillars between product decisions and the operating foundation">
  <rect x="20" y="16" width="680" height="54" rx="12" class="box"/>
  <text x="360" y="40" text-anchor="middle" class="t">Product managers and product leaders decide</text>
  <text x="360" y="58" text-anchor="middle" class="s">Strategy · prioritization · roadmap · launch · pricing · sunset</text>
  <line x1="130" y1="70" x2="130" y2="92" class="ln"/>
  <line x1="360" y1="70" x2="360" y2="92" class="ln"/>
  <line x1="590" y1="70" x2="590" y2="92" class="ln"/>
  <rect x="20" y="92" width="220" height="118" rx="12" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".5"/>
  <text x="36" y="118" class="t">Business and data insights</text>
  <text x="36" y="142" class="s">One metric glossary</text>
  <text x="36" y="160" class="s">Self-serve dashboards</text>
  <text x="36" y="178" class="s">Revenue, margin, retention</text>
  <text x="36" y="196" class="s">AI eval and cost reports</text>
  <rect x="250" y="92" width="220" height="118" rx="12" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)" stroke-opacity=".5"/>
  <text x="266" y="118" class="t">Customer and market insights</text>
  <text x="266" y="142" class="s">One feedback repository</text>
  <text x="266" y="160" class="s">Research panel and ops</text>
  <text x="266" y="178" class="s">Win-loss and field signals</text>
  <text x="266" y="196" class="s">Competitive changes</text>
  <rect x="480" y="92" width="220" height="118" rx="12" fill="var(--a3)" fill-opacity=".12" stroke="var(--a3)" stroke-opacity=".5"/>
  <text x="496" y="118" class="t">Process and governance</text>
  <text x="496" y="142" class="s">Cadence and planning calendar</text>
  <text x="496" y="160" class="s">Decision-rights register</text>
  <text x="496" y="178" class="s">Templates as harness skills</text>
  <text x="496" y="196" class="s">PM onboarding</text>
  <rect x="20" y="226" width="680" height="40" rx="10" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="360" y="251" text-anchor="middle" class="t">Operating cadence: weekly · monthly · quarterly · annual</text>
  <rect x="20" y="276" width="680" height="40" rx="10" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="360" y="301" text-anchor="middle" class="t">Tool stack and AI harness: systems of record, connectors, skills</text>
</svg>
<figcaption>The three pillars of product operations, after Perri and Tilles, sit between the decisions product people make and the foundation that keeps them supplied. Product ops owns the pillars and the foundation. It does not own the top row.</figcaption>
</figure>

### The force multiplier, and its guardrails (Cagan)

Marty Cagan, writing on the SVPG site in December 2021, describes the same shape with different labels: quantitative insights, qualitative insights, and tools and best-practices evangelism. He credits the structure largely to Perri's earlier work, and adds guardrails. He frames product ops as a **force multiplier** that sits beside product management and design and helps PMs, designers and sometimes product marketers do better work. His guardrails mark the line between helping and taking over:

| Product ops should | Product ops should not |
|---|---|
| Provide self-service data tools and one source of truth for KPIs | Do each team's analysis for them |
| Build research infrastructure and coach teams in research | Run the research on the team's behalf |
| Onboard and train new PMs and designers | Take over coaching or strategy from product leaders |
| Share good practices, with judgment about where they fit | Make product decisions |
| Help coordinate quarterly planning | Own planning, or become a command-and-control PMO in disguise |
| Be staffed by senior, credible people | Split the PM job into an "operational" half and a "real" half |

Cagan's warning is that with the wrong people in the role, process keeps growing until, in his words, "process becomes the thing." Keep that phrase near the charter. Every new template, ritual or approval step should be able to answer one question: which decision does this make faster or better?

### What product ops owns

Put the two views together and a product ops function in a B2B company owns six things, each with an artifact later in this chapter:

1. **The operating cadence.** The weekly, monthly, quarterly and annual rituals. Product ops schedules, preps and records them; product leaders run them.
2. **The planning calendar.** The year view that aligns product planning with the fiscal calendar, the board cycle, budget submissions and the annual customer event.
3. **Data and the metric glossary.** One definition per metric, one system of record per data type, self-serve access and, in 2026, the monthly AI quality and cost report.
4. **The feedback system.** One repository for customer signals from every channel, tagged so a PM can ask one question across all of it.
5. **Templates and decision rights.** Standard formats for recurring work (PRD, DACI, launch tier, QBR), increasingly packaged as shared skills in the AI harness, and the register of who decides what.
6. **PM enablement.** Onboarding, training and tool access, so a new PM contributes in weeks rather than a quarter.

Roadmaps, priorities, customer commitments and pricing are missing from the list on purpose. Product ops makes those decisions easier to make well; product managers and leaders still make them.

### When to create the function

There's no verified research threshold for when a company needs product ops. Pendo's guidance, which is a vendor heuristic, suggests somewhere around five to ten PMs or after a Series B, triggered by heavy administrative load on PMs, scattered data and inconsistent process. Perri describes the need as arriving at the growth stage and lists the warning signs: unreliable or siloed data, stale research, undefined cross-functional processes, no structured feedback loop, status meetings that produce no decisions, unclear decision authority, and leaders pulled into ad hoc reporting.

This book's heuristic is to watch for three signals instead of counting PMs:

- **Shared calendar.** Three or more product teams depend on one planning calendar, so a slip in one team's plan becomes everyone's problem.
- **Unstable numbers.** Leaders can't ask for the same metric twice and get the same answer.
- **Deck season.** PMs spend planning season building slides, and decisions wait for the slides.

When two of the three are true, start the function. Start small: one senior person, one pillar, and the pain that is loudest. In most B2B companies that is pillar one, because a single trusted metric glossary unblocks every ritual that follows. A shared product ops lead across a portfolio, as at Northlight, is a reasonable first shape. Hiring a team of junior coordinators is not, for the reason Cagan gives: the function only works if the people in it are credible enough to change how senior PMs behave.

:::leader For product leaders
Write the product ops charter before you hire. The charter decides whether you get a force multiplier or a PMO, and it is far easier to set scope on day one than to remove it later. Name the customers of product ops (PMs, product leaders, the field), the services it offers with response times, and the decisions it explicitly does not make.
:::

## The operating cadence in depth

Chapter 00 introduced the operating cadence as a table of weekly, biweekly, monthly, quarterly and annual rituals, with two rules: every ritual produces a decision or gets cancelled, and every decision gets written down. Product ops is what makes that table survive contact with a real calendar. This section adds three things: who runs each ritual, what product ops prepares before it, and what the AI harness can do as pre-work.

The cadence draws on several established rhythms. Amazon's weekly business review and its annual OP1 and OP2 planning cycle, as Colin Bryar and Bill Carr describe them in *Working Backwards*, are the model for a weekly metric walk and a written annual plan. Google's re:Work guide to OKRs sets annual and quarterly objectives, with mid-quarter check-ins and quarterly grading on a 0.0 to 1.0 scale; it suggests that scores around 0.6 to 0.7 are the sweet spot and that hitting 1.0 every time means the goals were too timid. Ryan Singer's *Shape Up*, from Basecamp, offers an alternative to the quarter: six-week cycles, each followed by a two-week cool-down in which a small betting table of senior people spends an hour or two choosing what the next cycle builds. The resulting plan needs no further approval and isn't interrupted. Product ops can run either rhythm.

### Weekly: the metric walk and the team sync

In the weekly **metrics review**, metric owners walk a fixed set of metrics, explain any variance from the expected trend, and say what they'll do about it. Keep the set fixed: if the dashboard changes every week, nobody learns what normal looks like.

Product ops owns the dashboard and the glossary, and checks before the meeting that every number uses the glossary definition. That check is unglamorous, and in this book's view it's the highest-leverage thing the function does. The **team sync** belongs to the PM; product ops only makes sure the decision log and risk register are where the team expects them.

### Monthly: product review, voice of the customer, and AI quality and cost

The monthly **product review** is where leadership sees roadmap progress, OKR status, competitive changes and a customer insight summary, and makes roadmap changes. Product ops prepares a standard pack so that every team's update has the same shape, which turns a parade of status reports into a comparison leaders can act on.

Two monthly rituals are worth adding in most B2B organizations. A **voice-of-the-customer readout** takes the feedback repository and shows the top themes by segment, with representative quotes and the accounts behind them, so that what sales hears and what support hears land in the same room. For any team shipping AI features, an **AI quality and cost review** looks at eval results, failures added to the suite, cost per successful outcome and gross margin impact. The AI lens section below covers what goes in it.

### Quarterly: business review and planning

The **quarterly business review** (QBR) looks backward: business results, OKR grades, lifecycle changes and what was learned. **Quarterly planning** looks forward: next quarter's bets, staffing and dependencies. Keep them separate. When a single meeting does both, the retrospective gets squeezed into the last ten minutes and the lessons never reach the plan.

Product ops runs the quarterly machinery: it publishes the planning calendar, collects the insight pack, schedules the betting table or portfolio review, chases the capacity check with engineering and publishes the roadmap internally and to the field. Product leaders own the choices.

### Annual: strategy refresh and planning

The annual cycle refreshes the durable artifacts (vision, strategy one-pager, personas, positioning) and produces the plan of record and the budget. In B2B companies it has to line up with things product doesn't control: the fiscal year, the board calendar, Finance's budget deadline and the annual customer event, where the year's biggest launch usually lands. Product ops builds the year view that makes those collisions visible months ahead.

### Calibrating process weight: one-way and two-way doors

A cadence that runs every decision through the same heavy process turns into the process-first organization Cagan warned about. Jeff Bezos, in Amazon's 2015 letter to shareholders, separates **Type 1** decisions (consequential and irreversible or nearly so: one-way doors) from **Type 2** decisions (changeable and reversible: two-way doors). He argues that Type 2 decisions "can and should be made quickly by high judgment individuals or small groups," and that large organizations drift toward using the heavyweight Type 1 process for everything, which brings slowness, risk aversion and too little experimentation.

Product ops should build that distinction into the cadence. Most roadmap sequencing calls are two-way doors and belong to the team, decided in the weekly or monthly ritual. Pricing model changes, deprecations, contractual commitments and new autonomous actions in production are one-way doors, and they get a written decision document, named roles and a slot in the quarterly or monthly leadership forum.

## The planning calendar

The operating cadence is the repeating rhythm. The **planning calendar** is the specific set of dated milestones that turns one quarter into the next, and the year into the next year. Product ops publishes it, and every milestone has an owner and a required input.

The offsets below are this book's synthesis, not a published standard; adjust them to your company's size and fiscal year.

| When | Milestone | Owner | Required input |
|---|---|---|---|
| Week −6 before quarter | Insight pack published | Product ops | Metrics vs. OKRs, customer themes, competitive changes, AI eval and cost trends |
| Week −4 | Draft bets due | Each PM | One-page bet per initiative, linked to OKRs |
| Week −3 | Betting table or portfolio review | Product leader | Ranked bets, capacity estimate |
| Week −2 | Capacity and dependency check | Engineering leads | Staffing plan, cross-team dependencies |
| Week −1 | Roadmap published internally and to the field | Product ops with PMM | Approved bets, field-safe roadmap version |
| Week 1 | Quarter starts; OKRs set | Product leader | Final OKRs |
| Week 6 | Mid-quarter check | Product ops | OKR progress, risks |
| Week 13 | QBR | Product leader | Results, grades, lessons |

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 210" role="img" aria-label="Quarterly planning calendar from six weeks before the quarter to the QBR">
  <line x1="40" y1="100" x2="690" y2="100" class="ln"/>
  <rect x="40" y="40" width="260" height="34" rx="8" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".5"/>
  <text x="170" y="62" text-anchor="middle" class="t">Planning: weeks −6 to −1</text>
  <rect x="320" y="40" width="370" height="34" rx="8" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)" stroke-opacity=".5"/>
  <text x="505" y="62" text-anchor="middle" class="t">Quarter: weeks 1 to 13</text>
  <circle cx="40" cy="100" r="6" fill="var(--a1)"/>
  <circle cx="125" cy="100" r="6" fill="var(--a1)"/>
  <circle cx="170" cy="100" r="6" fill="var(--a1)"/>
  <circle cx="215" cy="100" r="6" fill="var(--a1)"/>
  <circle cx="260" cy="100" r="6" fill="var(--a1)"/>
  <circle cx="320" cy="100" r="6" fill="var(--a2)"/>
  <circle cx="500" cy="100" r="6" fill="var(--a2)"/>
  <circle cx="690" cy="100" r="6" fill="var(--a3)"/>
  <text x="40" y="126" text-anchor="middle" class="s">−6</text>
  <text x="125" y="126" text-anchor="middle" class="s">−4</text>
  <text x="170" y="126" text-anchor="middle" class="s">−3</text>
  <text x="215" y="126" text-anchor="middle" class="s">−2</text>
  <text x="260" y="126" text-anchor="middle" class="s">−1</text>
  <text x="320" y="126" text-anchor="middle" class="s">1</text>
  <text x="500" y="126" text-anchor="middle" class="s">6</text>
  <text x="690" y="126" text-anchor="middle" class="s">13</text>
  <text x="40" y="152" class="s">Insight pack</text>
  <text x="96" y="170" class="s">Draft bets</text>
  <text x="150" y="188" class="s">Betting table</text>
  <text x="215" y="152" text-anchor="middle" class="s">Capacity</text>
  <text x="270" y="170" class="s">Roadmap out</text>
  <text x="320" y="188" class="s">OKRs set</text>
  <text x="500" y="152" text-anchor="middle" class="s">Mid-quarter check</text>
  <text x="690" y="152" text-anchor="end" class="s">QBR</text>
</svg>
<figcaption>A quarterly planning calendar. The decisions happen in weeks −4 to −2; product ops' job is to make sure the evidence arrives at week −6, so those weeks go to choosing.</figcaption>
</figure>

On top of the quarterly rhythm sits an annual overlay: the strategy refresh, the budget submission to Finance, the annual pricing review, and the code freeze and enablement milestones for the annual customer event. Put them all on one page, because collisions that stay hidden across separate team calendars show up at once there.

## Decision rights: DACI, RACI and RAPID

A cadence tells you when decisions happen. Decision rights tell you who makes them. Without them, rituals turn into discussions that end with "let's take this offline", and the decision gets made later by whoever cares most, or by nobody.

### DACI

**DACI**, popularized by Atlassian through its Team Playbook, names four roles for a single decision:

- **Driver**: gathers the stakeholders and information, sets the scope and gets a decision by the agreed date. Usually the PM.
- **Approver**: makes the decision. Atlassian is emphatic that this is one person.
- **Contributors**: have expertise and a voice, but no vote.
- **Informed**: are told the outcome. No voice, no vote.

Atlassian's play turns this into a document whose title is the question being decided, followed by status, impact, people, due date and outcome; a one- or two-sentence background; relevant data; decision factors such as cost, time and scalability; an options table with pros, cons and estimated resources and cost; action items; and the recorded outcome. The play suggests about fifteen minutes of prep and an hour to run, with three to six people. DACI fits most one-off product decisions, which is why this book uses it as the default.

### RACI and RAPID

**RACI** (Responsible, Accountable, Consulted, Informed) assigns roles to tasks and deliverables, where DACI assigns them to a decision. Responsible people do the work; one Accountable person signs off; Consulted people are in two-way conversation; Informed people get one-way updates. It fits recurring operational work such as the release process or launch tiers, where the same roles apply every time.

**RAPID**, from Bain & Company, adds a role that DACI lacks: **Agree**, a sparing veto for people who must sign off on feasibility or mandatory requirements, such as Legal or Security. The other roles are Recommend (leads, gathers input, proposes), Perform (executes), Input (consulted, doesn't decide) and Decide (ideally one person, who commits the organization and resolves any deadlock between Recommend and Agree). Bain suggests applying it first to high-value or high-frequency decisions.

| Situation | Use | Why |
|---|---|---|
| One-off product decision (scope, option choice, launch timing) | DACI | Lightest framework with a single approver |
| A function holds a hard veto (Security on production access, Legal on contract terms, regulatory sign-off) | RAPID | Makes the veto explicit and bounded |
| Recurring operational work (release, launch tier, deprecation notice) | RACI | Same roles every time; assigns the work as well as the sign-off |

### The decision-rights register

The most useful thing product ops can do with these frameworks is pre-assign them. A **decision-rights register** is a standing table of recurring decision types (pricing change, deprecation, new autonomous action in production, roadmap change after commit, AI model swap, launch tier) with the door type, the framework, the roles and the forum already filled in. When one of those decisions comes up, nobody spends the first meeting arguing about who decides. Chapter 29 covers how decisions are logged and reviewed in governance forums. The register is the operating mechanism that feeds those forums.

## The PM tool stack in 2026

Product ops owns stack hygiene: one system of record per data type, no overlapping tools bought by different teams, and clear access rules. Both Cagan and Pendo put tooling inside the function's remit. In 2026 the AI harness is also a layer that reaches into every other tool, which gives stack hygiene a second job: deciding what the harness can touch.

The enabling standard is the **Model Context Protocol** (MCP), which Anthropic introduced in November 2024 as an open way to connect AI assistants to the systems where data lives. In December 2025, Anthropic donated MCP to the Agentic AI Foundation, a directed fund under the Linux Foundation co-founded with Block and OpenAI; at that point Anthropic reported more than 10,000 active public MCP servers. Product tools now ship their own servers. Amplitude's lets an AI assistant run segmentation, funnel and retention analysis and read experiment results from a natural-language request. Linear's lets an assistant find, create and update issues, with a read-only option through a restricted scope. Vendors have also put agents inside their tools: Atlassian's Rovo searches across Atlassian and third-party apps and runs agents inside workflows, and Productboard Spark is an agent that works from product data and customer feedback.

That leaves product ops with a new design question for each category: what is the system of record, and what can the harness and the in-tool agents read or write?

| Category | Examples (2026) | Harness access default | What it feeds |
|---|---|---|---|
| Work tracking and roadmapping | Jira, Linear, Productboard, Aha! | Read; write only for drafts the PM approves | Roadmap, release plan, planning calendar |
| Product analytics and experimentation | Amplitude, Pendo, Mixpanel | Read | Metrics review, experiment readouts |
| Feedback and research repository | Support, CS, call notes, win-loss | Read, with customer-data rules applied | Voice-of-the-customer readout, discovery |
| Docs and knowledge | Confluence, Google Docs, Notion | Read; write in the team's own space | PRDs, decision log, QBR packs |
| AI harness and agents | Claude or similar, with skills and connectors | Not applicable: this is the layer that reaches the others | Every ritual's pre-work |
| AI quality and cost observability | Eval harness, provider usage and cost reports, LLM observability | Read | Monthly AI quality and cost review |

Vendor names are examples and capabilities change quickly; the categories and the access rules are what product ops should standardize. Read-only should be the default for every connector, with write access granted per use case and logged.

The second shift is that templates can now run. Anthropic introduced **Agent Skills** in October 2025 as folders of instructions, scripts and resources that the model loads only when relevant, and added organization-wide skill management in December 2025. For product ops, the template library becomes something the harness applies the same way every time: a PRD skill, a DACI skill, a QBR prep skill. Ask the harness to draft the DACI for a decision and it uses your organization's format.

## Measuring product ops

Measure product ops by what PMs and leaders can do faster or better. A function that publishes forty templates and changes no decision has failed. There's no verified benchmark for any of these measures, so treat them as this book's framework and set your own baselines.

| Measure | What it tells you | Pillar |
|---|---|---|
| Insight latency: time from a question to a trusted answer | Whether self-serve data and the feedback repository work | 1 and 2 |
| Metric disputes per quarter: the same metric, different answers | Whether the glossary holds | 1 |
| Ritual decision yield: share of rituals that log at least one decision | Whether the cadence produces decisions or theater | 3 |
| On-time planning decisions: share made on the calendar date | Whether the planning calendar holds | 3 |
| New PM time to first logged decision | Whether onboarding works | 3 |
| PM time on discovery and customers versus reporting (quarterly self-report) | Whether the function frees PM time | All |
| Tool cost per PM and number of overlapping tools | Whether the stack is under control | 3 |
| AI eval coverage: share of agent capabilities with a regression suite | Whether AI quality is governed | 1 |
| Internal satisfaction of PMs and field teams | Whether the customers of product ops value it | All |

Pendo's vendor guidance lists similar measures, such as PM time on strategic work and time from insight to decision. Its numeric targets come without sources, so set your own.

## How to apply it

This method sets up product operations for a portfolio, or repairs a function that has drifted. It assumes one senior product ops person working with a sponsoring product leader and two or three PMs as pilot customers. Plan on a quarter.

**Weeks 1 and 2: Diagnose.**

1. Interview every PM and two or three field leaders (sales, customer success, support) for thirty minutes each. Ask where they lose time, which numbers they don't trust, where customer evidence goes to die, and which decisions stall. Have the harness cluster the notes and count how often each pain appears.
2. Audit the last two QBRs and the last planning cycle. Mark every metric that appeared with two definitions, every decision that slipped past its date and every meeting that ended without a decision.
3. Score the three pillars red, amber or green, and pick one to fix first. Usually it's the metric glossary, because every ritual depends on it.

**Weeks 3 and 4: Charter.**

4. Write the product ops charter: mission, customers, scope by pillar with Cagan's "we do / we do not" lines, services with response times, owned artifacts, and the measures you'll report. Get the product leader to sign it, and share it with every PM.
5. Agree the measures and take a baseline. At minimum, measure insight latency, metric disputes and ritual decision yield.

**Weeks 5 to 8: Install the foundation.**

6. Publish the metric glossary for the ten to fifteen metrics leaders actually use, with one owner and one system of record each. Retire the duplicates.
7. Draw the tool stack map. Name the system of record for each data type, set read-only as the default harness access, and list overlapping tools to cut at renewal.
8. Build the detailed operating cadence calendar. Start from the meetings that already exist, absorb rituals into them where you can, and cancel any ritual with no decision output.
9. Publish the planning calendar for the next two quarters with the annual overlay. Send it to Finance and the field, not just product.
10. Write the decision-rights register for the five to eight recurring decision types that cause the most friction.

**Weeks 9 to 12: Run it and enable PMs.**

11. Run one full monthly cycle and one quarterly planning cycle on the new calendar. Product ops preps and records; product leaders run the rituals.
12. Package the core templates (PRD, DACI, QBR pack, launch tier) as shared skills in the team's harness, so the formats are applied the same way every time.
13. Assemble the PM onboarding kit and test it on the next new PM. Ask them where they got stuck in week one.
14. Report the measures against the baseline at the QBR. Keep what moved, cut what didn't, and review the charter.

Then put the charter on an annual review. Product ops should shrink its own process as often as it adds to it.

:::onramp If you're a PM without a product ops function
Do steps 2, 6 and 10 for your own product. A one-page metric glossary, a written cadence and five pre-assigned decision types will make you the most organized team in the portfolio, and they're the evidence a leader needs to fund the function.
:::

## The AI lens

### Product ops for AI-powered products

AI features add two things to the business and data insights pillar that most product ops functions weren't built for: quality that has to be measured continuously, and cost that varies with every request.

**Eval reporting.** Anthropic's January 2026 engineering guidance on evaluating AI agents gives product ops a vocabulary it can standardize across teams. An eval runs a **task** over several **trials**, a **grader** scores each one, and the **transcript** (the full trace) shows what the agent did. Graders come in three kinds: code-based (fast, cheap, brittle), model-based (flexible, but needs calibration against human judgment) and human (best, slow). Report two pass rates separately:

- **Capability evals** measure what the agent is learning to do. They should start low and climb.
- **Regression evals** protect what already works. They should sit near 100%; a drop is an incident.

Capability tasks graduate into the regression suite once they pass reliably. The guidance also separates **pass@k** (at least one success in k trials) from **pass^k** (all k trials succeed). That distinction matters most for agents that act. A suggestion the user can ignore is fine at pass@k. An autonomous remediation step needs pass^k, because consistency is the requirement: a 75% per-trial success rate gives roughly a 42% chance that three trials in a row all succeed. The guidance recommends starting with 20 to 50 tasks drawn from real failures, reading transcripts instead of trusting scores alone, and treating a steady 0% as a likely sign of a broken task or grader.

**Cost reporting.** The FinOps Foundation's FinOps for AI working group (its overview was updated in October 2026) names Product as a core persona in AI cost management. Product sets the quality bar with engineering through agreed evals and owns the value claim; FinOps supplies the cost data; Finance gets involved early. Its advice comes down to measuring the use case, not the token. Its unit metrics include cost per inference, blended cost per million tokens, cache hit rate, model fit (the share of requests sent to a more capable model than needed) and, most useful for product, **cost per successful outcome**: total run cost divided by the runs that met the quality bar, so the cost of failed runs counts against the successes. The working group recommends tracking these as distributions per use case; averages hide the few long agent runs that can dominate a bill. Billed tokens also exceed what the user typed, because system prompts, history and retrieved context all count.

Model providers publish usage and cost reports; Anthropic's, for example, breaks token use down by model, workspace and API key, reports daily cost in US dollars, and has data available within about five minutes. Product ops pulls these through a connector, joins them to outcome data and publishes the monthly view.

:::ai The monthly AI quality and cost review
One hour, run by the product leader, prepped by product ops. Agenda: eval scorecard by capability (capability and regression pass rates, pass^k for autonomous actions); new failures added to the suite since last month; cost per successful outcome, as a distribution and a trend; gross margin impact; model routing and caching changes, proposed or made; decisions logged. If a regression rate fell or the cost distribution widened, the meeting decides what to do about it before anything else.
:::

### Doing product ops with AI

The harness changes the work of product ops more than it changes the shape of the function.

- **Ritual pre-work.** Before the metrics review, the harness pulls the dashboard through the analytics connector, compares each metric to its expected range and drafts variance notes for the owners to correct. Before the product review, it assembles team updates into the standard pack. Product ops checks the pack; it no longer builds it.
- **Feedback synthesis.** With read access to tickets, call notes and the feedback repository, the harness clusters a month's signals into themes with linked quotes and accounts. Keep the evidence attached, as Chapter 01 insists: a theme that can't be traced to at least two real customers is the model's opinion.
- **Templates as skills.** A new PM gets the same PRD, DACI and QBR structure as a veteran, and a template change reaches everyone at once.
- **Decision hygiene.** After each ritual, the harness drafts the decision log entry from the notes, with roles from the register filled in, for the Driver to confirm.
- **Onboarding.** A new PM can ask the harness to summarize last quarter's decisions, list open risks and explain the glossary from the team's own documents.

Three rules keep this safe. First, **read-only by default**: write access is granted per use case, logged and reviewed at renewal. Second, **customer data stays in approved tools**: product ops publishes which connectors and models are approved for which data classes. Third, **a human signs every number that reaches a leader**: the harness drafts the variance note, and the metric owner owns it.

## The Beacon case: a charter for the Operations portfolio

:::example Where Beacon starts
Beacon has three PMs, a designer, about 35 engineers across five teams, two applied AI engineers, a product marketing manager and a product ops lead shared with Northlight Observe and Northlight Desk. The last QBR was rough. Three slides showed three different MTTR numbers: one from Observe data, one from Beacon's own telemetry and one from a customer success deck. Gross margin had fallen from 81% to 72% since the agentic features launched, and nobody owned a monthly view of cost per resolved incident. Feedback about the hallucinated root cause that led a customer to roll back the wrong service arrived through four channels, and it took two weeks to piece together which accounts had been affected. Your VP of Product for the Operations portfolio asks you and the shared product ops lead to fix the machinery before Beacon Agents launches at Northlight Live.
:::

**Diagnosis.** You and the ops lead interview the three Beacon PMs, the Observe and Desk group PMs and leads from sales, customer success and support. The harness clusters the notes. Three pains dominate: nobody trusts MTTR, nobody can answer "which customers had autonomous actions rolled back?" without a manual hunt, and planning for Northlight Live runs on a slide rather than a calendar. You score business and data insights red, and the other two pillars amber.

**The charter.** You write it for the whole Operations portfolio, with Beacon as the pilot, and the VP signs it. The "we do not" column does most of the work: the shared ops lead doesn't do PMs' analysis, run their research or decide what goes on any roadmap. The lead owns the metric glossary, the feedback tagging, the two calendars, the decision-rights register, the tool stack map and the onboarding kit. The charter makes no headcount request. Whether the portfolio needs a second ops person is a question for the next annual plan, and the charter's measures will inform it.

**One MTTR.** The glossary entry takes two meetings. Observe measures MTTR from first alert; Beacon measured from incident creation; the CS deck used customer-reported times. The VP decides, using the DACI the ops lead drafted: MTTR runs from first correlated alert to resolution, from Beacon's telemetry, with Observe data as the cross-check. The decision goes in the log, and the other two numbers come off every dashboard.

**The cadence.** You add a monthly AI quality and cost review for Beacon. It tracks diagnosis acceptance rate, autonomous resolution rate, regression pass rate, pass^k for the allowlisted autonomous actions, the distribution of cost per resolved incident, and gross margin. The first session surfaces what the averages had hidden: a small share of very long diagnosis runs accounts for a large share of inference cost. That becomes a bet for the next quarter: cap run length, route simple incidents to a smaller model, and watch whether diagnosis acceptance holds.

**The planning calendar.** The ops lead works back from Northlight Live. Code freeze for Beacon Agents, the enablement milestone for sales and partners, the security documentation pack for reviewers like Sam and the press briefing all go on one page, alongside the quarterly planning weeks and Finance's budget deadline. Two collisions appear immediately: the enablement milestone fell in the same week as week −3 planning, and the security pack was due after code freeze. Both move.

**Decision rights.** The register pre-assigns the decisions that kept stalling.

| Decision | Door type | Framework | Driver / Recommend | Approver / Decide | Contributors / Input | Agree (veto) |
|---|---|---|---|---|---|---|
| Allow autonomous rollback for allowlisted services | One-way | DACI | Principal PM | VP of Product, Operations | Applied AI engineers, security reviewer, SRE design partner (Priya's team), CS | n/a |
| Move Beacon Agents to per-resolved-incident pricing | One-way | DACI | Principal PM | Proposed: GM or CPO (the case doesn't name the approver; confirm) | Finance, sales, PMM, CS | n/a |
| Sunset Beacon Classic | One-way | RAPID | Principal PM | VP of Product, Operations | CS, support, engineering | Legal, on contract terms |
| Change allowlist defaults in a release | Two-way | RACI | Beacon PM for Act | Principal PM | Security reviewer | n/a |
| Reorder next sprint's backlog | Two-way | None: team decides | Team PM | Team PM | Engineering lead | n/a |

The rollback decision gets the heavy process: a full DACI document, pass^k eval results on the allowlisted actions, and a security review. The backlog reorder gets none.

**The stack.** The tool stack map names one system of record per data type and sets harness access: read-only for work tracking, analytics, eval results and provider cost reports; read with customer identifiers masked for the feedback repository; read-write only in the team's docs space. The rollback question that took two weeks now takes an afternoon, because the harness can join rollback events from analytics to the tagged tickets in the feedback repository.

**Measures.** The charter commits to three by the next QBR: one MTTR definition used everywhere, same-day answers to the rollback question, and a shorter time to first logged decision for the next PM who joins. That PM arrives a month later to cover Leo's MSP persona and gets the onboarding kit on day one, including a schedule for shadowing calls with two MSP partners and a set of first-week prompts. They log a first decision (the multi-tenant view's default sort, a two-way door) in week three.

## Product 360 artifacts

```template id="28-product-ops-charter" title="Product operations charter"
# Product operations charter · [Portfolio or organization] · v[n] · [Date]

**Sponsor:** [Product leader]   **Product ops lead:** [Name]   **Review date:** [Date, at least annually]

## Mission
One sentence: Product operations makes it faster and safer for [product teams] to make evidence-based decisions by [how].

## Customers of product ops
| Customer | What they need from us | How we'll know it works |
|---|---|---|
| PMs and designers | | |
| Product leaders | | |
| Field (sales, CS, support, partners) | | |
| Finance | | |

## Scope by pillar
| Pillar | We do | We do not |
|---|---|---|
| Business and data insights | Own the metric glossary and one source of truth; provide self-serve dashboards; publish the monthly AI quality and cost report | Do teams' analysis for them |
| Customer and market insights | Run the feedback repository and its tagging; maintain the research panel; publish the monthly voice-of-the-customer readout | Run teams' discovery or interviews for them |
| Process and governance | Publish the cadence and planning calendars; prep and record rituals; maintain the decision-rights register, templates and skills; onboard PMs | Make product decisions; own the roadmap; add process that no decision needs |

## Services and response times
| Service | Request route | Response time |
|---|---|---|
| New metric or definition change | | [e.g. decision within 2 weeks] |
| Access to a tool or connector | | |
| Ad hoc data question | | [self-serve first; escalation within N days] |
| New template or skill | | |

## Owned artifacts
- Metric glossary
- Operating cadence calendar
- Planning calendar with annual overlay
- Decision-rights register
- Tool stack map
- Template and skill library
- PM onboarding kit

## Decision rights of product ops itself
Product ops decides: [tool selection within budget, template formats, calendar dates, connector access defaults].
Product ops recommends, a product leader decides: [new rituals, new required steps, tool purchases above threshold].
Product ops never decides: roadmap content, priorities, pricing, customer commitments.

## Measures (baseline and target)
| Measure | Baseline | Target | Date |
|---|---|---|---|
| Insight latency | | | |
| Metric disputes per quarter | | | |
| Ritual decision yield | | | |
| New PM time to first logged decision | | | |

## Process budget
Every new ritual, template or required step names the decision it improves. Each review, we retire at least one thing that no longer does.
```

```template id="28-operating-cadence-calendar" title="Operating cadence calendar (detailed)"
# Operating cadence calendar · [Product or portfolio] · [Quarter]

**Owner:** [Product ops lead]   **Sponsor:** [Product leader]   **Last reviewed:** [Date]

| Ritual | Frequency and slot | Runs it | Product ops prep | Attendees | Inputs | Decision output | Recorded in | Harness pre-work |
|---|---|---|---|---|---|---|---|---|
| Metrics review | Weekly, [day, time], 30 min | Product leader or PM | Glossary check on every number; dashboard refreshed | PMs, eng leads, analyst | Dashboard, risk register | Variances explained; actions; escalations | Decision log | Draft variance notes against expected ranges |
| Team sync | Weekly, [slot] | PM | Decision log and risk register linked | Product team | Decision log, discovery log | Decisions logged | Decision log | Summarize open decisions and new evidence |
| Sprint review and planning | Biweekly, [slot] | Eng lead and PM | None | Product team | Backlog, release plan | Sprint commitment | Tracker | Draft release notes from closed work |
| Product review | Monthly, [slot], 60 min | Product leader | Standard update pack per team | Leadership, PMs, eng, design, PMM | Roadmap, OKRs, competitive changes, insight summary | Roadmap changes; asks for help | Decision log | Assemble team updates into the standard pack |
| Voice-of-the-customer readout | Monthly, [slot], 45 min | Product ops | Themes by segment from the repository | PMs, CS, support, sales | Feedback repository, win-loss | Themes assigned to owners | Feedback repository | Cluster the month's signals with linked quotes and accounts |
| AI quality and cost review | Monthly, [slot], 60 min | Product leader | Eval scorecard; cost distribution; margin view | PMs, applied AI, eng, finance partner | Eval results, usage and cost reports | Quality and cost actions; model or routing changes | Decision log | Draft scorecard and flag regressions and cost outliers |
| Quarterly business review | Quarterly, week 13 | Product leader | Results pack; OKR grades | Leadership, finance, sales, CS | Business model, OKRs, lifecycle stage | Lessons; staffing and pricing asks | QBR record | Draft the results narrative from the quarter's data |
| Planning or betting table | Quarterly, week −3 | Product leader | Insight pack; ranked bets; capacity | Product and eng leadership | Draft bets, capacity estimate | Next quarter's bets | Roadmap | Summarize each bet against OKRs and evidence |
| Roadmap publication | Quarterly, week −1 | Product ops with PMM | Field-safe roadmap version | Field, partners | Approved bets | Published roadmap | Roadmap | Draft the field version and FAQ |
| Strategy refresh | Annually, [month] | Product leader | Durable artifacts audited for staleness | Leadership | Vision, strategy, personas, positioning | Strategy for the year | Strategy one-pager | Flag contradictions between durable artifacts |
| Annual planning | Annually, aligned to fiscal year | Product leader with Finance | Budget template; planning calendar | Leadership, finance | Strategy, business case | Plan of record; budget | Annual plan | Draft the plan narrative from the strategy and results |

## Rules
1. Every ritual produces a decision or is cancelled.
2. Every decision is recorded where the table says.
3. Two-way-door decisions are made in the team rituals. One-way-door decisions follow the decision-rights register.
```

```template id="28-planning-calendar" title="Planning calendar"
# Planning calendar · [Organization] · FY[year]

**Owner:** [Product ops lead]   **Fiscal year starts:** [Date]   **Annual customer event:** [Date]

## Quarterly milestones (repeat for each quarter)
| Week (relative to quarter start) | Milestone | Owner | Required input | Q1 date | Q2 date | Q3 date | Q4 date |
|---|---|---|---|---|---|---|---|
| −6 | Insight pack published | Product ops | Metrics vs OKRs, customer themes, competitive changes, AI eval and cost trends | | | | |
| −4 | Draft bets due | PMs | One-page bets linked to OKRs | | | | |
| −3 | Betting table or portfolio review | Product leader | Ranked bets, capacity estimate | | | | |
| −2 | Capacity and dependency check | Eng leads | Staffing plan, dependencies | | | | |
| −1 | Roadmap published (internal and field) | Product ops with PMM | Approved bets | | | | |
| 1 | Quarter starts; OKRs set | Product leader | Final OKRs | | | | |
| 6 | Mid-quarter check | Product ops | OKR progress, risks | | | | |
| 13 | QBR | Product leader | Results, grades, lessons | | | | |

## Annual overlay
| Milestone | Date | Owner | Depends on |
|---|---|---|---|
| Strategy refresh | | | |
| Budget submission to Finance | | | |
| Board meeting(s) | | | |
| Annual pricing review | | | |
| Customer event: code freeze | | | |
| Customer event: enablement complete | | | |
| Customer event: security and compliance pack ready | | | |
| Customer event | | | |

## Collisions found
| Week | Collision | Resolution | Decided by |
|---|---|---|---|
| | | | |
```

```template id="28-daci-decision" title="DACI decision document and decision-rights register"
# DACI: [The question we're deciding]?

**Status:** Not started / In progress / Decided   **Impact:** High / Medium / Low   **Door type:** One-way / Two-way
**Due date:** [Date]   **Forum:** [Ritual where it will be decided]

## People
- **Driver:** [Name] (gathers input, sets scope, gets a decision by the due date)
- **Approver:** [One name]
- **Contributors:** [Names and what expertise each brings]
- **Informed:** [Groups to tell once decided]
- **Agree (only if a function holds a veto, RAPID style):** [Function and the condition they're checking]

## Background
[One or two sentences.]

## Relevant data
[Links to the evidence, with dates. Eval results and cost data for AI decisions.]

## Decision factors
[Cost, time, scalability, customer risk, reversibility, security, margin]

## Options considered
| Option | Pros | Cons | Estimated resources and cost |
|---|---|---|---|
| A | | | |
| B | | | |
| Do nothing | | | |

## Outcome
[Decision, date, approver, one-paragraph rationale]

## Action items
| Action | Owner | Due |
|---|---|---|
| | | |

---

# Decision-rights register · [Portfolio] · [Date]

| Recurring decision type | Door type | Framework | Driver or Recommend | Approver or Decide | Contributors or Input | Agree (veto) | Informed | Forum |
|---|---|---|---|---|---|---|---|---|
| Pricing model change | One-way | DACI | | | | | | |
| Deprecation or sunset | One-way | RAPID | | | | Legal | | |
| New autonomous action in production | One-way | DACI | | | | | | |
| AI model swap for a shipped feature | Depends on eval results | DACI | | | | | | |
| Roadmap change after commit | Two-way | DACI (light) | | | | | | |
| Launch tier | Two-way | RACI | | | | | | |
```

```template id="28-tool-stack-map" title="PM tool stack map"
# Tool stack map · [Organization] · [Date]

**Owner:** [Product ops lead]   **Approved data classes per model and connector:** [Link]

| Category | System of record | Other tools in use (overlap) | Owner | Harness access (none / read / read-write) | Agents inside the tool, and what they can write | Data it feeds | Ritual that consumes it | Renewal date | Annual cost |
|---|---|---|---|---|---|---|---|---|---|
| Work tracking and roadmapping | | | | | | | | | |
| Product analytics and experimentation | | | | | | | | | |
| Feedback and research repository | | | | | | | | | |
| Docs and knowledge | | | | | | | | | |
| AI harness and agents | | | | n/a | | | | | |
| AI quality and cost observability | | | | | | | | | |

## Access rules
1. Read-only is the default for every connector.
2. Write access is granted per use case, logged, and reviewed at renewal.
3. Customer data goes only to approved tools and models.
4. One system of record per data type. Overlaps are listed above and resolved at renewal.

## Shared skills
| Skill | Encodes template | Owner | Last updated |
|---|---|---|---|
| | | | |

## Cuts and changes at next renewal
| Tool | Action | Saving | Date |
|---|---|---|---|
| | | | |
```

```template id="28-ai-quality-cost-review" title="Monthly AI quality and cost report"
# AI quality and cost report · [Product] · [Month]

**Prepared by:** [Product ops]   **Reviewed in:** [Ritual, date]   **Sources:** [eval harness run IDs, usage and cost report period]

## Eval scorecard
| Capability | Eval type (capability / regression) | Tasks | Pass rate | pass@k or pass^k (k = ) | Change vs last month | Grader type |
|---|---|---|---|---|---|---|
| | | | | | | |

## New failures added to the suite
| Failure | Source (incident, ticket, transcript) | Added as task ID |
|---|---|---|
| | | |

## Outcome and cost
| Use case | Successful outcomes | Cost per successful outcome (p50 / p90) | Cache hit rate | Model fit notes | Trend |
|---|---|---|---|---|---|
| | | | | | |

## Margin
Gross margin impact this month: [value and change]. Main driver: [one sentence].

## Transcripts read
[Number read, and the one pattern worth discussing.]

## Decisions requested
1.
2.
```

```template id="28-pm-onboarding-kit" title="PM onboarding kit"
# PM onboarding kit · [Product or portfolio] · [New PM] · Start date [Date]

**Buddy:** [PM]   **Manager:** [Name]   **Product ops contact:** [Name]

## Before day one
- [ ] Access requests filed for every system on the tool stack map
- [ ] Harness set up with team skills and read-only connectors
- [ ] Added to the rituals marked below

## Read in week one
- Product 360 index and its twelve spine artifacts
- Metric glossary and North Star tree
- Last two QBR packs and the decision log for the last two quarters
- Decision-rights register
- Charter of the product ops function

## Rituals to attend
| Ritual | Attend / observe / skip for now | Starting week |
|---|---|---|
| | | |

## Customer exposure
| Week | Customer call to shadow | Persona | Notes |
|---|---|---|---|
| | | | |

## First-week harness prompts
1. "Summarize the decisions in the decision log from the last two quarters, grouped by theme, with the approver and date for each."
2. "List the open risks in the risk register and which ritual last discussed each."
3. "Explain the five metrics in the glossary I'm most likely to be asked about, with their definitions and current values."
4. "From the feedback repository, summarize the top themes for [persona] this quarter with linked quotes."

## 30 / 60 / 90
| By day | Outcome | Evidence |
|---|---|---|
| 30 | Can explain the strategy, metrics and top risks; first two-way decision logged | |
| 60 | Owns a ritual; first DACI driven | |
| 90 | Product 360 artifacts for the area refreshed; first bet through planning | |

## Feedback on this kit
Where did you get stuck in week one? [Answer goes to product ops.]
```

## Prompts

```prompt title="Diagnose where product operations is needed"
Goal: Find which product ops pillar to fix first, from evidence rather than complaints.
Paste in: notes from PM and field-leader interviews, the last two QBR packs, and the last planning cycle's calendar and decision log. Remove names if your harness isn't approved for HR-sensitive material.

You are helping me diagnose the product operations needs of [organization]. Product ops has three pillars: business and data insights, customer and market insights, and process and governance.

1. From the interview notes, list every distinct pain, how many people raised it and which pillar it belongs to. Quote the notes.
2. From the QBR packs, list every metric that appears with more than one value or definition, with the slide references.
3. From the planning calendar and decision log, list decisions that slipped past their dates and meetings that ended with no logged decision.
4. Score each pillar red, amber or green, with the evidence for each score.
5. Recommend the one pillar to fix first and the first three actions.

Use only the material provided. If something isn't supported by it, say "no evidence."

Check the output: confirm two of the metric conflicts yourself against the slides. If the recommendation is "fix everything," push back and ask for one pillar.
```

```prompt title="Draft a product ops charter with guardrails"
Goal: Get a first-draft charter that scopes product ops as a force multiplier, not a PMO.
Paste in: the diagnosis, the team structure, the sponsoring leader's goals, and any existing product ops job description.

Draft a product operations charter for [organization] with these sections: mission (one sentence), customers of product ops, scope by pillar in a "we do / we do not" table, services with response times, owned artifacts, decision rights of product ops itself, measures with baselines to collect, and a process budget rule.

Rules:
- Product ops enables and does not decide. It never owns roadmap content, priorities, pricing or customer commitments.
- It provides self-serve data, not analysis on demand; research infrastructure, not research.
- Every service and artifact must name the decision it makes faster or better. Cut any that can't.
- Flag anything in my inputs that would turn the function into a project management office or split the PM role.

Check the output: read the "we do not" column aloud to two PMs. If either says "but we need that," decide explicitly whether it belongs to product ops or to them.
```

```prompt title="Build the detailed operating cadence calendar"
Goal: Turn existing meetings into a cadence where every ritual produces a decision.
Paste in: the list of recurring meetings with attendees and agendas, the fiscal calendar, the annual customer event date, and the metric glossary.

Design a detailed operating cadence calendar for [product or portfolio]. For each ritual give: frequency and slot, who runs it, what product ops prepares, attendees, inputs, the decision it produces, where the decision is recorded, and what the AI harness can draft beforehand.

Reuse existing meetings wherever possible. Include a weekly metrics review, a monthly product review, a monthly voice-of-the-customer readout, a monthly AI quality and cost review if we ship AI features, a quarterly business review kept separate from quarterly planning, and an annual strategy refresh aligned to the fiscal year.

Then list every existing meeting you recommend cancelling or merging, and why. Finish with the weekly hours the cadence costs a PM.

Check the output: any ritual whose "decision output" is "discussion" or "alignment" has no decision. Cut it or give it one.
```

```prompt title="Write a DACI and place it in the decision-rights register"
Goal: Get a decision document with clear roles and the right process weight.
Paste in: the decision question, background, the evidence you have, the options, and the people involved with their roles.

Draft a DACI document for this decision: [question]. Use this structure: title phrased as the question; status, impact, door type and due date; Driver, one Approver, Contributors and Informed; one- or two-sentence background; relevant data with sources; decision factors; an options table with pros, cons and estimated resources and cost, including "do nothing"; action items.

Then:
1. Say whether this is a one-way or two-way door, and why. If it's a two-way door, recommend a lighter process.
2. Say whether any function holds a real veto (Security, Legal, regulatory). If so, add an Agree role, RAPID style, and state the condition they're checking.
3. Propose a row for our decision-rights register so this type of decision is pre-assigned next time.

Don't invent evidence. Mark any option whose cost or risk you can't estimate from the inputs.

Check the output: there must be exactly one Approver. If the draft names two, or a committee, fix it before sharing.
```

```prompt title="Map the tool stack and set harness access"
Goal: One system of record per data type, and safe defaults for what the harness can reach.
Paste in: the list of tools in use with owners, costs and renewal dates; the connectors your harness has; and your data classification policy.

Build a tool stack map for [organization] using these categories: work tracking and roadmapping; product analytics and experimentation; feedback and research repository; docs and knowledge; AI harness and agents; AI quality and cost observability.

For each category give: the system of record, overlapping tools, owner, recommended harness access (none, read or read-write) with a reason, any agents inside the tool and what they can write, which ritual consumes the data, renewal date and cost.

Default every connector to read-only. Recommend write access only where a named use case needs it, and say how it should be logged. List overlaps to resolve at renewal with the likely saving.

Check the output: confirm against your data policy that no connector with customer data is routed to an unapproved model. Ask the tool owners to confirm the access levels before you publish the map.
```

```prompt title="Prepare the monthly AI quality and cost review"
Goal: A one-page view of whether the AI features are getting better, staying safe and paying for themselves.
Paste in (or connect the harness to): this month's eval results with task counts and grader types, the list of new failures, the provider usage and cost report for the period, outcome counts from product analytics, and last month's report. Use only approved tools for production transcripts.

Prepare the monthly AI quality and cost report for [product].

1. Eval scorecard by capability: capability and regression pass rates reported separately, and pass^k for any capability where the agent acts without a human. Flag any regression rate below [threshold] and any capability rate stuck at 0% (a likely broken task or grader).
2. New failures since last month, and whether each has been added to the suite.
3. Cost per successful outcome for each use case: total cost divided by runs that met the quality bar. Show the median and the 90th percentile, and the trend.
4. The top three cost drivers, including any long-tail runs, and the gross margin impact.
5. Three decisions the review should make, each with the evidence.

Don't average away the distribution. Don't call a change an improvement unless it beats last month by more than run-to-run noise.

Check the output: open three transcripts behind the biggest change and confirm the story matches. Reconcile total cost with the provider's report before the meeting.
```

```prompt title="Generate a PM onboarding kit from team documents"
Goal: Give a new PM a week-one kit built from the team's real artifacts.
Paste in (or connect the harness to): the Product 360 index, metric glossary, decision log, risk register, cadence calendar, decision-rights register, tool stack map and the last two QBR packs.

Build an onboarding kit for a new PM joining [team] to own [area or persona]. Include: before-day-one access steps; a reading list in priority order with one line on why each matters; which rituals to attend, observe or skip for now; a customer-call shadowing plan for the first four weeks; five first-week prompts the PM can run against our documents; and a 30/60/90 plan with evidence for each milestone.

Write the kit for someone experienced in product management but new to our product, customers and jargon. Define every acronym from the glossary the first time it appears.

Check the output: give the kit to the most recent joiner and ask what was missing in their first week. Add it.
```

## Anti-patterns

:::warn The PMO in disguise
Product ops starts approving roadmaps, chasing status and enforcing gates. PMs start writing for product ops instead of for customers. Product ops supplies inputs and runs the machinery; product leaders and PMs decide. If the charter can't say what product ops does not do, write that column first.
:::

:::warn Process becomes the thing
Every quarter adds a template, a review or a required field, and nothing is ever retired. Each ritual and template should name the decision it improves. Run a process budget: when something new goes in, something old comes out.
:::

:::warn Two in a box
The organization splits the PM job into a "strategic" PM and an "operational" product ops partner for each team. The PM loses touch with the data and the details, and the ops partner ends up making product calls without the accountability. Product ops serves many teams from a central function. It doesn't pair with each PM.
:::

:::warn The analysis desk
Product ops becomes the place PMs send data questions, and the queue grows until answers take a week. Build self-serve access and a trusted glossary, and coach PMs to ask the harness directly. Product ops should answer the question "where is the trusted number?", not every question about it.
:::

:::warn Every decision through the one-way-door process
A backlog reorder gets the same DACI, review and sign-off as a pricing change. Teams stop experimenting and decisions queue for the monthly forum. Pre-assign door types in the decision-rights register and keep two-way doors with the team.
:::

:::warn Connectors with write access everywhere
The harness and the in-tool agents can create tickets, edit roadmaps and post to channels, and nobody knows which changes a person approved. Default every connector to read-only, grant write access per use case, and log it.
:::

:::warn AI cost reported as an average
The monthly report shows a single average cost per request, which looks fine while a small share of long agent runs drives most of the bill. Report cost per successful outcome as a distribution, and read the transcripts behind the tail.
:::

## Checklist

- [ ] The organization has checked the three signals (shared calendar, unstable numbers, deck season) and chosen one pillar to fix first.
- [ ] A signed product ops charter states its customers, services, owned artifacts and what product ops does not do.
- [ ] The metric glossary gives each leadership metric one definition, one owner and one system of record.
- [ ] Customer signals from every channel land in one feedback repository with consistent tags.
- [ ] The detailed cadence calendar names, for every ritual, who runs it, what product ops preps, the decision it produces and where it's recorded.
- [ ] The QBR and quarterly planning are separate rituals.
- [ ] The planning calendar shows quarterly milestones with owners and inputs, plus the annual overlay (fiscal year, budget, board, customer event).
- [ ] A decision-rights register pre-assigns door type, framework and roles for recurring decisions, with exactly one approver each.
- [ ] The tool stack map names one system of record per category, with read-only harness access as the default.
- [ ] Core templates are packaged as shared skills in the team's harness.
- [ ] Teams shipping AI features hold a monthly AI quality and cost review with separate capability and regression rates, pass^k for autonomous actions and cost per successful outcome as a distribution.
- [ ] A PM onboarding kit exists and was tested on the most recent joiner.
- [ ] Product ops reports its measures against a baseline at least quarterly, and retires at least one process each review.

## Key takeaways

- Product operations exists to make evidence-based decisions cheaper to reach. Perri and Tilles organize it into three pillars, which this book names business and data insights, customer and market insights, and process and governance.
- Product ops enables and does not decide. Cagan's guardrails (self-serve data rather than analysis, research infrastructure rather than research, coordination rather than ownership of planning) are what keep it from becoming a PMO.
- Create the function when teams share a planning calendar, leaders can't get the same number twice, and PMs spend planning season on slides. Start with one senior person and the loudest pillar, usually the metric glossary.
- The cadence and planning calendars make Chapter 00's rituals real. Every ritual has an owner, prep, a decision and a record, and the planning calendar gets the evidence to the room before the choices are made.
- Pre-assign decision rights by door type. DACI covers most product decisions, RAPID handles a real veto, RACI covers recurring work, and two-way doors stay with the team.
- In 2026 the AI harness reaches every tool through connectors. Product ops sets the systems of record, read-only defaults and shared skills, and for AI products owns the monthly report on eval results and cost per successful outcome.
