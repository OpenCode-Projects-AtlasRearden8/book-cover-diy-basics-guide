# Lesson 6 — Tool Guides: Canva, GIMP, and an Affinity Trial

Three free routes, one goal: a cover exported at exact print
dimensions with bleed honored. Pick your lane and follow only that
section end to end. All steps were written against current versions
of the tools; menu names shift occasionally — the *order* of the work
never does.

## Lane A — Canva (free tier)

**Setup**

1. Create a free Canva account. Skip the Pro trial for cover work —
   everything here works on the free tier.
2. `Create a design` → `Custom size`. If you have the KDP calculator
   template handy (recommended for print), use the *pixel* size it
   gives you at 300 DPI. Otherwise compute: inches x 300.
3. (Optional but smart) `File` → `Settings` → ensure units are set to
   whichever you computed in.

**Design**

4. Drop guides: `File` → `View` → `Rulers and guides` (or drag from
   rulers). Add vertical guides at each panel edge (back/spine/front
   boundaries) and horizontal ones 0.125" in from each edge — that
   inner boundary is the trim line; nothing critical goes outside it.
5. Add your background so it fills the whole canvas, bleed included
   (images and color must reach every edge of the canvas).
6. Build the layout with text layers: title, author, and (if used)
   series and tagline, keeping Lesson 4's habits.
7. Canva's free "positions" panel helps you align/mirror elements
   exactly — use it rather than nudging.

**Export (spot-check these, screenshot of the dialog optional)**

8. `Share` → `Download` → **JPG**, quality 100 (for print use PDF
   Print instead: `Share`/`Download` → `PDF Print`, then check
   `Crop marks and bleed` OFF because KDP does not want printer crop
   marks — your bleed is already in the art). If Canva's built-in
   "Print PDF" bleed toggle confuses you, simply ensure your canvas
   already includes the 0.125" bleed, and export with bleed off.
9. Open the exported file and measure: in any photo-viewer zoom to
   100% and use the ruler/guides, or just trust the pixel math:
   width_in x 300, height_in x 300 must match exactly.

**Canva-specific gotchas**

- Canva rounds some fractional sizes. If your exact size refuses to
  be entered, compute the pixel size and enter **px** instead of
  inches.
- Two-page view: Canva shows only the flat canvas — it is your job
  (and Lesson 8's) to mentally verify front, back, and spine lanes
  are where they should be.
- Free-tier assets: check the little crown/watermark warnings before
  export; you want zero pro assets inside your cover.

## Lane B — GIMP (free, desktop)

**Setup**

1. Download from gimp.org (free forever). Install.
2. `File` → `New`. Set width/height in pixels to your calculated
   print size at 300 DPI. Advanced options → X/Y resolution = 300 dpi.
3. `View` → enable `Show Rulers`; drag vertical guides to the panel
   boundaries (back|spine|front) and 0.125" inward from top and
   bottom, plus your text safe margins (0.25"+ from all trim edges).

**Design**

4. Background: `Edit` → `Fill with FG Color` (set FG to your
   background color) or paste a photo and scale with `Layer` →
   `Scale Layer` (separate the pasted image: `Layer` → `To New Layer`
   — or right-click the floating paste and `To New Layer`).
5. Text: press `T`, click, type. Set the title font/size in Tool
   Options. For tracked-out caps, use the `Letter spacing` field.
6. Align: `Image` → `Align Visible Layers` or drag with the Move tool
   and watch guide-snap (enable `View` → `Snap to Guides`).

**Export**

7. `File` → `Export As` → name `cover.jpg` → **Export**.
8. In the JPG dialog, quality 90–100. (For the flattest color, many
   indie printers prefer you submit JPG; KDP accepts either.)
9. Before closing: `File` → `Save As` → save the `.xcf` working
   master. Always keep masters.

**GIMP-specific gotchas**

- New layers default to floating pastes; always `To New Layer` after
  pasting so you don't accidentally merge things.
- Text layers can be re-edited later, but only if kept unflattened.
  Export flattens a *copy*; feel free to close without saving when
  finished only if you hit Save first.
- For the spine: any text on a curved/3D surface is an illusion —
  design flat and straight; the printer takes care of 3D.

## Lane C — Affinity (free trial)

Affinity offers a free trial of its professional apps — the trial
clock runs from installation. Schedule: design one weekend day,
export the next.

**Setup**

1. Start the trial of Affinity (Publisher, Designer, or Photo — any
   one can compose the wrap; Photo is the natural fit for raster
   covers).
2. `File` → `New` → set physical size to your wrap dimensions in
   inches at 300 DPI, or pick a pixel preset and override with your
   computed pixels.

**Design**

3. Set up guides at panel edges and safe margins (drag from rulers,
   or precise: `View` → `Guides/`Manager for numeric placement).
4. Build layers: background, main image, text blocks, final book
   details. Affinity's alignment + snapping is rock solid.

**Export**

5. `File` → `Export` → **JPG**, quality at maximum. (Or PDF if the
   KDP wizard wants vectors, but raster cover at exact pixel size is
   fully accepted.) Immediately after export, open the file and
   verify dimensions = computed pixels.

**Trial-specific gotchas**

- Trial days tick on calendar days, so leave export-to-KDP as the
  closing weekend task.
- Affinity files are kept as working masters; export copies. Save
  `.afdesign`/`.afphoto` early, save often.

## The KDP cover calculator + template (works with all lanes)

For print, KDP provides a free calculator that, once you enter
binding + trim + pages + paper, spits out the *exact* wrap size and a
template PNG with safe zones marked. The flow:

1. Enter interior type (b&w / color), page count, trim, binding.
2. Download the PNG template it offers (right size, with guides).
3. In any lane above, place that PNG as the bottom layer at 100% and
   design on layers above it, keeping art in the "bleed" band and
   text inside the marked safe zones.
4. Delete/hide the template layer before exporting.

This is single best-kept beginner hack for cover work — you design
*inside* a guaranteed-correct frame instead of verifying your own
math later.

---

**Next:** Lesson 7 — Common amateur tells (and how to fix each).
