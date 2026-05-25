# Fleet Report — Global WKB Pattern Discovery

- Operators generated: **89**
- Distinct constellation classes: **23**

## Pipeline outputs (summary table)

| Operator | type | slope p/q | rank | valuation | χ | n_roots | C_n | rings | regular? |
|---|---|---|---|---|---|---:|---:|---|:---:|
| `ODE_s1o2_r1_simple` | ode | 1/2 | 1 | simple | `beta + c**2` | 2 | 2 | [2] | ✓ |
| `ODE_s1o2_r2_simple` | ode | 1/2 | 2 | simple | `beta + c**4` | 4 | 4 | [4] | ✓ |
| `ODE_s1o2_r2_double` | ode | 1/2 | 2 | double | `beta + c**4 + c**2*gamma` | 4 | 2 | [4] |  |
| `ODE_s1o2_r2_mixed` | ode | 1/2 | 2 | mixed | `beta + c**4 + 3*c**2` | 4 | 2 | [2, 2] |  |
| `ODE_s1o2_r2_generic_complex` | ode | 1/2 | 2 | generic_complex | `beta + c**4 + 2*c**2 + 3*I*c**2` | 4 | 2 | [2, 2] |  |
| `ODE_s1o2_r3_simple` | ode | 1/2 | 3 | simple | `beta + c**6` | 6 | 6 | [6] | ✓ |
| `ODE_s1o2_r3_double` | ode | 1/2 | 3 | double | `beta + c**6 + c**4*gamma` | 6 | 2 | [4, 2] |  |
| `ODE_s1o2_r3_mixed` | ode | 1/2 | 3 | mixed | `beta + c**6 + 3*c**4 + 4*c**2` | 6 | 2 | [2, 4] |  |
| `ODE_s1o2_r3_generic_complex` | ode | 1/2 | 3 | generic_complex | `beta + c**6 + 2*c**4 + 3*I*c**4 + 3*…` | 6 | 2 | [2, 2, 2] |  |
| `ODE_s1o3_r1_simple` | ode | 1/3 | 1 | simple | `beta + c**3` | 3 | 3 | [3] | ✓ |
| `ODE_s1o3_r2_simple` | ode | 1/3 | 2 | simple | `beta + c**6` | 6 | 6 | [6] | ✓ |
| `ODE_s1o3_r2_double` | ode | 1/3 | 2 | double | `beta + c**6 + c**3*gamma` | 6 | 3 | [6] |  |
| `ODE_s1o3_r2_mixed` | ode | 1/3 | 2 | mixed | `beta + c**6 + 3*c**3` | 6 | 3 | [3, 3] |  |
| `ODE_s1o3_r2_generic_complex` | ode | 1/3 | 2 | generic_complex | `beta + c**6 + 2*c**3 + 3*I*c**3` | 6 | 3 | [3, 3] |  |
| `ODE_s1o3_r3_simple` | ode | 1/3 | 3 | simple | `beta + c**9` | 9 | 9 | [9] | ✓ |
| `ODE_s1o3_r3_double` | ode | 1/3 | 3 | double | `beta + c**9 + c**6*gamma` | 9 | 3 | [6, 3] |  |
| `ODE_s1o3_r3_mixed` | ode | 1/3 | 3 | mixed | `beta + c**9 + 3*c**6 + 4*c**3` | 9 | 3 | [3, 6] |  |
| `ODE_s1o3_r3_generic_complex` | ode | 1/3 | 3 | generic_complex | `beta + c**9 + 2*c**6 + 3*I*c**6 + 3*…` | 9 | 3 | [3, 3, 3] |  |
| `ODE_s1o4_r1_simple` | ode | 1/4 | 1 | simple | `beta + c**4` | 4 | 4 | [4] | ✓ |
| `ODE_s1o4_r2_simple` | ode | 1/4 | 2 | simple | `beta + c**8` | 8 | 8 | [8] | ✓ |
| `ODE_s1o4_r2_double` | ode | 1/4 | 2 | double | `beta + c**8 + c**4*gamma` | 8 | 4 | [8] |  |
| `ODE_s1o4_r2_mixed` | ode | 1/4 | 2 | mixed | `beta + c**8 + 3*c**4` | 8 | 4 | [4, 4] |  |
| `ODE_s1o4_r2_generic_complex` | ode | 1/4 | 2 | generic_complex | `beta + c**8 + 2*c**4 + 3*I*c**4` | 8 | 4 | [4, 4] |  |
| `ODE_s1o4_r3_simple` | ode | 1/4 | 3 | simple | `beta + c**12` | 12 | 12 | [12] | ✓ |
| `ODE_s1o4_r3_double` | ode | 1/4 | 3 | double | `beta + c**12 + c**8*gamma` | 12 | 4 | [8, 4] |  |
| `ODE_s1o4_r3_mixed` | ode | 1/4 | 3 | mixed | `beta + c**12 + 3*c**8 + 4*c**4` | 12 | 4 | [4, 8] |  |
| `ODE_s1o4_r3_generic_complex` | ode | 1/4 | 3 | generic_complex | `beta + c**12 + 2*c**8 + 3*I*c**8 + 3…` | 12 | 4 | [4, 4, 4] |  |
| `ODE_s2o3_r1_simple` | ode | 2/3 | 1 | simple | `beta + c**3` | 3 | 3 | [3] | ✓ |
| `ODE_s2o3_r2_simple` | ode | 2/3 | 2 | simple | `beta + c**6` | 6 | 6 | [6] | ✓ |
| `ODE_s2o3_r2_double` | ode | 2/3 | 2 | double | `beta + c**6 + c**3*gamma` | 6 | 3 | [6] |  |
| `ODE_s2o3_r2_mixed` | ode | 2/3 | 2 | mixed | `beta + c**6 + 3*c**3` | 6 | 3 | [3, 3] |  |
| `ODE_s2o3_r2_generic_complex` | ode | 2/3 | 2 | generic_complex | `beta + c**6 + 2*c**3 + 3*I*c**3` | 6 | 3 | [3, 3] |  |
| `ODE_s2o3_r3_simple` | ode | 2/3 | 3 | simple | `beta + c**9` | 9 | 9 | [9] | ✓ |
| `ODE_s2o3_r3_double` | ode | 2/3 | 3 | double | `beta + c**9 + c**6*gamma` | 9 | 3 | [6, 3] |  |
| `ODE_s2o3_r3_mixed` | ode | 2/3 | 3 | mixed | `beta + c**9 + 3*c**6 + 4*c**3` | 9 | 3 | [3, 6] |  |
| `ODE_s2o3_r3_generic_complex` | ode | 2/3 | 3 | generic_complex | `beta + c**9 + 2*c**6 + 3*I*c**6 + 3*…` | 9 | 3 | [3, 3, 3] |  |
| `ODE_s3o2_r1_simple` | ode | 3/2 | 1 | simple | `beta + c**2` | 2 | 2 | [2] | ✓ |
| `ODE_s3o2_r2_simple` | ode | 3/2 | 2 | simple | `beta + c**4` | 4 | 4 | [4] | ✓ |
| `ODE_s3o2_r2_double` | ode | 3/2 | 2 | double | `beta + c**4 + c**2*gamma` | 4 | 2 | [4] |  |
| `ODE_s3o2_r2_mixed` | ode | 3/2 | 2 | mixed | `beta + c**4 + 3*c**2` | 4 | 2 | [2, 2] |  |
| `ODE_s3o2_r2_generic_complex` | ode | 3/2 | 2 | generic_complex | `beta + c**4 + 2*c**2 + 3*I*c**2` | 4 | 2 | [2, 2] |  |
| `ODE_s3o2_r3_simple` | ode | 3/2 | 3 | simple | `beta + c**6` | 6 | 6 | [6] | ✓ |
| `ODE_s3o2_r3_double` | ode | 3/2 | 3 | double | `beta + c**6 + c**4*gamma` | 6 | 2 | [4, 2] |  |
| `ODE_s3o2_r3_mixed` | ode | 3/2 | 3 | mixed | `beta + c**6 + 3*c**4 + 4*c**2` | 6 | 2 | [2, 4] |  |
| `ODE_s3o2_r3_generic_complex` | ode | 3/2 | 3 | generic_complex | `beta + c**6 + 2*c**4 + 3*I*c**4 + 3*…` | 6 | 2 | [2, 2, 2] |  |
| `DIFFERENCE_s1o2_r1_simple` | difference | 1/2 | 1 | simple | `beta + c**2` | 2 | 2 | [2] | ✓ |
| `DIFFERENCE_s1o2_r2_simple` | difference | 1/2 | 2 | simple | `beta + c**4` | 4 | 4 | [4] | ✓ |
| `DIFFERENCE_s1o2_r2_mixed` | difference | 1/2 | 2 | mixed | `beta + c**4 + 3*c**2` | 4 | 2 | [2, 2] |  |
| `DIFFERENCE_s1o2_r2_generic_complex` | difference | 1/2 | 2 | generic_complex | `beta + c**4 + 2*c**2 + 3*I*c**2` | 4 | 2 | [2, 2] |  |
| `DIFFERENCE_s1o3_r1_simple` | difference | 1/3 | 1 | simple | `beta + c**3` | 3 | 3 | [3] | ✓ |
| `DIFFERENCE_s1o3_r2_simple` | difference | 1/3 | 2 | simple | `beta + c**6` | 6 | 6 | [6] | ✓ |
| `DIFFERENCE_s1o3_r2_mixed` | difference | 1/3 | 2 | mixed | `beta + c**6 + 3*c**3` | 6 | 3 | [3, 3] |  |
| `DIFFERENCE_s1o3_r2_generic_complex` | difference | 1/3 | 2 | generic_complex | `beta + c**6 + 2*c**3 + 3*I*c**3` | 6 | 3 | [3, 3] |  |
| `DIFFERENCE_s1o4_r1_simple` | difference | 1/4 | 1 | simple | `beta + c**4` | 4 | 4 | [4] | ✓ |
| `DIFFERENCE_s1o4_r2_simple` | difference | 1/4 | 2 | simple | `beta + c**8` | 8 | 8 | [8] | ✓ |
| `DIFFERENCE_s1o4_r2_mixed` | difference | 1/4 | 2 | mixed | `beta + c**8 + 3*c**4` | 8 | 4 | [4, 4] |  |
| `DIFFERENCE_s1o4_r2_generic_complex` | difference | 1/4 | 2 | generic_complex | `beta + c**8 + 2*c**4 + 3*I*c**4` | 8 | 4 | [4, 4] |  |
| `DIFFERENCE_s2o3_r1_simple` | difference | 2/3 | 1 | simple | `beta + c**3` | 3 | 3 | [3] | ✓ |
| `DIFFERENCE_s2o3_r2_simple` | difference | 2/3 | 2 | simple | `beta + c**6` | 6 | 6 | [6] | ✓ |
| `DIFFERENCE_s2o3_r2_mixed` | difference | 2/3 | 2 | mixed | `beta + c**6 + 3*c**3` | 6 | 3 | [3, 3] |  |
| `DIFFERENCE_s2o3_r2_generic_complex` | difference | 2/3 | 2 | generic_complex | `beta + c**6 + 2*c**3 + 3*I*c**3` | 6 | 3 | [3, 3] |  |
| `DIFFERENCE_s3o2_r1_simple` | difference | 3/2 | 1 | simple | `beta + c**2` | 2 | 2 | [2] | ✓ |
| `DIFFERENCE_s3o2_r2_simple` | difference | 3/2 | 2 | simple | `beta + c**4` | 4 | 4 | [4] | ✓ |
| `DIFFERENCE_s3o2_r2_mixed` | difference | 3/2 | 2 | mixed | `beta + c**4 + 3*c**2` | 4 | 2 | [2, 2] |  |
| `DIFFERENCE_s3o2_r2_generic_complex` | difference | 3/2 | 2 | generic_complex | `beta + c**4 + 2*c**2 + 3*I*c**2` | 4 | 2 | [2, 2] |  |
| `Q-DIFFERENCE_s1o2_r1_simple` | q-difference | 1/2 | 1 | simple | `beta + c**2` | 2 | 2 | [2] | ✓ |
| `Q-DIFFERENCE_s1o2_r2_simple` | q-difference | 1/2 | 2 | simple | `beta + c**4` | 4 | 4 | [4] | ✓ |
| `Q-DIFFERENCE_s1o2_r2_mixed` | q-difference | 1/2 | 2 | mixed | `beta + c**4 + 3*c**2` | 4 | 2 | [2, 2] |  |
| `Q-DIFFERENCE_s1o2_r2_generic_complex` | q-difference | 1/2 | 2 | generic_complex | `beta + c**4 + 2*c**2 + 3*I*c**2` | 4 | 2 | [2, 2] |  |
| `Q-DIFFERENCE_s1o3_r1_simple` | q-difference | 1/3 | 1 | simple | `beta + c**3` | 3 | 3 | [3] | ✓ |
| `Q-DIFFERENCE_s1o3_r2_simple` | q-difference | 1/3 | 2 | simple | `beta + c**6` | 6 | 6 | [6] | ✓ |
| `Q-DIFFERENCE_s1o3_r2_mixed` | q-difference | 1/3 | 2 | mixed | `beta + c**6 + 3*c**3` | 6 | 3 | [3, 3] |  |
| `Q-DIFFERENCE_s1o3_r2_generic_complex` | q-difference | 1/3 | 2 | generic_complex | `beta + c**6 + 2*c**3 + 3*I*c**3` | 6 | 3 | [3, 3] |  |
| `Q-DIFFERENCE_s1o4_r1_simple` | q-difference | 1/4 | 1 | simple | `beta + c**4` | 4 | 4 | [4] | ✓ |
| `Q-DIFFERENCE_s1o4_r2_simple` | q-difference | 1/4 | 2 | simple | `beta + c**8` | 8 | 8 | [8] | ✓ |
| `Q-DIFFERENCE_s1o4_r2_mixed` | q-difference | 1/4 | 2 | mixed | `beta + c**8 + 3*c**4` | 8 | 4 | [4, 4] |  |
| `Q-DIFFERENCE_s1o4_r2_generic_complex` | q-difference | 1/4 | 2 | generic_complex | `beta + c**8 + 2*c**4 + 3*I*c**4` | 8 | 4 | [4, 4] |  |
| `Q-DIFFERENCE_s2o3_r1_simple` | q-difference | 2/3 | 1 | simple | `beta + c**3` | 3 | 3 | [3] | ✓ |
| `Q-DIFFERENCE_s2o3_r2_simple` | q-difference | 2/3 | 2 | simple | `beta + c**6` | 6 | 6 | [6] | ✓ |
| `Q-DIFFERENCE_s2o3_r2_mixed` | q-difference | 2/3 | 2 | mixed | `beta + c**6 + 3*c**3` | 6 | 3 | [3, 3] |  |
| `Q-DIFFERENCE_s2o3_r2_generic_complex` | q-difference | 2/3 | 2 | generic_complex | `beta + c**6 + 2*c**3 + 3*I*c**3` | 6 | 3 | [3, 3] |  |
| `Q-DIFFERENCE_s3o2_r1_simple` | q-difference | 3/2 | 1 | simple | `beta + c**2` | 2 | 2 | [2] | ✓ |
| `Q-DIFFERENCE_s3o2_r2_simple` | q-difference | 3/2 | 2 | simple | `beta + c**4` | 4 | 4 | [4] | ✓ |
| `Q-DIFFERENCE_s3o2_r2_mixed` | q-difference | 3/2 | 2 | mixed | `beta + c**4 + 3*c**2` | 4 | 2 | [2, 2] |  |
| `Q-DIFFERENCE_s3o2_r2_generic_complex` | q-difference | 3/2 | 2 | generic_complex | `beta + c**4 + 2*c**2 + 3*I*c**2` | 4 | 2 | [2, 2] |  |
| `STRESS_equalmod` | ode | 1/2 | 3 | stress | `c**6 - 2*c**4 + 4*c**2 - 8` | 6 | 2 | [6] |  |
| `STRESS_doubleroot` | ode | 1/3 | 3 | stress | `c**9 - 4*c**6 + 5*c**3 - 2` | 9 | 3 | [6, 3] |  |
| `STRESS_zeroroot` | ode | 1/2 | 2 | stress | `c**4 - c**2` | 4 | 2 | [2, 2] |  |
| `STRESS_accidental_sym` | ode | 1/2 | 3 | stress | `c**6 + 1` | 6 | 6 | [6] | ✓ |

