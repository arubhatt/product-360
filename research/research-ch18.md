# Research notes: Chapter 18, The Product Data Landscape and the Reports That Matter

Status: complete (2026-10-30). Raw source log first, organized notes below.

## Running source log (raw, appended as read)

### S1. Cedric Chin, "The Amazon Weekly Business Review (WBR)", Commoncog. Published 2024-07-02, updated 2026-06-14. https://commoncog.com/the-amazon-weekly-business-review/ [S for Amazon facts; V for Commoncog's own description]
- WBR held by Amazon exec team since early 2000s; hundreds of metrics; framed as a process control tool to uncover the causal structure of the business.
- Answers three questions: what did customers experience last week, how did the business do, are we on track to targets.
- Cadence: metric owners look daily; Monday owners review; Tuesday department WBRs; Wednesday company WBR, 60 minutes (90 in holiday season), Finance facilitator.
- Exception-driven: owners speak only to exceptional variation or missed targets; routine metrics get "nothing to see here"; if no root cause, owner says "I don't know" and the facilitator logs a follow-up. No improvised explanations.
- Deck ordered causally: controllable input metrics first, then related output metrics, then financials. Static deck, every metric shown, fast handoffs.
- Amazon deck 400 to 500 metrics (per Chin); Commoncog's own deck has 47.
- Controllable input metrics = actionable levers; output metrics = outcomes (revenue, free cash flow). Outputs reported but teams work on inputs. Metrics added or dropped as predictive power changes.
- Chart formats: "6-12 graph" (trailing 6 weeks left, trailing 12 months right, prior-year line faded, targets as triangles from OP1/OP2 planning, box score below); 6-12 table for many entities (e.g., top customers); plain table. Consistent visual formats build familiarity.

### S2. dbt Labs, "dbt Semantic Layer" docs. Last updated 2026-09-29. https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl [V]
- Define metrics once on top of dbt models; the layer handles joins. Problem: metric logic duplicated across BI tools and applications. Moving definitions from BI layer to modeling layer means every unit uses the same definitions and a change propagates everywhere. Powered by MetricFlow.
- AI tools (Claude, ChatGPT) can connect through the dbt MCP server so answers use governed metrics "instead of guessing at raw tables" (paraphrase of page).

### S3. dbt Labs, "About dbt MCP server" docs. Last updated 2026-07-23. https://docs.getdbt.com/docs/dbt-ai/about-mcp [V]
- MCP server gives AI applications standardized access to dbt-managed models, metrics, lineage and freshness. Read-only with respect to data; does not retain production data. Remote (HTTP) and self-hosted forms. Tools cover Semantic Layer, Discovery (metadata), SQL, admin API. Text-to-SQL tool can be disabled with AI features off.
- Teaching point: the PM's harness should ask the semantic layer for "NRR, Q3, enterprise segment" rather than have the model write queries against raw tables.

### S4. Zhamak Dehghani, "Data Mesh Principles and Logical Architecture", martinfowler.com, 2020-12-03. https://martinfowler.com/articles/data-mesh-principles.html [V]
- Four principles: domain-oriented decentralized ownership; data as a product; self-serve data infrastructure as a platform; federated computational governance.
- Data as a product needs discoverability, security, explorability, understandability, trustworthiness; measurable goals (quality, lead time to consume, user satisfaction); a domain data product owner.
- Use: every source in the inventory gets an owner who treats it as a product; the PM is a consumer with requirements.

### S5. OpenTelemetry GenAI semantic conventions. https://opentelemetry.io/docs/specs/semconv/gen-ai/ and https://github.com/open-telemetry/semantic-conventions-genai (fetched 2026-10-30) [V]
- Conventions have moved to a dedicated GenAI repo. Cover spans, metrics, events for GenAI clients, agent spans, MCP, exceptions, plus provider-specific conventions (Anthropic, AWS Bedrock, Azure AI Inference, OpenAI). Maturity level not stated on the pages fetched; schema URL marked TODO. Do not claim "stable".
- Use: AI traces are a first-class product data source, with a shared vocabulary for model, tokens, tool calls.

### S6. FinOps Foundation, "FinOps for AI Overview". Last updated 2026-10-28. https://www.finops.org/wg/finops-for-ai-overview/ [V]
- Scope: cost and value of AI across model APIs, cloud AI services, SaaS, GPUs. Differences from cloud FinOps: tokens, volatile pricing, new stakeholders. Pair allocated AI cost with business outcomes.
- Named unit metrics: cost per inference; cost per million tokens; cost per successful outcome (run cost / runs meeting the quality bar); cost per API call; cache hit rate; model fit (share of requests sent to a more capable model than needed); anomaly cost percentage; ROI and time to value.
- Page says: State of Tokenomics survey (September 2026) found proving value or ROI most common challenge (43 percent); FOCUS v1.5 ratification scheduled December 2026 to add AI fields such as model identity and cache status. [V on FinOps page; survey itself not read: treat 43% as [S]]

