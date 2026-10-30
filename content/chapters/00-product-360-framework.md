<p class="lead">Owning a product means you can answer nine questions about it at any moment, show the artifact that holds each answer, and say when that artifact was last made true. The Product 360 is the model for those nine questions, the stack of artifacts that answers them, and the operating cadence that keeps the answers current.</p>

## Why this matters

Most product managers inherit a product the same way: a handoff document, a Jira project, a roadmap slide that is two quarters stale, a Slack channel and a list of people to meet. Somewhere in there is the strategy. Some of it lives in a deck from last year's planning cycle, some in the head of the PM who just left, and some nowhere at all.

You can run a product like that for a while. Then the questions start arriving faster than you can reconstruct the answers. Sales asks why a competitor's feature isn't on the roadmap. Finance asks why gross margin dropped four points. A customer asks when the legacy version reaches end of support. An executive asks for the three-year view by Friday. Each question gets answered from scratch, slightly differently each time, and the product drifts toward whoever asked most recently.

A Product 360 fixes this by making the product legible: to you, to your team, to your executives and, in 2026, to the AI tools you work with. It isn't a document. It's a small, connected set of artifacts, each owning one part of the picture, plus a rhythm for updating them. When it works, you stop rebuilding context and start using it.

This chapter defines the model. Every other chapter in the book goes deep on one part of it, and the Capstone shows you how to build your own.

## What a product manager is for

Before defining the 360, it's worth being precise about the job it serves, because "product manager" covers wildly different roles across companies.

### The four risks

Marty Cagan's framing from *Inspired* is still the cleanest starting point. Every product idea carries four risks:

- **Value risk**: will customers buy it, or choose to use it?
- **Usability risk**: can users figure out how to use it?
- **Feasibility risk**: can engineering build it with the time, skills and technology available?
- **Business viability risk**: does it work for the rest of the business: sales, marketing, finance, legal, support, partners?

In Cagan's model, the product manager is accountable for value and viability, the designer for usability, and the tech lead for feasibility. The team owns all four together. That split matters for the 360: the artifacts a PM must own are the ones that answer value and viability questions, and the artifacts the PM must be able to read and challenge are the ones that answer usability and feasibility.

Cagan's later books push the model up a level. *Empowered* argues that strong product teams are given problems to solve, not features to build. *Transformed* describes the "product operating model": how a company changes the way it decides what to build (discovery before delivery), how it builds (small, frequent, instrumented releases) and how it chooses problems (strategy and insight rather than a stakeholder wish list). The Product 360 is, among other things, the set of artifacts that makes a product operating model visible.

### Three intersections

Martin Eriksson's well-known diagram places product management at the intersection of business, technology and user experience. It's a useful reminder that a PM who lives entirely in one circle stops doing the job. A PM who only talks to engineers becomes a project manager. One who only talks to sales becomes a feature broker. One who only talks to designers loses the business case.

The 360 enforces the intersection structurally. You can't keep it current without regularly touching all three circles.

Ken Norton adds the part of the job that no diagram captures: a PM leads by influence, without direct reports, and acts as the advocate "for whoever isn't currently in the room." Sometimes that's the customer. Sometimes it's engineering, sales or finance. The 360 is how the people who aren't in the room still get represented, because their part of the picture is written down.

### How AI is changing the role

The PM role is shifting, and the people who defined it are still arguing about how much. In early 2025 Cagan sketched a future in which a typical product team shrinks from about eight people to about three (a PM, a designer and an engineer), with delivery largely automated and discovery becoming the main work. By mid-2026 he had tempered that. In "The AI Productivity Paradox" he argued that teams using AI to speed up an output-focused process ship more without getting better outcomes, while strong product organizations pull further ahead. A month later he wrote that his earlier optimism about AI turning many more people into strong "product creators" had been too high: the hard part was never the code, it was knowing what should exist.

Practitioner data points the same way. A late-2025 survey of about 1,750 tech workers by Lenny Rachitsky and Noam Segal found PMs using AI most for writing PRDs and building prototypes, with nearly two-thirds saving four or more hours a week, and far fewer using it for upstream thinking like research or roadmap choices. Norton's twenty-year retrospective on his own essay makes a similar argument: the human parts of the job (judgment, influence, advocacy) are the least likely to be automated.

The practical reading for this book: AI makes the artifacts cheaper to produce, so producing artifacts is no longer the job. Knowing which ones matter, making the choices inside them and keeping them true is the job. The Product 360 is built around that.

### Three levels of product work

