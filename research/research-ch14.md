# Research notes: Chapter 14, Digital Platform Strategy and Network Effects

Status: complete first pass (2026-10-30). Tags: [V] verified on primary source, [S] secondary only, [U] unverified.

## Sources log (as gathered)

### 1. Van Alstyne, Parker, Choudary. "Pipelines, Platforms, and the New Rules of Strategy." Harvard Business Review, April 2016. [V] (full text read via MIT IDE copy)
URL: https://hbr.org/2016/04/pipelines-platforms-and-the-new-rules-of-strategy (MIT IDE PDF copy: https://ide.mit.edu/wp-content/uploads/2017/05/Pipelines-Platforms-and-the-New-Rules-of-Strategy.pdf.pdf)
- Pipeline = creates value by controlling a linear series of activities (value chain). Platform = creates value by facilitating interactions between external producers and consumers. A firm can be both (Apple handset is a pipeline; plus App Store = platform).
- Four players in every platform ecosystem: owners (control IP and governance), providers (interface with users), producers (create offerings), consumers (use offerings).
- Three shifts, exact headings: (1) From resource control to resource orchestration. (2) From internal optimization to external interaction. (3) From a focus on customer value to a focus on ecosystem value.
  - Shift 1: the hard-to-copy asset is the community and the resources members contribute; "the network of producers and consumers is the chief asset."
  - Shift 2: emphasis moves from dictating processes to persuading participants; ecosystem governance becomes an essential skill.
  - Shift 3: maximize total ecosystem value; sometimes subsidize one side to attract another.
- Porter's five forces still apply but behave differently; watch interactions, participant access, new metrics.
- Launch with a single high-value core interaction, then expand to adjacent interactions (Facebook Harvard-only, then colleges, then everyone).
- Access and governance: strategy shifts from erecting barriers to eliminating barriers to production and consumption. Choices about access (who gets on) and governance (what participants may do).
- Openness has two dimensions: open architecture (access to platform resources, e.g., developer tools) and open governance (others shape rules of trade and reward sharing). Opening architecture without sharing rewards gives ability but no incentive; opening rewards with closed architecture gives incentive but no ability. Platforms often launch closed and open over time.
- "Permissionless innovation": producers build without approval but are guaranteed to share in value created.
- Unfettered access creates "noise" (Chatroulette example); successful platforms curate (ratings, insurance, app review).
- New metrics: interaction failure, engagement, match quality, negative network effects (congestion, misbehavior). Plus financial value of community.
- Leadership: skills for controlling internal resources do not transfer to nurturing ecosystems (Myspace under top-down management cited).
- PM application: use the four roles and three shifts as the frame for a "platform map"; use the four metrics as the platform health section of a network effects assessment.

### 2. NFX (James Currier and team). "The Network Effects Manual: 16 Different Network Effects (and counting)." nfx.com, page dated June 2021 (earlier 13-type version 2018). [V]
URL: https://www.nfx.com/post/network-effects-manual
- 16 types in five categories plus standalones; map arranges strongest and simplest at center.
- Direct: Physical (utilities, roads), Protocol (Ethernet, Bitcoin), Personal Utility (messaging tied to identity), Personal (identity and reputation, e.g., LinkedIn), Market Network (identity plus transactions, e.g., HoneyBook, Houzz).
- Hub-and-Spoke (content submitted to a hub and pushed out).
- 2-sided: Marketplace (buyers and sellers), Platform (developers build products that run on it, e.g., iOS, Xbox), Asymptotic Marketplace (early supply adds lots of value, then diminishes, e.g., ride hailing).
- Expertise (tool more valuable as more professionals know it, e.g., Excel, Salesforce).
- Data network effect: product more valuable as more data accumulates, where usage generates the data.
- Tech performance (tech improves with more users, e.g., BitTorrent).
- Social: Language, Belief, Bandwagon, Tribal.
- Claim: NFX's own three-year study found network effects account for about 70% of value created by tech companies since 1994. [V that NFX claims it; methodology NFX-internal, flag]
- Data network effects "generally weaker than many VCs believe": more data does not always add value; strength depends on how central data is to the product; Netflix (content-driven, marginal), Yelp (few reviewers, diminishing value per extra review), Experian (scale effect, not network effect, because consumer usage does not generate the data).
- PM application: classify each candidate effect by type; be honest that most B2B "data moats" are scale effects or asymptotic.

