<p class="lead">In a B2B business the installed base decides whether you grow. This chapter teaches the analyses that tell you who stays, who grows, who is worth investing in and what customers are saying: survival and cohort retention, revenue retention, lifetime value, health scores and sentiment. It shows how to turn each one into a strategy decision, and how to get an AI harness to run them without fooling you.</p>

## Why this matters

A customer who signs for one environment and expands to twelve over four years is worth many times the first deal. A customer who renews on paper while their engineers stop logging in is a loss you haven't booked yet. Neither shows up in a pipeline report.

Chapter 05 covered instrumentation, funnels and first retention curves, and Chapter 08 used data to choose a strategy. This chapter asks which customers, segments and channels deserve your next dollar, and what is eroding the base. B2B makes that harder in three ways:

1. **Churn is lumpy.** Customers leave at renewal dates, so the financial signal arrives once a year, long after the cause.
2. **The account is several people.** The user, the champion and the economic buyer can each be unhappy separately, and any one of them can end the relationship.
3. **The numbers are small.** You may have hundreds of accounts, not millions of users, and a handful of large customers can swing every average.

A Principal PM should be able to say at any time when and why customers leave (survival and cohort retention), whether the base is growing or leaking (net and gross revenue retention), which customers are worth most after the cost to serve them (lifetime value), which accounts need attention and whether attention helps (health scores and retention experiments), and what customers are saying that costs revenue (sentiment and the voice of the customer). These analyses feed the Business and Customer dimensions of your Product 360, and they're the evidence you'll bring to pricing (Chapter 15), lifecycle decisions (Chapter 30) and business reviews (Chapter 29).

## Survival analysis: when customers leave

### The survival curve and the hazard

Survival analysis, borrowed from medicine and engineering, asks how long customers stay and when they're most likely to leave. Two ideas carry most of the value:

- **The survival curve** shows the share of a starting group still with you after each period. It starts at 100% and can only stay flat or fall. One of the most widely used ways to draw one from real data is the estimate Edward Kaplan and Paul Meier published in 1958, built for exactly the situation where many subjects haven't reached the end of their story yet.
- **The hazard** is the chance that a customer who has made it to a given period leaves during that period: the risk right now, for customers still here.

The curve tells the cumulative story; the hazard shows where risk concentrates. A steadily falling curve can hide a hazard near zero for eleven months and high in month twelve, which points to the renewal decision and a pre-renewal value review. A hazard that peaks in month two points to onboarding instead.

Peter Fader and Bruce Hardie, whose work underpins much practical retention analysis, note that expected tenure is the area under the survival curve. A small lift in early survival raises the curve for every period after it, which is why early retention is worth so much.

The curve answers "when." To ask "what raises the risk," statisticians reach for the regression model David Cox published in 1972, which estimates how much each factor scales the hazard up or down: missing a connector at go-live, losing a champion, a smaller contract, a partner-led onboarding. You don't need the math. You need to ask for the factors, how much each one moves the hazard, and how many accounts sit behind each estimate, and to remember that a factor that moves with churn doesn't necessarily cause it.

### Censoring: the customers who haven't left yet

A customer who signed eight months ago and is still active hasn't churned, but you don't know when they will. Statisticians call this **censoring**. The documentation for lifelines, a widely used survival library maintained by Cameron Davidson-Pilon, puts it simply: you can't see the rest of the subject's history.

Most homegrown churn analysis goes wrong here. Drop current customers and you throw away the ones who last longest, so average lifetime comes out far too short; treat today as their end date and you still underestimate. Survival methods count censored customers as survivors for every period observed, without counting them as churn. Whenever you ask for a churn analysis, say explicitly that current customers are treated as still active.

### Contract churn and usage churn

B2B products have two kinds of departure, and each needs its own survival curve.

**Contract churn** is the customer not renewing. It's observed and unambiguous, and it happens at renewal dates. Fader and Hardie call this the **contractual setting**. With annual contracts, the contract hazard sits near zero mid-term and spikes at each renewal.

**Usage churn** is the customer still paying while use fades: seats go idle, workloads move, the champion leaves and nobody replaces them. It resembles what Fader and Hardie call the **noncontractual setting**, where you never see a clean exit and must infer from behavior whether a customer is still "alive."

Usage survival is the leading indicator; contract survival is the lagging, financial result. A PM who watches only contract churn learns about problems once a year, with no time left to act.

<figure class="fig" markdown="0">
<svg viewBox="0 0 640 330" role="img" aria-label="Survival curves for contract and usage over 36 months. Contract survival drops in steps at each annual renewal; usage survival declines steadily and sits below the contract curve, leading it.">
  <rect x="70" y="30" width="530" height="240" rx="6" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <line x1="70" y1="84" x2="600" y2="84" stroke="var(--border-2)" stroke-dasharray="3 4"/>
  <line x1="70" y1="150" x2="600" y2="150" stroke="var(--border-2)" stroke-dasharray="3 4"/>
  <line x1="70" y1="216" x2="600" y2="216" stroke="var(--border-2)" stroke-dasharray="3 4"/>
  <line x1="247" y1="30" x2="247" y2="270" stroke="var(--border-2)"/>
  <line x1="423" y1="30" x2="423" y2="270" stroke="var(--border-2)"/>
  <path d="M70 40 H247 V84 H423 V110 H600" fill="none" stroke="var(--a1)" stroke-width="3"/>
  <path d="M70 40 C130 52 190 70 247 82 S360 108 423 118 S540 136 600 146" fill="none" stroke="var(--a2)" stroke-width="3" stroke-dasharray="8 5"/>
  <text x="62" y="44" text-anchor="end" class="s">100%</text>
  <text x="62" y="154" text-anchor="end" class="s">75%</text>
  <text x="62" y="270" text-anchor="end" class="s">50%</text>
  <text x="70" y="290" text-anchor="middle" class="s">0</text>
  <text x="247" y="290" text-anchor="middle" class="s">Renewal 1 (month 12)</text>
  <text x="423" y="290" text-anchor="middle" class="s">Renewal 2 (month 24)</text>
  <text x="600" y="290" text-anchor="middle" class="s">36</text>
  <text x="335" y="315" text-anchor="middle" class="s">Months since contract start</text>
  <text x="440" y="60" class="t" style="fill:var(--a1)">Contract survival</text>
  <text x="440" y="76" class="s">Steps down only at renewals</text>
  <text x="300" y="190" class="t" style="fill:var(--a2)">Usage survival</text>
  <text x="300" y="206" class="s">Declines between renewals and leads</text>
  <text x="300" y="222" class="s">the contract curve by months</text>
  <text x="96" y="110" class="s" style="fill:var(--muted)">Gap between the curves:</text>
  <text x="96" y="126" class="s" style="fill:var(--muted)">accounts paying, not using</text>
