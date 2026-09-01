# ALICE GREENFINGERS - PHASE 15 REPRODUCTION RESULTS (STEPS 13-16)

*Executed on 2026-09-01 19:05:20*

## 1. TEN VERIFICATION GATES SUMMARY

| Gate ID | Verification Gate Item | Status | Verified Finding |
| :--- | :--- | :---: | :--- |
| Gate 01 | Original Binary SHA-256 | **PASS** | Matches `caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1` (0 bytes altered) |
| Gate 02 | Repository Artifact Manifest | **PASS** | `archive_manifest.json` cataloged |
| Gate 03 | Reconstructed Source Build | **PASS** | MinGW-W64 GCC 15.1.0 C++17 build succeeded |
| Gate 04 | Master Regression Suite | **PASS** | 55/55 scenarios passing |
| Gate 05 | Differential Trace Suite | **PASS** | 12/12 execution traces matching (100% event parity) |
| Gate 06 | Symbolic Validation Suite | **PASS** | 12 paths (9 SAT, 3 UNSAT, 0 UNKNOWN) & 10 experiments PASS |
| Gate 07 | Distribution Integrity | **PASS** | Windows & Linux packages validated |
| Gate 08 | Provenance Graph Consistency | **PASS** | 9 nodes, 12 edges, 0 dangling references |
| Gate 09 | Archival Manifest Integrity | **PASS** | Cryptographic hash validated |
| Gate 10 | Post-Execution Binary Integrity | **PASS** | Target binary untouched (0 modified bytes) |

**Overall Status:** **10/10 GATES PASSED (100% REPRODUCIBLE)**
