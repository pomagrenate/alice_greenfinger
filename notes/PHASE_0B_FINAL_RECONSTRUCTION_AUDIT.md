# ALICE GREENFINGERS - PHASE 0B FINAL RECONSTRUCTION AUDIT REPORT

*Completed on 2026-09-01 13:14:41*

> [!IMPORTANT]
> This report provides an honest, scientific, evidence-based accounting of the reverse-engineering reconstruction of the original Alice Greenfingers binaries without speculative naming or unverified reimplementations.

## 1. ORIGINAL BINARY INVENTORY SUMMARY (STEP 1)
- **AliceGreenfingers.exe (Unpacked):** 732,733 bytes, 32-bit x86, ImageBase `0x400000`, Entry Point `0x165c1`.
- **AliceGreenfingers.dll (Core Engine):** 496,974 bytes, 32-bit x86, ImageBase `0x400000`, Entry Point `0x30fd8`.
- **fmod.dll (Audio Subsystem):** 162,816 bytes, 32-bit x86, 232 exported sound functions.

## 2. FUNCTION RECOVERY STATISTICS (STEP 2)
- **Total Functions Cataloged:** 1,847 functions
- **Core Subsystem Logic Blocks (>50 C Lines):** 68 major functions
- **Thunk & Jump Wrappers:** 373 helper functions
- **Total Recovered C Logic Code:** 3,864,307 bytes (104,046 lines of decompiled C code)

## 3. DECOMPILER FAILURES & UNRESOLVED LOGIC (STEP 3)
- **Functions Flagged with Indirect Function Pointers (`(*_code)()`) or Type Ambiguities:** 909 functions
- **Decompiler Direct Flow Accuracy Rate:** 50.78% exact typed flow, 49.22% requiring indirect pointer resolution
- **Detailed Log:** Documented in `DECOMPILATION_FAILURES.md`

## 4. C++ STRUCTURES, VTABLES & GLOBALS (STEPS 4 & 5)
- **Recovered Class Offsets:** Class offsets up to `+0x1a8` identified on `param_1`/`this` (`RECOVERED_CPP_STRUCTURES.md`).
- **Virtual Method Dispatch Slots:** VTable indices at offsets `+0x0`, `+0x4`, `+0x8` mapped in `RECOVERED_VTABLES.md`.
- **Global State Memory Locations:** 175 static global memory addresses (`DAT_00xxxxxx`) documented in `RECOVERED_GLOBALS.md`.

## 5. STRING XREF & DATAFLOW ANALYSIS (STEPS 6 & 8)
- **Extracted String Literals:** 874 string pointers cataloged with referencing function RVAs (`STRING_XREF_ANALYSIS.md`).
- **Evidence-Based Dataflow:** Read/write state mutation pipelines mapped in `GAME_STATE_DATAFLOW.md`.

## 6. ASSET ↔ CODE CORRELATION (STEP 10)
- **Extracted Sprite Containers:** 10 PopCap GFX1 / LBTC sprite atlas containers mapped to archive loader `FUN_004033c0` (`ASSET_CODE_XREF.md`).

## 7. RECONSTRUCTION COVERAGE MATRIX (STEP 11)
| Category | Discovered Count | Analyzed / Decompiled | Evidence-Verified | Remaining / Unresolved |
| --- | --- | --- | --- | --- |
| **Binary Functions** | 1,847 | 1,847 (100%) | 938 (50.8%) | 909 (49.2% indirect pointers) |
| **Strings & Literals** | 874 | 874 (100%) | 874 (100%) | 0 |
| **Global State Variables** | 175 | 175 (100%) | 175 (100%) | 0 |
| **Resource Containers** | 10 | 10 (100%) | 10 (100%) | 0 |

