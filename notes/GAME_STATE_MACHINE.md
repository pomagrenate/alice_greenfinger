# ALICE GREENFINGERS - RECOVERED GAME STATE MACHINE (STEP 9)

*Generated on 2026-09-01 13:42:30*

## STATE TRANSITION MATRIX

| Current State Value | Trigger Action | Handler Function | Next State Value | Global Mutated | Evidence Classification |
| --- | --- | --- | --- | --- | --- |
| `STATE_00` (Startup) | Engine Boot | `FUN_0040d590` | `STATE_01` (Menu) | `DAT_004974f4` | **[VERIFIED]** |
| `STATE_01` (Menu) | "Start" Click | `FUN_00404170` | `STATE_02` (Dialog) | `DAT_004974f4` | **[VERIFIED]** |
| `STATE_02` (Dialog) | Submit Name | `FUN_00404170` | `STATE_03` (Gameplay) | `DAT_004a7f54` | **[VERIFIED]** |
| `STATE_03` (Gameplay) | Grid Click | `FUN_004096a0` | `STATE_03` (Gameplay) | `DAT_004a7f54` | **[VERIFIED]** |
