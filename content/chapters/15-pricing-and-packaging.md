<p class="lead">Chapter 12 showed you how much value your product creates for a customer. This chapter is about how you charge for it: the unit the price scales with, the packages customers choose between, the research that tells you what they'll pay, the discipline that stops discounts from eroding it, and the new pricing models that AI agents have pushed into B2B software in 2026.</p>

## Why this matters

Most product teams still decide price last. A few weeks before launch someone asks what it should cost, and by then the important pricing decisions have been made by accident. The features are bundled the way engineering happened to build them, the unit of charge is whatever the billing system supports, and the price comes from a competitor's page or last year's number.

Madhavan Ramanujam and Georg Tacke, partners at the pricing consultancy Simon-Kucher, argue in *Monetizing Innovation* (2016) that this order is the main reason good products miss their revenue goals. They report a Simon-Kucher survey of 1,615 companies in which 72% of new products from the prior five years had missed their revenue or profit targets or failed. That's vendor research, so read it as a sign of scale. The diagnosis matters more than the number: teams that build first and price afterward learn what customers would pay for only when it's too late to change what they built.

Three things make this harder in 2026. **Pricing changes far more often.** PricingSaaS, which tracks the published pricing of 500 SaaS and AI companies, counted more than 1,800 pricing changes among them in 2025: 43% to packaging, 40% to price or price structure and 17% to usage limits. Kyle Poyar, who writes the Growth Unhinged newsletter on B2B monetization, offers a practitioner's rule of thumb that pricing which used to last about 18 months can now be out of date within six. **AI broke the seat.** When an agent does work people used to do, a per-seat price charges less as the product delivers more. **AI has a cost of goods.** Every diagnosis or action consumes inference; Beacon's gross margin fell from 81% to 72% after its agentic features launched. A price that ignores cost loses money on your heaviest users, and a price set only on cost leaves most of the value on the table.

### What the PM owns

Finance owns margin targets and revenue recognition, sales owns the negotiation, and a pricing team, where one exists, owns the price book. The Principal PM owns what connects them to the product: which value metric the product can meter, which capabilities go in which package, what the product must log so a usage or outcome price can be billed and defended, and what customers see before an invoice surprises them. If the PM doesn't own those decisions, the billing system ends up making them.

:::key Price is a product requirement
The value metric, the packages, the metering and the spend controls are things the product has to do. Write them into the PRD alongside the features, with an owner and acceptance criteria. If the product can't measure a unit reliably, it can't charge for it.
:::

## Design the product around the price

### The core idea

The subtitle of Ramanujam and Tacke's book states the thesis: design the product around the price. Set a target price from evidence about willingness to pay, then design the product to fit it. Price becomes a design input that shapes which features get built and how they're packaged.

Their opening example contrasts two car launches. Porsche, before engineering the Cayenne, asked prospective buyers what they wanted in an SUV and what they would pay, and was prepared to walk away if the numbers didn't work. Fiat Chrysler built the Dodge Dart first and priced it afterward; the authors report it sold about 25,000 units in 2012, roughly a quarter of what analysts had forecast. The lesson for software is the same. Willingness to pay is data you can collect before you build, and it should change what you build.

### Four ways innovations fail to monetize

Ramanujam and Tacke name four failure types, and they're a useful diagnostic vocabulary for any portfolio review.

| Failure type | What happens | Typical cause | B2B example |
|---|---|---|---|
| **Feature shock** | Too many features crammed into one product; it confuses buyers and is often overpriced | Every stakeholder's request goes in; nobody asked what customers value | An enterprise tier with forty capabilities that most buyers use five of |
| **Minivation** | The right product for the right market, priced too low to reach its potential | Fear of losing deals; cost-plus pricing on a high-value capability | An AI agent priced as a cheap add-on when it replaces hours of skilled work |
| **Hidden gem** | A potential hit that never gets properly brought to market | It sits outside the core business, so nobody champions it | An internal tool that customers keep asking to buy |
| **Undead** | An innovation customers don't want that ships anyway | It answers a question nobody asked | A dashboard built because a competitor has one |

AI products are especially prone to minivation. A team ships an agent that saves a customer hours of work, then prices it on the cost of the tokens it consumes. Poyar's 2026 survey found that internal costs and margins were the top factor in setting AI prices, cited by 54% of companies, ahead of competition (36%) and the productivity gains customers get (30%). Cost sets the floor; the customer's value should set the price.

### The nine rules, in brief

The book then sets out nine rules. The first four belong in discovery and design, where most PMs never bring them: have the willingness-to-pay conversation early, because you can't prioritize without it; segment by needs and willingness to pay rather than defaulting to one offer; treat configuration and bundling as analysis; and choose the monetization model before the price point. The other five cover choosing a pricing strategy, building an outside-in business case on willingness-to-pay evidence, communicating value, using behavioral pricing tactics and keeping price integrity by avoiding knee-jerk repricing. In this book, launch strategy and behavioral tactics are in Chapter 12 and the business case is in Chapter 13.

## Willingness-to-pay conversations

A willingness-to-pay (WTP) conversation is a discovery interview with a pricing purpose. It belongs in the same weekly rhythm as the discovery interviews in Chapter 01, and the Mom Test rules still apply: ask about the past and the present, not opinions about the future.

The mistake is asking "What would you pay for this?" cold. Buyers either anchor low to protect their budget or give a polite number with nothing behind it. A good WTP conversation builds up to price through the buyer's own economics, in a deliberate order:

1. **Context.** What does the problem cost them today, in their numbers: hours, people, tools, incidents, penalties?
2. **Value.** Which capabilities matter most and least? A forced ranking ("if you could keep only three") is the qualitative cousin of the MaxDiff method described below.
3. **Metric.** How would they expect to pay for something like this: per user, per environment, per incident, per outcome? What would make a bill feel unfair?
4. **Range.** Using the Van Westendorp question forms: at what price would this seem so cheap they'd doubt it, a bargain, getting expensive, or too expensive to consider?
5. **Point check.** Using the Gabor-Granger form: "At [price] a year, would you buy?" Then move the price up or down depending on the answer.
6. **Budget.** Which budget line pays (software, services or headcount), who approves it, and what thresholds trigger a procurement review?
7. **Predictability.** Do they prefer a fixed commit, a cap or pay-as-you-go?

Run these conversations with the economic buyer as well as users. Only the person who owns the budget can tell you which budget pays and what the CFO will approve, and budget source matters more than it used to. Poyar's 2026 survey found that 70% of AI spend still comes from existing technology and software budgets, while AI-native companies are starting to tap services budgets (35%) and headcount budgets (15%). A product priced against a headcount budget can charge very differently from one priced against a software line.

:::onramp If you've never talked price with a customer
Start by adding the metric and budget questions (steps 3 and 6) to discovery interviews you're already running. They feel safe to ask, and the answers often surprise the whole team. Leave the range and point-check questions until you have a concept to show.
:::

## The value metric

The **value metric** is the unit your price scales with: per user, per environment, per API call, per resolved ticket. It decides who pays more, when revenue grows and what behavior the price encourages, which makes it the most consequential pricing choice you'll make. Chapter 12 cited the classic case of a copier maker charging per copy rather than per machine.

Poyar proposed five tests for a value metric in 2021. A good metric:

1. **Correlates with the value different customers get.** Customers who get more value pay more.
2. **Shares in the customer's success** and doesn't discourage adoption. If customers ration use to control the bill, the metric is fighting the product.
3. **Is flexible,** so customers can start small and grow.
4. **Grows over time for the average customer,** which gives you expansion revenue without a renegotiation.
5. **Is feasible to monitor and meter** accurately.

This book adds two tests that the AI era has made essential for B2B buyers:

6. **Predictable enough to budget.** Procurement has to approve an annual number. A metric whose volume the buyer can't forecast will be capped, negotiated down or blocked.
7. **Hard to dispute or game.** Both sides must be able to count the units and agree on the count. This matters most for outcome metrics, where the definition of "resolved" or "completed" decides the bill.

No metric scores well on all seven. Seats are predictable but stop tracking value once agents do the work. Usage tracks cost but is hard to budget. Outcomes track value but are hard to define and easy to dispute. That tension is why hybrids keep gaining ground: one metric for predictability, another for value. Poyar also warns that usage-linked revenue grows more slowly at first, because it waits on adoption. Answer that with a platform fee or a minimum commit rather than retreating to a metric that doesn't track value.

## Packaging: tiers, bundles and add-ons

Packaging decides which capabilities customers get together and at what price. Rules 2 and 3 of *Monetizing Innovation* apply directly: segment first, then build packages that match the segments.

### Good, better, best

Many B2B products use three tiers, often called good, better and best. Each tier should map to a real segment with its own needs and willingness to pay. A useful test: can you name the customer each tier is designed for and the job it serves?

To decide which features go where, Simon-Kucher practitioners, Ramanujam among them, use a heuristic that sorts features into three kinds:

- **Leaders** drive the purchase and define a tier. Customers pick a tier because of them.
- **Fillers** are nice to have. They add perceived value but don't drive the decision.
- **Killers** are features that, if included, make customers reject the package, usually because few want them and they push up the price.

Put one or two leaders in each tier, use fillers to round it out, and move killers into add-ons or remove them. MaxDiff research (described below) is a good way to sort features quantitatively.

Poyar adds a packaging rule that works well for B2B: keep features individual users need broadly available, and reserve team and organization capabilities for higher tiers. Single sign-on, advanced security, audit logs, admin controls, invoiced billing and premium support are things the organization values more than any single user, which makes them natural leaders for the top tier.

### Bundles and add-ons

An **add-on** suits a capability with narrow but intense demand: bundling it would inflate the price for everyone, and leaving it out loses the customers who need it. A **bundle** suits capabilities most customers value together.

AI features have gone through both moves. PricingSaaS's review of 2025 found a common arc: AI launched as a paid add-on, then got folded into core tiers alongside a price rise, with credits added as the consumption layer. Notion and Slack both folded AI add-ons into their plans and raised prices, according to that review. Metronome, a usage billing company that cataloged more than 50 AI pricing models in 2026, reports that tiers are increasingly distinguished by consumption capacity, model access and speed rather than by features and seats alone. Chapter 12 covers decoys, anchors and the ethical line; the rule from there applies here too: every tier must be a real offer some customer should rationally choose.

## Pricing research methods

Interviews tell you how buyers think about price; structured research tells you how many think that way. Four methods cover most needs. You don't need to run the statistics, but you do need to know what each one answers and what it can't tell you.

| Method | What it answers | How it works | Output | Main limits |
|---|---|---|---|---|
| **Van Westendorp price sensitivity meter** | What price range feels acceptable? | Four questions: too cheap to trust, a bargain, getting expensive, too expensive to consider | An acceptable range and indicative price points | No competitive context; doesn't predict volume |
| **Gabor-Granger** | How does purchase intent fall as price rises? | Yes or no at a starting price, then higher or lower prices depending on the answer | A demand curve, a revenue curve and a revenue-maximizing price | One product in isolation; no trade-offs between features |
| **Conjoint analysis** (choice-based) | What do buyers trade off, and what is each attribute worth? | Respondents choose among realistic packages that vary features and price, usually across 8 to 20 choice tasks | The value of each attribute, willingness to pay and a simulator for what-if packages | Needs a meaningful sample; heavier to design and run |
| **MaxDiff** (best-worst scaling) | Which features matter most? | Respondents see four or five items at a time and pick the most and least important, across 8 to 15 sets | Feature scores on a common scale, plus segments | Ranks features, not prices |

**Van Westendorp**, developed by the Dutch economist Peter van Westendorp in the 1970s, plots the four answers as cumulative curves whose crossings give an acceptable range, from the point of marginal cheapness to the point of marginal expensiveness. It's quick and good for early range-finding, but the crossings have a weak theoretical basis, and it works poorly in brand-new categories where buyers have no reference price. Newton, Miller and Smith extended it in 1993 with purchase-intent questions, which lets you estimate demand. **Gabor-Granger**, named for the economists Andre Gabor and Clive Granger, suits a repricing or launch where the package is settled and you need a price point. **Conjoint** infers willingness to pay from trade-offs instead of asking directly, which makes it the most realistic and the most expensive. **MaxDiff** is a packaging tool: use it to sort leaders, fillers and killers before you build tiers.

:::note The B2B reality
These methods work best with large samples. B2B products have small buyer populations, buying committees and negotiated prices. You may only be able to survey a few dozen economic buyers, and the person who answers the survey often isn't the one who signs. Treat survey results as one input, and triangulate with your own deal data: win and loss reasons, discount depth by segment, which tiers customers buy and where they upgrade.
:::

## Price elasticity and the break-even test

### Elasticity in one paragraph

**Price elasticity of demand** is the percentage change in quantity demanded divided by the percentage change in price, quoted as an absolute value. Above 1, demand is **elastic**: a price rise loses proportionally more volume, so revenue falls. Below 1, it's **inelastic**, and a price rise raises revenue. Demand gets more elastic with close substitutes, when the purchase is a large share of the budget and over longer horizons, and less elastic when someone else pays.

In B2B you rarely see a clean demand curve. The "quantity" that responds to price shows up as win rate, sales cycle length, discount depth, usage per account, expansion, downgrades and churn. Those are the numbers to watch.

### The break-even volume test

Before any price change, ask how much volume you can lose (or must gain) for the change to leave contribution flat. The arithmetic is simple, and a harness will run it for every scenario.

- For a **price cut**, the volume increase needed to hold contribution flat equals the cut divided by the contribution margin minus the cut.
- For a **price rise**, the volume loss you can absorb and still break even equals the rise divided by the contribution margin plus the rise.

At a 70% contribution margin, a 10% price cut needs about 16.7% more volume just to stand still (0.10 divided by 0.60). A 10% price rise still breaks even if volume falls by 12.5% (0.10 divided by 0.80). The lower your margin, the more dangerous a cut, which is why lower-margin AI products should be wary of discounting their way to growth.

:::key Ask the break-even question first
Every proposal to cut a price should state the volume increase it needs to pay for itself. Every proposal to raise one should state the volume loss it can absorb. If nobody can say whether that change in volume is plausible, the proposal isn't ready.
:::

### Measuring the impact of a price change

