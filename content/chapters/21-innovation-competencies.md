<p class="lead">Innovation strategy (Chapter 20) tells you where to place bets. This chapter is about the skills that make each bet cheaper to test: Lean Startup, customer development, design thinking and a maker's habit of building to learn. In 2026 the building part is close to free. The scarce things are a crisp hypothesis, real customer attention and the nerve to kill an idea the evidence has already killed.</p>

## Why this matters

Enterprise product organizations are good at execution: take a defined product, staff it, ship it, sell it. That machinery is wrong for a new idea whose customer, problem, solution and business model are still guesses. Run one through it and you get a roadmap, a launch date and a sales target for something nobody has shown anyone wants.

Steve Blank's central observation is that a startup is not a smaller version of a large company. A large company executes a known business model; a new venture searches for one. A new product line inside an established company is in search mode too, and search mode needs different tools, different metrics and a different idea of progress.

The methods in this chapter come from different traditions and argue with each other at the edges, but they share a core:

1. **Treat the plan as a set of hypotheses**, not a set of commitments.
2. **Get to real customers early**, because opinions formed inside the building are guesses.
3. **Build the least you can to learn the most you can**, then measure honestly.
4. **Decide on a schedule** whether to keep going, change course or stop.

A Senior or Principal PM is judged on whether their bets produced learning that changed decisions, whatever the count of workshops and prototypes. AI harnesses now let a PM build a working prototype in an afternoon, so the old excuse ("we can't test it until engineering builds it") is gone. That leaves the hard parts: hypotheses sharp enough to fail, thresholds set in advance and decisions made on a schedule.

:::key The unit of progress
In search mode, progress is validated learning: something you now know about customers, demonstrated with evidence, that changes what you do next. Features shipped, prototypes built and workshops held are activity. Count them only when they produced a decision.
:::

## The innovation competencies

### Lean Startup: build, measure, learn

Eric Ries coined "lean startup" on his blog in September 2008 and set it out in *The Lean Startup* in September 2011, building on Steve Blank's customer development and on lean manufacturing and lean software development. Ries's organization summarizes it as five principles:

1. **Entrepreneurs are everywhere**, including product teams inside large companies.
2. **Entrepreneurship is management**: search mode needs its own management practice.
3. **Validated learning** is the unit of progress.
4. **Innovation accounting** measures progress, sets milestones and prioritizes work with actionable metrics.
5. **Build-Measure-Learn**: turn ideas into products, measure how customers respond, learn whether to pivot or persevere, and speed up the loop.

The loop runs build, measure, learn, but you plan it backwards: decide what you need to learn, then what you'd measure to learn it, and only then the least you must build to produce that measurement. Teams that plan forwards build first and look for something to measure afterwards, which is how a pilot ends with a satisfaction survey and no decision.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 300" role="img" aria-label="Build-Measure-Learn loop, run clockwise and planned counter-clockwise">
  <rect x="245" y="20" width="150" height="56" rx="10" class="box"/>
  <text x="320" y="44" text-anchor="middle" class="t">Build</text>
  <text x="320" y="63" text-anchor="middle" class="s">least effort that yields evidence</text>
  <rect x="440" y="200" width="170" height="56" rx="10" class="box"/>
  <text x="525" y="224" text-anchor="middle" class="t">Measure</text>
  <text x="525" y="243" text-anchor="middle" class="s">actionable metric, set threshold</text>
  <rect x="30" y="200" width="170" height="56" rx="10" class="box"/>
  <text x="115" y="224" text-anchor="middle" class="t">Learn</text>
  <text x="115" y="243" text-anchor="middle" class="s">pivot, persevere or stop</text>
  <line x1="395" y1="60" x2="500" y2="196" class="ln" style="stroke:var(--a1)"/>
  <line x1="440" y1="236" x2="204" y2="236" class="ln" style="stroke:var(--a1)"/>
  <line x1="140" y1="196" x2="245" y2="60" class="ln" style="stroke:var(--a1)"/>
  <text x="470" y="118" class="s" style="fill:var(--a1)">Run: build, then measure</text>
  <text x="320" y="228" text-anchor="middle" class="s" style="fill:var(--a1)">then learn</text>
  <text x="320" y="140" text-anchor="middle" class="t" style="fill:var(--a2)">Plan in reverse</text>
  <text x="320" y="160" text-anchor="middle" class="s" style="fill:var(--a2)">1. What must we learn?</text>
  <text x="320" y="176" text-anchor="middle" class="s" style="fill:var(--a2)">2. What would show it?</text>
  <text x="320" y="192" text-anchor="middle" class="s" style="fill:var(--a2)">3. What is the least we build?</text>
  <text x="320" y="288" text-anchor="middle" class="s">The loop runs build, measure, learn. The plan starts from the learning.</text>
</svg>
<figcaption>Build-Measure-Learn. Run the loop clockwise, but plan it from the learning goal backwards, so that what you build exists only to produce a measurement that answers a question.</figcaption>
</figure>

#### The minimum viable product

Ries defines the MVP as the version of a new product that lets a team collect the most validated learning about customers with the least effort. In a 2009 blog post he corrected the common misreading: an MVP is the fastest route to learning, which differs from the smallest product you can ship, and it adds work, because the team now has to actually learn. His own example: a simple online ad test would have exposed a bad concept faster than two weeks of building.

Treat MVPs as a menu, chosen by the riskiest assumption. The names below are the common taxonomy across the lean literature rather than one author's list.

| MVP type | What the customer sees | What it tests | B2B example |
|---|---|---|---|
| **Smoke test or fake door** | A landing page, button or menu item for something that doesn't exist yet | Demand: will they click, sign up or ask? | A "Request early access" tile in the admin console |
| **Explainer video** | A short video of the product working | Whether the concept is understood and wanted | A two-minute walkthrough sent to design partners before a build |
| **Concierge** | The service, delivered visibly by people | Whether the outcome is valuable at all | A product ops lead compiling a report by hand each week |
| **Wizard of Oz** | What looks like a working product, with people operating it behind the scenes | Whether customers use and trust the product experience | An "agent" recommendation that an engineer checks before it's shown |
| **Single-feature** | One working capability, nothing else | Whether the core value holds up in real use | Diagnosis only, without remediation |
| **Piecemeal** | A product stitched from existing tools | End-to-end value before custom build | A workflow assembled from chat, ticketing and a shared document |
| **Presale or letter of intent** | An offer to buy something not yet built | Willingness to pay and procurement path | A signed letter of intent or a paid pilot agreement |