## Constellation classes (clustering)

### Class[Regular-12-gon]
All 12 roots lie on a single ring; rotational symmetry C_12. Regular 12-gon.
- members (1): `ODE_s1o4_r3_simple`
- representative: `ODE_s1o4_r3_simple` (eqtype=ode, slope=1/4, rank=3, valuation=simple)
  - χ = `beta + c**12`
  - rings: radius≈1.0000, count=12

### Class[Regular-9-gon]
All 9 roots lie on a single ring; rotational symmetry C_9. Regular 9-gon.
- members (2): `ODE_s1o3_r3_simple`, `ODE_s2o3_r3_simple`
- representative: `ODE_s1o3_r3_simple` (eqtype=ode, slope=1/3, rank=3, valuation=simple)
  - χ = `beta + c**9`
  - rings: radius≈1.0000, count=9

### Class[Regular-8-gon]
All 8 roots lie on a single ring; rotational symmetry C_8. Regular 8-gon.
- members (3): `ODE_s1o4_r2_simple`, `DIFFERENCE_s1o4_r2_simple`, `Q-DIFFERENCE_s1o4_r2_simple`
- representative: `ODE_s1o4_r2_simple` (eqtype=ode, slope=1/4, rank=2, valuation=simple)
  - χ = `beta + c**8`
  - rings: radius≈1.0000, count=8