You usually can't run a clean randomized test on prices under contract (Chapter 07 explains why), so measuring a price change means comparing against a baseline and ruling out confounders. Write the hypothesis before the change. Pick a baseline period that covers quarter-end effects, and use a phased rollout by region, segment or channel where that's legal and fair. Watch leading indicators (quote-to-close conversion, win rate, discount depth, sales cycle length, deals lost on price) and lagging ones (recurring revenue, net and gross retention, gross margin, downgrades, churn reasons). Poyar's rule of thumb on the leading side: losing about 20% of deals on price is healthy, far fewer suggests underpricing, and 40% or more is a red flag. Agree guardrails and kill criteria in advance, and list the confounders to check, such as a new competitor, a sales compensation change or one unusually large deal. The price change impact plan in this chapter's artifacts has these sections.

## Discount governance

A list price is a starting point. What the business actually keeps is lower, and the gap is where pricing strategy quietly fails.

Michael Marn and Robert Rosiello's 1992 *Harvard Business Review* article "Managing Price, Gaining Profit" argued that the right price can raise profit faster than more volume can. It's the commonly cited origin of the **pocket price waterfall**. Start at list price. Subtract on-invoice discounts to reach the invoice price. Then subtract everything that leaks out after the invoice: rebates, free months, free services, extended payment terms, credits. What's left is the **pocket price**, the money the business keeps. Plotting pocket prices across deals gives a **pocket price band**, and a wide band often means discounts follow who negotiated hardest rather than any policy.

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 330" role="img" aria-label="Pocket price waterfall: list price minus on-invoice discounts gives invoice price, minus off-invoice leakage gives pocket price">
  <line x1="40" y1="260" x2="650" y2="260" class="ln"/>
  <rect x="60" y="40" width="80" height="220" rx="4" fill="var(--a1)" fill-opacity=".30" stroke="var(--a1)"/>
  <rect x="160" y="40" width="80" height="40" rx="4" fill="var(--a3)" fill-opacity=".22" stroke="var(--a3)" stroke-opacity=".7"/>
  <rect x="260" y="80" width="80" height="180" rx="4" fill="var(--a1)" fill-opacity=".22" stroke="var(--a1)" stroke-opacity=".7"/>
  <rect x="360" y="80" width="80" height="22" rx="4" fill="var(--a3)" fill-opacity=".22" stroke="var(--a3)" stroke-opacity=".7"/>
  <rect x="460" y="102" width="80" height="22" rx="4" fill="var(--a3)" fill-opacity=".22" stroke="var(--a3)" stroke-opacity=".7"/>
  <rect x="560" y="124" width="80" height="136" rx="4" fill="var(--a2)" fill-opacity=".30" stroke="var(--a2)"/>
  <line x1="140" y1="40" x2="160" y2="40" class="ln" stroke-dasharray="3 3"/>
  <line x1="240" y1="80" x2="260" y2="80" class="ln" stroke-dasharray="3 3"/>
  <line x1="340" y1="80" x2="360" y2="80" class="ln" stroke-dasharray="3 3"/>
  <line x1="440" y1="102" x2="460" y2="102" class="ln" stroke-dasharray="3 3"/>
  <line x1="540" y1="124" x2="560" y2="124" class="ln" stroke-dasharray="3 3"/>
  <text x="100" y="280" text-anchor="middle" class="t">List price</text>
  <text x="200" y="280" text-anchor="middle" class="t">On-invoice</text>
  <text x="200" y="296" text-anchor="middle" class="s">discounts</text>
  <text x="300" y="280" text-anchor="middle" class="t">Invoice price</text>
  <text x="400" y="280" text-anchor="middle" class="t">Free months</text>
  <text x="400" y="296" text-anchor="middle" class="s">and credits</text>
  <text x="500" y="280" text-anchor="middle" class="t">Services, terms</text>
  <text x="500" y="296" text-anchor="middle" class="s">and rebates</text>
  <text x="600" y="280" text-anchor="middle" class="t" style="fill:var(--a2)">Pocket price</text>
  <text x="600" y="296" text-anchor="middle" class="s">what you keep</text>
  <text x="345" y="322" text-anchor="middle" class="s">Illustrative proportions. Off-invoice leakage is the part most price books never see.</text>
</svg>
<figcaption>The pocket price waterfall, after Marn and Rosiello. Discount policy has to govern every step, not only the on-invoice discount a rep types into the quote.</figcaption>
</figure>

A discount policy turns that picture into rules: a floor per tier and per unit rate; an approval matrix by discount depth, deal size and non-standard terms; expiry of introductory discounts at renewal; extra scrutiny at quarter-end; and a monthly report of the pocket price band by segment and rep. Two rules matter most.

**Give-get.** Every discount buys something: a longer term, prepayment, a larger commitment, publicity rights, auto-renewal or an automatic annual increase. Poyar's analysis of Common Paper contract data from more than 1,000 companies found that 90% of cloud service agreements include auto-renewal, and that pricing, renewal terms and invoice period are the points most often negotiated. Those are the levers to trade.

**Protect the unit rate.** Discount the package or the commitment, not the price of the value metric, unless the customer commits to volume. A cut unit rate becomes the anchor for every renewal and expansion.

For AI products, cap free pilot credits, give them an expiry date and count free usage as a discount in the waterfall. Free inference is a real cost that a list-price discount report never shows.

:::leader For product leaders
Discount data is product data. A tier that's discounted 40% in most deals is telling you its list price or its contents are wrong. Review the pocket price band with sales and finance every quarter, and treat a widening band as a packaging problem before treating it as a sales discipline problem.
:::

## Pricing AI work in 2026

### Five models

Chapter 31 introduced the main ways to price AI. Here they are with the evidence on how the market uses them.

| Model | Unit | Strength | Weakness | Where it fits |
|---|---|---|---|---|
| **Seat** | Per user per month | Predictable for both sides | Charges less as agents replace work | Copilots that assist people who stay in the loop |
| **Usage** | Per token, call, request or action | Tracks your cost | Hard for buyers to budget; token pricing invites commoditization | Developer platforms and APIs |
| **Credits** | A prepaid pool drawn down at different rates by different actions | One balance covers many actions; the vendor can reprice as model costs change | A black box for buyers; procurement fears runaway spend | Products with many AI actions of different cost and value |
| **Outcome** | Per resolved conversation, completed workflow or other result | Best alignment with value | Needs a clear definition, attribution and audit; the vendor carries performance risk | Agents with reliable performance and a measurable result |
| **Hybrid** | Platform or seat fee plus an allowance, with usage, credits or outcomes on top | Predictable base, value-linked growth | More to explain and meter | Most B2B AI products |

Poyar's 2026 survey of more than 230 B2B software and AI companies found hybrid pricing at 37%, up from 25% a year earlier, and AI credits at 29%, with another third planning to introduce credits within six to twelve months. In a later piece he reported that 76% of AI-native companies use variable or hybrid pricing, against 49% of SaaS companies. Asked which model they prefer, investors in the same survey favored hybrid (35%) and outcome-based (26%) pricing, with seat-based last at 5%.

