# Series-A atlas fingerprints — Constellation shapes (A1) & Symmetry breaking (A2)

Per-class fingerprints across the 23-class base atlas (`data/clusters.json`) and the 39-class refined atlas (`data/phase3_clusters.json`). Constellation geometry for the 23-class atlas is taken from `data/constellations.json`; for the 39-class atlas it is reconstructed from `data/phase3_invariants.json` (field `full_constellation`). Symmetry / resonance data come from each cluster's `representative_invariants` block (the authoritative `symmetry_C_n` field is used as the μ_q stabilizer C_k order).

## Contents
- A1 §1: 23-class atlas — ring-radius ratios + angular-gap multisets
- A1 §2: 39-class atlas — ring-radius ratios + angular-gap multisets
- A1 §3: Hierarchical dendrogram (text form)
- A1 §4: Minimal distinguishing invariants
- A2 §1: 23-class symmetry-breaking table (μ_q stabilizer)
- A2 §2: 39-class symmetry-breaking table (μ_q stabilizer, ω-resonance, z-resonance)
- A2 §3: Nontrivial-stabilizer roll-up

## A1 §1 — 23-class atlas: constellation-shape fingerprints

| Class | slope | n_rings | ring_counts | radii_sorted | ratios_to_inner | spread max/min | per-ring gap multisets |
|---|---|---:|---|---|---|---:|---|
| `Class[Regular-12-gon]` | 1/4 | 1 | [12] | [1] | [1] | 1.0 | {0.5236, 0.5236, 0.5236, 0.5236, 0.5236, 0.5236, 0.5236, 0.5236, 0.5236, 0.5236, 0.5236, 0.5236} |
| `Class[Regular-9-gon]` | 1/3 | 1 | [9] | [1] | [1] | 1.0 | {0.6981, 0.6981, 0.6981, 0.6981, 0.6981, 0.6981, 0.6981, 0.6981, 0.6981} |
| `Class[Regular-8-gon]` | 1/4 | 1 | [8] | [1] | [1] | 1.0 | {0.7854, 0.7854, 0.7854, 0.7854, 0.7854, 0.7854, 0.7854, 0.7854} |
| `Class[Regular-6-gon]` | 1/2 | 1 | [6] | [1] | [1] | 1.0 | {1.0472, 1.0472, 1.0472, 1.0472, 1.0472, 1.0472} |
| `Class[Regular-4-gon]` | 1/2 | 1 | [4] | [1] | [1] | 1.0 | {1.5708, 1.5708, 1.5708, 1.5708} |
| `Class[C4, rings=[4, 4]]` | 1/4 | 2 | [4, 4] | [0.786151, 1.27202] | [1, 1.61803] | 1.618034 | {1.5708, 1.5708, 1.5708, 1.5708} ; {1.5708, 1.5708, 1.5708, 1.5708} |
| `Class[C4, rings=[4, 4, 4]]` | 1/4 | 3 | [4, 4, 4] | [0.650351, 1.11234, 1.38234] | [1, 1.71036, 2.12553] | 2.12553 | {1.5708, 1.5708, 1.5708, 1.5708} ; {1.5708, 1.5708, 1.5708, 1.5708} ; {1.5708, 1.5708, 1.5708, 1.5708} |
| `Class[C4, rings=[4, 8]]` | 1/4 | 2 | [4, 8] | [0.750749, 1.15412] | [1, 1.5373] | 1.537297 | {1.5708, 1.5708, 1.5708, 1.5708} ; {0.3569, 0.3569, 0.3569, 0.3569, 1.2139, 1.2139, 1.2139, 1.2139} |
| `Class[C4, rings=[8]]` | 1/4 | 1 | [8] | [1] | [1] | 1.0 | {0.5236, 0.5236, 0.5236, 0.5236, 1.0472, 1.0472, 1.0472, 1.0472} |
| `Class[C4, rings=[8, 4]]` | 1/4 | 2 | [8, 4] | [0.953343, 1.10028] | [1, 1.15412] | 1.154124 | {0.6426, 0.6426, 0.6426, 0.6426, 0.9282, 0.9282, 0.9282, 0.9282} ; {1.5708, 1.5708, 1.5708, 1.5708} |
| `Class[Regular-3-gon]` | 1/3 | 1 | [3] | [1] | [1] | 1.0 | {2.0944, 2.0944, 2.0944} |
| `Class[C3, rings=[3, 3]]` | 1/3 | 2 | [3, 3] | [0.725563, 1.37824] | [1, 1.89955] | 1.899548 | {2.0944, 2.0944, 2.0944} ; {2.0944, 2.0944, 2.0944} |
| `Class[C3, rings=[3, 3, 3]]` | 1/3 | 3 | [3, 3, 3] | [0.563461, 1.15252, 1.53988] | [1, 2.04543, 2.7329] | 2.732895 | {2.0944, 2.0944, 2.0944} ; {2.0944, 2.0944, 2.0944} ; {2.0944, 2.0944, 2.0944} |
| `Class[C3, rings=[3, 6]]` | 1/3 | 2 | [3, 6] | [0.682328, 1.21061] | [1, 1.77423] | 1.774232 | {2.0944, 2.0944, 2.0944} ; {0.4758, 0.4758, 0.4758, 1.6186, 1.6186, 1.6186} |
| `Class[C3, rings=[6]]` | 1/3 | 1 | [6] | [1] | [1] | 1.0 | {0.6981, 0.6981, 0.6981, 1.3963, 1.3963, 1.3963} |
| `Class[C3, rings=[6, 3]]` | 1/3 | 2 | [6, 3] | [0.938279, 1.13589] | [1, 1.21061] | 1.210608 | {0.8567, 0.8567, 0.8567, 1.2377, 1.2377, 1.2377} ; {2.0944, 2.0944, 2.0944} |
| `Class[Regular-2-gon]` | 1/2 | 1 | [2] | [1] | [1] | 1.0 | {3.1416, 3.1416} |
| `Class[C2, rings=[2, 2]]` | 1/2 | 2 | [2, 2] | [0.618034, 1.61803] | [1, 2.61803] | 2.618034 | {3.1416, 3.1416} ; {3.1416, 3.1416} |
| `Class[C2, rings=[2, 2, 2]]` | 1/2 | 3 | [2, 2, 2] | [0.422957, 1.2373, 1.91087] | [1, 2.92534, 4.51788] | 4.517876 | {3.1416, 3.1416} ; {3.1416, 3.1416} ; {3.1416, 3.1416} |
| `Class[C2, rings=[2, 4]]` | 1/2 | 2 | [2, 4] | [0.563624, 1.332] | [1, 2.36328] | 2.363282 | {3.1416, 3.1416} ; {0.7137, 0.7137, 2.4278, 2.4278} |
| `Class[C2, rings=[4]]` | 1/2 | 1 | [4] | [1] | [1] | 1.0 | {1.0472, 1.0472, 2.0944, 2.0944} |
| `Class[C2, rings=[4, 2]]` | 1/2 | 2 | [4, 2] | [0.908863, 1.21061] | [1, 1.332] | 1.332003 | {1.2851, 1.2851, 1.8565, 1.8565} ; {3.1416, 3.1416} |
| `Class[C2, rings=[6]]` | 1/2 | 1 | [6] | [1.41421] | [1] | 1.0 | {0.7854, 0.7854, 0.7854, 0.7854, 1.5708, 1.5708} |

