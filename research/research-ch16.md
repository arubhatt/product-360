# Research notes: Chapter 16 "Defensibility and Moats" (Part III)

Status: complete for this pass. Compiled 2026-10-30. Tags: [V] verified on primary source; [S] secondary source only; [U] unverified, do not state as fact.
Note on method: the shared web search budget for this run was exhausted at the start, so sources were reached by direct fetch of known URLs. Several primary pages (7powers.com) returned 403. Gaps are listed in section (f).

## Source log (running)

- Porter, "What Is Strategy?", HBR Nov to Dec 1996. https://hbr.org/1996/11/what-is-strategy [V]
- Christensen, Raynor, McDonald, "What Is Disruptive Innovation?", HBR Dec 2015. https://hbr.org/2015/12/what-is-disruptive-innovation [V bibliographic only; body paywalled]
- Christensen Institute, "Disruptive Innovation" theory page. https://www.christenseninstitute.org/theory/disruptive-innovation/ [V]
- Wikipedia, "Disruptive innovation" (for Bower and Christensen 1995, Lepore 2014, Uber note). https://en.wikipedia.org/wiki/Disruptive_innovation [S]
- Acquired podcast, "7 Powers with Hamilton Helmer", released 2021-12-08 (recorded March 2020). https://www.acquired.fm/episodes/7-powers-with-hamilton-helmer [V for Helmer's spoken statements]
- Casado and Lauten, "The Empty Promise of Data Moats", a16z, 2019-05-09. https://a16z.com/the-empty-promise-of-data-moats/ [V]
- SemiAnalysis (Patel, Ahmad), "Google 'We Have No Moat, And Neither Does OpenAI'", 2023-05-04. https://newsletter.semianalysis.com/p/google-we-have-no-moat-and-neither [V that it was published; document is a leaked, unattributed opinion of one employee]
- Moros, Blas, "7 Powers" book notes on blas.com (secondary summary of Helmer). https://blas.com/7-powers/ [S]
- Strategy Capital, About page (Helmer bio, book 2017). https://www.strategycapital.com/about [V]
- Stanford HAI, AI Index Report 2025. https://hai.stanford.edu/ai-index/2025-ai-index-report [V]
- Appenzeller, "Welcome to LLMflation", a16z, 2024-11-12. https://a16z.com/llmflation-llm-inference-cost/ [V]
- Epoch AI, "LLM inference prices have fallen rapidly but unequally across tasks", 2025-03-12. https://epoch.ai/data-insights/llm-inference-price-trends [V]
- Bain, "Will Agentic AI Disrupt SaaS?", Technology Report 2025, 2025-09-23. https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/ [V]
- Anthropic, "Introducing the Model Context Protocol", 2024-11-25. https://www.anthropic.com/news/model-context-protocol [V]
- Anthropic, MCP donated to Agentic AI Foundation, 2025-12-09. https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation [V]
- Chen, "The New Moats" (with AI-era revisit), Greylock. https://greylock.com/greymatter/the-new-moats/ [V]
- Thompson, "Aggregation Theory", Stratechery, 2015-07-21. https://stratechery.com/2015/aggregation-theory/ [V]
- Buffett, Berkshire Hathaway 2007 shareholder letter (moat passage, p.6). https://www.berkshirehathaway.com/letters/2007ltr.pdf [V]
- NFX, "The Network Effects Manual", June 2021. https://www.nfx.com/post/network-effects-manual [V for what NFX claims]
- Wikipedia, "Software as a service" (SaaSpocalypse section, cites Inc. 2026-02-06). https://en.wikipedia.org/wiki/SaaSpocalypse [S]
- Intercom pricing (Fin $0.99 per outcome). https://www.intercom.com/pricing [V, accessed 2026-10-30]
- Salesforce Agentforce pricing. https://www.salesforce.com/agentforce/pricing/ [V, accessed 2026-10-30]
- Bower and Christensen, "Disruptive Technologies: Catching the Wave", HBR Jan to Feb 1995. https://hbr.org/1995/01/disruptive-technologies-catching-the-wave [V bibliographic and summary]
- Anthropic, "Effective context engineering for AI agents", 2025-09-29. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents [V]
- Cahn, "AI's $600B Question", Sequoia, 2024-06-20. https://www.sequoiacap.com/article/ais-600b-question/ [V]
- King and Baatartogtokh, "How Useful Is the Theory of Disruptive Innovation?", MIT Sloan Management Review, 2015-09-15. https://sloanreview.mit.edu/article/how-useful-is-the-theory-of-disruptive-innovation/ [V for the four elements; case counts not visible]
- Spolsky, "Strategy Letter V", Joel on Software, 2002-06-12. https://www.joelonsoftware.com/2002/06/12/strategy-letter-v/ [V]
- McGrath, "Transient Advantage", HBR June 2013. https://hbr.org/2013/06/transient-advantage [V bibliographic; body paywalled]
- Porter, "Strategy and the Internet", HBR March 2001. https://hbr.org/2001/03/strategy-and-the-internet [V summary]
- Slack API Terms of Service, effective 2025-10-10. https://slack.com/terms-of-service/api [V]
- Anthropic (Claude blog), Cowork plugins, 2026-01-30. https://claude.com/blog/cowork-plugins [V]
- Google Developers Blog, "A2A: A new era of agent interoperability", 2025-04-09. https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ [V]

