<p class="lead">An AI-powered product doesn't behave the same way twice, costs money every time someone uses it, and has to earn the user's trust one answer at a time. Those three facts change how you specify it, measure it, price it and run it. This chapter is the product manager's guide to all of that.</p>

## Why this matters

For thirty years, software products were deterministic. You wrote a requirement, engineering built it, QA checked that the same input produced the expected output, and you shipped. Marginal cost was close to zero, so pricing was mostly a question of value and competition. Trust came from reliability: once a feature worked, it kept working.

AI-powered products break all three assumptions.

- **Behavior is a distribution, not a specification.** The same prompt can produce a great answer, a mediocre one and a confidently wrong one. You can't specify the output; you can only specify how often it must be good, and what "good" means.
- **Cost scales with usage.** Every answer has an inference cost. A feature that delights users can quietly destroy gross margin. Agentic features, which call models many times per task, make this worse.
- **Trust is earned per answer.** Users can't easily tell a right answer from a plausible wrong one. A single confident mistake in a high-stakes moment can cost more trust than a hundred good answers earn.

The result is that the PM's job on an AI product expands. Quality becomes a product decision you specify with evals. Cost becomes a requirement with a gross-margin floor. Trust becomes a design problem with its own patterns. Autonomy becomes a dial you set per action, not a feature you ship. And regulation, for the first time in most enterprise PMs' careers, becomes a product input rather than a legal review at the end.

This chapter covers each of those. Chapter 32 covers the other half of AI-era product management: using AI to do the PM job itself. Chapter 33 goes deeper on responsible AI and regulation.

## Does this need AI at all?

The first question is the one teams skip. Google's People + AI Research (PAIR) team makes it the opening chapter of the *People + AI Guidebook*: decide whether AI adds value before deciding how to build it.

AI is a good fit when the task involves judgment over messy inputs (language, images, logs, unstructured documents), when a probabilistic answer is useful even if it's sometimes wrong, and when the cost of an error is low or can be caught. It's a poor fit when the task has a correct, rule-based answer, when every error is expensive and hard to detect, or when users need to predict exactly what the system will do.

PAIR's framing of **precision versus recall** is a practical tool here. Every AI feature makes two kinds of mistake: false positives (it says yes when the answer is no) and false negatives (it misses something real). They rarely cost the same. For Beacon, a false-positive root cause ("the deploy at 14:02 caused this") can send an engineer to roll back the wrong service, which is expensive. A false negative ("I couldn't determine the cause") just means the engineer diagnoses it manually, which is the status quo. That asymmetry should shape the product: tune for precision, and make "I don't know" a first-class answer.

:::key Start with the cost of being wrong
Before choosing a model or a pattern, write down what each kind of error costs the user and the business. That one table will drive your eval targets, your autonomy settings, your UX and, often, your pricing.
:::

## Workflows, agents and autonomy

### Workflows versus agents

Anthropic's widely cited essay "Building effective agents," by Erik Schluntz and Barry Zhang, draws the line that every AI PM needs. **Workflows** orchestrate models and tools through predefined code paths. **Agents** let the model direct its own process and tool use, in a loop, based on what it observes. Both are "agentic systems," and they sit on a spectrum of patterns, from simple to complex:

| Pattern | What it does | Use it when |
|---|---|---|
| **Augmented model** | One model call with retrieval, tools or memory | The task is a single step with the right context |
| **Prompt chaining** | A fixed sequence of model calls, each feeding the next | The task splits into predictable steps |
| **Routing** | Classifies the input and sends it to a specialized path | Different inputs need different handling |
| **Parallelization** | Splits work into parallel calls, or runs the same call several times and votes | Speed matters, or you want more confidence |
| **Orchestrator-workers** | One model breaks the task down and delegates to others | Subtasks can't be predicted in advance |
| **Evaluator-optimizer** | One model drafts, another critiques, in a loop | Clear evaluation criteria exist and iteration helps |
| **Autonomous agent** | The model uses tools in a loop until it reaches a goal or a stopping condition | The task is open-ended and the steps can't be predicted |

The essay's central advice is to start with the simplest pattern that works. Agentic systems trade latency and cost for capability. Many enterprise features work better as workflows, which are cheaper, faster and much easier to evaluate and audit. Use an agent only when the problem really is open-ended, and record the choice in the PRD as a decision with its rationale.

The same essay introduces the **agent-computer interface**: design the tools an agent uses as carefully as you'd design a human interface. Write tool descriptions the way you'd brief a junior developer, and design arguments so mistakes are hard to make. That's product work, and in B2B platforms it often falls to the PM who owns the API.

### Autonomy is a dial, set per action

Kevin Feng, David McDonald and Amy Zhang's 2025 paper "Levels of Autonomy for AI Agents" gives product teams a useful vocabulary. It defines five levels by the **user's** role, not the agent's capability:

| Level | User's role | What the agent does |
|---|---|---|
| **L1** | Operator | The user directs and decides; the agent carries out |
| **L2** | Collaborator | The user and agent plan and execute together |
| **L3** | Consultant | The agent leads and consults the user for expertise or preferences |
| **L4** | Approver | The agent acts and involves the user only for risky or pre-specified situations |
| **L5** | Observer | The agent acts fully autonomously; the user monitors |

The paper's key point is that autonomy is a design choice, separate from capability. A model that *can* act autonomously shouldn't necessarily be *allowed* to.

