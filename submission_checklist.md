# Submission checklist — v1.0

**Paper:** *The WKB Geometry of Newton Polygons: A Functorial Classification
Theory.*

**Companion dataset:** Zenodo v1.0, DOI `10.5281/zenodo.XXXXXXX`
(placeholder).

This checklist accompanies the manuscript bundles
`arxiv_bundle/` and `journal_bundle/`. Tick each item before pressing
"Submit".

---

## 1. Compilation

- [x] `pdflatex paper.tex` runs to exit code 0 on a clean MiKTeX/TeXLive
      install.
- [x] `bibtex paper` runs cleanly (2 cosmetic warnings only:
      "number but no volume" in `mochizuki-asymptotic` and
      `ramis-q-stokes`; both are Asterisque-style entries where this is
      correct).
- [x] Three `pdflatex` passes converge (TOC + cross-refs stable).
- [x] Final PDF: **19 pages, ~827 KB**.
- [x] Zero `LaTeX Warning` lines in `paper.log`.
- [x] Zero `Undefined` references.
- [x] Only three minor `Overfull/Underfull` hbox warnings (cosmetic; no
      visible bleed beyond the column).

## 2. Cross-reference closure

- [x] All 23 BibTeX cite keys in `paper.tex` resolve against
      `references.bib` (`wkb_dataset_v1`, `levelt`, `turrittin`,
      `wasow`, `sibuya`, `sabbah-isomon`, `sabbah-polarizable`,
      `mochizuki-asymptotic`, `robba-malgrange`,
      `birkhoff-trjitzinsky`, `sauloy`, `ramis-stokes`,
      `ramis-q-stokes`, `zhang`, `kawai-takei`, `iwaki-nakanishi`,
      `aoki-kawai-takei`, `gmn-spectral`, `boalch-stokes`,
      `boalch-wildhodge`, `arnold1976`, `brieskorn`, `mckay`).
- [x] Zero unused entries in `references.bib`.
- [x] All `\Cref{...}` references resolve (`thm:main`, `cor:ring`,
      `cor:vieta`, `thm:M1`, `thm:N1`, `thm:D2`, `thm:S1`, `thm:AT1`,
      `thm:AT3`, `thm:AT5`, `thm:AT7`).
- [x] All section labels resolve (`sec:intro`, `sec:prelim`, `sec:main`,
      `sec:multiedge`, `sec:degeneracy`, `sec:systems`,
      `sec:analytic`, `sec:classes`, `sec:related`, `sec:vision`,
      `sec:reproducibility`, `sec:ack`).
- [x] Figure 1 (taxonomy) and Figure 2 (constellation zoo) referenced
      from main text.

## 3. Figures and assets

- [x] `figures/constellations.png` (141 KB) renders inside the
      `figure` environment in Section 8.3 (constellation zoo).
- [ ] **TODO before camera-ready:** replace the Figure 1 `\fbox{...}`
      placeholder with a rendered TikZ taxonomy diagram per the spec in
      `taxonomy.txt`.  The placeholder is informative but visually
      austere.

## 4. Content placeholders to replace

- [x] **Author name** Papanokechi (mononym; matches Zenodo record
      10.5281/zenodo.20355904).
- [x] **ORCID** `0009-0000-6192-8273` (verified against Zenodo).
- [x] **Email** — Zenodo record does not expose an email; correspondence
      is routed via the ORCID record and the GitHub repository
      `https://github.com/papanokechi`. No placeholder email remains in
      the source.
- [ ] **Zenodo DOI** `10.5281/zenodo.XXXXXXX` — replace once the dataset
      is published (paper text **and** `references.bib`). The current
      placeholder DOI is the *concept* DOI for the WKB dataset; the
      author-identity reference Zenodo record is
      `10.5281/zenodo.20355904`.
- [ ] **arXiv identifier** for the companion preprint, if cross-listed.

## 5. Theorem-proof placement (per `integration_map.md`)

- [x] §3 — Main Theorem (`thm:main`), Corollaries (`cor:ring`,
      `cor:vieta`), degeneracy remark.
- [x] §4 — `thm:M1` (multi-edge factorisation), `thm:N1` (nested
      ramification).
