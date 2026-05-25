# `arxiv_bundle/` — arXiv submission bundle

This directory is a **self-contained submission package** ready for
[arXiv.org](https://arxiv.org/), category `math-ph` (cross-listed to
`math.CA`, `math.DS`, `cs.MS`).

## Contents

| File              | Description                                       |
|-------------------|---------------------------------------------------|
| `paper.tex`       | Master source (byte-identical to `paper/manuscript.tex`) |
| `paper.bbl`       | Pre-built bibliography (arXiv requires this)      |
| `references.bib`  | Source bibliography (for completeness)            |
| `paper.pdf`       | Compiled PDF (26 pp, 897,107 bytes)               |
| `figures/`        | `constellations.png`, `taxonomy_tikz.tex`         |
| `README.md`       | This file                                         |

## arXiv submission instructions

1. **Verify compile**: run `pdflatex → pdflatex → pdflatex` on this
   directory. (No `bibtex` step is needed — `paper.bbl` is included.)

2. **Create the upload bundle**:
   ```bash
   cd ..
   tar -czf wkb-newton-polygons-arxiv.tar.gz arxiv_bundle/
   ```

3. **Upload** to <https://arxiv.org/submit>:
   * primary category: `math-ph`
   * cross-listings: `math.CA`, `math.DS`, `cs.MS`
   * license: arXiv non-exclusive license to distribute

4. **MSC 2020 codes**:
   * Primary: 34E20 (Singular perturbations, turning point theory, WKB methods)
   * Secondary: 34M30 (Asymptotic, formal expansions in differential equations in the complex domain), 39A06 (Linear difference equations), 39A13 ($q$-difference equations)

## Engine compatibility

The source compiles cleanly under:

* arXiv's pdflatex (TeX Live 2024)
* MiKTeX 25.12 (used to produce this bundle)
* Overleaf (TeX Live 2024)

No exotic packages are used. The full preamble dependency list:

```
amsmath, amssymb, amsthm, amsfonts
mathtools
graphicx
hyperref
cleveref
tikz (with libraries positioning, fit, arrows.meta)
booktabs
xcolor
geometry
fancyhdr
```

## Differences from `journal_bundle/`

The `arxiv_bundle/` differs from `journal_bundle/` in only one way: the
journal bundle uses a placeholder class file (`class-file-placeholder.tex`)
which the journal will replace at typesetting; the arXiv bundle uses
plain `article` class.

The body, theorems, figures, and bibliography are **identical**.
