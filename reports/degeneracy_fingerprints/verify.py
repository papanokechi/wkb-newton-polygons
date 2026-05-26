import json
data = json.load(open('fingerprints.json'))
print(f'Records: {len(data)}')
for r in data:
    print(f'  {r["key"]:25s} chi={r["chi"]:25s} chi_w={r["chi_w"]:25s} rigidity={r["rigidity_class"]}')
    assert len(r['fingerprint_vector']) == len(r['fingerprint_vector_layout']), f'Length mismatch in {r["key"]}'
    print(f'    fp_vec length {len(r["fingerprint_vector"])} OK')

# Verify all four fingerprint vectors are distinct
vecs = [tuple(r['fingerprint_vector']) for r in data]
assert len(set(vecs)) == 4, "Fingerprints not all distinct!"
print('All four fingerprints are pairwise distinct.')

# Verify cross-checks against Phase-1 properties
expected = {
    "STRESS_zeroroot":       {"d": 4, "q": 2, "r": 2, "C_n": 2, "rigidity": "rigid_codim_1"},
    "STRESS_doubleroot":     {"d": 9, "q": 3, "r": 3, "C_n": 3, "rigidity": "rigid_codim_1"},
    "STRESS_equalmod":       {"d": 6, "q": 2, "r": 3, "C_n": 2, "rigidity": "real_only"},
    "STRESS_accidental_sym": {"d": 6, "q": 2, "r": 3, "C_n": 6, "rigidity": "very_rigid"},
}
for r in data:
    e = expected[r["key"]]
    assert r["d"] == e["d"], f'{r["key"]}: d mismatch'
    assert r["q"] == e["q"], f'{r["key"]}: q mismatch'
    assert r["r"] == e["r"], f'{r["key"]}: r mismatch'
    assert r["C_n_observed"] == e["C_n"], f'{r["key"]}: C_n mismatch'
    assert r["rigidity_class"] == e["rigidity"], f'{r["key"]}: rigidity mismatch ({r["rigidity_class"]} vs {e["rigidity"]})'
print('All Phase-1 cross-checks passed.')
