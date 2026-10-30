<p class="lead">Technical product management is the part of the job where the customer may be a developer, another team or an AI agent, and where the riskiest questions are about how the system behaves. This chapter covers why products fail, how development processes manage that risk, the fluency you need to hold your own in a design review, and how to frame, read and check experiments when an AI harness does the arithmetic.</p>

## Why this matters

Most senior PMs can write a good problem statement. Fewer can follow an architecture review and say what a design choice will cost customers in a year. The gap matters most in B2B, enterprise and platform businesses, because so much of the product is invisible: APIs, data models, reliability targets, permission scopes, versioning policies and per-request costs. Customers experience those decisions later, as outages, broken integrations, stalled security reviews and price increases.

Three shifts make this urgent in 2026.

**Building got cheap.** Marty Cagan's 2026 essay on the AI productivity paradox argues that teams ship faster with AI tools while results stay flat, because faster building inside an output-driven model produces more of the wrong things.

**The customer set changed.** Postman's 2025 State of the API report, a survey of more than 5,700 developers, architects and executives, found that 65% of organizations generate revenue from their APIs. Yet only 24% of developers design APIs with AI agents in mind, and 51% named unauthorized or excessive API calls from agents as their top security concern. Agents are API consumers now.

**Evidence work moved into the harness.** An AI model connected to your experiment platform will analyze an A/B test and answer fluently every time. Whether the answer is right depends on how you framed the question and which checks you demand.

These topics sit in the Build and Measure dimensions of your Product 360 (Chapter 00), underneath Chapter 05 (analytics and experiments), Chapter 06 (working with engineering) and Chapter 11 (delivery methodologies).

## What makes a PM technical

### A working definition

There's no authoritative definition of "technical product manager." Some companies mean a PM with an engineering degree; others mean someone who coordinates engineering work. This book defines the role by the product, not the person:

**A technical PM is a PM whose customers, product surface or dominant risks are technical, so they must reason about feasibility, architecture and operational tradeoffs directly instead of delegating them.**

Cagan's four product risks give the frame: value (will they buy or use it?), usability (can they figure it out?), feasibility (can we build and run it?) and viability (does it work for the business?). On a technical product, feasibility and viability move to the front, and the "user" is often a developer, an internal team or a piece of software. You can't hand those risks to the tech lead and wait for a verdict, because the tradeoffs inside them are product decisions: which customers get which guarantees, what you promise not to change, and what each call costs.

### Four variants of the role

The craft is the same across technical products, but the customer and the dominant risk change. Name both before you choose a process or a metric.

**Platform PMs.** Matthew Skelton and Manuel Pais's *Team Topologies* describes four team types (stream-aligned, platform, enabling and complicated subsystem) and three interaction modes (collaboration, X-as-a-Service and facilitation). A platform team provides a compelling internal product that speeds up stream-aligned teams by taking complexity off their plate. "Compelling" is the product test: if teams use your platform only because a mandate forces them to, what you've built is a dependency. Chapter 14 covers external platform strategy.

**API PMs.** An API is a promise. Steve Yegge's 2011 "platforms rant" recalls, from his time at Amazon, a mandate that every team expose its functionality only through service interfaces that could be offered to outside developers. Treat that as Yegge's recollection rather than documented Amazon policy. **Hyrum's Law**, Hyrum Wright's observation popularized by Titus Winters, is the API PM's daily reality: with enough users, every observable behavior of your system will be depended on by somebody, whatever the documentation says. Stripe's engineering blog (Brandur Leach, 2017) describes one public answer: date-named API versions, each account pinned to the version current at its first call, and older response shapes produced by applying each breaking change in reverse. Google's API Design Guide, used inside Google since 2014, covers resource names, standard methods, errors, versioning and backward compatibility.

**Infrastructure PMs.** Here reliability is the product, and the Google SRE book's chapter on service level objectives supplies the vocabulary. A **service level indicator (SLI)** is a precisely defined measure of one aspect of service, such as latency. A **service level objective (SLO)** is a target for an SLI. A **service level agreement (SLA)** is a contract with consequences, usually financial, for missing an SLO. The **error budget** is the failure the SLO allows. Setting an SLO is a product decision, because reliability and speed of change compete for the same engineering time.

**AI/ML PMs.** AI outputs vary from run to run and cost money on every call (Chapter 31). Quality has to be measured with evals before value is tested with experiments, and inference cost is a margin line you own. Beacon's gross margin fell from 81% to 72% after agentic features launched, mostly because of inference cost.

:::onramp If you're new to technical products
Ask two questions about any piece of work: "Who calls this?" and "What happens to them if we change it?" If the first answer includes another team, a partner's code or an AI agent, you're doing technical product management, whatever your title says.
:::

## Why products fail

You can't choose a process to manage risk until you know which risks kill products. Three sources help.

### What startup post-mortems say

CB Insights' 2026 analysis of startup failures examined 431 venture-backed companies that shut down publicly since 2023 and identified reasons for 385. Companies could have several reasons, so the shares add up to more than 100%: 70% ran out of capital, 43% had poor product-market fit, 29% cited bad timing or macro conditions and 19% had unsustainable unit economics.

CB Insights itself notes that running out of capital is usually the final cause of death rather than the root problem. The product-relevant root causes are poor fit and unsustainable unit economics, and the second matters more in 2026, because AI features carry a per-use cost. Mind the limits: these are self-reported explanations for venture-backed companies after the zero-interest-rate era. They make good pre-mortem prompts and weak causal proof.

### Cagan's root causes of failed product efforts

Cagan's 2015 SVPG essay on the root causes of product failure, also a chapter of *Inspired*, looks inside established companies and argues that most failed efforts share a process. Paraphrased, his ten root causes are: (1) ideas come from sales and stakeholders, and the team becomes implementers; (2) business cases demand predictions nobody can know yet; (3) roadmaps are prioritized feature lists, though many features won't deliver; (4) the product role shrinks to documenting requirements; (5) design arrives too late, only to polish; (6) engineering arrives too late to contribute ideas; (7) agile is applied only to delivery; (8) funding goes to projects rather than outcomes; (9) all the risk sits at the end, because customers validate only after the build; and (10) the opportunity cost of the whole process.

His alternative is continuous discovery alongside continuous delivery, with roadmaps of problems instead of features. Causes 6 and 9 are where a technical PM has the most leverage: bring engineers into discovery, and test feasibility early with spikes instead of finding a hard constraint in month five.

### The feature factory

John Cutler's 2016 post "12 Signs You're Working in a Feature Factory" names the pattern from inside a team. Paraphrased, the signs are: no measurement of impact; people shuffled between projects without stable missions; success theater around launches; little scrapped work; work disconnected from core metrics; no retrospectives on product decisions; heavy prioritization with no checking afterward; no iteration after launch; hand-offs that keep the team away from research and from customers after release; large batches; deal-driven features that ignore complexity costs; and invisible technical debt. In a later follow-up for Amplitude, Cutler added that teams usually fall into the factory through good intentions, such as locking a roadmap early to protect overloaded designers.

