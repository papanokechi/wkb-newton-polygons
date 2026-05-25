# Repo-URL Insertion — Verification Report

**Task.** Verify whether the public GitHub repository URL
`https://github.com/papanokechi/wkb-newton-polygons` is present in the
`\paragraph{Reproducibility.}` block of `\section*{Computational and AI Disclosure}`
across all four synchronized manuscript copies; if missing, insert it and
recompile.

**Outcome.** URL was missing from all four files; the required sentence
has been inserted, all four files are byte-identical post-edit, and the
manuscript recompiles cleanly at 26 pages with 0 errors and 0 LaTeX
warnings.

---

## 1. Pre-edit search (before changes)

| # | File                                       | URL present? | Line |
|---|--------------------------------------------|--------------|------|
| 1 | `paper/paper.tex`                          | **MISSING**  |   —  |
| 2 | `arxiv_bundle/paper.tex`                   | **MISSING**  |   —  |
| 3 | `journal_bundle/paper.tex`                 | **MISSING**  |   —  |
| 4 | `major_revision/followup/paper_v2_1.tex`   | **MISSING**  |   —  |

All four files were byte-identical at 99,309 bytes; SHA-256 match
confirmed prior to edit. A snapshot of the pre-edit file is preserved at
`major_revision/repo_url_check/paper_pre_repourl.tex` and serves as the
diff base.

> *Note*. Line 89 of all four files already contained
> `\url{https://github.com/papanokechi}` inside the author `\thanks{...}`
> block (a link to the author's GitHub profile, not the repo). This does
> not satisfy the task requirement, which targets the project repo URL
> inside the Reproducibility paragraph.

---

## 2. Insertion location

In every file the `\paragraph{Reproducibility.}` heading sits at
**line 2036**, and the first sentence of that paragraph closes with
`MIT (code and pipelines).` at the end of line 2042 (post-edit).
The new sentence was inserted immediately after that period and before
the existing `The dataset DOI is \texttt{...}` sentence:

```latex
\paragraph{Reproducibility.}
The complete computational record --- operators, Newton polygons,
characteristic polynomials, constellations, clusters, counterexamples,
Phase-III/IV invariants, proof skeletons, integration map, and
rendered figures --- is deposited as the companion Zenodo dataset
\cite{wkb_dataset_v1}, licensed CC-BY-4.0 (text and data) and MIT
(code and pipelines).
All code, fleet scripts, and sample artifacts are publicly available
at \url{https://github.com/papanokechi/wkb-newton-polygons}, which
mirrors the Zenodo v2.0 dataset and provides a stable, versioned
record of the computational workflow.
The dataset DOI is \texttt{10.5281/zenodo.XXXXXXX}
(placeholder, assigned by Zenodo at publication of v1.0). See
\Cref{sec:reproducibility} for the command sequence that reproduces
every artifact.
```

The inserted sentence (lines 2043–2046):

- begins with a capital letter,
- terminates with a period,
- uses `\url{...}` exactly (no `\href`, no leading scheme outside the brace),
- preserves every other word of the original Reproducibility paragraph,
- does not introduce a paragraph break (single blank line still
  separates the paragraph from the following Acknowledgements section).

---

## 3. Post-edit search

| # | File                                       | URL present? | Line |
|---|--------------------------------------------|--------------|------|
| 1 | `paper/paper.tex`                          | **PRESENT**  | 2044 |
| 2 | `arxiv_bundle/paper.tex`                   | **PRESENT**  | 2044 |
| 3 | `journal_bundle/paper.tex`                 | **PRESENT**  | 2044 |
| 4 | `major_revision/followup/paper_v2_1.tex`   | **PRESENT**  | 2044 |

All four files are byte-identical after the edit:

```
99553 bytes  SHA-256 fe7bec32ae64b4c7...  paper/paper.tex
99553 bytes  SHA-256 fe7bec32ae64b4c7...  arxiv_bundle/paper.tex
99553 bytes  SHA-256 fe7bec32ae64b4c7...  journal_bundle/paper.tex
99553 bytes  SHA-256 fe7bec32ae64b4c7...  major_revision/followup/paper_v2_1.tex
```

Size delta: **+244 bytes** = the inserted sentence including newlines
(re-flowing the existing `(code and pipelines).` onto its own line).

---

## 4. Compile verification (paper/paper.tex)

Four-pass compile (pdflatex → bibtex → pdflatex × 3) executed in
`paper/`:

| Metric                        | Result                          |
|-------------------------------|---------------------------------|
| LaTeX errors                  | **0**                           |
| Undefined references          | **0**                           |
| Undefined citations           | **0**                           |
| LaTeX warnings                | **0**                           |
| Page count                    | **26**                          |
| PDF size                      | **898,187 bytes**               |
| BibTeX warnings (pre-existing)| 2 (cosmetic: `mochizuki-asymptotic`, `ramis-q-stokes` — number-vs-volume style only)  |

Page count is unchanged at 26 (target met); PDF size grew by 1,082 bytes
(897,105 → 898,187), consistent with the additional inline URL.

Full compile transcript is captured in `compile_log_repo_url.md`.

---

## 5. Bundle parity

Rebuilt `paper.pdf` + `paper.bbl` were synced to the bundle copies and
the Zenodo v2.0 package, so every distribution channel now ships the
URL-inserted PDF:

```
898187 bytes  paper/paper.pdf
898187 bytes  arxiv_bundle/paper.pdf
898187 bytes  journal_bundle/paper.pdf
898187 bytes  publication_pipeline/zenodo_v2_package/paper.pdf
898187 bytes  publication_pipeline/zenodo_v2_package/manuscript.pdf
```

`paper/paper.tex` was also mirrored into
`publication_pipeline/zenodo_v2_package/manuscript.tex` so the Zenodo
upload tree carries the same source.

---

## 6. Deliverables

All artifacts placed in `major_revision/repo_url_check/`:

- `paper_pre_repourl.tex` — pre-edit snapshot (diff base).
- `repo_url_check_and_insert.diff` — unified diff covering all four
  manuscript files (one hunk each, identical content).
- `repo_url_verification_report.md` — this file.
- `compile_log_repo_url.md` — four-pass compile transcript.

---

## 7. Final checklist

- [x] URL searched in all four target files (pre-edit: missing in all).
- [x] URL inserted immediately after the first sentence of
      `\paragraph{Reproducibility.}` in every file.
- [x] Sentence uses `\url{...}` exactly and terminates with a period.
- [x] No other wording in the disclosure was altered.
- [x] All four files byte-identical after the edit (single SHA-256).
- [x] Compile clean: 0 errors, 0 undefined refs, 0 undefined cites,
      0 LaTeX warnings, 26 pages.
- [x] Rebuilt PDF/bbl propagated to `arxiv_bundle/`,
      `journal_bundle/`, and `publication_pipeline/zenodo_v2_package/`.
- [x] Unified diff regenerated as `repo_url_check_and_insert.diff`.
- [x] Pre-existing BibTeX cosmetic warnings (2) unchanged.
