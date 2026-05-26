# SIGMA Submission Package — Summary

**Target journal:** SIGMA (Symmetry, Integrability and Geometry: Methods and Applications)
**URL:** <https://www.emis.de/journals/SIGMA/>
**Submission portal:** <https://www.emis.de/journals/SIGMA/submit.html>
**Submission type:** Research article
**Assembled:** 2026-05-26

---

## At-a-glance metadata

| Field | Value |
|---|---|
| **Title** | The WKB Geometry of Newton Polygons: A Functorial Classification Theory |
| **Author** | Papanokechi (mononym) — Independent Researcher |
| **ORCID** | [0009-0000-6192-8273](https://orcid.org/0009-0000-6192-8273) |
| **Email** | *(TO ADD before submission — see manuscript_compliance_report.md §2 Issue 2)* |
| **Affiliation** | Independent Researcher, Yokohama, Japan |
| **arXiv link** | *PLACEHOLDER — to be assigned at arXiv submission; suggested primary `math-ph`* |
| **Zenodo DOI (dataset)** | `10.5281/zenodo.20387847` · concept `10.5281/zenodo.20387846` |
| **GitHub repo** | <https://github.com/papanokechi/wkb-newton-polygons> |
| **GitHub release** | <https://github.com/papanokechi/wkb-newton-polygons/releases/tag/v2.0> |
| **MSC2020 (primary)** | 34M40 (Stokes phenomena, connection problems, isomonodromic deformation) |
| **MSC2020 (secondary)** | 34M30, 34M35, 39A06, 39A13 |
| **Page count** | 26 |
| **Manuscript file size** | 99,553 B source / 898,187 B PDF |
| **License (manuscript)** | CC-BY-4.0 |
| **License (code + data)** | MIT (code/fleets) + CC-BY-4.0 (text/figures/data atlas) |

---

## Files to submit through the SIGMA portal

| Slot | File | Source | Notes |
|---|---|---|---|
| Primary manuscript PDF | `manuscript.pdf` | `paper/manuscript.pdf` (898,187 B) | 26 pp, camera-ready |
| Primary manuscript TeX | `manuscript.tex` (or `paper.tex`) | `paper/manuscript.tex` (99,553 B) | Standalone — SIGMA can recompile |
| Bibliography database | `references.bib` | `paper/references.bib` (8,753 B) | 24 entries, `alpha` style |
| Pre-built bibliography | `paper.bbl` | `paper/paper.bbl` (5,533 B) | Lets SIGMA skip `bibtex` |
| Figure 1 (taxonomy) | `figures/taxonomy_tikz.tex` | `figures/taxonomy_tikz.tex` (4,792 B) | TikZ source, `\input`-ed |
| Figure 2 (atlas) | `figures/constellations.png` | `figures/constellations.png` (141,890 B) | 300 DPI raster |
| **Cover letter** | `cover_letter.pdf` | *PLACEHOLDER — see template below* | 1 page |
| Supplementary archive | `wkb-newton-polygons-zenodo-v2.0.zip` | `publication_pipeline/wkb-newton-polygons-zenodo-v2.0.zip` (2,090,144 B) | Optional — SIGMA accepts a Zenodo DOI in lieu of attaching the zip |

---

## Cover letter — template (to finalise)

The text below is a single-page submission cover letter, written for the SIGMA editor-in-chief panel (which rotates across the SIGMA editorial board). Customise the `[EDITOR NAME]` and dating before submission.

```
Subject: Submission to SIGMA — "The WKB Geometry of Newton Polygons:
         A Functorial Classification Theory"

[DATE]

Dear [EDITOR NAME] and the SIGMA editorial board,

I am pleased to submit the manuscript "The WKB Geometry of Newton
Polygons: A Functorial Classification Theory" for consideration in
SIGMA.

The paper establishes a constellation functor F that sends each scalar
linear operator L with one irregular singularity at infinity to its
WKB exponent constellation C(L), via the identity chi(c) = chi_w(c^q)
on the dominant Newton-polygon edge. Built from a 23-operator atlas
that is expanded to 39 via systematic stratification (Phases I-V of
the paper), F is shown to be naturally compatible with mu_q-pullbacks,
multi-edge filtrations, ramified covers (Levelt-Turrittin), and the
analytic anti-Stokes skeleton. The main results are eight
theorem-proof pairs (M1, N1, D2, S1, AT1, AT3, AT5, AT7) that bridge
the formal Newton-polygon picture and the analytic wild character
variety.

The work fits SIGMA's scope at the intersection of irregular ODEs,
Stokes phenomena, and Frobenius/character-variety geometry. It is
written in a constructively reproducible style: all 39 operators, the
clustering, the analytic skeleton, and the proofs are accompanied by
an open atlas (Zenodo DOI 10.5281/zenodo.20387847) and a GitHub
repository (https://github.com/papanokechi/wkb-newton-polygons)
that re-derives every figure and table.

The Computational and AI Disclosure section (Section *) declares the
use of GitHub Copilot CLI + Anthropic Claude as a structured-search
and exposition aid; all theorems, proofs, and verifications are the
human author's. The dataset is dual-licensed CC-BY-4.0 (text + atlas)
+ MIT (code + fleets).

This manuscript has not been submitted elsewhere and is not under
review at another journal.

Yours sincerely,

Papanokechi
ORCID 0009-0000-6192-8273
Independent Researcher, Yokohama, Japan
Email: [EMAIL]
```

**Action:** save as `publication_pipeline/sigma_submission/cover_letter_template.txt` (also shipped alongside this report) and finalise with the editor's name, date, and email before submission.

---

## Keywords

(Identical to manuscript L137–140 — paste into SIGMA's "Keywords" form field:)

```
WKB analysis; Newton polygon; irregular singularity; formal classification;
Levelt–Turrittin; Stokes phenomenon; anti-Stokes directions;
wild character variety; functorial classification; μ_q-pullback
```

10 keywords, semicolon-separated.

---

## Abstract (paste-ready)

(From manuscript L101–134; 175 alpha-words, well under SIGMA's typical ≤ 220 ceiling.)

> We develop a constellation functor F that classifies scalar linear operators L with one irregular singularity at infinity by their dominant Newton-polygon edge. For each such L of dominant slope −p/q (with gcd(p, q) = 1) and rank multiplier r, the characteristic polynomial of the WKB balance factors as χ(c) = χ_w(c^q), where χ_w(w) of degree r is the inner polynomial. The constellation C(L) = Roots(χ) is naturally μ_q-equivariant, and the assignment L ↦ C(L) extends to a functor F on a category of scalar linear operators with morphisms generated by μ_q-pullbacks, direct sums, multi-edge filtrations, ramified covers, and resonance-preserving deformations. Building on a 23-operator atlas (Phase I), the atlas is expanded to 39 operators (Phase III) and a 12-row invariant-lifting table is established between Newton-polygon data and the analytic anti-Stokes skeleton (Phase IV). The main classification results are eight theorem-proof pairs (M1, N1, D2, S1, AT1, AT3, AT5, AT7) consolidating: a multiplicativity / Levelt-Turrittin block-decomposition (M1), the visible μ_lcm(q,q') symmetry of fibre constellations (N1), the cross-ring Kummer-cyclotomic locus (D2), a slope-filtration / Stokes-structure compatibility (S1, AT5), and the analytic counterparts: the anti-Stokes/Δ-argument correspondence on the ramified cover (AT1), nested μ_qq'-symmetry of wild data (AT3), and the p-visibility theorem (AT7) that gives the exact formula 2pq(r + qC(r,2)) for the within-ring direction count.

---

## Reproducibility & AI-Disclosure summary

- **Reproducibility (manuscript §11 + §Reproducibility of the AI Disclosure):** every figure, table, and theorem statement in the paper is regenerable from the public Zenodo deposit `10.5281/zenodo.20387847` (dataset atlas + fleet scripts) and the GitHub repo `papanokechi/wkb-newton-polygons` (release v2.0). The deterministic pipeline (fleets/fleet.py … fleet5.py) takes < 30 s on a stock laptop to re-derive the Phase I–V atlas.
- **AI disclosure (manuscript §Computational and AI Disclosure):** five roles of AI assistance are demarcated explicitly: (i) structured search across the atlas, (ii) candidate-conjecture filtering against the 11-stratum counterexample knowledge base, (iii) LaTeX drafting and notation-locking, (iv) pipeline scaffolding, (v) typo / cross-reference linting. The author certifies that every theorem, proof, hypothesis, and counterexample stratum is the human author's work; AI was used as a structured-search and exposition aid, not as a mathematical authority.

---

## Submission flow checklist

| # | Step | Owner | Status |
|---|---|---|---|
| 1 | Run DOI propagation script with live Zenodo DOI | author | ⏳ |
| 2 | Add email + postal affiliation to manuscript front-matter | author | ⏳ |
| 3 | Finalise cover letter (editor name, date, email) | author | ⏳ |
| 4 | Post arXiv preprint from `arxiv_bundle/` | author | ⏳ |
| 5 | Back-propagate arXiv ID into manuscript + Zenodo `isSupplementTo` row | author | ⏳ |
| 6 | Final 4-pass compile; verify 26-pp / 0-errors | author | ⏳ |
| 7 | Submit via SIGMA portal | author | ⏳ |
| 8 | Log submission in `siarc/submitted/submission_log.txt` (§1 Active deposits) | SIARC ledger | ⏳ |

---

## Companion files in this folder

| File | Purpose |
|---|---|
| `manuscript_compliance_report.md` | Field-by-field manuscript audit (Issue 1 = DOI, Issue 2 = email, Issue 3 = version labels) |
| `zenodo_sufficiency_report.md` | Supplementary archive audit (PASS — record live & complete) |
| `arxiv_readiness_report.md` | arXiv bundle audit (PASS WITH MINOR POLISH — needs DOI propagation) |
| `sigma_submission_readiness.md` | Final consolidated verdict |
