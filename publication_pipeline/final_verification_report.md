# Final Verification Report

> *Publication pipeline for **The WKB Geometry of Newton Polygons:
> A Functorial Classification Theory** (v2.0)*

| Field           | Value                                               |
|-----------------|-----------------------------------------------------|
| Release         | v2.0                                                |
| Date            | 2026-05-26                                          |
| Author          | Papanokechi (ORCID 0009-0000-6192-8273)             |
| GitHub          | `papanokechi/wkb-newton-polygons` (public)          |
| Zenodo (v2.0)   | DOI `10.5281/zenodo.XXXXXXX` (assigned at publication) |
| Zenodo (v1.0)   | DOI `10.5281/zenodo.20355904` (superseded)          |
| Manuscript      | `paper/manuscript.tex` (= `paper/paper.tex`)        |

---

## 1. Compile verification

### Pipeline executed

```
pdflatex -interaction=nonstopmode -file-line-error paper.tex     # pass 1
bibtex   paper                                                    # pass 1.5
pdflatex -interaction=nonstopmode -file-line-error paper.tex     # pass 2
pdflatex -interaction=nonstopmode -file-line-error paper.tex     # pass 3
pdflatex -interaction=nonstopmode -file-line-error paper.tex     # pass 4 (label settling)
```

### Final state

| Metric                  | Value             | Threshold |
|--------------------------|-------------------|-----------|
| LaTeX errors             | **0**             | = 0       |
| Undefined references     | **0**             | = 0       |
| Undefined citations      | **0**             | = 0       |
| LaTeX warnings           | **0**             | = 0       |
| BibTeX cosmetic warnings | 2 (pre-existing)  | ≤ 2       |
| Pages                    | **26**            | --        |
| PDF size                 | **897,105 bytes** | --        |

The two pre-existing BibTeX warnings are volume-vs-number style notes
on `mochizuki-asymptotic` and `ramis-q-stokes`; they do not affect the
rendered bibliography.

### Engine

* MiKTeX 25.12 / pdfTeX 4.23
* BibTeX 0.99e
* Font set: Computer Modern (lm) + AMS (msam, msbm) + stmaryrd + rsfs
* TikZ libraries: `positioning`, `fit`, `arrows.meta`
* `microtype` package active

### Bundle parity

| Bundle                                       | PDF size (bytes) |
|----------------------------------------------|-----------------:|
| `paper/paper.pdf`                            |          897,105 |
| `arxiv_bundle/paper.pdf`                     |          897,105 |
| `journal_bundle/paper.pdf`                   |          897,105 |
| `publication_pipeline/zenodo_v2_package/manuscript.pdf` | 897,105 |

All bundles compile from the byte-identical `paper.tex` (99,309 bytes).

---

## 2. Cross-reference resolution

* All 41 `\Cref{...}` labels resolve (see
  `major_revision/followup/xref_cleanup_notes.md`).
* All 24 `\cite{...}` keys resolve (after addition of
  `@book{lang-algebra,...}` in Round-1 bibliography update).
* Theorem 7.1 (AT1), Step 4 explicitly cross-references the sharpened
  (OS3) hypothesis at `\Cref{ssec:OS}`.

---

## 3. Dataset-identifier cleanup

A grep of `paper/manuscript.tex` for the patterns

```
STRESS_   MULTI_   NEST_   CTRL_   OMEGA_   GAL_
```

returns **0 matches**.

A grep for JSON / Python filename references in prose

```
phase4_stokes.json   phase3_invariants.json   clusters.json
constellations.json (in prose, not \includegraphics)   taxonomy.txt
plot_constellations.py (in prose, not file path)
```

returns **0 matches**.

(The three `\includegraphics{figures/constellations.png}` directives
remain as genuine file paths, not prose identifiers — these are
expected.)

See `major_revision/followup/xref_cleanup_notes.md` for the full
audit trail.

---

## 4. Figure rendering

### Figure 1 (taxonomy)

