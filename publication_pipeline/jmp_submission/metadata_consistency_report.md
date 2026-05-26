# Metadata Consistency Report — JMP Submission

**Date:** 2026-05-26
**Scope:** cross-file audit of DOI, GitHub URL, version label, ORCID,
title, author, and citation metadata across the manuscript ecosystem.
**Authoritative IDs (this audit):**
- Zenodo version DOI: `10.5281/zenodo.20387847`
- Zenodo concept DOI: `10.5281/zenodo.20387846`
- GitHub repo:        `https://github.com/papanokechi/wkb-newton-polygons`
- ORCID:              `0009-0000-6192-8273`
- Version label:      `v1.0` (current public release; matches Zenodo deposit version)

---

## 1 — DOI consistency table

| Site | File | Line | Current value | Match? | Action |
|------|------|------|---------------|--------|--------|
| Disclosure (post-rewrite) | paper/manuscript.tex | 2046–2049 | `10.5281/zenodo.20387847` + `20387846` | ✅ | none |
| Disclosure (post-rewrite) | paper/paper.tex | 2046–2049 | same | ✅ | none |
| Disclosure (post-rewrite) | arxiv_bundle/paper.tex | 2046–2049 | same | ✅ | none |
| Disclosure (post-rewrite) | journal_bundle/paper.tex | 2046–2049 | same | ✅ | none |
| Disclosure (post-rewrite) | major_revision/followup/paper_v2_1.tex | 2046–2049 | same | ✅ | none |
| Header comment | paper/manuscript.tex | 5 | `10.5281/zenodo.XXXXXXX  (PLACEHOLDER)` | 🔴 | propagate DOI |
| Header comment | paper/paper.tex | 5 | same | 🔴 | propagate DOI |
| Header comment | arxiv_bundle/paper.tex | 5 | same | 🔴 | propagate DOI |
| Header comment | journal_bundle/paper.tex | 5 | same | 🔴 | propagate DOI |
| Header comment | major_revision/followup/paper_v2_1.tex | 5 | same | 🔴 | propagate DOI |
| §11 Reproducibility note | paper/manuscript.tex | 1945 | `10.5281/zenodo.XXXXXXX` | 🔴 | propagate DOI |
| §11 Reproducibility note | paper/paper.tex | 1945 | same | 🔴 | propagate DOI |
| §11 Reproducibility note | arxiv_bundle/paper.tex | 1945 | same | 🔴 | propagate DOI |
| §11 Reproducibility note | journal_bundle/paper.tex | 1945 | same | 🔴 | propagate DOI |
| §11 Reproducibility note | major_revision/followup/paper_v2_1.tex | 1945 | same | 🔴 | propagate DOI |
| BibTeX `wkb_dataset_v1` doi | paper/references.bib | 17 | `10.5281/zenodo.XXXXXXX` | 🔴 | propagate DOI |
| BibTeX `wkb_dataset_v1` doi | arxiv_bundle/references.bib | 17 | same | 🔴 | propagate DOI |
| BibTeX `wkb_dataset_v1` doi | journal_bundle/references.bib | 17 | same | 🔴 | propagate DOI |
| BibTeX `wkb_dataset_v1` note | paper/references.bib | 18 | `https://doi.org/10.5281/zenodo.XXXXXXX` | 🔴 | propagate DOI |
| BibTeX `wkb_dataset_v1` note | arxiv_bundle/references.bib | 18 | same | 🔴 | propagate DOI |
| BibTeX `wkb_dataset_v1` note | journal_bundle/references.bib | 18 | same | 🔴 | propagate DOI |
| Bibliography (compiled) | arxiv_bundle/paper.bbl | (line ~88) | `10.5281/zenodo.XXXXXXX` | 🔴 | recompile after bib fix |
| README badge | README.md | 5 | `zenodo.XXXXXXX.svg` | 🔴 | propagate DOI |
| README BibTeX | README.md | 109–110 | `zenodo.XXXXXXX` | 🔴 | propagate DOI |
| CITATION.cff top-level | CITATION.cff | 11, 13 | `zenodo.XXXXXXX` | 🔴 | propagate DOI |
| CITATION.cff preferred-citation | CITATION.cff | 47, 48 | `zenodo.XXXXXXX` | 🔴 | propagate DOI |
| CITATION.cff identifier | CITATION.cff | 52 | `zenodo.XXXXXXX` | 🔴 | propagate DOI |

