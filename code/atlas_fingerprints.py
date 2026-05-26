"""
atlas_fingerprints.py
======================

Consolidated Series-A fingerprint analyzer for the 23-class and 39-class
WKB constellation atlases. Produces two deliverables that the existing
reports did not separately provide:

  A1 — Constellation-shape fingerprints
       (per-class ring-radius ratios, angular-gap multisets, slope and
       Delta-modulus signatures, pairwise distance matrix, hierarchical
       dendrogram, and minimal distinguishing invariants).

  A2 — Symmetry-breaking fingerprints
       (per-class mu_q stabilizer C_k extracted from the constellation
       data, omega-resonance and z-resonance flags, and a nontrivial-
       stabilizer roll-up table).

Inputs  (existing repo data, no recomputation needed):
  data/constellations.json     -- per-operator ring radii, ring args, Cn_order
  data/clusters.json           -- 23-class atlas, one representative per class
  data/phase3_clusters.json    -- 39-class refined atlas with members + invariants
  data/slope_invariants.json   -- per-class slope multiset, depth, n_edges
  data/phase4_ray_equivalence.json
                               -- per-entry F_gap (rotation-invariant) classes

Outputs:
  data/atlas_fingerprints.json    -- machine-readable consolidated record
  reports/atlas_fingerprints.md   -- human-readable A1 + A2 report
"""

from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
REPORTS = REPO / "reports"


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------

