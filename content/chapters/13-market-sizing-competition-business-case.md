<p class="lead">Every investment request makes three claims, whether or not anyone writes them down: the market is big enough to matter, we can win our share of it against the real alternatives, and the money comes back on a timeline the company can live with. This chapter turns those claims into a market sizing worksheet, a competitive map and a business case, each built from evidence a finance partner can check.</p>

## Why this matters

Senior PMs lose funding arguments they should win, and win ones they should lose, for the same reason: the numbers in the deck can't be traced back to anything. A TAM slide copied from an analyst report, a competitor grid of green ticks, a revenue line that bends upward in year three. Finance has seen that deck many times and discounts it on sight.

More spreadsheet skill won't fix this. In 2026 an AI harness will build the model, draw the chart and draft the memo in minutes. What it can't do is decide which market boundary is honest, which competitor actually takes your deals, or which assumption deserves the most argument. That judgment is the PM's job, and it's the subject of this chapter.

Three ideas run through everything that follows.

1. **Size from the bottom up and check from the top down.** A market size you can't rebuild from account counts and prices is a guess with a large number attached.
2. **Compete against what the customer would actually do.** In B2B, a large share of lost deals end with the buyer doing nothing, and building in-house is a live option in many categories. Neither appears on most competitor grids.
3. **Make the business case argue about assumptions, not arithmetic.** A case that finance signs shows every assumption, its source and its owner, and points the debate at the two or three assumptions that move the answer.

These artifacts belong to the Market and Business dimensions of your Product 360. They feed strategy (Chapter 03), pricing (Chapter 15), defensibility (Chapter 16) and positioning (Chapter 24).

:::onramp If you've never built a business case
Start with the assumptions register, not the revenue chart. Write down every number the case depends on, where it came from and who owns it. Most of the work, and most of the credibility, lives there.
:::

## Market sizing done right

### TAM, SAM and SOM

TAM, SAM and SOM have no single originator. They are a practitioner convention that spread through venture and startup practice, and teams use them loosely. Use them precisely:

- **Total addressable market (TAM)**: the revenue available if every possible buyer with the job bought a solution like yours. It answers "how big could this ever be?"
- **Serviceable addressable market (SAM)**: the part of TAM your product can actually serve today, given its integrations, geographies, compliance posture, channels and price point. It answers "who could buy this now?"
- **Serviceable obtainable market (SOM)**: the part of SAM you can realistically win in a stated period, given sales and partner capacity, win rates and competition. It answers "what will we actually get?"

The definitions are easy; the boundaries take discipline. Each layer needs a written rule for who is in and who is out, mapped to something real: an integration you have, a region where you can sell, a certification you hold, a channel that reaches the buyer.

:::key SOM is a capacity number
SOM comes from your go-to-market model: reps and partners, their ramp, pipeline per rep, win rate, average contract value and expansion through net revenue retention. "We'll take 5% of a huge market" is a TAM with a hopeful percentage attached.
:::

### Top-down, bottom-up and value-based sizing

There are three ways to size a market, and a defensible number uses at least two.

**Top-down** starts from an industry total, usually an analyst figure, and narrows it with percentages: the share in your regions, the share in your segments, the share that would buy this kind of product. It's fast and useful as a sanity ceiling. It's weak because each narrowing percentage is usually a guess, and the starting figure often measures a different category from the one you're in.

**Bottom-up** counts real accounts that fit your ideal customer profile and multiplies by a realistic annual value per account. For usage-priced products, annual value is units of value consumed times unit price. Bottom-up is slower, but every input can be checked, and it maps to how sales and finance already plan. A sales leader can argue with your account count; nobody can argue with a percentage pulled from the air.

**Value-based** (or job-based) sizing measures what the job costs today, including people's time and the status quo, and then asks what share a product could capture. It follows Clayton Christensen's jobs framing: customers hire a product to make progress, and whatever they spend on that progress now, including their own hours, is the real budget. Value-based sizing is how you size a market that doesn't have an analyst category yet, which in 2026 describes most agentic AI products.

Then **triangulate**. If the top-down and bottom-up numbers land within the same order of magnitude, you have a defensible range. If they don't, one of your assumptions is broken, and finding it is more valuable than either number.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 330" role="img" aria-label="TAM, SAM and SOM as nested boxes, with top-down sizing narrowing from the outside and bottom-up sizing building from account counts">
  <rect x="150" y="20" width="340" height="290" rx="12" class="box"/>
  <rect x="190" y="80" width="260" height="210" rx="10" fill="var(--a2)" fill-opacity=".10" stroke="var(--a2)" stroke-opacity=".6"/>
  <rect x="235" y="150" width="170" height="120" rx="8" fill="var(--a1)" fill-opacity=".16" stroke="var(--a1)" stroke-opacity=".7"/>
  <text x="320" y="44" text-anchor="middle" class="t">TAM: every buyer with the job</text>
  <text x="320" y="62" text-anchor="middle" class="s">Ceiling. Rarely the decision number.</text>
  <text x="320" y="104" text-anchor="middle" class="t" style="fill:var(--a2)">SAM: who we can serve now</text>
  <text x="320" y="122" text-anchor="middle" class="s">Integrations, regions, compliance, channel</text>
  <text x="320" y="196" text-anchor="middle" class="t" style="fill:var(--a1)">SOM: what we win</text>
  <text x="320" y="214" text-anchor="middle" class="s">Reps, partners, win rate,</text>
  <text x="320" y="230" text-anchor="middle" class="s">contract value, expansion</text>
  <text x="320" y="252" text-anchor="middle" class="s">in a stated period</text>
  <line x1="40" y1="40" x2="40" y2="270" class="ln"/>
  <path d="M34 262 L40 276 L46 262" fill="none" stroke="var(--muted)"/>
  <text x="20" y="160" text-anchor="middle" class="s" transform="rotate(-90 20 160)">Top-down: industry total × filters</text>
  <line x1="600" y1="276" x2="600" y2="44" class="ln"/>
  <path d="M594 52 L600 38 L606 52" fill="none" stroke="var(--muted)"/>
  <text x="620" y="160" text-anchor="middle" class="s" transform="rotate(90 620 160)">Bottom-up: accounts × value per account</text>
</svg>
<figcaption>Top-down sizing narrows an industry total with percentages; bottom-up sizing builds from counted accounts and realistic value per account. Use bottom-up for the decision and top-down as the check. SOM is set by go-to-market capacity, not by a share of TAM.</figcaption>
</figure>

### Common sizing errors

Reviewers see the same mistakes again and again. The list below is practitioner consensus rather than the result of a single study, and each error is cheap to avoid.

