<p class="lead">A signed innovation placemat buys you a quarter of attention. What happens next decides whether the bet becomes a product: who in the company gains or loses if it works, how the team is organized and protected, which policies quietly block it, how the portfolio decides to fund, pivot or kill it, and how it crosses from a pilot with friendly customers into the core business. This chapter covers that second half of innovation, the part most plans leave out.</p>

## Why this matters

Innovation in established companies often survives the lab and dies in the hallway. A bet with good evidence runs into a sales compensation plan that pays nothing for the new SKU, a security review queue sized for routine releases, a finance cycle that funds work once a year, and a peer team that loses roadmap share if the bet wins. Nobody is acting in bad faith. Each person is doing the job the company pays them to do.

Charles O'Reilly and Michael Tushman built their research on this tension: the same organization has to run a mature business efficiently and explore new ones, and the two jobs pull in opposite directions. Vijay Govindarajan and Chris Trimble observed in HBR in 2010 that special innovation teams run into conflict with the rest of the organization as a matter of course. Steve Blank's name for what companies often do instead of resolving that conflict is **innovation theater**: labs, demos and press releases that never change what the company sells.

AI makes the gap between pilot and product the defining problem. BCG's October 2024 survey of 1,000 senior executives in 59 countries found that 74% of companies had yet to show tangible value from AI. Its September 2025 study found about 60% achieving hardly any material value and only about 5% achieving value at scale. Pilots are easy to start. Scaling them is where companies fail, and the research in this chapter's AI lens suggests the causes are mostly organizational.

You will rarely own the budget, the org chart or the comp plan. You will map who needs to say yes, design the team boundary, name the policies that need exceptions, bring evidence to the portfolio review and make the case for the next tranche. This chapter gives you a method and six artifacts for that work, building on the placemat (Chapter 20), the experiments (Chapter 21) and the mechanisms (Chapter 22).

## Core concepts and frameworks

### Exploration and exploitation

James March, in a 1991 paper in *Organization Science*, described two kinds of organizational learning. **Exploitation** refines what the company already does: efficiency, execution, incremental improvement. **Exploration** searches for what it could do: experimentation, variation, new models. Both compete for the same people and money.

Exploitation pays back sooner and more reliably, so a company that lets resources flow to the surest return starves exploration without anyone deciding to. The roadmap fills with core work because every core item has a customer, a revenue number and a deadline, while the new bet has only a hypothesis. The rest of this chapter is about countering that drift on purpose.

### The ambidextrous organization

O'Reilly and Tushman developed the **ambidextrous organization** in a 1996 *California Management Review* article, brought it to a wide audience in HBR in 2004 and extended it in *Lead and Disrupt* (2016). They are more optimistic than Clayton Christensen: incumbents can survive disruption if they compete in mature markets (efficiency, control, incremental change) and new domains (flexibility, autonomy, experimentation) at the same time.

Their prescription is **structural ambidexterity**. Exploratory units are separated from the core, with their own people, processes, metrics and culture, and integrated at the senior team. The new unit gets targeted access to the core's assets (customers, brand, data, sales channels) where those assets give it an advantage, under a strategic intent that justifies both.

Cristina Gibson and Julian Birkinshaw, studying 41 business units in a 2004 *Academy of Management Journal* paper, described a second form, **contextual ambidexterity**: individuals inside one unit divide their time between the current business and new opportunities, supported by the unit's culture and systems.

| Situation | Better fit | Why |
|---|---|---|
| A bet close to the core, sold to the same buyers through the same channel | Contextual: a team inside the product org with protected time | The bet needs the core's routines more than protection from them |
| A bet that needs a different price, buyer, channel or risk profile | Structural: a separate team with its own metrics | The core's routines will reshape the bet into a core feature |
| A bet whose economics don't yet work | Structural, small and time-boxed | Core metrics would kill it before the economics are known |

The most useful question this research gives a PM is concrete: **what does the explore team borrow from the core, and who governs each borrowing?** In B2B software the borrowed assets are usually customer relationships, product telemetry, the sales force, security certifications, platform services and the brand. Each is a source of advantage and of conflict. Write them down, name who decides access, and agree what the core gets back.

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 330" role="img" aria-label="Ambidextrous design: a senior team integrates a core unit and an explore unit, with borrowed assets flowing from core to explore under governed agreements">
  <rect x="190" y="14" width="300" height="62" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".6"/>
  <text x="340" y="40" text-anchor="middle" class="t">Senior team and executive champion</text>
  <text x="340" y="60" text-anchor="middle" class="s">Shared strategic intent; settles disputes</text>
  <rect x="20" y="130" width="260" height="180" rx="10" class="box"/>
  <text x="40" y="158" class="t">Core (exploit)</text>
  <text x="40" y="182" class="s">Metrics: revenue, margin, uptime</text>
  <text x="40" y="202" class="s">Process: release train, stage gates</text>
  <text x="40" y="222" class="s">Funding: annual plan</text>
  <text x="40" y="242" class="s">Culture: predictability</text>
  <text x="40" y="272" class="s" style="fill:var(--muted)">Shared staff: sales, support,</text>
  <text x="40" y="290" class="s" style="fill:var(--muted)">security review, SRE</text>
  <rect x="400" y="130" width="260" height="180" rx="10" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)" stroke-opacity=".6"/>
  <text x="420" y="158" class="t">Explore (dedicated team)</text>
  <text x="420" y="182" class="s">Metrics: learning, leading indicators</text>
  <text x="420" y="202" class="s">Process: experiments, evidence gates</text>
  <text x="420" y="222" class="s">Funding: metered tranches</text>
  <text x="420" y="242" class="s">Culture: speed, candor about failure</text>
  <text x="420" y="272" class="s" style="fill:var(--muted)">Single-threaded leader;</text>
  <text x="420" y="290" class="s" style="fill:var(--muted)">own kill criteria</text>
  <line x1="260" y1="76" x2="150" y2="130" class="ln"/>
  <line x1="420" y1="76" x2="530" y2="130" class="ln"/>
  <line x1="280" y1="190" x2="392" y2="190" class="ln"/>
  <polygon points="392,185 400,190 392,195" fill="var(--muted)"/>
  <line x1="400" y1="250" x2="288" y2="250" class="ln"/>
  <polygon points="288,245 280,250 288,255" fill="var(--muted)"/>
  <text x="340" y="180" text-anchor="middle" class="s">Borrowed: customers,</text>
  <text x="340" y="212" text-anchor="middle" class="s">data, channel, certs</text>
  <text x="340" y="242" text-anchor="middle" class="s">Returned: learning,</text>
  <text x="340" y="274" text-anchor="middle" class="s">new revenue, talent</text>
</svg>
<figcaption>Structural ambidexterity in product terms. The two units run on different metrics, processes and funding. The senior team integrates them, and every asset the explore team borrows from the core has a named owner and an agreement about what flows back.</figcaption>
</figure>

### The dedicated team and the performance engine

