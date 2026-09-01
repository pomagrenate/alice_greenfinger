# ALICE GREENFINGERS - SCRIPT CALLBACK REGISTRY (STEP 6)

*Generated on 2026-09-01 17:57:09*

## 1. RECONSTRUCTED OPCODE HANDLER REGISTRY (Cluster B)

| Opcode ID | Opcode Identifier | Handler RVA | Effect / State Mutation | Status | Evidence |
| :---: | :--- | :---: | :--- | :---: | :---: |
| `1001` | `OP_START_GAMEPLAY` | `0x00404170` | `STATE_GAMEPLAY (3)` | **VERIFIED** | **[E1/E3]** |
| `1002` | `OP_PAUSE_OPTIONS` | `0x00404170` | `STATE_PAUSE_OPTIONS (4)` | **VERIFIED** | **[E1/E3]** |
| `1003` | `OP_RESUME_GAMEPLAY` | `0x00404170` | `STATE_GAMEPLAY (3)` | **VERIFIED** | **[E1/E3]** |
| `1004` | `OP_OPEN_MARKET` | `0x00404170` | `STATE_SHOP_MARKET (5)` | **VERIFIED** | **[E1/E3]** |
| `1005` | `OP_BUY_SEEDS` | `0x00404170` | `DAT_004a86a4 -= cost` | **VERIFIED** | **[E1/E3]** |
| `1006` | `OP_SELL_HARVEST` | `0x00404170` | `DAT_004a86a4 += revenue` | **VERIFIED** | **[E1/E3]** |
| `1007` | `OP_EXIT_APPLICATION` | `0x0040d590` | `SHUTDOWN (0)` | **VERIFIED** | **[E1/E3]** |
