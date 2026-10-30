<p class="lead">You've been handed a product surface area: a product, a set of customers, some teams and a revenue line. You have about 90 days before people expect you to know what you're talking about. This chapter turns the whole book into one playbook for those 90 days: what to build, in what order, how to use an AI harness to draw the answers out of you and your organization, and how to keep the result true after day 90.</p>

## Why this matters

A Principal PM who takes over an existing product inherits the product and a pile of documents describing a product that no longer quite exists. The strategy deck predates the last pricing change. The personas leave out the buyer. The roadmap in the ticketing tool has drifted from last quarter's executive review. Nobody is lying; the documents stopped being maintained at different times, and now they disagree.

The usual response is to read everything, meet everyone and form a view. That works, slowly, and it leaves the view in your head. Ask "what's our North Star?" in week six and you'll have an answer; the organization still won't. Chapter 00 argued for a Product 360 instead: a connected set of artifacts with owners and review dates that anyone (and any AI harness) can read. This chapter is about building one under time pressure while doing the job.

Michael Watkins, in *The First 90 Days* (first published in 2003), framed a leader's transition as a set of tasks rather than a period of absorption: accelerate your learning, diagnose the situation, agree on expectations with your boss, secure early wins, build coalitions and your team, and manage yourself. Two features of product leadership in a B2B or platform business change how those tasks play out.

First, **90 days is shorter than most enterprise release cycles**. You won't ship much that you started. Your early wins are decisions: a scope dispute settled, a pricing question answered with data, a launch plan that finally has an owner. A Product 360 is how you make those decisions visible and durable.

Second, **in 2026 you don't do this work alone**. A harness connected to your document tools, ticketing, CRM and analytics can read everything you inherited faster than you can open it. It can't decide what your North Star should be, or whether a legacy engine sunsets this year. The bottleneck has moved from finding information to making and recording judgments, and this chapter's central technique, the **grilling session**, targets it: the harness interviews you one question at a time, proposes an answer from the evidence, challenges weak answers and writes everything down.

## The playbook

### Three phases, five moves

Time runs across three 30-day phases. Within each phase, you repeat a loop of five moves.

The phases follow Watkins's sequence, adapted for product work. In **days 1 to 30 (learn and anchor)** you scope, inventory, load the evidence into the harness, map stakeholders, ask only factual questions and land one early decision. In **days 31 to 60 (decide and build the spine)** you grill dimension by dimension, generate the spine artifacts from the answers and audit them against each other. In **days 61 to 90 (operate and prove)** you run the cadence, produce the event artifacts the calendar demands, hold a business review on the 360 and score its maturity.

The five moves are this book's synthesis. They borrow two patterns that Erik Schluntz and Barry Zhang described in Anthropic's 2024 guidance on building agents: **prompt chaining**, where fixed steps each take the previous step's output with a check in between, and the **evaluator-optimizer** loop, where one pass produces and a second critiques against clear criteria. Here the checks between steps are you.

1. **Anchor.** Give the harness your reference materials and connectors. It inventories them, maps them to the nine dimensions, quotes the evidence and produces a gap list.
2. **Grill.** Run a grilling session per dimension. The harness asks; you decide; every answer goes into a log.
3. **Generate.** The harness turns the log plus the evidence into the book's templates, with every claim tagged to its source.
4. **Audit.** A separate pass checks the artifacts against each other and against their sources.
5. **Maintain.** The cadence keeps the artifacts true: weekly exception briefs, monthly roadmap checks, quarterly and annual re-grills.

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 310" role="img" aria-label="The 90-day playbook: three phases across the top and the five-move loop of anchor, grill, generate, audit and maintain underneath">
  <rect x="20" y="20" width="220" height="70" rx="12" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".5"/>
  <text x="36" y="46" class="t">Days 1 to 30</text>
  <text x="36" y="66" class="s">Learn and anchor</text>
  <text x="36" y="82" class="s">Index · stakeholder map · gap list</text>
  <rect x="250" y="20" width="220" height="70" rx="12" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)" stroke-opacity=".5"/>
  <text x="266" y="46" class="t">Days 31 to 60</text>
  <text x="266" y="66" class="s">Decide and build the spine</text>
  <text x="266" y="82" class="s">Spine 2 to 9 · AI four · day-60 audit</text>
  <rect x="480" y="20" width="220" height="70" rx="12" fill="var(--a3)" fill-opacity=".12" stroke="var(--a3)" stroke-opacity=".5"/>
  <text x="496" y="46" class="t">Days 61 to 90</text>
  <text x="496" y="66" class="s">Operate and prove</text>
  <text x="496" y="82" class="s">Cadence · events · health review</text>
  <rect x="20" y="140" width="120" height="60" rx="10" class="box"/>
  <text x="80" y="166" text-anchor="middle" class="t">Anchor</text>
  <text x="80" y="186" text-anchor="middle" class="s">gap list</text>
  <rect x="165" y="140" width="120" height="60" rx="10" class="box"/>
  <text x="225" y="166" text-anchor="middle" class="t">Grill</text>
  <text x="225" y="186" text-anchor="middle" class="s">session log</text>
  <rect x="310" y="140" width="120" height="60" rx="10" class="box"/>
  <text x="370" y="166" text-anchor="middle" class="t">Generate</text>
  <text x="370" y="186" text-anchor="middle" class="s">artifacts</text>
  <rect x="455" y="140" width="120" height="60" rx="10" class="box"/>
  <text x="515" y="166" text-anchor="middle" class="t">Audit</text>
  <text x="515" y="186" text-anchor="middle" class="s">contradictions</text>
  <rect x="600" y="140" width="100" height="60" rx="10" class="box"/>
  <text x="650" y="166" text-anchor="middle" class="t">Maintain</text>
  <text x="650" y="186" text-anchor="middle" class="s">cadence</text>
  <line x1="140" y1="170" x2="165" y2="170" class="ln"/>
  <line x1="285" y1="170" x2="310" y2="170" class="ln"/>
  <line x1="430" y1="170" x2="455" y2="170" class="ln"/>
  <line x1="575" y1="170" x2="600" y2="170" class="ln"/>
  <line x1="650" y1="200" x2="650" y2="250" class="ln"/>
  <line x1="650" y1="250" x2="225" y2="250" class="ln"/>
  <line x1="225" y1="250" x2="225" y2="200" class="ln"/>
  <text x="437" y="270" text-anchor="middle" class="s">quarterly and annual re-grill of living and durable artifacts</text>
  <text x="80" y="130" text-anchor="middle" class="s" style="fill:var(--a2)">gate: you approve</text>
  <text x="225" y="130" text-anchor="middle" class="s" style="fill:var(--a2)">gate: you approve</text>
  <text x="515" y="130" text-anchor="middle" class="s" style="fill:var(--a2)">gate: you approve</text>
  <text x="360" y="300" text-anchor="middle" class="s" style="fill:var(--muted)">Three human gates: the PM approves the gap list, each session log and the audit.</text>
</svg>
<figcaption>The 90-day playbook. The phases set what you build; the five moves set how you build each artifact. Maintenance loops back into grilling, so the 360 is re-decided on a rhythm rather than rewritten from scratch. The gates sit after the gap list, each session log and the audit.</figcaption>
</figure>

### Facts and decisions

The most important distinction in this chapter is between two kinds of missing information.

A **fact** is already true somewhere in your organization: current ARR, open escalations, the next launch date, the gross margin trend, what the last ten win/loss notes say. Facts have owners and sources. You shouldn't be asked for them, and you shouldn't make them up; the harness should fetch them through a connector, cite the source and ask you to confirm.

A **decision** is something only a person can supply: which segment you'll stop serving, what the North Star should be, whether a legacy engine sunsets this year, how much margin you'll trade for growth. Decisions have deciders and trade-offs. No connector holds them, and a harness that invents them is doing your job badly.

Asking a model to "write our strategy" blurs the two. It returns something fluent that mixes real facts, plausible-sounding facts and decisions nobody made. The grilling session separates them: facts get fetched and cited, decisions get asked one at a time with a recommendation you can accept, change or reject.

