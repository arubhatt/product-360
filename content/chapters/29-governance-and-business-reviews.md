<p class="lead">Governance is how a product organization looks at itself on a schedule: which numbers it reads each week, which decisions it writes down, which risks it tracks and who gets the call when something breaks. Done well, it makes good decisions faster and bad surprises rarer. Done badly, it becomes a calendar full of meetings that change nothing. This chapter shows you how to build the first kind and retire the second.</p>

## Why this matters

As a Senior or Principal PM, you spend a large share of your week inside governance forums: the weekly metrics review, the monthly product review, the quarterly business review, the autumn planning cycle and the escalation when a customer is angry. These forums decide where money, people and attention go, so treat them as the control system for the real work.

Most governance grows by accretion. A forum created after a crisis outlives it. A status deck gets longer each quarter because removing a slide feels risky. A decision made in a hallway is remembered three different ways six months later. A risk is visible to everyone and owned by no one. Nobody intends this; it's what happens when nobody designs the system as a whole.

AI adds a second pressure in 2026. A harness can assemble a review pack from live systems in minutes, so producing governance material is now cheap. Reading it, checking it and acting on it costs as much as ever. Teams that used to be starved of data now risk drowning in fluent, unverified summaries, and the PM's job moves from compiling the pack to verifying it.

This chapter covers the forums (weekly business review, monthly product review, internal QBR, annual planning, portfolio review, metric review), the records that hold them together (decision log, risk register, escalation policy) and the medium underneath: written narratives instead of slides for any meeting that decides something. Together they form the Operate dimension of your Product 360 (Chapter 00) and lean on the product ops function in Chapter 28.

## Core concepts and frameworks

### Governance that helps and governance that hurts

Jeff Bezos's 2016 letter to Amazon shareholders names the failure mode precisely. He calls it **process as proxy**: good process exists to serve customers, but over time a team can start to manage the process instead of the outcome, until "we followed the process" becomes an acceptable answer to a bad result. His test is a question every PM should ask of every forum they attend: do you own the process, or does the process own you?

The same letter makes a second point that matters for governance design. Bezos argues that most decisions should be made with **"somewhere around 70% of the information you wish you had"**, because speed matters as much as quality. A year earlier, in his 2015 letter, he had split decisions into two types. **Type 1** decisions are consequential and irreversible or nearly so; they deserve a slow, careful, consultative process. **Type 2** decisions are reversible, and should be made quickly by individuals or small groups. His warning is that large organizations tend to apply the heavyweight Type 1 process to almost everything, and the result is slowness, risk aversion and too little experimentation.

That gives you a design rule: heavyweight review is for one-way doors, and everything else gets delegated, logged and revisited if it turns out wrong. Much of what people call bureaucracy is a Type 2 decision run through a Type 1 process.

This book adds a test for recurring forums. **A forum earns its place if it regularly changes a decision, a resource allocation or a metric owner's next action.** If its last three sessions changed nothing, merge it, shrink it or cancel it. Chapter 00 put it more bluntly: every ritual produces a decision or it gets cancelled.

:::key Governance is a product
Treat your governance system the way you'd treat a product. It has users (the people in the room and the people who act on the outcome), a job (make good decisions at the right speed) and a cost (hours of senior attention). Design it deliberately, measure whether it does its job and retire the parts that don't.
:::

### The operating cadence

The forums nest. The weekly review catches exceptions in the inputs; the monthly and quarterly reviews compare progress with the annual plan; annual planning sets that plan; the portfolio review divides the investment envelope. Three standing records run alongside and connect them.

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 380" role="img" aria-label="Operating cadence: weekly, monthly, quarterly and annual forums stacked, with the decision log, risk register and escalation policy running alongside">
  <rect x="20" y="20" width="440" height="70" rx="10" class="box"/>
  <text x="40" y="48" class="t" style="fill:var(--a1)">Annual: OP1 and OP2 plan narratives</text>
  <text x="40" y="70" class="s">Sets metrics, initiatives, resources and targets for the year</text>
  <rect x="20" y="105" width="440" height="70" rx="10" class="box"/>
  <text x="40" y="133" class="t" style="fill:var(--a1)">Quarterly: internal QBR and portfolio review</text>
  <text x="40" y="155" class="s">Rolls products up; invest, maintain, harvest or divest</text>
  <rect x="20" y="190" width="440" height="70" rx="10" class="box"/>
  <text x="40" y="218" class="t" style="fill:var(--a1)">Monthly: product review narrative</text>
  <text x="40" y="240" class="s">Progress against plan; assumption changes; course corrections</text>
  <rect x="20" y="275" width="440" height="70" rx="10" class="box"/>
  <text x="40" y="303" class="t" style="fill:var(--a1)">Weekly: business review (WBR)</text>
  <text x="40" y="325" class="s">Input metrics; exceptions explained by owners; actions</text>
  <line x1="240" y1="275" x2="240" y2="260" class="ln"/>
  <line x1="240" y1="190" x2="240" y2="175" class="ln"/>
  <line x1="240" y1="105" x2="240" y2="90" class="ln"/>
  <rect x="490" y="20" width="170" height="325" rx="10" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="575" y="48" text-anchor="middle" class="t" style="fill:var(--a2)">Standing records</text>
  <rect x="505" y="70" width="140" height="70" rx="8" class="box"/>
  <text x="575" y="100" text-anchor="middle" class="t">Decision log</text>
  <text x="575" y="120" text-anchor="middle" class="s">DACI, door type</text>
  <rect x="505" y="160" width="140" height="70" rx="8" class="box"/>
  <text x="575" y="190" text-anchor="middle" class="t">Risk register</text>
  <text x="575" y="210" text-anchor="middle" class="s">Owner, trigger</text>
  <rect x="505" y="250" width="140" height="70" rx="8" class="box"/>
  <text x="575" y="280" text-anchor="middle" class="t">Escalation policy</text>
  <text x="575" y="300" text-anchor="middle" class="s">Triggers, levels</text>
  <line x1="460" y1="182" x2="490" y2="182" class="ln"/>
  <text x="240" y="370" text-anchor="middle" class="s" style="fill:var(--muted)">Exceptions flow up; plans and targets flow down</text>
</svg>
<figcaption>The operating cadence. Each forum is measured against the one above it, and the three standing records connect them. Exceptions and proposed changes flow up; plans, targets and decisions flow down.</figcaption>
</figure>

| Forum | Cadence | Question it answers | Typical output |
|---|---|---|---|
| Weekly business review | Weekly | What happened to customers and to our inputs last week, and is anything exceptional? | Owner actions; items taken offline |
| Monthly product review | Monthly | Are we on track against the annual plan, and what should change? | Course corrections; asks |
| Internal QBR | Quarterly | How is the portfolio doing against plan, and what does the next quarter need? | Next-quarter commitments; resourcing decisions |
| Portfolio review | Quarterly or half-yearly | Where should the next dollar of investment go? | Posture per product: invest, maintain, harvest, divest |
| Metric review | Quarterly | Are we still measuring the right things? | Metrics added, changed or retired |
| Annual planning | Yearly, with a January revision | What will we achieve next year, with what resources? | The plan of record |

