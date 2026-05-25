#!/usr/bin/env python3
"""
build_v2.py - Build paper_v2_0.tex (round-1 applied) and paper_v2_1.tex
(round-1 + round-2 applied) from the v1 paper.tex and the major_revision/
followup/ deliverables.

Output:
   - paper_v2_0.tex          (used as the base for the followup diff)
   - paper_v2_1.tex          (final post-everything; copied to paper.tex)
   - major_revision_followup.diff   (unified diff: v2_0 -> v2_1)

The script uses unique anchor strings from the live paper.tex to locate
each surgical edit; it does NOT depend on line numbers.
"""
import os
import re
import difflib
import textwrap
import shutil
import sys

ROOT = r'C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\siarc\workspace\wkb-newton-polygons'
PAPER_V1 = os.path.join(ROOT, 'paper', 'paper.tex')
MR = os.path.join(ROOT, 'major_revision')
F = os.path.join(MR, 'followup')

def read(p):
    with open(p, 'r', encoding='utf-8') as h: return h.read()
def write(p, s):
    with open(p, 'w', encoding='utf-8') as h: h.write(s)

src = read(PAPER_V1)
print('v1 size:', len(src))

# ============================================================================
# ROUND-1 EDITS: apply the major_revision_patch content surgically.
# ============================================================================

# (A) Replace ABSTRACT with the round-1 revised abstract content.
rev_abs = read(os.path.join(MR, 'revised_abstract.tex'))
abs_body = re.search(r'\\begin\{abstract\}.*?\\end\{abstract\}', rev_abs, re.S).group(0)

m = re.search(r'\\begin\{abstract\}.*?\\end\{abstract\}', src, re.S)
assert m, "abstract not found in v1"
src = src[:m.start()] + abs_body + src[m.end():]
print('after abstract replace:', len(src))

# (B) Replace SECTION 1 (Introduction) with the round-1 revised intro.
rev_intro = read(os.path.join(MR, 'revised_introduction.tex'))
intro_body = re.search(
    r'\\section\{Introduction\}\\label\{sec:intro\}.*\Z',
    rev_intro, re.S
)
assert intro_body, "introduction body not found in round-1 file"
intro_body_str = intro_body.group(0).rstrip()

m = re.search(
    r'\\section\{Introduction\}\\label\{sec:intro\}.*?(?=\n\n\n%% ====)',
    src, re.S
)
assert m, "intro span not found in src"
src = src[:m.start()] + intro_body_str + '\n\n' + src[m.end()+1:]
print('after intro replace:', len(src))

# (C) Insert a notation table just after the \begin{notation}[The classification functor]
#     block (the round-1 "notation table" addition).
notation_table_block = r"""

%% ---------------------------------------------------------------------------
%% Round-1 follow-up: consolidated notation table for the manuscript
%% ---------------------------------------------------------------------------
\begin{table}[t]
\centering
\small
\begin{tabular}{@{}ll@{}}
\toprule
\textbf{Symbol} & \textbf{Meaning} \\
\midrule
$L$            & scalar linear operator with one irregular singularity at $\infty$ \\
$\op \in \{\opD, \opS, \opT\}$
               & derivation, shift, or $q$-shift, respectively \\
$\NL$          & Newton polygon of $L$ at $\infty$ \\
$E$, $-p/q$, $r$
               & dominant edge; slope (lowest terms); rank multiplier \\
$\LCinf(\cdot)$ & leading coefficient at $x = \infty$ \\
$\chi(c)$, $\chi_w(w)$
               & WKB characteristic polynomial; inner polynomial ($\chi(c) = \chi_w(c^q)$) \\
$\Cl(L)$       & exponent constellation $= \Roots(\chi) \subset \mathbb{C}$ \\
$\Fclass$      & constellation map / functor $(L, \mathfrak{e}) \mapsto \Cl(L)$ \\
$\mu_q, \zeta_q$
               & group of $q$-th roots of unity; primitive root $e^{2\pi i / q}$ \\
$\Dij$         & pairwise difference $c_i - c_j$, $c_i, c_j \in \Cl(L)$ \\
$\Acov$        & anti-Stokes set on the $q$-fold cover $x = t^q$ \\
$\Zlc, \Qlc$   & cyclotomic ring $\mathbb{Z}[\zeta_q]$ and field $\mathbb{Q}(\zeta_q)$ \\
$R_\alpha$     & $\mu_q$-ring $\{\zeta_q^j z_\alpha : 0 \le j < q\}$ \\
\bottomrule
\end{tabular}
\caption{Notation used throughout the paper.}\label{tab:notation}
\end{table}
"""
anchor = r'\end{notation}'
i = src.find(anchor)
assert i >= 0, 'notation block not found'
i_end = i + len(anchor)
# Insert the table after the notation block, before the next section.
src = src[:i_end] + notation_table_block + src[i_end:]
print('after notation table insert:', len(src))

