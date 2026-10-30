<p class="lead">Some of the value your customers get from your product is made by people you don't employ: the partner who writes a connector, the integrator who builds a runbook, the agent inside someone else's assistant that calls your API. This chapter shows how to decide whether to design for that on purpose, how to tell a real network effect from a hopeful one, and how to compete when the platforms you depend on belong to someone else.</p>

## Why this matters

Most enterprise products start as pipelines: you build something, sell it, and the customer uses it, with you controlling every step. B2B software rarely stays that way for long. Customers want your product to talk to the twenty other tools they run. Partners want to resell it, extend it or bundle it. In 2026, AI agents want to call it. Each of those pressures pushes you to become partly a platform, and each comes with a choice you'll make either deliberately or by accident: who gets to build on you, on what terms, and who captures the value they create.

Get it right and outsiders add value faster than your engineering team could, and each new participant makes the product more useful to everyone else. Get it wrong and you open your architecture without giving anyone a reason to build on it, or you promise the board a "data network effect" that a well-funded competitor can match.

PMs tend to underrate the platforms they sit on. Your product probably reaches some customers through an app store, a hyperscaler marketplace, an AI assistant's directory or a larger suite's integration catalog. Those owners write rules you didn't write and can change them without asking you. A platform strategy has to cover both sides, the ecosystem you host and the ecosystems you join.

This chapter covers the pipeline and platform lens, the core interaction, a test for network effect claims, the cold start, openness and governance, and how to work with platforms you don't own, including the agent ecosystems built on MCP and A2A. These belong to the Strategy and Business dimensions of your Product 360. Chapter 13 sizes the market and maps competitors; Chapter 15 prices the offer; Chapter 16 asks which moats you really have. This chapter asks whether network effects are one of them, and how to build them if they aren't yet.

## Platforms and pipelines

### Two ways to create value

Marshall Van Alstyne, Geoffrey Parker and Sangeet Paul Choudary, in their 2016 HBR article "Pipelines, Platforms, and the New Rules of Strategy" and their book *Platform Revolution* from the same year, draw the distinction this chapter builds on. A **pipeline** creates value by controlling a linear series of activities: the classic value chain, where you design, make, sell and support. A **platform** creates value by facilitating interactions between external producers and consumers. The platform owner doesn't make most of what gets exchanged. It makes the exchange possible, safe and worth repeating.

A company can be both. Their own example is Apple: the handset is a pipeline product, and the App Store on top of it is a platform. Most B2B software companies are hybrids in the same way. The core product is a pipeline; the integration catalog, partner program and API are a platform, whether or not anyone designed them as one.

The authors name four roles in every platform ecosystem:

| Role | What they do | B2B example |
|---|---|---|
| **Owner** | Controls the platform's intellectual property and governance | The software vendor |
| **Providers** | Offer the interface through which users reach the platform | Resellers, managed service providers, hyperscaler marketplaces |
| **Producers** | Create the offerings that run on or through the platform | Connector authors, integration partners, customers who publish runbooks or templates |
| **Consumers** | Use those offerings | The end users and teams who get the value |

The same company can hold more than one role. A managed service provider can be a provider (it delivers your product to its customers) and a producer (it writes automations that run on it).

### Three shifts

The article argues that moving from pipeline to platform changes what strategy means, in three shifts:

1. **From resource control to resource orchestration.** On a platform, the hard-to-copy asset is the network of producers and consumers and what its members contribute, more than anything the owner holds on its own balance sheet.
2. **From internal optimization to external interaction.** Management shifts from running your own processes to persuading people you don't control to participate, which makes ecosystem governance a core skill.
3. **From customer value to ecosystem value.** A platform maximizes the total value of the ecosystem, which sometimes means subsidizing one side to attract the other.

The authors also argue that platforms need different metrics, and name four for a platform health review: **interaction failure** (how often a consumer arrives and finds nothing useful), **engagement** (how actively participants contribute and return), **match quality** (how well the platform connects the right producer to the right consumer) and **negative network effects** (congestion, spam and misbehavior that grow with scale).

:::key The diagnostic question
Ask which parts of your customers' value are already created by people outside your company. If the answer is "a lot, by accident," you have a platform you aren't managing. If it's "almost none," decide whether that's a choice or a gap.
:::

### The core interaction

*Platform Revolution* centers platform design on the **core interaction**: the single most important exchange the platform exists to enable. It has three components: the **participants** (a producer and a consumer), the **value unit** (the thing exchanged, such as a listing, an app or a connector) and the **filter** (the mechanism that decides which value units reach which consumers). Choudary put the design rule bluntly in a 2015 interview with MIT's Initiative on the Digital Economy: "Don't start with technology, start with the interaction." He contrasted platforms with light filters, where almost anything gets through, with platforms that apply many complex filters because a bad match is expensive.

The HBR authors add a sequencing rule: launch with one high-value core interaction, then expand to adjacent ones, as Facebook did when it opened from one university to other colleges and then to everyone.

For a B2B product, write the core interaction as a sentence:

> On our platform, **[producer]** creates **[value unit]**; **[filter]** matches it to **[consumer]**, who **[acts on it]**.

If you can't fill in the filter, you probably have an API and not yet a platform.

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 330" role="img" aria-label="Platform map: the owner governs a core interaction in which producers create value units, a filter matches them, and consumers act, with providers delivering access">
  <rect x="200" y="20" width="280" height="56" rx="10" class="box"/>
  <text x="340" y="44" text-anchor="middle" class="t">Owner</text>
  <text x="340" y="63" text-anchor="middle" class="s">Sets architecture, access and rules</text>
  <rect x="30" y="130" width="170" height="80" rx="10" class="box"/>
  <text x="115" y="158" text-anchor="middle" class="t">Producers</text>
  <text x="115" y="178" text-anchor="middle" class="s">Partners, connector</text>
  <text x="115" y="194" text-anchor="middle" class="s">authors, customers</text>
  <rect x="255" y="120" width="170" height="100" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".7"/>
  <text x="340" y="146" text-anchor="middle" class="t" style="fill:var(--a1)">Core interaction</text>
  <text x="340" y="168" text-anchor="middle" class="s">Value unit</text>
  <text x="340" y="186" text-anchor="middle" class="s">passes through</text>
  <text x="340" y="204" text-anchor="middle" class="s">the filter</text>
  <rect x="480" y="130" width="170" height="80" rx="10" class="box"/>
  <text x="565" y="158" text-anchor="middle" class="t">Consumers</text>
  <text x="565" y="178" text-anchor="middle" class="s">Users and teams</text>
  <text x="565" y="194" text-anchor="middle" class="s">who act on it</text>
  <rect x="200" y="262" width="280" height="56" rx="10" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="340" y="286" text-anchor="middle" class="t">Providers</text>
  <text x="340" y="305" text-anchor="middle" class="s">Resellers, MSPs, marketplaces</text>
  <line x1="200" y1="170" x2="255" y2="170" class="ln"/>
  <line x1="425" y1="170" x2="480" y2="170" class="ln"/>
  <line x1="340" y1="76" x2="340" y2="120" class="ln" stroke-dasharray="4 4"/>
  <line x1="340" y1="220" x2="340" y2="262" class="ln" stroke-dasharray="4 4"/>
  <text x="228" y="162" text-anchor="middle" class="s" style="fill:var(--a2)">create</text>
  <text x="452" y="162" text-anchor="middle" class="s" style="fill:var(--a2)">match</text>
  <text x="352" y="102" class="s" style="fill:var(--muted)">governs</text>
  <text x="352" y="246" class="s" style="fill:var(--muted)">delivers access</text>
