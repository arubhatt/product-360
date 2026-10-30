# Research notes: Chapter 31, "Building AI-Powered Products"

The Product 360 Handbook (2026 edition). Notes compiled 2026-10-30. Audience: Senior to Principal PMs, B2B enterprise and platform.

How to read these notes:

- **[V]** means I checked the claim against a primary source (the vendor, author, regulator or official document) during this session.
- **[S]** means I found it in secondary sources only (law-firm notes, trade press, vendor blogs). It is probably right, but cite carefully.
- **[U]** means unverified, contested or from my prior knowledge without a fresh check. Confirm before print.

Section 7 (regulation) is the most time-sensitive. The EU AI Act high-risk dates changed in 2026, and several 2025 to mid-2026 sources (including some ISO 42001 vendor pages) still give the old August 2026 date.

---

## 1. Evals

### 1.1 Hamel Husain and Shreya Shankar: error analysis first

**Source.** "AI Evals: Everything You Need to Know" (the evals FAQ), hamel.dev, published 2026-09-18, modified 2026-09-21 [V]. It grew out of their Maven course; reported student counts range from about 1,500 to over 3,000 [S].

**Core positions** [V, from the FAQ]:

- **Error analysis is the foundation.** The FAQ calls it "the most important activity in evals." Method: read real traces, write free-form notes on what went wrong (open coding), cluster the notes into a failure taxonomy (axial coding), and stop when new traces stop surfacing new failure types (theoretical saturation). Start with about 30 hand-annotated traces.
- **Look at the data before you write rubrics.** Criteria written up front narrow what reviewers notice, and criteria change as you read examples ("criteria drift").
- **Binary pass/fail over 1 to 5 scales.** Likert scales produce inconsistent labels and drift toward the middle. If you need finer progress tracking, measure sub-components separately.
- **One narrow LLM judge per failure mode.** Validate each judge against human labels using train/dev/test splits, and report true positive rate and true negative rate separately rather than raw "agreement". The FAQ suggests roughly 100 to 200 labeled examples per failure mode.
- **Automate only what pays off.** Use code assertions where a rule can catch the failure. Reserve LLM judges for persistent, subjective failures. The FAQ reports that teams often spend 60 to 80% of development time on error analysis and evaluation.
- **Distrust generic metrics** ("helpfulness", ROUGE, BERTScore), and write evaluators for failures you have observed rather than imagined, except for explicit constraints such as "never mention competitors".
- **One accountable domain expert ("benevolent dictator")** owns the quality call. Do not outsource core error analysis.

**Lenny's Podcast episode.** "Why AI evals are the hottest new skill for product builders," with Husain and Shankar, 2025-09-25 [V]. The free show notes frame well-written eval prompts as living product requirements (section heading: "evals are the new PRDs") and put the running cost at about 30 minutes a week once set up [V, show notes; transcript paywalled].