Cagan's productivity paradox gives the 2026 twist: AI coding tools turn a feature factory into a faster one. For technical PMs the common symptom is the deal-driven connector, built to close one customer and then maintained, versioned and secured forever.

:::key Three lenses, one pre-mortem
Post-mortem data shows which outcomes kill companies, Cagan shows which processes produce them, and Cutler shows how those processes feel from inside. Use all three as pre-mortem prompts.
:::

### The pre-mortem

Gary Klein's 2007 *Harvard Business Review* article "Performing a Project Premortem" supplies the method. The leader announces that the project has already failed, each person silently writes every plausible reason why, and the group shares reasons one at a time to strengthen the plan. Declaring the failure as a fact gives knowledgeable worriers permission to speak while their concerns are still cheap to act on. Klein builds on research by Mitchell, Russo and Pennington on "prospective hindsight": imagining that an outcome has already happened makes it easier to explain. For technical products, put engineering, security and support in the room, because the failures that kill platform and AI products are often technical and commercial at once.

## How products get built: processes compared

Every development process is a theory about where risk lives and when to retire it. Most enterprise organizations run several at once: funding on top, delivery underneath and, in good teams, discovery alongside.

**Sequential ("waterfall").** The model of requirements, design, implementation, verification and maintenance in strict order is usually traced to Winston Royce's 1970 paper "Managing the Development of Large Software Systems." Royce presented the sequential model and then wrote that it "is risky and invites failure," because testing comes last and problems found there force redesign. His five fixes were to do a preliminary program design first, document the design, do the job twice (build a pilot first), plan and monitor testing, and involve the customer formally. The third and fifth are prototyping and customer collaboration by other names. "Waterfall" as most teams practice it keeps Royce's sequence and drops his fixes.

**Stage-Gate.** Robert Cooper's model divides development into stages, where the team gathers information through market research, technical tests and customer validation, and gates, where management decides to continue, stop or redirect the investment. Cooper frames it as an information model for reducing uncertainty and an investment model for managing risk, which is why it survives in portfolio governance at companies that call themselves agile. His Agile Stage-Gate hybrid runs sprints inside each stage. The common failure is gates that never kill anything. If your gate reviews haven't stopped a project in a year, they aren't gates.

**Agile.** The 2001 Manifesto for Agile Software Development values individuals and interactions over processes and tools, working software over comprehensive documentation, customer collaboration over contract negotiation, and responding to change over following a plan. Agile fixed the delivery problem Royce described by getting working software in front of people early and often. On its own it doesn't decide what's worth building, which is Cagan's root cause 7.

**Lean.** Eric Ries's *The Lean Startup* (2011), introduced in Chapter 01, makes validated learning the unit of progress through a build-measure-learn loop. In enterprise, a minimum viable product must clear a much higher bar for security and support, and "measure" often means a handful of design partners.

**Dual-track.** Desirée Sy's 2007 paper on agile user-centered design describes interaction designers working at least one cycle ahead of developers in a separate track. Jeff Patton popularized **dual-track development** and clarified it in "Dual Track Development is not Duel Track" (2017): one process with two kinds of concurrent work. Discovery aims to learn fast; development aims to build predictably at high quality. The whole team takes part in discovery, which kills or changes many ideas. In Patton's words, "The whole team is responsible for product outcomes, not just on-time delivery."

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 270" role="img" aria-label="Dual-track development: a discovery track and a delivery track running in parallel, with validated ideas flowing down and production learning flowing back up">
  <text x="20" y="34" class="t">Discovery track</text><text x="20" y="52" class="s">Learn fast: is it valuable, usable, feasible, viable?</text>
  <rect x="20" y="64" width="150" height="50" rx="10" class="box"/><text x="34" y="86" class="t">Frame problem</text><text x="34" y="104" class="s">outcome, risks</text>
  <rect x="190" y="64" width="150" height="50" rx="10" class="box"/><text x="204" y="86" class="t">Prototype, spike</text><text x="204" y="104" class="s">feasibility early</text>
  <rect x="360" y="64" width="150" height="50" rx="10" class="box"/><text x="374" y="86" class="t">Test with users</text><text x="374" y="104" class="s">evals, partners</text>
  <rect x="530" y="64" width="170" height="50" rx="10" fill="var(--a3)" fill-opacity=".14" stroke="var(--a3)" stroke-opacity=".6"/><text x="544" y="86" class="t">Killed or changed</text><text x="544" y="104" class="s">most ideas end here</text>
  <line x1="170" y1="89" x2="190" y2="89" class="ln"/><line x1="340" y1="89" x2="360" y2="89" class="ln"/><line x1="510" y1="89" x2="530" y2="89" class="ln"/>
  <line x1="435" y1="114" x2="435" y2="162" stroke="var(--a1)" stroke-width="2"/>
  <text x="445" y="144" class="s" style="fill:var(--a1)">validated idea, ready to build</text>
  <text x="20" y="150" class="t">Delivery track</text><text x="20" y="168" class="s">Build well: predictable, high quality</text>
  <rect x="20" y="180" width="200" height="50" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".6"/><text x="34" y="202" class="t">Sprint n</text><text x="34" y="220" class="s">build, test, release</text>
  <rect x="240" y="180" width="200" height="50" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".6"/><text x="254" y="202" class="t">Sprint n+1</text><text x="254" y="220" class="s">build, test, release</text>
  <rect x="460" y="180" width="240" height="50" rx="10" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)" stroke-opacity=".6"/><text x="474" y="202" class="t">Production learning</text><text x="474" y="220" class="s">experiments, SLOs, support signals</text>
  <line x1="220" y1="205" x2="240" y2="205" class="ln"/><line x1="440" y1="205" x2="460" y2="205" class="ln"/>
  <line x1="680" y1="180" x2="680" y2="114" stroke="var(--a2)" stroke-width="2" stroke-dasharray="5 4"/>
  <text x="560" y="254" class="s">learning feeds the next round of discovery</text>
</svg>
<figcaption>Dual-track development is one team doing two kinds of work at once. Discovery retires value, usability, feasibility and viability risk before delivery invests in production quality, and what ships feeds evidence back into discovery.</figcaption>
</figure>

| Process | Where it fits in B2B and platform work | Main failure mode |
|---|---|---|
| **Sequential** | Fixed-scope contracts, regulated deliverables, hardware, known migrations | Expensive problems surface last |
| **Stage-Gate** | Portfolio funding and big platform bets | Gates that never kill |
| **Agile** | Delivering software increments | Agile only in delivery, requirements still dictated |
| **Lean** | New products and new segments | MVPs too thin for enterprise buyers |
| **Dual-track** | The default for product teams in 2026 | Two separate teams, discovery treated as a phase |

