<p class="lead">A feature that customers love earns you a good quarter. A moat earns you good years, because it stops capable competitors from taking those returns away. This chapter gives you the tools to tell the two apart: Hamilton Helmer's 7 Powers, Michael Porter's view of sustainable advantage, Clayton Christensen's disruption theory stated the way he meant it, and an honest account of what still defends software when every competitor can call the same AI models you can.</p>

## Why this matters

Every strategy deck has a slide called "Our differentiation." Most of those slides list features. Features matter, but a feature only defends you for as long as a rival needs to build it, and in 2026 that can be a matter of weeks. When a competitor can prototype your headline capability with a frontier model, a few connectors and a good prompt, the question your leadership, your board and your best customers will ask is the one this chapter answers: what stops someone from doing this cheaper?

Warren Buffett popularized the moat metaphor in his shareholder letters. In the 2007 Berkshire Hathaway letter he argued that a business earning high returns is a castle that competitors will attack again and again, so it needs an enduring moat to protect those returns. He named two kinds he liked: being the low-cost producer, and owning a powerful worldwide brand. He also said he avoided industries prone to rapid and continuous change, because a moat that has to be rebuilt constantly isn't a moat. And he described an annual test for the businesses Berkshire owned: did the moat widen or narrow this year?

Both halves of Buffett's view land hard on AI-era software. His warning about rapid change describes most of the feature work in your backlog. His annual test is the right cadence for a moat review. A Principal PM should be able to say, with evidence, which of the product's advantages widened this year and which narrowed.

This shows up in three places in your work:

1. **Investment.** Work that deepens a real barrier compounds. Work that matches a competitor's feature mostly keeps you level.
2. **Pricing and margin.** A real moat shows up as pricing power or lower cost. If gross margin is falling and discounts are growing, the moat is narrowing, whatever the deck says. Chapter 15 covers pricing; this chapter tells you whether you have the power to price.
3. **Credibility.** Boards have heard "data moat" and "network effects" from every team. A PM who can separate a real barrier from a hopeful one, and say which way it's trending, earns trust that carries into other decisions.

This chapter belongs to the Strategy dimension of your Product 360. Chapter 13 maps the competitors; Chapter 14 tests network effects and platform plays. This chapter asks which of your advantages will still be standing when those competitors respond.

## The frameworks: what makes an advantage last

### Helmer's 7 Powers: benefit plus barrier

Hamilton Helmer, an investor who co-founded Strategy Capital in 2013 and taught strategy at Stanford for about a decade, published *7 Powers: The Foundations of Business Strategy* in 2017. It gives a precise test for what counts as an advantage.

Helmer defines Power as the conditions that create the potential for **persistent differential returns**: returns above those of your competitors that last. Every Power has two parts, and you need both:

- **A benefit**: something that improves cash flow. You can charge more, your costs are lower, or you need less investment to deliver the same thing.
- **A barrier**: something that stops competitors from copying the benefit and competing it away.

The barrier is the part teams forget. A benefit without a barrier is just a good idea that rivals will copy. Helmer is blunt that operational excellence (doing the same things better than others) isn't Power by this test, because good practice spreads and competitors catch up. His short version of the value of a business is market size multiplied by Power: a large market with no Power is worth less than it looks, because competition drains the returns.

Here are the seven Powers, each with its benefit and barrier:

| Power | Benefit | Barrier | Example or note |
|---|---|---|---|
| **Scale economies** | Unit cost falls as volume grows | A challenger faces prohibitive cost to gain the share needed to match your costs | Netflix spreading the fixed cost of original content across a growing subscriber base |
| **Network economies** | Each customer gets more value as the number of other customers grows | A challenger faces an unattractive cost to build an equivalent user base; markets often tip to one winner | Helmer notes that how strong a network effect will be is hard to judge in advance |
| **Counter-positioning** | A newcomer adopts a new, superior business model | The incumbent won't copy it, because copying would damage its existing business | Vanguard's low-cost index funds against Fidelity's actively managed funds |
| **Switching costs** | You can charge more on follow-on sales to existing customers | A rival must compensate customers for the cost and risk of switching | Enterprise software that customers have configured and integrated deeply |
| **Branding** | Customers pay more because of emotional appeal or reduced uncertainty | Hysteresis: building an equivalent reputation takes a long period of consistent action | Long-established premium brands |
| **Cornered resource** | Preferential access, on attractive terms, to an asset that independently raises value | Access is held by contract, ownership or decree, not won in the market | Pixar's group of proven directors, its "Brain Trust" |
| **Process power** | Embedded ways of organizing and working that lower cost or improve the product | Hysteresis: the know-how is complex and opaque, so rivals can't copy it quickly | The Toyota Production System |

**Counter-positioning is often temporary.** In a long interview on the Acquired podcast (recorded in 2020), Helmer explained that the incumbent usually knows the new model is good. It just can't afford the hit to its current business yet. Over time, the incumbent may decide to accept the damage and copy. So counter-positioning buys you a window, and you need to use that window to build a second Power.

**Switching costs need repeat purchase.** In the same interview Helmer noted that switching costs only pay off if there's a follow-on sale to capture: an expansion, a renewal, a new module. B2B software usually has one, which makes switching costs a natural candidate for enterprise products. They only count if the benefit shows up in renewal pricing, expansion revenue or net revenue retention.

**Powers have timing.** Helmer argues that different Powers become available at different stages of a business. He places switching costs in the takeoff phase, the period of rapid growth, and warns that the window to establish them often closes. If you haven't built switching costs while customers are adopting you, it's very hard to add them later.

**Most products have one or two.** A business with one strong Power, deliberately deepened, is in better shape than one that claims five on a slide.