# (D) Insert Lemma 4.0 (chi-multiplicative) before Theorem 4.1.
#     Round 2 uses the v2 lemma (already widened).
lemma_v2 = read(os.path.join(F, 'lemma_chi_multiplicative_v2.tex'))
# Extract from \begin{lemma} through \end{remark} (lemma + proof + iteration remark).
m = re.search(r'\\begin\{lemma\}.*?\\end\{remark\}', lemma_v2, re.S)
assert m, "lemma block not found in v2 file"
lemma_block = m.group(0)

# For v2.0 (round-1 only), we still need the lemma; use the v1 single-slope version.
lemma_v1 = read(os.path.join(MR, 'proofs_major_revision.tex'))
m_v1 = re.search(r'\\begin\{lemma\}.*?\\end\{proof\}', lemma_v1, re.S)
assert m_v1, "v1 lemma block not found"
lemma_block_v1 = m_v1.group(0)

# We'll insert two slightly different versions for v2.0 and v2.1.
# Locate insertion point: before \begin{theorem}[Per-edge factorisation; multi-edge generalisation]
anchor = r'\begin{theorem}[Per-edge factorisation; multi-edge generalisation]'
i = src.find(anchor)
assert i >= 0, 'thm:M1 begin not found'
src_pre_lemma = src[:i]
src_post_lemma = src[i:]
# We'll insert later for v2.0 vs v2.1.

# (E) Replace the proof of Theorem 4.1 (\Cref{thm:M1}) with the round-1 full proof.
m_proof_v1 = re.search(
    r'\\begin\{proof\}\[Proof of \\Cref\{thm:M1\}.*?\\end\{proof\}',
    lemma_v1, re.S
)
assert m_proof_v1, "M1 proof not found in round-1 content"
thm_m1_proof_block = m_proof_v1.group(0)

# Locate the existing proof block (Proof sketch) immediately after the thm:M1
# theorem statement.
thm_m1_proof_existing_re = re.compile(
    r'\\begin\{proof\}\[Proof sketch\]\s*\n\\textit\{Step 1 \(Slope decomposition\)\.\}.*?\\qedhere\n\\end\{proof\}',
    re.S
)
m = thm_m1_proof_existing_re.search(src)
assert m, "existing M1 proof sketch not found"
src = src[:m.start()] + thm_m1_proof_block + src[m.end():]
print('after M1 proof replace:', len(src))

# Also append the M1 remark (cyclic-vector) right after.
m_rem = re.search(r'\\begin\{remark\}\\label\{rem:M1-cyclic-vector\}.*?\\end\{remark\}', lemma_v1, re.S)
if m_rem:
    rem_block = m_rem.group(0)
    # Insert right after the new proof block.
    pos = src.find(thm_m1_proof_block) + len(thm_m1_proof_block)
    src = src[:pos] + '\n\n' + rem_block + src[pos:]
    print('after M1 cyclic-vector remark insert:', len(src))

# (F) Rename dataset-internal strata in the four-strata enumeration.
old_strata = textwrap.dedent(r"""
\begin{enumerate}[leftmargin=2em]
\item \texttt{STRESS\_equalmod} (equal-modulus locus): six points on a
      single circle of radius $\sqrt{2}$, \emph{not} evenly spaced.
\item \texttt{STRESS\_doubleroot} (discriminant locus / resonant
      multiplicity): two rings, the inner with multiplicity $2$ at each
      apparent point.
\item \texttt{STRESS\_zeroroot} (zero-root locus / wall-crossing): two
      points at radius $1$ together with a multiplicity-$q$ root at the
      origin.
\item \texttt{STRESS\_accidental\_sym} (enhanced symmetry): a regular
      $rq$-gon with cyclic symmetry $C_{rq} \supsetneq C_q$, occurring at
      slope $-p/q$ but exhibiting symmetry above what $q$ predicts.
\end{enumerate}
""").strip('\n')

