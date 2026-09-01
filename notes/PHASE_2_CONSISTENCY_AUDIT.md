# ALICE GREENFINGERS - PHASE 2 CONSISTENCY AUDIT REPORT (STEP 18)

*Generated on 2026-09-01 17:11:45*

## AUTOMATED CONSISTENCY CHECK RESULTS

| Check ID | Verification Item | Status | Detailed Finding |
| --- | --- | --- | --- |
| Check 01 | Function ID <-> RVA 1:1 Mapping & Total Count | **PASS** | 1,847 functions loaded, 0 duplicate RVAs, 0 duplicate IDs. |
| Check 02 | Generated Header RVA Manifest Integrity | **PASS** | 1854 RVA definitions found in recovered_addresses.h. |
| Check 03 | Global State Variable Provenance (175 Globals) | **PASS** | 175 globals documented with provenance and extern declarations. |
| Check 04 | VTable Slot Offset Integrity (+0x00, +0x04, +0x08, +0x0C) | **PASS** | All 4 virtual method dispatch slots verified on VTABLE_00497000. |
| Check 05 | Unresolved Call Registry Parity (425 Calls) | **PASS** | 425 unresolved indirect call sites isolated behind telemetry stubs across Clusters A-G. |
| Check 06 | Group A Verified Reconstruction Boundary (1,194 Functions) | **PASS** | 1194 functions in Group A verified boundary (64.6% coverage). |
| Check 07 | Runtime-Verified Function Coverage (170 Functions) | **PASS** | 170 functions verified via dynamic runtime execution traces. |
| Check 08 | Source Module Directory Blueprint Alignment | **PASS** | All 11 modular source files exist matching Phase 1 blueprint. |
| Check 09 | Original Binary Non-Modification Integrity | **PASS** | Target AliceGreenfingers_unpacked.exe is intact (732,733 bytes, 0 modifications). |
| Check 10 | Anti-Hallucination Provenance Headers in Reconstructed Source | **PASS** | Every reconstructed function includes provenance comments, original RVAs, and confidence ratings. |

**Overall Result:** **10/10 CHECKS PASSED (100%)**