## (a) Key concepts and frameworks

### 1. Moat (Warren Buffett)
- Origin of the metaphor in business usage. Buffett, 2007 Berkshire letter: a great business needs an enduring moat that protects excellent returns on invested capital, because competitors will "repeatedly assault" any castle earning high returns. Examples he names: low-cost producer (GEICO, Costco) and a powerful worldwide brand (Coca-Cola, Gillette, American Express). He rules out industries "prone to rapid and continuous change" because a moat that must be continuously rebuilt is no moat. He also excludes businesses whose success rests on one superstar manager. [V]
- His annual test of investee companies: whether their moats widened during the year. [V, same letter]
- PM application: Buffett's two tests translate directly. (1) Does the advantage protect returns, not just revenue? (2) Did it widen or narrow this year? The second is the right cadence for a moat review. His "rapid change" caveat is the honest starting point for AI-era software: most software features fail his "enduring" test.

### 2. Hamilton Helmer, 7 Powers (2017)
- Bibliographic: Hamilton Helmer, 7 Powers: The Foundations of Business Strategy, 2017. Helmer co-founded Strategy Capital (with John Rutherford, 2013) and taught strategy at Stanford for about a decade. [V Strategy Capital About page]
- Definition of Power: "the set of conditions creating the potential for persistent differential returns." Every Power needs both a Benefit (improves cash flow: higher price, lower cost or less investment) and a Barrier (prevents competitors from arbitraging the benefit away). [S, Blas summary; consistent with Acquired interview]
- Fundamental equation: Value = Market size x Power (Blas summary wording). The book's fuller form is commonly given as Value = M0 x g x s x m (current market size, market growth, long-term differential market share, long-term differential margin). [S for the short form; U for the long form, check against the book]
- The seven Powers with Benefit and Barrier (summary from Blas notes and Acquired interview; [S] unless noted):

