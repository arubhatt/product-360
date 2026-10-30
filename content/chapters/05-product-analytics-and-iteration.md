<p class="lead">Launch is when your product hypothesis meets real behavior at scale. This chapter covers how to instrument a product so that behavior is legible, how to read activation, retention and funnels without fooling yourself, when a controlled experiment is the right tool and when it isn't, and how to turn what you learn into the next iteration.</p>

## Why this matters

Chapter 01 ended with a hypothesis and a falsifying signal: "we'll know we're right when..." Shipping doesn't answer that question. It makes an answer possible, and only if someone decided in advance what to measure, built the measurement before launch and looked at it honestly afterward. Skip any of those steps and the launch gets called a success because nobody can prove otherwise.

Three things make this harder in B2B, enterprise and platform products than the consumer playbooks admit.

**Volume is low.** A consumer app with millions of daily users can test a button and get a clean answer in a week. An enterprise product with a few hundred customer accounts can't. Ron Kohavi and Stefan Thomke, writing in Harvard Business Review in 2017, put the practical floor for online experiments at a few thousand daily active users. Many enterprise products sit below that, and almost every account-level decision does.

**The unit is the account.** One customer has an admin who installs, a lead who configures, users who use and an executive who renews. A funnel that counts only people can't tell you why accounts stall.

**More usage can be bad news.** An on-call engineer who spends forty minutes in an incident tool at 3 a.m. had a bad night, and a metric that rewards time spent will call it a win.

AI features add a fourth problem. Their quality varies by input, drifts as models and prompts change, and can't be fully proven before launch. Post-launch analytics is where you find out whether the AI is right often enough in the wild, and whether people accept its output because it's correct or because it sounds confident.

This chapter builds the core of the Measure dimension of your Product 360 (Chapter 02 sets the North Star and metric tree it hangs from): instrumentation, core analytics, fit signals, measurement frameworks, experimentation and the iteration loop.

## Instrumentation and event design

### Start from questions

The most common instrumentation failure is tracking everything a developer could think of, then finding six months later that none of it answers the question leadership is asking. Work backward instead.

Amplitude's data-planning playbook sets out a three-step order: define the business objectives, break each key metric into the critical paths and actions behind it, and only then design events and properties. The Goals, Signals, Metrics process that comes with HEART (below) reaches the same order from the user-experience side. An event exists because a question needs it.

Before you name a single event, write the five to ten questions the launch must answer. "Are new accounts reaching first value within two weeks?" "Do responders accept the agent's diagnosis?" "Where do admins abandon connector setup?" Each question points to a metric, and each metric to a small set of events. Anything left over is a candidate for deletion.

### Naming and properties

A widely used convention, codified in Twilio Segment's naming guidance, is **Object Action**: the thing acted on plus a past-tense verb, from the user's point of view. "Incident Opened," "Diagnosis Accepted," "Connector Installed." Segment recommends Proper Case for event names and snake_case for properties, and says consistency matters more than which convention you pick. Amplitude adds a warning: differently capitalized names become different events, so "diagnosis accepted" and "Diagnosis Accepted" quietly split your data.

Three rules do most of the work:

- **Put variable detail in properties, never in names.** One "Order Completed" event with a payment-method property beats a family of near-duplicates. A name that embeds an ID or a customer creates an unbounded list of events nobody can analyze.
- **Avoid events so generic they answer nothing.** "Page Clicked" tells you activity happened, not what the person was trying to do.
- **Separate event properties from user and account properties.** Event properties describe one occurrence (which diagnosis, what confidence). User properties describe who did it and persist (role, plan). In B2B, add account and, where relevant, workspace or partner properties.

### B2B and platform additions

Identity in an enterprise product has at least three levels: user, account and often a workspace or tenant. A partner or managed service provider may sit above several accounts. Most questions you'll be asked are account-level ("how many accounts reached first value this quarter?"), so every event needs an account identifier. Check that it does before launch.

Two more additions matter for platform and AI products. Log **actor type** (human, agent or automation) whenever a machine can trigger the same action as a person; otherwise an agent that starts acting looks like a surge in user engagement. And fire events that feed revenue or trust metrics **from the server**, where a browser can't block them; client events are fine for interface behavior.

### The tracking plan as a contract

The **tracking plan** lists every event, exactly when it fires, its properties and types, the question it answers, the metric it feeds and its owner. Segment describes it as a living document that tools can validate incoming data against. Engineering implements it, data validates it, product owns what it means. When a dashboard number looks wrong, start there.

Add a privacy column. The security reviewer will ask what leaves the customer's environment. Properties should never carry customer content (log lines, ticket text, prompts) or personal data without a documented reason and an approval.

:::onramp If instrumentation is new to you
Pick one critical path, such as signup to first value. Write the three to five events that mark its steps, name each as Object plus past-tense Action, list the properties you'd need to slice it by account and role, and review it with an engineer before the sprint starts.
:::

## Core analytics: activation, engagement, retention, funnels

### Activation

**Activation** is the moment a new user or account first gets real value. Dave McClure's pirate metrics call it a happy first visit; in enterprise products it's rarely a visit and never a login. Define it as a specific completed action that delivers the outcome the customer bought. The HEART authors note that "using" a product can be defined as completing a key task, which is the right instinct.

In B2B, activation usually belongs to the account and takes several people: the admin connects the data sources, the lead configures the workflow, a user completes the core task once. Track time to activation as well as the rate, because a slow path to first value is where enterprise deals turn into shelfware.

### Engagement

**Engagement** measures frequency, intensity or depth of use over a period. Kerry Rodden, Hilary Hutchinson and Xin Fu recommend reporting it as an average per user, never as a total, because totals rise with headcount. Their Gmail example is the model: the share of active users who visited on five or more days in the past week, which they found strongly predictive of longer-term retention.

The same authors warn that engagement may not be meaningful in an enterprise context where people use the product as part of their job, and suggest focusing on happiness or task success there. For an incident tool, an approval workflow or a compliance product, less time spent can be the goal.

### Retention cohorts and curves