### S7. Michael V. Marn and Robert L. Rosiello, "Managing Price, Gaining Profit", Harvard Business Review, Sept to Oct 1992. https://hbr.org/1992/09/managing-price-gaining-profit [V for authors/year only]
- HBR abstract page does not define pocket price waterfall; concept attribution to Marn and Rosiello is standard but treat definition as [S] until checked against McKinsey piece.

### S8. Jeff Bezos, 2016 Letter to Shareholders, Amazon (published April 2017). https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders [V]
- "Resist proxies": as companies grow they manage to proxies. Process becomes the thing (checking steps were followed rather than outcomes). Surveys and market research become proxies for customers; survey numbers are hard to interpret and can mislead. Builders should understand customers through anecdote and intuition, using research to find blind spots.
- Quote: "The process is not the thing."
- Use: every report is a proxy; the PM must keep the proxy tied to customer reality (pair metrics with anecdotes, e.g., sales call excerpts, ticket verbatims).

### S9. Fangyu Lei and others, "Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows", arXiv 2411.07763, v1 2024-11-12, v2 2025-03-17, ICLR 2025 Oral. https://arxiv.org/abs/2411.07763 [V]
- 632 enterprise text-to-SQL workflow tasks (BigQuery, Snowflake; databases often over 1,000 columns; multi-query, some over 100 lines).
- o1-preview code agent: 21.3% on Spider 2.0 versus 91.2% on Spider 1.0 and 73.0% on BIRD.
- Use: evidence for why an AI harness pointed at raw enterprise tables gives unreliable answers, and why governed definitions (semantic layer, metric dictionary) matter. Caveat: 2024 to 2025 models; leaderboard numbers have since risen; do not cite as current state of the art.

### S10. Bitol, Open Data Contract Standard (ODCS), latest docs (v3.1.0+ structure). https://bitol-io.github.io/open-data-contract-standard/latest/ (fetched 2026-10-30) [V]
- Platform-agnostic YAML standard for data contracts. Sections: fundamentals, schema, data quality, SLA, team and roles (ownership), support, pricing, infrastructure, authoritative definitions, tags.
- Use: the data source inventory row is a lightweight contract (owner, freshness SLA, quality checks, definitions). Linux Foundation affiliation not confirmed on page fetched: do not state.

### S11. Barr Moses, "What Is Data Observability?", Monte Carlo blog, updated 2026-10-28. https://montecarlo.ai/blog-what-is-data-observability [V]
- Data downtime: periods when data is partial, erroneous, missing or otherwise inaccurate.
- Five pillars: freshness, quality (null rates, unique rates, ranges), volume, schema, lineage.
- Use: the five pillars become a PM-level checklist ("before I trust this number") the harness can run per source. Vendor source: frame as Moses's framing.

### S12. Benn Stancil, "The missing piece of the modern data stack", benn.substack.com, 2021-04-22. https://benn.substack.com/p/metrics-layer [V]
- Data stack has ingestion, transformation and BI but no shared place to define metrics; formulas scatter across dashboards, spreadsheets and ad hoc queries, producing inconsistent answers. Proposes a metrics layer on the warehouse that any tool queries.
- Quote: "there's no central repository for defining a metric."

### S13. Snowflake, "Open Semantic Interchange" announcement blog, 2025-09-23. https://www.snowflake.com/en/blog/open-semantic-interchange-ai-standard/ [V]
- Open-source initiative for a vendor-neutral semantic model specification (YAML) and query API across analytics, AI and BI tools; intended as Apache project.
- Named participants include Snowflake, dbt Labs, Salesforce, ThoughtSpot, Sigma, Hex, Omni, Cube, Atlan, Alation, Select Star, Honeydew, RelationalAI, Mistral AI, BlackRock, Blue Yonder, Elementum AI.
- Problem framed: definitions shift as they move between AI agents and BI tools; no common semantic standard.
- Use: semantic layer as concept is becoming an industry standard in the AI era; PM does not need the tool, needs the idea.

### S14. Bain and Company, "Introducing the Net Promoter System" (Loyalty Insights). https://www.bain.com/insights/introducing-the-net-promoter-system-loyalty-insights/ [V]
- 0 to 10 likelihood-to-recommend; promoters 9 to 10, passives 7 to 8, detractors 0 to 6; NPS = % promoters minus % detractors; follow-up "why" and "what could we do better". Originator Fred Reichheld (Bain); 2003 HBR article origin is common knowledge but not confirmed on this page [S].

