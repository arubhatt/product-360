# Research notes: Chapter 33, Responsible AI and Regulation for PMs

Status: complete (2026-10-30). Researched 2026-10-30. Not legal advice. Tags: [V] verified on primary or authoritative consolidated text; [S] secondary only; [U] unverified, prior knowledge.

Constraint note: the shared web-search budget for this run was exhausted before this chapter started, so verification used direct fetches of known primary URLs only. Facts from research-ch31.md section 7 are carried forward with their original tags.

## (b) Verified facts (running log)

### EU AI Act operative dates after the Digital Omnibus (Regulation (EU) 2026/1744)
- EUR-Lex fetch of eur-lex.europa.eu/eli/reg/2026/1744/oj returned an empty page on 2026-10-30. Title confirmed earlier in research-ch31 [V].
- Article 26 (deployer obligations) consolidated text on artificialintelligenceact.eu states, under Article 113, application from 2 December 2027 for Annex III systems and 2 August 2028 for Annex I systems. https://artificialintelligenceact.eu/article/26/ (fetched 2026-10-30) [S, consolidated text by Future of Life Institute, reflects the Omnibus].
- Article 50 transparency applies from 2 August 2026 per Article 113. https://artificialintelligenceact.eu/article/50/ (fetched 2026-10-30) [S].

### Article 50 transparency, who does what (Regulation (EU) 2024/1689) [S, consolidated text]
- 50(1) Provider: systems interacting directly with people must be designed so people know they are dealing with AI, unless obvious.
- 50(2) Provider: synthetic audio, image, video or text output marked in a machine-readable, detectable format, as far as technically feasible. Assistive editing that does not substantially alter input is excluded.
- 50(3) Deployer: inform people exposed to emotion recognition or biometric categorisation.
- 50(4) Deployer: disclose deep fakes; disclose AI-generated text published to inform the public on matters of public interest unless it had human review and editorial responsibility.

### Article 26 deployer obligations for high-risk systems [S, consolidated text]
1 use per provider instructions; 2 human oversight by competent people with authority; 4 input data relevant and representative where the deployer controls it; 5 monitor, inform provider and authority of risk, suspend use, report serious incidents; 6 keep logs under its control for at least six months; 7 employers inform workers and representatives before workplace use; 9 use provider's Article 13 information for DPIAs; 11 inform people subject to Annex III decisions; 12 cooperate with authorities.

### US: Colorado
- SB24-205 "Consumer Protections for Artificial Intelligence" signed 2024-05-17; the legislature page lists duties from 2026-02-01 and does not show later amendments. https://leg.colorado.gov/bills/sb24-205 (fetched 2026-10-30) [V for original law only].
- SB25B-004 "Increase Transparency for Algorithmic Systems" signed 2025-08-28, moved SB24-205 obligations to **2026-06-30**. https://leg.colorado.gov/bills/sb25b-004 (fetched 2026-10-30) [V]. Status after 2026-06-30 (whether the 2026 regular session amended, delayed again or let it take effect) NOT verified: see flags.

### EU AI Act Article 113 consolidated dates [S, artificialintelligenceact.eu, fetched 2026-10-30; matches research-ch31 and EPRS]
- 2025-02-02 Chapters I and II (definitions, AI literacy, prohibitions).
- 2025-08-02 notified bodies, GPAI (Chapter V), governance, penalties except Art. 101.
- 2026-07-27 Arts. 102 to 110 (amendments to other EU acts).
- 2026-08-02 general application, including Art. 50 transparency and Art. 101 GPAI fines.
- 2026-12-02 new Art. 5 prohibitions (points (ba), (bb); non-consensual intimate imagery and CSAM generation).
- 2027-12-02 high-risk under Art. 6(2) and Annex III.
- 2028-08-02 high-risk under Art. 6(1) and Annex I.
https://artificialintelligenceact.eu/article/113/

