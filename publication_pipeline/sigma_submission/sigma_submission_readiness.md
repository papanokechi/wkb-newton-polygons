# SIGMA Submission Readiness — Final Verdict

**Project:** WKB Geometry of Newton Polygons — A Functorial Classification Theory
**Target journal:** SIGMA (Symmetry, Integrability and Geometry: Methods and Applications)
**Reports consulted:**
- `manuscript_compliance_report.md`
- `zenodo_sufficiency_report.md`
- `arxiv_readiness_report.md`
- `sigma_submission_package_summary.md`

**Verdict date:** 2026-05-26

---

## 🟡 Overall verdict: **PASS WITH MINOR POLISH**

The mathematics, the figures, the supplementary archive, the GitHub mirror, the bibliography, the AI disclosure, and the reproducibility section are all submission-ready. Five small touch-ups remain before clicking *Submit* on the SIGMA portal; none requires re-deriving any result, re-running the pipeline, or revising any proof. Total effort estimate: **30–45 minutes**.

---

## Per-report verdict roll-up

| Report | Verdict | Blocking? |
|---|---|---|
| Manuscript compliance | 🟡 PASS WITH MINOR POLISH | No, but should be fixed before submission |
| Zenodo sufficiency | 🟢 PASS | No |
| arXiv readiness | 🟡 PASS WITH MINOR POLISH | No (arXiv submission is itself optional & post-SIGMA-portal) |

---

## ✅ Cleared (no action needed)

- **Manuscript structure:** title, ORCID, abstract (175 alpha-words), MSC2020 (5 codes), 10 keywords, acknowledgements section, references with `alpha`-style `paper.bbl`, AI Disclosure (5 sub-roles), Reproducibility §11, GitHub URL in Disclosure.
- **Math content:** all 8 theorems (M1, N1, D2, S1, AT1, AT3, AT5, AT7) consolidated post-rubber-duck-correction; 11-strata counterexample knowledge base; Phase I–V pipelines deterministic and re-runnable.
- **Build pipeline:** 4-pass compile produces identical 898,187-byte 26-page PDF across `paper/`, `arxiv_bundle/`, `journal_bundle/`, and `major_revision/followup/`. Zero LaTeX errors, zero undefined refs/cites, zero LaTeX warnings.
- **Bundle parity:** all 4 manuscript copies byte-identical (99,553 B). Figures (constellations.png + taxonomy_tikz.tex) ship with each bundle.
- **Zenodo deposit:** 45 files, MD5 cross-verified, DOI `10.5281/zenodo.20387847` live and resolving; CC-BY-4.0 + MIT dual-licensing in place; `isSourceOf` + `isIdenticalTo` relations correct; description aligned with manuscript abstract.
- **Reproducibility:** fleet scripts in repo + Zenodo regenerate the atlas in < 30 s; SHA-stable outputs.
- **Disclosure honesty:** AI tooling identified by name (GitHub Copilot CLI + Anthropic Claude Opus 4.7); five specific roles enumerated; author retains full mathematical accountability.

---

## 🟡 To resolve before submission (BLOCKING for portal acceptance, NOT for results)

### Action 1 — Propagate the live Zenodo DOI (≈ 30 s)

The string `10.5281/zenodo.XXXXXXX` is still a placeholder at **3 sites** in `paper/manuscript.tex` + `arxiv_bundle/paper.tex` + `journal_bundle/paper.tex` + `major_revision/followup/paper_v2_1.tex` (lines 5, 1945, 2047) and inside `references.bib`'s `@misc{wkb_dataset_v1, ...}` entry.

**Run:**

```sh
cd <repo-root>
bash publication_pipeline/doi_propagation_commands.sh 10.5281/zenodo.20387847
```

The script also touches `CITATION.cff`, `README.md`, `submission_checklist.md`, and `zenodo_metadata_v2.0.txt`. It then triggers a 4-pass recompile. Commit + push the result; SIGMA reviewers will see the DOI baked in.

### Action 2 — Add author email + postal affiliation

The current `\author{Papanokechi\thanks{Independent researcher.}}` is missing both a corresponding-author email (SIGMA portal field is required) and a city/country (SIGMA portal field is required).

**Drop-in replacement for L85–90 of all four manuscript copies:**

```latex
\author{%
  Papanokechi\thanks{Independent researcher, Yokohama, Japan.
  Email: \href{mailto:ppapanokechi@gmail.com}{\texttt{ppapanokechi@gmail.com}}.
  ORCID:
  \href{https://orcid.org/0009-0000-6192-8273}{\texttt{0009-0000-6192-8273}}.
  Code and data repository:
  \url{https://github.com/papanokechi/wkb-newton-polygons}.}
}
```

### Action 3 — Refresh stale version labels

