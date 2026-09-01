# ALICE GREENFINGERS - RECOVERED VTABLES & VIRTUAL DISPATCH (STEP 4)

*Generated on 2026-09-01 13:12:26*

## VTABLE DISPATCH MATRIX

| VTable Slot Offset | Dispatch Instruction Pattern | Referencing Functions | Subsystem Role |
| --- | --- | --- | --- |
| `0x00` | `(**(code **)*param_1)(param_1)` | `FUN_0040d590` | Constructor / VTable Init |
| `0x04` | `(**(code **)(*param_1 + 4))(param_1)` | `FUN_004096a0` | Render / Update Frame Dispatch |
| `0x08` | `(**(code **)(*param_1 + 8))(param_1)` | `FUN_00404170` | Event Listener Dispatch |
