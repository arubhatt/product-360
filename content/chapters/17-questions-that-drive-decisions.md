<p class="lead">Your AI harness can now answer almost any data question in seconds. That moves the hard part of data-driven product management upstream, to the question itself. This chapter teaches you to start from the decision, ask the questions that could change it, name the evidence that answers each one, and judge the decision by how it was made rather than by how it turned out.</p>

## Why this matters

Ask a harness connected to your analytics, CRM and support tools "How is adoption going?" and you'll get a confident answer. It will have a number, a trend line and a tidy paragraph. It probably won't help you decide anything, because the question didn't say which accounts count, over what period, measured how, or compared with what. The model filled those gaps with guesses, and you can't see which guesses it made.

For most of the last two decades, the constraint on data-driven decisions was access: getting an analyst's time, waiting for a dashboard, learning a query language. Data-driven decision making spread anyway. Erik Brynjolfsson and Kristina McElheran found that the share of US manufacturing plants using it rose from about 11% to 30% between 2005 and 2010. In 2026 the access constraint is mostly gone. Connectors built on the Model Context Protocol let a harness reach product analytics, the warehouse, the CRM, ticketing and call transcripts in a single conversation. The constraint that remains is the quality of what you ask.

Bad questions are expensive in three ways. They waste time on analysis that can't change anything. They produce numbers that look like evidence and get pasted into decks as if they were. And they quietly train the organization to treat data as decoration for decisions already made. Good questions do the opposite: each one names a decision, an owner and the answer that would change the plan.

Part IV of this book follows that order. This chapter is about the questions: which decisions a product leader makes across the lifecycle, what to ask for each one and what evidence answers it. Chapter 18 maps where product data lives and the standard reports every product leader should own. Chapter 19 covers the mechanics of asking a harness and verifying what comes back. You won't find query syntax or spreadsheet formulas anywhere in Part IV. Your harness does the mechanics. Your job is to know what to ask, what a good answer looks like and when the answer is good enough to act on.

## Core concepts and frameworks

### Start from the decision, not the data

Every question in this chapter hangs off a chain with five links:

1. **Decision**: what you're choosing, between which options, by when and who decides.
2. **Question**: the one thing you need to know to choose well.
3. **Evidence**: the quantitative and qualitative sources that answer it.
4. **Report**: the view that puts the evidence in front of you (a funnel, a cohort table, a theme analysis).
5. **Owner**: the person who gets the answer, checks it and brings it to the decision.

Teams usually enter the chain at link 4. Someone opens a dashboard, notices a line moving and starts asking why. Sometimes that finds a real problem. More often it produces activity that never reaches a decision. Entering at link 1 is slower for the first ten minutes and faster for everything after.

The test for whether a question deserves effort comes from Douglas Hubbard's *How to Measure Anything*. Hubbard treats measurement as a reduction in uncertainty, not the elimination of it, and argues that the value of a measurement depends on whether it could change a decision. In practice that gives you one blunt test for any question: **what answer would change what we do?** If every plausible answer leads to the same action, skip the question or make it smaller. If you can name the answer that would flip the decision, you've found a question worth asking, and you already know how precise the answer needs to be.

:::key The value test
Before you ask a question, write down the answer that would change your decision. If you can't name one, drop the question or narrow it until you can.
:::

Hubbard also argues that intangibles such as satisfaction, flexibility or technology risk can be measured once you say what you'd observe if they changed. That's useful in B2B, where "trust in the product" or "strategic fit" often gets declared unmeasurable and then argued about forever. Ask what would be different in the world if trust were higher. Fewer manual overrides? More teams approving the feature for production? Those are observable, so they can be counted or ranged.

### Decisions across the product lifecycle

Product leaders make the same seven kinds of decision again and again, in roughly the order a product lives through them. Each has its own options, its own evidence and its own typical mistakes.

| Stage | The decision | Typical options |
|---|---|---|
| **Discover** | Which problem and segment to pursue | Pursue, park, keep exploring |
| **Invest** | Whether to fund it, how much and in what order | Fund, fund a smaller test, decline |
| **Build** | Whether to proceed with this solution | Proceed, change scope, stop |
| **Launch** | Whether to ship and how widely | Ship, widen rollout, hold, roll back |
| **Grow** | Where to invest for retention and expansion | Onboarding, adoption, expansion, partners |
| **Price** | Whether to set or change price and packaging | Change, test, grandfather, hold |
| **Retire** | Whether to sunset, migrate or keep | Sunset, migrate, extend, keep |