Connectors make the fact side practical. The Model Context Protocol, which Anthropic introduced in November 2024 and which moved to vendor-neutral governance under the Linux Foundation's Agentic AI Foundation in December 2025, lets the harness look things up in your document tools, ticketing, CRM and data platforms under the same access rules as you. Chapter 19 covers setting up sources and verifying what the harness reports.

:::key The one rule
Never ask the PM for a fact a connected source can answer, and never let the harness supply a decision the PM hasn't made. Everything in the 360 is either sourced, decided or marked as a gap.
:::

### The grilling session

A grilling session is a structured interview in which the harness asks the questions. It has a clear lineage. In 2023, Jules White and colleagues at Vanderbilt published a catalog of prompt patterns that included the **Flipped Interaction** pattern: instead of the user asking the model questions, the model asks the user questions until it has what it needs to reach a goal. They stressed that a flipped prompt should always state the goal of the interaction, and that the more specific the constraints on what to collect, the better the result.

Two later sources support the mechanism. Belinda Li, Alex Tamkin, Noah Goodman and Jacob Andreas tested model-led questioning in three domains and found that it often captured what people wanted more informatively than prompts or labels the users wrote themselves, took less effort, and surfaced considerations people hadn't anticipated. Their domains weren't product strategy, so treat this as evidence that the mechanism works rather than proof that grilling produces better strategy. And Anthropic's guidance for Claude Code recommends the same move for software: when you haven't worked out what you want, have the model interview you until it could write the specification, write it down, then build from it in a fresh session.

This book's grilling session adds three things the Flipped Interaction pattern doesn't specify:

1. **A recommended answer with every question.** The harness proposes an answer with its reasoning and evidence. You react instead of composing from scratch, which is faster and exposes the harness's assumptions.
2. **Challenges against explicit tests.** The harness doesn't accept a weak answer just because you gave it.
3. **A written log.** Every question, recommendation, answer, challenge and status goes into a grilling session log, which later becomes the source for the artifacts.

The challenges are the part people skip, and the reason not to is sycophancy. Mrinank Sharma and colleagues at Anthropic found in 2023 that five state-of-the-art assistants tended to tell users what they wanted to hear across four free-form tasks, and that in human preference data, responses matching the user's views were more likely to be preferred. A harness that agrees with you launders your weakest answers into confident-looking artifacts, which is worse than no session at all. So the master grilling prompt gives the harness explicit tests and tells it not to agree for its own sake.

The tests are this book's synthesis, in the Socratic tradition of asking for clarification, evidence, assumptions, alternatives and consequences. Every answer in a grilling session should pass all seven:

| Test | Passes when the answer... | Typical failing answer | Chapter |
|---|---|---|---|
| **Specific** | Names a segment, number, date or owner | "Enterprise customers," "soon" | 17 |
| **Evidenced** | Cites a source, or is labeled an assumption with a test | "Customers love it" | 01, 19 |
| **Falsifiable** | Says what result would prove it wrong | "Agents will transform ops" | 01 |
| **Trade-off named** | Says what you give up | A strategy with no refusals | 03 |
| **Consistent** | Doesn't contradict an earlier answer or an existing artifact | Positioning that promises what the risk assessment forbids | 00 |
| **Owned** | Someone is accountable and there's a review date | "The team will track it" | 29 |
| **Decision-relevant** | Changes a decision someone makes in the next quarter | A metric nobody acts on | 17 |

An answer that fails a test gets one push: the harness names the test, explains the gap and asks again. If the second answer still fails, the harness stops arguing. It logs the item as **overridden**, with your reason for keeping the answer, or as **open**, with an owner if someone else holds the answer. An open item in the log is honest; the same gap hidden inside a confident artifact is what misleads people later.

Each dimension's session ends the same way: a short readback of what was decided, a **premortem** and your confirmation. Gary Klein described the premortem in 2007: the team assumes the project has already failed and works out why. In a grilling session the harness scopes it to the dimension: "It's 90 days from now and this artifact misled a decision. What happened?" The answers often surface the assumption you'd been avoiding.

:::onramp If grilling sounds uncomfortable
It's meant to be a little uncomfortable, like a good one-on-one with a demanding manager. "I don't know yet" is always a legitimate answer: the harness logs it as open, asks who would know and moves on. What won't survive is an answer you can't defend.
:::

### Live mode and file mode

There are two ways to run a grilling session, and they suit different dimensions.

**Live mode** is a conversation: one question at a time, a recommendation, your answer, a challenge, the next question. It suits judgment-heavy dimensions (Strategy, Business, Leadership) where each answer changes which question should come next. A session of 20 to 40 questions per dimension, over 45 to 90 minutes, is a reasonable target. Those numbers are this book's guidance, not research findings.

**File mode** is a written questionnaire. The harness writes every question for a dimension into a document, each with its recommended answer and a blank "Your answer" line. You or a stakeholder edit the file; untouched recommendations count as accepted; the harness ingests it, challenges the weak answers in a short live follow-up and writes the log. File mode suits fact-heavy dimensions and anything other people must answer: the Go-to-market questions to your product marketing manager, the Business questions to finance, the Build questions to your engineering lead.

There's a second reason to split by dimension. Anthropic's applied AI team, writing about context engineering in 2025, described **context rot**: recall degrades as the context grows, so context is a finite resource with diminishing returns. Their remedies apply directly: keep structured notes outside the conversation (the grilling log), load material just in time, and summarize and restart when a session runs long. One marathon conversation across nine dimensions will quietly lose what you decided in the first hour.

### Anchoring the harness in reference materials

Without evidence, a harness can only recommend from general knowledge. Before the first session, give it what already describes the product: strategy decks, PRDs, the pricing page, QBR decks, win/loss notes, the roadmap, dashboard and finance exports, support escalations. Where connectors exist it reads the sources directly; elsewhere you supply exports.

Anthropic's prompting guidance for long documents gives three rules that generalize to any harness. Put long documents first and instructions after them; Anthropic reports that a question placed at the end improved response quality by up to 30 percent in its tests, especially with several documents. Label each document with its source. And ask the model to pull out the relevant quotes before it does the task. Here, that means each document carries its **name, owner and date**, and the intake prompt extracts quoted evidence per dimension before summarizing anything. The date matters most: a 2025 strategy deck and a 2026 pricing proposal can each be accurate about a different moment.

The intake produces a **gap list**, split three ways:

- **Facts found**, each with a quote and a source, for you to confirm.
- **Facts missing**, each with the likely owner and the system that probably holds it.
- **Decisions missing**, each phrased as a question for a grilling session.

Chapter 00's inventory prompt sorts documents into dimensions and marks them current, stale or contradicted. The intake prompt in this chapter goes one step further: it turns that inventory into the agenda for every grilling session that follows.

:::warn Confidential material
Reference materials for a Product 360 almost always include customer data, unreleased financials or confidential strategy. Use only a harness and connectors your company has approved for that data, and check before you connect. The prompts in this chapter assume that check has happened.
:::

### The build order

Chapter 00 lists twelve spine artifacts and says to build them in roughly that order. Chapter 31 adds four for AI-powered products. Event artifacts come when the calendar demands them. The table below turns that into a 90-day schedule. It's the dependency default; your gap list's business risk decides the actual order, as it did for Beacon in Chapter 00.

