<p class="lead">Most of what a PM ships before the code is a document: a proposal that wins a budget, a memo that settles a decision, a press release that tells the team what it is building, an email that unblocks a launch. This chapter teaches you to write those documents so the reader can decide quickly and well, and to use AI to draft them without handing it the thinking.</p>

## Why this matters

A PM has very little formal authority. You can't order engineering to build something, sales to sell it or a vice president to fund it. What you can do is put an argument in front of people that is clear enough to act on and strong enough to survive their objections. In most B2B and platform companies, that argument travels as writing. Meetings end, slides get presented once, and the document is what gets forwarded to the person who wasn't in the room.

Writing does a second job that matters even more: it tests your thinking. A strategy that sounds coherent in conversation often falls apart when you try to put it in sentences, because prose forces you to say which claim depends on which evidence and what you're actually asking for. Paul Graham made this point in his 2024 essay "Writes and Write-Nots": "If you're thinking without writing, you only think you're thinking." (The idea is often credited to the computer scientist Leslie Lamport.) For a Senior or Principal PM, the document is where you find out whether you have a position at all.

In 2026 there's a third reason. Drafting has become nearly free. Any PM can produce ten polished pages in a few minutes, so polish no longer signals effort or judgment. A 2025 Harvard Business Review article by Kate Niederhoffer and colleagues named the result **workslop**: AI-generated work that looks finished but lacks the substance to move a task forward, so the real thinking lands on whoever receives it. In BetterUp Labs' survey of 1,150 US desk workers for that research, 40% said they'd received workslop in the previous month, and each instance cost about two hours to deal with. The PMs whose documents still get read are the ones whose pages are dense with judgment: a narrow ask, real evidence, honest tradeoffs and a clear recommendation.

This chapter covers narrowing the objective and analyzing the audience; structure (Barbara Minto's Pyramid Principle, the SCQA opening and bottom line up front); Amazon's six-page narratives and PR/FAQs; the PM's core documents; persuasion principles and the evidence behind them; and writing with AI. Chapter 35 covers presenting the same arguments live, and Chapter 36 covers the stakeholder relationships that decide whether a well-written proposal lands.

## Start with the objective and the reader

### Narrow the objective until someone can say yes

Most weak proposals fail before the first sentence, because the writer never decided what they wanted. "Improve agent quality" is a topic. "Approve a one-quarter hold on the autonomous tier, decided by the VP of Product before the launch content lock" is an objective. The difference is that a reader can say yes or no to the second one.

A narrowed objective has four parts:

- **The action**: what you want to happen, stated as a verb (approve, fund, choose, stop, agree).
- **The decider**: the one person whose yes makes it happen. If you can't name them, you're writing to the wrong reader.
- **The deadline**: when the decision is needed, and why that date.
- **The scope**: what's included and, just as important, what isn't.

Write this objective as one sentence before anything else. If it takes three sentences, you have three proposals; decide which comes first. Then imagine the decider replies with a single word. If neither "yes" nor "no" would tell you what to do next, the objective isn't narrow enough.

:::key One document, one ask
Every persuasive document has exactly one primary ask, stated in a sentence a busy reader could approve by replying "yes." Secondary requests go in a separate document or a clearly labeled "also" line at the end.
:::

### Audience analysis

Once you know what you want, work out who has to agree and what each of them needs to hear. Aristotle's *Rhetoric* gave writers a durable lens for this more than two thousand years ago. As the philosopher Christof Rapp summarizes it, Aristotle identified three ways a speaker persuades: through the speaker's character and credibility (**ethos**), through the emotions the audience is brought into (**pathos**) and through the argument itself (**logos**). Different readers weight these differently. A CFO leans on logos; a customer champion who was burned by the last tool needs some pathos (you understand the risk to them); a new executive who doesn't know you yet needs ethos before either.

In B2B companies, the readers of a significant proposal form something like a buying group (Chapter 01 describes the customer version). There is usually a decider, one or two people who can veto, people whose work changes if you're right, and people who will be asked their opinion by the decider. For each, answer six questions:

| Question | Why it matters |
|---|---|
| What is their role in this decision? (decide, veto, advise, execute, informed) | Tells you how much of the document is for them |
| What do they already know? | Sets the level of context and jargon |
| What do they believe now, and what would have to change? | Tells you which objection to address first |
| What do they care about and get measured on? | Tells you which benefit to lead with |
| What are they afraid of? | Usually the real objection, rarely stated |
| How will they read this? (pre-read, phone, forwarded, summarized by an assistant) | Sets length, format and where the ask goes |

The last row is new. In 2026, many readers will meet your document first as an AI summary in their inbox or chat tool. Microsoft's 2025 Work Trend Index reported that 68% of leaders at the companies it calls "Frontier Firms" used AI for internal communications, against 46% globally. If your ask is buried on page three, a summary may drop it. Put the ask where both a person and a summarizer will find it: the first lines.

### The curse of knowledge

Chip and Dan Heath popularized the term **curse of knowledge** in a 2006 Harvard Business Review article and in *Made to Stick* (2007): once you know something, it's hard to imagine not knowing it, so experts systematically overestimate how much their audience will understand. The Heaths illustrate it with a 1990 Stanford study by Elizabeth Newton, in which people tapped out the rhythm of well-known songs and badly overestimated how often listeners would recognize the tune. The tappers could hear the melody in their heads; the listeners heard only knocking.

PMs live inside this curse. You've spent weeks on the data and the customer calls; your reader has spent none, so acronyms, project names and "as discussed" references read as noise. The fix is mechanical: have someone outside the work (or an AI harness instructed to play a specific reader) mark every term or reference they can't follow, and either define it or remove it.

## Structure: answer first

### The Pyramid Principle

Barbara Minto developed the **Pyramid Principle** as a way to structure business writing so the reader gets the point before the detail. Her central rule is that a document should present its ideas as a pyramid under one main point. The governing thought sits at the top. Beneath it sit a small number of key points that each support it. Beneath each of those sit the facts and arguments that support that point.

The pyramid gives the reader the conclusion first, so everything after it reads as support, and it groups the support, so each reader can stop at the depth that answers their question. An executive may read only the governing thought and the key line; the engineering lead may read one branch to the bottom.

As commonly taught from Minto's book, the pyramid has a few working rules:

- **Ideas at any level summarize the ideas grouped below them.** If a key point doesn't follow from its support, either the point or the support is wrong.
- **Ideas in each group are the same kind of idea.** Three reasons, three steps or three options; never two reasons and a step.
- **Ideas in each group are in a logical order**: by importance, by time or by structure.
- **The groups should be mutually exclusive and collectively exhaustive (MECE).** No overlaps, and nothing important missing.

<figure class="fig" markdown="0">
<svg viewBox="0 0 680 360" role="img" aria-label="The Pyramid Principle with an SCQA opening: situation, complication and question lead to the answer, which sits at the top of a pyramid of three key points, each supported by evidence">
  <rect x="20" y="30" width="150" height="54" rx="8" class="box"/>
  <text x="34" y="52" class="t">Situation</text><text x="34" y="72" class="s">What the reader accepts</text>
  <rect x="20" y="96" width="150" height="54" rx="8" class="box"/>
  <text x="34" y="118" class="t">Complication</text><text x="34" y="138" class="s">What changed or broke</text>
  <rect x="20" y="162" width="150" height="54" rx="8" class="box"/>
  <text x="34" y="184" class="t">Question</text><text x="34" y="204" class="s">What the reader now asks</text>
  <line x1="170" y1="189" x2="300" y2="62" class="ln"/>
  <text x="95" y="244" text-anchor="middle" class="s">The opening (SCQA)</text>
  <rect x="300" y="30" width="250" height="64" rx="10" fill="var(--a1)" fill-opacity=".14" stroke="var(--a1)"/>
  <text x="425" y="56" text-anchor="middle" class="t" style="fill:var(--a1)">Answer: the governing thought</text>
  <text x="425" y="78" text-anchor="middle" class="s">One sentence the decider can approve</text>
  <line x1="425" y1="94" x2="290" y2="140" class="ln"/>
  <line x1="425" y1="94" x2="425" y2="140" class="ln"/>
  <line x1="425" y1="94" x2="560" y2="140" class="ln"/>
  <rect x="220" y="140" width="140" height="54" rx="8" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)"/>
  <text x="290" y="164" text-anchor="middle" class="t">Key point 1</text><text x="290" y="182" text-anchor="middle" class="s">Reason or option</text>
  <rect x="370" y="140" width="110" height="54" rx="8" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)"/>
  <text x="425" y="164" text-anchor="middle" class="t">Key point 2</text><text x="425" y="182" text-anchor="middle" class="s">Same kind</text>
  <rect x="490" y="140" width="140" height="54" rx="8" fill="var(--a2)" fill-opacity=".12" stroke="var(--a2)"/>
  <text x="560" y="164" text-anchor="middle" class="t">Key point 3</text><text x="560" y="182" text-anchor="middle" class="s">Logical order</text>
  <line x1="290" y1="194" x2="290" y2="236" class="ln"/>
  <line x1="425" y1="194" x2="425" y2="236" class="ln"/>
  <line x1="560" y1="194" x2="560" y2="236" class="ln"/>
  <rect x="220" y="236" width="410" height="54" rx="8" fill="var(--surface-2)" stroke="var(--border-2)"/>
  <text x="425" y="260" text-anchor="middle" class="t">Evidence under each point</text>
  <text x="425" y="278" text-anchor="middle" class="s">Data, customer quotes, costs, risks, each with a source</text>
  <text x="425" y="322" text-anchor="middle" class="s" style="fill:var(--muted)">Readers stop at the depth that answers their question. Executives often stop at the key line.</text>
  <text x="425" y="342" text-anchor="middle" class="s" style="fill:var(--a3)">Each level must summarize the level below it.</text>