:::key Write both cells or claim nothing
For every advantage you claim, write the benefit in cash-flow terms (price premium, lower cost, capital avoided) and the barrier in competitor terms (what would it cost a capable rival to copy this, and why won't they?). If either cell is empty, you don't have a Power. You have a strength.
:::

:::onramp If strategy frameworks are new to you
Start with one question for every "differentiator" in your product's deck: "If our best-funded competitor decided to copy this tomorrow, what would stop them?" If the honest answer is "nothing much, it would take them a quarter," that differentiator is a feature. Most are, and that's fine. Just don't build the strategy on it.
:::

### Porter: advantage comes from a system, not a feature

Michael Porter's 1996 Harvard Business Review article "What Is Strategy?" makes a distinction that pairs neatly with Helmer. **Operational effectiveness** means performing similar activities better than rivals: faster releases, a cleaner UI, better support. It's necessary, but it isn't strategy, because best practices diffuse and competitors converge. **Strategy** means choosing a different set of activities to deliver a unique mix of value.

Porter argues that two things make a strategic position sustainable:

- **Trade-offs.** You choose what not to do. A company that serves enterprise security reviewers with deep audit controls can't also be the cheapest self-serve tool, and a competitor that tries to do both ends up worse at each.
- **Fit.** Your activities reinforce each other. Porter describes three orders of fit: simple consistency between activities and strategy, activities that reinforce one another, and optimization of effort across them. Fit makes a position hard to copy, because a rival has to match the whole interlocking system, and the odds of matching every activity compound against the imitator.

In a 2001 article, "Strategy and the Internet," Porter argued that the internet tended to weaken industry profitability and didn't create proprietary advantage on its own, because every competitor could adopt it. The winners integrated it into a distinctive way of competing. Swap "the internet" for "generative AI" and the argument still holds.

For a PM, Porter's lesson is about altitude. A single feature is operational effectiveness. A moat is usually a system: your data, your workflow position, your pricing model, your channel and your reputation for safety fitting together so that a rival would have to rebuild all of them at once.

### Christensen's disruption theory, stated correctly

Clayton Christensen introduced the idea with Joseph Bower in a 1995 HBR article, "Disruptive Technologies: Catching the Wave," and developed it in *The Innovator's Dilemma* (1997). In 2015, Christensen, Michael Raynor and Rory McDonald published "What Is Disruptive Innovation?" in HBR precisely because the term had come to mean any big change.

The theory, as the Christensen Institute states it, describes a process:

1. Incumbents improve their products for their most demanding, most profitable customers. Christensen calls this **sustaining innovation**. Eventually they overshoot what many mainstream customers need.
2. A smaller entrant with fewer resources gets a **foothold** in one of two places: the **low end** of the market (customers the incumbent is happy to give up, because they're the least profitable) or a **new market** of nonconsumers (people who didn't buy anything before, because existing products were too expensive or complicated).
3. The entrant's product starts out **worse** on the measures of performance the mainstream market has always valued, but it's cheaper, simpler or more convenient.
4. The entrant improves until it's good enough for mainstream customers, who then switch.

The Christensen Institute is explicit that disruptive innovations aren't breakthrough technologies that make good products better. A better product sold to the incumbent's best customers is a sustaining innovation, and by Christensen's own account incumbents usually win those fights.

This is why Christensen and his co-authors argued in 2015 that Uber didn't fit the theory: it started in the mainstream taxi market, not at the low end or among nonconsumers. Uber changed an industry, but through a different process.

The theory has serious critics, and you should know them. Jill Lepore, writing in *The New Yorker* in 2014, argued that the theory rested on selectively chosen cases and that some companies named as disruption victims remained dominant. Andrew King and Baljir Baatartogtokh, in MIT Sloan Management Review in 2015, tested Christensen's own cases against four conditions the theory requires: the incumbent was on a sustaining trajectory, it overshot customer needs, it was capable of responding, and it actually floundered as a result. Many cases didn't meet all four. The fair conclusion is that disruption is a specific pattern that sometimes happens, not a law that explains every incumbent's decline.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 350" role="img" aria-label="Disruption: the incumbent improves past what mainstream customers need while an entrant starts below and improves until it is good enough">
  <line x1="70" y1="300" x2="615" y2="300" class="ln"/>
  <line x1="70" y1="300" x2="70" y2="25" class="ln"/>
  <line x1="70" y1="150" x2="610" y2="70" stroke="var(--muted)" stroke-width="1.5" stroke-dasharray="6 5"/>
  <line x1="70" y1="220" x2="610" y2="150" stroke="var(--muted)" stroke-width="1.5" stroke-dasharray="6 5"/>
  <line x1="70" y1="175" x2="610" y2="35" stroke="var(--a1)" stroke-width="3"/>
  <line x1="300" y1="290" x2="610" y2="110" stroke="var(--a2)" stroke-width="3"/>
  <circle cx="521" cy="162" r="7" fill="var(--a3)"/>
  <line x1="90" y1="36" x2="120" y2="36" stroke="var(--a1)" stroke-width="3"/>
  <text x="128" y="40" class="s">Incumbent: sustaining innovation</text>
  <line x1="90" y1="56" x2="120" y2="56" stroke="var(--a2)" stroke-width="3"/>
  <text x="128" y="60" class="s">Entrant: starts worse, improves fast</text>
  <line x1="90" y1="76" x2="120" y2="76" stroke="var(--muted)" stroke-width="1.5" stroke-dasharray="6 5"/>
  <text x="128" y="80" class="s">Needs: demanding (upper), mainstream</text>
  <text x="615" y="240" text-anchor="end" class="s" style="fill:var(--a3)">Good enough: mainstream switches</text>
  <text x="80" y="290" class="s">Foothold: low end or nonconsumers</text>
  <text x="340" y="325" text-anchor="middle" class="s">Time</text>
  <text x="34" y="165" text-anchor="middle" class="s" transform="rotate(-90 34 165)">Performance on measures customers value</text>
</svg>
<figcaption>Disruption as Christensen described it. The incumbent improves for its best customers and overshoots the mainstream. The entrant starts below what mainstream customers need, from a low-end or new-market foothold, and switches them once it is good enough. A better product aimed at the incumbent's best customers is a sustaining threat, not a disruptive one.</figcaption>
</figure>

**The disruption test.** Use the correct version of the theory as a four-question check on any threat:

1. Is the threat **worse** on the measures our customers use to judge us today?
2. Is it **cheaper or simpler**, or does it serve people who **don't buy** from anyone today?
3. Is it **improving fast** on the measures that matter to our mainstream customers?
4. Is it attached to a **business model we'd find unattractive** to copy?

Four yeses describe a disruptive threat. Christensen himself later observed that low-end entry tends to come with a business model the incumbent finds unattractive, which is the bridge to Helmer's counter-positioning. If the answers are mostly no, you're facing a sustaining competitor, and you fight it with product, sales and price.

### Moats in AI-era software

If AI makes software cheaper to build, what defends a software business? Jerry Chen revisited his Greylock essay "The New Moats" for the AI era and concluded that the new moats are mostly the old ones: workflows, data integration, trust, network effects, scale and go-to-market. What has changed is which of those still hold, and how fast the rest erode.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 330" role="img" aria-label="Layers of an AI product and their moat potential, from commodity models at the bottom to trust and distribution at the top">
  <rect x="40" y="250" width="360" height="44" rx="8" class="box"/>
  <text x="56" y="277" class="t">Model access</text>
  <text x="415" y="277" class="s">Commodity input. Low.</text>
  <rect x="40" y="198" width="360" height="44" rx="8" class="box"/>
  <text x="56" y="225" class="t">Connectors and integration breadth</text>
  <text x="415" y="225" class="s">Standardizing. Falling.</text>
  <rect x="40" y="146" width="360" height="44" rx="8" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)"/>
  <text x="56" y="173" class="t">Proprietary context and outcome data</text>
  <text x="415" y="173" class="s">Real if exclusive and compounding</text>
  <rect x="40" y="94" width="360" height="44" rx="8" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)"/>
  <text x="56" y="121" class="t">Workflow depth and system of action</text>
  <text x="415" y="121" class="s">Switching costs. Strong.</text>
  <rect x="40" y="42" width="360" height="44" rx="8" fill="var(--a1)" fill-opacity=".14" stroke="var(--a1)"/>
  <text x="56" y="69" class="t">Trust, distribution and ecosystem</text>
  <text x="415" y="69" class="s">Slow to build. Strongest.</text>
  <line x1="20" y1="290" x2="20" y2="48" class="ln"/>
  <polygon points="14,54 20,42 26,54" fill="var(--muted)"/>
  <text x="250" y="318" text-anchor="middle" class="s">Higher layers take longer to build and longer to copy</text>
