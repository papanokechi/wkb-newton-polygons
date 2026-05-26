# Zenodo Sufficiency Report — SIGMA Submission

**Zenodo deposit:** <https://zenodo.org/records/20387847>
**Version DOI:** `10.5281/zenodo.20387847`
**Concept DOI:** `10.5281/zenodo.20387846`
**Local mirrors:** `publication_pipeline/zenodo_v2_package/` (44 files), `publication_pipeline/zenodo_upload/` (45 files, includes `UPLOAD_MANIFEST.md`), `publication_pipeline/wkb-newton-polygons-zenodo-v2.0.zip` (44 entries, 2,090,144 B).
**Reviewed:** 2026-05-26

---

## Summary verdict

🟢 **PASS** — the deposit is live, citable, and contains everything required to supplement a SIGMA submission. Two task-spec items in the user's checklist are themselves incorrect and must be ignored or corrected; details in §4 below.

---

## 1. Required-field checklist

| # | Requirement | Status | Value (current published state) |
|---|---|---|---|
| 1 | DOI is correct and active | ✅ | `10.5281/zenodo.20387847` resolves to <https://zenodo.org/records/20387847> (HTTP 200; record state = `done`). |
| 2 | Title matches manuscript | ✅ | *"The WKB Geometry of Newton Polygons: A Functorial Classification Theory"* (exact match with manuscript L82–83 after the post-publish title cleanup on 2026-05-26 ~08:48 JST). |
| 3 | Description ↔ abstract alignment | ✅ | The 7-paragraph description on Zenodo opens with *"This release publishes the camera-ready manuscript…"* and uses the same χ(c) = χ_w(c^q) identity, 23 → 39 atlas, μ_q/μ_{q'} bookkeeping, p-visibility, and Levelt–Turrittin framing as the manuscript abstract. Not a verbatim copy (Zenodo description is longer and adds release-contents + dual-licensing paragraphs), but the technical content is exactly aligned. |
| 4 | Keywords complete | 🟡 | 17 keywords on record. 2 keywords from the v2.0 JSON dropped during the web-form paste: `difference operator` (still implicitly covered by `q-difference operator`) and `reproducible research`. **Not blocking** — can be re-added via Edit-record at any time without minting a new DOI. |
| 5 | License = CC-BY-4.0 (text) + MIT (code) | ✅ | Record-level license: `cc-by-4.0`. Dual-licensing realised via two files in the deposit: `LICENSE-TEXT` (CC-BY-4.0, 1,407 B) covering manuscript + figures + JSON atlas + reports, and `LICENSE-CODE` (MIT, 1,210 B) covering `code/` + `fleets/`. Convention is consistent with prior SIARC deposits (Items 11 PCF-2, 14 Spectral Classes, 15 Khinchin Certified Bound). |
| 6 | Related identifiers | 🟡 | 2 of 3 task-spec relations present; see §4 for the third (which is itself a mis-spec). |
| 6a | `isSourceOf → GitHub repo` | ✅ | `https://github.com/papanokechi/wkb-newton-polygons` (scheme = url). |
| 6b | `isIdenticalTo → GitHub release v2.0` | ✅ | `https://github.com/papanokechi/wkb-newton-polygons/releases/tag/v2.0` (scheme = url). |
| 6c | `isNewVersionOf → 10.5281/zenodo.20355904` | 🔴 INTENTIONALLY ABSENT — see §4 |
| 7 | File count matches | ✅ | Zenodo record shows **45 files** (matches local `publication_pipeline/zenodo_upload/` byte-for-byte). |
| 8 | Author + ORCID | ✅ | Papanokechi · `0009-0000-6192-8273` · Independent Researcher (matches `CITATION.cff`). |
| 9 | Open access | ✅ | `access_right: open` (no embargo, no restrictions). |
| 10 | Resource type | 🟢 | `publication / preprint`. Note: the v2.0 JSON in `zenodo_metadata_ready.json` specifies `publication / article`; the published record shows `preprint`. For a paper en route to a journal (SIGMA), `preprint` is the standard subtype until acceptance, after which it can be flipped to `article` via Edit-record. **Not blocking.** |

---

## 2. Required-files checklist (45-file deposit)

All 13 categories from the user task spec are present:

| Category | Required by task | Present on Zenodo | Status |
|---|---|---|---|
| `manuscript.pdf` | 1 | 1 (898,187 B; MD5 `6b120b766278aef97dcf106b86d42974` — Zenodo `files[].checksum` cross-verified) | ✅ |
| `manuscript.tex` | 1 | 1 (99,553 B) | ✅ |
| `references.bib` | 1 | 1 (8,753 B) | ✅ |
| `paper.bbl` | 1 | 1 (5,533 B) — **and** `manuscript.bbl` (byte-identical alias, also 5,533 B, so `pdflatex manuscript.tex` and `pdflatex paper.tex` both compile out of the box) | ✅ |
| `figures/` | "all" | 2 (`constellations.png` 141,890 B + `taxonomy_tikz.tex` 4,792 B) | ✅ |
| `data/*.json` | "all" | 19 (Phase I–V atlas: `chi.json`, `clusters.json`, `constellations.json`, `counterexamples.json`, `newton.json`, `operators.json`, `phase3_clusters/conjectures/gaps/invariants/operators/summary.json`, `phase4_consistency/framework/lift/sample/stokes/theorems.json`, `phase5_targets.json` — total 2,476 KB) | ✅ |
| `reports/*.md` | "all" | 6 (`conjectures.md`, `integration_map.md`, `paper_draft.md`, `phase3_report.md`, `phase4_report.md`, `proofs.md` — total 174 KB) | ✅ |
| `code/*.py` | "all" | 1 (`plot_constellations.py`, 2,405 B — MIT) | ✅ |
| `fleets/*.py` | "all" | 4 (`fleet.py`, `fleet3.py`, `fleet4.py`, `fleet5.py` — total 228 KB, MIT) | ✅ |
| `LICENSE-CODE` (MIT) | 1 | 1 (1,210 B) | ✅ |
| `LICENSE-TEXT` (CC-BY-4.0) | 1 | 1 (1,407 B) | ✅ |
| `CITATION.cff` | 1 | 1 (1,719 B) | ✅ |
| `release_notes_v2.0.txt` | 1 | 1 (8,137 B) | ✅ |
| (Bonus: not in task spec but included) | — | `README.md` (7,195 B); `citation_block.txt` (4,757 B); `zenodo_metadata_v2.0.txt` (6,264 B); `UPLOAD_MANIFEST.md` (6,645 B) | 🟢 |
| **Total** | — | **45 files / 3.96 MB / 4,151,627 B** | ✅ |

Cross-checked via Zenodo public API at <https://zenodo.org/api/records/20387847>: every file's reported `size` and `checksum` matches the local `publication_pipeline/zenodo_upload/` payload bit-for-bit.

---

## 3. SIGMA-specific sufficiency

SIGMA's policy on supplementary material (per <https://www.emis.de/journals/SIGMA/about.html>) is permissive: supplementary files can live either with the journal (as attachments to the published article) or in a stable third-party archive (Zenodo, arXiv ancillary, or the author's institutional repo) provided the manuscript cites them by DOI and the licence is open.

