# Research notes: Chapter 17, The Questions That Drive Product Decisions

Status: in progress. Research date 2026-10-30. Note: WebSearch budget for this run was exhausted at the start; sources were reached by direct WebFetch of known primary URLs.

## Source log (running)

### Eric Ries, Vanity Metrics vs. Actionable Metrics (guest post on tim.blog, 2009-05-19) [V]
URL: https://tim.blog/2009/05/19/vanity-metrics-vs-actionable-metrics/
- Vanity metrics look good but do not tell you what to do next (examples: total hits, cumulative totals).
- Actionable metrics show clear cause and effect, enough to guide a decision.
- Three principles in this post: "Measure what matters" (few metrics; detailed reports diagnose, actionable metrics reveal), "Metrics are people, too" (trace numbers to real customers, then talk to them), "Measure the macro" (do not optimize intermediate numbers like click-through; focus on purchase, retention).
- Techniques: split tests (revenue per customer in test vs control), per-customer ratios instead of totals, cohort analysis by signup week, keyword-acquisition cohorts (IMVU example revealed users were younger than assumed).
- NOTE: this post does NOT contain "actionable, accessible, auditable". The three A's are from Ries's later writing (The Lean Startup, 2011, ch. 7). Verify separately.
- Quote: "Vanity metrics: good for feeling awesome, bad for action." (Ries, 2009)

### Jeff Bezos, 2015 Letter to Shareholders (Amazon, filed April 2016) [V]
URL: https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm
- Type 1: consequential, irreversible or nearly irreversible ("one-way doors"); decide slowly, carefully, with deliberation and consultation.
- Type 2: changeable, reversible ("two-way doors"); a suboptimal one need not be lived with for long; should be made quickly by high-judgment individuals or small groups.
- Risk: as organizations grow, they tend to use the heavyweight Type 1 process on most decisions, including Type 2. Result: slowness, unthoughtful risk aversion, failure to experiment, diminished invention.
- Quote: "Type 2 decisions can and should be made quickly" (Bezos, 2015 letter)

### Jeff Bezos, 2016 Letter to Shareholders ("Day 1") (Amazon, filed April 2017) [V]
URL: https://www.sec.gov/Archives/edgar/data/1018724/000119312517120198/d373368dex991.htm
- High-velocity decisions: most decisions should be made with about 70% of the information you wish you had; waiting for 90% usually means being slow.
- Being wrong is often cheaper than being slow, if you are good at spotting and correcting bad decisions.
- "Disagree and commit" saves time when there is conviction without consensus; applies to leaders too.
- Resist proxies: process as proxy (following process becomes the goal) and surveys/market research as proxy (averages and beta percentages mislead; owners need deep customer understanding). Directly relevant to vanity metrics: the metric becomes the thing.
- Quote: "around 70% of the information you wish you had" (Bezos, 2016 letter)

### Daniel Kahneman, Dan Lovallo, Olivier Sibony, "Before You Make That Big Decision" (Harvard Business Review, June 2011) [V for authors/date; checklist items S]
URL: https://hbr.org/2011/06/the-big-idea-before-you-make-that-big-decision
- A decision-quality-control checklist for leaders reviewing a team's recommendation: you cannot remove your own biases, but you can detect them in a team's proposal.
- The 12 questions (from memory of the article; the fetched page was paywalled, so mark [S] and recheck): self-interested biases; affect heuristic (has the team fallen in love with it); groupthink (were dissenting views explored); saliency (overweighting an analogy to a memorable success); confirmation bias (credible alternatives considered); availability (what data would you want if starting fresh); anchoring (where did the numbers come from); halo effect; sunk-cost/attachment to past decisions; overconfidence (is the base case too optimistic); disaster neglect (is the worst case bad enough); loss aversion (is the team too cautious).
- Application: the PM uses this as a review pass on their own decision memo, or asks the AI harness to red-team a memo against these 12 checks.