Shreyas Doshi distinguishes three levels at which product work happens: **impact** (are we working on the things that will move the business?), **execution** (are we doing those things well?) and **optics** (does it look like we're doing them well?). Teams get into trouble when they argue at different levels. An executive asking an impact question ("should we be in this market?") gets an execution answer ("we're on track for the March release").

The Product 360 is organized to keep those levels separate. Strategy artifacts answer impact questions. Plans, specs and metrics answer execution questions. Reviews and communication artifacts handle optics honestly: they're how you show the work without performing it.

:::onramp If you're new to product management
A PM's job is to decide, with the team, which problems are worth solving and to make sure the solution creates value for customers and the business. You don't need to be the smartest person on any single dimension. You need to be the person who sees all of them at once and makes the tradeoffs explicit. That "seeing all of them at once" is what a Product 360 is for.
:::

## The nine dimensions of the Product 360

The Product 360 divides the product into nine dimensions. Each one answers a question someone will eventually ask you, and each maps to a part of this book.

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 300" role="img" aria-label="The nine dimensions of the Product 360 grouped into Direction, Delivery and Durability">
  <rect x="10" y="10" width="220" height="250" rx="14" class="box"/>
  <rect x="250" y="10" width="220" height="250" rx="14" class="box"/>
  <rect x="490" y="10" width="220" height="250" rx="14" class="box"/>
  <text x="30" y="42" class="t" style="fill:var(--a1)">DIRECTION</text>
  <text x="30" y="60" class="s">Why and for whom</text>
  <text x="270" y="42" class="t" style="fill:var(--a2)">DELIVERY</text>
  <text x="270" y="60" class="s">What and how</text>
  <text x="510" y="42" class="t" style="fill:var(--a3)">DURABILITY</text>
  <text x="510" y="60" class="s">How it lasts</text>
  <g>
    <rect x="30" y="80" width="180" height="48" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".5"/><text x="46" y="101" class="t">1 Customer</text><text x="46" y="118" class="s">Who it's for, what job</text>
    <rect x="30" y="138" width="180" height="48" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".5"/><text x="46" y="159" class="t">2 Strategy</text><text x="46" y="176" class="s">Where we play, how we win</text>
    <rect x="30" y="196" width="180" height="48" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".5"/><text x="46" y="217" class="t">3 Business</text><text x="46" y="234" class="s">How it makes money</text>
  </g>
  <g>
    <rect x="270" y="80" width="180" height="48" rx="10" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)" stroke-opacity=".5"/><text x="286" y="101" class="t">4 Build</text><text x="286" y="118" class="s">What's next, how it's made</text>
    <rect x="270" y="138" width="180" height="48" rx="10" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)" stroke-opacity=".5"/><text x="286" y="159" class="t">5 Measure</text><text x="286" y="176" class="s">How we know it works</text>
    <rect x="270" y="196" width="180" height="48" rx="10" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)" stroke-opacity=".5"/><text x="286" y="217" class="t">6 Go-to-market</text><text x="286" y="234" class="s">How it reaches customers</text>
  </g>
  <g>
    <rect x="510" y="80" width="180" height="48" rx="10" fill="var(--a3)" fill-opacity=".12" stroke="var(--a3)" stroke-opacity=".5"/><text x="526" y="101" class="t">7 Operate</text><text x="526" y="118" class="s">How we run it</text>
    <rect x="510" y="138" width="180" height="48" rx="10" fill="var(--a3)" fill-opacity=".12" stroke="var(--a3)" stroke-opacity=".5"/><text x="526" y="159" class="t">8 Lifecycle</text><text x="526" y="176" class="s">Where it is in its life</text>
    <rect x="510" y="196" width="180" height="48" rx="10" fill="var(--a3)" fill-opacity=".12" stroke="var(--a3)" stroke-opacity=".5"/><text x="526" y="217" class="t">9 Leadership</text><text x="526" y="234" class="s">Who must be aligned</text>
  </g>
  <rect x="10" y="272" width="700" height="24" rx="8" fill="var(--a2)" fill-opacity=".14"/>
  <text x="360" y="289" text-anchor="middle" class="s" style="fill:var(--text)">AI runs through every dimension: what you build and how you do the work</text>
</svg>
<figcaption>The nine dimensions, grouped by the kind of question they answer. AI is not a tenth dimension; it changes all nine.</figcaption>
</figure>

