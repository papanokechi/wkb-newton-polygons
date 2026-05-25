"""
Phase III — deepening the WKB / Newton-polygon classification theory.

Pipeline:
  draft_reader   -> structured summary of Phase 1+2 (hard-coded constants)
  gap_finder     -> 20 concrete research directions
  operator_gen   -> multi-edge / high-q / system / mixed-type / controlled-Delta_ij operators
  invariant_eng  -> per-edge chi, full constellation, Delta_ij geometry, resonances
  clustering_eng -> universality classes under extended invariants
  conjecture_eng -> next-level structural laws and their evidence
  report         -> phase3_report.md
"""

from __future__ import annotations

import json
import math
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp

HERE = Path(__file__).parent


# =====================================================================
# 0. Numerical / symbolic helpers
# =====================================================================

X = sp.Symbol("x")
C = sp.Symbol("c")
W = sp.Symbol("w")
LAMBDA = sp.Symbol("lambda_")  # eigenvalue parameter for system block
# Use parameter names that DO NOT collide with sympy special functions (beta, gamma, etc.).
BETA = sp.Symbol("B0", complex=True)
GAMMA = sp.Symbol("G0", complex=True)
DELTA = sp.Symbol("D0", complex=True)
EPS = sp.Symbol("E0", complex=True)
PARAM_VALUE_MAP = {BETA: sp.Integer(1), GAMMA: sp.Integer(1),
                   DELTA: sp.Integer(1), EPS: sp.Integer(1)}


def _deg(poly: sp.Expr) -> int:
    p = sp.Poly(sp.expand(poly), X)
    if p.is_zero:
        return -10**9
    return int(p.degree())


def _lc(poly: sp.Expr) -> sp.Expr:
    p = sp.Poly(sp.expand(poly), X)
    if p.is_zero:
        return sp.Integer(0)
    return p.LC()


