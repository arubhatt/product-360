<p class="lead">Every product starts as a guess about a person, a problem and a solution. The job of this chapter is to make that guess explicit, split it into parts that can each be proven wrong, and replace the parts that fail with evidence before anyone writes a line of code.</p>

## Why this matters

Plenty of failed products were built well. They failed because the team built something good for a problem nobody had badly enough to pay for, or for a customer who wasn't the one making the decision. Those are hypothesis failures, and they're cheap to catch early and very expensive to catch late.

The trap is that a product idea feels like one thing. "An AI agent that diagnoses incidents for SRE teams" sounds like a single proposition. It's actually at least three separate bets stacked on top of each other: that SRE teams are the right customer, that slow diagnosis is a problem they'd pay to fix, and that an AI agent is a solution they'd trust. Any one of those can be false while the other two are true. If you test the bundle, a failure tells you nothing about which part broke.

This chapter gives you four tools that work together:

1. **The product hypothesis**, which splits the bet into customer, problem and solution, so each can fail on its own.
2. **Jobs to be done**, which tells you what progress the customer is really trying to make, and what they'd fire to hire you.
3. **Personas**, which turn "the customer" into specific people with specific goals, including the people who buy rather than use.
4. **Journey maps and discovery interviews**, which put the hypothesis in front of reality on a weekly rhythm.

These are the Customer dimension of your Product 360. Everything downstream (vision, strategy, roadmap, positioning, pricing) assumes they're right, so they're the first durable artifacts worth getting right.

## The product hypothesis

### Three parts that fail separately

A good product hypothesis has three parts, written so each one can be tested independently:

- **Customer hypothesis**: who specifically has the problem, in what role and context.
- **Problem hypothesis**: what hurts, in what situation, and what it costs them.
- **Solution hypothesis**: what you propose, and what observable signal will tell you it works.

The order matters, and teams often get it wrong. If the customer and problem hypotheses fail, the solution hypothesis is moot, so you test them first. Most discovery interviews should test only the first two. Showing someone your solution before you've confirmed their problem invites them to be polite about it, and polite feedback is worthless.

:::key Test the problem before the solution
A solution can only be as right as the problem it solves. Spend your first interviews proving the customer and problem hypotheses. Bring the solution in once you have evidence the problem is real, frequent and costly.
:::

This three-part shape draws on Eric Ries's *The Lean Startup*, which treats every new venture as resting on **leap-of-faith assumptions**. Ries names two that matter most: the **value hypothesis** (does the product deliver value once people use it?) and the **growth hypothesis** (how will new customers discover and adopt it?). In consumer products the growth hypothesis is often about virality. In B2B it's almost always about the buying process: "security teams will approve a self-serve trial," or "the champion can get budget without a new line item." Write that assumption down too, because in enterprise products it often kills ideas that customers value.

### The Lean UX hypothesis statement

When you move from problem to solution, Jeff Gothelf and Josh Seiden's *Lean UX* offers a compact format that links a feature to two outcomes at once. It's commonly written as:

> We believe that **[business outcome]** will be achieved if **[user]** attains **[benefit]** with **[feature]**.

The value of this format is that it forces you to name both the user's outcome and the business's outcome. In enterprise products, name the customer's outcome and your own separately. "Reduced audit-prep time for the customer" and "expansion revenue for us" are different outcomes, and a feature can deliver one without the other.

Pair each hypothesis with the smallest test that could falsify it and the signal you'll watch. A hypothesis without a falsifying signal is a wish.

### Assumption mapping

Once you've written the hypothesis, list every assumption underneath it. There are always more than you think. David Bland's assumption-mapping technique, described in *Testing Business Ideas* (with Alex Osterwalder), sorts them two ways.

First, by type of risk:

- **Desirability**: do customers want this?
- **Feasibility**: can we deliver it?
- **Viability**: should we, financially?

Then, on a 2x2: how **important** the assumption is to success, against how much **evidence** you already have. The top-right quadrant (important, little evidence) is where you test first. Everything else can wait.

For B2B products, this book adds a fourth lens that the standard three tend to hide: **adoptability**. Will the buying group, the security review and procurement let this through? A product can be desirable to users, feasible to build and viable on paper, and still never get past a security questionnaire. If your product touches production systems, customer data or AI decision-making, adoptability assumptions usually belong in the top-right quadrant.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 340" role="img" aria-label="Assumption map: importance against evidence, with the test-first quadrant highlighted">
  <rect x="80" y="20" width="260" height="140" rx="10" class="box"/>
  <rect x="350" y="20" width="260" height="140" rx="10" fill="var(--a4)" fill-opacity=".14" stroke="var(--a4)" stroke-opacity=".6"/>
  <rect x="80" y="170" width="260" height="140" rx="10" class="box"/>
  <rect x="350" y="170" width="260" height="140" rx="10" class="box"/>
  <text x="100" y="48" class="t">Important, well evidenced</text><text x="100" y="68" class="s">Monitor. Plan around it.</text>
  <text x="370" y="48" class="t" style="fill:var(--a4)">Important, little evidence</text><text x="370" y="68" class="s">Test first. These kill products.</text>
  <text x="100" y="198" class="t">Less important, well evidenced</text><text x="100" y="218" class="s">Ignore for now.</text>
  <text x="370" y="198" class="t">Less important, little evidence</text><text x="370" y="218" class="s">Park. Revisit if importance rises.</text>
  <text x="370" y="104" class="s">• Security will approve agent write access</text>
  <text x="370" y="122" class="s">• Responders accept AI root causes</text>
  <text x="370" y="140" class="s">• Buyers will pay per resolved incident</text>
  <line x1="80" y1="325" x2="610" y2="325" class="ln"/>
  <text x="345" y="338" text-anchor="middle" class="s">Evidence: strong ← → weak</text>
  <text x="30" y="165" text-anchor="middle" class="s" transform="rotate(-90 30 165)">Importance: high ↑</text>
