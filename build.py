#!/usr/bin/env python3
"""Build the Product 360 Handbook into a static site in docs/.

Source lives in content/: book.json holds the table of contents and
content/chapters/*.md holds the chapters. Run:

    .venv/bin/python build.py          # build the site
    .venv/bin/python build.py --pdf    # also print the full book to PDF

Chapter Markdown supports a few extensions on top of standard Markdown:

    :::note Title           callout box (kinds: note, ai, warn, example,
    ...                     onramp, leader, key)
    :::

    ```prompt title="..."   copy-ready AI prompt, collected into Appendix B
    ```template id="..." title="..."
                            copy-ready artifact template, collected into
                            Appendix A and written to docs/templates/<id>.md
    - [ ] item              interactive checklist item (saved per browser)
"""

import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import markdown
from markdown.extensions.toc import slugify

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
CHAPTERS = CONTENT / "chapters"
ASSETS = ROOT / "assets"
OUT = ROOT / "docs"
VERSION = "1"

CALLOUT_LABELS = {
    "note": "Note",
    "ai": "The AI lens",
    "warn": "Anti-pattern",
    "example": "Beacon case",
    "onramp": "On-ramp",
    "leader": "For product leaders",
    "key": "Key idea",
}

FENCE_RE = re.compile(r"^```(prompt|template)([^\n]*)\n(.*?)\n```[ \t]*$", re.M | re.S)
ATTR_RE = re.compile(r'(\w+)="([^"]*)"')
CALLOUT_RE = re.compile(r"^:::(\w+)[ \t]*([^\n]*)\n(.*?)\n:::[ \t]*$", re.M | re.S)


# ---------------------------------------------------------------- the book


def load_book():
    book = json.loads((CONTENT / "book.json").read_text())
    entries = []
    for ch in book["front"]:
        entries.append({**ch, "part": None, "kind": "front"})
    for part in book["parts"]:
        for ch in part["chapters"]:
            entries.append({**ch, "part": part, "kind": "chapter"})
    for ap in book["appendices"]:
        entries.append({**ap, "part": None, "kind": "appendix"})
    for e in entries:
        e["url"] = e["slug"] + ".html"
        src = CHAPTERS / (e.get("file") or e["slug"] + ".md")
        e["src"] = src if src.exists() else None
        e["ready"] = bool(e["src"] or e.get("generated"))
    return book, entries


def label(e):
    if e["kind"] == "appendix":
        return "Appendix " + e["num"]
    if e["num"]:
        return "Chapter " + e["num"]
    return ""


# ---------------------------------------------------------------- markdown


def render_block(kind, attrs, body, entry, store):
    title = attrs.get("title", "Prompt" if kind == "prompt" else "Template")
    esc = html.escape(body)
    if kind == "prompt":
        store["prompts"].append({"title": title, "body": body, "entry": entry})
        icon = "✦"
        tag = "Prompt"
        extra = ""
    else:
        tid = attrs.get("id") or slugify(title, "-")
        store["templates"].append({"id": tid, "title": title, "body": body, "entry": entry})
        icon = "▤"
        tag = "Template"
        extra = f'<a class="blk-dl" href="templates/{tid}.md" download>Download .md</a>'
    return (
        f'<div class="blk blk-{kind}"><div class="blk-h"><span class="blk-tag">{icon} {tag}</span>'
        f'<span class="blk-t">{html.escape(title)}</span><span class="blk-actions">{extra}'
        f'<button class="blk-copy" type="button">Copy</button></span></div>'
        f"<pre><code>{esc}</code></pre></div>"
    )


