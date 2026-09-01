# ALICE GREENFINGERS - GAME STATE MACHINE RUNTIME SPECIFICATION (STEP 6)

*Generated on 2026-09-01 17:41:26*

## 1. EVIDENCE-BACKED STATE TRANSITION MATRIX

| Source State | Trigger Event / Input | Target State | Evidence & Register Mutation | Confidence |
| --- | --- | --- | --- | :---: |
| `STATE_STARTUP (0)` | `Platform_Initialize() / EngineContext Init` | `STATE_STARTUP (0)` | FUN_0040d590 initializes DAT_004974f4 = 0 | **[VERIFIED]** |
| `STATE_STARTUP (0)` | `WinMain_Menu / Load Complete` | `STATE_MAIN_MENU (1)` | FUN_00404170 Opcode 1003 sets DAT_004974f4 = 1 | **[VERIFIED]** |
| `STATE_MAIN_MENU (1)` | `Profile Dialog / New Player Button` | `STATE_NAME_DIALOG (2)` | FUN_00404170 UI Dialog handler sets DAT_004974f4 = 2 | **[VERIFIED]** |
| `STATE_MAIN_MENU (1) / STATE_NAME_DIALOG (2)` | `Start Game Button / Opcode 1001` | `STATE_GAMEPLAY (3)` | FUN_00404170 Opcode 1001 sets DAT_004974f4 = 3, DAT_004a7f54 = 1 | **[VERIFIED]** |
| `STATE_GAMEPLAY (3)` | `Options Button / Esc Key / Opcode 1002` | `STATE_PAUSE_OPTIONS (4)` | FUN_00404170 Opcode 1002 sets DAT_004974f4 = 4 | **[VERIFIED]** |
| `STATE_PAUSE_OPTIONS (4)` | `Resume Game Button / Opcode 1001` | `STATE_GAMEPLAY (3)` | FUN_00404170 Opcode 1001 restores DAT_004974f4 = 3 | **[VERIFIED]** |
| `STATE_GAMEPLAY (3)` | `Market Button Click / Shop Trigger` | `STATE_SHOP_MARKET (5)` | FUN_00404170 Market transition sets DAT_004974f4 = 5 | **[RUNTIME-OBSERVED]** |
| `STATE_SHOP_MARKET (5)` | `Return to Farm Button Click` | `STATE_GAMEPLAY (3)` | FUN_00404170 Return transition sets DAT_004974f4 = 3 | **[RUNTIME-OBSERVED]** |