</svg>
<figcaption>The Pyramid Principle with an SCQA opening. The situation, complication and question earn the reader's attention; the answer goes at the top of the pyramid; three key points of the same kind support it; evidence sits beneath each point.</figcaption>
</figure>

### SCQA: the opening that earns the answer

Minto also gave writers a way to open: **Situation, Complication, Question**. Her own materials describe it as a framework for finding the question already in the reader's mind. The usual business shorthand adds the Answer, giving **SCQA**.

- **Situation**: something the reader already knows and agrees with. It establishes common ground.
- **Complication**: what changed, broke or is threatening. This is the reason the document exists.
- **Question**: the question the complication raises in the reader's mind. Often it stays implicit.
- **Answer**: your governing thought, the top of the pyramid.

A good SCQA fits in a short paragraph. The situation should be undisputed; if the reader would argue with it, you've started the debate too early. The complication should be specific and measured. The answer should match your narrowed objective. Use SCQA when there's a real problem and a real choice; forcing one into a routine status update creates false drama.

### BLUF and writing for executives

The military version of answer-first is **BLUF**, bottom line up front: put the conclusion, recommendation or request in the first lines, then the background. It has long been a norm in US military writing (Army Regulation 25-50, which governs Army correspondence, is the usual citation). Kabir Sehgal adapted it for business email in a 2016 Harvard Business Review article on writing email with military precision. He also recommends a subject line that tells the reader what kind of action is needed.

BLUF assumes the reader may read only the first two lines, so those lines must stand alone. Writing for executives adds three habits:

1. **State the decision you need and the date in the first sentence.** "I need your approval by Friday to..." respects a calendar full of other documents.
2. **Give the recommendation, not just the options.** Executives can overrule you. They can't easily do your analysis for you. Show the options you rejected in one line each so they can see you considered them.
3. **Make the cost of saying no visible.** Every proposal has a "do nothing" option. Say what it costs and who pays.

Jakob Nielsen's research on how people read on the web, first published in 1997, found that most users scan rather than read word for word. Todd Rogers and Jessica Lasky-Fink, behavioral scientists who study communication, have written a full book on writing for busy readers built on the same premise: the reader's attention is the scarce resource. Write for the scanner. Use headings that say something ("Hold the autonomous tier one quarter" rather than "Recommendation"), put the key claim at the start of each paragraph and keep paragraphs short.