def md_to_html(text, entry, store):
    stash = []

    def keep(fragment):
        stash.append(fragment)
        return f"\n\nSTASH{len(stash) - 1}END\n\n"

    def fence(m):
        attrs = dict(ATTR_RE.findall(m.group(2)))
        return keep(render_block(m.group(1), attrs, m.group(3), entry, store))

    text = FENCE_RE.sub(fence, text)

    def callout(m):
        kind = m.group(1)
        title = m.group(2).strip() or CALLOUT_LABELS.get(kind, kind.title())
        inner = md().convert(m.group(3))
        return keep(
            f'<aside class="callout callout-{kind}"><div class="callout-h">'
            f'<span class="callout-k">{CALLOUT_LABELS.get(kind, kind.title())}</span>'
            f"{'<span class=callout-t>' + html.escape(title) + '</span>' if title != CALLOUT_LABELS.get(kind) else ''}"
            f"</div>{inner}</aside>"
        )

    text = CALLOUT_RE.sub(callout, text)
    conv = md()
    out = conv.convert(text)
    for i, frag in enumerate(stash):
        out = out.replace(f"<p>STASH{i}END</p>", frag)
    for i, frag in enumerate(stash):
        out = out.replace(f"STASH{i}END", frag)

    count = [0]

    def check(m):
        count[0] += 1
        return (
            f'<li class="chk"><label><input type="checkbox" data-k="{entry["slug"]}-{count[0]}">'
            f"<span>{m.group(1)}</span></label></li>"
        )

    out = re.sub(r"<li>\[ \] (.*?)</li>", check, out, flags=re.S)
    out = re.sub(r"<table>", '<div class="tbl"><table>', out)
    out = re.sub(r"</table>", "</table></div>", out)
    return out, conv.toc_tokens


def md():
    return markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "attr_list", "md_in_html", "sane_lists", "smarty"],
        extension_configs={"toc": {"toc_depth": "2-3"}, "smarty": {"smart_dashes": False}},
    )


# ---------------------------------------------------------------- layout


def sidebar(book, entries, current):
    def link(e):
        cls = ["nav-l"]
        if e is current:
            cls.append("on")
        if not e["ready"]:
            cls.append("soon")
        num = f'<span class="nav-n">{e["num"]}</span>' if e["num"] else '<span class="nav-n">·</span>'
        return f'<a class="{" ".join(cls)}" href="{e["url"]}">{num}<span>{html.escape(e["title"])}</span></a>'

    rows = ['<nav class="nav" aria-label="Chapters">']
    rows.append('<div class="nav-g">' + "".join(link(e) for e in entries if e["kind"] == "front") + "</div>")
    for part in book["parts"]:
        mine = [e for e in entries if e["part"] is part]
        is_open = current is not None and current["part"] is part
        rows.append(
            f'<details class="nav-p"{" open" if is_open else ""}><summary><span class="nav-pm" aria-hidden="true"></span>'
            f'<span class="nav-pn">Part {part["num"]}</span><span class="nav-pt">{html.escape(part["title"])}</span></summary>'
            + "".join(link(e) for e in mine)
            + "</details>"
        )
    aps = [e for e in entries if e["kind"] == "appendix"]
    is_open = current is not None and current["kind"] == "appendix"
    rows.append(
        f'<details class="nav-p"{" open" if is_open else ""}><summary><span class="nav-pm" aria-hidden="true"></span>'
        '<span class="nav-pn">Back</span><span class="nav-pt">Appendices</span></summary>'
        + "".join(link(e) for e in aps)
        + "</details>"
    )
    rows.append("</nav>")
    return "".join(rows)


LOGO = (
    '<svg class="logo" viewBox="0 0 32 32" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="var(--a1)"/><stop offset=".5" stop-color="var(--a2)"/><stop offset="1" stop-color="var(--a3)"/>'
    '</linearGradient></defs><circle cx="16" cy="16" r="12" fill="none" stroke="url(#lg)" stroke-width="4" '
    'stroke-dasharray="66 9.4" stroke-linecap="round" transform="rotate(-80 16 16)"/><circle cx="16" cy="16" r="3.2" fill="var(--a2)"/></svg>'
)


def page(book, entries, current, title, body, toc_html="", description=""):
    side = sidebar(book, entries, current)
    pdf = '<a class="ibtn hide-sm" href="product-360-handbook.pdf">PDF</a>' if (OUT / "product-360-handbook.pdf").exists() else ""
    rail = f'<aside class="rail" aria-label="On this page"><div class="rail-in"><div class="rail-h">On this page</div>{toc_html}</div></aside>' if toc_html else ""
    full_title = html.escape(f"{title} · {book['title']}" if current else book["title"])
    return f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{html.escape(description or book['tagline'])}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;0,7..72,600;1,7..72,400&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="assets/css/book.css?v={VERSION}">
