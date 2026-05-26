# Submission File List — SIGMA

**Purpose:** what to post to arXiv + what to email to SIGMA.
**SIGMA submission flow:** arXiv overlay — post to arXiv, then email arXiv ID to `editor@sigma-journal.com`.
**SIGMA "How to Submit":** <https://www.emis.de/journals/SIGMA/about.html#submit>

---

## ⚠️ SIGMA has no web upload portal

SIGMA is an **arXiv overlay journal**. The actual submission consists of:

1. Uploading the manuscript to arXiv (canonical path), then
2. Emailing the arXiv ID + cover letter to `editor@sigma-journal.com`.

There is no SIGMA web form to upload PDF + figures + bib through. The lists below are split accordingly: §A (post to arXiv), §B (email to SIGMA), §C (cite in manuscript / cover letter).

---

## A. Upload to arXiv

| Slot | File | Source | Size | Notes |
|---|---|---|---:|---|
| 1 | `paper.tex` | `arxiv_bundle/paper.tex` | 99,553 B | Single-source TeX, standalone AMS-`article` class |
| 2 | `paper.bbl` | `arxiv_bundle/paper.bbl` | 5,533 B | Pre-built `alpha`-style bibliography (arXiv skips `bibtex`) |
| 3 | `references.bib` | `arxiv_bundle/references.bib` | 8,753 B | For downstream readers (arXiv ignores when `.bbl` is present) |
| 4 | `figures/taxonomy_tikz.tex` | `arxiv_bundle/figures/taxonomy_tikz.tex` | 4,792 B | Figure 1 (TikZ; `\input`-ed into `paper.tex`) |
| 5 | `figures/constellations.png` | `arxiv_bundle/figures/constellations.png` | 141,890 B | Figure 2 (300 DPI raster) |
| 6 | `README.md` | `arxiv_bundle/README.md` | 2,406 B | Optional reader's note |

**Subtotal — 6 files, ~263 KB raw**, ~150 KB after gzip.

**Tarball command:**
```sh
cd arxiv_bundle
tar czf ../arxiv-submission.tgz paper.tex paper.bbl references.bib \
        figures/taxonomy_tikz.tex figures/constellations.png README.md
```

**Suggested arXiv classification:**
- Primary: `math-ph`
- Cross-list: `math.CA`, `math.AG`

**⚠️ arXiv endorsement required (BLOCKER for first-time submitters):**

Posting to `math-ph` requires an endorsement because the submitting account has:
- a non-institutional email (`ppapanokechi@gmail.com`), and
- no prior arXiv claims under ORCID `0009-0000-6192-8273` to bootstrap auto-endorsement.