</svg>
<figcaption>Where defensibility sits in an AI product. The model layer is a supplier anyone can buy from. Integration breadth is standardizing. The durable candidates sit above: exclusive context, deep workflow position, and trust and distribution built over years.</figcaption>
</figure>

**Model access isn't a moat.** Stanford's AI Index 2025 reported that the cost of querying a model performing at the level of GPT-3.5 fell more than 280-fold between November 2022 and October 2024. A 2024 a16z analysis by Guido Appenzeller, which he called "LLMflation," estimated that the cost of a given level of capability was falling about tenfold a year. Epoch AI found price declines at constant performance ranging from about 9 to 900 times a year depending on the task, while cautioning that the fastest declines may not persist. Quality is converging too: the AI Index found the gap between the best open-weight and closed models on some benchmarks shrank from 8 percent to 1.7 percent in a year, and the gap between the top model and the tenth-best narrowed from 11.9 percent to 5.4 percent. A leaked 2023 Google memo, published by SemiAnalysis under the title "We Have No Moat, And Neither Does OpenAI," made the same argument about open-source models; it was one anonymous employee's view, not Google's position, but the convergence it described has continued. In Helmer's terms, a model API gives an application builder no barrier. It's a supplier your rivals can buy from tomorrow. David Cahn of Sequoia has argued that businesses with high fixed costs and low marginal costs tend to see prices competed down toward marginal cost, which is where undifferentiated AI features are heading.

**Data moats are weaker than they sound.** Martin Casado and Peter Lauten's 2019 a16z essay "The Empty Promise of Data Moats" is the standard corrective. Most so-called data network effects, they argue, are really data scale effects with diminishing returns: each additional record costs more to get and adds less, data goes stale, and competitors can often assemble a "minimum viable corpus" good enough to compete. Their example of a support chatbot shows automated coverage of customer intents plateauing around 40 percent, because the remaining questions are a long, thin tail. NFX's network effects manual lists data as one of sixteen types of network effect and describes it as weaker than investors tend to assume. Chapter 14 covers how to test a data network effect claim. For this chapter, the rule is that data is a moat only when it's proprietary or hard to get, refreshed by use, concentrated in the hard part of the problem, and when the accuracy it buys actually drives adoption.

**Workflow integration and systems of record still defend.** Chen's original framework separated systems of record (the CRM, the HR system, the ERP: where the authoritative data lives), systems of engagement (where people do the work) and "systems of intelligence" that combine data across systems to make predictions. Bain's 2025 technology report treats systems of record as the defensible base layer in an agentic world because of their unique data structures, long histories of activity and embedded regulatory logic. In Helmer's terms, deep workflow position is switching costs plus, sometimes, process power. The question to ask is whether customers have built their processes, approvals and compliance evidence around your product, or whether they just log in to it.

**Proprietary context is the new candidate.** An AI agent is only as good as what it knows at run time. Anthropic's 2025 guidance on context engineering treats the context window as a scarce resource to be filled with the highest-signal information, retrieved just in time. In a B2B agent, that information is customer-specific: system topology, history, runbooks, permissions, and labels for which past actions worked. A rival can call the same model; it can't easily call the same context. But be careful about the Helmer category. Context is a cornered resource only if your access is protected by contract, structure or position. If any competitor could get the same context through the same APIs once the customer connects them, it's a scale advantage at best.

**Interoperability lowers integration moats.** "We have 200 integrations" used to be a real switching cost. Anthropic introduced the Model Context Protocol (MCP) in November 2024 as an open standard for connecting AI applications to tools and data. In December 2025 it was donated to the Agentic AI Foundation, a directed fund under the Linux Foundation co-founded by Anthropic, Block and OpenAI, with more than 10,000 active public servers and more than 97 million monthly SDK downloads at the time. Google launched the Agent2Agent (A2A) protocol in April 2025 with more than 50 technology partners. When connectors are standard, the breadth of your integration catalog stops being a barrier. What still counts is depth: how much a connector can do safely, how well it's governed, and what you learn from the actions taken through it.

**Distribution and the user relationship.** Ben Thompson's Aggregation Theory, set out on Stratechery in 2015, argues that when distribution becomes nearly free, power shifts to whoever owns the relationship with the user, and suppliers get commoditized. In 2026 the AI assistant with connectors is a new candidate aggregator. A SaaS product reached only as a connector inside someone else's assistant risks becoming a supplier to that assistant. Some companies are responding by putting up data walls: Slack's API terms, effective October 2025, bar external apps from using Slack data obtained through the API to train large language models and from building persistent indexes of other organizations' data. Bain's 2025 report also recommends that SaaS vendors limit other AI platforms from learning on their data. Data walls protect a position, but they cost you openness, and Chapter 14 explains why openness can be the stronger play.

