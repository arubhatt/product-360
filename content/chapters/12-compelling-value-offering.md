<p class="lead">A value offering is the claim that your product leaves a customer better off by more than it costs them, stated in terms the customer can check. This chapter shows you how to build that claim from evidence: what the customer is trying to get done, what their next best alternative costs, how much better you are in money terms, what the investment is worth to your own company, and how the price should move as the product ages.</p>

## Why this matters

Many B2B products are priced by habit. Someone looks at a competitor's price page, adds a margin to a cost estimate, or carries last year's list price forward with a small increase. Then sales discounts until deals close. Nobody can say what the product is worth to a specific customer, so nobody can defend the price when procurement pushes, and the discount becomes the real price.

The habit is common. Andreas Hinterhuber, pooling earlier pricing surveys in a 2008 review, found that only about 17% of firms set prices mainly on customer value; the rest leaned on cost or on competitors. Price from cost and you cap revenue at whatever your engineering happened to cost. Price from competitors and you inherit their mistakes. Either way you leave value on the table, or charge for value the customer doesn't believe in and lose the deal.

The problem is getting sharper in 2026. AI products carry real marginal costs again (inference, retrieval, evaluation), while the cost of a given level of model capability keeps falling fast. Buyers are also more skeptical. In June 2025 Gartner predicted that more than 40% of agentic AI projects would be canceled by the end of 2027, and named unclear business value as one of the causes. An AI product without a credible customer value model is a cancellation candidate, however capable the AI behind it.

Finance owns the hurdle rate, sales owns the negotiation and a pricing team, where one exists, owns the price book. The Principal PM owns the chain that connects them: which customer job the product does, what the customer would do instead, how much better the product is in money terms, and whether the investment pays back for your company. This chapter covers that chain, and produces five artifacts: a value proposition canvas per buying-group role, an economic value model, a customer ROI calculator spec, an investment case and a lifecycle pricing plan. Chapter 15 goes deeper on packaging and price metrics, and Chapter 13 on market sizing and the full business case.

## The value proposition canvas

### Customer profile and value map

Alexander Osterwalder and his Strategyzer co-authors introduced the **value proposition canvas** in *Value Proposition Design* (2014). It has two halves that you fill in separately and then compare.

The **customer profile**, drawn as a circle, describes one customer segment:

- **Jobs**: what the customer is trying to get done. These can be functional (restore the service), social (look competent to leadership) or emotional (stop dreading the pager).
- **Pains**: bad outcomes, obstacles and risks around the job.
- **Gains**: outcomes and benefits the customer wants, from the ones they require to the ones that would surprise them.

The **value map**, drawn as a square, describes your offer:

- **Products and services**: what you actually sell.
- **Pain relievers**: how the offer removes or reduces specific pains.
- **Gain creators**: how the offer produces specific gains.

**Fit** is the claim that your pain relievers and gain creators address the pains and gains that matter most to this segment. Strategyzer is explicit that fit is a claim until customers confirm it. The canvas is a hypothesis, which is why it belongs next to the product hypothesis from Chapter 01 and gets tested the same way.

Two practices make the canvas useful. First, rank the jobs, pains and gains by importance, and write each pain and gain in a measurable form ("waits 40 minutes for the right expert to join the call" instead of "slow escalations"). Second, tag every pain reliever and gain creator to the pain or gain it addresses. An untagged feature is looking for a customer.

### One canvas per buying-group role

The standard canvas assumes one customer. In enterprise software, a deal has several. Chapter 01 introduced the B2B buying group: end user, champion, economic buyer, technical evaluator, procurement. Each has different jobs, and a product that fits one role perfectly can fail on another.

Draw one canvas per role, not one per account. The end user's canvas tells you what makes the product worth using. The economic buyer's canvas tells you what makes it worth paying for, and their gains (lower cost, more output per head, less risk) become the inputs to your economic value model. The technical evaluator's pains (privileged access, audit, regulatory paperwork) are often the binding constraint: no amount of user delight survives a security veto. If you sell through partners, the partner needs a canvas too, and its central gain is margin.

:::key The economic buyer's gains are the bridge to price
The end user's canvas explains adoption. The economic buyer's canvas explains willingness to pay. When you move from the canvas to the value model, start from the economic buyer's ranked gains and express each one in money.
:::

## Economic value to the customer

### Reference value plus differentiation value

The canvas tells you what the customer values. **Economic value to the customer** (EVC) tells you how much. Thomas Nagle and Georg Müller, in *The Strategy and Tactics of Pricing* (Evert Gruyaert joined them for the 2023 seventh edition), call the method economic value estimation (EVE); MIT's pricing course teaches the same idea under the older EVC label. The logic is short.

A rational customer buys your product only if the value they get, minus your price, is at least as good as the value they'd get from their next best alternative, minus its price. Rearranged, that sets a ceiling on your price:

> EVC = reference value + differentiation value

- **Reference value** is the price of the customer's **next best alternative**: the option they'd actually choose if you didn't exist. It might be a competitor, an internal tool, a services contract, or people doing the work by hand.
- **Differentiation value** is the money value of every way you differ from that alternative. Some differences are positive (fewer hours, less downtime, more revenue). Some are negative (switching effort, training, risk that the new thing fails). Both go in the model.

EVC is a ceiling, not a price. At EVC the customer is indifferent between you and the alternative, so they have no reason to switch. Your price has to sit below it, leaving part of the differentiation value with the customer as their incentive to buy.

MIT's teaching note works this through with a fictional computer maker. The product was worth $6,000 more than the competitor's over its life ($4,000 in labor, $500 in electricity, $1,500 in licenses). The competitor charged $6,800, so EVC was $12,800. The firm priced at $9,800: it kept half the differentiation value and gave the other half to the customer.

### Doing it honestly

The MIT note describes a sequence that holds up well in B2B. Adapted for a PM:

1. **Define the benefit, not the feature.** Value comes from what changes for the customer. The note cites Xerox pricing its copiers per copy rather than per machine, because copies were the benefit.
2. **Name the honest next best alternative,** from the customer's point of view. Use its real price after discounts, in the same units and over the same time horizon as yours.
3. **List every source of differentiation,** positive and negative.
4. **Quantify each one with evidence:** pilots, customer benchmarks, independent tests, the customer's own operating data.
5. **Add reference and differentiation value** to get EVC.
6. **Decide how much value to leave with the customer.**