</svg>
<figcaption>Illustrative contract and usage survival for one cohort. The contract curve moves only at renewal, so it reports trouble late. The usage curve shows the same trouble months earlier, while there's still time to act. The gap between them is the at-risk base.</figcaption>
</figure>

For usage-priced products the two collapse into one: usage decay is revenue churn, immediately. If you charge per resolved incident or per unit consumed, a customer whose usage halves has halved their bill, with no renewal date to warn you.

### The sorting effect

Plot retention rate by year of tenure and it usually rises: year-three customers renew at a higher rate than year-one customers. The natural reading is that the product gets stickier with use.

Fader and Hardie show the pattern appears even when no individual customer becomes more loyal. Customers differ in their underlying propensity to leave, the high-propensity ones go early, and the group left in year three is mostly low-propensity customers. They call the rising rate "simply a sorting effect in a heterogeneous population."

Two consequences follow. Don't credit the product for rising tenure retention until you've compared like with like, such as the same segment before and after a change. And don't project retention by fitting a trend line to a few years of averages: Fader and Hardie show common curve fits produce impossible forecasts, such as retention that climbs forever or survival that goes negative. Use survival methods and segment the base.

### Cohort retention

A **cohort** is a group of customers who started in the same month or quarter. The standard view is a **retention triangle**: one row per cohort, one column per period since start, each cell showing the share retained. Read it three ways:

- **Down a column**: do newer cohorts retain better at the same age? This shows whether onboarding or product changes worked.
- **Along a row**: where does decay stop? A curve that flattens shows a durable core getting lasting value. Lenny Rachitsky and Casey Winters, in a 2020 survey of growth leaders, argue that a flat retention curve plus a scalable acquisition strategy is enough to keep a business alive. A curve still decaying toward zero signals weak fit.
- **Along a diagonal**: the same calendar month across cohorts. A diagonal dip points to an event that hit everyone at once, such as a price change, an outage or a competitor's launch.

Track three kinds of retention, because they diverge:

| Lens | Counts | Tells you |
|---|---|---|
| Logo retention | Accounts still under contract | Whether you keep relationships |
| User or seat retention | Active people inside retained accounts | Whether the product is still used (the leading signal) |
| Revenue retention | Recurring revenue from the cohort | Whether the base grows or shrinks in dollars |

In B2B, cohort by segment as well as by date: annual contract value (ACV) band, industry, channel and onboarding path often explain more than signup month. SaaS Capital's 2025 retention benchmarks found contract value the best single axis for comparing retention, ahead of company age, size or industry.

## Revenue retention: NRR and GRR

### Definitions

Two numbers summarize a recurring-revenue base. SaaS Capital's definitions are typical:

- **Net revenue retention (NRR)**: recurring revenue today from customers who were customers twelve months ago, divided by those customers' recurring revenue twelve months ago. It includes expansion, cross-sell and price increases, net of contraction and churn, and can exceed 100%.
- **Gross revenue retention (GRR)**: the same calculation without expansion, cross-sell and price increases. It can't exceed 100%, and revenue churn is roughly 100% minus GRR.

NRR asks whether the installed base grows on its own. GRR asks how much of it you keep. You need both, with logo retention beside them.

:::key NRR without GRR hides a leaky bucket
A healthy NRR can come from a few large customers expanding fast while many smaller ones leave. Report NRR, GRR and logo retention together, by segment, and break NRR into starting revenue, expansion, contraction and churn, because the investment decision depends on which of those moved.
:::

### Decompose before you conclude

Build an NRR bridge for each segment: starting revenue a year ago, plus expansion (seats, environments, new products, price increases), minus contraction (downgrades, lower consumption), minus churn (customers lost entirely).

The same NRR can describe opposite businesses. One has strong GRR and modest expansion: it keeps customers and needs a better expansion path, so it should invest in packaging and cross-sell. Another has weak GRR and large expansion from a few accounts: an expansion engine on a leaking base, fine until the big accounts stop growing. That one needs a retention bet, usually in onboarding, adoption or a weak segment.

### Benchmarks and comparability

Benchmarks orient you; they don't set targets. SaaS Capital's 2025 survey of more than 1,000 private B2B SaaS companies found median NRR of 101% and median GRR of 91%. Companies with ACV above $250,000 had median GRR of about 95%, and multi-year contracts showed 103% NRR and 94% GRR. SaaS Capital also associated NRR of 110% or more with above-median growth and NRR below 100% with below-median growth. For enterprise SaaS, Rachitsky and Winters' 2020 practitioner survey put good NRR at about 110% and great at about 130%. These come from different samples and years, so don't mix them.

Before comparing NRR with anyone else's, read their definition: NRR isn't a regulated accounting measure, and companies choose different cohorts, windows and revenue bases. Snowflake's annual report for the fiscal year ended January 2026 reports NRR of 125%, measured on consumption revenue over a trailing two-year cohort of capacity-contract customers, with customers who stopped using the platform kept in at zero. That suits a consumption business and can't be compared with a seat-based subscription NRR.

Usage-priced NRR also moves with workloads: a customer can "expand" because they had a bad quarter with more incidents. Separate environment-driven volume from adoption-driven expansion.

## Customer lifetime value

### What CLV is for

**Customer lifetime value (CLV)** is the present value of the margin a customer will generate over the relationship. Sunil Gupta, Donald Lehmann and Jennifer Ames Stuart, in their 2004 paper "Valuing Customers," define customer value as the expected sum of discounted future earnings, and show that valuing customers this way makes it possible to value a firm, even a fast-growing one with negative earnings.

A PM uses CLV to compare: which segment or channel is worth more after cost to serve, how much to spend acquiring a customer there, whether a retention gain beats an acquisition gain, and how a pricing change alters the value of the base. One company-wide CLV number rarely decides anything.

### Simple and predictive models

The simple model takes margin per period, a retention rate and a discount rate. With constant retention, CLV becomes a multiple of annual margin that depends only on retention and the discount rate, the "margin multiple" view associated with Gupta and Lehmann. It's a good first estimate and shows why retention matters: as retention nears 100%, the multiple climbs steeply.

The weakness is the constant rate, which ignores the sorting effect. Fader and Hardie's 2010 paper on customer-base valuation shows that one aggregate retention rate gives a downward-biased estimate of the remaining value of the existing base, because the customers still with you are, on average, the loyal ones.

Better models weight each period's discounted margin by the survival curve for that segment or account. Fader and Hardie's shifted-beta-geometric model for contracts gives each customer their own constant chance of leaving, varying across customers, which captures the sorting effect simply. Machine-learning models can also predict CLV per account from usage, firmographics and support history.