Cagan's 2026 distinction between building to learn and building to earn adds the AI-era overlay. Building to learn means prototypes made to test value, usability, feasibility and viability; building to earn means production-quality delivery. As AI lowers the cost of building, discovery becomes the bottleneck, so a team that uses AI only to write code faster is speeding up the track that was never the constraint.

:::leader For product leaders
Write down which process governs which decision: usually gates for funding, sprints for delivery and a weekly rhythm for discovery. Trouble starts when a gate review demands a feature list or a sprint review sets strategy.
:::

## The technical fluency you need

A Principal PM doesn't design the system, but needs to understand it well enough to spot product decisions in disguise and recognize a weak answer. Five areas cover most of it.

**Architecture.** Be able to draw your product's system-context diagram from memory: main components, external systems, where data lives, and which calls are synchronous (the caller waits) or asynchronous (the work happens later through a queue or event). Much customer-visible behavior follows from that picture. If a diagnosis waits on five synchronous calls to customer tools, it's as slow as the slowest one. If actions go through a queue, "approved" and "executed" are different moments, and the UI has to say which one the user is seeing.

**APIs.** For any API you own or depend on, know its resources and methods, authentication, scopes, rate limits, versioning and what it has promised not to change. Know the difference between an additive change (a new field or endpoint, usually safe) and a breaking one (removing or renaming a field, changing a default, tightening validation). Because of Hyrum's Law, ask "what observable behavior changes?" before "what does the contract say?"

**Data models.** Know the main entities, how they relate and what identifies each one. In B2B add **tenancy** (whose data is this, and how is it kept apart?) and **residency** (which region holds it?). "Show an MSP a combined view across its customers" is a tenancy question before it's a screen.

**System design tradeoffs.** Four come up in almost every decision:

- **Consistency, availability and latency.** Eric Brewer's 2012 retrospective on his CAP theorem argues that "pick two of three" misleads: the choice is made per operation and per piece of data, it's a matter of degree, and it matters mainly during network partitions, which are rare but real. As he puts it, "CAP prohibits only a tiny part of the design space." The product question is what each user should see, and what should be allowed to happen, when part of the system can't reach another part.
- **Reliability versus speed of change**, set by the error budget.
- **Cost per request**, which for AI features scales with usage, context length and model choice.
- **Reversibility.** A public API shape, a data model or a pricing unit is expensive to undo. Spend review time in proportion.

**Reading a design doc.** Malte Ubl's 2020 description of design docs at Google is a good model of what to expect: context and scope; goals and non-goals; the design itself, emphasizing tradeoffs; **alternatives considered**, which Ubl calls one of the most important sections; and cross-cutting concerns such as security, privacy and observability. Large projects might run 10 to 20 pages and a mini design doc 1 to 3. Read one as a PM in five passes:

1. **Goals and non-goals against the PRD** (Chapter 04).
2. **Alternatives considered.** Were cheaper or more reversible options weighed?
3. **Cross-cutting concerns.** Which customer promises does it touch: security, residency, latency, cost?
4. **Interfaces.** Who calls this, and what breaks for existing callers?
5. **What's missing.** Ask what would make the team regret this in a year.

Many teams also keep **architecture decision records (ADRs)**, a format Michael Nygard proposed in 2011: one to two pages with a title, the context, the decision ("We will..."), a status (proposed, accepted, deprecated or superseded) and the consequences, good and bad. ADRs are superseded, never deleted. Before asking engineering to change a component, read its ADR history to learn what the team knowingly gave up.

:::ai Let the harness read first
Connected to your repositories and wiki, a harness can summarize a design doc against your PRD, list the ADRs behind a component and draft review questions. Use it to prepare, then read the alternatives-considered section yourself, because a summary flattens exactly that judgment.
:::

## Experiments and analysis

Chapter 05 covers instrumentation and the experiment readout. This section covers the concepts you need to frame a test, read results honestly and check a harness's analysis. You don't need formulas; you need to know what each concept protects you from.

### Framing the question

Before launching a controlled experiment, write down:

- **The decision** it informs, who makes it, and **the hypothesis**.
- **The primary metric.** Ron Kohavi, Diane Tang and Ya Xu, in *Trustworthy Online Controlled Experiments*, call it the **overall evaluation criterion (OEC)**: a quantitative measure of the experiment's objective, ideally one that predicts long-term value.
- **Guardrail metrics.** They describe two kinds: organizational guardrails such as latency, errors and cost, which the change must not harm, and trust guardrails, which tell you whether the experiment itself is sound.
- **The unit of randomization**: user, account, team or tenant. In B2B, randomizing users inside one customer often contaminates the test, because colleagues share runbooks. Randomizing by account is cleaner but gives far fewer units.
- **The minimum effect worth detecting**: the smallest change that would alter the decision.
- **The sample size and stopping rule**, fixed in advance.

### Getting the data into shape

Most wrong experiment answers come from the data feeding the analysis, not from the statistics. The harness does the joining and cleaning, but you decide the rules, and you should write them down before anyone sees a result:

- **Which units count.** Who was eligible, and which units are excluded: internal and test accounts, partner sandboxes, bots and synthetic monitors. In B2B a single load-testing tenant can outweigh dozens of real ones.
- **How assignment joins to outcomes.** Every metric row has to trace back to the group the unit was assigned to, not the group it happened to see. Ask what happens to units that switched groups or appear in both.
- **Exact metric definitions.** "Acceptance rate" needs a numerator, a denominator, a time window and a rule for repeats. Two reasonable definitions can produce opposite answers.
- **How outliers are handled.** One very large account can move an average on its own. Decide in advance whether to cap values or report a median as well.
- **Gaps and duplicates.** Ask for counts of missing and duplicated events by group. A logging gap that hits one group more than the other looks exactly like an effect.

Ask the harness to state each of these rules back to you, with the row counts before and after each exclusion, before it reports any effect.

### Significance and power, as concepts

A **p-value** answers a narrow question: if the change had no effect, how surprising would data like these be? The American Statistical Association's 2016 statement, by Ronald Wasserstein and Nicole Lazar, sets out six principles. Paraphrased: a p-value indicates how incompatible the data are with a specified model; it doesn't measure the probability that the hypothesis is true; decisions shouldn't rest only on crossing a threshold; inference needs full reporting; a p-value doesn't measure the size or importance of an effect; and alone it isn't a good measure of evidence. "Statistically significant" means "unlikely to be pure noise under the assumptions," so always ask for the **effect size with a confidence interval** as well.

**Power** is the chance the experiment detects a real effect of the size you care about. An underpowered test often misses real effects, so "no significant difference" from a small test tells you little. B2B products hit this constantly: a few hundred customers can't power an account-level test of a small effect in a week. The honest options are a longer run, a larger minimum effect, a different unit or a different method.