## A1 §2 — 39-class refined atlas: constellation-shape fingerprints

*Note.* Zero-radius roots (c = 0, arising on multi-edge classes with a degenerate sub-edge) are not counted as a ring; their count appears in the `0-roots` column instead.

| ID | n_edges | n_rings | ring_counts | 0-roots | radii_sorted | ratios_to_inner | spread | Δ-mod | Δ-arg |
|---|---:|---:|---|---:|---|---|---:|---|---|
| `P3C00` | 1 | 2 | [5, 5] | 0 | [0.863664, 1.15786] | [1, 1.34064] | 1.340635 | [5, 5, 5, 5, 5, 5]… | [2, 2, 2, 2, 2, 2]… |
| `P3C01` | 1 | 1 | [4] | 0 | [1] | [1] | 1.0 | [2, 2, 2] | [2, 2, 1, 1] |
| `P3C02` | 1 | 2 | [5, 5] | 0 | [0.768441, 1.30134] | [1, 1.69348] | 1.693476 | [5, 5, 5, 5, 5, 5]… | [2, 2, 2, 2, 2, 2]… |
| `P3C03` | 1 | 3 | [3, 3, 3] | 0 | [1, 1.06266, 1.25992] | [1, 1.06266, 1.25992] | 1.259921 | [6, 6, 6, 3, 3, 3]… | [3, 3, 3, 3, 3, 3]… |
| `P3C04` | 1 | 1 | [8] | 0 | [1] | [1] | 1.0 | [8, 4, 4, 4, 4, 4] | [4, 4, 4, 2, 2, 2]… |
| `P3C05` | 1 | 1 | [10] | 0 | [1] | [1] | 1.0 | [10, 10, 10, 10, 5] | [5, 5, 5, 5, 5, 4]… |
| `P3C06` | 1 | 1 | [12] | 0 | [1] | [1] | 1.0 | [12, 12, 6, 6, 6, 6]… | [6, 6, 6, 6, 6, 4]… |
| `P3C07` | 1 | 1 | [2] | 0 | [1] | [1] | 1.0 | [1] | [1] |
| `P3C08` | 1 | 1 | [3] | 0 | [0.793701] | [1] | 1.0 | [3] | [1, 1, 1] |
| `P3C09` | 1 | 2 | [3, 3] | 0 | [0.783264, 1.27671] | [1, 1.62999] | 1.629987 | [3, 3, 3, 3, 3] | [1, 1, 1, 1, 1, 1]… |
| `P3C10` | 1 | 3 | [4, 4, 4] | 0 | [0.753464, 0.974394, 1.36208] | [1, 1.29322, 1.80776] | 1.807758 | [4, 4, 4, 4, 4, 4]… | [2, 2, 2, 2, 2, 2]… |
| `P3C11` | 1 | 1 | [5] | 0 | [1] | [1] | 1.0 | [5, 5] | [2, 2, 2, 2, 2] |
| `P3C12` | 1 | 3 | [5, 5, 5] | 0 | [0.771805, 0.918355, 1.41085] | [1, 1.18988, 1.82799] | 1.82799 | [5, 5, 5, 5, 5, 5]… | [2, 2, 2, 2, 2, 2]… |
| `P3C13` | 1 | 1 | [6] | 0 | [1] | [1] | 1.0 | [6, 3, 3, 3] | [3, 2, 2, 1, 1, 1]… |
| `P3C14` | 1 | 1 | [6] | 0 | [1] | [1] | 1.0 | [6, 6, 3] | [3, 3, 3, 2, 2, 2] |
| `P3C15` | 1 | 1 | [8] | 0 | [1] | [1] | 1.0 | [6, 6, 6, 6, 4] | [4, 4, 3, 3, 3, 2]… |
| `P3C16` | 1 | 2 | [6, 6] | 0 | [0.802926, 1.24544] | [1, 1.55113] | 1.551134 | [6, 6, 6, 6, 6, 6]… | [3, 3, 3, 3, 3, 2]… |
| `P3C17` | 1 | 3 | [6, 6, 6] | 0 | [0.805854, 0.931484, 1.3322] | [1, 1.1559, 1.65315] | 1.653147 | [6, 6, 6, 6, 6, 6]… | [3, 3, 3, 3, 3, 3]… |
| `P3C18` | 1 | 1 | [7] | 0 | [1] | [1] | 1.0 | [7, 7, 7] | [3, 3, 3, 3, 3, 3]… |
| `P3C19` | 1 | 2 | [7, 7] | 0 | [0.828501, 1.207] | [1, 1.45685] | 1.456846 | [7, 7, 7, 7, 7, 7]… | [3, 3, 3, 3, 3, 3]… |
| `P3C20` | 1 | 1 | [8] | 0 | [1] | [1] | 1.0 | [8, 4, 4, 4, 4, 4] | [4, 4, 4, 3, 2, 2]… |
| `P3C21` | 1 | 2 | [3, 6] | 0 | [1, 1.25992] | [1, 1.25992] | 1.259921 | [12, 12, 6, 3, 3] | [5, 5, 5, 2, 2, 2]… |
| `P3C22` | 1 | 1 | [12] | 0 | [1] | [1] | 1.0 | [12, 12, 12, 12, 12, 6] | [6, 6, 6, 6, 6, 5]… |
| `P3C23` | 1 | 1 | [14] | 0 | [1] | [1] | 1.0 | [14, 14, 14, 14, 14, 14]… | [7, 7, 7, 7, 7, 7]… |
| `P3C24` | 1 | 1 | [15] | 0 | [1] | [1] | 1.0 | [15, 15, 15, 15, 15, 15]… | [7, 7, 7, 7, 7, 7]… |
| `P3C25` | 1 | 1 | [18] | 0 | [1] | [1] | 1.0 | [18, 18, 18, 18, 18, 18]… | [9, 9, 9, 9, 8, 8]… |
| `P3C26` | 2 | 3 | [2, 3, 2] | 3 | [0.693205, 1.12246, 1.44257] | [1, 1.61923, 2.08102] | 2.081019 | [9, 6, 6, 3, 3, 2]… | [4, 4, 4, 3, 3, 3]… |
| `P3C27` | 2 | 3 | [2, 4, 2] | 4 | [0.693205, 1.09051, 1.44257] | [1, 1.57314, 2.08102] | 2.081019 | [16, 8, 8, 6, 4, 2]… | [6, 5, 5, 5, 5, 4]… |
| `P3C28` | 2 | 3 | [3, 2, 3] | 6 | [0.914724, 1, 1.2271] | [1, 1.09323, 1.3415] | 1.341504 | [18, 18, 15, 12, 3, 3]… | [15, 7, 7, 7, 6, 6]… |
| `P3C29` | 2 | 3 | [2, 5, 2] | 5 | [0.693205, 1.07177, 1.44257] | [1, 1.54611, 2.08102] | 2.081019 | [25, 10, 10, 10, 5, 5]… | [10, 6, 6, 5, 5, 5]… |
| `P3C30` | 2 | 3 | [5, 5, 5] | 5 | [0.863664, 1.07177, 1.15786] | [1, 1.24096, 1.34064] | 1.340635 | [25, 25, 25, 10, 5, 5]… | [10, 5, 5, 5, 5, 5]… |
| `P3C31` | 2 | 4 | [3, 4, 4, 3] | 8 | [0.783264, 0.935335, 1.1659, 1.27671] | [1, 1.19415, 1.48852, 1.62999] | 1.629987 | [32, 32, 28, 24, 24, 4]… | [28, 9, 9, 9, 9, 8]… |
| `P3C32` | 2 | 3 | [4, 6, 4] | 6 | [0.83259, 1.05946, 1.20107] | [1, 1.27249, 1.44257] | 1.442574 | [42, 24, 24, 15, 6, 4]… | [15, 9, 9, 8, 7, 7]… |
| `P3C33` | 3 | 1 | [9] | 11 | [1] | [1] | 1.0 | [99, 55, 6, 6, 6, 3]… | [55, 15, 13, 13, 11, 11]… |
| `P3C34` | 3 | 3 | [2, 8, 2] | 13 | [0.693205, 1, 1.44257] | [1, 1.44257, 2.08102] | 2.081019 | [106, 79, 26, 26, 7, 7]… | [78, 14, 14, 13, 13, 13]… |
| `P3C35` | 2 | 1 | [5] | 0 | [1] | [1] | 1.0 | [3, 2, 2, 2, 1] | [2, 1, 1, 1, 1, 1]… |
| `P3C36` | 2 | 3 | [3, 3, 3] | 0 | [0.783264, 1, 1.27671] | [1, 1.27671, 1.62999] | 1.629987 | [3, 3, 3, 3, 3, 3]… | [1, 1, 1, 1, 1, 1]… |
| `P3C37` | 3 | 1 | [9] | 0 | [1] | [1] | 1.0 | [6, 6, 6, 3, 3, 2]… | [4, 2, 2, 2, 2, 2]… |
| `P3C38` | 3 | 1 | [15] | 0 | [1] | [1] | 1.0 | [45, 45, 15] | [15, 12, 12, 12, 12, 12]… |