### Role switching, Article 25(1) [S, consolidated text]
A deployer, distributor or importer becomes the provider of a high-risk system if it (a) puts its name or trademark on it, (b) substantially modifies it so it stays high-risk, or (c) changes the intended purpose of a non-high-risk system, including a GPAI system, so it becomes high-risk. https://artificialintelligenceact.eu/article/25/
PM application: a platform that lets customers configure an agent for HR screening or credit decisions can turn the customer into a provider; the platform PM must state intended purpose and prohibited uses in terms and docs.

### Penalties, Article 99 [S, consolidated text]
Prohibited practices: up to EUR 35M or 7% worldwide turnover, whichever higher. Other operator obligations: EUR 15M or 3%. Incorrect information to authorities: EUR 7.5M or 1%. SMEs and small mid-caps (SMCs, added by Omnibus): whichever is lower. https://artificialintelligenceact.eu/article/99/

### US federal posture
- Executive Order 14365 "Ensuring a National Policy Framework for Artificial Intelligence," signed 2025-12-11. Directs: AG AI Litigation Task Force within 30 days to challenge state AI laws; Commerce evaluation of "onerous" state laws within 90 days; BEAD non-deployment funds conditioned; FCC proceeding on a federal reporting and disclosure standard that could preempt; FTC policy statement on how the FTC Act applies to AI within 90 days; a legislative recommendation for a preemptive federal framework (carve-outs: child safety, compute and data center infrastructure, state procurement). Colorado's algorithmic discrimination law is named in Section 1. https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/ (fetched 2026-10-30) [V]. Outcomes of those 90-day actions not verified [U].
- July 2025 America's AI Action Plan directed NIST to revise the AI RMF (carried from ch31) [S]. NIST page confirms AI RMF 1.0 "is being revised as part of the White House AI Action Plan," no date given [V].

### US states (selected)
- California SB 53, Transparency in Frontier Artificial Intelligence Act (TFAIA), signed 2025-09-29. Large frontier developers publish a framework explaining how they apply national, international and industry standards; report critical safety incidents to the Office of Emergency Services; whistleblower protections; CalCompute consortium. https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/ [V, governor press release]. Applies to frontier model developers, not most B2B application vendors.
- Texas HB 149 (Texas Responsible AI Governance Act, TRAIGA), "Relating to regulation of the use of artificial intelligence systems in this state; providing civil penalties," signed 2025-06-22, effective 2026-01-01. https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=HB149 [V]. Substantive content (intent-based prohibitions, AG enforcement, sandbox) from prior knowledge [U].

### NIST AI RMF [V, nist.gov and airc.nist.gov, fetched 2026-10-30]
- AI RMF 1.0 released 2023-01-26; Generative AI Profile NIST AI 600-1 released 2024-07-26; concept note for a Critical Infrastructure profile 2026-04-07.
- Core: Govern (6 categories; cross-cutting culture, policies, accountability), Map (5; context to frame risk), Measure (4; quantitative and qualitative analysis and monitoring), Manage (4; allocate resources, respond, recover, communicate). https://airc.nist.gov/airmf-resources/airmf/5-sec-core/

### NIST AI 600-1 Generative AI Profile, the 12 risks [V, read from the PDF, nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf]
1 CBRN Information or Capabilities; 2 Confabulation; 3 Dangerous, Violent, or Hateful Content; 4 Data Privacy; 5 Environmental Impacts; 6 Harmful Bias or Homogenization; 7 Human-AI Configuration; 8 Information Integrity; 9 Information Security; 10 Intellectual Property; 11 Obscene, Degrading, and/or Abusive Content; 12 Value Chain and Component Integration. The profile defines confabulation as confidently stated but erroneous or false content. (This resolves ch31 flag 4 on the list.)

