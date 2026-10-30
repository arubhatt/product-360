<p class="lead">Every offering you ship will eventually stop growing, and most will eventually be retired. Lifecycle management is the discipline of knowing where each offering, module, API and model dependency sits on that path, setting investment to match, and, when the time comes, ending things on dates customers can plan around.</p>

## Why this matters

Product teams are good at starting things and bad at ending them. Launches get a plan, a date, a keynote slot and an executive sponsor. Retirements get a support ticket from an angry customer who found out by accident. The asymmetry is expensive in both directions. Offerings that should be harvested keep absorbing engineering capacity, and offerings that should be retired get switched off abruptly, which burns the trust you need for the next migration.

In B2B and platform businesses the cost is higher than in consumer products, for three reasons.

1. **Customers build on you.** An enterprise customer has wired your product into runbooks, integrations, compliance evidence and training. Removing a feature breaks their systems as well as their habits. Every API, webhook and data format you publish is a promise with a lifetime, whether or not you wrote the lifetime down.
2. **Contracts encode the lifecycle.** Notice periods, support commitments, data return and deletion terms and partner agreements often decide what you can retire and when. A PM who discovers these terms after the announcement has a legal problem as well as a product one.
3. **Your own dependencies have lifecycles.** In 2026 many enterprise products depend on third-party models, cloud services and protocols that are themselves deprecated on someone else's schedule. A model behind one of your features can be retired with 60 days' notice, the minimum Anthropic publishes for its publicly released models, and preview models at some providers can go with two weeks' notice. Lifecycle management now runs in both directions: the promises you make and the promises made to you.

This chapter covers the whole arc: assessing each offering's real stage, setting investment to match, gating irreversible moments, balancing the portfolio, and running end-of-life, API deprecation and model deprecation as planned programs with owners. It's the Lifecycle dimension of your Product 360, and it connects directly to strategy (Chapter 03), pricing (Chapter 15), governance (Chapter 29) and AI-powered products (Chapter 31).

## Core concepts and frameworks

### The product life cycle and its four stages

The product life cycle (PLC) describes an offering's sales over time as an S-shaped rise followed by a plateau and a fall. Theodore Levitt's 1965 Harvard Business Review article "Exploit the Product Life Cycle" argued that executives knew the concept but rarely used it to plan, and set out to make it a practical management tool. Later writers added a fifth stage at the start; Fox's 1975 version, for example, includes precommercialization before launch.

The four classic stages each call for a different posture. Here's how they typically show up in a B2B or platform business:

| Stage | Typical signals | What the PM optimizes | Investment posture |
|---|---|---|---|
| **Introduction** | Slow adoption, design partners and lighthouse customers, high cost to serve, roadmap driven by discovery | Product-market fit in a narrow segment; learning per dollar | Invest selectively, price for learning |
| **Growth** | Rapid ARR growth, new competitors arriving, go-to-market scaling | Capture share; harden the platform; widen integrations and the partner channel | Invest heavily |
| **Maturity** | Growth slows to the market's rate, pricing pressure, retention and expansion dominate | Margin, packaging, efficiency; extend the curve with new segments or adjacent jobs | Sustain, and fund the next curve |
| **Decline** | Shrinking usage, falling share of new bookings, a successor exists or should | Cost to serve, orderly migration, trust | Harvest, consolidate or retire |

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 320" role="img" aria-label="The product life cycle curve rising through introduction and growth, flattening in maturity and falling in decline, with an extension curve branching off in maturity and the posture for each stage below">
  <line x1="60" y1="250" x2="650" y2="250" class="ln"/>
  <line x1="60" y1="30" x2="60" y2="250" class="ln"/>
  <line x1="190" y1="40" x2="190" y2="250" stroke="var(--border-2)" stroke-dasharray="4 4"/>
  <line x1="330" y1="40" x2="330" y2="250" stroke="var(--border-2)" stroke-dasharray="4 4"/>
  <line x1="500" y1="40" x2="500" y2="250" stroke="var(--border-2)" stroke-dasharray="4 4"/>
  <path d="M60 240 C 130 238, 160 225, 190 200 S 290 90, 330 80 S 450 62, 500 80 S 600 170, 640 205" fill="none" stroke="var(--a1)" stroke-width="3"/>
  <path d="M430 68 C 470 55, 520 40, 600 36" fill="none" stroke="var(--a2)" stroke-width="2.5" stroke-dasharray="6 5"/>
  <text x="560" y="28" class="s" style="fill:var(--a2)">Extension: new segment or job</text>
  <text x="125" y="58" text-anchor="middle" class="t">Introduction</text>
  <text x="260" y="58" text-anchor="middle" class="t">Growth</text>
  <text x="415" y="58" text-anchor="middle" class="t">Maturity</text>
  <text x="575" y="110" text-anchor="middle" class="t">Decline</text>
  <text x="30" y="140" text-anchor="middle" class="s" transform="rotate(-90 30 140)">Revenue or usage</text>
  <text x="355" y="268" text-anchor="middle" class="s">Time (a hypothesis to review each planning cycle, not a schedule)</text>
  <rect x="60" y="280" width="128" height="32" rx="8" class="box"/>
  <rect x="192" y="280" width="136" height="32" rx="8" class="box"/>
  <rect x="332" y="280" width="166" height="32" rx="8" class="box"/>
  <rect x="502" y="280" width="148" height="32" rx="8" fill="var(--surface-2)" stroke="var(--a3)"/>
  <text x="124" y="301" text-anchor="middle" class="s">Invest to learn</text>
  <text x="260" y="301" text-anchor="middle" class="s">Invest to scale</text>
  <text x="415" y="301" text-anchor="middle" class="s">Sustain, fund next curve</text>
  <text x="576" y="301" text-anchor="middle" class="s" style="fill:var(--a3)">Harvest or retire</text>
</svg>
<figcaption>The classic product life cycle with an investment posture per stage. The dashed curve is the point of the critique: decisions in maturity can bend the line upward, and treating a plateau as decline can bend it down.</figcaption>
</figure>

### Why the curve misleads

The PLC has had serious critics almost from the start. Nariman Dhalla and Sonia Yuspeh, writing in Harvard Business Review in 1976 under the title "Forget the Product Life Cycle Concept!", opened with a floor wax brand whose sales had leveled off. Research suggested more advertising could revive it; management launched a new product instead. Their broader argument, as it's usually summarized, is that the curve is a result of marketing decisions rather than an independent force. Call a plateau "decline," cut investment, and the decline arrives on schedule. Even Levitt treated locating a product on the curve as a matter of judgment more than measurement.

Three features of 2026 software make the critique sharper:

- **Continuous delivery resets the curve.** A SaaS product that ships every week rarely follows one smooth bell. Features age at different rates inside the same product.
- **Platforms have stacked curves.** The core product, its modules, its API versions and its model dependencies each sit at a different stage. "Our product is in maturity" is almost always too coarse to act on.
- **AI features commoditize fast.** A capability that was a differentiator at introduction can become table stakes within months as general-purpose models improve. Summarization is the obvious example. The stage can change between two planning cycles.

The practical conclusion is to keep the PLC as a vocabulary and drop it as a forecast. Assess the stage of each offering, module, API version and model dependency separately. Treat the stage as a hypothesis backed by evidence, and let it set the investment posture until the next review.

:::key Treat the stage as a decision input
A lifecycle stage is your best current reading of the evidence, and it's partly self-fulfilling. Write down the signals behind the call, your confidence and the one signal that would change your mind. Then review it every planning cycle.
:::

