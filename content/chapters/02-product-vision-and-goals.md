<p class="lead">A vision says what change the product exists to make. Goals say what should be measurably different this quarter because of it. This chapter builds the chain between the two: a vision people can repeat, a business broken into parts someone owns, a North Star with a tree of inputs beneath it, and OKRs that name behavior changes rather than features to ship.</p>

## Why this matters

Most product organizations have a vision and a goal system, and the two rarely connect. The vision lives on a slide from an offsite. The goals live in a planning tool and read like a release list: ship the connector, launch the dashboard, hit the date. Ask why a team is building a particular feature this quarter, and nobody can trace the answer back to the vision without hand-waving.

That gap costs you three ways. Teams optimize for output, so the organization ships a lot and learns little. Leaders lose the ability to say no, because without a stable purpose every request looks as reasonable as the next. And when results disappoint, nobody can tell whether the vision, the strategy or the execution was wrong, because the layers were never written down separately.

The fix is a chain of artifacts, each answering one question:

1. **Vision**: what positive change does the product bring about, for whom, over the next several years?
2. **Decomposition**: what are the parts of the business and of the customer's workflow, and who owns each?
3. **North Star and metric tree**: what single measure best captures the value customers get, and which inputs drive it?
4. **OKRs**: what behavior change are we committing to this quarter, and how will we know?
5. **Goal review**: is the chain still holding, and what do we change?

These artifacts anchor the Strategy and Measure dimensions of your Product 360 (Chapter 00). They sit on top of the Customer dimension from Chapter 01: the vision describes a change for the personas you validated, and the North Star counts the job those personas hire you to do. Strategy and the roadmap (Chapter 03) then describe how you get there.

## Vision, goals and the layers between

### Vision, mission, strategy and goals

These words get used loosely. Some companies call their long-range aspiration a mission; others call the same thing a vision. No single usage is authoritative, so this book defines its own. Agree on yours with leadership before you argue about content.

| Layer | Question it answers | Typical horizon | Changes when | Measured by |
|---|---|---|---|---|
| **Mission** | What does the company exist to do? | Indefinite | Almost never | Not measured directly |
| **Product vision** | What positive change does this product bring about, and for whom? | Several years, often five or more | The purpose itself turns out to be wrong | Not measured directly |
| **Product strategy** | How will we realize the vision: which market, needs, standout features and business goals? | 12 to 24 months, reviewed at least quarterly | Evidence shows a better path | Business goals and KPIs |
| **Goals (North Star, OKRs)** | What should be measurably different this period? | A quarter to a year | Every cycle | Key results, inputs, guardrails |

The structure follows Roman Pichler's product strategy framework, revised in May 2026. Pichler stacks four layers: the product vision (the purpose, stable and not measurable), the product strategy (the approach, usually covering 12 to 24 months and reviewed at least every three months), the product roadmap (outcome-based product goals and metrics) and the product backlog. KPIs sit outside the stack, derived from the strategy, business goals and roadmap outcomes. He argues that OKRs can work at the roadmap level but don't suit the vision or the strategy.

Separating the layers lets each change at its own speed: you can pivot the strategy without losing the purpose. If your vision changes every time the strategy does, what you wrote was a strategy in inspirational language.

Marty Cagan draws the same line in his 2016 essay on vision versus strategy. The vision is the future the team is trying to create; the strategy is the sequence of products and releases that gets there.

### What a good vision does

Pichler describes the product vision as the overarching goal and the reason for creating the product: the positive change it should bring about. His advice, paraphrased: ground it in why you care; describe the change, not the product; keep it separate from the strategy; build it with the people who will use it; choose a vision that benefits others; make it broad and ambitious; keep it short; and use it as the first filter for ideas and change requests. His vision board checklist adds six qualities to test a draft against: inspiring, shared, ethical, concise, ambitious and enduring.

On horizon, the sources differ. Pichler has said a vision should guide the team for at least three to five years, and elsewhere five to ten. Cagan suggests two to five for most software, longer for hardware. Treat it as "several years, often five or more," and pick a number your organization will actually plan against.

The most common failure in 2026 is the **solution vision**, one that names the technology. Pichler's own illustration is a children's computer game: a description of the game and its interactive characters is not the vision, while helping children enjoy music and dancing is. The same test applies to AI products. "An AI coding assistant with autonomous agents" describes a product. A vision about the change developers experience survives the day the team learns that agents were the wrong mechanism. If your vision contains "AI," "agent," "platform" or a feature name, rewrite it.

For B2B products, describe the change in the customer's organization rather than in yours. "Become the leading AIOps vendor" is a company ambition. "On-call teams resolve incidents before customers feel them" is a product vision, and it tells every engineer what a good week looks like.

:::key The vision is the filter
A vision earns its keep when it settles arguments. A feature that doesn't move the customer toward the change the vision describes needs an unusually strong reason to be on the roadmap. If your vision can't reject anything, it's too vague.
:::

### Three formats: statement, board and narrative

One sentence rarely carries enough to steer a team. Use three formats, at different lengths, for different audiences.

**The vision statement** is one or two sentences: the change, and for whom. It goes at the top of every strategy document and quarterly review, and its job is to be remembered.

**The product vision board** is Pichler's one-page tool for connecting the vision to the first strategic choices. The statement runs across the top, with four sections beneath: **target group** (which market or segment, who uses and who buys), **needs** (the problem solved and the benefit provided), **product** (what it is and the three to five features that make it stand out) and **business goals** (how it benefits the company). An extended version adds competitors, revenue sources, cost factors and channels. Make one board per product, not per feature. For a platform, the target group usually needs several rows: users, the economic buyer, the security gatekeeper and partners.

Alongside the board, many teams write a **positioning-style vision**, adapted from the positioning statement Geoffrey Moore popularized in *Crossing the Chasm*. It runs roughly: for a named target customer with a stated need, or dissatisfied with the current alternative, the product is a member of a named category that delivers a key benefit; unlike the main alternative, it offers a stated difference. Strictly, it's a positioning statement, not a purpose vision in Pichler's sense. It earns a place beneath the vision because it forces you to name the category, the alternative and the difference. In B2B the alternative is often a manual process ("engineers, runbooks and chat") rather than a competitor, and if it differs by segment, write one line per segment. Chapter 24 develops positioning.

**The vision narrative** is the long form: a page or two describing the customer's world once the product has done its job. The best-known version is Amazon's Working Backwards practice, described by Colin Bryar and Bill Carr in *Working Backwards*. The team writes a press release announcing the finished product to customers, always under one page, followed by FAQs of five pages or less. Reviewers push on the "so what?" of every claim, and extra pages win nothing. Practitioners commonly split the FAQ into external questions (customers and press) and internal ones (cost, feasibility, risk, economics).

