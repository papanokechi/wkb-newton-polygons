"""Anti-Stokes ray-spacing equivalence partition of the atlas.

For each entry of ``data/phase4_stokes.json`` this script computes:

  * the **raw fingerprint** -- the sorted multiset

        F_raw(L) = ( arg(Delta_ij) mod pi/p  :  i < j ),

    quantized to ``--digits`` decimal places of radians; and

  * the **rotation-invariant fingerprint** -- the sorted multiset of
    cyclic gaps of ``F_raw`` on the circle of circumference ``pi/p``.

Two atlas entries are declared *ray-equivalent* iff they share the
same stratum index ``p`` and the same quantized fingerprint.  The
script emits both the raw partition (gauge-fixed by the recorded
chart) and the gap-invariant partition (which is invariant under
global rotation of the constellation).

This follows the determinacy statement of Theorem AT1
(``paper/paper.tex`` lines 1485-1517): the cover-ray multiset is
determined by ``{ arg Delta_ij mod pi/p : i < j }``.

Usage
-----
::

    python code/ray_equivalence.py \\
        --input  data/phase4_stokes.json \\
        --output data/phase4_ray_equivalence.json \\
        --report reports/phase4_ray_equivalence_report.md

Outputs are byte-deterministic given the same input file and the same
``--digits`` value.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def reduce_arg_mod(arg: float, modulus: float) -> float:
    """Reduce ``arg`` to the half-open interval ``[0, modulus)``."""
    v = math.fmod(arg, modulus)
    if v < 0.0:
        v += modulus
    if v >= modulus:
        v -= modulus
    return v


def raw_fingerprint(
    entry: dict[str, Any], digits: int
) -> tuple[tuple[float, ...], int]:
    """Multiset of ``arg(Delta_ij) mod pi/p`` for all non-degenerate pairs.

    Pairs with ``delta_zero == True`` (coincident constellation roots,
    Delta_ij = 0) contribute no cover-ray and are excluded; the number
    of such excluded pairs is returned alongside the fingerprint so the
    partition can preserve that degeneracy.
    """
    p = entry["p"]
    modulus = math.pi / p
    quant = 10 ** digits
    modulus_q = int(round(modulus * quant))
    values: list[int] = []
    skipped = 0
    for pair in entry["rays_per_pair"]:
        if pair.get("delta_zero", False):
            skipped += 1
            continue
        re, im = pair["delta"]
        if re == 0.0 and im == 0.0:
            # Defensive fallback: treat exact-zero delta as delta_zero
            # even if the flag is missing.
            skipped += 1
            continue
        a = math.atan2(im, re)
        v = reduce_arg_mod(a, modulus)
        # Quantize via integer rounding to make the multiset hashable
        # while folding floating-point noise.  Snap a value that landed
        # at the upper boundary back to zero.
        k = int(round(v * quant))
        if k == modulus_q:
            k = 0
        values.append(k)
    values.sort()
    return tuple(v / quant for v in values), skipped


def gap_fingerprint(
    raw: tuple[float, ...], modulus: float, digits: int
) -> tuple[float, ...]:
    """Rotation-invariant fingerprint: cyclic gaps of ``raw`` on the
    circle of circumference ``modulus``.

    The cyclic gap sequence is canonicalized to its lexicographically
    smallest rotation so that equivalent multisets compare equal
    regardless of the gauge.
    """
    if not raw:
        return ()
    quant = 10 ** digits
    sorted_vals = sorted(raw)
    gaps: list[int] = []
    n = len(sorted_vals)
    for i in range(n):
        nxt = sorted_vals[(i + 1) % n]
        cur = sorted_vals[i]
        if i + 1 == n:
            g = (nxt + modulus) - cur
        else:
            g = nxt - cur
        gaps.append(int(round(g * quant)))
    # Canonicalize: pick the lexicographically minimal cyclic rotation.
    best = min(tuple(gaps[i:] + gaps[:i]) for i in range(n))
    return tuple(v / quant for v in best)


def multiplicity_profile(raw: tuple[float, ...]) -> list[int]:
    """Sorted list of multiplicities; size = number of distinct values."""
    return sorted(Counter(raw).values(), reverse=True)


def build_partition(
    data: dict[str, dict[str, Any]], digits: int
) -> dict[str, Any]:
    """Return raw and gap-invariant ray-equivalence partitions."""
    per_entry: dict[str, dict[str, Any]] = {}
    raw_groups: dict[tuple[int, int, tuple[float, ...]], list[str]] = defaultdict(list)
    gap_groups: dict[tuple[int, int, tuple[float, ...]], list[str]] = defaultdict(list)

    for name, entry in data.items():
        p = entry["p"]
        modulus = math.pi / p
        raw, skipped = raw_fingerprint(entry, digits)
        gap = gap_fingerprint(raw, modulus, digits)
        per_entry[name] = {
            "p": p,
            "q": entry["q"],
            "N": entry["N"],
            "n_pairs": entry["n_pairs"],
            "delta_zero_pair_count": skipped,
            "modulus_pi_over_p": modulus,
            "fingerprint_size": len(raw),
            "distinct_count": len(set(raw)),
            "multiplicity_profile": multiplicity_profile(raw),
            "raw_fingerprint": list(raw),
            "gap_fingerprint": list(gap),
        }
        # Include `skipped` in the bucket key so two atlas entries with
        # the same active multiset but a different number of coincident
        # constellation roots are not silently merged.
        raw_groups[(p, skipped, raw)].append(name)
        gap_groups[(p, skipped, gap)].append(name)

    def emit(groups: dict[tuple[int, int, tuple[float, ...]], list[str]],
             kind: str) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        # Sort classes by (p, skipped, size desc, first member name).
        sorted_keys = sorted(
            groups.keys(),
            key=lambda k: (k[0], k[1], -len(groups[k]), sorted(groups[k])[0]),
        )
        for idx, key in enumerate(sorted_keys):
            p, skipped, sig = key
            members = sorted(groups[key])
            out.append({
                "class_id": f"R{kind}-p{p}-{idx:02d}",
                "p": p,
                "delta_zero_pair_count": skipped,
                "size": len(members),
                "members": members,
                "fingerprint_size": len(sig),
                "distinct_count": len(set(sig)),
                "multiplicity_profile": multiplicity_profile(sig),
                "fingerprint": list(sig),
            })
        return out

    raw_partition = emit(raw_groups, "raw")
    gap_partition = emit(gap_groups, "gap")

    return {
        "schema": "wkb-newton-polygons/ray-equivalence/v1",
        "definition": {
            "raw_fingerprint":
                "Sorted multiset { arg(Delta_ij) mod pi/p }, quantized to "
                f"10^-{digits} rad. Two atlas entries lie in the same raw "
                "class iff they share p and this multiset.",
            "gap_fingerprint":
                "Cyclic gap multiset of raw_fingerprint on the circle of "
                "circumference pi/p, canonicalized to its lex-min rotation. "
                "Two atlas entries lie in the same gap class iff they share "
                "p and this gap multiset; this partition is invariant "
                "under global rotation of the constellation.",
        },
        "quantization_digits": digits,
        "n_atlas_entries": len(data),
        "n_raw_classes": len(raw_partition),
        "n_gap_classes": len(gap_partition),
        "per_entry": per_entry,
        "raw_partition": raw_partition,
        "gap_partition": gap_partition,
    }


def render_report(part: dict[str, Any]) -> str:
    lines: list[str] = []
    add = lines.append
    add("# Anti-Stokes ray-spacing equivalence partition of the atlas")
    add("")
    add("This report is generated by `code/ray_equivalence.py` from "
        "`data/phase4_stokes.json`.")
    add("")
    add("## Definitions")
    add("")
    add("For each atlas entry with stratum index `p` we compute")
    add("")
    add("    F_raw(L) = sorted multiset { arg(Delta_ij) mod pi/p : i < j }")
    add("")
    add("(values in `[0, pi/p)`, quantized to "
        f"10^-{part['quantization_digits']} rad).  Two entries are")
    add("**raw-equivalent** iff they share `p` and `F_raw`.  The")
    add("**gap fingerprint** `F_gap` is the cyclic gap multiset of `F_raw`")
    add("on the circle of circumference `pi/p`, canonicalized to its")
    add("lexicographically minimal rotation; this is invariant under a")
    add("global rotation of the constellation.")
    add("")
    add("Reference: Theorem AT1, `paper/paper.tex` (lines 1485-1517).")
    add("")
    add("## Summary")
    add("")
    add(f"* Atlas entries: **{part['n_atlas_entries']}**")
    add(f"* Raw ray-equivalence classes: **{part['n_raw_classes']}**")
    add(f"* Gap ray-equivalence classes: **{part['n_gap_classes']}**")
    add("")
    add("Per-`p` breakdown of the raw partition:")
    add("")
    by_p: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for cls in part["raw_partition"]:
        by_p[cls["p"]].append(cls)
    add("| p | atlas entries | raw classes | gap classes |")
    add("|--:|--------------:|------------:|------------:|")
    gap_by_p: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for cls in part["gap_partition"]:
        gap_by_p[cls["p"]].append(cls)
    for p in sorted(by_p):
        n_entries = sum(c["size"] for c in by_p[p])
        n_raw = len(by_p[p])
        n_gap = len(gap_by_p[p])
        add(f"| {p} | {n_entries} | {n_raw} | {n_gap} |")
    add("")
    add("## Non-singleton ray-equivalence classes (raw)")
    add("")
    non_singleton_raw = [c for c in part["raw_partition"] if c["size"] > 1]
    if not non_singleton_raw:
        add("*(No non-singleton raw classes -- every atlas entry has a "
            "unique raw fingerprint within its `p`-stratum.)*")
    else:
        for cls in non_singleton_raw:
            add(f"### {cls['class_id']}  (p={cls['p']}, "
                f"size={cls['size']})")
            add("")
            add("Members:")
            for m in cls["members"]:
                add(f"  - `{m}`")
            add("")
            add(f"Fingerprint size = {cls['fingerprint_size']}, "
                f"distinct = {cls['distinct_count']}, "
                f"multiplicity profile = "
                f"{cls['multiplicity_profile']}.")
            add("")
    add("## Non-singleton ray-equivalence classes (gap-invariant)")
    add("")
    non_singleton_gap = [c for c in part["gap_partition"] if c["size"] > 1]
    if not non_singleton_gap:
        add("*(No non-singleton gap classes.)*")
    else:
        for cls in non_singleton_gap:
            add(f"### {cls['class_id']}  (p={cls['p']}, "
                f"size={cls['size']})")
            add("")
            add("Members:")
            for m in cls["members"]:
                add(f"  - `{m}`")
            add("")
            add(f"Fingerprint size = {cls['fingerprint_size']}, "
                f"distinct = {cls['distinct_count']}, "
                f"multiplicity profile = "
                f"{cls['multiplicity_profile']}.")
            add("")
    add("## Per-entry signature table")
    add("")
    add("| entry | p | q | N | |F| | distinct | multiplicity profile |")
    add("|-------|--:|--:|--:|---:|---------:|----------------------|")
    for name in sorted(part["per_entry"]):
        info = part["per_entry"][name]
        prof = ",".join(str(m) for m in info["multiplicity_profile"])
        add(f"| `{name}` | {info['p']} | {info['q']} | {info['N']} "
            f"| {info['fingerprint_size']} | {info['distinct_count']} "
            f"| `[{prof}]` |")
    add("")
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", default="data/phase4_stokes.json", type=Path)
    ap.add_argument("--output", default="data/phase4_ray_equivalence.json",
                    type=Path)
    ap.add_argument("--report",
                    default="reports/phase4_ray_equivalence_report.md",
                    type=Path)
    ap.add_argument("--digits", type=int, default=6,
                    help="Quantization precision in decimal places of rad "
                         "(default: 6).")
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    with args.input.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    part = build_partition(data, args.digits)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as fh:
        json.dump(part, fh, indent=2, sort_keys=True)
        fh.write("\n")
    report = render_report(part)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("w", encoding="utf-8") as fh:
        fh.write(report)
    print(f"Atlas entries: {part['n_atlas_entries']}")
    print(f"Raw ray-equivalence classes: {part['n_raw_classes']}")
    print(f"Gap ray-equivalence classes: {part['n_gap_classes']}")
    print(f"Wrote: {args.output}")
    print(f"Wrote: {args.report}")


if __name__ == "__main__":
    main()
