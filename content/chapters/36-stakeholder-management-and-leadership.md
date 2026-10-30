<p class="lead">A Principal PM rarely manages the people whose help they need. Sales, finance, legal, security, support and your own manager all hold part of every decision you care about. This chapter covers the craft of working through them: mapping who matters, trading in what they value, settling who decides, saying no without burning trust, and, once you lead other PMs, building the team and culture that make the rest easier.</p>

## Why this matters

In an enterprise software company, many product failures that look like strategy failures are alignment failures. The roadmap was sound, but finance found out about the pricing change two weeks before launch. The agent worked, but security saw the access model for the first time in a customer escalation. The launch was ready, but sales had promised a connector nobody had agreed to build. Each of these is a stakeholder problem, and each is cheaper to prevent than to repair.

Cheap building raises the stakes. When a team can prototype a feature in days with AI tools, the constraint moves to deciding what to build and getting the people around the product to back it. Marty Cagan's July 2026 essay on what he calls the AI productivity paradox argues that output is up while outcomes often are not, and that the bottleneck is choosing well. In a B2B company, choosing well is a group activity: you need the evidence, and you need the people who can block, fund or sell the result to agree with it.

Seniority changes the job as well. Ravi Mehta's PM competency model, which he updated in August 2026, describes how expectations shift by level: early-career PMs are judged on execution, Senior PMs on shaping features from customer insight, group PMs and directors on connecting work to vision and strategy, and senior leaders on working mainly through people, managing up and across. A Principal PM sits on the boundary between the last two: expected to move outcomes you do not control, through people who do not report to you, while raising the PMs around you.

The chapter has two halves that share one skill set. **Stakeholder management** covers mapping, influence, decision rights, alignment, conflict, managing up and leading across functions. **Product leadership** covers hiring and growing PMs, coaching, team charters, culture, and leading a product organization through the changes AI is forcing in 2026. Chapter 34 covers the writing and Chapter 35 the meetings through which most of this work happens; this chapter covers the relationships and decisions underneath them.

## Core concepts and frameworks

### Who counts as a stakeholder

A stakeholder is anyone who can affect your product's outcome or is affected by it, and who is not on the team building it. Cagan's model of empowered product teams treats the PM, the designer and the tech lead as one team with split accountability: the PM for value and viability, the designer for usability and the tech lead for feasibility. Engineering and design are your team. If you find yourself managing your own engineers as stakeholders, look at how the team was chartered.

For a B2B or platform product, stakeholders fall into two groups, and it helps to map them separately.

- **Internal**: your manager and the executive team, peer PMs whose products you depend on or compete with for resources, sales, marketing, support and customer success, finance, legal, security and compliance, partner teams, and product operations.
- **External**: the customer's economic buyer, champion and security reviewer, partners who build on or resell your product, and sometimes regulators or standards bodies.

Chapter 01 treats the external buying group as personas. Here both groups are relationships, each with a current position, a desired position and a plan to close the gap.

### Stakeholder mapping: the power-interest grid

The most common tool for sorting stakeholders is the power-interest grid, usually attributed to Aubrey Mendelow. Mendelow's 1981 conference paper on environmental scanning argued that how an organization watches its environment should depend on how dynamic that environment is and on each stakeholder's relative power. The familiar two-by-two with action labels in each quadrant is a later practitioner adaptation of that idea. Treat it as a useful convention, not as Mendelow's own diagram.

The grid plots power (the ability to change your outcome) against interest (how much attention they pay to it):

| Quadrant | Power | Interest | Default engagement |
|---|---|---|---|
| **Manage closely** | High | High | Involve in decisions, co-create, meet often |
| **Keep satisfied** | High | Low | Brief and concise; raise only what touches their goals |
| **Keep informed** | Low | High | Regular updates and an early-warning channel; use them as a signal |
| **Monitor** | Low | Low | Light touch; watch for movement |

For enterprise and platform work, this book adds three extensions.

**Add stance.** Power and interest say how much attention someone deserves. They say nothing about whether that person is with you. Add a third attribute for each stakeholder: champion, supporter, neutral, skeptic or blocker. A high-power skeptic and a high-power champion sit in the same quadrant and need completely different plans.

**Draw the move.** For each important stakeholder, mark where you need them to be, and by when. The arrows turn the map into a plan.

**Watch the sleeping gatekeepers.** In enterprise software, the people with the most power over a launch are often the least interested until late: security, legal, procurement and finance. Left in "keep satisfied" or "monitor," they surface in the last two weeks with a veto. Move gatekeepers to "manage closely" early, deliberately, even when they are not asking for attention.

<figure class="fig" markdown="0">
<svg viewBox="0 0 660 400" role="img" aria-label="Power-interest grid for the Beacon Agents launch, with arrows showing where stakeholders need to move">
  <rect x="90" y="20" width="270" height="160" rx="10" class="box"/>
  <rect x="370" y="20" width="270" height="160" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".6"/>
  <rect x="90" y="190" width="270" height="160" rx="10" class="box"/>
  <rect x="370" y="190" width="270" height="160" rx="10" class="box"/>
  <text x="105" y="44" class="t">Keep satisfied</text>
  <text x="385" y="44" class="t" style="fill:var(--a1)">Manage closely</text>
  <text x="105" y="214" class="t">Monitor</text>
  <text x="385" y="214" class="t">Keep informed</text>
  <circle cx="130" cy="80" r="6" fill="var(--a2)"/><text x="142" y="84" class="s">Security and legal</text>
  <circle cx="130" cy="118" r="6" fill="var(--a2)"/><text x="142" y="122" class="s">Finance</text>
  <circle cx="130" cy="156" r="6" fill="var(--a2)"/><text x="142" y="160" class="s">Sales leadership</text>
  <circle cx="400" cy="80" r="6" fill="var(--a1)"/><text x="412" y="84" class="s">VP of Product (your manager)</text>
  <circle cx="400" cy="118" r="6" fill="var(--a1)"/><text x="412" y="122" class="s">Product marketing</text>
  <circle cx="400" cy="250" r="6" fill="var(--a3)"/><text x="412" y="254" class="s">Support lead</text>
  <circle cx="400" cy="288" r="6" fill="var(--a3)"/><text x="412" y="292" class="s">Observe and Desk group PMs</text>
  <circle cx="130" cy="250" r="6" fill="var(--muted)"/><text x="142" y="254" class="s">Partner team</text>
  <line x1="262" y1="80" x2="388" y2="140" class="ln" stroke-dasharray="5 4"/>
  <line x1="208" y1="118" x2="388" y2="152" class="ln" stroke-dasharray="5 4"/>
  <line x1="258" y1="156" x2="388" y2="164" class="ln" stroke-dasharray="5 4"/>
  <line x1="580" y1="282" x2="580" y2="166" class="ln" stroke-dasharray="5 4"/>
  <text x="520" y="152" class="s">Move by launch</text>
  <line x1="90" y1="368" x2="640" y2="368" class="ln"/>
  <text x="365" y="388" text-anchor="middle" class="s">Interest: low ← → high</text>
  <text x="40" y="185" text-anchor="middle" class="s" transform="rotate(-90 40 185)">Power: low ← → high</text>
