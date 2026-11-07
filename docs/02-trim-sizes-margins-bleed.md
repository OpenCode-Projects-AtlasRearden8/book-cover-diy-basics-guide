# Lesson 2 — Trim Sizes, Margins, and Bleed

This is the lesson that keeps KDP's automated checks from bouncing your
file. Once, carefully; then it becomes second nature.

## Vocabulary in plain English

- **Trim size**: the final size of the book — how big it is once
  trimmed. Common KDP paperbacks: 6" x 9", 5.5" x 8.5", 5" x 8",
  5.25" x 8", 6.14" x 9.21". For your first book, 6" x 9" is the
  friendly default.
- **Bleed**: an extra **0.125" (1/8 inch)** of artwork extending past
  the trim edge on every side, top and bottom included. Paper
  cutting machines are accurate-but-not-perfect; bleed gives them
  slack so you never see a white sliver at the edge.
- **Safe margin (the "text keep-out")**: a zone inside the trim line
  where *forever-needs-to-be-read* stuff — title, author name, spine
  text, barcodes — should stay. Keep it generous: **0.25"–0.5" in
  from the trim line** at minimum.
- **Full-wrap cover**: a wide rectangle holding back cover + spine +
  front cover as one flat image. Width = back + spine + front + bleed
  allowances; height = trim height + top bleed + bottom bleed.

## The one formula to care about (print)

For a paperback with bleed, full wrap:

```
wrap width  =  (trim width  x 2)  +  spine width  +  0.25"  (bleed both sides)
wrap height =   trim height  + 0.25"                  (bleed top + bottom)
```

The `0.25"` is two bleed allowances of 0.125" each. Example (6" x 9"
paperback, spine width 1.06" — spine math in Lesson 3):

```
wrap width  = 6 + 6 + 1.06 + 0.25 = 13.31"
wrap height = 9 + 0.25            = 9.25"
```

## Ebook covers: the easy case

KDP's recommended ebook size: **1600 x 2560 px (1:1.6 ratio),
minimum 72 dpi, JPG or TIFF**. Recommend making it bigger —
**2000 x 3125 px or larger** — so it also looks good in big-display
ads and print-on-demand mockup tools. RGB color. Plain sRGB. Done.

## Where things must live (print cover map)

Picture the flat wrap, left to right:

```
[ BLEED | BACK COVER | SPINE | FRONT COVER | BLEED ]
         (0.25" empty + safe zone inside it on every open edge)
```

Rules of thumb:

- **Nothing critical within 0.25" of any edge**, except the artwork
  which must run all the way through the bleed.
- **Spine text** only if the spine is wide enough. KDP's guidance:
  treat spine text as risky below ~100 pages; keep it off for 99 or
  fewer (see Lesson 3). Even on thick books, leave 0.0625" of margin
  above and below the spine letters, vertically centered.
- **Barcode zone**: the bottom-right of the back cover (KDP places the
  ISBN barcode, about 2" x 1.2"). Keep that area design-simple or
  empty: no critical art, no texture-fine detail under where the
  barcode white box lands.
- **Trim lines are invisible** in your flat file — draw them yourself
  as temporary guides so you never "fudge it."

## Three mistakes that bounce covers

1. **Bleed is not the same as border.** A 0.125" *frame* of a colored
   rectangle that stops exactly AT the trim line is not bleed. Bleed is
   extra artwork running PAST the trim, 0.125" deep, on all four sides.
2. **Text placed in the bleed zone.** If any letters live within the
   outermost 0.125" band they may be chewed off. People literally write
   author names in that band. Don't.
3. **Wrong dimensions.** If your wrap width is 13.31" and the file is
   13.375", something gets scaled, stretched, or cropped. Build the
   canvas to the exact right size from the start (calculators and
   templates in the tools lesson).

## The "0.25 both sides" cheat sheet

| Trim size | Without bleed | With 0.125" bleed (height) |
|---|---|---|
| 5" x 8" | 5 x 8 | 5.25 x 8.25 wrap (in x pages) |
| 5.25" x 8" | 5.25 x 8 | 5.5 x 8.25 |
| 5.5" x 8.5" | 5.5 x 8.5 | 5.75 x 8.75 |
| 6" x 9" | 6 x 9 | 6.25 x 9.25 |

(For wrap width in the final file you add the spine width — Lesson 3.)

## Checklist: before you leave this lesson

- [ ] I know my trim size and it is one KDP supports.
- [ ] I know my page count and paper type (needed for spine width).
- [ ] My design has 0.125" of bleed on all four sides.
- [ ] All text, logo-type, and spine words sit inside a 0.375" safety
      margin from the trim line (belt-and-suspenders; 0.25" is the
      bare minimum).
- [ ] The bottom-right back cover zone is barcode-friendly.

---

**Next:** Lesson 3 — Spine math for print.