Resolution path:
1. Start a submission at <https://arxiv.org/submit>; select `math-ph`.
2. arXiv emails a 6-character endorsement code.
3. Forward the code to an established `math-ph` author (good candidates: authors of papers cited in `references.bib`; SIGMA editorial-board members who are `math-ph`-active, e.g., Eric Rains, Bertrand Eynard, Boris Khesin, Alexander Its, Carlos Simpson — they understand SIGMA's arXiv-overlay model).
4. The endorser enters the code at <https://arxiv.org/auth/endorse>; one positive vote suffices.
5. After endorsement, complete the submission.

**Timeline impact:** endorsement typically resolves in 3–14 days. Plan accordingly.

If the endorsement path stalls, fall back to the SIGMA exception path in §E below.

---

## B. Email to SIGMA (`editor@sigma-journal.com`)

After arXiv assigns an ID (typically same-day; arXiv ID format `YYMM.NNNNN`):

| Slot | Content | Source |
|---|---|---|
| 1 | **Email body** = cover letter | Render `submission_cover_letter.md` to plain text (or attach as PDF); replace `[ARXIV ID]` with the assigned ID |
| 2 | **Subject line** | `Submission to SIGMA — arXiv:[ARXIV ID] — The WKB Geometry of Newton Polygons` |
| 3 | **Optional attachment** | None required (the arXiv ID IS the submission). Optionally include the cover letter as `cover_letter.pdf` attachment for editorial convenience. |

**Recipients:**
- To: `editor@sigma-journal.com`
- Cc *(in case primary doesn't acknowledge in 2 working days)*: `sigmajournal@gmail.com`

**Important:** do NOT email the manuscript PDF/zip in the first instance. SIGMA's preferred flow is *"arXiv ID first; manuscript attached only by exception"*.

---

## C. Cite in manuscript / cover letter (do NOT re-upload)

These artefacts already live at stable URLs and are cited by identifier:

| Resource | Identifier | Cited at |
|---|---|---|
| Supplementary archive (45 files, 3.96 MB) | DOI `10.5281/zenodo.20387847` | Manuscript L1945, L2047 (after DOI propagation); cover letter; arXiv abstract page |
| GitHub mirror | <https://github.com/papanokechi/wkb-newton-polygons> | Manuscript L2043–2044; cover letter |
| GitHub release v2.0 | <https://github.com/papanokechi/wkb-newton-polygons/releases/tag/v2.0> | Zenodo `isIdenticalTo` relation |

The Zenodo deposit contains the full 45-file supplementary archive (`manuscript.pdf`, `manuscript.tex`, `references.bib`, `paper.bbl`, `figures/`, `data/` 19 JSON, `reports/` 6 MD, `code/` MIT, `fleets/` MIT, `LICENSE-CODE`, `LICENSE-TEXT`, `CITATION.cff`, `release_notes_v2.0.txt`, `README.md`, plus 3 bonus files); none of this needs to be re-uploaded through arXiv or attached to the SIGMA email — the DOI in the manuscript body and cover letter is the canonical reference.

---

## D. Pre-submission checklist

| # | Item | Action | Status |
|---|---|---|:---:|
| 1 | Live DOI baked into manuscript | `bash publication_pipeline/doi_propagation_commands.sh 10.5281/zenodo.20387847` | ⏳ |
| 2 | Author email + postal affiliation added to `\author{\thanks{...}}` | Edit L85–90 of all 4 manuscript copies | ⏳ |
| 3 | Stale v1.0/v2.0 version labels cleaned (4 sites) | See `sigma_manuscript_compliance.md` §B.3 | ⏳ |
| 4 | Acknowledgements finalised (or graceful placeholder) | Edit L2056–L2062 | ⏳ |
| 5 | 4-pass recompile (`pdflatex → bibtex → pdflatex → pdflatex`) | Verify 26 pp, 0 errors, 0 undefined refs/cites | ⏳ |
| 6 | Strip LaTeX artefacts from `arxiv_bundle/` | `rm arxiv_bundle/paper.{aux,log,out,toc,blg}` | ⏳ |
| 7 | Tar arxiv submission | `tar czf arxiv-submission.tgz …` (see §A) | ⏳ |
| 8 | Upload to arXiv `math-ph` primary | Via <https://arxiv.org/submit> | ⏳ |
| 9 | Wait for arXiv ID assignment | Typically same-day | ⏳ |
| 10 | Customise cover letter | Replace `[DATE]`, `[EDITOR NAME]`, `[ARXIV ID]`, `[EMAIL]` in `submission_cover_letter.md` | ⏳ |
| 11 | Email SIGMA editorial office | `editor@sigma-journal.com`, Subject = `Submission to SIGMA — arXiv:[ID] — …` | ⏳ |
| 12 | Update Zenodo deposit | Edit-record → add `isSupplementTo arXiv:[ID]` | ⏳ |
| 13 | Update manuscript front-matter | Add arXiv ID; commit and push | ⏳ |
| 14 | Log submission in SIARC ledger | `siarc/submitted/submission_log.txt §1 Active deposits` | ⏳ |

---

## E. Direct-email-only submission to SIGMA (exception path; viable backup if arXiv endorsement stalls)

SIGMA accepts direct-email submissions but only as an exception, and the author must explain why arXiv is not being used. "Unable to obtain an arXiv endorsement as a first-time independent submitter" is a plausible exceptional reason that SIGMA's editorial office is likely to accept.

**When to invoke this path:** if the endorsement request takes longer than 2 weeks to resolve, or if no suitable endorser can be located.

**Email payload for the exception path:**

```
To:       editor@sigma-journal.com
Cc:       sigmajournal@gmail.com  (only if no acknowledgement in 2 working days)
Subject:  Submission to SIGMA (direct) — The WKB Geometry of
          Newton Polygons (arXiv endorsement pending)

Attached:
  - manuscript.pdf             (898,187 B; 26 pp)
  - paper.tex                  (99,553 B)
  - paper.bbl                  (5,533 B)
  - references.bib             (8,753 B)
  - figures/taxonomy_tikz.tex  (4,792 B)
  - figures/constellations.png (141,890 B)
  - cover_letter.pdf           (~5 KB; includes an "arXiv endorsement
                                pending" paragraph explaining why
                                arXiv is not being used at submission
                                time)

Body: short version of cover letter + the endorsement-blocked
explanation paragraph (verbatim suggested wording below).
```

**Suggested explanation paragraph for the cover letter** (drop in between the abstract paragraph and the closing):

> *Per SIGMA's submission policy, I would ordinarily post the manuscript to arXiv first. As a first-time independent submitter to the `math-ph` category, however, my arXiv account has not yet obtained the required endorsement: my email is non-institutional and the manuscript is single-author, which closes both auto-endorsement paths. An endorsement request is open with members of the `math-ph` community, and I will post to arXiv as soon as it is granted. In the meantime I am submitting the manuscript directly per SIGMA's exception-path policy. The full supplementary archive is permanently available via Zenodo DOI [10.5281/zenodo.20387847](https://doi.org/10.5281/zenodo.20387847) and the GitHub mirror at <https://github.com/papanokechi/wkb-newton-polygons>.*

**After SIGMA acceptance via the exception path**, once endorsement is eventually granted, post to arXiv and link it back via Zenodo's `isSupplementTo` relation. Camera-ready proceeds normally regardless of submission route.

— *End of file list.*