**Retention** is the share of users or accounts from one period still active in a later one. A **cohort** is a group that started in the same period, and a cohort retention curve plots the share of each cohort still active after one, two, three periods. Eric Ries advises always looking at cohort-based metrics over time. Total active users can rise for months while every new cohort churns faster than the last, because acquisition hides the decline; cohorts expose it.

Sequoia's data science team describes three shapes worth recognizing on sight:

- **Declining to zero.** Every cohort eventually leaves. The product hasn't found a group for whom it's essential.
- **Flattening.** The curve drops early, then levels off. A core keeps coming back, and a higher plateau is healthier.
- **Smiling.** The curve dips and then rises as churned users return.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 330" role="img" aria-label="Three retention curve shapes: declining to zero, flattening, and smiling">
  <rect x="70" y="20" width="550" height="250" rx="8" class="box"/>
  <line x1="90" y1="250" x2="600" y2="250" class="ln"/>
  <line x1="90" y1="40" x2="90" y2="250" class="ln"/>
  <path d="M90 50 C 160 140, 230 200, 320 228 S 520 248, 600 249" fill="none" stroke="var(--a3)" stroke-width="3"/>
  <path d="M90 50 C 150 130, 210 160, 300 168 S 500 172, 600 172" fill="none" stroke="var(--a1)" stroke-width="3"/>
  <path d="M90 50 C 150 130, 220 170, 300 178 S 470 150, 600 128" fill="none" stroke="var(--a2)" stroke-width="3"/>
  <text x="605" y="232" text-anchor="end" class="s" style="fill:var(--a3)">Declining to zero: no fit yet</text>
  <text x="605" y="162" text-anchor="end" class="s" style="fill:var(--a1)">Flattening: a core keeps returning</text>
  <text x="605" y="116" text-anchor="end" class="s" style="fill:var(--a2)">Smiling: churned users come back</text>
  <text x="345" y="290" text-anchor="middle" class="s">Periods since the cohort started (match the window to natural usage)</text>
  <text x="40" y="150" text-anchor="middle" class="s" transform="rotate(-90 40 150)">Share of cohort still active</text>
  <text x="100" y="40" class="t">100%</text>
</svg>
<figcaption>Read the shape before the number. A flattening curve is behavioral evidence that a core of customers has found value; a curve heading to zero means acquisition is filling a leaky bucket.</figcaption>
</figure>