Writing the press release forces you to say what a customer would actually notice; writing the internal FAQ forces you to confront what will make it hard. Cagan's word for the same idea in other media is a **visiontype**: a narrative, storyboard or prototype that makes the future concrete enough to argue with. For enterprise products, write the release from both the daily user's and the economic buyer's points of view, and put the buying group's questions (security, procurement, data residency, partner economics) in the internal FAQ. Those questions decide whether the vision ships. Chapter 34 covers narrative craft.

### Breaking the business into parts

A vision describes the whole, but goals have to be owned by parts. Before setting goals, decompose the business into pieces small enough to own and large enough to matter. Four lenses help.

**Business model components.** Alexander Osterwalder and Yves Pigneur's Business Model Canvas splits a business into nine building blocks: customer segments, value propositions, channels, customer relationships, revenue streams, key resources, key activities, key partnerships and cost structure. Here the canvas shows which component each goal moves. A pricing change moves revenue streams and cost structure; a partner program moves channels and key partnerships. If a goal moves no component, question whether it's a business goal.

**Value streams.** The Scaled Agile Framework separates an **operational value stream** (the activities that deliver a product or service to a customer, such as a purchase order through to delivery) from a **development value stream** (the activities that turn a business hypothesis into a working solution). The customer's operational value stream is the most useful spine for decomposing a product and its metrics, because each stage is a place where value is created or lost.

**Team-aligned areas.** Matthew Skelton and Manuel Pais, in *Team Topologies*, describe four team types (**stream-aligned**, **enabling**, **complicated-subsystem** and **platform**) and three interaction modes (collaboration, X-as-a-service and facilitation). For goals, this means product areas should map to streams so each stream-aligned team can own a metric end to end, and platform teams should state their goals as service to the stream-aligned teams.

**Capability, segment and model.** Lay your product's capabilities against its segments and revenue components to see where goals overlap and where nobody owns anything.

Decomposition comes first because of ownership. A North Star fans out into inputs, and each input needs exactly one owning team. If two teams share an input, merge their goals or split the input. If an input has no team, it won't move.

## North Star and metric trees

### The North Star metric

Sean Ellis popularized the North Star metric, which he and Morgan Brown describe in *Hacking Growth*: the single metric that best captures the core value a product delivers to its customers. The emphasis is on one.

Amplitude turned the idea into a framework. Its North Star Playbook, co-authored by John Cutler, presents the North Star as a bridge between the language of the customer, the product and the business. In Amplitude's 2024 guidance, a good North Star metric does three things:

1. It **reflects customer value**: it rises when customers get more of what they hired the product for.
2. It **represents the product strategy**: it measures the bet you're making now.
3. It's a **leading indicator** of business success: it moves before revenue does.

Amplitude pairs the metric with a statement of product vision, so the North Star measures the current strategy toward a stable purpose. It warns against vanity metrics and against lagging financial measures, such as monthly recurring revenue or average revenue per user, as the North Star. Revenue is the result; the North Star is the customer behavior that produces it.

Amplitude also describes three "games" a product can play:

| Game | What it measures | Typical North Star shape |
|---|---|---|
| **Attention** | How much time customers are willing to spend in the product | Time engaged, sessions with depth |
| **Transaction** | How many transactions users make on the platform | Completed purchases, bookings, payments |
| **Productivity** | How efficiently and effectively someone gets their work done | Units of work completed with the product |

Most B2B software plays the productivity game, which rules out many tempting metrics. Logins, seats and time in product measure attention, and in a productivity product more time in the tool can mean the product is failing. Pick a metric at the customer's unit of value: incidents resolved, invoices approved, deployments shipped, contracts executed.

Platforms need one more decision. A platform has at least two sides, such as developers who build on it and the organizations that use what they build. State which side the North Star measures, and give the other side an input in the tree.

### The input-metric tree

The North Star is too slow and too aggregate for one team to steer by week to week. Amplitude's answer is **inputs**: three to five complementary factors that most directly drive the North Star and that the team can influence through the product. It suggests four lenses for finding them: **breadth** (how many customers get the value), **depth** (how much each gets), **frequency** (how often) and **efficiency** (how quickly or cheaply).

Arrange the result as a tree. The North Star sits at the root, the inputs beneath it, and beneath each input the drivers a single team can move in a quarter. Each input has one owning team, which is why the decomposition comes first.

