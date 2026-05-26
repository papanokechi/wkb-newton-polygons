# JMP / AIP Editorial Manager Submission Checklist

**Target:** Journal of Mathematical Physics (AIP Publishing)
**Portal:** AIP Editorial Manager — `https://www.editorialmanager.com/jmp/`
**Article type:** Research Article
**Manuscript:** *The WKB Geometry of Newton Polygons: A Functorial
Classification Theory*

---

## A — Pre-submission requirements

| ✓ | Item | Status | Where |
|---|------|--------|-------|
| [ ] | Editorial Manager account active | TODO | new registration; corresponding-author email required |
| [ ] | ORCID linked to account | TODO | 0009-0000-6192-8273 |
| [ ] | Corresponding-author email confirmed | TODO | (insert at portal-form time) |
| [ ] | Postal address for corresponding author | TODO | "Independent researcher, Yokohama, Japan" or comparable |
| [x] | No prior submission to JMP or other AIP journals | ✅ | confirmed first-time submission |
| [x] | No prior journal submission elsewhere | ✅ | confirmed |
| [x] | No arXiv preprint (or arXiv preprint disclosed) | ✅ | no preprint; declared in cover letter |
| [x] | All co-authors notified | n/a | single-author manuscript |

---

## B — Manuscript files (uploaded to Editorial Manager)

| ✓ | Slot | File | Status |
|---|------|------|--------|
| [x] | Cover letter | `cover_letter.pdf` (render from `jmp_cover_letter.md`) | drafted in this folder |
| [x] | Manuscript PDF | `journal_bundle/paper.pdf` (898,187 B, 26 pages) | exists |
| [x] | Manuscript TeX source | `journal_bundle/paper.tex` (99,553 B) | exists, AI disclosure rewritten |
| [x] | Bibliography source | `journal_bundle/references.bib` | exists |
| [x] | Bibliography compiled | `journal_bundle/paper.bbl` | exists |
| [x] | Figure file | `journal_bundle/figures/constellations.png` | exists |
| [ ] | Supplementary file (optional) | Zenodo DOI cited inline instead | done |
| [ ] | Highlights / graphical abstract | not required for JMP | n/a |

**Total upload set:** 6 files, < 2 MB. Zenodo deposit referenced by DOI.

---

## C — Metadata fields (portal form)

| ✓ | Field | Source |
|---|-------|--------|
| [x] | Title | `jmp_submission_metadata.md` |
| [x] | Running title (≤ 50 chars) | `jmp_submission_metadata.md` |
| [x] | Author name | Papanokechi |
| [x] | Affiliation | "Independent Researcher" |
| [ ] | Corresponding-author email | **TODO at portal-form time** |
| [x] | ORCID | 0009-0000-6192-8273 |
| [x] | Abstract (≤ 250 words) | 195 words, in `jmp_submission_metadata.md` |
| [x] | Keywords (5–20) | 19 keywords supplied |
| [x] | MSC2020 codes | 5 codes (34M30, 34M40, 34M03, 12H05, 14M99) |
| [x] | PACS / arXiv class | not required by JMP, but `math-ph` primary noted |
| [x] | Suggested reviewers | placeholder area in cover letter |
| [x] | Opposed reviewers | none |
| [x] | Funding declaration | "None declared" |
| [x] | Conflict of interest | "None" |
| [x] | Data availability statement | drafted, points to Zenodo DOI |
| [x] | AI-assistance declaration | drafted, points to §Computational and AI Disclosure |

---

## D — Policy compliance

| ✓ | Policy | Status |
|---|--------|--------|
| [x] | AIP / COPE AI-policy compliance | ✅ post-rewrite: AI used only in 4 supporting roles, no AI-authored math content, AI not listed as author |
| [x] | AIP authorship criteria (CRediT) | ✅ single-author; author retains sole accountability |
| [x] | Conflict-of-interest disclosure | ✅ "none" declared |
| [x] | Funding disclosure | ✅ "none" declared |
| [x] | Data availability (FAIR principles) | ✅ Zenodo deposit, DOI-citable, CC-BY-4.0 / MIT licensed |
| [x] | Reproducibility | ✅ deterministic pipelines, JSON atlas, command sequence documented |
| [x] | Plagiarism / originality | ✅ first publication; no preprint; no overlap with author's prior work |
| [x] | Copyright | TODO at acceptance; AIP transfer-of-copyright form or CC-BY option (Open Access $$$) |

---

## E — Submission workflow (10 steps in Editorial Manager)

1. **Create / log in.** Editorial Manager → JMP submission portal.
2. **Select article type.** "Research Article".
3. **Upload manuscript.** Drag-drop `paper.pdf`, `paper.tex`,
   `references.bib`, `paper.bbl`, and the figure file. Mark
   `paper.pdf` as "Main Manuscript" and `paper.tex` as "Source File".
4. **Enter metadata.** Copy from `jmp_submission_metadata.md`:
   title, running title, abstract, keywords, MSC codes.
5. **Author block.** Single author, with email, ORCID, affiliation
   (postal location optional but recommended).
6. **Cover letter.** Upload PDF or paste content from
   `jmp_cover_letter.md`.
7. **Suggested reviewers.** Provide 3–5 names with affiliations and
   emails (author supplies at submission time).
8. **Declarations.** Fill funding, conflict-of-interest, data
   availability, and AI-disclosure fields (text from
   `jmp_submission_metadata.md`).
9. **Review submission summary.** Verify file list, metadata,
   declarations.
10. **Submit.** Confirm; receive manuscript ID and acknowledgement
    email.

---

## F — Typical review timeline (informational)

| Stage | Typical duration |
|-------|------------------|
| Editorial triage | 1–2 weeks |
| Peer review | 4–8 weeks |
| First decision | 6–10 weeks from submission |
| Revision round (if any) | author-paced |
| Acceptance to online publication | 2–4 weeks after acceptance |

JMP does *not* operate as an arXiv overlay; **no endorsement is
required** to submit (unlike SIGMA's arXiv-overlay model). Direct
portal submission is the canonical and only submission path.

---

## G — Post-acceptance to-do

1. Sign AIP transfer-of-copyright form (or pay APC for CC-BY OA).
2. Receive proofs from AIP production team (typically 1–3 weeks
   post-acceptance).
3. Final corrections → online publication with DOI.
4. Cross-post to arXiv `math-ph` if/when desired (no longer gated by
   the endorsement issue once the JMP DOI is live).
5. Update `CITATION.cff` and `README.md` with JMP DOI.
6. Add JMP citation to Zenodo deposit (`isPublishedIn` relation).