| Error | What it looks like | The fix |
|---|---|---|
| TAM presented as SAM | "Our market is $40B" when the product integrates with one cloud | Write the SAM boundary rule and size it separately |
| Top-down only | Analyst total times three guessed percentages | Build a bottom-up count and compare |
| SOM as a share | "1% of TAM is still huge" | Derive SOM from reps, partners, win rates and contract value |
| Borrowed category | An analyst category that bundles products you don't compete with | Read the report's definition before using its number |
| Double counting | The same account in the enterprise row and the partner row | Make segments mutually exclusive, and say how |
| Mixed revenue types | One-time services added to recurring subscription value | Size recurring and one-time revenue on separate lines |
| Static unit price | Assuming today's price holds while AI compresses it | Model price per unit of value and its trend |
| Effort in the wrong place | Days on TAM, an hour on SOM | Spend most of the time on SAM and SOM, where decisions are made |

The borrowed-category error is a version of a problem Michael Porter describes in industry analysis: defining the industry too broadly or too narrowly. Porter suggests testing the boundary on two dimensions, product scope and geographic scope. If the competitors, buyers and economics differ across a boundary, it's a different market and deserves its own row.

### Segmentation and the beachhead

A market size is only as useful as its segments. One blended number hides customers who close in six weeks and stay for years behind customers who stall in security review and churn at renewal.

Segment by **trigger and job** first, then by **buying motion**. A trigger is the event that makes a customer start looking: a major outage, an audit finding, a merger, a headcount freeze. The job is the progress they're trying to make. The buying motion is how they buy: direct enterprise sales, partner-led mid-market, self-serve. "Platform teams with more than 50 production services who had a customer-facing outage in the last year" is a segment. "Enterprises in financial services" is a filter.

Christensen and his co-authors add a useful reminder: **nonconsumers** belong in the market. Teams that do the job by hand, or don't do it at all, are often the largest segment, and they're invisible to a top-down number built from vendor revenue.

Geoffrey Moore's *Crossing the Chasm* gives segmentation its strategic purpose. Pick one **beachhead** segment narrow enough to dominate, deliver the whole product that segment needs, win references there and then expand into adjacent segments that share needs and talk to each other, like a row of bowling pins. Moore's point for a sizing exercise is that the beachhead is chosen for winnability and word of mouth, not because it's the biggest row on the sheet.

Each segment gets its own sizing row, competitive set and win rate. If you can't name a segment's main alternative and likely win rate, you don't understand it well enough to size it.

:::leader For product leaders
Insist that every sizing number in a funding request shows its method (top-down, bottom-up or value-based), its sources with dates and a confidence rating. A shared worksheet format across the portfolio lets you compare opportunities on the same terms, and stops each PM from picking the method that produces the biggest number.
:::

## Competitive analysis

### Four layers of competition

Most competitor grids list companies that sell something similar to the same buyer. That's the first of four layers, and in enterprise software it's rarely the one that loses you the most deals.

| Layer | Definition | Examples in B2B | What it tells you |
|---|---|---|---|
| **Direct** | Same category, same buyer | Specialist vendors with a similar product | Feature and price comparisons, battlecards |
| **Indirect** | Different category, same job or same budget | A platform adding your capability as a feature | Bundling risk and procurement pressure |
| **Substitutes** | A different way to do the job | Services firms, in-house tools, a general AI harness wired to company systems | Ceiling on your price, build-versus-buy debates |
| **Do-nothing** | Status quo, delay or indecision | Existing people and processes, "not this year" | Often your largest source of lost deals |

Porter treats substitutes as one of the five forces and counts doing without and doing it yourself as substitutes. He also notes that substitutes are "always present, but they are easy to overlook." In 2026 the do-it-yourself option has become much stronger: a customer's platform team can connect a general-purpose AI harness to its own systems through connectors and assemble a good-enough version of many narrow products.

The do-nothing layer is the one with hard numbers behind it. Matthew Dixon and Ted McKenna, in *The JOLT Effect*, analyzed about 2.5 million recorded sales conversations and report that 40 to 60% of lost deals ended in no decision rather than a loss to a competitor. Their prescription for sellers has four steps: judge the level of the buyer's indecision, offer a clear recommendation, limit the exploration so the buyer isn't drowning in options, and take risk off the table. Each step has a product counterpart: sensible defaults, a recommended starting configuration, fewer packaging choices and a pilot that can be reversed.

April Dunford, in *Obviously Awesome*, makes the same point from the positioning side. Start competitive work by asking what customers would do if your product didn't exist. Your unique attributes only count relative to those alternatives, and for many products the honest answer is "keep doing what they do now." Chapter 24 builds positioning on that answer.

:::key Put do-nothing on every map
If the status quo isn't on your competitive landscape, battlecard and win/loss taxonomy, you're analyzing the deals you lost to vendors and ignoring the pile, often just as large, that you lost to inertia.
:::

### Porter's Five Forces as a lens

Porter's Five Forces, first published in HBR in 1979 and updated in 2008, explains how industry structure splits the value a product creates among rivals, buyers, suppliers, new entrants and substitutes. The five forces are rivalry among existing competitors, the threat of new entrants, the bargaining power of buyers, the bargaining power of suppliers and the threat of substitutes. Porter's broader point is that competition for profit reaches well beyond the rivals you name in a deal.

A PM should use the forces to explain margin and pricing power. Two of Porter's own warnings are the most useful:

- **Factors are not forces.** Industry growth, technology, government policy and complementary products matter, but they aren't extra forces. Trace their effect through the five. Fast market growth, for example, can soften rivalry for a while and also attract new entrants.
- **Analysis beats lists.** Porter's common pitfalls include defining the industry too broadly or too narrowly, listing factors instead of analyzing them, giving every force equal weight, confusing an effect such as price sensitivity with its cause in the buyer's economics, treating the analysis as static, mistaking cyclical change for structural change and using the framework to label an industry good or bad instead of using it to guide choices.

For AI products in 2026, two forces deserve fresh attention. **Supplier power** now includes model providers, because inference cost sets gross margin, and a price change by a model provider flows straight into your unit economics. **Substitutes** include the general-purpose AI harness with connectors, which lets a buyer assemble a narrow agent without buying one. If those two forces are strong in your market, your pricing model and your evidence of reliability matter more than your feature list. Chapter 16 takes this further into moats.

### The competitive landscape map

A landscape map plots the alternatives on two axes. The rule that makes it useful: **choose axes that buyers actually decide on**, not axes chosen because they put you in the top-right corner. Good axes come from win/loss interviews and buyers' requirement lists. Typical examples are breadth of integration against depth of automation, or time to value against configurability.

Plot all four layers, including in-house builds and the status quo, which usually sit in a revealing position. Use bubble size for a third dimension, such as installed base, only when you have a source for it. Date-stamp the map, because a landscape older than two quarters in an AI category is already stale.

### Competitor profiles and battlecards

A **competitor profile** is the reference document for one alternative. It covers who they are, whom they target, their product and roadmap signals, pricing and packaging, go-to-market and partners, strengths and weaknesses, where they win against you and where you win, and their likely next move. Every factual line carries a source and a last-verified date, and the profile has a confidence rating. Product, marketing and leadership use profiles for strategy.

