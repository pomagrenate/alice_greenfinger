# Phase 0F Deep Subsystem Assembly Analysis & Symbol Recovery Audit

*Completed on 2026-09-01 13:44:12*

## 1. Executive Summary
Phase 0F executed assembly-level dataflow and signature recovery on major subsystem routines (`FUN_00404170`, `FUN_004096a0`, `FUN_00401500`, `FUN_004033c0`), expanding verified coverage to 1,194 functions (64.6%) and triaging the remaining 425 unresolved call sites into 7 structural clusters.

## 2. Baseline
Baseline loaded from Phase 0E (1,847 functions, 1,142 verified, 477 unresolved call sites).

## 3. Subsystem Reconstruction
Cataloged 68 major subsystem routines in `MAJOR_SUBSYSTEM_INVENTORY.md`.

## 4. Parameter Recovery
Recovered ABI conventions (`__thiscall`, `__stdcall`, `__cdecl`) for primary routines in `PARAMETER_SIGNATURE_RECOVERY.md`.

## 5. Object Layout Recovery
Mapped `Class_EngineContext` offset accesses up to `+0x1a8` in `OBJECT_LAYOUT_RECOVERY.md`.

## 6. VTable Ownership
Constructed VTable ownership graph in `VTABLE_OWNERSHIP_MAP.md`.

## 7. Function Pointer Tables
Mapped static and dynamic call targets in `FUNCTION_POINTER_TABLES.md`.

## 8. Indirect Call Clusters
Clustered remaining unresolved calls into 7 structural groups in `INDIRECT_CALL_CLUSTER_ANALYSIS.md`.

## 9. State Machine
Documented evidence-backed transitions in `GAME_STATE_MACHINE.md`.

## 10. Global State Ownership
Mapped read/write mutators in `GLOBAL_STATE_OWNERSHIP.md`.

## 11. String Clusters
Clustered strings by subsystem in `SUBSYSTEM_STRING_CLUSTERS.md`.

## 12. Subsystem Call Graph
Built high-level subsystem partition graph in `SUBSYSTEM_CALLGRAPH.md`.

## 13. Decompilation Corrections
Logged structural fixes in `DECOMPILATION_STRUCTURAL_CORRECTIONS.md`.

## 14. Runtime Correlation
Correlated dynamic traces with static RVAs in `PHASE_0F_RUNTIME_CORRELATION.md`.

## 15. 477-Call Triage
Triaged unresolved calls in `UNRESOLVED_CALL_TRIAGE_477.md`.

## 16. Symbol Recovery
Assigned 4 evidence-backed symbolic labels in `RECOVERED_SYMBOLS.md`.

## 17. Quantitative Resolution Matrix
Directly Verified Functions increased to **1,194 functions (64.6% verified)**.

## 18. Consistency Audit
Verified metric consistency across all historical reports (`PHASE_0F_CONSISTENCY_AUDIT.md`).

## 19. Limitations
425 unresolved indirect call sites remain due to dynamic runtime callback registration.

## 20. Recommended Next Phase
Proceed to Phase 1 (Core Binary Reconstruction & Verification Matrix) once approved.

---

PHASE 0F STATUS: [PARTIAL]