new_strata = textwrap.dedent(r"""
\begin{enumerate}[leftmargin=2em]
\item \emph{Equal-modulus locus.} Six points on a single circle of
      radius $\sqrt{2}$, \emph{not} evenly spaced.
\item \emph{Discriminant locus} (resonant multiplicity): two rings, the
      inner with multiplicity $2$ at each apparent point.
\item \emph{Zero-root locus} (wall-crossing): two points at radius $1$
      together with a multiplicity-$q$ root at the origin.
\item \emph{Accidental-symmetry locus.} A regular $rq$-gon with cyclic
      symmetry $C_{rq} \supsetneq C_q$, occurring at slope $-p/q$ but
      exhibiting symmetry above what $q$ predicts.
\end{enumerate}
""").strip('\n')
assert old_strata in src, "old strata enumeration not found"
src = src.replace(old_strata, new_strata)
print('after strata renaming:', len(src))

# (G) Replace Theorem 5.1 (thm:D2) statement + proof with the round-1 revised version.
m_thm = re.search(
    r'\\begin\{theorem\}\[Inner-polynomial Kummer dichotomy; prime \$q\$,\s*revised\]\\label\{thm:D2\}.*?\\end\{theorem\}',
    lemma_v1, re.S
)
assert m_thm, "revised D2 theorem statement not found"
new_d2_thm = m_thm.group(0)

m_proof = re.search(
    r'\\begin\{proof\}\[Proof of \\Cref\{thm:D2\}\].*?\\end\{proof\}',
    lemma_v1, re.S
)
assert m_proof, "revised D2 proof not found"
new_d2_proof = m_proof.group(0)

# Find and replace D2 theorem block
old_d2_thm_re = re.compile(
    r'\\begin\{theorem\}\[Inner-polynomial \$\\mathbb\{Z\}\$-resonance dichotomy; prime\s*\n?\$q\$\]\\label\{thm:D2\}.*?\\end\{theorem\}',
    re.S
)
m = old_d2_thm_re.search(src)
assert m, "old D2 theorem not found"
src = src[:m.start()] + new_d2_thm + src[m.end():]
print('after D2 thm replace:', len(src))

# Replace D2 "proof sketch" with the full proof
old_d2_proof_re = re.compile(
    r'\\begin\{proof\}\[Proof sketch\]\n\\textit\{Set-up\.\}.*?\\end\{proof\}',
    re.S
)
m = old_d2_proof_re.search(src)
assert m, "old D2 proof sketch not found"
src = src[:m.start()] + new_d2_proof + src[m.end():]
print('after D2 proof replace:', len(src))

# (G2) Remove the search-window-limitation remark for D2 (now refactored)
old_d2_search_rem_re = re.compile(
    r'\\begin\{remark\}\[Search-window limitation\]\\label\{rem:D2-search\}.*?\\end\{remark\}',
    re.S
)
m = old_d2_search_rem_re.search(src)
if m:
    # Replace with the bounded-search corroboration remark from the round-1 content
    m_corr = re.search(
        r'\\begin\{remark\}\[Bounded-search corroboration\]\\label\{rem:D2-search\}.*?\\end\{remark\}',
        lemma_v1, re.S
    )
    if m_corr:
        src = src[:m.start()] + m_corr.group(0) + src[m.end():]
        print('after D2 search-window remark replace:', len(src))

# (H) Sharpen (OS3).
old_OS3 = r"""\item[(OS3)] No $\omega$-resonance beyond $\mu_q$: the multiset
       $\{\arginline \Dij \mod \pi/p\}$ has no coincidences beyond
       those forced by the ring structure."""
new_OS3 = r"""\item[(OS3)] \emph{Sharpened.} No $\omega$-resonance beyond
       $\mu_q$: the multiset $\{\arginline \Dij \mod \pi/p\}$ has no
       coincidences beyond those forced by the $\mu_q$-ring structure
       on $\Cl(L)$. Equivalently, every coincidence
       $\arginline \Dij \equiv \arginline \Delta_{i'j'} \pmod{\pi/p}$
       must arise from a pairing of unordered $\mu_q$-images
       $\{c_i, c_j\} \subset R_\alpha$ and
       $\{c_{i'}, c_{j'}\} \subset R_\alpha$ inside the SAME ring
       $R_\alpha$; cross-ring coincidences are excluded."""
assert old_OS3 in src, "(OS3) not found"
src = src.replace(old_OS3, new_OS3)
print('after (OS3) sharpen:', len(src))

# (I) Replace Theorem 7.1 (thm:AT1) proof with the round-1 full proof.
m_proof_at1 = re.search(
    r'\\begin\{proof\}\[Proof of \\Cref\{thm:AT1\}\].*?\\end\{proof\}',
    lemma_v1, re.S
)
assert m_proof_at1, "AT1 full proof not found"
new_at1_proof = m_proof_at1.group(0)