## A1 §3 — Hierarchical dendrogram (text form)

Coarse-to-fine split using the keys L1..L5 below. Each row reports how many distinct buckets the atlas falls into when keyed at that level.

### 23-class atlas
| Level | Key | # buckets |
|---|---|---:|
| L1 | Cn_order | 7 |
| L2 | Cn_order × n_rings | 13 |
| L3 | Cn_order × n_rings × ring_counts | 23 |
| L4 | Cn_order × n_rings × ring_counts × ratios_to_inner | 23 |
| L5 | full fingerprint | 23 |

L5 bucket map (23-class):

```
  key=[1, (2,), (1.0,), 2]  ->  ['Class[Regular-2-gon]']
  key=[1, (3,), (1.0,), 3]  ->  ['Class[Regular-3-gon]']
  key=[1, (4,), (1.0,), 2]  ->  ['Class[C2, rings=[4]]']
  key=[1, (4,), (1.0,), 4]  ->  ['Class[Regular-4-gon]']
  key=[1, (6,), (1.0,), 2]  ->  ['Class[C2, rings=[6]]']
  key=[1, (6,), (1.0,), 3]  ->  ['Class[C3, rings=[6]]']
  key=[1, (6,), (1.0,), 6]  ->  ['Class[Regular-6-gon]']
  key=[1, (8,), (1.0,), 4]  ->  ['Class[C4, rings=[8]]']
  key=[1, (8,), (1.0,), 8]  ->  ['Class[Regular-8-gon]']
  key=[1, (9,), (1.0,), 9]  ->  ['Class[Regular-9-gon]']
  key=[1, (12,), (1.0,), 12]  ->  ['Class[Regular-12-gon]']
  key=[2, (2, 2), (1.0, 2.618034), 2]  ->  ['Class[C2, rings=[2, 2]]']
  key=[2, (2, 4), (1.0, 2.363282), 2]  ->  ['Class[C2, rings=[2, 4]]']
  key=[2, (3, 3), (1.0, 1.899548), 3]  ->  ['Class[C3, rings=[3, 3]]']
  key=[2, (3, 6), (1.0, 1.774232), 3]  ->  ['Class[C3, rings=[3, 6]]']
  key=[2, (4, 2), (1.0, 1.332003), 2]  ->  ['Class[C2, rings=[4, 2]]']
  key=[2, (4, 4), (1.0, 1.618034), 4]  ->  ['Class[C4, rings=[4, 4]]']
  key=[2, (4, 8), (1.0, 1.537297), 4]  ->  ['Class[C4, rings=[4, 8]]']
  key=[2, (6, 3), (1.0, 1.210608), 3]  ->  ['Class[C3, rings=[6, 3]]']
  key=[2, (8, 4), (1.0, 1.154124), 4]  ->  ['Class[C4, rings=[8, 4]]']
  key=[3, (2, 2, 2), (1.0, 2.925344, 4.517876), 2]  ->  ['Class[C2, rings=[2, 2, 2]]']
  key=[3, (3, 3, 3), (1.0, 2.04543, 2.732895), 3]  ->  ['Class[C3, rings=[3, 3, 3]]']
  key=[3, (4, 4, 4), (1.0, 1.710364, 2.12553), 4]  ->  ['Class[C4, rings=[4, 4, 4]]']
```