This book adds an element the framework leaves implicit: **guardrails**. A guardrail is a counter-metric that must not cross a threshold while you push an input. Without one, a team can move its input by degrading something the tree doesn't show: faster diagnosis by guessing more, higher adoption by discounting, more automation by taking riskier actions. In B2B products, guardrails usually cover quality, trust, cost and customer health. Put them on the tree, next to the inputs they protect.

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 380" role="img" aria-label="A metric tree: the North Star at the root, four inputs beneath it, team drivers beneath each input, and a guardrail band along the bottom">
  <rect x="200" y="16" width="280" height="62" rx="10" fill="var(--a1)" fill-opacity=".14" stroke="var(--a1)"/>
  <text x="340" y="42" text-anchor="middle" class="t" style="fill:var(--a1)">North Star</text>
  <text x="340" y="62" text-anchor="middle" class="s">Incidents resolved with Beacon's help per week</text>
  <line x1="340" y1="78" x2="340" y2="104" class="ln"/>
  <line x1="92" y1="104" x2="588" y2="104" class="ln"/>
  <line x1="92" y1="104" x2="92" y2="122" class="ln"/>
  <line x1="257" y1="104" x2="257" y2="122" class="ln"/>
  <line x1="423" y1="104" x2="423" y2="122" class="ln"/>
  <line x1="588" y1="104" x2="588" y2="122" class="ln"/>
  <rect x="16" y="122" width="152" height="66" rx="8" class="box"/>
  <text x="92" y="146" text-anchor="middle" class="t">Breadth</text>
  <text x="92" y="166" text-anchor="middle" class="s">Environments with</text>
  <text x="92" y="180" text-anchor="middle" class="s">full connector coverage</text>
  <rect x="181" y="122" width="152" height="66" rx="8" class="box"/>
  <text x="257" y="146" text-anchor="middle" class="t">Depth</text>
  <text x="257" y="166" text-anchor="middle" class="s">Diagnosis</text>
  <text x="257" y="180" text-anchor="middle" class="s">acceptance rate</text>
  <rect x="347" y="122" width="152" height="66" rx="8" class="box"/>
  <text x="423" y="146" text-anchor="middle" class="t">Efficiency</text>
  <text x="423" y="166" text-anchor="middle" class="s">Alert-to-incident</text>
  <text x="423" y="180" text-anchor="middle" class="s">compression ratio</text>
  <rect x="512" y="122" width="152" height="66" rx="8" class="box"/>
  <text x="588" y="146" text-anchor="middle" class="t">Autonomy</text>
  <text x="588" y="166" text-anchor="middle" class="s">Autonomous resolution</text>
  <text x="588" y="180" text-anchor="middle" class="s">rate (allowlisted)</text>
  <line x1="92" y1="188" x2="92" y2="210" class="ln"/>
  <line x1="257" y1="188" x2="257" y2="210" class="ln"/>
  <line x1="423" y1="188" x2="423" y2="210" class="ln"/>
  <line x1="588" y1="188" x2="588" y2="210" class="ln"/>
  <rect x="16" y="210" width="152" height="54" rx="8" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="92" y="232" text-anchor="middle" class="s">Connectors team:</text>
  <text x="92" y="248" text-anchor="middle" class="s">setup time, coverage</text>
  <rect x="181" y="210" width="152" height="54" rx="8" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="257" y="232" text-anchor="middle" class="s">Diagnose team:</text>
  <text x="257" y="248" text-anchor="middle" class="s">eval pass rate, citations</text>
  <rect x="347" y="210" width="152" height="54" rx="8" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="423" y="232" text-anchor="middle" class="s">Correlate team:</text>
  <text x="423" y="248" text-anchor="middle" class="s">grouping precision</text>
  <rect x="512" y="210" width="152" height="54" rx="8" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="588" y="232" text-anchor="middle" class="s">Act team:</text>
  <text x="588" y="248" text-anchor="middle" class="s">allowlist adoption</text>
  <rect x="16" y="290" width="648" height="72" rx="10" fill="var(--a3)" fill-opacity=".12" stroke="var(--a3)" stroke-dasharray="5 4"/>
  <text x="340" y="314" text-anchor="middle" class="t" style="fill:var(--a3)">Guardrails (must not cross a threshold)</text>
  <text x="340" y="336" text-anchor="middle" class="s">Wrong-action rate · Inference cost per resolved incident · MTTR · Responder trust</text>
  <text x="340" y="352" text-anchor="middle" class="s">Each team's goal names the guardrail it could break</text>
</svg>
<figcaption>Beacon's North Star and input-metric tree. Each input has one owning team, and the guardrail band stops any team from moving its input by degrading quality, trust or cost.</figcaption>
</figure>

A metric tree is a causal hypothesis. You believe that raising diagnosis acceptance will raise incidents resolved with Beacon's help, so test it: when the input moved in the past, did the North Star follow? If an input rises for two quarters while the North Star stays flat, the link is broken and the input should go. Chapter 05 covers reading these relationships, and Chapter 19 covers asking a harness for them.

## Goals that steer the work

### Outcomes over output

Josh Seiden defines an outcome as a change in human behavior that drives business results. Drawing on the Kellogg Foundation's logic model, he separates three levels: **output** (what the team makes), **outcome** (the change in customer behavior the output produces) and **impact** (the business result at the top).

Each end has its own trap. Output goals ("launch diagnosis v2") are easy to hit and say nothing about whether anyone benefited. Impact goals ("grow ARR 38%") are what the business needs, but Seiden warns against handing them to small teams: no single team can move them, so the goal produces anxiety instead of direction. Outcomes sit in between, specific enough for a team to influence and close enough to value to matter.

Seiden's two questions turn any feature into an outcome: what will people be doing differently as a result, and how will you know? Jeff Gothelf and Seiden built a key-result pattern on the same idea in their 2024 book on customer-centric OKRs, whose title states it: *Who Does What By How Much?* A good key result names an actor, a behavior and a measurable change.

| Level | Example for an incident product | Who can move it |
|---|---|---|
| Output | Ship cited-evidence view in diagnosis | One team, by shipping |
| Outcome | On-call engineers accept the proposed root cause in more incidents | One team, by learning |
| Impact | Net revenue retention holds above target | The business, over quarters |

Ship dates still matter. They go in the delivery plan.

### OKRs: where they came from and how they work

Objectives and key results grew out of Peter Drucker's management by objectives. Andy Grove adapted the practice at Intel in the 1970s and described it in *High Output Management* (1983). John Doerr took Grove's course at Intel in 1975, introduced OKRs to Google in 1999 while at the venture firm Kleiner Perkins, and popularized them in *Measure What Matters* (2018).

Doerr defines an **objective** as what is to be achieved: significant, concrete, action-oriented and ideally inspirational. **Key results** measure progress toward it: specific, time-bound, aggressive yet realistic, and either met or not. A typical set has one objective and three to five key results. His sentence form doubles as a test: "I will [objective] as measured by [key results]." He credits OKRs with five benefits: focus, alignment, commitment, tracking and stretching.

Google's OKR playbook, reproduced on Doerr's site, adds the most useful distinction in OKR practice. **Committed** OKRs are ones the team agrees will be achieved; the expected score is 1.0, and a miss calls for a postmortem that the playbook says is not meant to punish. **Aspirational** OKRs describe how you'd like the world to look; the expected average is 0.7, with high variance, and they may carry across cycles. The playbook names the traps: failing to separate the two kinds, business-as-usual OKRs, timid aspirational OKRs, sandbagging, low-value objectives and committed objectives with too few key results to show they were met.

Christina Wodtke, in her 2014 essay "The Art of the OKR" and in *Radical Focus*, puts the weight on cadence. Objectives are qualitative, time-bound to a month or a quarter, and achievable by the team without depending on others. Key results are quantitative, usually three, set so the team's confidence of hitting each is about five in ten. Review that confidence weekly, and leave the OKRs alone until the period ends.

Marty Cagan supplies the counterweight. In 2020 he wrote that after years of advocating OKRs he had stopped recommending them in most companies he meets, because OKRs are an empowerment technique and fail where teams aren't empowered. In the same series he ties accountability to ambition: missing a moonshot is expected, while missing a conservative goal or a high-integrity commitment calls for a review with peers, much like an outage review. Read his position as "OKRs only work with empowered teams," not as a rejection of objectives.

One disagreement is worth knowing. Wodtke's 2014 essay endorses individual OKRs alongside company and team OKRs. Cagan argues against individual and functional objectives, and many organizations have dropped individual OKRs because they turn into task lists and get tangled with performance reviews. This book sides with team objectives, because the team is the unit that can change customer behavior.

### Why OKRs fail

Most OKR failures are predictable, and each has a known cause.

