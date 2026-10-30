# Research notes: Chapter 06, Product Engineering and Execution

Prepared 2026-10-30 for *The Product 360 Handbook* (2026 edition). Audience: Senior to Principal PMs, B2B enterprise and platform products. Notes only; not chapter prose. Maps to eCornell "Product Engineering and Execution" (work with engineering, sprint planning, user stories, issue management).

**Verification key**
- **[V]** Verified this session on the primary source or the author's own site (URL and date given).
- **[S]** Secondary only, or general knowledge consistent across sources. Check before print.

Research note: the session's web search allowance ran out partway through. Later items were verified by fetching primary pages directly; a few attributions below remain [S] for that reason.

---

## Part A. Key concepts and frameworks

### A1. The PM and engineering partnership

- **What good looks like [S, synthesis]:** The PM owns the problem, the outcome and the order of work; engineering owns the solution's design, the estimate and the quality bar; both own the scope trade-off. The Scrum Guide (2020) encodes this split: in Sprint Planning the Product Owner brings the *why* (a Sprint Goal) and proposes the *what*, and the Developers decide the *how* and how much they can take. [V] https://scrumguides.org/scrum-guide.html
- **Card, Conversation, Confirmation (Ron Jeffries, 2001) [V]:** A story is a *card* (a token, just enough text to identify the requirement), a *conversation* (the ongoing exchange between customer and programmers, supported by examples) and a *confirmation* (acceptance tests the customer defines at the start of the iteration, ideally executable). This is the cleanest statement that the written story is not the specification; the conversation is. https://ronjeffries.com/xprog/articles/expcardconversationconfirmation/ (30 Aug 2001)
- **B2B/platform application:** In platform teams the "customer" in the conversation is often an internal or external developer, a partner or a security reviewer. A PM who sends tickets over the wall gets what the ticket says. A PM who joins refinement, brings customer evidence and agrees the confirmation tests gets what the customer needs.
- **Health signals for the partnership (synthesis, use as a checklist, not as research):** engineers can state the customer problem behind their current work; scope changes are negotiated, not dictated; the PM can explain the top three engineering risks; technical debt and reliability work appear on the same roadmap as features; the PM attends demos and reviews and does not only read status.

### A2. Sprint planning, cadence, capacity

- **Scrum Guide 2020 (Ken Schwaber and Jeff Sutherland) [V]:** Sprints are fixed-length events of one month or less. Sprint Planning answers three topics: why is this Sprint valuable (Sprint Goal), what can be done (items selected with the Product Owner), how will the work get done (Developers plan it). Timebox: at most eight hours for a one-month Sprint, shorter for shorter Sprints. The Product Goal is a future state of the product that the team plans against. https://scrumguides.org/scrum-guide.html
- **Capacity (synthesis) [S]:** Plan against available person-days after leave, on-call rotation, support duty and meetings, then reserve explicit allocation for unplanned work, bugs and debt. Common practice is a fixed percentage reserve; there is no authoritative standard percentage, so the book should present it as a team choice informed by the team's own history.
- **Shape Up, appetite (Ryan Singer, Basecamp/37signals) [V]:** An *appetite* is a time budget, not a prediction. An estimate goes from design to a number; an appetite goes from a number to a design. "Fixed time, variable scope." Small-batch work: one designer and one or two programmers for one to two weeks; big-batch: the same team for a six-week cycle. https://basecamp.com/shapeup/1.2-chapter-03 (book year not shown on page; usually cited as 2019 [S])
- **B2B application:** Enterprise PMs often run two clocks: a team cadence (one or two weeks) and a customer-facing release train or quarterly commitment. The PM's job is to keep the Sprint Goal tied to an outcome on the quarterly plan, and to protect capacity for escalations from large accounts so they do not silently eat the plan.

### A3. Estimation: story points versus no estimates