**Peeking** is the most common way PMs break their own experiments. Evan Miller's 2010 post "How Not To Run an A/B Test" explains that significance calculations assume a sample size fixed in advance. In his illustration, a change with no real effect, checked repeatedly and stopped at the first reading significant at 5%, came out a false positive about 26% of the time. Fix the sample size before launch, or use a sequential or Bayesian design built for planned checkpoints.

### Interpreting results

Read a result in a fixed order, and stop if an early check fails.

1. **Check the split.** A **sample ratio mismatch (SRM)**, as Aleksander Fabijan and colleagues define it in their 2019 KDD paper, is an observed ratio of units between groups that differs from the designed ratio, a sign that assignment, logging or eligibility is broken. Kohavi and colleagues treat the SRM check as a trust guardrail for every experiment. If it fails, the result can't be trusted.
2. **Read the primary metric**: effect size, interval and significance, as planned.
3. **Read the guardrails.** A primary-metric win that breaks latency, cost or error rates isn't a win.
4. **Read only planned segments.** Slice enough ways and something will look significant by chance. Treat unplanned segments as exploratory hypotheses.
5. **Apply Twyman's law.** Kohavi and colleagues use it as a rule of thumb: a result that looks surprising or unusually good is more often a mistake than a discovery.

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 150" role="img" aria-label="Reading order for experiment results: split check, primary metric, guardrails, planned segments, decision, with a stop if the split check fails">
  <rect x="10" y="30" width="122" height="56" rx="10" fill="var(--a3)" fill-opacity=".14" stroke="var(--a3)" stroke-opacity=".6"/><text x="22" y="54" class="t">1. SRM check</text><text x="22" y="74" class="s">is the split sound?</text>
  <rect x="152" y="30" width="122" height="56" rx="10" class="box"/><text x="164" y="54" class="t">2. Primary</text><text x="164" y="74" class="s">effect and interval</text>
  <rect x="294" y="30" width="122" height="56" rx="10" class="box"/><text x="306" y="54" class="t">3. Guardrails</text><text x="306" y="74" class="s">cost, latency, errors</text>
  <rect x="436" y="30" width="122" height="56" rx="10" class="box"/><text x="448" y="54" class="t">4. Segments</text><text x="448" y="74" class="s">planned ones only</text>
  <rect x="578" y="30" width="130" height="56" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".6"/><text x="590" y="54" class="t">5. Decide</text><text x="590" y="74" class="s">surprising? recheck</text>
  <line x1="132" y1="58" x2="152" y2="58" class="ln"/><line x1="274" y1="58" x2="294" y2="58" class="ln"/><line x1="416" y1="58" x2="436" y2="58" class="ln"/><line x1="558" y1="58" x2="578" y2="58" class="ln"/>
  <line x1="71" y1="86" x2="71" y2="112" stroke="var(--a3)" stroke-width="2"/>
  <text x="20" y="132" class="s" style="fill:var(--a3)">Fails? Stop. Find the cause. Report no effects.</text>
</svg>
<figcaption>Read every experiment result in the same order, and brief the AI harness to use it too. A failed split check ends the analysis, however good the primary metric looks.</figcaption>
</figure>

### When you can't A/B test

Many B2B decisions can't be randomized cleanly, such as pricing under contract or admin features used by a few people per account. The alternatives are weaker but honest: staged rollouts with a comparison group, long-running holdouts, switching a change on and off over time, or before-and-after comparisons against a similar group. Name the method and its weaknesses in the readout.

For AI features, add a step first. Cagan's October 2026 essay "Experimentation, AI and the Product Model" argues that because AI products are probabilistic, teams should use evals early to establish quality and reserve the costlier A/B tests for establishing value.

## How to apply it

This method takes a significant technical bet (a platform capability, a public API, an AI feature) from idea to evidence. It assumes you have a product hypothesis (Chapter 01) and an outcome target (Chapter 02), and it runs over four to eight weeks alongside normal delivery.

1. **Name the customer and the dominant risk.** Write one sentence naming who calls or uses the capability: a person, a developer, an internal team or an AI agent. Rate Cagan's four risks plus adoptability, the B2B lens from Chapter 01, then match the process: spikes and prototypes for feasibility risk, customer tests for value risk, a gate for a large funding ask.
2. **Run a failure pre-mortem** with the product trio plus security, support and a sales or partner lead. Announce that the bet failed a year from now, give everyone five silent minutes, then prompt for gaps with the three lenses. Rank the reasons and give each top risk an owner, an early-warning signal and a mitigation.
3. **Get fluent on this bet.** Rate yourself on the fluency self-assessment and close the two biggest gaps before the design review. Draw the system-context diagram yourself and compare it with engineering's; the differences are your questions.
4. **Review the design as a PM** in five passes, using the technical design review checklist. Ask that every hard-to-reverse decision be recorded as an ADR.
5. **Write the interface promise.** If the bet exposes an API, platform service or MCP server, write the API and platform product brief, with an explicit section on what agents may call and what needs a human approval.
6. **Plan the evidence.** For AI capabilities, define the evals that establish quality (Chapter 31) and don't expose customers until they pass. Write the experiment plan before launch: decision, hypothesis, primary metric, guardrails, unit, minimum effect, sample size and stopping rule. If you can't randomize, name the alternative and its weaknesses.
7. **Analyze with the harness, then check it.** Send an experiment analysis request with the pre-registered plan and outputs in a fixed order, SRM check first. Reconcile group counts against the platform, ask the harness to critique its own analysis, and for important decisions have a fresh session or second model reproduce the headline numbers. Record the decision, evidence and limits in the decision log.

## The AI lens

### Building AI-powered and agent-facing products

**Agents are a customer segment.** Agents explore, retry, chain calls and act at machine speed for a human who may not be watching. Your API brief needs an agent section: permitted operations, scopes, rate limits, attribution to a human and revocation. The **Model Context Protocol (MCP)** has become the common way to expose a product to agents. Anthropic introduced it in November 2024 and in December 2025 donated it to the Agentic AI Foundation, a fund under the Linux Foundation co-founded by Anthropic, Block and OpenAI; by then there were more than 10,000 active public MCP servers. An MCP server is an API product with every obligation in this chapter, and agents will depend on its tool descriptions as surely as developers depend on field names.

**Quality comes before value.** AI behavior drifts when models or prompts change. Run evals before experiments, and treat a model or prompt change as a product change that needs its own evidence.

**Cost belongs in the design review.** For every AI capability, ask for cost per call and per outcome at expected and peak usage.

**Experiments need AI-aware guardrails.** Add guardrails for wrong or harmful outputs, cost per outcome and latency, and for agents, the rate of actions a human had to undo.

### Doing the work with AI

In 2026 your harness reaches the experiment platform, warehouse, ticketing and repositories through connectors, often MCP servers. You stop exporting data and start writing briefs, and analysis quality depends on the clarity of the request, the context you supply and the checks you run.

