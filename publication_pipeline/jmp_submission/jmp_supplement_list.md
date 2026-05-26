# JMP Supplementary Material List

**Strategy.** Cite the Zenodo deposit by DOI in the manuscript; do not
re-upload the full 44-file deposit to the AIP Editorial Manager
portal. AIP's Editorial Manager supports a small number of
supplementary files (typically ≤ 5 files, ≤ 50 MB total). The full
artifact tree is mirrored on Zenodo and on GitHub.

---

## 1 — External archival deposit (cited by DOI)

### Zenodo

| Field | Value |
|-------|-------|
| Version DOI | `10.5281/zenodo.20387847` |
| Concept DOI | `10.5281/zenodo.20387846` |
| Title | The WKB Geometry of Newton Polygons (companion dataset) |
| Author | Papanokechi |
| ORCID | 0009-0000-6192-8273 |
| Version | v1.0 |
| Licence | CC-BY-4.0 (text + data) / MIT (code) |
| File count | 44 |
| Total size | 3.96 MB |
| Public URL | `https://zenodo.org/records/20387847` |
| First published | 2026-05 |

### GitHub mirror

| Field | Value |
|-------|-------|
| Repository | `papanokechi/wkb-newton-polygons` |
| URL | `https://github.com/papanokechi/wkb-newton-polygons` |
| Tag | `v2.0` (manuscript-revision label; tracks Zenodo v1.0 deposit) |
| Licence | dual: CC-BY-4.0 + MIT (root `LICENSE-TEXT`, `LICENSE-CODE`) |
| Topics | wkb-analysis, newton-polygon, stokes-phenomenon, irregular-singularity, levelt-turrittin, classification-theory, mathematical-physics, computer-algebra, reproducible-research |

---

## 2 — Files uploaded directly to the JMP Editorial Manager portal

For a JMP submission, only the main manuscript and a small set of
required-by-portal files are uploaded:

| Slot | File | Source path | Size | Purpose |
|------|------|-------------|------|---------|
| Manuscript (PDF, compiled) | `manuscript.pdf` | `journal_bundle/paper.pdf` | 898,187 B | reviewer-facing PDF |
| Manuscript (TeX source) | `manuscript.tex` | `journal_bundle/paper.tex` | 99,553 B | typesetting source |
| Bibliography (source) | `references.bib` | `journal_bundle/references.bib` | ~ 6 KB | bib database |
| Bibliography (compiled) | `paper.bbl` | `journal_bundle/paper.bbl` | ~ 9 KB | bibliography output |
| Figure file | `figures/constellations.png` | `journal_bundle/figures/constellations.png` | ~ 130 KB | sole figure |
| Cover letter | `cover_letter.pdf` | (renderfrom `jmp_cover_letter.md`) | — | portal slot |

Total: 6 files, < 2 MB.

---

## 3 — Files cited by the manuscript but available *only* via Zenodo / GitHub

These are the artifacts that the manuscript references but that are
NOT uploaded to the JMP portal — they live in the Zenodo deposit /
GitHub repo and are accessible to reviewers via the DOI / repo URL.

### Data atlas (19 JSON files, ~ 1.7 MB)
- `chi.json`, `phase4_framework.json`, `phase4_lift.json`,
  `phase4_sample.json`, `phase4_stokes.json`,
  `phase4_consistency.json`, `phase4_theorems.json`,
  `phase5_targets.json`, `counterexamples.json`, ...

### Reports (6 markdown files, ~ 200 KB)
- `phase4_report.md`, `proofs.md`, `integration_map.md`,
  `final_verification_report.md`, `compile_log_repo_url.md`,
  `repo_url_verification_report.md`

### Pipeline scripts (5 Python files, ~ 200 KB)
- `fleet.py`, `fleet3.py`, `fleet4.py`, `fleet5.py`, plus utility
  scripts in `code/`.

### Repository metadata
- `README.md`, `CITATION.cff`, `LICENSE-CODE` (MIT),
  `LICENSE-TEXT` (CC-BY-4.0), `release_notes_v2.0.txt`,
  `CHANGELOG.md`, `CONTRIBUTING.md`.

---

## 4 — Reviewer-access summary (text for portal "Supplementary
Information" field)

> The full computational record supporting this submission — including
> all symbolic operators, JSON data atlases, fleet pipelines, proof
> skeletons, and rendered figures — is permanently archived at
> Zenodo, DOI `10.5281/zenodo.20387847` (concept DOI
> `10.5281/zenodo.20387846`), licensed CC-BY-4.0 / MIT, and mirrored
> at `https://github.com/papanokechi/wkb-newton-polygons`. The Zenodo
> deposit contains 44 files (~ 4 MB). Reviewers can re-execute the
> deterministic pipelines (`fleet.py` through `fleet5.py`) to reproduce
> every figure and every numerical statement in the manuscript. See
> §11 of the manuscript and the Zenodo `README.md` for the command
> sequence.

---

## 5 — Licence summary

| Asset class | Licence | Why |
|-------------|---------|-----|
| Manuscript text + figures | CC-BY-4.0 | journal-standard open-access licence; explicit in `LICENSE-TEXT` |
| Pipelines (`fleet.py` etc.) + utility code | MIT | permissive, enables downstream reuse |
| Data (JSON atlas + reports) | CC-BY-4.0 | matches manuscript |

The Zenodo deposit page lists CC-BY-4.0 as the top-level licence; MIT
is documented for the `code/` and `fleets/` subtrees via
`LICENSE-CODE` and a notice in each file header.