### Class[Regular-6-gon]
All 6 roots lie on a single ring; rotational symmetry C_6. Regular 6-gon.
- members (9): `ODE_s1o2_r3_simple`, `ODE_s1o3_r2_simple`, `ODE_s2o3_r2_simple`, `ODE_s3o2_r3_simple`, `DIFFERENCE_s1o3_r2_simple`, `DIFFERENCE_s2o3_r2_simple`, `Q-DIFFERENCE_s1o3_r2_simple`, `Q-DIFFERENCE_s2o3_r2_simple`…
- representative: `ODE_s1o2_r3_simple` (eqtype=ode, slope=1/2, rank=3, valuation=simple)
  - χ = `beta + c**6`
  - rings: radius≈1.0000, count=6

### Class[Regular-4-gon]
All 4 roots lie on a single ring; rotational symmetry C_4. Regular 4-gon.
- members (9): `ODE_s1o2_r2_simple`, `ODE_s1o4_r1_simple`, `ODE_s3o2_r2_simple`, `DIFFERENCE_s1o2_r2_simple`, `DIFFERENCE_s1o4_r1_simple`, `DIFFERENCE_s3o2_r2_simple`, `Q-DIFFERENCE_s1o2_r2_simple`, `Q-DIFFERENCE_s1o4_r1_simple`…
- representative: `ODE_s1o2_r2_simple` (eqtype=ode, slope=1/2, rank=2, valuation=simple)
  - χ = `beta + c**4`
  - rings: radius≈1.0000, count=4

