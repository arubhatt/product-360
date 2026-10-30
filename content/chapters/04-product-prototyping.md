<p class="lead">A prototype is the cheapest thing you can build that answers a specific question about risk. In 2026 you can generate a convincing one in an afternoon, which makes it easier than ever to learn fast and easier than ever to mistake a demo for a product. This chapter covers how to choose what to prototype, test it with real people, staff the team that will build the real thing, and write the PRD that records what you decided.</p>

## Why this matters

Chapter 01 left you with a hypothesis and a map of its assumptions. Conversation can test some of them. Solution assumptions usually need more, because people predict their own behavior badly: you have to put something in front of them and watch.

That's the job of a prototype. Marty Cagan frames the distinction as **building to learn** versus **building to earn**. Discovery builds to learn: the output is evidence about whether a solution is worth building. Delivery builds to earn: the output is a product that customers rely on at scale. Cagan's argument, repeated across his writing from 2025 into 2026, is that most products fail because teams never discovered a solution worth building, not because they couldn't build. Faster building doesn't fix that.

AI makes the distinction sharper. A product manager with a prompt-to-app builder can produce a clickable, data-backed, deployed prototype before lunch. That speeds up discovery, and it also creates a trap: a polished prototype looks finished, and enterprise products are mostly made of things a prototype never shows: permissions, audit logs, reliability, integrations, data residency, migration and support.

The chapter follows the work in order: decide what to prototype, build it, test it so the result changes a decision, staff the team and write the PRD. These artifacts sit in the Build dimension of your Product 360 (Chapter 00).

## Prototypes: what they're for

### The four risks, one question at a time

Cagan names four risks that any product idea has to retire: **value** (will customers buy or choose it?), **usability** (can they figure out how to use it?), **feasibility** (can we build it with the time, skills and technology we have?) and **viability** (does it work for the rest of the business: sales, legal, finance, security?). Chapter 01's adoptability lens maps mostly onto viability here: the security reviewer, procurement and the partner channel each have to say yes.

A prototype should target one risk, two at most. Write the risk question at the top before anyone builds anything:

> We are testing whether **[persona]** will **[observable behavior]** when **[situation]**, using **[prototype]**. This prototype deliberately ignores **[what it doesn't cover]**.

The last clause does more work than it looks. An approval-screen prototype ignores multi-tenancy, permissions, audit logging and scale. Saying so stops stakeholders treating it as a commitment and lists what the PRD must cover later.

Prototypes also communicate a solution better than a written spec, but Cagan treats that as secondary: teams that use the prototype mainly to communicate, and skip testing it, build products that fail.

:::key One prototype, one question
Every prototype starts with a written risk question and a list of what it ignores. If you can't say which of value, usability, feasibility or viability it tests, you're building a demo.
:::

### Cagan's prototype types

In a 2014 SVPG essay, "Flavors of Prototypes," Cagan describes four families, with the user prototype split by fidelity. Different people build each one to answer a different question.

| Type | What it is | Built by | Answers | Afterward |
|---|---|---|---|---|
| **Feasibility prototype** | Just enough code to retire a technical risk: a new technology, an algorithm, a performance question. May have no interface. | Engineers | Can we build it? | May be thrown away or built on |
| **Low-fidelity user prototype** | Interactive wireframes. Information and workflow, not visual design or real data. | Interaction designers | Does the flow make sense? | A simulation; no code to keep |
| **High-fidelity user prototype** | A realistic-looking simulation with realistic (not live) data. | Designers | Can users use it, and why don't they like it? | A simulation; informs the spec |
| **Live-data prototype** | Connects to real data and takes real traffic in quantity (A/B, opt-in or invite-only). Only the critical use cases. | Developers | Does this approach beat what we have, on real metrics? | Engineers still have to productize it |
| **Hybrid prototype** | Combines aspects of the others. Cagan's example: live data, no live traffic, so the team can watch users judge relevance. | Depends on the mix | Are the results relevant? | Used to learn, not to prove |

Carry two of Cagan's points into every review. A high-fidelity user prototype can't prove a product will sell; his favorite use is learning *why* users don't like a design. And even a successful live-data prototype skips what makes software a product: full use cases, test automation, localization, scalability. He's blunt about it: "this is not a product."

B2B and AI teams should use the hybrid type more than they do. Running a diagnosis agent on real past incidents, with no live traffic and no actions executed, tells you whether the output is good enough to be worth testing with users, at a fraction of the cost and risk of a live pilot.

## The fidelity ladder

### Fidelity is three dials

NN/g's Kara Pernice defines fidelity as how closely a prototype resembles the final product, along three independent dimensions: **interactivity**, **visuals** and **content**. A prototype can be high on one and low on another. A grey wireframe can carry real incident data; a pixel-perfect mockup can be full of placeholder text.

Low fidelity is fast to change, and users criticize it more freely. High fidelity tests realistic timing and detailed workflows, but it's slower to build and invites attachment.

For expert B2B users, this book's rule of thumb is to turn up the **content** dial first. An SRE notices fake logs instantly and stops believing the session. A plain wireframe with realistic incidents, plausible service names and coherent timelines teaches you more than a beautiful screen showing "Lorem ipsum error 404."

AI builders collapse the cost of visual and interactive fidelity, so teams reach for polish by default, and the attachment risk rises: the result looks finished, and stakeholders ask when it ships.

### The rungs

The fidelity ladder is this book's synthesis of Cagan's types, Pernice's dimensions and two service-simulation methods. The **interface track** makes the front end more real. The **service track** makes the work behind it more real, while the front end can stay simple.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 330" role="img" aria-label="The fidelity ladder: an interface track from sketch to coded prototype, a service track from concierge to live-data prototype, and the boundary where prototypes end and products begin">
  <text x="20" y="22" class="t">Interface track: how real it looks and behaves</text>
  <rect x="20" y="34" width="118" height="72" rx="10" class="box"/>
  <text x="79" y="62" text-anchor="middle" class="t">Sketch</text>
  <text x="79" y="82" text-anchor="middle" class="s">minutes</text>
  <rect x="148" y="34" width="118" height="72" rx="10" class="box"/>
  <text x="207" y="62" text-anchor="middle" class="t">Wireframe</text>
  <text x="207" y="82" text-anchor="middle" class="s">hours</text>
  <rect x="276" y="34" width="118" height="72" rx="10" class="box"/>
  <text x="335" y="62" text-anchor="middle" class="t">Clickable</text>
  <text x="335" y="82" text-anchor="middle" class="s">user prototype</text>
  <rect x="404" y="34" width="118" height="72" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)"/>
  <text x="463" y="62" text-anchor="middle" class="t" style="fill:var(--a1)">Coded</text>
  <text x="463" y="82" text-anchor="middle" class="s">AI-built or hand-built</text>
  <text x="20" y="146" class="t">Service track: how real the work behind it is</text>
  <rect x="20" y="158" width="118" height="72" rx="10" class="box"/>
  <text x="79" y="186" text-anchor="middle" class="t">Concierge</text>
  <text x="79" y="206" text-anchor="middle" class="s">human, visible</text>
  <rect x="148" y="158" width="118" height="72" rx="10" class="box"/>
  <text x="207" y="186" text-anchor="middle" class="t">Wizard of Oz</text>
  <text x="207" y="206" text-anchor="middle" class="s">human, hidden</text>
  <rect x="276" y="158" width="118" height="72" rx="10" class="box"/>
  <text x="335" y="186" text-anchor="middle" class="t">Hybrid</text>
  <text x="335" y="206" text-anchor="middle" class="s">live data, no traffic</text>
  <rect x="404" y="158" width="118" height="72" rx="10" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)"/>
  <text x="463" y="186" text-anchor="middle" class="t" style="fill:var(--a2)">Live-data</text>
  <text x="463" y="206" text-anchor="middle" class="s">real data and traffic</text>
  <line x1="540" y1="28" x2="540" y2="240" class="ln" stroke-dasharray="5 5"/>
  <rect x="552" y="34" width="78" height="196" rx="10" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="591" y="118" text-anchor="middle" class="t">Product</text>
  <text x="591" y="138" text-anchor="middle" class="s">build to</text>
  <text x="591" y="154" text-anchor="middle" class="s">earn</text>
  <line x1="20" y1="268" x2="522" y2="268" class="ln"/>
  <path d="M522 263 L532 268 L522 273 Z" fill="var(--muted)"/>
  <text x="20" y="290" class="s">Cost, time to build and attachment rise to the right.</text>
  <text x="20" y="310" class="s">Choose the lowest rung that answers the risk question.</text>
  <text x="552" y="262" class="s">Reliability, security,</text>
  <text x="552" y="278" class="s">scale, compliance</text>
