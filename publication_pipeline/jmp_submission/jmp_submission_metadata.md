# JMP Submission Metadata Block

Portal-paste fields for the AIP Editorial Manager submission form.

---

## Article type

`Article` (full research paper, ≥ 12 pages, multi-section structure
with theorems, proofs, figures, and a reproducibility deposit).

## Title

> **The WKB Geometry of Newton Polygons: A Functorial Classification
> Theory**

## Running title (≤ 50 chars)

> WKB Geometry of Newton Polygons

## Author(s)

| Field | Value |
|-------|-------|
| Given name | Papanokechi |
| Family name | (single-name attribution) |
| Affiliation | Independent Researcher |
| Postal location | (recommended to add: "Yokohama, Japan" or comparable) |
| Email | (insert at portal-form time — required by AIP) |
| ORCID | 0009-0000-6192-8273 |
| Web profile | `https://github.com/papanokechi/wkb-newton-polygons` |
| Corresponding author | yes (single-author manuscript) |
| Conflict of interest | none |

## Abstract (195 non-math words; JMP cap is 250)

> Linear differential operators with one irregular singularity organise
> themselves, on the open generic stratum, into a *constellation
> functor* `F: L ↦ C(L)` that sends each operator to the multiset of
> roots of its WKB characteristic polynomial χ. The functor refines
> the classical Levelt–Turrittin slope decomposition while retaining
> Galois-theoretic finesse, and it organises a finite taxonomy of 23
> cluster classes indexed by the Newton-polygon slope `−p/q`, the
> inner polynomial `χ_w` of degree `r`, and a list of cyclotomic /
> Galois invariants. We prove a structural multi-edge law `M1`, a
> nested-ramification rule `N1`, a Kummer / cyclotomic dichotomy `D2`,
> a system pullback `S1`, and four analytic-lifting theorems
> `AT1, AT3, AT5, AT7` that transfer the discrete invariants to the
> Levelt–Turrittin cover and predict anti-Stokes ray counts that match
> a numerical atlas exactly on the generic stratum. The 23-class
> taxonomy is supported by a deterministic 48-operator computational
> zoo whose JSON atlas, fleet pipelines, and rendered figures are
> deposited at Zenodo (DOI 10.5281/zenodo.20387847).

## Keywords (19 — order: theory → method → application)

```
WKB analysis
Newton polygon
irregular singularity
Stokes phenomenon
Levelt-Turrittin decomposition
characteristic polynomial
constellation functor
inner polynomial
cyclotomic invariants
Kummer dichotomy
Galois orbit
differential Galois theory
wild character variety
anti-Stokes rays
classification theory
mathematical physics
symbolic computation
computer-assisted mathematics
reproducible research
```

## MSC2020 codes

| Code | Description |
|------|-------------|
| 34M30 | Asymptotics, summation methods (Stokes phenomenon) |
| 34M40 | Stokes phenomenon, ramification, exact-WKB |
| 34M03 | Formal methods, normal forms |
| 12H05 | Differential algebra |
| 14M99 | Special algebraic varieties (related to character varieties) |

(JMP additionally accepts PACS / arXiv subject classes; primary
arXiv category for cross-listing if/when the paper is later posted:
`math-ph`; secondary: `math.CA`, `math.AG`.)

## Funding

> None declared. This work was conducted as independent research with
> no external funding.

## Conflict of interest

> The author declares no conflicts of interest, no financial
> relationships, and no non-financial competing interests that could
> have appeared to influence the work reported in this paper.

## Data availability statement

> The complete computational record — operators, Newton polygons,
> characteristic polynomials, constellations, clusters, counterexamples,
> Phase III/IV invariants, proof skeletons, integration map, and
> rendered figures — is openly available in the companion Zenodo
> deposit at DOI 10.5281/zenodo.20387847 (concept DOI
> 10.5281/zenodo.20387846) under CC-BY-4.0 (text and data) and MIT
> (code and pipelines). A mirror GitHub repository at
> `https://github.com/papanokechi/wkb-newton-polygons` provides a
> versioned record of the computational workflow.

## Reproducibility statement

> All numerical and symbolic results were produced by deterministic
> Python pipelines (`fleet.py` through `fleet5.py`). No randomised
> algorithms were used, and no random seeds need be set: every JSON
> artifact, every figure, and every theorem-proof pair is reproduced
> bytewise on re-execution. Section 11 (Reproducibility) of the
> manuscript and the companion `README.md` document the command
> sequence.

## AI / computer-assistance disclosure

> See §Computational and AI Disclosure of the manuscript. Briefly: a
> publicly-available AI assistant (GitHub Copilot CLI driving
> Anthropic Claude Opus 4.7) was used in four supporting capacities —
> drafting assistance, code generation for the fleet pipelines,
> exploratory pattern-finding on numerical data, and organisational
> support for LaTeX assembly. The assistant was **not** used to
> generate mathematical content, definitions, conclusions, or proof
> arguments. All mathematical statements, theorem formulations,
> proofs, and classification claims were authored, validated, and
> finalised by the human author.

## Suggested reviewers (optional but encouraged by AIP)

(Author should supply 3–5 names at portal-form time. Suggested
expertise areas:)

- Irregular-singularity theory / Levelt–Turrittin decomposition
- Stokes phenomenon / wild character varieties (Boalch–Sabbah–Hertling
  school)
- Differential Galois theory / Picard–Vessiot
- Exact-WKB / resurgence (Voros, Kawai, Takei lineage)
- Symbolic-computation methods in mathematical physics

## Opposed reviewers (optional)

None.

## Prior dissemination

No arXiv preprint at submission time. No prior submission to other
journals. Companion Zenodo deposit is publicly available but contains
reproducibility artifacts only; the mathematical text was first
publicly released at the moment of this submission.
