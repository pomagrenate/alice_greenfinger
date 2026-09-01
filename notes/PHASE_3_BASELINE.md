# ALICE GREENFINGERS - PHASE 3 BASELINE AUDIT REPORT (STEP 1)

*Generated on 2026-09-01 17:25:01*

## 1. PHASE 2 INHERITED BASELINE METRICS

- **Total Binary Functions:** 1,847 (100% cataloged)
- **Group A Direct C Reconstructed:** 1,194 (64.6% coverage)
- **Runtime Verified Routines:** 170 (9.2% execution coverage)
- **Unresolved Indirect Call Sites:** 425 (Triaged into Clusters A–G)
- **Mapped VTable Slots:** 4 (`+0x00`, `+0x04`, `+0x08`, `+0x0C` on `VTABLE_00497000`)
- **Recovered Static Globals:** 175 (`DAT_00xxxxxx`)
- **Extracted String Literals:** 874 strings
- **Modular Source Tree:** 11 C/C++ modules compiling cleanly via CMake / Ninja
- **Non-Modification Rule:** 100% verified (0 bytes altered in `AliceGreenfingers_unpacked.exe`)

## 2. PHASE 3 OBJECTIVES
1. Progressively replace structural telemetry stubs with verified behavioral implementations.
2. Construct function-by-function provenance database and behavioral call-graph.
3. Deeply audit core execution anchors (`FUN_00404170`, `FUN_004096a0`, `FUN_00401500`, `FUN_004033c0`).
4. Reconstruct gameplay simulation, rendering pipeline, event dispatch, and resource decompression.
5. Execute behavioral differential verification against original binary.
