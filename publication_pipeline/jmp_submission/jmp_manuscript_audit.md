# JMP Manuscript Audit — Compliance Check

**Date:** 2026-05-26
**Target journal:** Journal of Mathematical Physics (AIP Publishing)
**Manuscript:** `paper_v2_1.tex` (= `paper/manuscript.tex` = `paper/paper.tex`
= `arxiv_bundle/paper.tex` = `journal_bundle/paper.tex`, byte-identical)
**Version after this audit:** post §AI Disclosure rewrite, post DOI bake-in
in §AI Disclosure Reproducibility paragraph.

---

## 1 — Field-by-field audit

| # | Item | Status | Detail |
|---|------|--------|--------|
| 1 | Title | ✅ PASS | `\title{The WKB Geometry of Newton Polygons: A Functorial Classification Theory}` (paper.tex L82–83). |
| 2 | Author block | ⚠ MINOR | `\author{Papanokechi\thanks{Independent researcher. ORCID: 0009-0000-6192-8273. \url{https://github.com/papanokechi}.}}` (L85–90). |
| 2a |  – Author name | ✅ PASS | Single author "Papanokechi". |
| 2b |  – ORCID | ✅ PASS | 0009-0000-6192-8273 present, valid checksum. |
| 2c |  – Affiliation | ⚠ MINOR | "Independent researcher" with no postal address. AIP accepts this but listing a city/country (e.g., "Independent researcher, Yokohama, Japan") improves portal completeness. |
| 2d |  – **Author email** | 🔴 **BLOCKER** | **No email anywhere in the manuscript.** AIP Editorial Manager requires a corresponding-author email. Author must add one before submission (web-form field, not strictly required in TeX source). |
| 3 | Date | ⚠ MINOR | `\date{(preprint v1.0)}` (L92). Recommend changing to `\today` or `\date{}` for journal submission; "preprint" label can be misread. |
| 4 | Abstract | ✅ PASS | Lines 101–134. **195 non-math words** (counted in revised abstract artifact). JMP accepts up to 250 words → comfortably under the cap. Self-contained, no `\cite` calls inside abstract. |
| 5 | Keywords | ✅ PASS | `\keywords{...}` at L137–140 — 19 keywords matching Zenodo deposit metadata. |
| 6 | MSC2020 | ✅ PASS | `\subjclass[2020]{34M30, 34M40, 34M03, 12H05, 14M99}` at L143. Five codes — primary classifications include irregular singularities (34M30), Stokes phenomenon (34M40), formal/exact methods (34M03), differential algebra (12H05), and applications/other (14M99). |
| 7 | Acknowledgements | ⚠ MINOR | Present but contains stale forward-reference: "will be added in the camera-ready version (v2.0)" (paper.tex L2061–2062). v2.0 release is complete and Zenodo DOI is live → either remove the placeholder language or update to acknowledge the published artifact (Zenodo `10.5281/zenodo.20387847`). |
| 8 | AI / Computational disclosure | ✅ PASS (post-rewrite) | **§*Computational and AI Disclosure** (sec:disclosure, L1951). After Task-2 rewrite this turn: 4 sub-roles (Drafting, Code generation, Exploratory pattern-finding, Organisational support). "Proof-skeleton generation" and "Conjecture selection" roles removed. AI-not-used-for-mathematical-content statement explicit in role (iii). Compliant with AIP/COPE policy (no AI authorship, no AI-generated science). |
| 9 | Reproducibility statement (inside §AI Disclosure) | ✅ PASS (post-rewrite) | DOI baked in: `10.5281/zenodo.20387847` (version DOI) + `10.5281/zenodo.20387846` (concept DOI). GitHub URL `https://github.com/papanokechi/wkb-newton-polygons` present. CC-BY-4.0/MIT dual licence stated. Stale "Zenodo v2.0 dataset" language removed. |
| 10 | §11 Reproducibility note (sec:reproducibility, L1914) | ⚠ MINOR | This is the *separate* numbered §11 (not the §AI Disclosure block). Still contains DOI placeholder at L1945: `\texttt{10.5281/zenodo.XXXXXXX}) will be assigned by Zenodo on publication`. Recommend rewrite to current DOI before submission (one-line edit; see metadata_consistency_report.md). |
| 11 | Header DOI placeholder | ⚠ MINOR | Line 5: `%% Companion dataset: doi:10.5281/zenodo.XXXXXXX  (PLACEHOLDER)`. Cosmetic comment, no effect on compiled PDF, but should be updated for consistency. |
| 12 | References compile | ✅ PASS | 4-pass build (pdflatex→bibtex→pdflatex×3) completes with 0 undefined citations, 0 undefined references, 2 cosmetic BibTeX warnings (pre-existing, unrelated to JMP submission). |
| 13 | Bibliography DOI placeholder | ⚠ MINOR | `references.bib` L17–18 (in all 3 copies — paper/, arxiv_bundle/, journal_bundle/) and the bbl file have `10.5281/zenodo.XXXXXXX` in the `wkb_dataset_v1` entry. Should be propagated to current DOI before submission. |
| 14 | Figures | ✅ PASS | Single figure `figures/constellations.png` referenced via `\includegraphics`. Renders at 26-page final compile. PNG is included in the journal_bundle/figures/ directory. |
| 15 | DOI in metadata | ✅ PASS (in §AI Disclosure post-rewrite) / ⚠ MINOR (elsewhere) | DOI now live in §AI Disclosure but still placeholder in §11 + header + bib (see #10, #11, #13). |
| 16 | GitHub URL in disclosure | ✅ PASS | L2044 of paper.tex: `\url{https://github.com/papanokechi/wkb-newton-polygons}` (full repo URL). |
| 17 | GitHub URL in author block | ⚠ MINOR | L89 has `\url{https://github.com/papanokechi}` (account URL, not repo URL). Recommend extending to `https://github.com/papanokechi/wkb-newton-polygons` for consistency, or removing the URL from the author thanks footnote entirely. |
| 18 | Dataset identifiers in prose | ✅ PASS | No bare dataset filenames or internal artifact paths in the running prose. References to data are via `\cite{wkb_dataset_v1}` (Zenodo DOI citation key) or via the §AI Disclosure paragraph. |
| 19 | Internal filenames | ✅ PASS | Only `proofs.md`, `integration_map.md`, `counterexamples.json`, `constellations.png`, `fleet.py`/`fleet3-5.py` mentioned — all are public artifacts in the Zenodo deposit / GitHub repo. No internal session paths, no temp files, no machine-specific paths. |
| 20 | No arXiv ID in metadata | ℹ INFO | Manuscript has no `arXiv:XXXX.XXXXX` placeholder in the body (good — there is no preprint yet, JMP submission is direct). If the author later cross-posts to arXiv after JMP acceptance, the arXiv ID can be added at that time. |
| 21 | Shell escapes / \write18 | ✅ PASS | No `\write18`, no `\immediate\write18`, no `--shell-escape` build dependency. Pure LaTeX + BibTeX build. |
| 22 | External dependencies | ✅ PASS | All packages in the preamble are standard TeX Live/MiKTeX (amsmath, amsthm, hyperref, cleveref, enumitem, etc.). No locally-developed `.sty` files. |

---

## 2 — Summary of issues by severity

### 🔴 BLOCKERS (must fix before submission)

1. **Author email missing.** Add corresponding-author email when filling
   the JMP Editorial Manager submission form. (Email does not need to be
   in the TeX source; AIP collects it via the portal.) Suggested:
   `ppapanokechi@gmail.com` if no institutional email exists.

### ⚠ MINOR POLISH (recommended before submission, not blocking)

2. Add postal location to `\thanks{...}` author footnote
   (e.g., "Independent researcher, Yokohama, Japan").
3. Change `\date{(preprint v1.0)}` → `\date{\today}` or `\date{}`.
4. Remove "will be added in the camera-ready version (v2.0)" language
   from Acknowledgements (paper.tex L2061–2062).
5. Replace remaining DOI placeholders **outside** §AI Disclosure with the
   live DOI `10.5281/zenodo.20387847`:
   - Header comment (L5 of all 5 manuscript copies).
   - §11 Reproducibility note (L1944–1945).
   - `references.bib` `wkb_dataset_v1` entry (L17–18) in all 3 bundle
     copies.
   - `paper.bbl` bibliography output.
   - `README.md` badge (L5) and BibTeX block (L109–110).
   - `CITATION.cff` (5 placeholder sites: L11, L13, L47, L48, L52).
6. Extend the author-footnote GitHub URL from
   `https://github.com/papanokechi` to
   `https://github.com/papanokechi/wkb-newton-polygons` (or remove).

### ℹ INFORMATIONAL

7. No arXiv preprint yet — that is consistent with the JMP submission
   plan (JMP does not require arXiv; SIGMA does). The
   `arXiv:XXXX.XXXXX` placeholder in `CITATION.cff` L49 reflects an
   *intended* future cross-post and is not a blocker for JMP.

---

## 3 — Compile-time evidence

- **Pre-task baseline (Phase 10):** 26 pages, 898,187-byte PDF,
  0 errors, 0 undefined refs/cites, 0 LaTeX warnings, 2 cosmetic
  BibTeX warnings.
- **Post-task verification (this turn):** 26 pages, **886,457-byte
  PDF**, **0 errors, 0 LaTeX warnings, 0 undefined refs/cites**,
  2 cosmetic BibTeX warnings (unchanged). Verified for
  `journal_bundle/`, `paper/`, and `arxiv_bundle/` — all three bundles
  produce byte-identical PDFs.
- **Note on size change:** The new disclosure paragraph is shorter
  than the 5-role version that it replaces, accounting for the
  ~12 KB PDF size reduction. Page count is unchanged at 26.
- **Side-fix this turn:** `\usepackage{tikz}` +
  `\usetikzlibrary{positioning, fit, arrows.meta}` added to all 5
  manuscript preambles. The `taxonomy_tikz.tex` figure (L1740)
  required these packages but they were missing from the preambles
  — pre-existing bug, predates Task 2.

---

## 4 — Verdict

**Manuscript compliance with JMP submission policy: PASS WITH MINOR POLISH.**

- The §AI Disclosure rewrite (Task 2) lifts the manuscript from
  *AI-policy-fragile* to *AIP/COPE compliant*.
- All structural JMP requirements (title, author, abstract ≤ 250 words,
  MSC codes, keywords, figures, references, AI disclosure) are met.
- The one true blocker is the missing corresponding-author email, which
  is supplied at portal-form time (not via TeX edit).
- The MINOR-POLISH items (≈ 15 minutes of edits + recompile) are
  recommended for a clean submission but do not gate it.

See `metadata_consistency_report.md` for cross-file placeholder inventory
and `jmp_submission_readiness.md` for the final overall verdict.
