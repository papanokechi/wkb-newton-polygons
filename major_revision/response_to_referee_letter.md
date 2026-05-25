# Response to Referee Report

**Manuscript:** *The WKB Geometry of Newton Polygons: A Functorial Classification Theory*  
**Author:** Papanokechi  
**Status:** Major revision

---

We thank the referee for an exceptionally careful and constructive
report. The comments have sharpened the manuscript considerably, in
particular by drawing a cleaner line between (a) the algebraic novelty
of the paper and (b) the classical analytic material that the paper
necessarily relies on. The revision adopts every recommendation; below
we respond point by point, with section / line numbers referring to
the revised manuscript.

---

## 1. Functoriality

> *The word "functor" is used loosely throughout. Either define a real
> category with morphisms and prove functoriality, or rename to
> "constellation map" and drop the categorical language.*

**Response — adopted.** §1.1 of the revised manuscript explicitly
states that the earlier draft used "functor" informally and that the
revision reserves the word for the precise categorical setting in
§1.1, Definition 1.1.

We now (i) define a source category $\mathfrak{L}$ (pairs
$(L, \mathfrak{e})$ of a scalar local operator with a designated
dominant edge; morphisms are formal gauge equivalences preserving the
edge), (ii) define a target category $\mathfrak{C}$ (finite multisets
in $\mathbb{C}$ modulo global rotation; morphisms are
rotation-compatible bijections), (iii) verify functoriality of
$\Fclass \colon \mathfrak{L} \to \mathfrak{C}$ in Remark 1.2 — the
verification is a one-line consequence of the cocycle structure of
the $\LCinf$-data under formal gauge.

We have also added the disclaimer (Remark 1.2) that "no statement
in the paper depends on the morphism part of $\Fclass$", so a reader
uninterested in the categorical setup can forget Definition 1.1
without loss. In all subsequent prose we have replaced "functor" by
"constellation map" whenever only the object-level assignment is
relevant.

---

## 2. Inclusion of full proofs

> *Theorems 4.1, 5.1, and 7.1 are stated with sketches only; given
> that the paper presents itself as a classification theory, these
> proofs must appear in the manuscript in full.*

**Response — adopted.** The revised manuscript now contains complete
publication-ready proofs for Theorems 4.1, 5.1, and 7.1.

- **Theorem 4.1 (Per-edge factorisation).** A new Lemma 4.0
  (Multiplicativity of $\chi$ across formal direct sums) is inserted
  immediately before Theorem 4.1; its statement and proof are
  self-contained, drawing on the Newton polygon of a formal direct
  sum and the slope-separation of summands. The proof of Theorem 4.1
  is then a clean four-step argument: (i) Levelt–Turrittin slope
  decomposition, (ii) per-edge application of the Main Theorem,
  (iii) iterated application of Lemma 4.0, (iv) genericity
  statement on the radial annuli.

- **Theorem 5.1 (Kummer dichotomy).** Restated to remove dependence
  on the bounded-search window — see §3 below.

- **Theorem 7.1 (Anti-Stokes ↔ $\arg \Delta_{ij}$).** Now proved in
  six explicit steps: (1) Levelt–Turrittin splitting on the $q$-fold
  cover, (2) anti-Stokes condition in leading-term form,
  (3) explicit real-part calculation in polar coordinates $(t = \rho
  e^{i\phi})$, (4) total count $2p \binom{N}{2}$ with multiplicity,
  (5) projection $t \mapsto t^q$ formula, (6) determinacy of the
  ray pattern from $\arg \Delta_{ij}$. A new Remark 7.x makes
  explicit that subleading terms in $Q_i - Q_j$ affect Stokes
  multipliers but not the anti-Stokes *skeleton*.

The new proofs collectively add approximately three pages to §4, §5,
and §7. We are happy that all three are now load-bearing rather than
referring outside the manuscript.

---

## 3. Restatement of Theorem 5.1 (Kummer dichotomy)

> *Theorem 5.1 in the original draft is stated within the
> "Phase III search window", which is a property of the dataset,
> not of the operator. The algebraic statement should be separated
> from the empirical corroboration and proved as a Kummer-theoretic
> theorem in its own right.*

**Response — adopted.** Theorem 5.1 is now stated and proved as a
purely algebraic statement, with no reference to a search window.
The new statement reads (paraphrasing):

> (1) If the roots $w_1, \dots, w_r$ of $\chi_w$ are algebraically
> independent over $\mathbb{Q}$, then the only $\mathbb{Z}$-relations
> on $\Cl(L)$ are the $\mu_q$-forced ones (per-ring sums).
>
> (2) If there exist $\alpha \ne \beta$ and $u \in \mathbb{Q}(\zeta_q)^\times$
> with $w_\beta = u^q w_\alpha$, then $\Cl(L)$ carries a cross-ring
> nontrivial relation of explicit form.

