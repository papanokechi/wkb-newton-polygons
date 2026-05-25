#!/usr/bin/env bash
# ============================================================================
# doi_propagation_commands.sh
#
# After Zenodo assigns the v2.0 DOI, run this script to propagate it
# across the workspace.  Pass the new DOI as the first argument:
#
#     bash doi_propagation_commands.sh 10.5281/zenodo.1234567
#
# The script substitutes the placeholder "10.5281/zenodo.XXXXXXX" (and
# the matching URL form) in every relevant file, commits the change,
# and re-tags the v2.0 release.
#
# Safe to run from the project root.  Requires git.
# ============================================================================

set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: bash doi_propagation_commands.sh <NEW_DOI>"
    echo "Example: bash doi_propagation_commands.sh 10.5281/zenodo.1234567"
    exit 1
fi

NEW_DOI="$1"
PLACEHOLDER="10.5281/zenodo.XXXXXXX"
PLACEHOLDER_URL="https://doi.org/${PLACEHOLDER}"
NEW_URL="https://doi.org/${NEW_DOI}"

echo "Propagating DOI:"
echo "    placeholder: ${PLACEHOLDER}"
echo "    new        : ${NEW_DOI}"
echo

# ---- Files to update --------------------------------------------------------
FILES=(
    "paper/manuscript.tex"
    "paper/paper.tex"
    "arxiv_bundle/paper.tex"
    "journal_bundle/paper.tex"
    "paper/references.bib"
    "arxiv_bundle/references.bib"
    "journal_bundle/references.bib"
    "README.md"
    "CITATION.cff"
    "CHANGELOG.md"
    "CONTRIBUTING.md"
    "submission_checklist.md"
    "citation_block.txt"
    "release_notes_v1.0.txt"
    "publication_pipeline/release_notes_v2.0.txt"
    "publication_pipeline/zenodo_metadata_v2.0.txt"
    "publication_pipeline/repo_file_contents/README.md"
    "publication_pipeline/repo_file_contents/CITATION.cff"
    "publication_pipeline/repo_file_contents/CHANGELOG.md"
    "publication_pipeline/repo_file_contents/CONTRIBUTING.md"
    "publication_pipeline/repo_file_contents/data/README.md"
    "publication_pipeline/zenodo_v2_package/README.md"
    "publication_pipeline/zenodo_v2_package/citation_block.txt"
    "publication_pipeline/zenodo_v2_package/zenodo_metadata_v2.0.txt"
    "publication_pipeline/zenodo_v2_package/release_notes_v2.0.txt"
    "publication_pipeline/zenodo_v2_package/CITATION.cff"
)

# ---- Sed-in-place replacement (portable across GNU sed / BSD sed) -----------
for f in "${FILES[@]}"; do
    if [ -f "${f}" ]; then
        # Use a backup suffix and remove it after, to be GNU-/BSD-compatible.
        sed -i.bak \
            -e "s|${PLACEHOLDER}|${NEW_DOI}|g" \
            -e "s|${PLACEHOLDER_URL}|${NEW_URL}|g" \
            "${f}"
        rm -f "${f}.bak"
        echo "  updated  ${f}"
    else
        echo "  skipped  ${f}  (not found)"
    fi
done

# ---- Recompile the paper to bake the new DOI into the PDF -------------------
echo
echo "Recompiling paper/manuscript.tex with new DOI ..."
( cd paper && \
    pdflatex -interaction=nonstopmode -file-line-error manuscript.tex > /dev/null && \
    bibtex manuscript                                                  > /dev/null && \
    pdflatex -interaction=nonstopmode -file-line-error manuscript.tex > /dev/null && \
    pdflatex -interaction=nonstopmode -file-line-error manuscript.tex > /dev/null \
)
# Copy the rebuilt PDF and bbl into the bundles
cp paper/manuscript.pdf paper/paper.pdf
cp paper/manuscript.bbl paper/paper.bbl
cp paper/paper.pdf arxiv_bundle/paper.pdf
cp paper/paper.bbl arxiv_bundle/paper.bbl
cp paper/paper.pdf journal_bundle/paper.pdf
cp paper/paper.bbl journal_bundle/paper.bbl

# ---- Commit and re-tag ------------------------------------------------------
git add -A
git -c user.name="papanokechi" \
    -c user.email="papanokechi@users.noreply.github.com" \
    commit -m "Propagate Zenodo v2.0 DOI: ${NEW_DOI}" \
    -m "" \
    -m "Replaces placeholder 10.5281/zenodo.XXXXXXX with the assigned DOI" \
    -m "across the manuscript, BibTeX, README, CITATION.cff, and pipeline" \
    -m "metadata. Recompiles the PDF and updates the arxiv/journal bundles." \
    -m "" \
    -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"

# Move the v2.0 tag to point at the DOI-propagated commit
git tag -d v2.0 || true
git push origin :refs/tags/v2.0 || true
git tag -a v2.0 -m "v2.0: camera-ready release with assigned DOI ${NEW_DOI}"

git push origin main
git push origin v2.0

echo
echo "Done.  v2.0 tag now points at the DOI-propagated commit."
echo "Visit: https://github.com/papanokechi/wkb-newton-polygons/releases/tag/v2.0"