Govindarajan and Trimble, in their 2010 HBR article and their book *The Other Side of Innovation* (2010), describe every innovation initiative as a partnership. The **dedicated team** is built for the new work, staffed and organized as if from scratch. The **shared staff** sit inside the **performance engine**, the existing operation built for repeatable, efficient work. The dedicated team lacks the core's assets, and the performance engine is designed to resist anything that disrupts its routines, so neither succeeds alone.

Their rule is to split the work line by line. Shared staff get only the tasks that fit their existing routines; anything that conflicts goes to the dedicated team, even if the core could technically do it. They also recommend running the initiative as a disciplined experiment, with hypotheses written down and learning reviewed separately from the core's performance reviews.

In enterprise software the conflicts are predictable. Sales reps paid on quota won't sell a small new SKU with an unfamiliar price. Tier 1 support scripts don't cover the new product's failure modes. The security review queue is sized for routine releases, so a product asking for new access to customer systems waits behind everything else. A release train built for stability can't absorb weekly experiments.

Amazon's version, as Colin Bryar and Bill Carr describe it in *Working Backwards* (2021), is the **single-threaded leader**: one leader whose only job is one initiative, with a team as separable as possible. It's the practical minimum for a bet that matters. For the most exploratory bets, Blank's 2015 guidance goes further: teams of fewer than five, physically separate, with their own plans, metrics and incentives.

:::key Split the work before you staff the team
List every task the bet needs from launch to scale: build, eval, sell, price, bill, support, review for security, operate. For each, ask whether the core's routine fits the bet. If it fits, it goes to shared staff with a named owner. If it conflicts, it goes to the dedicated team or gets a policy exception. The list is the team design.
:::

### Stakeholder mapping for innovation

Aubrey Mendelow's **power and interest grid**, popularized by Mind Tools, sorts stakeholders into four groups: manage closely (high power, high interest), keep satisfied (high power, lower interest), keep informed (lower power, high interest) and monitor. Mind Tools adds the next step: understand each key stakeholder's interests, current opinion, influences and what would win their support.

The grid is too static for innovation. Innovation threatens someone's metric, budget or status, and the threatened people often have the most power. This book's **innovation stakeholder map** adds four columns:

| Column | What it captures | Why it matters for innovation |
|---|---|---|
| **Current stance** | Champion, supporter, neutral, skeptic or blocker | Shows where to spend time, and whether you're spending it on allies |
| **What they gain if it works** | The metric, goal or problem it helps them with | The basis of your message to them |
| **What they lose if it works** | Budget, headcount, a metric that gets worse, risk they carry, roadmap share | The real source of resistance, rarely said out loud |
| **Evidence that would move them** | The proof point, pilot result or policy change that would change their stance | Turns the map into a plan |

The loss column matters most. A sales leader whose quota rests on per-environment pricing loses predictability when the price moves to outcomes. A peer group PM loses engineering capacity or data priority. Finance carries the margin risk. If you can't fill this column honestly for every high-power stakeholder, you don't yet understand the opposition.

### The internal campaign

Winning support for an innovation is a small change program, and John Kotter's eight steps are a useful skeleton: create a sense of urgency; build a guiding coalition; form a strategic vision; enlist a volunteer army; enable action by removing barriers; generate short-term wins; sustain acceleration; institute change.

Four of them translate directly into a PM's **campaign plan**:

- **Urgency.** Tie the bet to a threat or goal executives already care about, in the words of the strategy memo.
- **Guiding coalition.** One executive champion (Chapter 20) is rarely enough. Recruit leaders from the functions whose routines the bet disrupts, often sales, security and finance, plus a customer or two who will speak for it.
- **Volunteer army.** Find the engineers, sellers, support leads and customer SREs who want the bet to win, and give each something to do.
- **Short-term wins.** Schedule evidence before each decision point. A design-partner result shared before the portfolio review persuades more than a forecast shown during it.

The campaign plan organizes this by audience, with a message per stakeholder segment, the moments to deliver it and an objections log. Chapter 36 covers stakeholder management and Chapter 34 the writing.

### Policies that help or kill innovation

Most of the barriers in Kotter's fifth step are policies written for the core that nobody designed with a new bet in mind. Blank argues that core managers need incentives to support new bets, and that legal, finance and procurement should help innovators get to yes. A PM rarely writes these policies, but you can name the ones blocking your bet and propose a bounded exception.

| Policy area | The version that kills innovation | The version that helps |
|---|---|---|
| Funding | One annual budget decision | Tranches released at evidence milestones, any time of year |
| Sales compensation | New SKUs earn little or nothing toward quota | Time-boxed quota credit for pilot deals |
| Security and risk review | One queue for everything | A fast path for pre-agreed low-risk scopes, with full review before scale |
| Customer contracts | Standard paper for every customer | A design-partner template with pilot terms, a data-use clause and an exit |
| Performance reviews | The team is judged on core metrics | Learning reviewed separately from performance |
| Failure | Killing a project is a career risk | Teams that kill their own bets on evidence are recognized |
| Decision rights | Every decision goes to the same committee | Reversible decisions delegated; irreversible ones escalated |

The last row comes from Jeff Bezos's 2016 letter to Amazon shareholders, which separates **two-way door** decisions (reversible, deserving a light process) from one-way doors, and warns against one heavyweight process for both. Starting or extending a pilot is a two-way door. Moving a product into the core, changing list price or sunsetting what it replaces is a one-way door.

The failure row has a well-known example. Astro Teller of X, the moonshot factory, wrote in 2016 about the Foghorn team, which worked on fuel from seawater, concluded it couldn't become cost-competitive within five years and ended its own project so people and money could move to better bets. Teller tells the story as one to follow. The policy lesson is to make that decision safe and visible.

External rules can help too. The EU AI Act requires each member state to set up at least one **AI regulatory sandbox**, where AI systems are developed and tested for a limited time before reaching the market, ending with an exit report that conformity assessors must take into account. The text as adopted in 2024 set 2 August 2026 for the sandboxes to be operational; amended text gives 2 August 2027. Copy the idea internally: a **sandbox policy** that bounds the customers, data and actions a bet may touch and ends with a written exit report.

### Managing innovation as a portfolio

Chapter 20 introduced two portfolio lenses. Bansi Nagji and Geoff Tuff's **innovation ambition matrix** (HBR, 2012) sorts bets into core, adjacent and transformational; their benchmark from the firms they studied was roughly 70/20/10 in spend, with returns running roughly the other way. The **three horizons** sort bets by maturity. Blank's 2015 contribution was to match each horizon to a management method: Horizon 1 executes a known model with standard process, KPIs and stage gates; Horizon 2 extends the model to new customers or channels; Horizon 3 searches for a new model with small separate teams and evidence-based metrics.

The portfolio review is the forum where all bets are seen together and each gets a decision. Four tools make it work.

**Innovation accounting.** Eric Ries, in *The Lean Startup* (2011), proposed measuring an early venture by validated learning: establish a baseline, tune the engine, then pivot or persevere. In *The Startup Way* (2017) he carries the idea into large companies with metered funding released in small increments as teams show evidence, decided by internal growth boards. Chapter 21 builds the innovation accounting dashboard for one bet. The portfolio review reads the dashboards together.

