# Phase 0E Runtime State Exploration & Coverage Expansion Audit

*Completed on 2026-09-01 13:37:54*

## 1. Objective
Systematically explore deeper runtime states of Alice Greenfingers, trigger unreached code paths, capture concrete indirect call targets, and expand the evidence-backed reconstruction boundary.

## 2. Phase 0D Baseline
Started from baseline of 1,847 functions, 1,110 verified, and 509 unresolved indirect call sites.

## 3. Runtime States Explored
Explored 6 states: `STATE_STARTUP`, `STATE_MAIN_MENU`, `STATE_NAME_DIALOG`, `STATE_GAMEPLAY`, `STATE_PAUSE_OPTIONS`, `STATE_SHOP_MARKET`.

## 4. New Runtime Evidence
Captured 32 newly executed indirect call sites during gameplay and options navigation.

## 5. Newly Resolved Indirect Calls
+32 call sites resolved (`0x004097f0` frame render update, `0x00404210` dialog control listener).

## 6. Static ↔ Dynamic Correlation
Verified 100% address match between static Ghidra RVAs and active process execution addresses.

## 7. VTable / Callback Validation
Confirmed VTable slots `+0x00`, `+0x04`, `+0x08`, `+0x0C`.

## 8. Global State Observations
Observed 5 active global variables (`DAT_004974f4`, `DAT_004a7f54`, etc.) mutated during runtime ticks.

## 9. Function Coverage
Directly Verified Functions increased to **1,142 functions (61.8% verified)**.

## 10. Quantitative Resolution Matrix
Documented in `PHASE_0E_RESOLUTION_MATRIX.md`.

## 11. Remaining Unresolved Logic
477 indirect call sites remain unresolved.

## 12. Evidence Quality
All items classified strictly as `[VERIFIED]`, `[RUNTIME-OBSERVED]`, `[HIGH-CONFIDENCE]`, or `[UNRESOLVED]`.

## 13. Limitations
Logged in `PHASE_0E_LIMITATIONS.md`.

## 14. Reproducibility
Automated script `analysis/phase0e_consistency_audit.py` validates metric consistency across all artifacts.

## 15. Final Status

PHASE 0E STATUS: [PARTIAL]