- **Origin of story points (Ron Jeffries, "Story Points Revisited", 23 May 2019) [V]:** XP teams first estimated in time, then in "ideal days" (a pair working without interruption), multiplied by a load factor of about three. Stakeholders found the day numbers confusing, so the team called them points. Points mainly helped decide how much work fit an iteration. Jeffries now calls points a weak basis for forecasting, sees estimate-versus-actual comparison as waste, calls comparing teams by velocity harmful, and prefers slicing stories small and avoiding estimates where possible; teams that find points useful can keep them. https://ronjeffries.com/articles/019-01ff/story-points/Index.html
- **#NoEstimates:** Woody Zuill is credited with the first #NoEstimates tweet in 2012 [S]. Vasco Duarte's book *NoEstimates* recommends: count delivered items against the remaining backlog, forecast from throughput (items per unit of time), manage scope continuously when remaining items exceed forecast capacity, choose high-impact items, plan around a sprint goal without sizing, and treat a budget as a time-and-investment box. [V] InfoQ Q&A by Ben Linders, 7 Dec 2015. https://www.infoq.com/articles/book-review-noestimates
- **Planning Poker [S]:** Named and popularized by Mike Cohn (*Agile Estimating and Planning*, 2005), building on James Grenning's 2002 technique. Not verified this session.
- **How to teach the debate:** Both camps agree on the underlying practice: slice work small and similar in size, then forecast from observed throughput. The disagreement is whether a numeric size per item adds information beyond the count. For a PM, the useful outputs are a probabilistic date range and the scope levers, not the points. In 2026, a PM can ask the AI harness to pull the last N sprints of completed items from the tracker connector and produce a throughput-based forecast range with assumptions stated; no formulas are needed.
- **B2B application:** Enterprise customers and sales ask for dates. Give ranges with confidence and name the scope that moves the date. Commit externally only to what has a buffer; commit internally to the Sprint Goal.

### A4. User stories

- **Template (Connextra, early 2000s; popularized by Mike Cohn) [V]:** "As a [type of user], I [want/need/am required] to [do something], so that [reason or benefit]." Mike Cohn credits Rachel Davies at Connextra, a UK company, in the early 2000s. Cohn's stated advantages: who, what, why in logical order; first person makes it relatable; stakeholders can fill in the blanks; it helps prioritization. https://www.mountaingoatsoftware.com/blog/advantages-of-the-as-a-user-i-want-user-story-template (page updated 22 Apr 2026); https://www.mountaingoatsoftware.com/agile/user-stories
- **Acceptance criteria (Cohn) [V]:** details that show whether a story was completed correctly; can be examples, rules, tests or brief notes; they are the "confirmation" of the three Cs. An **epic** is a large story kept before details are known and split into smaller, finishable stories as it nears development.
- **INVEST (Bill Wake, 17 Aug 2003) [V]:** Independent (no overlap, schedulable in any order); Negotiable (a placeholder for conversation); Valuable (to the customer; slice vertically through all layers); Estimable (enough to rank and schedule); Small (a few person-weeks at most in the original; modern teams aim far smaller); Testable (understood well enough to write a test). Wake pairs it with **SMART tasks**: Specific, Measurable, Achievable, Relevant, Time-boxed. https://xp123.com/invest-in-good-stories-and-smart-tasks/
- **Given-When-Then (Dan North, "Introducing BDD", 2006) [V]:** Template: Given some initial context, When an event occurs, Then ensure some outcomes. North's story template: As a [X], I want [Y], so that [Z]. Example scenario: customer withdraws cash from an account in credit. First published in *Better Software*, March 2006; on dannorth.net 20 Sep 2006. https://dannorth.net/blog/introducing-bdd/
- **Gherkin (Cucumber reference) [V]:** Keywords: Feature, Rule, Example/Scenario, Given, When, Then, And, But, Background, Scenario Outline with Examples. Guidance: three to five steps per example; Given sets a known state (not user interaction); When avoids implementation detail; Then asserts only observable outputs, not internal state; keep Background short (ideally four lines or fewer). https://cucumber.io/docs/gherkin/reference/
- **EARS (Alistair Mavin and colleagues, Rolls-Royce, 2009) [V]:** Easy Approach to Requirements Syntax. Patterns: Ubiquitous "The <system> shall <response>"; Event-driven "When <trigger>, the <system> shall <response>"; State-driven "While <precondition>, the <system> shall <response>"; Unwanted behaviour "If <trigger>, then the <system> shall <response>"; Optional feature "Where <feature is included>, the <system> shall <response>". https://alistairmavin.com/ears/ Relevance in 2026: some agentic coding tools write acceptance criteria in EARS style (Kiro is commonly reported to, [S]; Kiro's docs page only says "structured notation").

**Template to print (user story with acceptance criteria):**