A **battlecard** is the sales-facing summary for one competitive situation, one page long. Most competitive intelligence teams converge on a similar set of sections: why we win (three points with proof), their pitch in their own words, landmines (questions that expose their gaps), objection handling, pricing guidance, customer proof and a "do not say" list of claims you can't prove. Three rules keep battlecards honest:

1. Every claim traces to a source someone has checked.
2. No disparagement. It costs sellers credibility with the buyer, and false claims about a competitor can create legal exposure.
3. Refresh on a cadence, and show the owner and last-updated date on the card.

Write a battlecard against do-nothing too. It's the one sellers need most and the one teams most often forget to write. Chapter 27 covers how to roll battlecards out to the field.

### Win/loss analysis

Win/loss analysis supplies the evidence for everything else in this section. Without it, your landscape map and battlecards reflect what the team believes about competitors rather than what buyers experienced.

Clozd, a win/loss vendor, summarizes the program design that works: an executive sponsor, an ongoing program rather than a one-time project, a neutral interviewer (buyers are polite to the vendor who lost and candid with a third party), interviews over surveys, and a balanced sample of wins and losses that mirrors the pipeline, stratified by segment and deal size.

PMs should add four things:

- **Include no-decisions and churn.** A sample of only wins and competitive losses misses the biggest category.
- **Code reasons into a stable taxonomy**, such as product gap, price, trust or risk, timing, relationship, competitor strength and status quo. Keep the codes stable for at least a year so trends mean something.
- **Separate stated reasons from evidence.** "Price" is an easy reason for a buyer to give and often not the whole story. Check stated reasons against call recordings and CRM history.
- **Report themes with counts and short quotes**, then route each theme to an owner in product, marketing or sales, with a date to report back. Themes with no owner tend to reappear in next quarter's report unchanged.

## The business case finance signs

### What finance is checking

A finance partner reading your case asks four questions. Are the assumptions sourced and owned? Does the case include doing nothing and a cheaper option? How bad is the downside, and how likely? Will we know early if it's going wrong?

A case that finance signs runs in a predictable order: decision requested, problem and opportunity, options (always including do nothing), recommendation, assumptions register, financial summary, scenarios, sensitivity, risks, milestones with kill criteria and the ask. The business case template in this chapter follows that order.

### Assumptions, scenarios and sensitivity

The **assumptions register** is the heart of the case: each assumption with its value, source, confidence, owner and test. When the meeting turns into an argument about a number, the register shows which assumption is in question and who can settle it.

**Scenarios** and **sensitivity** are different tools, and good cases use both.

- A **scenario** changes several linked assumptions together to tell a coherent story. In a downside scenario, adoption is slower, so expansion is slower, and price discounts are deeper because the product is less proven. Show three: downside, base and upside.
- **Sensitivity** flexes one assumption at a time, across a plausible range, to find which ones move the answer most. Present it as a ranked list, with the most influential assumption at the top (the tornado ordering). The two or three assumptions at the top of that list are where the meeting should spend its time, and where your validation plan should spend its money.

### Decision analytics without the spreadsheet

Behind every business case sits a small decision model, and the PM owns its logic. That logic answers three kinds of question, and each needs different evidence:

- **What has happened?** Descriptive questions: current ARR by segment, win rate by competitor, cost per unit of value today. The evidence is your own systems of record (CRM, billing, telemetry), and the risk is a definition mismatch, such as two teams counting "customer" differently.
- **What is likely to happen?** Predictive questions: adoption curve, ramp, churn, price trend. The evidence is history plus the outside view, and the answer should always be a range, never a single line.
- **What should we do?** Prescriptive questions: which option, which segment first, how much to invest given limited engineers, sellers and budget. The model chooses among options under constraints you state, and the constraints are where most of the argument belongs.

Build the model as a **driver tree**: the outcome finance cares about (NPV, ARR, gross margin) at the top, broken into the operational drivers that produce it (accounts, adoption, units of value per account, price, cost per unit, headcount). Every leaf of the tree is a row in the assumptions register. When you ask a harness to build the model, give it the tree and the register, ask it to show which leaves each output depends on, and check one period by hand with FP&A. The mechanics belong to the harness and to finance; the structure, the constraints and the evidence for each leaf belong to you. Chapters 17 to 19 go deeper on asking the right questions of your data and checking the harness's answers.

### NPV, payback and the hurdle rate

Amy Gallo's HBR refresher on net present value states the principle simply: money you hold now is worth more than money you collect later, because it can be invested in the meantime. Net present value (NPV) discounts future cash flows back to today at a discount rate and subtracts the investment. A positive NPV at the company's hurdle rate means the project creates value on paper. Chapter 12 works through the discounted cash flow view in more detail.

Two practical rules:

- **Don't pick the discount rate yourself.** The hurdle rate is finance's call. Ask FP&A for it, and use theirs.
- **Show payback alongside NPV.** Executives like payback period (how long until cumulative cash in exceeds cash out) because it's simple. It's also blind to everything after the payback date and to the time value of money. Showing both stops a fast-payback, low-value project from beating a slower, much more valuable one.

### The outside view and the fat tail

Daniel Kahneman and Dan Lovallo distinguish the **inside view**, which forecasts from the details of this project, from the **outside view**, which starts from how similar projects actually turned out. The inside view is reliably optimistic. Their remedy is to anchor on the outside view first. Bent Flyvbjerg turned it into a practical method for project planning, **reference class forecasting**, in three steps: pick a class of comparable past projects, find the distribution of their outcomes and position your project within it.

For software investments, the reference class is sobering. Flyvbjerg and Alexander Budzier studied 1,471 IT projects and found an average cost overrun of 27%. The average hides a fat tail: about one project in six was what they called a black swan, with an average cost overrun of 200% and a schedule overrun of almost 70%. For your business case, the lesson is that the downside scenario must be genuinely bad, and the risks section must name what would put this project in the tail.

Gary Klein's **premortem** is the fastest way to fill that risks section. Before approval, the team imagines that the project has failed badly and writes down every reason why. Klein's reasoning is that treating failure as already certain makes it easier for people to name risks they would otherwise keep to themselves.

### Working with FP&A

Bring financial planning and analysis (FP&A) in before the model is final, not after. In the first conversation, agree on:

- **The driver tree**: which operational drivers produce revenue and cost, and how they connect.
- **The discount rate and the time horizon**.
- **Cost allocation rules**: how shared engineering, inference, support and hosting are charged to the initiative.
- **Revenue recognition**: especially for usage-based or outcome-based pricing, where when revenue counts may differ from when the customer pays.

Then divide the work: FP&A owns the model's mechanics and the company's conventions, and you own the assumptions and their evidence. After launch, track actuals against the case and report the gap honestly. A PM whose last case was tracked and roughly right gets the next one approved faster.

