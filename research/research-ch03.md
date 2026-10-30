# Research notes: Chapter 03, Building a Product Strategy and Roadmap

Prepared 2026-10-30 for *The Product 360 Handbook* (2026 edition). Audience: Senior to Principal PMs, B2B enterprise and platform products. Maps to eCornell "Building a Product Strategy and Roadmap" (prioritization framework, backlog, roadmap).

**Verification key**
- **[V]** Verified this session against the primary source or the author's own site (URL given).
- **[S]** Secondary only: consistent summaries, or the primary was unreachable this session. Check the book before quoting.
- **[U]** Unverified, from general knowledge. Confirm before print.

---

## Part A. Key concepts and frameworks

### A1. What strategy is: Richard Rumelt's kernel

- **Source:** Richard P. Rumelt, *Good Strategy/Bad Strategy: The Difference and Why It Matters* (Crown Business, 2011) [S on publisher and year]. Short form: "The perils of bad strategy," *McKinsey Quarterly*, June 2011 [S; McKinsey page timed out this session]. Later book: *The Crux: How Leaders Become Strategists* (2022) [U].
- **The kernel [S, consistent across summaries]:**
  1. **Diagnosis:** names the most pressing challenge and simplifies a messy situation into the one problem that matters most. It explains the "why".
  2. **Guiding policy:** the overall approach for dealing with the obstacles the diagnosis found. It rules things out as much as in.
  3. **Coherent actions:** coordinated policies, resource commitments and actions that carry out the guiding policy and reinforce each other. Not a list of independent initiatives.