### The weekly business review

The best-documented weekly metrics forum is Amazon's **weekly business review (WBR)**, described by Colin Bryar and Bill Carr in *Working Backwards* and in detail by Cedric Chin of Commoncog. Chapter 18 covers how to design the metric pack, including the "6-12" chart of trailing weeks and months. Here the focus is the WBR as a forum: who speaks, what they may say and how it connects to the rest. Three features define it.

**Metric owners are business leaders, not analysts.** In Bryar and Carr's account, the person who speaks to a metric is the person accountable for moving it, and they prepare in advance, knowing which metrics to skip and which to explain. In Chin's account, owners look at their numbers daily, a department WBR precedes the company one and Finance facilitates.

**Discussion centers on controllable inputs.** Outputs such as revenue, gross profit and churn are shown, but they lag and, in Bryar and Carr's description, generally can't be moved directly and sustainably. Inputs are the actions a team controls. Bezos made the same point in his 2009 letter: Amazon's 2010 plan contained 452 detailed goals, each with an owner, deliverables and a target date, and 360 of them directly affected customer experience. The word "revenue" appeared eight times in that goals document and "free cash flow" four times; net income and gross margin didn't appear at all. He framed the approach as concentrating on the controllable inputs to the business.

**Variance explanation is exception-driven.** Every metric is shown, but owners speak only to exceptional variation or a missed target. A normal week gets a quick "nothing to see here." For an exception, the owner gives a root cause and an action, or says plainly that they don't know yet and are investigating. Chin connects this to Donald Wheeler's distinction between **routine variation** (the process behaving as it always does, where chasing individual wiggles finds nothing) and **exceptional variation** (something changed, so investigate). He warns that forcing teams to explain every up or down move wastes time and invites gaming.

That gives three acceptable forms of variance explanation. Put them in writing for your team:

1. **Routine.** "Within normal range. Nothing to see here."
2. **Explained.** "Exceptional. Cause: [cause, with evidence]. Action: [action, owner, date]."
3. **Unexplained.** "Exceptional. Cause unknown. Next step: [investigation, owner, date]."

Ban the fourth form, an improvised cause that sounds plausible. It feels helpful in the room and corrupts the team's model of the business.

Chin's account adds two practices. Strategy debates get taken offline, so the WBR stays short. And metrics get added when they reveal a real driver or after something blows up, then demoted to a department review when they stop being useful.

:::onramp If you've never run a WBR
Start with the three forms of variance explanation. Before your next metrics review, ask each owner to label every metric routine, explained or unexplained, in writing, before the meeting. The meeting gets shorter immediately, and the unexplained items become the agenda.
:::

### Monthly and quarterly business reviews

The **monthly business review (MBR)** and **quarterly business review (QBR)** ask whether you're on track against the plan, and what should change. Bryar and Carr describe the Amazon format. Each operating unit reports the prior month or quarter against the annual operating plan in a written narrative of six pages or fewer, plus appendix tables. The review is held 5 to 10 business days after the period closes and runs for an hour with the senior leader, their direct reports and chosen stakeholders. The group leader writes it with their team and finance partner. The contents follow a set order:

1. A table of key output and input metrics against plan and prior year, with prose commentary that puts roughly 80% of the focus on controllable inputs.
2. Three to five key initiatives, each with a red, yellow or green status, the input metric it moves and its headcount.
3. Updates to business assumptions and proposed course changes.
4. Resource status: hiring, and fixed and variable operating cost against budget.
5. An appendix.

For a product organization, use two layers. The **monthly product review** belongs to the PM: one product, one narrative, reviewed with your leader and cross-functional peers. The **internal QBR** belongs to the portfolio leader: several products rolled up, with the tradeoffs only visible at that level. Keep it distinct from the customer QBR that account teams run with large customers (Chapter 27).

The third section matters most: **assumption changes and proposed course corrections.** Every plan rests on assumptions about the market, the customer and your capacity. The monthly review is where you say in writing which have moved and what you propose. A review with no changed assumptions describes either a remarkably predictable business or a hidden problem.

### Annual planning: OP1 and OP2

Annual planning sets the investment envelope and the plan every other review is measured against. Bryar and Carr describe Amazon's version as two passes, **OP1** and **OP2**, and their calendar-year example runs roughly like this:

| When | What happens |
|---|---|
| June | CEO and CFO set top-down guidance: targets for metrics, initiatives and resources |
| July and August | Optional offsites and vision documents |
| September and October | Teams write OP1 plans as narratives (about four weeks); Finance loads the numbers |
| October and November | OP1 reviews, first with the division executive and then with the CEO and executive team |
| November | CEO finalizes the OP1 profit and loss, decisions and goals |
| November and December | Board review |
| January | Executive team reviews variance against fourth-quarter actuals and produces OP2, the plan of record |

The design point is that **top-down targets meet bottom-up plans at the OP1 review**, where initiatives get funded, cut or modified. A plan, in their framing, has four parts: metrics, initiatives, resources and org structure. They recommend more than 5 and fewer than 20 key metrics (8 to 15 is typical), and specific, measurable initiatives, each with a leader, dates, projected metric impact and resources.

Two more practices are worth adopting. A small subset of goals gets elevated: in Amazon's case roughly 15% of reviewed initiatives and metrics became S-Team goals, which took about 75% of that team's review time and were reported quarterly. And mid-year changes are deliberately hard: changing an OP goal or adding resources needed senior approval, while adding an initiative within existing resources was easier. In their account the friction is deliberate: it keeps the plan of record worth measuring against.

Add one section their template doesn't name: **what we will not do.** Declined tradeoffs are part of the plan, and writing them down stops the same requests returning every month. Chapter 03 covers the strategy behind the plan.

### Portfolio reviews

A portfolio review asks where the next dollar should go. The idea of managing products as a portfolio of cash uses and cash sources traces to the **growth-share matrix**. BCG's history of it says Alan Zakon (later BCG's CEO) first sketched it, refined it with colleagues, and Bruce Henderson popularized it in a 1970 essay, "The Product Portfolio." It sorts businesses by market growth and relative share: **stars** (high growth, high share) deserve significant investment; **cash cows** (low growth, high share) fund the others; **question marks** (high growth, low share) need investment or exit depending on their odds; and the low-growth, low-share quadrant is a candidate for divesting or repositioning.

Practitioners often turn this into four **postures**: invest, maintain, harvest and divest. The verbs are common practice, not BCG's labels, and they suit a product review better than the quadrant names because they state what you'll do.

| Posture | What it means | What the review should see |
|---|---|---|
| **Invest** | Grow share or create a market; fund ahead of revenue | Evidence the bet is working; the input metrics that prove it |
| **Maintain** | Hold position; fund at a sustainable level | Stable unit economics; the cost of keeping parity |
| **Harvest** | Minimize new investment; maximize cash and retention | Margin, retention and the support load trend |
| **Divest** | Exit through sunset, sale or migration | Migration plan, customer impact and dependencies |