## How to apply it

Here's a four-week method for taking a significant investment (a new product, a new segment or a pricing change) from idea to a signed business case. It assumes you already have a tested product hypothesis (Chapter 01).

**Week 1: Frame the market.**

1. Write the decision you need in one sentence: what you're asking for, from whom and by when.
2. Define segments by trigger, job and buying motion. Make them mutually exclusive and write the rule that separates them.
3. Draft the bottom-up sizing worksheet: account counts per segment, annual value per account and the basis for each, with a source, date and confidence for every input. Ask the harness to draft it with cited inputs, then verify every number yourself.
4. Run a top-down check and a value-based check. If the methods disagree by more than an order of magnitude, find the broken assumption before going further.
5. Write the SAM boundary rule and the SOM capacity logic (reps, partners, ramp, win rate, contract value, net revenue retention).

**Week 2: Map the competition.**

6. List alternatives in all four layers: direct, indirect, substitutes and do-nothing. For each segment, name the main alternative.
7. Run a Five Forces pass focused on the two or three strongest forces and what they mean for margin and pricing power.
8. Pull the last two quarters of win/loss evidence: interview notes, CRM reasons and call recordings. Code the reasons into your taxonomy, including no-decisions.
9. Draw the landscape map on axes taken from buyers' requirements. Write or refresh profiles for the top three alternatives and battlecards for the top two, including do-nothing.

**Week 3: Build the case with FP&A.**

10. Meet FP&A. Agree on the driver tree, discount rate, horizon, cost allocation and revenue recognition.
11. Fill the assumptions register. Every assumption gets a source, confidence and owner.
12. Ask for the reference class: how did comparable past launches at your company actually perform against their cases? Set the base case from the outside view and adjust.
13. Run three scenarios and a one-at-a-time sensitivity. Rank the assumptions by how much they move NPV.
14. Run a premortem with the team and turn its output into the risks section.

**Week 4: Decide.**

15. Write the case in the standard order, with the recommendation first. Put the ranked sensitivity on the first page.
16. Set milestones and kill criteria tied to the top-ranked assumptions: "If diagnosis acceptance is below X by month six, we stop expansion spend."
17. Pre-wire the decision with finance, sales and your manager before the review meeting.
18. After approval, log the decision (Chapter 29) and schedule the first actuals-against-case review.

Keep the competitive work running after approval. Monthly win/loss interviews, competitor monitoring and battlecard refreshes give the earliest warning that a top-ranked assumption is failing.

## The AI lens

### When the product is AI-powered

AI products change the inputs to all three artifacts.

- **Value per unit, not per seat.** AI products increasingly charge per unit of work: per resolved ticket, per document, per task. Size the market by units of value (incidents, claims, contracts) times a unit price, and model how that price is likely to fall as competitors and model costs shift. A seat-based sizing of an agent product overstates the market if the agent reduces the seats.
- **Inference cost in the case.** For AI features, cost of goods sold includes inference, which scales with usage and changes with model choice and provider pricing. The business case needs inference cost per unit of value, its trend and a sensitivity line for it. Chapter 31 covers how to engineer that cost down; Chapter 15 covers pricing to cover it.
- **Supplier power and substitutes.** Run the Five Forces pass with model providers as suppliers and general-purpose AI harnesses as substitutes. Ask, explicitly, what stops a customer's platform team from assembling a good-enough version in-house, and put the answer in the competitive map.
- **Claims discipline.** In March 2024 the US Securities and Exchange Commission brought its first "AI washing" actions, settling with two investment advisers, Delphia and Global Predictions, for $400,000 in combined penalties over false claims about their use of AI. It's a reminder that AI marketing claims can be false. Verify competitors' AI claims before you react to them, and keep unprovable AI claims off your own battlecards.
- **Trust as a competitive dimension.** For AI products that act, buyers weigh reliability, audit trails and human control alongside features. Put trust on the landscape map and in the win/loss taxonomy.

### Doing the work with AI

Desk research is the part of this chapter that AI has changed most. Deep research agents became widely available in 2025: OpenAI announced deep research in February, and Anthropic launched Research in Claude in April, running multiple searches that build on each other across the web and connected workspace data, and returning citations. Since Anthropic introduced the Model Context Protocol in November 2024 as an open standard for connecting assistants to data sources and tools, a harness can also read your CRM, call recordings, win/loss notes and documents through connectors. Competitive intelligence vendors followed: Klue launched an agent in June 2025 that pulls from the open web, recorded sales calls, win/loss interviews and internal files to keep competitor profiles current and flag rivals in live deals.

So the harness can now do in hours what took an analyst days: gather public sources (filings, pricing pages, release notes, job posts, reviews) into an evidence table, draft sizing worksheets, profiles and battlecards with a cited source for each input, code win/loss transcripts against your taxonomy, and monitor competitors on a schedule.

The work has shifted from collecting to verifying, and verification is where AI research is weakest. In a March 2025 study, Klaudia Jaźwińska and Aisvarya Chandrasekar at Columbia Journalism Review's Tow Center tested eight generative search tools on 1,600 queries and found they answered more than 60% incorrectly, with error rates ranging from 37% for the best tool to 94% for the worst. ChatGPT, for example, signaled low confidence in only 15 of 200 responses and never declined to answer. Their test was about citing news articles, not market research, but the failure modes carry over: confident answers, wrong or missing citations, and weak separation of authoritative sources from rumor. Harnesses are also unreliable at counting (account counts are exactly what bottom-up sizing needs) and at staying inside your category definition.

Use this verification protocol for every AI-assisted market or competitive artifact:

1. **Evidence before narrative.** Ask for the evidence table first: claim, number, source URL, publication date, the exact quote and the source's definition of the category. Read the table before you ask for prose.
2. **Open the source.** For every number that will reach a decision, open the cited source and confirm the number, its date and its definition. A citation that doesn't contain the claim is a fabricated citation, however plausible it looks.
3. **Tag what you can't verify.** Anything without a primary source gets an [Unverified] tag or comes out.
4. **Triangulate counts.** Check any account count or market figure with a second method or a second independent source.
5. **Human gate for the field.** No competitor claim goes on a battlecard until a person has verified it on a primary source and dated it.
6. **Sample the coding.** When the harness codes win/loss transcripts, a person checks a random sample of at least ten against the transcripts and corrects the taxonomy before the counts are used.

:::ai The one-line rule
Let the harness collect, draft and monitor. A person verifies every number and every competitor claim on a primary source before it reaches a decision or a seller.
:::

Treat customer data with the same care as in any other analysis. Call recordings and win/loss interviews contain customer names and commercial terms, so use only harnesses and connectors your company has approved for that data.

## The Beacon case: sizing Beacon Agents and building the case

