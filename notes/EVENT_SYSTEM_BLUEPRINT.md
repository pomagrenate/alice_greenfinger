# ALICE GREENFINGERS - EVENT SYSTEM BLUEPRINT (STEP 6)

*Generated on 2026-09-01 13:47:43*

## EVENT DISPATCH PIPELINE

```
Win32 Message Loop / Input Event
    ↓
FUN_00404170 (Engine_EventOpcodeDispatcher)
    ↓
Opcode Lookup ("ADLIBREGISTER" / "GUICTRLSETDATA")
    ↓
VTable Slot +0x08 Dispatch
    ↓
Game State Mutator (DAT_004974f4 / DAT_004a7f54)
```
