# ALICE GREENFINGERS - REGISTER & STACK DATAFLOW ANALYSIS (STEP 4)

*Generated on 2026-09-01*

## 1. Primary Register Usage Conventions
- **`ECX` Register (`__thiscall`):** Holds the base address of `Class_EngineContext` across engine initialization (`FUN_0040d590`), frame rendering (`FUN_004096a0`), and event dispatch (`FUN_00404170`).
- **`EAX` Register:** Holds return status codes (`1` = handled/success, `0` = unhandled/default) and integer return values.
- **`EDX` / `EBX` Registers:** Used as scratch registers for arithmetic and intermediate pointer calculation.
- **`ESI` / `EDI` Registers:** Preserved across calls; used for string searching (`rep cmpsb`) and memory block copies (`rep movsd`).
- **Stack Offsets:** Local scratch variables stored at `[ebp-4]`, `[ebp-8]`, `[ebp-12]`; parameters passed at `[ebp+8]`, `[ebp+12]`, `[ebp+16]`.
