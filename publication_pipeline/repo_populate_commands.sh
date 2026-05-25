#!/usr/bin/env bash
# ============================================================================
# repo_populate_commands.sh
#
# Populates the public GitHub repository papanokechi/wkb-newton-polygons
# with the full workspace contents and pushes the v2.0 initial release.
#
# Requirements:
#   - The repo created by repo_creation_commands.sh exists.
#   - git installed and configured (user.name, user.email).
#   - This script is executed from the workspace root (where paper/,
#     arxiv_bundle/, ... directories live).
# ============================================================================

set -euo pipefail

REPO_OWNER="papanokechi"
REPO_NAME="wkb-newton-polygons"
REMOTE_URL="https://github.com/${REPO_OWNER}/${REPO_NAME}.git"
PP="publication_pipeline"

# ---- 1. Stage canonical paper.tex as paper/manuscript.tex -------------------
# The manuscript is canonically named paper.tex in the workspace; the
# public release exposes it as manuscript.tex (matching the Zenodo file
# naming convention).
if [ ! -f paper/manuscript.tex ]; then
    cp paper/paper.tex paper/manuscript.tex
fi
if [ ! -f paper/manuscript.pdf ]; then
    cp paper/paper.pdf paper/manuscript.pdf
fi
if [ ! -f paper/manuscript.bbl ]; then
    cp paper/paper.bbl paper/manuscript.bbl
fi
# references.bib already at paper/references.bib

# ---- 2. Drop in repo-level metadata files -----------------------------------
cp "${PP}/repo_file_contents/.gitignore"      .gitignore
cp "${PP}/repo_file_contents/README.md"       README.md
cp "${PP}/repo_file_contents/CITATION.cff"    CITATION.cff
cp "${PP}/repo_file_contents/CONTRIBUTING.md" CONTRIBUTING.md
cp "${PP}/repo_file_contents/CHANGELOG.md"    CHANGELOG.md

# LICENSE-CODE and LICENSE-TEXT live at workspace root already.

# ---- 3. Drop in folder-level READMEs ----------------------------------------
for d in paper arxiv_bundle journal_bundle data reports figures code fleets; do
    if [ -f "${PP}/repo_file_contents/${d}/README.md" ]; then
        cp "${PP}/repo_file_contents/${d}/README.md" "${d}/README.md"
    fi
done

# ---- 4. Initialise git, set remote, push ------------------------------------
git init -b main
git remote add origin "${REMOTE_URL}"

# Add everything except files matched by .gitignore.
git add -A

# Sanity-check what's being committed (informative; doesn't gate the commit).
git status --short | head -200

git -c user.name="papanokechi" \
    -c user.email="papanokechi@users.noreply.github.com" \
    commit \
    -m "Initial public release (v2.0): camera-ready manuscript + dataset" \
    -m "" \
    -m "Includes the camera-ready LaTeX manuscript (26 pp, 897 KB), the full" \
    -m "Phase I-V computational atlas (19 JSON artifacts, ~2.6 MB), the" \
    -m "arXiv and journal submission bundles, fleet scripts (fleet1..5),"  \
    -m "phase reports, the eight in-manuscript theorem proofs, and the"   \
    -m "Round-1 + Round-2 referee revision packages."                     \
    -m ""                                                                  \
    -m "Companion Zenodo dataset: 10.5281/zenodo.XXXXXXX (v2.0)."          \
    -m ""                                                                  \
    -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"

git push -u origin main

# ---- 5. Tag the v2.0 release ------------------------------------------------
git tag -a v2.0 -m "v2.0: camera-ready release"
git push origin v2.0

# ---- 6. Optionally create a GitHub release ----------------------------------
gh release create v2.0 \
    --title "v2.0 — camera-ready release" \
    --notes-file "${PP}/release_notes_v2.0.txt"

echo "Repository populated and v2.0 release published."
echo "URL: https://github.com/${REPO_OWNER}/${REPO_NAME}"
