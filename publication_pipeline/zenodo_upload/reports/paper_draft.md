# Paper Draft Artifacts — "The WKB Geometry of Newton Polygons: A Classification Theory"

> Notation lock: L (operator); D, S, T (derivation, shift, q-shift); N(L) (Newton polygon at ∞);
> dominant edge of slope −p/q with gcd(p,q)=1; rank multiplier r; χ(c), χ_w(w);
> C(L) = Roots(χ); μ_q = q-th roots of unity; ζ_q = e^{2πi/q}; F : L ↦ C(L) the constellation functor.


## 1. ABSTRACT

Local linear operators with one irregular singularity—differential, difference, or q-difference—are organised, via the WKB ansatz over the dominant Newton edge, by a discrete invariant: the *exponent constellation* $\mathcal{C}(L) \subset \mathbb{C}$. We promote this organisation to a functorial classification. Writing $\mathsf{F} \colon L \mapsto \mathcal{C}(L)$ from scalar local models with one dominant Newton edge to finite multisets in $\mathbb{C}$ taken up to global rotation, we determine the image of $\mathsf{F}$ and the structure of its fibres.

The main structural law is algebraic. If the dominant Newton edge has slope $-p/q$ in lowest terms and the edge contains $r{+}1$ lattice points, then the WKB characteristic polynomial factors as
$$\chi(c) \;=\; \chi_w(c^q),$$
where $\chi_w \in \mathbb{C}[w]$ has degree $r$. Consequently
$$\mathcal{C}(L) \;=\; \bigsqcup_{w_i \in \mathrm{Roots}(\chi_w)} \mu_q \cdot w_i^{1/q},$$
a $\mu_q$-equivariant pullback of the inner spectrum $\mathrm{Roots}(\chi_w)$ along $c \mapsto c^q$. The image of $\mathsf{F}$ is therefore a stratified space whose generic stratum, indexed by tuples $(p,q,r)$, contains finite-multiset configurations of $r$ concentric $q$-gons; the deeper strata correspond to equal-modulus collisions, multiplicities in $\chi_w$, and zero roots.

An automated sweep over $89$ representative operators—five slopes $p/q$, three ranks $r$, four valuation patterns, three equation types, plus four hand-built degeneracy probes—yields **23** distinct constellation classes. Vieta's identity refines to a per-ring monodromy law $\sum_k m_k \Delta_k \equiv \theta \pmod{2\pi}$ under the gauge $\beta \mapsto e^{i\theta}\beta$ of the leading coefficient.

The contribution is a classification of the functor itself, not of the operators feeding it: a discrete geometry of WKB images, with explicit generic and special strata, intrinsic monodromy, and equation-type-invariant combinatorics.


## 2. OUTLINE

**1. Introduction and Motivation** (≈3 pages)
- Pose the problem: organise the space of locally irregular linear operators by their dominant WKB content.
- Define the functor $\mathsf{F}$ informally; preview the main structural law $\chi(c)=\chi_w(c^q)$.
- State scope: one dominant Newton edge, single irregular singularity at $\infty$, scalar operators, three equation types.
- *Vision paragraph (§7)* closes the introduction.

**2. Preliminaries: Newton Polygons at the Irregular Singularity** (≈4 pages)
- Newton polygon $N(L)$ as the upper convex hull of $\{(k,\deg a_k)\}$; conventions for $\infty$ vs. $0$.
- Slopes, edges, ramification denominator $q$, rank multiplier $r$, lattice points on the edge.
- Parallel statements for $D$, $S$, $T$ with the same combinatorial Newton recipe.
- Visual lemma: every edge of slope $-p/q$ in lowest terms has lattice points exactly at $(rq{-}jq,\,jp)$ for $0\le j\le r$.

**3. The WKB Characteristic Polynomial and its Factorisation** (≈4 pages)
- Derive $\chi(c)=\sum_{(k,d)\in\text{edge}} \mathrm{LC}_\infty(a_k)\,c^k$ from leading-order WKB balance.
- *Main Theorem (§3 of this document)* and its proof.
- Discussion of normalisation across operator types: $c \leftrightarrow f'/f$ for ODE, $\log(Sf/f)$ for difference, $\log_q(Tf/f)$ for q-difference; the combinatorial $\chi$ is invariant, the *analytic* meaning of $c$ is not.

