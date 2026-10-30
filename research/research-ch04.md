# Research notes: Chapter 04, Product Prototyping

Status: in progress (started 2026-10-30). Tags: [V] verified on primary source; [S] secondary only; [U] unverified.

## (b) Verified facts: source log (S1 to S32)

### S1. Marty Cagan, "Flavors of Prototypes," SVPG, 2014-02-23 [V]
URL: https://www.svpg.com/flavors-of-prototypes/
- Five flavors (four families, user split by fidelity):
  - Feasibility prototype: built by engineers in discovery to retire technical risk (new tech, algorithm, performance). Just enough code to answer the question; may have no UI; may be thrown away.
  - Low-fidelity user prototype: interactive wireframes; simulation; covers information and workflow only, not visual design or real data. Built by interaction designers.
  - High-fidelity user prototype: still a simulation, looks real, realistic but not live data. Used for usability testing, stakeholder communication, fast learning. Cannot prove a product will sell. Cagan's favourite use: learn why users do not like a design, not whether they do.
  - Live-data prototype: connects to real data, receives live traffic in quantity (A/B, opt-in, invite-only). Implements only critical use cases; skips productization (full use cases, test automation, localization, scalability, SEO). Built by developers. Purpose: real analytics to prove the approach beats current product.
  - Hybrid: combines aspects; example: live data but no live traffic, so team observes users to learn about relevance (search, recommendations). Learn, not prove.
