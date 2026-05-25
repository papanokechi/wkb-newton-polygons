# `figures/` — Manuscript figures

Source files for the figures appearing in `paper/manuscript.tex`.

## Files

| File                 | Bytes    | Used in              | Description |
|----------------------|---------:|----------------------|-------------|
| `constellations.png` |  141,890 | Figure 2 (the *zoo*) | Constellation zoo: 23 representative exponent constellations arranged in a 5×5 grid, plus the four degeneracy strata. Rendered from `code/plot_constellations.py` and `data/constellations.json`. |
| `taxonomy_tikz.tex`  |    4,792 | Figure 1 (taxonomy)  | Real TikZ source for the taxonomy diagram showing the **23-class atlas refining to 39 classes** under the $\mu_q$ / $\mu_{q'}$ symmetry layer, plus the degeneracy island. |

## Regenerating Figure 2 (`constellations.png`)

```bash
cd ..
python code/plot_constellations.py \
    --input data/constellations.json \
    --output figures/constellations.png
```

The script uses matplotlib with a fixed rng seed; output is
byte-deterministic.

## Re-rendering Figure 1 (`taxonomy_tikz.tex`)

The TikZ source is `\input{}`-ed by `paper/manuscript.tex` directly, so
no separate compile is needed in normal use. To preview the figure
standalone:

```bash
# Create a minimal wrapper:
cat > tikz_test.tex <<'EOF'
\documentclass{standalone}
\usepackage{tikz}
\usetikzlibrary{positioning,fit,arrows.meta}
\newcommand{\Cl}{\mathcal{C}}
\newcommand{\Fclass}{\mathcal{F}}
\begin{document}
\input{taxonomy_tikz.tex}
\end{document}
EOF
pdflatex tikz_test.tex
```

This produces `tikz_test.pdf` (~96 KB, one page), which is the
standalone version of Figure 1.

## Required TikZ libraries

* `positioning` — for `\node[right=of ...]`, `\node[below=of ...]`
* `fit` — for the grouping boxes around the atlas grid and degeneracy
  island
* `arrows.meta` — for the refinement arrows from the 23-class grid to
  the 39-class layer

These are declared in the preamble of `paper/manuscript.tex`.

## Macros used

The TikZ file references two project-level macros defined in
`paper/manuscript.tex`:

* `\Cl` — abbreviation for $\mathcal{C}$ (the constellation map)
* `\Fclass` — abbreviation for $\mathcal{F}$ (a class family)

If compiling `taxonomy_tikz.tex` outside the main paper, redefine these
macros in your wrapper preamble (see the example above).

## Cross-references in the manuscript

* Figure 1 label: `\Cref{fig:taxonomy}`
* Figure 2 label: `\Cref{fig:zoo}`

Both labels resolve cleanly in the v2.0 compile (see
`../publication_pipeline/final_verification_report.md`).

## License

These figures are released under [CC BY 4.0](../LICENSE-TEXT).