### 3. Andrew Chen. The Cold Start Problem: How to Start and Scale Network Effects. Harper Business, 2021. [V for stage names and atomic network via author's site; book text not read]
URLs: https://andrewchen.com/?p=4769 (author excerpt, essay on hiring a head of growth) ; https://andrewchen.com/solve-a-hard-problem-cold-start-problem/ (book chapter excerpt on hard side)
- Five stages, exact names: (1) The Cold Start Problem, (2) Tipping Point, (3) Escape Velocity, (4) Hitting the Ceiling, (5) The Moat.
- Atomic network: per Chen, the smallest possible network that is stable and can grow on its own. [V paraphrase from author site]
- Anti-network effects: early on, a network that is too small makes users leave because they cannot find what they want, which shrinks it further. [V]
- Hard side: a minority of users who create disproportionate value and are hardest to attract and keep (creators, app developers, sellers, managers who invite colleagues). Advice: solve a hard problem for the hard side, start with an underserved niche of it, then expand to adjacent segments. [V]
- Tipping point: a repeatable playbook for building adjacent atomic networks until the market tips (Tinder by campus, Uber by city). [S]
- Escape velocity: compounding acquisition, engagement and economic loops. [S]
- PM application (B2B): the atomic network is often one team, one account, or one integration pair (e.g., one SRE team plus its five core tools). The hard side in a developer platform is the builders (connector authors, partners), not the end users.
- Flag: secondary claims like "hard side costs 5 to 10 times more to acquire" are not in Chen's text that I saw. Do not use.

### 4. Hagiu, Andrei and Julian Wright. "When Data Creates Competitive Advantage." Harvard Business Review, January to February 2020. [V for thesis; criteria list S]
URL: https://hbr.org/2020/01/when-data-creates-competitive-advantage ; BU summary https://bu.edu/dbi/2020/06/01/when-data-can-give-you-a-competitive-edge-and-when-it-cant
- Thesis: executives commonly assume more customers produce more data, a better product, more customers; authors say this "data-enabled learning" loop is usually weaker and less enduring than true network effects.
- Quote (V, HBR intro): "In most instances people grossly overestimate the advantage that data confers." (13 words)
- Conditions for advantage (S, via secondary summaries; HBR body paywalled): value added by customer data is high relative to the standalone product; the marginal value of data stays high (does not plateau quickly); data does not lose relevance fast; data is proprietary; improvements are hard to imitate; learning from one user improves the product for other users (then it is closer to a network effect). Strongest position combines data-enabled learning with genuine network effects. 
- Authors prefer the term "data-enabled learning" over "data network effects" because the phenomenon need not involve a network effect.
- PM application: use these as the "data moat" test in a network effects assessment.

### 5. Eisenmann, Thomas, Geoffrey Parker and Marshall Van Alstyne. "Platform Envelopment." Strategic Management Journal 32(12), 2011, pp. 1270 to 1285. DOI 10.1002/smj.935. [S: citation confirmed across several listings; abstract summarized via secondary]
URL: https://doi.org/10.1002/smj.935 (also HBS working paper 2007)
- Envelopment: a provider in one platform market enters another platform market by bundling its own functionality with the target's, leveraging shared user relationships. Lets entrants bypass the need for breakthrough innovation; incumbents protected by network effects against standalone rivals can still be enveloped.
- Commonly described three forms (S, from paper abstract as cited in literature): envelopment of complements, of weak substitutes, and of functionally unrelated platforms. [verify wording before using as a list]
- PM application: in B2B, the classic threat is a large suite (observability platform, ITSM suite, hyperscaler) bundling your category as a feature into an existing customer relationship.

### 6. Linux Foundation. "Linux Foundation Announces the Formation of the Agentic AI Foundation (AAIF)." Press release, 9 December 2025. [V]
URL: https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
- AAIF formed 9 Dec 2025 under the Linux Foundation. Founding projects: Model Context Protocol (contributed by Anthropic), goose (contributed by Block), AGENTS.md (contributed by OpenAI).
- Platinum members: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI.
- Release states more than 10,000 published MCP servers and adoption by Claude, Cursor, Microsoft Copilot, Gemini, VS Code, ChatGPT and others (as of Dec 2025).
- PM application: MCP is now neutrally governed infrastructure, a "protocol network effect" in NFX terms; building an MCP server is a distribution decision, not a bet on one vendor.