**Stage gates for innovation.** Robert Cooper's **Stage-Gate** model, first in print in 1988, puts a gate before each stage. Gatekeepers who own the resources review deliverables against criteria and decide Go, Kill, Hold or Recycle; a Go commits people, money and the next gate date. Keep that discipline and change the criteria, so early gates ask for evidence instead of business cases:

| Gate | What the bet must show | What it releases |
|---|---|---|
| Gate 1: problem | The customer and problem hypotheses hold in real interviews (Chapter 01) | A small team and a time box for solution tests |
| Gate 2: solution | Customers use the solution and the riskiest assumption has been tested (Chapter 21) | A dedicated team and design partners |
| Gate 3: business model | Customers pay or commit, and unit economics work within a known range | Pilot expansion and go-to-market preparation |
| Gate 4: scale | The scale-up readiness checklist passes and a receiving owner is named | General availability and transfer to the core plan |

**Discovery-driven planning.** Rita McGrath and Ian MacMillan, in HBR in 1995, argued that new ventures need a planning tool built for what they don't know. Start from the profit the venture must produce, work backward to the operations needed, list every assumption and set milestones at which each is tested before more money is committed. That milestone plan is the backbone of metered funding: each tranche is earned by retiring an assumption.

**Portfolio metrics.** Revenue says little about a set of early bets, so the review reads five portfolio measures each quarter: spend by band against the agreed mix (Chapter 20), the number of bets at each gate, assumptions retired, bets killed or pivoted, and bets transferred to the core. Each answers a different question. The mix shows whether the company is funding what it said it would. The gate count shows whether bets are moving or piling up at one gate. Assumptions retired is the portfolio's learning rate. Kills and transfers show whether the review is making decisions at all. A portfolio that retires few assumptions and kills nothing isn't testing its bets.

### Kill criteria

Bets that should die often don't, because each review adds a little more hope and sunk cost. Write the kill criteria before the bet is funded, while everyone is optimistic.

Two ideas make them useful. In the same 2016 post, Teller imagines a team asked to train a monkey to recite Shakespeare on a pedestal. Teams build the pedestal first because it's easy to show progress, while the monkey is the real risk. Write kill criteria against the monkey, the riskiest assumption. Annie Duke, in *Quit* (2022), recommends **states and dates**: if by a given date the bet hasn't reached a given state, it stops. This book's kill line combines them:

> We stop **[bet]** if by **[date]** we have not shown **[state, and how it's measured]**, unless **[named exception]**. The decision is made by **[forum]**.

Every bet carries one, agreed at the gate that funds it. A healthy portfolio kills some bets every year.

### Scaling from pilot to product

A successful pilot answers a narrow question: did this work for these customers, with this team's attention? Scaling asks two harder ones.

**Does the result hold at scale?** John List, in *The Voltage Effect* (2022), frames scaling as a problem where ideas that scale share common traits and ideas that fail do so in many separate ways. In B2B the usual failure points are familiar: design partners were larger, more engaged and friendlier than the market; the team gave pilot customers attention support can't replicate; the unit economics assumed pilot volumes; and the pilot ran under exceptions that don't apply at scale.

**Can the organization absorb it?** Blank names three paths for a bet that succeeds: an existing Horizon 1 unit adopts it, it grows into a standalone business, or it's sold or spun out. He also notes that success leaves technical and organizational debt someone has to pay down. Choose the path deliberately and name a **receiving owner**, the leader who will put the product into their plan, budget and roadmap.

Funding has to change on the way through:

| Funding model | Fits | Watch for |
|---|---|---|
| Central innovation budget | Horizon 3 search, early gates | Bets that never leave it |
| Metered funding by a growth board | Gates 2 and 3, when evidence arrives unevenly | Boards that meet too rarely to release money on time |
| Core business unit takes it into its plan | Adjacent bets transferring to an existing product | The core trims the bet to fit its own metrics |
| New P&L | A different buyer, model or margin structure | Overhead and a long path to profit |

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 300" role="img" aria-label="Innovation path from explore through gates to scale, with a kill exit at every gate and three transfer paths after scale">
  <rect x="10" y="60" width="120" height="70" rx="10" class="box"/>
  <text x="70" y="90" text-anchor="middle" class="t">Explore</text>
  <text x="70" y="110" text-anchor="middle" class="s">Problem, solution</text>
  <rect x="170" y="60" width="120" height="70" rx="10" class="box"/>
  <text x="230" y="90" text-anchor="middle" class="t">Pilot</text>
  <text x="230" y="110" text-anchor="middle" class="s">Design partners</text>
  <rect x="330" y="60" width="120" height="70" rx="10" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)" stroke-opacity=".6"/>
  <text x="390" y="90" text-anchor="middle" class="t">Scale</text>
  <text x="390" y="110" text-anchor="middle" class="s">Readiness checklist</text>
  <line x1="130" y1="95" x2="162" y2="95" class="ln"/>
  <polygon points="162,90 170,95 162,100" fill="var(--muted)"/>
  <line x1="290" y1="95" x2="322" y2="95" class="ln"/>
  <polygon points="322,90 330,95 322,100" fill="var(--muted)"/>
  <text x="150" y="50" text-anchor="middle" class="s">Gate</text>
  <text x="310" y="50" text-anchor="middle" class="s">Gate</text>
  <line x1="150" y1="100" x2="150" y2="200" class="ln"/>
  <line x1="310" y1="100" x2="310" y2="200" class="ln"/>
  <line x1="450" y1="95" x2="470" y2="95" class="ln"/>
  <line x1="470" y1="95" x2="470" y2="200" class="ln"/>
  <rect x="80" y="200" width="420" height="44" rx="10" fill="var(--a3)" fill-opacity=".14" stroke="var(--a3)" stroke-opacity=".6"/>
  <text x="290" y="227" text-anchor="middle" class="t">Kill or pivot: state-and-date kill line not met</text>
  <line x1="450" y1="80" x2="510" y2="30" class="ln"/>
  <line x1="450" y1="95" x2="510" y2="95" class="ln"/>
  <line x1="450" y1="110" x2="510" y2="160" class="ln"/>
  <rect x="510" y="12" width="160" height="40" rx="8" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".6"/>
  <text x="590" y="37" text-anchor="middle" class="s">Absorb into a core unit</text>
  <rect x="510" y="75" width="160" height="40" rx="8" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".6"/>
  <text x="590" y="100" text-anchor="middle" class="s">Grow as standalone</text>
  <rect x="510" y="140" width="160" height="40" rx="8" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".6"/>
  <text x="590" y="165" text-anchor="middle" class="s">Sell or spin out</text>
  <text x="290" y="280" text-anchor="middle" class="s" style="fill:var(--muted)">Each gate releases the next tranche or stops the bet. After scale, a receiving owner takes it into a plan.</text>
</svg>
<figcaption>From explore to scale. Every gate can stop the bet, and a bet that passes the last gate leaves the innovation portfolio by one of three transfer paths, each with a named receiving owner.</figcaption>
</figure>

### Sustaining after scale

Once a scaled bet joins the core, most of its work becomes what the Christensen Institute calls **sustaining innovation**: making good products better for the most demanding customers. That is the right mode for it now: it has customers, a revenue line and uptime commitments, and it should be run with Horizon 1 discipline.