Manny Medina, writing in Growth Unhinged in 2025, splits agent pricing into **per agent** (a fixed fee, like a hire), **per action**, **per workflow** (a completed multi-step process) and **per outcome**. Outcome pricing, he argues, needs an agent that performs consistently, a clear success metric, a way to attribute the result to the agent and contracts long enough to absorb custom terms.

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 300" role="img" aria-label="AI pricing models placed on two axes: bill predictability for the buyer and alignment of price with value">
  <line x1="70" y1="250" x2="640" y2="250" class="ln"/>
  <line x1="70" y1="250" x2="70" y2="30" class="ln"/>
  <text x="355" y="285" text-anchor="middle" class="s">Alignment of price with customer value: low to high</text>
  <text x="30" y="140" text-anchor="middle" class="s" transform="rotate(-90 30 140)">Bill predictability: low to high</text>
  <rect x="95" y="45" width="120" height="44" rx="8" class="box"/>
  <text x="155" y="72" text-anchor="middle" class="t">Seat</text>
  <rect x="215" y="180" width="120" height="44" rx="8" class="box"/>
  <text x="275" y="207" text-anchor="middle" class="t">Usage</text>
  <rect x="330" y="125" width="120" height="44" rx="8" class="box"/>
  <text x="390" y="152" text-anchor="middle" class="t">Credits</text>
  <rect x="500" y="185" width="120" height="44" rx="8" class="box"/>
  <text x="560" y="212" text-anchor="middle" class="t">Outcome</text>
  <rect x="440" y="50" width="180" height="56" rx="8" fill="var(--a2)" fill-opacity=".18" stroke="var(--a2)"/>
  <text x="530" y="74" text-anchor="middle" class="t" style="fill:var(--a2)">Hybrid</text>
  <text x="530" y="94" text-anchor="middle" class="s">platform fee + outcomes or credits</text>
</svg>
<figcaption>No single unit gives buyers a predictable bill and ties price to value. Hybrids combine a predictable base with a value-linked layer, which is why their share keeps growing. Positions are qualitative.</figcaption>
</figure>

### What the public examples teach

**Outcome pricing needs a definition you could defend in an audit.** Intercom prices its Fin agent from $0.99 per outcome (the 2026 wording on its pricing page), charged once per conversation. An outcome counts when the customer confirms the issue is resolved, when they don't ask for more help after Fin responds, or when Fin completes a defined workflow, including handoffs. The second condition is inferred rather than confirmed, and inferred outcomes are where buyers argue. Zendesk, which launched outcome-based pricing for AI agents in August 2024, publishes a more operational definition: escalated conversations aren't evaluated, a language model reviews each conversation to confirm it was resolved without a human, fixed evaluation windows apply (72 hours after the first email), test activity is excluded and customers get a usage dashboard. According to Metronome, HubSpot moved its Breeze Customer Agent in 2026 from $1 per conversation, regardless of result, to charging only for resolved conversations. Metronome's lesson: price micro-outcomes the vendor controls (a resolved conversation), not macro-outcomes it doesn't (closed revenue).

Put together, an outcome price needs seven parts: a **unit**, **eligibility** rules, **exclusions**, a **verification** method, an **evaluation window**, a **customer-visible audit trail** and a **dispute and credit path**. Zendesk's published pages cover the first six and don't describe the seventh, which is the one your buyer's procurement team will ask about first.

**Value metrics for agents are still being discovered.** Salesforce launched Agentforce at $2 per conversation. In May 2025 it introduced Flex Credits at $500 per 100,000 credits, with 20 credits per action, or $0.10 per action, along with an agreement that lets customers shift budget between user licenses and credits. The same announcement scheduled per-user licenses for employee-facing agents for later that year. Within about a year, Salesforce had put conversation, action and per-user units in front of customers. Expect your own unit to move too, and design the contract so it can.

**Credits blend two kinds of logic.** Poyar defines credits as a pooled, prepaid allowance drawn down by different actions at different rates. Metronome sees credits doing three jobs: a proxy for compute cost, a single balance for many kinds of value, and a gate on premium usage within a tier. Poyar's critique, in March 2026, is that credits often mix value-based logic (pay for work done) with cost-based logic (pay for the vendor's model bill), so buyers can't judge whether they're getting value. In his 2026 survey report he put it more bluntly: credits "are great for vendors. They can become a nightmare for customers." If you use credits, publish the rate card, keep it stable and show customers their burn rate.

**Spend controls are part of the product.** In June 2025 Cursor moved its Pro plan from 500 requests a month to a $20 monthly usage pool at API prices, with unlimited use of its Auto model. In its own account on July 4, 2025, the company said it hadn't made clear that "unlimited" applied only to Auto, and that a poorly communicated rollout led to surprise charges. It apologized and refunded unexpected charges incurred between June 16 and July 4. The failure was in how the units were named and communicated, and in the missing warnings before charges landed, more than in the price.

GitHub Copilot's premium requests show the controls done carefully. Each plan includes a monthly allowance (300 premium requests on Copilot Pro, 1,500 on Pro+). Extra requests cost $0.04 each, but only if the customer has set a budget for them, and when the allowance runs out, users fall back to included models instead of hitting a wall. Metronome's checklist for hybrid AI pricing adds low-balance alerts, caps per user, department or project, a real-time burn-rate dashboard, a rule on rollover and an explicit overage policy: stop at zero, or finish the task and bill afterward.

:::ai Metering is now infrastructure
In January 2026 Stripe completed its acquisition of Metronome, a usage and credit billing company. A major payments company buying a usage billing specialist is a sign that metering and credit billing are becoming standard infrastructure you can buy. The hard part left for the PM is product: which unit, what definition, what the customer sees and what happens at the limit.
:::

## How to apply it

Poyar describes a pricing project in four phases: set the strategy, validate with research, prepare the implementation and follow through after launch. Here's that sequence as a method for a new pricing model or a major repricing, over roughly a quarter.

**Phase 1: Strategy (weeks 1 to 3).**

1. **State the objective:** acquisition, revenue or margin; new logos or expansion. The answer changes every later choice.
2. **Diagnose today's pricing:** the pocket price band, discount depth by segment, deals lost on price, gross margin per unit of the current metric and the cost of serving your heaviest users. Name the Monetizing Innovation failure you're closest to.
3. **Score candidate value metrics** against the seven tests, and draft two or three model options with a hypothesis for each.

**Phase 2: Research (weeks 3 to 7).**

4. **Run 15 to 30 WTP conversations** across segments, with economic buyers, lost prospects and churned customers as well as users.
5. **Add structured research where the sample allows:** MaxDiff to sort features and add-ons, Van Westendorp or Gabor-Granger on price points, conjoint if you can reach enough comparable buyers.
6. **Interview your own sellers and customer success managers** about where deals stall and which terms they give away.

**Phase 3: Design and prepare (weeks 7 to 11).**

7. **Build the packages** from segments and research, with leaders in every tier.
8. **Write the outcome definition,** with all seven parts, if any part of the price depends on one.
9. **Specify metering and spend controls** as product requirements: what's logged, what customers see, alerts, caps and the overage policy.
10. **Model every existing account under the new price,** as Poyar recommends. Flag accounts whose bill moves beyond a set threshold, and decide grandfathering, migration offers and notice.
11. **Write the discount policy and the price change impact plan,** with kill criteria, and get sign-off from finance and sales.

**Phase 4: Launch and follow through (week 12 onward).**

12. **Shadow-bill first:** show customers what they would have paid for one to three months before charging them.
13. **Enable sales and customer success** (Chapter 27) with the definition, the controls and the talk track.
14. **Review the impact plan** at 30, 90 and 180 days, and take the kill or revise decision on schedule.