</svg>
<figcaption>An assumption map for Beacon Agents. The top-right quadrant gets tested first. Two of the three assumptions there are adoptability and trust assumptions, not feature assumptions.</figcaption>
</figure>

### The opportunity assessment

Before a team commits real discovery time, it's worth a one-page gate. Marty Cagan's opportunity assessment, first published on SVPG in 2006, asks ten questions:

1. Exactly what problem will this solve?
2. For whom do we solve that problem?
3. How big is the opportunity?
4. What alternatives are out there?
5. Why are we best suited to pursue this?
6. Why now?
7. How will we get this product to market?
8. How will we measure success and make money from it?
9. What factors are critical to success?
10. Given the above, what's the recommendation?

Cagan has since argued, in *Inspired*, that most product work needs lighter framing than a full assessment. Treat the ten questions as a gate for new products and major bets, and use the hypothesis and assumption map for everything smaller. The useful discipline is question 4. Teams that can't name the alternatives (including "do nothing" and "build it ourselves") haven't understood the problem yet.

## Jobs to be done

A persona tells you who the customer is. Jobs to be done (JTBD) tells you why they'd buy anything at all. It's one of the most useful ideas in customer understanding, and it comes in two distinct schools that are worth keeping separate.

### The core idea

Clayton Christensen and his co-authors, in *Competing Against Luck* and the 2016 HBR article "Know Your Customers' 'Jobs to Be Done'," define a job as **the progress a customer is trying to make in a particular circumstance**. Jobs have functional, social and emotional dimensions. Customers "hire" a product to do the job and "fire" whatever they were using before.

The famous example is a fast-food chain's milkshake. Researchers found that many morning buyers were hiring a milkshake to make a long, boring commute bearable and keep them full until mid-morning. The real competition wasn't other milkshakes. It was bagels, bananas and boredom. The lesson: segment by job and circumstance, not by demographics or product category.

In enterprise software, asking "what did the customer fire to hire us?" is often revealing. The fired option is more often a spreadsheet, a services contract, an internal script or a person's evenings than a competitor.

### School one: progress and switching (Moesta, Spiek, Klement)

Bob Moesta and Chris Spiek developed the **four forces of progress**, which explain when a customer actually switches:

- **Push** of the current situation: the friction that starts the search.
- **Pull** of the new solution: the better future they imagine.
- **Anxiety** about the new solution: fear it won't work or will cause new problems.
- **Habit** of the present: the comfort of the way things are.

A switch happens only when push and pull together outweigh anxiety and habit. The model is practical because it shows where effort goes missing. Product teams tend to spend most of their energy on pull (features) and little on reducing anxiety, which in B2B is often the force that decides the deal.

Moesta's **switch interview** reconstructs the timeline of a real, recent purchase, from the first thought that something had to change through looking, deciding and using, attaching each force to dated moments. Interview customers who switched to you in the last 90 days and customers who switched away. In enterprise, interview the champion and at least one other member of the buying group, because the anxiety usually sits with security or procurement, not with the user.