**4. The Constellation Functor $\mathsf{F}$ and its Image** (≈4 pages)
- Define $\mathsf{F}$ precisely; specify the target category (finite multisets in $\mathbb{C}$ modulo global rotation, with discriminant data).
- Image stratification: open stratum (distinct $|w_i|$), discriminant stratum (multiplicities), equal-modulus stratum, zero-root locus.
- Fibres of $\mathsf{F}$ over a fixed constellation: equation-type-invariance theorem (combinatorial form), with the analytic caveat. *(Conjectures.md, §Observation 5.)*

**5. Classification: The 23 Constellation Classes** (≈5 pages, the bulk of the paper)
- Indexing: $(q, r, \pi)$ where $\pi$ is the multiplicity-with-modulus partition of the $r$ roots of $\chi_w$.
- The taxonomy diagram (§4 of this document) lives here as the principal figure.
- Catalogue: each of the 23 classes with $(q,r,\pi)$, representative $\chi$, and pointer to figure panel.
- Computational artifacts: `constellations.json`, `clusters.json` cited; full table in an appendix.

**6. Generic vs. Degenerate Strata** (≈3 pages)
- Generic stratum: $r$ concentric $q$-gons.
- Four named degenerate strata, each illustrated by a stress test:
  - *Equal-modulus* (`STRESS_equalmod`),
  - *Resonant multiplicity* (`STRESS_doubleroot`),
  - *Zero-root* (`STRESS_zeroroot`),
  - *Accidental symmetry* (`STRESS_accidental_sym`).
- Statement and proof that the 23 classes cover the union of the open stratum and the four named degenerate strata for $p/q\in\{1/2,1/3,1/4,2/3,3/2\}$ and $r\le 3$.
- Stress-test figure panels (the bottom row of the constellation zoo figure).

**7. Monodromy: Vieta Lifts and the Per-Ring Sum Rule** (≈3 pages)
- Lemma (Vieta monodromy): $\arg\prod c_k$ shifts by $\theta$ when $\beta\mapsto e^{i\theta}\beta$.
- Per-ring rotation $\Delta_k$ is defined $\bmod\,2\pi/m_k$; the well-defined lift $m_k\Delta_k$ obeys $\sum_k m_k\Delta_k\equiv \theta\pmod{2\pi}$.
- Worked examples on the open stratum and on `STRESS_doubleroot` (resonance forces a logarithmic correction).
- Reference: `conjectures.md`, Corollaries 4, 4a, 4b.

**8. Examples and a Reproducibility Note** (≈2 pages)
- Walkthrough of three operators, one per equation type, with the full pipeline output.
- Software note: `fleet.py` and the artifacts `operators.json`, `newton.json`, `chi.json`, `constellations.json`, `clusters.json`, `conjectures.md`, `constellations.png` are bundled.
- Reproducibility: deterministic pipeline; no random seeds.

**9. Discussion and Future Directions** (≈2 pages)
- Beyond one dominant edge: multi-edge Newton polygons and stratification by edge sequences.
- Systems: matrix operators, root systems on edges, links to wild character varieties.
- The functor $\mathsf{F}$ as a classification primitive: what additional Stokes data (phases, lines) refine it.
- Open: a sharp converse to the constellation classification.


## 3. MAIN THEOREM

**Theorem 1 (Factorisation of the WKB characteristic polynomial).**
Let $L = \sum_{k=0}^{n} a_k(x)\,\square^k$ be a scalar linear operator with polynomial coefficients $a_k \in \mathbb{C}[x]$ and a single irregular singularity at $x = \infty$, where $\square$ denotes one of $D = d/dx$, the shift $S$, or the $q$-shift $T$. Assume the Newton polygon $N(L)$ at $\infty$ has a unique dominant edge $E$ of slope $-p/q$ with $\gcd(p, q) = 1$ and $p, q \ge 1$, containing $r + 1$ lattice points
$$E \cap \mathbb{Z}^2 = \big\{(rq - jq,\; jp) : 0 \le j \le r\big\}.$$
Define
$$\alpha_j \;:=\; \mathrm{LC}_\infty\!\left(a_{rq - jq}\right) \qquad (0 \le j \le r),$$
the leading $x$-coefficient at $\infty$, and the WKB characteristic polynomial
$$\chi(c) \;:=\; \sum_{j=0}^{r} \alpha_j\, c^{(r-j)q} \;\in\; \mathbb{C}[c].$$
Then the inner polynomial
$$\chi_w(w) \;:=\; \sum_{j=0}^{r} \alpha_j\, w^{\,r-j} \;\in\; \mathbb{C}[w], \qquad \deg \chi_w = r,$$
satisfies $\chi(c) = \chi_w(c^q)$, and the WKB exponent constellation factors as the $\mu_q$-equivariant fibre product
$$\boxed{\;\mathcal{C}(L) \;=\; \mathrm{Roots}(\chi) \;=\; \bigsqcup_{w_i \in \mathrm{Roots}(\chi_w)} \big\{\, c \in \mathbb{C} : c^q = w_i \,\big\}\;}$$
where roots are counted with multiplicity and the union is over the $r$ roots $w_i$ of $\chi_w$.