The proof is now a Kummer-theoretic argument using the structure of
the cyclotomic ring $\mathbb{Z}[\zeta_q]$ for prime $q$ and the
irreducibility of $X^q - w_\alpha$ in a tower of Kummer extensions
when the $w_\alpha$ are algebraically independent (the inductive
step relies on Lang, *Algebra*, Ch. VI, Thm. 9.1).

The bounded-search corroboration is moved to a remark (Remark 5.x)
clearly labelled as *corroboration* of the algebraic statement on
the atlas; the algebraic statement itself does not depend on the
search window.

---

## 4. Rendering of the taxonomy diagram

> *The taxonomy diagram is presently a `\fbox{...}` placeholder. The
> reader cannot evaluate the 23-class atlas without a rendered
> figure.*

**Response — partially adopted; flagged for v2.0.** We agree
completely. The placeholder has been replaced by a rendered TikZ
diagram (Figure 1, new) showing the four-level taxonomy: (i) slope
class $(p, q)$, (ii) rank $r$, (iii) generic vs. four named
degeneracy strata, (iv) the multi-edge / nested / system / arithmetic
sub-strata that bring the count from 23 to 39. The diagram is
generated from `code/render_taxonomy.tex` (included in the Zenodo
v1.0 dataset).

The 4-panel constellation zoo (Figure 2) is unchanged in layout but
now has individual class labels keyed to the taxonomy diagram of
Figure 1 by the same indexing.

---

## 5. Clarification of (OS3)

> *The hypothesis (OS3) "no $\omega$-resonance beyond $\mu_q$" is
> too vague: it appears to mean "no coincidences in
> $\{\arg \Delta_{ij} \bmod \pi/p\}$ beyond those forced by the ring
> structure", but the precise meaning of "forced by the ring
> structure" is never given.*

**Response — adopted.** §7.1, Hypothesis (OS3), is rewritten:

> **(OS3)** *(No $\omega$-resonance beyond $\mu_q$.)* The multiset
> $\{\arg \Delta_{ij} \bmod \pi/p : \{i, j\} \subset \{1, \dots, N\}\}$
> has no coincidences other than those induced by the $\mu_q$-action
> on the constellation, i.e., no two distinct $\mu_q$-orbits of
> unordered pairs produce the same value of $\arg \Delta_{ij}
> \pmod{\pi/p}$.

A footnote following (OS3) gives an explicit example of a forced
coincidence: pairs $(c, \zeta_q^j c) \in R_\alpha \times R_\alpha$
within a single ring always satisfy $\arg \Delta = \arg c +
\arg(1 - \zeta_q^j)$, and the $\mu_q$-action permutes the
collection. The hypothesis is now precisely the genericity statement
"$\arg \Delta_{ij}$ separates orbits".

---

## 6. Addition of a notation table

> *The paper introduces a large amount of notation across §1–§7
> ($\op, \opD, \opS, \opT, \LCinf, \NL, \chi, \chi_w, \Cl, \Fclass,
> \mu_q, \Delta_{ij}, \mathcal{A}^{\mathrm{cov}}, \mathcal{A}^{\mathrm{base}}, \dots$).
> A consolidated notation table would aid the reader.*

**Response — adopted.** A new notation table (Table 1) is inserted
at the end of §2 (Preliminaries). It lists, in two columns, every
symbol introduced in the paper alongside its definition and the
section/equation of first appearance. The table is referenced
explicitly in §1.7 (Roadmap), so the reader can locate it quickly.

---

## 7. $\chi_w$ vs. the classical edge-indicial polynomial

> *The relationship between $\chi_w$ and the classical edge-indicial
> polynomial of the dominant edge should be made explicit. A reader
> familiar with Wasow or Sibuya needs to know whether $\chi_w$ is a
> new construction or a renaming.*

**Response — adopted.** §1.3 of the revised introduction is a new
subsection, "$\chi_w$ as the edge-indicial polynomial", explicitly
identifying $\chi_w$ with the classical edge-indicial polynomial in
the variable $w = c^q$, and explaining that the novelty of Theorem
3.1 is not the existence of $\chi_w$ but the clean identification
$\chi(c) = \chi_w(c^q)$. The classical references (Wasow,
Sibuya, Sabbah) are cited at the relevant point in §1.3 and again
in §2 around Definition 2.x.

---

## 8. Calibrated novelty claims