Two consumer stories recur. Zappos founder Nick Swinmurn photographed shoes in stores and sold them online before the company held any stock. Dropbox, as Ries tells it, used an explainer video to test demand before the product was ready. In B2B the strongest MVPs are usually concierge, Wizard of Oz and presale, because enterprise buyers judge outcomes and contracts more than interfaces.

:::onramp Concierge versus Wizard of Oz
Both put humans where software will eventually be. In a concierge MVP the people are visible, and you're testing whether the outcome is worth having. In a Wizard of Oz MVP the customer sees a product, and you're testing whether they'll use and trust it. In enterprise settings, tell the customer's contract owner what's manual even when the end user can't see it.
:::

#### Innovation accounting

Search mode breaks normal metrics: revenue is near zero, and every chart rises because it starts from nothing. Ries's answer is innovation accounting, which in *The Lean Startup* runs through three milestones:

1. **Establish the baseline.** Use an MVP to get real data on where the business stands today, not where the plan says it will be.
2. **Tune the engine.** Run experiments that move the baseline toward the ideal in the business plan.
3. **Pivot or persevere.** If tuning isn't moving the numbers fast enough, the hypothesis is wrong; change it.

The metrics have to be **actionable**. **Vanity metrics** paint the rosiest picture without reflecting what drives the business: cumulative sign-ups, total page views, logos on a slide. Actionable metrics show cause and effect, usually by cohort, so you can see whether this week's customers behave better than last month's because of something you changed. Ries also asks that metrics be accessible (people can understand them) and auditable (people can trace them to real customers).

For enterprise products, the problem is time. A long sales cycle means revenue arrives months after the decision it should inform. Use leading indicators that move within weeks: weekly active users among design partners, the acceptance rate of an AI recommendation in a pilot, security reviews passed, procurement stages reached, letters of intent signed. Choose metrics that can embarrass you before the quarter ends; Chapter 05 covers the analytics.

#### Pivots

Ries defines a pivot as a structured course correction designed to test a new fundamental hypothesis about the product, strategy or engine of growth. Blank's shorter version: a pivot changes the plan, not the executive. In a 2009 post Ries warned against jumping to an unrelated vision, which throws away what you've learned. His advice is to keep "one foot in the past": hold on to the validated learning and change one fundamental hypothesis.

*The Lean Startup* catalogues ten pivot types:

| Pivot | What changes | Enterprise example |
|---|---|---|
| **Zoom-in** | One feature becomes the whole product | Diagnosis becomes the product; remediation waits |
| **Zoom-out** | The whole product becomes one feature of something larger | A standalone tool becomes a module of a platform |
| **Customer segment** | Same product, different customer | Sell through managed service providers instead of direct |
| **Customer need** | Same customer, different problem | Solve audit preparation instead of incident response |
| **Platform** | Application becomes platform, or the reverse | Open the agent framework to partners |
| **Business architecture** | High margin and low volume, or low margin and high volume | Move from enterprise sales to a self-serve tier |
| **Value capture** | How you make money | Per-environment fee becomes per-resolved-incident price |
| **Engine of growth** | Viral, sticky or paid growth | Rely on expansion within accounts instead of new logos |
| **Channel** | How you reach customers | Partner resale instead of direct sales |
| **Technology** | Same solution, different technology | A rules engine replaced by an AI agent |

In B2B, value capture and business architecture pivots are common and underrated, because many enterprise ideas fail on the business model while the product is fine. Chapter 15 covers pricing.

Ries also proposed a regular strategic review, for example once per development cycle, so pivot decisions get made on a schedule against evidence. His warning signs: a chronically frustrated team, experiments that produce only modest gains, and doubt about three questions. Are we solving an important problem? Are early adopters actually adopting? Does the product deliver what it promises?

Ries's *The Startup Way* (2017) applies the method inside established companies, drawing on his work with GE on its FastWorks program, and is associated with metered funding: internal ventures get money in tranches tied to validated learning (Chapter 23).

:::note The critiques of Lean Startup
Ben Horowitz argued in 2010 that some markets reward running fat: spending heavily to grab a market quickly. Teppo Felin, Alfonso Gambardella, Scott Stern and Todd Zenger argued that lean methods bias teams toward incremental, easily testable ideas. Daniel Levinthal pointed out that many of its ideas existed earlier in management research. It also fits badly where prototypes are expensive or risky, where tests cost more than the learning is worth and where teams can't interpret their own experiments. Use the method where a cheap test can answer a real question. Where it can't, make the bet deliberately and say so.
:::

### Customer development: get out of the building

Steve Blank developed customer development in the 1990s from patterns across his own startups, first set it out in *The Four Steps to the Epiphany* and later turned it into an operating guide with Bob Dorf in *The Startup Owner's Manual*. The core idea is that a new venture's business model is a set of untested hypotheses, and the only place to test them is with customers. His slogan, "get out of the building," means exactly that: there are no facts inside your office.

The method has four steps. The first two are **search**; the last two are **execute**.

1. **Customer discovery.** Turn the business model into hypotheses and test them with customers.
2. **Customer validation.** Prove the sale is repeatable and scalable.
3. **Customer creation.** Scale demand once the model is proven.
4. **Company building.** Organize to execute the proven model.

You iterate inside the search steps. A failed validation sends you back to discovery with a new hypothesis, which is a pivot by another name. Blank's Lean LaunchPad course spread the method to more than 75 universities, and the US National Science Foundation adopted it for its Innovation Corps (I-Corps) program in 2011.

In enterprise products, adapt it two ways:

- **The customer is a buying group.** Discovery has to cover the end user, the champion, the economic buyer and the security gatekeeper separately (Chapter 01 sets out the B2B persona set). An idea can pass discovery with users and fail it with the gatekeeper.
- **Validation means a repeatable sale.** One enthusiastic design partner is discovery evidence. Validation is several customers buying without heroic help: a sales rep closes without the PM on the call, and security reviews pass without a custom exception.

