<p class="lead">Every product question in Part IV ends with "and what evidence would answer it?" This chapter is the map of where that evidence lives: ten sources of product data, what each can and can't tell you, who owns it and where it misleads. It then sets out the twelve reports a product leader should own, the questions each must answer, and the governance that keeps everyone counting the same thing.</p>

## Why this matters

Chapter 17 taught you to start from the decision and work back to the question. The next problem is practical. In an enterprise company the answer to almost any interesting question is spread across five systems owned by five teams, each with its own definition of "customer," its own refresh schedule and its own blind spots. Product telemetry knows what users did but not why. The CRM knows what the rep typed into the loss-reason field but not what the buyer actually thought. Billing knows what the customer paid but not what value they got. Support knows who complained but not who quietly left.

A Principal PM doesn't need to be the person who pulls these numbers. In 2026 an AI harness with connectors does most of the pulling. What the PM does need is three things the harness can't supply on its own:

1. **A map.** Which source answers which question, at what grain, with what known traps. Without the map you ask the wrong system and get a confident wrong answer.
2. **A report set.** A small, stable set of recurring reports, each built around named questions, a cadence and an audience. Without it, every leadership meeting starts with an argument about whose number is right.
3. **Definitions.** One written definition per metric, with an owner and a version. Without definitions, two honest teams report different numbers for the same quarter and neither is wrong.

AI raises the stakes. A harness pointed at raw enterprise tables will happily write a query, run it and present the result in a clean table. Whether that number means what you think depends on the map, the definitions and the governed layer they sit in.

Chapter 05 covers instrumentation, funnels and experiments, and Chapter 09 covers the analysis of retention, health scores and sentiment. This chapter doesn't repeat those methods. Its job is the landscape, the recurring reports and the governance that ties them together. Chapter 19 then shows how to collect, permission and query all of it through the harness.

## The product data landscape

### Ten sources, one map

Most enterprise product questions draw on ten sources, each sharp on some questions and blind on others. The table below is this book's synthesis of what each source can and can't tell you. Use it as the starting row set for your own data source inventory.

| Source | Can tell you | Can't tell you | Usual owner | Traps to check |
|---|---|---|---|---|
| **Product telemetry and analytics** | Behavior, adoption, funnels and time to value, by user and by account | Why users did it, what they intended, or work done in other tools | Product analytics or data engineering; the PM owns the tracking plan | Instrumentation gaps after releases; test, bot and internal tenants inflating counts; renamed events; user and account identity mismatch; sampling |
| **CRM** (accounts, opportunities, contacts) | Pipeline, win and loss, segment, deal stage, stated loss reasons | The real reason a deal was lost; anything about product usage | Sales operations or RevOps | Stage inflation near quarter end; a single "primary product" field on multi-product deals; duplicate accounts; loss reasons picked from a dropdown in a hurry |
| **Billing and subscription** | ARR, expansion, contraction, churn, discounts, usage charges | Why customers expand or leave; the value they got | Finance or billing operations | Bookings, billings and revenue are three different numbers; multi-year prepayment; credits and true-ups; a parent and child account hierarchy that differs from the CRM's |
| **Support tickets** | Pain themes, defect trends, time to resolve, which accounts struggle | How common a problem is among customers who never file a ticket; how severe it felt | Support operations | Category taxonomies drift; agents pick "other"; one incident produces many duplicate tickets |
| **Surveys and NPS** | Stated sentiment, relationship risk, verbatim reasons | Behavior; the views of people who didn't respond | Customer experience or marketing | Who was surveyed (user or economic buyer); timing just after an outage; a score reported without the follow-up "why" |
| **Sales and customer calls** (recordings and transcripts) | Competitor mentions, objections, the customer's own language, requests in context | How often something happens across the base, since you only see the calls that were recorded | Sales enablement or RevOps | Recency and vividness bias; consent and retention rules |
| **Product reviews and communities** (review sites, marketplace listings, forums) | Competitive perception, switching reasons, how buyers compare you | Representativeness | Product marketing | Vendor-solicited reviews; old reviews describing old versions |
| **Market and competitive data** (analyst reports, competitor pricing pages, release notes, job postings) | Direction, positioning, competitor moves | Precise share in a niche | Product marketing or strategy | Analyst definitions of the market differ; stale snapshots |
| **Finance and FP&A** (plan, forecast, cost of goods sold, margin by product) | Margin, plan against actual, unit economics | Feature-level cost, unless someone wrote the allocation rules | FP&A | Allocation methods; plan numbers mistaken for actuals; fiscal and calendar periods mixed |
| **AI traces and evals** | What the model and agent actually did on each request, quality against a test set, failure modes, cost per request | Whether the customer got value, unless joined to outcome data | Applied AI or platform engineering; the PM co-owns the eval criteria | Customer content and personal data inside traces; generic judge scores; offline eval pass rates mistaken for production quality |