</svg>
<figcaption>The fidelity ladder. Prototypes live left of the dashed line. Crossing it means meeting run-time demands that no prototype was built for, whatever tool produced it.</figcaption>
</figure>

- **Sketch.** Pen, whiteboard or a quick drawing in a chat window. Good for exploring several directions with the trio in an hour.
- **Wireframe.** Layout and content without visual design. Tests information architecture: does the user find the evidence, the approval button, the rollback scope?
- **Clickable.** A user prototype that responds along the main paths. The workhorse of usability testing.
- **Coded.** Runs as software, built by hand or by an AI builder. Handles interactions (typing, filtering, live charts) that clickable prototypes fake badly. Still a simulation unless it's connected to real data and traffic.
- **Concierge.** A human delivers the service openly, by hand, to a few customers. The canonical example is Food on the Table, a meal-planning startup that served its first customer face to face before automating anything. Its founder, Manuel Rosso, argued that if a personal, high-touch service can't win adoption, a web page won't. Eric Ries tells the story in *The Lean Startup* as the concierge MVP.
- **Wizard of Oz.** The participant uses an interface that appears automated, but a hidden human (the "wizard") produces some or all of the responses. NN/g's Sara Paul and Maria Rosala trace the method to Don Norman and Allen Munro in 1973 and the name to Jeff Kelley's 1983 dissertation on natural-language interfaces. They recommend it for conversational interfaces, recommendations and generative AI features, where it tests desirability before you invest in building. Participants sometimes guess a human is involved, and anyone deceived must be debriefed afterward.
- **Hybrid and live-data.** The top of the service track, where engineers own the build.

What separates concierge from Wizard of Oz is what the customer knows. In a concierge test, the customer knows a person is doing the work, so you learn whether the outcome is valuable. In a Wizard of Oz test, the customer believes it's automated, so you learn about the experience and value of the future automated product.

:::onramp If you've only used design-tool prototypes
Start one rung lower than you think. Most early questions ("will they find it?", "do they understand what the agent did?") can be answered with a wireframe full of realistic content. Move up only when a lower rung can't answer the question.
:::

## Prototyping with AI in 2026

### The tool categories

Tools shift every few months, so this book teaches categories. Colin Matthews, writing in Lenny's Newsletter in January 2025, sorted AI prototyping tools into chatbots that produce one-off prototypes, cloud development environments that build hosted multi-page apps, and local developer assistants that work inside a real codebase. Design-to-code tools arrived as a fourth category through 2025 and 2026.

| Category | What it does | Typical use | Who owns it |
|---|---|---|---|
| **Chat-and-artifact** | Your AI harness generates a working page or small app inside the conversation and can share a link. | Single-screen concepts, test stimuli | PM or designer |
| **Prompt-to-app builders** ("vibe-coding" builders) | Hosted builders that turn a description into a multi-page app with a database and a URL. Cagan names Lovable and Bolt; Matthews also lists Replit and v0. | Clickable or coded user prototypes with realistic data | PM or designer, with engineering review before any real data |
| **Design-to-code** | Start from a design or design system and produce a coded prototype. Figma launched Figma Make in May 2025; Anthropic released Claude Design as a research preview in April 2026, with a handoff bundle for Claude Code. | High-fidelity user prototypes that match the product | Designer, with PM |
| **Coding agents in the real codebase** | Agents working in the product's repository. Matthews lists Copilot and Cursor among others; Cagan cites Claude Code and Cursor as professional build tools. | Feasibility and live-data prototypes; production work | Engineers |

The term **vibe coding** comes from Andrej Karpathy, who in February 2025 described building software by giving in to the AI and not reading the generated code. Collins named it its Word of the Year for 2025. This book uses the narrow meaning, building without reading the code, which is acceptable for a throwaway prototype and unacceptable for a product.

One rule ties the categories together: **the closer a prototype gets to production data and real customers, the more engineering ownership it needs.**

### Cagan's warnings about prototypes and products

Cagan's 2025 essay "Prototypes vs Products" lists the run-time demands that separate the two: reliability; telemetry and observability; performance at scale; multiple languages and currencies; integrations; zero-downtime maintenance and fault tolerance; and data security, compliance and disaster recovery. A prototype covers a handful of use cases and simple rules; an enterprise product may involve thousands of use cases and complex business policy. He puts the priority plainly: "reliability is our most important feature."

His warnings, for any team using AI builders:

- **Prototyping tools and build tools serve different purposes.** The gen-AI prototyping tools are generally not for building actual products, and don't need to be. Production quality almost always takes different tools and skills.
- **PMs underestimate the gap**, especially PMs without engineering backgrounds, and vendors overstate how automatically a prototype becomes a product.
- **Self-deception is the newer risk.** Cagan sees product people themselves now confusing the two.

He allows one exception: internal tools and customer-enabling tools carry lower operational demands, so their path to product quality is shorter.

Security makes the gap concrete. In 2025, a critical vulnerability (CVE-2025-48757) was published describing insufficient row-level security in sites generated by one prompt-to-app builder, letting unauthenticated users read or write data. The vendor disputed it, saying customers are responsible for protecting their application data. Whoever is right about responsibility, the PM's lesson holds: a vibe-coded prototype must never hold real customer data or be exposed publicly without engineering review.

