# Research notes: Chapter 02, Product Vision and Goals

Prepared 2026-10-30 for *The Product 360 Handbook* (2026 edition). Audience: Senior to Principal PMs, B2B enterprise and platform products. Maps to the eCornell course "Product Vision and Goals" (set a product vision, break the business into parts, define objectives and key results).

**Verification key**
- **[V]** Verified this session against the primary source or the author's own site (URL given).
- **[S]** Verified only through secondary sources. Check the primary before quoting.
- **[U]** Unverified. From general knowledge or a single weak source. Confirm before print.

---

## Part A. Key concepts and frameworks

### 1. Vision (Roman Pichler)

- **Definition [V]:** Pichler calls the product vision the overarching goal and the reason for creating the product; it describes the positive change the product brings about. It gives a lasting purpose, a "true north". Source: Pichler, "8 Tips for Creating a Compelling Product Vision", romanpichler.com, first published 8 Oct 2014, updated 15 Feb 2023. https://www.romanpichler.com/blog/tips-for-writing-compelling-product-vision/
- **Eight tips [V] (paraphrased):** (1) ground it in why you care and what change it should bring; (2) focus on the change, not the product; (3) keep vision and strategy separate so you can pivot without losing purpose; (4) build it collaboratively so it is shared; (5) choose a vision that benefits others; (6) make it broad and ambitious; (7) keep it short and memorable; (8) use it as the first filter for ideas and change requests.
- **Time horizon:** In a comment reply on that post, Pichler says the vision should guide for at least three to five years [V]. Other Pichler pages (via search snippet) say "five to ten years" [S]. Flag: both appear; book can say "several years, often five or more".
- **Purpose vs solution [S, search snippet from romanpichler.com]:** Pichler contrasts a solution-focused vision (build an AI coding assistant with autonomous agents) with a purpose-driven one (help people create software at the speed of thought). Good 2026 example of the trap: naming the AI technique in the vision.
- **Product Strategy Framework v3 [V]:** Pichler, "The Product Strategy Framework: A Revised Guide for Product Leaders", 11 May 2026. https://www.romanpichler.com/blog/romans-product-strategy-framework-v3/ Layers top to bottom: **product vision** (purpose, stable, not measurable, often a slogan); **product strategy** (approach to realise the vision, guardrails for discovery, usually 12 to 24 months, four choices: target market, customer needs, standout features, business goals; reviewed at least every three months); **product roadmap** (outcome-based product goals, optional time frames, coarse features, metrics); **product backlog**. KPIs sit outside the framework, derived from strategy needs, business goals and roadmap outcomes. He says OKRs can work at roadmap level but are not suited to vision or strategy.
- **PM application:** Use the vision as the stable layer; let strategy change quarterly. In B2B platforms, the vision should describe the change for the customer's organisation (for example, on-call teams), not for Northlight.

### 2. Product Vision Board (Roman Pichler)

- **Format [V for sections, romanpichler.com/tools/product-vision-board/]:** Vision statement across the top; four cells beneath: **Target Group**, **Needs**, **Product** (key features, the standout three to five), **Business Goals**. Extended version adds business model cells: **Competitors**, **Revenue Sources**, **Cost Factors**, **Channels**. https://www.romanpichler.com/tools/product-vision-board/
- **Guiding questions [S]:** Vision: why are you creating this product, what positive change should it bring? Target group: which market or segment, who are the users and customers? Needs: what problem does it solve, what benefit does it provide? Product: what is it, what makes it stand out, is it feasible? Business goals: how will it benefit the company?
- **License [S]:** Third-party template sites say it is released under Creative Commons Attribution-ShareAlike 3.0. Pichler's page did not state a licence. Do not reproduce his graphic; describe the layout in prose or redraw generically.
- **PM application:** One board per product, not per feature. For a platform, Target Group usually has two or more rows (users, economic buyer, partners). The board is the bridge between vision and the strategy chapter (ch03).

### 3. Vision narratives: Amazon Working Backwards (PR/FAQ) and the six-pager

