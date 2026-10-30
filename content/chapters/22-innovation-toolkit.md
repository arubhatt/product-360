<p class="lead">Innovation strategy (Chapter 20) tells you where to bet, and the competencies in Chapter 21 make each bet cheaper to test. This chapter covers the mechanisms a company uses to find, fund and capture new ideas: fourteen of them, from a two-day hackathon to a full acquisition. Each fits a different kind of bet, costs a different amount and fails in its own way. The PM's job is to pick the right one for the question at hand and make sure whatever it produces lands in a product.</p>

## Why this matters

Most enterprise companies already run several innovation mechanisms: an annual hackathon, an idea portal, a corporate development team, perhaps a venture fund and a few university relationships. What they rarely have is a reason for using one rather than another. The hackathon runs because it ran last year. The idea portal collects ideas nobody owns. The venture fund invests in startups the product teams have never heard of.

Steve Blank has a name for the result: **innovation theater**. In his telling, it's what happens when a company produces impressive projects, demo days and press releases while the product direction stays exactly where it was. It usually comes from poor fit or missing follow-through: the mechanism was wrong for the question, or nobody planned what would happen to the output.

A Senior or Principal PM is well placed to fix both. You know which questions the roadmap can't answer yet, and you own the place where innovation output has to land. That makes you the natural owner of two decisions innovation programs usually leave open:

1. **Which mechanism fits this bet?** A feasibility question calls for a hackathon or a prototype. An adoption question calls for design partners. A "does this exist already?" question calls for a venture client pilot. A "we need this capability within a year and can't build it" question calls for a license, a partnership or an acquisition.
2. **Where does the output go?** Every mechanism needs a named receiving owner, a budget for follow-on work and a decision date, agreed before the mechanism starts.

The AI era raises the stakes. Prototypes are now cheap, so hackathons and experiments produce far more output, and more of it dies in a demo folder. Meanwhile the "buy" side of the toolkit has changed shape. Between 2024 and 2025 several high-profile AI deals were license-and-hire arrangements rather than classic acquisitions. And every AI product team now depends on a model provider, which is itself a build, partner or buy decision.

:::key The PM owns fit and follow-through
Innovation programs often belong to a central team. The choice of mechanism for a specific product bet, and the plan for what happens to its output, belong to the PM who will have to ship the result. If you can't name the receiving owner and the follow-on budget before a mechanism starts, you're scheduling theater.
:::

## The innovation toolkit

### Two pipes: open innovation

Henry Chesbrough's open innovation, set out in 2003, is the frame that holds the toolkit together. His argument is that firms can and should use outside ideas as well as their own, and outside paths to market as well as internal ones. That gives you two pipes.

- **Inbound** brings outside knowledge in: licensing a patent or technology, buying a startup's product, working with a university lab, co-developing with customers, acquiring a company.
- **Outbound** takes unused inside knowledge out: licensing technology to others, spinning out a product that isn't core, opening an interface so partners can build on your platform.

A third, coupled mode combines the two in alliances and joint development, where knowledge flows both ways at once.

The story Chesbrough drew on is Xerox PARC. The lab invented much of what became the modern desktop computer, but Xerox captured little of the value. Its Star workstation sold only about 25,000 units, and staff and spin-outs (Metaphor in 1982, among others) carried PARC's ideas to other companies. Xerox eventually donated PARC to SRI International in 2023. The lesson for a PM is that a closed innovation system loses ideas it can't use. An open one at least gets to decide what happens to them.

Open innovation has known costs: revealing information, risking advantage through disclosed intellectual property, accepting less control and the hard work of absorbing ideas invented elsewhere. The last is the one PMs feel most. A startup pilot or university result that nobody inside has time to integrate is wasted, however good it is.

For a platform PM, the most important outbound lever is usually an open interface. A public API, a published connector specification or an MCP server lets partners and customers build on your product without you funding the work. Chapter 14 covers platform strategy; here, the point is that outbound is a product decision.

### Match the mechanism to the bet

Before choosing a mechanism, decide what kind of bet you have. Chapter 20 introduced two lenses for that; use them as the front end of the mechanism selector.

**The horizon.** Steve Blank's lean version of the Three Horizons model (the model itself comes from Mehrdad Baghai, Stephen Coley and David White) separates three kinds of work. Horizon 1 executes the current business model, with known metrics and stage-gated delivery. Horizon 2 extends the current business into partly known territory: new customers for an existing product, or new capabilities for existing customers. Horizon 3 searches for a business model nobody has proven yet. Blank's Horizon 3 teams are small (fewer than five people) and talk to more than 100 customers in about ten weeks while building iterative prototypes.

**The ambition.** Bansi Nagji and Geoff Tuff's innovation ambition matrix asks two questions: where you play (existing markets through to new ones) and how you win (existing products and assets through to new ones). The answers sort a bet into core, adjacent or transformational.

Mechanisms tend to produce one band more than others. Hackathons, idea challenges and design partner programs mostly feed Horizon 1 and 2 work. Incubators, venture capital and acquisitions are Horizon 2 and 3 tools. A hackathon can't answer a Horizon 3 business model question in two days, and an acquisition is an expensive way to get a Horizon 1 feature.

**The organizing rule.** Charles O'Reilly and Michael Tushman's work on the ambidextrous organization (2004) is the standard reference on where new work should live. As it's usually taught, breakthrough units do best when they're structurally separate from the core business but tied to it at the senior level through a shared strategy. Blank adds practical rules: give Horizon 3 teams their own plans, incentives and metrics; embed legal, finance and procurement people so the team can get to a yes; reward core-business managers for supporting new work; and decide in advance how a successful project graduates, whether by absorption, spin-out or a new standalone unit. Chapter 23 covers graduation.

:::onramp If the horizon language is new to you
Think of it as three questions. Are we improving what we sell today (Horizon 1)? Are we taking what we have somewhere new (Horizon 2)? Are we looking for a business we don't have yet (Horizon 3)? The further out, the smaller and more separate the team, the more customer conversations per week and the less the work should be judged by revenue this year.
:::

### The fourteen mechanisms

The table compares the full toolkit. Costs are relative to each other, not budgets.

