# Local-Invariant Characterisation of the Four Degenerate Strata

**Date:** 2026-05-26
**Companion script:** `compute_fingerprints.py` (run to regenerate
`fingerprints.json`).
**Phase-3 gap addressed:** G15 — *Codimension count for each degeneracy stratum.*

---

## 1. Setup

Each Phase-1 representative is a single-edge WKB symbol
$$\chi(c) \;=\; \chi_w(c^q), \qquad
  \chi_w(w) \;=\; w^{r} + \beta_1 w^{r-1} + \dots + \beta_r,$$
with dominant-edge slope $-p/q$ (lowest terms) and inner-polynomial degree $r$,
so $d = qr$.  The canonical local moduli of the dominant edge is
$\beta = (\beta_1,\dots,\beta_r) \in \mathbb{C}^{r}$.

The user-requested **"Jacobian of $\chi$ under small $\Delta_{ij}$ shifts"** is
realised as the **Vieta Jacobian** on c-root perturbations,
$J_\alpha[k,i] = \partial \alpha_k / \partial c_i$, restricted to the centered
subspace $T = \{\varepsilon \in \mathbb C^{d} : \sum_i \varepsilon_i = 0\}$
(translations leave all $\Delta_{ij} = c_i - c_j$ invariant). Its kernel on
$T$ records the "swap" directions induced by coincident roots; its rank
records the genuine $\Delta_{ij}$ response.

---

## 2. Fingerprint table

| stratum | $(d,q,r)$ | $\chi$ | $\beta$ | $C_n$ | codim$_\mathbb C^\beta$ | codim$_\mathbb R^\beta$ | soft$_\mathbb C^\beta$ | $J_\alpha\!\mid_T$  rank / ker | swap-kernel | incid (z, d, e, s) | rigidity |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `STRESS_zeroroot`       | (4,2,2) | $c^4 - c^2$           | $(-1, 0)$    | 2 | 1 | 2 | 1 | **2 / 1** | 1 | (✓, –, –, –) | rigid (codim 1) |
| `STRESS_doubleroot`     | (9,3,3) | $c^9-4c^6+5c^3-2$    | $(-4, 5, -2)$ | 3 | 1 | 2 | 2 | **5 / 3** | 3 | (–, ✓, –, –) | rigid (codim 1) |
| `STRESS_equalmod`       | (6,2,3) | $c^6-2c^4+4c^2-8$    | $(-2, 4, -8)$ | 2 | **0** | 2 | — | **5 / 0** | 0 | (–, –, ✓, –) | real-only |
| `STRESS_accidental_sym` | (6,2,3) | $c^6 + 1$             | $(0, 0, 1)$   | 6 | **2** | 4 | 1 | **5 / 0** | 0 | (–, –, ✓, ✓) | very rigid |

Columns:
- **codim$_\mathbb C^\beta$**: complex codimension of the stratum in
  $\beta$-space (number of independent complex-algebraic defining equations).
- **codim$_\mathbb R^\beta$**: real codimension (= 2·codim$_\mathbb C$ for
  complex-algebraic, = number of independent real equations for equalmod).
- **soft$_\mathbb C^\beta$**: $\mathbb C$-dim of the in-stratum tangent space
  in $\beta$-space (= $r$ − codim$_\mathbb C$). For `equalmod` the stratum
  is real-only and complex soft-dim is undefined.
- **$J_\alpha\!\mid_T$ rank / ker**: rank and kernel dim of the Vieta Jacobian
  restricted to the centered c-root perturbation space $T$ (dim $d-1$).
- **swap-kernel**: dim of $J_\alpha$'s null space coming from coincident
  c-roots (a structural source of softness in $T$).
- **incid (z, d, e, s)**: incidence flags — does the representative satisfy
  (zero-root, disc-zero, equimodular, $C_d$-sparse)? Confirms that the four
  strata **overlap**: `doubleroot` is also trivially equimodular via the
  coincident pair, and `accidental_sym` is equimodular as well (all sixth
  roots of $-1$ have $|w|=1$).

---

## 3. Per-stratum analysis

### 3.1  `STRESS_zeroroot`  —  zero inner root

- **Defining equation:** $F(\beta) = \beta_r = 0$ (constant term of $\chi_w$).
- **Jacobian:** $\mathrm dF/\mathrm d\beta = (0, \dots, 0, 1)$ (rank 1).
- **Codim$_\mathbb C^\beta = 1$.**
- **Vieta side:** c-roots = $\{0, 0, 1, -1\}$, one coincident pair at $c=0$.
  $\mathrm{rank}(J_\alpha\!\mid_T) = 2$, $\mathrm{ker}(J_\alpha\!\mid_T) = 1$,
  and the kernel coincides with the **swap-kernel** of the doubled c=0
  root. So the kernel is geometric (multiplicity-induced), not a genuine
  $\beta$-tangent direction.
- **Interpretation:** Single complex-algebraic constraint. A normal perturbation
  of $\beta_r$ destroys the stratum at first order. **Rigid (codim 1).**