Use a per-account predictive model when the decision differs by account: where to put customer success capacity, which accounts get an executive sponsor, which renewals get a pricing exception. For segment-level questions, a survival-weighted segment model is usually enough.

### Pitfalls

1. **Revenue instead of margin.** Use contribution margin after the cost to serve. For AI products this matters more than it used to: Bessemer Venture Partners' State of AI 2025 report found its fastest-scaling AI companies averaging gross margins of about 25%, often negative, and its steadier cohort about 60%. Inference cost belongs in the margin line.
2. **One blended retention rate.** Enterprise and mid-market curves differ, and averaging them misstates both.
3. **Expansion forever.** Plug NRR above 100% into a simple formula and value grows without limit. Cap the expansion assumption or let it decay.
4. **Ignoring cost to serve.** Customer success time, support load, partner margin and onboarding effort vary sharply by segment.
5. **False precision.** "Between $0.9M and $1.5M, most sensitive to year-two retention" starts the right conversation; "$1.2M" ends it.
6. **CLV without payback.** A customer worth a lot in year six doesn't fund this year's payroll.
7. **Ignoring the partner layer.** When partners resell or manage your product, model both the partner relationship and each end customer, because partner churn takes many end customers with it.

## Health scores and churn prediction

### What a health score is

A **customer health score** combines several signals into one banded rating per account (green, yellow, red) so customer success and product teams can see which accounts need attention. Gainsight's chief customer officer Kellie Capote described a structure called **DEAR**:

- **Deployment**: is the customer set up to use what they bought? Compare entitlements with what's activated.
- **Engagement**: are you connected to the right stakeholders, beyond one champion?
- **Adoption**: how broadly (across users) and deeply (in core workflows) do they use the product?
- **ROI**: are they reaching the outcomes they bought for, verified against agreed milestones?

DEAR pushes the score beyond usage. Gainsight's scorecard guidance likewise lists sentiment, engagement, relationships and customer value beside usage and adoption, and says to rework the scorecard if churn keeps surprising you. Segment the model too, because what predicts renewal at a large direct account rarely predicts it at a small partner-sourced one. A customer can use your product daily and still leave because the economic buyer never saw the value.

### Rules or a learned model

A health score built this way is a set of rules: a person picks the signals, the weights and the band thresholds. A **churn prediction model** learns the weights from past renewals instead, and can be a survival model of the kind described earlier or a machine-learning classifier over usage, support, billing and relationship data. The learned model often ranks risk better; the rules are easier for a customer success manager to explain to an account and to act on. Many teams run both: the model to rank accounts and the rules to explain the ranking. In B2B the deciding constraint is usually data volume, because a few hundred renewals a year is thin training data, so keep the model simple and check it the same way you check the rules.

### Validate against outcomes

A health score is a prediction, so test it like one. For the last four to eight quarters of renewals, how many churned accounts were green 90 days out, and how many reds renewed happily? If most churned accounts were green, the score is decoration.

Watch for **label leakage**: signals that appear only after the customer has decided to leave, such as a cancellation request, a bulk data export or a request for contract terms. They make a back-test look accurate and fire too late to help. Watch for **score inflation** too: if customer success managers set their own sentiment input and are measured on the share of green accounts, the score drifts green.

### Risk is not the same as response

Eva Ascarza's 2018 research on what she called retention futility belongs in every health-score discussion. The customers most likely to leave aren't necessarily the ones an intervention will save. In her field studies, targeting customers most likely to respond to a retention offer reduced churn more than targeting those at highest risk, and in some cases, as the American Marketing Association's summary notes, targeting the likeliest defectors increased churn.

Some high-risk customers have already decided, and outreach reminds them to cancel; some low-risk customers would have stayed anyway. So use the score to find the at-risk population, offer the intervention (a value review, training, a migration package) to a random half of a risk band, compare outcomes with the other half and target future effort at the kinds of accounts that responded.

:::note A health score answers "who might leave"
It doesn't answer "whom should we act on." Only an experiment answers that. Use the score to find candidates and the pilot to choose among them.
:::

## Sentiment and the voice of the customer

Sentiment shows what customers think and say, which often explains what they do.

### NPS and its critics

Fred Reichheld introduced the **Net Promoter Score** in a 2003 Harvard Business Review article. Customers rate how likely they are to recommend the company from zero to ten. Nines and tens are promoters, sevens and eights passives, zero to six detractors, and NPS is the percentage of promoters minus the percentage of detractors.

It spread because it's simple, and it has been contested almost as long. Timothy Keiningham and colleagues, in a 2007 Journal of Marketing study of Norwegian firms across five industries, couldn't replicate the claim that NPS clearly beats measures such as customer satisfaction at predicting growth. Jeff Sauro's 2018 replication found Reichheld's original analysis had compared NPS with past growth; matched to later growth, NPS explained on average about 38% of the variation in two-year growth. That's a meaningful share, and far from the only number you need.

The sharpest critique comes from NPS's own authors. In "Net Promoter 3.0" (2021), Reichheld, Darci Darnell and Maureen Burns wrote that self-reported scores and misuse had "sown confusion and diminished its credibility," citing practices such as tying scores to frontline bonuses. They proposed **Earned Growth**, an accounting-based counterpart drawn from audited revenue rather than survey answers, which credits growth that comes from repeat and expanded purchases and from customers' recommendations. Because it rests on revenue, it is much harder to game than a survey.

In B2B, samples per account are small, the respondent is often not the person who renews, and one detractor at a top-ten account outweighs twenty promoters at small ones. Report NPS by account and role, next to retention.

### CSAT and customer effort

**Customer satisfaction (CSAT)** surveys ask how satisfied a customer was with a specific interaction, usually right after it: a support case, an onboarding session, a release. They spot a broken touchpoint quickly and say little about renewal.

Matthew Dixon, Karen Freeman and Nicholas Toman argued in "Stop Trying to Delight Your Customers" (Harvard Business Review, 2010) that reducing customer effort drives loyalty in service interactions more than delight does, and introduced the **Customer Effort Score**. For enterprise products, effort is a sharp lens on onboarding, integration and support.

### Text analytics with LLMs

The richest sentiment data is text: tickets, call transcripts, community posts, sales notes, survey comments, churn interviews and post-incident reviews. In 2026 an AI harness can read all of it. The evidence on how well is mixed:

- Zhang and colleagues, testing 13 sentiment tasks across 26 datasets in 2023, found large language models did well on simple polarity, lagged on harder tasks such as sentiment about specific product aspects, and clearly beat small models when labeled examples were scarce.
- Von der Heyde and colleagues, coding open-ended survey answers in 2025, found performance varied widely between models, and uneven accuracy across categories shifted the share of each theme, distorting the overall picture.
- A 2025 pilot by Langer Research Associates had a frontier model code 1,166 survey answers against a human codebook of more than 40 categories. In the first 500 answers, 35% of substantive responses went uncoded or were obviously miscoded, and 42% were acceptable. The model matched on keywords in category names, missed negative meaning in a positively framed question and missed sarcasm. The authors noted the narrow scope and a hard question, and concluded the oversight needed undercut the productivity gain.

Newer models may do better, but the shape of the risk holds: polarity is easy; aspect-level themes, negation, sarcasm and domain language are hard. The answer is the verification protocol in the AI lens below.

For large collections, Anthropic's Clio system (since renamed Anthropic Insights), built to study real-world AI use while protecting privacy, offers a published pattern: extract facets from each item, cluster similar items, have a model summarize each cluster, arrange clusters in a hierarchy and suppress clusters too small to keep individuals anonymous. The same steps fit a voice-of-customer pipeline.

### The voice-of-customer program

A **voice-of-customer (VoC) program** turns listening into decisions. It has five parts:

- **Listening posts**: surveys, tickets, call recordings, community forums, sales and CSM notes, churn and win-loss interviews, and product telemetry.
- **A shared taxonomy**: a stable set of themes (onboarding, reliability, pricing, trust, integrations) that every source maps to, so trends stay comparable.
- **Closing the loop**: respond to the customer who raised an issue, and separately fix the root cause behind a recurring theme.
- **Ownership**: each theme has an owner who reports on it.
- **Revenue linkage**: themes are reported with the retention and revenue of the accounts raising them.

Revenue linkage makes VoC strategic. "Pricing complaints are up" is noise. "Pricing complaints come mostly from mid-market accounts with falling GRR that hold a large share of next quarter's renewals" is a decision. With VoC platforms now proposing themes through generative topic detection for humans to approve, the PM's job is designing the taxonomy, checking the machine and connecting themes to revenue.

## From analysis to strategy

Every analysis in this chapter should end in a decision:

| Analysis | Strategy question | Typical decision |
|---|---|---|
| Survival by segment | Which customers stay, and for how long? | Invest in or exit segments; tighten the ideal customer profile |
| Hazard by lifecycle stage | Where in the lifecycle do we lose customers? | Onboarding, adoption or renewal investment |
| Cohort retention before and after a change | Did the onboarding, pricing or migration change help? | Keep, roll back or extend the change |
| NRR and GRR decomposition by segment | Is expansion masking churn? | Retention bet or expansion bet |
| CLV by segment and channel | Where is a customer worth most after cost to serve? | Channel mix, acquisition spend limits, partner terms |
| Retention and CLV by price plan or package | Does the pricing model keep and grow the customers we want? | Price levels, caps, bundles and which plan to steer new customers toward |
| Health score plus a retention pilot | Whom should we act on? | Customer success capacity allocation |
| VoC themes linked to revenue | Which problems cost us revenue? | Roadmap priority, packaging and pricing changes |

:::leader For product leaders
Ask for these analyses as a set. A portfolio review that sees NRR without GRR, or CLV without survival curves, will fund the wrong bets. Make the retention report a standing quarterly artifact with fixed definitions, owned by product and agreed with finance, so the numbers keep their meaning between reviews.
:::

## How to apply it

Run this method once to build a baseline, then repeat steps 4 to 9 every quarter.

1. **Agree definitions with finance and customer success**: churn (non-renewal, contraction, inactivity for how long), active, revenue base (contracted, billed or consumed) and cohort start (signature or go-live). Disagreement here is the usual reason two teams report different churn for the same product.
2. **Choose three to six segments** that matter for decisions, such as ACV band, channel, industry or onboarding path. More, and every cell is too small to read.
3. **Inventory the sources** (CRM, billing, telemetry, support and success systems, survey tools) and note which your harness reaches through connectors.
4. **Draw contract and usage survival curves by segment**, treating current customers as censored, and read the hazard to see where risk concentrates.
5. **Build cohort triangles** for logo, user and revenue retention, and read them down columns, along rows and along diagonals.
6. **Decompose NRR and GRR by segment**, and reconcile the totals to finance's figures before showing anyone.
7. **Build a CLV model by segment and channel** on contribution margin after cost to serve, with survival-weighted retention, capped expansion and ranges. Name the one or two assumptions that move the answer most.
8. **Define or revalidate the health score.** Back-test it against four to eight quarters of renewals, remove leaking signals and design a randomized pilot for the at-risk band.
9. **Run the VoC analysis** on six months of text, validate the coding on a human-labeled sample and link themes to the revenue and retention of the accounts raising them.
10. **Write the strategy implications.** For each finding, state the decision it supports, the size of the prize, your confidence and what would change your mind. Bring two or three decisions to the portfolio review, not twenty findings.
11. **File the outputs in the Product 360** as durable artifacts with owners and review dates, and log the decisions.

:::onramp If you're new to retention analysis
Start with steps 1, 4 and 6 for one segment. A survival curve that handles current customers correctly and an NRR bridge that reconciles to finance will teach you more about your product than a dozen dashboards.
:::

## The AI lens

### When the product is AI-powered

- **Margin moves.** A more engaged customer can be a less profitable one. Model CLV on contribution margin after inference, and recompute it when routing, pricing or usage changes (Chapter 31 covers the cost levers).
- **Outcome pricing turns usage churn into revenue churn.** Charge per task or per outcome and every drop in usage is an immediate drop in revenue. Usage survival becomes a financial metric, watched weekly.
- **Trust events are churn events.** One visible AI failure can raise the hazard for a whole account. Put trust signals in the health score: rejected AI recommendations, reversed agent actions, escalations after AI involvement, falling acceptance rates.
- **Switching costs may be low.** Bessemer's 2025 report notes that retention in many fast-growing AI products is fragile where switching is easy, so read early AI retention curves skeptically.

### Doing the work with AI

A harness with connectors to your CRM, billing, telemetry and support systems does the mechanics. Your work is a precise request, a verification routine and judgment (Chapter 19 covers asking a harness in general).

**A precise request** names the decision, sources and time window, population and exclusions, every definition, the method in plain words ("survival curve by segment, treating current customers as still active"), the outputs and the checks. It also rules out fitted trend lines, dropped current customers and conclusions from tiny cohorts.

**Verify every output:**