For product specification, this book recommends setting autonomy **per action class**, not per product. An agent can sensibly be at L4 for reading logs and drafting a diagnosis, and at L2 for anything that writes to a production system. Pair that with a **reversibility map**: which actions can be undone cheaply, which are costly to reverse and which are irreversible. Irreversible actions need approval, dry-run modes or two-step confirmation, however good the model is.

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 230" role="img" aria-label="Autonomy set per action class: reading at high autonomy, writing at lower autonomy">
  <line x1="40" y1="190" x2="690" y2="190" class="ln"/>
  <text x="40" y="214" class="s">L1 Operator</text><text x="190" y="214" class="s">L2 Collaborator</text><text x="350" y="214" class="s">L3 Consultant</text><text x="500" y="214" class="s">L4 Approver</text><text x="630" y="214" class="s">L5 Observer</text>
  <rect x="490" y="24" width="190" height="34" rx="8" fill="var(--a2)" fill-opacity=".16" stroke="var(--a2)" stroke-opacity=".6"/><text x="502" y="46" class="t">Read logs, metrics, traces</text>
  <rect x="490" y="66" width="190" height="34" rx="8" fill="var(--a2)" fill-opacity=".16" stroke="var(--a2)" stroke-opacity=".6"/><text x="502" y="88" class="t">Draft diagnosis and summary</text>
  <rect x="330" y="108" width="210" height="34" rx="8" fill="var(--a3)" fill-opacity=".16" stroke="var(--a3)" stroke-opacity=".6"/><text x="342" y="130" class="t">Allowlisted, reversible action</text>
  <rect x="170" y="150" width="220" height="34" rx="8" fill="var(--a4)" fill-opacity=".16" stroke="var(--a4)" stroke-opacity=".6"/><text x="182" y="172" class="t">Rollback or config change in prod</text>
</svg>
<figcaption>Beacon Agents' autonomy, set per action class. Reading and drafting run at L4; reversible allowlisted actions at L3; anything that changes production at L2, with a human approval on every action.</figcaption>
</figure>

### Connectors, MCP and agent protocols

Agents are only as useful as what they can reach. In 2026 that increasingly runs through open protocols. The **Model Context Protocol (MCP)**, which Anthropic introduced in late 2024, became the common way for AI applications to connect to tools and data. In December 2025 Anthropic donated MCP to the new Agentic AI Foundation under the Linux Foundation, co-founded with OpenAI and Block, and at that point Anthropic reported more than 10,000 active public MCP servers. Google's **Agent2Agent (A2A)** protocol, hosted by the Linux Foundation since mid-2025, addresses a different problem: agents talking to other agents across organizations. The two are complementary, and the landscape is still moving.

For a B2B platform PM, the practical implication is that an **MCP server is now a product surface**, comparable to a public API. Customers' agents (in Claude, ChatGPT, Copilot or their own harnesses) reach your product through it. It needs a scope, an authentication model, rate limits, versioning, documentation, and a pricing position. Treat it as a product, with an owner, rather than as an integration somebody builds on a Friday.

## Evals: quality as a product decision

### Why evals replace "it works"

In a deterministic product, QA checks whether a feature works. In an AI product, the question is how often it works, on which kinds of input, and how badly it fails when it doesn't. The tool for answering that is an **eval**: a set of test cases, run automatically, each graded pass or fail, producing a quality score you can track over time and gate releases on.

Evals are where the PM's definition of quality becomes executable. That's why so many product leaders now describe eval-writing as a core PM skill, and why the PM (or a domain expert the PM designates) must own the eval's definition of "good" rather than leaving it to engineering.

### Start with error analysis

Hamel Husain and Shreya Shankar, whose evals course and FAQ are the most complete practitioner reference, put it bluntly: error analysis is "the most important activity in evals." Their method:

1. **Read real traces.** Pull about 30 real interactions (inputs, model outputs, tool calls). Read every one.
2. **Write free-form notes** on what went wrong in each. Don't use a rubric yet; rubrics written in advance narrow what you notice.
3. **Cluster the notes** into a **failure taxonomy**: a named list of the ways the product fails.
4. **Keep going until you stop finding new failure types.** That's your signal that the taxonomy is complete enough for now.

The failure taxonomy becomes the eval's structure and, often, the team's backlog. Each recurring failure mode gets a fix, and if it persists, a dedicated test.

Husain and Shankar add several rules that are worth adopting as team policy:

- **Use binary pass/fail, not 1 to 5 scales.** Rating scales produce inconsistent labels and drift toward the middle. If you need finer tracking, measure sub-components separately.
- **One narrow judge per failure mode.** When you use a model to grade outputs (an "LLM-as-judge"), give it one specific failure to check. Validate each judge against human labels, and report how often it catches real failures and how often it correctly passes good outputs, separately, rather than a single "agreement" number.
- **Distrust generic metrics.** "Helpfulness" scores and text-similarity metrics rarely track what users care about. Write evaluators for failures you've actually observed.
- **Name one accountable domain expert.** Someone has to make the final call on what "good" means. On most product teams, that's the PM or a domain expert the PM designates.

### Capability, regression and consistency

Anthropic's January 2026 guide "Demystifying evals for AI agents" adds vocabulary that's useful for planning.

**Capability evals** measure what the product can't yet do well. They should start with a low pass rate: they're the hill you're climbing. **Regression evals** protect what already works, and should pass at nearly 100% on every release. When a capability eval saturates, it graduates into the regression suite.

The guide also distinguishes two ways of counting success over several attempts, and the difference matters enormously for customer-facing products:

- **pass@k** is the probability that at least one of k attempts succeeds. It's the right measure when a user can pick the best of several options.
- **pass^k** is the probability that all k attempts succeed. It's the right measure when a customer expects the product to work every time.

The arithmetic is unforgiving. A task that succeeds 75% of the time on any one try succeeds three times in a row only about 42% of the time (0.75 × 0.75 × 0.75). For an agent that runs the same kind of task hundreds of times a week, consistency, not best-case capability, is what customers experience.

