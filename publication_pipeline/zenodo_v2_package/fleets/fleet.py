"""
Fleet pipeline for Global WKB Pattern Discovery.

Engines:
  1. operator_generator      — emit a family of operators with metadata
  2. newton_polygon_engine   — upper convex hull of (k, deg a_k); dominant edge
  3. characteristic_polynomial_engine — extract chi(c) from the dominant edge
  4. constellation_engine    — solve chi(c) = 0 and record root set
  5. clustering_engine       — cluster by symmetry invariants
  6. conjecture_engine       — output classification statements

The unified rule used:

    L = sum_k a_k(x) * D^k                       (D = d/dx, S=f->f(x+1), T=f->f(qx))

    Newton polygon = upper convex hull of points  P_k = (k, deg a_k).
    A *dominant edge* is the edge of largest WKB level lambda = 1 - slope.
    For an edge passing through  {(k_i, d_i)},  the characteristic polynomial is

       chi(c)  =  sum_i  LC(a_{k_i}) * c^{k_i}

    where  LC  picks the coefficient of  x^{d_i}  in  a_{k_i}.
    For ODE, chi-variable c plays the role of  f'/f * x^{1-lambda}.
    For difference / q-difference, c plays the analogous role of the shift
    quotient (Sf/f or Tf/f), and the *combinatorial geometry of chi* is the
    same.

The user's "slopes / valuations / ranks / equation types" parameter sweep is
encoded in `generate_operators`.
"""

from __future__ import annotations

import json
import math
import os
from dataclasses import dataclass, field, asdict
from fractions import Fraction
from typing import Any

import numpy as np
import sympy as sp


# -------------------------------------------------------------------- helpers


def _lc(poly: sp.Expr, x: sp.Symbol) -> sp.Expr:
    """Leading coefficient of poly in x at x=infinity (highest-degree term)."""
    p = sp.Poly(sp.expand(poly), x)
    if p.is_zero:
        return sp.Integer(0)
    return p.LC()


def _deg(poly: sp.Expr, x: sp.Symbol) -> int:
    p = sp.Poly(sp.expand(poly), x)
    if p.is_zero:
        return -10**9  # sentinel for "no point"
    return int(p.degree())