| Failure | What it looks like | Source of the diagnosis | Fix |
|---|---|---|---|
| Too many objectives | Seven objectives, twenty-five KRs | Doerr on focus | One to three objectives per team |
| Key results that are tasks | "Launch X," "Publish Y" | Seiden on outcomes | Rewrite as who does what by how much |
| OKRs beside a fixed feature roadmap | Features and dates are already decided | Cagan | Give teams problems, not features |
| Cascading by function or individual | Engineering, design and PM each have their own OKRs | Cagan | Team objectives for cross-functional teams |
| Set and forget | Written in week one, read in week thirteen | Wodtke, Cagan | Weekly confidence check-in |
| No stated ambition | Nobody knows if 0.6 is a failure | Google playbook | Label each OKR committed or aspirational |
| Sandbagged or impossible targets | Every KR hit, or none | Wodtke's five-in-ten confidence | Calibrate at set-up and record the assumption |
| No counter-metrics | KR hit by degrading something unmeasured | This book's synthesis | Attach a guardrail to each KR |

:::onramp If OKRs are new to you
Write one objective and three key results for your own team this quarter, then apply two tests. Does each key result describe something a customer does differently? Would you be surprised, but not shocked, to miss it? If either answer is no, rewrite it before anyone else sees it.
:::

:::leader For product leaders
The most valuable thing a leader does in an OKR system is decline to hand teams a feature list alongside the objectives. If the roadmap already says what to build and when, the OKRs are decoration. Give each team a problem tied to an input on the metric tree, agree on the ambition level, and review confidence weekly.
:::

## How to apply it

This method takes about four weeks for a product with a validated hypothesis and personas from Chapter 01. For an existing product with a stale vision, run it before the planning cycle so the goals land in time to shape the roadmap.

**Week 1: Vision.**

1. Gather the inputs: the revised product hypothesis, personas and job stories, the evidence log, current metrics, and the company's strategy and financial targets.
2. Draft three to five candidate vision statements with the product trio, then test them with a sales leader, a customer success leader and two or three customers. Discard any that names a technology or describes your ambition rather than a customer change. Score the rest against Pichler's six qualities and pick one.
3. Write the vision narrative: a press release dated two to three years out, plus an FAQ with every hard buying-group question in the internal section. Circulate it. The comments are the real output, because they show where leadership disagrees.
4. Fill in the vision board and write one positioning-style line per buying segment. If two segments name different alternatives, take that to the strategy work in Chapter 03.

**Week 2: Decompose.**

5. Map the customer's operational value stream in five to eight stages, from trigger to outcome. Mark where value is created and where it leaks.
6. Lay the product's capabilities, segments and revenue components against the value stream and the business model components. Note every place two teams own the same thing or nobody owns anything.
7. Map each team to a stage or capability. Platform and enabling teams get goals stated as service to the stream-aligned teams.

**Week 3: North Star and tree.**

8. Name the game and the customer's unit of value. Test two or three North Star candidates against Amplitude's three criteria.
9. Define the North Star precisely enough for a customer or auditor to recount it: what counts, what doesn't, over what period, from which data. If it might one day become a price meter, write it to that standard now.
10. Find three to five inputs using breadth, depth, frequency and efficiency. Ask the harness how each moved against the North Star over the last four to eight quarters. Drop inputs with no visible relationship, or label them untested bets.
11. Give each input one owning team and a guardrail with a threshold.

**Week 4: OKRs.**

12. Have each team draft one to three objectives tied to its input, with key results written as who does what by how much. Move every deliverable to the delivery plan.
13. Label each OKR committed or aspirational, record the team's starting confidence in each key result, and note each baseline's source.
14. Review the full set with leadership in one sitting. Look for collisions, gaps against the tree, business-as-usual goals and any key result that could be hit by breaking a guardrail.

**After launch.**

15. Check confidence weekly. Run a monthly goal review of inputs, guardrails and confidence trends. Change plans freely; change OKRs only at the end of the period.
16. Score every OKR at the end of the cycle. Hold a peer review, run like an outage review, for any committed OKR that was badly missed.

## The AI lens

### Goals for AI-powered products

A deterministic feature either works or it doesn't. An AI feature works some fraction of the time, at some cost per use, with a level of user trust that rises and falls with its mistakes. A goal set that tracks only adoption or value will reward a team for pushing an AI feature into situations it can't handle.

This book uses four goal families for AI products. The model is the book's own synthesis of the sources below.

| Family | Question | Example measures | Usual role |
|---|---|---|---|
| **Value** | Is the customer getting the outcome? | The North Star and its inputs | Objective |
| **Quality** | Is the output right, and how wrong is it when it's wrong? | Eval pass rate on a held-out set, task fidelity, share of severe errors | Guardrail, sometimes objective |
| **Trust** | Do people rely on it the right amount? | Acceptance rate, override rate, wrong-action rate, audit-log completeness | Guardrail, sometimes objective |
| **Cost** | Can we afford to deliver it at scale? | Inference cost per unit of value, gross margin | Guardrail |

Quality, trust and cost usually act as guardrails while the value goal is pushed. One of them becomes the objective when it's the binding constraint, such as after a trust incident or when margin falls below plan.

**Write quality goals the way evaluators do.** Anthropic's guidance on success criteria for model-based features asks that criteria be specific, measurable, achievable and relevant. Its worked example is deliberately multidimensional: an accuracy score, a rate of non-toxic outputs, a share of severe errors and a latency target, all on a held-out test set. "The model is good" is not a goal. A goal names the test set, the measure and the threshold. Chapter 31 covers the evaluation suite behind these numbers.

**Weigh errors by what they cost.** Google's People + AI Guidebook advises weighting false positives and false negatives by their real-world cost, and treating precision against recall as a tradeoff to set with real users. An incident agent that misses a root cause wastes a responder's time. One that confidently names the wrong one can send the responder to roll back the wrong service. Those errors deserve different thresholds. The guidebook also recommends explicit thresholds that trigger action, such as a rising rejection rate prompting a model review; write those triggers into the goal review.

**Decide what to automate before setting autonomy goals.** The guidebook distinguishes automation, suited to tedious, hard or risky tasks, from augmentation, suited to tasks people enjoy or feel responsible for. An autonomy goal is legitimate only for tasks customers want automated. Elsewhere, the goal is a better human decision, measured by acceptance and outcome.

**Make cost a first-class goal.** Inference cost scales with use, so the most successful AI feature can also be the most expensive. Stripe's 2025 framework for pricing AI products names three kinds of charge metric: **consumption** (per unit of usage, loosely tied to value), **workflow** (per completed task) and **outcome** (only when a defined result happens, closest to value and riskiest for the seller). When the price meter is an outcome, the North Star, the revenue metric and the customer's value become one number, and cost per outcome decides the margin. Intercom's Fin charges $0.99 per outcome and publishes what counts as one, for example a customer who asks for no further help after Fin's last answer. If your North Star may become a price meter, its definition has to be one a customer can audit. Chapter 15 covers pricing.

