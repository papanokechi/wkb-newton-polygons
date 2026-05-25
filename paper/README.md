# `paper/` — Final camera-ready manuscript

This directory contains the **camera-ready LaTeX manuscript** for
*The WKB Geometry of Newton Polygons: A Functorial Classification Theory*
(version 2.0).

## Contents

| File              | Description                                       |
|-------------------|---------------------------------------------------|
| `manuscript.tex`  | Master LaTeX source (99,309 bytes)                |
| `manuscript.pdf`  | Compiled PDF — **26 pp, 897,105 bytes**           |
| `references.bib`  | Bibliography (BibTeX format, 24 entries)          |
| `paper.bbl`       | Pre-built bibliography (no `bibtex` needed)       |
| `figures/`        | `constellations.png`, `taxonomy_tikz.tex`         |

## Compile

```bash
pdflatex -interaction=nonstopmode manuscript.tex
bibtex   manuscript
pdflatex -interaction=nonstopmode manuscript.tex
pdflatex -interaction=nonstopmode manuscript.tex
```

Final compile state: **0 errors, 0 undefined refs, 0 LaTeX warnings**.

(Two cosmetic BibTeX warnings on `mochizuki-asymptotic` and
`ramis-q-stokes` are pre-existing volume-vs-number style notes and do
not affect the rendered bibliography.)

## Engine

* MiKTeX 25.12 / pdfTeX 4.23
* BibTeX 0.99e
* Font set: Computer Modern (lm) + AMS (msam, msbm)
* TikZ libraries: `positioning, fit, arrows.meta`

## Notation

A complete notation table appears in §2 of `manuscript.tex`
(`\Cref{tab:notation}`). The principal symbols are:

| Symbol          | Meaning                                              |
|-----------------|------------------------------------------------------|
| $L$             | scalar linear operator, one irregular singularity at $\infty$ |
| $N(L)$          | Newton polygon of $L$                                |
| $\chi_L(c)$     | WKB characteristic polynomial of $L$                 |
| $\chi_w(w)$     | inner polynomial: $\chi(c) = \chi_w(c^q)$ on each slope block |
| $\mathcal{C}(L)$| WKB exponent constellation, $= \text{Roots}(\chi_L)$ |
| $\mu_q$         | group of $q$-th roots of unity (acts on each slope-graded block) |
| $\Delta_{ij}$   | analytic difference $c_i - c_j$ on the $t$-cover    |
| $F$             | the constellation map / functor $L \mapsto \mathcal{C}(L)$ |

## Sections

1. Introduction (constellation map, prior art, summary of contributions)
2. Preliminaries and notation table
3. The constellation map $F$ on $\mathcal{O}\mathrm{p}_1$
4. **Per-edge factorisation** — Theorem 4.1 (M1) + Lemma `chi-multiplicative`
5. **Kummer dichotomy** — Theorem 5.1 (D2)
6. Pullback systems and the determinant polygon — Theorem 6.1 (S1)
7. **Analytic lifting** — Theorems 7.1–7.4 (AT1, AT3, AT5, AT7)
8. The atlas: 23 single-edge classes refining to 39 classes
9. Counterexamples and degeneracy boundaries
10. Related work
11. Computational and AI disclosure
12. Acknowledgements
   * References

## Revision history

See `../CHANGELOG.md` for the complete revision history. The version in
this directory incorporates **both rounds** of refereed revisions
(see `../major_revision/` for the patch sets and response letters).
