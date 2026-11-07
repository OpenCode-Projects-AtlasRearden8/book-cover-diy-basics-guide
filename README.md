# Book Cover DIY Basics Guide

A beginner-friendly manual for designing clean, KDP-ready book covers
yourself, using free tools (Canva's free tier, GIMP, or an Affinity
trial). Explains genre expectations, safe margins and bleed, spine
math for print, typography, fits-the-vibe checklists, common amateur
tells, and a final pre-publish walkthrough — all in plain English,
step by step, never condescending.

Brought to you by **Asdale Dynamics, LLC** — Dylan Asdale's company
for beginner-friendly AI education, books and guides, and practical
tools the LLC can publish or sell. Written in the same spirit as
*The Massive AI Manual*: like a friend would, no jargon walls.

## What's in here

- `docs/` — the manual itself, as Markdown lessons:
  - `00-start-here.md` — how to use the manual, tool choice
  - `01-genre-expectations.md` — what each genre's shelf looks like
  - `02-trim-sizes-margins-bleed.md` — bleed, safe margins, wrap math
  - `03-spine-math.md` — pages x multiplier, worked examples
  - `04-typography.md` — two fonts, hierarchy, tracking, alignment
  - `05-fits-the-vibe-checklist.md` — thumbnail / squint / shelf tests
  - `06-tool-guides.md` — step-by-step Canva, GIMP, Affinity trial
  - `07-amateur-tells.md` — 15 tells, each with a five-minute fix
  - `08-pre-publish-walkthrough.md` — export-day checklist
  - `09-cheat-sheet.md` — quick-reference appendix
- `site/` — a static site with one HTML page per lesson + an index
  (generated from `docs/` by `build.py`).
- `build.py` — regenerates the static site from `docs/`.
- `verify.py` — runs all verification (build + tests).
- `tests/` — automated checks (spine math, generated output, hygiene).

## Running it

Requirements: Python 3 with the `markdown` package
(`pip install markdown`), or just run:

```bash
python3 verify.py
```

That builds the site into `site/` and runs the verification suite.

To build only:

```bash
python3 build.py
```

Then open `site/index.html` in any browser. No server needed — the
site is plain static HTML/CSS.

## Design notes

- Nothing here publishes anything. No publishing-platform integrations
  — the manual only teaches and offers local "screenshots-style" spot
  checks of your exported files (front/back/spine crops, pixel math).
- This project is the *learning* manual. For automated validation of a
  cover file against KDP math, see the separate
  `kdp-cover-bleed-checker-cli` project.
- Print specs drift; the manual repeatedly points you at the official
  KDP cover-dimension calculator as the source of truth. The math here
  teaches you why the calculator's numbers are what they are.
- No secrets, API keys, or personal data — it's all static text.

## License

MIT — see `LICENSE`. Copyright (c) 2026 Asdale Dynamics, LLC.
