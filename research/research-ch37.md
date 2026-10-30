# Research notes: Chapter 37 "Building Your Product 360" (Part X, Capstone)

Status: complete. Researched 2026-10-30. Search budget note: the shared WebSearch budget for this run was exhausted before this chapter started, so all sources were reached by direct WebFetch of known primary URLs, plus the book's own Chapter 00 and Chapter 31 text and the local grilling skill. Fewer secondary sources than other chapters; that is deliberate, not a gap in rigor.

## Internal anchors (from the book itself, do not contradict)

- Chapter 00 defines nine dimensions (Customer, Strategy, Business, Build, Measure, Go-to-market, Operate, Lifecycle, Leadership), three families (Direction, Delivery, Durability) and three artifact kinds (durable, living, event).
- Chapter 00 twelve-artifact spine, in build order: (1) Product 360 index; (2) problem hypothesis and personas; (3) vision and strategy one-pager; (4) competitive landscape; (5) business model and unit economics summary; (6) outcome roadmap now/next/later; (7) North Star and metric tree with dashboard; (8) OKRs; (9) positioning and messaging; (10) operating cadence and decision log; (11) lifecycle stage assessment; (12) stakeholder map and DACI. Chapter 00 says "build these twelve first, in roughly this order" and promises the Capstone "walks through it in a 30/60/90-day plan".
- Chapter 00 six-step method: scope the surface area; inventory; map to nine dimensions (current / stale / contradicted); build the spine; set the cadence; publish and keep alive. The Capstone "expands them into a full 30/60/90-day plan with prompts".
- Chapter 00 AI add-ons (templates in Chapter 31): eval plan (Measure), AI cost model (Business), model and vendor register (Lifecycle), AI risk assessment (Operate). Chapter 31 also has the AI PRD addendum (event artifact). Template ids: eval-plan, ai-cost-model, model-register, ai-risk-assessment, ai-prd-addendum.
- Chapter 00 cadence table: weekly (team sync, metrics review), biweekly (sprint review/planning), monthly (product review, roadmap refresh), quarterly (QBR, OKR reset, portfolio review), annually (strategy refresh), per event (launch readiness, go/no-go, post-launch review, sunset gate). Two rules: every ritual produces a decision or is cancelled; decisions are written down.
- Chapter 00 Beacon case already covers days 1 to 14: scope paragraph, 140-document inventory, the Observe boundary dispute as decision log item 1, ranked gaps (gross margin, North Star, launch plan, Classic lifecycle first; personas and strategy "can wait a month"). By the QBR: index plus twelve linked artifacts (four new, five repaired, three "stale, owner assigned"), six decision log entries, cadence on the calendar. Chapter 37 must continue from this, not restate a different version.
- Chapter 00 already contains prompts: inventory-and-map prompt, draft-the-index prompt, design-a-cadence prompt, contradiction-check prompt. Chapter 37 prompts must go further (grilling) and not duplicate these verbatim; reference them by chapter.
- Chapter 00 says the 360 index must be "readable by machines" and that Chapter 32 covers AI in the work and "the Capstone gives you the prompts".
- Appendix C in book.json: "Product 360 Maturity Model. Score your product's 360 and find the weakest dimension." Chapter 37 should link to it, not define it fully.
- Appendix A (artifact library) and Appendix B (prompt library) are generated from template and prompt blocks, so every Chapter 37 template and prompt should be a proper block with an id.

## Chapter map for cross-references (by number)

Customer: 01, 10. Strategy: 02, 03, 13, 14, 16. Business: 12, 13, 15. Build: 03, 04, 06, 11. Measure: 02, 05, 09, 17, 18, 19. Go-to-market: 24, 25, 26, 27. Operate: 28, 29. Lifecycle: 30. Leadership: 34, 35, 36. AI: 31, 32, 33. Innovation: 20 to 23. Technical PM: 07, 08. Framework: 00.

## (a) Key concepts and frameworks

### A1. Flipped Interaction pattern (Jules White and colleagues, Vanderbilt, 2023)
- Source: White, Fu, Hays, Sandborn, Olea, Gilbert, Elnashar, Spencer-Smith, Schmidt, "A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT", arXiv:2302.11382, submitted 21 Feb 2023. [V]
- Summary: instead of the user driving, the model asks the user questions to reach a stated goal. Motivation: the model often knows better what information is needed and can pick the format, number and content of questions. Structure (paraphrased contextual statements): ask me questions to achieve X; keep asking until a condition is met; optionally ask one at a time. The paper stresses a flipped prompt "should always specify the goal of the interaction" and that the more specific the constraints and information to collect, the better the outcome.
- Related patterns in the same catalog: Persona (model takes a point of view, for example a security reviewer), Question Refinement (model suggests better questions), Cognitive Verifier (model splits a question into sub-questions and combines answers).
- PM application: the grilling session is a Flipped Interaction with three additions the paper does not specify: (1) the harness proposes a recommended answer with each question; (2) it challenges weak answers against explicit tests; (3) it writes answers to a log that later becomes artifacts. Name the lineage, then explain the additions as this book's synthesis.