### Lifecycle stage assessment

A lifecycle stage assessment turns the stage from a feeling into an evidence-backed call. For each offering, you collect a small set of signals over a stated window: growth against the market; share of new bookings (is this still how customers enter, or only how old customers renew?); net revenue retention and gross churn; cost to serve, including support and on-call load; competitive parity with rivals' bundles and general-purpose AI tools; dependency risk from platforms, models or protocols being retired; and strategic fit with the strategy in Chapter 03.

The output is a stage, a confidence level (low, medium or high), the single signal that would change the call, and an **investment posture**: invest, sustain, harvest or retire. Harvest means you keep the offering serviceable and profitable while deliberately spending less on it. Retire means you start an end-of-life program.

Two of these signals deserve extra attention. **Engineering share against revenue share** catches the most common failure: a declining product absorbing far more capacity than its revenue justifies, usually because its old architecture generates incidents. **Dependency risk** catches the newest one: an offering in healthy growth can be forced into a migration because a model or protocol it relies on is being retired.

### Portfolio lifecycle balance

A single offering's stage tells you how to manage it. The mix of stages across a portfolio tells you whether the business has a future. The classic tool here is the Boston Consulting Group's growth-share matrix, first sketched by Alan Zakon and popularized by Bruce Henderson's 1970 essay "The Product Portfolio." It sorts offerings by market growth and relative share into four groups: **stars** (invest), **cash cows** (milk to fund the others), **question marks** (invest or discard) and what BCG first called pets and later **dogs** (liquidate, divest or reposition). BCG's own summary notes that every product eventually becomes either a cash cow or a pet.

The matrix maps loosely onto the PLC. Question marks are usually in introduction, stars in growth, cash cows in maturity and dogs in decline. For a PM, the useful output is a one-page portfolio view: each offering's stage, posture, share of revenue and share of engineering capacity. Three patterns should worry you:

1. **Everything in maturity.** Strong cash flow, no next curve. The portfolio will look healthy until a competitor's new category arrives.
2. **Everything in introduction.** Lots of bets and no cash engine to fund them. Common in AI-first startups and new business units.
3. **Decline consuming growth's capacity.** A retiring product holds a larger share of engineering than of revenue, and the growth offerings are starved. This is the pattern a sunset usually fixes.

:::leader For product leaders
Review lifecycle balance at the portfolio level at least twice a year, alongside the business reviews in Chapter 29. Ask each group PM what share of their capacity goes to each stage, and whether that matches the posture you agreed.
:::

### Stage gates

Robert G. Cooper's **Stage-Gate** process, a term that first appeared in print in 1988, breaks new product development into stages separated by decision gates. In the commonly published form it runs from Discovery through five stages: Scoping (or Concept), Build the Business Case, Development, Testing and Validation, and Launch, followed by a post-launch review.

Each gate has the same anatomy:

- **Deliverables**: what the team brings to the gate, defined in advance.
- **Criteria**: what the gatekeepers judge, covering both readiness and business value, often scored with tools such as scorecards and Expected Commercial Value.
- **Outputs**: a decision and, if the decision is to proceed, an approved plan, resources and the date of the next gate.

Cooper's gates allow four decisions: **Go**, **Kill**, **Hold** and **Recycle**. Kill is the important one. A gate that has never killed anything is a status meeting. Later generations of Stage-Gate borrowed from agile practice, adding build-and-test cycles, rapid customer validation and sprints inside stages, so the model no longer implies a waterfall.

For B2B and platform products, you rarely need a full gate sequence for every feature. The discovery and delivery methods in Chapters 01, 04 and 11 handle most work. Use light gates at **moments of irreversible commitment**: entering a new segment, declaring general availability, changing price, announcing end-of-sale and ending support. Those are the points where reversing course costs customers or money.

The same logic runs in reverse at the end of the lifecycle. This book uses four **retirement gates**:

| Gate | Question | Typical evidence | Possible decisions |
|---|---|---|---|
| **R1 Consider retirement** | Should we start planning an end-of-life? | Stage assessment, engineering against revenue share, successor readiness | Go to planning, Hold, Recycle (fix and re-invest) |
| **R2 Announce end-of-sale** | Are we ready to tell customers and stop selling? | Sunset decision memo, legal review, migration path, communication plan | Go, Hold, Kill (keep the product) |
| **R3 End support** | Have enough customers moved to stop fixing it? | Migration progress by ARR, blocker list, extended support uptake | Go, Hold (extend for named accounts) |
| **R4 Decommission** | Can we shut it down and delete the data? | Zero active usage or approved exceptions, data return and deletion evidence | Go, Hold |

Write gate criteria before the first gate. A useful structure separates **must-meet** criteria, which knock a proposal out if any fails (strategic fit, legal and security clearance, no unmitigated customer harm, a funded owner), from **should-meet** criteria scored on a scale (customer evidence, market attractiveness, competitive advantage, feasibility, financial return, risk). Agree the decision rules in advance, so the score can't be argued after the fact.

### End-of-life milestones

Enterprise vendors that sell long-lived products publish end-of-life programs as a sequence of dated milestones. Names vary by vendor, but the pattern is consistent enough to describe generically:

1. **End-of-life announcement.** A public notice that gives every date below and names the recommended successor.
2. **End-of-sale (last order date).** No new orders. Renewals of existing subscriptions may continue.
3. **Last ship date or last new term.** For hardware, the last shipment; for software, the last date a new subscription term can start.
4. **End of software maintenance.** No new features or bug fixes. Security fixes may continue for a period.
5. **End of security fixes.** No more vulnerability patches.
6. **Last date of support.** Support contracts end. Documentation usually stays available for a while.

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 230" role="img" aria-label="End-of-life milestones on a timeline: announcement, end-of-sale, end of maintenance, end of security fixes, last date of support and decommission, with the service level narrowing over time">
  <line x1="40" y1="110" x2="650" y2="110" class="ln"/>
  <circle cx="60" cy="110" r="8" fill="var(--a1)"/>
  <circle cx="160" cy="110" r="8" fill="var(--a1)"/>
  <circle cx="300" cy="110" r="8" fill="var(--a2)"/>
  <circle cx="420" cy="110" r="8" fill="var(--a2)"/>
  <circle cx="540" cy="110" r="8" fill="var(--a3)"/>
  <circle cx="630" cy="110" r="8" fill="var(--a3)"/>
  <text x="60" y="88" text-anchor="middle" class="t">Announce</text>
  <text x="160" y="88" text-anchor="middle" class="t">End-of-sale</text>
  <text x="300" y="88" text-anchor="middle" class="t">End of maintenance</text>
  <text x="420" y="70" text-anchor="middle" class="t">End of security fixes</text>
  <text x="540" y="88" text-anchor="middle" class="t">Last date of support</text>
  <text x="630" y="70" text-anchor="middle" class="t">Decommission</text>
  <rect x="60" y="140" width="240" height="22" rx="6" fill="var(--a1)" fill-opacity=".18"/>
  <text x="70" y="156" class="s">Features off; fixes, security and support on</text>
  <rect x="300" y="168" width="120" height="22" rx="6" fill="var(--a2)" fill-opacity=".18"/>
  <text x="308" y="184" class="s">Security and support</text>
  <rect x="420" y="196" width="120" height="22" rx="6" fill="var(--a3)" fill-opacity=".18"/>
  <text x="428" y="212" class="s">Support only</text>
  <text x="40" y="30" class="s">Migration window: customers move to the successor across the whole span</text>
  <line x1="40" y1="40" x2="540" y2="40" stroke="var(--muted)" stroke-dasharray="5 4"/>