:::example The decision on the table
Northlight's leadership wants to launch Beacon Agents at Northlight Live and move pricing from per-environment to per-resolved-incident. The CFO has asked for a business case before committing engineering and go-to-market investment for the next two years. You have four weeks. All sizing and financial figures below are illustrative, built for this worked example; only the company facts (ARR, growth, customers, NRR and gross margin) come from Beacon's record.
:::

**Sizing: the SAM fork.** Beacon has about 420 enterprise customers and about $48M in ARR, so the average customer pays roughly $114K a year. The harness first offers a top-down figure for the broad AIOps category. You reject it as the decision number because that category bundles observability platforms with agent products, and Beacon competes with only part of it.

You build bottom-up instead, with value per account calculated as resolved incidents per year times a target price per resolved incident. The worksheet exposes the strategic tension in Beacon's strategy: build on Northlight Observe data, or stay tool-agnostic.

| Segment (illustrative) | Accounts | Annual value per account | Segment value | In SAM if Observe-only? | In SAM if tool-agnostic? |
|---|---|---|---|---|---|
| Enterprise on Northlight Observe | 1,100 | $225K | about $250M | Yes | Yes |
| Enterprise on other observability stacks | 5,000 | $225K | about $1.1B | No | Yes, through connectors and MCP servers |
| Mid-market served by MSP partners | 12,000 end customers | $30K | about $360M | No | Yes, if multi-tenant billing ships |

An Observe-only SAM is about $250M. A tool-agnostic SAM is about $1.7B, roughly seven times larger. The worksheet makes the trade concrete: the larger SAM comes with lower win rates against incumbent platforms, more integration work and a dependency on the multi-tenant features Leo, the MSP operations manager, needs.

**SOM from capacity.** Rather than claim a share of $1.7B, you build SOM from the go-to-market model: the number of enterprise reps and their ramp, partner-sourced pipeline from MSPs, win rates by segment from last year's CRM data and expansion through Beacon's 118% NRR. The capacity model lands at a three-year ARR range that brackets the roughly $126M that Beacon would reach if its 38% growth simply continued for three years. That agreement is the useful signal: the plan depends on sustaining today's growth, which the team has already shown it can do, and on no sudden leap in market share.

**The competitive map.** You draw all four layers:

- **Direct**: startups building ops agents.
- **Indirect**: AIOps features in large observability platforms, and incident-management tools adding AI.
- **Substitutes**: a general AI harness that a customer's platform team connects to its own tools through MCP connectors, plus in-house scripts.
- **Do-nothing**: humans plus runbooks plus chat, which is the main alternative for most prospects.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 360" role="img" aria-label="Beacon competitive landscape: breadth of tool coverage against depth of action">
  <line x1="80" y1="310" x2="610" y2="310" class="ln"/>
  <line x1="80" y1="310" x2="80" y2="30" class="ln"/>
  <text x="345" y="340" text-anchor="middle" class="s">Breadth of tool coverage: single platform → tool-agnostic</text>
  <text x="30" y="170" text-anchor="middle" class="s" transform="rotate(-90 30 170)">Depth of action: summarize → diagnose → act</text>
  <text x="70" y="295" text-anchor="end" class="s">Summarize</text>
  <text x="70" y="200" text-anchor="end" class="s">Diagnose</text>
  <text x="70" y="105" text-anchor="end" class="s">Act</text>
  <circle cx="170" cy="230" r="34" fill="var(--a2)" fill-opacity=".16" stroke="var(--a2)"/>
  <text x="170" y="226" text-anchor="middle" class="s">Observability</text>
  <text x="170" y="240" text-anchor="middle" class="s">platform AIOps</text>
  <circle cx="400" cy="250" r="28" fill="var(--a2)" fill-opacity=".16" stroke="var(--a2)"/>
  <text x="400" y="246" text-anchor="middle" class="s">Incident tools</text>
  <text x="400" y="260" text-anchor="middle" class="s">adding AI</text>
  <circle cx="330" cy="110" r="26" fill="var(--a3)" fill-opacity=".16" stroke="var(--a3)"/>
  <text x="330" y="106" text-anchor="middle" class="s">Ops-agent</text>
  <text x="330" y="120" text-anchor="middle" class="s">startups</text>
  <circle cx="540" cy="150" r="28" fill="var(--surface-2)" stroke="var(--border-2)" stroke-dasharray="4 3"/>
  <text x="540" y="146" text-anchor="middle" class="s">DIY harness</text>
  <text x="540" y="160" text-anchor="middle" class="s">+ connectors</text>
  <rect x="455" y="268" width="140" height="34" rx="8" fill="var(--surface-2)" stroke="var(--border-2)" stroke-dasharray="4 3"/>
  <text x="525" y="289" text-anchor="middle" class="s">Do nothing: people + runbooks</text>
  <circle cx="480" cy="80" r="30" fill="var(--a1)" fill-opacity=".2" stroke="var(--a1)"/>
  <text x="480" y="78" text-anchor="middle" class="t" style="fill:var(--a1)">Beacon</text>
  <text x="480" y="94" text-anchor="middle" class="s">Agents</text>
</svg>
<figcaption>An illustrative landscape for Beacon Agents, dated to the quarter it was drawn. The axes come from buyers' requirement lists. Dashed shapes are substitutes and the status quo, which most competitor grids leave out. Positions are judgments to be tested in win/loss interviews, not measurements.</figcaption>
</figure>

**Five Forces.** The analysis points at two forces. **Supplier power** is rising: inference cost from model providers is why Beacon's gross margin fell from 81% to 72% after agentic features launched. **Substitutes** are strong: a capable platform team can wire a general harness to its observability and ticketing tools. Buyer power is also high, because platforms bundle AI features and Marcus, the VP of IT Operations, needs an ROI story for his CFO. The lesson for the case is that per-resolved-incident pricing and evals-backed trust matter more than another integration.

**Win/loss.** The harness codes a quarter of loss interviews and CRM notes against the taxonomy, and a person checks a sample. In mid-market, **no decision** is the top loss reason: buyers liked the demo and stayed with runbooks and chat. In enterprise, the hallucinated root cause that led a customer to roll back the wrong service shows up as a **trust** objection in several losses. The do-nothing battlecard applies the JOLT steps: recommend Correlate and Diagnose as the starting point, limit the options and take risk off the table with allowlisted low-risk actions and a human approval gate. The battlecard against observability platforms leads with tool-agnostic coverage, cited evidence for every diagnosis and the audit log that Sam, the security reviewer, requires. Its "do not say" list bans any MTTR claim not backed by a named, referenceable customer.

**The business case.** With FP&A, you agree on how inference cost is allocated and how per-resolved-incident revenue is recognized. The assumptions register has twelve entries; four matter most:

| ID | Assumption | Why it matters |
|---|---|---|
| A1 | Diagnosis acceptance rate in production | Drives resolved incidents, and so revenue under the new price |
| A2 | Inference cost per resolved incident | Drives gross margin, already down to 72% |
| A3 | Autonomous resolution rate for allowlisted actions | Drives the headcount leverage Marcus needs for his ROI story |
| A4 | Share of Beacon Classic customers who migrate | Drives near-term revenue and support cost |

