# arXiv Readiness Report — SIGMA Submission

**Bundle inspected:** `arxiv_bundle/`
**Target archive:** `math-ph` (primary), with cross-list to `math.CA` (Classical Analysis & ODEs) and `math.AG` (Algebraic Geometry — wild character variety side).
**Reviewed:** 2026-05-26

---

## Summary verdict

🟢 **PASS WITH MINOR POLISH** — bundle builds cleanly under arXiv's AutoTeX (TeX Live 2024 simulation). Two follow-ups before posting: DOI-placeholder propagation and an explicit `00README.XXX` for arXiv's processor.

---

## 1. Bundle inventory

| File | Size | Notes |
|---|---:|---|
| `paper.tex` | 99,553 B | Single source TeX, byte-identical to `paper/manuscript.tex`. |
| `paper.bbl` | 5,533 B | Pre-built `alpha`-style bibliography (arXiv will SKIP `bibtex` when `.bbl` ships). |
| `references.bib` | 8,753 B | Included for downstream re-build by readers — arXiv ignores `.bib` if `.bbl` is present. |
| `paper.pdf` | 898,187 B | Final 26-page PDF; arXiv re-builds from source but this acts as a parity check. |
| `paper.aux` | 13,847 B | LaTeX-pass artefact (arXiv strips). |
| `paper.log` | 27,981 B | LaTeX-pass artefact (arXiv strips). |
| `paper.out` | 6,213 B | hyperref outline (arXiv strips). |
| `paper.toc` | 5,406 B | TOC artefact (arXiv strips). |
| `paper.blg` | 1,247 B | bibtex log (arXiv strips). |
| `figures/constellations.png` | 141,890 B | Figure 2 (atlas summary). |
| `figures/taxonomy_tikz.tex` | 4,792 B | Figure 1, `\input`-ed in source — TikZ standalone (so it compiles in the main document, no separate compile-of-standalone needed). |
| `README.md` | 2,406 B | Optional reader's note (arXiv preserves but does not display). |

**arXiv-relevant set** (after artefact strip): `paper.tex`, `paper.bbl`, `references.bib`, `figures/constellations.png`, `figures/taxonomy_tikz.tex`, `README.md` — **6 files, 262,937 B total source payload**.

---

## 2. arXiv-compliance checklist

| # | Requirement | Status | Notes |
|---|---|---|---|
| 1 | **Single source TeX file** | ✅ | `paper.tex` is the only top-level TeX; the only `\input` target is `figures/taxonomy_tikz.tex` (allowed, since it lives in the bundle). |
| 2 | **All figures included** | ✅ | 2 figures, both present in `figures/`. No external image URLs, no `\includegraphics{http://...}`. |
| 3 | **No external dependencies** | ✅ | All `\usepackage{...}` calls reference TeX Live-shipped packages (amsmath, amssymb, amsthm, mathtools, geometry, graphicx, hyperref, xcolor, enumitem, booktabs, tikz, pgfplots, microtype, cleveref). No custom `.sty` files. |
| 4 | **No `\write18` / `--shell-escape`** | ✅ | grep across `arxiv_bundle/` returns 0 matches for `\write18`, `\immediate\write18`, `--shell-escape`, `--enable-write18`. **arXiv would auto-reject** if any of these were present. |
| 5 | **No `\input` of out-of-bundle paths** | ✅ | The only `\input` is `\input{figures/taxonomy_tikz.tex}`; the path is relative and the target is in the bundle. |
| 6 | **PDF builds cleanly** | ✅ | 4-pass `pdflatex → bibtex → pdflatex → pdflatex` produces 898,187-byte PDF, 26 pages, 0 errors, 0 undefined refs, 0 undefined cites, 0 LaTeX warnings, 2 cosmetic BibTeX warnings (one for capitalised middle word in a journal title, both pre-existing and SIGMA-acceptable). |
| 7 | **`paper.bbl` shipped** | ✅ | arXiv requires the `.bbl` to be in the bundle since it does not auto-run `bibtex`. Confirmed at 5,533 B. |
| 8 | **DOI included in metadata** | 🟡 | The Zenodo dataset DOI is referenced in source at lines 5, 1945, and 2047 but **still as the placeholder `10.5281/zenodo.XXXXXXX`**. Action: run `bash publication_pipeline/doi_propagation_commands.sh 10.5281/zenodo.20387847` BEFORE creating the arXiv submission tarball. The propagation script writes to `arxiv_bundle/paper.tex` simultaneously with the canonical copy, so a single invocation fixes both. |
| 9 | **GitHub repo URL included in disclosure** | ✅ | Confirmed at lines 2043–2044 of `arxiv_bundle/paper.tex`: *"All code, fleet scripts, and sample artifacts are publicly available at \url{https://github.com/papanokechi/wkb-newton-polygons}"* — inserted in Phase 10. |
| 10 | **Encoding** | ✅ | Pure ASCII-clean source (no UTF-8 BOM, no non-ASCII chars in code; mathematical Unicode lives only inside `$...$` delimiters where Tex parses it as math anyway). |
| 11 | **Line endings** | ✅ | LF throughout (the bundle was prepared on a Unix-style pipeline; no CRLF mixing). |
| 12 | **Filename hygiene** | ✅ | Lowercase, no spaces, no Unicode in filenames. |
| 13 | **License declaration for arXiv** | ✅ | Manuscript text is CC-BY-4.0 (see `LICENSE-TEXT` in Zenodo deposit; also declared in `paper/README.md`). arXiv accepts `cc-by-4.0` via its submission-form license picker. |

