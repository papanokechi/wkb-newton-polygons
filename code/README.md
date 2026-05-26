# `code/` — Plotting and utility scripts

Auxiliary scripts (not pipeline-critical) for rendering figures and
post-processing the JSON dataset.

## Files

| File                   | Bytes | Purpose                              |
|------------------------|------:|--------------------------------------|
| `plot_constellations.py`| 2,405 | Renders `figures/constellations.png` from `data/constellations.json`. |
| `ray_equivalence.py`   | varies | Anti-Stokes ray-spacing equivalence partition of the atlas. Computes per-entry `{ arg(Δ_ij) mod π/p }` fingerprints (raw and gap-invariant) and groups entries by identical fingerprints. Writes `data/phase4_ray_equivalence.json` and `reports/phase4_ray_equivalence_report.md`. |
| `extract_slope_invariants.py` | varies | Extracts the 23-class and 39-class atlas slope multisets, Δ-modulus / Δ-argument partitions, μ_q stabilizer (`sym C_k`), ω-resonance flags, and z-resonance counts. Writes `data/slope_invariants.json` and `reports/slope_invariants_report.md`. |
| `atlas_fingerprints.py` | varies | Series-A fingerprint analyzer: per-class ring-radius ratios, angular-gap multisets, hierarchical dendrogram, minimal distinguishing invariants (A1), and μ_q stabilizer / ω-resonance / z-resonance roll-up (A2). Writes `data/atlas_fingerprints.json` and `reports/atlas_fingerprints.md`. |

## Usage

```bash
# From the repository root:
python code/plot_constellations.py \
    --input data/constellations.json \
    --output figures/constellations.png

python code/ray_equivalence.py \
    --input  data/phase4_stokes.json \
    --output data/phase4_ray_equivalence.json \
    --report reports/phase4_ray_equivalence_report.md

python code/extract_slope_invariants.py
# Reads data/clusters.json + data/phase3_clusters.json + data/phase3_invariants.json
# Writes data/slope_invariants.json + reports/slope_invariants_report.md

python code/atlas_fingerprints.py
# Reads data/clusters.json + data/phase3_clusters.json
#       + data/constellations.json + data/phase3_invariants.json
# Writes data/atlas_fingerprints.json + reports/atlas_fingerprints.md
```

Default behaviour for `plot_constellations.py`: reads
`data/constellations.json`, plots the 23 representative constellations
in a 5×5 grid plus the four degeneracy strata, and writes a 141 KB PNG
to `figures/constellations.png`.

Default behaviour for `ray_equivalence.py`: reads
`data/phase4_stokes.json` (48 atlas entries), computes for each entry
the multiset `{ arg(Δ_ij) mod π/p }` (quantized to 10⁻⁶ rad) and its
rotation-invariant cyclic-gap canonicalization, and writes a
machine-readable JSON partition plus a Markdown report.

## Dependencies

```
python >= 3.10
numpy
matplotlib
```

Install via:

```bash
pip install numpy matplotlib
```

## Determinism

The script uses no rng; all geometry is derived from the JSON data
directly. Output is byte-deterministic.

## Style

* PEP 8, ~100-column lines.
* Pure functions; no global state.
* JSON I/O uses `json.load` / `json.dump` with `indent=2, sort_keys=True`.

## License

[MIT](../LICENSE-CODE).
