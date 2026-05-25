# wkb-newton-polygons

Consolidated working tree for the project

> **The WKB Geometry of Newton Polygons: A Functorial Classification Theory.**
> *Papanokechi, Independent Researcher
> ([ORCID 0009-0000-6192-8273](https://orcid.org/0009-0000-6192-8273))*

This folder is the **single, canonical workspace** for the camera-ready
paper and its companion computational atlas (v1.0). Everything produced
across Phases I–VI of the fleet investigation lives here.

For the long-form project README — phase summaries, classification
theory overview, full artifact descriptions, reproducibility, and
licensing details — see [`README.md`](README.md) (the Zenodo-package
README, included verbatim).

---

## Layout

```
wkb-newton-polygons/
├── README.md                       # Zenodo-package README (full project doc)
├── README-LAYOUT.md                # THIS FILE — directory map only
├── CITATION.cff                    # Citation File Format (CFF v1.2)
├── LICENSE-CODE                    # MIT (applies to /code and /fleets)
├── LICENSE-TEXT                    # CC-BY-4.0 (applies to everything else)
│
├── citation_block.txt              # BibTeX / plain-text / CFF citation snippets
├── zenodo_metadata.txt             # Zenodo upload metadata block
├── release_notes_v1.0.txt          # v1.0 release notes
├── submission_checklist.md         # Camera-ready / arXiv / journal checklist
├── author_metadata_patch.txt       # Diff of the Zenodo identity alignment
├── directory_structure.txt         # Original (Zenodo-side) directory spec
│
├── paper/                          # MASTER LaTeX source (build here)
│   ├── paper.tex                   # The manuscript (19 pp.)
│   ├── paper.pdf                   # Compiled PDF
│   ├── paper.bbl                   # Pre-built bibliography
│   ├── references.bib              # 23-entry BibTeX database
│   └── figures/constellations.png  # Figure 2 (constellation zoo)
│
├── arxiv_bundle/                   # arXiv submission package
│   ├── paper.tex, paper.bbl, paper.pdf, references.bib
│   ├── README.md                   # Build & submission instructions
│   └── figures/constellations.png
│
├── journal_bundle/                 # Journal submission package
│   ├── paper.tex, paper.bbl, paper.pdf, references.bib
│   ├── README.md                   # Per-journal class-file switch notes
│   ├── class-file-placeholder.txt  # Springer/Elsevier/AMS/JEP/SIGMA instructions
│   └── figures/constellations.png
│
├── data/                           # JSON artifacts of Phases I–V
│   ├── operators.json, newton.json, chi.json, constellations.json
│   ├── clusters.json, counterexamples.json
│   ├── phase3_{gaps,operators,invariants,clusters,conjectures,summary}.json
│   ├── phase4_{framework,lift,sample,stokes,consistency,theorems}.json
│   └── phase5_targets.json
│
├── reports/                        # Markdown reports + theorem material
│   ├── paper_draft.md              # Draft prose (abstract / outline / vision)
│   ├── proofs.md                   # 8 theorem-proof blocks (M1, N1, D2, S1, AT1, AT3, AT5, AT7)
│   ├── integration_map.md          # Section-placement map for proofs.md
│   ├── conjectures.md              # Phase I/II conjecture list
│   ├── phase3_report.md            # Phase III synthesis
│   └── phase4_report.md            # Phase IV synthesis
│
├── figures/                        # Top-level master figure
│   └── constellations.png
│
├── code/                           # Utility / plotting scripts
│   └── plot_constellations.py
│
└── fleets/                         # Fleet-of-agents pipeline scripts
    ├── fleet.py                    # Phase I/II
    ├── fleet3.py                   # Phase III
    ├── fleet4.py                   # Phase IV
    └── fleet5.py                   # Phase V
```

---

## Build the paper

```powershell
cd paper
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

Three `pdflatex` passes (plus one `bibtex`) settle all cross-references.
Output: 19 pages, ~827 KB, zero LaTeX warnings, zero undefined refs.

---

## Build a submission bundle

The bundles ship with a pre-compiled `paper.bbl`, so for either
`arxiv_bundle/` or `journal_bundle/` only three `pdflatex` passes are
needed (no `bibtex` call):

```powershell
cd arxiv_bundle    # or: cd journal_bundle
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

The journal bundle ships with `class-file-placeholder.txt`, which lists
the exact `\documentclass{...}` substitution for Springer Nature
(LMaPh / AHP), Elsevier (`elsarticle`), AMS (`amsart`), JEP (`jep`), and
SIGMA (`sigma`).

---

## Reproduce the atlas

The five fleet scripts in `fleets/` reproduce the full computational
atlas:

```powershell
python fleets/fleet.py     # Phase I/II
python fleets/fleet3.py    # Phase III (multi-edge, systems, resonances)
python fleets/fleet4.py    # Phase IV (analytic lifting)
python fleets/fleet5.py    # Phase V  (theorem-proof consolidation)
```

All computations are exact (sympy / fractions); re-runs reproduce the
JSON artifacts byte-wise. See the top-level `README.md` for a full
phase-by-phase reproducibility note.

---

## Identity & licensing

* **Author:** Papanokechi (Independent Researcher).
* **ORCID:** [0009-0000-6192-8273](https://orcid.org/0009-0000-6192-8273).
* **Code:** MIT (`LICENSE-CODE`).
* **Text, data, figures:** CC-BY-4.0 (`LICENSE-TEXT`).
* **Companion Zenodo dataset DOI:** `10.5281/zenodo.XXXXXXX`
  *(placeholder; assigned at upload).*
* **Identity-source Zenodo record:**
  [10.5281/zenodo.20355904](https://doi.org/10.5281/zenodo.20355904)
  (Khinchin K_0 deposit; same author).

See `submission_checklist.md` for the full pre-submission checklist.
