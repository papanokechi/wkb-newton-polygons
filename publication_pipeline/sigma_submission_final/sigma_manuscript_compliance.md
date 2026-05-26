# SIGMA Manuscript Compliance — `paper_v2_1.tex`

**Manuscript file:** `major_revision/followup/paper_v2_1.tex` (99,553 B; byte-identical to `paper/manuscript.tex`, `arxiv_bundle/paper.tex`, `journal_bundle/paper.tex`)
**Companion PDF:** `paper/manuscript.pdf` (898,187 B, 26 pp)
**Target journal:** SIGMA — Symmetry, Integrability and Geometry: Methods and Applications
**Submission guide:** <https://www.emis.de/journals/SIGMA/about.html>
**Reviewed:** 2026-05-26

---

## Section verdict: 🟡 PASS WITH MINOR POLISH

The math, structure, and machine-checkable parts are clean. Three categories of small edits are needed: (1) bake the live DOI into 3 placeholder sites, (2) add author email + postal affiliation, (3) refresh stale v1.0/v2.0 version labels.

---

## A. Field-by-field compliance table

| # | Required field | Status | Line(s) in `paper_v2_1.tex` | Detail |
|---|---|:---:|---:|---|
| 1 | Title | ✅ | 82–83 | *"The WKB Geometry of Newton Polygons: A Functorial Classification Theory"* — matches Zenodo record after the post-publish title-cleanup edit on 2026-05-26 08:48 JST. |
| 2 | Author | ✅ | 85–90 | `Papanokechi` (mononym, canonical). |
| 3 | Affiliation | 🔴 | 86 | Only the textual note *"Independent researcher."* inside `\thanks{...}`. **SIGMA submission portal requires city + country.** Recommended: *"Independent researcher, Yokohama, Japan."* |
| 4 | Email | 🔴 | — | **MISSING.** SIGMA's corresponding-author email field is required. Recommended: `ppapanokechi@gmail.com` (matches GitHub Discussions fallback channel registered in the SIARC pipeline). |
| 5 | ORCID | ✅ | 87 | `0009-0000-6192-8273` (live hyperlink). |
| 6 | Abstract present | ✅ | 101–134 | Self-contained `\begin{abstract}…\end{abstract}` block. |
| 7 | Abstract ≤ 220 words | ✅ | — | **175 alpha-words** (math expressions stripped); 224 raw tokens including math. Well under SIGMA's typical 200–250 ceiling. |
| 8 | MSC2020 codes present | ✅ | 143 | `34M40` (primary); `34M30, 34M35, 39A06, 39A13` (secondary). 5 codes; in scope for SIGMA. |
| 9 | Keywords present | ✅ | 137–140 | 10 keywords (WKB analysis; Newton polygon; irregular singularity; formal classification; Levelt–Turrittin; Stokes phenomenon; anti-Stokes directions; wild character variety; functorial classification; μ_q-pullback). |
| 10 | Acknowledgements section | 🟡 | 2056–2062 | Section present, but body still reads *"Acknowledgements of individual collaborators and funding sources will be added in the camera-ready version (v2.0)."* — placeholder language to finalise. |
| 11 | AI disclosure present + factual | ✅ | 1951–2050 | `\section*{Computational and AI Disclosure}` with 5 paragraphs: Computational environment / Automated pipelines (Phases I–V) / Role of AI assistance (5 sub-roles labeled (i)–(v)) / Human accountability / Reproducibility. Tooling named explicitly (GitHub Copilot CLI + Anthropic Claude Opus 4.7). Factual, non-promotional, attributable. |
| 12 | Reproducibility statement | ✅ | 1914–1946 (§11) + 2036–2050 (in disclosure §Reproducibility) | Dataset directory structure, fleet sequence, deterministic-rebuild guarantee all documented. |
| 13 | Figures render correctly | ✅ | (TikZ + PNG sources) | Figure 1 = `figures/taxonomy_tikz.tex` (4,792 B); Figure 2 = `figures/constellations.png` (141,890 B, 300 DPI). Both shipped in `arxiv_bundle/figures/` and `journal_bundle/figures/`. |
| 14 | References compile cleanly | ✅ | 2068–2069 | `\bibliographystyle{alpha}` + `\bibliography{references}`. 24 entries in `references.bib`; 4-pass `pdflatex → bibtex → pdflatex → pdflatex` produces 0 errors, 0 undefined refs/cites, 0 LaTeX warnings, 2 cosmetic BibTeX warnings (capitalised middle-word in journal title — pre-existing, SIGMA-acceptable). |
| 15 | DOI present (Zenodo dataset) | 🟡 | 5, 1945, 2047 | DOI text appears as **placeholder** `10.5281/zenodo.XXXXXXX` at 3 sites. Live DOI is `10.5281/zenodo.20387847`. Resolution: one-shot `bash publication_pipeline/doi_propagation_commands.sh 10.5281/zenodo.20387847`. |
| 16 | GitHub repo URL present | ✅ | 2043–2044 | *"All code, fleet scripts, and sample artifacts are publicly available at `\url{https://github.com/papanokechi/wkb-newton-polygons}`"* — inserted in Phase 10 (post-Round-2 revision). |
| 17 | No dataset-internal identifiers in prose | ✅ | — | `grep` finds no occurrences of `operator_id`, `op_id`, `phase_id`, `dataset_id`, `fleet_run_id`, or per-item JSON record indices in body text. (Round-1 revision sweep removed all such identifiers.) |
| 18 | No internal filenames in prose | ✅ | — | The only filenames referenced in prose are public artefacts (`fleet.py`, `fleet3.py`, `fleet4.py`, `fleet5.py`, `chi.json`, `clusters.json`, `phase3_…json`, `phase4_…json`) — all of which are in the Zenodo deposit. No `~/.copilot/`, no `siarc/`, no internal-folder leaks. |
| 19 | No `\write18` / shell-escape | ✅ | — | grep finds 0 hits across all 4 manuscript copies. |

