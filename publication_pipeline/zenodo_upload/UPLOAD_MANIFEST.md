# Zenodo v2.0 — Upload Manifest

**Drag this entire folder (or the companion zip) onto Zenodo draft
[20387847](https://zenodo.org/uploads/20387847).**

After Zenodo assigns the DOI (it will be `10.5281/zenodo.20387847`),
run `publication_pipeline/doi_propagation_commands.sh 10.5281/zenodo.20387847`
from the repo root to propagate the DOI across every placeholder file
and re-tag `v2.0` on GitHub.

---

## Folder identity

| | |
|---|---|
| Path (workspace) | `publication_pipeline/zenodo_upload/` |
| Companion zip    | `publication_pipeline/zenodo_upload.zip` (1.26 MB) |
| File count       | **45** (44 deposit files + this manifest) |
| Total size       | **3.96 MB** (uncompressed) |
| Record draft     | https://zenodo.org/uploads/20387847 |
| Expected DOI     | `10.5281/zenodo.20387847` |
| GitHub mirror    | https://github.com/papanokechi/wkb-newton-polygons |

---

## Layout (44 files)

### Top-level (12 files, 1.04 MB)

| File | Bytes | Notes |
|---|---:|---|
| `manuscript.tex`             |  99,553 | LaTeX source; line 2044 contains the public GitHub URL. |
| `manuscript.pdf`             | 898,187 | Camera-ready 26-page PDF (4-pass clean compile). |
| `manuscript.bbl`             |   5,533 | Pre-built bibliography (so `pdflatex manuscript.tex` works without bibtex). |
| `paper.bbl`                  |   5,533 | Same bbl, alternate basename so `pdflatex paper.tex` also works (paper.tex is in arxiv_bundle/, but Zenodo readers may rename). |
| `references.bib`             |   8,753 | 24-entry BibTeX bibliography. |
| `LICENSE-CODE`               |   1,210 | MIT (applies to `code/`, `fleets/`). |
| `LICENSE-TEXT`               |   1,407 | CC-BY-4.0 (applies to `manuscript.*`, `figures/`, `reports/`, `data/`). |
| `CITATION.cff`               |   1,719 | Machine-readable citation metadata. |
| `citation_block.txt`         |   4,757 | Plain-text + BibTeX/APA/Chicago/IEEE citation strings. |
| `README.md`                  |   7,195 | Top-level Zenodo record description. |
| `release_notes_v2.0.txt`     |   8,137 | Full v2.0 release notes. |
| `zenodo_metadata_v2.0.txt`   |   6,264 | This record's metadata in plain text (for transparency). |

### `figures/` (2 files, 143 KB)

| File | Bytes | Licence |
|---|---:|---|
| `figures/constellations.png` | 141,890 | CC-BY-4.0 |
| `figures/taxonomy_tikz.tex`  |   4,792 | CC-BY-4.0 |

### `data/` (19 files, 2.42 MB) — full Phase I–V JSON atlas, CC-BY-4.0

| File | Bytes |
|---|---:|
| `data/chi.json`                 | 17,896 |
| `data/clusters.json`            | 24,530 |
| `data/constellations.json`      | 78,954 |
| `data/counterexamples.json`     |  9,046 |
| `data/newton.json`              | 55,364 |
| `data/operators.json`           | 28,565 |
| `data/phase3_clusters.json`     | 85,896 |
| `data/phase3_conjectures.json`  | 11,422 |
| `data/phase3_gaps.json`         |  4,564 |
| `data/phase3_invariants.json`   | 532,046 |
| `data/phase3_operators.json`    | 93,423 |
| `data/phase3_summary.json`      |  2,569 |
| `data/phase4_consistency.json`  | 11,958 |
| `data/phase4_framework.json`    |  3,631 |
| `data/phase4_lift.json`         |  7,782 |
| `data/phase4_sample.json`       |  2,230 |
| `data/phase4_stokes.json`       | 1,524,593 |
| `data/phase4_theorems.json`     | 16,208 |
| `data/phase5_targets.json`      | 25,169 |

### `reports/` (6 files, 174 KB, CC-BY-4.0)

| File | Bytes |
|---|---:|
| `reports/conjectures.md`        | 24,259 |
| `reports/integration_map.md`    |  4,979 |
| `reports/paper_draft.md`        | 23,897 |
| `reports/phase3_report.md`      | 32,120 |
| `reports/phase4_report.md`      | 42,539 |
| `reports/proofs.md`             | 50,617 |

### `code/` (1 file, MIT)

| File | Bytes |
|---|---:|
| `code/plot_constellations.py`   |  2,405 |

### `fleets/` (4 files, 228 KB, MIT)

| File | Bytes |
|---|---:|
| `fleets/fleet.py`               | 43,384 |
| `fleets/fleet3.py`              | 69,822 |
| `fleets/fleet4.py`              | 58,252 |
| `fleets/fleet5.py`              | 61,932 |

---

## How to upload

### Option A — single zip (fastest)

1. Open <https://zenodo.org/uploads/20387847>.
2. Drag `publication_pipeline/zenodo_upload.zip` onto the file area.
3. Paste the metadata from
   `publication_pipeline/zenodo_v2_metadata/zenodo_metadata_ready.txt`
   (or push it via the REST API with
   `zenodo_metadata_ready.json`).
4. Click **Save**, then **Publish**.

### Option B — drag the folder (44 individual entries)

1. Open <https://zenodo.org/uploads/20387847>.
2. Drag the entire `publication_pipeline/zenodo_upload/` folder onto
   the file area (Zenodo preserves the directory paths in filenames).
3. Same metadata step + **Publish**.

### Option C — scripted

From the repo root, with your Zenodo personal access token in
`$env:ZENODO_TOKEN`:

```powershell
.\publication_pipeline\zenodo_v2_metadata\zenodo_upload.ps1
```

The script pushes metadata + all 44 files via the bucket API. Re-run
with `-Publish` to publish.

---

## Verification

| Check | Result |
|---|---|
| File count                          | 44 ✓ |
| Total size                          | 3.95 MB ✓ |
| manuscript.pdf SHA-256              | `6DC11EC007E9B329…` (matches paper/ rebuilt PDF) |
| Manuscript contains GitHub repo URL | ✓ (line 2044 of manuscript.tex) |
| LICENSE-CODE (MIT) present          | ✓ |
| LICENSE-TEXT (CC-BY-4.0) present    | ✓ |
| CITATION.cff has ORCID              | ✓ (0009-0000-6192-8273) |
| paper.pdf alias dropped (dedup)     | ✓ (kept only canonical manuscript.pdf) |
| Both `*.bbl` names present          | ✓ (`manuscript.bbl` and `paper.bbl`, identical content) |

---

## Notes

- **`paper.bbl` is included in addition to `manuscript.bbl`** so that
  readers who run `pdflatex paper.tex` or `pdflatex manuscript.tex`
  both get a successful compile without re-running bibtex. The two
  files are byte-identical aliases.
- **`paper.pdf` was removed** as a redundant alias of `manuscript.pdf`
  (byte-identical, would just bloat the Zenodo record).
- **`paper.tex` is not included** in the Zenodo upload — it lives in
  the GitHub `arxiv_bundle/` and `journal_bundle/` folders, and is
  byte-identical to `manuscript.tex` anyway. `manuscript.tex` is the
  canonical source name in this record.
- All metadata placeholders (`10.5281/zenodo.XXXXXXX`,
  `arXiv:XXXX.XXXXX`) are intentional — they'll be substituted by
  `doi_propagation_commands.sh` once Zenodo and arXiv assign real
  identifiers.
