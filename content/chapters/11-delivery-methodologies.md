<p class="lead">A delivery method is a set of bets about where your risk lives: in what to build, in how long it takes, in the interruptions, or in the coordination between teams. This chapter shows you what each mainstream method optimizes, how to choose one per team rather than per company, how to prioritize with RICE without fooling yourself, and what changes when coding agents make building cheap and verification becomes the constraint.</p>

## Why this matters

Most PMs inherit their delivery method. The company "does Scrum" or "does SAFe," the tracker is already configured, and the ceremonies are on the calendar before you arrive. So the method gets treated as plumbing, something engineering owns and product tolerates.

That's a mistake, because the method decides what you learn and when. A platform team running Scrum while half its work is customer escalations will miss every Sprint Goal and slowly stop believing in goals at all. A product with five teams on one release train will spend more energy on coordination than on customers. Those are product problems that show up as missed outcomes.

The method also shapes how you answer the rest of the business. Sales wants dates, customer success wants a service level for escalations and finance wants a forecast. Each method gives you a different, and differently honest, way to answer.

And in 2026 the ground has moved. Coding agents write a growing share of the code, so building is cheaper and faster than it was even two years ago. Review, evaluation, security approval and customer adoption haven't sped up at the same rate. Methods designed around the cost of building now have to be tuned around the cost of verifying. To retune a method, you need to know which risk each of its parts was designed to control.

This is the Delivery dimension of your Product 360. Chapter 06 covers the execution mechanics underneath it (stories, story maps, releases); this chapter covers the operating system those mechanics run on.

## The methods and what each one optimizes

### Waterfall, and when it still fits

Waterfall is plan-driven, phase-gated delivery: requirements, design, build, test and deploy run in sequence, each closed by a sign-off. Scope is fixed early, and time and cost are estimated from it.

The usual citation is Winston Royce's 1970 paper on managing large software systems. As David Wheeler and others point out, Royce drew the sequential model and then described it as risky, arguing for iteration between phases. The industry is often said to have adopted the diagram and skipped the warning, though how much of waterfall's spread came from that misreading rather than from fixed-price procurement is debated.

Waterfall fails where you can't know the answer by analysis. Dave Snowden's Cynefin framework separates **ordered** domains, where cause and effect are known or discoverable by expert analysis, from **complex** domains, where you only understand the system by acting on it. A new AI feature whose behavior you can't predict until it meets real customer data is complex. So is any product whose main risk is whether customers value it. Planning harder doesn't reduce that risk; only contact with reality does.

But waterfall still fits some B2B work:

- **Ordered problems with a known target state**, such as a data-residency migration with a known schema and cutover plan.
- **Fixed external scope and dates you don't control**: a contractual deliverable, a certification audit, a regulatory documentation deadline.
- **Long lead times where late change is very expensive**: hardware, firmware, or a partner integration tied to the partner's release train.

Even then, build inside each gate in small, tested increments. "Plan-driven at the contract level, iterative inside" is the common enterprise pattern: the customer gets the fixed commitment, and the team still gets feedback every week or two.

### The Agile Manifesto

In February 2001, seventeen practitioners (among them Kent Beck, Alistair Cockburn, Martin Fowler, Ken Schwaber, Jeff Sutherland and Ron Jeffries) published the Manifesto for Agile Software Development. It states four values. Paraphrased:

- People and interactions over process and tools.
- Working software over exhaustive documentation.
- Customer collaboration over contract negotiation.
- Responding to change over following a plan.

The closing line is the part people forget: the items on the right still have value; the signatories value the items on the left more. The manifesto never argued against plans or contracts, only about which wins when they conflict.

For a B2B PM, the third value is the hardest. Enterprise sales runs on statements of work, roadmap commitments and renewal conditions. What you can do is shape them: commit to outcomes and dates with explicit uncertainty, rather than to feature lists. "By the end of Q2, EU customers can produce AI Act documentation for Beacon from within the product" is a commitment the team can deliver iteratively. "Feature X with fields A to F by June 3" isn't.

Martin Fowler's 2018 keynote named the **Agile Industrial Complex**: process imposed on teams from outside, producing what he called faux-agile. His remedies were for teams to choose their own process, to treat technical excellence as essential, and to organize around long-lived products rather than projects. This chapter takes the same stance. The method is the team's decision, bounded by what the organization genuinely needs (forecasts, compliance, coordination). Your job is to make those bounds explicit and keep them minimal.

### Scrum

The Scrum Guide by Ken Schwaber and Jeff Sutherland, last revised in November 2020, defines Scrum as a lightweight framework for generating value through adaptive solutions to complex problems. It rests on empiricism and lean thinking, and calls itself purposefully incomplete: it defines the frame and leaves practices to the team. The structure:

| Element | What the 2020 Guide specifies |
|---|---|
| **Accountabilities** | Product Owner, Scrum Master, Developers. One Scrum Team of typically 10 or fewer people, with no sub-teams or hierarchy. The 2020 revision replaced "roles" with "accountabilities." |
| **Events** | The Sprint (fixed length, one month or less, the container for everything else); Sprint Planning (up to 8 hours for a one-month Sprint); Daily Scrum (15 minutes); Sprint Review (up to 4 hours); Sprint Retrospective (up to 3 hours). Shorter Sprints get shorter events. |
| **Artifacts and commitments** | Product Backlog, committed to a Product Goal; Sprint Backlog, committed to a Sprint Goal; Increment, committed to a Definition of Done. |
| **Pillars and values** | Transparency, inspection and adaptation. Commitment, focus, openness, respect and courage. |

Several Scrum Teams on one product share one Product Goal, one Product Backlog and one Product Owner.

Scrum's strength is forced inspection: every Sprint ends with a working increment and a review, so a team can't drift for long unnoticed. Its weakness is the assumption that most work can be planned at the start of a Sprint. Teams with heavy interrupt load either reserve so much capacity that the Sprint Goal is meaningless or miss the goal every Sprint.

Two practices make Scrum work in B2B. First, write the Sprint Goal as an outcome or a learning goal, not a bundle of tickets: "Responders can see the deploy that most likely caused an incident, with evidence, for the three most common connectors." Second, use the **Sprint Review as your best customer-evidence forum**. Invite a design partner or a customer success manager, and show the increment against the Sprint Goal and the outcome metric. A ticket walkthrough for internal stakeholders wastes the one event designed for inspection.

In 2025, Sutherland, John Coleman and Ralph Jocham published the Scrum Guide Expansion Pack, optional guidance alongside the unchanged 2020 Guide. Its AI section asks teams to keep outcomes, quality and learning under control so that speed produces value rather than faster failure.

### Product Owner versus product manager

