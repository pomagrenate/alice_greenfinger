# ALICE GREENFINGERS - RUNTIME STARTUP TRACE (STEP 5)

*Generated on 2026-09-01 13:31:48*

## INITIALIZATION SEQUENCE & MODULE LOADING ORDER

| Sequence Step | Module / Event Name | Action Observed | Target Function / API | Evidence Classification |
| --- | --- | --- | --- | --- |
| `0x01` | `AliceGreenfingers_unpacked.exe` | PE Image Loading | EntryPoint (`0x004165c1`) | **[VERIFIED Static/PE]** |
| `0x02` | `KERNEL32.DLL` | Base Environment Init | `GetVersionExW`, `HeapAlloc` | **[VERIFIED Import]** |
| `0x03` | `AliceGreenfingers.dll` | Engine Subsystem Binding | `DirectDrawCreate` / Window Setup | **[VERIFIED Import]** |
| `0x04` | `fmod.dll` | Audio Subsystem Binding | `_FSOUND_Sample_Load@20` | **[VERIFIED Import]** |
| `0x05` | Graphics Container Loader | `.gfx` Container Parsing | `FUN_004033c0` | **[VERIFIED Code Flow]** |
