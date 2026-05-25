# Major-Revision Self-Verification Checklist

**Manuscript:** *The WKB Geometry of Newton Polygons: A Functorial Classification Theory*  
**Revision target:** v2.0 (post-referee, pre-resubmission)  
**Author:** Papanokechi

This checklist is to be worked through before the resubmission is sent
back to the journal. Each item is a binary verification step; if any
box is unchecked, the resubmission is not ready.

---

## A. Theorem and proof completeness

| ☐ | Item |
|---|------|
| ☐ | Theorem 3.1 (Main) — proof intact, no regressions, $\boxed{\chi(c) = \chi_w(c^q)}$ display preserved. |
| ☐ | Theorem 4.1 (M1, per-edge factorisation) — full proof in §4, *not* a "proof sketch". |
| ☐ | Theorem 4.1 — Lemma 4.0 (multiplicativity of $\chi$ across formal direct sums) inserted *before* Theorem 4.1, with its own proof. |
| ☐ | Theorem 4.1 proof steps explicitly labelled: (1) Levelt–Turrittin slope decomposition; (2) per-edge Main Theorem; (3) iterated Lemma 4.0; (4) genericity. |
| ☐ | Theorem 4.2 (N1, nested ramification) — proof intact, references to Lemma 4.0 if appropriate. |
| ☐ | Theorem 5.1 (D2, Kummer dichotomy) — **restated** to remove the bounded-search window from the hypothesis. |
| ☐ | Theorem 5.1 proof — Kummer-theoretic argument with the field tower $\mathbb{Q}(\zeta_q) \subset \mathbb{Q}(\zeta_q)(w_1, \dots, w_r) \subset \cdots \subset \mathbb{Q}(\zeta_q)(w_1, \dots, w_r)(z_1, \dots, z_r)$ explicit, citing Lang, *Algebra*, Ch. VI, Thm. 9.1. |
| ☐ | Theorem 5.1 corroboration — bounded-search statistics moved to Remark 5.x ("Bounded-search corroboration"), clearly labelled. |
| ☐ | Theorem 5.1 — composite-$q$ extension remark (Remark 5.y) retained. |
| ☐ | Theorem 6.1 (S1) — proof intact. |
| ☐ | Theorem 7.1 (AT1) — full proof in §7, *not* a "proof sketch". |
| ☐ | Theorem 7.1 proof steps explicitly labelled: (1) Levelt–Turrittin on $x = t^q$; (2) anti-Stokes leading-term form; (3) real-part calculation $\mathrm{Re}(\Delta_{ij}\, t^p) = \rho^p |\Delta_{ij}| \cos(\arg \Delta_{ij} + p\phi)$; (4) $2p \binom{N}{2}$ total count; (5) projection $t \mapsto t^q$; (6) determinacy. |
| ☐ | Theorem 7.1 — Remark 7.x ("Beyond the leading term") added, separating skeleton from Stokes multipliers. |
| ☐ | Theorems 7.2 (AT3), 7.3 (AT5), 7.4 (AT7) — proofs intact, scope statements ("$\mu_{q'}$-equivariance, not WCV theorem") preserved. |

---

## B. Functoriality and category-theoretic language

| ☐ | Item |
|---|------|
| ☐ | §1.1 ("The constellation map") states explicitly that the earlier draft used "functor" informally. |
| ☐ | Definition 1.1 (category $\mathfrak{L}$, category $\mathfrak{C}$, functor $\Fclass \colon \mathfrak{L} \to \mathfrak{C}$) is precise and complete. |
| ☐ | Remark 1.2 includes the disclaimer "no statement in the paper depends on the morphism part of $\Fclass$". |
| ☐ | Every prose use of "functor" in the body refers either to Definition 1.1 directly or to the informal "constellation map" reading; "functor" does *not* appear undefined anywhere after §1.1. |
| ☐ | The phrase "constellation map" is used in §2–§8 wherever only the object-level assignment is at stake. |

---

## C. Taxonomy diagram and figures