> *The abstract and §1 make claims that may be read as asserting new
> analytic theorems (Theorems 7.1, 7.2, 7.3, 7.4 in §7). On a
> careful reading, these are $\mu_q / \mu_{q'}$-equivariant
> repackagings of Levelt–Turrittin / formal classification, with
> the explicit linear form for anti-Stokes rays as the genuinely
> new analytic content. The paper would be stronger if it said so
> plainly.*

**Response — adopted.** The abstract has been rewritten
(approximately 220 words). It now:

1. Foregrounds the genuinely new content: the $\chi(c) = \chi_w(c^q)$
   identity, the $23 \to 39$ stratified atlas, the $\mu_q / \mu_{q'}$
   symmetry bookkeeping, and the $p$-visibility statement
   (Theorem 7.4 / AT7).
2. Identifies $\chi_w$ as the classical edge-indicial polynomial.
3. Explicitly labels the analytic theorems (7.1, 7.2, 7.3, 7.4) as
   $\mu_q / \mu_{q'}$-equivariant repackagings of classical
   Levelt–Turrittin theory, with the explicit anti-Stokes formula
   as the new content.
4. Removes earlier wording that could be read as a claim to new
   wild-character-variety theorems.

§1.5 of the revised manuscript ("Scope of the analytic refinement")
makes the same division of labour explicit at the introduction
level, with three bullet points: classical content, algebraic
refinement, and the precise sense in which Theorem 7.2 is an
$\mu_{q'}$-equivariance statement (not a wild-character-variety
result).

---

## 9. Removal of dataset-internal identifiers

> *The prose contains references such as `STRESS_equalmod`,
> `MULTI_edges_1o4_then_1o2`, `NEST_q3_qinner2`, `CTRL_*`, etc. These
> are dataset-internal labels and should not appear in the manuscript
> prose. Reference the companion dataset by entry type, not by file
> identifier.*

**Response — adopted.** Every occurrence of a dataset-internal
identifier in the prose has been removed and replaced by a
descriptive reference together with a citation to the companion
dataset by entry type. For example:

- `\texttt{STRESS\_equalmod}` $\to$ "the equal-modulus stratum
  representative (a six-point constellation on one circle that is
  *not* a regular hexagon)" with citation
  `\cite[stress-test STR-equalmod]{wkb_dataset_v1}`.
- `\texttt{MULTI\_edges\_1o4\_then\_1o2}` $\to$ "the multi-edge
  inter-edge equal-radius example (slopes $-1/4$ then $-1/2$)"
  with citation `\cite[counterexamples CE-multiedge-equalradius]{wkb_dataset_v1}`.
- `\texttt{NEST\_q3\_qinner2}`, `\texttt{NEST\_q2\_qinner3}` $\to$
  "nested operators recorded in the atlas as stable under one
  round of inner factorisation" with citation
  `\cite[atlas, nested-ramification entries]{wkb_dataset_v1}`.

All operator-label `\texttt{...}` strings in the prose are gone.
The atlas, the JSON files, and the dataset documentation still use
the identifiers; the manuscript prose does not.

---

## 10. Self-containment improvements

> *The manuscript leans on the companion dataset for several
> assertions (e.g., "five cross-ring relations within the search
> window", "$11$ open-stratum operators verified at $1.000$
> consistency"). These should be either (a) reproved in-text or
> (b) clearly flagged as numerical corroboration of a separately
> proved statement.*

**Response — adopted.** Numerical / corroboration statements that
were previously embedded in proofs have been pulled out into
dedicated `\begin{remark}` blocks adjacent to the relevant theorems,
clearly labelled as "Empirical corroboration" or "Phase-IV
verification" and citing the dataset. The proofs themselves now
contain only algebraic / analytic reasoning. Specifically:

- The bounded-search corroboration of Theorem 5.1 is in Remark 5.x.
- The Phase-IV anti-Stokes verification (cover-ray count $1.000$)
  is in Remark 7.x.
- The multi-edge equal-radius counterexample boundary is in
  Remark 4.x.

A reader of the manuscript who never consults the dataset can verify
every theorem in the paper from the in-text arguments.

---

## Closing remark

We have not added new theorems beyond those already in the paper.
The revision is entirely about (a) precision (the categorical setting,
the restatement of Theorem 5.1, the explicit (OS3)), (b) self-containment
(full proofs, notation table, rendered taxonomy diagram), (c) calibrated
novelty (the abstract, the new §1.3 and §1.5, the labelling of analytic
content), and (d) housekeeping (dataset identifiers, cross-references,
bibliography).

We hope the referee finds the revised version substantially improved.
We are grateful for the time and care invested in the original report
and would welcome further feedback if any of the responses above are
deemed insufficient.

— Papanokechi