Platform businesses need a caveat the matrix misses. A low-share component can be a dependency for higher-value products or for customers' own integrations. Before moving anything to divest, price the cascade: which products, partners and customer workflows break, and what migrating them costs. Chapter 14 covers platform dependencies; Chapter 30 covers running the sunset.

For each product or bet, show the current and proposed posture, the evidence, the investment this year and next, the dependencies and the **posture trigger**: the evidence that would move it to a different posture. Without triggers, the portfolio ossifies around last year's bets.

### Metric reviews

A **metric review** asks whether you're still measuring the right things. Run it quarterly, apart from the WBR, so this week's exceptions don't crowd it out.

For each metric in the WBR and the plan, ask five questions:

1. Does it still have a named owner who acts on it?
2. Is its definition written down and versioned, and does every report use the same one?
3. Do we know its normal range, so we can tell routine variation from exceptional?
4. For an input metric: when it moved, did the output follow? Which inputs moved without the output following?
5. In the last quarter, did it trigger a discussion or a decision? If not, should it be demoted?

The fourth question improves the business. An input that moves without its output following is the wrong input or the wrong definition of it. Refining it until it predicts the output is how a team learns the causal structure of its business, the WBR's purpose in Chin's framing. Chapters 02 and 18 cover metric trees and the metric dictionary.

### Decision rights and the decision log

Much governance pain comes from unclear decision rights: nobody knows who decides, so everybody weighs in and nothing ends. **DACI**, popularized by Atlassian's Team Playbook, is the lightest fix that works. It names four roles:

- **Driver**: coordinates the stakeholders, gathers the information, scopes the decision and makes sure it gets made by the agreed date. Usually the PM.
- **Approver**: makes the decision. Atlassian is emphatic that there is exactly one, writing **"The one person (yes: one!) who makes the decision."**
- **Contributors**: have the subject knowledge and make recommendations. They have a voice but not a vote.
- **Informed**: are told the outcome. No voice, no vote.

Atlassian's template adds the record: status, impact and due date, a short background, the decision criteria, at least three options with pros, cons and cost, action items and the outcome.

Bain's **RAPID** (Recommend, Agree, Perform, Input, Decide) is the main alternative. It adds an explicit **Agree** role, sparing and veto-like, often for legal or regulatory must-haves, and a **Perform** role for whoever executes. Bain advises that not every decision needs formal roles; start with high-value or high-frequency ones. Use DACI by default, and borrow RAPID's Agree role when a genuine veto holder, such as compliance, would otherwise hide among the Contributors.