**Expect reviewers to read your trust goals.** Wrong-action rate, override rate and audit completeness are what a customer's security reviewer, and increasingly a regulator, will ask about. NIST's AI Risk Management Framework, released in January 2023 and extended with a Generative AI Profile in July 2024, organizes the work into four functions: govern, map, measure and manage. Your trust guardrails are evidence for "measure." Chapter 33 covers regulation.

### Doing the work with AI

With a harness connected to analytics, CRM, support and planning tools, most of this chapter's mechanics get faster. The judgment stays with you.

- **Vision drafts from evidence.** Give the harness the Chapter 01 interview snapshots and ask for candidate vision statements, each traced to supporting evidence, with any that name a technology flagged. Write the final one yourself.
- **Narrative drafts, then cuts.** A harness produces a plausible PR/FAQ in minutes, and a fluent narrative can hide that nobody has thought through the hard questions. Use the draft to find the questions, and own every claim in the version you circulate.
- **Testing the tree.** Ask how each candidate input moved against the North Star over past quarters, by segment, and where the relationship is weak or reversed. Teams used to skip this because it needed an analyst. Past co-movement is evidence, not proof of cause.
- **OKR critique.** Models are good at spotting outputs disguised as outcomes, missing baselines and gameable key results. Have one critique every draft before the leadership review.
- **The goal review.** The harness assembles inputs, guardrails, confidence trends and what changed. You interpret and decide.

Three rules keep this honest. Every number in a goal document traces to a source the harness actually read; otherwise it's a placeholder. Baselines come from data, never from the model. Customer data, financials and unreleased plans go only into tools your company has approved for them.

:::ai The one-line rule
Let the harness draft, test and assemble. Keep the choice of vision, North Star and ambition with the people who will be held accountable for them.
:::

## The Beacon case: from vision to quarterly goals

:::example Where Beacon starts
Your Chapter 01 discovery confirmed the problem (diagnosis consumes most of each incident, and burnout matters as much as MTTR) and split the solution: diagnosis first, supervised action gated on security controls. Leadership now wants Beacon's goals for the next two quarters, ahead of the Beacon Agents launch at Northlight Live. The current "vision" is a slide reading "the leading AI platform for IT operations." The current goals are a release list.
:::

**The vision.** The trio drafts five candidates. Two name agents and go. One describes Northlight's ambition rather than a customer change. The team settles on:

> Every on-call team can resolve incidents before customers feel them, without losing sleep or control.

It describes a change for Priya's team and for Dana at 3 a.m. "Without losing sleep" carries the burnout finding from discovery. "Without losing control" commits to the human approval gate, which matters to Sam and makes the vision ethical in Pichler's sense. It names no technology and would survive a change of strategy.

**The positioning line.** For the direct enterprise segment: for IT operations and SRE teams at large enterprises who are drowning in alerts and still diagnosing incidents by hand with runbooks and chat, Beacon is an incident agent platform that correlates alerts, diagnoses root cause with cited evidence and runs approved fixes; unlike AIOps features inside a single observability suite, Beacon works across the customer's tools through connectors and keeps a human approval gate on every risky action.

The "unlike" clause surfaces Beacon's strategic tension: cross-tool neutrality or deep integration with Northlight Observe data? One line can't credibly claim both. The team flags the choice for Chapter 03 and writes a second line for the MSP segment, where Leo's alternative is a patchwork of tools across 60 customers.

**The vision narrative.** The press release is dated at Northlight Live. Its headline is about Dana, paged at 3 a.m. and opening an incident that is already diagnosed, with cited evidence and a proposed rollback waiting for approval. The external FAQ answers Marcus (MTTR and escalations) and Leo (multi-tenant views and per-customer billing). The internal FAQ is longer and more useful. It covers Sam's questions (least-privilege access, audit logs, data residency, AI Act documentation for EU customers), the drop in gross margin from 81% to 72% after the agentic features launched, and what per-resolved-incident pricing would do to revenue predictability. The VP of Product's main comment: the internal FAQ should have been written first.

**Decomposition.** The customer's operational value stream runs detect, correlate, diagnose, decide, act and learn. Beacon's capabilities line up as Correlate, Diagnose, Act and Learn, with connectors feeding every stage, and the five engineering teams map one each to Connectors, Correlate, Diagnose, Act and Learn. The map exposes a gap: nobody owns "decide," where a responder chooses whether to accept the diagnosis. Diagnose and Act each assumed the other did. The trio gives it to Diagnose, because acceptance is a diagnosis outcome.

**North Star and tree.** The North Star is incidents resolved with Beacon's help per week, a productivity-game metric at the customer's unit of value. The team writes a definition precise enough to audit, because if per-resolved-incident pricing goes ahead, this definition becomes the price meter. The inputs are environments with full connector coverage (breadth), diagnosis acceptance rate (depth), alert-to-incident compression ratio (efficiency) and autonomous resolution rate on allowlisted actions (autonomy). Weekly active responders stays on the dashboard as a health metric, because it measures attention.

The guardrails are wrong-action rate, inference cost per resolved incident, MTTR (must not rise) and responder trust from a quarterly pulse. The wrong-action guardrail exists because of a real event: a customer rolled back the wrong service after Beacon proposed a hallucinated root cause. Without it, the Diagnose team could raise acceptance by sounding more confident.

When the harness compares past quarters, three inputs move with the North Star. Autonomous resolution has too little history to tell, so it stays on the tree labeled as an untested bet.

**The OKR draft that failed.** The Agents program's first draft read: ship Beacon Agents GA by Northlight Live; launch 12 new connectors; publish AI Act documentation. All three are outputs with deadlines, none names a customer behavior, and all three were on the delivery plan already. It's the pattern Cagan describes: OKRs layered on a roadmap that has already decided what to build.

**The OKR set.** The rewrite gives the Diagnose team one objective, three key results and a cost guardrail:

- *Objective:* On-call engineers trust Beacon's diagnosis enough to act on it.
- *KR1 (aspirational):* Diagnosis acceptance rate across enterprise customers rises from [baseline] to [target]. Confidence: five in ten.
- *KR2 (aspirational):* The share of responders who approve a Beacon-proposed action within ten minutes rises from [baseline] to [target].
- *KR3 (committed):* Wrong-root-cause reports stay below [threshold] per 1,000 diagnoses.
- *Guardrail (committed, shared with the Act team):* Inference cost per resolved incident stays below [threshold] and falls by [n]% over the quarter.