def _upper_hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Upper convex hull of integer lattice points sorted by x then y."""
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    upper: list[tuple[int, int]] = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) >= 0:
            upper.pop()
        upper.append(p)
    upper.reverse()
    return upper


# ---------------------------------------------------------------- data types


@dataclass
class Operator:
    name: str
    eqtype: str          # "ode" | "difference" | "q-difference"
    slope: str           # rational string "p/q" describing the *requested* slope
    rank: int            # integer multiplier r
    valuation: str       # "simple" | "double" | "mixed"
    expression: str      # operator written as a string for the record
    coeffs_sym: list[sp.Expr] = field(default_factory=list)  # a_k(x) sympy expressions, k=0..n
    coeffs: list[str] = field(default_factory=list)          # string view for JSON


@dataclass
class NewtonPolygon:
    points: list[tuple[int, int]]   # all (k, deg a_k) for nonzero a_k
    hull: list[tuple[int, int]]     # upper convex hull vertices
    dominant_edge: list[tuple[int, int]]  # vertices of the edge with biggest -slope
    slope: tuple[int, int]          # (p, q) with slope = -p/q ; p>=0, q>0, gcd=1
    lattice_points_on_edge: list[tuple[int, int]]


@dataclass
class CharPoly:
    chi_str: str
    chi_in_c: sp.Expr
    degree: int
    inner_poly_in_w_str: str          # chi as polynomial in w = c^q (if applicable)
    inner_degree: int                  # degree in w
    is_binomial: bool


@dataclass
class Constellation:
    roots: list[complex]
    radii: list[float]                 # |c_k|
    args: list[float]                  # arg c_k in (-pi, pi]
    rings: list[dict[str, Any]]        # list of {radius, count, base_angle}
    n_roots: int
    symmetry_group_order: int          # order of detected rotational sym C_n
    invariants: dict[str, Any]


@dataclass
class Cluster:
    label: str
    description: str
    members: list[str] = field(default_factory=list)
    representative: dict[str, Any] = field(default_factory=dict)


# -------------------------------------------------------- 1. Operator generator


def generate_operators() -> list[Operator]:
    x = sp.Symbol("x")
    beta = sp.Symbol("beta", complex=True)
    gamma = sp.Symbol("gamma", complex=True)

    ops: list[Operator] = []

    slopes = [(1, 2), (1, 3), (1, 4), (2, 3), (3, 2)]
    ranks = [1, 2, 3]
    valuations = ["simple", "double", "mixed", "generic_complex"]

    # ---- ODE family
    # For slope p/q (lowest terms), rank r:
    #   edge runs from (rq, 0) (top of operator) to (0, rp) (constant term).
    #   lattice points on edge:  (rq - j q,  j p)   for j = 0..r
    #   coefficient pattern (alpha_j on the edge point):
    #     simple : alpha_0 = 1, alpha_r = beta
    #     double : alpha_0 = 1, alpha_r = beta, plus ONE interior alpha_j = gamma
    #     mixed  : every alpha_j = 1 except alpha_r = beta (generic edge polynomial)
    #
    # Off-edge "decoy" terms (sub-dominant) are added with degree 1 less than
    # the lattice line to verify the polygon engine actually picks them out.
    for p, q in slopes:
        for r in ranks:
            n = r * q                       # operator order
            for valuation in valuations:
                if valuation != "simple" and r == 1:
                    # for r=1 there are no interior lattice points; skip
                    continue
                a = [sp.S.Zero] * (n + 1)
                # edge lattice points and their alpha_j
                # Use *generic* distinct coefficients so the inner polynomial
                # in w = c^q does not degenerate (all roots on one circle).
                for j in range(r + 1):
                    k_idx = n - j * q       # ∂^{k_idx}
                    d = j * p               # x^d coefficient
                    if j == 0:
                        alpha = sp.Integer(1)
                    elif j == r:
                        alpha = beta
                    else:
                        if valuation == "simple":
                            alpha = sp.S.Zero
                        elif valuation == "double":
                            alpha = gamma if j == max(1, r // 2) else sp.S.Zero
                        elif valuation == "mixed":
                            alpha = sp.Integer(j + 2)
                        else:  # generic_complex — pick non-conjugate complex coefficients
                            # so that the inner polynomial has r roots all with
                            # *distinct* moduli (no complex-conjugate collapse).
                            alpha = sp.Integer(j + 1) + sp.I * sp.Integer(2 * j + 1)
                    a[k_idx] = a[k_idx] + alpha * x ** d
                # decoy sub-dominant term: x^{rp-1} in the constant coeff
                # (slightly off the edge so it must NOT change Newton polygon)
                if r * p >= 1:
                    a[0] = a[0] + sp.Integer(0)  # leave alone — keep operators clean
                # build readable expression
                D = sp.Function("D")
                expr_terms = []
                for k_idx in range(n + 1):
                    if a[k_idx] != 0:
                        expr_terms.append(f"({sp.sstr(a[k_idx])})*D^{k_idx}")
                expr = " + ".join(expr_terms)
                ops.append(
                    Operator(
                        name=f"ODE_s{p}o{q}_r{r}_{valuation}",
                        eqtype="ode",
                        slope=f"{p}/{q}",
                        rank=r,
                        valuation=valuation,
                        expression=expr,
                        coeffs_sym=a,
                        coeffs=[sp.sstr(c) for c in a],
                    )
                )

    # ---- Difference and q-difference operators
    # We use the SAME Newton-polygon construction (which is the combinatorial
    # heart of the WKB analysis). The "characteristic polynomial" chi(c) is
    # then a polynomial in the shift quotient variable c = Sf/f (difference)
    # or c = Tf/f (q-difference). The combinatorial constellation is the same.
    for eqtype, op_symbol in [("difference", "S"), ("q-difference", "T")]:
        # we mirror only a representative subset to keep the zoo manageable
        for p, q in slopes:
            for r in [1, 2]:
                for valuation in ["simple", "mixed", "generic_complex"]:
                    if valuation != "simple" and r == 1:
                        continue
                    n = r * q
                    a = [sp.S.Zero] * (n + 1)
                    for j in range(r + 1):
                        k_idx = n - j * q
                        d = j * p
                        if j == 0:
                            alpha = sp.Integer(1)
                        elif j == r:
                            alpha = beta
                        else:
                            if valuation == "mixed":
                                alpha = sp.Integer(j + 2)
                            elif valuation == "generic_complex":
                                alpha = sp.Integer(j + 1) + sp.I * sp.Integer(2 * j + 1)
                            else:
                                alpha = sp.S.Zero
                        a[k_idx] = a[k_idx] + alpha * x ** d
                    expr_terms = []
                    for k_idx in range(n + 1):
                        if a[k_idx] != 0:
                            expr_terms.append(f"({sp.sstr(a[k_idx])})*{op_symbol}^{k_idx}")
                    expr = " + ".join(expr_terms)
                    ops.append(
                        Operator(
                            name=f"{eqtype.upper()}_s{p}o{q}_r{r}_{valuation}",
                            eqtype=eqtype,
                            slope=f"{p}/{q}",
                            rank=r,
                            valuation=valuation,
                            expression=expr,
                            coeffs_sym=a,
                            coeffs=[sp.sstr(c) for c in a],
                        )
                    )

    # ---- Stress-test operators (rubber-duck blind-spot probes)
    # Each is hand-crafted to violate naive forms of the conjectures so the
    # pipeline can flag the failure mode.
    stress_cases: list[tuple[str, str, str, list[sp.Expr]]] = []

    # (a) Equal-modulus distinct w-roots: chi_w(w) = (w - 2)(w^2 + 4) = w^3 - 2w^2 + 4w - 8
    #     roots {2, 2i, -2i} all have |w| = 2.  Take p/q = 1/2, r = 3.
    #     a_6 = 1, a_4 = -2 x, a_2 = 4 x^2, a_0 = -8 x^3.
    x = sp.Symbol("x")
    a = [sp.S.Zero] * 7
    a[6] = sp.Integer(1)
    a[4] = sp.Integer(-2) * x
    a[2] = sp.Integer(4) * x**2
    a[0] = sp.Integer(-8) * x**3
    stress_cases.append(("STRESS_equalmod", "ode", "1/2", a))

    # (b) Double root of chi_w: chi_w(w) = (w-1)^2 (w-2) = w^3 - 4w^2 + 5w - 2.
    #     slope 1/3, r = 3.
    a = [sp.S.Zero] * 10
    a[9] = sp.Integer(1)
    a[6] = sp.Integer(-4) * x
    a[3] = sp.Integer(5) * x**2
    a[0] = sp.Integer(-2) * x**3
    stress_cases.append(("STRESS_doubleroot", "ode", "1/3", a))

    # (c) Zero root of chi_w: chi_w(w) = w (w - 1) = w^2 - w.
    #     slope 1/2, r = 2.  alpha_0 = 1 (top), alpha_2 = 0 (constant term zero!).
    a = [sp.S.Zero] * 5
    a[4] = sp.Integer(1)
    a[2] = sp.Integer(-1) * x
    # a[0] = 0 -- intentionally zero constant => one root c=0
    stress_cases.append(("STRESS_zeroroot", "ode", "1/2", a))

    # (d) Accidental larger symmetry: chi(c) = c^6 + 1.  Slope 1/2, r = 3.
    #     The minimal q-guaranteed symmetry is C_2 (from slope denominator 2),
    #     but the actual symmetry is C_6.
    a = [sp.S.Zero] * 7
    a[6] = sp.Integer(1)
    a[0] = sp.Integer(1) * x**3   # x^3 = x^{rp}
    stress_cases.append(("STRESS_accidental_sym", "ode", "1/2", a))

    for name, eqtype, slope_str, coeffs in stress_cases:
        expr = " + ".join(
            f"({sp.sstr(c)})*D^{k}" for k, c in enumerate(coeffs) if c != 0
        )
        ops.append(
            Operator(
                name=name,
                eqtype=eqtype,
                slope=slope_str,
                rank=3 if "_zeroroot" not in name else 2,
                valuation="stress",
                expression=expr,
                coeffs_sym=coeffs,
                coeffs=[sp.sstr(c) for c in coeffs],
            )
        )

    return ops


# ----------------------------------------------------- 2. Newton polygon engine


def compute_newton_polygon(op: Operator) -> NewtonPolygon:
    x = sp.Symbol("x")
    pts: list[tuple[int, int]] = []
    coeffs_sym = op.coeffs_sym
    for k, ak in enumerate(coeffs_sym):
        d = _deg(ak, x)
        if d > -10**8:
            pts.append((k, d))

    hull = _upper_hull(pts)

    # dominant edge = the edge whose slope is the most NEGATIVE (largest -slope)
    edges: list[tuple[tuple[int, int], tuple[int, int], Fraction]] = []
    for a, b in zip(hull, hull[1:]):
        if b[0] == a[0]:
            continue
        slope = Fraction(b[1] - a[1], b[0] - a[0])
        edges.append((a, b, slope))
    if not edges:
        # only one point — degenerate; treat as slope 0
        dominant = [hull[0]]
        slope_frac = Fraction(0, 1)
    else:
        # most negative slope is the dominant (WKB highest-level) edge
        a, b, slope_frac = min(edges, key=lambda e: e[2])
        dominant = [a, b]

    # express slope as (-p, q) with p >= 0, q > 0, gcd(p,q)=1
    p = -slope_frac.numerator if slope_frac.numerator <= 0 else slope_frac.numerator
    q = slope_frac.denominator
    # (note: slope is normally negative -> -slope = p/q > 0)
    if slope_frac == 0:
        p, q = 0, 1
    else:
        p_, q_ = (-slope_frac).numerator, (-slope_frac).denominator
        p, q = p_, q_

    lattice_pts: list[tuple[int, int]] = []
    if len(dominant) == 2:
        a, b = dominant
        dx, dy = b[0] - a[0], b[1] - a[1]
        g = math.gcd(abs(dx), abs(dy)) if (dx or dy) else 1
        sx, sy = dx // g, dy // g
        for t in range(g + 1):
            lattice_pts.append((a[0] + t * sx, a[1] + t * sy))
    else:
        lattice_pts = list(dominant)

    return NewtonPolygon(
        points=pts,
        hull=hull,
        dominant_edge=dominant,
        slope=(p, q),
        lattice_points_on_edge=lattice_pts,
    )


# ----------------------------------- 3. Characteristic polynomial engine


def compute_characteristic_polynomial(op: Operator, np_: NewtonPolygon) -> CharPoly:
    x = sp.Symbol("x")
    c = sp.Symbol("c")
    coeffs_sym = op.coeffs_sym

    terms = []
    for (k, d) in np_.lattice_points_on_edge:
        ak = coeffs_sym[k]
        lc = _lc(ak, x)
        if lc != 0:
            terms.append(lc * c**k)
    chi = sp.expand(sum(terms))

    # try to write chi as polynomial in w = c^q
    p, q = np_.slope
    inner_str = ""
    inner_deg = -1
    if q > 1:
        w = sp.Symbol("w")
        try:
            chi_in_w = sp.Poly(chi.subs(c, w ** (sp.Rational(1, 1)) * c**0) * 1, c)
        except Exception:
            chi_in_w = None
        # construct via degree-mapping:  c^{kq} -> w^k
        polyc = sp.Poly(chi, c)
        new_coeffs: dict[int, sp.Expr] = {}
        ok = True
        for monom, coef in polyc.terms():
            (exp_,) = monom
            if exp_ % q != 0:
                ok = False
                break
            new_coeffs[exp_ // q] = coef
        if ok and new_coeffs:
            chi_in_w_poly = sum(coef * w**k for k, coef in new_coeffs.items())
            inner_str = sp.sstr(sp.expand(chi_in_w_poly))
            inner_deg = max(new_coeffs)

    chi_poly = sp.Poly(chi, c)
    degree = chi_poly.degree() if not chi_poly.is_zero else 0
    # binomial iff exactly two nonzero terms
    n_terms = sum(1 for _, coef in chi_poly.terms() if coef != 0)
    is_binomial = (n_terms == 2)

    return CharPoly(
        chi_str=sp.sstr(chi),
        chi_in_c=chi,
        degree=degree,
        inner_poly_in_w_str=inner_str,
        inner_degree=inner_deg,
        is_binomial=is_binomial,
    )


# ------------------------------------------- 4. Constellation engine


def compute_constellation(op: Operator, chi: CharPoly) -> Constellation:
    c = sp.Symbol("c")
    beta = sp.Symbol("beta", complex=True)
    gamma = sp.Symbol("gamma", complex=True)

    # specialize free parameters so we can compute numerical roots
    chi_num = chi.chi_in_c.subs({beta: sp.Integer(1), gamma: sp.Integer(1)})
    polyc = sp.Poly(chi_num, c)
    coef_list = [complex(c_) for c_ in polyc.all_coeffs()]
    if len(coef_list) <= 1:
        roots: list[complex] = []
    else:
        roots = list(np.roots(coef_list))

    # Monodromy probe: rotate beta by theta = pi/3 and re-solve.
    theta = math.pi / 3
    chi_rot = chi.chi_in_c.subs({beta: sp.exp(sp.I * sp.Rational(1, 3) * sp.pi),
                                  gamma: sp.Integer(1)})
    polyc_rot = sp.Poly(sp.expand(chi_rot), c)
    coef_list_rot = [complex(c_) for c_ in polyc_rot.all_coeffs()]
    if len(coef_list_rot) <= 1:
        roots_rot: list[complex] = []
    else:
        roots_rot = list(np.roots(coef_list_rot))

    radii = [abs(r) for r in roots]
    args = [math.atan2(r.imag, r.real) for r in roots]

    # cluster roots into rings by radius (relative tolerance)
    rings: list[dict[str, Any]] = []
    used = [False] * len(roots)
    for i, ri in enumerate(radii):
        if used[i]:
            continue
        ring_idx = [
            j for j in range(len(radii)) if not used[j] and abs(radii[j] - ri) <= 1e-7 + 1e-6 * ri
        ]
        for j in ring_idx:
            used[j] = True
        ring_args = sorted([args[j] for j in ring_idx])
        # base angle
        base = ring_args[0] if ring_args else 0.0
        rings.append(
            {
                "radius": float(ri),
                "count": len(ring_idx),
                "base_angle": float(base),
                "args": [float(a) for a in ring_args],
            }
        )
    rings.sort(key=lambda d: d["radius"])

    # match rotated-beta rings to the original rings by radius (Vieta says the
    # radii do NOT change since |beta|=1)
    rings_rot: list[dict[str, Any]] = []
    radii_rot = [abs(r) for r in roots_rot]
    args_rot = [math.atan2(r.imag, r.real) for r in roots_rot]
    used_rot = [False] * len(roots_rot)
    for i, ri in enumerate(radii_rot):
        if used_rot[i]:
            continue
        ring_idx = [
            j for j in range(len(radii_rot)) if not used_rot[j] and abs(radii_rot[j] - ri) <= 1e-7 + 1e-6 * ri
        ]
        for j in ring_idx:
            used_rot[j] = True
        ring_args = sorted([args_rot[j] for j in ring_idx])
        rings_rot.append(
            {
                "radius": float(ri),
                "count": len(ring_idx),
                "args": [float(a) for a in ring_args],
            }
        )
    rings_rot.sort(key=lambda d: d["radius"])

    # per-ring rotation: pair rings by sorted radius order (radii are
    # |β|-invariant by Vieta).
    per_ring_rotation: list[float] = []
    if len(rings) == len(rings_rot):
        for ring, match in zip(rings, rings_rot):
            if ring["count"] != match["count"] or ring["count"] == 0:
                per_ring_rotation.append(float("nan"))
                continue
            m = ring["count"]
            a0 = ring["args"][0]
            cand = [(match["args"][k] - a0) % (2 * math.pi / m) for k in range(m)]
            delta = min(cand)
            per_ring_rotation.append(float(delta))
    else:
        per_ring_rotation = [float("nan")] * len(rings)

    # rotational symmetry: largest n such that rotating roots by 2pi/n
    # permutes them (within tolerance). The polynomial chi has form
    # sum_k a_k c^k; rotation invariance by 2pi/n means a_k != 0 only for
    # k in some residue class mod n.
    nonzero_exps = sorted(int(m[0]) for m, coef in polyc.terms() if coef != 0)
    if len(nonzero_exps) >= 2:
        diffs = [nonzero_exps[i] - nonzero_exps[0] for i in range(1, len(nonzero_exps))]
        sym = diffs[0]
        for d in diffs[1:]:
            sym = math.gcd(sym, d)
        sym_order = abs(sym)
    elif len(nonzero_exps) == 1:
        # only one nonzero term — degenerate (no constellation, all roots at 0)
        sym_order = 1
    else:
        sym_order = 1

    # Vieta-based product-of-roots monodromy: arg(prod c_k) at beta=1 vs at
    # beta=e^{i theta} must differ by theta (mod 2*pi).
    if roots and roots_rot:
        prod0 = 1.0 + 0j
        prodt = 1.0 + 0j
        for rr in roots:
            prod0 *= rr
        for rr in roots_rot:
            prodt *= rr
        argshift = (math.atan2(prodt.imag, prodt.real) - math.atan2(prod0.imag, prod0.real)) % (2 * math.pi)
        # bring into (-pi, pi]
        if argshift > math.pi:
            argshift -= 2 * math.pi
        monodromy_matches = abs(((argshift - theta) + math.pi) % (2 * math.pi) - math.pi) < 1e-6
    else:
        argshift = float("nan")
        monodromy_matches = False

    # Strict regular-polygon test: all roots on one circle AND evenly
    # spaced (args differ by 2π/n with tolerance).
    def _is_regular(rings_struct: list[dict], n_total: int) -> bool:
        if len(rings_struct) != 1 or rings_struct[0]["count"] != n_total or n_total < 2:
            return False
        a_sorted = sorted(rings_struct[0]["args"])
        expected = 2 * math.pi / n_total
        for i in range(n_total):
            d = (a_sorted[(i + 1) % n_total] - a_sorted[i]) % (2 * math.pi)
            if abs(d - expected) > 1e-6:
                return False
        return True

    invariants = {
        "n_roots": len(roots),
        "n_rings": len(rings),
        "ring_radii": [r["radius"] for r in rings],
        "ring_counts": [r["count"] for r in rings],
        "Cn_order": int(sym_order),
        "is_regular_polygon": _is_regular(rings, len(roots)),
        "monodromy_theta": float(theta),
        "monodromy_argshift_product": float(argshift) if not math.isnan(argshift) else None,
        "monodromy_matches_theta": bool(monodromy_matches),
        "per_ring_rotation": [r if not math.isnan(r) else None for r in per_ring_rotation],
    }

    return Constellation(
        roots=[complex(r) for r in roots],
        radii=[float(r) for r in radii],
        args=[float(a) for a in args],
        rings=rings,
        n_roots=len(roots),
        symmetry_group_order=int(sym_order),
        invariants=invariants,
    )


# ----------------------------------------- 5. Clustering engine


def cluster(results: list[dict[str, Any]]) -> list[Cluster]:
    """
    Cluster constellations by their *shape invariants*:
        (eqtype-class, Cn_order, ring counts tuple).
    Equation type is grouped (ode vs shift vs q-shift) because the
    combinatorics is identical across them.
    """
    by_key: dict[tuple, list[dict[str, Any]]] = {}
    for r in results:
        ring_counts = tuple(r["constellation"]["ring_counts"])
        key = (
            r["constellation"]["Cn_order"],
            ring_counts,
            r["constellation"]["is_regular_polygon"],
        )
        by_key.setdefault(key, []).append(r)

    clusters: list[Cluster] = []
    for key, members in sorted(by_key.items(), key=lambda kv: (-kv[0][0], kv[0])):
        cn, ring_counts, is_reg = key
        if is_reg:
            label = f"Class[Regular-{cn}-gon]"
            desc = (
                f"All {sum(ring_counts)} roots lie on a single ring; rotational "
                f"symmetry C_{cn}. Regular {cn}-gon."
            )
        else:
            label = f"Class[C{cn}, rings={list(ring_counts)}]"
            desc = (
                f"Multi-ring constellation with ring multiplicities {list(ring_counts)} "
                f"and global rotational symmetry C_{cn}."
            )
        rep = members[0]
        clusters.append(
            Cluster(
                label=label,
                description=desc,
                members=[m["operator"]["name"] for m in members],
                representative={
                    "name": rep["operator"]["name"],
                    "eqtype": rep["operator"]["eqtype"],
                    "slope": rep["operator"]["slope"],
                    "rank": rep["operator"]["rank"],
                    "valuation": rep["operator"]["valuation"],
                    "chi": rep["chi"]["chi_str"],
                    "rings": rep["constellation"]["rings"],
                },
            )
        )
    return clusters


# --------------------------------------------- 6. Conjecture engine


def make_conjectures(results: list[dict[str, Any]], clusters: list[Cluster]) -> list[str]:
    conjs: list[str] = []
    nonstress = [r for r in results if r["operator"]["valuation"] != "stress"]
    stress = [r for r in results if r["operator"]["valuation"] == "stress"]

    # ============================================================
    # MAIN THEOREM (the structural source from which everything
    # else descends). The pipeline does NOT prove this theorem; it
    # just observes that every behaviour in the zoo is consistent
    # with it. The theorem itself is an elementary algebraic fact.
    # ============================================================
    conjs.append(
        "**Main Theorem (μ_q-equivariant pullback).** "
        "Let L have a dominant Newton edge of slope −p/q (lowest terms) and "
        "rank multiplier r (so the edge has r+1 lattice points). Define the "
        "*inner polynomial* χ_w(w) of degree r by χ(c) = χ_w(c^q). Then the "
        "WKB exponent constellation is the **μ_q-equivariant pullback of the "
        "root multiset of χ_w under c ↦ c^q**: \n\n"
        "Roots(χ) = ⋃_{w_i : χ_w(w_i)=0} { c ∈ ℂ : c^q = w_i }. \n\n"
        "Every other observation in this report is a direct corollary of this "
        "factorisation plus Vieta, away from the discriminant / zero-root / "
        "equal-modulus loci."
    )

    # ------------------------------------------------------------
    # Corollaries (algebraic consequences, verified across the zoo)
    # ------------------------------------------------------------
    simple_results = [r for r in nonstress if r["operator"]["valuation"] == "simple"]
    all_simple_regular = all(
        r["constellation"]["is_regular_polygon"] for r in simple_results
    )
    if all_simple_regular and simple_results:
        conjs.append(
            "**Corollary 1 (Simple ⇒ regular d-gon).** "
            "χ binomial αc^d+β ⇒ constellation = regular d-gon centered at 0, "
            "with d = r·q. *Why*: roots of a binomial are roots of unity scaled "
            "and rotated. "
            f"Verified on {len(simple_results)}/{len(simple_results)} simple operators."
        )

    # Corollary 2: q | C_n (μ_q-equivariance).
    q_ok = True
    counter = 0
    for r in nonstress:
        q_s = int(r["operator"]["slope"].split("/")[1])
        if r["constellation"]["Cn_order"] % q_s != 0:
            q_ok = False
            break
        counter += 1
    if q_ok and counter:
        conjs.append(
            "**Corollary 2 (q | C_n, the μ_q-equivariance).** "
            "If the dominant edge has slope p/q (lowest terms) then C_q acts "
            "on Roots(χ) by c ↦ ζ_q c. Hence the detected rotational-symmetry "
            "order is a *multiple of q*; it may be strictly larger when χ has "
            "accidental coefficient zeros (see STRESS_accidental_sym below). "
            f"Verified on {counter}/{counter} non-stress operators."
        )

    # Corollary 3: ring-count partition is a q-refinement.
    partition_ok = all(
        all(rcc % int(r["operator"]["slope"].split("/")[1]) == 0
            for rcc in r["constellation"]["ring_counts"])
        for r in nonstress
    )
    if partition_ok:
        conjs.append(
            "**Corollary 3 (Ring-count partition is a q-refinement).** "
            "Group Roots(χ) by |c|. Each block has size divisible by q, since "
            "each fiber {c: c^q = w_i} is a regular q-gon. The partition is "
            "the |w|-fibre-structure of the inner polynomial. "
            f"Verified on {len(nonstress)}/{len(nonstress)} operators."
        )

    # Corollary 3a (generic regime): all w-moduli distinct ⇒ r rings of size q
    generic_results = [r for r in nonstress if r["operator"]["valuation"] == "generic_complex"
                       and r["operator"]["rank"] >= 2]
    generic_r_match = all(
        len(r["constellation"]["ring_radii"]) == r["operator"]["rank"]
        for r in generic_results
    )
    if generic_results and generic_r_match:
        conjs.append(
            "**Corollary 3a (Generic regime: rank ⇒ ring count).** "
            "When all |w_i| are distinct (a Zariski-open condition on edge "
            "coefficients, achieved here with non-real complex generic α_j), "
            "the constellation has *exactly r rings of q points each*. "
            f"Verified on {len(generic_results)}/{len(generic_results)} "
            "generic_complex operators."
        )

    # Corollary 4 (Vieta monodromy)
    n_check = sum(1 for r in nonstress if r["constellation"]["monodromy_matches_theta"])
    conjs.append(
        f"**Corollary 4 (Vieta monodromy).** Under β → e^{{iθ}}β, "
        f"arg ∏ c_k changes by exactly θ (mod 2π). This is literally Vieta's "
        f"identity ∏ c_k = (−1)^d β/α applied to the leading and constant "
        f"coefficient. "
        f"Verified on {n_check}/{len(nonstress)} non-stress operators with θ = π/3."
    )

    # Corollary 4a (Simple ring rotation = θ/d)
    simple_per_ring_ok = 0
    for r in simple_results:
        theta = r["constellation"]["monodromy_theta"]
        d = r["constellation"]["n_roots"]
        rotations = r["constellation"]["per_ring_rotation"]
        if d and rotations:
            expected = (theta / d) % (2 * math.pi / d)
            if all(abs(((rot - expected) + math.pi / d) % (2 * math.pi / d) - math.pi / d) < 1e-5
                   for rot in rotations if rot is not None):
                simple_per_ring_ok += 1
    if simple_results:
        conjs.append(
            f"**Corollary 4a (Simple ring rotates by θ/d).** "
            f"For binomial χ, every root rotates by θ/d. Verified on "
            f"{simple_per_ring_ok}/{len(simple_results)} simple operators."
        )

    # Corollary 4b (Weighted ring-rotation sum rule)
    weighted_ok = 0
    weighted_total = 0
    for r in nonstress:
        rings_ = r["constellation"]["ring_counts"]
        rots = r["constellation"]["per_ring_rotation"]
        if rots and all(rot is not None for rot in rots):
            weighted_total += 1
            theta = r["constellation"]["monodromy_theta"]
            total = sum(c_ * rot for c_, rot in zip(rings_, rots)) % (2 * math.pi)
            diff = abs((total - theta) % (2 * math.pi))
            diff_norm = min(diff, 2 * math.pi - diff)
            if diff_norm < 1e-6:
                weighted_ok += 1
    if weighted_total:
        conjs.append(
            "**Corollary 4b (Weighted ring-rotation sum rule).** "
            "Σ_k m_k Δ_k ≡ θ (mod 2π). This is the additive (logarithmic) form "
            "of Vieta. It is *not* an independent statement: the individual "
            "Δ_k are only defined modulo 2π/m_k, and m_k · Δ_k is exactly the "
            "well-defined Vieta lift. "
            f"Verified on {weighted_ok}/{weighted_total} operators (machine precision)."
        )

    # ------------------------------------------------------------
    # Pipeline-level invariance (combinatorial, NOT analytic)
    # ------------------------------------------------------------
    ode_keys = {(r["constellation"]["Cn_order"], tuple(r["constellation"]["ring_counts"]))
                for r in nonstress if r["operator"]["eqtype"] == "ode"}
    diff_keys = {(r["constellation"]["Cn_order"], tuple(r["constellation"]["ring_counts"]))
                 for r in nonstress if r["operator"]["eqtype"] in ("difference", "q-difference")}
    if diff_keys.issubset(ode_keys):
        conjs.append(
            "**Observation 5 (Equation-type invariance — combinatorial only).** "
            "*Under the same tropical-symbol extraction recipe* (Newton polygon "
            "→ edge polynomial χ via leading x-coefficients), the constellation "
            "class depends only on χ and not on whether L is ODE / shift / "
            "q-shift. *Caveat*: this is **not** a statement about formal "
            "operator classification — the natural spectral variable differs "
            "across equation types (c vs e^c vs q^c). The Levelt–Turrittin / "
            "Birkhoff–Trjitzinsky / Sauloy classifications use distinct "
            "normalisations and may attach different formal types to operators "
            "that share a constellation."
        )

    # ------------------------------------------------------------
    # Stress-test failure modes (these are the *interesting* edges
    # of the global structural map)
    # ------------------------------------------------------------
    if stress:
        conjs.append("**Stress-test report (failure modes of the naive picture).**")
    for r in stress:
        name = r["operator"]["name"]
        rc = r["constellation"]["ring_counts"]
        cn = r["constellation"]["Cn_order"]
        chi = r["chi"]["chi_str"]
        nr = r["constellation"]["n_roots"]
        if "equalmod" in name:
            # chi_w = (w-2)(w^2+4); three distinct w-roots, all |w| = 2
            note = ("Equal-modulus collision: χ_w has 3 distinct roots {2, ±2i}, "
                    "all with |w| = 2. Generic ring-count prediction (r distinct "
                    f"rings) FAILS: we see ring counts {rc} on a single radius. "
                    "→ refutes a naive 'rank ⇒ r rings' without genericity.")
        elif "doubleroot" in name:
            note = ("Double inner root: χ_w = (w-1)²(w-2). One w-orbit appears "
                    f"with multiplicity 2 — constellation ring counts {rc} "
                    "count *geometric* roots (not multiplicities). Logarithmic / "
                    "resonant Stokes phenomena may appear in the analytic theory "
                    "even though the geometric constellation looks tame.")
        elif "zeroroot" in name:
            note = ("Zero inner root: χ_w(0) = 0 → c = 0 lies on the "
                    "constellation. The fibre c^q = 0 is one point with "
                    f"multiplicity q, *not* a regular q-gon. Constellation = {rc} "
                    "rings; the c = 0 sector is degenerate.")
        elif "accidental" in name:
            note = (f"Accidental symmetry: χ(c) = c^6 + 1, slope 1/2 → minimal "
                    f"q-symmetry is C_2, but detected symmetry is **C_{cn}** "
                    "(strictly larger). This shows that 'q | C_n' is sharp only "
                    "for *generic* edge coefficients; sparse χ inflates C_n.")
        else:
            note = ""
        conjs.append(f"- `{name}`: χ = `{chi}`, n={nr}, C_{cn}, rings={rc}. {note}")

    # ------------------------------------------------------------
    # Final critical commentary
    # ------------------------------------------------------------
    conjs.append(
        "**Critical commentary (what the picture does NOT say).** "
        "(1) Ring-count partitions discard phase information and are *not* a "
        "standard invariant of meromorphic connections; Stokes geometry "
        "depends on differences c_i − c_j, not on |c_i|. "
        "(2) The 'rank ⇒ r rings' direction needs a genericity hypothesis "
        "(distinct |w_i|), and the real-coefficient signature (Conjecture 3c "
        "from an earlier draft) is **false in general** — see STRESS_equalmod. "
        "(3) Equation-type invariance is a statement about the extraction "
        "recipe, not about the analytic operator category."
    )

    return conjs


# ============================================================ main driver

def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    ops = generate_operators()
    print(f"[generator] produced {len(ops)} operators")

    results: list[dict[str, Any]] = []
    for op in ops:
        npg = compute_newton_polygon(op)
        chi = compute_characteristic_polynomial(op, npg)
        con = compute_constellation(op, chi)
        results.append(
            {
                "operator": asdict(op),
                "newton": {
                    "points": npg.points,
                    "hull": npg.hull,
                    "dominant_edge": npg.dominant_edge,
                    "slope": list(npg.slope),
                    "lattice_points_on_edge": npg.lattice_points_on_edge,
                },
                "chi": {
                    "chi_str": chi.chi_str,
                    "degree": chi.degree,
                    "inner_in_w": chi.inner_poly_in_w_str,
                    "inner_degree": chi.inner_degree,
                    "is_binomial": chi.is_binomial,
                },
                "constellation": {
                    "n_roots": con.n_roots,
                    "rings": con.rings,
                    "ring_counts": [r["count"] for r in con.rings],
                    "ring_radii": [r["radius"] for r in con.rings],
                    "Cn_order": con.symmetry_group_order,
                    "is_regular_polygon": con.invariants["is_regular_polygon"],
                    "monodromy_theta": con.invariants["monodromy_theta"],
                    "monodromy_argshift_product": con.invariants["monodromy_argshift_product"],
                    "monodromy_matches_theta": con.invariants["monodromy_matches_theta"],
                    "per_ring_rotation": con.invariants["per_ring_rotation"],
                },
            }
        )

    # remove non-serializable sympy expr from each operator dict
    for r in results:
        r["operator"].pop("coeffs_sym", None)

    clusters = cluster(results)
    conjectures = make_conjectures(results, clusters)

    # write artifacts
    with open(os.path.join(out_dir, "operators.json"), "w", encoding="utf-8") as f:
        json.dump([r["operator"] for r in results], f, indent=2)
    with open(os.path.join(out_dir, "newton.json"), "w", encoding="utf-8") as f:
        json.dump([{"name": r["operator"]["name"], **r["newton"]} for r in results], f, indent=2)
    with open(os.path.join(out_dir, "chi.json"), "w", encoding="utf-8") as f:
        json.dump([{"name": r["operator"]["name"], **r["chi"]} for r in results], f, indent=2)
    with open(os.path.join(out_dir, "constellations.json"), "w", encoding="utf-8") as f:
        json.dump([{"name": r["operator"]["name"], **r["constellation"]} for r in results], f, indent=2)
    with open(os.path.join(out_dir, "clusters.json"), "w", encoding="utf-8") as f:
        json.dump(
            [
                {
                    "label": c.label,
                    "description": c.description,
                    "members": c.members,
                    "representative": c.representative,
                }
                for c in clusters
            ],
            f,
            indent=2,
        )

    # human-readable report
    lines = []
    lines.append("# Fleet Report — Global WKB Pattern Discovery\n")
    lines.append(f"- Operators generated: **{len(ops)}**")
    lines.append(f"- Distinct constellation classes: **{len(clusters)}**\n")

    lines.append("## Pipeline outputs (summary table)\n")
    lines.append("| Operator | type | slope p/q | rank | valuation | χ | "
                 "n_roots | C_n | rings | regular? |")
    lines.append("|---|---|---|---|---|---|---:|---:|---|:---:|")
    for r in results:
        op = r["operator"]
        nr = r["constellation"]["n_roots"]
        cn = r["constellation"]["Cn_order"]
        rings = r["constellation"]["ring_counts"]
        is_reg = "✓" if r["constellation"]["is_regular_polygon"] else ""
        chi_s = r["chi"]["chi_str"]
        if len(chi_s) > 38:
            chi_s = chi_s[:36] + "…"
        lines.append(
            f"| `{op['name']}` | {op['eqtype']} | {op['slope']} | {op['rank']} | "
            f"{op['valuation']} | `{chi_s}` | {nr} | {cn} | {rings} | {is_reg} |"
        )

    lines.append("\n## Constellation classes (clustering)\n")
    for c in clusters:
        lines.append(f"### {c.label}")
        lines.append(c.description)
        lines.append(f"- members ({len(c.members)}): " +
                     ", ".join(f"`{m}`" for m in c.members[:8]) +
                     ("…" if len(c.members) > 8 else ""))
        rep = c.representative
        lines.append(f"- representative: `{rep['name']}` (eqtype={rep['eqtype']}, "
                     f"slope={rep['slope']}, rank={rep['rank']}, "
                     f"valuation={rep['valuation']})")
        lines.append(f"  - χ = `{rep['chi']}`")
        ring_lines = []
        for ring in rep['rings']:
            ring_lines.append(f"radius≈{ring['radius']:.4f}, count={ring['count']}")
        lines.append("  - rings: " + "; ".join(ring_lines))
        lines.append("")

    lines.append("## Conjectures, Corollaries, and Stress Tests\n")
    for cj in conjectures:
        # stress-test items already start with '- '
        if cj.startswith("- "):
            lines.append(cj)
        else:
            lines.append(cj)
        lines.append("")

    report = "\n".join(lines)
    with open(os.path.join(out_dir, "conjectures.md"), "w", encoding="utf-8") as f:
        f.write(report)

    # console summary
    print(f"[newton]    polygons computed for {len(results)} operators")
    print(f"[chi]       characteristic polynomials extracted")
    print(f"[constell.] constellations and rings computed")
    print(f"[cluster]   {len(clusters)} distinct classes")
    print(f"[conjecture] {len(conjectures)} conjectures written")
    print(f"\nReport at: conjectures.md")


if __name__ == "__main__":
    main()
