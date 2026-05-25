# Theorem-Proof Consolidation for *The WKB Geometry of Newton Polygons*

This file collects eight theorem-proof pairs distilled from Phases I-IV of the
fleet investigation. They are intended for direct insertion into the paper draft
("The WKB Geometry of Newton Polygons: A Classification Theory") after
section-level integration; cross-references and section placement are recorded
in `integration_map.md`.

## Notation (consistent with paper_draft §1-3)

* $L$: scalar linear operator on $\mathbb{C}[x]$ with one irregular singularity at $x = \infty$;
  the irregular operator $\square$ is one of $D = d/dx$, the shift $S$, or the $q$-shift $T$.
* $N(L)$: Newton polygon of $L$ at $\infty$; $E_\alpha$ the edges, of slope $-p_\alpha/q_\alpha$
  with $\gcd(p_\alpha, q_\alpha) = 1$.
* $\mathrm{LC}_\infty$: leading coefficient at $\infty$ (the coefficient of the
  highest-degree monomial in $x$).
* $\alpha_j^{(\alpha)} = \mathrm{LC}_\infty(\text{coefficient of $\square^k$ for $(k, \cdot) \in E_\alpha$})$.
* $\chi^{(\alpha)}(c) = c^{k_0^{(\alpha)}} \chi_w^{(\alpha)}(c^{q_\alpha})$: per-edge WKB
  characteristic polynomial; $\chi_w^{(\alpha)}$ inner polynomial of degree $r_\alpha$.
* $\chi(c) = \prod_\alpha \chi^{(\alpha)}(c)$ in the multi-edge case; $\chi(c) = \chi_w(c^q)$
  in the single-edge case.
* $\mathcal{C}(L) := \mathrm{Roots}(\chi)$ the **constellation** of $L$.
* $\Delta_{ij} := c_i - c_j$ for $c_i, c_j \in \mathcal{C}(L)$, $i \ne j$.
* $\mu_q$ the group of $q$-th roots of unity; $\zeta_q := e^{2\pi i/q}$ primitive.
* $F : L \mapsto \mathcal{C}(L)$: the **classification functor**.
* $Q_i(t)$: irregular-type polynomial on the ramified cover $x = t^q$, with
  $Q_i(t) = c_i t^p + R_i(t)$, $\deg R_i < p$.
* $\mathrm{MW}(L)$: wild character variety of $L$ at $\infty$.

## Open-stratum hypotheses (used jointly in AT1, AT3, AT5, AT7)

* **(OS1)** $\chi_w$ is squarefree (discriminant nonzero).
* **(OS2)** $\chi_w(0) \ne 0$ (no zero-roots in $\mathcal{C}(L)$).
* **(OS3)** No $\omega$-resonance beyond $\mu_q$ (the multiset $\{\arg \Delta_{ij} \mod \pi/p\}$
  has no coincidences beyond those forced by ring structure).
* **(OS4)** For multi-edge $L$: per-edge radial annuli pairwise disjoint.
* **(OS5)** For multi-edge $L$: cross-edge leading coefficients nonzero (so the
  cross-edge degree formula of AT5 applies without correction).

## Scope

All theorems are stated for **scalar ODEs** (the $\square = D$ case). The
difference ($\square = S$) and $q$-difference ($\square = T$) versions of M1, N1, D2, S1
hold verbatim at the constellation level (they follow from the same algebraic
factorisation argument); the analytic theorems AT1, AT3, AT5, AT7 have direct
analogues in those settings but require separate analytic foundations
(Birkhoff-Trjitzinsky for difference operators; Ramis's
$\theta$-Stokes for $q$-difference) and are deferred.

---


## Theorem M1 (Per-edge factorisation, multi-edge generalisation).

### Hypotheses

\textbf{Hypotheses.} $L$ scalar, polynomial coefficients, one irregular singularity
at $x = \infty$, $N(L)$ multi-edge with edges of strictly increasing slope. The
formal direct-sum decomposition (Step 1) is unconditional; the multiset disjoint
union (Step 3) is unconditional; the \emph{set} disjoint union (Step 4) holds
on the open subset $U_{\mathrm{disj}}$.


### Statement

Let $L$ be a scalar linear operator with polynomial coefficients on $\mathbb{C}[x]$
and a single irregular singularity at $x = \infty$. Suppose $N(L)$ at $\infty$ has
edges $E_1, \ldots, E_m$ with pairwise distinct slopes $-p_\alpha / q_\alpha$
($\gcd(p_\alpha, q_\alpha) = 1$) and $r_\alpha + 1$ lattice points on $E_\alpha$.
Then:

\begin{enumerate}
  \item (Slope decomposition.) The formal differential module $\widehat{M}(L)$
  associated to $L$ admits a canonical slope decomposition into slope-graded
  pieces $\widehat{M}_1, \ldots, \widehat{M}_m$, with $\widehat{M}_\alpha$ of
  pure slope $p_\alpha / q_\alpha$. Passing back from formal modules to cyclic
  vectors, $\widehat{M}_\alpha$ corresponds to a single-slope scalar operator
  $L_\alpha$ (well-defined up to formal gauge), so we may write
  $\widehat{L} \simeq L_1 \oplus \cdots \oplus L_m$ in the sense of formal
  modules.

  \item (Per-edge characteristic polynomial.) Each $L_\alpha$ satisfies the
  Phase-I Main Theorem with $\chi^{(\alpha)}(c) = c^{k_0^{(\alpha)}}\,
  \chi_w^{(\alpha)}\!\big(c^{q_\alpha}\big)$, where $k_0^{(\alpha)}$ is the
  height of $E_\alpha$ above the $c$-axis and $\chi_w^{(\alpha)}$ is the inner
  polynomial of degree $r_\alpha$ built from $\mathrm{LC}_\infty$ of the
  $E_\alpha$ coefficients.

  \item (Total factorisation.) Define
  $\chi(c) := \prod_{\alpha=1}^{m}\, \chi^{(\alpha)}(c)$. Then
  $\mathcal{C}(L) = \bigsqcup_{\alpha=1}^{m}\, \mathcal{C}_\alpha$ as
  multisets, with $\mathcal{C}_\alpha = \mathrm{Roots}(\chi^{(\alpha)})$.
\end{enumerate}

\noindent\textbf{Genericity.} On the open subset of coefficient space where
the per-edge radial annuli $\big[\rho_\alpha^{\min},\, \rho_\alpha^{\max}\big]$
with $\rho_\alpha^{\bullet} = |w_\bullet^{(\alpha)}|^{1/q_\alpha}$ are pairwise
disjoint, the union is in fact a disjoint union of \emph{distinct} subsets of
$\mathbb{C}$.


### Proof

