#!/usr/bin/env python3
"""Build the static site from docs/ markdown lessons into site/.

Pure stdlib + ``markdown``. Deterministic: run it twice, get identical
output. Run ``python3 build.py`` to (re)generate, or ``python3 verify.py``
to build and run the whole verification suite.
"""

import html
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

SPINE_MULTIPLIERS = {
    "white": 0.002252,   # b&w interior on white paper
    "cream": 0.0025,     # b&w interior on cream paper
    "color": 0.002347,   # standard color interior
}
BLEED = 0.125


def spine_width(pages: int, paper: str) -> float:
    """Spine width in inches for a given page count and paper stock."""
    if pages <= 0:
        raise ValueError("pages must be positive")
    if paper not in SPINE_MULTIPLIERS:
        raise KeyError(f"unknown paper stock: {paper!r}")
    return round(pages * SPINE_MULTIPLIERS[paper], 4)


def wrap_dimensions(trim_w: float, trim_h: float, pages: int, paper: str) -> tuple:
    """Full wrap (back+spine+front) with bleed, in inches, rounded to 4dp."""
    s = spine_width(pages, paper)
    w = round(trim_w * 2 + s + BLEED * 2, 4)
    h = round(trim_h + BLEED * 2, 4)
    return w, h


def px(width_in: float, height_in: float, dpi: int = 300) -> tuple:
    """Convert inches to rounded pixels at the given DPI."""
    return (round(width_in * dpi), round(height_in * dpi))


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Book Cover DIY Basics Guide</title>
<meta name="description" content="Beginner manual for designing clean, KDP-ready book covers yourself with free tools. By Asdale Dynamics, LLC.">
<link rel="stylesheet" href="{prefix}style.css">
</head>
<body>
<header class="site-header">
  <a class="home" href="{prefix}index.html">Book Cover DIY Basics Guide</a>
  <span class="byline">by Asdale Dynamics, LLC</span>
</header>
<main>
{body}
</main>
<nav class="pager">
  {prev_link}{next_link}
</nav>
<footer>
  <p>Part of the <a href="{prefix}index.html">Book Cover DIY Basics Guide</a>.
  © 2026 Asdale Dynamics, LLC — MIT licensed. Local spot checks only;
  nothing here publishes anything.</p>
</footer>
</body>
</html>
"""

def slug_of(md_path: Path) -> str:
    return md_path.stem


def title_of(md_text: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled lesson"


def render_page(body_html: str, title: str, href: str,
                prev_lesson=None, next_lesson=None) -> str:
    prefix = "../" if "/" in href else ""
    if prev_lesson:
        prev_link = '<a class="pager-prev" href="{href}">&larr; {label}</a>'.format(
            href=prev_lesson[0], label=prev_lesson[1])
    else:
        prev_link = '<span class="pager-prev"></span>'
    if next_lesson:
        next_link = '<a class="pager-next" href="{href}">{label} &rarr;</a>'.format(
            href=next_lesson[0], label=next_lesson[1])
    else:
        next_link = '<span class="pager-next"></span>'
    return TEMPLATE.format(
        title=html.escape(title),
        prefix=prefix,
        body=body_html,
        prev_link=prev_link,
        next_link=next_link,
    )


def build_site() -> list:
    """Generate site/ from docs/. Returns the list of lesson slugs."""
    md_paths = sorted(DOCS.glob("*.md"))
    if not md_paths:
        raise RuntimeError(f"no markdown lessons found in {DOCS}")
    SITE.mkdir(exist_ok=True)
    (SITE / "style.css").write_text((ROOT / "assets" / "style.css").read_text())

    renderer = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])

    entries = []  # (slug, title)
    pages_html = {}
    for i, path in enumerate(md_paths):
        text = path.read_text(encoding="utf-8")
        renderer.reset()
        body = renderer.convert(text)
        title = title_of(text)
        slug = slug_of(path)
        entries.append((slug, title))
        prev = None if i == 0 else (f"{md_paths[i-1].stem}.html", title_of(md_paths[i-1].read_text()))
        nxt = None if i == len(md_paths) - 1 else (
            f"{md_paths[i+1].stem}.html", title_of(md_paths[i+1].read_text()))
        page = render_page(body, title, f"{slug}.html", prev, nxt)
        pages_html[f"{slug}.html"] = page

    index_body = ["<h1>Book Cover DIY Basics Guide</h1>",
                  '<p class="lede">Design clean, KDP-ready covers yourself — with free tools,'
                  " plain English, and no condescension. Read the lessons in order:"
                  " genre first, math second, taste last.</p>",
                  '<p class="byline-note">Made by <strong>Asdale Dynamics, LLC</strong> —'
                  " beginner-friendly guides and practical tools, from Dylan Asdale"
                  " (<em>The Massive AI Manual</em>).</p>",
                  '<ol class="toc">']
    for slug, title in entries:
        index_body.append(f'<li><a href="{slug}.html">{html.escape(title)}</a></li>')
    index_body.append("</ol>")
    pages_html["index.html"] = render_page(
        "\n".join(index_body), "Index — Book Cover DIY Basics Guide",
        "index.html", None, (entries[0][0] + ".html", entries[0][1]))

    for fname, content in pages_html.items():
        (SITE / fname).write_text(content, encoding="utf-8")

    return [e[0] for e in entries]


if __name__ == "__main__":
    slugs = build_site()
    print(f"built {len(slugs)} lesson pages + index into site/:")
    for s in slugs:
        print(f"  {s}.html")
