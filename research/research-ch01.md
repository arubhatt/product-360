# Research notes: Chapter 01, Developing a Product Hypothesis and Personas

Prepared 2026-10-30 for *The Product 360 Handbook* (2026 edition). Audience: Senior to Principal PMs, B2B enterprise and platform products.

**Verification key**
- **[V]** Verified this session against the primary source or the author's own site (URL given).
- **[V2]** Verified only through consistent secondary sources. Check the book before quoting.
- **[U]** Unverified. Drawn from general knowledge or a single weak source. Confirm before print.

---

## Part A. Key concepts and frameworks

### 1. Problem and hypothesis framing

#### 1.1 Leap-of-faith assumptions (Eric Ries, *The Lean Startup*, 2011)
- **Summary [V2]:** Ries treats a venture's plan as resting on two leap-of-faith assumptions. The **value hypothesis** asks whether the product delivers value to customers once they use it. The **growth hypothesis** asks how new customers will discover and adopt it. The MVP is the smallest experiment that tests these assumptions, and the riskiest assumptions are tested first. Ries also suggests studying analogs (comparable successes) and antilogs (comparable failures) to surface which assumptions matter.
- **PM application:** Before a business case, list the two or three beliefs that, if false, kill the initiative. In B2B, the growth hypothesis is often a channel or buying-process assumption (for example, "security teams will approve a self-serve trial"), not a virality assumption.

#### 1.2 Lean Canvas (Ash Maurya, 2010)
- **Summary [V]:** Maurya created Lean Canvas in 2010 as an adaptation of Osterwalder's Business Model Canvas for products under extreme uncertainty. It replaces four BMC boxes (Key Partners, Key Activities, Key Resources, Customer Relationships) with **Problem, Solution, Key Metrics, Unfair Advantage**. Source: https://leanspark.ai/leancanvas (leancanvas.com now redirects here).
- **Template:** The classic canvas has 9 boxes: Problem, Customer Segments, Unique Value Proposition, Solution, Channels, Revenue Streams, Cost Structure, Key Metrics, Unfair Advantage. The current version on Maurya's site shows 12 elements by adding three sub-boxes: **Existing Alternatives** (under Problem), **Early Adopters** (under Customer Segments) and **High-Level Concept** (the "X for Y" analogy, under UVP).
- **Suggested fill order [U]:** Maurya's books recommend starting with Customer Segments and Problem, then UVP, then Solution. Confirm the exact order in *Running Lean*, 3rd ed. (2022).
- **PM application:** Use one canvas per customer segment. In platform products, write separate canvases for the developer segment and the enterprise-buyer segment; they usually have different problems and different existing alternatives.

#### 1.3 Customer-problem-solution hypothesis (general format)
- **Summary [U, synthesized from Lean Startup and eCornell course framing]:** A three-part statement that separates who, what hurts, and what you propose, so each part can be tested and fail on its own.
- **Template:**
  > **Customer:** We believe [specific segment, role and context]
  > **Problem:** experiences [problem] when [situation], which costs them [measurable consequence].
  > **Solution:** We believe [solution concept] will solve this, and we will know we are right when [observable signal] within [timeframe].
- **PM application:** Test in order. If the customer and problem hypotheses fail, the solution hypothesis is moot. Most interview programs in Part A.5 test the first two only.

