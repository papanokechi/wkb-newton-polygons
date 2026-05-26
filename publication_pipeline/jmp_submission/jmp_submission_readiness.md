# JMP Submission Readiness — Final Verdict

**Date:** 2026-05-26
**Target:** Journal of Mathematical Physics (AIP Publishing)
**Manuscript:** *The WKB Geometry of Newton Polygons: A Functorial
Classification Theory*

---

## Verdict

> 🟢 **PASS WITH MINOR POLISH — ready to submit after ~ 15 minutes of
> portal-form completion and (optionally) DOI propagation.**

The manuscript is technically and structurally ready for JMP. The
AI-policy rewrite this turn (Task 2) clears the only substantive
policy concern. The remaining blockers are corresponding-author email
(supplied at portal-form time) and the DOI placeholder cleanup
(optional; can be run with one command).

There is **no arXiv-endorsement gate** for JMP (in contrast to SIGMA),
so submission can proceed immediately once the corresponding-author
email is supplied.

---

## Status by component

| Component | Status | Notes |
|-----------|--------|-------|
| **Manuscript compliance** (`jmp_manuscript_audit.md`) | 🟢 PASS WITH MINOR POLISH | 22 checks, 17 PASS, 4 MINOR, 1 BLOCKER (email — portal field) |
| **AI disclosure rewrite** (`ai_disclosure_rewrite.diff`) | 🟢 DONE | 5 manuscript copies updated; 4 new roles; AI-not-used-for-math statement explicit |
| **Metadata consistency** (`metadata_consistency_report.md`) | ⚠ MINOR POLISH | DOI placeholder in 23 sites outside §AI Disclosure; CITATION.cff has 1 stale-relic row |
| **Cover letter** (`jmp_cover_letter.md`) | 🟢 DRAFTED | AIP-style; significance, originality, AI disclosure summary |
| **Submission metadata** (`jmp_submission_metadata.md`) | 🟢 DRAFTED | Portal-paste-ready; abstract 195/250 words |
| **Supplement list** (`jmp_supplement_list.md`) | 🟢 DRAFTED | 6-file portal upload + Zenodo DOI citation |
| **Submission checklist** (`jmp_submission_checklist.md`) | 🟢 DRAFTED | 10-step Editorial Manager workflow |

---

## Action list (in suggested execution order)

### Immediate (5 minutes)

1. **Compile-verify the post-rewrite manuscript.** ✅ **VERIFIED THIS TURN.**
   ```
   cd journal_bundle
   pdflatex paper.tex && bibtex paper && pdflatex paper.tex && pdflatex paper.tex
   ```
   **Result:** 26 pages, **886,457-byte PDF**, **0 errors, 0 LaTeX
   warnings, 0 undefined refs/cites, 0 undefined references**, 2
   pre-existing cosmetic BibTeX warnings (unchanged). Confirmed for
   journal_bundle/, paper/, and arxiv_bundle/ — all three produce
   identical 886,457-byte PDFs.

   *Side-fix applied this turn:* `\usepackage{tikz}` +
   `\usetikzlibrary{positioning, fit, arrows.meta}` added to the
   preamble of all 5 manuscript copies. The `taxonomy_tikz.tex`
   figure required these but they were missing from the preambles
   (pre-existing bug, predates Task 2).

2. **Decide on corresponding-author email.** Suggested:
   `ppapanokechi@gmail.com` if no institutional email exists. Add at
   Editorial Manager registration time.

### Minor polish (15 minutes; recommended but not blocking)

3. **Run the DOI propagation script** to replace the remaining 23
   placeholder sites:
   ```
   bash publication_pipeline/doi_propagation_commands.sh 10.5281/zenodo.20387847
   ```
   This updates: 5 manuscript header comments, 5 §11 Reproducibility
   notes, 3 references.bib copies, paper.bbl, README.md badge +
   BibTeX block, and 5 CITATION.cff sites.

4. **Fix CITATION.cff bug** — delete lines 54–56 referencing the
   unrelated Khinchin paper `10.5281/zenodo.20355904`. (Manual edit;
   see `metadata_consistency_report.md` §4.)

5. **Cosmetic cleanups:**
   - `\date{(preprint v1.0)}` → `\date{\today}` (paper.tex L92)
   - Remove "will be added in the camera-ready version (v2.0)" from
     Acknowledgements (paper.tex L2061–2062)
   - Extend author-footnote URL from `github.com/papanokechi` to
     `github.com/papanokechi/wkb-newton-polygons` (paper.tex L89)

6. **Commit + push minor-polish changes** to GitHub.

### Portal submission (30–45 minutes)

7. **Register / log in** to AIP Editorial Manager
   (`https://www.editorialmanager.com/jmp/`).

8. **Follow the 10-step workflow** in `jmp_submission_checklist.md` §E.

9. **Receive manuscript ID** and acknowledgement email; record in
   `submission_log.txt`.

---

## Why we are not blocked

Compared with the SIGMA submission path (which is gated by arXiv
endorsement; see `publication_pipeline/sigma_submission_final/`), the
JMP submission path is **unblocked** for the following reasons:

| Concern | SIGMA | JMP |
|---------|-------|-----|
| arXiv endorsement required | yes (math-ph; 3–14 days lead time; depends on identifying an endorser) | no — direct portal submission |
| Cover-letter style | technical / declarative | "significance-to-field" emphasis (drafted in `jmp_cover_letter.md`) |
| Author email required at submission | no (arXiv→email model) | yes (Editorial Manager field) |
| Supplement upload model | arXiv ancillary files | external DOI citation (Zenodo) + small portal slot |
| AI policy | conservative (SIGMA = MDPI-adjacent style) | COPE-aligned (AIP standard) — rewrite this turn complies |
| Open-access option | green-OA standard | optional (CC-BY, with APC) |
| Estimated time-to-first-decision | 6–12 weeks | 6–10 weeks |

The JMP path imposes no exogenous gate (no endorsement, no minimum
preprint, no community membership). All preparation is under the
author's direct control and is complete or near-complete in this
folder.

---

## Files in this folder

```
publication_pipeline/jmp_submission/
├── ai_disclosure_rewrite.diff          (5-file unified diff, ~ 22 KB)
├── jmp_cover_letter.md                  (AIP-style cover letter)
├── jmp_manuscript_audit.md              (22-row compliance audit)
├── jmp_submission_checklist.md          (10-step portal workflow)
├── jmp_submission_metadata.md           (portal-paste metadata)
├── jmp_submission_readiness.md          (this file)
├── jmp_supplement_list.md               (upload list + Zenodo citation)
└── metadata_consistency_report.md       (cross-file DOI / URL audit)
```

Manuscript-side artifacts (modified this turn):
```
paper/manuscript.tex                     (§AI Disclosure rewritten + DOI baked in)
paper/paper.tex                          (same)
arxiv_bundle/paper.tex                   (same)
journal_bundle/paper.tex                 (same)
major_revision/followup/paper_v2_1.tex   (same)
```

---

## Sign-off

The work for the Task-2 §AI Disclosure rewrite is complete and
verified. The Tasks 1, 3, 4, 5 deliverables are written. The author
can proceed to portal submission as soon as the corresponding-author
email is supplied. The DOI-propagation cleanup is recommended but not
required for the JMP submission to be accepted.

**Recommended next action:** open Editorial Manager, register an
account with `0009-0000-6192-8273` (ORCID) and the corresponding
email, then follow `jmp_submission_checklist.md` §E step-by-step.
