<p class="lead">A strategy is a small set of choices about where you will win and what you will refuse to do. A roadmap shows those choices over time, and a backlog is the queue that feeds it. Most product organizations have all three, and in most of them the three don't connect. This chapter shows you how to write a strategy that rules things out, prioritize against it with frameworks you understand well enough to distrust, and publish a roadmap that tells each audience what is committed and what is a bet.</p>

## Why this matters

Ask a room of product managers to show you their strategy and most will show you a roadmap. Ask for the roadmap and you'll get features with quarters next to them. Ask why those features, and the answer is usually some mix of the largest customer's requests, the loudest executive's idea and whatever the team was already building.

That's a plan, and a plan without a strategy has two problems. Nobody can evaluate it, because it never says what the product is up against. And it can't say no: every new request competes with every existing item on equal terms, so the loudest one wins and the roadmap grows until it means nothing.

Enterprise and platform products feel this hardest. More people hold legitimate claims on the roadmap, long sales cycles pull for dated promises, and platform work has indirect value. Without a strategy the enabler always loses to the feature a named customer asked for, and three years later the product can't do anything new without a rewrite.

AI adds a further pressure in 2026. Marty Cagan argued through 2026 on SVPG that cheaper, faster building moves the bottleneck to deciding what to build, and that building faster doesn't fix a team heading the wrong way. Strategy and prioritization are where the direction gets set.

This chapter covers the Strategy dimension of your Product 360 and connects it to Delivery, building on the hypothesis and personas from Chapter 01 and the vision and goals from Chapter 02. It gives you a strategy kernel and choice cascade that force a diagnosis and explicit refusals; strategy hypotheses with proxy metrics; an honest comparison of prioritization frameworks; a backlog policy; and an outcome roadmap that separates commitments from bets, with a view for each audience.

## What strategy is, and what it isn't

### Rumelt's kernel

Richard Rumelt, in *Good Strategy/Bad Strategy* (2011), gives the most useful working definition for a product manager. Good strategy has a **kernel** of three parts:

- **Diagnosis**: names the most important challenge and simplifies a messy situation into the one problem that matters most, including why it exists.
- **Guiding policy**: the overall approach to the obstacles the diagnosis found. It rules options out as much as in.
- **Coherent actions**: coordinated actions, policies and resource commitments that carry out the guiding policy and reinforce one another. A list of independent initiatives doesn't qualify, however good each one is.

Most product strategies skip the diagnosis and start at actions, which is why they read like roadmaps. Without a diagnosis, nobody can tell whether the actions address the real problem, and nobody can argue about them productively.

Rumelt also describes four hallmarks of **bad strategy**, and you'll recognize all of them from planning season:

| Hallmark | What it looks like in a product strategy |
|---|---|
| **Fluff** | "Leverage AI to deliver a best-in-class, customer-centric platform experience." Jargon that sounds like insight and commits to nothing. |
| **Failure to face the challenge** | No diagnosis. The document never says what is hard, so its plan can't be judged against it. |
| **Mistaking goals for strategy** | "Grow ARR 40% and reach 90% gross retention." Results you want, with no way past what stands in the way. |
| **Bad strategic objectives** | A laundry list of twelve initiatives, or objectives as hard as the original problem ("become the platform of choice"). |

Two more of Rumelt's ideas earn their place. A **proximate objective** is a target close enough to reach, which turns a fuzzy challenge into a solvable one. "Become the trusted AI for incident response" is aspiration; "get responders to accept the agent's diagnosis in most incidents across our top 50 accounts by next June" is a proximate objective. A **chain-link system** performs only as well as its weakest link. Enterprise adoption is often one: a superb diagnosis feature is worthless if the security review blocks deployment.

Test any guiding policy this way: can a stranger who reads it predict three requests you'll refuse? If not, it isn't ruling anything out.

:::key Strategy is a choice that costs you something
If your strategy doesn't disappoint some customers, sellers or executives, it hasn't chosen anything. Name what you won't do in the guiding policy, and tell the people who'll be disappointed before they find out from the roadmap.
:::

### Playing to Win: the choice cascade

A. G. Lafley and Roger Martin, in *Playing to Win* (2013), define strategy as an integrated set of choices and lay it out as a **cascade of five questions**:

1. **What is our winning aspiration?** The purpose, framed in terms of winning.
2. **Where will we play?** Customer segments, buyers, geographies, channels, product categories and stages of the value chain.
3. **How will we win?** The value proposition and competitive advantage in those arenas.
4. **What capabilities must be in place?** The activities that make the how-to-win real.
5. **What management systems are required?** The systems, structures and measures that build and sustain those capabilities.

The cascade is iterative: each choice constrains and is constrained by the others, so you move up and down it. It also nests. A product line's cascade sits inside its business unit's, which sits inside the company's. Yours can be narrower than the level above, but it shouldn't contradict it.

Martin's 2014 HBR article "The Big Lie of Strategic Planning" explains why so many strategies turn into plans. Planning lists activities and budgets the company controls, so it feels safe. Strategy bets on things it doesn't control (customers and competitors), so it feels uncomfortable, and teams retreat into planning to avoid choosing.

For B2B and platform PMs, **where to play** is the question most roadmaps quietly dodge. Do you design for the practitioner or the economic buyer when they want different things? Direct enterprise or the partner channel? System of record, or a layer on someone else's data? Each is a real choice with real losers. A roadmap that serves every answer at once serves none of them well.

Rumelt and Martin fit together. Many cascades leave out Rumelt's diagnosis and jump straight to aspiration. Martin's where-to-play and how-to-win make Rumelt's guiding policy concrete. Use the kernel as the spine and the five questions as the checklist.

One more habit belongs here. For each strategic option, ask **what would have to be true** for it to be a great choice, about customers, competitors, your capabilities and the economics, and test the conditions you're least sure of. A strategy is a set of linked hypotheses, and the discovery work in Chapter 01 is how you find out which ones hold.

### Gibson Biddle: DHM and the SMT lockup

Gibson Biddle, who led product at Netflix from 2005 to 2010, offers a product-level toolkit that sits underneath the cascade. In a January 2025 post on his *Ask Gib* newsletter, he connects his models as four questions. What are you building long term (his **GLEe** vision model: get big on something, lead in it, keep expanding)? What are the company's priorities (**GEM**: executives force-rank growth, engagement and monetization, each with a proxy metric)? What are your hypotheses for delivering the product? And how does the work fit together over time (the roadmap)?

The third question is the core. **DHM** asks how the product will **Delight** customers in **Hard-to-copy**, **Margin-enhancing** ways, and Biddle treats these hypotheses as the foundation of product strategy. The **SMT lockup** makes them runnable: each **Strategy** (a hypothesis) is paired with a **Metric** (a proxy metric) and **Tactics** (the projects and experiments that carry it out). If the tactics ship and the metric doesn't move, the hypothesis was wrong, and you know it.

