# Submission Summary — SIGMA

**Project:** WKB Geometry of Newton Polygons — A Functorial Classification Theory
**Submission compiled:** 2026-05-26

---

## A. Submission tracking

| Identifier | Value | Status |
|---|---|:---:|
| Zenodo DOI (version) | `10.5281/zenodo.20387847` | ✅ Active |
| Zenodo DOI (concept) | `10.5281/zenodo.20387846` | ✅ Active |
| GitHub repository | <https://github.com/papanokechi/wkb-newton-polygons> | ✅ Public |
| GitHub release | <https://github.com/papanokechi/wkb-newton-polygons/releases/tag/v2.0> | ✅ Tagged |
| arXiv preprint ID | *(PLACEHOLDER — to be assigned)* | ⏳ Pending |
| SIGMA assignment number | *(PLACEHOLDER — to be assigned by SIGMA on submission)* | ⏳ Pending |
| Submission date | *(PLACEHOLDER — set at portal-submit time)* | ⏳ Pending |

---

## B. Persistent links

| Resource | URL |
|---|---|
| Zenodo record page | <https://zenodo.org/records/20387847> |
| Zenodo DOI resolver | <https://doi.org/10.5281/zenodo.20387847> |
| GitHub repo | <https://github.com/papanokechi/wkb-newton-polygons> |
| GitHub release v2.0 | <https://github.com/papanokechi/wkb-newton-polygons/releases/tag/v2.0> |
| arXiv (when assigned) | `https://arxiv.org/abs/[ARXIV ID]` |

---

## C. Key cross-citations

Each of the following identifiers must be present in the manuscript front-matter / body before SIGMA submission. Use this table to verify post-edit consistency.

| # | Identifier | Present in manuscript? | Site |
|---|---|:---:|---|
| 1 | Zenodo DOI `10.5281/zenodo.20387847` | 🟡 placeholder | L5, L1945, L2047 of `paper_v2_1.tex` |
| 2 | GitHub repo `https://github.com/papanokechi/wkb-newton-polygons` | ✅ | L2043–2044 of `paper_v2_1.tex` |
| 3 | Author ORCID `0009-0000-6192-8273` | ✅ | L87 of `paper_v2_1.tex` |
| 4 | Author email | 🔴 missing | (add to `\thanks{...}` at L86) |
| 5 | Postal affiliation | 🔴 missing | (add to `\thanks{...}` at L86) |
| 6 | MSC2020 codes | ✅ | L143 |
| 7 | Keywords (10) | ✅ | L137–140 |
| 8 | Abstract (175 alpha-words) | ✅ | L101–134 |
| 9 | arXiv ID | ⏳ pending | (add to front-matter after arXiv assignment) |

---

## D. Per-section readiness verdicts

| Report | Verdict |
|---|---|
| `sigma_manuscript_compliance.md` | 🟡 PASS WITH MINOR POLISH (3 categories of small edits) |
| `sigma_zenodo_sufficiency.md` | 🟢 PASS (record live, 45 files, MD5 cross-verified) |
| `sigma_arxiv_readiness.md` | 🟡 PASS WITH MINOR POLISH (DOI propagation needed) |

**Consolidated verdict** *(in `sigma_submission_readiness_final.md`)*: 🟡 **PASS WITH MINOR POLISH** — ≈ 30–45 minutes of mechanical edits to ready-to-submit state.

---

## E. Submission flow

```
                  ┌─────────────────────────────────────────┐
                  │  (a) Propagate live DOI                 │
                  │     bash doi_propagation_commands.sh    │
                  │     10.5281/zenodo.20387847             │
                  └─────────────────┬───────────────────────┘
                                    ▼
                  ┌─────────────────────────────────────────┐
                  │  (b) Add email + postal affiliation     │
                  │     Edit \thanks{...} at L85–90         │
                  └─────────────────┬───────────────────────┘
                                    ▼
                  ┌─────────────────────────────────────────┐
                  │  (c) Clean stale v1.0/v2.0 labels       │
                  │     Edit L92, L1946, L2045, L2062       │
                  └─────────────────┬───────────────────────┘
                                    ▼
                  ┌─────────────────────────────────────────┐
                  │  (d) 4-pass recompile                   │
                  │     pdflatex → bibtex → pdflatex (×2)  │
                  │     Verify 26 pp, 0 errors              │
                  └─────────────────┬───────────────────────┘
                                    ▼
                  ┌─────────────────────────────────────────┐
                  │  (e) Customise + render cover letter    │
                  │     submission_cover_letter.md → .pdf   │
                  └─────────────────┬───────────────────────┘
                                    ▼
                  ┌─────────────────────────────────────────┐
                  │  (f) Optional: post arXiv preprint      │
                  │     tar czf arxiv-submission.tgz        │
                  │     Upload to arXiv math-ph             │
                  │     Back-propagate arXiv ID             │
                  └─────────────────┬───────────────────────┘
                                    ▼
                  ┌─────────────────────────────────────────┐
                  │  (g) Submit via SIGMA portal            │
                  │     Upload 7 files (see filelist.md)    │
                  │     Cite Zenodo DOI in cover letter     │
                  └─────────────────┬───────────────────────┘
                                    ▼
                  ┌─────────────────────────────────────────┐
                  │  (h) Log in SIARC ledger                │
                  │     submission_log.txt §1 Active        │
                  │     Trigger _build_submission_html.py   │
                  └─────────────────────────────────────────┘
```

---

## F. Companion files in this folder

| File | Purpose |
|---|---|
| `sigma_manuscript_compliance.md` | Field-by-field manuscript audit |
| `sigma_zenodo_sufficiency.md` | Supplementary-archive audit |
| `sigma_arxiv_readiness.md` | arXiv bundle audit |
| `submission_cover_letter.md` | 1-page cover letter template + customisation notes |
| `submission_metadata_block.md` | Title / abstract / MSC / keywords / ORCID / DOI — paste-ready |
| `submission_filelist.md` | What to upload through the portal |
| **`submission_summary.md`** | *(this file)* — at-a-glance submission tracking |
| `sigma_submission_readiness_final.md` | Final consolidated verdict |

— *End of summary.*