<figure class="fig" markdown="0">
<svg viewBox="0 0 700 330" role="img" aria-label="Seven lifecycle decisions, each feeding the same chain from decision to question to evidence to report to owner">
  <rect x="10" y="20" width="88" height="70" rx="10" class="box"/>
  <rect x="108" y="20" width="88" height="70" rx="10" class="box"/>
  <rect x="206" y="20" width="88" height="70" rx="10" class="box"/>
  <rect x="304" y="20" width="88" height="70" rx="10" class="box"/>
  <rect x="402" y="20" width="88" height="70" rx="10" class="box"/>
  <rect x="500" y="20" width="88" height="70" rx="10" class="box"/>
  <rect x="598" y="20" width="88" height="70" rx="10" class="box"/>
  <text x="54" y="48" text-anchor="middle" class="t">Discover</text><text x="54" y="70" text-anchor="middle" class="s">which problem</text>
  <text x="152" y="48" text-anchor="middle" class="t">Invest</text><text x="152" y="70" text-anchor="middle" class="s">fund or not</text>
  <text x="250" y="48" text-anchor="middle" class="t">Build</text><text x="250" y="70" text-anchor="middle" class="s">proceed or stop</text>
  <text x="348" y="48" text-anchor="middle" class="t">Launch</text><text x="348" y="70" text-anchor="middle" class="s">widen or roll back</text>
  <text x="446" y="48" text-anchor="middle" class="t">Grow</text><text x="446" y="70" text-anchor="middle" class="s">where to invest</text>
  <text x="544" y="48" text-anchor="middle" class="t">Price</text><text x="544" y="70" text-anchor="middle" class="s">change or hold</text>
  <text x="642" y="48" text-anchor="middle" class="t">Retire</text><text x="642" y="70" text-anchor="middle" class="s">sunset or keep</text>
  <line x1="54" y1="100" x2="642" y2="100" class="ln"/>
  <line x1="348" y1="100" x2="348" y2="130" class="ln"/>
  <rect x="20" y="140" width="120" height="76" rx="10" fill="var(--a1)" fill-opacity=".14" stroke="var(--a1)"/>
  <rect x="155" y="140" width="120" height="76" rx="10" class="box"/>
  <rect x="290" y="140" width="120" height="76" rx="10" class="box"/>
  <rect x="425" y="140" width="120" height="76" rx="10" class="box"/>
  <rect x="560" y="140" width="120" height="76" rx="10" class="box"/>
  <text x="80" y="170" text-anchor="middle" class="t" style="fill:var(--a1)">Decision</text><text x="80" y="192" text-anchor="middle" class="s">options, date, owner</text>
  <text x="215" y="170" text-anchor="middle" class="t">Question</text><text x="215" y="192" text-anchor="middle" class="s">what would change it</text>
  <text x="350" y="170" text-anchor="middle" class="t">Evidence</text><text x="350" y="192" text-anchor="middle" class="s">quant and qual</text>
  <text x="485" y="170" text-anchor="middle" class="t">Report</text><text x="485" y="192" text-anchor="middle" class="s">the view that answers</text>
  <text x="620" y="170" text-anchor="middle" class="t">Owner</text><text x="620" y="192" text-anchor="middle" class="s">checks and brings it</text>
  <line x1="140" y1="178" x2="155" y2="178" class="ln"/>
  <line x1="275" y1="178" x2="290" y2="178" class="ln"/>
  <line x1="410" y1="178" x2="425" y2="178" class="ln"/>
  <line x1="545" y1="178" x2="560" y2="178" class="ln"/>
  <path d="M620 216 L620 270 L80 270 L80 216" fill="none" stroke="var(--a2)" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="350" y="292" text-anchor="middle" class="s" style="fill:var(--a2)">The answer returns to the decision. If no answer could change it, the question was not worth asking.</text>
  <text x="350" y="318" text-anchor="middle" class="s">Enter at the decision, not at the dashboard.</text>
</svg>
<figcaption>Seven decision types across the lifecycle. Each one runs through the same chain: a decision with options, a question that could change it, evidence, the report that shows it, and an owner who brings the answer back.</figcaption>
</figure>

### A question bank for each decision

The tables below are a starter question bank. Each question is paired with the quantitative evidence and the qualitative evidence that answer it, and with the specific call it informs. You'll adapt the wording to your product, but most B2B decisions draw on some version of these.

Notice two patterns as you read. First, almost every question needs both kinds of evidence. Numbers tell you what is happening and how much; conversations tell you why, and whether the number means what you think it means. Eric Ries made this point in 2009 with a principle he called "metrics are people, too": trace the number back to real customers, then go talk to them. Second, the unit of analysis in B2B is usually the **account**, then the **role** within it. A feature used heavily by three large customers and ignored by four hundred others looks healthy in a total and alarming in a distribution.

**Discover.** The decision is which problem, for which segment, enters the opportunity space. Teresa Torres's opportunity solution tree (Chapter 01) gives the structure: a desired outcome at the root, customer opportunities beneath it. Discovery questions size and rank those opportunities.

| Question | Quantitative evidence | Qualitative evidence | Informs |
|---|---|---|---|
| Which pains are most frequent and most costly, and for which segment? | Support ticket themes by account tier, usage gaps, in-product search terms | Interview stories, call transcripts, win/loss notes | Which opportunity goes on the tree |
| How do customers solve it today, and what does that cost them? | Time spent on workarounds, tools and services in use | Contextual interviews, switch stories | Pursue or park |
| Who feels the pain, and who would pay to remove it? | Pain concentration by role and account size | Buying-group interviews | Target persona and buyer |

**Invest.** The decision is whether to fund the opportunity, at what size and in what sequence. Marc Andreessen defined product/market fit as being in a good market with a product that can satisfy it, so invest questions look for evidence of pull from a market worth being in.

| Question | Quantitative evidence | Qualitative evidence | Informs |
|---|---|---|---|
| How much value is at stake, as a range? | Addressable accounts, current spend on alternatives, expansion potential | Pull signals: inbound requests, pilots that convert, executives who sponsor | Fund, and at what size |
| What would we have to believe, and which belief is weakest? | Evidence attached to each assumption | The assumption map (Chapter 01) | The next test before full funding |
| How reversible is this commitment? | Contract terms, architecture and staffing commitments | Views of legal, security and the field | The evidence bar and who decides |

**Build.** The decision is whether to keep going with this solution. Marty Cagan's four big risks make a good question set: value (will customers buy or choose to use it), usability (can they figure it out), feasibility (can engineering build it with the time, skills and technology available) and business viability (does it work for sales, legal, finance and compliance).

| Question | Quantitative evidence | Qualitative evidence | Informs |
|---|---|---|---|
| Value: do design partners use it on real work, more than once? | Repeat use in the pilot, by account and role | Observed sessions, partner interviews | Proceed or rethink the solution |
| Usability: can a new user complete the core task unaided? | Task success and time on task | Usability test notes | Fix the flow before scaling |
| Feasibility: can we hit quality, speed and cost targets? | Eval results, latency, cost per task | Engineering spike findings | Change scope or architecture |
| Viability: can sales, legal, security and finance support it? | Margin model, deal desk data | Security review findings, field feedback | Proceed, add controls or stop |

**Launch.** The decision is whether to ship, widen the rollout, hold or roll back. Ron Kohavi, Diane Tang and Ya Xu call the primary success measure of an experiment its **overall evaluation criterion** (OEC), chosen to predict long-term value, and they pair it with guardrail metrics that catch harm. Chapter 05 covers experiment design. Here the point is that launch questions must be written before launch, with the thresholds that mean widen, hold or roll back.

| Question | Quantitative evidence | Qualitative evidence | Informs |
|---|---|---|---|
| Did it move the outcome metric without breaking a guardrail? | Experiment, or staged rollout against matched comparison accounts | Follow-up calls with treated accounts | Widen, hold or roll back |
| Who adopts, who doesn't, and why? | Adoption funnel by account and role | Calls with non-adopters | Product fix or enablement fix |
| What broke that we didn't predict? | Support volume and incidents per adopting account | Escalations, field reports | Pause the rollout |

In enterprise products you often have too few accounts for a clean A/B test. The fallback is a staged rollout compared with similar accounts that haven't received the change, plus a qualitative readout. It's weaker evidence, so say so in the decision memo.

