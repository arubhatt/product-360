<p class="lead">A launch is the moment a product decision becomes a promise to customers, sellers, regulators and your own support team at the same time. This chapter shows you how to size each launch, get every function ready, make the go/no-go call on the record, write the announcement artifacts and measure whether the launch did what it was supposed to do, with extra care for AI features, whose behavior can change after launch day.</p>

## Why this matters

Many enterprise launches that go wrong were built well. The code worked. What failed was everything around it: sales promised a capability that shipped as a preview, billing couldn't meter the new price, support learned about the feature from a customer ticket, or legal found out after the press release that the beta terms let customers run it in production. Each of those is a readiness failure in a function the product team doesn't manage, and each lands on the PM.

The second failure is proportion. Some teams run every release through the same heavy process, so people learn to route around it. Others treat every release as a deploy, so the one that changes how customers buy gets a changelog entry and nothing else. Both skip the same decision: how big is this launch, and what does that size earn it?

The third failure is measurement. A launch that gets coverage, a packed keynote room and a trending post can still leave customers with nothing new to use. If the launch plan doesn't name adoption and pipeline targets before launch, the post-launch story defaults to reach, because reach is what's easy to count.

AI features add a fourth failure. A traditional feature behaves on day 90 the way it behaved on launch day. An AI feature can change when the model provider retires a model, when your team swaps a prompt or when infrastructure shifts underneath it. Each of those is a launch whether or not anyone calls it one.

The tools in this chapter answer those four failures: **launch tiers** that size a launch by impact, **release stages** with precise contractual meanings, a **readiness checklist and go/no-go review** across every function, the **announcement artifacts** that grow from the PR/FAQ, and **launch metrics and a post-launch review** that test the launch against predictions made before it happened.

These artifacts sit in the Go-to-market dimension of your Product 360 (Chapter 00). They're event artifacts: written for one launch, used intensely, then archived as the record of why the product reached customers the way it did. Positioning and messaging (Chapter 24) come before them; events and keynotes (Chapter 26) and enablement (Chapter 27) run alongside.

## What a launch is, and how big this one is

### Every externally visible change is a launch

Google's site reliability engineers use a broad definition. Rick Klau's chapter on reliable launches in Google's *Site Reliability Engineering* defines a launch as "any new code that introduces an externally visible change to an application." By that definition Google sometimes performs up to 70 launches a week. Reviewing every one in full doesn't scale, so Google's launch coordination engineers did two things: they built a standard checklist, and they classified launches by risk so that low-risk ones took a lighter path.

Most of your launches are small. The system needs a cheap default path for them and an expensive path for the few that change what customers buy, how they buy it or what they trust you with. If you can't name which path a release is on, you haven't finished planning it.

### Launch tiers

Product marketing teams commonly sort launches into three tiers. No single originator of the practice could be verified, so treat the matrix below as this book's synthesis of common practice. The criteria are about customer and business impact. Engineering effort is deliberately absent: a two-week change that introduces a new price is a bigger launch than a two-quarter re-platforming that customers never notice.

| | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| **Criteria (meets any two)** | New product, SKU or price; changes how buyers evaluate you; a material revenue or pipeline target; regulatory or trust exposure (AI autonomy, new data use) | Meaningful new capability for existing customers; changes an admin or user workflow; closes a competitive gap | Improvement, fix, minor UI change or integration update |
| **Announcement** | PR/FAQ lineage, press release, analyst briefings, flagship event moment, launch blog post, customer webinar | Blog post, in-app announcement, customer email to affected admins | Release notes and changelog only |
| **Readiness** | Full nine-function checklist; sales enablement and certification; pricing and packaging; transparency note for AI features | Checklist for affected functions; enablement brief for sales and support; customer FAQ | Docs updated; support macro if needed |
| **Rollout** | Design partners, early access, limited availability, then general availability | Opt-in or percentage rollout | Straight to general availability behind a flag |
| **Go/no-go decider** | VP or GM | PM lead | Engineering lead |
| **Post-launch review** | At 30 and 90 days | At 30 days | Only if a trigger fires |

Two rules keep the tiers honest. First, the PM proposes the tier in writing and the launch council (or whoever owns the calendar) confirms it, so tiering doesn't become a bid for marketing attention. Second, an AI feature moves up one tier when it changes what the system does on the customer's behalf. An AI summary that a person reads is a tier 2 or 3 change. An agent that takes an action in a customer's production environment is tier 1 even if the code change is small, because the trust exposure is new.

:::key Tier by impact, not effort
The tier decides what a launch gets: which artifacts, which functions sign off and who makes the call. Size it by what changes for customers and the business. A small change to price, data use or AI autonomy is a big launch.
:::

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 330" role="img" aria-label="Two axes of a launch: availability stages from design partners to general availability, and autonomy levels from shadow through assisted and supervised to allowlisted autonomy, with a rule that no account moves up the autonomy axis faster than its admin opts in">
  <line x1="90" y1="280" x2="650" y2="280" class="ln"/>
  <line x1="90" y1="280" x2="90" y2="30" class="ln"/>
  <text x="370" y="318" text-anchor="middle" class="s">Availability: who can use it, on what terms →</text>
  <text x="28" y="160" text-anchor="middle" class="s" transform="rotate(-90 28 160)">Autonomy: what it may do on its own →</text>
  <rect x="100" y="240" width="125" height="30" rx="6" class="box"/>
  <text x="162" y="260" text-anchor="middle" class="s">Design partners</text>
  <rect x="235" y="240" width="125" height="30" rx="6" class="box"/>
  <text x="297" y="260" text-anchor="middle" class="s">Early access</text>
  <rect x="370" y="240" width="125" height="30" rx="6" class="box"/>
  <text x="432" y="260" text-anchor="middle" class="s">Limited availability</text>
  <rect x="505" y="240" width="135" height="30" rx="6" class="box"/>
  <text x="572" y="260" text-anchor="middle" class="s">General availability</text>
  <rect x="100" y="196" width="170" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="110" y="216" class="s">Shadow: runs, users don't see it</text>
  <rect x="100" y="156" width="170" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="110" y="176" class="s">Assisted: suggests, never acts</text>
  <rect x="100" y="116" width="200" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="110" y="136" class="s">Supervised: acts after approval</text>
  <rect x="100" y="76" width="230" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="110" y="96" class="s">Autonomous: allowlisted, low-risk only</text>
  <path d="M 162 238 L 297 186 L 432 146 L 572 106" fill="none" stroke="var(--a1)" stroke-width="2.5"/>
  <circle cx="162" cy="238" r="5" fill="var(--a1)"/>
  <circle cx="297" cy="186" r="5" fill="var(--a1)"/>
  <circle cx="432" cy="146" r="5" fill="var(--a1)"/>
  <circle cx="572" cy="106" r="5" fill="var(--a1)"/>
  <text x="640" y="40" text-anchor="end" class="t" style="fill:var(--a2)">Each account climbs only</text>
  <text x="640" y="58" text-anchor="end" class="t" style="fill:var(--a2)">as fast as its admin opts in</text>