</svg>
<figcaption>A generic end-of-life sequence. Each milestone switches off one kind of service, so customers can see exactly what they lose and when. The migration window runs across the whole span.</figcaption>
</figure>

Public lifecycle policies show two ways to set the dates. Microsoft's **Fixed Lifecycle Policy** sets the timeline at launch: a minimum of five years of Mainstream Support (incident support, security updates and the ability to request non-security fixes and design changes), followed for some products by Extended Support (security updates, paid support, no new features or design changes). After that, security updates are available only through the paid Extended Security Update (ESU) program. Microsoft's **Modern Lifecycle Policy**, for continuously serviced products, works by notice instead: customers stay supported as long as they stay current, stay licensed and the product is still offered. Microsoft commits to at least 30 days' notice when customers must act to avoid significant degradation, and at least 12 months' notice before ending support for a product with no successor (excluding free services and previews).

Microsoft also publishes a precise vocabulary worth borrowing. **Deprecation** means a feature is no longer in active development and may be removed later; it still works. **End of servicing** means a version gets no more quality or security updates. **Removal** means a feature is gone. **Retirement** means a service is no longer available or supported. Teams that use "deprecated" to mean "gone" confuse customers, so define your terms once and publish them.

Other vendors show the variety. Red Hat Enterprise Linux 8, 9 and 10 run a ten-year life cycle in three phases (Full Support, Maintenance Support, then an Extended Life Phase with knowledge base access and limited support but no fixes) and sell paid add-ons for longer coverage. Google Cloud writes its notice commitment into its terms of service: at least 12 months' notice before discontinuing a service or material functionality, or making a backwards-incompatible change to a customer-facing API, with exceptions for legal requirements, material security risk and substantial economic or technical burden, and with pre-GA services excluded.

Windows 10 Home and Pro show a long-signposted end of support at scale: support ended on October 14, 2025, with a published migration path and, for Enterprise, Education and Pro editions in commercial use, an ESU program sold in yearly terms running to October 10, 2028. Microsoft describes ESU as a last-resort paid option and a temporary bridge while customers migrate.

### Paid extended support as a bridge and a lever

Extended support is where lifecycle meets revenue. For Windows Server 2012 and 2012 R2, whose extended support ended on October 10, 2023, Microsoft priced on-premises ESU at the full license price per year for up to three years, back-billed late enrollees and offered ESU free on Azure. One program priced staying put high enough to encourage migration and made the vendor's preferred destination cheaper. Red Hat's paid extensions follow the same pattern.

Extended support is a design choice with three levers: price, duration and scope. Price it as a bridge, cap the duration, limit it to security fixes, and decide whether the successor gets a matching incentive.

### Sunsetting: deciding to retire

Retiring an offering is a strategy decision with a financial case, and it deserves the same rigor as a launch. The **sunset decision memo** states the recommendation in one sentence with dates, then answers seven questions. Why now? Who is affected, by segment, ARR and partner? What are the options (keep investing, maintenance only, sell or open-source, migrate and retire), including the cost of doing nothing, since maintenance is never free? What's the financial impact: ARR at risk, expected migration and churn, savings and one-time costs? What do contracts say about notice, service levels, data return and deletion? How do customers get across? And what would make us pause?

That last question matters more than it looks. A sunset without reversal criteria becomes either a political fight every time a large customer objects, or a deadline enforced against the evidence. Writing the criteria first ("if less than [x]% of affected ARR has migrated by end of maintenance, we extend support for named accounts under paid extended support") turns the escalation into a check against a rule you already agreed.

Revenue recognition, deferred revenue and accounting treatment of credits belong to finance. Flag the questions in the memo; don't answer them yourself.

### Migration plans and customer communication

The migration plan is where most sunsets succeed or fail. Its center is a **feature parity map** (each old capability, its new equivalent, the gap and the workaround), surrounded by segmentation by complexity and ARR, tooling, a parallel run, incentives and per-account tracking.

Stripe's documented pattern for upgrading webhook endpoints is a clean model of a parallel run: create a second endpoint on the new version, run both, switch processing to the new one, monitor, then disable the old endpoint while keeping a path to revert. Customers move with a safety net, and the provider can see who has actually switched.

Communication principles follow from the published policies above. Name every date up front. Name the successor. State what changes at each milestone. Send programmatic signals as well as email, so systems notice even when people don't. Publish one canonical place where every deprecation and its dates live. Then sequence the audiences: pre-brief top accounts and partners before the public notice, send the public notice, remind at fixed intervals, send a final warning, and confirm after retirement. Partners such as managed service providers need earlier notice than direct customers, because they have to migrate their own customers.

### API deprecation policies

APIs are where lifecycle promises are most explicit, because breaking an API breaks someone's code. The published policies of large platforms show a range of approaches, and the common thread is that the length of the promise depends on the stability label you shipped:

| Policy | Core rule |
|---|---|
| **Kubernetes** | Elements are removed only by incrementing the API group version. Generally available APIs may be deprecated but not removed within a major version. Beta APIs are served for at least 9 months or 3 minor releases after deprecation, whichever is longer. Alpha APIs can be removed in any release without notice. |
| **Google AIP-185** | Major versions only, with alpha, beta and stable channels. Beta features can be removed after a deprecation period, recommended at 180 days. Stable versions need a reasonable, well-communicated deprecation period. |
| **GitHub REST API** | Versions are named by release date. Breaking changes ship only in a new version, and the previous version is supported for at least 24 months after a new one ships. |
| **Stripe** | Each account has a default API version, and Stripe recommends pinning the version in code, so customers upgrade on their own schedule. |
| **Model Context Protocol (MCP)** | Features move through Active, Deprecated and Removed. A deprecation must document a migration path (any named replacement must already be Active) and stay in place for at least twelve months from the revision that first marks it deprecated. An expedited removal for an active security risk still gets at least ninety days. |

The MCP policy is worth studying because it's recent and complete. Besides the twelve-month floor, it requires several signals for every deprecation: a deprecated tag in the schema, a notice in the specification prose, a changelog entry and an entry in a single registry of deprecated features with the earliest removal date. Tier 1 SDKs must mark the API deprecated with their language's native mechanism in their next release and should emit runtime warnings. The policy also says features may stay deprecated much longer than the minimum, which is a useful reminder that the floor isn't a target.

Two HTTP standards make deprecation machine-readable. The **Sunset** header (RFC 8594, by Erik Wilde, 2019) signals that a URI will likely stop responding at a given date. The **Deprecation** header (RFC 9745, by Sanjay Dalal and Erik Wilde, March 2025) signals that a resource is or will be deprecated, from a given date. Both are hints, not guarantees, and the Sunset date can't be earlier than the Deprecation date. Each standard also defines a link relation that points to your policy or migration guide. Returning both headers on deprecated endpoints means every client log records the warning, months before anything breaks.

:::onramp If API lifecycles are new to you
Start with three habits. Label every public surface alpha, beta or stable when you ship it. Publish a one-page deprecation policy that says how much notice each label gets. And measure who still calls a deprecated endpoint each week, so you can contact them directly instead of hoping they read the changelog.
:::

## How to apply it

Here's a method for running lifecycle management across a product or portfolio. Steps 1 to 4 are a standing practice you repeat every planning cycle. Steps 5 to 9 run whenever an offering reaches retirement.

**Establish the lifecycle picture.**