```
Title: <verb phrase>
Story: As a <role in context>, I want <capability>, so that <outcome>.
Context and evidence: <customer quotes, ticket IDs, metric>
Acceptance criteria:
  Scenario: <name>
    Given <known state>
    When <event>
    Then <observable outcome>
  (repeat for edge, error and permission cases)
Non-functional: <latency, audit, data residency, accessibility>
Out of scope: <explicit>
Open questions: <owner, due>
Telemetry: <event that proves use / value>
```

- **B2B application:** Enterprise stories need non-functional and role criteria that consumer stories skip: tenant isolation, RBAC role, audit log entry, API versioning, admin versus end-user path. Write a separate scenario for each permission boundary.

### A5. User story mapping (Jeff Patton)

- **Article (8 Oct 2008) [V]:** "The New User Story Backlog is a Map". Activities across the top (big things users do), user tasks beneath them, arranged left to right in narrative order; the top row is the **backbone**; stories hang below as **ribs** and are prioritized by vertical position; the top slice forms the **walking skeleton**, the smallest end-to-end system, built first. Releases are horizontal swim lanes (often masking tape). Backbone items are not ranked against each other. Critique of the flat backlog: it orders by build sequence and explains poorly what the system does; it hides gaps; prioritizing a hundred items one by one is tedious; splitting epics loses context. https://jpattonassociates.com/the-new-backlog/
- **Earlier origin [V]:** Patton's January 2005 *Better Software* article "How You Slice It" first described the approach. https://jpattonassociates.com/user-story-mapping/
- **Book [S]:** *User Story Mapping*, O'Reilly, 2014. The book's release strategy of opening game, midgame, endgame and the line about minimizing output and maximizing outcome are commonly attributed to it; not verified this session.
- **Template (story map layout):**

```
Users/personas row:   Dana (on-call)        | Priya (SRE lead)       | Sam (security)
Backbone (activities): Get paged -> Understand -> Decide -> Act -> Close and learn
User tasks:            open alert | read diagnosis | approve step | run action | write PIR
------------------- Release 1 (walking skeleton) -------------------
stories...
------------------- Release 2 -------------------
stories...
```

- **B2B application:** Map more than one persona across the same backbone (user, approver, admin, buyer). Many enterprise gaps are in the hand-offs between personas, which a flat backlog hides.

### A6. Definition of Ready and Definition of Done

- **Definition of Done (Scrum Guide 2020) [V]:** a formal description of the state of the Increment when it meets the quality measures required for the product. An item that does not meet it cannot be released or shown at the Sprint Review and returns to the Product Backlog. https://scrumguides.org/scrum-guide.html
- **Definition of Ready [V]:** Not in the Scrum Guide, which says only that items the team can finish within one Sprint are "ready for selection". Agile Alliance glossary: explicit, visible criteria, generally based on INVEST, that a story must meet before entering the iteration; early references in a Scrum Yahoo group in early 2008 and a formal write-up in October 2008; no single originator named. https://www.agilealliance.org/glossary/definition-of-ready/ Attribution to Jeff Sutherland and Systematic is common but [S].
- **Caution (synthesis):** a DoR helps the team push back on vague work; it should not become a stage gate that blocks discovery or collaboration. Keep it short.
- **Template, DoR for a B2B platform team:** problem and evidence linked; acceptance criteria in Given-When-Then; permissions and tenancy cases listed; dependencies named with owner; design attached or "no UI"; telemetry defined; fits in one sprint; security or privacy review need flagged.
- **Template, DoD:** code reviewed (human review of any agent-written code); automated tests pass including acceptance scenarios; behind a flag if not for all customers; docs and release notes drafted; telemetry live; security checks pass; deployed to production (dark if needed); no new P1 bugs open.

### A7. Issue and bug management