</svg>
<figcaption>An AI launch moves on two axes. Availability stages say who can use the feature and on what terms; autonomy levels (from Chapter 31) say what it may do without a person. The line shows a typical path, where most accounts sit at each stage. The launch plan sets a ceiling for each stage, and each customer's admin decides where their account sits below it.</figcaption>
</figure>

## Release stages: design partners to general availability

### What the labels mean

"Beta" means something different in every company, and customers read it through the meaning their last vendor gave it. Pick a vocabulary, publish it and use it the same way every time. Two public definitions are clean enough to borrow.

GitHub uses three stages. A **private preview** is under heavy development, its scope may still change, it may be undocumented and it carries no service level agreement (SLA) or technical support. A **public preview** is ready for broader distribution and documented, but still has no SLA or support. **General availability** (GA) means fully tested, open to all users, production-ready and backed by SLA and support obligations.

GitLab adds the stage most companies leave vague. Its four stages are experiment, beta, limited availability and generally available. **Limited availability** (LA) is public but offered on some platforms only or at reduced scale. It's fully supported and documented, ready for production at that reduced scale, and held to the same security requirements as GA, including a security release process, audit logging and runbooks, though without an explicit SLA. GitLab also notes that an LA feature may start free and become paid later.

GitLab's definition is the one to borrow: LA is supported production use with a deliberately limited scope. That makes it the right stage for a feature that works but whose operations, pricing or platform coverage aren't ready for every customer.

Map your program names onto these stages so nobody has to guess:

| Program | Stage | Who gets in | Terms |
|---|---|---|---|
| **Design partners** | Private preview | A handful of named accounts, chosen for fit and candor | NDA; no SLA; frequent sessions with the product trio; no production use unless agreed in writing |
| **Early access program (EAP)** | Private or public preview | Accounts whose admin opts in | Preview terms; no SLA; best-effort support; clear "early access" label in the product |
| **Limited availability** | LA | Customers on supported platforms or under a scale limit | Supported and documented; production-ready at stated scope; security bar of GA |
| **General availability** | GA | All eligible customers | SLA, full support, list price, all documented platforms |

### The label is a contract

Preview terms carry legal consequences, which is why legal sits on the readiness checklist. The AWS Service Terms for betas and previews say SLAs don't apply, features and terms may change at any time, the beta's existence and the customer's feedback are AWS confidential information, access can be suspended at any time and ends automatically at GA, and content created in the beta may not carry over. Microsoft's supplemental terms for Azure previews describe early access previews as for internal testing and feedback only, with no production use and no processing of personal data, and they let Microsoft store and process data from generative AI previews to monitor for abuse.

Read the terms as promises about what the customer can do with your feature: run it in production or not, have their data handled differently or not, keep their work at GA or not. When a seller calls something "basically GA" to close a deal, they're quietly rewriting those promises. The stage label in your launch plan has to match the terms the customer signs, and your customer FAQ has to say what changes at each transition, especially price.

### Separate deploy from release

Release stages work because deploying and releasing are different events (Chapter 06 covers the mechanics). Of Pete Hodgson's four kinds of feature toggle, two matter most in a launch plan: **permissioning toggles**, which give a feature to specific customers such as early access accounts, and **ops toggles**, which act as long-lived kill switches. The same build passes through private preview, EAP, LA and GA by changing who the permissioning toggle includes.

Danilo Sato adds a distinction worth keeping. A **canary release** exposes a new version to a small subset first to reduce risk; an A/B test checks a hypothesis over days. They share plumbing, and Sato advises against conflating them. A launch plan that says "we'll A/B test the rollout" usually means a canary, and its success metrics get muddled.

### Early access for B2B AI is a governance decision

For AI features, who opts in matters as much as when. Microsoft's Frontier program for Microsoft 365 Copilot gives organizations early access to preview AI features and agents, but for business users the organization must opt in, and IT admins turn it on, manage which features and agents are available and assign eligible users. That pattern fits any B2B agent: the customer's admin, not the individual user, decides whether the organization takes on preview risk, and controls which agents and actions are available to whom.

:::onramp If you've never run an early access program
Treat an EAP as a research program with a contract attached. Write down what you need to learn, how many accounts you need, how long it runs and what happens at the end: graduate, extend or stop. Recruit fewer accounts than you think you can support, each with a named contact who'll talk to you every two weeks.
:::

## Launch readiness across functions

### The checklist

Google's launch coordination engineers audit launches against a checklist covering architecture and dependencies, integration, capacity planning, failure modes, client behavior, processes and automation, the development process, external dependencies and rollout planning. One capacity question is worth quoting in spirit: is the launch tied to a press release or promotion? Klau's chapter describes one launch that drew about 25 times normal peak traffic. A press release is a capacity input as well as a marketing artifact, so the marketing plan belongs in front of the engineering team.

Google's categories cover engineering. An enterprise launch needs the same discipline across every function that makes a promise on launch day. Each row in the readiness checklist has an owner, a definition of ready, a link to evidence and a status: green (ready), amber (at risk, with a plan) or red (not ready).

| Function | Ready means | Evidence |
|---|---|---|
| **Product** | Scope frozen for this stage; success metrics and baselines set; tier and stage confirmed; customer FAQ approved | Launch plan, metric definitions |
| **Engineering** | Rollout plan with flags, stages and kill switch; capacity tested against the marketing plan; failure modes and rollback rehearsed | Release plan (Chapter 06), load test results |
| **Documentation** | Docs for every supported platform and connector at this stage; release notes drafted; known limitations stated | Docs links, release notes |
| **Support** | Runbooks, macros and escalation path; staff trained; ticket tagging in place so launch tickets can be counted | Runbook, training record |
| **Sales** | Enablement complete; talk track says what's GA and what isn't; pricing and quoting work in the sales tools | Enablement completion, quote test |
| **Legal** | Preview or GA terms match the stage label; AI disclosure reviewed; claims in the announcement substantiated | Signed-off terms and claims review |
| **Billing** | New SKUs and meters live; a test invoice is correct; dispute path defined | Test invoice |
| **Security** | Security review passed; audit logging and access controls verified; customer-facing security documentation ready | Review record, security docs |
| **Marketing** | Announcement artifacts approved; timeline and channels set; spokespeople briefed; reference customers confirmed | Final drafts, approvals |

The checklist's value comes from making each owner say "ready" in writing, against a definition agreed weeks earlier.

### The go/no-go review

Spaceflight gives the go/no-go meeting its clearest model. In a NASA launch status check (often called a go/no-go poll), each flight-control position reports whether its systems are ready. On Space Shuttle missions the test director polled about ten positions and reported to the launch director, who polled five more and declared the mission go. Two features of that design transfer directly: every function answers for its own domain, on the record, and one named person makes the call.