---

## B. Outstanding issues (priority order)

### 🔴 1. DOI placeholder `10.5281/zenodo.XXXXXXX` at 3 sites

| Site | Line | Context |
|---|---:|---|
| Header comment | 5 | `%% Companion dataset: doi:10.5281/zenodo.XXXXXXX  (PLACEHOLDER)` |
| §11 Reproducibility | 1945 | `\texttt{10.5281/zenodo.XXXXXXX}) will be assigned by Zenodo on publication of v1.0` |
| §Computational and AI Disclosure → Reproducibility | 2047 | `The dataset DOI is \texttt{10.5281/zenodo.XXXXXXX}` |

The DOI propagation script also rewrites `references.bib`'s `@misc{wkb_dataset_v1, ...}` `doi` field, `CITATION.cff`'s `doi:` line, `README.md`'s badge, and the metadata text files. One command, ≈ 30 seconds.

### 🔴 2. Missing email + postal affiliation

Suggested drop-in replacement for L85–90:

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

### 🟡 3. Stale v1.0/v2.0 version labels

Three pieces of prose mix the manuscript-internal `v2.0` label (post-Round-2 revision) with the Zenodo deposit version `v1.0`:

| Line | Current text | Recommended edit |
|---:|---|---|
| 92 | `\date{\today\hspace{1ex}\textsc{(preprint v1.0)}}` | Drop the parenthetical, or change to `\textsc{(post-Round-2 revision)}`. |
| 1946 | "…will be assigned by Zenodo on publication of v1.0" | Replace with: "The dataset DOI is `10.5281/zenodo.20387847` (Zenodo concept `10.5281/zenodo.20387846`)." (DOI propagation handles part of this; the "of v1.0" phrase becomes vestigial and should be dropped.) |
| 2045 | "…which mirrors the Zenodo v2.0 dataset…" | Replace `v2.0` → `v1.0`, or drop the version qualifier entirely. (The Zenodo deposit's version field is `"1.0"`.) |
| 2062 | "…will be added in the camera-ready version (v2.0)." | Replace `(v2.0)` → `(in the accepted version)`, or write the final acknowledgements text now. |

---

## C. Cross-copy parity check

| Copy | Size (B) | Status |
|---|---:|---|
| `paper_v2_1.tex` (= `major_revision/followup/paper_v2_1.tex`) | 99,553 | Canonical for this report |
| `paper/manuscript.tex` | 99,553 | Byte-identical |
| `arxiv_bundle/paper.tex` | 99,553 | Byte-identical |
| `journal_bundle/paper.tex` | 99,553 | Byte-identical |

All four copies share the same SHA-256 and need the same edits.

---

## D. Things that are clean (no action needed)

- **Compile reproducibility:** 4-pass build produces 898,187-byte PDF identically across MiKTeX 2024 + TeX Live 2024.
- **Page count:** 26 pages, stable.
- **Theorem environments:** AMS-standard (`thm`, `lem`, `cor`, `prop`, `defn`, `rem`); compatible with `sigma_v3.cls` swap at camera-ready stage.
- **Cross-references:** all `\Cref{...}` and `\eqref{...}` resolve.
- **Hyperref:** `colorlinks=true`, SIGMA-friendly.
- **`\input` chain:** the only external `\input` is `figures/taxonomy_tikz.tex`, which is bundled in all 4 manuscript copies' `figures/` subdirs.
- **License:** manuscript text is CC-BY-4.0 (declared in `paper/README.md` and the Zenodo deposit); SIGMA-compatible.

---

## E. Submission-form preview (SIGMA portal)

What will paste cleanly today (no edits):

```
Title:      The WKB Geometry of Newton Polygons: A Functorial Classification Theory
Author:     Papanokechi
ORCID:      0009-0000-6192-8273
Keywords:   WKB analysis; Newton polygon; irregular singularity;
            formal classification; Levelt–Turrittin; Stokes phenomenon;
            anti-Stokes directions; wild character variety;
            functorial classification; μ_q-pullback
MSC2020:    34M40 (primary); 34M30, 34M35, 39A06, 39A13 (secondary)
Abstract:   [paste from L101–134, 175 alpha-words]
```

What needs to be edited or added before paste:

```
Affiliation:  [ADD: Independent researcher, Yokohama, Japan]
Email:        [ADD: ppapanokechi@gmail.com]
Dataset DOI:  10.5281/zenodo.20387847    [AFTER propagation; currently XXXXXXX]
arXiv ID:     [PLACEHOLDER — to be assigned at arXiv submission]
```

— *End of report.*
