# Research notes: Chapter 32, The AI-Augmented Product Manager

Status: complete (24 sources; about 6,600 words, over the 4,000 target because the raw source log is kept). Compiled 2026-10-30. Note: the shared WebSearch budget for this run was exhausted before this chapter began, so sources were reached by direct WebFetch of known URLs plus cross-checks against verified notes for chapters 00, 03, 04, 07, 14 and 19. Tags: [V] verified on primary source in this session or in an earlier chapter's notes; [S] secondary only; [U] unverified.

## Source log (raw extracts)

### S1. Segal, N. and Rachitsky, L. "AI tools are overdelivering" (survey). Lenny's Newsletter, 23 Dec 2025. [V]
URL: https://www.lennysnewsletter.com/p/ai-tools-are-overdelivering-results
- n = 1,750 tech workers (PMs, engineers, designers, founders, others). Survey field dates not stated.
- PM top current uses: writing PRDs 21.5%; mockups and prototypes 19.8%; improving communication (email, presentations) 18.5%; user research 4.7%; roadmap ideas 1.1%.
- PM demand gaps: user research is the largest gap of any task (+27.2 points; about a third want it as a primary use). Mockups and prototypes 19.8% now versus 44.4% desired (+24.6 points), the most wanted future use.
- 63% of PMs say AI saves 4+ hours a week. Over 70% of PMs report quality improvements.
- PM tools: ChatGPT most used (57.7%), Claude second; Lovable 8.7%, Copilot 8.4%, Cursor 7.7%.
- All roles: 55% say AI exceeded expectations; almost 70% say it improved work quality; more than half save at least half a day a week; 92.4% report at least one significant downside; engineers 51% better quality and 21% worse (highest "worse" share); designers least positive (45% positive ROI vs 78% founders). Agentic platform adoption in 2025 described as slow.
- Reading for the chapter: PMs use AI for production work (documents, mockups, communication) far more than for upstream discovery and strategy. That is the gap the chapter should close.

### S2. Cagan, M. "The AI Productivity Paradox." SVPG, 23 Jul 2026. [V]
URL: https://www.svpg.com/the-ai-productivity-paradox/
- Teams use AI to ship faster but outcomes do not improve, because most use it to accelerate the project model, which is built for output rather than outcomes.
- Strong product companies win on culture, strategy and discovery, not delivery speed, so AI is widening the gap between strong companies and the rest.
- Strong teams use AI first to "build to learn" (discovery: generate and test solutions with users and stakeholders for value and viability) and only then to "build to earn" (delivery: reliable, scalable, commercial quality).
- Cites Atlassian State of Teams 2026: 89% of executives say AI increased speed of work; only 6% confident they can point to specific organization-wide AI ROI [S, via Cagan; Atlassian primary not fetched]. Cites McKinsey Quarterly that sustained performance impact is elusive (no figures). Also quotes Hilary Gridley and Chip Huyen.
- Verbatim phrase: "designed to deliver output, rather than outcomes".

### S3. Rajasekaran, P., Dixon, E., Ryan, C. and Hadfield, J. (Anthropic Applied AI team). "Effective context engineering for AI agents." Anthropic Engineering, 29 Sep 2025. [V]
URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Context engineering curates the whole token set the model sees at inference (system prompt, tools, data, message history); prompt engineering is a subset. Iterative: curation happens on every call.
- "Context rot": recall degrades as the window fills; models have a finite "attention budget".
- System prompts at the "right altitude": neither brittle hard-coded logic nor vague guidance. Start minimal; add instructions and examples in response to observed failures.
- Few diverse canonical examples beat long lists of edge-case rules. Tools minimal and unambiguous.
- Just-in-time retrieval: keep lightweight references (paths, links, queries) and load at run time; hybrid with some upfront loading often works best.
- Long tasks: compaction (summarize and restart), structured note-taking (persistent notes outside the window), sub-agents with clean contexts returning condensed summaries.
- Verbatim goal: "find the smallest set of high-signal tokens".

### S4. Anthropic. "Introducing Agent Skills." claude.com blog, 16 Oct 2025, updated 18 Dec 2025. [V]
URL: https://claude.com/blog/skills
- A skill is a folder of instructions (SKILL.md), scripts and resources that Claude loads only when a task calls for it, loading the minimum needed (progressive disclosure pattern).
- Available in Claude apps (Pro, Max, Team, Enterprise; admins enable on Team and Enterprise), the API, Claude Code and the Agent SDK.
- 18 Dec 2025 update: organization-wide skill management, partner skills directory, Agent Skills published as an open standard (agentskills.io) for cross-platform portability.
- Business examples: document generation to company standards, brand guidelines, Rakuten finance workflow (Anthropic customer claim, treat as vendor material).
- PM application: package recurring PM work (weekly metrics narrative, PRD review, win/loss synthesis, release notes in house style) as team skills so every PM gets the same format and checks.