### S15. Pendo, "The 2019 Feature Adoption Report". https://www.pendo.io/resources/the-2019-feature-adoption-report/ [V on vendor page]
- Headline: 80 percent of features in the average software product are rarely or never used. Basis: anonymized usage data from 615 Pendo subscriptions (customers using Pendo over a year). Vendor data, 2019, method not peer reviewed: cite as Pendo's finding with year, not as universal law.

### S16. Anthropic, "Introducing the Model Context Protocol", 2024-11-25. https://www.anthropic.com/news/model-context-protocol [V]
- Open standard for two-way secure connections between AI tools and data sources. Launch servers: Google Drive, Slack, GitHub, Git, Postgres, Puppeteer.

### S17. Langfuse docs, "Observability overview" (undated, fetched 2026-10-30). https://langfuse.com/docs/observability/overview [V]
- A trace records each operation in a request: LLM calls, retrieval steps, tool executions, custom logic; nested observations; exact prompt and response; latency per step; token usage and cost; metadata; scores (including LLM-as-judge) to monitor quality.
- Use: what the "AI traces" row of the inventory contains and what it can answer.

### S18. Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, Jiri De Jonghe, "Demystifying evals for AI agents", Anthropic Engineering, 2026-01-09. https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents [V]
- Terms: task, trial, grader, transcript (trace/trajectory), outcome (final environment state, not what the agent says).
- pass@k (at least one success in k) versus pass^k (all k succeed; for consistency-critical agents).
- Capability evals start low; regression evals should sit near 100%.
- Quote: "You won't know if your graders are working well unless you read the transcripts"

### S19. Hamel Husain and Shreya Shankar, "LLM Evals: Everything You Need to Know" (evals FAQ), hamel.dev, page dated 2026-09-18 (modified 2026-09-21). https://hamel.dev/blog/posts/evals-faq/ [V]
- "Error analysis is the most important activity in evals." Review real traces, open notes, group into failure taxonomy; annotate at least 30 traces personally before asking an agent; continue until saturation.
- Prefer binary pass/fail over Likert; avoid generic off-the-shelf scores (helpfulness, coherence) as headline metrics.
- Authors report 60 to 80 percent of development time on error analysis and evaluation.

### S20. Gainsight, "Customer Health Score" guide. https://www.gainsight.com/guides/customer-health-score/ (fetched 2026-10-30) [V]
- Health scorecard inputs: product usage versus entitlements, feature adoption, sentiment, engagement (cadence calls, EBR follow-through), relationships (exec sponsor, advocacy), customer value (outcomes).
- Treat inputs as leading indicators; benchmark and monitor; if churn blindsides you for successive quarters, rework the scorecard (i.e., validate against actual renewals).

### S21. Gainsight, "The Essential Guide to Quarterly Business Reviews". https://www.gainsight.com/guides/the-essential-guide-to-quarterly-business-reviews/ (fetched 2026-10-30) [V]
- QBR: quarterly, demonstrate value, align goals; EBR: senior leadership, annual or biannual, longer view.
- Sections: executive summary; key KPIs that matter to the customer; ROI analysis tied to use cases; progress versus prior goals; benchmarking; health update with drivers; action items with owners and dates; schedule next QBR.
- Metrics: value against original buying reasons, adoption and time to value, ROI (hours saved, revenue, efficiency).
- Note: this is the customer-facing QBR. The chapter's "QBR pack" may also mean the internal quarterly product review for leadership; define both.

### S22. Anthropic, "Claude for Financial Services", 2025-07-15 (updated 2026-04-10). https://www.anthropic.com/news/claude-for-financial-services [V]
- Connectors announced include Snowflake and Databricks (warehouses) plus data providers (S&P Global, FactSet, PitchBook, Morningstar, Daloopa), Box, Palantir. Page states every claim links to its original source.
- Use (carefully): illustrates the 2025 to 2026 pattern of harness plus warehouse connectors plus cited answers. Not product-management specific.

### S23. Wikipedia, "Goodhart's law" (fetched 2026-10-30). https://en.wikipedia.org/wiki/Goodhart%27s_law [S]
- Charles Goodhart, 1975 paper on UK monetary policy: statistical regularities collapse once used for control. Marilyn Strathern, "'Improving ratings': audit in the British University system", European Review, 1997, generalized it: when a measure becomes a target it ceases to be a good measure (credited to Keith Hoskin, 1996). Campbell's law (Donald Campbell) is a related earlier idea.

### S24. SaaS Capital, "SaaS Retention Benchmarks for Private B2B Companies", 2025-09-18. https://www.saas-capital.com/research/saas-retention-benchmarks-for-private-b2b-companies/ [V]
- NRR definition used: December 2024 MRR from customers who were customers in December 2023, divided by December 2023 MRR; includes upsell, cross-sell, price increases. GRR same but excludes expansion; GRR cannot exceed 100%.
- Example: median NRR 102% for ACV $25,000 to $50,000. Median growth 24% for companies above $1M ARR.
- Use: definitional choices (MRR snapshot versus trailing 12 months, price increases in or out, cohort basis) change the number; the metric dictionary must pin them.

