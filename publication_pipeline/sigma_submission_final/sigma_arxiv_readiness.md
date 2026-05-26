# arXiv Readiness Check — SIGMA Submission

**Bundle inspected:** `arxiv_bundle/`
**Suggested arXiv categories:** `math-ph` (primary); `math.CA` + `math.AG` (cross-list)
**Reviewed:** 2026-05-26

---

## Section verdict: 🟡 PASS WITH MINOR POLISH

Bundle compiles cleanly under arXiv's AutoTeX simulation and ships every figure + `.bbl` artefact. One follow-up: bake the live DOI into the 3 placeholder sites before tarballing.

---

## A. Compliance table

| # | Required | Status | Notes |
|---|---|:---:|---|
| 1 | Single TeX file | ✅ | `arxiv_bundle/paper.tex` (99,553 B) is the sole top-level TeX. The only `\input` is `figures/taxonomy_tikz.tex`, which lives in the bundle. |
| 2 | All figures included | ✅ | `figures/constellations.png` (141,890 B) + `figures/taxonomy_tikz.tex` (4,792 B). No external image URLs, no `\includegraphics{http://...}`. |
| 3 | No external dependencies | ✅ | All `\usepackage{...}` calls reference TeX Live-shipped packages (amsmath, amssymb, amsthm, mathtools, geometry, graphicx, hyperref, xcolor, enumitem, booktabs, tikz, pgfplots, microtype, cleveref). No custom `.sty` files. |
| 4 | No shell escapes | ✅ | grep across `arxiv_bundle/` returns 0 matches for `\write18`, `\immediate\write18`, `--shell-escape`, `--enable-write18`. arXiv would auto-reject if any were present. |
| 5 | PDF builds cleanly | ✅ | 4-pass `pdflatex → bibtex → pdflatex → pdflatex` produces 898,187-byte PDF, 26 pp, 0 errors, 0 undefined refs, 0 undefined cites, 0 LaTeX warnings. |
| 6 | DOI included | 🟡 | Zenodo dataset DOI referenced at lines 5, 1945, 2047 of `arxiv_bundle/paper.tex` but **still as placeholder** `10.5281/zenodo.XXXXXXX`. **Action:** propagate the live DOI before posting (see §C). |
| 7 | GitHub repo URL included | ✅ | Lines 2043–2044: *"All code, fleet scripts, and sample artifacts are publicly available at `\url{https://github.com/papanokechi/wkb-newton-polygons}`"* (inserted in Phase 10). |
| 8 | `.bbl` shipped | ✅ | `paper.bbl` (5,533 B) is in the bundle. arXiv requires this because AutoTeX does not run `bibtex`. |
| 9 | Encoding | ✅ | Pure ASCII source; no UTF-8 BOM; mathematical Unicode lives only inside math-mode delimiters. |
| 10 | Line endings | ✅ | LF throughout (no CRLF mixing). |
| 11 | Filename hygiene | ✅ | Lowercase, no spaces, no Unicode in filenames. |
| 12 | License declaration | ✅ | Manuscript text is CC-BY-4.0 (`paper/README.md`, Zenodo deposit); arXiv accepts `cc-by-4.0` via its license picker. |

---

## B. Bundle inventory

| File | Size (B) | Purpose |
|---|---:|---|
| `paper.tex` | 99,553 | Single source TeX, byte-identical to `paper/manuscript.tex` |
| `paper.bbl` | 5,533 | Pre-built `alpha`-style bibliography (arXiv skips `bibtex` when `.bbl` ships) |
| `references.bib` | 8,753 | For downstream readers (arXiv ignores `.bib` when `.bbl` is present) |
| `paper.pdf` | 898,187 | Final 26-page PDF (arXiv re-builds from source but the local PDF is a parity check) |
| `figures/constellations.png` | 141,890 | Figure 2 (atlas summary) |
| `figures/taxonomy_tikz.tex` | 4,792 | Figure 1, `\input`-ed in source |
| `README.md` | 2,406 | Reader's note (arXiv preserves but does not display) |
| `paper.aux`, `paper.log`, `paper.out`, `paper.toc`, `paper.blg` | 54,694 (total) | LaTeX-pass artefacts (arXiv strips; recommended to remove locally before tarballing) |

**Submission payload after artefact strip:** 6 files (`paper.tex`, `paper.bbl`, `references.bib`, `figures/*` × 2, `README.md`) = **262,937 B raw**, ≈ 150 KB after gzip.

---

## C. Recommended pre-submission steps

### Step 1 (REQUIRED) — propagate the live DOI

```sh
cd <repo-root>
bash publication_pipeline/doi_propagation_commands.sh 10.5281/zenodo.20387847
```

Rewrites the 3 `XXXXXXX` placeholders in `arxiv_bundle/paper.tex` simultaneously with the other 3 manuscript copies. Recompiles the PDF.

### Step 2 (RECOMMENDED) — add `00README.XXX` for arXiv's AutoTeX

Create `arxiv_bundle/00README.XXX`:

```
%auto-include paper.bbl
%no-bibtex
```

Strictly optional (AutoTeX usually figures this out), but eliminates a class of "missing .bib entry" misfires if arXiv's TeX Live snapshot differs from the local one.

### Step 3 (RECOMMENDED) — strip LaTeX artefacts before tarballing

```sh
rm arxiv_bundle/paper.aux
rm arxiv_bundle/paper.log
rm arxiv_bundle/paper.out
rm arxiv_bundle/paper.toc
rm arxiv_bundle/paper.blg
tar czf arxiv-submission.tgz -C arxiv_bundle .
```

arXiv strips these on its end, but the upload is smaller and the AutoTeX log is cleaner.

### Step 4 (OPTIONAL) — re-derive the PDF for parity

After Step 1, recompile so the shipped `paper.pdf` matches what arXiv's AutoTeX will generate. Avoids the reader's "downloaded PDF differs from rebuild" surprise.

---

## D. Cross-list categories

| Category | Rationale |
|---|---|
| `math-ph` (primary) | Wild character variety, Stokes geometry, p-adic-flavoured WKB — natural home. |
| `math.CA` (cross-list) | Linear ODEs with irregular singularities, Newton polygons, Levelt–Turrittin. |
| `math.AG` (cross-list) | μ_q-pullback geometry, functorial classification, character-variety structure. |

SIGMA accepts arXiv preprints from any of these primary categories; the cross-list set helps discoverability.

---

## E. Pre-flight sanity checks

| Check | Command | Expected | Got |
|---|---|---|---|
| Bundle compiles | `cd arxiv_bundle && pdflatex paper && bibtex paper && pdflatex paper && pdflatex paper` | 0 errors | 0 errors |
| PDF parity | `Get-FileHash arxiv_bundle/paper.pdf` vs `paper/manuscript.pdf` | identical | identical (898,187 B) |
| Font embedding | `pdffonts paper.pdf` | all fonts embedded | all embedded (Computer Modern + Latin Modern + Helvetica-narrow for TikZ; subset = yes) |
| No `\write18` | `grep -nR 'write18' arxiv_bundle/` | 0 matches | 0 matches |
| No `\openout` outside bundle | `grep -nR '\\openout' arxiv_bundle/` | 0 (LaTeX-internal only) | 0 (only auto-generated `.aux` opens) |

---

**⚠️ arXiv endorsement is required for this paper** (first-time submitter to `math-ph` with non-institutional email + single-author paper closes both auto-endorsement paths). Plan for **3–14 days** to obtain endorsement; backup path is direct email to SIGMA (see §G).

---

## F. arXiv is the SIGMA submission portal (NOT optional in normal circumstances)

**Correction to earlier notes:** SIGMA is explicitly an **arXiv overlay journal**, and arXiv is the *canonical* submission path. Per the SIGMA "How to Submit" page (<https://www.emis.de/journals/SIGMA/about.html>):

> *"Please submit the paper to arXiv.org and send the arXiv number to editor@sigma-journal.com or (in exceptional cases only) you can send the zipped paper in TeX/LaTeX format directly to editor@sigma-journal.com … with an explanation why you prefer not to put the paper to arXiv."*

Concrete consequences:

1. **There is no separate SIGMA web portal.** The "submission" consists of posting to arXiv, then emailing the arXiv ID to `editor@sigma-journal.com`.
2. **Posting to arXiv must precede emailing SIGMA**, since the email body is built around the arXiv ID.
3. **Direct-by-email-only submission** is allowed as an exception but requires written justification for not using arXiv. For this paper, "first-time `math-ph` submitter awaiting endorsement" is the relevant justification if endorsement stalls (see §G).
4. **Therefore the arXiv-readiness checks in this report are mandatory pre-submission checks**, not "nice to have".

---

## G. Endorsement strategy

| Step | Action | Notes |
|---|---|---|
| 1 | Start a `math-ph` submission at <https://arxiv.org/submit> | Triggers arXiv to email a 6-char endorsement code |
| 2 | Identify candidate endorsers | (i) Authors of papers cited in `references.bib` (the Sabbah / Mochizuki / Hertling / Singer school for irregular ODEs and Stokes geometry); (ii) SIGMA editorial-board members who are `math-ph`-active (e.g., Eric Rains, Bertrand Eynard, Boris Khesin, Alexander Its, Carlos Simpson). These editors are familiar with SIGMA's arXiv-overlay model. |
| 3 | Contact 1–3 candidates politely | Include the endorsement code, Zenodo DOI `10.5281/zenodo.20387847`, GitHub URL <https://github.com/papanokechi/wkb-newton-polygons>, and a 1-paragraph abstract. **Do not** mass-mail many endorsers at once — arXiv's policy discourages this. |
| 4 | Wait for endorser to act | One positive endorsement is sufficient |
| 5 | If no response in ~2 weeks | Take the SIGMA exception path (direct-email-to-`editor@sigma-journal.com` with endorsement-blocked justification; see `submission_filelist.md` §E for the email template) |

— *End of report.*
