# Research notes: Chapter 11, Delivery Methodologies

Researched 2026-10-30. Part II. Tags: [V] verified on the primary source, [S] secondary only, [U] unverified or from memory. Web search budget ran out late in the session; remaining gaps are listed in section (f).

Scope reminder: maps to the eCornell course on project methodologies for technical products (Agile, Scrum, Kanban, RICE, consumer behaviour applied to pricing signals). Pricing gets one short section that points to Chapters 12 and 15. Artifacts to build: methodology selection guide, team working agreement, RICE scoring sheet, cycle or sprint review template, process health check.

## (a) Key concepts and frameworks

### 1. Waterfall (plan-driven, phase-gated delivery)

- **Origin and the Royce misreading.** Winston Royce's 1970 paper "Managing the Development of Large Software Systems" is the usual citation for waterfall. Royce drew the sequential model, then called it risky and argued for iteration (Wikipedia summarises his advice as running the process at least twice). David Wheeler and the BCS both argue the field adopted the diagram and ignored the warning. Whether the model's popularity was caused by misreading or by other forces (contracting, defence procurement) is debated. Teach this as a paraphrase, not a quote. [S]
- **What it is.** Sequential phases (requirements, design, build, test, deploy) with sign-off gates. Scope is fixed early; time and cost are estimated from scope.
- **When it still fits for a B2B or platform PM in 2026.**
  - Work in an ordered domain in Snowden's Cynefin sense: cause and effect are known or discoverable by analysis (for example, a regulated data-residency migration with a known target state).
  - External fixed dates and fixed scope that are not yours to move: a contractual deliverable for a strategic account, a certification audit, a compliance deadline such as EU AI Act documentation.
  - Hardware, firmware or partner integrations with long lead times where changing direction late is very expensive.
  - Even then, run the build inside the gate in small increments. "Waterfall at the contract level, iterative inside" is the common enterprise pattern. [author synthesis]
- **When it fails.** Complex domains (Cynefin: you can only understand by interacting with the system), new AI features whose behaviour is not knowable until you test them on real data, and any product where the main risk is value rather than execution.

### 2. The Agile Manifesto (2001)

- 17 signatories, February 2001 (Beck, Beedle, van Bennekum, Cockburn, Cunningham, Fowler, Grenning, Highsmith, Hunt, Jeffries, Kern, Marick, Martin, Mellor, Schwaber, Sutherland, Thomas). [V]
- Four values, paraphrase for the chapter: people and interactions over process and tools; working software over exhaustive documentation; customer collaboration over contract negotiation; responding to change over following a plan. The closing line matters: the items on the right still have value, the left are valued more. [V]
- B2B application: the "contract negotiation" value is the hardest in enterprise sales, where SOWs and roadmap commitments exist. The PM's job is to turn commitments into outcomes and dates with explicit uncertainty, not feature lists.
- Martin Fowler (2018) named the "Agile Industrial Complex" that imposes process on teams, and called for teams to choose their own process, for technical excellence, and for products over projects (long-lived teams). Good framing for the chapter's thesis: method is a team decision bounded by organisational needs. [V]

### 3. Scrum (Scrum Guide 2020, Schwaber and Sutherland)

- Definition: a lightweight framework that helps people, teams and organisations generate value through adaptive solutions for complex problems. Built on empiricism and lean thinking. [V]
- **Template: 3-5-3 summary for the chapter.**
  - Accountabilities (2020 changed "roles" to "accountabilities"): Product Owner, Scrum Master, Developers. One Scrum Team, no sub-teams or hierarchies, typically 10 or fewer people. [V]
  - Events: the Sprint (fixed length, one month or less, container for the rest), Sprint Planning (max 8 hours for a one-month Sprint), Daily Scrum (15 minutes), Sprint Review (max 4 hours), Sprint Retrospective (max 3 hours). Shorter Sprints, shorter events. [V]
  - Artifacts and their commitments: Product Backlog with the Product Goal; Sprint Backlog with the Sprint Goal; Increment with the Definition of Done. [V]
  - Pillars: transparency, inspection, adaptation. Values: commitment, focus, openness, respect, courage. [V]
  - Large teams split into multiple cohesive Scrum Teams sharing one Product Goal, one Product Backlog and one Product Owner. [V]