- **Severity versus priority [S]:** Severity is the degree of technical impact a defect has on the operation of a system (ISTQB glossary wording as reported by several secondary sources); priority is the business importance or urgency of fixing it. Severity is usually set by QA or engineering; priority by the product owner. Classic examples: a crash in a rarely used admin export (high severity, low priority); a misspelled customer name on the login page (low severity, high priority).
- **Priority scale example (Google Issue Tracker docs) [V]:** P0 addressed immediately, full outage or critical function unavailable with no workaround; P1 addressed quickly, significant impact on many users, painful workaround; P2 reasonable timescale, the default; P3 when able; P4 eventually, polish only. https://developers.google.com/issue-tracker/concepts/issues
- **Bug bar (Microsoft practice) [V]:** Ben Armstrong (Microsoft, 30 Dec 2004) describes a bug bar as a list of requirements a bug must meet to be fixed in a milestone or release (examples: customer reported, application crash, data loss). In triage the question "Does it meet the bar?" ends debate. The bar is low early in a cycle and rises as ship approaches; some teams start the next cycle with a quality milestone to fix deferred bugs. https://learn.microsoft.com/en-us/archive/blogs/virtual_pc_guy/does-it-meet-the-bar Microsoft's security bug bar (SDL) rates vulnerabilities critical, important, moderate, low [S].
- **Error budget as a release policy (Google SRE Workbook, Steven Thurgood, 2018) [V]:** If a service exceeds its error budget over the preceding four weeks, all changes and releases stop except P0 issues and security fixes until it is back within SLO; reliability work is required if a code bug or procedural error caused the overage; disputes go to the CTO. The policy is not a punishment. https://sre.google/workbook/error-budget-policy/
- **SLAs (synthesis):** In B2B, customer-facing support SLAs (response and resolution time by severity) are contractual and owned with support; internal fix SLAs (for example, P1 fix within N days) are a team agreement. Keep them separate and make sure the internal SLA is shorter than the contractual one.
- **Template, bug triage policy (one page):** scope; severity definitions S1 to S4 with examples from this product; priority rule (severity x customer impact x contractual exposure x workaround); triage cadence and attendees (PM, eng lead, QA, support); fix SLAs per priority; bug bar per release phase; escalation path for named enterprise accounts; definition of a regression; reporting (open P1/P2 count, age, escape rate).
- **AI-harness note:** In 2026 a PM can ask the harness, through the tracker and support connectors, for "new bugs this week grouped by suspected root cause, with linked customer tickets and ARR at risk" and get a draft triage agenda. The PM still decides priority; the harness prepares evidence.

### A8. Technical debt as a product decision

- **Ward Cunningham, OOPSLA '92 experience report, "The WyCash Portfolio Management System" [V]:** Shipping first-time code is like going into debt; a little debt speeds development if paid back promptly with a rewrite; every minute on not-quite-right code is interest; the danger is when the debt is not repaid. https://c2.com/doc/oopsla92.html
- **Martin Fowler, "Technical Debt" (rewritten April 2019; page dated 21 May 2019) [V]:** cruft is debt; the extra effort it causes is interest (example: four days on clean code versus six on crufty code, two days of interest). Paying principal pays off only if more work will touch that area. Pay down gradually, starting where change is most frequent; stable code rarely touched can be left alone. https://martinfowler.com/bliki/TechnicalDebt.html
- **Fowler's Technical Debt Quadrant (14 Oct 2009) [V for axes]:** axes reckless versus prudent and deliberate versus inadvertent. Prudent-deliberate: knowingly taken to make a release. Reckless-deliberate: "quick and dirty" because the team thinks it cannot afford clean code. Reckless-inadvertent: a team unaware of good design makes a mess. Prudent-inadvertent: after a year of work the team learns what the design should have been. Diagram captions (commonly quoted: "We don't have time for design", "We must ship now and deal with consequences", "What's layering?", "Now we know how we should have done it") are in an image and are [S]. https://martinfowler.com/bliki/TechnicalDebtQuadrant.html
- **Product framing:** Debt is a portfolio decision: what interest are we paying (slower lead time, incidents, onboarding drag, inability to ship a roadmap item) and where. Use Fowler's "pay where you change" rule to rank items.
- **Template, tech debt register:** ID; area or service; description; quadrant (deliberate/inadvertent, prudent/reckless); interest being paid (evidence: lead time, incidents, escalations, blocked roadmap items); change frequency of the area; principal (effort range); risk if left (security, compliance, scale); proposed fix and slice; owner; decision (pay now, schedule, accept, retire); review date.
- **AI-era wrinkle [S, synthesis]:** coding agents lower the cost of paying principal (refactors, test backfill, migrations) and can also create debt faster (large, plausible, unreviewed changes). Treat agent-written code as debt-prone until reviewed and tested.

### A9. Release planning, feature flags, progressive delivery