The note also records a classic failure. A backup company calculated an EVC 100% above its own price and concluded it was underpriced, but it had ignored that rivals were discounting 80% from list. The honest reference value was far lower than the list price it had used. Step 2 is where most value models go wrong, and it's almost always in the vendor's favor.

### How close to price to the ceiling

How much of the differentiation value can you capture? The MIT note lists conditions that move the price closer to EVC: when your product is a small part of the cost of an important end benefit, when someone else shares or pays the cost, and when the spend falls into a budget the buyer doesn't scrutinize. The main condition that pushes price well below EVC is **uncertainty**: if the customer isn't sure they'll realize the benefit, they discount it.

For AI products, uncertainty dominates. Buyers have heard the claims before, and an agent's results depend on the customer's own data, processes and adoption. That argues for leaving more value with the customer early, and for reducing their uncertainty directly through pilots, guarantees or prices tied to outcomes.

:::onramp If you're new to value models
Start with one customer and three drivers. Ask the economic buyer what the job costs them today in hours, downtime or lost revenue, and what they'd do if your product disappeared. Write their numbers down in their words. That one page is already more useful than a list price borrowed from a competitor.
:::

## Value-based, cost-plus and competitive pricing

Pricing courses usually present three approaches as alternatives. In practice each one answers a different question, and a sound price uses all three.

| Approach | How it sets price | What it gets right | Where it fails |
|---|---|---|---|
| **Cost-plus** | Unit cost plus a markup | Simple, easy to defend internally, guarantees margin per unit | Ignores willingness to pay. For software and AI, marginal cost is low or falling, so it underprices and anchors price to a number that keeps moving |
| **Competitive** | Relative to rivals' prices | Reflects what buyers see when they compare | Inherits rivals' mistakes and assumes your differentiation is zero |
| **Value-based** | From EVC by segment | Captures the value you create and explains the price to the buyer | Needs evidence, segmentation and a sales team that can sell value |

Cost-plus deserves a specific warning for AI products. Andreessen Horowitz's Guido Appenzeller estimated in 2024 that the inference cost of a large language model at a constant level of capability was falling roughly tenfold a year, so a cost-plus price set in January is wrong by spring. The working synthesis uses all three:

- **Cost sets the floor.** Below your fully loaded cost to serve (including inference for AI features), every sale loses money.
- **The competitive reference sets the anchor.** The next best alternative's real price is what the buyer compares you against.
- **Value sets the ceiling.** EVC is the most a rational buyer would pay.

Price sits in the corridor between the floor and the ceiling. Where in the corridor depends on your strategy (share or margin), the buyer's uncertainty and the lifecycle stage.

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 350" role="img" aria-label="Economic value to the customer built as a stacked bar, with cost floor, reference value, positive and negative differentiation, EVC ceiling and the price corridor">
  <line x1="40" y1="280" x2="640" y2="280" class="ln"/>
  <rect x="60" y="250" width="80" height="30" rx="4" class="box"/>
  <rect x="170" y="210" width="80" height="70" rx="4" fill="var(--a2)" fill-opacity=".22" stroke="var(--a2)" stroke-opacity=".7"/>
  <rect x="280" y="70" width="80" height="140" rx="4" fill="var(--a1)" fill-opacity=".22" stroke="var(--a1)" stroke-opacity=".7"/>
  <rect x="390" y="70" width="80" height="40" rx="4" fill="var(--a3)" fill-opacity=".22" stroke="var(--a3)" stroke-opacity=".7"/>
  <rect x="500" y="110" width="80" height="170" rx="4" fill="var(--a1)" fill-opacity=".38" stroke="var(--a1)"/>
  <line x1="250" y1="210" x2="280" y2="210" class="ln" stroke-dasharray="3 3"/>
  <line x1="360" y1="70" x2="390" y2="70" class="ln" stroke-dasharray="3 3"/>
  <line x1="470" y1="110" x2="500" y2="110" class="ln" stroke-dasharray="3 3"/>
  <line x1="40" y1="180" x2="640" y2="180" stroke="var(--a3)" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="44" y="172" class="t" style="fill:var(--a3)">Your price</text>
  <text x="595" y="132" class="s">Value left</text>
  <text x="595" y="148" class="s">with customer</text>
  <text x="595" y="212" class="s">Value you</text>
  <text x="595" y="228" class="s">capture</text>
  <text x="100" y="300" text-anchor="middle" class="t">Cost to serve</text>
  <text x="100" y="316" text-anchor="middle" class="s">the floor</text>
  <text x="210" y="300" text-anchor="middle" class="t">Reference</text>
  <text x="210" y="316" text-anchor="middle" class="s">next best alternative</text>
  <text x="320" y="300" text-anchor="middle" class="t">+ Positive</text>
  <text x="320" y="316" text-anchor="middle" class="s">differentiation</text>
  <text x="430" y="300" text-anchor="middle" class="t">− Negative</text>
  <text x="430" y="316" text-anchor="middle" class="s">differentiation</text>
  <text x="540" y="300" text-anchor="middle" class="t">EVC</text>
  <text x="540" y="316" text-anchor="middle" class="s">the ceiling</text>
  <text x="340" y="340" text-anchor="middle" class="s">Price sits in the corridor between cost and EVC. Where it sits is a strategy choice.</text>
</svg>
<figcaption>Economic value to the customer. Start from the honest next best alternative, add what you do better and subtract what you do worse, in money. The gap between your price and EVC is the customer's reason to buy.</figcaption>
</figure>

## Investment value: DCF and NPV for product decisions

The value model asks whether the product is worth it to the customer. The investment case asks whether building it is worth it to you. Finance answers that with **discounted cash flow** (DCF), and the summary number is **net present value** (NPV). You don't need to build the spreadsheet; the harness and your finance partner will. You need to understand the logic well enough to defend the assumptions and to spot when the model is lying.

### The idea in one paragraph