In July 2026, Cagan added what he called the AI productivity paradox: teams that use AI to produce the old artifacts faster (business cases, roadmaps, requirements documents, code) don't get better outcomes. Strong teams use AI to prototype and test in discovery, then build properly in delivery.

## Usability testing that changes decisions

### The method in brief

NN/g's Kate Moran describes usability testing as three elements: a **facilitator**, a set of **tasks** and a **participant**, who usually thinks aloud. Tests are **qualitative** (find problems and understand why) or **quantitative** (measure task success or time against a benchmark). They run in person or remotely, and remote tests are **moderated** (live, over screen share) or **unmoderated** (a tool delivers written tasks).

For enterprise users, moderated remote is the practical default: they're scarce, busy and often behind firewalls, and their workflows are complex enough that unmoderated sessions tend to stall on the first unfamiliar step.

### How many users

Jakob Nielsen's 2000 essay "Why You Only Need to Test with 5 Users" rests on a model he built with Thomas Landauer. Across Nielsen's projects, a single user revealed about 31% of the problems on average, and five users found about 85%. His recommendation is many small studies: with budget for 15 users, run three rounds of five and redesign between rounds. He calls elaborate usability tests a waste of resources.

The caveat matters in B2B: the model assumes comparable users. With distinct user groups, Nielsen suggests three to four users per group for two groups, and three per group for three or more. A 2012 update separated study types: about five users for qualitative tests, at least 20 for quantitative ones. So "five users" means a small panel per distinct role per round. An enterprise product with an on-call engineer, an SRE lead and a security reviewer needs one for each.

Steve Krug's *Rocket Surgery Made Easy* offers a complementary cadence for teams without researchers: three participants, one morning a month, a same-day debrief where each observer names the most serious problems they saw, then the smallest change that fixes the worst ones. Nielsen's five is a sample size per round; Krug's three-a-month is a rhythm. Both favor small, frequent tests over large, rare ones.

### Thinking aloud

Nielsen calls thinking aloud perhaps the single most valuable usability method. Participants use the system while saying what they're thinking. It's cheap, works on anything from paper to shipped software, and persuades, because executives who watch a session see the problem for themselves.

It's also unnatural, participants filter their thoughts to sound smart, and facilitator prompts change behavior. So the facilitator gives representative tasks and stays quiet: prompt only on silence, never lead, and note every intervention so you can discount what follows it.

### Writing tasks

Marieke McCloskey's three rules for task scenarios, published by NN/g, separate a test from a guided tour:

1. **Make the task realistic.** Give the context a real user would have.
2. **Make it actionable.** Ask them to do it, not to describe how they would.
3. **Avoid clues.** Don't name buttons, tabs or menu labels, and don't give steps.

Weak: "Click the Diagnose tab and read the root cause." Strong: "You were paged for checkout latency at 03:10. Find out what most likely caused it, and decide what to do next."

### From results to decisions

A test changes a decision only if someone agreed, before the sessions, what result would change it. This book's practice is to **pre-register signals** in the test plan: a proceed signal ("at least four of five on-call engineers correctly approve or reject the proposed action"), an iterate signal and a kill signal ("any participant approves a rollback that the evidence on screen contradicts"). Results then map onto a decision instead of starting a debate.

Nielsen's severity scale gives the readout a shared language. Severity combines frequency, impact and persistence, with market impact judged separately:

| Rating | Meaning | Action |
|---|---|---|
| 0 | Not a usability problem | None |
| 1 | Cosmetic | Fix if time allows |
| 2 | Minor | Low priority |
| 3 | Major | High priority |
| 4 | Usability catastrophe | Must fix before release |

Every finding in the readout carries a severity, a count ("three of five participants"), one piece of evidence (a clip or a quote) and a decision: fix, test again, accept or kill.

:::ai Synthetic participants
NN/g's Rosala and Moran found AI-simulated users sycophantic, shallow, unable to report real behavior and weakest for niche groups (Chapter 01 covers the evidence). A harness can play a participant to pilot your script and expose confusing tasks. It can't replace a single real session, and niche enterprise roles such as an on-call SRE or a security reviewer are where it's weakest.
:::

## Staffing the team

### The product trio

Teresa Torres defines the **product trio** as, at minimum, a product manager, a designer and a software engineer who are "jointly responsible for a shared outcome." Together they interview customers, map opportunities, choose a target, generate solutions and test them. She contrasts this with the handoff model, where requirements, mockups and code each get reworked as work passes between functions, and projects run late and over budget.

Cagan's empowered product team, in *Inspired* and *Empowered*, is the same idea at full size: a product manager, a product designer and typically two to ten engineers with a tech lead, given a problem rather than a feature.

For AI-powered products, this book extends the trio. Model quality and evals are core risks, so an **applied AI engineer** (or ML engineer) should be a standing fourth member during discovery. That's our recommendation, not Torres's.

### Team types and interaction modes

Matthew Skelton and Manuel Pais's *Team Topologies* names four team types: **stream-aligned** (delivers customer value along one value stream and owns its outcomes), **platform** (provides internal services that remove complexity for stream-aligned teams), **enabling** (helps other teams build a capability, temporarily) and **complicated subsystem** (owns a component that needs scarce specialist knowledge). It names three interaction modes: **collaboration** (close, time-boxed, expensive; good for discovering a new boundary), **X-as-a-Service** (one team consumes another's service through a clear interface) and **facilitating** (one team helps another remove obstacles).

Their central constraint is **cognitive load**: overloaded teams decide worse and move slower. Interaction modes should evolve, typically from collaboration to X-as-a-Service once an interface is stable.

Staffing a new initiative, answer two questions in writing: what type of team is this, and what's our interaction mode with each neighbor right now?

Cagan's 2025 essay on **forward deployed engineers** describes a pattern he sees in complex enterprise settings, including AI-agent startups: an engineer (increasingly a PM or designer) embedded with a target customer to learn their environment and what their outcomes require. Forward deployed engineers prototype with customers, and a platform team generalizes what they learn. Without a platform strategy, Cagan cautions, the pattern produces many expensive custom solutions.

### Capacity, honestly

A staffing plan that lists names but not capacity is a wish. Start from the people assigned, then subtract what they can't spend on the new work: on-call, maintenance, support escalations, migrations and other keep-the-lights-on load. What's left is usually smaller than the slide says.

Then compare it with **appetite**, Ryan Singer's term in *Shape Up* for how much time the business is willing to spend on a problem. Fixing time and varying scope keeps teams out of endless negotiation; in Singer's words, "Stating the appetite in the pitch prevents unproductive conversations." The staffing plan and the PRD should state the same appetite.

:::leader For product leaders
Staffing is a strategy decision expressed in headcount. Find the binding constraint (often a single designer, one applied AI engineer or a platform team every initiative depends on), name it in the plan, and decide explicitly whether to add capacity, sequence the work or cut scope. An unnamed constraint gets resolved by whoever escalates loudest.
:::

## Writing the PRD

### Prototype shows, PRD decides