Two more practical rules from the guide: start with **20 to 50 tasks** drawn from real failures and user-reported bugs, balancing "should do" and "should not do" cases; and **grade outcomes, not paths**. For an agent, check whether the end state is right (the ticket was updated, the service is healthy), not whether it called tools in exactly the expected order, because agents often find valid routes nobody anticipated.

### Are evals the new PRD?

A popular line in 2025 and 2026 holds that "evals are the new PRD." Braintrust's version of the argument is that static specs assume deterministic behavior, while evals define target behavior, acceptance criteria and regression thresholds in a form that can gate releases. Lisa Murkin, writing in Mind the Product, offers the counterpoint: golden datasets overfit, thirty examples are directional rather than proof, datasets drift away from real usage while looking healthy, and a dataset owned only by product recreates the old PRD's problems.

This book's position sits between them. **Evals don't replace the PRD; they become its acceptance criteria in executable form.** The narrative PRD still carries the why, the who, the economics and the risk. The eval suite defines, precisely and testably, what "working" means.

## The AI PRD

An AI PRD keeps everything a classic PRD has and adds a set of sections that classic PRDs never needed. Published AI PRD templates, such as Miqdad Jaffer and Paweł Huryn's in *The Product Compass* and Product School's, add model, data and prompt requirements, accuracy and hallucination limits, guardrails and drift monitoring. Most underweight cost. Here's the full set of differences.

| Classic PRD | What the AI PRD adds or changes |
|---|---|
| Deterministic functional requirements | Behavior specified as **eval sets with pass-rate targets** per failure mode, plus consistency (pass^k) targets |
| Acceptance by QA test cases | Acceptance by **validated graders** (code checks, calibrated model judges, human review) and regression thresholds in CI |
| A list of edge cases | A **failure taxonomy** from error analysis, plus adversarial and "should refuse" cases |
| Performance and security requirements | Adds **latency budgets** (time to first token, end to end), **cost per task**, model and fallback policy, and drift monitoring |
| Data model | **Data requirements**: grounding sources, permissions, personal data handling, retention and feedback capture |
| UX flows | **Trust and failure UX**: confidence, citations, correction, undo and escalation |
| Launch plan | **Staged autonomy**: shadow mode, assisted, supervised, autonomous; kill switch |
| Pricing as a go-to-market item | **Unit economics as a requirement**: a gross-margin floor per feature |
| Compliance review at the end | **Regulatory classification up front**: risk tier, transparency duties, documentation obligations |

The AI PRD addendum template at the end of this chapter covers every row.

## Cost, latency and unit economics

### The cost curve is falling, and your bill may still rise

The price of AI capability has fallen at a startling rate. Epoch AI's 2025 analysis found that the price of reaching a fixed level of model performance fell by between 9x and 900x per year, depending on the task and threshold. GPT-4-level performance on one widely used knowledge benchmark went from about $37.50 per million tokens in March 2023 to about $0.18 by early 2025. Andreessen Horowitz's Guido Appenzeller called the trend "LLMflation" and put it at roughly 10x per year at constant capability.

But a falling price per token doesn't guarantee a falling cost per task. The steepest cuts apply to models that are no longer the frontier. Reasoning models think in long chains of tokens, and agents call models many times per task, so **tokens per task** tends to rise as products get more capable. Budget and price per task, not per token.

### Gross margin is the number to watch

Classic SaaS businesses run gross margins of roughly 75 to 80% or more. AI products run much lower. ICONIQ's 2026 State of AI report projects an average AI-product gross margin of about 53% for 2026, and Kyle Poyar's 2026 monetization survey found a median *target* AI gross margin of about 50%, with only 12% of companies targeting 80% or more. Your finance team will notice before you do.

The levers a PM controls:

- **Model routing**: send easy requests to small, cheap models and hard ones to frontier models. Often the single biggest lever.
- **Prompt caching**: long, stable instructions and context can be cached so repeat calls cost a fraction of the original. Check your provider's current pricing, because it changes often.
- **Workflow caching for agents**: once an agent solves a recurring task, convert the successful path into deterministic code and call the model only when something unexpected happens. Andreessen Horowitz's 2026 analysis of computer-use agents describes this as the pattern that makes agents economical on stable, high-volume work.
- **Budgets and stopping conditions**: maximum steps, tokens, time and spend per task, with an escalation path when a limit is hit.
- **Latency design**: stream output, keep time to first token low on interactive paths, use small models where speed matters, and run long agent tasks asynchronously.

### Pricing AI

Seat-based pricing breaks when AI does the work that seats represented. If one agent replaces part of five people's work, charging per seat charges less as you deliver more. That's why AI pricing is in flux.

| Model | How it works | Strength | Risk |
|---|---|---|---|
| **Seat** | Per user per month | Simple, predictable | Revenue falls as AI replaces human effort |
| **Usage or credits** | Per token, call, action or credit | Tracks cost | Passes cost volatility to customers; bill anxiety |
| **Outcome** | Per resolved ticket, resolved incident or qualified lead | Aligns price with value | Needs a measurable, attributable outcome; vendor carries performance risk |
| **Hybrid** | Platform fee plus credits or outcomes | Balances predictability and alignment | More complex to explain and meter |

The market is moving toward hybrids. Poyar's 2026 survey of more than 230 B2B software and AI companies found hybrid pricing had become the most common model, at 37% of companies, and 29% using AI credits. The public examples show the experimentation. Intercom's Fin AI agent has charged $0.99 per outcome. Salesforce launched Agentforce at $2 per conversation, then in May 2025 moved to Flex Credits priced at about $0.10 per action, and added per-user options later that year. And Cursor's July 2025 move from request limits to included usage produced surprise charges, a public apology and refunds: a reminder that usage-linked pricing needs metering visibility and spend controls before it launches. Chapter 15 covers AI pricing in depth.

