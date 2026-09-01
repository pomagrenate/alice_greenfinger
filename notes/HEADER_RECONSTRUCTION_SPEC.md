# ALICE GREENFINGERS - HEADER RECONSTRUCTION SPECIFICATION (STEP 15)

*Generated on 2026-09-01 13:47:59*

## PROPOSED RECONSTRUCTION HEADER TREE

```
reconstructed/include/
├── platform_types.h       // Primitive types & OS definitions
├── recovered_globals.h    // Static global variable declarations
├── recovered_objects.h    // Class_EngineContext structure map
├── recovered_vtables.h    // VTable slot pointer definitions
├── event_system.h         // Event dispatcher FUN_00404170 header
├── state_system.h         // Game state machine enum & handlers
├── resource_system.h      // PopCap .gfx parser FUN_004033c0 header
├── rendering.h            // Render loop FUN_004096a0 header
└── audio.h                // FMOD wrapper FUN_00411000 header
```