Experimentation tools are moving into AI and observability platforms. Datadog announced its acquisition of the experimentation company Eppo in May 2025, and OpenAI announced in September 2025 that it would acquire the experimentation platform Statsig. Vendors also ship agents that summarize results; Optimizely's guidance for its agent recommends asking for a specific comparison (named variations, named metrics, significance and a summary table) instead of a vague request to analyze the test. That advice suits any harness. No vendor publishes independent evidence of how accurate these summaries are, so verification stays with you.

The harness pulls data and runs standard checks well once you name them. It will also answer a vague question confidently, pick a plausible metric that isn't your pre-registered one, or skip the SRM check unless asked. Cagan's 2026 advice on coaching with AI applies: configure the model with your context, ask it for critique rather than affirmation, and re-check important conclusions because models aren't deterministic. In practice:

- **Supply the plan with the data.** The pre-registered hypothesis, metric definitions, unit and stopping rule make the question checkable.
- **Fix the order of outputs**, SRM first, with an instruction to stop if it fails.
- **Reconcile one number yourself.** If the group sizes differ from the experiment platform's, nothing else matters yet.
- **Ask for assumptions and a critique.** "What would a skeptical statistician say about this analysis?" tends to surface the assumptions a fluent summary hides.
- **Reproduce important calls** in a fresh session or with a second model.

:::ai The harness does the arithmetic. You own the question.
A harness can't know which decision the experiment was meant to inform, what you committed to measure before launch, or whether the result fits everything else you know about customers. Put those three in the request, then check the answer against them.
:::

## The Beacon case: a technical review of Beacon Agents

:::example Where Beacon starts
After the discovery work in Chapter 01, Beacon is building diagnosis first and supervised action second, with audit logs, scoped credentials and a kill switch moved forward on the roadmap. Leadership wants to announce Beacon Agents at Northlight Live. As Principal PM you have three technical jobs first: pressure-test the launch, review the design of the Act capability's approval gate, and prove that a new diagnosis layout helps responders before it reaches all 420 customers.
:::

**The fluency check.** On the self-assessment you rate yourself weak in two areas the launch depends on: data residency, because EU customers want AI Act documentation, and inference cost, because gross margin has already fallen from 81% to 72%. You spend an hour with the applied AI engineers on how cost per diagnosis scales with retrieved data, and ask the harness to summarize the ADRs behind Beacon's regional data stores.

**The pre-mortem.** You run 60 minutes with the trio, a Northlight security architect, a support lead and the partner manager for Leo's MSP. The premise: six months after Northlight Live, Beacon Agents has failed. The reasons cluster into four main stories:

| Failure story | Lens | Early-warning signal | Mitigation (owner) |
|---|---|---|---|
| A hallucinated root cause leads a customer to roll back the wrong service, and the story spreads | Fit; risk at the end | Acceptance rate falls or undo rate rises in the pilot | Evals on resolved incidents gate every exposure; evidence shown with each diagnosis (applied AI lead) |
| Security reviewers block write access without audit logs and AI documentation | Adoptability | Security review time in pilot deals | Per-action audit log and kill switch before Act; AI Act documentation pack (PM, security) |
| Inference cost pushes margin below 72% at scale | Unit economics | Cost per diagnosis by tenant size | Cost budget per diagnosis in the design; cheaper model for triage (tech lead) |
| Connectors break when an observability vendor changes its API | Hyrum's Law, reversed | Connector error rates | Contract tests against partner APIs; connector SLOs (platform PM) |

Two Cutler signs also surface: a prospect's demand for a bespoke connector, and no post-launch review of the last two correlation releases. Both go to the roadmap review.

**The design review.** Reviewing the Act team's design doc for the approval gate with the checklist, you raise five questions:

- *Scope:* is the allowlist per tenant or global? Leo's MSP runs operations for 60 customers with different risk tolerances, so it has to be per tenant.
- *Reliability:* what's the SLO for approval latency? If Dana approves a rollback at 3 a.m. and execution waits in a queue, the UI must show "approved, executing" separately from "done."
- *Reversibility:* what happens if the rollback itself fails? The doc covers the action, not undoing it.
- *Data:* where do EU tenants' audit logs live, and for how long? The doc assumes one region.
- *Alternatives:* only a synchronous approval call was considered. You ask for the asynchronous option to be written up.

The regional audit-log decision becomes an ADR, with the cost of a second store under consequences.

**The interface promise.** Leo's MSP wants to trigger approved runbook steps from its own tooling. Your brief for a Beacon Actions API and MCP server specifies tenant-scoped tokens, per-tenant rate limits, every action attributed to a named human approver, date-based versions in the style Stripe describes, and deprecation aligned with the Beacon Classic sunset (Chapter 30). Agents may read diagnoses and request actions; only a human approval or the customer's allowlist can execute one.

**The experiment.** Design has a new diagnosis layout that puts the cited evidence above the proposed root cause. It first runs against the diagnosis evals to confirm it doesn't change which root cause is shown. The plan names diagnosis acceptance rate as the primary metric, with MTTR, wrong-action rate and inference cost per incident as guardrails. Randomization is by tenant, because responders on one team would otherwise see both layouts. With about 420 customers, power is limited, so the plan fixes a longer run.

A quick look at the experiment dashboard shows a clear, significant lift. But your analysis request puts the SRM check first, and it fails: the planned 50/50 split of tenants came out noticeably uneven. The harness traces the cause to provisioning. One MSP onboarded its customers through a bulk path that bypassed the assignment service and defaulted every new tenant to the new layout. Those smaller tenants already had higher acceptance, so most of the "lift" came from who was in each group.

The team fixes assignment and reruns the test. The second run shows a smaller lift with healthy guardrails, and the layout ships. The decision log records both runs and the SRM failure's cause.

## Product 360 artifacts

These artifacts belong in the Build and Measure dimensions of your Product 360. The experiment analysis request works alongside the experiment design and readout templates in Chapter 05; the API and platform brief complements the developer platform brief in Chapter 14, which covers ecosystem strategy rather than the interface promise.