In a 2006 SVPG essay, "Revisiting the Product Spec," Cagan argued that traditional specs take too long to write, are seldom read and create a false sense of progress. A high-fidelity prototype covering nearly all the screens and major use cases should be most of the spec, he wrote, and the spec isn't ready for engineering until that prototype has passed usability and desirability tests. He kept a written supplement for what a prototype can't show: use cases, release requirements such as reliability, performance and scalability, and platform requirements.

In B2B and platform products, that supplement is large. API contracts, permissions, service levels, compliance obligations, pricing and packaging, migration and partner impact don't appear on any screen. This book's rule is **prototype shows, PRD decides**. The prototype is the behavior spec. The PRD is the decision record: why this problem, for whom, what's in and out, how you'll know it worked, and every requirement the prototype can't show.

Ben Horowitz's "Good Product Manager/Bad Product Manager," written in the 1990s and posted publicly in 2012, sets the tone: good product managers give direction in writing, define the *what*, leave the *how* to engineering and take written positions on the important tradeoffs. A PRD that specifies database tables has wandered into engineering's job. A PRD that won't take a position on scope has skipped the PM's.

### What a PRD contains

Teams vary widely, as Lenny Rachitsky's survey of PM templates shows. This book's full PRD has these sections, each there because a decision depends on it:

| Section | The question it answers |
|---|---|
| Problem and evidence | What's wrong, for whom, and how do we know? |
| Customers and personas | Which personas, including the buying group? |
| Goals and success metrics | What outcome moves, by how much, measured how? |
| Non-goals | What this version deliberately doesn't do |
| Scope and user journeys | What the user does, step by step (link the tested prototype) |
| Requirements and acceptance criteria | What must be true for each journey to count as done |
| Non-functional requirements | Security, permissions, audit, performance, reliability, data residency, accessibility |
| Dependencies and staffing | Which teams, which interaction modes, what capacity |
| Risks and open questions | What could still go wrong, and what we don't know yet |
| Rollout, pricing and packaging | How it reaches customers and what it costs them |
| Decision log | What was decided, by whom, when, and why |

### The one-page PRD

Most work doesn't need eleven sections on day one. The one-page PRD is this book's synthesis of Singer's pitch and the one-pager format Rachitsky collects. From Singer it takes three ingredients most PRDs lack: **appetite**, **no-gos** (explicit exclusions) and **rabbit holes** (known pitfalls, patched in advance). Its sections are problem, who, why now, appetite, a solution sketch linked to the prototype, success metric, non-goals, top risks and open questions.

Use it to align leadership and the trio on a bet, then grow it into the full PRD as test results arrive.

### PR/FAQ or PRD?

Amazon's **working backwards** method, which Werner Vogels described in 2006, starts from the customer and works back to the minimum technology needed. Vogels listed four documents written before building: a press release, an FAQ, a description of the customer experience (mockups of each screen or, for web services, use cases with code samples) and a user manual.

Colin Bryar and Bill Carr's *Working Backwards* describes the **PR/FAQ** in practice. The press release names the product, the customer and the benefit, then covers the problem, the solution, quotes from a spokesperson and a hypothetical customer, and how to get started. The FAQ has an external half (price, how it works, support) and an internal half (competition, demand, unit economics, investment, legal issues, dependencies and the top reasons it could fail). Most PR/FAQs never become products, by design.

The two documents answer different questions, in sequence:

| | PR/FAQ | PRD |
|---|---|---|
| Decides | Whether to build | What to build and how we'll know it works |
| Written | Before discovery commits real effort | After prototype tests, revised through delivery |
| Reader | Leaders deciding on investment | The team building it and the teams that depend on it |
| Main content | Customer narrative, economics, risks | Scope, requirements, acceptance, non-functional needs, decisions |
| Evidence | Assumptions, stated plainly | Test results and data |

The sequence that works: PR/FAQ, then prototype tests, then PRD. Platform PMs should take Vogels' point about web services literally. The customer experience of an API is sample code, so writing the developer documentation before building is one of the strongest prototypes a platform PM has.

### The PRD has two readers now

In September 2025, GitHub released Spec Kit, an open-source toolkit for writing specs that AI coding agents consume, and Den Delimarsky described the approach as **spec-driven development**. It has four phases: specify (what and why, user journeys, success criteria), plan (stack, architecture, constraints), tasks (small, testable items) and implement (the agent works the tasks while humans review focused changes). Vague prompts force agents to guess, so the intent written in the spec becomes the source of truth.

The PRD may now be read by people and by agents. The PM still owns the *what* and the *why*: user journeys, acceptance criteria, non-goals and constraints, written precisely enough that an agent could turn them into a plan and tests. Engineering owns the plan and the tasks. A requirement an agent can't interpret ("make it intuitive") was never a good requirement for people either.

### The AI feature addendum

When the feature is AI-powered, the classic PRD is necessary but not sufficient. Chapter 31 covers the **AI PRD addendum**: evals with pass-rate targets as acceptance criteria, a failure taxonomy, latency budgets and cost per task, trust and failure UX, staged autonomy with a kill switch, a gross-margin floor and regulatory classification. Attach it to the PRD for any feature where a model's output reaches a user or takes an action.

## How to apply it

This method runs one discovery-to-PRD cycle on a significant bet, after the hypothesis work in Chapter 01. Plan on four to eight weeks.

**Frame (week 1)**

1. **Pick the riskiest assumptions** from the top-right quadrant of the assumption map. Write a risk question for each and name the risk it tests.
2. **Write the PR/FAQ** if the bet is new or large, and hold the review. Proceed only on a go.
3. **Write the one-page PRD**, with appetite and no-gos. It will be wrong in places; that's what the tests are for.

**Prototype (weeks 1 to 3)**

4. **Choose the type and rung** for each risk question: the lowest rung that can answer it. For expert users, turn up content fidelity before visual fidelity.
5. **Assign builders by type.** Engineers build feasibility and live-data prototypes; designers and PMs build user prototypes. Decide up front which are throwaway.
6. **Set the data rule.** No real customer data in any prototype a PM or designer built with a prompt-to-app or chat tool. Use realistic synthetic data that a domain expert has checked for believability.
7. **Pilot every prototype** with a colleague before real sessions.

**Test (weeks 2 to 5)**

8. **Write the test plan**: the decision it informs, the risk question, the prototype, participants per role, three to five tasks, pre-registered signals, logistics and the readout date.
9. **Recruit three to five participants per distinct role**, through customer success and sales.
10. **Run moderated remote sessions with think-aloud.** The trio watches every session; invite one stakeholder who needs convincing.
11. **Debrief the same day, then iterate.** Fix the worst problems with the smallest change and retest with new participants.

**Decide and write (weeks 5 to 8)**

