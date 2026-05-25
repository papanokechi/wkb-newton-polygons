# Phase III — Deepening the WKB / Newton-Polygon Classification Theory

## 1. Structured summary of the draft theory (draft_reader)

**Title:** The WKB Geometry of Newton Polygons: A Classification Theory

**Main Theorem:** If the dominant Newton edge has slope -p/q in lowest terms and contains r+1 lattice points at (rq - jq, jp) for 0 <= j <= r, then chi(c) = chi_w(c^q) and C(L) is the mu_q-equivariant pullback bigsqcup_{w_i in Roots(chi_w)} { c : c^q = w_i }.

**Corollaries:**
- Generic ring decomposition: when the |w_i| are pairwise distinct and nonzero, C(L) is r concentric mu_q-orbits of size q.
- Vieta monodromy: under beta = alpha_r -> e^{i theta} beta, the lift sum m_k Delta_k = theta (mod 2 pi).

**Degeneracy loci:**
- discriminant {disc chi_w = 0}: multiple roots in chi_w cause ring multiplicity > q
- equal-modulus {|w_i| = |w_j|, i != j}: distinct mu_q-orbits merge into one radius with non-uniform angular distribution
- zero-root {alpha_r = 0}: c = 0 enters C(L) with multiplicity q and the dominant edge jumps

**Open problems explicitly stated in the draft:**
- Multi-edge Newton polygons and stratification by edge sequences.
- Matrix / system operators and links to wild character varieties.
- Sharp converse to the constellation classification.
- What Stokes data (phases, lines) refine F to a complete invariant.

## 2. Gaps and research directions (gap_finder)