### 7. Linux Foundation. "Linux Foundation Launches the Agent2Agent Protocol Project..." Press release, 23 June 2025. [V via search of LF release; S on member list]
URL: https://linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents
- A2A created by Google (announced April 2025), transferred to the Linux Foundation, launched as an LF project 23 June 2025 at Open Source Summit North America. Backed by AWS, Google, Microsoft, Salesforce, SAP, ServiceNow and others; release cites support from more than 100 companies.
- Vendor-neutral governance; SDKs and developer tools transferred too.
- Editorial note: one founding backer in the list is the author's employer; book rule says no employer-specific content, so list members generically ("major cloud and enterprise software vendors") or name only non-employer members.
- MCP vs A2A framing for the chapter: MCP connects an agent to tools and data (agent-to-tool); A2A connects agents to other agents (agent-to-agent). Both are protocol-layer platforms.

### 8. Choudary, Sangeet Paul, interviewed by MIT IDE. "Interactions Must Drive Platform Design." ide.mit.edu, 17 Sep 2015. [V]
URL: https://ide.mit.edu/insights/sangeet-choudary-interactions-must-drive-platform-design
- Advice: start with the interaction, not the technology, and remove friction. Filters govern access and content and balance openness with structure (light filters on Twitter vs many complex filters on Airbnb).
- Platform Revolution (Parker, Van Alstyne, Choudary; W. W. Norton, 2016) core interaction components: participants (producer, consumer), value unit, filter. [S: from multiple summaries; book not read directly]. Book also describes platform functions pull, facilitate, match. [U: not verified this session]

### 9. A2A Project. "A New Chapter for A2A: Joining the Agentic AI Foundation." a2a-protocol.org blog, 27 Aug 2026. [V] Plus a2a-protocol.org home and "What's New in v1.0". [V for content; v1.0 date S]
URLs: https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/ ; https://a2a-protocol.org/latest/
- A2A accepted as a Growth Stage project at the Agentic AI Foundation (AAIF); post dated 27 Aug 2026. States more than 150 organizations back A2A and it runs in production in supply chain, financial services and mobile platforms.
- Framing used by the A2A project itself: MCP is the vertical layer (agent to tools and data), A2A is the horizontal layer (agent to agent). The home page calls them complementary, not competing.
- v1.0 is the stable spec. Changes include restructured Agent Card (supportedInterfaces list, JWS signatures on cards), multi-tenancy via tenant field, renamed operations, removal of implicit and password OAuth flows. Release date: a linked post URL suggests 12 March 2026 [S]; secondary sources say March or April 2026. Flag: say "early 2026".
- Secondary press gives conflicting dates (17, 20 Aug 2026) for the AAIF move; use 27 Aug 2026 blog post as the primary date or just "August 2026".

### 10. Model Context Protocol. Specification versioning page and 2026-07-28 changelog. modelcontextprotocol.io, accessed 30 Oct 2026. [V]
URLs: https://modelcontextprotocol.io/specification/versioning ; https://modelcontextprotocol.io/specification/2026-07-28/changelog
- Current MCP protocol version: 2026-07-28 (previous: 2025-11-25). Versions are dates of the last backwards-incompatible change.
- 2026-07-28 makes MCP stateless: removes protocol-level sessions and the initialize handshake; adds mandatory server/discover; moves Tasks into an official extension; adds extensions capability field; adopts a feature lifecycle and deprecation policy (minimum 12-month deprecation window); deprecates Roots, Sampling and Logging features; deprecates Dynamic Client Registration in favor of Client ID Metadata Documents.
- PM relevance: a platform with a published deprecation policy is a governance signal to builders. Use as the model for "developer platform brief" API lifecycle section. Do not teach protocol details in the chapter; just the governance lesson.

### 11. MCP blog. "Introducing the MCP Registry" (preview). blog.modelcontextprotocol.io, 8 Sep 2025. [V]
URL: https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/
- Open catalog and API for publicly available MCP servers; the "primary source of truth". Anyone can build compatible sub-registries: public ones (opinionated marketplaces tied to particular clients) and private ones (enterprise internal registries). Maintained by a registry working group.
- PM relevance: discovery layer of the agent ecosystem looks like app-store layering (upstream neutral catalog, curated downstream marketplaces, private enterprise catalogs). Enterprise buyers increasingly ask "is your server in our private registry with approved scopes?"