old_at1_proof_re = re.compile(
    r'\\begin\{proof\}\[Proof sketch\]\n\\textit\{Step 1 \(Levelt--Turrittin on the \$q\$-cover\)\.\}.*?\\end\{proof\}',
    re.S
)
m = old_at1_proof_re.search(src)
assert m, "existing AT1 proof sketch not found"
src = src[:m.start()] + new_at1_proof + src[m.end():]
print('after AT1 proof replace:', len(src))

# (J) Clean the AT1 "beyond the open stratum" remark (remove dataset IDs).
old_at1_beyond = r"""\begin{remark}[Beyond the open stratum]\label{rem:AT1-degenerate}
Outside (OS1)--(OS3), four classes of corrections occur:
on the discriminant locus (\texttt{CTRL\_disc\_eps*}) resonance /
logarithmic Stokes data appear; on the equal-modulus locus
(\texttt{STRESS\_equalmod}, \texttt{CTRL\_conjroots\_t*}) the rotation
in \Cref{cor:vieta} becomes a rigid permutation up to shared rotation;
on the zero-root locus (\texttt{CTRL\_zeroroot\_*}) the Newton polygon
itself wall-crosses; on the $\omega$-resonance locus
(\texttt{OMEGA\_*}, \texttt{GAL\_cyclotomic\_*}) anti-Stokes rays cluster
beyond what (OS3) permits.
\end{remark}"""
new_at1_beyond = r"""\begin{remark}[Beyond the open stratum]\label{rem:AT1-degenerate}
Outside (OS1)--(OS3), four classes of corrections occur:
on the discriminant locus, resonance / logarithmic Stokes data appear;
on the equal-modulus locus, the rotation in \Cref{cor:vieta} becomes a
rigid permutation up to shared rotation; on the zero-root locus, the
Newton polygon itself wall-crosses; on the $\omega$-resonance locus,
anti-Stokes rays cluster beyond what (OS3) permits.
\end{remark}"""
assert old_at1_beyond in src, "AT1 beyond-the-open-stratum remark not found"
src = src.replace(old_at1_beyond, new_at1_beyond)
print('after AT1 remark clean:', len(src))

# Also clean the AT1 verification remark (drop dataset filename).
old_at1_verif = r"""\begin{remark}[Phase-IV verification]\label{rem:AT1-verif}
The Phase-IV consistency check
\cite[phase4\_stokes.json]{wkb_dataset_v1} verifies the formula
$\#\Acov_{\mathrm{actual}} / \#\Acov_{\mathrm{expected}} = 1.000$ exactly
on $11$ open-stratum operators.
\end{remark}"""
new_at1_verif = r"""\begin{remark}[Computational verification]\label{rem:AT1-verif}
The companion dataset \cite{wkb_dataset_v1} contains a sweep verifying
the formula $\#\Acov_{\mathrm{actual}} / \#\Acov_{\mathrm{expected}}
= 1.000$ exactly on $11$ open-stratum operators.
\end{remark}"""
assert old_at1_verif in src, "AT1 verif remark not found"
src = src.replace(old_at1_verif, new_at1_verif)
print('after AT1 verif clean:', len(src))

# (K) Replace M1 counterexample remark dataset IDs.
old_M1_counter = r"""\begin{remark}[Counterexample boundary for M1]\label{rem:M1-counter}
The disjoint-union conclusion in (3) is a multiset statement; as
\emph{sets} in $\mathbb{C}^\times$ the per-edge constellations may
coincide on the \emph{inter-edge equal-radius stratum} (examples in the
companion dataset: \texttt{MULTI\_edges\_1o4\_then\_1o2},
\texttt{MULTI\_edges\_1o3\_r2\_then\_1o2}; see
\cite[counterexamples.json: CE-multiedge-equalradius]{wkb_dataset_v1}).
Likewise, when a per-edge $\chi_w^{(\alpha)}(0) = 0$, the zero-root
contributions of adjacent edges \emph{share} the origin in $\mathbb{C}$
(CE-multiedge-zerosharing). These are not contradictions: the multiset
disjoint union is preserved; only the set-theoretic statement is
weakened.
\end{remark}"""
new_M1_counter = r"""\begin{remark}[Counterexample boundary for M1]\label{rem:M1-counter}
The disjoint-union conclusion in (3) is a multiset statement; as
\emph{sets} in $\mathbb{C}^\times$ the per-edge constellations may
coincide on the \emph{inter-edge equal-radius stratum}, where the
radial annuli of two distinct edges accidentally share a radius.
Examples are documented in the companion dataset \cite{wkb_dataset_v1}.
Likewise, when a per-edge $\chi_w^{(\alpha)}(0) = 0$, the zero-root
contributions of adjacent edges \emph{share} the origin in $\mathbb{C}$.
These are not contradictions: the multiset disjoint union is preserved;
only the set-theoretic statement is weakened.
\end{remark}"""
assert old_M1_counter in src, "M1 counter remark not found"
src = src.replace(old_M1_counter, new_M1_counter)
print('after M1 counter clean:', len(src))

