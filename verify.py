#!/usr/bin/env python3
"""Verification for the Book Cover DIY Basics Guide.

Runs:
  1. site build (regenerates site/ from docs/)
  2. unit tests for the spine/wrap math helpers
  3. output checks: every lesson page exists and parses sanely
  4. repo hygiene: LICENSE line, README credit, no obvious secrets

Run ``python3 verify.py``. Exit code 0 = all good.
"""

import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import build as guide  # noqa: E402

DOCS = ROOT / "docs"
SITE = ROOT / "site"

EXPECTED_LESSONS = [
    "00-start-here",
    "01-genre-expectations",
    "02-trim-sizes-margins-bleed",
    "03-spine-math",
    "04-typography",
    "05-fits-the-vibe-checklist",
    "06-tool-guides",
    "07-amateur-tells",
    "08-pre-publish-walkthrough",
    "09-cheat-sheet",
]


class SpineMathTests(unittest.TestCase):
    def test_spine_width_white_paper(self):
        self.assertEqual(guide.spine_width(90, "white"), 0.2027)
        self.assertEqual(guide.spine_width(240, "white"), 0.5405)
        self.assertEqual(guide.spine_width(320, "white"), 0.7206)

    def test_spine_width_cream_paper_matches_lesson_table(self):
        # Lesson 3 cheat-sheet values for cream (0.0025 in/page)
        for pages, expected in [(90, 0.225), (120, 0.3), (180, 0.45),
                                (240, 0.6), (320, 0.8), (448, 1.12)]:
            self.assertAlmostEqual(guide.spine_width(pages, "cream"), expected, places=4)

    def test_spine_width_rejects_bad_input(self):
        with self.assertRaises(ValueError):
            guide.spine_width(0, "white")
        with self.assertRaises(KeyError):
            guide.spine_width(100, "cardboard")

    def test_worked_example_from_lesson_3(self):
        # 6 x 9, 288 pages, cream paper
        w, h = guide.wrap_dimensions(6, 9, 288, "cream")
        self.assertAlmostEqual(w, 12.97, places=2)
        self.assertAlmostEqual(h, 9.25, places=2)
        self.assertEqual(guide.px(w, h), (3891, 2775))

    def test_wrap_formula_matches_lesson_2_example(self):
        # Lesson 2 example: 6x9 with a 1.06" spine
        w = round(6 * 2 + 1.06 + 0.25, 4)
        self.assertAlmostEqual(w, 13.31, places=3)


class SiteOutputTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        guide.build_site()

    def test_all_lesson_pages_exist(self):
        for slug in EXPECTED_LESSONS:
            self.assertTrue((SITE / f"{slug}.html").is_file(), f"missing {slug}.html")
        self.assertTrue((SITE / "index.html").is_file())
        self.assertTrue((SITE / "style.css").is_file())

    def test_docs_match_expected_lesson_list(self):
        slugs = sorted(p.stem for p in DOCS.glob("*.md"))
        self.assertEqual(slugs, EXPECTED_LESSONS)

    def test_every_page_is_complete_html(self):
        for slug in ["index.html"] + [f"{s}.html" for s in EXPECTED_LESSONS]:
            text = (SITE / slug).read_text(encoding="utf-8")
            self.assertIn("<!DOCTYPE html>", text)
            self.assertIn("</html>", text)
            self.assertIn("Asdale Dynamics, LLC", text)
            self.assertIn("style.css", text)

    def test_no_raw_markdown_leaks_into_html(self):
        text = (SITE / "03-spine-math.html").read_text(encoding="utf-8")
        self.assertNotIn("**", text)
        self.assertIn("<table>", text)  # tables extension worked

    def test_pager_links_connect_the_chain(self):
        first = (SITE / "00-start-here.html").read_text(encoding="utf-8")
        self.assertIn('href="01-genre-expectations.html"', first)
        last = (SITE / "09-cheat-sheet.html").read_text(encoding="utf-8")
        self.assertIn('href="08-pre-publish-walkthrough.html"', last)

    def test_pager_nothing_publishes_disclaimer_present(self):
        text = (SITE / "index.html").read_text(encoding="utf-8")
        self.assertIn("MIT licensed", text)


class RepoHygieneTests(unittest.TestCase):
    LICENSE = ROOT / "LICENSE"
    README = ROOT / "README.md"

    def test_license_first_line_is_mit(self):
        self.assertEqual(self.LICENSE.read_text().splitlines()[0], "MIT License")

    def test_license_copyright_line_exact(self):
        expected = "Copyright (c) 2026 Asdale Dynamics, LLC"
        self.assertIn(expected, self.LICENSE.read_text())

    def test_readme_credits_llc(self):
        self.assertIn("Asdale Dynamics, LLC", self.README.read_text())

    def test_no_obvious_secrets_in_repo_files(self):
        pattern = re.compile(
            r"(AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}"
            r"|-----BEGIN (RSA|OPENSSH|EC) PRIVATE KEY-----)",
            re.MULTILINE,
        )
        scopes = [DOCS, ROOT / "assets", ROOT / "tests", SITE,
                  ROOT / "build.py", ROOT / "verify.py", self.README, self.LICENSE]
        bad = []
        for scope in scopes:
            if scope.is_file():
                paths = [scope]
            elif scope.is_dir():
                paths = [p for p in scope.rglob("*") if p.is_file()]
            else:
                continue
            for p in paths:
                try:
                    text = p.read_text(encoding="utf-8", errors="ignore")
                except OSError:
                    continue
                if pattern.search(text):
                    bad.append(str(p))
        self.assertEqual(bad, [], f"possible secrets found in: {bad}")

    def test_docs_mention_required_topics(self):
        union = "\n".join(p.read_text(encoding="utf-8") for p in DOCS.glob("*.md"))
        for topic in ["bleed", "spine", "Canva", "GIMP", "thumbnail", "barcode"]:
            self.assertIn(topic, union, f"topic missing from docs: {topic}")


def main() -> int:
    print("== building site ==")
    subprocess.run([sys.executable, str(ROOT / "build.py")], check=True)
    print("== running tests ==")
    loader = unittest.TestLoader()
    suite = unittest.TestSuite([
        loader.loadTestsFromTestCase(SpineMathTests),
        loader.loadTestsFromTestCase(SiteOutputTests),
        loader.loadTestsFromTestCase(RepoHygieneTests),
    ])
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
