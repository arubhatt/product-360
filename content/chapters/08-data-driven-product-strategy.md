<p class="lead">Growth numbers decide where a company puts its money, and in most product organizations the PM inherits them from marketing and sales without knowing how they were made. This chapter teaches you to read, question and build those numbers: what a customer costs to win and is worth to keep, where buyers stall on the way in, which channels actually cause demand, and how far you can trust the attribution report that says so.</p>

## Why this matters

A product strategy makes claims about money even when it doesn't say so. "Move upmarket" assumes enterprise deals pay back. "Add a free tier" assumes enough triers convert to cover the cost of serving them. "Invest in partners" assumes partner-sourced customers are cheaper to win or worth more to keep. Each claim rests on growth metrics: acquisition cost, lifetime value, payback, conversion by stage and channel effectiveness.

Senior PMs get into trouble with these numbers in three ways. They accept a blended average, though a company-wide CAC can hide one motion that pays back in a year and another that never does. They treat an attribution report as a causal finding, though a dashboard that credits webinars with 40% of pipeline only describes which touches it saw before deals closed. And they ignore the stages nobody measures. In 2026 a growing share of B2B buying research happens inside AI assistants and peer conversations that never appear in your analytics.

You don't need to run the marketing mix. You do need the numbers that steer product investment to be defined consistently, cut by the segments that matter and tested for causality before anyone bets a roadmap on them. The most valuable thing the data reveals is often a product problem: a trial that never activates, or a security review where deals sit for months.

These numbers sit in the Business dimension of your Product 360, next to the business case (Chapter 13) and pricing (Chapter 15). Chapter 05 covers product analytics after launch, and Chapter 09 goes deeper on lifetime value and retention modeling.

## Growth economics: the numbers strategy runs on

### CAC, LTV and payback

David Skok, a venture investor at Matrix Partners, set out the unit economics of recurring-revenue businesses in his "SaaS Metrics 2.0" guide, first written in 2011. A subscription business works when a customer earns it comfortably more than the customer cost to win, and earns that cost back before the company runs out of capital. The three numbers, in standard form:

- **Customer acquisition cost (CAC)**: total sales and marketing cost for a period divided by the new customers won in it. Say whether it's blended (all channels) or paid only, and whether it's fully loaded (salaries, tools, events, partner commissions).
- **Lifetime value (LTV)**: average revenue per account, multiplied by gross margin, divided by the churn rate. Customer lifetime is one divided by churn.
- **CAC payback**: CAC divided by the monthly gross margin a new customer brings in (new monthly recurring revenue per customer, multiplied by gross margin). The answer is in months.

Skok offers two guidelines. LTV should be more than three times CAC, and payback should be under 12 months. He relaxes the payback guideline for enterprise land-and-expand businesses, where about 20 months can still work because the customer grows after the first deal. Treat them as reference points for a conversation.

Three adjustments matter for B2B and platform products:

- **Expansion breaks the simple LTV formula.** With net revenue retention above 100%, LTV computed from churn alone runs toward infinity. Cap the lifetime (five years is a common choice) and say so, or model expansion with the retention methods in Chapter 09.
- **Gross margin is a product variable.** AI features carry inference cost. If gross margin falls, payback lengthens and LTV shrinks even when price and CAC don't move, so shipping an agentic feature is also a growth decision.
- **Partner economics belong in CAC.** Margin shared with a reseller or managed service provider is a cost of acquiring that customer; leaving it out flatters the partner motion.

:::key Never report a blended CAC alone
Compute CAC, payback and LTV by segment and by motion (direct enterprise, partner, self-serve, cross-sell). The blended number is an average of very different businesses, and strategy decisions are about which of those businesses to grow.
:::

### B2B pipeline metrics

The demand waterfall popularized by SiriusDecisions gave most B2B companies their lead stages: the **MQL** (marketing qualified lead, with intent inferred from signals such as downloads, event registrations and page visits), the **SAL** (accepted by sales), the **SQL** (qualified by sales), the **opportunity** and finally closed-won or closed-lost. The measures that matter are stage conversion, days in stage, win rate and **pipeline coverage** (open pipeline divided by the quota it has to cover). Many teams also track **pipeline velocity**, commonly stated as opportunities times win rate times average deal size, divided by cycle length. It's a practitioner formula with no single author, and it puts the four levers in one line.

Two cautions. In B2B the unit that buys is the account and its buying group (Chapter 01), so a pipeline counted in leads overstates demand when five people from one company download the same white paper. And marketing and sales operations own the stage definitions, which drift. Get the written definition and source system before you use a pipeline number in a strategy argument. You usually own the product-side stages yourself: trial or proof-of-value starts, activation, product-qualified leads and expansion signals.

### Product-led growth and the PQL

OpenView Partners defines **product-led growth** (PLG) as a go-to-market strategy in which the product itself is the primary driver of acquisition, conversion and expansion. By OpenView's own account, its partner Blake Bartlett coined the term in 2016.

Wes Bush of ProductLed sharpened the most useful PLG measure, the **product-qualified lead (PQL)**: a lead who has experienced meaningful value in the product, usually through a free trial or freemium plan. An MQL is qualified by marketing signals (someone opened an email); a PQL is qualified by experienced value (someone got the outcome).

Bush's method for defining a PQL has three steps:

1. Find the behaviors that correlate with upgrading, usually tied to the "aha" moment when users first get value.
2. Review the candidate signals: product interest, number of users, features used, usage and spend patterns, and adoption velocity.
3. Start with a **minimum viable PQL**, a simple threshold such as a number of logins, and refine it toward the behaviors that best predict conversion.

The standard PLG metrics follow the user from sign-up to expansion: sign-ups, activation rate, time to value, trial-to-paid conversion, PQL rate and PQL-to-paid conversion, seat and usage expansion, and net revenue retention. For B2B, add the **product-qualified account (PQA)**, a practitioner term for an account where several users have crossed the PQL threshold. One enthusiastic engineer is a lead; three engineers in the same company accepting the product's output is a buying signal.

