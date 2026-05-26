# Slope-based invariants across the WKB Newton-polygon atlas

Per-class slope multisets, gcd(p,q) structure, and ramification depth
for both the 23-class base atlas and the 39-class μ_q / μ_q′
refinement. Classes are then clustered by their slope fingerprint.


## 23-class base atlas (`clusters.json`)

| ID | Label | Slope multiset | gcd structure | Ramification depth (global) | n_edges |
|---|---|---|---|---|---|
| — | Class[Regular-12-gon] | 1/4×1 | 1×1 | 4×1 | 1×1 |
| — | Class[Regular-9-gon] | 1/3×1, 2/3×1 | 1×2 | 3×2 | 1×2 |
| — | Class[Regular-8-gon] | 1/4×3 | 1×3 | 4×3 | 1×3 |
| — | Class[Regular-6-gon] | 1/2×2, 1/3×3, 2/3×3, 3/2×1 | 1×9 | 2×3, 3×6 | 1×9 |
| — | Class[Regular-4-gon] | 1/2×3, 1/4×3, 3/2×3 | 1×9 | 2×6, 4×3 | 1×9 |
| — | Class[C4, rings=[4, 4]] | 1/4×6 | 1×6 | 4×6 | 1×6 |
| — | Class[C4, rings=[4, 4, 4]] | 1/4×1 | 1×1 | 4×1 | 1×1 |
| — | Class[C4, rings=[4, 8]] | 1/4×1 | 1×1 | 4×1 | 1×1 |
| — | Class[C4, rings=[8]] | 1/4×1 | 1×1 | 4×1 | 1×1 |
| — | Class[C4, rings=[8, 4]] | 1/4×1 | 1×1 | 4×1 | 1×1 |
| — | Class[Regular-3-gon] | 1/3×3, 2/3×3 | 1×6 | 3×6 | 1×6 |
| — | Class[C3, rings=[3, 3]] | 1/3×6, 2/3×6 | 1×12 | 3×12 | 1×12 |
| — | Class[C3, rings=[3, 3, 3]] | 1/3×1, 2/3×1 | 1×2 | 3×2 | 1×2 |
| — | Class[C3, rings=[3, 6]] | 1/3×1, 2/3×1 | 1×2 | 3×2 | 1×2 |
| — | Class[C3, rings=[6]] | 1/3×1, 2/3×1 | 1×2 | 3×2 | 1×2 |
| — | Class[C3, rings=[6, 3]] | 1/3×2, 2/3×1 | 1×3 | 3×3 | 1×3 |
| — | Class[Regular-2-gon] | 1/2×3, 3/2×3 | 1×6 | 2×6 | 1×6 |
| — | Class[C2, rings=[2, 2]] | 1/2×7, 3/2×6 | 1×13 | 2×13 | 1×13 |
| — | Class[C2, rings=[2, 2, 2]] | 1/2×1, 3/2×1 | 1×2 | 2×2 | 1×2 |
| — | Class[C2, rings=[2, 4]] | 1/2×1, 3/2×1 | 1×2 | 2×2 | 1×2 |
| — | Class[C2, rings=[4]] | 1/2×1, 3/2×1 | 1×2 | 2×2 | 1×2 |
| — | Class[C2, rings=[4, 2]] | 1/2×1, 3/2×1 | 1×2 | 2×2 | 1×2 |
| — | Class[C2, rings=[6]] | 1/2×1 | 1×1 | 2×1 | 1×1 |

## 39-class refined atlas (`phase3_clusters.json`)

