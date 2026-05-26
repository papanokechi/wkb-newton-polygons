"""Extract slope-based invariants across the WKB Newton-polygon atlas.

For each class (23-class base atlas and 39-class mu_q/mu_q' refinement) compute:
  - slope multiset (per-edge (p, q) pairs in lowest terms, aggregated across members)
  - gcd(p, q) structure (per-edge raw gcds, before reduction)
  - ramification depth (per-edge q / gcd(p, q); global = lcm across edges of one member)
Then cluster classes by their slope fingerprint and report collisions.

Outputs:
  ../data/slope_invariants.json     -- full structured artifact
  ../reports/slope_invariants_report.md  -- human-readable summary
"""
from __future__ import annotations

import json
import math
import os
from collections import Counter, defaultdict
from fractions import Fraction
from functools import reduce
from typing import Any

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
REPORTS = os.path.normpath(os.path.join(HERE, "..", "reports"))


def load(name: str) -> Any:
    with open(os.path.join(DATA, name), encoding="utf-8") as fh:
        return json.load(fh)


def lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b) if a and b else (a or b)


def parse_slope_string(s: str) -> tuple[int, int] | None:
    """Parse a slope literal like '1/2', '-1/3', '2/5'. Returns (p, q) with q > 0."""
    try:
        f = Fraction(s)
    except (ValueError, ZeroDivisionError):
        return None
    return (f.numerator, f.denominator)


# ---------------------------------------------------------------------------
# 1. Build unified per-operator info
# ---------------------------------------------------------------------------

def build_operator_info() -> dict[str, dict[str, Any]]:
    ops1 = load("operators.json")          # 89 entries; slope as 'p/q' string
    ops3 = load("phase3_operators.json")   # 48 entries; sometimes structured
    inv3 = load("phase3_invariants.json")  # 48 entries; per_edge p, q, r

    info: dict[str, dict[str, Any]] = {}

    # Phase 1/2 operators: single-edge, slope is a 'p/q' string
    for op in ops1:
        name = op["name"]
        slope = parse_slope_string(op.get("slope", ""))
        edges: list[dict[str, int]] = []
        if slope is not None:
            p, q = slope
            edges.append({"p": p, "q": q, "r": op.get("rank", 1)})
        info[name] = {
            "name": name,
            "family": "scalar",
            "eqtype": op.get("eqtype"),
            "rank": op.get("rank"),
            "valuation": op.get("valuation"),
            "n_edges": len(edges),
            "edges": edges,
            "source": "operators.json",
        }

    # Phase 3 invariants: definitive per-edge data; overrides single-edge defaults
    by_inv = {entry["operator"]: entry for entry in inv3}
    for name, entry in by_inv.items():
        edges = [
            {"p": int(e["p"]), "q": int(e["q"]), "r": int(e.get("r", 1))}
            for e in entry.get("per_edge", [])
        ]
        rec = info.setdefault(
            name,
            {
                "name": name,
                "family": entry.get("family", "scalar"),
                "eqtype": entry.get("eqtype"),
                "rank": None,
                "valuation": None,
                "n_edges": 0,
                "edges": [],
                "source": "phase3_invariants.json",
            },
        )
        rec["family"] = entry.get("family", rec.get("family", "scalar"))
        rec["eqtype"] = entry.get("eqtype", rec.get("eqtype"))
        rec["n_edges"] = int(entry.get("n_edges", len(edges)))
        rec["edges"] = edges  # authoritative
        rec["source"] = (rec.get("source", "") + "+phase3_invariants").strip("+")

    # Phase 3 operators metadata: family/eqtype hints where invariants are absent
    by_op3 = {op["name"]: op for op in ops3}
    for name, op in by_op3.items():
        rec = info.setdefault(
            name,
            {
                "name": name,
                "family": op.get("family", "scalar"),
                "eqtype": op.get("eqtype"),
                "rank": op.get("rank"),
                "valuation": op.get("valuation"),
                "n_edges": 0,
                "edges": [],
                "source": "phase3_operators.json",
            },
        )
        if not rec.get("family"):
            rec["family"] = op.get("family", "scalar")
        if not rec.get("eqtype"):
            rec["eqtype"] = op.get("eqtype")

    return info


# ---------------------------------------------------------------------------
# 2. Per-operator slope invariants
# ---------------------------------------------------------------------------

