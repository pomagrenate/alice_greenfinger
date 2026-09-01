# ALICE GREENFINGERS - PHASE 8 BASELINE REPORT (STEP 1)

*Generated on 2026-09-01 17:56:55*

## 1. TARGET BINARY READ-ONLY INTEGRITY

- **Binary Path:** `C:\Users\Admin\Downloads\AliceGreenfingers_RE\extracted\AliceGreenfingers_unpacked.exe`
- **File Size:** 732,733 bytes
- **SHA-256:** `caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1`
- **Integrity Status:** **100% READ-ONLY / UNTOUCHED**

## 2. INHERITED INDIRECT CALL CLUSTER BASELINE (425 Sites)

| Cluster ID | Subsystem Domain | Call Sites | Baseline Status |
| --- | --- | ---: | :---: |
| **Cluster A** | VTable Virtual Dispatch | 142 | Isolated (4 slots recovered on `VTABLE_00497000`) |
| **Cluster B** | Script / Opcode Event Callbacks (`ADLIBREGISTER`) | 98 | Opcode 1001/1002 mapped |
| **Cluster C** | GUI Control Callback Hooks (`GUICTRLSETDATA`) | 85 | Click & Hover bounds mapped |
| **Cluster D** | Resource / Archive Decoders (PopCap LBTC) | 54 | `PopCap_LBTC_Header` recovered |
| **Cluster E** | Win32 API Import Pointers (GDI / User32 / Kernel32) | 46 | Target deterministic via PE IAT |
| **Cluster F** | State Machine Transition Dispatchers | 32 | 6 States verified (`0..5`) |
| **Cluster G** | Stack Function Pointers / Isolated Helpers | 20 | Frame-local callback structures |

## 3. PHASE 8 OBJECTIVES
1. Deep provenance tracking and resolution pass across all 425 sites.
2. Reconstruct Win32 IAT imports (Cluster E), opcode callbacks (Cluster B), and state dispatches (Cluster F).
3. Investigate late-game multi-day progression, trophies, and crop unlocks.
4. Maintain 100% pass across all 34 existing regression scenarios.