12. **Write the readout.** Rate findings by severity with counts and evidence, compare them with the signals and recommend proceed, iterate, pivot or stop.
13. **Write the staffing plan**: team type, roles, interaction modes, net capacity, appetite and the binding constraint.
14. **Grow the one-pager into the full PRD.** Link the tested prototype as the behavior spec; add non-functional requirements, dependencies and the decision log; attach the Chapter 31 addendum for AI features.
15. **Review the PRD with engineering, design and the gatekeepers** (security, legal, partner teams) before delivery planning starts. Stories and acceptance criteria continue in Chapter 06.

Later test results revise the PRD, and every revision lands in the decision log.

## The AI lens

### Prototyping AI-powered products

AI features change what a prototype has to prove.

- **Quality is the first feasibility question.** For a deterministic feature, feasibility asks whether you can build it. For an AI feature it asks whether the output is good enough, often enough. Answer that with a hybrid prototype first: run the model on real historical cases with no live traffic and have domain experts grade the output. If quality is far from the bar, interface polish won't save it.
- **Test trust, not only usability.** A user can understand an AI output perfectly and still not act on it, or act on it when they shouldn't. Seed tasks where the AI is wrong on purpose. For an AI feature, the most important usability finding is whether users catch a confident, plausible mistake.
- **Use Wizard of Oz to separate the experience from the model.** A human wizard produces the ideal output so you learn whether the format, evidence and level of autonomy drive trust before the model can deliver it. Have engineers define feasible responses so the wizard doesn't promise what the model can't do.
- **Prototype the failure states.** Every AI prototype needs a screen for "I'm not sure," a way to correct the output and a way to undo an action. A happy-path-only prototype tests a product that won't exist.

### Doing the work with AI

Hand the harness the mechanical work:

- Drafting the test plan from the PR/FAQ's riskiest assumptions and the assumption map.
- Generating realistic synthetic data (incidents, logs, tickets) for prototypes, for a domain expert to review.
- Building single-screen prototypes in several variants so the trio can compare directions.
- Piloting the script against a synthetic participant to find confusing or leading tasks.
- Transcribing sessions, clustering observations and drafting the readout with counts and timestamps.
- Drafting the capacity table and the PRD from the schedules, readout and decision log.

Keep with people:

- Choosing the risk question, moderating sessions, judging severity and making the decision.
- Verifying every number in the readout against the recordings. "Four of five" when it was three of five changes the decision.
- Taking positions in the PRD. A harness will happily produce a balanced document that decides nothing.

Cagan's 2026 framing fits: PMs should be builders who build to learn, and the hard skill is product sense, judging what a prototype reveals. If the harness makes you faster at producing artifacts, including PRDs, but no better at deciding, you've walked into the productivity paradox.

:::ai Two rules for AI-assisted discovery
Every AI-built prototype is labeled with what it ignores and that its data is synthetic. Every AI-drafted readout links each finding to a clip or timestamp a person has checked. Customer recordings and transcripts go only into tools your company has approved for customer data.
:::

## The Beacon case: prototyping supervised remediation

:::example Where Beacon starts
Chapter 01's discovery split Beacon Agents in two: diagnosis ships first, and supervised remediation (the agent proposes a runbook step such as a rollback, and a human approves it) follows, gated on audit logs, scoped credentials and a kill switch. Leadership wants supervised remediation announced at Northlight Live. Before anyone commits a date, you need evidence.
:::

**The risk questions.** The trio, now four with an applied AI engineer, writes three:

1. *Usability and value:* Will Dana, paged at 3 a.m., correctly approve or reject an agent-proposed action from the evidence on screen within five minutes?
2. *Viability (adoptability):* Will Sam approve the permissions and audit model for allowlisted actions?
3. *Feasibility:* Can the agent retrieve recent deploys and change tickets through the existing connectors, including MCP servers, and cite them within the latency budget?

**The prototype set.** Each question gets the lowest rung that answers it:

- **Feasibility prototype.** The applied AI engineers wire the agent to the deploy and change-ticket connectors in a sandbox and measure citation latency. No interface; throwaway.
- **User prototype.** The designer and you build the approval screen with a design-to-code tool: proposed action, root cause, cited evidence, blast radius, approve and reject. Content fidelity is high: Priya's team helps write a dozen realistic incidents. No real customer data goes near it.
- **Wizard of Oz.** In two design-partner sessions, an SRE on the Beacon team writes the "agent's" diagnosis live behind the interface, to learn whether the evidence format drives trust before the agent can produce it. Participants are debriefed afterward.
- **Hybrid prototype.** With two design partners' agreement and under their data controls, the agent diagnoses real past incidents: live data, no live traffic, no actions executed. Two SREs grade each diagnosis to estimate the offline diagnosis acceptance rate.

**The prototype that wanted to ship.** Two weeks in, a sales leader asks to demo the approval screen at Marcus's peer roundtable as "what's coming." You walk through what's missing: least-privilege access, per-action audit logs, data residency and the kill switch, exactly Sam's requirements. It goes to the roundtable as a labeled concept with invented data.

**The test.** Moderated remote sessions with think-aloud cover three roles: five on-call engineers (Dana's role) and three SRE leads (Priya's) on the approval flow, and three security reviewers (Sam's) on the permissions and audit screens. No task names an interface label. Each on-call engineer sees four incidents, one with a seeded wrong root cause: a plausible recent deploy that the timeline contradicts. The pre-registered signals: proceed if at least four of five on-call engineers make the right call on every incident; kill this design if any participant approves the seeded wrong rollback without opening the evidence.

**The readout.** Round one trips the kill signal.

| Severity | Finding | Count | Decision |
|---|---|---|---|
| 4 | Evidence citations sit behind a tab; participants approved the seeded wrong rollback without opening it | 3 of 5 on-call engineers | Fix before retest: list the cited evidence on the approval screen itself |
| 3 | "Blast radius" wording unclear; reviewers couldn't tell which services an action could touch | 2 of 3 security reviewers | Fix: list affected services and credentials explicitly |
| 2 | SRE leads wanted to see who approved past actions | 2 of 3 SRE leads | Accept for v1; add to audit-log requirements |

The Wizard of Oz sessions agree: participants questioned weak diagnoses when the evidence appeared with timestamps, and trusted them when it was summarized. In round two, with the cited evidence listed on the approval screen, all five new on-call engineers reject the seeded wrong rollback, and all three security reviewers say they could approve the permissions model if the audit log ships with it.

You also record what the test couldn't tell you: whether responders still check the evidence at 3 a.m., under real pressure, after weeks of mostly correct diagnoses, and whether the agent's real failure modes look like the seeded one. Both become open questions in the PRD and things the design-partner pilot must measure. Chapter 31 picks up what happens when one of them goes wrong.

**The staffing plan.** With three PMs, one designer, about 35 engineers across five teams and two applied AI engineers in Beacon, the plan makes Beacon Agents a **stream-aligned team**: you as PM, the designer (shared with the rest of Beacon, and named as the binding constraint), a tech lead, six engineers and one applied AI engineer. The connectors team serves as a **platform team** through an X-as-a-Service interface, after two weeks of collaboration to agree the approval and audit APIs. The second applied AI engineer and a senior SRE run an **enabling** effort for one quarter to build the eval practice into the team. One engineer works in a forward-deployed pattern with two design partners. Net capacity is what's left after on-call and the team's share of migrating customers off Beacon Classic. The plan asks for one decision: hire or borrow a second designer, or sequence the MSP work for Leo after launch.

**The PRD.** You grow the one-pager into the full PRD, targeted at Northlight Live, with the tested prototype as the behavior spec. Non-goals include fully autonomous actions beyond each customer's allowlist and multi-tenant views for MSP partners such as Leo in v1. The Chapter 31 addendum covers diagnosis acceptance evals, the failure taxonomy, cost per resolved incident (a pointed question: Beacon's gross margin already fell from 81% to 72% after agentic features launched) and the EU AI Act documentation European customers have asked for.