The risk is that the capabilities behind the bet's success (the fast experiment loop, the eval discipline, the direct line to design partners) dissolve in the transfer. Christensen and Michael Overdorf argued in HBR in 2000 that the processes and values that make an organization good at its core make it bad at new businesses. Three practices protect the gains:

- **An exit report.** Borrow the sandbox idea. Before transfer, the dedicated team writes down what it learned, which assumptions are still open, which exceptions it ran under and what the receiving unit must keep doing.
- **Metrics that outlive the transfer.** Keep the bet's leading indicators and evals in the receiving unit's business review (Chapter 29) for two or three quarters.
- **A small explore cell.** Keep a few people from the dedicated team on the next hypothesis in the same space, so the capability survives along with the product.

### Pitching the plan to executives

The pitch asks executives for something specific: the next tranche, people, policy exceptions or a transfer decision. Chapter 20's placemat is its core. For a funding or scale decision, add what the bet has learned since the last gate, the precise ask and the scale path with its receiving owner.

The **Working Backwards PR/FAQ**, as Bryar and Carr describe it, supplies the discipline for the supporting document. Its internal FAQ covers what executives ask anyway: market size, competition, unit economics, upfront investment, risks, regulation, third-party dependencies, the assumptions required for success and the top reasons it could fail. Its review meeting opens with 15 to 20 minutes of silent reading and spends about 40 minutes on discussion, aiming at the truth rather than a sale.

Bezos's 2016 letter adds two norms. Most decisions should be made with about 70% of the information you wish you had, because waiting is usually slower than correcting a wrong call. And a leader can disagree and still commit. Use the door test in the pitch: label which parts of the ask are reversible, so executives can approve them quickly, and which aren't, so the debate goes where it belongs. Chapter 35 covers the delivery.

:::leader For product leaders
Run one innovation portfolio review a quarter where every bet is seen against the target mix, with its kill line, its evidence since last time and a decision. Keep it separate from the core business review, because a bet judged on core metrics in the same meeting as the core will lose. Count kills as a sign the review works.
:::

## How to apply it

This method takes one funded bet, with a signed placemat from Chapter 20, from funding to the core business. The first five steps take about a quarter; the last three run at each gate until the bet is transferred or killed.

**Step 1: Map the people (week 1).**

1. Have your AI harness draft a list, from the placemat, org chart, meeting notes and CRM, of everyone whose budget, metric, process or customers the bet touches. Add the peers and support functions it usually misses.
2. Plot each on power and interest, then fill in stance, gain, loss and the evidence that would move them. Write the loss column yourself, and confirm stances in one-to-one conversations.
3. Write a one-line coalition gap: which high-power stakeholder is neutral or skeptical, and what it would take to move them.

**Step 2: Design the team boundary (weeks 1 and 2).**

4. List every task from build to scale and split it between the dedicated team and shared staff, using Govindarajan and Trimble's rule: shared staff get only the tasks that fit their routines.
5. Name a single-threaded leader. If nobody can be full time, the bet isn't yet a priority.
6. Write down each asset borrowed from the core, who governs access and what the core gets back.

**Step 3: Name the blocking policies (week 2).**

7. For each conflict found in step 4, find the policy behind it: compensation, review queues, contracts, funding cycle, performance reviews.
8. Propose a bounded exception for each: who it covers, for how long, with what guardrail and what ends it. Ask for exceptions rather than rewrites; let the exception's evidence argue for permanent change later.

**Step 4: Run the campaign (weeks 2 to 12).**

9. Build the campaign plan from the stakeholder map: one message per audience segment, the moments to deliver it, the coalition members and their roles.
10. Schedule short-term wins before each decision point. Put the dates in the plan, and make each one a piece of evidence, not a demo.
11. Keep an objections log. Answer each objection with evidence or a change to the plan, and record which you chose.

**Step 5: Join the portfolio review (from the first quarter).**

12. Agree the gate criteria for the bet's current stage, using evidence for early gates and business case for late ones.
13. Write the kill line in state-and-date form, against the riskiest assumption, and get the forum to agree it before releasing the tranche.
14. Report each quarter on the innovation portfolio review template, with a recommended decision.

**Step 6: Test readiness to scale (before gate 4).**

15. Run the scale-up readiness checklist with evidence links for every item. An item without evidence fails.
16. Choose the transfer path (absorb, standalone, or sell or spin out) and name the receiving owner, with their agreement to put the bet into their next plan.

**Step 7: Pitch the decision (at each gate that needs executives).**

17. Update the placemat and write the pitch outline: what was learned, the ask with the door type of each part, the kill line and the scale path.
18. Red-team it with a skeptical peer and with your harness playing the executives. Run a silent read at the start of the meeting.

**Step 8: Transfer and sustain (the two or three quarters after scale).**

19. Write the exit report and hand it to the receiving owner with the evals, dashboards and open assumptions.
20. Keep the bet's metrics in the receiving unit's business review for two or three quarters, and keep a small explore cell working on the next hypothesis.

:::note What good looks like after two quarters
Every high-power stakeholder has a known stance and a plan. The dedicated team has a single-threaded leader and a written split of work with shared staff. At least one blocking policy has a bounded exception. The bet has passed or failed a gate on evidence, and the portfolio review has killed or pivoted at least one bet somewhere in the portfolio.
:::

## The AI lens

### Building AI-powered products

AI innovations often stall between pilot and scale, and the evidence points at the organization more than the model.

**The gap is organizational.** BCG's October 2024 survey describes a **70-20-10 principle** for AI: successful companies put about 70% of their effort into people and processes, 20% into technology and data and 10% into algorithms. (It's unrelated to Nagji and Tuff's portfolio split.) Google Cloud's DORA research reached a similar conclusion for AI-assisted software development in 2025: AI amplifies an organization's existing strengths and weaknesses, and the biggest returns come from working on the organizational system. For an AI product, the stakeholder map, the team boundary and the policies in this chapter matter as much as the evals.

**The pilot statistics are noisy.** One widely discussed 2025 study, the MIT NANDA report "The GenAI Divide" (150 leader interviews, a survey of 350 employees and an analysis of 300 public deployments), reported that only about 5% of AI pilots produced rapid revenue acceleration, and that buying from specialized vendors succeeded about 67% of the time against roughly a third as often for internal builds. Its sample is small and its definition of success narrow, so treat it as a signal, not a benchmark.

**Autonomy should be earned.** Anthropic's guidance on building agents (Erik Schluntz and Barry Zhang, 2024) recommends the simplest solution that works, adding complexity only when evals show it improves outcomes. Pilots often run with more autonomy than the job needs because the team watches every incident. Before scaling, ask whether a fixed workflow would do the job at lower cost with fewer compounding errors.

**The cost curve moves.** Stanford HAI's AI Index 2025 reported that the inference cost of a system performing at the level of GPT-3.5 fell more than 280-fold between November 2022 and October 2024. State inference cost in a scale-up case as a curve with a dated assumption. A bet killed on unit economics deserves a dated recheck.

