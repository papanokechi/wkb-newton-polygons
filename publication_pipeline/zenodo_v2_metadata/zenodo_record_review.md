# Zenodo Record Review — `10.5281/zenodo.20387847`

**URL:** <https://zenodo.org/records/20387847>
**DOI (this version):** `10.5281/zenodo.20387847`
**Concept DOI (latest-version pointer):** `10.5281/zenodo.20387846`
**State:** ✅ Published · open access
**Reviewed:** 2026-05-26

---

## TL;DR

The deposit went through cleanly: 45 files, 3.96 MB, DOI assigned,
GitHub link wired up, license correct. Two corrections are strongly
recommended (one mandatory) before sharing the link widely:

1. 🔴 **Mandatory** — the rich-text description still says this record
   "supersedes the v1.0 dataset (10.5281/zenodo.20355904)". That
   DOI belongs to a **different paper** (Khinchin's constant), and the
   `isNewVersionOf` relation was correctly removed already — so this
   stray sentence in the description must also be removed for accuracy.
2. 🟡 **Strongly recommended** — title currently reads
   *"… A Functorial Classification Theory (v2.0)"*. Since this is
   Zenodo version 1.0, drop the trailing "(v2.0)" for consistency
   (the v2.0 label is an internal manuscript-revision tag, not a
   deposit version).

Both can be edited in-place via Zenodo's "Edit record" without
minting a new DOI. After editing, run the local DOI-propagation
script to bake `10.5281/zenodo.20387847` into the GitHub
repository's metadata files.

---

## 1. Identification ✅

| Field | Value | Verdict |
|---|---|---|
| Record ID            | `20387847`                                  | ✅ |
| Concept ID           | `20387846`                                  | ✅ |
| Version DOI          | `10.5281/zenodo.20387847`                   | ✅ |
| Concept DOI          | `10.5281/zenodo.20387846`                   | ✅ |
| Version string       | `1.0`                                       | ✅ correct (first-ever deposit) |
| Publication date     | 2026-05-26                                  | ✅ |
| State                | `done`                                      | ✅ published |
| Access right         | `open`                                      | ✅ |
| License (controlled) | `cc-by-4.0`                                 | ✅ |
| Title                | *"… A Functorial Classification Theory **(v2.0)**"* | 🟡 trailing tag |
| Resource type        | `publication / preprint`                    | 🟢 acceptable (was article in JSON; preprint is fine for un-refereed work) |

---

## 2. Authorship ✅

| | |
|---|---|
| Name        | Papanokechi |
| Affiliation | Independent Researcher |
| ORCID       | `0009-0000-6192-8273` ✓ matches `CITATION.cff` |

---

## 3. Description content 🔴

The published HTML description begins:

> "This release accompanies the camera-ready manuscript … and
> **supersedes the v1.0 dataset (10.5281/zenodo.20355904)** by
> promoting it to a complete, refereed publication."

That sentence is factually wrong:

- `10.5281/zenodo.20355904` is **"A Certified Bound and a Conditional
  Lean Theorem for a Bounded-Height Algebraicity Exclusion for
  Khinchin's Constant"** (published 2026-05-23) — an entirely
  different paper.
- This deposit has **no prior Zenodo version**; it is the first
  Zenodo record for the WKB paper.

**Fix (recommended edit):** open the record's *Edit* view and
replace the opening paragraph of the description with:

> "This release publishes the camera-ready manuscript *The WKB
> Geometry of Newton Polygons: A Functorial Classification Theory*
> together with its full Phase I–V computational atlas, refereed
> revision packages, and submission bundles."

The remaining paragraphs of the description (χ-factorisation,
23 → 39 atlas, μ_q bookkeeping, p-visibility, repository pointer,
dual-licensing) are accurate and should be preserved verbatim.

---

## 4. Keywords ✅ (with two minor drops)

17 keywords accepted; 2 missing relative to the JSON I generated:

| Keyword | Status |
|---|---|
| WKB analysis                | ✅ |
| Newton polygon              | ✅ |
| irregular singularity       | ✅ |
| formal classification       | ✅ |
| Stokes phenomenon           | ✅ |
| anti-Stokes directions      | ✅ |
| Levelt-Turrittin theorem    | ✅ |
| exponent constellation      | ✅ |
| mu_q-pullback               | ✅ |
| slope filtration            | ✅ |
| Kummer dichotomy            | ✅ |
| p-visibility                | ✅ |
| functorial classification   | ✅ |
| classification theory       | ✅ |
| q-difference operator       | ✅ |
| irregular ODE               | ✅ |
| constellation map           | ✅ |
| **difference operator**     | ❌ dropped |
| **reproducible research**   | ❌ dropped |

Not blocking; can be added during the same edit pass if desired.

---

## 5. Related identifiers ✅

| Relation         | Identifier | Verdict |
|---|---|---|
| `isSourceOf`     | `https://github.com/papanokechi/wkb-newton-polygons`            | ✅ |
| `isIdenticalTo`  | `https://github.com/papanokechi/wkb-newton-polygons/releases/tag/v2.0` | ✅ (matches the v2.0 GitHub tag) |
| `isNewVersionOf` | *(correctly removed)*                                            | ✅ |
| `isSupplementTo` | arXiv id — **not yet added** (placeholder skipped)               | 🟢 intentional |

When the arXiv preprint is posted, add it as
`isSupplementTo` via *Edit record*. No re-versioning needed.

---

## 6. Communities ⚪

None joined. Original metadata listed four (math-ph, exact-wkb,
stokes-phenomena, reproducible-research). Communities only get
attached after a curator of that community accepts the submission,
and several of those names may not exist as Zenodo communities.
Acceptable as-is; can be requested later from the record page.

---

## 7. Files — 45 uploaded, 3.96 MB total ✅

All 45 files transferred. **Heads-up:** Zenodo's web UI flattens
directory structure, so what was

```
data/chi.json
figures/constellations.png
reports/proofs.md
code/plot_constellations.py
fleets/fleet.py
```

now appears in the Zenodo record as

```
chi.json
constellations.png
proofs.md
plot_constellations.py
fleet.py
```

with no folders. No name collisions occurred (all 45 filenames are
unique), so the flat layout is fine. The companion zip on GitHub
preserves the directory structure for users who want to reconstruct
the original layout.

**Cross-checked against the GitHub repo:**

| Tier | Expected | Found | Verdict |
|---|---:|---:|---|
| Manuscript bundle (`manuscript.{tex,pdf,bbl}` + `paper.bbl` + `references.bib`) | 5 | 5 | ✅ |
| Metadata files (`README.md`, `CITATION.cff`, `LICENSE-CODE`, `LICENSE-TEXT`, `citation_block.txt`, `release_notes_v2.0.txt`, `zenodo_metadata_v2.0.txt`, `UPLOAD_MANIFEST.md`) | 8 | 8 | ✅ |
| `figures/`     | 2  | 2  | ✅ |
| `data/`        | 19 | 19 | ✅ |
| `reports/`     | 6  | 6  | ✅ |
| `code/`        | 1  | 1  | ✅ |
| `fleets/`      | 4  | 4  | ✅ |
| **Total**      | 45 | 45 | ✅ |

Total payload: **4,151,627 bytes (3.96 MB)** — matches the local
folder byte-for-byte.

---

## 8. Open follow-ups (post-publication)

These are not blocking the record itself but should be done now
that the DOI is final.

### 8.1 🔴 Edit the description (see §3 above)
Direct edit on the Zenodo record page. No new DOI needed.

### 8.2 🟡 Edit the title (drop the trailing "(v2.0)")
Same edit pass as §8.1. Final title should read exactly:

> The WKB Geometry of Newton Polygons: A Functorial Classification Theory

### 8.3 🟢 Propagate the DOI through the GitHub repo
The repo still has 46+ files containing the placeholder
`10.5281/zenodo.XXXXXXX`. Run from the project root:

```bash
bash publication_pipeline/doi_propagation_commands.sh 10.5281/zenodo.20387847
```

This will update:

- `CITATION.cff` (3 DOI fields)
- `README.md`
- `submission_checklist.md`
- `zenodo_metadata_v2.0.txt`
- `paper_v2_1.tex` + `manuscript.tex` copies (if they hold DOI references)
- All files under `publication_pipeline/`, `arxiv_bundle/`, `journal_bundle/`, `major_revision/`

After running, commit and push:

```bash
git add -A
git commit -m "Propagate Zenodo DOI 10.5281/zenodo.20387847"
git push origin main
```

### 8.4 🟢 Re-tag the GitHub release with the DOI
The `v2.0` GitHub tag predates the DOI assignment. Either:

- **(option a)** leave the existing `v2.0` tag and add a release note
  edit pointing to the DOI, OR
- **(option b)** delete + re-tag with the DOI in the release notes
  (forces `isIdenticalTo` to truly remain identical bit-for-bit).

Option (a) is safest because the GitHub tag is referenced from the
Zenodo record's `isIdenticalTo`. Editing release notes only is
non-disruptive.

### 8.5 🟢 (Optional) request community memberships
From <https://zenodo.org/records/20387847>, click *Edit* →
*Communities* → request inclusion in any existing communities you
want this record to be visible in.

### 8.6 🟢 Add the arXiv DOI later
Once arXiv assigns an identifier, edit the record and add a row to
*Related identifiers*: `isSupplementTo / arXiv:XXXX.XXXXX`.

---

## 9. What can never be edited (so we got it right the first time) ✅

The following are immutable post-publication on Zenodo:

| Locked field | Our value | Verdict |
|---|---|---|
| Version DOI               | `10.5281/zenodo.20387847`        | ✅ |
| Files (content + names)   | 45 files, 3.96 MB               | ✅ |
| Publication date          | 2026-05-26                       | ✅ |
| Version string            | `1.0`                            | ✅ |

(Title, description, keywords, related identifiers, communities,
authors, license — all editable via *Edit record*.)

---

## 10. Final verdict

The record is **publishable as-is** for arXiv cross-references and
collaborator links, but the description's claim that it supersedes
an unrelated DOI is a real factual error that should be corrected
in the next edit pass. Once §8.1 and §8.2 are applied, the record
will be fully accurate and ready for permanent citation.

| Severity | Issue | Action |
|---|---|---|
| 🔴 Must fix | Description supersession claim (unrelated DOI) | Edit description |
| 🟡 Should fix | Title trailing "(v2.0)" | Edit title |
| 🟢 Nice to add | `difference operator` + `reproducible research` keywords | Add in same pass |
| 🟢 Nice to do | Propagate DOI through repo | Run `doi_propagation_commands.sh` |
| 🟢 Future    | Add arXiv `isSupplementTo` when posted | New related-id row |