### S5. METR. "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity." metr.org, 10 Jul 2025. [V]
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- RCT: 16 experienced open-source developers, 246 real issues (about two hours each) randomly assigned AI-allowed or not; mainly Cursor Pro with Claude 3.5/3.7 Sonnet.
- With AI allowed, developers took 19% longer. They expected a 24% speedup beforehand and still believed afterwards they had been sped up 20%.
- Authors' caveats: snapshot of early-2025 tools, one setting, small sample, not evidence AI slows most developers. The page now says these results are out of date and points to a February 2026 follow-up (not fetched) [U on follow-up content].
- Chapter use: self-reported time savings (as in S1) and measured productivity can diverge. PMs should measure outcomes, not feelings of speed.

### S6. Willison, S. "Context engineering." simonwillison.net, 27 Jun 2025. [V]
URL: https://simonwillison.net/2025/Jun/27/context-engineering/
- Records that Tobi Lutke (Shopify CEO) preferred "context engineering" over prompt engineering, describing it as providing all the context needed for a task to be plausibly solvable; Andrej Karpathy endorsed it, describing it as filling the window with just the right information for the next step. Both originals were social posts [S for their exact wording; cite via Willison].
- Willison's view: the term will stick because its inferred meaning (supplying the right context) matches its intended meaning, whereas "prompt engineering" came to mean typing into a chatbot.

### S7. Mollick, E. "Centaurs and Cyborgs on the Jagged Frontier." One Useful Thing, 16 Sep 2023. Summarizes Dell'Acqua, McFowland, Mollick, Lifshitz-Assaf, Kellogg, Rajendran, Krayer, Candelon and Lakhani, "Navigating the Jagged Technological Frontier," HBS Working Paper 24-013 (2023). [V on Mollick's summary; HBS and SSRN pages returned 403, so paper itself S]
URL: https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged
- 758 BCG consultants (about 7% of its consulting force), 18 realistic consulting tasks plus one task designed to sit outside GPT-4's ability.
- With GPT-4, inside the frontier: 12.2% more tasks, 25.1% faster, 40% higher quality. Outside the frontier: correct 84% of the time without AI versus 60 to 70% with AI.
- Jagged frontier: AI is strong at some tasks and weak at others that look equally hard to humans; you learn where the line is only through use.
- Centaurs divide work cleanly between human and AI; cyborgs interleave at a fine grain. Mollick warns of "falling asleep at the wheel".
- PM application: the jagged frontier is why verification is task-specific. A PM must know which PM tasks sit inside the frontier (drafting, summarizing, reformatting) and which are risky (novel judgment, numbers without sources, claims about specific customers).

### S8. OWASP GenAI Security Project. "OWASP Top 10 for LLM Applications 2025." genai.owasp.org. [V]
URL: https://genai.owasp.org/llm-top-10/
- LLM01 Prompt Injection; LLM02 Sensitive Information Disclosure; LLM03 Supply Chain; LLM04 Data and Model Poisoning; LLM05 Improper Output Handling; LLM06 Excessive Agency; LLM07 System Prompt Leakage; LLM08 Vector and Embedding Weaknesses; LLM09 Misinformation; LLM10 Unbounded Consumption. Release date not stated on the page (2024 v1.1 dated 11 Apr 2024; 2025 translations dated from 12 Mar 2025).
- PM application: the three that bite a PM's own harness most: prompt injection (a customer email or web page read by a connector contains instructions), sensitive information disclosure (pasting customer data into unapproved tools), excessive agency (an agent with send or write permissions acting without review). Misinformation maps to the verification section.

### S9. EU AI Act, Article 4 (AI literacy). artificialintelligenceact.eu. [V on the site; see flag]
URL: https://artificialintelligenceact.eu/article/4/
- Providers and deployers of AI systems must take measures so staff who operate or use AI on their behalf have sufficient AI literacy, considering their knowledge, experience, the context of use and the people affected. Applies from 2 February 2025.
- Flag: the text the site currently shows includes language on Commission and Member State support and AI Board recommendations, which may reflect amendments proposed in the Commission's late-2025 "Digital Omnibus". Confirm the in-force wording before the chapter states the obligation precisely.
- PM application: a product team's AI usage policy and onboarding (artifact 4) is a practical way to show AI literacy measures for EU-facing companies.

### S10. Cagan, M. "Product Coaching and AI." SVPG, 4 Feb 2026. [V]
URL: https://www.svpg.com/product-coaching-and-ai/
- A foundation model, configured with project instructions and the company's strategic context, can act as a personal product coach good enough for most individual contributors; leaders should pair it with a human leadership coach because leadership problems are about people, politics and power.
- Tell the model which operating model you are trying to learn (product model, not project model). Ask it for critique and mistakes, not affirmation.
- Using AI only to speed up project-model work (aggregating requests, generating roadmaps, writing PRDs) exposes theater rather than adding value; an engineer or agent could do those tasks.
- Notes that companies restricting AI tools for security and privacy reasons slows adoption.
- Verbatim: "a foundation model is not a deterministic product."

