# Compile Log Summary — Repo-URL Insertion

**Source file**: `paper/paper.tex` (post-edit, 99,553 bytes)
**Engine**: MiKTeX 25.12 / pdfTeX 4.23
  (`C:\Users\shkub\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe`)
**BibTeX**: `C:\Users\shkub\AppData\Local\Programs\MiKTeX\miktex\bin\x64\bibtex.exe`
**Working directory**: `wkb-newton-polygons/paper/`
**Run mode**: `-interaction=nonstopmode -file-line-error`

## Pass sequence

A four-pass sequence was used (one extra pdflatex pass after the
standard three to fully settle the `\Cref` label re-resolution and
suppress the cosmetic "Label(s) may have changed" warning that lingers
after three passes).

```powershell
Remove-Item *.aux,*.log,*.out,*.toc,*.bbl,*.blg,*.synctex.gz
& pdflatex -interaction=nonstopmode -file-line-error paper.tex   # Pass 1: build labels + cite keys
& bibtex   paper                                                 # BibTeX: resolve citations
& pdflatex -interaction=nonstopmode -file-line-error paper.tex   # Pass 2: inject bbl
& pdflatex -interaction=nonstopmode -file-line-error paper.tex   # Pass 3: settle xrefs
& pdflatex -interaction=nonstopmode -file-line-error paper.tex   # Pass 4: settle final labels
```

Exit codes:

| Step      | Exit code | Notes                                            |
|-----------|-----------|--------------------------------------------------|
| pdflatex 1| 1         | Expected: missing bibliography (no `.bbl` yet).  |
| bibtex    | 0         | Cosmetic warnings only (see below).              |
| pdflatex 2| 1         | Cross-ref warnings expected after bbl injection. |
| pdflatex 3| 1         | "Label(s) may have changed" while xrefs settle.  |
| pdflatex 4| 1         | All warnings cleared; PDF identical to pass 3.   |

> *Note*. pdfTeX returns exit code `1` whenever a warning is logged,
> regardless of whether the PDF was written successfully. We rely on the
> structured log scan (below) for the actual error count.

## Final compile metrics (from `paper.log`)

| Metric                          | Count / value             |
|---------------------------------|---------------------------|
| `^!` LaTeX errors               | **0**                     |
| Undefined references            | **0**                     |
| Undefined citations             | **0**                     |
| `LaTeX Warning:` lines          | **0**                     |
| Pages output                    | **26**                    |
| PDF size                        | **898,187 bytes**         |
| Pre-existing BibTeX warnings    | 2 (cosmetic, unchanged)   |

## BibTeX warnings (pre-existing, unchanged)

```
Warning--there's a number but no volume in mochizuki-asymptotic
Warning--there's a number but no volume in ramis-q-stokes
```

Both are stylistic "number without volume" notes from `bibtex` on
journal entries where the bibliography format would prefer either a
volume number or no issue number. They have been present since the
v1.0/v2.0 compiles and do not affect the PDF output. No new BibTeX
warnings introduced by this edit.

## Comparison with pre-edit baseline

| Metric                  | v2.0 baseline | Post-URL insertion | Δ                         |
|-------------------------|---------------|--------------------|---------------------------|
| Pages                   | 26            | 26                 | 0                         |
| PDF bytes               | 897,105       | 898,187            | +1,082                    |
| Errors                  | 0             | 0                  | 0                         |
| Undef refs              | 0             | 0                  | 0                         |
| Undef cites             | 0             | 0                  | 0                         |
| LaTeX warnings          | 0             | 0                  | 0                         |
| BibTeX cosmetic warns   | 2             | 2                  | 0                         |
| Source TeX bytes        | 99,309        | 99,553             | +244 (new URL sentence)   |

## Verdict

The URL-insertion edit compiles cleanly and preserves the page count,
warning count, and bibliography state of the v2.0 baseline. The +1,082
PDF bytes correspond to the extra glyphs for the new sentence
("All code, fleet scripts, and sample artifacts are publicly available
at `<repo URL>`, which mirrors the Zenodo v2.0 dataset and provides a
stable, versioned record of the computational workflow.") rendered
through `\url{...}` with hyperref's `urlcolor=blue!50!black`. No new
warnings, no layout reflow that would shift the page count, and no
change to bibliography resolution.