The sensitivity ranking puts **inference cost per incident** and **diagnosis acceptance rate** at the top: each moves NPV more than the next three assumptions combined in the illustrative model. For the outside view, you ask FP&A for the actual-against-plan record of Northlight's past launches in Observe and Desk, and you apply the Flyvbjerg fat-tail warning to the connector and integration work, which is the part most likely to run long. The downside scenario assumes integration takes twice as long as planned.

The case goes to the CFO recommending two stages. Stage one funds Correlate and Diagnose on per-resolved-incident pricing for existing customers. Stage two, the tool-agnostic expansion, is released only if diagnosis acceptance and inference cost per incident hit their milestones by month six. The kill criteria are the same two assumptions that top the sensitivity ranking.

## Product 360 artifacts

```template id="13-market-sizing-worksheet" title="Market sizing worksheet"
# Market sizing worksheet · [Product or opportunity] · v[n] · [Date]

**Owner:** [PM]   **Reviewed with:** [FP&A, sales ops]   **Period for SOM:** [e.g., 3 years]

## Value unit
Annual value per account = [units of value per year, e.g., resolved incidents, documents, seats] × [price per unit]
Basis for price: [current price list / pricing research / comparable products]
Expected price trend: [flat / falling by about x% a year because ...]

## Segments (mutually exclusive)
| Segment | Definition (trigger, job, firmographic filters) | Buying motion | Account count | Source and date | Confidence (H/M/L) | Annual value per account | Basis for value | Segment value | In SAM? (Y/N and why) | Reachable in period |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

Rule that keeps segments from overlapping: [describe]

## Totals
| Layer | Value | Boundary rule | What would have to be true |
|---|---|---|---|
| TAM | | Every buyer with the job | |
| SAM | | [integrations, regions, compliance, channel] | |
| SOM | | From the capacity model below | |

## SOM capacity model
| Driver | Value | Source | Owner |
|---|---|---|---|
| Quota-carrying reps (by year) | | | |
| Ramp time | | | |
| Partner-sourced pipeline | | | |
| Win rate by segment | | | |
| Average first-year contract value | | | |
| Net revenue retention | | | |

## Cross-checks
- Top-down check: [industry total, source, category definition, filters] → [value]
- Value-based check: [cost of the job today, including people time] → [value]
- Do the methods agree within an order of magnitude? [Yes / No: the broken assumption is ...]

## Excluded on purpose
[Segments, regions or revenue types left out, and why]
```

```template id="13-competitive-landscape" title="Competitive landscape"
# Competitive landscape · [Product] · [Segment] · [Quarter]

**Owner:** [PM or PMM]   **Last verified:** [Date]   **Next refresh:** [Date]

## The question customers are answering
"What would we do if [product] didn't exist?" Most common answer in win/loss: [answer]

## Alternatives by layer
| Layer | Alternative | Who chooses it | Why they choose it | Our win rate against it | Evidence |
|---|---|---|---|---|---|
| Direct | | | | | |
| Indirect | | | | | |
| Substitute (including build in-house) | | | | | |
| Do-nothing | Status quo / delay | | | | |

## Map axes
- X axis: [buying criterion] · Source: [win/loss, RFPs, requirement lists]
- Y axis: [buying criterion] · Source:
- Bubble size (only if sourced): [measure and source]

## Five Forces summary
| Force | Strength (H/M/L) | Evidence | Effect on our margin or pricing power |
|---|---|---|---|
| Rivalry | | | |
| New entrants | | | |
| Buyer power | | | |
| Supplier power (including model providers) | | | |
| Substitutes (including DIY AI harness) | | | |

Strongest two forces and what we do about them:
1.
2.

## What changed since the last version
-
```

```template id="13-competitor-profile" title="Competitor profile"
# Competitor profile · [Alternative] · [Date]

**Owner:** [PM or PMM]   **Last verified:** [Date]   **Confidence:** H / M / L

## Snapshot
| Field | Detail | Source and date |
|---|---|---|
| Who they are | | |
| Size (revenue, funding or segment revenue) | | |
| Target customers and segments | | |
| Go-to-market and partners | | |

## Product and roadmap signals
| Date | Signal (release, pricing change, hiring, partnership) | Source | What it suggests |
|---|---|---|---|
| | | | |

## Pricing and packaging
[Model, tiers, published prices, discount patterns. Mark anything from deal hearsay as unverified.]

## Strengths and weaknesses (from buyers' point of view)
| Strengths | Evidence | Weaknesses | Evidence |
|---|---|---|---|
| | | | |

## Head to head
- Where they win against us (segments, situations):
- Where we win against them:
- Our win rate against them, last four quarters:

## AI claims check
| Claim they make | Verified? (Y/N/partly) | How verified |
|---|---|---|
| | | |

## Likely next move
[Prediction, with reasoning and confidence]

## Sources
[List with URLs and access dates]
```

```template id="13-battlecard" title="Battlecard"
# Battlecard · [Us] vs [Alternative] · [Segment]

**Owner:** [PMM]   **Last updated:** [Date]   **Review cadence:** monthly

## When you'll meet them
[Deal signals that this alternative is in play]

## Why we win (three points, each with proof)
1. [Point] · Proof: [customer, metric or demo]
2.
3.

## Their pitch, in their words
[Summary of how they position, from their own materials]

## Landmines to set (questions that expose real gaps)
- "[Question for the buyer]"
-

## Objection handling
| Objection | Response | Proof |
|---|---|---|
| | | |

## Quick dismisses
- [Misconception] → [one-line correction with source]

## Pricing guidance
[How they price, typical discounting, how to position our price]

## Customer proof
[References and logos cleared for use]

## Do not say
- [Claims we can't prove, including unverified AI or performance claims]
- Never disparage the competitor.

## Sources
[Each claim's source and verification date]
```

```template id="13-do-nothing-battlecard" title="Do-nothing battlecard"
# Battlecard · [Us] vs doing nothing · [Segment]

**Owner:** [PMM]   **Last updated:** [Date]

## How the status quo shows up
[Signals: "not this quarter," endless evaluation, more stakeholders added late]

## Cost of doing nothing (buyer's numbers, not ours)
[What the job costs today in time, risk and money, with the buyer's own figures where possible]

## Judge the indecision
Questions to find out whether the buyer is stuck on fear of a wrong choice:
-

## Offer a recommendation
[The single starting configuration we recommend for this segment, and why]

## Limit the exploration
[What we will not ask them to evaluate now]

## Take risk off the table
[Pilot terms, reversibility, controls, approval gates, references]

## Proof
[Customers who moved from the same status quo, with outcomes they'll confirm]
```