### S11. Model Context Protocol. "What is the Model Context Protocol (MCP)?" modelcontextprotocol.io, spec revision 2026-07-28, fetched 30 Oct 2026. [V]
URL: https://modelcontextprotocol.io/docs/getting-started/intro
- Open-source standard for connecting AI applications to external systems: data sources, tools and workflows. Analogy on the page: a USB-C port for AI applications.
- Supported by Claude, ChatGPT, VS Code, Cursor and others. MCP Apps extension lets servers render interactive UI inside AI clients.
- Cross-check from ch14 and ch19 notes [V]: current spec revision 2026-07-28; MCP Registry preview launched 8 Sep 2025; MCP security best practices page exists (confused deputy, token passthrough, session hijacking, least privilege scopes).
- PM application: connectors are how a PM's harness reads the backlog, CRM, call recordings, support tickets, analytics and docs without copy-paste. Each connector is also an access grant, so the usage policy must list approved connectors and their scopes (read versus write).

### S12. Schluntz, E. and Zhang, B. "Building effective agents." Anthropic Engineering, 19 Dec 2024. [V]
URL: https://www.anthropic.com/engineering/building-effective-agents
- Workflows: LLMs and tools orchestrated through predefined code paths. Agents: the LLM directs its own process and tool use. (The page shows author first names; full names per byline Erik Schluntz and Barry Zhang [S for surname].)
- Patterns: prompt chaining, routing, parallelization (sectioning, voting), orchestrator-workers, evaluator-optimizer.
- Start with the simplest solution; agents trade latency and cost for performance; many needs are met by one well-built call with retrieval and examples.
- Three principles: simplicity, transparency (show planning steps), careful agent-computer interface (tool documentation and testing).
- PM application: most PM automation should be a workflow (a scheduled weekly digest is prompt chaining) not an open-ended agent. Use evaluator-optimizer for document review: one pass drafts, a second pass critiques against a rubric.

### S13. Matthews, C. "A guide to AI prototyping for product managers." Lenny's Newsletter (guest post), 7 Jan 2025. [V, partial: paywalled after first template]
URL: https://www.lennysnewsletter.com/p/a-guide-to-ai-prototyping-for-product
- Three tool classes: chatbots with canvases (single-page, cannot host); cloud development environments (v0, Bolt, Replit, Lovable) for multi-page prototypes; local developer assistants (Cursor, Copilot, Windsurf) for production code.
- Workflow: pick tool by goal; start from a design screenshot and ask for an exact match, or from a broad prompt using design-system patterns; add features one at a time with specific prompts; test with users before engineering builds.
- Caveats: vague prompts make tools rebuild what exists; expect most time to go to debugging.
- Chapter use: brief cross-reference only (Chapter 4 covers prototyping in depth); in this chapter, prototyping sits on the workflow map as "build to learn".

### S14. Microsoft WorkLab. "2025: The Year the Frontier Firm Is Born" (Work Trend Index). 23 Apr 2025. [V]
URL: https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born
- 31,000 knowledge workers in 31 markets, surveyed 6 Feb to 24 Mar 2025 by Edelman Data x Intelligence; leader survey n = 9,037.
- Concepts: "Frontier Firm" (hybrid teams of humans plus agents); "human-agent ratio" (how many agents per role and how many humans to guide them); "agent boss" (a person who builds, delegates to and manages agents).
- Stats: 82% of leaders say this is a pivotal year to rethink strategy and operations; 24% have deployed AI organization-wide, 12% still in pilot; 81% expect agents moderately or extensively integrated within 12 to 18 months; Microsoft 365 telemetry shows about 275 interruptions a day (every two minutes) during core hours.
- Vendor research: tag as vendor survey in the chapter. PM application: "agent boss" framing for a PM who runs scheduled agents; the interruption figure supports batching AI-assisted triage into a routine.

### S15. Anthropic. "What are projects?" Claude Help Center, fetched 30 Oct 2026. [V]
URL: https://support.claude.com/en/articles/9517075-what-are-projects
- Projects are self-contained workspaces with their own chat history, a knowledge base (uploaded documents, text, code) and project instructions (tone, role, perspective).
- Paid plans switch to retrieval (RAG) mode as knowledge nears the context limit, expanding capacity "by up to 10x" (vendor claim).
- Team and Enterprise: share projects with people or the whole organization, "Can view" or "Can edit".
- A new project version (beta) runs a project as one conversation with parallel cloud threads, rolling out from Claude Code.
- PM application: the product context pack (artifact 3) lives as a shared project; instructions hold the house rules; knowledge holds the Product 360 documents. Equivalent features exist in other harnesses (custom GPTs or ChatGPT projects, Gemini Gems) [U: not fetched; describe generically].

### S16. Anthropic. "Cowork" product page (claude.com), fetched 30 Oct 2026. [V for feature list; no page date]
URL: https://claude.com/blog/cowork-research-preview
- Cowork is Claude's agent for non-coding knowledge work (research, analysis, document creation) that works across chosen folders and connected tools and returns work for review.
- Capabilities listed: works on local files (docx, pdf, xlsx, pptx, csv); connectors (examples Amplitude, Microsoft 365, Slack on Team); scheduled tasks that run daily, weekly or monthly unattended; skills and plugins (plugins bundle skills, connectors and sub-agents); built-in browser; computer use in research preview.
- Controls: user chooses folders and tools; deletion needs approval; with permission settings on it shows its plan and waits for approval before significant actions; Enterprise admin controls, spend limits, tool permissions, activity streaming to a SIEM via OpenTelemetry.
- Page date: the newest dated item is 26 Aug 2026; first launch date of Cowork not confirmed in this session [U: widely reported as a January 2026 research preview; do not state a date without verification].
- Do not print prices in the book (they change).
- PM application: scheduled tasks are the mechanism for the weekly operating routine (Monday metrics digest, Friday competitor scan). Describe the capability generically: "a harness that can run a saved prompt on a schedule with your connectors".