### Serious incidents, Article 73 [S, consolidated text]
Providers of high-risk systems report to the market surveillance authority of the Member State where it occurred: immediately after establishing a causal link or reasonable likelihood, no later than 15 days after awareness; widespread infringement no later than 2 days; death no later than 10 days. An incomplete initial report is allowed, then a complete one. Definition in Art. 3(49). Deployers report to the provider first (Art. 26(5)). https://artificialintelligenceact.eu/article/73/ Applies with the high-risk dates.

### Annex III, the eight high-risk areas [S, consolidated text]
1 biometrics (identification, categorisation, emotion recognition); 2 critical infrastructure (safety components in digital infrastructure, road traffic, water, gas, heating, electricity); 3 education; 4 employment (recruiting, screening, promotion, termination, task allocation, performance monitoring); 5 essential services (benefits, credit scoring, life and health insurance pricing, emergency call triage); 6 law enforcement; 7 migration and border control; 8 justice and democratic processes. https://artificialintelligenceact.eu/annex/3/
PM note for Beacon: "safety components in the management and operation of critical digital infrastructure" is the Annex III item an infra/ops agent must consciously screen against. Whether an IT ops agent for a commercial customer counts is a legal question; record the reasoning (Art. 6(4)).

### Article 6(3) and 6(4) exemption test [S, consolidated text]
An Annex III system is not high-risk if it poses no significant risk and meets any one of: narrow procedural task; improves the result of a completed human activity; detects patterns or deviations without replacing human assessment absent proper review; preparatory task. Profiling of natural persons is always high-risk. A provider relying on the exemption must document the assessment before market placement and register (Art. 49(2)); the Omnibus kept this registration [S, ch31]. https://artificialintelligenceact.eu/article/6/

### OWASP Top 10 for LLM Applications 2025 [V, genai.owasp.org/llm-top-10/]
LLM01 Prompt Injection; LLM02 Sensitive Information Disclosure; LLM03 Supply Chain; LLM04 Data and Model Poisoning; LLM05 Improper Output Handling; LLM06 Excessive Agency; LLM07 System Prompt Leakage; LLM08 Vector and Embedding Weaknesses; LLM09 Misinformation; LLM10 Unbounded Consumption. OWASP also runs an Agentic Security initiative (no agentic list confirmed on that page).

### Model cards [V, arXiv 1810.03993]
Mitchell, Wu, Zaldivar, Barnes, Vasserman, Hutchinson, Spitzer, Raji and Gebru, "Model Cards for Model Reporting," FAT* 2019. Short documents accompanying trained models with benchmarked evaluation across groups and intersectional groups, intended uses and out-of-scope contexts, and evaluation procedures. Section list (Model Details, Intended Use, Factors, Metrics, Evaluation Data, Training Data, Quantitative Analyses, Ethical Considerations, Caveats and Recommendations) is from prior knowledge of the paper [U, high confidence; check the PDF].

### Provider obligations for high-risk systems, Article 16 [S, consolidated text, https://artificialintelligenceact.eu/article/16/]
Meet Section 2 requirements: risk management (Art. 9), data governance (10), technical documentation (11), record-keeping/logging (12), transparency and instructions for use to deployers (13), human oversight (14), accuracy, robustness and cybersecurity (15). Plus: quality management system (17), keep documentation (18) and logs (19), name and contact marking, conformity assessment (43), EU declaration of conformity (47), CE marking (48), registration (49(1)), corrective actions (20), demonstrate conformity on request, accessibility.

### Fundamental rights impact assessment, Article 27 [S, consolidated text, https://artificialintelligenceact.eu/article/27/]
Required of deployers that are public bodies or private entities providing public services, and deployers of Annex III point 5(b) and (c) systems (credit scoring, life and health insurance pricing); Annex III point 2 (critical infrastructure) excluded. Before first use. Contents (a) deployer processes and intended purpose; (b) period and frequency of use; (c) affected people and groups; (d) specific risks of harm; (e) human oversight measures; (f) measures if risks materialise, including governance and complaints. Results notified to the market surveillance authority via a Commission template. Where a GDPR DPIA covers parts, the FRIA complements it and may cross-refer. Paragraphs marked amended by the Omnibus; detail not read [flag].