**Trust and brand.** Helmer's branding benefit includes reduced uncertainty, and that's the enterprise AI case exactly. A buyer letting an agent act in production is paying for confidence that it won't cause harm. The barrier is hysteresis, which cuts both ways: trust takes years of consistent behavior to build and one bad incident to dent. In practice, AI trust is built from visible mechanisms (cited evidence, approval gates, audit logs, documented risk controls) and a long record of using them.

**Ecosystems and complements.** Joel Spolsky's 2002 essay "Strategy Letter V" put a classic platform strategy in one line: "Smart companies try to commoditize their products' complements." If the layers next to yours become cheap and plentiful, demand for your layer rises. For an AI product, that can mean opening schemas, publishing connectors and welcoming partner agents, so the ecosystem grows around the part you own. Chen makes a related point about open source: it commoditizes the layer it touches and pushes value to the layers beside it.

### AI and the threat to SaaS seats

The sharpest strategic question for many B2B products in 2026 is what happens to per-seat pricing when software does the work people used to do. Bain's 2025 report put it plainly: seat-based pricing may not fit when AI is doing the work. Bain scores each workflow on two dimensions, how far AI can automate it and how far third-party AI can reach into it. The resulting four scenarios are AI enhancing the existing product ("core strongholds," where human judgment still matters and rivals struggle to copy the workflow), spending compressing ("open doors," where third-party agents reach in through exposed APIs and capture value), AI outshining the existing product ("gold mines," where the incumbent's exclusive data and rules give it a head start on full automation) and AI cannibalizing it ("battlegrounds," where the incumbent must replace its own product with AI or lose the work). Bain recommends pricing for work done (tasks completed, tickets resolved) rather than for access.

Pricing pages show the shift. As of October 2026, Intercom prices its Fin agent at $0.99 per outcome, and Salesforce prices Agentforce through a mix of per-conversation fees, per-action credits and per-user licenses. Chapter 15 covers how to design these models.

Horizontal agents are also reaching into jobs that role-specific SaaS used to own. In January 2026 Anthropic released 11 open-source starter plugins for Claude Cowork, covering roles such as legal, sales, finance, support and product management. When a general assistant can pick up a role's workflow through a plugin and a few connectors, a seat-priced tool for that role has to show what it does that the assistant can't.

Market sentiment has moved too. Inc. reported that roughly $300 billion of SaaS market value was lost in a selloff in early February 2026, dubbed the "SaaSpocalypse." The causes of a market move are hard to pin down, so treat it as evidence of what your board is worried about, not evidence about your product.

Apply both lenses before you accept the headline. In Christensen's terms, an agent sold per outcome can be a genuine low-end or new-market foothold: it serves teams that never bought seats, at a lower price, with lower quality at first. In Helmer's terms, a seat-priced incumbent faces counter-positioning, because charging per outcome would cut its own seat revenue as agents reduce the number of people who need seats. But many "AI kills SaaS" claims describe sustaining innovations sold to the same buyers, which incumbents usually win. Run the four-question test on each threat rather than adopting the narrative wholesale.

:::leader For product leaders
Ask every product in your portfolio the same two questions each year: which Power do you have, with benefit and barrier written out, and did it widen or narrow? Then look across the answers. If several products claim the same Power (usually "our data"), check whether it's one shared asset or several weak copies. Portfolio-level moats, such as one trust posture and one security review that covers every product, are often stronger than any single product's.
:::

## How to apply it

Here's a method for assessing your moat honestly and turning the result into decisions. Run it once properly, then repeat the review every year (Buffett's cadence) and whenever a major competitor or platform shift appears. It takes about three weeks the first time.

**Week 1: Gather evidence before opinions.**

1. **Collect the claims.** Pull every statement of differentiation from the strategy deck, the board deck, the sales battlecards (Chapter 13) and the last few analyst briefings. List each claim in one line. There are usually more than anyone expects, and some contradict each other.
2. **Collect the evidence.** For each claim, find data that would show the benefit if it were real: win rates against named competitors, discount levels by segment, renewal and expansion rates, gross margin trends, time and cost to onboard, and churn reasons from win/loss notes. Ask your AI harness to assemble this from connected systems, with sources, and treat anything without a source as opinion.
3. **Interview the people who see competitors.** Talk to four or five account executives, two solutions engineers and two customer success managers. Ask about the last deal lost to a competitor, the last renewal at risk, and what the customer said they could get elsewhere.

**Week 2: Run the assessments.**

4. **Fill in the 7 Powers assessment.** For each Power, write the benefit in cash-flow terms, the barrier in competitor terms and the evidence for both. Mark each as present, emerging or absent. Be strict: a Power with an empty barrier cell is absent. Expect one or two to survive.
5. **Score the moat sources.** Use the moat scorecard to rate the AI-era sources (proprietary data, proprietary context, workflow depth, switching costs, distribution, trust, ecosystem, scale economics, counter-positioning, process power) from 0 to 3. Require evidence for any score above 1. Add Buffett's column: did this widen or narrow in the past year?
6. **Check for disruption.** For the three most serious competitive threats, run the four-question disruption test. Separate sustaining threats (fight with product and sales) from disruptive ones (which may need a different business model or unit) and from aggregator threats (where someone else is taking the user relationship).
7. **Find the commoditizing features.** List the features where a model provider, a platform bundle, open source or an AI assistant now offers something good enough. For each one, decide whether it's your product or a complement to your product.

**Week 3: Decide and set the watch.**

8. **Write commoditization response plans** for the features under threat. Choose among five responses: move up the stack, bundle the feature into a system with fit, reprice, open it up and commoditize it yourself, or harvest and exit.
9. **Decide where to invest.** Pick the one or two Powers you'll deliberately deepen over the next year. Name the roadmap items that build the barrier (not just the benefit) and the metric that will show the barrier is widening.
10. **Set up the competitive threat monitor.** Agree on the signals, sources and triggers, and have the AI harness draft it monthly for you to validate.
11. **Present the result.** Show your manager and the leadership team the Powers you have, the ones you don't, the features you'll stop defending and the barriers you'll build. Record the decisions in the decision log, with a review date a year out.

:::key The barrier is the roadmap item
When you decide to deepen a Power, put the barrier on the roadmap, not just the benefit. "Better root-cause accuracy" is a benefit any competitor can chase. "Outcome labels from approved actions that only flow back to us" is a barrier. Name the work that builds the second kind.
:::

### Choosing a response when a feature gets commoditized

Commoditization is normal. The mistake is defending a commodity feature as if it were a moat. Five responses cover most situations:

| Response | When it fits | What it looks like | Framework behind it |
|---|---|---|---|
| **Move up the stack** | The commoditized feature is an input to a bigger outcome you can own | Stop selling the step; sell the result the step contributes to, and price on that result | Porter (a distinct position) |
| **Bundle into a system** | The feature is more valuable combined with your other activities than on its own | Tie it to your workflow, data and governance so a rival must copy the whole system | Porter (fit) |
| **Reprice** | The feature's cost to serve is falling and rivals are cutting price | Lower its price or include it, and shift revenue to outcomes or to the layer you defend | Bain (work-done pricing) |
| **Commoditize it yourself** | The feature is a complement to the part you own | Open the schema or interface, give it away or make it standard, so demand for your core grows | Spolsky (commoditize complements) |
| **Harvest and exit** | The feature has no path to a barrier and serves a shrinking need | Stop investing, migrate customers to the replacement, and retire it on a schedule | McGrath (transient advantage) |

Rita McGrath's 2013 HBR article "Transient Advantage" is a useful backstop here. She argues that in fast-moving markets advantages are temporary, so companies should manage a portfolio of them and get as good at exiting old advantages gracefully as at launching new ones. Chapter 30 covers the mechanics of retiring a product or feature.

If the commoditizing force is a disruptive entrant (it passes the four-question test), Christensen's advice from *The Innovator's Dilemma* is to consider responding with a separate unit or a separate business model rather than forcing the response through the core business's priorities and margins. Chapters 20 and 22 cover how to set that up.

## The AI lens

### Building AI-powered products

When the product is AI-powered, five defensibility questions change.

- **The model is a supplier, so treat it like one.** Design your architecture so you can switch models without rebuilding the product, and track inference cost per outcome as a core economic metric. Falling model prices help you, but they help your competitors equally, so a cost advantage only counts if it comes from something they can't copy, such as better routing, caching or smaller specialized models trained on your own outcome data. Chapter 31 covers the engineering.
- **Your evaluation pipeline can be process power.** A team that turns every production failure into a test case, and every test case into a measurable improvement, builds know-how that's slow to copy. That's Helmer's process power if it compounds and stays opaque to rivals. Write down the loop and measure its speed.
- **Context beats corpus.** For most B2B agents, the advantage is less about how much data you've collected and more about what customer-specific context the agent can retrieve at run time, and whether that context is exclusive. Map which context sources only you can reach, and which any competitor could reach through the same standard connectors.
- **Outcome labels are the scarce data.** Logs and telemetry are plentiful. What's rare is a reliable label saying which action actually fixed the problem, approved by a human and confirmed by the result. If your product sits where those labels are created, design to capture them, with consent and contracts that say so.
- **Trust is a feature you can lose in a day.** For agents that act, trust is the branding Power. Build the mechanisms that make it visible (cited evidence, approval gates, audit trails, kill switches) and keep a record of incidents and fixes. Chapter 33 covers the governance and regulatory side.

### Doing the work with AI

AI changes competitive work mostly in gathering and sorting evidence, which used to take most of the time.

**Where AI helps.** A harness connected to your CRM, win/loss notes, support tickets, call summaries and competitor release notes can assemble the evidence base for a moat review in hours. It can classify each competitive signal by type (sustaining, low-end, new-market, counter-positioning, aggregator) and by which moat source it attacks, draft a first 7 Powers assessment for you to challenge, and run a disruption test on a new entrant from its public material. It's also a useful sparring partner: ask it to argue the competitor's case against your claimed barrier.

**Where AI doesn't help.** A model can't tell you what your competitors will decide to do, and it tends to repeat the strategy vocabulary it has seen most often, which means it will happily confirm a "data network effect" that's really a scale effect. It also can't see the deals your sales team didn't log. Treat its assessments as drafts and its classifications as hypotheses.

**Keep the evidence attached.** Every claim in the moat scorecard should link to a source: a win/loss note, a renewal record, a margin report, a customer quote. Competitive notes and pricing data are confidential; use an approved tool, and keep customer identifiers out of any prompt that doesn't need them.

:::ai The one-line rule
Use AI to gather competitive evidence and to argue against your moat. Don't use it to certify your moat. The judgment about which barrier will hold is yours.
:::

## The Beacon case: what actually protects Beacon

:::example Where Beacon starts
Beacon is growing fast (about $48M in ARR, up 38 percent year over year, with net revenue retention of 118 percent), but gross margin has dropped from 81 percent to 72 percent since agentic features launched, because of inference cost. The board deck lists four moats: "proprietary AI," "our data," "200 integrations" and "deep Observe integration." In the last quarter, two large observability platforms announced AI incident summaries bundled into existing contracts, and a startup began selling an ops agent to mid-market teams at a low monthly price. The VP of Product asks you for an honest moat assessment before the annual planning cycle.
:::

**The evidence.** You ask the harness to pull win/loss notes, renewal records, discount data and churn reasons from the past four quarters, and to list every competitor mention with its source. You interview five account executives, two solutions engineers and two customer success managers. Two patterns stand out. Deals lost on correlation alone are rising, and in each one the buyer cited a bundled feature from a platform they already paid for. Renewals, though, are strong wherever customers have allowlisted autonomous actions and routed approvals through Beacon. None of the accounts that route remediation approvals through Beacon has churned.

**The 7 Powers assessment.** You go through the Powers one at a time.

| Power | Verdict | Benefit | Barrier | Evidence |
|---|---|---|---|---|
| Scale economies | Absent | None today; inference cost per incident is roughly what rivals pay | None | Margin fell from 81 to 72 percent |
| Network economies | Absent, emerging in one channel | Leo's MSP customers share runbooks across tenants | Not yet a barrier | Covered in Chapter 14 as a cross-side effect being built |
| Counter-positioning | Emerging, best candidate | Per-resolved-incident pricing aligns price with value | Seat-priced incident tools would cut their own revenue by matching it | Depends on the pricing move landing |
| Switching costs | Present, growing | Expansion into Beacon Agents; NRR of 118 percent | Tuned runbooks, approval policies, allowlists and a completed security review are costly to redo | No churn among accounts with approval workflows |
| Branding (trust) | Fragile | Buyers like Marcus pay for confidence the agent won't make things worse | Hysteresis, which also means slow recovery | The hallucinated root cause that led a customer to roll back the wrong service |
| Cornered resource | Absent | Resolved-incident history | No contractual or structural exclusivity | Likely a scale effect with diminishing returns |
| Process power | Emerging | Post-incident reviews feed evals and retrieval | Only if the loop compounds faster than rivals can build one | Loop exists; its speed isn't measured yet |