</svg>
<figcaption>A power-interest grid for the Beacon Agents launch. Security, legal, finance and sales leadership hold high power but low interest, so the plan moves them into "manage closely" well before launch. The peer group PMs move up because the build-on-Observe question gives them a real stake in the decision.</figcaption>
</figure>

Map internal and external stakeholders on separate grids, because you reach your CFO and a customer's security reviewer through entirely different channels.

### Influence without authority: the exchange model

Allan Cohen and David Bradford's *Influence Without Authority*, now in its third edition (2017), is built on one idea they call the Exchange Model. You get cooperation from people you do not manage by offering something they value in return. Cohen and Bradford call the things people value **currencies**, and influence depends on knowing which currencies the other person cares about and which ones you can pay in.

Used as a ledger of favors, the model turns transactional. Its real use is diagnostic: before you ask anyone for anything, you work out what they are measured on, what pressures they face this quarter and what would make their job easier, then look for a trade that leaves both sides better off.

Cohen and Bradford list many currencies. For a B2B PM, this book groups the ones you can actually pay in into four kinds:

- **Information**: customer evidence, early visibility into the roadmap, a heads-up before a change lands on someone's team.
- **Task help**: a feature flag that unblocks a deal, a field-ready demo, a known-issues page that cuts support's escalations.
- **Visibility**: crediting a sales engineer's customer insight in an executive review, putting a support lead's analysis in front of the VP.
- **Direction**: a credible vision people want to be part of, and a clear answer to "why are we doing this?"

The quickest way to find someone's currency is to find their metric: bookings this quarter for sales, ticket volume and satisfaction for support, margin and forecast accuracy for finance, risk exposure for legal. "This will lift adoption" asks support for a favor. "This removes the top cause of escalations from your queue" offers them a trade.

:::key Diagnose before you ask
Before any significant ask, write one line for the person you need: what they are measured on, what they are worried about this quarter, and what you can offer that moves either. If you cannot fill in the line, you are not ready to ask.
:::

### Decision rights: DACI and RAPID

Contentious decisions usually stall on authority rather than data. Two people each believe they hold the final call, a third believes they hold a veto, and the debate about options becomes a proxy fight. Write down decision rights before the debate starts.

The **DACI** format, as Atlassian's Team Playbook describes it, assigns four roles:

- **Driver**: gathers the stakeholders and information, sets the scope and gets a decision made by the agreed date.
- **Approver**: the one person who makes the decision. The playbook is emphatic that there is exactly one.
- **Contributors**: subject-matter experts who have a voice but no vote.
- **Informed**: people affected by the outcome who are told afterward, with no voice or vote.

Atlassian's template opens with the decision phrased as a question ("DACI: [question we're trying to answer]?"), then background, relevant data, decision factors, options with pros, cons and cost, and the outcome, which is shared and recorded.

Bain and Company's **RAPID** format splits the roles differently: Recommend, Agree, Perform, Input and Decide. Bain's guidance matches Atlassian's on the core point, that ideally one person decides, and adds a role DACI lacks. The **Agree** role is a veto, reserved for must-meet requirements such as legal or regulatory constraints, and Bain advises using it sparingly. If a group must decide, Bain recommends agreeing up front on how a deadlock gets broken.

| Situation | Use | Why |
|---|---|---|
| A product decision with many opinions and no formal veto | DACI | Separates the one decider from the many contributors |
| A decision where legal, security or compliance can block | RAPID, or DACI with a "Must agree" row | Makes the veto explicit and early instead of implicit and late |
| A decision that will be executed by another team | RAPID | The Perform role names who has to carry it out |
| A recurring decision type (pricing exceptions, deal requests) | Either, written once into the team charter | Removes the authority debate from every instance |

For enterprise AI products, security and legal reviewers often hold a legitimate block on anything that touches production systems or customer data. Labeling them "Contributors" hides that. Name the veto, and bring the reviewer in early enough that their requirements shape the options instead of killing the chosen one.

### Alignment practices

Decision rights tell you who decides. Alignment practices make sure the decision sticks.

- **Pre-wiring.** Meet each key stakeholder one-on-one before the group meeting. Show them the recommendation, hear their objection in private and adjust where it is fair. Nobody should see your proposal for the first time in a room where they have to react in public.
- **Written pre-reads.** Send the decision document ahead and spend the meeting on disagreements (Chapter 34 covers the writing).
- **A decision log.** Record each decision, its date, the Approver, the options rejected and the reason, so that six months later nobody relies on memory.
- **Disagree and commit.** Amazon's leadership principles describe the norm well: leaders challenge decisions they disagree with, respectfully and even when it is uncomfortable, and then commit fully once the decision is made. The second half matters as much as the first. A stakeholder who reopens a logged decision without new evidence is breaking the agreement.
- **A standing escalation path.** Atlassian's Working Agreements play includes an explicit escalation process: who decides when the team cannot, and how the decision gets shared. Write yours down before you need it.

### Managing conflict and saying no

Most stakeholder conflict in B2B products comes from five places: deal-driven requests from sales, launch timing with marketing, escalations from support, margin with finance, and risk with legal and security. Each function is defending its own metric, so treat the conflict as a clash of measures and look for the trade.

Chris Jones and Marty Cagan's December 2025 essay on stakeholders and the product model gives PMs a useful frame, written as asks of the stakeholders themselves. Stakeholders should share the business context and constraints they own (go-to-market, regulation, financials, partnerships). They should bring problems, with who is affected and how success will be measured, rather than features. They should review prototypes early rather than long documents. And they should ask for firm-date commitments, which Jones and Cagan call high-integrity commitments, only when a date truly matters.

That frame is also the script for saying no. When a request arrives as a feature, convert it into the underlying problem, its owner and its success measure. Then decide it on the same criteria as everything else on the roadmap. Four responses cover most cases:

| Response | When to use it | What you commit to |
|---|---|---|
| **"Not now, and here is when we'll revisit."** | The problem is real but lower priority than current work | A date tied to evidence, such as "after the Q1 adoption review" |
| **"Yes, if."** | The request is worth doing at the cost of something else | Naming what drops, and getting the owner of that work to agree |
| **"No, and here is an alternative."** | A workaround, configuration, partner or integration solves the problem | Helping make the alternative work |
| **"No, and here is why."** | The request conflicts with strategy or the evidence | The reasoning, in writing, so it can be challenged |

Say no to the request, never to the person, and put the decision and its reason in writing. When you and a peer cannot settle a disagreement, escalate together: "We disagree on X. We both want Y. Please decide by Friday." A joint escalation gets a fast decision and keeps the relationship intact; going around a peer rarely does.

Kim Scott's Radical Candor framework helps with the conversation itself. Scott plots feedback on two dimensions, caring personally and challenging directly. Doing both is radical candor; caring without challenging is ruinous empathy; challenging without caring is obnoxious aggression; doing neither is manipulative insincerity. PMs who struggle to say no are usually stuck in ruinous empathy: they say yes to protect the relationship, fail to deliver, and damage it more than an honest no would have.

### Managing up

John Gabarro and John Kotter's Harvard Business Review article "Managing Your Boss," first published in 1980, makes a simple claim: the relationship with your manager is one of mutual dependence between two fallible people, and it deserves deliberate time and energy. The version commonly taught from their work has three parts. Understand your manager's goals, pressures, strengths, weaknesses and preferred way of working. Understand your own. Then build a relationship that fits both, with clear mutual expectations, a steady flow of information, dependability and honesty, and careful use of your manager's time.

Will Larson's 2026 writing on engineering leadership adds a reason this matters more now. He describes middle management as largely balancing pressure from executives, peers and teams, and argues that getting the benefit of AI-era speed requires fast, binding executive decisions when teams disagree. Your manager cannot make those decisions quickly if you bring status instead.

Three practices follow:

1. **Bring decisions, not status.** For each item that needs your manager, state the decision, your recommendation, the deadline and what happens if it slips.
2. **No surprises.** Bad news travels up from you before it arrives from anyone else. Your manager should never learn about a risk to your product in someone else's meeting.
3. **A weekly written update.** Outcomes moved, decisions needed, risks and asks, on one page. It replaces most status meetings and gives your manager material to manage up in turn.

### Leading across functions

Each function around the product has its own metric, its own calendar and its own way of being let down by product. Leading across them means knowing all three.

| Function | What they are measured on | What they need from product | What product needs from them |
|---|---|---|---|
| **Sales** | Bookings and pipeline this quarter | Roadmap themes with confidence levels (not dates), a clear way to raise deal requests, early access for sales engineers | Go-to-market context, deal patterns, honest loss reasons |
| **Marketing** | Pipeline, launch reach, positioning | Evidence, customer stories, a clear line between generally available and preview | Positioning and launch-tier discipline (Chapters 24 and 25) |
| **Support and success** | Ticket volume, resolution time, satisfaction, retention | Known-issues lists, agreed severity definitions, a fix path | Escalation and ticket themes as discovery input (Chapter 27) |
| **Finance** | Margin, forecast accuracy, plan attainment | Pricing and packaging logic, cost assumptions, early warning on margin changes | Business context, planning constraints (Chapter 15) |
| **Legal and security** | Risk exposure, compliance | Early involvement on data use, AI risk documentation and contracts | Requirements early enough to design for them (Chapter 33) |

For deal requests, give sales a structured intake: the problem, the account, the revenue at stake, the deadline and whether other customers share the need. It converts features into problems before they reach you and turns one-off escalations into evidence you can aggregate. Chapter 27 covers the enablement side of the sales relationship and Chapter 29 the business reviews where these conversations become formal.

:::onramp If you're newer to the PM role
Pick the two functions you work with least, and book a 30-minute conversation with someone in each. Ask three questions: what are you measured on, what did product do last quarter that made your job harder, and what is one thing we could do that would help? Write down the answers. That is your first stakeholder map.
:::

### Hiring and growing PMs

Product leadership starts with a written picture of what good looks like. Without one, hiring runs on taste, promotion on visibility, and coaching has no target.

Ravi Mehta's competency model is a useful starting point. It groups PM work into four areas (product execution, customer insight, product strategy and influencing people) and twelve competencies, including product delivery, product definition, fluency with data, voice of the customer, product vision and roadmapping, and business outcome ownership. Two features of the model are worth copying. Expectations shift by level, so a Senior PM and a Director are judged on different competencies. And business outcome ownership holds constant at every level: no PM, however junior, is excused from caring whether the work moved the business. Mehta's 2026 update redefines product definition as specifying work clearly enough for both humans and AI agents to build from, and gives architectural judgment more weight, because teams now have to separate real customer opportunities from capabilities looking for a problem.

A career ladder turns the model into expectations. For each level, state four things:

- **Scope**: a feature, a product area, a product line or a portfolio.
- **Impact**: the outcomes the person is expected to move, and at what scale.
- **Autonomy**: how much direction they need, and how ambiguous a problem they can take on alone.
- **Competencies**: which ones matter most at that level, and at what proficiency.

This book recommends two tracks above Senior PM: a Principal PM path for individual contributors who lead through expertise and influence, and a Group PM or Director path for people managers. Write both tracks with equal care. If the Principal track is vague, strong practitioners become reluctant managers to get promoted.

Hire against the same competencies. Each interview in the loop tests named competencies with structured questions and a written rubric, and the decision rests on rubric evidence rather than the loudest voice in the debrief. Include one work sample taken from real work, such as turning a messy decision thread into a DACI draft or reframing a sales feature request as a problem. Tell candidates up front whether they may use an AI assistant on it; if they may, score how they checked and edited its output, because that is the job they will do.

### Coaching and the 1:1

Coaching sits at the center of product leadership in Marty Cagan and Chris Jones's *Empowered*. Their central argument is that strong companies get results less by hiring exceptional people than by enabling ordinary teams to solve hard problems, and coaching is how a leader does the enabling.

**The GROW model**, developed by Sir John Whitmore and colleagues and popularized in his book *Coaching for Performance*, structures a coaching conversation in four steps: the **Goal** (what the person wants from this conversation and this problem), the **Reality** (what is true now, with evidence), the **Options** (what they could do) and the **Will** (what they will do, by when). The discipline is asking rather than telling; a coach who jumps to Options before hearing the Reality is solving the wrong problem.