**Agents are becoming a portfolio line.** BCG's 2025 study estimated agents at about 17% of AI value in 2025, rising to a projected 29% by 2028. Agentic bets need their own gate criteria: eval coverage for every action the agent can take, an approval model, audit logs and documentation for regulators. Chapter 31 covers evals and Chapter 33 regulation.

:::ai Scale the system around the model
An AI pilot proves that a model can do the task for a few customers under close watch. Scaling proves that the company can sell, support, secure, price and operate it for everyone. Write gate 4 criteria for the second question, because that's where AI bets fail.
:::

### Doing the work with AI

A harness with connectors (many built on the Model Context Protocol, which Anthropic released in November 2024) can pull from the CRM, the org chart, meeting notes, product analytics, support tickets, eval results and finance reports. That makes this chapter's artifacts much faster to draft:

- **Stakeholder map.** Draft from org charts, meeting notes and email threads, with the harness proposing stances and citing the evidence for each. You correct the stances and write the loss column.
- **Campaign messages.** Draft one message per audience from a single evidence pack, so every audience hears the same facts framed for their problem.
- **Portfolio review.** Assemble each bet's row from usage, pipeline, eval and cost reports, and flag every bet that crossed or missed its kill line since the last review.
- **Readiness audit.** Check each checklist item against linked evidence, and list items that have a claim but no evidence.
- **Red team.** Play the CFO, the head of sales and the security reviewer, and list their hardest questions about the pitch.

Two guardrails apply. First, the harness cites where every number came from, and no number goes into a pitch or a portfolio review without a source you have checked. Second, the harness drafts and the forum decides: the kill call, the transfer decision and the stance you record for a colleague are judgments a person owns. Stakeholder maps and portfolio reviews contain sensitive views about colleagues, unreleased plans and customer data, so use only tools your company has approved for confidential information, and keep the stakeholder map's loss column out of shared drives.

## The Beacon case: from design partners to the core

:::example Where Beacon starts
In Chapter 20 the CFO signed Beacon's FY2027 placemat: Beacon Agents with per-resolved-incident pricing, an adjacent bet piloted with 10 design partners, at least two of them MSP-led. Chapter 21's experiments narrowed Act to allowlisted low-risk actions after the hallucinated root cause, and Chapter 22 set up the MSP design partner program and the other mechanisms. Now the bet has to survive the company. The launch is planned for Northlight Live, gross margin sits at 72% against 81% before the agentic features, and the sales organization is paid on per-environment pricing. Your VP asks for a plan to get Agents through the gate to scale.
:::

The tranche sizes, dates and targets in this section are illustrative numbers created for this chapter. They are not part of the Beacon case facts.

**Beacon is itself an ambidexterity story.** Beacon launched in 2023 as an alert-correlation feature inside Northlight Observe and was spun out in 2024, a bet that grew out of the core. It still borrows telemetry data from Observe, plus the Northlight sales force and Northlight's security certifications. You write those borrowings down first, because the case's strategic tension (build on Observe data or stay tool-agnostic) is about one of them. Nothing in writing says what Observe gets back, so that goes on the champion's list.

**The stakeholder map.** The harness drafts the list from the org chart, the placemat and three months of meeting notes. You add two people it missed, the shared product ops lead and the head of partner sales, and write the loss column yourself. The tension sits in that column:

- **Northlight sales leadership** (high power, skeptic): quotas rest on per-environment pricing, and per-incident pricing makes bookings less predictable. Evidence that would move them: design-partner deal sizes under the new price, and a comp exception for the pilot.
- **Finance** (high power; supportive at the top through the CFO, skeptical below): carries the margin risk. Evidence: inference cost per resolved incident trending down across design partners.
- **Northlight's internal security review lead** (high power, neutral): every agent action that touches production adds review load. Evidence: per-action audit logs, scoped credentials and a kill switch working in the pilot.
- **The Observe and Desk group PMs** (medium power, neutral): Observe loses data priority if Beacon goes tool-agnostic; Desk wants a say in tickets Beacon creates. Evidence: a written agreement on data access and ticket integration.
- **Support and customer success** (medium power, skeptic): nobody has a runbook for "the agent did something." Evidence: support runbooks and a named escalation path before GA.
- **Priya, two other design-partner SRE leads, and Leo's MSP** (customer champions, the last one conditional on per-customer billing that protects margin): the volunteer army outside the company.

The coalition gap: sales leadership is a high-power skeptic, and no sales leader is in the coalition yet.

**The dedicated team.** One of Beacon's five engineering teams and the applied AI engineers become the Agents team, led single-threaded by one of the three Beacon PMs. Shared staff keep billing infrastructure, the release train for Correlate and Diagnose, and tier 2 support. The dedicated team takes evals, the approval gate, the pilot's billing logic, design-partner onboarding and tier 3 escalations, because none of those fit existing routines.

**The policies.** Three need bounded exceptions:

1. **A sales comp exception**: quota credit for per-incident pilot deals at the per-environment equivalent, for two quarters, for named accounts only.
2. **A fast-path security review** for allowlisted low-risk actions (restart, scale) inside a pre-agreed scope, with full review before any new action type is added.
3. **A design-partner contract template** with pilot pricing, an exit clause and a data-use clause that lets resolved incidents feed the eval suite.

**The campaign.** The coalition is the CFO (champion), the VP of Product, the security review lead and two design-partner customers. To close the coalition gap you add a regional sales vice president who already has two Agents pilots in their accounts. The short-term wins are dated: design-partner results on diagnosis acceptance and MTTR before the sales kickoff, a security walkthrough of audit logs before the GA gate, and Priya presenting her team's results at the customer advisory board. The objections log opens with the hallucinated root cause. The answer is evidence: the eval suite now includes that incident and similar cases, and Beacon won't propose an action below the cited-evidence threshold.

**The portfolio review.** At the quarterly Operations portfolio review, Beacon's bets appear on one page:

| Bet | Horizon | Stage | Kill line (illustrative) | Decision |
|---|---|---|---|---|
| Correlate improvements and the Beacon Classic sunset | H1 | Run | Not an innovation bet; tracked on core metrics | Continue |
| Beacon Agents with per-resolved-incident pricing | H2 | Gate 3 to gate 4 | Stop autonomous actions if any Sev-1 incident is caused by an agent action; stop the pricing pilot if by end of Q2 FY2027 fewer than half of design partners renew at the new price | Scale, pending readiness |
| MSP multi-tenant console | H2 | Gate 2 | Stop if by end of Q1 FY2027 fewer than three design-partner MSPs use it weekly | Continue, next tranche released |
| Change-risk scoring (venture client pilot) | H3 | Gate 1 to gate 2 | Stop if the startup's scores don't beat Beacon's baseline on replayed deploys by the pilot end date | Continue |
| Autonomous remediation beyond allowlisted actions | H3 | Gate 1 | Stop if remediation safety evals aren't passing on the incident replay by end of Q2 FY2027 | Hold until evals mature |

The runbook-to-agent bet from the hackathon is killed at this review: its agents didn't pass evals on the incident replay, and the team itself recommended stopping. You name the team in the review, because a clean kill on evidence is the behavior the portfolio needs.