```template id="07-technical-design-review" title="Technical design review checklist (PM questions)"
# Technical design review · [Design doc title] · [Date]

**Reviewer:** [PM]   **Doc owner:** [Tech lead]   **Linked PRD:** [link]   **Decision needed by:** [Date]

## 1. Problem and outcome
- [ ] The doc's context and goals match the PRD's problem and outcome metric.
- [ ] Notes:

## 2. Non-goals
- [ ] Every non-goal is acceptable to customers, sales, support and partners.
- [ ] Non-goals that need to be communicated externally: [list]

## 3. Who calls this
- [ ] Callers are named: human users / developers / internal teams / AI agents / partners.
- [ ] For each caller, what changes for them: [notes]

## 4. Alternatives considered
- [ ] At least one cheaper, simpler or more reversible option was weighed.
- [ ] The reason for rejecting each alternative is stated.

## 5. Data
- [ ] What is stored, where (region), for how long, under which tenant: [answer]
- [ ] Residency and retention match customer commitments.

## 6. Reliability
- [ ] Proposed SLIs and SLOs: [list]
- [ ] Error budget and what happens when it's spent.
- [ ] Failure behavior: what each user sees when a dependency is down.

## 7. Compatibility
- [ ] Observable behaviors that change for existing callers (ordering, timing, defaults, error text): [list]
- [ ] Versioning and migration plan for breaking changes.

## 8. Security and privacy
- [ ] Least-privilege access and scopes.
- [ ] Audit logging, including actions taken by agents and who approved them.
- [ ] Revocation path (kill switch, token revocation).

## 9. Cost
- [ ] Unit cost per request and per customer outcome, at expected and peak usage: [numbers]
- [ ] Margin impact: [estimate]

## 10. Observability and rollback
- [ ] How we'll know it works in production: [signals]
- [ ] How we undo it, including undoing a failed rollback.

## 11. Reversibility
- [ ] Decisions that are hard to reverse (public interface, data model, pricing unit) are flagged: [list]

## 12. Decisions to record
| Decision | ADR number | Status |
|---|---|---|
| | | |

## The regret question
What would make us regret this design in a year? [answer]

## Outcome
Approve / Approve with changes / Revise and re-review. Changes requested: [list]
```

```template id="07-api-platform-brief" title="API and platform product brief"
# API and platform product brief · [Interface or service name] · v[n] · [Date]

**Owner:** [PM]   **Tech lead:** [name]   **Status:** Draft / In review / Published

## Customers
| Customer type | Who specifically | Their job to be done | Volume expected |
|---|---|---|---|
| External developers | | | |
| Partners | | | |
| Internal teams | | | |
| AI agents (via API or MCP server) | | | |

## The interface promise
- Resources and operations offered: [list]
- Events or webhooks emitted: [list]
- What we promise never to change without a new version: [list]
- Observable behaviors we know callers depend on (Hyrum's Law check): [list]

## Versioning and deprecation
- Versioning scheme: [date-based / numbered / other]
- What counts as a breaking change: [definition]
- Deprecation notice period and migration support: [policy]

## Reliability
- SLIs and SLO targets: [list]
- SLA, if any, and its consequences: [terms]
- Error budget policy: [what happens when it's spent]

## Limits and access
- Rate limits and quotas, by customer tier: [table]
- Authentication method and scopes: [list]
- Least-privilege defaults: [description]

## Agent readiness
- Operations agents may call: [list]
- Operations that require a human approval: [list]
- Agent rate limits and attribution (which human each agent acts for): [policy]
- MCP server: yes / no / planned. Tool descriptions owned by: [name]

## Commercials
- Pricing or internal chargeback unit: [unit]
- Cost to serve per unit: [estimate]

## Adoption and success
- Adoption metric: [active integrations, time to first successful call, share of target teams using it]
- Health metrics: [error rate, breakage reports, support tickets per integration]

## Documentation and onboarding
- Reference docs, samples and quickstart: [links]
- Time to first successful call target: [time]

## Open questions
1.
2.
```

```template id="07-failure-premortem" title="Failure pre-mortem"
# Failure pre-mortem · [Initiative] · [Date]

**Facilitator:** [name]   **Participants:** [product trio, security, support, sales or partner lead, others]

## The premise
It is [date, 6 to 12 months out]. [Initiative] has failed. Write down every plausible reason why, on your own, before anyone speaks.

## Prompts (use after silent writing, to find gaps)
- Market and product fit: did customers need it badly enough? Was the timing wrong?
- Unit economics: did cost to serve or pricing make it unsustainable?
- Process (Cagan's root causes): were ideas dictated by stakeholders? Did engineering or design arrive too late? Did all the risk sit at the end?
- Feature factory signs (Cutler): no measurement, deal-driven features, no tweaking after launch, hand-offs, invisible debt?
- Technical: compatibility breaks, reliability, security review, data residency, cost at scale?

## Raw reasons
| # | Reason | Raised by |
|---|---|---|
| 1 | | |

## Ranked risks
| Rank | Failure story | Likelihood (H/M/L) | Damage (H/M/L) | Early-warning signal | Mitigation | Owner | Review date |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

## Changes to the plan
1.
2.

## Revisit
At each milestone: which early-warning signals have moved?
```

```template id="07-experiment-analysis-request" title="Experiment analysis request"
# Experiment analysis request · [Experiment name] · [Date]

Use this brief as the prompt to an AI harness or the request to an analyst. If it includes customer data, use an approved tool.

## The decision
- Decision this informs: [ship / iterate / stop / roll back]
- Decision maker: [name]

## The plan, as written before launch
- Hypothesis: [text, copied from the plan]
- Unit of randomization: [user / account / team / tenant]
- Expected split: [for example, 50/50]
- Primary metric (OEC) and definition: [metric]
- Guardrail metrics and definitions: [list]
- Minimum effect worth detecting: [value]
- Stopping rule and planned sample size: [rule]
- Pre-registered segments: [list, or "none"]

## Data
- Sources (connector or system names): [list]
- Date range: [start to end]
- Known data issues: [list]
- Exclusions (internal, test and sandbox accounts, bots): [list]
- Outlier rule (cap, median or none): [rule]

## Required outputs, in this order
0. Data preparation: each exclusion applied, with unit counts by group before and after; counts of missing and duplicated events by group.
1. Sample ratio mismatch check: observed versus expected split, and whether it fails. If it fails, stop and report likely causes; do not report effects.
2. Primary metric: effect size, confidence interval and significance, as planned.
3. Guardrails: status of each, with intervals.
4. Pre-registered segments only.
5. Plain-language summary in under 150 words.
6. Assumptions made about data and method.
7. Data-quality caveats.
8. What result would change the conclusion.

## Not allowed
- Changing the primary metric or its definition.
- Reporting new segments unless labeled "exploratory."
- Declaring a winner if the SRM check fails or the stopping rule wasn't met.

## Verification (completed by the requester)
- [ ] Group counts match the experiment platform.
- [ ] Primary metric and segments are the pre-registered ones.
- [ ] Harness critiqued its own analysis; issues raised: [list]
- [ ] For major decisions, a second pass reproduced the headline numbers.
```

