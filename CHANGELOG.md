# Changelog

All notable changes to *The WKB Geometry of Newton Polygons* dataset and
manuscript are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and the project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0] — 2026-05-26

> **Camera-ready public release**: full manuscript + Round-2 refereed
> revisions + 39-class refinement.

### Added
* **Final camera-ready manuscript** `paper/manuscript.tex` (99,309 bytes,
  26 pages PDF).
* **Real TikZ taxonomy figure** (`figures/taxonomy_tikz.tex`) replacing
  the v1.0 placeholder; depicts the 23 → 39 class refinement.
* **Eight in-manuscript theorem proofs** (M1, N1, D2, S1, AT1, AT3, AT5,
  AT7) — previously distributed as `reports/proofs.md`, now integrated.
* **Notation table** (§2) covering all symbols ($L$, $N(L)$, $\chi$,
  $\chi_w$, $\mathcal{C}(L)$, $\mu_q$, $\Delta_{ij}$, $F$, $\mathfrak{r}$,
  …).
* **Computational and AI disclosure** (§11) consistent with prior Zenodo
  uploads.
* **`@book{lang-algebra}`** bibliography entry for the Kummer-theory
  citation in the new Theorem 5.1 proof.
* **arXiv and journal submission bundles** with byte-identical
  `paper.tex`.
* **`publication_pipeline/`** directory with repo-creation scripts,
  Zenodo v2.0 metadata, and DOI propagation tooling.

### Changed
* **Abstract trimmed** from 234 to 186 non-math words; novelty claims
  recalibrated to foreground the $\chi_w$ factorisation, the 23 → 39
  stratified atlas, $\mu_q$ / $\mu_{q'}$ bookkeeping, and the
  $p$-visibility result.
* **Introduction** rewritten to clarify the constellation-map status of
  $F$ (real category + morphisms + functoriality theorem in §3), to
  identify $\chi_w$ with the classical edge-indicial polynomial, and to
  delineate proved vs. classical content in the analytic lifting layer.
* **Theorem 5.1 (Kummer dichotomy)** restated to separate the proved
  algebraic content from empirical bounded-search corroboration.
  Step 2 of the proof was corrected (Round 2): the dimensionally
  confused `$-u \cdot q'$` phrasing was replaced with a clean
  $u = a/b$ lowest-terms derivation yielding the integer relation
  $b \, z_\beta - a \, z_\alpha = 0$.
* **Lemma `chi-multiplicative`** widened (Round 2) to cover the case
  of a single-slope summand adjoined to a multi-slope operator,
  provided all slopes are pairwise distinct; the iterated form is
  exactly what Theorem 4.1's induction needs.
* **Anti-Stokes Theorem 7.1, Step 4** now cross-references the
  sharpened (OS3) hypothesis in §7.1 (`\Cref{ssec:OS}`).
* **All dataset-internal identifiers** (`STRESS_*`, `MULTI_*`,
  `NEST_*`, `CTRL_*`, `OMEGA_*`, `GAL_*`) and JSON / PY filename
  mentions removed from manuscript prose.

### Fixed
* All undefined references and citations (0 in v2.0; the missing
  `lang-algebra` entry was added).
* Figure 1 placeholder replaced with the real TikZ source.
* Three-pass compile (pdflatex → bibtex → pdflatex × 2) reports
  **0 errors, 0 undefined refs, 0 LaTeX warnings**.

### Removed
* Overclaims about new "wild character variety" theorems.
* The strong reading of $F$ as a categorical functor without a
  category definition (replaced with a precise functoriality
  theorem on the explicit category $\mathcal{O}\mathrm{p}_1$).

### Bundle parity
* `paper/`, `arxiv_bundle/`, and `journal_bundle/` ship byte-identical
  `paper.tex` files (99,309 bytes).
* All three bundles compile to 26-page PDFs of ~897 KB.

---

## [1.0] — 2026-05-26 *(superseded)*

> Initial Zenodo dataset release.

### Added
* Computational atlas: 96 operators (48 single-edge + 48
  multi-edge / systems / nested / controlled).
* Newton polygons, characteristic polynomials $\chi(c)$, inner
  polynomials $\chi_w(w)$, and exponent constellations.
* Phase I–V JSON artifacts.
* Phase reports (Phase II, III, IV) in `reports/`.
* `proofs.md` with eight theorem–proof skeletons (M1, N1, D2, S1,
  AT1, AT3, AT5, AT7).
* `integration_map.md` placing each theorem in the draft.
* Draft paper text (`paper_draft.md`).
* Constellation zoo figure (`figures/constellations.png`).
* Zenodo metadata block, citation block, release notes.

### Known limitations (v1.0)
* Stokes constants not yet computed (only directions and Galois
  groupoids).
* Wild character variety functor only stated, not proved.
* Taxonomy figure was a $\fbox$ placeholder.

### DOI
`10.5281/zenodo.20355904`

---

## Future versions

### [3.0] *(planned)* — extended analytic layer
* Numerical Stokes constants for a representative subset of the atlas.
* Explicit ring decomposition of wild character varieties for selected
  multi-edge cases.
* Extension to operators with more than one irregular singularity
  (atlas over $\mathbb{P}^1$ rather than a single puncture).
