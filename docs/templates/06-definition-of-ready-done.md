<!-- Definition of Ready and Definition of Done · from Chapter 06 of The Product 360 Handbook -->

# Definition of Ready and Done · [Team] · v[n] · [Date]

**Agreed by:** [PM, engineering lead, designer, QA]   **Review after:** any escaped defect, or quarterly

## Definition of Ready (keep it short; drop any line that never catches anything)
- [ ] Problem and customer evidence linked
- [ ] Acceptance criteria written as Given-When-Then, including error cases
- [ ] Permission, role and tenancy cases listed
- [ ] Dependencies named, each with an owner
- [ ] Design attached, or marked "no UI"
- [ ] Telemetry events defined
- [ ] Fits in one sprint (passes INVEST "Small")
- [ ] Security, privacy or compliance review need flagged
- [ ] AI features: risk class assigned and eval cases added

## Definition of Done
- [ ] Code reviewed by a person, including every agent-written change
- [ ] Automated tests pass, including the acceptance scenarios
- [ ] Behind a flag if not released to all customers; flag has a removal task and expiry date
- [ ] Docs and release notes drafted
- [ ] Telemetry live and checked in production
- [ ] Security checks pass
- [ ] Deployed to production (dark if needed)
- [ ] No new P0 or P1 bugs open against it
- [ ] AI features: evals pass at threshold; cost per task within budget; compliance documentation updated
- [ ] Actions that change customer systems: audit entry verified; kill switch tested