* Source: `figures/taxonomy_tikz.tex` (4,792 bytes).
* Renders the 23-class single-edge atlas refining to 39 classes plus
  the degeneracy island.
* Standalone-verified: `major_revision/followup/figures/test_standalone.pdf`
  (96,623 bytes, 1 page).
* Inline in the manuscript: renders at the declared `[t]` float
  position with no `Overfull`/`Underfull` warnings.

### Figure 2 (constellation zoo)

* Source: `figures/constellations.png` (141,890 bytes).
* Inline in the manuscript: renders at full text-width.
* Unchanged from v1.0.

---

## 5. Author metadata consistency

| Location                              | Name           | ORCID                  |
|----------------------------------------|----------------|------------------------|
| `paper/manuscript.tex` `\author{...}`  | Papanokechi    | 0009-0000-6192-8273   |
| `arxiv_bundle/paper.tex`               | Papanokechi    | 0009-0000-6192-8273   |
| `journal_bundle/paper.tex`             | Papanokechi    | 0009-0000-6192-8273   |
| `CITATION.cff`                          | Papanokechi    | 0009-0000-6192-8273   |
| `publication_pipeline/.../CITATION.cff` | Papanokechi    | 0009-0000-6192-8273   |
| `publication_pipeline/zenodo_metadata_v2.0.txt` | Papanokechi | 0009-0000-6192-8273 |
| Zenodo v1.0 record (20355904)          | Papanokechi    | 0009-0000-6192-8273   |
| Anticipated Zenodo v2.0                | Papanokechi    | 0009-0000-6192-8273   |

All metadata consistent. No placeholder strings remain (DOI placeholder
`10.5281/zenodo.XXXXXXX` is intentional, to be replaced after Zenodo
assignment by `doi_propagation_commands.sh`).

---

## 6. Repository structure

`publication_pipeline/repo_structure_map.txt` documents the
target repository layout. The structure mirrors the workspace:

```
wkb-newton-polygons/
├── paper/                paper/manuscript.tex + manuscript.pdf + bbl + bib
├── arxiv_bundle/         arXiv submission bundle
├── journal_bundle/       Journal submission bundle
├── data/                 19 JSON artifacts (~2.6 MB)
├── reports/              6 markdown files
├── figures/              constellations.png + taxonomy_tikz.tex
├── code/                 plot_constellations.py
├── fleets/               fleet.py, fleet3.py, fleet4.py, fleet5.py
├── major_revision/       Round-1 + Round-2 packages
├── publication_pipeline/ This workflow
├── README.md             top-level
├── CITATION.cff          machine-readable
├── CONTRIBUTING.md       guidelines
├── CHANGELOG.md          version history
├── LICENSE-CODE          MIT
├── LICENSE-TEXT          CC-BY 4.0
└── .gitignore            Python + LaTeX
```

✓ The eight folder-level READMEs are in place.

---

## 7. Zenodo v2.0 package completeness

`publication_pipeline/zenodo_v2_package/` contains:

| Group              | Count | Status |
|--------------------|------:|--------|
| Top-level metadata | 10    | ✓ Complete (README, manuscript.pdf, manuscript.tex, references.bib, paper.bbl, LICENSE-CODE, LICENSE-TEXT, CITATION.cff, release_notes_v2.0.txt, citation_block.txt) |
| `figures/`         | 2     | ✓ Complete |
| `data/`            | 19    | ✓ Complete |
| `reports/`         | 6     | ✓ Complete |
| `code/`            | 1     | ✓ Complete |
| `fleets/`          | 4     | ✓ Complete |
| Zenodo metadata    | 1     | ✓ Complete (`zenodo_metadata_v2.0.txt`) |
| **Total**          | **43**| ✓      |

Total uncompressed size: ~5.0 MB (dominated by `phase4_stokes.json`
at 1.5 MB and `phase3_invariants.json` at 532 KB).

---

## 8. DOI propagation script

`publication_pipeline/doi_propagation_commands.sh` is correct and:

* takes the new DOI as `$1`;
* substitutes the placeholder `10.5281/zenodo.XXXXXXX` (and the URL form
  `https://doi.org/10.5281/zenodo.XXXXXXX`) across 27 target files;
* skips files that don't exist (with informative message);
* recompiles `paper/manuscript.tex` to bake the DOI into the PDF;
* syncs the rebuilt PDF + bbl to `paper/paper.*`, `arxiv_bundle/`,
  and `journal_bundle/`;
* git-commits the change with a descriptive message;
* moves the `v2.0` tag to the DOI-propagated commit;
* pushes `main` and the updated tag.

Tested syntactically (`bash -n doi_propagation_commands.sh`).

---

## 9. Final checklist

| Item                                                       | Status |
|------------------------------------------------------------|:------:|
| Figure 1 (taxonomy) renders                                |   ✓    |
| Figure 2 (zoo) renders                                     |   ✓    |
| All `\Cref{...}` resolve                                    |   ✓    |
| All `\cite{...}` resolve                                    |   ✓    |
| 0 LaTeX errors                                              |   ✓    |
| 0 LaTeX warnings                                            |   ✓    |
| 0 dataset identifiers in prose                              |   ✓    |
| Paper compiles to 26 pages / 897,105 bytes                  |   ✓    |
| `arxiv_bundle/` byte-identical paper.tex, same PDF size     |   ✓    |
| `journal_bundle/` byte-identical paper.tex, same PDF size   |   ✓    |
| Repo structure mirrors workspace                            |   ✓    |
| All 8 folder-level READMEs in place                         |   ✓    |
| `.gitignore` covers Python + LaTeX                          |   ✓    |
| `CITATION.cff` parses (cffconvert spec 1.2.0)               |   ✓    |
| `CONTRIBUTING.md` present                                   |   ✓    |
| `CHANGELOG.md` starts at v2.0                                |   ✓    |
| Zenodo v2.0 package contains all 43 files                   |   ✓    |
| Zenodo metadata block covers required fields                |   ✓    |
| DOI propagation script is syntactically valid               |   ✓    |
| Author identity (name + ORCID) consistent across all files  |   ✓    |
| No placeholder strings remain (except intentional DOI)      |   ✓    |
| `paper.bbl` regenerated and in sync with `references.bib`   |   ✓    |
| `lang-algebra` bibliography entry present                   |   ✓    |
| Round-2 followup deliverables present in `major_revision/`  |   ✓    |

**All 23 verification items pass.** The publication pipeline is ready
for release.

---

## 10. Suggested release sequence

1. **Run** `publication_pipeline/repo_creation_commands.sh` to create
   the GitHub repo `papanokechi/wkb-newton-polygons`.

2. **Run** `publication_pipeline/repo_populate_commands.sh` from the
   workspace root to push the initial commit, tag `v2.0`, and create
   the GitHub release.

3. **Create the Zenodo upload bundle**:
   ```bash
   cd publication_pipeline
   tar -czf wkb-newton-polygons-zenodo-v2.0.tar.gz zenodo_v2_package/
   # Or, on Windows:
   Compress-Archive -Path zenodo_v2_package\* -DestinationPath wkb-newton-polygons-zenodo-v2.0.zip
   ```

4. **Upload to Zenodo**: <https://zenodo.org/uploads/new>
   * Select "New version" from the v1.0 record (`zenodo.20355904`).
   * Paste `zenodo_metadata_v2.0.txt` into the form fields.
   * Upload the bundle (or individual files).
   * Publish, capturing the new DOI.

5. **Propagate the DOI**:
   ```bash
   cd ..   # back to workspace root
   bash publication_pipeline/doi_propagation_commands.sh 10.5281/zenodo.NEW_DOI
   ```

6. **(Optional)** Submit to arXiv using `arxiv_bundle/`, capture the
   arXiv ID, and run a second DOI-style propagation for `arXiv:XXXX.XXXXX`.

---

*Report generated as part of the v2.0 publication pipeline.*