| Phase | Artifact | Spine # | Dimension | Built from (chapters) | Template |
|---|---|---|---|---|---|
| Days 1 to 30 | Product 360 index | 1 | All | 00 | `product-360-index` |
| | Stakeholder map and DACI (draft) | 12 | Leadership | 28, 36 | `36-stakeholder-map`, `36-daci-decision` |
| | Decision log (opened day 1) | 10 | Operate | 00, 29 | `29-decision-log` |
| | Urgent event artifacts with fixed dates | Event | Varies | 25, 30 | `25-launch-plan`, `30-lifecycle-stage-assessment` |
| Days 31 to 60 | Problem hypothesis and personas | 2 | Customer | 01, 10 | `product-hypothesis`, `b2b-persona` |
| | Vision and strategy one-pager | 3 | Strategy | 02, 03, 14, 16, 20 | `03-strategy-one-pager` |
| | Competitive landscape | 4 | Strategy | 13, 16 | `13-competitive-landscape` |
| | Business model and unit economics | 5 | Business | 12, 13, 15 | `13-business-case`, `15-value-metric-assessment` |
| | North Star and metric tree, with dashboard | 7 | Measure | 02, 05, 17, 18 | `02-north-star-tree` |
| | OKRs | 8 | Measure | 02 | `02-okr-set` |
| | Outcome roadmap (now, next, later) | 6 | Build | 03, 06, 11 | `03-now-next-later-roadmap` |
| | Positioning and messaging | 9 | Go-to-market | 24 | `24-positioning-statement`, `24-messaging-framework` |
| | Eval plan, AI cost model, model register, AI risk assessment | AI four | Measure, Business, Lifecycle, Operate | 31, 33 | `eval-plan`, `ai-cost-model`, `model-register`, `ai-risk-assessment` |
| Days 61 to 90 | Operating cadence (formalized) | 10 | Operate | 00, 28, 29 | `operating-cadence` |
| | Lifecycle stage assessment | 11 | Lifecycle | 30 | `30-lifecycle-stage-assessment` |
| | Event artifacts: PRD, PRFAQ, launch plan, event plan, sunset plan, AI PRD addendum | Event | Varies | 04, 25, 26, 30, 31, 34 | `04-prd`, `34-pr-faq`, `25-launch-plan`, `26-event-plan`, `30-end-of-life-plan`, `ai-prd-addendum` |
| | Product 360 health review and maturity score | Review | All | 37, Appendix C | `37-health-review` |

Three details differ from Chapter 00's list. The stakeholder map moves to the front, because you need to know whom to grill. The decision log opens on day 1, though the full cadence (spine 10) waits for the third phase; the first scope dispute needs somewhere to go. And the roadmap follows the North Star and OKRs, because a roadmap you can't trace to a measure of success is a list of features.

:::leader For product leaders: running this across a portfolio
If several PMs are building 360s at once, standardize the moves, not the content: the same master grilling prompt, challenge tests and health review template for everyone, packaged as a reusable skill or saved prompt. The portfolio review can then compare dimensions across products. Chapter 28 covers how product operations can own that kit.
:::

### Keeping it alive

The 90 days end with a running cadence. Chapter 00 defined the rhythm (weekly, biweekly, monthly, quarterly, annual and per event) and two rules: every ritual produces a decision or is cancelled, and decisions get written down. Chapter 29 covers governance and business reviews in depth.

The harness lowers what maintenance costs, and the weekly review shows how. In Cedric Chin's account of Amazon's weekly business review, informed by former Amazon executive Colin Bryar, the same graphs appear every week so people learn what normal variation looks like; owners say "nothing to see here" for routine lines, explain the exceptions, or admit they don't know yet and schedule the follow-up. Chapter 18 builds that pack. This chapter's maintenance prompt has the harness draft the weekly brief from connected sources as **exceptions only**: what moved outside its normal range and the likely reason, or "unknown, owner investigating." You verify the numbers and add the judgment.

The other rhythms follow Chapter 00's artifact kinds. Living artifacts (roadmap, metrics, OKRs, competitive landscape, stakeholder map) get a **quarterly re-grill**: a short session on what changed. Durable artifacts (vision, strategy, personas, positioning, lifecycle stage) get an **annual re-grill**, or an early one when an event forces it. Each re-grill starts from the last log and asks only what's changed.

### Scoring maturity

Appendix C gives a maturity model for scoring your 360 dimension by dimension and finding the weakest one. Its shape borrows from the Capability Maturity Model that Watts Humphrey and the Software Engineering Institute at Carnegie Mellon developed from 1986, with five levels from ad hoc to continuously improving. Only the shape is borrowed; the Product 360 levels are this book's own.

You can ask the questions behind the scale of any dimension before you open Appendix C. Does an artifact exist? Does it have an owner and a review date? Is it current, with cited sources? Does a ritual make decisions from it? Is it consistent with the other artifacts and readable by the harness? Each "yes" is a step up. The day-90 health review asks these across all nine dimensions, scores them against Appendix C and picks the weakest as next quarter's focus.

## How to apply it: the 90-day plan

The plan assumes you've taken over an existing product. For a new product the order holds, but the intake is thinner and more of the gap list is decisions.

**Before day 1: set up the workspace.**