- **Feature toggles (Pete Hodgson on martinfowler.com, 9 Oct 2017) [V]:** four categories. Release toggles: short-lived, mostly static, hide unfinished code so trunk can deploy anytime. Experiment toggles: per-user dynamic, last long enough for statistical results. Ops toggles: usually short-lived, some long-lived kill switches, reconfigurable fast during incidents. Permissioning toggles: can last years, per-request entitlement decisions. Toggle debt controls: add a removal task when creating a release toggle; expiry dates; "time bombs" that fail a test after expiry; a cap on active toggles. https://martinfowler.com/articles/feature-toggles.html
- **Progressive delivery (James Governor, RedMonk, coined 2018) [V for 2025 book post]:** The 2025 book *Progressive Delivery* (Governor, Kimberly Harrison, Heidi Waterhouse, Adam Zimman; IT Revolution, 4 Nov 2025 [S on date]) frames the goal as delivering what users need when they need it at the least cost and risk to everyone, with four tenets: Abundance, Automation, Alignment, Autonomy. Techniques implied: cohort rollouts, dark launches, running multiple versions and letting users choose when to migrate. https://redmonk.com/jgovernor/progressive-delivery-the-book-is-here/ (12 Nov 2025). The original 2018 post ("Towards Progressive Delivery", 6 Aug 2018) returned 404; its definition (canaries, flags, blast radius) is [S].
- **Decouple deploy from release (synthesis):** deploy is an engineering event; release is a product and customer event. Flags let the PM choose who sees what, when.
- **Template, release plan (B2B):** release name and outcome; scope in and out; flag names and types; rollout stages (internal, design partners, opt-in beta, percentage or cohort GA, regions); entry and exit criteria per stage (error rate, latency, acceptance metric, support tickets); kill-switch owner; customer communications (release notes, admin notices, deprecation notices); enablement (support, sales, partners); compliance artifacts; rollback plan; date range with confidence.

### A10. DORA metrics as context

- **Current metrics (dora.dev, page dated 5 Jan 2026) [V]:** five software delivery performance metrics. Throughput: change lead time (commit to production), deployment frequency, failed deployment recovery time. Instability: change fail rate (deployments needing immediate intervention), deployment rework rate (unplanned deployments caused by a production incident). Best applied per application or service. https://dora.dev/guides/dora-metrics-four-keys/
- **PM use:** context, not targets. A PM reads them to understand how fast a validated idea can reach customers and how risky each release is. Do not use them to compare teams.

### A11. AI coding agents and the PM in 2026

- **Spec-driven development (SDD):** GitHub's Spec Kit (Den Delimarsky, GitHub Blog, 2 Sep 2025) [V] splits work into Specify (what and why: user journeys, success criteria), Plan (stack, architecture, constraints), Tasks (small, independently testable items) and Implement (agent works through tasks; humans review focused changes). Argument: agents need unambiguous direction; vague prompts force guesses that surface late; the spec is a living document. https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
- **Böckeler's critique (martinfowler.com, 15 Oct 2025) [V]:** three levels: spec-first, spec-anchored, spec-as-source. Concerns: many repetitive markdown files tedious to review; overkill for small changes (a small bug became four stories with 16 acceptance criteria in one tool); agents still ignore instructions; heavy upfront specs fight iteration; spec-as-source may repeat model-driven development's failures plus LLM non-determinism. https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- **Thoughtworks Technology Radar, Nov 2025 [V]:** spec-driven development placed in **Assess**; elaborate and opinionated; doubts that hand-crafted rules for AI scale. https://www.thoughtworks.com/radar/techniques/spec-driven-development
- **Implication for PMs:** the user story, acceptance criteria and DoR are now also agent inputs. Spec quality is a throughput lever: ambiguity that a human engineer would resolve in conversation becomes a wrong implementation at agent speed. The three Cs still apply; the conversation now includes the agent's plan, which the PM and engineer review before code.
- **Review is the new bottleneck:** see Part D (Faros AI, DORA 2025, Anthropic). PM implications: smaller slices (INVEST "Small" matters more), acceptance tests written before implementation, explicit review capacity in sprint planning, and a DoD that requires human review of agent output.

---

## Part B. Verified facts (with URL and date)

