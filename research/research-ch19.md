# Research notes: Chapter 19, AI-Native Analysis: Collecting Data and Asking the Harness

Status: complete (2026-10-30). Research constraint: the shared WebSearch budget for this run was exhausted before this chapter began, so all sources below were reached by direct WebFetch of known primary URLs, plus MCP governance facts already verified in research-ch31.md (cross-referenced, not re-fetched). Tags: [V] verified on primary source, [S] secondary only.

## (b) Verified facts (running log)

### MCP architecture (modelcontextprotocol.io, "Architecture overview", spec revision 2026-07-28, fetched 2026-10-30) [V]
URL: https://modelcontextprotocol.io/docs/learn/architecture
- Participants: an MCP **host** (the AI application, for example Claude Desktop, Claude Code or VS Code) creates one MCP **client** per MCP **server**; each client keeps a dedicated connection to its server. A server is "a program that provides context to MCP clients".
- Local servers use the stdio transport and typically serve one client; remote servers use Streamable HTTP and typically serve many clients. MCP recommends OAuth to obtain authentication tokens for remote servers.
- Server primitives: **tools** (executable functions the AI can invoke, such as API calls or database queries), **resources** (data sources that provide context, such as file contents, records, API responses), **prompts** (reusable templates, such as system prompts or few-shot examples).
- The docs' own example matches our use case: a database server can expose tools for querying, a resource holding the schema, and a prompt with few-shot examples.
- Client primitive: **elicitation** (server asks the user for input or confirmation). **Sampling and logging are deprecated** as of 2026-07-28.
- 2026-07-28 makes the protocol stateless: every request carries version and capabilities; servers implement a mandatory `server/discover` request. Optional extensions include a Tasks extension for long-running requests (durable handle, poll for result), relevant to long warehouse queries.
- The spec says MCP "does not dictate how AI applications use LLMs or manage the provided context". PM implication: the protocol moves data; judgement about context and verification stays with the user and the harness.