**First 1:1 questions.** Lara Hogan's questions for a first 1:1 open any new coaching relationship well. Ask what frustrates the person and how you will be able to tell, how they like to receive feedback and recognition (in public or private), what would make the 1:1s useful, what their short- and long-term goals are, what they need from you, the team and peers, and whether they have enough challenge, time to reflect and timely feedback.

The 1:1 belongs to the person you are coaching, so their agenda comes first. Listen, coach one real problem, give and ask for feedback, and leave with commitments on both sides.

### Team charters

A team charter is one page that says why a team exists, what it owns, how it works and how it is measured. It prevents much of the stakeholder conflict described earlier, because it settles ownership and decision rights before anyone needs them.

Google's Project Aristotle, a study of 180 teams (115 engineering project teams and 65 sales pods), identified five dynamics that distinguished effective teams. In order of importance: psychological safety, dependability, **structure and clarity** (clear roles, plans and goals), meaning and impact. A charter addresses structure and clarity directly.

This chapter's charter template combines three sources: outcome framing from Cagan (teams get problems and are measured on outcomes); explicit ownership from Atlassian's Roles and Responsibilities play, with a named primary owner wherever responsibilities overlap and a review every three to six months; and channels, meeting plan and escalation process from Atlassian's Working Agreements play.

### Product culture and psychological safety

Amy Edmondson defined team psychological safety in a 1999 paper in *Administrative Science Quarterly* as a shared belief among team members that the team is safe for interpersonal risk taking. Her field study of 51 work teams in a manufacturing company found that psychological safety was associated with learning behavior, and that learning behavior in turn connected psychological safety to team performance. The team leader's coaching and the support of the wider context shaped how safe teams felt. Project Aristotle later ranked psychological safety first of its five dynamics and credited the concept to Edmondson.

Two misreadings are common. One treats psychological safety as niceness, a team where nobody challenges anybody. Edmondson's research points the other way: safety matters because it makes learning possible, and learning lifts performance. Her later book, *The Fearless Organization* (2018), carries the idea to whole organizations. The other misreading treats safety as soft and separate from product performance. In product teams it is operational. A team is psychologically safe when an engineer can say "this eval result is worse than we reported," a designer can say "users don't understand this flow," and a PM can say "my hypothesis was wrong," early, without paying a social price.

Culture is also structural. Cagan distinguishes three kinds of product team. **Delivery teams** have a product owner administering a backlog and are accountable for output. **Feature teams** are handed a roadmap of features with dates, are accountable for output, and leave value and viability to the stakeholder who requested the work, so the PM acts largely as a project manager. **Empowered product teams** are cross-functional, given problems to solve and measured on outcomes. A leader who asks for empowerment while handing teams feature roadmaps sends two messages, and teams believe the roadmap.

:::leader For product leaders
Your behavior after a failure sets the culture faster than any values statement. In the first review after something goes wrong, ask what the team learned and what made the problem hard to see earlier, before asking who was responsible. Then act on what you hear, and thank the person who brought the bad news where the team can see it.
:::

## How to apply it

Use this method when you take on a new product, a new role or a major bet. The first six steps take about a month and then become a quarterly rhythm. The last three apply once you lead or coach other PMs.

1. **Build the stakeholder map.** List every internal and external stakeholder for the product or initiative. For each, record power, interest, current stance, what they are measured on and what they fear. Plot them on two grids, internal and external.
2. **Mark the moves.** For each high-power stakeholder, write where you need them to be and by when. Move gatekeepers (security, legal, finance, procurement) toward "manage closely" now, while they still have time to shape the work.
3. **Write the engagement plan.** For each stakeholder or group, set the objective (inform, consult, involve or decide), the message or ask, the channel, the cadence and the owner. Add the signal that tells you the engagement is working.
4. **Settle decision rights for the next contentious decision.** Write a DACI document before anyone debates options. Name one Approver. If legal or security can block, add a "Must agree" row. Pre-wire each Contributor one-on-one before the decision meeting.
5. **Set up the request intake and the no.** Give sales and other functions one structured path for requests, built around problems rather than features. Decide each request on the roadmap's criteria, and answer in writing with one of the four responses.
6. **Establish the upward rhythm.** Agree with your manager on a weekly written update (outcomes moved, decisions needed, risks, asks) and on what counts as a no-surprises item.
7. **Charter the team.** Write the charter with the team, not for it: mission, problems owned, outcome metrics with baselines, out of scope, roles, decision rights, stakeholders, working agreements and escalation path. Set a review date three to six months out.
8. **Calibrate competencies.** Have each PM you coach complete the competency self-assessment with evidence. Review it together, agree on one or two development focuses per quarter and link them to real work.
9. **Run coaching 1:1s.** Use the 1:1 template weekly or fortnightly. Coach one real problem per session with GROW. Track commitments on both sides.

Repeat steps 1 to 3 every quarter and after any reorganization, major launch or incident.

## The AI lens

### Leading AI-powered products and AI-era teams

AI-powered products change who your stakeholders are and how much power they hold.

- **Gatekeepers gain power.** When a product's agent can act on production systems or touches customer data, security, legal and compliance move from occasional reviewers to holders of a real veto. Chapter 33 covers the regulatory substance. The stakeholder lesson is to treat their requirements as design inputs from the first prototype.
- **Finance becomes a product stakeholder.** Inference cost puts gross margin on the product agenda. Pricing, packaging and model choices now have direct margin consequences that finance will want to see before launch, not after (Chapter 15).
- **Eval results become alignment evidence.** Contentious AI decisions, such as how much autonomy to ship, should be decided on eval results and incident data that every Contributor can see. Chapter 31 covers evals. A DACI document for an AI decision without eval evidence in its data section is an opinion contest.
- **Safety to report bad news becomes a quality control.** On an AI product, the earliest warning of a hallucination problem usually comes from an engineer looking at eval results or a support agent reading a strange ticket. Whether that person speaks up is a question of psychological safety.

The larger leadership question in 2026 is what product teams should look like. The debate has two sides, and neither has strong evidence yet.

On one side, some companies are merging roles around AI-assisted building. LinkedIn's chief product officer, Tomer Cohen, said in a December 2025 podcast interview that the company had replaced its associate product manager program with an Associate Product Builder program teaching coding, design and product management together, and had created a formal "Full Stack Builder" title and career ladder so that people from any function can take a product from idea to launch. Atlassian's State of Teams 2026 survey, a vendor study of 12,035 knowledge workers and 173 Fortune 1000 executives fielded in early 2026, found that 77% of executives expect more horizontal teams with fewer layers.