**Corollary 1 (Generic ring decomposition).** Suppose the moduli $|w_1|, \ldots, |w_r|$ are pairwise distinct and all $w_i \ne 0$. Then $\mathcal{C}(L)$ consists of exactly $r$ concentric $\mu_q$-orbits ("rings") of $q$ points each, with radii $|w_i|^{1/q}$ and angular bases $\arg(w_i)/q \pmod{2\pi/q}$.

**Corollary 2 (Vieta monodromy).** Fix $\alpha_0$ and let $\beta := \alpha_r$ vary. Under $\beta \mapsto e^{i\theta}\beta$,
$$\arg\!\left(\prod_{c \in \mathcal{C}(L)} c\right) \;\longmapsto\; \arg\!\left(\prod_{c \in \mathcal{C}(L)} c\right) \;+\; \theta \pmod{2\pi}.$$
If $\mathcal{C}(L)$ admits a $\mu_q$-equivariant ring decomposition $\mathcal{C}(L) = \bigsqcup_{k=1}^{s} R_k$ with $|R_k| = m_k$, and the rings deform rigidly under the variation of $\beta$ with rotations $\Delta_k$ (each defined modulo $2\pi/m_k$), then the unambiguous lifts $m_k \Delta_k \in \mathbb{R}/2\pi\mathbb{Z}$ obey
$$\sum_{k=1}^{s} m_k \Delta_k \;\equiv\; \theta \pmod{2\pi}.$$

**Remark (Degenerate loci).** The clean ring picture of Corollary 1 fails on three explicit subvarieties of the coefficient space $(\alpha_0, \ldots, \alpha_r)$:
*(i)* the *discriminant locus* $\{\mathrm{disc}\,\chi_w = 0\}$, where roots of $\chi_w$ coalesce and ring multiplicities exceed $q$;
*(ii)* the *equal-modulus locus* $\{|w_i| = |w_j|\text{ for some } i \ne j\}$, where distinct $\mu_q$-orbits merge into a single radius with non-uniform angular distribution—an extension of the ring picture that survives Corollary 2 only after replacing "rigid rotation" with "rigid permutation up to a shared rotation";
*(iii)* the *zero-root locus* $\{\alpha_r = 0\}$, where $c = 0$ enters the constellation with multiplicity $q$ and the dominant edge itself jumps.
The first stratum carries resonance / logarithmic Stokes data; the second is responsible for the apparent regularity of `STRESS_equalmod` (a six-point constellation on one circle that is *not* a regular hexagon); the third is a wall-crossing of the Newton polygon itself.


## 4. TAXONOMY DIAGRAM SPEC

**Title:** *The $\mathsf{F}$-image stratification: 23 constellation classes.*

**Overall geometry.** A $4 \times 4$ "atlas" grid plus a detached "degeneracy island" at the lower right, on a single landscape page.

**Atlas axes.**
- *Horizontal axis (columns):* $q \in \{2, 3, 4\}$ — the cyclic-symmetry order forced by the slope denominator. Slope numerator $p$ is *not* an axis because, by the Main Theorem, the constellation depends on $\chi_w$ alone, which is independent of $p$; representatives at $p/q = 1/q$ and $(q{-}1)/q$ etc. occupy the same cell.
- *Vertical axis (rows):* $r \in \{1, 2, 3\}$ — the rank multiplier. Increasing $r$ moves downward.
- One auxiliary column at far left labelled "$r=1$" spans all $q$ (the rank-$1$ slice has trivial rank structure and is rendered as a single row of three cells across the top).

**Cell structure.** Each $(q, r)$ cell with $r \ge 2$ is subdivided into three sub-tiles indexed by the *valuation pattern* of $\chi_w$:
- *Simple* (top tile): only $\alpha_0, \alpha_r \ne 0$. One regular $rq$-gon (single ring of $rq$ points).
- *Double* (middle tile): one interior $\alpha_j \ne 0$. Two-radius generic pattern *or*, on the discriminant locus, a single-radius merger.
- *Mixed/Generic* (bottom tile): all $\alpha_j \ne 0$. Generic stratum: $r$ rings of $q$ points each; real-coefficient stratum: equal-modulus mergers from complex-conjugate $w$-pairs.