### GDPR DPIA, Article 35 [V, consolidated GDPR text via gdpr-info.eu, https://gdpr-info.eu/art-35-gdpr/]
Required where processing is likely to result in high risk; always for (a) systematic and extensive evaluation incl. profiling with legal or similarly significant effects, (b) large-scale special-category or criminal data, (c) large-scale systematic monitoring of public areas. Minimum contents: (a) systematic description and purposes; (b) necessity and proportionality; (c) risks to data subjects; (d) measures to address them.

### EDPB Opinion 28/2024 [V for title and date]
"Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models," adopted 2024-12-18. https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en. The three topics (when a model is anonymous; legitimate interest as a legal basis with a three-step test; consequences of unlawfully processed training data for later use) are from prior knowledge [U, high confidence].

### OWASP Top 10 for Agentic Applications 2026 [V, released 2025-12-09, https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/]
ASI01 Agent Goal Hijack; ASI02 Tool Misuse; ASI03 Identity and Privilege Abuse; ASI04 Agentic Supply Chain Vulnerabilities; ASI05 Unexpected Code Execution; ASI06 Memory and Context Poisoning; ASI07 Insecure Inter-Agent Communication; ASI08 Cascading Failures; ASI09 Human-Agent Trust Exploitation; ASI10 Rogue Agents. Directly relevant to Beacon Agents (tool misuse, privilege abuse, cascading failures).

### Principles sets
- OECD AI Principles, adopted 2019, updated May 2024. Five values-based principles: inclusive growth, sustainable development and well-being; human rights and democratic values, including fairness and privacy; transparency and explainability; robustness, security and safety; accountability. https://oecd.ai/en/ai-principles [V]
- Microsoft six principles: fairness; reliability and safety; privacy and security; inclusiveness; transparency; accountability. Responsible AI Standard referenced (v2, June 2022, from prior knowledge [U]). https://www.microsoft.com/en-us/ai/principles-and-approach [V for principles]
- Anthropic Responsible Scaling Policy, updated 2024-10-15: framework for catastrophic-risk governance with AI Safety Level (ASL) standards that tighten as capability grows. https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy [V]. Later RSP versions exist [U].

### EU codes of practice
- GPAI Code of Practice published 2025-07-10; three chapters: Transparency (with a Model Documentation Form, for Art. 53), Copyright (policy for EU copyright compliance), Safety and Security (only for systemic-risk models, Art. 55). Signatories include Anthropic, Google, Microsoft, Mistral AI and OpenAI; xAI signed only Safety and Security. https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai [V]
- Code of Practice on marking and labelling AI-generated content (Art. 50(2), (4), (5)): first draft 2025-12-17, second draft 2026-03-03, draft guidelines 2026-05-08, **final code 2026-06-10**; about 190 signatories by end of July 2026. Two sections: providers (marking and detection) and deployers (labelling deepfakes and public-interest text). Commission and AI Board confirmed it as an adequate voluntary means; supplemented by Art. 50 guidelines and an optional EU icon set. https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content [V]

### Security questionnaires and controls
- CSA AI Controls Matrix (AICM) v1 released 2025-07-09 (updated 2025-10-30; v1.1 now newest): 243 control objectives across 18 domains, mapped to ISO/IEC 42001, NIST AI RMF, NIST AI 600-1, EU AI Act, ISO 27001 and BSI AIC4. Companion AI-CAIQ questionnaire; STAR for AI certification with Level 1 self-submission. https://cloudsecurityalliance.org/artifacts/ai-controls-matrix [V]
PM application: build the AI security questionnaire answer bank on AI-CAIQ structure so one set of answers maps to ISO 42001 and EU AI Act asks.

