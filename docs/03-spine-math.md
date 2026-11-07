# Lesson 3 — Spine Math for Print

The spine is the one part of the cover where being wrong is visible
from across a room: a spine too narrow for your letters, or front/back
art that got baked into the spine area because you guessed the width.
Here is the actual math, and it is friendlier than it sounds.

## The spine formula (with honest caveats)

Spine width = **pages x multiplier**, where the multiplier depends on
your paper stock. The multipliers below are the widely-cited KDP
industry approximations for common stocks:

| Paper stock | Multiplier (inches per page) |
|---|---|
| Black & white interior on **white paper** | 0.002252 |
| Black & white interior on **cream paper** | 0.0025 |
| Standard **color** interior | 0.002347 |
| **Premium color** interior | 0.002347 (use KDP's template for exact) |

Example: 320-page novel, white paper b&w:

```
spine = 320 x 0.002252 = 0.72064"  → build at ~0.72"
```

> **The friendly warning.** These multipliers are approximations that
> drift slightly with press settings. The *always-safe* workflow is:
> use the **KDP cover-dimension calculator** (free, on kdp.amazon.com)
> to generate an exact-size template PNG or PSD, then design inside
> that template. This lesson teaches you the math so the calculator's
> numbers never surprise you.

## What changes with the size of the spine

- **Below ~100 pages**: the spine is thin (a 90-page 6x9 on white
  paper is about 0.20"). **Do not put text on the spine.** It will
  likely be illegible and may not survive the folding/gluing process
  cleanly. Keep the spine area artwork-only, matching front and back.
- **100+ pages**: spine text is acceptable. Use a font sized so the
  title reads clearly, vertically centered, with breathing room equal
  to at least ~0.0625" above and below the text block.
- **Horizontal centering**: spine letters should be optically centered
  (slightly-high of true center feels right; nobody knows why; trust
  the eye).

## A worked example you can copy

Book: 6" x 9" trim, 288 pages, b&w on cream paper.

```
spine  = 288 x 0.0025 = 0.72"
wrap width  = (6 x 2) + 0.72 + 0.25 = 12.97"
wrap height = 9 + 0.25              = 9.25"
front panel starts at: 0.125 (bleed) + 6 + 0.72 = 6.845" from left
back panel ends at:    0.125 (bleed) + 6        = 6.125"  from left
spine occupies: 6.125" to 6.845"
```

Design your wrap at 12.97" x 9.25" @ 300 DPI (3891 x 2775 px) and use
vertical guides at 6.125" and 6.845" so the spine has its own lane.

## DPI math (why 300)

KDP requires print covers at **300 DPI**. Convert inches to pixels
simply by multiplying by 300:

```
12.97" x 9.25"  →  (12.97 x 300) x (9.25 x 300)  px
                →  3891 x 2775 px
```

Same trick for ebook (which is measured in pixels directly — Lesson 2).

## Three spine mistakes

1. **Eyeballing the width.** "Looks about an inch" is how people end
   up with a 0.72" spine on a 1.06" book. Compute; never guess.
2. **Backing spine art with way too much contrast** between spine and
   panels, so any tiny press shift makes the spine look like a sticker.
   Keep the cover background continuous across the spine when you can.
3. **Spine text touching the edges of the spine lane.** Give the text
   block vertical padding inside the spine lane.

## Cheat sheet: quick spine widths

Assuming white paper, b&w interior (0.002252 in/page):

| Pages | Spine width (in) | Spine text? |
|---|---|---|
| 90    | 0.20 | No |
| 120   | 0.27 | Borderline; lean no |
| 180   | 0.41 | Yes, small type |
| 240   | 0.54 | Yes |
| 320   | 0.72 | Yes, comfortable |
| 448   | 1.01 | Yes, plenty of room |

Cream paper (0.0025): same page counts give 0.23 / 0.30 / 0.45 / 0.60 /
0.80 / 1.12 respectively — cream is always a touch thicker.

---

**Next:** Lesson 4 — Typography that doesn't fight you.
