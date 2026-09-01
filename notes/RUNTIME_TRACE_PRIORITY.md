# ALICE GREENFINGERS - RUNTIME TRACE PRIORITY TIERS (STEP 4)

*Generated on 2026-09-01 13:29:44*

| Tier | Target Subsystem / Function | Priority Focus | Execution Trigger |
| --- | --- | --- | --- |
| **P0** | `FUN_00404170`, `FUN_004096a0` | Event Loop & Primary Render Frame | Automatic / Engine Startup |
| **P1** | Subroutines reachable from P0 | VTable Dispatches at offsets `+0x04`, `+0x08` | Frame Render Update |
| **P2** | Script / Event Handlers | `"ADLIBREGISTER"`, `"GUICTRLSETDATA"` | UI Widget Interaction |
| **P3** | Global State Mutators | Static Memory Addresses (`DAT_00xxxxxx`) | Game State Transitions |