## The AI lens

### When the product is AI-powered

**Price from value, floor at cost.** Use the cost model and margin floor from Chapter 31 as the floor and Chapter 12's economic value to the customer as the ceiling. Poyar's survey found a median target AI gross margin of about 50%, with only 12% of companies aiming for 80% or more. Agree your target with finance before you choose a unit, because outcome units leave you carrying cost risk and usage units hand it to the customer.

**Expect model costs to move your rate card.** When a provider changes its prices, or a new model doubles the tokens per task, the cost per unit of your value metric changes overnight. Credits and outcome prices let you absorb that without repricing customers, but only if your contract doesn't fix the cost assumptions. Review gross margin per unit of value metric monthly.

**Make trust a pricing term.** For an agent that acts, customers will ask who pays when it's wrong. A published policy that waives charges and credits the customer when the agent causes harm turns a trust problem into a contract term, and answers a question both the security reviewer and the CFO will ask. Chapter 33 covers the wider responsibility questions.

**Treat your MCP server and API as priced surfaces.** When customers' own agents call your product, the caller is software. Decide which calls are included, which are metered and what rate limits apply, before an agent somewhere runs ten thousand calls on a flat fee.

### Doing the work with AI

A harness connected to your CRM, billing system, product analytics and call recordings does pricing's mechanical work in minutes. It can turn WTP transcripts into a range and metric preference per segment with quotes as evidence, score value metrics, rerun break-even arithmetic, model every account's bill under a new price, and compare win rate, discount depth and cycle length before and after a change. Chapter 19 covers how to ask those questions well.

Three cautions. Customer, contract and pricing data are confidential, so use only approved tools. Simulated respondents can help you find confusing survey questions, but they aren't willingness-to-pay evidence (Chapter 01 covers synthetic users). And a model will happily produce a precise-looking elasticity from a handful of deals, so ask for the sample size behind every number and what else changed in the same period.

## The Beacon case: pricing Beacon Agents per resolved incident

:::example Where Beacon starts
Beacon charges a platform fee per environment plus usage, and leadership wants a per-resolved-incident price for Beacon Agents at launch. Gross margin has fallen from 81% to 72% since agentic features launched, against the 70% floor set in Chapter 31. Chapter 12 proposed an illustrative price for one design partner: a $60,000 platform fee plus $100 per resolved incident. Your job now is to turn that into a pricing and packaging proposal that finance, sales, Sam's security team and Leo's MSP channel can all accept. All research results and figures below are illustrative.
:::

**Why per-environment pricing has to change.** One environment can produce five incidents a year or five hundred. The price doesn't track the value Marcus gets, and it doesn't track Beacon's cost, which rises with every diagnosis and action. So inference cost can climb while revenue stays flat, which is how margin fell. The unit that matches both the North Star (incidents resolved with Beacon's help per week) and the cost driver is a resolved incident.

**The value metric assessment.** The trio scores five candidates against the seven tests.

| Candidate metric | Tracks value | Encourages adoption | Start small | Grows | Meterable | Budgetable | Hard to dispute |
|---|---|---|---|---|---|---|---|
| Environments | Low | High | Medium | Low | High | High | High |
| Alerts ingested | Low | Low (punishes noisy estates) | Medium | High | High | Low | High |
| Actions executed | Medium | Low (rewards activity) | High | Medium | High | Low | High |
| Credits | Medium | Medium | High | Medium | High | Medium | Medium |
| Incidents resolved | High | High | High | Medium | Medium | Medium | Low |

Incidents resolved wins on value and adoption and loses on predictability and dispute risk; environments is the reverse. The recommendation is a hybrid: a platform fee per environment for predictable revenue, and a per-resolved-incident layer for Agents, with an annual commitment and a monthly minimum.

**The research.** You run 22 WTP conversations: economic buyers like Marcus and SRE leads like Priya at direct enterprise customers, three MSPs including Leo, and four EU customers. Buyers like paying for outcomes but every one of them asks for a cap or a commitment ("I can't take an open-ended number to my CFO"). Van Westendorp questions on price per resolved incident give an acceptable range that comfortably contains $100. A short MaxDiff exercise on add-ons puts the EU AI Act documentation pack first for EU customers and the multi-tenant console first for MSPs; both become add-ons rather than tier features. The MSPs reject discounts as a margin mechanism and ask for a wholesale rate.

**The packages.** Correlate and Diagnose sit in the platform fee in three tiers, with SSO and advanced admin as leaders in the top tier. Beacon Agents is the outcome layer. Audit logs, scoped credentials and the kill switch ship wherever Agents ships, in every tier: you refuse to make the controls Sam needs to approve an agent an upsell. Leo gets per-tenant metering and invoicing at a wholesale rate.

**The outcome definition.** You build on the definition from Chapter 31 and write all seven parts. *Unit:* one incident. *Eligibility:* Beacon correlated the incident, and a responder accepted Beacon's diagnosis or an approved Beacon action completed. *Exclusions:* rejected diagnoses, incidents reopened within 24 hours, actions rolled back, test and sandbox environments and incidents later merged as duplicates. *Verification:* an evidence record per incident (diagnosis, acceptance, action log, closure). *Window:* 24 hours after closure. *Audit trail:* every billed incident is visible in a customer dashboard. *Disputes:* customers can flag an incident within 30 days, and upheld disputes are credited.

**The agent-caused incident policy.** The hallucinated root cause that led a customer to roll back the wrong service shapes one clause. If a Beacon action or an accepted wrong diagnosis causes or extends an incident, neither the original nor the follow-on incident is billable, and the customer receives a service credit. That answers the question Marcus's CFO asked in Chapter 31: who pays when the agent makes things worse?

**Spend controls.** Each customer commits to an annual pool of resolved incidents. Alerts go to the account admin at 75%, 90% and 100% of the commitment. Caps can be set per business unit. Beacon never stops mid-incident: overage is billed after the incident closes, at the contracted rate, up to an agreed ceiling. The pricing page and quotes say "one resolved incident" and never "unlimited."

**The break-even conversation.** Sales asks for authority to cut the per-incident rate 10% for large deals. At the 70% margin floor, a 10% cut needs about 16.7% more resolved incidents to hold contribution flat. But the number of resolved incidents is set by the customer's incident rate and Beacon's resolution rate, not by price, so a lower rate buys almost no extra volume. The discount policy says so: deeper discounts only for larger commitments or multi-year terms, never on the unit rate alone, and pilot credits that expire after 60 days.

**The impact plan.** Existing per-environment contracts are honored until renewal, migrating customers get 12 months of price protection, and design partners are shadow-billed for three months before any charge. You track gross margin per resolved incident against the 70% floor, win rate, discount depth, net revenue retention against today's 118%, deals lost on price and disputes per 1,000 billed incidents. Finance agrees the kill-or-revise triggers before launch: a dispute rate above a set threshold, or a fall in win rate beyond a set band.

## Product 360 artifacts

