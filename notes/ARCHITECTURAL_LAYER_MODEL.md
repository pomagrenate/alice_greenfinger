# ALICE GREENFINGERS - ARCHITECTURAL LAYER MODEL (STEP 2)

*Generated on 2026-09-01 13:47:32*

## 10-LAYER ARCHITECTURAL STACK

| Layer Level | Layer Name | Core Functions | Primary Role | Confidence |
| --- | --- | --- | --- | --- |
| **Layer 1** | Process & Win32 Platform | `EntryPoint`, Win32 API Imports | Process Lifecycle & Heap | **[VERIFIED]** |
| **Layer 2** | Engine Initialization | `FUN_0040d590` | Subsystem Setup & VPtr Binding | **[VERIFIED]** |
| **Layer 3** | Resource & Archive System | `FUN_004033c0` | PopCap GFX Archive Extraction | **[VERIFIED]** |
| **Layer 4** | Object & GUI Framework | `FUN_00401500` | UI Control Management | **[VERIFIED]** |
| **Layer 5** | Event & Callback Dispatch | `FUN_00404170` | Opcode & Listener Dispatch | **[VERIFIED]** |
| **Layer 6** | Game State Management | State Machine Mutators | State Values 0..3 Transitions | **[VERIFIED]** |
| **Layer 7** | Gameplay Logic Engine | Grid Tile Handlers | Planting / Harvesting Rules | **[HIGH-CONFIDENCE]** |
| **Layer 8** | Rendering Engine | `FUN_004096a0` | Surface Blitting & Frame Render | **[VERIFIED]** |
| **Layer 9** | Audio & FMOD Integration | `FUN_00411000` | Sample Loading & Music Playback | **[VERIFIED]** |
| **Layer 10**| Persistence & Configuration | File I/O Helpers | Profile Save / Load | **[HIGH-CONFIDENCE]** |