| ☐ | Item |
|---|------|
| ☐ | Figure 1 (taxonomy) — TikZ-rendered, no `\fbox{...}` placeholder remains. |
| ☐ | Figure 1 four-level structure: slope class $(p, q)$ → rank $r$ → generic vs. four named degeneracies → multi-edge / nested / system / arithmetic sub-strata. |
| ☐ | Figure 1 has visible class labels matching the 23-class atlas in the body and the 39-class refinement. |
| ☐ | Figure 2 (constellation zoo, `constellations.png`) — present, captioned, referenced from §8. |
| ☐ | Figure cross-references (`\Cref{fig:taxonomy}`, `\Cref{fig:zoo}`) compile cleanly. |
| ☐ | `code/render_taxonomy.tex` is included in the Zenodo dataset v1.0 (referenced from the Reproducibility note). |

---

## D. Notation and conventions

| ☐ | Item |
|---|------|
| ☐ | Table 1 (Notation) — inserted at the end of §2, lists every symbol used in §1–§8 (at least $\op, \opD, \opS, \opT, \LCinf, \NL, \chi, \chi_w, \Cl, \Fclass, \mu_q, \zeta_q, \Delta_{ij}, \mathcal{A}^{\mathrm{cov}}, \mathcal{A}^{\mathrm{base}}, \mathrm{MW}, \mathrm{Sym}^n, \mathfrak{S}_n$). |
| ☐ | Each notation-table row has: symbol, definition, section/equation of first use. |
| ☐ | §1.7 (Roadmap) references Table 1 explicitly. |
| ☐ | All macros referenced in proofs are defined in the preamble (no undefined macro errors). |

---

## E. $\chi_w$ ↔ classical edge-indicial polynomial

| ☐ | Item |
|---|------|
| ☐ | §1.3 ("$\chi_w$ as the edge-indicial polynomial") exists and is at least one paragraph. |
| ☐ | The text identifies $\chi_w$ as the classical edge-indicial polynomial in the variable $w = c^q$. |
| ☐ | Wasow, Sibuya, Sabbah cited at the point of identification. |
| ☐ | The paragraph distinguishes "novelty of $\chi_w$" (none) from "novelty of $\chi(c) = \chi_w(c^q)$" (the identity). |

---

## F. Open-stratum hypotheses (OS3 in particular)

| ☐ | Item |
|---|------|
| ☐ | §7.1 (OS1)–(OS5) are listed as a bulleted environment. |
| ☐ | (OS3) explicitly reads "no two distinct $\mu_q$-orbits of unordered pairs produce the same $\arg \Delta_{ij}$ modulo $\pi/p$" (or equivalent precise wording). |
| ☐ | A footnote or remark gives the example of $\mu_q$-forced coincidences within a single ring. |
| ☐ | The dependencies "Theorem 7.1 uses (OS1)–(OS3)", etc. are still listed at the end of §7.1. |

---

## G. Calibrated novelty