- Says of live-data prototypes: "this is not a product" [V]; engineers must still productize after a successful test.
- Fidelity defined as how realistic the prototype looks [V].
- Note: Shortform summary of Inspired treats hybrid more broadly and cites Wizard of Oz as an example [S]. Inspired 2nd ed. (Wiley, 2017) has separate chapters on each type [S: O'Reilly listing].

### S2. Marty Cagan, "The Purpose of Prototypes," SVPG, 2025-09-12 [V]
URL: https://www.svpg.com/the-purpose-of-prototypes/
- Prototypes exist primarily to discover a solution worth building: "building to learn" vs delivery, "building to earn" [V].
- Use prototypes to test the four risks (value, usability, feasibility, viability) before building.
- Communication to engineers is a real but secondary benefit; teams that treat the prototype mainly as a communication artifact and skip testing build products that fail.
- Names Lovable, Bolt and Figma Make as gen-AI prototyping tools; says these are generally not for building actual products, and do not need to be [V].
- Production quality (reliable, scalable, maintainable, performant, secure) is "almost always" done with different tools and skills [V].
- Most products fail because teams could not discover a solution worth building, not because they could not build: faster building does not address that.
- Security/compliance reviewers may need prototypes to assess viability.
- Testing probabilistic (AI) prototypes adds layers; promised in later articles.
- Says top product companies now evaluate candidates' use of these tools for product-creator roles [V, claim as stated by Cagan].

### S3. Jakob Nielsen, "Why You Only Need to Test with 5 Users," NN/g, 2000-03-18 [V]
URL: https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/
- Nielsen and Thomas Landauer model: problems found = N(1 - (1 - L)^n); average L = 31% across Nielsen's projects [V].
- Five users find about 85% of problems in a study [V].
- Recommendation: many small studies, not one big one. With budget for 15, run three rounds of 5, redesigning between rounds [V].
- Distinct user groups: 3 to 4 per group for two groups; 3 per group for three or more [V].
- Caveats: assumes comparable users; 31% is an average not a law; one user can mislead, aim for at least 3.
- Quotes: "zero users give zero insights"; "Elaborate usability tests are a waste of resources." [V]

### S4. Jakob Nielsen, "How Many Test Users in a Usability Study?," NN/g, 2012-06-03 [V]
URL: https://www.nngroup.com/articles/how-many-test-users/
- Qualitative usability: 5. Quantitative: at least 20. Card sorting: at least 15 per group. Eyetracking: 39 for stable heatmaps [V].
- B2B use: five is per persona/role. Beacon has distinct roles (on-call engineer, SRE lead, security reviewer), so plan 3 to 5 per role, not 5 total.

### S5. Jakob Nielsen, "Thinking Aloud: The #1 Usability Tool," NN/g, 2012-01-15 [V]
URL: https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/
- Definition: participants use the system while continuously verbalizing thoughts [V].
- Benefits: cheap, robust, flexible (paper to shipped), persuasive (let execs watch), learnable in a day.
- Downsides: not statistical; unnatural; participants filter thoughts to look smart; facilitator prompts can bias behavior.
- Facilitator steps: recruit representative users, give representative tasks, shut up and let them talk (prompt only on silence), avoid leading questions, note where you intervened and discount that data.
- Quote: "Thinking aloud may be the single most valuable usability engineering method." (over 15 words? No: 10 words) [V]

### S6. Steve Krug, Rocket Surgery Made Easy, New Riders, 2010 [S for details]
Secondary: Lee Munroe review, 2010 (https://leemunroe.com/rocket-surgery-made-easy); book TOC listings.
- DIY testing: one morning a month, three participants, debrief the same day (TOC chapter "Debriefing 101") [S].
- Observers each note the most serious problems they saw; team fixes the most serious first [S].
- Fix with the smallest change that solves the problem: "try to do the least you can do" [S, quoted in review; confirm in book].
- Krug concedes three users are not statistically valid; value comes from frequency [S].
- Reconcile with Nielsen: both argue small, frequent rounds over large rare studies. Krug's 3/month is a cadence; Nielsen's 5 is a per-round sample.
- Krug's earlier book Don't Make Me Think (1st ed. 2000; 3rd "Revisited" ed. 2014) is the source of the self-evident design principle [S].

### S7. Sara Paul and Maria Rosala, "The Wizard of Oz Method in UX," NN/g, 2024-04-19 [V]
URL: https://www.nngroup.com/articles/wizard-of-oz/
- Definition: participant uses an interface that appears automated but is fully or partly run by a hidden human "wizard" [V].
- Origin: Don Norman and Allen Munro used it in 1973 (airport travel assistant); Jeff Kelley coined the name in his 1983 Johns Hopkins dissertation on natural-language interfaces [V per NN/g].
- Best for: conversational interfaces, recommendation algorithms, real-time lookup; lowers investment risk of gen-AI features by testing desirability before building [V].
- Caveats: participants may guess a human is behind it (roleplay); debrief if deception used; responses hard to keep consistent; engineers should define feasible responses; pilot first; static prototypes often suffice.
- Quote: "a user interacts with an interface that appears to be autonomous." [V]

### S8. Concierge MVP, Manuel Rosso (Food on the Table), SlideShare deck, c. 2011 [S]
URL: https://www.slideshare.net/slideshow/manuel-rosso-food-on-the-table/7239850
- Food on the Table served its first customer by hand (face-to-face meal planning) before automating. Argument: if you cannot win adoption with a high-touch personal service, a web page will not do it [S].
- Eric Ries tells this story in The Lean Startup (2011) as the concierge MVP [S; book is primary, not fetched].
- Distinction (synthesis): in a concierge test, the customer knows a human is doing the work; in Wizard of Oz, the human is hidden and the customer believes it is automated. Concierge tests value; WoZ tests the experience and value of the future automated product.

### S9. Kara Pernice, "UX Prototypes: Low Fidelity vs. High Fidelity," NN/g, 2016-12-18 [V]
URL: https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/
- Fidelity = how closely the prototype resembles the final product, on three independent dimensions: interactivity, visuals, content [V]. A prototype can be high on one and low on another.
- Low fidelity: fast, changeable mid-session, users criticize more freely, designers less attached; risk: slow human "computer" breaks flow.
- High fidelity: realistic timing and behavior, tests detailed workflows and components; risk: slower to build, attachment to polished work.
- Notes Wizard of Oz is especially useful for AI systems before the AI exists [V].
- Pilot every prototype before sessions.
- Quote: "testing final products is uninformed and risky." [V]
- 2026 application: AI builders collapse the build cost of high fidelity, which makes the attachment risk worse, not better. Teach the PM to choose fidelity per dimension: e.g., low visual fidelity, high content fidelity (real incident data) for Beacon.

### S10. Colin Matthews, "A guide to AI prototyping for product managers," Lenny's Newsletter, 2025-01-07 [V for free portion; rest paywalled]
URL: https://www.lennysnewsletter.com/p/a-guide-to-ai-prototyping-for-product
- Three categories [V]:
  1. Chatbots (Claude, ChatGPT): simple one-off prototypes; Claude Artifacts run code and share a link; limited multi-page.
  2. Cloud development environments (Replit, Bolt, v0, Lovable): full-stack, hosted, multi-page prototypes.
  3. Local developer assistants (GitHub Copilot, Cursor, Windsurf, Zed): IDE tools working in a real codebase; for production-bound work by people who code.
- His per-tool advice (v0 for design quality, Bolt for speed, Replit for data tools, Lovable for integrations) is a snapshot of early 2025; tool positions shift fast. Use categories, not brand rankings, in the book.
- Follow-up "How to get your entire team prototyping with AI" (Lenny's, paywalled) covers team-wide workflow [S].

### S11. Figma, "Config 2025 press release," Figma blog, 2025-05-07 [V]
URL: https://www.figma.com/blog/config-2025-press-release/
- Figma Make announced: "An AI-powered prompt-to-code tool that turns written descriptions or existing designs into working prototypes or apps" [V, quote over 15 words; paraphrase in book].
- Same event: Figma Sites, Draw, Buzz, Grid [V]. Secondary reports that Make went GA in July 2025 [S].
- Category name for the book: design-to-code (start from a design or design system, output a coded prototype).

### S12. Andrej Karpathy coins "vibe coding," X post, February 2025; Collins Word of the Year 2025 (announced 2025-11-06) [S]
URLs: https://en.wikipedia.org/wiki/Vibe_coding ; coverage e.g. https://kvia.com/news/business-technology/cnn-business-consumer/2025/11/06/vibe-coding-named-collins-dictionarys-word-of-the-year/
- Karpathy described fully giving in to the AI and not reading the generated code [S]. Collins defines it as turning natural language into code using AI [S].
- Book use: define vibe coding precisely as building without reading the code. That is acceptable for a throwaway prototype and unacceptable for a product. This is the sharpest way to restate Cagan's prototype-vs-product line in 2026.

### S13. Anthropic, "Introducing Claude Design by Anthropic Labs," anthropic.com, 2026-04-17 [V]
URL: https://www.anthropic.com/news/claude-design-anthropic-labs
- Research preview for Pro, Max, Team and Enterprise; off by default on Enterprise until admins enable it [V].
- Creates designs, prototypes, slides, one-pagers through conversation; can apply a team's design system; inputs include prompts, documents, a codebase, or captured website elements [V].
- Turns static mockups into interactive shareable prototypes for feedback and user testing; can build code-powered prototypes [V].
- Handoff bundle passes a finished design to Claude Code [V]. Exports: internal URL, folder, Canva, PDF, PPTX, HTML.
- Book use: an example of the "harness-native" category where the PM's AI harness, already connected to docs and code, produces the prototype. Mention by category with this as one dated example; avoid tool advocacy.
- Secondary claim that Figma stock fell 7% on launch day: [U], do not use.

### S14. Lovable CVE-2025-48757 (row-level security), published to NVD 2025-05-30 [S]
URL: https://www.sentinelone.com/vulnerability-database/cve-2025-48757/ (NVD page did not render; SentinelOne mirror)
- Insufficient row-level security policy in Lovable-generated sites (through 2025-04-15) let unauthenticated attackers read or write arbitrary tables; CVSS 3.1 score 9.3 critical; CWE-863 [S].
- Vendor disputes the CVE, stating customers are responsible for protecting their application data [S].
- Reported by researcher Matt Palmer; about 170 affected projects found in a scan of Lovable's showcase [S, figures vary by source].
- Book use: the concrete reason a vibe-coded prototype must never be connected to real customer data or exposed publicly without engineering review. Cite as "a 2025 critical vulnerability disclosure" with the CVE ID; avoid naming more than needed. Later "April 2026 breach" reports: [U], do not use.

### S15. Teresa Torres, "Product Trio," Product Talk, 2021-05-05 [V]
URL: https://www.producttalk.org/product-trio/
- Trio = at minimum a product manager, a designer and a software engineer, jointly responsible for a shared outcome [V].
- Contrasts with handoff model (requirements rewritten, mockups redesigned, code rewritten; late and over budget).
- Together they interview customers, map the opportunity space, pick a target opportunity, generate solutions and test them iteratively [V].
- Missionary vs mercenary teams (phrase originates with John Doerr, popularized by Cagan) [S on origin].
- Quote: "A product trio is jointly responsible for a shared outcome." [V]
- 2026 extension (book's own synthesis, flag as such): for AI features, add an applied AI engineer (or ML engineer) as a standing fourth member during discovery, because model feasibility and evals are core risks. Beacon already has 2 applied AI engineers.

### S16. Matthew Skelton and Manuel Pais, Team Topologies (IT Revolution, 2019; 2nd ed. 2025 [U]); key concepts page [V]
URL: https://teamtopologies.com/key-concepts
- Four team types [V]: stream-aligned (delivers customer value on a value stream, owns outcomes); platform (provides services that remove complexity for stream-aligned teams); enabling (temporarily builds capability in other teams, then moves on); complicated subsystem (owns components needing specialist knowledge).
- Three interaction modes [V]: collaboration (close, time-boxed, high bandwidth, high cost, for discovery); X-as-a-Service (clear boundary, minimal interaction); facilitating (one team helps another remove obstacles, temporary).
- Cognitive load: teams have limited capacity; overloaded teams decide worse and slow down [V].
- Interaction modes should evolve: collaborate to discover an interface, then move to X-as-a-Service [S].
- PM application: in staffing a new initiative, name the team type and the interaction mode with each neighbor. For a platform PM, the internal teams are the customer and X-as-a-Service is the target end state.

### S17. Marty Cagan, Inspired (2nd ed., Wiley, 2017) and Empowered (with Chris Jones, Wiley, 2020): team composition [S]
- Product team = cross-functional (product manager, product designer, typically 2 to 10 engineers, with a tech lead) empowered to solve a problem rather than build a handed-down feature [S].
- Distinguishes empowered product teams from delivery teams (no PM or designer; build features handed to them) and feature teams [S].
- Inspired has a breakout on the tech lead role [S, TOC].

### S18. Marieke McCloskey, "Turn User Goals into Task Scenarios for Usability Testing," NN/g, 2014-01-12 [V]
URL: https://www.nngroup.com/articles/task-scenarios-usability-testing/
- Three rules [V]: make the task realistic; make it actionable (do it, do not describe it); avoid clues and step-by-step instructions (do not name buttons or menu labels).
- Specific but not leading: give the context details a real user would have.
- Beacon task example (book's own): "You were paged for checkout latency at 03:10. Find out what most likely caused it and decide what to do next." Not: "Click the Diagnose tab and read the root cause."

### S19. Jakob Nielsen, "Severity Ratings for Usability Problems," NN/g, 1994-11-01 [V]
URL: https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/
- Severity = frequency + impact + persistence; assess market impact separately [V].
- Scale 0 to 4 [V]: 0 not a usability problem; 1 cosmetic (fix if time); 2 minor (low priority); 3 major (high priority); 4 usability catastrophe (must fix before release).
- Readout use: every finding gets a severity, a count (e.g., 4 of 5 participants), evidence (clip or quote), and a decision (fix, test again, accept, kill).

### S20. Marty Cagan, "Revisiting the Product Spec," SVPG, 2006-10-12 [V]
URL: https://www.svpg.com/revisiting-the-product-spec/
- Traditional specs take too long, are seldom read, and give a false sense of progress [V].
- A high-fidelity prototype covering nearly all screens and major use cases should be the majority of the spec; the spec is not ready for engineering until the prototype passes usability and desirability tests [V].
- Supplement with use cases, release requirements (reliability, performance, scalability), platform requirements [V].
- Quote: "the spec must accurately represent the behavior of the software" [V]
- Tension for the chapter: in B2B and platform work, the PRD still carries things a prototype cannot show (API contracts, permissions, SLAs, compliance, pricing and packaging, migration, partner impact). Teach "prototype shows, PRD decides": the prototype is the behavior spec, the PRD is the decision record and the non-visible requirements.

### S21. Werner Vogels, "Working Backwards," All Things Distributed, 2006-11-01 [V]
URL: https://www.allthingsdistributed.com/2006/11/working_backwards.html
- Four documents written before building [V]: press release; FAQ; customer experience (mockups of each screen; for web services, use cases with code snippets); user manual (concepts, how-to, reference; one per user type).
- Start from the customer and work backward to the minimum technology needed [V].
- Quote: "The goal is to drive simplicity through a continuous, explicit customer focus." (12 words) [V]
- Platform note: for APIs, the "customer experience" document is sample code; for a B2B platform PM this is the strongest argument for writing the developer docs first.

### S22. Colin Bryar and Bill Carr, Working Backwards (St. Martin's Press, 2021); workingbackwards.com concept page [V for page; book details S]
URL: https://workingbackwards.com/concepts/working-backwards-pr-faq-process/
- Press release structure [V]: heading (one sentence naming the product); subheading (target customer and benefit, one sentence); summary (location, outlet, realistic launch date, overview); problem; solution (better, faster or cheaper than alternatives); quotes (company spokesperson, hypothetical customer); how to get started.
- FAQ [V]: external (customer and press: price, how it works, support) and internal (competition, market size, demand, unit economics, upfront investment, legal and regulatory, dependencies, technical challenges, assumptions, top reasons it could fail).
- Review [V]: author drafts and refines with manager and peers; first review with about 10 people led by a decision-maker; meetings open with 15 to 20 minutes of silent reading then about 40 minutes of discussion; outcome go, no-go, defer, rework or reprioritize.
- Many iterations; AWS's initial PR/FAQs took over a year; Fulfillment by Amazon wrote two PR/FAQs (seller and buyer) [V per page].
- Commonly cited length guidance (press release about one page, FAQ up to about five pages): [S], not confirmed on the page fetched; confirm in book before stating.
- Funnel not tunnel: the process screens out most ideas [V].

### S23. Ryan Singer, Shape Up, Basecamp (37signals), 2019; ch. 6 "Write the Pitch" [V for content; year S]
URL: https://basecamp.com/shapeup/1.5-chapter-06
- Pitch ingredients [V]: problem; appetite (time the team is willing to spend); solution (core elements, quickly graspable); rabbit holes (known pitfalls patched in advance); no-gos (explicit exclusions).
- Quote: "Stating the appetite in the pitch prevents unproductive conversations." [V]
- Use: the one-page PRD should borrow appetite and no-gos. Appetite ties the PRD to the staffing plan (fixed time, variable scope).

### S24. Den Delimarsky, "Spec-driven development with AI: Get started with a new open source toolkit," GitHub Blog, 2025-09-02 [V]
URL: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
- Spec Kit: open source toolkit for writing specs that AI coding agents (GitHub Copilot, Claude Code, Gemini CLI) consume [V].
- Four phases [V]: specify (what and why, user journeys, success criteria); plan (stack, architecture, constraints); tasks (small testable items); implement (agent works tasks, human reviews focused changes).
- Argument: vague prompts force agents to guess; specs become living, executable artifacts; "intent is the source of truth" [V].
- Book use (2026 PRD): the PRD now has two readers, humans and agents. Write requirements so an agent can turn them into a plan and tests: explicit user journeys, acceptance criteria, non-goals, constraints. The PRD's "what" sections feed the engineering spec; the PM does not write the plan or tasks.

### S25. Kate Moran, "Usability Testing 101," NN/g, 2019-12-01, last reviewed 2026-07-15 [V]
URL: https://www.nngroup.com/articles/usability-testing-101/
- Three elements [V]: facilitator, tasks, participant (often thinking aloud).
- Qualitative (find problems, more common) vs quantitative (task success, time on task, benchmarks) [V].
- In-person vs remote; remote is moderated (live over screen share) or unmoderated (tool delivers written tasks) [V].
- B2B note: moderated remote is the default for enterprise users (scarce, busy, behind firewalls). Unmoderated rarely works for complex expert workflows.

### S26. Maria Rosala and Kate Moran, "Synthetic Users: If, When, and How to Use AI-Generated 'Research'," NN/g, 2024-06-21 [V]
URL: https://www.nngroup.com/articles/synthetic-users/
- Synthetic users cannot replace research with real people; useful only for desk research, preparing studies (piloting a guide), and generating hypotheses [V].
- Limitations [V]: sycophantic, overly favorable answers (synthetic learner claimed to finish every course; real learners had not); shallow, unprioritized needs; no real behavior; approve nearly every concept; weak on niche populations.
- Quote: "Real user research is essential." [V]
- Book use: in a 2026 workflow, the harness can pilot the test script against a synthetic participant to catch confusing tasks, draft the readout from transcripts, and cluster findings. It must not stand in for the five real participants. Niche B2B roles (SRE on-call, security reviewer) are exactly where synthetic users are weakest.

### S27. Marty Cagan, "Prototypes vs Products," SVPG, 2025-11-07 [V]
URL: https://www.svpg.com/prototypes-vs-products/
- Prototype = discovery, build to learn; product = delivery, build to earn [V].
- Scope gap: prototypes cover a few use cases and simple rules; enterprise products can involve dozens to thousands of use cases and complex business policy [V].
- Run-time demands products must meet that prototypes usually do not [V]: reliability; telemetry and observability; performance at scale; multiple languages and currencies; integrations; zero-downtime maintenance and fault tolerance; data security, compliance, disaster recovery.
- Exception: internal tools and customer-enabling tools have lower operational demands, so the path to product quality is shorter [V].
- Prototyping tools (Lovable, Bolt, Figma Make) vs professional build tools (Claude Code, Cursor) serve different purposes [V].
- Warnings [V]: PMs without engineering backgrounds underestimate the prototype-to-product gap and have embarrassed themselves in front of engineers; vendors overstate; the newer risk is product creators themselves confusing prototype and product.
- Quotes: "reliability is our most important feature"; "it's buyer beware." [V]
- Prototype-to-product automation is an open question, partly because spoken-language specs are imprecise [V].

### S28. Marty Cagan, "Build to Learn vs Build to Earn," SVPG, 2026-04-16 (plus "Build To Learn FAQ," 2026-04-27, not fetched) [V]
URL: https://www.svpg.com/build-to-learn-vs-build-to-earn/
- Discovery = build to learn (test value, usability, feasibility, viability); delivery = build to earn (commercial quality: scale, reliability, security). A conceptual model, not sequential phases [V].
- With delivery cost falling, the bottleneck is discovering a solution worth building [V].
- AI prototyping makes live-data prototypes cheaper; teams can test several approaches in parallel, then refine the best sequentially [V].
- PMs are builders who build to learn, not engineers of production systems. PMs whose role is mainly coordination or "glue" face rising risk. The hard skill is product sense: judging what prototypes reveal. Tool proficiency is the easy part [V].
- Quote: "the real bottleneck is in discovering a solution that's worth building." [V]

### S29. Marty Cagan, "Forward Deployed Engineers," SVPG, 2025-09-17 [V]
URL: https://www.svpg.com/forward-deployed-engineers/
- FDE: usually an engineer, increasingly a PM or designer, embedded with a target customer to learn their environment and what outcomes require [V].
- Most valuable in complex enterprise and custom-solution settings; cites AI agent startups; visit several customers to see patterns [V].
- FDEs prototype with customers; a platform product org generalizes what they learn into reusable capabilities (Palantir model as described by Cagan) [V].
- Caution: without a platform strategy, FDEs create many costly custom solutions [V].
- Staffing use for Beacon: one FDE-style engineer embedded with two or three design-partner customers during Beacon Agents discovery, feeding the platform teams.

### S30. Marty Cagan, "The AI Productivity Paradox," SVPG, 2026-07-23 [V]
URL: https://www.svpg.com/the-ai-productivity-paradox/
- Teams using AI to produce old artifacts faster (business cases, roadmaps, requirements docs, code) do not get better outcomes [V].
- Strong teams use AI to prototype and test in discovery, then build commercial-quality products in delivery [V].
- Launching AI-generated builds straight to customers is the risky shortcut [V].
- Cagan cites Chip Huyen: the hardest part remains knowing what to build [V as quoted by Cagan; not checked at origin].
- Book use: warn that an AI-drafted PRD is the same trap. The harness should speed the evidence and the thinking, not the page count.

### S31. Ben Horowitz, "Good Product Manager/Bad Product Manager," a16z, posted 2012-06-15 (written about 15 years earlier) [V]
URL: https://a16z.com/good-product-manager-bad-product-manager/
- Good PMs give direction in writing, define the "what" and leave the "how" to engineering, produce reusable FAQs and documents, and take written positions on major tradeoffs [V].
- Use: the PRD as a written position on the what and why, not the how.

### S32. eCornell, "Product Prototyping" course page (Keith Cowing, Cornell Tech) [V]
URL: https://ecornell.cornell.edu/courses/product-management/product-prototyping/
- Outcomes [V]: create a prototype; create a staffing plan (roles and responsibilities); write a PRD for an MVP, framed as a "pillar artifact" that rallies the team.
- Chapter maps one section to each outcome.

---

## (a) Key concepts and frameworks: synthesis for the chapter

1. **Build to learn vs build to earn (Cagan, S2, S27, S28).** The organizing idea for the chapter. A prototype is the cheapest artifact that answers a specific risk question (value, usability, feasibility, viability). A product survives real customers at scale. B2B application: write the risk question at the top of every prototype ("we are testing whether an on-call engineer trusts a cited root cause enough to act on it"), and name what the prototype deliberately ignores (permissions, multi-tenancy, audit logging, scale).

2. **Cagan's prototype flavors (S1).** Feasibility (engineers, retire technical risk), user (designers; low or high fidelity; simulation), live-data (developers; real data and real traffic; proves), hybrid (e.g., live data without live traffic; learns). Template line for the test plan: "Prototype type: ___. Risk addressed: ___. Built by: ___. Throwaway or reusable: ___."

3. **Fidelity is three dials, not one (Pernice, S9).** Interactivity, visuals, content. B2B rule of thumb (book's synthesis): content fidelity matters most for expert users, so use real or realistic incident data even in a grey wireframe; experts notice fake logs instantly and stop believing.

4. **Fidelity ladder (book's synthesis from S1, S7, S8, S9).** Sketch, wireframe, clickable (user prototype), coded (AI-built or hand-coded user prototype), Wizard of Oz (human hidden behind an apparently automated interface), concierge (human delivers the service openly), live-data prototype. Choose the lowest rung that answers the risk question. WoZ and concierge are rungs on a different axis (simulating the back end, not the front end); place them as "service fidelity."

5. **AI prototyping categories, 2025 to 2026 (S10, S11, S13, S27).** Use categories, not brand rankings:
   - Chat-and-artifact (prototype inside the AI harness; e.g., Claude Artifacts).
   - Prompt-to-app builders, "vibe-coding" builders (hosted full-stack: Lovable, Bolt, v0, Replit).
   - Design-to-code (start from designs or a design system: Figma Make 2025, Claude Design 2026).
   - Coding agents in the real codebase (Claude Code, Cursor, Copilot): delivery tools, used for feasibility or live-data prototypes by engineers.
   Rule: the closer to production data and real customers, the more engineering ownership is required.

6. **Cagan's warnings (S2, S27, S28, S30).** Prototype is not product; enterprise products need reliability, observability, scale, integrations, security, compliance, recovery; PMs underestimate the gap; vendors overstate; communication is a secondary purpose and must not replace testing; building faster does not fix building the wrong thing.

7. **Usability testing (Nielsen S3 to S5, S19; Krug S6; McCloskey S18; Moran S25).** Five users per distinct user group per round, iterate rounds; think-aloud; realistic, actionable tasks with no clues; severity 0 to 4. Krug's cadence: a morning a month, three users, same-day debrief, fix the worst problems with the smallest change.
   - **Test plan template (book's):** decision this test informs; risk and hypothesis; prototype and fidelity; participants (roles, count per role, screener); tasks (3 to 5); success signals and kill signals defined before testing; logistics (moderated remote, recording consent, observers); readout date and decision owner.
   - **Script skeleton (standard NN/g and Krug practice):** welcome and consent; "we are testing the design, not you"; think-aloud instructions with a warm-up; background questions; tasks one at a time; post-task question (e.g., confidence 1 to 7); wrap-up and debrief (reveal WoZ if used).
   - **Readout template:** decision requested; top findings ranked by severity with counts and one clip or quote each; what we will change; what we still do not know; recommendation (proceed, iterate and retest, pivot, stop).
   - **Turning results into decisions (book's synthesis):** pre-register the kill and proceed signals in the plan so results map to a decision, not a debate.

8. **Product trio and team staffing (Torres S15; Cagan S17, S29; Skelton and Pais S16).** Trio jointly owns an outcome. For AI products, add the applied AI engineer to discovery (book's extension, flag). Staffing plan template (book's): outcome and appetite; team type (stream-aligned, platform, enabling, complicated subsystem); roles with named owners and percent allocation; interaction modes with neighboring teams; capacity (engineer-weeks available after on-call, maintenance and keep-the-lights-on load); dependencies; gaps and hiring or borrowing asks; review date.

9. **PRD (Cagan S20; Horowitz S31; Singer S23; Delimarsky S24; Chapter 31).** "Prototype shows, PRD decides." Full PRD sections (book's synthesis): problem and evidence; customer and personas; goals and success metrics; non-goals; scope and user journeys (link prototype); requirements with acceptance criteria; non-functional (security, permissions, audit, performance, residency); dependencies and staffing; risks and open questions; rollout and pricing or packaging impact; decision log. For AI features, add the Chapter 31 addendum (evals as acceptance criteria, failure-mode list, cost per task, human oversight, AI Act role).
   - **One-page PRD (book's synthesis, borrowing Shape Up and Lenny's 1-pager idea):** problem; who; why now; appetite; solution sketch with prototype link; success metric; non-goals; top risks; open questions.

10. **PRFAQ vs PRD (Vogels S21; Bryar and Carr S22).** PRFAQ decides whether to build (customer-facing narrative plus internal FAQ on economics and risk); PRD decides what to build and how we will know it works. Sequence: PRFAQ, then prototype tests, then PRD. For platforms, the "customer experience" document is sample code and API docs.

## (b) Verified facts
See source log S1 to S32 above. Each entry carries URL, date and [V]/[S]/[U] tags.

## (c) Quotes (under 15 words, chosen five)
1. "this is not a product" (Marty Cagan, "Flavors of Prototypes," SVPG, 2014) [V]
2. "the real bottleneck is in discovering a solution that's worth building." (Cagan, "Build to Learn vs Build to Earn," SVPG, 2026) [V]
3. "zero users give zero insights" (Jakob Nielsen, NN/g, 2000) [V]
4. "A product trio is jointly responsible for a shared outcome." (Teresa Torres, Product Talk, 2021) [V]
5. "Stating the appetite in the pitch prevents unproductive conversations." (Ryan Singer, Shape Up) [V]
Alternates: "Real user research is essential." (Rosala and Moran, NN/g, 2024); "reliability is our most important feature" (Cagan, 2025).

## (d) 2025 to 2026 AI-era developments (verified)
- Feb 2025: Karpathy coins "vibe coding"; Collins Word of the Year 2025 (S12) [S].
- Jan 2025: Matthews' three-category map of AI prototyping tools (S10) [V].
- May 2025: Figma Make launched at Config (S11) [V].
- May 2025: CVE-2025-48757 on Lovable-generated apps, disputed by vendor (S14) [S].
- Sep 2025: GitHub Spec Kit, spec-driven development for coding agents (S24) [V].
- Sep to Nov 2025: Cagan's prototyping series: purpose of prototypes, FDEs, prototypes vs products (S2, S29, S27) [V].
- Apr 2026: Claude Design research preview with handoff to Claude Code (S13) [V]; Cagan "Build to Learn vs Build to Earn" (S28) [V].
- Jul 2026: Cagan "AI Productivity Paradox" (S30) [V]. Oct 2026: SVPG "Experimentation, AI and the Product Model" exists (not fetched) [U on content].
- Ongoing: NN/g position that synthetic users cannot replace real participants (S26) [V].
- Harness workflow to teach (book's): PM asks the harness, connected to the research repository and ticket system, to draft the test plan from the PRFAQ's riskiest assumptions; pilot the script against a synthetic participant only to find confusing tasks; transcribe and cluster sessions; draft the readout with counts and clips the PM verifies; draft the PRD from the readout and decision log. Every number in the readout is checked against recordings by a human.

## (e) Beacon worked-example ideas (consistent with beacon-case.md)
- **Risk question:** Will Dana, paged at 3 a.m., accept and act on an agent-proposed root cause with cited evidence within five minutes? Will Priya trust supervised remediation enough to approve a rollback through the approval gate? Will Sam approve the permissions model?
- **Prototype set for Beacon Agents (supervised remediation):**
  - Feasibility prototype (applied AI engineers): can the agent retrieve deploys and change tickets through existing MCP connectors and cite them within latency budget?
  - User prototype (designer plus PM using a design-to-code tool): the approval-gate screen showing root cause, evidence citations, proposed runbook step, blast radius, and approve or reject. Seeded with realistic incident data, never real customer data.
  - Wizard of Oz: in a design-partner session, an SRE on the Beacon team writes the "agent" diagnosis live behind the interface to test whether evidence format drives trust before the agent is good enough. Debrief afterward.
  - Live-data hybrid: run diagnosis on real past incidents from two design partners (live data, no live traffic, no actions executed) to measure diagnosis acceptance rate offline.
- **Usability test:** 5 on-call engineers (Dana role), 3 SRE leads (Priya), 3 security reviewers (Sam) on the permissions screen; moderated remote; think-aloud; tasks without UI labels. Success signal: at least 4 of 5 on-call engineers correctly decide approve or reject on seeded right and wrong diagnoses. Include a seeded wrong root cause (echo of the hallucinated-root-cause storyline) to test whether users catch it. Kill signal: users approve the wrong rollback.
- **Readout finding examples:** severity 4: evidence citations hidden behind a tab, 3 of 5 approved the seeded wrong diagnosis; severity 3: blast-radius language unclear to Sam.
- **Staffing plan:** Beacon has 3 PMs, 1 designer, about 35 engineers in 5 teams, 2 applied AI engineers. Proposal: Beacon Agents as a stream-aligned team with PM, designer (shared, a stated constraint), tech lead, 6 engineers, 1 applied AI engineer; connectors team as platform team (X-as-a-Service); evals capability as enabling team for one quarter; an FDE-style engineer embedded with design partners. Capacity: subtract on-call and Beacon Classic migration load. Flag the single designer as the binding constraint.
- **PRD:** Beacon Agents supervised remediation for Northlight Live launch; non-goals include fully autonomous actions beyond customer allowlist and MSP multi-tenant views (Leo) in v1; AI addendum pointing to Chapter 31 (evals for diagnosis acceptance, failure modes, inference cost per resolved incident given margin drop from 81% to 72%, EU AI Act documentation for EU customers).
- **PRFAQ contrast:** short PRFAQ headline for Northlight Live announcement, with internal FAQ on per-resolved-incident pricing and gross margin.
- **Prototype-vs-product moment:** a PM vibe-codes a slick approval screen and a sales leader wants to demo it to Marcus's peers; the PM explains what is missing (least-privilege access, audit logs, data residency: Sam's needs).

## (f) Editorial flags
- Hybrid prototype definition differs: SVPG 2014 blog (live data, no live traffic) vs book summaries of Inspired that include Wizard of Oz. Use Cagan's blog definition and treat WoZ separately.
- Krug details (three users, morning a month, "do the least you can do") are from secondary sources; confirm against Rocket Surgery Made Easy before quoting. Krug's quote not in the chosen five for that reason.
- Wizard of Oz origin: NN/g credits Norman and Munro 1973 and Kelley's naming in 1983; other sources say 1984 for Kelley's published paper. Use NN/g wording.
- Concierge MVP story (Food on the Table) checked only via Rosso's deck summary; Ries attribution [S].
- Working Backwards length limits (one-page PR, about five-page FAQ) not confirmed on a primary page; Bryar and Carr book year 2021 [S].
- Team Topologies second edition year [U].
- Lovable CVE details (scope, counts) vary across security-vendor sources; vendor disputes the CVE. Use carefully and factually, or omit the vendor name.
- Claude Design: "Figma stock fell 7%" [U], do not use. Product is a research preview; status may change by publication.
- Tool landscape moves monthly. Teach categories; any named tool should be dated "as of 2026."
- Product trio plus applied AI engineer is the book's extension, not Torres's.
- Templates (test plan, script, readout, staffing plan, PRD, one-page PRD) are the book's syntheses; the chapter must present them as Product 360 templates, not as any single author's.
- Web search budget ran out during research; Working Backwards length guidance, Krug primary text, and SVPG "Build To Learn FAQ" and "Experimentation, AI and the Product Model" were not checked.
