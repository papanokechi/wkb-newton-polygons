# Zenodo Sufficiency Check — SIGMA Submission

**Zenodo record:** <https://zenodo.org/records/20387847>
**DOI (version):** `10.5281/zenodo.20387847`
**DOI (concept):** `10.5281/zenodo.20387846`
**Local mirrors:** `publication_pipeline/zenodo_upload/` (45 files, byte-identical to record), `publication_pipeline/wkb-newton-polygons-zenodo-v2.0.zip` (44-entry archive; the 45th file, `UPLOAD_MANIFEST.md`, was added directly on the Zenodo side post-zip).
**Reviewed:** 2026-05-26

---

## Section verdict: 🟢 PASS

Record is live, citable, complete, and consistent with the manuscript. No blocking issues for SIGMA submission.

---

## A. Required-files presence table

| Required file | On Zenodo? | Size (B) | Local path |
|---|:---:|---:|---|
| `manuscript.pdf` | ✅ | 898,187 | `paper/manuscript.pdf` |
| `manuscript.tex` | ✅ | 99,553 | `paper/manuscript.tex` |
| `references.bib` | ✅ | 8,753 | `paper/references.bib` |
| `paper.bbl` | ✅ | 5,533 | `paper/paper.bbl` (also `manuscript.bbl` alias, byte-identical) |
| `figures/` | ✅ | — | 2 files: `constellations.png` (141,890 B) + `taxonomy_tikz.tex` (4,792 B) |
| `data/*.json` | ✅ | — | 19 atlas files (Phase I–V), 2,476 KB total |
| `reports/*.md` | ✅ | — | 6 markdown reports (`conjectures.md`, `integration_map.md`, `paper_draft.md`, `phase3_report.md`, `phase4_report.md`, `proofs.md`), 174 KB total |
| `code/*.py` | ✅ | 2,405 | `code/plot_constellations.py` (MIT-licensed) |
| `fleets/*.py` | ✅ | — | 4 fleets (`fleet.py`, `fleet3.py`, `fleet4.py`, `fleet5.py`), 228 KB total |
| `LICENSE-CODE` (MIT) | ✅ | 1,210 | `LICENSE-CODE` |
| `LICENSE-TEXT` (CC-BY-4.0) | ✅ | 1,407 | `LICENSE-TEXT` |
| `CITATION.cff` | ✅ | 1,719 | `CITATION.cff` |
| `release_notes_v2.0.txt` | ✅ | 8,137 | `release_notes_v2.0.txt` |
| `README.md` | ✅ | 7,195 | `README.md` |

**14 of 14 required categories present.**

Bonus files (in deposit but not on task spec):

| Bonus file | Size (B) | Purpose |
|---|---:|---|
| `citation_block.txt` | 4,757 | Ready-to-paste citation strings (BibTeX + APA + Chicago) |
| `zenodo_metadata_v2.0.txt` | 6,264 | Mirror of the Zenodo metadata block, for offline reference |
| `UPLOAD_MANIFEST.md` | 6,645 | Hand-authored upload manifest (file-by-file) |

Total: **45 files / 3.96 MB / 4,151,627 B** — matches Zenodo API report `len(record.files) = 45`.

---

## B. Metadata sufficiency