Three pieces of prose carry inconsistent "v1.0 vs v2.0" labelling (the Zenodo deposit is v1.0; the project's manuscript internal label is v2.0; both are correct in their own scopes, but the text mixes them):

| Line | Change |
|---|---|
| L92 | Either drop `\hspace{1ex}\textsc{(preprint v1.0)}` from `\date{}`, or change to `\textsc{(post-Round-2 revision)}` |
| L1946 | After DOI propagation, this becomes "*…assigned by Zenodo on publication of v1.0*" → still mismatches with the post-prop literal DOI. Rewrite to *"The dataset DOI is `10.5281/zenodo.20387847` (Zenodo concept `10.5281/zenodo.20387846`)."* (The propagation script already handles inserting the DOI; this is just a one-word "v1.0" → "" cleanup.) |
| L2045 | Replace "*…mirrors the Zenodo v2.0 dataset…*" with "*…mirrors the Zenodo dataset…*" (drop the version qualifier). |
| L2062 | Replace "*…will be added in the camera-ready version (v2.0).*" with "*…will be finalized at the camera-ready stage.*" |

### Action 4 — Finalise the cover letter

Template ships in `sigma_submission_package_summary.md` §Cover letter. Customise `[EDITOR NAME]`, `[DATE]`, and `[EMAIL]`.

### Action 5 (optional but recommended) — Post arXiv first

SIGMA encourages an accompanying arXiv preprint. Post `arxiv_bundle/` to arXiv (`math-ph` primary, `math.CA` + `math.AG` cross-list). After getting the arXiv ID:

1. Update the manuscript: add `arXiv:YYMM.NNNNN` to the front-matter (e.g., as a second `\thanks{}` line on the title, or as a footnote on page 1).
2. Update the Zenodo deposit: Edit-record → add `isSupplementTo arXiv:YYMM.NNNNN` row.
3. Re-tag GitHub release v2.0.1 with the arXiv-ID-baked manuscript.
4. Re-commit and push.

---

## 🟢 Spec issues that the user task should not be relitigated

For audit transparency, the user task spec contained two items that are **themselves incorrect** and were intentionally not enforced in this report. These reflect a confusion in the original task drafting; the current published Zenodo state is the correct one.

| Task spec item | Reality | Resolution |
|---|---|---|
| *"related identifiers include: isNewVersionOf → 10.5281/zenodo.20355904"* | `20355904` is the unrelated Khinchin's-constant paper. The WKB deposit `20387847` is the first-ever Zenodo record for this manuscript and has no prior version to supersede. | **Do NOT add the row.** A separate post-publish edit-pass on 2026-05-26 already removed the matching mis-identification from the description body. |
| *"Zenodo v2.0 upload" / "version = 2.0"* | Zenodo deposit is `version: "1.0"`. The string `v2.0` in this project's filesystem (`release_notes_v2.0.txt`, `paper_v2_1.tex`, `wkb-newton-polygons-zenodo-v2.0.zip`) is the **manuscript-internal post-Round-2 revision label**, not the Zenodo version. | The two scales (manuscript-internal `v2.0` vs Zenodo `1.0`) are independent; they happen to numerically disagree by 1 but each is consistent within its own naming scheme. No change to Zenodo metadata; manuscript prose cleaned up via Action 3 above. |

---

## ⏳ After SIGMA acceptance (deferred actions, NOT required for first submission)

| # | Action |
|---|---|
| 1 | Swap `\documentclass{article}` for `\documentclass{sigma}` from `sigma_v3.cls` (SIGMA house style for camera-ready) |
| 2 | Flip Zenodo resource type from `preprint` → `article` |
| 3 | Finalise acknowledgements (collaborators, funders) |
| 4 | Add the SIGMA publication DOI to `references.bib` (self-cite) and to the GitHub README |
| 5 | Mint Zenodo v1.1 with the SIGMA DOI baked in (`isPublishedIn` → SIGMA DOI; `isNewVersionOf` → `10.5281/zenodo.20387847` — *this* is when the `isNewVersionOf` relation finally becomes correct, but pointing at the current WKB record, not at 20355904) |
| 6 | Re-tag GitHub release v2.1 (post-acceptance) |

---

## Final readiness statement

**The manuscript is mathematically and computationally ready for submission to SIGMA.**

The four blocking touch-ups (DOI propagation, email + affiliation, version-label cleanup, cover letter) are mechanical edits to fewer than 10 lines across the source tree, and a one-line script invocation handles the DOI propagation. Recompile, commit, push, post to arXiv (optional), then submit through the SIGMA portal. Estimated total time from "start touch-ups" to "click Submit": **30–45 minutes** for the manuscript edits + script invocation, plus ~24 hours of arXiv processing latency if Action 5 is included.

— *End of report.*