### S25. Juan Sequeda, Dean Allemang, Bryon Jacob, "A Benchmark to Understand the Role of Knowledge Graphs on Large Language Model's Accuracy for Question Answering on Enterprise SQL Databases", arXiv 2311.07509, 2023-11-13. https://arxiv.org/abs/2311.07509 [V]
- Insurance-domain enterprise schema, questions from reporting to metrics. GPT-4 zero-shot: 16% accuracy directly on SQL; 54% over a knowledge graph (ontology plus mappings) representation.
- Use: second piece of evidence that business context (semantic layer, ontology, definitions) sharply improves AI answers on enterprise data. Dated 2023 models; directional only. Authors work at data.world (vendor interest): note.

---

# ORGANIZED NOTES

Overlap check: ch05 covers instrumentation, tracking plans, funnels, HEART, experiments and AI feature analytics; ch09 covers NRR/GRR math, survival analysis, health score modelling, NPS validity and LLM text analytics. Ch18 should not re-teach those. Its job is the map (where data lives, who owns it, what it can and cannot say), the report set (questions, cadence, audience) and governance (definitions, single source of truth, semantic layer). Cross-reference by chapter number only.

## (a) Key concepts and frameworks

### A1. Data source inventory: "what each source can and cannot tell you" (author synthesis, informed by Dehghani S4, Moses S11, ODCS S10)
No single originator. Build it as a table with one row per source and these columns (adapted from ODCS sections and data-as-a-product properties): Source | System of record | Owner (named team) | Grain (event, account, opportunity, ticket, invoice, trace) | Freshness (refresh cadence) | Join key to account | Can tell you | Cannot tell you | Known traps | Access path for the harness (connector or MCP server, governed or raw).
Draft content for the ten sources:
1. Product telemetry and analytics. Can: behaviour, adoption, funnels, time to value by user and account. Cannot: why; intent; anything off-product (work done in other tools). Owner: product analytics or data engineering, PM owns the tracking plan. Traps: instrumentation gaps after releases; bot, test and internal tenants inflating counts; event renames; user versus account identity mismatch; sampling.
2. CRM (opportunities, accounts, contacts). Can: pipeline, win/loss, segment, deal stages, stated loss reasons. Cannot: true reasons for loss (rep-entered free text), product usage. Owner: sales ops / RevOps. Traps: stage inflation near quarter end; "primary product" field on multi-product deals; duplicate accounts; loss reasons picked from a dropdown in a hurry.
3. Billing and subscription. Can: ARR, MRR, expansion, contraction, churn, discounts, usage charges. Cannot: why customers expand or churn; product value. Owner: finance / billing ops. Traps: bookings versus billings versus revenue; multi-year prepay; credits and true-ups; parent/child account hierarchy differs from CRM.
4. Support tickets. Can: pain themes, defect trends, time to resolve, which accounts struggle. Cannot: prevalence across silent customers (selection bias: only those who complain); severity as felt by customer. Owner: support ops. Traps: category taxonomies drift; agents pick "other"; duplicate tickets per incident.
5. Surveys and NPS. Can: stated sentiment, relationship risk, verbatims. Cannot: behaviour; low response rates bias toward extremes; champion answers, buyer does not. Owner: CX or marketing. Traps: who was surveyed (user versus economic buyer); timing after incidents; score without the "why" (Bain S14 includes follow-up questions). Bezos S8: surveys are proxies.
6. Sales and customer calls (conversation recordings, transcripts). Can: competitor mentions, objections, language customers use, feature requests in context. Cannot: frequency in the base (sampled by what reps record); consent and retention rules apply. Owner: sales enablement / RevOps. Traps: recency and vividness bias; privacy.
7. Product reviews (public review sites, marketplace listings, community forums). Can: competitive perception, switching reasons, review-site comparisons. Cannot: representativeness (incentivized reviews, small samples). Owner: product marketing. Traps: vendor-solicited reviews; old reviews of old versions.
8. Market and competitive data (analyst reports, competitor pricing pages, job postings, release notes, win/loss). Can: direction and positioning. Cannot: precise share in a niche. Owner: product marketing / strategy. Traps: analyst sizing definitions differ; stale snapshots.
9. Finance and FP&A (plan, forecast, cost of goods sold, gross margin by product). Can: margin, plan versus actual, unit economics. Cannot: feature-level cost without allocation rules. Owner: FP&A. Traps: allocation methods; plan numbers versus actuals; fiscal versus calendar periods.
10. AI traces and evals (S5, S17, S18, S19). Can: what the model and agent actually did per request (prompt, retrieval, tool calls, latency, tokens, cost, scores), quality against a test set, failure modes. Cannot: whether the user got value unless joined to outcome data; eval sets drift from production. Owner: applied AI / platform engineering, PM co-owns eval criteria. Traps: personal data and customer content in traces (access control, retention); judge models scoring generically (S19); offline eval pass rates mistaken for production quality.
B2B application: the PM's leverage is the join key. Most enterprise questions need account-level joins across telemetry, CRM, billing and support; the inventory must state the account ID mapping and its known breaks.

