# ALICE GREENFINGERS - PHASE 4 TARGET FUNCTIONS (STEP 2)

*Generated on 2026-09-01 17:35:24*

| Function ID | RVA | Category | Subsystem Role | Decompiled Lines | Evidence Level |
| --- | --- | --- | --- | ---: | --- |
| `FUN_004096a0` | `0x004096a0` | `SIMULATION_RENDER` | 60 Hz Main World Frame Render & Tile/Layer Update Loop | 484 | **[Ghidra decompilation + runtime execution trace]** |
| `FUN_00404170` | `0x00404170` | `EVENT_DISPATCH` | Opcode & UI Event Callback Dispatcher | 2408 | **[String xrefs ('ADLIBREGISTER', 'GUICTRLSETDATA') + runtime UI trace]** |
| `FUN_00401500` | `0x00401500` | `SCRIPT_HOST` | Script Engine Host & Control Initializer | 333 | **[Ghidra decompilation + Win32 class registration]** |
| `FUN_004033c0` | `0x004033c0` | `RESOURCE_LOADER` | PopCap GFX Container / LBTC Archive Parser | 209 | **[Magic 'LBTC' header check + sprite atlas handle assignment]** |
| `FUN_004037a0` | `0x004037a0` | `PERSISTENCE_IO` | File Stream Header Reader (ReadFile wrapper) | 150 | **[Direct Win32 ReadFile API call with error handling]** |
| `FUN_00403910` | `0x00403910` | `PERSISTENCE_IO` | File Buffer Block Reader | 45 | **[Win32 ReadFile block streaming]** |
| `FUN_00403a20` | `0x00403a20` | `MEMORY_ALLOC` | Resource Buffer Allocator & Stream Slicer | 112 | **[Heap allocation & pointer indexing]** |
| `FUN_0040d590` | `0x0040d590` | `ENGINE_INIT` | Engine Context Initializer & VTable Binding | 102 | **[VTABLE_00497000 binding + STATE_STARTUP init]** |
| `FUN_00411000` | `0x00411000` | `AUDIO_FMOD` | FMOD Audio Subsystem Host Wrapper | 45 | **[FMOD DLL exported thunks]** |
| `FUN_004165c1` | `0x004165c1` | `PLATFORM_ENTRY` | Win32 PE Entry Point & CRT Startup | 15 | **[PE Optional Header AddressOfEntryPoint]** |
