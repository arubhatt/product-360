# Research notes: Chapter 05, Product Analytics and Iteration

Status: complete (2026-10-30). Tags: [V] verified on primary source; [S] secondary only; [U] not verified online.

## Sources log (working)

1. Kohavi, Henne, Sommerfield. Practical Guide to Controlled Experiments on the Web: Listen to Your Customers not to the HiPPO. KDD 2007. Author PDF (read in full text extract). [V]
2. Kohavi, Tang, Xu. Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing. Cambridge University Press, 2020. https://experimentguide.com/ [V for bibliographic facts]
3. Microsoft ExP (Fabijan et al.). Diagnosing Sample Ratio Mismatch in A/B Testing. Microsoft Research blog, 14 Sep 2020. https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/ [V]
4. Fabijan, Gupchup, Gupta, Omhover, Qin, Vermeer, Dmitriev. Diagnosing Sample Ratio Mismatch in Online Controlled Experiments: A Taxonomy and Rules of Thumb for Practitioners. KDD 2019, pp. 2156 to 2164. [S via search]
5. Evan Miller. How Not To Run an A/B Test. evanmiller.org, 18 Apr 2010. https://www.evanmiller.org/how-not-to-run-an-ab-test.html [V]
6. Rahul Vohra. How Superhuman Built an Engine to Find Product/Market Fit. First Round Review, 13 Nov 2018. https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/ [V]
7. Rodden, Hutchinson, Fu. Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications. CHI 2010. https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/ [V bibliographic]
8. Dave McClure. Startup Metrics for Pirates (slides). SlideShare, 2007. https://www.slideshare.net/dmc500hats/startup-metrics-for-pirates-long-version [V for the five stage definitions; date from general knowledge, see flags]
9. Kohavi, Deng, Vermeer. A/B Testing Intuition Busters. KDD 2022. https://exp-platform.com/abtestingintuitionbusters/ [V bibliographic]

## Raw verified facts (to be organized below)

- OEC definition (Kohavi et al. 2007) [V]: a quantitative measure of the experiment's objective; statistics calls it the response or dependent variable. Paper recommends a single metric, possibly a weighted combination of objectives, because a single metric "forces tradeoffs to be made once" and aligns the organization. Says a good OEC should not be short-term focused; long-term goals belong in the OEC (example: search ads penalty for unclicked ad real estate; repeat visits; latent conversions).
- Limitations of controlled experiments (Kohavi et al. 2007) [V]: (1) quantitative metrics but no explanations (the "why" needs user studies); (2) short-term vs long-term effects (experiments typically run a few weeks); (3) primacy and newness effects, so some experiments must run multiple weeks; one fix is to compute the OEC for new users only; (4) features must be implemented to sufficient quality (paper prototypes complement); (5) consistency (users may see different variants); (6) parallel experiments (strong interactions rare in their experience).
- HiPPO = Highest Paid Person's Opinion; KDD 2007 paper described by exp-platform.com as first peer-reviewed paper to use the term. https://exp-platform.com/hippo/ [V]
- SRM [V, Microsoft blog 2020]: a statistically significant difference between the observed ratio of users in variants and the configured ratio. Detect with chi-square test; Microsoft uses p < 0.0005 threshold (conservative to limit false alarms). "At Microsoft, a recent analysis showed that about 6% of A/B tests have an SRM." Cause taxonomy: assignment, execution, log processing, analysis, experimenter actions (for example uneven ramp-up, self-selection into a variant).
- Peeking [V, Evan Miller 2010]: significance levels assume a sample size fixed in advance; stopping when the dashboard shows significance inflates false positives. Illustration: a do-nothing change with stop-at-first-significance (checking up to 150 observations) gives a 26.1% false positive rate versus the nominal 5%. Remedies: fix sample size in advance, sequential designs, Bayesian designs.
- Sean Ellis test [V via Vohra 2018]: "How would you feel if you could no longer use the product?" Very / somewhat / not disappointed. Ellis benchmarked nearly 100 startups; those struggling almost always had under 40% "very disappointed". Superhuman: 22% start, 33% after narrowing to the very disappointed personas, 58% after about three quarters of work. Four questions: (1) how would you feel; (2) what type of people would most benefit; (3) main benefit; (4) how can we improve. Engine: segment by answer, build high-expectation customer (HXC) profile, analyze somewhat-disappointed respondents whose main benefit matches the core, ignore not-disappointed feedback; roadmap split half doubling down on what lovers love, half fixing what holds back the somewhat disappointed [confirm half/half split, see flags].
- AARRR [V on slides]: Acquisition (users come from channels), Activation (happy first visit), Retention (come back), Referral (like it enough to tell others), Revenue (monetization). 
- Kohavi on minimum scale [S/V mixed]: Kohavi and Thomke, HBR 2017 "The Surprising Power of Online Experiments": any company with at least a few thousand daily active users can run these tests (as quoted in a search excerpt of the HBR PDF). Podcast summaries cite "tens of thousands" and around 200,000 as ideal. Treat the HBR line as the citable one; verify.