### 39-class atlas
| Level | Key | # buckets |
|---|---|---:|
| L1 | Cn_order | 12 |
| L2 | Cn_order × n_rings | 21 |
| L3 | Cn_order × n_rings × ring_counts | 34 |
| L4 | Cn_order × n_rings × ring_counts × ratios_to_inner | 36 |
| L5 | full fingerprint | 36 |

L5 bucket map (39-class):

```
  key=[1, (2,), (1.0,), 2]  ->  ['P3C07']
  key=[1, (3,), (1.0,), 1]  ->  ['P3C08']
  key=[1, (4,), (1.0,), 2]  ->  ['P3C01']
  key=[1, (5,), (1.0,), 1]  ->  ['P3C11', 'P3C35']
  key=[1, (6,), (1.0,), 3]  ->  ['P3C13']
  key=[1, (6,), (1.0,), 6]  ->  ['P3C14']
  key=[1, (7,), (1.0,), 1]  ->  ['P3C18']
  key=[1, (8,), (1.0,), 2]  ->  ['P3C15']
  key=[1, (8,), (1.0,), 4]  ->  ['P3C04', 'P3C20']
  key=[1, (9,), (1.0,), 1]  ->  ['P3C33', 'P3C37']
  key=[1, (10,), (1.0,), 10]  ->  ['P3C05']
  key=[1, (12,), (1.0,), 6]  ->  ['P3C06']
  key=[1, (12,), (1.0,), 12]  ->  ['P3C22']
  key=[1, (14,), (1.0,), 14]  ->  ['P3C23']
  key=[1, (15,), (1.0,), 1]  ->  ['P3C38']
  key=[1, (15,), (1.0,), 15]  ->  ['P3C24']
  key=[1, (18,), (1.0,), 18]  ->  ['P3C25']
  key=[2, (3, 3), (1.0, 1.629987), 3]  ->  ['P3C09']
  key=[2, (3, 6), (1.0, 1.259921), 3]  ->  ['P3C21']
  key=[2, (5, 5), (1.0, 1.340635), 5]  ->  ['P3C00']
  key=[2, (5, 5), (1.0, 1.693476), 5]  ->  ['P3C02']
  key=[2, (6, 6), (1.0, 1.551134), 6]  ->  ['P3C16']
  key=[2, (7, 7), (1.0, 1.456846), 7]  ->  ['P3C19']
  key=[3, (2, 3, 2), (1.0, 1.619234, 2.081019), 1]  ->  ['P3C26']
  key=[3, (2, 4, 2), (1.0, 1.573138, 2.081019), 2]  ->  ['P3C27']
  key=[3, (2, 5, 2), (1.0, 1.546112, 2.081019), 1]  ->  ['P3C29']
  key=[3, (2, 8, 2), (1.0, 1.442574, 2.081019), 1]  ->  ['P3C34']
  key=[3, (3, 2, 3), (1.0, 1.093226, 1.341504), 1]  ->  ['P3C28']
  key=[3, (3, 3, 3), (1.0, 1.062659, 1.259921), 3]  ->  ['P3C03']
  key=[3, (3, 3, 3), (1.0, 1.276709, 1.629987), 1]  ->  ['P3C36']
  key=[3, (4, 4, 4), (1.0, 1.293219, 1.807758), 4]  ->  ['P3C10']
  key=[3, (4, 6, 4), (1.0, 1.272491, 1.442574), 2]  ->  ['P3C32']
  key=[3, (5, 5, 5), (1.0, 1.189879, 1.82799), 5]  ->  ['P3C12']
  key=[3, (5, 5, 5), (1.0, 1.240961, 1.340635), 5]  ->  ['P3C30']
  key=[3, (6, 6, 6), (1.0, 1.155897, 1.653147), 6]  ->  ['P3C17']
  key=[4, (3, 4, 4, 3), (1.0, 1.194152, 1.488515, 1.629987), 1]  ->  ['P3C31']
```

