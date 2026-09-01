# Alice Greenfingers — Reproducibility Specification

## 1. Master Verification Command
```bash
python tools/reproduce.py
```

## 2. Ten Verification Gates
1. **Gate 1 — Original Binary SHA-256:** Verifies `caf0c6f7...` (0 modified bytes).
2. **Gate 2 — Reconstructed Source Build:** Verifies clean CMake/Ninja build.
3. **Gate 3 — Distribution Packaging:** Verifies Windows and Linux standalone distribution creation.
4. **Gate 4 — Master Regression Suite:** Verifies 55/55 regression scenarios pass.
5. **Gate 5 — Consistency Audit:** Verifies repository integrity and cross-references.
6. **Gate 6 — Differential Trace Audit:** Verifies 12/12 scenario trace matches.
7. **Gate 7 — Symbolic Execution Audit:** Verifies 12 symbolic paths and 0 replay mismatches.
8. **Gate 8 — Post-Execution Binary Check:** Confirms read-only status.
9. **Gate 9 — Provenance Graph Audit:** Verifies 0 dangling dependencies in graph.
10. **Gate 10 — Archival Manifest Audit:** Verifies canonical cryptographic hashes.