Three patterns run through the table. Behavioral sources (telemetry, traces) tell you *what* and never *why*. Voice-of-customer sources (support, surveys, calls) tell you *why* but are biased toward whoever chose to speak. Commercial sources (CRM, billing, finance) tell you *what it was worth* but are entered by people with quotas and closing deadlines. Market sources (reviews, analyst and competitive data) sit outside your customer base and tell you how buyers you haven't won see you. A good answer usually triangulates across at least two of these families.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 380" role="img" aria-label="Ten product data sources in four families flow through a governed layer into weekly, monthly and quarterly reports">
  <defs><marker id="ar18" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="var(--muted)"/></marker></defs>
  <rect x="20" y="20" width="185" height="82" rx="10" class="box"/>
  <text x="34" y="42" class="t">Behavior</text>
  <text x="34" y="62" class="s">Product telemetry</text>
  <text x="34" y="78" class="s">AI traces and evals</text>
  <rect x="20" y="108" width="185" height="82" rx="10" class="box"/>
  <text x="34" y="130" class="t">Commercial</text>
  <text x="34" y="150" class="s">CRM</text>
  <text x="34" y="166" class="s">Billing and subscription</text>
  <text x="34" y="182" class="s">Finance and FP&amp;A</text>
  <rect x="20" y="196" width="185" height="82" rx="10" class="box"/>
  <text x="34" y="218" class="t">Voice of customer</text>
  <text x="34" y="238" class="s">Support tickets</text>
  <text x="34" y="254" class="s">Surveys and NPS</text>
  <text x="34" y="270" class="s">Sales and customer calls</text>
  <rect x="20" y="284" width="185" height="82" rx="10" class="box"/>
  <text x="34" y="306" class="t">Market</text>
  <text x="34" y="326" class="s">Product reviews</text>
  <text x="34" y="342" class="s">Market and competitive data</text>
  <rect x="245" y="70" width="160" height="250" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".7"/>
  <text x="325" y="100" text-anchor="middle" class="t" style="fill:var(--a1)">Governed layer</text>
  <text x="325" y="134" text-anchor="middle" class="s">Account ID map</text>
  <text x="325" y="160" text-anchor="middle" class="s">Metric dictionary</text>
  <text x="325" y="186" text-anchor="middle" class="s">Semantic layer</text>
  <text x="325" y="212" text-anchor="middle" class="s">Five-question trust check</text>
  <text x="325" y="262" text-anchor="middle" class="s">Owners, freshness,</text>
  <text x="325" y="278" text-anchor="middle" class="s">definitions, versions</text>
  <line x1="205" y1="61" x2="243" y2="130" class="ln" marker-end="url(#ar18)"/>
  <line x1="205" y1="149" x2="243" y2="170" class="ln" marker-end="url(#ar18)"/>
  <line x1="205" y1="237" x2="243" y2="220" class="ln" marker-end="url(#ar18)"/>
  <line x1="205" y1="325" x2="243" y2="262" class="ln" marker-end="url(#ar18)"/>
  <rect x="445" y="20" width="175" height="120" rx="10" class="box"/>
  <text x="459" y="42" class="t" style="fill:var(--a2)">Weekly</text>
  <text x="459" y="62" class="s">Weekly metrics review</text>
  <text x="459" y="78" class="s">Product health</text>
  <text x="459" y="94" class="s">Customer health list</text>
  <text x="459" y="110" class="s">Support trends digest</text>
  <text x="459" y="126" class="s">AI quality and cost</text>
  <rect x="445" y="150" width="175" height="120" rx="10" class="box"/>
  <text x="459" y="172" class="t" style="fill:var(--a2)">Monthly</text>
  <text x="459" y="192" class="s">Funnel and activation</text>
  <text x="459" y="208" class="s">Feature adoption</text>
  <text x="459" y="224" class="s">Retention and NRR</text>
  <text x="459" y="240" class="s">Pipeline influence</text>
  <text x="459" y="256" class="s">Pricing and discount</text>
  <rect x="445" y="280" width="175" height="86" rx="10" class="box"/>
  <text x="459" y="302" class="t" style="fill:var(--a3)">Quarterly</text>
  <text x="459" y="322" class="s">QBR pack</text>
  <text x="459" y="338" class="s">Portfolio review</text>
  <line x1="405" y1="150" x2="443" y2="80" class="ln" marker-end="url(#ar18)"/>
  <line x1="405" y1="195" x2="443" y2="210" class="ln" marker-end="url(#ar18)"/>
  <line x1="405" y1="240" x2="443" y2="322" class="ln" marker-end="url(#ar18)"/>
</svg>
<figcaption>The product data landscape. Ten sources in four families feed a governed layer (account map, metric dictionary, semantic layer and trust check), and only then the report set. Reports that read raw sources directly are where conflicting numbers come from.</figcaption>
</figure>

### The join key is the PM's leverage

In consumer products most questions live inside one source. In B2B they almost never do. "Which accounts are adopting Diagnose, what are they paying, and are they filing more tickets than before?" needs telemetry, billing and support joined at the account level. That join is where enterprise analysis quietly breaks.

Each system keeps its own idea of an account. The CRM has a parent company with subsidiaries. Billing has bill-to entities that follow the contract, not the org chart. Telemetry has tenants and environments. Support has whatever the customer typed into the email domain field. A partner who manages sixty customers might appear as one account in the CRM and sixty tenants in telemetry. If nobody owns the mapping between these, every cross-source report is wrong in a way nobody can see.

Make the account mapping an explicit part of your inventory: which identifier each source uses, how they map to each other, and where the mapping is known to break. It's dull work, and it's one of the most valuable fixes a product leader can ask a data team for, because every cross-source report in this chapter depends on it.

### Every source is a data product

Zhamak Dehghani's data mesh principles, published in 2020, are mostly about how to organize data platforms, and you don't need the architecture. One idea is worth taking whole: **treat data as a product**. Dehghani argues that each domain should own its data and serve it to others the way a product team serves customers, with a named owner and with qualities she lists as discoverable, understandable, trustworthy and secure, among others.

For a PM, this reframes the relationship with every row in the table above. You are a customer of the CRM data, the billing data and the support data. Like any customer, you can write requirements: the freshness you need, the definitions you rely on, the join key you need populated. And like any product, each source should have an owner you can name. "The data team" doesn't count. A source without a named owner is a source nobody will fix when it breaks.

### Before you trust a number: the five-question check