- **Origin [V]:** Colin Bryar and Bill Carr, *Working Backwards: Insights, Stories, and Secrets from Inside Amazon* (St. Martin's Press, 2021). Amazon published an excerpt: "An insider look at Amazon's culture and processes", aboutamazon.com (undated page). https://aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes
- **PR/FAQ format [V on excerpt]:** a press release of a few paragraphs, always under one page, written as if announcing the finished product to customers; followed by an FAQ of five pages or less. Reviewers push on the "so what?" of each claim. The excerpt says there are no awards for extra pages.
- **Internal vs external FAQ [S]:** Book summaries describe external (customer and press) questions and internal (stakeholder: cost, feasibility, risk, P&L) questions. Not on the excerpt page; confirm in the book.
- **Six-pager [S]:** A separate narrative memo format (up to six pages, read silently at the start of the meeting) used for proposals and reviews; the PR/FAQ is the narrative used for new products. The silent-reading start is widely reported; confirm wording in the book.
- **Typical PR sections [S, widely reproduced, not checked against the book]:** headline; subheading (who the customer is and the benefit); summary paragraph; problem; solution; quote from a company spokesperson; how to get started; customer quote; closing call to action.
- **PM application (vision narrative):** A vision narrative is longer and more concrete than a vision statement: it describes a day in the life of the customer three to five years out, after the product has done its job. For B2B, write the PR from the economic buyer's and the daily user's points of view, and put security, procurement and partner questions in the internal FAQ. 2026 practice: draft with an AI harness from interview evidence, then cut by hand; the narrative is a thinking tool, so the PM must own every claim.

### 4. Positioning-style vision (Geoffrey Moore)

- **Origin [S]:** Geoffrey A. Moore, *Crossing the Chasm* (HarperBusiness, 1991; 3rd ed. 2014). Moore's positioning statement, sometimes called the "elevator test", is widely used as a short vision or product-concept statement. The primary text was not available online this session; wording below is the standard reproduction.
- **Template [S]:**
  > For [target customers] who are dissatisfied with [the current market alternative], our product is a [new product category] that provides [key problem-solving capability]. Unlike [the product alternative], we have assembled [key whole-product features for your specific application].
- **Common simplified variant [S]:** For [target customer] who [statement of need or opportunity], the [product name] is a [product category] that [key benefit, reason to buy]. Unlike [primary competitive alternative], our product [statement of primary differentiation].
- **Placement in this chapter:** Moore's format is a positioning statement, not a purpose vision in Pichler's sense. Use it as the "product concept" line under the vision (who, category, benefit, differentiation). Ch on positioning and GTM can go deeper.
- **PM application:** In B2B, the "current market alternative" is often a manual process (humans plus runbooks) rather than a competitor. Write one statement per buying segment if the alternative differs.

### 5. Vision vs mission vs strategy (working definitions for the book)

- **Mission [synthesis]:** what the organisation exists to do, enduring, company-level. **Vision [Pichler, V]:** the positive change a product brings about; stable, purpose-driven, not measurable. **Strategy [Pichler, V; also Rumelt, see ch03]:** the chosen approach to realise the vision: target market, needs, standout features, business goals; reviewed at least quarterly. **Goals [Pichler, V]:** outcome-based product goals on the roadmap, measured with KPIs; OKRs operate here, not at vision level.
- **Flag:** "Mission" vs "vision" usage is inconsistent across sources (some companies call the long-range aspiration the mission). The chapter should define terms for this book and note the inconsistency rather than claim one correct usage.

### 6. North Star Metric (Sean Ellis; Amplitude North Star Framework)

- **Sean Ellis definition [S]:** The North Star Metric is the single metric that best captures the core value a product delivers to customers. Ellis stresses one metric, not several. Examples commonly attributed to his talks: Airbnb nights booked, Facebook daily active users. Secondary only (revelx.co, saasacademy.com); confirm wording against *Hacking Growth* (Ellis and Morgan Brown, Crown Business, 2017) before quoting.
- **Amplitude North Star Framework [V]:** Amplitude blog, Julia Sholtz, "Every Product Needs a North Star Metric" (published 20 Aug 2024). https://amplitude.com/blog/product-north-star-metric
  - A good North Star Metric aligns to customer value, represents product strategy, and is a leading indicator of success. It pairs a statement of product vision with a metric that measures the current strategy.
  - **Three games [V]:** Attention (how much time customers are willing to spend in the product); Transaction (how many transactions users make on the platform); Productivity (how efficiently and effectively someone gets their work done). Most B2B SaaS, including Beacon, plays the productivity game.
  - **Inputs [V]:** three to five influential, complementary factors that most directly affect the North Star and that the team can influence through the product. Breadth, depth, frequency and efficiency are suggested lenses for finding inputs.
- **North Star Playbook [V for existence and authorship]:** Amplitude, *The North Star Playbook*, co-authored by John Cutler (former Amplitude product evangelist) with others. https://amplitude.com/books/north-star/about-north-star-framework The intro frames the framework as connecting the language of the customer, of the product and of the business. Full checklist text not retrievable this session [U for any further detail, including the "greenfield test" for inputs].
- **Avoid [V, Amplitude blog]:** vanity metrics and lagging indicators such as MRR or ARPU as the North Star.
- **Metric tree (input-metric tree):** The North Star at the root, three to five inputs beneath, and team-level drivers beneath each input. Each team owns one input. B2B variant: add a counter-metric (guardrail) at each level, for example quality or cost, so teams cannot game an input.
- **PM application (B2B and platform):** Pick a value metric at the customer's unit of value (resolved incidents, approved invoices, deployments shipped), not seats or logins. Platform businesses often need a two-sided view (developers building on the platform and end customers using what they build), so state which side the North Star measures and give the other side an input.

### 7. Outcomes over output (Josh Seiden; Jeff Gothelf)

- **Definition [V]:** Seiden defines an outcome as a change in human behaviour that drives business results. Source: Intercom podcast with Josh Seiden, 4 Jul 2019. https://www.intercom.com/blog/podcasts/josh-seiden-on-why-product-teams-should-focus-on-outcome-vs-output Book: Seiden, *Outcomes Over Output* (Sense & Respond Press, 2019). Some secondary versions add "measurable" [S].
- **Output, outcome, impact [V]:** Drawing on the Kellogg Foundation's Logic Model, outputs are what teams make, outcomes are the customer behaviour changes those produce, and impact is the business result at the top. Seiden warns against handing high-level impact goals (for example "cut costs") to small teams; give them outcomes they can move.
- **Key questions [V]:** What will people be doing differently as a result of this feature? How will you know?
- **PM application:** Write key results as behaviour changes of named actors ("on-call engineers accept the proposed root cause"), not as shipped features ("launch diagnosis v2"). Ship dates belong in the delivery plan.

### 8. OKRs: Grove, Doerr, Google, Wodtke, Cagan

- **Origin [S]:** Andy Grove developed the method at Intel in the 1970s, building on Peter Drucker's management by objectives; Grove called it iMBOs (Intel Management by Objectives). Grove described it in *High Output Management* (Random House, 1983). John Doerr learned it at Intel (Wikipedia says 1975 [S]), introduced it to Google in 1999 [U, widely reported], and popularised it in *Measure What Matters* (Portfolio, 2018).
- **Doerr's definitions [V]:** whatmatters.com (Doerr's site) says an objective is what is to be achieved, no more and no less; objectives are significant, concrete, action-oriented and ideally inspirational. Key results measure progress toward the objective; they are specific, time-bound, aggressive yet realistic, and either met or not. Typically one objective with three to five key results. https://www.whatmatters.com/faqs/okr-meaning-definition-example
- **Doerr's formula [V]:** "I will (Objective) as measured by (Key Results)."
- **Committed vs aspirational [V]:** committed OKRs are expected to be fully achieved; aspirational (stretch, "moonshot") OKRs may not be and can span cycles. Google scores each KR 0.0 to 1.0 and averages; Grove's approach is yes or no; some use red, yellow, green.
- **FACTS [V]:** Doerr's OKR "superpowers": Focus, Alignment, Commitment, Tracking, Stretching.
- **0.7 sweet spot [U]:** Google's re:Work guidance that 0.6 to 0.7 is a good score for aspirational OKRs is widely cited; not verified this session.
- **Christina Wodtke [S]:** *Radical Focus* (Cucina Media, 2015; 2nd ed. 2021). Objectives are qualitative and inspirational; key results are quantitative, typically three; key results should be set so the team has roughly a 50/50 chance of hitting them. The "four-square" weekly status: priorities for the week, confidence in each KR, the OKR, and health metrics. Monday commitments and Friday wins rituals. Secondary sources only this session (readingraphics, speakerdeck summary); confirm in the book.
- **Marty Cagan [V]:** "Team Objectives: Overview", SVPG, 24 Feb 2020. https://svpg.com/team-objectives-overview/ After years advocating OKRs, he says he stopped recommending the practice in most companies he meets. Reasons: feature-team cultures (OKRs are an empowerment technique), objectives given while solutions are still dictated by feature roadmaps with dates, functional managers cascading their own objectives, individual objectives diluting team focus, and leaders who set and forget. Remedy: empowered product teams, team (not manager or individual) objectives, and active leadership that turns strategy into problems to solve. Follow-up article "Team Objectives: Accountability" suggests treating a badly missed objective like an outage review with peers [S].
- **Common OKR failures (synthesis for the chapter; each tied to a source above):** too many objectives (Doerr: focus); key results that are tasks or outputs (Seiden; Wodtke's "is it a result or a task?" test [S]); cascading by function or individual (Cagan); OKRs alongside a fixed feature roadmap (Cagan); set and forget with no weekly check-in (Wodtke, Cagan); sandbagged or impossible targets with no stated confidence (Wodtke 50/50; Doerr committed vs aspirational); OKRs tied to compensation [U: Doerr and Google advise separating them; verify]; no counter-metrics so teams game the KR (synthesis).

### 8a. Additions on OKRs (verified after section 8 was drafted)

- **Google's OKR Playbook [V]:** reproduced on whatmatters.com (author listed as Google, undated). https://www.whatmatters.com/resources/google-okr-playbook Committed OKRs are ones "we agree will be achieved"; expected score 1.0, and a miss needs a postmortem that is not meant to punish. Aspirational OKRs express how we would like the world to look; expected average score 0.7, with high variance. Named traps: failing to separate committed from aspirational; business-as-usual OKRs; timid aspirational OKRs; sandbagging; low-value objectives; insufficient KRs for committed objectives. This resolves the [U] on the 0.7 figure above: it is now [V] via the Playbook reproduction.
- **Wodtke, "The Art of the OKR" [V]:** eleganthack.com, 1 Feb 2014. https://eleganthack.com/the-art-of-the-okr/ Objectives are qualitative, inspirational, time-bound (month or quarter) and achievable by the team without depending on others. Typically three key results, quantitative (growth, engagement, revenue, performance, quality). KRs should be difficult, not impossible; set confidence around 5 out of 10. Review confidence weekly; do not change OKRs mid-period. Note: this 2014 post recommends one company OKR plus one per team and individual OKRs; *Radical Focus* 2nd ed. may differ [U].
- **Cagan on accountability [V]:** "Team Objectives: Accountability", SVPG, 4 Mar 2020. https://svpg.com/team-objectives-accountability/ Accountability scales with ambition: missing a moonshot is expected; missing a conservative "roof shot" or a high-integrity commitment is where accountability applies. Treat a substantial miss like an outage: a team objective post-mortem with peers, especially affected teams.
- **Criticisms collected on Wikipedia [S]:** many organisations no longer set individual OKRs because they become task lists and get conflated with performance reviews; multi-level OKRs can recreate waterfall planning. https://en.wikipedia.org/wiki/Objectives_and_key_results Wikipedia also gives: Grove popularised OKRs at Intel in the 1970s; *High Output Management* 1983; Doerr attended Grove's course in 1975 as an Intel salesperson; by 1999 Doerr was at Kleiner Perkins and introduced OKRs to Google.
- **Gothelf and Seiden, *Who Does What By How Much? A Practical Guide to Customer-Centric OKRs* [S]:** Sense & Respond Press, 2024 (publisher page says 28 May 2024; retailer lists 31 May 2024). Gothelf blog announcing it, 3 Jun 2024 [V for existence]: https://jeffgothelf.com/blog/who-does-what-by-how-much/ The title is the key-result pattern: a named customer or user (who) does a specific behaviour (what) by a measurable amount (how much). The formal wording of the formula was not retrievable [U]; use the title as the pattern and attribute it.

### 9. Breaking the business into parts

The eCornell course asks PMs to break the business into parts before setting goals. Four lenses, each with a source:

- **Business model components (Osterwalder and Pigneur) [S]:** *Business Model Generation* (Wiley, 2010). The nine building blocks: Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure. Strategyzer's page confirms nine blocks covering who you serve, what you offer, how you deliver, what it costs and what it earns, but does not list names [V for count only]. https://www.strategyzer.com/library/the-business-model-canvas Ch01 already uses Lean Canvas; here the BMC is used to find which component each goal moves (for example, a pricing change moves Revenue Streams and Cost Structure).
- **Value streams (SAFe) [V]:** Scaled Agile Framework, "Value Streams", last updated 10 Mar 2025. https://framework.scaledagile.com/value-streams/ An **operational value stream** is the set of activities that deliver a product or service to a customer (example: a purchase order through to delivery). A **development value stream** is the sequence of activities that turns a business hypothesis into a digitally enabled solution. For a PM, the customer's operational value stream (for Beacon: detect, triage, diagnose, act, learn) is the best spine for decomposing the product and its metrics.
- **Team-aligned decomposition (Skelton and Pais, Team Topologies) [V]:** teamtopologies.com key concepts. https://teamtopologies.com/key-concepts Four team types: stream-aligned (aligned to a flow of work from, usually, a segment of the business domain), enabling, complicated-subsystem, platform. Three interaction modes: collaboration, X-as-a-service, facilitation. Book: *Team Topologies* (IT Revolution, 2019) [S for year]. Use: product areas should map to streams so that each team can own an input metric end to end.
- **Product areas and capability map (synthesis):** list the product's capabilities (Beacon: Correlate, Diagnose, Act, Learn, plus connectors and platform), the segments (direct enterprise, MSP partners), and the revenue components. A 3-axis decomposition (capability x segment x business model component) shows where goals overlap and who owns what.
- **Why this matters for goals:** decomposition is what lets a single North Star fan out into an input-metric tree where each input has one owning team. If two teams share an input, either merge the input or split it.

### 10. Goal-setting for AI products

- **Success criteria for LLM features [V]:** Anthropic's documentation, "Define your success criteria" (platform.claude.com docs, page current 2026). https://platform.claude.com/docs/en/docs/test-and-evaluate/define-success Good criteria are specific, measurable, achievable and relevant. Its example is multidimensional (an accuracy score, a non-toxic output rate, an error-severity share, and a latency percentile on a held-out test set). Common criteria categories: task fidelity, consistency, relevance and coherence, tone and style, privacy preservation, context utilisation, latency, price.
- **People + AI Guidebook (Google PAIR) [V]:** "User Needs + Defining Success" chapter, undated. https://pair.withgoogle.com/chapter/user-needs/ Start from a real user need and ask whether AI adds unique value; a rule-based approach may be simpler. Automation suits tedious, hard or risky tasks; augmentation suits tasks people enjoy or own. The reward function shapes the experience; design it across UX, product and engineering, and watch long-term effects. Weigh false positives and false negatives by real-world cost, not equally. Precision vs recall is a trade-off to set with real users. Set explicit thresholds that trigger action (for example a rising rejection rate prompts model review).
- **Trustworthy AI framing (NIST) [V for dates]:** NIST AI RMF 1.0 released 26 Jan 2023; four functions Govern, Map, Measure, Manage; Generative AI Profile (NIST-AI-600-1) released 26 Jul 2024; on 7 Apr 2026 NIST released a concept note for a critical-infrastructure profile; the RMF is being revised under the White House AI Action Plan (no date given). https://www.nist.gov/itl/ai-risk-management-framework The trustworthiness characteristics list was not on that page [U for the exact list; commonly given as valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, fair with harmful bias managed].
- **Book's model for AI goals (synthesis for the chapter):** an AI product's goal set has four families, all needed: (1) **value** (the outcome for the customer, the North Star); (2) **quality** (eval pass rates on a held-out set, task fidelity, error severity); (3) **trust** (acceptance rate, override rate, wrong-action rate, user-reported confidence, audit completeness); (4) **cost** (inference cost per unit of value, gross margin). Quality, trust and cost usually sit as guardrails (must not fall below or rise above X) rather than as the objective. This four-family model is the author's synthesis; label it.
- **Pricing tied to outcomes as a goal signal [V]:** Stripe, "A framework for pricing AI products", 11 Sep 2025 (Kunal Mahajan, Helen Lee). https://stripe.com/blog/a-framework-for-pricing-ai-products Three charge-metric types: consumption (per unit of usage; predictable for the seller, weak link to value), workflow (per completed task), outcome (only when a defined result happens; closest to customer value, highest cost risk for the seller). When the price metric is an outcome, the North Star and the revenue metric converge, and inference cost becomes a first-class goal.
- **Intercom Fin [V]:** Fin is priced at $0.99 per resolution, where a resolution is counted when no further help is requested after Fin's last answer; billed once per conversation. https://fin.ai/pricing (page current Oct 2026). Intercom's blog (Aisling O'Reilly, 28 Apr 2025) argues outcome pricing ties vendor revenue to results and lets buyers compare AI cost with human cost; it notes forecasting is harder. https://www.intercom.com/blog/pricing-ai-agents/ Use only as a verified real-world example of an outcome metric doubling as a price metric; do not extend beyond what the pages say.

---

## Part B. Verified facts (with URL and date)

| # | Fact | Source | Date | Tag |
|---|---|---|---|---|
| 1 | Pichler defines product vision as the overarching goal and the reason for creating the product; eight tips listed in Part A.1 | https://www.romanpichler.com/blog/tips-for-writing-compelling-product-vision/ | 2014, updated 15 Feb 2023 | [V] |
| 2 | Pichler's vision qualities: inspiring, shared, ethical, concise, ambitious, enduring (five to ten years) | https://www.romanpichler.com/blog/product-vision-board-checklist/ | 31 Jan 2023, updated 31 Jan 2024 | [V] |
| 3 | Product Vision Board cells: vision, target group, needs, product, business goals; extended adds competitors, revenue sources, cost factors, channels | https://www.romanpichler.com/tools/product-vision-board/ | page current 2026 | [V] |
| 4 | Pichler framework v3: vision, strategy (12 to 24 months, reviewed at least quarterly), roadmap, backlog; OKRs suited to roadmap not vision | https://www.romanpichler.com/blog/romans-product-strategy-framework-v3/ | 11 May 2026 | [V] |
| 5 | Cagan: vision describes the future we are trying to create; can be a narrative, storyboard or prototype ("visiontype"); typically 2 to 5 years, hardware 5 to 10 | https://www.svpg.com/vision-vs-strategy/ | 15 Jul 2016 | [V] |
| 6 | Amazon PR is under one page; FAQ five pages or less | https://aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes | undated excerpt of 2021 book | [V] |
| 7 | Amplitude NSM criteria: customer value, product strategy, leading indicator; three games; three to five inputs | https://amplitude.com/blog/product-north-star-metric | 20 Aug 2024 | [V] |
| 8 | John Cutler co-authored Amplitude's North Star Playbook | https://amplitude.com/books/north-star/about-north-star-framework | page current 2026 | [V] |
| 9 | Seiden: outcome is a change in human behaviour that drives business results | https://www.intercom.com/blog/podcasts/josh-seiden-on-why-product-teams-should-focus-on-outcome-vs-output | 4 Jul 2019 | [V] |
| 10 | Doerr's OKR formula and definitions; 3 to 5 KRs; FACTS | https://www.whatmatters.com/faqs/okr-meaning-definition-example | page current 2025 | [V] |
| 11 | Google: committed OKRs expected 1.0; aspirational average 0.7; six named traps | https://www.whatmatters.com/resources/google-okr-playbook | undated | [V] |
| 12 | Wodtke: ~3 KRs, 50/50 confidence, weekly confidence review | https://eleganthack.com/the-art-of-the-okr/ | 1 Feb 2014 | [V] |
| 13 | Cagan stopped recommending OKRs in most companies; five failure causes | https://svpg.com/team-objectives-overview/ | 24 Feb 2020 | [V] |
| 14 | Cagan: accountability tied to ambition; miss reviewed like an outage | https://svpg.com/team-objectives-accountability/ | 4 Mar 2020 | [V] |
| 15 | Grove, Intel, iMBOs; Doerr 1975; HOM 1983; Google 1999 | https://en.wikipedia.org/wiki/Objectives_and_key_results | page current | [S] |
| 16 | SAFe operational vs development value streams | https://framework.scaledagile.com/value-streams/ | updated 10 Mar 2025 | [V] |
| 17 | Team Topologies four team types, three interaction modes | https://teamtopologies.com/key-concepts | page current | [V] |
| 18 | Anthropic success criteria: specific, measurable, achievable, relevant; eight criteria categories | https://platform.claude.com/docs/en/docs/test-and-evaluate/define-success | page current 2026 | [V] |
| 19 | Google PAIR: weigh false positives and negatives by cost; precision vs recall | https://pair.withgoogle.com/chapter/user-needs/ | undated | [V] |
| 20 | NIST AI RMF 1.0 26 Jan 2023; GenAI Profile 26 Jul 2024; CI profile concept note 7 Apr 2026 | https://www.nist.gov/itl/ai-risk-management-framework | page current 2026 | [V] |
| 21 | Stripe: consumption, workflow, outcome pricing metrics | https://stripe.com/blog/a-framework-for-pricing-ai-products | 11 Sep 2025 | [V] |
| 22 | Fin $0.99 per resolution; resolution definition | https://fin.ai/pricing | page current Oct 2026 | [V] |
| 23 | EU AI Act: in force 1 Aug 2024; prohibitions 2 Feb 2025; GPAI 2 Aug 2025; general application 2 Aug 2026; high-risk Annex III 2 Dec 2027, Annex I 2 Aug 2028 (per site updated 31 Aug 2026) | https://artificialintelligenceact.eu/implementation-timeline/ | updated 31 Aug 2026 | [S] (non-official site; confirm on EUR-Lex) |

---

## Part C. Short quotes (under 15 words)

1. Roman Pichler on product vision: "the overarching goal you are aiming for, the reason for creating the product." romanpichler.com, 8 Tips (2014, updated 2023).
2. Josh Seiden: "An outcome is a change in human behavior that drives business results." Intercom podcast, 4 Jul 2019.
3. Marty Cagan on OKRs: "first and foremost an empowerment technique." SVPG, Team Objectives: Overview, 24 Feb 2020.
4. Marty Cagan: "accountability is directly related to ambition." SVPG, Team Objectives: Accountability, 4 Mar 2020.
5. Marty Cagan: the product vision "describes the future we are trying to create." SVPG, Vision vs. Strategy, 15 Jul 2016.

---

## Part D. 2025 to 2026 AI-era developments (verified)

- **Pichler's framework v3 (11 May 2026) [V]:** places OKRs at roadmap level only and keeps KPIs outside the framework; uses an AI coding assistant as his example of a solution-focused (bad) vision [S on the example]. Useful 2026 anchor for "do not name the technology in the vision".
- **Outcome-based AI pricing becomes mainstream enough for Stripe to codify it (11 Sep 2025) [V]:** consumption vs workflow vs outcome metrics. For AI agent products, the unit of value, the North Star and the price meter increasingly coincide.
- **Intercom Fin, $0.99 per resolution (current Oct 2026) [V]:** an example of a value metric (resolution) used as both success metric and price, with a published definition of what counts.
- **Intercom on value-based AI pricing (28 Apr 2025) [V]:** buyers can compare AI resolution cost with human cost; forecasting is the weak point.
- **NIST (2024 to 2026) [V]:** Generative AI Profile (Jul 2024); critical-infrastructure profile concept note (7 Apr 2026); RMF revision under the White House AI Action Plan. Trust goals can map to Govern, Map, Measure, Manage.
- **EU AI Act (2025 to 2026) [S]:** prohibitions applied 2 Feb 2025; GPAI rules 2 Aug 2025; general application 2 Aug 2026; high-risk dates shown as 2 Dec 2027 (Annex III) and 2 Aug 2028 (Annex I) on a site updated 31 Aug 2026, which implies the delay proposed in the EU's Digital Omnibus was adopted [U on the mechanism; confirm on EUR-Lex]. Relevant to Beacon's EU storyline and to trust goals.
- **Gothelf and Seiden, *Who Does What By How Much?* (2024) [S]:** customer-centric OKRs; a speaker profile says it addresses AI-era productivity and value delivery [U on content].
- **Practice shift for the chapter (synthesis, not a fact):** with an AI harness connected to analytics, CRM and support data through connectors, a PM can draft a metric tree, test whether candidate inputs move with the North Star historically, and produce a weekly goal review. Teach the questions and prompts, not the queries.

---

## Part E. Beacon worked example ideas (consistent with beacon-case.md)

- **Vision statement (draft):** "Every on-call team can resolve incidents before customers feel them, without losing sleep or control." Purpose-driven, names no technique (not "agents"), passes Pichler's six qualities. Check: shared (Priya, Dana, Marcus), ethical (human approval gate), enduring.
- **Positioning line (Moore format):** For IT operations and SRE teams at large enterprises who are drowning in alerts and still diagnosing incidents by hand with runbooks and chat, Beacon is an AI incident agent platform that correlates alerts, diagnoses root cause with cited evidence and runs approved fixes. Unlike AIOps features inside a single observability suite, Beacon works across the customer's tools through connectors and keeps a human approval gate on every risky action. (Note strategic tension: tool-agnostic vs Northlight Observe data; the positioning line forces the choice.)
- **Vision narrative:** a PR/FAQ dated at Northlight Live, announcing Beacon Agents. Headline about Dana being paged at 3 a.m. and finding the incident already diagnosed with a proposed rollback awaiting approval. Internal FAQ covers Sam's questions (least privilege, audit logs, data residency, AI Act documentation), inference cost and margin (81% to 72%), and per-resolved-incident pricing. External FAQ includes Leo (MSP multi-tenant views).
- **Product Vision Board:** Target group rows: SRE leads and on-call engineers (users), VP IT Ops (buyer), security reviewer (gatekeeper), MSPs (partner). Needs: fewer pages, diagnosis under five minutes, trust, ROI. Product: Correlate, Diagnose, Act, Learn. Business goals: ARR growth (38%), NRR (118%), margin recovery.
- **Decomposition:** capability axis (Correlate, Diagnose, Act, Learn, connectors); segment axis (direct enterprise, MSP); business model axis (platform fee per environment, usage, per-resolved-incident). Customer's operational value stream: detect, correlate, diagnose, decide, act, learn. Map each of the 5 engineering teams to a stage.
- **North Star and metric tree:** North Star is incidents resolved with Beacon's help per week (given). Inputs (three to five, using breadth, depth, frequency, efficiency): (1) breadth: weekly active responders, or environments with full connector coverage; (2) depth: diagnosis acceptance rate; (3) efficiency: alert-to-incident compression ratio and time to diagnosis; (4) autonomy: autonomous resolution rate on allowlisted actions. Guardrails: wrong-action rate (link to the hallucinated root cause storyline), inference cost per resolved incident (margin), MTTR must not rise, customer-reported trust. Note the game: productivity game.
- **OKR set (quarter, illustrative):** Objective: "On-call engineers trust Beacon's diagnosis enough to act on it." KRs (who does what by how much): diagnosis acceptance rate rises from X to Y across enterprise customers; responders who approve a Beacon-proposed action within 10 minutes rises from X to Y; wrong-root-cause reports per 1,000 diagnoses fall below Z (committed); inference cost per resolved incident falls by N% (committed guardrail). Mark one OKR aspirational (autonomous resolution) and one committed (quality guardrail). Leave numbers as placeholders unless the case file supplies them; only MTTR names, ratios and NRR 118%, margin 81 to 72%, ARR $48M, 420 customers, 38% growth are given.
- **Bad OKR to critique:** "Ship Beacon Agents GA by Northlight Live; launch 12 new connectors; publish AI Act docs" (all outputs, no behaviour change, deadline-driven, matches Cagan's failure of OKRs alongside a feature roadmap).
- **Goal review:** a monthly review the PM runs with an AI harness: pull North Star and input trends, eval pass rates and cost per resolved incident from connected sources; flag which inputs moved without moving the North Star (broken causal link); confidence per KR (Wodtke); post-mortem on any missed committed KR (Cagan's outage framing). Use the hallucinated root cause incident as the trigger for adding a guardrail KR.
- **Pricing link:** moving to per-resolved-incident pricing aligns North Star, price meter and customer value (Stripe's outcome metric; Fin as a real-world analogue). Requires a published definition of "resolved with Beacon's help" so customers can audit it.

---

## Part F. Editorial flags

1. **Vision time horizon conflict:** Pichler gives at least three to five years (2014 post comment) and five to ten years (2023 checklist); Cagan gives 2 to 5 years (5 to 10 for hardware). Present as a range and attribute each.
2. **Moore positioning template:** wording not verified against *Crossing the Chasm*; the long form ("dissatisfied with the current market alternative ... whole product") and the short form circulate. Confirm in the 3rd edition before printing either verbatim.
3. **Sean Ellis NSM definition:** secondary only. Confirm in *Hacking Growth* (2017) or an Ellis primary source before attributing exact wording.
4. **Amplitude North Star Playbook checklist and "greenfield test":** chapter text not retrievable; rely on the 2024 Amplitude blog for criteria, games and inputs. Playbook co-authors beyond John Cutler not confirmed.
5. **Doerr introduced OKRs to Google in 1999:** Wikipedia [S]; widely reported; confirm in *Measure What Matters*.
6. **OKRs and compensation:** often said Google and Doerr advise decoupling; not verified this session. Google's Playbook (as reproduced) only says a missed committed OKR's postmortem is not punitive.
7. **Wodtke details:** four-square and Monday commitments / Friday wins are from secondary summaries; her 2014 post supports 3 KRs, 5/10 confidence and weekly check-ins. Her 2014 post endorses individual OKRs, which conflicts with Cagan and with later practice; present as a disagreement.
8. **Cagan's stance is contested:** he stopped recommending OKRs in most companies (2020) while *Empowered* (2020) describes team objectives with key results. Present as "OKRs only work with empowered teams", not "Cagan rejects OKRs".
9. **Amazon PR/FAQ section list and internal/external FAQ:** secondary only.
10. **Gothelf and Seiden formula wording:** only the book title is verified; publication date differs by source (28 vs 31 May 2024).
11. **NIST trustworthy characteristics list:** not on the fetched page; confirm in AI RMF 1.0 document before listing.
12. **EU AI Act high-risk dates:** taken from a non-official tracker; confirm on EUR-Lex, and do not describe the Digital Omnibus outcome without a primary source.
13. **Four-family AI goal model (value, quality, trust, cost) and the B2B "adoptability" style additions:** author's synthesis; label as the book's framework.
14. **Mission vs vision terminology:** no authoritative single definition; define for the book and note variance.
15. **Search budget:** the session's web search limit was reached before Christina Wodtke's *Radical Focus* 2nd ed., Grove's *High Output Management* and Doerr's *Measure What Matters* could be checked directly; treat details from them as [S] until checked.