1. [V] Ron Jeffries published "Card, Conversation, Confirmation" on 30 Aug 2001. https://ronjeffries.com/xprog/articles/expcardconversationconfirmation/
2. [V] Bill Wake published INVEST on 17 Aug 2003. https://xp123.com/invest-in-good-stories-and-smart-tasks/
3. [V] Mike Cohn credits the "As a... I want... so that" template to Rachel Davies at Connextra (UK), early 2000s. https://www.mountaingoatsoftware.com/blog/advantages-of-the-as-a-user-i-want-user-story-template (updated 22 Apr 2026)
4. [V] Dan North's "Introducing BDD" first appeared in Better Software, March 2006. https://dannorth.net/blog/introducing-bdd/
5. [V] Jeff Patton's "The New User Story Backlog is a Map" is dated 8 Oct 2008; his story mapping approach was first described in a January 2005 Better Software article. https://jpattonassociates.com/the-new-backlog/ ; https://jpattonassociates.com/user-story-mapping/
6. [V] Scrum Guide 2020: Sprints are one month or less; Sprint Planning is timeboxed to eight hours for a one-month Sprint; the guide does not define a Definition of Ready. https://scrumguides.org/scrum-guide.html
7. [V] Agile Alliance: early "definition of ready" references in early 2008, formal write-up October 2008. https://www.agilealliance.org/glossary/definition-of-ready/
8. [V] Cucumber recommends three to five steps per Gherkin example. https://cucumber.io/docs/gherkin/reference/
9. [V] EARS was developed by Alistair Mavin and colleagues at Rolls-Royce, first published 2009. https://alistairmavin.com/ears/
10. [V] Ward Cunningham introduced the debt metaphor in his OOPSLA '92 experience report. https://c2.com/doc/oopsla92.html
11. [V] Fowler's Technical Debt Quadrant was published 14 Oct 2009. https://martinfowler.com/bliki/TechnicalDebtQuadrant.html
12. [V] Pete Hodgson's "Feature Toggles" was published on martinfowler.com 9 Oct 2017 and defines four toggle categories. https://martinfowler.com/articles/feature-toggles.html
13. [V] Google SRE Workbook example error budget policy freezes all changes except P0 and security fixes when the four-week budget is exceeded. https://sre.google/workbook/error-budget-policy/
14. [V] Microsoft "bug bar" described by Ben Armstrong, 30 Dec 2004. https://learn.microsoft.com/en-us/archive/blogs/virtual_pc_guy/does-it-meet-the-bar
15. [V] DORA lists five delivery metrics including deployment rework rate (page dated 5 Jan 2026). https://dora.dev/guides/dora-metrics-four-keys/
16. [V] Ron Jeffries ("Story Points Revisited", 23 May 2019) says he may have invented story points and regrets it. https://ronjeffries.com/articles/019-01ff/story-points/Index.html

---

## Part C. Short quotes (under 15 words)

1. "Shipping first time code is like going into debt." Ward Cunningham, OOPSLA '92. https://c2.com/doc/oopsla92.html
2. A good story "captures the essence, not the details." Bill Wake, 2003. https://xp123.com/invest-in-good-stories-and-smart-tasks/
3. On story points: "If I did, I'm sorry now." Ron Jeffries, 2019. https://ronjeffries.com/articles/019-01ff/story-points/Index.html
4. A flat backlog is "A bag of context-free mulch." Jeff Patton, 2008. https://jpattonassociates.com/the-new-backlog/
5. "intent is the source of truth." Den Delimarsky, GitHub Blog, 2025. https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/

---

## Part D. 2025 to 2026 AI-era developments (verified)