**Scale-up readiness.** The checklist for Agents, with an evidence link per item, fails three items: support runbooks for agentic escalations exist only in draft; the gross margin plan uses today's inference cost instead of a dated cost curve; and AI Act documentation for EU customers isn't ready. The autonomy question also earns its place. Pilot data shows responders reviewed every run of two allowlisted actions anyway, so autonomous mode added risk without saving time, and those two stay supervised at GA.

**The transfer path.** Agents extends Beacon's own product, so it will be absorbed into Beacon's core roadmap rather than grown as a separate business. The engineering lead for the Diagnose team agrees to take on Agents' on-call and release cadence in the next annual plan. The exit report will list the open assumptions (MSP billing at scale, EU documentation) and the exceptions that end at transfer.

**The pitch.** You update the placemat and write a two-page pitch for the Northlight executive team, with an internal FAQ covering margin, cannibalization of per-environment revenue, the Observe dependency and AI risk. The ask has three parts, each labeled by door type: the next funding tranche for Agents (two-way, released against the open readiness items), the comp exception extended to GA accounts for two quarters (two-way) and the fast-path security review made standing policy for allowlisted actions (one-way, so it gets the most discussion). The meeting opens with a silent read. The head of sales asks the question the harness predicted in rehearsal: what happens to bookings if large customers move to per-incident pricing at renewal? Your FAQ has a range from finance, marked as an estimate. The executives approve the tranche and the extension, and send the security policy back with one change: a quarterly audit of every allowlisted action across customers.

## Product 360 artifacts

Six artifacts carry a bet from funding to the core. The stakeholder map and campaign plan win support, the team charter sets the boundary with the core, the portfolio review decides, the readiness checklist tests scale, and the pitch outline asks for the decision.

```template id="23-innovation-stakeholder-map" title="Innovation stakeholder map"
# Innovation stakeholder map · [Bet name] · [Date]

**Owner:** [PM]   **Champion:** [Executive]   **Confidential:** contains views about colleagues; share only with the core team.

| Name and role | Power (H/M/L) | Interest (H/M/L) | Grid group | Current stance | Gains if it works | Loses if it works | Evidence that would move them | Owner and next touch |
|---|---|---|---|---|---|---|---|---|
| | | | Manage closely / Keep satisfied / Keep informed / Monitor | Champion / Supporter / Neutral / Skeptic / Blocker | | Budget, headcount, metric, risk, roadmap share | | |

## Borrowed assets
| Asset borrowed from the core | Governed by | Terms of access | What the core gets back |
|---|---|---|---|
| Customers | | | |
| Data | | | |
| Sales channel | | | |
| Certifications and compliance | | | |
| Platform services | | | |

## Coalition gap (one line)
[Which high-power stakeholder is neutral, skeptical or blocking, and what would move them.]

## Changes since last version
| Date | Stakeholder | Stance before → after | What changed it |
|---|---|---|---|
```

```template id="23-innovation-campaign-plan" title="Innovation campaign plan"
# Innovation campaign plan · [Bet name] · [Quarter]

**Objective:** [The decision or behavior this campaign must produce, and by when]
**Decision needed:** [Forum, date, decision maker]
**Urgency in their words:** [The corporate goal or threat, quoted from the strategy memo, with source]

## Guiding coalition
| Member | Function | Role in the campaign | Commitment asked |
|---|---|---|---|
| [Executive champion] | | Sponsor; opens doors | Attend gates; recruit one peer |
| | | | |

## Audiences and messages (from the stakeholder map)
| Audience segment | Their problem | The evidence for them | The ask | Messenger |
|---|---|---|---|---|
| | | | | |

## Volunteer army
[Who inside or outside the company wants this to win, and what each will do: run a demo, staff a pilot, tell a story.]

## Short-term wins (dated, each a piece of evidence)
| Date | Win | Evidence it produces | Before which decision |
|---|---|---|---|
| | | | |

## Channels and moments
| Moment | Date | Audience | What we show |
|---|---|---|---|
| Executive staff meeting | | | |
| QBR or business review | | | |
| All-hands demo | | | |
| Customer advisory board | | | |

## Barriers and policy exceptions requested
| Barrier | Policy behind it | Exception proposed (who, how long, guardrail, end condition) | Owner | Status |
|---|---|---|---|---|

## Objections log
| Date | Objection | From | Response: evidence or plan change | Resolved? |
|---|---|---|---|---|

## Measures of support
[Stance changes on the stakeholder map; exceptions granted; pilots staffed by volunteers; decision outcome.]
```

```template id="23-dedicated-team-charter" title="Dedicated team charter"
# Dedicated team charter · [Bet name] · [Date]

**Single-threaded leader:** [Name, and the scope they gave up]
**Executive champion:** [Name]   **Form:** Structural (separate team) / Contextual (protected time inside a team)
**Why this form:** [Distance from the core: buyer, price, channel, risk profile]

## Explore and exploit alignment
| Element | Core (performance engine) | This bet (dedicated team) |
|---|---|---|
| Strategic intent | | |
| Critical tasks | | |
| People and skills | | |
| Structure and decision rights | | |
| Metrics and rewards | | |
| Culture and norms | | |
| Funding | Annual plan | Tranches at evidence milestones |

## Split of work
| Task (build to scale) | Fits core routine? | Owner: dedicated team or shared staff | Named person | Conflict to manage |
|---|---|---|---|---|
| Build | | | | |
| Evals and quality | | | | |
| Pricing and billing | | | | |
| Selling | | | | |
| Support and escalation | | | | |
| Security and risk review | | | | |
| Operations and on-call | | | | |
| Release and deployment | | | | |

## Supporting policies
| Policy area | Current rule | Exception or new rule | Approved by | Ends when |
|---|---|---|---|---|

## Reviews
Learning review: [cadence, forum, separate from performance reviews]
Disputes with the core are settled by: [champion or senior team]
```

```template id="23-innovation-portfolio-review" title="Innovation portfolio review"
# Innovation portfolio review · [Portfolio] · [Quarter]

**Forum:** [Name]   **Decision makers:** [Names]   **Prepared by:** [PM]   **Sources:** [Reports used, with dates]

## Portfolio summary
| Measure | This quarter | Last quarter | Target |
|---|---|---|---|
| Spend mix: core / adjacent / transformational | | | [Agreed mix] |
| Bets by stage (gate 1 / 2 / 3 / 4) | | | |
| Assumptions retired this quarter (learning velocity) | | | |
| Bets killed or pivoted this quarter | | | Some, every year |
| Bets transferred to the core this quarter | | | |

## Bets
| Bet | Horizon or zone | Stage | Riskiest assumption | Evidence since last review | Leading indicator vs plan | Spend to date | Next tranche asked | Kill line (state and date) | Kill line status | Door type of the decision | Recommended decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | H1 / H2 / H3 | | | | | | | | Met / Not met / Not yet due | Two-way / One-way | Continue / Pivot / Scale / Kill / Hold |

## Kill lines crossed or missed
[Every bet whose kill line date passed this quarter, with the state reached and the decision.]

## Decisions
| Bet | Decision | Resources released | Next gate date | Decided by |
|---|---|---|---|---|

## Recognition
[Teams that killed or pivoted a bet on evidence this quarter.]
```