### Design thinking: from empathy to prototype

Design thinking came to business largely through IDEO and Stanford. IDEO describes it as a human-centered approach to solving complex problems, says it helped make design thinking accessible rather than inventing it, and credits David Kelley, Tim Brown and Jane Fulton Suri. Kelley helped found Stanford's Hasso Plattner Institute of Design (the d.school). Brown's 2008 Harvard Business Review article "Design Thinking" argued that design belongs at the front of product, service and strategy work instead of at the end as styling.

IDEO frames the target as the overlap of three lenses: **desirability** (what people value), **feasibility** (what technology makes possible) and **viability** (what the organization needs to succeed). David Bland uses the same three to sort assumptions. For B2B products this book adds a fourth, **adoptability**: will the buying group, security review and procurement let it through? The extension is this book's own (Chapter 01).

#### The d.school's five modes

The d.school's *Design Thinking Bootleg* (2018) names five modes of design work and describes itself as a set of tools and methods that keeps evolving. Treat the modes as a vocabulary, not a waterfall.

| Mode | What you do | Enterprise PM version |
|---|---|---|
| **Empathize** | Observe and engage people to understand their experience | Sit with the on-call engineer through a real incident review |
| **Define** | Frame a meaningful, actionable problem from what you saw | Write the job story and the point of view for one persona |
| **Ideate** | Generate many options before choosing | Ten approaches to the approval step, including "no approval" |
| **Prototype** | Make ideas tangible enough to react to | A clickable or AI-built facade of the approval screen |
| **Test** | Put the prototype in front of people and learn | Five sessions with real responders, scored against a threshold |

The Nielsen Norman Group's version, by Sarah Gibbons, adds a sixth phase, **Implement**, and groups the six into three stages: understand, explore and materialize. Both sources stress that the phases loop. Testing usually sends you back to understanding.

#### The Double Diamond

The UK Design Council developed the Double Diamond out of work it began in 2003 to describe the design process in a common way. It has four phases in two diamonds:

- **Discover**: understand the real problem by spending time with the people affected.
- **Define**: reframe the challenge using what discovery revealed.
- **Develop**: generate varied solutions, ideally co-designed with users.
- **Deliver**: test at small scale, reject what fails and improve what works.

Each diamond opens up the options, then narrows them: the first on the problem, the second on the solution. The Design Council stresses that teams often loop back. Its wider **Framework for Innovation** adds four principles (put people first; communicate visually and inclusively; collaborate and co-create; iterate, iterate, iterate), plus leadership that permits experimentation and engagement with the people delivering and receiving the work.

The most common enterprise failure is skipping the first diamond. A large customer "asked for" a feature, so the team starts in Develop with the customer's proposed solution as the brief. The customer's request is a clue about a problem, not a definition of it.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 260" role="img" aria-label="Double Diamond with where design thinking, Lean Startup, customer development and experiments are strongest">
  <polygon points="30,110 165,30 300,110 165,190" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <polygon points="300,110 435,30 570,110 435,190" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="97" y="114" text-anchor="middle" class="t">Discover</text>
  <text x="232" y="114" text-anchor="middle" class="t">Define</text>
  <text x="367" y="114" text-anchor="middle" class="t">Develop</text>
  <text x="502" y="114" text-anchor="middle" class="t">Deliver</text>
  <text x="165" y="20" text-anchor="middle" class="s">Problem space</text>
  <text x="435" y="20" text-anchor="middle" class="s">Solution space</text>
  <line x1="30" y1="212" x2="300" y2="212" class="ln" style="stroke:var(--a1)"/>
  <text x="165" y="206" text-anchor="middle" class="s" style="fill:var(--a1)">Design thinking strongest here</text>
  <line x1="300" y1="230" x2="610" y2="230" class="ln" style="stroke:var(--a2)"/>
  <text x="455" y="224" text-anchor="middle" class="s" style="fill:var(--a2)">Lean Startup MVPs and innovation accounting</text>
  <line x1="470" y1="248" x2="610" y2="248" class="ln" style="stroke:var(--a3)"/>
  <text x="465" y="252" text-anchor="end" class="s" style="fill:var(--a3)">Customer development: validate a repeatable sale</text>
  <text x="590" y="114" class="s" style="fill:var(--muted)">loop</text>
</svg>
<figcaption>Where each method is strongest. Design thinking does its best work in the first diamond, Lean Startup in the second, and customer development carries the idea into a repeatable sale. Bland's experiment library runs across all of it.</figcaption>
</figure>

#### The critiques of design thinking

Design thinking's critics describe what many enterprise design programs actually produce. Rebecca Ackermann's 2023 retrospective in MIT Technology Review gathered the main lines:

- **Short, fresh-eyes engagements** produce recommendations ungrounded in how the work really happens.
- **Innovation theater**: workshops and sticky notes that change nothing.
- **Pilots that stall before scale**, such as an IDEO.org project that became too expensive to scale and a 2013 San Francisco school cafeteria redesign that relied on connected vending machines many sites couldn't support.
- **Designers as privileged interpreters.** Lilly Irani argued in 2018 that the method elevates designers over the people they interpret; former IDEO designer George Aye described consultants as tourists.

Ackermann also reports the responses: the d.school's revamped degree materials drop the "design thinking" label and talk about making and care instead of empathy, and Tim Brown argues lasting impact needs capability building and longer engagements. For an enterprise PM, a two-day workshop with no follow-through, no build and no metric is theater. Tie every design activity to an experiment with a threshold and a decision someone will make.

### Testing Business Ideas: the experiment library

David J. Bland and Alexander Osterwalder's *Testing Business Ideas* (2019) connects these traditions. It turns design thinking's three lenses and Lean Startup's loop into a practice: break an idea into testable assumptions, prioritize them, test the riskiest with the cheapest experiment that gives strong enough evidence, and decide.

The book's library holds more than 40 experiment types, each graded by cost, time to run and strength of evidence. They split broadly into two families:

- **Discovery experiments**: cheap, fast and weaker evidence. Customer interviews, search trend analysis, discussion forums, explainer videos, paper prototypes.
- **Validation experiments**: costlier and stronger evidence. Concierge, Wizard of Oz, mock sales, letters of intent, presales, split (A/B) tests and single-feature MVPs.

Bland's **assumptions mapping**, which he learned from Jeff Gothelf, Josh Seiden and Giff Constable, is covered in Chapter 01. Here the important tool is the **Test Card**, which forces four things into the open before a test runs: the hypothesis that must hold, how you'll test it, what you'll measure and what success looks like, including the threshold. Its partner, the **Learning Card**, records afterwards what you believed, what you observed, what you learned and what you'll do as a result. After each round, each hypothesis is marked right, wrong or still unclear.

Bland rates what people do above what they say. Translated to B2B:

| Weaker evidence | Stronger evidence |
|---|---|
| "This is interesting" in a quarterly business review | A signed letter of intent with a named budget owner |
| A survey where most respondents say they'd consider it | A paid pilot, even a small one |
| A design partner's enthusiasm in a workshop | The design partner's security team approving the integration |
| Clicks on a fake-door tile | Customers completing a request form that names their environment and timeline |

### Design sprints

Jake Knapp began running design sprints at Google in 2010, on products including Chrome and Search, and brought them to GV in 2012 with contributions from Braden Kowitz, Michael Margolis, John Zeratsky and Daniel Burka. Knapp, Zeratsky and Kowitz published the method as *Sprint* in 2016. A sprint compresses a double diamond into five days:

| Day | Work |
|---|---|
| **Monday: Map** | Set a long-term goal, map the challenge, ask experts, pick a target customer and moment |
| **Tuesday: Sketch** | Remix existing ideas, sketch solutions individually, start recruiting customers |
| **Wednesday: Decide** | Critique the sketches, choose, and storyboard the prototype |
| **Thursday: Prototype** | Build a realistic facade ("fake it") and write the interview script |
| **Friday: Test** | Interview customers and watch how they react |

The book adds about seven people or fewer, a **Decider** who makes the calls, a **Facilitator** who runs the room and five customer interviews on Friday, drawing on Jakob Nielsen's usability research. Knapp and Zeratsky have since added a **Foundation Sprint** for earlier-stage work.

In enterprise products, recruit five people per persona that matters and don't mix them; five SRE leads and five security reviewers will tell you different things. The facade is usually an admin console, an approval flow or an ROI report, and an AI harness can now build it in hours.

### Maker culture and rapid experimentation

Maker culture grew out of do-it-yourself culture. Dale Dougherty launched *Make:* magazine in 2005 and Maker Faire in 2006, hackerspaces, fab labs and makerspaces spread the tools, and cheap 3D printing made one-off prototypes affordable. Neil Gershenfeld compared the spread of digital fabrication to the shift from minicomputers to personal computers.

The lesson for software PMs is "make to think": a prototype is an argument and a learning tool, and nobody should mistake it for a deliverable. When trying an idea costs this little, the question changes from "should we build this?" to "what would we learn if we built it this afternoon?"

The same habit scales into large-company experimentation. Stefan Thomke's 2020 Harvard Business Review article "Building a Culture of Experimentation" describes Booking.com running about 25,000 tests a year, including a test of a stripped-down home page that removed years of optimized content. Most B2B products don't have that traffic, so enterprise experiments are usually qualitative or small-sample: design partners, pilots and fake doors in an admin console. They're still worth running, as long as every experiment card states its evidence strength honestly. Chapter 05 covers controlled experiments for products with the volume.

:::leader For product leaders
These competencies don't survive a funding model that rewards confident plans. If teams get money by promising a launch date and a revenue number, they'll hide uncertainty instead of testing it. Fund early bets in tranches against learning milestones, ask for the experiment card before the roadmap, and treat a well-evidenced "stop" as a success. Chapter 23 covers the governance.
:::

### How the methods fit together

A workable division of labor:

| Question | Strongest method | Typical artifact |
|---|---|---|
| What problem is worth solving, for whom? | Design thinking, first diamond | Point of view, journey map |
| Is the business model real? | Customer development | Business model hypotheses, buying-group interviews |
| What is the riskiest assumption, and how do we test it? | Testing Business Ideas | Experiment card |
| Is our solution any good? | Design sprint, Lean Startup MVP | Prototype, MVP plan |
| Are we making progress? | Innovation accounting | Innovation accounting dashboard |
| Should we change course? | Pivot-or-persevere review | Review record |

## How to apply it

Here's an eight-week cycle for taking one innovation bet from hypothesis to a pivot-or-persevere decision. It assumes the bet was chosen through the innovation strategy in Chapter 20 and that the product hypothesis and assumption map from Chapter 01 exist.

**Week 1: Frame the bet.**

1. Decide which diamond you're in. If the problem isn't yet evidenced with the people who have it, spend the cycle on the first diamond, whatever the customer's feature request says.
2. Pull the top-right quadrant from the assumption map: important assumptions with little evidence. Label each desirability, feasibility, viability or adoptability.
3. Agree who decides. Name a Decider for the cycle and a date for the pivot-or-persevere review, and put both in the calendar now.

**Week 2: Design the experiments.**

4. Write an experiment card for each of the top three assumptions. Fill in the Test Card fields (we believe, to verify that we will, and measure, we are right if) before anyone builds anything. The threshold is a number or an observable behavior, written down in advance.
5. Pick the cheapest experiment that produces evidence strong enough for the decision. Spending two engineering quarters needs stronger evidence than running another test.
6. For anything that needs a build, write an MVP plan: the MVP type, who sees it, how they're recruited, what you won't build and what happens to the MVP after the decision.

**Week 3: Set the baseline.**

7. Choose three to five actionable leading indicators for the bet and get today's value for each, by cohort. Write down the vanity metrics you'll deliberately ignore.
8. Put them on an innovation accounting dashboard alongside the experiments and their status.

**Weeks 3 and 4: Prototype and sprint where it pays.**

9. If the riskiest assumption is about the solution experience, run a five-day design sprint on it, with five customers per key persona on the Friday.
10. Build prototypes with your AI harness as realistic facades. Label what's faked, keep real customer data out and decide who on the team checks the prototype before a customer sees it.

