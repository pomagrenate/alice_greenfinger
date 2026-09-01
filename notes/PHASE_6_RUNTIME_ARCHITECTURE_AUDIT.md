# ALICE GREENFINGERS - RUNTIME ARCHITECTURE AUDIT (STEP 2)

*Generated on 2026-09-01*

## 1. Runtime Subsystem Inventory
- **Platform Layer (`src/platform/win32_boundary.cpp`):** Handles Win32 initialization and engine context lifecycle.
- **Engine Context (`src/objects/engine_context.cpp`):** Manages primary object layout and `VTABLE_00497000` binding.
- **State Machine (`src/state/game_state.cpp`):** Encapsulates the 6 verified states (`0..5`) and transition rules.
- **Event Dispatcher (`src/events/event_dispatcher.cpp`):** Reconstructs `FUN_00404170` opcode string matching and VTable slot `+0x08` callback dispatch.
- **Game Loop (`src/engine/game_loop.cpp`):** Implements `FUN_004096a0` 60 Hz frame render tick and simulation advancement (`DAT_004a7f54++`).
- **Resource Pipeline (`src/resources/resource_loader.cpp`):** Reconstructs `FUN_004033c0` with `PopCap_LBTC_Header` and `PopCap_Sprite_Entry` parsing.
- **Rendering Boundary (`src/rendering/directdraw_boundary.cpp`):** Provides 3-layer compositing abstraction (Background, Simulation Sprites, GUI Overlay).
- **Audio Boundary (`src/audio/fmod_system.cpp`):** Reconstructs `FUN_00411000` host wrapper and `DAT_004b1200` status flag.
- **Telemetry & Checkpoints:** 425 unresolved calls isolated behind `Unresolved_RecordCall`; structured checkpoint logging in `analysis/runtime_checkpoints/`.
