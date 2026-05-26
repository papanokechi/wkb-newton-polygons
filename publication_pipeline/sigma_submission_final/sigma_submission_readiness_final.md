# SIGMA Submission Readiness — Final Verdict

**Project:** WKB Geometry of Newton Polygons — A Functorial Classification Theory
**Target journal:** SIGMA — Symmetry, Integrability and Geometry: Methods and Applications
**Reports consulted:** `sigma_manuscript_compliance.md`, `sigma_zenodo_sufficiency.md`, `sigma_arxiv_readiness.md`
**Verdict date:** 2026-05-26

---

## 🟠 Overall verdict: **PASS WITH MINOR POLISH + arXiv ENDORSEMENT GATE**

The manuscript is **mathematically complete**, the **supplementary Zenodo archive is live and citable**, the **arXiv bundle compiles cleanly**, and the **GitHub mirror is published**. Three categories of pre-submission edits remain (~30–45 min), plus one external dependency:

- **arXiv endorsement (3–14 days)** — SIGMA is an arXiv-overlay journal, so posting to arXiv is the canonical submission path. As a first-time `math-ph` submitter with a non-institutional email and a single-author paper, both auto-endorsement paths are closed; a personal endorsement from an established `math-ph` author is required. Backup path: direct email to `editor@sigma-journal.com` with endorsement-blocked justification (SIGMA's exception path, documented in `submission_filelist.md` §E).

Total wall-clock estimate: **3–14 days** (dominated by endorsement latency); **30–45 min** of mechanical work on the author's side.

---

## Per-report verdict roll-up

| Section | Report | Verdict | Blocking? |
|---|---|---|:---:|
| 1 | Manuscript compliance | 🟡 PASS WITH MINOR POLISH | No, but should be fixed before submission |
| 2 | Zenodo sufficiency | 🟢 PASS | No |
| 3 | arXiv readiness | 🟡 PASS WITH MINOR POLISH | No (arXiv is itself optional for SIGMA) |

---

## ✅ What is ready (no action needed)

### Manuscript structure
- Title (matches Zenodo exactly)
- ORCID `0009-0000-6192-8273` (live hyperlink)
- Abstract (175 alpha-words; well under 220 ceiling)
- MSC2020 (5 codes: 34M40 primary; 34M30, 34M35, 39A06, 39A13 secondary)
- 10 keywords
- Acknowledgements section present (body language to finalise; non-blocking)
- AI Disclosure (5 enumerated sub-roles, factual, named tooling)
- Reproducibility §11
- GitHub repo URL in Disclosure (L2043–2044)
- References: 24 entries in `references.bib`; `alpha` style; `paper.bbl` pre-built

### Math content
- 8 main theorems consolidated post-Round-2: M1, N1, D2, S1, AT1, AT3, AT5, AT7
- 11-stratum counterexample knowledge base
- p-visibility formula: 2pq(r + q·C(r,2)) (Theorem AT7)
- 23 → 39 operator atlas (Phases I → III)
- 12-row invariant-lifting table (Phase IV)

### Build pipeline
- 4-pass `pdflatex → bibtex → pdflatex → pdflatex` produces deterministic 898,187-byte PDF
- 26 pages, stable
- 0 errors, 0 undefined refs, 0 undefined cites, 0 LaTeX warnings
- Reproduces across MiKTeX 2024 + TeX Live 2024 + arXiv AutoTeX

### Cross-copy parity
- All 4 manuscript copies byte-identical (99,553 B; same SHA-256)
- `paper/manuscript.pdf` MD5 ≡ Zenodo API checksum for `manuscript.pdf` ≡ `journal_bundle/paper.pdf` ≡ `arxiv_bundle/paper.pdf`

### Zenodo deposit
- DOI `10.5281/zenodo.20387847` live, resolving, `state=done`
- 45 files / 3.96 MB; full categorical coverage
- License: CC-BY-4.0 (record-level) + MIT (LICENSE-CODE for code/fleets) — dual-licensing in place
- Related identifiers: `isSourceOf` GitHub repo ✅ + `isIdenticalTo` GitHub release v2.0 ✅
- Resource type: `preprint` (correct until SIGMA acceptance)
- 17 keywords on record (manuscript has 10; deposit superset is acceptable)
- Post-publish edit (2026-05-26 08:48 JST) cleaned title and description

### Compliance hygiene
- No `\write18` / shell-escape anywhere in 4 manuscript copies + bundles
- No dataset-internal identifiers (operator_id, op_id, phase_id, fleet_run_id) in prose
- No internal filesystem leaks (`siarc/`, `~/.copilot/`, etc.)
- Pure ASCII source; LF line endings; lowercase filenames

---

## 🟡 What needs polish (BLOCKING for portal acceptance, NOT for results)

### Action 1 — Propagate the live Zenodo DOI (≈ 30 seconds)

```sh
cd <repo-root>
bash publication_pipeline/doi_propagation_commands.sh 10.5281/zenodo.20387847
```

Rewrites the 3 `10.5281/zenodo.XXXXXXX` placeholders at L5, L1945, L2047 of all 4 manuscript copies + `references.bib` + `CITATION.cff` + `README.md` + metadata text files. Recompiles. ~46 files touched in one pass.

### Action 2 — Add author email + postal affiliation

Drop-in replacement for L85–90:

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

SIGMA's submission portal requires both fields.

### Action 3 — Refresh stale v1.0/v2.0 version labels (4 sites)

| Line | Change |
|---|---|
| L92 | Drop `\hspace{1ex}\textsc{(preprint v1.0)}` from `\date{}` (or change to `\textsc{(post-Round-2 revision)}`) |
| L1946 | "…assigned by Zenodo on publication of v1.0" → "The dataset DOI is `10.5281/zenodo.20387847` (Zenodo concept `10.5281/zenodo.20387846`)." (DOI propagation handles the literal-DOI part; the "of v1.0" phrase becomes vestigial and should be dropped.) |
| L2045 | "…mirrors the Zenodo v2.0 dataset…" → "…mirrors the Zenodo dataset…" |
| L2062 | "…will be added in the camera-ready version (v2.0)." → "…will be finalized at the camera-ready stage." |

### Action 4 — Finalise cover letter

Template ships in `submission_cover_letter.md`. Replace `[DATE]`, `[EDITOR NAME]`, `[ARXIV ID]`, `[EMAIL]`; render to 1-page PDF.

### Action 5 (REQUIRED for the standard arXiv-overlay path) — Post arXiv preprint

SIGMA is an **arXiv overlay journal**: there is no separate SIGMA web portal. The submission consists of posting to arXiv, then emailing the arXiv ID to `editor@sigma-journal.com`.

**⚠️ Endorsement gate:** As a first-time `math-ph` submitter with a non-institutional email and a single-author paper, both arXiv auto-endorsement paths are closed. The author must obtain a personal endorsement from an established `math-ph` arXiv author.

Endorsement workflow:

1. Start a `math-ph` submission at <https://arxiv.org/submit> → arXiv emails a 6-character endorsement code.
2. Forward the code to 1–3 candidate endorsers — authors of papers cited in `references.bib` (Sabbah / Mochizuki / Hertling / Singer school), or SIGMA editorial-board members active in `math-ph` (e.g., Eric Rains, Bertrand Eynard, Boris Khesin, Alexander Its, Carlos Simpson). Include the Zenodo DOI and GitHub repo URL. Do NOT mass-mail many endorsers simultaneously (arXiv policy discourages this).
3. Once endorsed, complete the arXiv submission. Tar `arxiv_bundle/` with the artefact-stripped 6-file payload (see `sigma_arxiv_readiness.md` §C).
4. After arXiv assigns an ID (typically same-day post-endorsement), back-propagate the arXiv ID into the manuscript front-matter and Zenodo `isSupplementTo` relation. Re-tag GitHub release v2.0.1.

**Timeline:** typically 3–14 days from endorsement request to arXiv ID.

### Action 5b (BACKUP — if endorsement stalls beyond ~2 weeks)

SIGMA accepts direct-email submissions "in exceptional cases" with written justification for not using arXiv. "First-time `math-ph` submitter awaiting endorsement" is a plausible exceptional reason.

Email payload — see `submission_filelist.md` §E for the template, including the suggested explanation paragraph for the cover letter.

---

## ⏳ After SIGMA acceptance (deferred — NOT required for first submission)

| # | Action |
|---|---|
| 1 | Swap `\documentclass{article}` for `\documentclass{sigma}` (`sigma_v3.cls` — SIGMA house style for camera-ready) |
| 2 | Flip Zenodo resource type `preprint` → `article` |
| 3 | Finalise acknowledgements (collaborators, funders) |
| 4 | Add SIGMA publication DOI to `references.bib` (self-cite) and GitHub README |
| 5 | Mint Zenodo v1.1 with SIGMA DOI baked in (`isPublishedIn → SIGMA DOI`; `isNewVersionOf → 10.5281/zenodo.20387847`) |
| 6 | Re-tag GitHub release v2.1 (post-acceptance) |

---

## 📌 Final readiness statement

**The manuscript is mathematically and computationally ready for submission to SIGMA.**

The four blocking author-side touch-ups (DOI propagation, email + affiliation, version-label cleanup, cover letter) are mechanical edits to fewer than 10 lines across the source tree, and a single script invocation handles the DOI propagation. After these:

1. **Recompile** — 4-pass `pdflatex → bibtex → pdflatex → pdflatex` (≈ 30 s)
2. **Commit + push** to GitHub
3. **Open an arXiv endorsement request** by starting a `math-ph` submission → forward the 6-char endorsement code to 1–3 candidate endorsers (see Action 5 above) — **3–14 days**
4. **Post to arXiv** (canonical path) once endorsement is granted, **OR** invoke SIGMA's exception path (`submission_filelist.md` §E) if endorsement stalls
5. **Email SIGMA editorial office** — `editor@sigma-journal.com` with the arXiv ID (or attached manuscript in the exception case)
6. **Log in SIARC ledger** — `submission_log.txt §1 Active deposits`

**Estimated total time from "start touch-ups" to "send email to SIGMA":**
- Author-side mechanical work: 30–45 minutes
- arXiv endorsement wait: 3–14 days (dominant)
- arXiv processing latency after endorsement: ~24 hours
- SIGMA editor acknowledgement: 2 working days per SIGMA's policy

— *End of report.*