### Class[C4, rings=[4, 4]]
Multi-ring constellation with ring multiplicities [4, 4] and global rotational symmetry C_4.
- members (6): `ODE_s1o4_r2_mixed`, `ODE_s1o4_r2_generic_complex`, `DIFFERENCE_s1o4_r2_mixed`, `DIFFERENCE_s1o4_r2_generic_complex`, `Q-DIFFERENCE_s1o4_r2_mixed`, `Q-DIFFERENCE_s1o4_r2_generic_complex`
- representative: `ODE_s1o4_r2_mixed` (eqtype=ode, slope=1/4, rank=2, valuation=mixed)
  - χ = `beta + c**8 + 3*c**4`
  - rings: radius≈0.7862, count=4; radius≈1.2720, count=4

### Class[C4, rings=[4, 4, 4]]
Multi-ring constellation with ring multiplicities [4, 4, 4] and global rotational symmetry C_4.
- members (1): `ODE_s1o4_r3_generic_complex`
- representative: `ODE_s1o4_r3_generic_complex` (eqtype=ode, slope=1/4, rank=3, valuation=generic_complex)
  - χ = `beta + c**12 + 2*c**8 + 3*I*c**8 + 3*c**4 + 5*I*c**4`
  - rings: radius≈0.6504, count=4; radius≈1.1123, count=4; radius≈1.3823, count=4