| Mechanism | Fits when | Relative cost and time | Evidence to point to | Main failure modes |
|---|---|---|---|---|
| Idea challenge | You need many problems or ideas quickly, with broad participation | Low; weeks | Netflix Prize; internal challenge programs | No owner or budget for winners; idea graveyard |
| Hackathon | You need to test feasibility, spread a new technology or build energy | Low to medium; one to three days plus preparation | Atlassian ShipIt and Jira Service Desk; the Nolte planning kit | Demo theater; no continuity plan |
| Innovation training | A skills gap blocks adoption of a new approach | Medium; weeks to months | Training built around real projects (Claude Frontier Academy, 2026) | Training with no project attached |
| Intrapreneurship program | People inside have ideas and need air cover | Medium; months | Lockheed Skunk Works; employee-chosen project time | No receiving organization; career risk for participants |
| Internal incubator or accelerator | Several Horizon 2 or 3 bets need protected funding | Medium to high; quarters | Google Area 120 graduates | Cut in downturns; graduation never happens |
| Innovation lab | Long-horizon research, or a signal to talent and customers | High; years | Xerox PARC | Distance from the business; theater |
| Corporate venture capital | You want a view of a market and a pipeline of possible acquisitions | High capital; years | Most units mix strategic and financial aims | Strategic and financial goals conflict |
| Startup partnership and venture client | A startup already solves a real problem you have | Low to medium; weeks to months | BMW Startup Garage | Procurement and security drag; pilot purgatory |
| Open innovation programs | Knowledge sits outside, or unused assets sit inside | Varies | Chesbrough; the PARC lesson | Intellectual property leakage; not-invented-here |
| Co-development with design partners | You need real workflows and data to shape a product | Medium; one to three quarters | Practitioner practice; no rigorous study | Custom work for one loud customer |
| University partnership | Hard research questions; recruiting | Medium; multi-year | MIT-IBM lab (2017) | Timelines and IP terms out of sync |
| Licensing, in or out | The asset is well defined and tradable | Low to medium | Arm's licensing model | Royalty stacking; dependency |
| Acqui-hire, license-and-hire, acquisition | You need a team or capability faster than you can build it | Very high; months | 2024 to 2025 AI talent deals | Integration failure; regulatory scrutiny; talent leaving |
| Spin-out | An asset is valuable but not core | Medium | Byteboard from Area 120; Metaphor from PARC | Parent keeps too much control, or none |

The fourteen fall into four families.

**Mechanisms that harvest ideas and skills from inside.** Idea challenges, hackathons, training and intrapreneurship programs all draw on what employees already know. They're cheap, fast and good at surfacing problems, feasibility and talent. Their shared weakness is continuity: they produce output faster than the organization can absorb it.

Idea challenges descend from prize competitions such as the Netflix Prize: $1 million offered in 2006 for a 10% better recommendation algorithm, won in 2009 by BellKor's Pragmatic Chaos with 10.06%. In B2B, an internal challenge's value is often in the problems submitted: asking field engineers and support staff what customers work around every week is discovery at scale.

Innovation training is shifting toward residencies. Anthropic's Claude Frontier Academy, announced in October 2026 with $100 million of backing, aims to train 10,000 engineers by the end of 2027 through a multi-day program and a 12-week residency in which each engineer leads a real project at their own organization. No outcome data exists yet, so treat it as a design pattern rather than proof. Training that ends in a shipped project at the learner's own company is a stronger design than training that ends in a certificate.

Intrapreneurship, a term Gifford and Elizabeth Pinchot coined in 1978, gives employees the air cover to pursue a new venture inside the company. Lockheed's Skunk Works, set up in 1943, is the classic structural example. These programs need a named organization ready to receive a successful project, and a promise that joining won't damage anyone's career. Without both, the best people stay away.

**Structures that protect new work.** Incubators, accelerators and labs give new bets protected money and time, which makes them the most expensive internal options and the most exposed to budget cuts. Google's Area 120, created in March 2016, shows both sides. Some projects graduated: the Aloud dubbing tool moved into YouTube's auto-dubbing in 2023, and Byteboard spun out as an independent company in 2021. But Area 120 was moved under Google Labs in November 2021 and significantly reduced in the January 2023 layoffs. An incubator without graduation criteria and a receiving organization becomes an easy line to cut.

**Mechanisms that bring the outside in.** Corporate venture capital, startup partnerships, design partners, university partnerships and licensing all reach outside the company. They usually cost less and move faster than building, at the price of control and the work of absorbing what comes back.

University partnerships, such as the MIT-IBM lab set up in 2017, suit hard research questions with long timelines. They fail when product teams expect quarterly results, or when nobody settles intellectual property ownership until after it exists. Licensing in suits a well-defined asset that a contract can protect. Licensing out turns an internal asset into revenue: Arm built its business on designing processor technology and licensing it to chipmakers for fees and royalties, rather than manufacturing chips.

**Mechanisms that change ownership.** Acquisitions, acqui-hires, license-and-hire deals and spin-outs move assets, people or both across the company boundary. They're the hardest to unwind and are covered below.

### Hackathons that change the roadmap

Most PMs run a hackathon long before they touch an acquisition. Atlassian's ShipIt is the standard example of a hackathon with product impact: a 24-hour event in which, according to Atlassian, five employees built a simpler portal for raising Jira issues that became Jira Service Desk.

The most useful planning structure comes from a research planning kit by Alexander Nolte, James Herbsleb, Kiev Gama and Abasi-amefon Affia-Jomants, first published in 2020 and revised in 2025. It breaks a hackathon into twelve decisions:

1. **Goal:** what do you want to achieve?
2. **Theme:** what is the overall theme?
3. **Competition or cooperation:** do teams compete for prizes or work together?
4. **Stakeholder involvement:** how do people from outside take part?
5. **Participant recruitment:** who should come?
6. **Specialized preparation:** what will teams need in order to take part?
7. **Duration and breaks:** how long and how intense?
8. **Ideation:** when and how do teams develop ideas?
9. **Team formation:** how do people with shared interests find each other?
10. **Agenda:** what happens during the event?
11. **Mentoring:** how will you support participants?
12. **Continuity planning:** what happens after it ends?

The kit's authors recommend setting goals about four months ahead and naming the tensions you'll have to manage: the organization's goals against participants' personal ones, illustrating a concept against producing something useful, challenging against achievable, speed against quality. Their most important point concerns the last decision: "continuity does not come for free." Plan it before the event and tie the event to a wider strategy. Outcomes worth continuing include product extensions, reusable technology, community and learning, as well as new ventures.

For a B2B product team, three adaptations matter. Pick a goal the roadmap needs answered. Give teams realistic data and systems, cleared by security in advance. Judge on measured results against a shared test set rather than demo polish. The AI lens section turns these into rules for AI hackathons.

### Design partners and co-development

A design partner is a customer who helps shape a product before general availability, sharing workflows and data and giving scheduled feedback in return for early access and influence. In B2B and platform businesses, design partners are often the most valuable inbound mechanism, because the knowledge you need (how a workflow really runs, what security will approve, what a buyer will pay for) sits inside customers.

We found no rigorous study of design partner programs, so the guidance here is this book's own practice, built around the mechanism's familiar failure modes.