**Weeks 4 to 7: Run, measure, learn.**

11. Run the experiments. Write a learning card within two days of each result, with the evidence attached.
12. Update the dashboard weekly. Mark each assumption right, wrong or still unclear.
13. Kill experiments that can no longer change the decision.

**Week 8: Decide.**

14. Hold the pivot-or-persevere review. Bring the dashboard, the learning cards and the options: persevere, pivot (name the type) or stop. For each, state the cost and what you'd keep.
15. Record the decision, the reason and the next milestone. A pivot starts a new cycle with a new hypothesis; a stop gets a short write-up so the learning isn't lost.

:::key Thresholds before data
Write the success threshold before the experiment starts. A threshold chosen after you see the result is a rationalization. If the team can't agree on a threshold, it doesn't yet agree on what the experiment is for.
:::

## The AI lens

### Building AI-powered products

AI products put extra weight on certain assumptions, and the methods need small adjustments to test them.

- **Feasibility is a quality distribution.** For an AI feature, feasibility means how often the model is right, on which inputs, at what cost per call. Treat model quality as an assumption with a threshold and test it with an evaluation set before you test desirability with customers (Chapter 31 covers evals).
- **Wizard of Oz is the natural AI MVP.** A person who produces or checks the output behind the interface separates the desirability question (do they want this output?) from the feasibility question (can the model produce it reliably?).
- **Trust is usually the riskiest assumption.** For agents that act, the open question is whether customers will let the agent act, and under what controls. Test approval rates, overrides and what the gatekeeper requires.
- **Viability includes inference cost.** An AI MVP can be desirable and feasible and still lose money on every use. Track cost per successful outcome from the first experiment, and expect a value capture pivot on the table at the first review.

### Doing the work with AI

The biggest change in 2026 is the cost of the Build step. Anthropic introduced Artifacts with Claude 3.5 Sonnet in June 2024, putting generated code, documents and site designs beside the conversation for editing in real time. Figma launched Figma Make, a prompt-to-app tool for interactive prototypes, in May 2025. In July 2025 Anthropic described its designers feeding design files to Claude Code to iterate on working feature code, and people in legal and data science building working prototypes without being software engineers.

Andrej Karpathy named the casual end of this "vibe coding" in February 2025: describe what you want in plain language, accept the generated code and steer by results. In March 2025 Y Combinator's Jared Friedman informally estimated that about a quarter of its Winter 2025 batch had codebases about 95% generated by AI, while YC's partners stressed that founders still needed the skill to judge and fix the output.

For a PM, the harness is now the makerspace: a clickable approval flow, a mock ROI report or a fake-door tile takes an afternoon. Three consequences follow.

**The bottleneck moves from building to learning.** When building is nearly free, the scarce resources are customer attention, crisp hypotheses and the willingness to kill ideas. Lean Startup's "least you must build" becomes "least customer time you must spend." Design experiments so each customer conversation answers a real question.

**Measured speed isn't perceived speed.** METR's July 2025 randomized study of 16 experienced open-source developers, working on 246 real issues in their own repositories, found they took 19% longer when AI tools were allowed. The developers had expected a 24% speedup and still believed afterwards that they'd been about 20% faster. METR is explicit about the limits (a small sample, early-2025 tools, one setting), now labels the results out of date and never claimed AI slows most developers. What the study does show is that people misjudge their own speed. Apply innovation accounting to your own process: measure the cycle time from hypothesis to decision, and ignore the number of prototypes produced.

**AI-built prototypes carry real risk.** Public reporting in 2025 described apps built on vibe-coding platforms exposing personal data and an AI coding agent deleting a production database. A prototype you show an enterprise customer is a facade. It should never touch real customer data or production systems without the same security review as any other software. Label it as a prototype on screen.

:::ai Synthetic users are not test subjects
Chapter 01 covers synthetic users in depth, including NN/g's October 2026 finding that they produce far less variety than human respondents. In experiment terms: a synthetic respondent can help you pilot a script or generate hypotheses, but it can never satisfy the "we are right if" line on an experiment card or appear on a learning card as evidence.
:::

The harness is useful for drafting experiment cards and candidate thresholds, proposing the cheapest test that gives strong enough evidence, building facades, turning session notes into learning cards with sources attached, and assembling the pivot review pack (the Prompts section has one for each). It can't decide what a result means for the strategy, set the threshold for you or stand in for the customer.

## The Beacon case: experimenting toward Beacon Agents

:::example Where Beacon stands
Chapter 01 left Beacon with a revised hypothesis: diagnosis ships first, aiming at a 60% acceptance rate in pilots, and supervised action follows once audit logs, scoped credentials and a kill switch exist. Northlight wants to launch Beacon Agents at Northlight Live. Gross margin has dropped from 81% to 72% since the agentic features launched, because of inference cost, and the pricing team wants to move from per-environment pricing to a per-resolved-incident price. You have three bets to test before the launch, and a leadership team that would prefer a roadmap.
:::

**Framing the bets.** The top-right quadrant of the assumption map becomes three bets, each with an owner and a Decider:

1. **Supervised remediation trust** (desirability and adoptability): SRE leads like Priya will approve agent-proposed runbook steps inside the approval gate.
2. **Per-resolved-incident pricing** (viability): economic buyers like Marcus will accept a price per resolved incident, and partners like Leo can bill their own customers that way.
3. **MSP multi-tenant view** (desirability): managed service providers want a per-customer view of incidents enough to justify building one.

**Experiment 1: a Wizard of Oz for remediation.** Building the full Act capability would take quarters. Instead, five design-partner environments get an approval card: Beacon proposes a runbook step (restart, roll back or scale) with cited evidence, and a Northlight engineer checks it before it appears. The contract owners know a human is in the loop. The card reads: *We believe that SRE leads will approve agent-proposed runbook steps. To verify that, we will show verified proposals in five design-partner environments for four weeks. And measure approval rate and time to approve. We are right if at least 60% of proposals are approved within two minutes* (a fictional threshold the team set before the test). Sam reviews the card first, because the gatekeeper's requirements are part of the assumption.

