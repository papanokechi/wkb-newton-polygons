# `fleets/` — Agent-pipeline scripts

The fleet scripts orchestrate the **Phase I–V** computational pipeline
that produced the atlas and proof skeletons.

Each fleet emulates a small team of agents (operator generator,
Newton-polygon engine, characteristic-polynomial engine, constellation
engine, clustering engine, conjecture engine, …) connected as a
chain.

## Files

| File         | Bytes  | Phase covered           | Key outputs                                 |
|--------------|-------:|-------------------------|---------------------------------------------|
| `fleet.py`   | 43,384 | **I + II** (zoo + base atlas) | `operators.json`, `newton.json`, `chi.json`, `constellations.json`, `clusters.json`, `counterexamples.json` |
| `fleet3.py`  | 69,822 | **III** (multi-edge, systems, nested) | `phase3_*.json`                            |
| `fleet4.py`  | 58,252 | **IV** (analytic lifting AT1–AT8)      | `phase4_*.json`                            |
| `fleet5.py`  | 61,932 | **V** (proof skeleton consolidation)   | `phase5_targets.json` + (text) `proofs.md`, `integration_map.md` |

## Running the full pipeline

From the repository root:

```bash
# Phase I + II : ~5 minutes on a laptop
python fleets/fleet.py

# Phase III : ~15 minutes
python fleets/fleet3.py

# Phase IV : ~45 minutes (anti-Stokes computation is the bottleneck)
python fleets/fleet4.py

# Phase V : ~2 minutes (the heavy lifting is symbolic)
python fleets/fleet5.py
```

Output files land in `data/` (with the canonical names listed in the
table above) and `reports/` (for the markdown summaries).

## Reproducibility

* Each fleet pins its rng seeds and parameter sweeps at the top of the
  script.
* Output is byte-deterministic given the same Python version (≥ 3.10).
* The `--verify-only` flag (where supported) re-derives the outputs and
  diffs them against the committed JSON, exiting nonzero on any
  mismatch.

## Dependencies

```
python >= 3.10
sympy
numpy
mpmath
```

Install via:

```bash
pip install sympy numpy mpmath
```

(No external services or network access required.)

## Architecture

Each fleet script defines a sequence of **agents** (Python classes
implementing a single `step(input)` method) connected by an
**orchestrator** (a generator that walks the dependency graph). The
orchestrator is responsible for:

* persisting intermediate state to JSON;
* logging each agent's run-time and output size;
* catching and reporting any deviation from the expected schema.

Agent definitions follow a consistent naming scheme:

```python
class OperatorGenerator:        # produces L(θ)
class NewtonPolygonEngine:      # produces Newton polygon and slope info
class CharacteristicPolyEngine: # produces χ(c) and χ_w(w)
class ConstellationEngine:      # produces Roots(χ)
class ClusteringEngine:         # groups into universality classes
class ConjectureEngine:         # emits classification statements
```

Later fleets (`fleet3.py`, `fleet4.py`, `fleet5.py`) extend this by
adding multi-edge handling, analytic-lift agents, and proof-skeleton
generators.

## Status

These scripts are **research code**: they are written for clarity and
auditability rather than maximum performance. They produce the exact
JSON files committed under `data/`. There is no test suite separate
from the verify-mode flag.

## License

[MIT](../LICENSE-CODE).