- **Choose partners for representativeness, not enthusiasm.** The most eager customer is often the least typical. Pick partners who match the target segment, who will share data and who have an executive sponsor.
- **Make commitments run both ways.** The partner commits to a feedback cadence and to letting you use what you learn. You commit to early access, a named contact and usually some pricing protection.
- **Guard against custom work.** The classic failure is building one loud partner's special requirements into the product. Ship a partner-requested feature only if it serves several partners.
- **Set an end date and exit rules.** When the program ends, partners convert to paying customers on normal terms or leave.

Chapter 01 covers the discovery interviewing that sits inside a design partner program. Chapter 21 covers the experiments you run with partners.

### Venture clients and corporate venture capital

When a startup may already have solved your problem, the fastest path is often to become its customer. The **venture client** model, associated with Gregor Gimmy and BMW, builds on this idea: the company buys and uses a startup's product for a strategic purpose, without taking equity. BMW's Startup Garage, founded in 2015, describes itself as the first venture client unit. Its process runs from discovery through assessment, a purchase order that makes the startup a supplier, a proof of concept and, if it works, a long-term partnership. BMW reports assessing more than 6,000 startups, piloting more than 280 and turning more than 38 into regular suppliers, with four to eight weeks from first contact to evaluation. The numbers are self-reported; the process is the useful part.

For an enterprise PM, a venture client pilot answers a fit question ("does this work in our workflow?") in weeks rather than quarters, and it surfaces the real obstacles early. Those are usually procurement and security review. Involve your security reviewer and procurement contact from the first week; pilot purgatory, where a successful pilot never becomes a contract, is the mechanism's signature failure.

**Corporate venture capital** takes equity in startups through a fund. Its aims are strategic (a view of a market, access to technology, a pipeline of acquisitions), financial or, most often, both, with strategic fit screened first. The acquisition pipeline matters. In the United States in 2024, according to PitchBook and NVCA data, 1,083 of 1,147 venture-backed exits were acquisitions and only 42 were IPOs. Acquisition is the usual exit, so a corporate fund often doubles as a scouting channel for corporate development.

Most PMs don't run a fund. Your job is to give the fund a thesis (which problems matter to the roadmap over the next two to three years) and to run the pilot when a portfolio company fits. When strategic and financial goals conflict, the thesis keeps the fund useful to product.

### Build, partner or buy

The hardest toolkit decision is whether to build a capability, get it through a partner or buy it. Laurence Capron and Will Mitchell's research on resource pathways is the most useful guide. Their premise: new strategies need new resources, no company can build everything, and licensing, alliances and acquisitions are all legitimate routes. Their warning is that companies fall back on the path they habitually use, which they call the implementation trap. In practice, an engineering-led company builds by reflex and an acquisitive one buys by reflex.

Their framework is a sequence of questions. This book uses it in the following form.

1. **Are our internal resources relevant?** If the knowledge, skills and organizational fit are close enough to what the new capability needs, build it.
2. **If not, is the resource tradable?** If a contract or license can define and protect what you need, borrow it by contract: license it or buy it as a service.
3. **If not, how close do we need to be to the partner?** If a bounded collaboration with aligned goals is enough, borrow it through an alliance, such as co-development or a joint program.
4. **Only if deep integration is needed, and feasible, buy.** Acquisition comes last.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 380" role="img" aria-label="Build, partner or buy decision sequence: four questions leading to build, license, alliance or acquire">
  <rect x="20" y="20" width="300" height="56" rx="10" class="box"/>
  <text x="36" y="44" class="t">1. Are internal resources relevant?</text>
  <text x="36" y="63" class="s">Knowledge, skills and organizational fit</text>
  <rect x="20" y="110" width="300" height="56" rx="10" class="box"/>
  <text x="36" y="134" class="t">2. Is the resource tradable?</text>
  <text x="36" y="153" class="s">Can a contract define and protect it?</text>
  <rect x="20" y="200" width="300" height="56" rx="10" class="box"/>
  <text x="36" y="224" class="t">3. Is a bounded collaboration enough?</text>
  <text x="36" y="243" class="s">Limited joint work, aligned goals</text>
  <rect x="20" y="290" width="300" height="56" rx="10" class="box"/>
  <text x="36" y="314" class="t">4. Is deep integration needed?</text>
  <text x="36" y="333" class="s">And feasible? If not, rethink the plan</text>
  <line x1="170" y1="76" x2="170" y2="110" class="ln"/>
  <line x1="170" y1="166" x2="170" y2="200" class="ln"/>
  <line x1="170" y1="256" x2="170" y2="290" class="ln"/>
  <text x="178" y="98" class="s">no</text>
  <text x="178" y="188" class="s">no</text>
  <text x="178" y="278" class="s">no</text>
  <line x1="320" y1="48" x2="400" y2="48" class="ln" style="stroke:var(--a1)"/>
  <line x1="320" y1="138" x2="400" y2="138" class="ln" style="stroke:var(--a1)"/>
  <line x1="320" y1="228" x2="400" y2="228" class="ln" style="stroke:var(--a1)"/>
  <line x1="320" y1="318" x2="400" y2="318" class="ln" style="stroke:var(--a1)"/>
  <text x="346" y="40" class="s" style="fill:var(--a1)">yes</text>
  <text x="346" y="130" class="s" style="fill:var(--a1)">yes</text>
  <text x="346" y="220" class="s" style="fill:var(--a1)">yes</text>
  <text x="346" y="310" class="s" style="fill:var(--a1)">yes</text>
  <rect x="400" y="24" width="225" height="48" rx="10" fill="var(--surface-2)" stroke="var(--a1)"/>
  <text x="414" y="45" class="t" style="fill:var(--a1)">Build</text>
  <text x="414" y="62" class="s">Internal team, hackathon, incubator</text>
  <rect x="400" y="114" width="225" height="48" rx="10" fill="var(--surface-2)" stroke="var(--a2)"/>
  <text x="414" y="135" class="t" style="fill:var(--a2)">Borrow by contract</text>
  <text x="414" y="152" class="s">License, venture client, service</text>
  <rect x="400" y="204" width="225" height="48" rx="10" fill="var(--surface-2)" stroke="var(--a2)"/>
  <text x="414" y="225" class="t" style="fill:var(--a2)">Borrow by alliance</text>
  <text x="414" y="242" class="s">Design partners, co-development</text>
  <rect x="400" y="294" width="225" height="48" rx="10" fill="var(--surface-2)" stroke="var(--a3)"/>
  <text x="414" y="315" class="t" style="fill:var(--a3)">Buy</text>
  <text x="414" y="332" class="s">Acquire, or license-and-hire</text>
  <text x="20" y="370" class="s">Each "no" moves one step further from control and one step closer to integration cost.</text>
</svg>
<figcaption>The build, partner or buy sequence, adapted from Capron and Mitchell's resource pathways. Acquisition is the last question, not the first. In 2026, add two checks at every step: dependency on a model provider, and whether you need the team or only the technology.</figcaption>
</figure>

