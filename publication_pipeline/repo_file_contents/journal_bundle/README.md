# `journal_bundle/` — Journal submission bundle

This directory is a **submission-ready package for a math-physics
journal** (e.g., *Comm. Math. Phys.*, *J. Phys. A*, *Adv. Math.*,
*SIGMA*).

## Contents

| File                              | Description                          |
|-----------------------------------|--------------------------------------|
| `paper.tex`                        | Master source                        |
| `paper.bbl`                        | Pre-built bibliography               |
| `references.bib`                   | Source bibliography                  |
| `paper.pdf`                        | Compiled PDF                         |
| `class-file-placeholder.tex`       | Marker for the journal class file    |
| `figures/`                         | `constellations.png`, `taxonomy_tikz.tex` |
| `README.md`                        | This file                            |

## How to adapt for a specific journal

1. **Locate the journal's class file** (e.g. `cmp.cls`, `JPhysA.cls`,
   `imamatNo.cls`, `sigma.cls`).
2. **Place it next to `paper.tex`** in this directory.
3. **Edit `paper.tex`**: change `\documentclass{article}` to the
   journal's class invocation (e.g. `\documentclass[12pt]{cmp}`).
4. **Verify the `\title`, `\author`, `\affiliation`, `\thanks`** macros
   match the class's expected interface.
5. **Recompile**:
   ```bash
   pdflatex paper.tex
   bibtex   paper
   pdflatex paper.tex
   pdflatex paper.tex
   ```

## Author metadata for journal submission

The `\author` block uses:

```latex
\author{Papanokechi}
\thanks{Independent Researcher.
        ORCID: \href{https://orcid.org/0009-0000-6192-8273}{0009-0000-6192-8273}.
        Email: see Zenodo record.}
```

Most journals also require a cover-letter PDF and a brief abstract in
plain text. The plain-text abstract (186 non-math words) is available
in `../major_revision/followup/revised_abstract_v2.tex` (strip
LaTeX macros to obtain plain text).

## MSC 2020 codes

* Primary: 34E20 (Singular perturbations; WKB)
* Secondary: 34M30, 39A06, 39A13

## Suggested keywords (for journal metadata form)

WKB analysis, Newton polygon, irregular singularity, formal
classification, Stokes phenomenon, anti-Stokes directions,
Levelt–Turrittin theorem, exponent constellation, $\mu_q$-pullback,
slope filtration, Kummer dichotomy, $p$-visibility.

## Files that **must NOT be edited** before journal submission

* `references.bib` — bibliography style is locked.
* `paper.bbl` — regenerate after editing `references.bib`, do not
  hand-edit.
* `figures/` — both figures are camera-ready.

## Differences from `arxiv_bundle/`

The journal bundle uses a placeholder class-file invocation that will
be replaced by the journal-specific class at production. Otherwise the
body, theorems, figures, and bibliography are byte-identical to
`arxiv_bundle/paper.tex`.