```template id="13-win-loss-analysis" title="Win/loss analysis"
# Win/loss analysis · [Product] · [Period]

**Sponsor:** [Executive]   **Interviewer:** [Neutral third party / internal non-sales]   **Owner:** [PM]

## Sample
| Segment | Wins | Losses to competitor | No decision | Churned | Interviews completed | Deals in period |
|---|---|---|---|---|---|---|
| | | | | | | |

Sample matches pipeline mix? [Yes / No: gaps are ...]

## Win rate trend
[By quarter and segment, from CRM]

## Reason taxonomy (stable codes)
Product gap · Price · Trust or risk · Timing · Relationship · Competitor strength · Status quo · Other

## Top reasons won
| Code | Count | Short buyer quote or paraphrase | Evidence beyond the interview |
|---|---|---|---|
| | | | |

## Top reasons lost (including no decision)
| Code | Count | Short buyer quote or paraphrase | Stated reason vs evidence |
|---|---|---|---|
| | | | |

## Competitor-specific patterns
-

## No-decision patterns
-

## Implications and actions
| Theme | Product | Positioning | Sales | Owner | Due |
|---|---|---|---|---|---|
| | | | | | |

## Coding quality
AI-assisted coding? [Y/N] · Sample checked by a person: [n of N] · Corrections made:
```

```template id="13-business-case" title="Business case"
# Business case · [Initiative] · v[n] · [Date]

**Owner:** [PM]   **Finance partner:** [FP&A]   **Decision maker:** [Name]   **Decision needed by:** [Date]

## 1. Decision requested
[One sentence: what, how much, by when]

## 2. Problem and opportunity
[The customer problem, the evidence and the market size (link the sizing worksheet)]

## 3. Options considered
| Option | Cost | Expected benefit | Why not chosen |
|---|---|---|---|
| Do nothing | | | |
| Smaller option | | | |
| Recommended option | | | |

## 4. Assumptions register
| ID | Assumption | Value | Source or evidence | Confidence (H/M/L) | Owner | How we'll test it | Date |
|---|---|---|---|---|---|---|---|
| A1 | | | | | | | |

## 5. Financial summary (base case)
| Item | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Revenue | | | |
| Cost of goods sold (including inference) | | | |
| Gross margin | | | |
| Investment (people, vendors, go-to-market) | | | |
| Net cash flow | | | |

NPV at finance's hurdle rate of [x%]: [value]   Payback: [months]   IRR (if finance uses it): [value]

## 6. Scenarios
| | Downside | Base | Upside |
|---|---|---|---|
| Story in one line | | | |
| Key assumption values | | | |
| NPV | | | |
| Payback | | | |

Outside view: reference class used [past launches], their actual-against-plan record [summary], and how the base case was adjusted.

## 7. Sensitivity (ranked)
| Rank | Assumption | Range tested | NPV swing |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## 8. Risks and mitigations (from the premortem)
| Risk | Likelihood | Impact | Mitigation | Early signal |
|---|---|---|---|---|
| | | | | |

## 9. Milestones and kill criteria
| Milestone | Date | Metric and threshold | If missed |
|---|---|---|---|
| | | | |

## 10. Agreements with FP&A
Driver tree · Discount rate and horizon · Cost allocation · Revenue recognition

## 11. Ask
[People, money, time, and the first review date for actuals against this case]
```

## Prompts

```prompt title="Draft a bottom-up market sizing worksheet with cited inputs"
Goal: Get a first bottom-up sizing that you can check line by line.
Paste in: your product description, value unit and price, segment definitions, and any internal data on account counts and contract values (CRM exports need an approved tool).

Build a bottom-up market sizing worksheet for [product] using these segments: [segments].

For each segment give: the definition (trigger, job, firmographic filters), an account count, the source and its date, a confidence rating (H/M/L), the annual value per account and its basis, and whether it falls inside our SAM given these constraints: [integrations, regions, compliance, channels].

Rules:
- Produce the evidence table first: every number with its source URL, publication date, the exact passage it came from and the source's definition of the category. Then the worksheet.
- If you can't find a primary source for a count, write "No source found" and give your estimate separately, labeled as an estimate with your reasoning.
- Make the segments mutually exclusive and say how.
- Then run a top-down check from an industry total and report whether the two methods agree within an order of magnitude. If they don't, name the assumption most likely to be wrong.

Check the output: open every source for the three largest segment values and confirm the number, date and definition. Recount anything the model counted itself. Reject any figure whose source doesn't contain it.
```

```prompt title="Build SOM from go-to-market capacity"
Goal: Replace "x% of the market" with a capacity-based SOM.
Paste in: rep headcount plan, ramp time, pipeline per rep, partner-sourced pipeline, win rates by segment, average contract value and net revenue retention. Use an approved tool for internal sales data.

Using these go-to-market inputs for [product], estimate the serviceable obtainable market over [period].

1. Show the driver tree from reps and partners to new ARR and expansion ARR, year by year.
2. State every assumption and its source from what I provided. Don't introduce new numbers without labeling them as your assumptions.
3. Compare the result with the SAM of [value] and with what our current growth rate of [x%] would produce if it held. Explain any gap.
4. Name the two inputs that move SOM most, and the range for each that would change the decision.

Check the output: confirm the arithmetic on one year by hand or with FP&A. If SOM is more than a small fraction of SAM in the first period, ask what capacity would have to exist to deliver it.
```

```prompt title="Map the four layers of competition"
Goal: See every alternative a buyer weighs, including doing nothing.
Paste in: product description, target segments, win/loss notes and CRM loss reasons for the last two quarters (remove personal identifiers; use an approved tool).

For [product] in [segment], list the alternatives a buyer considers in four layers: direct competitors, indirect competitors (different category, same job or budget), substitutes (including services and building in-house with a general AI harness and connectors) and do-nothing (status quo, delay).

For each alternative give: who chooses it, why, what evidence in the material supports that, and our win rate against it if the data shows one.

Then propose two axes for a landscape map that buyers actually decide on, citing where in the material those criteria appear. Don't choose axes because they favor us.

Finally, run a Five Forces pass for this market. Treat model providers as suppliers and general-purpose AI harnesses as substitutes. Rank the forces by strength and explain what the top two mean for our margin and pricing power.

Check the output: every alternative and axis should trace to the material or to a cited public source. Ask a seller and a customer success manager whether the do-nothing and substitute entries match what they see.
```

```prompt title="Build an evidence table of competitor changes"
Goal: Monitor competitors with facts you can verify, not summaries you have to trust.
Paste in: the list of competitors and the period to cover.

Build an evidence table of every public change by these competitors in the last [12 months]: [competitors]. Include pricing and packaging changes, major releases, partnerships, acquisitions and leadership changes.

For each row give: date, competitor, change, source URL, source type (company's own site, filing, press, review site, social post) and a short quote from the source under 15 words.

Rules:
- Flag any row without a primary source (the company's own site or a filing) as "Secondary only."
- Flag any AI capability claim as "Vendor claim, not verified."
- Don't summarize or interpret until the table is complete. Then list the three changes most likely to affect our deals, with reasoning.

Check the output: open every source for rows you plan to use, and confirm the date and the quote. Delete any row whose source doesn't say what the table says.
```