```template id="07-technical-fluency-self-assessment" title="Technical fluency self-assessment"
# Technical fluency self-assessment · [Name] · [Quarter]

Rate each area 1 to 4. 1 = I need someone to explain it to me. 2 = I can follow the discussion. 3 = I can ask the questions that expose tradeoffs, without help. 4 = I can teach it and spot a weak answer.

| Area | Behavioral anchor for a 3 | Rating (1 to 4) | Evidence |
|---|---|---|---|
| Architecture | I can draw our system-context diagram and explain which calls are synchronous | | |
| APIs | I can say which proposed changes are breaking and why | | |
| Data models | I can explain our main entities, tenancy and residency | | |
| Reliability | I can propose SLOs and explain the error budget tradeoff | | |
| Security and privacy | I can explain our access model, scopes and audit trail | | |
| Cost | I know our unit cost per request and per customer outcome | | |
| Experimentation | I can frame a test and spot SRM, peeking and segment fishing | | |
| AI systems | I can explain our evals, retrieval and agent permissions | | |
| Design docs | I can review a design doc and find the hard-to-reverse decisions | | |

## Two areas to grow this quarter
1. Area: [ ]   Plan: [who will teach me, what I'll read in our own docs, what I'll practice]   Evidence of progress: [ ]
2. Area: [ ]   Plan:   Evidence of progress:

## Review
Re-rate at the end of the quarter with your tech lead's input.
```

```template id="07-feature-factory-check" title="Feature factory check"
# Feature factory check · [Team] · [Quarter]

Score each sign 0 (not true), 1 (sometimes true) or 2 (true). Signs paraphrased from John Cutler.

| Sign | Score (0 to 2) | Evidence |
|---|---|---|
| We don't measure the impact of what we ship | | |
| People move between projects without a stable mission | | |
| Launches are celebrated; outcomes aren't checked | | |
| We rarely kill or scrap work | | |
| Work isn't connected to core metrics | | |
| We don't review past product decisions | | |
| We prioritize hard but never check whether priorities paid off | | |
| We don't iterate after launch | | |
| Hand-offs keep the team away from research and from customers after release | | |
| We ship in large batches | | |
| Deal-driven features ignore complexity cost | | |
| Technical debt and refactoring are invisible | | |

**Total:** [ ] of 24

## AI acceleration check
Has AI-assisted building increased our output without improving outcomes? [evidence]

## Two changes for next quarter
1.
2.
```

## Prompts

```prompt title="Review a design doc as a PM"
Goal: Find the product decisions hidden in an engineering design doc before you approve it.
Paste in: the design doc, the PRD it implements and any customer commitments it touches (SLAs, residency, security terms). Use an approved tool if the doc is confidential.

Act as a senior product manager reviewing this design doc for [product]. Compare it with the PRD.

1. List any gap between the doc's goals and non-goals and the PRD's problem and outcome. Flag non-goals that customers, sales or partners would object to.
2. Summarize the alternatives considered and the stated reason each was rejected. If only one option is discussed, say so, and suggest one cheaper or more reversible alternative worth writing up.
3. List every customer promise the design touches: security, data residency and retention, latency, availability, cost. For each, say whether the doc addresses it.
4. List the callers of any interface (users, developers, internal teams, AI agents) and what changes for each. Name any observable behavior that changes, even if it isn't documented.
5. Identify the decisions that would be expensive to reverse and should be recorded as ADRs.
6. Write ten questions for the design review, most important first.

Quote the doc when you cite it. Don't assume facts that aren't in the material.

[design doc]
[PRD]

Check the output: read the alternatives-considered section yourself and compare it with the summary. Confirm every quoted line exists in the doc. Drop any question you can answer from the doc in under a minute.
```

```prompt title="Run a failure pre-mortem"
Goal: Generate a broad, ranked list of failure stories for a major bet, as preparation for a team pre-mortem.
Paste in: the plan or PRD, the launch date, the target customers, the business model and known constraints.

It is [date, 6 to 12 months after launch] and [initiative] has failed. Write the most plausible failure stories, each in two or three sentences, in the past tense.

Cover all of these lenses:
- Market and fit: customers didn't need it badly enough, or timing was wrong.
- Unit economics: cost to serve, inference cost or pricing made it unsustainable.
- Process: ideas came from stakeholders, design or engineering joined too late, all the risk sat at the end, or the team worked as a feature factory.
- Technical: compatibility breaks, reliability, security review, data residency, cost at scale.
- Adoption: the buying group, security or procurement blocked it.

For each story, give a likelihood (H/M/L), damage (H/M/L), the earliest signal that would warn us, and one mitigation. Rank by likelihood times damage.

Don't soften the stories. Base them on the plan provided; mark any story that depends on an assumption not in the material.

[plan]

Check the output: use it after the team's silent writing round, not before, so it widens the list rather than anchoring it. Delete generic stories that would apply to any product. The useful ones mention your customers, your architecture or your pricing.
```

```prompt title="Draft an API and platform product brief"
Goal: Turn engineering's interface design into a product promise that customers, partners and agents can rely on.
Paste in: the API spec or design doc, the target customers, any SLOs and the existing versioning or deprecation policy.

Using the material provided, draft an API and platform product brief for [interface or service] with these sections: customers (developers, partners, internal teams, AI agents); the interface promise; observable behaviors callers are likely to depend on even though they aren't documented; versioning and deprecation; reliability (SLIs, SLOs, any SLA); limits and access (rate limits, scopes, least-privilege defaults); agent readiness (which operations agents may call, which need human approval, attribution, MCP server plan); commercials; adoption and success metrics; open questions.

Rules:
- Mark every field the material doesn't support as "Open question" rather than filling it in.
- List any change in the spec that would break existing callers.
- Flag any operation that lets an agent change customer systems without a human approval or allowlist.

[material]

Check the output: walk the "breaking changes" and "agent operations" lists with the tech lead. Confirm the rate limits and SLOs match what engineering can operate, not what sounds good.
```

```prompt title="Write an experiment plan before launch"
Goal: Pre-register an experiment so the analysis can't drift after the data arrives.
Paste in: the hypothesis, the feature, the customer base (number of accounts and users, how they're grouped) and the metrics available.

Help me write an experiment plan for [feature]. Ask me questions until you can fill every field, then produce the plan:

- The decision this informs and who makes it.
- Hypothesis.
- Primary metric (one) with a precise definition.
- Guardrail metrics: business guardrails (latency, error rate, cost, and for AI features wrong-output and undo rates) and the sample ratio check.
- Unit of randomization, and why. Consider whether users within the same account would contaminate each other.
- Minimum effect worth detecting, in terms of the decision.
- Whether we have enough units to detect it in a reasonable time. Explain the tradeoff in plain language; don't show formulas.
- Stopping rule, fixed in advance.
- Pre-registered segments.
- If a randomized test isn't feasible, the best alternative method and its weaknesses.
- For AI features, the evals that must pass before exposure.

[hypothesis and context]

Check the output: make sure there's exactly one primary metric and the stopping rule is a rule, not "when it looks significant." If the plan says the test can't reach a useful answer, believe it and change the design.
```

