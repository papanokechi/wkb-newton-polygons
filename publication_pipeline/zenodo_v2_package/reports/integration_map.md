# Integration Map: `proofs.md` $\to$ paper

This file records where each of the 8 theorem-proof blocks in `proofs.md` should
be inserted into "The WKB Geometry of Newton Polygons: A Classification Theory".
It also records cross-references, figure dependencies, and inter-theorem
dependencies.

## Paper section structure (target)

Following the existing draft (`paper_draft.md`) and natural extension:

* **§1.** Introduction & overview.
* **§2.** Notation, Newton polygons, WKB symbol.
* **§3.** The Main Theorem ($\chi(c) = \chi_w(c^q)$, single-edge).
* **§4.** Multi-edge generalisation; nested ramification.
* **§5.** Degeneracy strata and arithmetic stratification ($\chi_w$-strata).
* **§6.** Systems and the symmetric-power factorisation.
* **§7.** Analytic lifting: anti-Stokes skeleton and slope filtration.
* **§8.** Difference / q-difference parallels (deferred).
* **§9.** Constellation zoo, taxonomy, related work, vision.

## Placement table

| Thm | Title | Target § | Cross-refs | Phase evidence | Depends on |
|-----|-------|----------|------------|----------------|-----------|
| M1 | Per-edge factorisation | §4 | Fig. constellation zoo (multi-edge panels); Phase-III `M1` block | `MULTI_*` ops, `phase3_conjectures.json#M1` | Main Theorem |
| N1 | Nested ramification | §4 | Constellation diagram for `NEST_*` | `phase3_conjectures.json#N1` | Main Theorem |
| D2 | Z-resonance dichotomy (prime $q$) | §5 | Cross-ring partition table; Phase-III sharpness numbers | `phase3_conjectures.json#D2`; 4 prime-$q$ generic ops + 6 simple-$\chi_w$ ops | Main Theorem, Cor. 1 |
| S1 | System pullback | §6 | Block-diagonal system diagram | `SYS2_*`, `SYS3_*`; `phase3_conjectures.json#S1` | Main Theorem |
| AT1 | Anti-Stokes $\leftrightarrow$ $\arg \Delta_{ij}$ | §7 | Stokes-graph figure; cover/base diagram | `phase4_stokes.json` (11 open-stratum ops, ratio 1.000) | Main Thm, Levelt-Turrittin |
| AT3 | Nested ramification: $\mu_{q'}$ on wild data | §7 | Constellation+symmetry diagram for `NEST_*` | `phase4_consistency.json` NEST entries | N1, AT1, Levelt-Turrittin |
| AT5 | Multi-edge slope filtration | §7 | Slope-filtration figure (per-edge + cross-edge ray diagram) | `phase4_stokes.json` MULTI* entries | M1, AT1 |
| AT7 | $p$-visibility | §7 | PINV verification table (4 panels: $p = 1, 2, 3, 4$) | `phase4_stokes.json` PINV entries (70, 140, 210, 280) | AT1, P1 (Phase-III) |

## Inter-theorem dependency graph

```
Main Theorem (paper_draft §3)
   |
   +-- M1 (multi-edge factorisation)  -----+
   |                                       |
   +-- N1 (nested ramification)            |
   |       |                               |
   |       +-- AT3 (nested wild symmetry)  |
   |                                       v
   +-- AT1 (anti-Stokes / Δ_ij)          AT5 (multi-edge slope filtration)
   |       |
   |       +-- AT7 (p-visibility)
   |
   +-- D2 (Z-resonance dichotomy)
   |
   +-- S1 (system pullback)
```

## Insertion checklist

* **§3 Main Theorem.** Reference `\\mathrm{LC}_\\infty` definition is needed in §2;
  ensure §3 cites it correctly. Add forward reference to M1 / N1 in the Remarks block of §3.
* **§4 Multi-edge & nested.** Place M1 first (it sets up the slope decomposition).
  Then N1 as a sub-result of the Main Theorem applied to nested inner polynomials.
* **§5 Degeneracy strata.** D2 is the centrepiece. Add an arithmetic-classification
  paragraph distinguishing the chi_w-strata (D2 case (i) vs (ii)) and place the
  Phase-III dichotomy numbers in a table.
* **§6 Systems.** S1 is short; place after the block-diagonal vs coupled distinction.
  Note the coupled-system extension as future work (referencing Boalch).
* **§7 Analytic lifting.** Place AT1 first (open-stratum baseline). Then AT3 (after
  N1), AT5 (after M1, AT1), AT7 (after AT1). Open-stratum hypotheses (OS1)-(OS5)
  should be stated at the start of §7 and referenced.
* **§8 Difference / q-difference.** Brief restatement of M1, N1, D2, S1 in those
  settings, with citations to Birkhoff-Trjitzinsky and Ramis.

## Figures / artifacts

* `constellations.png`: 23-class taxonomy used in §3.
* (To produce) Slope-filtration diagram for AT5.
* (To produce) PINV verification table for AT7 (4 panels showing distinct anti-Stokes
  ray patterns for $p = 1, 2, 3, 4$).
* (To produce) Nested-ramification diagram showing constellation + $\mu_{q'}$-symmetry
  for AT3.

## Cross-validation

Before paper-finalisation, run a consistency check:
* Each theorem in `proofs.md` must match its Phase-III conjecture / Phase-IV theorem
  by hypothesis tightness (i.e.\ no statement weaker than its source).
* Each counterexample in `counterexamples.json` must appear in the
  "Counterexamples / sharpness boundary" block of the relevant theorem.
* Each Phase-III/IV evidence pointer must reference a real artefact under
  `files/phase{3,4}_*.json`.
