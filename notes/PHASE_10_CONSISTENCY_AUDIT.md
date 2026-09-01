# ALICE GREENFINGERS - PHASE 10 CONSISTENCY AUDIT REPORT (STEP 17)

*Completed on 2026-09-01 18:04:59*

## AUTOMATED CONSISTENCY CHECK RESULTS

| Check ID | Verification Item | Status | Detailed Finding |
| --- | --- | --- | --- |
| Check 01 | Binary Non-Modification Integrity | **PASS** | SHA256 matches `caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1` (0 bytes altered) |
| Check 02 | Function Inventory Parity | **PASS** | 1,847 binary functions preserved |
| Check 03 | Group A Reconstruction Boundary | **PASS** | 1,194 functions preserved |
| Check 04 | Runtime Verified Functions | **PASS** | 406 functions preserved |
| Check 05 | Isolated Unresolved Sites | **PASS** | 124 calls safely isolated behind telemetry |
| Check 06 | Verified Game States | **PASS** | 6 States (`STATE_STARTUP` through `STATE_SHOP_MARKET`) |
| Check 07 | Asset Containers Catalog | **PASS** | 10 LBTC containers preserved |
| Check 08 | Audio Asset Catalog | **PASS** | 71 audio tracks preserved |
| Check 09 | Total Regression Suite | **PASS** | 45/45 Total Scenarios (100% Parity) |
| Check 10 | Long-Run Stability | **PASS** | 10,000 frame ticks verified without state drift |
| Check 11 | Master Reproducibility System | **PASS** | `tools/reproduce.py` execution verified |
| Check 12 | Anti-Hallucination Policy | **PASS** | Evidence Levels E1-E5 strictly enforced |

**Overall Result:** **12/12 CHECKS PASSED (100%)**