The Scrum Guide makes the Product Owner accountable for maximizing the value of the team's work, for developing and communicating the Product Goal, and for ordering the Product Backlog. The PO may delegate the work but keeps the accountability. In the Guide's words, "The Product Owner is one person, not a committee."

Product management is a broader job: that accountability plus discovery, strategy, pricing, go-to-market and stakeholder leadership. Marty Cagan argued in 2011 against splitting an outward-facing "product manager" from an inward-facing backlog "product owner." Nobody then owns the product, the two misunderstand each other, and good backlog decisions need deep customer knowledge.

Large B2B companies split the roles anyway, sometimes for good reasons: a platform team's backlog can be deeply technical, and a technical PO from engineering may order it better than a PM could. If you work in that structure, manage the risk Cagan named: a **proxy without customer contact**, ordering tickets on the PM's say-so with no first-hand evidence. The PO joins customer calls and design-partner sessions, owns outcome metrics rather than ticket throughput, and agrees decision rights with the PM in writing (the working agreement later in this chapter has a section for it).

### Kanban and flow

The Kanban Guide (Daniel Vacanti, John Coleman and contributors; current edition May 2025) defines Kanban as a strategy for optimizing the flow of value through a process. Its three practices are to define and visualize the workflow (in a Definition of Workflow that states what counts as started and finished, and the policies in between), to actively manage items (control WIP, prevent unnecessary aging, unblock), and to improve the workflow. It requires four **flow metrics**, and their exact definitions matter:

| Metric | Definition | What it tells you |
|---|---|---|
| **Work in progress (WIP)** | Items started but not finished | How much the team is juggling |
| **Throughput** | Items finished per unit of time | Delivery rate |
| **Work item age** | Time from start to now, for unfinished items | A leading indicator: what's stuck right now |
| **Cycle time** | Time from start to finish, for finished items | A lagging indicator: how long things take |

A **service level expectation (SLE)** is a forecast stated as a period and a probability: "85% of items finish in eight days or less." It comes from historical cycle time (a best guess at first) and, since the 2025 edition, lives in the Definition of Workflow. That edition also renamed "Kanban measures" as flow metrics and made WIP control less prescriptive.

Why WIP limits work comes from queuing theory. Little's Law, which John Little proved in 1961, says that, in a stable system, average cycle time equals average WIP divided by average throughput. Hold throughput steady, halve the work in progress, and average cycle time halves. Teams that start everything finish everything late.

Kanban fits teams whose demand is interrupt-driven: platform, integration and connector teams, security fixes and customer escalations. Your levers are WIP limits per state, **classes of service** (for example, an expedite lane for a P1 customer escalation that may break the WIP limit, used sparingly), and an SLE that sales and customer success can quote. "Connector bugs reported by a paying customer: 85% fixed within ten working days" is more useful to an account team than any roadmap slide.

### Shape Up

Ryan Singer's *Shape Up*, published by Basecamp with a foreword by Jason Fried, describes a method built around fixed time and variable scope:

- **Six-week cycles**, followed by a **two-week cool-down** for bugs, small fixes and planning the next cycle.
- **Appetite**: how much time the business wants to spend on a problem, decided before anyone designs a solution. An estimate starts from a design and asks how long; an appetite starts from a time budget and asks what design fits.
- **Shaping**: a small senior group works the problem until it's rough enough to leave room for the team, solved enough that the main elements are clear and bounded enough that everyone knows what's out. The result is a **pitch** with five ingredients: problem, appetite, solution, rabbit holes and no-gos.
- **The betting table**: during cool-down, stakeholders choose which pitches to bet the next cycle on. Singer calls the stance "bets, not backlogs": unchosen pitches aren't queued.
- **The circuit breaker**: a project that doesn't ship by the end of its cycle is cancelled by default, not extended. Teams are uninterrupted during the cycle and own their scope.
- **Hill charts**, which show work moving uphill (figuring it out) and then downhill (executing what's known).

Shape Up assumes a small company with few external commitments. Enterprise teams have to map cycles onto quarterly planning and reserve capacity for escalations. The most portable idea is **appetite**. Any team, in any method, can decide up front that a problem is worth two weeks or six, and then cut scope to fit. That's how you hold a fixed launch date without heroics.

### Dual-track agile

Desiree Sy described the pattern in 2007 for fitting UX work into agile teams. Marty Cagan popularized the name **dual-track agile** in 2012, and Jeff Patton wrote an explainer in 2017 (updated in 2023) that credits Sy and corrects common misreadings.

Two kinds of work run in parallel. **Discovery** is fast, cheap learning (hypotheses, time-boxed experiments, prototypes) ending in a decision to build, kill or keep learning. **Delivery** is predictable, releasable, high-quality software.

Patton's cautions are the useful part. It's two tracks, not two teams: the same people do both, with the product trio (PM, designer, tech lead) spending more of their week in discovery. Discovery isn't a phase before development. Good discovery kills many ideas; if everything that enters comes out the other side, it's validation theater.

Cagan later dropped the label for "continuous discovery and continuous delivery," because the name pushed people toward process diagrams. The practice is what matters: the backlog receives only items that passed a discovery test (Chapter 01 covers the discovery habits themselves).

### Scaled frameworks

Scaled frameworks solve a coordination problem: many teams working on one product or portfolio with dependencies between them.

**SAFe** (the Scaled Agile Framework) groups teams into Agile Release Trains that plan together in **Planning Intervals**, cadence-based timeboxes typically 8 to 12 weeks long, usually four or five iterations plus an Innovation and Planning iteration. SAFe prioritizes with **WSJF** (weighted shortest job first), which divides cost of delay by job duration, where cost of delay sums relative estimates of user and business value, time criticality, and risk reduction or opportunity enablement. SAFe credits the approach to Don Reinertsen's work on product development flow. In June 2026 Scaled Agile released **AI-Native SAFe** alongside Core SAFe, arguing that the bottleneck has moved from building software to verifying that what's built is safe, secure and valuable.

SAFe has strong critics, and their arguments are views, not settled fact. Fowler's Agile Industrial Complex critique applies directly, and Dave Snowden has criticized SAFe in sharp terms. A common PM complaint is that it pulls product managers into release coordination and front-loads planning into large events, which encourages bigger batches. Defenders respond that later versions address earlier critiques.

**LeSS** (Large-Scale Scrum) takes the opposite approach: one Product Owner, one Product Backlog, one common Sprint and one shippable increment for the whole product. Basic LeSS covers up to eight teams of about eight people; LeSS Huge extends the same structure to a few thousand. LeSS insists on cross-functional feature teams rather than single-specialty teams, and describes itself as deliberately simple.

Before you adopt either, ask whether the dependencies need coordinating at all. Many are artifacts of architecture and team boundaries. A stable API, a connector contract or a self-service platform capability can remove a dependency that a release train would otherwise plan around. Coordination frameworks earn their cost when dependencies are real and permanent, not when they're accidental.

### Choosing a method

Five questions get you most of the way:

1. **How much is known?** Ordered problems tolerate planning; complex ones need short feedback loops.
2. **Where is the main risk?** Cagan's four risks (value, usability, feasibility, viability, covered in Chapter 00) point to different methods. Value and usability risk need discovery and frequent review. Feasibility risk needs spikes and prototypes. Viability risk needs stakeholders in the loop.
3. **What's been promised externally?** Fixed dates, fixed scope, contractual deliverables and service levels.
4. **How interrupt-driven is demand?** When a large share of the team's work arrives unplanned, a Sprint plan keeps breaking.
5. **How many teams share the code, and how strong is the test and eval automation?** Coordination cost and verification cost both shape batch size.

The figure below places most teams; the methodology selection guide in the artifacts section adds the remaining cases, including fixed-date bets (appetite-bounded cycles), many teams on one product (remove dependencies, then scale) and agent-heavy teams with strong automation (continuous flow with a fixed review cadence).

Choose per team, not per company. A mature team migrating customers off a legacy engine and a new team building an AI agent face different risks; force them into one method and at least one runs the wrong one. Share the outcome layer instead: the North Star, the quarterly outcome goals, the review rhythm with leadership and what "done" means for customers.

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 380" role="img" aria-label="Method selection map: how much is known against how interrupt-driven demand is, with a default method in each quadrant">
  <rect x="90" y="20" width="270" height="140" rx="10" class="box"/>
  <rect x="370" y="20" width="270" height="140" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".6"/>
  <rect x="90" y="170" width="270" height="140" rx="10" class="box"/>
  <rect x="370" y="170" width="270" height="140" rx="10" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)" stroke-opacity=".6"/>
  <text x="108" y="48" class="t">Plan-driven, iterative inside</text>
  <text x="108" y="70" class="s">Known target state, fixed external</text>
  <text x="108" y="88" class="s">date and scope. Gates at the contract</text>
  <text x="108" y="106" class="s">level, small tested increments within.</text>
  <text x="388" y="48" class="t" style="fill:var(--a1)">Scrum or Shape Up + discovery</text>
  <text x="388" y="70" class="s">Value risk high. Sprint Goals or</text>
  <text x="388" y="88" class="s">appetite-bounded bets, a discovery</text>
  <text x="388" y="106" class="s">track, reviews with customers.</text>
  <text x="108" y="198" class="t">Kanban with WIP limits and an SLE</text>
  <text x="108" y="220" class="s">Many small, known items arriving</text>
  <text x="108" y="238" class="s">unplanned. Classes of service,</text>
  <text x="108" y="256" class="s">a quotable service level.</text>
  <text x="388" y="198" class="t" style="fill:var(--a2)">Kanban + a discovery track</text>
  <text x="388" y="220" class="s">Unplanned demand and unknowns.</text>
  <text x="388" y="238" class="s">Flow for delivery, a fixed weekly</text>
  <text x="388" y="256" class="s">slot for learning and review.</text>
  <line x1="90" y1="325" x2="640" y2="325" class="ln"/>
  <text x="365" y="345" text-anchor="middle" class="s">How much is known: ordered (left) to complex (right)</text>
  <text x="40" y="165" text-anchor="middle" class="s" transform="rotate(-90 40 165)">Demand: planned (top) to interrupt-driven (bottom)</text>
  <text x="365" y="370" text-anchor="middle" class="s" style="fill:var(--muted)">Across all quadrants: five or more teams on one product? Remove dependencies first, then scale.</text>
</svg>
<figcaption>A starting point for choosing a method per team. Two questions (how much is known, and how much demand arrives unplanned) place most teams. Fixed external dates, team count and the strength of test and eval automation then adjust the default.</figcaption>
</figure>

### RICE in depth

The method decides how often you re-prioritize; a scoring model decides how. Sean McBride introduced RICE on the Intercom blog in 2018 because teams favored pet ideas, clever ideas and new work, and underweighted effort. RICE forces four factors into the open. Chapter 03 compares it with the other prioritization frameworks; this section goes deeper on its scales and on how it fails in B2B.

| Factor | Intercom's definition and scale |
|---|---|
| **Reach** | How many people or events the initiative affects per time period, taken from real metrics where possible. Intercom's example: customers per quarter. |
| **Impact** | How much it moves the goal for each person reached: 3 massive, 2 high, 1 medium, 0.5 low, 0.25 minimal. |
| **Confidence** | How sure you are of the reach, impact and effort estimates: 100% high, 80% medium, 50% low. Below 50%, McBride calls it a moonshot. |
| **Effort** | Total person-months across product, design and engineering. Whole numbers, or 0.5 for well under a month. |

The score is reach times impact times confidence, divided by effort. McBride describes it as "total impact per time worked."

Intercom's own guidance is that RICE isn't a hard rule: challenge any result that looks wrong, and accept that dependencies and table-stakes work may justify doing a lower-scoring item first. Seven pitfalls show up repeatedly, and most are worse in B2B:

1. **Confidence by conviction.** Teams assign 80% because they feel sure. Itamar Gilad's Confidence Meter, built for a different scoring model, makes the fix concrete: opinions and self-conviction count for almost nothing, and confidence rises only with evidence such as research, data and launch results. Label the evidence behind every confidence score and cap confidence by label.
2. **Reach in the wrong unit.** A feature used by 40 people at your three largest accounts may matter more than one used by 4,000 at small accounts. Define reach as accounts or ARR touched per quarter, and use one unit across the sheet.
3. **Impact drift between scorers.** One PM's "massive" is another's "high." Calibrate with two or three reference items.
4. **Effort counts only the code.** Coding agents lower build effort. They don't lower review, evals, security review, migration, documentation or enablement. Estimate effort to "safely in production and adopted."
5. **False precision.** A score of 2,400 against 2,350 is noise. Group results into bands.
6. **No cost of delay.** RICE has no term for time, so a contractual deadline or a legacy system that costs more each month doesn't move the score. WSJF puts time criticality in the numerator; re-score the top of a RICE list with it.
7. **Mixed grain.** A two-day fix and a two-quarter platform investment don't belong on the same sheet. Score initiatives against initiatives.

Let the harness gather the evidence. Ask it, through connectors to product analytics and the CRM, how many accounts hit the relevant workflow last quarter and how much ARR they represent, then ask it to name the weakest assumption in each row.

