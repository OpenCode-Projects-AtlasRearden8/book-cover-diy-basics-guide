# STATUS.md

Last updated: 2026-11-07

## What was built

A complete beginner manual — **Book Cover DIY Basics Guide** — for
designing clean, KDP-ready book covers yourself with free tools, plus a
static website that presents it lesson by lesson.

### Contents

| Area | Files | Notes |
|---|---|---|
| Manual (Markdown) | `docs/00`–`docs/09` (10 lessons) | Genre expectations, trim/margins/bleed, spine math, typography, vibe checklists, tool guides (Canva/GIMP/Affinity trial), amateur tells, pre-publish walkthrough, cheat sheet |
| Static site | `site/index.html` + 10 lesson pages + `style.css` | Generated from `docs/`; prev/next navigation, index table of contents |
| Site generator | `build.py` | Markdown → HTML, stdlib + `markdown` package |
| Verification | `verify.py`, `tests` (in verify.py) | 16 tests: spine/wrap math, site output, repo hygiene |
| Assets | `assets/style.css` | Warm print-inspired stylesheet |
| Meta | `README.md`, `LICENSE` (MIT), `.gitignore` | Copyright (c) 2026 Asdale Dynamics, LLC |

Scope kept exactly as requested: **no publishing-platform
integrations of any kind.** The manual only teaches and describes
local, screenshots-style spot checks (front/back/spine crops you make
on your own machine). Related-but-distinct: automated validation lives
in the separate `kdp-cover-bleed-checker-cli` project.

## How to run it

```bash
python3 verify.py   # builds site/ and runs all 16 tests
python3 build.py    # rebuilds site/ from docs/ alone
```

Requirements: Python 3 with `pip install markdown`. Then open
`site/index.html` in any browser (fully static; no server needed).

## Verification results

- `python3 verify.py` → **16/16 tests passed, exit code 0**, including:
  - Spine math matches the lesson tables (white 0.002252, cream
    0.0025, color 0.002347 inches/page) and the worked 6x9/288-page
    example (12.97" x 9.25" wrap = 3891 x 2775 px at 300 DPI)
  - Every lesson page and index generates as complete HTML with
    working prev/next links; tables render as real `<table>` elements
  - LICENSE contains the exact line
    `Copyright (c) 2026 Asdale Dynamics, LLC`; README credits the LLC
  - Secret-pattern scan (AWS keys, generic API-key shapes, private
    key blocks) across all shipped files found nothing
- Manual prose was proofread pass-over-pass (fixed typos, awkward
  phrasing, and numbering slips introduced while drafting).

## Known gaps / honest limits

- **Print specs drift.** Spine multipliers and margin rules are
  widely-cited approximations, not a guarantee; the lessons
  deliberately route readers to KDP's official cover-dimension
  calculator as the source of truth, and tests only verify internal
  consistency of *our own* math.
- **No images.** The site is text-only for now; lesson diagrams
  (bleed zones, spine lanes) are described in words and code blocks.
- **Menu placements** in the tool guides can drift as Canva/GIMP/
  Affinity update; the step *order* is the durable part.
- **English only.** No i18n of the manual.
- The site ships prebuilt HTML; since it is static and checked-in,
  remember to run `build.py` after editing `docs/`.