1. **DORA 2025, State of AI-Assisted Software Development** (Google Cloud blog, Nathen Harvey and Derek DeBellis, 23 Sep 2025) [V]: nearly 5,000 respondents plus over 100 hours of qualitative data; 90% use AI at work; over 80% believe it increased productivity; 30% report little or no trust in AI-generated code. AI adoption now has a positive relationship with throughput and product performance (not the case in 2024) but still a negative relationship with delivery stability. Framing: AI is an amplifier of existing strengths and dysfunctions; speed exposes weak downstream controls (tests, version control, fast feedback). https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
2. **DORA AI Capabilities Model** (page updated 25 Nov 2025) [V for existence, S for names]: seven capabilities that amplify AI's benefits. Names as commonly reported: clear and communicated AI stance; healthy data ecosystems; AI-accessible internal data; strong version control practices; working in small batches; user-centric focus; quality internal platforms. Secondary reporting says teams with strong user focus gain from AI while those with poor user focus see performance decline [S]. https://dora.dev/research/ai/ai-capabilities-model
3. **METR RCT, early 2025** (10 Jul 2025) [V]: 16 experienced open-source developers, 246 real issues in their own repos, mainly Cursor Pro with Claude 3.5/3.7 Sonnet. Tasks took 19% longer with AI allowed; developers forecast a 24% speedup and afterwards still believed about 20%. Caveats: small sample, early-2025 tools, specific setting. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
4. **METR update** (24 Feb 2026) [V]: late-2025 follow-up estimates were -18% task time for returning developers (CI -38% to +9%) and -4% for new recruits (CI -15% to +9%), where negative means AI reduced time. METR calls these unreliable because 30% to 50% of developers withheld tasks they would not do without AI, pay was lower, and time tracking breaks with concurrent agents; it believes they are likely a lower bound and that developers are probably more sped up in early 2026, but calls its data very weak evidence of size. https://metr.org/blog/2026-02-24-uplift-update/
5. **Faros AI, AI Productivity Paradox Report 2025** (23 Jul 2025; vendor telemetry, over 10,000 developers, 1,255 teams) [V]: in high-AI-adoption teams, tasks completed +21%, PRs merged +98%, PR review time +91%, PR size +154%, bugs per developer +9%. Later Faros reports (2026, about 22,000 developers) describe longer review cycles and a widening quality gap; specific 2026 figures not verified. https://www.faros.ai/blog/ai-software-engineering ; https://faros.ai/research
6. **Stack Overflow Developer Survey 2025** [V]: 84% use or plan to use AI tools (76% prior year); 33% trust AI accuracy, 46% distrust, 3% highly trust; 66% cite solutions "almost right, but not quite"; 45.2% say debugging AI-generated code takes more time. https://survey.stackoverflow.co/2025/ai
7. **Anthropic, "How AI Is Transforming Work at Anthropic"** (2 Dec 2025) [V]: 132 surveyed engineers and researchers, 53 interviews, 200,000 Claude Code transcripts. Claude used in about 59% of work (28% a year earlier); self-reported productivity gain about 50% (self-report caveat); 27% of Claude-assisted work would not otherwise have been done; consecutive tool calls per transcript rose from 9.8 to 21.2 and human turns fell from 6.2 to 4.1; most can fully delegate only 0 to 20% of their work and delegate easily verifiable, low-stakes tasks. Note for the book: Anthropic makes Claude, so treat as an interested party. https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
8. **Spec-driven development** emerged as a named practice in 2025: GitHub Spec Kit (2 Sep 2025), Kiro specs (requirements.md, design.md, tasks.md; docs updated 15 Oct 2026) [V] https://kiro.dev/docs/specs/ , Böckeler's analysis (15 Oct 2025), Thoughtworks Radar "Assess" (Nov 2025).

**Synthesis for the chapter (not a sourced claim):** the evidence points the same way: code generation got cheaper, while review, verification, integration and stability did not keep pace. For the PM this moves the constraint upstream (clarity of intent, acceptance tests, slice size) and downstream (review capacity, progressive delivery, quality gates). The PM's leverage is spec quality and slicing, not pushing for more output.

---

## Part E. Beacon worked example ideas (consistent with beacon-case.md)

Facts to respect: Beacon is Northlight's AI agent platform for IT ops/SRE; about 35 engineers across 5 teams, 2 applied AI engineers, 3 PMs, 1 designer; you are the newly arrived Principal PM; launch of Beacon Agents (supervised remediation) at Northlight Live; personas Priya, Dana, Marcus, Sam, Leo; hallucinated root cause incident; Beacon Classic sunset; EU AI Act documentation requests; MSP multi-tenancy.