Two 2026 additions fit the framework to AI products. The first is **model-provider dependency**: a team using a frontier model has already made a partner decision, often without calling it one. Inference cost, switching costs and contract terms belong in the analysis. The second is the **talent-only path**: since 2024, "buy" has split into buying a company, buying a team and licensing technology, and each option leaves customers in a different place.

### Acquisitions, acqui-hires and license-and-hire

Acquisitions are the most expensive mechanism, with the worst reputation. Clayton Christensen, Richard Alton, Curtis Rising and Andrew Waldeck wrote in 2011 that study after study puts the failure rate of mergers and acquisitions "somewhere between 70% and 90%." The range summarizes other studies and is contested, so treat it as a warning rather than a measurement.

Their proposed discipline is to judge a deal by what it does to the acquirer's business model: the value proposition, resources, processes and profit formula. A deal that **leverages** the existing business model (it adds a capability your customers, sales motion and pricing can absorb) can be integrated. A deal that **reinvents** the business model (a different customer, price point or way of making money) should usually be kept separate, so the acquirer doesn't crush what it paid for under old processes. For a PM, that becomes one question on the acquisition brief: does this target extend our model or change it? Integration depth follows the answer.

The AI era added a new deal shape. In a **license-and-hire** deal (sometimes called a reverse acqui-hire), a large company hires a startup's founders and key staff and pays a license fee for its technology, which lets investors get a return while a smaller company carries on. Four public deals show the pattern and its variations:

- **Microsoft and Inflection, March 2024.** Microsoft hired Inflection's co-founders and most of its roughly 70 staff and paid about $650 million to license its technology. The UK Competition and Markets Authority treated the deal as a merger situation and cleared it in September 2024.
- **Google and Character.ai, August 2024.** Google hired co-founder Noam Shazeer and took a non-exclusive license to the company's technology.
- **Meta and Scale AI, June 2025.** Meta agreed to buy a 49% non-voting stake for about $14.8 billion, and Scale's chief executive, Alexandr Wang, joined Meta.
- **Google and Windsurf, July 2025.** Google reportedly paid about $2.4 billion in a license-and-hire deal for Windsurf's chief executive and senior staff. Within days, on July 14, 2025, Cognition signed an agreement to acquire the rest of Windsurf: its intellectual property, product, brand, about $82 million of annual recurring revenue, more than 350 enterprise customers and the remaining staff, with vesting accelerated for all employees.

The Windsurf sequence is the one to study. "Buy" now has at least three versions (the company, the team, the technology), and each leaves the target's customers in a different position: a license-and-hire can strand them with a weakened company, while a full acquisition takes on their contracts. On the buying side, the customer outcome belongs in the brief. If you depend on a startup supplier, it's a risk to watch.

**Spin-outs** run the other way. When an asset is valuable but not core, it can leave as an independent company; Byteboard's 2021 spin-out from Area 120 and Metaphor's 1982 departure from PARC are two examples. The PM's question is how much connection to keep: a commercial agreement, a minority stake or nothing. A parent that keeps too much control smothers the spin-out; one that keeps none loses the option to bring it back.

## How to apply it

Use this method whenever a bet in the roadmap or innovation portfolio (Chapter 20) needs something normal delivery can't provide. The selection steps take a few days of PM time.

**Frame the bet.**

1. Write the bet as a question, not a solution. "Can we convert runbooks into supervised agents that pass our safety evals?" is a question. "Build a runbook agent" is a solution looking for permission.
2. Place it on the horizon and ambition lenses from Chapter 20: core, adjacent or transformational; Horizon 1, 2 or 3. Note the time by which you need an answer.
3. Name the type of uncertainty that blocks it. Most bets are blocked by one of five: *feasibility* (can it be built?), *desirability and adoption* (will customers use it and will their security teams approve it?), *availability* (does someone already have it?), *capability* (do we have the skills and people?) or *business model* (can we make money from it?).

**Choose the mechanism.**

4. Map the uncertainty to a short list of mechanisms. Feasibility points to hackathons, internal prototypes and university partnerships. Desirability and adoption point to design partners and co-development. Availability points to venture client pilots and licensing. Capability points to training, partnerships, acqui-hires and acquisitions. Business model points to incubators and design partners, and at the far end to acquisitions that bring a proven model.
5. Run the build, partner or buy questions on the short list. Start with "are our internal resources relevant?" and move outward only when the answer is no. Add the two 2026 checks: model-provider dependency, and whether you need the team or only the technology.
6. Score the candidates on cost, time to an answer, control, customer impact and reversibility. Pick the cheapest mechanism that can answer the question in time. Write the reason down on the mechanism selector.

**Plan the landing before the launch.**

7. Name the receiving owner: the PM and engineering leader who will own the output if it works. If nobody will sign, stop here.
8. Reserve follow-on capacity in advance: a sprint, a quarter's slot or a budget line, depending on the mechanism.
9. Set the decision date and the evidence that will decide it. Use the same discipline as an experiment card in Chapter 21: thresholds written before the work starts.
10. Bring in security, legal and procurement early for anything that touches outside parties or production data. Gatekeepers who hear last turn successful pilots into stalled ones.

**Run, decide and record.**

11. Run the mechanism using the plan for its type (the hackathon plan, design partner program plan or acquisition brief in this chapter).
12. On the decision date, make one of four calls: absorb into the roadmap, continue with a new question, hand to a different mechanism (a successful hackathon prototype often becomes a design partner pilot) or stop.
13. Record the decision and the evidence in the decision log, and update the portfolio view in Chapter 20. Chapter 23 covers how successful bets scale.

:::leader For product leaders
Review the toolkit as a portfolio once a quarter. For each mechanism the organization runs, ask three questions: which roadmap decisions did it change this year, what did it cost, and which outputs are waiting for a receiving owner? A mechanism that can't point to a changed decision in a year is theater. Fund the mechanisms that land, and stop the ones that don't.
:::

## The AI lens

### Building AI-powered products

AI changes the toolkit in four ways that matter for anyone building AI-powered products.

**Your model provider is a partner decision.** Every product built on a frontier model depends on a supplier for its most important component. Give that relationship the same rigor as any other build, partner or buy decision. Regulators have examined the same questions. In January 2024 the US Federal Trade Commission issued orders to Alphabet, Amazon, Anthropic, Microsoft and OpenAI to study investments and partnerships in generative AI. Its staff report, published in January 2025, described cloud partners holding equity, revenue-sharing rights and in some cases control or exclusivity rights, and raised concerns about switching costs and access to sensitive information. Those regulatory concerns are also your commercial risks. Before you deepen a model partnership, know what it would cost to switch, what the provider can see and whether the terms limit who else you can work with. A portable abstraction layer between your product and the model, plus an evaluation suite that runs against any model, keeps the partnership a choice you can revisit.