Each sub-tile bears a thumbnail of the canonical constellation (small filled discs, unit-circle reference).

**Encoding of generic vs. special.**
- *Generic stratum:* solid black thumbnails, framed in a thin black border. Class label in serif (e.g. "$(q,r,\pi)=(3,2,1{+}1)$").
- *Real-coefficient mergers:* same thumbnail but framed in dashed grey. Label includes a parenthetical "(real)".
- *Single-ring collapses* of multi-rank operators (e.g. mixed/$r=2$ over reals giving one ring of $2q$): grey background fill.
- *Accidental-symmetry inflation:* corner badge "$\,C_{m}\!\supsetneq\!C_q$" with the actual symmetry $m$ stated.

**Degeneracy island.** A boxed inset, drawn slightly detached from the atlas with a connecting arrow, holding the four stress-test classes as a $1 \times 4$ row:
1. `STRESS_equalmod` (`equal-modulus`): one ring, $rq$ points, *non-uniform* angular distribution. Annotate with $|w_1| = |w_2| = |w_3| = 2$.
2. `STRESS_doubleroot` (`resonant multiplicity`): two rings $[m_1, m_2]$ where one ring carries a multiplicity-$2$ marker (drawn as a doubled disc).
3. `STRESS_zeroroot` (`zero-root collapse`): one ring + a starred origin (multiplicity-$q$ root at $c=0$); annotated with "$\chi_w(0)=0$".
4. `STRESS_accidental_sym` (`enhanced symmetry`): regular $rq$-gon with $C_{rq}$ badge instead of expected $C_q$.

**Connectors and arrows.**
- Vertical arrows within each column indicate the *resolution-of-degeneracy direction:* small perturbations of $\chi_w$ coefficients move a constellation upward, from a degenerate stratum to the generic stratum of the same $(q, r)$.
- An arrow from the degeneracy island to its parent atlas cell, labelled with the codimension-$1$ relation: `equalmod` $\to (q, r)=(2,3)$, `doubleroot` $\to (3,3)$, `zeroroot` $\to (2,2)$ via $\alpha_r{=}0$ (wall-crossing of the dominant edge), `accidental_sym` $\to (2,3)$.

**Legend block.** Bottom-left, four entries:
- "Disc = simple root of $\chi$ at radius $|w_i|^{1/q}$";
- "Doubled disc = multiplicity-$2$ root";
- "Star at origin = zero-root sector";
- "Dashed border = real-coefficient stratum".

**Caption.** *Figure 1. The constellation atlas. The functor $\mathsf{F}$ has image stratified by $(q, r, \pi)$ with $\pi$ the modulus-multiset of $\mathrm{Roots}(\chi_w)$. Generic strata are bordered solid; codimension-one collapses (real-coefficient, multiplicity, accidental symmetry) appear as labelled deformations. The degeneracy island collects the four named stress-test classes that fall outside the open stratum.*


## 5. CONSTELLATION ZOO FIGURE LAYOUT

**Figure 2.** *Representative constellations across the $\mathsf{F}$-image.*

**Grid:** $3 \times 4$, landscape, occupying a full page. Panel side $\approx$ 4.5 cm. Inter-panel gap 0.6 cm. Top row = open stratum (simple/binomial), middle row = intermediate ranks, bottom row = stress tests.

**Panel-by-panel specification:**

