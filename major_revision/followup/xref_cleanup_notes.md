# Cross-reference cleanup notes (Round-2 follow-up)

This document records the cross-reference and dataset-identifier hygiene
work performed in the Round-2 follow-up patch.

## 1. (OS3) cross-reference in Theorem 7.1, Step 4

The Round-1 patch sharpened (OS3) — the third open-stratum hypothesis in
\Cref{ssec:OS} — to explicitly exclude *cross-ring* coincidences in the
multiset $\{\arg \Dij \mod \pi/p\}$, retaining only ring-forced
coincidences.

Step 4 of the proof of \Cref{thm:AT1} now refers to the sharpened (OS3)
explicitly:

> Under the sharpened (OS3) of \Cref{ssec:OS}, no such collisions occur
> beyond those forced by the $\mu_q$-ring structure on $\Cl(L)$.

(Previously: "Under (OS3), no such collisions occur beyond those forced
by the ring structure.")

## 2. Dataset-identifier removal

All dataset-internal identifiers of the form `STRESS_<name>`,
`MULTI_edges_…`, `NEST_q<m>_qinner<n>`, `CTRL_<…>`, `OMEGA_<…>`,
`GAL_<…>`, and references to specific filename `phase4_stokes.json`,
`phase3_invariants.json`, `clusters.json`, `constellations.json`,
`taxonomy.txt`, `plot_constellations.py` have been removed from the
prose of `paper.tex`.

Specifically:
- §3.5 (\Cref{rem:degenerate}) — `\texttt{STRESS\_equalmod}` → "equal-modulus stratum (e.g.\ a six-point constellation on one circle...)".
- §4.1 (\Cref{rem:M1-counter}) — `\texttt{MULTI\_edges\_*}` → "examples documented in the companion dataset".
- §4.2 (\Cref{rem:N1-min}) — `\texttt{NEST\_q3\_qinner2}, \texttt{NEST\_q2\_qinner3}` → "two such nested operators".
- §5.1 (strata enumeration) — four `\texttt{STRESS\_*}` items → italicised plain-English stratum names.
- §7.2 (\Cref{rem:AT1-degenerate}) — `\texttt{CTRL\_disc\_eps*}`, `\texttt{STRESS\_equalmod}`, `\texttt{CTRL\_conjroots\_t*}`, `\texttt{CTRL\_zeroroot\_*}`, `\texttt{OMEGA\_*}`, `\texttt{GAL\_cyclotomic\_*}` → plain prose ("discriminant locus", "equal-modulus locus", "zero-root locus", "ω-resonance locus").
- §7.2 (\Cref{rem:AT1-verif}) — `[phase4_stokes.json]{wkb_dataset_v1}` → `\cite{wkb_dataset_v1}`.
- §8.2 (figure caption) — `\texttt{constellations.png}, \texttt{plot\_constellations.py}` reference dropped; replaced with a single repository citation.
- §8 (post-figure paragraph) — `[\texttt{clusters.json}, \texttt{constellations.json}]{wkb_dataset_v1}` → `\cite{wkb_dataset_v1}`.
- §8.1 (taxonomy textual reference) — `[\texttt{taxonomy.txt}]{wkb_dataset_v1}` → `\cite{wkb_dataset_v1}`.

(The three remaining occurrences of `constellations.png` are the
`\includegraphics{figures/constellations.png}` paths in Figure 2 — a
genuine file path, not a dataset identifier in prose, and therefore
kept.)

## 3. `\Cref` resolution check

A `pdflatex → bibtex → pdflatex × 2` compile reports **0 undefined
references** and **0 undefined citations** in the final manuscript.

The 41 unique `\Cref{...}` labels referenced are:

```
cor:ring, cor:vieta, def:chi, def:F-functor, fig:taxonomy, fig:zoo,
lem:chi-multiplicative, rem:D2-composite, rem:D2-search,
rem:degenerate, rem:F-functoriality, rem:N1-analytic,
sec:analytic, sec:classes, sec:degeneracy, sec:main, sec:multiedge,
sec:prelim, sec:related, sec:reproducibility, sec:systems, sec:vision,
ssec:M1, ssec:OS, thm:AT1, thm:AT3, thm:AT5, thm:AT7,
thm:D2, thm:M1, thm:N1, thm:S1, thm:main,
…
```

All 41 labels resolve.

## 4. Bibliography cleanup

One new bibliography entry was added to `references.bib`:

```bibtex
@book{lang-algebra,
  author    = {Lang, Serge},
  title     = {Algebra},
  edition   = {Revised Third},
  publisher = {Springer},
  series    = {Graduate Texts in Mathematics},
  volume    = {211},
  year      = {2002},
  address   = {New York},
  doi       = {10.1007/978-1-4613-0041-0}
}
```

This entry is cited by the new Theorem 5.1 proof (Kummer theory step)
in the Round-1 deliverable `proofs_major_revision.tex`. Its omission
from the original `references.bib` triggered the only undefined-citation
warning in the first compile pass.

After this addition, the only remaining BibTeX warnings are two
*pre-existing, purely cosmetic* warnings about volume-vs-number fields
in `mochizuki-asymptotic` and `ramis-q-stokes` (entries authored in
Round-0; unrelated to this revision).

## 5. Summary

| Class of cleanup            | Items | Status   |
|------------------------------|-------|----------|
| Dataset-internal identifiers | 13    | Removed  |
| JSON / PY filename refs       | 6     | Removed  |
| `\Cref` resolution            | 41    | All OK   |
| Undefined refs                | 0     | OK       |
| Undefined citations           | 0     | OK (after lang-algebra) |
| LaTeX warnings                | 0     | OK       |
| BibTeX warnings (cosmetic)    | 2     | Pre-existing |