---

## 3. Recommended pre-submission steps

### Step A (REQUIRED) — propagate the live DOI

```sh
cd <repo-root>
bash publication_pipeline/doi_propagation_commands.sh 10.5281/zenodo.20387847
```

This single invocation rewrites the three `XXXXXXX` placeholders in `arxiv_bundle/paper.tex`, recompiles the PDF, and updates `references.bib`'s `@misc{wkb_dataset_v1, ...}` `doi` field.

### Step B (RECOMMENDED) — add `00README.XXX` for arXiv's processor

Create `arxiv_bundle/00README.XXX`:

```
%auto-include paper.bbl
%no-bibtex
```

Tells arXiv's AutoTeX to use the shipped `.bbl` directly and skip `bibtex`. Strictly optional (AutoTeX usually figures this out), but it eliminates an entire class of "missing .bib entry" misfires when arXiv's TeX Live snapshot differs slightly from the local one.

### Step C (RECOMMENDED) — strip LaTeX artefacts before tarballing

Before `tar czf arxiv-submission.tgz arxiv_bundle/`, run:

```sh
rm arxiv_bundle/paper.aux
rm arxiv_bundle/paper.log
rm arxiv_bundle/paper.out
rm arxiv_bundle/paper.toc
rm arxiv_bundle/paper.blg
```

arXiv strips these on its end, but the upload is smaller and the AutoTeX log is cleaner without them. The 6 files needed (`paper.tex`, `paper.bbl`, `references.bib`, `figures/`, `README.md`, optional `00README.XXX`) total ~263 KB raw, ~150 KB after gzip.

### Step D (OPTIONAL) — re-derive the PDF for parity

After step A, recompile the PDF in the bundle (`pdflatex paper → pdflatex paper`) so that the shipped `paper.pdf` matches what arXiv's AutoTeX will generate. This avoids the reader's "downloaded PDF differs from the rebuild" surprise.

---

## 4. Cross-list categories

Suggested arXiv classification (matches MSC2020 in manuscript L143):

| Category | Rationale |
|---|---|
| `math-ph` (primary) | Wild character variety, Stokes geometry, p-adic-flavoured WKB — natural home. |
| `math.CA` (cross-list) | Linear ODEs with irregular singularities, Newton polygons, Levelt–Turrittin. |
| `math.AG` (cross-list) | μ_q-pullback geometry, functorial classification, character-variety structure. |

(SIGMA accepts arXiv preprints from any of these primary categories; the cross-list set helps discoverability.)

---

## 5. License compatibility

| Aspect | Setting | arXiv accepts? |
|---|---|---|
| Manuscript text | CC-BY-4.0 | ✅ Yes (`cc-by-4.0` is one of arXiv's selectable license types). |
| Code referenced from manuscript | MIT (bundled separately in the GitHub repo) | ✅ N/A for arXiv (code is in the Zenodo deposit and the GitHub repo, not in the arXiv source). |
| Figures | CC-BY-4.0 (inherits from manuscript) | ✅ Yes. |

---

## 6. Pre-flight sanity checks

| Check | Command | Expected | Got |
|---|---|---|---|
| Bundle compiles | `cd arxiv_bundle && pdflatex paper && bibtex paper && pdflatex paper && pdflatex paper` | 0 errors | 0 errors |
| PDF parity | `Get-FileHash arxiv_bundle/paper.pdf` vs `paper/manuscript.pdf` | identical | identical (898,187 B) |
| Font embedding | `pdffonts paper.pdf` | all fonts embedded | all embedded (Computer Modern + Latin Modern + Helvetica-narrow for TikZ; subset = yes) |
| No `\write18` | `grep -nR 'write18' arxiv_bundle/` | 0 matches | 0 matches |
| No `\openout` outside bundle | `grep -nR '\\openout' arxiv_bundle/` | 0 (LaTeX-internal only) | 0 (only auto-generated `.aux` opens) |

---

## 7. Conclusion

The bundle is essentially shovel-ready. After **Step A** (DOI propagation, ~30 seconds) the `arxiv_bundle/` is suitable to be tarred and uploaded to arXiv as the SIGMA-companion preprint. SIGMA's submission form has a free-text "arXiv ID" field that the author should fill in with the resulting `arXiv:YYMM.NNNNN` identifier; that ID can then be back-propagated into the manuscript's Zenodo description (Edit-record → add `isSupplementTo arXiv:...`) and into the manuscript's `references.bib` `@misc{wkb_preprint_arxiv, ...}` stub, in a final two-line commit.
