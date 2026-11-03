# The Product 360 Handbook

*Building, Running and Governing Products in the AI Era.* Read it at <https://arubhatt.github.io/product-360/>. A field guide and operating system for product leaders, 2026 edition. Curated by Arunabh Bhattacharjee.

The handbook is a self-contained textbook for product managers and a framework for building a "Product 360" (the complete set of artifacts, rituals and decisions that make a product legible) for any product surface area. It covers the topics of the Product Management 360 certificate, plus go-to-market, product operations, lifecycle management and AI-era product management. It is independent of Cornell University and eCornell.

## Read it locally

The built site lives in `docs/` and has no runtime dependencies. Open `docs/index.html` in a browser, or serve it:

```bash
python3 -m http.server 8360 --directory docs
```

Then visit <http://localhost:8360>.

## Build it

```bash
python3 -m venv .venv
```

```bash
.venv/bin/pip install -r requirements.txt
```

```bash
.venv/bin/python build.py
```

Add `--pdf` to also print the full book to `docs/product-360-handbook.pdf` (uses Google Chrome in headless mode).

## Repository layout

| Path | What it is |
|---|---|
| `content/book.json` | Table of contents: parts, chapters, summaries, course mapping |
| `content/chapters/` | Chapter sources in Markdown |
| `content/beacon-case.md` | Facts for the running Beacon case, used by every chapter |
| `assets/` | CSS and JavaScript for the site |
| `build.py` | Static site generator |
| `docs/` | Built site, ready for GitHub Pages |
| `AUTHORING.md` | How chapters are written: shape, voice, markup, quality gate |
| `REFERENCES.md` | Every source used, grouped by chapter |
| `GRILL.md` | The scoping decisions behind the book |

## Read it online

Live at <https://arubhatt.github.io/product-360/>, published with GitHub Pages from the `/docs` folder on `main`. Pushing a rebuilt `docs/` to `main` updates the site.

## License

All rights reserved for now. See `LICENSE`.