### A2. Data as a product and domain ownership (Zhamak Dehghani, data mesh, 2019 to 2020; S4)
Four principles: domain ownership; data as a product; self-serve platform; federated computational governance. Data products need discoverability, understandability, trustworthiness and a named owner. PM application: treat each inventory row as a product with an owner and an SLA; the PM is a customer of those products and writes requirements for them (freshness, definitions, join keys). Do not teach mesh architecture.

### A3. Data downtime and the five pillars (Barr Moses, Monte Carlo; S11)
Data downtime: periods when data is partial, erroneous, missing or inaccurate. Pillars: freshness, quality, volume, schema, lineage. PM application: a five-question "trust check" before acting on any number. Prompt template for the harness: "Before answering, check: when was this table last refreshed; did row counts for the last 7 days fall outside the usual range; did any field definitions change in the last 30 days; what upstream sources feed it; are null or out-of-range rates abnormal. Report any failure before the answer."

### A4. Data contracts (Open Data Contract Standard, Bitol; S10)
A data contract records schema, quality expectations, SLA, ownership, support and authoritative definitions for a dataset. PM application: the PM does not write YAML, but requests a contract (or a contract-shaped row in the inventory) for any source a recurring report depends on.

### A5. Metrics layer and semantic layer (Benn Stancil 2021, S12; dbt Semantic Layer and MetricFlow, S2; Open Semantic Interchange 2025, S13)
Problem (Stancil): no central place to define a metric; definitions scatter across dashboards, spreadsheets and ad hoc queries. Concept: define each metric once (measure, filters, time grain, dimensions, owner), then every tool, including AI agents, asks the layer rather than raw tables. dbt: a change propagates everywhere. OSI: industry move to a vendor-neutral spec so definitions do not shift between agents and BI tools. PM application: the semantic layer is the "single source of truth" in practice; in 2026 it is also the safest interface for an AI harness (S3, S9, S25).

### A6. Metric dictionary (author synthesis grounded in S2, S12, S24)
Exact template proposed (one entry per metric):
- Name and ID
- Plain-language definition (one sentence a customer could read)
- Formula in words (numerator, denominator, filters, exclusions)
- Grain and time window (weekly, trailing 12 months, snapshot date)
- Segments allowed (tier, region, channel, cohort)
- Source of record and semantic-layer name
- Owner (accountable person) and steward (maintains logic)
- Type: input (controllable) or output (S1); North Star, health, guardrail
- Target and threshold for "exceptional variation"
- Known caveats and the decisions it informs
- Version and change log (date, what changed, why)
Example of why it matters: NRR depends on choices such as snapshot MRR versus trailing 12 months and whether price increases count (SaaS Capital definition S24 includes price increases). Two teams can report different NRR for the same quarter without either being wrong.

### A7. Amazon Weekly Business Review (Amazon practice; described by Colin Bryar and Bill Carr in "Working Backwards" (2021) and by Cedric Chin, Commoncog, S1)
Precise format per Chin: weekly, exception-driven; deck ordered causally, controllable input metrics, then outputs, then financials; static deck; owners say "nothing to see here" for normal variation and "I don't know" plus a logged follow-up when there is no root cause; 6-12 graphs (trailing 6 weeks, trailing 12 months, prior-year line, target markers, box score). B2B application: a product WBR of 15 to 30 metrics (author recommendation, not Amazon's number), each with an owner, ordered from Beacon inputs (connectors live, diagnosis acceptance) to outputs (incidents resolved with Beacon's help, NRR) to financials (ARR, gross margin). Low-volume B2B caveat: weekly enterprise metrics are noisy; use trailing 4-week views and account lists, not only percentages. Attribution: "Working Backwards" authorship is well known but not fetched in this session [S].

### A8. Resist proxies (Jeff Bezos, 2016 shareholder letter; S8) and Goodhart's law (Goodhart 1975; Strathern 1997; S23)
Every report is a proxy. Pair numbers with anecdotes; rotate scrutiny to inputs that may be gamed (for example, "diagnosis acceptance rate" can be gamed by auto-accept defaults).