### S17. NIST. "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (NIST AI 600-1). 26 Jul 2024. [V for ID and date]
URL: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- Cross-sectoral companion to the AI RMF. DOI 10.6028/NIST.AI.600-1.

- The 12 GAI risks (section 2, verified from the PDF text): 1 CBRN information or capabilities; 2 Confabulation; 3 Dangerous, violent or hateful content; 4 Data privacy; 5 Environmental impacts; 6 Harmful bias or homogenization; 7 Human-AI configuration (anthropomorphizing, automation bias, over-reliance); 8 Information integrity; 9 Information security; 10 Intellectual property; 11 Obscene, degrading and/or abusive content; 12 Value chain and component integration.
- Confabulation: confidently stated but erroneous or false content (colloquially hallucinations), including outputs that diverge from the input or contradict earlier statements; NIST calls it a natural result of how generative models are designed.
- PM application: the AI usage policy's risk section can map to four of these for PM work: confabulation, data privacy, human-AI configuration (automation bias), intellectual property.

### S18. Anthropic. "Prompt engineering overview." Claude Platform docs, fetched 30 Oct 2026. [V]
URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Before prompt engineering, have (1) clear success criteria, (2) a way to test against them empirically, (3) a first draft prompt.
- Techniques referenced: clarity, examples, XML structuring, role prompting, thinking, prompt chaining (detail on the "Prompting best practices" page, not fetched).
- Not every failing criterion is a prompt problem; latency and cost may be better fixed by model choice.
- PM application: every prompt in the team library carries a "what good looks like" line and two or three test inputs, a lightweight eval. This is the bridge from prompt library to eval discipline (Chapter on AI evals).

### S19. Cagan, M. "Experimentation, AI and the Product Model." SVPG, 21 Oct 2026. [V]
URL: https://www.svpg.com/experimentation-ai-and-the-product-model/
- AI cut the time and cost of building; few companies see matching outcome gains. With building easier, the critical skill is figuring out what to build, which makes experimentation central to discovery. For AI products, evals assess quality early; reserve slower, costlier A/B tests for establishing value.

### S20. Rachitsky, L. "All of the Lenny and Friends Summit talks are now online!" Lenny's Newsletter, 29 Sep 2026. [V for the write-up; speakers' words are as reported]
URL: https://www.lennysnewsletter.com/p/all-of-the-lenny-and-friends-summit
- Section heading (cross-check ch00): "The PM job is expanding, not disappearing."
- Geoff Charles (Ramp): PMs expanding toward GM scope, owning the business outcome.
- Tamar Yehoshua (Atlassian): PM, engineering and design are not collapsing into one "builder"; each role can do much more than before.
- Elena Verna (Lovable): builds prototypes, changes the pricing page and ships to production herself, and runs research and analysis.
- Robby Stein (Google Search): as building gets easier, PM value centers on judgment and taste.
- Katie Dill (Stripe): use AI to "raise the ceiling, not just the floor."
- Ami Vora (Anthropic) and Yehoshua: no single right AI workflow yet; depends on product type and phase.
- Chapter use: supports "what not to delegate" (judgment, taste) and the claim that norms are still forming, so teams should write their own.

### S21. Atlassian. "The State of Teams 2026." Atlassian blog, 27 Apr 2026. [V] (confirms the figure Cagan cites in S2)
URL: https://www.atlassian.com/blog/state-of-teams-2026
- Double-blind survey, Jan to Feb 2026: 12,035 knowledge workers and 173 Fortune 1000 executives, plus 25 Fortune 500 executive interviews.
- 89% of executives say AI increases speed; only 6% are sure they have clear examples of organization-wide AI ROI.
- 85% of knowledge workers use AI at work; only 29% have embedded it in their workflows.
- 87% of knowledge workers lack time or capacity to coordinate when everyone is in execution mode. Only 24% of leaders focus on using AI to improve teamwork. 55% of executives say AI is widening performance gaps between teams.
- The 14% of teams that achieved AI ROI are up to 5.6x more likely to say AI helps them plan and prioritize and 9.4x more likely to say it increases collaboration (vendor survey).
- Chapter use: the "use versus embed" gap (85% vs 29%) is the argument for workflow maps and routines rather than ad hoc chat.

### S22. Anthropic. "How Anthropic teams use Claude Code." claude.com blog, 24 Jul 2025. [V] (vendor self-report)
URL: https://claude.com/blog/how-anthropic-teams-use-claude-code
- Non-engineering examples: product design feeds design files to the agent to write and test feature code, and uses it to map error states and logic flows so edge cases surface before development; growth marketing analyzes CSVs of hundreds of ads with two specialized sub-agents; legal prototyped an internal routing tool.
- Tips: treat the agent as a thought partner rather than a code generator; give it abstract problems, let it work, then review before refining.
- PM application: edge-case mapping is a strong PRD prompt (list error states, empty states, permission states, failure modes).