| Dimension | The question it answers | Core artifacts | Where in this book |
|---|---|---|---|
| **1. Customer** | Who is this for, and what job are they hiring it to do? | Personas, JTBD statements, journey maps, problem hypothesis, discovery log | Ch. 01, 10 |
| **2. Strategy** | Where do we play, how do we win, and what will we say no to? | Vision, strategy one-pager, competitive landscape, platform map | Ch. 02, 03, 13, 14, 16 |
| **3. Business** | How does this make money, and is the money worth it? | Business case, pricing and packaging, unit economics model | Ch. 12, 13, 15 |
| **4. Build** | What are we building next, and how does it get made? | Roadmap, PRDs and PRFAQs, backlog, release plan | Ch. 03, 04, 06, 11 |
| **5. Measure** | How do we know it's working? | North Star and metric tree, OKRs, dashboards, experiment readouts, evals | Ch. 02, 05, 09, 17 to 19 |
| **6. Go-to-market** | How does it reach, convince and keep customers? | Positioning, messaging, launch plans, enablement, announcements | Ch. 24 to 27 |
| **7. Operate** | How do we run it week to week? | Operating cadence, business reviews, decision log, risk register | Ch. 28, 29 |
| **8. Lifecycle** | Where is it in its life, and what happens next? | Lifecycle stage assessment, stage-gate criteria, sunset plans | Ch. 30 |
| **9. Leadership** | Who needs to be aligned, and are they? | Stakeholder map, DACI, communication plan, team charter | Ch. 34 to 36 |

The nine group into three families. **Direction** (customer, strategy, business) answers why and for whom. **Delivery** (build, measure, go-to-market) answers what and how. **Durability** (operate, lifecycle, leadership) answers how the product keeps working as a business over years, which is the part most PM training skips entirely.

:::key The test of a Product 360
Pick any of the nine questions. If you can open one artifact, show the answer and say when it was last made true, that dimension is covered. If the answer lives in a meeting, a person or a slide from last year, it isn't.
:::

### Why AI is not a tenth dimension

It would be easy to add "AI" as a tenth box. That would be a mistake, because in 2026 AI changes every one of the nine, in two different ways.

**AI in the product.** When the product itself is AI-powered, each dimension gets new questions. Customer: how much do users trust an answer they can't verify? Business: what does each inference cost, and does pricing cover it? Build: what's the eval suite, and which model are we on? Measure: how do we measure quality when the output isn't deterministic? Operate: who responds when the model starts producing worse answers after a provider update? Lifecycle: what happens to customers when the underlying model is deprecated? Chapter 31 covers these in depth, and every chapter has an AI lens section for its own dimension.

**AI in the work.** Separately, AI changes how you build and maintain the 360 itself. A harness like Claude, with connectors into your docs, tickets, CRM and analytics, can draft an artifact from raw material, check one artifact against another, and answer questions across the whole set. That only works if the 360 exists in a form the harness can read. Chapter 32 covers this, and the Capstone gives you the prompts.

## The artifact stack

A Product 360 is built from artifacts. Not every document is an artifact. An artifact, in this book, is a document with an owner, a purpose, an audience, and an update rhythm. If any of those four is missing, the document will rot.

### Three kinds of artifact

Artifacts change at different speeds, and treating them all the same is how teams end up with either a stale strategy or a strategy that changes every week.

- **Durable artifacts** change rarely, usually once a year or at a major strategic shift. Vision, strategy one-pager, personas, positioning. If these change monthly, you don't have a strategy; you have a mood.
- **Living artifacts** change on a cadence: weekly, monthly or quarterly. Roadmap, metrics dashboard, OKRs, risk register, decision log, competitive landscape. If these go a quarter without an update, they're lying to someone.
- **Event artifacts** are created for a specific decision or moment and then archived. PRDs, PRFAQs, launch plans, experiment readouts, business cases, post-launch reviews, sunset plans. They're written once, used intensely, and then become the history that explains why the product looks the way it does.

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 250" role="img" aria-label="The artifact stack: durable, living and event artifacts">
  <rect x="20" y="20" width="680" height="62" rx="12" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".5"/>
  <text x="40" y="46" class="t">Durable · yearly</text>
  <text x="40" y="66" class="s">Vision · strategy one-pager · personas · positioning · North Star · lifecycle stage</text>
  <rect x="60" y="94" width="600" height="62" rx="12" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)" stroke-opacity=".5"/>
  <text x="80" y="120" class="t">Living · weekly to quarterly</text>
  <text x="80" y="140" class="s">Roadmap · OKRs · dashboards · competitive landscape · risk register · decision log</text>
  <rect x="100" y="168" width="520" height="62" rx="12" fill="var(--a3)" fill-opacity=".12" stroke="var(--a3)" stroke-opacity=".5"/>
  <text x="120" y="194" class="t">Event · per decision or moment</text>
  <text x="120" y="214" class="s">PRD · PRFAQ · business case · launch plan · experiment readout · sunset plan</text>
