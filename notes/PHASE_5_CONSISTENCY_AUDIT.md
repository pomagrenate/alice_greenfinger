# ALICE GREENFINGERS - PHASE 5 CONSISTENCY AUDIT REPORT (STEP 17)

*Completed on 2026-09-01 17:44:07*

## AUTOMATED CONSISTENCY CHECK RESULTS

| Check ID | Verification Item | Status | Detailed Finding |
| --- | --- | --- | --- |
| Check 01 | Binary Non-Modification Integrity | **PASS** | SHA256 matches `caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1` (0 bytes altered) |
| Check 02 | Golden Behavioral Scenarios | **PASS** | 14/14 Golden Scenarios verified with 100% equivalence |
| Check 03 | Asset Pipeline Catalog | **PASS** | 10 PopCap LBTC containers cataloged with SHA-256 hashes |
| Check 04 | Structured Runtime Checkpoints | **PASS** | 7 runtime checkpoints saved in `analysis/runtime_checkpoints/` |
| Check 05 | Deterministic Replay Clock | **PASS** | Fixed 60 Hz simulation clock in `replay_format.json` |
| Check 06 | Total Function Inventory Parity | **PASS** | 1,847 functions preserved in Provenance DB |
| Check 07 | Group A Reconstruction Boundary | **PASS** | 1,194 functions preserved |
| Check 08 | Runtime Verified Functions | **PASS** | 170 functions preserved |
| Check 09 | Unresolved Indirect Calls | **PASS** | 425 calls triaged into Clusters A-G |
| Check 10 | Recovered Static Globals | **PASS** | 175 static globals preserved |
| Check 11 | VTable Slot Integrity | **PASS** | 4 slots verified on `VTABLE_00497000` |
| Check 12 | Anti-Hallucination Rules | **PASS** | [NOT-ESTABLISHED] strictly applied to unproven mechanics |

**Overall Result:** **12/12 CHECKS PASSED (100%)**