- **G1. Multi-edge Newton polygons** — Phase 1+2 treated only the dominant edge; an operator with k > 1 edges yields a slope filtration that the present F ignores.
- **G2. 2x2 and 3x3 systems** — F is defined on scalar operators only; for systems the eigenvalue spectrum of the leading symbol generates a richer constellation.
- **G3. High-ramification slopes (q >= 5)** — All Phase-1 sweep points used q in {2,3,4}; q=5,6,7 may exhibit phenomena (number-theoretic resonance, larger automorphism groups) invisible at small q.
- **G4. Delta_ij modulus partition** — The constellation only records {c_i}; the multiset {|c_i - c_j|} is a finer invariant that survives global rotation.
- **G5. Delta_ij argument partition** — Stokes lines are determined by arg(c_i - c_j); a modulus-free angular invariant is the bridge to Stokes-graph classification.
- **G6. Z-resonance among constellation points** — Integer linear relations sum n_k c_k = 0 with small |n_k| signal accidental algebraic dependencies absent from Phase 1's clustering key.
- **G7. omega-resonance beyond mu_q** — When arg(c_i) - arg(c_j) is in 2 pi Q with denominator strictly larger than q, the constellation has additional rotational structure.
- **G8. Mixed-type operators (D + lambda S)** — Operators combining differential and difference terms test whether F's combinatorial output is genuinely equation-type-agnostic at the Newton-polygon level.
- **G9. Controlled discriminant collisions** — Phase 1 found degenerations by stress test; a parametric family approaching the discriminant locus would expose the deformation law.
- **G10. Slope-filtration interaction across edges** — For multi-edge polygons, do the per-edge constellations C_alpha algebraically interact (resonances among edges) or are they independent?
- **G11. Analytic fibres of F (equation-type discrimination)** — Phase 1 noted that the combinatorial chi is equation-type invariant but the analytic meaning of c is not; an analytic invariant distinguishing ODE/diff/q-diff is missing.
- **G12. Galois action on chi_w** — Gal(Q-bar/Q) acts on the roots w_i; this action lifts to a permutation of the rings of C(L). Phase 1 has no Galois-theoretic invariant.
- **G13. Sharpness of p-invariance** — Phase 1 conjectured the slope numerator p is invisible; in multi-edge or systems contexts this may fail (p could survive as a phase twist).
- **G14. Orbit fusion under real-coefficient pairing** — Real chi_w has conjugate root pairs of equal modulus, fusing two mu_q-orbits; this is recorded as a class but not as an invariant of F.
- **G15. Codimension count for each degeneracy stratum** — Phase 1 names 4 strata but does not specify their codimension in the alpha-coefficient space, blocking a precise stratification statement.
- **G16. Deep zero-root strata** — alpha_r = 0 alone gives multiplicity q at zero, but if alpha_r = alpha_{r-1} = 0, the constellation collapses further.
- **G17. Per-edge gauge group** — Each edge alpha admits its own leading-coefficient gauge beta_alpha; Vieta monodromy may decompose under the product of these groups.
- **G18. Inner-polynomial ramification** — chi_w itself may admit a further factorisation chi_w(w) = chi_v(w^{q'}) for some q' > 1; this is iterated mu_q-pullback structure.
- **G19. Mixed equation-type Newton polygons** — If a single operator carries both D^k and S^k terms, the Newton-polygon recipe still applies; do the resulting classes match the pure ones?
- **G20. Limit of high-rank / high-q families** — What is the asymptotic structure of C(L) as r, q -> infinity? Equidistribution on annuli? Random-matrix-like statistics?

## 3. Extended operator zoo (operator_generator)

Generated **48** operators across the following families:
  - scalar: 44
  - system: 4

**HIGHQ** (15 operators): HIGHQ_simple_s1o5_r1, HIGHQ_simple_s1o5_r2, HIGHQ_genc_s1o5_r2, HIGHQ_simple_s2o5_r2, HIGHQ_genc_s2o5_r2, HIGHQ_simple_s1o6_r1...
**MULTI** (7 operators): MULTI_edges_1o3_then_1o2, MULTI_edges_1o4_then_1o2, MULTI_edges_1o5_then_1o2, MULTI_edges_1o3_r2_then_1o2, MULTI_edges_1o4_r2_then_1o3, MULTI_edges_2o5_then_3o5...
**MULTI3** (2 operators): MULTI3_1o4_1o3_1o2, MULTI3_1o5_1o3_1o2
**SYS2** (2 operators): SYS2_1o2_1o3, SYS2_1o3_r2_genc
**SYS3** (2 operators): SYS3_1o2_1o3_1o4, SYS3_1o5_r1_x3
**MIX** (2 operators): MIX_DandS_1o3_r2, MIX_DandS_1o4_r3
**CTRL** (8 operators): CTRL_disc_eps1, CTRL_disc_eps1o5, CTRL_disc_eps1o25, CTRL_conjroots_t0, CTRL_conjroots_t1, CTRL_conjroots_t2...
**NEST** (2 operators): NEST_q3_qinner2, NEST_q2_qinner3
**GAL** (2 operators): GAL_cyclotomic_3, GAL_cyclotomic_5
**OMEGA** (2 operators): OMEGA_q2_fifth, OMEGA_q3_seventh
**PINV** (4 operators): PINV_s1o5_r2_genc, PINV_s2o5_r2_genc, PINV_s3o5_r2_genc, PINV_s4o5_r2_genc

## 4. Extended invariants (invariant_engine)

New invariants computed for every operator:
- **Delta_ij modulus and argument partitions**: the multiset of pairwise differences {c_i - c_j}, partitioned by modulus and by argument modulo 2π.
- **Z-resonance**: small integer relations Σ n_k c_k = 0 with |n_k| ≤ 3, ≤ 4 terms.
- **Omega-resonance**: smallest m so that all arg(c_i)/arg(c_j) differences are in 2π·(Z/m); flagged when m > q.
- **Symmetry inflation**: largest C_n leaving the multiset invariant; compared to the Newton-polygon-predicted C_q.
- **Multi-edge interference**: per-edge radii lists, shared-radii detection, edge-disjointness flag, zero-root count.

**Highlights from the sweep:**
- 8 operators exhibit symmetry inflation (C_n with n > q).
- 22 operators exhibit omega-resonance (angular denominator strictly larger than q).
- 33 operators admit a *cross-ring nontrivial* Z-resonance (per-ring partial sums do not individually vanish).
- 5 operators admit only mu_q-forced Z-resonances (relations lying in the Z-span of single-ring cyclotomic ideals).
- 13 operators have multi-edge Newton polygons.

## 5. New universality classes (clustering_engine)

Clustering by the extended invariant key produces **39** classes (versus 23 in Phase 1).

| Class | n | Description |
|---|---:|---|
| `P3C00` | 4 | family=scalar; edges=1; Delta-mod-partition=[5, 5, 5, 5, 5, 5, 5, 5, 5]; Delta-arg-partition=[2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_5; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False |
| `P3C01` | 2 | family=scalar; edges=1; Delta-mod-partition=[2, 2, 2]; Delta-arg-partition=[2, 2, 1, 1]; omega-resonant=True; sym C_2; nontrivial-z-relations=16; edges-disjoint=True; zero-roots=False |
| `P3C02` | 2 | family=scalar; edges=1; Delta-mod-partition=[5, 5, 5, 5, 5, 5, 5, 5, 5]; Delta-arg-partition=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_5; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False |
| `P3C03` | 2 | family=scalar; edges=1; Delta-mod-partition=[6, 6, 6, 3, 3, 3, 3, 3, 3]; Delta-arg-partition=[3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_3; nontrivial-z-relations=3; edges-disjoint=True; zero-roots=False |
| `P3C04` | 2 | family=scalar; edges=1; Delta-mod-partition=[8, 4, 4, 4, 4, 4]; Delta-arg-partition=[4, 4, 4, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]; omega-resonant=True; sym C_4; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False |
| `P3C05` | 2 | family=scalar; edges=1; Delta-mod-partition=[10, 10, 10, 10, 5]; Delta-arg-partition=[5, 5, 5, 5, 5, 4, 4, 4, 4, 4]; omega-resonant=True; sym C_10; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False |
| `P3C06` | 2 | family=scalar; edges=1; Delta-mod-partition=[12, 12, 6, 6, 6, 6, 6, 6, 6]; Delta-arg-partition=[6, 6, 6, 6, 6, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2]; omega-resonant=True; sym C_6; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False |
| `P3C07` | 1 | family=scalar; edges=1; Delta-mod-partition=[1]; Delta-arg-partition=[1]; omega-resonant=False; sym C_2; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False |
| `P3C08` | 1 | family=scalar; edges=1; Delta-mod-partition=[3]; Delta-arg-partition=[1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False |
| `P3C09` | 1 | family=scalar; edges=1; Delta-mod-partition=[3, 3, 3, 3, 3]; Delta-arg-partition=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_3; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False |
| `P3C10` | 1 | family=scalar; edges=1; Delta-mod-partition=[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2]; Delta-arg-partition=[2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_4; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False |
| `P3C11` | 1 | family=scalar; edges=1; Delta-mod-partition=[5, 5]; Delta-arg-partition=[2, 2, 2, 2, 2]; omega-resonant=False; sym C_1; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False |
| `P3C12` | 1 | family=scalar; edges=1; Delta-mod-partition=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]; Delta-arg-partition=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_5; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False |
| `P3C13` | 1 | family=scalar; edges=1; Delta-mod-partition=[6, 3, 3, 3]; Delta-arg-partition=[3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_3; nontrivial-z-relations=2; edges-disjoint=True; zero-roots=False |
| `P3C14` | 1 | family=scalar; edges=1; Delta-mod-partition=[6, 6, 3]; Delta-arg-partition=[3, 3, 3, 2, 2, 2]; omega-resonant=False; sym C_6; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False |
| `P3C15` | 1 | family=scalar; edges=1; Delta-mod-partition=[6, 6, 6, 6, 4]; Delta-arg-partition=[4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1]; omega-resonant=True; sym C_2; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False |
| `P3C16` | 1 | family=scalar; edges=1; Delta-mod-partition=[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 3, 3]; Delta-arg-partition=[3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_6; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False |
| `P3C17` | 1 | family=scalar; edges=1; Delta-mod-partition=[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 3, 3, 3]; Delta-arg-partition=[3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_6; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False |
| `P3C18` | 1 | family=scalar; edges=1; Delta-mod-partition=[7, 7, 7]; Delta-arg-partition=[3, 3, 3, 3, 3, 3, 3]; omega-resonant=False; sym C_1; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False |
| `P3C19` | 1 | family=scalar; edges=1; Delta-mod-partition=[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]; Delta-arg-partition=[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_7; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False |
| `P3C20` | 1 | family=scalar; edges=1; Delta-mod-partition=[8, 4, 4, 4, 4, 4]; Delta-arg-partition=[4, 4, 4, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_4; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False |
| `P3C21` | 1 | family=scalar; edges=1; Delta-mod-partition=[12, 12, 6, 3, 3]; Delta-arg-partition=[5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1]; omega-resonant=False; sym C_3; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False |
| `P3C22` | 1 | family=scalar; edges=1; Delta-mod-partition=[12, 12, 12, 12, 12, 6]; Delta-arg-partition=[6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 3, 3]; omega-resonant=True; sym C_12; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False |
| `P3C23` | 1 | family=scalar; edges=1; Delta-mod-partition=[14, 14, 14, 14, 14, 14, 7]; Delta-arg-partition=[7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 5, 4, 2, 2]; omega-resonant=True; sym C_14; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False |
| `P3C24` | 1 | family=scalar; edges=1; Delta-mod-partition=[15, 15, 15, 15, 15, 15, 15]; Delta-arg-partition=[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 2]; omega-resonant=True; sym C_15; nontrivial-z-relations=5; edges-disjoint=True; zero-roots=False |
| `P3C25` | 1 | family=scalar; edges=1; Delta-mod-partition=[18, 18, 18, 18, 18, 18, 18, 18, 9]; Delta-arg-partition=[9, 9, 9, 9, 8, 8, 8, 8, 8, 7, 7, 7, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1]; omega-resonant=True; sym C_18; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False |
| `P3C26` | 1 | family=scalar; edges=2; Delta-mod-partition=[9, 6, 6, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; Delta-arg-partition=[4, 4, 4, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True |
| `P3C27` | 1 | family=scalar; edges=2; Delta-mod-partition=[16, 8, 8, 6, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]; Delta-arg-partition=[6, 5, 5, 5, 5, 4, 4, 4, 4, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_2; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True |
| `P3C28` | 1 | family=scalar; edges=2; Delta-mod-partition=[18, 18, 15, 12, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; Delta-arg-partition=[15, 7, 7, 7, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True |
| `P3C29` | 1 | family=scalar; edges=2; Delta-mod-partition=[25, 10, 10, 10, 5, 5, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; Delta-arg-partition=[10, 6, 6, 5, 5, 5, 5, 5, 5, 5, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True |
| `P3C30` | 1 | family=scalar; edges=2; Delta-mod-partition=[25, 25, 25, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]; Delta-arg-partition=[10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_5; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True |
| `P3C31` | 1 | family=scalar; edges=2; Delta-mod-partition=[32, 32, 28, 24, 24, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; Delta-arg-partition=[28, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True |
| `P3C32` | 1 | family=scalar; edges=2; Delta-mod-partition=[42, 24, 24, 15, 6, 4, 4, 4, 4, 4, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]; Delta-arg-partition=[15, 9, 9, 8, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_2; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True |
| `P3C33` | 1 | family=scalar; edges=3; Delta-mod-partition=[99, 55, 6, 6, 6, 3, 3, 2, 2, 2, 2, 2, 2]; Delta-arg-partition=[55, 15, 13, 13, 11, 11, 11, 11, 11, 11, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_1; nontrivial-z-relations=30; edges-disjoint=False; zero-roots=True |
| `P3C34` | 1 | family=scalar; edges=3; Delta-mod-partition=[106, 79, 26, 26, 7, 7, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; Delta-arg-partition=[78, 14, 14, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=30; edges-disjoint=False; zero-roots=True |
| `P3C35` | 1 | family=system; edges=2; Delta-mod-partition=[3, 2, 2, 2, 1]; Delta-arg-partition=[2, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_1; nontrivial-z-relations=2; edges-disjoint=False; zero-roots=False |
| `P3C36` | 1 | family=system; edges=2; Delta-mod-partition=[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]; Delta-arg-partition=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=3; edges-disjoint=True; zero-roots=False |
| `P3C37` | 1 | family=system; edges=3; Delta-mod-partition=[6, 6, 6, 3, 3, 2, 2, 2, 2, 2, 2]; Delta-arg-partition=[4, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_1; nontrivial-z-relations=30; edges-disjoint=False; zero-roots=False |
| `P3C38` | 1 | family=system; edges=3; Delta-mod-partition=[45, 45, 15]; Delta-arg-partition=[15, 12, 12, 12, 12, 12, 6, 6, 6, 6, 6]; omega-resonant=False; sym C_1; nontrivial-z-relations=30; edges-disjoint=False; zero-roots=False |

Of these, several are *new* in the sense that they lie outside the Phase-1 atlas:
- 27 classes lie in multi-edge, omega-resonant, or system territory not covered by Phase 1.

## 6. Next-level conjectures (conjecture_engine)

### M1. Per-edge factorisation (multi-edge generalisation of the Main Theorem)

**Statement.** For a scalar operator L with Newton polygon N(L) having edges E_1, ..., E_m at the irregular singularity (ordered by increasing slope), each E_alpha of slope -p_alpha/q_alpha with r_alpha+1 lattice points contributes a characteristic polynomial chi^{(alpha)}(c) = c^{k_0^{(alpha)}} * chi_w^{(alpha)}(c^{q_alpha}). The full WKB symbol factors as the PRODUCT chi(c) = prod_alpha chi^{(alpha)}(c) and the constellation C(L) is the (multiset) DISJOINT UNION of per-edge constellations C_alpha, each obtained from chi_w^{(alpha)} by the same mu_{q_alpha}-equivariant pullback as the Main Theorem.

**Evidence.** {"n_multi_edge_operators": 9, "examples": ["MULTI_edges_1o3_then_1o2", "MULTI_edges_1o4_then_1o2", "MULTI_edges_1o5_then_1o2", "MULTI_edges_1o3_r2_then_1o2", "MULTI_edges_1o4_r2_then_1o3"], "edges_disjoint_count": 7}

**Remarks.** Independence is generic: per-edge constellations occupy distinct radii in the OPEN stratum. Equal-radius collisions between different edges define an inter-edge degeneracy locus that extends the Phase-1 single-edge stratification.

### M2. Multi-edge zero-root sharing (right-edge)

**Statement.** Let N(L) have two consecutive edges E_alpha (less negative slope) and E_beta (more negative, dominant) meeting at the joint vertex (k_*, d_*) with k_* > 0. Indexing per-edge characteristic polynomials so that the leftmost lattice point of each edge starts at k = 0, the dominant edge's chi^{(beta)}(c) factors as c^{k_*} * chi_w^{(beta)}(c^{q_beta}); the less-negative edge contributes no factor of c. Thus C_beta carries a multiplicity-k_* root at c = 0, while C_alpha generically does not. In particular, multi-edge polygons always exhibit the dominant-edge zero-root degeneracy.

**Evidence.** {"multi_edge_operators_with_dominant_zero_roots": 9, "examples": ["MULTI_edges_1o3_then_1o2", "MULTI_edges_1o4_then_1o2", "MULTI_edges_1o5_then_1o2", "MULTI_edges_1o3_r2_then_1o2", "MULTI_edges_1o4_r2_then_1o3"], "observed_per_edge_zero_root_distribution": "left edges always 0; right (dominant) edge gives k_* zeros equal to the joint k-coordinate."}

**Remarks.** Extends the Phase-1 zero-root stratum: in single-edge polygons alpha_r = 0 was an accidental degeneracy; in multi-edge polygons the zero-root is *generic* on the dominant edge, with multiplicity given by the joint vertex.

### D1. Delta-modulus partition law (open stratum)

**Statement.** For a scalar single-edge operator on the open stratum (distinct |w_i|, distinct args, no Z- or omega-resonance), the multiset of pairwise differences {|c_i - c_j| : i<j} has cardinality exactly binomial(rq, 2) = rq(rq-1)/2, and the modulus partition factors as a product of three contributions: (i) intra-ring differences indexed by pairs in mu_q, (ii) inter-ring differences indexed by pairs (w_i, w_j), (iii) a global rotation of all of (ii) by the same mu_q action. In particular, the number of DISTINCT moduli in the Delta-multiset is at most (q-1)/2 + r*q*(r-1)/2 (counting multiplicities).

**Evidence.** {"open_stratum_count": 16, "examples": ["HIGHQ_simple_s1o5_r1", "HIGHQ_simple_s1o6_r1", "HIGHQ_simple_s1o7_r1", "HIGHQ_genc_s1o5_r3", "HIGHQ_genc_s1o6_r3"], "observed_distinct_moduli": [2, 3, 3, 21, 27, 5, 18, 5, 9, 9]}

### D2. Inner-polynomial Z-resonance dichotomy (prime-q version)

**Statement.** Let L be scalar with one dominant edge of slope -p/q with q PRIME and inner polynomial chi_w of degree r >= 2, so C(L) is a disjoint union of r mu_q-orbits with radii rho_alpha = |w_alpha|^{1/q}. Call a small-coefficient (|n_k| <= 3, support <= 4) Z-relation sum n_k c_k = 0 *mu_q-forced* if its per-ring partial sums each vanish individually; otherwise call it *cross-ring nontrivial*. Then: (i) for GENERIC chi_w (the w_alpha algebraically independent over Q), C(L) admits no cross-ring nontrivial Z-relation; (ii) for SIMPLE chi_w (the w_alpha satisfying a Q-linear relation), C(L) admits cross-ring nontrivial Z-relations -- one for each independent Q-linear dependence among the q-th roots w_alpha^{1/q}. For COMPOSITE q the same statement holds modulo the cyclotomic relations of mu_q acting on each ring (the mu_q-forced piece is correspondingly richer and includes Z-combinations of single-ring sub-orbit sums).

**Evidence.** {"operators_with_nontrivial_z": 33, "operators_with_only_mu_q_forced_z": 5, "operators_with_no_z": 10, "prime_q_genc_operators": 4, "prime_q_genc_with_zero_nontrivial_Z": 4, "simple_multiring_with_Z": 6, "examples_prime_q_genc_no_Z": ["HIGHQ_genc_s1o5_r2", "HIGHQ_genc_s2o5_r2", "HIGHQ_genc_s3o7_r2", "HIGHQ_genc_s1o5_r3"], "examples_simple_with_Z": ["HIGHQ_simple_s1o5_r2", "HIGHQ_simple_s2o5_r2", "HIGHQ_simple_s1o6_r2", "HIGHQ_simple_s3o7_r2", "HIGHQ_simple_s1o5_r3"], "sharpness": "All prime-q (q=5 or 7) generic-chi_w single-edge operators produce zero cross-ring Z-relations; every simple-chi_w multi-ring operator produces at least 5. The dichotomy is exact for prime q in the sweep."}

**Remarks.** Cross-ring Z-relations form a *lattice* in C(L) - C(L) that is invariant of the chi_w-stratum: operators on the same chi_w-stratum share their cross-ring Z-resonance lattice. This lattice is a finer invariant than mu_q symmetry and refines D1's modulus partition into an arithmetic stratification of F.

### O1. Omega-resonance classification

**Statement.** The constellation C(L) has angular spacing in 2 pi * (Z/m) with m > q if and only if chi_w has roots on a finite Galois orbit of (Z/m)^x distinct from the trivial mu_q-orbit. Equivalently: omega-resonance is equivalent to chi_w factoring as a product of cyclotomic-like polynomials in w whose roots have a common rational angular spacing.

**Evidence.** {"omega_resonant_count": 22, "examples": ["HIGHQ_simple_s1o5_r2", "HIGHQ_genc_s1o5_r2", "HIGHQ_simple_s2o5_r2", "HIGHQ_genc_s2o5_r2", "HIGHQ_simple_s1o6_r2"], "observed_denoms": [6, 10, 12, 14, 15, 16, 18, 21, 24]}

**Remarks.** This is the 'accidental symmetry' phenomenon of Phase 1 elevated to a precise structural law: the symmetry-inflation factor m / q is exactly the LCM of the inner Galois orbits' angular denominators.

### S1. System pullback: blocks act independently on F

**Statement.** For a block-diagonal system Phi = diag(L_1, ..., L_n) of scalar operators, the constellation C(Phi) is the multiset disjoint union of C(L_i). Hence F(Phi) = bigsqcup_i F(L_i), and F factors through the symmetric power: F : Sys^n(scalar local models) -> Sym^n( finite multisets in C ).

**Evidence.** {"system_operators": 4, "examples": ["SYS2_1o2_1o3", "SYS2_1o3_r2_genc", "SYS3_1o2_1o3_1o4", "SYS3_1o5_r1_x3"]}

**Remarks.** This handles block-diagonal systems exactly; for general (coupled) systems the same disjoint-union statement holds after diagonalisation of the leading symbol when the eigenvalues are distinct; coalescence of eigenvalues defines a system-level discriminant stratum, conjecturally classified by Levelt-Turrittin decomposition.

### P1. p-invariance of the Delta-modulus partition (verified for q=5)

**Statement.** Fixing q and r, varying p in {1, 2, 3, 4} (all coprime to 5) while keeping chi_w fixed produces operators with IDENTICAL Delta-modulus partitions and identical C_n symmetry orders. Hence the slope numerator p is invisible to the Delta-invariant as well as to F itself.

**Evidence.** {"pinv_examples": ["PINV_s1o5_r2_genc", "PINV_s2o5_r2_genc", "PINV_s3o5_r2_genc", "PINV_s4o5_r2_genc"], "all_signatures_equal": true, "common_signature": [5, 5, 5, 5, 5, 5, 5, 5, 5]}

**Remarks.** Phase 1 conjectured this for F (the constellation); Phase 3 elevates it to the finer Delta-invariant.

### N1. Nested ramification: iterated mu_q-pullback

**Statement.** If chi_w(w) itself factors as chi_v(w^{q'}) for some q' > 1 (i.e. chi_w has only exponents in q' Z), then C(L) = bigsqcup_{v in Roots(chi_v)} { c : c^{q q'} = v }, exhibiting (mu_q x mu_{q'})-equivariance. The effective ramification is q q' and the apparent symmetry group is C_{q q'}, even though the Newton polygon advertises only q.

**Evidence.** {"nested_examples": ["NEST_q3_qinner2", "NEST_q2_qinner3"], "observed_symmetries": [["NEST_q3_qinner2", 6], ["NEST_q2_qinner3", 6]]}

**Remarks.** This is the iterated form of the Main Theorem; it explains 'hidden' symmetry inflation in chi without invoking a Newton-polygon refinement.

### F1. Slope-filtration target for multi-edge F

**Statement.** F extends to multi-edge scalar operators with target = the category of FILTERED multisets in C (ordered by the slope sequence of N(L)). The grading captures the asymptotic dominance: an exponent c in C_alpha (slope -p_alpha/q_alpha) controls the WKB solution at order x^{p_alpha/q_alpha}. The single-edge classification of Phase 1 is the associated-graded of this filtration on each stratum.

**Evidence.** {"multi_edge_operators": 9}

**Remarks.** This is the natural functorial reframing of multi-edge as a filtration whose graded pieces are Phase-1 classes.

### G1. Galois action on rings

**Statement.** The absolute Galois group Gal(Q-bar/Q) acts on the roots of chi_w; this action lifts uniquely to a permutation of the rings R_k of C(L) covering the mu_q action. The orbit structure of Gal on rings is an arithmetic invariant of F refining the modulus partition.

**Evidence.** {"galois_examples": ["GAL_cyclotomic_3", "GAL_cyclotomic_5"], "observed_omega_denoms": [["GAL_cyclotomic_3", 6], ["GAL_cyclotomic_5", 10]]}

**Remarks.** When chi_w is irreducible over Q, all rings form a single Galois orbit; when chi_w factors, the rings split according to the factorisation. GAL_cyclotomic_3 / 5 give cyclotomic ring orbits with omega-resonance denominators 6 / 10 respectively.

## 7. How Phase III extends the classification theory

The Phase-1+2 theory described F as a functor from single-edge scalar local models to multisets in C, with image stratified by 23 constellation classes. Phase III enlarges F in **four** dimensions:

1. **Source category enlarged** — to multi-edge scalar operators (via the per-edge factorisation law M1) and to block-diagonal systems (via the system-pullback law S1). The latter exhibits F as compatible with `Sym^n`-product structure.
2. **Target enriched with a slope filtration** — multi-edge constellations are no longer flat multisets but *filtered* multisets graded by Newton-polygon slope (F1). Phase-1 classes are recovered as the associated graded pieces.
3. **Finer invariants on the target side** — the Delta_{ij} modulus and argument partitions (D1), Z-resonance signatures (D2), omega-resonance denominators (O1), and Galois orbit structure on rings (G1) all refine the constellation invariant. These bring F into contact with Stokes-graph and spectral-network combinatorics, which depend on differences c_i - c_j rather than the c_i themselves.
4. **Iterated ramification** — chi_w may itself admit a mu_{q'}-pullback structure (N1), producing apparent symmetry C_{q q'} with only C_q visible from the Newton polygon. This is the precise structural mechanism behind the Phase-1 'accidental symmetry' phenomenon.

The combined result: F factors as a tower

    F : { multi-edge scalar / system local models } -> { filtered Galois-equivariant multisets in C }

with each layer of refinement (multi-edge -> slope-filtration; chi_w -> nested ramification; Delta_ij -> Stokes adjacency) introducing exactly one new universal stratum. The 23 Phase-1 classes describe the simplest layer (single edge, no resonance, no inflation); the additional classes catalogued here populate the deeper layers in a uniform combinatorial language.