"Proprietary AI" disappears: Beacon calls the same frontier models its rivals can, so model access gives it no barrier. "Our data" becomes two things. The resolved-incident history is a data scale effect, valuable but likely to plateau, in line with Casado and Lauten. The outcome labels (which approved action actually resolved the incident) are rarer, and they're the asset worth designing around.

**The moat scorecard.** The widened-or-narrowed column carries the most information. Switching costs and workflow depth widened, because more customers routed approvals through Beacon. Integration breadth narrowed: with MCP connectors now standard, "200 integrations" no longer stops anyone. Proprietary context is strong for Northlight Observe customers, where Beacon has deep, governed access to telemetry and change history, and weak for tool-agnostic prospects. That's the case's long-running tension between building on Observe data and staying tool-agnostic, now seen as a moat trade-off. Chapter 14 resolved it with an open architecture that gives Observe customers the deepest integration; the scorecard confirms that the Observe advantage is real but shouldn't be the whole strategy.

**The disruption check.** You run the four-question test on the two threats. The large observability platforms' AI summaries are sustaining innovations: better products sold to the same buyers. They're a serious threat to correlation, but they aren't disruption, and Beacon fights them with diagnosis quality and workflow depth. The startup ops agent is different. It's worse on enterprise measures (no approval gates, no audit logs), it's cheap and serves mid-market teams without an SRE function who never bought an AIOps tool, it's improving quickly, and its low monthly price is a model Beacon's enterprise sales motion can't serve profitably. That's four yeses, and the exposed flank is Leo's MSP customers. You recommend the MSP channel get its own packaging and price point rather than waiting for the enterprise product to trickle down.

**The commoditization response.** Correlation, Beacon's original feature, is being commoditized from two directions: platform bundles, and AI assistants that can summarize alerts through standard connectors. You write the response plan. Correlation is a complement to diagnosis and action, so Beacon treats it as one: it's included in the platform fee rather than sold as a feature, and the team considers opening the incident-grouping schema so partners build on it. Value moves up the stack to Diagnose and Act, priced per resolved incident (Chapter 15). The legacy Beacon Classic engine is harvested through the planned migration (Chapter 30).

**The data wall question.** One proposal is to change Beacon's API terms, following the Slack precedent, to bar third-party agents from training on or indexing Beacon incident data. You weigh it against the open architecture and the partner ecosystem from Chapter 14. The decision is a narrow wall: partners can read and act on incidents for the customer who connected them, but outcome labels aren't exposed for training outside that customer, and Sam reviews the terms.

**The decision.** Leadership approves three moves. Deepen switching costs and process power through approval workflows, allowlist management and a measured post-incident learning loop that captures outcome labels. Pursue counter-positioning through per-resolved-incident pricing. Rebuild trust as an explicit program after the wrong-rollback incident, with cited evidence on every diagnosis and audit logs Sam can export. Each move gets a metric: renewal rate for accounts with approval workflows, eval improvement per month from post-incident reviews, and diagnosis acceptance rate. You set up a monthly threat monitor with product marketing and book the next full moat review for a year out.

## Product 360 artifacts

```template id="16-seven-powers-assessment" title="7 Powers assessment"
# 7 Powers assessment · [Product] · [Date]

**Owner:** [PM]   **Reviewed with:** [names]   **Next review:** [date, one year out]

Rule: a Power counts only if both the benefit and the barrier cells are filled with evidence. Expect one or two to survive.

| Power | Status (present / emerging / absent) | Benefit in cash-flow terms (price, cost, capital) | Barrier: what stops a capable rival, and why won't they copy? | Evidence (with source) | Action |
|---|---|---|---|---|---|
| Scale economies | | | | | |
| Network economies | | | | | |
| Counter-positioning | | | | | |
| Switching costs | | | | | |
| Branding (including trust) | | | | | |
| Cornered resource | | | | | |
| Process power | | | | | |

## Claims that did not survive
| Claimed advantage | Why it fails (no benefit / no barrier / no evidence) | What it really is (feature, strength, scale effect) |
|---|---|---|
| | | |

## Timing
- Stage of the business (early, rapid growth, mature):
- Powers still available to build at this stage:
- Window closing on (for example, switching costs during rapid growth):

## The one or two Powers we will deepen
1. [Power] · Barrier-building roadmap items: [items] · Metric that shows the barrier widening: [metric]
2.

## Decision
Agreed by [name] on [date]. Logged in [decision log].
```

```template id="16-moat-scorecard" title="Moat scorecard"
# Moat scorecard · [Product] · [Year]

Scoring: 0 = none, 1 = claimed but unproven, 2 = real with evidence, 3 = real, evidenced and hard to copy. Any score above 1 needs a source.

| Moat source | Score (0 to 3) | Evidence (source) | This year: widened / stable / narrowed | What would erase it | Leading indicator to watch |
|---|---|---|---|---|---|
| Proprietary data (exclusive, refreshed by use, in the hard tail) | | | | | |
| Proprietary context (what the agent can know that rivals can't) | | | | | |
| Outcome labels (which action actually worked) | | | | | |
| Workflow depth / system of record or action | | | | | |
| Switching costs (configuration, approvals, compliance evidence) | | | | | |
| Distribution and channel (who owns the user relationship) | | | | | |
| Trust and brand | | | | | |
| Ecosystem (partners, connectors, complements) | | | | | |
| Scale economics (including inference cost per outcome) | | | | | |
| Counter-positioning (business model rivals won't copy) | | | | | |
| Process power (eval and learning loop speed) | | | | | |
| Model access | 0 | Rivals can buy the same models | | | Price and quality of alternative models |

## Annual test
- Widened this year:
- Narrowed this year:
- Biggest surprise:

## Implications
- Stop defending:
- Start building:
- Pricing and margin effect:
```

```template id="16-disruption-test" title="Disruption test"
# Disruption test · [Threat] · [Date]

**Threat:** [competitor, product or category]   **Source of signal:** [where we saw it]

| Question | Yes / No | Evidence |
|---|---|---|
| 1. Is it worse on the measures our customers use to judge us today? | | |
| 2. Is it cheaper or simpler, or does it serve people who don't buy from anyone today? | | |
| 3. Is it improving fast on the measures our mainstream customers care about? | | |
| 4. Is it attached to a business model we'd find unattractive to copy? | | |

## Classification
Sustaining / Low-end disruption / New-market disruption / Counter-positioning / Aggregator (taking the user relationship)

## Which of our customers are exposed first
[Segment, channel or persona]

## Response
- If sustaining: product, sales and pricing response:
- If disruptive: separate offer, unit or business model considered? [yes/no, why]
- Owner:
- Review date:
```