The Act team takes an aspirational objective on autonomous resolution for allowlisted, low-risk actions, scored against the 0.7 expectation. The quality and cost commitments are labeled committed, so a miss on either triggers a peer review.

**The goal review.** At the first monthly review, the harness reports that compression ratio rose for the second month running while incidents resolved with Beacon's help stayed flat in the MSP segment. Leo's customers had more grouped incidents but no more resolved ones, because few MSP environments had full connector coverage. The team leaves the OKRs alone and changes the plan: the Connectors team prioritizes the two integrations MSPs use most, and the breadth input gets a segment split next quarter.

## Product 360 artifacts

```template id="02-vision-statement" title="Product vision statement and board"
# Product vision · [Product] · v[n] · [Date]

**Owner:** [PM]   **Agreed with:** [names]   **Horizon:** [years]   **Next review:** [date]

## Vision statement
[One or two sentences: the positive change the product brings about, and for whom. No technology, feature or company ambition.]

## Quality check (pass / fail, with a note)
| Quality | Pass? | Note |
|---|---|---|
| Inspiring: people want to work toward it | | |
| Shared: built with and agreed by the team and key stakeholders | | |
| Ethical: benefits customers and does no harm | | |
| Concise: easy to remember and repeat | | |
| Ambitious: broad enough to guide several years | | |
| Enduring: survives a change of strategy | | |
| Names no technology, feature or mechanism | | |
| Describes a change for the customer, not for us | | |

## Vision board
| Target group | Needs | Product | Business goals |
|---|---|---|---|
| Users: | Problem solved: | What it is: | Revenue: |
| Economic buyer: | Benefit delivered: | 3 to 5 standout features: | Retention or expansion: |
| Gatekeepers: | | | Margin or cost: |
| Partners: | | | Strategic: |

## Extended board (optional)
| Competitors and alternatives | Revenue sources | Cost factors | Channels |
|---|---|---|---|
| | | | |

## Positioning line (one per buying segment)
For [target customer] who [need, or dissatisfaction with the current alternative], [product] is a [category] that [key benefit]. Unlike [main alternative, including manual processes], [product] [primary differentiation].

## Ideas this vision rules out
1.
2.
```

```template id="02-vision-narrative" title="Vision narrative (press release and FAQ)"
# Vision narrative · [Product] · [Date of the imagined announcement]

**Owner:** [PM]   **Status:** Draft / In review / Agreed   **Reviewers:** [names]

## Press release (under one page)
**Headline:** [The customer outcome, in a customer's words]
**Subheading:** [Who the customer is and the benefit they get]
**Summary:** [What is launching and why it matters, in two or three sentences]
**The problem:** [What the customer's day looks like today, and what it costs them]
**The solution:** [What changes for the daily user]
**What the economic buyer sees:** [The business result for the person who pays]
**Quote from our leader:** [Why we built it]
**Quote from a customer:** [Illustrative; mark as imagined]
**How to get started:** [The first step for a new customer]

## External FAQ (customers, partners, press)
1. Q: A:
2. Q: A:

## Internal FAQ (leadership, engineering, finance, legal)
1. What will it cost to build and to run per unit of value?
2. What are the hardest technical problems, and how confident are we?
3. What will security, procurement and legal reviewers ask, and what are our answers?
4. What does this do to revenue, margin and pricing?
5. What must be true about customers that we have not yet proven?
6. What are we choosing not to do?

## Open questions after review
| Question | Owner | Due |
|---|---|---|
| | | |

Rule: no claim in the narrative may rest on a number we have not sourced. Mark every imagined quote and every target as such.
```

```template id="02-business-decomposition" title="Business decomposition map"
# Business decomposition · [Product] · [Date]

## Customer's operational value stream
| Stage | [Stage 1] | [Stage 2] | [Stage 3] | [Stage 4] | [Stage 5] | [Stage 6] |
|---|---|---|---|---|---|---|
| What the customer does | | | | | | |
| Where value leaks today | | | | | | |
| Our capability that serves it | | | | | | |
| Owning team | | | | | | |
| Metric that shows progress | | | | | | |

## Capability × segment
| Capability | [Segment A] | [Segment B] | [Segment C] |
|---|---|---|---|
| | Owner / metric | | |

## Business model components each goal moves
| Component | Current state | Goals that move it | Owner |
|---|---|---|---|
| Customer segments | | | |
| Value propositions | | | |
| Channels | | | |
| Customer relationships | | | |
| Revenue streams | | | |
| Key resources | | | |
| Key activities | | | |
| Key partnerships | | | |
| Cost structure | | | |

## Team types
| Team | Type (stream-aligned / platform / enabling / complicated-subsystem) | Stream or service | Main interaction mode |
|---|---|---|---|
| | | | |

## Gaps and overlaps
- Stages or components nobody owns:
- Stages or components two teams both claim:
- Decision and owner for each:
```

```template id="02-north-star-tree" title="North Star and input-metric tree"
# North Star and metric tree · [Product] · [Date]

## Vision (one line)
[Vision statement]

## North Star
**Metric:** [name]
**Game:** Attention / Transaction / Productivity
**Definition:** what counts: [ ] · what does not count: [ ] · period: [ ] · data source: [ ]
**Could it become a price meter?** Yes / No. If yes, can a customer audit the count? [how]
**Checks:** reflects customer value [ ] · represents the current strategy [ ] · leads revenue [ ] · not a vanity or lagging financial metric [ ]
**Side measured (platforms):** [which side; how the other side appears below]

## Inputs (three to five)
| Input | Lens (breadth / depth / frequency / efficiency) | Definition | Baseline and source | Owning team | Evidence it drives the North Star |
|---|---|---|---|---|---|
| | | | | | Tested / Weak / Untested bet |

## Team drivers under each input
| Input | Driver | Team | Target this quarter |
|---|---|---|---|
| | | | |

## Guardrails
| Guardrail | Family (quality / trust / cost / health) | Threshold | Inputs it protects | Who watches it |
|---|---|---|---|---|
| | | | | |

## Health metrics (watched, not goals)
-

## Review
Last tested against history: [date]. Inputs to replace or re-test: [list].
```