The PR/FAQ from week one, with its imagined Northlight Live announcement and an internal FAQ on per-resolved-incident pricing and margin, decided the bet was worth testing. The PRD decides what v1 is, and v1 is narrower than the press release imagined.

## Product 360 artifacts

These templates are this book's syntheses of the methods above. The test plan, script and readout are used once per round; the staffing plan and the PRDs are durable and revised as the work moves.

```template id="04-prototype-test-plan" title="Prototype test plan"
# Prototype test plan · [Initiative] · Round [n] · [Date]

**Owner:** [PM]   **Trio:** [PM, designer, engineer, applied AI engineer if AI]   **Decision owner:** [Name]   **Readout date:** [Date]

## Decision this test informs
[The specific decision, e.g. "Proceed to PRD with design A, iterate, or stop."]

## Risk question
We are testing whether [persona] will [observable behavior] when [situation], using [prototype].
Risk type: Value / Usability / Feasibility / Viability (adoptability)
Assumption(s) from the assumption map: [#, #]

## Prototype
- Type: Feasibility / Low-fidelity user / High-fidelity user / Live-data / Hybrid / Wizard of Oz / Concierge
- Fidelity: Interactivity [L/M/H] · Visuals [L/M/H] · Content [L/M/H]
- Built by: [Name, tool category]
- Throwaway or reusable: [ ]
- Deliberately ignores: [permissions, scale, audit, multi-tenancy, ...]
- Data: synthetic (reviewed by [domain expert]) / real (engineering-owned, with [controls])
- Piloted with: [Colleague] on [Date]

## Participants
| Role (persona) | Count this round | Screener criteria | Recruiting source |
|---|---|---|---|
| | | | |

## Tasks (three to five, no interface labels)
1.
2.
3.

## Signals (agreed before testing)
- Proceed if:
- Iterate if:
- Kill or pivot if:

## Logistics
Format: moderated remote / in person / unmoderated   Session length: [min]   Recording consent: [method]
Observers: [names]   Debrief: same day, [time]
Wizard of Oz or deception used: Yes / No   If yes, debrief script: [link]
Customer data handling: [approved tools only; what's recorded and where it's stored]
```

```template id="04-usability-test-script" title="Usability test script"
# Usability test script · [Prototype] · [Persona] · [Date]

**Facilitator:** [Name]   **Note-taker:** [Name]   **Length:** [45 to 60] minutes

## 1. Welcome and consent (5 min)
- Thank them. Explain the session: "We're testing a design, not you. You can't do anything wrong here."
- "Some of what you see won't work yet. That's expected."
- Ask permission to record. Name who is observing.

## 2. Thinking aloud (3 min)
- "As you work, please say what you're thinking: what you're looking at, what you expect, what surprises you."
- Warm-up: ask them to think aloud while doing a simple task on a familiar site or tool.

## 3. Background (5 min)
- "Tell me about your role and how [the situation] usually comes up for you."
- "Tell me about the last time it happened. What did you do?"

## 4. Tasks (25 to 35 min)
Read one task at a time. Hand it over in writing as well.

| # | Scenario (realistic, actionable, no clues) | What we're watching for | Post-task question |
|---|---|---|---|
| 1 | | | "How confident are you in what you just decided, from 1 to 7? Why?" |
| 2 | | | |
| 3 | | | |

Facilitator rules: stay quiet. Prompt only on silence ("What are you thinking now?"). Don't answer questions about the interface; turn them back ("What would you expect?"). Note every intervention.

## 5. Wrap-up (5 min)
- "What was most confusing? What was most useful?"
- "If you could change one thing, what would it be?"
- If Wizard of Oz was used: explain that a person produced some responses, why, and offer to answer questions.
- Thank them and confirm any incentive.

## Note-taking grid
| Time | Task | What they did | What they said (verbatim) | Intervention? |
|---|---|---|---|---|
| | | | | |
```

```template id="04-test-readout" title="Usability test readout"
# Test readout · [Initiative] · Round [n] · [Date]

**Decision requested:** [proceed / iterate and retest / pivot / stop]   **Decision owner:** [Name]   **Recordings:** [link, access-controlled]

## Summary (three sentences)
What we tested, with whom, and what we recommend.

## Against the pre-registered signals
| Signal | Threshold | Result | Met? |
|---|---|---|---|
| Proceed | | | |
| Kill | | | |

## Findings, ranked by severity
Severity: 0 not a problem · 1 cosmetic · 2 minor · 3 major · 4 catastrophe (must fix before release)

| # | Severity | Finding | Count (n of N, by role) | Evidence (clip or quote, timestamp) | Decision (fix / retest / accept / kill) |
|---|---|---|---|---|---|
| 1 | | | | | |

## What we'll change before the next round
Smallest change that fixes each severity 3 and 4 finding:
1.
2.

## What worked (keep)
-

## What we still don't know
-

## Effect on the hypothesis and PRD
Assumptions confirmed, revised or killed: [#, #]   PRD sections to update: [ ]

## Verification
Every count and quote checked against recordings by [Name] on [Date].
```

```template id="04-team-staffing-plan" title="Team staffing plan"
# Team staffing plan · [Initiative] · [Date]

**Owner:** [PM]   **Approver:** [Leader]   **Review date:** [Date]

## Outcome and appetite
- Outcome the team owns: [metric and target]
- Appetite: [weeks or quarters] for [scope boundary]

## Team type
Stream-aligned / Platform / Enabling / Complicated subsystem. Why:

## Roles
| Role | Named person | Allocation (%) | Responsibilities | Backfill or gap |
|---|---|---|---|---|
| Product manager | | | | |
| Product designer | | | | |
| Tech lead | | | | |
| Engineers | | | | |
| Applied AI engineer (AI features) | | | | |
| Forward-deployed engineer (if used) | | | | |
| Product marketing | | | | |
| Other (data, security, docs) | | | | |

## Interaction modes with neighboring teams
| Team | Mode now (collaboration / X-as-a-Service / facilitating) | Until | Target mode | Interface or agreement |
|---|---|---|---|---|
| | | | | |

## Capacity
| | Engineer-weeks per quarter |
|---|---|
| Gross (people × weeks × allocation) | |
| Less on-call | |
| Less maintenance and support | |
| Less migrations and other keep-the-lights-on work | |
| **Net capacity for this initiative** | |

Net capacity versus appetite: [fits / doesn't fit, by how much]

## Binding constraint
[The one role or team that limits throughput, and the decision needed: add, borrow, sequence or cut.]

## Dependencies and risks
-

## Asks
-
```