### Other jurisdictions
- South Korea: Framework Act on AI Development and Establishment of a Foundation for Trustworthiness, promulgated 2025-01-21, effective **2026-01-22**. High-impact AI duties (risk management plan, explanation plan, user protection, human oversight, records); generative AI notice and output labelling; domestic representative for foreign operators above thresholds; fines up to KRW 30 million. https://fpf.org/blog/south-koreas-new-ai-framework-act-a-balancing-act-between-innovation-and-regulation/ [S, Future of Privacy Forum analysis]
- China: Measures for Labeling AI-Generated Synthetic Content (CAC, MIIT, MPS, NRTA), published 2025-03-14, effective **2025-09-01**; explicit (visible) labels and implicit (metadata) labels. https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm [V]

### NIST AI 600-1 on red-teaming and incident disclosure [V, PDF Appendix A]
- Four primary considerations of the GAI Public Working Group: Governance, Content Provenance, Pre-deployment Testing, Incident Disclosure.
- Definition: AI red-teaming is a structured testing exercise to probe an AI system for flaws and vulnerabilities such as inaccurate, harmful or discriminatory outputs, often in a controlled environment with developers.
- Types: General Public (ordinary users with lived experience; better in large groups); Expert (domain specialists, e.g. cybersecurity); Combination (experts refine general-public prompts); Human/AI (GAI-led red-teaming, more cost-effective; human and GAI-led suited to different harms). Results need further analysis before feeding governance decisions; teams should be diverse and have deployment-context expertise.
- Action GV-1.5-002: review incident response and incident disclosure processes to find gaps and update them.

### Anthropic Transparency Hub [V, https://www.anthropic.com/transparency, fetched 2026-10-30]
Per-model summary tables linking to full system cards: safety evaluations (even-handedness, honesty and hallucination, election integrity, child safety, self-harm), agentic and security testing (prompt-injection robustness, harmful computer-use, sandbox escape, cyber and bio), external red-teaming, and RSP evaluations. Useful as a public example of what a system card contains; a B2B app vendor's system card is narrower.

### Microsoft AI Impact Assessment Template and Guide [V that both are published, https://www.microsoft.com/en-us/ai/tools-practices; sections not read, U]
Public template and guide from Microsoft's Responsible AI program. Sections from prior knowledge [U]: system information and purpose, intended uses, stakeholders, potential harms by goal, fitness for purpose, data, and mitigations mapped to Responsible AI Standard goals. Use the idea, not the exact headings, unless re-verified.

---

## (a) Key concepts and frameworks, with PM application

### 1. Responsible AI principles into product practice
Originators: OECD AI Principles (2019, updated May 2024); Microsoft's six principles; NIST AI RMF "characteristics of trustworthy AI" (valid and reliable; safe; secure and resilient; accountable and transparent; explainable and interpretable; privacy-enhanced; fair with harmful bias managed) [U for exact wording, high confidence, from AI 100-1].
Translation table for the chapter (author synthesis, not a cited framework):

| Principle | Product question | What the PM builds or specifies | Evidence artifact |
|---|---|---|---|
| Fairness | Who could be treated worse, and how would we know? | Slice-level evals by customer segment, language, region; no profiling of people unless reviewed | Eval report with slices |
| Transparency | Does the user know it is AI and why it said this? | AI disclosure (Art. 50(1)), cited evidence, confidence cues, labels on generated text | UX spec, system card |
| Accountability | Who owns each risk and who can stop the launch? | Named risk owner per use case, RAI review gate, decision log | RAI review record |
| Privacy | What personal data enters prompts, logs, training? | Data minimisation, retention, no training on customer data by default, DPIA trigger | DPIA, data flow diagram |
| Safety | What is the worst action the system can take? | Autonomy limits, approval gates, kill switch, allowlists | Red-team plan, autonomy matrix |
| Security | How can it be attacked or misused? | Prompt-injection defences, least-privilege tools, connector scoping (OWASP LLM and Agentic top 10s) | Threat model, questionnaire answers |