| # | Class label | Operator (representative) | What to plot |
|---|---|---|---|
| **A1** | $(q,r,\pi) = (3, 1, *)$ | `ODE_s1o3_r1_simple`: $\chi = c^3 + 1$ | 3 filled discs on the unit circle at angles $\pi/3, \pi, 5\pi/3$. Light dotted unit-circle reference. |
| **A2** | $(4, 2, 1{+}1\text{-collapsed})$ | `ODE_s1o4_r2_simple`: $\chi = c^8 + 1$ | Regular $8$-gon on the unit circle. |
| **A3** | $(2, 3, 1{+}1{+}1\text{-collapsed})$ | `ODE_s1o3_r2_simple`: $\chi = c^6 + 1$, slope $1/3$, $r{=}2$ | Regular $6$-gon on the unit circle. Newton-polygon-predicted $q = 3$. |
| **A4** | $(3, 3, 2{+}1)$ generic | `ODE_s1o3_r3_double`: $\chi = c^9 + c^6 + 1$ | Two concentric rings, $6$ + $3$ points. Use **two distinct colours** for the two rings; label radii. |
| **B1** | $(3, 3, 1{+}1{+}1)$ real-mixed | `ODE_s1o3_r3_mixed`: $\chi = 1 + c^9 + 3 c^6 + 4 c^3$ | One ring of $3$ + one ring of $6$ (the latter is the complex-conjugate pair merger). Two colours; dashed border on the figure to signal *real-coefficient stratum*. |
| **B2** | $(4, 3, 1{+}1{+}1)$ generic complex | `ODE_s1o4_r3_generic_complex` | Three concentric $4$-gons. Three colours. The hallmark generic-stratum image. |
| **B3** | $(3, 3, 1{+}1{+}1)$ generic complex | `ODE_s1o3_r3_generic_complex` | Three concentric $3$-gons. |
| **B4** | $(3, 2, 1{+}1)$ generic complex | `ODE_s2o3_r3_generic_complex` (or 2/3, r=3) | Three concentric $3$-gons; identical class to B3 (illustrates that the slope numerator $p$ is invisible to $\mathcal{C}(L)$). |
| **C1** | `STRESS_equalmod` $(2, 3, 3)$ | $\chi = c^6 - 2 c^4 + 4 c^2 - 8$ | Six points on a single circle of radius $\sqrt{2}$, *not* evenly spaced. Overlay a faint regular hexagon in grey to highlight the angular mismatch. |
| **C2** | `STRESS_doubleroot` $(3, 3, 2{+}1)$ | $\chi = c^9 - 4 c^6 + 5 c^3 - 2$ | Two rings $[6, 3]$; render the inner ring as **doubled discs** (each apparent disc is a multiplicity-$2$ root) to encode the resonance. |
| **C3** | `STRESS_zeroroot` $(2, 2, 1{+}0)$ | $\chi = c^4 - c^2$ | One ring of $2$ at radius $1$, plus a **star** at the origin marking the multiplicity-$2$ zero. Annotate "$c = 0$, mult. $q = 2$". |
| **C4** | `STRESS_accidental_sym` | $\chi = c^6 + 1$, slope $1/2$ | Regular hexagon; *badge* "$C_6 \supsetneq C_2$". Visually identical to A3 but appears in a slope-$1/2$ context: this juxtaposition is the entire point of the panel. |

**Common annotations on every panel.**
- Light-grey unit circle as visual scale.
- Axes lines $\mathrm{Re}\,c$ and $\mathrm{Im}\,c$ drawn faintly through the origin.
- Title: class label in monospace (e.g. `(3,3,2+1)`) above the panel.
- Sub-caption beneath each panel: rotational symmetry $C_n$ and ring-count vector $[m_1, \ldots, m_s]$.
- Top row (A1–A4) shares one colour scheme (single-ring class = black, multi-ring = qualitative palette); bottom row (C1–C4) uses a distinct colour family (warm tones) to flag degeneracy.

**Reusable artefact.** The panels are produced by `plot_constellations.py`; supplying the class list above and the $\chi$ representatives yields the rendered figure already saved as `constellations.png`. A higher-resolution version is generated by re-running with `dpi=200`.

**Caption.** *Figure 2. Twelve panels covering the principal strata of the $\mathsf{F}$-image. Top row: simple (binomial) class — single regular polygon, the class characterised by a single Galois orbit of $\chi_w$. Middle row: double and generic-complex classes — two or three concentric $\mu_q$-orbits. Bottom row: four degenerate strata exhibiting equal-modulus merger, root multiplicity, zero roots, and accidental cyclic enhancement. Panels A3 and C4 are visually identical 6-gons — the same multiset $\mathcal{C}(L) = \{e^{i\pi(2k+1)/6}\}_{k=0}^{5}$ — but live in different cells of the atlas: A3 has slope $1/3$ (Newton-polygon-predicted minimum symmetry $C_3$ enhanced to $C_6$), while C4 has slope $1/2$ (predicted $C_2$ enhanced to $C_6$). The constellation alone does not recover the cell; the Newton-polygon-derived denominator $q$ is required. This is the visible signature that $\mathsf{F}$ is many-to-one and that "accidental symmetry" is a feature, not a bug, of every simple-class operator.*


## 6. RELATED WORK

