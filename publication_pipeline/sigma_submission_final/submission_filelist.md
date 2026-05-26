# Submission File List — SIGMA

**Purpose:** what to upload through the SIGMA submission portal.
**SIGMA portal:** <https://www.emis.de/journals/SIGMA/submit.html>

---

## A. Required files (upload through portal)

| Slot | File | Source | Size | Notes |
|---|---|---|---:|---|
| 1 | `manuscript.pdf` | `paper/manuscript.pdf` | 898,187 B | 26 pp, camera-ready PDF |
| 2 | `manuscript.tex` *(or `paper.tex`)* | `paper/manuscript.tex` | 99,553 B | LaTeX source, standalone, AMS-`article` class |
| 3 | `references.bib` | `paper/references.bib` | 8,753 B | BibTeX database, 24 entries |
| 4 | `paper.bbl` | `paper/paper.bbl` | 5,533 B | Pre-built `alpha`-style bibliography (so SIGMA can skip `bibtex`) |
| 5 | `figures/taxonomy_tikz.tex` | `figures/taxonomy_tikz.tex` | 4,792 B | Figure 1 (TikZ; `\input`-ed into `paper.tex`) |
| 6 | `figures/constellations.png` | `figures/constellations.png` | 141,890 B | Figure 2 (300 DPI raster) |
| 7 | `submission_cover_letter.pdf` | (render `submission_cover_letter.md` to PDF) | ~5 KB | 1-page cover letter; see `submission_cover_letter.md` for template |

**Subtotal — 7 files, ~1.16 MB.** Manuscript + figures + cover letter cover the entire SIGMA portal upload.

---

## B. Supplementary archive (cite by Zenodo DOI; do NOT re-upload)

SIGMA permits supplementary material to be archived externally with a stable DOI. **Do not re-upload** the supplementary zip through the portal — cite the Zenodo DOI in the manuscript and cover letter.

| Description | Reference |
|---|---|
| Full supplementary archive (45 files, 3.96 MB) | <https://zenodo.org/records/20387847> · DOI `10.5281/zenodo.20387847` |
| Local mirror (Zenodo-equivalent layout) | `publication_pipeline/zenodo_upload/` |
| Local zip snapshot | `publication_pipeline/wkb-newton-polygons-zenodo-v2.0.zip` (2,090,144 B; 44 entries; the 45th file `UPLOAD_MANIFEST.md` was added Zenodo-side post-zip) |

The 45-file Zenodo archive includes (all categories already verified — see `sigma_zenodo_sufficiency.md`):

- `manuscript.pdf`, `manuscript.tex`, `references.bib`, `paper.bbl`
- `figures/` (2 files)
- `data/` (19 JSON atlas files, Phase I–V)
- `reports/` (6 markdown reports)
- `code/` (1 Python file, MIT)
- `fleets/` (4 Python pipeline files, MIT)
- `LICENSE-CODE` (MIT)
- `LICENSE-TEXT` (CC-BY-4.0)
- `CITATION.cff`
- `release_notes_v2.0.txt`
- `README.md`
- `citation_block.txt` (bonus)
- `zenodo_metadata_v2.0.txt` (bonus)
- `UPLOAD_MANIFEST.md` (bonus)

---

## C. Pre-upload checklist

Before clicking *Submit* on the SIGMA portal:

| # | Item | Action | Status |
|---|---|---|:---:|
| 1 | Live DOI baked into manuscript | `bash publication_pipeline/doi_propagation_commands.sh 10.5281/zenodo.20387847` | ⏳ |
| 2 | Author email + postal affiliation added to `\author{\thanks{...}}` | Edit L85–90 of all 4 manuscript copies | ⏳ |
| 3 | Stale v1.0/v2.0 version labels cleaned up (4 sites) | See `sigma_manuscript_compliance.md` §B.3 | ⏳ |
| 4 | Acknowledgements finalised (or kept as graceful placeholder) | Edit L2056–L2062 | ⏳ |
| 5 | 4-pass recompile after edits (`pdflatex → bibtex → pdflatex → pdflatex`) | Verify 26 pp, 0 errors, 0 undefined refs/cites | ⏳ |
| 6 | Cover letter customised | Replace `[DATE]`, `[EDITOR NAME]`, `[ARXIV ID]`, `[EMAIL]` in `submission_cover_letter.md`; render to PDF | ⏳ |
| 7 | arXiv preprint posted *(optional but recommended)* | Tar `arxiv_bundle/` → arXiv `math-ph`; record assigned ID | ⏳ |
| 8 | arXiv ID back-propagated *(if Step 7 done)* | Edit manuscript front-matter; Zenodo Edit-record → add `isSupplementTo arXiv:...` | ⏳ |
| 9 | Final manuscript bytes pushed to GitHub | `git commit -m "Pre-SIGMA submission polish" && git push` | ⏳ |
| 10 | Submission logged in SIARC ledger | Add entry to `siarc/submitted/submission_log.txt §1 Active deposits` | ⏳ |

---

## D. Naming convention for portal uploads

SIGMA's portal does not enforce strict filename conventions, but a tidy convention helps the editor:

```
manuscript.pdf                       # primary submission
manuscript.tex                       # source (rename from paper.tex if uploading separately)
references.bib                       # bibliography database
paper.bbl                            # pre-built bibliography
figures/taxonomy_tikz.tex            # Figure 1 source
figures/constellations.png           # Figure 2 raster
cover_letter.pdf                     # cover letter
```

If the SIGMA portal accepts only a single tarball, bundle as:

```sh
tar czf sigma-submission.tgz \
    manuscript.pdf manuscript.tex references.bib paper.bbl \
    figures/taxonomy_tikz.tex figures/constellations.png \
    cover_letter.pdf
```

(Estimated tarball size: ~250 KB.)

---

## E. NOT submitting to SIGMA (intentionally external)

For audit clarity — the following are **not** uploaded through the SIGMA portal because they live in the Zenodo deposit and/or GitHub repo:

- `data/` (atlas JSON)
- `reports/` (Phase III/IV markdown reports)
- `code/`, `fleets/` (Python pipeline)
- `LICENSE-CODE`, `LICENSE-TEXT`
- `CITATION.cff`
- `release_notes_v2.0.txt`
- `README.md`
- `UPLOAD_MANIFEST.md`, `citation_block.txt`, `zenodo_metadata_v2.0.txt`

The manuscript's Reproducibility and Disclosure sections direct readers to the Zenodo DOI for all of the above.

— *End of file list.*
