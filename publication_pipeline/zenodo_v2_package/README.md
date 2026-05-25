# The WKB Geometry of Newton Polygons — Zenodo v2.0 Package

This is the **Zenodo v2.0 upload package** for the project

> **The WKB Geometry of Newton Polygons: A Functorial Classification Theory**
> Papanokechi (2026)
> DOI: [10.5281/zenodo.XXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXX)
> arXiv: arXiv:XXXX.XXXXX (placeholder; updated after submission)
> GitHub: <https://github.com/papanokechi/wkb-newton-polygons>

v2.0 **supersedes** [v1.0](https://doi.org/10.5281/zenodo.20355904) by
promoting the dataset to a complete, refereed publication with the
camera-ready manuscript and full in-manuscript proofs.

---

## What this Zenodo record contains

| Top-level file                | Description                                  |
|-------------------------------|----------------------------------------------|
| `manuscript.pdf`              | **Camera-ready paper** — 26 pp, 897 KB       |
| `manuscript.tex`              | LaTeX source (99,309 B)                       |
| `references.bib`              | BibTeX bibliography (24 entries)              |
| `paper.bbl`                   | Pre-built bibliography (no `bibtex` needed)   |
| `LICENSE-CODE`                | MIT (applies to `code/`, `fleets/`)            |
| `LICENSE-TEXT`                | CC-BY 4.0 (applies to `manuscript.*`, `reports/`, `figures/`) |
| `CITATION.cff`                | Machine-readable citation metadata           |
| `citation_block.txt`          | Plain-text + BibTeX citation strings         |
| `release_notes_v2.0.txt`      | Detailed release notes                        |
| `zenodo_metadata_v2.0.txt`    | This record's Zenodo metadata (for transparency) |

| Sub-directory  | # files | Description                                |
|----------------|--------:|--------------------------------------------|
| `figures/`     |       2 | `constellations.png`, `taxonomy_tikz.tex`  |
| `data/`        |      19 | Full Phase I–V JSON atlas (~2.6 MB)         |
| `reports/`     |       6 | Phase reports + `proofs.md` + `integration_map.md` |
| `code/`        |       1 | `plot_constellations.py`                   |
| `fleets/`      |       4 | `fleet.py`, `fleet3.py`, `fleet4.py`, `fleet5.py` |

Total: 41 files.

---

## How to use this record

### Read the paper

Open `manuscript.pdf` (26 pages). The notation table is in §2 and
covers all symbols. The main classification result is Theorem 3.x; the
eight proven theorems are M1, N1, D2, S1, AT1, AT3, AT5, AT7.

### Recompile the paper from source

```bash
pdflatex manuscript.tex
# (paper.bbl is pre-built, so bibtex is optional)
pdflatex manuscript.tex
pdflatex manuscript.tex
```

Result: byte-identical to `manuscript.pdf` (modulo TeX timestamp).

### Use the dataset

The 19 JSON files in `data/` form a self-contained atlas. See
`reports/phase3_report.md` and `reports/phase4_report.md` for the
content overview. Schemas are documented in the file headers; values
use standard JSON (no extensions).

### Re-derive the dataset

```bash
python fleets/fleet.py    # Phase I+II
python fleets/fleet3.py   # Phase III
python fleets/fleet4.py   # Phase IV
python fleets/fleet5.py   # Phase V
```

Outputs are byte-deterministic given Python ≥ 3.10 and the
seeds/parameters pinned at the top of each script.

### Re-render Figure 2

```bash
python code/plot_constellations.py \
    --input  data/constellations.json \
    --output figures/constellations.png
```

---

## Related identifiers

| Relation         | Identifier                                            |
|------------------|-------------------------------------------------------|
| `isNewVersionOf` | [10.5281/zenodo.20355904](https://doi.org/10.5281/zenodo.20355904) (v1.0) |
| `isSupplementTo` | arXiv:XXXX.XXXXX (placeholder)                         |
| `isSourceOf`     | <https://github.com/papanokechi/wkb-newton-polygons>   |
| `isIdenticalTo`  | <https://github.com/papanokechi/wkb-newton-polygons/releases/tag/v2.0> |

---

## Licensing

| Files                            | License        |
|----------------------------------|----------------|
| `manuscript.pdf`, `manuscript.tex`, `paper.bbl`, `references.bib`, `figures/*`, `reports/*` | [CC BY 4.0](LICENSE-TEXT) |
| `code/*`, `fleets/*`             | [MIT](LICENSE-CODE)         |
| `data/*` (the JSON atlas)        | [CC BY 4.0](LICENSE-TEXT)   |

You are free to use, modify, and redistribute these materials provided
you preserve attribution and respect the per-file license terms.

---

## Citation

See `citation_block.txt` for BibTeX, plain-text, APA, Chicago, and IEEE
forms. The preferred BibTeX entry is:

```bibtex
@misc{papanokechi-wkb-newton-2026,
  author       = {Papanokechi},
  title        = {The {WKB} Geometry of {Newton} Polygons:
                  A Functorial Classification Theory},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {2.0},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {https://doi.org/10.5281/zenodo.XXXXXXX}
}
```

---

## What's new in v2.0 (vs v1.0)

* Camera-ready manuscript (26 pp PDF) with full in-manuscript proofs of
  M1, N1, D2, S1, AT1, AT3, AT5, AT7.
* Real TikZ taxonomy figure replacing the v1.0 placeholder; depicts the
  23 → 39 class refinement under µ_q / µ_q' symmetry.
* Round-1 referee revisions: calibrated novelty in abstract,
  precise functoriality on the explicit category $\mathcal{O}\mathrm{p}_1$,
  Theorem 5.1 restated, notation table, dataset identifiers removed
  from prose, AI/computational disclosure (§11).
* Round-2 referee revisions: Lemma `chi-multiplicative` widened to
  multi-slope adjunction, Theorem 5.1 Step 2 arithmetic corrected,
  abstract trimmed to 186 non-math words, (OS3) sharpened and
  cross-referenced in Theorem 7.1 Step 4.
* arXiv-ready and journal-ready submission bundles available in the
  companion GitHub repository.

See `release_notes_v2.0.txt` for full details.

---

## Known limitations

* Stokes constants are **not** computed in this release (only
  directions and Galois groupoids); planned for v3.0.
* Wild character varieties are stated as a target only.
* Operators with more than one irregular singularity are out of scope
  for this release.

---

## Author

**Papanokechi** · Independent Researcher
ORCID: [0009-0000-6192-8273](https://orcid.org/0009-0000-6192-8273)

---

## Computational and AI disclosure

The Phase I–V atlas was generated by a fleet of orchestrated Python
pipelines (`fleets/`). AI assistance was used for conjecture selection,
proof-skeleton drafting, counterexample guarding, refinement passes,
and manuscript assembly. All mathematical statements, proofs, and
classifications were reviewed and finalised by the human author. See
§11 of `manuscript.pdf` for the full disclosure.

---

## Acknowledgements

Computational work used Python 3.10+, sympy, numpy, mpmath, and
TikZ/pdfTeX. Thank you to the anonymous referees of the Round-1 and
Round-2 reviews for the careful and constructive feedback that
materially improved this work.