### Class[C4, rings=[4, 8]]
Multi-ring constellation with ring multiplicities [4, 8] and global rotational symmetry C_4.
- members (1): `ODE_s1o4_r3_mixed`
- representative: `ODE_s1o4_r3_mixed` (eqtype=ode, slope=1/4, rank=3, valuation=mixed)
  - χ = `beta + c**12 + 3*c**8 + 4*c**4`
  - rings: radius≈0.7507, count=4; radius≈1.1541, count=8

### Class[C4, rings=[8]]
Multi-ring constellation with ring multiplicities [8] and global rotational symmetry C_4.
- members (1): `ODE_s1o4_r2_double`
- representative: `ODE_s1o4_r2_double` (eqtype=ode, slope=1/4, rank=2, valuation=double)
  - χ = `beta + c**8 + c**4*gamma`
  - rings: radius≈1.0000, count=8

### Class[C4, rings=[8, 4]]
Multi-ring constellation with ring multiplicities [8, 4] and global rotational symmetry C_4.
- members (1): `ODE_s1o4_r3_double`
- representative: `ODE_s1o4_r3_double` (eqtype=ode, slope=1/4, rank=3, valuation=double)
  - χ = `beta + c**12 + c**8*gamma`
  - rings: radius≈0.9533, count=8; radius≈1.1003, count=4