### Annie Duke, Thinking in Bets (Portfolio, 2018-02-06) [V publisher page]
URL: https://www.penguinrandomhouse.com/books/552885/thinking-in-bets-by-annie-duke/
- Decision quality and outcome quality are different things: good decisions can lose to luck, bad ones can win. Example used: Pete Carroll's Super Bowl XLIX pass call.
- "Resulting" is Duke's name for judging a decision by its outcome (term is in the book; the publisher page does not use it, so [S] for the term).
- Treat decisions as bets: state confidence, list possible outcomes, choose the best odds; replace the need for certainty with calibrated "I'm not sure" / percentage confidence.
- Quote: "Even the best decision doesn't yield the best outcome every time." (publisher description of Thinking in Bets, 2018)
- Duke's later books: How to Decide (Portfolio, 2020) [S for date] with tools such as decision trees, pre-commitment, premortems, and the idea of logging what you knew at the time; Quit (2022) with kill criteria and "quitting contracts", premortems, backcasts, expected value (tools confirmed on https://www.annieduke.com/books/ [V]).
- Application for PMs: the decision memo records the information, options, probabilities and kill criteria at the time of the decision, so later review judges the process not the result. A retrospective asks "was it the decision or the dice?"

### Kerry Rodden, Hilary Hutchinson, Xin Fu, "Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications" (CHI 2010, Google) [V]
URL: https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/
- Introduces the HEART framework (Happiness, Engagement, Adoption, Retention, Task success) and a process for mapping product goals to metrics (widely known as Goals, Signals, Metrics; label [S], the abstract does not use it).
- Application: a question bank starts with the goal, names the signal (behavior or attitude that would show the goal is met), then the metric. B2B twist: Adoption and Task success measured per account and per role, not just per user.

### Teresa Torres, Opportunity Solution Trees (Product Talk, 2023-12-06) [V]
URL: https://www.producttalk.org/opportunity-solution-trees/
- Layers: desired outcome (root) > opportunities (customer needs, pains, desires) > solutions > assumption tests.
- Purpose: balance business value with customer value; shared visual map of what to work on next and why.
- Quote: "help product teams chart the best path to their desired outcome" (Torres, 2023)
- Application: each node in the tree generates a question type. Outcome node: "is this the right metric?" Opportunity node: "how big and how frequent is this pain, for whom?" Solution node: "does this solution move the outcome?" Assumption test: "what is the cheapest evidence that would change our mind?"

## AI-era sources (2024 to 2026)

### Anthropic, Introducing the Model Context Protocol (2024-11-25) [V]
URL: https://www.anthropic.com/news/model-context-protocol
- MCP is an open standard for connecting AI assistants to where data lives: content repositories, business tools, development environments.
- Relevance: the PM's harness reaches analytics, CRM, support tickets, call transcripts and billing through connectors. Question framing becomes the bottleneck, not access.

### dbt Labs, dbt Semantic Layer docs (accessed 2026-10-30) [V]
URL: https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl
- Define metrics once in the modeling layer (MetricFlow); used consistently by every tool; change the definition once and it updates everywhere.
- States that AI tools such as Claude and ChatGPT can connect through the dbt MCP server so answers use governed metric definitions instead of guessing at raw tables.
- Application: the metric definition card is the human-readable twin of a governed semantic-layer metric. The PM should ask "is there a governed definition of this metric?" before trusting any AI answer.

### Snowflake, Cortex Analyst docs (accessed 2026-10-30) [V]
URL: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst
- LLM-powered natural-language questions over structured data, no SQL by the user.
- Snowflake states generic AI struggles with text-to-SQL from schema alone because schemas lack business process definitions and metric handling; a semantic view supplies logical tables, dimensions, facts, metrics, relationships, join paths and verified example questions.
- Recommends running evaluations against verified queries to measure accuracy.
- Application: vendors themselves say ambiguity in metric definitions is the main failure mode. That is the case for the metric definition card and for "verified questions" in a team question bank.