## Trust and the UX of being wrong

### Calibrated trust

The goal isn't maximum trust. It's **calibrated trust**: users trusting the system as much as its reliability warrants, and no more. PAIR's guidebook builds its trust chapters around this idea, along with treating errors and graceful failure as part of the core flow rather than an edge case.

Microsoft's **Guidelines for Human-AI Interaction**, published by Saleema Amershi and colleagues at CHI 2019 and validated with practitioners across twenty products, offer eighteen guidelines grouped into four moments. Paraphrased:

- **Initially**: make clear what the system can do, and how well it can do it.
- **During interaction**: time help to the context, show relevant information, and match social norms while mitigating bias.
- **When it's wrong**: make it easy to invoke, dismiss and correct; scope down when uncertain; and explain why it did what it did.
- **Over time**: learn from behavior cautiously, invite granular feedback, provide global controls, and tell users when the system changes.

Use them as a launch-review checklist. Most AI trust failures map to one of them, usually "make clear how well it can do it" or "scope services when in doubt."

### Patterns that work

- **Show sources and confidence** wherever the user must act on an output. A root cause with three linked log lines is checkable; a bare assertion isn't.
- **Make "I don't know" a good answer.** Design an explicit low-confidence state, and reward it in evals rather than penalizing it.
- **Make correction cheap** with inline edits, regenerate and undo, and capture every correction as a label for evals.
- **Disclose AI.** Users should know when they're talking to an AI, especially in support. In the EU it's increasingly a legal requirement, too.
- **Degrade gracefully** to search, templates or a human when confidence is low or the model provider is down.
- **Design against rubber-stamping.** "Human in the loop" fails silently when reviewers approve everything. Make wrong output easy to spot: highlight what changed, show the evidence, and sample approvals for audit.

### What failure looks like in public

Four widely reported incidents illustrate the failure modes PMs must design against:

- **Air Canada (2024).** A support chatbot told a customer they could claim a bereavement fare retroactively. A Canadian tribunal held the airline responsible for what its chatbot said, rejecting the argument that the bot was a separate entity. Lesson: you own your AI's statements. Ground policy answers in approved sources and show them.
- **Cursor (2025).** An AI support agent invented a login policy that didn't exist, and users cancelled before a co-founder corrected it publicly. Lesson: disclose AI agents, and restrict policy statements to retrieved, approved content.
- **Replit (2025).** During a code freeze, an AI coding agent ran destructive commands against a user's live database, then misreported whether recovery was possible. Replit separated development and production databases afterward. Lesson: least privilege, environment separation and approval for irreversible actions.
- **Deloitte Australia (2025).** A government report produced with AI assistance contained fabricated citations and a fabricated quote; the firm issued a corrected report and refunded part of the fee. Lesson: any AI-assisted deliverable needs citation verification and disclosure.

## Data, flywheels and moats

Every AI strategy deck has a data flywheel: more usage produces more data, which makes the product better, which attracts more usage. Many teams assume a flywheel they don't actually have. Usage compounds only when it produces **labels** (signals of what was good or bad), those labels **feed** evals or model improvements, and users can **see** the improvement.

In B2B, there's a further constraint: enterprise contracts often forbid training on customer data. The flywheel may have to run on per-customer context (runbooks, history, preferences), on your own eval sets, and on aggregate signals customers have consented to share. Write feedback capture into the requirements: what signal, under which consent and contract terms, stored where.

Model access isn't a moat; every competitor can call the same models. The defensible advantages in 2026 are workflow integration and switching costs, proprietary context (the customer-specific knowledge your product accumulates), distribution, and trust. Chapter 16 covers defensibility in depth.

## Regulation: a product input now

Regulation used to arrive at the end of an enterprise product cycle, as a legal review. For AI products it needs to arrive at the start, because the evidence regulators require (risk management, logging, human oversight, accuracy testing, documentation) has to be built into the product, not bolted on.

A snapshot as of late 2026, which Chapter 33 covers in depth. This is not legal advice, and dates should be confirmed with counsel before you rely on them.

- **EU AI Act.** The Act entered into force in August 2024. Prohibited practices and AI-literacy duties applied from February 2025, and obligations for general-purpose AI models from August 2025. Transparency obligations, such as telling people they're interacting with AI, apply from August 2026. In July 2026 the EU adopted the "Digital Omnibus" amendment (Regulation (EU) 2026/1744), which postponed the high-risk obligations: stand-alone high-risk systems now from December 2027, and AI embedded in regulated products from August 2028.
- **NIST AI Risk Management Framework.** A voluntary US framework built on four functions (Govern, Map, Measure, Manage), with a 2024 Generative AI Profile listing risks specific to generative AI, such as confabulation. Widely used in enterprise risk programs.
- **ISO/IEC 42001.** The first certifiable AI management system standard, published in late 2023. It's becoming the AI counterpart of ISO 27001 in enterprise security questionnaires.

For a PM, the practical step is to record in the PRD whether you're a provider or a deployer of each AI system, its likely risk tier, and the transparency and documentation duties that follow. Even where obligations are years away, enterprise customers will ask for this documentation in security reviews now.

## How to apply it

Here's the lifecycle for building an AI-powered feature or product, from idea to scale.