- **Four hallmarks of bad strategy [S]:** (1) **Fluff:** jargon and buzzwords posing as insight. (2) **Failure to face the challenge:** no diagnosis, so the plan cannot be evaluated. (3) **Mistaking goals for strategy:** stating desired results ("grow 30%") with no plan to overcome obstacles. (4) **Bad strategic objectives:** a long laundry list of things to do, or objectives that are as hard as the original problem ("blue-sky objectives").
- **Other Rumelt ideas worth a sidebar [S]:** proximate objectives (a target close enough to be achievable, which turns a fuzzy challenge into a solvable one); leverage; chain-link systems (performance limited by the weakest link); Nvidia's 1990s turnaround as a kernel example (confirm detail in the book before using; prefer to omit real-company example and use Beacon).
- **B2B/platform PM application:** A product strategy that cannot name its diagnosis is a goal list. For an enterprise PM, the diagnosis usually involves a buying-side or ecosystem constraint (a gatekeeper, an incumbent platform's data gravity, a partner channel), not just a user pain. Test: can a stranger reading your guiding policy predict which three requests you will refuse?
- **Template (strategy kernel, one page):**
  > **Diagnosis:** The critical challenge is ___ because ___. Evidence: ___.
  > **Guiding policy:** We will ___ (and therefore we will not ___).
  > **Coherent actions (3 to 5):** ___; each names owner, resource commitment and how it reinforces the others.
  > **Proximate objective:** By ___ we will have ___ (measurable, achievable).
  > **Bad-strategy check:** fluff? goal masquerading as strategy? laundry list? unfaced challenge?

### A2. Strategy as an integrated set of choices: Lafley and Martin, *Playing to Win*

- **Source:** A. G. Lafley and Roger L. Martin, *Playing to Win: How Strategy Really Works* (Harvard Business Review Press, 2013) [S on publisher; year consistent across sources]. Companion: Roger L. Martin, "The Big Lie of Strategic Planning," *Harvard Business Review*, January to February 2014 [V: https://hbr.org/2014/01/the-big-lie-of-strategic-planning, intro only]. HBR video "A Plan Is Not a Strategy" (2022) [S].
- **The strategy choice cascade (five questions) [S, consistent across many summaries]:**
  1. **What is our winning aspiration?** The purpose of the enterprise, defined in terms of winning.
  2. **Where will we play?** The arenas: customers, segments, geographies, channels, product categories, value-chain stages.
  3. **How will we win?** The value proposition and competitive advantage in those arenas (Martin frames this as low cost or differentiation) [S].
  4. **What capabilities must be in place?** The activities and capabilities that make the how-to-win real.
  5. **What management systems are required?** The systems, structures and measures that build and sustain those capabilities.
- **Key idea:** strategy is an integrated set of choices, not a vision and not a plan. The cascade is iterative, not top-down only: each level's choices constrain and are constrained by the others. Choices at one level of the company nest inside the choices of the level above (a product line's cascade nests inside the business unit's) [S].
- **Martin's critique of planning [S]:** planning lists activities and budgets the company will do; it rarely says what the company chooses not to do and why. Planning feels safe because it is under the company's control; strategy is uncomfortable because it bets on things the company does not control (customers, competitors).
- **"What would have to be true?" [U, widely attributed to Martin and the Monitor/P&G strategy process]:** for each strategic possibility, list the conditions that must hold for it to be a great choice, then test the ones the team is least confident about. This links directly to hypothesis testing (Chapter 01) and is the bridge between strategy and discovery.
- **B2B/platform PM application:** A product-level cascade forces a platform PM to choose arenas explicitly: which buyer (economic buyer vs practitioner), which channel (direct enterprise vs partner/MSP), which ecosystem position (system of record vs layer on top of others' data). "Where to play" is where most B2B roadmaps quietly avoid choosing.
- **Combining Rumelt and Martin:** Rumelt's diagnosis is the missing first box in many cascades; Martin's where-to-play and how-to-win make Rumelt's guiding policy concrete. A practical one-pager uses Rumelt's kernel as the spine and Martin's five questions as the checklist.

### A3. Gibson Biddle: DHM, GEM, GLEe, SMT

- **Source:** Gibson Biddle (VP Product at Netflix 2005 to 2010 [S]; later Chief Product Officer at Chegg [U]), "Ask Gib: How do all your product strategy frameworks fit together?" *Ask Gib* newsletter (Substack), 7 January 2025 [V: https://askgib.substack.com/p/ask-gib-how-do-all-your-product-strategy]. Earlier long-form series on Medium, "How to Define Your Product Strategy" (2017 onward) [U on dates; Medium returned 403].
- **Biddle's four questions and models [V]:**
  1. *Long term, what are you building?* Positioning and branding; **GLEe** product vision model: **G**et big (on something), **L**ead (in that thing), **E**xpand (and keep expanding, the small "e").
  2. *What are the company's high-level priorities?* **GEM:** executives force-rank **G**rowth, **E**ngagement and **M**onetization, and assign a proxy metric to each.
  3. *What are your hypotheses for delivering the product?* **DHM:** how will the product **D**elight customers in **H**ard-to-copy, **M**argin-enhancing ways. Articulating these hypotheses is, in his words, the foundation of product strategy. **SMT lockup:** each **S**trategy is paired with a **M**etric (a proxy metric) and **T**actics (projects and experiments), so progress and the hypothesis can be tested.
  4. *How does the work fit together over time?* **Product roadmap:** shows when teams plan to deliver projects; the overall roadmap includes a high-level summary of product strategy; each "swimlane" (pod) has its own more detailed SMT and roadmap. Strategy is top-down and bottom-up and the two "meet in the middle."
- **Proxy metrics [S]:** a measurable, moveable stand-in for a hard-to-move top metric (Biddle's Netflix example is that retention is the top metric but too slow to move per experiment). Use proxies that are measurable, moveable by the team, and correlated with the top metric.
- **B2B/platform PM application:** "Delight" in B2B is split across personas (practitioner delight vs buyer value vs gatekeeper safety). "Hard-to-copy" for platforms usually means data network effects, integration depth and switching costs, ecosystem/partner lock-in, or proprietary evaluation data. "Margin-enhancing" became central again in the AI era because inference cost compresses gross margin (Beacon's drop from 81% to 72%).
- **SMT table format:**
  | Strategy (hypothesis) | Proxy metric | Tactics (projects, experiments) | D / H / M |
  |---|---|---|---|

### A4. Prioritization frameworks compared

General principle for the chapter: a scoring framework is a **conversation structure and a consistency device**, not an oracle. Every framework fails the same two ways: (1) inputs are opinions dressed as numbers; (2) the score optimizes inside the backlog you already have and cannot tell you whether the backlog serves the strategy. Strategy filters first; scoring ranks second.

#### RICE (Sean McBride, Intercom)
- **Source [V]:** Sean McBride, "RICE: Simple prioritization for product managers," Intercom blog, page dated 5 January 2018 (https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/). Widely cited as 2016; flag the date.
- **Formula:** RICE score = (Reach × Impact × Confidence) ÷ Effort. "Total impact per time worked."
- **Scales [V]:** Reach = people or events per time period (for example, customers per quarter), from real product data where possible. Impact per person: Massive 3, High 2, Medium 1, Low 0.5, Minimal 0.25. Confidence: High 100%, Medium 80%, Low 50% (below 50% is a "moonshot"). Effort: person-months across product, design and engineering.
- **Author's own caveats [V]:** not a hard and fast rule; lower scorers may go first as dependencies or table stakes for certain customers; working out of order is fine if the trade-off is visible.
- **Fits:** many comparable, medium-sized items in a product with usage data. **Failure modes in B2B:** Reach undervalues low-count, high-ARR accounts and gatekeeper requirements (one bank's audit requirement can unblock $2M); Impact is a guess; ignores time criticality and dependencies; platform enablers score low because their Reach is indirect. **B2B adaptation:** define Reach in accounts or ARR touched, not users, and make the choice explicit.

#### ICE (Sean Ellis)
- **Source [V via Gilad]:** ICE = Impact × Confidence × Ease, each on a relative 1 to 10 scale. Invented by Sean Ellis to prioritize growth experiments (Itamar Gilad, "The tool that will help you choose better product ideas," itamargilad.com, n.d.).
- **Fits:** fast ranking of many small experiments. **Failure modes:** three subjective numbers; Confidence is often self-assessed. **Fix:** Itamar Gilad's **Confidence Meter** grades confidence by the type of evidence: self conviction, thematic support and others' opinions earn near zero; anecdotal support and market data earn a little; customer evidence (interviews, studies) more; MVP and launch usage data most. Gilad calls opinion-based bets no better than roulette (paraphrase).

#### MoSCoW (Dai Clegg; DSDM)
- **Source:** Agile Business Consortium, DSDM Agile Project Framework, "MoSCoW prioritisation" [V via search extract of https://www.agilebusiness.org/?p=1907]. Origin with Dai Clegg at Oracle, 1994 [U].
- **Categories:** **M**ust have (minimum usable subset; without it the release is pointless, unsafe or illegal), **S**hould have (important, painful to leave out, but a workaround exists), **C**ould have (desirable, first to drop), **W**on't have this time (agreed out of scope for this timebox, which manages expectations).
- **DSDM guidance [V]:** Must Haves no more than about 60% of effort, a pool of Could Haves at about 20%; percentages apply to estimated effort, not count. Above 60% Must effort introduces a risk of failure.
- **Fits:** fixed-date, fixed-scope releases and contractual or regulatory deliverables (a committed enterprise release, a compliance deadline). **Failure modes:** everything becomes a Must; no ranking within a bucket; says nothing about value. The **Won't** bucket is the most useful part for B2B expectation-setting with sales.

#### Kano model (Noriaki Kano et al., 1984)
- **Source [S via Zacarias]:** Noriaki Kano et al., "Attractive Quality and Must-be Quality," 1984 (Japanese Society for Quality Control journal [U]); summarized in Daniel Zacarias, "The Complete Guide to the Kano Model," Folding Burritos (https://foldingburritos.com/blog/kano-model/).
- **Categories:** Must-be (basic expectations), Performance (one-dimensional, linear), Attractive (delighters), Indifferent, plus Reverse and Questionable (survey artifacts).
- **Method:** a functional question ("how do you feel if you have X?") and a dysfunctional question ("if you do not have X?"), each answered: I like it, I expect it, I am neutral, I can tolerate it, I dislike it. Cross-tabulate to classify.
- **Category decay:** delighters become performance and then must-be features over time. AI summaries were attractive in 2023 and are must-be in 2026 enterprise tools (author's framing, not a sourced fact).
- **Fits:** deciding the mix of a release; identifying table stakes vs differentiators. **Failure modes:** survey cost; respondents cannot evaluate features they have never seen (especially novel AI capabilities); different personas classify differently (SRE vs VP vs security reviewer). Segment by persona.

#### WSJF and Cost of Delay (Don Reinertsen; SAFe)
- **Reinertsen [S]:** Donald G. Reinertsen, *The Principles of Product Development Flow: Second Generation Lean Product Development* (Celeritas, 2009). Core argument: quantify the economic cost of delay; sequence work by cost of delay divided by duration (CD3) so the most value is delivered soonest. Most teams do not know the cost of a week of delay for their projects.
- **SAFe WSJF [V]:** "relative cost of delay divided by the relative job duration." Cost of Delay components: user and business value, time criticality, risk reduction and/or opportunity enablement. WSJF ignores sunk costs; priorities update continuously (https://framework.scaledagile.com/wsjf). SAFe practice uses a relative modified-Fibonacci scale [U, not on page fetched].
- **Black Swan Farming (Joshua Arnold) [V]:** Cost of Delay is a way of communicating the impact of time on outcomes; it combines urgency and value. CD3 = Cost of Delay Divided by Duration (https://blackswanfarming.com/cost-of-delay/). Critics argue SAFe's relative-point version loses the economic meaning of Reinertsen's dollars-per-week version [S, flag].
- **Fits:** large, time-sensitive items: renewal-linked features, regulatory deadlines (EU AI Act dates), competitive windows, platform enablers ("opportunity enablement" gives them credit RICE does not). **Failure modes:** relative scores invite gaming; duration estimates for discovery-heavy AI work are unreliable.

#### Opportunity scoring (Anthony Ulwick, Outcome-Driven Innovation)
- **Source [S, covered in Chapter 01 notes]:** Ulwick, *What Customers Want* (McGraw-Hill, 2005); Strategyn "opportunity algorithm": Opportunity = Importance + max(Importance − Satisfaction, 0), on survey ratings of desired outcome statements.
- **Fits:** choosing which customer outcomes (not features) are underserved, at strategy level. **Failure modes:** survey design effort; the score ranks needs, not solutions; can miss latent needs.

#### Value vs effort (2×2)
- **Origin:** general practice; no single originator [U]. Quadrants commonly named quick wins (high value, low effort), big bets or major projects (high value, high effort), fill-ins (low, low), money pits or time sinks (low value, high effort).
- **Fits:** a workshop's first cut; communicating with executives. **Failure modes:** both axes are guesses; collapses risk and time into nothing; everything drifts toward the "quick win" corner when estimates are optimistic.

#### Comparison table (for the chapter)
| Framework | Unit of decision | Best fit | Main failure mode | B2B adaptation |
|---|---|---|---|---|
| RICE | features, projects | many comparable items, usage data exists | Reach undervalues high-ARR, low-count accounts | Reach in accounts or ARR |
| ICE | experiments | growth tests, fast triage | three opinions multiplied | Confidence Meter evidence levels |
| MoSCoW | scope within a timebox | fixed-date commitments | everything is a Must | cap Musts at about 60% effort; publish Won'ts |
| Kano | feature types | release mix, table stakes | personas disagree; novel features unratable | run per persona |
| WSJF / CD3 | large items in a queue | time-sensitive, enabler work | relative points lose economics | price a week of delay in ARR at risk |
| Opportunity scoring | customer outcomes | strategy and discovery focus | survey cost; ranks needs, not solutions | survey per buying-center role |
| Value vs effort | anything | first-pass workshop | guesses on both axes | add a confidence column |

### A5. Roadmaps

#### Why feature-and-date roadmaps fail (Marty Cagan, SVPG)
- **Two inconvenient truths [V]:** Cagan, "The Inconvenient Truth About Product," SVPG, 17 March 2013 (https://www.svpg.com/the-inconvenient-truth-about-product/): at least half of ideas will not work, and ideas that do work typically take several iterations to deliver the expected business value.
- **The alternative [V]:** Cagan, "The Alternative to Roadmaps," SVPG, 7 September 2015 (https://www.svpg.com/the-alternative-to-roadmaps/). Feature roadmaps descend from command-and-control planning, tell teams what to build without a stated problem, and reward output. Alternative: product vision and strategy; business objectives (OKRs) per team, with teams deciding how; **high-integrity commitments** only where a fixed date or deliverable is truly needed. Suggested exercise: review last year's roadmap and count how many items met their business objectives.
- **High-integrity commitments [S/U on detail]:** in Cagan's later writing (*Inspired*, 2nd ed., 2017; *Empowered*, 2020 [U]), a commitment is made only after enough discovery that the team knows the solution is valuable, usable and feasible, and engineers have estimated it; then the date is kept. Use sparingly.
- **2026 update [V]:** Cagan, "Predictability vs Outcomes," SVPG, 12 October 2026 (https://www.svpg.com/predictability-vs-outcomes/): outcomes vs output is a false trade-off; the real tension is outcomes vs predictability. Most companies implicitly prioritize predictability. Predictability is sometimes required and handled with commitment techniques. Roadmaps of untested ideas with dates reinforce the predictability bias. Cites Henrik Kniberg's line equating full predictability with zero innovation. In 2026, abundant output with scarce outcomes is worse than ever.

#### Now / Next / Later (Janna Bastow, ProdPad)
- **Source [V]:** Janna Bastow, "I invented the Now-Next-Later roadmap..." ProdPad blog, 18 October 2022 (https://www.prodpad.com/blog/invented-now-next-later-roadmap/). First sketched in 2012 with Simon Cast as "Current / Near Term / Future" [V via author's comment reply]. Created out of frustration with Jira-style release planners and timeline roadmaps that force false date precision.
- **Columns [V]:** **Now:** work actively under way, well defined and broken into small pieces. **Next:** follows Now, less detailed, may depend on what Now teaches. **Later:** bigger, hazier problems kept on the radar; solutions not yet defined.
- **Rules [V]:** items are problems first; ideas, experiments and initiatives attach to problems and tie to objectives. No fixed delivery dates; columns reflect confidence and need not be equal in size; commit only to near-term work; time-sensitive items may carry a deadline; accountability sits in OKRs, not dates.
- **B2B/platform PM application:** Enterprise customers and sales need dates for some items (contracted features, compliance deadlines, deprecations). Keep the Now/Next/Later structure and mark the small set of dated **commitments** explicitly, distinct from **bets**. Deprecation and migration dates (Beacon Classic sunset) are commitments by nature.

#### *Product Roadmaps Relaunched* (Lombardo, McCarthy, Ryan, Connors)
- **Source:** C. Todd Lombardo, Bruce McCarthy, Evan Ryan and Michael Connors, *Product Roadmaps Relaunched: How to Set Direction while Embracing Uncertainty* (O'Reilly Media, 2017) [V on title and authors via Amazon listing; publisher and year S]. Book home: productculture.org [V that it lists the book].
- **Roadmap components [U, from memory of the book; confirm against the text before print]:** primary: **product vision**, **business objectives** (outcomes), **timeframes** (broad horizons, not dates), **themes** (customer needs or problems to solve), **disclaimer** (that the roadmap will change). Secondary: features and solutions, stage of development, confidence, target customers, product areas.
- **Key ideas [U]:** a roadmap is a statement of strategic intent and direction, not a release plan; build it around themes (problems) rather than features; gain buy-in through shuttle diplomacy and consensus building; tailor views by audience while keeping one source of truth.

#### Commitments vs bets
- **Shape Up betting table [U]:** Ryan Singer, *Shape Up* (Basecamp, 2019): leadership bets fixed appetites (six-week cycles) on shaped pitches; there is no backlog carried forward; unchosen pitches are not saved centrally. Useful contrast for backlog hygiene. Not fetched this session; confirm.
- **Synthesis for the chapter:** three categories on every roadmap: **Commitments** (dated, discovery done, engineers estimated, a customer or regulator depends on it); **Bets** (outcome-framed, sized by appetite, may be killed on evidence); **Explorations** (discovery only, no delivery promise). Sales-facing views show commitments and bet themes, never exploration specifics.

#### Communicating roadmaps (synthesis; flag as author guidance, not a sourced fact)
- **Executives:** outcomes, strategic bets, investment mix (for example, percent of capacity on new value vs platform vs tech debt), risks and decisions needed. One page.
- **Sales and field:** what they can say, what they cannot; commitments with dates; themes for Next and Later without dates; a "Won't" list; how to log customer requests; forward-looking statement guidance (public companies often need a safe-harbor disclaimer for roadmap disclosures [U; check legal practice]).
- **Customers:** problems you are solving for them and the direction, under NDA where needed; commitments only where contractual; invite discovery participation (design partners) rather than promising features.
- **Engineering and partners:** dependencies, API and deprecation timelines, platform contracts; partners need longer notice than direct customers.

### A6. Backlog construction and hygiene

- **Scrum Guide definition [V]:** Ken Schwaber and Jeff Sutherland, *The Scrum Guide*, November 2020 (https://scrumguides.org/scrum-guide.html): the Product Backlog is an emergent, ordered list of what is needed to improve the product. Its commitment is the **Product Goal**, a future state of the product the team plans against. **Refinement** is the ongoing act of breaking down and further defining items (description, order, size). The Product Owner is accountable for backlog management: developing and communicating the Product Goal, creating and communicating items, ordering them, and keeping the backlog transparent; the work may be delegated but accountability stays.
- **DEEP (Roman Pichler) [V]:** "Make the Product Backlog DEEP," romanpichler.com, 8 February 2010, updated 18 November 2024 (https://www.romanpichler.com/blog/make-the-product-backlog-deep/). **D**etailed appropriately (more detail at the top), **E**stimated (rough sizes for items needed for the current product goal), **E**mergent (changes continually with feedback), **P**rioritised (ordered; Pichler suggests risk first, then cost-benefit and dependencies). Keep it short and focused on the next product goal; a backlog of several hundred items is the core problem; if it has become too long, discard it and derive a fresh one from the roadmap. Pichler credits the "less detail at lower priority" principle to Schwaber and Beedle. Attribution of the DEEP acronym itself is often given to Mike Cohn [U].
- **Bets, not backlogs (Ryan Singer, *Shape Up*, 37signals/Basecamp) [V]:** chapter 7 "Bets, Not Backlogs" (https://basecamp.com/shapeup/2.1-chapter-07). Backlogs are a weight that creates a false sense of being behind. A betting table before each six-week cycle chooses pitches; unchosen pitches are dropped and not tracked centrally; anyone who still believes in one can lobby again. Book year 2019 [U].
- **Opportunity Solution Tree (Teresa Torres) [V]:** producttalk.org, updated 6 December 2023 (https://www.producttalk.org/opportunity-solution-tree/). Outcome (root, preferably a product outcome) > opportunities (customer needs, pains, desires) > solutions (for one target opportunity at a time) > assumption tests. A solution placed in the delivery backlog is a bet; discovery reduces its risk. Prioritize opportunities before solutions; effort is excluded at the opportunity stage.
- **Synthesis: backlog policy for a B2B platform team (author guidance)**
  1. **Three stores, not one list:** (a) **request inbox** (raw customer, sales, partner and support asks, linked to accounts and ARR; never ordered); (b) **opportunity backlog** (problems, clustered and sized; tied to the strategy's guiding policy); (c) **delivery backlog** (ordered, refined, sized; covers only the next one to two cycles of the Now column).
  2. **Entry criteria for delivery backlog:** linked opportunity and outcome; evidence level stated (Confidence Meter); owner; rough size; acceptance criteria; for AI features, an eval or quality bar.
  3. **Ageing rule:** items untouched for two quarters are archived with a reason; the request inbox remains searchable so sales can still see that a request was logged.
  4. **Capacity allocation:** declared split across new value, platform and enablers, quality and tech debt, and customer commitments; reviewed quarterly.
  5. **Review cadence:** weekly refinement of the top; monthly opportunity review; quarterly strategy and roadmap check; every reorder of a commitment is communicated.
  6. **Closing the loop:** every request gets a status a seller can quote ("logged, mapped to theme X, not planned this half").
- **AI harness use (2026):** an agent with connectors to the CRM, support desk and issue tracker can cluster requests into opportunities, attach ARR and account counts, flag duplicates and stale items, and draft the "why not" note. The PM reviews clusters and owns the ordering. Prompts, not formulas: "Group the last 90 days of feature requests from enterprise accounts into problem themes; for each theme show account count, ARR at renewal in the next two quarters and three verbatim excerpts."

### A7. Strategy one-pager (synthesis template for the chapter)

Combines Rumelt (kernel), Lafley and Martin (cascade) and Biddle (DHM, SMT). Author template; not from any one source.

> **Product:** ___ | **Horizon:** 12 to 24 months | **Owner:** ___ | **Last reviewed:** ___
> 1. **Diagnosis:** the one critical challenge, with evidence.
> 2. **Winning aspiration:** what winning looks like for customers and for us.
> 3. **Where we play / where we do not:** segments, buyers, channels, ecosystem position.
> 4. **How we win (DHM):** Delight ___; Hard to copy ___; Margin ___.
> 5. **Guiding policy:** the approach, plus the three things we will say no to.
> 6. **Coherent actions / SMT:** 3 to 5 strategies, each with a proxy metric and the tactics.
> 7. **Capabilities and systems we must build:** ___.
> 8. **What would have to be true:** the riskiest assumptions and how we will test them.
> 9. **Outcome metrics:** North Star plus 2 to 3 inputs; guardrails (margin, trust, quality).

### A8. Prioritization scorecard (synthesis template)

| Item (opportunity or bet) | Strategy link (which coherent action) | Accounts / ARR affected | Customer value (1 to 3) | Time criticality (cost of delay per month) | Risk reduction / enablement | Effort (team-weeks) | Evidence level (Confidence Meter) | Score | Decision (commit / bet / explore / no) |
|---|---|---|---|---|---|---|---|---|---|

Rules: score only items that pass the strategy filter; show the evidence level next to every score; a human writes the decision column; record why any item moves out of score order (McBride's visible trade-off rule).

### A9. Now / Next / Later roadmap and communication pack (synthesis templates)

- **Roadmap columns:** Now (committed, in delivery) | Next (bets, discovery under way) | Later (problems we intend to solve). Each card: problem or outcome, target metric, confidence, type (commitment / bet / exploration), date only if a commitment.
- **Communication pack:** (1) executive one-page (outcomes, bets, investment mix, risks, decisions needed); (2) field view (talk track, commitments with dates, themes without dates, Won't list, request process, disclaimer); (3) customer view (problems and direction, design-partner invitations); (4) partner and developer view (API changes, deprecations, notice periods); (5) changelog of what moved and why.

---

## Part B. Verified facts (with URL and date)

1. [V] RICE: Reach × Impact × Confidence ÷ Effort; Impact scale 3 / 2 / 1 / 0.5 / 0.25; Confidence 100% / 80% / 50%; Effort in person-months. McBride, Intercom, page dated 5 January 2018. https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/
2. [V] ICE was invented by Sean Ellis to prioritize growth experiments; each factor on a relative 1 to 10 scale. Gilad, itamargilad.com (n.d.). https://itamargilad.com/the-tool-that-will-help-you-choose-better-product-ideas/
3. [V] DSDM recommends Must Haves at no more than about 60% of effort and a pool of Could Haves at about 20%, on estimated effort, not count. Agile Business Consortium. https://www.agilebusiness.org/?p=1907 (read via search extract, not full fetch)
4. [V] SAFe defines WSJF as relative cost of delay divided by relative job duration; Cost of Delay = user and business value + time criticality + risk reduction and/or opportunity enablement. Scaled Agile, accessed 2026-10-30. https://framework.scaledagile.com/wsjf
5. [V] Kano categories (must-be, performance, attractive, indifferent, reverse, questionable) and the functional/dysfunctional question pair with five answer options. Original paper: Kano et al., "Attractive Quality and Must-be Quality," 1984. Zacarias, Folding Burritos. https://foldingburritos.com/blog/kano-model/
6. [V] Now-Next-Later: Bastow, ProdPad, 18 October 2022; first sketched in 2012 as Current / Near Term / Future. https://www.prodpad.com/blog/invented-now-next-later-roadmap/
7. [V] Cagan's two inconvenient truths: at least half of ideas will not work; working ideas take several iterations. SVPG, 17 March 2013. https://www.svpg.com/the-inconvenient-truth-about-product/
8. [V] Cagan's alternative to roadmaps: vision, team objectives, high-integrity commitments where needed. SVPG, 7 September 2015. https://www.svpg.com/the-alternative-to-roadmaps/
9. [V] Cagan: the real tension is outcomes vs predictability, not outcomes vs output. SVPG, 12 October 2026. https://www.svpg.com/predictability-vs-outcomes/
10. [V] Biddle's frameworks in order: GLEe vision, GEM priorities with proxy metrics, DHM hypotheses, SMT lockup, roadmap (overall and per swimlane). Ask Gib, 7 January 2025. https://askgib.substack.com/p/ask-gib-how-do-all-your-product-strategy
11. [V] Scrum Guide 2020: Product Backlog is an emergent, ordered list; Product Goal is its commitment. https://scrumguides.org/scrum-guide.html
12. [V] DEEP backlog attributes; Pichler, 8 February 2010, updated 18 November 2024. https://www.romanpichler.com/blog/make-the-product-backlog-deep/
13. [V] Shape Up: "Bets, Not Backlogs," six-week cycles, unchosen pitches not tracked centrally. 37signals. https://basecamp.com/shapeup/2.1-chapter-07
14. [V] Opportunity Solution Tree levels; a solution in the delivery backlog is a bet. Torres, Product Talk, 6 December 2023. https://www.producttalk.org/opportunity-solution-tree/
15. [V] Martin, "The Big Lie of Strategic Planning," HBR, January to February 2014. https://hbr.org/2014/01/the-big-lie-of-strategic-planning
16. [V] METR: the length of tasks frontier agents complete at 50% reliability doubled about every 7 months over roughly six years (to early 2025); METR notes the trend estimate ranges roughly 1 to 4 doublings per year and the static figure is dated. 19 March 2025. https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
17. [V] Anthropic gives at least 60 days' notice before retiring a publicly released model; deprecation table shows, for example, Claude Sonnet 4.5 deprecated 30 September 2026 with retirement 30 November 2026, and Claude Opus 4 and Sonnet 4 (released May 2025) retired 15 June 2026. Accessed 2026-10-30. https://platform.claude.com/docs/en/about-claude/model-deprecations
18. [V] Anthropic announced Claude Opus 5.5 (22 September 2026), Sonnet 5.5 (28 September 2026) and Haiku 5.5 (7 October 2026). https://www.anthropic.com/news
19. [V] EU AI Act: in force 1 August 2024; prohibitions and AI literacy 2 February 2025; GPAI obligations 2 August 2025; generally applicable 2 August 2026; AI Omnibus (proposed 19 November 2025, political agreement 7 May 2026, in force 27 July 2026) moved Annex III high-risk obligations from 2 August 2026 to 2 December 2027 and Annex I to 2 August 2028. European Commission, accessed 2026-10-30. https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
20. [V] Cagan: AI made building faster and cheaper; the hard part is deciding what to build; AI products make A/B tests slower and costlier, so use evals earlier and reserve tests for proving value. SVPG, 21 October 2026. https://www.svpg.com/experimentation-ai-and-the-product-model/
21. [V] Cagan: most teams use AI to speed up the output-oriented project model; faster building does not fix a team heading the wrong way. SVPG, 23 July 2026. https://www.svpg.com/the-ai-productivity-paradox/
22. [S] Rumelt's kernel (diagnosis, guiding policy, coherent actions) and four hallmarks of bad strategy (fluff, failure to face the challenge, mistaking goals for strategy, bad strategic objectives). *Good Strategy/Bad Strategy*, 2011; *McKinsey Quarterly*, 2011. Secondary: https://sachinrekhi.com/good-strategy-bad-strategy-richard-rumelt
23. [S] Lafley and Martin's five-question strategy choice cascade. *Playing to Win*, HBR Press, 2013. Secondary: https://fs.blog/2013/03/playing-to-win-how-strategy-really-works/

## Part C. Short quotes (all under 15 words)

1. "If you only quantify one thing, quantify the Cost of Delay." Don Reinertsen, *The Principles of Product Development Flow*, as quoted by Scaled Agile, https://framework.scaledagile.com/wsjf
2. "at least half of our ideas are just not going to work." Marty Cagan, SVPG, 2013, https://www.svpg.com/the-inconvenient-truth-about-product/
3. "The Product Backlog is an emergent, ordered list of what is needed to improve the product." Schwaber and Sutherland, *The Scrum Guide*, 2020 (16 words; trim to "an emergent, ordered list of what is needed to improve the product" if used).
4. "100% predictability = 0% innovation." Henrik Kniberg, as quoted by Cagan, SVPG, 12 October 2026, https://www.svpg.com/predictability-vs-outcomes/
5. "Backlogs are a big weight we don't need to carry." Ryan Singer, *Shape Up*, https://basecamp.com/shapeup/2.1-chapter-07

## Part D. 2025 to 2026 AI-era developments relevant to strategy and roadmaps

1. **Capability cadence outpaces annual and even quarterly plans.** Anthropic's model table (fact 17) implies new frontier releases roughly every two to three months through 2025 and 2026 (Opus 4 in May 2025, Opus 4.1 in August, Sonnet 4.5 in September, Haiku 4.5 in October, Opus 4.5 in November 2025; Opus 4.6, 4.7, 4.8, 5 and 5.5 through 2026). The 2026 release months are **inferred** from "not sooner than" retirement dates set one year out; flag before stating as fact. METR's doubling trend (fact 16) is the best public evidence that agent capability on long tasks grows fast. Implication: an AI product's Later column can become feasible inside a quarter; a Now item built around a model limitation can become obsolete.
2. **Model retirement is a roadmap dependency.** Providers retire models on published schedules with notice measured in weeks to months (60 days minimum for Anthropic). A B2B AI product needs a standing "model migration" lane: re-run evals on each new model, re-baseline cost, decide upgrade timing. This is a commitment-class item because it is externally dated.
3. **Regulatory dates move.** The EU AI Omnibus (fact 19) moved Annex III high-risk obligations by 16 months after many vendors had planned to August 2026. Lesson for cost of delay: regulatory deadlines are commitments, but the date itself can change; track the source and replan.
4. **Output is cheap; deciding is the bottleneck.** Cagan's 2026 essays (facts 9, 20, 21) argue AI made building cheap but did not make outcomes cheap; feature roadmaps that AI can now generate instantly entrench the predictability bias; evals come earlier and A/B tests get costlier for AI features. Implication: prioritization should weight evidence (Confidence Meter) more and effort less, because effort estimates shrink and become less discriminating.
5. **Roadmapping AI products: author synthesis for the chapter.** (a) Frame Now/Next/Later items as **capability-independent customer outcomes** ("diagnosis an on-call engineer trusts in under five minutes"), not model-dependent features. (b) Keep a **capability watchlist**: for each Later item, the capability threshold that would move it to Next, checked against each new model via the team's evals. (c) Run a **quarterly "what would have to be true" refresh** on AI bets. (d) Budget an **eval and migration lane** as fixed capacity. (e) Treat **unit economics** as a roadmap constraint (Biddle's M in DHM), since inference cost moves with model choice. (f) Never commit dates to customers for capabilities that depend on unreleased model improvements.
6. **The AI harness in strategy work (2026 practice).** PMs use an AI assistant with connectors to draft a strategy kernel from customer-call notes, CRM and win/loss data; to red-team a strategy against Rumelt's four hallmarks; to produce audience-specific roadmap views from one source; and to cluster backlog requests. Teach as prompts and review steps; the PM owns choices. (Author practice; no external statistic.)

## Part E. Beacon worked example ideas (consistent with beacon-case.md)

- **Strategy kernel for Beacon 2027:**
  - *Diagnosis:* Beacon's correlation lead is eroding as large observability platforms bundle AIOps; customers trust Beacon to summarize but not yet to act; and agentic features cut gross margin from 81% to 72%. The critical challenge is converting diagnosis trust into supervised action without breaking margin.
  - *Guiding policy:* win on **trusted diagnosis and supervised remediation across the customer's existing tools** (tool-agnostic via connectors and MCP), using Northlight Observe data as an accelerant, not a requirement. This resolves the build-on-Observe vs tool-agnostic tension explicitly; say what Beacon will not do (for example, will not build its own metrics store; will not ship fully autonomous actions outside customer allowlists).
  - *Coherent actions:* (1) raise diagnosis acceptance rate with cited evidence and evals; (2) launch Beacon Agents at Northlight Live with approval gates and audit logs Sam can sign off; (3) move to per-resolved-incident pricing to align price with value and fund inference; (4) cut inference cost per incident (model routing); (5) sunset Beacon Classic to free a team.
  - *Proximate objective:* for example, diagnosis acceptance rate above a target in the top 50 accounts by a stated quarter (author to choose fictional numbers).
- **Playing to Win cascade for Beacon:** where to play: enterprise SRE and platform teams with multi-vendor observability, plus MSPs (Leo) for mid-market; not small teams with a single-vendor stack. How to win: trusted, cited diagnosis plus safe action, priced per outcome.
- **DHM for Beacon:** Delight: Dana gets "what broke and what to do" in under five minutes. Hard to copy: resolved-incident data feeding retrieval and evals (Learn loop), connector breadth, approval and audit design. Margin: per-resolved-incident pricing plus model routing.
- **Bad strategy example to critique:** a draft that says "Become the #1 AI agent platform for IT operations with best-in-class AI" (fluff, goal as strategy) and lists twelve initiatives (laundry list).
- **Prioritization scorecard exercise:** five candidates: (a) EU AI Act documentation pack (time-critical, gatekeeper, enables EU deals); (b) MSP multi-tenant billing for Leo; (c) autonomous rollback for allowlisted actions; (d) Beacon Classic migration tooling; (e) a ServiceNow-style ticketing connector (use a generic name, not a real vendor). Show RICE ranking (b) or (e) high because of Reach, while WSJF ranks (a) and (d) high because of time criticality and opportunity enablement. Lesson: framework choice changes the answer; strategy decides which lens matters. After the AI Omnibus moved Annex III dates, re-score (a) and show cost of delay dropping but not to zero (customers still ask; Sam's needs persist).
- **Now / Next / Later for Beacon:** Now: Beacon Agents supervised remediation GA for Northlight Live (commitment); Beacon Classic sunset with dated migration milestones (commitment); diagnosis citation quality (bet). Next: per-resolved-incident pricing pilot (bet); MSP multi-tenant views (bet). Later: broader autonomous resolution for low-risk classes, gated by eval thresholds on future models (exploration with capability watchlist).
- **Roadmap communication pack:** Marcus gets outcomes and ROI; sales gets commitments (Agents GA date, Classic end-of-life date) and themes without dates; Priya's team gets design-partner invitations; partners like Leo get API and deprecation notice periods; Sam gets AI Act documentation timeline.
- **The hallucinated root cause incident** can show a reprioritization: trust work jumps the queue; show the changelog entry explaining what moved and why.
- **Backlog policy:** 3 PMs, about 35 engineers across 5 teams; capacity split example (fictional): 50% new value, 20% platform and connectors, 15% quality, evals and model migration, 15% commitments and Classic migration.

## Part F. Editorial flags

1. Rumelt and Playing to Win details are secondary-only this session (McKinsey page timed out; Medium blocked). Check the books for exact hallmark wording, publisher names and the Nvidia example before print. Prefer Beacon examples over real-company ones.
2. RICE date: Intercom page shows 5 January 2018; widely cited as 2016. Use "Intercom, 2016 (updated 2018)" only after confirming, or say "Sean McBride at Intercom".
3. MoSCoW origin (Dai Clegg, Oracle, 1994) is unverified; DSDM guidance read via search extract, not a full page fetch.
4. *Product Roadmaps Relaunched* components list (vision, business objectives, timeframes, themes, disclaimer; secondary components) is from memory; the publisher page was blocked. Verify against the book before presenting as its template.
5. "What would have to be true" is widely attributed to Martin and the P&G/Monitor process; not verified this session.
6. Cagan's "high-integrity commitments" process detail (discovery, then estimate, then commit) is from his books, not verified this session; the 2015 SVPG article names the concept only.
7. Shape Up publication year (2019) and DEEP acronym origin (Mike Cohn) are unverified.
8. SAFe modified-Fibonacci scale not on the page fetched. Critique that SAFe's relative WSJF loses Reinertsen's economics is a practitioner debate; present as contested.
9. 2026 Claude release months are inferred from retirement-floor dates; state only the dated facts (fact 17 and 18) or confirm on the announcements.
10. Bastow post title as given in refs is approximate; confirm exact title on the ProdPad page.
11. Value vs effort quadrant names vary by source; no single originator.
12. Quote 3 (Scrum Guide) is 16 words in full; trim if used.
13. Web search budget ran out mid-session; no 2025 to 2026 survey statistics on roadmap practice were gathered. Do not invent any.
