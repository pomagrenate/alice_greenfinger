# ALICE GREENFINGERS - RUNTIME BEHAVIOR MATRIX (STEP 13)

*Generated on 2026-09-01 13:32:33*

| User Action / Trigger | Observed Subsystem Function | Indirect Call Site | Target Function | Subsystem Affected |
| --- | --- | --- | --- | --- |
| Launch Executable | EntryPoint (`0x004165c1`) | `0x00401610` | `FUN_0040d590` | Environment Setup |
| Frame Tick | `FUN_004096a0` | `0x004097f0` | `VTABLE_SLOT_0x04` | World Layer Render |
| UI Control Click | `FUN_00404170` | `0x00404210` | `VTABLE_SLOT_0x08` | Dialog Event Handler |
