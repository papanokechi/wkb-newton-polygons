# Submission Cover Letter — SIGMA

**Target journal:** SIGMA — Symmetry, Integrability and Geometry: Methods and Applications
**Portal:** <https://www.emis.de/journals/SIGMA/submit.html>
**Letter length:** 1 page (≤ 400 words)
**Tone:** Concise, technical, declarative — matches SIGMA's editorial culture (research-statement style, not promotional)

---

## Customisation placeholders

Before submission, replace:

| Placeholder | Value |
|---|---|
| `[DATE]` | The date of submission (e.g., `2026-05-26`) |
| `[EDITOR NAME]` | If addressed to a specific editor (e.g., the most relevant from <https://www.emis.de/journals/SIGMA/editorial-board.html>); otherwise leave the generic salutation |
| `[EMAIL]` | The corresponding-author email (e.g., `ppapanokechi@gmail.com`) |
| `[ARXIV ID]` | Once arXiv assigns an ID (e.g., `2605.NNNNN`); if arXiv is being posted in parallel with SIGMA submission, write *"arXiv submission pending"* |

---

## Letter (ready to copy to PDF)

```
                                                                  [DATE]

To the Editors of SIGMA
(Symmetry, Integrability and Geometry: Methods and Applications)

Dear [EDITOR NAME] and the SIGMA editorial board,

I am pleased to submit the manuscript

  "The WKB Geometry of Newton Polygons:
   A Functorial Classification Theory"

for consideration in SIGMA.

The paper establishes a constellation functor F that sends each scalar
linear operator L with one irregular singularity at infinity to its
WKB exponent constellation C(L), via the identity chi(c) = chi_w(c^q)
on the dominant Newton-polygon edge. Built from a 23-operator atlas
that is systematically expanded to 39 via stratification (Phases I-V),
F is shown to be naturally compatible with mu_q-pullbacks, multi-edge
filtrations, ramified covers (Levelt-Turrittin), and the analytic
anti-Stokes skeleton. The main results are eight theorem-proof pairs
(M1, N1, D2, S1, AT1, AT3, AT5, AT7) that bridge the formal
Newton-polygon picture and the analytic wild character variety. The
within-ring direction count is given by the closed formula
2pq(r + q*binom(r,2)) (Theorem AT7, "p-visibility").

The work fits SIGMA's scope at the intersection of irregular ODEs,
Stokes phenomena, and Frobenius / character-variety geometry. It is
written in a constructively reproducible style: all 39 operators, the
clustering, the analytic skeleton, and every theorem-supporting
computation are accompanied by a public open atlas

  Zenodo deposit  10.5281/zenodo.20387847
  GitHub mirror   https://github.com/papanokechi/wkb-newton-polygons

that re-derives every figure and table in under 30 seconds on a stock
laptop. The companion arXiv preprint is [ARXIV ID].

The Computational and AI Disclosure section declares the use of GitHub
Copilot CLI together with Anthropic Claude as a structured-search and
exposition aid; all theorems, proofs, hypotheses, and counterexample
strata are the human author's. The dataset is dual-licensed
CC-BY-4.0 (text + atlas) and MIT (code + fleet scripts).

The manuscript has not been submitted elsewhere and is not under
review at another journal. I have no conflicts of interest to declare.

Yours sincerely,

Papanokechi
ORCID 0009-0000-6192-8273
Independent Researcher, Yokohama, Japan
Email: [EMAIL]
```

---

## Notes for the author

- **Length:** the letter as written above is ~340 words (excluding placeholders), well under SIGMA's customary 1-page guideline.
- **Tone match:** SIGMA's editor-facing letters tend to be technical-declarative (avoid superlatives like "groundbreaking" or "novel"; SIGMA's referees infer novelty from the content). The above tone is already aligned.
- **Conflict-of-interest line:** include it — SIGMA's submission portal asks for an explicit COI statement.
- **Funding / grant disclosure:** if applicable, add a sentence between the COI line and the sign-off. For an independent-researcher submission with no external funding, the current text is correct as-is.
- **No "this is the first" or "we are the first to..."** language — SIGMA's style guide discourages priority claims in cover letters.
- **Save as `submission_cover_letter.pdf`** (1 page) and attach to the SIGMA portal upload alongside `manuscript.pdf`.