### 12. AWS. "Introducing AI agents and tools in AWS Marketplace." What's New, 16 Jul 2025. [V]
URL: https://aws.amazon.com/about-aws/whats-new/2025/07/ai-agents-tools-aws-marketplace
- New category for third-party AI agents and agent tools; natural-language search; listings can indicate MCP and A2A support; deploy via Amazon Bedrock AgentCore Runtime or add tools to AgentCore Gateway; "streamlined procurement".
- [S] Press coverage (PYMNTS, CRN Asia) reported about 800 to 900 listings at launch; use "hundreds" if cited.
- PM relevance: hyperscaler marketplaces are now agent distribution channels; protocol support is a filter buyers use.

### 13. Anthropic. "Donating the Model Context Protocol and establishing the Agentic AI Foundation." anthropic.com, 9 Dec 2025. [V] And "Introducing the Model Context Protocol," 25 Nov 2024. [V]
URLs: https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation ; https://www.anthropic.com/news/model-context-protocol
- MCP announced 25 Nov 2024 as an open standard replacing one-off integrations between AI assistants and data sources ("every new data source requires its own custom implementation" problem, i.e., the N x M integration problem; the N x M label is ours, not Anthropic's).
- Donation 9 Dec 2025 to AAIF, described as a directed fund under the Linux Foundation; reasons: keep it open, community-driven, vendor-neutral. Figures at donation: more than 10,000 active public MCP servers; 97M+ monthly SDK downloads across Python and TypeScript; clients include ChatGPT, Cursor, Gemini, Microsoft Copilot, VS Code. MCP governance model stated to "remain unchanged".
- PM lesson: a platform owner giving up control of a protocol to grow the protocol network effect (open governance in the Van Alstyne/Parker/Choudary sense). The value capture moves up to models, clients and services.

### 14. Microsoft. "Introducing Microsoft Marketplace." Official Microsoft Blog, 25 Sep 2025. [V]
URL: https://blogs.microsoft.com/blog/2025/09/25/introducing-microsoft-marketplace/
- Merges Azure Marketplace and Microsoft AppSource into one destination for cloud solutions, AI apps and agents (US first). Over 3,000 AI apps and agents newly available. Dedicated AI Apps and Agents category.
- Purchases of eligible "Azure benefit" solutions count fully toward a customer's Azure consumption commitment. This is the core economic reason enterprise ISVs list on hyperscaler marketplaces: buyers spend pre-committed cloud budget.
- Channel: distributors (Arrow, Crayon, Ingram Micro, Pax8, TD SYNNEX) integrating Marketplace into their own marketplaces; resale-enabled private offers (private preview) let ISVs authorize channel partners to sell on their behalf.
- PM relevance for Beacon: MSP partner Leo could buy Beacon through a distributor marketplace; customers like Marcus could burn cloud commit on Beacon.

### 15. Salesforce. AgentExchange announcement press release, 4 Mar 2025. [V]
URL: https://www.salesforce.com/news/press-releases/2025/03/04/agentexchange-announcement/
- Marketplace and community for Agentforce, built into Salesforce. Partners offer prebuilt actions, prompt templates, topics and agent templates. More than 200 partners and hundreds of components at launch.
- Example of an incumbent SaaS suite turning its agent product into a platform with a component marketplace.

### 16. OpenAI developer docs (Apps SDK / plugins), accessed 30 Oct 2026. [V for current page content; history S]
URL: https://developers.openai.com/apps-sdk
- As of Oct 2026 the page describes ChatGPT plugins that combine skills, MCP servers and optional UI, built on MCP (UI resources attached to MCP tools); publishing to the ChatGPT Directory requires following plugin guidelines and remote MCP server review requirements.
- [S, from memory not re-verified this session] OpenAI introduced "apps in ChatGPT" and the Apps SDK at DevDay, October 2025. Flag naming drift: "apps" in 2025 vs "plugins" on the 2026 docs page. Chapter should describe generically ("AI assistant app directories that accept MCP-based integrations, subject to review").

### 17. Apple. App Review Guidelines. developer.apple.com, accessed 30 Oct 2026. [V]
URL: https://developer.apple.com/app-store/review/guidelines/
- Five sections: Safety, Performance, Business, Design, Legal. Guiding principle: safe place for users, real chance for developers. Living document; apps no longer working may be removed; cheating review can lead to expulsion from the developer program; developers are responsible for third-party SDKs inside their apps.
- US storefront: under 3.1.1(a) and 3.1.3(a), apps may include buttons and external links to non-IAP purchase methods without applying for an entitlement; elsewhere generally requires an entitlement (e.g., StoreKit External Purchase Link Entitlement) in approved storefronts.
- PM use: (1) best-known example of a published platform governance policy with a clear structure, useful as template for the "platform governance policy" artifact; (2) example of how platform rules you do not own change under regulation and courts, a dependency risk.
- Flag: do not narrate the legal history (Epic v. Apple, EU DMA) without verifying dates; not verified this session.

### 18. Hagiu, Andrei. "Strategic Decisions for Multisided Platforms." MIT Sloan Management Review, Winter 2014 (online 19 Dec 2013). [V for the four decisions and multihoming definition]
URL: https://sloanreview.mit.edu/article/strategic-decisions-for-multisided-platforms/
- Four strategic decisions: (1) number of sides, (2) design, (3) pricing structure, (4) governance rules.
- Distinguishes switching costs (leave one platform for another) from multihoming costs (stay on current platform and also join a competing one).
- PM use: the four decisions become section headings in a platform map or developer platform brief.

### 19. Casado, Martin and Peter Lauten. "The Empty Promise of Data Moats." a16z, 9 May 2019. [V]
URL: https://a16z.com/the-empty-promise-of-data-moats/
- Argues data is rarely a moat for enterprise startups; true data network effects are doubtful there; most claims are scale effects that weaken over time. Example from a support chatbot: early data covers common intents cheaply; later data costs more and adds less; coverage plateaus (about 40% of intents in that example) so competitors can catch up.
- Quote: "defensibility is not inherent to data itself" (6 words). [V]
- Advice: bootstrap a minimum viable corpus; know the long tail of your data distribution; quality over quantity; secure proprietary sources; do not rely on data alone.
- PM application: directly relevant to Beacon's "Learn" loop claims.

### 20. NFX. "The Network Effects Bible (Updated 2024)." nfx.com, first published July 2019. [V]
URL: https://www.nfx.com/post/network-effects-bible
- Definition: every new user makes the product more valuable to every other user.
- Strength drivers: density (link-to-node ratio) and clustering; find the densest "white-hot center" and expand outward.
- Asymptotic effects: past some size, more participants add little value to existing users (more drivers once wait times are short).
- Threats: disintermediation (users meet on the platform, then transact off it) and multi-tenanting, NFX's term for multi-homing (joining competing networks cheaply).

### 21. Gawer, Annabelle and Michael Cusumano. "How Companies Become Platform Leaders." MIT Sloan Management Review, Winter 2008. [V for content below]
URL: https://sloanreview.mit.edu/article/how-companies-become-platform-leaders/
- Platform = core components from one company plus complements from others. Platform leaders solve technical challenges (architecture, interfaces, selective disclosure of IP so third parties can build) and business challenges (make key complements yourself or create incentives for others).
- "Coring" and "tipping" strategies are associated with this work [S, not visible in the page excerpt; verify before naming them].

### 22. Choudary, Sangeet Paul. Reshuffle (companion site reshufflebook.com). [V for thesis; publication year and publisher U]
URL: https://www.reshufflebook.com/
- Thesis: AI lowers coordination costs, which changes firm boundaries, industry architecture and where value is captured; most AI programmes stop at task efficiency.
- Use only as an optional framing line for the "agents as ecosystem coordinators" section.

---

## (a) Key concepts and frameworks (synthesis for the chapter)

1. **Pipeline vs platform** (Van Alstyne, Parker, Choudary, HBR 2016; Platform Revolution, W. W. Norton 2016). Pipeline: linear value chain you control. Platform: you facilitate value-creating interactions between external producers and consumers. Most B2B firms are hybrids. Template for the platform map: the four roles (owner, provider, producer, consumer) plus the three shifts. B2B application: ask which of your product's value is made by outsiders (connector authors, partners, integrators, customers' own runbooks) and whether you could make that a deliberate design choice.

