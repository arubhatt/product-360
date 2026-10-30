# Product 360 Handbook: Grilling Session

This file holds every decision I need before I write the book. Each question has a recommended answer. Edit any **Your answer** line you disagree with, add notes anywhere, and send the file back. Anything you leave untouched, I'll treat as accepted.

Quick context from my prep work:

- I read the structure of [The AI Founder's Handbook](https://arubhatt.github.io/ai-founders-handbook/): plain static HTML, a left sidebar grouped by parts, two-digit chapter numbers, `/` search, a dark mode toggle, a PDF download, and a "series" label.
- I read the [eCornell Product Management 360 certificate](https://ecornell.cornell.edu/certificates/engineering/product-management-360/). It has 14 core courses, a 6-course Product Management elective track (your screenshot), and a 6-course Technical Product Management elective track.
- Your `gh` CLI is logged in to `sqbu-github.cisco.com` (Cisco Enterprise GitHub) and not to `github.com`. That affects Section F.

How to answer: edit the text after **Your answer:**. For multi-choice questions, delete the options you don't want or write your own.

---

## A. Audience, purpose and voice

### A1. Who is the primary reader?

The book can't be pitched at an APM and a CPO at the same time without losing one of them.

- (a) New PMs (0 to 3 years)
- (b) Senior PM to Principal/Group PM, with short on-ramps for newer PMs
- (c) Product leaders (Director, VP, CPO)

**Recommended:** (b). The "build your Product 360 for your surface area" goal is a Principal PM's job. On-ramp boxes keep newer PMs from getting lost, and leadership sidebars cover portfolio and org topics.

**Your answer:** (b)

### A2. What product context should the examples assume?

- (a) B2B enterprise and platform products (SaaS, infrastructure, collaboration, security)
- (b) Consumer products
- (c) Neutral, with a mix

**Recommended:** (a) as the default, with consumer examples where the concept is clearer in consumer (growth loops, pricing psychology, A/B testing at scale).

**Your answer:** (a)

### A3. Should the book contain anything specific to your employer?

**Recommended:** No. The book stays fully public-safe: no internal processes, product names, roadmaps, metrics or terminology from Cisco or any other employer. Real companies appear only through public case studies. I'll also avoid anything that could read as an official Cisco publication.

**Your answer:** No

### A4. What voice should the book use?

**Recommended:** A practitioner's voice. Second person ("you"), direct and opinionated where the evidence supports it, short on theory recaps and long on how to apply it. Your voice profile (candid, curious, occasional humor) guides the prose, toned for a textbook rather than a post. Every chapter goes through your `check` skill with the `strong` control.

**Your answer:** As recommended

### A5. Title, subtitle, byline and series label

**Recommended:**

- Title: **The Product 360 Handbook**
- Subtitle: **Building, Running and Governing Products in the AI Era**
- Tagline: **A field guide and operating system for product leaders, 2026 edition**
- Byline: **Curated by Arunabh Bhattacharjee** (matches the AI Founder's Handbook)
- Series label: **Product Leadership Series** (the AI Founder's Handbook uses "Startup Bootcamp Series")

**Your answer:** As recommended

### A6. How should the book relate to the eCornell course?

this book has nothing to do with the Cornell course except for taking the outline and topics as an ideation

**Recommended:** you don't have to mention the course nor refer to it. It is merely an outline that is used for Product 360. You should also take other topics that were not mentioned here and add them to the textbook as high-level items

**Your answer:** As recommended

---

## B. Scope and structure

### B1. Overall ordering principle

- (a) Follow the certificate order: PM track, then TPM track, then core courses
- (b) Follow the product lifecycle: discover, define, build, launch, operate, retire
- (c) Hybrid: start with the PM track (as you asked), then group everything else by lifecycle and discipline

**Recommended:** (c). Starting with the six PM-track chapters satisfies your brief. After that, lifecycle grouping reads better than the certificate's order, which puts Excel first and persuasive writing last.

**Your answer:** (c)

### B2. Should there be a framework chapter before the PM track?

**Recommended:** Yes. Chapter 00, "The Product 360 Framework," defines the model the whole book hangs on: the 360 dimensions (customer, strategy, business, build, go-to-market, operate, lifecycle, AI, leadership), the artifact stack, the operating cadence, and how a PM uses the book to build their own 360. The capstone chapter at the end walks through building one from scratch.

**Your answer:** Yes

### B3. Proposed table of contents

This is the draft. Rename, merge, cut, reorder, or add chapters directly in the list.

**Front matter**

- Preface: How to use this book
- 00 The Product 360 Framework

**Part I: Product Management**

- 01 Developing a Product Hypothesis and Personas (problem framing, JTBD, journey maps, discovery interviews, opportunity solution trees)
- 02 Product Vision and Goals (vision, mission, North Star, metric trees, OKRs)
- 03 Building a Product Strategy and Roadmap (strategy kernels, prioritization frameworks, backlog, outcome roadmaps)
- 04 Product Prototyping (fidelity ladder, AI prototyping tools, usability testing, staffing, the PRD)
- 05 Product Analytics and Iteration (instrumentation, funnels, retention, experiments, iteration loops)
- 06 Product Engineering and Execution (working with engineering, sprints, user stories, issue management, technical debt)

**Part II: Technical Product Management**

- 07 Navigating Technical Product Management (why products fail, the development process, AI-assisted analysis and A/B testing)
- 08 Developing a Data-Driven Product Strategy (marketing metrics, journey design, attribution)
- 09 Optimizing Product Strategy Using Analytics (survival analysis, CLV, sentiment analysis)
- 10 Consumer Insights and Product Specifications (decision psychology, specs, relaunches)
- 11 Delivery Methodologies (waterfall, Agile, Scrum, Kanban, Shape Up, dual-track, RICE and alternatives)
- 12 Creating a Compelling Value Offering (DCF, value-based pricing across the lifecycle, behavioral pricing)

**Part III: Business and Market Strategy**

- 13 Market Sizing, Competitive Analysis and the Business Case
- 14 Digital Platform Strategy and Network Effects
- 15 Pricing and Packaging Strategy
- 16 Defensibility and Moats

**Part IV: Data-Driven Decisions in the AI Era**

No syntax in this part: no SQL, no Excel formulas, no Tableau clicks. It assumes an AI harness does the querying, modeling and charting, and teaches what a product leader needs instead: the right questions, the right data, and the right reports.

- 17 The Questions That Drive Product Decisions (decision types by lifecycle stage, a question bank per decision, what evidence answers each question, how to tell a good question from a vanity question)
- 18 The Product Data Landscape and the Reports That Matter (data sources across telemetry, CRM, billing, support, surveys, market and competitive data; the standard report set, and the questions each report must answer; worked examples)
- 19 AI-Native Analysis: Collecting Data and Asking the Harness (how to collect and permission the data, connectors and MCP servers, passing context into Claude or another harness, analysis and report prompts, checking AI-generated numbers, turning answers into decisions)

These three chapters cover the Cornell spreadsheet, SQL and visualization courses at the level of decisions rather than tools. The same rule applies to Chapter 07: "Python for PMs" becomes "AI-assisted analysis and experimentation."

**Part V: Innovation**

- 20 Innovation Strategy and the Innovation Placemat
- 21 Innovation Competencies: Lean Startup, Design Thinking and Maker Culture
- 22 The Innovation Toolkit (hackathons, incubators, partnerships, M&A and others)
- 23 Implementing, Evaluating and Scaling Innovation (stakeholders, teams, portfolios, sustaining)

**Part VI: Go-to-Market: Offers, Announcements and Events**

- 24 Positioning, Messaging and the Offer
- 25 Launch Management (launch tiers, readiness, beta and early access, announcements)
- 26 Events, Keynotes and Demos
- 27 Sales Enablement, Customer Success and the Feedback Loop

**Part VII: Product Operations and Lifecycle Management**

- 28 Product Operations (cadences, rituals, decision rights, tooling, data)
- 29 Governance and Business Reviews (portfolio reviews, QBR/MBR, metric reviews, decision logs)
- 30 Product Lifecycle Management (stage gates, maturity, sunsetting, end-of-sale and end-of-life)

**Part VIII: AI-Era Product Management**

- 31 Building AI-Powered Products (AI PRDs, evals, agents, cost, latency, trust and UX)
- 32 The AI-Augmented Product Manager (AI workflows across every PM task)
- 33 Responsible AI and Regulation for PMs (EU AI Act, NIST AI RMF, ISO/IEC 42001)

**Part IX: Influence and Leadership**

- 34 Persuasive Writing for PMs (narratives, PRFAQs, one-pagers, proposals, email)
- 35 Presentations and Executive Communication
- 36 Stakeholder Management and Product Leadership

**Capstone**

- 37 Building Your Product 360: an end-to-end playbook for taking over a product surface area (first 30/60/90 days, the asset build order, the operating cadence)

**Appendices**

- A. Artifact Library (every template in one place)
- B. Prompt Library (every prompt in one place)
- C. Product 360 Maturity Model and Self-Assessment
- D. Glossary

**Recommended:** This is okay but you should also do some online research and find out what is missing in product management for principal product managers that need to be here. 

**Your answer:** As recommended

### B4. Standard chapter template

Every chapter would follow the same skeleton so the book works as a reference:

1. **Why this matters** (the job this chapter helps you do)
2. **Core concepts and frameworks** (attributed to the best thinkers on the topic)
3. **How to apply it** (step-by-step method)
4. **The AI lens, 2026** (what changes when the product is AI-powered, and what AI changes about doing the work)
5. **Worked example** (the running case, see B6)
6. **Product 360 artifacts** (the templates this chapter produces, ready to copy)
7. **AI prompts** (copy-ready prompts for this chapter's tasks)
8. **Anti-patterns** (common failure modes)
9. **Checklist** (what "done" looks like)
10. **Key takeaways**

**Recommended:** Use this template. Sections can flex when a topic needs it, but artifacts, prompts and checklist are required in every chapter.

**Your answer:** As recommended

### B5. Chapter depth

38 chapters plus appendices is a big book. Depth sets the quality and the time it takes.

- (a) Compact: about 2,500 words per chapter (about 100k words total)
- (b) Standard: about 4,000 to 6,000 words per chapter plus templates (about 180k words total)
- (c) Deep: 8,000+ words per chapter

**Recommended:** (b). It's deep enough to be the textbook, and still readable as a reference. Some chapters (00, 03, 31, 37) will run longer.

**Your answer:** (b)

### B6. Running example

A single product carried through every chapter makes the 360 concrete.

**Recommended:** A fictional B2B AI product used in every chapter: **"Beacon," an AI agent platform that helps IT and operations teams detect, diagnose and resolve incidents**. It's enterprise, platform-shaped, AI-native, and has pricing, partner, launch and lifecycle stories to tell. It isn't a real Cisco product. Short secondary examples (consumer app, hardware-plus-software, internal platform) appear where the main case doesn't fit.

**Your answer:** As recommended

### B7. Which artifacts must the book include?

You asked for every artifact needed to govern strategy, execution, feature development, offers and events, product ops and lifecycle. Here's my list. Delete anything you don't want and add anything missing.

**Customer and discovery:** problem hypothesis, persona, JTBD statement, customer journey map, interview guide, discovery synthesis, opportunity solution tree, voice-of-customer report.

**Vision and strategy:** product vision statement, vision narrative, strategy one-pager, strategy kernel (diagnosis, guiding policy, actions), market sizing (TAM/SAM/SOM), competitive landscape, competitive battlecard, SWOT, business case, unit economics model, pricing and packaging proposal, platform and ecosystem map, North Star and metric tree, OKRs.

**Planning and prioritization:** prioritization scorecard, opportunity assessment, now/next/later roadmap, theme-based roadmap, release plan, capacity plan, dependency map.

**Definition and build:** PRD, one-page PRD, PRFAQ (Amazon working backwards), AI PRD addendum (eval spec, model and vendor selection, data needs, guardrails), user story and acceptance criteria, story map, prototype test plan, technical design review checklist, definition of ready and done.

**Measurement:** instrumentation and event spec, dashboard spec, experiment design doc, A/B test readout, post-launch review, iteration plan.

**Go-to-market:** positioning statement, messaging framework, offer definition, launch tier matrix, launch plan, launch readiness checklist, beta and early access program plan, announcement blog post, press release, customer FAQ, internal FAQ, sales enablement kit, pitch deck outline, demo script, event and keynote plan, partner enablement plan, win/loss analysis.

**Operations and governance:** product operating cadence calendar, weekly business review, monthly and quarterly business review deck, portfolio review, decision log, DACI/RACI, risk register, stakeholder map, communication plan, product ops tool stack map.

**Lifecycle:** stage-gate criteria, product lifecycle stage assessment, sunset and end-of-life plan, end-of-sale notice, migration plan, deprecation communication plan.

**AI and responsibility:** AI use-case assessment, eval plan, red-team plan, AI risk and impact assessment, model card, AI cost model, human-in-the-loop design, incident response plan for AI.

**Leadership:** 30/60/90 plan, Product 360 self-assessment, team charter.

**Recommended:** Include all of the above.

**Your answer:** As recommended

### B8. Templates format

**Recommended:** Templates appear inline in each chapter with a copy button, and each also exists as a standalone Markdown file in a `templates/` folder (downloadable from the Artifact Library page). Markdown pastes cleanly into Confluence, Notion, Google Docs and GitHub.

**Your answer:** As recommended

### B9. Product 360 operating system

**Recommended:** The book defines a recommended cadence (weekly, monthly, quarterly, annual) that tells the PM which artifact to update when, and who reviews it. Chapter 00 introduces it, Chapters 28 and 29 detail it, and Chapter 37 puts it in practice.

**Your answer:** As recommended

---

## C. AI-era content (2026)

### C1. How should AI show up in the book?

- (a) Only in a dedicated AI part
- (b) An "AI lens" section in every chapter, plus a dedicated AI part for depth

**Recommended:** (b). AI changes every part of the job in 2026, so it can't live only in one part.

**Your answer:** (b)

### C2. Prompt style

**Recommended:** Model-agnostic prompts that work in Claude, ChatGPT, Gemini or Copilot. Each prompt states its goal, the inputs to paste in, the prompt itself, and how to check the output. Where it helps, I'll include agent-style workflows (for example, "synthesize 20 interview transcripts into an opportunity solution tree") and notes on what to keep away from AI tools (confidential data, final decisions).

**Your answer:** As recommended

### C3. Naming tools and vendors

**Recommended:** Name tool categories first and give a few representative examples, labeled "as of late 2026." No rankings and no paid placement. This keeps the book useful after tools change.

**Your answer:** As recommended

### C4. Overlap with The AI Founder's Handbook

Some topics overlap (evals, model selection, AI unit economics, responsible AI).

**Recommended:** Cover them from the PM's angle and link to the AI Founder's Handbook for founder and infrastructure depth. Don't duplicate content.

**Your answer:** Duplicate the content,  because this book needs to be self-contained.  it cannot reference other books and other material and flip-flop readers between all of these different sites. It must be in one place.  

### C5. Regulation coverage

**Recommended:** Cover the EU AI Act (timeline and obligations as they stand in late 2026), NIST AI RMF, ISO/IEC 42001, and the general shape of US state laws, with a clear note that this isn't legal advice.

**Your answer:** As recommended

---

## D. Research, authors and references

### D1. Core authors and sources

I'll research each topic across the best practitioners and authors, using primary sources wherever possible. Here's the starting list. Strike anyone you don't trust and add anyone missing.

- **Product discovery and craft:** Marty Cagan (*Inspired*, *Empowered*, *Transformed*), Teresa Torres (*Continuous Discovery Habits*), Melissa Perri (*Escaping the Build Trap*), Dan Olsen (*The Lean Product Playbook*), Jeff Gothelf and Josh Seiden (*Lean UX*, *Outcomes Over Output*), Rob Fitzpatrick (*The Mom Test*)
- **Customer understanding:** Clayton Christensen and Bob Moesta (Jobs to Be Done), Tony Ulwick (Outcome-Driven Innovation), Indi Young (mental models), Alan Cooper (personas)
- **Strategy:** Richard Rumelt (*Good Strategy Bad Strategy*), A.G. Lafley and Roger Martin (*Playing to Win*), Hamilton Helmer (*7 Powers*), Geoffrey Moore (*Crossing the Chasm*), Gibson Biddle (DHM model)
- **Goals and metrics:** John Doerr (*Measure What Matters*), Christina Wodtke (*Radical Focus*), Amplitude North Star Playbook, Sean Ellis
- **Roadmaps and prioritization:** C. Todd Lombardo et al. (*Product Roadmaps Relaunched*), Roman Pichler, Intercom (RICE), Shreyas Doshi
- **Execution:** Jeff Patton (*User Story Mapping*), Mike Cohn, Ryan Singer (*Shape Up*), Donald Reinertsen (*Principles of Product Development Flow*), Henrik Kniberg
- **Analytics and experimentation:** Ron Kohavi, Diane Tang and Ya Xu (*Trustworthy Online Controlled Experiments*), Alistair Croll and Benjamin Yoskovitz (*Lean Analytics*), Reforge
- **Innovation:** Eric Ries (*The Lean Startup*), Steve Blank, IDEO and Stanford d.school (design thinking), Clayton Christensen (*The Innovator's Dilemma*), Scott Anthony
- **Platforms:** Geoffrey Parker, Marshall Van Alstyne and Sangeet Paul Choudary (*Platform Revolution*), NFX on network effects, Andrew Chen (*The Cold Start Problem*)
- **Pricing:** Madhavan Ramanujam and Georg Tacke (*Monetizing Innovation*), Patrick Campbell, Kyle Poyar, Hermann Simon
- **Go-to-market:** April Dunford (*Obviously Awesome*, *Sales Pitch*), Colin Bryar and Bill Carr (*Working Backwards*), Pragmatic Institute
- **Product ops and lifecycle:** Melissa Perri and Denise Tilles (*Product Operations*), Silicon Valley Product Group, PDMA body of knowledge
- **AI products:** Chip Huyen (*AI Engineering*), Hamel Husain and Shreya Shankar (evals), Ethan Mollick (*Co-Intelligence*), Google PAIR (*People + AI Guidebook*), Microsoft HAX guidelines, Anthropic and OpenAI published guidance
- **Communication:** Barbara Minto (*The Pyramid Principle*), Nancy Duarte (*Resonate*, *DataStory*), Cole Nussbaumer Knaflic (*Storytelling with Data*), Chip and Dan Heath (*Made to Stick*)
- **Practitioner writing:** Lenny Rachitsky, Shreyas Doshi, John Cutler, Ken Norton, Julie Zhuo, Ben Horowitz ("Good Product Manager, Bad Product Manager")

**Recommended:** Use this list as the core, and add primary research (HBR, academic papers, company engineering and product blogs) per topic.

**Your answer:** As recommended

### D2. Quoting and attribution in the book

**Recommended:** Paraphrase and attribute by name inside the text ("Teresa Torres calls this an opportunity solution tree"). Direct quotes stay short and rare. Full citations live only in `REFERENCES.md`, as you asked, with no footnotes or link lists in the chapters.

**Your answer:** As recommended

### D3. REFERENCES.md format

**Recommended:** One `REFERENCES.md` at the repo root, grouped by chapter. Each entry gives author, title, publisher or site, year, URL, and a one-line note on what I used it for. A "Further reading" shortlist per chapter tops each group.

**Your answer:** As recommended

### D4. Research and writing approach (this one has a real cost)

Researching and writing about 38 chapters at this quality is a lot of work. The fastest path is a multi-agent workflow where parallel agents research and draft chapters while I set the standard, integrate and edit. That uses a large number of tokens.

- (a) Multi-agent workflow: parallel research and drafting per part, then my integration and `check` pass on every chapter. Fastest, highest token use.
- (b) I write chapters one at a time in this session. Slower and more consistent, still large token use.

**Recommended:** (a), but only after a pilot (see G1) locks the quality bar, so every agent writes against approved examples.

**Your answer:** (a)

---

## E. Site design and tech

### E1. Architecture

**Recommended:** The same approach as the AI Founder's Handbook: plain static HTML, CSS and JavaScript, no framework, opens straight from the file system, deploys to GitHub Pages without a build step on GitHub. I author chapters in Markdown and a small Python script generates the HTML pages, search index and PDF, so edits later are easy.

**Your answer:** As recommended

### E2. Visual design

- (a) Reuse the AI Founder's Handbook design exactly, so the two books look like one series
- (b) The same layout and features, with its own color accent and identity

**Recommended:** (b). Same reading experience and series feel, different accent color so readers can tell the books apart.

**Your answer:**  Actually think about the design deeply, take the best design for a dark mode textbook, and do it. You don't have to copy the entire design exactly. It could be completely new and the look and feel could be fresher but it needs to maintain its readability and its modern attractiveness.

### E3. Site features

Delete any you don't want.

- Left sidebar with parts and chapters, collapsible like your screenshot
- Per-chapter "on this page" outline
- Full-text search (`/` shortcut)
- Light and dark mode. Dark Mode by Default.
- Copy buttons on every template and prompt
- Interactive chapter checklists saved in your browser
- Previous and next chapter navigation
- Print styles and a full-book PDF download
- Inline SVG diagrams for the main frameworks (the 360 model, metric trees, lifecycle, launch tiers)
- Mobile layout

**Recommended:** All of the above.

**Your answer:** As recommended

### E4. Diagrams

**Recommended:** Hand-built high quality inline SVG diagrams, infographic, about two / three / four per chapter where a picture explains the framework better than text. No stock images.

**Your answer:** As recommended

---

## F. Git, GitHub and hosting

### F1. Which GitHub?

You said "private for now, available on github.com eventually." Your `gh` CLI is only logged in to Cisco's `sqbu-github.cisco.com`. Pushing a personal book there would put it inside Cisco's enterprise GitHub, which is probably not what you want for a personal publication.

- (a) A private repo on github.com under `arubhatt` (same account as the AI Founder's Handbook). You'll need to run `gh auth login --hostname github.com` once before I push.
- (b) Cisco's `sqbu-github.cisco.com`

**Recommended:** (a).

**Your answer:** (a)

### F2. Repo name and visibility

GitHub can't make a single branch private. Privacy is set at the repo level.

**Recommended:** A private repo named `product-360-handbook`, with the site on `main`. When you're ready to publish, you flip the repo to public and turn on GitHub Pages from `main`. Note that GitHub Pages on a private repo needs a paid GitHub plan, so on a free plan the site goes live only after the repo is public.

**Your answer:** As recommended

### F3. License

**Recommended:** Private, all rights reserved, for now. When you go public, CC BY-NC-SA 4.0 for the text and templates (people can share and adapt with credit, not sell). I'll add the license file but leave it switched to "all rights reserved" until you say so.

**Your answer:** As recommended

---

## G. Process and review

### G1. Pilot before full production

**Recommended:** Yes. I first build the site shell plus three pilot chapters: 00 (The Product 360 Framework), 01 (Developing a Product Hypothesis and Personas), and 31 (Building AI-Powered Products). You review them locally. Once you approve the quality, depth and tone, I produce the rest against them.

**Your answer:** Yes

### G2. How do you want to review?

**Recommended:** You open the local site in a browser (I'll start a local server), and send feedback in chat or as comments in a Markdown review file. Each part gets its own commit so changes are easy to trace.

**Your answer:** As recommended

### G3. Commit and push

**Recommended:** I commit and push after the pilot and after each completed part, all to the private repo from F1. Commit messages carry the standard Claude co-author line.

**Your answer:** As recommended

### G4. Anything I should know that I haven't asked?

For example: a product area you want the book to serve first, topics you've seen done badly elsewhere, chapters you care most about, a deadline, or people who will review it.

**Your answer:** I want you to generate some prompts in the last capstone section that I can use with either Harness or Claude. I'm able to create a detailed set of artifacts for the product of my choice by doing a detailed grilling session with the harness (with constant back and forth) and also giving you reference materials to look at to anchor all of that information 