```template id="15-pricing-packaging-proposal" title="Pricing and packaging proposal"
# Pricing and packaging proposal · [Product] · v[n] · [Date]

**Owner:** [PM]   **Finance partner:** [Name]   **Sales or deal desk partner:** [Name]   **Decision maker:** [Name]   **Decision needed by:** [Date]

## 1. Objective
What this pricing optimizes for: acquisition / revenue / margin; new logos / expansion. One paragraph on why now.

## 2. Diagnosis of current pricing
- Current model and value metric:
- Pocket price band by segment (from the discount report):
- Share of deals lost on price (last two quarters):
- Gross margin per unit of current value metric, and the trend:
- Monetizing Innovation failure we're closest to: feature shock / minivation / hidden gem / undead. Evidence:

## 3. Segments
| Segment | Needs | Willingness to pay (evidence) | Budget line that pays | Preferred way to pay |
|---|---|---|---|---|
| | | | | |

## 4. Value metric
Chosen metric: [unit]. Runner-up: [unit]. See the value metric assessment.

## 5. Model
Seat / usage / credits / outcome / hybrid. Structure: [platform fee, included allowance, metered layer, commit, minimum].

## 6. Packages
| | [Tier 1] | [Tier 2] | [Tier 3] |
|---|---|---|---|
| Designed for (segment) | | | |
| Leaders (why they buy this tier) | | | |
| Fillers | | | |
| Included allowance | | | |
| List price | | | |

Add-ons (narrow, intense demand): [name, price, who buys it]
Removed or moved (killers): [feature, reason]
Included in every tier on principle (for example, safety or compliance controls): [list]

## 7. Price points and evidence
| Price point | Research method | Sample | Result | Confidence |
|---|---|---|---|---|
| | | | | |

## 8. Unit economics
Cost per unit of value metric: [amount, date]. Gross margin at list: [%]. At typical discount: [%]. Margin floor: [%].

## 9. Outcome definition (if any)
Link to the outcome definition artifact.

## 10. Metering and spend controls
What's logged, what customers see, alerts, caps, overage policy, rollover.

## 11. Migration of existing customers
Accounts modeled: [n]. Bills up more than [x]%: [n]. Bills down more than [x]%: [n]. Grandfathering, notice and migration offers:

## 12. Discount policy and impact plan
Links to both. Kill or revise criteria in one line.

## 13. Decision
Approved / revise / rejected, by [name] on [date].
```

```template id="15-value-metric-assessment" title="Value metric assessment"
# Value metric assessment · [Product] · [Date]

Score each candidate High / Medium / Low on each test, with one line of evidence per score.

| Test | [Metric A] | [Metric B] | [Metric C] | [Metric D] |
|---|---|---|---|---|
| 1. Correlates with the value different customers get | | | | |
| 2. Shares in customer success; doesn't discourage adoption | | | | |
| 3. Lets customers start small and grow | | | | |
| 4. Grows over time for the average customer | | | | |
| 5. Feasible to monitor and meter accurately | | | | |
| 6. Predictable enough for procurement to budget | | | | |
| 7. Hard to dispute or game | | | | |
| Tracks our cost to serve | | | | |
| Fits the North Star metric | | | | |

Tests 1 to 5 follow Kyle Poyar's value metric criteria. Tests 6 and 7 are B2B additions.

## Behavior check
For each finalist: what will customers do to keep the bill down, and is that behavior good or bad for them and for us?

## Recommendation
Primary metric: [ ]. Predictability layer (if hybrid): [ ]. Why:

## What the product must build to meter it
[Events logged, data retained, customer-visible reporting]
```

```template id="15-wtp-interview-guide" title="Willingness-to-pay interview guide"
# Willingness-to-pay interview guide · [Product or concept] · [Date]

**Interviewee:** [role; economic buyer preferred]   **Segment:** [ ]   **Length:** 45 minutes   **Interviewers:** [PM plus one]

## Rules
Don't name a price first. Don't pitch before you ask. Ask about current costs in their numbers. Never ask "what would you pay?" cold.

## 1. Context (10 min)
- "Walk me through the last time [problem] happened. What did it cost: hours, people, tools, penalties?"
- "What do you use or pay for today to deal with it?"

## 2. Value (10 min)
- Show the capability list. "If you could keep only three, which?" "Which could you live without?"

## 3. Metric (5 min)
- "How would you expect to pay for something like this: per user, per environment, per [unit of work], per outcome?"
- "What would make a bill for this feel unfair?"

## 4. Range (5 min, after showing the concept)
- "At what price would this seem so cheap you'd doubt it works?"
- "At what price would it feel like a bargain?"
- "At what price would it start to feel expensive, but still worth considering?"
- "At what price would it be too expensive to consider?"

## 5. Point check (5 min)
- "At [price] per [unit or year], would you buy?" Move up or down depending on the answer.

## 6. Budget and buying (5 min)
- "Which budget would this come from: software, services or headcount?"
- "Who approves it? At what amount does procurement get involved?"

## 7. Predictability (5 min)
- "Would you rather have a fixed commitment, a cap, or pay as you go? Why?"

## After the call
| Field | Answer |
|---|---|
| Current cost of the problem (their numbers) | |
| Top three capabilities | |
| Preferred metric; unfair-bill triggers | |
| Range: too cheap / bargain / expensive / too expensive | |
| Point check result | |
| Budget line and approver | |
| Commit, cap or pay-as-you-go | |
| Memorable quote (verbatim) | |
```

```template id="15-outcome-definition" title="Outcome definition for outcome-based pricing"
# Outcome definition · [Product] · v[n] · [Date]

**Owner:** [PM]   **Reviewed by:** finance, legal, customer success, [customer advisory board]

1. **Unit.** One [conversation / incident / workflow / document] counts once, however many steps it takes.
2. **Eligibility.** The conditions under which a unit can be billed: [what the product must have done; what the customer must have confirmed or not contested].
3. **Exclusions.** Never billed: [escalated to a human; reopened within [window]; actions rolled back; test and sandbox; duplicates; other].
4. **Verification.** How we decide: [evidence record, automated review, human confirmation]. What the customer can see of it:
5. **Evaluation window.** The outcome is final [time] after [event].
6. **Audit trail.** Every billed unit appears in [dashboard or export] with its evidence, within [time].
7. **Disputes and credits.** Customers can dispute within [days]. Upheld disputes are credited on the next invoice. Target dispute rate: under [n] per 1,000 billed units.
8. **Harm clause.** If our product causes or worsens the outcome it's paid for: [not billable; follow-on not billable; service credit of [amount]].
9. **Macro-outcomes we deliberately don't price,** because we don't control them: [list].

## Worked examples
| Scenario | Billable? | Why |
|---|---|---|
| | | |
```

```template id="15-price-change-impact-plan" title="Price change impact plan"
# Price change impact plan · [Change] · [Date]

**Owner:** [PM]   **Analyst or harness owner:** [Name]   **Finance partner:** [Name]

## Hypothesis
We expect [change] to move [metric] by [amount] in [segment] within [time], because [reason].

## Break-even
- Contribution margin today: [%]
- For a cut: volume increase needed = cut ÷ (margin − cut) = [%]
- For a rise: volume loss we can absorb = rise ÷ (margin + rise) = [%]
- Is that volume change plausible? Evidence:

## Scope and rollout
New logos / renewals / expansions. Segments, regions and channels. Phased rollout or holdout: [design, and why it's fair and legal].

## Baseline
Period: [dates]. Known seasonality and quarter-end effects:

## Indicators
| Type | Metric | Baseline | Expected | Guardrail |
|---|---|---|---|---|
| Leading | Quote-to-close conversion | | | |
| Leading | Win rate | | | |
| Leading | Discount depth | | | |
| Leading | Sales cycle length | | | |
| Leading | Deals lost on price (share) | | | |
| Leading | Bill-shock tickets or disputes | | | |
| Lagging | ARR and gross margin | | | |
| Lagging | Net and gross revenue retention | | | |
| Lagging | Downgrades and churn reasons | | | |

## Confounders to check
[New competitor, sales compensation change, product release, large deals, macro events]

## Existing customers
Grandfathering rule: [ ]. Notice period: [ ]. Price protection: [ ]. Accounts needing a personal conversation: [list].

## Kill or revise criteria
We revise if [condition]. We roll back if [condition]. Decided by [name].

## Reviews
30 days: [date]. 90 days: [date]. 180 days: [date].
```