The classification we develop sits adjacent to, but is structurally orthogonal to, four established programmes. As a *methodological* precedent we take the ADE classification of simple singularities (Arnol'd, Brieskorn) and of finite subgroups of $SU(2)$: a small discrete invariant—a Dynkin diagram—organises an apparently heterogeneous zoo of analytic objects, with strata governed by simple-root combinatorics and degenerations corresponding to root-system collisions. Our 23 constellation classes occupy an analogous slot: a finite combinatorial atlas indexed by the discrete data $(p, q, r, \chi_w)$, with degenerate strata produced by collisions among the $w_i$ (the analogue of root coincidences). Unlike the ADE setting, our classes are not labelled by Dynkin diagrams—the relevant combinatorics is the partition of $\chi_w$'s roots by modulus and Galois orbit—but the *style* of classification (discrete invariants, stratified moduli, degeneration loci) is closely modelled on it.

The Levelt–Turrittin theorem and its descendants (Sabbah, Mochizuki) give a *formal* classification of meromorphic connections by *irregular type*: a multiset of exponential factors $e^{P_i(x^{1/q})}$ together with regular-singular twists. Birkhoff–Trjitzinsky and the q-difference theories of Sauloy, Ramis, and Zhang play the parallel role for difference and q-difference operators. Each of these theories classifies *the operator* up to formal or analytic equivalence. Our object is different: we classify the *image* of the WKB-extraction functor $\mathsf{F}$, i.e. the discrete geometry that a Newton polygon and its leading edge coefficients deposit on the complex plane. The connection is one-way: the Levelt–Turrittin/Birkhoff–Trjitzinsky exponents are recovered from $\mathcal{C}(L)$ together with auxiliary phase data, but $\mathcal{C}(L)$ itself is coarser and admits a clean independent classification.

A third neighbour is the Stokes-graph classification of Painlevé and other low-rank equations (Kawai–Takei, Iwaki–Nakanishi, Aoki–Kawai–Takei), and more broadly the spectral-network programme of Gaiotto–Moore–Neitzke. There, classification proceeds via the *combinatorial topology of Stokes lines* in the complex plane, which depends on $c_i - c_j$ rather than $|c_i|$. Our ring-modulus partition is therefore *not* a Stokes invariant and does not reproduce spectral-network combinatorics; instead it captures the strictly weaker but exact information of the multiset $\{c_i^q\}$. This makes $\mathsf{F}$ a coarsening of the spectral-network functor, which we view as an asset: the coarser invariant is computable directly from Newton-polygon data and admits a closed-form classification, whereas Stokes graphs in general do not.

The fourth neighbour is the geometry of *wild character varieties* and the irregular Riemann–Hilbert correspondence (Boalch, Sabbah, Mochizuki). Those theories produce moduli stacks parametrising local data of irregular connections; our $\mathsf{F}$-image is, in essence, a discrete shadow of such a stack restricted to scalar operators with one dominant edge. We do not attempt to lift the present classification to the level of stacks or to incorporate Stokes structures; rather, we exhibit a self-contained classification of the discrete part of the local data and indicate, in the discussion, the natural enrichments. The contribution is best understood as building a separately classifiable layer of the local picture—a "Newton-polygon WKB stratum"—on which the analytic theories can subsequently be erected.


## 7. VISION PARAGRAPH

The natural object of study, in our view, is not any individual operator but the *constellation functor* $\mathsf{F}$ itself: the map from locally-irregular linear models to their WKB exponent multisets. Once $\mathsf{F}$ is named, the questions become geometric—what is its image, what are its fibres, what are its strata, how does it deform—and admit answers in closed form when restricted to one dominant Newton edge. The 23 classes catalogued here populate the lowest-dimensional cells of $\mathrm{Im}(\mathsf{F})$; their adjacencies trace out the discriminant, equal-modulus, and zero-root walls along which the structure changes. The natural sequel is to walk the same programme up the complexity ladder: multi-edge Newton polygons (where $\mathsf{F}$ acquires a slope-filtration target), matrix and meromorphic-connection systems (root systems on each edge, with wild character varieties as the codomain), and the analytic refinement that attaches Stokes phases to each $\mu_q$-orbit, lifting the discrete constellation to a full irregular-Riemann–Hilbert datum. In each enlargement, the classifiable object is the functor, and the discrete combinatorics of the constellation continues to sit transversally to the analytic theory—coarser, computable, and structurally separable. We expect this functorial reframing to be useful precisely because it makes a single, universal target geometry visible behind a great many local stories that, treated one at a time, have looked unrelated.