**Connectors make partnering cheaper.** Anthropic introduced the Model Context Protocol in November 2024 as an open standard for connecting AI assistants to the systems where data lives. Standard connectors lower the cost of several mechanisms. A design partner can connect a prototype to their own tools in days, a hackathon team can build against realistic systems instead of mock data, and a platform can open itself to partners by publishing an MCP server. That last one is an outbound open innovation move.

**Agent prototypes need a judging rule.** AI hackathons tend to produce agents that impress in a demo and fail on real cases. Erik Schluntz and Barry Zhang's guidance on building effective agents (Anthropic, December 2024) supplies one. They distinguish workflows, where code fixes the sequence of model and tool calls, from agents, where the model directs its own steps and tool use. They recommend starting with the simplest solution, often a single well-grounded model call, and adding complexity "only when it demonstrably improves outcomes." Ask every team which pattern it used, and for an eval result that justifies anything beyond a workflow. Chapter 31 covers evals.

**Buy has new shapes.** License-and-hire deals, minority stakes with key hires and full acquisitions of the remaining business are all now normal in AI. On the buying side, choose the shape by what customers need as well as what you need. If you depend on an AI startup as a supplier, a license-and-hire deal can take its founders and key engineers at short notice.

### Doing the work with AI

An AI harness with connectors to your documents, CRM, support tickets and market research does much of the reading and drafting around each mechanism. You keep the judgment.

- **Scouting.** A harness can scan public information on startups in a problem space and draft a long list with the evidence for each claim. Whether a product works in your environment is a question for a venture client pilot.
- **Selecting.** Give the harness your bet, the five types of uncertainty and the mechanism table, and ask it to argue for and against each candidate. It's a useful sparring partner because it names mechanisms you habitually skip, the implementation trap in action.
- **Running hackathons.** The harness can generate a sandbox data set, draft the eval cases from anonymized historical data and score submissions against them consistently. Judges still decide what matters.
- **Running design partner programs.** Partner calls, tickets and usage can be synthesized weekly, with every theme traced to the partners who raised it, which is how you enforce the several-partners rule.
- **Diligence.** For a partnership or acquisition, the harness can read public filings, documentation, security pages and customer reviews, and draft the questions you need answered. Treat its summaries as leads to verify. Anything that touches a confidential deal stays inside tools your company has approved for it, and within a small, named circle.

One widely quoted piece of evidence on building against partnering needs careful handling. In August 2025, Fortune reported on an MIT NANDA study, *The GenAI Divide*, which found that only about 5% of enterprise generative AI pilots delivered rapid revenue acceleration, and that buying from specialized vendors and partnering succeeded about 67% of the time while internal builds succeeded less often. The study's methods (interviews, a survey and a small sample) have been publicly criticized. Use it as a reason to ask whether your team is building what it could buy, and not as proof that partnering wins.

If you run AI training for your product organization, borrow the residency pattern described earlier and end it with a shipped improvement to your own product.

:::ai The one-line rule
AI makes ideas, prototypes and long lists nearly free, and leaves follow-through as expensive as ever. Spend the time it saves on choosing the mechanism, planning the landing and checking the evidence.
:::

## The Beacon case: choosing mechanisms for the Beacon backlog

:::example Where Beacon starts
Beacon itself started inside another product. It launched in 2023 as an AIOps alert-correlation feature inside Northlight Observe and became a standalone product in 2024. Now it's moving from "correlate and summarize" to Beacon Agents, and gross margin has fallen from 81% to 72% because of inference cost. Four bets on the backlog can't be answered by normal delivery. Your VP asks you to propose how to pursue each one before the annual planning review.
:::

**The four bets.** You write each one as a question and name the uncertainty that blocks it.

| Bet | Question | Blocking uncertainty | Mechanism chosen | Why |
|---|---|---|---|---|
| MSP multi-tenant agent console | Will MSPs like Leo's run agents across 60 customers, and how should billing work? | Desirability and business model | Design partner program with five to eight MSPs | The workflow and billing model are unknown, and the partners own the data |
| Change-risk scoring before deploys | Can we score a deploy's risk before it ships? | Availability | Venture client pilot with a startup | A startup may already solve it; the question is fit, not invention |
| Remediation safety evals | How do we prove an agent's remediation is safe enough to run? | Feasibility and credibility | University partnership plus an internal build | A hard research problem, and credibility matters to Sam and to EU customers |
| Runbook-to-agent conversion | Can we turn written runbooks into supervised agents that pass our evals? | Feasibility | AI hackathon | Many engineers hold runbook knowledge, and feasibility is the open question |

The remediation safety bet comes straight out of the hallucinated root cause that led a customer to roll back the wrong service. Sam and the EU customers asking for AI Act documentation want evidence from someone other than Northlight. That's why you pair an outside research partner with the internal eval team, instead of choosing one.

**The hackathon.** You plan "Beacon Agent Days," a two-day event, using the twelve decisions. The goal is three runbook agents that pass an eval on sandbox incidents. The theme is supervised remediation. Teams cooperate and share a connector library. Priya and two customer SREs judge; Sam pre-approves sandbox access two weeks ahead. Preparation means a sandbox with MCP connectors and a replay of anonymized past incidents. The judging rule is measured diagnosis acceptance and safe action rate on the replay, not slide quality. For continuity, each winning agent gets a named PM owner and a one-sprint follow-on slot, agreed with engineering leadership before the event starts.

**The design partner program.** For the MSP console, you select partners on three criteria: multi-tenant scale, willingness to share incident data and an executive sponsor. Partners commit to a feedback session every two weeks and to sharing usage data; Northlight commits to early access, a named PM contact and price protection for the first contract year. You add the rule that matters most for a partner channel: a console feature ships only if at least three partners need it. Leo's company is a partner, and so are MSPs that look less like Leo's.

**The build, partner or buy question.** The biggest decision sits off the backlog list: the diagnosis model layer, which drives the margin problem. You work through the four questions.

- *Are internal resources relevant?* Partly. Northlight has Observe telemetry and a history of resolved incidents, which is the data needed to fine-tune smaller, cheaper models for diagnosis. It has only two applied AI engineers, so a full in-house model program isn't realistic.
- *Is the resource tradable?* Yes. Frontier model access can be bought by contract, and the commercial terms can be negotiated.
- *Is a bounded collaboration enough?* For now, yes. A deeper commercial agreement with a model provider could lower inference cost. You list the risks the FTC report named (switching costs, exclusivity and access to sensitive data) as terms to negotiate.
- *Is deep integration needed?* Not yet. Buying a small team with inference-optimization skills is a real option, and you note it as the fallback if the partnership doesn't move margin within two quarters.

