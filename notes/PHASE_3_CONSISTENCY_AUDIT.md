# ALICE GREENFINGERS - PHASE 3 CONSISTENCY AUDIT (STEP 17)

*Completed on 2026-09-01 17:25:18*

## AUTOMATED CONSISTENCY CHECK RESULTS

| Check ID | Verification Item | Status | Finding |
| --- | --- | --- | --- |
| Check 01 | Provenance Database Coverage | **PASS** | 1,847 functions mapped in `function_provenance.json` |
| Check 02 | RVA Uniqueness & 1:1 Mapping | **PASS** | 0 duplicate RVAs, 0 duplicate IDs |
| Check 03 | Verified Boundary Baseline | **PASS** | 1,194 Group A functions preserved |
| Check 04 | Runtime Verified Functions | **PASS** | 170 functions runtime-verified |
| Check 05 | Unresolved Indirect Calls | **PASS** | 425 calls triaged into Clusters A-G |
| Check 06 | Static Globals Provenance | **PASS** | 175 static globals declared & defined |
| Check 07 | VTable Slot Integrity | **PASS** | Slots `+0x00`, `+0x04`, `+0x08`, `+0x0C` verified |
| Check 08 | State Machine States | **PASS** | 6 verified states (0..5) |
| Check 09 | Non-Modification Integrity | **PASS** | `AliceGreenfingers_unpacked.exe` intact (732,733 bytes) |
| Check 10 | Call-Graph Edge Integrity | **PASS** | All edges connect valid function nodes |
| Check 11 | Behavioral Differential Tests | **PASS** | 100% assertions passed |
| Check 12 | Anti-Hallucination Rules | **PASS** | All inferences strictly labelled |

**Overall Result:** **12/12 CHECKS PASSED (100%)**
