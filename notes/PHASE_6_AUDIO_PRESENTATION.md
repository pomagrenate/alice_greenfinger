# ALICE GREENFINGERS - AUDIO PRESENTATION SPECIFICATION (STEP 13)

*Generated on 2026-09-01*

## 1. Audio Presentation Architecture
- **Header / Implementation:** `include/audio/fmod_system.h` & `src/audio/fmod_system.cpp`.
- **Status Word:** `DAT_004b1200` (`1` = enabled, `0` = disabled).
- **Presentation Rule:** The GUI window and rendering pipeline operate fully independent of audio availability; if FMOD DLL or audio hardware is absent, playback calls gracefully no-op while preserving state register integrity.
