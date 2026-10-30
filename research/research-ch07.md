# Research notes: Chapter 07, Navigating Technical Product Management

Status: complete (2026-10-30). Tags: [V] verified on primary source; [S] secondary only; [U] unverified.

## Sources log (running)

1. CB Insights. Why startups fail (2026 analysis). Published 2026-03-05. https://www.cbinsights.com/research/report/startup-failure-reasons-top/ [V]
   - Sample: 431 VC-backed companies that shut down publicly since 2023; reasons identifiable for 385.
   - Ran out of capital 70%; poor product-market fit 43%; bad timing or macro conditions 29%; unsustainable unit economics 19%. Multiple reasons allowed, so totals exceed 100%.
   - CB Insights itself says running out of capital is usually the final cause of death rather than the root problem.
   - Caveats: self-reported post-mortems, founder interviews, shutdown announcements; VC-backed only; post-zero-interest-rate period; excludes companies with a prior exit.
   - Earlier editions (cite only as history, all [S]): 2014 to 2018 analysis of 101 post-mortems, "no market need" cited by 42%; a 2019/2021 "top 12" edition of 111 post-mortems widely reported as ran out of cash or failed to raise 38%, no market need 35%, got outcompeted 20%. I could not reach the CB Insights primary page for either earlier edition. Secondary: SmartCompany https://www.smartcompany.com.au/startupsmart/analysis/startups-fail-founders-capital/ ; CMO Council 2021 https://cmocouncil.org/expert-views/cmo-blog/define-the-need-before-you-bleed-marketing-rigor-can-reduce-start-up-failure

2. Cagan, Marty. The Root Causes of Product Failure. SVPG, 2015-06-05. https://svpg.com/product-fail/ [V]
   - Ten root causes (paraphrased): (1) ideas come from sales and stakeholders, team becomes implementers; (2) business cases demand revenue and cost predictions nobody can know yet; (3) roadmaps are prioritized feature lists, though many features will not deliver and the ones that do take iterations; (4) the product role shrinks to documenting requirements (project management); (5) design arrives too late, only to polish; (6) engineering arrives too late to contribute ideas; (7) agile applied only to delivery; (8) funding projects, not outcomes, leaves orphaned projects; (9) all risk sits at the end, customer validation comes after the build; (10) opportunity cost of the whole process.
   - Alternative: continuous discovery alongside continuous delivery; product, design and engineering collaborate from the start; roadmaps of problems (outcomes) rather than features (outputs).
   - The same material is the "Root Causes of Failed Product Efforts" chapter in INSPIRED, 2nd ed. (Wiley, 2017) [S for chapter title].

3. Cutler, John. 12 Signs You're Working in a Feature Factory. cutle.fish, 2016-11-17. https://cutle.fish/blog/12-signs-youre-working-in-a-feature-factory [V]
   - Signs (paraphrased): no measurement; "team Tetris" (people shuffled between projects without missions); success theater around launches; rare failures or scrapped work; work disconnected from core metrics; no PM retrospectives on decisions; prioritization obsession with no checking afterward, roadmaps of features not goals; no tweaking after launch; hand-offs (team excluded from research and from post-release contact with support, CS, sales); large batches; chasing upfront revenue with deal-driven features that ignore complexity costs; shiny objects (debt and refactoring invisible).
   - Follow-up: Cutler, "12 Signs You're Working in a Feature Factory, 3 Years Later," Amplitude blog (about 2019; page shows no date [U for exact date]). https://amplitude.com/blog/12-signs-youre-working-in-a-feature-factory-3-years-later Key point: teams fall in through good intentions (for example locking a roadmap early to protect overloaded designers); OKRs and fixed roadmaps can over-constrain teams; lower WIP; learning-focused measurement.

4. Cooper, Robert G. Stage-Gate. Term first in print 1988 [S]. Cooper talk summary: "The Evolution of StageGate: Integrating Agile and Lean for New Product Development," Syracuse University Whitman/Snyder Center, undated (2023 or later). https://snyder.syracuse.edu/snyder/the-evolution-of-stagegate-integrating-agile-and-lean-for-new-product-development/ [V for Cooper's own framing via event write-up]
   - Cooper frames Stage-Gate as an information model to reduce uncertainty and manage risk, and as an investment model, not a project-management tool. Stages gather information (market research, lab tests); gates are management reviews deciding continue, stop or redirect (commonly go, kill, hold, recycle [S]). Typical five stages plus gates [S].
   - Variants: StageGate Lite, TD (technology development), versions for AI development. Agile StageGate: sprints inside stages (software about two weeks; physical products one to three months), with planning, build, customer test, management demo and retrospective.
   - Known failure mode [S]: gates that never kill, clogging the pipeline. Linear model struggles with real loops.