### Class[Regular-3-gon]
All 3 roots lie on a single ring; rotational symmetry C_3. Regular 3-gon.
- members (6): `ODE_s1o3_r1_simple`, `ODE_s2o3_r1_simple`, `DIFFERENCE_s1o3_r1_simple`, `DIFFERENCE_s2o3_r1_simple`, `Q-DIFFERENCE_s1o3_r1_simple`, `Q-DIFFERENCE_s2o3_r1_simple`
- representative: `ODE_s1o3_r1_simple` (eqtype=ode, slope=1/3, rank=1, valuation=simple)
  - χ = `beta + c**3`
  - rings: radius≈1.0000, count=3

### Class[C3, rings=[3, 3]]
Multi-ring constellation with ring multiplicities [3, 3] and global rotational symmetry C_3.
- members (12): `ODE_s1o3_r2_mixed`, `ODE_s1o3_r2_generic_complex`, `ODE_s2o3_r2_mixed`, `ODE_s2o3_r2_generic_complex`, `DIFFERENCE_s1o3_r2_mixed`, `DIFFERENCE_s1o3_r2_generic_complex`, `DIFFERENCE_s2o3_r2_mixed`, `DIFFERENCE_s2o3_r2_generic_complex`…
- representative: `ODE_s1o3_r2_mixed` (eqtype=ode, slope=1/3, rank=2, valuation=mixed)
  - χ = `beta + c**6 + 3*c**3`
  - rings: radius≈0.7256, count=3; radius≈1.3782, count=3

### Class[C3, rings=[3, 3, 3]]
Multi-ring constellation with ring multiplicities [3, 3, 3] and global rotational symmetry C_3.
- members (2): `ODE_s1o3_r3_generic_complex`, `ODE_s2o3_r3_generic_complex`
- representative: `ODE_s1o3_r3_generic_complex` (eqtype=ode, slope=1/3, rank=3, valuation=generic_complex)
  - χ = `beta + c**9 + 2*c**6 + 3*I*c**6 + 3*c**3 + 5*I*c**3`
  - rings: radius≈0.5635, count=3; radius≈1.1525, count=3; radius≈1.5399, count=3

### Class[C3, rings=[3, 6]]
Multi-ring constellation with ring multiplicities [3, 6] and global rotational symmetry C_3.
- members (2): `ODE_s1o3_r3_mixed`, `ODE_s2o3_r3_mixed`
- representative: `ODE_s1o3_r3_mixed` (eqtype=ode, slope=1/3, rank=3, valuation=mixed)
  - χ = `beta + c**9 + 3*c**6 + 4*c**3`
  - rings: radius≈0.6823, count=3; radius≈1.2106, count=6

### Class[C3, rings=[6]]
Multi-ring constellation with ring multiplicities [6] and global rotational symmetry C_3.
- members (2): `ODE_s1o3_r2_double`, `ODE_s2o3_r2_double`
- representative: `ODE_s1o3_r2_double` (eqtype=ode, slope=1/3, rank=2, valuation=double)
  - χ = `beta + c**6 + c**3*gamma`
  - rings: radius≈1.0000, count=6

### Class[C3, rings=[6, 3]]
Multi-ring constellation with ring multiplicities [6, 3] and global rotational symmetry C_3.
- members (3): `ODE_s1o3_r3_double`, `ODE_s2o3_r3_double`, `STRESS_doubleroot`
- representative: `ODE_s1o3_r3_double` (eqtype=ode, slope=1/3, rank=3, valuation=double)
  - χ = `beta + c**9 + c**6*gamma`
  - rings: radius≈0.9383, count=6; radius≈1.1359, count=3

### Class[Regular-2-gon]
All 2 roots lie on a single ring; rotational symmetry C_2. Regular 2-gon.
- members (6): `ODE_s1o2_r1_simple`, `ODE_s3o2_r1_simple`, `DIFFERENCE_s1o2_r1_simple`, `DIFFERENCE_s3o2_r1_simple`, `Q-DIFFERENCE_s1o2_r1_simple`, `Q-DIFFERENCE_s3o2_r1_simple`
- representative: `ODE_s1o2_r1_simple` (eqtype=ode, slope=1/2, rank=1, valuation=simple)
  - χ = `beta + c**2`
  - rings: radius≈1.0000, count=2