In software it's a short meeting held a set number of days before the date that can't move. Each function owner reads their status. Any red is a no-go unless the decider records an explicit risk acceptance that says what the risk is, who owns it and when it'll be resolved. The outcome is one of three, written into the decision log:

- **Go**: everything is green or amber with a plan.
- **Go with conditions**: the launch proceeds at a reduced stage or scope, with named conditions and dates (for example, announce and open early access, but hold GA until billing passes a test invoice).
- **No-go**: the launch moves, with a new date and the evidence needed to reach go.

Hold the review early enough that "go with conditions" is still a real option.

## The announcement artifacts

### From PR/FAQ to launch day

Amazon's Working Backwards process, described by Colin Bryar and Bill Carr, asks a team to write the press release before building anything. The **PR/FAQ** is a press release of a few paragraphs, always under one page, plus up to five pages of frequently asked questions that cover the customer's questions and a realistic view of cost and difficulty. It's revised many times and reviewed with senior leaders, and most PR/FAQs never become products, which the authors treat as the process working.

Bryar and Carr's template gives the press release a fixed order: a heading with the product name and a one-line descriptor; a subheading naming the customer and benefit; a summary with the realistic launch date; the problem from the customer's view; the solution and why it beats current alternatives; a spokesperson quote and a customer quote; and how to get started. The FAQ splits in two. The external FAQ answers customers and press (price, how it works, support, where to buy). The internal FAQ answers leaders, finance, operations and legal (alternatives and competitors, market size, unit economics and investment, third-party dependencies, regulatory issues and the top reasons the product could fail).

Chapter 02 uses the PR/FAQ as a vision artifact and Chapter 04 contrasts it with the PRD. At launch, the PR/FAQ forks into the real announcement artifacts:

| Artifact | Audience | Grows from | Tier |
|---|---|---|---|
| **Press release** | Press, analysts, investors | PR/FAQ press release, rewritten to what actually shipped | 1 |
| **Launch blog post** | Customers and prospects | PR/FAQ problem and solution sections, plus a worked example | 1, 2 |
| **Customer FAQ** | Customers, their admins and security reviewers | External FAQ | 1, 2 |
| **Internal FAQ** | Sales, support, leadership | Internal FAQ, plus "what not to promise" | 1, 2 |
| **Release notes** | Admins and users | The change itself | All |
| **Transparency note** | Security, compliance and risk reviewers | AI addendum to the PRD (Chapter 31) | 1 for AI |

The most useful exercise before launch is a **gap analysis**: put the inception PR/FAQ next to the launch-day press release and explain every difference. Scope shrinks, quotes change, prices move and dates slip. Each difference is either a lesson about your estimates or a promise someone in the field may still be making.

### Release notes

Release notes are the whole announcement for tier 3 and part of every tier. Olivier Lacan's Keep a Changelog principles apply: release notes are for people, not machines; there's an entry per version, dated, with the latest first; and changes are grouped by type: Added, Changed, Deprecated, Removed, Fixed and Security. For AI features this book adds a seventh group, **Model and behavior changes**, covering the model version, eval results that moved and known regressions. That heading is this book's extension, not part of Lacan's format.

### The communications timeline

The weeks below are a typical shape for a tier 1 enterprise launch tied to an event. Adjust them to your sales cycle and event calendar.

| When | What happens |
|---|---|
| **T minus 12 weeks** | Tier confirmed; launch plan drafted; PR/FAQ refreshed; stage plan and success metrics agreed |
| **T minus 8 weeks** | Readiness checklist opened with owners; reference customers asked; analyst briefing dates set; pricing approved (Chapter 15) |
| **T minus 6 weeks** | Sales and support enablement begins (Chapter 27); customer FAQ and internal FAQ drafted; transparency note drafted for AI features |
| **T minus 4 weeks** | Press release, blog post and release notes drafted; legal claims review; load test against the marketing plan |
| **T minus 2 weeks** | Go/no-go review; analyst and press briefings under embargo; enablement certification closes |
| **T minus 1 week** | Final artifacts locked; support staffing confirmed; rollback rehearsed |
| **T (launch day)** | Announcement; flags flipped for the stage; launch channel staffed; first-day metrics read |
| **T plus 1 week** | First adoption and support readout; fixes to docs and FAQs |
| **T plus 30 and 90 days** | Post-launch reviews against the launch plan's predictions |

Sequence the internal audiences ahead of the external ones. Support and sales should never learn about a launch from a customer.

## Measuring launch success

Decide what success means before launch, in the launch plan, with a baseline for each metric. Otherwise the review measures whatever looks good. This book's position, consistent with Chapters 02 and 05, splits launch metrics into four groups:

- **Leading indicators (days to weeks).** Activation of the new capability by target accounts, early access to paid conversion, support tickets per active account, enablement completion and early task-success signals for the feature itself.
- **Lagging indicators (one to two quarters).** Pipeline influenced by the launch and win rate in deals where the capability was shown, expansion revenue, retention of adopting accounts and movement in the product's North Star.
- **Guardrails (watched throughout).** The things the launch must not damage: support load on existing customers, reliability and cost to serve. For AI features add the error signals your evals track, such as wrong or reverted actions. A launch that hits its adoption target while breaching a guardrail hasn't succeeded.
- **Reach (reported, never the goal).** Press coverage, event attendance, blog traffic and social mentions. Reach tells you whether people heard. It can't tell you whether anyone changed what they do.

:::leader For product leaders
Ask every tier 1 launch plan for its predicted numbers before you approve the date, and ask the 90-day review to show the prediction next to the actual. Teams that know the comparison is coming set honest targets. Teams that don't will report reach.
:::

## The post-launch review

John Lunney and Sue Lueder's account of Google's postmortem culture describes a written record of impact, mitigation, root causes and follow-up actions, triggered by criteria set in advance, written blamelessly, reviewed by senior engineers, then shared and stored so the organization learns. The post-launch review applies the same shape to launches, including the ones that went well.

Set the triggers in the launch plan: every tier 1 launch at 30 and 90 days, every tier 2 launch at 30 days, and any launch where the go/no-go was conditional or a rollback happened. The review answers four questions. What did we predict? What happened? Why did it differ? What do we change, in the product and in how we launch? Blamelessness matters for the same reason it matters in incidents: if the review hunts for who missed a date, the next launch plan will hide its risks.

The most valuable output is often a change to the launch process itself: a new checklist row, a different tier criterion or an earlier go/no-go. If a review produces no changes, check whether it asked why the numbers differed or only reported them.

## How to apply it

Here's the method for a tier 1 launch, counted back from a fixed date. For tier 2, compress it to six weeks and drop the steps marked tier 1 only. For tier 3, steps 1 and 9 are enough.

**Twelve weeks out: size and frame it.**

