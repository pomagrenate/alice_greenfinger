# FUN_00404170 DEEP BEHAVIORAL FORENSIC AUDIT (STEP 4)

*Generated on 2026-09-01*

## 1. Binary Identification & Metadata
- **Function RVA:** `0x00404170` (Base Address `0x00400000`)
- **Subsystem:** `SUBSYS_EVENT_DISPATCH` (Opcode & UI Event Callback Dispatcher)
- **ABI:** `__thiscall` (`ECX` = Context pointer, `param_1` = opcode/message ID, `param_2` = payload)
- **Function Size:** 65,255 bytes decompiled C control flow (2,408 lines)
- **Classification:** **[VERIFIED]** (Static decompilation + runtime UI event traces)

## 2. Call Relationships
- **Callers (4):** `WinMain / EntryPoint`, `FUN_00401500`, `FUN_0040d590`, `EngineContext_EventCallback`
- **Direct Callees (5):** `FUN_00403cd0`, `FUN_00403c90`, `FUN_00408f40`, `FUN_00403d10`, `FUN_00401b10`
- **Indirect Dispatch Sites (Cluster B):** Opcode callback table (`ADLIBREGISTER` runtime registration)

## 3. Control Flow Regions
- **Region 1 (Validation):** Validates input event vector and checks `DAT_004974f4` state.
- **Region 2 (Opcode String Hash/Match):** Matches incoming command tokens against `"ADLIBREGISTER"`, `"GUICTRLSETDATA"`, `"GUICTRLSETSTATE"`, `"WinTitleMatchMode"`.
- **Region 3 (State Mutation):** Sets active game state:
  - Opcode 1001 -> `DAT_004974f4` = 3 (`STATE_GAMEPLAY`)
  - Opcode 1002 -> `DAT_004974f4` = 4 (`STATE_PAUSE_OPTIONS`)
  - Opcode 1003 -> `DAT_004974f4` = 1 (`STATE_MAIN_MENU`)
- **Region 4 (Cleanup):** Restores stack frame and returns status code `1` (success) or `0` (handled).

## 4. Evidence Classification
- Control flow & string matches: **[VERIFIED]**
- Opcode-to-state mutations: **[RUNTIME-OBSERVED]**
- Dynamic script callbacks: **[UNRESOLVED — preserved in telemetry stubs]**