- **Product Owner vs product manager.** The Scrum Guide makes the PO accountable for maximising value, the Product Goal and ordering the backlog; the PO is one person, not a committee, and may delegate the work but keeps accountability. [V] Marty Cagan (2011) argues against splitting an outward-facing "product manager" from an inward-facing backlog "product owner": nobody owns the product, the two roles misunderstand each other, and good backlog decisions require deep customer knowledge. [V] Teaching point: PO is an accountability inside one framework; product management is a job that includes it plus discovery, strategy, pricing, go-to-market and stakeholder work. In large B2B organisations a "technical PO" often owns a platform team's backlog under a PM; the chapter should name the risk (proxy without customer contact) and the mitigation (PO joins customer calls, owns outcomes, not just tickets).
- **Scrum Guide Expansion Pack (2025).** Sutherland, John Coleman and Ralph Jocham published optional guidance alongside the 2020 Guide, including expansions on product thinking, strategy, and "AI and Scrum" (keep outcomes, quality and learning in control so that speed produces value rather than faster failure). The 2020 Guide remains the definition. [V partial; release month S]
- B2B application: Sprint Review is the PM's best customer-evidence forum. Invite a design partner or a customer success manager; show the increment against the Sprint Goal and the outcome metric, not a list of tickets.

### 4. Kanban (Kanban Guide, Vacanti, Coleman and others)

- Current edition v2025.5 (May 2025). Kanban is a strategy for optimising the flow of value through a process. [V]
- Three practices: define and visualise the workflow (the Definition of Workflow, DoW); actively manage items (control WIP, prevent unnecessary ageing, unblock); improve the workflow. [V]
- **Four required flow metrics (exact definitions to teach):**
  - WIP: items started but not finished.
  - Throughput: count of items finished per unit of time.
  - Work Item Age: time from start to now for unfinished items (leading indicator).
  - Cycle Time: time from start to finish for finished items (lagging indicator). [V]
- **Service Level Expectation (SLE):** a period plus a probability, for example "85% of items finish in eight days or less", based on historical cycle time, best guess at first, shown in the DoW. [V]
- 2025 changes: SLE moved into the DoW; "Kanban Measures" renamed Flow Metrics; WIP control less prescriptive; removed the claim that Kanban is immutable. [V]
- Little's Law (average cycle time equals average WIP divided by average throughput) underlies why WIP limits shorten cycle time. The Guide refers to queuing theory but does not name the law; attribute to John Little (1961) from general knowledge. [U, flag]
- B2B application: Kanban fits platform, SRE-facing, integration and connector teams whose demand is interrupt-driven (escalations, partner requests, security fixes). The PM's levers are WIP limits, explicit classes of service (expedite for a P1 customer escalation), and an SLE that sales and customer success can quote.

### 5. Shape Up (Ryan Singer, Basecamp)

