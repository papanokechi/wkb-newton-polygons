"""
compute_fingerprints.py
-----------------------
Local-invariant characterisation of the four Phase-1 degenerate strata of the
WKB-Newton polygon classification.

For each stratum representative chi(c), we compute:

(1) Jacobian J_alpha = d alpha / d c at the constellation roots (centered),
    answering the user-requested "Jacobian of chi under small Delta_ij shifts."

(2) Defining-function Jacobian dF/dbeta in the inner-coefficient space
    beta = (beta_1, ..., beta_r) of chi_w(w) = w^r + beta_1 w^{r-1} + ... + beta_r.
    From its rank we read off rigid (transverse, complex codim) directions and
    soft (tangent) directions. Equalmod is real-only and is rank-counted as a
    real Jacobian.

(3) Discrete fingerprint vector with degree, ramification, codimensions,
    rotational symmetry, and stratum incidence flags.

Output:
    fingerprints.json    -- structured numerical/discrete fingerprint
    degeneracy_fingerprints.md -- human-readable summary

Author : SIARC autopilot
Date   : 2026-05-26
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp

# ----------------------------------------------------------------------------
# 0. Symbolic primitives
# ----------------------------------------------------------------------------

c_var = sp.symbols("c")
w_var = sp.symbols("w")
t_var = sp.symbols("t")

EPS_RANK = 1e-9  # numerical SVD tolerance for rank


def beta_to_chi_w(betas):
    """chi_w(w) = w^r + beta_1 w^{r-1} + ... + beta_r."""
    r = len(betas)
    return w_var**r + sum(betas[k] * w_var ** (r - 1 - k) for k in range(r))


def chi_from_beta(betas, q):
    """chi(c) = chi_w(c^q)."""
    return beta_to_chi_w(betas).subs(w_var, c_var**q)


def _poly_coeffs_in_c(expr):
    """Return descending list of complex coefficients of expr in c_var."""
    p = sp.Poly(expr, c_var)
    return [complex(c) for c in p.all_coeffs()]


def _np_roots(expr):
    """Robust complex roots using numpy.roots (handles multiplicities).
       Returns list of length d (with multiplicities)."""
    coeffs = _poly_coeffs_in_c(expr)
    rs = np.roots(coeffs)
    return [complex(r) for r in rs]


def _exact_roots_with_multiplicity(expr):
    """Use sympy factoring to recover exact roots and multiplicities, then
       expand into a length-d list of (numerically coincident) complex roots
       suitable for the Vieta Jacobian computation.

       Returns list of length d = deg(expr) with multiplicities resolved
       (identical coincident roots, not numerically-perturbed near-duplicates).
    """
    poly = sp.Poly(expr, c_var)
    d = poly.degree()
    factor_dict = sp.roots(poly)  # {root_expr: multiplicity}
    if sum(factor_dict.values()) != d:
        # fallback: irreducible factor over Q[c]; resort to numpy.roots
        return _np_roots(expr)
    out = []
    for root_expr, mult in factor_dict.items():
        val = complex(sp.N(root_expr, 30))
        for _ in range(mult):
            out.append(val)
    return out


def _np_roots_w(beta_vals):
    """Roots of chi_w in w using numpy.roots."""
    coeffs = [1.0 + 0j] + [complex(b) for b in beta_vals]
    rs = np.roots(coeffs)
    return [complex(z) for z in rs]


def numeric_rank(A, tol=EPS_RANK):
    A = np.asarray(A, dtype=complex)
    if A.size == 0:
        return 0
    s = np.linalg.svd(A, compute_uv=False)
    smax = s.max() if s.size else 1.0
    return int(np.sum(s > tol * smax))


def real_rank(A, tol=EPS_RANK):
    A = np.asarray(A, dtype=float)
    if A.size == 0:
        return 0
    s = np.linalg.svd(A, compute_uv=False)
    smax = s.max() if s.size else 1.0
    return int(np.sum(s > tol * smax))


def complex_to_real_jac(Jc):
    """Convert a complex Jacobian d f / d x (with f, x complex) to the real
    Jacobian d (Re f, Im f) / d (Re x, Im x).

    If f is holomorphic in x: real-jac has the block form
        [[A, -B],
         [B,  A]]
    where Jc = A + i B.
    For non-holomorphic f (e.g. |w|^2), pass the explicit real-Jacobian instead.
    """
    Jc = np.asarray(Jc, dtype=complex)
    A = Jc.real
    B = Jc.imag
    top = np.concatenate([A, -B], axis=1)
    bot = np.concatenate([B,  A], axis=1)
    return np.concatenate([top, bot], axis=0)


# ----------------------------------------------------------------------------
# 1. Vieta Jacobian J_alpha = d alpha_k / d c_i  (the Delta_ij response)
# ----------------------------------------------------------------------------

def vieta_jacobian(roots):
    """Return J in C^{d x d} where chi(c) = prod_i (c - c_i)
                                          = c^d + alpha_1 c^{d-1} + ... + alpha_d
                                          (so alpha_k = (-1)^k e_k(roots))
       and J[k-1, i-1] = d alpha_k / d c_i,  k = 1..d,  i = 1..d.

       Closed form: alpha_k = (-1)^k e_k(c_1,...,c_d),
                    d alpha_k / d c_i = (-1)^k e_{k-1}(c without c_i).
    """
    d = len(roots)
    syms = sp.symbols(f"z0:{d}")
    poly = sp.Poly(sp.prod([t_var - z for z in syms]), t_var)
    coeffs = poly.all_coeffs()  # length d+1, leading = 1 (alpha_0)

    Jsym = sp.zeros(d, d)
    for k in range(1, d + 1):  # alpha_k
        for i in range(d):
            Jsym[k - 1, i] = sp.diff(coeffs[k], syms[i])

    subs = dict(zip(syms, roots))
    Jn = np.array(Jsym.subs(subs).evalf(30), dtype=object)
    return Jn.astype(complex)


def vieta_diagnostics(roots, label):
    """Compute rank of full Vieta Jacobian, of its restriction to the centered
       subspace T = {sum eps_i = 0}, and detect swap-kernel structure from
       coincident roots."""
    d = len(roots)
    J = vieta_jacobian(roots)
    full_rank = numeric_rank(J)

    # centered subspace T (dim d-1): any basis of C^{d-1} via "drop last column,
    # adjust"; project J onto T by composing with a (d x (d-1)) basis matrix B
    # whose columns span T.
    # Use B = [I_{d-1}; -1^T]  i.e. eps_d = -(eps_1 + ... + eps_{d-1}).
    B = np.zeros((d, d - 1), dtype=complex)
    B[:d - 1, :d - 1] = np.eye(d - 1)
    B[d - 1, :] = -1.0
    J_T = J @ B  # shape (d, d-1)
    rank_on_T = numeric_rank(J_T)

    # detect coincident roots (swap kernel dim)
    rs = np.array([complex(r) for r in roots])
    coincidences = 0
    seen = []
    multiplicities = []
    for r in rs:
        matched = False
        for k, (s, m) in enumerate(seen):
            if abs(r - s) < 1e-10:
                seen[k] = (s, m + 1)
                matched = True
                break
        if not matched:
            seen.append((r, 1))
    multiplicities = [m for _, m in seen]
    swap_kernel_dim = sum(m - 1 for m in multiplicities)

    return {
        "label": label,
        "d": d,
        "ordered_root_multiplicities": sorted(multiplicities, reverse=True),
        "swap_kernel_dim_predicted": swap_kernel_dim,
        "rank_full_Jacobian":        full_rank,
        "rank_on_centered_T":        rank_on_T,
        "ker_dim_on_centered_T":     (d - 1) - rank_on_T,
    }


# ----------------------------------------------------------------------------
# 2. Stratum-defining Jacobians in beta-space (CANONICAL)
# ----------------------------------------------------------------------------

def jac_zeroroot(beta_vals):
    """Stratum: zero inner root  <=>  beta_r = 0  (constant term of chi_w).
       F(beta) = beta_r.  dF/dbeta is the row e_r (last basis vector)."""
    r = len(beta_vals)
    dF_dbeta_complex = np.zeros((1, r), dtype=complex)
    dF_dbeta_complex[0, r - 1] = 1.0
    return {
        "F_description": "beta_r (constant term of chi_w)",
        "F_value_at_rep": complex(beta_vals[-1]),
        "dF_dbeta_complex": dF_dbeta_complex,
        "is_complex_algebraic": True,
    }


def jac_doubleroot(beta_vals):
    """Stratum: discriminant locus  <=>  disc_w(chi_w) = 0.
       F(beta) = disc_w(chi_w).  Compute dF/dbeta symbolically."""
    r = len(beta_vals)
    syms = sp.symbols(f"b1:{r + 1}")  # beta_1, ..., beta_r
    chi_w = w_var**r + sum(syms[k] * w_var ** (r - 1 - k) for k in range(r))
    Disc = sp.discriminant(chi_w, w_var)
    grad = [sp.diff(Disc, s) for s in syms]
    subs = dict(zip(syms, beta_vals))
    F_value = complex(Disc.subs(subs).evalf(30))
    dF = np.array([[complex(g.subs(subs).evalf(30)) for g in grad]], dtype=complex)
    return {
        "F_description": "disc_w(chi_w)",
        "F_value_at_rep": F_value,
        "dF_dbeta_complex": dF,
        "is_complex_algebraic": True,
    }


def jac_equalmod(beta_vals):
    """Stratum: equimodular inner roots  <=>  some |w_i|^2 = |w_j|^2.
       Real-analytic, not complex-algebraic.

       Defining functions at the representative: for the three inner roots
       w_1, w_2, w_3 (with all three equimodular at the rep), pick
           F_1 = |w_1|^2 - |w_2|^2
           F_2 = |w_2|^2 - |w_3|^2
       (a third pairwise equation is dependent on these two).

       Compute the real Jacobian dF / d(Re beta, Im beta) at the rep.
    """
    r = len(beta_vals)
    ws = _np_roots_w(beta_vals)
    # check: all equal modulus?
    mods = sorted([abs(z) for z in ws])
    assert max(mods) - min(mods) < 1e-8, "equalmod rep is not equimodular!"

    # Finite-difference dF / d(real, imag) of each beta_k
    h = 1e-6
    # F: beta -> R^{r-1}  (r-1 independent equimodular constraints among r roots)
    def F_real(b_complex):
        roots = _np_roots_w(b_complex)
        # sort roots by argument to maintain consistent labelling under perturb
        roots = sorted(roots, key=lambda z: (np.angle(z), abs(z)))
        mods2 = [abs(z) ** 2 for z in roots]
        return np.array([mods2[k] - mods2[k + 1] for k in range(len(roots) - 1)],
                        dtype=float)

    # Make a sorted reference labelling
    ws_ref = sorted(ws, key=lambda z: (np.angle(z), abs(z)))
    F0 = F_real(beta_vals)
    nF = len(F0)
    # Jacobian columns: 2r columns = (d/d Re beta_k, d/d Im beta_k)
    Jreal = np.zeros((nF, 2 * r), dtype=float)
    for k in range(r):
        bp = list(beta_vals); bp[k] = bp[k] + h
        bm = list(beta_vals); bm[k] = bm[k] - h
        Jreal[:, k]       = (F_real(bp) - F_real(bm)) / (2 * h)
        bp = list(beta_vals); bp[k] = bp[k] + 1j * h
        bm = list(beta_vals); bm[k] = bm[k] - 1j * h
        Jreal[:, r + k]   = (F_real(bp) - F_real(bm)) / (2 * h)
    return {
        "F_description": "|w_i|^2 - |w_{i+1}|^2 (i=1..r-1), real-analytic",
        "F_value_at_rep": F0.tolist(),
        "dF_dbeta_real": Jreal,
        "is_complex_algebraic": False,
    }


def jac_accidental_sym(beta_vals):
    """Stratum: C_d-inflation by sparse chi_w  <=>  beta_1 = ... = beta_{r-1} = 0
       (chi_w = w^r + beta_r).
       F(beta) = (beta_1, ..., beta_{r-1}).  dF/dbeta = [I_{r-1} | 0]."""
    r = len(beta_vals)
    dF = np.zeros((r - 1, r), dtype=complex)
    for k in range(r - 1):
        dF[k, k] = 1.0
    return {
        "F_description": "beta_1, beta_2, ..., beta_{r-1}  (sparsity to a single-binomial inner polynomial)",
        "F_value_at_rep": [complex(b) for b in beta_vals[:-1]],
        "dF_dbeta_complex": dF,
        "is_complex_algebraic": True,
    }


# ----------------------------------------------------------------------------
# 3. Delta_ij multiset fingerprint
# ----------------------------------------------------------------------------

def delta_fingerprint(roots):
    rs = np.array([complex(r) for r in roots])
    d = len(rs)
    pairs = [(i, j) for i in range(d) for j in range(i + 1, d)]
    deltas = [rs[i] - rs[j] for (i, j) in pairs]
    mods = [abs(z) for z in deltas]
    args = [(np.angle(z) % np.pi) if abs(z) > 1e-12 else float("nan")
            for z in deltas]  # mod pi because c_i-c_j and c_j-c_i differ by sign

    def count_distinct(xs, tol=1e-8):
        xs_sorted = sorted([x for x in xs if not (isinstance(x, float) and np.isnan(x))])
        if not xs_sorted:
            return 0
        cnt = 1
        for a, b in zip(xs_sorted, xs_sorted[1:]):
            if abs(b - a) > tol:
                cnt += 1
        return cnt

    n_zero_delta = sum(1 for m in mods if m < 1e-10)
    return {
        "n_pairs": len(pairs),
        "distinct_moduli": count_distinct(mods),
        "distinct_args_mod_pi": count_distinct([a for a in args if not np.isnan(a)]),
        "n_zero_delta_pairs": n_zero_delta,
        "min_nonzero_modulus": float(min((m for m in mods if m > 1e-10),
                                         default=0.0)),
        "max_modulus": float(max(mods)) if mods else 0.0,
    }


# ----------------------------------------------------------------------------
# 4. Incidence flags  (overlaps between strata at the representative)
# ----------------------------------------------------------------------------

def incidence_flags(beta_vals, q):
    """Detect which of the four named conditions hold at this representative.
       Returns dict of booleans + the inner-root multiset for context."""
    ws = _np_roots_w(beta_vals)
    mods = sorted([abs(z) for z in ws])

    has_zero_root = any(abs(z) < 1e-9 for z in ws)
    # multiple inner root?
    chi_w_local = beta_to_chi_w(beta_vals)
    disc = complex(sp.discriminant(chi_w_local, w_var).evalf(30))
    has_double = abs(disc) < 1e-9
    # equimodular pair?
    has_equimod = False
    for i in range(len(ws)):
        for j in range(i + 1, len(ws)):
            if abs(ws[i] - ws[j]) > 1e-9 and abs(abs(ws[i]) - abs(ws[j])) < 1e-9:
                has_equimod = True
                break
    # accidental_sym (C_d inflation): chi_w is a binomial w^r + beta_r
    has_acc_sym = all(abs(b) < 1e-9 for b in beta_vals[:-1])

    return {
        "zero_root":       has_zero_root,
        "disc_zero":       has_double,
        "equimodular":     has_equimod,
        "C_d_sparse":      has_acc_sym,
        "inner_roots":     [(float(z.real), float(z.imag)) for z in ws],
        "inner_disc":      [disc.real, disc.imag],
    }


# ----------------------------------------------------------------------------
# 5. Drive: configure the four strata and compute everything
# ----------------------------------------------------------------------------

# beta convention: chi_w(w) = w^r + beta_1 w^{r-1} + ... + beta_r.
# Matching to representative polynomials:
#   STRESS_zeroroot:       chi = c^4 - c^2          => chi_w = w^2 - w,        beta = (-1,  0)
#   STRESS_doubleroot:     chi = c^9 - 4c^6+5c^3-2  => chi_w = w^3-4w^2+5w-2, beta = (-4,  5, -2)
#   STRESS_equalmod:       chi = c^6 - 2c^4+4c^2-8  => chi_w = w^3-2w^2+4w-8, beta = (-2,  4, -8)
#   STRESS_accidental_sym: chi = c^6 + 1            => chi_w = w^3 + 1,        beta = ( 0,  0,  1)

STRATA = [
    {
        "key": "STRESS_zeroroot",
        "type": "zero_inner_root",
        "chi_expr": c_var**4 - c_var**2,
        "q": 2, "r": 2, "d": 4,
        "beta": [sp.Integer(-1), sp.Integer(0)],
        "ring_partition": [2, 2],
        "C_n_observed": 2,
        "jac_fn": jac_zeroroot,
        "description": "Inner polynomial has a root at 0; the c=0 sector of the constellation is q-fold degenerate.",
    },
    {
        "key": "STRESS_doubleroot",
        "type": "discriminant_locus",
        "chi_expr": c_var**9 - 4*c_var**6 + 5*c_var**3 - 2,
        "q": 3, "r": 3, "d": 9,
        "beta": [sp.Integer(-4), sp.Integer(5), sp.Integer(-2)],
        "ring_partition": [6, 3],
        "C_n_observed": 3,
        "jac_fn": jac_doubleroot,
        "description": "Inner polynomial has a repeated root (chi_w = (w-1)^2(w-2)); two mu_q-orbits coalesce.",
    },
    {
        "key": "STRESS_equalmod",
        "type": "equimodular_inner_roots",
        "chi_expr": c_var**6 - 2*c_var**4 + 4*c_var**2 - 8,
        "q": 2, "r": 3, "d": 6,
        "beta": [sp.Integer(-2), sp.Integer(4), sp.Integer(-8)],
        "ring_partition": [6],
        "C_n_observed": 2,
        "jac_fn": jac_equalmod,
        "description": "All three inner roots {2, +2i, -2i} have |w|=2; three mu_q-orbits collapse to one radius.",
    },
    {
        "key": "STRESS_accidental_sym",
        "type": "C_d_inflation_via_sparse_chi_w",
        "chi_expr": c_var**6 + 1,
        "q": 2, "r": 3, "d": 6,
        "beta": [sp.Integer(0), sp.Integer(0), sp.Integer(1)],
        "ring_partition": [6],
        "C_n_observed": 6,
        "jac_fn": jac_accidental_sym,
        "description": "chi_w is a binomial w^r + beta_r; rotational symmetry inflates from C_q to C_d=C_{qr}.",
    },
]


def analyse(s):
    key = s["key"]
    q, r, d = s["q"], s["r"], s["d"]
    beta_vals = s["beta"]

    # 1. Vieta Jacobian on c-roots (centered)
    c_roots = _exact_roots_with_multiplicity(s["chi_expr"])
    vieta = vieta_diagnostics(c_roots, key)

    # 2. Defining Jacobian on beta-space
    jac = s["jac_fn"](beta_vals)
    if jac["is_complex_algebraic"]:
        # complex Jacobian dF/dbeta: count complex rank
        dF_C = jac["dF_dbeta_complex"]
        rank_C = numeric_rank(dF_C)
        codim_C = rank_C
        codim_R = 2 * rank_C  # complex equations -> 2 real equations each
        soft_dim_C_in_beta = r - rank_C
        # convert to real Jacobian for unified soft-direction count
        dF_R = complex_to_real_jac(dF_C)
        rank_R = real_rank(dF_R)
        soft_dim_R_in_beta = 2 * r - rank_R
    else:
        # real Jacobian only
        dF_R = jac["dF_dbeta_real"]
        rank_R = real_rank(dF_R)
        codim_C = 0  # not complex-algebraic
        codim_R = rank_R
        rank_C = None
        soft_dim_C_in_beta = None
        soft_dim_R_in_beta = 2 * r - rank_R

    # 3. Delta-fingerprint
    delta = delta_fingerprint(c_roots)

    # 4. Incidence flags
    inc = incidence_flags(beta_vals, q)

    # 5. Rigidity class (semantic)
    #   - "very_rigid"     : codim_C >= 2  (more than one independent complex equation)
    #   - "rigid_codim_1"  : codim_C == 1  (single complex-algebraic hypersurface)
    #   - "real_only"      : codim_C == 0 but codim_R >= 1 (real-analytic only)
    #   - "open"           : no codim at all
    if codim_C >= 2:
        rigidity = "very_rigid"
    elif codim_C == 1:
        rigidity = "rigid_codim_1"
    elif codim_R >= 1:
        rigidity = "real_only"
    else:
        rigidity = "open"

    fp_vector = [
        d, q, r,
        codim_C,
        codim_R,
        int(rank_R),
        (soft_dim_C_in_beta if soft_dim_C_in_beta is not None else -1),
        int(soft_dim_R_in_beta),
        int(s["C_n_observed"]),
        int(jac["is_complex_algebraic"]),
        delta["distinct_moduli"],
        delta["distinct_args_mod_pi"],
        delta["n_zero_delta_pairs"],
        vieta["rank_on_centered_T"],
        vieta["ker_dim_on_centered_T"],
        vieta["swap_kernel_dim_predicted"],
        int(inc["zero_root"]),
        int(inc["disc_zero"]),
        int(inc["equimodular"]),
        int(inc["C_d_sparse"]),
    ]

    return {
        "key": key,
        "type": s["type"],
        "description": s["description"],
        "chi": sp.sstr(s["chi_expr"]),
        "chi_w": sp.sstr(beta_to_chi_w(beta_vals)),
        "d": d, "q": q, "r": r,
        "beta_at_rep": [complex(b).real if abs(complex(b).imag) < 1e-12 else (complex(b).real, complex(b).imag)
                        for b in beta_vals],
        "ring_partition": s["ring_partition"],
        "C_n_observed": s["C_n_observed"],
        "defining_function":            jac["F_description"],
        "F_value_at_rep":               jac["F_value_at_rep"]
            if not hasattr(jac["F_value_at_rep"], "tolist") else jac["F_value_at_rep"],
        "is_complex_algebraic":         jac["is_complex_algebraic"],
        "rank_dF_dbeta_complex":        rank_C,
        "rank_dF_dbeta_real":           int(rank_R),
        "codim_C_in_beta_space":        codim_C,
        "codim_R_in_beta_space":        codim_R,
        "soft_dim_C_in_beta_space":     soft_dim_C_in_beta,
        "soft_dim_R_in_beta_space":     int(soft_dim_R_in_beta),
        "vieta_jacobian_on_c_roots":    vieta,
        "delta_multiset":               delta,
        "incidence_flags":              {k: bool(v) if isinstance(v, (bool, np.bool_)) else v
                                         for k, v in inc.items()
                                         if k in ("zero_root", "disc_zero", "equimodular", "C_d_sparse")},
        "inner_roots":                  inc["inner_roots"],
        "inner_disc":                   inc["inner_disc"],
        "rigidity_class":               rigidity,
        "fingerprint_vector":           fp_vector,
        "fingerprint_vector_layout": [
            "d", "q", "r",
            "codim_C_in_beta", "codim_R_in_beta",
            "rank_dF_real",
            "soft_dim_C_in_beta", "soft_dim_R_in_beta",
            "C_n",
            "is_complex_algebraic",
            "delta_distinct_moduli",
            "delta_distinct_args_mod_pi",
            "delta_zero_pairs",
            "vieta_rank_on_T",
            "vieta_ker_dim_on_T",
            "vieta_swap_kernel_dim",
            "inc_zero_root", "inc_disc_zero", "inc_equimod", "inc_C_d_sparse",
        ],
    }


def main():
    out = []
    for s in STRATA:
        rec = analyse(s)
        out.append(rec)

    here = Path(__file__).parent
    json_path = here / "fingerprints.json"
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"Wrote {json_path}")

    # Console preview
    print()
    print("=" * 96)
    print("DEGENERACY FINGERPRINT TABLE")
    print("=" * 96)
    print(f"{'key':24s} {'(d,q,r)':>8s} {'codimC':>7s} {'codimR':>7s}"
          f" {'soft C/R (beta)':>16s} {'C_n':>4s}"
          f" {'Vieta rk/ker (T)':>17s} {'incid(z,d,e,s)':>16s} {'rigidity':>14s}")
    for rec in out:
        inc = rec["incidence_flags"]
        inc_str = "({},{},{},{})".format(
            int(inc["zero_root"]), int(inc["disc_zero"]),
            int(inc["equimodular"]), int(inc["C_d_sparse"]))
        dqr = f"({rec['d']},{rec['q']},{rec['r']})"
        soft = (f"{rec['soft_dim_C_in_beta_space']}/"
                f"{rec['soft_dim_R_in_beta_space']}"
                if rec['soft_dim_C_in_beta_space'] is not None
                else f"-/{rec['soft_dim_R_in_beta_space']}")
        v = rec["vieta_jacobian_on_c_roots"]
        vrk = f"{v['rank_on_centered_T']}/{v['ker_dim_on_centered_T']}"
        print(f"{rec['key']:24s} {dqr:>8s} {rec['codim_C_in_beta_space']:>7} "
              f"{rec['codim_R_in_beta_space']:>7} {soft:>16s} "
              f"{rec['C_n_observed']:>4} {vrk:>17s} {inc_str:>16s} {rec['rigidity_class']:>14s}")
    print()
    print("Fingerprint vector layout:", out[0]["fingerprint_vector_layout"])
    for rec in out:
        print(f"  {rec['key']:24s} -> {rec['fingerprint_vector']}")


if __name__ == "__main__":
    main()