### 3.2  `STRESS_doubleroot`  —  discriminant locus of $\chi_w$

- **Defining equation:** $F(\beta) = \mathrm{disc}_w(\chi_w) = 0$.
- **Jacobian:** $\mathrm dF/\mathrm d\beta$ computed symbolically; at the rep
  it is **nonzero** (verified numerically). Codim$_\mathbb C^\beta = 1$.
- **Vieta side:** c-roots are the union of $\{1,\omega,\omega^2\}$ (each
  doubled) and $\{2^{1/3},2^{1/3}\omega,2^{1/3}\omega^2\}$ (simple), $\omega
  = e^{2\pi i/3}$. Three coincident pairs ⇒ swap-kernel dim 3.
  $\mathrm{rank}(J_\alpha\!\mid_T) = 5$, $\mathrm{ker}(J_\alpha\!\mid_T) = 3$.
- **Important subtlety (rubber-duck-flagged):** $\mathrm{disc}_w$ vanishes
  *quadratically* in the inner-root separation $w_1 - w_2$. A naive Jacobian
  $\mathrm d\mathrm{disc}/\mathrm dw$ at the coincident pair is **zero**, which
  is why we compute in $\beta$-space (always smooth) rather than $w$-space.
- **Interpretation:** Single complex-algebraic hypersurface, codim 1.
  Rank-deficient c-root Jacobian reflects 3 directions of multiplicity-induced
  softness — these correspond to *staying on the doubleroot stratum* by
  redistributing the doubled c-roots among their orbit. **Rigid (codim 1).**

### 3.3  `STRESS_equalmod`  —  equimodular triple of inner roots

- **Defining equations (real):** $F_1(\beta) = |w_1|^2 - |w_2|^2$, $F_2(\beta)
  = |w_2|^2 - |w_3|^2$. Real-analytic but **not complex-algebraic**: there
  is no holomorphic equation in $\beta$ defining this stratum.
- **Jacobian:** real finite-difference $\mathrm dF/\mathrm d(\mathrm{Re}\,\beta,
  \mathrm{Im}\,\beta) \in \mathbb R^{2 \times 6}$ has rank 2 at the rep
  ($w = \{2, 2i, -2i\}$, all $|w| = 2$). Codim$_\mathbb R^\beta = 2$,
  codim$_\mathbb C^\beta = 0$.
- **Vieta side:** all six c-roots are simple; swap-kernel dim 0,
  $\mathrm{rank}(J_\alpha\!\mid_T) = 5 = d - 1$ (full).
- **Interpretation:** The "softest" of the four strata in the complex
  category: a holomorphic perturbation of $\beta$ generically leaves
  `equalmod`, but only along 2 of the 6 real dimensions; the other 4 real
  directions slide *within* the equimodular locus. **Real-only.**
- **Triple vs pair:** at the rep all three roots are equimodular, hence
  $\binom{3}{2} = 3$ pairwise constraints but only 2 are independent. The
  generic equimodular stratum (one equimodular pair, rest distinct moduli)
  has codim$_\mathbb R^\beta = 1$.

### 3.4  `STRESS_accidental_sym`  —  $C_d$-inflation by sparse $\chi_w$

- **Defining equations:** $\beta_1 = \beta_2 = \dots = \beta_{r-1} = 0$
  (only $\beta_r$ remains nonzero), i.e. $\chi_w(w) = w^r + \beta_r$ is a
  binomial.
- **Jacobian:** $\mathrm dF/\mathrm d\beta = [\,I_{r-1}\;|\;0\,]$,
  rank $r-1 = 2$. Codim$_\mathbb C^\beta = r - 1 = 2$.
- **Vieta side:** c-roots are the $d$-th roots of $-\beta_r$, all simple;
  $\mathrm{rank}(J_\alpha\!\mid_T) = 5$, swap-kernel dim 0.
- **Interpretation:** Highest-codim stratum of the four (codim 2 in a 3-dim
  $\beta$-space). The C_d-inflation is structurally rigid: any single
  middle-coefficient $\beta_k$ becoming nonzero ($1 \le k \le r-1$) breaks
  the $C_d$ symmetry to $C_q$ at first order. **Very rigid.**
- **Overlap with equalmod (rubber-duck-flagged):** The representative is
  $\chi_w = w^3 + 1$ whose roots are the cube roots of $-1$, all on the
  unit circle $|w| = 1$. So `accidental_sym ⊂ equalmod` at the rep.
  This is **generic** for the stratum: a binomial $w^r + \beta_r$ has roots
  on a common circle of radius $|\beta_r|^{1/r}$, so $C_d$-inflation always
  implies equimodularity.

---

## 4. Rigid vs. soft summary

The four strata divide into three rigidity classes:

| class | strata | property |
|---|---|---|
| **very rigid** (codim$_\mathbb C \ge 2$) | `accidental_sym` | multiple independent complex equations; codim is large fraction of $r$ |
| **rigid (codim 1)** | `zeroroot`, `doubleroot` | single complex-algebraic hypersurface |
| **real-only soft** (codim$_\mathbb C = 0$, codim$_\mathbb R \ge 1$) | `equalmod` | no holomorphic obstruction; only real-analytic constraint |