**Grow.** The decision is where to invest for retention and expansion. Kerry Rodden, Hilary Hutchinson and Xin Fu's HEART framework (happiness, engagement, adoption, retention, task success) and their method of moving from goals to signals to metrics help here. In B2B, measure adoption and task success per account and per role, not only per user.

| Question | Quantitative evidence | Qualitative evidence | Informs |
|---|---|---|---|
| Which early behaviors predict retention and expansion? | Cohort retention by activation behavior | Interviews with the healthiest accounts | Onboarding changes (test causation first) |
| Why do accounts contract or churn? | Usage decline before renewal, the NRR bridge | Customer success notes, exit interviews | Retention plays and product fixes |
| Where is expansion coming from? | NRR by segment, seat and usage growth | Champion interviews | Packaging and account strategy |

**Price.** The decision is whether to set or change price and packaging (Chapter 15 covers pricing in depth). Peter van Westendorp's price sensitivity meter offers four survey questions that bracket an acceptable range: at what price is it too expensive to consider, so cheap you'd doubt the quality, getting expensive but still worth considering, and a bargain.

| Question | Quantitative evidence | Qualitative evidence | Informs |
|---|---|---|---|
| Does the value metric track the value customers get? | Billed units against customer outcomes; cases of bill shock | Buyer interviews | Choice of value metric |
| What happens to win rate, discount and margin at the new price? | Deal desk data, win/loss, gross margin per unit | Lost-deal reasons | Change, test or hold |
| What range do buyers find acceptable? | Discount distribution by segment | Van Westendorp questions, buyer interviews | Price points and tiers |

**Retire.** The decision is whether to sunset, migrate or keep (Chapter 30 covers the lifecycle mechanics). Annie Duke's *Quit* argues for deciding your quitting conditions in advance, when you can still think clearly, and that applies to sunsets in both directions: when you'll stop, and what would make you pause.

| Question | Quantitative evidence | Qualitative evidence | Informs |
|---|---|---|---|
| Who still depends on it, and what is it worth and costing? | Active accounts, ARR, support load, maintenance cost | Interviews with the top dependents | Sunset date and support level |
| What blocks migration? | Migration progress by account | Blocker interviews | Migration tooling and incentives |
| What would make us pause or extend? | Kill and pause criteria set in advance | Executive sponsor input | The sunset plan itself |

### Good questions and vanity questions

Eric Ries drew the line in a 2009 post: **vanity metrics** make you feel good but don't tell you what to do, while **actionable metrics** show clear cause and effect. His summary was blunt: "Vanity metrics: good for feeling awesome, bad for action." The examples he used were cumulative totals, numbers that can only go up. In *The Lean Startup* he added three tests for a good report, which this chapter applies to questions:

- **Actionable**: the answer shows cause and effect clearly enough that you know what to do.
- **Accessible**: the people who need to act can understand it, and it's expressed in terms of real customers and their behavior.
- **Auditable**: anyone can trace the number back to the underlying customers and records, and check it.

Vanity questions are the questions that produce vanity metrics. You can spot them with five tests:

1. **Does the answer only go up?** Totals (all users ever, all incidents touched, all agents deployed) rise with time and market size. Rewrite as a rate per account, per cohort or per period.
2. **Could any plausible answer change what we do?** If not, it's a vanity question, however interesting.
3. **Is there a comparison?** A number without a baseline, a control, a segment or a target is trivia.
4. **Can we name the customers behind it?** If you can't trace it to accounts you could call, you can't audit it and you can't learn why.
5. **Can it be gamed once it's a target?** Charles Goodhart observed in 1975 that a statistical regularity tends to collapse once it's used for control. Marilyn Strathern's 1997 phrasing became the common version: when a measure becomes a target, it ceases to be a good measure. Pair every target with a guardrail that catches the gaming.

Here's what rewriting looks like:

| Vanity question | Better question | Decision it informs |
|---|---|---|
| How many users logged in last month? | Of accounts that went live in Q2, what share have three or more weekly active users in week 8, compared with Q1's cohort? | Whether to change onboarding |
| How many AI suggestions did we generate? | What share of suggestions were accepted, by severity, and what share of accepted ones were later reverted? | Whether to widen the AI's autonomy |
| What's our pipeline for the new SKU? | In late-stage deals where the new SKU was offered, what are the win rate and discount depth compared with deals where it wasn't, and why were the losses lost? | Pricing and packaging |
| What's our NPS? | Which detractor themes appear in accounts up for renewal this half, and how much ARR do those accounts hold? | Retention priorities |

Jeff Bezos's 2016 letter to shareholders names the organizational version of this problem: **proxies**. A metric or process starts as a stand-in for something you care about, and over time people manage the stand-in instead. Survey averages and dashboards are useful proxies until they replace knowing your customers. Vanity questions are how proxies take over.

### Which report answers which question

You don't need to know how to build a report, but you do need to know which kind answers your question, so you can ask for it by name. Chapter 18 covers each report in depth; this is the map.

| Report | The question it answers |
|---|---|
| Trend over time, with a comparison band | Is it changing, and is the change bigger than normal noise? |
| Funnel | Where do accounts or users drop out between steps? |
| Cohort retention table or curve | Do newer groups stick better than older ones? |
| Segment breakdown | Is this true for everyone, or only for some accounts, roles or regions? |
| Distribution | Are a few accounts driving the total? |
| Experiment or rollout readout | Did our change cause the difference? |
| Account health and NRR bridge | Where is revenue growing, and where is it leaking? |
| Theme analysis of text | What are customers telling us in tickets, calls and reviews, and how often? |

Every one of these should state four things on its face: the population, the time window, the metric definition and the comparison. If a report you're handed doesn't, ask for them before you read the result.

### Decision quality: judge the decision, not the dice

Annie Duke built *Thinking in Bets* around a distinction most organizations blur: **decision quality is different from outcome quality**. A good decision can lose to bad luck; a bad decision can win. Duke calls judging a decision by its outcome **resulting**, and it's the default in most product reviews. The feature that worked was a great call; the one that didn't was a mistake. That habit teaches teams to avoid risk and to rewrite history.

The fix is to treat decisions as bets. State your confidence, list the possible outcomes, choose the option with the best odds and record what you knew at the time. Then, when you review the decision later, ask whether the process was sound given that information, separately from whether the result was good.