def per_operator_invariants(rec: dict[str, Any]) -> dict[str, Any]:
    edges = rec["edges"]
    per_edge: list[dict[str, int]] = []
    for e in edges:
        p, q = int(e["p"]), int(e["q"])
        g = math.gcd(abs(p), abs(q)) or 1
        p_red, q_red = p // g, q // g
        # canonical sign: denominator positive
        if q_red < 0:
            p_red, q_red = -p_red, -q_red
        ram = q_red  # ramification index of this slope
        per_edge.append(
            {
                "p": p,
                "q": q,
                "r": int(e.get("r", 1)),
                "gcd": g,
                "p_reduced": p_red,
                "q_reduced": q_red,
                "ramification": ram,
            }
        )

    ram_indices = [e["ramification"] for e in per_edge]
    global_ram = reduce(lcm, ram_indices, 1) if ram_indices else 0
    return {
        "name": rec["name"],
        "family": rec.get("family", "scalar"),
        "eqtype": rec.get("eqtype"),
        "n_edges": rec.get("n_edges", len(edges)),
        "per_edge": per_edge,
        "slope_multiset": sorted(
            (e["p_reduced"], e["q_reduced"]) for e in per_edge
        ),
        "gcd_multiset": sorted(e["gcd"] for e in per_edge),
        "ramification_multiset": sorted(ram_indices),
        "ramification_depth_global": global_ram,
    }


# ---------------------------------------------------------------------------
# 3. Per-class aggregation
# ---------------------------------------------------------------------------

def fmt_slope(p: int, q: int) -> str:
    return f"{p}/{q}"


def aggregate_class(cls: dict[str, Any], op_inv: dict[str, dict[str, Any]],
                    label_key: str = "label") -> dict[str, Any]:
    members = cls.get("members", [])
    member_records = [op_inv[m] for m in members if m in op_inv]
    missing = [m for m in members if m not in op_inv]

    # Aggregate multisets across all edges of all members
    slope_counter: Counter[tuple[int, int]] = Counter()
    gcd_counter: Counter[int] = Counter()
    ram_per_edge_counter: Counter[int] = Counter()
    ram_global_counter: Counter[int] = Counter()
    n_edges_counter: Counter[int] = Counter()
    eqtype_counter: Counter[str] = Counter()

    for r in member_records:
        for s in r["slope_multiset"]:
            slope_counter[tuple(s)] += 1
        for g in r["gcd_multiset"]:
            gcd_counter[g] += 1
        for ri in r["ramification_multiset"]:
            ram_per_edge_counter[ri] += 1
        ram_global_counter[r["ramification_depth_global"]] += 1
        n_edges_counter[r["n_edges"]] += 1
        if r.get("eqtype"):
            eqtype_counter[r["eqtype"]] += 1

    # Class-level slope fingerprint: the aggregated slope multiset across all
    # members, together with the n_edges signature and the multiset of global
    # ramification depths. Two classes "collide" iff they share this tuple.
    slope_ms = tuple(sorted(
        (p, q, c) for (p, q), c in slope_counter.items()
    ))
    n_edges_ms = tuple(sorted(n_edges_counter.items()))
    ram_global_ms = tuple(sorted(ram_global_counter.items()))
    ram_per_edge_ms = tuple(sorted(ram_per_edge_counter.items()))

    fingerprint = {
        "slope_multiset": [
            {"slope": fmt_slope(p, q), "p": p, "q": q, "count": c}
            for (p, q, c) in slope_ms
        ],
        "n_edges_multiset": [
            {"n_edges": k, "count": c} for (k, c) in n_edges_ms
        ],
        "ramification_depth_multiset": [
            {"depth": d, "count": c} for (d, c) in ram_global_ms
        ],
        "ramification_per_edge_multiset": [
            {"ramification": r, "count": c} for (r, c) in ram_per_edge_ms
        ],
    }
    fingerprint_tuple = (slope_ms, n_edges_ms, ram_global_ms)

    return {
        "class_id": cls.get("id"),
        "label": cls.get(label_key) or cls.get("description"),
        "description": cls.get("description"),
        "n_members": cls.get("n_members", len(members)),
        "members": members,
        "missing_members": missing,
        "slope_multiset": [
            {"slope": fmt_slope(p, q), "p": p, "q": q, "count": c}
            for (p, q), c in sorted(slope_counter.items())
        ],
        "gcd_structure": [
            {"gcd": g, "count": c} for g, c in sorted(gcd_counter.items())
        ],
        "ramification_per_edge_distribution": [
            {"ramification": r, "count": c}
            for r, c in sorted(ram_per_edge_counter.items())
        ],
        "ramification_depth_distribution": [
            {"depth": d, "count": c}
            for d, c in sorted(ram_global_counter.items())
        ],
        "n_edges_distribution": [
            {"n_edges": k, "count": c} for k, c in sorted(n_edges_counter.items())
        ],
        "eqtype_distribution": dict(eqtype_counter),
        "slope_fingerprint": fingerprint,
        "_fingerprint_key": fingerprint_tuple,
    }


