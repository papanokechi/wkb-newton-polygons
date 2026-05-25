# `code/` — Plotting and utility scripts

Auxiliary scripts (not pipeline-critical) for rendering figures and
post-processing the JSON dataset.

## Files

| File                   | Bytes | Purpose                              |
|------------------------|------:|--------------------------------------|
| `plot_constellations.py`| 2,405 | Renders `figures/constellations.png` from `data/constellations.json`. |

## Usage

```bash
# From the repository root:
python code/plot_constellations.py \
    --input data/constellations.json \
    --output figures/constellations.png
```

Default behaviour: reads `data/constellations.json`, plots the 23
representative constellations in a 5×5 grid plus the four degeneracy
strata, and writes a 141 KB PNG to `figures/constellations.png`.

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