2. **Core interaction** (Platform Revolution). Participants, value unit, filter. Design the single most important interaction first; layer others later (Facebook, LinkedIn). Template line: "On our platform, [producer] creates [value unit]; [filter] matches it to [consumer], who [consumes/acts]."

3. **Network effect types** (NFX manual, 2021, 16 types). For B2B and enterprise, the relevant ones: Protocol, Platform (2-sided, developers build on it), Marketplace and Asymptotic Marketplace, Expertise (professionals trained on the tool), Data (usually weaker than claimed), Tech performance, Bandwagon. Direct effects are rare in enterprise tools except inside collaboration and messaging.
   - **Direct (same-side):** more users of the same type make it better for each other.
   - **Indirect / cross-side:** more of one side makes it better for the other side (developers and users; buyers and sellers).
   - **Data network effects:** only when usage generates data that improves the product for *other* users; otherwise it is data-enabled learning or a scale effect (Hagiu and Wright 2020; NFX; Casado and Lauten 2019).
   - **Expertise** is underrated in enterprise: certified admins and trained SREs make switching costly.

4. **Network effects assessment** (synthesis; no single originator, built from NFX types plus Hagiu-Wright criteria plus HBR 2016 metrics). Proposed template for each claimed effect: Type (NFX) | Sides involved | Mechanism (who gets more value when whom joins) | Evidence today (metric) | Strength drivers (density, clustering) | Limits (asymptote, multi-homing cost, disintermediation risk) | Verdict (real network effect / scale effect / switching cost / aspiration). Platform health metrics from HBR 2016: interaction failure, engagement, match quality, negative network effects.