# (L) Clean the N1 nested-ramification remark (drop dataset IDs).
old_N1_min = r"""\begin{remark}[Minimality]\label{rem:N1-min}
The hypothesis $\chi_w(w) = \chi_v(w^{q'})$ is preserved under further
inner factorisations $\chi_v(v) = \chi_u(v^{q''})$; iterating until no
inner factorisation is possible gives the \emph{minimal} $q' q'' \cdots$
through which the constellation factors. The Phase-III sweep records two
such nested operators in the atlas (\texttt{NEST\_q3\_qinner2},
\texttt{NEST\_q2\_qinner3}), both stable under one round of inner
factorisation.
\end{remark}"""
new_N1_min = r"""\begin{remark}[Minimality]\label{rem:N1-min}
The hypothesis $\chi_w(w) = \chi_v(w^{q'})$ is preserved under further
inner factorisations $\chi_v(v) = \chi_u(v^{q''})$; iterating until no
inner factorisation is possible gives the \emph{minimal} $q' q'' \cdots$
through which the constellation factors. The companion atlas
\cite{wkb_dataset_v1} records two such nested operators, both stable
under one round of inner factorisation.
\end{remark}"""
assert old_N1_min in src, "N1 minimality remark not found"
src = src.replace(old_N1_min, new_N1_min)
print('after N1 min clean:', len(src))

# (M) Clean the zoo caption (drop \texttt{constellations.png} etc.).
old_zoo_caption_tail = r"""is the visible signature that
$\Fclass$ is many-to-one and that accidental symmetry is a feature of
every simple-class operator. Source:
\cite[\texttt{constellations.png}, \texttt{plot\_constellations.py}]{wkb_dataset_v1}.}"""
new_zoo_caption_tail = r"""is the visible signature that
$\Fclass$ is many-to-one and that accidental symmetry is a feature of
every simple-class operator. The full dataset of plots is in the
companion repository \cite{wkb_dataset_v1}.}"""
assert old_zoo_caption_tail in src, "zoo caption tail not found"
src = src.replace(old_zoo_caption_tail, new_zoo_caption_tail)
print('after zoo caption clean:', len(src))

# Clean the textual reference to clusters.json/constellations.json after the figure.
old_zoo_ref = r"""\Cref{fig:zoo} shows twelve representative panels. The full enumeration
of all $23$ classes, with explicit operator representatives, $\chi_w$
data, and panel pointers, lives in the companion dataset
\cite[\texttt{clusters.json},
\texttt{constellations.json}]{wkb_dataset_v1}."""
new_zoo_ref = r"""\Cref{fig:zoo} shows twelve representative panels. The full enumeration
of all $23$ classes, with explicit operator representatives, $\chi_w$
data, and panel pointers, lives in the companion dataset
\cite{wkb_dataset_v1}."""
assert old_zoo_ref in src, "zoo dataset reference text not found"
src = src.replace(old_zoo_ref, new_zoo_ref)
print('after zoo dataset ref clean:', len(src))

# Clean the taxonomy textual reference to taxonomy.txt.
old_tax_ref = r"""A precise textual specification (axes, sub-tile
structure, encoding conventions, degeneracy island, legend) is recorded
in the dataset \cite[\texttt{taxonomy.txt}]{wkb_dataset_v1} and is
suitable for a figure-rendering pipeline. The diagram lives in this
section in the camera-ready manuscript."""
new_tax_ref = r"""A precise textual specification (axes, sub-tile
structure, encoding conventions, degeneracy island, legend) is recorded
in the companion dataset \cite{wkb_dataset_v1}."""
assert old_tax_ref in src, "taxonomy textual ref not found"
src = src.replace(old_tax_ref, new_tax_ref)
print('after taxonomy textual ref clean:', len(src))

# Save the "round-1 only" version BEFORE applying round-2 lemma/Thm5.1/figure/abstract.
# We'll insert the v1 lemma here (for v2.0) and v2 lemma (for v2.1) at the same place.
v2_0 = src_pre_lemma_inject = None  # placeholder, computed below