## A1 §4 — Minimal distinguishing invariants

Greedy add-one-at-a-time search over candidate invariants {I_Cn, I_nrings, I_rc, I_ratios, I_slope, I_omega, I_z}. Stops when all classes are separated.

### 23-class atlas
Minimal separating set: **['I_rc', 'I_Cn']**

| Step | Added | # distinct classes (out of 23) | # collisions |
|---:|---|---:|---:|
| 1 | `I_rc` | 19 | 4 |
| 2 | `I_Cn` | 23 | 0 |

### 39-class atlas
Minimal separating set: **['I_slope', 'I_omega']**

| Step | Added | # distinct classes (out of 39) | # collisions |
|---:|---|---:|---:|
| 1 | `I_slope` | 37 | 2 |
| 2 | `I_omega` | 39 | 0 |

## A2 §1 — 23-class symmetry-breaking table

| Class | C_k (μ_q stabilizer) | is_regular_polygon |
|---|---:|---|
| `Class[Regular-12-gon]` | C_12 | yes |
| `Class[Regular-9-gon]` | C_9 | yes |
| `Class[Regular-8-gon]` | C_8 | yes |
| `Class[Regular-6-gon]` | C_6 | yes |
| `Class[Regular-4-gon]` | C_4 | yes |
| `Class[C4, rings=[4, 4]]` | C_4 | no |
| `Class[C4, rings=[4, 4, 4]]` | C_4 | no |
| `Class[C4, rings=[4, 8]]` | C_4 | no |
| `Class[C4, rings=[8]]` | C_4 | no |
| `Class[C4, rings=[8, 4]]` | C_4 | no |
| `Class[Regular-3-gon]` | C_3 | yes |
| `Class[C3, rings=[3, 3]]` | C_3 | no |
| `Class[C3, rings=[3, 3, 3]]` | C_3 | no |
| `Class[C3, rings=[3, 6]]` | C_3 | no |
| `Class[C3, rings=[6]]` | C_3 | no |
| `Class[C3, rings=[6, 3]]` | C_3 | no |
| `Class[Regular-2-gon]` | C_2 | yes |
| `Class[C2, rings=[2, 2]]` | C_2 | no |
| `Class[C2, rings=[2, 2, 2]]` | C_2 | no |
| `Class[C2, rings=[2, 4]]` | C_2 | no |
| `Class[C2, rings=[4]]` | C_2 | no |
| `Class[C2, rings=[4, 2]]` | C_2 | no |
| `Class[C2, rings=[6]]` | C_2 | no |