| # | Required | Zenodo state | Status |
|---|---|---|:---:|
| 1 | DOI correct and active | `10.5281/zenodo.20387847` → HTTP 200, `state=done` | ✅ |
| 2 | Metadata matches manuscript | Title verbatim ≡ manuscript L82–83; description opens with manuscript-mirrored framing (χ(c) = χ_w(c^q), 23 → 39 atlas, μ_q symmetry, p-visibility, Levelt–Turrittin) | ✅ |
| 3 | Keywords complete | 17 keywords on record (manuscript has 10; deposit is a superset). 2 keywords from the v2.0 JSON dropped during web-form paste: `difference operator` (implied by `q-difference operator`) and `reproducible research`. Non-blocking; can be re-added via Edit-record at any time. | 🟡 |
| 4 | Related identifiers include GitHub repo | `isSourceOf → https://github.com/papanokechi/wkb-newton-polygons` ✅ + `isIdenticalTo → https://github.com/papanokechi/wkb-newton-polygons/releases/tag/v2.0` ✅ | ✅ |
| 5 | License = CC-BY-4.0 (text) | Record-level: `cc-by-4.0`; LICENSE-TEXT file shipped (1,407 B) | ✅ |
| 6 | License = MIT (code) | `LICENSE-CODE` file shipped (1,210 B); `code/` + `fleets/` annotated MIT in `UPLOAD_MANIFEST.md` and `release_notes_v2.0.txt` | ✅ |
| 7 | Author + ORCID match CITATION.cff | Papanokechi · `0009-0000-6192-8273` · Independent Researcher | ✅ |
| 8 | Open access | `access_right: open` (no embargo) | ✅ |
| 9 | Resource type | `publication / preprint` (correct subtype until SIGMA acceptance, flip to `article` post-acceptance) | ✅ |

---

## C. Cross-verifications

| Check | Method | Result |
|---|---|---|
| Record API health | `GET https://zenodo.org/api/records/20387847` | HTTP 200, `state=done` |
| DOI resolves | `https://doi.org/10.5281/zenodo.20387847` | Redirects to record page |
| Manuscript MD5 parity | local `manuscript.pdf` MD5 = `6b120b766278aef97dcf106b86d42974` vs Zenodo API `files[manuscript.pdf].checksum` | Match |
| File count | local `publication_pipeline/zenodo_upload/` = 45 files vs Zenodo API `len(record.files)` | Match (45 = 45) |
| Title cleanup landed | API `metadata.title` | No trailing "(v2.0)" — clean |
| Description cleanup landed | API `metadata.description` | No `20355904`, no "supersedes the v1.0 dataset" |
| Post-publish edit timestamp | API `updated` | 2026-05-25 23:48:32 UTC = 2026-05-26 08:48 JST |

---

## D. Note on the task-spec phrasing "Zenodo v2.0 record"

The task spec consistently refers to *"Zenodo v2.0 record"*; the deposit's actual `metadata.version` field is `"1.0"`. The string `v2.0` in this project's filesystem (`release_notes_v2.0.txt`, `paper_v2_1.tex`, `wkb-newton-polygons-zenodo-v2.0.zip`) is the **manuscript-internal post-Round-2 revision label**, not the Zenodo version. The two labels are independent; the Zenodo deposit is correctly v1.0 (first record for this paper). No change required.

---

## E. Optional improvements (non-blocking)

| # | Improvement | Where | Effort |
|---|---|---|---|
| 1 | Re-add 2 dropped keywords (`difference operator`, `reproducible research`) | Edit-record → Keywords | <1 min |
| 2 | Add `isSupplementTo arXiv:XXXX.XXXXX` after arXiv post | Edit-record → Related identifiers | <1 min |
| 3 | Request `math-ph` community membership | Record page → Communities | curator latency 1–14 days |
| 4 | Flip resource type `preprint → article` after SIGMA acceptance | Edit-record → Resource type | <1 min |

None is a precondition for SIGMA submission.

---

## F. Audit log

- 2026-05-26 ~03:30 JST — Deposit `20387847` published with title trailing "(v2.0)" + description sentence referencing unrelated DOI `20355904`.
- 2026-05-26 ~04:15 JST — Issues caught by post-publish review (`zenodo_record_review.md`); paste-ready corrected description prepared.
- 2026-05-26 ~08:48 JST — Edit-record applied: title cleaned, description sentence removed. API `updated` timestamp confirms.
- 2026-05-26 ~09:10 JST — Submission-log §3 Item 16 added with DOI, version 1.0, 45-file manifest, MD5 cross-verification (`siarc/submitted/submission_log.txt` L882–L890); HTML rebuilt.
- 2026-05-26 ~09:19 JST — *(this report)*.

— *End of report.*