Alan Klement, in a 2013 post on the Intercom blog (crediting Intercom's Paul Adams with the idea), proposed **job stories** as an alternative to persona-based user stories. A job story separates the situation and motivation from the solution:

> **When** [situation], **I want to** [motivation], **so I can** [expected outcome].

Klement's argument is that a user story ("As an SRE, I want an AI root cause...") ties the implementation to the motivation, so when a feature fails you can't tell whether the build or the assumption was wrong. Write the job story first to define the problem. Then write user stories beneath it as candidate solutions.

### School two: the job as a process (Ulwick)

Tony Ulwick's **Outcome-Driven Innovation** treats the job as a process with measurable steps. Lance Bettencourt and Ulwick's 2008 HBR article "The Customer-Centered Innovation Map" lays out a universal job map that any job can be broken into: defining what's needed, locating inputs, preparing, confirming readiness, executing, monitoring, modifying and concluding.

At each step, customers have **desired outcomes**, written in a precise format: a direction of improvement, a metric, the object of control and a contextual clarifier. For example: "Minimize the time it takes to identify which recent change caused an outage." Because the statements are precise and solution-free, you can survey customers on them at scale. Ulwick's **opportunity score** then ranks them:

> Opportunity = Importance + max(Importance − Satisfaction, 0)

Importance and satisfaction are the share of respondents rating an outcome as very or extremely important, or very or extremely satisfied, usually scaled to 0 to 10. The `max()` keeps over-served outcomes (high satisfaction) from dragging the score below their importance. High scores mean important and underserved: that's where to build.

### Which school to use

The two schools have publicly disagreed, and a Principal PM should be explicit about which lens they're using. In practice they fit different questions:

| Question | Use | Why |
|---|---|---|
| Why do customers switch to us, or away? | Switch interviews and four forces | Reveals the anxiety and habit your features don't address |
| What problem should this feature solve? | Job stories | Keeps the motivation separate from the implementation |
| Which unmet needs matter most across a large market? | ODI job map and opportunity scores | Quantifies importance and satisfaction at scale |
| Where in a workflow are we losing customers? | Job map plus journey map | Shows which step fails and what it costs |

:::onramp If JTBD is new to you
Start with one habit: before any feature discussion, write the job story. "When [situation], I want to [motivation], so I can [outcome]." If the team can't agree on the job story, they're not ready to debate the feature.
:::

## Personas

### Where personas came from, and why they go wrong

Alan Cooper introduced personas to software design in *The Inmates Are Running the Asylum* (1999). His point was simple: design for a specific person, not an elastic "user" who can be stretched to justify any feature. John Pruitt and Jonathan Grudin later described persona practice at Microsoft and why it works: teams engage with a specific, named person far more than with an abstract user segment. Pruitt and Tamara Adlin's *The Persona Lifecycle* added the idea that personas are born, used and eventually retired, like any other artifact.

Personas go wrong in predictable ways. They get made once, printed on a poster and never updated. They describe demographics ("Priya, 34, likes hiking") instead of goals and behaviors. And they get invented in a conference room, then treated as research.

### Three kinds of persona

The Nielsen Norman Group distinguishes three kinds, and knowing which one you have is most of the battle:

| Type | Basis | Effort | Use it for |
|---|---|---|---|
| **Proto-persona** | The team's assumptions, no new research | 2 to 4 hour workshop | Exposing disagreement and creating hypotheses to test |
| **Qualitative persona** | 5 to 30 interviews, coded into themes | Weeks | Most product decisions. NN/g calls this the best fit for most teams. |
| **Statistical persona** | Qualitative research plus a survey of 100+ (ideally 500+) respondents, clustered | Months | Pricing, packaging and sizing decisions where segment size matters |

Jeff Gothelf's **proto-persona** technique, described in UX Magazine in 2012, is especially useful in enterprise companies. Executives and team members each sketch the customer they're picturing on a four-quadrant sheet (a sketch and name; behaviors and beliefs; demographics; needs and goals), present them, and consolidate to three to five. The exercise rarely produces accurate personas. What it reliably produces is the discovery that sales, product and the executive team are picturing three different customers. That's worth knowing on day one.

The practical path: start with proto-personas, label them as hypotheses, and graduate to qualitative personas within a quarter. Save statistical personas for decisions that need segment sizes.

### Personas in B2B: the buying group

Consumer products often have one persona who discovers, buys and uses the product. Enterprise products almost never do. The user, the person who signs, the person who can veto and the person who championed the deal internally are different people with different jobs and different anxieties.

Marketing researchers have studied this for more than fifty years. Frederick Webster and Yoram Wind's 1972 model of the **buying center** identified the roles of users, influencers, buyers, deciders and gatekeepers. Robert Miller and Stephen Heiman's *Strategic Selling* popularized the economic buyer, user buyer, technical buyer and coach, and the MEDDIC sales method renamed the coach as the **champion**. Gartner's research on B2B buying describes six buying jobs that the buying group has to complete, in no fixed order: problem identification, solution exploration, requirements building, supplier selection, validation and consensus creation.

For product work, this book recommends a standard B2B persona set. Every enterprise product should have at least these, each with a job story and its main anxiety:

| Persona | Role in the deal | Typical job | Typical anxiety |
|---|---|---|---|
| **End user** | Uses the product daily | Get their own work done faster or better | "This will make my job harder before it makes it easier." |
| **Champion** | Advocates internally and builds the case | Solve a team problem and look good doing it | "If this fails, it's my reputation." |
| **Economic buyer** | Owns the budget and signs | Hit a business target within budget | "I can't prove the ROI to my CFO." |
| **Technical evaluator** | Security, IT or architecture review | Keep the environment safe and supportable | "This creates a risk I'll be blamed for." |
| **Procurement or legal** (gatekeeper) | Contract and vendor approval | Reduce commercial and legal risk | "These terms expose us." |

Map each of Gartner's buying jobs to the persona who owns it. Consensus creation is where enterprise deals stall, so the champion needs artifacts that help them sell internally: an ROI model, a security pack, a reference customer. Those artifacts are product decisions as much as sales ones.

:::leader For product leaders
Persona sets should be shared across a portfolio, not reinvented by every PM. If three products sell to the same economic buyer, they should agree on who that buyer is and what they need. Make the portfolio's persona set a durable artifact owned at the group level, and let each product extend it with its own end users.
:::

## Journey maps

A persona tells you who. A job tells you why. A **journey map** tells you what happens, step by step, as that person tries to make progress, and where it goes wrong.

NN/g's Sarah Gibbons defines a journey map as a visualization of the process a person goes through to accomplish a goal, and lays out its anatomy in three zones:

- **The lens**: one actor (one persona per map) and the scenario, with their expectations.
- **The experience**: the phases of the journey, and for each phase the person's actions, thoughts and emotions (usually drawn as a line of highs and lows).
- **The insights**: the opportunities the map reveals, each with an internal owner and a metric.

Journey maps sit in a family of related tools. An **experience map** is broader and product-agnostic. A **service blueprint**, a technique G. Lynn Shostack introduced in HBR in 1984, extends the journey into the company: the frontstage actions customers see, the backstage actions they don't and the support processes underneath, separated by lines of interaction, visibility and internal interaction. A **user story map** is a planning tool for delivery, covered in Chapter 06.

For B2B products, draw the journey at two levels:

1. **The buying journey**: the buying group working through the six buying jobs, with one swimlane per persona. This is where you discover that the security review takes eleven weeks.
2. **The usage journey**: one end user, one scenario, the classic NN/g map. This is where you discover that time-to-value is lost in onboarding.

Connect the two at the **first value** moment: the point where the customer first gets the outcome they bought. In enterprise products, a service blueprint of onboarding often shows that the time to first value is lost in handoffs between sales, provisioning, support and customer success, not in the product's interface.

## Discovery interviews

Hypotheses, jobs, personas and journeys are all guesses until you talk to customers. Three bodies of work define how to do that well.

### The Mom Test

Rob Fitzpatrick's *The Mom Test* is named for the idea that you should be able to ask your mother about your business idea and get useful answers, even though she loves you and wants to be supportive. It has three rules:

1. Talk about their life instead of your idea.
2. Ask about specifics in the past instead of generics or opinions about the future.
3. Talk less and listen more.

Fitzpatrick identifies three kinds of bad data: **compliments** ("that sounds great"), **fluff** (generic claims, hypotheticals and promises about the future) and **ideas** (feature requests, which you should dig behind to find the problem). The real signal is **commitment**: time, reputation or money. In enterprise products, a pilot, a security-review slot or an introduction to an executive counts as commitment. "We'd definitely use that" doesn't.

The single most useful substitution in discovery: replace "Would you use X?" with "Tell me about the last time you had to do Y. What did you use? What did it cost you?"

### Continuous discovery

Teresa Torres, in *Continuous Discovery Habits*, argues that discovery shouldn't be a phase. It should be a habit: weekly touchpoints with customers, by the team building the product, in pursuit of a desired outcome. She recommends the **product trio** (PM, designer and tech lead) interview at least one customer a week.

Torres's **opportunity solution tree** organizes what you learn:

- The **desired outcome** is the root: the metric the team is trying to move.
- **Opportunities** branch from it: unmet customer needs, pain points and desires, discovered in interviews.
- **Solutions** branch from opportunities.
- **Assumption tests** sit under each solution.

The tree keeps teams from jumping from outcome straight to solution. Revisit the opportunity space every three or four interviews.

Torres's **story-based interviews** collect specific past stories ("Tell me about a time when..."), and her **interview snapshot** captures each one on a single page: the participant, quick facts for context, a memorable quote, the opportunities heard, insights not yet actionable, and a small experience map of the story's key moments.

For a Principal PM, the habit is the point. Automate recruiting (in-product intercepts, customer success referrals, a standing research panel) so the trio talks to a customer every week without anyone having to kick off a project.

### Interviewing craft

Steve Portigal's *Interviewing Users* covers the craft that the other two assume: building rapport, embracing how the participant sees the world, using silence and follow-up questions, and moving from interviewing to sense-making. Use Portigal for how to run the conversation, Fitzpatrick for what to ask, and Torres for cadence and synthesis.

## How to apply it

Here's a six-week method for building the Customer dimension of a Product 360 from scratch, or for testing a major new bet within an existing product.

**Week 1: Write it down.**

1. Draft the three-part product hypothesis: customer, problem, solution. Include the growth (buying-process) assumption.
2. Run a 90-minute proto-persona workshop with the product trio, a sales leader and a customer success leader. Consolidate to three to five personas, including the B2B roles. Label every persona "hypothesis."
3. Write a job story for each persona.
4. List every assumption and map them: desirability, feasibility, viability, adoptability; importance against evidence.

**Week 2: Recruit and prepare.**

5. Write an interview guide that tests the customer and problem hypotheses only. Use the Mom Test rules: past behavior, specifics, no pitching.
6. Recruit 12 to 15 interviews across personas: at least five end users, three champions, two economic buyers and two technical evaluators. Include recent switchers to you and away from you.

**Weeks 3 to 5: Interview continuously.**

7. Run two to five interviews a week as a trio. Write an interview snapshot within 24 hours of each.
8. Every three or four interviews, update the opportunity solution tree and the assumption map. Move assumptions as evidence arrives.
9. For switchers, run the four-forces analysis. Pay special attention to anxiety.

**Week 6: Decide.**

10. Revise the personas from proto to qualitative, based on what you heard. Retire any that didn't show up in reality.
11. Draw the buying and usage journey maps, and mark the opportunities.
12. Rewrite the hypothesis. For each of the three parts, state whether it's confirmed, revised or killed, with the evidence.
13. Make a decision with your manager: proceed to vision and strategy (Chapter 02), pivot the hypothesis and run another cycle, or stop.

Then keep the weekly interview habit going. The Customer dimension is durable, but the discovery log behind it is living.

## The AI lens

### Building AI-powered products

When the product is AI-powered, the customer hypothesis needs a few things that classic hypotheses leave out.

- **The trust threshold.** For any AI output, there's a level of accuracy below which users won't rely on it and a level of consequence above which they won't let it act. Make both part of the problem hypothesis. "SRE leads will accept an AI-proposed root cause if it's right at least [x]% of the time and shows its evidence" is testable. "Users want AI diagnosis" isn't.
- **The delegation job.** AI products, especially agents, change the job from "help me do this" to "do this for me." Those are different jobs with different anxieties. Write both job stories and test which one customers are hiring for. Often it's the first for now and the second later.
- **The technical evaluator's new questions.** For AI products, the technical evaluator persona has a growing list of concerns: where data goes, whether it trains models, what the agent can access, how decisions are logged, and what regulation applies. Chapter 33 covers the regulatory side. In discovery, the point is to interview this persona early, because their anxiety decides adoptability.
- **The persona's AI posture.** Add one field to every persona in an AI product: how they feel about AI doing their work today. Enthusiasts, pragmatists and skeptics behave very differently, and the mix shifts from one segment to the next.

### Doing the work with AI

AI changes discovery work dramatically, mostly in synthesis. User Interviews' *State of User Research 2025* found that 80% of researchers were using AI, up sharply from the prior year, while 91% worried about accuracy and hallucinations. Both findings hold at once, and the practical rules follow from them.

**Where AI helps.** NN/g's Kate Moran and Maria Rosala, in "Accelerating Research with AI," find the biggest gains in planning and analysis: drafting interview guides, transcribing, first-pass coding and clustering of themes, drafting snapshots and summarizing across many interviews. A harness with access to your interview transcripts, support tickets, CRM notes and sales call recordings can draft a first opportunity solution tree far faster than a team working by hand.

**Where AI doesn't help.** AI can't observe behavior, so it shouldn't moderate or analyze usability tests. It can't decide what a story means for your strategy. And it tends to smooth over exactly the things that matter most in discovery: the rare, surprising remark and the subgroup that behaves differently.

**Keep the evidence attached.** Every AI-generated insight should link back to the source quote or clip. If you can't trace a theme to at least two real customers, it's the model's opinion, not a finding.

### The synthetic users debate

The most contested AI practice in discovery is the **synthetic user**: an AI-generated respondent meant to stand in for a real customer. The evidence is now strong enough to give clear guidance.

NN/g's 2024 analysis by Rosala and Moran found synthetic users to be sycophantic and idealized. They "care about everything," so they can't prioritize; they can't report real past behavior because they don't have any; and they're weakest for niche groups. In October 2026, NN/g published an empirical comparison of 120 synthetic respondents against 604 human respondents to the same survey. The headline conclusions roughly matched, but humans produced more than fifty distinct labels for their own field where the synthetic respondents produced about a dozen: a collapse in variety that hides exactly the edge cases discovery exists to find.

The strongest evidence for AI respondents comes with an important caveat. A 2024 Stanford-led study (Park and colleagues) built AI agents from two-hour interviews with 1,052 real people, and those agents replicated each person's survey answers about 85% as well as the people replicated their own answers two weeks later. But each agent was grounded in an interview with one specific, real person. That's a digital twin of a participant you already researched, not a persona invented from a prompt.

The rules for an enterprise PM:

- **Use synthetic users to prepare.** Pilot an interview guide, explore an unfamiliar domain, or generate a first set of proto-personas to test.
- **Never present synthetic output as research.** Label it hypothesis, and validate it with real customers.
- **Be most skeptical where B2B insight matters most.** Niche roles, buying-group politics and long-tail edge cases are exactly where synthetic users are weakest.

:::ai The one-line rule
AI can draft, cluster and summarize what customers said. It can't tell you what customers would say, and it can't decide what it means. Supplement human research with AI; don't substitute for it.
:::

## The Beacon case: testing the Beacon Agents hypothesis

:::example Where Beacon starts
Beacon's leadership wants to move from "correlate and summarize" to Beacon Agents: AI agents that diagnose incidents and run approved remediation steps. The strategy deck assumes SRE teams want it. Your Product 360 inventory (Chapter 00) showed that the existing personas are all end users from 2024, with no economic buyer or security reviewer. Before the Agents roadmap gets committed, you test the hypothesis.
:::

**The hypothesis.** You write it in three parts:

- *Customer:* We believe SRE and platform teams of 20 to 100 engineers at enterprises already using Beacon for alert correlation...
- *Problem:* ...lose most of each incident to diagnosis (finding which change, service or dependency caused it), which costs them [time to resolve, on-call burnout and SLA penalties].
- *Solution:* We believe an agent that proposes a root cause with cited evidence, and runs allowlisted remediation steps after human approval, will cut diagnosis time by at least half. We'll know we're right when responders accept the agent's diagnosis in at least 60% of incidents during a 30-day pilot.
- *Growth (buying process):* Security teams will approve agent write access to production for allowlisted actions.

**The assumption map.** The trio maps 22 assumptions. Three land in the top-right quadrant: security will approve write access; responders will accept AI root causes; and buyers will pay per resolved incident. None of them is a feature assumption.

**The proto-personas.** The workshop produces five personas, and an immediate surprise. The sales leader pictures the buyer as a VP of IT Operations; the CTO pictures an SRE lead. Both exist: Marcus (VP of IT Operations) is the economic buyer and Priya (SRE lead) is the champion. Dana (on-call engineer) is the end user, Sam (security and compliance reviewer) is the technical evaluator and Leo (MSP operations manager) is the partner persona. Nobody had previously written down Sam.

**The interviews.** Over three weeks the trio runs 14 interviews: six on-call engineers, three SRE leads, two VPs, two security reviewers and one MSP. They include two customers who left Beacon for a competitor's AIOps feature.

What they hear:

- **The problem is confirmed, with a twist.** Diagnosis really is most of the incident. But the most-cited cost is on-call burnout and attrition, ahead of MTTR. Marcus cares about MTTR because his CFO does; Priya cares about keeping her team. That changes the positioning conversation in Chapter 24.
- **The solution is half-confirmed.** Engineers want the diagnosis badly ("just tell me which deploy did it"). They are far more cautious about the agent acting. Several describe a specific incident where an automated remediation script made an outage worse.
- **Anxiety lives with Sam.** Both security reviewers say they'd block agent write access without per-action audit logs, scoped credentials and a kill switch. One says they'd also need documentation for EU AI Act obligations, because their company sells in Europe.
- **The two switchers** left because the competitor's feature was bundled into a platform they already paid for. The push was price and procurement simplicity, not capability. That's a strategy signal for Chapter 03.

**The decision.** You rewrite the hypothesis. The customer hypothesis holds. The problem hypothesis is revised: burnout joins MTTR as a primary cost. The solution hypothesis is split in two. Diagnosis ships first, aiming at a 60% acceptance rate. Supervised action follows, gated on security features (audit logs, scoped credentials, a kill switch) that move from "later" to "now" on the roadmap. The growth assumption is replaced: security will approve write access *if* those controls exist, which becomes the next assumption to test with a design partner.

Sam is now a formal persona in the Product 360, with a job story: *"When a new tool asks for production access, I want to see exactly what it can do and how to revoke it, so I can approve it without becoming the person who gets blamed for the next outage."*

## Product 360 artifacts

```template id="product-hypothesis" title="Product hypothesis"
# Product hypothesis · [Product or initiative] · v[n] · [Date]

**Owner:** [PM]   **Status:** Draft / Testing / Confirmed / Revised / Killed

## Customer hypothesis
We believe [specific segment, role and context]...

## Problem hypothesis
...experience [problem] when [situation], which costs them [measurable consequence].

## Solution hypothesis
We believe [solution concept] will solve this.
We will know we are right when [observable signal] reaches [threshold] within [timeframe].

## Growth or buying-process hypothesis
We believe customers will discover and adopt this by [channel or buying process], and that [buying-group gate, such as security or procurement] will approve it because [reason].

## Business outcome
If the hypothesis holds, the business outcome is [metric and target]. The customer outcome is [metric and target].

## Riskiest assumptions (from the assumption map)
1. [Assumption] · Type: desirability / feasibility / viability / adoptability · Test: [smallest test] · Signal: [what would falsify it]
2.
3.

## Evidence log
| Date | Source (interview, data, test) | What we learned | Effect on hypothesis |
|---|---|---|---|
| | | | |

## Decision
[Proceed / pivot / stop], decided by [name] on [date]. Reason: [one paragraph].
```

```template id="assumption-map" title="Assumption map"
# Assumption map · [Product or initiative] · [Date]

| # | Assumption | Type (D/F/V/A) | Importance (H/M/L) | Evidence today (strong/some/none) | Quadrant | Test | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |

Types: D = desirability (do they want it?), F = feasibility (can we build it?), V = viability (should we, financially?), A = adoptability (will the buying group, security and procurement let it through?).

## Test first (important, little evidence)
1.
2.
3.

## Review rhythm
Update after every three or four interviews or tests. Move assumptions between quadrants as evidence arrives, and note why.
```

```template id="opportunity-assessment" title="Opportunity assessment"
# Opportunity assessment · [Opportunity] · [Date]

**Owner:** [PM]   **Decision needed by:** [Date]   **Decision maker:** [Name]

1. **Exactly what problem will this solve?** (value proposition)
2. **For whom do we solve that problem?** (target personas and segments)
3. **How big is the opportunity?** (market size and how it was estimated)
4. **What alternatives are out there?** (competitors, substitutes, build-it-yourself, do nothing)
5. **Why are we best suited to pursue this?** (our differentiator)
6. **Why now?** (market window)
7. **How will we get this product to market?** (go-to-market approach)
8. **How will we measure success and make money?** (metrics and revenue model)
9. **What factors are critical to success?** (solution requirements and riskiest assumptions)
10. **Recommendation:** go, no-go or investigate further, with the next decision point.

Adapted from Marty Cagan's ten opportunity-assessment questions.
```

```template id="b2b-persona" title="B2B persona"
# Persona · [Name], [Role]

**Type:** Proto (hypothesis) / Qualitative / Statistical   **Evidence:** [number of interviews, sources]   **Owner:** [PM]   **Last validated:** [Date]   **Retire by:** [Date or condition]

## Role in the deal
End user / Champion / Economic buyer / Technical evaluator / Procurement or legal / Partner

## Context
- Organization type and size:
- Team and reporting line:
- Tools they use today:
- What they're measured on:

## Job story
When [situation], I want to [motivation], so I can [expected outcome].

## Goals
1.
2.

## Pains (in their words)
- "[Quote]" (interview #, date)
- "[Quote]"

## Four forces
- Push (what's wrong today):
- Pull (the better future they imagine):
- Anxiety (what worries them about switching):
- Habit (what keeps them where they are):

## AI posture (AI products only)
Enthusiast / Pragmatist / Skeptic, with evidence:

## What they need from us to say yes
[Proof points, artifacts, controls, references]

## Buying jobs they own
Problem identification / Solution exploration / Requirements building / Supplier selection / Validation / Consensus creation
```

```template id="job-statements" title="Job stories and desired outcomes"
# Jobs · [Product] · [Date]

## Job stories (one per persona and situation)
| Persona | When (situation) | I want to (motivation) | So I can (outcome) | Evidence |
|---|---|---|---|---|
| | | | | |

## Job map (for one core job)
| Step | What the customer is doing | Desired outcomes (direction + metric + object + context) |
|---|---|---|
| Define | | |
| Locate | | |
| Prepare | | |
| Confirm | | |
| Execute | | |
| Monitor | | |
| Modify | | |
| Conclude | | |

## Opportunity scoring (if surveyed)
| Desired outcome | Importance (0 to 10) | Satisfaction (0 to 10) | Opportunity = I + max(I − S, 0) |
|---|---|---|---|
| | | | |
```

```template id="journey-map" title="Customer journey map"
# Journey map · [Persona] · [Scenario] · [Date]

**Journey type:** Buying journey / Usage journey   **Evidence:** [sources]

## Lens
- Actor:
- Scenario:
- Expectations:

## Experience
| Phase | [Phase 1] | [Phase 2] | [Phase 3] | [Phase 4] | [Phase 5] |
|---|---|---|---|---|---|
| Actions | | | | | |
| Thoughts | | | | | |
| Emotion (−2 to +2) | | | | | |
| Touchpoints | | | | | |
| Backstage (who at our company is involved) | | | | | |
| Pain points | | | | | |

## First value
The moment the customer first gets the outcome they bought: [describe]. Median time to reach it today: [time].

## Opportunities
| Opportunity | Phase | Owner | Metric | Priority |
|---|---|---|---|---|
| | | | | |
```

```template id="discovery-interview-guide" title="Discovery interview guide"
# Discovery interview guide · [Topic] · [Date]

**Hypothesis under test:** customer / problem (not solution)   **Persona:** [persona]   **Length:** 45 minutes

## Before the call
- Learning goals (max three):
  1.
  2.
  3.
- What would change our mind:

## Opening (5 min)
- Thank them, explain we're learning, not selling. Ask permission to record.
- "Tell me about your role and what a typical week looks like."

## The story (25 min)
- "Tell me about the last time [the situation] happened."
- "What happened first? Then what?"
- "Who else was involved?"
- "What did you use to deal with it? Why that?"
- "What did it cost you: time, money, stress, reputation?"
- "What have you tried to fix it? What happened?"
- "If it happened again tomorrow, what would you do?"

## Switching (if they recently changed tools) (10 min)
- "When did you first think something had to change?"
- "What made you start looking? What did you look at?"
- "What almost stopped you?"
- "What would make you switch away?"

## Close (5 min)
- "Is there anything I should have asked?"
- "Who else should I talk to?"
- Ask for a commitment: a follow-up, an intro, a pilot.

## Rules
Ask about past specifics, not future hypotheticals. Don't pitch. Dig behind feature requests to the problem. Silence is a tool.
```

```template id="interview-snapshot" title="Interview snapshot"
# Interview snapshot · [Participant] · [Date]

**Persona:** [persona]   **Interviewers:** [trio]   **Recording:** [link]

## Quick facts
[Context that matters: company, team size, tools, role]

## Memorable quote
"[Quote]"

## The story in five moments
1.
2.
3.
4.
5.

## Opportunities heard (needs, pains, desires)
-
-

## Insights (notable, not yet actionable)
-

## Evidence for or against the hypothesis
| Assumption | For / Against / Neutral | Evidence |
|---|---|---|
| | | |

## Commitment offered
[None / follow-up / intro / pilot / other]
```

## Prompts

```prompt title="Pressure-test a product hypothesis"
Goal: Find the weakest part of your hypothesis before customers do.
Paste in: your three-part product hypothesis, growth assumption and any evidence you already have.

Act as a skeptical product leader reviewing this hypothesis for [product]. 

1. Rewrite it so the customer, problem and solution parts can each be proven false on their own. Flag any part that's untestable as written.
2. List at least 15 assumptions underneath it. Classify each as desirability, feasibility, viability or adoptability (will the buying group, security and procurement let it through?).
3. Rate each assumption's importance (H/M/L) and the evidence I've provided (strong/some/none). Show the top-right quadrant: important, little evidence.
4. For the top three, propose the smallest, fastest test and the result that would falsify it.
5. Name the two customer alternatives I seem to be underestimating, including "do nothing."

Don't soften the critique. Don't invent evidence I haven't given you.

[hypothesis and evidence]

Check the output: are the top-three assumptions really the ones that would kill the product? If the model ranked a feature preference above a buying-process or trust assumption, push back.
```

```prompt title="Draft proto-personas from existing company data"
Goal: Get a first set of proto-personas to test, built from what the company already knows.
Paste in (or connect the harness to): CRM opportunity notes, win/loss notes, sales call summaries, support tickets and any existing personas. Use only tools approved for customer data, and remove personal identifiers first.

From the material provided for [product], draft proto-personas for an enterprise buying group: end user, champion, economic buyer, technical evaluator and procurement or legal, plus any role that appears repeatedly.

For each persona give: role in the deal, context, a job story ("When..., I want to..., so I can..."), goals, pains quoted from the material with source references, the four forces (push, pull, anxiety, habit) and what they need to say yes.

Rules:
- Every claim must cite the source document. If the material doesn't support a field, write "No evidence yet."
- Mark every persona "Proto-persona: hypothesis to test."
- Note where different sources seem to describe different people in the same role.

Check the output: read three of the cited sources and confirm the quotes and paraphrases are accurate. Treat the personas as the starting point for interviews, not their conclusion.
```

```prompt title="Write a Mom Test interview guide"
Goal: Produce an interview guide that tests the problem, not your solution.
Paste in: the customer and problem hypotheses, the persona you'll interview and your three learning goals.

Write a 45-minute discovery interview guide for [persona] to test this customer and problem hypothesis: [hypothesis]. 

Follow the Mom Test rules: ask about specific past events, not future hypotheticals or opinions; never describe our solution; dig behind any feature request to the underlying problem. Include an opening, a story section built around "Tell me about the last time...", a switching section for people who recently changed tools, and a close that asks for a concrete commitment.

After the guide, list five questions I might be tempted to ask that would produce bad data (compliments, fluff or ideas), and rewrite each one.

Check the output: delete any question that mentions our product or asks "would you." Read the guide aloud; if it sounds like a sales call, rewrite it.
```

```prompt title="Turn an interview transcript into a snapshot"
Goal: Capture each interview on one page within a day.
Paste in: one interview transcript, the persona and the current list of assumptions under test. Use an approved tool for customer recordings.

Create an interview snapshot from this transcript with these sections: quick facts, one memorable quote (verbatim), the story in five key moments, opportunities heard (needs, pains and desires, phrased from the customer's point of view and free of solutions), insights not yet actionable, evidence for or against each assumption listed, and any commitment offered.

Rules:
- Quote verbatim, with timestamps. Never paraphrase inside quotation marks.
- If the participant talked about the future or gave an opinion rather than a past example, label it "opinion" and weight it lower.
- Don't infer things the participant didn't say.

[assumptions]
[transcript]

Check the output: play the clip at two of the timestamps and confirm the quotes. Make sure the opportunities are problems, not features.
```

```prompt title="Synthesize interviews into an opportunity solution tree"
Goal: Find the patterns across many interviews without losing the evidence.
Paste in: all interview snapshots so far, the desired outcome (the metric the team is trying to move) and the current assumption map.

Using these interview snapshots for [product], build an opportunity solution tree with this desired outcome at the root: [outcome].

1. Cluster the opportunities heard into parent and child opportunities. Name each from the customer's point of view.
2. For each opportunity, list the participants who raised it (by snapshot ID), with a representative quote, and how many personas it spans.
3. Flag any opportunity raised by only one participant as "single source," and any that appears only in one persona.
4. Identify surprises: opportunities that contradict our hypothesis or appear in an unexpected persona.
5. Update the assumption map: which assumptions gained or lost evidence?

Don't propose solutions yet.

Check the output: every opportunity should trace to at least one real quote. Read the single-source and surprise items yourself; they're where models are most likely to over-generalize, and also where the best insights often hide.
```

```prompt title="Pilot an interview guide with a synthetic respondent"
Goal: Find confusing or leading questions before you spend a real customer's time.
Paste in: your interview guide and a short description of the persona.

Role-play as a [persona description] being interviewed with this guide. Answer each question in character, briefly. Then step out of character and tell me:
1. Which questions were confusing, leading or likely to produce opinions rather than past stories.
2. Which questions a real person in this role might refuse or be unable to answer, and why.
3. What important topic the guide doesn't cover.

Important: your in-character answers are not research and will not be used as evidence. I only want feedback on the guide.

[guide]

Check the output: use only the guide feedback. Discard the in-character answers entirely.
```

## Anti-patterns

:::warn The bundled hypothesis
"Enterprises want an AI agent for incidents" gets tested as one bet. When the pilot disappoints, nobody can tell whether the customer, the problem or the solution was wrong. Split the hypothesis, and test the customer and problem before the solution.
:::

:::warn Personas as posters
Beautifully designed personas with stock photos and hobbies, made once and never updated. Personas are artifacts with owners, evidence and retirement dates. If a persona hasn't been validated against a real conversation in six months, mark it stale.
:::

:::warn The user-only persona set
Every persona is a user. Nobody wrote down the economic buyer, the security reviewer or procurement, so the product delights users and dies in the buying process. Every enterprise product needs the buying group.
:::

:::warn Asking about the future
"Would you use this?" "How much would you pay?" "Is this a problem for you?" Each produces polite, useless answers. Ask about the last time it happened, what they did and what it cost.
:::

:::warn Synthetic research presented as real
An AI-generated survey of "500 enterprise buyers" appears in a strategy deck. It's fluent, confident and fictional. Synthetic output is for preparing research, never for replacing it.
:::

:::warn Discovery as a phase
The team does six weeks of research before a big build, then stops talking to customers for a year. Make discovery a weekly habit with automated recruiting, so the evidence keeps arriving after the strategy is set.
:::

## Checklist

- [ ] The product hypothesis is written in three parts (customer, problem, solution) plus a growth or buying-process assumption, and each part can be falsified on its own.
- [ ] Every assumption is on an assumption map, classified as desirability, feasibility, viability or adoptability, and the top-right quadrant has tests assigned.
- [ ] Major bets have a one-page opportunity assessment with a recommendation and a decision maker.
- [ ] Each persona has a job story, and the core job has a job map with desired outcomes.
- [ ] The persona set includes the full B2B buying group: end user, champion, economic buyer, technical evaluator and procurement or legal.
- [ ] Every persona is labeled proto, qualitative or statistical, with its evidence and last-validated date.
- [ ] Buying and usage journey maps exist and connect at the first-value moment.
- [ ] The interview guide tests the problem, not the solution, and follows the Mom Test rules.
- [ ] At least 12 interviews across personas are complete, each with a snapshot, including recent switchers.
- [ ] The opportunity solution tree traces every opportunity to real quotes.
- [ ] For AI products, the hypothesis states trust thresholds and the personas record AI posture.
- [ ] No synthetic or AI-generated output is presented as customer evidence.
- [ ] The hypothesis has been revised with evidence, and a proceed, pivot or stop decision is in the decision log.
- [ ] A weekly interview habit with automated recruiting is running.

## Key takeaways

- A product idea is several bets stacked together. Split it into customer, problem and solution hypotheses, and test the first two before showing anyone the third.
- Map every assumption by type and by importance against evidence. In B2B, add adoptability: the security review and the buying group often kill products that users want.
- Jobs to be done tells you why customers would buy anything. Use switch interviews and the four forces to understand switching, job stories to frame features and Ulwick's outcome scores to prioritize at scale.
- Enterprise personas must include the buying group. The economic buyer, champion, technical evaluator and procurement each have a different job and a different anxiety.
- Discovery is a weekly habit, not a phase. Ask about the past, talk less and treat commitment as the only real signal.
- AI is good at drafting guides and synthesizing transcripts, and unreliable at standing in for customers. Keep every insight linked to a real quote, and label synthetic output as hypothesis.