### A2. "Interview me" before specifying (Anthropic, Claude Code best practices)
- Source: Claude Code docs, "Best practices for Claude Code", code.claude.com/docs/en/best-practices (fetched 2026-10-30; redirected from the older anthropic.com/engineering/claude-code-best-practices). [V]
- Summary: when you have not worked out what you want, ask Claude to interview you until it could write the spec, then write the spec to a file; then start a fresh session to build from that file so the build begins with clean context and a written definition of done. The same page advises putting team procedures in skills (a SKILL.md file loaded only when needed) and writing down only what Claude cannot find on its own.
- PM application: run grilling per dimension, write the result to a grilling log file, then generate artifacts in a fresh session from the log plus reference materials. Package the master grilling prompt as a reusable skill so the cadence can rerun it.

### A3. Grilling skill pattern (practitioner skill, the author's local Claude skill)
- The local "grilling" skill (user's own config, not a published source; do not cite as a publication) encodes the design the user asked for: interview relentlessly, walk each branch of the decision tree resolving dependencies one by one, give a recommended answer for each question, one question at a time, look up facts from the environment rather than asking, and put decisions to the user. Do not act until shared understanding is confirmed.
- Use as the design spec for the master grilling prompt. Distinguish facts (harness looks them up through connectors) from decisions (PM must answer). This distinction is the heart of the chapter's method.
- Editorial flag: a widely shared "grill me" skill attributed to Matt Pocock circulated in 2025 to 2026; could not verify (search budget exhausted). Do not attribute unless verified.

### A4. Sycophancy as the reason the harness must be told to challenge (Sharma et al., Anthropic, 2023)
- Source: Mrinank Sharma and 18 co-authors, "Towards Understanding Sycophancy in Language Models", arXiv:2310.13548, v1 20 Oct 2023, v4 10 May 2025. [V]
- Findings (abstract): five state-of-the-art assistants showed sycophancy across four free-form tasks; in human preference data, responses matching the user's views were more likely to be preferred; humans and preference models sometimes preferred convincing sycophantic answers over correct ones.
- PM application: a grilling session where the harness just agrees is worse than none, because it launders weak answers into confident artifacts. The prompts must give explicit challenge tests (evidence, specificity, falsifiability, trade-off named, owner named) and a rule that the harness may not accept an answer that fails a test without the PM explicitly overriding it, which gets logged.

### A5. Anchoring the harness in reference materials (Anthropic prompting guidance)
- Source: Anthropic, "Prompting best practices" (Claude platform docs, long-context section), platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (fetched 2026-10-30; the old long-context-tips URL redirects here). [V]
- Exact advice: put long documents (20k+ tokens) near the top, above the query and instructions; the page states that queries at the end can improve response quality by up to 30 percent in tests, especially with complex multi-document inputs. Wrap each document in document tags with content and source metadata. For long-document tasks, ask the model to quote the relevant parts first, then do the task.
- PM application for the intake prompt: load reference materials first, each labeled with source, owner and date; instruct the harness to extract quoted evidence per dimension before it summarizes; every claim in the gap list carries a source tag, and "no source" becomes a grilling question rather than an invented answer. Teach it as structure, not syntax: the reader names each document and its date; the harness does the tagging when working through connectors.

### A6. Context engineering and the 360 as persistent memory (Anthropic Applied AI, 2025)
- Source: Rajasekaran, Dixon, Ryan, Hadfield, "Effective context engineering for AI agents", Anthropic Engineering, 29 Sep 2025. [V]
- Summary: context engineering is curating the best set of information the model sees at inference (instructions, tools, external data, history). Techniques: just-in-time retrieval (keep references such as file paths and load on demand), structured note-taking (agent writes notes outside the context window and reads them back), compaction (summarize and restart near the limit). "Context rot": recall degrades gradually as context grows; context is a finite resource with diminishing returns.
- PM application: the grilling log and the Product 360 index are the structured notes. Long grilling sessions should be split by dimension, each ending in a written log entry, rather than one marathon conversation that rots. The maintenance prompt reloads the index and only the artifacts due for review (just in time), not everything.

### A7. Workflow patterns for the prompt suite (Anthropic, Building effective agents)
- Source: Erik Schluntz and Barry Zhang, "Building effective agents", Anthropic, 19 Dec 2024. [V] (page credits "Erik S." and Barry Zhang)
- Prompt chaining: split a task into fixed sequential steps, each call taking the prior output, with checks between steps; trades latency for accuracy. Example given: write an outline, verify it against criteria, then draft.
- Evaluator-optimizer: one call produces, a second critiques against clear criteria, loop until good enough; fits when criteria are clear and human-style feedback would measurably improve the output.
- Advice: keep agent design simple.
- PM application: the chapter's prompt suite is a chain: intake (gap list) then master grilling then per-dimension grilling then artifact generation then consistency audit. The consistency audit is an evaluator-optimizer pass with explicit criteria (the Chapter 00 contradiction tests). Gates between steps are human: the PM approves the gap list before grilling and the log before generation.

### A8. Model Context Protocol (Anthropic, 2024)
- Source: Anthropic, "Introducing the Model Context Protocol", 25 Nov 2024. [V]
- Definition: open standard connecting AI assistants to where data lives (content repositories, business tools, development environments); developers expose data through MCP servers or build MCP clients. Launch pre-built servers: Google Drive, Slack, GitHub, Git, Postgres, Puppeteer.
- PM application: connectors are how the harness looks up facts itself (Chapter 32). In the grilling session, facts that exist in a connected system (ARR, ticket counts, launch dates, roadmap items) are fetched, cited and shown to the PM for confirmation; only judgments are asked.

### A9. Premortem (Gary Klein, 2007)
- Source: Gary Klein, "Performing a Project Premortem", Harvard Business Review, September 2007. [V on author, date and core idea only]
- Core idea: the team assumes the project has just failed and generates plausible reasons why.
- PM application: a grilling move. At the end of each dimension, the harness runs a premortem: "It is 90 days from now and this dimension's artifact misled a decision. What happened?" Also used at day 90 on the whole plan.
- Editorial flag: the commonly cited figure that prospective hindsight increases ability to identify reasons for outcomes by 30 percent (attributed to Mitchell, Russo and Pennington, 1989) was not on the fetched page. Do not use the number unless verified at the primary source.

### A10. Language-model-driven elicitation works (Li, Tamkin, Goodman, Andreas, 2023)
- Source: Belinda Z. Li, Alex Tamkin, Noah Goodman, Jacob Andreas, "Eliciting Human Preferences with Language Models", arXiv:2310.11589, 17 Oct 2023. [V]
- Summary: Generative Active Task Elicitation (GATE) has the model ask the user free-form questions to learn what they want. In preregistered experiments in three domains (email validation, content recommendation, moral reasoning), model-led elicitation often produced more informative responses than user-written prompts or labels; users found it less effortful and it surfaced considerations they had not anticipated.
- PM application: the research basis for grilling rather than "write me a strategy". The PM does not have to know in advance everything the strategy artifact needs; the harness draws it out. Caveat for the chapter: the domains tested were not product strategy, so present it as supporting evidence for the mechanism, not proof that grilling produces better strategy.

### A11. Chain-of-Verification for the consistency audit (Dhuliawala et al., Meta AI, 2023)
- Source: Dhuliawala, Komeili, Xu, Raileanu, Li, Celikyilmaz, Weston, "Chain-of-Verification Reduces Hallucination in Large Language Models", arXiv:2309.11495, Sep 2023. [V]
- Method: draft a response; plan verification questions; answer them independently so the draft does not bias the answers; produce a revised final response. Reduced hallucination on list questions, closed-book QA and long-form generation.
- PM application: the consistency audit and artifact generation prompts should (1) draft, (2) list every factual claim and number, (3) check each against the cited source in a separate pass, (4) mark each claim verified, unsourced or contradicted. Pairs with Chapter 19's "verify the numbers" rule and Chapter 00's contradiction-check prompt.

### A12. Leadership transition model (Michael D. Watkins, The First 90 Days)
- Sources: Wikipedia, Michael D. Watkins (first published 2003 by Harvard Business School Press; second edition 2013, Harvard Business Review Press) [S]; IMD faculty page (book first published 2003, sold over 1.5 million copies, 23 languages; Watkins directs IMD's First 90 Days program; Thinkers50 Hall of Fame 2023) [V on IMD page]; Genesis Advisers "Our approach" page: the Transition Roadmap covers learning, alignment, early wins, coalitions, team building and self-management [V].
- Summary for the chapter: a new leader's job in the first 90 days is to accelerate learning, diagnose the situation, agree on expectations with the boss, secure early wins, build coalitions and the team, and manage themselves. The chapter's 30/60/90 maps onto this: days 1 to 30 learn and diagnose (inventory, intake, listening tour, grilling on facts); days 31 to 60 align and build the spine (grilling on decisions, artifact generation, stakeholder alignment, first early wins); days 61 to 90 run the cadence and prove it (QBR, consistency audit, health review, maturity score).
- B2B/platform application: early wins for a Principal PM are usually decisions unblocked (a scope dispute settled, a pricing question answered with data), not features shipped; 90 days is shorter than most enterprise release cycles.
- Editorial flag: the STARS model (Start-up, Turnaround, Accelerated growth, Realignment, Sustaining success) is widely attributed to the 2013 edition, but no fetched primary page confirmed the five names. Use only if the author can confirm from the book; otherwise describe "match your approach to the situation" generically and attribute to Watkins. Same for "breakeven point" (the point where the new leader's net contribution turns positive): unverified, omit or flag.

### A13. Maturity levels (Watts Humphrey and the SEI Capability Maturity Model)
- Source: Wikipedia, "Capability Maturity Model" [S]: developed at the Software Engineering Institute, Carnegie Mellon, with Watts Humphrey leading from 1986; Humphrey's 1989 book Managing the Software Process; CMM v1.1 published 1993. Five levels: Initial, Repeatable, Defined, Managed, Optimizing.
- PM application: Appendix C's Product 360 maturity model can borrow the shape (five levels per dimension), not the content. A suggested per-dimension scale consistent with Chapter 00 language: 0 Missing; 1 Exists (some artifact, owner unclear); 2 Owned (owner and review date); 3 Current (reviewed on its cadence, cited sources); 4 Used (a ritual makes decisions from it, decision log shows it); 5 Connected (consistent with other artifacts, machine-readable, maintained with the harness). Editorial flag: check Appendix C's actual scale before the chapter quotes levels; the chapter should link, not define.
- Attribute the borrowed shape to Humphrey and the SEI; be clear the Product 360 levels are this book's synthesis.

### A14. Weekly business review mechanics (Amazon, as described by Cedric Chin with Colin Bryar)
- Source: Cedric Chin, "The Amazon Weekly Business Review", Commoncog, 2 Jul 2024 (updated 14 Jun 2026). [S] (secondary account of Amazon practice, informed by former Amazon executive Colin Bryar)
- Summary: a fixed deck of the same graphs and tables each week so people learn what normal looks like; owners say "nothing to see here" for routine variation and explain exceptions or admit they do not know, with follow-up scheduled; output metrics reported but not debated, controllable input metrics are the focus; strategy discussion is taken offline; company meeting about 60 minutes. Framed as a process control tool.
- PM application: the weekly maintenance prompt should produce an exception-only brief (what moved outside normal and why, or "unknown, owner X investigating"), not a full recap. Ties to Chapters 18, 29 and Chapter 00's weekly ritual.

### A15. Socratic question types as the grilling challenge set
- Source: Wikipedia, "Socratic questioning" [S]. Pedagogy section lists six question types (cited there to a UK teaching website the article itself flags as possibly unreliable): clarifying, challenging assumptions, evidence, alternative viewpoints, implications and consequences, questioning the question. Wikipedia cites Richard Paul with Binker (1990) and Paul and Elder (2006, The Thinker's Guide to the Art of Socratic Questioning) for the broader idea that Socratic questioning follows the structure of thinking.
- Editorial flag: do not attribute the six-type list to Richard Paul specifically; the Wikipedia page does not. Present the challenge moves as this book's set, "in the Socratic tradition".
- PM application: the harness's challenge moves map to these. Book's synthesis of seven challenge tests for any grilling answer: (1) Specific: names a segment, number, date or owner, not "customers" or "soon". (2) Evidenced: cites a source, or is labeled an assumption with a test. (3) Falsifiable: says what would prove it wrong (Chapter 01's killable hypothesis). (4) Trade-off named: says what you give up (Chapter 03's strategy kernel). (5) Consistent: does not contradict an earlier answer or an existing artifact. (6) Owned: someone is accountable and a review date exists. (7) Decision-relevant: changes a decision someone will make in the next quarter. An answer failing any test gets one push; on the second failure the harness logs it as an open question with the PM's override reason.

### A16. Persistent instructions and project knowledge as the 360's home in the harness
- Anthropic, "Projects" (claude.ai), 25 Jun 2024 [V]: groups chats with curated knowledge (docs, code, transcripts, past work) and custom instructions; each project had a 200K-token context window at launch, described as equivalent to a 500-page book.
- Claude Code docs, "How Claude remembers your project" [V, fetched 2026-10-30]: each session starts with a fresh context; two mechanisms carry knowledge across sessions: CLAUDE.md files (instructions you write; project, user or org scope; AGENTS.md also read) and auto memory (notes Claude writes from corrections; first 200 lines or 25KB loaded each session). Both are treated as context, not enforced configuration.
- Agent Skills (Anthropic, 16 Oct 2025; updated 18 Dec 2025) [V]: folders of instructions, scripts and resources Claude loads only when relevant; work in Claude apps, Claude Code, Agent SDK and API. (Already covered in Chapters 28 and 32 notes; Chapter 37 should reference Chapter 32 rather than re-explain.)
- PM application, tool-neutral: set up a "Product 360 workspace" in whatever harness the reader uses: (1) standing instructions (the product scope paragraph, the nine dimensions, the challenge tests, the no-invention rule), (2) project knowledge (the 360 index and spine artifacts, read through connectors where possible), (3) the grilling prompts saved as reusable skills or saved prompts. Avoid click-paths.

### A17. The author's own grilling-file precedent (internal)
- The project root has GRILL.md, the planning session for this book: every question has a recommended answer and a "Your answer" line; untouched answers are treated as accepted; the author's answer to the capstone question is the request for these prompts. This is an asynchronous variant of grilling (written questionnaire) versus the live one-question-at-a-time variant.
- Chapter idea: offer both modes. Live mode (one question at a time, conversation) for judgment-heavy dimensions (strategy, business, leadership). File mode (harness writes all questions with recommended answers to a document; PM edits; harness ingests) for fact-heavy dimensions or when stakeholders must contribute (for example, sending the go-to-market questions to the PMM). Editorial flag: ask the author whether to mention that the book itself was planned this way; it is true but personal.

## Synthesis for the chapter (book's own frameworks, label as synthesis)

### S1. The four-stage loop: Anchor, Grill, Generate, Audit (then Maintain)
1. Anchor (intake): load reference materials and connectors; harness inventories, maps to nine dimensions, extracts quoted evidence and produces a gap list split into facts missing (go fetch or ask an owner) and decisions missing (grill the PM). Builds on Chapter 00's inventory prompt.
2. Grill: master prompt sets rules; per-dimension prompts run one dimension per session; each ends with a premortem and a log entry.
3. Generate: artifact prompt turns log plus evidence into the book's templates, every claim tagged with its source (log entry ID or document), unsourced items left as visible gaps.
4. Audit: consistency audit (evaluator-optimizer plus Chain-of-Verification): cross-artifact contradictions, unsourced numbers, stale dates, spine coverage.
5. Maintain: weekly exception brief, monthly roadmap check, quarterly re-grill of living artifacts, annual re-grill of durable ones.

### S2. Grilling session rules (master prompt design spec)
- State the goal and the stop condition up front (Flipped Interaction).
- One question at a time; each with the harness's recommended answer and the reason, drawn from the evidence where possible (local grilling skill; GATE).
- Facts versus decisions: never ask what a connected source can answer; fetch it, cite it, ask the PM to confirm. Ask only for judgments, priorities and trade-offs.
- Walk the decision tree in dependency order: scope before customer, customer before strategy, strategy before roadmap and pricing, North Star before OKRs.
- Challenge with the seven tests (A15); one push, then log as open with override reason. Explicitly instruct against agreeing for its own sake (sycophancy, A4).
- Keep a running log: question ID, dimension, question, recommended answer, PM answer, evidence cited, challenge raised, status (agreed, overridden, open, needs owner), linked artifact, date.
- End each dimension with a short summary readback, a premortem question and confirmation before moving on.
- Pace: 20 to 40 questions per dimension is a reasonable target (synthesis, not a researched number); 45 to 90 minutes per session; split sessions to avoid context rot (A6).

### S3. Per-dimension grilling question banks (seed questions; harness extends)
- Customer (Ch 01, 10): who is the buyer, user, champion, gatekeeper; the job and the current alternative; which persona we would disappoint; evidence from the last 10 customer conversations.
- Strategy (Ch 02, 03, 13, 14, 16, 20): diagnosis in one sentence; where we play and will not; how we win; what competitors would have to do to beat us; platform or product; moat.
- Business (Ch 12, 13, 15): how we make money; unit economics; pricing metric and its link to value; margin trend; what would make the business case false.
- Build (Ch 03, 04, 06, 11, 07): now/next/later and why; what we stopped; delivery model; tech debt bets; dependencies.
- Measure (Ch 02, 05, 08, 09, 17, 18, 19): North Star and why it reflects customer value; input metrics we can move; the decision each metric informs; data trust gaps.
- Go-to-market (Ch 24 to 27): positioning statement, category, proof; launch tiers; enablement; feedback loop from sales and CS.
- Operate (Ch 28, 29): cadence, decision rights, risk register, what rituals produce decisions.
- Lifecycle (Ch 30): stage per offering; sunset candidates; migration obligations.
- Leadership (Ch 34, 35, 36): stakeholder map; who can say no; DACI for the top three decisions; communication plan.
- AI (Ch 31, 32, 33): eval plan and current scores; cost per task trend; model register and deprecation dates; risk assessment and regulatory duties; how the team uses the harness.
- Innovation (Ch 20 to 23) folds into Strategy: innovation portfolio balance; Horizon placement.

### S4. Artifact build order (30/60/90)
- Days 1 to 30 (Learn and anchor): scope paragraph; intake gap list; Product 360 index (spine 1); stakeholder map and DACI draft (spine 12, because you need to know whom to grill); listening tour; urgent event artifacts that have deadlines; facts-only grilling. Early decision win.
- Days 31 to 60 (Decide and build the spine): grill and generate spine 2 to 9 in dependency order: problem hypothesis and personas; vision and strategy one-pager; competitive landscape; business model and unit economics; North Star and metric tree; OKRs; outcome roadmap; positioning. AI four for an AI product: eval plan, AI cost model, model register, AI risk assessment (Ch 31). Consistency audit at day 60.
- Days 61 to 90 (Operate and prove): operating cadence and decision log (spine 10) running for at least four weekly cycles; lifecycle stage assessment (spine 11); event artifacts as the calendar demands (PRD, PRFAQ, launch plan, sunset plan, AI PRD addendum); first QBR on the 360; Product 360 health review; maturity self-assessment against Appendix C; plan for next quarter.
- Rule from Chapter 00 still holds: urgency can reorder (Beacon did business model, North Star, launch plan and Classic lifecycle first). The order above is the dependency default; the gap list's business risk decides the actual order. Note: Chapter 00 lists cadence and decision log as spine 10 but Beacon opened a decision log in week 1; the chapter should say the log starts on day 1 and the full cadence is formalized by day 90.

## (b) Verified facts (with URL and date)

- [V] White et al., "A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT", arXiv:2302.11382, 21 Feb 2023; Flipped Interaction pattern defined there. https://arxiv.org/abs/2302.11382
- [V] Claude Code docs recommend asking Claude to interview you until it could write the spec, then building in a fresh session from the written spec. https://code.claude.com/docs/en/best-practices (fetched 2026-10-30)
- [V] Sharma et al., "Towards Understanding Sycophancy in Language Models", arXiv:2310.13548, Oct 2023 (v4 May 2025): five assistants showed sycophancy; preference data favored responses matching user views. https://arxiv.org/abs/2310.13548
- [V] Li, Tamkin, Goodman, Andreas, "Eliciting Human Preferences with Language Models", arXiv:2310.11589, Oct 2023: LM-led elicitation often more informative than user-written prompts or labels, less effortful. https://arxiv.org/abs/2310.11589
- [V] Dhuliawala et al., "Chain-of-Verification Reduces Hallucination in Large Language Models", arXiv:2309.11495, Sep 2023. https://arxiv.org/abs/2309.11495
- [V] Anthropic prompting docs: long documents at the top; queries at the end can improve response quality by up to 30 percent in tests; wrap documents with source metadata; quote relevant parts first. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (fetched 2026-10-30)
- [V] Anthropic, "Effective context engineering for AI agents", 29 Sep 2025. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- [V] Anthropic, "Building effective agents", 19 Dec 2024 (prompt chaining, evaluator-optimizer). https://www.anthropic.com/research/building-effective-agents
- [V] Anthropic introduced MCP on 25 Nov 2024. https://www.anthropic.com/news/model-context-protocol
- [V] Linux Foundation formed the Agentic AI Foundation on 9 Dec 2025 with MCP (from Anthropic), goose (Block) and AGENTS.md (OpenAI). https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
- [V] MCP specification current version as of 2026-10-30 is dated 2026-07-28; servers offer resources, prompts and tools; clients may offer elicitation (server-initiated requests for more information from users); spec principles require explicit user consent for data access and tool calls. https://modelcontextprotocol.io/specification/latest
- [V] Agent Skills announced 16 Oct 2025, updated 18 Dec 2025. https://claude.com/blog/skills
- [V] Claude Projects launched 25 Jun 2024 with project knowledge and custom instructions. https://www.anthropic.com/news/projects
- [V] Claude Code memory: CLAUDE.md and auto memory carry knowledge across sessions. https://code.claude.com/docs/en/memory (fetched 2026-10-30)
- [V] Gary Klein, "Performing a Project Premortem", HBR, Sep 2007. https://hbr.org/2007/09/performing-a-project-premortem
- [V] The First 90 Days first published 2003; Watkins is at IMD; book sold over 1.5 million copies in 23 languages (IMD page). https://www.imd.org/faculty/professors/michael-watkins/
- [S] Second edition 2013 (Harvard Business Review Press). https://en.wikipedia.org/wiki/Michael_D._Watkins
- [V] Genesis Advisers describe the First 90 Days Transition Roadmap: learning, alignment, early wins, coalitions, team building, self-management. https://genesisadvisers.com/our-difference/our-approach/
- [S] CMM: SEI at Carnegie Mellon, Watts Humphrey from 1986, v1.1 in 1993, five levels Initial, Repeatable, Defined, Managed, Optimizing. https://en.wikipedia.org/wiki/Capability_Maturity_Model
- [S] Amazon WBR mechanics (Cedric Chin with Colin Bryar). https://commoncog.com/the-amazon-weekly-business-review/

## (c) Quotes (under 15 words)

1. Flipped interaction prompt "should always specify the goal of the interaction." White et al., 2023, arXiv:2302.11382.
2. Context is a "finite resource with diminishing marginal returns." Anthropic Applied AI, Effective context engineering, 2025.
3. "Maintain simplicity in your agent's design." Schluntz and Zhang, Building effective agents, Anthropic, 2024.
4. Model-led elicitation can "elicit responses that are often more informative than user-written prompts or labels." Li et al., 2023 (13 words; trim to "often more informative than user-written prompts or labels" if tight).
5. Teams "assume that the project they are planning has just failed." Klein, HBR, 2007.

## (d) 2025 to 2026 AI-era developments (verified)

- Context engineering as a named discipline (Anthropic, Sep 2025): long grilling sessions degrade; persist to notes; split sessions.
- Agent Skills (Oct 2025, open standard Dec 2025 per Chapter 32 notes): the master grilling prompt and maintenance prompt can be packaged as reusable skills so every PM in a portfolio runs the same session.
- MCP moved to vendor-neutral governance under the Linux Foundation's Agentic AI Foundation (Dec 2025); AGENTS.md (OpenAI, Aug 2025) also contributed. Implication: the "any harness" framing is realistic; connectors are not tied to one vendor.
- MCP spec 2026-07-28 includes elicitation (servers can ask the user for information mid-task) and extensions such as Skills over MCP and MCP Apps. Implication: grilling-style question flows are becoming a protocol-level pattern, not just a prompt trick. Keep this light; no protocol detail in the chapter.
- Claude Code best practices (2026 docs): "interview me until you could write the spec" is now first-party advice, which validates the grilling-then-generate split.
- Sycophancy remains a known failure mode (Sharma et al. revised May 2025). Editorial flag: OpenAI rolled back a GPT-4o update in April 2025 for sycophancy; page returned 403, unverified, do not use without verification.

## (e) Beacon worked example ideas (consistent with beacon-case.md and Chapter 00)

Continuity: Chapter 00 covered weeks 1 to 2 (scope, 140-document inventory, Observe boundary dispute logged, four urgent artifacts, by the QBR twelve linked artifacts with three "stale, owner assigned"). Chapter 37 should replay the full 90 days at a higher level and show the grilling in action, without contradicting those facts. Suggest framing: Chapter 00 showed the inventory; Chapter 37 shows how the twelve were actually built and kept alive. Check whether "the QBR" in Chapter 00 is at about day 14 (manager gave two weeks) or day 90; the chapter must reconcile (suggest: Chapter 00's QBR is the first one at roughly day 14 to 30; Chapter 37's day-90 QBR is the second, or reword to "the next portfolio review").

Days 1 to 30:
- Intake: connectors to the doc wiki, ticketing (roadmap), CRM, analytics and the FP&A model export. Gap list shows facts missing (current autonomous resolution rate by segment; inference cost per resolved incident) and decisions missing (North Star definition, pricing metric, Observe boundary, Classic end-of-life date).
- First grilling session: Business. Sample exchange: harness asks "What gross margin must Beacon Agents reach for the per-resolved-incident price to be viable?", recommends a target with reasoning from the FP&A export, PM answers "back to 80%", harness challenges: 81% was the pre-agent level; what inference cost per incident does 80% imply, and is there evidence it is reachable? Logged as open, owner applied AI lead, with a premortem note: "the price launches at Northlight Live and margin falls further".
- Stakeholder map early: Priya (champion), Dana (user), Marcus (buyer), Sam (gatekeeper), Leo (MSP partner), plus internal: VP of Product, Observe group PM, PMM, product ops lead. DACI for the Observe boundary decision; the VP of Product as approver.
- Early win: the Observe boundary settled with a recorded decision (avoid inventing the outcome? choose one consistent with the "strategic tension"; suggestion: correlation stays a shared capability, Beacon owns diagnosis and action; flag as author's choice).

Days 31 to 60:
- Grill Customer: personas updated to add Marcus and Sam (Chapter 00 said missing). Challenge: PM says "SRE teams" are the customer; harness pushes for the buyer and the MSP channel (Leo).
- Grill Measure: North Star "incidents resolved with Beacon's help per week" (beacon-case). Harness challenges whether "with Beacon's help" is defined (accepted diagnosis? executed action?) and links to diagnosis acceptance rate and autonomous resolution rate as inputs.
- Grill AI: the hallucinated root-cause incident (customer rolled back the wrong service) used as a premortem anchor for the eval plan and AI risk assessment; Sam's needs drive audit-log and least-privilege items; EU customers' AI Act documentation request goes into the AI risk assessment (Chapter 33).
- Generate artifacts; day-60 consistency audit finds, for example, the positioning draft promises "autonomous remediation" while the AI risk assessment allows autonomy only for allowlisted low-risk actions; the roadmap shows a Classic feature investment that contradicts the lifecycle assessment. Each becomes a decision log entry.

Days 61 to 90:
- Cadence running: weekly exception brief (WBR style) on North Star, MTTR, diagnosis acceptance rate, autonomous resolution rate, weekly active responders, inference cost per incident; monthly roadmap refresh; quarterly QBR. Maintenance prompt drafts the weekly brief from connectors; PM verifies numbers.
- Beacon Agents launch at Northlight Live: launch plan, PRFAQ, readiness checklist (event artifacts).
- Beacon Classic sunset plan and migration (Chapter 30).
- Day 90: Product 360 health review: per dimension, state, last reviewed, open grilling items; maturity self-assessment showing, for example, Measure and Business at "Used", Leadership at "Owned", Lifecycle at "Exists"; weakest dimension chosen as next quarter's focus. Use only fictional numbers from beacon-case ($48M ARR, 38% growth, 420 customers, 81% to 72% margin, NRR 118%). Do not invent new metrics values beyond those without labeling them illustrative.

## Artifacts to build (template ideas)

1. 30/60/90 plan: header (product, scope paragraph, start date, manager, reviewers); for each phase: goals, artifacts to deliver (spine numbers), grilling sessions scheduled, stakeholders to meet, decisions to land, early win, exit criteria, risks; a "what I will not do in the first 90 days" list.
2. Product 360 build tracker: one row per artifact (12 spine plus AI four plus active event artifacts): number, artifact, dimension, kind, chapter/template id, source materials, grilling session ID, owner, status (not started, grilling, drafted, audited, published), last reviewed, next review, open questions count.
3. Grilling session log: header (product, dimension, date, participants, reference materials loaded with dates); rows: Q-ID, question, harness recommendation and reason, answer, evidence (doc or connector source), challenge raised (which test), status (agreed / overridden with reason / open / needs owner), feeds artifact; footer: premortem answer, summary readback confirmed (Y/N), next session.
4. Product 360 health review: per dimension: artifact, owner, last reviewed, freshness (current / stale / contradicted), maturity level (link to Appendix C scale), open grilling items, contradictions from last audit, decision needed; summary: weakest dimension, top three fixes, cadence health (rituals held, decisions produced), AI artifacts health (eval scores trend, cost per task trend, model deprecations due).

## Prompt suite (design list for the chapter; each needs Goal / Paste in / prompt / Check the output)

1. Set up the Product 360 workspace (standing instructions).
2. Intake: ingest reference materials and produce a gap list (facts vs decisions, quoted evidence, sources and dates).
3. Master grilling prompt (rules, order, challenge tests, log format, stop condition, file mode option).
4. Per-dimension prompts: Customer, Strategy, Business, Build, Measure, Go-to-market, Operate, Lifecycle, Leadership, AI (each with chapter refs, seed questions, required outputs, dimension-specific challenges).
5. Premortem close for each session.
6. Artifact generation: log plus evidence into a named template from the book; every claim tagged; unsourced items left as gaps; no new facts.
7. Consistency audit (cross-artifact, Chain-of-Verification on numbers, freshness, spine coverage).
8. Maintenance prompts: weekly exception brief; monthly roadmap check; quarterly re-grill of living artifacts; annual re-grill of durable artifacts; event trigger (new launch or sunset).
9. Health review and maturity self-assessment draft (against Appendix C).
10. File-mode grilling questionnaire for stakeholders (send to PMM, finance, engineering lead).
Each prompt touching customer or confidential data must remind the reader to use an approved tool (AUTHORING.md).

## (f) Editorial flags

- Search budget was exhausted for this run; no WebSearch performed. All sources reached by direct fetch of known URLs. A follow-up pass could add PM-specific onboarding sources (for example, practitioner 30/60/90 guides), but none are required for the chapter's claims.
- STARS model names and "breakeven point" (Watkins) not verified on a primary page; use only if confirmed.
- The premortem "30 percent" prospective hindsight figure not verified; omit.
- A "grill me" skill attributed to Matt Pocock not verified; omit attribution.
- OpenAI GPT-4o sycophancy rollback (April 2025) not verified (403); omit or verify.
- Six Socratic question types: Wikipedia sources them to a flagged-unreliable website; do not attribute to Richard Paul.
- Question counts per dimension (20 to 40) and session lengths are the book's synthesis, not researched numbers; present as guidance.
- GATE evidence comes from non-PM domains; present as mechanism support only.
- Appendix C's actual scale must be checked before Chapter 37 cites level names; the five-level scale in A13 is a suggestion.
- Chapter 00 timeline reconciliation (QBR at about two weeks versus day 90) must be resolved; see (e).
- Observe boundary outcome is the author's choice; not fixed in beacon-case.md.
- Whether to mention that this book was itself planned with a grilling file (GRILL.md) is the author's call.