The Vieta-Jacobian softness (swap-kernel) is **orthogonal** to the
$\beta$-rigidity: `zeroroot` and `doubleroot` both pick up swap-kernels from
c-root multiplicities (1 and 3 respectively), but those kernels are
geometric reorderings, not $\beta$-tangent directions.

---

## 5. Stratum incidences (non-disjointness)

| representative | zero-root | disc-zero | equimodular | $C_d$-sparse |
|---|---|---|---|---|
| `zeroroot`       | ✓ | – | – | – |
| `doubleroot`     | – | ✓ | (trivially via coincident pair, not flagged) | – |
| `equalmod`       | – | – | ✓ | – |
| `accidental_sym` | – | – | ✓ | ✓ |

The strata are **not** pairwise disjoint:
1. `accidental_sym ⊂ equalmod` (binomial $\chi_w$ ⇒ roots on a circle).
2. `doubleroot` representatives trivially have equal-modulus *coincident*
   pairs (the equimodular flag in the script excludes coincident pairs, but
   one could include them).
3. `zeroroot` is disjoint from the other three at the representative.

Phase-3 work should respect this overlap structure when stratifying the
α-coefficient space.

---

## 6. Fingerprint vector (machine-readable)

20-dim integer vector layout:

```
[d, q, r,
 codim_C_in_beta, codim_R_in_beta,
 rank_dF_real, soft_dim_C_in_beta, soft_dim_R_in_beta,
 C_n,
 is_complex_algebraic,
 delta_distinct_moduli, delta_distinct_args_mod_pi, delta_zero_pairs,
 vieta_rank_on_T, vieta_ker_dim_on_T, vieta_swap_kernel_dim,
 inc_zero_root, inc_disc_zero, inc_equimod, inc_C_d_sparse]
```

| stratum | fingerprint vector |
|---|---|
| `STRESS_zeroroot`       | `[4, 2, 2, 1, 2, 2, 1, 2, 2, 1, 3, 1, 1, 2, 1, 1, 1, 0, 0, 0]` |
| `STRESS_doubleroot`     | `[9, 3, 3, 1, 2, 2, 2, 4, 3, 1, 5, 12, 3, 5, 3, 3, 0, 1, 0, 0]` |
| `STRESS_equalmod`       | `[6, 2, 3, 0, 2, 2, -1, 4, 2, 0, 4,  8, 0, 5, 0, 0, 0, 0, 1, 0]` |
| `STRESS_accidental_sym` | `[6, 2, 3, 2, 4, 4, 1, 2, 6, 1, 3,  6, 0, 5, 0, 0, 0, 0, 1, 1]` |

All four vectors are pairwise distinct, so the fingerprint is **separating**
on the Phase-1 stress-test set. Three discriminating coordinates suffice
in practice:
- `codim_C_in_beta`: separates `equalmod` (0), {zeroroot, doubleroot} (1),
  `accidental_sym` (2).
- `vieta_swap_kernel_dim`: separates `zeroroot` (1) from `doubleroot` (3).
- `inc_C_d_sparse`: separates `accidental_sym` (1) from the others (0).

---

## 7. Caveats / open follow-ups

1. **Stratum representatives, not generic stratum points.** The codim
   numbers are *at* the representatives. `equalmod` away from the
   triple-equimodular configuration has codim$_\mathbb R = 1$; we have
   reported the more degenerate case (codim$_\mathbb R = 2$) per the
   Phase-1 stress example.
2. **Δ_ij Jacobian interpretation.** "Jacobian of χ under Δ_ij shifts" is
   interpreted as $J_\alpha = \mathrm d\alpha/\mathrm dc$ restricted to the
   centered subspace $T = \{\sum \varepsilon_i = 0\}$. Pairwise differences
   $\Delta_{ij}$ themselves are over-parameterised ($\binom{d}{2}$ pairs
   from $d-1$ independent centered perturbations).
3. **No Stokes-graph adjacency.** Phase-3 G5 hints that arg-partitions of
   $\Delta_{ij}$ control Stokes-line combinatorics. We have recorded only
   the count of distinct $\arg\Delta_{ij} \bmod \pi$; a finer
   Stokes-tangent fingerprint is deferred.
4. **Multi-edge degeneracies are out of scope.** Phase-3 M1/M2 introduce
   inter-edge degeneracy loci (equal-radius collisions between different
   edges' constellations); those are *not* among the four Phase-1 strata.

---

## 8. Pointers

- `compute_fingerprints.py` — analysis script (regenerate via `python compute_fingerprints.py`).
- `fingerprints.json` — full structured output (per-stratum records with all Jacobians and diagnostics).
- Phase-1 stress examples: `reports/conjectures.md` §"Stress-test report" (lines 287-298).
- Phase-3 gap G15: `reports/phase3_report.md` line 40.