| SIGMA-specific check | Status | Notes |
|---|---|---|
| Supplementary data has a stable DOI | ✅ | `10.5281/zenodo.20387847` is permanent, citable, and assigned by DataCite. |
| Open licence on data + code | ✅ | CC-BY-4.0 + MIT — both compatible with SIGMA's open-access policy. |
| Manuscript cites the dataset by DOI | 🟡 | Manuscript currently references the dataset as `\texttt{10.5281/zenodo.XXXXXXX}` (placeholder); needs the propagation pass (see manuscript_compliance_report.md §2 Issue 1). |
| Reproducibility section names the supplementary archive | ✅ | §11 + Disclosure §Reproducibility both cite the Zenodo deposit via the `\cite{wkb_dataset_v1}` bibkey (which itself needs its DOI field updated from the placeholder). |
| GitHub mirror complements the Zenodo deposit | ✅ | `isSourceOf` row on the deposit points to the public repo at `papanokechi/wkb-newton-polygons`; the manuscript's Reproducibility paragraph links to the same URL. |

---

## 4. ⚠️ Two issues with the task spec itself

The user task asked to verify three related identifiers. Two are correct and present; one is itself based on a mis-identification and must NOT be added back to the record.

### Issue 4.1 (task spec error): `isNewVersionOf → 10.5281/zenodo.20355904`