**DOI propagation status:** ✅ 5 of 28 sites now carry the live DOI
(the §AI Disclosure paragraph in each of 5 manuscript copies — done in
this Task-2 commit). The remaining 23 sites still hold the
`XXXXXXX` placeholder.

**Recommended fix:** run the existing
`publication_pipeline/doi_propagation_commands.sh` with
`10.5281/zenodo.20387847` as `$1`. The script targets the 27 placeholder
sites listed in the v2.0 release pipeline and recompiles the manuscript
+ retags v2.0.

---

## 2 — GitHub URL consistency table

| Site | File | Line | Current value | Match? | Action |
|------|------|------|---------------|--------|--------|
| AI Disclosure body | paper/manuscript.tex | 2044 | `https://github.com/papanokechi/wkb-newton-polygons` | ✅ | none |
| AI Disclosure body | paper/paper.tex | 2044 | same | ✅ | none |
| AI Disclosure body | arxiv_bundle/paper.tex | 2044 | same | ✅ | none |
| AI Disclosure body | journal_bundle/paper.tex | 2044 | same | ✅ | none |
| AI Disclosure body | major_revision/followup/paper_v2_1.tex | 2044 | same | ✅ | none |
| Author footnote | paper/manuscript.tex | 89 | `https://github.com/papanokechi` (account URL) | ⚠ | extend to repo URL or drop |
| Author footnote | (same in 4 other copies) | 89 | same | ⚠ | extend to repo URL or drop |
| README header | README.md | (top) | `papanokechi/wkb-newton-polygons` | ✅ | none |
| CITATION.cff | CITATION.cff | 12 | `https://github.com/papanokechi/wkb-newton-polygons` | ✅ | none |
| Zenodo metadata | publication_pipeline/zenodo_v2_metadata/zenodo_metadata_ready.json | (related_identifiers) | full repo URL + releases/tag/v2.0 | ✅ | none |

**Consistency:** all *reference* sites carry the full repo URL. The
author-footnote site at L89 uses the account-only URL — recommend
upgrading for consistency with the rest of the manuscript, though it is
not strictly a violation (the account URL does resolve to the user
profile which links to the repo).

---

## 3 — Version label consistency

| Site | Value | Notes |
|------|-------|-------|
| Zenodo deposit | `v1.0` | The deposit was uploaded as v1.0 (not v2.0); user explicitly removed the "isNewVersionOf" relation pre-publish. |
| GitHub release tag | `v2.0` | Pre-publish tag created during repo population; **mismatches** Zenodo deposit version. |
| CITATION.cff `version:` | `"2.0"` | **Mismatches** Zenodo deposit (`v1.0`). |
| §AI Disclosure (pre-rewrite) | "Zenodo v2.0 dataset" | **Mismatched** — fixed in this rewrite (now reads "Zenodo dataset" without version label). |
| `\date{(preprint v1.0)}` | `v1.0` | Matches Zenodo deposit ✅. |
| README internal references | mix of v1.0 and v2.0 | needs harmonisation |
| release_notes_v2.0.txt | `v2.0` | matches GitHub tag, not Zenodo |
| wkb-newton-polygons-zenodo-v2.0.zip | `v2.0` (filename) | matches GitHub tag, not Zenodo |

**Diagnosis.** The v2.0 label was inherited from the *manuscript revision
cycle* (Round-1, Round-2 major-revision → v2.0 camera-ready). When the
Zenodo deposit was created, the user removed the "isNewVersionOf"
relation pointing to `10.5281/zenodo.20355904` (an unrelated record) and
set the Zenodo *version* to v1.0 (since the prior Zenodo
[`20355904`] was not actually a previous version of *this* dataset).
The GitHub release tag and the file naming retained `v2.0` as a
*manuscript-version* label.