```prompt title="Analyze experiment results through the harness"
Goal: Get a trustworthy analysis of a finished experiment, in an order that catches broken experiments first.
Paste in (or connect the harness to): the pre-registered experiment plan and the experiment platform or warehouse tables. Use only tools approved for customer data.

Analyze the experiment [name] using the data in [sources] for [date range]. The plan below was written before launch. Follow it exactly.

Produce, in this order:
1. Sample ratio mismatch check: expected versus observed split of [unit]. If the check fails, stop. Report the mismatch and the most likely causes, and don't report any effects.
2. Primary metric [name, definition]: effect size, confidence interval and significance.
3. Each guardrail [names]: effect and interval, and whether it breached its threshold.
4. Pre-registered segments only: [list]. Anything else must be labeled "exploratory."
5. A plain-language summary under 150 words for [decision maker].
6. Every assumption you made about the data and the method.
7. Data-quality caveats.
8. What result would change the conclusion.

Don't change the primary metric, don't add segments unless they're labeled exploratory, and don't declare a winner if the stopping rule wasn't met.

[experiment plan]

Check the output: compare the group counts with the experiment platform yourself. Confirm the metric definitions match the plan. Then run the critique prompt in this chapter on the result.
```

```prompt title="Critique an analysis before you act on it"
Goal: Find the weaknesses in an experiment analysis, whether a harness, an analyst or a vendor tool produced it.
Paste in: the analysis, the pre-registered plan and the raw summary counts from the experiment platform.

Act as a skeptical statistician reviewing this analysis before a product decision. Don't be agreeable; I want the problems.

1. Does the analysis follow the plan: same primary metric, unit, segments and stopping rule? List every deviation.
2. Was a sample ratio mismatch check done, and does the split in the analysis match the platform counts I've supplied?
3. Is there any sign of peeking (stopping early) or of segments chosen after seeing the data?
4. Is the effect size practically meaningful, and how wide is the interval? What decision would a result at each end of the interval support?
5. Does any result look too good or surprising? List checks to rule out a data or logging problem.
6. What else could explain the result besides the change being tested?

[analysis]
[plan]
[platform counts]

Check the output: for any deviation it finds, go back to the source data or the analyst before deciding. For a major decision, run the original analysis again in a fresh session or with a second model and compare the headline numbers.
```

```prompt title="Build your technical fluency on a system"
Goal: Get up to speed on the architecture behind your product, using your own company's documents as the textbook.
Paste in (or connect the harness to): design docs, ADRs, architecture diagrams and runbooks for [system]. Use an approved tool for internal documents.

I'm the PM for [product] and I want to understand [system] well enough to review designs and spot product tradeoffs. Using only the documents provided:

1. Describe the system-context: main components, external systems, where data lives (including region and tenancy) and which calls are synchronous or asynchronous.
2. Summarize the ADR history: the five decisions that most shape the system today, what each gave up, and which are hard to reverse.
3. Explain the reliability targets and how close we run to them, if the documents say.
4. Explain what drives cost per request.
5. Quiz me with eight questions, one at a time, starting easy and getting harder. After each answer, tell me what I got right and what I missed, citing the source document.

Cite the document for every claim. If the documents don't cover something, say so rather than filling the gap from general knowledge.

Check the output: draw the system-context diagram yourself, then compare it with the tech lead's. Ask about every difference. Re-rate yourself on the fluency self-assessment afterward.
```

## Anti-patterns

:::warn The requirements translator
The PM turns stakeholder requests into tickets and hands them to engineering. Engineers never hear the customer problem, so they can't propose the cheaper solution they'd have seen. That's Cagan's root causes 1, 4 and 6 at once. Bring engineers into discovery, and bring them problems.
:::

:::warn The faster feature factory
The team adopts AI coding tools, doubles its release rate and celebrates. Outcomes don't move, and every new feature adds maintenance, compatibility and security surface. Measure outcomes, scrap what doesn't earn its keep and spend the extra capacity on discovery.
:::

:::warn The undocumented promise
A platform team changes the order of results in an API response because the documentation never promised it, and integrations break across hundreds of customers. Under Hyrum's Law, observable behavior is the contract. Treat any change to it as a compatibility decision.
:::

:::warn Rubber-stamping the design review
The PM skims the design doc, sees nothing about the UI and approves. Six months later the data model can't support per-tenant settings, and EU residency needs a second datastore nobody budgeted for. Read for alternatives, data, cost and reversibility.
:::

:::warn Peeking and segment fishing
The PM stops the test the first day it shows significance, then finds a segment where the effect looks strong. Each step raises the odds of a false positive. Fix the stopping rule and segments before launch, and label everything else exploratory.
:::

:::warn Trusting the fluent readout
A harness or vendor agent produces a confident summary declaring a winner, and nobody checks the split or the metric. Brief it with the pre-registered plan, demand the SRM check first and reconcile the counts yourself.
:::

:::warn A/B testing an unmeasured model
An AI feature goes straight into an A/B test with no evals. When results disappoint, nobody can tell whether the idea failed or the model had a bad week. Establish quality with evals before you test value with customers.
:::

## Checklist

- [ ] For each major capability, the customer (human, developer, internal team, agent) and the dominant risk are named, and the process matches the risk.
- [ ] A failure pre-mortem with engineering, security and support has produced ranked risks with owners, signals and mitigations.
- [ ] The team has scored itself on the feature factory check this quarter.
- [ ] You can draw the system-context diagram and explain the main data entities, tenancy and residency.
- [ ] You've completed the fluency self-assessment and are working on two named areas.
- [ ] Every significant design doc has a PM review covering goals, alternatives, data, reliability, compatibility, security, cost and reversibility, and hard-to-reverse decisions are recorded as ADRs.
- [ ] Every API, platform service or MCP server has a product brief with versioning, SLOs, limits, scopes and an agent section.
- [ ] AI capabilities pass evals before any customer experiment.
- [ ] Every experiment has a pre-registered plan with one primary metric, guardrails, a unit of randomization and a stopping rule.
- [ ] Every analysis starts with an SRM check, reports effect sizes with intervals and labels unplanned segments exploratory.
- [ ] AI-produced analyses are reconciled against platform counts and critiqued before anyone decides.

## Key takeaways

- The product defines a technical PM: when the customers, surface or dominant risks are technical, you reason about feasibility and operational tradeoffs yourself. Name the customer and the dominant risk first.
- Post-mortems point to fit and unit economics, Cagan to a process that pushes risk to the end, and Cutler to how that process feels from inside. Use all three in a pre-mortem.
- Every development process is a theory about where risk lives. Gates govern funding, agile governs delivery, and dual-track discovery retires most product risk.
- Technical fluency means seeing the product decisions inside architecture, APIs, data models and tradeoffs: what you promise not to change, what reliability you guarantee, what each call costs and what's hard to reverse.
- Fix the metric, unit and stopping rule before launch, check the split before reading results, and read effect sizes with intervals rather than a significance verdict.
- An AI harness can run the analysis, but you own the question and the checks: brief it with the plan, demand the SRM check first, reconcile the counts and ask for a critique.