# Now compute v2.0 by inserting the v1 lemma at the M1 anchor position.
# (Re-find anchor in current src.)
anchor = r'\begin{theorem}[Per-edge factorisation; multi-edge generalisation]'
i = src.find(anchor)
assert i >= 0, 'thm:M1 anchor not found after intermediate edits'

# Final figure replacement and Thm 5.1 step-2 fix touch text AFTER the M1 anchor,
# but for the v2.0 reference (round-1 only) we still want the figure replacement
# and the Thm 5.1 statement+proof as in round-1 (already injected).
#
# So the only remaining differences between v2.0 and v2.1 are:
#   * lemma (single-slope v1 vs widened v2),
#   * Thm 5.1 proof Step 2 (-u*q' phrasing -> a/b derivation, plus non-exhaustiveness remark),
#   * abstract (round-1 234-word vs round-2 186-word),
#   * taxonomy figure (placeholder vs \input{figures/taxonomy_tikz.tex}),
#   * possibly (OS3) cross-ref tweak in Thm 7.1 Step 4.

# Build v2.0:
v2_0 = src[:i] + lemma_block_v1 + '\n\n' + src[i:]

# Build v2.1: insert v2 lemma block (with iteration remark).
v2_1 = src[:i] + lemma_block + '\n\n' + src[i:]

# In v2.0, the abstract is round-1 (234 words); we already replaced it.
# In v2.1, replace the abstract with the round-2 trimmed v2.
abs_v2 = read(os.path.join(F, 'revised_abstract_v2.tex'))
abs_v2_body = re.search(r'\\begin\{abstract\}.*?\\end\{abstract\}', abs_v2, re.S).group(0)
m = re.search(r'\\begin\{abstract\}.*?\\end\{abstract\}', v2_1, re.S)
v2_1 = v2_1[:m.start()] + abs_v2_body + v2_1[m.end():]

# In v2.0, the Thm 5.1 proof still has the -u*q' phrasing. v2.1 fixes it.
# Apply the Step-2 fix to v2.1 only.
step2_fix = read(os.path.join(F, 'theorem_5_1_step2_fix.tex'))
# Extract the replacement Step-2 block.
m_step2 = re.search(
    r'%% ------------------- Drop-in replacement for Step 2 -------------------------\n(.*?)\n%% --------------- Drop-in addition AFTER Step 3 \(mutual exclusivity\) ----------',
    step2_fix, re.S
)
assert m_step2, "Step-2 replacement block not found in followup file"
step2_replacement = m_step2.group(1).strip()

m_nonexh = re.search(
    r'%% --------------- Drop-in addition AFTER Step 3 \(mutual exclusivity\) ----------\n(.*?)\n%% =================================================================',
    step2_fix, re.S
)
assert m_nonexh, "non-exhaustiveness scope addition not found"
nonexh_addition = m_nonexh.group(1).strip()

# Now in v2.1 replace the v1 Step 2 block with the v2 step-2 fix.
# Find the old Step 2 in v2.1.
old_step2_re = re.compile(
    r'\\smallskip\n\\textit\{Step 2 \(Kummer relation gives a cross-ring relation\)\.\}.*?This proves \(2\)\.',
    re.S
)
m = old_step2_re.search(v2_1)
assert m, "v1 Step 2 (with -u*q' phrasing) not found in v2.1"
v2_1 = v2_1[:m.start()] + step2_replacement + v2_1[m.end():]

# Add the non-exhaustiveness paragraph right after Step 3.
old_step3_end_re = re.compile(
    r'(Hence \(1\)\nand \(2\) cannot hold simultaneously\.\s*\\end\{proof\})',
    re.S
)
m = old_step3_end_re.search(v2_1)
assert m, "Step 3 end not found"
v2_1 = v2_1[:m.start()] + 'Hence (1)\nand (2) cannot hold simultaneously.\n\n' + nonexh_addition + '\n\\end{proof}' + v2_1[m.end():]