```template id="23-scale-up-readiness-checklist" title="Scale-up readiness checklist"
# Scale-up readiness checklist · [Bet name] · [Date]

**Gate:** Pilot to scale (gate 4)   **Receiving owner:** [Name]   **Transfer path:** Absorb into core unit / Grow standalone / Sell or spin out

Every item needs an evidence link. An item with a claim and no evidence is a fail.

| # | Item | Pass / Fail | Evidence link | Owner | Fix by |
|---|---|---|---|---|---|
| 1 | Results hold outside the pilot: customers representative of the target segments, not only the friendliest | | | | |
| 2 | Results hold without pilot-level attention from the team | | | | |
| 3 | Unit economics at scale volumes, including inference cost as a dated curve | | | | |
| 4 | For AI: autonomy matches the job; a simpler workflow was considered and rejected on evidence | | | | |
| 5 | Evals cover the actions and outputs customers will rely on, and will keep running after transfer | | | | |
| 6 | Operational readiness: support runbooks, escalation path, on-call, documentation | | | | |
| 7 | Go-to-market readiness: price, SKU, billing, sales compensation, partner enablement | | | | |
| 8 | Compliance and risk: security review, audit logs, data residency, AI risk documentation | | | | |
| 9 | Receiving owner has the bet in their plan, budget and roadmap | | | | |
| 10 | Integration and technical debt listed, each with an owner | | | | |
| 11 | Pilot exceptions listed, with what replaces each at scale | | | | |
| 12 | Metrics and dashboards continue in the receiving unit's business review for two or three quarters | | | | |
| 13 | Sunset or migration plan for anything the bet replaces | | | | |
| 14 | Exit report written: what was learned, open assumptions, what the receiving unit must keep doing | | | | |

## Decision
[Scale / Scale with conditions / Not yet], decided by [forum] on [date]. Conditions: [list].
```

```template id="23-innovation-pitch-outline" title="Innovation pitch outline"
# Innovation pitch · [Bet name] · [Decision forum] · [Date]

Format: two pages plus appendix, read silently at the start of the meeting.

## 1. Headline
[One sentence: the customer, the outcome and the decision we're asking for.]

## 2. Problem and why now
[The customer problem in their words; the corporate goal it serves, quoted; what changed that makes now the time.]

## 3. What we learned since the last gate
| Assumption | Evidence | Result | Source |
|---|---|---|---|

## 4. The bet and the business model
[What we will build or scale, how it makes money, unit economics with dated assumptions.]

## 5. The ask
| Item | Amount or scope | Door type (two-way / one-way) | Released against |
|---|---|---|---|
| Money | | | |
| People | | | |
| Policy exceptions | | | |
| Transfer decision | | | |

## 6. Milestones and tranches
| Milestone | Date | Evidence required | Tranche released |
|---|---|---|---|

## 7. Kill criteria
We stop [bet] if by [date] we have not shown [state, measured as], unless [named exception]. Decided by [forum].

## 8. Scale path
[Transfer path, receiving owner and the date they take it into their plan.]

## 9. Top risks
[Top three from the risk register, each with owner and trigger.]

## Appendix: internal FAQ
Market size and evidence · Competition and alternatives · Unit economics · Upfront investment · Cannibalization of current revenue · Dependencies on other teams and third parties · Regulation and AI risk · Assumptions that must hold · Top reasons this could fail

## AI disclosure
[Which parts were drafted or analyzed with AI, and confirmation that every number was checked against its source.]
```

## Prompts

```prompt title="Draft an innovation stakeholder map"
Goal: Get a first stakeholder map that shows who gains and who loses if the bet works.
Paste in (or connect the harness to): the placemat, the org chart for the affected functions, recent meeting notes and email threads about the bet. These contain confidential views about colleagues; use only a tool approved for that material.

Using the material provided for [bet], draft an innovation stakeholder map.

1. List everyone whose budget, metric, process, customers or roadmap the bet touches. Include peers and support functions (sales, support, security review, finance, legal, procurement, partner teams).
2. For each, rate power and interest (H/M/L) and place them on the grid: manage closely, keep satisfied, keep informed or monitor.
3. Propose a current stance (champion, supporter, neutral, skeptic, blocker) and quote or cite the evidence for it. If there is no evidence, write "Unknown: confirm in person."
4. For each, state what they gain if the bet works and what they could lose (budget, headcount, a metric that gets worse, risk they carry, roadmap share).
5. Suggest the evidence that would move each high-power stakeholder who isn't a supporter.
6. Write a one-line coalition gap.

Don't infer stances from job titles alone.

Check the output: every stance should cite a source or say "Unknown." Rewrite the loss column yourself; the model tends to understate it. Confirm stances in one-to-one conversations before you act on them.
```

```prompt title="Write the campaign messages by audience"
Goal: Give each audience the same evidence, framed for their problem.
Paste in: the stakeholder map, the evidence pack (pilot results, customer quotes, cost data, with sources) and the decision you need.

You're helping me build support for [bet] before [decision forum] on [date].

For each audience segment in the stakeholder map:
1. State their problem in one sentence, in their terms.
2. Select the two or three pieces of evidence from the pack that matter most to them. Cite each.
3. Write the ask: one specific action or decision.
4. Draft a 120-word message I could send or say.
5. List the objection they're most likely to raise and the evidence that answers it, or say that no evidence in the pack answers it.

Use only evidence from the pack. Don't change any number. Don't promise anything the pack doesn't support.

Check the output: compare every number with the source. Read the objections list closely; an objection with no answering evidence is a gap to close before the meeting, not a messaging problem.
```

```prompt title="Split the work between the dedicated team and shared staff"
Goal: Design the team boundary before staffing the bet.
Paste in: the placemat, a description of how the core organization handles build, release, sales, pricing, billing, support, security review and operations today, and any policy documents for those functions.

For [bet], list every task needed from build to scale. For each task:
1. Describe the core organization's existing routine for it.
2. Judge whether the routine fits what the bet needs. Explain the conflict where it doesn't (cadence, incentives, risk tolerance, skills, metrics).
3. Recommend an owner: shared staff if the routine fits, the dedicated team if it conflicts.
4. Where a policy causes the conflict, name the policy and propose a bounded exception: who it covers, for how long, the guardrail and what ends it.

Then list the assets the dedicated team will borrow from the core and propose who should govern each.

Check the output: walk the list with one leader from each shared function. If they say a "fits" routine doesn't, move the task. Exceptions without an end condition aren't bounded; add one.
```