1. **Write the cost-of-error table.** For each kind of mistake (false positive, false negative, harmful output, wrong action), write what it costs the user and the business.
2. **Decide whether AI is the right tool.** If a rule-based solution meets the need, use it. If not, state why AI adds value.
3. **Choose the simplest pattern.** Start at the top of the workflow-to-agent table and move down only when a simpler pattern fails. Record the decision.
4. **Set autonomy per action class.** Build the reversibility map. Default anything that changes a system of record to L2 (human approval) until evidence supports more.
5. **Prototype and run error analysis.** Put a prototype in front of real or realistic inputs, read at least 30 traces, and build the failure taxonomy.
6. **Build the eval suite.** Turn the taxonomy into 20 to 50 tasks with binary graders. Separate capability from regression evals. Validate any model judges against human labels. Set pass-rate and pass^k targets with your domain expert.
7. **Build the cost model.** Estimate tokens and model calls per task, cost per task at expected volume, and gross margin at the proposed price. Set a margin floor. Identify routing and caching levers.
8. **Design the trust UX.** Sources, confidence, "I don't know," correction, undo, escalation, disclosure. Review against the human-AI interaction guidelines.
9. **Classify the regulatory exposure.** Provider or deployer, risk tier, transparency duties, documentation. Bring counsel in now.
10. **Roll out in stages.** Shadow mode (the AI runs, users don't see it, you compare to humans); assisted (users see suggestions); supervised (the AI acts with approval); autonomous for allowlisted actions. Move between stages on eval and production evidence, not on the calendar.
11. **Monitor in production.** Track quality on sampled production traffic, cost per task, latency, user corrections and escalations. Re-run regression evals on every model, prompt or provider change.
12. **Close the loop.** Every production failure becomes a new eval case. Review the failure taxonomy monthly.

:::leader For product leaders
Make the eval suite, the cost model and the model register required artifacts in your portfolio's Product 360 for every AI-powered product, and review them in the monthly product review alongside the dashboard. AI products that aren't measured this way drift in quality and margin without anyone noticing, until a customer or the CFO does.
:::

## The AI lens: using AI to build AI products

There's a recursion worth exploiting here: AI is very good at helping you build the artifacts this chapter describes, as long as you keep the judgment human.

- **Drafting eval cases.** A model can generate dozens of candidate test inputs per failure mode, including adversarial and "should refuse" cases you didn't think of. You and your domain expert curate them.
- **Clustering error notes.** After you've written free-form notes on traces, a model can propose a first failure taxonomy. Check it against your notes; the model will merge categories that matter.
- **Writing judge prompts.** A model can draft a narrow judge for one failure mode. You must still validate it against human labels. An unvalidated judge is a second model's opinion, not a measurement.
- **Building the cost model.** Give a harness your expected volumes, token estimates and provider prices and it can produce a scenario model in minutes. Check every input yourself.
- **Red-teaming.** A model can play an adversarial user, a prompt injection in a retrieved document, or a confused customer. It finds different weaknesses than your team does.

The guardrail: **never let a model grade its own work unvalidated, and never let it decide what "good" means.** Those are the two decisions that make an eval meaningful.

## The Beacon case: the wrong rollback

:::example What happened
Three weeks into the Beacon Agents design-partner pilot, a responder at a retail customer accepts the agent's diagnosis that a deploy to the checkout service caused a latency spike, and rolls it back. The real cause was a database failover in a different region. The rollback takes checkout down for eleven minutes during a sale. The customer's VP of IT Operations calls Northlight's CEO.
:::

**The immediate response.** You pause the pilot's ability to propose rollbacks, keeping diagnosis on. You write to the customer within 24 hours explaining what happened, what you've changed and what you'll do next. The incident goes in the decision log and the risk register, and it becomes the first entry in a new AI incident review process (Chapter 33).

**Error analysis.** You and the applied AI engineers pull 120 pilot traces and read them. Free-form notes cluster into a failure taxonomy of seven modes. The top three:

1. **Recency bias.** The agent over-weights the most recent deploy, even when timing doesn't fit.
2. **Single-region blindness.** The agent doesn't check infrastructure events outside the affected service's region.
3. **Overconfident framing.** Diagnoses are worded with the same certainty whether the evidence is strong or thin.

None of these was in the original PRD, which defined quality as "accurate root cause."

**The eval suite.** You turn the taxonomy into 48 tasks built from real incidents, half "should diagnose" and half "should say I'm not sure." Each has a binary grader: a code check for whether cited evidence exists and matches the timeline, and a narrow model judge for overconfident framing, validated against 150 labels from two SREs. Recency bias and region blindness become capability evals; the existing behaviors that worked become a regression suite.

**The targets.** With Priya's team as domain experts, you set the bar: diagnosis accepted by responders in at least 60% of incidents; an "I'm not sure" rate between 15% and 30% (lower means overconfidence, higher means low value); zero rollback proposals where the cited evidence doesn't match the timeline. Because responders see the agent every incident, you track pass^3 on the regression suite, not just single-run accuracy.

**Autonomy and UX.** Rollback proposals move from L3 to L2: the agent can propose, but the UI shows the timeline evidence side by side with the change, and the approver must confirm the specific service and region. Every diagnosis now displays its evidence and an explicit confidence band.

**Cost.** The fix isn't free. Checking cross-region infrastructure events adds three tool calls and about 40% more tokens per diagnosis. Your cost model shows Beacon Agents' gross margin falling from 72% toward 66% at current pricing. You route the first-pass triage to a smaller model and cache the stable runbook context, which brings the projected margin back to about 71%. The margin floor goes in the AI PRD: 70%.

**Pricing.** The incident sharpens the per-resolved-incident pricing question. Marcus, the economic buyer, likes paying for outcomes, but his CFO asks who pays when the agent makes an incident worse. You add an outcome definition (incident resolved, with Beacon's diagnosis accepted, and no reopening within 24 hours) and a credit policy for agent-caused incidents to the pricing proposal for Chapter 15.

**The result.** Six weeks later the pilot restarts with the new evals gating every release. Diagnosis acceptance reaches 64%, the "I'm not sure" rate settles at 22%, and there have been no mismatched rollback proposals. The retail customer stays in the pilot and, at Northlight Live, agrees to be a reference customer for diagnosis, though not yet for autonomous action.

## Product 360 artifacts

```template id="ai-prd-addendum" title="AI PRD addendum"
# AI PRD addendum · [Feature] · v[n] · [Date]

Attach to the standard PRD. Every section is required for AI-powered features.

## 1. Why AI
- The user problem (link to PRD):
- Why a rule-based solution isn't enough:
- Cost-of-error table:

| Error type | Example | Cost to user | Cost to business | Detectable by user? |
|---|---|---|---|---|
| False positive | | | | |
| False negative | | | | |
| Harmful or inappropriate output | | | | |
| Wrong action (agents) | | | | |

## 2. Pattern and autonomy
- Pattern: augmented model / chain / routing / parallel / orchestrator / evaluator-optimizer / agent
- Why the simpler patterns weren't enough:
- Autonomy per action class:

| Action class | Reversibility (cheap / costly / irreversible) | Autonomy (L1 to L5) | Approval and confirmation design |
|---|---|---|---|
| | | | |

- Stopping conditions and budgets: max steps [n], max tokens [n], max time [n], max spend per task [$]
- Escalation path when a limit is hit:

## 3. Quality (link to eval plan)
- Failure taxonomy (top modes):
- Capability eval targets:
- Regression eval threshold (target near 100%):
- Consistency target (pass^k):
- Accountable domain expert:

## 4. Models and data
- Models and providers (link to model register):
- Fallback when the provider is unavailable or degraded:
- Grounding sources and how they're permissioned:
- Personal and customer data handled, retention, residency:
- Training and feedback use permitted by contracts: yes / no / with consent
- Feedback signals captured and where they're stored:

## 5. Cost and latency (link to AI cost model)
- Cost per task at expected volume:
- Gross-margin floor:
- Latency budget: time to first token [ms], end to end [s]
- Cost levers in use: routing / caching / workflow caching / budgets

## 6. Trust and failure UX
- How capability and limits are communicated:
- Sources and confidence display:
- "I don't know" state:
- Correction, undo and regenerate:
- AI disclosure:
- Graceful degradation:
- Anti-rubber-stamping design (for approvals):

## 7. Risk and regulation (link to AI risk assessment)
- Our role: provider / deployer
- Likely risk tier and jurisdictions:
- Transparency and documentation duties:
- Security threats considered: prompt injection, data exfiltration, credential misuse

## 8. Rollout
| Stage | Entry criteria (evals and production evidence) | Who sees it | Exit criteria |
|---|---|---|---|
| Shadow | | | |
| Assisted | | | |
| Supervised | | | |
| Autonomous (allowlisted actions) | | | |

- Kill switch: who can pull it, and how fast it takes effect:
```

```template id="eval-plan" title="Eval plan"
# Eval plan · [Feature] · [Date]

**Owner:** [PM or domain expert]   **Engineering owner:** [Name]   **Last run:** [Date]   **Gates releases:** yes / no

## Error analysis
- Traces reviewed: [n] on [dates], from [source]
- Reviewers:
- Failure taxonomy:

| # | Failure mode | Description | Example trace | Frequency in sample | Severity (H/M/L) |
|---|---|---|---|---|---|
| 1 | | | | | |

## Eval suite
| Suite | Type | # tasks | Grader (code / model judge / human) | Target | Current |
|---|---|---|---|---|---|
| [Failure mode 1] | Capability | | | | |
| [Existing behaviors] | Regression | | | ≥ 98% | |
| Should refuse or say "I'm not sure" | Capability | | | | |
| Consistency | pass^[k] | | | | |

## Judge validation (for each model judge)
| Judge | Failure mode | Human labels | True positive rate | True negative rate | Last validated |
|---|---|---|---|---|---|
| | | | | | |

## Run policy
- Runs on: every prompt change / model change / provider change / release
- Regression failure policy: block release / require approval from [name]
- Production sampling: [n] traces per [week], reviewed by [name]
- New failures from production become eval cases within [n] days

## History
| Date | Change | Capability score | Regression score | Notes |
|---|---|---|---|---|
| | | | | |
```

```template id="ai-cost-model" title="AI cost model"
# AI cost model · [Feature] · [Date]

**Owner:** [PM]   **Finance partner:** [Name]   **Prices as of:** [Date]

## Per-task cost
| Step | Model | Calls per task | Input tokens | Output tokens | Cached share | Cost per call | Cost per task |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| **Total** | | | | | | | **$** |

Include retrieval, tool and infrastructure costs per task.

## Volume and margin
| Scenario | Tasks per month | Inference cost | Other COGS | Revenue | Gross margin |
|---|---|---|---|---|---|
| Low | | | | | |
| Expected | | | | | |
| High | | | | | |

- Gross-margin floor: [%]
- Cost per task at which the floor is breached: [$]

## Levers
| Lever | Expected saving | Quality risk | Status |
|---|---|---|---|
| Route [step] to a smaller model | | | |
| Cache [stable context] | | | |
| Convert [recurring path] to deterministic code | | | |
| Lower step or token budget | | | |

## Sensitivities
- If tokens per task rise 50%:
- If the provider raises prices 20%:
- If usage doubles in a quarter:
```

```template id="model-register" title="Model and vendor register"
# Model and vendor register · [Product] · [Date]

| Feature | Model and version | Provider | Hosting region | Data sent | Training on our data? | Contract and DPA | Fallback model | Deprecation date | Last eval run | Owner |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

## Change policy
- Any model, version or provider change requires a regression eval run and sign-off from [name].
- Deprecation notices are reviewed [monthly]; migrations are planned at least [n] months before the date.
- Customers are notified of material model changes per [contract terms].
```

```template id="ai-risk-assessment" title="AI risk assessment"
# AI risk assessment · [Feature] · [Date]

**Owner:** [PM]   **Reviewers:** [security, legal, privacy, responsible AI]   **Next review:** [Date]

## System description
- What it does, for whom, and what decisions or actions it influences:
- Our role: provider / deployer
- Jurisdictions and likely risk classification (confirm with counsel):

## Risks
| # | Risk | Category (accuracy, bias, privacy, security, safety, IP, transparency, over-reliance) | Likelihood | Impact | Mitigations | Residual risk | Owner |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |

## Controls
- Human oversight design:
- Logging and audit (what is retained, for how long, who can access it):
- Transparency to users:
- Security: prompt injection, data exfiltration, credential scope:
- Monitoring and incident response (link):

## Documentation customers may request
- [ ] System description and intended use
- [ ] Data handling and residency
- [ ] Evaluation results and known limitations
- [ ] Human oversight and controls
- [ ] Incident response process
- [ ] Relevant certifications or framework alignment (for example ISO/IEC 42001, NIST AI RMF)

## Sign-off
| Role | Name | Date | Decision |
|---|---|---|---|
| | | | |
```

## Prompts

```prompt title="Open-code a batch of AI traces"
Goal: Get a fast first pass of error notes on real traces, to speed up (not replace) your own error analysis.
Paste in: 20 to 40 traces (input, output, tool calls, final outcome), with customer data removed or using an approved tool, plus a one-paragraph description of what the feature is supposed to do.

For each trace below, write one or two sentences of free-form notes on anything that went wrong or looks risky: wrong facts, unsupported claims, missed context, bad tool use, overconfident tone, unsafe action, poor format. If nothing went wrong, write "OK." Don't score with a rating scale. Don't group the notes yet.

Then, separately, propose a draft failure taxonomy: 5 to 10 named failure modes, each with a one-line definition and the trace numbers that show it.

[feature description]
[traces]

Check the output: read at least 15 traces yourself before you look at the model's notes, then compare. Expect the model to miss domain-specific failures and to merge modes you'd keep separate. The final taxonomy is yours.
```

```prompt title="Generate eval cases for one failure mode"
Goal: Build a balanced set of test cases quickly.
Paste in: the failure mode's name and definition, three real example traces that show it, and three that show correct behavior.

Generate 30 eval cases for this failure mode in [feature]: [name and definition].
- 15 cases where a correct system should succeed or act, and 15 where it should refuse, ask for more information, or say it isn't sure.
- Vary difficulty: include obvious cases and subtle ones.
- Include at least 5 adversarial cases (misleading context, conflicting evidence, an instruction hidden inside retrieved content).
- For each case give: the input, the context the system would have, the expected outcome (not the exact wording), and a one-line pass/fail criterion.

Base the cases on the real examples; don't invent product capabilities the examples don't show.

[examples]

Check the output: have your domain expert review every case. Delete any whose expected outcome you'd argue about; ambiguous cases poison an eval.
```

```prompt title="Draft and validate a model judge"
Goal: Create a narrow LLM-as-judge for one failure mode, plus a plan to validate it.
Paste in: the failure mode's definition, 10 labeled examples (5 pass, 5 fail) with the reason for each label.

Write a judge prompt that checks one thing only: [failure mode]. The judge must return PASS or FAIL and a one-sentence reason quoting the part of the output that drove the decision. Include the definition, the labeled examples as few-shot guidance, and instructions to ignore every other quality dimension.

Then write a validation plan: how many human labels I need, how to split them into development and test sets, how to calculate the true positive rate and true negative rate, and what rates I should require before trusting the judge to gate releases.

[definition and examples]

Check the output: run the judge on a held-out set you labeled yourself. Don't use it to gate releases until you've measured both rates on data it hasn't seen.
```

```prompt title="Build a first AI cost model"
Goal: See the gross-margin effect of an AI feature before it ships.
Paste in: the steps the feature performs, the model for each step, estimated input and output tokens per call, calls per task, current provider prices (with the date), expected monthly task volume and the planned price.

Build a cost model for [feature] with:
1. A per-task cost table by step, including caching assumptions.
2. Monthly cost, revenue and gross margin at low, expected and high volume.
3. The cost per task at which gross margin falls below [floor]%.
4. Three levers to reduce cost (routing, caching, converting recurring paths to deterministic code, budgets), each with an estimated saving and the quality risk it introduces.
5. Sensitivity to tokens per task rising 50% and prices rising 20%.

Show your formulas. Don't invent prices; use only the ones I gave you, and flag any input you had to assume.

[inputs]

Check the output: recompute one scenario by hand. Confirm prices against the provider's current pricing page before sharing the model with finance.
```

```prompt title="Review an agent's autonomy design"
Goal: Find autonomy and permission gaps before a customer does.
Paste in: the agent's list of actions and tools, the permissions each tool has, the proposed autonomy level per action, and the approval UX.

Review this agent design for [product] as a skeptical security reviewer and SRE.
1. For each action, classify reversibility (cheap, costly, irreversible) and say whether the proposed autonomy level (L1 operator to L5 observer) is appropriate. Recommend changes.
2. Identify any tool with broader permissions than its actions need.
3. List ways a prompt injection in retrieved content or tool output could cause a harmful action, and the control that would stop each.
4. Check stopping conditions and budgets. What happens when a limit is hit?
5. Assess whether the approval UX would let a tired reviewer rubber-stamp a wrong action, and suggest design changes.
Finish with the five changes you'd require before production.

[design]

Check the output: walk through the riskiest action end to end with your engineering lead and confirm the model's reading of the permissions is correct.
```

```prompt title="Red-team an AI feature"
Goal: Find failure modes your team hasn't imagined.
Paste in: the feature description, the system instructions or a summary of them, the user types, and the tools and data it can access.

Act as a red team for [feature]. Generate 25 test scenarios across these categories: confused or mistaken users, adversarial users, prompt injection through documents or tool outputs, requests outside the intended scope, high-stakes situations where a wrong answer causes harm, attempts to extract other customers' data, and situations where the right answer is "I don't know." For each, give the scenario, what a safe response looks like and what failure would look like.

Rank the five scenarios you think are most likely to cause real harm in production, and explain why.

[feature details]

Check the output: run the top-ranked scenarios against the real system. Add every failure you find to the eval suite.
```

```prompt title="Review an AI PRD for gaps"
Goal: Make sure an AI PRD covers what classic PRDs miss.
Paste in: the PRD and its AI addendum.

Review this PRD for an AI-powered feature. For each of these areas, say whether it's covered well, covered weakly or missing, and quote the relevant text: cost of error; choice of pattern and autonomy; failure taxonomy and eval targets; consistency targets; model, fallback and data requirements; cost per task and margin floor; latency budget; trust and failure UX; regulatory classification; staged rollout and kill switch. Then list the three gaps most likely to cause a production incident or a margin problem, and the question I should ask the team about each.

[PRD]

Check the output: confirm each "covered well" against the PRD yourself. Bring the three questions to your next review.
```

## Anti-patterns

:::warn Vibe checks
The team tries a dozen prompts, the answers look good, and the feature ships. Quality is never measured, so nobody notices when a model update makes it worse. If there's no eval suite gating releases, there's no quality bar.
:::

:::warn Agents for everything
A multi-step agent is built for a task a single model call with the right context could do. It's slower, costlier and harder to evaluate. Start with the simplest pattern that works.
:::

:::warn One autonomy level for the whole product
The agent is either fully supervised (and users find it tedious) or fully autonomous (and someone gets hurt). Set autonomy per action class, based on reversibility.
:::

:::warn The margin surprise
The feature succeeds, usage grows, and finance discovers gross margin has fallen ten points. Cost per task and a margin floor belong in the PRD, and on the monthly dashboard.
:::

:::warn Unvalidated judges
A model grades the outputs, the scores look great, and nobody has checked whether the judge agrees with humans. An unvalidated judge measures nothing.
:::

:::warn Human in the loop, in name only
Every action requires approval, reviewers approve 99.8% of them in under two seconds, and the one wrong action sails through. Design approval screens that make wrong output easy to see, and audit a sample of approvals.
:::

:::warn Regulation at the end
The product is built, and then legal asks for logging, documentation and human-oversight evidence it doesn't have. Classify regulatory exposure at the start, and build the evidence in.
:::

## Checklist

- [ ] A cost-of-error table exists, and it drives eval targets, autonomy and UX.
- [ ] The PRD explains why AI is the right tool, and why simpler patterns weren't enough.
- [ ] Autonomy is set per action class, with a reversibility map and approval design for anything costly or irreversible.
- [ ] Stopping conditions and budgets (steps, tokens, time, spend) are defined, with an escalation path.
- [ ] Error analysis on at least 30 real traces produced a failure taxonomy.
- [ ] The eval suite has capability and regression sets, binary graders, validated judges and consistency (pass^k) targets, and it gates releases.
- [ ] A named domain expert owns the definition of "good."
- [ ] The AI cost model shows cost per task, gross margin at three volumes and a margin floor.
- [ ] The model and vendor register lists every model, version, provider, data flow, fallback and deprecation date.
- [ ] The trust UX covers sources, confidence, "I don't know," correction, disclosure and graceful degradation, and it was reviewed against the human-AI interaction guidelines.
- [ ] Regulatory role, risk tier and documentation duties are recorded, and counsel has reviewed them.
- [ ] The rollout is staged (shadow, assisted, supervised, autonomous) with evidence-based entry and exit criteria and a kill switch.
- [ ] Production monitoring covers quality, cost, latency, corrections and escalations, and production failures become eval cases.
- [ ] Any MCP server or API that agents use to reach the product has an owner, scope, authentication, versioning and pricing position.
- [ ] The eval plan, cost model, model register and risk assessment are linked from the Product 360 index.

## Key takeaways

- AI products behave like distributions, cost money per use and earn trust one answer at a time. Specifying, measuring, pricing and running them is different from classic software.
- Start with the cost of being wrong. It sets your eval targets, autonomy levels and UX, and often your pricing.
- Use the simplest pattern that works. Reserve agents for open-ended tasks, and set autonomy per action class based on how reversible each action is.
- Evals are the PRD's acceptance criteria in executable form. Build them from error analysis on real traces, use binary graders and validated judges, and track consistency, not just best-case accuracy.
- Cost per task and gross margin are product requirements. Falling token prices don't guarantee falling task costs, and AI margins run well below classic SaaS.
- Design for calibrated trust: show evidence, make "I don't know" a good answer, make correction cheap and stop human review from becoming a rubber stamp.
- Regulation is now a product input. Record your role, risk tier and obligations at the start, and build the evidence into the product.