### S23. Mollick, E. "Making AI Work: Leadership, Lab, and Crowd." One Useful Thing, 22 May 2025. [V]
URL: https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and
- Leadership sets urgency and a concrete picture of AI-enabled work; the Lab (a small central team) builds and tests tools, benchmarks and demos; the Crowd (all employees) learns by use and shares workflows. Experienced workers judge output best.
- "Secret cyborgs": people hide AI use for fear of punishment, loss of respect, layoffs, or higher workloads. Remedies: name zones where experimentation is allowed; default to permitting use where ethical and legal; reassure that disclosed gains will not cost jobs; hands-on practice over prompting tips; leaders model use openly; incentives for transformational uses ("Build incentives, even massive incentives").
- PM application to team adoption: a product org's Lab can be product ops plus one AI-curious PM; the Crowd is every PM sharing prompts in the library; Leadership is the VP of Product modeling use in reviews.

### S24. Anthropic. "Best practices for Claude Code." Claude Code docs, fetched 30 Oct 2026. [V]
URL: https://code.claude.com/docs/en/best-practices
- Deterministic versus non-deterministic instructions: a prompt, memory file or skill is read by the model, which usually but not always follows it; a hook, deny rule or managed setting is enforced by the harness every time. Use the deterministic kind for things that must always or never happen.
- "Brainstorm first": ask the model to interview you until it could write the spec, then write it to a file; start a fresh session to build from that written definition of done.
- Keep the always-loaded memory file short: only what the model cannot work out itself (how to confirm work, misleading places, decisions not written elsewhere, anything corrected twice). Every line costs attention on every task.
- Put team procedures in skills: the model sees name and description always and reads the full file only when needed. Side-effecting skills can be set so only a person can start them.
- "Give Claude a check to run": without a pass or fail check, "looks done" is all it has, and you become the test suite.
- Review against your spec, not in general; tell the reviewer to skip style, because a reviewer asked to find problems always finds something.
- PM translation (for the chapter, generically, without tool click-paths): the interview-me-then-write-a-brief pattern for PRDs; the context pack kept short with the rest in referenced files; recurring PM procedures as skills; verification checks phrased as pass or fail ("every number has a cited source row; every customer quote has a call ID"); reviews against the brief rather than open-ended critique; permissions (read-only connectors) as the deterministic layer of the usage policy.

### Cross-checked from earlier chapter notes (already [V] there)
- Faros AI, "AI Productivity Paradox Report 2025" (23 Jul 2025; telemetry from over 10,000 developers, 1,255 teams): high-AI-adoption teams completed 21% more tasks and merged 98% more PRs, while PR review time rose 91%. (research-ch06.md) Use only as engineering-side context for Cagan's paradox; note the shared phrase "productivity paradox" predates Cagan's essay.
- Cagan, "Build To Learn FAQ" (27 Apr 2026) exists per research-ch07.md; build to learn versus build to earn distinction.
- MCP Registry preview, 8 Sep 2025; MCP security best practices (research-ch14.md, research-ch19.md).


---

## (a) Key concepts and frameworks

1. **The production versus upstream gap** (Segal and Rachitsky, S1). PMs use AI mostly for production work: PRDs 21.5%, mockups 19.8%, communication 18.5%. Discovery and strategy lag: user research 4.7%, roadmap ideas 1.1%. The largest wanted change is user research (+27.2 points). B2B application: the chapter's workflow map should push AI upstream into interview synthesis, win/loss, support-ticket mining and assumption mapping, where enterprise PMs have the most unread evidence.

2. **The AI productivity paradox; build to learn versus build to earn** (Cagan, S2, S19). AI speeds up output; outcomes stay flat when teams use it inside the project model. Use AI first to build to learn (fast prototypes tested with customers and stakeholders for value and viability), then to build to earn (commercial quality). Atlassian's 89% speed versus 6% ROI data (S21) is the evidence he cites. B2B application: a PM's AI time budget should be weighted toward discovery and decision quality, and the PM should measure outcomes, not documents produced.