```prompt title="Draft a battlecard from verified profile material"
Goal: Turn a verified competitor profile into a one-page battlecard sellers will use.
Paste in: the competitor profile (with sources), relevant win/loss themes and approved customer proof.

Using only the material provided, draft a one-page battlecard for [us] vs [competitor] in [segment] with these sections: when you'll meet them, why we win (three points, each with proof from the material), their pitch in their words, landmines (questions for the buyer that expose real gaps), objection handling (objection, response, proof), pricing guidance, customer proof and a "do not say" list.

Rules:
- Every claim must cite the source in the material. If proof is missing, write "Proof needed" instead of inventing it.
- No disparaging language about the competitor.
- Put any performance or AI claim we can't prove on the "do not say" list.

Check the output: have a person verify each claim against its primary source before the card goes to the field. Ask two sellers whether the landmines sound like questions a buyer would take seriously.
```

```prompt title="Code win/loss transcripts against a taxonomy"
Goal: Find patterns across many win/loss interviews without losing the evidence.
Paste in: interview transcripts and CRM notes for the period, and your reason taxonomy. These contain customer data: use an approved tool and remove personal identifiers where you can.

Code these [n] win/loss interviews against this taxonomy: [codes, for example product gap, price, trust or risk, timing, relationship, competitor strength, status quo].

1. For each interview, list the outcome (win, loss to competitor, no decision, churn), segment, the codes that apply and a short supporting excerpt for each code, with a timestamp or line reference.
2. Separate stated reasons from evidence: if the buyer says "price" but the transcript shows another cause, note both.
3. Return counts by code and outcome, split by segment.
4. Return two supporting excerpts per code, and flag any code supported by a single interview.

Check the output: pick at least ten interviews at random and check the codes against the transcripts yourself. If more than one or two are wrong, fix the taxonomy definitions and rerun before using the counts.
```

```prompt title="Stress-test a business case before finance does"
Goal: Find the weak points in your case while you can still fix them.
Paste in: the draft business case, the assumptions register and the scenario and sensitivity results.

Act as a skeptical FP&A partner reviewing this business case for [initiative].

1. List every assumption that lacks a source or owner, or whose confidence seems higher than its evidence.
2. Check whether the options include doing nothing and a cheaper alternative. If not, describe them.
3. Using the sensitivity results provided, name the three assumptions that matter most, and say what evidence would make each credible.
4. Test the downside scenario: is it bad enough? Compare it with typical IT project overruns and say what would put this project in the tail.
5. Run a premortem: assume the initiative failed badly two years from now and list the ten most likely reasons.
6. Propose kill criteria tied to the top assumptions, with dates and thresholds.

Don't recalculate the model unless I ask. Don't invent benchmarks; if you cite an external figure, give its source so I can check it.

Check the output: take the top three assumptions and the premortem list to your FP&A partner. Verify any external figure the model cites before it goes into the case.
```

## Anti-patterns

:::warn The analyst TAM on slide one
A large number from an analyst report opens the deck, for a category that bundles products you don't compete with. Finance discounts the whole case from that slide on. Lead with a bottom-up SAM and use the top-down figure as a check.
:::

:::warn SOM as a percentage
"If we get just 2% of the market..." There's no sales capacity, win rate or contract value behind it. Build SOM from reps, partners and win rates, or don't show it.
:::

:::warn The competitor grid of green ticks
A feature grid listing direct competitors, with every row favoring you. It ignores substitutes and the status quo, and the axes were chosen to flatter. Map all four layers on axes buyers use.
:::

:::warn No battlecard for doing nothing
The team has detailed cards for every vendor and none for the alternative that takes 40 to 60% of lost deals in the Dixon and McKenna data. Write the do-nothing card first.
:::

:::warn Win/loss by sales opinion
Loss reasons come from the CRM field the rep fills in on the way out of the deal. "Price" dominates, and nobody checks. Use neutral interviews, include no-decisions and check stated reasons against evidence.
:::

:::warn The hockey stick with no register
A revenue chart that turns sharply upward in year three, with no list of the assumptions that produce it. Show the assumptions register and the ranked sensitivity before any chart.
:::

:::warn Trusting the harness's citations
An AI research report goes into the case with its citations unchecked. One cited source doesn't contain the number; another measures a different category. Verify every number that reaches a decision on its primary source.
:::

## Checklist

- [ ] The decision requested is written in one sentence, with a decision maker and date.
- [ ] Segments are defined by trigger, job and buying motion, and they don't overlap.
- [ ] The sizing worksheet is bottom-up, with a source, date and confidence for every input.
- [ ] A top-down or value-based check agrees with the bottom-up number within an order of magnitude, or the gap is explained.
- [ ] SAM has a written boundary rule; SOM comes from a go-to-market capacity model.
- [ ] The competitive set covers direct, indirect, substitutes (including in-house AI builds) and do-nothing.
- [ ] The Five Forces pass names the strongest forces and their effect on margin and pricing power.
- [ ] The landscape map uses buyer-chosen axes and carries a date.
- [ ] Profiles and battlecards cite sources, show an owner and last-updated date, and include a do-nothing battlecard.
- [ ] Win/loss analysis runs continuously, uses neutral interviews, includes no-decisions and codes reasons into a stable taxonomy.
- [ ] Every number from an AI harness was checked on its primary source before reaching a decision or a seller.
- [ ] The business case includes do nothing and a cheaper option, an assumptions register with owners, three scenarios and a ranked sensitivity.
- [ ] NPV uses finance's hurdle rate, and payback is shown alongside it.
- [ ] The downside reflects the outside view and the fat tail, and the risks come from a premortem.
- [ ] For AI products, inference cost per unit of value and its trend are in the model.
- [ ] Kill criteria are tied to the top-ranked assumptions, and an actuals-against-case review is scheduled.

## Key takeaways

- Size markets bottom-up from counted accounts and value per account, and use top-down and value-based numbers as checks. SOM is a go-to-market capacity number, not a share of TAM.
- Segment by trigger, job and buying motion, and give each segment its own sizing row, competitive set and win rate.
- Compete against what customers would actually do. In B2B that's often nothing, and increasingly it's an in-house build on a general AI harness.
- Use Porter's Five Forces to explain margin and pricing power. For AI products, watch supplier power from model providers and substitution by do-it-yourself agents.
- A business case finance signs argues about assumptions: a sourced register, three scenarios, a ranked sensitivity, an outside-view downside and kill criteria tied to the assumptions that matter most.
- Let the harness collect, draft and monitor, and have a person verify every number and competitor claim on its primary source.
