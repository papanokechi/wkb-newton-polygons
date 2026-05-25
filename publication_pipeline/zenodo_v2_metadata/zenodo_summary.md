# Zenodo v2.0 Metadata Package — Summary

**Project.** "The WKB Geometry of Newton Polygons: A Functorial Classification Theory"
**Author.** Papanokechi · Independent Researcher · ORCID
[0009-0000-6192-8273](https://orcid.org/0009-0000-6192-8273)
**Version.** 2.0
**Publication date.** 2026-05-26
**GitHub.** <https://github.com/papanokechi/wkb-newton-polygons>
**v1.0 record being superseded.**
[10.5281/zenodo.20355904](https://doi.org/10.5281/zenodo.20355904)

---

## What this folder contains

`publication_pipeline/zenodo_v2_metadata/` — five publication-ready
artefacts for the Zenodo v2.0 upload:

| File | Purpose |
|---|---|
| `zenodo_metadata_ready.json` | Structured metadata block, ready to POST to Zenodo's REST API (`/api/deposit/depositions`). |
| `zenodo_metadata_ready.txt`  | Same content rendered as a human-readable copy-paste block for the Zenodo web upload form. |
| `zenodo_filelist.txt`        | Upload-time file checklist — every one of the 44 files in the upload bundle with size and per-file licence. |
| `zenodo_keywords.txt`        | Clean one-keyword-per-line list (19 keywords). |
| `zenodo_related_identifiers.txt` | The four related-identifier rows (isNewVersionOf v1.0, isSourceOf GitHub, isIdenticalTo tagged release, isSupplementTo arXiv placeholder). |
| `zenodo_summary.md`          | This document. |

The companion upload bundle lives at
`publication_pipeline/wkb-newton-polygons-zenodo-v2.0.zip` (44 entries,
2,090,144 bytes; regenerated 2026-05-26 to include the GitHub-repo-URL
insertion in the manuscript).

---

## Extracted metadata

### Title

> The WKB Geometry of Newton Polygons: A Functorial Classification Theory

(Matches `paper/paper.tex` `\title{...}` and `CITATION.cff` exactly.)

### Author

| Field | Value |
|---|---|
| Name | Papanokechi |
| Affiliation | Independent Researcher |
| ORCID | 0009-0000-6192-8273 |
| Email | *not present in any source file* — see note below |

> **Note on email.** No email address is recorded in `CITATION.cff`,
> `README.md`, the manuscript metadata, or the existing Zenodo metadata
> draft. Zenodo accepts author entries without an email; if you wish to
> publish a contact address, add it directly in the Zenodo web form at
> upload time and (optionally) propagate it back to `CITATION.cff`
> afterwards. The deliverables in this folder do not invent an email.

### Abstract

Sourced from `major_revision/followup/revised_abstract_v2.tex`.
**195 non-math words** (target ≤ 220).

The HTML-rendered version is embedded in `zenodo_metadata_ready.json`
under `metadata.description` and as a paste-ready block in
`zenodo_metadata_ready.txt`. The plain LaTeX original is preserved
verbatim at the source location.

### Keywords (19)

WKB analysis · Newton polygon · irregular singularity · formal
classification · Stokes phenomenon · anti-Stokes directions ·
Levelt-Turrittin theorem · exponent constellation · mu_q-pullback ·
slope filtration · Kummer dichotomy · p-visibility · functorial
classification · classification theory · q-difference operator ·
difference operator · irregular ODE · constellation map · reproducible
research

### MSC 2020 subjects

| Code  | Subject |
|-------|---------|
| 34E20 | Singular perturbations, turning point theory, WKB methods |
| 34M30 | Asymptotic, formal expansions in differential equations in the complex domain |
| 39A06 | Linear difference equations |
| 39A13 | q-difference equations |
| 12H05 | Differential algebra |

### Licence

Top-level Zenodo selector: **CC-BY-4.0**.
Within the record, files are dual-licensed:

| Files | Licence |
|---|---|
| `manuscript.*`, `paper.*`, `references.bib`, `figures/*`, `reports/*`, `data/*` | CC-BY-4.0 (`LICENSE-TEXT`) |
| `code/*`, `fleets/*` | MIT (`LICENSE-CODE`) |

### Related identifiers

| Relation | Identifier | Scheme |
|---|---|---|
| `isNewVersionOf` | `10.5281/zenodo.20355904` | doi |
| `isSourceOf`     | `https://github.com/papanokechi/wkb-newton-polygons` | url |
| `isIdenticalTo`  | `https://github.com/papanokechi/wkb-newton-polygons/releases/tag/v2.0` | url |
| `isSupplementTo` | `arXiv:XXXX.XXXXX` *(placeholder)* | arxiv |

### Communities

| Identifier | Purpose |
|---|---|
| `math-ph` | Mathematical physics |
| `exact-wkb` | Exact WKB theory community |
| `stokes-phenomena` | Stokes-phenomenon community |
| `reproducible-research` | Reproducibility-focused community |

> If a target community does not yet exist on Zenodo or has a different
> identifier, drop the missing line from
> `zenodo_metadata_ready.json` before upload — Zenodo otherwise rejects
> the deposit.

---

## Upload bundle (44 files; ~3.7 MB unzipped)

| Tier | Count | Total | Licence |
|---|---:|---:|---|
| Top-level | 12 | 1.94 MB | CC-BY-4.0 + metadata |
| `figures/` | 2 | 146 KB | CC-BY-4.0 |
| `data/` | 19 | 2.55 MB | CC-BY-4.0 |
| `reports/` | 6 | 178 KB | CC-BY-4.0 |
| `code/` | 1 | 2.4 KB | MIT |
| `fleets/` | 4 | 233 KB | MIT |

See `zenodo_filelist.txt` for the per-file checklist and licence
assignments.

---

## Verification (all six checks pass)

| # | Check | Result |
|---|---|---|
| 1 | Abstract ≤ 220 non-math words | **OK** (195 words) |
| 2 | Title matches manuscript `\title{...}` exactly | **OK** |
| 3 | ORCID `0009-0000-6192-8273` matches CITATION.cff and manuscript | **OK** |
| 4 | GitHub repo URL present in disclosure section of `manuscript.tex` | **OK** (line 2044) |
| 5 | `LICENSE-CODE` (MIT) and `LICENSE-TEXT` (CC-BY-4.0) both present in bundle | **OK** |
| 6 | All 44 expected file paths exist in `wkb-newton-polygons-zenodo-v2.0.zip` | **OK** (0 missing, 0 extra) |

---

## After Zenodo assigns the DOI

Run `publication_pipeline/doi_propagation_commands.sh` (it already
exists from the v2.0 publication pipeline) to substitute the real DOI
into:

- `paper/paper.tex` and the three bundle copies (in the
  `\bibitem{wkb_dataset_v1}` placeholder line and the
  `\texttt{10.5281/zenodo.XXXXXXX}` line)
- `paper/references.bib`
- `CITATION.cff`
- `README.md`
- `publication_pipeline/zenodo_metadata_v2.0.txt`
- `publication_pipeline/zenodo_v2_metadata/zenodo_metadata_ready.json`
- `publication_pipeline/zenodo_v2_metadata/zenodo_metadata_ready.txt`

Then recompile (`pdflatex → bibtex → pdflatex × 2`) and push to GitHub
to keep the public mirror in sync.

If arXiv assigns its identifier first or later, do the same with the
`arXiv:XXXX.XXXXX` placeholder.

---

## Caveats / open items

1. **Email** is intentionally not embedded in any deliverable. Add it
   in the Zenodo web form if desired.
2. **Communities.** `math-ph` is widely used; `exact-wkb`,
   `stokes-phenomena`, and `reproducible-research` are aspirational
   identifiers — verify each one exists on Zenodo's community catalogue
   (`https://zenodo.org/communities/`) before uploading; remove any
   that don't.
3. **arXiv placeholder.** `isSupplementTo: arXiv:XXXX.XXXXX` is a
   deliberate placeholder. Update it the moment arXiv assigns an
   identifier; the DOI-propagation script handles the substitution.
4. **The companion Zenodo zip was rebuilt this session** to include the
   URL-corrected manuscript (898,187 B vs the previous 897,105 B);
   the pre-rebuild zip is gone. The contents of
   `publication_pipeline/zenodo_v2_package/` remain the source of truth
   and were the input to the rebuild.