Your recommendation: partner now, behind a portable abstraction layer and a model-agnostic eval suite, and build selectively where Observe data gives an edge, starting with a fine-tuned model for alert correlation. This eases the tension between using Observe data and staying tool-agnostic: the data advantage goes into the models, and the product stays open to other tools through its connectors.

**The acquisition brief.** Corporate development brings you a target: Kestrel, a fictional startup created for this example, which builds Kubernetes remediation agents with unusually strong evals. You write the brief. Kestrel leverages Beacon's business model (same buyers, same incident workflow, compatible pricing), so it could be integrated rather than kept separate. You lay out four options in order of commitment: a venture client pilot first, a minority investment, a license-and-hire for the eval team, or a full acquisition. You note what each does to Kestrel's own customers, because a license-and-hire would leave them with a hollowed-out supplier, the position Windsurf's customers were in until Cognition bought the rest of the company. You set trigger conditions to proceed: the pilot must show Kestrel's evals catch failure cases that Beacon's current evals miss, on Beacon's own incident replay, within eight weeks.

**The decision.** The VP approves all four mechanisms and the model partnership, and asks corporate development to start with the venture client pilot for Kestrel rather than a term sheet. Every mechanism has a receiving owner, and two of them are the other Beacon PMs.

## Product 360 artifacts

```template id="22-innovation-mechanism-selector" title="Innovation mechanism selector"
# Innovation mechanism selector · [Bet name] · [Date]

**Owner:** [PM]   **Decision maker:** [Name]   **Answer needed by:** [Date]

## The bet as a question
[One question the roadmap can't answer yet. No solution language.]

## Placement (from the innovation portfolio, Chapter 20)
- Ambition: Core / Adjacent / Transformational
- Horizon: 1 / 2 / 3
- Why: [one or two sentences]

## Blocking uncertainty (pick the main one)
- [ ] Feasibility: can it be built?
- [ ] Desirability and adoption: will customers use it, and will their security teams approve it?
- [ ] Availability: does someone already have it?
- [ ] Capability: do we have the skills and people?
- [ ] Business model: can we make money from it?

## Candidate mechanisms
| Mechanism | Answers the question? | Cost (L/M/H) | Time to answer | Control | Customer impact | Reversible? |
|---|---|---|---|---|---|---|
| [e.g. hackathon] | | | | | | |
| [e.g. venture client pilot] | | | | | | |
| [e.g. design partners] | | | | | | |

## Build, partner or buy check
1. Internal resources relevant? [Yes / Partly / No, with evidence]
2. Resource tradable by contract? [Yes / No]
3. Bounded collaboration enough? [Yes / No]
4. Deep integration needed and feasible? [Yes / No]
- Model-provider dependency: [none / describe]
- Need the team, or only the technology? [team / technology / both]

## Choice
**Mechanism:** [name]   **Why this one:** [the cheapest mechanism that answers the question in time, and why]
**Rejected and why:** [one line each]

## Landing plan
- Receiving owner (PM and engineering lead): [names, signed]
- Follow-on capacity reserved: [sprint, quarter slot or budget]
- Gatekeepers involved from the start: [security, legal, procurement]
- Decision date: [date]   **Evidence that decides:** [thresholds set now]
- Possible outcomes: Absorb / Continue with new question / Hand to another mechanism / Stop
```

```template id="22-hackathon-plan" title="Hackathon plan"
# Hackathon plan · [Event name] · [Dates]

**Sponsor:** [Exec]   **Owner:** [PM]   **Planning started:** [date, about four months ahead]

## 1. Goal
[What the roadmap needs answered. Measurable: e.g. "three prototypes that pass eval X".]

## 2. Theme
[One theme tied to a named bet.]

## 3. Competition or cooperation
[Choice and why. Shared assets teams can reuse.]

## 4. Stakeholder involvement
- Customer or partner participants and judges: [names]
- Security pre-approval of data and system access: [name, date]

## 5. Participant recruitment
[Who, how many, which skills. Include domain experts, not only engineers.]

## 6. Specialized preparation
- Sandbox environment and connectors: [list]
- Data set (anonymized, approved): [description]
- Eval set and scoring method: [description]
- Templates, starter code, model access: [list]

## 7. Duration and breaks
[Length, hours, rest. No overnight heroics unless chosen.]

## 8. Ideation
[Before or during the event; problem list seeded from customer evidence.]

## 9. Team formation
[How people find teams; maximum team size.]

## 10. Agenda
| Time | Activity |
|---|---|
| | Kickoff: goal, rules, judging |
| | Build |
| | Mentor check-ins |
| | Evaluation run on the shared eval set |
| | Presentations and judging |

## 11. Mentoring
[Who mentors on product, security, AI, domain.]

## 12. Continuity (agreed before the event)
- Each winning project gets: [named PM owner, follow-on slot, budget]
- Other outcomes we'll keep: [reusable components, connectors, eval cases, people to recruit into the bet]
- Decision review date: [date]

## Judging rules
- Measured results on the shared eval set: [weight]
- Customer value against the bet's question: [weight]
- Safety and security: [pass/fail gate]
- Demo polish: not scored

## Tensions we're managing
[Organizational vs personal goals; concept vs useful output; challenge vs achievable; speed vs quality.]
```

```template id="22-design-partner-program-plan" title="Design partner program plan"
# Design partner program plan · [Product or capability] · [Dates]

**Owner:** [PM]   **Executive sponsor:** [Name]   **Program length:** [one to three quarters]

## Learning goals
1. [What we must learn about workflow]
2. [What we must learn about adoption and approval]
3. [What we must learn about pricing or packaging]

## Selection criteria
- Matches target segment: [criteria]
- Willing to share data: [what, under which agreement]
- Executive sponsor on their side: [required]
- Mix: [include at least one partner unlike the most enthusiastic one]
- Number of partners: [typically five to eight]

## Commitments
| Partner commits to | We commit to |
|---|---|
| Feedback sessions every [n] weeks | Early access to builds |
| Usage and outcome data shared | Named PM contact |
| [Reference or case study if successful] | [Pricing protection for first term] |
| [Security review in parallel] | [Roadmap visibility under NDA] |

## Rules for what ships
- A partner-requested feature ships only if [at least n] partners need it.
- Single-partner requests go to a separate log, reviewed at program end.
- No custom branches or one-off integrations.

## Cadence and evidence
- Weekly: synthesis of feedback, every theme traced to partners
- Monthly: progress against learning goals
- Thresholds that end the program early (positive or negative): [list]

## Exit
- End date: [date]
- Conversion terms to standard commercial contract: [summary]
- What happens to partners who don't convert: [plan]
- Data handling at exit: [return or delete]
```