5. Royce, Winston W. Managing the Development of Large Software Systems. Proceedings, IEEE WESCON, August 1970, pp. 1 to 9. PDF copy: https://faculty.washington.edu/hazeline/misc/reserve/royce_waterfall.pdf [V, text extracted]
   - Royce presents the sequential model and then writes that the implementation "is risky and invites failure."
   - His five fixes: Step 1 program design comes first; Step 2 document the design; Step 3 do it twice (build a pilot); Step 4 plan, control and monitor testing; Step 5 involve the customer formally.
   - Teaching point: "waterfall" as practiced is a caricature of the paper; Royce never used the word "waterfall" [S, widely reported; the word does not appear in the extracted text headings, but verify full text before claiming].

6. Beck, Kent et al. Manifesto for Agile Software Development. 2001. https://agilemanifesto.org/ and https://agilemanifesto.org/principles.html [V]
   - Four values: individuals and interactions over processes and tools; working software over comprehensive documentation; customer collaboration over contract negotiation; responding to change over following a plan. Twelve principles (early and continuous delivery, welcome changing requirements, frequent delivery, daily business and developer collaboration, motivated individuals, face-to-face conversation, working software as measure of progress, sustainable pace, technical excellence, simplicity, self-organizing teams, regular reflection).

7. Sy, Desirée. Adapting Usability Investigations for Agile User-Centered Design. Journal of Usability Studies 2(3), May 2007, pp. 112 to 132. https://uxpajournal.org/adapting-usability-investigations-for-agile-user-centered-design/ [S via search abstract; journal page exists]
   - Origin of the two-track idea: interaction designers work at least one cycle ahead of developers in a separate track.

8. Patton, Jeff. Dual Track Development is not Duel Track. Jeff Patton & Associates, 2017-05-10, updated 2023-04-12. https://www.jpattonassociates.com/dual-track-development/ [V]
   - One process, two kinds of concurrent, continuous work: discovery (learn fast, validate) and development (predictable, high quality). Whole team takes part in discovery, not only PM and design. Good discovery kills or changes many ideas. Learning continues after release.
   - Quote: "The whole team is responsible for product outcomes, not just on-time delivery."