On the other side, the same survey found that 89% of executives say AI increases speed while only 6% are sure they have clear examples of organization-wide return on AI. Cagan's September 2026 essay "Experts Lead Experts" argues that the push for more builders and fewer managers is a passing phase, that some companies that cut managers are already reversing course, and that cheaper building makes skilled product, design and engineering leadership more important. Larson argues that durable, persistent teams remain the building block because domain context accumulates in them, even as individuals can do far more on their own. Cagan's August 2026 definition of the product role, which draws on analyst Benedict Evans, lands in the same place: AI lowers the barrier to building, but finding the deeper problem, a solution customers value and one that works for the business are still the job.

This book's position: change the work before you change the boxes. Reskill your PMs in the skills that AI makes more valuable, measure whether outcomes (not output) improve, and then decide on team shape with evidence. The reskilling plan has four parts, each taught elsewhere in this book:

| Skill | What it means in 2026 | Where it is covered |
|---|---|---|
| AI product judgment | Reading evals, weighing cost and risk, setting autonomy levels | Chapters 31 and 33 |
| Agent-ready definition | Specs clear enough for humans and agents to build from, as Mehta's update describes | Chapters 04 and 06 |
| Building to learn | Using cheap prototypes to answer questions, kept separate from building to earn, in Cagan's terms | Chapters 04 and 21 |
| Evidence through questions | Working with data by asking the harness good questions and checking its answers | Chapters 17 to 19 |

### Doing the work with AI

Stakeholder work is mostly reading, remembering and preparing, which is where an AI harness with the right connectors helps most.

**Refresh the map from evidence.** With connectors to your CRM, ticketing and chat tools, ask the harness: "For each person on this stakeholder map, what have they said or asked about this initiative in the last 30 days? Link every item." Update the stance column from what people said, not from your memory of a meeting two months ago.

**Prepare the pre-wire.** Before a contentious decision, have the harness draft a one-page brief per stakeholder: what they have said on the topic, what they are measured on, the objection they are likely to raise and the evidence that answers it.

**Draft the DACI document.** Point the harness at the decision thread and the data, and ask for a first draft in the DACI format. Rewrite the options section yourself, because how options are framed largely decides the outcome.

**Gather competency evidence.** For a self-assessment, the harness can collect links to a PM's documents, decisions and results from the last two quarters. The rating stays a human judgment.

**Use AI as a coach, with care.** Cagan wrote in February 2026 that many product people lack a manager who can coach them, and he now recommends configuring a foundation model as a personal coach with project instructions and the company's strategic context, while concentrating human coaching on product leaders. He also warns that users have to steer the model, challenge its answers and expect it to vary between sessions. Give your PMs a coaching setup loaded with the team charter, the strategy and the competency model, and keep the human 1:1 for judgment, feedback and career.

Three cautions apply. Stakeholder notes are sensitive: use only approved tools, and never paste private conversations about colleagues into an unapproved model. Larson warns that low-quality AI-generated proposals passed to other teams are actively harmful, so never send a stakeholder a document you have not rewritten and checked yourself. And the harness can summarize what someone said; it cannot tell you what they will do. Influence still runs on relationships you build directly.

:::ai The one-line rule
Let the harness gather what stakeholders said, draft the documents and collect the evidence. Keep the reading of people, the framing of options and every commitment in human hands.
:::

## The Beacon case: launching Beacon Agents through the organization

:::example Where Beacon starts
Beacon Agents, the supervised remediation capability, is set to launch at Northlight Live. You are the Principal PM, newly in the role, reporting to the VP of Product for the Operations portfolio. Gross margin has fallen from 81% to 72% since agentic features launched, because of inference cost. A customer recently rolled back the wrong service after Beacon proposed a hallucinated root cause. EU customers are asking for AI Act documentation. And the strategic tension between building on Northlight Observe data and staying tool-agnostic is unresolved.
:::

**The map.** Your first stakeholder map, built in your second week, shows the problem at once: the high-power, low-interest quadrant holds every function that can stop the launch. Security and legal have not looked at the autonomous-action design. Finance has not seen the per-resolved-incident pricing model against the new margin. Sales leadership is interested only when a large deal is at stake. You mark arrows moving all three into "manage closely" before the launch content is locked. You also move the Observe and Desk group PMs from "keep informed" up the grid, because the build-on-Observe question gives them a genuine stake. Externally, you map Marcus (economic buyer), Priya (champion), Sam (the security reviewer who gates production access) and Leo (the MSP partner) on a separate grid.

**The currencies.** You write one line per stakeholder before asking for anything. The support lead, measured on escalations and still handling fallout from the hallucinated root cause, values a known-issues page and a direct line into the eval work. Finance, measured on margin, values an early look at the cost model and a seat in the pricing decision. The sales leader wants deals closed before year-end and values a field-ready demo and early access for sales engineers.

**The contentious decision.** The hardest call is whether Beacon Agents should launch with autonomous actions enabled by default for customer-allowlisted, low-risk actions, or ship supervised-only. Sales wants autonomy as the headline; support and security want caution after the incident. You write a DACI document titled "DACI: Should Beacon Agents launch with autonomous low-risk actions on by default, or supervised-only?" You are the Driver. The VP of Product is the single Approver. The Beacon engineering lead, the applied AI engineers, security, legal, product marketing, the support lead and sales leadership are Contributors. The Observe and Desk group PMs, customer success and the partner team are Informed. Because security and legal can legitimately block anything that acts on production, you add a "Must agree" row for both, borrowing RAPID's Agree role, and you meet each of them before anyone else sees the options.

The data section carries the diagnosis acceptance rate, the eval results and the incident review. The decision factors are customer trust, the launch story, legal exposure and margin. Pre-wiring changes the options: security will agree to autonomy only with per-action audit logs and a kill switch, which turns a binary choice into three options. The VP decides on supervised-only by default at launch, with autonomous low-risk actions available as an opt-in per customer, and the decision goes into the log with the reasons. Sales leadership disagrees in the meeting, says so clearly and commits.