In enterprise software, PLG usually shows up as **product-led sales**: the product creates qualified demand and sales closes it. Even sales-led companies now need a measured trial stage. Forrester's *State of Business Buying, 2026* reported that more than 60% of business buyers use a trial to evaluate solutions, rising to 78% for purchases of $10 million or more. If buyers try before they buy, the trial is a funnel stage, and its activation rate is a product metric.

:::onramp If these acronyms are new to you
Learn three before your first growth review: CAC (what a new customer costs), payback (months to earn it back) and PQL (a user who got real value from the product). For each, ask for the segment cut and the definition.
:::

## Designing journeys with data

### The funnel by journey stage

Chapter 01 drew the buying and usage journeys as maps of what people do and feel. This chapter puts numbers on them. Dave McClure's AARRR "pirate metrics" (acquisition, activation, retention, referral, revenue) gave startups one version of the idea; Gartner's six B2B buying jobs give the enterprise version, in which a buying group works through several jobs at once and often loops back. Both replace a single funnel with stages that have their own questions and measures.

A **journey funnel model** records, for each stage:

- the buyer's question at that stage ("Is this problem worth solving?" "Will security approve it?");
- the persona who owns that question;
- the touchpoints: owned (website, docs), paid, earned (press, reviews, community), partner, product and AI answer engines;
- the **entry definition**: what has to be true for an account to count as in this stage;
- a leading metric and the conversion rate to the next stage;
- median time in stage;
- whether the stage is observable (yes, partly or no);
- the owner and the data source, with its blind spots.

The entry definition does most of the work. "Trial started" means nothing until you decide whether it's a sign-up, a connected data source or a first real outcome. Write it so two analysts would count the same accounts.

### The stages you can't see

B2B journeys are non-linear and involve several people, and some of the most important stages leave no trace in your systems. G2's survey of more than 1,000 B2B software buyers in August 2025 found that half now start their buying journey in an AI chatbot rather than a search engine, and that AI chat had become the top source for building a shortlist. G2 sells visibility on its review site, so read the survey as a vendor's finding, but the direction matches Forrester's 2026 report, which describes buyers starting in AI answer engines and then validating what they find with trusted people.

So the journey funnel needs rows for stages you can't observe directly: the AI assistant conversation, the peer recommendation, the community thread. Mark them "not observable" and record how you'll estimate them: self-reported attribution ("How did you first hear about us?"), win-loss interviews and periodic audits of what AI assistants say about your category. A funnel that starts at your first tracked page view describes your instrumentation more than your buyer.

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 300" role="img" aria-label="Journey funnel by stage, with observable, partly observable and invisible stages">
  <rect x="20" y="40" width="120" height="70" rx="10" fill="var(--surface-2)" stroke="var(--border-2)" stroke-dasharray="5 4"/>
  <text x="80" y="68" text-anchor="middle" class="t">Problem</text>
  <text x="80" y="88" text-anchor="middle" class="s">AI answers, peers</text>
  <rect x="150" y="40" width="120" height="70" rx="10" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)"/>
  <text x="210" y="68" text-anchor="middle" class="t">Explore</text>
  <text x="210" y="88" text-anchor="middle" class="s">Docs, reviews</text>
  <rect x="280" y="40" width="120" height="70" rx="10" fill="var(--a1)" fill-opacity=".14" stroke="var(--a1)"/>
  <text x="340" y="68" text-anchor="middle" class="t">Trial / PoV</text>
  <text x="340" y="88" text-anchor="middle" class="s">Activation, PQA</text>
  <rect x="410" y="40" width="120" height="70" rx="10" fill="var(--a1)" fill-opacity=".14" stroke="var(--a1)"/>
  <text x="470" y="68" text-anchor="middle" class="t">Validate</text>
  <text x="470" y="88" text-anchor="middle" class="s">Security, ROI</text>
  <rect x="540" y="40" width="120" height="70" rx="10" fill="var(--a1)" fill-opacity=".14" stroke="var(--a1)"/>
  <text x="600" y="68" text-anchor="middle" class="t">Buy, expand</text>
  <text x="600" y="88" text-anchor="middle" class="s">Win rate, NRR</text>
  <line x1="140" y1="75" x2="150" y2="75" class="ln"/>
  <line x1="270" y1="75" x2="280" y2="75" class="ln"/>
  <line x1="400" y1="75" x2="410" y2="75" class="ln"/>
  <line x1="530" y1="75" x2="540" y2="75" class="ln"/>
  <path d="M600 110 C600 190, 210 190, 210 112" fill="none" stroke="var(--a3)" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="405" y="190" text-anchor="middle" class="s" style="fill:var(--a3)">Customers' recommendations feed the next buyer's early stages</text>
  <rect x="20" y="230" width="16" height="16" rx="3" fill="var(--surface-2)" stroke="var(--border-2)" stroke-dasharray="4 3"/>
  <text x="44" y="243" class="s">Not observable: estimate with self-reports and audits</text>
  <rect x="20" y="258" width="16" height="16" rx="3" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)"/>
  <text x="44" y="271" class="s">Partly observable: anonymous until identified</text>
  <rect x="380" y="230" width="16" height="16" rx="3" fill="var(--a1)" fill-opacity=".14" stroke="var(--a1)"/>
  <text x="404" y="243" class="s">Observable: product, CRM and billing data</text>
  <text x="20" y="22" class="s" style="fill:var(--muted)">One row per stage in the journey funnel model. Shading shows how much your data can see.</text>
</svg>
<figcaption>A B2B journey funnel by stage. The earliest stages, where buyers frame the problem with AI assistants and peers, are the least observable, and they are increasingly where shortlists form.</figcaption>
</figure>

## Measuring channel effectiveness

### What ad metrics measure

Ad platforms report a standard ladder of measures. Impressions and cost per thousand impressions (CPM) describe delivery. Click-through rate and cost per click describe response. Cost per lead, cost per opportunity and return on ad spend (ROAS, attributed revenue divided by spend) describe outcomes, but only the outcomes the platform's attribution credits to the ad. Each step down the ladder is closer to what the business cares about, and each still counts conversions that touched the ad rather than conversions it caused. In B2B, prefer cost per opportunity or per pipeline dollar over cost per lead, because lead volume is the easiest number to inflate. The causal version of each measure divides by incremental outcomes instead: cost per incremental opportunity, or incremental ROAS.