#### 1.4 Lean UX hypothesis statements (Jeff Gothelf and Josh Seiden)
- **Summary [V2]:** Lean UX (O'Reilly; 1st ed. 2013, 3rd ed. 2021 [U on edition years]) reframes requirements as hypotheses linking a business outcome, a user, a user outcome and a feature. The Lean UX Canvas (v2) restricts each hypothesis to one solution.
- **Template (Lean UX Canvas v2 form, widely reproduced) [V2]:**
  > We believe that **[business outcome]** will be achieved if **[user]** attains **[benefit]** with **[feature]**.
- **Earlier slide form (Gothelf, 2016 deck) [V2]:** "We believe this [business outcome] will be achieved if [these users] successfully [attain this user outcome] with [this feature]." A "for [user]" variant also circulates; I could not trace it to Gothelf or Seiden, so treat it as **[U]**.
- **PM application:** Pair each hypothesis with the smallest test and the measurable signal. In enterprise contexts, the "business outcome" should name the customer's outcome and your outcome separately (for example, reduced audit prep time for the customer, expansion revenue for you).

#### 1.5 Assumption mapping (David J. Bland; *Testing Business Ideas*, Bland and Osterwalder, Wiley, 2019)
- **Summary [V2]:** Teams sort assumptions into three risk types: **Desirability** (do customers want this?), **Feasibility** (can we deliver it?), **Viability** (should we, financially?). They then plot each assumption on a 2x2 of **importance** (how critical to success) against **evidence** (how much proof exists). The top-right "important, little evidence" quadrant is tested first. The technique builds on the assumptions work in Gothelf and Seiden's *Lean UX*. Product Compass (Pawel Huryn) argues the two versions differ and critiques the 2x2; useful if the chapter wants a counterpoint.
- **PM application:** Run it as a 60-minute trio exercise after drafting the hypothesis. In B2B, add a fourth lens many teams miss: **adoptability** (will the buying group, security review and procurement let this through?). That fourth lens is this author's suggestion, not Bland's. Label it as such.

#### 1.6 Opportunity assessment (Marty Cagan, SVPG, 2006)
- **Summary [V]:** Cagan's ten questions, published 13 Dec 2006 at https://www.svpg.com/assessing-product-opportunities/:
  1. Exactly what problem will this solve? (value proposition)
  2. For whom do we solve that problem? (target market)
  3. How big is the opportunity? (market size)
  4. What alternatives are out there? (competitive landscape)
  5. Why are we best suited to pursue this? (our differentiator)
  6. Why now? (market window)
  7. How will we get this product to market? (go-to-market strategy)
  8. How will we measure success/make money from this product? (metrics/revenue strategy)
  9. What factors are critical to success? (solution requirements)
  10. Given the above, what's the recommendation? (go or no-go)
- **Note [U]:** *Inspired*, 2nd ed. (Wiley, 2017), revisits this and argues for lighter-weight framing for most work. Confirm wording before citing.
- **PM application:** Use the ten questions as the one-page gate before discovery investment, then let the hypothesis statement and assumption map carry the detail.

---

### 2. Jobs to Be Done (JTBD)

#### 2.1 Christensen: jobs theory and the milkshake
- **Summary [V2]:** Christensen, Hall, Dillon and Duncan, "Know Your Customers' 'Jobs to Be Done'" (*HBR*, Sept 2016) and *Competing Against Luck* (HarperBusiness, 2016). A job is the progress a customer is trying to make in a particular circumstance, with functional, social and emotional dimensions. The milkshake case: a fast-food chain found morning buyers "hired" milkshakes to make a long, boring commute bearable and to stay full until mid-morning. The competition was bagels, bananas and boredom, not other milkshakes. The lesson is to segment by job and circumstance, not by demographics or product category.
- **Caution:** Retellings add details (exact times, quantities) that vary. Quote the HBR article or the book, not a blog.
- **PM application:** Ask "what did the customer fire to hire us?" In enterprise software the fired option is often a spreadsheet, a services contract or an internal script.

#### 2.2 Bob Moesta and Chris Spiek: switch interviews and the forces of progress
- **Summary [V]:** Source: https://jobstobedone.org/the-four-forces/. The four forces model, developed by Moesta and Spiek:
  - **Push** of the current situation (friction that starts the search).
  - **Pull** of the new solution (the better future imagined, not the feature list).
  - **Anxiety** of the new solution (fear it will not work, risk to data).
  - **Habit** of the present (comfortable inertia).
  - A switch happens only when Push + Pull > Anxiety + Habit.
- **Switch interview [V2]:** Reconstructs the timeline of a real, recent purchase from first thought through decision and use, attaching each force to dated moments. Commonly taught timeline stages are first thought, passive looking, active looking, deciding, consuming and satisfaction **[U: confirm stage names against Moesta, *Demand-Side Sales 101*, 2020, or the Re-Wired Group materials]**.
- **PM application:** Interview customers who switched to you in the last 90 days and customers who switched away. For enterprise, interview the champion and at least one other buying-group member, because anxiety often sits with security or procurement, not the user.

#### 2.3 Tony Ulwick: Outcome-Driven Innovation (ODI)
- **Job map [V2]:** Bettencourt and Ulwick, "The Customer-Centered Innovation Map," *HBR*, May 2008 (https://hbr.org/2008/05/the-customer-centered-innovation-map). The universal eight steps are commonly given as **Define, Locate, Prepare, Confirm, Execute, Monitor, Modify, Conclude** [U: the HBR landing page did not show the list; confirm from the article PDF].
- **Desired outcome statement [V2]:**
  > [Direction of improvement] + [metric] + [object of control] + [contextual clarifier]
  > Example: "Minimize the time it takes to locate a file during a patient consultation."
  - Direction is typically "minimize" (sometimes "increase"); the metric is usually time or likelihood.
- **Opportunity score [V]:** Strategyn gives the Opportunity Algorithm as
  > **Opportunity = Importance + max(Importance − Satisfaction, 0)**
  - Importance and satisfaction are the percentage of respondents rating an outcome very or extremely important / satisfied (top-two-box), commonly scaled to 0 to 10. The max() floor stops over-served outcomes from reducing the score. Source: https://strategyn.com/quantify-your-customers-unmet-needs/. Strategyn says Ulwick introduced it in a 2002 HBR article ("Turn Customer Input into Innovation," Jan 2002 [U on title]).
  - Thresholds such as "above 10 is underserved, above 15 is extreme" appear in vendor tools and secondary sources but **I could not confirm them in Strategyn's own materials [U]**.
- **PM application:** Use ODI where the job is stable and the market is large enough for a quantitative survey (often 150+ respondents [U]). For platform products, run the job map on the operator's job (for example, "provision secure access for a new contractor"), not on your feature set.

#### 2.4 Alan Klement: job stories
- **Summary [V]:** Klement's guest post "Designing Features Using Job Stories," Intercom blog, 23 Dec 2013, credits Paul Adams at Intercom with first mentioning job stories. Klement argues personas and user stories hide causality: user stories tie implementation to motivation, so a failed feature does not tell you whether the build or the assumption was wrong. Job stories separate situation and motivation from the solution. Source: https://www.intercom.com/blog/using-job-stories-design-features-ui-ux/
- **Template [V2; the 2013 post does not give a fixed template]:**
  > **When** [situation], **I want to** [motivation], **so I can** [expected outcome].
- Klement later expanded this in *When Coffee and Kale Compete* (some sources say 2014, others 2016 [U]).
- **PM application:** Write the job story first to define the problem, then write user stories as candidate solutions beneath it. Klement's own guidance, quoted in academic work, supports this split.

#### 2.5 Note for the chapter: two JTBD schools
Moesta and Klement focus on the *progress* and *switching moment*. Ulwick focuses on the *job as a process* with measurable outcomes. Klement and Ulwick have publicly disagreed (for example, Ulwick's post "Confusion Leads to Klement's Illusion" on jobs-to-be-done.com). A Principal PM should use the switch interview for qualitative discovery and ODI for quantitative prioritization, and be explicit about which lens they use.

---

### 3. Personas

#### 3.1 Origin: Alan Cooper
- **Summary [V2]:** Cooper began using a proto-persona idea around 1983, based on informal interviews with seven or eight users (often told via his imagined colleague "Kathy"). He introduced personas publicly in *The Inmates Are Running the Asylum* (Sams, 1998 or 1999; sources disagree [U]). Cooper's own account on cooper.com returned 404 this session; Wikipedia's persona article summarizes it.
- **PM application:** Cooper's core point still holds: design for a specific person, not an elastic "user" who can be stretched to justify any feature.

#### 3.2 Pruitt and Adlin; Pruitt and Grudin
- **Summary [V]:** John Pruitt and Jonathan Grudin, "Personas: Practice and Theory" (DUX 2003, Microsoft Research), described persona practice at Microsoft and the psychology of why personas engage teams more than scenarios alone (https://www.microsoft.com/en-us/research/publication/personas-practice-theory/). Pruitt and Tamara Adlin, *The Persona Lifecycle* (Morgan Kaufmann, 2006), frames personas as a five-phase lifecycle: family planning, conception and gestation, birth and maturation, adulthood (use), and lifetime achievement and retirement (ROI and reuse) [phase names V2].
- **PM application:** Treat personas as an artifact with an owner and a retirement date, not a poster.

#### 3.3 Proto-personas (Jeff Gothelf, UX Magazine, 1 May 2012)
- **Summary [V]:** Proto-personas are personas that are *not* initially the result of research. They encode the team's and executives' assumptions so they can be tested. Source: https://uxmag.com/articles/using-proto-personas-for-executive-alignment
- **Template [V]:** A four-quadrant sheet: sketch, name and basic demographics (top-left); behaviors and beliefs (top-right); demographics (bottom-left); needs and goals (bottom-right).
- **Workshop [V]:** Day 1 three-hour session: executives draft personas in 15 minutes, present them, then place them on five behavioral spectrums by vote. The team consolidates to 3 to 5 personas. Day 2 validates the set and runs a short design studio. The follow-up email restates that they are assumptions.
- **PM application:** In enterprise orgs, the proto-persona workshop is a strong tool for exposing that sales, product and the exec team are each picturing a different buyer.

#### 3.4 NN/g guidance: three persona types
- **Summary [V]:** Page Laubheimer, "3 Persona Types: Lightweight, Qualitative, and Statistical," NN/g, 21 Jun 2020 (https://www.nngroup.com/articles/persona-types/):
  - **Proto (lightweight):** no new research; 2 to 4 hour workshop; 3 to 6 personas. Aligns assumptions but may not reflect users.
  - **Qualitative:** 5 to 30 interviews, coded into themes. NN/g calls this the best fit for most teams. It cannot size each persona's share of users.
  - **Statistical:** qualitative research, then a survey of at least 100 (ideally 500+) respondents, clustered (latent class, factor analysis, k-means). Costly; results often similar to qualitative personas.
- **PM application:** Start proto, graduate to qualitative within a quarter. Reserve statistical personas for pricing and packaging decisions where segment size matters.

#### 3.5 B2B buying-center personas
- **Buying center [V2]:** Webster and Wind (1972) defined the organizational buying center with five roles: **users, influencers, buyers, deciders, gatekeepers**. Bonoma (1982) is credited with adding **initiator** [V2]. Primary article not retrieved.
- **Strategic Selling buying influences [V2]:** Miller and Heiman, *Strategic Selling* (1985; revised as *The New Strategic Selling*, 2005 [U on dates]): **Economic Buyer** (budget and final approval), **User Buyer** (uses or supervises the solution day to day), **Technical Buyer** (screens on feasibility, risk, compliance; can say no, rarely yes), **Coach** (internal guide). MEDDIC renames the coach role **Champion**.
- **Recommended persona set for this book (synthesis, label as author's framework):** Economic buyer, Champion, End user, Technical evaluator (security, IT, architecture), plus Procurement/legal as a gatekeeper. Each gets a job story and its main anxiety (Moesta).
- **Gartner B2B buying research:**
  - **Six buying jobs [V2]:** problem identification, solution exploration, requirements building, supplier selection, validation, consensus creation. Gartner's 9 Oct 2018 press release says buyers complete all six and address validation and consensus throughout; the jobs are non-linear. (Press release returned HTTP 403 this session; job names consistent across secondary sources.) https://www.gartner.com/en/newsroom/press-releases/2018-10-09-gartner-says-the-marketing-to-sales-handoff-should-no-longer-exist
  - **Buying group of 6 to 10 decision makers; 17% of buying time spent meeting potential suppliers (split across all suppliers, so about 5 to 6% per vendor when three are considered) [U].** Widely attributed to Gartner (circa 2019 to 2020), but the Gartner page returned 403 and I found no Gartner newsroom source for 17%. An older Gartner page cites 24% for time with all suppliers. Do not print either figure without the primary report.
  - **Rep-free preference [V2 via Gartner newsroom search excerpt]:** Gartner press release, 25 Jun 2025: 61% of B2B buyers prefer an overall rep-free buying experience (survey of 632 B2B buyers, Aug to Sep 2024). https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience
  - **AI and buyers [V2 via search excerpt]:** Gartner press release, 20 May 2026: 69% of B2B buyers turn to sales reps to validate AI-generated insights (survey of 645 buyers, Aug to Sep 2025). https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights
- **PM application:** Map each buying job to the persona who owns it. Consensus creation is where enterprise deals stall, so the champion persona needs artifacts (ROI model, security pack) that help them sell internally.

---

### 4. Customer journey mapping

#### 4.1 NN/g journey maps
- **Summary [V]:** Sarah Gibbons, "Journey Mapping 101," NN/g, 9 Dec 2018, last reviewed 15 Jul 2026 (https://www.nngroup.com/articles/journey-mapping-101/). Definition: a visualization of the process a person goes through to accomplish a goal.
- **Components (template):**
  - **Zone A, the lens:** Actor (one persona per map), Scenario and expectations.
  - **Zone B, the experience:** Journey phases; per phase, actions, mindsets (thoughts), emotions (as a line of highs and lows).
  - **Zone C, the insights:** Opportunities, with internal ownership and metrics.
- **Related maps [V]:**
  - **Experience map:** the broader parent; a generic person's experience, not tied to a product.
  - **Journey map:** specific actor, scenario and product.
  - **Service blueprint:** the company-side extension of a journey map.
  - **User-story map:** planning and implementation tool; journey maps are for discovery.

#### 4.2 Service blueprints
- **Summary [V]:** Sarah Gibbons, "Service Blueprints: Definition," NN/g, 27 Aug 2017, last reviewed 15 Jul 2026 (https://www.nngroup.com/articles/service-blueprints-definition/). A diagram of how people, props and processes relate at the touchpoints of a specific customer journey.
- **Template rows:** Evidence; Customer actions; *line of interaction*; Frontstage actions; *line of visibility*; Backstage actions; *line of internal interaction*; Support processes.
- **Origin [V2]:** G. Lynn Shostack, "Designing Services That Deliver," *HBR*, 1984.
- **PM application:** For B2B platforms, the "backstage" is usually provisioning, support, billing and customer success. Blueprinting onboarding often shows that time-to-value is lost in handoffs, not in the UI.

#### 4.3 B2B extension (author synthesis)
Draw the journey at two levels: the **buying journey** (Gartner's six jobs, multiple personas, swimlane per buying-group role) and the **usage journey** (one actor per map, per NN/g). Connect them at the "first value" moment.

---

### 5. Discovery interviewing

#### 5.1 *The Mom Test* (Rob Fitzpatrick, 2013)
- **Summary [V2]:** Three rules:
  1. Talk about their life instead of your idea.
  2. Ask about specifics in the past instead of generics or opinions about the future.
  3. Talk less and listen more.
- Three kinds of bad data: **compliments, fluff** (generic claims, future promises, hypotheticals), and **ideas** (feature requests to dig behind). Fitzpatrick also stresses asking for commitment and advancement (time, reputation, money) as the real signal.
- **PM application:** Replace "Would you use X?" with "Tell me about the last time you had to do Y. What did you use? What did it cost you?" In enterprise, a pilot, a security review slot or an exec intro counts as commitment.

#### 5.2 Teresa Torres, *Continuous Discovery Habits* (Product Talk LLC, 2021 [U on year, widely cited])
- **Definition [U from book; matches Torres's talks]:** At minimum, weekly touchpoints with customers, by the team building the product, where they conduct small research activities in pursuit of a desired outcome. The ProductTalk snapshot article recommends at least one interview per week, with the product trio.
- **Opportunity solution tree [V]:** Torres, ProductTalk, 6 Dec 2023 (https://www.producttalk.org/opportunity-solution-tree/). Levels: **desired outcome** (root) → **opportunities** (unmet needs, pain points, desires) → **solutions** → **assumption tests**. Revisit the opportunity space every three to four interviews.
- **Story-based interviews [V]:** Collect specific past stories with prompts such as "Tell me about a time when…"; avoid generalizations and speculation.
- **Interview snapshot [V]:** Torres, ProductTalk, 21 Feb 2024 (https://www.producttalk.org/interview-snapshot/). Fields: participant name; photo; quick facts (context, not a fixed set); memorable quote; opportunities; insights (notable, not yet actionable); experience map of the story's key moments.
- **PM application:** For a Principal PM, the habit is the point: automate recruiting (in-product intercepts, CSM referrals) so the trio talks to a customer every week without a project kickoff.

#### 5.3 Steve Portigal, *Interviewing Users* (Rosenfeld Media; 1st ed. 2013, 2nd ed. 17 Oct 2023)
- **Summary [V2]:** The second edition adds operations, organizational impact and remote research. Portigal emphasizes embracing how the participant sees the world, building rapport, using silence and follow-up questions, and moving from interviewing to sense-making. Publisher page: https://rosenfeldmedia.com/books/interviewing-users-second-edition/
- **PM application:** Use Portigal for interviewing craft (rapport, probing, silence) and Torres for cadence and synthesis.

---

### 6. AI-era practice (2025 to 2026)

#### 6.1 AI-assisted research synthesis
- **NN/g guidance [V]:** Kate Moran and Maria Rosala, "Accelerating Research with AI," NN/g, 27 Sep 2024, last reviewed 21 Jan 2026 (https://www.nngroup.com/articles/research-with-ai/). AI helps most in planning and analysis. Use it for a first pass at coding and clustering; verify transcripts and translations; spot-check quantitative output. Do not use AI to moderate or analyze usability tests, because it cannot observe behavior. AI interviewers suit structured, large-scale feedback, not semistructured discovery.
- **Earlier tool evaluation [V]:** Feifei Liu and Kate Moran, "AI-Powered Tools for UX Research: Issues and Limitations," NN/g, 2 Jul 2023 (https://www.nngroup.com/articles/ai-powered-tools-limitations/). Tools could not process video, could not take in study context, gave vague outputs, and cited weakly. NN/g notes tools have since improved; cite as a baseline, not current state.
- **Adoption data [V]:** User Interviews, *State of User Research 2025*, published 10 Sep 2025, 485 researchers, fielded 25 Jul to 9 Aug 2025 (https://www.userinterviews.com/state-of-user-research-2025-report): 80% of researchers use AI (up 24 points year over year); 41% view AI's current effect on UXR negatively vs 32% positively; 91% worry about accuracy and hallucinations; 63% fear AI could devalue human insight. Their 2023 survey had about one in five researchers using AI (https://www.userinterviews.com/ai-in-ux-research-report-2023).
- **Torres and AI [V2]:** ProductTalk references AI-generated interview snapshots available through Vistaly. Confirm the product relationship before naming the vendor in print.
- **PM application:** Let AI transcribe, tag and draft snapshots; keep humans on the opportunity framing and on deciding what the story means. Keep the source clip linked to every AI-generated insight.

#### 6.2 Synthetic users and AI personas: the debate
- **NN/g position [V]:** Maria Rosala and Kate Moran, "Synthetic Users: If, When, and How to Use AI-Generated 'Research'," NN/g, 21 Jun 2024 (https://www.nngroup.com/articles/synthetic-users/). Defines a synthetic user as an AI-generated profile that attempts to mimic a user group. Findings: synthetic users are sycophantic and idealized (claimed to finish every course), "care about everything" so they cannot prioritize, cannot report real past behavior, reflect uncontrollable training data, and are weak for niche groups. Acceptable uses: desk research on unfamiliar domains, piloting an interview guide, generating hypotheses and proto-personas to test with real users. Do not present synthetic findings as research or base final decisions on them.
- **NN/g empirical follow-up [V]:** Rachel Banawa, "Synthetic Users vs. Human Respondents," NN/g, 16 Oct 2026 (https://www.nngroup.com/articles/synthetic-users-vs-human-respondents/). Compared 604 human respondents from an earlier NN/g terminology survey with 120 synthetic respondents generated on the Synthetic Users platform (Feb 2026). Same headline conclusion, but humans gave 50+ distinct labels versus about a dozen from synthetic respondents ("mode collapse"); 84% of synthetic vs about 70% of human respondents used UX terms (significant). 93% of synthetic PMs used UX terms vs 44% of human PMs. Recommendation: use synthetic respondents for hypotheses and broad-pattern checks; use humans when rare responses, subgroup differences or unexpected vocabulary matter. **This is the most current, directly relevant source for the chapter.** Note the confound the author flags: sample role mix differed (20% UX professionals synthetic vs 67% human).
- **Evidence for (with caveats):**
  - **[V]** Park et al., "Generative Agent Simulations of 1,000 People," arXiv:2411.10109, 15 Nov 2024. Agents built from two-hour interviews with 1,052 real people replicated those people's General Social Survey answers 85% as accurately as the people replicated their own answers two weeks later. Interview-grounded agents showed less accuracy bias across racial and ideological groups than agents given demographic descriptions. https://arxiv.org/abs/2411.10109 ; Stanford HAI summary: https://hai.stanford.edu/policy/simulating-human-behavior-with-ai-agents. **Key nuance for PMs:** the agents were grounded in real interviews with the specific people. That is a digital twin of a participant, not a persona invented from a prompt.
  - **[V2]** Brand, Israeli and Ngwe, "Using GPT for Market Research," HBS Working Paper 23-062 (2023; ACM EC 2024). GPT-3.5 produced willingness-to-pay estimates of realistic magnitude that matched patterns expected from theory. A Nov 2025 follow-up, "Using LLMs for Market Research," found fine-tuning improved predictions for new features. https://www.hbs.edu/ris/Publication%20Files/23-062_47458a4a-8be2-4b53-a3a3-9b5af20578b1.pdf ; https://www.msi.org/working-paper/using-llms-for-market-research-2/
- **PM application for B2B:** Synthetic users are weakest exactly where enterprise PMs need insight: niche roles (for example, a SOC analyst at a regulated bank), organizational politics in the buying group, and the long tail of edge cases. Use them to stress-test an interview guide or to generate a first proto-persona, then label the output "hypothesis" and validate with real interviews.

---

## Part B. Verified facts with URL

| # | Fact | Source |
|---|------|--------|
| 1 | Cagan's 10 opportunity-assessment questions, published 13 Dec 2006. | https://www.svpg.com/assessing-product-opportunities/ |
| 2 | Lean Canvas created by Ash Maurya in 2010; replaces BMC's Key Partners, Key Activities, Key Resources, Customer Relationships with Problem, Solution, Key Metrics, Unfair Advantage. | https://leanspark.ai/leancanvas |
| 3 | Opportunity = Importance + max(Importance − Satisfaction, 0), using top-two-box percentages. | https://strategyn.com/quantify-your-customers-unmet-needs/ |
| 4 | "The Customer-Centered Innovation Map," Bettencourt and Ulwick, HBR, May 2008. | https://hbr.org/2008/05/the-customer-centered-innovation-map |
| 5 | Four forces (push, pull, anxiety, habit) developed by Bob Moesta and Chris Spiek; switch when push + pull > anxiety + habit. | https://jobstobedone.org/the-four-forces/ |
| 6 | Klement's job stories post on Intercom blog, 23 Dec 2013, credits Paul Adams. | https://www.intercom.com/blog/using-job-stories-design-features-ui-ux/ |
| 7 | Gothelf's proto-persona article, UX Magazine, 1 May 2012; four-quadrant template; consolidate to 3 to 5 personas. | https://uxmag.com/articles/using-proto-personas-for-executive-alignment |
| 8 | NN/g three persona types; qualitative = 5 to 30 interviews; statistical = 100+ (ideally 500+) survey respondents. Laubheimer, 21 Jun 2020. | https://www.nngroup.com/articles/persona-types/ |
| 9 | Pruitt and Grudin, "Personas: Practice and Theory," DUX 2003. | https://www.microsoft.com/en-us/research/publication/personas-practice-theory/ |
| 10 | Journey map definition and components; experience map vs journey map vs blueprint. Gibbons, 9 Dec 2018. | https://www.nngroup.com/articles/journey-mapping-101/ |
| 11 | Service blueprint elements and three lines. Gibbons, 27 Aug 2017. | https://www.nngroup.com/articles/service-blueprints-definition/ |
| 12 | Opportunity solution tree levels; opportunity = unmet need, pain point or desire. Torres, 6 Dec 2023. | https://www.producttalk.org/opportunity-solution-tree/ |
| 13 | Interview snapshot fields. Torres, 21 Feb 2024. | https://www.producttalk.org/interview-snapshot/ |
| 14 | NN/g synthetic users article, Rosala and Moran, 21 Jun 2024. | https://www.nngroup.com/articles/synthetic-users/ |
| 15 | NN/g synthetic vs human study: 120 synthetic vs 604 human; 50+ vs about 12 labels. Banawa, 16 Oct 2026. | https://www.nngroup.com/articles/synthetic-users-vs-human-respondents/ |
| 16 | NN/g "Accelerating Research with AI," Moran and Rosala, 27 Sep 2024 (reviewed 21 Jan 2026). | https://www.nngroup.com/articles/research-with-ai/ |
| 17 | 80% of researchers use AI (n=485, Jul to Aug 2025). | https://www.userinterviews.com/state-of-user-research-2025-report |
| 18 | Generative agents of 1,052 people reached 85% of human test-retest accuracy on GSS. | https://arxiv.org/abs/2411.10109 |
| 19 | Portigal, *Interviewing Users*, 2nd ed., Rosenfeld Media, 17 Oct 2023. | https://rosenfeldmedia.com/books/interviewing-users-second-edition/ |
| 20 | Gartner: 61% of B2B buyers prefer a rep-free experience (n=632, Aug to Sep 2024), press release 25 Jun 2025. Verified from Gartner search excerpt only; page fetch blocked. | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience |

---

## Part C. Short quotes (max 5, each under 15 words)

1. "Supplement, don't substitute." (Rosala and Moran, NN/g, "Synthetic Users," 2024)
2. "Synthetic users seem to care about everything." (Rosala and Moran, NN/g, 2024)
3. "Never rely on AI tools to perform all your analysis for you." (Moran and Rosala, NN/g, "Accelerating Research with AI," 2024)
4. "Why now? (market window)" (Cagan, SVPG, "Assessing Product Opportunities," 2006)
5. An opportunity is "an unmet customer need, pain point, or desire." (Torres, ProductTalk, 2023)

Quotes 1 to 3 and 5 were extracted by a fetch tool summarizer; re-check exact wording on the page before print.

---

## Part D. Reference list

| Author | Title | Publisher / site | Year | URL | Note |
|---|---|---|---|---|---|
| Ries, Eric | *The Lean Startup* | Crown Business | 2011 | n/a | Leap-of-faith assumptions; value and growth hypotheses. |
| Maurya, Ash | Lean Canvas | LEANSpark (leancanvas.com) | 2010 (page current) | https://leanspark.ai/leancanvas | Canvas boxes and BMC adaptation. |
| Maurya, Ash | *Running Lean*, 3rd ed. | O'Reilly | 2022 [U] | n/a | Fill order and problem interviews. |
| Gothelf, J. and Seiden, J. | *Lean UX*, 3rd ed. | O'Reilly | 2021 [U] | n/a | Hypothesis statements; Lean UX Canvas. |
| Gothelf, Jeff | Using Proto-Personas for Executive Alignment | UX Magazine | 2012 | https://uxmag.com/articles/using-proto-personas-for-executive-alignment | Proto-persona template and workshop. |
| Bland, D. J. and Osterwalder, A. | *Testing Business Ideas* | Wiley | 2019 | n/a | Assumption mapping; desirability, feasibility, viability. |
| Huryn, Pawel | Assumption Prioritization Canvas | Product Compass | n.d. | https://www.productcompass.pm/p/assumption-prioritization-canvas | Critique of Bland's 2x2. |
| Cagan, Marty | Assessing Product Opportunities | SVPG | 2006 | https://www.svpg.com/assessing-product-opportunities/ | Ten questions. |
| Cagan, Marty | *Inspired*, 2nd ed. | Wiley | 2017 | n/a | Later view on opportunity assessment. |
| Christensen, C., Hall, T., Dillon, K., Duncan, D. | Know Your Customers' "Jobs to Be Done" | *Harvard Business Review* | 2016 | https://hbr.org/2016/09/know-your-customers-jobs-to-be-done | Canonical JTBD article; milkshake. |
| Christensen, C. et al. | *Competing Against Luck* | HarperBusiness | 2016 | n/a | Book-length jobs theory. |
| Moesta, B. and Spiek, C. | The Four Forces | jobstobedone.org | n.d. | https://jobstobedone.org/the-four-forces/ | Forces of progress. |
| Moesta, Bob | *Demand-Side Sales 101* | Lioncrest | 2020 [U] | n/a | Switch timeline; buyer-side JTBD for B2B. |
| Bettencourt, L. and Ulwick, A. | The Customer-Centered Innovation Map | *HBR* | 2008 | https://hbr.org/2008/05/the-customer-centered-innovation-map | Universal job map. |
| Ulwick, Anthony | *What Customers Want* | McGraw-Hill | 2005 | n/a | ODI; outcome statements; opportunity algorithm. |
| Strategyn | Quantify Your Customers' Unmet Needs | strategyn.com | n.d. | https://strategyn.com/quantify-your-customers-unmet-needs/ | Opportunity algorithm. |
| Klement, Alan | Designing Features Using Job Stories | Intercom blog | 2013 | https://www.intercom.com/blog/using-job-stories-design-features-ui-ux/ | Job stories vs personas and user stories. |
| Klement, Alan | *When Coffee and Kale Compete* | self-published | 2016 [U] | n/a | Progress-making JTBD. |
| Cooper, Alan | *The Inmates Are Running the Asylum* | Sams | 1998/1999 [U] | n/a | First published use of personas. |
| Pruitt, J. and Grudin, J. | Personas: Practice and Theory | DUX 2003 / Microsoft Research | 2003 | https://www.microsoft.com/en-us/research/publication/personas-practice-theory/ | Why personas work. |
| Pruitt, J. and Adlin, T. | *The Persona Lifecycle* | Morgan Kaufmann | 2006 | n/a | Five-phase lifecycle. |
| Laubheimer, Page | 3 Persona Types | NN/g | 2020 | https://www.nngroup.com/articles/persona-types/ | Proto, qualitative, statistical. |
| Webster, F. and Wind, Y. | A General Model for Understanding Organizational Buying Behavior | *Journal of Marketing* | 1972 | n/a | Buying center roles. |
| Miller, R. and Heiman, S. | *Strategic Selling* | Morrow / Warner | 1985 [U] | n/a | Economic, user, technical buyer; coach. |
| Gartner | Gartner Says the Marketing-to-Sales Handoff Should No Longer Exist | Gartner Newsroom | 2018 | https://www.gartner.com/en/newsroom/press-releases/2018-10-09-gartner-says-the-marketing-to-sales-handoff-should-no-longer-exist | Six B2B buying jobs. |
| Gartner | 61% of B2B Buyers Prefer a Rep-Free Buying Experience | Gartner Newsroom | 2025 | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience | Self-serve preference. |
| Gartner | 69% of B2B Buyers Turn to Sales Reps to Validate AI-Generated Insights | Gartner Newsroom | 2026 | https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights | AI in the buying journey. |
| Gibbons, Sarah | Journey Mapping 101 | NN/g | 2018 (rev. 2026) | https://www.nngroup.com/articles/journey-mapping-101/ | Journey map anatomy. |
| Gibbons, Sarah | Service Blueprints: Definition | NN/g | 2017 (rev. 2026) | https://www.nngroup.com/articles/service-blueprints-definition/ | Blueprint lines and rows. |
| Shostack, G. Lynn | Designing Services That Deliver | *HBR* | 1984 | n/a | Origin of service blueprinting. |
| Fitzpatrick, Rob | *The Mom Test* | self-published | 2013 | n/a | Three interview rules. |
| Torres, Teresa | *Continuous Discovery Habits* | Product Talk LLC | 2021 [U] | n/a | Weekly touchpoints; OST. |
| Torres, Teresa | Opportunity Solution Trees | ProductTalk | 2023 | https://www.producttalk.org/opportunity-solution-tree/ | OST levels. |
| Torres, Teresa | Interview Snapshots | ProductTalk | 2024 | https://www.producttalk.org/interview-snapshot/ | Snapshot fields. |
| Portigal, Steve | *Interviewing Users*, 2nd ed. | Rosenfeld Media | 2023 | https://rosenfeldmedia.com/books/interviewing-users-second-edition/ | Interview craft. |
| Rosala, M. and Moran, K. | Synthetic Users: If, When, and How to Use AI-Generated "Research" | NN/g | 2024 | https://www.nngroup.com/articles/synthetic-users/ | Core critique and acceptable uses. |
| Banawa, Rachel | Synthetic Users vs. Human Respondents | NN/g | 2026 | https://www.nngroup.com/articles/synthetic-users-vs-human-respondents/ | Empirical comparison; mode collapse. |
| Moran, K. and Rosala, M. | Accelerating Research with AI | NN/g | 2024 (rev. 2026) | https://www.nngroup.com/articles/research-with-ai/ | Where AI helps in research. |
| Liu, F. and Moran, K. | AI-Powered Tools for UX Research: Issues and Limitations | NN/g | 2023 | https://www.nngroup.com/articles/ai-powered-tools-limitations/ | Early tool evaluation. |
| User Interviews | The State of User Research 2025 | userinterviews.com | 2025 | https://www.userinterviews.com/state-of-user-research-2025-report | AI adoption among researchers. |
| Park, J. S. et al. | Generative Agent Simulations of 1,000 People | arXiv 2411.10109 | 2024 | https://arxiv.org/abs/2411.10109 | Interview-grounded agents; 85% normalized accuracy. |
| Brand, J., Israeli, A., Ngwe, D. | Using GPT for Market Research | HBS Working Paper 23-062 | 2023 | https://www.hbs.edu/ris/Publication%20Files/23-062_47458a4a-8be2-4b53-a3a3-9b5af20578b1.pdf | LLM WTP estimates. |

---

## Part E. Open flags for the author

1. **Gartner 17% / 6 to 10 decision makers:** not verified against a Gartner primary page (403). An older Gartner page reportedly says 24%. Get the original report or drop the number.
2. **Klement template wording** ("When… I want to… so I can…") is standard but not stated as a fixed template in the 2013 Intercom post. Cite his later book or jtbd.info (fetch failed).
3. **Ulwick job-map step names and opportunity thresholds (10, 15)** need the HBR PDF or *What Customers Want*.
4. **Switch-interview timeline stage names** need a Moesta primary source.
5. **Cooper book year (1998 vs 1999), Torres book year (2021), Lean UX 3rd ed. year, Klement book year, Strategic Selling year** are from memory or conflicting secondary sources.
6. **Lean UX "for [user]" variant** could not be traced to Gothelf or Seiden.
7. **Quotes in Part C** came through a summarizing fetch tool; confirm exact wording on the live page.
8. **Adoptability lens** (1.5) and the **B2B persona set** (3.5) are synthesis for this book, not attributed frameworks. Present them as the Handbook's own.