### 2. EU AI Act roles, tiers and obligations (Regulation (EU) 2024/1689 as amended by (EU) 2026/1744)
- Roles: provider (develops or has developed and places on market under own name), deployer (uses under its authority), plus importer, distributor, authorised representative; GPAI model provider is separate. Role can switch under Art. 25 (rebrand, substantial modification, repurpose into high-risk).
- Typical B2B SaaS map: model lab = GPAI model provider; the SaaS vendor = provider of the AI system; the enterprise customer = deployer. A vendor using its own AI internally is also a deployer.
- Tiers: prohibited (Art. 5; from 2025-02-02, new items 2026-12-02); high-risk (Annex I products, Annex III uses; from 2028-08-02 and 2027-12-02); transparency-only (Art. 50; from 2026-08-02); minimal (no specific duties beyond AI literacy, Art. 4). GPAI models have their own track (from 2025-08-02).
- Obligations by tier: see Art. 16 (provider) and Art. 26 (deployer) lists above; Art. 27 FRIA for certain deployers; Art. 73 serious incidents; Art. 50 disclosure and marking.
- What PMs must build in (even before 2027): intended-purpose statement and prohibited-use list; logging that deployers can retain six months; human oversight controls (Art. 14); instructions for use (Art. 13) packaged for deployers; accuracy and robustness metrics (Art. 15) from the eval suite; AI-interaction disclosure and machine-readable marking of generated content; an Art. 6(4) documented non-high-risk assessment where relying on 6(3).

### 3. NIST AI RMF (NIST AI 100-1, 2023) and GenAI Profile (AI 600-1, 2024)
Voluntary. Govern (culture, policy, roles), Map (context, intended use, impacts), Measure (evals, metrics, monitoring), Manage (prioritise, respond, recover, communicate). Profiles tailor it; 600-1 adds 12 GAI risks and four considerations. PM application: Map is the PM's home function (use-case context, users, harms); Measure is the eval suite; Manage is launch gates and incident response; Govern is the RAI review process. US customers and federal buyers often ask for AI RMF alignment rather than EU conformity.

### 4. ISO/IEC 42001:2023 AI management system
First certifiable AI management system standard, December 2023, Annex SL structure shared with ISO 27001 so it bolts onto an existing ISMS [U for structure detail; iso.org returned 403]. Requires AI policy, roles, AI risk assessment, AI system impact assessment, controls (Annex A), internal audit and continual improvement. PM application: the certification is a company decision, but the PM supplies per-product impact assessments, lifecycle records and supplier controls. In questionnaires it is becoming the AI analogue of ISO 27001 (ch31, [S]).

### 5. Documentation artifacts
- Model cards: Mitchell et al. 2019 (above). Datasheets for Datasets: Gebru et al. (arXiv 2018, CACM 2021) [U, not fetched].
- System cards: the term is used by labs (Anthropic, OpenAI) for whole-system documentation including safeguards, red-teaming and agentic tests. For a B2B app, the "system card" documents the product system: models used, data flows, tools and permissions, autonomy limits, evals, known limitations, monitoring. Microsoft's "Transparency Notes" are a comparable public form [U].
- AI impact assessment: Microsoft template (above); ISO 42001 system impact assessment; EU FRIA (Art. 27) for deployers; GDPR DPIA (Art. 35). PM goal: one assessment that cross-references the others (the Omnibus explicitly allows FRIA to cross-refer to DPIA).

### 6. Red-teaming
NIST 600-1 typology above. For agents, scope to OWASP Agentic top 10 (goal hijack via injected tool output, tool misuse, privilege abuse, cascading failures). Plan template: objective; system version and scope; harm categories (from 600-1 list and OWASP lists); red-team type and people; scenarios and seeds; success criteria and severity scale; data handling; how findings flow into evals and the backlog; retest date.