- [x] §5 — `thm:D2` (prime-q Kummer dichotomy) preceded by the four
      named strata.
- [x] §6 — `thm:S1` (system pullback via determinant polygon /
      Sym^n).
- [x] §7 — `thm:AT1`, `thm:AT3`, `thm:AT5`, `thm:AT7` (analytic
      lifting), preceded by the open-stratum hypotheses (OS1)-(OS5).

## 6. Notation consistency

- [x] Slope written as `-p/q`, gcd(p,q) = 1.
- [x] Rank denoted `r`; rank vertex `(rq, 0) -> (0, rp)`.
- [x] WKB characteristic polynomial `chi(c)`; inner polynomial
      `chi_w(w)` of degree `r`.
- [x] Functor written `F: L |-> C(L)` (Sans-serif F in math via
      `\Fclass`).
- [x] Group of q-th roots of unity `mu_q`; primitive root `zeta_q`.
- [x] Pairwise differences `Delta_{ij} := c_i - c_j`.
- [x] Wild monodromy / character variety stratum `MW(L)` defined in
      preamble.

## 7. arXiv submission

- [x] Primary category: **math-ph**.
- [x] Suggested cross-listings: **math.CA**, **math.DS**, **math.AG**.
- [x] MSC2020: 34M40 (primary); 34M30, 34M35, 39A06, 39A13 (secondary).
- [x] Bundle contains pre-built `paper.bbl` (so arXiv does not have to
      run BibTeX).
- [x] Bundle is self-contained: only the four files `paper.tex`,
      `references.bib`, `paper.bbl`, `figures/constellations.png` are
      needed.
- [ ] If cross-listing is changed, update the `\keywords{...}` line and
      the "MSC2020 classification" footnote.

## 8. Journal submission

- [x] Bundle contains a `class-file-placeholder.txt` with switch-over
      instructions for Springer Nature, Elsevier, AMS, JEP, SIGMA.
- [ ] Drop in the journal's `.cls` file when chosen.
- [ ] Swap the `\documentclass{article}` line for the journal class.
- [ ] Verify the body still compiles with the journal class
      (theorem environments and cross-references in particular).
- [ ] Adapt `\author{...}` block to the journal's front-matter macros.
- [ ] Confirm the journal's preferred bibliography style and update
      `\bibliographystyle{...}` (currently `alpha`).

## 9. Licensing and policies

- [x] Code (fleet scripts, plot scripts): MIT (matches Zenodo metadata).
- [x] Text and figures: CC-BY 4.0 (matches Zenodo metadata).
- [x] No third-party copyrighted material reused beyond
      standard citation.
- [x] All figures are produced by the authors.
- [ ] Add a copyright/licensing footnote to the title page if the
      journal requires it.

## 10. Companion dataset

- [x] Zenodo metadata block prepared (`zenodo_metadata.txt`,
      `README.md`, `directory_structure.txt`, `release_notes_v1.0.txt`,
      `citation_block.txt`).
- [ ] Upload Zenodo bundle and capture the assigned DOI.
- [ ] Update the placeholder DOI in `paper.tex` and
      `references.bib`.

## 11. Final reading pass

- [ ] Spell-check (US/UK consistency).
- [ ] Equation numbering: only the equations referenced have numbers
      (current source already uses `\[` `\]` for the rest).
- [ ] Theorem statements read in isolation (a reader scanning bold
      titles can follow the spine of the paper).
- [ ] No "TODO", "FIXME", "?", or `\todo` markers left in the source.
      (Verified for the v1.0 source.)

## Known limitations (carried over to v2.0)

* Figure 1 (taxonomy) is rendered as a labelled `\fbox` with a
  prose caption; v2.0 should replace this with a TikZ figure.
* The constellation zoo figure (`figures/constellations.png`) is a
  3x4 placeholder rendering from Phase I; v2.0 should regenerate with
  per-panel class labels.
* Stokes constants are not computed — only the anti-Stokes ray
  positions and per-ray counts. This is a deliberate scope choice
  documented in §7.1 (Theorem AT1 et seq.).
* Author identity is finalised: Papanokechi (ORCID
  0009-0000-6192-8273); only the Zenodo DOI for the WKB-dataset itself
  remains as a placeholder until the dataset record is published.