## A2 §2 — 39-class symmetry-breaking table

| ID | C_k (μ_q stabilizer) | is_regular | ω-resonance denom | z-resonances |
|---|---:|---|---:|---:|
| `P3C00` | C_5 (invariant says C_5) | no | 0 | 0 |
| `P3C01` | C_2 (invariant says C_2) | yes | 6 | 16 |
| `P3C02` | C_5 (invariant says C_5) | no | 15 | 0 |
| `P3C03` | C_3 (invariant says C_3) | no | 3 | 3 |
| `P3C04` | C_4 (invariant says C_4) | yes | 24 | 30 |
| `P3C05` | C_10 (invariant says C_10) | yes | 10 | 30 |
| `P3C06` | C_6 (invariant says C_6) | yes | 18 | 30 |
| `P3C07` | C_2 (invariant says C_2) | no | 2 | 1 |
| `P3C08` | C_1 (invariant says C_1) | yes | 3 | 1 |
| `P3C09` | C_3 (invariant says C_3) | no | 0 | 2 |
| `P3C10` | C_4 (invariant says C_4) | no | 0 | 30 |
| `P3C11` | C_1 (invariant says C_1) | yes | 5 | 0 |
| `P3C12` | C_5 (invariant says C_5) | no | 0 | 0 |
| `P3C13` | C_3 (invariant says C_3) | yes | 21 | 2 |
| `P3C14` | C_6 (invariant says C_6) | yes | 6 | 30 |
| `P3C15` | C_2 (invariant says C_2) | yes | 10 | 30 |
| `P3C16` | C_6 (invariant says C_6) | no | 18 | 30 |
| `P3C17` | C_6 (invariant says C_6) | no | 0 | 30 |
| `P3C18` | C_1 (invariant says C_1) | yes | 7 | 0 |
| `P3C19` | C_7 (invariant says C_7) | no | 21 | 0 |
| `P3C20` | C_4 (invariant says C_4) | yes | 12 | 30 |
| `P3C21` | C_3 (invariant says C_3) | no | 3 | 30 |
| `P3C22` | C_12 (invariant says C_12) | yes | 12 | 30 |
| `P3C23` | C_14 (invariant says C_14) | yes | 14 | 30 |
| `P3C24` | C_15 (invariant says C_15) | yes | 15 | 5 |
| `P3C25` | C_18 (invariant says C_18) | yes | 18 | 30 |
| `P3C26` | C_1 (invariant says C_1) | no | 0 | 30 |
| `P3C27` | C_2 (invariant says C_2) | no | 0 | 30 |
| `P3C28` | C_1 (invariant says C_1) | no | 0 | 30 |
| `P3C29` | C_1 (invariant says C_1) | no | 0 | 30 |
| `P3C30` | C_5 (invariant says C_5) | no | 0 | 30 |
| `P3C31` | C_1 (invariant says C_1) | no | 0 | 30 |
| `P3C32` | C_2 (invariant says C_2) | no | 0 | 30 |
| `P3C33` | C_1 (invariant says C_1) | yes | 24 | 30 |
| `P3C34` | C_1 (invariant says C_1) | no | 0 | 30 |
| `P3C35` | C_1 (invariant says C_1) | yes | 12 | 2 |
| `P3C36` | C_1 (invariant says C_1) | no | 0 | 3 |
| `P3C37` | C_1 (invariant says C_1) | yes | 24 | 30 |
| `P3C38` | C_1 (invariant says C_1) | yes | 5 | 30 |