# (N) Taxonomy figure replacement.
# v2.0 uses an explicit reference to the dataset taxonomy.txt; v2.1 \input{}s the TikZ file.
old_fig_v1 = r"""\begin{figure}[t]
\centering
\fbox{\parbox{0.97\linewidth}{\centering\textsf{[Figure~1
placeholder]}\\[0.4ex]\textsl{Taxonomy diagram of the $23$ constellation
classes; spec in \S\ref{ssec:taxonomy} and the companion dataset
\cite{wkb_dataset_v1}.}}}
\caption{The $\Fclass$-image stratification: $23$ constellation classes.
\textbf{Atlas.} A $4 \times 4$ grid indexed by $q \in \{2, 3, 4\}$
(columns) and $r \in \{1, 2, 3\}$ (rows), with a separate ``$r = 1$''
row spanning all $q$. Each $(q, r)$ cell with $r \ge 2$ is subdivided by
the valuation pattern of $\chi_w$: \emph{simple} (only $\alpha_0,
\alpha_r \ne 0$, single regular $rq$-gon), \emph{double} (one interior
$\alpha_j \ne 0$, two-radius generic or single-radius merger on the
discriminant locus), \emph{mixed/generic} (all $\alpha_j \ne 0$).
\textbf{Generic vs.\ special encoding.} Solid borders mark the generic
stratum, dashed grey borders the real-coefficient stratum, grey fill the
single-ring collapses, corner badges the accidental-symmetry classes.
\textbf{Degeneracy island.} A detached $1 \times 4$ inset records the
four stress-test classes (\texttt{STRESS\_equalmod},
\texttt{STRESS\_doubleroot}, \texttt{STRESS\_zeroroot},
\texttt{STRESS\_accidental\_sym}) with codimension-$1$ connector arrows
to the parent atlas cells.}
\label{fig:taxonomy}
\end{figure}"""

# In v2.0 (round-1 only), the figure already has a placeholder \input but cleaned strata names.
new_fig_v2_0 = r"""\begin{figure}[t]
\centering
\fbox{\parbox{0.97\linewidth}{\centering\textsf{[Figure~1
placeholder]}\\[0.4ex]\textsl{Taxonomy diagram of the $23$ constellation
classes; render to be provided in the camera-ready version
(see \cite{wkb_dataset_v1} for the textual specification).}}}
\caption{The $\Fclass$-image stratification: $23$ single-edge
constellation classes, refining to $39$ once multi-edge polygons,
nested ramification, and prime-$q$ arithmetic strata are tracked
(\Cref{thm:M1,thm:N1,thm:D2}).
\textbf{Atlas.} A $4 \times 4$ grid indexed by $q \in \{2, 3, 4\}$
(columns) and $r \in \{1, 2, 3\}$ (rows), with a separate ``$r = 1$''
row spanning all $q$. Each $(q, r)$ cell with $r \ge 2$ is subdivided by
the valuation pattern of $\chi_w$: \emph{simple} (only $\alpha_0,
\alpha_r \ne 0$, single regular $rq$-gon), \emph{double} (one interior
$\alpha_j \ne 0$, two-radius generic or single-radius merger on the
discriminant locus), \emph{mixed/generic} (all $\alpha_j \ne 0$).
\textbf{Degeneracy island.} A detached $1 \times 4$ inset records the
four named degenerate strata (equal-modulus, double root, zero root,
accidental symmetry) with codimension-$1$ connector arrows to the
parent atlas cells.}
\label{fig:taxonomy}
\end{figure}"""

# In v2.1 (round-2 applied), the figure uses the actual TikZ file.
new_fig_v2_1 = r"""\begin{figure}[t]
\centering
\input{figures/taxonomy_tikz.tex}
\caption{The $\Fclass$-image stratification: $23$ single-edge
constellation classes, refining to $39$ once multi-edge polygons,
nested ramification, and prime-$q$ arithmetic strata are tracked
(\Cref{thm:M1,thm:N1,thm:D2}). The $23$-class atlas is the slope-by-rank
grid plus four named degenerate strata (equal-modulus, double root,
zero root, accidental symmetry); the $+16$ refining strata come from
the multi-edge product (M1), nested ramification (N1), and the
prime-$q$ Kummer dichotomy (D2).}
\label{fig:taxonomy}
\end{figure}"""

assert old_fig_v1 in v2_0, "old figure block not found in v2.0"
v2_0 = v2_0.replace(old_fig_v1, new_fig_v2_0)
assert old_fig_v1 in v2_1, "old figure block not found in v2.1"
v2_1 = v2_1.replace(old_fig_v1, new_fig_v2_1)
print('figure replaced in both versions')