:::onramp If this is new to you
Take your last proposal and read only its first two sentences. Could someone make the decision from those alone? If not, rewrite them until they could.
:::

## Amazon's narrative culture

Amazon has said more in public than most companies about how it runs on writing, and its practices are often copied without the parts that make them work.

### The six-page narrative

In his 2017 letter to shareholders, Jeff Bezos wrote that Amazon doesn't do slide presentations in its meetings. Instead it writes "narratively structured six-page memos" that attendees read silently at the start of the meeting, in what he called a kind of study hall. The same letter makes a point about quality that is easy to skip: a great memo is written and rewritten, shared with colleagues for improvement, set aside for a few days and edited again with fresh eyes. Bezos wrote that a great memo probably takes a week or more.

The format works for three reasons:

- **Prose exposes gaps.** Bullet points let you place two ideas next to each other without saying how they connect. Narrative forces the connection.
- **Silent reading puts everyone on the same page.** The meeting starts from shared, complete context, so discussion goes straight to the hard parts rather than to the presenter's delivery.
- **The document outlives the meeting.** It becomes the record of what was decided and why.

Amazon publishes no official six-page template. The outline in this chapter's artifacts is this book's recommended shape: context and the question, tenets or principles, the current state with data, the proposal, alternatives considered, risks and mitigations, the plan and the ask, with an appendix for detail.

### The PR/FAQ and Working Backwards

The other Amazon form is the **PR/FAQ**, the core of what former Amazon executives Colin Bryar and Bill Carr call the Working Backwards process. Before building a new product, the team writes the press release they'd publish on launch day, followed by a set of frequently asked questions. The idea is to start from the customer experience and work backward to what has to be built, rather than starting from technology and looking for a customer.

According to the Working Backwards guidance, the press release has a standard shape:

- **Heading**: names the product in a way the target customer understands, in one sentence.
- **Subheading**: names the target customer and the benefit, in one sentence.
- **Summary paragraph**: the city, the outlet and the planned launch date, plus a summary of the product and its benefits.
- **Problem paragraph**: the customer's problem, from the customer's point of view.
- **Solution paragraph(s)**: how the product solves it, how it differs from today's alternatives and how to get started.
- **Quotes and getting started**: one quote from a company spokesperson, one from a hypothetical customer, how easy it is to start and where to go.

The FAQ comes in two parts. The **external FAQ** answers what customers and the press would ask: price, how it works, how to get help, where to buy. The **internal FAQ** answers what stakeholders would ask: who has the problem and how many will pay, how the product beats alternatives, market size, edge cases, technical and operational challenges, dependencies, regulation, unit economics and investment, and the assumptions that must hold, including the top three reasons the product could fail.

Bryar and Carr describe firm length limits: the press release is always under a page and the FAQ is five pages or fewer. In their description of the review, the author circulates the document, attendees read it silently, the most senior people tend to speak last so they don't anchor everyone else, and the critical part of the meeting is line-by-line feedback. The Working Backwards guidance describes a typical review as roughly 15 to 20 minutes of reading followed by about 40 minutes of discussion, and suggests a first draft should take hours, not days, because it will be rewritten many times.

For B2B PMs, the press release forces clarity about the customer and benefit, and the internal FAQ is where you confront the security review, the margin, the migration and the reasons it could fail.

### What to borrow, and what not to

You don't need Amazon's culture to use its tools, but keep the parts that make them work:

| Borrow | Don't copy blindly |
|---|---|
| Writing the decision down in full sentences before the meeting | A six-page length for every decision; most need one page |
| Silent reading at the start, so nobody is assumed to have pre-read | Silent reading for documents that should have been an email |
| The press release as a test of whether the customer benefit is clear | A PR/FAQ for incremental features with no new customer |
| The internal FAQ's "top three reasons this could fail" | A polished press release used as marketing copy |
| Rewriting over days, with peer review | Long documents that are long because the thinking isn't done |

## The PM's core documents

### The one-page proposal

The one-page proposal is the workhorse. It asks for one decision, gives the reader enough to make it, and fits on one page so it can be read in a couple of minutes and forwarded without a summary. Its structure is the pyramid, compressed:

1. **The ask** (one or two sentences): the narrowed objective, the decider and the date.
2. **Why now** (SCQA in a short paragraph): situation, complication, the question.
3. **The recommendation and three reasons**, each with its strongest piece of evidence.
4. **Options considered**, including doing nothing, each with its cost.
5. **Risks and what would change your mind.**
6. **Cost and next steps**, with owners and dates.

The "what would change my mind" line is often the most persuasive sentence on the page: it shows you've considered being wrong and lets skeptics agree conditionally.

### The decision memo

A decision memo records a decision and why it was made. Two ideas from Bezos's shareholder letters make it better.

In the 2015 letter he distinguished **Type 1 decisions**, which are consequential and nearly irreversible (one-way doors), from **Type 2 decisions**, which can be reversed if they turn out wrong (two-way doors). He argued that organizations often apply heavyweight Type 1 processes to Type 2 decisions and become slow. Say which type the decision is, because that sets how much evidence and review it deserves. Many decisions can be split: a pricing change for existing customers may be close to a one-way door, while a pilot for a cohort of new customers is a two-way door.

In the 2016 letter he wrote that most decisions can be made with about 70% of the information you'd ideally want, and described **disagree and commit**: a leader can say they disagree, commit to the decision anyway and move on. Record dissent explicitly, so the person who disagreed can commit with their concern on file instead of relitigating it. Decision memos are the backbone of a decision log (Chapter 29).

### Strategy documents