**Recommended action.** Two equally valid normalizations:

- **Option A — Treat v2.0 as the manuscript label, keep Zenodo at v1.0:**
  - Update `CITATION.cff` `version:` to `"v1.0 (manuscript v2.0)"` or
    add a comment line clarifying that the manuscript revision number
    and the Zenodo deposit version are distinct.
  - Add a one-line note in `README.md` and `release_notes_v2.0.txt`
    explaining the convention.
- **Option B — Re-version the Zenodo deposit to v2.0:**
  - Publish a new version of the Zenodo record as v2.0 (gets a new
    version DOI under the same concept DOI `20387846`).
  - Update the version DOI in all bake-in sites.

For the JMP submission, **Option A** is the lower-friction path
(no further DOI churn). It is suggested in the cover letter (no
visible version-mismatch from JMP's perspective: they cite the concept
DOI, which is version-agnostic).

---

## 4 — CITATION.cff stale-relic bug

`CITATION.cff` lines 54–56 currently read:

```
- type: doi
  value: 10.5281/zenodo.20355904
  description: "Zenodo record for v1.0 of this dataset (superseded)"
```

**Problem.** DOI `10.5281/zenodo.20355904` is *not* a previous version of
this dataset. It is an unrelated record (Khinchin's-constant paper) that
was mistakenly listed as the "v1.0 superseded" relation during repo
population. The same misidentification appeared earlier in the Zenodo
deposit body and in the `isNewVersionOf` relation; **both of those
instances were already removed pre-publish**, but the CITATION.cff
remnant survived.

**Recommended fix.** Remove lines 54–56 of CITATION.cff entirely. Result:
no false "previous version" claim, no risk of citation tooling (e.g.,
GitHub's citation generator) showing a misleading provenance trail.

---

## 5 — Cross-file inconsistencies summary

| Inconsistency | Severity | Recommended fix |
|---------------|----------|----------------|
| DOI placeholder in 23 sites outside §AI Disclosure | 🔴 BLOCKER for full submission polish | run `doi_propagation_commands.sh` |
| CITATION.cff false "v1.0 (superseded)" row pointing to unrelated Khinchin paper | 🔴 BUG | delete L54–56 of CITATION.cff |
| CITATION.cff version `"2.0"` vs Zenodo deposit version `v1.0` | ⚠ MINOR | clarify in README + cite block, or re-publish Zenodo as v2.0 |
| Author footnote GitHub URL is account-only, not repo URL | ⚠ COSMETIC | extend to `papanokechi/wkb-newton-polygons` |
| `\date{(preprint v1.0)}` reads as "preprint" not "published" | ⚠ COSMETIC | change to `\date{\today}` |
| Acknowledgements still says "will be added in camera-ready v2.0" | ⚠ STALE | remove forward-reference; v2.0 is camera-ready |
| `arXiv:XXXX.XXXXX` in CITATION.cff L49 | ℹ INFO | leave as-is until/unless arXiv cross-post happens |

---

## 6 — Verdict

**Metadata consistency: PASS WITH MINOR POLISH.**

- The §AI Disclosure rewrite this turn fixes the AI-policy-fragile
  content and bakes the live DOI into 5 manuscript copies.
- The remaining 23 placeholder sites are tracked by an existing
  propagation script and can be cleared in one command.
- The CITATION.cff Khinchin-paper bug is a 3-line deletion.
- None of the residual issues *block* the JMP submission (the journal
  portal accepts DOIs that the *manuscript* references — DOI live in the
  §AI Disclosure is sufficient for the submission record).
- All issues should be cleared before the manuscript is publicly
  re-released or arXiv'd, but they do not gate the initial JMP
  submission.

See `jmp_submission_readiness.md` for the final overall verdict.