```template id="02-okr-set" title="Team OKR set"
# OKRs · [Team] · [Quarter]

**Input on the metric tree this team owns:** [input]   **Guardrails this team could break:** [list]

## Objective 1: [Qualitative, inspiring, achievable by this team]
**Type:** Committed (expected 1.0) / Aspirational (expected about 0.7)

| # | Key result (who does what by how much) | Baseline and source | Target | Confidence at start (0 to 10) | Type |
|---|---|---|---|---|---|
| KR1 | | | | | |
| KR2 | | | | | |
| KR3 | | | | | |

**Guardrail for this objective:** [metric, threshold]
**Problem the team is solving (not a feature list):** [one paragraph]

## Objective 2 (optional)
...

## Tests before submitting
- [ ] Each KR names an actor and a behavior change, not a deliverable.
- [ ] Each KR has a baseline with a named source.
- [ ] Each OKR is labeled committed or aspirational.
- [ ] No KR can be hit by breaking a guardrail.
- [ ] Deliverables and dates are in the delivery plan, not here.
- [ ] The team can move every KR without waiting on another team.

## Moved to the delivery plan
- [Output] · [date]
```

```template id="02-ai-goal-set" title="AI feature goal set"
# AI goal set · [Feature] · [Quarter]

**Task automated or augmented:** [describe]   **Automate or augment?** [choice and reason]

| Family | Measure | Definition and test set | Baseline | Threshold or target | Role (objective / guardrail) | Action if breached |
|---|---|---|---|---|---|---|
| Value | | | | | | |
| Quality | | Held-out set: [name, size, last refreshed] | | | | |
| Quality: severe errors | | | | | | |
| Trust | Acceptance rate | | | | | |
| Trust | Override or rejection rate | | | | | |
| Trust | Wrong-action rate | | | | | |
| Cost | Inference cost per unit of value | | | | | |
| Cost | Gross margin contribution | | | | | |

## Error costs
| Error | Example | Cost to the customer | Weighting |
|---|---|---|---|
| False positive | | | |
| False negative | | | |

## Triggers
- If [measure] crosses [threshold] for [period], then [model review / rollback / pause autonomy / escalate].

## Evidence for reviewers
Where the security reviewer, auditor or regulator can find each trust measure: [location]
```

```template id="02-goal-review" title="Monthly goal review"
# Goal review · [Product] · [Month]

**Prepared by:** [PM]   **Data pulled from:** [sources and date]   **Attendees:** [names]

## North Star
| Metric | Last month | This month | Trend (3 months) | Comment |
|---|---|---|---|---|
| | | | | |

## Inputs
| Input | Owner | This month | Trend | Moved with the North Star? |
|---|---|---|---|---|
| | | | | Yes / No / Unclear |

## Guardrails
| Guardrail | Threshold | This month | Status (OK / Watch / Breached) | Action |
|---|---|---|---|---|
| | | | | |

## OKR confidence
| Team | KR | Confidence last month | Confidence now | Why it changed |
|---|---|---|---|---|
| | | | | |

## Broken links
Inputs that moved without moving the North Star, and our explanation:

## Decisions
| Decision | Owner | By when |
|---|---|---|
| | | |

## End of cycle only: committed OKRs missed
| OKR | Score | Peer review date | What we learned |
|---|---|---|---|
| | | | |

Rule: change plans freely; change OKRs only at the end of the period.
```

## Prompts

```prompt title="Draft vision statements from customer evidence"
Goal: Get candidate vision statements grounded in what customers said, not in what the company wants to be.
Paste in: interview snapshots or the evidence log, the personas and job stories, and the current vision if one exists. Use a tool approved for customer data.

You are helping me write the product vision for [product]. Using only the evidence provided:

1. Summarize, in five bullets, the change customers most want in their work, each with the snapshot IDs that support it.
2. Draft five candidate vision statements of one or two sentences. Each must describe a positive change for the customer's organization. None may name a technology, feature, mechanism or our company's market position.
3. Score each candidate against six qualities: inspiring, shared, ethical, concise, ambitious, enduring. Say which quality each one is weakest on.
4. For the strongest two, list three feature ideas each would rule out.
5. If the current vision names a technology or describes our ambition instead of a customer change, say so plainly.

[evidence]

Check the output: confirm each supporting snapshot ID actually says what the summary claims. Reject any candidate that would need rewriting if the strategy changed.
```

```prompt title="Write a vision narrative and stress its FAQ"
Goal: Produce a press release and FAQ that expose the hard questions behind the vision.
Paste in: the vision statement, personas (including the economic buyer and security reviewer), the product hypothesis and any known cost, pricing and risk facts. Confidential financials go only into an approved tool.

Write a vision narrative for [product] in the Working Backwards style, dated [date of the imagined announcement].

Part 1: a press release under one page, with a headline about the daily user's outcome, a subheading, the problem, the solution, what the economic buyer gets, how to get started and two quotes clearly marked as imagined.
Part 2: an external FAQ of five to eight questions customers, partners and press would ask.
Part 3: an internal FAQ of at least eight questions covering cost to build and run, technical risk, security and procurement objections, regulatory obligations, pricing and margin, and what we are choosing not to do. Answer only from the facts provided. Where a fact is missing, write "Unknown: [what we need to find out]."

Then list the three questions in the internal FAQ most likely to stop this vision from shipping.

[inputs]

Check the output: delete any number the model introduced that is not in your inputs. Read the internal FAQ first; if it is shorter or easier than the press release, it has not done its job.
```

```prompt title="Decompose the business and find ownership gaps"
Goal: Break the product and business into parts so every goal has one owner.
Paste in: a list of capabilities, segments, revenue components, teams and what each team works on today.

For [product], build a decomposition in four parts:

1. The customer's operational value stream from trigger to outcome, in five to eight stages. For each stage: what the customer does, where value leaks today and which of our capabilities serves it.
2. A capability by segment grid showing which team owns each cell.
3. The nine business model components (customer segments, value propositions, channels, customer relationships, revenue streams, key resources, key activities, key partnerships, cost structure), with the current goals that move each one.
4. Each team classified as stream-aligned, platform, enabling or complicated-subsystem, with its main interaction mode.

Then list every stage or component that nobody owns, every one two teams both claim, and a recommended owner for each with the reason.

[inputs]

Check the output: walk the value stream yourself with one real customer's recent experience. If a stage the customer went through is missing, add it before trusting the gaps list.
```

```prompt title="Choose a North Star and test its input tree"
Goal: Pick a North Star at the customer's unit of value and check whether the proposed inputs actually drive it.
Paste in (or connect the harness to): the vision, the decomposition, metric definitions and at least four quarters of history for the candidate North Star and inputs, by segment.

For [product]:

1. Name the game we play (attention, transaction or productivity) and the customer's unit of value.
2. Propose two or three North Star candidates. Test each against three criteria: reflects customer value, represents the current strategy, leads revenue. Reject vanity metrics and lagging financial metrics.
3. For the recommended North Star, write a definition precise enough for a customer to audit: what counts, what does not, period and data source.
4. Propose three to five inputs using breadth, depth, frequency and efficiency.
5. Using the history provided, show for each input how it moved relative to the North Star, overall and by segment. Classify each as "moves with the North Star," "weak or reversed" or "too little history." Do not claim causation from co-movement.
6. Propose one guardrail per input that would catch someone gaming it.

[definitions and data]

Check the output: pick one input and ask for the underlying quarter-by-quarter numbers and their source. If the harness cannot point to the source, treat the classification as unverified.
```