</svg>
<figcaption>Durable artifacts constrain living ones; living artifacts decide which event artifacts get written. When an event artifact contradicts a durable one, either the event is wrong or the strategy needs to change, and that should be an explicit decision.</figcaption>
</figure>

The stack has a direction. Durable artifacts constrain living ones: the roadmap should be explainable from the strategy. Living artifacts decide which event artifacts get written: a PRD exists because something made it onto the roadmap. When an event artifact contradicts a durable one (a PRD for a segment the strategy says you don't serve), you've found either a bad PRD or a strategy that needs revisiting. Both are worth knowing, and the stack makes the conflict visible.

### The minimum viable 360

The full artifact list in this book runs to about a hundred templates. You won't maintain a hundred documents, and you shouldn't try. Most products need a spine of about twelve, with everything else created when an event calls for it.

| # | Artifact | Kind | Dimension |
|---|---|---|---|
| 1 | Product 360 index (the home page that links everything) | Living | All |
| 2 | Problem hypothesis and personas | Durable | Customer |
| 3 | Vision and strategy one-pager | Durable | Strategy |
| 4 | Competitive landscape | Living, quarterly | Strategy |
| 5 | Business model and unit economics summary | Living, quarterly | Business |
| 6 | Outcome roadmap (now / next / later) | Living, monthly | Build |
| 7 | North Star and metric tree, with the dashboard | Living, weekly | Measure |
| 8 | OKRs | Living, quarterly | Measure |
| 9 | Positioning and messaging | Durable | Go-to-market |
| 10 | Operating cadence and decision log | Living, weekly | Operate |
| 11 | Lifecycle stage assessment | Durable, reviewed yearly | Lifecycle |
| 12 | Stakeholder map and DACI | Living, quarterly | Leadership |

If you're building a 360 from nothing, build these twelve first, in roughly this order. The Capstone walks through it in a 30/60/90-day plan.

:::warn Template theater
The fastest way to kill a Product 360 is to create all hundred templates on day one, fill them with plausible text, and never touch them again. A half-empty 360 that's true is worth more than a complete one that's fiction. Build an artifact when a question demands it, and keep it only if someone uses it.
:::

### Where the 360 lives

The 360 needs one home: a single page (the **Product 360 index**) that links every artifact, names its owner and shows when it was last updated. That page can live in Confluence, Notion, Google Drive, a SharePoint site or a Git repository. The tool matters less than three properties:

1. **One entry point.** Anyone new to the product starts at the index.
2. **Visible freshness.** Every artifact shows its owner and last-reviewed date. Stale artifacts are flagged, not hidden.
3. **Readable by machines.** In 2026 this one matters more than it used to. If your artifacts are in formats an AI harness can read through a connector (pages, docs, Markdown files), the harness can answer questions across the whole 360. If they're screenshots of slides, it can't.

## The operating cadence

Artifacts don't keep themselves true. People do, on a rhythm. The operating cadence is the calendar that says which artifact gets reviewed when, by whom, and what decision the review produces.

The cadence below is this book's synthesis, and it borrows from several well-tested practices. Amazon's weekly business review (WBR), as Colin Bryar and Bill Carr describe it in *Working Backwards*, has metric owners walk a fixed set of metrics every week and explain the variances. The quarterly business review (QBR) is standard in enterprise software. Annual planning cycles like Amazon's OP1 and OP2 have teams write next year's plan as a narrative in the fall and revise it into the plan of record after the holiday quarter. Melissa Perri and Denise Tilles, in *Product Operations*, make the same case from the operations side: one of their three pillars of product ops is process and governance, alongside business and data insights and customer and market insights. Without dependable rituals for looking at data, customers and plans, decisions get made on anecdote.

| Cadence | Ritual | Artifacts reviewed | Decision it produces |
|---|---|---|---|
| **Weekly** | Product team sync; metrics review | Dashboard, decision log, risk register, discovery log | What we adjust this week; which risks escalate |
| **Biweekly** | Sprint review and planning (with engineering) | Backlog, release plan, active PRDs | What ships next; what gets cut |
| **Monthly** | Product review with leadership; roadmap refresh | Roadmap, OKR progress, competitive changes, customer insight summary | Roadmap changes; asks for help |
| **Quarterly** | Business review (QBR); OKR reset; portfolio review | Business model, OKRs, competitive landscape, stakeholder map, lifecycle stage | Next quarter's bets; staffing; pricing changes |
| **Annually** | Strategy refresh and planning | Vision, strategy one-pager, personas, positioning, business case, lifecycle assessment | Where to play, how to win, what to stop |
| **Per event** | Launch readiness; go/no-go; post-launch review; sunset gate | Launch plan, PRFAQ, readiness checklist, sunset plan | Ship or hold; continue, pivot or retire |

Two rules make the cadence work. First, **every ritual produces a decision or it gets cancelled**. A weekly metrics review that never changes anything is theater. Second, **decisions get written down**, in a decision log with the date, the decision, the options considered, who decided and why. Six months later, when someone asks why you chose usage pricing, the log answers in thirty seconds. Chapter 29 covers decision logs and DACI (the Driver, Approver, Contributors, Informed model popularized by Atlassian) in detail.

:::leader For product leaders: nesting the 360
In a portfolio, Product 360s nest. A group PM or director keeps a portfolio-level 360 whose strategy and business dimensions summarize the products beneath it, and whose operate dimension runs the portfolio review. Each product keeps its own 360. Feature-area PMs often keep a light 360 (customer, build, measure) that inherits strategy from the product level. The rule: a lower-level 360 should never contradict a higher one without a recorded decision.
:::

## How to build your Product 360

Here is the method in six steps. The Capstone expands it into a full 30/60/90-day plan with prompts; this is the outline.

1. **Scope the surface area.** Write down, in one paragraph, exactly what you own: which product or products, which customers, which teams, which revenue. Scope disputes are the most common hidden cause of a broken 360. If two PMs both think they own pricing, neither of their 360s is true.
2. **Inventory what exists.** Gather every document, deck, dashboard and ticket that describes the product. Don't judge it yet; just collect it. An AI harness with connectors into your doc tools makes this hours of work instead of weeks.
3. **Map it to the nine dimensions.** Sort the inventory by dimension and kind (durable, living, event). Mark each item as current, stale or contradicted. Gaps become obvious immediately.
4. **Build the spine.** Create or repair the twelve spine artifacts, in order, starting with the Product 360 index. Reuse what's good; rewrite what's stale. Each artifact gets an owner and a review date.
5. **Set the cadence.** Put the rituals on the calendar, with the artifacts each one reviews. Start lighter than you think you need. A weekly metrics review and a monthly roadmap review beat an ambitious calendar nobody attends.
6. **Publish and keep it alive.** Share the index with your team, your manager and your key stakeholders. Tell them it's the source of truth. Then make it true: when a decision happens, it goes in the log; when a strategy changes, the one-pager changes first.

## The AI lens

### Your 360 is your AI context

The single biggest change AI brings to the PM job in 2026 is that a well-kept Product 360 becomes reusable context. When your artifacts are current and readable, you can hand them to a harness and ask questions that used to take a week of meetings:

- "Does the Q3 roadmap still trace back to the strategy one-pager? List anything on the roadmap that doesn't."
- "Summarize every decision in the log that touches pricing, and flag any that contradict the current packaging doc."
- "Draft a first version of the QBR narrative from the dashboard export, the OKR tracker and this month's customer insight summary."

None of those prompts works on a 360 that lives in people's heads. All of them work on a 360 that lives in a connected set of pages. That's a strong practical argument for building the 360 even if you never have time to read every artifact yourself: the harness will.

:::ai What changes when the product is AI-powered
Add four artifacts to the spine for any AI-powered product: an **eval plan** (how quality is measured, and the current scores), an **AI cost model** (cost per task or per user, and its trend), a **model and vendor register** (which models are in use, their versions and deprecation dates), and an **AI risk assessment** (failure modes, guardrails, and regulatory obligations). Chapter 31 has templates for all four. They belong in the Build, Business, Operate and Lifecycle dimensions respectively, which is another way of seeing that AI changes every dimension.
:::

### What not to hand to AI

The harness drafts, checks and summarizes. It doesn't decide, and it doesn't own. Three guardrails:

- **Data boundaries.** Customer data, unreleased financials and confidential strategy go only into tools your company has approved for that data. Check before you connect.
- **Decisions stay human.** An AI can lay out pricing options with their tradeoffs. You and your approvers choose. The decision log records who decided, and it shouldn't say "the model."
- **Verify the numbers.** AI-generated summaries of metrics are fast and frequently wrong in small ways: a misread column, a wrong time window, a silently dropped segment. Every number that goes into a durable artifact or an executive review gets checked against the source. Chapter 19 covers how.

## The Beacon case: a new Principal PM's first inventory

:::example Day one on Beacon
You've just joined Northlight Systems as Principal PM for Beacon, the AI agent platform for IT operations. Your manager, the VP of Product for the Operations portfolio, gives you two weeks to "get your arms around it" before the quarterly business review.
:::

You start with step 1 and write the scope paragraph: *"Beacon: the standalone AI incident-management product, including Beacon Classic (legacy correlation) and Beacon Agents (diagnosis and supervised remediation). Customers: about 420 enterprise accounts plus the MSP partner channel. Teams: 3 PMs, 1 designer, 5 engineering teams, 2 applied AI engineers, a PMM and shared product ops. Revenue: about $48M ARR."* You send it to your manager and to the group PM for Northlight Observe, because you suspect the boundary between Beacon and Observe is fuzzy. It is: Observe's PM believes alert correlation belongs to Observe. That disagreement goes into the decision log as the first open item.

Step 2, the inventory, turns up 140 documents. Sorted against the nine dimensions, the picture looks like this:

| Dimension | What exists | State |
|---|---|---|
| Customer | Three personas from 2024, all users, no buyer or security persona | Stale; missing Marcus (economic buyer) and Sam (security reviewer) |
| Strategy | A 2025 strategy deck; no one-pager; vision statement in an all-hands slide | Stale; doesn't mention agents |
| Business | Pricing page; a finance model owned by FP&A | Contradicted: gross margin dropped from 81% to 72% and the strategy deck still assumes 80% |
| Build | Jira roadmap view; 23 PRDs, 9 for features that shipped differently | Living but noisy |
| Measure | A dashboard with 40 charts; no North Star | No agreed definition of success |
| Go-to-market | Positioning from the Classic era; no launch tiering | Stale; Beacon Agents launch at Northlight Live is in four months |
| Operate | Weekly team sync; no decision log; risk register abandoned in 2025 | Missing |
| Lifecycle | Nothing on Beacon Classic's end of life | Missing, and customers are asking |
| Leadership | No stakeholder map; Observe boundary disputed | Missing |

The gaps rank themselves. Gross margin and the missing North Star are business-critical and visible to executives within weeks. The Beacon Agents launch has a fixed date. Beacon Classic's end of life is creating customer escalations. So your first spine artifacts after the index are the business model summary, the North Star and metric tree, the launch plan, and a lifecycle assessment for Classic. Personas and strategy follow, but they can wait a month; the four urgent artifacts can't.

By the QBR you have a Product 360 index with nine dimensions, twelve linked artifacts (four new, five repaired, three still marked "stale, owner assigned"), a decision log with six entries and a cadence on the calendar. It isn't complete. It's true, and everyone can see which parts aren't done yet. That's the state you're aiming for.

## Product 360 artifacts

```template id="product-360-index" title="Product 360 index"
# [Product name] · Product 360

**Owner:** [Name, title]   **Last reviewed:** [YYYY-MM-DD]   **Lifecycle stage:** [Introduce / Grow / Mature / Decline / Retire]

## Scope
[One paragraph: which products, customers, teams and revenue this 360 covers. Name what is explicitly out of scope and who owns it.]

## The 360 at a glance
| Dimension | Key question | Artifact (link) | Owner | Kind | Last reviewed | State |
|---|---|---|---|---|---|---|
| Customer | Who is this for, and what job? | [Personas and problem hypothesis] | | Durable | | Current / Stale / Missing |
| Strategy | Where we play, how we win | [Vision and strategy one-pager] | | Durable | | |
| Strategy | Who we compete with | [Competitive landscape] | | Living (Q) | | |
| Business | How it makes money | [Business model and unit economics] | | Living (Q) | | |
| Build | What's next | [Outcome roadmap] | | Living (M) | | |
| Measure | How we know it works | [North Star, metric tree, dashboard] | | Living (W) | | |
| Measure | What we committed to | [OKRs] | | Living (Q) | | |
| Go-to-market | How it reaches customers | [Positioning and messaging] | | Durable | | |
| Operate | How we run it | [Operating cadence, decision log, risk register] | | Living (W) | | |
| Lifecycle | Where it is in its life | [Lifecycle stage assessment] | | Durable | | |
| Leadership | Who must be aligned | [Stakeholder map and DACI] | | Living (Q) | | |
| AI (if applicable) | Quality, cost, models, risk | [Eval plan, AI cost model, model register, AI risk assessment] | | Living (M) | | |

## Current priorities
1. [The one to three things that matter most this quarter, each linked to its artifact]

## Open decisions
[Link to the decision log, filtered to open items]

## Active events
[Links to in-flight PRDs, launch plans, business cases, sunset plans]

## Key contacts
[Engineering lead, design lead, PMM, product ops, sales lead, support lead, finance partner]
```

```template id="artifact-inventory" title="Artifact inventory and gap assessment"
# Artifact inventory · [Product] · [Date]

## Scope statement
[Paste the one-paragraph scope.]

## Inventory
| # | Document | Link | Dimension | Kind (durable/living/event) | Last updated | Owner | State (current/stale/contradicted) | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |

## Gaps by dimension
| Dimension | Spine artifact | Exists? | State | Business risk if missing (H/M/L) | Deadline driver | Priority |
|---|---|---|---|---|---|---|
| Customer | Problem hypothesis and personas | | | | | |
| Strategy | Vision and strategy one-pager | | | | | |
| Strategy | Competitive landscape | | | | | |
| Business | Business model and unit economics | | | | | |
| Build | Outcome roadmap | | | | | |
| Measure | North Star and metric tree | | | | | |
| Measure | OKRs | | | | | |
| Go-to-market | Positioning and messaging | | | | | |
| Operate | Cadence and decision log | | | | | |
| Lifecycle | Lifecycle stage assessment | | | | | |
| Leadership | Stakeholder map and DACI | | | | | |

## Contradictions found
[Each pair of artifacts that disagree, what they disagree on, and who needs to resolve it.]

## Build order
1. [Artifact] because [deadline or risk]
```

```template id="operating-cadence" title="Product operating cadence"
# Operating cadence · [Product] · [Quarter]

| Cadence | Ritual | Day and time | Attendees | Artifacts reviewed | Output | Owner |
|---|---|---|---|---|---|---|
| Weekly | Metrics review | | PM, eng lead, design, analyst | Dashboard, risk register | Adjustments, escalations | |
| Weekly | Team sync | | Product team | Decision log, discovery log | Decisions logged | |
| Biweekly | Sprint review and planning | | Product team | Backlog, release plan | Sprint commitment | |
| Monthly | Product review | | Leadership, PM, eng, design, PMM | Roadmap, OKRs, competitive changes, insight summary | Roadmap changes, asks | |
| Quarterly | Business review | | Leadership, finance, sales, CS | Business model, OKRs, lifecycle stage | Bets, staffing, pricing | |
| Annually | Strategy refresh | | Leadership | All durable artifacts | Strategy for the year | |
| Per event | Launch go/no-go | | Launch team | Launch plan, readiness checklist | Ship or hold | |

## Rules
- Every ritual produces a decision or is cancelled after two meetings without one.
- Decisions are written in the decision log within 24 hours.
- Each artifact shows its owner and last-reviewed date. Anything past its review date is marked stale on the 360 index.
```

## Prompts

```prompt title="Inventory and classify existing product documents"
Goal: Turn a pile of existing documents into a first Product 360 inventory.
Paste in (or connect the harness to): the documents, decks, pages and dashboards you've gathered for [product]. Use only tools approved for this data.

You are helping a Principal PM build a Product 360 for [product]. The Product 360 has nine dimensions: Customer, Strategy, Business, Build, Measure, Go-to-market, Operate, Lifecycle, Leadership. Artifacts are durable (change yearly), living (change on a weekly to quarterly cadence) or event (created for one decision or moment).

For every document provided:
1. Give its title, link or file name, and last-updated date if visible.
2. Assign one primary dimension and the artifact kind.
3. Summarize in one sentence what question it answers.
4. Mark it current, stale (older than its natural cadence) or contradicted (conflicts with another document), and say which document it conflicts with.

Then produce:
- A table of the twelve spine artifacts (Product 360 index, problem hypothesis and personas, vision and strategy one-pager, competitive landscape, business model and unit economics, outcome roadmap, North Star and metric tree, OKRs, positioning and messaging, operating cadence and decision log, lifecycle stage assessment, stakeholder map and DACI) showing which exist, their state and the best existing source for each.
- A list of every contradiction you found, quoting the conflicting statements.

Do not invent documents or fill gaps with guesses. If you can't tell a document's date or state, say so.

Check the output: open three documents the model marked "current" and two it marked "contradicted" and confirm it read them correctly. Spot-check that no spine artifact was marked "exists" on the strength of a passing mention.
```

```prompt title="Draft the Product 360 index from the inventory"
Goal: Produce the first version of the Product 360 index page.
Paste in: the scope paragraph, the completed artifact inventory and the list of open decisions.

Using the inventory below, draft a Product 360 index for [product] using this structure: scope; a table of the nine dimensions with key question, linked artifact, owner, kind, last reviewed and state; current priorities (no more than three); open decisions; active events; key contacts.

Rules:
- Use only artifacts and facts that appear in the inventory. Where an artifact is missing, write "Missing" and leave the owner blank for me to fill.
- Rank current priorities by business risk and deadline, and give a one-line reason for each.
- Keep the page under 600 words. It's a map, not a report.

[inventory]

Check the output: every link should resolve to a real document, every "current" label should match the inventory, and the priorities should be ones you'd defend to your manager.
```

```prompt title="Design an operating cadence that fits the team"
Goal: Get a realistic first cadence instead of an aspirational one.
Paste in: team size and roles, existing recurring meetings, the planning calendar (QBR dates, annual planning), and upcoming events such as launches.

I own [product]. Here's my team and the meetings that already exist: [details]. Propose an operating cadence using the fewest new meetings possible. Reuse existing meetings where they can absorb a ritual. For each ritual give: frequency, attendees, the artifacts reviewed, the decision it produces and a 1-line agenda. Flag any ritual that has no clear decision output, and recommend cutting it. Finish with the total hours per week the cadence costs the PM and the engineering lead.

Check the output: count the hours yourself. If the PM's ritual load exceeds about 20% of the week, ask for a lighter version.
```

```prompt title="Audit the 360 for contradictions"
Goal: Find places where your artifacts disagree before an executive does.
Paste in: your current strategy one-pager, roadmap, OKRs, business model summary and positioning doc (or point the harness to them).

Compare these artifacts for [product] and list every contradiction or unsupported link. Specifically:
1. Roadmap items that don't trace to a strategic choice in the one-pager.
2. OKRs that measure something the strategy doesn't prioritize, or priorities with no OKR.
3. Positioning claims the roadmap doesn't support.
4. Business-model assumptions (margin, price, growth) that conflict with the latest numbers.
For each, quote both sources, explain the conflict in one sentence and suggest which artifact is more likely to be wrong and why.

Check the output: for each contradiction, decide yourself which artifact to change, and log the decision.
```

## Anti-patterns

:::warn The document museum
A wiki full of beautifully formatted pages, none touched since the launch that justified them. The tell: no artifact shows an owner or a last-reviewed date. Fix it by adding freshness to the index and archiving anything nobody claims.
:::

:::warn The 360 in your head
Everything is current, and all of it lives in the PM's memory. The product works until the PM goes on vacation, changes teams or gets asked the same question by two executives on the same day. If it isn't written, it isn't part of the 360.
:::

:::warn Everything is living
Strategy, personas and positioning get revised every sprint because a customer said something interesting. Durable artifacts are supposed to be stable. Capture the signal in the discovery log, and change durable artifacts at the strategy refresh, or with an explicit decision.
:::

:::warn The AI-generated 360 nobody checked
A harness can produce a complete-looking 360 in an afternoon. If you didn't verify the facts and make the choices, it's a plausible fiction with your name on it. Use AI to draft and to check; own every claim that ships.
:::

:::warn Scope fog
Two PMs each believe they own the same capability. Both 360s look complete, and both are wrong. Write the scope paragraph first and get the boundary agreed before you build anything else.
:::

## Checklist

- [ ] I've written a one-paragraph scope for my product, and my manager and neighboring PMs agree with it.
- [ ] Every existing document is inventoried and mapped to a dimension and artifact kind.
- [ ] The Product 360 index exists, links every spine artifact and shows owners and last-reviewed dates.
- [ ] All twelve spine artifacts exist, or are explicitly marked missing with an owner and date.
- [ ] For an AI-powered product, the eval plan, AI cost model, model register and AI risk assessment are on the index.
- [ ] Contradictions between artifacts are listed, and each has a decision owner.
- [ ] The operating cadence is on the calendar, and every ritual names the decision it produces.
- [ ] A decision log exists and has entries from the last two weeks.
- [ ] The index is shared with my team, my manager and key stakeholders as the source of truth.
- [ ] The 360 lives somewhere an approved AI harness can read it.

## Key takeaways

- A Product 360 is the set of artifacts and rituals that keep a product legible: nine dimensions, each answering a question someone will eventually ask you.
- The dimensions group into Direction (customer, strategy, business), Delivery (build, measure, go-to-market) and Durability (operate, lifecycle, leadership). Most PM training skips the third group.
- Artifacts come in three kinds. Durable ones change yearly, living ones change on a cadence and event ones serve a single decision. Treating them all alike produces either a stale strategy or no strategy.
- Start with a spine of twelve artifacts and the Product 360 index. Build everything else when a question demands it.
- The operating cadence keeps the 360 true. Every ritual produces a decision, and every decision gets logged.
- AI isn't a tenth dimension. It changes all nine, both in what you build and in how you maintain the 360, and a well-kept 360 is the best context you can give a harness.