```prompt title="Assemble the innovation portfolio review"
Goal: Prepare the quarterly review from live evidence, with kill lines flagged.
Paste in (or connect the harness to): each bet's placemat and kill line, usage and leading-indicator reports, pipeline and bookings, eval results, cost reports and spend to date. Use an approved tool for financial and customer data.

Build the innovation portfolio review for [portfolio] for [quarter].

1. For each bet, fill in: horizon, stage, riskiest assumption, evidence since the last review (with sources), leading indicator against plan, spend to date, next tranche asked, kill line and its status (met, not met, not yet due).
2. Flag every bet whose kill line date fell in this quarter, and state what was reached against what was promised.
3. Classify each pending decision as a two-way or one-way door, with a one-line reason.
4. Compute the spend mix against the target and count assumptions retired, kills and transfers this quarter.
5. Propose a decision for each bet (continue, pivot, scale, kill, hold) with the evidence for it.

Every number must cite its report and date. If a number is missing, write "No data," never an estimate.

Check the output: spot-check three numbers against the source reports. Read each proposed decision against its kill line yourself; a model will often recommend "continue" for a bet that missed its line.
```

```prompt title="Audit scale-up readiness against evidence"
Goal: Find the readiness gaps before the scale gate does.
Paste in: the scale-up readiness checklist with the team's answers and evidence links, the pilot results, the support and security documentation, and the pricing and margin plan.

Review this scale-up readiness checklist for [bet].

1. For each item, check whether the linked evidence actually supports the answer. Mark it "Supported," "Claimed but not evidenced" or "Contradicted," with a reason.
2. Compare the pilot customers with the target segments on size, engagement, industry and region. Say where the pilot is unrepresentative.
3. Check the unit economics: is inference or other variable cost stated as a dated curve or a fixed number? What happens to margin at 5 and 20 times pilot volume under the stated assumption?
4. For AI products: list the actions the product takes autonomously, and for each, whether pilot data shows customers needed that autonomy or approved every action anyway.
5. List the pilot exceptions and whether each has a replacement at scale.

Check the output: open the evidence for every item marked "Supported." Treat "Claimed but not evidenced" as a fail until someone produces the evidence.
```

```prompt title="Red-team the innovation pitch as the executive team"
Goal: Hear the hardest questions before the meeting does.
Paste in: the pitch outline, the updated placemat and the internal FAQ.

Act as the executive team reviewing this pitch for [bet]: the CFO, the head of sales, the head of security and the business unit leader who would receive the product at scale. Each of you has read it silently.

1. Each executive asks their three hardest questions, from their own goals and risks.
2. For each question, say whether the pitch or FAQ answers it with evidence, answers it weakly or doesn't answer it.
3. Identify any part of the ask that is labeled a two-way door but is hard to reverse.
4. Name the single weakest claim in the pitch and the evidence that would fix it.

Be skeptical and specific. Don't praise the pitch.

Check the output: add the unanswered questions to the internal FAQ with real answers or an honest "unknown, and here's how we'll find out." Don't add numbers to answer them unless you have a source.
```

```prompt title="Write the exit report for a transfer to the core"
Goal: Hand the receiving owner what the dedicated team learned, so it survives the transfer.
Paste in: the bet's experiment and learning cards, the innovation accounting dashboard, the readiness checklist, the list of pilot exceptions and the eval suite description.

Draft an exit report for [bet] as it transfers to [receiving owner].

Sections:
1. What we set out to learn and what we learned, assumption by assumption, with evidence.
2. Assumptions still open, and the evidence that would close each.
3. Exceptions the bet ran under (pricing, compensation, security, contracts), and what replaces each after transfer.
4. Practices the receiving unit must keep: eval runs, design-partner contact, leading indicators to keep in the business review for two or three quarters.
5. Known technical and integration debt, each with a proposed owner.
6. What we would do differently.

Use only the material provided. Mark anything inferred as "inferred."

Check the output: review it with the single-threaded leader and the receiving owner together. If the receiving owner can't name who will run each practice in section 4, the transfer isn't ready.
```

## Anti-patterns

:::warn Innovation theater
Labs, hackathons and demo days with press releases, and nothing that changes what the company sells. Steve Blank's name for it fits. If no bet has transferred to the core or been killed on evidence in a year, the portfolio is producing theater.
:::

:::warn The bet judged on core metrics
An early bet is reviewed in the same meeting as the core business, on revenue and margin. It loses every time. Review innovation in its own forum, with evidence criteria at early gates and business criteria at late ones.
:::

:::warn A dedicated team that does everything
The team rebuilds billing, support and security review from scratch to avoid friction, and can't reach customers at scale. Split the work line by line: shared staff for anything that fits their routines, the dedicated team only for what conflicts.
:::

:::warn Kill criteria written after the fact
The bet misses its target, and the review sets a new target. Write the kill line in state-and-date form at the gate that funds the bet, against the riskiest assumption rather than the easiest progress to show.
:::

:::warn The pilot that never ends
A pilot runs for four quarters with friendly customers and team attention nobody can replicate. Pilots have an end date, a scale gate and a receiving owner. If nobody will take the product into their plan, it isn't ready to scale.
:::

:::warn Scaling the demo
An AI pilot works under close watch and scales with the same autonomy, the same fixed-cost assumption and no support runbook. Scale the system around the model: evals, operations, pricing, compliance, and autonomy only where it pays.
:::

## Checklist

- [ ] The stakeholder map covers everyone whose budget, metric, process or customers the bet touches, with stance, gain, loss and the evidence that would move them.
- [ ] Every high-power stakeholder's stance has been confirmed in conversation, and the coalition gap is written down.
- [ ] The campaign plan has a message per audience, dated short-term wins before each decision point and an objections log.
- [ ] The bet has a single-threaded leader and a written split of work between the dedicated team and shared staff.
- [ ] Every asset borrowed from the core has an owner and terms, including what the core gets back.
- [ ] Each blocking policy has a bounded exception with a scope, a guardrail and an end condition.
- [ ] The bet appears in a quarterly innovation portfolio review, separate from the core business review.
- [ ] Gate criteria match the stage: evidence at early gates, business case at late ones.
- [ ] The bet has a state-and-date kill line agreed before its current tranche was released.
- [ ] The scale-up readiness checklist passes with evidence links, including inference cost as a dated curve for AI products.
- [ ] A transfer path and a receiving owner are named, and the bet is in the receiving owner's plan.
- [ ] The pitch labels each part of the ask as a two-way or one-way door and includes an internal FAQ.
- [ ] An exit report has been handed over, and the bet's metrics stay in the receiving unit's review for two or three quarters.
- [ ] Every number in the pitch and portfolio review traces to a source someone checked.

## Key takeaways

- Innovation in established companies often fails inside the company, in compensation plans, review queues, funding cycles and peer priorities. Plan for those as carefully as for the product.
- Add what each stakeholder loses if the bet works to the power and interest grid. The loss column explains the resistance and points to the evidence that would move it.
- Design the team boundary before staffing: a single-threaded leader, a dedicated team for work that conflicts with core routines, shared staff for the rest, and a written agreement for every asset borrowed from the core.
- Ask for bounded policy exceptions, not rewrites, and let the exception's evidence make the case for permanent change.
- Run innovation as a portfolio with its own review, stage-appropriate gates, metered funding and state-and-date kill lines, and expect it to kill some bets every year.
- Scaling is a separate test from piloting: results must hold for representative customers without team attention, and a named receiving owner must take the product into their plan. AI bets fail here most often.
- Pitch the next decision: what was learned, a precise ask labeled by door type, the kill line and the scale path, read silently and debated on evidence.