```prompt title="Rewrite output goals as outcome OKRs"
Goal: Turn a release list into OKRs that name behavior changes.
Paste in: the draft OKRs or goal list, the metric tree and the team's owned input.

Act as a demanding OKR coach reviewing these goals for [team].

1. Classify each objective and key result as output (something we ship), outcome (a change in what a named customer does) or impact (a business result).
2. Rewrite every output and impact key result as "who does what by how much," tied to the team's input on the metric tree. Leave the baseline and target as [placeholders] unless I supplied them.
3. Move every deliverable to a "delivery plan" list with its date.
4. Label each OKR committed or aspirational, and explain the choice.
5. For each key result, name the guardrail it could break and how a team might hit the number while making the product worse.
6. Flag any key result the team cannot move without another team's work.

[draft goals]
[metric tree]

Check the output: make sure no baseline or target appeared that you did not provide. Read each rewritten KR aloud with "as measured by" in front of it; if it sounds like a task, rewrite it again.
```

```prompt title="Set quality, trust and cost goals for an AI feature"
Goal: Define the guardrails that keep an AI feature's value goal honest.
Paste in: the feature description, the task it automates or augments, the value goal, current eval results, known failure cases and cost per unit of value. Use an approved tool for any customer incidents.

For the AI feature [feature], draft a goal set in four families: value, quality, trust and cost.

1. Say whether the task suits automation or augmentation, and why.
2. For quality: name the held-out test set needed, the measures (task fidelity, severe-error share and any others that fit) and a threshold for each. Mark thresholds as proposals.
3. For errors: describe a false positive and a false negative in this feature, their real cost to the customer, and which should be weighted more heavily.
4. For trust: propose acceptance, override and wrong-action measures, and how each will be logged so a customer's security reviewer can inspect it.
5. For cost: propose inference cost per unit of value as a guardrail, and say what happens to margin if usage doubles.
6. Write three triggers in the form "if [measure] crosses [threshold] for [period], then [action]."

[inputs]

Check the output: every threshold should be labeled as a proposal until the team has a baseline. Confirm the severe-error definition with someone who has handled a real customer incident.
```

```prompt title="Assemble the monthly goal review"
Goal: Produce the goal review in minutes so the meeting is spent on decisions.
Paste in (or connect the harness to): the metric tree, OKR set, guardrail thresholds, this month's and the last three months' values, and the teams' confidence ratings.

Prepare this month's goal review for [product]:

1. North Star: this month, last month and the three-month trend, with a one-line explanation from the data.
2. Inputs: each input's trend and whether it moved with the North Star this month.
3. Guardrails: status against threshold (OK, watch or breached), with the action already agreed for a breach.
4. OKR confidence: each key result's confidence now against last month, with the teams' stated reasons.
5. Broken links: any input that rose for two or more months while the North Star stayed flat or fell, overall or in any segment.
6. Three decisions the group should make, each with the evidence behind it.

Cite the source for every number. If a value is missing, say so; do not estimate it.

[tree, OKRs, data, confidence]

Check the output: spot-check two numbers against the source system. Make sure the proposed decisions change plans, not the OKRs themselves, unless the cycle has ended.
```

## Anti-patterns

:::warn The technology vision
"Be the leading agentic AI platform for IT operations." It names a mechanism and a market position, and it describes nothing a customer would notice. When the mechanism changes, so does the vision. Describe the customer's change instead.
:::

:::warn Revenue as the North Star
ARR or MRR is chosen as the North Star because it is what the board watches. It lags customer value by quarters and tells no team what to change. Revenue is the impact; the North Star is the customer behavior that produces it.
:::

:::warn Attention metrics in a productivity product
Daily active users or time in product become the headline metric for a tool people use to finish work. In a productivity product, more time can mean the product is failing. Count completed units of the customer's work.
:::

:::warn The release list dressed as OKRs
"Ship X by the event. Launch 12 connectors. Publish the docs." Every key result is a deliverable with a date. Move deliverables to the delivery plan and write key results as who does what by how much.
:::

:::warn The tree with no guardrails
A team hits its input by degrading something the tree does not show: acceptance by sounding more certain, automation by taking riskier actions, adoption by discounting. Put a guardrail beside every input, with a threshold and an owner.
:::

:::warn Set and forget
OKRs are written in week one and scored in week thirteen. Nobody knew in week four that confidence had collapsed. Check confidence weekly and review the tree monthly.
:::

## Checklist

- [ ] The vision statement describes a change for the customer, names no technology, and passes the six quality checks.
- [ ] A vision narrative exists, and its internal FAQ covers security, procurement, cost, pricing and regulatory questions.
- [ ] Each buying segment has a positioning-style line that names its real alternative.
- [ ] The customer's operational value stream is mapped, and every stage has one owning team.
- [ ] The North Star is at the customer's unit of value, passes the three criteria and has an auditable definition.
- [ ] Three to five inputs sit under the North Star, each with one owning team and evidence of how it moved with the North Star.
- [ ] Every input has a guardrail with a threshold.
- [ ] Every key result names who does what by how much, with a sourced baseline.
- [ ] Every OKR is labeled committed or aspirational, with a starting confidence.
- [ ] Deliverables and dates live in the delivery plan, not in the OKRs.
- [ ] For AI features, quality, trust and cost goals exist, with a named test set and triggers for action.
- [ ] A weekly confidence check and a monthly goal review are on the calendar, and missed committed OKRs get a peer review.

## Key takeaways

- Keep vision, strategy and goals as separate layers. The vision describes a lasting change for the customer; the strategy and goals change as evidence arrives.
- Write the vision three ways: a statement people remember, a board that connects it to target group, needs, product and business goals, and a narrative whose internal FAQ exposes what will make it hard.
- Decompose the business along the customer's value stream, capabilities, segments and business model components before setting goals, so each goal has exactly one owner.
- Choose a North Star at the customer's unit of value, put three to five owned inputs beneath it, and test the links against history. Add guardrails so no input can be moved by breaking something else.
- Write key results as changes in what named people do, label each OKR committed or aspirational, and check confidence weekly. OKRs work only when teams are given problems rather than feature lists.
- AI products need quality, trust and cost goals alongside value. When the price meter becomes an outcome, the North Star's definition has to be precise enough for a customer to audit.