The **decision log** records the result. Each entry records the decision in one sentence, the date, the DACI names, the options considered, the evidence, the outcome and two fields this book adds: the **door type** (one-way or two-way, after Bezos's Type 1 and Type 2) and the **reversal trigger** (the evidence that would make you revisit it, with a revisit date). Bezos's 70% rule fits here too: for a two-way door, write down what information would change the decision, then decide without waiting for it.

### Risk registers

A **risk register** lists what could go wrong, each item with an owner and a plan. The format is old and dull, and it works when kept current. Public references for risk management practice include HM Treasury's *Orange Book* in the UK; for AI products, the US National Institute of Standards and Technology's **AI Risk Management Framework** (AI RMF 1.0, released in January 2023) organizes the work into four functions: **Govern, Map, Measure and Manage.** NIST added a Generative AI Profile in July 2024 and, as of 2026, says AI RMF 1.0 is under revision.

A useful row has a **risk statement** written as cause, event and consequence ("Because [cause], [event] may happen, which would [consequence]"); a category, plus the AI RMF function for AI risks; likelihood and impact; one named owner; mitigations; an **early indicator** that the risk is starting to happen; an **escalation threshold** saying when and to whom the owner escalates; and the date last reviewed. The indicator and threshold tell you when to act; without them, the register only records. Review the top risks in every monthly product review and the full register quarterly. Chapter 33 covers AI risk assessment and regulation in depth.

### Escalation paths

Escalation is governance under time pressure. Bezos's 2016 letter puts the principle in one line: **"recognize true misalignment issues early and escalate them immediately."** The alternative, he notes, is that disagreements get settled by exhaustion, with whoever has more stamina carrying the decision.

Site reliability engineering has the most developed escalation discipline. Google's *Site Reliability Engineering* book says to declare an incident if any one of three things is true: a second team is needed, the problem is visible to customers, or it's unsolved after an hour of concentrated analysis. It also insists on named roles and explicit, acknowledged handoffs. For product escalation, borrow the **objective triggers**: anyone can check them, so escalating doesn't feel like judging a colleague.

A product escalation policy needs five things:

1. **Triggers**: customer-visible impact, a second team needed, an issue unresolved after a set time, a proposed change to the plan of record, a budget variance above a threshold, regulatory or security exposure.
2. **Levels**: who gets it at each level, by role, with a time to respond.
3. **A required packet**: a one-page narrative with the issue, the options, a recommendation and the specific ask. Nobody escalates with a forwarded email thread.
4. **Handoff**: an explicit statement of who owns the issue now.
5. **Closure**: once decided, everyone commits, including those who disagreed, and the decision goes into the log. Bezos calls this **disagree and commit**, and his letter is clear that it applies to the boss as well.

### Narratives instead of slides

Bezos's 2017 letter describes Amazon's practice: no slide presentations, but narratively structured six-page memos, read silently at the start of the meeting. He writes that **"a great memo probably should take a week or more"** to write, rewrite and edit.

Bryar and Carr explain why. In their account, a slide meeting spends roughly 75% of its time presenting and 25% discussing; a narrative meeting inverts that, with about 25% reading and 75% discussion. They draw on Edward Tufte's critique of slides for small-group decisions. Their working rules: six pages or fewer for a 60-minute meeting and three or fewer for 30 minutes; full sentences, with tables and charts allowed; an appendix that never holds required reading; FAQs that anticipate the reader's questions. While reading, attendees write comments in the margins; the team then works through them in order, and the most senior person speaks last.

Narratives suit decision meetings of roughly 5 to 20 people; slides suit one-to-many broadcasts such as an all-hands or a customer QBR. The narrative types they list map onto this chapter: the OP1 plan, the MBR and QBR, the PR/FAQ, the correction-of-error (COE) review and standard operating procedures.

| Use a narrative when | Use slides when |
|---|---|
| A group of 5 to 20 has to make or shape a decision | You're broadcasting to a large audience |
| The argument depends on reasoning, tradeoffs or data | The content is mostly visual or demonstrative |
| Readers need to compare options in depth | The audience is external and expects a deck |
| You want questions surfaced in writing before discussion | Time is too short for reading |

If your organization mandates decks, put the decisions and asks on the first page, write the summary in prose and circulate in advance for written comments. Chapters 34 and 35 cover the craft.

## How to apply it

Here's a method for designing (or redesigning) the governance around a product or portfolio over one quarter. If you're new in a role, it doubles as a way to learn how decisions actually get made.

**Weeks 1 and 2: Inventory and prune.**

1. **List every recurring forum and record** that touches your product. For each forum, note the attendees, the monthly hours it consumes (attendees times duration, plus preparation) and what its last three sessions changed.
2. **Apply the earn-its-place test.** Merge, shrink or cancel any forum whose last three sessions changed no decision, resource or owner action. Write down what you cancelled and why, so it doesn't quietly return.
3. **Sort recurring decisions by door type**: pricing, roadmap, model or prompt changes, customer exceptions, deprecations. Delegate two-way doors to the lowest sensible level with a log entry; give one-way doors a named Approver and a written proposal.

**Weeks 3 and 4: Decision rights and records.**

4. **Write a decision-rights map**: Driver, Approver, Contributors and Informed for each recurring decision type. Name genuine veto holders (security, legal, compliance) explicitly, borrowing RAPID's Agree role.
5. **Start the decision log** and backfill last quarter's major decisions. The backfill usually exposes decisions that different people remember differently. Resolve them now.
6. **Clean up the risk register.** Rewrite every risk as cause, event and consequence, with one owner, an early indicator and an escalation threshold. Delete risks nobody will own; nobody was managing them anyway.
7. **Write the escalation policy** and test it in a 30-minute tabletop exercise with a realistic scenario, so you find the gaps before a real escalation does.

**Weeks 5 to 8: The review cadence.**

8. **Stand up the WBR** with the metric pack from Chapter 18. Publish the three forms of variance explanation and have owners label every metric before the meeting. Run four weeks before changing the format.
9. **Write the first monthly product review** as a narrative of six pages or fewer, reviewed 5 to 10 business days after close. Make the assumption-changes section the longest.
10. **Agree the internal QBR format** with your portfolio leader: decisions and asks first, then performance against plan, initiatives, risks and commitments.

**Weeks 9 to 12: The quarterly and annual layers.**

11. **Run the first metric review.** Apply the five questions to every metric. Retire or demote at least one; if you can't find one, look harder.
12. **Run a portfolio review**, or prepare your product's entry for your leader's, with posture, evidence and posture trigger.
13. **Prepare for annual planning.** Learn the calendar: when guidance arrives and when plans are due. Start the narrative early; a plan written the week it's due reads like one.

**Ongoing: Govern the governance.** Every six months, repeat steps 1 and 2 and report the hours your forums consumed against the decisions they produced.

:::leader For product leaders
You set the governance load for everyone below you. Each forum you attend generates preparation work two or three levels down, often far more than the meeting itself. Before adding a forum, name the one you'll retire. Ask for narratives instead of decks for any review where you're the Approver, and speak last.
:::

## The AI lens

### Governing AI-powered products

AI products change what governance has to watch in four places.

**The WBR needs AI inputs**: regression eval pass rates, the rate at which users accept the model's output, the "I'm not sure" rate, inference cost per unit of value and the share of actions taken autonomously. Give each a named owner, usually the applied AI lead or the PM. Chapter 31 covers definitions.

**Model and prompt changes are decisions.** A model upgrade, prompt change or new agent tool can change behavior as much as a release, so log them. Most prompt changes are two-way doors. Widening what an agent may do on its own in a customer's production environment is closer to a one-way door, because trust lost to a bad autonomous action recovers slowly. Give that class of change a named Approver.

**The risk register needs AI rows and regulatory dates.** Map AI risks to the AI RMF functions so security and compliance reviewers can follow your reasoning, and track regulatory milestones as dated triggers. For products sold into the EU, the European Commission's AI Act timeline is the clearest example: general applicability began on 2 August 2026, and the Digital Omnibus on AI (Regulation (EU) 2026/1744), in force since 27 July 2026, moved the obligations for high-risk systems listed in Annex III to 2 December 2027. Chapter 33 covers the obligations themselves.

**Escalation needs AI triggers.** A wrong AI output that a customer acted on is customer-visible and usually needs a second team, which meets two SRE triggers at once. Write AI-specific triggers into the policy before you need them.

Underneath sits a wider shift. Microsoft's 2025 Work Trend Index, a vendor survey of 31,000 workers in 31 markets, found that 81% of leaders expected agents to be moderately or extensively integrated into their company's AI strategy within 12 to 18 months, and proposed a "human-agent ratio" as a management metric. Treat it as directional. When agents do work inside your product and your company, your forums have to review what the agents did as well as what people did.

### Doing the work with AI: review packs and their verification

Anthropic introduced the **Model Context Protocol** (MCP) in November 2024 as an open standard for connecting AI assistants to the systems where data lives. With connectors, a harness can pull metrics, tickets, CRM notes and docs into a draft WBR or monthly review in minutes. **Agent Skills**, introduced in October 2025, let a team package the recipe (sources, metric definitions, format, verification checklist) as a folder of instructions, so every week's pack is built the same way. Grounded **citations**, as Anthropic's platform documentation describes them, return the exact passages supporting each claim.

The gain is real, and so is the new failure mode: fluent summaries are easy to trust. Two public examples make the risk concrete. In 2025, Fortune reported that Deloitte would partially refund the Australian government for a 237-page report, published in July 2025, after errors were found that included citations to nonexistent papers and a fabricated quote attributed to a federal court judge; the revised version disclosed the use of a generative AI tool, and Deloitte said the findings were unchanged. And Vectara's public hallucination leaderboard, which measures how often models add unsupported content when summarizing a document they were given, still showed a nonzero rate for every listed model in October 2026. Grounding a model in source documents doesn't make it error-free.

A valid citation shows the cited passage exists. It doesn't show that the claim drawn from it is right, that the source was current or that the causal story connecting two numbers is true.

This book's verification protocol for any AI-assembled review pack has six rules:

1. **Every number cites its source system and a timestamp.** No citation, no number.
2. **The owner reconciles headline numbers** against the system of record before the pack circulates. Headline means anything in the summary, any output metric and any number tied to a decision.
3. **Causal claims are labeled hypotheses** unless the metric owner confirms them. "Acceptance fell because of the model change" stays a hypothesis until someone checks.
4. **Spot-check a fixed sample of citations** every week, chosen by the reviewer, not the author. Read the source and confirm the claim.
5. **Disclose AI drafting and name the accountable human.** Microsoft's 2025 Work Trend Index report did exactly this, stating that AI helped produce it and that people reviewed and revised all AI-generated content. Copy the practice.
6. **The owner writes the last sentence of every variance explanation.** The model can propose; the owner states the cause, or states that it's unknown.

| Task | The harness | The metric owner or PM |
|---|---|---|
| Pull metrics and build the 6-12 charts | Drafts from connectors, with citations | Confirms sources and freshness |
| Flag exceptional variation | Compares against the normal range | Decides whether it matters |
| Draft variance explanations | Proposes candidate causes with evidence | Writes the final explanation |
| Summarize customer events and escalations | Clusters tickets and notes | Picks what customers really experienced |
| Draft the monthly narrative | Produces a first draft from the WBRs and plan | Rewrites the assumptions and recommendations |
| Check the pack | Runs the checklist and lists unverified claims | Signs off |

:::ai The one-line rule
Let the harness compile, compare and draft. Never let it be the metric owner. A number in a review pack is a claim someone is accountable for, and that someone has to be a person who checked it.
:::

## The Beacon case: building Beacon's operating system

:::example Where Beacon starts
Three months into your role as Principal PM for Beacon, governance has grown by accretion. Beacon has a weekly metrics review (redesigned using Chapter 18), a monthly status deck for the VP of Product for the Operations portfolio, a quarterly business review that rolls up Observe, Desk and Beacon, and a planning cycle that starts next month. The decision log is a chat channel. The risk register is a spreadsheet tab last updated before Beacon Agents entered its design-partner pilot. Then the wrong rollback happens.
:::

**The escalation that tested the system.** The incident from Chapter 31, where a responder at a retail customer accepted the agent's root cause, rolled back the wrong service and took checkout down for eleven minutes during a sale, met two triggers before anyone had written them down: it was customer-visible, and it needed a second team. The customer's VP of IT Operations called Northlight's CEO, so the escalation reached the top without passing anyone who could act on it. Afterward you write the policy you wish you'd had. Any AI-caused customer-visible incident reaches you and the applied AI lead within an hour and the VP of Product the same business day, with a one-page packet: what happened, what's already changed, the options and the ask. An enterprise customer threatening churn alongside a security finding reaches the VP within 24 hours.

**The decision log, rebuilt.** You move the log out of the chat channel and backfill it. Two entries from the incident set the pattern. Pausing the agent's rollback proposals is a **two-way door**: you're the Approver, and the reversal trigger is the eval suite reaching its targets. Widening customer-allowlisted autonomous actions in future releases is treated as a **one-way door** for trust: the VP of Product approves, Sam's security requirements sit in an explicit Agree role and the revisit date is tied to the next eval report.

**The risk register, rewritten.** "AI hallucination" was the only AI row. You rewrite it: because the agent can over-weight recent deploys and miss events outside the affected region, it may propose a wrong root cause with high confidence, which could lead a responder to take a harmful action in production. The early indicator is the eval suite's rate of diagnoses with mismatched timelines; the escalation threshold is any customer-visible action taken on a wrong diagnosis. You map it to the AI RMF's Measure and Manage functions, the first thing Sam asks about. A second row covers EU AI Act documentation, with regulatory dates and customer requests as triggers.

**The weekly review, with an AI-built pack.** Your product ops lead packages the WBR recipe as a team skill: connectors to the metrics store, incident tracker and CRM, the metric dictionary and the six-rule checklist. In the second week the checklist catches something the draft didn't flag: inference cost per resolved incident cites a finance dashboard that hadn't refreshed in three weeks. The finance partner corrects the figure before circulation. Nothing in the draft looked wrong; only the timestamp rule caught it.

**The pricing decision.** Moving Beacon Agents to a per-resolved-incident price is a Type 1 decision: it changes contracts, partner margins and revenue recognition, and is hard to undo once customers sign. You're the Driver; the VP of Product for the Operations portfolio is the Approver; finance, product marketing and sales are Contributors; partners, including MSPs like Leo's, are Informed before any announcement. The record lists three options (keep per-environment pricing, a hybrid, or a full move), each with pros, cons and cost. Chapter 15 covers the pricing itself; here the point is one Approver, a date and a record anyone can find.

**The portfolio review.** Your VP's quarterly portfolio review asks for a posture for each part of Beacon. You propose **invest** for Beacon Agents, **maintain** for correlation and **harvest, then divest** for the legacy Beacon Classic engine through a migration, with the share of Classic customers migrated as the posture trigger. The review pushes back, rightly: several Classic customers call its correlation APIs from their own integrations, so a divest date set without pricing that cascade would break workflows Beacon doesn't own. The date moves to the lifecycle plan in Chapter 30, gated on a migration path for API users.

**The monthly narrative.** You replace the status deck with a five-page monthly product review. The metrics table shows the outputs: ARR of about $48M growing 38% year over year, NRR of 118% and gross margin of 72%, down from 81% before the agentic features launched. The commentary concentrates on inputs: diagnosis acceptance, autonomous resolution and inference cost per resolved incident. The assumption-changes section is the longest. The plan assumed trust would grow with accuracy; the rollback showed that trust also depends on how the agent expresses uncertainty. The proposed course change is to ship calibrated confidence before widening autonomous actions. The VP reads in silence, writes eleven margin comments and speaks last.

**The OP1 narrative.** Next year's plan is a narrative, not the deck template. Its thesis is that Beacon earns the right to act autonomously by proving it can diagnose reliably. It names three initiatives: launching Beacon Agents with supervised remediation at Northlight Live; recovering gross margin from 72% through inference cost work, toward a target the finance partner sets; and completing the AI Act documentation EU customers have asked for, owned with Sam. Its "what we will not do" section carries over the refusals from the strategy in Chapter 03, including no Beacon metrics store, which settles a request that had come up in three consecutive monthly reviews.

## Product 360 artifacts

```template id="29-weekly-business-review" title="Weekly business review"
# Weekly business review · [Product] · Week of [Date]

**Pack owner:** [Name]   **Facilitator:** [Name]   **Length:** [30 to 60] minutes
**Data freshness:** [timestamp of the latest source refresh]   **Sources:** [systems of record]
**AI drafting:** [Yes/No]. Drafted by [harness or skill name]; verified by [Name] on [date].

## 1. What customers experienced last week
- Top customer events, incidents and escalations (max three), with links:
  1.
  2.
  3.

## 2. Output metrics (shown, not debated)
| Metric | This week | vs plan | vs prior year | Trailing 6 weeks | Owner |
|---|---|---|---|---|---|
| | | | | | |

## 3. Controllable input metrics (the discussion)
| Metric | Owner | This week | vs plan | Routine / Exceptional | Owner note |
|---|---|---|---|---|---|
| | | | | | |

Owner notes use one of three forms only:
- Routine: "Within normal range. Nothing to see here."
- Explained: "Exceptional. Cause: [cause, evidence link]. Action: [action, owner, date]."
- Unexplained: "Exceptional. Cause unknown. Next step: [investigation, owner, date]."

## 4. Actions from last week
| Action | Owner | Due | Status (done / on track / late) |
|---|---|---|---|
| | | | |

## 5. Taken offline
| Topic | Owner | Forum it goes to | Date |
|---|---|---|---|
| | | | |

## 6. Verification checklist (before circulation)
- [ ] Every number cites a source system and timestamp
- [ ] Headline numbers reconciled against the system of record by their owners
- [ ] Causal claims labeled "hypothesis" unless the owner confirmed them
- [ ] Citation spot-check done by the reviewer: [n] checked, [n] corrected
- [ ] Every variance explanation's final sentence written by its owner
```

```template id="29-monthly-product-review" title="Monthly product review"
# Monthly product review · [Product] · [Month, Year]

**Author:** [PM]   **With:** [finance partner, engineering lead, design lead]
**Review date:** [5 to 10 business days after month close]   **Length:** six pages or fewer, plus appendix
**Reviewers:** [leader, peers, invited stakeholders]   **AI drafting disclosed:** [Yes/No; verified by Name]

## 1. Summary (half a page, prose)
What happened, whether we're on track against the annual plan, and the one or two decisions or asks for this review.

## 2. Metrics against plan and prior year
| Metric | Type (input/output) | Actual | Plan | Prior year | Commentary |
|---|---|---|---|---|---|
| | | | | | |
Commentary: most of it on controllable inputs. For each exceptional move: cause, or "unknown" and next step.

## 3. Key initiatives (three to five)
| Initiative | Owner | Status (R/Y/G) | Input metric it moves | Headcount | Next milestone |
|---|---|---|---|---|---|
| | | | | | |
For anything yellow or red: what changed, what we're doing, what we need.

## 4. Assumptions that changed, and proposed course corrections
| Plan assumption | What we now believe | Evidence | Proposed change | Decision needed from |
|---|---|---|---|---|
| | | | | |

## 5. Top risks (from the risk register)
| Risk | Owner | Early indicator status | Change since last month |
|---|---|---|---|
| | | | |

## 6. Resources
Hiring against plan; fixed and variable operating cost against budget; inference or other usage-driven cost against budget.

## 7. Asks and decisions
1. [Decision or ask] · Approver: [Name] · Needed by: [Date]

## Appendix (never required reading)
6-12 charts, detailed tables, decision log entries made this month.
```

```template id="29-qbr-outline" title="Internal QBR outline"
# Internal quarterly business review · [Portfolio or product] · Q[n] [Year]

**Owner:** [Portfolio leader]   **Contributors:** [PMs, finance, engineering, GTM leads]
**Format:** narrative preferred. If a deck is mandated, keep this order and write page 1 in prose.

1. **Summary and decisions needed** (one page, prose): the quarter in three sentences; the decisions and asks for this review, each with an Approver.
2. **Outputs against the operating plan**: revenue, retention, margin and the North Star against plan and prior year.
3. **Inputs and what moved them**: the controllable inputs that explain the outputs, with evidence. Label unconfirmed causes as hypotheses.
4. **Initiatives**: status (R/Y/G) for each plan initiative, the input metric it moves and the change since last quarter.
5. **Changed assumptions**: which plan assumptions no longer hold and what we propose instead.
6. **Cross-product tradeoffs**: shared resources, dependencies and conflicts only visible at portfolio level.
7. **Top five risks**: from the risk register, with owners, indicators and escalations this quarter.
8. **Next-quarter commitments**: what we will deliver, the metric each moves and what we will not do.
9. **Appendix**: per-product monthly reviews, 6-12 charts, decision log extract, headcount and budget detail.

Rule: decisions and asks come first. Nothing in the appendix is required reading.
```

```template id="29-annual-plan-narrative" title="Annual plan narrative"
# [Year] operating plan · [Product or portfolio] · OP1 draft v[n] / OP2

**Author:** [Name]   **Finance partner:** [Name]   **Due:** [Date]   **Top-down guidance received:** [Date, link]

## 1. Introduction and thesis (one paragraph)
What this product will achieve next year, and the single bet the plan rests on.

## 2. Last year in review
| Goal | Target | Actual | Hit / missed | What we learned |
|---|---|---|---|---|
| | | | | |

## 3. Key metrics (more than 5, fewer than 20)
| Metric | Type (input/output) | Owner | Q1 | Q2 | Q3 | Q4 | Year-end target |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 4. Key initiatives
| Initiative | Leader | Start / finish | Metric it moves, and by how much | Resources | Elevated goal? (Y/N) |
|---|---|---|---|---|---|
| | | | | | |

## 5. Resources and organization
Headcount by team, hiring plan, operating cost, usage-driven cost (inference, cloud) and any org changes.

## 6. What we will not do
| Request or option declined | Who asked | Why not this year |
|---|---|---|
| | | |

## 7. Risks and dependencies
Top risks from the register; dependencies on other teams, with named counterparts and agreed dates.

## 8. FAQ
Questions a skeptical reviewer will ask, answered in advance.

## 9. Appendix
P&L, initiative detail, headcount table, roadmap.

## Change control
After OP2, changing a goal or adding resources requires approval from [role]. Adding an initiative within existing resources requires [role].

## OP2 revision (January)
Variance against Q4 actuals: [summary]. Changes from OP1: [list, with reasons].
```

```template id="29-portfolio-review" title="Portfolio review"
# Portfolio review · [Portfolio] · [Quarter or half, Year]

**Owner:** [Portfolio leader]   **Approver for posture changes:** [Name]   **Investment envelope:** [amount or headcount]

## Portfolio summary
| Product or bet | Current posture | Proposed posture | Market growth | Our position | Gross margin (after usage costs) | Investment this year | Investment next year | Decision needed |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Postures: Invest (grow; fund ahead of revenue) · Maintain (hold; fund sustainably) · Harvest (minimize new investment; maximize cash and retention) · Divest (exit through sunset, sale or migration).

## Per product or bet
### [Name]
- Posture now and proposed:
- Evidence for the proposal (input and output metrics, customer evidence):
- Strategic fit:
- **Posture trigger** (the evidence that would move this to a different posture):
- Dependencies (other products, partners, customer integrations that rely on it):
- Cost of the cascade if divested:
- Decision needed and Approver:

## Decisions made
Recorded in the decision log: [links]
```

```template id="29-decision-log" title="Decision log"
# Decision log · [Product or portfolio]

**Log owner:** [Name]   **Location:** [single shared location]   **Review:** monthly for revisit dates

| ID | Date | Decision (one sentence) | Door type (one-way / two-way) | Driver | Approver | Contributors | Informed | Options considered | Evidence (links) | Outcome / status | Reversal trigger | Revisit date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D-001 | | | | | | | | | | | | |

## Full record (for one-way doors)
### D-[ID] · [Decision title]
- **Status:** Not started / In progress / Decided   **Impact:** High / Medium / Low   **Due:** [Date]
- **Background (one or two sentences):**
- **Relevant data:** [links, with timestamps]
- **Decision factors (criteria):** [e.g. cost, time to market, reversibility, customer trust]
- **Options (at least three):**

| Option | Description | Pros | Cons | Cost (money and people) |
|---|---|---|---|---|
| A | | | | |
| B | | | | |
| C | | | | |

- **Veto holders, if any (RAPID's Agree role):**
- **What information would change this decision:**
- **Outcome:** [decision, Approver, date]
- **Dissent recorded, and commitment confirmed:**
- **Action items:** [action, owner, date]
```

```template id="29-risk-register" title="Risk register"
# Risk register · [Product or portfolio]

**Register owner:** [Name]   **Top risks reviewed:** monthly   **Full review:** quarterly   **Last full review:** [Date]

| ID | Risk statement (Because [cause], [event] may happen, which would [consequence]) | Category | AI RMF function (Govern / Map / Measure / Manage), if AI | Likelihood (H/M/L) | Impact (H/M/L) | Owner | Mitigations in place | Mitigations planned | Early indicator | Escalation threshold, and to whom | Status | Last reviewed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-001 | | | | | | | | | | | | |

Categories: customer, security, AI behavior, regulatory, commercial, delivery, dependency, people.

## Dated triggers (regulatory and contractual)
| Date | Obligation or event | Affected risk IDs | Owner | Readiness |
|---|---|---|---|---|
| | | | | |

## Closed risks
| ID | Closed on | Why (mitigated / occurred / no longer relevant) | Lesson |
|---|---|---|---|
| | | | |
```

```template id="29-escalation-policy" title="Escalation policy"
# Escalation policy · [Product or portfolio] · v[n] · [Date]

**Policy owner:** [Name]   **Approved by:** [Name]   **Last tested (tabletop):** [Date]

## When to escalate (any one trigger is enough)
- Customer-visible impact, including any customer action taken on a wrong AI output
- A second team is needed to resolve it
- Unresolved after [time] of concentrated work
- A proposed change to the plan of record (goal, date or resources)
- Budget or usage-cost variance above [threshold]
- Security, privacy or regulatory exposure
- An enterprise customer threatening churn
- A disagreement between owners unresolved after [time]

Escalating early is expected. Nobody is judged for escalating against a trigger.

## Levels
| Level | Who (role and name) | Response time | Can decide |
|---|---|---|---|
| 1 | [PM and engineering lead] | [time] | [scope] |
| 2 | [Group PM or director] | [time] | [scope] |
| 3 | [VP of Product, with peer VPs as needed] | [time] | [scope] |

## The escalation packet (one page, required)
1. What happened, and the impact, with evidence
2. What has already been done
3. Options (at least two), with tradeoffs
4. Recommendation
5. The specific ask, and by when

## Handoff
State explicitly who owns the issue now, and confirm acknowledgment in writing.

## Closure
- The Approver decides; everyone commits, including those who disagreed.
- The decision goes into the decision log; the risk register is updated.
- For customer-visible incidents, a correction-of-error narrative goes to the next monthly product review.
```

## Prompts

```prompt title="Assemble a cited weekly business review pack"
Goal: Get a first draft of the WBR pack in minutes, with every number traceable.
Paste in (or connect the harness to): the WBR metric list with definitions, owners and targets; read access to the metrics store, incident tracker and CRM; last week's pack and action list. Use an approved tool if the data includes customer names or contract values.

Build this week's weekly business review pack for [product], week of [date], using the attached template.

Rules:
1. Every number must cite its source system, the exact report or query it came from and the source's last refresh timestamp. If you can't find a source or the refresh is older than [n] days, write "UNVERIFIED" instead of the number.
2. For each input metric, compare this week with its normal range over the last [20] weeks. Label it "routine" or "exceptional" and say why in one line. Don't explain routine moves.
3. For exceptional moves, list up to three candidate causes with the evidence for each, labeled "hypothesis for owner." Don't pick one.
4. Summarize what customers experienced: the top three incidents, escalations or notable tickets, with links.
5. Carry forward last week's actions with their current status from the tracker.
6. End with a list of every claim you couldn't verify.

Check the output: open the three oldest timestamps and two random citations yourself. Make sure no owner note has been written for the owner; the "hypothesis for owner" lines are prompts for them, not explanations.
```

```prompt title="Verify an AI-drafted review pack before it circulates"
Goal: Catch stale numbers, broken citations and invented causes before a leader reads them.
Paste in: the draft pack, the metric dictionary and exports or links from the systems of record for the headline numbers.

Act as the reviewer of this [weekly / monthly / quarterly] review pack for [product]. Check it against the attached sources and report, in a table:

1. Every headline number (anything in the summary, any output metric, any number tied to a decision): matches the source / doesn't match / can't check. Give the source value and timestamp.
2. Every citation in a random sample of [10]: does the cited passage exist, and does it support the claim as written?
3. Every causal claim ("X drove Y", "because", "due to"): is it labeled as a hypothesis or confirmed by a named owner? List any that aren't.
4. Any metric whose definition in the pack differs from the metric dictionary.
5. Any source older than [n] days.

Don't fix the pack. List the problems, ranked by how badly they'd mislead a decision.

Check the output: re-check two of the items the model marked "matches" yourself. A reviewer that never finds anything isn't reviewing.
```

```prompt title="Draft the monthly product review narrative"
Goal: Turn a month of weekly reviews into a first-draft narrative of six pages or fewer.
Paste in: the month's WBR packs and action logs, the annual plan (metrics, initiatives, assumptions), the top of the risk register, the month's decision log entries and the budget report.

Draft a monthly product review narrative for [product] for [month], using the attached template. Write in full sentences, not bullets, except for the tables.

1. Summary: half a page. State whether we're on track against the annual plan and the one or two decisions this review needs.
2. Metrics against plan and prior year: put most of the commentary on controllable inputs.
3. Initiatives: status and the input metric each moves.
4. Assumptions that changed: compare each plan assumption with this month's evidence and list those that no longer hold. This is the most important section; don't leave it empty without saying why.
5. Risks, resources and asks.

Label every causal claim as a hypothesis unless the action logs show an owner confirmed it. Keep it to [n] pages; move detail to an appendix that nobody has to read.

Check the output: rewrite the summary and the assumptions section yourself. They carry your judgment, and the model can only propose them. Confirm every number against the verified WBR packs.
```

```prompt title="Red-team an annual plan narrative"
Goal: Find the weaknesses a senior reviewer will find, before the OP1 review.
Paste in: your plan narrative draft, the top-down guidance and last year's plan with actuals.

Act as a demanding executive reviewing this annual operating plan for [product]. Read it through five lenses, one at a time:
1. Facts and truth: which claims lack evidence or contradict last year's actuals?
2. Strategic vision: does the plan follow from a clear thesis, or is it a list?
3. Metrics and initiatives: does every initiative name the metric it moves and by how much? Are there more than 5 and fewer than 20 key metrics?
4. Achievability: which commitments look unrealistic given the resources and last year's delivery record?
5. Resource allocation: where is investment misaligned with the stated priorities?

Then write the ten questions you'd ask in the review, and list anything that should be in a "what we will not do" section but isn't.

Check the output: answer each of the ten questions in the plan's FAQ, or change the plan. Ignore any critique that relies on facts not in the materials.
```

```prompt title="Prepare a DACI decision record"
Goal: Turn a stuck discussion into a decision with one Approver and a date.
Paste in: the thread, notes or documents where the decision has been debated, and the names and roles of the people involved.

From this material, draft a DACI decision record for: [decision].

1. Propose a Driver, one Approver, Contributors and Informed, with a one-line reason for each. If more than one person seems to think they're the Approver, say so explicitly.
2. Write the background in one or two sentences.
3. List the decision factors (criteria) that people have actually argued about.
4. Lay out at least three options, including any that were mentioned and dropped, each with pros, cons and estimated cost.
5. Classify the decision as a one-way or two-way door, and explain why.
6. List what information would change the decision, and whether waiting for it is worth the delay.
7. Flag anyone who appears to hold a veto (security, legal, compliance).

Don't recommend an option. Don't invent costs or facts not in the material; write "unknown" instead.

Check the output: confirm the Approver with that person before circulating. Check that each option is described fairly enough that its advocate would agree with the summary.
```

```prompt title="Audit the governance calendar"
Goal: Find the forums that cost more than they return.
Paste in (or connect): your calendar for the last [8] weeks, the list of recurring forums with attendees, and the decision log and action logs. Use an approved tool for calendar data.

For each recurring forum I attend or own:
1. Estimate the hours it consumes per month: attendees multiplied by duration, plus a preparation estimate I'll confirm.
2. From the decision and action logs, list what it changed in its last three sessions: decisions made, resources moved, owner actions created.
3. Flag forums with no changes in their last three sessions, forums that overlap more than half their attendees and agenda with another, and forums making two-way-door decisions with a one-way-door process.
4. Recommend for each: keep, merge (with which), shrink or cancel.

Check the output: talk to the owner of each forum flagged for cancellation before acting. Logs undercount the decisions made in a room; ask what would break if it stopped.
```

```prompt title="Build risk register entries from incidents and requests"
Goal: Turn incidents, customer requests and regulatory deadlines into risks someone owns.
Paste in: recent incident reviews, security questionnaire findings, customer escalations, the current register and any regulatory dates that apply. Use an approved tool for customer and security data.

Review this material for [product] and propose risk register entries.

For each risk:
1. Write it as: "Because [cause], [event] may happen, which would [consequence]."
2. Assign a category and, for AI risks, the NIST AI RMF function (Govern, Map, Measure or Manage) it falls under, with a one-line reason.
3. Propose likelihood and impact (H/M/L), citing the evidence.
4. Propose an early indicator we can actually observe and an escalation threshold.
5. Mark whether it duplicates or should be merged with an existing register entry.

List dated obligations separately, with their source. Don't assign owners; leave that field blank for me.

Check the output: confirm every regulatory date against the official source before adding it. Assign one owner per risk yourself, and delete any risk nobody will own.
```

## Anti-patterns

:::warn Process as proxy
The team can show that every review happened on time, every template was filled in and every risk was logged, and the product is still losing customers. The process has replaced attention to the outcome. Ask of every forum whether it changed a decision, a resource or an action recently. If not, change it or stop it.
:::

:::warn Type 1 process for Type 2 decisions
A prompt change, a copy change or a pilot extension goes through the same multi-week review as a pricing change. Teams stop experimenting because the review costs more than the experiment. Sort decisions by door type and delegate two-way doors with a log entry.
:::

:::warn The narrated WBR
Owners explain every up and down move, including routine noise, and improvise causes that sound plausible. The meeting runs long and the team learns false lessons. Use the three forms of variance explanation, and make "cause unknown, investigating" an acceptable answer.
:::

:::warn Status without assumptions
The monthly review reports green, yellow and red against every initiative but never says which assumptions behind the plan have changed. Leaders learn about the broken assumption at the end of the year. Make the assumption-changes section mandatory, and longest.
:::

:::warn The committee Approver
A decision lists five approvers. Each can delay it and none owns it, so it gets made by whoever has the most stamina. Name one Approver per decision, and name veto holders separately if they exist.
:::

:::warn The write-only risk register
Risks are logged, rated and never read again. When one happens, the register shows it was known. Give every risk an owner, an early indicator and an escalation threshold, and review the top risks every month.
:::

:::warn The unverified AI pack
A harness-drafted review pack circulates with a stale number, a broken citation or an invented cause, and a leader acts on it. A fluent pack can still be wrong. Require citations and timestamps, owner reconciliation of headline numbers and an owner-written final sentence for every variance explanation.
:::

## Checklist

- [ ] Every recurring forum has a stated purpose, an owner and evidence that it changed a decision, resource or action in its last three sessions.
- [ ] Recurring decision types are sorted into one-way and two-way doors, and two-way doors are delegated with a log entry.
- [ ] A decision-rights map names the Driver, one Approver, Contributors and Informed for each recurring decision type, with veto holders named explicitly.
- [ ] The decision log is in one shared location and records door type, options, evidence, reversal trigger and revisit date.
- [ ] The WBR runs on controllable inputs with named owners, and every variance explanation uses one of the three forms.
- [ ] The monthly product review is a narrative of six pages or fewer, held 5 to 10 business days after close, with a substantive assumption-changes section.
- [ ] The internal QBR puts decisions and asks first and keeps required reading out of the appendix.
- [ ] The annual plan narrative has more than 5 and fewer than 20 key metrics, initiatives with owners and metric impact, and a "what we will not do" section.
- [ ] The portfolio review states a posture, the evidence and a posture trigger for each product or bet, and prices dependencies before any divest decision.
- [ ] A quarterly metric review has retired or changed at least one metric.
- [ ] Every risk in the register has one owner, an early indicator and an escalation threshold; AI risks are mapped to the AI RMF functions and regulatory dates are tracked.
- [ ] The escalation policy has objective triggers, levels with response times, a one-page packet, an explicit handoff and a closure rule, and has been tested in a tabletop exercise.
- [ ] AI-drafted review packs follow the six verification rules, disclose AI drafting and name the accountable human.
- [ ] The governance calendar is audited every six months for hours spent against decisions produced.

## Key takeaways

- Governance earns its place by changing decisions, resources and actions. A forum whose last three sessions changed nothing should be merged, shrunk or cancelled.
- Match the weight of the process to the decision. One-way doors deserve a written proposal and a single named Approver; two-way doors should be delegated, logged and revisited if they turn out wrong.
- The weekly business review works when business leaders own the metrics, discussion centers on controllable inputs and variance explanations are routine, explained or honestly unexplained.
- Monthly and quarterly reviews are written comparisons against the annual plan. Their most valuable section says which assumptions have changed and what should change as a result.
- The decision log, the risk register and the escalation policy hold the cadence together. Each needs owners, triggers and dates to be more than a record.
- Write narratives for decision meetings and keep slides for broadcasts. Reading in silence and having the most senior person speak last produces better questions than a presentation does.
- AI harnesses make review packs cheap to produce and easy to over-trust. Require a cited source and timestamp for every number, label unconfirmed causes as hypotheses and keep a named human accountable for every claim.
