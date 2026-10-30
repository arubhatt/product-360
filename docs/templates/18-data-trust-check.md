<!-- Data trust check · from Chapter 18 of The Product 360 Handbook -->

# Data trust check · [Report or analysis] · [Date]

Run before any number drives a decision. Record failures before the answer, not after.

| Check | Question | Result | Action if failed |
|---|---|---|---|
| Freshness | When was each source last updated? Is that later than the decision needs? | | |
| Quality | Are null, duplicate or out-of-range rates unusual? | | |
| Volume | Did event or row counts move outside the normal range? | | |
| Schema | Did any field, event name or definition change in the last 30 days? | | |
| Lineage | Which upstream sources feed this number? Did any have a problem? | | |
| Definition | Which dictionary entry and version was used? | | |
| Denominator | What's the base, and how many accounts does it contain? | | |
| Hand check | Does one named account reconcile across sources? | | |

**Verdict:** Trust / Trust with caveats (list) / Don't use yet