3. **The jagged frontier; centaurs and cyborgs** (Dell'Acqua, Mollick and colleagues with BCG, S7). Inside the frontier, consultants with GPT-4 were 25.1% faster with 40% higher quality; outside it, correctness fell from 84% to 60 to 70%. Centaurs split tasks; cyborgs interleave. B2B application: map each PM task to inside, edge or outside the frontier and set verification depth to match (artifact 1 column).

4. **Self-report versus measured productivity** (METR, S5). Developers felt 20% faster while measured 19% slower. Application: a team adopting AI should measure cycle time and outcome metrics, not survey sentiment alone. Pair with S1's self-reported savings.

5. **Context engineering** (term popularized by Tobi Lutke and Andrej Karpathy, June 2025, per Willison S6; method from Anthropic's Applied AI team, S3). Curate the smallest set of high-signal context: right-altitude instructions, a few canonical examples, references loaded just in time, notes kept outside the window, sub-agents for side work. Application: **the Product 360 as context**. The book's own artifacts (personas, vision, strategy, metrics tree, decision log, pricing, competitive map) are exactly the high-signal context a harness needs. Keep an always-loaded brief short and point to the full documents.

6. **Workflows versus agents** (Schluntz and Zhang, Anthropic, S12). Workflows follow predefined steps; agents choose their own. Start simple. Patterns: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer. Application: an **automation ladder** for PM work (Product 360 synthesis): (1) one-off prompt, (2) saved prompt in the library, (3) shared project with the context pack, (4) skill that packages procedure plus checks, (5) scheduled task that runs the skill with connectors, (6) agent with write access behind an approval gate. Climb only when the step below is stable and verified.

7. **Skills and the deterministic layer** (Anthropic, S4, S24). Skills are folders with instructions, scripts and resources loaded only when relevant; an open standard since Dec 2025. Instructions in prompts and skills are followed probabilistically; permissions, hooks and admin settings are enforced every time. Application: recurring PM work (weekly metrics narrative, PRD review, release notes, QBR prep) becomes team skills; confidentiality rules that must never fail belong in permissions (read-only connectors, blocked folders), not in a prompt.

8. **Give it a check to run; review against the spec** (Claude Code best practices, S24; Anthropic prompt docs, S18). Define success criteria and tests before tuning prompts. A reviewer told to find problems always finds something, so review against the brief and say what to skip. Application: verification protocol for PM outputs (see artifact 4 and flags) with pass or fail checks: every number traces to a named source; every customer quote has a source ID; every competitor claim has a dated URL; no new commitments appear that the PM did not make.

9. **The interview-me pattern** (S24). Ask the harness to interview you until it could write the brief, then write it; start a fresh session to draft from the brief. Application: PRD and narrative drafting starts from the PM's thinking, not a blank-page generation, which keeps judgment with the PM (Cagan's warning in S10 that AI-written PRDs can be theater).

10. **AI as product coach** (Cagan, S10). Configure the model with company strategic context and the operating model you want to learn; ask for critique, not affirmation. Leaders still need a human coach for people and politics. Application: a "coach me" prompt in the library and a red-team prompt before every review.

11. **Leadership, Lab and Crowd; secret cyborgs** (Mollick, S23). Adoption needs leaders who model use, a small lab that builds and tests, and a crowd that shares what works; hidden use signals fear. Application: team adoption norms: open sharing of prompts, a named product-ops owner for the library, explicit experimentation zones, "AI use is expected and disclosed, not hidden".

12. **Agent boss and human-agent ratio** (Microsoft Work Trend Index, S14). People who build, delegate to and manage agents. Application: a PM who runs scheduled agents owns their outputs as if they were a junior teammate's work.

13. **Risk frames** (OWASP LLM Top 10 2025, S8; NIST AI 600-1, S17; EU AI Act Article 4, S9). For a PM's own harness the material risks are prompt injection via connected content, sensitive information disclosure, excessive agency, misinformation or confabulation, automation bias (NIST "human-AI configuration") and IP. Article 4 requires AI literacy measures for staff of providers and deployers from 2 Feb 2025.

14. **Judgment stays human** (Lenny and Friends Summit speakers, S20; Cagan, S2, S10). Speakers converge on judgment and taste as the PM's core; norms are unsettled ("We don't know the answer", Ami Vora). Application: the "do not delegate" list: decisions and trade-offs; commitments to customers; prioritization calls; relationship moments (escalations, bad news, negotiation, coaching); final say on what ships; anything signed with the PM's name without reading it.

### Artifact skeletons (Product 360 originals, built from the sources above; not attributed to any author)

**1. AI workflow map for a PM.** Columns: PM activity | Frequency | AI role (draft, synthesize, critique, monitor, prototype, none) | Frontier position (inside, edge, outside) | Context needed | Connector or source | Verification check | Human-only step | Automation level (ladder 1 to 6). Rows: discovery synthesis; customer and win/loss calls; PRD and narrative writing; prototyping; metrics review and analysis; competitive monitoring; roadmap and prioritization; stakeholder updates; meeting prep and follow-up; review prep (QBR, exec, launch readiness); release notes and enablement; post-incident or post-launch reviews.

**2. Prompt library entry template.** Name | Owner | Task and when to use | Inputs required (files, connectors) | Context to attach (which context pack sections) | Prompt text with placeholders | Output format | What good looks like (success criteria) | Verification checks (pass or fail) | Known failure modes | Test inputs (2 to 3) | Data classification allowed (public, internal, confidential, restricted) | Version and last reviewed date | Promote to skill? (yes when used weekly by 2+ PMs).

**3. Context pack for a product.** Always-loaded brief (one to two pages): product one-liner; customers and personas; North Star and input metrics with current values and dates; strategy pillars and non-goals; current quarter outcomes; pricing and packaging summary; glossary; house style and banned words; decision rights. Referenced files (loaded when needed): full personas, opportunity tree, roadmap, metrics definitions, competitive map, decision log, recent research summaries, open risks. Rules: date every number; owner per section; review monthly; mark confidentiality per file; nothing restricted in shared projects.

**4. AI usage policy for a product team.** Sections: purpose; approved tools and tiers (enterprise accounts with no training on data); approved connectors with scopes (read versus write); data classes and where each may go; never-enter list (credentials, restricted customer data, unannounced financials, personal data beyond need); verification standard by output type; disclosure (label AI-assisted drafts in reviews; never present synthesized quotes as verbatim); agent and automation rules (approval gates on any send, write or external action; owner per scheduled task; prompt-injection caution for external content); do-not-delegate list; AI literacy onboarding (Article 4); incident reporting for AI mistakes; review cadence.

**5. Weekly AI-assisted operating routine.** Monday: scheduled metrics digest against the context pack, PM writes the "so what" and decisions. Tuesday: discovery synthesis of last week's calls and tickets; update opportunity tree. Wednesday: drafting block (interview-me brief, then draft, then evaluator pass against the brief). Thursday: stakeholder prep (pre-reads, likely objections, red-team). Friday: competitive scan digest, prompt-library upkeep (retire, refine, promote), and a 15-minute review of what AI got wrong this week. Daily: meeting prep and follow-ups drafted by the harness, sent by the PM.

### Prompt seeds for the chapter (to be written out in full)
Discovery: synthesize interview transcripts into themes with quote IDs and counts; contrast what customers said versus did; draft an interview guide that avoids leading questions; mine support tickets for jobs and pains by segment; win/loss pattern extraction. Strategy: red-team my strategy against the four risks; list assumptions and the cheapest test for each; coach me as Cagan-style product coach on this decision. PRDs and narratives: interview me until you can write the brief; draft a six-page narrative from the brief; map edge, error, empty and permission states; review this PRD against the brief and list gaps, skip style. Prototyping: turn this brief into a clickable prototype spec; generate three divergent concepts. Analysis: state the question, the metric definitions and the evidence needed; explain this metric movement with ranked hypotheses and what would disprove each; check this chart's claim against the data. Competitive: weekly diff of competitor release notes, pricing pages and docs with dated links; battlecard update. Stakeholders and meetings: pre-read with likely objections per stakeholder; meeting notes into decisions, owners, dates; draft an exec update in a fixed format; draft bad-news messages for the PM to rewrite. Review prep: QBR pack outline from connected CRM and usage data; launch readiness checklist gaps. Verification: list every factual claim in this draft with its source or "unsourced".

---

## (b) Verified facts (summary list)
- [V] Segal and Rachitsky survey, 23 Dec 2025, n = 1,750; PM uses PRDs 21.5%, mockups 19.8%, communication 18.5%, user research 4.7%, roadmap ideas 1.1%; 63% of PMs save 4+ hours a week; 92.4% of all respondents report at least one significant downside. https://www.lennysnewsletter.com/p/ai-tools-are-overdelivering-results
- [V] Cagan, "The AI Productivity Paradox," 23 Jul 2026. https://www.svpg.com/the-ai-productivity-paradox/
- [V] Atlassian State of Teams 2026 (27 Apr 2026): 89% of execs say AI increases speed; 6% sure of org-wide ROI; 85% of knowledge workers use AI, 29% embedded it. https://www.atlassian.com/blog/state-of-teams-2026
- [V] METR, 10 Jul 2025: 19% slower measured; 20% faster believed. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- [V via Mollick summary, S for paper] BCG jagged frontier study, 2023: 758 consultants; +12.2% tasks, 25.1% faster, 40% higher quality; outside frontier 84% versus 60 to 70% correct. https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged
- [V] Anthropic context engineering, 29 Sep 2025. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- [V] Agent Skills, 16 Oct 2025; open standard 18 Dec 2025. https://claude.com/blog/skills
- [V] MCP described as an open standard for connecting AI apps to external systems; spec revision 2026-07-28. https://modelcontextprotocol.io/docs/getting-started/intro
- [V] Microsoft Work Trend Index, 23 Apr 2025: 31,000 workers, 31 markets; 82% of leaders call it a pivotal year; 81% expect agents integrated in 12 to 18 months. https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born
- [V] NIST AI 600-1, 26 Jul 2024, 12 GAI risks including confabulation and human-AI configuration. https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- [V] OWASP Top 10 for LLM Applications 2025 list. https://genai.owasp.org/llm-top-10/
- [V] EU AI Act Article 4 AI literacy applies from 2 Feb 2025. https://artificialintelligenceact.eu/article/4/

## (c) Quotes (under 15 words)
1. "designed to deliver output, rather than outcomes" (Marty Cagan, The AI Productivity Paradox, SVPG, 2026)
2. "find the smallest set of high-signal tokens" (Anthropic Applied AI team, Effective context engineering for AI agents, 2025)
3. "a foundation model is not a deterministic product." (Marty Cagan, Product Coaching and AI, SVPG, 2026)
4. "The PM job is expanding, not disappearing." (Lenny Rachitsky, Summit write-up, 2026)
5. "raise the ceiling, not just the floor" (Katie Dill, Stripe, as reported in Rachitsky's Summit write-up, 2026)

## (d) 2025 to 2026 developments (verified)
- Feb 2025: EU AI Act Article 4 AI literacy duty applies (S9).
- Apr 2025: Microsoft Work Trend Index introduces "Frontier Firm" and "agent boss" (S14).
- May 2025: Mollick's Leadership, Lab and Crowd adoption model (S23).
- Jun 2025: "context engineering" term spreads (Lutke, Karpathy, via Willison, S6).
- Jul 2025: METR RCT shows measured slowdown versus perceived speedup (S5); Anthropic publishes how its non-engineering teams use agents (S22).
- Sep 2025: Anthropic context engineering guide (S3); MCP Registry preview (cross-check).
- Oct to Dec 2025: Agent Skills launched, then published as an open standard (S4).
- Dec 2025: Segal and Rachitsky survey of 1,750 (S1).
- Feb 2026: Cagan on AI as product coach (S10).
- Apr 2026: Atlassian State of Teams 2026 (S21).
- Jul 2026: Cagan's AI Productivity Paradox (S2); MCP spec revision 2026-07-28 (S11).
- 2026: knowledge-work agents with scheduled tasks, connectors, skills and plugins in mainstream harnesses (S16; launch date unverified).
- Sep 2026: Lenny and Friends Summit themes on judgment and an expanding PM role (S20).
- Oct 2026: Cagan on evals versus A/B tests as building gets cheap (S19).

## (e) Beacon worked example ideas (consistent with beacon-case.md)
- **Beacon context pack**: brief holds the North Star (incidents resolved with Beacon's help per week), input metrics (diagnosis acceptance rate, autonomous resolution rate, MTTR, weekly active responders), personas (Priya, Dana, Marcus, Sam, Leo), ARR about $48M growing 38%, NRR 118%, gross margin 72% after agentic launch, pricing move to per-resolved-incident, the build-on-Observe versus tool-agnostic tension. Referenced files: the post-incident review of the hallucinated root cause, Beacon Classic sunset plan, EU AI Act documentation requests.
- **Workflow map for "You" (Principal PM)**: connectors to call recordings, support tickets, CRM, product analytics and the backlog; a Monday scheduled digest of the five Beacon metrics with "what changed and why" hypotheses; a Friday competitor digest across observability AIOps features, incident tools and ops-agent startups.
- **Discovery synthesis**: 30 customer calls about Beacon Agents' approval gate; the harness clusters concerns by persona (Sam wants audit logs and least privilege; Dana wants a five-minute answer; Leo wants per-tenant views). Verification catches one synthesized "quote" that no transcript contains; the team rule becomes "quotes need a call ID".
- **Echo of the storyline**: the hallucinated root cause in the product mirrors a PM-side near miss: an AI-drafted QBR for a key account stated an MTTR improvement the data did not support. The PM's verification check ("every number traces to a source") caught it before Marcus saw it. Teaches that the PM must apply to their own work the same eval discipline Beacon applies to its agent.
- **Pricing narrative**: interview-me pattern to write the per-resolved-incident pricing brief; evaluator pass against the brief; red-team prompt playing the CFO and an MSP (Leo) on margin.
- **Northlight Live prep**: launch readiness review pack drafted from connected tracker data; PM owns go/no-go.
- **Team adoption**: Beacon's 3 PMs, designer and product ops lead build a shared prompt library; product ops lead is the "Lab"; two recurring prompts (release notes in house style, weekly metrics narrative) promoted to team skills; usage policy forbids pasting customer incident data into unapproved tools and requires read-only connectors to production-adjacent systems, which also satisfies Sam-style reviewers inside Northlight.
- **Do-not-delegate moment**: telling the customer affected by the wrong rollback what happened is done by the PM in person, with AI only helping prepare the timeline.

## (f) Editorial flags
- WebSearch budget was exhausted before this chapter's research; all sources reached by direct URL. Some candidate sources could not be checked: Shopify's Tobi Lutke "reflexive AI usage" memo (April 2025, on X, fetch failed); Mollick's book Co-Intelligence (2024) four rules; Teresa Torres on AI-assisted synthesis; Hilary Gridley's work on team AI adoption (quoted by Cagan). Mention only with verification.
- The BCG jagged frontier figures are verified on Mollick's summary, not the HBS paper (403).
- METR says its July 2025 results are out of date and points to a February 2026 follow-up not fetched here. If cited, note the follow-up exists and do not state its findings.
- Atlassian, Microsoft, Faros and Anthropic customer stories are vendor research; label as such.
- Survey percentages in S1 are self-reported; survey field dates and sampling method not stated.
- EU AI Act Article 4 wording shown on the site may reflect amendment proposals (Digital Omnibus); confirm in-force text before quoting obligations.
- Cowork's launch date and exact scheduled-task behavior: describe capabilities generically; no prices; product names change.
- "Productivity paradox" phrase was used by Faros in 2025 before Cagan's 2026 essay; attribute each use correctly.
- Projects RAG "up to 10x" is a vendor claim; avoid or label.
- Artifact templates and the automation ladder are Product 360 syntheses, not quoted frameworks.
