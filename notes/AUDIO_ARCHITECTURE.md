# ALICE GREENFINGERS - AUDIO ARCHITECTURE (STEP 11)

*Generated on 2026-09-01 13:47:51*

## FMOD AUDIO INTEGRATION ARCHITECTURE

- **Wrapper Function:** `FUN_00411000` (FMOD Audio Subsystem Host)
- **Imported APIs:** `_FSOUND_Sample_Load@20`, `_FSOUND_PlaySound@8`, `_FSOUND_Close@0`
- **Audio Channels:** Sound Effects (SFX) & Background Music (BGM)
- **State Binding:** Triggered via Opcode events in `FUN_00404170`