1. **Inventory the lifecycle surface.** List every offering, module, edition, public API version, webhook format, SDK and third-party dependency (models, cloud services, protocol versions) you'd have to manage if it changed. For each, record the owner, the stability label it shipped with, the customers or ARR that depend on it and any contract terms that mention it. Most teams find surfaces nobody owns.
2. **Assess the stage of each item.** Run a lifecycle stage assessment for every offering and major module. Gather the signals over a stated window, make the call, record your confidence and the signal that would change it. For dependencies, record the provider's stage and published dates.
3. **Set postures and check the portfolio.** Assign invest, sustain, harvest or retire to each item, and build the one-page portfolio view with revenue share and engineering share side by side. Agree the postures with your manager and finance, and flag any item where engineering share exceeds revenue share by a wide margin.
4. **Gate the irreversible moments.** Write must-meet and should-meet criteria for the gates you'll use: new segment, general availability, price change and the four retirement gates. Name the gatekeepers. Put the next review dates on the calendar. Publish your deprecation policy for APIs and other technical surfaces now, before you need it.

**Retire an offering.**

5. **Write the sunset decision memo and pass gate R1.** Make the case with options, financial impact, contract review and reversal criteria. Pass R1 to start planning, and keep the circle small until R2: early leaks turn a plan into a rumor.
6. **Build the end-of-life plan and pass gate R2.** Set every milestone date, from announcement to decommission, working back from the longest contractual notice period you found. Get legal sign-off on notice, data return and deletion, and partner terms. Get finance sign-off on the revenue impact and any credits or extended support pricing.
7. **Prepare migration and communication.** Build the migration plan (parity map, tooling, parallel run, incentives, per-account tracking) and the deprecation communication plan (audiences, channels, sequence). Pre-brief top accounts and partners before the public notice. Then announce, with every date and the successor named in the first message.
8. **Run the program and pass gate R3.** Track migration weekly by ARR as well as by account count, since a few large accounts can hide behind a good count. Work the blocker list. Watch recently migrated accounts closely, because anything the parallel run missed shows up after cutover. At end of maintenance, apply the reversal criteria you wrote in step 5, not new ones.
9. **Decommission and close.** At gate R4, confirm zero active usage or approved exceptions, return and delete customer data with evidence, remove the offering from price lists and documentation, and run a short retrospective. Update the lifecycle register and the portfolio view.

:::note How long does all this take?
The stage assessment and portfolio view take a few days once the data is accessible, and much less in later cycles. An enterprise end-of-life program usually runs between 12 and 24 months from announcement to decommission, set by your notice commitments, contract terms and how hard the migration is. Plan the internal work (memo, legal review, tooling) for a quarter before the announcement.
:::

## The AI lens

### Building AI-powered products: models have lifecycles too

Every AI feature you ship sits on top of a model with its own lifecycle, set by someone else. By late 2026 the major providers have converged on a similar vocabulary, and the differences in notice periods are large enough to shape your architecture.

| Provider or channel | Lifecycle states | Notice before retirement (as published, October 2026) |
|---|---|---|
| **Anthropic** | Active, Legacy, Deprecated, Retired | At least 60 days for publicly released models; active models carry a "not sooner than" retirement date |
| **OpenAI** | Legacy (no more updates), deprecation (announced with a shutdown date), shutdown | At least 6 months for generally available models, at least 3 months for specialized variants, about 2 weeks possible for previews, shorter for safety or compliance |
| **Microsoft Foundry** | Preview, GA, Legacy (optional), Deprecated, Retired | Standard GA lifecycle of 18 months, deprecated for new customers at 12 months; at least 60 days' retirement notice for GA, 30 days for previews; some partner models follow 12-month lifecycles |
| **Amazon Bedrock** (models launched from September 7, 2026) | Active, Legacy, End-of-Life | An "EOL no sooner than" date per model; Legacy periods of 6 months for most models and 45 days for some |
| **Google Gemini API** | Stable, Preview, Latest alias, Experimental | At least 2 weeks before a preview is deprecated; experimental models may change without notice |

Four lessons follow for a PM.

**Notice periods are short compared with enterprise lifecycles.** Your customers may have contracts with 12 months' notice for material changes, while a model underneath your feature can be retired in 60 days. In 2026 alone, Anthropic deprecated and retired several Claude models, among them Sonnet 4 and Opus 4 (deprecated April 14, retired June 15) and Opus 4.1 (deprecated June 5, retired August 5), with roughly two-month windows. OpenAI announced on June 11, 2026 that older GPT-5 and o3 snapshots would shut down on December 11, 2026. With windows this short, put a model swap on every AI feature's roadmap as a recurring item.

**Channel dates differ from provider dates.** Anthropic and Amazon both note that a model's retirement date on a cloud platform can differ from the provider's own date. If your product reaches the same model through two channels, or in different regions, you have two schedules to track.

**Aliases and pinned versions fail differently.** A "latest" alias changes under you with each release, so behavior can shift without a deploy. A pinned snapshot holds still, then retires. Microsoft Foundry adds automatic upgrades for standard deployments, rolled out region by region, unless the customer opts out, in which case the deployment stops working at retirement. Choose deliberately per feature, and record the choice.

**Lifecycles reach parameters and APIs too.** Anthropic removed the temperature, top_p and top_k sampling parameters in its 2026-10-21 API version. A prompt or integration that depended on them needs the same migration discipline as a model swap.

Watch the vocabulary, too. Microsoft's Foundry documentation warns that an API status of "Deprecated" corresponds to what its docs call retired, so read each provider's definitions before you interpret a status field. Provider practices beyond notice also vary: Anthropic committed in November 2025 to preserve the weights of its publicly released models for at least the lifetime of the company. That doesn't move your migration date, but customers who ask about a provider's practices deserve an accurate answer.

**Your own AI features need the same discipline.** An AI feature can enter decline quickly, either because the model under it is retiring or because general-purpose assistants now do the job. Treat it like any other offering: assess the stage, set the posture and run an end-of-life when it's time. Customers that maintain AI risk documentation, for example in response to the EU AI Act (Chapter 33), may need notice when the model behind a feature changes, even if the feature's behavior looks the same.

The **model deprecation runbook** in the artifacts section turns this into a repeatable process: inventory every model dependency by feature, channel, region and customer tier; watch provider notices and status fields; set an internal deadline well before the provider's; run your eval suite on candidates, comparing quality, latency and cost together; canary and cut over with a rollback path; and tell customers when behavior, data handling or price changes. Microsoft's guidance makes the key point well: evaluate replacements on your own prompts and data, not on public benchmarks alone. The investment that makes all of this cheap is made earlier, in the evals and model abstraction described in Chapter 31.

### Doing the work with AI

Lifecycle work is document-heavy and data-scattered, which suits an AI harness connected to your systems.

- **Assembling the evidence.** With connectors to CRM, billing, product analytics, support and the engineering tracker, the harness can pull every signal for a stage assessment, with sources cited, far faster than a person can. Your job is to challenge the outliers and decide what the evidence means. Chapter 19 covers how to ask and verify.
- **Building the dependency inventory.** Pointed at architecture docs, service catalogs and provider lifecycle pages, the harness can draft the list of model and API dependencies, with each provider's published dates. Have an engineer confirm it; inventories built from docs miss what's only in code.
- **Reading contracts.** Given a set of customer agreements, the harness can extract notice clauses, service-level commitments, data return terms and termination rights into a table. Legal must verify every row before it informs a date. Contract text is confidential, so use only tools your company has approved for it.
- **Drafting communications.** From the end-of-life plan, the harness can draft the end-of-sale notice, the FAQ, partner briefings, in-product banners and the account-team talk track, each tuned to its audience. Check every date and commitment against the plan; drafts that drift by a week cause real damage.
- **Tracking migration.** Asked weekly, the harness can report migration status by account and ARR from telemetry and CRM, flag stalled accounts and summarize customer replies to the notice by theme. Read the angry replies yourself.