Ronald Howard and colleagues at Stanford and the Strategic Decisions Group developed a definition of decision quality with six elements, later set out by Carl Spetzler, Hannah Winter and Jennifer Meyer in *Decision Quality*:

1. An appropriate **frame**: the right problem, scope and perspective.
2. Creative, doable **alternatives**.
3. Relevant and reliable **information**.
4. Clear **values and trade-offs**.
5. Sound **reasoning**.
6. **Commitment** to action.

The framework uses a weakest-link principle: a decision is only as good as its weakest element. That's a useful corrective for this chapter. Questions and evidence improve element 3. They can't fix a bad frame or a missing alternative. A team can run excellent analysis on the wrong choice between two options when a third, better option was never put on the table.

When you review a recommendation from your team, Daniel Kahneman, Dan Lovallo and Olivier Sibony offer a complementary tool. Their 2011 *Harvard Business Review* article argues that leaders can't remove their own biases but can detect them in a team's proposal, and gives a checklist of questions to ask before approving. Among them: has the team fallen in love with the option, were dissenting views and credible alternatives explored, where did the numbers come from, and is the worst case bad enough? Use them as a review pass on your own decision memos, or ask your harness to red-team a memo against them.

### One-way doors and two-way doors

How much evidence does a decision deserve? Jeff Bezos's 2015 letter to shareholders gives the most useful answer. **Type 1** decisions are consequential and irreversible or nearly so: one-way doors. They deserve slow, careful deliberation and consultation. **Type 2** decisions are changeable and reversible: two-way doors. If you get one wrong, you don't have to live with it for long. As Bezos put it, "Type 2 decisions can and should be made quickly," by individuals or small groups with good judgment. His warning was that growing organizations drift into using the heavyweight Type 1 process for everything, which brings slowness, unthoughtful risk aversion and too little experimentation.

His 2016 letter added a rule of thumb: most decisions should be made with about 70% of the information you wish you had. Waiting for 90% usually means you're being slow, and being wrong is often cheaper than being slow if you're good at noticing and correcting mistakes. The same letter describes **disagree and commit**: when there's conviction without consensus, say you disagree, then commit fully to the decision.

Put the two ideas together and you get an evidence bar for each decision:

| | Type 2 (two-way door) | Type 1 (one-way door) |
|---|---|---|
| Examples | A feature flag, an onboarding change, a beta scope | A public price change, a platform commitment, an agent acting in production, a sunset date |
| Questions | One or two, fast | A full question brief for each critical unknown |
| Evidence | The quickest credible read | Quant and qual, with metric definitions agreed in advance |
| Decided by | The PM or the trio | A named decision forum |
| Artifact | A line in the decision log | A decision memo with a pre-mortem and kill criteria |

A skill worth practicing is converting Type 1 decisions into Type 2 ones. A staged rollout, a per-customer toggle, a grandfathering window or a pilot contract makes a one-way door partly reversible, and lowers the evidence bar to match.

:::leader For product leaders
Audit your review forums for misclassified decisions. If two-way doors are waiting weeks for a steering committee, you're paying Bezos's slowness tax. If one-way doors are being decided in a sprint review, you're taking risks nobody priced. Publish which decision types go to which forum (Chapter 29 covers governance).
:::

### Framing a question so a harness can answer it

A well-framed data question has four parts that a vague one leaves out. This book's shorthand is **PTMC**:

- **Population**: which accounts, users or records count, and which are excluded. "Paying enterprise accounts live for 60 days or more, excluding internal and trial tenants."
- **Time window**: the dates, the time zone and whether partial periods count. "Weeks starting 1 July to 30 September, UTC, complete weeks only."
- **Metric definition**: the numerator, the denominator, the unit and the filters, or the name of a governed definition everyone already agrees on.
- **Comparison**: against what. A prior period, a control group, another segment or a target.

Around those four, add the **decision** (so the harness knows what the answer is for) and the **output** you want back (including the definitions and record counts it used, so you can audit them). Anthropic's prompting guidance suggests treating a model like a brilliant new colleague who lacks context on your norms, and testing a prompt by asking whether a colleague with minimal context would be confused by it. A new analyst on day one would ask you for exactly these things. Give them up front.

:::onramp If you're new to data questions
Practice on one metric you already report. Write down its population, time window, definition and comparison in a sentence each. If you can't, or if your team gives different answers, you've found the first metric definition card to write.
:::

## How to apply it

Use this method for any decision that matters enough to write down. For a Type 2 decision it takes an afternoon and most steps shrink to a sentence. For a Type 1 decision, expect one to three weeks, most of it waiting for evidence and conversations.

1. **Name the decision.** Write the options (at least three, including "do nothing" or "keep doing what we do"), the date it must be made, who decides and whether it's a one-way or two-way door. If you can't list the options, you aren't ready to ask questions yet; go back to framing.
2. **Draft the questions that could change it.** Start from the question bank for the right lifecycle stage. Keep three to five. For each one, write the answer that would change your choice. Drop any question that fails the value test.
3. **Run the vanity tests.** Check each question for totals that only rise, missing comparisons, numbers you can't trace to accounts and targets that could be gamed. Rewrite the failures as rates, per-account measures or cohort comparisons.
4. **Define the metrics.** For every metric a question uses, find the governed definition if your company has one. If it doesn't, write a metric definition card: numerator, denominator, population, time grain, source, owner and the guardrail that catches gaming. Agree the definitions with whoever will challenge the result before you see the numbers.
5. **Plan the evidence.** For each question, list the quantitative sources, the qualitative sources and the report type that answers it. Decide the comparison now. If accounts are too few for an experiment, name the matched comparison and the qualitative follow-up you'll use instead.
6. **Ask the harness, then audit the answer.** Frame each question with population, time window, metric definition and comparison, plus the decision it serves. Ask for the definitions, filters and record counts back. Reconcile the result with a number you already trust, or ask for it two different ways. Chapter 19 covers this step in detail.
7. **Put people behind the numbers.** Pull the list of accounts behind the key result and talk to a handful: some that moved, some that didn't. This is where you find out whether the metric means what you think, and why it moved.
8. **Write the decision memo.** Lead with the recommendation. Cover the frame, the options, the evidence and your confidence in it, the trade-offs, the reasoning, the reversibility and the kill criteria. Run the bias checks against it before anyone else reads it.
9. **Decide and commit.** Bring the memo to the decision maker or forum. Record who disagreed and committed. Log the decision with its review date.
10. **Review the decision, not the dice.** On the review date, compare what happened with what you expected. Ask two separate questions: was the process sound given what we knew, and what did we learn about the world? Feed the answers back into the question bank.

