# `reports/` — Phase reports and proof skeletons

Markdown reports documenting each computational phase, plus the
theorem/proof skeletons consolidated in Phase V.

## File index

| File                  | Bytes    | Description                                |
|-----------------------|---------:|--------------------------------------------|
| `paper_draft.md`      |   23,897 | Original Phase-V draft (now superseded by `paper/manuscript.tex`) |
| `phase3_report.md`    |   32,120 | Phase III: multi-edge, systems, nested, controlled |
| `phase4_report.md`    |   42,539 | Phase IV: analytic lifting (AT1–AT8)        |
| `phase4_ray_equivalence_report.md` | varies | Anti-Stokes ray-spacing equivalence partition of the atlas (raw + gap-invariant). |
| `slope_invariants_report.md` | varies | 23-class and 39-class atlas tables with slope multisets, Δ-partitions, μ_q stabilizer, ω-resonance, z-resonance. |
| `atlas_fingerprints.md` | varies | Series-A consolidated fingerprints (constellation shape A1 + symmetry breaking A2): ring-radius ratios, gap multisets, dendrogram, minimal distinguishing invariants, nontrivial-stabilizer roll-up. |
| `degeneracy_fingerprints/` | dir | Phase-1 stress-test stratum fingerprints (4 strata: zeroroot, doubleroot, equalmod, accidental_sym): 20-dim Vieta/codimension/incidence fingerprint addressing Phase-3 gap G15. |
| `conjectures.md`      |   24,259 | Consolidated conjecture list (M1, N1, D1–D2, …) |
| `proofs.md`           |   50,617 | Eight theorem–proof skeletons (M1, N1, D2, S1, AT1, AT3, AT5, AT7) |
| `integration_map.md`  |    4,979 | Section-by-section placement of each theorem in the paper |

## Relationship to the manuscript

The reports were the **drafting substrate**: their contents were
consolidated, polished, and integrated into `paper/manuscript.tex`
during Phase VI (manuscript assembly).

* `paper_draft.md` is the **pre-integration** draft. It documents the
  original outline before sections were renumbered or theorems
  re-stated for the camera-ready version.
* `proofs.md` contains the eight theorem proofs in **expanded form**
  (skeleton + remarks). The manuscript versions are typeset and may
  be slightly shorter for compactness, but mathematical content is
  identical.
* `integration_map.md` maps each conjecture/theorem to its target
  section in the manuscript and notes inter-theorem dependencies.

## Citation chain

When a phase report cites another phase report, the cross-reference is
of the form `[reports/phaseN_report.md §X.Y]`. When a phase report
cites a dataset artifact, the cross-reference is of the form
`[data/phaseN_artifact.json]`.

## Provenance

| Phase | Pipeline script             | Output JSONs                                    | Report             |
|-------|-----------------------------|-------------------------------------------------|--------------------|
| I+II  | `fleets/fleet.py`            | `operators.json`, `newton.json`, `chi.json`, `constellations.json`, `clusters.json`, `counterexamples.json` | (folded into Phase III) |
| III   | `fleets/fleet3.py`           | `phase3_*.json`                                  | `phase3_report.md`  |
| IV    | `fleets/fleet4.py`           | `phase4_*.json`                                  | `phase4_report.md`  |
| V     | `fleets/fleet5.py`           | `phase5_targets.json`                            | `proofs.md` + `integration_map.md` |
| VI    | (manual / AI-assisted)       | `paper/manuscript.tex`, `paper/manuscript.pdf`   | (the paper itself)  |

## Reading order

For a new reader, the recommended path is:

1. **`paper/manuscript.pdf`** — the polished theory and proofs.
2. **`reports/phase3_report.md`** — for the construction of the
   computational atlas.
3. **`reports/phase4_report.md`** — for the analytic-lifting layer.
4. **`reports/proofs.md`** — for the expanded proof skeletons (these
   contain remarks and intermediate steps omitted from the typeset
   version for compactness).
5. **`reports/integration_map.md`** — to navigate from a manuscript
   section to its underlying phase artifacts.
