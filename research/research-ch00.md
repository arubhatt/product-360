# Research notes: Chapter 00, "The Product 360 Framework"

Prepared for *The Product 360 Handbook* (2026 edition). Research date: 30 October 2026. These are notes, not chapter prose.

Verification key used below:

- **[V]** I read it on the primary source (author's own site, publisher listing or official page).
- **[S]** Secondary source only. Check before printing.
- **[U]** Could not verify. Do not cite as fact.

---

## (a) Key concepts and frameworks

### 1. Defining the PM role and the product operating model

**Marty Cagan / SVPG: the product operating model** [V]
SVPG introduced the term "product operating model" in early 2023 and describes it as how the best tech-powered companies work, not as a methodology. The SVPG introduction (10 Feb 2023) frames the change along three dimensions:
- **How you build.** Small, frequent, dependable releases, at least every two weeks and ideally continuously.
- **How you solve problems.** Teams get problems to solve and outcomes to hit instead of feature lists. The PM, designer and engineers choose a solution that is valuable, usable, feasible and viable.
- **How you decide which problems to solve.** Product, design and technology leaders decide, using a customer-focused product vision and an insight-driven product strategy.

The page groups the model's principles into five areas: product culture (principles over process, trust over control, innovation over predictability, learning over failure), product strategy (focus, insight, transparency, quarterly bets), product teams (empowerment, outcomes over output, ownership, collaboration), product discovery and product delivery. *Transformed* (2024) turns these into a transformation playbook. Secondary summaries say the book has about 20 "product model principles"; I did not verify the count [S].
*How a PM applies it:* Use the three dimensions as a diagnostic. A team that ships quarterly, gets handed a roadmap of features and has strategy set by sales is still in the "prior model" (Cagan's term) on all three.

**Cagan: the four product risks** [V]
Value (will customers buy or choose it), usability (can users work out how to use it), feasibility (can we build it with the time, skills and technology we have) and viability (does it work for the business: legal, finance, go-to-market, compliance, ethics). Cagan's first version had three risks. The second edition of *Inspired* (Wiley, December 2017; often cited as 2018) split value into customer value and business viability ("Product Risk Taxonomy," SVPG, 10 July 2023). SVPG's 2023 operating-model introduction gives each risk an owner: the PM owns value and viability, the designer owns usability and the tech lead owns feasibility.
*How a PM applies it:* Before committing delivery capacity, tag every major bet with its riskiest of the four and name the discovery work that retires it. For B2B enterprise, viability usually carries the hidden risk (security review, contract terms, partner channel, pricing).

**Cagan's 2025 and 2026 role definitions** [V]
- "The Era of the Product Creator" (27 May 2025): a product creator is anyone actively shaping the product and taking on the four risks, whatever their title. Cagan says the PM job is not facilitation, project management or backlog administration, and that PMs who do not create product are exposed to generative AI.
- "A Fresh Definition of the Product Role" (10 Aug 2026): Cagan borrows three skills from Benedict Evans: seeing the broader problem behind a pain point, finding a solution users will value, and knowing the company well enough to make that solution viable. He maps them to problem discovery, value risk and viability risk. He also says his 2025 "product creator" piece was too optimistic: new tools have not turned many more people into strong product creators.

**Ben Horowitz: "Good Product Manager/Bad Product Manager"** [V for posting date; S for origin]
a16z posted it on 15 June 2012. The page calls it a training document written about 15 years earlier, which puts it in the mid to late 1990s. Secondary sources tie it to Horowitz's time at Netscape and some add David Weiden as co-author; the a16z page credits Horowitz alone [S]. Its main contrasts: the good PM acts as "CEO of the product" and owns the result without excuses; defines the *what* and leaves the *how* to engineering; writes things down; shapes the narrative for the press and the market; and breaks problems into parts. The bad PM blames resources, slides into project management, and argues verbally instead of in writing.
*How a PM applies it:* It works as a behavioral checklist for self-review. Critics argue that "CEO of the product" overstates the PM's authority, since nobody reports to a PM. Pair it with Norton's influence-based framing.

**Ken Norton: "How to Hire a Product Manager"** [V]
Published 14 June 2005, updated 2023, with retrospectives in November 2015 and 9 June 2025. Norton describes the PM as the advocate for whoever is not in the room (customers, engineering, sales, executives) who leads by influence without direct reports. He hires for raw intelligence, a technical background (with the warning that ex-engineers must stop making the technical decisions), product instincts ("spidey-sense"), leadership earned from peers, comfort with several functional perspectives, and shipping experience. In the 2025 retrospective he drops brainteasers, adds designers to the core team, notes the original never says "listen," and argues the human parts of the job are the least likely to be automated by AI.

**Shreyas Doshi: LNO and the three levels of product work** [S]
- *LNO* (Twitter thread, about 1 Feb 2020, per Aakash Gupta's write-up): sort tasks into **Leverage** (about 10x return on effort; give them your best time), **Neutral** (roughly 1x return; do them well enough) and **Overhead** (low return; do them quickly or delegate). Gupta flags a common error: treating Neutral work as Leverage because of perfectionism.
- *Three levels of product work* (workshop notes live-tweeted by swyx, Feb 2022, plus Doshi's own threads): **Impact** (effectiveness, outcomes), **Execution** (getting things done, outputs) and **Optics** (how the work is perceived). Doshi says each person has a default ranking. His related claim, that most execution problems are really strategy problems, comes from his Lenny's Podcast appearance [S].
*How a PM applies it:* LNO is a weekly triage on the calendar. The three levels help in disagreements: when two leaders disagree, check whether they are arguing at different levels, for example one about impact and the other about optics.
*Flag:* I could not retrieve Doshi's original threads. Cite the podcast or a captured thread URL, not the secondary summaries.

**Melissa Perri: the build trap and the Product Kata** [V book; S definitions]
*Escaping the Build Trap* (O'Reilly, November 2018). The build trap is when an organization measures success by output (features shipped) instead of outcomes (customer and business value). The **Product Kata**, adapted from Toyota's Improvement Kata, runs as a loop: understand the direction or challenge, analyze the current condition, set the next target condition, then choose and run experiments (steps), comparing what was expected with what was learned. Repeat. Perri's 22 July 2015 blog post names the elements Direction/Challenge, Target Condition, Obstacle, Current Condition, Step, Expected and Learned [V]. I could not open the book's chapter 15 (O'Reilly returned a 403), so the book's exact step wording is [U].

**Lenny Rachitsky on PM roles and levels** [V partial]
- "Product management career ladders" (24 May 2022) reviews ladders from 20+ companies. Free-preview takeaways: about two-thirds of companies have both an IC track and a manager track, and the split usually happens around L6, Senior PM. The level definitions are behind the paywall [U].
- His post on the senior PM role lists three paths after senior IC: senior IC (Principal), manager of PMs (usually "Group PM" or "Product Lead") and manager of managers (Director) [S, snippet only].
- 2026 position: in his Lenny & Friends Summit write-up (29 Sep 2026), Lenny argues the PM job is expanding, not disappearing. The PM, engineering and design roles are not collapsing into one "builder"; each is growing [V].

**Principal PM and Group PM scope** [S]
No authoritative cross-industry standard exists. Common patterns in career-guide sources:
- *Principal PM*: senior IC, often the top IC rung. Scope covers a product area or initiatives that cross several teams; influence comes from strategy, technical depth and cross-org alignment, not reporting lines. Placement on the ladder varies: one source puts Principal mid-ladder at Amazon, below Director, and says Group PM follows Principal at Microsoft [S].
- *Group PM*: first people-manager rung. A player-coach who leads several PMs across a portfolio. Leverage shifts from the PM's own output to the output of the PMs they manage.
- *Reforge*: its PM Competency Model, built with Ravi Mehta (Reforge blog, 13 Feb 2024), has 12 competencies. The commonly cited four groups (Product Execution, Customer Insight, Product Strategy, Influencing People) appear only in an image on the page, so the grouping is [U] until checked against Reforge course material or ravi-mehta.com.
*Recommendation:* In the book, define Principal and Group PM scope in your own terms (breadth of portfolio, time horizon, artifacts owned) and present company ladders as illustrations, not as a standard.

### 2. Holistic PM frameworks that resemble a "360"

**Pragmatic Institute Framework** [V]
Formerly the Pragmatic Marketing Framework. It has 37 boxes in seven categories: Market, Focus, Business, Planning, Programs, Enablement and Support. Market-facing boxes include Market Problems, Win/Loss Analysis, Distinctive Competencies, Competitive Landscape and Asset Assessment; Business includes Business Plan, Pricing, Buy/Build/Partner and Product Profitability. Secondary sources say the strategic boxes sit to the left (upper half on some versions) and the execution boxes to the right [S]. Its premise is market-driven: start from validated market problems, not from the technology.
*Closest analog to "Product 360":* Pragmatic is the strongest precedent for a full map of PM responsibilities, especially its go-to-market and enablement boxes. Product 360 differs because it adds AI and leadership dimensions and an operating cadence.

**AIPMM ProdBOK** [V]
*The Guide to the Product Management and Marketing Body of Knowledge (ProdBOK Guide)*, sponsored by AIPMM, first edition 2013 (Greg Geracie, editor). I found no later edition [U]. It is a PMBOK-style lifecycle reference.

**ISO/IEC 20926: CORRECTION** [V]
ISO/IEC 20926:2009 is *Software and systems engineering: Software measurement: IFPUG functional size measurement method 2009* (function points). It is **not** a product management standard. Do not cite it as one. Better-fitting standards bodies or bodies of knowledge:
- **ISPMA SPMBOK** (International Software Product Management Association). Reference framework with Product Strategy and Product Planning at its core, plus Development, Marketing, Sales and Distribution, and Service and Support. Study guide by Kittlaus and Fricker (Springer, 2017) [V for book; S for structure].
- ISO 56000-series (innovation management) could be mentioned as context, but I did not research it [U].

**PDMA Body of Knowledge** [V]
*Product Development and Management Body of Knowledge*, 3rd edition (Wiley), the basis of the NPDP certification. Seven areas: Management, Strategy, Portfolio, Process, Design and Development, Market Research, and Culture and Teams. Earlier editions used a different seven (including Tools and Metrics and Lifecycle Management). Cite the 3rd edition list.

**Martin Eriksson: the product management Venn diagram** [V]
"What, exactly, is a Product Manager?" (Mind the Product, 5 Oct 2011). Product management sits where **Business**, **Technology** and **User Experience** overlap. A good PM has deep experience in at least one, passion for all three, and can talk fluently with specialists in each. In a 2021 conversation with Matt LeMay, Eriksson said the model still holds ten years later. Lenny's 2026 summit write-up refers to the same Venn diagram when arguing that the circles are not collapsing [V].

**Dan Schmidt: the Product Management Triangle** [S]
Corners: the **product**, **developers**, **users** (customers) and **the business**. The PM's job is to fill the white space between them: developers and users (how each experiences the product), users and business (turning user value into revenue) and developers and business (allocating technical cost against business value). I could not find the original post or its date (usually given as around 2014) [U]. Cite through a stable secondary source or leave the date out.

**Amazon Working Backwards (PR/FAQ)** [S, documented in Bryar and Carr 2021]
Before building, the team writes a press release for the finished product (about one page, focused on customer value) and an FAQ covering hard customer, business and execution questions. Ian McAllister's Quora answer is the best-known public description: iterating on a press release is cheaper and faster than iterating on the product. Sources date that answer to 2010, 2011 or 2012 [U]; a mirror exists from July 2011, so it was posted no later than mid-2011. Colin Bryar and Bill Carr, *Working Backwards* (St. Martin's Press, 2021), give the canonical account. One secondary source says Amazon developed the process mainly in 2004 to 2007 [S].
*How a PM applies it:* Use the PR/FAQ as the entry gate to the artifact stack. In B2B, write the FAQ for the buyer, the admin and the security reviewer, not only the end user.

**Robert G. Cooper: Stage-Gate** [S]
Developed in the mid-1980s from Cooper's research on new-product success. Work moves through stages (discovery or scoping, business case, development, testing, launch) separated by gates where a governance group decides go, kill, hold or recycle, using agreed criteria. The most-cited formal description is Cooper, "Stage-gate systems: A new tool for managing new products," *Business Horizons* 33(3), 1990, pp. 44 to 54. Later versions add agile-stage hybrids, voice of the customer and spiral development. The trademark and exact origin year are [U] (sources say 1986 or 1988).
*How a PM applies it:* In enterprise and hardware-adjacent platforms, gates map onto portfolio reviews. The risk is gates that judge documents instead of evidence, which is the build trap with extra paperwork.

### 3. Product operating cadences and governance

**Amazon Weekly Business Review (WBR)** [S; Commoncog's account of Bryar and Carr and of Bryar interviews]
- Purpose: what did customers experience last week, how did the business do, and are we on track to hit plan.
- Rhythm: data refreshes Sunday night; metric owners review on Monday; departmental WBRs on Tuesday; the company WBR on Wednesday (60 minutes, 90 in peak season), with roughly 400 to 500 metrics, run by finance.
- Format: the same deck every week (6-12 graphs: trailing six weeks plus trailing twelve months against the prior year and the plan). Owners skip normal variation and explain exceptions; "I don't know" gets a logged follow-up. Strategy debates are out of scope.
- **Controllable input metrics vs output metrics.** Inputs, such as selection, price, in-stock rate and delivery speed, are what teams can move directly. Outputs, such as revenue and free cash flow, are reported but not "managed." Teams refine their inputs by trial and error until they correlate with the outputs (Bryar and Carr's in-stock example).
- The process is fractal: the same review runs at company, department and team level.

**Amazon annual planning: OP1, OP2 and S-team goals** [S]
OP1 is the bottom-up operating plan drafted in late summer and fall. OP2 is the revision after the holiday quarter, finalized in January, and becomes the plan of record. Leadership picks a subset of each team's goals as S-team goals (the book's example: 6 of a team's 23), which finance tracks green, yellow or red each quarter. Goals are mostly input-focused and deliberately aggressive (Commoncog reports about 75% expected to be met fully). Plans and proposals are written as six-page narratives read in silence at the start of the meeting. One blog calls OP2 a mid-year review; the book-based sources contradict that, so do not use it.

**QBRs, strategy reviews and portfolio reviews** [general practice; no single originator]
Quarterly business reviews appear in two forms: internal (business or product line against plan) and customer-facing (account health and value delivered, common in B2B SaaS customer success). Cagan's model treats product strategy as a portfolio of quarterly bets, so the quarterly review is where strategy and team objectives get reset [V for the SVPG principle]. I found no authoritative primary source for a standard QBR format. Present it as a synthesis.

**Product operations: Perri and Tilles** [V book; S pillar wording]
*Product Operations: How Successful Companies Build Better Products at Scale* (Produx Labs, 2023). Pillar names differ across sources:
- Book and retailer description: **Data and Insights**; **Customer and Market Insights**; **Process and Governance**.
- Author interviews: "Business and Data Insights," and in one case "Process and Practices."
*Recommendation:* cite the publisher wording and note the variant. The purpose of product ops is to raise the speed and quality of product decisions. It is not a PMO.
Cagan (21 Oct 2026) says product ops "did not take" the experimentation direction, and proposes a separate "experimentation ops" function [V].

**Decision records: DACI (Atlassian Team Playbook)** [V]
Roles: **Driver** (one person, runs the process), **Approver** (one person, makes the final call), **Contributors** (provide expertise; advise but do not vote) and **Informed** (told after the decision). The Confluence template records status, impact, due date, background, relevant data, decision factors, options considered (with pros, cons and cost), action items and outcome. Atlassian advises using it for big cross-team decisions, not small ones. Compared with RACI, DACI requires a single approver. Atlassian does not say who invented DACI; attributions to Intuit in the 1980s are [U]. Atlassian also cites a McKinsey figure of a 25% higher success rate, which I could not trace [U].
*Decision log:* combine DACI pages with an index (date, decision, approver, link, revisit date). This combination is a synthesis, not a named framework.

### 4. The AI shift, 2025 to 2026 (dated statements)

| Date | Source | Claim |
|---|---|---|
| 25 Feb 2025 | Cagan, "A Vision for Product Teams" [V] | Over 3 to 10 years, typical teams shrink from about 8 people (PM, designer, about 6 engineers) to about 3 (PM, designer, engineer). Delivery is largely automated and discovery becomes the main activity. Each team owns a broader scope with less cross-team coordination. Product owners and feature-team PMs are at the most risk. |
| 27 May 2025 | Cagan, "The Era of the Product Creator" [V] | "Product creator" is defined by work (owning the four risks), not by title. Non-creator PMs will be left behind. |
| 9 Jun 2025 | Norton, HTHAPM 20-year retrospective [V] | The human parts of PM are the least likely to be automated. |
| 7 Nov 2025 | Cagan, "Prototypes vs Products" [V] | AI prototyping tools (Lovable, Bolt, Figma Make) are for building to learn. Professional tools (Claude Code, Cursor) are for building to earn. A high-fidelity prototype is not a near-finished product, especially in enterprise, which can involve thousands of use cases plus security, compliance, telemetry and scale. Cagan doubts code generation closes this gap within 3 to 5 years. |
| 23 Dec 2025 | Segal and Rachitsky, AI productivity survey (n = 1,750) [V] | PMs' top AI uses: writing PRDs (21.5%), mockups and prototypes (19.8%), communication (18.5%). User research is at 4.7% and roadmap ideas at 1.1%. 63% of PMs save 4+ hours a week. 44.4% want to use AI for prototyping next, the most-wanted future use. AI helps PMs produce outputs more than it helps them think upstream. |
| 16 Apr 2026 | Cagan, "Build to Learn vs Build to Earn" [V] | Building is no longer the bottleneck; discovering a solution worth building is. Cheap prototypes allow live-data testing and several approaches tested in parallel. |
| 23 Jul 2026 | Cagan, "The AI Productivity Paradox" [V] | Teams that use AI to speed up an output-focused model ship more without better outcomes. Strong product companies pull further ahead. |
| 10 Aug 2026 | Cagan, "A Fresh Definition of the Product Role" [V] | The hard part was never the code. It is knowing what should exist. His 2025 optimism about product creators was too high. |
| 29 Sep 2026 | Rachitsky, Lenny & Friends Summit write-up [V] | The PM role is expanding, not merging into one "builder." Speakers (Ramp, Lovable, Google Search, Linear, Stripe) described PMs taking GM-style business ownership, PMs prototyping and shipping, and judgment and taste becoming the differentiator. They did not agree on whether roadmaps are obsolete or whether PMs should ship to production. |
| 21 Oct 2026 | Cagan, "Experimentation, AI and the Product Model" [V] | AI products are probabilistic, so evals become a core quality practice, and quantitative tests cost more and age faster. Experimentation should be a core competency with a hybrid staffing model. |

Industry signal [S]: LinkedIn reportedly replaced its APM program with a "Product Builder" program that trains generalists across product, design and engineering. I did not verify this on LinkedIn's own site.

---

## (b) Verified facts with URL

1. SVPG's product operating model introduction (10 Feb 2023) defines three dimensions of change and five principle areas, and assigns risk ownership by role. https://svpg.com/the-product-operating-model-an-introduction/
2. Cagan first used "product operating model" as a term on 3 Mar 2023. https://svpg.com/the-product-operating-model/
3. The four risks, and how value was later split into value and viability (10 Jul 2023). https://svpg.com/product-risk-taxonomies
4. *Inspired* 2nd edition, Wiley, published 12 Dec 2017 (1st edition 2008). https://bookshop.org/p/books/inspired-how-to-create-tech-products-customers-love-marty-cagan/8599213
5. *Empowered*, Cagan with Chris Jones, Wiley, December 2020. https://www.oreilly.com/library/view/empowered-ordinary-people/9781119691297/
6. *Transformed*, Cagan with Lea Hickman, Christian Idiodi, Chris Jones and Jon Moore, Wiley, 12 Mar 2024, ISBN 9781119697336. https://porchlightbooks.com/product/transformed-moving-to-the-product-operating-model--marty-cagan/isbn/9781119697336
7. Horowitz essay posted on a16z on 15 Jun 2012. The page says it was written about 15 years earlier. https://a16z.com/good-product-manager-bad-product-manager/
8. Norton's essay was first published 14 Jun 2005; the 20-year retrospective is dated 9 Jun 2025. https://www.bringthedonuts.com/essays/productmanager.html and https://www.bringthedonuts.com/essays/how-to-hire-a-pm-retrospective/
9. Eriksson's Venn diagram article, 5 Oct 2011: Business, Technology, UX. https://www.mindtheproduct.com/what-exactly-is-a-product-manager/
10. ISO/IEC 20926:2009 is the IFPUG functional size measurement method, not a PM standard. https://www.iso.org/standard/51717.html
11. AIPMM ProdBOK Guide, first edition 2013. https://aipmm.com/about
12. Pragmatic Framework: 37 boxes in 7 categories. https://www.pragmaticinstitute.com/product/framework/
13. PDMA BoK 3rd edition: seven topic areas. https://www.oreilly.com/library/view/-/9781119829942/
14. *Escaping the Build Trap*, O'Reilly, November 2018. https://oreilly.com/library/view/escaping-the-build/9781491973783
15. Perri's Product Kata blog post (22 Jul 2015) and its element names. https://melissaperri.com/blog/2015/07/22/the-product-kata
16. Lenny's PM career ladder analysis (24 May 2022): about two-thirds of companies have dual tracks, and the split usually comes at Senior PM (L6). https://www.lennysnewsletter.com/p/product-management-career-ladders
17. Reforge PM Competency Model with Ravi Mehta: 12 competencies (13 Feb 2024). https://www.reforge.com/blog/maximize-the-performance-of-your-product-managers
18. DACI roles and template fields. https://www.atlassian.com/team-playbook/plays/daci
19. Lenny & Friends Summit write-up, 29 Sep 2026: "The PM job is expanding, not disappearing." https://www.lennysnewsletter.com/p/all-of-the-lenny-and-friends-summit
20. AI productivity survey, 23 Dec 2025, n = 1,750, with the PM figures above. https://lennysnewsletter.com/p/ai-tools-are-overdelivering-results
21. Cagan, "A Vision for Product Teams," 25 Feb 2025 (team of about 8 shrinking to about 3). https://www.svpg.com/a-vision-for-product-teams/
22. Cagan, "The Era of the Product Creator," 27 May 2025. https://www.svpg.com/the-era-of-the-product-creator/
23. Cagan, "Prototypes vs Products," 7 Nov 2025. https://svpg.com/prototypes-vs-products/
24. Cagan, "Build to Learn vs Build to Earn," 16 Apr 2026. https://svpg.com/build-to-learn-vs-build-to-earn/
25. Cagan, "The AI Productivity Paradox," 23 Jul 2026. https://svpg.com/the-ai-productivity-paradox/
26. Cagan, "A Fresh Definition of the Product Role," 10 Aug 2026. https://svpg.com/a-fresh-definition-of-the-product-role/
27. Cagan, "Experimentation, AI and the Product Model," 21 Oct 2026. https://svpg.com/experimentation-ai-and-the-product-model/
28. WBR mechanics, OP1/OP2 timing and S-team goals, from Commoncog's account based on Bryar and Carr (first published 2 Jul 2024, updated 14 Jun 2026). Secondary, but detailed and built on interviews with Bryar. https://commoncog.com/the-amazon-weekly-business-review/

---

## (c) Quotes (each under 15 words, checked on the source page)

1. "your job is to be the advocate for whoever isn't currently in the room" (Ken Norton, "How to Hire a Product Manager," 2005) https://www.bringthedonuts.com/essays/productmanager.html
2. "It's about achieving outcomes versus merely producing output." (SVPG, "The Product Operating Model: An Introduction," 2023) https://svpg.com/the-product-operating-model-an-introduction/
3. "product discovery will become the main activity of product teams" (Marty Cagan, "A Vision for Product Teams," 2025) https://www.svpg.com/a-vision-for-product-teams/
4. "Writing the code isn't the hard part" (Marty Cagan, "A Fresh Definition of the Product Role," 2026) https://svpg.com/a-fresh-definition-of-the-product-role/
5. "The PM job is expanding, not disappearing." (Lenny Rachitsky, section heading, Lenny & Friends Summit write-up, 2026) https://www.lennysnewsletter.com/p/all-of-the-lenny-and-friends-summit

Note: quote wording came through a fetch tool that summarizes pages. Recheck punctuation against the live page before printing.

---

## (d) Reference list

| Author | Title | Publisher / site | Year | URL | Note |
|---|---|---|---|---|---|
| Cagan, M. | *Inspired: How to Create Tech Products Customers Love*, 2nd ed. | Wiley | 2017 | https://bookshop.org/p/books/inspired-how-to-create-tech-products-customers-love-marty-cagan/8599213 | Product discovery, four risks, the product trio. |
| Cagan, M. and Jones, C. | *Empowered: Ordinary People, Extraordinary Products* | Wiley | 2020 | https://www.oreilly.com/library/view/empowered-ordinary-people/9781119691297/ | Product leadership: coaching, strategy, empowered teams. |
| Cagan, M. et al. | *Transformed: Moving to the Product Operating Model* | Wiley | 2024 | https://porchlightbooks.com/product/transformed-moving-to-the-product-operating-model--marty-cagan/isbn/9781119697336 | Transformation playbook and model principles. |
| SVPG | "The Product Operating Model: An Introduction" | svpg.com | 2023 | https://svpg.com/the-product-operating-model-an-introduction/ | Three dimensions and principle areas. |
| Cagan, M. | "Product Risk Taxonomy" | svpg.com | 2023 | https://svpg.com/product-risk-taxonomies | Why there are four risks. |
| Cagan, M. | "A Vision for Product Teams" | svpg.com | 2025 | https://www.svpg.com/a-vision-for-product-teams/ | Teams shrinking to about 3 people. |
| Cagan, M. | "The Era of the Product Creator" | svpg.com | 2025 | https://www.svpg.com/the-era-of-the-product-creator/ | Role defined by risks owned, not title. |
| Cagan, M. | "Prototypes vs Products" | svpg.com | 2025 | https://svpg.com/prototypes-vs-products/ | Limits of AI prototypes in enterprise. |
| Cagan, M. | "Build to Learn vs Build to Earn" | svpg.com | 2026 | https://svpg.com/build-to-learn-vs-build-to-earn/ | Discovery vs delivery building with AI. |
| Cagan, M. | "The AI Productivity Paradox" | svpg.com | 2026 | https://svpg.com/the-ai-productivity-paradox/ | More output does not mean better outcomes. |
| Cagan, M. | "A Fresh Definition of the Product Role" | svpg.com | 2026 | https://svpg.com/a-fresh-definition-of-the-product-role/ | Three skills from Benedict Evans; revises his 2025 view. |
| Cagan, M. | "Experimentation, AI and the Product Model" | svpg.com | 2026 | https://svpg.com/experimentation-ai-and-the-product-model/ | Evals and experimentation ops. |
| Horowitz, B. | "Good Product Manager/Bad Product Manager" | a16z.com | 2012 (written 1990s) | https://a16z.com/good-product-manager-bad-product-manager/ | Classic behavioral contrasts. |
| Norton, K. | "How to Hire a Product Manager" | Bring the Donuts | 2005 (upd. 2023) | https://www.bringthedonuts.com/essays/productmanager.html | PM as advocate who leads by influence. |
| Norton, K. | "How to Hire a PM: 20-year retrospective" | Bring the Donuts | 2025 | https://www.bringthedonuts.com/essays/how-to-hire-a-pm-retrospective/ | What changed, including AI. |
| Gupta, A. | "LNO Framework for Product Managers" | Product Growth | 2020 | https://www.news.aakashg.com/p/lno-framework-for-product-managers | Secondary source for Doshi's LNO. |
| Wang, S. (swyx) | Live notes from a Shreyas Doshi workshop | Thread Reader | 2022 | https://threadreaderapp.com/thread/1492687642550411267.html | Secondary source for the three levels. |
| Perri, M. | *Escaping the Build Trap* | O'Reilly | 2018 | https://oreilly.com/library/view/escaping-the-build/9781491973783 | Build trap; Product Kata. |
| Perri, M. | "The Product Kata" | melissaperri.com | 2015 | https://melissaperri.com/blog/2015/07/22/the-product-kata | Original kata elements. |
| Perri, M. and Tilles, D. | *Product Operations* | Produx Labs | 2023 | https://www.goodreads.com/book/show/199368360 | Three pillars of product ops. |
| Rachitsky, L. | "Product management career ladders" | Lenny's Newsletter | 2022 | https://www.lennysnewsletter.com/p/product-management-career-ladders | IC and manager tracks across 20+ companies. |
| Segal, N. and Rachitsky, L. | "AI tools are overdelivering" | Lenny's Newsletter | 2025 | https://lennysnewsletter.com/p/ai-tools-are-overdelivering-results | Survey of 1,750 on AI use. |
| Rachitsky, L. | Lenny & Friends Summit write-up | Lenny's Newsletter | 2026 | https://www.lennysnewsletter.com/p/all-of-the-lenny-and-friends-summit | PM role expanding, not merging. |
| Reforge | "Maximize the performance of your product managers" | reforge.com | 2024 | https://www.reforge.com/blog/maximize-the-performance-of-your-product-managers | 12-competency model with Ravi Mehta. |
| Eriksson, M. | "What, exactly, is a Product Manager?" | Mind the Product | 2011 | https://www.mindtheproduct.com/what-exactly-is-a-product-manager/ | Business, Technology, UX Venn diagram. |
| Pragmatic Institute | Pragmatic Framework | pragmaticinstitute.com | current | https://www.pragmaticinstitute.com/product/framework/ | 37 boxes, 7 categories. |
| AIPMM (Geracie, G., ed.) | *ProdBOK Guide* | AIPMM | 2013 | https://aipmm.com/about | Lifecycle body of knowledge. |
| PDMA (Anderson, A. M. et al.) | *Product Development and Management Body of Knowledge*, 3rd ed. | Wiley | 2022? | https://www.oreilly.com/library/view/-/9781119829942/ | NPDP basis, 7 areas. Year [U]. |
| ISPMA / Kittlaus and Fricker | *Software Product Management: The ISPMA-Compliant Study Guide* | Springer | 2017 | https://ispma.org/bok/ | SPM reference framework. |
| ISO | ISO/IEC 20926:2009 | iso.org | 2009 | https://www.iso.org/standard/51717.html | Function points. Not a PM standard. |
| Cooper, R. G. | "Stage-gate systems: A new tool for managing new products" | *Business Horizons* 33(3) | 1990 | (DOI not retrieved) | Formal Stage-Gate description. |
| Bryar, C. and Carr, B. | *Working Backwards* | St. Martin's Press | 2021 | https://www.goodreads.com/work/quotes/81650661 | PR/FAQ, WBR, OP1/OP2, six-pagers. |
| Chin, C. | "The Amazon Weekly Business Review" | Commoncog | 2024 (upd. 2026) | https://commoncog.com/the-amazon-weekly-business-review/ | Detailed WBR mechanics. |
| Atlassian | DACI decision-making framework | Atlassian Team Playbook | current | https://www.atlassian.com/team-playbook/plays/daci | Roles and decision template. |

---

## Editorial flags (unresolved)

1. **ISO/IEC 20926 is the wrong standard.** It covers function-point sizing. Remove it, or replace it with ISPMA as the closest "standard" body of knowledge for software PM.
2. **Horowitz origin.** The year and co-author (David Weiden) are not settled. Write "written at Netscape in the 1990s, published on a16z in 2012."
3. **Dan Schmidt's triangle.** I could not locate the original post or its date. Secondary sources also disagree on the name ("Product Management Triangle" vs "Product Network").
4. **Shreyas Doshi.** LNO and the three levels are verified only through secondary sources. Find the original threads or a podcast timestamp.
5. **Product ops pillar names.** Sources disagree: "Data and Insights" vs "Business and Data Insights," and "Process and Governance" vs "Process and Practices." Use the book's wording.
6. **Product Kata wording in the book.** The book chapter was not accessible. The 2015 blog wording is verified.
7. **Reforge's four competency groups.** The 12-competency count is verified; the four group names are not.
8. **Principal and Group PM scope.** There is no authoritative standard. The book should define these itself.
9. **Amazon process detail.** It comes from Commoncog's account of Bryar and Carr, not Amazon. Before printing, check the WBR rhythm, metric counts and the 75% S-team figure against the book.
10. **McAllister's Quora date** (2010, 2011 or 2012) and **Stage-Gate's origin year** (1986 or 1988) are not settled.
11. **DACI origin** (Intuit is often claimed) and Atlassian's McKinsey "25% higher success" figure are untraced.
12. **QBR, strategy review and portfolio review formats** have no single primary source. Present the cadence in Chapter 00 as the author's synthesis.
13. **LinkedIn's "Product Builder" program** is reported second-hand only.
14. **PDMA 3rd edition year** was not confirmed (probably 2022 or 2023).