# (O) Cross-reference cleanup: in v2.1, add an explicit (OS3) cross-reference
# to Thm 7.1 Step 4. Locate the new AT1 proof block.
old_at1_step4_marker = r"distinct count is governed by collisions in $\{\arginline \Dij \mod \pi/p\}$"
# We have the new AT1 proof in v2_1 already; search for the step-4 paragraph,
# which mentions (OS3)
# Strategy: locate "Under (OS3), no such collisions" and add cross-ref to ssec:OS.
old_OS3_inline_re = re.compile(
    r'Under \(OS3\), no such collisions occur beyond those forced by the\nring structure\.',
    re.S
)
if old_OS3_inline_re.search(v2_1):
    v2_1 = old_OS3_inline_re.sub(
        r'Under the sharpened (OS3) of \\Cref{ssec:OS}, no such\ncollisions occur beyond those forced by the $\\mu_q$-ring\nstructure on $\\Cl(L)$.',
        v2_1
    )
    print('AT1 Step 4 OS3 cross-ref injected (v2.1 only)')
else:
    # Maybe phrasing differs; just attempt to find any (OS3) in v2.1's new AT1 proof
    pass

# (P) Remove the AT3 "Phase-IV correction" remark dataset filename.
old_at3_corr = r"\cite[phase4\_stokes.json]{wkb_dataset_v1}"
if old_at3_corr in v2_0:
    v2_0 = v2_0.replace(old_at3_corr, r"\cite{wkb_dataset_v1}")
if old_at3_corr in v2_1:
    v2_1 = v2_1.replace(old_at3_corr, r"\cite{wkb_dataset_v1}")

# (Q) Strip any remaining \texttt{STRESS_, MULTI_, NEST_, CTRL_, OMEGA_, GAL_} patterns
# from prose. Search across both versions.
for tok in ('STRESS\\_', 'MULTI\\_', 'NEST\\_', 'CTRL\\_', 'OMEGA\\_', 'GAL\\_'):
    cnt0 = v2_0.count(tok)
    cnt1 = v2_1.count(tok)
    if cnt0 or cnt1:
        print(f'  remaining dataset ID "{tok}": v2.0={cnt0}, v2.1={cnt1}')

# Also strip any phase4_stokes.json, phase3_invariants.json, phase4_correction.* refs.
for j in ('phase4\\_stokes.json', 'phase3\\_invariants.json', 'phase4\\_correction'):
    cnt0 = v2_0.count(j)
    cnt1 = v2_1.count(j)
    if cnt0 or cnt1:
        print(f'  remaining JSON ref "{j}": v2.0={cnt0}, v2.1={cnt1}')

# (R) Clean the last remaining STRESS_equalmod reference in the §3 remark.
old_stress_inline = r"""responsible for the apparent regularity of stress test
\texttt{STRESS\_equalmod} (a six-point constellation on one circle that is
\emph{not} a regular hexagon); the third is a wall-crossing of the Newton"""
new_stress_inline = r"""responsible for the apparent regularity of the
equal-modulus stratum (e.g.\ a six-point constellation on one circle
that is \emph{not} a regular hexagon); the third is a wall-crossing of
the Newton"""
if old_stress_inline in v2_0:
    v2_0 = v2_0.replace(old_stress_inline, new_stress_inline)
    print('STRESS_equalmod inline ref cleaned in v2.0')
if old_stress_inline in v2_1:
    v2_1 = v2_1.replace(old_stress_inline, new_stress_inline)
    print('STRESS_equalmod inline ref cleaned in v2.1')

# Final check.
for tok in ('STRESS\\_', 'MULTI\\_', 'NEST\\_', 'CTRL\\_', 'OMEGA\\_', 'GAL\\_'):
    cnt0 = v2_0.count(tok)
    cnt1 = v2_1.count(tok)
    if cnt0 or cnt1:
        print(f'  STILL REMAINING dataset ID "{tok}": v2.0={cnt0}, v2.1={cnt1}')

# Write the files.
v2_0_path = os.path.join(F, 'paper_v2_0.tex')
v2_1_path = os.path.join(F, 'paper_v2_1.tex')
write(v2_0_path, v2_0)
write(v2_1_path, v2_1)
print(f'\nv2.0 written: {os.path.getsize(v2_0_path)} bytes')
print(f'v2.1 written: {os.path.getsize(v2_1_path)} bytes')

# Generate the followup unified diff.
diff = difflib.unified_diff(
    v2_0.splitlines(keepends=False),
    v2_1.splitlines(keepends=False),
    fromfile='a/paper.tex',
    tofile='b/paper.tex',
    n=3,
    lineterm=''
)
diff_text = '\n'.join(diff) + '\n'
diff_path = os.path.join(F, 'major_revision_followup.diff')
write(diff_path, diff_text)
print(f'followup diff written: {os.path.getsize(diff_path)} bytes ({diff_text.count(chr(10))} lines)')
print('Done.')