### A9. The standard report set (author synthesis; components sourced)
Format for each report: purpose question(s) | cadence | audience | owner | primary sources | key metrics | decision it feeds.
1. Weekly metrics review (WBR). Q: what changed, is it exceptional, why, what are we doing. Weekly. Product leadership, eng leads, PMM, CS lead. Sources: semantic layer across telemetry, billing, support, AI traces. (S1)
2. Product health. Q: is the product working for customers (reliability, latency, error rates, incident-free days, defect backlog)? Weekly or daily. Product and engineering.
3. Funnel and activation. Q: where do new accounts stall between signed and first value; time to value by segment. Weekly view, monthly deep dive. PM, onboarding, CS. (ch05 for mechanics)
4. Retention and NRR. Q: which cohorts and segments expand, contract, churn; GRR versus NRR; leading signals. Monthly, quarterly. Product leadership, finance, CS. (ch09 for math; S24 for definitions)
5. Feature adoption. Q: which features are used, by whom, breadth versus depth, which to invest in or retire. Monthly; per launch at 30/60/90 days. PMs, design, PMM. (Pendo S15 as caution: much shipped software goes unused)
6. Customer health. Q: which accounts are at risk or ready to expand, and why. Weekly list, monthly trend. CS, account teams, PM. (Gainsight S20; validate against renewals)
7. Pipeline influence. Q: which product capabilities appear in won and lost deals, in which segments; where product gaps block deals. Monthly, quarterly. Product leadership, sales leadership. Caveat: influence is correlation through CRM tagging and call mentions, not causal attribution.
8. Pricing and discount. Q: what customers actually pay versus list (price waterfall concept, Marn and Rosiello 1992), discount depth by segment and rep, packaging uptake, usage-to-price fit. Monthly, quarterly. Product, pricing, finance, sales ops.
9. Support trends. Q: top themes by volume and by ARR affected, new themes, defect versus how-to, deflection. Weekly digest, monthly review. PM, support, engineering.
10. AI quality and cost. Q: is the AI getting better or worse (eval pass rates, regression suite near 100% per S18, production acceptance, hallucination reports), what does each outcome cost (FinOps unit metrics, S6: cost per successful outcome, cost per million tokens, cache hit rate, model fit). Weekly; release gate on every model or prompt change. PM, applied AI, finance.
11. QBR pack. Two meanings: (a) internal quarterly product review for executives (strategy progress, OKRs, output metrics, bets); (b) customer-facing QBR built per account (Gainsight S21 sections: exec summary, customer KPIs, ROI, progress, benchmarks, health, actions). Quarterly.
12. Portfolio review. Q: across product lines, where is investment versus return (ARR growth, margin, NRR, strategic fit, cost to serve); what to grow, sustain, harvest, sunset. Quarterly or semiannual. VP product, CFO, CEO staff.

### A10. Inputs versus outputs ordering (Amazon WBR, S1)
Report set as a causal chain: inputs (things teams control this week) feed outputs (customer and business results). Each report should label which metrics are inputs.

### A11. AI-first data work (author synthesis grounded in S2, S3, S9, S16, S22, S25)
Pattern: PM states a question, the harness queries governed sources through connectors/MCP, returns an answer with source, definition and freshness, and flags trust-check failures. Rules to teach: ask the semantic layer, not raw tables; require the harness to cite metric name and definition version; ask for the denominator; ask "what would change this conclusion"; spot-check one account by hand. Prompt shapes (no code): "Using the governed metric 'net revenue retention (v3)', show NRR by tier for the last four quarters, state the definition used, the data freshness, and any accounts excluded."

## (b) Verified facts