## Additional sources log (batch 2)

10. Kohavi and Thomke. The Surprising Power of Online Experiments. Harvard Business Review, Sep to Oct 2017. https://hbr.org/2017/09/the-surprising-power-of-online-experiments [V on article text]
11. Deng, Xu, Kohavi, Walker. Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data (CUPED). WSDM 2013. https://exp-platform.com/cuped/ [V]
12. Rodden, Hutchinson, Fu. HEART paper full text (Google research PDF). https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36299.pdf [V]
13. Twilio Segment. Naming conventions: why you need them for clean data. Twilio resource center, undated. https://www.twilio.com/en-us/resource-center/naming-conventions-for-clean-data [V]
14. Amplitude. Plan your taxonomy (Data planning playbook). Amplitude docs, current. https://amplitude.com/docs/data/data-planning-playbook [V]
15. Sequoia Capital Data Science. Retention. Sequoia articles, undated. https://articles.sequoiacap.com/retention [V]
16. Eric Ries. The Lean Startup (LSE public lecture slides), 12 Jan 2012. https://www.lse.ac.uk/assets/richmedia/channels/publicLecturesAndEvents/slides/20120112_1830_theLeanStartup_sl.pdf [V]
17. Ziegler et al. Productivity Assessment of Neural Code Completion. MAPS 2022 / arXiv 2205.06537. https://arxiv.org/abs/2205.06537 [V abstract]
18. Husain and Shankar. AI Evals: Everything You Need to Know (FAQ). hamel.dev, updated Sep 2026. https://hamel.dev/blog/posts/evals-faq/ [V]
19. OpenTelemetry. Semantic Conventions for Generative AI (repo). GitHub, 2026. https://github.com/open-telemetry/semantic-conventions-genai [V scope only]

## Raw verified facts (batch 2)