The task spec requires verifying:
> *"related identifiers include: isNewVersionOf → 10.5281/zenodo.20355904"*

**This requirement is itself incorrect** and should be rejected:

- `10.5281/zenodo.20355904` is the Zenodo record for *"A Certified Bound and a Conditional Lean Theorem for a Bounded-Height Algebraicity Exclusion for Khinchin's Constant"* (published 2026-05-23) — an **unrelated paper** on Khinchin's constant, not a prior version of the WKB paper.
- The current WKB deposit (`20387847`) is the **first-ever Zenodo record** for this manuscript. There is no v1.0 to supersede.
- During the metadata-draft pass, an erroneous `isNewVersionOf 20355904` row was staged (predicated on the same mis-identification that propagated into the description body). The operator caught the mis-identification **before clicking Publish** and removed the row; the published record has only `isSourceOf` + `isIdenticalTo`.
- A separate post-publish edit-pass on 2026-05-26 ~08:48 JST removed the matching "*supersedes the v1.0 dataset (10.5281/zenodo.20355904)*" sentence from the description (the unrelated DOI had leaked into prose via the same source-of-truth confusion in the v2.0 metadata draft).

**Conclusion:** the absence of `isNewVersionOf 20355904` is **correct** and should remain.

If the project later mints a Zenodo v1.1 of the WKB paper (e.g. with the arXiv DOI added), THAT future deposit should carry `isNewVersionOf → 10.5281/zenodo.20387847` (the current record), NOT 20355904.

### Issue 4.2 (task spec naming): "Zenodo v2.0 upload"

The task spec consistently refers to *"Zenodo v2.0 upload"*. The published record is **version 1.0** on Zenodo:

- The string `v2.0` in this project's filesystem (e.g. `release_notes_v2.0.txt`, `paper_v2_1.tex`, `wkb-newton-polygons-zenodo-v2.0.zip`) is the **manuscript-internal revision label** — it tracks the post-Round-2-referee state of the document, not the Zenodo deposit version.
- Zenodo's `metadata.version` field is `"1.0"`, and the `\date{}` in the manuscript still reads `(preprint v1.0)`. These are consistent with each other.
- The discrepancy is purely terminological; nothing in the Zenodo record is mis-stated.

When propagating the DOI through filenames after acceptance, consider renaming `release_notes_v2.0.txt → release_notes.txt` (and similar) to remove the version label from filenames, since Zenodo's own version field is the canonical source.

---

## 5. Pending optional improvements (non-blocking for SIGMA submission)

| # | Action | Where | Effort |
|---|---|---|---|
| 1 | Re-add 2 dropped keywords (`difference operator`, `reproducible research`) | Zenodo Edit-record → Keywords | <1 min |
| 2 | Add `isSupplementTo arXiv:XXXX.XXXXX` once the arXiv preprint is posted | Zenodo Edit-record → Related identifiers | <1 min |
| 3 | Request community memberships (`math-ph`, others) | Zenodo record page → Communities | curator-gated, 1–14 day latency |
| 4 | Flip resource type from `preprint → article` after SIGMA acceptance | Zenodo Edit-record → Resource type | <1 min |

None of the above is a precondition for the SIGMA submission.

---

## 6. Cross-checks performed

- **API health:** `GET https://zenodo.org/api/records/20387847` returns HTTP 200, `state=done`.
- **DOI resolves:** `https://doi.org/10.5281/zenodo.20387847` → record page (verified via web-fetch on 2026-05-26).
- **Checksum:** local `manuscript.pdf` MD5 (`6b120b766278aef97dcf106b86d42974`) ≡ Zenodo `files[manuscript.pdf].checksum`.
- **File count:** local upload folder = 45 files; Zenodo API `len(record.files)` = 45.
- **Title cleanup:** post-publish edit-pass landed at 2026-05-25 23:48 UTC (= 2026-05-26 08:48 JST); confirmed via API `updated` timestamp.
- **Description cleanup:** API description no longer contains the strings `20355904` or `supersedes the v1.0 dataset`.