### 7. AI incident response
Extends security incident response with AI-specific triggers: harmful or false outputs at scale (confabulation), unsafe agent actions, prompt-injection compromise, data leakage via outputs, bias findings, model provider changes. Regulatory clocks: EU Art. 73 (15, 10, 2 days, for high-risk once applicable); GDPR personal data breach 72 hours (Art. 33) [U, prior knowledge, high confidence]; California SB 53 critical safety incidents (frontier developers only). Public incident trackers: AI Incident Database, OECD AI Incidents Monitor (cited in ch31). PM role: severity definitions, customer comms, kill switch and rollback of model or prompt versions, turning each incident into an eval case.

### 8. Data protection interplay
GDPR Art. 35 DPIA triggers likely when AI evaluates people (profiling) or processes special-category data; Art. 22 automated decisions with legal or similarly significant effects [U, not fetched]; EDPB Opinion 28/2024 on AI models (anonymity, legitimate interest, unlawful training data). Omnibus adds a legal basis for processing special-category data for bias detection [S]. For B2B platforms, the vendor is usually processor; customer is controller; contracts (DPA) must cover AI sub-processors (model providers), data residency and no-training commitments.

### 9. Customer AI security questionnaires
Common structure (author synthesis from CSA AICM/AI-CAIQ and ISO 42001): AI governance and policy; model and supplier inventory; data use (training, retention, residency); privacy; security (prompt injection, access, isolation between tenants); evals and red-teaming; human oversight and autonomy; transparency to end users; incident response; regulatory position (EU AI Act role and tier, NIST alignment, ISO 42001 status). Answer bank: one canonical answer, evidence link, owner, last-reviewed date, and which framework IDs it satisfies. An AI harness with connectors can draft answers from the bank, but a human owner signs.

### 10. Responsible AI review inside a product org
Author synthesis: triage at idea stage (risk tier), proportional review (light for low, full board for high), gates at PRD, pre-beta, pre-GA, and on material change (new model, new tool permission, new data source, new market). Roles: PM owns the assessment; applied AI owns evals; security owns threat model; legal and privacy advise; a named approver can block. Evidence stored with the product, not in slide decks.

## (c) Short quotes (under 15 words)
1. Red-teaming is "a structured testing exercise used to probe an AI system." NIST AI 600-1, 2024.
2. Confabulation: "confidently stated but erroneous or false content." NIST AI 600-1, 2024.
3. With profiling, an Annex III system "shall always be considered to be high-risk." EU AI Act, Art. 6(3).
4. The FRIA "shall complement that data protection impact assessment." EU AI Act, Art. 27(4).
5. Deployers keep automatically generated logs "of at least six months." EU AI Act, Art. 26(6).

## (d) 2025 to 2026 developments (verified unless tagged)
- 2025-02-02 EU prohibitions and AI literacy applied; 2025-08-02 GPAI obligations applied; GPAI Code of Practice 2025-07-10 [V].
- 2025-09-01 China labelling measures effective [V]. 2026-01-22 Korea AI Framework Act effective [S].
- 2025-06-22 Texas TRAIGA signed, effective 2026-01-01 [V]. 2025-08-28 Colorado delay to 2026-06-30 [V]. 2025-09-29 California SB 53 signed [V].
- 2025-12-09 OWASP Top 10 for Agentic Applications 2026 [V]. 2025-07-09 CSA AICM and AI-CAIQ [V].
- 2025-12-11 Executive Order 14365 on a national AI policy framework and state-law preemption [V].
- 2026-04-07 NIST concept note for a critical infrastructure AI RMF profile; AI RMF revision under way, no date [V].
- 2026-06-10 EU Code of Practice on marking and labelling AI-generated content final [V]. 2026-07-27 Digital Omnibus in force [S]; 2026-08-02 Art. 50 applies [S].
- Next: 2026-12-02 new prohibitions and end of Art. 50(2) grace for legacy systems; 2027-12-02 Annex III; 2028-08-02 Annex I.

