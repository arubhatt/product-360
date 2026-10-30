# Research notes: Chapter 23, Implementing, Evaluating and Scaling Innovation

Status: complete first pass (2026-10-30). Tags: [V] verified on primary source, [S] secondary only, [U] unverified.
Process note: the shared WebSearch budget for this run was exhausted at the start, so sources were fetched directly from known primary URLs with WebFetch. No search engine was used.

## Sources log (as gathered)

### 1. O'Reilly, C. A. and Tushman, M. L. "The Ambidextrous Organization." Harvard Business Review, April 2004. [V for title, authors, date only]
URL: https://hbr.org/2004/04/the-ambidextrous-organization
- HBR preview confirms authors (O'Reilly, Stanford GSB; Tushman, HBS), April 2004, and the Janus framing (watch the past and the future at once). Study details not visible on the preview page; see later entries.
- Paywalled. Study figures commonly cited from this article (35 breakthrough attempts in 15 business units; ambidextrous designs succeeding over 90% of the time) could NOT be verified on a primary page this run. See editorial flags.

### 2. Wikipedia. "Organizational ambidexterity." (accessed 2026-10-30) [S]
URL: https://en.wikipedia.org/wiki/Organizational_ambidexterity
- Exploration (search, experimentation, innovation) vs exploitation (refinement, efficiency, execution): credited to James G. March, "Exploration and Exploitation in Organizational Learning," Organization Science 2 (1991), 71 to 87. Term "ambidexterity" credited to Robert Duncan (1976).
- Tushman and O'Reilly (1996, California Management Review 38, 8 to 30): ambidextrous firms pursue incremental and discontinuous innovation at the same time by hosting contradictory structures.
- Structural ambidexterity: separate units for exploration and exploitation (Tushman and O'Reilly). Contextual ambidexterity: individuals in one unit split time between alignment and adaptability (Gibson and Birkinshaw, Academy of Management Journal 47, 2004, 41 business units, ambidexterity correlated with performance).
- PM use: structural for Horizon 3 bets that need different economics; contextual for Horizon 1 and 2 bets inside a product team.

### 3. Nagji, B. and Tuff, G. "Managing Your Innovation Portfolio." Harvard Business Review, May 2012. [V for authors and date; matrix details S]
URL: https://hbr.org/2012/05/managing-your-innovation-portfolio
- Monitor Group innovation practice leaders. Problem statement on preview: innovation activity is dispersed, haphazard and episodic, and leaders suspect returns are too low.
- Widely reported content (not visible on preview): Innovation Ambition Matrix with axes "where to play" (existing to new markets/customers) and "how to win" (existing to new products/assets); three zones core, adjacent, transformational; average high performers allocate about 70/20/10 and returns run roughly the inverse (10/20/70). Treat the numbers as [S] and flag; the 70/20/10 is a benchmark of firms in their sample, not a rule.

### 4. Govindarajan, V. and Trimble, C. "Stop the Innovation Wars." Harvard Business Review, July to August 2010. [V for authors, date and summary]
URL: https://hbr.org/2010/07/stop-the-innovation-wars
- Summary on preview: special innovation teams often run into conflict with the rest of the organization.
- Core model (from their book The Other Side of Innovation, Harvard Business Review Press, 2010) [S]: every innovation initiative is a partnership between a Dedicated Team (built for the new work, hired and organized as if from scratch) and the Shared Staff inside the Performance Engine (the existing operation, built for repeatable efficiency). Work is split deliberately: give the shared staff only tasks that fit their routines; anything that conflicts goes to the dedicated team. Leaders must manage the partnership and run a disciplined experiment (formalize hypotheses, review learning separately from performance reviews).
- PM use: decide line by line which Beacon tasks (sales, support, SRE on-call, security review) are shared vs dedicated.

### 5. Blank, S. "Lean Innovation Management: Making Corporate Innovation Work." steveblank.com, 26 June 2015. [V]
URL: https://steveblank.com/2015/06/26/lean-innovation-management-making-corporate-innovation-work/
- Maps McKinsey's three horizons to management methods. H1 execute known model (process, KPIs, stage gate). H2 extend existing model (new channels, customers). H3 search for a new model: small teams (fewer than five), physically separate, Lean Startup tools, own plans, KPIs and incentives.
- Handoff after success: adopted by an H1 unit, grown into a standalone group, or sold or spun out. Proposes a dedicated group to refactor the technical and organizational debt that results.
- "Innovation theater": impressive projects and press releases without change in product trajectory.
- H1 managers must be incentivized to support H2 and H3; support functions (legal, finance, procurement) help innovators get to yes.
- Evidence metrics: activity targets (example: 100+ customer conversations in 10 weeks), Investment Readiness Level and Technology Readiness Level for go/no-go funding.
- Blank's own claim of "10x more initiatives in 1/5 the time" is unsupported in the post; do not repeat as fact.

### 6. Kotter Inc. "The 8 Steps for Leading Change." kotterinc.com (accessed 2026-10-30). [V]
URL: https://www.kotterinc.com/methodology/8-steps/
- Exact step names: 1 Create a Sense of Urgency. 2 Build a Guiding Coalition. 3 Form a Strategic Vision. 4 Enlist a Volunteer Army. 5 Enable Action by Removing Barriers. 6 Generate Short-Term Wins. 7 Sustain Acceleration. 8 Institute Change.
- Evolved from Leading Change (book) into the 8 Accelerators (Accelerate, 2014) and CHANGE (2021). The page does not give the original year; Leading Change is 1996 (Harvard Business School Press) and the HBR article "Leading Change: Why Transformation Efforts Fail" is 1995 [S].
- PM use: a campaign plan for an innovation is a small change program. Steps 1, 2, 4 and 6 map directly to the campaign plan artifact.

### 7. Bezos, J. "2016 Letter to Shareholders." aboutamazon.com, April 2017. [V]
URL: https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders
- Reversible ("two-way door") decisions deserve a lightweight process; one-size-fits-all decision making is the trap.
- Make most decisions with about 70% of the information you wish you had; be good at spotting and correcting bad decisions.
- "Disagree and commit": state objections, then commit quickly (his Amazon Studios example).
- PM use: classify innovation decisions at the portfolio review as two-way (pilot, extend) or one-way (transfer to core, sunset, price change), and match the gate weight to the type.

### 8. Ries, E. "Principles." theleanstartup.com (accessed 2026-10-30). [V]
URL: https://theleanstartup.com/principles
- Innovation accounting: a startup-specific accounting focused on how to measure progress, set milestones and prioritize work.
- Build-Measure-Learn: turn ideas into products, measure customer response, learn whether to pivot or persevere.
- Validated learning is the unit of progress under extreme uncertainty.
- The three-step sequence (establish baseline with an MVP; tune the engine toward the ideal; pivot or persevere) is from The Lean Startup book (Crown Business, 2011) [S]; the page itself mentions tuning the engine and pivot or persevere but not "baseline" as a named step.
- PM use: the innovation portfolio review reports learning metrics per bet (assumptions tested, leading indicators against the plan), not revenue, until the bet reaches scaling.

### 9. Cooper, R. G. / Stage-Gate International. "The Stage-Gate Model: An Overview." stage-gate.com (accessed 2026-10-30). [V]
URL: https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/
- Term first in print 1988. Discovery and Ideation, then Stage 1 Concept (scoping), Stage 2 Build the Business Case, Stage 3 Development, Stage 4 Testing and Validation, Stage 5 Launch, then post-launch review. A gate precedes each stage (five gates).
- Gate structure: deliverables from prior stage, criteria (readiness and business value: Expected Commercial Value, Value-Based Scorecard), outputs Go, Kill, Hold or Recycle. A Go also commits resources, timeline and the next gate date.
- Gatekeepers: senior cross-functional managers who own the resources for the next stage; leadership team at gates 3 to 5 for big projects.
- Newer generations add build-test cycles, rapid customer validation and in-stage sprints; dynamic gates.
- PM use: for innovation bets, keep the gate shape (deliverables, criteria, Go/Kill/Hold/Recycle, resources released) but swap financial criteria for evidence criteria in early gates (see Blank's IRL and Ries).

### 10. McGrath, R. G. and MacMillan, I. C. "Discovery-Driven Planning." Harvard Business Review, July to August 1995. [V for authors, date, premise]
URL: https://hbr.org/1995/07/discovery-driven-planning
- Premise: new ventures need a different planning and control tool; many failures could be avoided or capped.
- Method [S, standard summary]: start from required profit (reverse income statement), list the operations needed (pro forma operations specs), document assumptions (assumptions checklist), and plan milestones at which assumptions are tested before more money is committed.
- PM use: the backbone of a funding model that releases money per milestone (metered funding) rather than annual budget.

### 11. Estrada, S. "MIT report: 95% of generative AI pilots at companies are failing." Fortune, 18 August 2025, reporting MIT NANDA "The GenAI Divide: State of AI in Business 2025" (lead author Aditya Challapally). [S]
URL: https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
- Method: 150 leader interviews, survey of 350 employees, analysis of 300 public AI deployments.
- About 5% of AI pilots achieve rapid revenue acceleration; the rest stall with little measurable P&L impact.
- Buying from specialized vendors and partnering succeeds about 67% of the time; internal builds about one third as often.
- More than half of GenAI budgets go to sales and marketing tools; biggest ROI found in back-office automation.
- Flag: methodology and "95%" definition were widely criticized; cite as "one widely discussed 2025 study" and give the method.

### 12. BCG. "AI Adoption in 2024: 74% of Companies Struggle to Achieve and Scale Value." Press release, 24 October 2024. [V]
URL: https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value
- Survey of 1,000 CxOs and senior executives, 59 countries, 20+ sectors. 74% have yet to show tangible value from AI. 4% cutting-edge, plus 22% beginning to realize substantial gains (26% leaders).
- BCG "70-20-10 principle" for AI: 70% of effort on people and processes, 20% technology and data, 10% algorithms. (Do not confuse with Nagji and Tuff's 70/20/10 portfolio split.)

### 13. BCG. "The Widening AI Value Gap" (Build for the Future 2025). bcg.com, 30 September 2025. [V]
URL: https://www.bcg.com/publications/2025/are-you-generating-value-from-ai-the-widening-gap
- 5% of firms "future-built"; 35% scaling and beginning to generate value; 60% achieve hardly any material value.
- Future-built firms: five times the revenue increases and three times the cost reductions from AI.
- Agents about 17% of total AI value in 2025, projected 29% by 2028. Future-built firms put 15% of AI budgets into agents; a third of them use agents vs 12% of scalers.
- Survey size not stated on the page.
- PM use: scaling, not piloting, is the bottleneck; the chapter's scale-up readiness checklist addresses this directly.

### 14. Mind Tools. "Stakeholder Analysis." mindtools.com (accessed 2026-10-30), adapting Mendelow (1981). [V for Mind Tools text; Mendelow original S]
URL: https://www.mindtools.com/aol0rms/stakeholder-analysis
- Power/interest grid. High power, high interest: Manage Closely. High power, less interest: Keep Satisfied. Low power, high interest: Keep Informed (they often help with detail). Low power, less interest: Monitor.
- Three steps: identify, prioritize (plot on grid), understand key stakeholders (interests, motivations, current opinion, who influences them, how to win support).
- Attribution: Mendelow, A. L. (1981), "Environmental Scanning: The Impact of the Stakeholder Concept," ICIS 1981 Proceedings. Note: many sources say 1991 (a later Mendelow paper); use 1981 for the ICIS origin and flag.
- PM use for innovation: the classic grid is static. For innovation add two columns: current stance (champion, supporter, neutral, skeptic, blocker) and what they lose if the innovation succeeds (budget, headcount, status, risk exposure). Innovation threats come from people whose performance engine metrics get worse.

### 15. Working Backwards LLC. "Working Backwards PR/FAQ Process." workingbackwards.com (accessed 2026-10-30). [V]
URL: https://workingbackwards.com/concepts/working-backwards-pr-faq-process/
- Press release: Heading; Subheading (one sentence, customer and benefit); Summary (city, outlet, launch date, product and benefits); Problem (customer's view, big enough to matter); Solution (how it solves it, better, faster or cheaper than today); Quotes and Getting Started (spokesperson quote, hypothetical customer quote, how to start).
- FAQ: External (price, how it works, support, where to buy) and Internal (TAM, competition, unit economics, upfront investment, risks, regulation, third-party dependencies, assumptions required for success, top reasons it could fail).
- Review: solo draft (often a PM), feedback, initial review (about 10 contributors plus decision maker), executive review over several drafts. Meeting: 15 to 20 minutes silent reading, about 40 minutes discussion, aim is truth-seeking not selling. Outcome go/no-go.
- Source book: Bryar, C. and Carr, B. Working Backwards. St. Martin's Press, 2021 [S]. The book also describes the "single-threaded leader" model (a leader whose only job is one initiative, with a separable team) [S].
- PM use: the innovation pitch outline uses the internal FAQ list as the executive Q and A appendix; the single-threaded leader is the practical form of a dedicated team.

### 16. EU AI Act, Article 57 "AI Regulatory Sandboxes." artificialintelligenceact.eu (accessed 2026-10-30). [V on secondary host of the legal text; date conflict flagged]
URL: https://artificialintelligenceact.eu/article/57/
- Each member state must have at least one national AI regulatory sandbox. Regulation (EU) 2024/1689 as adopted says operational by 2 August 2026; the page also shows amended text saying 2 August 2027 (likely the Digital Omnibus amendment). Flag and check the Official Journal before stating a date.
- Sandboxes: controlled environment to develop, test and validate AI for a limited time before market placement. Participants get written proof of completed activities and an exit report that conformity assessors must take into account. Good-faith participants following the sandbox plan face no administrative fines under the Act (still liable for third-party damage). Priority access for SMEs and start-ups (and small mid-caps in amended text).
- PM use: an example of an external policy that helps innovation; internally, mirror it with a "sandbox policy" (bounded customers, bounded data, explicit exit report).

### 17. Schluntz, E. and Zhang, B. "Building Effective Agents." Anthropic Engineering, 19 December 2024. [V]
URL: https://www.anthropic.com/engineering/building-effective-agents
- Start with the simplest solution that works; workflows (predefined paths) vs agents (model directs its own steps and tool use). Add complexity only when it demonstrably improves outcomes; let evals decide.
- PM use: a scale-up readiness check for AI innovations should ask whether the pilot used more autonomy than the job needs, because complexity raises cost and compounds errors at scale.

### 18. O'Reilly, C. A. and Tushman, M. L. Lead and Disrupt: How to Solve the Innovator's Dilemma. Stanford Business Books, March 2016 (second edition 2021 [S]). [V for 2016 edition page]
URL: https://www.gsb.stanford.edu/faculty-research/books/lead-disrupt-how-solve-innovators-dilemma
- Ambidexterity: compete in mature core markets (efficiency, control, incremental change) while winning in new domains (flexibility, autonomy, experimentation).
- Explicitly more optimistic than Christensen that incumbents can survive disruption; needs both top-down and bottom-up leadership; based on a decade-plus research program and field work.
- Commonly summarized conditions for ambidexterity [S]: a compelling strategic intent that justifies exploration; explicit senior-team commitment and funding; structurally separate exploratory units with their own alignment (people, structure, culture, metrics) plus targeted integration with the core where the new unit can leverage assets (customers, brand, data, channels); a common identity across units; leaders who can hold the tension. Use as a checklist, flag as S.
- PM use: the key design question is "what does the explore unit borrow from the core, and how is that borrowing governed?" For Beacon in 2023 to 2024 that was Observe data and Northlight's sales force.

### 19. Ries, E. The Startup Way. Currency (Penguin Random House), October 2017. [V for title, author, year]
URL: https://www.thestartupway.com/
- Media coverage on the site frames the idea of an "entrepreneurship function" to sustain corporate innovation.
- Book concepts [S, not verified on primary page this run]: metered funding (fund teams in small increments tied to validated learning, like venture rounds), growth boards (a small internal board that reviews a team's evidence and decides on the next tranche), and innovation accounting in three levels (dashboard of leading indicators; business-model drivers; net present value). Flag as S.
- PM use: the funding model section of the chapter; Beacon's "Agents" bet could run on metered tranches tied to diagnosis acceptance and autonomous resolution evidence.

### 20. Stanford HAI. "The 2025 AI Index Report." hai.stanford.edu, 2025 (released April 2025 [S]). [V]
URL: https://hai.stanford.edu/ai-index/2025-ai-index-report
- 78% of organizations reported using AI in 2024, up from 55% the year before.
- Inference cost for a GPT-3.5-level system fell more than 280-fold between November 2022 and October 2024; hardware costs down 30% per year; energy efficiency up 40% per year.
- PM use: unit economics of an AI innovation change quickly; scale-up business cases need a cost curve assumption, not a fixed inference cost (ties to Beacon's margin drop from 81% to 72%).

### 21. DORA (Google Cloud). "State of AI-assisted Software Development 2025." dora.dev, 2025. [V for framing]
URL: https://dora.dev/research/2025/dora-report/
- Central claim: AI acts as an amplifier of an organization's existing strengths and weaknesses; the biggest returns come from focusing on the underlying organizational system, not the tools.
- Report includes a companion "DORA AI Capabilities Model" (seven capabilities; names not visible on the landing page, not verified).
- PM use: supports the chapter's claim that supporting policies and operating model, not models, decide whether AI innovation scales.

### 22. Wikipedia. "John A. List." (accessed 2026-10-30) [S]
URL: https://en.wikipedia.org/wiki/John_A._List
- List published The Voltage Effect in February 2022 (Crown). Frames scaling as an "Anna Karenina problem": scalable ideas share traits; unscalable ones fail in their own ways.
- The book's "five vital signs" of scalability were NOT verified this run; see flags.

### 23. Teller, A. "Tackle the Monkey First." X, the moonshot factory blog, 8 December 2016. [V]
URL: https://x.company/blog/posts/tackle-the-monkey-first/
- Thought experiment: to get a monkey reciting Shakespeare on a pedestal, teams build the pedestal first because it is easy to show progress, while the monkey is the real risk. Work the hardest, most uncertain part first.
- Example: Foghorn team (seawater to carbon-neutral fuel) could not show cost competitiveness within five years and ended its own project so resources could move to better bets.
- PM use: kill criteria are written against the "monkey" (the riskiest assumption), not the pedestal. Rewarding teams that kill their own projects is a supporting policy.

### 24. Anthropic. "Introducing the Model Context Protocol." anthropic.com, 25 November 2024. [V]
URL: https://www.anthropic.com/news/model-context-protocol
- Open standard for connecting AI assistants to data sources and tools via MCP servers and clients; replaces one-off connectors.
- PM use: the AI harness can pull portfolio evidence (usage, pipeline, support tickets, eval results) through connectors to draft the portfolio review; Beacon itself uses MCP connectors to customer systems.

### 25. Duke, A. Quit: The Power of Knowing When to Walk Away. annieduke.com (book page). [V for title]; Portfolio (Penguin Random House), 2022 [S]
URL: https://www.annieduke.com/books/
- Book idea [S]: set kill criteria in advance as "states and dates" (if by a given date we have not reached a given state, we stop), because in the moment people escalate commitment. Duke also discusses Teller's monkeys and pedestals.
- PM use: every bet in the innovation portfolio carries a pre-committed state-and-date kill line, agreed at the gate that funds it.

---

## (a) Key concepts and frameworks for the chapter

1. Exploration vs exploitation (James G. March, 1991). Two kinds of learning that compete for the same resources; exploitation's returns are surer and nearer, so it crowds out exploration unless leaders protect it. Applies to any PM who owns both a growing core and a new bet.

2. Ambidextrous organization (Charles O'Reilly and Michael Tushman, 1996 CMR; 2004 HBR; Lead and Disrupt, 2016). Structurally separate explore units with their own alignment (people, metrics, culture, processes), integrated at the senior team, with targeted links to core assets, under a strategic intent that justifies both. Contextual ambidexterity (Gibson and Birkinshaw, 2004) is the alternative where individuals split time. B2B application: decide what the new unit borrows from the core (customers, data, sales channel, brand, compliance certifications) and who governs each borrowing. Template idea for the chapter: an "explore and exploit alignment table" with rows (strategic intent, critical tasks, people and skills, structure, metrics and rewards, culture, leadership) and two columns (core, new).

3. Dedicated Team plus Performance Engine (Vijay Govindarajan and Chris Trimble, 2010). Innovation = partnership between a dedicated team and the shared staff in the performance engine. Split the work so shared staff only do tasks compatible with their routines; build the dedicated team "from scratch" (hire outsiders, new metrics, new roles); run the initiative as a disciplined experiment with learning reviews separate from performance reviews. B2B application: in enterprise software the classic conflicts are sales comp (reps will not sell a small new SKU), support (tier 1 cannot answer agentic questions), security review queues, and the release train.

4. Single-threaded leader (Amazon practice, described by Colin Bryar and Bill Carr, Working Backwards, 2021) [S]. One leader, one initiative, a team that is as separable as possible. The practical minimum of a dedicated team.

5. Stakeholder power and interest grid (Aubrey Mendelow, 1981; popularized by Mind Tools). Manage Closely, Keep Satisfied, Keep Informed, Monitor. For innovation extend it into an innovation stakeholder map with columns: name and role; power (H/M/L); interest (H/M/L); current stance (champion, supporter, neutral, skeptic, blocker); what they gain if it works; what they lose (budget, headcount, metric, risk); evidence that would move them; owner and next touch. The "what they lose" column is the innovation-specific addition and is the chapter's original contribution, not a sourced framework.

6. Internal campaign plan (adapting John Kotter's 8 steps). Urgency, guiding coalition, vision, volunteer army, remove barriers, short-term wins, sustain acceleration, institute change. Campaign plan template for the chapter (original synthesis): objective and decision needed; audiences by segment from the stakeholder map; message per audience (their problem, the evidence, the ask); proof points and short-term wins scheduled; channels and moments (exec staff meeting, QBRs, all-hands demo, customer advisory board); coalition members and their roles; objections log; milestones and measures of support.

7. Three horizons (Mehrdad Baghai, Stephen Coley and David White, The Alchemy of Growth, 1999 [S]) mapped to management systems by Steve Blank (2015): H1 execute the known model with KPIs and stage gate; H2 extend the model; H3 search for a new model with small separate teams, Lean tools, own KPIs and incentives. Handoff paths after success: adopt into H1, grow standalone, or sell or spin out.

8. Innovation Ambition Matrix and 70/20/10 (Bansi Nagji and Geoff Tuff, 2012) [S for numbers]. Core, adjacent, transformational along "where to play" and "how to win" axes. Their benchmark: high performers allocated about 70% core, 20% adjacent, 10% transformational, while returns ran roughly 10/20/70. Use as a reference point that each firm sets for itself, not a target.

9. Innovation accounting (Eric Ries, The Lean Startup 2011; The Startup Way 2017). Measure validated learning; establish a baseline, tune the engine, pivot or persevere. Corporate extension [S]: metered funding and growth boards; three levels of metrics from leading indicators to business-model drivers to financial value.

10. Stage-Gate (Robert G. Cooper, first in print 1988). Stages separated by gates with deliverables, criteria, and Go, Kill, Hold or Recycle outputs; gatekeepers own the resources. For innovation, keep the gate discipline but change the criteria by stage: early gates on evidence (problem, solution fit, willingness to pay, riskiest assumption retired), late gates on business case. Blank's Investment Readiness Level is the evidence-based alternative [S: level definitions not verified].

11. Discovery-driven planning (Rita McGrath and Ian MacMillan, 1995). Reverse income statement, operations specs, assumptions checklist, milestone plan. The milestone plan defines when assumptions get tested and when the next tranche is released.

12. Kill criteria. Annie Duke's states and dates (Quit, 2022) [S]; Astro Teller's monkey first (2016). Template line: "We stop [bet] if by [date] we have not shown [state, measured as], unless [named exception]. Decided by [forum]." Supporting policy: celebrate teams that kill their own projects (X Foghorn example).

13. Scaling from pilot to product. Two-part question: does the result hold at scale (John List, The Voltage Effect, 2022, frames this as many independent ways to fail; specific vital signs not verified), and can the organization absorb it (transfer to core). Transfer options (Blank): absorb into an H1 unit, keep as a standalone unit, or sell or spin out. Funding options: corporate innovation budget, metered funding by a growth board, core business unit takes it into its plan, or new P and L. Beacon's own history (feature in Observe 2023, standalone product 2024) is a reverse example: a feature that grew out of the core.

14. Sustaining after scale. Christensen Institute defines sustaining innovation as improvements that keep the current trajectory of competition. Once a scaled innovation becomes core, it moves to H1 management: KPIs, roadmap, release train, and its own sustaining roadmap. The risk is that the explore unit's capabilities (rapid experiment loops, eval discipline, direct customer access) dissolve on transfer. Mitigation: keep a small explore cell, write an exit report (borrowing the EU AI Act sandbox idea), and keep the innovation metrics running for two or three quarters after transfer.

15. Pitching the plan (the eCornell "placemat"). A one-page view of the innovation plan for executives. Combine with the PR/FAQ (Working Backwards): customer problem, solution, why now, evidence to date, ask (money, people, policy exceptions), kill criteria, scale path. Review norm: silent read then discussion, truth-seeking over selling. Bezos 2016 letter: classify two-way vs one-way door decisions; decide with about 70% of the information.

16. AI lens. Most AI innovation stalls between pilot and scale (BCG 2024: 74% without tangible value; BCG 2025: 60% with hardly any material value; MIT NANDA 2025 widely reported 5% of pilots producing rapid revenue acceleration). BCG's 70-20-10 for AI (people and process 70, technology and data 20, algorithms 10) and DORA's "AI as amplifier" both say the operating system around the innovation decides the outcome. Anthropic's agent guidance says add autonomy only when evals show it pays. Inference cost falls fast (Stanford AI Index 2025), so the unit-economics assumption in a scale case should be a curve.

## Artifact templates to build in the chapter (original synthesis; no source claims these exact formats)

- Innovation stakeholder map: table as in concept 5 plus a one-line "coalition gap" summary.
- Campaign plan: as in concept 6, one page, with a dated calendar of short-term wins.
- Innovation portfolio review: one row per bet with horizon (H1 to H3) or zone (core, adjacent, transformational); stage; riskiest assumption; evidence since last review; leading indicator vs plan; spend to date and next tranche asked; kill line (state and date); decision (continue, pivot, scale, kill). Portfolio summary: allocation vs target mix, number of kills (a healthy portfolio kills some), learning velocity (assumptions retired per quarter).
- Scale-up readiness checklist: evidence holds outside pilot customers (representative segments); unit economics at scale including inference cost; operational readiness (support, SRE, on-call, documentation); go-to-market readiness (pricing, SKU, sales comp, partner enablement); compliance and risk (security review, AI risk documentation, data residency, audit logs); receiving owner named with budget in their plan; integration debt listed with an owner; metrics and evals that continue after transfer; sunset plan for anything it replaces.
- Innovation pitch outline (placemat): headline and customer; problem and why now; what we learned (evidence); the bet and the business model; the ask (money, people, policy exceptions); milestones with tranche release; kill criteria; scale path and receiving owner; risks and internal FAQ appendix.

## (b) Verified facts with URL and date

- [V] O'Reilly and Tushman, "The Ambidextrous Organization," HBR, April 2004. https://hbr.org/2004/04/the-ambidextrous-organization
- [V] Lead and Disrupt, Stanford Business Books, March 2016; argues incumbents can survive disruption through ambidexterity, contra Christensen's pessimism. https://www.gsb.stanford.edu/faculty-research/books/lead-disrupt-how-solve-innovators-dilemma
- [S] March 1991 Organization Science 2, 71 to 87 coined the exploration vs exploitation framing; Gibson and Birkinshaw 2004 studied 41 business units. https://en.wikipedia.org/wiki/Organizational_ambidexterity
- [V] Nagji and Tuff, HBR, May 2012, Monitor Group. https://hbr.org/2012/05/managing-your-innovation-portfolio (70/20/10 and 10/20/70 numbers [S])
- [V] Govindarajan and Trimble, "Stop the Innovation Wars," HBR, July to August 2010. https://hbr.org/2010/07/stop-the-innovation-wars
- [V] McGrath and MacMillan, "Discovery-Driven Planning," HBR, July to August 1995. https://hbr.org/1995/07/discovery-driven-planning
- [V] Kotter 8 step names. https://www.kotterinc.com/methodology/8-steps/
- [V] Stage-Gate first in print 1988; five stages, five gates; Go, Kill, Hold, Recycle. https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/
- [V] Blank 2015: H3 teams fewer than five people, physically separate; "innovation theater"; handoff options. https://steveblank.com/2015/06/26/lean-innovation-management-making-corporate-innovation-work/
- [V] Bezos 2016 letter: about 70% of information; disagree and commit; two-way doors. https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders
- [V] PR/FAQ structure and review meeting (15 to 20 minutes reading, about 40 minutes discussion). https://workingbackwards.com/concepts/working-backwards-pr-faq-process/
- [V] Teller, monkey first, 8 December 2016; Foghorn ended. https://x.company/blog/posts/tackle-the-monkey-first/
- [V] BCG, 24 October 2024: 1,000 executives, 59 countries; 74% no tangible AI value; 70-20-10 principle. https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value
- [V] BCG, 30 September 2025: 5% future-built, 60% hardly any value; agents 17% of AI value in 2025, 29% by 2028. https://www.bcg.com/publications/2025/are-you-generating-value-from-ai-the-widening-gap
- [S] MIT NANDA via Fortune, 18 August 2025: 150 interviews, 350 surveyed, 300 deployments; about 5% of pilots achieve rapid revenue acceleration; vendor purchases succeed about 67% vs internal builds about a third as often. https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
- [V] Stanford AI Index 2025: 78% of organizations used AI in 2024 (55% in 2023); GPT-3.5-level inference cost down more than 280-fold Nov 2022 to Oct 2024. https://hai.stanford.edu/ai-index/2025-ai-index-report
- [V] DORA 2025: AI as amplifier of existing strengths and weaknesses. https://dora.dev/research/2025/dora-report/
- [V] Anthropic, Building Effective Agents, 19 December 2024. https://www.anthropic.com/engineering/building-effective-agents
- [V] Anthropic, MCP announced 25 November 2024. https://www.anthropic.com/news/model-context-protocol
- [V, date conflict] EU AI Act Article 57 sandboxes; exit reports; no administrative fines for good-faith participants. https://artificialintelligenceact.eu/article/57/

## (c) Quotes (under 15 words)

1. "If you wait for 90%, in most cases, you're probably being slow." Jeff Bezos, 2016 Letter to Shareholders.
2. "consider adding complexity only when it demonstrably improves outcomes." Schluntz and Zhang, Anthropic, Building Effective Agents, 2024.
3. "AI's primary role is as an amplifier." DORA, State of AI-assisted Software Development 2025.
4. Special innovation teams "inevitably run into conflict with the rest of the organization." Govindarajan and Trimble, HBR, 2010 (article summary).
5. "Hey, nice pedestal, great job!" Astro Teller, Tackle the Monkey First, 2016 (the boss's misplaced praise).

## (d) 2025 to 2026 AI-era developments

- Pilot-to-scale gap is the defining AI innovation problem: BCG September 2025 (60% hardly any value, 5% future-built); BCG October 2024 (74% no tangible value); MIT NANDA August 2025 (widely reported 95% of pilots without measurable P and L impact, contested).
- Agentic AI share of value rising: BCG 2025 estimates agents at about 17% of AI value in 2025, 29% by 2028.
- Gartner predictions often cited: over 40% of agentic AI projects canceled by end of 2027 (June 2025) and 30% of GenAI projects abandoned after proof of concept by end of 2025 (July 2024). Primary pages returned 403 this run: [U], do not use without verification.
- Cost curve: inference costs fall steeply (AI Index 2025), so kill criteria based on unit economics need a date and a cost assumption, and a bet killed on cost may deserve a re-check later.
- Connectors and MCP (since November 2024) let a PM's AI harness assemble portfolio evidence from many systems; the PM still owns the judgment and the kill call.
- Regulation as a supporting policy: EU AI Act regulatory sandboxes (Article 57), with exit reports; amended timelines under discussion (2026 vs 2027).
- AI as amplifier (DORA 2025): organizational system (platform, practices, policy) decides whether AI innovation pays.

AI harness uses for the chapter (practice guidance, not sourced claims): ask the harness to draft the stakeholder map from meeting notes, CRM and org chart via connectors, then the PM corrects stances; draft per-audience campaign messages from one evidence pack; assemble the portfolio review from usage, pipeline, eval and cost reports and highlight bets that crossed or missed their kill lines; red-team the pitch by asking the harness to play the CFO, the head of sales and the security reviewer and list their hardest questions; check the scale-up readiness checklist against real evidence links, flagging items with no evidence. Guardrail: the harness must cite where each number came from; no number enters a pitch without a source.

## (e) Beacon worked example ideas (consistent with beacon-case.md)

- Origin story as ambidexterity: Beacon began in 2023 as an AIOps correlation feature inside Northlight Observe and spun out in 2024. Use it to show a "grow out of the core" path and what Beacon still borrows from Observe (telemetry data, the Northlight sales force, security certifications). The strategic tension (build on Observe data vs stay tool-agnostic) is a targeted-integration choice.
- The innovation now: Beacon Agents (supervised remediation) and the per-resolved-incident price. Treat Agents as an H2/H3 bet inside a business growing 38% with NRR 118%.
- Stakeholder map: Priya (champion, customer side), Marcus (economic buyer), Sam (security gatekeeper, Manage Closely), the VP of Product (sponsor), the Observe and Desk group PMs (peers who may lose roadmap share or data priority), Northlight sales leadership (comp plans built on per-environment pricing; loses predictability with per-incident pricing), finance (worried about gross margin falling from 81% to 72%), support and customer success (new agentic escalations), Leo the MSP partner (wants multi-tenant billing). The "what they lose" column is where the drama sits.
- Campaign plan: short-term wins scheduled before Northlight Live (design-partner results on diagnosis acceptance rate and MTTR); guiding coalition of the VP of Product, a sales leader, a security leader and two design-partner customers; objections log includes the hallucinated root cause incident and how evals now catch it.
- Dedicated team: one of Beacon's five engineering teams plus the 2 applied AI engineers form the Agents team with a single-threaded leader; shared staff are Northlight sales, support, security review and the release train. Policies needed: a sales comp exception for per-incident pricing pilots, a fast-path security review for allowlisted low-risk actions, a design-partner contract template with a data-use clause for evals.
- Portfolio review: Beacon's bets across horizons, for example H1 Correlate improvements and the Beacon Classic sunset; H2 Diagnose expansion to new connectors and the MSP multi-tenant offer; H3 autonomous remediation beyond allowlisted actions. Each with a state-and-date kill line (example only, numbers to be invented in-chapter and labelled fictional): autonomous remediation stops if by end of Q2 autonomous resolution rate on allowlisted actions is below target or any severity-one incident is caused by an agent action.
- Scale-up readiness: Agents moving from design partners to general availability at Northlight Live: evals in place after the hallucinated root cause, AI Act documentation for EU customers, audit logs for Sam, support runbooks, pricing and billing ready for per-resolved-incident, gross margin plan accounting for inference cost trend.
- Pitch: a one-page placemat to the Northlight executive team asking for tranche-based funding of Agents, a pricing pilot exception and the fast-path security policy, with the internal FAQ as appendix (margin, cannibalization of per-environment revenue, Observe dependency, AI risk).

## (f) Editorial flags

- O'Reilly and Tushman 2004 study figures (35 breakthrough innovations in 15 business units; over 90% success for ambidextrous designs vs far lower for other designs) not verified on a primary page: HBR paywall. Do not cite numbers unless verified.
- Nagji and Tuff 70/20/10 allocation and 10/20/70 returns: secondary only. If used, present as their 2012 benchmark from the companies they studied.
- Govindarajan and Trimble model details (Dedicated Team, Shared Staff, Performance Engine): only the HBR summary verified; book details [S]. Concept names are well established.
- Christensen and Overdorf 2000 Resources, Processes and Values: only authors and date verified; RPV framework details [S].
- Three Horizons original book (Baghai, Coley, White, The Alchemy of Growth, 1999): McKinsey page timed out; [S].
- Ries metered funding, growth boards and three-level innovation accounting: from The Startup Way, not verified on a primary page.
- Blank's Investment Readiness Level levels not verified (post URL 404); mention only as named.
- Mendelow date: Mind Tools cites 1981 (ICIS Proceedings); many sources cite 1991. Use 1981 with Mind Tools as the source, or avoid the year.
- The Voltage Effect five vital signs not verified; do not list them.
- MIT NANDA 95% figure is contested and reported via Fortune; Gartner predictions [U] (403).
- EU AI Act Article 57 sandbox deadline: 2 August 2026 in the adopted text vs 2 August 2027 in amended text shown on the same page. Check the Official Journal.
- Amazon single-threaded leader and PR/FAQ history are company practice claims reported by former Amazon executives; attribute to Bryar and Carr.
- eCornell certificate pages did not show the "Implementing Innovation" or "Evaluating and Scaling Innovation" course pages; "placemat" format not verified from eCornell; the chapter's placemat template is original.
- Avoid "Google 20% time" and "3M 15% rule" as examples unless verified on primary sources; not checked this run.
- WebSearch budget was exhausted at the start of this run; sources were reached by direct fetch only. A follow-up pass with search could verify the flagged items.