### Incrementality is the question

Every channel report answers some version of "how many conversions touched this channel?" The strategic question is **how many conversions would not have happened without it**. That's **incrementality**, and you can only measure it against a counterfactual: a comparable group that didn't get the activity. The gap between the two questions is large. Brett Gordon, Florian Zettelmeyer, Neha Bhargava and Dan Chapsky compared measurement approaches across 15 large advertising experiments at Facebook (*Marketing Science*, 2019). Observational methods applied to the same campaigns, using the kind of data advertisers typically hold, often failed to recover the lift the experiments measured, generally overestimating it and sometimes substantially underestimating it. The mechanism is selection: ads target people already likely to buy, so exposed people convert more whether or not the ad did anything.

A second lesson matters more in B2B. Randall Lewis and Justin Rao, in the *Quarterly Journal of Economics* in 2015, analyzed 25 large field experiments run by US retailers and brokerages. Even experiments with millions of users gave imprecise estimates of advertising returns, because individual purchase behavior is noisy compared with the effect of an ad. A B2B company with a few hundred target accounts should expect wide confidence intervals. Run experiments anyway, size them honestly and decide in advance what you'll do with an inconclusive result.

### Lift tests at concept level

Three designs cover most cases:

- **User-level randomized lift tests (holdouts).** A random treatment group sees the ads and a control group doesn't. Garrett Johnson, Randall Lewis and Elmar Nubbemeyer's "ghost ads" method (2017) logs the ads the control group *would* have seen instead of paying to show them placebo ads, which cuts cost and sharpens the comparison.
- **Geo experiments (matched markets).** Turn spend on or off in comparable regions and compare outcomes, with no user tracking. In B2B this works only where a region holds enough target accounts to show a difference.
- **Account-level holdouts.** The B2B adaptation: randomly withhold a share of target accounts from a campaign and compare opportunity creation. It's a practice rather than a published framework, and it suits account-based marketing because the target list already exists.

Whatever the design, write the hypothesis, unit of randomization, primary metric, guardrails, minimum detectable effect, duration and decision rule before the test starts. Chapter 05 covers experiment readouts in depth.

### Marketing mix modeling and multi-touch attribution

**Marketing mix modeling (MMM)** works top-down. It relates outcomes to aggregate spend by channel over time, controlling for seasonality and trend. It needs no user-level data, so privacy changes don't break it, but it's slow, needs a long history and struggles with the small conversion volumes of many B2B businesses. Open-source MMM is now free: Google made Meridian, a Bayesian model that works with geo-level data, generally available in January 2025, and Meta's Robyn uses ridge regression with a budget allocator. Both are built to be **calibrated with experiments**. Forrester has noted that Meridian's outputs need statistical skill to interpret, so the scarce resource is now interpretation.

**Multi-touch attribution (MTA)** works bottom-up, assigning credit across the touchpoints it can observe for each person or account before a conversion. It's fast and granular, which suits tuning campaigns in flight. It's also correlational, sees only tracked touches and keeps losing ground to tracking restrictions and consent rules.

| | MMM | MTA | Experiments |
|---|---|---|---|
| Question it answers | How should budget be split across channels? | Which touches preceded conversions? | Did this activity cause additional outcomes? |
| Data | Aggregate spend and outcomes over time | User- or account-level touch paths | Randomized treatment and control groups |
| Strengths | Privacy-durable; sees offline and brand effects | Fast; granular; good for in-flight tuning | Causal; the reference point for the other two |
| Weaknesses | Slow; needs history; weak at low B2B volumes | Correlational; blind to untracked touches | Costly; noisy at small samples; one question at a time |
| Use it for | Annual and quarterly allocation | Campaign optimization | Calibrating MMM and settling big budget calls |

The working default in 2026 is **triangulation**: MMM for allocation, experiments for causal truth and to calibrate the MMM, and attribution for in-flight optimization. When the three disagree, a well-powered experiment wins, and the disagreement tells you where the other two are biased.

## Attribution models and their biases

### The models

Attribution models are rules for splitting credit for a conversion across the touches before it. Each rule has a built-in bias, and in B2B, where a deal may involve dozens of touches across a buying group over many months, the bias decides which team gets budget.

| Model | Rule | What it gets wrong in B2B |
|---|---|---|
| First touch | All credit to the first recorded touch | Over-credits awareness channels; ignores everything that convinced the buying group |
| Last touch | All credit to the last touch before conversion | Over-credits demand capture (branded search, retargeting, the sales email before the meeting); under-credits what created the demand |
| Linear | Equal credit to every touch | Looks fair but makes no causal claim; rewards channels that generate many low-value touches |
| Time decay | More credit to touches nearer conversion | Recency bias; penalizes the early education that long enterprise cycles depend on |
| Position-based (U-shaped) | Most credit to first and last touch, the rest spread across the middle (commonly 40/20/40) | The weights are convention, not evidence; W-shaped variants add opportunity creation as a third anchor |
| Data-driven | Machine learning on path data, comparing converting and non-converting paths | Better than fixed rules, but trained on the platform's own observed data; can't see off-platform touches |

The tooling has already moved. In 2023 Google retired first click, linear, time decay and position-based models from Google Ads and Google Analytics 4, leaving data-driven and last-click attribution; it said fewer than 3% of Google Ads web conversions used the rules-based models. Those models now live mainly in the CRM and marketing automation tools where B2B teams build pipeline attribution.

### Biases that apply to every model

Four biases cut across all of them:

- **Only observed touches count.** Peer referrals, community threads, podcasts and AI assistant answers are "dark" touches, and their credit goes to whatever the model can see.
- **Selection bias.** Targeting puts ads in front of people already likely to buy, so exposure and conversion are correlated before the ad does anything. This is the bias Gordon and colleagues measured.
- **Double counting.** Every ad platform attributes conversions to itself, so the platforms' reports often add up to more conversions than actually happened.
- **The wrong unit.** Person-level models spread credit across individuals when a group made the decision.

Google describes its data-driven model as specific to each advertiser and conversion event, comparing exposed users with a holdback group of similar users. That improves on fixed rules, but it's still the platform grading its own homework. Use it to optimize within that platform, and use experiments to decide how much budget the platform deserves.