Barr Moses of Monte Carlo uses the term **data downtime** for periods when data is partial, erroneous, missing or otherwise inaccurate. She describes five pillars of data health. Each converts naturally into a question a PM (or the PM's harness) can ask before acting on a number:

1. **Freshness.** When was this data last updated, and is that later than the decision needs?
2. **Quality.** Are null rates, duplicate rates or out-of-range values unusual this period?
3. **Volume.** Did the row or event count jump or drop outside its normal range?
4. **Schema.** Did any field, event name or definition change recently?
5. **Lineage.** What upstream sources feed this number, and did any of them have a problem?

A sudden drop in weekly active users can be a broken event after a release as easily as a real change in behavior. Ask the five questions first. They take minutes with a harness, and they can save the meeting where an executive reallocates headcount because of a tracking bug.

### Every report is a proxy

Jeff Bezos, in his 2016 letter to Amazon shareholders, warned against managing to proxies. As companies grow, he argued, the process becomes the thing being managed, and surveys and market research start to stand in for customers. His short version: "The process is not the thing." Every report in this chapter is a proxy for something you can't observe directly: customer value, product quality, the health of a relationship.

The related warning is usually credited to the economist Charles Goodhart and generalized by the anthropologist Marilyn Strathern: when a measure becomes a target, people optimize the measure and it stops telling you what it used to. In product data the risk is concrete. If the team is rewarded on "diagnosis acceptance rate," a default that pre-selects "accept" will raise it without anyone being better served.

Two habits keep proxies honest. Pair every important metric with a small, regular dose of the thing it stands for: a handful of ticket verbatims, a call excerpt, a trace someone actually read. And watch the inputs that are easiest to game, especially once they appear in a goal.

## The reports that matter

### Inputs first: the weekly business review

The most fully described model for a recurring metrics review is Amazon's Weekly Business Review, which Cedric Chin of Commoncog has written up in detail. Chin describes it as a process-control tool for uncovering the causal structure of the business, and it answers three questions every week: what did customers experience last week, how did the business do, and are we on track against targets?

Four features of the format, as Chin describes it, transfer directly to a B2B product team:

- **Causal order.** The deck starts with **controllable input metrics** (the levers teams can move this week), then the **output metrics** they're meant to drive, then the financials. Teams report on outputs but work on inputs.
- **Exception-driven discussion.** Every metric is shown, but owners speak only to exceptional variation or a missed target. Normal weeks get "nothing to see here." If an owner doesn't know the cause, they say so, and a follow-up gets logged. Improvised explanations aren't allowed.
- **A fixed visual format.** Chin describes the "6-12 graph": the trailing six weeks on the left, the trailing twelve months on the right, last year as a faded line and targets marked. Because every chart looks the same, readers spot anomalies quickly.
- **A living metric set.** Metrics are added and dropped as their predictive power changes.

Chin reports that Amazon's deck runs to 400 to 500 metrics, and that his own company's version has 47. A product team needs far fewer. This book's recommendation for a B2B product WBR is 15 to 30 metrics, each with a named owner. One caveat matters in enterprise: with hundreds rather than millions of customers, weekly percentages are noisy. Use trailing four-week views and show the account list behind any move, not just the percentage.

### The twelve-report set

The WBR is one report. A product leader in an enterprise business owns, or co-owns, a set of about a dozen. The set below is this book's framework. Each report is defined by the questions it must answer, not by its charts, and each feeds a named decision.

| Report | Questions it must answer | Cadence | Audience |
|---|---|---|---|
| **1. Weekly metrics review (WBR)** | What changed? Is it exceptional? Why? What are we doing about it? | Weekly | Product leadership, engineering leads, product marketing, customer success lead |
| **2. Product health** | Is the product working for customers: reliability, latency, error rates, defect backlog? | Daily view, weekly review | Product and engineering |
| **3. Funnel and activation** | Where do new accounts stall between signature and first value? How long does first value take, by segment? | Weekly view, monthly deep dive | PM, onboarding, customer success |
| **4. Retention and NRR** | Which cohorts and segments expand, contract or churn? How do gross and net retention compare? What are the leading signals? | Monthly, quarterly | Product leadership, finance, customer success |
| **5. Feature adoption** | Which features are used, by whom, how broadly and how deeply? Which deserve more investment and which should be retired? | Monthly, plus 30, 60 and 90 days after each launch | PMs, design, product marketing |
| **6. Customer health** | Which accounts are at risk or ready to expand, and why? | Weekly list, monthly trend | Customer success, account teams, PM |
| **7. Pipeline influence** | Which capabilities show up in won and lost deals, in which segments? Where do product gaps block deals? | Monthly, quarterly | Product leadership, sales leadership |
| **8. Pricing and discount** | What do customers actually pay against list? Where is discounting deepest? Which packages sell? Does usage fit price? | Monthly, quarterly | Product, pricing, finance, sales operations |
| **9. Support trends** | What are the top themes by volume and by ARR affected? What's new? Defect or how-to? | Weekly digest, monthly review | PM, support, engineering |
| **10. AI quality and cost** | Is the AI getting better or worse? What does each successful outcome cost? | Weekly, plus a release gate on every model or prompt change | PM, applied AI, finance |
| **11. QBR pack** | Internal: are our bets and goals on track? Customer-facing: what value did this customer get? | Quarterly | Executives; or the customer's buying group |
| **12. Portfolio review** | Across product lines, where is investment against return? What do we grow, sustain, harvest or retire? | Quarterly or twice a year | VP of Product, CFO, CEO staff |

Treat the questions column as the report's specification. A report that can't answer its questions needs rebuilding or retiring, however good its charts look.

### Notes on the reports that go wrong most often

**Feature adoption.** Pendo's 2019 Feature Adoption Report, based on usage data from 615 of its subscriptions, found that 80% of features in the average product were rarely or never used. It's vendor data from one platform and one year, so treat it as a warning rather than a law. The warning is still worth heeding: an adoption report that lists only the features people use hides the far larger set nobody uses. Show breadth (how many accounts touched it) and depth (how often, by how many users per account), and show the bottom of the list.

**Retention and NRR.** Net revenue retention looks like one number and is really a stack of choices. SaaS Capital's 2025 benchmark defines it from a December-to-December snapshot of recurring revenue, counts upsell, cross-sell *and price increases*, and pairs it with gross revenue retention, which excludes expansion and so can't exceed 100%. Another company might use trailing twelve months, or exclude price increases. Both are legitimate; mixing them isn't. Chapter 09 covers the analysis. This report's job is to state which definition it uses, every time.

**Customer health.** Gainsight's guidance on health scores lists the usual inputs: usage against entitlements, feature adoption, sentiment, engagement, relationships and customer outcomes. Its most useful advice is the check: if churn keeps surprising you quarter after quarter, rework the score. A health report should show, at least quarterly, how well last quarter's scores predicted this quarter's renewals.

**Pipeline influence.** This is the report most easily inflated. "Influenced pipeline" usually means a capability was tagged on an opportunity or mentioned on a call. That's correlation, not cause. Present it as evidence of where product shows up in deals, never as revenue the product "drove," and always show lost deals alongside won ones. The most valuable rows are the gaps: capabilities that appear repeatedly in losses.

**Pricing and discount.** Michael Marn and Robert Rosiello, writing in Harvard Business Review in 1992, popularized the idea of a price waterfall: the list price is eroded step by step by discounts, rebates, payment terms and other concessions before it becomes the price the company actually keeps. The report applies the same idea to software: list, then negotiated discount, then credits and free months, then the realized price per unit. Chapter 15 covers pricing strategy; this report shows where the leakage is.

**Support trends.** Ranking themes by ticket count lets one noisy account set your priorities. Rank them twice: by volume and by the ARR of the accounts affected, and show which themes are new this period. Separate defects from how-to questions, since the first goes to engineering and the second to documentation and onboarding. Because the "other" category grows whenever the taxonomy drifts, ask the harness to read a sample of "other" tickets each month and propose new themes.

**AI quality and cost.** This report is new for most teams and is covered in the AI lens below.

**QBR pack.** "QBR" means two things. The **internal QBR** is a quarterly product review for executives: strategy progress, goals, output metrics, bets placed and killed. The **customer QBR** is a per-account review with the customer; Gainsight's guide lists its usual sections, from an executive summary and the KPIs that matter to the customer through ROI, progress against prior goals, health, and actions with owners and dates. The product leader owns the first and supplies the definitions for the second, so every account team tells the value story the same way. Chapter 29 covers the forums these packs feed.

**Portfolio review.** This report compares product lines that measure themselves differently, so it only works when every line reports the same few metrics under the same definitions: ARR and growth, NRR, gross margin, cost to serve and the investment each line consumes. Show each line's trend over at least four quarters beside its strategic role, because a line with low growth may be doing its job if its role is to protect the base. The decision it feeds is where to grow, sustain, harvest or retire, and Chapter 30 covers what happens after a retire decision.

:::onramp If you own no reports yet
Start with two: the weekly metrics review and the support trends digest. The first forces you to choose and define your metrics. The second keeps you in contact with what customers are actually struggling with. Add the rest as decisions demand them.
:::

## One definition per metric

### Why honest teams report different numbers

Benn Stancil, writing in 2021, named the gap in the modern data stack: "there's no central repository for defining a metric." The data gets loaded and transformed centrally, but the formula for "active account" or "churn" lives in each dashboard, each spreadsheet and each analyst's query. Every copy drifts a little. Eventually marketing, finance and product each present a different number for the same thing, each correctly computed from its own definition.

Governance, at the level a product leader needs it, is the set of practices that stop this. It has four parts: written definitions, a single source of truth, a semantic layer that serves the definitions, and contracts with the owners of each source.

### The metric dictionary

The metric dictionary is a written entry for every metric that appears in a recurring report. Chapter 17's metric definition card pins down one metric for one question; the dictionary is the governed collection of those cards, extended with ownership, type, thresholds and versioning. This book's template (in the artifacts section) asks for:

- a plain-language definition a customer could read;
- the formula in words: numerator, denominator, filters and exclusions;
- the grain and time window;
- the segments it may be cut by;
- the source of record and its name in the semantic layer;
- an owner who is accountable for it and a steward who maintains the logic;
- its type: input or output, North Star, health metric or guardrail;
- a target and a threshold for "exceptional variation";
- known caveats and the decisions it informs;
- a version number and a change log.

The change log matters most. Definitions should change when the business changes, but never silently. When the definition of "active responder" changes in June, every chart that crosses June needs a marker, and anyone comparing this quarter to last needs to know.

### A single source of truth

"Single source of truth" is often heard as "one giant database." In practice it means something smaller and more useful: for each metric, exactly one place where its definition and its computed value are authoritative, and an agreement that every report reads from there. Two dashboards may show the same metric; they may not compute it separately.

When two numbers disagree, the single source of truth also settles which one stands, so the meeting can spend its time on the business instead of on reconciliation.

### The semantic layer as a concept

A **semantic layer** (Stancil called it a metrics layer) is the mechanism that makes a single source of truth practical. It sits between the raw data and every tool that uses it. Each metric is defined once: the measure, the filters, the time grain, the dimensions it can be sliced by. Dashboards, spreadsheets and AI agents all ask the layer for "NRR by tier for Q3" instead of computing it themselves. dbt Labs' documentation describes the payoff plainly: define a metric once, and a change to its definition flows to every place that uses it.

You don't need to know how any particular semantic layer is built. You need to know three things. It exists or it doesn't in your company. Your recurring reports should read from it wherever it does. And in 2026 it's also the safest interface for an AI harness, a point the AI lens takes up. The industry is moving the same way: in September 2025 Snowflake announced the Open Semantic Interchange, an effort with dbt Labs, Salesforce, ThoughtSpot and others to create a vendor-neutral standard for semantic definitions, so that a metric means the same thing whether a BI tool or an AI agent asks for it.

### Data contracts

A **data contract** is a written agreement between the owner of a dataset and the people who depend on it. The Open Data Contract Standard, maintained by the Bitol project, organizes a contract into sections that include schema, data quality expectations, service levels, team and roles, support and authoritative definitions. You won't write the contract file, but you should ask for one, or at least a contract-shaped row in your inventory, for every source a recurring report depends on: who owns it, how fresh it will be, what quality checks run and who to call when it breaks.

:::leader For product leaders
Make one person accountable for each metric in your WBR, by name. Then agree with your data, finance and RevOps peers which metrics are shared across functions (ARR, NRR, active accounts) and who owns each one's definition. The cross-functional metrics are where conflicting numbers come from, and they're too important to be owned by whoever built the first dashboard.
:::

## How to apply it

Here's a method for building the data landscape and report set for a product you've just inherited, or for resetting one that has grown into forty dashboards nobody trusts. Plan on about six weeks of part-time effort, most of it conversations.

**Weeks 1 and 2: Map what exists.**

1. **List the decisions first.** Take the decision question bank from Chapter 17. For each recurring decision (quarterly planning, pricing changes, launch go or no-go, renewals at risk), note the questions it depends on.
2. **Build the data source inventory.** One row per source, using the inventory template. Ask your harness to draft it from whatever documentation, catalogs and dashboards it can reach, then verify each row with the owner in a 20-minute conversation. The questions for each owner: what's the grain, how fresh is it, what's the account identifier, what does everyone get wrong about this data, and who fixes it when it breaks?
3. **Map the account key.** For each source, record the account identifier and how it maps to the others. Mark every known break: partner-managed tenants, subsidiaries, merged accounts, trial tenants.
4. **Inventory the existing reports.** List every dashboard and recurring deck that mentions your product. For each, note who uses it and which decision it informs. Expect to find duplicates computing the same metric differently, and dashboards with no audience.

**Weeks 3 and 4: Define and choose.**

5. **Pick the WBR metrics.** Choose 15 to 30, ordered from controllable inputs to outputs to financials. Connect them to the North Star and metric tree from Chapter 02. Name an owner for each.
6. **Write the metric dictionary entries.** Start with the WBR metrics and the cross-functional ones (ARR, NRR, active accounts). Where two teams define a metric differently, don't pick a winner in a spreadsheet. Get the owners in a room, agree on one definition, version it and log the change.
7. **Draft the report catalog.** For each of the twelve reports, write the questions it must answer, its cadence, audience, owner, sources and the decision it feeds. Mark which reports exist, which need rebuilding and which you'll defer. Most teams should run five or six well before attempting all twelve.

**Weeks 5 and 6: Build, run and prune.**

8. **Move definitions into the governed layer.** Work with the data team so that each dictionary entry exists in the semantic layer (or the closest thing your company has), and point the recurring reports at it.
9. **Run the WBR for four weeks before changing it.** Use the exception-driven rules: owners speak only to exceptional variation, "I don't know" is allowed and logged, and nobody improvises a cause. After four weeks, drop metrics that never triggered a discussion or a decision, and add the ones people kept asking about.
10. **Retire what the catalog replaced.** Archive duplicate dashboards, with a note pointing to the governed report. Leaving them up guarantees the old numbers resurface in someone's deck.
11. **Schedule the reviews.** Put the weekly, monthly and quarterly reports on the calendar, with named owners, and add a quarterly review of the inventory and dictionary themselves. Sources change, owners move and definitions drift.

The inventory, dictionary and catalog are durable artifacts in your Product 360. The reports built on them are living artifacts, rebuilt every cycle.

## The AI lens

### When the product is AI-powered

AI features add a data source that most report sets ignore, and they change the economics enough that the report set has to follow.

**AI traces are product data.** A trace records each step of a request: the prompt and response, retrieval steps, tool calls, latency per step, tokens and cost, plus any quality scores attached afterward. That's how the Langfuse documentation describes them. OpenTelemetry has published semantic conventions for generative AI that cover agent spans and MCP tool calls, along with conventions for specific model providers, so the vocabulary for traces is converging. (The conventions are still evolving; check their status before you depend on a particular field.) For an agent product, the trace is the only record of *why* the product did what it did. Put AI traces in your inventory with an owner, an access policy and a retention rule, because they routinely contain customer content.

**Evals belong in the report set.** Anthropic's 2026 guide to evaluating agents distinguishes **capability evals**, which start low and measure progress on hard tasks, from **regression evals**, which should sit near 100% and catch anything that breaks. It also defines pass^k, the share of tasks where all k attempts succeed, for agents where consistency matters more than an occasional success. Those distinctions belong on the AI quality and cost report. A capability eval rising from 40% to 55% is good news; a regression suite falling from 99% to 94% is a release blocker.

Numbers alone won't tell you what's wrong. Hamel Husain and Shreya Shankar, in their evals FAQ, call error analysis the most important activity in evals: read real traces, write open notes on what went wrong, group the notes into a taxonomy of failures, and keep going until new traces stop revealing new failure types. They recommend that you personally annotate at least 30 traces before handing the work to an agent, and they favor simple pass or fail judgments over 1-to-5 ratings. The AI quality report should therefore include the current failure taxonomy and its counts, alongside the pass rates.

**Cost becomes a product metric.** Inference cost moves margin. The FinOps Foundation's guidance on FinOps for AI names unit metrics that fit directly into a product report: cost per inference, cost per million tokens, cache hit rate, **model fit** (the share of requests sent to a more capable model than the task needs) and, most useful for a PM, **cost per successful outcome**: total run cost divided by the runs that met the quality bar. That last metric ties quality to cost. A cheaper model that halves cost per call but doubles failures can raise cost per successful outcome.

**Outcome pricing turns a product metric into a billing unit.** When you price per resolved task, per resolved ticket or per successful outcome, the definition of "resolved" is no longer only an analytics question. It's on the invoice. Product, finance and billing must share one definition, versioned, with finance as a co-owner. Chapter 15 covers the pricing decision; the metric dictionary is where you make it auditable.

### Doing the work with AI

Most PMs in 2026 reach their data through an AI harness: Claude or a similar assistant connected to company systems through connectors. Anthropic introduced the Model Context Protocol (MCP) in November 2024 as an open standard for connecting AI tools to data sources, and some data platforms now expose their governed layers through it. dbt Labs' MCP server, for example, gives an AI assistant read-only access to governed metrics, lineage and freshness information. Chapter 19 covers the mechanics. Here the point is what to point the harness at.

**Ask the governed layer, not the raw tables.** Two studies show why. Spider 2.0, a benchmark of 632 real enterprise text-to-SQL tasks presented at ICLR 2025, found that the best agent tested solved 21.3% of them, against 91.2% on the older, simpler Spider 1.0 benchmark. A 2023 study by Juan Sequeda, Dean Allemang and Bryon Jacob found that GPT-4 answered 16% of questions correctly when querying an enterprise insurance database directly, and 54% when the same data was described through a knowledge graph that encoded the business meaning. Both studies used models that are now out of date, and the second came from a knowledge-graph vendor, so treat the exact numbers as historical. The direction is what matters: business context, encoded as definitions, makes AI answers on enterprise data far more reliable. Your metric dictionary and semantic layer are that context.

**Make provenance part of every answer.** Ask the harness to return, with every number, the metric name and definition version it used, the source, the data freshness and anything it excluded. Treat a number without provenance as a draft.

**Run the trust check before the analysis.** The five questions from earlier (freshness, quality, volume, schema, lineage) make a good preamble for any analysis prompt, and a harness can check them in seconds.

**Ask for the denominator and the accounts.** Percentages hide small numbers. In enterprise data, "acceptance fell 12 points" might be three accounts. Ask the harness to show the account list behind any move.

**Spot-check one account by hand.** For any number that will drive a decision, pick one account and trace it through each source with the owner. If the account doesn't reconcile, the report doesn't either.

**Keep the anecdote attached.** A harness can pull ticket verbatims, call excerpts and sample traces as easily as it pulls numbers. Ask for both. That's how you resist the proxy problem Bezos described.

:::ai The one-line rule
Let the harness pull and summarize. Make it cite the governed definition, the source and the freshness for every number, and make it say when it had to guess.
:::

Two cautions. Connecting a harness to customer data, call recordings or traces is a data-handling decision, so use only approved tools and connectors. And the harness will confidently answer a question your data can't answer; check the inventory's "can't tell you" column before you ask.

## The Beacon case: one number, two definitions

:::example Where Beacon starts
You've been Principal PM for Beacon for two months. Beacon has about $48M in ARR, growing 38% a year, across about 420 enterprise customers, with NRR at 118%. Gross margin fell from 81% to 72% after the agentic features launched, because of inference cost. There are 43 dashboards that mention Beacon. Leadership is preparing for Northlight Live, where Beacon Agents will launch, and for a move from per-environment pricing to a price per resolved incident.
:::

**The trigger.** A draft keynote slide from marketing quotes a total for incidents Beacon has resolved since launch. The number is many times larger than the North Star trend in the product team's weekly review. Both teams say they're right, and both are. Marketing counted every incident Beacon correlated. The product team counts **incidents resolved with Beacon's help**: incidents where a responder accepted Beacon's diagnosis or an approved action ran. Neither definition was written down.

**The inventory.** You build the data source inventory over two weeks. Several rows matter more than you expected:

- **Telemetry** records alerts ingested, incidents correlated, diagnoses proposed and accepted, actions proposed, approved and run. The trap: test tenants and Northlight's own internal tenant are mixed in with customers.
- **CRM** holds the 420 enterprise accounts plus partner accounts. The trap is Leo, the MSP operations manager. His 60 mid-market customers appear as child accounts under one partner account in the CRM but as 60 separate tenants in telemetry. Any per-account metric that ignores this mapping either drops them or counts them twice.
- **Billing** charges a platform fee per environment plus usage today. Once per-resolved-incident pricing launches, a "resolved incident" becomes a billing event. That makes the North Star definition a revenue definition too.
- **Support tickets** live in Northlight Desk, Northlight's own ITSM product, which means the support data has an owner inside the company and a clean API.
- **NPS** goes to whoever the customer success team lists as the contact, usually Priya, the SRE lead. Marcus, the VP of IT Operations who signs the renewal, is rarely surveyed. The score describes the champion's view, not the buyer's.
- **AI traces** hold each diagnosis's evidence chain, tool calls, tokens and cost. They also hold snippets of customer logs, which Sam, the security reviewer persona, will ask about.
- **FP&A** owns the margin numbers, but nobody has defined inference cost per resolved incident, which is the unit the new pricing will need.

**The definition.** You convene the owners of the North Star (you), billing (finance) and the keynote (product marketing) and agree one dictionary entry. "Incidents resolved with Beacon's help" counts an incident once, even if it was correlated across several tools, when a responder accepted Beacon's diagnosis, an approved Beacon action ran, or both. It excludes test and internal tenants. It's measured weekly from the semantic layer, with finance as co-owner because it's about to become a billing unit. Marketing gets a second, clearly labeled metric, "incidents correlated," which it can use in the keynote with its own definition on the slide.

Three other entries need the same treatment. **Diagnosis acceptance rate** counts acceptances over diagnoses *shown* to a responder, not diagnoses generated, because many diagnoses are generated for incidents nobody opens. **MTTR** is reported as a median, from Beacon's own incident timestamps, and labeled separately from any customer-reported MTTR. **NRR** is stated with its window and whether price changes count, so the 118% can be compared with next year's.

**The WBR.** You design Beacon's weekly review in causal order:

| Order | Metric | Type | Owner (role) |
|---|---|---|---|
| Inputs | New customer connectors live | Input | Integrations engineering lead |
| | Accounts with Diagnose enabled | Input | Diagnose PM |
| | Regression eval pass rate | Input | Applied AI lead |
| | Median time to first diagnosis | Input | Engineering lead |
| Outputs | Incidents resolved with Beacon's help (North Star) | Output | Principal PM |
| | Diagnosis acceptance rate | Output | Diagnose PM |
| | Autonomous resolution rate | Output | Agents PM |
| | Weekly active responders | Output | Principal PM |
| | Median MTTR, reference cohort | Output | Principal PM |
| Financials | ARR and NRR | Financial | Finance partner |
| | Gross margin | Financial | Finance partner |
| | Inference cost per resolved incident | Financial | Finance partner and Principal PM |

In the fourth week, most lines get "nothing to see here." One doesn't. Diagnosis acceptance has dropped for EU accounts over three weeks. The Diagnose PM doesn't yet know why, says so, and the follow-up is logged. By the next review, error analysis on a sample of EU traces shows that a retrieval change is pulling evidence from the wrong region's logs for customers with data-residency settings.

**The AI quality and cost report.** That finding connects to the incident everyone at Beacon remembers: the hallucinated root cause that led a customer to roll back the wrong service. When the team reread that trace, the agent had cited logs from a different service with a similar name. That case is now in the regression suite, along with the EU retrieval failure. The report tracks regression pass rate (target near 100%), production acceptance, rollbacks after a Beacon action, the failure taxonomy from error analysis and cost per successful diagnosis. The last metric explains the margin story better than total inference spend: it shows which failures are also costing money.

**Pipeline influence.** Joining CRM loss reasons with call transcripts shows a pattern in deals lost to prospects who don't use Northlight Observe: buyers asking whether Beacon works with their existing observability tools. The sample is small and the link is correlational, but it bears directly on the build-on-Observe versus tool-agnostic tension, so it goes into the quarterly portfolio review.

**The QBR packs.** The customer QBR for Marcus now uses the governed definitions: MTTR trend, escalations avoided, incidents resolved with Beacon's help, approval-gate statistics Sam can audit, and an ROI story for the CFO. The internal QBR puts Beacon beside Observe and Desk: 38% ARR growth, 118% NRR and a 72% gross margin that now has a unit-cost explanation and an owner.

**What changed.** The keynote slide uses "incidents correlated," labeled. Of the 43 dashboards, the duplicates are archived with a pointer, six governed reports from the catalog go live and the rest of the twelve are scheduled. The per-resolved-incident price launches on a definition that product, finance and billing signed. None of it needed new tooling: it took the inventory, four dictionary entries and agreement on who owns each number.

## Product 360 artifacts

```template id="18-data-source-inventory" title="Data source inventory"
# Data source inventory · [Product] · v[n] · [Date]

**Owner:** [PM]   **Reviewed with:** [data, RevOps, finance, support, applied AI owners]   **Next review:** [Date, at least quarterly]

## Sources
| Source | System of record | Owner (named person and team) | Grain (event, account, opportunity, invoice, ticket, trace) | Freshness | Account identifier | Can tell you | Can't tell you | Known traps | Harness access (governed or raw; connector or MCP) | Contract or SLA? |
|---|---|---|---|---|---|---|---|---|---|---|
| Product telemetry | | | | | | | | | | |
| CRM | | | | | | | | | | |
| Billing and subscription | | | | | | | | | | |
| Support tickets | | | | | | | | | | |
| Surveys and NPS | | | | | | | | | | |
| Sales and customer calls | | | | | | | | | | |
| Product reviews and communities | | | | | | | | | | |
| Market and competitive data | | | | | | | | | | |
| Finance and FP&A | | | | | | | | | | |
| AI traces and evals | | | | | | | | | | |

## Account mapping
| Source | Identifier used | Maps to the master account by | Known breaks (partners, subsidiaries, test tenants, merges) | Who fixes it |
|---|---|---|---|---|
| | | | | |

## Sensitive data
| Source | Contains customer content or personal data? | Access policy | Retention | Approved tools for AI use |
|---|---|---|---|---|
| | | | | |

## Open requests to source owners
| Request (freshness, field, definition, join key) | Owner | Needed for which report | Due |
|---|---|---|---|
| | | | |
```

```template id="18-report-catalog" title="Report catalog"
# Report catalog · [Product or portfolio] · [Date]

**Owner:** [Product leader]   **Rule:** every recurring report appears here, or it gets archived.

| # | Report | Questions it must answer | Decision it feeds | Cadence | Audience | Owner | Primary sources | Key metrics (dictionary IDs) | Status (live / rebuild / planned / deferred) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Weekly metrics review | What changed? Is it exceptional? Why? What are we doing? | Weekly priorities and escalations | Weekly | | | | | |
| 2 | Product health | Is the product working for customers? | Reliability investment, release holds | Daily view, weekly review | | | | | |
| 3 | Funnel and activation | Where do new accounts stall before first value? | Onboarding investment | Weekly, monthly deep dive | | | | | |
| 4 | Retention and NRR | Which cohorts expand, contract or churn, and why? | Retention bets, packaging | Monthly, quarterly | | | | | |
| 5 | Feature adoption | What's used, by whom, how broadly and deeply? What should we retire? | Invest, fix or retire | Monthly; 30, 60, 90 days after launch | | | | | |
| 6 | Customer health | Which accounts are at risk or ready to expand? | Account plans, escalations | Weekly list, monthly trend | | | | | |
| 7 | Pipeline influence | Which capabilities show up in won and lost deals? Which gaps block deals? | Roadmap, competitive response | Monthly, quarterly | | | | | |
| 8 | Pricing and discount | What do customers actually pay? Where does price leak? | Pricing and packaging changes | Monthly, quarterly | | | | | |
| 9 | Support trends | Top themes by volume and ARR affected; what's new? | Defect priorities, docs, deflection | Weekly digest, monthly | | | | | |
| 10 | AI quality and cost | Is the AI getting better or worse? What does a successful outcome cost? | Release gates, model choice, pricing | Weekly; every model or prompt change | | | | | |
| 11 | QBR pack (internal and customer) | Are bets on track? What value did this customer get? | Quarterly priorities; renewals | Quarterly | | | | | |
| 12 | Portfolio review | Where is investment against return across the portfolio? | Grow, sustain, harvest, retire | Quarterly or twice a year | | | | | |

## Archived reports
| Report | Replaced by | Archived on | Pointer left? |
|---|---|---|---|
| | | | |
```

```template id="18-weekly-business-review-pack" title="Weekly business review pack"
# Weekly business review · [Product] · Week of [Date]

**Facilitator:** [name]   **Data as of:** [timestamp]   **Definitions:** metric dictionary v[n]   **Trust check:** passed / failed on [source]

## Rules
- Every metric is shown. Owners speak only to exceptional variation or a missed target.
- "Nothing to see here" is a complete answer for a normal week.
- "I don't know yet" is allowed. The follow-up gets logged with an owner and a date.
- No improvised causes.

## 1. Controllable inputs
| Metric (dictionary ID) | Owner | This week | Trailing 4 weeks | Same week last year | Target | Exception? | Comment |
|---|---|---|---|---|---|---|---|
| | | | | | | Y / N | |

## 2. Outputs
| Metric (dictionary ID) | Owner | This week | Trailing 4 weeks | Trailing 12 months | Target | Exception? | Comment |
|---|---|---|---|---|---|---|---|
| North Star: | | | | | | | |
| | | | | | | | |

## 3. Financials
| Metric | Owner | Latest | Plan | Variance | Exception? | Comment |
|---|---|---|---|---|---|---|
| | | | | | | |

## Accounts behind the moves
For each exception, list the accounts that drove it, with ARR and segment.

## Customer reality check
Two or three verbatims (tickets, calls, traces) that show what the numbers stand for this week.

## Follow-ups
| # | Question | Owner | Due | Answered? |
|---|---|---|---|---|
| | | | | |

## Metric set changes proposed
Add / drop / redefine, with reason. (Change only after four weeks of evidence.)
```

```template id="18-qbr-metrics-pack" title="QBR metrics pack"
# QBR metrics pack · [Product] · Q[n] [Year]

**Version:** Internal (executive product review) / Customer ([Account name])   **Definitions:** metric dictionary v[n]   **Data as of:** [Date]

## A. Internal product QBR
### Summary
Three sentences: where we are against goals, the biggest change this quarter, the decision we need.

### Goals and bets
| Goal or bet | Target | Result | Status (on track / at risk / missed / killed) | Evidence |
|---|---|---|---|---|
| | | | | |

### Output metrics (quarter and trailing four quarters)
| Metric | Q-3 | Q-2 | Q-1 | This Q | Target | Comment |
|---|---|---|---|---|---|---|
| North Star | | | | | | |
| NRR (state window and price treatment) | | | | | | |
| GRR | | | | | | |
| ARR | | | | | | |
| Gross margin | | | | | | |
| AI cost per successful outcome (AI products) | | | | | | |

### What we learned
Top findings from adoption, support, pipeline and pricing reports.

### Decisions requested
1.
2.

## B. Customer QBR
### Executive summary
### The outcomes you bought us for
| Original buying reason | Metric | Baseline | This quarter | Trend |
|---|---|---|---|---|
| | | | | |

### Adoption and time to value
### ROI (method stated; customer's own numbers where possible)
### Progress against last quarter's goals
### Benchmark (only if the comparison group is defined)
### Health and risks
### Actions
| Action | Owner (ours / theirs) | Date |
|---|---|---|
| | | |

### Next QBR: [Date]
```

```template id="18-metric-dictionary" title="Metric dictionary entry"
# Metric: [Name] · ID [metric-id] · v[n]

**Owner (accountable):** [name]   **Steward (maintains logic):** [name]   **Status:** Draft / Approved / Deprecated

## Definition
One sentence a customer could read.

## Formula in words
- Numerator:
- Denominator:
- Filters and exclusions (test tenants, internal accounts, trials):
- Deduplication rule:

## Grain and time
- Grain (event, user, account):
- Time window (weekly, trailing 12 months, snapshot date):
- Fiscal or calendar:

## Allowed segments
[Tier, region, channel, cohort, product line]

## Source
- Source of record:
- Semantic layer name:
- Freshness:

## Type
Input / Output · North Star / Health / Guardrail / Financial · Billing unit? Y / N (if Y, finance co-owns)

## Targets and thresholds
- Target:
- Exceptional variation means:

## Caveats
What this metric can't tell you, and how it could be gamed.

## Decisions it informs
[Reports and decisions]

## Change log
| Version | Date | What changed | Why | Approved by | Charts that need a marker |
|---|---|---|---|---|---|
| | | | | | |
```

```template id="18-data-trust-check" title="Data trust check"
# Data trust check · [Report or analysis] · [Date]

Run before any number drives a decision. Record failures before the answer, not after.

| Check | Question | Result | Action if failed |
|---|---|---|---|
| Freshness | When was each source last updated? Is that later than the decision needs? | | |
| Quality | Are null, duplicate or out-of-range rates unusual? | | |
| Volume | Did event or row counts move outside the normal range? | | |
| Schema | Did any field, event name or definition change in the last 30 days? | | |
| Lineage | Which upstream sources feed this number? Did any have a problem? | | |
| Definition | Which dictionary entry and version was used? | | |
| Denominator | What's the base, and how many accounts does it contain? | | |
| Hand check | Does one named account reconcile across sources? | | |

**Verdict:** Trust / Trust with caveats (list) / Don't use yet
```

## Prompts

```prompt title="Draft a data source inventory"
Goal: Get a first draft of the inventory to verify with source owners.
Paste in (or connect the harness to): data catalog entries, dashboard lists, data team documentation and any existing metric definitions. Use only approved tools and connectors.

Draft a data source inventory for [product]. Use one row per source: product telemetry, CRM, billing and subscription, support tickets, surveys and NPS, sales and customer calls, product reviews and communities, market and competitive data, finance and FP&A, AI traces and evals, plus any other source you find.

For each row give: system of record, owner (named team and person if documented), grain, refresh frequency, account identifier, what it can tell us, what it can't tell us, known data quality traps and how an AI assistant can reach it (governed layer or raw tables).

Rules:
- Cite the document each field came from. If nothing documents a field, write "Unknown: ask owner."
- List every place where account identifiers differ between sources.
- Don't guess owners.

Check the output: take the draft to each owner and confirm every row in a short conversation. Count the "Unknown" cells; they're your request list.
```

```prompt title="Run the trust check before an analysis"
Goal: Catch broken data before it becomes a decision.
Paste in: the question you're about to ask and the metric names involved.

Before answering the question below, check the data behind it and report on each item first:
1. Freshness: when was each source last refreshed?
2. Volume: did event or row counts for the last 7 days fall outside their usual range?
3. Schema: did any field, event name or metric definition change in the last 30 days?
4. Lineage: which upstream sources feed these metrics, and did any report problems?
5. Quality: are null, duplicate or out-of-range rates unusual?

Use governed metrics from the semantic layer where they exist, and name the definition version for each. If any check fails, stop and tell me what failed before giving any answer.

Question: [question]

Check the output: if the harness reports all checks passed without naming dates, counts or versions, ask it to show the evidence for each.
```

```prompt title="Write a metric dictionary entry and find conflicts"
Goal: Pin one definition for a metric and expose where teams differ.
Paste in: every existing definition of the metric you can find (dashboards, decks, finance docs, contracts, pricing pages) with their sources.

Using the definitions below for [metric], do two things.

First, compare them. Make a table showing, for each source: numerator, denominator, filters and exclusions, time window, deduplication rule and who owns it. Highlight every difference that would change the number.

Second, draft one metric dictionary entry with: plain-language definition, formula in words, grain and time window, allowed segments, source of record, owner and steward, type (input or output; North Star, health, guardrail or financial; billing unit or not), caveats including how it could be gamed, and a change-log row explaining what this version changes from each existing definition.

Don't choose between conflicting definitions silently. List the decisions the owners need to make.

[definitions with sources]

Check the output: make sure every difference in the table traces to a real source. The decisions list is the agenda for the meeting with the owners.
```

```prompt title="Prepare the weekly business review"
Goal: Produce an exception-driven WBR draft from governed metrics.
Paste in (or connect): the WBR metric list with dictionary IDs, owners and targets. Use an approved tool if the data includes customer names.

Prepare this week's business review for [product] using only the governed metrics listed. Keep the order: inputs, then outputs, then financials.

For each metric show this week, the trailing four weeks, the same week last year where available and the target. Flag a metric as exceptional only if it crosses its documented threshold. For each exception, list the accounts that drove the move, with ARR and segment.

Don't explain causes. For each exception, list the questions the owner should answer and the data that could answer them.

Add two or three customer verbatims from this week's support tickets or call notes that relate to the exceptions, with sources.

State the data freshness and definition versions at the top.

Check the output: confirm the exception flags match the thresholds in the dictionary. Delete any sentence that offers a cause; that's the owner's job in the meeting.
```

```prompt title="Build the AI quality and cost report"
Goal: See whether the AI is getting better or worse, and what each good outcome costs.
Paste in (or connect): eval results (capability and regression suites), a sample of production traces, user feedback events and AI cost data. Traces may contain customer content: use an approved tool only.

Build this period's AI quality and cost report for [product/feature].

1. Regression suite pass rate and capability suite pass rate, with the change from last period. Flag any regression below [threshold].
2. Production quality: [acceptance rate or equivalent], and user-reported failures.
3. Error analysis: from the sampled traces, group failures into categories using short, plain names. Give counts and one example trace ID for each. Mark categories that are new this period.
4. Cost: cost per request, cost per million tokens, cache hit rate and cost per successful outcome (total run cost divided by runs that met the quality bar). Note any requests routed to a more capable model than the task seemed to need.
5. The three changes most likely to improve cost per successful outcome.

Check the output: open at least five of the cited traces and confirm they show the failure named. If new failure categories appear, add a regression case for each.
```

```prompt title="Draft a customer QBR metrics pack"
Goal: Tell one customer the value story with governed numbers.
Paste in (or connect): the account's governed metrics, the original buying reasons from the CRM opportunity, last QBR's goals, open support tickets and the latest health score. Use an approved tool for customer data.

Draft a QBR metrics pack for [account] with these sections: executive summary (three sentences), the outcomes they bought us for with baseline and current values, adoption and time to value, ROI with the method stated, progress against last quarter's goals, health and risks, and proposed actions with owners on both sides.

Rules:
- Use only governed metrics and state the definition for each the first time it appears.
- Where ROI depends on an assumption (for example, an hourly cost), show the assumption and mark it for the customer to confirm.
- Include risks honestly. Don't omit open escalations.

Check the output: reconcile two numbers by hand with the account team before the meeting. Remove any benchmark that doesn't define its comparison group.
```

```prompt title="Find where product shows up in won and lost deals"
Goal: Get evidence of product gaps in the pipeline without overstating influence.
Paste in (or connect): closed opportunities for the last two quarters with stated loss reasons, plus call transcript summaries or competitor mentions. Use an approved tool for call data.

For [product], analyze closed-won and closed-lost opportunities from [period].

1. List the capabilities and competitors mentioned, with counts in won and lost deals, by segment.
2. Highlight capabilities that appear much more often in losses than wins. For each, give three representative excerpts with opportunity IDs.
3. Compare stated loss reasons in the CRM with what the call excerpts suggest. Note where they disagree.
4. State the sample size for every claim, and label everything as correlation, not cause.

Don't estimate revenue "influenced" by the product.

Check the output: read the excerpts behind the top two gaps yourself. If the counts are small, say so in the report.
```

## Anti-patterns

:::warn The forty-dashboard estate
Every question gets a new dashboard, and none is ever retired. Three of them compute active accounts differently, and the one in the executive deck is the oldest. Keep a report catalog, point every report at governed definitions and archive the rest with a pointer.
:::

:::warn The undefined headline number
A launch slide, a board deck and a WBR each show a different count of the same thing, and nobody wrote down any of the definitions. Every metric that leaves the product team needs a dictionary entry with an owner and a version.
:::

:::warn Asking the wrong source
The team uses NPS to measure adoption, CRM loss reasons to explain churn, or support volume to size a problem across the base. Each source is blind to something. Check the "can't tell you" column before you ask.
:::

:::warn Trusting the harness on raw tables
A PM asks an AI assistant a revenue question, and it writes its own query against raw tables, joins on the wrong account key and returns a confident number. Point the harness at governed metrics, require it to cite definitions and freshness, and hand-check one account.
:::

:::warn The narrated WBR
The weekly review becomes a series of presentations in which every owner explains every metric, and causes are improvised on the spot. Show every metric, discuss only exceptions, and log "I don't know" as a follow-up.
:::

:::warn Influence inflation
"Product influenced $X of pipeline" appears in a planning deck, built from opportunity tags. It's correlation, it's easy to inflate and it teaches the organization to distrust product numbers. Report gaps in lost deals, with sample sizes, instead.
:::

:::warn Offline evals as the quality report
The AI quality report shows a high eval pass rate while customers report wrong answers. The eval set has drifted from production. Read production traces, keep the failure taxonomy current and add every production failure as a regression case.
:::

## Checklist

- [ ] A data source inventory covers all ten source types, with a named owner, grain, freshness, account identifier, "can tell you," "can't tell you" and known traps for each.
- [ ] The account mapping across telemetry, CRM, billing and support is written down, with known breaks (partners, subsidiaries, test tenants).
- [ ] Sources holding customer content or personal data, including AI traces, have an access policy, retention rule and approved tools listed.
- [ ] A report catalog lists every recurring report with its questions, decision, cadence, audience, owner and sources; duplicates are archived.
- [ ] The weekly business review runs in causal order (inputs, outputs, financials), is exception-driven and has a named owner for every metric.
- [ ] Every metric in a recurring report has a metric dictionary entry with an owner, a steward, a version and a change log.
- [ ] Cross-functional metrics (ARR, NRR, active accounts, any billing unit) have one agreed definition, with finance as co-owner where money is involved.
- [ ] Recurring reports and the AI harness read from the governed layer, not raw tables.
- [ ] The five-question trust check runs before any number drives a decision.
- [ ] For AI products, the AI quality and cost report tracks regression and capability evals, a failure taxonomy from error analysis and cost per successful outcome.
- [ ] Pipeline influence is reported as correlation, with sample sizes and lost deals shown.
- [ ] Internal and customer QBR packs use the same governed definitions.
- [ ] The inventory, dictionary and catalog are reviewed at least quarterly.

## Key takeaways

- Enterprise product questions cross sources. Map ten of them, with what each can and can't tell you, its owner and its traps, before asking anything of the data.
- The account mapping across telemetry, CRM, billing and support is the hidden dependency of every B2B report. Make someone own it.
- Own a small set of recurring reports, each defined by the questions it must answer, its cadence and its audience. Start with the weekly metrics review, ordered from controllable inputs to outputs to financials and discussed by exception.
- Write one definition per metric, with an owner and a version, and serve it from a single governed layer. When a product metric becomes a billing unit, finance co-owns the definition.
- For AI products, traces and evals are product data. Report regression and capability evals, the failure taxonomy and cost per successful outcome.
- Point the AI harness at governed definitions, require provenance with every number, run the trust check first and hand-check one account before acting.