| ID | Label | Slope multiset | gcd structure | Ramification depth (global) | n_edges |
|---|---|---|---|---|---|
| P3C00 | family=scalar; edges=1; Delta-mod-partition=[5, 5, 5, 5, 5, 5, 5, 5, 5]; Delta-arg-partition=[2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_5; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False | 1/5×1, 2/5×1, 3/5×1, 4/5×1 | 1×4 | 5×4 | 1×4 |
| P3C01 | family=scalar; edges=1; Delta-mod-partition=[2, 2, 2]; Delta-arg-partition=[2, 2, 1, 1]; omega-resonant=True; sym C_2; nontrivial-z-relations=16; edges-disjoint=True; zero-roots=False | 1/2×2 | 1×2 | 2×2 | 1×2 |
| P3C02 | family=scalar; edges=1; Delta-mod-partition=[5, 5, 5, 5, 5, 5, 5, 5, 5]; Delta-arg-partition=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_5; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False | 1/5×1, 2/5×1 | 1×2 | 5×2 | 1×2 |
| P3C03 | family=scalar; edges=1; Delta-mod-partition=[6, 6, 6, 3, 3, 3, 3, 3, 3]; Delta-arg-partition=[3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_3; nontrivial-z-relations=3; edges-disjoint=True; zero-roots=False | 1/3×2 | 1×2 | 3×2 | 1×2 |
| P3C04 | family=scalar; edges=1; Delta-mod-partition=[8, 4, 4, 4, 4, 4]; Delta-arg-partition=[4, 4, 4, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]; omega-resonant=True; sym C_4; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False | 1/4×2 | 1×2 | 4×2 | 1×2 |
| P3C05 | family=scalar; edges=1; Delta-mod-partition=[10, 10, 10, 10, 5]; Delta-arg-partition=[5, 5, 5, 5, 5, 4, 4, 4, 4, 4]; omega-resonant=True; sym C_10; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False | 1/5×1, 2/5×1 | 1×2 | 5×2 | 1×2 |
| P3C06 | family=scalar; edges=1; Delta-mod-partition=[12, 12, 6, 6, 6, 6, 6, 6, 6]; Delta-arg-partition=[6, 6, 6, 6, 6, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2]; omega-resonant=True; sym C_6; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False | 1/2×1, 1/3×1 | 1×2 | 2×1, 3×1 | 1×2 |
| P3C07 | family=scalar; edges=1; Delta-mod-partition=[1]; Delta-arg-partition=[1]; omega-resonant=False; sym C_2; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False | 1/2×1 | 1×1 | 2×1 | 1×1 |
| P3C08 | family=scalar; edges=1; Delta-mod-partition=[3]; Delta-arg-partition=[1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False | 1/3×1 | 1×1 | 3×1 | 1×1 |
| P3C09 | family=scalar; edges=1; Delta-mod-partition=[3, 3, 3, 3, 3]; Delta-arg-partition=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_3; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False | 1/3×1 | 1×1 | 3×1 | 1×1 |
| P3C10 | family=scalar; edges=1; Delta-mod-partition=[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2]; Delta-arg-partition=[2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_4; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False | 1/4×1 | 1×1 | 4×1 | 1×1 |
| P3C11 | family=scalar; edges=1; Delta-mod-partition=[5, 5]; Delta-arg-partition=[2, 2, 2, 2, 2]; omega-resonant=False; sym C_1; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False | 1/5×1 | 1×1 | 5×1 | 1×1 |
| P3C12 | family=scalar; edges=1; Delta-mod-partition=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]; Delta-arg-partition=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_5; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False | 1/5×1 | 1×1 | 5×1 | 1×1 |
| P3C13 | family=scalar; edges=1; Delta-mod-partition=[6, 3, 3, 3]; Delta-arg-partition=[3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_3; nontrivial-z-relations=2; edges-disjoint=True; zero-roots=False | 1/3×1 | 1×1 | 3×1 | 1×1 |
| P3C14 | family=scalar; edges=1; Delta-mod-partition=[6, 6, 3]; Delta-arg-partition=[3, 3, 3, 2, 2, 2]; omega-resonant=False; sym C_6; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False | 1/6×1 | 1×1 | 6×1 | 1×1 |
| P3C15 | family=scalar; edges=1; Delta-mod-partition=[6, 6, 6, 6, 4]; Delta-arg-partition=[4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1]; omega-resonant=True; sym C_2; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False | 1/2×1 | 1×1 | 2×1 | 1×1 |
| P3C16 | family=scalar; edges=1; Delta-mod-partition=[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 3, 3]; Delta-arg-partition=[3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_6; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False | 1/6×1 | 1×1 | 6×1 | 1×1 |
| P3C17 | family=scalar; edges=1; Delta-mod-partition=[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 3, 3, 3]; Delta-arg-partition=[3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_6; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False | 1/6×1 | 1×1 | 6×1 | 1×1 |
| P3C18 | family=scalar; edges=1; Delta-mod-partition=[7, 7, 7]; Delta-arg-partition=[3, 3, 3, 3, 3, 3, 3]; omega-resonant=False; sym C_1; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False | 1/7×1 | 1×1 | 7×1 | 1×1 |
| P3C19 | family=scalar; edges=1; Delta-mod-partition=[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]; Delta-arg-partition=[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_7; nontrivial-z-relations=0; edges-disjoint=True; zero-roots=False | 3/7×1 | 1×1 | 7×1 | 1×1 |
| P3C20 | family=scalar; edges=1; Delta-mod-partition=[8, 4, 4, 4, 4, 4]; Delta-arg-partition=[4, 4, 4, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_4; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False | 1/4×1 | 1×1 | 4×1 | 1×1 |
| P3C21 | family=scalar; edges=1; Delta-mod-partition=[12, 12, 6, 3, 3]; Delta-arg-partition=[5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1]; omega-resonant=False; sym C_3; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False | 1/3×1 | 1×1 | 3×1 | 1×1 |
| P3C22 | family=scalar; edges=1; Delta-mod-partition=[12, 12, 12, 12, 12, 6]; Delta-arg-partition=[6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 3, 3]; omega-resonant=True; sym C_12; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False | 1/6×1 | 1×1 | 6×1 | 1×1 |
| P3C23 | family=scalar; edges=1; Delta-mod-partition=[14, 14, 14, 14, 14, 14, 7]; Delta-arg-partition=[7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 5, 4, 2, 2]; omega-resonant=True; sym C_14; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False | 3/7×1 | 1×1 | 7×1 | 1×1 |
| P3C24 | family=scalar; edges=1; Delta-mod-partition=[15, 15, 15, 15, 15, 15, 15]; Delta-arg-partition=[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 2]; omega-resonant=True; sym C_15; nontrivial-z-relations=5; edges-disjoint=True; zero-roots=False | 1/5×1 | 1×1 | 5×1 | 1×1 |
| P3C25 | family=scalar; edges=1; Delta-mod-partition=[18, 18, 18, 18, 18, 18, 18, 18, 9]; Delta-arg-partition=[9, 9, 9, 9, 8, 8, 8, 8, 8, 7, 7, 7, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1]; omega-resonant=True; sym C_18; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=False | 1/6×1 | 1×1 | 6×1 | 1×1 |
| P3C26 | family=scalar; edges=2; Delta-mod-partition=[9, 6, 6, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; Delta-arg-partition=[4, 4, 4, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True | 1/2×1, 1/3×1 | 1×2 | 6×1 | 2×1 |
| P3C27 | family=scalar; edges=2; Delta-mod-partition=[16, 8, 8, 6, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]; Delta-arg-partition=[6, 5, 5, 5, 5, 4, 4, 4, 4, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_2; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True | 1/2×1, 1/4×1 | 1×2 | 4×1 | 2×1 |
| P3C28 | family=scalar; edges=2; Delta-mod-partition=[18, 18, 15, 12, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; Delta-arg-partition=[15, 7, 7, 7, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True | 1/2×1, 1/3×1 | 1×2 | 6×1 | 2×1 |
| P3C29 | family=scalar; edges=2; Delta-mod-partition=[25, 10, 10, 10, 5, 5, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; Delta-arg-partition=[10, 6, 6, 5, 5, 5, 5, 5, 5, 5, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True | 1/2×1, 1/5×1 | 1×2 | 10×1 | 2×1 |
| P3C30 | family=scalar; edges=2; Delta-mod-partition=[25, 25, 25, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]; Delta-arg-partition=[10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_5; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True | 2/5×1, 3/5×1 | 1×2 | 5×1 | 2×1 |
| P3C31 | family=scalar; edges=2; Delta-mod-partition=[32, 32, 28, 24, 24, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; Delta-arg-partition=[28, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True | 1/3×1, 1/4×1 | 1×2 | 12×1 | 2×1 |
| P3C32 | family=scalar; edges=2; Delta-mod-partition=[42, 24, 24, 15, 6, 4, 4, 4, 4, 4, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]; Delta-arg-partition=[15, 9, 9, 8, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_2; nontrivial-z-relations=30; edges-disjoint=True; zero-roots=True | 1/4×1, 1/6×1 | 1×2 | 12×1 | 2×1 |
| P3C33 | family=scalar; edges=3; Delta-mod-partition=[99, 55, 6, 6, 6, 3, 3, 2, 2, 2, 2, 2, 2]; Delta-arg-partition=[55, 15, 13, 13, 11, 11, 11, 11, 11, 11, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_1; nontrivial-z-relations=30; edges-disjoint=False; zero-roots=True | 1/2×1, 1/3×1, 1/4×1 | 1×3 | 12×1 | 3×1 |
| P3C34 | family=scalar; edges=3; Delta-mod-partition=[106, 79, 26, 26, 7, 7, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; Delta-arg-partition=[78, 14, 14, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=30; edges-disjoint=False; zero-roots=True | 1/2×1, 1/3×1, 1/5×1 | 1×3 | 30×1 | 3×1 |
| P3C35 | family=system; edges=2; Delta-mod-partition=[3, 2, 2, 2, 1]; Delta-arg-partition=[2, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_1; nontrivial-z-relations=2; edges-disjoint=False; zero-roots=False | 1/2×1, 1/3×1 | 1×2 | 6×1 | 2×1 |
| P3C36 | family=system; edges=2; Delta-mod-partition=[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]; Delta-arg-partition=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=False; sym C_1; nontrivial-z-relations=3; edges-disjoint=True; zero-roots=False | 1/3×2 | 1×2 | 3×1 | 2×1 |
| P3C37 | family=system; edges=3; Delta-mod-partition=[6, 6, 6, 3, 3, 2, 2, 2, 2, 2, 2]; Delta-arg-partition=[4, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]; omega-resonant=True; sym C_1; nontrivial-z-relations=30; edges-disjoint=False; zero-roots=False | 1/2×1, 1/3×1, 1/4×1 | 1×3 | 12×1 | 3×1 |
| P3C38 | family=system; edges=3; Delta-mod-partition=[45, 45, 15]; Delta-arg-partition=[15, 12, 12, 12, 12, 12, 6, 6, 6, 6, 6]; omega-resonant=False; sym C_1; nontrivial-z-relations=30; edges-disjoint=False; zero-roots=False | 1/5×1, 2/5×1, 3/5×1 | 1×3 | 5×1 | 3×1 |

## Fingerprint clusters — 23-class atlas

| # classes | Slope multiset | Global-depth multiset | n_edges multiset | Class IDs / labels |
|---:|---|---|---|---|
| 5 | 1/4×1 | 4×1 | 1×1 | Class[Regular-12-gon]; Class[C4, rings=[4, 4, 4]]; Class[C4, rings=[4, 8]]; Class[C4, rings=[8]]; Class[C4, rings=[8, 4]] |
| 4 | 1/2×1, 3/2×1 | 2×2 | 1×2 | Class[C2, rings=[2, 2, 2]]; Class[C2, rings=[2, 4]]; Class[C2, rings=[4]]; Class[C2, rings=[4, 2]] |
| 4 | 1/3×1, 2/3×1 | 3×2 | 1×2 | Class[Regular-9-gon]; Class[C3, rings=[3, 3, 3]]; Class[C3, rings=[3, 6]]; Class[C3, rings=[6]] |
| 1 | 1/2×1 | 2×1 | 1×1 | Class[C2, rings=[6]] |
| 1 | 1/2×2, 1/3×3, 2/3×3, 3/2×1 | 2×3, 3×6 | 1×9 | Class[Regular-6-gon] |
| 1 | 1/2×3, 1/4×3, 3/2×3 | 2×6, 4×3 | 1×9 | Class[Regular-4-gon] |
| 1 | 1/2×3, 3/2×3 | 2×6 | 1×6 | Class[Regular-2-gon] |
| 1 | 1/2×7, 3/2×6 | 2×13 | 1×13 | Class[C2, rings=[2, 2]] |
| 1 | 1/3×2, 2/3×1 | 3×3 | 1×3 | Class[C3, rings=[6, 3]] |
| 1 | 1/3×3, 2/3×3 | 3×6 | 1×6 | Class[Regular-3-gon] |
| 1 | 1/3×6, 2/3×6 | 3×12 | 1×12 | Class[C3, rings=[3, 3]] |
| 1 | 1/4×3 | 4×3 | 1×3 | Class[Regular-8-gon] |
| 1 | 1/4×6 | 4×6 | 1×6 | Class[C4, rings=[4, 4]] |

## Fingerprint clusters — 39-class refined atlas

| # classes | Slope multiset | Global-depth multiset | n_edges multiset | Class IDs / labels |
|---:|---|---|---|---|
| 5 | 1/6×1 | 6×1 | 1×1 | P3C14, P3C16, P3C17, P3C22, P3C25 |
| 4 | 1/3×1 | 3×1 | 1×1 | P3C08, P3C09, P3C13, P3C21 |
| 3 | 1/2×1, 1/3×1 | 6×1 | 2×1 | P3C26, P3C28, P3C35 |
| 3 | 1/5×1 | 5×1 | 1×1 | P3C11, P3C12, P3C24 |
| 2 | 1/2×1 | 2×1 | 1×1 | P3C07, P3C15 |
| 2 | 1/2×1, 1/3×1, 1/4×1 | 12×1 | 3×1 | P3C33, P3C37 |
| 2 | 1/4×1 | 4×1 | 1×1 | P3C10, P3C20 |
| 2 | 1/5×1, 2/5×1 | 5×2 | 1×2 | P3C02, P3C05 |
| 2 | 3/7×1 | 7×1 | 1×1 | P3C19, P3C23 |
| 1 | 1/2×1, 1/3×1 | 2×1, 3×1 | 1×2 | P3C06 |
| 1 | 1/2×1, 1/3×1, 1/5×1 | 30×1 | 3×1 | P3C34 |
| 1 | 1/2×1, 1/4×1 | 4×1 | 2×1 | P3C27 |
| 1 | 1/2×1, 1/5×1 | 10×1 | 2×1 | P3C29 |
| 1 | 1/2×2 | 2×2 | 1×2 | P3C01 |
| 1 | 1/3×1, 1/4×1 | 12×1 | 2×1 | P3C31 |
| 1 | 1/3×2 | 3×2 | 1×2 | P3C03 |
| 1 | 1/3×2 | 3×1 | 2×1 | P3C36 |
| 1 | 1/4×1, 1/6×1 | 12×1 | 2×1 | P3C32 |
| 1 | 1/4×2 | 4×2 | 1×2 | P3C04 |
| 1 | 1/5×1, 2/5×1, 3/5×1 | 5×1 | 3×1 | P3C38 |
| 1 | 1/5×1, 2/5×1, 3/5×1, 4/5×1 | 5×4 | 1×4 | P3C00 |
| 1 | 1/7×1 | 7×1 | 1×1 | P3C18 |
| 1 | 2/5×1, 3/5×1 | 5×1 | 2×1 | P3C30 |

## Collision summary

* 23-class atlas: 3 fingerprint buckets contain >1 class (i.e. distinct classes share the same slope fingerprint).
* 39-class atlas: 9 fingerprint buckets contain >1 class.


### Notable 23-class collisions

- slopes [1/4×1], depths [4×1] → 5 classes: Class[Regular-12-gon]; Class[C4, rings=[4, 4, 4]]; Class[C4, rings=[4, 8]]; Class[C4, rings=[8]]; Class[C4, rings=[8, 4]]
- slopes [1/2×1, 3/2×1], depths [2×2] → 4 classes: Class[C2, rings=[2, 2, 2]]; Class[C2, rings=[2, 4]]; Class[C2, rings=[4]]; Class[C2, rings=[4, 2]]
- slopes [1/3×1, 2/3×1], depths [3×2] → 4 classes: Class[Regular-9-gon]; Class[C3, rings=[3, 3, 3]]; Class[C3, rings=[3, 6]]; Class[C3, rings=[6]]

### Notable 39-class refined collisions

- slopes [1/6×1], depths [6×1] → 5 classes: P3C14, P3C16, P3C17, P3C22, P3C25
- slopes [1/3×1], depths [3×1] → 4 classes: P3C08, P3C09, P3C13, P3C21
- slopes [1/2×1, 1/3×1], depths [6×1] → 3 classes: P3C26, P3C28, P3C35
- slopes [1/5×1], depths [5×1] → 3 classes: P3C11, P3C12, P3C24
- slopes [1/2×1], depths [2×1] → 2 classes: P3C07, P3C15
- slopes [1/2×1, 1/3×1, 1/4×1], depths [12×1] → 2 classes: P3C33, P3C37
- slopes [1/4×1], depths [4×1] → 2 classes: P3C10, P3C20
- slopes [1/5×1, 2/5×1], depths [5×2] → 2 classes: P3C02, P3C05
- slopes [3/7×1], depths [7×1] → 2 classes: P3C19, P3C23