### Delivery choices are pricing signals

The course this part of the book maps to also touches on how customer behavior models apply to pricing. In a delivery chapter the relevant point is narrow: what you ship, when, and in which package sends signals customers read as price. Shipping a capability as a free beta trains customers to expect it free. Releasing it first to the top tier signals premium value. Usage limits set during a pilot become the anchor for the commercial limits. Make those decisions deliberately with whoever owns packaging. Chapter 12 covers value offerings, and Chapter 15 covers pricing and packaging in depth.

## How to apply it

Here's a method for setting up, or resetting, the delivery system for a product with one or more teams. Plan on about a month for the first pass, then a quarterly review.

**Week 1: Diagnose the work.**

1. **Write the outcome layer first.** Confirm the North Star and the quarter's outcome goals. Every team's method has to serve these.
2. **Classify each team's work.** From the last two quarters of finished work, how much was planned and how much unplanned? How much was ordered and how much complex? Ask the harness for this breakdown from the tracker, with examples, and check a sample yourself.
3. **Name the main risk per team.** Value risk needs discovery and customer review; feasibility risk needs spikes and prototypes; interruptions need flow management.
4. **List external commitments**: fixed dates, fixed scope and published service levels. Note which are truly fixed and which are fixed because nobody has asked.

**Week 2: Choose and agree.**

5. **Choose a default method per team** with the selection guide, with one paragraph on why and what would make you change it.
6. **Write a team working agreement** with each team. The team writes it; you make sure the organization's real needs (forecasts, compliance, service levels) are in it.
7. **Set appetites for fixed-date work.** Decide what each commitment is worth and what scope can be cut, and write the circuit breaker in advance.

**Week 3: Instrument.**

8. **Set up flow reporting** for every team, whatever its method: WIP, throughput, work item age and cycle time, plus age in review and verification states.
9. **Publish an SLE** for each class of interrupt work, and give it to customer success and sales.

**Week 4: Prioritize and review.**

10. **Score the next quarter's initiatives with RICE**, with reach in accounts or ARR, evidence labels on confidence and full effort to production. Re-score the top items with cost of delay, and record every override with its reason.
11. **Run reviews as evidence forums** that end with the decisions needed.

**Every quarter:**

12. **Run the process health check** with each team, and pick at most two changes. Change the method only when the work has changed, not because a quarter went badly.

:::onramp If you're new to delivery methods
Don't start by changing the method. Start by measuring flow for a month: how many items are in progress, how old the oldest ones are and how long things take to finish. Most delivery problems become obvious once those four numbers are on a screen, and the fix is usually smaller than a new framework.
:::

## The AI lens

### Building AI-powered products

AI features change what "done" means. Chapter 31 covers building AI products in depth; for delivery, three changes matter.

- **Evals belong in the Definition of Done.** An AI feature is done when it meets its quality bar on an eval set that reflects real use, and that eval runs on every change. Ship without updated evals and nobody can safely change the feature next Sprint.
- **AI work is complex.** Model behavior on real customer data can't be fully known by analysis, which puts most AI feature work in Cynefin's complex domain. Expect more discovery and more scope cuts; appetites work better than estimates.
- **Cost per task is a delivery constraint.** Inference cost scales with use, so a feature can pass every functional test and still damage the margin. Put a cost-per-task check in the Definition of Done for features that call models.

### Doing the work with AI

The bigger change is in how software gets built. Coding agents now write, test and open pull requests for a meaningful share of changes. The evidence on what that does to productivity is mixed and moving:

- **The slowdown result.** In a July 2025 randomized trial, METR found that 16 experienced open-source developers, working on 246 real issues with early-2025 AI tools, took 19% longer with AI, while believing it had made them about 20% faster.
- **The update.** In February 2026, with late-2025 tools, METR's estimates moved to modest speedups (about 18% for returning developers and about 4% for new ones) with wide uncertainty. METR called this weak evidence, partly because developers increasingly refused to work without AI.
- **The amplifier finding.** DORA's 2025 research concluded that AI acts mainly as an amplifier of an organization's existing strengths and weaknesses. Its AI Capabilities Model, built from almost 5,000 survey responses and 78 interviews, names seven capabilities that decide whether AI helps, including working in small batches, strong version control and quality internal platforms.
- **The delegation picture.** Anthropic's 2026 Agentic Coding Trends Report, a vendor document best read as direction of travel, reports that developers use AI in about 60% of their work but fully delegate only 0 to 20% of tasks. It also reports that 27% of AI-assisted work would not otherwise have been done: more experiments, and more things nobody asked for.
- **The discipline.** Kent Beck's 2025 writing on "augmented coding" keeps the human accountable for code quality and tests, and treats an agent disabling tests as a warning sign. AI-Native SAFe makes the same point from the framework side: the bottleneck has moved to verification.

Read together, these point to six implications for your delivery system:

1. **Shrink batch size.** Agents make large changes cheap to produce and expensive to review. Keep changes small anyway, as DORA's small-batches capability says.
2. **Treat verification as the constraint.** Review, evals, security approval and customer adoption are where work now waits. Give them explicit states on the board, WIP limits and age tracking.
3. **Separate the build loop from the review loop.** A two-week Sprint may be too slow a loop for building and still right for customer review and retrospectives. Consider continuous flow for delivery with a fixed cadence for review, retro and planning.
4. **Stop relying on velocity.** When a three-day story takes three hours, story points lose meaning. Throughput of verified outcomes and cycle time are steadier measures.
5. **Spend the cheaper build on discovery.** Prototypes take hours, so discovery can test more ideas. The risk moves to building things nobody needs, so discovery has to kill more.
6. **Put agents in the working agreement.** Which code agents may change, who reviews what, and what agents may never do (disable tests, edit eval suites, touch approval gates).