<script>try{{var t=localStorage.getItem('p360-theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head>
<body class="{'has-rail' if toc_html else ''}">
<div class="progress" aria-hidden="true"><span></span></div>
<header class="top">
  <button class="ibtn menu" id="menu-btn" aria-label="Open chapters">☰</button>
  <a class="brand" href="index.html">{LOGO}<span class="brand-t">Product <b>360</b></span><span class="brand-s hide-sm">Handbook</span></a>
  <div class="top-r">
    <button class="ibtn search-btn" data-search-open aria-label="Search"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/></svg><span class="hide-sm">Search</span><kbd class="hide-sm">/</kbd></button>
    {pdf}
    <button class="ibtn" id="theme-btn" aria-label="Toggle light and dark"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>
  </div>
</header>
<div class="shell">
  <aside class="side" id="side">{side}</aside>
  <div class="scrim" id="scrim"></div>
  <main class="main" id="main">{body}</main>
  {rail}
</div>
<div class="search-modal" id="search-modal" hidden>
  <div class="search-box" role="dialog" aria-label="Search the handbook">
    <input id="search-input" type="search" placeholder="Search the handbook…" autocomplete="off">
    <div id="search-results" class="search-results"></div>
    <div class="search-foot"><kbd>↑</kbd><kbd>↓</kbd> to move · <kbd>Enter</kbd> to open · <kbd>Esc</kbd> to close</div>
  </div>
</div>
<script src="assets/js/search-index.js?v={VERSION}"></script>
<script src="assets/js/book.js?v={VERSION}"></script>
</body>
</html>
"""


def toc_list(tokens):
    if not tokens:
        return ""
    items = []
    for t in tokens:
        kids = "".join(f'<li class="l3"><a href="#{c["id"]}">{c["name"]}</a></li>' for c in t.get("children", []))
        items.append(f'<li><a href="#{t["id"]}">{t["name"]}</a></li>{kids}')
    return '<ul class="rail-l">' + "".join(items) + "</ul>"


def chapter_head(e, minutes=None, artifacts=0, prompts=0):
    kicker = []
    if e["part"]:
        kicker.append(f'Part {e["part"]["num"]} · {html.escape(e["part"]["title"])}')
    elif e["kind"] == "appendix":
        kicker.append("Appendices")
    else:
        kicker.append("Front matter")
    meta = []
    if minutes:
        meta.append(f"{minutes} min read")
    if artifacts:
        meta.append(f"{artifacts} template{'s' if artifacts != 1 else ''}")
    if prompts:
        meta.append(f"{prompts} prompt{'s' if prompts != 1 else ''}")
    num = f'<div class="ch-num">{e["num"]}</div>' if e["num"] else ""
    return (
        f'<header class="ch-head">{num}<div class="ch-kicker">{" · ".join(kicker)}</div>'
        f'<h1>{html.escape(e["title"])}</h1><p class="ch-sum">{html.escape(e["summary"])}</p>'
        + (f'<div class="ch-meta">{" · ".join(meta)}</div>' if meta else "")
        + "</header>"
    )


def pager(entries, e):
    i = entries.index(e)
    prev = entries[i - 1] if i > 0 else None
    nxt = entries[i + 1] if i + 1 < len(entries) else None
    out = ['<nav class="pager">']
    if prev:
        out.append(f'<a class="pg pg-p" href="{prev["url"]}"><span>← Previous</span><b>{html.escape(prev["title"])}</b></a>')
    else:
        out.append('<a class="pg pg-p" href="index.html"><span>← Home</span><b>Contents</b></a>')
    if nxt:
        out.append(f'<a class="pg pg-n" href="{nxt["url"]}"><span>Next →</span><b>{html.escape(nxt["title"])}</b></a>')
    out.append("</nav>")
    return "".join(out)


# ---------------------------------------------------------------- pages


def plain_text(fragment):
    fragment = re.sub(r"<(script|style|svg)[^>]*>.*?</\1>", " ", fragment, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def index_sections(e, body_html, search):
    parts = re.split(r'(<h[23][^>]*id="[^"]+"[^>]*>.*?</h[23]>)', body_html, flags=re.S)
    head, anchor = e["title"], ""
    buf = parts[0]
    def flush(h, a, b):
        text = plain_text(b)
        if text:
            search.append({"c": e["title"], "n": label(e), "h": h, "u": e["url"] + (f"#{a}" if a else ""), "x": text[:4000]})
    for chunk in parts[1:]:
        m = re.match(r'<h[23][^>]*id="([^"]+)"[^>]*>(.*?)</h[23]>', chunk, flags=re.S)
        if m:
            flush(head, anchor, buf)
            anchor, head, buf = m.group(1), plain_text(m.group(2)), ""
        else:
            buf += chunk
    flush(head, anchor, buf)


def planned_body(e):
    outline = e.get("outline")
    items = "".join(f"<li>{html.escape(x)}</li>" for x in outline) if outline else ""
    return (
        '<div class="soon-card"><div class="soon-badge">In production</div>'
        "<p>This chapter is being researched and written. It will follow the standard chapter shape: "
        "why it matters, core frameworks, how to apply them, the AI lens, the Beacon case, templates, prompts, "
        "anti-patterns and a checklist.</p>"
        + (f"<h2>Planned scope</h2><ul>{items}</ul>" if items else "")
        + "</div>"
    )


def build_generated(e, entries, store):
    kind = e["generated"]
    if kind == "artifacts":
        out = ['<div class="prose"><p>Every template in the handbook, in chapter order. Copy one into your doc tool, '
               "or download the Markdown file. Each template links back to the chapter that explains how to use it.</p>"]
        current = None
        for t in store["templates"]:
            if t["entry"] is not current:
                current = t["entry"]
                out.append(f'<h2 id="{current["slug"]}">{label(current)}: {html.escape(current["title"])}</h2>')
            out.append(render_lib_item("template", t))
        if not store["templates"]:
            out.append("<p>Templates appear here as chapters are published.</p>")
        out.append("</div>")
        return "".join(out)
    if kind == "prompts":
        out = ['<div class="prose"><p>Every prompt in the handbook, grouped by chapter. The prompts are model-agnostic: '
               "they work in Claude, ChatGPT, Gemini or Copilot. Replace anything in <code>[square brackets]</code> "
               "with your own context before you run them.</p>"]
        current = None
        for p in store["prompts"]:
            if p["entry"] is not current:
                current = p["entry"]
                out.append(f'<h2 id="{current["slug"]}">{label(current)}: {html.escape(current["title"])}</h2>')
            out.append(render_lib_item("prompt", p))
        if not store["prompts"]:
            out.append("<p>Prompts appear here as chapters are published.</p>")
        out.append("</div>")
        return "".join(out)
    if kind == "coursemap":
        rows = []
        for c in entries:
            if c.get("cornell"):
                rows.append(f'<tr><td><a href="{c["url"]}">{c["num"]} {html.escape(c["title"])}</a></td><td>{html.escape(c["cornell"])}</td></tr>')
        return (
            '<div class="prose"><p>This handbook is a companion text for the topics in the '
            '<a href="https://ecornell.cornell.edu/certificates/engineering/product-management-360/">Product Management 360 certificate</a>. '
            "It is independent and is not affiliated with or endorsed by Cornell University or eCornell. "
            "The chapters cover each course topic at the level of product decisions. The data courses (spreadsheets, SQL, visualization) "
            "are covered in Part IV the way a product leader works in 2026: by asking the right questions of an AI harness, not by learning syntax.</p>"
            '<div class="tbl"><table><thead><tr><th>Handbook chapter</th><th>Certificate course</th></tr></thead><tbody>'
            + "".join(rows)
            + "</tbody></table></div>"
            "<p>Chapters without a course mapping (go-to-market, product operations, lifecycle, AI-era product management, leadership "
            "and the capstone) extend the certificate into the rest of the Product 360.</p></div>"
        )
    return ""


def render_lib_item(kind, item):
    e = item["entry"]
    back = f'<a class="blk-src" href="{e["url"]}">from {label(e) or e["title"]}</a>'
    extra = f'<a class="blk-dl" href="templates/{item["id"]}.md" download>Download .md</a>' if kind == "template" else ""
    tag = "✦ Prompt" if kind == "prompt" else "▤ Template"
    return (
        f'<div class="blk blk-{kind} blk-fold"><div class="blk-h"><span class="blk-tag">{tag}</span>'
        f'<span class="blk-t">{html.escape(item["title"])}</span><span class="blk-actions">{back}{extra}'
        f'<button class="blk-copy" type="button">Copy</button><button class="blk-toggle" type="button">Show</button></span></div>'
        f'<pre><code>{html.escape(item["body"])}</code></pre></div>'
    )


def home(book, entries):
    ready = [e for e in entries if e["ready"] and e["num"] and e["kind"] != "appendix"]
    cards = []
    for part in book["parts"]:
        items = []
        for e in [x for x in entries if x["part"] is part]:
            state = "" if e["ready"] else '<span class="badge">soon</span>'
            items.append(
                f'<a class="toc-i{"" if e["ready"] else " soon"}" href="{e["url"]}"><span class="toc-n">{e["num"]}</span>'
                f'<span><span class="toc-t">{html.escape(e["title"])}</span>{state}<span class="toc-x">{html.escape(e["summary"])}</span></span></a>'
            )
        cards.append(
            f'<section class="part-card"><div class="part-h"><span class="part-n">Part {part["num"]}</span>'
            f'<h3>{html.escape(part["title"])}</h3><p>{html.escape(part["blurb"])}</p></div><div class="toc-g">{"".join(items)}</div></section>'
        )
    front = "".join(
        f'<a class="toc-i" href="{e["url"]}"><span class="toc-n">{e["num"] or "·"}</span><span><span class="toc-t">{html.escape(e["title"])}</span>'
        f'<span class="toc-x">{html.escape(e["summary"])}</span></span></a>'
        for e in entries if e["kind"] == "front"
    )
    back = "".join(
        f'<a class="toc-i{"" if e["ready"] else " soon"}" href="{e["url"]}"><span class="toc-n">{e["num"]}</span><span><span class="toc-t">{html.escape(e["title"])}</span>'
        f'{"" if e["ready"] else "<span class=badge>soon</span>"}<span class="toc-x">{html.escape(e["summary"])}</span></span></a>'
        for e in entries if e["kind"] == "appendix"
    )
    wheel = (ROOT / "content" / "wheel.svg").read_text()
    return f"""
<section class="hero">
  <div class="hero-t">
    <div class="eyebrow">{html.escape(book['series'])} · {html.escape(book['edition'])}</div>
    <h1>{html.escape(book['title'])}</h1>
    <p class="hero-sub">{html.escape(book['subtitle'])}</p>
    <p class="hero-tag">{html.escape(book['tagline'])}.</p>
    <div class="hero-cta"><a class="btn" href="00-product-360-framework.html">Start with the framework</a><a class="btn btn-g" href="preface.html">How to use this book</a></div>
    <div class="hero-stats"><span><b>{len([e for e in entries if e['kind']=='chapter'])+1}</b> chapters</span><span><b>10</b> parts</span><span><b>{len(ready)}</b> published</span></div>
  </div>
  <div class="hero-w">{wheel}</div>
</section>
<section class="part-card"><div class="part-h"><span class="part-n">Front</span><h3>Start here</h3><p>The model the rest of the book builds on.</p></div><div class="toc-g">{front}</div></section>
{''.join(cards)}
<section class="part-card"><div class="part-h"><span class="part-n">Back</span><h3>Appendices</h3><p>The libraries you will keep open in a tab.</p></div><div class="toc-g">{back}</div></section>
<footer class="foot">Curated by <a href="{book['github']}">{html.escape(book['author'])}</a> · {html.escape(book['series'])}</footer>
"""


# ---------------------------------------------------------------- build


def build(make_pdf=False):
    book, entries = load_book()
    if OUT.exists():
        keep_pdf = OUT / "product-360-handbook.pdf"
        pdf_bytes = keep_pdf.read_bytes() if keep_pdf.exists() and not make_pdf else None
        shutil.rmtree(OUT)
    else:
        pdf_bytes = None
    (OUT / "templates").mkdir(parents=True)
    shutil.copytree(ASSETS, OUT / "assets")
    if pdf_bytes:
        (OUT / "product-360-handbook.pdf").write_bytes(pdf_bytes)

    store = {"prompts": [], "templates": []}
    rendered = {}
    for e in entries:
        if e["src"]:
            body, toc = md_to_html(e["src"].read_text(), e, store)
            rendered[e["slug"]] = (body, toc)

    search = []
    print_parts = []
    for e in entries:
        if e["slug"] in rendered:
            body, toc = rendered[e["slug"]]
            words = len(plain_text(body).split())
            n_t = sum(1 for t in store["templates"] if t["entry"] is e)
            n_p = sum(1 for p in store["prompts"] if p["entry"] is e)
            head = chapter_head(e, max(1, round(words / 230)), n_t, n_p)
            main = f'<article class="ch">{head}<div class="prose">{body}</div>{pager(entries, e)}</article>'
            index_sections(e, body, search)
            print_parts.append(f'<article class="ch print-ch">{head}<div class="prose">{body}</div></article>')
            (OUT / e["url"]).write_text(page(book, entries, e, e["title"], main, toc_list(toc), e["summary"]))
        elif e.get("generated"):
            body = build_generated(e, entries, store)
            main = f'<article class="ch">{chapter_head(e)}{body}{pager(entries, e)}</article>'
            index_sections(e, body, search)
            (OUT / e["url"]).write_text(page(book, entries, e, e["title"], main, "", e["summary"]))
        else:
            main = f'<article class="ch">{chapter_head(e)}<div class="prose">{planned_body(e)}</div>{pager(entries, e)}</article>'
            (OUT / e["url"]).write_text(page(book, entries, e, e["title"], main, "", e["summary"]))

    for t in store["templates"]:
        src = t["entry"]
        (OUT / "templates" / f"{t['id']}.md").write_text(
            f"<!-- {t['title']} · from {label(src) or src['title']} of {book['title']} -->\n\n{t['body']}\n"
        )

    (OUT / "index.html").write_text(page(book, entries, None, book["title"], home(book, entries)))
    (OUT / "assets" / "js" / "search-index.js").write_text(
        "window.P360_INDEX=" + json.dumps(search, ensure_ascii=False, separators=(",", ":")) + ";\n"
    )
    (OUT / ".nojekyll").write_text("")
    write_references(book, entries)
    cover = (
        f'<section class="print-cover">{LOGO}<div class="eyebrow">{html.escape(book["series"])} · {html.escape(book["edition"])}</div>'
        f'<h1>{html.escape(book["title"])}</h1><p class="hero-sub">{html.escape(book["subtitle"])}</p>'
        f'<p class="hero-tag">{html.escape(book["tagline"])}.</p><p class="cover-by">Curated by {html.escape(book["author"])}</p></section>'
    )
    print_html = page(book, entries, None, book["title"], cover + "".join(print_parts)).replace('<body class="', '<body class="print-all ')
    (OUT / "print.html").write_text(print_html.replace('data-theme="dark"', 'data-theme="light"'))
    print(f"Built {len(entries)} pages, {len(rendered)} written chapters, "
          f"{len(store['templates'])} templates, {len(store['prompts'])} prompts -> {OUT}")

    if make_pdf:
        pdf(OUT / "print.html", OUT / "product-360-handbook.pdf")
        build(make_pdf=False)


def write_references(book, entries):
    """Assemble REFERENCES.md from content/refs/<slug>.md, in book order."""
    out = [
        "# References\n",
        f"Every source used in {book['title']}, grouped by chapter. The chapters attribute ideas by name "
        "in the text but carry no links or footnotes; this file is where the sources live. Each entry gives "
        "author, title, publisher or site, year, URL where one exists, and what the source was used for. "
        "Web sources were accessed in October 2026.\n",
    ]
    for e in entries:
        ref = ROOT / "content" / "refs" / f"{e['slug']}.md"
        if ref.exists() and ref.read_text().strip():
            out.append(f"## {label(e) + ': ' if label(e) else ''}{e['title']}\n")
            out.append(ref.read_text().strip() + "\n")
    (ROOT / "REFERENCES.md").write_text("\n".join(out))


def pdf(src, dst):
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    subprocess.run(
        [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=15000",
         f"--print-to-pdf={dst}", src.resolve().as_uri()],
        check=True, capture_output=True,
    )
    print(f"PDF -> {dst}")


if __name__ == "__main__":
    build(make_pdf="--pdf" in sys.argv)