1. **Reconcile** totals to a number you trust, such as finance's ARR or customer count, within a stated tolerance.
2. **Echo the definitions.** Have the harness restate every definition it used; mismatches surface here.
3. **Spot-check records.** Ask for five example accounts behind a finding and check them in the source system.
4. **Show denominators.** Every rate comes with its count. A 40% churn rate on five accounts is an anecdote.
5. **Test sensitivity.** Rerun with a different inactivity threshold or cohort start. If the conclusion flips, it isn't one yet.
6. **Argue the other side.** Ask for the strongest case against the finding, including the sorting effect.

**For text, go further**, because LLM coding fails quietly:

1. Human-label a random sample (100 to 200 items is practical) before trusting automated coding.
2. Measure agreement and read the disagreements.
3. Compare theme shares between human and machine coding as well as item labels, since the distribution can shift while individual labels look fine.
4. Test negation, sarcasm and question framing on purpose.
5. Require verbatim quotes with source references for every theme.
6. Keep a frozen codebook for trend lines, and have the model propose new themes separately for human approval.
7. Remove personal data and check customer agreements and data residency rules before sending customer text to any model, and use only tools approved for customer data.

:::ai The analyst is now a reviewer
A harness can run a survival analysis, a CLV model or a theme analysis in minutes. A wrong answer arrives as fast as a right one and looks just as polished, so spend the time you saved on definitions and checking.
:::

## The Beacon case: what's inside 118% NRR

:::example Where Beacon starts
Beacon reports NRR of 118% on about $48M of ARR across about 420 enterprise customers. Leadership reads that as a healthy base and wants all investment aimed at Beacon Agents and the move to per-resolved-incident pricing. Gross margin has fallen from 81% to 72% since the agentic features launched. Customer success says renewals "feel harder" in the partner channel but can't say why. You're asked for a retention and value review before the annual plan.
:::

