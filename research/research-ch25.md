# Research notes: Chapter 25, Launch Management (Part VI)

Working notes for the chapter author. Not chapter prose. Tags: [V] verified on the primary source in this session; [S] secondary only; [U] unverified, from prior knowledge, check before print.

Session note: the web search budget for this workflow run was exhausted before this chapter began, so every source below was reached by fetching a known primary URL directly. Coverage is narrower than a search-led pass would give, and several items are flagged for later checking.

## Raw source log (appended as fetched)

### Google SRE book, ch. 27 "Reliable Product Launches at Scale" (Rick Klau, edited by others; O'Reilly 2016, free at sre.google) [V]
URL: https://sre.google/sre-book/reliable-product-launches/ (fetched 2026-10-30)
- Launch definition: any new code that introduces an externally visible change to an application.
- Launch Coordination Engineering (LCE): a consulting SRE team that audits launches, coordinates teams, signs off on launches judged safe, and teaches practice.
- Launch checklist categories: architecture and dependencies; integration; capacity planning (is the launch tied to a press release or promotion? expected traffic?); failure modes; client behavior; processes and automation; development process; external dependencies; rollout planning.
- Techniques: gradual and staged rollouts (canary machines, then a datacenter, then global, auto rollback on failed validation); feature flags (typically 1 to 10 percent of users first, revertible independently); load testing for overload behavior.
- Numbers: Google sometimes performs up to 70 launches per week; one launch saw about 25 times normal peak traffic (NORAD Tracks Santa on Keyhole); by 2008 about 30 percent of reviews were classed as low risk.
- Use: the engineering half of the readiness checklist, and evidence that "press release" is a capacity input, not only a marketing artifact. Also: launch reviews scaled by classifying low-risk launches, which is the logic behind tiers.

### Bryar, C. and Carr, B. Working Backwards (St. Martin's Press, 2021), excerpt on aboutamazon.com [V]
URL: https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes (fetched 2026-10-30)
- PR/FAQ = press release plus frequently asked questions; written before building to test whether the idea is worth pursuing.
- Press release: a few paragraphs, always under one page, summarizing the customer experience. FAQ: up to five pages, covering customer questions and a realistic view of cost and difficulty.
- Revised many times and reviewed with senior leaders; most PR/FAQs never become products, and the authors treat that as intended.
- Use: the PR/FAQ is a pre-build artifact. At launch it is the seed for the real press release, blog post and customer FAQ. A good chapter move: compare the Beacon Agents PR/FAQ written a year earlier with the launch-day press release.

### Microsoft Azure, Supplemental Terms of Use for Microsoft Azure Previews (last updated June 2026) [V]
URL: https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/
- Previews are optional pre-release features, services, software or regions ("preview, beta, or other pre-release").
- "Early Access Previews" label covers frontier, early access, private preview, research or experimental offerings: internal testing and feedback only, no production use, no sharing with third parties, confidentiality under NDA, and no Personal Data processing.
- Generative AI previews: not for production; Microsoft may store and process customer data and outputs to monitor for abuse.
- Use: shows that the preview label carries contractual consequences (data, confidentiality, production use). The PM's stage label is a legal commitment, which is why legal sits on the readiness checklist.

### AWS Service Terms, Section 2 "Betas and Previews" [V]
URL: https://aws.amazon.com/service-terms/ (fetched 2026-10-30)
- Covers anything labeled beta, preview, pre-release or experimental, plus beta regions.
- SLAs do not apply; features and terms may change at any time; information about the beta, including its existence and the customer's feedback, is AWS Confidential Information.
- AWS may suspend or end access at any time; access ends automatically at GA; beta content may not carry over to the GA version.
- Provided "as is"; liability capped at what the customer paid for the beta in the prior 12 months.

### GitHub Docs, "GitHub's release cycle" (on the feature preview page) [V]
URL: https://docs.github.com/en/get-started/using-github/exploring-early-access-releases-with-feature-preview
- Private preview: under heavy development, scope changing, may be undocumented, no SLAs or technical support ("Technology Preview" counts here).
- Public preview: ready for broader distribution, documented, can be public or private, no SLAs or technical support.
- General availability: fully tested, open to all users, production-ready, with SLA and technical support obligations.
- Use: the cleanest three-stage public definition. Recommend the chapter adopt this vocabulary (private preview, public preview, GA) and map "design partner", "EAP" and "limited availability" onto it.