## A2 §3 — Nontrivial-stabilizer roll-up

### 23-class atlas
- total classes: **23**  ·  trivial (C_1): **0**  ·  nontrivial: **23**

| C_k | # classes | members |
|---:|---:|---|
| C_2 | 7 | `Class[C2, rings=[2, 2, 2]]`, `Class[C2, rings=[2, 2]]`, `Class[C2, rings=[2, 4]]`, `Class[C2, rings=[4, 2]]`, `Class[C2, rings=[4]]`, `Class[C2, rings=[6]]`, `Class[Regular-2-gon]` |
| C_3 | 6 | `Class[C3, rings=[3, 3, 3]]`, `Class[C3, rings=[3, 3]]`, `Class[C3, rings=[3, 6]]`, `Class[C3, rings=[6, 3]]`, `Class[C3, rings=[6]]`, `Class[Regular-3-gon]` |
| C_4 | 6 | `Class[C4, rings=[4, 4, 4]]`, `Class[C4, rings=[4, 4]]`, `Class[C4, rings=[4, 8]]`, `Class[C4, rings=[8, 4]]`, `Class[C4, rings=[8]]`, `Class[Regular-4-gon]` |
| C_6 | 1 | `Class[Regular-6-gon]` |
| C_8 | 1 | `Class[Regular-8-gon]` |
| C_9 | 1 | `Class[Regular-9-gon]` |
| C_12 | 1 | `Class[Regular-12-gon]` |