### Class[C2, rings=[2, 2]]
Multi-ring constellation with ring multiplicities [2, 2] and global rotational symmetry C_2.
- members (13): `ODE_s1o2_r2_mixed`, `ODE_s1o2_r2_generic_complex`, `ODE_s3o2_r2_mixed`, `ODE_s3o2_r2_generic_complex`, `DIFFERENCE_s1o2_r2_mixed`, `DIFFERENCE_s1o2_r2_generic_complex`, `DIFFERENCE_s3o2_r2_mixed`, `DIFFERENCE_s3o2_r2_generic_complex`…
- representative: `ODE_s1o2_r2_mixed` (eqtype=ode, slope=1/2, rank=2, valuation=mixed)
  - χ = `beta + c**4 + 3*c**2`
  - rings: radius≈0.6180, count=2; radius≈1.6180, count=2

### Class[C2, rings=[2, 2, 2]]
Multi-ring constellation with ring multiplicities [2, 2, 2] and global rotational symmetry C_2.
- members (2): `ODE_s1o2_r3_generic_complex`, `ODE_s3o2_r3_generic_complex`
- representative: `ODE_s1o2_r3_generic_complex` (eqtype=ode, slope=1/2, rank=3, valuation=generic_complex)
  - χ = `beta + c**6 + 2*c**4 + 3*I*c**4 + 3*c**2 + 5*I*c**2`
  - rings: radius≈0.4230, count=2; radius≈1.2373, count=2; radius≈1.9109, count=2

### Class[C2, rings=[2, 4]]
Multi-ring constellation with ring multiplicities [2, 4] and global rotational symmetry C_2.
- members (2): `ODE_s1o2_r3_mixed`, `ODE_s3o2_r3_mixed`
- representative: `ODE_s1o2_r3_mixed` (eqtype=ode, slope=1/2, rank=3, valuation=mixed)
  - χ = `beta + c**6 + 3*c**4 + 4*c**2`
  - rings: radius≈0.5636, count=2; radius≈1.3320, count=4

### Class[C2, rings=[4]]
Multi-ring constellation with ring multiplicities [4] and global rotational symmetry C_2.
- members (2): `ODE_s1o2_r2_double`, `ODE_s3o2_r2_double`
- representative: `ODE_s1o2_r2_double` (eqtype=ode, slope=1/2, rank=2, valuation=double)
  - χ = `beta + c**4 + c**2*gamma`
  - rings: radius≈1.0000, count=4

### Class[C2, rings=[4, 2]]
Multi-ring constellation with ring multiplicities [4, 2] and global rotational symmetry C_2.
- members (2): `ODE_s1o2_r3_double`, `ODE_s3o2_r3_double`
- representative: `ODE_s1o2_r3_double` (eqtype=ode, slope=1/2, rank=3, valuation=double)
  - χ = `beta + c**6 + c**4*gamma`
  - rings: radius≈0.9089, count=4; radius≈1.2106, count=2

### Class[C2, rings=[6]]
Multi-ring constellation with ring multiplicities [6] and global rotational symmetry C_2.
- members (1): `STRESS_equalmod`
- representative: `STRESS_equalmod` (eqtype=ode, slope=1/2, rank=3, valuation=stress)
  - χ = `c**6 - 2*c**4 + 4*c**2 - 8`
  - rings: radius≈1.4142, count=6

## Conjectures, Corollaries, and Stress Tests

**Main Theorem (μ_q-equivariant pullback).** Let L have a dominant Newton edge of slope −p/q (lowest terms) and rank multiplier r (so the edge has r+1 lattice points). Define the *inner polynomial* χ_w(w) of degree r by χ(c) = χ_w(c^q). Then the WKB exponent constellation is the **μ_q-equivariant pullback of the root multiset of χ_w under c ↦ c^q**: 

Roots(χ) = ⋃_{w_i : χ_w(w_i)=0} { c ∈ ℂ : c^q = w_i }. 

Every other observation in this report is a direct corollary of this factorisation plus Vieta, away from the discriminant / zero-root / equal-modulus loci.

**Corollary 1 (Simple ⇒ regular d-gon).** χ binomial αc^d+β ⇒ constellation = regular d-gon centered at 0, with d = r·q. *Why*: roots of a binomial are roots of unity scaled and rotated. Verified on 35/35 simple operators.