Two choices decide whether a retention curve means anything. The **window** must match how often people naturally need the product: weekly for a daily tool, monthly or per incident for something used in bursts. And "active" must mean a **meaningful event** (Sequoia's example is a completed ride, not an app open). For bursty, event-driven products, normalize by opportunity: an account with no incidents this week had a quiet week, so "share of incidents touched by the product" is fairer than weekly active users.

In B2B, read retention at two layers. Logo retention and net revenue retention arrive at renewal, so they lag. Product retention, the share of an account's eligible work that runs through your product cohort by cohort, leads; it can warn you about a renewal two quarters early.

### Funnels

A **funnel** is an ordered set of steps with the conversion rate between each pair. It shows where people drop out; recordings, tickets or a conversation with the people who dropped tell you why.

Enterprise funnels cross people and time. The admin installs a connector, the lead configures rules a week later, an on-call engineer uses the result a week after that. Build these funnels at account level, measure the time between steps as well as the conversion, and attribute each step to the role that owns it.

:::key Pick the unit before you pick the metric
For every metric, write down whether it counts users, accounts or units of work (incidents, tickets, deployments). Most arguments about whether a number is good turn out to be two people using different units.
:::

## Product-market fit signals

Fit shows up in what people say about losing a product and in what they do over time. Use both.

### The Sean Ellis test

Sean Ellis's survey asks users how they would feel if they could no longer use the product: very disappointed, somewhat disappointed or not disappointed. As Rahul Vohra reported in First Round Review in 2018, Ellis benchmarked nearly a hundred startups and found that those struggling for traction almost always had fewer than 40% answering "very disappointed."

Vohra's account of using the test at Superhuman is more useful than the threshold. Superhuman started at 22% very disappointed. Narrowing its focus to the kinds of people who answered "very disappointed" raised the number to 33% for that segment, and after roughly three quarters of focused work it reached 58%. Vohra added three questions (what type of people would most benefit, what is the main benefit, how could the product improve) and segmented the answers: profile the high-expectation customer from the very disappointed group, study the somewhat disappointed who value the same main benefit because they're the most convertible, and set aside feedback from the not disappointed.

In B2B, adapt it three ways. Survey active users inside active accounts and report the respondent count, because a few dozen answers are directional. Segment by persona, because the daily user and the champion experience the product differently. And ask the economic buyer about renewal intent and the business case instead, since the buyer doesn't use the product.

### Retention flattening

The behavioral counterpart is the flattening cohort curve. A survey measures attitude at one moment; a curve that levels off shows a core of customers choosing the product week after week. When the two disagree, investigate. A high Ellis score with a declining curve often means only the enthusiasts answered. A flattening curve with a low score can mean use is mandated rather than valued, which shows up at renewal.

## Measurement frameworks: AARRR and HEART

### AARRR pirate metrics

Dave McClure's **AARRR** framework, named for the sound a pirate makes, describes five stages of a customer's life with a product:

| Stage | McClure's definition | B2B reading |
|---|---|---|
| **Acquisition** | Users come to the product from channels | Pipeline, often sales-led or partner-led |
| **Activation** | They have a happy first visit | The account reaches first value |
| **Retention** | They come back | The account keeps running its work through the product |
| **Referral** | They like it enough to tell others | References, case studies, partner recommendations |
| **Revenue** | They pay | Contract value, expansion and net revenue retention |

The useful part for a senior PM is the order. If activation and retention are weak, acquisition spend fills a leaky bucket. When leadership asks for more pipeline, AARRR shows where the leak is.

### HEART and Goals, Signals, Metrics

Rodden, Hutchinson and Fu developed **HEART** at Google and published it at the CHI conference in 2010:

- **Happiness**: attitudes such as satisfaction, perceived ease of use and likelihood to recommend, tracked with a well-designed recurring survey.
- **Engagement**: frequency, intensity or depth of use per user over a period.
- **Adoption**: new users of a product or feature in a period.
- **Retention**: the share of one period's users still present in a later one.
- **Task success**: efficiency (time to complete), effectiveness (share completed) and error rate.

They built HEART to complement what they called **PULSE** metrics (page views, uptime, latency, seven-day active users and earnings), which run the business but are indirect and easy to misread as measures of experience: more page views can mean people are lost.

For each category you use, write the **Goal** (what the feature should achieve for the user), the **Signals** (behaviors or attitudes that would show success or failure, and whether they're logged) and the **Metrics** (signals normalized into rates or per-user averages, with automated traffic filtered out). The authors note that failure signals such as abandonment or undo are often easier to detect, and that you shouldn't use every category every time. In enterprise products, Task success and Happiness usually carry the weight; Engagement may be the row you leave blank on purpose.

One more lesson from the paper applies to every launch. After a redesign of iGoogle, satisfaction dropped and then recovered as users adjusted. The authors call this **change aversion**. Read the trend over enough weeks to see past an early dip.

| Use | When |
|---|---|
| AARRR | Explaining the whole customer lifecycle and where the biggest leak is |
| HEART with Goals, Signals, Metrics | Choosing metrics for a specific product or feature |
| PULSE | Running the business and the service; never alone to judge a feature |

## Experimentation

### What a controlled experiment is

A **controlled experiment** (an A/B test) randomly splits users between a control, which sees the current experience, and one or more treatments, which see the change. Because the split is random, a difference in outcome beyond chance is caused by the change. No dashboard can give you that causal claim.

Ron Kohavi, Randal Henne and Dan Sommerfield's 2007 KDD paper, subtitled "Listen to Your Customers not to the HiPPO" (the highest paid person's opinion), set out the practice that Kohavi, Diane Tang and Ya Xu expanded in their 2020 book *Trustworthy Online Controlled Experiments*.

### The OEC and guardrails

The **Overall Evaluation Criterion (OEC)** is a quantitative measure of what the experiment is trying to achieve. Kohavi and his co-authors recommend agreeing on a single metric, possibly a weighted combination of objectives, because it forces the tradeoffs to be made once, before the test. They also warn against short-term OECs: long-term goals such as repeat use belong inside the definition.

**Guardrail metrics** must not get worse even if the OEC improves: latency, error rates, cost, trust signals, revenue. Kohavi, Tang and Xu treat them as a distinct class of metric. Declare them before the test starts; a treatment that lifts the OEC and breaks a guardrail doesn't ship.

### How experiments go wrong

**Sample ratio mismatch (SRM).** If you configured a 50/50 split and the groups came out meaningfully uneven, something in assignment, logging or analysis is broken, and the result can't be trusted until you find it. Microsoft's experimentation team detects SRM with a chi-square test at a strict threshold (p below 0.0005) to limit false alarms, and reported in 2020 that about 6% of its A/B tests showed one. Causes range from assignment and execution to log processing, analysis and experimenter actions such as an uneven ramp-up. No readout should go out without an SRM check.

**Peeking.** Significance levels assume a sample size fixed in advance. Check the dashboard daily and stop the moment it shows significance, and your false positive rate climbs far above the nominal 5%. Evan Miller's 2010 illustration showed a change that does nothing reaching "significance" 26.1% of the time under stop-at-first-significance. Fix the sample size and duration in advance, or use a sequential method designed for repeated looks, and run whole weeks.

### What experiments can't tell you

The 2007 paper lists the limits. Experiments tell you which variant won and by how much, never why; that needs qualitative research. They usually run a few weeks, so they see short-term effects. **Primacy and newness effects** (people reacting to change itself) can mislead early results, so some tests must run several weeks or measure new users only. The feature has to be built well enough to test. And users may notice they see something different from colleagues, which matters in B2B, where teammates compare screens.

Expect most ideas to fail. Kohavi and Thomke reported that only about 10% to 20% of experiments at Google and Bing produce positive results, and that across Microsoft roughly a third are positive, a third neutral and a third negative. If every readout your team writes is positive, look at how the tests are chosen, run and reported.

### When not to A/B test

Skip the controlled experiment when:

- **Volume is too low.** Work out the minimum detectable effect first. With hundreds of accounts it's often larger than any plausible result; if so, don't start.
- **Units interfere.** Teammates in one account share work, so if one sees the treatment and another the control, behavior leaks across. Randomize by account or not at all.
- **The change is contractual.** Pricing, terms and entitlements differ by customer only through negotiation.
- **Safety is at stake.** Don't randomize whether a risky automated action runs.
- **The decision is cheap and reversible.** Ship it, watch the guardrails, roll back if needed.

### Alternatives, from stronger to weaker evidence

When a clean test isn't possible, you still want causal evidence. For each option below, ask the same question: what else could explain this change?

| Method | How it works | Assumption you're making |
|---|---|---|
| Account-level randomized pilot | Pair similar accounts, randomize one of each pair | Pairs are truly similar; enough pairs to see an effect |
| Staged rollout with a holdout | Roll out in waves; keep a random set of accounts back | The holdout stays untouched and comparable |
| Before and after with a comparison group | Compare the change in exposed accounts with similar unexposed ones | Both groups would have moved together without the change |
| Interrupted time series | Look for a break in a long, stable trend at launch | Nothing else changed at the same moment |
| Pre-period adjustment (CUPED) | Use each unit's pre-experiment behavior to reduce noise | Pre-period behavior predicts the outcome |
| Offline replay (AI features) | Run the new model on past cases and grade the results | Past cases represent future ones |
| Design-partner evidence | Structured interviews and observation with a few customers | Partners resemble the wider base |

CUPED, published in 2013 by Alex Deng, Ya Xu, Ron Kohavi and Toby Walker, uses data from before the experiment to strip out variance unrelated to the treatment. On Bing it cut variance by about half: the same statistical power with half the users or half the time. For a low-volume B2B product, that can decide whether a test can conclude at all. You don't need the math. Ask your data partner or your AI harness whether a pre-period adjustment is available and what it does to the minimum detectable effect.

## The iteration loop

### Build, measure, learn

Most PMs know Eric Ries's Build-Measure-Learn loop. Fewer remember his emphasis: minimize the total time through the loop, including measuring and learning. Plan it backward. Decide what you need to learn, then what you'd measure to learn it, then the least you'd build to get that measurement.

Ries defined **innovation accounting** as three milestones: establish the baseline (measure how customers behave with what exists), tune the engine (run experiments to move the metrics toward the ideal) and decide whether to pivot or persevere (when experiments stop producing gains). He set three tests for the metrics behind those calls: **actionable** (cause and effect are clear enough to act on), **accessible** (people can understand and reach them) and **auditable** (people can trace them to the underlying data). His shorthand for scope is worth keeping: split-test the small, measure the large. Interface and copy changes suit experiments; large bets, such as an agent that takes actions, are judged by cohorts and milestones over time.

### Validating the hypothesis after launch

Launch moves the product hypothesis from untested to testable. The **post-launch review** tests it. Hold it at a point you named before launch (often 30, 60 or 90 days, depending on the usage cycle) and answer, assumption by assumption, whether the evidence says validated, invalidated or unclear. Compare against the success criteria written before launch. Criteria written afterward will always find a way to call the launch a win.

### Planning the next iteration

The **iteration plan** turns the review's open assumptions into the next tests. For each, write the next experiment or measurement, the evidence that would change your mind, an owner, a date and an explicit stop condition, and tie it to a dashboard metric. Without stop conditions, the plan is just a backlog.

## How to apply it

This method runs from about four weeks before a launch to the first iteration decision after it. For a feature, the same steps fit into a sprint or two.

**Before launch: decide what you'll believe.**

1. **Restate the hypothesis and success criteria.** Take the solution hypothesis from Chapter 01 and the North Star and input metrics from Chapter 02. Write down, with numbers and a date, what result would mean validated, invalidated and unclear, and get your manager and engineering lead to agree in writing.
2. **Write the questions.** List the five to ten the launch must answer, including at least one each on activation, task success or quality, retention and a guardrail.
3. **Draft the tracking plan.** Map each question to a metric, events and properties. Use Object Action names, put the account identifier on every event, log actor type wherever an agent can act, and add a privacy note to every property.
4. **Fill in a HEART grid** with goals, signals and metrics. Leave rows blank on purpose and say why.
5. **Spec the dashboard.** North Star at the top, three to five inputs, guardrails, definitions (numerator, denominator, window, unit) and the action each chart should trigger. Cut any chart that doesn't connect to a decision.
6. **Choose how you'll get causal evidence.** If volume supports an A/B test, write the experiment design doc now. If it doesn't, pick the strongest alternative (usually a staged rollout with a holdout) and write down its assumption.
7. **Validate instrumentation before launch.** Run the critical paths in a test environment and check every event against the plan. Data lost in the launch window doesn't come back.

**First weeks after launch: watch, don't conclude.**

8. **Check data quality daily for the first week**: event volumes by account, missing properties, duplicates, and the sample ratio if an experiment is running.
9. **Watch guardrails, not the OEC.** A guardrail breach justifies a rollback at any time. The OEC waits for the planned duration.
10. **Collect the why in parallel.** Talk to five to ten users in the rollout, read support tickets and, for AI features, read real traces.

**At the review point: decide.**

11. **Write the readout or post-launch review**: validity first, then the primary result with its uncertainty, guardrails, segments (labeled pre-registered or exploratory) and qualitative evidence.
12. **Call each assumption** validated, invalidated or unclear against the criteria from step 1. "Unclear" is an honest verdict; it means the next iteration must produce better evidence.
13. **Run a fit check if the product is new**: the Ellis survey by persona, next to the retention cohorts.
14. **Write the iteration plan**, with a stop condition for every item and a dated pivot-or-persevere checkpoint.
15. **Record the decision** (ship, iterate or kill) in the decision log, and update the Measure dimension of your Product 360 with the current tracking plan, dashboard spec and readout.

:::leader For product leaders
Ask for the success criteria before launch, not the dashboard after it. Give nulls and negatives the same airtime as wins; if only positive results reach your staff meeting, your teams will learn to find them. Fund instrumentation as part of the feature, because a follow-up ticket for it rarely gets prioritized.
:::

## The AI lens

### Measuring AI-powered products in production

An AI feature that passed its offline evals (Chapter 31) still needs measuring after launch. Production inputs are messier than any eval set, and models, prompts and retrieval sources change underneath you. Anthropic's January 2026 guidance on evaluating agents describes layers (automated evals, production monitoring, A/B tests, user feedback, transcript review and human studies) and argues that no single layer catches every problem. Post-launch analytics is the production half of that stack.

**Behavioral signals of quality.** The user's response to an AI output is your richest quality signal. Instrument each as an event: accepted, edited or rejected (with a reason if you can ask cheaply); the size and type of corrections; reversions of an accepted output, which for agents that act is the most important failure signal you have; regenerations and retries; escalation back to the manual path; and time to complete the task with and without AI on similar cases.

**Acceptance is necessary and insufficient.** Albert Ziegler and colleagues' 2022 study of GitHub Copilot found that the acceptance rate of suggestions tracked developers' perceived productivity better than whether the accepted code persisted. That makes acceptance a strong signal of perceived value. It says nothing direct about correctness. A confident, plausible, wrong answer gets accepted too, and that's the failure that hurts customers most. Pair every acceptance metric with a correctness signal: reversions, downstream outcomes or graded samples.

**Consistency for agents.** Anthropic's guide distinguishes pass@k (at least one success in k tries) from pass^k (success on all k). An agent that succeeds 75% of the time on one try succeeds three times in a row only about 42% of the time. Users of an agent acting on production systems experience every run, so pass^k is the honest view.

**Error analysis on real traces.** Hamel Husain and Shreya Shankar put error analysis at the center of AI evaluation: collect representative production traces, have a domain expert write free-text notes on what went wrong, group the notes into a failure taxonomy, count each mode, and repeat until new traces stop revealing new failures. They suggest reviewing at least 100 traces and annotating about 30 yourself before letting an AI assistant suggest categories. One domain expert is the final voice on quality, and binary pass or fail checks built from your own failure modes replace generic scores and 1 to 5 scales. After an AI launch, block an hour a week for it.

**Cost, latency and context.** Inference cost per completed task belongs on the dashboard next to quality, because a feature can improve one and destroy margin at the same time; latency belongs among the guardrails. Every AI event should carry the model version, prompt or agent version, number of retrieved sources, tool calls, latency, cost and the human decision that followed. OpenTelemetry maintains an evolving set of semantic conventions for generative AI (spans, metrics, events and MCP calls) that lets engineering traces and product events share identifiers, so you can go from a product metric to the exact traces behind it.

**Model changes are product changes.** Where volume allows, run a model or prompt swap as an experiment with quality, cost and latency as guardrails. Where it doesn't, replay past cases offline first, then stage the rollout with a holdout.

### Doing the work with AI

In 2026 much of this work can happen through questions to an AI harness connected to analytics, warehouse, ticketing and CRM tools, often through MCP connectors that analytics vendors now provide. The harness drafts a tracking plan from a PRD, checks new events against the taxonomy for duplicates and naming drift, answers plain-language questions about funnels and cohorts, runs the sample ratio check, drafts readouts and clusters hundreds of rejection reasons into themes.

What stays with you: choosing the questions, owning the definitions, judging validity, interpreting a null and making the call. A harness will answer the question you asked fluently, including when it was the wrong question or the data is broken. Four habits keep it honest:

- **Ask for definitions with every number.** Numerator, denominator, window and unit, checked against the dashboard spec.
- **Ask for validity before results.** Sample ratio, duration served and data quality come first.
- **Ask what else could explain it.** Seasonality, a concurrent launch, one large account's outage, a shift in customer mix.
- **Label exploratory findings.** A harness can slice data a hundred ways in a minute, which makes chance wins easy to find. Pre-register the segments you care about.

Analytics prompts often carry customer names and usage details. Use only tools approved for that data, and keep traces with customer content inside approved systems.

:::ai The harness is the analyst; you're the editor
Let the harness run the queries, build the charts and draft the readout. Spend your time choosing the question, checking definitions and validity, and deciding what the result means for the product.
:::

## The Beacon case: did the diagnosis agent work?

:::example Where Beacon is
Chapter 01 ended with a split hypothesis. Diagnosis ships first, and responders should accept the agent's root cause in at least 60% of incidents during a 30-day pilot. Supervised action (Beacon Agents) follows at Northlight Live, gated on audit logs, scoped credentials and a kill switch. Beacon has about 420 enterprise customers, a North Star of incidents resolved with Beacon's help per week, and gross margin down from 81% to 72% since agentic features launched. You own the measurement plan.
:::

**The tracking plan.** You start with seven questions, among them: do responders accept the diagnosis; how long from page to accepted diagnosis (Dana needs under five minutes); do accepted diagnoses hold up; and what does each resolved incident cost in inference. Ten core events follow, all Object Action: Incident Correlated, Diagnosis Proposed, Diagnosis Accepted, Diagnosis Rejected (with a reason), Diagnosis Edited, Action Proposed, Action Approved, Action Executed, Action Reverted and Incident Resolved. Each carries account_id, partner_id (for Leo's MSP tenants), actor_type and model_version; actions also carry risk_tier and whether they were allowlisted. Sam adds one rule: no log content or personal data in any property, and the customer-facing audit trail stays separate from product analytics.

**HEART and the dashboard.** The trio leaves Engagement blank, citing the HEART authors' own caveat: for Dana, less time in Beacon at 3 a.m. is success. Task success carries the weight (acceptance rate, page to accepted diagnosis, action revert rate). Adoption is accounts with a first accepted diagnosis within 14 days. Retention is the share of each account's incidents touched by Beacon, by cohort month. Happiness is a quarterly Ellis-style survey. The dashboard puts the North Star on top; inputs are compression ratio, acceptance rate, autonomous resolution rate and weekly active responders; guardrails are revert rate, wrong-root-cause reports, inference cost per resolved incident and 95th percentile diagnosis latency; MTTR and NRR (118%) sit at the bottom as lagging indicators.

**The experiment that wasn't.** Design wants to test inline versus collapsed evidence citations. Responders in an account share incidents, so randomization has to be by account, and the harness's estimate shows that with about 420 accounts the minimum detectable effect is far larger than anyone expects. You choose a staged rollout to half the accounts with a matched holdout, a pre-period adjustment on each account's acceptance rate, and an offline replay on 300 past incidents first. The move to per-resolved-incident pricing isn't tested at all, because prices differ by contract and testing them would damage trust; that evidence comes from design partners and a cohort comparison.

**An experiment that was.** The alert grouping screen in self-serve mid-market tenants does have volume, so the team runs a responder-level 50/50 test. The first readout shows a strong win, and the harness's draft calls it. The sample ratio check fails. MSP tenants had been bucketed by partner_id, so whole partners landed in one arm. You hold the readout, fix assignment and rerun. The rerun shows a smaller real improvement with every guardrail passing.

**The 30-day review.** Acceptance is above the 60% target, and on the dashboard the hypothesis looks validated. Then the revert rate at one large customer spikes. It traces to the failure Chapter 31 warns about: the agent proposed a confident, wrong root cause, the responder accepted it and rolled back the wrong service.

The review names the lesson. Acceptance had been measuring trust, and confident answers earn trust whether or not they're right. The team adds a failure signal (a diagnosis accepted, then an action reverted within an hour) and runs error analysis on 100 rejected or reverted traces, with the SRE who knows the customer environments best as the final voice. The largest cluster is the recency bias Chapter 31 names (the agent over-weights the latest deploy), made worse here by stale deploy data from one connector. The success criterion becomes acceptance with no reversion, and the verdict is recorded as "validated for acceptance, unclear for correctness."

**The fit check.** In Beacon's survey data, 46% of SRE leads like Priya would be very disappointed to lose Beacon, against 31% of on-call engineers like Dana. Dana's group asks for one thing: faster time to a trustworthy diagnosis. The cohorts agree: accounts where on-call engineers accept diagnoses in their first two weeks flatten, and the rest decline.

**The iteration plan.** Three items, each with a stop condition. Fix the stale connector and add a freshness check, measured by the reverted-after-accept rate. Speed up diagnosis for Dana, measured against the five-minute goal. For fully autonomous low-risk actions, use Ries's milestones: the baseline is the autonomous resolution rate at Northlight Live, tuning covers allowlist templates and the approval experience, and the pivot-or-persevere decision is dated for the end of next quarter with a written rule. Marcus gets one page with the North Star, cost per resolved incident and the decision, and the readout goes into the decision log.

## Product 360 artifacts

These are Product 360 formats, synthesized for this book from the practices described above. Keep the tracking plan, HEART grid and dashboard spec as living artifacts in the Measure dimension; experiment designs, readouts and post-launch reviews are event artifacts that feed the decision log.

```template id="05-tracking-plan" title="Tracking plan and event spec"
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
```

```template id="05-heart-grid" title="HEART metrics grid"
# HEART grid · [Product or feature] · [Date]

**Owner:** [PM]   **Unit of analysis:** user / account / unit of work ([which])

| Category | Goal (what we want for the user) | Signal (behavior or attitude that shows success or failure) | Metric (normalized, with window) | Source (logs / survey) | Logged today? | Target | Owner |
|---|---|---|---|---|---|---|---|
| Happiness | | | | | | | |
| Engagement | | | | | | | |
| Adoption | | | | | | | |
| Retention | | | | | | | |
| Task success | | | | | | | |

## Rows left blank on purpose
| Category | Why we are not measuring it |
|---|---|
| | |

## Failure signals
List the signals that would show the feature failing (abandonment, undo, rejection, reversion, escalation):
-
-

## Notes
- Engagement is reported per user or per account, never as a total.
- Plan to read Happiness over several weeks after a change, to see past change aversion.
```

```template id="05-metrics-dashboard-spec" title="Metrics dashboard spec"
# Metrics dashboard spec · [Product] · v[n] · [Date]

**Purpose:** [the decision or review this dashboard serves]   **Audience:** [who looks at it, how often]   **Owner:** [PM]   **Data freshness:** [daily / hourly]

## Layout
1. North Star: [metric] (Chapter 02)
2. Input metrics (3 to 5)
3. Guardrails
4. Lagging indicators

## Metric definitions
| Metric | Tier (North Star / input / guardrail / lagging) | Numerator | Denominator | Window | Unit (user / account / work item) | Segments available | Target or threshold | Action this metric triggers |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## Guardrails
| Guardrail | Threshold | Who is alerted | What happens on breach |
|---|---|---|---|
| | | | |

## Standard segments
[Persona or role, plan tier, region, account size, partner, cohort month, model_version]

## Charts we decided not to include
| Chart | Why it was cut |
|---|---|
| | |

## Review rhythm
Reviewed in [weekly team review / monthly metric review]. Definitions changed only through [owner], with a dated note.
```

```template id="05-experiment-design" title="Experiment design doc"
# Experiment design · [Name] · [Date]

**Owner:** [PM]   **Analyst:** [Name]   **Decision maker:** [Name]   **Status:** Draft / Approved / Running / Read out

## 1. Decision this informs
[What we will do differently depending on the result.]

## 2. Hypothesis
We believe [change] for [segment] will [move OEC by at least X] because [reason]. We will know when [metric and threshold].

## 3. Unit of randomization
User / account / tenant / other: [choice]. Why: [interference risk, how the experience is shared].

## 4. Metrics
- OEC: [one metric or weighted combination, with definition]
- Secondary metrics: [list]
- Guardrails: [metric: must not degrade by more than X]

## 5. Power and duration
- Baseline and variance of the OEC: [values and source]
- Minimum detectable effect: [value]
- Sample size per arm: [n]
- Duration: [whole weeks]
- Variance reduction: [pre-period adjustment used? yes / no]
- Stopping rule: fixed duration / sequential method [name]. No early stopping on the OEC.

## 6. Population and ramp
Included: [who]. Excluded: [who and why]. Ramp: [percent by date].

## 7. Validity checks
- [ ] Sample ratio check before readout
- [ ] Pre-period or A/A comparison of arms
- [ ] Novelty or primacy watch: read results by week
- [ ] Data quality: event volumes by arm

## 8. Decision rule (written before launch)
| Result | Decision |
|---|---|
| OEC up, guardrails pass | |
| OEC up, a guardrail fails | |
| No detectable change | |
| OEC down | |

## 9. Risks and communication
Privacy review: [status]. Customer notice required by contract? [yes / no]. Safety: [any action that must not be randomized].

## If we cannot run a controlled experiment
Method chosen: [staged rollout with holdout / matched comparison / time series / offline replay / design partners]. Assumption we are making: [state it]. What else could explain a change: [list].
```

```template id="05-ab-readout" title="A/B test readout"
# Experiment readout · [Name] · [Date]

**Decision:** [Ship / iterate / kill], recommended by [PM], decided by [Name] on [date].

## Validity
- Sample ratio: configured [x/y], observed [x/y], check [pass / fail]
- Duration served: [dates, whole weeks]
- Data quality issues: [none / list]
- Deviations from the design doc: [none / list]

If any validity check failed, stop here: the result is not interpretable. State the cause and the rerun plan.

## Primary result
OEC: control [value], treatment [value], difference [value] with [95%] interval [low to high].

## Guardrails
| Guardrail | Threshold | Result | Pass / fail |
|---|---|---|---|
| | | | |

## Secondary metrics
| Metric | Difference | Interval | Notes |
|---|---|---|---|

## Segments
| Segment | Pre-registered or exploratory | Result |
|---|---|---|

## What we learned
[What moved, and the qualitative evidence for why. Include what surprised us.]

## Next step
[Action, owner, date]
```

```template id="05-post-launch-review" title="Post-launch review"
# Post-launch review · [Feature or product] · [Review point: 30 / 60 / 90 days] · [Date]

**Owner:** [PM]   **Attendees:** [trio, data, stakeholders]

## The hypothesis as written before launch
[Paste it verbatim, with its date.]

## Success criteria set before launch
| Criterion | Target | Date set |
|---|---|---|

## What happened
| Area | Metric | Result | Against target |
|---|---|---|---|
| Activation | | | |
| Task success or quality | | | |
| Retention | | | |
| Guardrails | | | |
| Revenue or business signal | | | |

## What customers said
[Themes from conversations, tickets and, for AI features, trace review. Link the evidence.]

## Verdict by assumption
| Assumption | Validated / invalidated / unclear | Evidence |
|---|---|---|

## Decisions
1.
2.

## What we would instrument differently
[Events or properties we missed, definitions that caused confusion.]
```

```template id="05-iteration-plan" title="Iteration plan"
# Iteration plan · [Product or feature] · [Period] · [Date]

**Owner:** [PM]   **Linked review:** [post-launch review or readout]

## Open assumptions and next tests
| Assumption | Current status | Next test or measurement | Evidence that would change the plan | Dashboard metric | Owner | Due | Stop condition |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Pivot-or-persevere checkpoint
- Baseline: [metric and value, date]
- Tuning work: [what we will change]
- Decision date: [date]
- Persevere if: [result]
- Pivot or stop if: [result]

## Not doing this iteration
[Items considered and deliberately deferred, with the reason.]
```

## Prompts

```prompt title="Draft a tracking plan from a PRD"
Goal: Get a first tracking plan that starts from questions, not events.
Paste in: the PRD or feature spec, the main user flows, the North Star and input metrics, and the current event taxonomy (or a list of existing event names). Unreleased plans are confidential; use an approved tool.

You are helping a PM instrument [feature] in a B2B product before launch.

1. List the 5 to 10 questions this launch must answer. Include activation, task success or quality, retention and at least one guardrail.
2. For each question, name the metric (numerator, denominator, window, unit: user, account or work item).
3. Propose the events and properties each metric needs. Name events as Object plus past-tense Action in Proper Case; name properties in snake_case. Put variable detail in properties, never in names.
4. Every event must carry account_id and actor_type (human, agent, automation). Mark events that should fire server-side.
5. Compare your events with the existing taxonomy. Flag duplicates, near-duplicates and casing differences.
6. Add a privacy note to every property. Flag any property that could carry customer content or personal data.

Output the plan as a table with: event, fires when, question, metric, properties, source, privacy note.

Check the output: every event should trace to a question. Delete events that don't. Walk one critical path with an engineer and confirm the "fires when" moments are precise enough to implement.
```

```prompt title="Build a HEART grid for a feature"
Goal: Choose user-centered metrics for one feature and decide which categories to leave out.
Paste in: the feature description, the personas who use it, the product hypothesis and any existing metrics.

Using Rodden, Hutchinson and Fu's HEART framework and their Goals, Signals, Metrics process, build a HEART grid for [feature] in a B2B product.

For each category (Happiness, Engagement, Adoption, Retention, Task success):
- State the goal for the user.
- List candidate signals, including failure signals such as abandonment, undo, rejection or reversion. Say whether each is likely logged today.
- Turn the best signal into a normalized metric (rate, share or per-user or per-account average) with a window.

Then recommend which categories to leave blank and why. Consider whether engagement is meaningful when use is part of the person's job, and whether more time spent would be good or bad here.

Check the output: no metric should be a raw total. If the grid uses Engagement for a workflow where less time is the goal, push back.
```

```prompt title="Diagnose a retention curve"
Goal: Read cohort retention honestly and find what separates customers who stay.
Paste in (or connect the harness to): cohort retention data by start month, the definition of "active" and the window, and account attributes (segment, size, plan, persona mix, activation date). Use only tools approved for customer data.

Analyze retention for [product] by cohort.

1. State the definition of active, the unit and the window you are using. Tell me if the window seems mismatched to how often customers naturally need the product.
2. Describe the curve shape for each cohort: declining toward zero, flattening (and at what level) or smiling.
3. Compare recent cohorts with older ones. Are newer cohorts better or worse?
4. Find which early behaviors (in the first 14 to 30 days) most separate accounts that stay from accounts that decline. Show the size of each group.
5. List alternative explanations for any pattern (customer mix, seasonality, a large account, a pricing change).

Don't claim causation from these comparisons; label them as associations to test.

Check the output: confirm the definition of active matches the dashboard spec. Look at the group sizes; a striking difference between two groups of eight accounts is a lead, not a finding.
```

```prompt title="Decide whether to A/B test, and design it"
Goal: Find out whether a controlled experiment is feasible and, if it is, write the design doc.
Paste in: the change, the decision it informs, the candidate OEC with its baseline and variance, traffic or account counts, how users share work within an account, and any contractual or safety constraints.

Act as an experimentation reviewer for [product], a B2B product.

1. Recommend the unit of randomization (user, account, tenant) and explain the interference risk.
2. Estimate the minimum detectable effect for a test of [duration] with this volume, with and without a pre-period adjustment (CUPED-style). Show your assumptions.
3. Say plainly whether the test is worth running. If the detectable effect is larger than any plausible result, or the change is contractual or safety-critical, say so.
4. If it is worth running, draft an experiment design doc: decision, hypothesis, unit, OEC, guardrails with thresholds, sample size, duration in whole weeks, stopping rule (no peeking), validity checks including a sample ratio check, and a decision rule for each outcome including a null.
5. If it isn't, recommend the strongest alternative (account-paired pilot, staged rollout with holdout, comparison group, time series, offline replay, design partners) and state the assumption it relies on.

Check the output: have an analyst confirm the power estimate before you commit. Make sure the decision rule was written before the test, and that a null result has a named action.
```

```prompt title="Draft an A/B readout that checks validity first"
Goal: Produce a readout that can't announce an invalid result.
Paste in (or connect the harness to): the experiment design doc and the results: counts per arm, OEC, guardrails, secondary metrics and segments.

Draft an experiment readout for [experiment] using this order:
1. Validity: compute the sample ratio against the configured split and say whether it passes a strict test. Report duration served and any data quality issues. If validity fails, stop and write only the cause and rerun plan.
2. Primary result: the OEC difference with a confidence interval, not only a p-value.
3. Guardrails: each one, pass or fail against its threshold.
4. Segments: label each as pre-registered (from the design doc) or exploratory.
5. Week-by-week view of the OEC, to check for novelty or primacy effects.
6. A recommendation (ship, iterate or kill) that follows the decision rule in the design doc. If the result conflicts with the rule, say so.

Don't describe exploratory segments as findings. Don't round a null into a "directional win."

Check the output: recompute the sample ratio yourself or with an analyst. Read the recommendation against the pre-written decision rule; if they differ, the readout needs an explicit reason.
```

```prompt title="Run error analysis on AI feature traces"
Goal: Find the real failure modes of an AI feature in production and turn them into checks.
Paste in: a sample of production traces (inputs, retrieved context, outputs, tool calls and the user's response), plus your own free-text notes on the first 30 or so. Traces often contain customer data; use only an approved tool and remove identifiers where you can.

You are assisting a domain expert with error analysis on [AI feature].

1. Using my notes as the starting vocabulary, propose a taxonomy of failure modes. Keep categories specific (for example, "used stale deploy data") rather than generic ("low quality").
2. Assign each remaining trace to zero or more categories, with a one-line justification quoting the trace.
3. Count traces per failure mode and show which modes most often lead to the user rejecting or reverting the output.
4. Tell me when new traces stop producing new categories.
5. For the top three failure modes, propose a binary pass or fail check that an automated grader or a reviewer could apply.

Don't use generic quality scores or 1 to 5 scales.

Check the output: read 10 traces the model categorized and confirm you agree. The domain expert has the final say on every category and every check. Compare the proposed checks with human judgment on a fresh sample before trusting them.
```

```prompt title="Write the post-launch review and iteration plan"
Goal: Call each assumption honestly and turn the open ones into dated tests.
Paste in: the product hypothesis and success criteria as written before launch, the dashboard results, any experiment readouts, Ellis survey results by persona, retention cohorts and a summary of customer conversations and trace review. Customer names and conversation notes are confidential; use an approved tool.

Draft a post-launch review for [feature] at [30/60/90] days.

1. Restate the pre-launch hypothesis and success criteria verbatim. Don't adjust them.
2. For each assumption, give a verdict (validated, invalidated or unclear) with the evidence. Where a metric met its target but another signal contradicts it, say so and mark it unclear.
3. List what we would instrument differently.
4. Draft an iteration plan: for each open or invalidated assumption, the next test, the evidence that would change our plan, the dashboard metric, an owner placeholder, a date and a stop condition.
5. Propose a pivot-or-persevere checkpoint with a baseline, the tuning work and a written rule for each outcome.

Check the output: compare the success criteria with the originals word for word. If any verdict reads more positive than the evidence, rewrite it yourself. Every iteration item needs a stop condition.
```

## Anti-patterns

:::warn Track everything, answer nothing
The team instruments every click "so we have the data," then can't answer leadership's first question because no event maps to a metric and half are named three different ways. Start from the questions and delete events nobody uses.
:::

:::warn Success criteria written after launch
Nobody wrote down what success looked like, so the review picks whichever metric went up. Write the criteria, with numbers and a date, before launch, and paste them verbatim into the review.
:::

:::warn Consumer engagement metrics in an enterprise workflow
The dashboard celebrates rising time in product for a tool whose job is to get people out quickly. Decide per feature whether more use is good, and lean on task success and outcomes where use is part of the job.
:::

:::warn Peeking and declaring victory
The PM stops the experiment the morning it shows significance. Fix the duration and sample size in advance, run whole weeks, and read the OEC once.
:::

:::warn The readout without a validity check
A striking win goes to the executive staff meeting; a week later someone finds a sample ratio mismatch. No readout leaves the team until the sample ratio, duration and data quality have been checked.
:::

:::warn Forcing A/B tests on a few hundred accounts
An account-level test that could only detect an implausibly large effect reports "no significant difference," and the team concludes the change doesn't matter. Calculate the minimum detectable effect first; when volume can't support a test, use a staged rollout, a matched comparison or offline replay.
:::

:::warn Acceptance rate as the AI quality metric
The AI feature's acceptance rate looks healthy, so nobody reads the traces. Then a confident, wrong answer gets accepted and acted on. Pair acceptance with a correctness signal such as reversions or graded samples, and run error analysis on real traces every week after launch.
:::

## Checklist

- [ ] The product hypothesis and success criteria, with numbers and a date, were written and agreed before launch.
- [ ] A tracking plan starts from questions, uses Object Action names, puts account_id and actor_type on every event, and has a privacy note on every property.
- [ ] Instrumentation was validated in a test environment before launch.
- [ ] A HEART grid exists for the feature, with blank rows explained.
- [ ] The dashboard spec defines every metric's numerator, denominator, window and unit, and names the action each chart triggers.
- [ ] Activation is defined as a completed action that delivers value, measured per account with time to activation.
- [ ] Retention is read by cohort, with a window matched to natural usage and a meaningful definition of active.
- [ ] Every experiment had its OEC, guardrails, sample size, duration, stopping rule and decision rule written before it started, and every readout reports validity before the result.
- [ ] Where volume is too low for an A/B test, the alternative method and its assumption are written down.
- [ ] AI features log model version, cost, latency and the human decision, and pair acceptance with a correctness signal.
- [ ] Error analysis on at least 100 production traces has been done, with a named domain expert owning the quality bar.
- [ ] The post-launch review calls each assumption validated, invalidated or unclear against the original criteria.
- [ ] The iteration plan has an owner, a date and a stop condition for every item, plus a dated pivot-or-persevere checkpoint.

## Key takeaways

- Write the success criteria, with numbers and a date, before you launch, and judge the launch against them verbatim.
- Instrument from questions. A tracking plan with consistent Object Action names, account identifiers and actor type is what makes every later answer trustworthy, including the ones your AI harness gives you.
- Read B2B products at the right unit. Activation, funnels and retention mostly belong to the account, and in many enterprise workflows less time in the product means the product is working.
- Use attitudinal and behavioral fit signals together: the Ellis survey by persona, and cohort curves that flatten.
- Controlled experiments give causal answers only when the OEC, guardrails and stopping rule are set in advance and the sample ratio checks out. When volume is too low for a test, as it is for most account-level decisions, choose a weaker method knowingly and name its assumption.
- For AI features, acceptance measures trust. Pair it with reversions, graded samples and regular error analysis on real traces, and track cost per outcome next to quality.
- Close the loop quickly. The post-launch review and iteration plan turn each assumption into a verdict and the next dated test.