### 39-class atlas
- total classes: **39**  ·  trivial (C_1): **13**  ·  nontrivial: **26**

| C_k | # classes | members |
|---:|---:|---|
| C_1 | 13 | `P3C08`, `P3C11`, `P3C18`, `P3C26`, `P3C28`, `P3C29`, `P3C31`, `P3C33`, `P3C34`, `P3C35`, `P3C36`, `P3C37`, `P3C38` |
| C_2 | 5 | `P3C01`, `P3C07`, `P3C15`, `P3C27`, `P3C32` |
| C_3 | 4 | `P3C03`, `P3C09`, `P3C13`, `P3C21` |
| C_4 | 3 | `P3C04`, `P3C10`, `P3C20` |
| C_5 | 4 | `P3C00`, `P3C02`, `P3C12`, `P3C30` |
| C_6 | 4 | `P3C06`, `P3C14`, `P3C16`, `P3C17` |
| C_7 | 1 | `P3C19` |
| C_10 | 1 | `P3C05` |
| C_12 | 1 | `P3C22` |
| C_14 | 1 | `P3C23` |
| C_15 | 1 | `P3C24` |
| C_18 | 1 | `P3C25` |

---
## Headline findings

### A1 — constellation shape
- 23-class atlas: **2 invariants suffice** — `['I_rc', 'I_Cn']` (ring_counts × Cn_order). Ring-radius ratios provide secondary structure but are not needed for separation.
- 39-class atlas: **2 invariants suffice** — `['I_slope', 'I_omega']` (slope multiset × ω-resonance denominator). The Δ-modulus partition (slope) is finer than ring-counts on the refined atlas.

### A2 — symmetry breaking
- 23-class atlas: **all 23 classes have nontrivial μ_q stabilizer** (C_k with k ≥ 2). Stabilizer orders present: ['2', '3', '4', '6', '8', '9', '12'].
- 39-class atlas: **26 of 39 classes have nontrivial stabilizer**; 13 have trivial C_1 stabilizer (symmetry fully broken).
- 39-class stabilizer orders present: [1, 2, 3, 4, 5, 6, 7, 10, 12, 14, 15, 18].

Generated by `code/atlas_fingerprints.py`. Inputs: `data/clusters.json`, `data/phase3_clusters.json`, `data/constellations.json`, `data/phase3_invariants.json`.