| Power | Benefit | Barrier | Canonical example in Helmer |
|---|---|---|---|
| Scale economies | Unit cost falls as volume grows | Prohibitive cost for a challenger to gain the share needed to match costs | Netflix spreading fixed content cost across subscribers (Acquired, [V] spoken) |
| Network economies | Value to each customer rises with the number of other customers | Unattractive cost for a challenger to gain enough users; often winner-take-all | Helmer notes intensity is hard to judge up front (Acquired) |
| Counter-positioning | A new, superior business model | Collateral damage: the incumbent will not copy because copying would damage its existing business | Vanguard index funds versus Fidelity's active funds |
| Switching costs | Higher prices on follow-on sales to current customers | A rival must compensate customers for the cost of switching | Enterprise software (SAP is Helmer's usual example, [U] not confirmed in fetched text) |
| Branding | Higher price from emotional appeal or reduced uncertainty | Hysteresis: a long period of consistent reinforcing action is needed | Tiffany in the book ([U]) |
| Cornered resource | Preferential access, on attractive terms, to a coveted asset that independently raises value | Fiat: access is held by decree, contract or ownership, not earned in the market | Pixar's directors "Brain Trust" (Acquired and Blas) |
| Process power | Embedded company organization and activity sets that lower cost or improve the product | Hysteresis: rivals cannot copy quickly because the know-how is complex and opaque | Toyota Production System |

- Helmer on counter-positioning (Acquired): he treats it as partly temporary because, over time, the incumbent may accept the damage and copy. He also says the incumbent often knows the new model is good but cannot afford the hit now. [V spoken]
- Helmer on switching costs (Acquired): monetization needs repeat purchase, "some kind of razor blade aspect". [V spoken]
- Power Progression (from the book; [U] stage mapping not confirmed on a fetched page): Origination (before takeoff): counter-positioning and cornered resource are typically available. Takeoff (rapid growth): scale economies, network economies and switching costs must be established during this window. Stability: branding and process power. Acquired confirms Helmer places switching costs in takeoff and says the takeoff window "often closes". Flag for check before stating the full mapping.
- Key Helmer test for PMs: operational excellence is not Power. Being better is arbitraged away unless a Barrier exists. This matches Porter's distinction below.
- How a B2B or platform PM applies it: for each claimed advantage, write the Benefit in cash flow terms (price premium, cost, capex avoided) and the Barrier in competitor terms (what would it cost a capable rival to copy, and why would they not). If either cell is empty, it is not a Power. Then place the business on the Power Progression to see which Powers are still available to build. Helmer's useful corollary: most products have one or two real Powers, not seven.

### 3. Michael Porter: sustainable advantage (brief)
- "What Is Strategy?" (HBR, Nov to Dec 1996) [V]: operational effectiveness (doing the same things better) is necessary but not strategy, because best practice diffuses and rivals converge. Strategy is choosing a different set of activities to deliver a unique mix of value. Sustainability comes from trade-offs (choosing what not to do, which blocks straddlers) and fit among activities. Three orders of fit: simple consistency, reinforcing activities, optimization of effort. Fit makes advantage sustainable because a rival must copy the whole interlocking system; the odds of matching every activity compound.
- "Strategy and the Internet" (HBR, March 2001) [V summary]: a new general-purpose technology tends to weaken industry profitability and does not by itself create proprietary advantage; distinctive strategy matters more, and winners integrate the new technology with their existing ways of competing. Direct analogy for generative AI in 2026.
- PM application: a feature is operational effectiveness. A moat is usually a system of fit (data, workflow, pricing, channel, trust) that a rival would need to replicate all at once.

### 4. Clayton Christensen: disruption, stated correctly
- Lineage: Bower and Christensen, "Disruptive Technologies: Catching the Wave" (HBR, Jan to Feb 1995) [V]; The Innovator's Dilemma (Harvard Business School Press, 1997) [V bibliographic via Wikipedia]; Christensen, Raynor and McDonald, "What Is Disruptive Innovation?" (HBR, Dec 2015) [V bibliographic], written to correct misuse.
- Correct statement (Christensen Institute page, [V]): disruption is a process in which a smaller entrant with fewer resources gains a foothold either at the low end of an existing market (customers incumbents are happy to cede because the bottom offers little profit) or in a new market of nonconsumers. Incumbents keep improving for their most demanding, most profitable customers (sustaining innovation). The entrant's offering starts out worse by the historical measures of performance, then improves until it is good enough for mainstream customers, who then switch. Disruption is "NOT breakthrough technologies that make good products better."
- What disruption is not: any big change, any successful startup, or any technology shock. Christensen himself said Uber is not disruptive in his sense because it started in the mainstream taxi market, not at the low end or among nonconsumers (via Wikipedia citing the 2015 HBR article and a 2016 Forbes interview, [S]). Christensen later noted that low-end entry correlates with a business model unattractive to the incumbent ([S], Forbes 2016 via Wikipedia). This is the bridge to Helmer's counter-positioning.
- Critiques (state fairly): Jill Lepore, "The Disruption Machine", The New Yorker, 23 June 2014, argued the theory rests on selected cases and that some named victims remained dominant ([S] via Wikipedia). King and Baatartogtokh (MIT Sloan Management Review, Sept 2015) coded Christensen's own cases against four conditions (incumbents on a sustaining trajectory; performance overshoot; incumbents able to respond; incumbents actually floundered) and found that only a minority met all four ([V] for the four conditions; the share is commonly reported as 9 percent of 77 cases, [U], not visible in fetched text).
- PM application: use the correct test as a checklist. Is the threat (1) worse on our customers' current measures of performance, (2) cheaper or simpler, or serving people who do not buy today, (3) improving fast, and (4) attached to a business model we would find unattractive to copy? Four yeses mean disruption. A better product sold to our best customers is a sustaining threat; incumbents usually win those fights by Christensen's own account.

### 5. AI disruption of SaaS seats: apply both lenses
- The structural argument (Bain, Sept 2025, [V]): when AI does the work, per-seat pricing stops tracking value; Bain recommends pricing for work done (tasks, resolved tickets) and names Intercom and Salesforce as moving that way. Bain's 2x2 scores each workflow on AI automation potential and on third-party AI penetration potential, giving four scenarios: AI enhances SaaS ("core strongholds"), spending compresses ("open doors"), AI outshines SaaS ("gold mines"), AI cannibalizes SaaS ("battlegrounds"). Bain treats systems of record as the defensible base layer because of unique data structures, long activity histories and embedded regulatory logic.
- Christensen lens: an AI agent sold per outcome can be a new-market or low-end foothold (it serves teams that never bought seats, at lower cost, with lower quality at first). Helmer lens: a seat-priced incumbent faces counter-positioning, since moving to outcome pricing cuts its own seat revenue when agents reduce headcount.
- Classroom caution: many "AI kills SaaS" claims are sustaining innovations sold to the same buyers and fail the disruption test. Teach readers to run the four-question test rather than adopt the headline.

### 6. Moats in AI-era software (synthesis, each with attribution)
- Model access is not a moat. Evidence: inference cost at constant capability falls fast (a16z "LLMflation": roughly 10x per year; Epoch AI: 9x to 900x per year depending on task; Stanford AI Index 2025: GPT-3.5-level cost fell over 280-fold from Nov 2022 to Oct 2024), and model quality converges (AI Index 2025: open versus closed gap fell from 8 percent to 1.7 percent on some benchmarks in a year; top versus 10th model gap from 11.9 percent to 5.4 percent). Anyone can call the same models. The leaked 2023 Google memo ("We have no moat") made the same argument about open-source models; present it as one employee's opinion. Helmer framing: a model API has no Barrier for the application builder; it is a supplier, not a Power.
- Data moats and their limits (Casado and Lauten, a16z, 2019 [V]; NFX 2021 [V]): most "data network effects" are really data scale effects with diminishing returns; marginal data gets more expensive while it adds less; data goes stale; competitors can often reach a "minimum viable corpus". Defensible only when data is proprietary or hard to access, refreshed by use, concentrated in the hard long tail, and when accuracy gains drive adoption. NFX lists data as one of 16 network effect types and calls it weaker than investors assume.
- Workflow integration and systems of record (Jerry Chen, Greylock, "The New Moats" and its AI revisit [V]; Bain 2025 [V]): value sits in systems of record (CRM, HCM, ERP), systems of engagement and "systems of intelligence" that combine data across systems. Chen's AI-era conclusion: "the new moats are the old moats", namely workflows, data integration, trust, network effects, scale and go-to-market. Helmer mapping: switching costs plus process power.
- Proprietary context: in an agentic product, the moat candidate is not the model but what the agent knows at run time: customer-specific history, topology, runbooks, permissions and outcome labels. Anthropic's context engineering guidance (Sept 2025 [V]) treats context as a finite resource to curate with high-signal tokens retrieved just in time; the PM's question is whether that curated context is exclusive and compounding. Helmer mapping: a cornered resource only if access is contractual or structural, otherwise a scale effect.
- Distribution: Ben Thompson's Aggregation Theory (Stratechery, 2015 [V]) says that when distribution is free, power shifts to whoever owns the user relationship and suppliers are commoditized. In 2026 the AI harness (assistant plus connectors) is a new candidate aggregator; a SaaS app reached only as an MCP connector risks becoming a supplier. Counter-move evidence: Slack's API terms (effective 10 Oct 2025 [V]) bar third parties from using API data to train LLMs and from building persistent indexes of other organizations' data. Bain also recommends restricting other AI platforms from learning on your data.
- Interoperability lowers integration moats: MCP (Anthropic, Nov 2024) became a Linux Foundation project under the Agentic AI Foundation in Dec 2025 with 10,000+ active public servers and 97M+ monthly SDK downloads [V]; Google's A2A protocol launched April 2025 with 50+ partners [V]. Implication: "we have 200 integrations" is weaker as a switching cost once connectors are standard; depth of action and governance inside the integration matters more.
- Trust and brand: Helmer's Branding Benefit includes "reduced uncertainty", which is the enterprise AI case: buyers pay for confidence that an agent will not cause harm. Barrier is hysteresis, so trust takes years to build and one incident to dent. Pair with audit logs, approval gates and evidence.
- Ecosystems: Spolsky's "commoditize your complements" (2002 [V]) explains platform plays: make the layers next to you cheap and plentiful (connectors, open schemas, partner agents) so demand for your layer rises. Chen notes open source commoditizes the layer it touches and pushes value to adjacent layers.

### 7. Commoditization response (frameworks)
- Porter: compete on a distinct system, not the feature.
- Spolsky: if a layer is commoditizing, decide whether it is your product or your complement; if a complement, help commoditize it.
- Christensen: if the commoditizing entrant serves nonconsumers or the low end, consider a separate unit or model rather than fighting with the core business model (stated in Innovator's Dilemma [S]).
- Rita McGrath, "Transient Advantage" (HBR June 2013) and The End of Competitive Advantage (2013): advantages are temporary; firms should run a portfolio of advantages and plan graceful exit as well as launch. Her stage model (launch, ramp up, exploit, reconfigure, disengage) is [U] here; check before use.
- Andy Grove's "strategic inflection point" (Only the Paranoid Survive, 1996) [U, not fetched; attribute only by name if used].

### 8. Templates for the chapter's artifacts (proposed formats; author's own, not from a source)

7 Powers assessment (one row per Power):
| Power | Do we have it today? (Yes / Emerging / No) | Benefit in cash flow terms | Barrier: what stops a capable rival | Evidence (data, not opinion) | Stage available (origination, takeoff, stability) | Action |

Moat scorecard (score 0 to 3 per source; evidence required for any score above 1):
| Moat source | Score | Evidence | Trend this year (widening, stable, narrowing) | What would erase it | Leading indicator |
Rows: proprietary data, proprietary context, workflow depth / system of record, switching costs, distribution and channel, trust and brand, ecosystem, scale economics (including inference cost per outcome), counter-positioning, process power. Add Buffett's annual test: did each row widen or narrow?

Commoditization response plan (per feature under threat):
1. Feature and the commoditizing force (model provider, platform bundle, open source, AI harness).
2. Test: is this our product or our complement?
3. Disruption check (four questions in section 4).
4. Options: move up the stack (outcome, not feature); bundle into a system with fit; reprice (cost-to-serve and outcome pricing); open it up and commoditize it; harvest and exit.
5. Decision, owner, metrics to watch, review date.

Competitive threat monitor (monthly, AI-assisted):
| Threat | Type (sustaining, low-end, new-market, counter-positioning, aggregator) | Signal observed and source | Which moat row it attacks | Severity | Trigger for action | Owner |
Prompt pattern for the AI harness: ask it to scan release notes, pricing pages, win/loss notes and support tickets from connected systems, classify each signal by type and moat row, and cite evidence; the PM validates before anything enters the monitor.

## (b) Verified facts (with URL and date)

1. [V] Buffett (2007 letter, p.6): great businesses need an enduring moat; a moat that must be continuously rebuilt is no moat; he judges investees on whether moats widened during the year. https://www.berkshirehathaway.com/letters/2007ltr.pdf (letter dated Feb 2008, for 2007)
2. [V] Helmer published 7 Powers in 2017; co-founded Strategy Capital in 2013 with John Rutherford; taught at Stanford about ten years. https://www.strategycapital.com/about
3. [V] Acquired episode with Helmer recorded March 2020, released 8 Dec 2021; Helmer places switching costs in the takeoff phase. https://www.acquired.fm/episodes/7-powers-with-hamilton-helmer
4. [V] Porter, "What Is Strategy?", HBR Nov to Dec 1996: OE is not strategy; trade-offs and fit sustain advantage; three orders of fit. https://hbr.org/1996/11/what-is-strategy
5. [V] Porter, "Strategy and the Internet", HBR March 2001: internet tends to weaken industry profitability; distinctive strategy matters more. https://hbr.org/2001/03/strategy-and-the-internet
6. [V] Bower and Christensen, "Disruptive Technologies: Catching the Wave", HBR Jan to Feb 1995. https://hbr.org/1995/01/disruptive-technologies-catching-the-wave
7. [V] Christensen, Raynor, McDonald, "What Is Disruptive Innovation?", HBR Dec 2015. https://hbr.org/2015/12/what-is-disruptive-innovation
8. [V] Christensen Institute: low-end and new-market footholds; disruption is not breakthrough technology that makes good products better. https://www.christenseninstitute.org/theory/disruptive-innovation/ (accessed 2026-10-30)
9. [V] King and Baatartogtokh, MIT SMR, 15 Sept 2015: four tested conditions for disruption. https://sloanreview.mit.edu/article/how-useful-is-the-theory-of-disruptive-innovation/
10. [V] Casado and Lauten, a16z, 9 May 2019: data moats weaker than assumed; chatbot example plateaus near 40 percent intent coverage. https://a16z.com/the-empty-promise-of-data-moats/
11. [V] NFX, June 2021: 16 network effect types; claims network effects account for 70 percent of tech value since 1994 (NFX's own study; treat as NFX's claim). https://www.nfx.com/post/network-effects-manual
12. [V] Stanford AI Index 2025: GPT-3.5-level inference cost fell over 280-fold Nov 2022 to Oct 2024; open versus closed gap 8 percent to 1.7 percent; top versus 10th model gap 11.9 percent to 5.4 percent. https://hai.stanford.edu/ai-index/2025-ai-index-report
13. [V] a16z LLMflation, 12 Nov 2024: cost at equivalent capability falls about 10x per year; GPT-3-level MMLU 42 went from $60 to $0.06 per million tokens in about 3 years. https://a16z.com/llmflation-llm-inference-cost/
14. [V] Epoch AI, 12 Mar 2025: price declines of 9x to 900x per year at constant performance, varying by task; fastest declines may not persist. https://epoch.ai/data-insights/llm-inference-price-trends
15. [V] SemiAnalysis, 4 May 2023, published leaked Google memo; one unnamed employee's view; SemiAnalysis disagreed with it. https://newsletter.semianalysis.com/p/google-we-have-no-moat-and-neither
16. [V] Bain Technology Report 2025 (23 Sept 2025): four-scenario agentic SaaS framework; recommends shift from access pricing to work-done pricing. https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
17. [V] Intercom prices Fin at $0.99 per outcome (accessed 2026-10-30). https://www.intercom.com/pricing
18. [V] Salesforce Agentforce: $2 per conversation, Flex Credits at $500 per 100,000 credits with 20 credits per action (about $0.10), plus per-user licences from $5 to $550 per user per month (accessed 2026-10-30). Shows hybrid seat plus usage plus outcome pricing. https://www.salesforce.com/agentforce/pricing/
19. [V] MCP introduced 25 Nov 2024; donated to the Agentic AI Foundation (Linux Foundation directed fund) 9 Dec 2025, co-founded by Anthropic, Block and OpenAI; 10,000+ active public servers; 97M+ monthly SDK downloads. https://www.anthropic.com/news/model-context-protocol and https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
20. [V] Google A2A protocol, 9 Apr 2025, 50+ technology partners at launch. https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
21. [V] Slack API terms effective 10 Oct 2025: external apps may not use API data to train an LLM, may not bulk export message data, and may not keep persistent indexes of other organizations' data. https://slack.com/terms-of-service/api
22. [V] Anthropic Cowork plugins, 30 Jan 2026: 11 open-source starter plugins for roles including legal, sales, finance, support and product management. https://claude.com/blog/cowork-plugins
23. [S] "SaaSpocalypse": about $300B of SaaS market value lost around 3 Feb 2026, per Inc. (Brian Contreras, 6 Feb 2026), whose URL references Anthropic. Primary article was not reachable (403). https://en.wikipedia.org/wiki/SaaSpocalypse and https://www.inc.com/brian-contreras/saaspocalypse-generative-ai-stock-market-anthropic-300-billion/91298739
24. [V] Chen (Greylock): AI-era revisit concludes the new moats are the old moats: workflows, data integration, trust, network effects, scale, go-to-market. https://greylock.com/greymatter/the-new-moats/
25. [V] Thompson, Aggregation Theory, 21 Jul 2015. https://stratechery.com/2015/aggregation-theory/
26. [V] Spolsky, Strategy Letter V, 12 Jun 2002: commoditize your complements; IBM PC and Microsoft examples. https://www.joelonsoftware.com/2002/06/12/strategy-letter-v/
27. [V] Cahn, Sequoia, 20 Jun 2024: GPU compute is commoditizing; high fixed cost and low marginal cost businesses see prices competed toward marginal cost. https://www.sequoiacap.com/article/ais-600b-question/
28. [V] Anthropic context engineering post, 29 Sept 2025. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## (c) Quotes (under 15 words)

1. "A moat that must be continuously rebuilt will eventually be no moat at all." Warren Buffett, Berkshire Hathaway 2007 letter. (15 words; trim to "A moat that must be continuously rebuilt will eventually be no moat" if a strict under-15 count is needed.)
2. "the set of conditions creating the potential for persistent differential returns" Hamilton Helmer's definition of Power, 7 Powers (2017), via Blas summary [S, check against book].
3. "Disruptive Innovations are NOT breakthrough technologies that make good products better" Christensen Institute.
4. "Smart companies try to commoditize their products' complements." Joel Spolsky, Strategy Letter V, 2002.
5. "Seat-based pricing may not fit when AI is doing the work." Bain Technology Report 2025.

## (d) 2025 to 2026 AI-era developments (verified unless tagged)

- Price collapse at constant capability continued: Epoch AI (Mar 2025) and Stanford AI Index 2025. Model access is a commodity input.
- Frontier and open-weight convergence (AI Index 2025).
- Bain (Sept 2025) framework for which SaaS workflows agentic AI will enhance, compress, outshine or cannibalize.
- Outcome and usage pricing goes mainstream: Intercom $0.99 per outcome; Salesforce Agentforce mixes per-conversation, per-action credits and per-user licences.
- Interoperability standards: A2A (Apr 2025), MCP to Linux Foundation AAIF (Dec 2025). Integration breadth is less of a moat.
- Data walls go up: Slack API terms (Oct 2025) restrict LLM training and indexing by third parties; Bain advises restricting AI platforms from learning on your data.
- Horizontal agents reach into vertical SaaS jobs: Anthropic Cowork plugins (Jan 2026) for legal, finance, sales, support and PM.
- Market reaction: "SaaSpocalypse" selloff of early Feb 2026 [S].
- Context engineering (Sept 2025) frames proprietary run-time context as the agent's real input.

## (e) Beacon worked example ideas (consistent with beacon-case.md)

- Run the 7 Powers assessment for Beacon honestly. Likely result:
  - Model access: no Power. Beacon calls the same frontier models rivals can call; inference cost is a margin issue (gross margin 81 to 72 percent), not a moat.
  - Switching costs: emerging. Allowlisted autonomous actions, tuned runbooks, approval policies and Sam's completed security review are costly to redo. Per Helmer the Benefit must show up as follow-on pricing (Beacon Agents upsell, NRR 118 percent).
  - Cornered resource or scale effect: resolved-incident history from the Learn loop. Be honest: per Casado and Lauten it is likely a data scale effect with diminishing returns, not a network effect, unless cross-customer learning (with consent) improves diagnosis acceptance rate for all customers.
  - Proprietary context: deep, governed access to Northlight Observe telemetry plus customer topology and change tickets. Strong for Observe customers, weak for tool-agnostic prospects. This is the book's strategic tension (build on Observe data versus stay tool-agnostic) seen as a moat trade-off.
  - Counter-positioning: per-resolved-incident pricing versus seat-priced incident tools. Rivals selling per responder seat would cut their own revenue by charging per resolution. This is Beacon's best candidate Power if the pricing move lands.
  - Branding (trust): fragile. The hallucinated root-cause incident (wrong service rolled back) shows hysteresis works both ways. Trust assets: cited evidence, approval gates, audit logs, AI Act documentation for EU customers.
  - Process power: the evals plus post-incident review pipeline that turns each resolved incident into a better eval set. Emerging; only a Power if hard to copy and compounding.
  - Network economies: Leo's MSP channel (60 customers each) could create a partner ecosystem; not a network effect yet.
- Moat scorecard for Beacon with "widened or narrowed this year" column (Buffett test). Example narrowing: correlation (Beacon Classic) commoditized as observability platforms ship AIOps grouping; this supports the sunset storyline.
- Commoditization response plan: "Correlate" is being commoditized by platform bundles and AI harnesses that can summarize alerts through MCP connectors. Response: treat correlation as a complement (make it cheap or free, possibly open the grouping schema), move value up to Diagnose and Act priced per resolved incident, and harvest Beacon Classic via the migration.
- Disruption check on a startup ops agent sold to mid-market teams with no SRE function at a low monthly price: low-end and new-market signs (nonconsumers, cheaper, worse on enterprise measures). Leo's MSP customers are the exposed flank. Contrast with a large observability vendor adding AI diagnosis for its own top customers: sustaining, not disruptive.
- Competitive threat monitor: the PM asks the AI harness, through connectors to win/loss notes, CRM, support tickets and competitor release notes, to classify each signal by type and moat row, with citations; Priya and Marcus quotes from customer calls feed it. Monthly review with product marketing.
- Data wall decision: whether Beacon's API terms should limit third-party agents from training on or indexing Beacon incident data, weighed against the tool-agnostic strategy and partner ecosystem (Slack precedent).

## (f) Editorial flags

1. Helmer primary site (7powers.com) returned 403. Power definition, Benefit and Barrier table come from a secondary summary (Blas) plus the Acquired interview. Verify wording against the book before quoting; prefer paraphrase.
2. Power Progression stage mapping (origination: counter-positioning, cornered resource; takeoff: scale, network, switching costs; stability: branding, process power) is from memory of the book; only "switching costs in takeoff" is verified. Check before stating.
3. Long-form fundamental equation (M0 x g x s x m) unverified.
4. Helmer's canonical examples for switching costs (SAP) and branding (Tiffany) unverified.
5. King and Baatartogtokh result (often cited as 9 percent of 77 cases) not visible in fetched text; do not state the number unless verified.
6. Christensen's Uber comment comes via Wikipedia citing HBR 2015 and Forbes 2016 [S]; HBR body was paywalled.
7. McGrath's transient advantage stage model and Grove's strategic inflection point not fetched; attribute by name only or verify.
8. SaaSpocalypse figures ($300B, Feb 2026) and its link to Anthropic product launches are secondary only; Inc. article returned 403. Do not assert causation.
9. NFX "70 percent of value" is NFX's own study claim; contested framing; attribute if used.
10. The leaked Google memo is an anonymous individual's opinion; do not present it as Google's position.
11. Buffett quote 1 is exactly 15 words; trim or paraphrase to meet the under-15 rule.
12. Pricing pages (Intercom, Salesforce) change often; state "as of October 2026".
13. Web search budget was exhausted at the start of this run; coverage of AI-era SaaS disruption commentary (analyst views, counter-arguments that systems of record gain from agents) is thinner than ideal. A follow-up pass could add one or two independent analyses.