**Corollary 2 (q | C_n, the μ_q-equivariance).** If the dominant edge has slope p/q (lowest terms) then C_q acts on Roots(χ) by c ↦ ζ_q c. Hence the detected rotational-symmetry order is a *multiple of q*; it may be strictly larger when χ has accidental coefficient zeros (see STRESS_accidental_sym below). Verified on 85/85 non-stress operators.

**Corollary 3 (Ring-count partition is a q-refinement).** Group Roots(χ) by |c|. Each block has size divisible by q, since each fiber {c: c^q = w_i} is a regular q-gon. The partition is the |w|-fibre-structure of the inner polynomial. Verified on 85/85 operators.

**Corollary 3a (Generic regime: rank ⇒ ring count).** When all |w_i| are distinct (a Zariski-open condition on edge coefficients, achieved here with non-real complex generic α_j), the constellation has *exactly r rings of q points each*. Verified on 20/20 generic_complex operators.

**Corollary 4 (Vieta monodromy).** Under β → e^{iθ}β, arg ∏ c_k changes by exactly θ (mod 2π). This is literally Vieta's identity ∏ c_k = (−1)^d β/α applied to the leading and constant coefficient. Verified on 85/85 non-stress operators with θ = π/3.

**Corollary 4a (Simple ring rotates by θ/d).** For binomial χ, every root rotates by θ/d. Verified on 35/35 simple operators.

**Corollary 4b (Weighted ring-rotation sum rule).** Σ_k m_k Δ_k ≡ θ (mod 2π). This is the additive (logarithmic) form of Vieta. It is *not* an independent statement: the individual Δ_k are only defined modulo 2π/m_k, and m_k · Δ_k is exactly the well-defined Vieta lift. Verified on 70/70 operators (machine precision).

**Observation 5 (Equation-type invariance — combinatorial only).** *Under the same tropical-symbol extraction recipe* (Newton polygon → edge polynomial χ via leading x-coefficients), the constellation class depends only on χ and not on whether L is ODE / shift / q-shift. *Caveat*: this is **not** a statement about formal operator classification — the natural spectral variable differs across equation types (c vs e^c vs q^c). The Levelt–Turrittin / Birkhoff–Trjitzinsky / Sauloy classifications use distinct normalisations and may attach different formal types to operators that share a constellation.

**Stress-test report (failure modes of the naive picture).**

- `STRESS_equalmod`: χ = `c**6 - 2*c**4 + 4*c**2 - 8`, n=6, C_2, rings=[6]. Equal-modulus collision: χ_w has 3 distinct roots {2, ±2i}, all with |w| = 2. Generic ring-count prediction (r distinct rings) FAILS: we see ring counts [6] on a single radius. → refutes a naive 'rank ⇒ r rings' without genericity.

- `STRESS_doubleroot`: χ = `c**9 - 4*c**6 + 5*c**3 - 2`, n=9, C_3, rings=[6, 3]. Double inner root: χ_w = (w-1)²(w-2). One w-orbit appears with multiplicity 2 — constellation ring counts [6, 3] count *geometric* roots (not multiplicities). Logarithmic / resonant Stokes phenomena may appear in the analytic theory even though the geometric constellation looks tame.

- `STRESS_zeroroot`: χ = `c**4 - c**2`, n=4, C_2, rings=[2, 2]. Zero inner root: χ_w(0) = 0 → c = 0 lies on the constellation. The fibre c^q = 0 is one point with multiplicity q, *not* a regular q-gon. Constellation = [2, 2] rings; the c = 0 sector is degenerate.

- `STRESS_accidental_sym`: χ = `c**6 + 1`, n=6, C_6, rings=[6]. Accidental symmetry: χ(c) = c^6 + 1, slope 1/2 → minimal q-symmetry is C_2, but detected symmetry is **C_6** (strictly larger). This shows that 'q | C_n' is sharp only for *generic* edge coefficients; sparse χ inflates C_n.

**Critical commentary (what the picture does NOT say).** (1) Ring-count partitions discard phase information and are *not* a standard invariant of meromorphic connections; Stokes geometry depends on differences c_i − c_j, not on |c_i|. (2) The 'rank ⇒ r rings' direction needs a genericity hypothesis (distinct |w_i|), and the real-coefficient signature (Conjecture 3c from an earlier draft) is **false in general** — see STRESS_equalmod. (3) Equation-type invariance is a statement about the extraction recipe, not about the analytic operator category.