:::key Use attribution as a lens
Choose the attribution model for the decision it supports, write down what it over-credits and under-credits, and never move strategic budget on attribution alone. Strategic allocation needs an experiment or a calibrated model behind it.
:::

## Measurement after the privacy shifts

For several years, product and marketing teams planned for the end of third-party cookies in Chrome. It never came. The position as of this edition, based on Google's most recent statement (October 2025):

- **Chrome kept third-party cookies.** Google dropped its plan to deprecate them in July 2024. In April 2025 it said it would not roll out a standalone prompt for third-party cookies either, leaving users to choose in Chrome's privacy settings; Incognito mode blocks them by default. In October 2025 Google retired most of the Privacy Sandbox technologies, including the Attribution Reporting API, citing ecosystem feedback and low adoption, while committing to keep working on an interoperable attribution standard through the W3C. The only restriction actually rolled out was a test on 1% of Chrome users in 2024.
- **iOS requires permission to track.** Since iOS 14.5, enforced from April 2021, apps must use Apple's AppTrackingTransparency framework to ask permission before tracking users across other companies' apps and sites or reading the device's advertising identifier. Without consent, the identifier returns zeros.

User-level journeys were already incomplete, and consent requirements, platform rules, ad blockers and browser privacy settings keep making them more so. The privacy-safe attribution API that teams were waiting for has been retired. Plan measurement on the assumption that you'll never see the whole path, and lean on assets you already own:

- **First-party data**: CRM records, product telemetry and billing data, which describe the account that buys.
- **Aggregate models**: MMM needs no user-level data.
- **Experiments**: account-level and geo holdouts need no cross-site tracking.
- **Self-reported attribution**: "How did you first hear about us?" at sign-up or the first sales call captures touches no tracking will.

## How strategy uses these numbers

Growth metrics earn their place when they change a strategic choice. They inform the two choices Chapter 03 takes from A.G. Lafley and Roger Martin's *Playing to Win*, where to play and how to win, and a third: where to put the next dollar.

**Where to play.** LTV, CAC and payback by segment and motion show which customers and routes to market are worth growing. A motion that pays back in 15 months and expands at 130% deserves a different investment from one that pays back in 30 months and churns.

**How to win.** Conversion and time-in-stage data from the journey funnel model show the **binding constraint**: the stage where the most value is lost. Very often it's a product problem. Trials that never activate point at onboarding and time to value; deals that sit in security review point at missing controls and documentation. Fixing the constraint usually beats buying more demand that will pile up at the same stage.

**Investment allocation.** MMM and experiments inform budget shifts. The strategy memo states the expected incremental return as a range, and the test result that would change the decision.

**Long term against short term.** John Dawes of the Ehrenberg-Bass Institute offers a heuristic he calls the 95:5 rule: only about 5% of B2B buyers are in market at any time, and the other 95% won't buy for months or years. Dawes presents it as a rule of thumb rather than a measured constant, and the implication doesn't depend on the exact split: attribution that credits only in-market capture will starve the activities that make buyers remember you when they do enter the market.

**The guardrail.** Goodhart's law warns that a measure turned into a target stops being a good measure. Set an MQL target and you'll get MQLs. Pair every growth target with a quality measure from the next stage (MQL-to-opportunity rate, PQL-to-paid conversion, first-year retention) so that gaming one shows up in the other.

:::leader For product leaders
Insist on one written definition for every growth metric used in portfolio reviews, with a named owner and source system. Many arguments about growth strategy between product, marketing and sales turn out to be arguments about definitions; settle those once, at the portfolio level.
:::

## How to apply it

This method builds the growth evidence behind a product strategy over roughly one quarter. It assumes an AI harness connected to the CRM, product analytics and billing, and marketing and sales operations willing to work with you on definitions.

**Weeks 1 and 2: Agree the definitions.**

1. List every growth metric your strategy depends on (CAC, payback, LTV, NRR, stage conversions, activation, PQL or PQA) with its definition, owner, source system and time window. Where teams define a term differently, record both and agree one.
2. Decide the cuts: at minimum segment and motion (direct, partner, self-serve, cross-sell), plus region if economics differ by region.

**Weeks 2 to 4: Build the scorecard and the journey funnel.**

3. Ask the harness for CAC, payback and LTV by motion and segment, each figure traced to its source and the gross margin it assumes. Fill the growth metrics scorecard.
4. Draw the journey funnel model with sales, marketing and customer success. Write each stage's entry definition, pull conversion and median time in stage, and mark how observable each stage is.
5. Name the binding constraint, the stage with the largest loss or longest wait, and ask what product change would move it.

**Weeks 4 to 6: Audit the attribution.**

6. Fill an attribution assessment for the report that budget decisions actually use.
7. Add a self-reported attribution question at sign-up or first meeting if none exists, and compare its answers with the tracked view.

**Weeks 6 to 12: Test what matters.**

8. Pick the one or two bets where the money is large and the evidence weakest, and write a channel experiment plan for each. A B2B test may need two quarters to read.
9. If the company runs an MMM, ask whether it has been calibrated with experiments, and offer yours as calibration points.

**Week 12: Decide and write it down.**

10. Write the data-driven strategy memo, with impact as a range and the result that would change your mind. Chapter 34 covers memo writing; Chapter 29 covers the review where it gets decided.
11. Put the scorecard and funnel on a monthly review cadence. Refresh the numbers each month, and change a definition only when the review agrees to, with the old and new versions recorded.

:::note Bring a memo to the review
A dashboard shows what happened. A strategy memo says what you'll do about it, and what evidence would make you stop. Executives can act on the second.
:::

## The AI lens

### Building AI-powered products

AI products change the growth math in ways that classic SaaS metrics hide.

