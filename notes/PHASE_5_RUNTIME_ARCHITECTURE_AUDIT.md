# ALICE GREENFINGERS - RECONSTRUCTION RUNTIME ARCHITECTURE AUDIT (STEP 2)

*Generated on 2026-09-01 17:39:54*

## MODULE-BY-MODULE VERIFICATION & PROVENANCE MATRIX

| Module Name | Source Implementation File | Subsystem Functionality | Evidence Status |
| --- | --- | --- | --- |
| `platform` | `src/platform/win32_boundary.cpp` | Win32 message pump, window class setup, and CRT entry point initialization | **[VERIFIED]** |
| `objects` | `src/objects/engine_context.cpp` | EngineContext layout allocation, VTable 00497000 pointer binding | **[VERIFIED]** |
| `globals` | `src/globals/recovered_globals.cpp` | 175 static global variables (DAT_004974f4, DAT_004a7f54, DAT_00497528, DAT_004a86a4) | **[VERIFIED]** |
| `state` | `src/state/game_state.cpp` | 6-state game state machine (STARTUP, MAIN_MENU, NAME_DIALOG, GAMEPLAY, PAUSE, SHOP_MARKET) | **[VERIFIED]** |
| `events` | `src/events/event_dispatcher.cpp` | Opcode event dispatcher FUN_00404170, string matching, VTable slot +0x08 hook | **[VERIFIED]** |
| `engine` | `src/engine/game_loop.cpp` | 60 Hz frame render tick loop FUN_004096a0 and simulation update | **[VERIFIED]** |
| `resources` | `src/resources/resource_loader.cpp` | PopCap LBTC container extractor FUN_004033c0 and sprite atlas loader | **[VERIFIED]** |
| `rendering` | `src/rendering/directdraw_boundary.cpp` | 3-layer compositing engine (Background, Simulation Sprites, GUI Overlay) | **[RECONSTRUCTED-ABSTRACTION]** |
| `audio` | `src/audio/fmod_system.cpp` | FMOD audio subsystem host wrapper FUN_00411000 and status word DAT_004b1200 | **[VERIFIED]** |
| `recovered` | `src/recovered/recovered_group_a.cpp` | 1,194 Group A recovered functions with typed signatures and RVA provenance | **[VERIFIED]** |
| `unresolved` | `unresolved/unresolved_calls.cpp` | 425 triaged indirect call sites isolated behind telemetry recording stubs | **[ISOLATED-TELEMETRY]** |