</svg>
<figcaption>A platform map built from the four ecosystem roles and the core interaction. The owner designs the filter; most of the value units come from outside.</figcaption>
</figure>

## Network effects

### What a network effect is, and what it isn't

NFX, a venture firm that publishes a widely cited taxonomy of network effects, defines one simply: each new user makes the product more valuable to every other user. NFX's own study claims network effects account for about 70% of the value created by technology companies since 1994. That's NFX's analysis rather than independent research, but it explains why "we have network effects" appears in so many pitch decks.

The definition is stricter than it sounds. Several things that make a product better as it grows are not network effects:

- **Scale effects**: fixed costs spread over more customers, so you can invest more in the product. Real advantage, no network.
- **Learning effects**: the vendor learns from usage and improves the product. Real, often valuable, but the benefit doesn't depend on users connecting to each other.
- **Switching costs**: customers stay because leaving is painful. That's lock-in.

Chapter 16 treats each of these as a moat in its own right. Keep them separate from network effects because they behave differently: network effects can compound and tip a market, while scale and learning effects usually flatten out.

### The types that matter in B2B

NFX's "Network Effects Manual" (2021 version) lists 16 types, arranged on a map with the strongest and simplest at the center. You don't need all 16. For enterprise and platform businesses, a handful do most of the work:

| Type | Mechanism | B2B example | How common in enterprise |
|---|---|---|---|
| **Direct (same-side)** | More users of the same kind make it better for each other | Messaging and collaboration tools inside a company | Common inside collaboration products, rare elsewhere |
| **Protocol** | Everyone who adopts a shared standard makes it more valuable to adopt | Network standards; in 2026, agent protocols such as MCP | Growing fast in AI infrastructure |
| **Platform (two-sided)** | Developers build products that run on the platform; more users attract more developers and vice versa | Operating systems, CRM app ecosystems, integration catalogs | The main one for B2B platforms |
| **Marketplace (two-sided)** | More buyers attract more sellers and vice versa | Cloud marketplaces, freelance and services marketplaces | Common in procurement and services |
| **Asymptotic marketplace** | Early supply adds a lot of value, then each extra supplier adds little | Ride hailing, where wait times stop improving | More common than teams admit |
| **Expertise** | The tool gets more valuable as more professionals know how to use it | Spreadsheets, CRM platforms, admin certifications | Underrated in enterprise |
| **Data** | The product improves as usage generates data | Search, fraud detection, AI products | Usually weaker than claimed (see below) |

The first row is a family rather than a single NFX type: NFX groups several same-side effects, protocol effects among them, under its direct category, and groups marketplace, platform and asymptotic marketplace effects as two-sided.

**Direct** network effects are same-side: more of one kind of participant helps others of the same kind. **Indirect** or **cross-side** effects run between sides: more developers help users, and more users attract developers. B2B platforms mostly depend on cross-side effects, so the hard part is usually getting the producers to show up.

**Expertise** deserves more attention than it gets. When an industry's administrators and engineers have spent years learning your product, every hire who already knows it lowers a customer's cost of staying, and every customer that uses it makes the skill more valuable to learn. Certification and public training content feed it.

### Data network effects and their limits

The most overclaimed effect in B2B, and especially in AI products, is the data network effect: "More customers give us more data, which makes the product better, which brings more customers."

Andrei Hagiu and Julian Wright took this loop apart in a 2020 HBR article, "When Data Creates Competitive Advantage." "In most instances," they write, "people grossly overestimate the advantage that data confers." They prefer the term **data-enabled learning** because the loop often involves no network at all. The vendor learns; customers don't benefit from each other. Their analysis suggests asking a set of questions before you count data as an advantage:

- How much value does customer data add compared with what the product does without it?
- Does the marginal value of more data stay high, or does it plateau quickly?
- How fast does the data lose relevance?
- Is the data proprietary, or can competitors get the same thing elsewhere?
- Are the improvements hard to imitate once someone sees them?
- Does learning from one customer improve the product for other customers? (If yes, it's closer to a real network effect.)

Martin Casado and Peter Lauten at Andreessen Horowitz made a parallel argument for enterprise startups in 2019, "The Empty Promise of Data Moats." In their view, most claimed data network effects in enterprise are scale effects that weaken over time, and "defensibility is not inherent to data itself." Their example is a support chatbot: early data covers the common customer intents cheaply, later data costs more and adds less, and coverage plateaus, so a competitor can catch up. They advise building a minimum viable corpus, understanding the long tail, preferring quality over volume, securing proprietary sources and never relying on data alone.

NFX's manual agrees: data network effects are generally weaker than many investors believe, and their strength depends on how central the data is to the product. A credit bureau gets more valuable with more data, but consumers don't generate that data by using the product, so NFX classes it as a scale effect.

:::key The data moat test
Count data as a network effect only when one customer's usage measurably improves the product for other customers, and the improvement keeps growing with scale. Otherwise call it data-enabled learning, measure where it plateaus, and don't build the strategy on it alone.
:::

### Strength, ceilings and leaks

Three ideas from NFX's "Network Effects Bible" help you judge strength.

- **Density and clustering.** A network with many connections per member is stronger than a large but sparse one. NFX advises finding the densest center of your network and expanding outward from it. In B2B, density often sits inside a single account, an industry vertical or a partner's customer base.
- **Asymptotes.** Past some size, more participants add little value for the people already there. Once a responder has connectors for every tool they run, the hundred-and-first connector does nothing for them.
- **Leaks.** Two threats drain value out of a network. **Disintermediation** happens when participants meet on the platform, then transact off it. **Multi-homing** (NFX calls it multi-tenanting) happens when participants join competing networks at the same time because it's cheap to do so.

Hagiu, in a 2013 MIT Sloan Management Review article on multisided platforms, draws a useful line between **switching costs** (the cost of leaving one platform for another) and **multihoming costs** (the cost of staying and also joining a competitor). Multihoming is usually cheap in B2B integrations and marketplaces: a partner can list on three marketplaces, and a customer can connect two observability tools. When it's cheap, winner-take-all outcomes get less likely, and you compete on the quality of each interaction.

### Getting started: the cold start problem

Every network is worthless at size zero. Andrew Chen's *The Cold Start Problem* (2021) describes how networks get going in five stages: the **Cold Start Problem**, the **Tipping Point**, **Escape Velocity**, **Hitting the Ceiling** and **The Moat**.

Three of Chen's ideas matter most for B2B PMs:

- **The atomic network.** The smallest network that is stable and can grow on its own. In consumer products it might be one campus or one city. In B2B it's often one team, one account or one integration pair: a single SRE team with its five core tools connected, say, or one partner's customer base.
- **The hard side.** Chen describes it as the minority of users who create disproportionate value: creators, sellers, app developers. They are the hardest to attract and keep. His advice is to solve a hard problem for the hard side, starting with an underserved niche of it, then expand to adjacent segments. In a developer platform, the hard side is the builders.
- **Anti-network effects.** Early on, a network that's too small drives people away because they can't find what they need, which shrinks it further. A sparse integration catalog does exactly this to an enterprise evaluator.

Annabelle Gawer and Michael Cusumano, writing in MIT Sloan Management Review in 2008 about how companies become platform leaders, describe the lever a B2B platform usually has for breaking a cold start: make the key complements yourself, or create incentives for others to make them. In B2B that often means building the first connectors in-house and starting the partner program once the atomic network works.

:::onramp If platform strategy is new to you
Start with two sentences. First, the core interaction: who produces what, how it's matched, and who consumes it. Second, the hard side: which participants are hardest to attract, and what hard problem you'll solve for them. If you can't write either sentence clearly, the plan isn't ready.
:::

## Openness, governance and envelopment

### Two dials of openness

Van Alstyne, Parker and Choudary describe openness along two dimensions:

- **Open architecture**: how much access outsiders have to the platform's resources, such as APIs, SDKs, data and developer tools.
- **Open governance**: how much outsiders shape the rules of trade and share in the rewards.

The two need to move together. Open the architecture without sharing rewards and builders have the ability but no incentive. Share rewards with a closed architecture and they have the incentive but no ability. The authors note that platforms often launch closed and open over time, and they describe the ideal as **permissionless innovation**: producers can build without asking, and are guaranteed a share of the value they create.

Openness has a cost. The authors cite Chatroulette, where unfettered access produced noise that drove users away. Successful platforms curate through reviews, ratings, certification and enforcement, removing barriers to good participation while keeping bad participation out.

### Four platform decisions

Hagiu's MIT Sloan article frames the strategic choices for any multisided platform as four decisions. They make good section headings for a platform plan:

1. **Number of sides.** Who are the distinct groups you bring together? Adding a side (say, managed service providers alongside direct customers and integration partners) adds value and complexity.
2. **Design.** Which features and services does the platform provide itself, and which does it leave to participants?
3. **Pricing structure.** Which side pays, how much, and which side gets subsidized? Chapter 15 covers pricing mechanics; the platform question is who pays.
4. **Governance rules.** What can participants do, what's forbidden, and how are rules enforced?

Gawer and Cusumano add that platform leaders solve technical problems (architecture, interfaces, how much intellectual property to disclose so others can build) and business problems (which complements to make and which to incentivize). The HBR authors warn that skills for controlling internal resources don't transfer well to nurturing an ecosystem.

### APIs, developer ecosystems and marketplaces

An API is open architecture and nothing more. It becomes a developer ecosystem when the other three pieces arrive: a reason to build (Chen's hard problem for the hard side), a share of the value (the open-governance dial) and a filter that puts builders' work in front of the customers who need it. Treat the developer surface as a product with its own customer, the builder, and its own funnel:

- **Discover.** Can a builder find out what the platform lets them do, and which customers they'd reach?
- **First working call.** How long from sign-up to a call that returns real data in a sandbox? This is the leading indicator of a developer ecosystem, because builders who stall here rarely come back.
- **Ship.** What review, certification and listing steps sit between a working integration and a customer using it, and how long do they take?
- **Earn.** How do builders get paid or rewarded: revenue share, co-sell, leads, placement, a certification badge?
- **Stay.** What do you promise about versioning and deprecation? Builders weigh the cost of rework every time you break an interface.

Gawer and Cusumano's point about selective disclosure applies here: expose enough of the interfaces for others to build valuable complements, and keep the parts that let you hold the platform together. The developer platform brief in this chapter is organized around these questions.

A marketplace adds transactions to the ecosystem, so the HBR health metrics matter more. Interaction failure (a buyer searches and finds nothing that fits) is the cold start showing up in the catalog. Match quality decides whether buyers trust the ranking. Disintermediation is the marketplace's particular leak: once a partner and a customer have met, they can close the next deal directly. You can't stop that entirely, so make staying on the platform worth it through billing, procurement, trust signals and support, and write any rules about steering customers off the platform into the governance policy.

### Envelopment: the B2B threat

Thomas Eisenmann, Geoffrey Parker and Marshall Van Alstyne described **platform envelopment** in a 2011 *Strategic Management Journal* paper. A provider in one platform market enters another by bundling its own functionality with the target's, using the user relationships it already has. The entrant needs a bundle and a shared customer, not a breakthrough. Network effects protect an incumbent against standalone rivals; they offer much less protection against a platform that already owns the customer relationship.

In enterprise software, envelopment is a common way for specialist products to lose. A large suite adds your category as a feature, includes it in a contract the customer already has, and wins on procurement simplicity rather than capability. Chapter 13's competitive analysis should name the platforms that could envelop you, and Chapter 16 covers the defenses.

## Platforms you don't own

### Hosts and complements

When you list on an app store, a hyperscaler marketplace or an AI assistant's directory, you're a producer on someone else's platform. Gawer and Cusumano's term for what you supply is a **complement**: something that makes the host platform more valuable.

Being a good complement is often the right strategy. The host brings distribution, trust and a buying path; the cost is dependency. Four questions frame the tradeoff:

1. **What does the host give us?** Distribution, procurement shortcuts, trust signals, billing, discovery.
2. **What does it take?** Fees, data, rules about what we can do, sometimes the direct customer relationship.
3. **What can change without our consent?** Policies, ranking, fees, technical requirements.
4. **What's our exit and multi-homing plan?** Can we serve the same customers through another host, or directly, if this one changes the deal?

Add a fifth for B2B: **are we a complement the host might envelop?** A host has every incentive to build the features its complements prove valuable.

### App stores and published rules

Apple's App Review Guidelines are probably the best-known published platform governance policy, and a useful structural model even if you never ship a mobile app. Five sections (Safety, Performance, Business, Design and Legal) sit under a principle of a safe place for users and a real chance for developers. The document is living: apps that stop working may be removed, cheating the review can mean expulsion from the developer program, and developers answer for third-party code inside their apps.

The guidelines also show that a host's rules change. As of October 2026, apps on Apple's US storefront may include buttons and links to purchase methods outside Apple's in-app purchase system without applying for a special entitlement, while most other storefronts still require one. If your revenue model depends on a host's rules, those rules are a dependency to track like any other.

### Hyperscaler marketplaces

Cloud marketplaces have become a buying path for enterprise software for an economic reason. Microsoft's September 2025 launch of Microsoft Marketplace, which merged Azure Marketplace and AppSource, made the logic explicit: purchases of eligible solutions count fully toward a customer's Azure consumption commitment. A buyer with a pre-committed cloud budget can buy your product without finding new money. Microsoft also described resale-enabled private offers that let a vendor authorize channel partners to sell on its behalf.

AWS added a category for AI agents and agent tools to AWS Marketplace in July 2025, with listings that can indicate support for agent protocols such as MCP and A2A. Salesforce launched AgentExchange in March 2025 as a marketplace for prebuilt agent actions, templates and components, with more than 200 partners at launch. The pattern: the large platforms are turning agent capabilities into catalog items, and protocol support has become a filter buyers use.

### AI model and assistant platforms

The newest platforms you don't own are the AI models and assistants your product builds on or plugs into. You may depend on a model provider for the intelligence inside your product (Chapter 31 covers the model and vendor register for that dependency). And you may publish integrations into AI assistants that customers already use, through directories that, as of October 2026, accept MCP-based integrations subject to review requirements.

Both are host relationships with one added risk: the host moves fast. Model versions deprecate, directory rules change, and what your product does may appear in the assistant itself. Put each AI platform on your platform map with an owner and an exit plan.

## How to apply it

Here's a method for building a platform strategy for an existing B2B product over about six weeks. It produces five artifacts: a platform map, a network effects assessment, an ecosystem and partner strategy, a developer platform brief and a platform governance policy.

**Weeks 1 and 2: Map what exists.**

1. **Inventory the outsiders.** List every party outside your company that creates value in your product today: partners, connector authors, resellers, MSPs, integrators, customers who share runbooks. For each, note what they produce, who consumes it and what they get. Pull the evidence (integration usage, partner-sourced revenue, marketplace transactions) rather than relying on the partner team's slide.
2. **Draw the platform map.** Assign each party to a role: owner, provider, producer or consumer. Write the core interaction as one sentence, including the filter. Then list the platforms you depend on (marketplaces, clouds, model providers, AI assistants) and the platforms that could envelop you.
3. **Write the four decisions as they stand today.** Number of sides, design, pricing structure and governance rules. Note which were decided deliberately and which just happened.

**Weeks 3 and 4: Test the network effects.**

4. **List every claimed network effect.** Take them from strategy decks, board materials and sales pitches. For each, name the NFX type, the sides involved and the mechanism: who gets more value when whom joins?
5. **Find the evidence.** For a cross-side effect, does an account's usage rise when more relevant integrations exist, and do producers arrive faster as the customer base grows? For a data effect, does customer A's usage measurably improve the product for customer B, and where does that plateau? Write a verdict for each: real network effect, data-enabled learning, scale effect, switching cost or aspiration.
6. **Place yourself on Chen's five stages.** Name the atomic network and the hard side. Check the four HBR health metrics: interaction failure, engagement, match quality and negative network effects.

**Week 5: Decide the stance.**

7. **Choose host, complement or both, platform by platform.** For your own platform, decide how far to open the architecture and governance, and in what order. For each platform you depend on, answer the five host questions and write the exit or multi-homing plan.
8. **Write the ecosystem and partner strategy.** Segment partners, define the value exchange for each segment and pick three to five metrics.
9. **If you're opening to builders, write the developer platform brief.** Target builder, the hard problem you'll solve for them, surfaces, access tiers, reward model, versioning and deprecation policy, success metrics.

**Week 6: Govern and commit.**

10. **Draft the platform governance policy.** Participant obligations, review and certification, data and security rules, quality filters, an enforcement ladder, appeals, and how much notice you give before changing the rules.
11. **Review with your leadership and the partner organization.** Record the openness decision, the network effect verdicts and the governance policy in the decision log. Agree on which platform metrics go into the quarterly business review (Chapter 29).

Revisit the network effects assessment twice a year. Asymptotes arrive and multi-homing rises as a product grows, so an effect that was real at one size can flatten at the next.

:::leader For product leaders
Platform decisions cut across product, partnerships, sales and legal, so they tend to be made piecemeal by whoever is closest to the deal. Make one leader accountable for the platform map and governance policy across the portfolio. If three products each run their own partner program with different terms, partners will notice before you do.
:::

## The AI lens

### Agent ecosystems are platforms

In 2026 the biggest platform shift for B2B products is agent ecosystems: AI agents that discover and call tools, and increasingly call each other. The plumbing for both is now governed as shared infrastructure.

**MCP, agent to tool.** Anthropic introduced the Model Context Protocol in November 2024 as an open standard for connecting AI assistants to the systems where data lives, replacing a custom integration for every pairing of assistant and data source. On 9 December 2025, Anthropic donated MCP to the newly formed Agentic AI Foundation (AAIF), a directed fund under the Linux Foundation. The foundation's founding projects were MCP, Block's goose and OpenAI's AGENTS.md, and its platinum members include the major cloud and AI vendors. At the time of the donation, Anthropic reported more than 10,000 active public MCP servers and more than 97 million monthly SDK downloads, with clients including ChatGPT, Cursor, Gemini, Microsoft Copilot and VS Code.

**A2A, agent to agent.** The Agent2Agent protocol, created by Google and announced in April 2025, became a Linux Foundation project in June 2025. Its stable v1.0 specification arrived in early 2026, with signed Agent Cards (the descriptions agents publish about themselves) and support for multi-tenancy. In August 2026 the A2A project announced it had joined the AAIF as a growth-stage project, reporting backing from more than 150 organizations. The project describes MCP as the vertical layer (an agent reaching down to tools and data) and A2A as the horizontal layer (agents working with other agents), and calls the two complementary.

**Registries and marketplaces.** Discovery is layering the way app stores did. The MCP Registry, previewed in September 2025, is an open catalog of public MCP servers that anyone can build sub-registries on top of: public ones that act as curated marketplaces for particular clients, and private ones that enterprises run internally. Hyperscaler and SaaS marketplaces now list agents and agent tools, and AI assistant directories accept MCP-based integrations subject to review.

In NFX's terms, MCP and A2A are **protocol network effects**: each product that adopts them makes adopting them more valuable for everyone else. Anthropic's donation is a clear case of the HBR authors' open-governance lever. A platform owner gave up control of a protocol to grow the protocol's network effect, and the competition for value moves up the stack to models, clients and services.

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 300" role="img" aria-label="Agent ecosystem layers: A2A connects agents horizontally, MCP connects each agent vertically to tools and data, registries and marketplaces handle discovery">
  <rect x="20" y="20" width="640" height="44" rx="10" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="340" y="47" text-anchor="middle" class="t">Discovery: registries, private catalogs, marketplaces, assistant directories</text>
  <rect x="40" y="100" width="170" height="60" rx="10" class="box"/>
  <text x="125" y="128" text-anchor="middle" class="t">Agent A</text>
  <text x="125" y="146" text-anchor="middle" class="s">e.g. ITSM agent</text>
  <rect x="255" y="100" width="170" height="60" rx="10" fill="var(--a1)" fill-opacity=".12" stroke="var(--a1)" stroke-opacity=".7"/>
  <text x="340" y="128" text-anchor="middle" class="t" style="fill:var(--a1)">Your agent</text>
  <text x="340" y="146" text-anchor="middle" class="s">host and complement</text>
  <rect x="470" y="100" width="170" height="60" rx="10" class="box"/>
  <text x="555" y="128" text-anchor="middle" class="t">Agent C</text>
  <text x="555" y="146" text-anchor="middle" class="s">e.g. assistant</text>
  <line x1="210" y1="130" x2="255" y2="130" class="ln"/>
  <line x1="425" y1="130" x2="470" y2="130" class="ln"/>
  <text x="232" y="122" text-anchor="middle" class="s" style="fill:var(--a2)">A2A</text>
  <text x="448" y="122" text-anchor="middle" class="s" style="fill:var(--a2)">A2A</text>
  <line x1="125" y1="160" x2="125" y2="210" class="ln"/>
  <line x1="340" y1="160" x2="340" y2="210" class="ln"/>
  <line x1="555" y1="160" x2="555" y2="210" class="ln"/>
  <text x="135" y="190" class="s" style="fill:var(--a3)">MCP</text>
  <text x="350" y="190" class="s" style="fill:var(--a3)">MCP</text>
  <text x="565" y="190" class="s" style="fill:var(--a3)">MCP</text>
  <rect x="20" y="210" width="640" height="50" rx="10" class="box"/>
  <text x="340" y="240" text-anchor="middle" class="t">Tools and data: observability, ticketing, chat, CI/CD, cloud</text>
  <text x="340" y="288" text-anchor="middle" class="s" style="fill:var(--muted)">MCP is the vertical layer; A2A is the horizontal layer; discovery sits above both</text>
</svg>
<figcaption>The agent ecosystem as a platform stack. Your product can host connectors and agents, publish itself as a complement into other hosts, or both.</figcaption>
</figure>

### Host, complement or both

The agent ecosystem forces the host and complement choice on every B2B product:

- **Be a host.** Agents and connectors from outside plug into your product. You need a filter (which ones you trust), governance (what they may do) and a cold start plan for the builders.
- **Be a complement.** Publish your capabilities as an MCP server or an A2A agent so other hosts (assistants, ITSM suites, cloud agent runtimes) can use them. You get distribution through someone else's network, and you take on the host dependency.
- **Do both.** Decide, platform by platform, which role you're playing and what you expect from it.

Publishing an MCP server is now a distribution decision more than a bet on one vendor, because the protocol is neutrally governed and supported by many clients. It also hands buyers a new question to ask: is your server in our private registry, with the scopes our security team approved? Plan for that question in the governance policy and the security pack.

Protocol governance also gives you a model for your own. The MCP specification published on 28 July 2026 adopted a formal feature lifecycle and deprecation policy with a minimum twelve-month deprecation window. A published deprecation policy tells builders how long their work will keep running. If you want producers to invest in your platform, make them the same kind of promise.

Choudary's more recent book, *Reshuffle*, argues that AI lowers coordination costs and so changes firm boundaries and where value gets captured. Applied to agent ecosystems, that suggests the agent that coordinates the others, deciding which tool or agent handles each step, holds a strong position. If someone else owns that coordinating agent, watch it for envelopment.

### Building AI-powered platform products

Three platform questions are specific to AI products. First, "our agent learns from every customer" is a data-enabled learning claim at best; data residency and customer contracts often forbid the cross-customer learning that would make it a network effect. Second, when an outside connector or agent acts through your product, its failure looks like yours, so governance has to cover what third-party tools may do as well as what they may read. Third, if each interaction costs you inference, subsidizing a side costs more than on a pure software platform; model it before promising free usage to builders (Chapters 15 and 31 cover the cost side).

### Doing the work with AI

A harness connected to your CRM, partner portal, marketplace listings, analytics and integration logs can gather most of the evidence for a network effects assessment. Ask it questions:

- Which integrations are used weekly by the most accounts, and which are installed but idle?
- Do accounts with more active integrations retain or expand at different rates, after accounting for size?
- Which partner-sourced deals closed, through which marketplace, and against which cloud commitments?
- How long did the last ten new connectors take from first contact to first working call?

Have it draft the assessment table with a cited source for every row and a verdict column, then argue with it. Models write "this creates a flywheel" fluently, so ask for the opposite case on each claimed effect and the evidence that would prove it wrong.

AI also helps with governance: finding gaps in a draft policy or enforcement ladder, or checking a partner's submission against certification criteria. Treat the output as a first draft. Governance decisions affect partners' livelihoods, and someone accountable has to make them.

:::ai The one-line rule
AI can gather the evidence for a network effect and draft the case for and against it. Whether the effect is real is settled by evidence from your own customers and builders.
:::

## The Beacon case: Beacon's platform decision

:::example Where Beacon starts
Beacon connects to customers' observability, ticketing, chat, CI/CD and cloud tools, partly through MCP servers. The strategy deck claims "network effects from our Learn loop" and treats the integration catalog as a sales checkbox. Meanwhile, the case's oldest strategic tension is unresolved: build on Northlight Observe data, which is an advantage, or stay tool-agnostic, which is a larger market. In discovery (Chapter 01), two customers who had left Beacon said they switched to an AIOps feature bundled into a platform they already paid for. You decide to answer the tension as a platform question.
:::

**The platform map.** You draw the four roles. Northlight is the owner. The producers are connector and agent builders (Northlight's own teams, observability and ticketing vendors, MSPs such as Leo's who write runbooks, and customers' SREs who author their own). The consumers are responders such as Dana and Priya. The providers are the MSPs and resellers who deliver Beacon to the mid-market. The core interaction, written as a sentence: *A connector or runbook author creates an integration or runbook step; Beacon's diagnosis agent matches it to a live incident; the responder acts on it.* The filter is Beacon's diagnosis agent plus the approval gate. Once it's written down, the team sees that the quality of the filter is most of the product.

**The network effects assessment.** You list four claimed effects and give each a verdict:

| Claimed effect | NFX type | Mechanism | Verdict |
|---|---|---|---|
| More connectors make Beacon more useful; more customers attract connector builders | Platform (cross-side) | Responders get coverage of more of their stack; builders get access to Beacon's customer base | Real but early. Outside builders have barely started. |
| The Learn loop improves diagnosis as more incidents resolve | Data | Resolved incidents feed retrieval and evals | Mostly data-enabled learning within each customer. Cross-customer transfer is limited by data residency and contracts, and the gains are likely to plateau. |
| SREs trained on Beacon runbooks prefer it at their next job | Expertise | Skills travel with people | Plausible, unmeasured. Worth seeding through certification. |
| Leo's 60 customers share runbooks | Two-sided, inside one MSP | Each runbook Leo's team writes serves every tenant; each new tenant makes runbooks more worth writing | Real and dense. A candidate atomic network. |

The "Learn loop network effect" becomes data-enabled learning: a real advantage you'll measure but won't build the strategy on. The cross-side effect is the one to build.

**Cold start.** The atomic network is one platform team (Priya's 40 people) with its five core tools connected, or one MSP with its tenants. The hard side is the connector builders and MSPs. Following Gawer and Cusumano, Northlight builds the first 20 connectors itself, prioritized by which tools appear most in customer incidents, and opens a partner program only once those 20 are used weekly.

**The openness decision.** The Observe-versus-agnostic tension turns out to be an openness question. Observe-only protects a data advantage that, on inspection, is data-enabled learning. Opening the architecture to any observability tool through MCP connectors grows the market and the cross-side effect. You recommend an open architecture with curated governance: certified connectors, scoped credentials and Beacon's human approval gate for any action, with full autonomy only for low-risk actions the customer allowlists. Observe customers still get the deepest integration, which keeps the advantage without making it a wall.

**Platforms Beacon doesn't own.** You map three host relationships:

- **Hyperscaler marketplaces**, so Marcus can buy Beacon against existing cloud commitments and Leo can buy through a distributor's marketplace. Pricing per resolved incident needs metering that works through each marketplace's billing.
- **A Beacon MCP server**, so responders can ask about incidents from the AI assistants they already use, listed in the public registry and in customers' private registries with scopes documented for Sam.
- **A Beacon agent exposed over A2A**, so an ITSM agent (including Northlight Desk's) can hand off diagnosis and receive a cited root cause back.

The envelopment risk goes on the map too: the large observability platforms named in the competitive analysis, and cloud providers' own operations agents, could bundle a "good enough" incident agent into contracts customers already have.

**Governance.** The hallucinated root cause incident, where a customer rolled back the wrong service, shapes the policy. Any third-party connector that feeds diagnosis must pass certification; connectors that return bad data move through an enforcement ladder from warning to suspension to delisting; and every third-party runbook action that touches production runs with least privilege, audit logging and the approval gate. Sam reviews the policy before it's published to partners.

**The decision.** Leadership approves the open architecture, the 20-connector cold start, the three host listings and the governance policy. The board deck replaces "network effects from our Learn loop" with two lines: a cross-side platform effect being built, and data-enabled learning being measured. You add three platform metrics to the quarterly review: weekly active integrations per account, connector-sourced diagnosis acceptance rate and time for a partner to build a first working connector.

## Product 360 artifacts

```template id="14-platform-map" title="Platform map"
# Platform map · [Product] · v[n] · [Date]

**Owner:** [PM]   **Reviewed with:** [partnerships lead, architect]   **Next review:** [Date]

## Ecosystem roles
| Role | Who (named parties or segments) | What they create or do | What they get today | Evidence |
|---|---|---|---|---|
| Owner | [us] | Architecture, access, rules | | |
| Providers | [resellers, MSPs, marketplaces] | Deliver access to customers | | |
| Producers | [partners, connector authors, customers who share content] | Create value units | | |
| Consumers | [users and teams] | Act on value units | | |

## Core interaction
On our platform, [producer] creates [value unit]; [filter] matches it to [consumer], who [acts on it].

- Value unit:
- Filter (how the right value unit reaches the right consumer):
- What a failed interaction looks like:

## Adjacent interactions (later)
1.
2.

## The four platform decisions, as they stand
| Decision | Today (deliberate or accidental?) | Proposed |
|---|---|---|
| Number of sides | | |
| Design (what we provide vs what participants provide) | | |
| Pricing structure (who pays, who is subsidized) | | |
| Governance rules | | |

## Platforms we depend on (we are a complement)
| Host platform | What it gives us | What it takes | What can change without our consent | Exit or multi-homing plan |
|---|---|---|---|---|
| | | | | |

## Platforms that could envelop us
| Platform | Shared customer relationship | Bundle they could offer | Early warning signal | Our defense (see moats, Chapter 16) |
|---|---|---|---|---|
| | | | | |
```

```template id="14-network-effects-assessment" title="Network effects assessment"
# Network effects assessment · [Product] · [Date]

**Owner:** [PM]   **Evidence sources:** [analytics, CRM, partner portal, marketplace data]

## Claimed effects
| # | Claimed effect (as stated in our materials) | NFX type | Sides involved | Mechanism: who gets more value when whom joins? | Evidence today (metric, value, source) | Density and clustering | Limits (asymptote, multi-homing, disintermediation) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |

Verdict options: real network effect / data-enabled learning / scale effect / switching cost / aspiration (no evidence yet).

## Data moat test (for any data claim)
| Question | Answer | Evidence |
|---|---|---|
| How much value does customer data add compared with the product without it? | | |
| Does the marginal value of more data stay high, or plateau? Where? | | |
| How fast does the data lose relevance? | | |
| Is the data proprietary, or available to competitors? | | |
| Are the improvements hard to imitate? | | |
| Does one customer's data improve the product for other customers? Are we allowed to use it that way? | | |

## Cold start position
- Stage (Cold Start Problem / Tipping Point / Escape Velocity / Hitting the Ceiling / The Moat):
- Atomic network (smallest stable network that grows on its own):
- Hard side (participants who create disproportionate value and are hardest to attract):
- Hard problem we solve for the hard side:

## Platform health
| Metric | Definition for our platform | Current value | Trend |
|---|---|---|---|
| Interaction failure | | | |
| Engagement | | | |
| Match quality | | | |
| Negative network effects (congestion, spam, misbehavior) | | | |

## What changes in our strategy and board story
[One paragraph: which effects we will build on, which we will stop claiming, what we will measure.]
```

```template id="14-ecosystem-partner-strategy" title="Ecosystem and partner strategy"
# Ecosystem and partner strategy · [Product] · [Date]

**Owner:** [PM]   **Partner organization lead:** [Name]   **Decision maker:** [Name]

## Stance by platform
| Platform | Our role (host / complement / both) | Why | Commitment level (explore / invest / core) |
|---|---|---|---|
| Our own platform | Host | | |
| [Marketplace] | Complement | | |
| [AI assistant or agent runtime] | Complement | | |

## Partner segments and value exchange
| Segment | Examples | What they give us | What they get | Terms (rev share, co-sell, listing, certification) | Owner |
|---|---|---|---|---|---|
| Technology integrations | | | | | |
| Marketplaces and distributors | | | | | |
| Channel (resellers, MSPs) | | | | | |
| Systems integrators | | | | | |
| Agent and connector builders | | | | | |

## Openness plan
- Architecture (what outsiders can access now, and next):
- Governance (what say and share of value outsiders get now, and next):
- Sequence (what opens when, and the trigger for each step):

## Dependency and exit plan
| Host | Revenue or pipeline share through it | Biggest rule-change risk | Multi-homing or direct alternative |
|---|---|---|---|
| | | | |

## Metrics (three to five)
| Metric | Target | Review cadence |
|---|---|---|
| | | |

## Decisions and open questions
-
```

```template id="14-developer-platform-brief" title="Developer platform brief"
# Developer platform brief · [Product] · v[n] · [Date]

**Owner:** [PM]   **Engineering lead:** [Name]   **Developer relations:** [Name]

## Target builder (the hard side)
- Who they are (partner type, role, skill level):
- The hard problem we solve for them:
- What they use today instead:

## Job story
When [situation], I want to [motivation], so I can [expected outcome].

## Surfaces
| Surface | Purpose | Status | Audience |
|---|---|---|---|
| Public API | | | |
| SDKs | | | |
| MCP server (agent to tool) | | | |
| A2A agent and Agent Card (agent to agent) | | | |
| Sandbox and test data | | | |

## Access tiers
| Tier | Who qualifies | What they can do | Review required? |
|---|---|---|---|
| Open | | | |
| Certified partner | | | |
| Strategic | | | |

## Reward model
How builders share in the value they create: [listing, revenue share, co-sell, lead sharing, certification badge, marketplace placement].

## Versioning and deprecation
- Versioning scheme:
- Minimum deprecation notice: [period]
- How breaking changes are announced:
- Support window for old versions:

## Registry and marketplace listings
Where builders' work, and our own servers and agents, will be discoverable: [public registries, private enterprise registries, marketplaces].

## Success metrics
| Metric | Definition | Target |
|---|---|---|
| Time to first working integration | | |
| Active builders (shipped in last 90 days) | | |
| Third-party integrations used weekly | | |
| Share of customer value from third-party integrations | | |

## Risks and open questions
-
```

```template id="14-platform-governance-policy" title="Platform governance policy"
# Platform governance policy · [Platform] · v[n] · Effective [Date]

**Policy owner:** [Name]   **Approved by:** [product, security, legal]   **Next review:** [Date]

## Purpose and principles
[Two or three sentences: what the platform is for, and the balance it strikes between users' safety and builders' opportunity.]

## Scope
Who this applies to: [connector authors, agent builders, marketplace sellers, resellers].

## 1. Safety and security
- Least-privilege access: [scopes allowed by default; scopes needing review]
- Actions on customer systems: [which require human approval; which may run autonomously and under what customer allowlist]
- Audit logging: [what must be logged and retained]
- Data handling: [residency, retention, training use]
- Responsibility for third-party code and models inside a submission:

## 2. Performance and quality
- Certification criteria: [functional tests, accuracy thresholds, uptime]
- Quality filters: [how listings are ranked and matched]
- What happens when a submission stops working:

## 3. Business terms
- Fees and revenue share:
- Pricing and billing rules (including metering for usage-based pricing):
- Rules on steering customers off the platform:

## 4. Design and experience
- Required disclosures to users (what the integration does, what it can access):
- Branding rules:

## 5. Legal and compliance
- Regulatory obligations passed to participants (for AI features, see Chapter 33):
- Contract terms and liability:

## Review process
| Stage | Who reviews | Target time |
|---|---|---|
| Submission | | |
| Security review | | |
| Certification | | |

## Enforcement ladder
| Level | Trigger | Action | Notice given |
|---|---|---|---|
| 1. Warning | | | |
| 2. Suspension | | | |
| 3. Delisting | | | |
| 4. Removal from program | | | |

## Appeals
How a participant appeals, who decides and how fast.

## Changes to this policy
Minimum notice before a change takes effect: [period]. Where changes are announced: [channel]. Change log below.

| Version | Date | Change | Reason |
|---|---|---|---|
| | | | |
```

## Prompts

```prompt title="Draft a platform map from company data"
Goal: Get a first platform map built from evidence, not from the partner team's slide.
Paste in (or connect the harness to): the partner list, integration usage data, marketplace transaction reports, reseller and MSP account lists, and the current product strategy. Use only tools approved for customer and partner data.

Build a platform map for [product] using the four ecosystem roles: owner, providers, producers and consumers.

1. Assign every party in the material to one or more roles. For each, say what they create or do, what they get today, and cite the source.
2. Write the core interaction as one sentence: "[producer] creates [value unit]; [filter] matches it to [consumer], who [acts on it]." If the material doesn't show a filter, say so.
3. List the platforms we depend on as a complement, with what each gives us and what it takes.
4. List platforms that share our customer relationships and could bundle our function into their offer.
5. State the four platform decisions (number of sides, design, pricing structure, governance rules) as they appear today, and mark each as deliberate or accidental based on the evidence.

Don't invent partners, usage numbers or terms. Write "No evidence" where the material is silent.

Check the output: confirm three of the cited figures against the source reports. Check that the filter is a real mechanism in the product, not a marketing phrase.
```

```prompt title="Test our network effect claims"
Goal: Separate real network effects from scale effects, learning and aspiration.
Paste in: every network effect claim from our strategy, board and sales materials, plus the analytics the harness can reach (account usage, integration usage, retention and expansion by cohort). Use only tools approved for customer data.

Act as a skeptical board member reviewing the network effect claims for [product].

For each claim:
1. Name the network effect type (direct, protocol, two-sided platform, marketplace, asymptotic marketplace, expertise, data) and the sides involved.
2. State the mechanism: who gets more value when whom joins?
3. Propose the evidence that would confirm it and the evidence that would refute it, then report what our data shows, with sources.
4. For any data claim, answer: does one customer's usage improve the product for other customers, are we allowed to use the data that way, and where does the improvement plateau?
5. Give a verdict: real network effect, data-enabled learning, scale effect, switching cost or aspiration.
6. Argue the opposite of your verdict in two sentences.

Don't describe anything as a flywheel unless the evidence shows each step.

Check the output: for every "real network effect" verdict, look at the cited evidence yourself. If the evidence is an aggregate correlation, ask whether account size explains it.
```

```prompt title="Plan the cold start for a builder ecosystem"
Goal: Find the atomic network and a hard problem to solve for the hard side.
Paste in: the platform map, a list of integrations customers request most (from support tickets, sales notes and lost-deal reasons), and current integration usage. Use only tools approved for customer data.

For [product], help me plan how to start the producer side of our platform.

1. Propose three candidate atomic networks: the smallest set of customers, builders and integrations that would be stable and grow on its own. For each, say why it's dense.
2. Identify the hard side: which participants create disproportionate value and are hardest to attract?
3. For the hard side, propose two hard problems we could solve for them, starting with an underserved niche.
4. List the complements we should build ourselves before opening to partners, ranked by how often they appear in customer demand, with sources.
5. Define the signal that would tell us the atomic network works and it's time to open the partner program.

Check the output: are the "build ourselves" complements backed by demand evidence, or by what's easy to build? Confirm the hard side is the group that's actually scarce today.
```

```prompt title="Decide host, complement or both for an agent ecosystem"
Goal: Make a deliberate choice about MCP servers, A2A agents and agent marketplaces.
Paste in: the platform map, the product's main capabilities, customers' requests for AI assistant or agent integrations, the security team's requirements, and the list of agent marketplaces and assistant directories we're considering. Use an approved tool for customer requests and security requirements.

For [product], recommend whether to act as a host, a complement or both in the agent ecosystem.

1. List the capabilities other agents and assistants would most want to call, with evidence from customer requests.
2. For each, say whether it should be exposed as an MCP server (agent to tool), an A2A agent (agent to agent), or neither yet, and why.
3. For each marketplace or directory under consideration, answer: what it gives us, what it takes, what can change without our consent, and our exit plan.
4. Identify where we'd be a complement that the host could later absorb into its own product.
5. List the governance requirements a customer's security reviewer will ask about (scopes, audit logs, approval gates, registry listing) and which we already meet.

Base claims about protocols and marketplaces only on the documents I provide. If something isn't covered, say "needs verification."

Check the output: verify any statement about protocol versions, governance or marketplace terms against the current official documentation before it goes into a decision.
```

```prompt title="Draft a platform governance policy"
Goal: Produce a first draft of governance rules that builders can read and security can approve.
Paste in: the platform map, the developer platform brief, the security team's requirements for third-party access, recent incidents involving third-party integrations, and any existing partner terms. Incident and partner details are confidential, so use an approved tool.

Draft a platform governance policy for [platform] with these sections: purpose and principles; scope; safety and security; performance and quality; business terms; design and experience; legal and compliance; review process; enforcement ladder (warning, suspension, delisting, removal); appeals; and how much notice we give before changing the policy.

Rules:
- Tie every security rule to a requirement in the material, and cite it.
- For any third-party action on customer systems, state whether it needs human approval and who can allowlist autonomous actions.
- Make every enforcement step specific: trigger, action, notice.
- Flag any rule that would be hard for a small partner to meet.

Check the output: have legal and security review it before publishing. Read the enforcement ladder from a partner's point of view: is each trigger objective enough that two reviewers would reach the same decision?
```

```prompt title="Stress-test an envelopment threat"
Goal: Understand how a larger platform could bundle your function, and what would defend against it.
Paste in: the competitive analysis, win and loss notes that mention bundling, and public announcements from the platforms that share our customers. Use only approved tools for deal data.

For [product], analyze the envelopment threat from [platform].

1. Describe the shared customer relationship: which buyers, which contracts, which budget lines.
2. Describe the bundle they could offer and what "good enough" would look like to our buyer.
3. List the evidence from win and loss notes that bundling has already cost us deals, with sources.
4. Identify which of our advantages survive a bundle (network effects, data-enabled learning, expertise, integrations, trust) and which don't.
5. Propose three responses, from cheapest to most ambitious, and the signal that would trigger each.

Don't assume the competitor's roadmap. Base it on public announcements and our own deal evidence.

Check the output: confirm the cited deals. Ask whether the proposed defenses are things buyers have said they value, or things we wish they valued.
```

## Anti-patterns

:::warn The flywheel slide
A circular diagram with arrows labeled "more customers, more data, better product" appears in the board deck, with no evidence for any arrow. Most of these are data-enabled learning or scale effects. Test each arrow, and keep only the ones your data supports.
:::

:::warn Opening the API and calling it a platform
The team publishes an API and waits for builders. Nobody comes, because the architecture is open but the rewards aren't. Builders need a reason as well as a way: distribution, revenue or customers they can't reach otherwise.
:::

:::warn Opening everything at once
A marketplace launches with no review, no certification and no enforcement. Low-quality submissions crowd out good ones, and an integration that misbehaves in production becomes your incident. Curate early. Open in steps, with governance ready before each step.
:::

:::warn Ignoring the hard side
The platform plan is all about end users, because they're the customers. The builders, partners and MSPs who create the value units get a portal and a logo program. Solve a hard problem for the hard side, or the cross-side effect never starts.
:::

:::warn Treating a host as a channel you control
Most of a product's new pipeline comes through one marketplace or one suite's catalog, and nobody owns the dependency. Then the host changes its fees, ranking or rules, or ships your feature itself. Every host belongs on the platform map with an exit or multi-homing plan.
:::

:::warn Changing the rules without notice
A platform changes its terms or breaks an API with a few weeks' warning. Builders who lose work once stop investing. Publish a deprecation policy and a minimum notice period, and keep to them.
:::

## Checklist

- [ ] The platform map names the owner, providers, producers and consumers, with evidence for each.
- [ ] The core interaction is written as one sentence, including a real filter.
- [ ] The four platform decisions (sides, design, pricing structure, governance) are written down and marked deliberate or accidental.
- [ ] Every claimed network effect has a type, a mechanism, evidence and a verdict.
- [ ] Every data claim has passed or failed the data moat test, and the board story matches the verdict.
- [ ] The atomic network and the hard side are named, with a hard problem the platform solves for the hard side.
- [ ] Openness of architecture and governance move together, with a sequence and a trigger for each step.
- [ ] Every platform you depend on has an owner, a dependency note and an exit or multi-homing plan.
- [ ] Envelopment threats are named, with early warning signals.
- [ ] For agent ecosystems, the host, complement or both decision is recorded per platform, with MCP and A2A choices and registry plans.
- [ ] The developer platform brief includes a published versioning and deprecation policy.
- [ ] The platform governance policy covers security, quality, business terms, enforcement, appeals and change notice, and security and legal have approved it.
- [ ] Platform health metrics (interaction failure, engagement, match quality, negative network effects) are in the quarterly review.

## Key takeaways

- Most B2B products are hybrids: a pipeline at the core and a platform around it. Find out how much of your customers' value outsiders already create, then decide whether to manage that on purpose.
- Start with the core interaction: who produces what, how it's filtered and who acts on it. If you can't name the filter, you don't have a platform yet.
- Classify every claimed network effect by type and test it with evidence. In enterprise, cross-side platform effects and expertise are often real; data network effects are usually data-enabled learning that plateaus.
- Cold start is solved on the hard side. Find the atomic network, build the first complements yourself, and open to builders once that small network works.
- Open architecture and open governance have to move together, with curation from the start. Builders need both the ability and a reason to build.
- The platforms you don't own are part of your strategy. Map each host, what it gives and takes, what it can change without you, and how you'd leave. Watch for envelopment by platforms that share your customers.
- MCP and A2A, now governed under the Agentic AI Foundation, turn agent ecosystems into protocol networks. Decide platform by platform whether you're a host, a complement or both.