**Definitions first.** With finance and customer success you agree that churn is non-renewal of the platform contract, active means at least one weekly active responder in a 28-day window, and cohorts start at go-live. You segment by channel (direct enterprise versus mid-market customers sourced through MSP partners such as Leo's firm) and by Beacon Classic migration.

**The NRR bridge.** The harness reconciles to finance's ARR within half a percent, and the blended 118% splits sharply. In this worked example, direct enterprise accounts show NRR of 124% and GRR of 94%, carried by large customers expanding into Beacon Agents. MSP-sourced accounts show NRR of 101% and GRR of 83%. Direct accounts hold most of the revenue, so the blend looks excellent while the partner channel leaks. Logo retention is starker: most logos lost last year were MSP-sourced.

**The survival curves.** Contract survival for MSP-sourced customers looks acceptable through the first renewal, but weekly active responders start falling about four months after go-live, right after the MSP's onboarding team hands over, and the gap widens until renewal. Leo confirms it in an interview: his engineers configure Beacon per tenant, nobody owns tuning after go-live, and correlation quality drifts as customer environments change.

Two more findings come from the hazard view. Accounts migrated from Beacon Classic show a usage hazard spike in the two months after migration, which matters for the sunset plan (Chapter 30). And at the retail customer hit by the wrong rollback (Chapter 31), responders kept using Beacon to group alerts but stopped accepting its diagnoses for weeks: usage churn at the feature level, invisible in a logo count.

**The health score.** The old score is mostly logins and flagged only a minority of last year's churned accounts as red 90 days out. You rebuild it on DEAR plus a trust component:

- *Deployment*: connectors live against entitled environments (observability, ticketing, chat, CI/CD).
- *Engagement*: relationships with Priya (champion), Marcus (economic buyer) and Sam (security approval current).
- *Adoption*: weekly active responders, share of incidents touched by Beacon, diagnosis acceptance rate.
- *ROI*: MTTR change against the customer's baseline, confirmed in a business review with Marcus.
- *Trust*: rejected diagnoses, reversed agent actions and escalations after agent involvement.

Back-tested on six quarters of renewals, the new score catches far more of the churned accounts, mostly through Deployment and Trust.

**The retention pilot.** Customer success wants to call every red account; you propose Ascarza's approach. Of 40 yellow and red accounts, a random 20 get a guided "Agents readiness review" (connector cleanup, tuning and a value session with the economic buyer) and 20 get normal coverage. After a quarter, reviewed accounts with an active champion improved usage clearly, while those whose champion had left barely moved. Customer success now aims the review at at-risk accounts with a live champion and handles champion loss through an executive sponsor program.

**CLV by channel.** A CLV brief compares channels on contribution margin after inference cost, partner margin and cost to serve. MSP-sourced customers cost far less to acquire, but at current GRR they're worth less than direct customers in every scenario; at direct-level GRR, the channel would return more per dollar in most scenarios. The most sensitive assumption is year-two retention, exactly what the post-handover tuning gap destroys.

**Voice of customer.** The harness codes six months of tickets, post-incident reviews and Northlight Live feedback against the VoC taxonomy. On a human-labeled sample of 150 items, polarity agreement is good, but the pricing theme is undercounted and the model coded "Beacon would be great if it stopped paging me at 3 a.m." as positive. After the codebook gains negation examples, two themes stand out: requests for EU AI Act documentation, mostly from security reviewers like Sam, and worry about unpredictable bills under per-resolved-incident pricing, concentrated in the MSP accounts already showing weak GRR.

**The decisions.** You bring three to the portfolio review:

1. **A retention bet on the partner channel.** Fund multi-tenant tuning and drift alerts for MSPs ahead of two Agents features, measured by MSP-sourced GRR each quarter.
2. **Pricing guardrails.** The per-resolved-incident proposal for Chapter 15 gains a monthly cap and a usage forecast per customer, so bill shock doesn't drive churn in the channel least able to absorb it.
3. **Trust as a retention investment.** Eval quality and the confidence display (Chapter 31) join the retention plan, with the health score's Trust component as the leading indicator.

The board deck keeps the 118% headline and adds a row beneath it with NRR, GRR and logo retention for each channel, so the partner-channel leak is visible every quarter.

## Product 360 artifacts

```template id="09-retention-churn-report-spec" title="Retention and churn report spec"
# Retention and churn report spec · [Product] · v[n] · [Date]

**Owner:** [PM]   **Agreed with:** [Finance lead], [Customer success lead]   **Cadence:** Quarterly   **Next review:** [Date]

## Decisions this report supports
1. [For example: where to invest retention effort next quarter]
2. [For example: whether the onboarding change worked]

## Definitions (fixed; change only with a version bump)
| Term | Definition | Source system |
|---|---|---|
| Customer | [Contracting entity / account] | [CRM] |
| Cohort start | [Contract signature / go-live] | |
| Contract churn | [Non-renewal / termination] | |
| Usage churn | [No active users for N days / usage below X% of baseline] | [Telemetry] |
| Active | [Definition] | |
| Revenue base | [Contracted ARR / billed / consumed] | [Billing] |
| NRR | Revenue now from customers active 12 months ago ÷ their revenue 12 months ago | |
| GRR | As NRR, excluding expansion, cross-sell and price increases (max 100%) | |

## Segments
[Three to six: ACV band, channel, industry, region, onboarding path, migration status]
Minimum cohort size for reporting a rate: [N accounts]

## Sections
1. **Headline**: NRR, GRR and logo retention, overall and by segment, with counts.
2. **NRR bridge** by segment: starting revenue, + expansion, − contraction, − churn.
3. **Contract survival curves** by segment, current customers treated as censored.
4. **Usage survival curves** by segment, with the gap to contract survival.
5. **Hazard view**: where in the lifecycle risk concentrates.
6. **Cohort triangles**: logo, user and revenue retention.
7. **Churn reasons**: coded from exit interviews and notes, linked to revenue lost.
8. **What changed since last quarter** and why.
9. **Implications**: decisions proposed, with size of prize and confidence.

## Checks before publishing
- [ ] Totals reconcile to finance ARR within [x]%
- [ ] Definitions echoed back by the analysis and match this spec
- [ ] Five sample accounts spot-checked in source systems
- [ ] No rate shown without its count
- [ ] Sensitivity to the inactivity threshold tested

## Change log
| Version | Date | Change | Approved by |
|---|---|---|---|
| | | | |
```

```template id="09-clv-model-brief" title="CLV model brief"
# Customer lifetime value model brief · [Product] · [Date]

**Owner:** [PM]   **Finance partner:** [Name]   **Decision it informs:** [For example: channel investment, acquisition spend limits, CS coverage]

## Question
[One sentence. For example: "Is a mid-market customer acquired through partners worth more or less than a direct one, after cost to serve?"]

## Scope
- Segments or channels compared:
- Population and time window:
- Exclusions:

## Model type
Simple (constant retention, margin multiple) / Survival-weighted by segment / Predictive per account
Why this level is enough for the decision:

## Inputs and assumptions
| Input | Value or range | Source | Confidence |
|---|---|---|---|
| Revenue per customer per year | | | |
| Gross margin after inference and hosting | | | |
| Cost to serve (CS, support, onboarding) | | | |
| Partner margin (if any) | | | |
| Retention by year (from survival curve) | | | |
| Expansion assumption (capped or decaying) | | | |
| Discount rate | | Finance | |
| Acquisition cost | | | |
| Horizon | [years] | | |

## Outputs
| Segment | CLV low | CLV base | CLV high | CLV ÷ acquisition cost | Payback period |
|---|---|---|---|---|---|
| | | | | | |

## Sensitivity
The two assumptions that move the answer most:
1.
2.

## What this model doesn't capture
[For example: strategic value of logos, partner-level churn, referral value]

## Recommendation and confidence
[Decision supported, confidence level, what would change it]
```

```template id="09-health-score-definition" title="Customer health score definition"
# Customer health score definition · [Product] · v[n] · [Date]

**Owner:** [PM or CS lead]   **Purpose (decision it drives):** [For example: which accounts get proactive CS outreach]   **Review date:** [Date]

## Population
[Which accounts; segment variants if the model differs by segment]

## Components
| Component | Signal | Source system | Weight | Green | Yellow | Red | Available how early before renewal? |
|---|---|---|---|---|---|---|---|
| Deployment | [Entitled vs activated] | | | | | | |
| Engagement | [Stakeholder coverage: champion, buyer, gatekeeper] | | | | | | |
| Adoption | [Breadth and depth of use] | | | | | | |
| ROI | [Agreed outcome milestones met] | | | | | | |
| Trust (AI products) | [Rejected or reversed AI actions] | | | | | | |
| Sentiment | [Survey, ticket themes] | | | | | | |

## Overall bands
Green: [rule]   Yellow: [rule]   Red: [rule]
Refresh cadence: [daily / weekly]

## Exclusions (leakage check)
Signals deliberately left out because they appear only after a decision to leave:
-

## Playbook per band
| Band | Owner | Action | Response time |
|---|---|---|---|
| Green | | | |
| Yellow | | | |
| Red | | | |

## Validation
- Back-test window: last [4 to 8] quarters of renewals
- Share of churned accounts that were red 90 days before renewal: [x]%
- Share of churned accounts that were green 90 days before renewal: [x]%
- Share of red accounts that renewed: [x]%
- Retention pilot (randomized) planned or run: [link]

## Governance
Who can change weights: [name]   Manual overrides allowed: Yes / No, logged by [name]
```

```template id="09-retention-pilot-plan" title="Retention pilot plan"
# Retention pilot plan · [Intervention] · [Date]

**Owner:** [PM]   **CS partner:** [Name]   **Decision it informs:** whom to target with [intervention] at scale

## Hypothesis
Offering [intervention] to [risk band or segment] will improve [usage measure / renewal] compared with normal coverage.

## Design
- Eligible population: [accounts, risk band, segment]
- Assignment: random, [n] treatment and [n] control
- Intervention: [what exactly happens, who delivers it]
- Control: normal coverage
- Duration: [weeks]
- Primary measure: [for example weekly active users, renewal intent, GRR]
- Secondary measures:

## What we want to learn
Which kinds of accounts respond (for example: champion present, deployment incomplete, segment)

## Guardrails
- No account is denied help it requests
- Stop rule: [condition]

## Result
| Group | Accounts | Primary measure before | After | Change |
|---|---|---|---|---|
| Treatment | | | | |
| Control | | | | |

Accounts that responded most: [characteristics]
Targeting rule going forward: [rule]
```

```template id="09-voc-report" title="Voice-of-customer report"
# Voice-of-customer report · [Product] · [Period]

**Owner:** [PM]   **Sources:** [surveys, tickets, calls, community, CSM notes, churn interviews]   **Items analyzed:** [n]   **Codebook version:** [v]

## Headline
[Two or three sentences: the themes that matter most and what they cost or could earn]

## Themes
| Theme | Share of items | Trend vs last period | Accounts raising it | ARR of those accounts | GRR of those accounts | Owner |
|---|---|---|---|---|---|---|
| | | | | | | |

## For each top theme
**[Theme name]**
- What customers say (three verbatims with source references):
  1. "[Quote]" ([source, date])
  2.
  3.
- Who raises it: [segments, roles]
- Link to retention or revenue: [evidence]
- Root cause (if known):
- Action and owner:

## New themes proposed this period (pending approval)
| Proposed theme | Example items | Approve / merge / reject |
|---|---|---|
| | | |

## Sentiment scores (context only)
| Measure | This period | Last period | Responses | By role |
|---|---|---|---|---|
| NPS | | | | |
| CSAT | | | | |
| Effort score | | | | |

## Closing the loop
- Individual follow-ups completed: [n of n]
- Root-cause fixes shipped since last report:

## Method and quality
- Human-labeled validation sample: [n] items; agreement: [measure]
- Theme shares, human vs machine: [comparison]
- Known weaknesses: [for example negation, sarcasm, a theme undercounted]
- Personal data removed before analysis: Yes / No; approved tool used: [tool]
```

```template id="09-sentiment-analysis-request" title="Sentiment analysis request"
# Sentiment analysis request · [Topic] · [Date]

**Requester:** [PM]   **Decision it informs:** [Decision]   **Due:** [Date]

## Question
[For example: "What are the main sources of frustration among mid-market customers in the last two quarters, and are they linked to lower retention?"]

## Sources and window
| Source | Connector or export | Time window | Approx. volume | Data restrictions |
|---|---|---|---|---|
| | | | | |

## Data handling
- Personal data to remove:
- Customer contract or residency limits checked by: [name]
- Approved tool:

## Codebook
Use codebook v[n] (attached). New themes may be proposed separately, not added.
Sentiment: positive / negative / mixed / neutral, per theme mentioned (aspect level), not only per item.

## Known hard cases to test
- Negation ("would be great if it stopped...")
- Sarcasm
- Positive question framing with negative answers
- Domain terms: [list]

## Validation
- Human-labeled sample: [n] random items, labeled by [names] before seeing machine output
- Report agreement, disagreements and theme shares (human vs machine)

## Outputs
- Theme table with counts, shares and trends
- Three verbatims per theme with source references
- Link to account retention and revenue where the source allows
- Confidence statement and known weaknesses
```

```template id="09-retention-strategy-decision" title="Retention strategy decision"
# Retention strategy decision · [Product] · [Date]

**Owner:** [PM]   **Decision maker:** [Name]   **Decision needed by:** [Date]

## Finding
[One paragraph: what the analysis showed, with the key numbers and their counts]

## Evidence
| Analysis | Result | Confidence | Link |
|---|---|---|---|
| Survival / hazard | | | |
| NRR and GRR decomposition | | | |
| CLV comparison | | | |
| Health score and pilot | | | |
| VoC themes | | | |

## Options
| Option | Type (retention / expansion / pricing / segment exit / channel) | Expected effect | Cost | Risk |
|---|---|---|---|---|
| 1. | | | | |
| 2. | | | | |
| 3. Do nothing | | | | |

## Recommendation
[Option], because [reason].

## Success measure and review
- Leading indicator: [for example usage survival in segment X]
- Lagging indicator: [for example GRR in segment X]
- Review date:
- What would make us reverse this:
```

## Prompts

```prompt title="Build survival curves for contract and usage churn"
Goal: See when customers leave, by segment, for both contracts and usage.
Paste in (or connect the harness to): CRM contract records, billing history and product usage data for [product]; your agreed definitions; the segment list. This involves customer data, so use only an approved tool.

Analyze customer survival for [product] over [time window].

Definitions:
- Cohort start: [go-live / signature date]
- Contract churn: [definition]
- Usage churn: [definition, for example no active users for N days]
- Segments: [list]

Method:
1. Build a contract survival curve and a usage survival curve for each segment. Treat customers who haven't churned as still active (censored), never as churned and never dropped.
2. Show the hazard by period: in which months after start is the risk of leaving highest?
3. Show the gap between usage and contract survival for each segment.
4. Don't fit trend lines or project beyond the observed data.

Output: a chart per segment, a table of survival at 6, 12, 24 and 36 months with the number of accounts at risk at each point, and a one-paragraph finding per segment.

Checks: restate every definition you used; reconcile the starting customer count to [trusted number]; flag any segment with fewer than [N] accounts; list five example churned accounts per segment with their dates.

Check the output: confirm the counts at risk shrink over time but never include churned accounts; open two of the example accounts in the CRM and confirm their dates. If any curve rises, something is wrong.
```

```prompt title="Decompose NRR and GRR by segment"
Goal: Find out whether expansion is masking churn.
Paste in (or connect): ARR or billing by account for the last [13+] months, segment attributes, and finance's reported NRR and ARR. Use an approved tool.

For customers active on [date 12 months ago], calculate by segment:
- Starting recurring revenue
- Expansion (seats, environments, new products, price increases), listed separately
- Contraction
- Churn (customers lost entirely)
- NRR, GRR and logo retention

Present an NRR bridge per segment and a summary table with account counts.

Then:
1. Name the accounts contributing most to expansion and to churn in each segment, and what share of the segment's expansion the top five accounts represent.
2. Tell me whether any segment's NRR depends on a few large accounts.
3. Argue the strongest case that the overall NRR is less healthy than it looks.

Checks: reconcile overall NRR and ending ARR to finance's figures [paste] within [x]%; if they don't reconcile, explain the difference before anything else.

Check the output: if the reconciliation is off, stop and resolve definitions with finance. Read the "less healthy than it looks" argument and decide whether it's true.
```

```prompt title="Draft a CLV model by segment and channel"
Goal: Compare what customers are worth across segments after the cost to serve.
Paste in: survival or retention by segment (from your survival analysis), revenue per account, gross margin after inference and hosting, cost-to-serve estimates, partner margins, acquisition cost by channel and finance's discount rate.

Build a customer lifetime value comparison for these segments: [list].

Rules:
- Use contribution margin after inference, hosting, support, customer success and partner margin, not revenue.
- Use segment-specific retention by year from the survival data, not one blended rate.
- Cap expansion at [x]% per year, decaying to zero by year [n].
- Present low, base and high cases for each segment, and say which assumptions define each case.
- Show payback period beside CLV.

Then name the two assumptions that move the comparison most, and tell me whether the ranking of segments changes under any plausible combination of assumptions.

Don't invent inputs I haven't given you. Where an input is missing, list it as a gap.

Check the output: recompute one segment's base case by hand at a rough level to confirm the order of magnitude. If the ranking of segments flips across the range, report the comparison as uncertain.
```

```prompt title="Back-test a customer health score"
Goal: Find out whether the health score would have warned you in time.
Paste in (or connect): health score history by account, renewal outcomes for the last [4 to 8] quarters, and the score definition. Use an approved tool.

For every renewal in [period], find each account's health score and each component's value 90 days before the renewal date.

Report:
1. A table of outcome (renewed, contracted, churned) against band (green, yellow, red) 90 days before, with counts.
2. Which components best separated churned from renewed accounts.
3. Any signal that appears only shortly before churn (for example cancellation requests, data exports) and may be leaking the outcome.
4. Churned accounts that were green 90 days before: list them and what the data shows about why the score missed them.
5. Suggested changes to weights or components, each with the evidence for it.

Check the output: read three of the "green but churned" accounts yourself in the CRM and CS notes. Reject any suggested signal that only appears after a customer has decided to leave.
```

```prompt title="Code customer text for themes and sentiment"
Goal: Turn tickets, transcripts and survey comments into themes you can trust.
Paste in (or connect): the text sources for [period], the codebook, and a human-labeled sample of [100 to 200] items. Remove personal data first, check customer agreements, and use only an approved tool.

Code each item against the codebook below. For each item:
- Assign one or more themes from the codebook.
- Give sentiment per theme mentioned (positive, negative, mixed, neutral), not only for the whole item.
- Quote the phrase that supports each label.

Rules:
- Use only codebook themes. Propose new themes in a separate list with five example items each; don't add them to the results.
- Watch for negation ("would be great if it stopped..."), sarcasm and positively framed questions with negative answers.
- If an item is ambiguous, label it "unclear" rather than guessing.

Then compare your labels with the human-labeled sample: report agreement per theme, list every disagreement, and compare theme shares between your coding and the human coding.

[codebook]
[human-labeled sample]

Check the output: read every disagreement. If any theme's share differs materially between human and machine coding, revise the codebook with examples and rerun before reporting trends.
```

```prompt title="Link voice-of-customer themes to revenue"
Goal: Find which customer problems cost revenue.
Paste in (or connect): the validated theme coding by account, and ARR, GRR, health band and renewal date by account. Use an approved tool.

For each theme:
1. Count the accounts raising it and the ARR they represent.
2. Compare GRR, health band and churn rate for accounts raising the theme with accounts that don't.
3. Show the ARR up for renewal in the next two quarters among accounts raising it.
4. Give three verbatims with source references.

Rank themes by revenue at risk, not by volume of mentions. Flag any theme where the account count is below [N] as too small to conclude.

Then argue the strongest alternative explanation for the top theme's link to churn (for example, both caused by segment or account size).

Check the output: an association between a theme and churn doesn't prove the theme causes churn. Check the alternative explanation against segment-level data before putting the theme on the roadmap.
```

```prompt title="Turn retention findings into strategy options"
Goal: Move from findings to two or three decisions.
Paste in: your retention report, CLV brief, health score validation, pilot results and VoC report.

Act as a skeptical portfolio reviewer. From the material provided for [product]:

1. List the three findings with the largest revenue or margin implications, with the evidence and confidence for each.
2. For each finding, propose options across these types: retention bet, expansion bet, pricing or packaging change, segment or channel change, do nothing.
3. Estimate the size of the prize for each option as a range, showing the arithmetic and assumptions.
4. Recommend one option per finding and state what result in the next two quarters would make us reverse it.
5. Name the finding most likely to be wrong and why.

Don't invent numbers that aren't in the material. Mark every estimate as an estimate.

Check the output: trace every number back to the source reports. Cut any recommendation that doesn't name a leading indicator you can actually measure.
```

## Anti-patterns

:::warn Celebrating blended NRR
NRR well above 100% goes into the board deck and nobody asks what's under it, while one segment leaks. Show GRR and logo retention beside NRR, by segment, with the bridge.
:::

:::warn Dropping current customers from churn analysis
"We only count customers whose lifetime we know" throws away the longest-lived customers and reports lifetimes far shorter than reality. Treat current customers as survivors whose story isn't finished.
:::

:::warn Reading the sorting effect as stickiness
Retention rises with tenure and the team credits the product, when the loyal customers simply outlasted the rest. Compare like with like, and never extrapolate a fitted trend line.
:::

:::warn Revenue CLV for an AI product
The model uses list price and the old gross margin, with no inference cost, partner margin or customer success time, so the most expensive segment looks the most valuable. Use contribution margin after cost to serve, as a range.
:::

:::warn Calling every red account
Customer success calls every high-risk account. Some had already decided and some didn't need help, so the effort lands where it changes least. Find candidates with the score and learn who responds with a randomized pilot.
:::

:::warn The green account that churned
The health score is mostly logins, nobody back-tests it, and churned accounts were green the quarter before they left. Validate the score against renewals every two quarters.
:::

:::warn One NPS number for the company
A single NPS figure from whoever answered stands in for customer health, though the respondent often isn't the buyer. Report sentiment by account and role, next to retention.
:::

:::warn Trusting LLM theme counts unchecked
The harness codes ten thousand tickets in minutes and the theme chart goes straight to the roadmap review. Validate on a human-labeled sample, compare theme shares and require verbatims for every theme.
:::

## Checklist

- [ ] Churn, active, revenue base and cohort start are defined in writing and agreed with finance and customer success.
- [ ] Contract and usage survival curves exist by segment, with current customers treated as censored, and the hazard view shows where risk concentrates.
- [ ] Cohort triangles cover logo, user and revenue retention.
- [ ] NRR, GRR and logo retention are reported together by segment, with an NRR bridge that reconciles to finance.
- [ ] Any NRR comparison with another company states both definitions.
- [ ] The CLV model uses contribution margin after inference and cost to serve, segment retention and capped expansion, and shows ranges and payback.
- [ ] The health score has components, bands, playbooks and an owner, is free of leaking signals and has been back-tested against at least four quarters of renewals.
- [ ] A randomized retention pilot has informed whom customer success targets.
- [ ] Sentiment is reported by account and role, beside retention.
- [ ] LLM text coding is validated on a human-labeled sample, with theme shares compared and verbatims attached, using approved tools and data stripped of personal details.
- [ ] Each analysis ends in a decision with a leading indicator and a review date in the decision log.

## Key takeaways

- Contract churn in B2B arrives once a year and late. Track usage survival as the leading indicator, and treat current customers as survivors whose story isn't finished.
- Rising retention with tenure is usually the sorting effect. Segment before you conclude, and never project retention with a fitted trend line.
- Report NRR, GRR and logo retention together, by segment, with a bridge of expansion, contraction and churn, and read the definition before comparing with anyone.
- Use CLV to compare segments and channels, built on contribution margin after inference and cost to serve, with segment retention, capped expansion and ranges.
- A health score tells you who might leave; a randomized pilot tells you whom acting on will help.
- LLMs can read every ticket and transcript and fail quietly on negation, sarcasm and theme shares. Validate against human labels and link themes to revenue.
- With a harness doing the mechanics, your work is the definitions, the verification and the decision each analysis supports.