Money today is worth more than the same money later, because money today can be invested and because future money is uncertain. Amy Gallo's HBR refresher frames NPV around this **time value of money**. To compare a product investment against its cost, finance estimates the net cash the product will produce each year, discounts each year's cash back to today at a **discount rate** (the company's required return, often called the hurdle rate), adds them up and subtracts the upfront investment. A positive NPV means the investment is expected to return more than the hurdle. A negative NPV means the company would do better putting the money elsewhere.

### What a PM must understand

Seven ideas carry most of the weight:

1. **The drivers are product decisions.** Adoption, price, gross margin, cost to build and run, and time to first revenue all come from you.
2. **The discount rate comes from finance.** Riskier bets often carry a higher rate, which is fair: uncertain cash is worth less.
3. **Late cash counts for less.** Anything that brings revenue forward, such as faster onboarding, raises NPV more than a bigger number in year five.
4. **Sensitivity beats precision.** Find the two or three assumptions that flip the NPV from positive to negative, and put your evidence effort there.
5. **Use scenarios, not one number.** Base, downside and upside cases show the range; a single NPV to the nearest thousand dollars is false precision.
6. **Model the counterfactual honestly.** Clayton Christensen, Stephen Kaufman and Willy Shih argued in HBR in 2008 that DCF quietly kills innovation when the "do nothing" option is assumed to keep today's cash flows. In most markets, doing nothing means decline, because competitors move. Compare the investment against the realistic baseline, not a flat line.
7. **Staging creates option value.** An investment broken into stages with go or stop gates is worth more than one all-or-nothing bet, because you can stop when early evidence is bad. Forrester's TEI method captures the same idea as **flexibility**: the value of future options a first investment opens up.

:::leader For product leaders
Ask every investment case for the do-nothing baseline and the top three sensitivities before you look at the NPV. If the baseline is flat in a market where competitors are bundling your feature, the case is understating its own value. If the PM can't name which assumption flips the sign, they don't yet know what they're betting on.
:::

Finance may also report **payback period** (how long until cumulative cash covers the investment), **ROI** (net benefit divided by cost, which ignores timing) or **internal rate of return** (the discount rate at which NPV equals zero). Use whichever your finance partner uses, and report NPV alongside it, because NPV respects both size and timing.

## Pricing across the product life cycle

### Skimming and penetration at launch

Joel Dean's 1950 HBR article "Pricing Policies for New Products" set out the idea that a new product's price should change as it moves from novelty toward commodity. Dean framed the launch decision as a choice between two strategies:

- **Skimming**: launch high, sell to the buyers who value the product most, and step the price down over time to reach the next segment.
- **Penetration**: launch low to win share fast, build scale or network effects, and make the market less attractive for imitators.

Skimming suits early demand that is insensitive to price, separable segments and protection from fast imitation. Penetration suits price-sensitive demand, strong scale or network effects, and competitors who will copy you quickly.

The evidence suggests most companies don't choose either. Martin Spann, Marc Fischer and Gerard Tellis studied 663 digital camera models from 79 brands in one large European market and found that only about 20% of launches followed a skimming or penetration pattern. About 60% simply priced in line with the market. Pricing like the market is a strategy too, but usually an accidental one. A Principal PM should make the launch choice explicitly and write down why.

### Growth, maturity and decline

| Stage | What changes | Pricing objective | Typical moves |
|---|---|---|---|
| **Introduction** | Value is uncertain; few references | Prove value, win design partners, learn willingness to pay | Skim or penetrate deliberately; pilots, outcome guarantees, design-partner terms |
| **Growth** | Segments emerge; sales scales | Capture value by segment; protect price integrity | Good, better, best tiers; discount guardrails; a clear value metric |
| **Maturity** | Competitors close the gap; differentiation value shrinks | Retention and expansion over new-logo price | Bundling, packaging changes, cost discipline, new differentiation; watch net revenue retention |
| **Decline** | A successor or substitute takes over | Harvest, migrate or exit with trust intact | Hold price for the loyal base, migration credits toward the successor, announced end-of-life dates |

Two B2B points matter at the ends of the life cycle. At **launch**, enterprise buyers rarely respond to a low price alone; they respond to reduced risk. A penetration strategy in B2B is often a low-risk entry offer (a pilot, a usage minimum, credits) more than a low list price. At **decline**, the customer's switching cost is your responsibility. A sunset price plan is also a trust plan: customers judge the successor product by how you treat them on the way out. Chapter 30 covers lifecycle management and sunsetting in full.

## Behavioral pricing: evidence and ethics

Classical value models assume buyers compute value rationally. They don't, entirely, and behavioral research identifies four effects that matter for pricing. The evidence for each is real, and so are its limits.

### Decoys

Joel Huber, John Payne and Christopher Puto showed in 1982 that adding an option which is clearly worse than one option, but not clearly worse than another, shifts choice toward the option it makes look good. This is the **decoy** or **attraction effect**: a "Pro" tier priced just below "Enterprise" with far fewer features makes Enterprise look like a bargain.

Shane Frederick, Leonard Lee and Ernest Baskin pushed back in 2014. In their experiments the effect appeared mostly when every attribute was shown as a number in a stylized table, and tended to vanish when people experienced the product or when even one attribute was perceptual. They questioned its practical significance. Huber, Payne and Puto replied in the same journal issue that the effect is robust whenever the conditions of a study are closely replicated. The useful reading for a B2B PM is uncomfortable: a pricing page with tiers side by side in a numeric table is exactly where decoys are most likely to work. That raises the ethical bar.

### Anchoring

The first number a buyer sees shapes what they'll pay. Amos Tversky and Daniel Kahneman described anchoring in a 1974 paper in *Science*. Dan Ariely, George Loewenstein and Drazen Prelec showed its force on willingness to pay in a 2003 study: students wrote down the last two digits of their social security number before stating what they'd pay for products such as wine, chocolates and computer accessories. Those with above-median numbers stated values 57% to 107% higher. Yet almost all of them still ranked the products sensibly against each other. Absolute value was easy to move; relative value was stable.

In enterprise sales, the anchor is the first price or the first ROI figure in the conversation. That's an argument for opening with a real enterprise tier and a well-evidenced value model, and against inventing a list price you never intend to charge.

### Charm pricing

Eric Anderson and Duncan Simester ran three field experiments with a mail-order retailer and found that prices ending in 9 increased demand in all three, more so for new items. The authors suggest such endings work best when customers have limited information. Enterprise buyers with procurement teams are the high-information case, so charm pricing belongs on a self-serve plan, not in a negotiated contract.

### Bundling

William Adams and Janet Yellen's 1976 analysis distinguished **separate pricing** (components only), **pure bundling** (the package only) and **mixed bundling** (both). Because buyers value components differently, a bundle can sell to buyers who wouldn't pay the standalone price of either part. Suites, platform editions and AI add-ons are all bundling decisions; Chapter 15 covers packaging in depth.

### The ethical line

Behavioral effects are tools, and regulators have started drawing lines around their use. The US Federal Trade Commission's 2022 staff report on dark patterns sorted deceptive designs into four groups: designs that create false beliefs, that hide or delay material information, that lead to unauthorized charges, and that obscure privacy choices. Its examples include countdown timers on offers that aren't really time-limited and **drip pricing**, where mandatory fees appear only late in the purchase. The report cites a ticketing study in which buyers who weren't shown fees upfront spent about 20% more and were 14% more likely to complete the purchase. In the EU, Article 6a of the Price Indication Directive, applying since May 2022, requires that announced price reductions be genuine.

Those rules mostly target consumer markets, but surprise usage overages, AI consumption charges buried in an order form and "launch week only" discounts that quietly continue are the enterprise versions of the same tactics.

:::key A test for any behavioral tactic
Use a tactic only if every option is real and purchasable, the full price (including usage) is disclosed before commitment, and the customer would not feel tricked if they learned how the page or proposal was designed.
:::

## ROI and business value models for B2B buyers

### Total cost of ownership

Enterprise buyers don't compare your price with a competitor's price. They compare **total cost of ownership** (TCO): every cost of acquiring, deploying, operating and eventually retiring a solution over its life. Subscription is often the smaller part. Implementation, integration, training, internal administration and switching away later all count.

AI products add costs that older TCO models miss: usage and overage charges, the time people spend reviewing and approving AI output, data preparation, evaluation, change management and keeping integrations working as connected systems change. If your value model ignores these, the buyer's finance team will add them for you, usually pessimistically.

### The TEI pattern

Forrester's **Total Economic Impact** (TEI) method gives a well-known structure for business value studies. It has four components: **benefits**, **costs**, **flexibility** (the value of future options the investment creates) and **risk** (an adjustment that reduces benefit estimates according to how uncertain they are). Results are usually modeled for a composite organization built from interviews with several customers, not promised to each buyer. Forrester's published policy requires vendor-commissioned studies to be labeled as commissioned.

That structure, including the disclosure, is a good template for any vendor-built ROI claim. Risk-adjust every benefit. Say who built the model. Separate what was measured from what was modeled.

### From value model to customer ROI calculator

Your EVC model is internal: it tells you where the price ceiling is. A **customer ROI calculator** is the external version, built for the economic buyer and the champion to test the claim with their own numbers. A good one starts from the economic buyer's value drivers, cites the evidence for every default and lets the customer overwrite it, counts the full TCO, ramps benefits over time, shows a risk haircut on each benefit, and reports net benefit, payback and NPV at the customer's own discount rate.

One more property separates a credible value model from a sales tool: after the sale, the same drivers are measured in the product. Most teams skip this, and it's the part that matters at renewal, when the buyer's finance team compares the claim with what happened.

## How to apply it

This method builds the value offering for a new product or a major capability. Plan on four to six weeks alongside discovery, and revisit it at every lifecycle stage.

1. **Draw a canvas for each buying-group role.** Start from the Chapter 01 personas. Rank jobs, pains and gains in measurable form, tag every reliever and creator, and mark which rankings come from interviews and which are guesses.
2. **Name the next best alternative per segment.** Ask customers what they'd do if your product disappeared, and record its real cost after discounts, in your units and time horizon. Often the alternative is people and spreadsheets, and its cost is time.
3. **Build the EVC model with three customers.** Quantify positive and negative drivers with the customer's own numbers, risk-adjust the uncertain ones, and log a source for every number.
4. **Set the price corridor.** Take the fully loaded cost to serve (with inference) from finance as the floor and risk-adjusted EVC as the ceiling. Write down where you'll sit and why.
5. **Write the investment case.** Give the harness your drivers and finance's discount rate; ask for NPV, sensitivities and three scenarios against a realistic do-nothing baseline. Propose stage gates.
6. **Spec the customer ROI calculator,** and agree with customer success how its drivers will be measured after the sale.
7. **Write the lifecycle pricing plan:** stage, objective, price relative to EVC, value metric, discount guardrails and the trigger for the next stage.
8. **Run the ethics review on every pricing surface:** pricing pages, proposals and order forms.
9. **Close the loop.** Each quarter, compare realized value from product data with the value you claimed. Where it falls short, fix the product or the claim.

## The AI lens

### When the product is AI-powered

AI changes the value offering in five ways.

**The charge model.** Bessemer Venture Partners' 2026 AI pricing playbook describes five models: per seat, by usage (tokens, calls), per workflow completed, per outcome achieved, and hybrids. Seat pricing breaks when the product does work that seats used to represent. Stripe's guide to pricing AI products separates the **value metric** (what the customer gets) from the **charge metric** (what you bill on): a resolved ticket is the value; a conversation, an action or a credit may be the charge.

**The outcome definition comes before the price.** Bessemer argues outcome pricing works when you trust the model's performance, can absorb variance in compute cost, and the outcome is unambiguous and measurable. Zendesk announced in August 2024 that customers would pay only for issues its AI agents resolved autonomously. Intercom now prices its Fin AI agent at $0.99 per outcome, counts an outcome when the customer confirms resolution, doesn't ask for more help after Fin responds, or Fin completes a workflow including a handoff, and sets a monthly minimum. Salesforce's Agentforce runs three models at once: credits per action, a price per conversation and per-user licenses. Even the leaders hedge with hybrids. If you charge per outcome, write down what counts, what doesn't (rejected answers, reversals, reopened tickets), how disputes are handled and what credit applies when the AI makes things worse. Ambiguity here becomes a billing dispute later.

**Margin is a constraint again.** Bessemer characterizes AI companies' gross margins as commonly 50% to 60%, against 80% to 90% for traditional software. Price on value; guard on cost. Check the price against the AI cost model (Chapter 31) at today's inference cost and at the volume you expect a year out, because agentic workloads use more tokens per task even as the price per token falls.

**The reference value moves to labor.** Bessemer notes that AI spending often comes from labor budgets, not only IT budgets. When an agent does work a person used to do, the honest next best alternative may be that person's time. That raises EVC, and it raises scrutiny, because the buyer will check the claim against real hours.

**Uncertainty is the main discount.** Buyers discount AI value because they aren't sure they'll realize it. Pilots with agreed success measures, a minimum with outcome-based charges above it, visible quality reporting and spend alerts reduce that uncertainty more cheaply than a lower price does. A surprise overage is the enterprise version of drip pricing.

### Doing the work with AI

Most of this chapter's analysis is now harness work. The PM's job is to supply the evidence, defend the assumptions and read the result.

**Where the harness helps.** Drafting canvases from interview snapshots; pulling value drivers and customers' own numbers out of discovery transcripts; building the EVC, NPV and ROI models from stated assumptions; running sensitivities and scenarios; reviewing a pricing page against the ethics test. With connectors to the CRM, product analytics and billing, it can also compare claimed with realized value across the customer base each quarter.

**Where it doesn't.** The harness can't know your customer's downtime cost, your finance team's discount rate or which alternative the buyer really has. Left to fill gaps, it will produce plausible benchmark numbers with no source. Every number in a value model needs a named source, and "the model estimated it" isn't one.

**Keep the math checkable.** Ask the harness to show each calculation in words next to its result, and recompute one line yourself. Value models are read by finance teams who will.

:::ai The one-line rule
Let the harness do the arithmetic, the scenarios and the first drafts. Never let it supply the inputs. A value model is only as credible as the customer evidence behind each number.
:::

## The Beacon case: building the value offering for Beacon Agents

:::example Where Beacon starts
Beacon is moving its pricing from a per-environment platform fee toward a per-resolved-incident price for Beacon Agents, ahead of launch at Northlight Live. Gross margin has dropped from 81% to 72% since agentic features launched. Marcus, the VP of IT Operations, keeps asking for "an ROI story for the CFO," and sales has been discounting to fill the gap. You're asked for a value offering that sales can defend and finance can approve. All customer numbers below are illustrative.
:::

**The canvases.** You draw one per role. Dana needs to know what broke and what to do in under five minutes. Priya's top pains are alert floods and fear that the agent will make an incident worse. Marcus wants headcount leverage and an ROI case for his CFO. Sam's pains are privileged production access, audit and AI regulatory documentation. Leo's main gain, for the MSP channel, is margin. Mapping pain relievers shows a gap: apart from the approval gate, nothing addresses Priya's fear of the agent acting wrongly. The credit policy below becomes a pain reliever as well as a pricing term.

**The next best alternative.** For most prospects it's humans plus runbooks plus chat. Its incremental software price is close to zero, because they already pay for chat and runbooks. For customers inside a large observability platform, the alternative is a bundled AIOps feature, also at zero incremental price. So the reference value is near zero, and almost all of Beacon's EVC is differentiation value. That changes the sales conversation: Beacon can't argue it's cheaper than the alternative. It has to show it's better by more than it costs.

**The EVC model.** You build it with one design-partner customer, using their numbers. They have about 1,200 significant incidents a year, and the pilot target is 60% resolved with Beacon's help, as defined in Chapter 31: diagnosis accepted, no reopening within 24 hours.

| Driver | Calculation (illustrative) | Annual value | Risk haircut | Risk-adjusted |
|---|---|---|---|---|
| Responder hours saved | 720 incidents × 2.5 hours × $100 an hour | $180,000 | 20% | $144,000 |
| Downtime avoided | 40 customer-facing incidents × 20 minutes × $1,000 a minute | $800,000 | 50% | $400,000 |
| Escalations avoided | 120 escalations × $500 each | $60,000 | 20% | $48,000 |
| Onboarding and connector setup | 300 hours × $100 | −$30,000 | none | −$30,000 |
| Approval-gate oversight | 1,200 incidents × 6 minutes × $100 an hour | −$12,000 | none | −$12,000 |
| Wrong-diagnosis risk | Expected cost of a misdiagnosis, agreed with Priya | −$50,000 | none | −$50,000 |
| **Differentiation value** | | **$948,000** | | **$500,000** |

Downtime is the biggest driver and the least certain, so it gets the largest haircut. The wrong-diagnosis line comes straight from the hallucinated-rollback storyline: you'd rather name it than have Sam's team raise it in procurement.

**The price corridor.** Finance supplies the cost to serve, and the AI cost model from Chapter 31 sets a 70% margin floor. With reference value near zero, EVC for this customer is about $500,000 risk-adjusted. Because the buyer's uncertainty is high at launch, you propose capturing roughly a quarter of it: a $60,000 platform fee plus $100 per resolved incident, about $132,000 a year at 720 incidents. That's about 26% of risk-adjusted EVC and about 14% of the unadjusted figure. In Marcus's terms: about $592,000 of risk-adjusted benefit against about $224,000 of total cost including setup, oversight and risk, a net benefit near $368,000.

**The outcome definition and credit policy.** Following the discipline of public outcome definitions, you specify what counts as a resolved incident, what's excluded (diagnoses responders rejected, incidents reopened within 24 hours, actions rolled back), and a credit when Beacon's action makes an incident worse. A monthly minimum protects Beacon's cost base; outcome charges above it scale with value.

**The investment case.** Finance sets a 12% discount rate for the Beacon Agents program. Your illustrative model has a $6M upfront investment and incremental gross profit of $0.5M, $1.5M, $2.5M and $3.0M over four years. Against a flat do-nothing baseline, NPV is about −$0.7M, and the program looks like a mistake. But the realistic baseline isn't flat. Observability platforms are bundling AIOps, and the two switchers from Chapter 01 left for exactly that reason. Modeling the erosion Agents would prevent (an illustrative $0.3M, $0.8M, $1.4M and $2.0M a year) turns NPV to about +$2.5M. The sensitivities that flip the sign are the resolved-incident rate, the per-incident price and inference cost per incident. You propose stage gates on each: a 60% diagnosis acceptance rate in the pilot, at least 70% gross margin at launch volume, and renewal of the first design partners.

**The lifecycle plan.** One portfolio, four stages:

- **Beacon Classic** (decline): price held for existing contracts, migration credits toward Agents, and an announced end-of-life date.
- **Correlate** (maturity): folded into the platform fee and offered as a bundle with Northlight Observe.
- **Diagnose** (growth): good, better, best tiers with discount guardrails.
- **Agents** (introduction): neither a pure skim nor a penetration play. A list price anchored to EVC, with risk reduced through design-partner pilots, the credit policy and the minimum, rather than through a low headline price.

**The pricing page.** Before Northlight Live, marketing proposes a "Pro" tier designed to make Enterprise look cheap, and a countdown banner for "launch week only" pricing that would quietly continue afterward. You reject both under the ethics test. The page keeps three real tiers, shows Enterprise as a genuine anchor, and states the per-incident charge and the minimum next to the platform fee, so no usage cost appears for the first time on an invoice.

**The ROI calculator.** You spec a calculator for Marcus built from the same drivers, with his inputs editable and every default cited. The disclosure says it was built by Northlight and that results are modeled, not measured. Customer success agrees to report the same three drivers from product data in every quarterly business review, so the ROI claim becomes a tracked number before the first renewal.

## Product 360 artifacts

```template id="12-value-proposition-canvas" title="Value proposition canvas (per buying-group role)"
# Value proposition canvas · [Product] · [Role] · v[n] · [Date]

**Segment:** [segment]   **Role in the deal:** End user / Champion / Economic buyer / Technical evaluator / Procurement / Partner
**Owner:** [PM]   **Evidence:** [number of interviews, pilots, data sources]   **Status:** Hypothesis / Partly confirmed / Confirmed

## Customer profile
### Jobs (ranked)
| Rank | Job | Type (functional / social / emotional) | Evidence |
|---|---|---|---|
| 1 | | | |

### Pains (ranked, measurable)
| Rank | Pain | Measurable form (how much, how often) | Evidence |
|---|---|---|---|
| P1 | | | |

### Gains (ranked, measurable)
| Rank | Gain | Measurable form | Required / expected / desired / unexpected | Evidence |
|---|---|---|---|---|
| G1 | | | | |

## Value map
### Products and services
-

### Pain relievers
| Pain reliever | Addresses (pain ID) | Proof available today |
|---|---|---|
| | | |

### Gain creators
| Gain creator | Addresses (gain ID) | Proof available today |
|---|---|---|
| | | |

## Fit
- Top pains and gains with no reliever or creator:
- Relievers or creators that address nothing ranked:
- Gains that feed the economic value model (economic buyer canvas only):

## Untested assumptions
1. [Assumption] · Test: [how] · Signal: [what would falsify it]
```

```template id="12-evc-model" title="Economic value to the customer (EVC) model"
# EVC model · [Product] · [Segment] · [Customer or composite] · [Date]

**Owner:** [PM]   **Built with:** [customer names and roles, or "composite of n customers"]   **Time horizon:** [e.g. 12 months]   **Units:** [per year / per seat / per incident]

## 1. Benefit (not feature)
What changes for the customer, in one sentence:

## 2. Next best alternative
- What the customer would do without us:
- Its real price after discounts, in our units and horizon: $[ ]   Source:
- **Reference value:** $[ ]

## 3. Differentiation drivers
| Driver | + / − | Calculation in words | Inputs (owner) | Annual value | Evidence and source | Confidence (H/M/L) | Risk haircut % | Risk-adjusted value |
|---|---|---|---|---|---|---|---|---|
| | + | | | | | | | |
| | − | | | | | | | |
| **Total differentiation value** | | | | | | | | |

## 4. EVC
- EVC (unadjusted) = reference value + differentiation value: $[ ]
- EVC (risk-adjusted): $[ ]

## 5. Price corridor
- Floor: fully loaded cost to serve, including inference: $[ ]   Source: finance
- Ceiling: risk-adjusted EVC: $[ ]
- Proposed price: $[ ]   Share of risk-adjusted EVC captured: [ ]%
- Why this share (lifecycle stage, buyer uncertainty, strategy):

## 6. Assumption log
| # | Assumption | Value used | Source | Date checked | Owner |
|---|---|---|---|---|---|
| 1 | | | | | |

## 7. Review
Next review date, and the product data that will confirm or correct each driver:
```

```template id="12-customer-roi-calculator-spec" title="Customer ROI calculator spec"
# Customer ROI calculator spec · [Product] · v[n] · [Date]

**Owner:** [PM]   **Partners:** product marketing, sales engineering, customer success, finance
**Audience:** [economic buyer role] and [champion role]
**Disclosure line (shown on every output):** Built by [company]. Results are modeled from the inputs shown, not measured at your organization. [If any inputs come from a commissioned study, say so.]

## Value drivers
| Driver | Calculation in words | Input the customer owns | Default value | Source of default | Editable? |
|---|---|---|---|---|---|
| | | | | | Yes |

## Cost side (full TCO)
| Cost | Calculation in words | Default | Source |
|---|---|---|---|
| Subscription or platform fee | | | |
| Usage, outcome or overage charges | | | |
| Implementation and integration | | | |
| Internal admin and oversight time | | | |
| Training and change management | | | |
| (AI products) Review and approval time, data preparation | | | |

## Time to value
- Ramp assumption by month or quarter:
- Month in which full value is assumed:

## Risk adjustment
| Driver | Default haircut % | Why | Customer can change? |
|---|---|---|---|
| | | | |

## Outputs
- Net benefit (year 1 and three-year)
- ROI
- Payback in months
- NPV at the customer's own discount rate (customer enters the rate)
- A sensitivity view: the two inputs that move the result most

## Rules
- No default without a cited source. Missing evidence shows as "Customer to supply."
- Every calculation is visible in plain words, not hidden.
- The customer can export inputs and assumptions.

## After the sale
| Driver | How it is measured in product | Report | Cadence | Owner |
|---|---|---|---|---|
| | | Quarterly business review | Quarterly | Customer success |
```

```template id="12-investment-case" title="Investment case (NPV summary)"
# Investment case · [Initiative] · [Date]

**Owner:** [PM]   **Finance partner:** [name]   **Decision maker:** [name]   **Decision needed by:** [date]

## Decision asked
[One sentence: approve $[ ] for [scope] through [first gate].]

## Options
| Option | Description | Baseline assumption |
|---|---|---|
| Do nothing | | [Realistic baseline, including erosion if competitors move] |
| Option A | | |
| Option B (staged) | | |

## Key assumptions
| Driver | Value | Evidence | Confidence (H/M/L) |
|---|---|---|---|
| Adoption (customers, ramp) | | | |
| Price and value metric | | | |
| Gross margin (including inference) | | | |
| Cost to build | | | |
| Cost to run | | | |
| Time to first revenue | | | |

## Cash flow summary (by year, versus do-nothing baseline)
| | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 |
|---|---|---|---|---|---|
| Incremental revenue | | | | | |
| Incremental gross profit | | | | | |
| Investment | | | | | |
| Erosion avoided versus baseline | | | | | |
| Net cash flow | | | | | |

## Results
- Discount rate (from finance): [ ]%
- NPV: $[ ]   Payback: [ ] months   IRR (if finance uses it): [ ]%
- NPV against a flat baseline, for comparison: $[ ]

## Sensitivity (top three drivers)
| Driver | Value at which NPV reaches zero | How far that is from the base case |
|---|---|---|
| | | |

## Scenarios
| Scenario | Key differences | NPV |
|---|---|---|
| Downside | | |
| Base | | |
| Upside | | |

## Stage gates and kill criteria
| Gate | Date | Evidence required to continue | Kill or pivot if |
|---|---|---|---|
| | | | |

## Value not in the numbers
- Strategic options this creates (flexibility):
- Risks not modeled:
```

```template id="12-lifecycle-pricing-plan" title="Lifecycle pricing plan"
# Lifecycle pricing plan · [Product or portfolio] · [Date]

**Owner:** [PM]   **Partners:** pricing or monetization, finance, sales, customer success

| Product or capability | Stage (intro / growth / maturity / decline) | Evidence for stage | Pricing objective | Price relative to EVC | Packaging and value metric | Discount guardrails | Trigger for next stage | Customer communication | Risks |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

## Launch choice (introduction stage only)
- Skimming / penetration / market-based, and why:
- How buyer uncertainty is reduced (pilot, guarantee, minimum, credits):

## Decline and sunset (decline stage only)
- Price for the remaining base:
- Migration offer toward the successor:
- End-of-life date and notice period:
- Contract commitments to honor:

## Review
Review at each quarterly business review, and whenever a stage trigger fires.
```

```template id="12-pricing-ethics-review" title="Pricing surface ethics review"
# Pricing ethics review · [Pricing page, proposal or order form] · [Date]

**Reviewer:** [PM]   **Second reviewer:** [legal or product marketing]

| Check | Pass / Fail | Notes |
|---|---|---|
| Every option shown is real and purchasable (no decoy that cannot be bought) | | |
| Any reference or "was" price is a price we actually charged | | |
| Any deadline or scarcity claim is true and will be honored | | |
| The full price, including usage, overage and minimums, is shown before commitment | | |
| AI consumption charges are explained in plain words with an example bill | | |
| Spend visibility, alerts or caps exist for usage-based charges | | |
| Cancellation or downgrade terms are as easy to find as the purchase path | | |
| A customer who learned how this was designed would not feel tricked | | |

## Decision
Ship / Fix and re-review. Fixes required:
```

## Prompts

```prompt title="Draft value proposition canvases from discovery evidence"
Goal: Get a first canvas for each buying-group role, grounded in what customers actually said.
Paste in: interview snapshots, call notes or win/loss notes, and your persona set. Use only tools approved for customer data, and remove personal identifiers first.

From the material provided for [product], draft a value proposition canvas for each of these roles: [end user, champion, economic buyer, technical evaluator, partner].

For each role:
1. List jobs, pains and gains, ranked by how often and how strongly they appear in the material. Write each pain and gain in a measurable form where the material allows.
2. Cite the source document for every item. If the material doesn't support an item, leave it out.
3. Map our current products and features to pain relievers and gain creators, tagging each to the pain or gain ID it addresses.
4. List the top-ranked pains and gains with no reliever or creator, and any features that address nothing ranked.

Mark every canvas "Hypothesis: to be confirmed with customers."

Check the output: open three citations and confirm the paraphrase matches. Look hardest at the economic buyer's gains, since they feed the value model.
```

```prompt title="Build an EVC model from customer evidence"
Goal: Turn differentiation into money and find the price ceiling for one segment.
Paste in: the economic buyer's canvas, notes from value conversations with [n] customers, the next best alternative and its real price, and any pilot data. This includes customer data; use an approved tool.

Build an economic value to the customer (EVC) model for [product] in [segment], over [time horizon].

1. State the benefit in one sentence, in customer terms.
2. Confirm the next best alternative and its real price after discounts, in our units. If my evidence doesn't support the price, say so.
3. List every differentiation driver, positive and negative. Include switching effort, oversight time and the risk of the product failing.
4. For each driver, give the calculation in words, the inputs, the source of each input and a confidence rating. Do not supply any number I haven't given you; write "Needs customer input" instead.
5. Propose a risk haircut per driver based on confidence, and show unadjusted and risk-adjusted EVC.
6. Show each calculation next to its result.

Check the output: recompute the largest driver yourself. Confirm that no input appears without a source, and that the negative drivers aren't missing or understated.
```

```prompt title="Stress-test an investment case"
Goal: Find the assumptions that decide whether the investment is worth making.
Paste in: the investment case draft, the driver assumptions with their evidence, and the discount rate from finance.

Act as a skeptical finance partner reviewing this investment case for [initiative].

1. Recompute NPV and payback from the assumptions given, showing each year's discounted cash flow in words and numbers.
2. Run sensitivity on every driver and list the three that move NPV most. For each, give the value at which NPV reaches zero.
3. Build downside, base and upside scenarios and explain what differs in each.
4. Critique the do-nothing baseline. If it's flat, describe what a realistic baseline would look like given these competitive facts: [facts], and recompute NPV against it.
5. Propose stage gates with measurable kill criteria.

Don't add assumptions I haven't given you without labeling them "added by reviewer."

Check the output: recompute one year's discounted cash flow by hand. Make sure any change to the baseline is backed by evidence you can show, not by optimism.
```

```prompt title="Spec a customer ROI calculator"
Goal: Produce a buyer-facing ROI calculator spec that a finance team will trust.
Paste in: the EVC model, the TCO components you know, the ramp assumptions and the evidence for each default.

Write a spec for a customer ROI calculator for [product], for [economic buyer role].

Include: value drivers with the calculation in words and the input the customer owns; full TCO including internal time; a ramp; a visible risk haircut per driver; outputs (net benefit, ROI, payback months, NPV at the customer's discount rate); a disclosure line saying who built it and that results are modeled; and a plan for measuring the same drivers in product after the sale.

Flag every default that lacks a cited source. Flag any benefit that would be counted twice.

Check the output: read it as the buyer's CFO would. If any default would embarrass you when the customer asks "where's that from?", replace it with "Customer to supply."
```

```prompt title="Draft a lifecycle pricing plan"
Goal: Make the pricing stage and the next move explicit for each product in a portfolio.
Paste in: the list of products or capabilities, revenue and growth trends, competitive moves, EVC estimates and current discounting data.

For each product in [portfolio]:
1. Propose its lifecycle stage and cite the evidence (growth, competitive pressure, discount trends, successor products).
2. State the pricing objective for that stage and the price relative to EVC.
3. Recommend packaging moves, discount guardrails and the trigger that would move it to the next stage.
4. For any product in introduction, compare skimming, penetration and market-based launch pricing for our situation, and recommend one with reasons.
5. For any product in decline, propose a migration offer and a sunset communication plan that protects trust.

Check the output: challenge any stage assignment that rests on a single data point. Confirm with sales that the discount guardrails are enforceable.
```

```prompt title="Review a pricing page against the ethics test"
Goal: Catch decoys, false urgency and hidden charges before customers do.
Paste in: the pricing page copy or screenshot text, the proposal or order form, and the actual price book.

Review this pricing surface for [product] against these checks:
1. Is every option real and purchasable? Flag any tier that seems designed only to make another tier look better.
2. Are all reference prices, discounts and deadlines true and honored as stated?
3. Is the full price, including usage, overage and minimums, visible before commitment?
4. Are AI consumption charges explained with a worked example bill?
5. Is cancelling or downgrading as easy to find as buying?
6. Would a customer who learned how this page was designed feel tricked?

For each failure, quote the text, explain the problem and propose replacement copy.

Check the output: compare every price and deadline the model accepted against the price book yourself. The model can't know whether a "limited time" offer will in fact end.
```

## Anti-patterns

:::warn Pricing from the cost sheet
Price is set at cost plus a markup because it's easy to defend internally. For software it underprices value; for AI it anchors the price to an inference cost that keeps falling. Use cost as the floor and value as the ceiling.
:::

:::warn The flattering alternative
The value model compares against the competitor's list price, or against a manual process costed at its most wasteful. Buyers recompute against their real alternative and stop trusting the rest of the model. Use the honest next best alternative at its real, discounted price.
:::

:::warn Benefits without negatives
The value model lists every gain and no costs: no switching effort, no oversight time, no risk of failure. Finance teams add those themselves, usually larger. Put negative differentiation in the model before the buyer does.
:::

:::warn The flat do-nothing baseline
The investment case assumes that without the investment, today's revenue continues. In a market where competitors are bundling your capability, the real baseline is decline, and the case understates its own value. Model the counterfactual honestly.
:::

:::warn The ROI claim nobody measures
A calculator full of defaults wins the deal, and nobody measures the same drivers after the sale. At renewal, the claim is still a claim. Instrument the drivers and report them in business reviews.
:::

:::warn Behavioral tricks on a pricing page
A decoy tier nobody can buy, a "launch week only" banner that never ends, a usage charge first seen on the invoice. They may lift a quarter's conversion and then cost you trust in every renewal. Every option real, every price disclosed.
:::

## Checklist

- [ ] Each buying-group role has a value proposition canvas with ranked, measurable pains and gains and tagged relievers and creators.
- [ ] The next best alternative is named per segment, with its real price after discounts and the source.
- [ ] The EVC model includes positive and negative differentiation, a source for every input and risk-adjusted totals.
- [ ] The price corridor is documented: cost floor from finance (including inference), risk-adjusted EVC ceiling and the share of value captured, with reasons.
- [ ] The investment case shows NPV against a realistic do-nothing baseline, the top three sensitivities, three scenarios and stage gates.
- [ ] A customer ROI calculator spec exists, with editable inputs, cited defaults, full TCO, ramp, risk haircuts and a disclosure line.
- [ ] The same value drivers are measured in product after the sale and reported in business reviews.
- [ ] Each product has a lifecycle stage, a pricing objective and a trigger for the next stage.
- [ ] Launch pricing is an explicit choice (skimming, penetration or market-based) with the reason written down.
- [ ] For AI products, the outcome definition, exclusions and credit policy are written before the price is set, and the price is checked against the AI cost model.
- [ ] Every pricing surface has passed the ethics review.
- [ ] No number in any value artifact came from the harness without a named source.

## Key takeaways

- A value offering is a claim the customer can check: what job you do, what their real alternative costs and how much better you are in money terms.
- EVC is the reference value of the next best alternative plus differentiation value, positive and negative. It's a ceiling; price below it and leave the customer a reason to buy.
- Cost sets the floor, the competitive reference sets the anchor and value sets the ceiling. Where you sit depends on strategy, lifecycle stage and the buyer's uncertainty.
- An investment case is only as honest as its do-nothing baseline. Report sensitivities, scenarios and stage gates rather than one NPV.
- Behavioral effects such as anchors, decoys and bundles are real but bounded; use them only when every option is real and every price is disclosed.
- For AI products, define the outcome before pricing it, price on value with a cost guardrail, and reduce buyer uncertainty with pilots and credits rather than discounts.