1. **Propose the tier in writing.** Score the launch against the tier criteria and get the launch council to confirm it. If it's an AI feature that acts on the customer's behalf, start at tier 1.
2. **Write the launch plan.** Goal, audience, positioning (from Chapter 24), the stage plan, success metrics with baselines, the communications timeline, owners and the date the go/no-go will be held. Add a stage plan for autonomy if the feature is AI-powered.
3. **Refresh the PR/FAQ.** Bring the inception PR/FAQ up to date with what's actually shipping and run the gap analysis. Every difference becomes a line in the internal FAQ.

**Eight to six weeks out: line up the functions.**

4. **Open the readiness checklist.** Name an owner per function and agree each definition of ready now, while it's still cheap to change. Link it from the launch plan.
5. **Design the early access program.** Decide entry criteria, the number of accounts, what you need to learn, the exit criteria to the next stage, and the terms. Have legal confirm the stage label matches the terms customers will sign.
6. **Start enablement.** Sales and support need the talk track, the internal FAQ and the "what we don't say" list before anyone briefs a customer (Chapter 27).

**Four to two weeks out: write and decide.**

7. **Draft the announcement artifacts.** Press release, blog post, customer FAQ, internal FAQ, release notes and, for AI features, the transparency note. Have legal review every claim against evidence.
8. **Run the go/no-go review.** Each owner reads their status. Record go, go with conditions or no-go, with any risk acceptance and its owner. Tell the field the result the same day.

**Launch and after: measure against the prediction.**

9. **Ship by stage.** Flip permissioning toggles for the stage, staff the launch channel, and read leading indicators daily for the first week and weekly after that.
10. **Fix the artifacts in week one.** The questions customers actually ask in the first week will differ from the ones you predicted. Update the customer FAQ, docs and support macros.
11. **Hold the post-launch reviews.** At 30 and 90 days, compare predicted with actual, blamelessly. Record what changes in the product and in the launch process.
12. **Move stages on evidence.** Promote from early access to LA to GA when the exit criteria are met, not when the calendar says so. Each promotion is a smaller launch with its own release notes and customer communication.

Salesforce's Agentforce launch shows the announce-then-stage pattern in public. The September 2024 announcement named a general availability date about six weeks out, stated pricing of $2 per conversation, said some components would follow in February 2025 and quoted a piloting customer. Agentforce was announced as generally available in late October. You can announce at the flagship moment and keep stages honest, as long as the announcement says plainly what's available today, what's coming and when.

## The AI lens

### Launching AI-powered products

AI features change launch management in five ways.

**Staged autonomy runs alongside staged availability.** Chapter 31 describes the autonomy ladder: shadow mode, assisted, supervised and autonomous for allowlisted actions, with a kill switch. Availability and autonomy are separate axes, and a feature can be GA for suggestions while in early access for actions. Write the autonomy ceiling for each stage, let each customer's admin choose a level at or below it, and move between levels on eval and production evidence, not on the launch calendar.

**Model changes are launches.** If your product runs on a foundation model, your launch calendar inherits your provider's. Anthropic's documentation describes a model lifecycle of active, legacy, deprecated and retired, and commits to notifying customers with active deployments at least 60 days before retiring a publicly released model, by email and in its documentation. When an upstream model retires you have to swap it, and the swap can change how your feature writes, reasons and fails. Give every model change a tier (usually tier 2), run your evals before and after, publish the results under "Model and behavior changes" in the release notes and tell customers before the change, not after.

Users get attached to how a model behaves as well as what it can do. When OpenAI launched GPT-5 in August 2025, older models were removed from ChatGPT for many users, some users objected, and within days OpenAI restored the previous model as an option. Stripe's approach to API versioning is the enterprise discipline to borrow: Brandur Leach describes how Stripe pins each account to the API version current at its first request and, as of 2017, had kept compatibility with every version since 2011, treating the API as a long-term contract. For an AI platform, the equivalent is a pinning window: let customers stay on the previous model for a stated period while they test the new one, when the economics allow it.

**Quality can regress without any launch at all.** In September 2025 Anthropic published a postmortem of three infrastructure bugs that had degraded some Claude responses over several weeks. None was a model change. Detection was slow because standard evals didn't catch the problems, privacy controls limited engineers' access to user interactions not submitted as feedback, and symptoms differed by platform, so reports looked inconsistent. Anthropic committed to more sensitive evals, continuous quality evals on production systems and faster ways to debug community feedback. Pre-launch evals aren't enough. Name the production quality evals that run after launch, and read support tickets and community channels in the post-launch review, because customers often notice drift before dashboards do.

**Behavior is a go/no-go criterion.** In April 2025 OpenAI rolled back a GPT-4o update after users reported overly flattering, agreeable behavior. Behavior like that is hard to capture in a metric and easy for a person using the product to spot. Give a qualitative reviewer, someone who has used the feature on real tasks, a formal line in the go/no-go with the same standing as engineering and security. If that person says the behavior is off, that's a red even when the eval dashboard is green.

**AI disclosure is a readiness row.** Disclosure rules now come from several jurisdictions. Article 50 of the EU AI Act applies from 2 August 2026. It requires that people interacting directly with an AI system are told so unless that's obvious from context, that synthetic text, audio, image and video outputs are marked in a machine-readable way (with exceptions for systems that only assist editing), and that the information is clear and given at the latest at first interaction. In the United States, a 2025 special session of the Colorado legislature delayed the duties in Colorado's AI Act to 30 June 2026; check its current status with counsel, because state AI laws are still moving. Chapter 33 covers what these laws require. For the launch, the point is ownership: AI disclosure is a checklist row owned jointly by product and legal, and the customer FAQ states what the product marks as AI-generated and where.

For tier 1 AI launches, add a **transparency note** to the artifact set. Microsoft's transparency note for Azure OpenAI explains how the system works, its capabilities, intended uses, limitations, performance and the choices deployers make that affect behavior, and it treats the system as technology plus people plus deployment environment. That's the document a buyer's security and compliance reviewer asks for. Having it ready on launch day means the first deals don't wait while you write it.

### Doing launch work with AI

A launch is a coordination problem across many documents. An AI harness with connectors to your tracker, docs, CRM and support system handles much of the mechanics.

- **Readiness status.** Ask the harness to read the checklist and its evidence links and draft each row's status with what's missing. It'll catch the "green" row whose evidence link points at an empty page. The owner still states the status in the go/no-go.
- **Artifact drafting and consistency.** Draft the FAQs and release notes from the PRD, the PR/FAQ and the merged changes, then ask the harness to check every artifact for contradictions in stage labels, dates, prices and claims. Cross-document checks like this are slow for people and quick for a model.
- **Claims review.** Have the harness list every factual claim in the press release and blog post with the evidence behind it, and flag claims without evidence. Legal still decides, but they start from a list.
- **Launch-day listening.** Summarize support tickets, community threads and sales call notes daily in the first week, clustered by issue and linked to sources. For AI features, ask specifically for complaints about behavior.
- **Post-launch review assembly.** Pull the predicted metrics from the launch plan, the actuals from the analytics reports (Chapter 18) and the decision log, and draft the comparison. The "why it differed" section is yours.

