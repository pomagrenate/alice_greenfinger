# PHASE 0D — DYNAMIC RUNTIME EVIDENCE AUDIT REPORT

*Completed on 2026-09-01 13:32:33*

> [!IMPORTANT]
> Phase 0D has established dynamic runtime evidence correlating static Ghidra control flow with actual execution behavior without modifying original binaries or introducing speculative class names.

## 1. Executive Summary
Phase 0D performed runtime evidence correlation across `AliceGreenfingers_unpacked.exe`. Primary targets `FUN_00404170` and `FUN_004096a0` were observed under execution, resolving 86 indirect call sites into evidence-verified targets.

## 2. Binary Integrity Verification
- `AliceGreenfingers_unpacked.exe` SHA-256 verified in `RUNTIME_BINARY_BASELINE.md`.
- Non-modification policy strictly enforced (0 bytes modified).

## 3. Runtime Environment
- Detected and logged in `RUNTIME_TOOLCHAIN.md`.

## 4. Address Mapping
- ASLR Disabled. 1:1 Static-to-Runtime Address Parity (`0x00400000` Base Image).

## 5. Startup Trace
- Logged in `RUNTIME_STARTUP_TRACE.md`.

## 6. FUN_00404170 Runtime Evidence
- Event dispatcher loop verified hit during UI event triggers.

## 7. FUN_004096a0 Runtime Evidence
- Frame render loop verified continuous execution during active game tick.

## 8. Indirect Call Resolution
- 86 indirect call sites resolved (`RUNTIME_INDIRECT_CALL_TRACE.md`).

## 9. VTable Validation
- VTable slots `+0x00`, `+0x04`, `+0x08` confirmed (`RUNTIME_VTABLE_VALIDATION.md`).

## 10. Callback / Script Dispatch Validation
- Opcode registration for `"ADLIBREGISTER"` and `"GUICTRLSETDATA"` confirmed (`RUNTIME_CALLBACK_VALIDATION.md`).

## 11. Global State Observations
- Static global memory locations (`DAT_004974f4`, `DAT_004a7f54`) verified read/write in `RUNTIME_GLOBAL_STATE_TRACE.md`.

## 12. State-Dependent Dispatch
- 12 state-dependent dispatches mapped (`STATE_DEPENDENT_DISPATCH.md`).

## 13. Static/Dynamic Correlation
- Documented in `STATIC_DYNAMIC_CORRELATION.md`.

## 14. Quantitative Resolution Matrix
- Verified Functions: Increased from 1,024 to **1,110 functions (60.1% verified)**.

## 15. Failed / Blocked Experiments
- 509 call sites remain unresolved due to unreached endgame state triggers (`RUNTIME_TRACE_FAILURES.md`).

## 16. Remaining Unknowns
- 509 dynamic call targets requiring deep gameplay state triggers.

## 17. Evidence Quality
- All findings classified strictly as `[VERIFIED]`, `[HIGH-CONFIDENCE]`, `[INFERRED]`, or `[UNRESOLVED]`.

## 18. Phase 1 Readiness Assessment
- Reconstructed control flow, vtables, event dispatchers, and binary inventory provide a solid, evidence-backed foundation.

---

PHASE 0D STATUS: [PARTIAL]
