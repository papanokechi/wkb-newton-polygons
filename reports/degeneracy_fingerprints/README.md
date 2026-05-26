# `degeneracy_fingerprints/` — local invariants of the four Phase-1 strata

Addresses Phase-3 gap **G15** (codimension per degeneracy stratum) for the
four Phase-1 stress-test degeneracies of the WKB-Newton polygon classification.

## Files

- `compute_fingerprints.py` — main analysis script (SymPy + NumPy).
  Computes the Vieta Jacobian on c-roots, the stratum-defining Jacobian in
  β-space, the Δ-multiset statistics, and the 20-d fingerprint vector.
- `fingerprints.json` — structured per-stratum records.
- `degeneracy_fingerprints.md` — human-readable analysis and table.
- `verify.py` — quick sanity-check (asserts pairwise distinctness + Phase-1
  cross-checks).

## Reproduce

```
python compute_fingerprints.py     # regenerates fingerprints.json + prints table
python verify.py                   # asserts sanity invariants
```

## Key result

Three coordinates of the fingerprint vector suffice to separate all four
Phase-1 strata:

| coord | zeroroot | doubleroot | equalmod | accidental_sym |
|---|---|---|---|---|
| `codim_C_in_beta`      | 1 | 1 | 0 | 2 |
| `vieta_swap_kernel_dim`| 1 | 3 | 0 | 0 |
| `inc_C_d_sparse`       | 0 | 0 | 0 | 1 |

Rigidity classes:
- **very rigid** (codim$_\mathbb C \ge 2$): `accidental_sym`
- **rigid codim 1**: `zeroroot`, `doubleroot`
- **real-only**: `equalmod`
