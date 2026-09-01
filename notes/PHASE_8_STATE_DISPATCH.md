# ALICE GREENFINGERS - STATE TRANSITION DISPATCH (STEP 11)

*Generated on 2026-09-01 17:57:25*

## 1. VERIFIED STATE MACHINE TRANSITION JUMP SITES (Cluster F)

| Transition | Source State | Target State | Trigger Condition | Status |
| :---: | :--- | :--- | :--- | :---: |
| `0 -> 1` | `STATE_STARTUP` | `STATE_MAIN_MENU` | `Boot completion` | **[VERIFIED (E1/E3)]** |
| `1 -> 2` | `STATE_MAIN_MENU` | `STATE_NAME_DIALOG` | `New Profile click` | **[VERIFIED (E1/E3)]** |
| `1 -> 3` | `STATE_MAIN_MENU` | `STATE_GAMEPLAY` | `Opcode 1001 Start` | **[VERIFIED (E1/E3)]** |
| `3 -> 4` | `STATE_GAMEPLAY` | `STATE_PAUSE_OPTIONS` | `Opcode 1002 Pause` | **[VERIFIED (E1/E3)]** |
| `4 -> 3` | `STATE_PAUSE_OPTIONS` | `STATE_GAMEPLAY` | `Opcode 1003 Resume` | **[VERIFIED (E1/E3)]** |
| `3 -> 5` | `STATE_GAMEPLAY` | `STATE_SHOP_MARKET` | `Opcode 1004 Market` | **[VERIFIED (E1/E3)]** |
| `5 -> 3` | `STATE_SHOP_MARKET` | `STATE_GAMEPLAY` | `Return button` | **[VERIFIED (E1/E3)]** |