| ☐ | Item |
|---|------|
| ☐ | Abstract — between 180 and 220 words inclusive (count verified). |
| ☐ | Abstract foregrounds the four genuinely new pieces: $\chi_w$-pullback identity; $23 \to 39$ stratified atlas; $\mu_q/\mu_{q'}$ symmetry bookkeeping; $p$-visibility. |
| ☐ | Abstract does **not** claim new analytic theorems for the $\mu_q$-equivariant repackaging of Levelt–Turrittin. |
| ☐ | Abstract does **not** claim new wild-character-variety theorems. |
| ☐ | §1.5 ("Scope of the analytic refinement") exists, with three bullets: classical content, algebraic refinement, equivariance-not-WCV. |
| ☐ | §1.6 ("What is and is not classified") explicitly disclaims classification of operators. |

---

## H. Counterexamples / dichotomy boundary in-text

| ☐ | Item |
|---|------|
| ☐ | Remark following Theorem 4.1 records the inter-edge equal-radius counterexample boundary, in prose (no `\texttt{MULTI_*}` label). |
| ☐ | Remark following Theorem 5.1 records the bounded-search corroboration, labelled as corroboration. |
| ☐ | Remark following Theorem 6.1 records the system-discriminant counterexample boundary, in prose. |
| ☐ | Remark following Theorem 7.1 records the four degenerate locus types: discriminant, equal-modulus, zero-root, $\omega$-resonance, in prose. |

---

## I. No dataset-internal identifiers in prose

| ☐ | Item |
|---|------|
| ☐ | A repository-wide grep for `STRESS_`, `MULTI_`, `NEST_`, `CTRL_`, `OMEGA_`, `GAL_`, `CE-`, `phase[0-9]_`, `_v[0-9]+`, `phase[0-9]+_[a-z]+\.json` returns no hits in any `\section`, `\subsection`, theorem body, remark body, or figure caption of `paper.tex`. |
| ☐ | Dataset citations use descriptive labels (e.g., "stress-test STR-equalmod entry of the companion dataset") rather than `\texttt{STRESS\_equalmod}`. |
| ☐ | The `\cite[...]{wkb_dataset_v1}` calls still resolve to the same Zenodo record but with human-readable inline anchors. |

---

## J. Cross-references and compilation

| ☐ | Item |
|---|------|
| ☐ | `pdflatex` runs cleanly (no errors). |
| ☐ | `bibtex` runs without "undefined citation" warnings. |
| ☐ | Three-pass build (`pdflatex` → `bibtex` → `pdflatex` × 2) produces a stable PDF with no "label changed, rerun" warnings. |
| ☐ | All `\Cref{thm:*}` references resolve. |
| ☐ | All `\Cref{sec:*}` references resolve. |
| ☐ | All `\Cref{fig:*}` references resolve. |
| ☐ | All `\Cref{tab:*}` references resolve (the new notation table). |
| ☐ | All `\cite{...}` references resolve. |
| ☐ | No `\fbox{...}` placeholders remain in the body. |
| ☐ | No `???` left in the body (typical "undefined reference" rendering). |
| ☐ | TikZ figure (`fig:taxonomy`) compiles standalone. |

---

## K. Bundles and reproducibility

| ☐ | Item |
|---|------|
| ☐ | `arxiv_bundle/paper.tex` updated to the v2.0 file. |
| ☐ | `journal_bundle/paper.tex` updated to the v2.0 file. |
| ☐ | Workspace master `wkb-newton-polygons/paper/paper.tex` updated. |
| ☐ | Three bundles all produce byte-identical PDFs (or, if intentional differences, documented in `submission_checklist.md`). |
| ☐ | Reproducibility note (§11) is up to date — references to `code/render_taxonomy.tex` if the rendered figure is included. |
| ☐ | Zenodo v1.0 DOI placeholder still in place (will be replaced at upload). |
| ☐ | Disclosure section (§ "Computational and AI Disclosure") unchanged in placement; if the new theorems are added, the `\Cref{...}` list in paragraph 4 is updated to include any newly added theorem labels. |

---

## L. Document hygiene

| ☐ | Item |
|---|------|
| ☐ | No commented-out drafts (`%%% TODO`, `%%% OLD`) left in `paper.tex`. |
| ☐ | No duplicated equation labels. |
| ☐ | No duplicated theorem labels (`thm:M1`, `thm:N1`, `thm:D2`, `thm:S1`, `thm:AT1`, `thm:AT3`, `thm:AT5`, `thm:AT7` each appear exactly once as `\label{...}`). |
| ☐ | Bibliography entries unchanged (no spurious additions). |
| ☐ | Author block, ORCID, affiliation unchanged from the v1.0 metadata-alignment pass. |

---

## M. Final pre-submission

| ☐ | Item |
|---|------|
| ☐ | `response_to_referee_letter.md` proofread, addressed to the journal handling editor. |
| ☐ | Page count after revision recorded in `submission_checklist.md` (expected: 21–23 pages, up from 20). |
| ☐ | A clean fresh clone of the workspace can build the v2.0 PDF without intervention. |
| ☐ | `disclosure_section_patch.txt`, `author_metadata_patch.txt`, `major_revision_patch.diff` collected in `major_revision/` for the editor's audit trail. |
| ☐ | A clean copy of the v2.0 PDF is attached to the resubmission cover email. |

---

## Sign-off

Once every box above is checked:

| Date checked | Reviewer | Signed off |
|--------------|----------|------------|
|              | Papanokechi |   ☐        |

Resubmit only after all boxes above are checked.