```template id="16-commoditization-response-plan" title="Commoditization response plan"
# Commoditization response plan · [Feature] · [Date]

**Owner:** [PM]   **Decision maker:** [name]   **Decide by:** [date]

## 1. The feature and the force
- Feature:
- Commoditizing force (model provider / platform bundle / open source / AI assistant / new entrant):
- Evidence that "good enough" alternatives exist (source):
- Share of revenue, usage or deals that depend on it today:

## 2. Product or complement?
Is this feature what customers pay us for, or something that makes the thing they pay for more valuable?
[Product / Complement], because:

## 3. Disruption check
Result of the disruption test (attach): [sustaining / disruptive / aggregator]

## 4. Options
| Option | What we'd do | Revenue effect | Cost effect | Risk | Fit with our Powers |
|---|---|---|---|---|---|
| Move up the stack (sell the outcome) | | | | | |
| Bundle into a system with fit | | | | | |
| Reprice (include it, or price on outcomes) | | | | | |
| Commoditize it ourselves (open it, make it standard) | | | | | |
| Harvest and exit | | | | | |

## 5. Decision
- Chosen response:
- What we stop doing:
- Customer and sales communication needed:
- Metrics to watch (three at most):
- Review date:
```

```template id="16-competitive-threat-monitor" title="Competitive threat monitor"
# Competitive threat monitor · [Product] · [Month]

**Drafted by:** AI harness from [connected sources]   **Validated by:** [PM]   **Reviewed with:** [product marketing, sales leader]

Rule: nothing enters the monitor without a cited source and a human check.

| Threat | Type (sustaining / low-end / new-market / counter-positioning / aggregator) | Signal observed | Source (link or record) | Moat row it attacks | Severity (H/M/L) | Trigger for action | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## Changes since last month
- New threats:
- Threats that grew:
- Threats that faded:

## Triggers hit this month
| Trigger | What happened | Action taken or proposed | Decision maker |
|---|---|---|---|
| | | | |

## Sources scanned
Win/loss notes · CRM opportunity notes · support tickets · call summaries · competitor release notes and pricing pages · partner feedback · analyst notes
```

## Prompts

```prompt title="Stress-test our claimed moats with 7 Powers"
Goal: Find out which of your claimed advantages are real Powers and which are features or hopes.
Paste in: the differentiation claims from your strategy and board decks, plus any evidence you have (win rates, discounts, renewal and expansion rates, margin trends). This is confidential; use an approved tool.

Act as a skeptical strategy advisor who knows Hamilton Helmer's 7 Powers framework. For [product]:

1. List each claimed advantage. Map it to one of the seven Powers (scale economies, network economies, counter-positioning, switching costs, branding, cornered resource, process power), or to "none".
2. For each, write the benefit in cash-flow terms (higher price, lower cost, less investment) and the barrier in competitor terms (what would it cost a capable rival to copy this, and why wouldn't they?).
3. Mark each as present, emerging or absent. A Power with no barrier, or no evidence, is absent.
4. Flag any claim that is really operational excellence, a data scale effect, or model access.
5. Name the one or two Powers most worth deepening, and the roadmap work that would build the barrier rather than the benefit.

Use only the evidence I give you. Where evidence is missing, write "No evidence" rather than inferring it.

[claims and evidence]

Check the output: for every Power marked present, read the barrier cell and ask whether your best-funded competitor would agree it stops them. If the model accepted "our data" or "our AI" as a Power without a barrier, push back.
```

```prompt title="Argue the competitor's case against our moat"
Goal: Hear the strongest case for why your moat won't hold, before a competitor proves it.
Paste in: your moat scorecard or 7 Powers assessment, and a short profile of your most capable competitor from public sources.

You are the head of strategy at [competitor]. Your CEO has asked how to take [product]'s best customers within 18 months. Using the assessment and profile below:

1. Identify which of [product]'s claimed barriers you could get around, and how (copy, bundle, reprice, partner, use standard connectors or protocols, or go after a segment they ignore).
2. Identify which barriers you could not get around, and why.
3. Say whether your attack would be sustaining (a better product for their best customers) or disruptive (cheaper or simpler, for the low end or for nonconsumers, with a business model they'd find unattractive).
4. Name the first customers you'd target and the message you'd use.

Be specific and concrete. Don't invent facts about either company; where you're assuming, say so.

[assessment]
[competitor profile]

Check the output: the barriers the model couldn't get around are your candidate moats. Test each against real deal evidence. Treat the attack plan as a hypothesis, not a forecast.
```

```prompt title="Run the disruption test on a new entrant"
Goal: Decide whether a new competitor is a sustaining threat or a disruptive one.
Paste in: the entrant's public material (website, pricing page, release notes, launch posts) and a description of your mainstream customers and the measures they judge you on.

Using Clayton Christensen's definition of disruption (a foothold at the low end or among nonconsumers, worse on the incumbent's traditional measures at first, improving until good enough for the mainstream), assess [entrant] against [product].

Answer each question with yes or no and the evidence from the material:
1. Is it worse on the measures our customers use to judge us today?
2. Is it cheaper or simpler, or does it serve people who don't buy from anyone today?
3. Is it improving fast on the measures our mainstream customers care about?
4. Is it attached to a business model we'd find unattractive to copy?

Then classify it: sustaining, low-end disruption, new-market disruption, counter-positioning or aggregator. Name which of our customer segments are exposed first.

Don't call something disruptive just because it's new, well funded or uses AI.

[entrant material]
[our customers and measures]

Check the output: confirm every "yes" cites the entrant's actual material. If the model called a better product for your best customers "disruptive," correct it: that's sustaining.
```

