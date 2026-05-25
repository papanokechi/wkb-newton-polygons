"""Generate matplotlib scatter plots of representative constellations."""
import json
import math
import os
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(DIR, "constellations.json"), encoding="utf-8") as f:
    data = json.load(f)

# Pick 12 representative operators across the full structural map
chosen = [
    "ODE_s1o3_r1_simple",
    "ODE_s1o4_r2_simple",
    "ODE_s1o2_r3_simple",
    "ODE_s1o3_r3_double",
    "ODE_s1o3_r3_mixed",
    "ODE_s1o4_r3_generic_complex",
    "ODE_s1o3_r3_generic_complex",
    "ODE_s2o3_r3_generic_complex",
    "STRESS_equalmod",
    "STRESS_doubleroot",
    "STRESS_zeroroot",
    "STRESS_accidental_sym",
]
by_name = {d["name"]: d for d in data}

fig, axes = plt.subplots(3, 4, figsize=(15, 11))
axes = axes.flatten()

for ax, name in zip(axes, chosen):
    d = by_name[name]
    rings = d["rings"]
    xs, ys = [], []
    colors = []
    palette = plt.cm.tab10(np.linspace(0, 1, max(1, len(rings))))
    for i, ring in enumerate(rings):
        rho = ring["radius"]
        for a in ring["args"]:
            xs.append(rho * math.cos(a))
            ys.append(rho * math.sin(a))
            colors.append(palette[i])
    # unit circle reference
    th = np.linspace(0, 2 * math.pi, 200)
    ax.plot(np.cos(th), np.sin(th), color="lightgray", linewidth=0.8, linestyle=":")
    # axes
    ax.axhline(0, color="lightgray", linewidth=0.5)
    ax.axvline(0, color="lightgray", linewidth=0.5)
    ax.scatter(xs, ys, c=colors, s=40, edgecolors="black", linewidth=0.5, zorder=5)
    Rmax = max(r["radius"] for r in rings) if rings else 1.0
    pad = 0.25 * Rmax + 0.1
    ax.set_xlim(-Rmax - pad, Rmax + pad)
    ax.set_ylim(-Rmax - pad, Rmax + pad)
    ax.set_aspect("equal")
    title = name.replace("ODE_", "").replace("_", " ")
    rc = d["ring_counts"]
    reg_mark = " regular" if d.get("is_regular_polygon") else ""
    ax.set_title(f"{title}\nC_{d['Cn_order']}, rings={rc}{reg_mark}", fontsize=9)
    ax.tick_params(labelsize=7)

plt.suptitle(
    "WKB Exponent Constellations — Representative Classes + Stress Tests",
    fontsize=13,
)
plt.tight_layout(rect=[0, 0, 1, 0.97])
out = os.path.join(DIR, "constellations.png")
plt.savefig(out, dpi=110)
print(f"Saved {out}")