:::ai The one rule for AI in lifecycle work
Let the harness assemble evidence and draft every document, then verify every date, number and contractual commitment against a primary source before anything reaches a customer. A wrong date in an end-of-sale notice is a promise you'll be held to.
:::

## The Beacon case: sunsetting Beacon Classic

:::example Where Beacon starts
Beacon Classic is the original 2023 correlation engine from the Northlight Observe era. Beacon's Correlate capability now runs on a newer engine that feeds Diagnose and Beacon Agents, but about 90 accounts still run Classic. Your Product 360 inventory (Chapter 00) found no lifecycle plan for it, and customers were asking. The strategy in Chapter 03 commits to sunsetting Classic to free a team for agentic work. Your job is to turn that commitment into dates customers can plan around. Classic's revenue figures below are illustrative planning numbers.
:::

**The stage assessment.** You assess Beacon's offerings separately rather than calling Beacon "in growth":

| Offering | Stage | Confidence | Posture | Deciding signal |
|---|---|---|---|---|
| Beacon Agents (supervised remediation) | Introduction | Medium | Invest | Design-partner adoption and security approvals |
| Diagnose | Growth | High | Invest | Diagnosis acceptance rate and share of new bookings |
| New Correlate engine | Maturity | Medium | Sustain, include in platform fee | Correlation is being commoditized by platform bundles and AI assistants (Chapter 16) |
| Beacon Classic | Decline | High | Harvest, then retire | About one-eighth of ARR on roughly a fifth of engineering capacity; can't feed Diagnose |

Classic's numbers make the case on their own. Its roughly 90 accounts represent about $6M of Beacon's $48M ARR, flat for a year. It consumes most of one of Beacon's five engineering teams in maintenance and on-call, because its rules engine generates a disproportionate share of incidents. And it can't feed agentic diagnosis, so every Classic customer is a customer who can't buy Beacon Agents. The portfolio view shows the third worrying pattern from earlier in the chapter: decline consuming growth's capacity while gross margin sits at 72% and inference cost work needs people.

**The sunset decision memo.** You write a three-page memo to the VP of Product with three options. *Keep investing* would cost a full team indefinitely to modernize an engine that duplicates the new one. *Maintenance only* frees part of a team but leaves Classic customers stranded outside Agents, and the on-call load stays. *Retire with migration* frees the team within about 18 months and moves Classic customers onto the engine that can feed Diagnose. You recommend the third. The financial section shows ARR at risk (the full $6M in the worst case), a planning assumption that at least 85% of Classic ARR migrates, the engineering capacity freed, and the one-time cost of migration credits and services. Finance owns the revenue treatment of the credits, and the memo says so.

Legal review finds two things. Most Classic contracts have 12 months' notice for material changes, which sets the floor for the support window. A small number of multi-year contracts run past the proposed last date of support, so the plan offers those accounts either migration with credits or support to the end of their current term. Sam, the security and compliance reviewer persona, needs evidence for two things at the end: that Classic data has been returned or deleted on a stated date, and that audit logs for the Classic period are retained as the contracts require.

The memo's reversal criterion is written before the announcement: *if less than 85% of Classic ARR has migrated by end of maintenance, named accounts may buy up to six months of paid extended support, security fixes only, at a premium to their current price.* The pattern echoes Microsoft's ESU program: a bridge priced to be temporary.

**The milestones.** The plan passes gate R2 with these dates, counted from the announcement at Northlight Live (month 0):

| Milestone | Timing | What changes for customers |
|---|---|---|
| End-of-life announcement and end-of-sale | Month 0 | No new Classic subscriptions; migration tooling and credits available |
| End of feature work | Month 0 | Classic receives fixes and security patches only |
| End of maintenance | Month 12 | No bug fixes; security fixes continue |
| Last date of support | Month 18 | Support and security fixes end; data export remains available |
| Decommission and data deletion | Month 18 plus 30 days | Classic is shut down; remaining data deleted with evidence provided |

**The migration plan.** Priya's team, like most Classic customers, has years of tuned correlation rules, and losing them is the biggest anxiety in the customer base. The plan builds a rule-import tool and a parallel run: Classic and the new engine process the same alerts side by side for at least two weeks, and the customer compares compression ratios before switching. No account is migrated silently, and data export is one step. Customers move in waves, with design partners first. Because Chapter 09's analysis showed a usage drop in the two months after migration, every migrated account gets a customer success check-in at 30 and 60 days, and Chapter 19's finding that migrated accounts accept fewer diagnoses keeps them out of the pricing pilot until their acceptance reaches the native range.

Marcus, the economic buyer persona, gets a different message: the migration doesn't touch uptime targets, the parallel run proves it before cutover, and the credits offset the effort. Leo's MSP and the other 17 MSP partners get bulk migration tooling for their tenants and a pre-brief two weeks before the public announcement, because each of them has dozens of customers to move.

**The API side.** Classic's webhooks and its v1 correlation API get a 12-month deprecation window, matching the MCP floor and the contract notice period. From the announcement, every response from a deprecated endpoint carries Deprecation and Sunset headers with a link to the migration guide. The account team receives a weekly list of customers still calling the v1 API, which turns a passive warning into a direct conversation.

**The model notice.** Midway through the program, the provider of the model behind Diagnose posts a deprecation notice with a 60-day retirement window. The model deprecation runbook starts the same day. The internal deadline is set 30 days before retirement. The applied AI engineers run the candidate models through the eval suite, including the regression set built after the hallucinated root cause that led a customer to roll back the wrong service. One candidate scores higher on acceptance but cites evidence less often, so it's rejected. The chosen replacement goes to a canary of design-partner accounts, then to everyone. Sam's AI Act documentation pack is updated before cutover, and EU customers get a short notice of the model change. Running two lifecycle programs at once, one you started and one imposed on you, is normal for an AI product in 2026. The runbook keeps the second from derailing the first.

**The decision log.** You record the sunset decision, the milestone dates, the reversal criterion and the model swap in the decision log, each with an owner and a review date. Gate R3 is on the calendar at month 12.

## Product 360 artifacts

```template id="30-lifecycle-stage-assessment" title="Lifecycle stage assessment"
# Lifecycle stage assessment · [Offering, module, API version or dependency] · [Date]

**Owner:** [PM]   **Evidence window:** [e.g., last four quarters]   **Next review:** [Date]

## Signals
| Signal | Value | Trend | Source |
|---|---|---|---|
| ARR or usage growth against the market | | | |
| Share of new bookings | | | |
| Net revenue retention and gross churn (customers whose main use is this offering) | | | |
| Active customers and usage trend | | | |
| Gross margin and cost to serve | | | |
| Support tickets per customer; on-call load | | | |
| Engineering share against revenue share | | | |
| Competitive parity (competitor bundles, general-purpose AI tools) | | | |
| Dependency risk (models, platforms, protocols with published end dates) | | | |
| Strategic fit (feeds or competes with the strategy) | | | |

## Assessment
- **Stage:** Introduction / Growth / Maturity / Decline
- **Confidence:** Low / Medium / High
- **The one signal that would change this call:**
- **Self-fulfilling risk:** what we'd stop doing if we call it this stage, and whether that would cause the decline

## Investment posture
Invest / Sustain / Harvest / Retire. Reason in two sentences:

## Portfolio view (one row per offering)
| Offering | Stage | Posture | Revenue share | Engineering share | Gap to resolve |
|---|---|---|---|---|---|
| | | | | | |

## Decision
Agreed by [name] on [date]. Next review: [date]. If the posture is Retire, open a sunset decision memo.
```

