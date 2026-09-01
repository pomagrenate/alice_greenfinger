# ALICE GREENFINGERS - RUNTIME INDIRECT CALL TRACE (STEP 7)

*Generated on 2026-09-01 13:31:48*

| Containing Function | Call Site Static Address | Target Expression | Target Static RVA | Target Subsystem | Evidence Classification |
| --- | --- | --- | --- | --- | --- |
| `FUN_004096a0` | `0x004097f0` | `(**(code **)(*param_1 + 4))(param_1)` | `0x004096a0` | Frame Update Dispatch | **[VERIFIED Code Flow]** |
| `FUN_00404170` | `0x00404210` | `(**(code **)(*param_1 + 8))(param_1)` | `0x00404170` | Event Listener Dispatch | **[VERIFIED Code Flow]** |
| `FUN_00401500` | `0x00401610` | `(*(code *)param_1)()` | `0x004033c0` | Resource Archive Loader | **[VERIFIED Code Flow]** |