5. **Data-enabled learning test** (Hagiu and Wright 2020). Questions: How much value does customer data add relative to the standalone product? How fast does marginal value of data fall? How quickly does data become stale? Is the data proprietary? Are improvements hard to imitate? Does learning from one customer improve the product for others? [criteria S; see flags]

6. **Cold start** (Andrew Chen 2021). Five stages: Cold Start Problem, Tipping Point, Escape Velocity, Hitting the Ceiling, The Moat. Atomic network; hard side; anti-network effects. B2B translation: atomic network can be a single customer's team, a single integration pair, or a cluster of MSP customers; hard side is usually the builders (connector and agent authors) or the partner channel.

7. **Openness and governance** (HBR 2016). Two levers: architecture (who can access resources) and governance (who sets rules and rewards). Mismatch failure modes: ability without incentive; incentive without ability. Start closed, open as value grows. "Permissionless innovation" with guaranteed value share. Curate to control noise.

8. **Multi-sided platform decisions** (Hagiu, MIT SMR 2014). Number of sides; design; pricing structure; governance rules. Switching costs vs multihoming costs.

9. **Multi-homing and envelopment** (NFX Bible on multi-tenanting; Eisenmann, Parker, Van Alstyne 2011). Low multihoming costs weaken winner-take-all. Envelopment: an adjacent platform bundles your function into its existing user relationships. B2B case: the large observability suite or hyperscaler adds "AI incident agent" as a bundled feature.

10. **Platform leadership** (Gawer and Cusumano 2008). Architecture, interfaces, selective IP disclosure; build key complements yourself or incentivize others.

11. **Working with platforms you do not own** (synthesis from Apple guidelines, AWS and Microsoft marketplaces, AI directories). Questions for a PM: What does the host platform give us (distribution, procurement, trust, commit drawdown)? What does it take (fees, rules, data, customer relationship)? What can change without our consent (policy, ranking, fees)? What is our exit or multi-homing plan? Are we a complement the host might envelop?