A strategy document is a longer persuasive piece: it argues for where to play and how to win over a year or more. Chapter 03 covers the content (Richard Rumelt's kernel of diagnosis, guiding policy and coherent actions). The writing advice here applies directly. Put the guiding policy in the first paragraph, use the diagnosis as the situation and complication, group the coherent actions as the key line of the pyramid and state what you are choosing not to do.

### Adapting a proposal into an email

Many decisions actually happen in email or chat, read on a phone between meetings, so adapting the proposal is a BLUF compression exercise. The subject line names the kind of request, the action and the date ("Decision needed by Thu: hold autonomous tier one quarter," never "Beacon Agents update"). The first line is the ask, answerable with one word. Three one-line reasons follow, then the cost of saying no, the link and what you'll do if you hear nothing.

Keep the email under about 150 words; if it needs more, its job is to get the reader to open the proposal. If you send several, tailor the first line: lead with risk for the security reviewer and with revenue for the sales leader.

## Persuasion: principles and their evidence

Structure gets your argument read; persuasion principles shape whether it lands. Use them with care. Some of the evidence is weaker than their popularity suggests, and misused they look like manipulation, which destroys the ethos you need for the next proposal.

### Cialdini's principles

Robert Cialdini's *Influence: The Psychology of Persuasion* is the most widely read book on the subject. His organization, Influence at Work, now lists seven principles:

| Principle | The idea | Honest use in a PM document |
|---|---|---|
| **Reciprocity** | People feel obliged to return what they first received | Do the reviewer's work for them: answer their known question before they ask it |
| **Scarcity** | People want more of what is limited or at risk of loss | State real deadlines and what is lost by waiting; never invent urgency |
| **Authority** | People defer to credible experts | Cite the SRE lead's data or the security architect's review, by name |
| **Consistency** | People want their actions to match what they've said before | Tie the ask to a goal or principle the reader already committed to |
| **Liking** | People say yes to people they like and feel similar to | Write in the reader's language and credit their prior work |
| **Social proof** | When unsure, people look at what others do | Show what comparable customers or teams did, with evidence |
| **Unity** | People favor those they see as part of a shared identity | Frame the proposal around the team's or company's shared goal |

Unity is the newest of the seven; Cialdini added it in a later edition of the book.

Now the caveat. Social psychology has been through a replication crisis, and some famous persuasion findings have proved fragile. One example touches Cialdini's own work. A 2008 study by Noah Goldstein, Cialdini and Vladas Griskevicius found that hotel guests reused towels more when a card said most guests did so, especially guests who had stayed in the same room. In 2014, Gerd Bohner and Lena Schlüter published a replication in PLOS ONE that did not find the effect. One failed replication doesn't overturn a body of research, and it would be wrong to say Cialdini's work doesn't replicate. It does mean you should treat these principles as useful lenses, not laws, and expect small, context-dependent effects. In B2B decisions the strongest lever is still logos: a clear ask, real evidence and honest tradeoffs.

:::note Persuasion versus manipulation
A useful line: you're persuading when the reader would still agree if they saw exactly what you were doing and why. Fake deadlines, cherry-picked customer quotes and anonymous "everyone agrees" claims fail that test, and readers in your own company will remember.
:::

### Made to Stick

Chip and Dan Heath's *Made to Stick* (2007) asks why some ideas survive and others are forgotten. They offer six principles, abbreviated as SUCCESs:

- **Simple**: find the core of the idea and strip it down to that.
- **Unexpected**: break a pattern the reader expects, to get attention.
- **Concrete**: use specific, sensory detail instead of abstraction.
- **Credible**: give the reader a way to believe it, including details they can check.
- **Emotional**: make the reader care about something specific.
- **Stories**: tell a story that shows the idea in action.

For PM writing, concrete and stories do the most work. "Diagnosis quality issues may impact customer trust" is abstract and forgettable. "A responder accepted our root cause, rolled back the checkout service, and took checkout down for eleven minutes during a sale" is concrete, credible and emotional at once, and the reader will repeat it in the next meeting. Lead with one real incident, then generalize with the data.

Simple is the narrowed objective again: finding the core means deciding what to leave out, which is hard because everything you leave out is true.

## How to apply it

This method works for any significant persuasive document; the time on each step scales with the stakes.

**Before you write**

1. **Narrow the objective** to one sentence with an action, a decider, a deadline and a scope.
2. **Classify the decision** as a one-way or two-way door. That sets the document type and how much evidence you need.
3. **Analyze the audience**: the decider and everyone who can veto or will be asked for an opinion. Name the objection most likely to sink the proposal.
4. **Gather the evidence with sources.** Ask your AI harness to pull data and documents through connectors, and keep the source next to every number.

**Think on paper**

5. **Build the pyramid by hand.** Don't delegate this step; if you can't build the pyramid, you don't have a recommendation yet.
6. **Write the SCQA opening**, with an undisputed situation and an answer that matches the objective.
7. **Write the "what would change my mind" line** and the rejected options, including doing nothing.

**Draft and test**

8. **Draft against the template.** AI can draft from your pyramid, evidence and template; you rewrite it in your voice and cut what you don't believe.
9. **Run reader tests.** Have the harness read as each key reader and list their first questions and the least credible claim. Then ask one real person outside the work.
10. **Verify every claim** against its source yourself. Fix or cut anything you can't trace.
11. **Cut** every sentence that doesn't support the governing thought. For high stakes, set it aside a day and cut again.

**Ship and follow through**

12. **Adapt for the channel** with a BLUF email or message that links the full document.
13. **Pre-wire the vetoes**: share the draft with people who can block it before the meeting, and fold in their objections (Chapter 36).
14. **Record the decision** in a short decision memo with reasons and dissent.

:::leader For product leaders
Make writing a team standard. Agree on a few document types with templates and default lengths, and a review norm (silent reading first, comments in the document, the most senior person speaks last). Reward one clear page over twenty slides, and set the AI disclosure and verification norm explicitly so each PM doesn't have to guess.
:::

## The AI lens

### Building AI-powered products

- **State uncertainty in numbers.** An AI feature's quality varies by case and over time, so "the agent is highly accurate" invites misreading. "Responders accepted the diagnosis in 64% of pilot incidents" can be checked and argued with. Put the measure, the sample and the period in the sentence (Chapter 31 covers evals).
- **Write the failure case into the proposal.** Every AI proposal needs a paragraph on what happens when the model is wrong: how the user will notice, what the blast radius is and how it's contained.
- **Write PR/FAQs for agents with the gatekeeper in the room.** For AI products in enterprise markets, the internal FAQ should answer the security and compliance reviewer's questions (data access, audit logs, model training on customer data, regulatory documentation) as fully as the customer's. Chapter 33 covers the regulatory content.
- **Don't let the press release overclaim autonomy.** "Resolves incidents automatically," for a product that needs human approval for most actions, will be quoted back to you by customers and regulators.

### Writing with AI: draft, don't think

Delegate drafting, critique and checking. Keep the thinking: the objective, the pyramid, the recommendation and the judgment about what to leave out.

A 2025 MIT Media Lab preprint by Nataliya Kosmyna and colleagues, "Your Brain on ChatGPT," compared people writing essays with an AI assistant, with a search engine and with no tool. The AI-assisted group showed the weakest brain connectivity, reported the lowest sense of ownership of their essays and had trouble quoting what they'd just written. The sample was small, the task was a single essay format and the paper is a preprint that has been widely over-reported, so treat it as a warning sign rather than proof. The practical risk is plain: if the model does the thinking, you won't own the argument when you have to defend it in the meeting.

Anthropic's AI Fluency course organizes good practice under four headings that map well onto writing. **Delegation**: hand over drafting, reader simulation and claim checking, and keep the ask and the pyramid. **Description**: give the model the audience analysis, template, evidence and samples of your writing. **Discernment**: read the draft as a skeptic and notice where it smoothed over a real tradeoff. **Diligence**: verify, use approved tools for confidential data and be open about how the document was made.

### Voice

AI drafts tend toward the same balanced, confident, generic voice, which makes your documents interchangeable with everyone else's. Most assistants let you supply writing samples or a style guide; give yours two or three of your best past documents and a short list of rules (sentence length, words you never use, how you state recommendations). Then rewrite the opening, the recommendation and the risks section yourself. That's where the reader decides whether to trust you.

### Verification

KPMG and the University of Melbourne's 2025 global study of trust in AI found that 66% of employees rely on AI output without evaluating its accuracy and 56% say they've made mistakes in their work because of AI. A persuasive document is the worst place for those mistakes, because a wrong number in a proposal costs you credibility on every future proposal.

Make verification a step with a visible output: have the harness list every factual claim with its source, then check each yourself. Cut anything without a source, or label it as your estimate.

### Disclosure

Disclosure is unsettled. KPMG's US findings from the same 2025 study reported that 53% of US workers avoid revealing when they use AI and present AI-generated content as their own. One reason is that visible AI use carries a cost: Jessica Reif, Richard Larrick and Jack Soll reported in PNAS in 2025, across four preregistered experiments with 4,439 participants, that people who use AI at work are rated as less competent and less motivated by others.

There's no cross-industry workplace standard for disclosure yet. Some fields have set one: the medical journal editors' group ICMJE requires authors to disclose AI use, bars listing AI as an author and holds the humans accountable for the content. This book recommends a similar norm for PM documents: a short line at the end of any significant document saying what AI did and what you checked. For example: "Drafted with an AI assistant from the incident review and support data; every number checked against source systems by [name]." The line answers the competence penalty by showing where your judgment went, which is what the reader is evaluating.

:::ai The one-line rule
Let AI draft the sentences; never let it decide the ask. If you couldn't defend the recommendation in the meeting without the document in front of you, the document isn't ready, however well it reads.
:::

## The Beacon case: winning the hold

:::example Where Beacon stands
Chapter 31 told the story of the wrong rollback: in the Beacon Agents design-partner pilot, a responder accepted the agent's diagnosis, rolled back the wrong service and took a customer's checkout down for eleven minutes. The team fixed the evals, and diagnosis acceptance reached 64%. Northlight Live is approaching, and the launch story includes autonomous remediation for allowlisted actions. You believe the autonomous tier needs another quarter of evaluation, and you have to win that argument in writing with a VP of Product who wants a big launch and a product marketing manager who has built the keynote around it.
:::

**Narrowing the objective.** Your first draft says "improve agent quality before launch," a topic. You narrow it: *"Approve launching Beacon Agents at Northlight Live with supervised remediation only, holding the autonomous tier one quarter while the two applied AI engineers extend the eval suite to autonomous actions; decision by the VP of Product before the launch content lock."* It asks for reallocation, not new budget.

**The audience worksheet.** The VP of Product decides, cares about the launch and the 38% growth story, and fears looking cautious in front of the CEO. The product marketing manager can't veto but can make the decision expensive; their fear is a keynote rewritten at the last minute. Sam, the security and compliance reviewer, would likely block autonomous write access without stronger audit evidence, and EU customers are asking for AI Act documentation. Marcus, the economic buyer, needs an ROI story for a CFO who has already asked who pays when the agent makes an incident worse. Priya, the champion, needs to trust the agent won't make things worse. The worksheet shows that the decider's real objection is the launch narrative.

**The SCQA.** *Situation:* Beacon Agents launches at Northlight Live, and diagnosis acceptance is the metric customers watch to decide whether to trust it. *Complication:* in the pilot, a confident wrong diagnosis led a customer to roll back the wrong service, and the autonomous tier would let that kind of action run without a human. *Question:* do we ship the autonomous tier on schedule? *Answer:* ship supervised remediation on schedule and hold the autonomous tier one quarter, until it clears an extended eval suite.

**The pyramid.** Three reasons, one kind (each is a risk the hold removes):

1. **It protects trust with users.** Priya and Dana's willingness to accept diagnoses is the product's leading indicator, and one autonomous mistake at launch would reset it.
2. **It protects the buyer story.** Marcus buys on MTTR and ROI; net revenue retention is 118%, and an agent-caused outage at a reference customer would put expansion at risk.
3. **It clears the gatekeepers.** Sam's review and EU customers' documentation requests are easier to satisfy for supervised actions, so the launch reaches more customers.

The "what would change my mind" line: *if the eval suite shows the autonomous actions meeting the regression bar on every release for six weeks before the content lock, ship the autonomous tier as planned.*

**Persuasion, honestly.** You lead with the eleven-minute checkout outage rather than a paragraph about "quality risk." You tie the ask to the North Star the VP already set (incidents resolved with Beacon's help per week), quote Priya from the post-incident review with her permission and use the real content lock as the only deadline.

**Doing it with AI.** Through connectors, the harness pulls the post-incident review and every support ticket mentioning the rollback. You give it your pyramid, the audience worksheet and the one-page template, then rewrite the ask, recommendation and risks yourself. Reader tests as the VP and as Sam surface the question you'd missed: what does the keynote say instead? You add a paragraph offering product marketing a different story ("the agent that tells you when it's not sure"), drawn from the eval work.

The claims check lists every number with its source, and one fails: the draft says gross margin "fell from 81% to about 70%," while the finance report says 72%. The model had drifted toward a figure from another document's cost discussion. You fix it and add the disclosure line at the bottom: *"Drafted with Claude from the incident review and support data; numbers checked against source systems by [your name]."*

**The email.** The VP will decide between meetings, so you adapt the one-pager into an email:

> **Subject:** Decision needed before content lock: hold Beacon Agents autonomous tier one quarter
>
> I recommend we launch Beacon Agents at Northlight Live with supervised remediation and hold the autonomous tier one quarter. I need your decision before the content lock.
>
> - Trust: one autonomous mistake at launch would reset responders' trust in diagnosis.
> - Revenue: our buyers renew on MTTR; an agent-caused outage at a reference account puts expansion at risk.
> - Reach: supervised actions clear security reviews and EU documentation requests faster.
>
> If no, we ship as planned and I'll add a launch-week rollback plan. The one-pager (with what would change my mind) is linked. I'll walk product marketing through a revised keynote story either way.

**The outcome.** The VP approves, on condition of a written go or no-go on the autonomous tier at the next quarterly business review, judged against the eval bar in the one-pager. Your decision memo records the product marketing manager's dissent ("a weaker keynote") and their commitment. The keynote leads with diagnosis that shows its evidence.

## Product 360 artifacts

```template id="34-audience-analysis" title="Audience analysis worksheet"
# Audience analysis · [Document or proposal] · [Date]

**Narrowed objective (one sentence):** [Action] by [decider] by [date], scope: [included / excluded]
**Decision type:** One-way door / Two-way door / Split (explain)
**Document type:** Email / One-page proposal / Decision memo / Six-page narrative / PR/FAQ

## Readers
| Reader | Role in decision (decide / veto / advise / execute / informed) | What they know | What they believe now | What they care about and are measured on | What they fear | How they will read it | Lead appeal (ethos / pathos / logos) |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

## The objection most likely to sink this
[Who holds it, in their words, and how the document answers it]

## Curse-of-knowledge check
Terms, acronyms and references a reader outside the work won't know:
- [Term]: define / remove

## Pre-wiring plan
| Reader | Share draft by | Channel | Their feedback | How the document changed |
|---|---|---|---|---|
| | | | | |
```

```template id="34-one-page-proposal" title="One-page proposal"
# [Title that states the recommendation, e.g. "Hold the autonomous tier one quarter"]

**Decision needed from:** [Name]   **By:** [Date and why that date]   **Author:** [PM]   **Decision type:** One-way / Two-way door

## The ask
[One or two sentences the decider could approve by replying "yes."]

## Why now
[Situation: what the reader already accepts.] [Complication: what changed, with a number.] [Question: what this raises.] [Answer: the ask, restated.]

## Recommendation and reasons
1. **[Reason 1]**: [strongest evidence, with source]
2. **[Reason 2]**: [strongest evidence, with source]
3. **[Reason 3]**: [strongest evidence, with source]

## Options considered
| Option | What it costs | Why not |
|---|---|---|
| Do nothing | | |
| [Option B] | | |
| **Recommended** | | |

## Risks and what would change my mind
- Risk: [risk] · Mitigation: [mitigation]
- I would change my recommendation if [specific, observable condition].

## Cost and next steps
| Step | Owner | Date |
|---|---|---|
| | | |

---
*How this was made: [e.g. "Drafted with an AI assistant from (sources); every number checked against source systems by (name)."]*
```

```template id="34-pr-faq" title="PR/FAQ"
# PR/FAQ · [Product or feature] · Draft v[n] · [Date]

**Author:** [PM]   **Reviewers:** [names]   **Status:** Draft / In review / Approved / Shelved

## Press release (under one page)

### [Heading: the product named so the target customer understands it, one sentence]
#### [Subheading: who the customer is and the benefit they get, one sentence]

**[City] · [Outlet] · [Planned launch date]**: [Summary paragraph: what the product is and its main benefit.]

**The problem.** [The customer's problem, from the customer's point of view, in their words.]

**The solution.** [How the product solves it, how it differs from today's alternatives (including doing nothing), and how to get started.]

"[Quote from a company spokesperson: why we built it.]" said [name, title].

"[Quote from a hypothetical customer: the outcome in their words.]" said [persona, role, company type].

**Getting started.** [How easy it is to start, and where to go.]

## External FAQ (customers and press)
1. How much does it cost?
2. How does it work?
3. How do I get help?
4. Where and how do I buy it?
5. [What does it access, and how is my data handled?]

## Internal FAQ (stakeholders; five pages or fewer for the whole FAQ)
1. Who has this problem, how many of them are there and how many will pay?
2. How does this beat the alternatives on quality, cost or speed? Who are the competitors?
3. How big is the market we can actually serve?
4. What edge cases matter, and how do we handle them?
5. What are the hardest technical, operational, legal and design problems? What new capabilities do we need?
6. What do we depend on (partners, platforms, other teams)?
7. What regulatory or compliance questions apply?
8. What are the unit economics, the upfront investment and the time to payback?
9. For AI products: what is the autonomy level, how do users notice when it's wrong and what is the blast radius?
10. What must be true for this to succeed, and what are the top three reasons it could fail?
```

```template id="34-six-page-narrative" title="Six-page narrative outline"
# [Title stating the proposal] · Narrative · [Date]

**Author:** [PM]   **Meeting:** [date]; silent reading in the first minutes   **Decision needed:** [one sentence]

This outline is a recommended shape, not an official format. Write in full paragraphs; tables and charts are fine where they carry data. Six pages is a ceiling.

## 1. Context and question (half a page)
The situation, the complication and the question this document answers. End with the answer in one sentence.

## 2. Tenets (a few lines)
The principles we're using to decide, stated so a reader can disagree with them.

## 3. Where we are today (one page)
The current state, with data and sources. What customers say, in their words. What we've tried.

## 4. The proposal (one and a half pages)
What we'll do, for whom and why. How it serves the tenets. What success looks like, in metrics.

## 5. Alternatives considered (half a page)
Each serious alternative, including doing nothing, and why we didn't choose it.

## 6. Risks and mitigations (half a page)
What could go wrong, how we'd know early and what we'd do. What would change our mind.

## 7. Plan and ask (half a page)
Milestones, owners, cost and the specific decisions needed from this meeting.

## 8. Open questions
What we don't know yet, and how we'll find out.

## Appendix (not counted in the six pages)
Supporting data, detailed models, customer evidence, glossary.

---
*How this was made: [AI use and verification line]*
```

```template id="34-decision-memo" title="Decision memo"
# Decision: [the decision, stated as a sentence] · [Date]

**Decider:** [Name]   **Author:** [PM]   **Status:** Proposed / Decided / Revisited
**Decision type:** One-way door / Two-way door / Split: [which part is which]
**Information confidence:** [roughly how much of what we'd want to know we have, and what's missing]

## Context
[Two or three sentences: the situation and complication.]

## Options
| Option | Benefits | Costs and risks | Reversible? |
|---|---|---|---|
| | | | |

## Decision
[What was decided, by whom, and the main reasons.]

## Dissent and commitment
| Person | Concern | Committed? |
|---|---|---|
| | | Yes / No |

## Conditions and review
- We will revisit if: [observable trigger]
- Review date: [date]   Forum: [governance forum or business review]

## Consequences
[What changes now: roadmap, owners, messages to customers or teams.]
```

```template id="34-executive-email" title="Executive email (BLUF)"
Subject: [Decision needed / FYI / Approval needed] by [date]: [the ask in under ten words]

[Name],

[The ask in one sentence that can be answered with one word.] [The date and why.]

- [Reason 1, one line]
- [Reason 2, one line]
- [Reason 3, one line]

[Cost of saying no, one sentence.] [What you'll do if you hear nothing, and when.]

Full proposal: [link]

[Your name]

---
Checks before sending:
- Under about 150 words.
- The first line works alone in a preview pane or an AI summary.
- First line tailored to this reader's main concern.
- Every number checked against its source.
```

## Prompts

```prompt title="Narrow a vague objective into one ask"
Goal: Turn a topic into a decision a reader can approve.
Paste in: your current draft ask or the problem in a few sentences, who you think decides and any deadline you know about.

I'm a product manager writing a proposal. Here is what I want to achieve: [draft ask or problem].

1. Rewrite it as one sentence with four parts: the action (a verb), the one person who decides, the deadline and the scope (what's included and excluded).
2. If my draft actually contains more than one ask, list them separately and tell me which should come first and why.
3. Give me three alternative versions, from the most ambitious to the most conservative, and the likely objection to each.
4. Tell me what information you'd need to make the ask sharper. Don't fill gaps with assumptions; list them as questions.

Check the output: imagine the decider replies with one word. If neither "yes" nor "no" would tell you what to do next, narrow it again. Make sure the decider named is a real person with the authority, not a committee.
```

```prompt title="Build an audience analysis"
Goal: Know who has to agree and what each of them fears before you draft.
Paste in: the narrowed ask, the list of readers with their roles, and anything you know about their goals and past positions (meeting notes, prior emails, strategy documents). Use an approved tool for internal documents.

For this proposal: [ask], complete an audience analysis for these readers: [readers and roles].

For each reader give: their role in the decision (decide, veto, advise, execute or informed), what they likely know, what they likely believe now, what they're measured on, what they're probably afraid of, how they'll read the document, and which appeal (credibility, emotion or logic) will matter most to them.

Then name the single objection most likely to sink the proposal, who holds it and how the document should answer it.

Rules: base every claim about a reader on the material I gave you, and cite it. Where you're guessing, label it "guess."

Check the output: the "guess" labels are where you need a conversation, not a better prompt. Confirm the biggest objection with at least one real person before drafting.
```

```prompt title="Draft from my pyramid, in my voice"
Goal: Get a first draft fast without handing over the thinking.
Paste in: your pyramid (governing thought, three key points, evidence with sources under each), the template for the document type, the audience analysis and two or three samples of your own writing.

Draft a [one-page proposal / decision memo / six-page narrative] using this template: [template].

The argument is fixed. Use my governing thought and key points exactly; don't add, merge or reorder them. Use only the evidence I've provided, and keep the source next to every number. Open with a Situation, Complication, Question, Answer paragraph. Put the ask in the first two sentences.

Match the voice of my writing samples: sentence length, directness, how I state recommendations. Avoid generic phrases, filler transitions and summary endings. Write "[NEEDS EVIDENCE]" wherever the template asks for something I haven't given you.

[pyramid]
[audience analysis]
[writing samples]

Check the output: rewrite the ask, the recommendation and the risks section yourself. Search for "[NEEDS EVIDENCE]" and either supply the evidence or cut the claim. Delete any sentence you wouldn't say aloud in the meeting.
```

```prompt title="Read my draft as a skeptical executive"
Goal: Find the questions and weak claims before the real reader does.
Paste in: the draft and a short description of the reader (role, goals, what they fear, how much time they have).

Act as [reader description], who has [two minutes] to read this and will decide [the ask].

1. In one sentence, what do you think I'm asking for? If it's unclear, say so.
2. List the first three questions you'd ask.
3. Identify the one claim you find least credible and explain why.
4. Name the option or risk you think I've ignored.
5. Tell me whether you would say yes, no or "not yet," and what would change your answer.

Be direct. Don't soften the critique, and don't invent facts about the company that aren't in the draft.

[draft]

Check the output: if the simulated reader misstates the ask, fix the first two sentences before anything else. Treat the simulation as a rehearsal; then ask one real person to do the same test.
```

```prompt title="Check every claim against its source"
Goal: Make sure no unverified number, name or quote leaves your desk.
Paste in: the final draft and the source documents or data the claims came from, or connect the harness to them. Use an approved tool for confidential data.

List every factual claim in this draft: each number, percentage, date, name, quote, product capability and comparison. For each, give:
- the exact sentence it appears in,
- the source document and location it came from,
- whether the source supports it exactly, roughly (for example rounded or paraphrased), or not at all.

Flag any claim with no source as "UNSOURCED." Flag any rounding or paraphrase that changes the meaning. Don't correct the draft; just report.

[draft]
[sources]

Check the output: open the source yourself for every number in the first paragraph and every number in the recommendation. Fix or cut every UNSOURCED claim, or label it as your estimate.
```

```prompt title="Adapt a proposal into a BLUF email"
Goal: Carry the ask into the channel where the decision will actually be made.
Paste in: the one-page proposal and the name, role and main concern of the email's reader.

Turn this proposal into an email to [reader], whose main concern is [concern].

- Subject line: the kind of request (decision, approval or information), the date and the ask in under ten words.
- First line: the ask, in one sentence that can be answered with one word, plus the date.
- Then three one-line reasons, with the one closest to [concern] first.
- Then one sentence on the cost of saying no and one on what I'll do if I hear nothing.
- End with the link placeholder to the full proposal.

Keep it under 150 words. Don't add claims that aren't in the proposal.

[proposal]

Check the output: read only the subject and first line, as if in a preview pane. Could the reader decide from those? Confirm every reason appears, with evidence, in the proposal.
```

```prompt title="Draft a PR/FAQ for a new product bet"
Goal: Test whether the customer benefit is clear before anyone builds.
Paste in: the product hypothesis, the target persona and their job story, known alternatives, any pricing and cost assumptions and what you know about risks.

Write a PR/FAQ for [product] with:
1. A press release under one page: heading (one sentence naming the product for the customer), subheading (customer and benefit, one sentence), summary paragraph with [city], [outlet] and [launch date], problem paragraph in the customer's words, solution paragraph (including how it differs from today's alternatives), a spokesperson quote, a hypothetical customer quote and how to get started.
2. An external FAQ: price, how it works, support, how to buy and how data is handled.
3. An internal FAQ: who has the problem and how many will pay, competitive advantage, serviceable market, edge cases, hardest problems, dependencies, regulation, unit economics, and the top three reasons it could fail.

Use only the facts I've provided. Mark customer quotes as hypothetical. Where I haven't given you a fact the FAQ needs, write the question and "[OPEN]" instead of an answer.

Check the output: if the press release would bore the target customer, the product isn't clear yet. Count the "[OPEN]" items; they're your research plan. Make sure the press release doesn't claim more autonomy or capability than the product will have at launch.
```

## Anti-patterns

:::warn The topic disguised as an ask
"An update on agent quality" or "thoughts on pricing" gets read, nodded at and forgotten, because nothing in it can be approved. Every persuasive document needs one ask with a decider and a date in the first two sentences.
:::

:::warn The mystery novel
The document walks through background, analysis and options in the order the author discovered them, and reveals the recommendation on the last page. Busy readers never get there. Put the answer first, then the support.
:::

:::warn Workslop
A long, fluent AI draft is sent with light editing. It looks complete, but the reader has to reconstruct the argument, check the numbers and guess at the ask. It costs the reader time and costs you credibility. Draft with AI; think, cut and verify yourself.
:::

:::warn The unverified number
A rounded, misremembered or model-generated figure appears in a proposal to an executive. Someone who knows the real number spots it, and the rest of the document loses credibility with it. Run a claims check on every significant document and trace every number to its source.
:::

:::warn Persuasion theater
Invented deadlines, anonymous "everyone agrees" claims, cherry-picked customer quotes. These sometimes work once. Inside a company you write for the same readers for years, and they remember. Persuade only in ways you'd be comfortable having the reader see.
:::

:::warn Cargo-cult narratives
The team adopts six-page memos for every decision, including ones that should be an email, and reading time crowds out discussion. Match the document type to the decision: most decisions need one page, and only the big one-way doors need a narrative or a PR/FAQ.
:::

## Checklist

- [ ] The ask is one sentence with an action, a decider, a deadline and a scope, and it appears in the first two sentences.
- [ ] The decision is classified as a one-way or two-way door, and the document type and length match it.
- [ ] An audience analysis covers the decider and everyone who can veto, and names the objection most likely to sink the proposal.
- [ ] The pyramid was built by the author: one governing thought, about three key points of the same kind, evidence under each.
- [ ] The opening uses SCQA where there's a real decision, with an undisputed situation and a specific complication.
- [ ] Options include doing nothing, with its cost, and the document says what would change the author's mind.
- [ ] Persuasion principles are used honestly: real deadlines, named sources, representative evidence.
- [ ] Every number, name, date and quote has been traced to its source by the author.
- [ ] The ask, recommendation and risks are in the author's own voice.
- [ ] Confidential data went only into approved AI tools, and a disclosure line states how AI was used and what was checked.
- [ ] A BLUF email or message carries the ask to the channel where the decision will be made.
- [ ] People who can veto saw the draft before the decision meeting.
- [ ] The decision, reasons and dissent are recorded in a decision memo.

## Key takeaways

- A persuasive document has one ask that a named decider can approve by a date. Narrow the objective before you write anything else.
- Structure for a reader who may stop after two sentences: answer first, three supporting points, evidence beneath, an SCQA opening when there's a real decision.
- Amazon's six-page narratives and PR/FAQs work because prose exposes gaps and silent reading builds shared context. Borrow the discipline, and match the document's length to the decision.
- Analyze the audience by role, beliefs, measures and fears. The objection that sinks a proposal is usually unstated and usually held by someone who can veto.
- Persuasion principles are useful lenses with uneven evidence. Concrete stories and honest tradeoffs do more in B2B decisions than any technique, and manipulation costs you the next proposal.
- With AI, delegate drafting, reader simulation and claim checking, and keep the ask, the pyramid and the recommendation. Verify every number yourself and disclose how the document was made.
