# Authoring guide

How chapters of The Product 360 Handbook are written. Every chapter, whoever drafts it, follows this guide. The pilot chapters (00, 01 and 31) are the quality bar.

## Files

- `content/book.json`: table of contents. A chapter is published when its entry has a `file` and that file exists in `content/chapters/`.
- `content/chapters/NN-slug.md`: chapter source in Markdown.
- `content/beacon-case.md`: facts for the running case. Use them as given; don't invent conflicting numbers.
- `REFERENCES.md`: every source used, grouped by chapter. Sources never appear in the chapter text as links or footnotes.
- `build.py`: builds `docs/`. Run `.venv/bin/python build.py` (add `--pdf` for the PDF).

## Reader and voice

- Reader: a Senior to Principal PM in a B2B, enterprise or platform business. Newer PMs get `:::onramp` boxes; leaders get `:::leader` boxes.
- Second person, practitioner voice. Direct and opinionated where the evidence supports it. Explain the mechanism and the tradeoff, then how to apply it.
- Attribute ideas by name in the text ("Teresa Torres calls this..."). Paraphrase. Direct quotes are rare and under 15 words.
- Never invent statistics, studies, quotes or case facts. Beacon numbers come from the case bible. Real-world numbers need a source in `REFERENCES.md`.
- No em dashes anywhere. Use commas, colons, semicolons, parentheses or new sentences.
- No throat-clearing, puffery, "It's not X, it's Y" contrasts, recap endings or mic-drop lines.
- The book is self-contained. Point to other chapters of this book, never to other books or sites for the reader to go read.
- No employer-specific content. Real companies appear only through public facts.
- Data and analysis are taught at the level of questions, evidence and reports. No SQL, spreadsheet formulas or tool click-paths; assume an AI harness does the mechanics.

## Chapter shape

Open with a short lead paragraph (`<p class="lead">...</p>`), then these `##` sections. Headings can be specific to the chapter ("Why personas fail in B2B" rather than "Anti-patterns") but the order and content hold.

1. **Why this matters**
2. **Core concepts and frameworks** (usually several `###` subsections)
3. **How to apply it** (numbered method)
4. **The AI lens** (both: building AI-powered products, and doing the work with AI)
5. **The Beacon case** (worked example, inside or after the method)
6. **Product 360 artifacts** (templates)
7. **Prompts**
8. **Anti-patterns**
9. **Checklist**
10. **Key takeaways** (five to seven bullets, no slogans)

Target length: 4,000 to 6,000 words of prose, plus templates and prompts.

## Markup

Callouts:

```
:::key Optional title
Body in Markdown.
:::
```

Kinds: `key`, `note`, `ai`, `example` (Beacon), `warn` (anti-pattern), `onramp`, `leader`.

Prompts (collected into Appendix B):

````
```prompt title="Short imperative title"
Goal: ...
Paste in: ...

<prompt text, with [placeholders]>

Check the output: ...
```
````

Templates (collected into Appendix A and written to `docs/templates/<id>.md`):

````
```template id="kebab-id" title="Artifact name"
# Artifact name
...
```
````

Template ids must be unique across the book.

Checklists: a normal list with `- [ ] item` lines.

Diagrams: inline SVG inside `<figure class="fig" markdown="0">...</figure>`. Use classes `t` (label), `s` (small label), `box`, `ln`, and the CSS variables `var(--a1)`, `var(--a2)`, `var(--a3)`, `var(--text)`, `var(--muted)`, `var(--border-2)`, `var(--surface-2)` so diagrams work in light and dark mode. Add a `<figcaption>`.

## Prompts standard

Every prompt states its goal, what to paste in, the prompt itself and how to check the output. Prompts are model-agnostic. Prompts that would send customer or confidential data say so and remind the reader to use an approved tool.

## Quality gate

Before a chapter is marked done:

1. Run the `check` skill (strong) over the prose, protecting code, prompts, templates, names and URLs.
2. Confirm every external fact has a source in `REFERENCES.md`.
3. Build and read the page in the browser, light and dark.