### MCP governance (cross-reference to research-ch31.md, verified there) [V]
- Anthropic donated MCP to the Agentic AI Foundation (AAIF), a directed fund under the Linux Foundation, on 2025-12-09; co-founded by Anthropic, Block and OpenAI. Source: https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
- At donation: more than 10,000 active public MCP servers and over 97 million monthly SDK downloads (Anthropic's figures).
- Current spec revision 2026-07-28 with at least 12 months' deprecation notice. Source: https://modelcontextprotocol.io/specification/versioning

### Claude custom connectors (Claude Help Center, "Getting started with custom connectors using remote MCP", fetched 2026-10-30; page shows no fixed date) [V]
URL: https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp
- Available on Free, Pro, Max, Ultra, Team and Enterprise; Free is limited to one custom connector.
- On Team, only Owners and Primary Owners can add connectors; on Enterprise, Owners, Primary Owners and custom roles with library-management rights. Members then connect and enable each connector individually (each authenticates as themselves).
- Anthropic does not verify custom connectors. The page tells users to connect only to trusted servers, review requested permissions, watch for prompt injection in hidden server instructions, and expect that developers may change tool behaviour.
- Individual tools can be switched off per conversation; for Research mode the page advises disabling tools that can write.
- PM application: this is the "approved tools" layer. The org admin decides which connectors exist; the PM decides which tools are on for a given analysis (read-only for analysis).

### Claude Projects (Claude Help Center, "What are projects?", fetched 2026-10-30) [V]
URL: https://support.claude.com/en/articles/9517075-what-are-projects
- A project is a workspace with its own chats, **project knowledge** (uploaded docs, text, code, files) and **project instructions** (how Claude should respond).
- All plans; free users capped at five projects. On paid plans, retrieval (RAG) switches on automatically as knowledge nears the context limit; Anthropic says this can raise capacity up to tenfold.
- PM application: a project per product area is the natural home for the context pack (metric dictionary, Product 360 summary, schema notes, prior reports).

### Long-context prompting (Claude Developer Platform docs, "Prompting best practices", long context section, fetched 2026-10-30) [V]
URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (old long-context-tips URL redirects here)
- For inputs of 20k+ tokens: put long-form data at the top, above the question, instructions and examples. Anthropic states queries at the end "can improve response quality by up to 30 percent in tests", especially with complex multi-document inputs.
- Wrap each document in `<document>` with `<source>` and `<document_content>` subtags (template reproduced in section a, Pattern C1).
- Ground responses in quotes: ask Claude to extract relevant quotes first, then answer from them.

### Reduce hallucinations (Claude Developer Platform docs, fetched 2026-10-30) [V]
URL: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Basic: allow "I don't know"; use direct quotes for documents over about 20k tokens; verify with citations and retract any claim without a supporting quote.
- Advanced: chain-of-thought verification (review summarized reasoning), best-of-N verification (run the same prompt several times and compare; inconsistency signals hallucination), iterative refinement, external knowledge restriction (only use provided documents).
- The page notes these techniques reduce but do not eliminate hallucinations; validate critical information for high-stakes decisions.

### Context engineering (Anthropic Engineering, "Effective context engineering for AI agents", 2025-09-29, Rajasekaran, Dixon, Ryan, Hadfield) [V]
URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Context engineering curates the whole token set the model sees (system prompt, tools, external data, history); prompt engineering is a subset.
- "Context rot": recall degrades as the window fills; context has an attention budget with diminishing returns.
- Principle: find "the smallest possible set of high-signal tokens" for the desired outcome.
- Just-in-time retrieval: keep lightweight references (file paths, stored queries, links) and let the agent load data through tools at runtime; slower but more adaptive; hybrids are common.
- PM application: a context pack should be short and curated, with links to live sources, not a dump of every export.

### Agent Skills (Anthropic/Claude blog, "Introducing Agent Skills", 2025-10-16; update 2025-12-18) [V]
URL: https://claude.com/blog/skills (anthropic.com/news/skills redirects here)
- Skills are folders of instructions, scripts and resources that Claude loads only when relevant (progressive disclosure). Available in Claude apps (Pro, Max, Team, Enterprise), Claude Code and the API.
- Examples given: Excel creation, brand guidelines; Rakuten uses skills for finance workflows that flag spreadsheet anomalies (Anthropic's customer claim).
- 2025-12-18 update: Agent Skills published as an open standard for cross-platform portability.
- PM application: package a team's recurring analysis (weekly metrics review, report format, verification checklist) as a skill so every PM runs it the same way.

### File creation and analysis (Claude blog, "Claude can now create and edit files", 2025-09-09) [V]
URL: https://claude.com/blog/create-files
- Claude creates and edits spreadsheets, documents, slide decks and PDFs, working in a private computer environment where it writes and runs code.
- Data analysis use: supply raw data, receive cleaned data, statistical analysis, charts and written insights.
- Anthropic's own warning: the feature gives Claude internet access, which may put data at risk; monitor chats closely.
- PM application: the PM never writes the code, but should ask to see the method (the code or steps the harness ran) as part of verification.

### Lethal trifecta (Simon Willison, simonwillison.net, 2025-06-16) [V]
URL: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- An agent that combines (1) access to private data, (2) exposure to untrusted content an attacker could write (web pages, emails, tickets) and (3) a way to send data out (HTTP requests, links) can be tricked into leaking private data.
- Willison argues vendor guardrails cannot reliably prevent this when users mix tools themselves; his advice is to avoid the combination entirely.
- PM application: an analysis session that has CRM and support-ticket connectors (private data plus attacker-writable ticket text) should not also have web or messaging tools that can send data out. Keep analysis sessions read-only and closed.

### MCP Security Best Practices (modelcontextprotocol.io, revision 2026-07-28, fetched 2026-10-30) [V]
URL: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- Named attack classes: confused deputy (proxy servers), token passthrough (forbidden by the authorization spec: servers must not accept tokens not issued to them), SSRF, state handle hijacking, local MCP server compromise, OAuth URL validation, mix-up attacks, localhost redirect impersonation.
- **Scope minimization** is the PM-relevant one. Broad scopes (`files:*`, `db:*`, `admin:*`) widen blast radius, make revocation disruptive, add audit noise and cause "consent abandonment" when users see long scope lists. Recommended: a minimal initial read-only scope, then incremental step-up when a privileged operation is first attempted. Listed mistakes include wildcard or omnibus scopes and bundling unrelated privileges.
- Local servers run with the client's privileges; clients must show the exact command and get consent before running a one-click local server.
- PM application: in a data access request, ask for named read scopes, not "full access"; prefer remote, vendor-hosted servers behind SSO over unvetted local ones.

### Spider 2.0 (Lei, Chen, Ye et al., ICLR 2025 oral; arXiv 2411.07763, v2 2025-03-17) [V]
URL: https://arxiv.org/abs/2411.07763
- Benchmark of real enterprise text-to-SQL workflows (schemas above 1,000 columns, BigQuery and Snowflake, multiple dialects, long multi-query tasks).
- At publication, an o1-preview code agent solved 21.3% of Spider 2.0 tasks, versus 91.2% on Spider 1.0 and 73.0% on BIRD.
- PM application: the gap between academic and enterprise benchmarks is the argument for governed metric layers and verification. Do not quote 21.3% as the state of the art in 2026 (see flags); quote it as "at publication".

### OWASP Top 10 for LLM Applications 2025: LLM02 Sensitive Information Disclosure (OWASP GenAI Security Project) [V]
URL: https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/
- Risk that LLM apps expose PII, financial details, health records, confidential business data, credentials, legal documents or proprietary code through output.
- Prevention themes: data sanitization and masking, access controls with least privilege and limited data-source access, privacy techniques (redaction, differential privacy), transparency and user education about what not to input.

### dbt MCP server (dbt Labs docs, fetched 2026-10-30) [V]
URL: https://docs.getdbt.com/docs/dbt-ai/about-mcp
- Gives AI applications governed access to dbt models, metrics, lineage and freshness. Self-hosted (local, for development) or remote (HTTP to the dbt platform, for consumption).
- Tool categories: Semantic Layer, SQL, metadata discovery, Administrative API, product docs.
- dbt's argument: without a semantic layer, LLMs infer business logic from raw tables and give inconsistent answers; querying through it computes metrics the same way everywhere.

### Snowflake-managed MCP server (Snowflake docs, fetched 2026-10-30) [V]
URL: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp
- Serves Cortex Analyst over semantic views, Cortex Search, Cortex Agents, custom tools and SQL execution through MCP. Snowflake recommends exposing a Cortex Agent as the main tool for governed business questions because direct SQL can bypass orchestration.
- RBAC applies per tool: the docs note that access to the server does not give access to its tools; each tool needs its own grant. OAuth authentication. Up to 50 tools per server. GA status and dates not stated on the page (flag).

### Vendor MCP servers by category (each fetched 2026-10-30) [V]
Pattern across vendors: hosted remote server, OAuth sign-in as the individual user, the server respects the user's existing permissions, and an admin switch to enable it. Status labels change fast; cite "as documented in October 2026".
- **Product analytics, Amplitude.** https://amplitude.com/docs/amplitude-ai/amplitude-mcp (page updated 2026-10-30). Read and modify charts, dashboards, notebooks, experiments, cohorts, feature flags, metrics, events, properties, session replays. Clients include Claude, Claude Code, Cursor, ChatGPT, Gemini CLI, Codex CLI. OAuth 2.0; respects the user's existing permissions and grants no extra data access; admins can restrict org-wide; role-based "Use MCP" read and write permissions per project.
- **Product analytics, Mixpanel.** https://docs.mixpanel.com/docs/mcp. Query events, funnels, retention; manage dashboards and Lexicon metadata. Clients include Claude, ChatGPT, Cursor, Codex. OAuth (service accounts in beta); docs say all existing project permissions and roles apply. US, EU and India regions (relevant to data residency). Admins enable it in AI settings; on by default for new free and growth accounts created after 2026-08-01.
- **Warehouse, Google BigQuery.** https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp (updated 2026-10-29). Managed endpoint; tools list_dataset_ids, list_table_ids, get_dataset_info, get_table_info, execute_sql and a read-only execute_sql_readonly. OAuth 2.0 plus IAM roles (MCP Tool User, BigQuery Job User, BigQuery Data Viewer). Status not stated.
- **Warehouse, Snowflake** and **semantic layer, dbt**: see above.
- **Ticketing and docs, Atlassian.** https://www.atlassian.com/blog/announcements/remote-mcp-server (2025-05-01). Remote MCP server for Jira and Confluence Cloud, launched in beta with Claude as first official partner; hosted by Atlassian on Cloudflare; OAuth; honours each user's existing permissions. (Current GA status not re-verified: flag.)
- **Chat, Slack.** https://docs.slack.dev/ai/mcp-server. Search messages, files, users and channels; read channels and threads; also send and schedule messages, manage canvases. OAuth user tokens with per-tool scopes; workspace admins approve client access; only Marketplace-published or internal apps. Clients include Claude.ai and Claude Code. Note the write tools: for analysis, disable send tools (lethal trifecta).

### DSBench (Jing, Huang, Wang et al., arXiv 2409.07703, v3 2025-04-11) [V]
URL: https://arxiv.org/abs/2409.07703
- Benchmark of realistic data analysis and data modeling tasks for data science agents. At publication, the best agent solved 34.12% of data analysis tasks.
- Use only as historical evidence that unsupervised agent analysis was unreliable on realistic tasks; 2026 models will score differently (flag).

### Anthropic commercial data use (Anthropic Privacy Center, "Is my data used for model training?", as of 2026-08-18) [V]
URL: https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training
- Commercial products (Claude for Work, Anthropic API) are not used for training by default unless the customer opts in. Feedback (thumbs up or down) may be used and is kept up to 5 years, de-linked from IDs; Team and Enterprise owners can disable feedback.
- PM application: one reason the "approved tool" rule matters. Pasting customer data into a personal consumer account carries different terms than the company's enterprise workspace.

### GDPR Article 5 (gdpr-info.eu, text of Regulation (EU) 2016/679) [V]
URL: https://gdpr-info.eu/art-5-gdpr/
- Six principles in 5(1): lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality.
- Data minimisation: personal data "adequate, relevant and limited to what is necessary". Purpose limitation: "collected for specified, explicit and legitimate purposes".
- PM application: the data access request states purpose, minimum fields, retention; aggregate or pseudonymise before the harness sees it.

### NIST AI 600-1 (Generative AI Profile of the AI RMF), 2024-07-26 [V for number and date]
URL: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- The landing page confirms the number and date. The risk list (which includes "confabulation") was not re-read on this pass: tag the risk names [S].

### MCP Registry (MCP blog, 2025-09-08) [V]
URL: https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/
- Open catalog and API of public MCP servers, launched in preview 2025-09-08, with no durability guarantees before GA. Enterprises can run private sub-registries that use it as upstream. PM application: the "approved connector list" can be a curated sub-registry run by IT, not a wiki page.

### Agent Skills open format (agentskills.io, fetched 2026-10-30) [V]
URL: https://agentskills.io/
- A skill is a folder with a `SKILL.md` (frontmatter `name` and `description` at minimum, plus instructions) and optional `scripts/`, `references/`, `assets/`. Loading is three-stage progressive disclosure: discovery (name and description only), activation (full SKILL.md when a task matches), execution. Originally developed by Anthropic, released as an open standard, adopted by many agent clients.

### Report structure and charts (books; not re-fetched beyond landing pages)
- Cole Nussbaumer Knaflic, *Storytelling with Data* (Wiley, 2015 [S for publisher and year]); site confirms title and author and that the book runs from choosing a chart type to designer thinking on colour and annotation. https://www.storytellingwithdata.com/books [V for title and author]
- Barbara Minto, *The Pyramid Principle*: ideas arranged as a pyramid under one main point; SCQ (situation, complication, question) intro. https://www.barbaraminto.com/ [V for pyramid and SCQ names]

## (a) Key concepts and frameworks for the chapter

### A1. The AI-native analysis loop (synthesis for the book; Product 360 framing, not an external framework)
Question, Access, Context, Ask, Verify, Report, Decide. Each step has an artifact: question (analysis request brief), access (data access request), context (context pack), ask (prompt patterns), verify (verification checklist), report (AI-generated report review), decide (decision log entry from earlier chapters). Label this as the book's own synthesis.

### A2. Collecting and permissioning data
- **Approved tools first.** Use the company's enterprise harness workspace and admin-approved connectors (Claude Help Center: on Team and Enterprise only owners or permitted roles add connectors; members authenticate individually). Commercial terms differ from consumer terms on training use (Anthropic Privacy Center).
- **Classify before you connect.** A simple four-tier scheme (public, internal, confidential, restricted) is a common industry convention; present it as convention, not a named standard. Restricted (PII, credentials, customer contract terms, security logs) never goes into a harness except through an approved, governed connector.
- **Least privilege, read-only by default.** MCP Security Best Practices: minimal initial scope, step-up only when needed, no wildcard scopes (Section b). Snowflake: server access does not imply tool access. BigQuery: a read-only SQL tool exists; ask for it.
- **Minimise and aggregate.** GDPR Art. 5 purpose limitation and data minimisation; OWASP LLM02 sanitization and masking. Prefer account-level aggregates and pseudonymous IDs to row-level personal data.
- **Avoid the lethal trifecta** (Willison): never combine private data, untrusted text (tickets, chats, web) and an outbound channel in one analysis session. Turn off write and send tools (Claude Help Center advises the same for Research).

### A3. Connectors and MCP servers in 2026
- Definition from the spec: host, client, server; tools, resources, prompts (Section b). In plain terms for PMs: an MCP server is an adapter a vendor publishes so any compliant harness can read (and sometimes write) that vendor's data as the signed-in user.
- Categories with documented 2026 examples: product analytics (Amplitude, Mixpanel), warehouse (BigQuery, Snowflake), semantic or metrics layer (dbt Semantic Layer, Snowflake semantic views), ticketing and docs (Jira and Confluence via Atlassian), chat (Slack). CRM and support systems also publish servers; not verified on this pass (flag), so name the category without vendor claims or verify before drafting.
- Governance: open protocol under the Agentic AI Foundation (Linux Foundation) since 2025-12-09; spec 2026-07-28 with a 12-month deprecation policy.
- **Governed metrics beat raw tables.** dbt and Snowflake both argue that answers should come through a semantic layer so "active account" means one thing. Spider 2.0 shows why: raw enterprise schemas defeat models far more often than academic benchmarks suggest.

### A4. File-based context versus live connectors (book's comparison table)
| | Files (exports, CSV, PDF, decks) | Live connectors (MCP) |
|---|---|---|
| Freshness | Snapshot at export time | Current at query time |
| Reproducibility | High: the file is the evidence | Lower unless the query and timestamp are saved |
| Permissions | Whoever holds the file | The signed-in user's existing rights |
| Best for | One-off deep dives, board numbers, sharing a frozen dataset | Recurring reviews, exploration, drill-down |
| Main risk | Stale or wrong export, PII leakage via copies | Wrong table or metric, write tools, injection via retrieved text |
Rule of thumb: explore live, decide on a frozen snapshot. Ask the harness to save the exact query, filters and timestamp alongside any number that goes into a decision.

### A5. Passing context into the harness
- **Projects and knowledge** (Claude Projects; other harnesses have equivalents): one project per product area, holding the context pack and instructions. RAG switches on automatically on paid plans as knowledge grows.
- **Context engineering** (Anthropic Applied AI team, 2025): smallest high-signal set; references plus just-in-time retrieval over pre-loading everything; context rot as windows fill.
- **Long-context structure** (Anthropic docs): data at the top, question at the end (up to 30% better in Anthropic's tests); each document tagged with source; extract quotes first.
- **Skills** (Anthropic, open standard): package recurring analyses (weekly metrics review, report format, verification checklist) so they run identically for every PM.
- **The Product 360 as context.** The PM's Product 360 (vision, personas, North Star and input metrics, strategy, current bets) is the single best context document: it tells the harness what "good" means and which segments matter.

**Context pack template (for the chapter's artifact):**
1. Purpose and decision this pack supports. 2. Product 360 summary (one page). 3. Metric dictionary: name, plain-language definition, owner, source system, grain, time zone, known caveats, canonical value for last period (for reconciliation). 4. Segment definitions (tier, region, partner versus direct). 5. Source map: which connector or file answers which question; freshness. 6. Data rules: classification, what must not be pulled, aggregation level. 7. Known data incidents and gaps (for example tracking change dates). 8. House style for reports. 9. Glossary of internal terms.

### A6. Analysis prompt patterns (draft prompts; the chapter should have many)
Base structure for every analysis prompt: Role and goal; Data (named sources, time window with explicit dates and time zone, segment); Definitions (point to the metric dictionary); Method requirements (show the query or steps; state assumptions); Output (table plus three-sentence finding); Honesty clause ("If the data cannot answer this, say so and say what is missing").
- **Describe:** "Using the Beacon weekly metrics source, report diagnosis acceptance rate for each of the last 12 complete ISO weeks (Monday to Sunday, UTC), overall and by customer tier. Show the query you ran, row counts per week, and flag any week with fewer than 50 diagnoses."
- **Diagnose:** "Acceptance rate fell from week 36 to week 41. Decompose the change into mix (which customers and incident types contributed volume) and rate (within-segment change). List the three largest contributors with numbers, then list two alternative explanations you could not rule out and what data would rule them out."
- **Compare:** "Compare MTTR for incidents where responders accepted Beacon's root cause against those where they did not, last 90 days, matched by severity. State why this comparison is not causal and what confounders remain."
- **Forecast:** "Project weekly resolved-with-Beacon incidents for the next 8 weeks under three scenarios (base, migration delayed, Agents adoption doubles). Give the method, the inputs you assumed, and a range rather than a point. Say which assumption the result is most sensitive to."
- **Segment:** "Cluster accounts by how they use Beacon (correlate only, diagnose, act). For each segment give count, ARR share, NRR and a one-line description. Use account-level aggregates only; no user-level data."
- **Qualitative synthesis:** "From these 40 support tickets and 12 call notes (attached, sources tagged), extract verbatim quotes about root-cause trust, group them into themes with counts, and keep the ticket ID next to every quote."
- **Report generation:** "Write a one-page update for Marcus (VP IT Ops). Lead with the answer in one sentence, then three supporting points, each with the number, its source and date window. Include one chart: acceptance rate by week with the launch date annotated. End with the decision requested and the open risks. Do not add any number not present in the analysis above."
- **Self-check prompt:** "Before you answer, list every number you will report with its source query and time window. Recompute each from the raw result. Flag any that changed."
- **Adversarial review prompt:** "Act as a skeptical finance partner. List the five weakest points in this analysis and what would change the conclusion."

### A7. Verifying AI-generated numbers (verification checklist draft)
Grounded in Anthropic's hallucination guidance (allow uncertainty, quotes and citations, best-of-N, restrict to provided data) plus standard analyst practice:
1. **Reconcile to source:** at least one headline number matches the system of record or the canonical value in the context pack.
2. **Ask for the method:** the query, filters, joins and time window used; read it in plain language ("explain this query as if to a non-analyst").
3. **Spot-check:** pick three rows or accounts and trace them end to end.
4. **Sanity bounds:** rates between 0 and 100%; segment counts sum to the total; week-over-week changes within plausible range; compare with last published value.
5. **Time-window traps:** partial current week or month, time zone mismatch (UTC versus local), fiscal versus calendar periods, trailing versus calendar windows, late-arriving data.
6. **Definition drift:** "active", "customer", "resolved" match the metric dictionary; deduplication of accounts and incidents.
7. **Denominator and mix:** averages of averages, Simpson's paradox across segments, survivorship (churned accounts dropped).
8. **Run it twice** (best-of-N): rerun or ask a fresh session; inconsistent numbers mean stop.
9. **Provenance in the report:** every number carries source, window and timestamp.
10. **Stakes-based depth:** a board or pricing number gets an analyst or data owner sign-off; an exploratory number does not.

### A8. Charts and narrative reports with AI
- The harness can produce charts and files directly (Claude file creation, 2025-09-09). PM's job is the brief: chart type for the comparison, one message per chart, annotate events, start bars at zero, label units and windows (Knaflic's principles, paraphrased).
- Narrative: answer first, grouped support (Minto pyramid); SCQ for the opening.
- **AI-generated report review (artifact):** Does the headline answer the question asked? Is every number traceable? Are causal words ("drove", "caused") justified? Are caveats proportional? Any number or quote not in the analysis? Is the chart honest (axis, window, annotation)? Is the decision request explicit? Has PII or customer naming been removed for the audience?

### A9. From answer to decision
An answer becomes a decision input only when it has: a stated confidence level, the decision it informs, the threshold that would change the decision, and an owner. Tie back to decision logs and metric trees in earlier chapters. Suggest a "decision memo" closing prompt: "Given this verified analysis, draft the options, the evidence for each, the reversible versus irreversible nature of each, and the recommendation, keeping facts and judgement in separate sections."

### A10. Artifacts (drafted structures)
**Data access request:** requester and role; purpose and decision supported; data sources and connectors; fields needed (minimum); classification of each; aggregation level; read-only scopes requested; duration and review date; retention and deletion of exports; harness and workspace used; approver (data owner, security reviewer); audit logging confirmed.
**Analysis request brief:** question in one sentence; decision it informs and by when; audience; metrics with dictionary links; time window with explicit dates and time zone; segments; sources allowed; known caveats; output format; verification depth required; owner.
**Verification checklist:** A7.
**AI-generated report review:** A8.
**Context pack template:** A5.

## (c) Short quotes (under 15 words)
1. "the smallest possible set of high-signal tokens" (Anthropic Applied AI team, Effective context engineering for AI agents, 2025)
2. "avoid that lethal trifecta combination entirely" (Simon Willison, The lethal trifecta, 2025)
3. "only loads what's needed, when it's needed" (Anthropic, Introducing Agent Skills, 2025)
4. "adequate, relevant and limited to what is necessary" (GDPR Article 5(1)(c))
5. MCP "does not dictate how AI applications use LLMs or manage the provided context" (MCP Architecture overview); trim to under 15 words if used.

## (d) 2025 to 2026 AI-era developments (verified)
- 2025-05-01: Atlassian remote MCP server (beta) for Jira and Confluence, Claude first partner.
- 2025-06-16: Willison names the lethal trifecta.
- 2025-09-08: MCP Registry preview, with private sub-registries for enterprises.
- 2025-09-09: Claude creates and edits spreadsheets, docs, decks, PDFs; data analysis with charts.
- 2025-09-29: Anthropic's context engineering essay.
- 2025-10-16: Agent Skills; 2025-12-18 published as an open standard.
- 2025-12-09: MCP donated to the Agentic AI Foundation (Linux Foundation).
- 2026-07-28: MCP spec revision (stateless, `server/discover`, sampling deprecated, 12-month deprecation policy).
- 2026: analytics and warehouse vendors (Amplitude, Mixpanel, BigQuery, Snowflake, dbt) document hosted MCP servers that respect existing permissions; Mixpanel turned MCP on by default for new free and growth accounts after 2026-08-01.
- 2026-08-18 (as-of date): Anthropic commercial products not used for training by default.

## (e) Beacon worked example ideas (consistent with beacon-case.md)
- **Question:** After Beacon Agents launched, diagnosis acceptance rate fell (choose an illustrative drop, clearly fictional) while weekly active responders rose. Is the agent getting worse, or is the mix changing? Decision: whether to delay the per-resolved-incident pricing pilot, since pricing depends on trust in diagnosis.
- **Access:** You file a data access request with Sam (security and compliance reviewer): read-only product analytics connector, read-only warehouse access through the semantic layer, Jira for change tickets, no Slack send tools, no customer-identifiable incident text leaving the warehouse; incidents aggregated by account tier and incident type. Sam asks for audit logging and EU data staying in the EU region (ties to EU AI Act storyline).
- **Context pack:** Beacon Product 360 summary, North Star (incidents resolved with Beacon's help per week), metric dictionary (acceptance rate definition, MTTR, autonomous resolution rate, compression ratio), segment definitions (direct enterprise versus MSP via Leo), known data events (Beacon Classic migration cohorts; the hallucinated-root-cause incident date).
- **Ask:** Describe, then diagnose (mix versus rate). Finding pattern: the drop is concentrated in accounts migrated from Beacon Classic, where alert grouping differs, so the denominator changed. A verification catch: the first AI answer used a trailing 7-day window ending mid-week in UTC, mixing a partial week; the reconciled number differs from the dashboard until the window is fixed. A second catch: "accepted" was counted per responder action, not per incident, double-counting incidents with two responders.
- **Qualitative:** Ticket and call-note synthesis shows Priya-type SRE leads distrust root causes after the wrong-service rollback incident; quotes kept with ticket IDs.
- **Report:** One-page note to Marcus and the VP of Product: answer first, chart of acceptance by week split by migrated versus native, decision: keep the pricing pilot on native accounts, delay for migrated ones until the Classic migration completes; owner and review date.
- **Dana's lens:** keep one prompt that asks how the finding changes the 3 a.m. experience, to stop analysis drifting from the user.
- All numbers in the worked example must be illustrative and labelled fictional; reuse given figures (ARR $48M, 420 customers, NRR 118%, margin 81% to 72%) only as given.

## (f) Editorial flags
1. **Search budget:** the shared WebSearch budget was exhausted before this chapter started; all sources came from direct fetches of known URLs. No independent search for 2026 developments not already known (for example newer text-to-SQL benchmarks or CRM vendor MCP servers) was possible. A follow-up pass is recommended.
2. **Spider 2.0 and DSBench figures** are at-publication results (2024 to 2025). Leaderboards will have moved by late 2026. Use them only as "at publication" evidence that enterprise schemas are hard, never as current capability.
3. **Vendor status labels** (GA versus preview) were not stated on the BigQuery, Snowflake and Slack pages; Atlassian's server launched as beta in May 2025 and its current status was not re-verified. Avoid status claims in the chapter, or verify before drafting.
4. **CRM and support-desk MCP servers** (for example Salesforce, HubSpot, Zendesk) were not verified on this pass. Describe the category without vendor-specific claims.
5. **"Up to 30 percent" and "up to tenfold"** are Anthropic's own claims from its docs and help center; attribute them to Anthropic.
6. **Four-tier data classification** is common convention, not a single named standard; present it as an example.
7. **NIST AI 600-1 risk list** (including "confabulation") not re-read; tag [S] or verify.
8. **Knaflic publisher and year** (Wiley, 2015) from memory: [S].
9. **Product drift:** Claude plan names (Free, Pro, Max, Ultra, Team, Enterprise) and admin-role details come from help-center pages that change frequently; keep the chapter vendor-neutral where possible ("your harness's project or workspace feature") and use Claude as the worked example.
10. **The Anthropic file-creation feature notes internet access as a data risk**; the chapter should mention the setting exists without giving click-paths.
11. The chapter must not teach SQL: "ask for the query" means asking the harness to show and explain its method in plain language, not reading or editing the query.