# ---------------------------------------------------------------------------
# 4. Cluster classes by fingerprint
# ---------------------------------------------------------------------------

def cluster_by_fingerprint(class_records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    buckets: dict[tuple, list[dict[str, Any]]] = defaultdict(list)
    for cr in class_records:
        buckets[cr["_fingerprint_key"]].append(cr)

    out: list[dict[str, Any]] = []
    for key, members in sorted(buckets.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        slope_ms, n_edges_ms, ram_global_ms = key
        out.append(
            {
                "fingerprint": {
                    "slopes_pretty": [
                        f"{fmt_slope(p, q)}×{c}" for (p, q, c) in slope_ms
                    ],
                    "slope_multiset": [
                        {"slope": fmt_slope(p, q), "p": p, "q": q, "count": c}
                        for (p, q, c) in slope_ms
                    ],
                    "n_edges_multiset": [
                        {"n_edges": k, "count": c} for (k, c) in n_edges_ms
                    ],
                    "ramification_depth_multiset": [
                        {"depth": d, "count": c} for (d, c) in ram_global_ms
                    ],
                },
                "n_classes": len(members),
                "class_ids": [m.get("class_id") for m in members],
                "labels": [m.get("label") for m in members],
            }
        )
    return out


# ---------------------------------------------------------------------------
# 5. Markdown report
# ---------------------------------------------------------------------------

def fmt_multiset(items: list[dict[str, Any]], key: str, value: str = "count") -> str:
    if not items:
        return "—"
    parts = [f"{it[key]}×{it[value]}" for it in items]
    return ", ".join(parts)


def render_markdown(base: list[dict[str, Any]], refined: list[dict[str, Any]],
                    cluster_base: list[dict[str, Any]],
                    cluster_refined: list[dict[str, Any]]) -> str:
    out: list[str] = []
    out.append("# Slope-based invariants across the WKB Newton-polygon atlas\n")
    out.append(
        "Per-class slope multisets, gcd(p,q) structure, and ramification depth\n"
        "for both the 23-class base atlas and the 39-class μ_q / μ_q′\n"
        "refinement. Classes are then clustered by their slope fingerprint.\n"
    )

    def emit_class_table(title: str, classes: list[dict[str, Any]]) -> None:
        out.append(f"\n## {title}\n")
        out.append(
            "| ID | Label | Slope multiset | gcd structure | "
            "Ramification depth (global) | n_edges |\n"
            "|---|---|---|---|---|---|"
        )
        for c in classes:
            slopes = fmt_multiset(c["slope_multiset"], "slope")
            gcds = fmt_multiset(c["gcd_structure"], "gcd")
            depth = fmt_multiset(c["ramification_depth_distribution"], "depth")
            nedge = fmt_multiset(c["n_edges_distribution"], "n_edges")
            label = (c.get("label") or "").replace("|", "\\|")
            out.append(
                f"| {c.get('class_id') or '—'} | {label} | "
                f"{slopes} | {gcds} | {depth} | {nedge} |"
            )

    emit_class_table("23-class base atlas (`clusters.json`)", base)
    emit_class_table("39-class refined atlas (`phase3_clusters.json`)", refined)

    def emit_fingerprint_clusters(title: str, buckets: list[dict[str, Any]]) -> None:
        out.append(f"\n## {title}\n")
        out.append("| # classes | Slope multiset | Global-depth multiset | "
                   "n_edges multiset | Class IDs / labels |\n"
                   "|---:|---|---|---|---|")
        for b in buckets:
            fp = b["fingerprint"]
            slopes = ", ".join(fp["slopes_pretty"]) or "—"
            depths = ", ".join(
                f"{d['depth']}×{d['count']}" for d in fp["ramification_depth_multiset"]
            ) or "—"
            nedges = ", ".join(
                f"{n['n_edges']}×{n['count']}" for n in fp["n_edges_multiset"]
            ) or "—"
            ids = [str(x) for x in b["class_ids"] if x is not None]
            labels = [str(x) for x in b["labels"] if x]
            tag = ", ".join(ids) if ids else "; ".join(l[:60] for l in labels)
            out.append(
                f"| {b['n_classes']} | {slopes} | {depths} | {nedges} | {tag} |"
            )

    emit_fingerprint_clusters(
        "Fingerprint clusters — 23-class atlas", cluster_base
    )
    emit_fingerprint_clusters(
        "Fingerprint clusters — 39-class refined atlas", cluster_refined
    )

    # Collision summary
    out.append("\n## Collision summary\n")
    base_collisions = [b for b in cluster_base if b["n_classes"] > 1]
    ref_collisions = [b for b in cluster_refined if b["n_classes"] > 1]
    out.append(
        f"* 23-class atlas: {len(base_collisions)} fingerprint buckets contain "
        f">1 class (i.e. distinct classes share the same slope fingerprint).\n"
        f"* 39-class atlas: {len(ref_collisions)} fingerprint buckets contain "
        f">1 class.\n"
    )
    if base_collisions:
        out.append("\n### Notable 23-class collisions\n")
        for b in base_collisions[:10]:
            fp = b["fingerprint"]
            slopes = ", ".join(fp["slopes_pretty"]) or "—"
            labels = "; ".join(str(x) for x in b["labels"] if x)
            depths = ", ".join(
                f"{d['depth']}×{d['count']}" for d in fp["ramification_depth_multiset"]
            )
            out.append(
                f"- slopes [{slopes}], depths [{depths}] "
                f"→ {b['n_classes']} classes: {labels}"
            )
    if ref_collisions:
        out.append("\n### Notable 39-class refined collisions\n")
        for b in ref_collisions[:10]:
            fp = b["fingerprint"]
            slopes = ", ".join(fp["slopes_pretty"]) or "—"
            ids = ", ".join(str(x) for x in b["class_ids"] if x is not None)
            depths = ", ".join(
                f"{d['depth']}×{d['count']}" for d in fp["ramification_depth_multiset"]
            )
            out.append(
                f"- slopes [{slopes}], depths [{depths}] "
                f"→ {b['n_classes']} classes: {ids}"
            )
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    op_info = build_operator_info()
    op_inv = {name: per_operator_invariants(rec) for name, rec in op_info.items()}

    cl_base = load("clusters.json")
    cl_ref = load("phase3_clusters.json")

    base_classes = [aggregate_class(c, op_inv, label_key="label") for c in cl_base]
    refined_classes = [aggregate_class(c, op_inv, label_key="description") for c in cl_ref]

    cluster_base = cluster_by_fingerprint(base_classes)
    cluster_refined = cluster_by_fingerprint(refined_classes)

    # Strip internal key from per-class records before serialising
    def strip(cs: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return [{k: v for k, v in c.items() if k != "_fingerprint_key"} for c in cs]

    base_clean = strip(base_classes)
    refined_clean = strip(refined_classes)

    artifact = {
        "schema_version": 1,
        "summary": {
            "n_operators": len(op_inv),
            "n_classes_base": len(base_classes),
            "n_classes_refined": len(refined_classes),
            "n_fingerprint_buckets_base": len(cluster_base),
            "n_fingerprint_buckets_refined": len(cluster_refined),
            "n_collision_buckets_base": sum(
                1 for b in cluster_base if b["n_classes"] > 1
            ),
            "n_collision_buckets_refined": sum(
                1 for b in cluster_refined if b["n_classes"] > 1
            ),
        },
        "operators": op_inv,
        "classes_base": base_clean,
        "classes_refined": refined_clean,
        "fingerprint_clusters_base": cluster_base,
        "fingerprint_clusters_refined": cluster_refined,
    }

    os.makedirs(DATA, exist_ok=True)
    os.makedirs(REPORTS, exist_ok=True)
    out_json = os.path.join(DATA, "slope_invariants.json")
    out_md = os.path.join(REPORTS, "slope_invariants_report.md")
    with open(out_json, "w", encoding="utf-8") as fh:
        json.dump(artifact, fh, indent=2, sort_keys=False)
        fh.write("\n")
    with open(out_md, "w", encoding="utf-8") as fh:
        fh.write(render_markdown(
            base_clean, refined_clean, cluster_base, cluster_refined
        ))

    # Console summary
    print(f"Operators processed       : {len(op_inv)}")
    print(f"Base classes              : {len(base_classes)}")
    print(f"Refined classes           : {len(refined_classes)}")
    print(f"Fingerprint buckets base  : {len(cluster_base)} "
          f"({artifact['summary']['n_collision_buckets_base']} collisions)")
    print(f"Fingerprint buckets ref.  : {len(cluster_refined)} "
          f"({artifact['summary']['n_collision_buckets_refined']} collisions)")
    print(f"Wrote: {out_json}")
    print(f"Wrote: {out_md}")


if __name__ == "__main__":
    main()