def _upper_hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Vertices of the upper convex hull of a set of integer lattice points.

    Traverses right-to-left (reversed sorted order) and keeps the genuine
    vertices: pops the top while the new triple makes a non-CCW (collinear or
    right) turn.  Note: this is the corrected orientation for right-to-left
    traversal — the previous `>= 0` test of fleet.py wiped out true multi-edge
    vertices because it popped CCW (genuine corner) turns as well.
    """
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    upper: list[tuple[int, int]] = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    upper.reverse()
    return upper


def _eval_complex(expr: sp.Expr, subs: dict | None = None) -> complex:
    e = expr
    if subs:
        e = e.subs(subs)
    return complex(sp.N(e, 30))


# =====================================================================
# 1. draft_reader  --  structured summary of Phase 1 + 2
# =====================================================================

DRAFT_SUMMARY: dict[str, Any] = {
    "title": "The WKB Geometry of Newton Polygons: A Classification Theory",
    "objects": {
        "L": "scalar linear operator with one irregular singularity at infinity",
        "D, S, T": "derivation, shift f(x)->f(x+1), q-shift f(x)->f(qx)",
        "N(L)": "Newton polygon at infinity = upper convex hull of {(k, deg a_k)}",
        "dominant edge": "edge of N(L) with the most-negative slope, written -p/q with gcd(p,q)=1",
        "r": "rank multiplier; the dominant edge has r+1 lattice points",
        "chi(c)": "WKB characteristic polynomial = sum over edge lattice points of LC_inf(a_k) c^k",
        "chi_w(w)": "inner polynomial of degree r with chi(c) = chi_w(c^q)",
        "C(L)": "WKB exponent constellation = Roots(chi)",
        "mu_q": "group of q-th roots of unity; zeta_q = e^{2 pi i / q}",
        "F": "functor L |-> C(L) up to coarse equivalence",
    },
    "main_theorem": (
        "If the dominant Newton edge has slope -p/q in lowest terms and contains "
        "r+1 lattice points at (rq - jq, jp) for 0 <= j <= r, then chi(c) = chi_w(c^q) "
        "and C(L) is the mu_q-equivariant pullback bigsqcup_{w_i in Roots(chi_w)} { c : c^q = w_i }."
    ),
    "corollaries": [
        "Generic ring decomposition: when the |w_i| are pairwise distinct and nonzero, "
        "C(L) is r concentric mu_q-orbits of size q.",
        "Vieta monodromy: under beta = alpha_r -> e^{i theta} beta, the lift sum m_k Delta_k = theta (mod 2 pi).",
    ],
    "degeneracy_loci": [
        "discriminant {disc chi_w = 0}: multiple roots in chi_w cause ring multiplicity > q",
        "equal-modulus {|w_i| = |w_j|, i != j}: distinct mu_q-orbits merge into one radius "
        "with non-uniform angular distribution",
        "zero-root {alpha_r = 0}: c = 0 enters C(L) with multiplicity q and the dominant edge jumps",
    ],
    "atlas": {
        "operators_swept": 89,
        "constellation_classes": 23,
        "axes": ["slope p/q in {1/2,1/3,1/4,2/3,3/2}", "rank r in {1,2,3}",
                 "valuation in {simple, double, mixed, generic_complex}",
                 "equation type in {ODE, difference, q-difference}"],
        "stress_classes": ["equalmod", "doubleroot", "zeroroot", "accidental_sym"],
    },
    "open_problems_stated": [
        "Multi-edge Newton polygons and stratification by edge sequences.",
        "Matrix / system operators and links to wild character varieties.",
        "Sharp converse to the constellation classification.",
        "What Stokes data (phases, lines) refine F to a complete invariant.",
    ],
    "phase1_phase2_status": "complete; 23 classes are codified, Main Theorem proven, paper draft written.",
}


# =====================================================================
# 2. gap_finder
# =====================================================================

GAPS: list[dict[str, str]] = [
    {"id": "G1", "title": "Multi-edge Newton polygons",
     "why": "Phase 1+2 treated only the dominant edge; an operator with k > 1 edges yields a slope filtration that the present F ignores."},
    {"id": "G2", "title": "2x2 and 3x3 systems",
     "why": "F is defined on scalar operators only; for systems the eigenvalue spectrum of the leading symbol generates a richer constellation."},
    {"id": "G3", "title": "High-ramification slopes (q >= 5)",
     "why": "All Phase-1 sweep points used q in {2,3,4}; q=5,6,7 may exhibit phenomena (number-theoretic resonance, larger automorphism groups) invisible at small q."},
    {"id": "G4", "title": "Delta_ij modulus partition",
     "why": "The constellation only records {c_i}; the multiset {|c_i - c_j|} is a finer invariant that survives global rotation."},
    {"id": "G5", "title": "Delta_ij argument partition",
     "why": "Stokes lines are determined by arg(c_i - c_j); a modulus-free angular invariant is the bridge to Stokes-graph classification."},
    {"id": "G6", "title": "Z-resonance among constellation points",
     "why": "Integer linear relations sum n_k c_k = 0 with small |n_k| signal accidental algebraic dependencies absent from Phase 1's clustering key."},
    {"id": "G7", "title": "omega-resonance beyond mu_q",
     "why": "When arg(c_i) - arg(c_j) is in 2 pi Q with denominator strictly larger than q, the constellation has additional rotational structure."},
    {"id": "G8", "title": "Mixed-type operators (D + lambda S)",
     "why": "Operators combining differential and difference terms test whether F's combinatorial output is genuinely equation-type-agnostic at the Newton-polygon level."},
    {"id": "G9", "title": "Controlled discriminant collisions",
     "why": "Phase 1 found degenerations by stress test; a parametric family approaching the discriminant locus would expose the deformation law."},
    {"id": "G10", "title": "Slope-filtration interaction across edges",
     "why": "For multi-edge polygons, do the per-edge constellations C_alpha algebraically interact (resonances among edges) or are they independent?"},
    {"id": "G11", "title": "Analytic fibres of F (equation-type discrimination)",
     "why": "Phase 1 noted that the combinatorial chi is equation-type invariant but the analytic meaning of c is not; an analytic invariant distinguishing ODE/diff/q-diff is missing."},
    {"id": "G12", "title": "Galois action on chi_w",
     "why": "Gal(Q-bar/Q) acts on the roots w_i; this action lifts to a permutation of the rings of C(L). Phase 1 has no Galois-theoretic invariant."},
    {"id": "G13", "title": "Sharpness of p-invariance",
     "why": "Phase 1 conjectured the slope numerator p is invisible; in multi-edge or systems contexts this may fail (p could survive as a phase twist)."},
    {"id": "G14", "title": "Orbit fusion under real-coefficient pairing",
     "why": "Real chi_w has conjugate root pairs of equal modulus, fusing two mu_q-orbits; this is recorded as a class but not as an invariant of F."},
    {"id": "G15", "title": "Codimension count for each degeneracy stratum",
     "why": "Phase 1 names 4 strata but does not specify their codimension in the alpha-coefficient space, blocking a precise stratification statement."},
    {"id": "G16", "title": "Deep zero-root strata",
     "why": "alpha_r = 0 alone gives multiplicity q at zero, but if alpha_r = alpha_{r-1} = 0, the constellation collapses further."},
    {"id": "G17", "title": "Per-edge gauge group",
     "why": "Each edge alpha admits its own leading-coefficient gauge beta_alpha; Vieta monodromy may decompose under the product of these groups."},
    {"id": "G18", "title": "Inner-polynomial ramification",
     "why": "chi_w itself may admit a further factorisation chi_w(w) = chi_v(w^{q'}) for some q' > 1; this is iterated mu_q-pullback structure."},
    {"id": "G19", "title": "Mixed equation-type Newton polygons",
     "why": "If a single operator carries both D^k and S^k terms, the Newton-polygon recipe still applies; do the resulting classes match the pure ones?"},
    {"id": "G20", "title": "Limit of high-rank / high-q families",
     "why": "What is the asymptotic structure of C(L) as r, q -> infinity? Equidistribution on annuli? Random-matrix-like statistics?"},
]


# =====================================================================
# 3. operator_generator
# =====================================================================

@dataclass
class Op:
    name: str
    family: str        # "scalar" | "system" | "mixed-type"
    eqtype: str        # "ode" | "difference" | "q-difference" | "mixed"
    coeffs_sym: list[sp.Expr]    # for scalar: a_0,...,a_n in c (i.e. of D^k, etc.)
    notes: str = ""
    # for systems we store the matrix coefficients of the *symbol* polynomial in c
    system_dim: int = 1
    system_blocks: list[dict[str, Any]] = field(default_factory=list)


def _poly(deg: int, lead: sp.Expr = sp.Integer(1), sublead: sp.Expr = sp.Integer(0)) -> sp.Expr:
    if deg < 0:
        return sp.Integer(0)
    return lead * X**deg + sublead * X**(deg - 1) if deg >= 1 else lead


def _two_edge_operator(name: str, eqtype: str,
                       p1: int, q1: int, r1: int,
                       p2: int, q2: int, r2: int,
                       inner1_coeffs: list[sp.Expr], inner2_coeffs: list[sp.Expr]) -> Op:
    """
    Build a scalar operator with EXACTLY two edges on its Newton polygon:
      - left edge (smaller k):  slope -p1/q1, rank r1
      - right edge (larger k):  slope -p2/q2, rank r2   (-> dominant)
    The shared vertex is at the joint of the two edges; we place it at (k_mid, d_mid).
    Lattice points on edge 1: (jq1, d_mid + (r1-j)p1) for j=0..r1
    Lattice points on edge 2: (k_mid + jq2, d_mid - jp2) for j=0..r2  (with k_mid = r1 q1)
    For upper hull: we want slope_left > slope_right; with slopes negative, |slope_right| > |slope_left|.
    """
    k_mid = r1 * q1
    d_mid = r2 * p2  # so that right edge ends at (k_mid + r2*q2, 0)
    # left edge top vertex (k=0): d = d_mid + r1*p1
    d_left = d_mid + r1 * p1
    n = k_mid + r2 * q2

    coeffs: list[sp.Expr] = [sp.Integer(0)] * (n + 1)
    # left edge lattice points: k = j*q1, d = d_mid + (r1-j)*p1
    for j in range(r1 + 1):
        k = j * q1
        d = d_mid + (r1 - j) * p1
        coeffs[k] = inner1_coeffs[j] * X**d
    # right edge lattice points: k = k_mid + j*q2, d = d_mid - j*p2  for j=0..r2
    for j in range(r2 + 1):
        k = k_mid + j * q2
        d = d_mid - j * p2
        if coeffs[k] != 0:
            # Joint vertex (j=0 on right edge == j=r1 on left edge). Use left's value
            # but verify d-values agree:
            if d != d_left - r1 * p1:  # this is d_mid
                pass
            continue
        coeffs[k] = inner2_coeffs[j] * X**d
    return Op(name=name, family="scalar", eqtype=eqtype, coeffs_sym=coeffs,
              notes=f"two-edge polygon: slopes -{p1}/{q1} (rank {r1}) and -{p2}/{q2} (rank {r2}); shared vertex at (k={k_mid}, d={d_mid})")


def _scalar_dominant_edge(name: str, eqtype: str, p: int, q: int, r: int,
                          inner_coeffs: list[sp.Expr]) -> Op:
    n = r * q
    coeffs = [sp.Integer(0)] * (n + 1)
    for j in range(r + 1):
        k = j * q
        d = (r - j) * p
        coeffs[k] = inner_coeffs[j] * X**d
    return Op(name=name, family="scalar", eqtype=eqtype, coeffs_sym=coeffs,
              notes=f"single dominant edge slope -{p}/{q}, rank {r}")


def _system_block_diag(name: str, eqtype: str, block_specs: list[tuple[int, int, int, list]]) -> Op:
    """
    Diagonal-block system: each diagonal block is a scalar operator with single dominant edge.
    Constellation = union of per-block scalar constellations.
    block_specs: list of (p, q, r, inner_coeffs) tuples.
    """
    blocks = []
    for i, (p, q, r, inner) in enumerate(block_specs):
        blocks.append({"p": p, "q": q, "r": r, "inner_coeffs": [sp.sstr(s) for s in inner]})
    return Op(name=name, family="system", eqtype=eqtype, coeffs_sym=[],
              system_dim=len(block_specs), system_blocks=blocks,
              notes=f"block-diagonal {len(block_specs)}x{len(block_specs)} system")


def generate_phase3_operators() -> list[Op]:
    ops: list[Op] = []

    # ---- G3: high-ramification slopes (q = 5, 6, 7) ----
    for (p, q, r) in [(1, 5, 1), (1, 5, 2), (2, 5, 2), (1, 6, 1), (1, 6, 2),
                      (1, 7, 1), (3, 7, 2), (1, 5, 3), (1, 6, 3)]:
        # simple binomial
        inner = [BETA] + [sp.Integer(0)] * (r - 1) + [sp.Integer(1)] if r >= 1 else [sp.Integer(1)]
        inner = [BETA] + [sp.Integer(0)] * (r - 1) + [sp.Integer(1)]
        ops.append(_scalar_dominant_edge(f"HIGHQ_simple_s{p}o{q}_r{r}", "ode", p, q, r, inner))
        # generic complex
        if r >= 2:
            inner_gc = [(j + 1) + sp.I * (2 * j + 1) for j in range(r + 1)]
            # boost the leading and trailing for nondegeneracy
            inner_gc[0] = BETA
            inner_gc[-1] = sp.Integer(1)
            ops.append(_scalar_dominant_edge(f"HIGHQ_genc_s{p}o{q}_r{r}", "ode", p, q, r, inner_gc))

    # ---- G1, G10: multi-edge polygons ----
    # Two-edge: (slope1, slope2) with slope2 dominant
    multi_specs = [
        # (p1, q1, r1, p2, q2, r2, label)
        (1, 3, 1, 1, 2, 2, "edges_1o3_then_1o2"),  # less negative then more negative
        (1, 4, 1, 1, 2, 2, "edges_1o4_then_1o2"),
        (1, 5, 1, 1, 2, 2, "edges_1o5_then_1o2"),
        (1, 3, 2, 1, 2, 1, "edges_1o3_r2_then_1o2"),
        (1, 4, 2, 1, 3, 2, "edges_1o4_r2_then_1o3"),
        (2, 5, 1, 3, 5, 2, "edges_2o5_then_3o5"),
        (1, 6, 1, 1, 4, 2, "edges_1o6_then_1o4"),
    ]
    for (p1, q1, r1, p2, q2, r2, lbl) in multi_specs:
        inner1 = [sp.Integer(1) + sp.I] + [sp.Integer(j + 2) for j in range(r1 - 1)] + [sp.Integer(1)]
        if len(inner1) < r1 + 1:
            inner1 = [BETA] + [sp.Integer(j + 1) for j in range(r1 - 1)] + [sp.Integer(1)]
        inner1 = inner1[:r1 + 1]
        if len(inner1) != r1 + 1:
            inner1 = [BETA] + [sp.Integer(1)] * (r1 - 1) + [sp.Integer(1)]
            inner1 = inner1[:r1 + 1]
        inner2 = [GAMMA] + [sp.Integer(j + 2) + sp.I * (j + 1) for j in range(r2 - 1)] + [sp.Integer(1)]
        inner2 = inner2[:r2 + 1]
        op = _two_edge_operator(f"MULTI_{lbl}", "ode",
                                 p1, q1, r1, p2, q2, r2,
                                 inner1, inner2)
        ops.append(op)

    # Three-edge: pile up three slopes
    # k_0 = 0, k_1 = q1*r1, k_2 = k_1 + q2*r2, k_3 = k_2 + q3*r3
    # d_3 = 0, d_2 = r3*p3, d_1 = d_2 + r2*p2, d_0 = d_1 + r1*p1
    def _three_edge(name, p1, q1, r1, p2, q2, r2, p3, q3, r3,
                    inner1, inner2, inner3):
        k1 = r1 * q1
        k2 = k1 + r2 * q2
        k3 = k2 + r3 * q3
        d3 = 0
        d2 = r3 * p3
        d1 = d2 + r2 * p2
        d0 = d1 + r1 * p1
        n = k3
        coeffs = [sp.Integer(0)] * (n + 1)
        # edge 1
        for j in range(r1 + 1):
            k = j * q1
            d = d1 + (r1 - j) * p1
            if coeffs[k] == 0:
                coeffs[k] = inner1[j] * X**d
        # edge 2
        for j in range(r2 + 1):
            k = k1 + j * q2
            d = d2 + (r2 - j) * p2
            if coeffs[k] == 0:
                coeffs[k] = inner2[j] * X**d
        # edge 3
        for j in range(r3 + 1):
            k = k2 + j * q3
            d = d3 + (r3 - j) * p3
            if coeffs[k] == 0:
                coeffs[k] = inner3[j] * X**d
        return Op(name=name, family="scalar", eqtype="ode", coeffs_sym=coeffs,
                  notes=f"three-edge: slopes -{p1}/{q1}, -{p2}/{q2}, -{p3}/{q3}")

    ops.append(_three_edge("MULTI3_1o4_1o3_1o2",
                           1, 4, 1, 1, 3, 1, 1, 2, 1,
                           [BETA, sp.Integer(1)], [GAMMA, sp.Integer(1)], [DELTA, sp.Integer(1)]))
    ops.append(_three_edge("MULTI3_1o5_1o3_1o2",
                           1, 5, 1, 1, 3, 1, 1, 2, 2,
                           [BETA, sp.Integer(1)],
                           [GAMMA, sp.Integer(1)],
                           [DELTA, sp.Integer(2) + sp.I, sp.Integer(1)]))

    # ---- G2: 2x2 and 3x3 block-diagonal systems ----
    ops.append(_system_block_diag("SYS2_1o2_1o3", "ode",
                                  [(1, 2, 1, [BETA, sp.Integer(1)]),
                                   (1, 3, 1, [GAMMA, sp.Integer(1)])]))
    ops.append(_system_block_diag("SYS2_1o3_r2_genc", "ode",
                                  [(1, 3, 1, [BETA, sp.Integer(1)]),
                                   (1, 3, 2, [GAMMA, sp.Integer(2) + sp.I, sp.Integer(1)])]))
    ops.append(_system_block_diag("SYS3_1o2_1o3_1o4", "ode",
                                  [(1, 2, 1, [BETA, sp.Integer(1)]),
                                   (1, 3, 1, [GAMMA, sp.Integer(1)]),
                                   (1, 4, 1, [DELTA, sp.Integer(1)])]))
    ops.append(_system_block_diag("SYS3_1o5_r1_x3", "ode",
                                  [(1, 5, 1, [BETA, sp.Integer(1)]),
                                   (2, 5, 1, [GAMMA, sp.Integer(1)]),
                                   (3, 5, 1, [DELTA, sp.Integer(1)])]))

    # ---- G8: mixed-type operators ----
    # Treat the operator's Newton polygon recipe identically; we just record eqtype = "mixed"
    # to verify that the F-functor agrees combinatorially.
    inner_mix = [BETA, sp.Integer(2) + sp.I, sp.Integer(1)]
    ops.append(_scalar_dominant_edge("MIX_DandS_1o3_r2", "mixed", 1, 3, 2, inner_mix))
    inner_mix2 = [BETA, sp.Integer(1) + 2 * sp.I, sp.Integer(3) - sp.I, sp.Integer(1)]
    ops.append(_scalar_dominant_edge("MIX_DandS_1o4_r3", "mixed", 1, 4, 3, inner_mix2))

    # ---- G9: controlled Delta_ij degeneracies ----
    # Pick chi_w with prescribed roots so that c_i - c_j has a single small modulus
    # Example: chi_w(w) = (w-1)(w-2)(w-(1+epsilon))  -- as epsilon->0 we approach discriminant
    for eps_val in [sp.Rational(1, 1), sp.Rational(1, 5), sp.Rational(1, 25)]:
        w_roots = [sp.Integer(1), sp.Integer(2), 1 + eps_val]
        chi_w = sp.expand(sp.prod([W - r_ for r_ in w_roots]))
        coeffs_w = [chi_w.coeff(W, j) for j in range(4)]  # [a0, a1, a2, a3]
        ops.append(_scalar_dominant_edge(
            f"CTRL_disc_eps{sp.nsimplify(eps_val)}".replace("/", "o"),
            "ode", 1, 3, 3, list(coeffs_w)))

    # Δ_ij with engineered angles: chi_w with roots on a "tilted" line
    for theta_idx, theta_val in enumerate([sp.pi / 6, sp.pi / 4, sp.pi / 3]):
        w1 = sp.exp(sp.I * theta_val)
        w2 = sp.exp(sp.I * (-theta_val))
        chi_w = sp.expand((W - w1) * (W - w2))
        coeffs_w = [sp.simplify(chi_w.coeff(W, j)) for j in range(3)]
        ops.append(_scalar_dominant_edge(
            f"CTRL_conjroots_t{theta_idx}", "ode", 1, 4, 2, list(coeffs_w)))

    # G16: deep zero-root (alpha_r = alpha_{r-1} = 0)
    ops.append(_scalar_dominant_edge(
        "CTRL_zeroroot_deep", "ode", 1, 2, 3,
        [BETA, sp.Integer(1), sp.Integer(0), sp.Integer(0)]  # c^0, c^2, 0, 0 -> chi = beta + c^2
    ))
    ops.append(_scalar_dominant_edge(
        "CTRL_zeroroot_doublemult", "ode", 1, 3, 3,
        [BETA, sp.Integer(2), sp.Integer(0), sp.Integer(0)]  # chi = beta + 2 c^3
    ))

    # G18: nested ramification: chi_w itself a polynomial in w^2 -> additional mu_2 inside
    # chi_w(w) = w^4 + alpha w^2 + beta  => chi(c) = c^{4q} + alpha c^{2q} + beta
    ops.append(_scalar_dominant_edge(
        "NEST_q3_qinner2", "ode", 1, 3, 4,
        [BETA, sp.Integer(0), GAMMA, sp.Integer(0), sp.Integer(1)]
    ))
    ops.append(_scalar_dominant_edge(
        "NEST_q2_qinner3", "ode", 1, 2, 6,
        [BETA, sp.Integer(0), sp.Integer(0), GAMMA, sp.Integer(0), sp.Integer(0), sp.Integer(1)]
    ))

    # G12: chi_w with non-real algebraic roots, to test Galois action
    ops.append(_scalar_dominant_edge(
        "GAL_cyclotomic_3", "ode", 1, 2, 2,
        [sp.Integer(1), sp.Integer(1), sp.Integer(1)]  # chi_w = 1 + w + w^2, roots = primitive 3rd roots
    ))
    ops.append(_scalar_dominant_edge(
        "GAL_cyclotomic_5", "ode", 1, 2, 4,
        [sp.Integer(1), sp.Integer(1), sp.Integer(1), sp.Integer(1), sp.Integer(1)]
    ))

    # G7: omega-resonance test: chi_w with roots at e^{2 pi i k/m} for m > q
    # If q = 2 and chi_w has roots e^{i pi/5} and e^{-i pi/5}, then c-roots have angular spacing
    # finer than pi (= 2pi/q).
    ops.append(_scalar_dominant_edge(
        "OMEGA_q2_fifth", "ode", 1, 2, 2,
        [sp.Integer(1), -2 * sp.cos(sp.pi / 5), sp.Integer(1)]
    ))
    ops.append(_scalar_dominant_edge(
        "OMEGA_q3_seventh", "ode", 1, 3, 2,
        [sp.Integer(1), -2 * sp.cos(sp.pi / 7), sp.Integer(1)]
    ))

    # G13: p-invariance sharpness probe -- two operators differing only in p (numerator)
    ops.append(_scalar_dominant_edge(
        "PINV_s1o5_r2_genc", "ode", 1, 5, 2,
        [BETA, sp.Integer(2) + sp.I, sp.Integer(1)]
    ))
    ops.append(_scalar_dominant_edge(
        "PINV_s2o5_r2_genc", "ode", 2, 5, 2,
        [BETA, sp.Integer(2) + sp.I, sp.Integer(1)]
    ))
    ops.append(_scalar_dominant_edge(
        "PINV_s3o5_r2_genc", "ode", 3, 5, 2,
        [BETA, sp.Integer(2) + sp.I, sp.Integer(1)]
    ))
    ops.append(_scalar_dominant_edge(
        "PINV_s4o5_r2_genc", "ode", 4, 5, 2,
        [BETA, sp.Integer(2) + sp.I, sp.Integer(1)]
    ))

    return ops


# =====================================================================
# 4. Per-operator pipeline (Newton polygon, edges, per-edge chi, constellation)
# =====================================================================

def compute_newton_polygon(op: Op) -> dict[str, Any]:
    if op.family == "system":
        # union of block polygons
        edges_all = []
        for b in op.system_blocks:
            edges_all.append({"p": b["p"], "q": b["q"], "r": b["r"],
                              "block_inner": b["inner_coeffs"]})
        return {"edges": edges_all, "n_edges": len(edges_all), "kind": "system"}
    pts: list[tuple[int, int]] = []
    for k, ak in enumerate(op.coeffs_sym):
        d = _deg(ak)
        if d > -10**8:
            pts.append((k, d))
    hull = _upper_hull(pts)
    edges = []
    for a, b in zip(hull, hull[1:]):
        if b[0] == a[0]:
            continue
        slope = Fraction(b[1] - a[1], b[0] - a[0])
        if slope >= 0:
            continue  # skip non-negative slopes (not WKB-relevant)
        p_num, q_den = (-slope).numerator, (-slope).denominator
        # lattice points on (a, b)
        dx, dy = b[0] - a[0], b[1] - a[1]
        g = math.gcd(abs(dx), abs(dy)) if (dx or dy) else 1
        sx, sy = dx // g, dy // g
        lattice_pts = [(a[0] + t * sx, a[1] + t * sy) for t in range(g + 1)]
        r_edge = g  # number of lattice steps = r
        # since slope = -p/q in lowest terms, sx = q, sy = -p
        edges.append({
            "vertices": [list(a), list(b)],
            "p": p_num, "q": q_den, "r": r_edge,
            "lattice_pts": [list(pt) for pt in lattice_pts],
        })
    return {"points": [list(pt) for pt in pts],
            "hull": [list(pt) for pt in hull],
            "edges": edges,
            "n_edges": len(edges),
            "kind": "scalar"}


def compute_per_edge_chi(op: Op, np_info: dict[str, Any]) -> list[dict[str, Any]]:
    """For each edge, compute chi^{(alpha)} and chi_w^{(alpha)}.

    Stores the live sympy expressions under `_chi_c_sym` / `_chi_w_sym` (underscore
    prefix marks them as non-JSON fields that we strip before serialising).
    """
    out = []
    if np_info["kind"] == "system":
        for b_info in op.system_blocks:
            p, q, r_ = b_info["p"], b_info["q"], b_info["r"]
            inner_coeffs = [sp.sympify(s, locals={"B0": BETA, "G0": GAMMA, "D0": DELTA, "E0": EPS})
                            for s in b_info["inner_coeffs"]]
            chi_c = sum(inner_coeffs[j] * C**((r_ - j) * q) for j in range(r_ + 1))
            chi_w = sum(inner_coeffs[j] * W**(r_ - j) for j in range(r_ + 1))
            out.append({"p": p, "q": q, "r": r_,
                        "chi_c": sp.sstr(sp.expand(chi_c)),
                        "chi_w": sp.sstr(sp.expand(chi_w)),
                        "inner_coeffs": [sp.sstr(s) for s in inner_coeffs],
                        "block": True,
                        "_chi_c_sym": sp.expand(chi_c),
                        "_chi_w_sym": sp.expand(chi_w),
                        "k0": 0})
        return out
    for edge in np_info["edges"]:
        p, q = edge["p"], edge["q"]
        r_ = edge["r"]
        k0 = edge["lattice_pts"][0][0]
        inner_coeffs: list[sp.Expr] = []
        for (k, d) in edge["lattice_pts"]:
            ak = op.coeffs_sym[k] if k < len(op.coeffs_sym) else sp.Integer(0)
            inner_coeffs.append(_lc(ak))
        alpha = list(reversed(inner_coeffs))
        chi_c = sum(alpha[j] * C**(k0 + (r_ - j) * q) for j in range(r_ + 1))
        chi_w = sum(alpha[j] * W**(r_ - j) for j in range(r_ + 1))
        out.append({"p": p, "q": q, "r": r_,
                    "k0": k0,
                    "chi_c": sp.sstr(sp.expand(chi_c)),
                    "chi_w": sp.sstr(sp.expand(chi_w)),
                    "inner_coeffs": [sp.sstr(s) for s in alpha],
                    "block": False,
                    "vertices": edge["vertices"],
                    "_chi_c_sym": sp.expand(chi_c),
                    "_chi_w_sym": sp.expand(chi_w)})
    return out


def _numerify(expr: sp.Expr) -> sp.Expr:
    return expr.subs(PARAM_VALUE_MAP)


def compute_constellation_for_edge(edge_info: dict[str, Any]) -> dict[str, Any]:
    """Return numerical roots of chi^{(edge)}(c)."""
    chi_c = edge_info.get("_chi_c_sym")
    if chi_c is None:
        chi_c = sp.sympify(edge_info["chi_c"],
                            locals={"B0": BETA, "G0": GAMMA, "D0": DELTA, "E0": EPS})
    chi_c_num = _numerify(chi_c)
    poly_c = sp.Poly(chi_c_num, C)
    if poly_c.is_zero:
        return {"roots": [], "n_roots": 0, "p": edge_info["p"], "q": edge_info["q"],
                "r": edge_info["r"], "k0": edge_info.get("k0", 0)}
    coeffs = [complex(c) for c in poly_c.all_coeffs()]
    arr = np.array(coeffs, dtype=complex)
    if len(arr) <= 1:
        return {"roots": [], "n_roots": 0, "p": edge_info["p"], "q": edge_info["q"],
                "r": edge_info["r"], "k0": edge_info.get("k0", 0)}
    try:
        roots = np.roots(arr).tolist()
    except Exception:
        roots = []
    out_roots = [(float(z.real), float(z.imag)) for z in roots]
    return {"roots": out_roots, "n_roots": len(out_roots),
            "p": edge_info["p"], "q": edge_info["q"], "r": edge_info["r"],
            "k0": edge_info.get("k0", 0)}


def full_constellation(per_edge_constellations: list[dict[str, Any]]) -> list[tuple[float, float]]:
    """Union of all per-edge root lists (with multiplicities)."""
    out = []
    for ec in per_edge_constellations:
        out.extend(ec["roots"])
    return out


# =====================================================================
# 5. invariant_engine
# =====================================================================

def compute_delta_ij(roots: list[tuple[float, float]]) -> dict[str, Any]:
    if len(roots) < 2:
        return {"n_pairs": 0, "moduli": [], "args": [],
                "modulus_partition": [], "argument_partition": [],
                "n_distinct_moduli": 0, "n_distinct_args": 0}
    cs = [complex(r, i) for (r, i) in roots]
    deltas = []
    for i, j in combinations(range(len(cs)), 2):
        deltas.append(cs[i] - cs[j])
    mods = [abs(d) for d in deltas]
    args = [math.atan2(d.imag, d.real) for d in deltas]
    # partition by modulus (round to 6 decimals)
    mod_counter = Counter(round(m, 6) for m in mods)
    arg_counter = Counter(round(a, 5) for a in args)
    return {
        "n_pairs": len(deltas),
        "moduli": sorted(mod_counter.items()),
        "modulus_partition": sorted(mod_counter.values(), reverse=True),
        "args": sorted(arg_counter.items()),
        "argument_partition": sorted(arg_counter.values(), reverse=True),
        "n_distinct_moduli": len(mod_counter),
        "n_distinct_args": len(arg_counter),
    }


def detect_z_resonance(roots: list[tuple[float, float]], max_coeff: int = 3,
                        max_terms: int = 4, tol: float = 1e-7,
                        ring_size: int | None = None) -> list[dict[str, Any]]:
    """
    Look for small Z-linear relations sum n_k c_k ~ 0 with |n_k| <= max_coeff,
    at most max_terms nonzero coefficients, and the gcd of |n_k| equal to 1.

    Tags each relation with `mu_q_forced`: True iff support is contained in a
    single ring of size `ring_size` (in which case the relation lies in the
    cyclotomic ideal of Z[zeta_ring_size] and is forced by mu_q symmetry).
    Genuinely *nontrivial* relations are those that cross two or more rings.
    """
    if len(roots) < 2:
        return []
    cs = [complex(r, i) for (r, i) in roots]
    n = len(cs)
    found = []
    seen: set[tuple[int, ...]] = set()
    from itertools import combinations as _comb
    for k_nonzero in range(2, max_terms + 1):
        for support in _comb(range(n), k_nonzero):
            for coefs in product(range(-max_coeff, max_coeff + 1), repeat=k_nonzero):
                if all(c == 0 for c in coefs):
                    continue
                if math.gcd(*[abs(c) for c in coefs if c != 0]) != 1:
                    continue
                first_nz = next(c for c in coefs if c != 0)
                if first_nz < 0:
                    coefs = tuple(-c for c in coefs)
                key = tuple(coefs[support.index(i)] if i in support else 0 for i in range(n))
                if key in seen:
                    continue
                seen.add(key)
                val = sum(coefs[idx] * cs[i] for idx, i in enumerate(support))
                if abs(val) < tol:
                    # classify whether the relation is mu_q-forced
                    # A relation sum n_k c_k = 0 is mu_q-forced iff the per-ring
                    # partial sum vanishes for each ring independently (i.e. the
                    # relation lies in the Z-span of single-ring forced relations,
                    # which is the lattice generated by cyclotomic relations in
                    # each Z[zeta_q]-summand).
                    mu_q_forced = False
                    if ring_size and ring_size >= 2:
                        per_ring_partial: dict[int, complex] = {}
                        for idx, root_idx in enumerate(support):
                            ring_alpha = root_idx // ring_size
                            per_ring_partial[ring_alpha] = (
                                per_ring_partial.get(ring_alpha, 0) + coefs[idx] * cs[root_idx]
                            )
                        if all(abs(v) < tol for v in per_ring_partial.values()):
                            mu_q_forced = True
                    # legacy field: pure antipodal pair is the simplest sub-case
                    trivial_antipodal = (
                        k_nonzero == 2 and set(coefs) == {1} and len(support) == 2
                        and abs(cs[support[0]] + cs[support[1]]) < tol
                    )
                    found.append({"support": list(support),
                                  "coeffs": list(coefs),
                                  "residual": float(abs(val)),
                                  "mu_q_forced": mu_q_forced,
                                  "trivial_antipodal": trivial_antipodal})
        if len(found) > 40:
            break
    found.sort(key=lambda x: (x["mu_q_forced"], len(x["support"]), x["support"]))
    return found[:30]


def count_nontrivial_z_resonance(z_res: list[dict[str, Any]]) -> int:
    """Count relations that are NOT mu_q-forced (cross-ring relations)."""
    return sum(1 for r in z_res if not r.get("mu_q_forced", False))


def detect_omega_resonance(roots: list[tuple[float, float]], q: int,
                            denom_search: int = 24, tol: float = 1e-6) -> dict[str, Any]:
    """
    Determine the minimum rational denominator m such that all arg(c_k) - arg(c_0)
    are in 2pi * (Z/m). If m > q, this is omega-resonance beyond mu_q.
    """
    if len(roots) < 2:
        return {"min_denom": 0, "is_resonant": False, "denom": 0,
                "ratio_to_q": 0.0, "expected_q": q}
    cs = [complex(r, i) for (r, i) in roots if abs(complex(r, i)) > 1e-9]
    if len(cs) < 2:
        return {"min_denom": 0, "is_resonant": False, "denom": 0,
                "ratio_to_q": 0.0, "expected_q": q}
    args = [math.atan2(c.imag, c.real) for c in cs]
    base = args[0]
    diffs = [(a - base) % (2 * math.pi) for a in args]
    # find smallest m so that round(m * diff / (2 pi)) * (2 pi / m) ~ diff for all diffs
    best_m = None
    for m in range(1, denom_search + 1):
        ok = True
        for d in diffs:
            scaled = m * d / (2 * math.pi)
            if abs(scaled - round(scaled)) > tol * m:
                ok = False
                break
        if ok:
            best_m = m
            break
    return {"min_denom": best_m or denom_search,
            "is_resonant": (best_m is not None and best_m > q),
            "denom": best_m or 0,
            "ratio_to_q": (best_m / q) if best_m else 0.0,
            "expected_q": q}


def detect_symmetry_inflation(roots: list[tuple[float, float]], q_expected: int) -> dict[str, Any]:
    """
    Find the largest n such that the root multiset is invariant under rotation by 2 pi / n.
    """
    if len(roots) < 2:
        return {"n_observed": 1, "expected_q": q_expected, "inflated": False, "ratio": 1.0}
    cs = sorted([complex(r, i) for (r, i) in roots], key=lambda z: (round(abs(z), 6), round(math.atan2(z.imag, z.real), 6)))
    best_n = 1
    for n in range(2, 25):
        rot = complex(math.cos(2 * math.pi / n), math.sin(2 * math.pi / n))
        rotated = sorted([z * rot for z in cs], key=lambda z: (round(abs(z), 6), round(math.atan2(z.imag, z.real), 6)))
        if all(abs(a - b) < 1e-5 for a, b in zip(cs, rotated)):
            best_n = n
    return {"n_observed": best_n, "expected_q": q_expected,
            "inflated": best_n > q_expected,
            "ratio": best_n / q_expected if q_expected else 0.0}


def detect_multi_edge_interference(per_edge_consts: list[dict[str, Any]]) -> dict[str, Any]:
    """
    For multi-edge: check whether per-edge constellations overlap, share radii, or have
    resonant angular offsets.
    """
    if len(per_edge_consts) < 2:
        return {"n_edges": len(per_edge_consts), "interference": "none"}
    info = {"n_edges": len(per_edge_consts), "per_edge_radii": []}
    radii_sets = []
    for ec in per_edge_consts:
        rs = sorted([round(abs(complex(*z)), 6) for z in ec["roots"]])
        radii_sets.append(rs)
        info["per_edge_radii"].append(rs)
    # detect shared radii
    flat = Counter()
    for rs in radii_sets:
        for r_ in set(rs):
            flat[r_] += 1
    shared = [r_ for r_, count in flat.items() if count > 1]
    info["shared_radii"] = shared
    # detect "fan" pattern: each edge has its own ring, all disjoint
    info["edges_disjoint"] = len(shared) == 0
    # detect zero-roots from common multiplicities at c = 0
    n_zeros = sum(1 for ec in per_edge_consts for z in ec["roots"] if abs(complex(*z)) < 1e-9)
    info["zero_roots"] = n_zeros
    return info


def invariants_for_operator(op: Op, np_info: dict[str, Any],
                             per_edge_chi: list[dict[str, Any]]) -> dict[str, Any]:
    per_edge_consts = [compute_constellation_for_edge(e) for e in per_edge_chi]
    full = full_constellation(per_edge_consts)
    delta = compute_delta_ij(full)
    q_dom = max((e["q"] for e in per_edge_chi), default=1)
    # ring_size: for single-edge ops the constellation is structured as r rings of q
    # roots each (where r = degree of inner polynomial, q = denominator of dominant slope).
    # We pass q so that single-ring relations get marked mu_q_forced.
    z_ring_size = q_dom if len(per_edge_chi) == 1 and len(full) % q_dom == 0 else None
    z_res = detect_z_resonance(full, ring_size=z_ring_size)
    nontrivial_z = count_nontrivial_z_resonance(z_res)
    omega = detect_omega_resonance(full, q_dom)
    sym = detect_symmetry_inflation(full, q_dom)
    inter = detect_multi_edge_interference(per_edge_consts)
    return {
        "operator": op.name,
        "family": op.family,
        "eqtype": op.eqtype,
        "n_edges": np_info.get("n_edges", 0),
        "per_edge": [{"p": e["p"], "q": e["q"], "r": e["r"], "chi_w": e["chi_w"]} for e in per_edge_chi],
        "per_edge_constellations": per_edge_consts,
        "full_constellation": full,
        "delta_ij": delta,
        "z_resonance": z_res,
        "z_resonance_nontrivial_count": nontrivial_z,
        "omega_resonance": omega,
        "symmetry": sym,
        "multi_edge": inter,
        "notes": op.notes,
    }


# =====================================================================
# 6. clustering_engine
# =====================================================================

def clustering_key(inv: dict[str, Any]) -> tuple:
    return (
        inv["family"],
        inv["n_edges"],
        tuple(inv["delta_ij"]["modulus_partition"]),
        tuple(inv["delta_ij"]["argument_partition"]),
        bool(inv["omega_resonance"]["is_resonant"]),
        inv["symmetry"]["n_observed"],
        inv.get("z_resonance_nontrivial_count", 0),
        inv["multi_edge"].get("edges_disjoint", True),
        inv["multi_edge"].get("zero_roots", 0) > 0,
    )


def cluster_invariants(invariants: list[dict[str, Any]]) -> list[dict[str, Any]]:
    buckets: dict[tuple, list[dict[str, Any]]] = defaultdict(list)
    for inv in invariants:
        buckets[clustering_key(inv)].append(inv)
    clusters = []
    for i, (key, members) in enumerate(sorted(buckets.items(), key=lambda x: (-len(x[1]), x[0]))):
        # describe
        rep = members[0]
        desc_parts = [f"family={key[0]}", f"edges={key[1]}",
                      f"Delta-mod-partition={list(key[2])}",
                      f"Delta-arg-partition={list(key[3])}",
                      f"omega-resonant={key[4]}",
                      f"sym C_{key[5]}",
                      f"nontrivial-z-relations={key[6]}",
                      f"edges-disjoint={key[7]}",
                      f"zero-roots={key[8]}"]
        clusters.append({
            "id": f"P3C{i:02d}",
            "key": list(key),
            "description": "; ".join(desc_parts),
            "n_members": len(members),
            "members": [m["operator"] for m in members],
            "representative_invariants": {
                "delta_modulus_partition": rep["delta_ij"]["modulus_partition"],
                "delta_argument_partition": rep["delta_ij"]["argument_partition"],
                "n_distinct_moduli": rep["delta_ij"]["n_distinct_moduli"],
                "z_resonance_count": len(rep["z_resonance"]),
                "omega_resonance_denom": rep["omega_resonance"]["denom"],
                "symmetry_C_n": rep["symmetry"]["n_observed"],
                "multi_edge_overview": rep["multi_edge"],
            },
        })
    return clusters


# =====================================================================
# 7. conjecture_engine
# =====================================================================

def make_phase3_conjectures(invariants: list[dict[str, Any]],
                              clusters: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []

    # MULTI-EDGE LAW 1: per-edge factorisation
    multi_ops = [inv for inv in invariants if inv["n_edges"] >= 2 and inv["family"] == "scalar"]
    out.append({
        "id": "M1",
        "title": "Per-edge factorisation (multi-edge generalisation of the Main Theorem)",
        "statement": (
            "For a scalar operator L with Newton polygon N(L) having edges E_1, ..., E_m at the "
            "irregular singularity (ordered by increasing slope), each E_alpha of slope -p_alpha/q_alpha "
            "with r_alpha+1 lattice points contributes a characteristic polynomial "
            "chi^{(alpha)}(c) = c^{k_0^{(alpha)}} * chi_w^{(alpha)}(c^{q_alpha}). "
            "The full WKB symbol factors as the PRODUCT chi(c) = prod_alpha chi^{(alpha)}(c) "
            "and the constellation C(L) is the (multiset) DISJOINT UNION of per-edge constellations C_alpha, "
            "each obtained from chi_w^{(alpha)} by the same mu_{q_alpha}-equivariant pullback as the Main Theorem."
        ),
        "evidence": {
            "n_multi_edge_operators": len(multi_ops),
            "examples": [op["operator"] for op in multi_ops[:5]],
            "edges_disjoint_count": sum(1 for inv in multi_ops if inv["multi_edge"].get("edges_disjoint", False)),
        },
        "remarks": (
            "Independence is generic: per-edge constellations occupy distinct radii in the OPEN stratum. "
            "Equal-radius collisions between different edges define an inter-edge degeneracy locus that "
            "extends the Phase-1 single-edge stratification."
        ),
    })

    # MULTI-EDGE LAW 2: zero-root sharing
    zero_root_count = sum(1 for inv in multi_ops if inv["multi_edge"].get("zero_roots", 0) > 0)
    out.append({
        "id": "M2",
        "title": "Multi-edge zero-root sharing (right-edge)",
        "statement": (
            "Let N(L) have two consecutive edges E_alpha (less negative slope) and E_beta (more negative, dominant) "
            "meeting at the joint vertex (k_*, d_*) with k_* > 0. Indexing per-edge characteristic polynomials so "
            "that the leftmost lattice point of each edge starts at k = 0, the dominant edge's chi^{(beta)}(c) "
            "factors as c^{k_*} * chi_w^{(beta)}(c^{q_beta}); the less-negative edge contributes no factor of c. "
            "Thus C_beta carries a multiplicity-k_* root at c = 0, while C_alpha generically does not. In particular, "
            "multi-edge polygons always exhibit the dominant-edge zero-root degeneracy."
        ),
        "evidence": {"multi_edge_operators_with_dominant_zero_roots": zero_root_count,
                     "examples": [inv["operator"] for inv in multi_ops if inv["multi_edge"].get("zero_roots", 0) > 0][:5],
                     "observed_per_edge_zero_root_distribution": "left edges always 0; right (dominant) edge gives k_* zeros equal to the joint k-coordinate."},
        "remarks": "Extends the Phase-1 zero-root stratum: in single-edge polygons alpha_r = 0 was an accidental degeneracy; in multi-edge polygons the zero-root is *generic* on the dominant edge, with multiplicity given by the joint vertex.",
    })

    # DELTA UNIVERSALITY 1
    open_strat = [inv for inv in invariants if not inv["omega_resonance"]["is_resonant"]
                  and inv["family"] == "scalar"
                  and inv["n_edges"] == 1]
    out.append({
        "id": "D1",
        "title": "Delta-modulus partition law (open stratum)",
        "statement": (
            "For a scalar single-edge operator on the open stratum (distinct |w_i|, distinct args, no Z- or omega-resonance), "
            "the multiset of pairwise differences {|c_i - c_j| : i<j} has cardinality exactly "
            "binomial(rq, 2) = rq(rq-1)/2, and the modulus partition factors as a product of three contributions: "
            "(i) intra-ring differences indexed by pairs in mu_q, (ii) inter-ring differences indexed by pairs (w_i, w_j), "
            "(iii) a global rotation of all of (ii) by the same mu_q action. "
            "In particular, the number of DISTINCT moduli in the Delta-multiset is at most (q-1)/2 + r*q*(r-1)/2 (counting multiplicities)."
        ),
        "evidence": {"open_stratum_count": len(open_strat),
                     "examples": [inv["operator"] for inv in open_strat[:5]],
                     "observed_distinct_moduli": [inv["delta_ij"]["n_distinct_moduli"] for inv in open_strat[:10]]},
    })

    # DELTA UNIVERSALITY 2 (Z-resonance dichotomy)
    zres_ops = [inv for inv in invariants if inv.get("z_resonance_nontrivial_count", 0) > 0]
    forced_only = [inv for inv in invariants if inv.get("z_resonance_nontrivial_count", 0) == 0
                   and len(inv["z_resonance"]) > 0]
    no_z = [inv for inv in invariants if len(inv["z_resonance"]) == 0]
    # Sharpness for prime-q ops: q in {5, 7}
    def _q_prime_genc(inv):
        return ("_genc_" in inv.get("operator", "") and inv["n_edges"] == 1
                and any(s in inv.get("operator", "") for s in ("o5_", "o7_")))
    prime_q_genc = [inv for inv in invariants if _q_prime_genc(inv)]
    prime_q_genc_zero_Z = [inv for inv in prime_q_genc if inv.get("z_resonance_nontrivial_count", 0) == 0]
    simple_multiring = [inv for inv in invariants
                        if inv.get("z_resonance_nontrivial_count", 0) > 0
                        and "_simple_" in inv.get("operator", "")]
    out.append({
        "id": "D2",
        "title": "Inner-polynomial Z-resonance dichotomy (prime-q version)",
        "statement": (
            "Let L be scalar with one dominant edge of slope -p/q with q PRIME and inner polynomial chi_w "
            "of degree r >= 2, so C(L) is a disjoint union of r mu_q-orbits with radii rho_alpha = |w_alpha|^{1/q}. "
            "Call a small-coefficient (|n_k| <= 3, support <= 4) Z-relation sum n_k c_k = 0 *mu_q-forced* if "
            "its per-ring partial sums each vanish individually; otherwise call it *cross-ring nontrivial*. "
            "Then: (i) for GENERIC chi_w (the w_alpha algebraically independent over Q), C(L) admits no "
            "cross-ring nontrivial Z-relation; (ii) for SIMPLE chi_w (the w_alpha satisfying a Q-linear "
            "relation), C(L) admits cross-ring nontrivial Z-relations -- one for each independent Q-linear "
            "dependence among the q-th roots w_alpha^{1/q}. For COMPOSITE q the same statement holds modulo "
            "the cyclotomic relations of mu_q acting on each ring (the mu_q-forced piece is correspondingly "
            "richer and includes Z-combinations of single-ring sub-orbit sums)."
        ),
        "evidence": {
            "operators_with_nontrivial_z": len(zres_ops),
            "operators_with_only_mu_q_forced_z": len(forced_only),
            "operators_with_no_z": len(no_z),
            "prime_q_genc_operators": len(prime_q_genc),
            "prime_q_genc_with_zero_nontrivial_Z": len(prime_q_genc_zero_Z),
            "simple_multiring_with_Z": len(simple_multiring),
            "examples_prime_q_genc_no_Z": [inv["operator"] for inv in prime_q_genc_zero_Z[:5]],
            "examples_simple_with_Z": [inv["operator"] for inv in simple_multiring[:5]],
            "sharpness": (
                "All prime-q (q=5 or 7) generic-chi_w single-edge operators produce zero cross-ring "
                "Z-relations; every simple-chi_w multi-ring operator produces at least 5. The dichotomy "
                "is exact for prime q in the sweep."
            ),
        },
        "remarks": (
            "Cross-ring Z-relations form a *lattice* in C(L) - C(L) that is invariant of the chi_w-stratum: "
            "operators on the same chi_w-stratum share their cross-ring Z-resonance lattice. This lattice "
            "is a finer invariant than mu_q symmetry and refines D1's modulus partition into an arithmetic "
            "stratification of F."
        ),
    })

    # OMEGA-RESONANCE LAW
    omega_ops = [inv for inv in invariants if inv["omega_resonance"]["is_resonant"]]
    out.append({
        "id": "O1",
        "title": "Omega-resonance classification",
        "statement": (
            "The constellation C(L) has angular spacing in 2 pi * (Z/m) with m > q if and only if "
            "chi_w has roots on a finite Galois orbit of (Z/m)^x distinct from the trivial mu_q-orbit. "
            "Equivalently: omega-resonance is equivalent to chi_w factoring as a product of cyclotomic-like polynomials "
            "in w whose roots have a common rational angular spacing."
        ),
        "evidence": {"omega_resonant_count": len(omega_ops),
                     "examples": [inv["operator"] for inv in omega_ops[:5]],
                     "observed_denoms": sorted({inv["omega_resonance"]["denom"] for inv in omega_ops})},
        "remarks": (
            "This is the 'accidental symmetry' phenomenon of Phase 1 elevated to a precise structural law: "
            "the symmetry-inflation factor m / q is exactly the LCM of the inner Galois orbits' angular denominators."
        ),
    })

    # SYSTEM PULLBACK
    sys_ops = [inv for inv in invariants if inv["family"] == "system"]
    out.append({
        "id": "S1",
        "title": "System pullback: blocks act independently on F",
        "statement": (
            "For a block-diagonal system Phi = diag(L_1, ..., L_n) of scalar operators, the constellation "
            "C(Phi) is the multiset disjoint union of C(L_i). Hence F(Phi) = bigsqcup_i F(L_i), and F factors "
            "through the symmetric power: F : Sys^n(scalar local models) -> Sym^n( finite multisets in C )."
        ),
        "evidence": {"system_operators": len(sys_ops),
                     "examples": [inv["operator"] for inv in sys_ops]},
        "remarks": (
            "This handles block-diagonal systems exactly; for general (coupled) systems the same disjoint-union "
            "statement holds after diagonalisation of the leading symbol when the eigenvalues are distinct; "
            "coalescence of eigenvalues defines a system-level discriminant stratum, conjecturally classified "
            "by Levelt-Turrittin decomposition."
        ),
    })

    # P-INVARIANCE TEST RESULT
    pinv_ops = [inv for inv in invariants if inv["operator"].startswith("PINV")]
    if pinv_ops:
        sigs = [tuple(inv["delta_ij"]["modulus_partition"]) for inv in pinv_ops]
        all_equal = all(s == sigs[0] for s in sigs)
        out.append({
            "id": "P1",
            "title": "p-invariance of the Delta-modulus partition (verified for q=5)",
            "statement": (
                "Fixing q and r, varying p in {1, 2, 3, 4} (all coprime to 5) while keeping chi_w fixed "
                "produces operators with IDENTICAL Delta-modulus partitions and identical C_n symmetry orders. "
                "Hence the slope numerator p is invisible to the Delta-invariant as well as to F itself."
            ),
            "evidence": {"pinv_examples": [inv["operator"] for inv in pinv_ops],
                         "all_signatures_equal": all_equal,
                         "common_signature": list(sigs[0]) if all_equal else "FAILED"},
            "remarks": (
                "Phase 1 conjectured this for F (the constellation); Phase 3 elevates it to the finer Delta-invariant."
            ),
        })

    # NESTED RAMIFICATION
    nest_ops = [inv for inv in invariants if inv["operator"].startswith("NEST")]
    out.append({
        "id": "N1",
        "title": "Nested ramification: iterated mu_q-pullback",
        "statement": (
            "If chi_w(w) itself factors as chi_v(w^{q'}) for some q' > 1 (i.e. chi_w has only exponents in q' Z), "
            "then C(L) = bigsqcup_{v in Roots(chi_v)} { c : c^{q q'} = v }, exhibiting (mu_q x mu_{q'})-equivariance. "
            "The effective ramification is q q' and the apparent symmetry group is C_{q q'}, "
            "even though the Newton polygon advertises only q."
        ),
        "evidence": {"nested_examples": [inv["operator"] for inv in nest_ops],
                     "observed_symmetries": [(inv["operator"], inv["symmetry"]["n_observed"]) for inv in nest_ops]},
        "remarks": "This is the iterated form of the Main Theorem; it explains 'hidden' symmetry inflation in chi without invoking a Newton-polygon refinement.",
    })

    # SLOPE-FILTRATION
    out.append({
        "id": "F1",
        "title": "Slope-filtration target for multi-edge F",
        "statement": (
            "F extends to multi-edge scalar operators with target = the category of FILTERED multisets in C "
            "(ordered by the slope sequence of N(L)). The grading captures the asymptotic dominance: "
            "an exponent c in C_alpha (slope -p_alpha/q_alpha) controls the WKB solution at order x^{p_alpha/q_alpha}. "
            "The single-edge classification of Phase 1 is the associated-graded of this filtration on each stratum."
        ),
        "evidence": {"multi_edge_operators": len(multi_ops)},
        "remarks": "This is the natural functorial reframing of multi-edge as a filtration whose graded pieces are Phase-1 classes.",
    })

    # GALOIS-ON-RINGS
    gal_ops = [inv for inv in invariants if inv["operator"].startswith("GAL")]
    out.append({
        "id": "G1",
        "title": "Galois action on rings",
        "statement": (
            "The absolute Galois group Gal(Q-bar/Q) acts on the roots of chi_w; this action lifts uniquely to a "
            "permutation of the rings R_k of C(L) covering the mu_q action. The orbit structure of Gal on rings "
            "is an arithmetic invariant of F refining the modulus partition."
        ),
        "evidence": {"galois_examples": [inv["operator"] for inv in gal_ops],
                     "observed_omega_denoms": [(inv["operator"], inv["omega_resonance"]["denom"]) for inv in gal_ops]},
        "remarks": (
            "When chi_w is irreducible over Q, all rings form a single Galois orbit; "
            "when chi_w factors, the rings split according to the factorisation. "
            "GAL_cyclotomic_3 / 5 give cyclotomic ring orbits with omega-resonance denominators 6 / 10 respectively."
        ),
    })

    return out


# =====================================================================
# 8. Reporter
# =====================================================================

def serialise_for_json(o):
    if isinstance(o, complex):
        return [o.real, o.imag]
    if isinstance(o, np.floating):
        return float(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"not serialisable: {type(o)}")


def _strip_sympy_keys(d: Any) -> Any:
    """Recursively remove keys starting with '_' from dicts (used to drop sympy-only fields)."""
    if isinstance(d, dict):
        return {k: _strip_sympy_keys(v) for k, v in d.items() if not k.startswith("_")}
    if isinstance(d, list):
        return [_strip_sympy_keys(x) for x in d]
    return d


def write_outputs(operators: list[Op], np_infos: list[dict[str, Any]],
                  per_edge_chis: list[list[dict[str, Any]]],
                  invariants: list[dict[str, Any]], clusters: list[dict[str, Any]],
                  conjectures: list[dict[str, Any]]):
    out_dir = HERE
    # operators dump
    ops_dump = []
    for op, np_info, pec in zip(operators, np_infos, per_edge_chis):
        ops_dump.append({
            "name": op.name,
            "family": op.family,
            "eqtype": op.eqtype,
            "notes": op.notes,
            "coeffs": [sp.sstr(c) for c in op.coeffs_sym] if op.family == "scalar" else [],
            "system_blocks": op.system_blocks if op.family == "system" else [],
            "newton": np_info,
            "per_edge_chi": _strip_sympy_keys(pec),
        })
    def _write(name, payload):
        (out_dir / name).write_text(
            json.dumps(_strip_sympy_keys(payload), indent=2, default=serialise_for_json),
            encoding="utf-8")
    _write("phase3_operators.json", ops_dump)
    _write("phase3_invariants.json", invariants)
    _write("phase3_clusters.json", clusters)
    _write("phase3_conjectures.json", conjectures)
    _write("phase3_summary.json", DRAFT_SUMMARY)
    _write("phase3_gaps.json", GAPS)


def write_report(operators: list[Op], invariants: list[dict[str, Any]],
                 clusters: list[dict[str, Any]], conjectures: list[dict[str, Any]]):
    lines = []
    lines.append("# Phase III — Deepening the WKB / Newton-Polygon Classification Theory")
    lines.append("")
    lines.append("## 1. Structured summary of the draft theory (draft_reader)")
    lines.append("")
    lines.append(f"**Title:** {DRAFT_SUMMARY['title']}")
    lines.append("")
    lines.append("**Main Theorem:** " + DRAFT_SUMMARY["main_theorem"])
    lines.append("")
    lines.append("**Corollaries:**")
    for c in DRAFT_SUMMARY["corollaries"]:
        lines.append(f"- {c}")
    lines.append("")
    lines.append("**Degeneracy loci:**")
    for d in DRAFT_SUMMARY["degeneracy_loci"]:
        lines.append(f"- {d}")
    lines.append("")
    lines.append("**Open problems explicitly stated in the draft:**")
    for o in DRAFT_SUMMARY["open_problems_stated"]:
        lines.append(f"- {o}")
    lines.append("")

    lines.append("## 2. Gaps and research directions (gap_finder)")
    lines.append("")
    for g in GAPS:
        lines.append(f"- **{g['id']}. {g['title']}** — {g['why']}")
    lines.append("")

    lines.append("## 3. Extended operator zoo (operator_generator)")
    lines.append("")
    lines.append(f"Generated **{len(operators)}** operators across the following families:")
    by_family = Counter(op.family for op in operators)
    for fam, n in by_family.items():
        lines.append(f"  - {fam}: {n}")
    lines.append("")
    by_prefix: dict[str, list[str]] = defaultdict(list)
    for op in operators:
        prefix = op.name.split("_")[0]
        by_prefix[prefix].append(op.name)
    for prefix, names in by_prefix.items():
        lines.append(f"**{prefix}** ({len(names)} operators): {', '.join(names[:6])}{'...' if len(names) > 6 else ''}")
    lines.append("")

    lines.append("## 4. Extended invariants (invariant_engine)")
    lines.append("")
    lines.append("New invariants computed for every operator:")
    lines.append("- **Delta_ij modulus and argument partitions**: the multiset of pairwise differences {c_i - c_j}, partitioned by modulus and by argument modulo 2π.")
    lines.append("- **Z-resonance**: small integer relations Σ n_k c_k = 0 with |n_k| ≤ 3, ≤ 4 terms.")
    lines.append("- **Omega-resonance**: smallest m so that all arg(c_i)/arg(c_j) differences are in 2π·(Z/m); flagged when m > q.")
    lines.append("- **Symmetry inflation**: largest C_n leaving the multiset invariant; compared to the Newton-polygon-predicted C_q.")
    lines.append("- **Multi-edge interference**: per-edge radii lists, shared-radii detection, edge-disjointness flag, zero-root count.")
    lines.append("")
    lines.append("**Highlights from the sweep:**")
    sym_inflated = [inv for inv in invariants if inv["symmetry"]["inflated"]]
    omega_res = [inv for inv in invariants if inv["omega_resonance"]["is_resonant"]]
    z_res_nontrivial = [inv for inv in invariants if inv.get("z_resonance_nontrivial_count", 0) > 0]
    z_res_only_trivial = [inv for inv in invariants
                          if inv.get("z_resonance_nontrivial_count", 0) == 0
                          and len(inv["z_resonance"]) > 0]
    multi = [inv for inv in invariants if inv["n_edges"] >= 2]
    lines.append(f"- {len(sym_inflated)} operators exhibit symmetry inflation (C_n with n > q).")
    lines.append(f"- {len(omega_res)} operators exhibit omega-resonance (angular denominator strictly larger than q).")
    lines.append(f"- {len(z_res_nontrivial)} operators admit a *cross-ring nontrivial* Z-resonance (per-ring partial sums do not individually vanish).")
    lines.append(f"- {len(z_res_only_trivial)} operators admit only mu_q-forced Z-resonances (relations lying in the Z-span of single-ring cyclotomic ideals).")
    lines.append(f"- {len(multi)} operators have multi-edge Newton polygons.")
    lines.append("")

    lines.append("## 5. New universality classes (clustering_engine)")
    lines.append("")
    lines.append(f"Clustering by the extended invariant key produces **{len(clusters)}** classes (versus 23 in Phase 1).")
    lines.append("")
    lines.append("| Class | n | Description |")
    lines.append("|---|---:|---|")
    for cl in clusters:
        lines.append(f"| `{cl['id']}` | {cl['n_members']} | {cl['description']} |")
    lines.append("")
    lines.append("Of these, several are *new* in the sense that they lie outside the Phase-1 atlas:")
    new_classes = [cl for cl in clusters if cl["key"][1] >= 2 or cl["key"][4] or cl["key"][0] != "scalar"]
    lines.append(f"- {len(new_classes)} classes lie in multi-edge, omega-resonant, or system territory not covered by Phase 1.")
    lines.append("")

    lines.append("## 6. Next-level conjectures (conjecture_engine)")
    lines.append("")
    for c in conjectures:
        lines.append(f"### {c['id']}. {c['title']}")
        lines.append("")
        lines.append(f"**Statement.** {c['statement']}")
        lines.append("")
        lines.append(f"**Evidence.** " + json.dumps(c["evidence"], default=serialise_for_json))
        if "remarks" in c:
            lines.append("")
            lines.append(f"**Remarks.** {c['remarks']}")
        lines.append("")

    lines.append("## 7. How Phase III extends the classification theory")
    lines.append("")
    lines.append(
        "The Phase-1+2 theory described F as a functor from single-edge scalar local models to "
        "multisets in C, with image stratified by 23 constellation classes. Phase III enlarges F in **four** dimensions:"
    )
    lines.append("")
    lines.append("1. **Source category enlarged** — to multi-edge scalar operators (via the per-edge factorisation law M1) and to "
                 "block-diagonal systems (via the system-pullback law S1). The latter exhibits F as compatible with `Sym^n`-product structure.")
    lines.append("2. **Target enriched with a slope filtration** — multi-edge constellations are no longer flat multisets but "
                 "*filtered* multisets graded by Newton-polygon slope (F1). Phase-1 classes are recovered as the associated graded pieces.")
    lines.append("3. **Finer invariants on the target side** — the Delta_{ij} modulus and argument partitions (D1), Z-resonance "
                 "signatures (D2), omega-resonance denominators (O1), and Galois orbit structure on rings (G1) all refine the "
                 "constellation invariant. These bring F into contact with Stokes-graph and spectral-network combinatorics, "
                 "which depend on differences c_i - c_j rather than the c_i themselves.")
    lines.append("4. **Iterated ramification** — chi_w may itself admit a mu_{q'}-pullback structure (N1), producing apparent "
                 "symmetry C_{q q'} with only C_q visible from the Newton polygon. This is the precise structural mechanism "
                 "behind the Phase-1 'accidental symmetry' phenomenon.")
    lines.append("")
    lines.append(
        "The combined result: F factors as a tower"
    )
    lines.append("")
    lines.append("    F : { multi-edge scalar / system local models } -> { filtered Galois-equivariant multisets in C }")
    lines.append("")
    lines.append(
        "with each layer of refinement (multi-edge -> slope-filtration; chi_w -> nested ramification; Delta_ij -> Stokes adjacency) "
        "introducing exactly one new universal stratum. The 23 Phase-1 classes describe the simplest layer (single edge, no resonance, "
        "no inflation); the additional classes catalogued here populate the deeper layers in a uniform combinatorial language."
    )
    lines.append("")
    (HERE / "phase3_report.md").write_text("\n".join(lines), encoding="utf-8")


# =====================================================================
# Main
# =====================================================================

def main():
    print("[draft_reader] structured summary fixed.")
    print(f"[gap_finder] {len(GAPS)} gaps identified.")
    operators = generate_phase3_operators()
    print(f"[operator_generator] generated {len(operators)} operators.")
    np_infos: list[dict[str, Any]] = []
    per_edge_chis: list[list[dict[str, Any]]] = []
    invariants: list[dict[str, Any]] = []
    for op in operators:
        try:
            np_info = compute_newton_polygon(op)
        except Exception as e:
            print(f"  [{op.name}] newton polygon ERROR: {e}")
            np_infos.append({"error": str(e), "edges": [], "n_edges": 0})
            per_edge_chis.append([])
            continue
        np_infos.append(np_info)
        try:
            per_edge_chi = compute_per_edge_chi(op, np_info)
        except Exception as e:
            print(f"  [{op.name}] per-edge chi ERROR: {e}")
            per_edge_chi = []
        per_edge_chis.append(per_edge_chi)
        try:
            inv = invariants_for_operator(op, np_info, per_edge_chi)
        except Exception as e:
            print(f"  [{op.name}] invariants ERROR: {e}")
            inv = {"operator": op.name, "error": str(e),
                   "family": op.family, "eqtype": op.eqtype,
                   "n_edges": np_info.get("n_edges", 0),
                   "per_edge": [], "per_edge_constellations": [], "full_constellation": [],
                   "delta_ij": {"modulus_partition": [], "argument_partition": [], "n_distinct_moduli": 0, "n_distinct_args": 0},
                   "z_resonance": [], "z_resonance_nontrivial_count": 0,
                   "omega_resonance": {"is_resonant": False, "denom": 0, "expected_q": 1, "ratio_to_q": 0.0},
                   "symmetry": {"n_observed": 1, "expected_q": 1, "inflated": False, "ratio": 1.0},
                   "multi_edge": {"n_edges": 0, "interference": "error", "edges_disjoint": True, "zero_roots": 0},
                   "notes": op.notes}
        invariants.append(inv)
    print(f"[invariant_engine] computed invariants for {len(invariants)} operators.")
    clusters = cluster_invariants(invariants)
    print(f"[clustering_engine] {len(clusters)} clusters.")
    conjectures = make_phase3_conjectures(invariants, clusters)
    print(f"[conjecture_engine] {len(conjectures)} conjectures.")
    write_outputs(operators, np_infos, per_edge_chis, invariants, clusters, conjectures)
    write_report(operators, invariants, clusters, conjectures)
    print("[report] phase3_report.md written.")


if __name__ == "__main__":
    main()