1. **Story map for "Act" (supervised remediation):** backbone across Dana (get paged, read diagnosis, review proposed runbook step, approve, watch outcome, close), Priya (configure allowlist, set approval policy, review audit), Sam (grant least-privilege connector scopes, export audit log). Walking skeleton release for Northlight Live: one action type (rollback of the last deploy) with a human approval gate, audit entry and kill switch. Later slices: restart, scale, autonomous low-risk allowlisted actions, MSP multi-tenant approvals for Leo.
2. **User story with Gherkin acceptance criteria:**
   - Story: As an on-call engineer (Dana), I want to approve or reject Beacon's proposed rollback in one step from the incident view, so that I can restore service without leaving the page.
   - Scenario: Given an incident with a proposed rollback citing a deploy in the last 30 minutes, and Dana holds the "Responder" role, When Dana selects Approve, Then the rollback runs, the incident timeline records who approved and the cited evidence, and Dana sees the result.
   - Scenario (permission): Given Dana lacks the approver role for that service, When she opens the proposal, Then Approve is disabled and the eligible approvers are shown.
   - Scenario (evidence quality): Given the diagnosis cites no deploy or change ticket, When the proposal is generated, Then no rollback is offered.
   - EARS version for the agent spec: "If the diagnosis cites no change event, then Beacon shall not propose a rollback."
3. **Definition of Ready / Done for Beacon Agents:** DoR adds "action risk class assigned" and "eval cases added for this action". DoD adds "audit log entry verified", "kill switch tested", "AI Act documentation field updated", "human review of agent-written code".
4. **Bug triage policy:** the hallucinated root cause that led a customer to roll back the wrong service is classified S1 (safety of production action) and P0 for affected tenants; triggers a bug bar change: any defect that can cause an unapproved or wrongly targeted action meets the bar at every phase. Use the severity versus priority distinction: a cosmetic error in the diagnosis summary for a top-10 account may be low severity but high priority.
5. **Release plan:** Beacon Agents behind release and permissioning toggles; stages: internal dogfood on Northlight Observe's own on-call, five design-partner customers, opt-in beta announced at Northlight Live, GA by region (EU after AI Act documentation is complete). Exit criteria per stage: diagnosis acceptance rate, zero wrong-target actions, approval-to-action latency, support tickets. Ops toggle as global kill switch owned by the on-call engineering lead.
6. **Tech debt register:** Beacon Classic correlation engine (prudent-deliberate debt from the 2024 spin-out) paid down through the sunset; duplicated connector auth code across five teams (reckless-inadvertent); eval harness gaps (interest paid in the hallucination incident). Rank with Fowler's "pay where you change" rule.
7. **AI coding agents at Beacon:** the 35 engineers use coding agents; PR volume rises and review time grows; the PM changes practice: smaller stories, Given-When-Then written before agent implementation, review capacity reserved in sprint planning, and DORA change fail rate watched as the stability signal. Use the harness with tracker and CI connectors to ask: "which merged changes last month lacked acceptance tests, and which incidents followed?"
8. **Estimation debate scene:** Marcus asks for a firm Northlight Live date. The PM gives a throughput-based range from the last eight sprints and names the scope lever (drop "scale" action from the launch slice).

Do not invent new numbers beyond those in beacon-case.md; any sprint or throughput figures in the chapter must be labelled as illustrative.

---

## Part F. Editorial flags

1. **DORA AI Capabilities Model names** are [S]; the primary page did not list them in text. Verify against the report before printing the list.
2. **Fowler quadrant captions** (the four quoted phrases) are in an image; axes and descriptions verified, captions [S].
3. **Progressive delivery 2018 origin post** returned 404; coining by Governor in 2018 is [S]. Book date and ISBN listings disagree [S].
4. **Definition of Ready originator:** commonly credited to Jeff Sutherland and Systematic; Agile Alliance names no originator. Present as "emerged in the Scrum community in 2008".
5. **Planning Poker and Agile Estimating and Planning (Cohn, 2005), User Story Mapping book (2014), Shape Up year (2019)** not verified on primary pages this session.
6. **Severity and priority definitions** attributed to the ISTQB glossary through secondary sources only.
7. **Kiro uses EARS** is commonly reported; Kiro's own docs page says only "structured notation".
8. **METR sign convention** is easy to misreport: METR's 2026 figures are negative time change (faster), and METR itself calls them unreliable. Do not write "AI makes developers 18% faster".
9. **Faros AI** is a vendor analyzing its customers' telemetry; correlational, not causal. Its 2026 figures (for example review-time increases) are unverified.
10. **Anthropic data** is self-reported and from the maker of Claude; label as such.
11. **No standard capacity reserve percentage** exists; present any figure as an example.
12. **#NoEstimates origin** (Zuill, 2012) is [S]; a key secondary page was unreachable.
13. Web search allowance ran out during research; a follow-up session could verify flags 1 to 7.