Bezos's 2017 letter to shareholders describes how Amazon replaced slide presentations with narrative memos read in silence at the start of meetings. He also wrote that great memos take a week or more and "simply can't be done in a day or two." Your harness can now draft a memo in minutes. That makes step 8 faster to type and no faster to think. Spend the time it saves on rewriting.

## The AI lens

### Building AI-powered products

AI features add decisions the classic lifecycle doesn't cover, and each brings its own questions.

- **How much autonomy to grant.** "Is the AI good?" is too broad to answer. Ask instead: for which kinds of task, at what accuracy and with what consequences when wrong, should it act without a person? That needs a measure of how often outputs are accepted, a measure of how often accepted outputs later turn out to be wrong, and a breakdown by severity. Autonomy decisions that touch production or customer data are usually one-way doors for the customer, even when they're reversible for you.
- **Whether quality is good enough to ship.** For AI features, eval results are first-class evidence in the build and launch question banks, alongside usage and interviews. Chapter 31 covers evals. The question to ask is whether the eval set reflects the incidents, documents or requests your customers actually send.
- **Whether the economics hold.** Inference cost scales with usage. Every AI feature needs a cost-per-task question next to its value question, broken down by task type, because the average hides the expensive tail.
- **Which metric to target.** AI features are especially prone to Goodhart's problem. Target an automation rate and the system (or the team tuning it) will find ways to automate more, including things it shouldn't. Pair every AI target with a guardrail that measures the harm the target could cause.

AI features also create new evidence. Every accepted, edited or rejected suggestion is a labeled example of what users think good looks like. Questions such as "where do users most often edit the AI's output, and what do they change?" are some of the most useful you can ask, and the answers are sitting in your logs.

### Doing the work with AI

The infrastructure for asking data questions in plain language matured quickly. Anthropic introduced the Model Context Protocol in November 2024 as an open standard for connecting AI assistants to where data lives. In December 2025 it was donated to the Agentic AI Foundation, a fund under the Linux Foundation co-founded by Anthropic, Block and OpenAI; at that point Anthropic reported more than 10,000 active public MCP servers. Product analytics vendors now expose their reports through these connectors. Mixpanel's MCP server, for example, lets an assistant run funnels, retention, flows and other reports from a natural-language request, using each person's existing permissions. Funnels and cohort tables are things you ask for in words.

That's why the question has become the bottleneck, and why definitions matter more than ever. The vendors say so themselves. dbt Labs' semantic layer documentation describes defining each metric once so every tool uses it consistently, and states that AI tools can connect through the dbt MCP server to use those governed definitions. Snowflake's documentation for Cortex Analyst says generic AI struggles to generate correct queries from a database schema alone, because schemas lack business definitions and metric handling, and it recommends a semantic model plus evaluations against verified queries.

Public benchmarks point the same way. On the BIRD benchmark, which tests natural-language questions against real-world databases, human data engineers and students reached about 93% execution accuracy. When this chapter was written in October 2026, the top entry on the leaderboard scored about 83%. So even the best systems get some well-posed questions wrong, before you add the ambiguity of a badly posed one.

Three rules follow:

- **Name the definition or supply it.** Ask whether a governed definition exists before trusting a number. If it doesn't, put the definition in the question.
- **Make the answer auditable.** Ask the harness to show the population, filters, time window and record count it used, and to list its assumptions. Reconcile against a number you already trust.
- **Keep the decision human.** Analytics vendors now ship agents that watch metrics on a schedule and propose analyses (Amplitude's AI agents are one example). Monitoring "what changed?" is being automated. Deciding "what should we do about it?" isn't, and neither is judging whether the evidence is good enough.

:::ai The harness rule
A harness answers the question you asked and fills every gap in it with a guess. Give it the population, time window, metric definition and comparison, and ask it to show its work. Then check one number by hand before you believe the rest.
:::

When questions involve customer data, contracts or revenue, use only harnesses and connectors your company has approved for that data, and ask for aggregates rather than records about named individuals unless you need them.

## The Beacon case: questions before the keynote

:::example Where Beacon starts
Beacon Agents (supervised remediation) launch at Northlight Live in a few weeks. The product marketing manager wants a headline number for the keynote and asks you, the Principal PM, "How many incidents did Beacon touch last quarter?" At the same time, leadership has to decide whether customers can allowlist **rollback** for autonomous execution at launch, or only restarts and scaling. The hallucinated root cause that led a customer to roll back the wrong service is still fresh. Gross margin has fallen from 81% to 72% since agentic features launched.
:::

**Rewriting the keynote question.** "Incidents touched" fails three vanity tests: it only goes up, it rises with alert volume whether or not Beacon helps, and it has no comparison. You propose Beacon's North Star instead, **incidents resolved with Beacon's help per week**, reported per active account and shown with two guardrails: the wrong-action rate and the share of accepted diagnoses later contradicted by the post-incident review. It makes a smaller number and a better story, and it's one you'd be comfortable having a customer's SRE lead check.

**Naming the decision.** The rollback decision has three options: allow autonomous rollback for allowlisted services at launch, keep rollback supervised (human approval) and revisit later, or remove rollback from Agents until the diagnosis quality improves. For customers, letting an agent roll back production on its own is close to a one-way door. You classify it Type 1 and write a question brief for each critical unknown.

**The question bank for the decision.**

| Stage | Question | Evidence | Informs |
|---|---|---|---|
| Launch | Among design-partner accounts using supervised remediation for eight weeks or more, did MTTR for allowlisted incident classes fall compared with their own prior eight weeks and with matched non-pilot accounts, without a rise in the wrong-action rate? | Rollout readout by account; post-incident reviews; calls with Priya-type SRE leads | Whether Agents work well enough to widen at all |
| Build | What share of accepted diagnoses in the last 90 days were later contradicted by the post-incident review, by service type and by action proposed? | Diagnosis logs joined to review outcomes; review notes | Whether rollback suggestions are reliable enough to run unattended |
| Build | What do security reviewers need before they'd allowlist rollback? | Interviews with Sam-type reviewers; security questionnaire history | Which controls must ship first |
| Price | What is inference cost per resolved incident, by incident class? | Cost and usage records by account | Whether autonomous rollback helps or hurts the margin story |

**The metric definition card.** The second question depends on diagnosis acceptance rate, and you find three teams computing it differently. You write the card: the numerator is incidents where a responder accepted Beacon's proposed root cause; the denominator is incidents where Beacon proposed one; the population is production environments of paying customers, excluding internal and test tenants; the grain is weekly, in UTC. The guardrail is the share of accepted diagnoses later contradicted by the post-incident review. The gaming risk is an interface default that nudges responders toward "accept."

**Asking the harness.** You send the first question to your harness, which is connected to product analytics, the incident store and the CRM, with the population, window, definition and comparison spelled out, and you ask it to return the account count and filters it used. The account count is higher than the number of design partners. Trial and internal tenants had slipped in because they carry the same feature flag. You re-ask with an explicit exclusion and reconcile the corrected count against the design-partner list from customer success. The corrected answer is less flattering, and it's the one you can defend.

**What the evidence says.** In the design-partner data, supervised remediation shortened resolution for the allowlisted incident classes, and responders accepted most restart and scale-out suggestions. Rollback was different. Accepted rollback suggestions on services with shared dependencies were contradicted by post-incident reviews far more often than restart suggestions, the same pattern as the incident everyone remembers. Two security reviewers said they'd allowlist rollback only with per-action audit logs, scoped credentials and a kill switch, and one of those controls isn't ready.

**The decision memo.** You recommend option two: launch with autonomous restarts and scaling for allowlisted services, keep rollback supervised, and build a per-customer rollback toggle so the later change is a two-way door for Northlight even though it isn't one for customers. The kill criterion is written in advance: any autonomous action with customer impact pauses autonomy expansion until a review is complete. The review date is set for after Northlight Live. The product marketing manager disagrees, because autonomous rollback would make a stronger keynote demo, and commits; the memo records that. The keynote shows supervised rollback with the approval step on screen.

**The review.** When the review date comes, you'll judge two things separately: whether the process was sound given what you knew in October, and what the post-launch data says about rollback reliability. If autonomous rollback would have been fine in hindsight, that's information about the world, not evidence that the decision was wrong.

## Product 360 artifacts

```template id="17-decision-question-bank" title="Decision question bank"
# Decision question bank · [Product] · v[n] · [Date]

**Owner:** [PM]   **Reviewed with:** [analytics lead, product ops]   **Next review:** [Date]

One row per standing question. Keep the questions you ask every quarter here, with the evidence that answers them, so nobody reinvents them.

| # | Stage (Discover / Invest / Build / Launch / Grow / Price / Retire) | Decision | Question (with population, window, metric, comparison) | Quantitative evidence | Qualitative evidence | Report type | Answer that would change the decision | Owner | Verified question? (Y/N) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |

## Retired questions
| Question | Why retired (failed value test, vanity, decision no longer live) | Date |
|---|---|---|
| | | |

Rules: every question names a decision. Totals that only rise are rewritten as rates, per-account measures or cohort comparisons. A question marked "verified" has a reviewed definition and a known-good answer the harness can be checked against.
```

```template id="17-question-brief" title="Question brief"
# Question brief · [Short name] · [Date]

**Owner:** [Name]   **Reviewer:** [Name]   **Answer needed by:** [Date]

## The decision
- Decision: [what we are choosing]
- Options: 1. [ ] 2. [ ] 3. [do nothing / keep current approach]
- Decision maker or forum: [ ]
- Decision date: [ ]
- Type: one-way door (Type 1) / two-way door (Type 2). Why: [ ]

## The question
[One sentence.]

## Why it matters
- What answer would change our decision: [ ]
- What we'll do if the answer is [A]: [ ]  If [B]: [ ]
- Confidence needed to act: [for example, "a clear direction across most comparison accounts"; roughly 70% of the information we'd like is enough for Type 2]

## Framing (PTMC)
- **Population:** [who or what counts; exclusions such as internal, trial or test tenants]
- **Time window:** [dates, time zone, partial periods in or out]
- **Metric definition:** [governed definition name, or numerator / denominator / unit / filters; link the metric definition card]
- **Comparison:** [prior period / control / matched accounts / segment / target]

## Evidence plan
| Evidence | Type (quant / qual) | Source or connector | Report type | Status |
|---|---|---|---|---|
| | | | | |

## Output requested
Format: [table, chart, one paragraph]. Show the definitions, filters, time window and record counts used. List assumptions and anything that would change the answer.

## Answer
- Result: [ ]
- Reconciled against: [known number or second method]
- Accounts behind the result we spoke to: [ ]
- Confidence: low / medium / high, because [ ]
- Effect on the decision: [ ]
```

```template id="17-metric-definition-card" title="Metric definition card"
# Metric definition card · [Metric name]

**Owner:** [Name]   **Last reviewed:** [Date]   **Status:** Draft / Agreed / Governed (in semantic layer)

## Meaning
- In plain language: [one sentence a new hire would understand]
- Decision it serves: [ ]
- Good direction: up / down   **Target or threshold:** [ ]

## Formula
- Numerator: [ ]
- Denominator: [ ]
- Unit: [percent, count per account per week, currency]

## Scope
- Population: [ ]
- Exclusions: [internal, test, trial tenants; other]
- Time grain and time zone: [ ]
- Unit of analysis: [user / account / environment / incident]

## Source of truth
- Governed definition: [name in the semantic layer or metrics catalog, or "none yet"]
- Underlying sources: [systems, not tables]
- Verified question and known-good answer: [a question with an answer the team has checked, for testing harness answers]

## Integrity
- Paired guardrail metric: [the harm this target could cause, measured]
- Gaming risks: [how people or systems could move the number without moving the outcome]
- Known caveats: [seasonality, data gaps, definition changes and their dates]

## Change log
| Date | Change | Approved by |
|---|---|---|
| | | |
```

```template id="17-decision-memo" title="Decision memo"
# Decision memo · [Decision] · [Date]

**Author:** [PM]   **Decision maker:** [Name or forum]   **Type:** one-way door / two-way door   **Review date:** [ ]

## Recommendation
[Two or three sentences: what we should do, and the single strongest reason.]

## Frame
- The problem we are solving: [ ]
- In scope: [ ]   Out of scope: [ ]
- What happens if we do nothing: [ ]

## Options considered
| Option | What it means | Main upside | Main risk |
|---|---|---|---|
| 1. | | | |
| 2. | | | |
| 3. Do nothing / keep current approach | | | |

## Evidence
- What we know (with question briefs linked): [ ]
- How confident we are and why: [ ]
- What we don't know, and why we're deciding anyway: [ ]

## Values and trade-offs
[The criteria we weighed and which mattered most.]

## Reasoning
[Why this option beats the others, in prose.]

## Pre-mortem and bias check
- It's a year from now and this failed. The most likely reasons: [ ]
- Have we fallen in love with this option? Were dissenting views and credible alternatives explored? Where did the key numbers come from? Is the worst case bad enough? [answers]

## Reversibility and kill criteria
- How we could reverse or limit it: [toggle, staged rollout, contract terms]
- Kill or pause criteria, set now: [ ]

## Commitment
- Owner and resources: [ ]
- Who disagreed and committed, and on what: [ ]

## Post-decision review (complete on the review date)
- What happened: [ ]
- Was the process sound given what we knew then? [ ]
- What did we learn about the world? [ ]
- Changes to our question bank or metric cards: [ ]
```

```template id="17-vanity-question-rewrite" title="Vanity question rewrite"
# Vanity question rewrite · [Team or review] · [Date]

Run every question in a review, dashboard or deck through these five tests. Rewrite any that fail.

| # | Original question | Only goes up? | Could change a decision? | Has a comparison? | Traceable to accounts? | Gameable without a guardrail? | Rewritten question | Decision it informs |
|---|---|---|---|---|---|---|---|---|
| 1 | | Y/N | Y/N | Y/N | Y/N | Y/N | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

A question passes when it can change a decision, includes a comparison, traces to named accounts and has a guardrail if it will become a target. Totals that only rise become rates, per-account measures or cohort comparisons.
```

```template id="17-decision-review" title="Decision review"
# Decision review · [Period] · [Date]

**Facilitator:** [Name]   **Decisions reviewed:** [number]

For each decision whose review date has passed, judge the process and the outcome separately.

| Decision | Date made | Type (1 / 2) | Expected outcome and confidence | Actual outcome | Process quality (frame, alternatives, information, trade-offs, reasoning, commitment: weakest link) | Decision or dice? | Lesson | Change to question bank |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## Patterns
- Two-way doors that waited too long: [ ]
- One-way doors decided too lightly: [ ]
- Questions that kept failing the value test: [ ]
```

## Prompts

```prompt title="Build a question bank for a decision"
Goal: Turn a pending decision into three to five questions that could change it, each with the evidence that answers it.
Paste in: the decision, its options, the decision date, who decides, and a short description of the product and its customers.

I'm a product manager deciding [decision] for [product]. The options are [options, including do nothing]. The decision is due [date] and [person or forum] decides.

1. Classify the lifecycle stage (discover, invest, build, launch, grow, price, retire) and say whether this is a one-way door or a two-way door, with your reasoning.
2. Propose up to eight candidate questions. For each, state the answer that would change the decision. Drop any question where every plausible answer leads to the same choice, and tell me which you dropped and why.
3. For the three to five questions that remain, give: the quantitative evidence, the qualitative evidence, the report type that would show it (trend, funnel, cohort, segment breakdown, distribution, experiment readout, NRR bridge or theme analysis) and the population, time window, metric definition and comparison it needs.
4. Use accounts and roles as the unit of analysis where it matters, not only users.

Don't invent data or results. Where you're unsure what data exists, say what I should check.

Check the output: for each question, read the "answer that would change the decision" aloud. If it doesn't actually flip the choice, cut the question. Make sure at least one question has qualitative evidence you'll gather by talking to customers.
```

```prompt title="Rewrite vanity questions"
Goal: Replace questions that produce feel-good numbers with questions that inform decisions.
Paste in: the questions or metrics from a dashboard, review deck or status update.

Review these questions and metrics from [team or review]. For each one, test:
- Does the answer only go up over time (a cumulative total)?
- Could any plausible answer change a decision? Which decision?
- Is there a comparison (prior period, control, segment, target)?
- Can the number be traced to named accounts we could call?
- If it became a target, how could it be gamed, and what guardrail would catch that?

Then rewrite each failing question as a rate, a per-account measure or a cohort comparison, and name the decision it informs. Keep any question that passes and say why.

[questions or metrics]

Check the output: confirm each rewrite names a real decision your team makes. If a rewrite needs data you don't collect, decide whether the question is worth instrumenting or should be answered qualitatively.
```

```prompt title="Frame a data question for the harness"
Goal: Get an answer you can audit, not just a number.
Paste in: the question brief (decision, question, population, time window, metric definition, comparison). Run it in a harness connected only to approved data sources.

I'm deciding [decision] by [date]. Answer this question: [question].

- Population: [who counts; exclude internal, trial and test tenants and anything else listed]
- Time window: [dates, time zone; complete periods only unless stated]
- Metric: use the governed definition [name] if it exists. If not, use: numerator [ ], denominator [ ], unit [ ], filters [ ]. Tell me which you used.
- Comparison: [prior period / matched accounts / control / segment / target]

Return:
1. The answer in a short table, with the comparison.
2. The exact population, filters, time window and record counts you used.
3. Any assumptions you made where my instructions were ambiguous.
4. The list of accounts behind the result, so I can follow up with some of them.
5. What would most likely change this answer.

If the data can't answer the question as framed, say so rather than approximating silently.

Check the output: compare the record count with a number you already trust (for example, the count of design partners or paying accounts). Ask for one key figure a second way. If the population is wrong, fix the framing and re-ask before reading the result.
```

```prompt title="Draft a metric definition card"
Goal: Find out how a metric is really being calculated across the company, and agree one definition.
Paste in (or connect the harness to): dashboards, reports, decks and documents that mention the metric, plus any semantic-layer or metrics-catalog entry for it. Use a harness your company has approved for internal business data.

Find every place [metric name] is defined or reported in the material provided. For each, extract the numerator, denominator, population, exclusions, time grain and source, and quote the definition with its location.

Then:
1. Show where the definitions differ, and how much each difference could change the number.
2. Propose one definition as a metric definition card: plain-language meaning, decision it serves, formula, population and exclusions, time grain and time zone, source of truth, owner, paired guardrail metric, gaming risks and known caveats.
3. List the people or teams who'll need to agree to the change.

Don't choose a definition because it produces a better-looking number.

Check the output: open two of the cited sources and confirm the extracted definitions. Circulate the card to the teams that use the metric before you use it in a decision.
```

```prompt title="Red-team a decision memo"
Goal: Find the weakest link in a decision before the decision forum does.
Paste in: the decision memo and the question briefs behind it. Remove confidential details your tool isn't approved for.

Act as a skeptical reviewer of this decision memo. Assess it in two passes.

Pass 1, decision quality. Rate each element as strong, adequate or weak, with a reason: the frame, the alternatives, the information, the values and trade-offs, the reasoning and the commitment. Name the weakest link, since a decision is only as good as its weakest element.

Pass 2, bias check. For each, say whether the memo shows signs of it and quote the passage: self-interest, falling in love with the option, groupthink or missing dissent, an overly convenient analogy, missing credible alternatives, anchoring on a number of unclear origin, an overly optimistic base case, a worst case that isn't bad enough, and excessive caution.

Then list the three questions the decision maker is most likely to ask, and whether the memo answers them.

Don't rewrite the memo. Don't soften the critique.

[memo and question briefs]

Check the output: fix the weakest link first, even if it isn't the easiest. If the review says an alternative is missing, add it to the options table rather than arguing it away.
```

```prompt title="Set the evidence bar for a set of decisions"
Goal: Stop treating every decision as a one-way door, or every one-way door as routine.
Paste in: a list of pending decisions with a line of context each (from a roadmap review, planning doc or decision log).

For each decision below, classify it as a one-way door (consequential and hard to reverse) or a two-way door (changeable and reversible), from the perspective of both our company and our customers. For each:
1. Explain the classification in one sentence.
2. Recommend the evidence bar: number of questions, quantitative and qualitative evidence, who decides and which artifact (decision log line or full memo).
3. For each one-way door, suggest a way to make it more reversible (staged rollout, per-customer toggle, pilot terms, grandfathering) and how that would change the evidence bar.
4. Flag any two-way door that appears to be waiting on a heavyweight process.

[decisions]

Check the output: challenge any one-way door the model classified as reversible only for us. If customers can't easily undo it, treat it as Type 1.
```

```prompt title="Run a decision review"
Goal: Learn from past decisions without judging them by their outcomes alone.
Paste in: decision memos or decision-log entries whose review dates have passed, with what actually happened. Use a harness approved for confidential business data.

For each decision:
1. Summarize what was expected at the time, with the stated confidence and the evidence available then.
2. Summarize what happened.
3. Assess the process separately from the outcome: given only what was known then, was the frame right, were the alternatives adequate, was the information relevant and reliable, were trade-offs clear, was the reasoning sound and was there commitment? Name the weakest element.
4. Classify the result: good decision and good outcome, good decision and bad outcome, bad decision and good outcome, or bad decision and bad outcome. Explain.
5. Suggest changes to our question bank or metric definitions based on what we learned.

Use only information that existed at the decision date when judging the process. Mark anything you can't determine.

[memos and outcomes]

Check the output: look hardest at "bad decision, good outcome," because a lucky result hides the flaw and the team is likely to repeat the process. Confirm the model judged the process only on information dated before the decision.
```

## Anti-patterns

:::warn Dashboard-first questions
The team opens a dashboard, sees a line move and spends a week explaining it. No decision was waiting on the answer. Start from a named decision and the answer that would change it; treat unexplained movement as a monitoring alert, not a research project.
:::

:::warn Totals in the keynote
"Our agents have handled a million tasks." The number only goes up, it grows with the market whether or not the product helps, and no customer can check it. Lead with a rate per account, against a comparison, with its guardrail beside it.
:::

:::warn The undefined metric
Three teams report "acceptance rate" with three definitions, and the harness picks whichever table it finds first. Each answer is internally consistent and they don't agree. Write the metric definition card, put it in the governed layer, and name it in every question.
:::

:::warn Resulting
A launch that worked becomes proof the decision was brilliant; a launch that missed becomes someone's mistake. Teams learn to avoid risk and to rewrite what they knew. Review decisions against the information available at the time, and record that information in the memo when you decide.
:::

:::warn One process for every door
Every decision goes to the same steering committee with the same deck. Reversible decisions wait for weeks, and irreversible ones get the same light touch as everything else. Classify each decision and match the evidence bar and the forum to it.
:::

:::warn Numbers without people
The analysis is rigorous and nobody has spoken to a customer behind it. The metric moved because one large account changed its configuration, or because trial tenants slipped into the population. Pull the account list behind every important result and call some of them.
:::

## Checklist

- [ ] Every analysis request names a decision, its options, its date and its decision maker.
- [ ] Each decision is classified as a one-way or two-way door, and the evidence bar matches.
- [ ] Each question states the answer that would change the decision.
- [ ] Questions are checked against the five vanity tests, and totals are rewritten as rates, per-account measures or cohort comparisons.
- [ ] Every data question specifies population, time window, metric definition and comparison.
- [ ] Every metric used in a decision has a definition card or a governed definition, with a paired guardrail.
- [ ] Each question has both quantitative and qualitative evidence, or a stated reason why one is enough.
- [ ] Harness answers show their population, filters and record counts, and at least one number is reconciled against a trusted source.
- [ ] Someone has spoken to customers behind the key results.
- [ ] One-way doors have a decision memo with options, evidence, trade-offs, a pre-mortem, kill criteria and a review date.
- [ ] Dissent is recorded, and disagree-and-commit is explicit.
- [ ] Decisions are reviewed on their review dates, judging process separately from outcome.
- [ ] The decision question bank is updated after each review.

## Key takeaways

- With an AI harness that can query almost anything, the scarce skill is asking the right question. Start from a named decision and ask only what could change it.
- Each lifecycle stage (discover, invest, build, launch, grow, price, retire) has its own decision and its own standard questions. Answer each question with both numbers and conversations, and use the account as the unit of analysis in B2B.
- Vanity questions produce totals that only rise, lack a comparison or can't be traced to customers. Rewrite them as rates, per-account measures and cohort comparisons, and pair every target with a guardrail.
- Frame every data question with population, time window, metric definition and comparison, and ask the harness to show its definitions and record counts so the answer is auditable.
- Match the evidence bar to reversibility. Decide two-way doors quickly with partial information; give one-way doors a full memo, kill criteria and a review date, and look for ways to make them reversible.
- Judge decisions by their process as well as their outcomes. Record what you knew when you decided, so later reviews can separate the decision from the dice.
