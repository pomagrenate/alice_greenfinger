# ALICE GREENFINGERS - COMPLETE SUBSYSTEM INVENTORY (STEP 2)

*Generated on 2026-09-01 18:00:28*

## 1. UNIFIED SUBSYSTEM CATALOG

| Subsystem ID | Subsystem Name | Primary Source File | Primary Function | Primary Globals | Evidence Level |
| :---: | :--- | :--- | :--- | :--- | :---: |
| `SUB-01` | Process Startup / Boot | `src/platform/win32_boundary.cpp` | `Platform_Initialize` | `DAT_004974f4` | **[E1/E3]** |
| `SUB-02` | Platform Window Context | `src/platform/window.cpp` | `Window_Create / Window_PollEvents` | `None` | **[E1/E3]** |
| `SUB-03` | Input Event Queue | `src/platform/input.cpp` | `Input_PushEvent / Input_PollEvent` | `None` | **[E1/E3]** |
| `SUB-04` | Event Dispatcher | `src/events/event_dispatcher.cpp` | `FUN_00404170` | `DAT_004974f4, DAT_004a86a4` | **[E1/E3]** |
| `SUB-05` | Game State Machine | `src/state/game_state.cpp` | `State_SetState / State_GetCurrentState` | `DAT_004974f4` | **[E1/E3]** |
| `SUB-06` | Simulation Loop & Clock | `src/engine/game_loop.cpp` | `GameLoop_Tick / FUN_004096a0` | `DAT_004a7f54` | **[E1/E3]** |
| `SUB-07` | Farm Grid & Crop Sim | `src/rendering/renderer.cpp` | `5x8 Soil Grid Simulation` | `DAT_004a7f54` | **[E1/E3]** |
| `SUB-08` | Economy Ledger | `src/events/event_dispatcher.cpp` | `DAT_004a86a4 +/- Arithmetic` | `DAT_004a86a4` | **[E1/E3]** |
| `SUB-09` | Market & Vendor Shop | `src/state/game_state.cpp` | `STATE_SHOP_MARKET (5)` | `DAT_004974f4, DAT_004a86a4` | **[E1/E3]** |
| `SUB-10` | Resource Loader (LBTC) | `src/resources/resource_loader.cpp` | `FUN_004033c0` | `DAT_00497528` | **[E1/E4]** |
| `SUB-11` | Animation Runtime | `src/rendering/animation.cpp` | `Animation_GetActiveSprite` | `DAT_004a7f54` | **[E1/E4]** |
| `SUB-12` | Software Renderer | `src/rendering/renderer.cpp` | `Renderer_RenderFrame` | `DAT_004974f4, DAT_004a7f54, DAT_004a86a4` | **[E1/E3]** |
| `SUB-13` | Audio Subsystem Host | `src/audio/fmod_system.cpp` | `FUN_00411000` | `DAT_004b1200` | **[E1/E3]** |
| `SUB-14` | Save / Load Persistence | `src/resources/resource_loader.cpp` | `FUN_004037a0` | `None` | **[E1/E4]** |
| `SUB-15` | Telemetry & Unresolved | `unresolved/unresolved_calls.cpp` | `Unresolved_RecordCall` | `None` | **[E1/E2]** |