- HEART [V, CHI 2010 full text]: categories Happiness, Engagement, Adoption, Retention, Task success. Happiness = attitudinal (satisfaction, visual appeal, likelihood to recommend, perceived ease of use), tracked with a well designed recurring survey. Engagement = behavioral proxies of frequency, intensity or depth over a period; report as average per user, not totals. Adoption = new users starting in a period; Retention = share of users from one period still present in a later one; "using" can be defined as completing a key task. Task success = efficiency (time on task), effectiveness (percent completed), error rate.
- HEART enterprise caveat [V]: the authors say it is not always appropriate to use every category, and that Engagement "may not be meaningful in an enterprise context" where use is part of the job; teams may focus on Happiness or Task success, though feature-level engagement can still matter. Key B2B teaching point.
- PULSE [V]: Page views, Uptime, Latency, Seven-day active users, Earnings. Authors call these low-level or indirect UX measures with ambiguous interpretation (more page views may mean confusion). Seven-day actives could rise even with 100% weekly turnover in theory.
- Goals-Signals-Metrics [V]: Goals (what user tasks, what is the change trying to achieve; resolve disagreement; feature goals differ from product goals; do not worry yet about measurability). Signals (what behavior or attitude shows success or failure; are actions logged; logs and surveys most common; choose signals sensitive and specific; failure often easier to detect, e.g. abandonment, undo). Metrics (normalize raw counts into ratios, percentages, per-user averages; filter automated traffic; ensure key actions are logged).
- Gmail example [V]: engagement metric = percentage of active users who visited on five or more days in the last week; strongly predictive of longer-term retention.
- iGoogle example [V]: satisfaction dropped after redesign then recovered: change aversion. Relevant to reading post-launch dips.
- Event naming [V, Segment/Twilio]: Object Action framework, past tense ("Product Viewed"); recommends Proper Case for events, snake_case for properties; consistency matters more than the choice; never put dynamic values in event names, send them as properties; document every event, property and casing in a tracking plan; tools can validate incoming data against the plan.
- Taxonomy [V, Amplitude]: three steps: define business objectives; break down key metrics into critical paths and actions; optimize events and properties. Prefer one event with a property (Order Completed with Payment Method) over near-duplicate events; avoid overly generic events ("Page Clicked"). Event properties describe one instance; user properties describe the user and persist. Consistent actor (the user's perspective). Capitalization creates distinct events.
- Retention curves [V, Sequoia]: retention = people who tried the product and liked it enough to return. Declining to zero = no product-market fit; flattening = a core keeps returning, higher plateau is healthier; smiling = churned users return. Choose the time window to match natural usage frequency and the "meaningful event" (a completed ride, not an app open).
- Build-Measure-Learn [V, Ries slides 2012]: "Minimize TOTAL time through the loop." Innovation accounting's three learning milestones: (1) establish the baseline (build an MVP, measure how customers behave now); (2) tune the engine (experiment to move metrics from baseline toward the ideal); (3) pivot or persevere (when experiments hit diminishing returns). Metrics should be Actionable, Accessible, Auditable ("the AAA's of metrics"). "Always look at cohort-based metrics over time"; "Split-test the small, measure the large."
- Kohavi and Thomke HBR 2017 [V]: "Any company that has at least a few thousand daily active users can conduct these tests." At Google and Bing only about 10% to 20% of experiments generate positive results; at Microsoft as a whole one third positive, one third neutral, one third negative. Bing social-pane integration cost more than $25 million and produced negligible results. Microsoft ExP experiments expose hundreds of thousands to tens of millions of users and scorecards check hundreds to thousands of metrics.
- CUPED [V]: uses pre-experiment data to cut metric variance; about 50% variance reduction on Bing, which equals the same power with half the users or half the duration. Directly relevant to low-volume B2B.
- Copilot acceptance [V abstract]: acceptance rate of suggestions, rather than persistence of completions in code, best tracked developers' perceived productivity. Supports "acceptance rate" as an AI feature metric, with flags (see below).
- Error analysis [V, Husain and Shankar FAQ]: steps: dataset of representative traces; open coding by a domain expert; axial coding into a failure taxonomy with counts; iterative refinement (an agent can cluster and suggest instances). Review at least 100 traces; annotate 30 yourself before agent suggestions; stop at saturation. One domain expert ("benevolent dictator") is the final voice on quality. Generic off-the-shelf metrics create false confidence; build binary pass/fail checks from your own failure modes and validate against human judgment.
20. Anthropic. Demystifying evals for AI agents. Anthropic Engineering, 9 Jan 2026. https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents [V]

Note on process: the shared web search budget ran out after about 20 searches; remaining facts were verified by direct fetches of primary URLs. AARRR origin date and a few attributions remain secondary (see flags).

---

# ORGANIZED NOTES

## (a) Key concepts and frameworks

### 1. Instrumentation and event design (tracking plan)

Origin: practitioner convention, codified by analytics vendors (Segment "Object Action"; Amplitude "Plan your taxonomy"). Not owned by one thinker, so attribute as "a widely used convention" and name the vendor guides as the source of the specific rules.

Precise summary:
- Start from questions, not events. Amplitude's playbook order: business objectives, then the critical paths and actions behind each key metric, then the events and properties. HEART's Goals, Signals, Metrics gives the same order from the user-experience side.
- Name events Object plus past-tense Action from the user's perspective: "Incident Opened", "Diagnosis Accepted". One convention, applied everywhere; casing differences create separate events.
- Put variable detail in properties, never in names. One event with a property beats near-duplicate events; overly generic events ("Page Clicked") answer nothing.
- Event properties describe one occurrence; user (and, in B2B, account or group) properties describe who did it and persist.
- The tracking plan is the contract between PM, engineering and data: it is validated against incoming data.

Template: tracking plan row (book's format, synthesized from the vendor guides)
| Field | Example (Beacon) |
|---|---|
| Event name (Object Action) | Diagnosis Accepted |
| Trigger (exact moment it fires) | Responder clicks Accept on the root-cause card, or applies the suggested fix |
| Question it answers | Do responders trust the agent's root cause? |
| Metric(s) it feeds | Diagnosis acceptance rate |
| Event properties | incident_id, diagnosis_id, model_version, confidence_band, evidence_count, time_since_page_seconds |
| Actor and account properties | user_role, account_id, plan_tier, region, partner_id |
| Owner | Beacon PM for Diagnose |
| Source | server-side (preferred for trust-critical events) or client |
| Status / version | proposed, implemented, validated; v2 |
| Privacy note | no log content or PII in properties |

B2B and platform application: identity has three levels (user, account, and often a workspace or tenant; for MSPs a partner above the account). Most B2B questions are account-level ("how many accounts reached first value"), so every event needs an account identifier. Server-side events for anything that drives revenue or trust metrics. For agents, the "user" may be a machine: log the actor type (human, agent, automation) as a property.

AI-harness angle: the PM drafts the tracking plan with the AI harness from the PRD and user flows, then asks it to check proposed events against the existing taxonomy for duplicates and naming drift. With an analytics connector (several vendors ship MCP servers by 2026), the PM asks questions in plain language; the tracking plan is what makes those answers trustworthy.

### 2. Core analytics: activation, engagement, retention, funnels

- Activation: the moment a new user or account first gets real value (the AARRR "happy first visit"). Define it as a specific completed action, not a login. HEART's note that "using" a product can mean completing a key task supports this. B2B: activation is per account and often multi-user (connectors installed, first incident correlated, first diagnosis accepted).
- Engagement: frequency, intensity or depth per user over a period, reported per user, never as totals (HEART). Gmail used the percentage of active users who visited on five or more days a week, which predicted longer-term retention. Enterprise caveat from the HEART authors: engagement may mean little when use is part of the job. For Beacon, more time in the product during an incident is bad.
- Retention cohorts and curves: group users or accounts by start period and track the share still active in later periods (HEART definition; Sequoia). Read the curve shape: declining to zero means no product-market fit; flattening means a core keeps coming back, and a higher plateau is healthier; smiling means churned users return. Match the window to natural usage frequency and choose a "meaningful event", not an app open. Ries: always look at cohort-based metrics over time.
- B2B retention has two layers: logo and revenue retention (NRR) as lagging indicators, and product retention (weekly active responders per account, incidents handled with Beacon) as leading ones. Incident tools have bursty, event-driven usage, so normalize by opportunity: share of incidents touched by Beacon, not raw weekly use.
- Funnels: ordered steps with conversion between them. The question is where people drop out and why. In B2B, funnels cross people (admin installs connector, SRE configures, on-call uses) and time (weeks), so build them at account level with time-to-step, not just conversion.

### 3. Product-market fit signals

- Sean Ellis test (Sean Ellis; documented by Rahul Vohra, 2018). Ask: how would you feel if you could no longer use the product? Very disappointed, somewhat disappointed, not disappointed. Benchmark: 40% or more "very disappointed". Ellis set this after benchmarking nearly 100 startups. Vohra's engine adds three questions (who benefits most, main benefit, how to improve) and segments the answers: find the high-expectation customer, convert the somewhat disappointed who value the core benefit, ignore the not disappointed.
- Retention flattening (common practitioner view, stated by Sequoia's data science team): a cohort curve that levels off is behavioral evidence of fit; the survey is attitudinal. Use both.
- B2B application: survey active users within active accounts (respondent count is small, so report the count and treat it as directional); segment by persona (Dana versus Priya versus Marcus), because the buyer and the user answer differently. Ask the economic buyer a different question about renewal intent.

### 4. AARRR pirate metrics (Dave McClure)

Acquisition, Activation, Retention, Referral, Revenue. McClure's definitions: users come from channels; have a happy first visit; come back; like it enough to refer others; pay. B2B adaptation: acquisition is pipeline (often sales-led), referral includes partner and peer references and case studies, revenue includes expansion. The value for a Principal PM is the order: activation and retention problems make acquisition spend wasteful.

### 5. HEART and Goals, Signals, Metrics (Kerry Rodden, Hilary Hutchinson, Xin Fu, Google, CHI 2010)

- Happiness (attitudes: satisfaction, ease, likelihood to recommend, via a recurring survey); Engagement (frequency, intensity, depth per user); Adoption (new users of a product or feature in a period); Retention (share of a period's users still present later); Task success (efficiency, effectiveness, error rate).
- Created as a complement to PULSE metrics (Page views, Uptime, Latency, Seven-day actives, Earnings), which the authors call indirect and ambiguous for judging UX changes.
- Process: for each relevant category, state Goals, then Signals (behavior or attitude that would show success or failure, and whether it is logged), then Metrics (normalized, filtered, dashboard-ready). Choose signals sensitive and specific to the goal; failure signals (abandonment, undo) are often easier.
- Template: HEART grid. Rows = H, E, A, R, T. Columns = Goal, Signal, Metric, Source (logs or survey), Owner. Leave a row blank on purpose and say why.
- B2B application: Task success and Happiness carry more weight than Engagement. For an AI agent, Task success maps to diagnosis accepted and incident resolved; error rate maps to rejected or reverted actions.

### 6. Experimentation (Ron Kohavi, Diane Tang, Ya Xu; Microsoft ExP)

- Controlled experiment: randomly split users between control and treatment; the difference in the OEC is caused by the change.
- OEC (Overall Evaluation Criterion): a quantitative measure of the experiment's objective. Kohavi, Henne and Sommerfield (2007) recommend a single metric, possibly a weighted combination, because it forces tradeoffs to be made once and aligns the organization, and they say long-term goals belong inside it.
- Guardrail metrics: metrics that must not degrade even if the OEC improves (latency, errors, cost, trust). Declared before the test. (The goal, driver, guardrail taxonomy is from the 2020 book; chapter text not fetched, so paraphrase without page cites.)
- Sample ratio mismatch: observed split differs significantly from the configured split; detect with a chi-square test (Microsoft uses p below 0.0005); about 6% of Microsoft A/B tests had an SRM. An SRM invalidates the result until the cause is found (assignment, execution, log processing, analysis, experimenter actions).
- Peeking: checking significance repeatedly and stopping when it crosses the line inflates false positives (Evan Miller's illustration: 26.1% instead of 5%). Fix sample size and duration in advance, or use a sequential method designed for repeated looks.
- Limits (Kohavi et al. 2007): tells you which and how much, not why; short-term window; primacy and newness effects need multi-week runs; features must be built; users may notice inconsistency.
- Base rates (Kohavi and Thomke 2017): only about 10% to 20% of experiments at Google and Bing are positive; at Microsoft, roughly a third positive, a third neutral, a third negative. Teaching point: most ideas fail, so the readout must be honest about nulls.
- Variance reduction: CUPED uses pre-experiment data; about 50% variance reduction on Bing (same power with half the users or time).

Template: experiment design doc (book format)
1. Decision this test informs and who makes it.
2. Hypothesis: We believe [change] for [segment] will [move OEC] because [reason]; we will know when [metric threshold].
3. Unit of randomization (user, account, tenant) and why.
4. OEC, secondary metrics, guardrails (with "must not degrade by more than X").
5. Minimum detectable effect, sample size, duration (whole weeks), stopping rule. No peeking.
6. Population, exclusions, ramp plan.
7. Validity checks: SRM test, A/A or pre-period check, novelty watch.
8. Decision rule written in advance: ship, iterate, or kill for each outcome, including null.
9. Risks, privacy, customer communication (B2B contracts may require notice).

Template: A/B readout
- One-line decision and recommendation.
- Validity: SRM result, data quality, duration served.
- OEC result with confidence interval, not just a p-value.
- Guardrails: each one, pass or fail.
- Segments examined (pre-registered vs exploratory, labeled).
- What we learned, including the "why" from qualitative follow-up.
- Next step and owner.

### 7. When not to A/B test (B2B low volume) and alternatives

- Kohavi and Thomke's threshold: at least a few thousand daily active users. Many B2B products, and almost all account-level decisions, fall below it. Beacon has about 420 customers: an account-randomized test cannot detect modest effects.
- Other reasons not to test: the change is contractually visible (pricing, terms), interference between units (shared on-call teams within one account see both variants), safety (do not randomize a risky autonomous action), or the decision is reversible and cheap anyway.
- Alternatives, from strongest to weakest evidence: account-level randomized pilot with paired accounts; staged rollout with a holdout group; before and after with a comparison group (difference-in-differences); interrupted time series; CUPED-style adjustment using pre-period data to raise sensitivity; offline evals and replay for AI features (run the new model on past incidents); design-partner programs with structured qualitative evidence. Name each method's assumption in the chapter; teach the question "what else could explain this change?" rather than the math.

### 8. Validating the product hypothesis post-launch and iteration planning

- Build-Measure-Learn (Eric Ries): minimize total time through the loop. Plan it backwards: decide what to learn, then what to measure, then what to build. Innovation accounting: establish the baseline, tune the engine, pivot or persevere. Metrics must be actionable, accessible, auditable. "Split-test the small, measure the large."
- Post-launch review template (book format): hypothesis as written before launch; success criteria set before launch; what happened (adoption, activation, task success, guardrails, revenue signal); what customers said; verdict per assumption (validated, invalidated, unclear); decisions; what we would do differently in instrumentation.
- Iteration plan template: for each open assumption, the next test, the evidence that would change the plan, owner, date, and the explicit "stop" condition. Tie each item to a metric on the dashboard.
- Metrics dashboard spec template: purpose and audience; North Star at top; 3 to 5 input metrics; guardrails; definitions (numerator, denominator, window, unit: user or account); segment filters; data freshness; owner; what action each chart should trigger. A chart without a decision attached is cut.

### 9. Analytics for AI features

- Measure quality in production, not only before launch. Anthropic's 2026 guidance layers automated evals, production monitoring, A/B tests, user feedback and transcript review, and human studies; no single layer catches everything.
- Behavioral signals of quality: acceptance (accepted, edited, rejected), corrections and edits, reversions and undos, regenerations, escalation to a human, time to resolution with versus without the AI. Ziegler et al. found the acceptance rate of code suggestions tracked developers' perceived productivity better than whether completions persisted in code; acceptance is a strong but incomplete proxy.
- Consistency matters for agents: pass@k (at least one success in k tries) versus pass^k (all k succeed). A 75% per-trial success gives roughly 42% for three in a row. For supervised remediation, pass^k is the honest metric.
- Error analysis (Hamel Husain, Shreya Shankar): read real traces, write free-text notes, group into a failure taxonomy, count, repeat to saturation (at least 100 traces). One domain expert owns the quality bar. Prefer binary pass or fail checks to 1 to 5 scales; distrust generic off-the-shelf scores.
- Cost per outcome is a product metric for AI features (Beacon's margin fell from 81% to 72%): track inference cost per resolved incident next to quality.
- Instrument AI events with model_version, prompt or agent version, retrieval sources count, tool calls, latency, cost, and the human decision. OpenTelemetry now maintains generative AI semantic conventions (spans, metrics, events, MCP) in a dedicated repository, so engineering traces and product events can share identifiers.

## (b) Verified facts with URL and date

- [V] OEC defined as a quantitative measure of the experiment's objective; single metric recommended. Kohavi, Henne, Sommerfield, KDD 2007. https://exp-platform.com/hippo/ (paper PDF). 2007.
- [V] Six limitations of controlled experiments (no explanation of why, short versus long term, primacy and newness, features must be built, consistency, parallel experiments). Same paper, 2007.
- [V] HiPPO = Highest Paid Person's Opinion; KDD 2007 described as first peer-reviewed paper to mention it. https://exp-platform.com/hippo/
- [V] About 6% of Microsoft A/B tests have an SRM; chi-square detection; p below 0.0005 threshold. Microsoft Research blog, 14 Sep 2020. https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/
- [S] SRM taxonomy paper: Fabijan et al., KDD 2019, pp. 2156 to 2164 (bibliographic details via search, not fetched).
- [V] Peeking: 26.1% false positive rate versus nominal 5% in Miller's example. evanmiller.org, 18 Apr 2010. https://www.evanmiller.org/how-not-to-run-an-ab-test.html
- [V] Book: Trustworthy Online Controlled Experiments, Kohavi, Tang, Xu, Cambridge University Press, 2020. https://experimentguide.com/
- [V] Any company with at least a few thousand daily active users can run A/B tests; 10% to 20% of experiments positive at Google and Bing; one third positive, neutral, negative at Microsoft; Bing social integration cost more than $25 million with negligible results. HBR, Sep to Oct 2017. https://hbr.org/2017/09/the-surprising-power-of-online-experiments
- [V] CUPED: about 50% variance reduction on Bing. Deng, Xu, Kohavi, Walker, WSDM 2013. https://exp-platform.com/cuped/
- [V] HEART categories, PULSE, Goals Signals Metrics, enterprise engagement caveat, Gmail five-of-seven-days metric. Rodden, Hutchinson, Fu, CHI 2010. https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/
- [V] Sean Ellis question and 40% benchmark from nearly 100 startups; Superhuman 22% to 33% to 58%; four-question survey. Rahul Vohra, First Round Review, 13 Nov 2018. https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/
- [V] AARRR stage definitions. Dave McClure, Startup Metrics for Pirates slides. https://www.slideshare.net/dmc500hats/startup-metrics-for-pirates-long-version (date: see flags).
- [V] Object Action naming, Proper Case events and snake_case properties, no dynamic values in names. Twilio Segment, undated. https://www.twilio.com/en-us/resource-center/naming-conventions-for-clean-data
- [V] Three-step taxonomy playbook; one event plus property over duplicates; event vs user properties. Amplitude docs, accessed 2026-10-30. https://amplitude.com/docs/data/data-planning-playbook
- [V] Retention curve shapes (declining, flattening, smiling); match window to natural frequency. Sequoia Capital, undated. https://articles.sequoiacap.com/retention
- [V] Minimize total time through the loop; three learning milestones; AAA metrics; cohort metrics. Eric Ries, LSE lecture slides, 12 Jan 2012. https://www.lse.ac.uk/assets/richmedia/channels/publicLecturesAndEvents/slides/20120112_1830_theLeanStartup_sl.pdf
- [V] Acceptance rate best tracked perceived productivity for Copilot users. Ziegler et al., arXiv 13 May 2022, MAPS 2022. https://arxiv.org/abs/2205.06537
- [V] Error analysis steps; review at least 100 traces; benevolent dictator; binary over Likert. Husain and Shankar, hamel.dev, updated Sep 2026. https://hamel.dev/blog/posts/evals-faq/
- [V] Task, trial, grader, transcript, outcome; code, model, human graders; pass@k versus pass^k (75% per trial gives about 42% for pass^3); layered evaluation. Anthropic Engineering, 9 Jan 2026. https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- [V] OpenTelemetry GenAI semantic conventions now in a dedicated repository covering spans, metrics, events and MCP. GitHub, 2026. https://github.com/open-telemetry/semantic-conventions-genai
- [V] Amplitude runs an official remote MCP server for analyzing product data, experiments and behavior from AI clients (docs, accessed 2026-10-30). https://amplitude.com/docs/mcp (cite as an example that analytics connectors exist; do not name tools in the chapter if house style forbids click-paths).

## (c) Short quotes (under 15 words)

1. "Minimize TOTAL time through the loop." Eric Ries, LSE lecture slides, 2012.
2. "At Microsoft, a recent analysis showed that about 6% of A/B tests have an SRM." Microsoft ExP blog, 2020. (15 words exactly counting "6%"; trim to paraphrase if needed.)
3. "Any company that has at least a few thousand daily active users can conduct these tests." Kohavi and Thomke, HBR 2017. (16 words: paraphrase in the chapter.)
4. "Binary evaluations force clearer thinking and more consistent labeling." Husain and Shankar, evals FAQ, 2026.
5. "No single evaluation layer catches every issue." Anthropic, Demystifying evals for AI agents, 2026 (wording as reported by fetch; recheck before use).

Usable as-is: 1 and 4. Use 2, 3, 5 as paraphrase.

## (d) 2025 to 2026 AI-era developments (verified)

- Analytics through connectors: vendors now expose product analytics, experiments and behavior to AI clients via MCP (Amplitude's official remote server is documented with OAuth setup and works with Claude clients). The PM's job shifts from building charts to asking precise questions and checking definitions. [V docs; launch date not verified]
- Agent evals vocabulary standardized: Anthropic's January 2026 guide defines tasks, trials, graders, transcripts, outcomes and distinguishes pass@k from pass^k; recommends layering offline evals, production monitoring, A/B tests, feedback and transcript review. [V]
- Error analysis as PM-owned practice: Husain and Shankar's FAQ (updated September 2026) puts a domain expert in charge of reading traces and setting binary quality checks, with an agent assisting clustering after 30 manual annotations. [V]
- Telemetry standards for AI: OpenTelemetry generative AI conventions moved into a dedicated repository covering spans, metrics, events and MCP. [V scope; move date [S] June 2026; status reported as Development, [S]]
- Acceptance rate as a recognized AI quality proxy, from the Copilot study (2022), now applied broadly to AI suggestions and agent proposals. [V for the study; broad adoption is an inference]

## (e) Beacon worked example ideas (consistent with beacon-case.md)

1. Tracking plan for Beacon Agents (supervised remediation), launched at Northlight Live. Events: Incident Correlated, Diagnosis Proposed, Diagnosis Accepted, Diagnosis Rejected (property: reason), Diagnosis Edited, Action Proposed, Action Approved, Action Executed, Action Reverted, Incident Resolved. Properties: account_id, partner_id (for Leo's MSP tenants), actor_type (human, agent, automation), model_version, risk_tier, allowlisted (true/false). Sam's requirement: no log content or PII in properties; audit trail separate from analytics.
2. HEART grid for Beacon, explicitly dropping overall Engagement (the HEART authors' enterprise caveat; for Dana, less time in Beacon at 3 a.m. is success). Task success: diagnosis acceptance rate, time from page to accepted diagnosis (Dana's five-minute need), action revert rate. Happiness: quarterly Ellis-style survey to responders. Adoption: accounts with first accepted diagnosis within 14 days. Retention: share of an account's incidents touched by Beacon, by cohort month.
3. Metrics dashboard spec: North Star (incidents resolved with Beacon's help per week) at the top; inputs: alert-to-incident compression, diagnosis acceptance rate, autonomous resolution rate, weekly active responders; guardrails: action revert rate, wrong-root-cause reports, inference cost per resolved incident (margin 81% to 72%), p95 diagnosis latency. Lagging: MTTR, NRR (118%).
4. The hallucinated root cause storyline: the post-launch review finds acceptance rate looked healthy while the revert rate on one customer spiked. Lesson: acceptance without a correctness check rewards confident answers; add "Diagnosis Accepted then Action Reverted within 1 hour" as a failure signal and run error analysis on 100 traces of rejected or reverted diagnoses. Ties to evals chapters.
5. Experiment design: test showing evidence citations inline versus collapsed on diagnosis acceptance. Unit: incident within account? Interference risk (same team), so randomize by account. With about 420 customers, the PM shows that the minimum detectable effect is too large; alternative is a staged rollout with a matched holdout of accounts plus pre-period adjustment (CUPED-style), and offline replay of past incidents. Pricing move to per-resolved-incident is explicitly not A/B tested (contracts, fairness); use design partners and cohort comparison.
6. A/B readout on a high-volume surface where testing is valid: alert grouping UI across all responders in self-serve mid-market tenants. Includes an SRM check that fails because MSP tenants were bucketed by partner_id, so the readout is invalidated and rerun. Shows SRM in a realistic B2B way.
7. PMF check per segment: Ellis survey to weekly active responders; SRE leads (Priya) at 46% very disappointed, on-call engineers (Dana) at 31%, which steers the iteration plan toward Dana's under-five-minute diagnosis. Numbers are fictional and must be labeled as Beacon data.
8. Iteration plan: pivot-or-persevere call on fully autonomous low-risk actions, using Ries's three milestones: baseline (autonomous resolution rate at launch), tune (allowlist templates, approval UX), decide at a dated checkpoint.
9. AI harness use: the PM asks the harness, through the analytics and ticketing connectors, for weekly acceptance by model_version and for a sample of 50 rejected diagnoses with reasons; the harness drafts the readout; the PM checks definitions and SRM before sending to Marcus.
10. Beacon Classic sunset: retention cohort of migrated versus unmigrated accounts as a guardrail during migration.

## (f) Editorial flags

- AARRR date and venue: commonly given as 2007 (500 Hats blog and talks); the original blog URL now redirects and the SlideShare page shows no date. Treat "2007" as [S]. Say "Dave McClure's pirate metrics, introduced in 2007" only if the author accepts a secondary date, or omit the year.
- Sean Ellis 40% origin: primary Ellis post not retrieved; the benchmark of nearly 100 startups is as reported by Vohra (First Round Review, 2018). Attribute through Vohra. Claims that Ellis used it at Dropbox are secondary only; do not use.
- Superhuman roadmap "half on what users love, half on what holds others back": stated in the notes from memory, not confirmed in the fetch. Verify before using.
- "If your retention curve doesn't flatten, you don't have product-market fit" (attributed to Brian Balfour): original not found. Do not quote; attribute the idea to Sequoia's retention guide instead.
- Goal, driver and guardrail metric taxonomy: from Kohavi, Tang and Xu 2020, chapter 7; chapter text not fetched. Paraphrase, no page numbers.
- 6% SRM figure: confirmed on the Microsoft blog; the KDD 2019 paper's exact wording not checked.
- Kohavi minimum scale: HBR 2017 says "a few thousand daily active users". Podcast summaries cite "tens of thousands" or about 200,000; unverified, do not use.
- Facebook "7 friends in 10 days", Slack "2,000 messages" and similar activation magic numbers were not verified in this research. Do not use; they are also consumer or SMB examples.
- Copilot acceptance rate: the study measured perceived productivity, not actual quality. Note in the chapter that acceptance can reward plausible but wrong output (Beacon's hallucinated root cause).
- OpenTelemetry GenAI conventions status (Development vs stable) and repo move date (June 2026) are secondary; describe as "evolving standard".
- Amplitude MCP launch date not verified; describe as "by 2026 major analytics vendors offer MCP connectors" with only the docs as evidence, or keep vendor-neutral.
- Husain and Shankar FAQ page shows update dates in September 2026; content may continue to change.
- Quote 5 wording comes from a summarizing fetch; recheck exact text before printing.
- Templates in (a) are the book's own synthesis, not quoted from any source. Label them as Product 360 formats.