```template id="30-stage-gate-criteria" title="Stage-gate criteria"
# Stage-gate criteria · [Gate name] · [Product or portfolio]

**Gate type:** New segment / General availability / Price change / R1 Consider retirement / R2 Announce end-of-sale / R3 End support / R4 Decommission
**Gatekeepers:** [names and roles]   **Decision owner:** [name]

## Deliverables the team brings
1.
2.
3.

## Must-meet criteria (any "No" stops the gate)
| Criterion | Yes / No | Evidence |
|---|---|---|
| Strategic fit with the agreed strategy | | |
| Legal and contract review complete | | |
| Security and privacy review complete | | |
| No unmitigated customer harm (data loss, broken integrations, compliance gaps) | | |
| Funded owner for the next stage | | |

## Should-meet criteria (score 1 to 5)
| Criterion | Weight | Score | Evidence |
|---|---|---|---|
| Customer evidence | | | |
| Market attractiveness | | | |
| Competitive advantage | | | |
| Feasibility or migration readiness | | | |
| Financial return or savings | | | |
| Risk (lower risk scores higher) | | | |
| **Weighted total** | | | |

## Decision rules (agreed before the gate)
- Go if all must-meet criteria pass and the weighted total is at least [threshold].
- Recycle if [condition]. Hold if [condition]. Kill if [condition].

## Outcome
Decision: Go / Kill / Hold / Recycle. Approved plan and resources: [summary]. Next gate date: [date]. Recorded in the decision log on [date].
```

```template id="30-sunset-decision-memo" title="Sunset decision memo"
# Sunset decision memo · [Offering] · [Date]

**From:** [PM]   **To:** [Decision owner]   **Approvers:** [Engineering, finance, legal, sales, customer success]

## Recommendation
[One sentence: retire X, with end-of-sale on [date] and last date of support on [date], migrating customers to Y.]

## Why now
- Usage and revenue trend:
- Cost to serve and engineering share:
- Security or dependency risk:
- Strategic fit:
- Successor readiness:

## Who is affected
| Segment | Accounts | ARR | Top accounts | Partners involved |
|---|---|---|---|---|
| | | | | |

## Options considered
| Option | What it costs | What it frees | Customer impact | Verdict |
|---|---|---|---|---|
| Do nothing (keep as is) | | | | |
| Keep investing | | | | |
| Maintenance only | | | | |
| Sell, spin off or open-source | | | | |
| Migrate and retire | | | | |

## Financial impact (planning assumptions, to be confirmed by finance)
- ARR at risk (worst case):
- Expected migration rate and expected churn:
- Savings (engineering, infrastructure, support):
- One-time costs (credits, migration services, tooling):
- Questions for finance (revenue recognition, credits, deferred revenue):

## Contract and legal review
- Notice periods in customer and partner agreements:
- Committed terms that run past the proposed dates:
- Service-level commitments affected:
- Data return, retention and deletion obligations:
- Regulatory obligations:

## Migration path and incentives
[Successor, parity summary, tooling, credits or price protection]

## Communication summary
[Who hears first, public announcement date, channels]

## Milestones and gates
| Gate or milestone | Date | Owner |
|---|---|---|
| R1 Consider retirement | | |
| R2 Announce end-of-sale | | |
| R3 End support | | |
| R4 Decommission | | |

## Reversal criteria (written before announcement)
If [condition, e.g., less than x% of affected ARR has migrated by end of maintenance], we will [action, e.g., offer paid extended support to named accounts for up to n months].

## Decision
[Approved / Not approved / Revise], by [name] on [date].
```

```template id="30-end-of-life-plan" title="End-of-life plan with milestones"
# End-of-life plan · [Offering] · v[n] · [Date]

**Program owner:** [PM]   **Successor:** [Offering]   **Status:** Planning / Announced / In migration / Closed

## Milestones
| Milestone | Date | What stops | What continues | Owner |
|---|---|---|---|---|
| End-of-life announcement | | | | |
| End-of-sale (last order date) | | New orders | Renewals [yes/no] | |
| Last new subscription term or last ship date | | | | |
| End of software maintenance | | Features and bug fixes | Security fixes, support | |
| End of security fixes | | Vulnerability patches | Support | |
| Last date of support | | Support contracts | Documentation, data export | |
| Decommission and data deletion | | Service and stored data | Deletion evidence on request | |

## Workstreams
| Workstream | Owner | Key deliverables | Due |
|---|---|---|---|
| Migration tooling and parallel run | | | |
| Customer communication | | | |
| Partner program | | | |
| Contracts and legal | | | |
| Pricing, credits and extended support | | | |
| Support staffing | | | |
| Data return and deletion | | | |
| Internal enablement (sales, customer success, support) | | | |
| Price list, documentation and website removal | | | |

## Extended support (if offered)
Price: [ ]   Maximum duration: [ ]   Scope: [security fixes only / other]   Eligibility: [named accounts]

## Metrics (reviewed weekly)
- Share of affected ARR migrated; share of accounts migrated
- Accounts blocked, with reason
- Calls to deprecated APIs by customer
- Support tickets about the end-of-life
- Usage and satisfaction in recently migrated accounts

## Reversal criteria
[Copied from the sunset decision memo]
```

```template id="30-end-of-sale-notice" title="End-of-sale notice"
# End-of-sale and end-of-life notice · [Offering] · [Announcement date]

## Summary
On [date], [company] will stop selling [offering and editions or SKUs]. Support continues until [last date of support]. We recommend moving to [successor], which [one-sentence benefit]. This notice lists every date and what changes at each.

## Affected products
| Product or SKU | Replacement |
|---|---|
| | |

## Milestones
| Milestone | Date | What this means for you |
|---|---|---|
| End-of-sale | | No new orders. Existing subscriptions [can / cannot] renew until [date]. |
| End of software maintenance | | No new features or bug fixes. Security fixes continue. |
| End of security fixes | | No further vulnerability patches. |
| Last date of support | | Support ends. Data export remains available until [date]. |
| Service shutdown and data deletion | | The service stops and remaining data is deleted. |

## What you need to do, and by when
1. [Action] by [date]
2. [Action] by [date]

## Migration support
- Tooling: [import, parallel run]
- Help: [migration services, office hours, documentation]
- Commercial terms: [credits, price protection, extended support terms if any]

## Your data
[How to export it, how long it stays available, when and how it is deleted, how to request deletion evidence]

## For developers
Deprecated APIs and webhooks: [list]. Responses include Deprecation and Sunset headers from [date]. Migration guide: [location].

## Contacts and FAQ
Account team: [contact]   Support: [contact]   FAQ: [location]
```

