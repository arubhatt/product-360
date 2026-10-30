<!-- Sentiment analysis request · from Chapter 09 of The Product 360 Handbook -->

# Sentiment analysis request · [Topic] · [Date]

**Requester:** [PM]   **Decision it informs:** [Decision]   **Due:** [Date]

## Question
[For example: "What are the main sources of frustration among mid-market customers in the last two quarters, and are they linked to lower retention?"]

## Sources and window
| Source | Connector or export | Time window | Approx. volume | Data restrictions |
|---|---|---|---|---|
| | | | | |

## Data handling
- Personal data to remove:
- Customer contract or residency limits checked by: [name]
- Approved tool:

## Codebook
Use codebook v[n] (attached). New themes may be proposed separately, not added.
Sentiment: positive / negative / mixed / neutral, per theme mentioned (aspect level), not only per item.

## Known hard cases to test
- Negation ("would be great if it stopped...")
- Sarcasm
- Positive question framing with negative answers
- Domain terms: [list]

## Validation
- Human-labeled sample: [n] random items, labeled by [names] before seeing machine output
- Report agreement, disagreements and theme shares (human vs machine)

## Outputs
- Theme table with counts, shares and trends
- Three verbatims per theme with source references
- Link to account retention and revenue where the source allows
- Confidence statement and known weaknesses
