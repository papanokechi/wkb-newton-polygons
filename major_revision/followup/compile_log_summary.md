# Compile log summary (Round-2 follow-up)

## Compile pipeline

```
pdflatex -interaction=nonstopmode -file-line-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -file-line-error paper.tex
pdflatex -interaction=nonstopmode -file-line-error paper.tex
```

(Three-pass pdflatex with one bibtex run between passes 1 and 2, as
required for cross-references and the bibliography to converge.)

## Final compile metrics (`paper/paper.tex`)

| Metric                   | Value             |
|---------------------------|-------------------|
| LaTeX errors              | **0**             |
| Undefined references      | **0**             |
| Undefined citations       | **0**             |
| LaTeX warnings (other)    | **0**             |
| BibTeX warnings (cosmetic)| 2                 |
| Pages                     | **26**            |
| PDF size                  | **897,105 bytes** |
| PDF location              | `paper/paper.pdf` |

The two cosmetic BibTeX warnings are pre-existing (volume-vs-number
fields in `mochizuki-asymptotic` and `ramis-q-stokes`); they are
unrelated to this revision and produce no visible artefacts in the
rendered bibliography.

## Bundle compile metrics

| Bundle               | Pages | PDF bytes  |
|----------------------|------:|-----------:|
| `paper/`             |    26 |   897,105  |
| `arxiv_bundle/`      |    26 |   897,107  |
| `journal_bundle/`    |    26 |   897,107  |

All three bundles compile from byte-identical `paper.tex` and inherit
the Round-2 follow-up changes. The 2-byte difference between the master
and bundle PDFs is the standard pdfTeX timestamp noise; content is
identical.

## Compile log highlights (`paper/paper.log`)

* `\Cref{...}`-resolved labels: 41 (all bound).
* External citations resolved: 24 (`@misc{wkb_dataset_v1}`,
  `@book{lang-algebra}`, the Levelt–Turrittin trio, Sabbah, Mochizuki,
  Robba–Malgrange, Birkhoff–Trjitzinsky, Sauloy, Ramis, Zhang, KT, IN,
  AKT, GMN, Boalch, Arnold, Brieskorn, McKay, …).
* All 24 `\cite{...}` keys resolve.
* TikZ libraries actually used: `positioning, fit, arrows.meta`
  (loaded by paper preamble; figure `figures/taxonomy_tikz.tex` compiles
  cleanly inline).

## Compile log triage

```
> grep "^!" paper.log                # LaTeX errors
(no matches)

> grep "undefined" paper.log         # undefined refs/citations
(no matches)

> grep "Warning" paper.log           # any warning of any kind
(no matches)
```

## What changed since the Round-1 baseline

In addition to the Round-2 followup paper.tex changes documented in
`major_revision_followup.diff`, the following bundle-level changes were
made for compile parity:

1. `paper/references.bib` (and bundle copies): one new `@book` entry
   added for `lang-algebra` (Kummer-theory citation used in the new
   Theorem 5.1 proof).
2. `paper/figures/taxonomy_tikz.tex` (and bundle copies): new file
   containing the real TikZ source for Figure 1, replacing the
   `\fbox` placeholder in the original camera-ready bundle.
3. `paper/figures/constellations.png`: unchanged.

## Notes on rendering quality

* The taxonomy figure renders cleanly at the intended size with no
  TikZ overruns.
* The new notation table (`\Cref{tab:notation}`) inserts cleanly into
  §2 and floats to its declared `[t]` position.
* The 39-class refinement footnote in the figure caption matches the
  body-text claim ("23 single-edge classes refining to 39").
* All in-text mathematical displays (especially the new Lemma proof,
  Theorem 5.1 Step 2 with the explicit $b z_\beta - a z_\alpha = 0$
  display, and the new Figure 1 input) render at the expected
  positions and do not provoke `Overfull \hbox` or `Underfull \hbox`
  warnings.

## Reproducibility

To re-run the compile from a clean checkout:

```powershell
cd paper
Remove-Item *.aux,*.log,*.out,*.toc,*.bbl,*.blg -ErrorAction SilentlyContinue
pdflatex -interaction=nonstopmode -file-line-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -file-line-error paper.tex
pdflatex -interaction=nonstopmode -file-line-error paper.tex
```

Engine used for this run:
* MiKTeX 25.12 / pdfTeX 4.23
* BibTeX 0.99e
* Default font set: Computer Modern (lm) + AMS Fonts (msam, msbm)