**Saying no.** Two weeks before Northlight Live, a sales director asks for a custom connector for one large prospect. You convert the request into a problem: the prospect uses a ticketing tool Beacon does not cover. You ask the harness, through the CRM and support connectors, how many of Beacon's roughly 420 customers use that tool and what revenue is attached. The answer is a handful of accounts. You reply in writing with "no, and here is an alternative": the partner team can build an MCP-based connector after the event, and you will review the evidence again in the first quarter.

**Managing up.** Your weekly note to the VP leads with the North Star (incidents resolved with Beacon's help per week), then decisions needed, risks (inference cost, customer trust after the incident) and asks. The DACI decision appears there a week before the meeting.

**The culture moment.** The blameless review of the hallucinated root cause turns up an uncomfortable fact: one of the applied AI engineers had flagged weak evals for that failure mode weeks earlier, in a channel where nobody acted on it. You make the fix structural. The new charter for the engineering team that owns Act (supervised remediation) sets "zero unapproved actions" as a hard constraint alongside its autonomous resolution rate, and its working agreements require eval regressions to be raised in the weekly product review, where the engineer who raises one is thanked by name.

**Leading the PMs.** As lead PM, you coach Beacon's other PMs. Their self-assessments share two gaps: judging AI quality from eval results, and influencing sales. One PM shadows the eval reviews before launch; another runs the deal-request intake with the sales director.

**The team shape memo.** Late in the quarter, your VP asks whether Beacon should reorganize into smaller builder pods with fewer PMs. You write a short memo that sets out the builder model and the arguments from Cagan and Larson, notes that Atlassian's own survey shows executives far more confident about AI speed than AI return, and recommends reskilling first: evals and AI product judgment, agent-ready specs, and building to learn. You propose revisiting team shape after two quarters of outcome data.

## Product 360 artifacts

```template id="36-stakeholder-map" title="Stakeholder map"
# Stakeholder map · [Product or initiative] · [Date]

**Owner:** [PM]   **Scope:** Internal / External   **Next review:** [Date, at least quarterly]

| Name and role | Team | Power (H/M/L, with reason) | Interest (H/M/L) | Quadrant | Current stance | Desired stance, by when | What they're measured on (their currency) | What they fear | Relationship owner | Last touch | Next action |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |

Quadrants: Manage closely (high power, high interest) / Keep satisfied (high power, low interest) / Keep informed (low power, high interest) / Monitor (low power, low interest).

Stance: Champion / Supporter / Neutral / Skeptic / Blocker.

## Sleeping gatekeepers
High-power stakeholders who could block late (security, legal, finance, procurement) and the date each moves to "manage closely":
1.
2.

## Evidence for stance
For each stance rating, link what the person actually said or did, with dates. Refresh from evidence, not memory.
```

```template id="36-stakeholder-engagement-plan" title="Stakeholder engagement plan"
# Stakeholder engagement plan · [Product or initiative] · [Quarter]

**Owner:** [PM]   **Linked map:** [link]

| Stakeholder or group | Quadrant | Objective (inform / consult / involve / decide) | Message or ask | Channel (1:1, written update, review forum, demo) | Cadence | Owner | Signal they're engaged | Risk if neglected |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## Pre-wiring before key decisions
| Decision | Date | Stakeholders to pre-wire | Likely objection | Evidence that answers it | Done |
|---|---|---|---|---|---|
| | | | | | |

## Upward rhythm
- Weekly written update to [manager]: outcomes moved, decisions needed, risks, asks.
- No-surprises items (always escalate within 24 hours): [list]

## Request intake
Requests from [functions] arrive through [channel] with: problem, affected customers or accounts, revenue at stake, deadline, other customers with the same need.
```

```template id="36-daci-decision" title="DACI decision record"
# DACI: [Question we're trying to answer]?

**Status:** Not started / In progress / Decided   **Impact:** High / Medium / Low   **Due date:** [Date]

## People
| Role | Name |
|---|---|
| Driver (runs the process, gets a decision by the date) | |
| Approver (one person only) | |
| Must agree (veto for must-meet requirements, such as legal or security; use sparingly) | |
| Contributors (voice, no vote) | |
| Informed (told the outcome afterward) | |

## Background
[One or two sentences: why this decision, why now.]

## Relevant data
[Metrics, eval results, customer evidence, incident reviews, cost. Link sources.]

## Decision factors
1. [Factor, and how it will be weighed]
2.
3.

## Options considered
| Option | Description | Pros | Cons | Resources and cost | Must-agree requirements met? |
|---|---|---|---|---|---|
| A | | | | | |
| B | | | | | |
| C | | | | | |

## Pre-wiring log
| Contributor | Date | Position | Concern raised | How the options changed |
|---|---|---|---|---|
| | | | | |

## Outcome
[Decision, decided by (Approver) on (date). Reason in one paragraph. Options rejected and why.]

## Action items
| Action | Owner | Due |
|---|---|---|
| | | |

## Disagreements recorded
[Who disagreed, on what, and their confirmation that they commit to the decision.]

Format after Atlassian's DACI play, with a "Must agree" role borrowed from Bain's RAPID.
```

```template id="36-team-charter" title="Team charter"
# Team charter · [Team name] · v[n] · [Date]

**Review date:** [3 to 6 months out]   **Charter owner:** [PM or lead]

## Mission
[One sentence: why this team exists.]

## Customers and problems we own
-
-

## Outcomes and metrics
| Outcome | Metric | Baseline today | Target | By when |
|---|---|---|---|---|
| | | | | |

Hard constraints (must never be violated): [for example, zero unapproved actions]

## Out of scope
[What this team does not own, and who does.]

## Members and roles
| Name | Role (PM, design, tech lead, engineering, applied AI, PMM) | Accountable for | Top 3 to 5 responsibilities |
|---|---|---|---|
| | | | |

Overlapping responsibilities and their named primary owner:

## Decision rights
| Decision type | Who decides | Must agree | Consulted |
|---|---|---|---|
| Roadmap priorities within our area | | | |
| Shipping to general availability | | | |
| Customer-specific requests | | | |
| [Other recurring decision] | | | |

## Key stakeholders and engagement
| Stakeholder | What they need from us | Cadence and channel |
|---|---|---|
| | | |

## Working agreements
- Core hours and time zones:
- Channels (urgent, async, decisions):
- Meetings (purpose, cadence, sync or async):
- How we give and receive feedback:
- How we raise bad news (eval regressions, incidents, slipped dates):

## Escalation path
When we can't agree: [step 1], then [step 2], decided by [role] within [time]. Decisions shared via [channel] and logged in [location].

## Interfaces and dependencies
| Team or system | What we depend on, or what depends on us | Contact |
|---|---|---|
| | | |
```

```template id="36-pm-competency-self-assessment" title="PM competency self-assessment"
# PM competency self-assessment · [Name] · [Level] · [Period]

**Manager or coach:** [Name]   **Check-in date:** [Date]

Rate 1 to 5 against the expectation for your level (1 = well below, 3 = meets, 5 = well above). Every rating needs evidence from the last two quarters.

| Competency | Expectation at my level | Self-rating | Evidence (links to artifacts, decisions, outcomes) | Manager rating | Gap | One development action |
|---|---|---|---|---|---|---|
| Problem discovery | | | | | | |
| Customer insight | | | | | | |
| Data fluency (questions, evidence, reports) | | | | | | |
| Product definition for humans and agents | | | | | | |
| Delivery | | | | | | |
| AI product judgment (evals, cost, risk) | | | | | | |
| Strategy and roadmap | | | | | | |
| Business outcome ownership | | | | | | |
| Stakeholder influence | | | | | | |
| Communication (writing and presenting) | | | | | | |
| Managing up | | | | | | |
| Team leadership and coaching | | | | | | |

## Focus for next quarter (one or two competencies)
| Competency | Real work that will exercise it | What good looks like by [date] | Support needed |
|---|---|---|---|
| | | | |

## Strengths to use more
-
```

```template id="36-one-on-one-coaching" title="1:1 coaching template"
# 1:1 · [Name] and [Manager or coach] · [Date]

The 1:1 belongs to [Name]. Their agenda comes first.

## Their agenda
1.
2.

## Wins since last time
-

## One challenge, coached with GROW
- **Goal:** what do you want from this conversation, and from this problem?
- **Reality:** what is true now? What evidence do you have? What have you tried?
- **Options:** what could you do? What else? What would you advise someone else to do?
- **Will:** what will you do, by when? How will I know?

## Feedback, both ways
- From me (specific, with an example; care personally and challenge directly):
- From you to me:

## Competency focus this quarter
[From the self-assessment.] Progress since last time:

## Commitments
| Who | What | By when |
|---|---|---|
| [Name] | | |
| [Manager] | | |

## What I owe you
[Introductions, decisions, air cover, resources.]

## For a first 1:1, also ask
- What frustrates you at work, and how will I be able to tell?
- How do you like to get feedback and recognition: in public or in private?
- What would make our 1:1s useful to you?
- What are your short- and long-term goals? What do you need from me, the team and your peers?
- Do you have enough challenge, time to reflect and timely feedback right now?
```

## Prompts

```prompt title="Build a stakeholder map from evidence"
Goal: Get a first stakeholder map grounded in what people have actually said, not in your memory.
Paste in (or connect the harness to): CRM notes, support tickets, chat threads, meeting notes and the org chart for the initiative. Use only tools approved for internal and customer data, and do not paste private conversations about colleagues into an unapproved model.

For [initiative], build a stakeholder map. List every internal and external stakeholder who appears in the material or the org chart.

For each person give: role and team; power over this initiative (high, medium or low, with the reason); interest (high, medium or low); quadrant (manage closely, keep satisfied, keep informed, monitor); current stance (champion, supporter, neutral, skeptic or blocker); what they appear to be measured on; what they seem worried about. Cite the source and date for every stance and concern.

Then:
1. Flag high-power, low-interest stakeholders who could block late, such as security, legal, finance or procurement.
2. Flag anyone whose stance has changed in the last 30 days, with the evidence.
3. Write "No evidence" wherever the material doesn't support a field. Don't guess stance from job title.

Check the output: open three of the cited sources and confirm they say what the map claims. Correct any stance you know to be wrong from direct conversation, and note why.
```

```prompt title="Prepare pre-wiring briefs for a contentious decision"
Goal: Walk into each one-on-one before a decision knowing the likely objection and the evidence that answers it.
Paste in: the DACI document, the stakeholder map, and anything each Contributor has said on the topic. Use an approved tool.

For each Contributor and Must-agree stakeholder on this DACI document, write a half-page pre-wiring brief:
- What they have said about this decision or topic, with sources and dates.
- What they are measured on, and how each option affects that measure.
- The objection they are most likely to raise.
- The evidence in the DACI data section that addresses it, or a note that no evidence covers it.
- One thing I could offer that they value (information, task help, visibility or direction).
- One question I should ask them rather than tell them.

Don't invent positions. If someone hasn't spoken on the topic, say so and suggest what to ask.

Check the output: any brief where the "likely objection" isn't supported by a source is a guess; treat it as a question to ask, not a position to rebut.
```

```prompt title="Draft a DACI decision record from a messy thread"
Goal: Turn a long debate into a decision document with clear rights and real options.
Paste in: the discussion thread or meeting notes, relevant data (metrics, eval results, incident reviews, cost), and who you think should hold each role.

Draft a DACI decision record for [decision]. Use this structure: the decision phrased as a question; status, impact and due date; people (Driver, one Approver, Must agree if legal or security can block, Contributors, Informed); one- or two-sentence background; relevant data with sources; decision factors; at least three options with description, pros, cons, resources and cost, and whether each meets the must-agree requirements; action items; outcome left blank.

Rules:
- Name exactly one Approver. If the thread suggests several people believe they decide, flag it as the first issue to resolve.
- Present each option in its strongest form, including options I seem to disfavor.
- Separate facts from the thread from opinions in it.

Check the output: rewrite the options section yourself. Ask the person most likely to disagree whether their preferred option is represented fairly before you circulate it.
```

```prompt title="Turn a feature request into a decision"
Goal: Answer a stakeholder request on the same criteria as the rest of the roadmap, and say no well when you need to.
Paste in: the request as written, the current roadmap themes and their success metrics, and (or connect the harness to) CRM and support data. Use only tools approved for customer data.

A stakeholder has asked for: [request]. 

1. Rewrite the request as a problem: who is affected, in what situation, what it costs them and how we'd measure success.
2. Using the CRM and support data, estimate how many customers share the problem and what revenue is attached. Show the evidence and how you counted.
3. Compare the problem against the roadmap themes and metrics. Where does it rank, and what would it displace?
4. Recommend one response: "not now, and here is when we'll revisit," "yes, if" (state what drops), "no, and here is an alternative," or "no, and here is why."
5. Draft a short written reply to the requester in that form. Keep it respectful and specific, and say no to the request, not the person.

Check the output: verify the customer count against a second source before sending. Make sure the reply names a date or a condition for revisiting, not a vague "later."
```

```prompt title="Write the weekly update to your manager"
Goal: Give your manager decisions, risks and asks on one page, every week.
Paste in (or connect the harness to): this week's metric readouts, the decision log, the risk list, project trackers and notes from key meetings.

Draft my weekly update to [manager] for [product]. Use four headings:
1. Outcomes moved: the North Star and two or three input metrics, with this week's change and a one-line explanation.
2. Decisions needed: each with my recommendation, the deadline and the cost of delay.
3. Risks: anything my manager would not want to hear about from someone else, with what I'm doing about it.
4. Asks: specific help, introductions or air cover.

Keep it under 300 words. No activity lists. If a metric moved for a reason you can't explain from the data, say "cause unknown" rather than guessing.

Check the output: would your manager learn anything here they'd be surprised to hear in another meeting next week? If something is missing, add it yourself.
```

```prompt title="Prepare a competency review with evidence"
Goal: Ground a PM competency conversation in evidence rather than impressions.
Paste in (or connect the harness to): the competency self-assessment template, the person's documents, decisions, launches and metric results from the last two quarters. Use an approved tool; this is personnel information.

For [name], at [level], gather evidence for each competency in the self-assessment. For each competency:
- List up to three pieces of evidence from the last two quarters, with links and dates.
- Note where evidence is thin or missing.
- Don't assign ratings. Ratings are for the person and their manager.

Then suggest two competencies where focused development would have the most effect on the person's current work, and propose one real piece of upcoming work that would exercise each.

Check the output: the person should review the evidence list first and add what the harness missed. Treat missing evidence as a question, not a judgment.
```

```prompt title="Set up an AI coaching companion for a PM"
Goal: Give a PM between-session coaching grounded in your team's context, while keeping human coaching for judgment and career.
Paste in: the team charter, the product strategy, the competency model, and the PM's chosen development focus for the quarter. Use an approved tool.

Act as a product coach for [name], a [level] PM on [team]. Use the charter, strategy and competency model below as your context.

How to coach:
- Use the GROW structure: ask about the Goal, then the Reality with evidence, then Options, then what they Will do and by when.
- Ask before you advise. Offer at most one suggestion per turn, and only after the person has described the situation.
- Hold them to outcomes, not output. If they describe a feature, ask what problem and metric it serves.
- Challenge directly when their plan contradicts the strategy or the evidence, and say why.
- If they raise a career, compensation, conflict with a colleague or wellbeing issue, tell them to take it to their manager.

[charter, strategy, competency model, development focus]

Check the output: in your next human 1:1, ask the PM what the coach told them that week and whether they disagreed with any of it. Expect answers to vary between sessions, and correct the setup if it drifts from your team's way of working.
```

## Anti-patterns

:::warn The stakeholder census
A spreadsheet of every name in the org chart with power and interest ratings, and no desired positions, no owners and no next actions. Nobody acts on it. For each high-power stakeholder, write where they need to be and by when.
:::

:::warn The late veto
Security, legal or finance see the launch for the first time two weeks before the date, and block it. They were in "keep satisfied" because they weren't asking questions. Move gatekeepers into "manage closely" early, and write any veto into the decision record as "Must agree."
:::

:::warn Two Approvers
The VP of Product and the VP of Sales both believe they own the launch decision. The debate about options is really a fight about authority, and it ends when one of them escalates. Name one Approver before anyone debates the options.
:::

:::warn Yes in the room, no in the roadmap
The PM agrees to every request in the meeting and quietly deprioritizes it afterward. Stakeholders learn that a yes from product means nothing. Say no in writing, with the reason and a date to revisit, and keep the yeses you give.
:::

:::warn Status up, decisions stuck
Weekly updates to your manager list everything the team did, and the three decisions that need a VP sit unasked. Lead with decisions needed, your recommendation and the deadline.
:::

:::warn Safety as niceness
A team avoids hard conversations in the name of psychological safety, and an eval regression goes unreported because nobody wants to be the bearer of bad news. Safety means people can raise problems early; the bar stays high.
:::

:::warn Reorganizing before reskilling
Leadership merges roles into builder pods because AI makes building cheaper, then discovers output went up and outcomes didn't. Change the work first, measure outcomes, and then decide the boxes.
:::

## Checklist

- [ ] Internal and external stakeholders are mapped on separate power-interest grids, with stance, currency and a desired position with a date.
- [ ] Gatekeepers who can block late (security, legal, finance, procurement) are in "manage closely" well before launch.
- [ ] An engagement plan sets an objective, channel, cadence, owner and engagement signal for each key stakeholder.
- [ ] Stance ratings are refreshed at least quarterly from evidence of what people said or did.
- [ ] The next contentious decision has a DACI record with one Approver, explicit Must-agree roles and at least three options.
- [ ] Every Contributor was pre-wired before the decision meeting.
- [ ] Decisions, rejected options and recorded disagreements are in a decision log.
- [ ] Requests from other functions arrive as problems through one intake and get a written answer with a reason.
- [ ] Your manager gets a weekly written update led by decisions needed, risks and asks.
- [ ] Your team has a charter with outcome metrics and baselines, decision rights, working agreements, an escalation path and a review date.
- [ ] Every PM you lead or coach has a competency self-assessment with evidence and one or two development focuses for the quarter.
- [ ] 1:1s follow the report's agenda, coach one real problem and end with commitments on both sides.
- [ ] Eval regressions, incidents and slipped dates have a defined, safe path to be raised early.
- [ ] Any change to team shape for AI follows a reskilling plan and outcome data, not output data alone.

## Key takeaways

- Map stakeholders with a power-interest grid, then add stance and a desired position with a date. In enterprise products, the gatekeepers who look uninterested are the ones who can stop a launch.
- Influence without authority is an exchange. Find what each stakeholder is measured on, and offer information, task help, visibility or direction that moves it.
- Settle decision rights before debating options: one Approver, explicit vetoes for legal and security, pre-wired Contributors and a logged decision that everyone commits to.
- Say no to the request, not the person. Turn features into problems, decide them on the roadmap's criteria, and answer in writing with a reason and a date.
- Manage up with decisions, risks and asks, and never let your manager be surprised.
- Product leadership means a clear competency model, coaching with structure, team charters that settle ownership, and a culture where bad news travels fast, which on AI products is a quality control.
- AI has made building cheaper and choosing well more important. Reskill PMs in AI product judgment, agent-ready definition and building to learn, and redraw the org chart only once outcome data supports it.