- Web book by Ryan Singer, foreword by Jason Fried. [V] Publication year 2019. [S]
- Mechanics: six-week cycles; two-week cool-down for bugs, ad hoc work and the betting table; **appetite** (how much time the business wants to spend, set before design, the opposite of an estimate); small batch (several one to two week projects in a cycle) or big batch (one six-week project); **shaping** by a small senior group working in parallel, at the right level of abstraction (rough, solved, bounded); **betting table** in cool-down where stakeholders choose pitches for the next cycle; a bet is uninterrupted and expected to ship; **circuit breaker**: unfinished projects are cancelled by default, not extended; "Bets, Not Backlogs"; small integrated teams own their tasks and scope; **hill charts** show work moving from unknown (uphill) to known (downhill). [V]
- Pitch template (from the book's shaping chapters, verify headings before using): problem, appetite, solution, rabbit holes, no-gos. [U on exact headings; widely reproduced]
- B2B application: fixed time, variable scope matches launch dates at a customer event. Watch the gaps: Shape Up assumes a small company with few external commitments; enterprise teams need to map cycles to quarterly planning and to reserve capacity for escalations. Appetite is the most portable idea for enterprise PMs.

### 6. Dual-track agile (Desiree Sy, Marty Cagan, Jeff Patton)

- Desiree Sy described the pattern in 2007 for UX work in agile teams; Cagan popularised "dual-track agile" (SVPG, 2012); Patton wrote the canonical explainer (2017, updated 2023). [V]
- Discovery track: fast, cheap learning, hypotheses, time-boxed experiments, decide build, kill or keep learning. Delivery track: predictable, quality, releasable software. [V]
- Patton's cautions: two tracks, not two teams; discovery is not a phase before development; good discovery kills many ideas; learning continues after release. [V]
- Cagan later dropped the label for "continuous discovery and continuous delivery" because the name pushed people toward process. [V]
- Link to Part I and III chapters on discovery. B2B application: the PM, designer and tech lead (Cagan's trio) spend a fixed share of each week in discovery with design partners while the team ships; the backlog only receives items that passed a discovery test.

### 7. Scaled frameworks (brief)

- **SAFe** (Scaled Agile). Core SAFe 6.0 (released April 2023 [S]). Agile Release Trains plan in **Planning Intervals** (formerly Program Increments [U]), cadence-based timeboxes typically 8 to 12 weeks, usually four or five iterations plus an Innovation and Planning (IP) iteration. [V] Prioritises with **WSJF** = Cost of Delay divided by job duration, with Cost of Delay = user and business value + time criticality + risk reduction or opportunity enablement, all relatively estimated; credited to Don Reinertsen's *The Principles of Product Development Flow* (2009). [V]
- **AI-Native SAFe (June 2026).** Released alongside Core SAFe, not replacing it; Early Access guidance every two weeks; full reveal at SAFe Summit, San Diego, 14 to 18 September 2026; thesis that the bottleneck has moved from building to verifying that what is built is safe, secure and valuable. Details of new roles are secondary only. [V for the framing]
- **Critiques (opinion, attribute by name):** Fowler's Agile Industrial Complex (process imposed on teams); Ron Jeffries (the premise that being large means you must "scale" is wrong) [S]; Dave Snowden ("SAFe: the infantilism of management") [S]; common PM complaint that SAFe puts PMs into delivery coordination and front-loads planning, encouraging bigger batches [S]. Defenders say later versions answer earlier critiques [S].
- **LeSS** (Craig Larman and Bas Vodde [S]). One Product Owner, one Product Backlog, one common Sprint, one shippable increment for the whole product; LeSS for up to eight teams of eight; LeSS Huge up to a few thousand people; cross-functional feature teams, no single-specialist teams; "deliberately simple". [V]
- Teaching stance: scaled frameworks solve a coordination problem. A PM should first ask whether the architecture and team topology can remove the dependencies instead of coordinating them.

### 8. Choosing a method

Suggested selection guide (author synthesis, built from the sources above):

| Situation | Default method | Why |
|---|---|---|
| Known solution, fixed external scope and date, ordered domain | Plan-driven with iterative build inside gates | Analysis works; change is costly |
| New capability, value risk high, stakeholders want regular demos | Scrum with dual-track discovery | Sprint Goal and Review force inspection |
| Interrupt-driven, many small items, service commitments | Kanban with WIP limits and an SLE | Flow and predictability per item |
| Product bets with a fixed launch date and variable scope | Shape Up style cycles, or Scrum with appetite-based scoping | Fixed time, variable scope |
| Five or more teams on one product, heavy dependencies | LeSS first; SAFe if the organisation needs portfolio governance | Coordination cost |
| AI agent-heavy team, small changes, strong CI and evals | Continuous flow with short planning cadence and frequent review | Batch size shrinks; verification is the constraint |

Questions for the guide: How much is known (Cynefin)? Where is the main risk (value, usability, feasibility, viability, per Cagan's four risks)? What external commitments exist? How interrupt-driven is demand? How many teams share the codebase? How strong is test and eval automation?

### 9. RICE in depth (Sean McBride, Intercom, 2018)

- Motivation: teams favour pet ideas, clever ideas and new work, and underweight effort. [V]
- **Exact scales:**
  - Reach: people or events per time period from real metrics (Intercom example: customers per quarter).
  - Impact per person against one goal: 3 massive, 2 high, 1 medium, 0.5 low, 0.25 minimal.
  - Confidence: 100% high, 80% medium, 50% low; below 50% is a "total moonshot".
  - Effort: person-months across product, design and engineering; whole numbers, 0.5 for well under a month.
  - Score = (Reach x Impact x Confidence) / Effort: total impact per time worked. [V]
- Intercom's own guidance: re-sort and challenge results that look wrong; RICE is not a hard rule; dependencies and table stakes may justify lower scores. [V]
- **Pitfalls to teach (author synthesis plus Gilad):**
  1. Confidence assigned by conviction, not evidence. Itamar Gilad's Confidence Meter scores opinions and self-conviction near zero and only climbs with research, data and launch evidence. Pair RICE confidence with an evidence label. [V for Gilad]
  2. Reach in the wrong unit for B2B: users vs accounts vs ARR. For enterprise, define reach as accounts or ARR touched per quarter, and state which.
  3. Impact scale drift between scorers; calibrate with two or three reference items.
  4. Effort in 2026: AI coding agents lower build effort but not review, security, migration and support effort. Estimate total effort to safely in production, including evals and customer communication.
  5. False precision and gaming: a 2,400 vs 2,350 difference is noise.
  6. Ignores cost of delay and strategic fit. Compare with WSJF, which puts time criticality in the numerator.
  7. Bundles ideas of different sizes: score at a comparable grain (initiatives, not tickets).
- RICE scoring sheet template (for the artifact): ID | Initiative | Goal metric | Reach (unit, period, source) | Impact (0.25 to 3, rationale) | Confidence (50/80/100, evidence type) | Effort (person-months, includes review and rollout) | RICE score | Override? (reason: dependency, table stakes, commitment) | Decision.
- AI harness use: the PM asks the agent, via connectors, for reach evidence (accounts affected last quarter from product analytics and CRM), drafts the sheet, then asks the agent to list the weakest assumption per row. No formulas taught.

### 10. Pricing signals (brief, pointer only)

- The eCornell module touches consumer behaviour models applied to pricing. In this chapter, limit to: delivery choices create pricing signals (what ships in which tier, packaging of a beta, usage limits). Point to Chapter 12 (pricing) and Chapter 15. No new research done here; do not add facts.

### 11. AI coding agents and cadence (2026)

- Evidence is mixed and moving:
  - METR RCT (July 2025, early-2025 tools): experienced open-source developers took 19% longer with AI, while believing they were about 20% faster. [V]
  - METR follow-up (February 2026, late-2025 tools): estimates moved to modest speedups (about 18% for returning developers, about 4% for new ones) with wide intervals; METR calls this weak evidence because developers increasingly refused to work without AI. [V]
  - DORA 2025: AI is an amplifier of existing strengths and weaknesses. [V] Secondary coverage says AI adoption now correlates with higher throughput but still with higher instability. [S]
  - DORA AI Capabilities Model (Sept 2025): seven capabilities, including working in small batches, strong version control practices, user-centric focus and quality internal platforms. [V]
  - Anthropic's 2026 Agentic Coding Trends Report (Jan 2026): developers use AI in about 60% of work but fully delegate only 0 to 20% of tasks; oversight moves to reviewing what matters; timeline compression from weeks to days changes which projects are viable. Vendor predictions. [V on PDF]
  - Kent Beck (June 2025): "augmented coding" keeps humans accountable for code quality and tests; warning signs include agents disabling tests. [V]
  - AI-Native SAFe (June 2026): bottleneck moves from building to verification. [V]
- Implications for the chapter (author synthesis):
  1. Batch size should shrink, not grow. Agents make it easy to produce large changes; DORA's small-batches finding says keep them small.
  2. The constraint moves to review, evals, security approval and customer adoption. Flow metrics should track age in review and verification states.
  3. Sprint length and planning overhead: two-week sprints may be too long a feedback loop for build, but still fine for customer-facing review. Consider continuous flow for delivery with a fixed cadence for review, retro and betting.
  4. Effort estimates and velocity become less meaningful; throughput of verified outcomes matters more.
  5. Discovery becomes cheaper (prototypes in hours), so the discovery track can test more ideas; the risk shifts to building things nobody asked for (Anthropic's 27% "would not otherwise have been done" figure cuts both ways).
  6. Working agreements must cover agent use: what agents may change, who reviews, Definition of Done includes evals and tests the agent did not write alone.

## Artifact sketches (for the chapter author)

- **Team working agreement:** cadence (planning, review, retro or betting), WIP limits per state, Definition of Ready (optional) and Definition of Done (tests, evals, security review, docs, release note), agent-use rules (allowed scopes, required human review, no disabling tests), escalation class of service and SLE, meeting norms, decision rights (PM, tech lead, designer), how customer escalations enter the system, review date.
- **Cycle or sprint review template:** goal (Sprint Goal or bet); what shipped vs goal; outcome metric movement; customer evidence shown; what we learned in discovery; flow metrics (throughput, cycle time 85th percentile, oldest item age); risks and decisions needed; next goal.
- **Process health check (quarterly, score 1 to 5 with evidence):** goals are outcomes not output; WIP within limits; cycle time trend; ageing items; batch size of changes; review and verification wait time; escaped defects and incidents; discovery-to-delivery ratio; customer contact per PM per month; agent-generated change share and revert rate; team-reported sustainability; ceremonies that produce decisions.

## (b) Verified facts with URL and date

- [V] Agile Manifesto, four values and 17 signatories, 2001. https://agilemanifesto.org/ (checked 2026-10-30)
- [V] Scrum Guide 2020 (November 2020): 3 accountabilities, 5 events with timeboxes (Planning 8h, Daily 15 min, Review 4h, Retro 3h for a one-month Sprint), 3 artifacts with commitments, team of 10 or fewer, PO is one person. https://scrumguides.org/scrum-guide.html
- [V] Kanban Guide v2025.5 (1 May 2025): definition, three practices, four flow metrics, SLE definition, list of 2025 changes. https://kanbanguides.org/the-kanban-guide/
- [V] Kanban Guide v2020.7 (July 2020) contributors include John Coleman and Daniel Vacanti. https://kanbanguides.org/the-kanban-guide/2020.7
- [V] Shape Up by Ryan Singer, foreword by Jason Fried: six-week cycles, two-week cool-down, appetite, betting table, circuit breaker, hill charts. https://basecamp.com/shapeup/0.3-chapter-01
- [V] Patton, Dual Track Development is not Duel Track, 10 May 2017 (updated 12 Apr 2023); credits Desiree Sy 2007. https://jpattonassociates.com/dual-track-development/
- [V] Cagan, Dual-Track Agile, 17 Sep 2012; later replaced the term with continuous discovery and delivery. https://www.svpg.com/dual-track-agile/
- [V] Cagan, Product Manager vs. Product Owner, 6 Dec 2011. https://www.svpg.com/product-manager-vs-product-owner/
- [V] McBride, RICE, Intercom, 5 Jan 2018: scales and formula. https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/
- [V] SAFe Planning Interval: 8 to 12 weeks, usually 4 or 5 iterations plus IP iteration. https://framework.scaledagile.com/planning-interval
- [V] SAFe WSJF = Cost of Delay / job duration; CoD components; Reinertsen attribution. https://framework.scaledagile.com/wsjf
- [V] AI-Native SAFe announced 16 Jun and released 23 Jun 2026, alongside Core SAFe. https://framework.scaledagile.com/blog/ai-native-safe-is-the-operating-model-for-the-ai-native-organization
- [V] LeSS: one PO, one backlog, one Sprint; up to eight teams of eight; LeSS Huge to a few thousand. https://less.works/less/framework/index
- [V] Fowler, Agile Australia keynote transcript, 25 Aug 2018. https://martinfowler.com/articles/agile-aus-2018.html
- [V] METR RCT, 10 Jul 2025: 16 developers, 246 issues, 19% longer with AI; forecast 24% faster, perceived 20% faster. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- [V] METR update, 24 Feb 2026: about 18% and 4% speedups with wide CIs; selection bias. https://metr.org/blog/2026-02-24-uplift-update/
- [V] DORA 2025: AI as amplifier. https://dora.dev/research/2025/dora-report/
- [V] DORA AI Capabilities Model, 23 Sep 2025: seven capabilities incl. small batches; almost 5,000 survey respondents and 78 interviews. https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model
- [V] Anthropic 2026 Agentic Coding Trends Report (Jan 2026): eight trends; 60% of work uses AI, 0 to 20% fully delegated; 27% of AI-assisted work would not otherwise be done. https://resources.anthropic.com/2026-agentic-coding-trends-report
- [V] Beck, Augmented Coding: Beyond the Vibes, 25 Jun 2025. https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
- [V] Cynefin: Snowden, late 1990s, first framework reference 1999; ordered, complex, chaotic, confused. https://cynefin.io/wiki/Cynefin
- [V] Gilad Confidence Meter: opinions score near zero. https://itamargilad.com/the-tool-that-will-help-you-choose-better-product-ideas/
- [S] Royce 1970 described then warned against the sequential model. https://dwheeler.com/essays/waterfall.html
- [S] SAFe 6.0 released April 2023. Search summary only.
- [S] DORA 2025: AI now associated with higher throughput and higher instability; about 90% AI use. Secondary coverage.

## (c) Quotes (under 15 words)

1. "The Product Owner is one person, not a committee." Scrum Guide 2020, Schwaber and Sutherland.
2. "The Scrum framework is purposefully incomplete" Scrum Guide 2020.
3. "AI's primary role is as an amplifier" DORA, State of AI-assisted Software Development 2025.
4. "total impact per time worked" Sean McBride, Intercom, 2018 (describing the RICE score).
5. "you care about the code, its complexity, the tests, & their coverage" Kent Beck, 2025 (13 words).

## (d) 2025 to 2026 AI-era developments (verified)

- Kanban Guide v2025.5 (May 2025): less prescriptive WIP control, SLE inside the Definition of Workflow. Not AI-specific but current.
- Scrum Guide Expansion Pack (2025): optional "AI and Scrum" guidance; 2020 Guide unchanged.
- METR July 2025 slowdown result, then February 2026 update showing modest speedups and a measurement crisis because developers will not work without AI.
- DORA 2025 report and AI Capabilities Model: AI amplifies; small batches, version control, user focus and internal platforms determine whether it helps.
- Kent Beck's augmented coding (June 2025): TDD and small steps as the discipline for agent work.
- Anthropic 2026 Agentic Coding Trends Report: delegation is partial, oversight shifts to what matters, timelines compress.
- AI-Native SAFe (June 2026): scaled framework vendor reframes the bottleneck as verification.
- Synthesis for the chapter: in 2026 the method question shifts from "how do we plan build work" to "how do we keep batches small and verification fast when build is cheap".

## (e) Beacon worked example ideas (consistent with beacon-case.md)

- **Five teams, three methods.** Beacon has about 35 engineers across 5 teams. Suggested split (fictional, decide in chapter): Correlate team (mature, migrating customers off Beacon Classic) runs Kanban with an SLE for migration tickets; Diagnose and Act teams (Beacon Agents) run two-week Scrum with dual-track discovery and evals in the Definition of Done; Connectors and platform team runs Kanban with an expedite class for customer escalations; Learn team runs Shape Up style six-week bets. Shows that one product can use more than one method under shared outcome goals and a shared North Star (incidents resolved with Beacon's help per week).
- **Fixed date, variable scope: Northlight Live.** The Beacon Agents launch at Northlight Live is a fixed date. The Principal PM sets an appetite (for example two six-week cycles) for supervised remediation and cuts scope (fewer runbook actions, allowlisted low-risk only) rather than moving the date. Circuit breaker: if autonomous rollback is not safe by the end of cycle two, it ships as approval-gated only.
- **RICE sheet for the next quarter.** Candidate items: per-resolved-incident billing instrumentation (pricing move, pointer to Ch 12 and 15); multi-tenant MSP view for Leo; AI Act documentation pack for EU customers (Sam); diagnosis citation improvements after the hallucinated root-cause incident; Beacon Classic migration tooling. Show reach in accounts or ARR touched, not users. Show the overrides: AI Act pack is a table-stakes commitment for EU renewals; citation fix gets confidence 100% because of incident evidence. Show how effort changes when the team accounts for evals and security review, not just agent-written code.
- **WSJF contrast.** Re-score the same list with WSJF; Classic sunset has high time criticality (support cost, contract dates), which RICE underweights.
- **AI agents and batch size.** Beacon engineers use coding agents; PR volume rose and review age became the oldest-item hotspot on the Kanban board. Process health check reveals verification wait time; the team adds a WIP limit on "in review", splits agent work into smaller PRs, and adds eval gates. Ties to the hallucinated root-cause storyline: an oversized change that skipped eval review.
- **Working agreement clause on agents.** Agents may open PRs in Diagnose and Act code; any change touching the Act approval gate needs two human reviewers and Sam's security sign-off; agents may not change or disable eval suites.
- **Gross margin as a delivery constraint.** Margin fell from 81% to 72% on inference cost; inference cost per resolved incident becomes a Definition of Done check for Diagnose features. Point to pricing chapters.
- **Scaled framework temptation.** Northlight leadership considers SAFe across Observe, Desk and Beacon; the Principal PM argues for LeSS-style single backlog per product plus a quarterly portfolio review, citing dependency reduction through connectors and APIs. Keep as a debate, not a verdict.

## (f) Editorial flags

- Shape Up publication year 2019 is [S]; the web book does not state it. Pitch headings (problem, appetite, solution, rabbit holes, no-gos) not verified on the page this session.
- Royce 1970: no primary access; use paraphrase and "often read as". The "do it twice" detail is from Wikipedia.
- Little's Law attribution (John Little, 1961) from general knowledge; not in Kanban Guide.
- "Planning Interval formerly Program Increment" not confirmed on the SAFe page.
- SAFe 6.0 release date April 2023 [S]. AI-Native SAFe role and practice details beyond the bottleneck framing are secondary.
- LeSS creators (Larman and Vodde) not on the fetched page [S].
- SAFe critiques (Jeffries, Snowden, Aha!) are opinion pieces; attribute as views, do not state as fact. Cagan's direct position on SAFe not found on SVPG; do not claim it.
- DORA 2025 throughput and instability findings and "about 90%" adoption are [S]; primary PDF not read. Do not quote numbers from 2024 as 2025.
- METR numbers: sign convention is easy to flip. Positive = slower. February 2026 results are explicitly weak evidence.
- Anthropic report is a vendor document with forecasts and customer cases; treat as direction of travel. The 60% and 0 to 20% figures originate in Anthropic Societal Impacts research cited in the report.
- Scrum Guide Expansion Pack release date (June vs July 2025) unresolved.
- Cagan's "four risks" (value, usability, feasibility, viability) used in the selection guide from memory of *Inspired*; cross-check with earlier chapters.
- Gilad's article is undated and does not mention RICE; the RICE pitfall link is our synthesis.
- WebSearch budget was exhausted; the eCornell course page was not fetched and its module list is taken from the brief.

## Extra details not used above

- METR note (17 Feb 2026): transcript analysis of 7 METR staff using Claude Code estimated time savings of about 1.5x to 13x, described as a soft upper bound [S]. https://metr.org/notes/2026-02-17-exploratory-transcript-analysis-for-estimating-time-savings-from-coding-agents/
- Fowler (2018) calls widespread name-only agile "faux-agile".
- Snowden critique of SAFe: https://thecynefin.co/safe-the-infantilism-of-management [S, not fetched].