\textbf{Step 1 (Slope decomposition).} By the formal-classification theorem of
Levelt-Turrittin (the scalar case of which is recorded in Sabbah's
\emph{Isomonodromic Deformations and Frobenius Manifolds}, Chapter II, or in
Wasow's \emph{Asymptotic Expansions for ODEs}, Chapter VII), the formal
differential module $\widehat{M}(L)$ associated to $L$ at $x = \infty$ decomposes
canonically as a direct sum
$$\widehat{M}(L) \;\simeq\; \bigoplus_{\alpha = 1}^{m} \widehat{M}_\alpha,$$
where each $\widehat{M}_\alpha$ has pure slope $p_\alpha/q_\alpha$ and the slopes
of the summands are exactly the slopes of the edges of $N(L)$. Choosing cyclic
vectors in each summand (Birkhoff-Schaepfer normal form) realises
$\widehat{M}_\alpha$ as the formal module of a single-slope scalar operator
$L_\alpha$, well-defined up to formal gauge. We write
$\widehat{L} \simeq L_1 \oplus \cdots \oplus L_m$ to mean this equivalence of
formal modules.

\textbf{Step 2 (Per-edge Main Theorem).} Each $L_\alpha$ is a scalar single-slope
connection with Newton polygon a \emph{single} edge of slope $-p_\alpha/q_\alpha$
and $r_\alpha + 1$ lattice points. The Phase-I Main Theorem
(\S 3 of paper\_draft) applies to $L_\alpha$ and yields
$$\chi^{(\alpha)}(c) \;=\; c^{k_0^{(\alpha)}}\, \chi_w^{(\alpha)}(c^{q_\alpha}),$$
where $\chi_w^{(\alpha)}(w) = \sum_{j=0}^{r_\alpha} \alpha_j^{(\alpha)}\, w^{r_\alpha - j}$
is the inner polynomial, $\alpha_j^{(\alpha)} = \mathrm{LC}_\infty\!\big(a_{(r_\alpha - j) q_\alpha + (\text{base of } E_\alpha)}\big)$,
and $k_0^{(\alpha)} \in \mathbb{Z}_{\ge 0}$ is the height of the left endpoint of
$E_\alpha$ above the $c$-axis (so $c^{k_0^{(\alpha)}}$ records the multiplicity
of $c = 0$ contributed by lattice points strictly below $E_\alpha$).

\textbf{Step 3 (Product factorisation).} Since the slope decomposition
$\widehat{L} \simeq \bigoplus_\alpha L_\alpha$ is a direct sum of formal connections,
the characteristic polynomial of $L$ (in the sense of the determinant of the
horizontal connection $1$-form, equivalently of the WKB symbol) factors as the
\emph{product} of the per-summand characteristic polynomials:
$$\chi(c) \;=\; \prod_{\alpha = 1}^{m}\, \chi^{(\alpha)}(c).$$
This is not a statement about ``scale separation'' but rather the determinant
of a direct sum (cf.\ Robba--Malgrange \emph{Le polygone de Newton} and the
multiplicativity of the Newton polygon of a tensor / direct-sum of formal
modules). Consequently, $\mathcal{C}(L) = \mathrm{Roots}(\chi) = \bigsqcup_\alpha \mathrm{Roots}(\chi^{(\alpha)}) = \bigsqcup_\alpha \mathcal{C}_\alpha$
as multisets.

\textbf{Step 4 (Genericity / open stratum).} The per-edge constellation
$\mathcal{C}_\alpha = \bigsqcup_{w \in \mathrm{Roots}(\chi_w^{(\alpha)})} \{c : c^{q_\alpha} = w\}$
occupies the radial annulus $\big[\rho_\alpha^{\min},\, \rho_\alpha^{\max}\big]$
with $\rho_\alpha^\bullet = |w^\bullet|^{1/q_\alpha}$ (here $w^{\min}, w^{\max}$
range over the minimum / maximum modulus of the roots of $\chi_w^{(\alpha)}$).
Relabelling the edges so that the radii $\rho_\alpha^{\min}$ are weakly
increasing in $\alpha$, the open subset
$$U_{\mathrm{disj}} := \big\{ (\alpha_j^{(\beta)}) : \rho_\alpha^{\max} < \rho_{\alpha + 1}^{\min}\ \ \forall \alpha = 1, \ldots, m-1 \big\} \subset \prod_\alpha \mathbb{C}^{r_\alpha + 1}$$
is the locus where the per-edge annuli are pairwise disjoint, and on it
$\mathcal{C}(L) = \bigsqcup \mathcal{C}_\alpha$ as honest disjoint subsets of
$\mathbb{C}^\times$. On the complement, the unions remain disjoint as
\emph{multisets} (with possible collisions in $\mathbb{C}^\times$ counted with multiplicity).

\hfill$\square$


### Counterexamples / sharpness boundary

* **CE-disc** (Discriminant locus of chi_w). Examples: `CTRL_disc_eps1`, `CTRL_disc_eps1o5`, `CTRL_disc_eps1o25`. *Fix:* Add hypothesis 'chi_w squarefree' (disc chi_w ne 0); resonance / logarithmic Stokes data appear when the discriminant degenerates.
* **CE-equalmod** (Equal-modulus locus). Examples: `STRESS_equalmod (paper draft Remark, §3)`, `CTRL_conjroots_t0`, `CTRL_conjroots_t1`, .... *Fix:* Restrict to the open subset {|w_i| pairwise distinct}; on the equal-modulus stratum, replace 'rigid rotation' by 'rigid permutation up to shared rotation' (cf. Cor. 2 of Main Theorem).
* **CE-zeroroot** (Zero-root locus). Examples: `CTRL_zeroroot_deep`, `CTRL_zeroroot_doublemult`. *Fix:* Add hypothesis 'alpha_r ne 0' (equivalently, chi_w(0) ne 0); when alpha_r = 0 the Newton polygon undergoes a wall-crossing and the dominant edge is replaced by a strictly shorter one.
* **CE-multiedge-equalradius** (Inter-edge equal-radius collision). Examples: `MULTI_edges_1o4_then_1o2 (subset where edges collide)`, `MULTI_edges_1o3_r2_then_1o2`. *Fix:* Restrict the per-edge factorisation Corollary to the open subset where the disjoint per-edge ring systems do not coincide radially; on the collision stratum the Stokes data interleave.
* **CE-multiedge-zerosharing** (Multi-edge zero-root sharing (M2)). Examples: `MULTI_edges_1o3_then_1o2`, `MULTI_edges_1o4_then_1o2`, `MULTI_edges_1o5_then_1o2`, .... *Fix:* Define per-edge constellations as multisets and identify the shared zero-roots at the joining vertices; the disjoint union is in the sheaf-theoretic / multiset sense.


### Scope and dependencies

* **Scope:** Scalar ODE setting. Parallel statements for difference and q-difference operators (with their own slope decomposition theorems) are recorded in §8 of the paper draft but not proved here.
* **Depends on:** Main Theorem (paper_draft §3)
* **Target section:** §4 (Multi-edge generalisation)

---

## Theorem N1 (Nested ramification: iterated $\mu_q$-pullback).

### Hypotheses

\textbf{Hypotheses.} $L$ scalar with one dominant edge of slope $-p/q$, $\gcd(p,q) = 1$;
$\chi_w(w) = \chi_v(w^{q'})$ for some $q' \ge 2$. No other genericity assumptions
are needed: N1 is a purely algebraic identity of polynomials.


### Statement

Let $L$ be scalar with one dominant edge of slope $-p/q$ as in the Main
Theorem. Suppose the inner polynomial admits a factorisation
$\chi_w(w) = \chi_v(w^{q'})$ for some integer $q' \ge 2$ and a polynomial
$\chi_v \in \mathbb{C}[v]$ of degree $r' = r/q'$ (so $\chi_w$ has nonzero
coefficients only in degrees that are multiples of $q'$). Then
$$\mathcal{C}(L) \;=\; \bigsqcup_{v \in \mathrm{Roots}(\chi_v)}\, \big\{\, c \in \mathbb{C} : c^{q q'} = v \,\big\}.$$
In particular each $v$-fibre carries the \emph{full} $\mu_{qq'}$-action (acting freely on
$\{c : c^{qq'} = v\}$). The \emph{visible} symmetry generated by the
$\mu_q$-action (from the outer factorisation $\chi(c) = \chi_w(c^q)$) and the
$\mu_{q'}$-action (from the nested factorisation $\chi_w = \chi_v \circ (\cdot)^{q'}$,
acting by permuting the $q'$-th roots of $v$ at the $w$-level) is
$\mu_{\mathrm{lcm}(q, q')} \subseteq \mu_{qq'}$. The two coincide exactly when
$\gcd(q, q') = 1$ (CRT), in which case $\mu_{qq'} \cong \mu_q \times \mu_{q'}$
canonically.


### Proof

By the Main Theorem, $\chi(c) = \chi_w(c^q)$. Substituting the hypothesis,
$$\chi(c) \;=\; \chi_w(c^q) \;=\; \chi_v\!\big((c^q)^{q'}\big) \;=\; \chi_v(c^{q q'}).$$
Hence
$$\mathcal{C}(L) \;=\; \mathrm{Roots}\!\big(\chi_v(c^{q q'})\big) \;=\; \bigsqcup_{v \in \mathrm{Roots}(\chi_v)} \big\{ c : c^{q q'} = v \big\}.$$

\textbf{Symmetry.} For each $v \in \mathrm{Roots}(\chi_v)$, the fibre
$\{c : c^{q q'} = v\}$ has cardinality $qq'$ and carries a free $\mu_{qq'}$-action.
The original Main Theorem's $\mu_q$-action sits inside $\mu_{qq'}$ as the
subgroup $\{\zeta_{qq'}^{q'k}\}$, acting on $c$ by $c \mapsto \zeta_q c$. A lift of
the inner-polynomial $\mu_{q'}$-symmetry (which permutes the $q'$ choices of
$q$-th root of $v$, i.e.\ acts by $w \mapsto \zeta_{q'} w$ at the $w$-level)
selects a $c$-level action by $c \mapsto \eta c$ with $\eta \in \mu_{qq'}$,
$\eta^q = \zeta_{q'}$. The subgroup of $\mu_{qq'}$ generated by these two actions
is $\mu_{\mathrm{lcm}(q, q')}$. When $\gcd(q, q') = 1$, $\mathrm{lcm}(q, q') = qq'$
and $\mu_{qq'} \cong \mu_q \times \mu_{q'}$ canonically; otherwise the two
factors share a common subgroup and the visible group is a proper subgroup of
the full $\mu_{qq'}$ acting on each fibre.

\textbf{Minimality.} The hypothesis ``$\chi_w(w) = \chi_v(w^{q'})$'' is preserved
under further inner factorisations $\chi_v(v) = \chi_u(v^{q''})$; iterating until
no inner factorisation exists gives the minimal $q' \cdot q'' \cdots$ for which
the constellation factors through.

\hfill$\square$


### Counterexamples / sharpness boundary

* **CE-nested-cancellation** (Nested-ramification cancellation). Examples: `(handled by recursive application of N1)`. *Fix:* State N1 / AT3 with 'minimal q' such that chi_w(w) = chi_v(w^{q'}) admits no further inner factorisation'; iterate until stable.


### Scope and dependencies

* **Scope:** Constellation-level theorem. The implications for the analytic ramification cover are addressed separately in Theorem AT3.
* **Depends on:** Main Theorem
* **Target section:** §4 (Nested ramification)

---

## Theorem D2 (Inner-polynomial Z-resonance dichotomy; prime $q$ case).

### Hypotheses

\textbf{Hypotheses.} $q$ prime; $\chi_w$ squarefree with $r \ge 2$ distinct roots
$w_1, \ldots, w_r$. Statement (i) is the algebraic-independence statement (no
$\mathbb{Z}$-relation \emph{at all} beyond $\mu_q$-forced); statement (ii) is
existential. For composite $q$, the $\mu_q$-forced sub-lattice is richer (it
contains sub-orbit sums coming from divisors of $q$); the dichotomy must be
restated by replacing ``$\lambda_\alpha = 0$ in $\mathbb{Z}[\zeta_q]$'' by
``$\lambda_\alpha$ in the kernel of the projection $\mathbb{Z}[\zeta_q] \to \prod_{d \mid q} \mathbb{Z}[\zeta_d]$''.


### Statement

Let $L$ be scalar with one dominant edge of slope $-p/q$ where $q$ is
\emph{prime}, and let $\chi_w$ have $r \ge 2$ distinct roots $w_1, \ldots, w_r$;
choose $q$-th roots $z_\alpha = w_\alpha^{1/q} \in \mathbb{C}$, so the ring
decomposition is
$\mathcal{C}(L) = \bigsqcup_\alpha R_\alpha$ with $R_\alpha = \{\zeta_q^j z_\alpha : 0 \le j < q\}$.

For $\lambda_1, \ldots, \lambda_r \in \mathbb{Z}[\zeta_q]$, write
$\Lambda(\lambda) = \sum_\alpha \lambda_\alpha z_\alpha \in \mathbb{C}$.
Call a $\mathbb{Z}$-relation $\sum_{\alpha, j} n_{\alpha j} \zeta_q^j z_\alpha = 0$
\textbf{$\mu_q$-forced} if every $\lambda_\alpha = \sum_j n_{\alpha j} \zeta_q^j$
lies in the ideal $\mathbb{Z}\cdot\Phi(\zeta_q) = \mathbb{Z}\cdot(1 + \zeta_q + \cdots + \zeta_q^{q-1}) = 0$
(equivalently, each $\lambda_\alpha = 0$ since $\Phi_q(\zeta_q) = 0$ is the only relation
among $1, \zeta_q, \ldots, \zeta_q^{q-1}$ for prime $q$); call it \textbf{cross-ring nontrivial} otherwise.

Then:
\begin{enumerate}
  \item \textbf{Generic case.} If $\{w_1, \ldots, w_r\}$ are algebraically independent
  over $\mathbb{Q}$, then $\mathcal{C}(L)$ admits \emph{no} cross-ring nontrivial
  $\mathbb{Z}$-relation.

  \item \textbf{Kummer/cyclotomic case.} If there exist $\lambda_\alpha \in \mathbb{Z}[\zeta_q]$
  not all zero such that $\sum_\alpha \lambda_\alpha z_\alpha = 0$, then this
  identity \emph{is} a cross-ring nontrivial $\mathbb{Z}$-relation on $\mathcal{C}(L)$.
  A clean sufficient condition is that the field extension
  $\mathbb{Q}(\zeta_q)(z_1, \ldots, z_r)$ has transcendence degree strictly less
  than $r$ over $\mathbb{Q}(\zeta_q)$; in particular, $w_\beta / w_\alpha \in (\mathbb{Q}(\zeta_q)^\times)^q$
  (so $z_\beta / z_\alpha \in \mathbb{Q}(\zeta_q)$ for a suitable choice of $q$-th
  roots) forces such a relation.
\end{enumerate}


### Proof

\textbf{Setup.} Each $R_\alpha = \{\zeta_q^j z_\alpha : 0 \le j < q\}$, so a
$\mathbb{Z}$-relation on $\mathcal{C}(L)$ takes the form
$\sum_{\alpha = 1}^{r} \sum_{j = 0}^{q - 1} n_{\alpha j}\, \zeta_q^j\, z_\alpha = 0.$
Collect terms by $\alpha$: setting $\lambda_\alpha := \sum_j n_{\alpha j} \zeta_q^j \in \mathbb{Z}[\zeta_q]$,
the relation becomes $\sum_\alpha \lambda_\alpha z_\alpha = 0$ in $\mathbb{C}$.

\textbf{$\mu_q$-forced sub-lattice.} For prime $q$, the kernel of the surjection
$\mathbb{Z}^q \twoheadrightarrow \mathbb{Z}[\zeta_q]$, $(n_0, \ldots, n_{q-1}) \mapsto \sum_j n_j \zeta_q^j$,
is generated by the cyclotomic relation $1 + \zeta_q + \cdots + \zeta_q^{q-1} = 0$
(the minimal polynomial of $\zeta_q$ over $\mathbb{Q}$ is the $q$-th cyclotomic
polynomial $\Phi_q(x) = 1 + x + \cdots + x^{q-1}$ of degree $q - 1$, so
$\mathrm{rk}_\mathbb{Z}(\mathbb{Z}[\zeta_q]) = q - 1$). Hence
$\lambda_\alpha = 0$ in $\mathbb{Z}[\zeta_q]$ iff $n_{\alpha 0} = n_{\alpha 1} = \cdots = n_{\alpha, q-1}$
(a constant vector along the cyclotomic kernel). Therefore the $\mu_q$-forced
sub-lattice is generated, ring by ring, by the per-ring sum $\sum_{c \in R_\alpha} c = z_\alpha \cdot \sum_j \zeta_q^j = 0$.

\textbf{Case (i) (Algebraic independence).} Suppose $\{w_\alpha\}_\alpha$ are
algebraically independent over $\mathbb{Q}$. Then $\{z_\alpha = w_\alpha^{1/q}\}_\alpha$
are algebraically independent over $\mathbb{Q}(\zeta_q)$: indeed, the field extension
$\mathbb{Q}(\zeta_q)(z_1, \ldots, z_r)$ is purely transcendental of transcendence
degree $r$ over $\mathbb{Q}(\zeta_q)$, because the $w_\alpha = z_\alpha^q$ are
algebraically independent and each $z_\alpha$ is algebraic of degree $q$ over
$\mathbb{Q}(\zeta_q)(w_\alpha)$ (by Eisenstein / cyclotomic Kummer theory).

Any $\mathbb{Z}[\zeta_q]$-linear relation $\sum_\alpha \lambda_\alpha z_\alpha = 0$
with some $\lambda_\alpha \ne 0$ would contradict algebraic independence of the
$z_\alpha$ over $\mathbb{Q}(\zeta_q)$. Hence all $\lambda_\alpha = 0$, which by the
preceding paragraph forces $n_{\alpha j}$ constant in $j$ for each $\alpha$, i.e. the
original $\mathbb{Z}$-relation is $\mu_q$-forced. This proves (i).

\textbf{Case (ii) (Kummer / cyclotomic).} If some $\lambda_\alpha \ne 0$ exists with
$\sum_\alpha \lambda_\alpha z_\alpha = 0$, expanding $\lambda_\alpha = \sum_j n_{\alpha j} \zeta_q^j$
recovers a $\mathbb{Z}$-relation $\sum_{\alpha, j} n_{\alpha j} \zeta_q^j z_\alpha = 0$.
By construction at least one $\lambda_\alpha \ne 0$, so the relation is \emph{not}
in the $\mu_q$-forced sub-lattice; it is cross-ring nontrivial.

The sufficient conditions follow from Kummer theory. If $w_\beta / w_\alpha = u^q$
for some $u \in \mathbb{Q}(\zeta_q)^\times$, then choosing $z_\beta$ as the $q$-th
root $u \cdot z_\alpha$ gives the $\mathbb{Z}[\zeta_q]$-relation
$z_\beta - u\, z_\alpha = 0$, which is a $\mathbb{Z}$-relation on
$\mathcal{C}(L)$ once $u$ is expanded as a $\mathbb{Z}$-linear combination of
$1, \zeta_q, \ldots, \zeta_q^{q-2}$ (the integral basis of $\mathbb{Z}[\zeta_q]$).
Specialising to $u \in \mathbb{Q}^\times$ (so $w_\beta / w_\alpha \in (\mathbb{Q}^\times)^q$)
gives a $\mathbb{Z}$-relation with support entirely in $\{z_\alpha, z_\beta\}$.

\textbf{Sharpness.} The Phase-III sweep records: every prime-$q$ generic-$\chi_w$
operator ($q \in \{5, 7\}$) produces zero cross-ring $\mathbb{Z}$-relations in the
search window $|n_k| \le 3$, support $\le 4$; every simple-$\chi_w$ multi-ring
operator produces $\ge 5$. The dichotomy is exact for prime $q$ within the search
window.

\hfill$\square$


### Counterexamples / sharpness boundary

* **CE-Zres-largecoef** (Z-resonance with large coefficients (D2 search-window limitation)). Examples: `(none detected in atlas, by construction; theoretical boundary)`. *Fix:* State D2 (i) as 'no cross-ring Z-relation in the |n_k| <= 3 / support <= 4 search window'; the genuine algebraic-independence statement (no Z-relation at all) requires algebraic independence of {w_alpha^{1/q}} over Q and is a transcendental-degree statement going beyond the sweep.
* **CE-Zres-compositeq** (Cyclotomic sub-orbit relations for composite q (D2 nuance)). Examples: `(implicit in q=4 and q=6 ops)`. *Fix:* Define 'mu_q-forced' as 'all per-ring sub-orbit sums vanish under the cyclotomic relations of mu_q' (this is the Phase-III refined definition); the cross-ring filter then identifies the truly cross-ring component.


### Scope and dependencies

* **Scope:** Stated for prime q; composite-q version is recorded in the Remark and uses sub-cyclotomic identities. Within the Phase-III search window, the dichotomy is sharp.
* **Depends on:** Main Theorem, Corollary 1 (ring decomposition)
* **Target section:** §5 (Degeneracy strata / arithmetic stratification)

---

## Theorem S1 (System pullback: block-diagonal direct sum).

### Hypotheses

\textbf{Hypotheses.} $\Phi$ block-diagonal with scalar blocks $L_i$ each satisfying
the Main Theorem hypotheses. Coupled-system extension: leading symbol diagonalisable
with distinct eigenvalues.


### Statement

Let $\Phi = \mathrm{diag}(L_1, \ldots, L_n)$ be a block-diagonal system of
scalar linear operators, each $L_i$ scalar with a single irregular singularity at
$x = \infty$ and Newton polygon $N(L_i)$. Then
$$\mathcal{C}(\Phi) \;=\; \bigsqcup_{i = 1}^{n}\, \mathcal{C}(L_i) \qquad \text{as multisets,}$$
and the constellation functor $F$ factors
$$F\,:\, \mathrm{Sys}^n(\text{scalar}) \;\longrightarrow\; \mathrm{Sym}^n(\text{finite multisets in } \mathbb{C}), \qquad F(\Phi) \;=\; \bigsqcup_i F(L_i).$$


### Proof

\textbf{Step 1.} For a block-diagonal system, the WKB characteristic polynomial
of $\Phi$ is the product of the per-block characteristic polynomials:
$$\chi_\Phi(c) \;=\; \det(\Phi - c \cdot \mathrm{Id})^{\sim} \;=\; \prod_{i = 1}^{n} \chi_{L_i}(c).$$
(More precisely: the WKB symbol of $\Phi$ acts diagonally on each block, so the
leading balance decouples across blocks.)

\textbf{Step 2.} Hence
$\mathrm{Roots}(\chi_\Phi) = \bigsqcup_i \mathrm{Roots}(\chi_{L_i})$ as multisets,
which is the claim.

\textbf{Step 3 (Factorisation through $\mathrm{Sym}^n$).} The map
$\Phi \mapsto (L_1, \ldots, L_n) \mapsto (\mathcal{C}(L_1), \ldots, \mathcal{C}(L_n))$
is $\mathfrak{S}_n$-equivariant under permutation of blocks (since the constellation
is a multiset, not an ordered tuple), so $F$ descends through the symmetric power.

\hfill$\square$

\textbf{Restriction (coupled systems).} For a general first-order system whose
leading symbol $A_0(x) = \mathrm{LC}_\infty(\Phi)$ is diagonalisable with distinct
eigenvalues, gauge transformations reduce $\Phi$ to a block-diagonal form to
leading order, and the conclusion of S1 holds at the constellation level.
Coalescence of leading eigenvalues defines a \emph{system discriminant stratum}
where the Levelt-Turrittin classification of irregular formal types is required;
S1 does not extend to that stratum without further hypotheses. Genuinely coupled
systems (non-semisimple leading symbol, Jordan blocks) lie outside the scope of
the present classification.


### Counterexamples / sharpness boundary

* **CE-coupled-system** (Coupled (non-block-diagonal) system). Examples: `(out of scope; not in atlas)`, `Generic Painleve-type systems`. *Fix:* Restrict S1 / AT4 to genuinely block-diagonal systems; for coupled systems, S1 holds after diagonalising the leading symbol when its eigenvalues are distinct, with system-discriminant strata defining further degenerations.


### Scope and dependencies

* **Scope:** Block-diagonal case is exact and tautological at the constellation level; coupled-system extension is conditional.
* **Depends on:** Main Theorem
* **Target section:** §6 (Systems)

---

## Theorem AT1 (Anti-Stokes $\leftrightarrow$ $\arg(\Delta_{ij})$ on the cover; open stratum).

### Hypotheses

\textbf{Open-stratum hypotheses (OS).}
(OS1) $\chi_w$ squarefree;
(OS2) $\chi_w(0) \ne 0$ (no zero-roots, so all $\Delta_{ij}$ relate distinct $c_i$);
(OS3) no $\omega$-resonance beyond $\mu_q$ (i.e., the multiset
$\{\arg \Delta_{ij} \mod \pi/p\}$ has no coincidences beyond those forced by the ring structure).


### Statement

Let $L$ be scalar with one dominant edge of slope $-p/q$ ($\gcd(p, q) = 1$), in
the \emph{open stratum} (OS1)--(OS3) below. Let $\mathcal{C}(L) = \{c_1, \ldots, c_N\}$
with $N = qr$ and $\Delta_{ij} = c_i - c_j$ for unordered pairs $\{i, j\}$. On
the ramified cover $x = t^q$, the formal connection splits as
$$\widehat{L}_{|x = t^q} \;\simeq\; \bigoplus_{i = 1}^{N}\, \big(\mathbb{C}\{t\},\ \mathrm{d} + \mathrm{d}Q_i(t)\big), \qquad Q_i(t) = c_i\, t^p + R_i(t),\ \deg R_i < p,$$
and the anti-Stokes directions on the $t$-plane are exactly
$$\mathcal{A}^{\mathrm{cov}} \;=\; \big\{\, \phi \in [0, 2\pi)\ :\ \arg(\Delta_{ij}) + p\, \phi \equiv \tfrac{\pi}{2} \pmod{\pi},\ \text{ some unordered } \{i, j\} \,\big\}.$$
Each unordered pair $\{i, j\}$ contributes exactly $2p$ cover-rays; the total
ray count \emph{with multiplicity} is $2p \binom{N}{2}$. The \emph{distinct} ray
count is determined by the $\Delta$-argument partition of
$\{\arg \Delta_{ij} \mod \pi/p\}_{\{i,j\}}$ (Phase-III D1). Under projection
to the base $x$-plane (covering map $t \mapsto t^q$), each unordered cover-pair's
$2p$ rays project to $2p/\gcd(2p, q)$ base-rays. The number of distinct base-rays
contributed by a single pair is therefore exactly $2p/\gcd(2p, q)$, with the
total distinct base-ray count obtained by accounting for cross-pair collisions.


### Proof

\textbf{Step 1 (Levelt-Turrittin on the $q$-cover).} By the Levelt-Turrittin theorem
(Sabbah \emph{Isomonodromic Deformations} Chap.\ II, Wasow Chap.\ VII, Sibuya
\emph{Linear ODEs in the Complex Domain}), there exists a ramification $x = t^q$
on which $\widehat{L}$ is gauge-equivalent to a direct sum of rank-one summands
$\big(\mathbb{C}\{t\},\ \mathrm{d} + \mathrm{d}Q_i(t)\big)$ with
$Q_i(t) = c_i t^p + R_i(t)$, $R_i \in \mathbb{C}[t]$ a polynomial of degree
strictly less than $p$ (here $t \to \infty$ corresponds to $x \to \infty$;
conventions match paper\_draft §3). Regular-singular
and formal-monodromy factors are absorbed into the rank-one summands as
logarithmic terms which do not affect the leading anti-Stokes analysis. The leading
coefficient of $Q_i$ is precisely a root of $\chi(c)$, so $c_i \in \mathcal{C}(L)$.

\textbf{Step 2 (Leading anti-Stokes condition).} Anti-Stokes directions (i.e.,
the boundaries of Stokes sectors for the pair $(i, j)$) are determined by the
\emph{leading} term of $Q_i(t) - Q_j(t)$ in $t$. On the open stratum the $c_i$
are pairwise distinct, so the leading term of $Q_i(t) - Q_j(t)$ is
$(c_i - c_j)\, t^p = \Delta_{ij}\, t^p$ (the lower-order $R_i, R_j$ terms contribute
sub-leading asymptotic corrections only, by the standard summation-theory
estimates; see Sabbah Thm.\ II.1.4). Writing $t = \rho\, e^{i\phi}$,
$$\mathrm{Re}\big(Q_i(t) - Q_j(t)\big) \;=\; \rho^p\, \mathrm{Re}\big(\Delta_{ij}\, e^{i p \phi}\big) + O(\rho^{p-1}) \;=\; \rho^p\, |\Delta_{ij}|\, \cos\!\big(\arg \Delta_{ij} + p \phi\big) + O(\rho^{p-1}).$$
Vanishing of the leading term gives
$\arg \Delta_{ij} + p \phi \equiv \tfrac{\pi}{2} \pmod{\pi}$,
and there are exactly $2p$ solutions in $[0, 2\pi)$ (the cosine has period $\pi$
in $p\phi$).

\textbf{Step 3 (Total count).} Summing over the $\binom{N}{2}$ unordered pairs
$\{i, j\}$ (the rays for $(i, j)$ and $(j, i)$ coincide modulo the $\pi$-period
of the cosine), the total number of cover-rays with multiplicity is
$2 p \binom{N}{2}$. The number of \emph{distinct} rays in $[0, 2\pi)$ is governed
by collisions in the multiset $\{\arg \Delta_{ij} \mod \pi/p : \{i, j\} \subseteq \mathcal{C}(L)\}$
(Phase-III D1 records this collision partition combinatorially).

\textbf{Step 4 (Projection to base).} The cover-to-base map $t \mapsto t^q$ acts
on phases by $\phi \mapsto q\phi \mod 2\pi$. Two cover-rays at angles $\phi_1, \phi_2$
project to the same base-ray iff $\phi_2 - \phi_1 \in (2\pi/q)\mathbb{Z}$. For a
fixed pair $(i, j)$, the $2p$ cover-rays are at $\phi_{ij, k} = \phi_{ij, 0} + k \pi/p$
($k = 0, 1, \ldots, 2p - 1$); the deck action $\phi \mapsto \phi + 2\pi/q$
identifies cover-rays into orbits of size $\gcd(2p, q)$, giving at most
$2p / \gcd(2p, q)$ distinct base-rays per pair. Equality holds away from cross-pair
collision strata (where two different pairs $(i, j), (i', j')$ project to the same
base-ray, reducing the total).

\hfill$\square$


### Counterexamples / sharpness boundary

* **CE-disc** (Discriminant locus of chi_w). Examples: `CTRL_disc_eps1`, `CTRL_disc_eps1o5`, `CTRL_disc_eps1o25`. *Fix:* Add hypothesis 'chi_w squarefree' (disc chi_w ne 0); resonance / logarithmic Stokes data appear when the discriminant degenerates.
* **CE-equalmod** (Equal-modulus locus). Examples: `STRESS_equalmod (paper draft Remark, §3)`, `CTRL_conjroots_t0`, `CTRL_conjroots_t1`, .... *Fix:* Restrict to the open subset {|w_i| pairwise distinct}; on the equal-modulus stratum, replace 'rigid rotation' by 'rigid permutation up to shared rotation' (cf. Cor. 2 of Main Theorem).
* **CE-zeroroot** (Zero-root locus). Examples: `CTRL_zeroroot_deep`, `CTRL_zeroroot_doublemult`. *Fix:* Add hypothesis 'alpha_r ne 0' (equivalently, chi_w(0) ne 0); when alpha_r = 0 the Newton polygon undergoes a wall-crossing and the dominant edge is replaced by a strictly shorter one.
* **CE-omega** (omega-resonance). Examples: `OMEGA_q2_fifth`, `OMEGA_q3_seventh`, `GAL_cyclotomic_3`, .... *Fix:* Either add 'no omega-resonance beyond mu_q' or replace 'distinct anti-Stokes directions' by 'distinct up to clustering at angular scale 2 pi / m'; for AT2 see Phase-IV calibration (universal-necessary; partial-sufficient).


### Scope and dependencies

* **Scope:** Open-stratum theorem. Phase-IV consistency: 11 open-stratum operators verify ratio actual/expected_max = 1.000 exactly.
* **Depends on:** Main Theorem, Levelt-Turrittin (cited)
* **Target section:** §7 (Analytic lifting)

---

## Theorem AT3 (Nested ramification induces $\mu_{q'}$-symmetry on wild data).

### Hypotheses

\textbf{Hypotheses.} As in N1: $\chi_w(w) = \chi_v(w^{q'})$ for some $q' \ge 2$,
$\chi_v$ admitting no further inner factorisation (else iterate). No additional
analytic hypotheses are required; AT3 is structural at the level of the formal
classification.


### Statement

Suppose the hypotheses of N1 hold: $\chi_w(w) = \chi_v(w^{q'})$ for some
$q' \ge 2$. Let $\mathcal{C}(L)$ be as in N1, and let $\mathrm{MW}(L)$ denote the
wild character variety of $L$ at $x = \infty$.

\begin{enumerate}
  \item The minimal Levelt-Turrittin ramification cover for $\widehat{L}$ is
  \textbf{still} $x = t^q$ (not $x = \tau^{q q'}$): on the $q$-cover, the formal
  connection splits as a direct sum of rank-one summands with irregular types
  $Q_i(t) = c_i t^p + (\text{lower})$, and the $c_i$ are exactly the elements of
  $\mathcal{C}(L)$ listed by N1.

  \item The nested factorisation $\chi_w = \chi_v \circ (\cdot)^{q'}$ induces an
  \emph{additional} $\mu_{q'}$-action on the constellation: choose any
  $\eta \in \mu_{qq'}$ with $\eta^q = \zeta_{q'}$ (the choice is unique modulo
  $\mu_q$); then $\eta$ acts on $\mathcal{C}(L)$ by $c \mapsto \eta\, c$, preserving
  each $v$-fibre $\{c : c^{qq'} = v\}$ and permuting the $q'$ choices of
  $w = c^q$ within that fibre. Combined with the original $\mu_q$-action of the
  cover (acting by $c \mapsto \zeta_q c$), the visible symmetry group of the
  constellation is $\mu_{\mathrm{lcm}(q, q')} \subseteq \mu_{qq'}$, with equality
  $\mu_{\mathrm{lcm}(q, q')} = \mu_{qq'}$ iff $\gcd(q, q') = 1$.

  \item The locus of irregular types $\{Q_i(t)\}_i$ compatible with the
  $\chi_w = \chi_v \circ (\cdot)^{q'}$ factorisation carries a natural
  $\mu_{q'}$-permutation symmetry (permuting the $q'$ choices of $q$-th root of
  $v$). At the level of the discrete part of the wild character variety
  $\mathrm{MW}(L)^{\mathrm{disc}}$ (parametrising irregular types modulo formal
  gauge), this symmetry organises the stratum of nested-factorisable types into
  a $\mu_{q'}$-equivariant subvariety. The full identification of this stratum
  with a quotient by $\mu_{q'}$ requires the wild character variety formalism of
  Boalch (\emph{Geometry and braiding of Stokes data}, 2014; \emph{Wild
  non-abelian Hodge theory on curves}); we assert here only the equivariance.
\end{enumerate}


### Proof

\textbf{Part (1) (Minimal cover is still $q$).} The Levelt-Turrittin ramification
index of a scalar single-slope formal connection equals the denominator $q$ of the
slope in lowest terms. The hypothesis $\chi_w(w) = \chi_v(w^{q'})$ constrains the
multiset of leading coefficients $\{c_i\}$ but does \emph{not} change the slope
$p/q$ of the Newton polygon. Hence the minimal cover on which the formal connection
splits into rank-one summands is $x = t^q$, exactly as in the Main Theorem and AT1.

(In particular, the Phase-IV draft of AT3 was \emph{incorrect} in claiming the
minimal cover becomes $x = \tau^{qq'}$. The corrected statement: nested
factorisation is a refinement of the constellation, not of the ramification cover.)

\textbf{Part (2) (Additional symmetry).} By N1, $\mathcal{C}(L) = \bigsqcup_v \{c : c^{qq'} = v\}$,
so each $v$-fibre carries a free $\mu_{qq'}$-action by $c \mapsto \zeta_{qq'} c$.
The original Main Theorem's $\mu_q$-symmetry corresponds, inside $\mu_{qq'}$, to the
subgroup $\{\zeta_{qq'}^{q' k}\}_k$. The nested $\mu_{q'}$-symmetry — acting at
the level of $w = c^q$ by $w \mapsto \zeta_{q'} w$ — lifts to an action on $c$
by multiplication by an $\eta \in \mu_{qq'}$ with $\eta^q = \zeta_{q'}$; such
$\eta$ exists in $\mu_{qq'}$ (e.g.\ $\eta = \zeta_{qq'}^q$), and is unique modulo
$\mu_q$. The subgroup of $\mu_{qq'}$ generated by $\zeta_q \in \mu_q$ and $\eta$
is precisely $\mu_{\mathrm{lcm}(q, q')}$. When $\gcd(q, q') = 1$, $\mathrm{lcm}(q,q') = qq'$
so the visible symmetry recovers the full fibre symmetry $\mu_{qq'} \cong \mu_q \times \mu_{q'}$
(CRT). For $\gcd(q,q') > 1$, the visible symmetry $\mu_{\mathrm{lcm}(q,q')}$ is a
\emph{proper} subgroup of the full polynomial fibre symmetry $\mu_{qq'}$.

\textbf{Part (3) (Equivariant strata of MW).} The discrete part of $\mathrm{MW}(L)$
parametrises tuples $(Q_1, \ldots, Q_N)$ of irregular-type polynomials modulo
gauge and formal monodromy. The $\mu_{q'}$-action of Part (2), acting on the
leading-coefficient multiset $\{c_i\}$ by $c_i \mapsto \eta c_i$, induces a
permutation of irregular types $Q_i \mapsto Q_{\sigma(i)}$ for some $\sigma$
depending on $\eta$. The locus of $\mathrm{MW}(L)^{\mathrm{disc}}$ compatible
with a fixed inner-polynomial $\chi_v$ is therefore $\mu_{q'}$-invariant. We do
not claim the further refinement that this locus is itself a $\mu_{q'}$-quotient
of a finer moduli space; that would require a precise model for the
``un-symmetrised'' irregular types, which lies in the wild-character-variety
machinery (Boalch \emph{op.\ cit.}, Sabbah \emph{Polarizable Twistor D-modules}).

\hfill$\square$


### Counterexamples / sharpness boundary

* **CE-nested-cancellation** (Nested-ramification cancellation). Examples: `(handled by recursive application of N1)`. *Fix:* State N1 / AT3 with 'minimal q' such that chi_w(w) = chi_v(w^{q'}) admits no further inner factorisation'; iterate until stable.


### Phase-IV correction note

Phase-IV AT3 incorrectly stated that the minimal cover becomes x = tau^{qq'}, leading to a ray-count of 2pq' per pair on a finer cover. The corrected statement: the cover stays at q; rays per pair on the q-cover are 2p (as in AT1); the mu_{q'}-action acts on the formal-monodromy classification (the discrete part of MW(L)).


### Scope and dependencies

* **Scope:** Reframed (vs Phase-IV draft AT3): the minimal Levelt-Turrittin cover remains q, not qq'; nested factorisation is a constellation-level / wild-character-variety symmetry, not an analytic ramification increase. The Phase-IV ray-count formula 2pq' is recalibrated below.
* **Depends on:** N1, AT1, Levelt-Turrittin
* **Target section:** §7 (Analytic lifting / Wild character variety)

---

## Theorem AT5 (Multi-edge slope filtration on the anti-Stokes skeleton).

### Hypotheses

\textbf{Open-stratum hypotheses (for AT5).}
(OS1)--(OS3) per-edge open-stratum (apply AT1 to each $L_\alpha$);
(OS4) per-edge radial annuli pairwise disjoint;
(OS5) cross-edge leading coefficients nonzero, i.e.\ $c_j \ne 0$ for $j \in \mathcal{C}_\beta$
(equivalently $\chi_w^{(\beta)}(0) \ne 0$, so the dominant edge has no zero-root contribution).
If (OS5) fails, the cross-edge degree must be recomputed from the next nonzero
term of $Q_j^{(\beta)}$, which may have degree strictly less than $P_\beta$ — in
which case the slope filtration on Stokes data needs the corresponding correction.


### Statement

Suppose $L$ has multi-edge Newton polygon as in M1, with edges $E_\alpha$ of
slope $-p_\alpha/q_\alpha$ and per-edge constellations $\mathcal{C}_\alpha$ of size
$N_\alpha = q_\alpha r_\alpha$. Let $d = \mathrm{lcm}(q_1, \ldots, q_m)$ and consider
the common cover $x = t^d$. Then:

\begin{enumerate}
  \item \textbf{Within-edge rays.} The anti-Stokes rays contributed by pairs
  $(i, j)$ both in $\mathcal{C}_\alpha$ are exactly the rays of AT1 applied to
  $L_\alpha$, lifted from the $q_\alpha$-cover to the $d$-cover (each such ray
  appears with multiplicity $d / q_\alpha$ on the $d$-cover): $2 P_\alpha \binom{N_\alpha}{2}$
  rays counted with multiplicity, where $P_\alpha = p_\alpha d / q_\alpha$.

  \item \textbf{Cross-edge rays.} For pairs $(i \in \mathcal{C}_\alpha, j \in \mathcal{C}_\beta)$
  with $\alpha \ne \beta$, write $\sigma_\alpha = p_\alpha / q_\alpha$ for the slope
  magnitude and WLOG $\sigma_\beta > \sigma_\alpha$ (the edges have distinct slopes,
  so $\sigma_\alpha \ne \sigma_\beta$). On the common cover, $P_\beta > P_\alpha$
  (with $P_\bullet := p_\bullet d/q_\bullet = \sigma_\bullet d$), so the irregular types satisfy
  $$Q_j^{(\beta)}(t) - Q_i^{(\alpha)}(t) \;=\; c_j\, t^{P_\beta} \,-\, c_i\, t^{P_\alpha} \,+\, (\text{lower}),$$
  whose leading term is $c_j t^{P_\beta}$ (provided $c_j \ne 0$; hypothesis (OS5)).
  The corresponding anti-Stokes directions are determined by
  $\arg(c_j) + P_\beta\, \phi \equiv \pi/2 \pmod{\pi}$, contributing $2 P_\beta$
  rays per cross-edge pair.

  \item \textbf{Slope filtration.} The Stokes data of $L$ decompose along the
  slope filtration $\widehat{L} \simeq \bigoplus_\alpha L_\alpha$: each summand
  $L_\alpha$ carries its own Stokes structure with rays of slope $-p_\alpha/q_\alpha$;
  cross-edge Stokes constants ($L_\alpha \to L_\beta$ with $\alpha < \beta$) are
  organised along rays of the \emph{higher} slope $-p_\beta/q_\beta$.
\end{enumerate}


### Proof

\textbf{Step 1 (Within-edge).} By M1, $\widehat{L} \simeq \bigoplus_\alpha L_\alpha$
as formal connections. The Stokes structure of a direct sum is the direct sum of
the per-summand Stokes structures, with no cross-summand interaction at the
\emph{within-summand} level. AT1 applied to $L_\alpha$ on its own $q_\alpha$-cover
$x = s^{q_\alpha}$ yields $2 p_\alpha \binom{N_\alpha}{2}$ rays at $s$-angles
$\psi_{ij, k} = \psi_{ij, 0} + k \pi / p_\alpha$. Lifting to the common cover
$x = t^d$ via $s = t^{d / q_\alpha}$, an $s$-angle $\psi$ corresponds to
$d / q_\alpha$ distinct $t$-angles $\phi = (q_\alpha / d)(\psi + 2\pi k)$,
$k = 0, \ldots, d/q_\alpha - 1$. Each $q_\alpha$-cover ray hence pulls back to
$d / q_\alpha$ rays on the $d$-cover. The total within-edge $E_\alpha$
contribution on the $d$-cover is therefore $2 p_\alpha \cdot (d/q_\alpha) \cdot \binom{N_\alpha}{2}
 = 2 P_\alpha \binom{N_\alpha}{2}$ rays, at $t$-angle spacing $\pi / P_\alpha$.

\textbf{Step 2 (Cross-edge leading term).} On the common cover $x = t^d$, the
edge $E_\alpha$'s rank-one summand has irregular type $Q_i^{(\alpha)}(t) = c_i\, t^{P_\alpha}$
($P_\alpha = p_\alpha d / q_\alpha = \sigma_\alpha d$); similarly for $E_\beta$.
Since the slopes are \emph{distinct}, $\sigma_\alpha \ne \sigma_\beta$, so
$P_\alpha \ne P_\beta$. WLOG $P_\beta > P_\alpha$. Then
$Q_j^{(\beta)}(t) - Q_i^{(\alpha)}(t) = c_j t^{P_\beta} - c_i t^{P_\alpha} + (\text{lower})$,
and assuming $c_j \ne 0$ (hypothesis (OS5)) the leading term is $c_j t^{P_\beta}$.
The anti-Stokes analysis (Step 2 of AT1) applied to this leading term gives the
condition $\arg c_j + P_\beta \phi \equiv \pi/2 \pmod{\pi}$, with $2 P_\beta$ solutions.

\textbf{Step 3 (Slope filtration).} The Stokes structure of $\widehat{L} \simeq \bigoplus_\alpha L_\alpha$
inherits the slope filtration: Stokes constants between summands of slopes
$\sigma_\alpha < \sigma_\beta$ are graded by the larger slope $\sigma_\beta$. This
is the standard Stokes-graded structure of a slope-filtered irregular connection
(see Sabbah \emph{Polarizable Twistor D-modules}, §11; Boalch, \emph{Wild
non-abelian Hodge theory on curves}, §3 for the geometric formulation).

\hfill$\square$


### Counterexamples / sharpness boundary

* **CE-multiedge-equalradius** (Inter-edge equal-radius collision). Examples: `MULTI_edges_1o4_then_1o2 (subset where edges collide)`, `MULTI_edges_1o3_r2_then_1o2`. *Fix:* Restrict the per-edge factorisation Corollary to the open subset where the disjoint per-edge ring systems do not coincide radially; on the collision stratum the Stokes data interleave.
* **CE-multiedge-zerosharing** (Multi-edge zero-root sharing (M2)). Examples: `MULTI_edges_1o3_then_1o2`, `MULTI_edges_1o4_then_1o2`, `MULTI_edges_1o5_then_1o2`, .... *Fix:* Define per-edge constellations as multisets and identify the shared zero-roots at the joining vertices; the disjoint union is in the sheaf-theoretic / multiset sense.


### Scope and dependencies

* **Scope:** Multi-edge / slope-filtered case. Cross-edge collisions on the equal-radius stratum cause additional refinements; zero-root contributions need (OS5).
* **Depends on:** M1, AT1
* **Target section:** §7 (Analytic lifting / multi-edge)

---

## Theorem AT7 ($p$-visibility: analytic anti-Stokes data detect $p$).

### Hypotheses

\textbf{Hypotheses.} Fixed $q$, $r$, and inner polynomial $\chi_w$;
$L_p$ scalar with one dominant edge of slope $-p/q$ for each coprime $p$.
Open-stratum (OS1)-(OS3) for the distinct-ray formula in Part (3); the
proportionality $\#\mathcal{A}^{\mathrm{cov}}_p \propto p$ is sub-stratum-independent.


### Statement

Fix $q$ and $r$ and let $\chi_w$ be a fixed inner polynomial of degree $r$.
For each $p \in \{p' : 1 \le p' < q,\ \gcd(p', q) = 1\}$, let $L_p$ denote a
scalar operator whose Newton polygon has a single dominant edge of slope $-p/q$
with the prescribed $\chi_w$. Then:

\begin{enumerate}
  \item (Constellation $p$-invariance, Phase-III P1.) $\mathcal{C}(L_p)$ is
  independent of $p$ as a multiset in $\mathbb{C}$, and the $\Delta$-modulus
  partition $\{|\Delta_{ij}|\}$ is $p$-independent.

  \item ($p$-visibility on the cover, AT7.) The anti-Stokes ray set
  $\mathcal{A}^{\mathrm{cov}}_p$ on the cover $x = t^q$ \emph{depends} on $p$:
  rays satisfy $\arg \Delta_{ij} + p \phi \equiv \tfrac{\pi}{2} \pmod{\pi}$, so
  varying $p$ rotates / dilates the ray pattern.

  \item Quantitatively, in the open stratum the cover-ray count is
  $2 p \binom{N}{2}$ with multiplicity. For $\chi_w$ generic with $r$ distinct
  nonzero roots of pairwise distinct moduli (so $\mathcal{C}(L)$ decomposes as
  $r$ disjoint rings of $q$ points each) and $q \ge 3$, the \emph{distinct}
  cover-ray count is
  $$\#\mathcal{A}^{\mathrm{cov}}_p \;=\; 2 p \cdot \Big(r \cdot q \,+\, q^2 \cdot \binom{r}{2}\Big) \;=\; 2 p\, q \,\big(\, r \,+\, q\, \tbinom{r}{2}\big),$$
  which is strictly proportional to $p$ for fixed $\chi_w$, and in particular is
  not $p$-invariant. The case $q = 2$ admits only one within-ring direction
  class per ring and the formula becomes $2 p (r + 4 \binom{r}{2})$.

  \item Hence Phase-III P1 holds at the constellation / $\Delta$-partition level,
  but \emph{fails} at the analytic anti-Stokes level: $p$ is invisible to the
  combinatorics of $\mathcal{C}(L)$ and visible to the analytic Stokes skeleton.
\end{enumerate}


### Proof

\textbf{Part (1) (P1).} $\chi(c) = \chi_w(c^q)$ by the Main Theorem, so
$\mathcal{C}(L_p) = \mathrm{Roots}(\chi)$ depends only on $\chi_w$, not on $p$.
Likewise $\Delta_{ij} = c_i - c_j$ depends only on $\mathcal{C}(L_p)$, so the
$\Delta$-modulus and $\Delta$-argument partitions are $p$-invariant.

\textbf{Part (2) (Visibility).} By AT1, cover-rays satisfy
$\arg \Delta_{ij} + p \phi \equiv \pi/2 \pmod{\pi}$. Solving for $\phi$:
$$\phi \;=\; \frac{1}{p}\!\left(\tfrac{\pi}{2} - \arg \Delta_{ij} + k \pi\right), \qquad k = 0, 1, \ldots, 2p - 1.$$
The set of $\phi$-values explicitly depends on $p$: the spacing between adjacent
rays for a fixed pair is $\pi/p$, so doubling $p$ halves the angular spacing.

\textbf{Part (3) (Counting on rings).} Suppose $\chi_w$ generic with $r$ distinct
nonzero roots of pairwise distinct moduli, so $\mathcal{C}(L) = \bigsqcup_{\alpha = 1}^{r} R_\alpha$
with $R_\alpha = \{\zeta_q^j z_\alpha : 0 \le j < q\}$. Assume $q \ge 3$. Pairs decompose as:
\begin{itemize}
  \item \emph{Within-ring.} For each ring $R_\alpha$ the $\binom{q}{2}$ unordered pairs
  $\{j, k\}$ with $j \ne k$ give differences
  $\Delta = z_\alpha(\zeta_q^j - \zeta_q^k) = z_\alpha \zeta_q^k(\zeta_q^{j-k} - 1)$.
  Hence $\arg \Delta \;=\; \arg z_\alpha + \tfrac{(j+k)\pi}{q} + \tfrac{\pi}{2} \pmod{\pi}$
  (using $\arg(\zeta_q^m - 1) = m\pi/q + \pi/2 \pmod{\pi}$ for $m \not\equiv 0$).
  The argument depends only on $(j + k) \bmod q$, which takes $q$ distinct values
  on the unordered pairs $\{j, k\}$ with $j \ne k$. Each of these $q$ direction
  classes contributes $2p$ rays (from the $k\pi/p$ ambiguity in AT1), giving
  $2 p q$ distinct cover-rays per ring and $2 p q r$ total within-ring.

  \item \emph{Cross-ring.} The $q^2 \binom{r}{2}$ unordered pairs across distinct
  rings $R_\alpha, R_\beta$ generically all have distinct $\arg \Delta \bmod \pi/p$
  (open stratum), each contributing $2p$ distinct cover-rays, totaling
  $2 p \cdot q^2 \binom{r}{2}$.
\end{itemize}
Summing:
$\#\mathcal{A}^{\mathrm{cov}}_p \;=\; 2 p q r + 2 p q^2 \binom{r}{2} \;=\; 2 p q\, \big(r + q \binom{r}{2}\big),$
proportional to $p$ as claimed.

\textbf{Phase-IV verification.} For the PINV family with $q = 5$, $r = 2$, $N = 10$,
the formula gives
$\#\mathcal{A}^{\mathrm{cov}}_p \;=\; 2 p \cdot 5 \cdot (2 + 5 \cdot 1) \;=\; 70 p.$
The empirical Phase-IV measurement (\texttt{phase4\_stokes.json}) records 70,
140, 210, 280 for $p = 1, 2, 3, 4$ respectively — exact agreement with $70 p$,
confirming the formula on the open stratum.

\textbf{Part (4) (Conclusion).} P1 (constellation level) and AT7 (analytic level)
are not contradictory: the constellation does not see $p$, but the Stokes
skeleton does, via the $\pi/p$-spacing of rays. AT7 is the analytic strengthening
of P1, recording precisely \emph{how} $p$ enters the Stokes geometry while
remaining invisible to the discrete classification.

\hfill$\square$


### Counterexamples / sharpness boundary

* **CE-p-invisible-discrete** (p-invariance at the discrete level (P1)). Examples: `PINV_s1o5_r2_genc`, `PINV_s2o5_r2_genc`, `PINV_s3o5_r2_genc`, .... *Fix:* P1 is preserved as a discrete invariance; AT7 records the analytic refinement that breaks p-invariance at the Stokes-data level.


### Scope and dependencies

* **Scope:** Statement of the strengthening of P1 at the analytic level. Verification on the PINV family confirms exact proportionality to p.
* **Depends on:** AT1, P1 (Phase-III)
* **Target section:** §7 (Analytic lifting / p-visibility)

---


## References to Phase III / IV evidence

Each theorem is empirically supported by the operator atlas of Phase III
(`phase3_invariants.json`, 48 operators across 11 families) and the
anti-Stokes skeleton computations of Phase IV (`phase4_stokes.json`, all 48
operators). The counterexample knowledge base (`counterexamples.json`)
catalogues the strata on which naive forms of the theorems fail.

* M1: 9 multi-edge operators (`MULTI_*`, `MULTI3_*`); 7 of 9 with disjoint
  per-edge radii.
* N1, AT3: 2 nested-ramification operators (`NEST_q3_qinner2`, `NEST_q2_qinner3`).
* D2: 4 prime-$q$ generic operators (HIGHQ_genc_s{1,2}o5_r2, HIGHQ_genc_s3o7_r2,
  HIGHQ_genc_s1o5_r3) -- all with zero cross-ring $\mathbb{Z}$-relations; 6
  simple-$\chi_w$ multi-ring operators -- all with $\ge 5$ cross-ring relations.
* S1: 4 system operators (`SYS2_*`, `SYS3_*`), all genuinely block-diagonal.
* AT1: 11 open-stratum operators with $\#\mathcal{A}^{\mathrm{cov}}_{\mathrm{actual}} / \#\mathcal{A}^{\mathrm{cov}}_{\mathrm{expected}} = 1.000$.
* AT5: 9 multi-edge operators, cross-edge contributions visible in
  `phase4_stokes.json` ray-multiplicity profiles.
* AT7: 4 PINV operators (`PINV_s{1,2,3,4}o5_r2_genc`), distinct-ray count $\propto p$
  (empirical: 70, 140, 210, 280).