12. **Agent ecosystems as platform strategy (2025 to 2026).** MCP (agent to tool and data, vertical) and A2A (agent to agent, horizontal), both under AAIF/Linux Foundation. Protocol network effects (NFX type 2) now apply to agents. Strategic choices for a B2B product: (1) be a host (agents and connectors plug into you), (2) be a complement (publish MCP servers and A2A agents into others' hosts), or (3) both. Registries (MCP Registry with public and private sub-registries) and marketplaces (AWS AI Agents and Tools, Microsoft Marketplace, Salesforce AgentExchange, AI assistant directories) are the new distribution surfaces.

### Artifact templates to build in the chapter (proposed formats, our own)
- **Platform map**: one page. Rows: owner, providers, producers, consumers (HBR 2016 roles), core interaction (participants, value unit, filter), adjacent interactions, platforms we depend on, platforms that could envelop us.
- **Network effects assessment**: table as in concept 4, plus data-enabled learning test, plus cold start stage and atomic network.
- **Ecosystem and partner strategy**: segments of partners (technology integrations, marketplaces, channel/MSPs, SIs), value exchange per segment (what they give, what they get), host-vs-complement stance per platform, exit and multi-homing plan, 3 to 5 metrics.
- **Developer platform brief**: target builder (hard side), job to be done, surfaces (APIs, MCP server, A2A agent card, SDKs), access tiers, reward model (rev share, co-sell, listing), versioning and deprecation policy (MCP's 12-month minimum as an example), success metrics (time to first working integration, active builders, integrations used weekly).
- **Platform governance policy**: scope; participant obligations; review and certification; data and security rules (least privilege, audit); quality filters; enforcement ladder (warn, delist, ban); appeals; change and deprecation notice; transparency. Modeled on structure of Apple's guidelines (Safety, Performance, Business, Design, Legal).

## (b) Verified facts table (quick reference)
- [V] HBR "Pipelines, Platforms, and the New Rules of Strategy," April 2016: three shifts and four roles as above. https://hbr.org/2016/04/pipelines-platforms-and-the-new-rules-of-strategy
- [V] NFX manual lists 16 network effect types (June 2021). https://www.nfx.com/post/network-effects-manual
- [V] NFX claims network effects account for about 70% of tech value since 1994 (NFX's own study). Same URL.
- [V] MCP announced by Anthropic 25 Nov 2024. https://www.anthropic.com/news/model-context-protocol
- [V] AAIF formed 9 Dec 2025 with MCP, goose, AGENTS.md. https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
- [V] At donation: 10,000+ active public MCP servers; 97M+ monthly SDK downloads. https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
- [V] MCP Registry preview 8 Sep 2025. https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/
- [V] Current MCP spec version 2026-07-28; stateless; 12-month deprecation policy. https://modelcontextprotocol.io/specification/2026-07-28/changelog
- [V] A2A became Linux Foundation project 23 Jun 2025; joined AAIF as Growth Stage project (blog 27 Aug 2026); 150+ organizations. https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/
- [V] AWS Marketplace AI agents and tools category 16 Jul 2025; listings show MCP/A2A support. https://aws.amazon.com/about-aws/whats-new/2025/07/ai-agents-tools-aws-marketplace
- [V] Microsoft Marketplace launched 25 Sep 2025; eligible purchases count toward Azure consumption commitment; 3,000+ AI apps and agents. https://blogs.microsoft.com/blog/2025/09/25/introducing-microsoft-marketplace/
- [V] Salesforce AgentExchange 4 Mar 2025; 200+ partners at launch. https://www.salesforce.com/news/press-releases/2025/03/04/agentexchange-announcement/
- [V] Apple App Review Guidelines: five sections; US storefront external purchase links allowed without entitlement under 3.1.1(a) and 3.1.3(a) (as of 30 Oct 2026). https://developer.apple.com/app-store/review/guidelines/
- [S] Platform Revolution: W. W. Norton, 2016; subtitle "How Networked Markets Are Transforming the Economy and How to Make Them Work for You".
- [S] The Cold Start Problem: Harper Business, 2021.
- [S] Platform Envelopment, SMJ 32(12), 2011, pp. 1270 to 1285.

## (c) Quotes (each under 15 words)
1. "the network of producers and consumers is the chief asset." Van Alstyne, Parker, Choudary, HBR 2016. [V]
2. "In most instances people grossly overestimate the advantage that data confers." Hagiu and Wright, HBR 2020. [V]
3. "defensibility is not inherent to data itself." Casado and Lauten, a16z 2019. [V]
4. "a minority of users that will create disproportionate value" Andrew Chen, on the hard side. [V on author site]
5. "Don't start with technology, start with the interaction" Choudary, MIT IDE 2015. [V]

## (d) 2025 to 2026 AI-era developments (verified)
- MCP donated to AAIF under Linux Foundation, 9 Dec 2025; platinum members AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI. [V]
- MCP Registry (preview Sep 2025) with public and private sub-registries. [V]
- MCP spec 2026-07-28: stateless, extensions, formal deprecation policy. [V]
- A2A: LF project June 2025; stable v1.0 early 2026 (signed Agent Cards, multi-tenancy) [date S]; joined AAIF Aug 2026. [V]
- Hyperscaler and SaaS agent marketplaces: AWS (Jul 2025), Microsoft Marketplace (Sep 2025), Salesforce AgentExchange (Mar 2025). [V]
- AI assistant directories accepting MCP-based integrations with review requirements (OpenAI docs, Oct 2026). [V current state]
- Thesis line (Choudary, Reshuffle): AI lowers coordination costs and moves where advantage sits. [V thesis]

## (e) Beacon worked example ideas (consistent with beacon-case.md)
- **Platform map for Beacon.** Owner: Northlight. Producers: connector and agent builders (Northlight's own teams, observability and ticketing vendors, MSPs like Leo writing runbooks, customers' SREs authoring runbooks). Consumers: responders (Dana, Priya). Providers: MSPs and resellers delivering Beacon to mid-market. Core interaction: a connector or runbook (value unit) is matched by Beacon's diagnosis agent (filter) to a live incident for a responder.
- **The strategic tension in beacon-case.md (build on Northlight Observe data vs stay tool-agnostic)** is exactly the openness decision. Open architecture (MCP connectors to any observability tool) grows the market and the cross-side effect; closed (Observe-only) protects data advantage. Recommend: open architecture with curated governance (certified connectors), and be honest that the "Observe data advantage" is data-enabled learning, not a network effect.
- **Network effects assessment for Beacon.** Candidate effects: (1) Platform/cross-side: more certified connectors make Beacon more useful to responders, more customers attract more connector builders. Real but early. (2) Data: resolved incidents feed retrieval and evals ("Learn"). Mostly within-customer learning; cross-customer only if anonymized patterns transfer, and limited by data residency (Sam's concerns, EU AI Act storyline). Verdict: data-enabled learning, asymptotic. (3) Expertise: SREs trained on Beacon runbooks. (4) MSP market: Leo's 60 customers form an atomic network where one runbook serves many tenants.
- **Cold start.** Atomic network = one platform team (Priya's 40 people) with its five core tools connected. Hard side = connector builders and MSPs. Tactic: Northlight builds the first 20 connectors itself (Gawer and Cusumano: make key complements yourself), then opens a partner program.
- **Working with platforms you do not own.** List Beacon on AWS and Microsoft marketplaces so Marcus can use cloud commit; publish a Beacon MCP server so Claude, Copilot and other assistants can query incidents; expose Beacon Agents via A2A so an ITSM agent (including Northlight Desk) can hand off diagnosis. Risk: envelopment by large observability platforms adding bundled AIOps agents (beacon-case.md names them as competitors) and by hyperscaler-native ops agents.
- **Governance policy.** Third-party runbook actions touching production need least privilege, audit logging, and Beacon's human approval gate; autonomous only for allowlisted low-risk actions. The hallucinated root cause storyline motivates certification and an enforcement ladder for connectors that return bad data.
- **Pricing tie-in.** Per-resolved-incident pricing affects partner revenue share; MSP per-customer billing needs multi-tenant metering.
- **AI harness prompts** (for the chapter's how-to): ask the harness, through connectors, to pull marketplace listing data, partner pipeline and connector usage, then draft the network effects assessment table with evidence cited per row and an explicit "verdict" column.

## (f) Editorial flags
- Hagiu and Wright criteria list is from secondary summaries (HBR body paywalled). Paraphrase as general questions; do not present as their numbered list.
- Platform Revolution "core interaction" (participants, value unit, filter) and "pull, facilitate, match" not read in the book this session. Core interaction triad is widely cited [S]; pull/facilitate/match [U].
- Gawer and Cusumano "coring and tipping" not verified on page excerpt.
- Platform Envelopment three forms (complements, weak substitutes, unrelated) [S]; verify before listing.
- NFX 70% figure is NFX's own study; attribute explicitly; do not present as independent research.
- A2A v1.0 date: March 2026 per linked post path, other sources say April. Write "early 2026". AAIF join date conflicts in press (17, 20, 27 Aug 2026); use the A2A blog (27 Aug 2026) or "August 2026".
- OpenAI naming drift ("apps" vs "plugins"); describe generically.
- AWS launch listing count varies (800 to 900) in press; avoid the number.
- Apple legal and regulatory history (Epic, EU DMA) not verified; avoid specifics.
- A2A Linux Foundation backers list includes the author's employer; to respect the no-employer-content rule, do not list backers by name.
- Reshuffle publication year and publisher not confirmed.
- Web search budget ran out during this session; Boudreau (2010) openness study, Rochet and Tirole two-sided markets, Eisenmann et al. 2006 winner-take-all conditions, and Google Cloud's agent marketplace were not verified. A follow-up pass could add them.