- **Inference cost moves payback.** Gross margin sits in the denominator of payback, so when an AI feature lowers margin every customer takes longer to pay back. Put gross margin by product line on the scorecard and recompute payback when it moves. Chapter 15 covers pricing that keeps margin aligned with usage.
- **Activation means trust.** For an AI product, a login is a weak activation signal. Define the PQL around accepted outputs (an accepted diagnosis, a merged suggestion, an approved action).
- **Usage pricing makes LTV a range.** When revenue depends on consumption or outcomes, average revenue per account varies more from month to month. Report LTV and payback as ranges with the assumption behind each end.
- **AI products meet longer validation.** Gartner reported in May 2026 that 69% of B2B buyers turn to sales reps to validate AI-generated insights. Buyers apply the same skepticism to an AI product's own claims, so expect security, legal and AI governance reviews to add a stage to the journey, and measure it.
- **AI assistants describe your product to buyers.** If an assistant gets your product wrong, buyers carry the error into the evaluation, which makes accurate public documentation a product concern.

### Answer engines and acquisition in 2026

Google said at its May 2025 developer conference that AI Overviews had reached 1.5 billion monthly users in 200 countries and territories, and that AI Mode was rolling out to everyone in the US. Pew Research Center tracked the browsing of 900 US adults in March 2025 and found that 18% of their Google searches produced an AI summary. When a summary appeared, users clicked a traditional result in 8% of visits, against 15% when it didn't, and clicked a link inside the summary in about 1% of visits. (Gartner predicted in 2024 that traditional search volume would fall 25% by 2026; treat that as a forecast, since this edition found no data confirming it.) In January 2026, according to press reports, OpenAI announced it would test ads in ChatGPT for US users on its Free and Go tiers, which makes answer engines a potential paid channel as well as an organic one. For a PM, that means:

- **Fewer, later, less attributable clicks.** Buyers arrive with a shortlist already formed in an assistant, and your attribution credits whatever they touched next.
- **An invisible stage.** The AI conversation belongs in the journey funnel model, marked not observable and estimated from self-reported attribution and audits.
- **Share of answer.** A practitioner metric is emerging: how often, and how accurately, AI assistants mention and recommend your product for the questions your target buyers ask. Run a fixed set of buyer questions across the major assistants on a schedule and score presence, position and accuracy.
- **Evidence feeds answers.** Assistants draw on public documentation, review sites, community discussion and third-party material, so clear, current documentation is now an acquisition asset.

Pranjal Aggarwal and colleagues named this **generative engine optimization (GEO)** in a KDD 2024 paper. In their benchmark, some content changes improved visibility in generative engine responses by up to 40%, varying by domain. That shows visibility can be influenced; vendor GEO playbooks remain untested tactics.

### AI in attribution and growth analytics

The measurement platforms now use machine learning throughout. Beyond Google's data-driven attribution and open-source Bayesian MMM, Meta has added an incremental attribution setting that uses holdouts and machine learning to estimate which conversions an ad caused, for bidding and reporting. Expect reported conversions to fall when you turn it on, because it counts fewer of them. Each of these tools is trained on what its owner can observe, and no platform is a neutral judge of its own effectiveness.

### Doing the work with AI

With an AI harness connected to the CRM, product analytics, billing and ad platforms, you can ask for payback by motion or conversion by stage and get a draft in minutes instead of waiting in an analyst's queue. The bottleneck moves from getting numbers to defining them consistently and judging whether they mean what they seem to mean, so your evidence standard becomes the main skill. Ask the harness for:

- the denominator and time window of every rate, and the segment cuts behind any average;
- the source system and filter for every figure that will reach a decision memo;
- a range wherever a number comes from a model or a small sample;
- what the data can't see: dark touches, unobservable stages and accounts missing from the join.

Watch for three failure modes. The harness may join records incorrectly (contacts to the wrong account, renewals counted as new logos) and produce a plausible, wrong number. Definitions drift silently, so "MQL" in the marketing automation system and in the CRM report may count different things. And a fluent narrative can make noisy data sound conclusive. Spot-check the joins yourself; Chapter 19 covers checking AI-generated analysis in depth.

:::ai The one-line rule
Let the harness do the counting and drafting. Keep the definitions, the causal judgment and the decision for yourself, and never let a number into a memo that you can't trace to a source.
:::

When the analysis involves customer records, pipeline data or contract values, use only AI tools your company has approved for that data.

## The Beacon case: finding where Beacon's growth money should go

:::example Where Beacon starts
Beacon's ARR is about $48M, up 38% year over year, with net revenue retention of 118%. Gross margin fell from 81% to 72% after the agentic features launched. The planning cycle opens with a marketing proposal to raise paid demand spend by a third to hit next year's new-logo target, and your VP asks you to bring a product view of growth to the review. The cost, funnel and channel figures below are used only in this chapter.
:::

**The ARR bridge.** You start by splitting last year's growth. Prior-year ARR was about $34.8M ($48M divided by 1.38). With NRR at 118%, existing customers now contribute about $41.0M, so expansion net of churn added about $6.3M and new logos about $7.0M. Nearly half of Beacon's net new ARR came from the installed base, yet the proposal puts all the incremental money into net-new demand.

**The scorecard.** The harness pulls a year of closed-won deals and sales and marketing cost by motion. Beacon won about 90 new logos at an average first-year contract value of about $78K, on about $12M of new-logo sales and marketing spend: a blended CAC of about $133K. At the old 81% gross margin, payback would be about 25 months; at today's 72% it's about 28. Both exceed the roughly 20 months Skok allows for enterprise land-and-expand businesses, and the agentic margin drop alone added about three months without anyone in sales or marketing doing anything differently.

The blended number hides three different businesses:

| Motion (fictional) | New logos | First-year ACV | Fully loaded CAC | Payback at 72% margin | NRR |
|---|---|---|---|---|---|
| Direct enterprise (Marcus signs) | 50 | about $102K | about $180K | about 29 months | 115% |
| MSP partners (Leo's firms), partner margin in CAC | 25 | about $40K | about $72K | about 30 months | 132% |
| Cross-sell to Northlight Observe customers | 15 | about $60K | about $80K | about 22 months | 112% |
| Blended | 90 | about $78K | about $133K | about 28 months | 118% |

Cross-sell pays back fastest. The MSP motion pays back slowly on the first contract but expands fastest, because each partner adds tenants. Direct enterprise is the largest and slowest. The cross-sell result also sharpens a standing tension: Beacon's cheapest growth comes from Northlight Observe customers, which pulls toward building on Observe data and away from staying tool-agnostic.

**The journey funnel.** You map the direct and cross-sell journey with sales and customer success. Priya asks an AI assistant how to cut alert noise, reads Beacon's docs and a community thread, and starts a proof of value on one environment. Activation is the first correlated incident; an account becomes a PQA when three or more responders accept a Beacon diagnosis. Then Sam runs a security review, Marcus builds the ROI case for his CFO and procurement closes.

Over the past year, about two thirds of 210 proofs of value reached a first correlated incident within two weeks, and accounts that became PQAs converted at more than twice the rate of those that didn't. The median deal then spent 74 days in Sam's security review and 19 in Marcus's ROI case. Deals rarely died in the trial; they waited in security review, where Sam's team asked the same questions about least privilege, audit logs, data residency and AI risk documentation every time. That's the binding constraint, and more paid demand would only lengthen the queue.

**The attribution assessment.** Marketing's pipeline dashboard uses last touch and credits Northlight Live registrations and branded search with most of the pipeline. A first-touch view of the same deals credits documentation traffic, referrals from AI assistants and in-product prompts inside Northlight Observe. Neither sees what the self-reported question at proof-of-value sign-up shows: many champions first heard of Beacon from a colleague or a community thread. The chosen model decides which team gets the budget, and none of them sees where many deals started.

**The channel experiment.** Most of the proposed increase would fund a paid social and webinar program aimed at about 600 target accounts. You propose an account-level holdout: randomly withhold 20% of them (about 120) for two quarters and compare opportunity creation rates, with the metric and decision rule registered in advance. With so few accounts only a large effect will be detectable, so you plan to read the result alongside self-reported attribution.

**The answer engine audit.** The harness runs a fixed set of buyer questions ("best tool to find the root cause of production incidents," "AIOps for managed service providers") across the major AI assistants each month. One assistant describes Beacon as autonomous by default. That's wrong (actions run behind a human approval gate, and only low-risk actions a customer allowlists run on their own), and it's exactly the claim that alarms reviewers like Sam. The fix is clearer public documentation of approval gates, audit logs and allowlists.

**The memo.** Your data-driven strategy memo recommends holding paid demand flat until the holdout reads out, and moving the proposed increase toward three things:

- Northlight Observe cross-sell and MSP expansion, where payback or expansion is strongest.
- A self-serve trust center (security documentation, audit log samples, data residency details and AI risk documentation) to shorten Sam's review, with median days in security review as the success metric.
- Continuing the move to per-resolved-incident pricing, which ties price to the value delivered and to the inference cost that drives margin (Chapter 15).

It names the evidence that would reverse the call: a clear lift in opportunity creation from the holdout, or a security-review median that doesn't fall after the trust center launches.

## Product 360 artifacts

```template id="08-growth-metrics-scorecard" title="Growth metrics scorecard"
# Growth metrics scorecard · [Product] · [Period] · v[n]

**Owner:** [PM]   **Definitions agreed with:** [marketing ops, sales ops, finance]   **Last refreshed:** [Date]

## Definitions (one line each, with source system)
- CAC: [blended or paid only; fully loaded or not; includes partner margin?] · Source: [system]
- Gross margin used: [%, by product line] · Source: [finance]
- LTV: [formula; lifetime cap in years; expansion treatment] · Source:
- Payback: CAC / (new monthly revenue per customer x gross margin) · Source:
- Activation: [event that counts] · PQL / PQA: [threshold] · Source:

## Scorecard by motion and segment
| Motion / segment | New logos | First-year ACV | CAC (fully loaded) | Gross margin | Payback (months) | LTV:CAC | NRR | Activation rate | PQL or PQA rate | Win rate | Median cycle (days) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Direct enterprise | | | | | | | | | | | |
| Partner / MSP | | | | | | | | | | | |
| Self-serve | | | | | | | | | | | |
| Cross-sell | | | | | | | | | | | |
| **Blended** | | | | | | | | | | | |

## Reference points
LTV:CAC above 3 and payback under 12 months (Skok); up to about 20 months for enterprise land-and-expand. Note any motion far outside these and why.

## What changed since last period
| Metric | Motion | Change | Cause (evidence) | Action |
|---|---|---|---|---|
| | | | | |

## Known gaps
[Missing data, definition disputes, motions too small to read]
```

```template id="08-journey-funnel-model" title="Journey funnel model"
# Journey funnel model · [Product] · [Segment] · [Date]

**Owner:** [PM]   **Built with:** [marketing, sales, customer success]   **Unit:** account / user

| Stage | Buyer question | Persona | Touchpoints (owned, paid, earned, partner, product, AI answer) | Entry definition | Leading metric | Conversion to next | Median days in stage | Observable? (yes / partly / no) | Owner | Data source and blind spots |
|---|---|---|---|---|---|---|---|---|---|---|
| Problem framing | | | | | | | | | | |
| Exploration | | | | | | | | | | |
| Trial / proof of value | | | | | | | | | | |
| Activation | | | | | | | | | | |
| Validation (security, ROI) | | | | | | | | | | |
| Purchase | | | | | | | | | | |
| Expansion and advocacy | | | | | | | | | | |

## How we estimate the unobservable stages
- Self-reported attribution question: [wording, where asked]
- Win-loss interviews: [cadence]
- AI answer audit: [cadence, question set]

## Binding constraint
Stage: [ ]   Evidence: [conversion, wait time]   Product hypothesis to fix it: [ ]   Metric to watch: [ ]
```

```template id="08-attribution-assessment" title="Attribution assessment"
# Attribution assessment · [Report or dashboard] · [Date]

**Owner:** [PM]   **Report owner:** [name, team]   **Model in use:** first touch / last touch / linear / time decay / position-based / data-driven / other

## The decision this report supports
[Budget allocation, campaign tuning, channel reviews, comp plans]

## Bias review
| Question | Answer |
|---|---|
| What does this model over-credit? | |
| What does it under-credit? | |
| Which touches can't it see? (peers, community, AI answers, events, partner) | |
| Is the unit right? (person versus account) | |
| Does any platform self-attribute here? Double counting risk? | |
| Is targeting creating selection bias? | |

## Cross-checks
| Method | Available? | What it says | Agrees with the report? |
|---|---|---|---|
| Experiment or holdout | | | |
| MMM (calibrated?) | | | |
| Self-reported attribution | | | |
| Win-loss interviews | | | |

## Verdict
Fit for: [ ]   Not fit for: [ ]   Change needed: [ ]   Review date: [ ]
```

```template id="08-channel-experiment-plan" title="Channel experiment plan"
# Channel experiment plan · [Channel or program] · [Date]

**Owner:** [PM or marketing lead]   **Analyst:** [name]   **Decision maker:** [name]

## Hypothesis
We believe [program] causes [outcome] in [segment], and we'll know we're right if [metric] is at least [x] higher in the treatment group than in the holdout.

## Design
- Unit of randomization: user / account / geo
- Population: [list, size]
- Treatment: [what they get]   Holdout: [share, what they don't get]
- Randomization method and who runs it:
- Duration: [weeks or quarters, with the reason]

## Metrics
- Primary (pre-registered): [ ]
- Guardrails: [ ]
- Minimum detectable effect at this sample size: [ ]

## Decision rule (written before launch)
- If lift ≥ [x]: [scale / keep]
- If no detectable lift: [cut / redesign / combine with other evidence]
- If inconclusive: [what we'll do, and what extra evidence we'll use]

## Threats and mitigations
[Contamination between groups, small sample, seasonality, sales outreach to holdout accounts]

## Readout
Date: [ ]   Result with interval: [ ]   Decision: [ ]   Logged in: [decision log]
```

```template id="08-answer-engine-audit" title="AI answer engine audit"
# AI answer engine audit · [Product] · [Month]

**Owner:** [PM or product marketing]   **Assistants checked:** [list]   **Run by:** [harness, date]

## Fixed buyer question set
| # | Buyer question (as a buyer would ask it) | Persona | Journey stage |
|---|---|---|---|
| 1 | | | |

## Results
| # | Assistant | Product mentioned? | Position in answer | Accurate? | Errors or risky claims | Sources the answer drew on |
|---|---|---|---|---|---|---|
| | | | | | | |

## Share of answer
[Mentions / questions asked, by assistant, against last month]

## Corrections
| Error | Likely source | Fix (docs, reviews, public content) | Owner | Recheck date |
|---|---|---|---|---|
| | | | | |
```

```template id="08-data-driven-strategy-memo" title="Data-driven strategy memo"
# [Decision] · Data-driven strategy memo · [Date]

**Author:** [PM]   **Decision maker:** [name]   **Decision needed by:** [Date]

## The decision we're asking for
[One or two sentences.]

## Context and numbers
[The three to five figures that matter, each with definition and source. Link to the scorecard and funnel model.]

## Options
| Option | Expected incremental impact (range) | Cost | Payback effect | Main risk |
|---|---|---|---|---|
| A | | | | |
| B | | | | |
| Do nothing | | | | |

## Recommendation
[Option, and why the evidence supports it.]

## What the data can't see
[Unobservable stages, attribution limits, small samples, open definitions.]

## What would change our mind
[The experiment result or metric movement that reverses this call, and by when we'll know.]

## Review date
[Date, forum]
```

## Prompts

```prompt title="Build a growth metrics scorecard by motion"
Goal: Get CAC, payback and LTV by motion and segment, with every number traced to a source.
Paste in (or connect the harness to): closed-won deals for the period, sales and marketing cost by motion, gross margin by product line, and your written metric definitions. Use only tools approved for CRM and financial data.

Using the data provided for [product] over [period], build a growth metrics scorecard with one row per motion ([direct, partner, self-serve, cross-sell]) and segment ([list]).

For each row compute: new logos, first-year ACV, fully loaded CAC (include partner margin or commission in partner CAC), gross margin, CAC payback in months, LTV with a [5]-year lifetime cap, LTV:CAC and NRR.

Rules:
- State the definition, denominator, time window and source system for every metric.
- Show the calculation for payback and LTV for one row so I can check it.
- If expansion makes the churn-based LTV formula meaningless, say so and use the cap.
- Flag any motion with fewer than [20] deals as too small to read reliably.
- Don't fill gaps with estimates. Write "no data" instead.

Check the output: recompute payback for one motion by hand from the figures shown. Confirm the new-logo count matches the CRM report finance uses.
```

```prompt title="Draft a journey funnel model and find the binding constraint"
Goal: Put numbers on each stage of the buying journey and find where value is lost.
Paste in: stage definitions, opportunity and trial data with stage timestamps, product activation events, and any self-reported attribution answers. Use an approved tool for customer data.

Build a journey funnel model for [product] in [segment], with the account as the unit. Use these stages: [list].

For each stage give: the entry definition I provided, the number of accounts that entered, conversion to the next stage, median and 80th-percentile days in stage, and whether the stage is observable in this data (yes, partly or no).

Then:
1. Name the binding constraint: the stage with the largest loss of accounts or the longest wait, and show the evidence.
2. Compare accounts that reached [PQL or PQA threshold] with those that didn't on later-stage conversion.
3. List which stages this data can't see and how I could estimate them.
4. Suggest two product hypotheses that might relieve the constraint, labeled as hypotheses.

Check the output: confirm that the entry definitions match what you supplied and haven't been reinterpreted. Spot-check five accounts' stage dates against the CRM.
```

```prompt title="Assess an attribution report before it drives budget"
Goal: Know what an attribution report can and can't support before money moves on it.
Paste in: the attribution report or dashboard export, the name of the model it uses, and the decision it's being used for. Pipeline data is confidential, so use an approved tool.

Act as a skeptical measurement analyst. For this attribution report on [product]:

1. Name the attribution model and explain in two sentences how it assigns credit.
2. List what it over-credits and what it under-credits for a B2B buying cycle of [length] with a buying group of [size].
3. List the touches it can't see (peer referrals, community, AI assistants, events, partners) and estimate how material each might be, labeled as a judgment.
4. Check for double counting across platforms and for person-level credit applied to account-level purchases.
5. Say which decisions the report is fit for and which it isn't, and what cross-check (experiment, calibrated MMM, self-reported attribution) would settle the largest open question.

Don't treat attributed conversions as caused conversions.

Check the output: if the model claims a channel "drove" pipeline, ask it to restate the claim as "touched." If the restated claim no longer supports the decision, you've found the problem.
```

```prompt title="Design an account-level holdout test"
Goal: Plan a channel experiment that can give a causal answer at B2B volumes.
Paste in: the program description, the target account list size, historical opportunity creation rates for similar accounts and the budget at stake. Use an approved tool for account and pipeline data.

Design an account-level holdout experiment for [program] targeting [n] accounts in [segment].

Include: the hypothesis; randomization method (stratified by [size, region, existing customer]); holdout share and the reason; primary metric and guardrails; duration; the minimum detectable effect at this sample size, with the arithmetic shown; threats such as sales reps contacting holdout accounts; and a decision rule for a positive, null and inconclusive result.

Be honest about power. If the sample can't detect a plausible effect, say so and propose how to combine the test with other evidence (self-reported attribution, longer duration, a geo design).

Check the output: confirm the minimum detectable effect is computed from the baseline rate you supplied. Make sure the decision rule was written for the null case, not only the win case.
```

```prompt title="Audit what AI assistants say about your product"
Goal: Measure share of answer and catch inaccurate AI descriptions before buyers repeat them.
Paste in: a fixed list of 15 to 30 buyer questions by persona and stage, your product's accurate positioning and key facts, and the list of competitors.

For each question in the list, ask [assistants available to you] as a buyer would and record: whether [product] is mentioned, its position in the answer, the competitors mentioned, whether the description of [product] is accurate against the facts provided, any risky or false claims, and the sources the answer cites.

Then summarize share of answer by assistant and by persona, list every inaccuracy with its likely source, and propose a documentation or content fix for each.

Run the questions exactly as written, with no product name added unless it's in the question.

Check the output: rerun three questions yourself and compare. Answers vary between runs, so treat a single month as a sample and watch the trend.
```

```prompt title="Draft a data-driven strategy memo"
Goal: Turn the scorecard, funnel and experiment evidence into a decision a leader can make.
Paste in: the growth metrics scorecard, the journey funnel model, the attribution assessment, any experiment readouts and the decision being asked for. These hold confidential financials, so use an approved tool.

Draft a two-page strategy memo for [decision maker] on [decision].

Structure: the decision asked for; the three to five numbers that matter, each with its source; options including "do nothing," each with expected incremental impact as a range and its effect on payback; the recommendation; what the data can't see; the result that would change the recommendation; and the review date.

Rules:
- Use only numbers in the material provided. Cite the artifact each comes from.
- Separate measured effects (experiments) from correlations (attribution) in the wording.
- Don't round ranges into single numbers.

Check the output: trace every number back to the source artifact. Delete any sentence that claims a channel or feature "drove" an outcome without experimental evidence.
```

## Anti-patterns

:::warn The blended CAC
One company-wide CAC and payback number gets used to argue for every motion at once. The average hides a motion that pays back in under two years and another that may never pay back. Cut every growth metric by motion and segment before it enters a strategy discussion.
:::

:::warn Attribution as causation
"Webinars drove 40% of pipeline" goes into a board deck on the strength of a last-touch report. The report shows which touches preceded deals. Only an experiment or a calibrated model can say what caused them. Write "touched" until you have causal evidence.
:::

:::warn Funding the stage you can see
Budget flows to whatever the tracking can observe, so demand capture gets richer and the stages that create demand (peer recommendations, community, AI answers) get starved. Put the unobservable stages in the funnel model and estimate them on purpose.
:::

:::warn More demand into a blocked funnel
Deals stall in security review or trials fail to activate, and the plan is to buy more leads. The new leads queue at the same stage. Find the binding constraint first; it's often a product fix.
:::

:::warn Margin-blind growth
An AI feature launches, inference cost lowers gross margin and nobody recomputes payback. Growth looks unchanged until finance notices. Put gross margin by product line on the scorecard and update payback whenever it moves.
:::

:::warn The underpowered test read as a verdict
A two-month holdout on 80 accounts shows no significant lift, and the program is declared worthless (or a small positive blip is declared proof). Size the test before you run it, write the decision rule for a null result and combine thin evidence with other sources.
:::

## Checklist

- [ ] Every growth metric in the strategy has one written definition, an owner, a source system and a time window.
- [ ] CAC, payback, LTV and NRR are reported by motion and segment, with partner margin in partner CAC and payback recomputed when gross margin moves.
- [ ] The PQL or PQA is defined by experienced value, and its link to paid conversion has been checked.
- [ ] The journey funnel model has entry definitions, conversion, time in stage and observability for every stage, including AI assistant and peer stages.
- [ ] The binding constraint is named, with evidence, and has a product hypothesis attached.
- [ ] Every attribution report used for budget has an attribution assessment listing its biases and blind spots.
- [ ] A self-reported attribution question is in place at sign-up or first meeting.
- [ ] Large budget or product bets have a channel experiment plan with a pre-registered metric, minimum detectable effect and decision rule, and any MMM in use is calibrated against experiments.
- [ ] A monthly AI answer engine audit tracks share of answer and accuracy.
- [ ] The strategy memo states expected impact as a range, what the data can't see and what would reverse the call.
- [ ] Every number in the memo traces to a reproducible source, and AI-generated figures have been spot-checked.

## Key takeaways

- Cut CAC, payback and LTV by motion and segment. The blended number averages different businesses, and strategy is a choice between them.
- Gross margin is a product variable. AI inference cost lengthens payback even when price and acquisition cost stay the same.
- Build the journey funnel by stage, with written entry definitions, and include the stages your data can't see. The binding constraint is often a product problem rather than a demand problem.
- Attribution describes which touches preceded a conversion. Incrementality, measured with experiments, tells you what caused it; use MMM, experiments and attribution together, and let the experiment win when they disagree.
- Chrome kept third-party cookies, but user-level measurement keeps eroding through consent, ATT and browser settings. Plan on first-party data, aggregate models, experiments and self-reported attribution.
- B2B buyers increasingly start in AI assistants. Track share of answer and the accuracy of what assistants say, and treat clear public documentation as an acquisition asset.
- Let the AI harness pull and draft the numbers. Keep definitions, causal judgment and the decision with you, and trace every figure to a source.
