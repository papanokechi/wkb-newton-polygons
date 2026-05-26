# Manuscript Compliance Report — SIGMA Submission

**Manuscript:** `paper/manuscript.tex` (byte-identical to `arxiv_bundle/paper.tex`, `journal_bundle/paper.tex`, and `major_revision/followup/paper_v2_1.tex`; SHA size 99,553 B)
**Companion PDF:** `paper/manuscript.pdf` (898,187 B, 26 pp)
**Target venue:** SIGMA — Symmetry, Integrability and Geometry: Methods and Applications
**Reviewed:** 2026-05-26

---

## Summary verdict

🟡 **PASS WITH MINOR POLISH** — manuscript is mathematically and structurally complete; three categories of touch-up needed before clicking *Submit* on the SIGMA portal: (1) bake the live Zenodo DOI into 3 placeholder sites, (2) add author email + postal affiliation, (3) refresh the acknowledgements + "Zenodo v2.0" / "preprint v1.0" version labels to match the final v1.0 deposit and post-Round-2 manuscript state.

---

## 1. Required-field checklist

| # | Requirement | Status | Location | Notes |
|---|---|---|---|---|
| 1 | Title | ✅ | L82–83 | *"The WKB Geometry of Newton Polygons: A Functorial Classification Theory"* — matches Zenodo record exactly. |
| 2 | Author | ✅ | L85–90 | Papanokechi (mononym, project canonical). |
| 3 | ORCID | ✅ | L87 | `0009-0000-6192-8273` (rendered as live hyperlink). |
| 4 | Affiliation (postal/institutional) | 🔴 | L86 | Only the textual note *"Independent researcher"* in `\thanks{...}`. SIGMA's submission form normally expects at least a city + country. **Recommended:** add *"Independent researcher, Yokohama, Japan"* (matches the HAL deposit form-field convention). |
| 5 | Email | 🔴 | — | **MISSING.** SIGMA's submission portal requires a corresponding-author email. **Recommended:** add `ppapanokechi@gmail.com` (the address registered on the SIARC pipeline; also used as the GitHub Discussions fallback channel for PCF-1). |
| 6 | Abstract present | ✅ | L101–134 | Self-contained, no internal references that point outside the abstract. |
| 7 | Abstract ≤ 220 words | ✅ | — | **175 alpha words** by strict count (math expressions stripped; 224 raw tokens including math). Well under SIGMA's typical 200–250 limit. |
| 8 | MSC2020 codes | ✅ | L143 | `34M40` (primary); `34M30, 34M35, 39A06, 39A13` (secondary). Five codes, in scope for SIGMA. |
| 9 | Keywords | ✅ | L137–140 | 10 keywords, semicolon-separated, matching the Zenodo deposit core terminology (WKB analysis; Newton polygon; irregular singularity; formal classification; Levelt–Turrittin; Stokes phenomenon; anti-Stokes directions; wild character variety; functorial classification; μ_q-pullback). |
| 10 | Acknowledgements | 🟡 | L2056–L2062 | Present (`\section*{Acknowledgements}`), but the body still reads *"Acknowledgements of individual collaborators and funding sources will be added in the camera-ready version (v2.0)"*. **Recommended:** finalize wording for SIGMA's pre-acceptance state (camera-ready language can be substituted at proof stage). |
| 11 | References compile cleanly | ✅ | L2068–2069 | `\bibliographystyle{alpha}` + `\bibliography{references}`. Pre-built `paper.bbl` (5,533 B) ships alongside; 4-pass compile produces 26 pp, no warnings, no undefined citations. |
| 12 | Figures render correctly | ✅ | L1740 (taxonomy `\input`), L? (constellations `\includegraphics`) | Figure 1 = `figures/taxonomy_tikz.tex` (TikZ, 4,792 B); Figure 2 = `figures/constellations.png` (141,890 B). Both bundled in arxiv_bundle/figures/ and journal_bundle/figures/. |
| 13 | AI disclosure present + factual | ✅ | L1951–L2050 | `\section*{Computational and AI Disclosure}` with 5 paragraphs: Computational environment, Automated pipelines (Phases I–V), Role of AI assistance, Human accountability, Reproducibility. Names the tooling explicitly (GitHub Copilot CLI + Anthropic Claude Opus 4.7). Factual and non-promotional. |
| 14 | Reproducibility statement | ✅ | L1914–L1946 (§11) + L2036–L2050 (in disclosure) | §11 lists the dataset directory structure, fleet sequence, deterministic guarantee. The Disclosure §Reproducibility points to both the Zenodo DOI and the public GitHub URL. |
| 15 | No dataset-internal identifiers in prose | ✅ | — | Confirmed: grep finds no `operator_id`, `op_id`, `phase_id`, `dataset_id`, `fleet_run_id`, or per-item JSON record indices in the prose. (Round-1 revision sweep removed these.) |
| 16 | No `\write18` / shell-escape macros | ✅ | — | grep finds zero hits across `paper/`, `arxiv_bundle/`, `journal_bundle/`, and `major_revision/followup/`. |

---

## 2. Outstanding issues to fix (in priority order)

### 🔴 Issue 1 — DOI placeholder `10.5281/zenodo.XXXXXXX` in 3 sites

The live Zenodo DOI is now `10.5281/zenodo.20387847` (concept `20387846`), but three sites in the manuscript still hold the placeholder string:

| Line | File | Context |
|---|---|---|
| 5 | `paper/manuscript.tex` + `arxiv_bundle/paper.tex` (header comment) | `%% Companion dataset: doi:10.5281/zenodo.XXXXXXX  (PLACEHOLDER)` |
| 1945 | (all 4 copies) | `\texttt{10.5281/zenodo.XXXXXXX}) will be assigned by Zenodo on publication of v1.0` — inside the Reproducibility note (§11). |
| 2047 | (all 4 copies) | `The dataset DOI is \texttt{10.5281/zenodo.XXXXXXX}` — inside the Computational and AI Disclosure / Reproducibility paragraph. |

**Fix:** run `bash publication_pipeline/doi_propagation_commands.sh 10.5281/zenodo.20387847` from the repo root, then `pdflatex → bibtex → pdflatex ×2`. The propagation script also handles `references.bib`, `CITATION.cff`, `README.md`, and the metadata files; it touches roughly 46 files in one pass.

### 🔴 Issue 2 — Missing email + postal affiliation

The current `\author{...\thanks{Independent researcher.}}` block has neither an email nor a city/country. SIGMA's submission portal will reject the form without a corresponding-author email.

**Suggested replacement (drop-in for L85–90):**

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

(Note: the GitHub URL also gets upgraded from `https://github.com/papanokechi` to the specific repo `https://github.com/papanokechi/wkb-newton-polygons`, consistent with the Reproducibility paragraph's repo pointer.)

### 🟡 Issue 3 — Stale version labels around v1.0 ↔ v2.0

Three pieces of prose carry inconsistent version labels:

| Site | Current text | Reality | Recommended edit |
|---|---|---|---|
| L92 `\date{...}` | `(preprint v1.0)` | Manuscript is post-Round-2 revision; project label is "v2.0"; Zenodo deposit is "v1.0" (first record for this paper). | Pick one convention. Cleanest: drop the parenthetical from `\date{}` entirely and rely on Zenodo's deposit version field as the canonical version source. |
| L1946 | "*…will be assigned by Zenodo on publication of v1.0*" | The deposit is v1.0 and has already been assigned. | Replace with: "*The dataset DOI is `10.5281/zenodo.20387847` (Zenodo concept `10.5281/zenodo.20387846`)*." |
| L2045 | "*…which mirrors the Zenodo v2.0 dataset…*" | The Zenodo deposit is v1.0 (this is the first-ever Zenodo record for the WKB paper; the unrelated `10.5281/zenodo.20355904` is a Khinchin's-constant deposit). | Replace "v2.0" with "v1.0" — or drop the version qualifier entirely. |
| L2062 | "*…will be added in the camera-ready version (v2.0).*" | Camera-ready and pre-acceptance are different milestones; SIGMA's referee process happens BEFORE camera-ready. | Either (a) keep the placeholder but change "(v2.0)" to "(in the accepted version)", or (b) write the final acknowledgements text now. |

### 🟢 Issue 4 — Document class (informational, not a blocker for SIGMA)

Current preamble:
```
\documentclass[11pt,a4paper]{article}
```

SIGMA's house style ships `sigma.cls` (latest: `sigma_v3.cls`, see <https://www.emis.de/journals/SIGMA/about.html#tex>). SIGMA accepts AMS-`article` submissions for the initial review and asks for the cls swap **only after acceptance**, so this is not a blocker for first-round submission. The current preamble compiles cleanly against `article.cls`.

---

## 3. Things that ARE clean (no action needed)

- Document compiles bytewise-deterministically: `pdflatex → bibtex → pdflatex → pdflatex` yields the same 898,187-byte PDF across MiKTeX and TeX Live.
- 26-page final PDF, no overfull/underfull warnings at compile.
- Bibliography style `alpha` (acceptable to SIGMA; they also accept `amsplain`, `amsalpha`, `siam`, etc.).
- All `\Cref{...}` cross-references resolve.
- Theorem-statement environments (`thm`, `lem`, `cor`, `prop`, `defn`, `rem`) are AMS-standard; no custom classes that would clash with `sigma.cls`.
- Hyperref colour links: `colorlinks=true` (SIGMA-friendly).
- No `\input` of external files outside the bundle (only `figures/taxonomy_tikz.tex`, which is shipped).
- 0 `\write18`, 0 shell-escape, 0 `\immediate\openout`.

---

## 4. Comparison across the 4 manuscript copies

| Copy | Bytes | Status |
|---|---:|---|
| `paper/manuscript.tex` | 99,553 | Canonical |
| `arxiv_bundle/paper.tex` | 99,553 | Byte-identical |
| `journal_bundle/paper.tex` | 99,553 | Byte-identical |
| `major_revision/followup/paper_v2_1.tex` | 99,553 | Byte-identical |

All four copies share the same SHA-256 and need the same fixes. The DOI-propagation script handles all four simultaneously.

---

## 5. Compile verification

| Pass | Command | Result |
|---|---|---|
| 1 | `pdflatex paper.tex` | Builds; 1 undefined cross-ref (resolved next pass) |
| 2 | `bibtex paper` | 24 entries from `references.bib`; 0 errors, 0 warnings |
| 3 | `pdflatex paper.tex` | Resolves citations |
| 4 | `pdflatex paper.tex` | Final pass; PDF 898,187 B; 26 pp; identical bytes to `paper/manuscript.pdf` |

(Result is reproducible from any of the 4 source copies above.)