**Experiment 2: a mock sale for pricing.** Live billing stays untouched. In renewal conversations, account teams show Marcus-type buyers a pricing page with per-resolved-incident options beside the current per-environment price and record what buyers choose to discuss and what they object to. The partner team asks three MSPs for letters of intent for per-incident billing. The card rates buyer preferences in conversation as medium evidence and a signed letter of intent as strong.

**Experiment 3: a concierge for MSPs.** Before anyone designs a multi-tenant interface, the shared product ops lead compiles a weekly per-customer incident report by hand for three MSP partners. If Leo's team uses the reports in their own customer reviews, the need is real; if the reports go unread, nobody builds a dashboard.

**A design sprint for Dana.** The designer runs a five-day sprint on a long-term goal Beacon already has: Dana knows what broke and what to do in under five minutes. On Thursday the team builds the incident summary card as a facade with the AI harness, using fabricated incidents. On Friday they run five sessions with on-call engineers, and a separate set with security reviewers on what the audit trail must show.

**The dashboard.** By design-partner cohort, the dashboard tracks diagnosis acceptance rate, MTTR, autonomous resolution rate on allowlisted actions, proposal approval rate and inference cost per resolved incident, which ties the bet to the margin problem. It deliberately leaves out total agent invocations, which go up whatever happens.

**The pivot-or-persevere review.** Midway through the cycle, a customer rolls back the wrong service on a hallucinated Beacon root cause. The review moves forward, with three options for the Decider:

- **Persevere**, with stronger evals and a cited-evidence threshold below which Beacon won't propose an action.
- **Zoom-in pivot**: make diagnosis the product for now and remove Act for a segment of customers until trust is rebuilt.
- **Customer segment pivot**: launch Beacon Agents first with MSPs, whose operators run remediations across many customers and may value the speed more.

The Decider chooses to persevere with diagnosis and narrow Act to allowlisted low-risk actions with the cited-evidence threshold, with no rollback proposals until the evals pass. The correlation and diagnosis learning stays and only the riskiest part of the bet changes. The Northlight Live launch message changes with it (Chapter 25), and the pricing experiment continues, because its evidence never depended on Act.

## Product 360 artifacts

```template id="21-experiment-card" title="Experiment card"
# Experiment card · [Experiment name] · [ID] · [Date]

**Owner:** [PM]   **Decider:** [Name]   **Linked bet or opportunity:** [Link]   **Status:** Designed / Running / Done

## Riskiest assumption
[One assumption from the assumption map]
Type: desirability / feasibility / viability / adoptability (buying group, security, procurement)

## Test card (complete before the test starts)
- We believe that: [assumption]
- To verify that, we will: [experiment type, audience, number of customers, duration]
- And measure: [metric or observable behavior]
- We are right if: [threshold, written before any data arrives]

## Cost and evidence
- Cost (people, money, customer time):
- Time to result:
- Evidence strength expected: weak / medium / strong, and why
- What decision this evidence will inform:

## AI disclosure
- Generated by the AI harness: [prototype / analysis / draft materials]
- From real customers: [sessions, behavior, signatures]
- Synthetic output used as evidence: none (synthetic output may only prepare the test)

## Learning card (complete after the test)
- We believed that:
- We observed: [result against the threshold, with links to evidence]
- From that we learned:
- Therefore we will: persevere / pivot (type) / run next test / stop
- Assumption status: right / wrong / still unclear
```

```template id="21-mvp-plan" title="MVP plan"
# MVP plan · [Product or bet] · [Date]

**Owner:** [PM]   **Decider:** [Name]   **Time box:** [Start] to [End]

## What we need to learn
- Hypothesis under test:
- Leap-of-faith assumptions: value hypothesis: [ ]; growth or buying-process hypothesis: [ ]
- The decision this MVP informs:

## MVP type and why
Smoke test or fake door / Explainer video / Concierge / Wizard of Oz / Single-feature / Piecemeal / Presale or letter of intent
Why this is the cheapest route to evidence strong enough for the decision:

## Who sees it
| Segment or persona | Number | How recruited | Consent and contract owner informed |
|---|---|---|---|
| | | | |

## Data and security
- Customer data used: none / synthetic only / real (security review reference: [ ])
- What is faked or manual, and who knows:

## Thresholds (set before launch)
- Success: [metric and threshold]
- Kill: [metric and threshold]
- Ambiguous result: [what we'll do]

## What we will deliberately not build
-
-

## After the decision
Destroy / harden and fold into the roadmap / hand to another team. Owner of the clean-up:
```

```template id="21-innovation-accounting-dashboard" title="Innovation accounting dashboard"
# Innovation accounting dashboard · [Bet] · Week of [Date]

**Owner:** [PM]   **Next pivot-or-persevere review:** [Date]

## Milestone status
- [ ] Baseline established (date and source)
- [ ] Tuning the engine (experiments since baseline: [n])
- [ ] Pivot-or-persevere decision due: [date]

## Leading indicators (by cohort, weekly)
| Indicator | Why it's actionable | Cohort | Baseline | Current | Target | Trend |
|---|---|---|---|---|---|---|
| | | | | | | |

## Learning velocity
| Measure | This cycle | Last cycle |
|---|---|---|
| Experiments completed | | |
| Assumptions validated | | |
| Assumptions invalidated | | |
| Still unclear | | |
| Median days from hypothesis to decision | | |
| Cost per validated learning (people-weeks) | | |

## Viability
- Cost per successful outcome (include inference cost for AI products):
- Evidence of willingness to pay (letters of intent, paid pilots):

## Vanity metrics deliberately excluded
- [Metric]: excluded because [it rises regardless of what we change]
-

## What changed our mind this week
[One paragraph, with links to learning cards]
```

