# Beacon: the running case (author bible)

Internal reference for anyone writing a chapter. Not published. Every chapter's worked example uses these facts so the case stays consistent. All of it is fictional. Never describe it as a real company or product.

## The company

- **Northlight Systems**: a fictional mid-size enterprise software company (about 2,400 employees, public, sells to IT and operations buyers). Three product lines: observability (Northlight Observe), IT service management (Northlight Desk) and Beacon.
- Sells direct to large enterprises and through partners (managed service providers and resellers) to the mid-market.

## The product

- **Beacon** is an AI agent platform that helps IT operations and SRE teams detect, diagnose and resolve incidents.
- History: launched in 2023 as an AIOps alert-correlation feature inside Northlight Observe. Spun out as a standalone product in 2024. In 2026 it is moving from "correlate and summarize" to agentic diagnosis and supervised remediation ("Beacon Agents").
- Core capabilities in 2026:
  1. **Correlate**: groups thousands of alerts into a handful of incidents.
  2. **Diagnose**: an agent pulls logs, metrics, traces, recent deploys and change tickets, then proposes a likely root cause with cited evidence.
  3. **Act**: runs approved runbook steps (restart, roll back, scale) with a human approval gate; fully autonomous only for low-risk actions the customer allowlists.
  4. **Learn**: post-incident reviews feed resolved incidents back into retrieval and evals.
- Connects to customer systems through connectors (including MCP servers) for observability tools, ticketing, chat, CI/CD and cloud providers.

## The people

| Persona | Role | What they need |
|---|---|---|
| **Priya**, SRE lead (primary user and champion) | Runs on-call for a 40-person platform team | Fewer pages, faster diagnosis, trust that the agent will not make things worse |
| **Dana**, on-call engineer (daily user) | Gets paged at 3 a.m. | A clear "what broke and what do I do" in under five minutes |
| **Marcus**, VP of IT Operations (economic buyer) | Owns the ops budget and uptime targets | Lower MTTR, fewer escalations, headcount leverage, an ROI story for the CFO |
| **Sam**, security and compliance reviewer (gatekeeper) | Approves any tool that touches production | Least-privilege access, audit logs, data residency, AI risk documentation |
| **Leo**, MSP operations manager (partner persona) | Runs ops for 60 mid-market customers | Multi-tenant views, per-customer billing, margin |

## The product team

- **You**: Principal PM for Beacon, newly in the role, reporting to the VP of Product for the Operations portfolio.
- Two group PMs under the portfolio (Observe and Desk) are peers. Beacon has 3 PMs, 1 product designer, about 35 engineers across 5 teams, 2 applied AI engineers, a product marketing manager and a shared product ops lead.

## Numbers (fictional, use as given)

- ARR: about $48M, growing 38% year over year. About 420 enterprise customers.
- Pricing (2026): platform fee per environment plus usage, moving toward a per-resolved-incident price for Beacon Agents. Gross margin dropped from 81% to 72% after agentic features launched because of inference cost.
- Key metrics: mean time to resolve (MTTR), alert-to-incident compression ratio, diagnosis acceptance rate (how often responders accept the agent's root cause), autonomous resolution rate, weekly active responders, net revenue retention (NRR, currently 118%).
- North Star: **incidents resolved with Beacon's help per week** (customer value, not usage).

## Market

- Competes with AIOps features in large observability platforms, incident-management tools adding AI, and startups building ops agents. Main alternative for most prospects: humans plus runbooks plus chat.
- Strategic tension: build on Northlight Observe data (advantage) versus stay tool-agnostic (larger market).

## Live storylines for chapters to use

- Launching Beacon Agents (supervised remediation) at Northlight's annual customer event, "Northlight Live."
- Moving pricing from per-environment to per-resolved-incident.
- A hallucinated root cause that led a customer to roll back the wrong service (used for evals, incident response and trust chapters).
- Sunsetting the legacy "Beacon Classic" correlation engine and migrating customers.
- EU customers asking for AI Act documentation.
