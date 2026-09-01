# ALICE GREENFINGERS - GAME STATE RECONSTRUCTION (STEP 6)

*Generated on 2026-09-01*

## 1. Proven State Machine Model
| State ID | Enum Identifier | Trigger Function | Mutated Global | Confidence |
| :---: | :--- | :--- | :--- | :--- |
| `0` | `STATE_STARTUP` | `FUN_0040d590` / `Platform_Initialize` | `DAT_004974f4 = 0` | **[VERIFIED]** |
| `1` | `STATE_MAIN_MENU` | `FUN_00404170` (Opcode 1003) | `DAT_004974f4 = 1` | **[VERIFIED]** |
| `2` | `STATE_NAME_DIALOG` | `FUN_00404170` (Dialog Enter) | `DAT_004974f4 = 2` | **[VERIFIED]** |
| `3` | `STATE_GAMEPLAY` | `FUN_00404170` (Opcode 1001) | `DAT_004974f4 = 3`, `DAT_004a7f54 = 1` | **[VERIFIED]** |
| `4` | `STATE_PAUSE_OPTIONS` | `FUN_00404170` (Opcode 1002) | `DAT_004974f4 = 4` | **[VERIFIED]** |
| `5` | `STATE_SHOP_MARKET` | `FUN_00404170` (Market Click) | `DAT_004974f4 = 5` | **[RUNTIME-OBSERVED]** |

## 2. Transition Rules & Verification
- `STATE_STARTUP` (0) → `STATE_MAIN_MENU` (1): Automatic on successful engine context init.
- `STATE_MAIN_MENU` (1) → `STATE_GAMEPLAY` (3): Triggered when player starts/continues farm.
- `STATE_GAMEPLAY` (3) ↔ `STATE_PAUSE_OPTIONS` (4): Triggered on Esc / Options button click.
- `STATE_GAMEPLAY` (3) ↔ `STATE_SHOP_MARKET` (5): Triggered on town market button click.