1. Create a Product 360 workspace in your harness: a project, folder or repository with standing instructions and a place for the artifacts. The instructions hold the scope paragraph (draft it now, even if it's wrong), the nine dimensions, the seven challenge tests and the no-invention rule. Use the workspace prompt and the workspace brief template; Chapter 32 covers how harnesses carry instructions across sessions.
2. Confirm which connectors and tools are approved for customer and financial data, and connect only those.

**Days 1 to 30: learn and anchor.**

3. **Scope the surface area** (Chapter 00, step 1). Send the scope paragraph to your manager and the PMs on your boundaries. Log any dispute as decision log entry 1. You now have a decision log.
4. **Run the intake.** Point the harness at your documents, ticketing, CRM, analytics and finance sources, or supply exports where connectors don't exist, each labeled with name, owner and date. Run the intake prompt, then review the gap list and correct anything misfiled before it drives the grilling. This is the first human gate.
5. **Draft the Product 360 index** (spine 1) with Chapter 00's index prompt. Mark everything you haven't verified as "unverified" and publish it to your team in week 2, half-empty and honest.
6. **Build the stakeholder map and a first DACI** (spine 12, Chapters 28 and 36). The harness can draft it from org charts, meeting invites and decision history; you correct it from conversations. It tells you whom to send file-mode questions to.
7. **Run a listening tour** alongside the intake: your manager, peers on the boundaries, engineering and design leads, sales, customer success, product marketing, finance and at least five customers across the buying group (Chapter 01). Ask each what's working, what's broken and what decision is overdue. Add the notes to the workspace, with permission and an approved tool.
8. **Grill the facts only.** Run short sessions that confirm or correct the "facts found" list, and send file-mode questionnaires to the owners of "facts missing." Hold off on strategy; you don't yet know enough to argue with your own answers.
9. **Land one early decision.** Pick the overdue decision with the clearest owner and the most evidence (often a scope boundary or an unowned metric), write a decision memo (Chapter 17), get it decided and log it. That's Watkins's early win, in the form a B2B product allows.
10. **Agree on expectations with your manager** at day 30: the gap list, the order for the next 60 days and what you will deliberately not do in the first 90.

**Days 31 to 60: decide and build the spine.**

11. **Grill dimension by dimension**, in dependency order: Customer, Strategy, Business, Measure, Build, Go-to-market, and AI for an AI-powered product. Use the master grilling prompt with the module for each dimension, live for judgment-heavy dimensions and file mode for anything a stakeholder must answer. Approve each log before you use it; this is the second human gate.
12. **Generate the artifacts** in a fresh session, one at a time, with the artifact generation prompt and the template named in the build order table. Every claim carries a source tag; anything unsourced stays as a visible gap. Record each artifact's owner and review date in the build tracker.
13. **Share drafts with the people who'll live with them** (the business model with finance, the AI risk assessment with security and legal, and so on). Treat their objections as new grilling input and log them.
14. **Run the day-60 consistency audit.** Each contradiction becomes a fix (the artifact was wrong) or a decision log entry (the conflict is real and someone must choose). This is the third human gate.

**Days 61 to 90: operate and prove.**

15. **Formalize the cadence** (spine 10). Put the weekly metrics review, monthly roadmap refresh and quarterly business review on the calendar, each with the artifacts it reviews and the decision it produces (Chapters 00 and 29). Start the weekly exception brief with the maintenance prompt and run at least four cycles before day 90.
16. **Assess the lifecycle stage** (spine 11, Chapter 30) of each offering in scope, legacy ones included. That's where inherited products hide their liabilities.
17. **Produce the event artifacts the calendar demands**: PRDs and PRFAQs (Chapters 04 and 34), launch plans (Chapter 25), event plans (Chapter 26), sunset plans (Chapter 30), AI PRD addenda (Chapter 31). Generate them from the spine. When an event artifact contradicts the spine, take the conflict to the decision log.
18. **Hold the business review on the 360.** Present from the index and spine artifacts rather than a deck built for the occasion (Chapter 35). A slide the 360 can't support marks a gap.
19. **Run the Product 360 health review**: each dimension's freshness, open grilling items and maturity score against Appendix C. Pick the weakest dimension as next quarter's focus.
20. **Run a premortem on the next quarter**, write the next 90-day plan and close this one.

:::key Three human gates
The harness does most of the mechanical work, but three approvals stay with you: the gap list before grilling, each session log before generation, and the audit before publishing. Skip one and the harness's mistakes reach artifacts other people treat as true.
:::

## The AI lens

### When the product is AI-powered

An AI-powered product needs a tenth grilling module. Chapter 00 explains why AI isn't a tenth dimension; the module exists because AI reaches into four of the nine at once, and each needs an artifact from Chapter 31.

- **Measure: the eval plan.** What does "good" mean for this AI feature, who decided, what are the current scores and what score stops a release? A PM who can't answer doesn't yet know whether the product works.
- **Business: the AI cost model.** What does one task or one resolved outcome cost in inference, and which way is it trending? AI features can quietly change unit economics, as Beacon's gross margin shows.
- **Lifecycle: the model and vendor register.** Which models and versions are in use, with which deprecation dates? A model retirement is a lifecycle event your customers will feel even if you change nothing.
- **Operate: the AI risk assessment.** What are the failure modes, guardrails and regulatory duties (Chapter 33)? The question that matters most: what's the worst thing this product has already done, and what changed afterward?

The premortem works especially well here. "It's 90 days from now and the agent caused an incident at a customer. What happened?" produces eval cases, guardrails and risk entries in one pass, and often exposes the gap between what the positioning promises and what the risk assessment allows.

### Doing the work with AI

Most of this chapter is about doing the work with AI. Five rules keep it honest.

**The harness asks; you decide.** If the harness starts answering its own questions with confident judgments, stop and restate the rule. If you catch yourself accepting every recommendation without reading the reasoning, slow down: an untouched recommendation is still your decision, logged under your name.

**Split sessions and write things down.** Each grilling session covers one dimension and ends in a written log. Generation happens in a fresh session that reads the approved log and the cited sources: the interview, write, then build pattern Anthropic recommends for coding work.

**Make the audit a separate pass.** Shehzaad Dhuliawala and colleagues at Meta AI showed in 2023 that a model hallucinates less when it drafts an answer, plans questions to verify its own claims, answers them independently so the draft doesn't bias them, and then revises. They called it Chain-of-Verification. The consistency audit prompt follows that shape, and Chapter 19's verification checklist covers the numbers in more depth.

**Package what you repeat.** You'll run the master grilling prompt and the maintenance prompt dozens of times. Save them where your harness keeps reusable instructions: a skill, a saved prompt or a project's standing instructions. Anthropic's Agent Skills, introduced in October 2025, and similar features elsewhere load packaged instructions only when relevant (Chapter 32). Packaging also lets a portfolio leader give every PM the same session.

**Keep the 360 machine-readable.** After day 90, the maintenance prompts read the index and only the artifacts due for review. That works only if the index is current and the artifacts are documents the harness can open (Chapter 00).

:::ai What the harness shouldn't touch
The harness drafts the gap list, the questions, the artifacts and the briefs. It doesn't approve any of them, it doesn't appear as the decider in the decision log, and it doesn't send anything to a stakeholder on your behalf without you reading it first.
:::

## The Beacon case: the first 90 days

:::example Picking up where Chapter 00 left off
Chapter 00 covered your first two weeks as Principal PM for Beacon: the scope paragraph, the 140-document inventory, the Northlight Observe boundary dispute logged as decision 1, and a first QBR showing an index with twelve linked artifacts (four new, five repaired, three "stale, owner assigned") and six decision log entries. Linked isn't the same as decided. This is how the twelve became true by the next business review, near day 90.
:::

**Days 1 to 30: intake and the first grilling.** You connect the harness to the documentation wiki, the roadmap in the ticketing system, the CRM, the analytics platform and an FP&A model export, all on tools approved for Northlight's confidential data, and run the intake. The facts-missing column includes the current autonomous resolution rate by segment and inference cost per resolved incident, which nobody owns yet (Chapter 18 later gives it owners in finance and product). The decisions-missing column has four items: the North Star definition, the pricing metric, the Observe boundary and the end-of-life date for Beacon Classic.

The first live session is Business, because gross margin is the most visible problem. The harness opens with a fact, cited from the FP&A export: gross margin fell from 81% to 72% after the agentic features launched, because of inference cost. Its first decision question: what gross margin must Beacon Agents reach for a per-resolved-incident price to be viable? The recommendation comes with reasoning from the export and a note that the strategy deck still assumes 80%.

You answer "back to 80%." The harness challenges on two tests. *Evidenced:* 81% was the pre-agent level; what inference cost per incident does 80% imply, and is there evidence it's reachable? *Owned:* who is accountable for the cost side? You don't know the cost figure and say so. The item is logged as open, owner the applied AI lead, with your note: "80% is a target to test, not a commitment." The premortem produces the line that shapes the next two months: *the new price launches at Northlight Live and margin falls further.*

Meanwhile you draft the stakeholder map: Priya, Dana, Marcus, Sam and Leo outside; your manager (the VP of Product for the Operations portfolio), the Observe and Desk group PMs, the product marketing manager, product ops and finance inside. The first DACI covers the Observe boundary, with your manager as approver.

That boundary becomes your early win. The listening tour shows that both teams want a clean story for customers who run both products; the disagreement is about who owns the correlation roadmap. Your memo proposes, and your manager approves, that Beacon keeps its Correlate team and owns diagnosis and action, while correlation of Observe-native alerts becomes a shared capability with a joint quarterly roadmap review. Decision 1 closes in week 4, consistent with the guiding policy you'll write in Chapter 03: Observe data as an accelerant, not a requirement.

**Days 31 to 60: grilling the spine.** The Customer session runs alongside the discovery work in Chapter 01. When you answer "SRE teams" to the question of who the customer is, the harness challenges on *Specific*: SRE teams use Beacon, but who signs, who blocks and who resells? Marcus, Sam and Leo enter the persona set, and Sam's job story comes from Chapter 01's interviews.

The Measure session starts from the North Star: incidents resolved with Beacon's help per week. The harness accepts the metric and challenges the phrase "with Beacon's help." An accepted diagnosis, an approved action or both? If per-resolved-incident pricing goes ahead, this definition becomes the price meter. You log it as open with a two-week deadline; the definition you later agree with finance and product marketing is the one in Chapter 18. The session also names diagnosis acceptance rate and autonomous resolution rate as inputs to the metric tree (Chapter 02).

The AI session anchors its premortem in a real event: the design-partner pilot in which a responder accepted a hallucinated root cause and rolled back the wrong service (Chapter 31). The eval plan, the guardrails and the AI risk assessment all take cases from it. Sam's requirements become audit-log and least-privilege items in the risk assessment, and the EU customers' requests for AI Act documentation go into its regulatory section (Chapter 33).

You generate the artifacts one at a time in fresh sessions. The day-60 consistency audit then finds two contradictions that no single artifact would have revealed. First, the positioning draft promises "autonomous remediation," while the AI risk assessment allows autonomy only for low-risk actions on a customer's allowlist. Second, the roadmap still carries a feature investment in Beacon Classic, while the draft lifecycle assessment puts Classic in decline. Both become decision log entries. The positioning changes to "supervised remediation" (Chapter 24). The Classic feature is cut, and its team moves to migration tooling (Chapter 30).

**Days 61 to 90: running it.** The cadence goes on the calendar. The weekly exception brief covers the North Star, MTTR, diagnosis acceptance rate, autonomous resolution rate, weekly active responders and inference cost per resolved incident. The maintenance prompt drafts it from the connected sources each Monday, and you check every number before it's shared. In one of the first four cycles, the brief flags diagnosis acceptance sliding while weekly active responders rise; Chapter 19 tells how the team traced it to the mix of accounts migrated from Classic rather than to agent quality. The brief surfaced the exception and named an owner the same week.

The event artifacts arrive on time because the spine already holds their inputs: the Beacon Agents launch and event plans for Northlight Live (Chapters 25 and 26) draw on positioning, personas and the risk assessment, and the Classic sunset plan (Chapter 30) on the lifecycle assessment.

At day 90 you run the health review. Measure and Business come out strongest: both have owners, are current and feed a ritual that decides from them. Leadership has a map and a DACI but no ritual that uses them yet. Lifecycle is weakest: Classic has an assessment and a sunset plan, but nobody has assessed Correlate and Diagnose as offerings in their own right. Scored against Appendix C, Lifecycle sits at the bottom, so it becomes next quarter's focus, with a re-grill in week 2.

The 360 still isn't complete. Three artifacts are marked "current, owner assigned, re-grill due." But every artifact traces to a log entry or a source, every contradiction the audit found is fixed or in the decision log, and anyone who asks what Beacon's North Star is gets the same answer from you, from the index and from the harness.

## Product 360 artifacts

Five artifacts carry the 90 days. The 30/60/90 plan sets the commitments, the build tracker shows progress, the grilling session log holds the decisions, the health review scores the result, and the workspace brief gives the harness its standing instructions. The spine artifacts themselves use the templates from the chapters named in the build order table.

```template id="37-30-60-90-plan" title="30/60/90 plan for a Product 360"
# 30/60/90 plan · [Product surface area] · Start date [date]

**PM:** [name]   **Manager:** [name]   **Reviewers:** [peers, engineering lead, design lead]
**Last updated:** [date]   **Status:** Draft / Agreed with manager / In progress / Closed

## Scope paragraph
[One paragraph: products, customers, teams, revenue. Note any boundary disputes and their decision log IDs.]

## Expectations agreed with my manager
- What success looks like at day 90:
- Decisions my manager expects me to bring:
- How and how often we'll review progress:

## Days 1 to 30: learn and anchor
**Goals:**
-
**Artifacts to deliver:** Product 360 index (spine 1), stakeholder map and DACI draft (spine 12), decision log opened, gap list, urgent event artifacts: [list]
**Grilling sessions:** facts only. [Dimensions and dates]
**File-mode questionnaires sent to:** [owner: dimension]
**Listening tour:** [names and roles, including at least five customers across the buying group]
**Early decision to land:** [decision, decider, date]
**Exit criteria:** gap list approved; index published; stakeholder map reviewed by manager; one decision logged
**Risks:**

## Days 31 to 60: decide and build the spine
**Goals:**
-
**Grilling sessions (dependency order):**
| Dimension | Mode (live / file) | Date | Participants | Log ID |
|---|---|---|---|---|
| Customer | | | | |
| Strategy | | | | |
| Business | | | | |
| Measure | | | | |
| Build | | | | |
| Go-to-market | | | | |
| AI (if AI-powered) | | | | |

**Artifacts to deliver:** spine 2 to 9; AI four if applicable: [list]
**Stakeholder reviews:** [artifact: reviewer]
**Consistency audit date:** [day 60]
**Exit criteria:** spine 2 to 9 drafted from approved logs; audit run; every contradiction fixed or logged
**Risks:**

## Days 61 to 90: operate and prove
**Goals:**
-
**Cadence started:** weekly exception brief from [date]; monthly roadmap refresh on [date]; QBR on [date]
**Artifacts to deliver:** operating cadence (spine 10), lifecycle stage assessment (spine 11), event artifacts: [list with dates]
**Health review date:** [date]
**Exit criteria:** four weekly cycles run; QBR held from the 360; health review scored against Appendix C; next quarter's focus dimension chosen
**Risks:**

## What I will not do in the first 90 days
-
-

## Day-90 close
**Premortem for next quarter:**
**Weakest dimension and next quarter's focus:**
**Open grilling items carried forward:** [count and IDs]
```

```template id="37-build-tracker" title="Product 360 build tracker"
# Product 360 build tracker · [Product] · Updated [date]

**Owner:** [PM]   **Index:** [link]
Status values: Not started / Grilling / Drafted / Audited / Published / Re-grill due

## Spine
| # | Artifact | Dimension | Kind | Template | Source materials | Grilling log ID | Owner | Status | Last reviewed | Next review | Open items |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Product 360 index | All | Living | product-360-index | | | | | | | |
| 2 | Problem hypothesis and personas | Customer | Durable | product-hypothesis, b2b-persona | | | | | | | |
| 3 | Vision and strategy one-pager | Strategy | Durable | 03-strategy-one-pager | | | | | | | |
| 4 | Competitive landscape | Strategy | Living, quarterly | 13-competitive-landscape | | | | | | | |
| 5 | Business model and unit economics | Business | Living, quarterly | 13-business-case | | | | | | | |
| 6 | Outcome roadmap | Build | Living, monthly | 03-now-next-later-roadmap | | | | | | | |
| 7 | North Star and metric tree, dashboard | Measure | Living, weekly | 02-north-star-tree | | | | | | | |
| 8 | OKRs | Measure | Living, quarterly | 02-okr-set | | | | | | | |
| 9 | Positioning and messaging | Go-to-market | Durable | 24-positioning-statement, 24-messaging-framework | | | | | | | |
| 10 | Operating cadence and decision log | Operate | Living, weekly | operating-cadence, 29-decision-log | | | | | | | |
| 11 | Lifecycle stage assessment | Lifecycle | Durable, yearly | 30-lifecycle-stage-assessment | | | | | | | |
| 12 | Stakeholder map and DACI | Leadership | Living, quarterly | 36-stakeholder-map, 36-daci-decision | | | | | | | |

## AI artifacts (AI-powered products)
| Artifact | Dimension | Template | Grilling log ID | Owner | Status | Last reviewed | Next review | Open items |
|---|---|---|---|---|---|---|---|---|
| Eval plan | Measure | eval-plan | | | | | | |
| AI cost model | Business | ai-cost-model | | | | | | |
| Model and vendor register | Lifecycle | model-register | | | | | | |
| AI risk assessment | Operate | ai-risk-assessment | | | | | | |

## Active event artifacts
| Artifact | Event and date | Template | Spine artifacts it draws on | Owner | Status | Archive date |
|---|---|---|---|---|---|---|
| | | | | | | |

## Summary
- Spine artifacts published: [n] of 12
- Open grilling items: [n]   Contradictions open from last audit: [n]
- Overdue reviews: [list]
```

```template id="37-grilling-session-log" title="Grilling session log"
# Grilling session log · [Product] · [Dimension] · [Session ID] · [Date]

**Mode:** Live / File   **Participants:** [PM, stakeholders]   **Harness:** [tool, approved for this data: Y/N]
**Reference materials loaded:**
| Source | Owner | Date of source | How loaded (connector / export / pasted) |
|---|---|---|---|
| | | | |

**Prior logs read:** [session IDs]

## Questions
| Q-ID | Question | Kind (fact / decision) | Harness recommendation and reason | Answer | Evidence (source or "assumption") | Challenge raised (test) | Status | Owner | Feeds artifact |
|---|---|---|---|---|---|---|---|---|---|
| [DIM]-01 | | | | | | | Agreed / Overridden / Open / Needs owner | | |
| [DIM]-02 | | | | | | | | | |

Status rules: Agreed means the answer passed all seven tests. Overridden means the PM kept an answer that failed a test, with the reason recorded below. Open means no answer yet. Needs owner means someone else holds the answer.

## Overrides
| Q-ID | Test failed | PM's reason for keeping the answer |
|---|---|---|
| | | |

## Premortem
"It's 90 days from now and this dimension's artifact misled a decision. What happened?"
- Answer:
- Changes made because of it:

## Readback
[Five to ten lines: what was decided in this session.]
**Readback confirmed by PM:** Y / N   **Date:**

## Next
- Follow-ups and owners:
- Next session:
```

```template id="37-health-review" title="Product 360 health review"
# Product 360 health review · [Product] · [Quarter] · [Date]

**Reviewer:** [PM]   **Attendees:** [manager, peers, product ops]
**Maturity scale:** Appendix C   **Previous review:** [link]

## By dimension
| Dimension | Artifacts | Owner | Last reviewed | Freshness (current / stale / contradicted) | Used in a ritual? (which) | Maturity (Appendix C) | Open grilling items | Audit contradictions open | Decision needed |
|---|---|---|---|---|---|---|---|---|---|
| Customer | | | | | | | | | |
| Strategy | | | | | | | | | |
| Business | | | | | | | | | |
| Build | | | | | | | | | |
| Measure | | | | | | | | | |
| Go-to-market | | | | | | | | | |
| Operate | | | | | | | | | |
| Lifecycle | | | | | | | | | |
| Leadership | | | | | | | | | |

## AI artifacts (AI-powered products)
- Eval scores: current, trend, last release gated by evals:
- Cost per task or outcome: current, trend:
- Model deprecations due in the next two quarters:
- AI risk assessment: last reviewed, new regulatory duties:

## Cadence health
| Ritual | Held as planned (n of n) | Decisions produced | Keep / change / cancel |
|---|---|---|---|
| Weekly metrics review | | | |
| Monthly roadmap refresh | | | |
| Quarterly business review | | | |

## Summary
- Weakest dimension:
- Top three fixes (owner, date):
  1.
  2.
  3.
- Re-grills scheduled: [dimension, date]
- What changed since the last review:
```

```template id="37-workspace-brief" title="Product 360 workspace brief"
# Product 360 workspace brief · [Product]

Standing instructions for the AI harness. Keep this short and current; it loads with every session.

## Scope
[The scope paragraph, with the date it was last confirmed.]

## Where the 360 lives
- Index: [location]
- Grilling logs: [location]
- Decision log: [location]
- Approved connectors: [list, with what each may be used for]
- Not approved for this workspace: [systems or data types]

## Rules
1. Never invent facts, numbers, quotes or decisions. If a source doesn't support it, say "no source" and add it to the gap list.
2. Fetch facts from connected sources and cite them (source, owner, date). Ask the PM only for decisions.
3. Ask one question at a time, with a recommended answer and the reason.
4. Test every answer against the seven challenge tests: specific, evidenced, falsifiable, trade-off named, consistent, owned, decision-relevant. Push once on a failure, then log it as open or overridden.
5. Don't agree to be agreeable. If the evidence points elsewhere, say so.
6. Write every session to a grilling log before ending it.
7. The decision log names a person as the decider, never the harness.

## Vocabulary
- Nine dimensions: Customer, Strategy, Business, Build, Measure, Go-to-market, Operate, Lifecycle, Leadership.
- Artifact kinds: durable, living, event.
- Product terms and metric definitions: [link to metric dictionary]

## Current state
- Phase: [days 1 to 30 / 31 to 60 / 61 to 90 / maintaining]
- Open grilling items: [n, link]
- Next review due: [artifact, date]
```

## Prompts

These eight prompts form a chain: set up the workspace, run the intake, grill with the master prompt plus a dimension module, generate the artifacts, audit them, maintain them and review their health. They work in any capable harness. Every one of them can touch customer data, unreleased financials or confidential strategy, so run them only in a harness and with connectors your company has approved for that data. Chapter 00's prompts (inventory, index, cadence and contradiction check) and Chapter 32's context-pack prompt complement this set.

```prompt title="Set up the Product 360 workspace"
Goal: Give the harness standing instructions so every later session follows the same rules.
Paste in: your scope paragraph, the list of approved connectors and data types, where the index and logs will live, and any existing metric dictionary. Use only a harness approved for your company's confidential data.

You're helping me build and maintain a Product 360 for [product surface area]. Draft a workspace brief that will load with every session in this workspace. Use the structure below and keep it under 600 words.

1. Scope: restate my scope paragraph. List any boundary that looks disputed or vague, as a question for me.
2. Where things live: the index, grilling logs, decision log and approved connectors, with what each connector may be used for. List anything I've said is not approved.
3. Rules for you, in this order:
   - Never invent facts, numbers, quotes or decisions. If no source supports something, say "no source" and add it to the gap list.
   - Fetch facts from connected sources and cite source, owner and date. Ask me only for decisions, priorities and trade-offs.
   - Ask one question at a time, each with your recommended answer and the reason.
   - Test every answer I give against seven tests: specific, evidenced, falsifiable, trade-off named, consistent, owned, decision-relevant. On a failure, name the test and push once. On a second failure, log the item as open or overridden with my reason.
   - Don't agree with me to be agreeable. If the evidence points elsewhere, say so plainly.
   - Write every session to a grilling log before it ends.
   - The decision log always names a person as decider, never you.
4. Vocabulary: the nine dimensions (Customer, Strategy, Business, Build, Measure, Go-to-market, Operate, Lifecycle, Leadership) and three artifact kinds (durable, living, event).
5. Current state: phase, open items, next review due.

Then ask me up to three questions about anything in the brief you couldn't fill from what I gave you.

[scope paragraph, connectors, locations, metric dictionary]

Check the output: read the rules section aloud. If any rule lets the harness answer a decision question on its own, or accept an answer without testing it, rewrite that rule before saving the brief.
```

```prompt title="Run the intake and produce a gap list"
Goal: Turn the documents and data you inherited into an evidence map and the agenda for every grilling session.
Paste in (or connect): strategy decks, PRDs, pricing pages, QBR and board decks, roadmap exports, dashboard exports, finance model exports, win/loss and support escalation summaries, your listening tour notes. Label each item with its name, owner and date. Put the documents first and this prompt after them. Use only approved tools; remove personal identifiers from customer material.

[documents, each labeled: name | owner | date]

You're running the intake for the Product 360 of [product]. Work in four passes and show each one.

Pass 1, evidence. For each of the nine dimensions, quote the passages from the documents that state a fact about the product (numbers, dates, owners, definitions, commitments, decisions already made). Give each quote its source name and date. Don't summarize yet.

Pass 2, conflicts and staleness. List every place where two sources disagree, or where a source is older than a later event it doesn't reflect. For each, give both quotes and dates.

Pass 3, the gap list. Produce one table per dimension with three sections:
- Facts found: the fact, the quote, the source, the date, and "confirm with [owner]".
- Facts missing: what's missing, the likely owner and the system that probably holds it.
- Decisions missing: phrased as a question I must answer, with why it matters in the next quarter.

Pass 4, the agenda. Propose the order of grilling sessions, starting with the dimension carrying the most business risk, and say why. Mark which sessions should be live and which should go to a stakeholder as a written questionnaire, and to whom.

Rules: every fact in Pass 3 must trace to a Pass 1 quote. If you're inferring rather than quoting, label it "inference." Never fill a gap with a plausible guess.

Check the output: pick five facts at random and open their sources. If any quote is wrong or any "fact" came from inference, rerun Pass 3 with a stricter instruction. Then move anything misfiled between facts and decisions before you approve the list.
```

```prompt title="Master grilling session"
Goal: Draw out the decisions behind one dimension of your Product 360, one question at a time, with the harness challenging weak answers and writing everything down.
Paste in: the workspace brief, the approved gap list for this dimension, earlier grilling logs that this dimension depends on, the dimension module from the next prompt, and any reference materials not already connected. Use only approved tools.

You're going to grill me about the [dimension] dimension of the Product 360 for [product]. The goal is a grilling log complete enough that a fresh session could generate the [artifact names] from it without asking me anything else. Stop when every question in the module and every decision-missing item in the gap list is agreed, overridden or open with an owner, or when I say stop.

How to run the session:
1. Before asking anything, list the facts you'll rely on from the gap list and connected sources, with citations, and ask me to confirm or correct them in one reply.
2. Then walk the decisions in dependency order: settle the questions other answers depend on first. Ask exactly one question per turn.
3. With each question, give your recommended answer and the reasoning, citing evidence where it exists. If the evidence is thin, say so and recommend anyway.
4. Never ask me for a fact a connected source can answer. Look it up, cite it and ask me to confirm.
5. Test each of my answers against the seven tests: specific, evidenced, falsifiable, trade-off named, consistent (with my earlier answers and existing artifacts), owned, decision-relevant. If an answer fails, name the test and explain the gap in two sentences, then ask again. If my second answer still fails, log it as "overridden" with my reason, or "open" with an owner, and move on. Don't argue a third time.
6. Don't agree with me to be agreeable. If I contradict the evidence or an earlier answer, say so before moving on.
7. If I say "I don't know," ask who would know, log it as "needs owner" and continue.
8. Every five questions, show a two-line running summary so I can correct drift.
9. When the questions are done, run a premortem: "It's 90 days from now and this dimension's artifact misled a decision. What happened?" Ask me for my answer, then add the two failure stories you think are most likely, and ask what we should change.
10. Finish with a readback of everything decided, ask me to confirm it, and then write the grilling log with these columns: Q-ID, question, kind (fact or decision), your recommendation and reason, my answer, evidence, challenge raised, status (agreed, overridden, open, needs owner), owner, feeds artifact. Add the overrides table, the premortem and the readback.

File mode: if I say "file mode," don't ask live. Instead write every question for this dimension into a questionnaire, each with your recommended answer, the reason and a blank "Your answer" line, addressed to [stakeholder]. When I paste back the edited file, treat untouched recommendations as accepted, test every edited answer against the seven tests, ask follow-ups only for failures (one at a time), and then write the log.

Start with step 1.

Check the output: before you approve the log, scan the status column. If every item is "agreed," the harness probably went easy on you; rerun the challenge step on your three most important answers. Make sure no "agreed" answer is a fact that nobody actually confirmed.
```

```prompt title="Grilling modules for each dimension"
Goal: Give the master grilling session the right seed questions, chapters and challenges for each dimension.
Paste in: the master grilling session prompt, followed by the one module below for the dimension you're grilling. The harness extends the seed questions from the gap list, so treat the seeds as a minimum. The Business, Customer and AI modules draw on finance, customer and incident data; use only approved tools.

Module: Customer (Chapters 01, 10). Produces: problem hypothesis, personas, job stories.
Seeds: Who is the user, the champion, the economic buyer, the technical evaluator and the gatekeeper? What job are they hiring the product for, and what's the current alternative, including doing nothing? Which persona would we disappoint to serve another? What did the last ten customer conversations say, with sources? What evidence would kill the problem hypothesis?
Extra challenge: reject "customers" or "users" without a named role and segment.

Module: Strategy (Chapters 02, 03, 13, 14, 16, 20 to 23). Produces: vision and strategy one-pager, competitive landscape.
Seeds: What's the diagnosis in one sentence? Where do we play, and where do we refuse to play? How do we win, and what would a competitor have to do to beat us? Product or platform? What's the moat, and how fast is it eroding? How is the innovation portfolio balanced across horizons?
Extra challenge: every strategic choice must name what we give up.

Module: Business (Chapters 12, 13, 15). Produces: business model and unit economics summary.
Seeds: How do we make money, by segment and channel? What are the unit economics and the margin trend? What's the pricing metric and how does it track customer value? What would make the business case false? What does finance believe that the product team doesn't?
Extra challenge: every number must cite the finance source and date.

Module: Build (Chapters 03, 04, 06, 07, 11). Produces: outcome roadmap, backlog policy.
Seeds: What's in now, next and later, and which outcome does each item serve? What did we stop doing, and who was told? Which delivery model fits each team? Which technical debt is a product bet? Which dependencies on other teams could break the plan?
Extra challenge: any roadmap item that doesn't trace to an outcome or a strategy choice is flagged.

Module: Measure (Chapters 02, 05, 08, 09, 17, 18, 19). Produces: North Star and metric tree, OKRs, dashboard spec.
Seeds: What's the North Star and why does it reflect customer value rather than usage? Which input metrics can teams move? What decision does each metric inform? Where are the definitions disputed or the data untrusted? Which OKRs are outcomes rather than outputs?
Extra challenge: every metric needs an exact definition, an owner and the decision it informs.

Module: Go-to-market (Chapters 24 to 27). Produces: positioning and messaging, launch tiers, enablement plan.
Seeds: What's the positioning statement, category and proof? What's in the next launch and at which tier? What do sales and customer success need that they don't have? How does field feedback reach the roadmap, and how fast?
Extra challenge: every claim in positioning must be supported by the product's current capability and risk assessment.

Module: Operate (Chapters 28, 29). Produces: operating cadence, decision log, risk register.
Seeds: Which rituals exist, and what decision does each produce? Who holds decision rights for pricing, roadmap, launches and sunsets? What's on the risk register, with owners? Which ritual should be cancelled?
Extra challenge: a ritual with no decision output is proposed for cancellation.

Module: Lifecycle (Chapter 30). Produces: lifecycle stage assessment, sunset candidates.
Seeds: What stage is each offering in, with evidence? Which offerings or features are sunset candidates? What migration obligations, contracts or notice periods apply? What would it cost to keep a declining offering another year?
Extra challenge: no offering is "growth" without trend evidence.

Module: Leadership (Chapters 34, 35, 36). Produces: stakeholder map and DACI, communication plan.
Seeds: Who can say no to the top three decisions this quarter? What's the DACI for each? Which stakeholder relationship is weakest, and why? What does each audience need to hear, how often and in what format?
Extra challenge: every DACI names one approver.

Module: AI (Chapters 31, 32, 33). Produces: eval plan, AI cost model, model and vendor register, AI risk assessment.
Seeds: What does "good" mean for each AI feature, who decided, and what are the current eval scores? What score blocks a release? What does one task or outcome cost in inference, and what's the trend? Which models and versions are in use, with deprecation dates? What's the worst thing the product has done, and what changed afterward? Which regulatory duties apply in which markets? How does the team itself use the harness, and with which data?
Extra challenge: run the premortem as "the AI caused an incident at a customer."

Check the output: after the session, compare the log against the module's "Produces" line. Every listed artifact should have enough agreed or overridden answers to fill its template; if one doesn't, schedule a short follow-up session rather than letting generation fill the gap.
```

```prompt title="Generate a Product 360 artifact from grilling logs"
Goal: Turn approved grilling answers and evidence into one of the book's templates, without adding anything that wasn't decided or sourced.
Paste in: in a fresh session, the workspace brief, the approved grilling log(s) for this artifact, the cited source documents and the empty template from this book (for example, the strategy one-pager from Chapter 03). Use only approved tools.

[grilling logs]
[source documents, each labeled: name | owner | date]
[template]

Fill in the [template name] for [product] using only the grilling logs and sources above.

Rules:
1. Every sentence or table cell that states a fact, number or decision ends with a source tag: the log Q-ID (for example [STR-07]) or the document name and date.
2. Use "overridden" answers as written, and add the override note in a comment so readers know a challenge was raised.
3. Where the template asks for something the logs and sources don't cover, write "GAP: [what's missing] (owner: [name or unknown])." Don't fill it.
4. Don't add facts, examples, competitors, numbers or quotes that aren't in the material.
5. Keep the template's headings and order. Write in plain language, short sentences.

After the artifact, list: (a) every GAP, (b) every place where two log answers seemed to conflict and how you handled it, (c) any open item from the log that this artifact depends on.

Check the output: pick five source tags and confirm each one supports the sentence it's attached to. Search for any sentence without a tag. Either it's connective text or it was invented; delete the second kind.
```

```prompt title="Audit the Product 360 for consistency"
Goal: Find contradictions, unsourced numbers and stale content across the whole 360 before anyone else does.
Paste in: the Product 360 index and every spine and AI artifact (or connect the harness to where they live), plus the decision log. Use only approved tools.

Audit the Product 360 for [product]. Work in separate passes and don't let an earlier pass change a later one's answers.

Pass 1, claims. List every factual claim and number in the artifacts, with the artifact and section it appears in.

Pass 2, verification questions. For each claim, write the question that would verify it ("What is the gross margin in the latest finance export?"). Then answer each question independently from the cited source alone, without looking at the artifact's wording. Mark each claim verified, unsourced, contradicted by its source, or stale (the source is older than a later event).

Pass 3, cross-artifact contradictions. Check these pairs at minimum: positioning against the AI risk assessment and current capability; roadmap against strategy one-pager and lifecycle assessment; OKRs against the North Star tree; business model against pricing and the AI cost model; personas against positioning and the stakeholder map; the decision log against every artifact a decision touched. Quote both sides of each contradiction.

Pass 4, coverage. Which spine artifacts are missing, have no owner, or are past their review date?

Output a table: issue, artifacts affected, quotes, type (unsourced, contradicted, stale, missing, cross-artifact), severity (blocks a decision this quarter / should fix / cosmetic), and a proposed resolution: "fix the artifact" if the source is clear, or "decision needed: [question], decider: [name]" if the conflict is real.

Check the output: every "decision needed" row goes into the decision log with a decider and a date. Spot-check three "verified" claims yourself; if any fails, rerun Pass 2 for that artifact.
```

```prompt title="Maintain the Product 360 on its cadence"
Goal: Keep the 360 true with the least effort: an exception-only weekly brief, a monthly roadmap check and scheduled re-grills.
Paste in: the workspace brief and the Product 360 index; the harness loads only the artifacts due for the chosen mode. Name the mode. Use only approved tools.

Mode: [weekly / monthly / quarterly / annual / event]

Weekly: From the connected metric sources, draft an exception brief for [product]'s weekly review. Use the same metrics in the same order every week: [list from the North Star tree]. For each, say "nothing to see here" if it moved within its normal range over the last eight weeks, or, if it didn't, give the size of the move, the likely reason with evidence, or "unknown, owner [name] investigating." Add new risks, decisions logged this week and any artifact whose review date passed. Keep it to one page.

Monthly: Compare the roadmap against the strategy one-pager, the OKRs and last month's decisions. List items that no longer trace to an outcome, items that changed without a decision log entry, and competitive or customer changes from the month that should affect the roadmap.

Quarterly: Load the living artifacts (roadmap, metric tree, OKRs, competitive landscape, business model, stakeholder map) and their last grilling logs. Run a short grilling session: for each artifact, ask what changed since the last log, with your recommended update and evidence, one question at a time, using the seven tests. Write a new log that references the previous one.

Annual: Do the same for the durable artifacts (vision and strategy, personas, positioning, lifecycle stage), and add one question per artifact: "If we were writing this from scratch today, would we write the same thing?"

Event: For [launch / sunset / pricing change / reorganization / incident], list every spine artifact the event affects and the questions each now needs answered, then start a grilling session on the first one.

Rules: verify every number against its source and show the source. Don't restate unchanged content. Don't propose decisions; frame them as questions with a recommended answer.

Check the output: check every number in the weekly brief against the dashboard before you share it. If the brief runs past one page, it's a recap, not an exception brief; cut it back.
```

```prompt title="Draft the Product 360 health review"
Goal: Score the 360 dimension by dimension against Appendix C and pick next quarter's focus.
Paste in: the Product 360 index, the build tracker, the latest consistency audit, the grilling logs' open items, the decision log and calendar evidence of which rituals were held, and the Appendix C maturity model. Use only approved tools.

Draft a Product 360 health review for [product] for [quarter], using the health review template.

For each of the nine dimensions (and the AI artifacts if applicable):
1. List the artifacts, owners and last-reviewed dates from the tracker.
2. Mark freshness: current, stale or contradicted, citing the audit.
3. Name the ritual that made a decision from this dimension's artifacts this quarter, citing the decision log. If none, say "not used."
4. Score maturity against Appendix C, quoting the level description you matched and the evidence for it. If evidence is mixed, give the lower level and say why.
5. Count open grilling items and open audit contradictions.

Then: cadence health (rituals held against planned, decisions produced, which to keep, change or cancel); AI artifact health (eval trend, cost trend, deprecations due); the weakest dimension with your reasoning; and three fixes, each with a suggested owner and date.

Finally, ask me three grilling questions, one at a time with recommended answers, to confirm the weakest dimension and the fixes before you finalize the review.

Check the output: challenge any score above the level the evidence supports; generous scores defeat the purpose. Make sure the weakest dimension is chosen by evidence, not by which one is most comfortable to fix.
```

## Anti-patterns

:::warn The marathon session
One conversation tries to grill all nine dimensions in an afternoon. By the third hour the harness has lost early answers and the PM is accepting recommendations to get it over with. Grill one dimension per session and write the log before you stop.
:::

:::warn The agreeable harness
Every answer is marked "agreed," every recommendation was accepted, and the artifacts read beautifully. Nothing was tested. Give the harness explicit challenge tests, tell it not to agree for its own sake, and treat a log with no challenges as a log to rerun.
:::

:::warn Asking the PM for facts
The harness asks you for ARR, launch dates and ticket counts, and you answer from memory. Some of those answers are wrong, and they're now in durable artifacts with your name on them. Facts come from connected sources, with citations; you confirm them. You answer decisions.
:::

:::warn Generating before deciding
Skipping the grilling and asking the harness to "write our strategy from these docs." The result blends real facts, invented ones and decisions nobody made, and it's fluent enough that nobody notices. Grill first; generate from the approved log.
:::

:::warn Template theater at speed
With a harness you can fill every spine and AI template in a day, and get a complete-looking 360 that nobody has decided, owned or reviewed. Now that drafting costs almost nothing, Chapter 00's warning matters more: an artifact counts only when its decisions are logged and its owner has a review date.
:::

:::warn Feature wins in the first 90 days
A new Principal PM tries to prove themselves by shipping something in the first quarter. In an enterprise release cycle, what ships was mostly decided before they arrived. Aim the early win at a decision unblocked and recorded.
:::

:::warn The 360 that stops at day 90
The build was a project with a finish line, and the cadence never started. Three months later the artifacts are as stale as the ones you inherited. The 90 days end with rituals on the calendar and re-grills scheduled, not with a published folder.
:::

## Checklist

- [ ] A workspace brief with scope, approved connectors (approved for confidential and customer data), the no-invention rule and the seven challenge tests loads with every session.
- [ ] The decision log was opened in the first week, with any scope dispute as an entry.
- [ ] The intake produced a gap list that separates facts found, facts missing and decisions missing, with a source and date for every fact, and you approved it before grilling.
- [ ] The stakeholder map and a first DACI exist before the decision-heavy grilling sessions start.
- [ ] One early decision has been landed, written as a memo and logged.
- [ ] Each dimension has a grilling session log with recommendations, answers, challenges, statuses, a premortem and a confirmed readback.
- [ ] Every spine artifact (and the four AI artifacts, for an AI-powered product) was generated from an approved log, with source tags on every claim and gaps left visible.
- [ ] The day-60 consistency audit has run, and every contradiction is fixed or logged as a decision with a decider.
- [ ] The weekly exception brief has run for at least four cycles, with every number checked against its source.
- [ ] The health review scored every dimension against Appendix C and named the weakest dimension as next quarter's focus.
- [ ] Quarterly re-grills of living artifacts and annual re-grills of durable ones are on the calendar.
- [ ] The grilling and maintenance prompts are saved as reusable instructions others on the team can run.

## Key takeaways

- A Principal PM's first 90 days produce decisions more than features. Build the Product 360 to make those decisions visible, owned and durable: learn and anchor, then decide and build the spine, then operate and prove.
- Separate facts from decisions. The harness fetches and cites facts through connectors; you supply decisions; anything neither sourced nor decided stays visible as a gap.
- The grilling session is the core technique: one question at a time, a recommended answer from the evidence, challenges against seven explicit tests and a written log. Run it per dimension, live for judgment and in file mode for stakeholders.
- Anchor the harness in labeled reference materials before you grill, and generate artifacts in a fresh session from the approved log. Keep three human gates: the gap list, the log and the audit.
- Audit the artifacts against each other as well as against their sources. The most useful findings are contradictions between positioning and risk, or between roadmap and lifecycle, and each one becomes a fix or a logged decision.
- Day 90 ends with a running cadence, a health review scored against Appendix C and the weakest dimension chosen as next quarter's focus.