```template id="22-build-partner-buy-analysis" title="Build, partner or buy analysis"
# Build, partner or buy analysis · [Capability] · [Date]

**Owner:** [PM]   **Reviewers:** [engineering, finance, corporate development, security]

## Capability needed and why
[What the strategy requires, by when, and the cost of not having it.]

## The four questions
| Question | Answer | Evidence |
|---|---|---|
| 1. Are internal resources relevant (knowledge, skills, organizational fit)? | | |
| 2. Is the resource tradable (can a contract define and protect it)? | | |
| 3. Is a bounded collaboration enough (limited joint work, aligned goals)? | | |
| 4. Is deep integration needed, and is it feasible? | | |

## Options compared
| | Build | Partner (contract or alliance) | Buy (company, team or technology) |
|---|---|---|---|
| Time to capability | | | |
| Cost (one-time and ongoing) | | | |
| Control | | | |
| Effect on gross margin | | | |
| Switching cost later | | | |
| Effect on customers | | | |
| Talent risk | | | |
| Regulatory exposure | | | |

## AI-era checks
- Model-provider dependency: [which provider, terms, switching cost, what they can see]
- Exclusivity or limits on other partners: [terms]
- Portability: [abstraction layer, model-agnostic evals]
- Team or technology only? [answer]

## Our default path and the trap
[Which path this company usually takes, and whether this analysis is just repeating it.]

## Recommendation
[Path, scope, and the conditions that would trigger the next path.]
**Review date:** [date]
```

```template id="22-acquisition-opportunity-brief" title="Acquisition opportunity brief"
# Acquisition opportunity brief · [Target] · [Date] · Confidential

**Author:** [PM]   **Corporate development lead:** [Name]   **Distribution:** [named list only]

## The target in one paragraph
[What they build, for whom, stage, team, and why it came up.]

## Strategic fit
- Roadmap bet it answers: [bet]
- Capability gained: [technology, team, customers, data]
- Time saved against building: [estimate with reasoning]

## Leverage or reinvent?
- Value proposition: [same / different]
- Customers and buyers: [same / different]
- Sales motion and pricing: [compatible / different]
- Verdict: Leverages our model (integrate) / Reinvents it (keep separate)

## Options, in order of commitment
| Option | What we get | Cost | Effect on the target's customers | Reversible? |
|---|---|---|---|---|
| Venture client pilot | Evidence of fit | | Served as normal | Yes |
| Minority investment | Option and relationship | | Unchanged | Partly |
| License-and-hire | Team and technology | | Risk of stranding | No |
| Full acquisition | Everything, plus contracts | | Inherited | No |

## Integration risks
[Talent retention, product overlap, technology stack, culture, security posture.]

## Diligence questions
[Technical, eval quality, data rights, security, customer contracts, open-source licenses.]

## Regulatory and approval considerations
[Merger review, data transfer, sector rules. Confirm with legal.]

## Trigger conditions to proceed
[Measured results, by date, that would justify the next level of commitment.]

## Recommendation
[Next step only. Not the whole deal.]
```

```template id="22-venture-client-pilot-charter" title="Venture client pilot charter"
# Venture client pilot charter · [Startup] · [Dates]

**Owner:** [PM]   **Startup contact:** [Name]   **Procurement:** [Name]   **Security:** [Name]

## Problem we're buying a solution to
[One paragraph, in customer terms.]

## Why buy rather than build
[Short answer from the build, partner or buy check.]

## Scope
- Workflow and environment: [where it runs]
- Data shared: [what, under which agreement]
- Duration: [weeks]
- Paid pilot value: [amount]

## Success criteria (set before the pilot)
| Measure | Threshold | Source |
|---|---|---|
| | | |

## Gates
- Security review completed by: [date]
- Purchase order issued by: [date]
- Mid-pilot check: [date]
- Decision: [date]

## Outcomes
- Pass: [contract path, owner, budget line]
- Partial: [what changes and one more cycle]
- Fail: [how we exit and what we keep]
```

## Prompts

```prompt title="Choose an innovation mechanism for a bet"
Goal: Pick the cheapest mechanism that can answer a roadmap question in time, and avoid your organization's habitual path.
Paste in: the bet, its horizon and ambition placement, the date you need an answer, your team's capacity and a list of the mechanisms your company already runs.

Act as a skeptical product leader helping me choose how to pursue this bet for [product].

1. Rewrite the bet as a single question with no solution language.
2. Name the main blocking uncertainty: feasibility, desirability and adoption, availability, capability or business model. Explain your choice.
3. Shortlist three mechanisms from this toolkit: idea challenge, hackathon, innovation training, intrapreneurship program, internal incubator, innovation lab, corporate venture capital, venture client pilot, open innovation program, design partners, university partnership, licensing, acquisition or license-and-hire, spin-out.
4. For each, give cost (low, medium, high), time to an answer, control, effect on customers and reversibility.
5. Run the build, partner or buy questions in order: internal resources relevant, resource tradable, bounded collaboration enough, deep integration needed.
6. Recommend one mechanism. Name the receiving owner role and the follow-on capacity it needs.
7. Tell me which mechanism I'm probably skipping out of habit, and why it might be better.

Don't invent facts about my company. Mark assumptions as assumptions.

[bet and context]

Check the output: confirm the recommendation actually answers the question you wrote in step 1. If it recommends the mechanism your company always uses, ask it to argue the strongest case for the second option.
```

```prompt title="Draft a hackathon plan with continuity built in"
Goal: Produce a hackathon plan that answers a roadmap question and has a landing plan before the event.
Paste in: the bet, the date range, likely participants, available sandbox systems and connectors, and any security constraints.

Draft a hackathon plan for [event] using these twelve decisions: goal, theme, competition or cooperation, stakeholder involvement, participant recruitment, specialized preparation, duration and breaks, ideation, team formation, agenda, mentoring and continuity planning.

Requirements:
- The goal must be measurable and tied to the bet.
- If teams build AI agents, the preparation must include a sandbox with approved data, an eval set and security pre-approval. The judging rule must reward measured results on the eval set over demo polish, and each team must state whether it built a workflow or an agent and justify any added complexity with an eval result.
- Continuity must name, for winning projects, an owner role, follow-on capacity and a review date.
- List the tensions we'll need to manage and how.

[context]

Check the output: if the continuity section could be deleted without changing anything else in the plan, it's too weak. Make sure no participant needs production data or credentials that security hasn't approved.
```

```prompt title="Design a design partner program"
Goal: Set up a design partner program that produces learning without turning into custom work for one customer.
Paste in: the capability, learning goals, target segment and a candidate partner list with what you know about each. Remove personal details and use an approved tool for customer information.

Design a design partner program for [capability].

1. Propose selection criteria and score each candidate partner against them. Flag partners who are enthusiastic but unrepresentative of the segment.
2. Draft commitments in both directions.
3. Propose a rule for which partner requests ship, and a separate log for single-partner requests.
4. Set a cadence, the evidence we'll collect and thresholds that would end the program early.
5. Draft exit and conversion terms.

[context]

Check the output: count how many proposed partners look like your most enthusiastic customer. If it's most of them, change the mix. Have legal review any data-sharing terms before you share them.
```