- [V] Amazon's company WBR runs Wednesdays, 60 minutes (90 in holiday season), Finance-facilitated; deck has 400 to 500 metrics (Chin's account; Amazon has not published this). Commoncog, 2024-07-02, updated 2026-06-14. https://commoncog.com/the-amazon-weekly-business-review/ (Tag [S] for the Amazon specifics; [V] that Chin reports them.)
- [V] dbt Semantic Layer: define metrics once in the modeling layer so changes refresh everywhere; AI tools connect via dbt MCP server to use governed metrics. dbt docs, updated 2026-09-29. https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl
- [V] dbt MCP server is read-only with respect to data and exposes Semantic Layer, Discovery and SQL tools. dbt docs, updated 2026-07-23. https://docs.getdbt.com/docs/dbt-ai/about-mcp
- [V] Open Semantic Interchange announced 2025-09-23 by Snowflake with partners including dbt Labs, Salesforce, ThoughtSpot, Sigma, Hex, Mistral AI. https://www.snowflake.com/en/blog/open-semantic-interchange-ai-standard/
- [V] Spider 2.0 (ICLR 2025): o1-preview agent solved 21.3% of 632 enterprise text-to-SQL tasks versus 91.2% on Spider 1.0 and 73.0% on BIRD. https://arxiv.org/abs/2411.07763 (v2 2025-03-17)
- [V] Sequeda, Allemang, Jacob (2023): GPT-4 zero-shot accuracy 16% on enterprise SQL questions versus 54% with a knowledge graph layer. https://arxiv.org/abs/2311.07509
- [V] Pendo 2019: 80 percent of features in the average product rarely or never used, from 615 subscriptions. https://www.pendo.io/resources/the-2019-feature-adoption-report/
- [V] MCP introduced by Anthropic on 2024-11-25 as an open standard connecting AI tools to data sources. https://www.anthropic.com/news/model-context-protocol
- [V] FinOps Foundation defines AI unit metrics including cost per successful outcome and model fit; page updated 2026-10-28; FOCUS v1.5 ratification scheduled December 2026 to add AI fields. https://www.finops.org/wg/finops-for-ai-overview/
- [S] FinOps State of Tokenomics survey (September 2026): proving value or ROI the top challenge at 43 percent (reported on FinOps overview page; survey not read).
- [V] NPS: promoters 9 to 10, passives 7 to 8, detractors 0 to 6; score = % promoters minus % detractors. Bain. https://www.bain.com/insights/introducing-the-net-promoter-system-loyalty-insights/
- [V] SaaS Capital NRR definition includes price increases; median NRR 102% for ACV $25k to $50k; published 2025-09-18. https://www.saas-capital.com/research/saas-retention-benchmarks-for-private-b2b-companies/
- [V] Data mesh four principles, Dehghani, 2020-12-03. https://martinfowler.com/articles/data-mesh-principles.html
- [V] Data downtime definition and five pillars, Barr Moses, Monte Carlo. https://montecarlo.ai/blog-what-is-data-observability
- [V] Anthropic agent evals: regression evals should sit near 100%; pass^k for consistency. 2026-01-09. https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- [V] Husain and Shankar report spending 60 to 80 percent of development time on error analysis and evaluation; recommend at least 30 traces reviewed personally first. https://hamel.dev/blog/posts/evals-faq/
- [V] OpenTelemetry GenAI conventions cover agent spans, MCP and provider-specific conventions including Anthropic and OpenAI; maturity not stated. https://github.com/open-telemetry/semantic-conventions-genai
- [V] Bezos 2016 letter: "Resist proxies"; process and surveys as proxies. https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders
- [V] Anthropic Claude for Financial Services (2025-07-15) launched with Snowflake and Databricks connectors and source-linked claims. https://www.anthropic.com/news/claude-for-financial-services

## (c) Quotes (under 15 words)
1. "The process is not the thing." Jeff Bezos, 2016 Letter to Shareholders.
2. "there's no central repository for defining a metric." Benn Stancil, 2021.
3. "Error analysis is the most important activity in evals." Hamel Husain and Shreya Shankar.
4. "You won't know if your graders are working well unless you read the transcripts" Anthropic, 2026 (13 words).
5. "When a measure becomes a target, it ceases to be a good measure." Marilyn Strathern, 1997 (12 words) [S, via Wikipedia; primary not read].

## (d) 2025 to 2026 AI-era developments (verified)
- Semantic layers exposed to AI through MCP: dbt MCP server (docs updated 2026-07-23) lets Claude and others query governed metrics, lineage and freshness, read-only. [V]
- Open Semantic Interchange (2025-09-23): cross-vendor effort to standardize semantic model definitions for AI agents and BI. [V]
- Enterprise text-to-SQL remains hard on raw schemas (Spider 2.0, ICLR 2025: 21.3% for the best agent tested). Use as historical evidence for governed interfaces, not a current ceiling. [V]
- AI traces get a standard vocabulary: OpenTelemetry GenAI conventions moved to a dedicated repo covering agent spans and MCP, with Anthropic and OpenAI provider conventions. Maturity unstated. [V]
- FinOps for AI matures: named unit metrics (cost per successful outcome, model fit, cache hit rate) and FOCUS v1.5 slated for December 2026 with AI fields. [V]
- Agent evals practice: Anthropic (Jan 2026) task, trial, grader, transcript, outcome; capability versus regression evals; Husain and Shankar FAQ (Sept 2026) on error analysis and binary judgments. [V]
- Harness plus warehouse connectors with source-cited answers (Claude for Financial Services, July 2025, with Snowflake and Databricks). [V]
Implication for the chapter: the PM's 2026 data job is less "pull the number" and more "own the definitions, the inventory and the questions," and check the harness's provenance.