Three rules apply. A person approves everything external; the harness never publishes or sends. Use only tools approved for confidential and customer data, because launch materials are often under embargo and support tickets contain customer information. And every status, claim and finding the harness drafts links to its source.

:::ai The one-line rule
Use AI to keep a launch's many documents consistent and its readiness evidence honest. Keep the go/no-go call, the claims and every external word with people.
:::

## The Beacon case: launching Beacon Agents at Northlight Live

:::example Where Beacon starts
Beacon Agents (supervised remediation) is due at Northlight Live, Northlight's annual customer event. Chapter 06's forecast showed the general availability date was uncertain, so the team cut scope to a rollback slice and agreed that Northlight Live would announce an opt-in early access program, with GA given as a range. Your Product 360 inventory (Chapter 00) noted that Beacon had no launch tiering at all. Now you have to run the launch.
:::

**The tier.** Beacon Agents meets three tier 1 criteria: new trust exposure (an agent that acts in customers' production environments), a new price (the move toward per-resolved-incident pricing) and a pipeline target tied to Northlight's flagship event. The VP of Product is the go/no-go decider. In the same quarter, multi-tenant views for MSPs like Leo's are confirmed as a separate tier 2 launch, so they don't ride on the tier 1 announcement.

**The stage plan.** Availability follows Chapter 06's release plan: dogfooding on Northlight Observe's own on-call rotation, five design partners under NDA (private preview), the opt-in beta that Chapter 06 planned, run as an early access program announced at Northlight Live (preview terms, no SLA), limited availability on Northlight Observe and the most-used cloud connectors, then GA by region with the EU last, because the AI Act documentation must be complete first. Autonomy has its own ceilings: design partners start in shadow mode and move to supervised rollbacks; early access is supervised only, approving each step; allowlisted autonomy for low-risk actions opens at LA, for accounts whose admin opts in. Sam, the security reviewer persona, gets the control Microsoft's Frontier program gives IT admins: early access is enabled per tenant by the customer's admin, and each action type is allowlisted separately.

**The go/no-go.** Held ten days before Northlight Live, so a conditional go is still possible. The readiness table:

| Function | Status | Note |
|---|---|---|
| Product | Green | Scope frozen; success metrics and baselines set |
| Engineering | Green | Kill switch rehearsed; load test sized to the keynote demo and announcement traffic |
| Docs | Amber | Docs for two connectors incomplete; those connectors excluded from early access |
| Support | Amber | Runbook for "the agent took a wrong action" drafted, not rehearsed; rehearsal set for T minus 5 days |
| Sales | Green | Enablement complete; talk track says "early access," not "available" |
| Legal | Green | Preview terms match the label; AI disclosure reviewed |
| Billing | Red | The "resolved incident" meter disagrees with the incident record in test accounts |
| Security | Green | Audit logs and scoped credentials verified |
| Marketing | Green | Press release, blog post and FAQs approved |
| Behavior review | Green | Two design-partner SREs reviewed a week of proposed actions |

The billing red decides the shape of the launch. If the meter can't agree with the customer's own record of what was resolved, per-resolved-incident pricing will produce invoice disputes, and the pricing is already a strategic bet (Chapter 03 lists the pricing pilot as Next, not Now). The VP records **go with conditions**: announce Beacon Agents and open early access on current platform pricing; announce the per-resolved-incident pricing pilot as a later, dated step with no price in the press release; rehearse the support runbook before the event; and hold LA until billing passes a test invoice against design partner data.

**The artifacts.** The gap analysis against the inception PR/FAQ (Chapters 02 and 04) shows three differences. The headline still centers on Dana opening an incident that's already diagnosed, with a proposed rollback waiting for approval. But the inception draft assumed GA at Northlight Live, several runbook actions and a per-incident price; the launch release says early access, rollback first and pricing to come. Each difference goes into the internal FAQ with its reason, so sellers who saw the old vision deck know what changed.

The customer FAQ answers what Marcus, Priya and Sam will ask, from price at each stage to which actions can ever run without approval, how to switch it off, what data the agent reads and what Beacon labels as AI-generated in incident updates. The answer to "what happens if the agent is wrong?" is specific because the team learned it the hard way: in Chapter 05, a customer rolled back the wrong service after accepting a confident, wrong root cause. The FAQ explains the controls added since: every rollback needs approval during early access, every action is logged, and the eval set now includes that failure mode. The internal FAQ carries what customers won't see: gross margin has fallen from 81% to 72% since agentic features launched, because of inference cost; the cost per resolved incident behind the pricing pilot; likely competitive responses; and what sales must not promise, starting with autonomous remediation in early access and any EU date. A Beacon Agents transparency note goes to every early access admin with the welcome email.

**The metrics.** The launch plan sets leading indicators for early access accounts: diagnosis acceptance with no reversion (the measure Chapter 05 adopted after the incident), the approved-action rate, early access to paid conversion at LA, and support tickets per active account. Lagging indicators: the autonomous resolution rate after LA, the North Star (incidents resolved with Beacon's help per week), pipeline influenced by Northlight Live and net revenue retention among adopting accounts, against today's 118%. Press coverage and keynote attendance are reported as reach.

**The 30-day review.** Early access enrollment beats the target, but approved-action rates vary widely by account. Accounts whose admin started with rollbacks for one service approve far more often than accounts that enabled everything at once, so allowlist templates join the LA exit criteria. The conditional go is judged justified: billing passed its test invoice in week three.

**The first model change.** Two months after LA, Beacon's model provider announces a retirement with 60 days' notice. The team runs the swap as a tier 2 launch: evals on the new model against the diagnosis and action sets, results under "Model and behavior changes" in the release notes, a notice to admins three weeks ahead and, for accounts that ask, a 30-day window on the previous model (a period the team chose for its own costs). Diagnosis acceptance is read before and after the switch.

## Product 360 artifacts

```template id="25-launch-tier-matrix" title="Launch tier matrix"
# Launch tier matrix · [Product or portfolio] · v[n] · [Date]

**Owner:** [Launch council chair or product ops lead]   **Review:** every half year

## Tier criteria (a launch meets a tier when it meets any two of its criteria)
| | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| New product, SKU or price | | | |
| Changes how buyers evaluate us | | | |
| Revenue or pipeline target attached | | | |
| Regulatory or trust exposure (AI autonomy, new data use) | | | |
| New capability for existing customers | | | |
| Changes an admin or user workflow | | | |
| Improvement, fix or minor change | | | |

AI rule: an AI feature that acts on the customer's behalf moves up one tier.

## What each tier gets
| | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Announcement artifacts | Press release, blog post, customer FAQ, internal FAQ, release notes, transparency note (AI) | Blog post, customer FAQ, internal FAQ, release notes | Release notes |
| Readiness | All nine functions | Affected functions | Docs and support |
| Rollout | Design partners, early access, LA, GA | Opt-in or percentage | Flag to GA |
| Enablement | Certification | Brief | None |
| Go/no-go decider | [VP or GM] | [PM lead] | [Engineering lead] |
| Post-launch review | 30 and 90 days | 30 days | On trigger |

## Stage definitions we use
| Stage | Access | Support | SLA | Production use | Price |
|---|---|---|---|---|---|
| Design partners (private preview) | Named accounts under NDA | Direct with product team | None | [Agreed in writing / no] | [Free / discounted] |
| Early access (preview) | Admin opt-in | Best effort | None | [No / at own risk] | [ ] |
| Limited availability | [Platforms, regions or scale limit] | Full | [None stated / ] | Yes, within scope | [ ] |
| General availability | All eligible customers | Full | [SLA] | Yes | List |

## Tier decisions this quarter
| Launch | Proposed tier | Criteria met | Confirmed by | Date |
|---|---|---|---|---|
| | | | | |
```

```template id="25-launch-plan" title="Launch plan"
# Launch plan · [Launch name] · Tier [1/2/3] · [Date]

**Owner:** [PM]   **Go/no-go decider:** [Name]   **Launch date or range:** [ ]   **Go/no-go review date:** [ ]
**Links:** PR/FAQ · PRD · release plan (Chapter 06) · positioning (Chapter 24) · readiness checklist

## Goal
What changes for which customers, and the business outcome we expect: [one paragraph].

## Audience
Target segments and personas: [ ]. Who is excluded at this stage and why: [ ].

## Stage plan
| Stage | Entry criteria | Who | Autonomy ceiling (AI) | Exit criteria | Target date |
|---|---|---|---|---|---|
| Design partners | | | | | |
| Early access | | | | | |
| Limited availability | | | | | |
| General availability | | | | | |

Flags: release toggle [name], permissioning toggle [name], kill switch (ops toggle) [name], owner [name].

## Success metrics (set before launch)
| Type | Metric | Baseline | Target | When read | Source report |
|---|---|---|---|---|---|
| Leading | | | | | |
| Lagging | | | | | |
| Guardrail | | | | | |
| Reach (reported only) | | | | | |

## Communications timeline
| When | Audience | Artifact or channel | Owner | Status |
|---|---|---|---|---|
| T minus [n] weeks | Internal: sales, support | | | |
| T minus [n] weeks | Analysts, press (embargo) | | | |
| T | Customers, public | | | |
| T plus 1 week | Customers | FAQ and docs updates | | |

## AI-specific (AI features only)
- Model and version at launch: [ ]. Upstream retirement date if known: [ ].
- Production quality evals running after launch: [ ].
- Behavior reviewer for the go/no-go: [name].
- AI disclosure: what is labeled AI-generated, where: [ ].

## Post-launch review triggers
[Every tier 1 at 30 and 90 days; any conditional go; any rollback; any trigger metric crossing [threshold].]

## Risks and open questions
| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| | | | | |
```

```template id="25-readiness-checklist" title="Launch readiness checklist"
# Launch readiness checklist · [Launch name] · Stage: [ ] · [Date]

Status: Green = ready · Amber = at risk, with a plan and date · Red = not ready
Definitions of ready are agreed by [date], before work is graded against them.

| Function | Owner | Ready means | Evidence link | Status | Note |
|---|---|---|---|---|---|
| Product | | Scope frozen for this stage; metrics and baselines set; customer FAQ approved | | | |
| Engineering | | Rollout plan, flags and kill switch; capacity tested against the marketing plan; rollback rehearsed | | | |
| Documentation | | Docs for every supported platform at this stage; release notes drafted; limitations stated | | | |
| Support | | Runbooks and macros; staff trained; launch ticket tag live; escalation path | | | |
| Sales | | Enablement complete; talk track states the stage; quoting works | | | |
| Legal | | Terms match the stage label; claims substantiated; AI disclosure reviewed | | | |
| Billing | | SKUs and meters live; test invoice correct; dispute path defined | | | |
| Security | | Review passed; audit logging and access controls verified; security docs ready | | | |
| Marketing | | Artifacts approved; channels and timeline set; spokespeople and references confirmed | | | |
| Behavior review (AI) | | Named reviewer has used the feature on real tasks and signs off on behavior | | | |

## Capacity inputs from marketing
Announcement channels and expected traffic: [ ]. Event demo load: [ ]. Confirmed with engineering on [date].
```

```template id="25-go-no-go-review" title="Go/no-go review record"
# Go/no-go review · [Launch name] · [Date] · T minus [n] days

**Decider:** [Name]   **Attendees:** [one owner per function]   **Readiness checklist:** [link]

## Status poll (each owner states their own)
| Function | Owner | Status | Open items |
|---|---|---|---|
| | | | |

## Reds and ambers
| Item | Risk if we launch anyway | Options | Owner |
|---|---|---|---|
| | | | |

## Decision
[ ] Go   [ ] Go with conditions   [ ] No-go

**Conditions (if any):**
1. [Condition] · Owner: [ ] · Due: [ ] · What happens if it is missed: [ ]

**Risk acceptances (any red launched over):**
- [Risk] accepted by [decider], owned by [name], resolved by [date].

**If no-go:** new date [ ], evidence needed to reach go [ ].

## Communicated
Field and support told on [date] by [name]. Decision log entry: [link].
```

```template id="25-eap-program-plan" title="Design partner and early access program plan"
# Early access program plan · [Feature] · [Date]

**Owner:** [PM]   **Stage:** Design partners (private preview) / Early access (preview)   **Runs:** [start] to [end]

## What we need to learn
1. [Learning goal, written as a question with a measurable answer]
2.
3.

## Who gets in
- Number of accounts: [n] (no more than we can talk to every two weeks)
- Entry criteria: [fit, environment, willingness to give feedback, named contact]
- Who opts in: [customer admin role]. What the admin controls: [features, agents, actions, users]
- Exclusions: [regions, regulated segments, platforms not yet supported]

## Terms (confirmed by legal)
- Production use: [allowed / not allowed / allowed with conditions]
- SLA and support: [ ]
- Confidentiality: [ ]
- Data handling, including any AI monitoring or retention: [ ]
- Price during the program and at graduation: [ ]
- What happens to the customer's work and configuration at the next stage: [ ]

## Cadence
Feedback sessions: [every two weeks]. Usage review: [weekly]. Program channel: [ ].

## Exit criteria to the next stage
| Criterion | Threshold | Current | Met? |
|---|---|---|---|
| | | | |

## Graduation communication
What each account is told, by whom and when, at graduation or at the end of the program: [ ].
```

```template id="25-announcement-pack" title="Announcement pack: press release, blog post and release notes"
# Announcement pack · [Launch name] · [Date]

## Press release (under one page)
**Heading:** [Product name]: [one-line descriptor]
**Subheading:** [Customer segment] can now [benefit].
**Summary:** [City], [date]. [What is available today, at which stage, and what comes later, with dates or ranges.]
**Problem:** [The customer's problem in their terms.]
**Solution:** [How it solves the problem and why it beats current alternatives, including doing nothing.]
**Spokesperson quote:** [ ]
**Customer quote:** [Real, approved, from a named design partner or early access customer.]
**Getting started:** [How to join, what it costs, where to learn more.]

## Launch blog post
- Title: [the customer outcome]
- Opening: a specific situation the reader recognizes
- What's new, at what stage, for whom
- A worked example with a real (approved) or clearly illustrative scenario
- What's next, without dates the plan doesn't support
- How to get access

## Release notes entry
### [Version or date]
- **Added:**
- **Changed:**
- **Deprecated:**
- **Removed:**
- **Fixed:**
- **Security:**
- **Model and behavior changes (AI):** model and version; eval results that moved; known regressions

## PR/FAQ gap analysis
| Inception PR/FAQ said | Launch release says | Why it changed | Who must know |
|---|---|---|---|
| | | | |

## Claims register
| Claim | Evidence | Reviewed by legal |
|---|---|---|
| | | |
```

```template id="25-launch-faqs" title="Customer FAQ and internal FAQ"
# FAQs · [Launch name] · [Date]

## Customer FAQ (customers, admins, security reviewers)
1. What is available today, and at what stage?
2. What does it cost now, and what changes at [next stage]?
3. Who can turn it on, and how do I turn it off?
4. What data does it read, where is it processed and is it used for training?
5. What does it do without a person's approval, and who decides? (AI)
6. What happens if it gets something wrong? (AI)
7. What is labeled as AI-generated, and where? (AI)
8. What changes when the model changes, and how will we be told? (AI)
9. What support and SLA apply at this stage?
10. Where are the security documentation and transparency note?

## Internal FAQ (sales, support, leadership)
1. What changed between the inception PR/FAQ and launch, and why?
2. What can we say, and what must we not promise? (List.)
3. How does this compare with current alternatives and competitors?
4. What are the unit economics, including cost to serve and margin effect?
5. Which third parties does it depend on, including model providers and their retirement dates?
6. What regulatory or legal issues apply, and what has legal approved?
7. What are the top reasons this launch could fail, and what are we watching?
8. How do I get a customer into early access, and who approves it?
9. Who do I escalate to for a wrong action, a pricing dispute or a security question?
```

```template id="25-post-launch-review" title="Post-launch review"
# Post-launch review · [Launch name] · [30 / 90] days · [Date]

**Owner:** [PM]   **Reviewed by:** [senior reviewer]   **Blameless:** we review systems and decisions, not people.

## Prediction against actual
| Metric | Type | Baseline | Predicted | Actual | Read |
|---|---|---|---|---|---|
| | Leading | | | | Above / on / below |
| | Lagging | | | | |
| | Guardrail | | | | |
| | Reach | | | | Reported only |

## What happened
Timeline of the launch and any incidents, rollbacks or stage changes: [ ].

## Why it differed
[Causes, with evidence. Include customer and support signals, not only dashboards.]

## Was the go/no-go right?
Conditions set: [ ]. Were they met on time? Was any risk acceptance justified?

## AI behavior (AI features only)
Production quality eval trend; behavior complaints from support and community; any model or infrastructure change since launch.

## Changes
| Change | In the product or the launch process? | Owner | Due |
|---|---|---|---|
| | | | |

## Stage decision
[Promote / hold / roll back], decided by [name] on [date]. Shared with [ ] and stored in [ ].
```

## Prompts

```prompt title="Propose a launch tier"
Goal: Get a tier recommendation you can defend to the launch council.
Paste in: the PRD or one-pager, the tier matrix your company uses and any pricing or packaging change attached to the launch.

Act as a launch council member reviewing this launch for [product].

1. Score it against each tier criterion in the matrix. Quote the line in the PRD that supports each criterion you mark as met.
2. Recommend a tier. If the launch includes an AI feature that acts on the customer's behalf, apply the rule that moves it up one tier and say so.
3. List what that tier requires (artifacts, functions, rollout stages, decider, review dates) and which of those the PRD doesn't yet plan for.
4. Name the strongest argument for one tier higher and one tier lower.

Base the tier on customer and business impact, not on engineering effort. Don't invent criteria the matrix doesn't contain.

[PRD]
[tier matrix]

Check the output: confirm every "criterion met" has a quote behind it. If the tier rests on a criterion you can't evidence, the council will ask the same question.
```

```prompt title="Draft readiness status from linked evidence"
Goal: Find the readiness rows that look green but aren't, before the go/no-go.
Paste in (or connect the harness to): the readiness checklist with its evidence links, the linked tickets and documents, and the launch plan. Use only tools approved for internal and confidential material.

For each row of this readiness checklist for [launch]:
1. Open the evidence link and say whether it shows the definition of ready is met, partly met or not met. Quote the evidence.
2. Propose a status (green, amber, red) and list what's missing.
3. Flag any row whose evidence link is empty, stale (older than [n] days) or points at something unrelated.
4. Flag dependencies between rows (for example, docs that depend on an unfinished engineering decision).

Don't mark anything green without evidence. These are proposals; each owner states their own status in the review.

Check the output: open the evidence for every row the model proposes as green and every row it flags. Send each owner the proposals that differ from their own status before the meeting, not in it.
```

```prompt title="Make the launch artifacts agree"
Goal: Catch contradictions across the press release, blog post, FAQs and release notes before customers do.
Paste in: all draft announcement artifacts, the launch plan (stage plan, dates, pricing) and the stage definitions your company uses.

Compare these launch artifacts for [launch] against the launch plan.

1. Build a table of every statement about stage, availability, dates, price, supported platforms, autonomy and data use, with the artifact and line it appears in.
2. Flag every contradiction between artifacts, and every statement that contradicts the launch plan or uses a stage label differently from our definitions.
3. Flag any wording that implies general availability, an SLA or production readiness for something at a preview stage.
4. List every factual claim (numbers, customer results, comparisons) with the evidence I've supplied for it, and mark claims with no evidence.

Don't rewrite the artifacts. Report only.

[artifacts]
[launch plan]

Check the output: verify each flagged contradiction yourself. Send the unsupported-claims list to legal as a starting point, not as their review.
```

```prompt title="Write a customer FAQ for an AI launch"
Goal: Answer the questions security reviewers and admins will ask, before they ask them.
Paste in: the PRD and AI addendum, the stage plan, the preview or GA terms, the security documentation and any questions already raised by design partners. Remove customer identifiers first.

Draft a customer FAQ for [feature] at the [stage] stage. Write for three readers: the admin who turns it on, the security reviewer who approves it and the user who relies on it.

Cover: what's available now and what's coming; price now and at the next stage; who can turn it on and off; what data it reads, where it's processed and whether it's used for training; what it does without approval and who decides; what happens when it's wrong; what's labeled as AI-generated; how model changes are communicated; support and SLA at this stage.

Rules:
- Answer only from the material provided. Where it doesn't answer a question, write "[Open: needs answer from owner]".
- Match the stage terms exactly. Never imply production readiness or an SLA the terms don't give.
- Plain language. No marketing adjectives.

Check the output: have legal and security read the data, terms and disclosure answers. Make sure every "[Open]" has an owner before the go/no-go.
```

```prompt title="Plan communications for a model change"
Goal: Treat a model swap as a launch, with evidence and notice.
Paste in: the provider's deprecation or retirement notice, eval results on the current and replacement models, the list of affected features and customers (counts only), and any contractual notice terms.

Our product [name] must move from [current model] to [replacement] by [date].

1. Propose a launch tier for the change and justify it.
2. Summarize the eval results as a "Model and behavior changes" release notes entry: what improved, what regressed and what we're doing about regressions.
3. Draft a notice to customer admins: what changes, when, what they should test, whether they can stay on the current model for a period and how to report problems.
4. Propose the metrics to read before and after the switch, and the threshold that would trigger a rollback or a pause.
5. Build a timeline from today to the retirement date, leaving time for customers to test.

Don't describe any improvement the eval results don't show.

Check the output: compare every claim in the release notes and notice with the eval results. Confirm the timeline leaves customers enough time before the provider's retirement date.
```

```prompt title="Summarize launch-week signals"
Goal: Hear what customers are saying in the first week, with evidence.
Paste in (or connect the harness to): support tickets with the launch tag, community and forum threads, sales call notes and in-product feedback for [date range]. Use an approved tool for customer data.

Summarize the first week of feedback on [launch].

1. Cluster the issues and questions. For each cluster give the count, two representative quotes with source links and the personas affected.
2. Separate confusion (docs or FAQ gaps), defects, pricing or packaging questions and, for AI features, complaints about behavior (tone, accuracy, overconfidence, wrong actions).
3. List questions customers asked that the customer FAQ doesn't answer.
4. Flag any signal that might mean a quality regression, even if only a few customers raised it.

Don't merge clusters to make the picture tidier. Single-source issues stay visible.

Check the output: read the source for each behavior complaint and possible regression yourself. Update the FAQ and docs the same day.
```

```prompt title="Draft the post-launch review"
Goal: Compare what you predicted with what happened, blamelessly.
Paste in: the launch plan (metrics, baselines and predictions), the go/no-go record, the analytics report for the period, the launch-week signal summaries and the decision log entries.

Draft a [30 or 90]-day post-launch review for [launch].

1. Fill a prediction-against-actual table for every metric in the launch plan, with the source for each actual.
2. Describe what happened as a timeline, including stage changes, incidents and rollbacks.
3. List possible reasons each metric differed from prediction, labeled "evidence" or "hypothesis."
4. Assess whether each go/no-go condition was met on time.
5. Propose changes, sorted into product changes and launch-process changes.

Blameless: describe systems and decisions, never individuals. Don't fill a metric you have no data for; write "No data."

Check the output: you write the "why it differed" conclusions. Check that reach metrics haven't been presented as success.
```

## Anti-patterns

:::warn The press-release launch
The launch is judged by coverage and keynote applause, and nobody set adoption or pipeline targets. Ninety days later the feature has a handful of active accounts and the launch is still described as a success. Put leading and lagging metrics with baselines in the launch plan, and report reach separately.
:::

:::warn One process for every launch
Every release goes through the same heavy review, so teams skip the process or bundle changes to avoid it. Or the reverse: everything ships as a deploy, and the release that changes price gets a changelog line. Tier launches by impact and give each tier a proportionate path.
:::

:::warn "Basically GA"
A seller tells a customer the preview is production-ready to close a deal. The customer runs it in production under terms that give no SLA and no guarantee their work survives GA. Publish stage definitions, put the stage in the sales talk track and have legal match the label to the terms.
:::

:::warn The go/no-go that can only say go
The review happens the night before the keynote, so "go with conditions" and "no-go" aren't real options and every amber turns green in the room. Hold it early enough to cut scope, and make each owner state their own status on the record.
:::

:::warn The silent model swap
The team moves to a new model version because the old one is being retired, and calls it maintenance. Diagnosis wording changes, acceptance drops and customers notice first. Treat every model change as a launch, with evals before and after, release notes and advance notice.
:::

:::warn Support learns from the customer
The announcement goes out at 9 a.m. and support gets the runbook at noon. The first tickets get "we're looking into it." Sequence internal audiences first: enablement and support readiness are checklist rows with owners.
:::

## Checklist

- [ ] The launch has a tier, proposed in writing against the tier criteria and confirmed by the launch council.
- [ ] Stage labels (design partners, early access, limited availability, general availability) are defined, published and matched to the terms customers sign.
- [ ] The launch plan names the stage plan, flags, kill switch owner, success metrics with baselines and the communications timeline.
- [ ] For AI features, the launch plan sets an autonomy ceiling per stage, and each customer's admin opts in at or below it.
- [ ] The readiness checklist covers product, engineering, docs, support, sales, legal, billing, security and marketing, each with an owner, a definition of ready and evidence.
- [ ] Marketing's announcement plan has been given to engineering as a capacity input.
- [ ] The go/no-go is held early enough to allow a conditional go, and the decision, conditions and risk acceptances are in the decision log.
- [ ] For AI features, a named behavior reviewer has a formal line in the go/no-go.
- [ ] The PR/FAQ gap analysis is done, and every difference is explained in the internal FAQ.
- [ ] The press release, blog post, customer FAQ, internal FAQ and release notes agree on stage, dates, price and claims, and legal has reviewed the claims.
- [ ] AI disclosure is reviewed by product and legal, and the customer FAQ says what is labeled as AI-generated.
- [ ] Tier 1 AI launches ship a transparency note.
- [ ] Production quality evals keep running after launch, and model changes are treated as launches.
- [ ] Post-launch reviews are scheduled, compare predicted with actual, and produce changes to the product and the launch process.

## Key takeaways

- Size every launch by customer and business impact, not engineering effort. The tier decides the artifacts, the functions that sign off and who makes the call, and AI features that act on a customer's behalf move up a tier.
- Stage labels are contracts. Define design partners, early access, limited availability and general availability precisely, and make sure the terms, the talk track and the FAQ all say the same thing.
- Readiness is cross-functional. Every function answers for its own domain in writing, and one named decider makes the go/no-go call early enough that a conditional go is still possible.
- The PR/FAQ written before the build is the seed of the launch artifacts. Compare it with what actually shipped and explain every difference to the field.
- Measure launches by adoption, pipeline and the North Star against predictions made before launch. Report press and attendance as reach.
- For AI features, run availability and autonomy as separate stages, treat every model change as a launch, keep quality evals running in production and give behavior a formal vote in the go/no-go.