**Proxy metrics** matter because top-line metrics move too slowly to steer by. Biddle's Netflix example is retention: it's the metric that matters, and no single experiment can move it in time to learn from. A good proxy is measurable, moveable by the team and correlated with the top metric. Chapter 02 covers metric trees.

DHM needs translation for B2B:

- **Delight** splits across personas. The on-call engineer wants speed, the VP an ROI story, the security reviewer controls. Delight only the practitioner and you can stall in procurement.
- **Hard to copy** for platforms usually means data that improves with use, integration depth and switching costs, ecosystem position or proprietary evaluation data. Chapter 16 covers moats.
- **Margin-enhancing** is central again for AI products, because inference cost compresses gross margin. A feature that delights and can't be copied but loses money on every use isn't a strategy. Chapter 15 covers pricing.

Biddle also says strategy is top-down and bottom-up, meeting in the middle. Leadership sets the cascade, teams propose SMTs that serve it, and the roadmap reconciles them.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 380" role="img" aria-label="The strategy-to-backlog stack: kernel and cascade at the top, DHM and SMT bets, prioritization filter, roadmap and backlog, with a feedback loop of evidence">
  <rect x="40" y="16" width="460" height="54" rx="10" class="box"/>
  <text x="60" y="40" class="t">Strategy kernel and choice cascade</text>
  <text x="60" y="58" class="s">Diagnosis, where to play, how to win, guiding policy (and what we won't do)</text>
  <rect x="40" y="86" width="460" height="54" rx="10" class="box"/>
  <text x="60" y="110" class="t">Strategy bets (DHM and SMT)</text>
  <text x="60" y="128" class="s">Each strategy paired with a proxy metric and tactics</text>
  <rect x="40" y="156" width="460" height="54" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".6"/>
  <text x="60" y="180" class="t" style="fill:var(--a1)">Strategy filter, then prioritization</text>
  <text x="60" y="198" class="s">Does it serve a coherent action? Only then score it</text>
  <rect x="40" y="226" width="460" height="54" rx="10" class="box"/>
  <text x="60" y="250" class="t">Outcome roadmap: now, next, later</text>
  <text x="60" y="268" class="s">Commitments, bets and explorations, labeled as such</text>
  <rect x="40" y="296" width="460" height="54" rx="10" class="box"/>
  <text x="60" y="320" class="t">Backlog: inbox, opportunities, delivery</text>
  <text x="60" y="338" class="s">Short, ordered, refined only for the next cycles</text>
  <line x1="270" y1="70" x2="270" y2="86" class="ln"/>
  <line x1="270" y1="140" x2="270" y2="156" class="ln"/>
  <line x1="270" y1="210" x2="270" y2="226" class="ln"/>
  <line x1="270" y1="280" x2="270" y2="296" class="ln"/>
  <path d="M500 323 H560 V43 H500" fill="none" stroke="var(--a2)" stroke-width="2"/>
  <text x="570" y="170" class="s" style="fill:var(--a2)">Evidence</text>
  <text x="570" y="186" class="s" style="fill:var(--a2)">flows back</text>
  <text x="570" y="202" class="s" style="fill:var(--a2)">up the stack</text>
  <text x="40" y="372" class="s">Choices flow down. What ships, and what the proxy metrics show, flows back up and revises the strategy.</text>
</svg>
<figcaption>The strategy-to-backlog stack. Prioritization frameworks work at one layer only: they rank items that have already passed the strategy filter, and can't tell you whether the backlog serves the strategy.</figcaption>
</figure>

### The strategy one-pager

Each model covers part of the job. In practice you want one page that combines them: Rumelt's kernel as the spine, Martin's cascade to make the choices explicit, Biddle's DHM and SMT to make the bets testable. This book's **strategy one-pager** (template below) has nine fields: diagnosis, winning aspiration, where we play and don't, how we win (DHM), guiding policy with three refusals, coherent actions as SMTs, capabilities and systems, what would have to be true, and outcome metrics with guardrails.

If it needs more than a page, the choices haven't been made. Review it quarterly, and change it when evidence says a bet was wrong, not when a large customer asks for something it rules out.

:::onramp If you've never written a strategy
Start with the diagnosis alone: one paragraph naming the single hardest problem your product faces, why it exists and the evidence. Show it to your manager and two peers. If they disagree, you've found the real strategy conversation, and it's worth having before anyone touches the roadmap.
:::

## Prioritization frameworks compared

A scoring framework is a **conversation structure and a consistency device**. It makes assumptions explicit and helps a group rank many items the same way. Every framework fails in the same two ways:

1. **The inputs are opinions dressed as numbers.** Multiplying three guesses gives you a precise-looking guess.
2. **The score ranks only the items in front of it.** A perfectly scored list of the wrong things is still the wrong list.

So the order is fixed: **strategy filters first, scoring ranks second.** An item that serves none of your coherent actions shouldn't be scored at all.

### RICE

Sean McBride, at Intercom, described **RICE** as an estimate of total impact per time worked:

> RICE score = (Reach × Impact × Confidence) ÷ Effort

**Reach** is people or events per period (customers per quarter, say), from real product data where possible. **Impact** per person uses a fixed scale: massive 3, high 2, medium 1, low 0.5, minimal 0.25. **Confidence** is high 100%, medium 80% or low 50%; McBride treats anything lower as a moonshot. **Effort** is person-months across product, design and engineering. McBride's own caveat: the score isn't a hard rule, and a lower scorer may go first as a dependency or as table stakes for certain customers, as long as the trade-off is visible.

RICE fits many comparable, medium-sized items with usage data behind them. In B2B it has a structural bias: **reach counts users, and enterprise value isn't spread evenly across users.** One regulated customer's audit requirement can unblock a large renewal while scoring low on reach, and platform enablers score low because their reach is indirect. Define reach in accounts or ARR touched, and say so at the top of the scorecard.

### ICE and the Confidence Meter

**ICE** (Impact × Confidence × Ease, each on a relative 1 to 10 scale) was invented by Sean Ellis to prioritize growth experiments. It's fast and good for triaging small tests, but all three numbers are opinions and confidence is usually self-assessed.

Itamar Gilad's **Confidence Meter** fixes that input by grading confidence on the type of evidence. Self-conviction, thematic fit and other people's opinions earn almost nothing; anecdotes and market data a little; customer evidence from interviews and studies more; usage data from an MVP or launch the most. Gilad's point, paraphrased: a bet backed only by opinion is little better than roulette. Use the meter with any framework.

### MoSCoW

**MoSCoW**, from the DSDM agile framework maintained by the Agile Business Consortium, sorts scope within a timebox. **Must have** is the minimum usable subset: without it the release is pointless, unsafe or illegal. **Should have** is important, with a workaround. **Could have** is desirable and first to drop. **Won't have this time** is agreed out of scope for this timebox. DSDM's guidance: Must Haves take no more than about 60% of estimated effort, with a pool of Could Haves at about 20% as contingency. Above 60%, the release is at risk.

MoSCoW fits fixed-date, fixed-scope work: a contracted enterprise release, a compliance deadline, a launch at your annual event. It fails when everything becomes a Must, and it says nothing about value or order within a bucket. Its most useful part for B2B teams is the **Won't** list: publishing what's out of scope before the field promises it prevents more escalations than any scoring model.

### Kano

The **Kano model** comes from Noriaki Kano and colleagues' 1984 paper "Attractive Quality and Must-be Quality." **Must-be** features are expected: absence hurts, presence earns nothing. **Performance** features satisfy roughly in proportion to how much you deliver. **Attractive** features delight when present and cost nothing when absent. **Indifferent** features don't matter, and **Reverse** and **Questionable** results usually flag survey problems. You ask a pair of questions per feature (how would you feel if you had it, and if you didn't?), each answered with one of five options (like it, expect it, neutral, can tolerate it, dislike it), and the pair of answers classifies the feature.

Categories decay: today's delighter becomes tomorrow's must-be. In this book's view, AI-generated summaries in enterprise tools have already made that trip. Kano fits decisions about a release's mix of table stakes and differentiators. Respondents can't rate features they've never seen (a real limit for novel AI capabilities), and personas disagree: an engineer may rate autonomous remediation attractive while the security reviewer rates its controls must-be. Run Kano per persona.

### WSJF and cost of delay

Don Reinertsen, in *The Principles of Product Development Flow* (2009), argues that most teams don't know their most important number: the **cost of delay**, what it costs in economic terms to deliver something later. His sequencing rule, often called **CD3** (cost of delay divided by duration), puts the highest cost of delay per unit of time first, so the most value arrives soonest. As Scaled Agile quotes him: "If you only quantify one thing, quantify the Cost of Delay."

The Scaled Agile Framework (SAFe) turned this into **WSJF** (weighted shortest job first): relative cost of delay divided by relative job duration, where cost of delay combines user and business value, time criticality, and risk reduction or opportunity enablement. WSJF ignores sunk costs, and priorities update as inputs change. **Opportunity enablement** credits the connector framework or data layer that unlocks later features, which RICE can't see; **time criticality** credits renewal-linked features, regulatory deadlines and competitive windows.

Practitioners debate whether SAFe's relative points lose Reinertsen's economics. In B2B the money version is often within reach: ARR at risk at a known renewal date gives you a defensible cost of delay per month. WSJF fails through gamed relative scores and unreliable duration estimates for discovery-heavy work, which includes most AI features.

### Opportunity scoring and value versus effort

Anthony Ulwick's **opportunity scoring**, covered in Chapter 01, ranks customer outcomes rather than features: importance plus any positive gap between importance and satisfaction. It works at strategy level, showing which needs are underserved before you've chosen solutions. It costs a careful survey and can miss needs customers can't yet articulate. In B2B, survey each buying-group role separately.

The **value versus effort** 2×2 has no single originator and many quadrant names (quick wins, big bets, fill-ins, money pits). It's a good first cut in a workshop and an easy picture for executives, but both axes are guesses, risk and timing vanish, and optimistic estimates drift everything toward quick wins. Adding a confidence column makes it much more honest.

### Choosing a framework

| Framework | Unit of decision | Best fit | Main failure mode | B2B adaptation |
|---|---|---|---|---|
| RICE | Features, projects | Many comparable items, usage data exists | Reach undervalues high-ARR, low-count accounts and enablers | Define reach in accounts or ARR touched |
| ICE | Experiments | Growth tests, fast triage | Three opinions multiplied | Grade confidence with the Confidence Meter |
| MoSCoW | Scope within a timebox | Fixed-date commitments | Everything becomes a Must | Cap Musts near 60% of effort; publish the Won'ts |
| Kano | Feature types | Release mix, table stakes vs differentiators | Personas disagree; novel features can't be rated | Run it per persona |
| WSJF / CD3 | Large items in a queue | Time-sensitive and enabler work | Relative points lose the economics | Price a month of delay in ARR at risk |
| Opportunity scoring | Customer outcomes | Strategy and discovery focus | Survey cost; ranks needs, not solutions | Survey each buying-group role |
| Value vs effort | Anything | First-pass workshop | Guesses on both axes | Add a confidence column |

**The framework you choose changes the answer.** RICE favors broad, measurable features; WSJF favors deadlines and enablers; Kano favors table stakes. Choosing the framework is itself a strategic choice, so let the guiding policy decide which lens matters and write it at the top of the scorecard. The Beacon case below ranks the same five items two ways.

:::leader For product leaders
Standardize the scorecard's columns across teams, not the formula. If every team records strategy link, accounts and ARR affected, cost of delay, evidence level and effort, you can compare across the portfolio and still let each team weight them for its context. Require a written reason whenever a decision departs from the score.
:::

## Building and keeping a healthy backlog

*The Scrum Guide* (2020) defines the Product Backlog as an emergent, ordered list of what's needed to improve the product, committed to a **Product Goal** the team plans against. **Ordered** means one sequence, not a pile with priority labels; **emergent** means it changes as you learn. The Product Owner can delegate backlog work but not the accountability.

Roman Pichler's **DEEP** criteria describe a healthy backlog: **Detailed appropriately** (more detail near the top), **Estimated**, **Emergent** and **Prioritized**. Pichler is blunt about size: a backlog of several hundred items is itself the problem, and if yours has grown that long, discard it and derive a fresh one from the roadmap.

Ryan Singer goes further in Basecamp's *Shape Up*, in a chapter titled "Bets, Not Backlogs." Before each six-week cycle a betting table chooses which pitches to fund, and unchosen pitches aren't kept centrally; anyone who still believes in one can bring it back. A long backlog, Singer argues, makes a team feel permanently behind, and most of its items will never be built.

Teresa Torres's **opportunity solution tree** links the backlog to strategy. The desired outcome sits at the root, customer opportunities branch from it, and solutions and assumption tests sit below. In her framing, a solution placed in the delivery backlog is a bet, and discovery reduces its risk.

### Three stores, not one list

For an enterprise or platform team, stop treating every request as a backlog item. This book recommends three stores:

1. **Request inbox.** Every raw ask from customers, sales, partners and support, linked to the account and its ARR. Never ordered and never promised, but searchable, so a seller can see that a request was logged and where it went.
2. **Opportunity backlog.** Requests clustered into customer problems, sized by accounts and ARR, and linked to the strategy's coherent actions. Strategy filtering happens here.
3. **Delivery backlog.** Ordered, refined, sized and short: only enough for the next one or two cycles of the Now column.

An item enters the delivery backlog with a linked opportunity and outcome, an evidence level, an owner, a rough size and acceptance criteria; AI features also need an eval or quality bar (Chapter 31). Items untouched for two quarters are archived with a reason, and every request gets a status a seller can quote, such as "logged, mapped to the multi-tenant theme, not planned this half."

The policy also declares a **capacity split** across new value, platform and enablers, quality and debt, and customer commitments. Chapter 06 treats technical debt as a product decision; the split is where that decision becomes visible. If the split isn't written down, the urgent crowds out the important.

## Roadmaps that tell the truth

### Why feature-and-date roadmaps fail

Marty Cagan's case against the classic roadmap rests on two inconvenient truths he set out on SVPG in 2013: at least half of product ideas won't work, and the ones that do usually take several iterations to deliver the expected business value. A roadmap of features with dates assumes both away. It promises untested ideas on dates set before anyone knows how many iterations they'll need.

In "The Alternative to Roadmaps" (2015), Cagan proposed three replacements: a product vision and strategy, business objectives for each team, and **high-integrity commitments** only where a real date is needed. Try his uncomfortable exercise: count how many items on last year's roadmap met their business objectives.

In October 2026 he sharpened the point. The real tension, he wrote, is **outcomes versus predictability**, not outcomes versus output. Most companies implicitly prioritize predictability, and roadmaps of untested ideas with dates reinforce that bias. He quoted Henrik Kniberg: "100% predictability = 0% innovation." When predictability is genuinely required, handle it with commitment techniques rather than a whole roadmap of promises.

This book's position follows. Every roadmap item is one of three types, and says which:

- **Commitments** carry a date because a customer, regulator, partner or launch depends on it. Make one only after enough discovery that the team knows the solution is valuable, usable and feasible, and engineers have estimated it. Then keep the date. Deprecations, contracted features and regulatory deadlines are commitments by nature.
- **Bets** are framed as outcomes, sized by how much you're willing to spend and open to being killed on evidence. Nobody outside the team sees a date.
- **Explorations** are discovery only, with no delivery promise.

The mix is a health check. A roadmap that is mostly commitments leaves no room to learn; one with no commitments won't survive enterprise sales.

### Now, next, later

Janna Bastow, writing on the ProdPad blog in 2022, describes how she created the **now-next-later** roadmap, first sketched in 2012 as current, near term and future, out of frustration with release planners and timelines that forced false precision about dates. **Now** is work under way, well defined and broken into small pieces. **Next** follows, with less detail, and may change depending on what Now teaches. **Later** holds bigger, hazier problems whose solutions aren't defined yet.

Bastow's rules make the format work. Items are problems first, with ideas and experiments attached and tied to objectives. Columns reflect confidence, not calendar time, and needn't be the same size. You commit only to near-term work, though a time-sensitive item can carry a deadline, and accountability lives in objectives rather than dates.

Enterprise products need one adaptation. Sales and customers legitimately need dates for contracted features, compliance deadlines and deprecations. Keep the structure, mark that small set of commitments explicitly, and leave everything else undated.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 300" role="img" aria-label="Now, next, later roadmap with commitments, bets and explorations, and confidence falling from left to right">
  <rect x="20" y="20" width="190" height="230" rx="10" class="box"/>
  <rect x="225" y="20" width="190" height="230" rx="10" class="box"/>
  <rect x="430" y="20" width="190" height="230" rx="10" class="box"/>
  <text x="40" y="46" class="t">Now</text><text x="40" y="64" class="s">In delivery, well defined</text>
  <text x="245" y="46" class="t">Next</text><text x="245" y="64" class="s">Discovery under way</text>
  <text x="450" y="46" class="t">Later</text><text x="450" y="64" class="s">Problems, not solutions</text>
  <rect x="34" y="80" width="162" height="44" rx="8" fill="var(--a1)" fill-opacity=".14" stroke="var(--a1)"/>
  <text x="44" y="100" class="s" style="fill:var(--a1)">Commitment</text><text x="44" y="116" class="s">Dated: customer depends on it</text>
  <rect x="34" y="134" width="162" height="44" rx="8" fill="var(--a1)" fill-opacity=".14" stroke="var(--a1)"/>
  <text x="44" y="154" class="s" style="fill:var(--a1)">Commitment</text><text x="44" y="170" class="s">Dated: deprecation milestone</text>
  <rect x="34" y="188" width="162" height="44" rx="8" fill="var(--a2)" fill-opacity=".14" stroke="var(--a2)"/>
  <text x="44" y="208" class="s" style="fill:var(--a2)">Bet</text><text x="44" y="224" class="s">Outcome and target metric</text>
  <rect x="239" y="80" width="162" height="44" rx="8" fill="var(--a2)" fill-opacity=".14" stroke="var(--a2)"/>
  <text x="249" y="100" class="s" style="fill:var(--a2)">Bet</text><text x="249" y="116" class="s">No external date</text>
  <rect x="239" y="134" width="162" height="44" rx="8" fill="var(--a2)" fill-opacity=".14" stroke="var(--a2)"/>
  <text x="249" y="154" class="s" style="fill:var(--a2)">Bet</text><text x="249" y="170" class="s">Killed if evidence says so</text>
  <rect x="444" y="80" width="162" height="44" rx="8" fill="var(--a3)" fill-opacity=".14" stroke="var(--a3)"/>
  <text x="454" y="100" class="s" style="fill:var(--a3)">Exploration</text><text x="454" y="116" class="s">Discovery only</text>
  <rect x="444" y="134" width="162" height="44" rx="8" fill="var(--a3)" fill-opacity=".14" stroke="var(--a3)"/>
  <text x="454" y="154" class="s" style="fill:var(--a3)">Exploration</text><text x="454" y="170" class="s">Capability watchlist item</text>
  <line x1="20" y1="275" x2="620" y2="275" class="ln"/>
  <text x="20" y="292" class="s">Confidence and detail: high</text>
  <text x="620" y="292" text-anchor="end" class="s">low</text>
</svg>
<figcaption>A now-next-later roadmap for an enterprise product. Columns show confidence, not calendar quarters. Only commitments carry dates, and they cluster in Now; Later holds problems and explorations.</figcaption>
</figure>

### Theme-based roadmaps

C. Todd Lombardo, Bruce McCarthy, Evan Ryan and Michael Connors wrote *Product Roadmaps Relaunched* (2017) about setting direction while embracing uncertainty. They build the roadmap around **themes** (customer needs or problems to solve) tied to the product vision and business objectives, use broad time horizons instead of release dates and say plainly that the roadmap will change. Features, stage of development and confidence are detail you add where an audience needs it. They also treat a roadmap as something you build agreement around through many one-to-one conversations before the big review.

Themes are the bridge from strategy. Each coherent action in the kernel should map to one or more themes, and each theme should name the outcome metric it moves. If a theme traces to no coherent action, ask why it's on the roadmap.

### One roadmap, several views

Build the roadmap once, then generate a view per audience:

- **Executives**: outcomes, bets, the capacity split, risks and decisions needed, on one page (Chapter 35).
- **Sales and the field**: dated commitments, undated themes, the Won't list, how to log a request and your company's forward-looking disclaimer; get legal guidance on roadmap disclosure before you publish (Chapter 27).
- **Customers**: the problems you're solving and your direction, commitments only where contractual, and design-partner invitations instead of feature promises.
- **Partners and developers**: API changes and deprecation timelines, with longer notice than direct customers get, because partners have their own customers to tell.

Every view carries a **changelog** of what moved and why. A roadmap that changes silently loses trust faster than one that changes often and says so.

:::key Never put a bet in a sales deck with a date on it
Once a date reaches a customer, it's a commitment whether you meant it or not. If a seller needs a date to close a deal, treat it as a request to convert a bet into a commitment, and put it through the same discovery and estimation gate as any other.
:::

## How to apply it

This method builds the Strategy dimension of a Product 360 and connects it to the roadmap. It takes about six weeks the first time and a few days each quarter after that.

**Weeks 1 and 2: Diagnose and choose.**

1. Gather the evidence: the hypothesis and personas (Chapter 01), the vision and North Star (Chapter 02), win/loss notes, churn reasons, competitive moves, unit economics and two quarters of customer requests.
2. Draft the diagnosis in one paragraph and test it with your manager, the engineering lead and a sales leader. Rewrite until they agree it's the real problem, even if they don't like it.
3. Work through the cascade. For each where-to-play choice, write what would have to be true and mark the conditions you're least sure of.
4. Write the guiding policy with three explicit refusals, and check it against Rumelt's four hallmarks.

**Week 3: Make the bets testable.**

5. Write the DHM, then turn the coherent actions into three to five SMTs, each with a proxy metric the team can move within a quarter.
6. Set one proximate objective, assemble the strategy one-pager and get it signed off by your manager and reviewed by peer PMs whose products it touches.

**Week 4: Prioritize.**

7. Rebuild the backlog into three stores. Cluster the request inbox into opportunities and drop those that serve no coherent action.
8. Choose your scoring lens and say why, then score the surviving opportunities with an evidence level beside every score. Write the decision column yourself (commit, bet, explore or no), with a reason for any departure from score order.

**Week 5: Build the roadmap.**

9. Place items in now, next and later, labeled commitment, bet or exploration. Date only commitments that have passed discovery and been estimated by engineering.
10. Write the backlog policy: stores, entry criteria, ageing rule, capacity split and cadence.

**Week 6: Communicate.**

11. Generate the audience views from the single roadmap, and hold the one-to-one conversations before the group review. Brief sales leadership on the Won't list before it reaches the field.
12. Publish with a changelog and set the cadence: weekly refinement, monthly opportunity review, quarterly strategy and roadmap review (Chapter 29).

## The AI lens

### Roadmapping AI products when capabilities shift every quarter

AI-powered products face a problem conventional products don't: the ground under the roadmap moves faster than the roadmap.

**Capability moves fast.** METR, a research group that evaluates frontier models, reported in March 2025 that the length of tasks frontier agents could complete with 50% reliability had doubled roughly every seven months over about six years, while noting wide uncertainty in that estimate. Releases come often: Anthropic, for example, announced Claude Opus 5.5 on 22 September 2026, Sonnet 5.5 six days later and Haiku 5.5 on 7 October. A Later item can become feasible within a quarter, and a Now item built around a model's limitation can be obsolete before it ships.

**Models retire on someone else's schedule.** Anthropic commits to at least 60 days' notice before retiring a publicly released model; its published table shows Claude Sonnet 4.5 deprecated on 30 September 2026 and retiring on 30 November 2026. An externally dated retirement makes model migration a commitment-class item whether you planned for it or not.

**Regulatory dates move too.** The EU AI Act entered into force on 1 August 2024 and became generally applicable on 2 August 2026. The AI Omnibus, in force from 27 July 2026, moved obligations for Annex III high-risk systems from 2 August 2026 to 2 December 2027, six days before the original date arrived. Treat regulatory deadlines as commitments whose date can change: track the source and replan when it moves (Chapter 33).

The practical rules:

- **Frame items as outcomes that don't depend on a particular model.** "A diagnosis an on-call engineer trusts in under five minutes" survives a model change; "a fine-tuned root-cause model" may not.
- **Keep a capability watchlist.** For each capability-dependent Later item, record the threshold that would move it to Next, measured on your own evals, and re-run them on each new model (Chapter 31).
- **Budget a fixed lane for evals and model migration** in the capacity split. It's recurring work with external dates.
- **Treat unit economics as a roadmap constraint.** This is Biddle's M. Inference cost changes with model choice, so a roadmap can grow usage while shrinking margin.
- **Refresh "what would have to be true" each quarter** for every AI bet.
- **Never give customers a date for a capability that depends on a model improvement that hasn't shipped.** That stays a bet.

Prioritization shifts as well. When AI makes building cheaper, effort estimates shrink and stop telling items apart, so weight evidence more and effort less. Cagan noted in October 2026 that A/B tests get slower and costlier for AI features, so evals come earlier and live tests are reserved for proving value. That changes how fast a bet can earn a higher Confidence Meter grade.

### Doing strategy and roadmap work with AI

An AI harness with connectors to your CRM, support desk, issue tracker and call notes changes the mechanics of this work, not who decides. It's good at clustering hundreds of requests into opportunities with accounts and ARR attached, flagging duplicates and stale items, drafting a diagnosis from win/loss notes with citations, red-teaming a strategy against Rumelt's hallmarks, scoring the same items under two frameworks, and generating audience views and changelogs from one source.

It can't make the choice the strategy exists to make, and it leans toward the balanced, inclusive answer that good strategy avoids. Ask a model for a strategy and you'll get a fluent one that rules nothing out, which is fluff in Rumelt's terms. Keep every proposed theme linked to the requests and accounts behind it, and send customer and CRM data only to tools your company has approved.

:::ai The one-line rule
Use AI to gather the evidence and attack the draft. Make the choices, and say no, yourself.
:::

## The Beacon case: choosing what Beacon won't do

:::example Where Beacon starts
Discovery (Chapter 01) confirmed that diagnosis is most of every incident, that responders want the diagnosis and are wary of the agent acting, and that security reviewers will block write access without audit logs, scoped credentials and a kill switch. Two customers left for a competitor's AIOps feature bundled into a platform they already paid for. Beacon has about $48M in ARR, growing 38%, with NRR at 118%; gross margin has fallen from 81% to 72% since agentic features launched. A draft 2027 strategy, written before you took the role, is waiting for you.
:::

**The bad draft.** It opens "Become the #1 AI agent platform for IT operations with best-in-class AI" and lists twelve initiatives. Against Rumelt's hallmarks it shows fluff (best-in-class), a goal posing as strategy (#1) and a laundry list, and it has no diagnosis. Margin and the bundling threat don't appear.

**The kernel.** You rewrite it.

- *Diagnosis:* Beacon's lead in alert correlation is eroding as large observability platforms bundle AIOps. Customers trust Beacon to summarize but not yet to act, and agentic features cut gross margin from 81% to 72%. The critical challenge is converting diagnosis trust into supervised action without breaking margin.
- *Guiding policy:* win on trusted diagnosis and supervised remediation across the customer's existing tools, through connectors and MCP, with Northlight Observe data as an accelerant rather than a requirement. That settles the old tension between building on Observe and staying tool-agnostic. Three refusals: no Beacon metrics store, no fully autonomous actions outside customer allowlists, and no edition for small teams on a single-vendor stack.
- *Coherent actions:* raise diagnosis acceptance with cited evidence and evals; launch Beacon Agents at Northlight Live with the approval gates and audit logs Sam needs; move toward per-resolved-incident pricing so price tracks value and funds inference; cut inference cost per incident through model routing; sunset Beacon Classic to free a team. Trust enables action, action justifies outcome pricing, pricing and routing restore margin, and the sunset funds the work.
- *Proximate objective:* diagnosis acceptance rate above 60% across the top 50 accounts by the end of Q2 2027.

**Where to play and DHM.** Enterprise SRE and platform teams running observability from several vendors, plus MSPs like Leo's for the mid-market; not small teams on one vendor's stack, where the bundled feature is good enough. Delight: Dana gets "what broke and what to do" in under five minutes. Hard to copy: resolved incidents feeding retrieval and evals through the Learn loop, connector breadth, and approval and audit design that security teams have already signed off. Margin: per-resolved-incident pricing plus model routing.

**Two frameworks, two answers.** You score five candidates: (a) an EU AI Act documentation pack, (b) multi-tenant billing for MSPs, (c) autonomous rollback for allowlisted actions, (d) Beacon Classic migration tooling and (e) a connector for a widely used ticketing system. RICE, with reach in accounts, puts MSP billing and the ticketing connector on top because they touch the most accounts. WSJF puts the AI Act pack and the migration tooling on top: the first is time-critical and unblocks stalled EU deals, and the second enables the sunset that frees a team. The guiding policy breaks the tie. Supervised action depends on gatekeeper trust, so time criticality and enablement matter most this half. You choose WSJF and write that choice at the top of the scorecard.

Then the AI Omnibus moves the Annex III dates to December 2027. You re-score the AI Act pack: its cost of delay drops but not to zero, because EU customers are still asking and Sam's needs haven't changed. It moves from Now to Next, and the changelog says why.

**The roadmap.** Now: Beacon Agents supervised remediation, generally available at Northlight Live (commitment); Beacon Classic sunset with dated migration milestones (commitment); diagnosis citation quality (bet). Next: a per-resolved-incident pricing pilot, MSP multi-tenant views and the AI Act documentation pack (all bets). Later: broader autonomous resolution for low-risk incident classes, gated by eval thresholds on future models (exploration, on the capability watchlist). The capacity split across the five teams is 50% new value, 20% platform and connectors, 15% quality, evals and model migration, and 15% commitments and the Classic migration.

**The communication pack.** Marcus gets outcomes and the ROI story. Sales gets the two dated commitments (Agents GA and the Classic end-of-life date), undated themes for everything else and the Won't list. Priya's team is invited to be a design partner for the citation work. Leo gets API and deprecation notice periods, longer than direct customers get. Sam gets the AI Act documentation timeline, with the Omnibus change explained.

**The reprioritization.** Mid-quarter, a hallucinated root cause leads a customer to roll back the wrong service. Trust work jumps the queue: the citation-quality bet gets two more engineers and a stricter eval bar, and MSP multi-tenant views slip a cycle. The changelog names the incident, what moved and why. Sales only ever had multi-tenant views as an undated theme, so nobody has to retract a promise.

## Product 360 artifacts

```template id="03-strategy-kernel" title="Strategy kernel"
# Strategy kernel · [Product] · v[n] · [Date]

**Owner:** [PM]   **Approver:** [Name]   **Review date:** [Date]

## Diagnosis
The critical challenge is [challenge] because [cause].
Evidence: [win/loss, churn, usage, competitive or economic data, with sources]

## Guiding policy
We will [overall approach].
Therefore we will not:
1. [Refusal]
2. [Refusal]
3. [Refusal]

## Coherent actions (3 to 5)
| # | Action | Owner | Resource commitment | How it reinforces the others |
|---|---|---|---|---|
| 1 | | | | |

## Proximate objective
By [date] we will have [measurable, achievable result].

## Bad-strategy check
- [ ] No fluff: every sentence commits to something.
- [ ] The challenge is named and faced.
- [ ] Goals are not standing in for strategy.
- [ ] Not a laundry list; actions are coherent.
- [ ] A stranger could predict three requests we'll refuse.
```

```template id="03-strategy-one-pager" title="Strategy one-pager"
# Product strategy · [Product] · Horizon: [12 to 24 months]

**Owner:** [PM]   **Last reviewed:** [Date]   **Nests inside:** [business unit or portfolio strategy]

1. **Diagnosis:** the one critical challenge, with evidence.
2. **Winning aspiration:** what winning looks like for customers and for us.
3. **Where we play / where we don't:** segments, buyers, channels, ecosystem position.
4. **How we win (DHM):**
   - Delight (per persona): [end user] / [champion] / [economic buyer] / [gatekeeper]
   - Hard to copy:
   - Margin-enhancing:
5. **Guiding policy:** the approach, plus the three things we'll say no to.
6. **Coherent actions as SMTs:**

| Strategy (hypothesis) | Proxy metric (current → target) | Tactics (projects, experiments) | D / H / M |
|---|---|---|---|
| | | | |

7. **Capabilities and systems we must build:**
8. **What would have to be true:**

| Condition | Confidence (H/M/L) | Test | Owner | Due |
|---|---|---|---|---|
| | | | | |

9. **Outcome metrics:** North Star [metric]; inputs [2 to 3]; guardrails [margin, trust, quality].

**Changes since last review:** [what changed and the evidence that changed it]
```

```template id="03-prioritization-scorecard" title="Prioritization scorecard"
# Prioritization scorecard · [Product] · [Period]

**Lens chosen:** [WSJF / RICE with reach in accounts / MoSCoW / Kano / other]
**Why this lens:** [how the guiding policy makes this lens the right one]
**Reach unit:** [accounts / ARR touched / users]

## Strategy filter (before scoring)
Only items linked to a coherent action are scored. Items removed at the filter:
| Item | Reason removed | Status told to requester |
|---|---|---|
| | | |

## Scored items
| Item (opportunity or bet) | Strategy link | Accounts / ARR affected | Customer value (1 to 3) | Cost of delay per month | Risk reduction / enablement | Effort (team-weeks) | Evidence level | Score | Decision (commit / bet / explore / no) |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

Evidence levels (Confidence Meter): opinion · anecdote or market data · customer evidence · MVP or launch data.

## Departures from score order
| Item | Moved from → to | Reason | Decided by |
|---|---|---|---|
| | | | |
```

```template id="03-now-next-later-roadmap" title="Now, next, later roadmap"
# Roadmap · [Product] · v[n] · [Date]

**Strategy:** [link to one-pager]   **Owner:** [PM]   **Next review:** [Date]

| | Now (in delivery) | Next (discovery under way) | Later (problems to solve) |
|---|---|---|---|
| Theme / outcome | | | |
| Target metric | | | |
| Type | Commitment / Bet / Exploration | | |
| Confidence (H/M/L) | | | |
| Date (commitments only) | | Not dated | Not dated |

## Commitments register
| Commitment | Who depends on it | Date | Discovery done? | Engineering estimate | Owner |
|---|---|---|---|---|---|
| | | | | | |

## Capability watchlist (AI products)
| Later item | Capability threshold to move to Next | Eval used | Last model tested | Result |
|---|---|---|---|---|
| | | | | |

## Capacity split
New value [x]% · Platform and enablers [x]% · Quality, evals and model migration [x]% · Commitments [x]%

## Changelog
| Date | What moved | From → to | Why |
|---|---|---|---|
| | | | |
```

```template id="03-roadmap-communication-pack" title="Roadmap communication pack"
# Roadmap communication pack · [Product] · [Date]

**Source roadmap:** [link]   **Disclaimer approved by:** [legal contact, date]

## 1. Executive view (one page)
- Outcomes we're driving and current metric values:
- Strategic bets and what would make us stop:
- Investment mix (capacity split):
- Top risks:
- Decisions needed from you:

## 2. Field view (sales, solutions, customer success)
- Talk track (three sentences):
- Commitments you can quote, with dates:
- Themes for Next and Later (no dates):
- Won't list (do not promise):
- How to log a customer request, and what status they'll get back:
- Forward-looking disclaimer:

## 3. Customer view
- Problems we're solving for you and our direction:
- Commitments (contractual only):
- Design-partner invitations:
- NDA required: yes / no

## 4. Partner and developer view
- API changes and versions:
- Deprecations, with notice periods:
- Platform contracts and dependencies:

## 5. Changelog since last version
| What moved | Why | Who was told |
|---|---|---|
| | | |
```

```template id="03-backlog-policy" title="Backlog policy"
# Backlog policy · [Product or team] · [Date]

**Accountable:** [PM]   **Reviewed:** quarterly

## Three stores
1. **Request inbox:** every raw ask, linked to account and ARR. Never ordered, never promised. Searchable by the field.
2. **Opportunity backlog:** requests clustered into customer problems, sized by accounts and ARR, linked to a coherent action.
3. **Delivery backlog:** ordered and refined; covers the next [one to two] cycles of Now only. Maximum size: [n] items.

## Entry criteria for the delivery backlog
- [ ] Linked opportunity and outcome
- [ ] Evidence level stated
- [ ] Owner named
- [ ] Rough size
- [ ] Acceptance criteria
- [ ] AI features: eval or quality bar defined

## Ageing rule
Items untouched for [two quarters] are archived with a reason. The requester's status updates automatically.

## Capacity split
| Category | Share | Notes |
|---|---|---|
| New value | | |
| Platform and enablers | | |
| Quality, debt, evals and model migration | | |
| Customer commitments | | |

## Cadence
- Weekly: refine the top of the delivery backlog.
- Monthly: opportunity review; cluster new requests.
- Quarterly: strategy and roadmap check; reset capacity split.
- Any reorder of a commitment is communicated within [n] business days.

## Request statuses a seller can quote
Logged · Mapped to theme [x] · In discovery · Planned (Now) · Not planned this half · Won't do (with reason)
```

## Prompts

```prompt title="Red-team a draft strategy"
Goal: Find out whether your strategy is a strategy or a plan, before your leadership review does.
Paste in: your draft strategy or one-pager, and the evidence behind the diagnosis.

Act as a demanding strategy reviewer for [product]. Evaluate this draft against Richard Rumelt's kernel and his four hallmarks of bad strategy.

1. Extract the diagnosis, guiding policy and coherent actions as written. If any is missing, say so plainly.
2. For each hallmark (fluff, failure to face the challenge, goals mistaken for strategy, bad strategic objectives), quote the sentences that show it and explain why.
3. Check whether the coherent actions reinforce one another. Name any action that is independent of the rest.
4. List three customer or internal requests this strategy would clearly refuse. If you can't find three, say the guiding policy rules nothing out.
5. Check the where-to-play choices: which segment, buyer, channel or ecosystem position is the draft avoiding a choice on?

Don't rewrite the strategy. Don't soften the critique. Don't add evidence I haven't provided.

[draft strategy]
[evidence]

Check the output: confirm each quoted sentence actually appears in your draft. Treat the refusal test as the most important result; if the model invented refusals the text doesn't support, your policy is too vague.
```

```prompt title="Draft a diagnosis from customer evidence"
Goal: Get a first, evidence-cited draft of the diagnosis to argue about.
Paste in (or connect the harness to): win/loss notes, churn reasons, competitive notes and a summary of unit economics for the last two to four quarters. Use only tools approved for customer and financial data.

From this material for [product], identify the three candidate challenges that most limit our growth or retention. For each:
- State it in one sentence, then explain the cause.
- Cite the specific sources that support it (document and passage).
- Note the evidence against it.
- Say whether it's a customer problem, a buying-process or gatekeeper problem, a competitive problem or an economic problem.

Then recommend which one is the critical challenge and why, in one paragraph. Label it "draft diagnosis for discussion."

Check the output: open three of the cited sources and confirm they say what the draft claims. Then ask whether the recommended challenge is the one your team avoids talking about; if it isn't, check whether it's the real one.
```

```prompt title="Cluster the request inbox into opportunities"
Goal: Turn months of raw requests into a short list of customer problems with commercial weight attached.
Paste in (or connect the harness to): feature requests from the CRM, support desk and sales notes for the last [90] days, with account names, ARR and renewal dates. Use an approved tool for customer data.

Group these requests for [product] into customer problem themes. Name each theme from the customer's point of view, without proposing a solution. For each theme give:
- number of accounts and total ARR affected;
- ARR renewing in the next two quarters;
- which personas raised it (end user, champion, economic buyer, security or compliance, partner);
- three short verbatim excerpts with sources;
- which coherent action in our strategy it serves, or "none."

Flag duplicate requests, single-account themes and any theme that conflicts with our guiding policy. Our strategy one-pager is below.

[strategy one-pager]
[requests]

Check the output: spot-check five requests to confirm they landed in the right theme, and verify the ARR totals against the CRM. Themes marked "none" are candidates for a polite no, not for scoring.
```

```prompt title="Score the same items under two lenses"
Goal: See how much your framework choice is changing the answer.
Paste in: five to ten candidate items with whatever you know about reach (in accounts), impact, confidence, effort, time criticality, enablement and cost of delay, plus your strategy one-pager.

Score these items for [product] twice:
1. RICE, with reach measured in accounts per quarter, impact on the 3 / 2 / 1 / 0.5 / 0.25 scale, confidence at 100% / 80% / 50% and effort in person-months.
2. WSJF, with cost of delay as user and business value plus time criticality plus risk reduction or opportunity enablement, divided by job duration.

Show both rankings side by side. For every item whose rank differs by two or more places, explain which input drives the difference. Then say which lens better fits our guiding policy, and why. Grade the evidence behind each input as opinion, anecdote or market data, customer evidence, or usage data, and flag scores that rest mostly on opinion.

[items]
[strategy one-pager]

Check the output: the model will fill gaps with plausible numbers. Strike any input you didn't provide, and rerun. The decision column stays yours.
```

```prompt title="Generate audience views from one roadmap"
Goal: Produce consistent executive, field, customer and partner views without retyping the roadmap four times.
Paste in: the source now-next-later roadmap with each item's type (commitment, bet, exploration), the Won't list, the changelog and your company's approved forward-looking disclaimer.

From this roadmap for [product], create four views:
1. Executive (one page): outcomes, strategic bets, capacity split, top risks, decisions needed.
2. Field: a three-sentence talk track, commitments with dates, Next and Later themes without dates, the Won't list, how to log a request, and the disclaimer verbatim.
3. Customer: problems we're solving and direction, commitments only if marked contractual, design-partner invitations.
4. Partner and developer: API changes, deprecations with notice periods, dependencies.

Rules: never show a date on any item not typed "commitment." Never include exploration specifics in the field or customer views. Copy the disclaimer exactly.

[roadmap]

Check the output: search every view for dates and confirm each belongs to a commitment. Read the field view as a seller would: is there any sentence a customer could hear as a promise?
```

```prompt title="Run the quarterly capability check on AI bets"
Goal: Decide which AI roadmap items a new model has moved, and which assumptions no longer hold.
Paste in: your capability watchlist, the latest eval results for the current and new models, inference cost per task for each, and the "what would have to be true" list for each AI bet.

For [product], compare the eval results against each watchlist threshold. For every Later or Next item:
- Has the threshold been met, nearly met or not met? Cite the eval figures.
- What would the change in inference cost do to unit economics at current volume?
- Which "what would have to be true" conditions are now true, still open or no longer true?

Recommend which items should move columns, which bets should be killed, and whether any model migration is now time-critical because of a retirement date. Separate what the evals show from your recommendation.

[watchlist]
[eval results]
[cost data]
[conditions]

Check the output: confirm every cited eval figure against the source run. Don't move an item to a dated commitment on the strength of one eval run.
```

## Anti-patterns

:::warn The goal list posing as strategy
"Grow ARR 40%, reach 90% retention, become the AI leader." Those are outcomes you want. Without a diagnosis of what stands in the way and a policy for getting past it, the document can't guide a single prioritization call.
:::

:::warn The strategy that refuses nothing
Every segment, every channel, every buyer, every integration. The roadmap shows it first: twelve themes, each one underfunded, and no reason a seller can give for any no.
:::

:::warn Scoring before filtering
The team spends a workshop scoring two hundred backlog items with RICE. Half of them don't serve any coherent action, and the debate over their impact scores eats the afternoon. Filter by strategy first, then score what's left.
:::

:::warn False precision
Impact 2, confidence 80%, effort 3.5 person-months, RICE score 137.1. The decimal places hide that every input was a guess. Show the evidence level beside every score, and round the scores.
:::

:::warn The dated wish list
A roadmap of untested features with quarter dates, shared with sales. Every slip becomes a broken promise, and every discovery that kills a feature becomes an escalation. Date commitments only, and label everything else as a bet.
:::

:::warn The infinite backlog
Eight hundred items, most of them years old, many duplicates, none ever deleted. The team spends refinement time on items that will never be built, and sellers believe "it's on the backlog" means something. Keep the delivery backlog short and archive by rule.
:::

:::warn Roadmapping around a model's limits
A team spends two quarters building elaborate scaffolding to work around a model's weakness, and the next model release removes the weakness. Frame AI roadmap items as outcomes, keep a capability watchlist and re-test each quarter before investing in workarounds.
:::

## Checklist

- [ ] The strategy names a diagnosis, with evidence, and a guiding policy with at least three explicit refusals.
- [ ] The where-to-play choices name the segment, buyer, channel and ecosystem position, including what's out.
- [ ] Each strategy is an SMT: a hypothesis with a proxy metric the team can move within a quarter.
- [ ] The DHM covers delight per persona, what's hard to copy and how the strategy improves margin.
- [ ] The strategy one-pager has a measurable proximate objective and passed a check against Rumelt's four hallmarks.
- [ ] Items are filtered by strategy before they are scored.
- [ ] The scorecard states the chosen lens and why, shows an evidence level beside every score, and records every departure from score order.
- [ ] The backlog is split into request inbox, opportunity backlog and a short delivery backlog, with an ageing rule.
- [ ] The capacity split is written down and reviewed quarterly.
- [ ] The roadmap labels every item as commitment, bet or exploration, and only commitments carry dates; every commitment passed discovery and has an engineering estimate.
- [ ] Audience views come from one source, the field view includes the Won't list and the approved disclaimer, and each view has a changelog.
- [ ] For AI products, the roadmap has a capability watchlist, an eval and model-migration lane, and no customer dates that depend on unreleased model improvements.
- [ ] Externally dated items (model retirements, regulatory deadlines, deprecations) are tracked to their source and replanned when they move.

## Key takeaways

- A strategy is a diagnosis, a guiding policy and coherent actions. If it doesn't name the challenge and rule things out, it's a plan or a goal list.
- Use the Playing to Win cascade to force explicit where-to-play and how-to-win choices, and Biddle's DHM and SMT to turn them into hypotheses with proxy metrics.
- Prioritization frameworks rank only what passes the strategy filter. Each one has a built-in bias, so choose the lens deliberately; in B2B, measure reach in accounts or ARR and price cost of delay where you can.
- Keep three backlog stores: a request inbox that's never promised, an opportunity backlog tied to strategy and a short, ordered delivery backlog.
- Build one now-next-later roadmap that labels every item as commitment, bet or exploration. Date only commitments, and generate audience views with a changelog from that one source.
- For AI products, frame roadmap items as outcomes, watch capability thresholds on your own evals, budget for model migration and treat model retirements and regulatory dates as commitments that can move.