```template id="21-design-sprint-plan" title="Design sprint plan"
# Design sprint plan · [Challenge] · [Dates]

**Decider:** [Name]   **Facilitator:** [Name]   **Team (seven or fewer):** [Names and roles]

## Monday: Map
- Long-term goal:
- Sprint questions (what could make us fail?):
  1.
  2.
  3.
- Experts to interview and their slots:
- Target customer and moment on the map:

## Tuesday: Sketch
- Existing ideas to remix (competitors, other teams, other industries):
- Recruiting started: [personas, numbers, screener]

## Wednesday: Decide
- Decision method:
- Storyboard owner:

## Thursday: Prototype
- Fidelity and tool (AI-built allowed):
- What is faked (label on screen):
- Data used: fabricated only, no production data
- Interview script owner:

## Friday: Test
| Persona | Sessions (five per persona) | Interviewer | Observers |
|---|---|---|---|
| | | | |

## Scorecard
| Sprint question | Session 1 | 2 | 3 | 4 | 5 | Pattern |
|---|---|---|---|---|---|---|
| | | | | | | |

## Decision and next experiment
[What the Decider decided, and the experiment card it produced]
```

```template id="21-pivot-or-persevere-review" title="Pivot-or-persevere review"
# Pivot-or-persevere review · [Bet] · [Date]

**Cadence:** every [6 to 8] weeks or once per cycle   **Decider:** [Name]
**Attendees:** product trio, Decider, finance partner, [others]

## Evidence summary
- Dashboard link and milestone status:
- Experiments since last review, with learning cards:
- What moved, and why we think so:
- What didn't move:

## Warning signs
- Are we solving an important problem? Evidence:
- Are early adopters actually adopting? Evidence:
- Does the product deliver what it promises? Evidence:
- Is the team chronically frustrated, with only modest gains from tuning?

## Options
| Option | Pivot type (if any) | What we keep | What changes | Cost | Evidence for |
|---|---|---|---|---|---|
| Persevere | n/a | | | | |
| Pivot | zoom-in / zoom-out / customer segment / customer need / platform / business architecture / value capture / engine of growth / channel / technology | | | | |
| Stop | n/a | | | | |

## Decision
- Decision:
- Rationale (one paragraph):
- What we keep from the past (validated learning carried forward):
- New or revised hypothesis:
- Next milestone and review date:
- Who will be told, and how:
```

```template id="21-double-diamond-brief" title="Double Diamond brief"
# Double Diamond brief · [Challenge] · [Date]

**Owner:** [PM]   **Designer:** [Name]   **Current phase:** Discover / Define / Develop / Deliver

## The request as received
[What the customer or stakeholder asked for, in their words. Treat it as a clue, not a brief.]

## Discover (diverge on the problem)
- People to spend time with (by persona, including the buying group):
- Methods: observation, interviews, data review
- What surprised us:

## Define (converge on the problem)
- Point of view or job story: When [situation], [persona] wants to [motivation], so they can [outcome].
- Problem statement we will design for:
- What we're explicitly not solving:

## Develop (diverge on solutions)
- Options generated (at least five, including "do nothing"):
- Co-design sessions held, and with whom:

## Deliver (converge on a solution)
- Small-scale test and its experiment card:
- What failed and was rejected:
- What will be improved and carried forward:

## Loop-backs
| Date | From phase | Back to phase | Why |
|---|---|---|---|
| | | | |
```

## Prompts

```prompt title="Turn an assumption map into experiment cards"
Goal: Get draft experiment cards for your riskiest assumptions, with honest evidence ratings.
Paste in: the assumption map (or its top-right quadrant), the decision the experiments must inform and any constraints on customer access, budget and time.

Act as an experienced product experimenter working on [product or bet].

For each of the top [three] important, unevidenced assumptions:
1. Restate it as a single falsifiable belief and label it desirability, feasibility, viability or adoptability (will the buying group, security and procurement let it through?).
2. Propose two candidate experiments: the cheapest one that could produce weak evidence, and the cheapest one that could produce strong evidence. For each, state cost, time to result and evidence strength, and say why.
3. Fill in a test card: we believe that, to verify that we will, and measure, we are right if. Propose a threshold, and explain what would make it too easy or too hard.
4. Say which decision the result would change, and what we would do if the result is ambiguous.

Rules: don't count opinions, compliments or synthetic responses as evidence. Prefer behavior and commitment (signatures, payments, security approvals, time spent). Don't invent facts about our customers.

[assumption map]
[decision and constraints]

Check the output: challenge every threshold yourself and agree it with the Decider before the test starts. Reject any experiment whose "strong evidence" is something customers say rather than something they do.
```

```prompt title="Choose the right MVP type"
Goal: Pick the cheapest MVP that answers your riskiest question, and see what you'd skip.
Paste in: the hypothesis, the single riskiest assumption, your persona set and what you can and can't put in front of customers (contract, security and data limits).

For [product or bet], compare these MVP types for testing this assumption: [assumption]. Types: smoke test or fake door, explainer video, concierge, Wizard of Oz, single-feature, piecemeal and presale or letter of intent.

Produce a table with: what the customer would see, what the MVP would actually prove, what it couldn't prove, cost and time, evidence strength, and risks in an enterprise setting (customer data, security review, contract owner disclosure).

Recommend one type and explain why it's the cheapest route to evidence strong enough for this decision: [decision]. Then list what we should deliberately not build.

Check the output: confirm the recommended MVP tests the assumption you named, not an easier neighboring one. If it needs real customer data or production access, take it through security review or choose another type.
```

```prompt title="Build a prototype facade for a sprint or test"
Goal: Get a realistic, clearly fake prototype in hours, ready for five customer sessions.
Paste in: the storyboard or sketches, the target persona and moment, the sprint questions and any design system files. Use fabricated data only.

Build an interactive prototype of [screen or flow] for [persona] at [moment]. It is a facade for customer interviews, not production software.

Requirements:
- Follow the storyboard exactly. Where it is unclear, ask me rather than guess.
- Use realistic but fabricated data. Never use real customer names, hostnames, incidents or credentials.
- Show a small "Prototype" label on every screen.
- Make only the paths in the storyboard work. Other controls can show "Not in this prototype."
- List every place where the prototype fakes behavior the real product would need to earn (for example accuracy, speed or permissions).

Check the output: click through every path in the storyboard yourself before a customer sees it. Confirm no real data appears anywhere, and that the list of faked behaviors is shared with everyone who runs a session.
```