```template id="30-migration-plan" title="Migration plan"
# Migration plan · [From offering] to [successor] · [Date]

**Owner:** [PM]   **Engineering lead:** [name]   **Customer success lead:** [name]

## Segments
| Segment | Accounts | ARR | Migration complexity (L/M/H) | Approach (self-serve / assisted / white-glove) | Wave |
|---|---|---|---|---|---|
| | | | | | |

## Feature parity map
| Old capability | New equivalent | Gap | Workaround or plan | Accounts relying on it |
|---|---|---|---|---|
| | | | | |

## Tooling
- Configuration or rule import:
- Data migration and export:
- Parallel run: [how long, what customers compare, how to revert]

## Success criteria per account
[e.g., parallel run complete, key metric within x% of old system, customer sign-off]

## Incentives
[Credits, price lock, free services, and their deadlines]

## Support staffing curve
| Period | Expected migrations | Support and services capacity needed |
|---|---|---|
| | | |

## Tracking
| Account | ARR | Wave | Status (not started / parallel run / migrated / blocked) | Blocker | Owner | Next step |
|---|---|---|---|---|---|---|
| | | | | | | |

## After migration
Check-ins at [30 and 60] days. Watch: [usage, satisfaction, key outcome metric].

## Escalation path
Blocker owner → [PM] → [decision owner], with a response time of [n] business days.
```

```template id="30-deprecation-communication-plan" title="Deprecation communication plan"
# Deprecation communication plan · [Offering, feature or API] · [Date]

**Owner:** [PM or PMM]   **Canonical page:** [location of the deprecation registry or lifecycle page]

## Audiences and channels
| Audience | What they need to know | Channel | Sender | First contact |
|---|---|---|---|---|
| Economic buyers | Dates, business impact, commercial terms | Account team call, email | Account executive | Pre-brief |
| Admins and champions | Dates, migration steps, tooling | Email, in-product banner, webinar | Product | Announcement |
| Developers | Deprecated endpoints, replacements, dates | Changelog, docs, Deprecation and Sunset headers, SDK warnings | Engineering | Announcement |
| Partners (resellers, MSPs) | All of the above, earlier, plus tenant tooling | Partner briefing, partner portal | Partner team | Pre-brief, before public notice |
| Internal (sales, customer success, support) | Talk track, FAQ, escalation path | Enablement session, internal page | PM and PMM | Before pre-briefs |

## Sequence
| When | Message | Audience |
|---|---|---|
| T minus [n] weeks | Internal enablement | Internal |
| T minus [n] weeks | Pre-brief | Top accounts and partners |
| T (announcement) | Public notice with every date and the successor | All |
| Fixed intervals (e.g., quarterly, then monthly) | Reminder with migration progress and next date | Accounts not yet migrated |
| [n] days before each milestone | Milestone warning | Affected accounts |
| Final warning | Last call with consequences | Accounts not yet migrated |
| After retirement | Confirmation and data deletion notice | All affected |

## Programmatic signals
- [ ] Deprecation and Sunset headers on deprecated endpoints
- [ ] Deprecated tags in schemas and SDKs, with runtime warnings
- [ ] Status field in the API or console
- [ ] Entry in the deprecation registry with earliest removal date

## Key messages (approved by legal)
1.
2.
3.

## Feedback loop
Customer replies and tickets summarized weekly by theme; owner: [name].
```

```template id="30-model-deprecation-runbook" title="Model deprecation runbook"
# Model deprecation runbook · [Product]

**Owner:** [PM]   **Applied AI lead:** [name]   **Last reviewed:** [Date]

## Standing preparation (before any notice)
- [ ] Model register: every model dependency by feature, provider, channel, region, version or alias, and customer tier
- [ ] Each provider's published lifecycle states, notice periods and "not sooner than" dates recorded
- [ ] Subscriptions to provider notices; status fields checked on a schedule
- [ ] Eval suite per feature, including regression sets from past incidents
- [ ] Model abstraction so a swap is a configuration change plus evals
- [ ] Decision per feature: pinned version or alias, and why

## When a notice arrives
| Step | Action | Owner | Done |
|---|---|---|---|
| 1 | Log the notice: model, channel, region, retirement date | | |
| 2 | Set the internal deadline at least [30] days before retirement | | |
| 3 | List affected features, customers and contracts (including AI risk documentation commitments) | | |
| 4 | Shortlist candidate replacements | | |
| 5 | Run the eval suite on representative data; compare quality, latency and cost together | | |
| 6 | Adjust prompts, tools and parameters for the chosen candidate | | |
| 7 | Shadow or canary with a limited set of accounts | | |
| 8 | Notify customers if behavior, data handling, region or price changes; update AI documentation | | |
| 9 | Cut over with a tested rollback path | | |
| 10 | Record results; update the model register and documentation | | |

## Candidate comparison
| Candidate | Quality (eval pass rate) | Regression set result | Latency | Cost per task | Data handling or region change | Decision |
|---|---|---|---|---|---|---|
| | | | | | | |

## Escalation
If no candidate meets the quality bar before the internal deadline: [options, e.g., degrade the feature gracefully, restrict it to supervised mode, request a provider extension where offered, notify customers].
```

## Prompts

```prompt title="Assess the lifecycle stage of an offering"
Goal: Get an evidence-backed stage call and investment posture for one offering or module.
Paste in (or connect the harness to): CRM bookings, billing and ARR by offering, product usage trends, support ticket volumes, engineering capacity by team, competitor notes and any dependency end dates. Use only tools approved for company financial and customer data.

Assess the lifecycle stage of [offering] using the evidence provided, over the window [window].

1. For each signal, give the value, the trend and the source: growth against the market, share of new bookings, net revenue retention and gross churn, usage trend, gross margin and cost to serve, support load, engineering share against revenue share, competitive parity, dependency risk and strategic fit.
2. Make a stage call (introduction, growth, maturity or decline) with a confidence level, and name the single signal that would most change it.
3. Recommend a posture (invest, sustain, harvest or retire) in two sentences.
4. Describe how the call could become self-fulfilling: what we'd stop doing if we accept it, and whether that would cause the outcome.

If a signal has no evidence, write "No evidence" rather than estimating it.

Check the output: open the sources for the two signals that drive the call and confirm the numbers. If the stage rests on one quarter of data, treat the confidence as low.
```

```prompt title="Build a portfolio lifecycle view"
Goal: See whether capacity across the portfolio matches each offering's stage.
Paste in: the stage assessments for each offering, revenue by offering and engineering capacity by team or offering.

Build a one-page portfolio lifecycle view for [portfolio].

1. Make a table: offering, stage, posture, share of revenue, share of engineering capacity, and the gap between the two.
2. Flag three patterns if present: everything in maturity (no next curve), everything in introduction (no cash engine), and decline-stage offerings holding more engineering share than revenue share.
3. Propose up to three capacity moves that would better match posture, and what each would cost.
4. List the questions I should ask each offering owner before the next business review.

Don't propose retiring anything without stating the customers and ARR affected.

Check the output: confirm the capacity shares with engineering leads. Allocation data is often stale, and a wrong share produces a wrong conclusion.
```

```prompt title="Draft a sunset decision memo"
Goal: Produce a first draft of the memo that asks to retire an offering.
Paste in: the stage assessment, account and ARR list for the offering, engineering cost estimates, successor readiness notes and any contract review notes. Customer and contract data is confidential: use an approved tool.

Draft a sunset decision memo recommending [retire / keep / maintain] for [offering], with these sections: recommendation in one sentence with dates; why now; who is affected (segments, ARR, top accounts, partners); options considered, including do nothing, keep investing, maintenance only, sell or open-source, and migrate and retire, each with cost, what it frees and customer impact; financial impact as planning assumptions; contract and legal review; migration path and incentives; communication summary; milestones and gates; reversal criteria; decision.

Rules:
- Use only numbers from the material provided. Mark any number you had to derive and show how.
- Write the reversal criteria as a measurable condition and a specific action.
- List open questions for finance and legal at the end rather than answering them.

Check the output: recompute ARR at risk from the account list yourself. Make sure the strongest argument against retiring appears in the options table, stated fairly.
```

