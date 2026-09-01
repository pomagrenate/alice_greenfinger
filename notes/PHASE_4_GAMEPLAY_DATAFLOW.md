# ALICE GREENFINGERS - GAMEPLAY DATAFLOW SPECIFICATION (STEP 5)

*Generated on 2026-09-01*

## 1. Global Variable Dataflow Pipelines
| Address | Functional Role | Access Type | Readers | Writers | Confidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `DAT_004974f4` | Active Game State (0..5) | Read/Write | `FUN_00404170`, `FUN_004096a0` | `FUN_0040d590`, `FUN_00404170` | **[VERIFIED]** |
| `DAT_004a7f54` | Frame Tick Counter | Read/Write | `FUN_004096a0` | `FUN_004096a0` | **[VERIFIED]** |
| `DAT_00497528` | Sprite Atlas Handle Pointer | Read/Write | `FUN_004096a0` | `FUN_004033c0` | **[VERIFIED]** |
| `DAT_004a86a4` | Gameplay / Currency State | Read/Write | `FUN_00404170`, `FUN_004096a0` | `FUN_00404170` | **[HIGH-CONFIDENCE]** |
