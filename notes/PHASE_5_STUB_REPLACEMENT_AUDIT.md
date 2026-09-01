# ALICE GREENFINGERS - STUB REPLACEMENT & INDIRECT CALL AUDIT (STEP 3)

*Generated on 2026-09-01 17:39:54*

## INDIRECT CALL TRIAGE & RESOLUTION STATUS

| Cluster Category | Site Count | Reconstructed Resolution | Resolution Finding |
| --- | ---: | --- | --- |
| **Cluster A (VTable Dispatch)** | 142 | 4 primary slots (+0x00, +0x04, +0x08, +0x0C) | Direct dispatch implemented for EngineContext; remaining slots isolated. |
| **Cluster B (Script/Opcode Callbacks)** | 98 | ADLIBREGISTER, GUICTRLSETDATA, GUICTRLSETSTATE | Token matchers implemented in event_dispatcher.cpp; dynamic scripts isolated. |
| **Cluster C (GUI Control Hooks)** | 85 | Button/Menu/Dialog click handlers | Routed to State_SetState; dynamic control callbacks isolated. |
| **Cluster D (Resource Decoders)** | 54 | FUN_004033c0 (LBTC parser) | LBTC header validation implemented in resource_loader.cpp; decompression isolated. |
| **Cluster E (Win32 API Pointers)** | 46 | Direct Win32 API binding (GetTickCount, ReadFile, WriteFile) | Bound to native platform functions; legacy stubs safe. |
| **Cluster F (State Transitions)** | 32 | State machine transition dispatchers (States 0..5) | Direct State_SetState dispatch; dynamic state callbacks isolated. |
| **Cluster G (Isolated Stack Pointers)** | 20 | 0 (isolated) | Strictly isolated behind Unresolved_RecordCall. |