### BIRD text-to-SQL benchmark (bird-bench.github.io, accessed 2026-10-30) [V, leaderboard volatile]
URL: https://bird-bench.github.io/
- 12,751 question/SQL pairs, 95 databases (33.4 GB), 37+ professional domains.
- Human performance (data engineers and database students): 92.96% execution accuracy.
- Top leaderboard entry at access time: 83.40% test execution accuracy (entry dated 2026-10-22 per page). FLAG: leaderboard changes often; cite as "at time of writing" or use only the human baseline and the point that the best systems still trail humans on hard, messy enterprise schemas.
- Teaching point: even strong systems answer some questions wrongly; ambiguous questions make it worse. Ask the harness to show its definition, population and filters so you can audit (Ries's "auditable").

### Anthropic, Donating MCP and establishing the Agentic AI Foundation (2025-12-09) [V]
URL: https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
- MCP donated to the Agentic AI Foundation (AAIF), a directed fund under the Linux Foundation, co-founded by Anthropic, Block and OpenAI; supported by Google, Microsoft, AWS, Cloudflare, Bloomberg.
- Stated adoption: more than 10,000 active public MCP servers; 97M+ monthly SDK downloads (Python and TypeScript); over 75 Claude connectors powered by MCP (as of Dec 2025).

### Mixpanel, MCP server docs (accessed 2026-10-30) [V]
URL: https://docs.mixpanel.com/docs/features/mcp
- AI assistants can query product analytics in natural language: insights, funnels, flows, retention, session replays; discover projects, events, properties. Can also build dashboards, edit metadata, manage cohorts, experiments and feature flags. Access follows each user's existing permissions.
- Teaching point: the report types (funnel, retention, flow, cohort) are now things you ask for in words. The PM must know which report answers which question, not how to build it.

## Decision quality and measurement theory

### Goodhart's law and Strathern's wording [S, Wikipedia; primary citations given]
URL: https://en.wikipedia.org/wiki/Goodhart%27s_law
- Charles Goodhart, "Problems of Monetary Management: The UK Experience" (1975): a statistical regularity tends to collapse once pressure is placed on it for control.
- Marilyn Strathern, "'Improving ratings': audit in the British University system", European Review 5(3), 1997, pp. 305 to 321: common form "When a measure becomes a target, it ceases to be a good measure" (she was drawing on Keith Hoskin, 1996).
- Application: pair every target metric with a guardrail (counter-metric); Beacon example below (autonomous resolution rate vs. wrong-action rate).

### Douglas W. Hubbard, How to Measure Anything, 3rd ed. (Wiley, 2014) [V for book details; S for concepts]
URL: https://www.wiley.com/en-us/How+to+Measure+Anything%3A+Finding+the+Value+of+Intangibles+in+Business%2C+3rd+Edition-p-9781118539279
- Wiley page confirms: intangibles such as customer satisfaction, flexibility, technology risk can be measured; "immeasurable" is a misconception; aim is less risky, more profitable decisions.
- From the book (well known, not on the publisher page, so [S]): measurement is a reduction in uncertainty, not elimination; value of information: measure what would change the decision; small samples reduce uncertainty a lot when you know little (e.g. "rule of five"); clarification chain (if it matters it is observable, if observable it can be measured as an amount or range).
- Application: a question is worth asking only if some plausible answer would change the decision. Question brief field: "What answer would change our decision?"

### Decision Quality: Ronald A. Howard (Stanford) and the Strategic Decisions Group tradition; Spetzler, Winter, Meyer, Decision Quality (Wiley, 2016) [V book details; elements S]
URLs: https://www.wiley.com/en-us/Decision+Quality%3A+Value+Creation+from+Better+Business+Decisions-p-9781119144670 ; https://en.wikipedia.org/wiki/Decision_quality
- Six elements: (1) appropriate frame, (2) creative, doable alternatives, (3) relevant and reliable information, (4) clear values and trade-offs, (5) sound reasoning, (6) commitment to action.
- Weakest-link principle: the decision is only as good as its weakest element.
- Wiley page's six steps: frame the problem, create alternatives, identify uncertain information, clarify values, apply analysis, develop buy-in.
- Wikipedia credits Howard Raiffa and Ronald A. Howard with the underlying decision analysis concepts (1960s). FLAG: attribution of the "DQ chain" usually goes to Howard and SDG (Spetzler); keep attribution as "Ronald Howard and colleagues at Stanford and the Strategic Decisions Group".
- Application: the decision memo template is built on these six elements; "information" is the place this chapter's question bank plugs in. Data alone cannot fix a bad frame or missing alternatives.

### Anthropic, Prompting best practices (platform.claude.com docs, accessed 2026-10-30) [V]
URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Treat Claude as a brilliant but new employee who lacks context on your norms; the more precisely you explain, the better the result.
- Key test: show the prompt to a colleague with minimal context; if they would be confused, the model will be too.
- Give context and motivation (why it matters, what it is for) to get more targeted responses.
- Application to question framing: the "question brief" is the context the harness needs. Population, time window, metric definition, comparison and the decision at stake are the context a new analyst would ask for on day one.

## Market and product-fit questions

### Marc Andreessen, "Part 4: The only thing that matters" (pmarchive, 2007-06-25) [V]
URL: https://pmarchive.com/guide_to_startups_part4.html
- Product/market fit defined as being in a good market with a product that can satisfy that market.
- Use in the invest stage: "do we have evidence of pull?" questions.

### Sean Ellis, product/market fit survey (pmfsurvey.com, with GoPractice) [V for attribution only]
URL: https://pmfsurvey.com/
- Page credits the survey to Sean Ellis and GoPractice. The well-known core question ("How would you feel if you could no longer use [product]?" with very / somewhat / not disappointed) and the 40% "very disappointed" benchmark are NOT on the fetched page: [S], FLAG. If used, present the 40% as Ellis's rule of thumb, not as a validated threshold, and note B2B sample-size limits (few accounts, many users per account).

### Peter van Westendorp, Price Sensitivity Meter (1976) [S, Wikipedia]
URL: https://en.wikipedia.org/wiki/Van_Westendorp%27s_Price_Sensitivity_Meter
- Four questions: too expensive to consider; so cheap quality is doubtful; starting to get expensive but still considered; a bargain.
- Use in the price stage question bank as a qualitative/survey evidence source, alongside win/loss, discount depth and usage-to-price fit.

## Data-driven decisions: evidence and practice

### Erik Brynjolfsson and Kristina McElheran, "The Rapid Adoption of Data-Driven Decision-Making" (American Economic Review 106(5), 2016, pp. 133 to 139) [V abstract]
URL: https://www.aeaweb.org/articles?id=10.1257/aer.p20161016
- Census data on US manufacturing plants: share using data-driven decision-making rose from about 11% to 30% between 2005 and 2010.
- Adoption uneven: larger plants, plants with complementary IT and skilled workers, and learning firms adopt more. Authors say it is consistent with evidence that DDD raises productivity (the productivity magnitude is in a companion paper; not verified here, do not quote a number).

### Jeff Bezos, 2017 Letter to Shareholders (Amazon, filed April 2018) [V]
URL: https://www.sec.gov/Archives/edgar/data/1018724/000119312518121161/d456916dex991.htm
- No slide presentations at Amazon; meetings start with silent reading of narrative memos (six pages).
- Weak memos come from underestimating the scope of the work; a great memo probably takes a week or more (rewrites, feedback, rest, fresh edit).
- Quote: "They simply can't be done in a day or two." (Bezos, 2017 letter, on great memos)
- Application: the decision memo is a narrative, not a dashboard screenshot. AI makes drafting fast, which raises the bar on thinking, not lowers it.

### Marty Cagan, The Four Big Risks (SVPG, 2017-12-04) [V]
URL: https://www.svpg.com/four-big-risks/
- Value (will customers buy or choose to use it), usability (can users figure it out), feasibility (can engineering build it with the time, skills, tech), business viability (does it work for sales, legal, finance, compliance, brand).
- Application: the build-stage question bank is organized by these four risks; each risk has a question, the cheapest evidence, and the decision (proceed, change, stop).

### Amplitude, AI Agents page (accessed 2026-10-30) [V, no launch date on page]
URL: https://amplitude.com/ai-agents
- Agents that watch metrics on a schedule, run diagnostics, analyze experiments, segment users, combine quant with support tickets and surveys, watch session replays for friction, draft dashboards and PRDs.
- Teaching point: monitoring ("did something change?") is being automated; the PM's scarce skill is asking the decision question and judging whether the evidence is good enough. Do not cite a launch date (FLAG: page says only "earlier this year").

### Ron Kohavi, Diane Tang, Ya Xu, Trustworthy Online Controlled Experiments (Cambridge University Press, 2020) [V book; guardrails from ch05 refs]
URL: https://experimentguide.com/
- Overall Evaluation Criterion (OEC): the quantitative measure of an experiment's objective, chosen to predict long-term value. Guardrail metrics protect against harm (covered in Chapter 5; cross-reference within the book only).
- Application: the launch-stage question "did it work?" needs an OEC and guardrails defined before launch, written on the metric definition card.

### Chip Heath and Dan Heath, Decisive (Crown Business, 2013) [S]
URL: https://heathbrothers.com/books/decisive/
- Page confirms a four-step process to counteract decision biases; steps not on page. Widely known as WRAP: Widen your options, Reality-test your assumptions, Attain distance before deciding, Prepare to be wrong. [S] Optional; use only if space allows.

### Eric Ries, The Lean Startup (Crown Business, 2011), ch. 7 "Measure" [S for the three A's]
URL: https://theleanstartup.com/principles
- Site confirms Build-Measure-Learn, innovation accounting, and that MVP measurement "must include actionable metrics" showing cause and effect.
- The three A's (from the book, not re-verified online in this run): Actionable (clear cause and effect, so you know what to do), Accessible (reports simple enough that everyone understands them; "metrics are people too", tied to real customers), Auditable (data is credible; anyone can trace a number back to the underlying customers and test it). FLAG: verify wording against the book before quoting; paraphrase only.

### Alistair Croll and Ben Yoskovitz, Lean Analytics (O'Reilly, 2013) [S]
URL: https://leananalyticsbook.com/
- Site confirms authors and "One Metric That Matters" for your current stage.
- From the book [S]: a good metric is comparative (over time or across groups), understandable, a ratio or rate, and changes behavior. Also contrasts exploratory vs reporting metrics, leading vs lagging, correlated vs causal. FLAG: verify before quoting.

---

# (a) Key concepts and frameworks: synthesis for the chapter

## 1. The core unit: a decision, not a dashboard
- Principle for the chapter: every question exists to inform a named decision with an owner and a date. If no answer would change the decision, it is not worth asking (Hubbard's value of information idea).
- Chain: Decision > Question > Evidence (quant + qual) > Report or source > Owner. This is the "question brief".
- Bezos's 70% rule and Type 1/Type 2 set how much evidence a question deserves: two-way doors get a fast question and a quick read; one-way doors get a full question brief, metric cards, and a decision memo with pre-mortem.

## 2. Good questions vs vanity questions
Vanity question tests (built on Ries; Croll and Yoskovitz; Goodhart/Strathern):
- Is the answer a cumulative total that only goes up (total signups, total agents deployed)? Vanity. Rewrite as a rate per cohort or per account.
- Could any plausible answer change what we do? If not, vanity.
- Is there a comparison (to last period, to a control, to a segment, to a target)? Without one, a number is trivia.
- Can we trace the number to named customers and talk to them? (Ries: metrics are people too; auditable.)
- Is the metric a target that people can game? Pair with a guardrail (Goodhart).
Examples of rewrites (B2B):
- Vanity: "How many users logged in last month?" Good: "Of accounts that went live in Q2, what share have three or more weekly active responders in week 8, compared with Q1 cohorts?" Informs: whether to change onboarding.
- Vanity: "How many AI suggestions did we generate?" Good: "What share of suggestions were accepted, by severity, and what share of accepted ones were later reverted?" Informs: whether to widen autonomy.
- Vanity: "What's our pipeline for the new SKU?" Good: "In late-stage deals where the new SKU was offered, what's the win rate and discount depth versus deals where it wasn't, and why did the losses go?" Informs: pricing and packaging.

## 3. Decision types across the lifecycle with question bank seeds
For each: decision, questions, evidence (quant / qual), report that answers it.

DISCOVER (Decision: which problem/segment to pursue)
- Q: Which jobs or pains are most frequent and most costly for which segment? Quant: support ticket themes by account tier, usage gaps, search logs. Qual: interviews, call transcripts, win/loss notes. Report: opportunity sizing by segment; theme analysis of transcripts (AI harness summarizes with citations).
- Q: How do customers solve it today, and what does it cost them? Qual: contextual interviews; Quant: time spent, workaround tools in use. Decision: pursue or park.
- Frame: Torres opportunity solution tree (outcome > opportunities).

INVEST (Decision: fund, size, sequence)
- Q: How much value is at stake, and how confident are we? Evidence: addressable accounts, current spend on alternatives, expansion potential, Andreessen-style pull signals (inbound requests, pilots converting). Report: business case with ranges, not points (Hubbard).
- Q: What would we have to believe? (assumption list) Evidence: the weakest assumption gets the next test.
- Q: Is this Type 1 or Type 2? Determines evidence bar.

BUILD (Decision: proceed, change scope, stop)
- Cagan's four risks as questions. Value: do design partners use the prototype on real work? Usability: can a new responder complete the core task unaided? Feasibility: can we hit latency/accuracy at acceptable cost? Viability: can sales, legal, security and finance support it?
- Evidence: prototype tests, eval results (for AI features), cost per task, security review findings.

LAUNCH (Decision: ship, widen rollout, roll back)
- Q: Did it move the outcome metric (OEC) without breaking guardrails? Evidence: controlled rollout or experiment; where accounts are too few for A/B, staged rollout with matched comparison and qualitative follow-up. Report: launch readout comparing treated vs comparison accounts, with pre-agreed success and kill thresholds.
- Q: Who is adopting and who is not, and why? Report: adoption funnel by account and role; qual: calls with non-adopters.

GROW (Decision: where to invest for expansion and retention)
- Q: Which behaviors in the first 30 to 90 days predict retention and expansion? Report: cohort retention by activation behavior (correlation, test causation before acting).
- Q: Why do accounts churn or contract? Evidence: churn reasons from CS notes, usage decline before renewal, NRR by segment.
- Report types: retention cohorts, funnel, account health, NRR bridge (expansion, contraction, churn).

PRICE (Decision: set or change price/packaging)
- Q: Does the value metric track the value customers get? Evidence: correlation of usage units with customer outcomes; bill shock cases. Qual: buyer interviews, Van Westendorp questions.
- Q: What happens to win rate, discount and margin at the new price? Evidence: deal desk data, win/loss, gross margin per unit.
- Report: price-volume-margin view by segment; discount distribution.

RETIRE (Decision: sunset, migrate, keep)
- Q: Who still depends on it, how much revenue and how much cost? Evidence: active accounts, contract terms, support load, maintenance cost. Qual: interviews with top dependents.
- Q: What is the migration path and what is our kill criterion? (Duke, Quit: decide the quit conditions in advance.)
- Report: dependency list by account and ARR; migration progress tracker.

## 4. Report catalog: which report answers which question (no tool mechanics)
- Trend over time with comparison band: "is it changing?"
- Funnel: "where do people drop between steps?"
- Cohort retention table/curve: "do newer groups stick better than older ones?"
- Segment breakdown: "is this true for everyone or only some accounts?"
- Distribution (not average): "are a few accounts driving the total?"
- Experiment/rollout readout: "did our change cause the difference?"
- Account health and NRR bridge: "where is revenue growing and leaking?"
- Theme analysis of text (tickets, calls, reviews): "what are people telling us and how often?"
Each report should state population, time window, metric definition and comparison.

## 5. Framing a question for an AI harness (population, time window, metric definition, comparison)
Template (proposed for the chapter; derived from Anthropic's guidance to give context and purpose, plus the metric card):
- Decision: what we are deciding and by when.
- Question: one sentence.
- Population: which accounts/users, inclusions and exclusions (e.g. paying enterprise accounts live 60+ days, exclude internal and trial tenants).
- Time window: dates, time zone, and whether partial periods are included.
- Metric definition: name the governed definition (semantic layer or metric card) or spell it out: numerator, denominator, unit, filters.
- Comparison: against what (previous period, control, segment, target).
- Evidence types: quant sources and qual sources to cite.
- Output: format, and "show your definitions, filters and the count of records used; flag assumptions; list what would change the answer".
- Check: ask for the same number two ways, or reconcile against a known report.
Rationale: Snowflake and dbt docs both state ungoverned metric definitions are the main failure mode for natural-language analytics; BIRD shows even top systems trail humans.

## 6. Artifacts (proposed formats)
Decision question bank (table): Lifecycle stage | Decision | Question | Quant evidence | Qual evidence | Report | Decision it informs | Owner.

Question brief (one page):
- Decision and date; Type 1 or Type 2
- Question
- Why it matters / what answer would change our mind
- Population, time window, metric definition(s), comparison
- Evidence plan: quant sources, qual sources
- Owner, reviewer, due date
- Confidence needed (Bezos 70% check)

Metric definition card:
- Name; plain-language meaning; why it matters (decision it serves)
- Formula: numerator, denominator, unit
- Population and exclusions; time grain; source of truth (governed definition)
- Owner; last reviewed
- Known caveats and gaming risks; paired guardrail metric
- Good/bad direction; target or threshold

Decision memo (narrative, after Bezos 2017 letter and Decision Quality six elements):
- Decision and recommendation (first)
- Frame: problem, scope, what is out of scope
- Options considered (at least three, including do nothing)
- Evidence: what we know, confidence, what we do not know
- Values and trade-offs: criteria and how weighted
- Reasoning: why this option; pre-mortem; biases checked (Kahneman, Lovallo, Sibony checklist)
- Reversibility: Type 1 or 2; kill criteria and review date (Duke)
- Commitment: owner, resources, who disagreed and committed
- Post-decision review: judge process separately from outcome (Duke)

# (b) Verified facts summary (see source log for URLs)
- [V] Bezos, 2015 letter: Type 1 (one-way door) vs Type 2 (two-way door) decisions; large orgs misuse Type 1 process. SEC filing, April 2016.
- [V] Bezos, 2016 letter: decide with about 70% of the information you wish you had; disagree and commit; resist proxies. SEC filing, April 2017.
- [V] Bezos, 2017 letter: narrative memos, no slides; great memos take a week or more. SEC filing, April 2018.
- [V] Ries, 2009-05-19: vanity vs actionable metrics; cohorts, split tests, per-customer metrics.
- [V] Kahneman, Lovallo, Sibony, HBR June 2011: checklist for detecting bias in team recommendations (items [S]).
- [V] Duke, Thinking in Bets, Portfolio, 2018-02-06: decision quality is separate from outcome.
- [V] Rodden, Hutchinson, Fu, CHI 2010: HEART framework and goals-to-metrics process.
- [V] Torres, 2023-12-06: opportunity solution tree layers.
- [V] Cagan, 2017-12-04: four big risks.
- [V] Andreessen, 2007-06-25: product/market fit definition.
- [V] Brynjolfsson and McElheran, AER 2016: DDD in US manufacturing plants rose from about 11% to 30% (2005 to 2010).
- [S] Strathern 1997 wording of Goodhart's law; Goodhart 1975 original.
- [V] Spetzler, Winter, Meyer, Decision Quality, Wiley 2016; six elements [S].
- [V] Hubbard, How to Measure Anything 3rd ed., Wiley 2014.
- [V] MCP announced 2024-11-25; donated to Linux Foundation's Agentic AI Foundation 2025-12-09; 10,000+ active public servers, 97M+ monthly SDK downloads at that date.
- [V] dbt Semantic Layer reachable by AI tools via the dbt MCP server; Snowflake Cortex Analyst relies on semantic views; Mixpanel MCP server runs funnels, retention, flows in natural language.
- [V, volatile] BIRD: human 92.96% execution accuracy; top system 83.40% at access date.
- [S] Van Westendorp 1976, four price questions.

# (c) Quotes (under 15 words)
1. "Vanity metrics: good for feeling awesome, bad for action." (Eric Ries, 2009, tim.blog)
2. "Type 2 decisions can and should be made quickly" (Jeff Bezos, 2015 letter to shareholders)
3. "around 70% of the information you wish you had" (Jeff Bezos, 2016 letter)
4. "Even the best decision doesn't yield the best outcome every time." (Penguin Random House description of Annie Duke's Thinking in Bets; attribute to the publisher description, not Duke, unless checked in the book)
5. "When a measure becomes a target, it ceases to be a good measure." (Marilyn Strathern, 1997; [S])

# (d) 2025 to 2026 AI-era developments
- MCP became neutral, foundation-governed infrastructure (Linux Foundation AAIF, Dec 2025), with 10,000+ public servers. Analytics, warehouse and semantic-layer vendors ship MCP servers (dbt, Mixpanel verified here). Implication: a PM's harness can query product analytics, warehouse metrics and text sources in one conversation.
- Semantic layers became the guardrail for AI analytics: dbt and Snowflake both state that governed metric definitions are what make natural-language answers trustworthy. Implication: metric definition cards are no longer bureaucracy; they are the input that makes AI answers correct.
- Analytics vendors ship agents that monitor metrics and propose analyses (Amplitude AI Agents). Implication: "what changed?" is automated; "what should we decide?" is not.
- Text-to-SQL accuracy is high but below human experts on hard benchmarks (BIRD). Implication: require the harness to show definitions, filters and record counts; reconcile against a known number.
- Prompting guidance from Anthropic (treat the model as a brilliant new colleague lacking context; give purpose) maps directly onto the question brief.

# (e) Beacon worked example ideas (consistent with beacon-case.md)
1. Question bank across Beacon's live storylines:
   - Discover: "Which incident types do Priya's peers at mid-market MSP customers spend the most responder hours on?" Evidence: incident categories by MTTR and responder count across ~420 customers; Leo-type MSP interviews. Decision: whether to prioritize multi-tenant diagnosis.
   - Invest/Launch (Beacon Agents at Northlight Live): "Among design-partner accounts using supervised remediation for 8+ weeks, did MTTR for allowlisted incident classes fall versus their own prior 8 weeks and versus matched non-pilot accounts, without a rise in wrong-action rate?" Decision: widen autonomy beyond allowlist (Type 1 for production actions, so heavier evidence bar; Sam's audit needs).
   - Build/trust: after the hallucinated root cause that caused a wrong rollback: "What share of accepted diagnoses in the last 90 days were later contradicted by the post-incident review, by service type?" Decision: whether to require a second evidence citation before suggesting rollback.
   - Grow: "Which first-30-day behaviors (connectors installed, runbooks approved, responders active) separate accounts with NRR above 118% from those below?" Decision: onboarding playbook changes.
   - Price (per-resolved-incident): "If we had billed per resolved incident over the last two quarters, how would each account's bill change, and which accounts would see a jump over 20%?" plus Van Westendorp-style buyer interviews with Marcus-type buyers. Decision: pricing transition plan and grandfathering. Also margin: "What is inference cost per resolved incident by incident class?" (margin fell 81% to 72%).
   - Retire (Beacon Classic): "Which accounts still route alerts through Classic, what ARR do they represent, and what blocks their migration?" Decision: sunset date and migration support; kill criteria agreed in advance.
2. Vanity vs good question pair for Beacon: "How many incidents did Beacon touch?" (vanity, rises with alert volume) vs. North Star "incidents resolved with Beacon's help per week" per active account, with guardrail "wrong-action rate" and "diagnosis acceptance then reversal rate".
3. Metric definition card worked example: "Diagnosis acceptance rate": numerator = incidents where responder accepted the agent's root cause; denominator = incidents where Beacon proposed a root cause; population = production environments of paying customers, exclude internal/test tenants; window = weekly, UTC; source = governed definition; guardrail = acceptance later contradicted by post-incident review; gaming risk = UI default nudging "accept".
4. Question brief to the AI harness: the PM (You) asks Claude, through connectors to analytics, ticketing and CRM, the Beacon Agents launch question with population, time window, definitions, comparison, and asks for definitions and record counts back; then the PM spots that trial tenants were included and re-asks.
5. Decision memo: widen autonomous remediation from 3 to 8 allowlisted action types: Type 1 for customers (production), but implement as reversible per-customer toggle to turn it into Type 2 for Northlight; disagree-and-commit with Sam documented; kill criterion: any wrong autonomous action with customer impact pauses the expansion.
Use only beacon-case numbers ($48M ARR, 38% growth, ~420 customers, NRR 118%, margin 81% to 72%). Any other numbers in the example must be clearly illustrative and labeled fictional.

# (f) Editorial flags
- Ries's three A's (actionable, accessible, auditable): not found on Ries's blog posts fetched; source is The Lean Startup (2011) ch. 7. Paraphrase; do not quote until checked against the book.
- Kahneman/Lovallo/Sibony 12 checklist items: article paywalled; item list from memory [S]. Paraphrase loosely or verify.
- "Resulting" as Duke's term: in Thinking in Bets, but not on the fetched publisher page [S].
- How to Decide (2020) publication details not verified (PRH URL 404).
- Sean Ellis 40% benchmark and question wording not on fetched page [S]; present as a rule of thumb, B2B caveat.
- Lean Analytics good-metric criteria and Decisive WRAP steps [S].
- Hubbard's value-of-information and "measurement is uncertainty reduction" framing [S], not on Wiley page.
- Decision Quality attribution: Wikipedia credits Howard and Raiffa; SDG/Spetzler popularized the six-element chain. Attribute carefully.
- BIRD leaderboard values change; the top entry date (2026-10-22) is as reported by the fetch; cite "at time of writing" or use only human baseline.
- Brynjolfsson productivity effect (often cited as 5 to 6%) is from a companion paper not verified here; do not use the number.
- Amplitude AI Agents launch date not verified.
- No verified source found for the question-framing template (population, time window, metric definition, comparison); present it as the book's own synthesis, supported by Anthropic, dbt and Snowflake guidance.
- WebSearch was unavailable in this run (budget exhausted); a later pass could verify the flagged items.