<figure class="fig" markdown="0">
<svg viewBox="0 0 700 250" role="img" aria-label="Delivery flow with coding agents: build is fast, work queues at review, evals and security, adoption">
  <rect x="20" y="70" width="110" height="60" rx="10" class="box"/>
  <text x="75" y="98" text-anchor="middle" class="t">Discover</text><text x="75" y="116" text-anchor="middle" class="s">trio + customers</text>
  <rect x="150" y="70" width="110" height="60" rx="10" fill="var(--a2)" fill-opacity=".14" stroke="var(--a2)" stroke-opacity=".6"/>
  <text x="205" y="98" text-anchor="middle" class="t">Build</text><text x="205" y="116" text-anchor="middle" class="s">agent + engineer</text>
  <rect x="280" y="70" width="110" height="60" rx="10" fill="var(--a1)" fill-opacity=".14" stroke="var(--a1)" stroke-opacity=".7"/>
  <text x="335" y="98" text-anchor="middle" class="t">Review</text><text x="335" y="116" text-anchor="middle" class="s">human reviewers</text>
  <rect x="410" y="70" width="130" height="60" rx="10" fill="var(--a1)" fill-opacity=".14" stroke="var(--a1)" stroke-opacity=".7"/>
  <text x="475" y="98" text-anchor="middle" class="t">Evals + security</text><text x="475" y="116" text-anchor="middle" class="s">quality, cost, risk</text>
  <rect x="560" y="70" width="120" height="60" rx="10" class="box"/>
  <text x="620" y="98" text-anchor="middle" class="t">Release + adopt</text><text x="620" y="116" text-anchor="middle" class="s">customers use it</text>
  <line x1="130" y1="100" x2="150" y2="100" class="ln"/><line x1="260" y1="100" x2="280" y2="100" class="ln"/><line x1="390" y1="100" x2="410" y2="100" class="ln"/><line x1="540" y1="100" x2="560" y2="100" class="ln"/>
  <text x="205" y="160" text-anchor="middle" class="s" style="fill:var(--a2)">Faster and cheaper</text>
  <text x="405" y="160" text-anchor="middle" class="s" style="fill:var(--a1)">Where work now waits: WIP limits and age here</text>
  <line x1="280" y1="175" x2="540" y2="175" class="ln" style="stroke:var(--a1)"/>
  <text x="350" y="215" text-anchor="middle" class="s">Small batches keep review fast. Large agent-written changes queue here and skip scrutiny.</text>
  <text x="350" y="40" text-anchor="middle" class="t">With coding agents, the constraint moves downstream</text>
</svg>
<figcaption>When agents make building cheap, work piles up in review, evals and security approval. Make those states visible on the board, limit their WIP, and track their age as closely as you once tracked build progress.</figcaption>
</figure>

### Using the harness for delivery work

A harness with connectors to the tracker, source control, product analytics and the CRM does the mechanics that used to eat a PM's week. Ask it for the weekly flow report with the five oldest items named, for RICE reach evidence with a source for every number, for a draft review from the goal, merged work and customer notes, and for the weakest assumption in your RICE sheet. You read, ask why and add the judgment: what it means and what decision is needed.

:::ai The rule for agent-speed delivery
Let agents make building cheaper, and spend the savings on smaller batches, more discovery and faster verification. If the team ships more code but cycle time, escaped defects or customer adoption don't improve, you've added throughput to the wrong stage.
:::

## The Beacon case: one product, three methods

:::example Where Beacon starts
Beacon has about 35 engineers across five teams, all running two-week Scrum because Northlight standardized on it years ago. The Beacon Agents launch at Northlight Live is a fixed date. Customers on Beacon Classic need migrating before the legacy engine is sunset. Engineers have adopted coding agents, and pull request volume has jumped. After the hallucinated root-cause incident, where a customer rolled back the wrong service, leadership asks you, the new Principal PM, whether the delivery system is fit for agentic features.
:::

**The diagnosis.** The harness classifies two quarters of tracker data. Correlate's work is mostly planned and ordered: migration tickets with a known target state. Connectors and platform spends close to half its time on unplanned escalations and partner requests, and has missed most Sprint Goals. Diagnose and Act are doing complex AI work whose main risk is whether responders trust the agent. Learn, which feeds resolved incidents back into retrieval and evals, faces large unknowns.

**Five teams, three methods.** You propose a split, and the teams adjust it:

| Team | Method | Why | Key metric |
|---|---|---|---|
| Correlate | Kanban with an SLE for migration tickets | Ordered work, a known target state, steady flow | Migration cycle time; accounts still on Classic |
| Connectors and platform | Kanban with an expedite class for customer escalations | Interrupt-driven demand | SLE for escalations; work item age |
| Diagnose | Two-week Scrum with dual-track discovery; evals and cost per task in the Definition of Done | High value risk; regular demos with design partners | Diagnosis acceptance rate |
| Act | Two-week Scrum with dual-track discovery; security sign-off in the Definition of Done | High value and trust risk; approval gates | Approved actions per incident; autonomous resolution rate |
| Learn | Six-week bets with appetites and a two-week cool-down | Exploratory; big unknowns | Eval coverage of resolved incidents |