```template id="15-discount-policy" title="Discount policy"
# Discount policy · [Product] · [Effective date]

**Owner:** [Deal desk lead]   **Product owner:** [PM]   **Finance owner:** [Name]

## Price book
| Item | List price | Floor | Notes |
|---|---|---|---|
| [Tier] | | | |
| [Value metric unit rate] | | | Discounted only with a volume commitment |

## Approval matrix
| Discount depth or term | Rep | Manager | Deal desk | Finance or CRO |
|---|---|---|---|---|
| Up to [x]% | ✓ | | | |
| [x] to [y]% | | ✓ | | |
| [y] to [z]% | | | ✓ | |
| Above [z]%, or any non-standard term | | | | ✓ |

## Give-get list (every discount buys something)
Multi-year term · prepayment · larger commitment · case study or publicity rights · auto-renewal · automatic annual increase · reference calls

## Rules
1. Discount the package or commitment, not the unit rate, unless volume is committed.
2. Introductory discounts expire at first renewal. Renewal uplift: [%].
3. Free pilot credits are capped at [amount] and expire after [days]. They count as discounts in the pocket price report.
4. Partner margin comes from a wholesale rate, not ad hoc discounts.
5. Quarter-end: deals above [x]% discount in the last [n] days of the quarter need [approver].

## Reporting
Monthly pocket price band by segment, tier and rep. Quarterly review with product, sales and finance. A tier discounted more than [x]% in most deals triggers a packaging review.
```

```template id="15-ai-pricing-model-comparison" title="AI pricing model comparison"
# AI pricing model comparison · [Product or AI capability] · [Date]

## Inputs
- What the buyer values, and whether it can be measured and attributed:
- Our cost per unit of work today, and its variability:
- How predictable the bill must be (procurement's view):
- Which budget pays: software / services / headcount:
- Our confidence in consistent performance (eval results):
- Can the customer audit the count?

## Comparison
| Criterion | Seat | Usage | Credits | Outcome | Hybrid |
|---|---|---|---|---|---|
| Unit | | | | | |
| Alignment with customer value | | | | | |
| Tracks our cost | | | | | |
| Bill predictability for the buyer | | | | | |
| Revenue as agents replace work | | | | | |
| Who carries performance risk | | | | | |
| Who carries model-cost risk | | | | | |
| Dispute risk | | | | | |
| Metering we'd need to build | | | | | |
| Gross margin at expected volume | | | | | |
| Competitor and market norm | | | | | |

## Spend controls required for the chosen model
Included allowance · alerts at [thresholds] · caps by [user, team, project] · overage policy (stop or finish and bill) · fallback behavior · rollover or expiry · burn-rate dashboard · plain-language unit names

## Recommendation
Model: [ ]. Why: [ ]. What would make us change it: [ ]. Review date: [ ].
```

## Prompts

```prompt title="Synthesize willingness-to-pay interviews by segment"
Goal: Turn a set of WTP conversations into price ranges and metric preferences you can defend, with the evidence attached.
Paste in: the interview transcripts or notes, the segment of each interviewee and the concept or prices shown. These are confidential customer conversations, so use an approved tool and remove personal identifiers first.

You are analyzing willingness-to-pay interviews for [product]. For each segment:

1. Summarize the current cost of the problem in the interviewees' own numbers, with a quote and interview ID for each.
2. Rank the capabilities they valued most and least.
3. List the value metrics they expected to pay by, and what they said would make a bill feel unfair.
4. Report the range answers (too cheap, bargain, getting expensive, too expensive) as a spread across interviewees, not as one average. State the number of interviewees behind each figure.
5. Report budget source, approver and preference for commit, cap or pay-as-you-go.
6. Flag contradictions between what users and economic buyers said.

Don't extrapolate to segments with fewer than [n] interviews; mark them "insufficient evidence."

Check the output: open three cited interviews and confirm the quotes. Check that every range shows its sample size. A precise price from five interviews is a hypothesis, not a finding.
```

```prompt title="Score candidate value metrics"
Goal: Choose the unit your price scales with by testing candidates against explicit criteria.
Paste in: a description of the product and what customers get from it, three to six candidate metrics, any usage distribution data you have (for example, how the metric varies across accounts) and your cost drivers.

Assess these candidate value metrics for [product]: [list].

Score each High, Medium or Low on these tests, with one sentence of reasoning per score:
1. Correlates with the value different customers get.
2. Shares in customer success and doesn't discourage adoption.
3. Lets customers start small and grow.
4. Grows over time for the average customer.
5. Feasible to monitor and meter accurately.
6. Predictable enough for procurement to budget.
7. Hard to dispute or game.
Then add: does it track our cost to serve, and does it fit our North Star metric: [metric]?

For the top two, describe what customers will do to keep their bill down, and whether that behavior hurts them or us. Recommend a single metric or a hybrid, and list what the product must log to meter it.

Check the output: challenge every "High" on test 1 by asking for the evidence. If the model can't name customers who get more value and would pay more under the metric, downgrade it.
```

```prompt title="Model existing accounts under a new price"
Goal: See who wins and who loses before you announce a pricing change.
Paste in (or connect the harness to): an export of current accounts with their current bill, usage of each candidate metric over the last 12 months, segment, renewal date and account owner. This is confidential commercial data; use an approved tool only.

For each account, calculate the annual bill under the current pricing and under the proposed pricing: [describe the new model, including allowances, commitments, minimums and rates].

Then:
1. Show the distribution of bill changes by segment.
2. List every account whose bill would rise more than [x]% or fall more than [y]%, with its renewal date and owner.
3. Total the revenue effect in year one and at full migration.
4. Suggest which accounts need grandfathering, price protection or a personal conversation, and why.
5. List the assumptions you made and any accounts with missing data.

Show how you calculated one example account step by step.

Check the output: recompute two accounts by hand, including one large account. Confirm that accounts with missing usage data weren't silently treated as zero.
```

```prompt title="Read the impact of a price change"
Goal: Find out what a price change actually did, separating its effect from everything else that happened.
Paste in (or connect the harness to): quotes, opportunities and closed deals for [n] days before and after the change, with segment, discount, cycle length, outcome and loss reason; the date and scope of the change; and the price change impact plan.

Compare the period before and after [change] on [date], by segment:
1. Win rate, average discount depth, sales cycle length, deal size and the share of losses coded as price.
2. For existing customers: expansion, downgrades and churn, with churn reasons.
3. Gross margin per unit of the value metric.

For each metric, give the sample size and say whether the difference is large enough to take seriously given that sample.

Then list other changes in the same period that could explain the results (competitor moves, sales compensation, product releases, unusually large deals, seasonality) and say how each would bias the comparison. Finally, compare the results with the guardrails and kill criteria in the plan.

Check the output: check that "lost on price" reasons match a sample of call notes, because price is the easiest reason for a buyer to give. Don't accept a conclusion that rests on a handful of deals.
```