## (e) Beacon worked example ideas (consistent with beacon-case.md)
1. Beacon data source inventory: telemetry (alerts ingested, incidents correlated, diagnoses proposed and accepted, actions run, approvals); Northlight CRM (420 enterprise accounts plus MSP partner accounts; Leo's 60 customers appear as child accounts, a known join trap); billing (platform fee per environment plus usage, moving to per-resolved-incident, so "resolved incident" becomes a billing event and must have one definition shared by product and finance); support tickets (Northlight Desk, ironically Northlight's own product); NPS split by persona (Priya and Dana versus Marcus); sales call transcripts (competitor AIOps mentions); review sites; FP&A (gross margin 81% to 72% after agentic launch); AI traces and evals (diagnosis evidence chains, tool calls, tokens, cost per diagnosis).
2. Metric dictionary entries for Beacon: North Star "incidents resolved with Beacon's help per week" (what counts as "help": diagnosis accepted, or action executed, or both; dedupe incidents correlated across tools; exclude test tenants); "diagnosis acceptance rate" (denominator: diagnoses shown to a responder, not generated); "autonomous resolution rate"; MTTR (customer-reported versus Beacon-measured; median not mean); NRR 118% (state definition: trailing 12 months, includes price changes or not). Show the per-resolved-incident pricing change forcing the product metric and the billing unit to share one definition, with finance as co-owner and a change log.
3. A definitional conflict story: Marketing's Northlight Live slide says "Beacon resolved 1.2 million incidents" (fictional) while product's WBR says a much smaller number because marketing counted correlated incidents and product counted resolved-with-help. Resolution: metric dictionary, semantic layer entry, single owner. Keep numbers clearly fictional.
4. Beacon WBR deck (author design): inputs (new connectors live, accounts with Diagnose enabled, eval regression suite pass rate, median diagnosis latency), outputs (North Star, diagnosis acceptance, autonomous resolution rate, weekly active responders, MTTR for customers in a reference cohort), financials (ARR, gross margin, inference cost per resolved incident). Owners named by role. "Nothing to see here" for most lines; one exception: acceptance rate dropped for EU accounts after a retrieval change.
5. AI quality and cost report tied to the hallucinated root cause storyline: the trace showed the agent cited logs from the wrong service; the eval set gains a regression case; report tracks regression suite pass rate (target near 100%), production acceptance, rollback-after-action events, and cost per successful diagnosis (FinOps "cost per successful outcome") to explain the margin drop.
6. QBR pack for Marcus (customer): MTTR trend, escalations avoided, incidents resolved with Beacon's help, approval-gate stats for Sam (audit), ROI story for the CFO; internal QBR for the VP of Product: Beacon versus Observe and Desk in the portfolio review (ARR growth 38%, margin 72%, NRR 118%).
7. Pipeline influence: CRM tags plus call transcripts show "tool-agnostic connectors" mentioned in lost deals where prospects do not use Northlight Observe, feeding the build-on-Observe versus tool-agnostic tension.
8. Harness prompt examples (no code): "Using governed metrics only, list the 20 accounts with the largest drop in diagnosis acceptance over 4 weeks, with ARR, health score, open P1 tickets and last NPS response. Cite definitions and data freshness. Flag any account where telemetry and billing disagree on environments."

## (f) Editorial flags
- Amazon WBR specifics (400 to 500 metrics, Wednesday timing, 6-12 graph) come from Cedric Chin's secondary account and from "Working Backwards" (Bryar and Carr, 2021), which was not fetched this session. Attribute to Chin or to Bryar and Carr; do not state as Amazon policy.
- Gartner's widely quoted "poor data quality costs organizations $12.9 million a year" could not be verified (Gartner page returned 403). Do not use.
- Pendo 80 percent figure is vendor data from 2019; present as Pendo's finding.
- Spider 2.0 and Sequeda et al. accuracy numbers reflect 2023 to 2025 models and specific setups; later models score higher. Use as directional evidence only; Sequeda et al. are from a knowledge graph vendor.
- OpenTelemetry GenAI conventions: maturity (development versus stable) not confirmed; avoid "standard is stable".
- FinOps 43 percent survey statistic is reported on the overview page; the survey itself was not read: tag [S] if used.
- Strathern quote verified only via Wikipedia [S]. Reichheld 2003 HBR origin of NPS not confirmed on Bain page fetched [S].
- Marn and Rosiello price waterfall definition not confirmed on the HBR abstract page; McKinsey page timed out. Describe the concept in paraphrase and attribute to Marn and Rosiello (HBR 1992) [S].
- Pipeline influence is contested: multi-touch attribution and "influenced pipeline" are correlational and easy to inflate. No source fetched; present as author guidance with an explicit caveat.
- ODCS: Linux Foundation affiliation not confirmed; do not state.
- The report set, metric dictionary template and inventory columns are author synthesis; label them as the book's framework, not an industry standard.
- Web search budget ran out after the first query; sources were fetched from known URLs. Areas thin on sources: sales call data, product review data, portfolio review frameworks.