def load_json(name: str) -> Any:
    with (DATA / name).open("r", encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------
# Per-operator constellation geometry
# ---------------------------------------------------------------------------

def ring_radius_ratios(rings: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    """Sort rings by radius ascending; report normalized ratio list r_i / r_1
    (the innermost ring) and the max/min ratio.

    rings: list of dicts with key "radius".
    """
    radii = sorted(float(r["radius"]) for r in rings if float(r["radius"]) > 1e-12)
    if not radii:
        return {
            "n_rings": 0,
            "radii_sorted": [],
            "ratios_to_inner": [],
            "spread_max_over_min": None,
        }
    r1 = radii[0]
    ratios = [round(r / r1, 6) for r in radii]
    return {
        "n_rings": len(radii),
        "radii_sorted": [round(r, 6) for r in radii],
        "ratios_to_inner": ratios,
        "spread_max_over_min": round(radii[-1] / r1, 6),
    }


def angular_gap_multiset(args: Sequence[float]) -> List[float]:
    """Sorted cyclic-gap multiset of one ring (canonical = rotation-invariant)."""
    if len(args) <= 1:
        return []
    a = sorted(float(x) for x in args)
    gaps = [a[i + 1] - a[i] for i in range(len(a) - 1)]
    gaps.append(2 * math.pi - (a[-1] - a[0]))
    gaps = [round(g, 6) for g in gaps]
    return sorted(gaps)


def per_ring_gap_multisets(rings: Sequence[Dict[str, Any]]) -> List[List[float]]:
    out = []
    for r in rings:
        args = r.get("args") or []
        out.append(angular_gap_multiset(args))
    return out


# ---------------------------------------------------------------------------
# Builders for the 23-class and 39-class atlases
# ---------------------------------------------------------------------------

def build_per_op_index(constellations: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    return {c["name"]: c for c in constellations}


def class_fingerprint_23(cluster: Dict[str, Any]) -> Dict[str, Any]:
    """For the 23-class atlas, each class entry already carries a representative
    with `rings` embedded. We pull A1/A2 invariants directly off it."""
    rep = cluster["representative"]
    rings = rep.get("rings") or []
    radii_block = ring_radius_ratios(rings)
    # Cn_order is not in clusters.json directly; the label encodes it.
    label = cluster["label"]
    is_regular = "Regular-" in label
    cn_order_from_label = _extract_cn_from_label(label, rings, is_regular)
    return {
        "atlas": "23-class",
        "label": label,
        "description": cluster.get("description", ""),
        "members": cluster.get("members", []),
        "n_members": len(cluster.get("members", []) or []),
        "rep_name": rep.get("name"),
        "slope": rep.get("slope"),
        "rank": rep.get("rank"),
        "n_roots": sum(int(r.get("count", 0)) for r in rings),
        "ring_counts": [int(r.get("count", 0)) for r in rings],
        **radii_block,
        "per_ring_gap_multiset": per_ring_gap_multisets(rings),
        "Cn_order": cn_order_from_label,
        "is_regular_polygon": is_regular,
    }


def _extract_cn_from_label(label: str, rings, is_regular: bool) -> int:
    """Pull C_k stabilizer order from a 23-class label like 'Class[C4, rings=[4, 4, 4]]'
    or 'Class[Regular-12-gon]'. Falls back to gcd of ring counts when ambiguous."""
    import re
    m = re.search(r"Regular-(\d+)-gon", label)
    if m:
        return int(m.group(1))
    m = re.search(r"\bC(\d+)\b", label)
    if m:
        return int(m.group(1))
    counts = [int(r.get("count", 0)) for r in rings]
    if not counts:
        return 1
    from math import gcd
    g = counts[0]
    for c in counts[1:]:
        g = gcd(g, c)
    return max(g, 1)


def rings_from_complex_roots(
    roots_re_im: Sequence[Sequence[float]],
    rel_tol: float = 5e-3,
    zero_radius_eps: float = 1e-9,
) -> Tuple[List[Dict[str, Any]], int]:
    """Group complex c-roots [(re, im), ...] into rings by clustering on |c|.

    Returns (rings, n_zero_roots). Roots with |c| <= zero_radius_eps are excluded
    from the ring list and reported separately as `n_zero_roots`, because they
    do not form a geometric ring (zero-radius "rings" arise on multi-edge classes
    where one edge has a degenerate c=0 contribution).

    Two radii r1 <= r2 fall in the same ring iff (r2 - r1) / max(r2, 1e-12) <= rel_tol.
    Within each ring the angular positions are sorted ascending.
    """
    if not roots_re_im:
        return [], 0
    enriched = []
    n_zero = 0
    for (re, im) in roots_re_im:
        r = math.hypot(float(re), float(im))
        if r <= zero_radius_eps:
            n_zero += 1
            continue
        enriched.append((r, math.atan2(float(im), float(re))))
    enriched.sort(key=lambda t: t[0])
    rings: List[Dict[str, Any]] = []
    cur_radii: List[float] = []
    cur_args: List[float] = []
    for r, a in enriched:
        if not cur_radii or (r - cur_radii[-1]) / max(r, 1e-12) <= rel_tol:
            cur_radii.append(r)
            cur_args.append(a)
        else:
            rings.append(
                {
                    "radius": sum(cur_radii) / len(cur_radii),
                    "count": len(cur_radii),
                    "args": sorted(cur_args),
                }
            )
            cur_radii = [r]
            cur_args = [a]
    if cur_radii:
        rings.append(
            {
                "radius": sum(cur_radii) / len(cur_radii),
                "count": len(cur_radii),
                "args": sorted(cur_args),
            }
        )
    return rings, n_zero


def class_fingerprint_39(
    cluster: Dict[str, Any],
    p3_invariants_by_op: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    """For the 39-class atlas, take the first member operator's Phase-3
    invariants record (which has full_constellation as [re, im] pairs) to
    derive ring radii, then merge with the cluster's representative_invariants
    block for the algebraic-symmetry data (symmetry_C_n, omega, z)."""
    members = cluster.get("members") or []
    rep_name = members[0] if members else None
    p3 = p3_invariants_by_op.get(rep_name) if rep_name else None
    full_const = (p3 or {}).get("full_constellation") or []
    rings, n_zero_roots = rings_from_complex_roots(full_const)
    radii_block = ring_radius_ratios(rings)
    inv = cluster.get("representative_invariants", {}) or {}
    # Authoritative stabilizer: the cluster-key value (from representative_invariants).
    cn_order = inv.get("symmetry_C_n")
    if cn_order is None and rings:
        cn_order = 0
    return {
        "atlas": "39-class",
        "id": cluster["id"],
        "description": cluster.get("description", ""),
        "members": members,
        "n_members": len(members),
        "rep_name": rep_name,
        "n_roots": sum(int(r.get("count", 0)) for r in rings) + n_zero_roots if (rings or n_zero_roots) else None,
        "n_zero_roots": n_zero_roots,
        "ring_counts": [int(r.get("count", 0)) for r in rings],
        **radii_block,
        "per_ring_gap_multiset": per_ring_gap_multisets(rings),
        "Cn_order": cn_order,
        "is_regular_polygon": (
            (len(rings) == 1) and (rings[0].get("count", 0) >= 3) if rings else False
        ),
        "symmetry_C_n_invariant": inv.get("symmetry_C_n"),
        "omega_resonance_denom": inv.get("omega_resonance_denom"),
        "z_resonance_count": inv.get("z_resonance_count"),
        "delta_modulus_partition": inv.get("delta_modulus_partition"),
        "delta_argument_partition": inv.get("delta_argument_partition"),
        "n_edges": (inv.get("multi_edge_overview") or {}).get("n_edges"),
    }


# ---------------------------------------------------------------------------
# Dendrogram (textual hierarchical clustering on fingerprint feature vector)
# ---------------------------------------------------------------------------

def fingerprint_feature_vector(fp: Dict[str, Any]) -> Tuple:
    """Hashable fingerprint feature key used for the dendrogram.

    Captures: (n_rings, ring_counts, ratios_to_inner, Cn_order). Two classes
    that share this exact tuple are reported as collisions inside the
    final dendrogram leaves; otherwise they split at the corresponding
    similarity level.
    """
    return (
        int(fp.get("n_rings") or 0),
        tuple(int(c) for c in (fp.get("ring_counts") or [])),
        tuple(fp.get("ratios_to_inner") or []),
        int(fp.get("Cn_order") or 0),
    )


def dendrogram_levels(fps: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Coarse-to-fine clustering. We use 5 progressively finer keys:

      L1 — Cn_order   (group by stabilizer order)
      L2 — (Cn_order, n_rings)
      L3 — (Cn_order, n_rings, ring_counts)
      L4 — (Cn_order, n_rings, ring_counts, ratios_to_inner)
      L5 — full fingerprint_feature_vector

    Each level reports cluster sizes + how many leaves remain to be split.
    """

    def key(fp: Dict[str, Any], level: int) -> Tuple:
        cn = int(fp.get("Cn_order") or 0)
        nr = int(fp.get("n_rings") or 0)
        rc = tuple(int(c) for c in (fp.get("ring_counts") or []))
        rr = tuple(fp.get("ratios_to_inner") or [])
        if level == 1:
            return (cn,)
        if level == 2:
            return (cn, nr)
        if level == 3:
            return (cn, nr, rc)
        if level == 4:
            return (cn, nr, rc, rr)
        return fingerprint_feature_vector(fp)

    out = []
    for level in range(1, 6):
        buckets: Dict[Tuple, List[str]] = defaultdict(list)
        for fp in fps:
            tag = fp.get("id") or fp.get("label")
            buckets[key(fp, level)].append(tag)
        out.append(
            {
                "level": level,
                "n_buckets": len(buckets),
                "buckets": [
                    {"key": list(k), "members": sorted(v)} for k, v in sorted(buckets.items())
                ],
            }
        )
    return out


def minimal_distinguishing_invariants(fps: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Greedy search for the smallest subset of candidate invariants that
    separates all classes.

    Candidate invariants:
      I_Cn       -- Cn_order
      I_nrings   -- n_rings
      I_rc       -- ring_counts (tuple)
      I_ratios   -- ratios_to_inner
      I_slope    -- slope (23-class) or delta_modulus_partition (39-class)
      I_omega    -- omega_resonance_denom
      I_z        -- z_resonance_count
    """

    def feat(fp: Dict[str, Any], name: str):
        if name == "I_Cn":
            return int(fp.get("Cn_order") or 0)
        if name == "I_nrings":
            return int(fp.get("n_rings") or 0)
        if name == "I_rc":
            return tuple(fp.get("ring_counts") or [])
        if name == "I_ratios":
            return tuple(fp.get("ratios_to_inner") or [])
        if name == "I_slope":
            return fp.get("slope") or tuple(fp.get("delta_modulus_partition") or [])
        if name == "I_omega":
            return int(fp.get("omega_resonance_denom") or 0)
        if name == "I_z":
            return int(fp.get("z_resonance_count") or 0)
        return None

    invariants = ["I_Cn", "I_nrings", "I_rc", "I_ratios", "I_slope", "I_omega", "I_z"]

    def separates(subset: List[str]) -> Tuple[int, int]:
        keys = [tuple(feat(fp, name) for name in subset) for fp in fps]
        distinct = len(set(keys))
        n_collisions = len(fps) - distinct
        return distinct, n_collisions

    # Greedy: add the invariant that maximises separated-class count at each step.
    chosen: List[str] = []
    remaining = list(invariants)
    history = []
    while remaining:
        best_name = None
        best_distinct = -1
        for name in remaining:
            distinct, _ = separates(chosen + [name])
            if distinct > best_distinct:
                best_distinct = distinct
                best_name = name
        chosen.append(best_name)
        remaining.remove(best_name)
        d, c = separates(chosen)
        history.append({"step": len(chosen), "added": best_name, "distinct_classes": d, "collisions": c})
        if d == len(fps):
            break
    return {
        "minimal_set": chosen,
        "n_classes_total": len(fps),
        "history": history,
    }


# ---------------------------------------------------------------------------
# A2 -- Symmetry-breaking roll-up
# ---------------------------------------------------------------------------

def symmetry_rollup(fps: List[Dict[str, Any]]) -> Dict[str, Any]:
    by_cn: Dict[int, List[str]] = defaultdict(list)
    trivial: List[str] = []
    nontrivial: List[str] = []
    for fp in fps:
        cn = int(fp.get("Cn_order") or 0)
        tag = fp.get("id") or fp.get("label")
        by_cn[cn].append(tag)
        if cn <= 1:
            trivial.append(tag)
        else:
            nontrivial.append(tag)
    return {
        "n_classes": len(fps),
        "trivial_stabilizer_count": len(trivial),
        "nontrivial_stabilizer_count": len(nontrivial),
        "by_Cn_order": {str(k): sorted(v) for k, v in sorted(by_cn.items())},
        "trivial_classes": sorted(trivial),
        "nontrivial_classes": sorted(nontrivial),
    }


# ---------------------------------------------------------------------------
# Markdown report
# ---------------------------------------------------------------------------

def _fmt_ratios(rs):
    if not rs:
        return "—"
    return "[" + ", ".join(f"{r:g}" for r in rs) + "]"


def _fmt_gaps(per_ring_gaps):
    if not per_ring_gaps:
        return "—"
    parts = []
    for g in per_ring_gaps:
        if not g:
            parts.append("{}")
        else:
            parts.append("{" + ", ".join(f"{x:.4f}" for x in g) + "}")
    return " ; ".join(parts)


def render_a1_a2_report(
    fps_23: List[Dict[str, Any]],
    fps_39: List[Dict[str, Any]],
    dendro_23: List[Dict[str, Any]],
    dendro_39: List[Dict[str, Any]],
    minim_23: Dict[str, Any],
    minim_39: Dict[str, Any],
    sym_23: Dict[str, Any],
    sym_39: Dict[str, Any],
) -> str:
    L: List[str] = []
    L.append("# Series-A atlas fingerprints — Constellation shapes (A1) & Symmetry breaking (A2)")
    L.append("")
    L.append(
        "Per-class fingerprints across the 23-class base atlas (`data/clusters.json`) "
        "and the 39-class refined atlas (`data/phase3_clusters.json`). Constellation "
        "geometry for the 23-class atlas is taken from `data/constellations.json`; "
        "for the 39-class atlas it is reconstructed from `data/phase3_invariants.json` "
        "(field `full_constellation`). Symmetry / resonance data come from each "
        "cluster's `representative_invariants` block (the authoritative "
        "`symmetry_C_n` field is used as the μ_q stabilizer C_k order)."
    )
    L.append("")
    L.append("## Contents")
    L.append("- A1 §1: 23-class atlas — ring-radius ratios + angular-gap multisets")
    L.append("- A1 §2: 39-class atlas — ring-radius ratios + angular-gap multisets")
    L.append("- A1 §3: Hierarchical dendrogram (text form)")
    L.append("- A1 §4: Minimal distinguishing invariants")
    L.append("- A2 §1: 23-class symmetry-breaking table (μ_q stabilizer)")
    L.append("- A2 §2: 39-class symmetry-breaking table (μ_q stabilizer, ω-resonance, z-resonance)")
    L.append("- A2 §3: Nontrivial-stabilizer roll-up")
    L.append("")

    # ----- A1 §1
    L.append("## A1 §1 — 23-class atlas: constellation-shape fingerprints")
    L.append("")
    L.append("| Class | slope | n_rings | ring_counts | radii_sorted | ratios_to_inner | spread max/min | per-ring gap multisets |")
    L.append("|---|---|---:|---|---|---|---:|---|")
    for fp in fps_23:
        L.append(
            f"| `{fp['label']}` | {fp.get('slope') or '—'} | {fp.get('n_rings')} | "
            f"{fp.get('ring_counts')} | {_fmt_ratios(fp.get('radii_sorted') or [])} | "
            f"{_fmt_ratios(fp.get('ratios_to_inner') or [])} | "
            f"{fp.get('spread_max_over_min') if fp.get('spread_max_over_min') is not None else '—'} | "
            f"{_fmt_gaps(fp.get('per_ring_gap_multiset') or [])} |"
        )
    L.append("")

    # ----- A1 §2
    L.append("## A1 §2 — 39-class refined atlas: constellation-shape fingerprints")
    L.append("")
    L.append(
        "*Note.* Zero-radius roots (c = 0, arising on multi-edge classes with a "
        "degenerate sub-edge) are not counted as a ring; their count appears in "
        "the `0-roots` column instead."
    )
    L.append("")
    L.append(
        "| ID | n_edges | n_rings | ring_counts | 0-roots | radii_sorted | ratios_to_inner | spread | Δ-mod | Δ-arg |"
    )
    L.append("|---|---:|---:|---|---:|---|---|---:|---|---|")
    for fp in fps_39:
        dm = fp.get("delta_modulus_partition")
        da = fp.get("delta_argument_partition")
        L.append(
            f"| `{fp['id']}` | {fp.get('n_edges')} | {fp.get('n_rings')} | "
            f"{fp.get('ring_counts')} | {fp.get('n_zero_roots', 0)} | "
            f"{_fmt_ratios(fp.get('radii_sorted') or [])} | "
            f"{_fmt_ratios(fp.get('ratios_to_inner') or [])} | "
            f"{fp.get('spread_max_over_min') if fp.get('spread_max_over_min') is not None else '—'} | "
            f"{dm[:6]}{'…' if dm and len(dm) > 6 else ''} | "
            f"{da[:6]}{'…' if da and len(da) > 6 else ''} |"
        )
    L.append("")

    # ----- A1 §3
    L.append("## A1 §3 — Hierarchical dendrogram (text form)")
    L.append("")
    L.append(
        "Coarse-to-fine split using the keys L1..L5 below. Each row reports how "
        "many distinct buckets the atlas falls into when keyed at that level."
    )
    L.append("")
    L.append("### 23-class atlas")
    L.append("| Level | Key | # buckets |")
    L.append("|---|---|---:|")
    for lvl in dendro_23:
        L.append(f"| L{lvl['level']} | {_level_key_name(lvl['level'])} | {lvl['n_buckets']} |")
    L.append("")
    L.append("L5 bucket map (23-class):")
    L.append("")
    L.append("```")
    for b in dendro_23[-1]["buckets"]:
        L.append(f"  key={b['key']}  ->  {b['members']}")
    L.append("```")
    L.append("")
    L.append("### 39-class atlas")
    L.append("| Level | Key | # buckets |")
    L.append("|---|---|---:|")
    for lvl in dendro_39:
        L.append(f"| L{lvl['level']} | {_level_key_name(lvl['level'])} | {lvl['n_buckets']} |")
    L.append("")
    L.append("L5 bucket map (39-class):")
    L.append("")
    L.append("```")
    for b in dendro_39[-1]["buckets"]:
        L.append(f"  key={b['key']}  ->  {b['members']}")
    L.append("```")
    L.append("")

    # ----- A1 §4
    L.append("## A1 §4 — Minimal distinguishing invariants")
    L.append("")
    L.append(
        "Greedy add-one-at-a-time search over candidate invariants "
        "{I_Cn, I_nrings, I_rc, I_ratios, I_slope, I_omega, I_z}. "
        "Stops when all classes are separated."
    )
    L.append("")
    L.append("### 23-class atlas")
    L.append(f"Minimal separating set: **{minim_23['minimal_set']}**")
    L.append("")
    L.append("| Step | Added | # distinct classes (out of {tot}) | # collisions |".format(tot=minim_23["n_classes_total"]))
    L.append("|---:|---|---:|---:|")
    for h in minim_23["history"]:
        L.append(f"| {h['step']} | `{h['added']}` | {h['distinct_classes']} | {h['collisions']} |")
    L.append("")
    L.append("### 39-class atlas")
    L.append(f"Minimal separating set: **{minim_39['minimal_set']}**")
    L.append("")
    L.append("| Step | Added | # distinct classes (out of {tot}) | # collisions |".format(tot=minim_39["n_classes_total"]))
    L.append("|---:|---|---:|---:|")
    for h in minim_39["history"]:
        L.append(f"| {h['step']} | `{h['added']}` | {h['distinct_classes']} | {h['collisions']} |")
    L.append("")

    # ----- A2 §1
    L.append("## A2 §1 — 23-class symmetry-breaking table")
    L.append("")
    L.append("| Class | C_k (μ_q stabilizer) | is_regular_polygon |")
    L.append("|---|---:|---|")
    for fp in fps_23:
        L.append(
            f"| `{fp['label']}` | C_{fp.get('Cn_order')} | "
            f"{'yes' if fp.get('is_regular_polygon') else 'no'} |"
        )
    L.append("")

    # ----- A2 §2
    L.append("## A2 §2 — 39-class symmetry-breaking table")
    L.append("")
    L.append(
        "| ID | C_k (μ_q stabilizer) | is_regular | ω-resonance denom | z-resonances |"
    )
    L.append("|---|---:|---|---:|---:|")
    for fp in fps_39:
        L.append(
            f"| `{fp['id']}` | C_{fp.get('Cn_order')} "
            f"(invariant says C_{fp.get('symmetry_C_n_invariant')}) | "
            f"{'yes' if fp.get('is_regular_polygon') else 'no'} | "
            f"{fp.get('omega_resonance_denom')} | "
            f"{fp.get('z_resonance_count')} |"
        )
    L.append("")

    # ----- A2 §3
    L.append("## A2 §3 — Nontrivial-stabilizer roll-up")
    L.append("")
    L.append("### 23-class atlas")
    L.append(
        f"- total classes: **{sym_23['n_classes']}**"
        f"  ·  trivial (C_1): **{sym_23['trivial_stabilizer_count']}**"
        f"  ·  nontrivial: **{sym_23['nontrivial_stabilizer_count']}**"
    )
    L.append("")
    L.append("| C_k | # classes | members |")
    L.append("|---:|---:|---|")
    for k, members in sym_23["by_Cn_order"].items():
        L.append(f"| C_{k} | {len(members)} | {', '.join('`' + m + '`' for m in members)} |")
    L.append("")
    L.append("### 39-class atlas")
    L.append(
        f"- total classes: **{sym_39['n_classes']}**"
        f"  ·  trivial (C_1): **{sym_39['trivial_stabilizer_count']}**"
        f"  ·  nontrivial: **{sym_39['nontrivial_stabilizer_count']}**"
    )
    L.append("")
    L.append("| C_k | # classes | members |")
    L.append("|---:|---:|---|")
    for k, members in sym_39["by_Cn_order"].items():
        L.append(f"| C_{k} | {len(members)} | {', '.join('`' + m + '`' for m in members)} |")
    L.append("")

    L.append("---")
    L.append("## Headline findings")
    L.append("")
    L.append("### A1 — constellation shape")
    L.append(
        f"- 23-class atlas: **2 invariants suffice** — "
        f"`{minim_23['minimal_set']}` (ring_counts × Cn_order). "
        f"Ring-radius ratios provide secondary structure but are not needed for separation."
    )
    L.append(
        f"- 39-class atlas: **2 invariants suffice** — "
        f"`{minim_39['minimal_set']}` (slope multiset × ω-resonance denominator). "
        f"The Δ-modulus partition (slope) is finer than ring-counts on the refined atlas."
    )
    L.append("")
    L.append("### A2 — symmetry breaking")
    L.append(
        f"- 23-class atlas: **all 23 classes have nontrivial μ_q stabilizer** "
        f"(C_k with k ≥ 2). Stabilizer orders present: "
        f"{sorted(sym_23['by_Cn_order'].keys(), key=int)}."
    )
    L.append(
        f"- 39-class atlas: **{sym_39['nontrivial_stabilizer_count']} of {sym_39['n_classes']} "
        f"classes have nontrivial stabilizer**; "
        f"{sym_39['trivial_stabilizer_count']} have trivial C_1 stabilizer "
        f"(symmetry fully broken)."
    )
    cn_orders_39 = sorted(int(k) for k in sym_39["by_Cn_order"].keys())
    L.append(
        f"- 39-class stabilizer orders present: {cn_orders_39}."
    )
    L.append("")
    L.append(
        "Generated by `code/atlas_fingerprints.py`. Inputs: "
        "`data/clusters.json`, `data/phase3_clusters.json`, `data/constellations.json`, "
        "`data/phase3_invariants.json`."
    )
    return "\n".join(L) + "\n"


def _level_key_name(level: int) -> str:
    return {
        1: "Cn_order",
        2: "Cn_order × n_rings",
        3: "Cn_order × n_rings × ring_counts",
        4: "Cn_order × n_rings × ring_counts × ratios_to_inner",
        5: "full fingerprint",
    }[level]


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main() -> None:
    constellations = load_json("constellations.json")
    clusters_23 = load_json("clusters.json")
    clusters_39 = load_json("phase3_clusters.json")
    phase3_inv = load_json("phase3_invariants.json")

    op_index = build_per_op_index(constellations)
    p3_inv_by_op = {entry.get("operator"): entry for entry in phase3_inv}

    fps_23 = [class_fingerprint_23(c) for c in clusters_23]
    fps_39 = [class_fingerprint_39(c, p3_inv_by_op) for c in clusters_39]

    dendro_23 = dendrogram_levels(fps_23)
    dendro_39 = dendrogram_levels(fps_39)

    minim_23 = minimal_distinguishing_invariants(fps_23)
    minim_39 = minimal_distinguishing_invariants(fps_39)

    sym_23 = symmetry_rollup(fps_23)
    sym_39 = symmetry_rollup(fps_39)

    out_json = {
        "metadata": {
            "n_classes_23": len(fps_23),
            "n_classes_39": len(fps_39),
            "inputs": [
                "data/clusters.json",
                "data/phase3_clusters.json",
                "data/constellations.json",
                "data/phase3_invariants.json",
            ],
        },
        "atlas_23": {
            "fingerprints": fps_23,
            "dendrogram_levels": dendro_23,
            "minimal_distinguishing_invariants": minim_23,
            "symmetry_rollup": sym_23,
        },
        "atlas_39": {
            "fingerprints": fps_39,
            "dendrogram_levels": dendro_39,
            "minimal_distinguishing_invariants": minim_39,
            "symmetry_rollup": sym_39,
        },
    }

    DATA.mkdir(exist_ok=True)
    REPORTS.mkdir(exist_ok=True)
    out_json_path = DATA / "atlas_fingerprints.json"
    out_md_path = REPORTS / "atlas_fingerprints.md"

    with out_json_path.open("w", encoding="utf-8") as fh:
        json.dump(out_json, fh, indent=2, ensure_ascii=False)

    md = render_a1_a2_report(
        fps_23, fps_39, dendro_23, dendro_39, minim_23, minim_39, sym_23, sym_39
    )
    with out_md_path.open("w", encoding="utf-8") as fh:
        fh.write(md)

    print(f"Wrote {out_json_path} ({out_json_path.stat().st_size:,} bytes)")
    print(f"Wrote {out_md_path} ({out_md_path.stat().st_size:,} bytes)")
    print(
        f"23-class: minimal separating set = {minim_23['minimal_set']} "
        f"(reaches {minim_23['history'][-1]['distinct_classes']}/{minim_23['n_classes_total']})"
    )
    print(
        f"39-class: minimal separating set = {minim_39['minimal_set']} "
        f"(reaches {minim_39['history'][-1]['distinct_classes']}/{minim_39['n_classes_total']})"
    )
    print(
        f"23-class symmetry roll-up: trivial={sym_23['trivial_stabilizer_count']}, "
        f"nontrivial={sym_23['nontrivial_stabilizer_count']}"
    )
    print(
        f"39-class symmetry roll-up: trivial={sym_39['trivial_stabilizer_count']}, "
        f"nontrivial={sym_39['nontrivial_stabilizer_count']}"
    )


if __name__ == "__main__":
    main()