### Google Cloud launch stages [U]
- Tried cloud.google.com/terms/launch-stages and cloud.google.com/products/product-launch-stages; neither returned the definitions. Do not cite Google Cloud stage definitions without checking.

### Working Backwards PR/FAQ template (workingbackwards.com, Bryar and Carr's site, no date) [V]
URL: https://workingbackwards.com/resources/working-backwards-pr-faq/
- Press release parts, in order: heading (product name plus one-sentence descriptor); subheading (one sentence naming the customer segment and benefit); summary (city, outlet, realistic launch date, overview); problem (from the customer's view, big enough to matter); solution (how it solves the core problem, why it beats current alternatives); quotes (one from a company spokesperson, one from a hypothetical customer); getting started and call to action.
- External FAQ (customers and press): price, how it works, how to get support, where to buy.
- Internal FAQ (leaders, finance, marketing, operations, legal): current alternatives and competitors, market size, unit economics and upfront investment, time to profitability, third-party dependencies, regulatory and legal issues, top reasons the product could fail.
- Use: gives the exact skeleton for three of the chapter's artifacts (press release, customer FAQ, internal FAQ). Teach the PM to keep the PR/FAQ alive from inception to launch, then fork it.

### GitLab Docs, "Support for Experiment, Beta, and Generally Available features" [V]
URL: https://docs.gitlab.com/policy/development_stages_support/ (fetched 2026-10-30)
Four stages, a rare public definition that includes limited availability:
| | Experiment | Beta | Limited availability | Generally available |
|---|---|---|---|---|
| Access | explicit opt-in, off by default | explicit opt-in, off by default | public, but some platforms only or reduced scale | public on all offerings |
| Support | none | commercially reasonable effort | fully supported and documented | fully supported and documented |
| SLA | none | none | no explicit SLA, but same security bar as GA | vulnerability remediation SLOs apply |
| Production | not ready | might not be ready | ready at reduced scale | ready at any scale |
| Notes | may be removed at any time; data-loss risk | breaking changes possible with less notice | needs security release process, audit logging, runbooks; may start free and become paid | completed security review, audit logging |
- Use: the best anchor for the chapter's "LA versus GA" definitions. Key teaching point: LA is supported production use at reduced scale or reduced platform coverage, not a polite name for beta. Pricing may switch on later, which must be in the customer FAQ from day one.

### Anthropic, "Model deprecations" (Claude Platform docs, fetched 2026-10-30) [V]
URL: https://platform.claude.com/docs/en/about-claude/model-deprecations
- Lifecycle vocabulary: Active (fully supported, recommended); Legacy (no more updates, may be deprecated); Deprecated (still works, not recommended, replacement named, retirement date assigned); Retired (requests fail).
- Notice: customers with active deployments are notified, at least 60 days before retirement for publicly released models; notified by email and in documentation.
- Advice to customers: test applications on newer models well before the retirement date; audit usage to find deprecated-model calls.
- Example from the page: Claude Sonnet 4.5 deprecated 2026-09-30, retirement 2026-11-30, replacement claude-sonnet-5-5. Partner platforms (Amazon Bedrock, Google-managed) set their own schedules.
- Use: Beacon runs on third-party foundation models, so Beacon's own launch calendar inherits upstream deprecation dates. A model swap inside Beacon Agents is itself a launch that needs a tier, evals, and customer communication. The four-stage vocabulary is a good template for Beacon's own "model change notice".

### Anthropic, "Commitments on model deprecation and preservation" (2025-11-04) [V]
URL: https://www.anthropic.com/research/deprecation-commitments
- Commits to preserve weights of all publicly released models for at least the company's lifetime; a post-deployment report on deprecation; "model interviews" before retirement, piloted with Claude Sonnet 3.6.
- Page does not state a customer notice period (that lives in the docs page above).
- Use: optional sidebar only. Shows that model retirement is now treated as a public commitment, not a silent infrastructure change.

### EU AI Act, Article 50 "Transparency obligations" (via artificialintelligenceact.eu, fetched 2026-10-30) [S, legal text mirror]
URL: https://artificialintelligenceact.eu/article/50/
- 50(1): providers must design systems that interact directly with people so those people are informed they are dealing with AI, unless obvious to a reasonably well-informed, observant person from context.
- 50(2): providers of systems generating synthetic audio, image, video or text must mark outputs in a machine-readable, detectable way; not required for systems that only assist standard editing or do not substantially alter input.
- 50(4): deployers must disclose deepfakes; and AI-generated text published to inform the public on matters of public interest, unless it underwent human review with editorial responsibility.
- 50(5): information must be clear and distinguishable, given at the latest at the first interaction or exposure, and accessible.
- Page states application from 2 August 2026. Chapter 31 research records an Omnibus grace period to 2026-12-02 for 50(2) for systems already on the market before 2026-08-02 [S, see research-ch31.md].
- Use: AI disclosure is a launch-readiness line item owned jointly by product and legal. For Beacon (B2B, users are on-call engineers), 50(1) is likely satisfied by context, but agent-written incident updates posted to customers' status pages or chat channels may need labeling. The customer FAQ should state what Beacon marks as AI-generated and where.

### Danilo Sato, "CanaryRelease" (martinfowler.com, 2014-06-25) [V]
URL: https://martinfowler.com/bliki/CanaryRelease.html
- Canary release: expose a new version to a small subset of users first; select users at random, internal staff first, or by profile, region or brand; on trouble, route traffic back to the old version.
- Sato separates canaries (risk reduction, short) from A/B tests (hypothesis testing, days): the two share plumbing but should not be conflated.

### Pete Hodgson, "Feature Toggles (aka Feature Flags)" (martinfowler.com, 2016, revised 2017-10-09) [V]
URL: https://martinfowler.com/articles/feature-toggles.html
- Four toggle types: release toggles (latent code, short-lived); experiment toggles (cohorts for A/B tests); ops toggles (degrade under load, long-lived kill switches); permissioning toggles (premium or beta users, can last years).
- Toggle debt: add a removal task when creating a release toggle; set expiry dates; "time bombs"; cap the toggle count.
- Use: separates deploy from release, which is what lets a PM run EAP, LA and GA on the same code. For Beacon Agents the autonomy level per action is effectively a permissioning toggle, and the kill switch is an ops toggle. Launch plan should name both.

### Salesforce Agentforce launch sequence (Salesforce newsroom) [V]
URLs: https://www.salesforce.com/news/press-releases/2024/09/12/agentforce-announcement/ (2024-09-12); https://www.salesforce.com/news/press-releases/2024/10/29/agentforce-general-availability-announcement/ (2024-10-29)
- 2024-09-12 announcement: Agentforce for Service and Sales "will be generally available on October 25, 2024"; some Atlas Reasoning Engine components due February 2025; pricing starts at $2 per conversation with volume discounts. One customer (Wiley) described as piloting, quoted as reporting more than 40 percent increase in case resolution (customer claim, not independently verified).
- 2024-10-29 release: Agentforce Service Agent and Agent Builder described as generally available; $2 per conversation.
- Use: a real B2B agent launch pattern: announce at a flagship moment with a named GA date about six weeks out, pilot customer proof in the release, price in the announcement, and some components explicitly later. Mirrors Beacon Agents at Northlight Live. Keep the example to these facts; do not add adoption numbers.
- Flag: the fetch of the 10-29 page reported GA as 10-29 while the 09-12 page promised 10-25. Cite "announced September 2024, generally available late October 2024" unless re-checked.

### Olivier Lacan, Keep a Changelog 1.1.0 [V]
URL: https://keepachangelog.com/en/1.1.0/
- Principles: changelogs are for people, not machines; an entry per version; latest first; dated; group by type; linkable.
- Six change types: Added, Changed, Deprecated, Removed, Fixed, Security.
- Use: release-notes format for the chapter. For AI features, propose adding a seventh heading for Beacon: "Model and behavior changes" (model version, eval deltas, known regressions). Mark that as the book's own extension, not Lacan's.

### Anthropic Engineering, "A postmortem of three recent issues" (2025-09-17) [V]
URL: https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues
- Three infrastructure bugs between August and September 2025 degraded some Claude responses: a context-window routing error (peaking at 16 percent of Sonnet 4 requests on 2025-08-31 after a load-balancing change on 2025-08-29); output corruption from a TPU server misconfiguration (2025-08-25 to 2025-09-02); and a compiler miscompilation affecting token selection (2025-08-25 to 2025-09-12).
- Why detection was slow: standard evals did not catch it (the model often recovers from isolated mistakes); privacy controls limit access to user interactions not submitted as feedback; symptoms differed by platform, so reports looked inconsistent.
- Commitments: more sensitive evals; continuous quality evals on production systems; faster privacy-preserving debugging of community feedback; keep relying on user feedback channels.
- Stated: Anthropic never reduces model quality because of demand, time of day or server load.
- Use: the strongest public example of model-quality communication after a silent change. Teaching points for Beacon: (1) an AI feature can regress without any model change, through infrastructure; (2) the launch plan needs production quality evals, not only pre-launch evals; (3) customers notice quality drift before dashboards do, so the post-launch review must read support and community signals.

### Lunney, J. and Lueder, S. "Postmortem Culture: Learning from Failure," Google SRE book ch. 15 (2016) [V]
URL: https://sre.google/sre-book/postmortem-culture/
- Postmortem: written record of impact, mitigation, root causes and follow-up actions.
- Triggers defined in advance: user-visible degradation over a threshold, data loss, on-call intervention such as rollback, resolution time over a threshold, monitoring failure.
- Blameless: focus on systemic contributors, assume good intent and reasonable information.
- Reviewed by senior engineers, then shared widely and stored in a repository; regular review sessions so none go unreviewed.
- Use: the post-launch review borrows this shape. Define post-launch review triggers in the launch plan, before launch (for example, "any tier 1 launch, and any launch where the go/no-go was conditional").

### Microsoft, "Transparency Note for Azure OpenAI" (Microsoft Learn, ms.date 2026-09-21) [V]
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/transparency-note
- A Transparency Note explains how an AI system works, its capabilities and limits, and the choices system owners make that affect behavior; it treats the system as technology plus people plus deployment environment.
- Audience: system owners, developers and deployers, and also end users and affected people.
- Headings: what a transparency note is; basics and key terms; capabilities; use cases (intended uses, considerations when choosing a use case); limitations; system performance and best practices; evaluating and integrating for your use.
- Use: a ready-made shape for an AI launch artifact that B2B buyers' security and compliance reviewers (Sam in the Beacon case) ask for. Recommend Beacon ship a "Beacon Agents transparency note" as a tier 1 launch artifact alongside the customer FAQ.

### Wikipedia, "Launch status check" [S]
URL: https://en.wikipedia.org/wiki/Launch_status_check
- Also called a "go/no go poll": at the start of a US spaceflight mission, each flight-control position reports whether its systems are ready. On Shuttle missions the NASA Test Director polled about ten positions and reported to the Launch Director, who polled five more and declared the mission go for launch.
- Use: origin story for the go/no-go meeting. The design lesson that transfers: every function answers for its own domain, on the record, and one named person makes the call. Avoid claims about when the practice began (the article does not say).

### Brandur Leach, "APIs as infrastructure: future-proofing Stripe with versioning" (Stripe blog, 2017-08-05) [V]
URL: https://stripe.com/blog/api-versioning
- Date-named rolling API versions; each account is pinned to the latest version on its first request; breaking changes are wrapped in version-change modules that transform responses back for older versions; the changelog is generated from those modules.
- Stripe had kept compatibility with every API version since 2011 (as of 2017) and treats the API as a long-term contract.
- Use: for platform launches, "launch" includes not breaking the people already built on you. Beacon's connector and MCP surfaces need the same discipline. Model changes are the AI-era equivalent of a breaking change, and pinning (letting a customer stay on a model version for a period) is an option to put in the launch plan.

### Wikipedia, "GPT-5" (fetched 2026-10-30) [S]
URL: https://en.wikipedia.org/wiki/GPT-5
- GPT-5 launched 2025-08-07. Legacy models were removed from ChatGPT for non-Pro users at launch; some users objected to removal without warning and to the automatic router's reduced control.
- Router problems: Sam Altman said the "autoswitcher" broke for part of launch day, which made GPT-5 seem worse.
- Reversal reported 2025-08-08: GPT-4o restored as a selectable option for Plus users while OpenAI monitored usage. A warmer-personality update followed 2025-08-15.
- Use: consumer example, but the lesson is universal and B2B-relevant: removing the old model on launch day is a breaking change. Users attach to behavior, not only capability. In B2B the equivalent is a model swap that changes how Beacon writes diagnoses; announce it, offer a transition window, and measure acceptance rate before and after.
- Flag: secondary source only. Cite at the level of "OpenAI restored the previous model as an option within days after user objections" unless a primary source is checked.

### Wikipedia, "GPT-4o" sycophancy section [S]
URL: https://en.wikipedia.org/wiki/GPT-4o
- OpenAI rolled back a GPT-4o update in April 2025 for "excessive sycophancy" after users reported overly flattering, agreeable behavior.
- [U] From prior knowledge, not re-verified here (openai.com returned 403): OpenAI's follow-up posts ("Sycophancy in GPT-4o", late April 2025, and "Expanding on what we missed with sycophancy", early May 2025) said offline evals and A/B tests looked positive while some expert testers felt the model was "off"; commitments included treating behavior issues as launch-blocking, an opt-in alpha testing phase, and more proactive communication about model updates, even subtle ones. Verify on openai.com before use.
- Use: the canonical go/no-go lesson for AI launches. Quantitative signals were green, qualitative signals were amber, and the launch proceeded. Teach: give the qualitative reviewer a formal veto line in the go/no-go.

### Microsoft, "Frontier program" for Microsoft 365 Copilot (fetched 2026-10-30, no date on page) [V]
URL: https://www.microsoft.com/microsoft-365-copilot/frontier-program
- Early access to preview AI features and agents before GA; features labeled "Frontier".
- Business users: the organization must opt in and the user needs a Copilot license. IT admins turn Frontier on in the admin center, manage feature and agent availability, and assign eligible users. Consumer subscribers can opt in individually.
- Access and usage-based costs vary by feature.
- Use: the B2B early-access pattern for AI: the tenant admin, not the end user, opts in, and controls which agents are available to whom. Beacon's EAP should copy this: tenant-level opt-in by the customer's admin (Sam or Marcus), per-action allowlists, and a visible "early access" label in the product.

### Colorado General Assembly, SB25B-004 (signed 2025-08-28) [V]
URL: https://leg.colorado.gov/bills/sb25b-004
- Extends the effective date of the Colorado AI Act (SB24-205, consumer protections for interactions with AI systems) to 2026-06-30.
- Page does not describe SB24-205's disclosure duties. [U] From prior knowledge: SB24-205 requires deployers of AI systems that interact with consumers to disclose that the consumer is interacting with AI, with high-risk duties for consequential decisions. Whether a 2026 session amended it again was not checked.
- Use: a sentence in the AI disclosure section that disclosure rules are now multi-jurisdiction, so the readiness checklist names "AI disclosure" as a legal line item, not a copywriting choice. Beacon (B2B, ops engineers, not consequential decisions about consumers) is unlikely to be high-risk under Colorado, but the legal review must say so in writing.

### Schneider, J. and Hall, J. "Why Most Product Launches Fail" (Harvard Business Review, April 2011) [S, paywalled]
URL: https://hbr.org/2011/04/why-most-product-launches-fail
- Only metadata and the opening paragraph were readable. Do not cite the article's list of failure causes or any statistic from it without access.

---

# Synthesis for the chapter author

## (a) Key concepts and frameworks

1. **Launch as an externally visible change (Google SRE, Klau).** Google defines a launch as any new code that introduces an externally visible change. Consequence for the PM: most launches are small, so the system needs a cheap default path and an expensive path for the few that matter. Google's launch reviews scaled partly by classifying low-risk launches. This is the root logic of launch tiers.

2. **Launch tiers (practitioner convention; no single originator found) [U as attribution].** Common practice in product marketing is three tiers. The book should present this as its own synthesis, not attribute it. Proposed matrix (the book's own, to state as such):
   | | Tier 1 | Tier 2 | Tier 3 |
   |---|---|---|---|
   | Criteria (any two) | new product, new SKU or price; changes how buyers evaluate us; material revenue or pipeline target; regulatory or trust exposure (AI autonomy, data use) | meaningful new capability for existing customers; changes admin or user workflow; competitive parity gap closed | improvement, fix, minor UI or integration |
   | Gets | PR/FAQ lineage, press release and analyst briefings, flagship event moment, sales enablement and certification, pricing and packaging, customer webinar, transparency note, go/no-go with exec decider, post-launch review at 30 and 90 days | blog post, release notes, in-app announcement, enablement brief for sales and support, customer FAQ, go/no-go with PM decider | release notes and changelog only, support macro if needed |
   | Rollout | design partners, then EAP, then LA, then GA | opt-in or percentage rollout | straight to GA behind a flag |
   | Decider | VP or GM | PM lead | engineering lead |
   Teaching point: tier by customer and business impact, not by engineering effort. AI features get bumped one tier up when they change what the system does on the customer's behalf.

3. **Release stages: private preview, public preview, LA, GA (GitHub, GitLab, AWS, Azure).** GitHub's three stages and GitLab's four (Experiment, Beta, Limited availability, GA) give the cleanest definitions. Key distinctions to teach: previews carry no SLA and often no support (AWS, GitHub); preview terms carry legal consequences (confidentiality, no production use, data handling: Azure, AWS); LA means supported production use at reduced scale or platform coverage, held to the same security bar as GA (GitLab). Map program names onto stages: design partners = private preview under NDA; EAP = private or public preview with admin opt-in; LA = supported, gated; GA = all customers, SLA, list price.

4. **Separate deploy from release (Hodgson; Sato; Google SRE).** Feature flags of four types (release, experiment, ops, permissioning) and canary releases let the same build pass through every stage. Canary is risk reduction over minutes or hours; A/B tests are hypothesis tests over days, and Sato warns against conflating them. Cross-reference Chapter 6's progressive delivery and release-plan template (research-ch06.md), so this chapter does not re-teach mechanics.

5. **Launch readiness checklist (Google SRE LCE categories plus GTM functions).** Google's engineering categories (architecture and dependencies, capacity tied to promotion, failure modes, client behavior, automation, external dependencies, rollout plan) cover only engineering. The chapter extends it across functions: product, engineering, docs, support, sales, legal, billing, security, marketing. Each row: owner, definition of ready, evidence link, status (green, amber, red). The Google point worth keeping: a press release is a capacity input.

6. **Go/no-go poll (NASA launch status check).** Every position reports go or no-go for its own domain, on the record, and one named director makes the call. Transfer to software: a short meeting, each function reads its readiness status, any red is a no-go unless the decider records an explicit risk acceptance, and decisions are written down (go, no-go, go with conditions). AI addition from the OpenAI sycophancy case [U]: a qualitative behavior reviewer has a formal no-go line even when metrics are green.

7. **Working Backwards PR/FAQ (Bryar and Carr; Amazon).** Pre-build artifact: a one-page press release plus up to five pages of FAQ, split external and internal. Exact section order is in the source log. At launch, it forks into the real press release, the blog post, the customer FAQ and the internal FAQ. Teach the gap analysis: compare the inception PR/FAQ with the launch-day release and explain every difference.

8. **Release notes (Lacan, Keep a Changelog).** Written for people; dated; latest first; grouped by Added, Changed, Deprecated, Removed, Fixed, Security. Book extension for AI features: a "Model and behavior changes" group.

9. **Platform launches do not break builders (Leach, Stripe).** Version pinning and long-term compatibility. AI-era analogue: model version pinning windows and deprecation notices.

10. **Post-launch review (Lunney and Lueder, Google SRE postmortem culture).** Blameless, triggered by criteria set in advance, reviewed by seniors, shared and stored. The post-launch review applies the same shape to launches that went well too: what we predicted (from the launch plan's success metrics), what happened, why, what we change.

11. **Measuring launch success.** No single external framework was verified in this session. The book's own position, consistent with earlier chapters: define leading and lagging metrics in the launch plan before launch. Leading (days to weeks): activation of the new capability by target accounts, EAP-to-paid conversion, support ticket rate per active account, enablement completion. Lagging (one to two quarters): influenced pipeline and win rate where the capability was shown, expansion revenue, retention of adopting accounts, and the product's North Star. Press coverage and event attendance are reach metrics, reported but never the goal.

## (b) Verified facts

All facts are in the source log above, each tagged [V], [S] or [U] with URL and date. The most chapter-ready:
- Google sometimes performs up to 70 launches per week; launch definition as any externally visible change [V, Google SRE book ch. 27].
- PR/FAQ: press release under one page, FAQ up to five pages [V, aboutamazon.com excerpt of Working Backwards].
- GitLab LA: production-ready at reduced scale, no explicit SLA, same security requirements as GA [V].
- AWS betas: no SLA, confidential, access ends at GA, content may not carry over [V].
- Anthropic gives at least 60 days' notice before retiring publicly released models [V].
- Agentforce: announced 2024-09-12 with a stated GA date of 2024-10-25 and $2 per conversation pricing [V].
- EU AI Act Art. 50 transparency obligations apply from 2026-08-02 [S, mirror site].
- Colorado AI Act effective date moved to 2026-06-30 [V].
- GPT-5 launch 2025-08-07, GPT-4o restored as an option days later [S].

## (c) Quotes (each under 15 words)

1. Google SRE book: a launch is "any new code that introduces an externally visible change to an application." (Klau, Site Reliability Engineering, ch. 27.) Note: 13 words.
2. Danilo Sato on canaries and A/B tests: "it is preferable to avoid conflating these two concerns." (CanaryRelease, 2014.)
3. Anthropic, postmortem 2025-09-17: Anthropic "never reduce[s] model quality due to demand, time of day, or server load."
4. Stripe, Leach 2017: an API "should run without interruption for as long as possible."
5. Salesforce, 2024-09-12: Agentforce "will be generally available on October 25, 2024." (Use only if the chapter needs the date in the source's words.)

## (d) 2025 to 2026 AI-era developments

- **Model changes are launches.** Anthropic's lifecycle vocabulary (Active, Legacy, Deprecated, Retired) and 60-day minimum notice [V]; the GPT-5 launch removing older models and partially reversing within days [S]; the April 2025 GPT-4o sycophancy rollback [S, details U]. Lesson: a model swap needs a tier, evals, release notes and a transition window.
- **Silent regressions without a model change.** Anthropic's September 2025 postmortem showed infrastructure changes can degrade AI quality, and that pre-launch evals alone did not catch it [V]. The launch plan needs continuous production quality evals and a feedback path.
- **Admin-controlled early access for agents.** Microsoft's Frontier program puts the tenant admin in control of which preview agents users get [V]. Azure's preview terms allow abuse monitoring of generative AI preview data [V]. EAP design for B2B AI is a governance decision.
- **AI disclosure becomes law.** EU AI Act Art. 50 from 2026-08-02 [S]; Colorado from 2026-06-30 [V for date]. Disclosure is a readiness checklist row owned by legal and product.
- **Transparency notes as launch artifacts.** Microsoft publishes transparency notes describing capabilities, intended uses and limitations [V]. For B2B AI, this is now part of the tier 1 kit that security reviewers expect.
- **Staged autonomy.** From Chapter 31: shadow mode, human approval, allowlisted autonomy, kill switch. For launches, autonomy level is a release stage of its own, independent of availability stage.

## (e) Beacon worked example ideas (consistent with beacon-case.md)

- **Launch:** Beacon Agents (supervised remediation, the Act capability) announced at Northlight Live. Tier 1: new pricing (per resolved incident), new trust exposure (actions in production), and Northlight's flagship event.
- **Two axes in the launch plan.** Availability: design partners (8 to 12 accounts under NDA, private preview) to EAP (admin opt-in, public preview label, no SLA) to LA (supported, selected connectors only, e.g., Northlight Observe plus two clouds) to GA (all connectors, SLA, list price). Autonomy: shadow (agent proposes, never acts) to approve-each-step to allowlisted low-risk actions autonomous. Rule: no account moves up the autonomy axis faster than its admin opts in. Numbers here are illustrative and should be labeled as such.
- **Go/no-go at T minus 10 days before Northlight Live.** Readiness table across nine functions. Plausible amber items: billing cannot yet meter "resolved incident" consistently (dispute risk); docs for two connectors incomplete; security review of action audit logs passed; support runbook for "agent took a wrong action" drafted but not rehearsed. Decision: go for announcement and LA, with GA and per-incident pricing as a dated later step, which mirrors the Agentforce pattern of announcing with a later GA date.
- **Use the hallucinated root cause storyline.** The incident where a customer rolled back the wrong service happened in EAP; the go/no-go requires the fix (eval set for that failure mode at a stated pass threshold, approval gate on rollbacks) before LA. The customer FAQ answers "what happens if the agent is wrong?" directly.
- **Artifacts in Beacon voice:** the inception PR/FAQ (written a year earlier) versus the launch press release, with a diff; customer FAQ (pricing transition from per environment, data use, which actions can be autonomous, how to turn it off, EU AI Act documentation); internal FAQ (gross margin at 72 percent and inference cost per resolved incident, competitive responses, what sales must not promise); release notes with "Model and behavior changes"; a Beacon Agents transparency note.
- **Personas:** Priya as design-partner champion; Dana as the EAP user whose acceptance rate is measured; Sam signs off the security and AI disclosure rows; Marcus is the buyer the press release speaks to; Leo (MSP) gets a tier 2 follow-on launch for multi-tenant views.
- **Success metrics:** leading: diagnosis acceptance rate and approved-action rate among LA accounts, EAP-to-paid conversion, support tickets per active account; lagging: autonomous resolution rate, North Star (incidents resolved with Beacon's help per week), pipeline influenced from Northlight Live, NRR among adopting accounts. Press coverage reported as reach only.
- **Model change after GA.** Upstream model deprecation (Beacon's provider retires a model with 60 days' notice) forces a model swap; treat it as a tier 2 launch with eval deltas published in release notes and a 30-day pinning window for customers.
- **Post-launch review at 30 and 90 days,** blameless format, comparing predicted with actual metrics, and recording whether the conditional go was justified.

## (f) Editorial flags

1. **Launch tiers have no verified originator.** Several product marketing sources could not be fetched (404s). Present the tier matrix as the book's own synthesis.
2. **Google Cloud launch stage definitions were not retrieved.** Do not cite them.
3. **OpenAI sycophancy postmortem details are [U].** openai.com returned 403. Only the rollback in April 2025 is [S]. Verify the commitments before quoting them.
4. **GPT-5 launch facts are [S]** (Wikipedia). Keep to the high-level sequence.
5. **Agentforce GA date ambiguity:** the September release promised 2024-10-25; the October 29 page was summarized as GA on that date. Use "late October 2024".
6. **EU AI Act Art. 50 date** came from a mirror site; Chapter 31 notes an Omnibus grace period for 50(2). Check against EUR-Lex before print.
7. **Colorado SB24-205 duties** are from prior knowledge; check whether a 2026 session amended it again.
8. **Wiley "more than 40 percent" figure** is a customer claim inside a vendor press release; use only as an example of how press releases use pilot proof, if at all.
9. **No verified external framework for launch success measurement** was found in this session; the leading and lagging list is the book's own position.
10. **Search budget.** The web search budget was exhausted before this chapter started; sources were reached by direct fetch. A later pass could add a product marketing source on tiers and enablement, and a design partner program source.