```template id="04-prd" title="Product requirements document (PRD)"
# PRD · [Feature or product] · v[n] · [Date]

**Owner:** [PM]   **Status:** Draft / In review / Approved / In delivery / Shipped   **Reviewers:** [engineering, design, security, legal, partner, PMM]
**Links:** Hypothesis · PR/FAQ · Prototype (behavior spec) · Test readouts · Staffing plan · AI addendum (Chapter 31)

## 1. Problem and evidence
What's wrong, for whom, how often, what it costs. Cite interviews, test readouts and data.

## 2. Customers and personas
| Persona | Role in the deal | What they need from this release |
|---|---|---|
| | | |

## 3. Goals and success metrics
| Metric | Baseline | Target | Measured how | By when |
|---|---|---|---|---|
| | | | | |

## 4. Non-goals
What this version deliberately doesn't do, and why.

## 5. Scope and user journeys
Journey 1: [persona] [situation] → [steps] → [outcome]. Prototype link: [ ]
Journey 2:

## 6. Requirements and acceptance criteria
| # | Requirement (the what) | Journey | Acceptance criteria (testable by a person or an agent) | Priority |
|---|---|---|---|---|
| | | | | |

## 7. Non-functional requirements
- Security and permissions:
- Audit and logging:
- Performance and reliability:
- Data residency and privacy:
- Accessibility and localization:
- Integrations and APIs (contracts, versioning):

## 8. Dependencies and staffing
Teams, interaction modes and capacity, from the staffing plan.

## 9. Risks and open questions
| Risk or question | Impact | Owner | How we'll resolve it | By when |
|---|---|---|---|---|
| | | | | |

## 10. Rollout, pricing and packaging
Rollout stages, eligibility, migration, enablement, pricing and packaging impact.

## 11. AI features only
Attach the AI PRD addendum (Chapter 31): evals and pass-rate targets, failure taxonomy, latency and cost per task, trust and failure UX, staged autonomy and kill switch, margin floor, regulatory classification.

## 12. Decision log
| Date | Decision | Options considered | Decided by | Rationale |
|---|---|---|---|---|
| | | | | |
```

```template id="04-one-page-prd" title="One-page PRD"
# One-page PRD · [Bet] · [Date]

**Owner:** [PM]   **Decision needed:** [what, from whom, by when]

**Problem.** [Two or three sentences, with the strongest piece of evidence.]

**Who.** [Primary persona, and the buying-group member who could block it.]

**Why now.** [What changed: customer demand, technology, competition, strategy.]

**Appetite.** [Time the business is willing to spend, and the team that would spend it.]

**Solution sketch.** [Core elements in a few bullets. Prototype link: ]

**Success metric.** [One metric, baseline, target, timeframe.]

**Non-goals and no-gos.**
-
-

**Rabbit holes.** [Known pitfalls and how we'll avoid them.]

**Top risks.** [Value / usability / feasibility / viability, one line each.]

**Open questions.**
-

**Next step.** [Test, build or stop, and when this page becomes a full PRD.]
```

## Prompts

```prompt title="Choose the right prototype for a risk question"
Goal: Pick the lowest rung on the fidelity ladder that can answer each risk question.
Paste in: your assumption map (top-right quadrant), the personas involved and any constraints on time, people or data.

For each assumption below, act as a skeptical product coach and:
1. Rewrite it as a risk question: "We are testing whether [persona] will [observable behavior] when [situation]."
2. Name the risk type: value, usability, feasibility or viability (including adoptability: will security, procurement and the buying group let it through?).
3. Recommend a prototype type (feasibility, low- or high-fidelity user, live-data, hybrid, Wizard of Oz or concierge) and set each fidelity dial (interactivity, visuals, content) to low, medium or high. Explain why a lower rung wouldn't answer the question.
4. Say who should build it (engineer, designer, PM), whether it's throwaway, and what it deliberately ignores.
5. State whether it needs real customer data. If it does, say that engineering must own it.

Don't recommend a higher-fidelity prototype than the question needs.

[assumptions, personas, constraints]

Check the output: for each recommendation, ask whether a sketch or wireframe with realistic content would answer the same question. If it would, drop a rung.
```

```prompt title="Draft a usability test plan and script"
Goal: Get a test plan and script that map results to a decision before any session runs.
Paste in: the risk question, the prototype description, the personas and the decision the test informs.

Draft a moderated remote usability test plan and script for [prototype], testing this risk question: [risk question].

Plan: the decision this informs; participants per distinct role (three to five each); three to five tasks; proceed, iterate and kill signals stated as observable thresholds; logistics including recording consent and same-day debrief.

Script: welcome and consent ("we're testing the design, not you"); think-aloud instructions with a warm-up; background questions about the participant's last real experience of the situation; each task as a realistic, actionable scenario; a confidence question after each task; wrap-up.

Task rules: never name a button, tab or menu label; never give steps; give the context a real user would have. If this is an AI feature, include at least one task where the AI output is plausibly wrong and the evidence on screen shows it.

[risk question, prototype, personas, decision]

Check the output: read each task aloud and delete any interface word that appears on the screen. Make sure the kill signal is something you'd actually act on.
```

```prompt title="Pilot the script with a synthetic participant"
Goal: Catch confusing, leading or impossible tasks before a real customer sees them.
Paste in: the test script and a short description of the persona and their environment.

Role-play as [persona description] in a moderated usability session using this script. Respond to each task briefly, in character, describing what you'd look for and where you might get stuck. Then step out of character and list:
1. Tasks that give away the answer or name interface elements.
2. Tasks a real person in this role couldn't attempt without context the script doesn't give.
3. Questions likely to produce opinions rather than behavior.
4. Anything that would take much longer than the time allotted.

Your in-character responses are not research and won't be reported as findings. I only want feedback on the script.

[script]

Check the output: use only the script feedback. Discard the in-character answers. Then pilot with a real colleague before the first session.
```

```prompt title="Turn session notes into a test readout"
Goal: Draft a readout that ranks findings by severity and ties them to the decision.
Paste in: session transcripts or notes (with timestamps), the test plan with its pre-registered signals and the observers' debrief notes. Use only tools approved for customer recordings.

Draft a usability test readout for [test].
1. List every distinct problem observed. For each: what happened, which participants (by ID and role), a verbatim quote or behavior with timestamp.
2. Propose a severity from 0 to 4 using frequency, impact and persistence. Show your reasoning; I'll decide the final rating.
3. Compare results with each pre-registered signal and say whether it was met.
4. For severity 3 and 4 findings, suggest the smallest change that might fix the problem.
5. List what worked, what we still don't know, and which assumptions were confirmed, revised or killed.

Rules: count only what the transcripts show. Never paraphrase inside quotation marks. If participants disagreed, say so. Don't recommend a decision; leave that section for me.

[test plan, transcripts, debrief notes]

Check the output: verify every count and quote against the recordings. Watch for findings inflated from one participant into "users."
```