## (e) Beacon worked-example ideas (consistent with beacon-case.md)
- Triage: Beacon's three capabilities scored separately. Correlate = minimal risk. Diagnose = transparency plus confabulation risk (the hallucinated root cause storyline). Act = highest operational risk because it changes production. EU AI Act screen: Beacon does not evaluate people, so not Annex III employment or essential services; the open question is Annex III point 2 (safety components of critical digital infrastructure) for customers that run critical infrastructure. Outcome: Northlight documents an Art. 6(3)/(4)-style assessment and treats Act as "high-risk-ready" anyway. Flag: do not state a legal conclusion; the chapter should show the reasoning and that counsel decides.
- Roles: Northlight is provider of Beacon; customers (Priya's company) are deployers; the model lab is GPAI provider. Leo the MSP may become a provider if he white-labels Beacon (Art. 25(1)(a)), only relevant if the use becomes high-risk.
- Sam (security and compliance gatekeeper) sends a 140-question AI security questionnaire (number fictional) before an EU bank renewal; the PM uses the answer bank and an AI harness drafting from it, mapped to AI-CAIQ.
- System card for Beacon Agents: models and versions, connectors and scopes, action allowlist, approval gate, autonomy levels, eval results (diagnosis acceptance rate), known limits, log retention (supports deployer six-month retention), disclosure UX.
- Red-team plan before Northlight Live: injected instructions inside log lines and ticket text (ASI01 goal hijack via tool output), a malicious MCP server (ASI04), privilege escalation through a runbook (ASI03), cascading rollbacks (ASI08), and confident wrong root causes (confabulation).
- Incident response replay: the wrong-service rollback, run through the AI incident plan: severity, kill switch for autonomous actions, customer notice, root-cause (retrieval gap or prompt change), new eval cases, system card update.
- RAI review: Beacon's gate before Beacon Agents GA with named approver; the decision log records accepted residual risks.
- Data: Beacon logs may contain personal data (usernames, IPs); Northlight is processor; no training on customer data by default; DPIA support pack for customers.

## (f) Editorial flags
1. EUR-Lex operative text of Regulation (EU) 2026/1744 not readable by fetch (empty page). Dates confirmed via the consolidated text on artificialintelligenceact.eu (Arts. 26, 27, 113) and earlier EPRS and law-firm sources. Check the OJ before print.
2. **Colorado AI Act status after 2026-06-30 is unverified.** Confirmed: SB24-205 (2024) and SB25B-004 delay to 2026-06-30. Not confirmed: whether the 2026 regular session amended, replaced or further delayed it, or whether it is now in effect, and AG rulemaking status. Web search budget was exhausted. Write "check current status" language or verify before drafting.
3. Outcomes of EO 14365 deliverables (Commerce list of state laws, FTC statement, FCC proceeding, any litigation, any federal preemption bill) not verified.
4. ISO/IEC 42001 details from prior knowledge (iso.org 403). Certification counts are [S] from ch31.
5. Omnibus amendments to Art. 27 FRIA (paragraphs 2, 4, 5) not read.
6. Model card section names, Microsoft impact assessment sections, Datasheets for Datasets, GDPR Arts. 22 and 33 details, EDPB 28/2024 three topics, Texas TRAIGA substance, Japan AI Promotion Act (2025) and UK posture: prior knowledge only [U].
7. Whether an IT operations agent falls under Annex III point 2 is a legal interpretation; contested and fact-specific. Present as a question for counsel.
8. Korea Act facts are from FPF analysis of a machine translation [S].
9. Quote 5 uses only the fragment confirmed verbatim.
10. No statistics on RAI adoption or questionnaire volumes were verified; do not invent them.
