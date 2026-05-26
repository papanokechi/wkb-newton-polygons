# Contributing to *The WKB Geometry of Newton Polygons*

Thank you for your interest in contributing. This repository is the
companion to a research manuscript and accompanying computational atlas,
and we welcome contributions that extend or correct the work.

---

## How you can contribute

### 1. Report a bug or correction

Please open a GitHub issue with:

* a brief description of the issue;
* a minimal reproducer (operator parameters, slope, etc.) when the
  issue concerns a specific entry in the atlas;
* the affected file (e.g. `data/operators.json` row, `paper/manuscript.tex`
  line number, or `fleets/fleet*.py` function).

For mathematical corrections (typos in proofs, mis-stated lemmas,
incorrect Newton polygons), please include a citation to the relevant
section of the manuscript.

### 2. Propose a new operator family

We are particularly interested in operators that:

* sit on the boundary of a documented stratum;
* exhibit unexpected $\Delta_{ij}$ degeneracies;
* are not in the current 39-class atlas;
* refine an existing class.

Open an issue with the operator's symbolic form, slope, expected
constellation, and any heuristic computations you have. If you submit
a pull request adding a new operator, please:

1. add the operator entry to `data/operators.json` (follow the schema
   used by existing entries);
2. add the computed `data/newton.json`, `data/chi.json`,
   `data/constellations.json` rows;
3. include a short note in `reports/` explaining its place in the atlas.

### 3. Improve the codebase

Style guide for `code/` and `fleets/`:

* Python 3.10+; standard PEP 8 with reasonable line lengths (~100).
* Pure functions where possible; the fleets are designed to be
  re-runnable from a clean checkout.
* JSON I/O uses 2-space indentation and stable key ordering.
* Pin numerical parameters explicitly (precision, bounded-search radii).

### 4. Extend or correct the proofs

If you find an error in the proofs or wish to extend a theorem
(e.g. a sharper genericity hypothesis), please:

* open an issue first to discuss the proposed change;
* if accepted, submit a PR modifying `paper/manuscript.tex` (or
  `major_revision/followup/` for amendments still in revision flow);
* include a short note in the PR description explaining what changed
  and how it affects downstream theorems.

---

## Pull-request workflow

```bash
git clone https://github.com/papanokechi/wkb-newton-polygons.git
cd wkb-newton-polygons
git checkout -b your-feature-branch
# ... make changes ...
git commit -m "Short summary (≤ 72 chars)

Longer description of what changed and why."
git push -u origin your-feature-branch
```

Then open a PR against `main`.

### Commit-message conventions

* Use the imperative mood ("Add ...", "Fix ...", "Correct ...").
* Keep the subject line ≤ 72 characters.
* Reference issues with `#NNN`.

### Compile check

Before submitting changes to `paper/`, please verify:

```bash
cd paper
pdflatex -interaction=nonstopmode manuscript.tex
bibtex manuscript
pdflatex -interaction=nonstopmode manuscript.tex
pdflatex -interaction=nonstopmode manuscript.tex
```

The PDF should compile with 0 errors and 0 undefined references.

### Dataset additions

For PRs that add or modify atlas entries, please also run:

```bash
python fleets/fleet.py --verify-only
python fleets/fleet3.py --verify-only
```

(Verification mode re-derives the Newton polygons and characteristic
polynomials from the operator definitions and checks them against the
committed JSON.)

---

## Code of conduct

This project follows the
[Contributor Covenant](https://www.contributor-covenant.org/) code of
conduct. Be respectful and constructive.

---

## License

By contributing, you agree that your contributions will be licensed
under the same terms as the project:

* **Code**: [MIT](LICENSE-CODE).
* **Text and figures**: [CC BY 4.0](LICENSE-TEXT).

---

## Contact

Open a GitHub issue for any question. For matters relating to academic
priority or co-authorship, please contact the author via the email
listed on the [Zenodo record](https://doi.org/10.5281/zenodo.20387847).