```prompt title="Draft a commoditization response plan"
Goal: Decide what to do with a feature that competitors, platforms or AI assistants now offer as good enough.
Paste in: a description of the feature, evidence that alternatives exist, the revenue or deals that depend on it, and your current 7 Powers assessment.

For [feature] in [product], draft a commoditization response plan.

1. Name the commoditizing force: model provider, platform bundle, open source, AI assistant or new entrant.
2. Decide whether the feature is our product (what customers pay for) or a complement (something that makes our product more valuable). Explain the reasoning.
3. Evaluate five responses: move up the stack and sell the outcome; bundle into a system with our other activities; reprice; commoditize it ourselves by opening or standardizing it; harvest and exit. For each, give the revenue effect, cost effect, main risk and fit with our Powers.
4. Recommend one response, what we'd stop doing, and three metrics to watch.

Don't recommend defending the feature on features alone unless you can name a barrier.

[feature, evidence, assessment]

Check the output: if the recommendation is "add more features," ask what the barrier is. Check the revenue effects against your own numbers before sharing the plan.
```

```prompt title="Build this month's competitive threat monitor"
Goal: Turn scattered competitive signals into a short, sourced monitor you can review in 30 minutes.
Paste in (or connect the harness to): win/loss notes, CRM opportunity notes, support tickets, call summaries, competitor release notes and pricing pages, and last month's monitor. These include customer data; use an approved tool and leave out personal identifiers.

From the sources provided for [product], build this month's competitive threat monitor.

For each signal:
- Describe what was observed, in one line, with the source record or link.
- Classify the threat type: sustaining, low-end, new-market, counter-positioning or aggregator (someone else taking the user relationship).
- Name which moat source it attacks, using these rows: [paste your moat scorecard rows].
- Rate severity (H/M/L) and say which trigger, if any, it hits: [paste your triggers].

Group related signals into one threat. List what's new, what grew and what faded since last month's monitor. Don't include any signal you can't cite.

Check the output: open three of the cited sources and confirm the signal is described accurately. Read every High-severity item yourself before it goes to the review meeting.
```

```prompt title="Test a data moat claim"
Goal: Find out whether "our data" is a real barrier or a scale effect that will plateau.
Paste in: a description of the data asset (what it is, how it's collected, who else could collect it, how it's used in the product), and any evidence that more data has improved the product.

Assess whether [data asset] gives [product] a defensible advantage. Use these tests:

1. Is the data proprietary or hard to get, or could a competitor assemble a "minimum viable corpus" from public sources, customers' own systems or standard connectors?
2. Is it refreshed by use, or does it go stale?
3. Is it concentrated in the hard, rare cases that matter most, or in common cases rivals already handle?
4. Does more data still improve the product, or has improvement flattened?
5. Does the improvement drive adoption, pricing or retention, with evidence?
6. Is access protected by contract or position (a cornered resource), or only by being first?

Conclude with one of: real barrier, data scale effect with diminishing returns, or not an advantage. Say what evidence would change the verdict.

[data asset description and evidence]

Check the output: if the model concluded "real barrier," confirm that the answer to question 1 names something a competitor truly can't get. Compare the verdict with your Chapter 14 data network effects test.
```

## Anti-patterns

:::warn The feature list as a moat slide
"Our differentiation" lists six features, each of which a competitor could build in a quarter. Features are operational effectiveness. A moat has a barrier: something that stops a capable rival from copying the benefit. Move the features to the roadmap and put only Powers on the strategy slide.
:::

:::warn "Proprietary AI"
The product calls the same frontier models every competitor can call, and the deck calls it proprietary. Model access is a supplier relationship with no barrier. Claim the context, workflow position or outcome data you've built around the model, if you have them.
:::

:::warn The data network effect that isn't
Every new customer adds data, so the team calls it a network effect. Usually it's a scale effect with diminishing returns that a rival can match with a good-enough corpus. Test it before you put it in front of the board, and measure whether more data is still improving the product.
:::

:::warn Calling every threat disruption
A well-funded competitor launches a better product for your best customers, and the team calls it disruption. That's a sustaining threat, and you fight it with product, sales and price. Save "disruption" for threats that pass all four questions, because the response is very different.
:::

:::warn Defending a commodity
A feature that platforms now bundle for free keeps getting roadmap investment because it was once the product's headline. Decide whether it's your product or a complement. If it's a complement, include it, open it or retire it, and spend the engineering time on the layer you can defend.
:::

:::warn The integration count as a switching cost
"We have 200 integrations" made sense when each connector was expensive to build. With standard protocols, integration breadth is cheap to match. Count depth instead: what can be done safely through the connector, and what you learn from it.
:::

:::warn The moat review that never repeats
The assessment gets done once for a strategy offsite and never revisited. Moats widen and narrow every year, often quietly. Put the review on the calendar annually, ask Buffett's question for every row, and run the threat monitor monthly in between.
:::

## Checklist

- [ ] Every claimed advantage has been mapped to one of the 7 Powers or marked "none."
- [ ] Each Power marked present has a benefit in cash-flow terms, a barrier in competitor terms and sourced evidence for both.
- [ ] Model access is scored as a supplier relationship, not a moat.
- [ ] Any data moat claim has been tested for exclusivity, freshness, coverage of hard cases, diminishing returns and effect on adoption.
- [ ] The moat scorecard includes a widened, stable or narrowed verdict for every row this year.
- [ ] The three most serious threats have been run through the four-question disruption test and classified.
- [ ] Every feature facing good-enough alternatives has a decision: product or complement, and a chosen response.
- [ ] The one or two Powers to deepen are named, with barrier-building roadmap items and a metric for each.
- [ ] Pricing decisions (Chapter 15) reflect where the product has real pricing power.
- [ ] For AI products, inference cost per outcome is tracked and the architecture allows switching models.
- [ ] Trust mechanisms (cited evidence, approval gates, audit logs) are treated as part of the moat, with an owner.
- [ ] A monthly competitive threat monitor runs, with every entry sourced and validated by a person.
- [ ] The assessment and decisions are in the decision log, with a review date a year out.

## Key takeaways

- A moat needs both a benefit that improves cash flow and a barrier that stops rivals from copying it. Most claimed advantages have the first and not the second.
- Porter and Helmer agree that doing the same things better than rivals doesn't last. Durable advantage usually comes from a system of activities that fit together, which rivals have to copy all at once.
- Disruption is a specific process: a foothold at the low end or among nonconsumers, worse at first, improving until good enough. A better product for your best customers is a sustaining threat.
- In AI-era software, model access is a commodity input, integration breadth is standardizing and data moats are usually weaker than claimed. Workflow depth, exclusive context, outcome data, trust and distribution are where defensibility holds.
- When a feature gets commoditized, decide whether it's your product or a complement, then move up the stack, bundle, reprice, open it up or exit.
- Review the moat every year by asking which advantages widened and which narrowed, and watch competitive signals monthly with an AI harness that cites its sources.