```prompt title="Run a build, partner or buy analysis"
Goal: Make a resource pathway decision with the evidence written down, including AI-era dependencies.
Paste in: the capability needed, the deadline, your team's relevant skills and assets, candidate partners or vendors, and any acquisition targets under consideration. Keep confidential deal information inside approved tools.

Analyze whether we should build, partner or buy [capability].

1. Answer in order: Are our internal resources relevant? Is the resource tradable by contract? Is a bounded collaboration enough? Is deep integration needed and feasible? Give the evidence for each answer, or say it's missing.
2. Compare build, partner and buy on time, cost, control, gross margin, switching cost, customer effect, talent risk and regulatory exposure.
3. For any AI capability, assess dependency on a model provider: switching cost, what the provider can see, exclusivity, and how to stay portable.
4. Say whether we need the team, the technology or both.
5. Name our likely default path and test whether this analysis is just confirming it.
6. Recommend a path and the conditions that would trigger the next one.

[context]

Check the output: every answer to the four questions should rest on evidence you supplied. Where the model filled a gap with a plausible guess, mark it and find out.
```

```prompt title="Draft an acquisition opportunity brief from public information"
Goal: Get a first draft of a brief for a possible acquisition, using only public information, to structure the conversation with corporate development.
Paste in: the target's name, public material about it (website, documentation, public announcements, reviews) and your roadmap bet. Do not paste confidential deal information into an unapproved tool.

Draft an acquisition opportunity brief for [target] in relation to [our bet].

Sections: the target in one paragraph; strategic fit; whether it leverages or reinvents our business model (value proposition, customers, sales motion, pricing); options in order of commitment (venture client pilot, minority investment, license-and-hire, full acquisition) with the effect of each on the target's own customers; integration risks; diligence questions; regulatory considerations to raise with legal; trigger conditions to proceed.

Rules:
- Cite the public source for every factual claim about the target. If something isn't in the material, write "unknown."
- Don't estimate valuation.

[material]

Check the output: open three cited sources and confirm the claims. Remove any fact without a source. Recommend only the next step, never the whole deal.
```

```prompt title="Audit our innovation programs for theater"
Goal: Find out which innovation mechanisms are changing product decisions and which are theater.
Paste in: a list of the organization's innovation programs from the past year, with outputs (projects, pilots, investments, events) and any record of what happened to them afterward.

Review these innovation programs for [organization].

For each program:
1. List the outputs and trace each one to a roadmap decision, shipped capability, partnership, hire or stop decision. Write "no trace" where none exists.
2. Identify whether a receiving owner and follow-on capacity existed before the program started.
3. Classify the program as landing, partly landing or theater, with the evidence.
4. Recommend: keep, fix (name the fix) or stop.

Then list outputs that are still waiting for an owner and suggest who should own each.

[program list and outcomes]

Check the output: confirm a sample of "landing" claims with the owners named. A program that lands only through one person's heroics is at risk; note it.
```

## Anti-patterns

:::warn Innovation theater
Demo days, press releases and pitch competitions, with no change in what the product does. The mechanism ran, the photos are good and the roadmap is untouched. Count only outputs that changed a decision, and stop funding mechanisms that can't show one in a year.
:::

:::warn The hackathon with no landing
A great prototype wins, everyone applauds and the team goes back to their day jobs on Monday. Six months later someone rebuilds the same thing from scratch. Name the owner, the follow-on slot and the review date before the event, or don't run it.
:::

:::warn The loudest design partner
One enthusiastic customer shapes the product into something only they need. Pick partners for representativeness, and ship a partner request only when several partners need it.
:::

:::warn Pilot purgatory
A venture client pilot succeeds, then sits for two quarters in procurement and security review. Bring procurement and the security reviewer in from the first week, and set the contract path before the pilot starts.
:::

:::warn The habitual path
Every capability gap gets the same answer: engineering-led companies build, acquisitive companies buy. Run the build, partner or buy questions in order every time, and ask which option you'd pick if your usual one were off the table.
:::

:::warn Buying a feature
A company is acquired to fill a Horizon 1 gap a partnership or a quarter of engineering could have closed. Acquisition is the last step in the sequence, and the brief should show why each earlier step fails.
:::

:::warn The accidental model partnership
The team chose a model provider in a prototype and never revisited it. A year later the product depends on one supplier's pricing and terms, with no way to switch. Treat the model provider as a partner decision, with portable abstractions and model-agnostic evals.
:::

## Checklist

- [ ] Every innovation bet is written as a question, placed on the horizon and ambition lenses, and tagged with its main blocking uncertainty.
- [ ] The chosen mechanism is the cheapest one that can answer the question in time, and the selector records why the others were rejected.
- [ ] The build, partner or buy questions were answered in order, with evidence, including model-provider dependency and team versus technology.
- [ ] A receiving owner has signed up, and follow-on capacity is reserved before the mechanism starts.
- [ ] Security, legal and procurement are involved from the start for anything that touches outside parties or production data.
- [ ] Hackathon plans cover all twelve decisions, judge AI prototypes on a shared eval set and plan continuity in advance.
- [ ] Design partner programs have selection criteria, commitments both ways, a multi-partner rule for features and an end date.
- [ ] Venture client pilots have success criteria, gates and a contract path set before they start.
- [ ] Acquisition briefs state whether the target leverages or reinvents the business model, compare options in order of commitment and show the effect on the target's customers.
- [ ] Confidential deal and customer information stays inside approved tools and a named circle.
- [ ] The innovation portfolio is reviewed quarterly, and mechanisms with no changed decisions in a year are fixed or stopped.

## Key takeaways

- The toolkit has fourteen mechanisms in four families: harvesting ideas and skills from inside, protecting new work, bringing the outside in and changing ownership. Each fits a different kind of bet.
- Choose a mechanism by the uncertainty blocking the bet (feasibility, desirability and adoption, availability, capability or business model), then pick the cheapest one that answers the question in time.
- Innovation theater usually comes from poor fit or missing follow-through. Name the receiving owner and reserve follow-on capacity before any mechanism starts.
- Use the build, partner or buy questions in order, and acquire only when deep integration is needed and feasible. Watch for your company's habitual path.
- In 2026, your model provider is a partner decision, MCP connectors make partnering and prototyping cheaper, and "buy" now includes license-and-hire deals that affect customers differently.
- AI makes ideas and prototypes cheap. Judge AI prototypes on measured eval results, and spend the saved time on landing the work.