All five share the North Star (incidents resolved with Beacon's help per week), one quarterly outcome review and one monthly product review with customer success, so leadership compares the teams on outcomes and flow rather than on ceremonies.

**Fixed date, variable scope.** Northlight Live won't move. You set an appetite of two six-week cycles for supervised remediation, shaped as a pitch with explicit no-gos: no new runbook actions beyond restart, roll back and scale; autonomous execution only for low-risk actions the customer allowlists. The circuit breaker is written down before the first cycle starts: if autonomous rollback isn't proven safe on the eval set by the end of cycle two, it ships approval-gated only. Marcus gets a date to plan around, and Sam gets a scope to review.

**The RICE sheet.** For next quarter, you score five initiatives with reach in accounts per quarter (out of about 420 customers), confidence capped by evidence label and effort counted to production:

| Initiative | Reach (accounts/qtr) | Impact | Confidence (evidence) | Effort (person-months) | RICE |
|---|---|---|---|---|---|
| Diagnosis citation improvements | 260 | 2 | 100% (incident review, eval failures) | 3 | 173 |
| AI Act documentation pack | 70 (EU accounts) | 1 | 80% (customer requests) | 2 | 28 |
| Beacon Classic migration tooling | 90 (still on Classic) | 1 | 80% (support data) | 3 | 24 |
| Per-resolved-incident billing instrumentation | 40 (pricing pilot) | 2 | 50% (pilot not yet run) | 5 | 8 |
| Multi-tenant MSP view | 18 (MSP partners) | 3 | 50% (interviews) | 4 | 6.75 |

The review doesn't end with "build in score order." **Effort changed the order**: the engineers first estimated the citation fix at one person-month, counting only agent-written code, and adding eval updates, security review and customer communication tripled it. **The unit hid value**: Leo's MSP view scores lowest because 18 partners each run operations for dozens of end customers; in ARR touched it moves up, so you note an override. **RICE missed time**: the AI Act pack is table stakes for EU renewals, and Classic migration gets more expensive every month the legacy engine runs. Re-scored with WSJF, both rise above the billing instrumentation, and you record the overrides. The billing work stays in the plan because the pricing move depends on it (Chapters 12 and 15 cover that decision).

**Agents and batch size.** The flow report confirms what leadership suspected. Opened pull requests have risen sharply, but the oldest items on the Diagnose and Act boards all sit in "in review." The change behind the hallucinated root cause was one of them: a large, mostly agent-written change to retrieval logic, approved without the full eval suite. The teams add a WIP limit on "in review," a size guideline for agent-generated pull requests and an eval gate that blocks merging when diagnosis quality drops on the regression set. Their working agreement gains a clause: agents may open pull requests in Diagnose and Act code; any change touching the Act approval gate needs two human reviewers and Sam's security sign-off; agents may not change or disable eval suites.

**Cost in the Definition of Done.** Beacon's gross margin fell from 81% to 72% after agentic features launched, on inference cost. Diagnose features now carry an inference-cost-per-resolved-incident check, reviewed with the same weight as quality.

**The scaling debate.** Northlight leadership raises SAFe across Observe, Desk and Beacon. You argue for a LeSS-style single backlog and Product Goal for Beacon, connector and API contracts to cut dependencies between products, and a quarterly portfolio review for what remains. The VP of Product hasn't decided, and you've framed it as a choice about coordination cost rather than about frameworks.

:::leader For product leaders
Standardize the outcome layer across teams, not the method. Shared North Star, shared quarterly outcome reviews, shared flow metrics and a shared definition of customer-facing done let you compare and govern teams that run different methods. A single mandated method gives you matching dashboards, and at least one team running a method that doesn't fit its work.
:::

## Product 360 artifacts

```template id="11-methodology-selection-guide" title="Methodology selection guide"
# Methodology selection guide · [Product] · [Team] · [Date]

**Owner:** [PM]   **Agreed with:** [tech lead, designer, team]   **Review by:** [Date]

## 1. The work (last two quarters, from the tracker)
- Share of work planned vs unplanned: [x]% / [y]%
- Share of work ordered (known solution) vs complex (learning required): [x]% / [y]%
- Typical item size: [hours / days / weeks]
- Examples of each category: [three links]

## 2. The main risk (Chapter 00's four risks)
Value / Usability / Feasibility / Viability, with evidence:

## 3. External commitments
| Commitment | Type (date, scope, service level) | Truly fixed? | Owner | Date |
|---|---|---|---|---|
| | | | | |

## 4. Coordination
- Teams sharing this codebase or backlog:
- Dependencies that could be removed by an API, contract or platform capability:

## 5. Verification strength
- Automated tests: strong / partial / weak
- Evals for AI behavior: strong / partial / weak / not applicable
- Share of changes written mainly by coding agents:

## 6. Default method
| Situation | Default |
|---|---|
| Ordered, fixed external date and scope | Plan-driven, iterative build inside gates |
| Complex, value risk high | Scrum with dual-track discovery |
| Interrupt-driven, service commitments | Kanban with WIP limits and an SLE |
| Fixed date, flexible scope | Appetite-bounded cycles (Shape Up style) or Scrum with appetites |
| Five or more teams, real dependencies | Remove dependencies first; then LeSS, or SAFe for portfolio governance |
| Agent-heavy, strong CI and evals | Continuous flow with a fixed review, retro and planning cadence |

**Chosen method:** [method]
**Why (one paragraph):**
**What would make us change it:** [specific trigger, e.g. unplanned work above an agreed share for two months]
```

```template id="11-team-working-agreement" title="Team working agreement"
# Team working agreement · [Team] · v[n] · [Date]

**Method:** [Scrum / Kanban / cycles / hybrid]   **Signed off by:** [team members]   **Review date:** [Date]

## Cadence
- Planning or betting: [when, how long]
- Daily coordination: [when, 15 minutes]
- Review with customers or customer-facing staff: [when, who is invited]
- Retrospective: [when]

## Workflow and WIP limits
| State | Entry policy | WIP limit |
|---|---|---|
| Ready | | |
| In progress | | |
| In review | | |
| Evals and security | | |
| Ready to release | | |

## Definition of Done
- [ ] Tests pass, including tests not written solely by an agent
- [ ] Evals updated and passing (AI features)
- [ ] Cost per task within budget (features that call models)
- [ ] Security review complete where required
- [ ] Documentation and release note written
- [ ] Customer-facing teams told what changed

## Coding agents
- Agents may change: [code areas]
- Agents may not change: [eval suites, test configuration, approval gates, security controls]
- Human review required: [one reviewer by default; two for these areas]
- Size guideline for agent-generated changes: [e.g. reviewable in one sitting]
- An agent disabling or deleting a test is treated as a defect.

## Interrupt work
- How escalations enter: [channel, triage owner]
- Classes of service: Expedite (may exceed WIP; criteria) / Standard / Fixed date
- Service level expectation: [x]% of [item type] finish within [n] days

## Decision rights
| Decision | Decides | Consulted |
|---|---|---|
| What problem to solve next | PM | Team, design, tech lead |
| How to solve it | Team | PM, design |
| Scope cuts inside an appetite | Team with PM | Stakeholders informed |
| Release readiness | Tech lead | PM, security |

## Meeting norms
[Start and end times, async defaults, recording, decisions written down]
```

```template id="11-rice-scoring-sheet" title="RICE scoring sheet"
# RICE scoring sheet · [Product] · [Quarter] · [Date]

**Goal metric all items are scored against:** [one metric]
**Reach unit:** accounts / ARR / users / events per [quarter]   (use one unit for the whole sheet)
**Calibration items:** [two or three reference items with agreed scores]

| ID | Initiative | Reach (unit, period, source) | Impact (3 / 2 / 1 / 0.5 / 0.25, rationale) | Confidence (100 / 80 / 50%, evidence label) | Effort (person-months to production and adoption) | RICE | Cost-of-delay note | Override? (dependency, table stakes, commitment) | Decision |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

Score = (Reach × Impact × Confidence) ÷ Effort.

## Evidence labels and confidence caps
| Evidence | Maximum confidence |
|---|---|
| Opinion or conviction | 50% |
| Anecdotes, a few customer requests | 50% |
| Interviews across personas, or usage data | 80% |
| Test result, pilot or incident evidence | 100% |

## Effort includes
Build, review, evals, security review, migration, documentation, enablement, support readiness.

## Review questions
1. Which three rows have the weakest evidence?
2. Which items have a deadline or rising cost that RICE ignores?
3. Which items differ by less than the noise? Treat them as ties.
4. Is every item at the same grain (initiatives, not tickets)?
```

```template id="11-shaped-bet" title="Shaped bet with appetite"
# Shaped bet · [Name] · [Date]

**Shaped by:** [names]   **Cycle:** [dates]   **Team:** [team]

## Problem
[The specific customer problem, with evidence: incidents, interviews, data]

## Appetite
[Small batch: 1 to 2 weeks / Big batch: 6 weeks / other]. This is a budget, not an estimate.

## Solution (rough, solved, bounded)
[The main elements and how they fit, at the level of a sketch]

## Rabbit holes
[Known technical or design traps, and how we avoid them]

## No-gos
[What is explicitly out of scope]

## Circuit breaker
If not shippable by [date], we [ship this reduced scope / stop and re-pitch]. We do not extend by default.

## Outcome signal
[The metric and threshold that tells us this worked, and when we'll check]
```

```template id="11-cycle-review" title="Sprint or cycle review"
# Review · [Team] · [Sprint or cycle n] · [Date]

**Attendees:** [team, PM, customer success, design partner]

## Goal
Sprint Goal or bet: [text]
Met / Partly met / Not met, with one line why:

## What shipped
| Item | Linked to goal? | Released to | Evidence it works |
|---|---|---|---|
| | | | |

## Outcome metric
[Metric]: [value before] → [value now]. Too early to tell? Say when we'll know.

## Customer evidence
[Demo feedback, design-partner reactions, support signals, quotes with source]

## What we learned in discovery
- Ideas tested:
- Killed:
- Moving to delivery:

## Flow
- Throughput: [items finished]
- Cycle time, 85th percentile: [days]
- Oldest unfinished item and its state: [item, age]
- Age in review and verification: [days]

## Risks and decisions needed
| Decision | Owner | By when |
|---|---|---|
| | | |

## Next goal
[Draft Sprint Goal or next bet]
```

```template id="11-process-health-check" title="Process health check"
# Process health check · [Team] · [Quarter] · [Date]

Score each from 1 (poor) to 5 (strong) with evidence. Pick at most two to improve next quarter.

| # | Dimension | Score | Evidence |
|---|---|---|---|
| 1 | Goals are outcomes, not output | | |
| 2 | WIP stays within limits | | |
| 3 | Cycle time trend is stable or improving | | |
| 4 | Few items age past the SLE | | |
| 5 | Changes are small (batch size) | | |
| 6 | Review and verification wait time is short | | |
| 7 | Escaped defects and incidents are low | | |
| 8 | Discovery kills or reshapes ideas before build | | |
| 9 | PM and team have regular direct customer contact | | |
| 10 | Agent-generated changes have a low revert rate | | |
| 11 | The team reports a sustainable pace | | |
| 12 | Every ceremony produces a decision or a change | | |

## Two changes for next quarter
1. [Change], owner, how we'll know it worked:
2.

## Method still fits?
Has the work changed (share unplanned, complexity, commitments, team count)? Yes / No. If yes, rerun the selection guide.
```

## Prompts

```prompt title="Recommend a delivery method for a team"
Goal: Get a reasoned default method for one team, based on its actual work rather than habit.
Paste in (or connect the harness to): the team's tracker for the last two quarters, its current method, the product's outcome goals and a list of external commitments. Use an approved tool if the tracker contains customer names.

You are helping me choose a delivery method for [team] on [product].

1. From the tracker, estimate the share of work that was planned vs unplanned, and ordered (known solution) vs complex (learning required). Give three example items for each category with links.
2. Identify the main risk for this team: value, usability, feasibility or viability. Cite the evidence.
3. List the external commitments and mark which look truly fixed.
4. Recommend a default method from: plan-driven with iterative build inside gates; Scrum with dual-track discovery; Kanban with WIP limits and an SLE; appetite-bounded cycles; continuous flow with a fixed review cadence. Explain why in one paragraph.
5. State the specific trigger that should make us revisit the choice.

Don't recommend a scaled framework unless more than four teams share this backlog. Flag any number you estimated rather than counted.

Check the output: open five of the example items and confirm they're classified correctly. If the planned/unplanned split looks wrong, the recommendation is wrong too.
```

```prompt title="Draft a team working agreement"
Goal: Produce a first draft the team can edit, covering cadence, WIP, Definition of Done and agent use.
Paste in: the chosen method, the team's current workflow states, any existing Definition of Done, security and compliance requirements, and how escalations arrive today.

Draft a team working agreement for [team] running [method]. Include:
- Cadence for planning or betting, daily coordination, review (with who from outside the team attends) and retrospective.
- Workflow states with entry policies and a proposed WIP limit for each, including explicit "in review" and "evals and security" states.
- A Definition of Done that includes tests, evals and cost-per-task checks for AI features, security review where required, documentation and customer-facing communication.
- Rules for coding agents: what they may change, what they may never change (eval suites, test configuration, approval gates), required human reviewers and a size guideline for agent-generated changes.
- Classes of service for interrupt work and a starting SLE, labeled as a guess until we have data.
- A decision-rights table for PM, tech lead, designer and team.

Mark every item you invented rather than took from my inputs with [proposed].

Check the output: the team, not you, should own the final version. Bring the draft to a retrospective and expect half the [proposed] items to change.
```

```prompt title="Gather evidence for a RICE sheet"
Goal: Replace guessed reach and confidence with evidence from company systems.
Paste in (or connect the harness to): the list of candidate initiatives, product analytics, CRM and support ticket data. Use only tools approved for customer data.

For each initiative below, for the last full quarter:
1. Reach: how many accounts used the affected workflow, and how much ARR those accounts represent. Show the source and the definition you used.
2. Signal strength: how many support tickets, CRM notes or sales-call summaries mention the problem, with three examples each.
3. Evidence label: opinion, anecdote, interviews, usage data, or test/pilot/incident evidence, based only on what you found.

Present a table with one row per initiative. Don't assign impact or effort; I'll do that with the team. If you can't find data for a field, write "no data" rather than estimating.

[initiatives]

Check the output: spot-check two reach numbers against the source system yourself. Confirm the workflow definition matches what the initiative actually changes.
```

```prompt title="Challenge a RICE sheet"
Goal: Find the scores most likely to be wrong before the sheet drives a quarter's plan.
Paste in: the completed RICE sheet with rationales, the goal metric and any known deadlines or commitments.

Act as a skeptical product leader reviewing this RICE sheet for [product].

1. For each row, name the weakest assumption (reach, impact, confidence or effort) and what evidence would test it.
2. Flag any confidence score higher than its evidence supports.
3. Flag any effort estimate that seems to count only code, not review, evals, security, migration, documentation and enablement.
4. Identify items with a deadline or rising cost over time. Re-score the top eight with WSJF (cost of delay as user and business value + time criticality + risk reduction or opportunity enablement, divided by job duration), using relative estimates, and show where the order changes.
5. Identify items whose scores differ by less than the noise, and treat them as ties.
6. Check that all items are at the same grain.

Don't change any number I gave you; propose changes with reasons.

Check the output: the useful result is the list of disagreements, not a new ranking. Take the top three to the team and decide them together.
```

```prompt title="Prepare a Sprint or cycle review"
Goal: Turn tracker and metric data into a review that shows outcomes and asks for decisions.
Paste in (or connect the harness to): the Sprint Goal or bet, the items finished, the outcome metric before and after, customer feedback from the period, and flow data from the tracker.

Draft a review for [team], [Sprint or cycle], with these sections: goal and whether it was met; what shipped and whether each item links to the goal; outcome metric movement (say "too early to tell" if it is); customer evidence with sources; discovery results (tested, killed, moving to delivery); flow (throughput, 85th percentile cycle time, oldest unfinished item and its state, age in review and verification); risks and decisions needed with owners; and a draft next goal.

Keep it to one page. Don't describe items that don't link to the goal in more than one line. Quote customer feedback verbatim with source; never paraphrase inside quotation marks.

Check the output: the "decisions needed" section is the reason the review exists. If it's empty, ask yourself what you need from the room before you send it.
```

```prompt title="Diagnose flow and process health"
Goal: Find where work is waiting, and whether coding agents have moved the bottleneck.
Paste in (or connect the harness to): the tracker and source control history for the last two quarters, the team's working agreement and its WIP limits.

For [team], analyze delivery flow over the last two quarters:
1. WIP, throughput, cycle time (median and 85th percentile) and work item age, by month.
2. Time spent in each workflow state, especially review, evals and security approval. Which state holds the oldest items?
3. Size of changes over time, and the share written mainly by coding agents. Compare revert and escaped-defect rates for large vs small changes and for agent-heavy vs other changes.
4. How often WIP limits were exceeded, and by which classes of work.
5. Score the team from 1 to 5 on each dimension of the process health check below, citing evidence.

Separate what the data shows from your interpretation. Don't claim a cause the data can't support.

[process health check dimensions]

Check the output: walk the board with the team and confirm the oldest items are stuck where the analysis says. Pick at most two changes.
```

```prompt title="Shape a bet with an appetite"
Goal: Turn a fixed-date commitment into a bounded bet with scope that can be cut safely.
Paste in: the problem and its evidence, the fixed date, the team and any constraints from security, compliance or customers.

Help me shape a bet for [problem] that must ship by [date] with [team].

1. Propose an appetite (small batch of 1 to 2 weeks, or one or more six-week cycles) and explain why.
2. Describe the solution at sketch level: the main elements and how they connect, without detailed design.
3. List the rabbit holes most likely to blow the appetite, and how to avoid each.
4. List explicit no-gos.
5. Propose a circuit breaker: the reduced scope that ships if the full scope isn't ready, and the date we decide.
6. Name the outcome signal and when we'll check it.

Be ruthless about scope. Assume the date can't move.

Check the output: show the no-gos and the circuit breaker to the stakeholders who care about the date before the cycle starts. If they won't accept the reduced scope, the appetite is wrong, not the team.
```

## Anti-patterns

:::warn One method for every team
The company mandates one method everywhere. The interrupt-driven platform team misses every Sprint Goal; the exploratory team fills its backlog with fake certainty. Standardize the outcome layer and flow metrics, and let teams choose their method.
:::

:::warn The Product Owner as a ticket proxy
A Product Owner orders the backlog on the PM's instructions and never talks to a customer, so nobody with customer evidence makes backlog decisions. Either the PM holds the accountability, or the PO joins customer conversations and owns outcome metrics.
:::

:::warn Sprint Reviews as status meetings
The review walks through closed tickets for internal stakeholders. No customer is in the room and no decision is made. Show the goal, the outcome metric and customer evidence, and end with decisions.
:::

:::warn RICE as an oracle
The team builds in score order. Confidence reflects conviction, reach counts users for an enterprise product, effort counts only code and deadlines are invisible. Use RICE to structure the debate, label the evidence and record every override.
:::

:::warn Moving the date instead of the scope
A fixed launch date approaches and the team asks for two more weeks, then two more. Set an appetite and a circuit breaker before the work starts, so cutting scope is the plan rather than a failure.
:::

:::warn Big batches because agents can write them
Agents produce large changes in minutes, and reviewers wave them through because reading them would take hours. Keep batches small, limit WIP in review and verification, and treat an agent disabling a test as a defect.
:::

:::warn Scaling before simplifying
Cross-team dependencies lead straight to a scaled framework and a quarterly planning event. Remove what a stable API, connector contract or self-service platform capability can remove before you coordinate the rest.
:::

## Checklist

- [ ] The product's North Star and quarterly outcome goals are written down and shared by every team.
- [ ] Each team's work has been classified (planned vs unplanned, ordered vs complex) from real tracker data.
- [ ] Each team has a chosen method with a one-paragraph rationale and a trigger for revisiting it.
- [ ] Each team has a working agreement covering cadence, WIP limits, Definition of Done, agent use, interrupt handling and decision rights.
- [ ] The Definition of Done for AI features includes evals and a cost-per-task check.
- [ ] Every team reports WIP, throughput, work item age and cycle time, including age in review and verification states.
- [ ] Interrupt work has classes of service and a published SLE that customer-facing teams can quote.
- [ ] Every fixed-date commitment has an appetite, explicit no-gos and a circuit breaker agreed in advance.
- [ ] The RICE sheet uses one reach unit suited to B2B, evidence labels on confidence and full effort to production.
- [ ] Items with deadlines or rising costs have been re-scored with cost of delay, and every override is recorded with its reason.
- [ ] Sprint or cycle reviews include customer evidence and end with decisions.
- [ ] The discovery track kills or reshapes ideas before they reach the delivery backlog.
- [ ] A process health check runs every quarter, with at most two changes chosen.
- [ ] Before any scaled framework is adopted, dependencies that architecture could remove have been listed.

## Key takeaways

- Each delivery method is a bet about where the risk lives. Waterfall bets on analysis, Scrum on regular inspection, Kanban on flow, Shape Up on fixed time with variable scope and dual-track agile on learning before building.
- Choose the method per team based on how much is known, where the risk sits, what's been promised and how interrupt-driven the demand is. Share the outcome layer across teams, not the ceremonies.
- The Product Owner is an accountability inside Scrum; product management is the broader job. If the roles are split, keep customer evidence in the backlog decisions.
- RICE structures prioritization debates but breaks in predictable ways. In B2B, use accounts or ARR for reach, tie confidence to evidence, count effort to production and check deadline-driven items with cost of delay.
- Scaled frameworks solve coordination problems. Remove dependencies through architecture and contracts before you coordinate them.
- With coding agents, building gets cheaper and verification becomes the constraint. Shrink batch sizes, limit WIP in review and evals, track age in those states and put agent rules in the working agreement.