```prompt title="Write a learning card from session notes"
Goal: Turn raw results into a learning card with the evidence attached.
Paste in: the experiment card (with its threshold), session notes or transcripts and any measured results. Use an approved tool for customer recordings and notes.

Using this experiment card and these results for [experiment], write a learning card:
- We believed that: (copy from the card)
- We observed: the result against the threshold, stated plainly, with each observation linked to its source (session ID and timestamp, or data source).
- From that we learned:
- Therefore we will: persevere, pivot (name the type), run a next test or stop, with the reason.
- Assumption status: right, wrong or still unclear.

Rules:
- Don't move the threshold. If the result is near it, say so and mark the assumption still unclear.
- Separate what customers did from what they said, and weight behavior more.
- Quote verbatim inside quotation marks. Don't infer what participants didn't say.
- List any surprises that don't fit the hypothesis.

[experiment card]
[results]

Check the output: open two of the cited sources and confirm them. If the learning card says "right" but the threshold wasn't met, it's wrong.
```

```prompt title="Prepare a pivot-or-persevere review"
Goal: Arrive at the review with the evidence assembled and the options costed, so the meeting is spent deciding.
Paste in: the innovation accounting dashboard, learning cards since the last review, the current hypothesis, and budget and team constraints.

Prepare a pivot-or-persevere review pack for [bet].

1. Summarize what the evidence shows since the last review: what moved, what didn't, and how strong the evidence is.
2. Answer three warning-sign questions with evidence: Are we solving an important problem? Are early adopters actually adopting? Does the product deliver what it promises?
3. Propose options: persevere, at most three pivots (name each type: zoom-in, zoom-out, customer segment, customer need, platform, business architecture, value capture, engine of growth, channel, technology) and stop.
4. For each option, state what validated learning we keep, what changes, the cost and the next milestone.
5. Name the evidence that would most change the recommendation.

Don't make the decision. Don't invent evidence that isn't in the material.

[dashboard]
[learning cards]
[hypothesis and constraints]

Check the output: make sure each pivot keeps real validated learning rather than jumping to an unrelated idea. Remove any option whose evidence is only opinion. The Decider decides.
```

```prompt title="Audit an innovation program for theater"
Goal: Find the activities that look like innovation but produce no decisions.
Paste in: a list of the last quarter's innovation activities (workshops, sprints, hackathons, pilots, prototypes), with any outputs and follow-up actions.

Review these innovation activities for [team or portfolio]. For each, answer:
1. What hypothesis did it test? (Write "none stated" if none.)
2. Was a success threshold set before it started?
3. What evidence did it produce, and how strong was it (weak, medium, strong)?
4. What decision did it change, and who made it?
5. Classify it as learning, preparation or theater, with a one-line reason.

Then list the three changes that would turn the most theater into learning, such as requiring an experiment card before a workshop or a decision owner for every pilot.

Check the output: confirm the classifications with the people who ran the activities before sharing. The goal is to change the system, not to blame a team.
```

## Anti-patterns

:::warn The MVP that is really version 1
The "MVP" took two quarters, has no threshold and was designed to sell. When it underperforms, nobody knows which assumption failed. Write the question and the threshold first, then build the least that answers it.
:::

:::warn Moving the goalposts
The pilot reaches a 41% approval rate against a 60% threshold, and the team decides that 41% is "a strong start." If thresholds move after the data arrives, the experiment was decoration. Set the threshold in advance, record the miss, and decide openly whether to persevere anyway.
:::

:::warn Workshop theater
A two-day design thinking workshop with executives, sticky notes and a photo for the newsletter, and no build, customer or decision. Tie every workshop to an experiment card, a customer and a Decider, or don't hold it.
:::

:::warn One design partner as validation
An enthusiastic champion co-designs the feature, and the team calls the idea validated. One champion is discovery evidence; validation is several customers buying, and passing security review, without the product team in the room.
:::

:::warn Prototypes faster than learning
The PM builds six AI prototypes in a week and tests none of them with a customer against a threshold. Count decisions made per cycle, and spend the time saved on recruiting the right customers.
:::

:::warn The pivot that is really a jump
After a bad quarter the team abandons its product and customers for an unrelated idea and calls it a pivot. Name the pivot type and the learning you're keeping.
:::

## Checklist

- [ ] The bet has a named Decider and a scheduled pivot-or-persevere review date.
- [ ] The team knows which diamond it's in, and hasn't skipped Discover because a customer asked for a feature.
- [ ] Every experiment has a card with a threshold written before the test started, plus its cost, time to result and evidence strength.
- [ ] Assumptions are labeled desirability, feasibility, viability or adoptability, and the riskiest are tested first.
- [ ] Every MVP has a plan naming its type, audience, thresholds, what won't be built and what happens after the decision.
- [ ] The innovation accounting dashboard shows actionable leading indicators by cohort, with a baseline, and lists the vanity metrics excluded.
- [ ] For AI products, cost per successful outcome and model quality thresholds are on the dashboard.
- [ ] Customer discovery covers each member of the buying group separately.
- [ ] Validation claims rest on repeatable behavior (signatures, payments, security approvals), not one champion's enthusiasm.
- [ ] Prototypes shown to customers use fabricated data, are labeled as prototypes and list what they fake.
- [ ] No synthetic or AI-generated response appears as evidence on a learning card.
- [ ] Every experiment ends in a learning card, and every review ends in a recorded decision that names what learning was kept.

## Key takeaways

- In search mode, progress is validated learning. Plan Build-Measure-Learn backwards: decide what to learn, then what to measure, then the least to build.
- An MVP is the fastest route to evidence, not a small first release. Choose the type (fake door, concierge, Wizard of Oz, presale and others) by the riskiest assumption, and in B2B prefer evidence of commitment: letters of intent, paid pilots and passed security reviews.
- Innovation accounting needs actionable leading indicators by cohort and a scheduled pivot-or-persevere review. A pivot changes one hypothesis and keeps the learning; Ries's ten types give you the options.
- Customer development reminds you that search and execution are different jobs. In enterprise products, discover with each member of the buying group and validate with a repeatable sale.
- Design thinking and the Double Diamond are strongest in the problem space. Their critics are right about theater, so tie every design activity to an experiment and a decision.
- AI has made building nearly free. The constraints are now customer attention, clear thresholds and honest measurement of your own speed, and synthetic users never count as evidence.