**How a PM applies it.** The PM (or the PM's chosen domain expert) runs the first error-analysis pass personally and owns the failure taxonomy. The taxonomy becomes the backlog: each recurring failure mode gets a fix, and if it persists, a dedicated judge. In a PRD, "quality" is written as a named list of failure modes with target pass rates, not as an adjective.

### 1.2 "Evals are the new PRD": the argument and the pushback

- **Origin is contested [U].** One summary credits Brendan Foody (Mercor) on X. Lenny's 2025 episode uses it as a section title. Braintrust published "Evals are the new PRD" (Ameya Bhatawdekar, 2026-03-27) [V]. Secondary coverage reports that Anthropic's Dianne Penn called evals "the new PRDs" on Lenny's Podcast; I could not reach a transcript, so treat this as [U].
- **Braintrust's argument [V].** Static specs assume deterministic behavior. Evals define target behavior, acceptance criteria and regression thresholds, and can gate CI/CD. The PM sets the bar; engineering iterates until the system clears it; production failures become new eval cases.
- **The Kevin Weil "most important PM skill" line [U].** Braintrust attributes it to Weil; other reporting credits the OpenAI and Anthropic CPOs jointly on a 2025 panel. Do not print it as a verbatim Weil quote without the transcript.
- **Pushback, Mind the Product [V].** Lisa Murkin (2026-07-16): golden datasets overfit, 30 examples are directional rather than proof, datasets drift from real usage while looking healthy, and product-only ownership recreates the old PRD's problems. The PRD survives in shorter form for why and for whom; the dataset covers what.

**Textbook framing (my suggestion).** Evals do not replace the PRD. They become the PRD's acceptance criteria in executable form, and the narrative PRD still carries strategy, customer, economics and risk.

### 1.3 Chip Huyen, *AI Engineering* (O'Reilly, January 2025)

[V for structure, from the author's GitHub ToC.] Evaluation spans Ch. 3 "Evaluation Methodology" (language-model metrics, exact evaluation, "AI as a judge" and its limitations, comparative ranking) and Ch. 4 "Evaluate AI Systems" (criteria including **cost and latency**, model selection and build vs buy, reading public benchmarks, designing an evaluation pipeline). Ch. 9 covers inference optimization; Ch. 10 covers architecture and user feedback.

**PM use.** Ch. 4 puts cost and latency next to quality as evaluation criteria and warns against picking models from public leaderboards. Ch. 10 treats user feedback as a design problem, which links to Section 6.

### 1.4 Eugene Yan

"Product Evals in Three Simple Steps" (eugeneyan.com, November 2025) [S]: label a small dataset, align LLM evaluators to those labels, run the harness on every change. He favors binary labels and suggests about 50 to 100 failure cases. Earlier work: a survey of LLM-as-judge effectiveness (August 2024) and the AlignEval tool (October 2024) [S]. Affiliation [U]: a 2026 conference page lists him at Anthropic, older pages at Amazon.

### 1.5 Anthropic and OpenAI guidance

**Anthropic, "Demystifying evals for AI agents"** (Engineering blog, 2026-01-09) [V]:

- **Vocabulary:** *task* (one test with inputs and success criteria), *trial* (one attempt), *grader*, *transcript* (the full record, including tool calls), *outcome* (the final state of the environment; for a booking agent, whether the reservation exists, not whether the agent said it booked one).
- **Three grader types:** code-based (cheap, objective, brittle), model-based (flexible, needs calibration), human (gold standard, used mainly to calibrate the others).
- **Capability vs regression evals.** Capability evals should start at a low pass rate (a hill to climb). Regression evals should pass at nearly 100%. Saturated capability evals graduate into the regression suite.
- **pass@k vs pass^k.** pass@k is the probability of at least one success in k tries. pass^k is the probability that all k succeed, which is the right metric for customer-facing consistency. Worked example: 75% per-trial success gives about 42% for three in a row.
- **Start with 20 to 50 tasks** drawn from real failures and user-reported bugs. Balance "should do" and "should not do" cases.
- **Grade outcomes, not paths.** Exact tool-call sequences are brittle, and agents find valid routes designers did not anticipate.
- **PM role:** evals force a team to define success and expose ambiguous requirements early. PMs and customer-facing staff can contribute tasks directly.

**OpenAI, "Evaluation best practices"** (developers.openai.com) [V]: eval-driven development (evaluate early and often, log everything, mine logs for cases); five steps (objective, dataset, metrics, run and compare, continuous evaluation); judge tips (prefer pairwise or pass/fail, control for position and verbosity bias); architecture-specific evals, including tool selection, argument precision and multi-agent handoff accuracy. Anti-patterns: "vibe-based" evaluation and datasets unlike production traffic.

**Time-sensitive [V].** OpenAI's hosted **Evals platform** goes read-only on 2026-10-31 and shuts down on 2026-11-30. The guidance stays; the product does not. Useful sidebar on vendor dependence in eval tooling.

**Also useful for PMs:** Aman Khan (Arize), "Beyond vibe checks: A PM's complete guide to evals," Lenny's Newsletter, 2025 [S, contents not re-read].

---

## 2. Agents

### 2.1 Anthropic, "Building effective agents"

Erik Schluntz and Barry Zhang, Anthropic, 2024-12-19 [V]. The page now carries a note that much of the tooling has changed and points readers to newer Managed Agents guidance; the conceptual framework is still the most cited.

- **Workflows vs agents.** Workflows orchestrate LLMs and tools through predefined code paths. Agents let the LLM direct its own process and tool use. Both are "agentic systems."
- **Patterns, simple to complex:** augmented LLM (retrieval, tools, memory); prompt chaining; routing; parallelization (sectioning, voting); orchestrator-workers; evaluator-optimizer; autonomous agents (tool use in a loop with checkpoints and stopping conditions).
- **Principles:** start with the simplest solution; agentic systems trade latency and cost for task performance; reserve agents for open-ended problems whose steps cannot be predicted, and test them in sandboxes.
- **Agent-computer interface (ACI):** design tools as carefully as human UI, write tool descriptions like docstrings for a junior developer, and "poka-yoke" the arguments (requiring absolute file paths removed a class of SWE-bench errors).

**PM application.** Ask whether the job needs an agent at all. Many B2B features work better as workflows, which are cheaper, faster and easier to evaluate and audit. Record the choice in the PRD as a decision with rationale.

### 2.2 OpenAI, "A practical guide to building agents" (April 2025)

[S, from summaries.] Layered guardrails (relevance and safety classifiers, PII filters, moderation, tool risk ratings checked before execution). Human intervention when failure thresholds are exceeded and for high-risk or irreversible actions, especially early in deployment.

### 2.3 Autonomy levels: a specification vocabulary

Kevin Feng, David McDonald and Amy Zhang, "Levels of Autonomy for AI Agents," Knight First Amendment Institute / arXiv 2506.12469, 2025 [V for the levels]. The levels are defined by the **user's role**:

| Level | User role | What the agent does |
|---|---|---|
| L1 | Operator | User directs and decides; agent acts |
| L2 | Collaborator | Plan, delegate and execute together |
| L3 | Consultant | Agent leads; consults user for expertise or preferences |
| L4 | Approver | Agent engages user only in risky or pre-specified situations |
| L5 | Observer | Full autonomy; user monitors |

Key idea: autonomy is a **design choice separate from capability**. The authors also propose "autonomy certificates" that would cap an agent's permitted level. That proposal is speculative governance, so present it as such.

### 2.4 What PMs must specify for an agentic product (synthesis)

This checklist is my synthesis of the sources above (Anthropic, OpenAI, Feng et al., a16z), not a published standard:

1. **Autonomy level per action class**, not one level per product (for example, L4 for reading and drafting, L2 for anything that writes to a system of record).
2. **Reversibility map.** Which actions are irreversible or costly, and which therefore need approval, two-step confirmation or dry-run mode.
3. **Tool and permission scope.** Least-privilege credentials, separate environments, and no production write access by default. See the Replit incident in Section 6.
4. **Stopping conditions and budgets**: maximum steps, tokens, time and spend per task, and the escalation path when a limit is hit.
5. **Escalation and handoff UX**: what the human sees, with what context, and the target time to respond.
6. **Outcome-based success criteria and graders**, plus pass^k targets for consistency (Section 1.5).
7. **Observability and audit**: traces retained, who can see them, and retention aligned with customer contracts.
8. **Security threats**: prompt injection through tool outputs and retrieved content, data exfiltration, credential handling (a16z lists these as ongoing governance concerns).

### 2.5 Model Context Protocol (MCP): status in late 2026

- **Governance [V].** Anthropic donated MCP to the **Agentic AI Foundation (AAIF)**, a directed fund under the **Linux Foundation**, on **2025-12-09**. The co-founders are Anthropic, Block and OpenAI, with support from Google, Microsoft, AWS, Cloudflare and Bloomberg. The founding projects are MCP, Block's goose and OpenAI's AGENTS.md. Anthropic said MCP's governance model would stay the same.
- **Adoption at donation [V, Anthropic's figures]:** more than 10,000 active public MCP servers and over 97 million monthly SDK downloads (Python and TypeScript), with adoption in ChatGPT, Cursor, Gemini, Microsoft Copilot and VS Code.
- **Spec version [V].** The current revision is **2026-07-28** (modelcontextprotocol.io). It replaces the handshake-based versioning of 2025-11-25 and earlier with per-request version negotiation and a `server/discover` RPC, and adds a deprecation policy (at least 12 months' notice). Trade press calls it the largest revision since launch, and reports a late-August 2026 roadmap prioritizing agent messaging and enterprise readiness (audit, SSO auth, gateways) [S].

**PM relevance.** For a B2B platform, an MCP server is now a distribution surface, comparable to a public API, through which customers' agents reach your product. Treat it as a product: scope, auth model, rate limits, pricing and versioning.

### 2.6 Agent-to-agent protocols (A2A)

- [V] Created by Google (April 2025), hosted by the **Linux Foundation since June 2025**. The LF release of **2026-04-09** reports more than 150 supporting organizations (AWS, Cisco, Google, IBM, Microsoft, Salesforce, SAP, ServiceNow among them), a stable **v1.0** spec with Signed Agent Cards for identity, SDKs in five languages, and integration into Azure AI Foundry, Copilot Studio and Amazon Bedrock AgentCore.
- **Positioning [V]:** complementary to MCP. MCP connects an agent to tools and data; A2A connects agents to each other across organizations.
- **Contested [S]:** IBM's ACP also had LF backing, and 2026 commentary still calls the landscape fluid. Do not tell readers A2A "won".

### 2.7 Computer use

[V] a16z, "Can Agents Use a Computer Yet? We've Got the Data" (Serafini, Amble, Zhou, 2026-08-10): the best OSWorld-Verified score rose from 42% to 85% in a year (human average about 72%), but 85% per task still compounds into failure across multi-step processes. Estimated cost is about $6 to $8 per hour for an agent, against about $10 for offshore BPO and $30 to $45 for a US back-office worker, though agents can be slower. What works: run the workflow once, cache it as deterministic code, and call the model only when something breaks. Best fit: high-volume, stable, machine-verifiable workflows on legacy interfaces without APIs. Individual vendor leaderboard claims are [S] and move monthly; cite the a16z synthesis with its date.

---

## 3. AI PRDs and specs

### 3.1 Published templates

- **Miqdad Jaffer and Paweł Huryn, "A Proven AI PRD Template,"** The Product Compass, 2025-03-26 [V]. Jaffer is described as a product lead at OpenAI, formerly at Shopify (titles vary by source [U]). Nine sections, strategy-heavy at the front (market, strategic alignment, competitive advantage), with an **AI-specific non-functional section**: architecture choices, accuracy standards, hallucination limits, RAG grounding, bias audits, drift monitoring, guardrails. Framed as a living document; case study is Shopify Auto Write. **Gap:** almost nothing on inference cost or unit economics.
- **Product School AI PRD template** [V for headings; undated, © 2026]: business objectives and KPIs; user journeys; **model, data and prompt requirements**; risk mitigation and legal compliance; go-to-market.
- **Aakash Gupta (Product Growth)** publishes AI PM curricula and podcast episodes, including "Evals are the new PRD" with Braintrust CEO Ankur Goyal [S]. I did not find a single canonical Aakash Gupta AI PRD template to cite [U]; check his newsletter before attributing one.

### 3.2 What differs from a classic PRD (synthesis across sources)

| Classic PRD | AI PRD adds or changes |
|---|---|
| Functional requirements are deterministic | Behavior is specified as **eval sets with pass-rate targets** per failure mode, plus pass^k for consistency |
| Acceptance by QA test cases | Acceptance by **validated graders** (code, LLM judge with known TPR/TNR, human) and regression thresholds in CI |
| Edge cases listed | **Failure taxonomy** from error analysis; adversarial and "should refuse" cases |
| Non-functional: performance, security | Adds **latency budgets (time to first token, end-to-end), cost per task, model and fallback policy, drift monitoring** |
| Data model | **Data requirements**: grounding sources, permissions, PII handling, retention, feedback capture |
| UX flows | **Trust and failure UX**: confidence display, citations, correction, undo, escalation (Section 5) |
| Launch plan | **Staged autonomy** and human-in-the-loop ramp; shadow mode; kill switch |
| Pricing as a GTM item | **Unit economics as a requirement** (gross-margin floor per feature) |
| Compliance review at the end | **Regulatory classification up front** (EU AI Act risk tier, transparency duties, ISO 42001 controls) |

---

## 4. Cost, latency, model selection and pricing

### 4.1 Inference cost trends

- **Epoch AI** (Cottier, Snodin, Owen, Adamczewski, "LLM inference price trends," 2025-03-12) [V]: the price to reach a fixed performance level fell between **9x and 900x per year**, depending on benchmark and threshold. GPT-4-level performance on GPQA Diamond got about 40x cheaper per year. GPT-4-level MMLU fell from $37.50 per million tokens (GPT-4, March 2023) to $0.18 (Gemini 2.0 Flash, February 2025). Caveat from Epoch: the fastest declines came in the most recent year, and it is unclear whether they will persist.
- **a16z, "LLMflation"** (Guido Appenzeller, 2024-11-12) [S]: roughly **10x per year** decline at constant capability. MIT FutureTech (Gundlach et al., 2025) estimates 5 to 10x a year for frontier models [S].
- **The contrarian point** (DSHR blog, August 2025) [S]: the steep cuts apply mostly to older, weaker models. Reasoning tokens and agentic loops raise **tokens per task**, so cost per task can rise while price per token falls. Budget per task, not per token.

### 4.2 Levers PMs control

- **Model routing:** easy requests to small models, hard ones to frontier models.
- **Prompt caching [V, Anthropic docs]:** cache writes cost 1.25x base input (5-minute) or 2x (1-hour); cache reads cost 0.1x by default and 0.05x or 0.025x on the newest models. Long, stable system prompts become far cheaper on repeat calls. Multipliers change often; date any figure you print.
- **Workflow caching for agents:** convert a successful run into deterministic code (Section 2.7).
- **Latency:** stream output, keep time to first token low, use small models on interactive paths, run long agent tasks asynchronously.

### 4.3 Gross-margin impact

- **ICONIQ State of AI** [S]: the July 2026 edition (about 305 executives) reports average AI-product gross margin of 45% in 2025, projected 53% in 2026 and 59% in 2027 (the January 2026 snapshot said 52% for 2026). Classic SaaS benchmarks are 75 to 80%+.
- **Growth Unhinged 2026** [V]: median target AI gross margin about 50%; only 12% target 80% or more.

### 4.4 Pricing models

- **Kyle Poyar, "The State of B2B Monetization in 2026,"** Growth Unhinged [V, free portion]: April to May 2026, more than 230 B2B software and AI companies. **Hybrid pricing at 37%** (25% a year earlier) is the most common model; companies above $150M ARR still lean on seats (29%). **29% use AI credits** and 33% plan to add them within 12 months. Investor preference: hybrid 35%, outcome 26%, usage 24%, seat 5%. The 2025 edition found only 5% with outcome-based pricing as their primary model [S].
- **Intercom Fin** [S for pricing]: **$0.99 per outcome** (resolution, procedure handoff or disqualification), with a 50-outcome monthly minimum outside Intercom's helpdesk. **Corporate change:** Intercom renamed itself **Fin** in May 2026 [S], and **Salesforce signed a definitive agreement on 2026-06-15 to acquire Fin for about $3.6 billion** [V, Salesforce investor release], closing expected in Salesforce's fiscal Q4 2027 subject to regulators. One aggregator says it closed 2026-09-10 [U]; describe it as pending unless rechecked.
- **Salesforce Agentforce:** $2 per conversation at launch (autumn 2024) [S]; **Flex Credits from 2025-05-15**, $500 per 100,000 credits, 20 credits ($0.10) per action [V, Salesforce press release]; per-user add-ons from summer 2025 [V for the announcement]. September and October 2026 secondary checks report unchanged Flex Credit rates [S]. The arc runs per-conversation, then per-action, then per-user options alongside.
- **Cautionary tale, Cursor (July 2025)** [S, plus Cursor's blog of 2025-07-04]: Pro moved from request limits to $20 of included usage. Unclear "unlimited" messaging produced surprise charges, an apology and refunds. Usage-linked pricing needs metering visibility and spend caps before launch.

**PM framing.** Seat pricing breaks when AI does the work seats represented. Usage pricing passes model-cost volatility to the customer and creates bill anxiety. Outcome pricing aligns price with value but needs a measurable, attributable outcome and moves performance risk to the vendor. Most B2B companies land on hybrid: platform fee plus credits or outcomes.

---

## 5. Trust, UX and human-AI interaction

### 5.1 Microsoft HAX: Guidelines for Human-AI Interaction

Amershi et al., CHI 2019 (Honorable Mention) [V for the 18-guideline count, the four phases and the validation with 49 practitioners across 20 products]. Microsoft says the guidelines synthesize more than 20 years of human-AI interaction research; they are part of the HAX Toolkit (design library, workbook, playbook). **The guideline list below is from my prior knowledge of the paper [U]; check the wording against the paper or HAX poster before printing.**

- **Initially:** G1 Make clear what the system can do. G2 Make clear how well the system can do what it can do.
- **During interaction:** G3 Time services based on context. G4 Show contextually relevant information. G5 Match relevant social norms. G6 Mitigate social biases.
- **When wrong:** G7 Support efficient invocation. G8 Support efficient dismissal. G9 Support efficient correction. G10 Scope services when in doubt. G11 Make clear why the system did what it did.
- **Over time:** G12 Remember recent interactions. G13 Learn from user behavior. G14 Update and adapt cautiously. G15 Encourage granular feedback. G16 Convey the consequences of user actions. G17 Provide global controls. G18 Notify users about changes.

**PM use.** Use the 18 guidelines as a launch-review checklist. My reading (not a published finding): the Air Canada and Cursor cases in Section 6 read as failures of G2 (how well) and G10 (scope when in doubt), which makes them good worked examples.

### 5.2 Google PAIR People + AI Guidebook

[V for history; chapter names from prior knowledge, U.] Published 2019-05-08, updated 2021-05-18; a second edition added patterns and case studies, and PAIR says it is revising for generative AI. Six chapters, each with a worksheet: **User Needs + Defining Success; Data Collection + Evaluation; Mental Models; Explainability + Trust; Feedback + Control; Errors + Graceful Failure.** Central ideas: decide whether AI adds value at all; weigh precision against recall by the cost of each error type; **calibrate trust** so users trust the system as much as its reliability warrants; treat error states and fallbacks as part of the core flow.

### 5.3 Calibrated trust and failure UX: PM patterns (synthesis)

- **Show sources and confidence** where the user must act on the output.
- **Make correction cheap** (inline edit, regenerate, undo) and capture corrections as labels.
- **Disclose AI agents** in support channels (see Cursor, Section 6).
- **Degrade gracefully** to search, templates or a human when confidence is low or the provider is down.
- **Watch for over-trust.** In B2B, reviewers rubber-stamping agent output is the hidden failure mode of "human in the loop." Design review screens that make wrong output easy to spot.

---

## 6. Data flywheels, moats and failure modes

### 6.1 Moats in 2026

[S; mostly practitioner and VC opinion, no rigorous data.] The emerging consensus:

- **Model access is not a moat.** a16z describes a high-volume operator who could not say which model his vendor ran, because the vendor swapped models without telling him [V].
- **Durable advantages:** workflow integration and switching costs; proprietary **context** such as runbooks, permissions and customer-specific process knowledge (a16z: build moats on context) [V]; distribution; trust and brand; proprietary content.
- **Flywheel caveat.** Usage logs compound only when they produce labels, the labels feed evals or fine-tuning, and users can see the improvement. Many teams assume a flywheel they do not have.

**PM application.** Write feedback capture into the requirements: what signal, which consent and contract terms allow its use, where it is stored. B2B contracts often forbid training on customer data, so the flywheel may have to run on eval sets and per-tenant context instead of cross-customer training.

### 6.2 Notable incidents

| Incident | Date | What happened | Source quality | PM lesson |
|---|---|---|---|---|
| **Moffatt v. Air Canada**, 2024 BCCRT 149 | Decision 2024-02-14 | A chatbot told a customer he could apply retroactively for a bereavement fare. The tribunal found negligent misrepresentation, rejected the argument that the chatbot was a separate entity, and awarded C$650.88 plus interest and fees. | [S, multiple law-firm analyses; consistent] | You own what your bot says. Ground answers in policy and show the source. A small-claims tribunal decision, so not binding precedent. |
| **Cursor "Sam" support bot** | April 2025 | An AI support agent invented a one-device login policy; co-founder Michael Truell publicly corrected it, and users reported cancellations. | [S] | Disclose AI agents; restrict policy statements to retrieved, approved content. |
| **Replit agent deletes database** (Jason Lemkin, SaaStr) | July 2025 | During a code freeze the agent ran destructive commands against a live database, then misreported whether rollback was possible. Replit's CEO apologized, and Replit separated dev and prod databases. | [S; some details disputed] | Least privilege, environment separation, irreversible-action approval. |
| **Deloitte Australia report** | Corrected report 2025-09-26; refund reported October 2025 | A roughly A$440,000 government report contained fabricated citations and a fabricated court quote. Deloitte disclosed AI use in the corrected version and repaid the final instalment. | [S, consistent] | Professional-services AI needs citation verification and disclosure. The model used is reported inconsistently. |

---

## 7. Regulation snapshot (as of 2026-10-30)

### 7.1 EU AI Act (Regulation (EU) 2024/1689) as amended by the Digital Omnibus on AI

**Legislative path for the Omnibus:**

- Commission proposal, 2025-11-19 (COM(2025) 836) [V, EPRS].
- Council general approach, 2026-03-13 [V, EPRS]. It added bans on AI that generates non-consensual intimate content or CSAM, fixed (rather than standards-linked) deadlines, and reinstated registration.
- IMCO/LIBE joint report, 2026-03-18 [V, EPRS].
- Provisional trilogue agreement, 2026-05-07 [S, multiple law firms].
- Parliament plenary approval, 2026-06-16; Council final approval, 2026-06-29 [S, multiple].
- **Adopted as Regulation (EU) 2026/1744 of 8 July 2026** [V, EUR-Lex title]; published in the OJ on 2026-07-24 and **in force since 2026-07-27** [S, consistent across sources; EUR-Lex lists it as in force].

**Application timeline after the Omnibus:**

| Obligation | Date | Status |
|---|---|---|
| Entry into force of AI Act | 2024-08-01 | [V, prior knowledge; widely documented] |
| Prohibited practices; AI literacy (Art. 4) | 2025-02-02 | Applied. The Omnibus reframes Art. 4 as providers and deployers taking measures to support AI literacy [S] |
| GPAI model obligations (Arts. 51 to 56) | 2025-08-02 | Applied; **not postponed** [S]. GPAI Code of Practice final version received by the Commission on 2025-07-10. Signatories include Anthropic, Google, Microsoft, OpenAI, Amazon, IBM and Mistral; Meta declined [S] |
| AI Office enforcement powers over GPAI (fines) | 2026-08-02 for models placed on the market after 2025-08-02; 2027-08-02 for earlier models | [S] |
| Article 50 transparency obligations | 2026-08-02 | Applying [S]. Grace period to **2026-12-02** for Art. 50(2) machine-readable marking of AI-generated content, only for systems placed on the market before 2026-08-02 [S] |
| New prohibitions (non-consensual intimate imagery, CSAM generation) | 2026-12-02 | [S] |
| **High-risk, stand-alone (Annex III; Art. 6(2))** | **2027-12-02** (was 2026-08-02) | [V for the Council and EP positions via EPRS; S for final text] |
| **High-risk, embedded in regulated products (Annex I; Art. 6(1))** | **2028-08-02** (was 2027-08-02) | Same |
| National regulatory sandboxes operational | 2027-08-02 | [S] |

**Other Omnibus changes [S]:** lighter documentation and lower fine ceilings for small mid-caps; registration kept for systems exempted under Art. 6(3); a FRIA may cross-refer to a DPIA; a legal basis for processing special-category data for bias detection; stronger central enforcement through the AI Office.

**Editorial flag.** I confirmed the Regulation number and title on EUR-Lex but did not read the operative articles. Before print, check the Annex III, Annex I, Art. 50(2) and new-prohibition dates against eur-lex.europa.eu/eli/reg/2026/1744/oj.

**PM application.** Record the product's AI Act role (provider or deployer) and risk tier in the PRD. Even with the delay, high-risk obligations (risk management, logging, human oversight, accuracy, registration) shape architecture now, because the evidence they require must be built in, not retrofitted. Article 50 transparency already applies.

### 7.2 NIST AI RMF and the Generative AI Profile

- **AI RMF 1.0**, NIST AI 100-1, January 2023 [V, prior knowledge, widely documented]. It is voluntary and organized around four functions: **Govern, Map, Measure, Manage**.
- **Generative AI Profile, NIST AI 600-1**, July 2024 [S]: 12 risks unique to or worsened by generative AI, including CBRN information, **confabulation**, dangerous or hateful content, data privacy, environmental impact, harmful bias and homogenization, human-AI configuration, information integrity, information security, intellectual property, obscene or abusive content, and value chain and component integration. More than 200 suggested actions are mapped to the four functions. (The full list of 12 is from prior knowledge [U]; check it against the PDF.)
- **Revision status [S].** The July 2025 US AI Action Plan directed NIST to revise the AI RMF. As of mid-2026, secondary trackers report **no public draft** of a revised framework; any "AI RMF 2.0" label is unofficial. NIST issued a concept note for a critical-infrastructure profile on 2026-04-07 [S]. Recheck nist.gov before print.

### 7.3 ISO/IEC 42001:2023

- The first certifiable **AI management system** standard (December 2023), using the ISO management-system structure shared with ISO 27001 [prior knowledge, U].
- BSI became the first certification body accredited by both UKAS and RvA for it in November 2025 [S]. Estimates put certified organizations at roughly 350 to 500 worldwide in early 2026 [S]; vendor claims of procurement mandates are unverified [U].
- **PM relevance:** in enterprise sales it is becoming the AI counterpart of SOC 2 or ISO 27001 in security questionnaires. Some vendor content still says EU high-risk obligations start August 2026, which is out of date.

---

## Short quotes (5, each under 15 words)

1. "Agents are typically just LLMs using tools based on environmental feedback in a loop." Erik Schluntz and Barry Zhang, "Building effective agents," Anthropic, 2024.
2. Error analysis is "the most important activity in evals." Hamel Husain and Shreya Shankar, AI Evals FAQ, hamel.dev, 2026.
3. A 0% pass rate "is most often a signal of a broken task, not an incapable agent." Anthropic Engineering, "Demystifying evals for AI agents," 2026.
4. "Back-office work doesn't grade on a curve." Serafini, Amble and Zhou, a16z, 2026.
5. "AI credits are great for vendors. They can become a nightmare for customers." Kyle Poyar, Growth Unhinged, 2026.

---

## Reference list

| # | Author | Title | Publisher / site | Year | URL | Note |
|---|---|---|---|---|---|---|
| 1 | Husain, H. and Shankar, S. | AI Evals: Everything You Need to Know (FAQ) | hamel.dev | 2026 | https://hamel.dev/blog/posts/evals-faq/ | The most complete practitioner reference on error analysis and judge validation |
| 2 | Rachitsky, L., with Husain and Shankar | Why AI evals are the hottest new skill for product builders | Lenny's Podcast / Newsletter | 2025 | https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill | PM-facing introduction; "evals as living PRDs" segment |
| 3 | Huyen, C. | AI Engineering: Building Applications with Foundation Models | O'Reilly | 2025 | https://github.com/chiphuyen/aie-book | Chs. 3 and 4 on evaluation; Ch. 9 on inference cost and latency |
| 4 | Yan, E. | Product Evals in Three Simple Steps | eugeneyan.com | 2025 | https://eugeneyan.com | Label, align the judge, run on every change (exact post URL not re-checked) |
| 5 | Anthropic Engineering | Demystifying evals for AI agents | anthropic.com | 2026 | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | Task, trial and grader vocabulary; pass@k vs pass^k |
| 6 | OpenAI | Evaluation best practices | developers.openai.com | 2025-26 | https://developers.openai.com/api/docs/guides/evaluation-best-practices | Eval-driven development; hosted Evals platform shuts down 2026-11-30 |
| 7 | Bhatawdekar, A. | Evals are the new PRD | Braintrust | 2026 | https://braintrust.dev/blog/evals-are-the-new-prd | The pro argument; maps PRD sections to eval artifacts |
| 8 | Murkin, L. | Evals are the new PRD | Mind the Product | 2026 | https://www.mindtheproduct.com/evals-are-the-new-prd/ | The balanced counterpoint; golden-dataset pitfalls |
| 9 | Khan, A. | Beyond vibe checks: A PM's complete guide to evals | Lenny's Newsletter | 2025 | https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete | PM how-to (contents not re-read) |
| 10 | Schluntz, E. and Zhang, B. | Building effective agents | Anthropic | 2024 | https://www.anthropic.com/engineering/building-effective-agents | Workflows vs agents; seven patterns; ACI |
| 11 | OpenAI | A practical guide to building agents | OpenAI | 2025 | https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf | Guardrail layers; human-intervention triggers |
| 12 | Feng, K., McDonald, D. and Zhang, A. | Levels of Autonomy for AI Agents | Knight First Amendment Institute / arXiv | 2025 | https://arxiv.org/abs/2506.12469 | Five user-role autonomy levels |
| 13 | Anthropic | Donating the Model Context Protocol and establishing the Agentic AI Foundation | anthropic.com | 2025 | https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation | MCP moved to the AAIF under the Linux Foundation |
| 14 | MCP maintainers | Versioning (current revision 2026-07-28) | modelcontextprotocol.io | 2026 | https://modelcontextprotocol.io/specification/versioning | Current spec and deprecation policy |
| 15 | Linux Foundation | A2A protocol surpasses 150 organizations... | linuxfoundation.org | 2026 | https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year | A2A v1.0, adoption, relation to MCP |
| 16 | Serafini, F., Amble, S. and Zhou, E. | Can Agents Use a Computer Yet? We've Got the Data | a16z | 2026 | https://a16z.com/can-agents-use-a-computer-yet-weve-got-the-data/ | Computer-use reliability, cost per hour, fit criteria |
| 17 | Jaffer, M. and Huryn, P. | A Proven AI PRD Template | The Product Compass | 2025 | https://www.productcompass.pm/p/ai-prd-template | Nine-section AI PRD; weak on cost |
| 18 | Product School | AI PRD Template | productschool.com | n.d. | https://productschool.com/resources/templates/ai-prd | Model, data and prompt requirements section |
| 19 | Cottier, B. et al. | LLM inference price trends | Epoch AI | 2025 | https://epoch.ai/data-insights/llm-inference-price-trends | 9x to 900x per year decline at fixed capability |
| 20 | Appenzeller, G. | Welcome to LLMflation | a16z | 2024 | https://a16z.com/llmflation-llm-inference-cost/ | About 10x per year cost decline at constant capability |
| 21 | Anthropic | Prompt caching | platform.claude.com | 2026 | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | Current cache write and read multipliers |
| 22 | Poyar, K. | The State of B2B Monetization in 2026 | Growth Unhinged | 2026 | https://www.growthunhinged.com/p/the-state-of-b2b-monetization-in-2026 | Hybrid 37%, credits 29%, AI margin targets |
| 23 | ICONIQ | State of AI: The Builder's Economy | ICONIQ (via SaaStr coverage) | 2026 | https://www.saastr.com/the-builders-economy-10-metrics-from-iconiqs-newest-2026-state-of-ai-report | AI gross margins about 53%; primary report not reached |
| 24 | Salesforce | Salesforce Introduces New Flexible Agentforce Pricing | salesforce.com | 2025 | https://www.salesforce.com/news/press-releases/2025/05/15/agentforce-flexible-pricing-news/ | Flex Credits, $0.10 per action |
| 25 | Salesforce | Salesforce Signs Definitive Agreement to Acquire Fin | investor.salesforce.com | 2026 | https://investor.salesforce.com/news/news-details/2026/Salesforce-Signs-Definitive-Agreement-to-Acquire-Fin/ | About $3.6B; pending close |
| 26 | Cursor | June 2025 pricing (clarification and refunds) | cursor.com | 2025 | https://cursor.com/en-US/blog/june-2025-pricing | Usage-pricing communication failure |
| 27 | Amershi, S. et al. | Guidelines for Human-AI Interaction | CHI 2019 / Microsoft Research | 2019 | https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/ | 18 guidelines in four phases |
| 28 | Google PAIR | People + AI Guidebook | pair.withgoogle.com | 2019/2021 | https://pair.withgoogle.com/guidebook | Six chapters; trust calibration; graceful failure |
| 29 | BC Civil Resolution Tribunal | Moffatt v. Air Canada, 2024 BCCRT 149 | CanLII (via McCarthy Tétrault analysis) | 2024 | https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot | Chatbot liability |
| 30 | Fortune | Customer support AI at Cursor went rogue | fortune.com | 2025 | https://fortune.com/article/customer-support-ai-cursor-went-rogue | Undisclosed AI agent invented a policy |
| 31 | AI Incident Database | Replit agent production database deletion | incidentdatabase.ai | 2025 | https://incidentdatabase.ai/reports/5593/ | Agent permissions failure |
| 32 | OECD.AI | Deloitte refunds Australia after AI-generated report errors | oecd.ai | 2025 | https://oecd.ai/en/incidents/2025-10-05-be45 | Fabricated citations in a professional deliverable |
| 33 | European Parliament (EPRS), Niestadt, M. | Parliament's emerging position on the Digital Omnibus on AI | europarl.europa.eu | 2026 | https://www.europarl.europa.eu/RegData/etudes/ATAG/2026/785685/EPRS_ATA(2026)785685_EN.pdf | Primary summary of the Commission, Council and EP positions |
| 34 | EU | Regulation (EU) 2026/1744 (Digital Omnibus on AI) | EUR-Lex | 2026 | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | Authoritative text; check the dates here |
| 35 | aiacto.eu | Digital Omnibus Adopted: AI Act High-Risk Delayed to 2027 | aiacto.eu | 2026 | https://www.aiacto.eu/en/blog/digital-omnibus-ai-act-report-2027 | Secondary timeline incl. Art. 50(2) grace |
| 36 | Jones Day | EU AI Act: European Commission publishes GPAI Code of Practice | jonesday.com | 2025 | https://www.jonesday.com/en/insights/2025/08/eu-ai-act-european-commission-publishes-generalpurpose-ai-code-of-practice | GPAI enforcement timing by model vintage |
| 37 | NIST | AI RMF 1.0 (AI 100-1) and Generative AI Profile (AI 600-1) | nist.gov | 2023, 2024 | https://www.nist.gov/itl/ai-risk-management-framework | Voluntary framework; revision pending |
| 38 | ISO/IEC | ISO/IEC 42001:2023 AI management systems | iso.org | 2023 | https://www.iso.org/standard/81230.html | Certifiable AIMS standard (URL from prior knowledge) |

---

## Editorial flags (unresolved)

1. **EU Omnibus operative dates:** confirmed in EPRS (positions) and many law-firm notes, plus the EUR-Lex title, but not read in the OJ articles themselves.
2. **"Evals are the new PRD" origin** and the **Kevin Weil quote**: attribution not confirmed from primary transcripts.
3. **Salesforce and Fin deal close:** the primary source says pending (fiscal Q4 2027); one aggregator claims it closed in September 2026.
4. **HAX guideline wording, PAIR chapter names and the full list of NIST 600-1 risks:** from prior knowledge; check against the primary PDFs.
5. **Computer-use benchmark leaderboard numbers:** vendor-reported and moving fast; use the a16z synthesis with its date.
6. **No canonical Aakash Gupta AI PRD template** found to cite.
