# ALICE GREENFINGERS - AUDIO BOUNDARY SPECIFICATION (STEP 11)

*Generated on 2026-09-01*

## 1. Audio System Architecture
- **Host Wrapper:** `FUN_00411000` initializes FMOD sound system.
- **Status Word:** `DAT_004b1200` (`1` = active, `0` = inactive/muted).
- **APIs Wrapped:** `_FSOUND_Sample_Load@20`, `_FSOUND_PlaySound@8`, `_FSOUND_Close@0`.
- **Headless Fallback:** In headless/test environments, provides a deterministic no-op mock while preserving status registers.