```prompt title="Extract lifecycle terms from customer contracts"
Goal: Find every contractual constraint on an end-of-life before you set dates.
Paste in: the customer and partner agreements, order forms and amendments for accounts using [offering]. These are confidential: use only a tool your legal team has approved, and treat the output as a draft for legal review.

For each agreement, extract into a table: customer, agreement and section reference, notice period for material changes or discontinuation, committed term end date, service-level commitments that mention [offering], data return and deletion terms, termination rights triggered by discontinuation, and any partner or reseller obligations.

Then summarize: the longest notice period found, agreements whose committed terms run past [proposed last date of support], and any clause that's ambiguous.

Quote the clause text for every notice period and termination right. If a field isn't addressed in the agreement, write "Not addressed."

Check the output: legal reviews every row before any date is set. Spot-check three agreements against the original text, including the one with the longest notice period.
```

```prompt title="Write an end-of-sale notice and audience versions"
Goal: Turn the end-of-life plan into clear customer communications for each audience.
Paste in: the end-of-life plan with milestones, the migration plan summary, approved commercial terms and the deprecation communication plan.

Using only the dates and terms provided, draft:
1. A public end-of-sale notice with a summary, affected products, a milestone table showing what changes at each date, what customers need to do and by when, migration support, data handling, a developer section and contacts.
2. A pre-brief email for economic buyers at top accounts, focused on business impact and commercial terms.
3. A partner briefing for resellers and managed service providers, including tenant migration tooling and earlier timelines.
4. A one-paragraph in-product banner and a talk track for account teams.

Rules: name the successor and every date in the first paragraph of each piece. Use "deprecated," "end of support" and "retired" exactly as defined here: [definitions]. Don't promise anything not in the plan.

Check the output: compare every date and commitment against the plan, line by line. Read the notice as the customer with the hardest migration would; if it doesn't tell them what to do next, rewrite it.
```

```prompt title="Report migration progress and stalled accounts"
Goal: Keep a migration program on track with a weekly evidence-based report.
Paste in (or connect the harness to): account list with ARR, migration status from telemetry and CRM, calls to deprecated APIs by customer, support tickets about the end-of-life and customer replies to the notice.

Produce this week's migration report for [offering]:
1. Share of affected ARR and accounts migrated, against plan, with the trend over the last [n] weeks.
2. Accounts with no progress in [n] weeks, ranked by ARR, with the last recorded blocker and owner.
3. Customers still calling deprecated APIs, with call volume.
4. Themes in support tickets and customer replies, each with two example sources.
5. Usage and satisfaction in accounts migrated in the last 60 days, compared with before migration.
6. Whether we're on track against the reversal criteria: [criteria].

Cite the source for every number. Don't infer a blocker that isn't recorded.

Check the output: confirm the ARR-migrated figure with finance or CRM directly before it goes to leadership. Read the angry replies yourself instead of relying on the theme summary.
```

```prompt title="Evaluate a replacement for a deprecated model"
Goal: Choose a replacement model before the provider's retirement date, on your own evidence.
Paste in: the deprecation notice, the feature's model register entry, eval results for each candidate on your eval suite and regression sets, latency and cost measurements, and any data handling or region differences. Don't paste customer data unless the tool is approved for it.

Compare the candidate replacements for [feature], currently on [model], which retires on [date].

1. Build a table: candidate, eval pass rate, regression set results, latency, cost per task, data handling or region changes.
2. Identify where each candidate is better or worse than the current model, and which failures are new.
3. Recommend a candidate, or recommend that none is ready, with the reason.
4. List what customers must be told (behavior, data handling, region, price) and which AI documentation needs updating.
5. Propose a canary plan and the rollback trigger.

Use only the results provided. Don't rely on public benchmark scores.

Check the output: rerun the regression cases that failed for the recommended candidate and read the outputs yourself. Confirm the retirement date for your specific channel and region with the provider's own page.
```

## Anti-patterns

:::warn The curve as destiny
A product's growth flattens for two quarters, someone calls it "mature," investment is cut and growth falls further, which seems to confirm the call. Treat the stage as a hypothesis with a named signal that would change it, and ask whether the plateau has a fixable cause before you change posture.
:::

:::warn The product nobody retires
An offering with a tenth of the revenue holds a fifth of the engineering capacity and most of the on-call pages. Nobody owns its end of life, so it continues by default. Compare engineering share with revenue share every planning cycle, and give every declining offering a named owner and a posture.
:::

:::warn Deprecation by surprise
Customers find out about a removal from a broken integration or a changelog line. Publish your deprecation policy before you need it, name every date and the successor in the first message, send machine-readable signals and pre-brief partners and top accounts.
:::

:::warn Dates set before contracts are read
The end-of-sale notice goes out, and then legal finds agreements with longer notice periods or committed terms that run past the last date of support. Review contracts before gate R2, and set dates from the longest constraint you find.
:::

:::warn The endless extension
Every large customer who objects gets another six months, the sunset slips quarter after quarter and the freed team never appears. Write reversal criteria before the announcement, price extended support as a bridge and apply the criteria you wrote, not new ones.
:::

:::warn Treating model retirements as someone else's problem
A provider retires a model with 60 days' notice, and the team discovers it has no eval suite, no list of affected features and a contract promising customers notice of material changes. Keep a model register, set internal deadlines well ahead of provider dates and make a model swap a routine, tested change.
:::

## Checklist

- [ ] Every offering, module, public API version and model dependency is in a lifecycle inventory with an owner.
- [ ] Each offering has a current stage assessment with evidence, confidence and the signal that would change the call.
- [ ] Each offering has an agreed posture: invest, sustain, harvest or retire.
- [ ] A portfolio view shows revenue share against engineering share, and gaps are resolved or explained.
- [ ] Gates exist for irreversible moments, with must-meet and should-meet criteria and decision rules agreed in advance.
- [ ] A published deprecation policy ties notice length to each surface's stability label.
- [ ] Any retirement has a sunset decision memo with options, financial impact, contract review and reversal criteria.
- [ ] The end-of-life plan sets every milestone date, and legal and finance have signed off.
- [ ] The migration plan has a parity map, tooling, a parallel run, incentives and per-account tracking.
- [ ] The communication plan pre-briefs partners and top accounts and includes machine-readable signals.
- [ ] Migration is tracked weekly by ARR, and recently migrated accounts get check-ins.
- [ ] Data return and deletion are completed with evidence at decommission.
- [ ] A model register lists every model dependency by channel and region, with provider dates and an internal deadline policy.
- [ ] The model deprecation runbook has been rehearsed on at least one swap.

## Key takeaways

- The product life cycle is a useful vocabulary and a poor forecast. Assess the stage of each offering, module, API and model dependency separately, with evidence, and review the call every planning cycle.
- Set an investment posture per stage, and check the portfolio for balance. The most common failure is a declining product holding more engineering capacity than its revenue justifies.
- Use gates at moments of irreversible commitment, including the retirement milestones, and write the criteria and decision rules before the gate.
- Run an end-of-life as a program: a sunset decision memo with reversal criteria, dated milestones set after contracts are read, a migration plan with a parallel run, and communications that reach partners first.
- APIs carry explicit lifecycle promises. Tie notice length to the stability label, publish the policy early and send machine-readable deprecation signals.
- In AI products, models and parameters retire on providers' schedules, often with weeks or a few months of notice. A model register, an eval suite and a rehearsed runbook make a swap routine.
- Let the harness assemble evidence and draft documents, and verify every date, number and contractual commitment before it reaches a customer.