```prompt title="Draft a staffing plan with honest capacity"
Goal: See whether the team you have can deliver the appetite you've stated.
Paste in (or connect the harness to): the team roster with allocations, the on-call schedule, the last two quarters of ticket and maintenance load, known migrations and the appetite from the one-page PRD.

Draft a staffing plan for [initiative].
1. Propose a team type (stream-aligned, platform, enabling or complicated subsystem) and explain why.
2. List roles, named people and allocation. Flag any role with no owner.
3. For each neighboring team, propose an interaction mode now (collaboration, X-as-a-Service or facilitating), when it should change and to what.
4. Calculate net capacity in engineer-weeks: gross capacity minus on-call, maintenance and support, and migrations, using the data provided. Show each subtraction and its source.
5. Compare net capacity with the appetite. Identify the binding constraint and give options: add, borrow, sequence or cut scope.

If data is missing for any subtraction, say so instead of estimating silently.

[roster, schedules, load data, appetite]

Check the output: confirm the subtractions with the tech lead. Ask whether the binding constraint the model named is the one the team would name.
```

```prompt title="Grow a one-pager into a PRD"
Goal: Draft a full PRD from the evidence, written for people and for coding agents.
Paste in: the one-page PRD, test readouts, the decision log, the staffing plan and links to the tested prototype.

Draft a PRD for [feature] with these sections: problem and evidence; customers and personas; goals and success metrics; non-goals; scope and user journeys; requirements with acceptance criteria; non-functional requirements (security, permissions, audit, performance, reliability, data residency, accessibility, integrations); dependencies and staffing; risks and open questions; rollout, pricing and packaging; decision log.

Rules:
- Define the what and the why, never the how. Leave architecture and tasks to engineering.
- Write each acceptance criterion so a person or a coding agent could turn it into a test.
- Every claim in "problem and evidence" must cite a readout, interview or data source from the material. Write "No evidence yet" where there is none.
- Treat the prototype as the behavior spec; describe only what it can't show.
- Where the material shows an unresolved tradeoff, write it as an open question with an owner. Don't resolve it yourself.
- If this is an AI feature, add a placeholder for the AI PRD addendum and list the questions it must answer.

[material]

Check the output: delete any sentence that would read the same in any company's PRD. Confirm the non-goals with the trio, and check that each non-functional requirement has a gatekeeper who has seen it.
```

```prompt title="Red-team a PRD before review"
Goal: Find the gaps a security reviewer, an engineer or a partner team would find, before the review.
Paste in: the PRD and, for AI features, its addendum.

Review this PRD as three reviewers in turn: a skeptical tech lead, a security and compliance reviewer, and the PM of a team that depends on this feature. For each reviewer:
1. List the requirements that are ambiguous or untestable.
2. List what's missing that they'd need to approve it.
3. Name the decision the PRD avoids taking.
Then list any place where the PRD describes a prototype's behavior as if it were already built to production standards (reliability, observability, scale, integrations, security, recovery).

[PRD]

Check the output: fix the gaps that would block approval. For the rest, add them to open questions with an owner rather than expanding the PRD.
```

## Anti-patterns

:::warn The demo that became a commitment
A polished AI-built prototype is shown to an executive or a customer without a label. Within a week it has a launch date. Label every prototype with what it ignores and that its data is synthetic, and show it as a concept.
:::

:::warn Polish before the question, fake content in it
The team spends two weeks perfecting a high-fidelity prototype for a question a wireframe could answer, then fills it with placeholder logs no SRE would believe. Start with the lowest rung that answers the risk question, and for expert users turn up content fidelity first.
:::

:::warn Five users, total
The team tests five people across three roles and declares the flow validated. Five is per distinct role, per round. Plan a small panel for each role, and iterate.
:::

:::warn Results without pre-agreed signals
The readout arrives, half the room reads it as success and the other half as failure, and the decision slips a month. Write the proceed, iterate and kill signals in the test plan before the first session.
:::

:::warn Real customer data in a vibe-coded prototype
A builder prototype gets connected to a design partner's real logs "just for the demo." Nobody has reviewed its access controls. Prototypes built by PMs and designers use synthetic data. Anything that touches real data is built and reviewed by engineering.
:::

:::warn The staffing plan without capacity
The plan lists six engineers and a launch date. It doesn't subtract on-call or the migration the same engineers own. Calculate net capacity, compare it with the appetite and name the binding constraint.
:::

:::warn The long, unread PRD
A forty-page PRD, drafted quickly with AI, restates the prototype in prose and takes no positions. Keep the PRD for decisions, non-goals and what no screen can show.
:::

## Checklist

- [ ] Every prototype has a written risk question, a risk type and a list of what it deliberately ignores.
- [ ] Each prototype is the lowest rung that answers its question, and engineers own anything touching real data.
- [ ] No prototype built by a PM or designer holds real customer data, and every prototype shown outside the team is labeled as a concept.
- [ ] AI-feature prototypes include failure states, and tests include a seeded wrong output.
- [ ] The test plan names the decision it informs and pre-registers proceed, iterate and kill signals.
- [ ] Each distinct role has three to five participants per round, recruited against a screener.
- [ ] Tasks are realistic and actionable and name no interface labels; the script has been piloted.
- [ ] Sessions use think-aloud, the trio observes and the debrief happens the same day.
- [ ] The readout rates every finding by severity, with counts and evidence checked against recordings.
- [ ] The staffing plan names team type, interaction modes, net capacity after keep-the-lights-on load and the binding constraint.
- [ ] A one-page PRD with appetite and no-gos exists before the full PRD.
- [ ] The full PRD links the tested prototype as the behavior spec and covers non-functional requirements, non-goals and a decision log.
- [ ] Acceptance criteria are testable by a person or an agent.
- [ ] AI features have the Chapter 31 addendum attached.
- [ ] Large new bets have a reviewed PR/FAQ before discovery commits real effort.

## Key takeaways

- A prototype exists to answer one risk question about value, usability, feasibility or viability. Write the question, and what the prototype ignores, before anyone builds it.
- Choose the lowest rung on the fidelity ladder that answers the question, and set fidelity per dial. For expert B2B users, realistic content matters more than visual polish.
- AI builders make prototypes cheap and convincing. They don't close the gap to a product: reliability, security, scale, integrations and compliance are still delivery work, owned by engineering.
- Test with three to five participants per distinct role per round, using think-aloud and tasks without clues. Pre-register the signals so results map to a decision.
- Staff the team as a trio (plus an applied AI engineer for AI products), name its team type and interaction modes, and plan from net capacity, not headcount.
- The prototype shows the behavior; the PRD records the decisions and everything a screen can't show. Write it for people and agents, start with one page, and use a PR/FAQ first when the question is whether to build at all.
