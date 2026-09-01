# ALICE GREENFINGERS - MASTER DIFFERENTIAL AUDIT REPORT (STEP 19)

*Completed on 2026-09-01 18:57:27*

## AUTOMATED DIFFERENTIAL AUDIT RESULTS

| Gate ID | Verification Item | Status | Finding |
| --- | --- | --- | --- |
| Gate 01 | Binary Non-Modification Integrity | **PASS** | SHA256 matches `caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1` (0 bytes altered) |
| Gate 02 | Trace Schema Specification | **PASS** | `trace_schema.json` format validated |
| Gate 03 | Original Trace Provenance | **PASS** | 12 scenarios captured in `traces/original_*.json` |
| Gate 04 | Reconstructed Trace Provenance | **PASS** | 12 scenarios captured in `traces/reconstructed_*.json` |
| Gate 05 | Normalization Engine Filter | **PASS** | Non-deterministic timestamps & host paths filtered |
| Gate 06 | Event-Order Sequence Comparison | **PASS** | 31/31 observable semantic events match 100% |
| Gate 07 | State-Transition Equivalence | **PASS** | States 0..5 transitions match 100% |
| Gate 08 | Economy Ledger Mutations | **PASS** | `DAT_004a86a4` arithmetic matches 100% |
| Gate 09 | Crop Lifecycle Simulation | **PASS** | 5-stage timer progression matches 100% |
| Gate 10 | Save/Load Stream Serialization | **PASS** | `AGSV` binary stream matches 100% |
| Gate 11 | Cross-Backend Semantic Traces | **PASS** | Win32/GDI and SDL2 produce identical traces |
| Gate 12 | Controlled Experiments Registry | **PASS** | 10/10 experiments verified (`EXP13-001`..`EXP13-010`) |

**Overall Verdict:** **12/12 DIFFERENTIAL GATES PASSED (100% MATCH RATE)**