9. Kohavi, Ron; Tang, Diane; Xu, Ya. Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing. Cambridge University Press, 2020. Chapter "Sample Ratio Mismatch and Other Trust-Related Guardrail Metrics," pp. 219 to 225. https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/sample-ratio-mismatch-and-other-trustrelated-guardrail-metrics/8DBB0F59AC7729D7BC6B94690DB9CCD5 [V for chapter existence and abstract; S for wording of Twyman's law]
   - Concepts: Overall Evaluation Criterion (OEC), a quantitative measure of the experiment's objective, ideally predictive of long-term value; guardrail metrics, of two types: organizational (for example latency, errors, cost) and trust-related (for example SRM), alerting experimenters to violated assumptions; the SRM check belongs on every experiment.
   - Twyman's law: a figure that looks interesting or different is usually wrong (paraphrase; exact book wording not verified [S]).

10. Kohavi, Ron and Thomke, Stefan. The Surprising Power of Online Experiments. Harvard Business Review 95(5), September to October 2017, pp. 74 to 82. Landing page: https://exp-platform.com/hbr-the-surprising-power-of-online-experiments/ [V for citation only]
   - Widely reported (from the article) that experimentation helped Bing find dozens of monthly revenue improvements raising revenue per search 10% to 25% a year [S: seen only in a fragmentary reprint]. Do not use the famous Bing headline figures unless the chapter author checks the full article.

11. Fabijan, Aleksander et al. Diagnosing Sample Ratio Mismatch in Online Controlled Experiments: A Taxonomy and Rules of Thumb for Practitioners. KDD 2019. https://www.microsoft.com/en-us/research/publication/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments-a-taxonomy-and-rules-of-thumb-for-practitioners/ [V for definition and venue]
   - SRM definition: the observed sample ratio differs from the expected one. SRM is a symptom of data quality problems; drawn from experience at four software companies.
   - "About 6% of experiments at Microsoft exhibit an SRM" is quoted in secondary material from the paper [S]; not on the abstract page.

12. Miller, Evan. How Not To Run an A/B Test. evanmiller.org, 2010-04-18. https://www.evanmiller.org/how-not-to-run-an-ab-test.html [V]
   - Peeking: significance formulas assume a sample size fixed in advance. Stopping at the first significant reading inflates false positives. His illustration: with a no-effect change, checking repeatedly and stopping at 5% significance yields roughly a 26% false positive rate. Peeking ten times turns a nominal 1% into roughly 5%.
   - Fixes: fix the sample size in advance; or use a sequential design with planned checkpoints; or a Bayesian design. Report significance only at the end.
   - Book use: teach as a concept and as a check the PM asks the AI harness to perform ("was the stopping rule set before launch?"), no formulas.

13. Wasserstein, Ronald L. and Lazar, Nicole A. The ASA's Statement on p-Values: Context, Process, and Purpose. The American Statistician, 2016 (released 2016-03-07). DOI 10.1080/00031305.2016.1154108 [S: primary page returned 403/404; principles consistent across multiple secondary sources including ScienceDaily 2016-03-07 https://www.sciencedaily.com/releases/2016/03/160307092305.htm]
   - Six principles (paraphrased): (1) p-values indicate how incompatible data are with a specified model; (2) they do not measure the probability that the hypothesis is true, or that data arose by chance alone; (3) decisions should not rest only on a threshold; (4) proper inference requires full reporting and transparency; (5) a p-value does not measure effect size or importance; (6) by itself a p-value is not a good measure of evidence.

14. OpenAI acquisition of Statsig, announced 2025-09-02. TechCrunch, 2025-09-02. https://techcrunch.com/2025/09/02/openai-acquires-product-testing-startup-statsig-and-shakes-up-its-leadership-team/ [S; OpenAI's own page returned 403]
   - Statsig: experimentation and feature-flag platform. Founder Vijaye Raji became OpenAI CTO of Applications. Reported value about $1.1B in stock (reported, not confirmed by OpenAI in text I could read). Platform brought in-house to speed product development.

15. Datadog. Datadog Acquires Eppo to Expand Its AI, Product Analytics, Experimentation and Feature Flag Capabilities. Press release, 2025-05-05. https://www.datadoghq.com/about/latest-news/press-releases/datadog-acquires-eppo-to-expand-its-ai/ [V via search of the press release; price undisclosed, about $220M only in press reports [S]]
   - Signal for the chapter: experimentation is consolidating into observability and AI-model platforms; for AI features, experiments and evals sit side by side.

16. Anthropic. Donating the Model Context Protocol and establishing the Agentic AI Foundation. 2025-12-09. https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation [V]
   - MCP described as a universal open standard for connecting AI applications to external systems; introduced by Anthropic about a year earlier (November 2024). Over 10,000 active public MCP servers; 97M+ monthly SDK downloads (Python and TypeScript). Agentic AI Foundation (a directed fund under the Linux Foundation) co-founded by Anthropic, Block and OpenAI.
   - Chapter use: MCP servers are the plumbing by which a PM's AI harness reaches the experiment platform, warehouse and tickets; and MCP is itself a "platform/API product" example of standards governance.

17. Optimizely Opal (vendor material, 2025 to 2026). Opal results summary and Results Summary Report agent; Experiment Program Health Review agent. https://support.optimizely.com/hc/en-us/articles/46350242034061-Experiment-Program-Health-Review-agent and https://www.optimizely.com/company/press/opal-turns-2 [V that features exist; no independent accuracy evidence]
   - Vendor guidance on prompting: ask for a specific comparison (variations, named metrics, significance, a summary table) rather than "analyze our A/B test results." Good illustration of the "experiment analysis request" artifact.

18. Ubl, Malte. Design Docs at Google. Industrial Empathy, 2020-07-06. https://www.industrialempathy.com/posts/design-docs-at-google/ [V]
   - Sections: context and scope (not a requirements doc); goals and non-goals; the actual design (system-context diagram, APIs, data storage, little code, emphasis on tradeoffs); alternatives considered (one of the most important sections); cross-cutting concerns (security, privacy, observability).
   - Length: larger projects about 10 to 20 pages; "mini design doc" 1 to 3 pages. Skip a design doc when there are no real tradeoffs or alternatives.
   - Lifecycle: create and iterate; review (lightweight comments or formal meeting); update during implementation; revisit after a year or two.
   - Quote: "Write them in whatever form makes the most sense for the particular project."
   - PM application: how to read a design doc. Read goals and non-goals against the PRD; read alternatives considered for the tradeoff logic; check cross-cutting concerns for the customer promises (security, residency, latency); ask what was left out.

19. Nygard, Michael. Documenting Architecture Decisions. Cognitect blog, 2011-11-15. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions [V]
   - ADR template: Title (short noun phrase, numbered); Context (forces at play, stated as facts, including conflicting ones); Decision ("We will..." in active voice); Status (proposed, accepted, deprecated, superseded); Consequences (all of them: positive, negative, neutral). One to two pages, stored in the repo, numbered, never deleted when superseded.
   - PM application: PMs read ADRs to learn why the system is shaped as it is before asking for a change; PMs can ask the AI harness to summarize the ADR history behind a component.

20. Klein, Gary. Performing a Project Premortem. Harvard Business Review, September 2007. https://hbr.org/2007/09/performing-a-project-premortem [V for summary]
   - Method: imagine the project has already failed, then each person generates plausible reasons; makes it safe for knowledgeable worriers to speak up during planning.
   - Usual procedure (from Klein's article, [S] for exact steps): brief on plan; announce it failed spectacularly; each person writes reasons silently (a few minutes); round-robin share one reason at a time; leader reviews the list and strengthens the plan; revisit periodically.
   - Research base: Mitchell, Russo and Pennington (1989), "Back to the future: Temporal perspective in the explanation of events," Journal of Behavioral Decision Making: "prospective hindsight." Klein's article reports that imagining an event has already happened increases the ability to identify reasons for outcomes by 30% [S, contested: one reading says the study measured number of reasons, not accuracy]. Flag.
   - Quote: "Projects fail at a spectacular rate." (Klein, HBR 2007)

21. Yegge, Steve. Stevey's Google Platforms Rant. Google+ post 2011-10-11; preserved copy https://gist.github.com/chitchcock/1281611 [V that the rant says this; the mandate itself is Yegge's recollection, unverified by Amazon]
   - Recalled mandate (around 2002, "plus or minus a year"): all teams expose data and functionality through service interfaces; communicate only via those interfaces; no direct linking, reading another team's data store or shared memory; any technology allowed; every interface designed so it could be exposed to outside developers. Yegge's thesis: platforms need long-term investment and internal teams must dogfood the same interfaces offered externally.
   - Quote: "Start with a Platform, and Then Use it for Everything."
   - Flag: never present the Bezos memo as documented Amazon fact; attribute to Yegge's recollection.

22. Skelton, Matthew and Pais, Manuel. Team Topologies (IT Revolution, 2019 [S for year]). Key concepts page https://teamtopologies.com/key-concepts [V]
   - Four team types: stream-aligned, platform, enabling, complicated subsystem. Three interaction modes: collaboration, X-as-a-Service, facilitation.
   - A platform team provides a compelling internal product that speeds up stream-aligned teams by removing complexity. Platform PM's customers are internal developers; success = adoption and reduced cognitive load, not features shipped.

23. Postman. 2025 State of the API Report. https://www.postman.com/state-of-api/2025/ [V]
   - 5,700+ respondents (developers, architects, executives). 82% have adopted some level of API-first; 25% fully API-first. 65% generate revenue from APIs. Only 24% design APIs with AI agents in mind. 51% name unauthorized or excessive API calls from AI agents as top security concern. MCP: about 70% aware (also stated as "two-thirds"), 10% use regularly. Flag the inconsistent awareness figure.
   - Chapter use: AI agents are now API consumers; the API/platform brief must name agent consumers, rate limits and permissions.

24. Google. API Design Guide. https://docs.cloud.google.com/apis/design [V]
   - Used inside Google since 2014. Covers resource-oriented design, resource names, standard methods (Get, List, Create, Update, Delete), custom methods, errors, versioning, backward compatibility, naming. Many topics now in AIP pages.

25. Cagan, Marty. Experimentation, AI and the Product Model. SVPG, 2026-10-21. https://www.svpg.com/experimentation-ai-and-the-product-model/ [V]
   - AI makes building faster and cheaper, so the hard problem is deciding what to build. Experimentation should drive innovation, not only optimization. AI products are probabilistic: use evals early for quality; reserve costlier A/B tests for establishing value. Hybrid model: teams run their own experiments, coached by embedded experimentation experts.

26. Cagan, Marty. The AI Productivity Paradox. SVPG, 2026-07-23. https://www.svpg.com/the-ai-productivity-paradox/ [V]
   - Teams ship faster with AI but results stay flat; the cause is the project (output) model. Faster building yields more of the wrong things. Links directly to Cutler's feature factory: AI can turn a feature factory into a faster feature factory. Cagan cites Chip Huyen's line that the hardest part remains knowing what to build [V as cited by Cagan].

27. Cagan, Marty. Build To Learn FAQ. SVPG, 2026-04-27. https://www.svpg.com/build-to-learn-faq/ [V]
   - Build to learn (discovery, prototypes to test value, usability, feasibility, viability) versus build to earn (delivery, production quality). As delivery cost falls, discovery is the bottleneck. AI in delivery: code generation; AI in discovery: prototyping and decision support.

28. Wright, Hyrum. Hyrum's Law. https://www.hyrumslaw.com/ [V]
   - With enough users of an API, all observable behaviors of the system will be depended on by somebody, regardless of the contract. Named and popularized by Titus Winters. Came from large-scale infrastructure migrations at Google.
   - PM application: every undocumented behavior of a platform (ordering of results, timing, error text) becomes a de facto commitment; deprecation plans must assume it.

29. Jones, Chris; Wilkes, John; Murphy, Niall; Smith, Cody (ed. Beyer, Betsy). Service Level Objectives, chapter 4 of Site Reliability Engineering. Google/O'Reilly, 2016 (site copyright 2017). https://sre.google/sre-book/service-level-objectives/ [V]
   - SLI: a precisely defined measure of one aspect of service (latency, error rate, throughput). SLO: target value or range for an SLI. SLA: a contract with consequences (often financial) for missing SLOs; no consequence means it is an SLO. Error budget: allowed rate of SLO misses.
   - PM application: platform PMs write SLOs into the product brief; the error budget is a product decision about how much reliability to trade for speed.

30. Leach, Brandur. APIs as infrastructure: future-proofing Stripe with versioning. Stripe blog, 2017-08-05. https://stripe.com/blog/api-versioning [V]
   - Date-named rolling versions, each with a small set of backward-incompatible changes; an account is pinned to the newest version at its first request and can override per request or upgrade; each breaking change is encapsulated in a "version change module" applied in reverse to produce older responses. Adding endpoints or fields is safe; removing fields is not ("Fields that were present before should stay present").
   - Use as the single real-company example of API compatibility as a product promise.

31. Brewer, Eric. CAP Twelve Years Later: How the "Rules" Have Changed. InfoQ (reprinted from IEEE Computer), 2012-05-30. https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/ [V]
   - "2 of 3" framing misleads: the consistency versus availability choice is fine-grained (per operation, per data) and a matter of degree. Partitions are rare; the real tradeoff happens during them. Recommended: detect partitions, enter an explicit partition mode, then recover and compensate. Partitions are effectively time bounds, linking CAP to latency.
   - Quote: "CAP prohibits only a tiny part of the design space."

32. Cagan, Marty. Product Coaching and AI. SVPG, 2026-02-04. https://www.svpg.com/product-coaching-and-ai/ [V]
   - Configure the model with your context; seek critique and mistakes rather than affirmation; models are non-deterministic so re-check important conclusions.

---

## (a) Key concepts and frameworks

### 1. What a technical PM is, and when the role differs
No single authoritative definition exists [flag]. Working definition for the book (author's own framing, not a cited fact): a technical PM is a PM whose customers, product surface or key risks are technical, so the PM must reason about feasibility, architecture and operational tradeoffs directly rather than delegating them. Cagan's four risks (value, usability, feasibility, viability; source 27 lists them) give the frame: on a technical product, feasibility and viability risks dominate and the "user" is often a developer or another team.
- Platform PM: internal customers (stream-aligned teams, per Team Topologies); X-as-a-Service is the target interaction mode; success measured by adoption and reduced cognitive load; the "compelling internal product" test (source 22).
- API PM: customer is a developer, increasingly an AI agent (Postman 2025, source 23). Promises are contracts: versioning and compatibility (Stripe, source 30; Google API Design Guide, source 24); Hyrum's Law means observable behavior becomes the contract (source 28). Yegge's platform rant on dogfooding the external interface (source 21).
- Infrastructure PM: reliability is the product; SLIs, SLOs, SLAs and error budgets are product decisions (source 29); tradeoffs like consistency versus availability (Brewer, source 31).
- AI/ML PM: probabilistic outputs; evals for quality before A/B tests for value (Cagan 2026, source 25); inference cost as a margin line (Beacon: 81% to 72%).
- How a B2B/platform PM applies it: name your primary customer (human user, developer, internal team, agent) and your dominant risk before choosing a process.

### 2. Why products fail
- CB Insights 2026 (source 1): capital exhaustion is usually the last symptom; poor product-market fit (43%) and unsustainable unit economics (19%) are the product-relevant root causes. Contrast with earlier editions (no market need as top or second reason). Teaching point: self-reported post-mortems are founders' explanations, not causal proof.
- Cagan's ten root causes (source 2): stakeholder-sourced ideas, business cases, feature roadmaps, PM as requirements writer, late design, late engineering, agile only in delivery, project funding, risk at the end, opportunity cost. Remedy: continuous discovery with delivery; outcome roadmaps.
- Cutler's feature factory (source 3): twelve signs, usable as a diagnostic. 2026 extension: Cagan's AI productivity paradox (source 26), AI accelerates output without changing outcomes.
- Application: a failure pre-mortem combines Klein's method (source 20) with these three lists as prompts.

### 3. Product development processes compared
| Process | Originator | Core idea | Where it fits in B2B/platform | Main failure mode |
|---|---|---|---|---|
| Waterfall (sequential) | Royce 1970 described and criticized it (source 5) | Phases in order, documents as hand-offs | Regulated, hardware, contract-bound work | Late discovery of problems; Royce himself said it invites failure |
| Stage-Gate | Cooper, 1980s, term in print 1988 (source 4) | Information-gathering stages plus investment gates (go, kill, hold, recycle) | Portfolio funding, hardware, big-bet platform investments; Agile StageGate hybrid | Gates that never kill; linear assumptions |
| Agile | Manifesto 2001 (source 6) | Iterative delivery, working software, responding to change | Delivery of software increments | Agile only in delivery (Cagan cause 7) |
| Lean (Lean Startup) | Ries 2011 (covered in ch01 refs) | Build, measure, learn; validated learning | New products, new segments | Vanity metrics; MVPs that are too small to learn from in enterprise |
| Dual-track | Sy 2007 origin (source 7); Patton popularized (source 8) | Discovery and delivery in parallel, same team | Default for product teams in 2026 | Two separate teams ("duel track"); discovery as a phase |
- Royce's five fixes (program design first, document the design, do it twice, plan and monitor testing, involve the customer) prefigure prototypes and customer involvement.
- 2026 overlay: Cagan's build to learn versus build to earn (source 27): AI lowers delivery cost so discovery becomes the bottleneck.

### 4. Technical fluency a PM needs
- Architecture: system-context diagram, components, where data lives, synchronous versus asynchronous calls. Team Topologies for org-architecture coupling (source 22).
- APIs: resources and methods, versioning, backward compatibility, rate limits, auth scopes (sources 24, 28, 30).
- Data models: entities, relationships, identifiers, tenancy (for Beacon: incident, alert, tenant, connector, action, approval).
- System design tradeoffs: consistency versus availability and latency (source 31), reliability targets (source 29), cost per request (inference).
- Reading a design doc (source 18): read goals and non-goals against the PRD; check alternatives considered; check cross-cutting concerns; ask "what would make us regret this in a year?" Read ADRs (source 19) for history.
- Template: Technical design review checklist (PM questions). Proposed structure:
  1. Problem and outcome: does the doc's context and goals match the PRD outcome?
  2. Non-goals: are the exclusions acceptable to customers and sales?
  3. Customers of the interface: humans, developers, internal teams, AI agents?
  4. Alternatives considered: were cheaper or reversible options weighed?
  5. Data: what is stored, where, for how long, under which tenant and region?
  6. Reliability: SLIs and SLOs proposed; error budget; failure behavior.
  7. Compatibility: what breaks for existing integrations (Hyrum's Law check)?
  8. Security and privacy: least privilege, audit logs, residency.
  9. Cost: unit cost per request or per resolved incident; margin impact.
  10. Observability and rollback: how do we know it works, how do we undo it?
  11. Reversibility: is this a one-way or two-way door decision? [Bezos letter concept; not verified this session, flag]
  12. Decisions to record as ADRs.

### 5. AI-assisted analysis and A/B testing (concepts, no code)
- Framing: hypothesis, primary metric (OEC, source 9), guardrails (organizational: latency, cost, error rates; trust: SRM), minimum detectable effect, unit of randomization (user, account, tenant; B2B often randomizes at account level, fewer units, less power).
- Significance and power at concept level: a p-value measures incompatibility of data with a no-effect model, not the probability that the idea works (ASA, source 13). Power is the chance of detecting a real effect of the chosen size; underpowered tests miss real effects and exaggerate the ones they find [concept; exaggeration point is a known statistical result, flag for citation if stated as fact]. Decide sample size and stopping rule before launch; peeking inflates false positives (Miller, source 12).
- Interpreting: effect size and confidence interval over a binary "significant"; check SRM first (sources 9, 11); Twyman's law for surprising wins; segment results only when pre-registered.
- B2B specifics: few accounts, heterogeneous customers, contracts and sales cycles; often cannot A/B test pricing or admin features; alternatives are staged rollouts, holdouts, switchback or before/after with comparison groups [concept, author framing].
- AI-era: evals for quality, A/B tests for value (source 25).
- Asking an AI harness to analyze experiment data and checking it: harness connects via MCP (source 16) to the experiment platform and warehouse. PM supplies the pre-registered plan and asks for specific outputs (vendor guidance, source 17). Then checks: did it run the SRM check; did it use the pre-set primary metric; does the reported sample match the platform dashboard; did it compute intervals, not only p-values; did it go segment fishing; ask it to list its assumptions and to critique its own analysis (Cagan, source 32: seek critique, re-check non-deterministic outputs). Re-run on a second pass or second model for important calls.
- Template: Experiment analysis request (prompt brief).
  - Decision this informs, and who decides.
  - Hypothesis, as written before launch.
  - Data sources (connector names), date range, unit of randomization, expected split.
  - Primary metric (OEC) and guardrails, with definitions.
  - Pre-set stopping rule and minimum detectable effect.
  - Required outputs: SRM check result; effect size with interval per metric; guardrail status; pre-registered segments only; plain-language summary under 150 words; list of assumptions and data-quality caveats; what would change the conclusion.
  - Forbidden moves: new segments without labeling them exploratory; changing the metric; declaring a winner if SRM fails.
  - Verification step: the PM spot-checks counts against the platform and asks the harness to critique its own result.

### 6. Other artifact templates
- API/platform product brief: customer (developer, internal team, agent); job to be done; interface promise (resources, methods, events); compatibility and versioning policy; SLOs; rate limits and quotas; auth scopes and least privilege; pricing or chargeback unit; adoption metric (active integrations, time to first successful call [author framing]); deprecation policy; documentation and samples; agent-readiness (MCP server, scopes).
- Failure pre-mortem: Klein procedure plus prompts from CB Insights categories, Cagan's ten causes and Cutler's twelve signs; output a ranked risk list with owner, early-warning signal and mitigation.
- Technical fluency self-assessment: rate 1 to 4 on architecture, APIs, data models, reliability (SLOs), security and privacy, cost, experimentation, AI systems (evals, retrieval, agents); for each, a behavioral anchor ("can explain the tradeoff in a design doc review without help"); pick two to grow per quarter. [Author construct, not a cited framework]

## (b) Verified facts summary (see sources log for URLs)
- [V] CB Insights 2026: 385 of 431 shutdowns analyzed; capital 70%, poor PMF 43%, timing 29%, unit economics 19%. 2026-03-05.
- [V] Cagan ten root causes, SVPG 2015-06-05.
- [V] Cutler feature factory twelve signs, 2016-11-17.
- [V] Royce, IEEE WESCON, August 1970: sequential implementation "risky and invites failure"; five steps.
- [V] Agile Manifesto 2001, four values.
- [V] Patton dual track, 2017-05-10.
- [V] Ubl design docs, 2020-07-06. [V] Nygard ADR, 2011-11-15.
- [V] Miller peeking, 2010-04-18: about 26% false positive in his illustration.
- [V] Fabijan et al. KDD 2019 SRM definition. [S] about 6% of Microsoft experiments show SRM.
- [S] ASA p-value statement six principles, 2016-03-07.
- [V] Anthropic MCP donation 2025-12-09: 10,000+ active public servers, 97M+ monthly SDK downloads; AAIF co-founded by Anthropic, Block, OpenAI.
- [S] OpenAI to acquire Statsig, announced 2025-09-02, about $1.1B reported.
- [V] Datadog acquires Eppo, 2025-05-05 (price undisclosed; $220M reported [S]).
- [V] Postman 2025: 5,700+ respondents; 82% some API-first; 65% revenue from APIs; 24% design for AI agents; 10% use MCP regularly.
- [V] Google API Design Guide in use since 2014.
- [V] Stripe date-based API versioning, 2017-08-05.
- [V] Cagan SVPG 2026: AI Productivity Paradox (07-23), Build To Learn FAQ (04-27), Experimentation, AI and the Product Model (10-21).

## (c) Quotes (under 15 words)
1. "is risky and invites failure" (Winston Royce, 1970, on the sequential model).
2. "The whole team is responsible for product outcomes, not just on-time delivery" (Jeff Patton, 2017).
3. "Features on roadmaps (output) are replaced by business problems to be solved (outcome)." (Marty Cagan, SVPG, 2015) [13 words]
4. "CAP prohibits only a tiny part of the design space." (Eric Brewer, 2012)
5. "Projects fail at a spectacular rate." (Gary Klein, HBR, 2007)

## (d) 2025 to 2026 AI-era developments
- MCP becomes neutral infrastructure: donated to Linux Foundation's Agentic AI Foundation, 2025-12-09 (source 16). PM harnesses reach experiment platforms, warehouses and ticketing through MCP connectors.
- Experimentation consolidates into AI and observability platforms: Datadog and Eppo (2025-05-05), OpenAI and Statsig (2025-09-02). Signal: experimentation is becoming part of the AI product stack; evals and experiments converge.
- Vendors ship AI agents that summarize experiment results (Optimizely Opal); no independent accuracy evidence found, so the PM's verification step matters.
- AI agents as API consumers: Postman 2025 shows only 24% design for agents; agent call volume is the top security worry. API/platform briefs must treat agents as a customer segment.
- Cagan 2026: AI productivity paradox; build to learn versus build to earn; evals for quality, A/B tests for value; hybrid experimentation coaching.

## (e) Beacon worked-example ideas (consistent with beacon-case.md)
- Beacon's PMs are technical PMs by the definition: customers include Priya and Dana (humans), Leo (multi-tenant MSP), Sam (gatekeeper) and developers who build connectors; MCP servers are part of the surface.
- Pre-mortem for Beacon Agents launch at Northlight Live: "It is six months later and Beacon Agents failed." Likely reasons generated: a hallucinated root cause triggers a wrong rollback (the existing storyline); Sam blocks deployment for missing audit logs and AI documentation; inference costs push gross margin below 72%; per-resolved-incident pricing disputes over what "resolved" means; connectors break when an observability vendor changes an API (Hyrum's Law in reverse). Map each to Cagan's causes and a mitigation.
- Feature factory check: score Beacon's roadmap against Cutler's signs, for example "chasing upfront revenue" when a large customer asks for a bespoke connector.
- Design doc review: the Act capability's approval-gate design doc. PM checklist questions: allowlist scope per tenant, audit log retention, rollback of the rollback, SLO for approval latency at 3 a.m. for Dana, consistency of incident state across regions for EU residency.
- API/platform brief: "Beacon Actions API and MCP server" for MSP partners (Leo): tenant-scoped tokens, rate limits, date-based versioning, deprecation tied to Beacon Classic sunset.
- Experiment: test a new diagnosis summary layout on diagnosis acceptance rate (primary) with guardrails MTTR, wrong-action rate, inference cost per incident. Randomize at the team or tenant level (not per incident) to avoid contamination; with about 420 customers, power is limited, so consider a longer run or a holdout. Show the PM writing an experiment analysis request to the harness, the harness reporting a "significant" lift, and the PM catching an SRM (for example, one MSP's tenants all landing in treatment) before acting.
- Evals before A/B: root-cause accuracy evals on resolved incidents (Learn capability) gate any experiment exposure.
- Fluency self-assessment: the new Principal PM rates themself low on data residency and inference cost and picks those two to grow.

## (f) Editorial flags
- CB Insights: earlier edition figures (42% no market need; 38/35/20 top three) are [S] only; the 2026 figures are verified. Do not mix editions. Self-reported reasons, not causes.
- Fabijan 6% SRM rate: [S]; abstract page does not state it.
- Klein's 30% prospective hindsight figure: contested interpretation (number of reasons versus accuracy); avoid or state carefully.
- ASA principles: primary page blocked; consistent across secondary sources.
- Bezos API mandate: Yegge's recollection; not an Amazon-confirmed document.
- Statsig $1.1B and Eppo $220M: press reports, not confirmed in the primary text I could read.
- Royce never using the word "waterfall": widely reported, not checked against the full text; avoid stating unless verified.
- "One-way and two-way door" decisions (Bezos 2015 shareholder letter): not verified in this session.
- Team Topologies book year 2019 and Cooper 1988 first print: [S].
- No authoritative definition of "technical PM" found; the definition is the book's own.
- Cutler's 3-years-later follow-up has no date on the page.
- Optimizely Opal: vendor claims, no independent accuracy evidence.
- Postman MCP awareness stated as both 70% and two-thirds.
- Search budget ran out before checking: a primary definition of TPM roles, Thoughtworks "API as a product" (not in the April 2026 Radar volume), and any study on LLM accuracy in statistical analysis. Chapter should not cite such a study without verification.
- Lean Startup details are covered in chapter 01 refs (Ries 2011); not re-verified here.
- Years in the refs list for hyrumslaw.com (2020), the Cutler Amplitude follow-up (2019) and the Cooper Syracuse talk (2023) are inferred, not stated on the pages.