```prompt title="Audit discounting with a pocket price view"
Goal: See where list price leaks away and whether discounts follow policy.
Paste in (or connect the harness to): closed deals for the last four quarters with list price, invoice price, every off-invoice concession (free months, credits, services, payment terms, rebates), segment, tier, rep, close date and the discount policy. Confidential; approved tools only.

For [product]:
1. Build a pocket price waterfall for the average deal in each segment: list, on-invoice discount, invoice price, each off-invoice leakage and pocket price.
2. Show the pocket price band: the spread of pocket price as a share of list, by segment and tier.
3. Identify deals that broke the discount policy, and the share closed in the last two weeks of a quarter.
4. Check whether larger discounts came with give-gets (longer term, prepayment, larger commitment, publicity rights).
5. Flag any tier discounted beyond [x]% in most deals as a possible packaging problem.

Check the output: trace two deals end to end against the contract. Confirm that free credits and pilot usage were counted as leakage rather than ignored.
```

```prompt title="Red-team an outcome definition"
Goal: Find the disputes, loopholes and perverse incentives in an outcome price before customers do.
Paste in: your draft outcome definition (unit, eligibility, exclusions, verification, window, audit trail, disputes, harm clause) and a description of how the product works.

Act in turn as three reviewers of this outcome definition for [product]:
1. A customer's procurement lead trying to minimize the bill. Find every case where they could argue an outcome shouldn't count.
2. Our CFO. Find every case where we'd do the work and fail to get paid, or where cost could exceed revenue.
3. An end user. Find any way the definition rewards the product for behavior that's bad for them (for example, closing incidents early or splitting one incident into several).

For each issue, propose a specific rewrite. Then write ten worked examples, including edge cases, with "billable" or "not billable" and the clause that decides it.

Check the output: give the worked examples to a colleague in customer success without the answers. Every case they decide differently is a clause to rewrite.
```

```prompt title="Pre-launch review of AI pricing communication and spend controls"
Goal: Avoid a surprise-bill backlash by testing what customers will read and experience.
Paste in: the draft pricing page, the announcement, the in-product usage screens or their specs, the spend-control design and the overage policy.

Review this AI pricing launch for [product] from a customer's point of view.
1. List every term a customer could misread, including "unlimited," "fair use," "credits," "requests" and any unit names. Propose plain-language replacements.
2. Walk through the first month for a light, a typical and a heavy user. Where would each first learn they're being charged more than expected?
3. Check for: an included allowance, alerts before limits, caps by user or team, an explicit overage policy, fallback behavior at the limit, a burn-rate view, notice to existing customers and a refund or credit path.
4. Draft the three questions most likely to show up in support tickets in week one, with answers.

Check the output: have someone outside the team read the pricing page for two minutes and explain what they'd pay. If their answer differs from yours, rewrite the page.
```

## Anti-patterns

:::warn Pricing in launch week
The product is built, the launch is booked and someone asks what it should cost. Packaging follows the code structure and the unit follows the billing system. Have the willingness-to-pay conversation during discovery, and let the target price shape what gets built.
:::

:::warn The cost-plus agent
An agent that saves customers hours of skilled work gets priced at token cost plus a markup. It's a minivation: the product is right and the revenue never arrives. Cost is the floor. Price from the customer's value.
:::

:::warn A metric that punishes adoption
Charging per alert ingested or per action executed means the customers who use the product most, or whose estates are noisiest, pay the most for the same value. They respond by rationing use. Test every metric against "does this discourage the behavior we want?"
:::

:::warn The undefined outcome
"We charge per resolution" with no written eligibility rules, exclusions, window or dispute path. The first large customer disputes a month of invoices and the sales team starts issuing credits by hand. Write all seven parts of the outcome definition before the first contract.
:::

:::warn Credits as a black box
A credit pool with a rate card nobody can find, changed whenever model costs move. Customers can't tell what they're paying for, and procurement caps the contract. Publish the rate card, keep it stable and show the burn rate.
:::

:::warn "Unlimited" with an asterisk
Marketing calls the plan unlimited; the terms limit it. Customers find out on the invoice. Name units plainly, turn on alerts by default and refund surprises quickly.
:::

:::warn Discounting the unit rate
A rep cuts the per-unit price to close a quarter-end deal. That rate becomes the anchor for every renewal and expansion. Discount the commitment or the package, and get something for it.
:::

:::warn Survey results as an oracle
A Van Westendorp chart from 30 respondents becomes the price. B2B samples are small, and the people who answer surveys aren't always the people who sign. Triangulate research with deal data, win and loss reasons and the pocket price band.
:::

## Checklist

- [ ] Willingness-to-pay questions are part of discovery for every major concept, with economic buyers as well as users.
- [ ] The pricing objective (acquisition, revenue or margin; new logos or expansion) is written down and agreed with finance.
- [ ] Candidate value metrics have been scored against all seven tests, and the product can meter the chosen one.
- [ ] Every tier is designed for a named segment and has at least one leader; killers are removed or moved to add-ons.
- [ ] Price points rest on more than one research method, and every figure shows its sample size.
- [ ] Every proposed price change states its break-even volume.
- [ ] For AI capabilities, gross margin per unit of the value metric is tracked monthly against a floor.
- [ ] Any outcome-based price has a written definition covering unit, eligibility, exclusions, verification, window, audit trail, disputes and harm.
- [ ] Spend controls (allowance, alerts, caps, overage policy, fallback, burn-rate view) are product requirements with owners.
- [ ] Safety and compliance controls that customers need to adopt the product aren't sold as upsells.
- [ ] Every existing account has been modeled under the new price, with grandfathering and notice decided.
- [ ] A discount policy with an approval matrix, a give-get list and a protected unit rate is in force, and the pocket price band is reviewed quarterly.
- [ ] A price change impact plan with guardrails, confounders and kill criteria was agreed before launch.
- [ ] The pricing is reviewed at least every six months.

## Key takeaways

- Set price early. Willingness-to-pay evidence collected in discovery should shape what gets built and how it's packaged; Ramanujam and Tacke's four failure types name what happens when it doesn't.
- The value metric is the most consequential pricing decision. Test it for value, adoption, growth, meterability, predictability and dispute risk; most B2B AI products need a hybrid to satisfy all of them.
- Build packages from segments. Put leaders in every tier, move narrow needs to add-ons and use MaxDiff, Van Westendorp, Gabor-Granger and conjoint as inputs to triangulate with deal data.
- Before any price change, calculate the break-even volume, then measure the result against a baseline with guardrails, confounders and kill criteria agreed in advance.
- Discounts leak through every step of the pocket price waterfall. Govern them with an approval matrix and give-gets, and protect the unit rate.
- Outcome pricing for agents works only with a definition you could defend in an audit, including a dispute path and a clause for when the agent causes harm, and with spend controls customers can see before the invoice arrives.
