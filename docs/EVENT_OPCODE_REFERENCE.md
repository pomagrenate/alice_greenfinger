# Alice Greenfingers - Reconstructed Event Opcode Reference

| Opcode ID | Constant Identifier | Trigger Source | Dispatched Result | Status |
| :---: | :--- | :--- | :--- | :---: |
| `1001` | `OP_START_GAMEPLAY` | Main Menu Start Button | Transitions to `STATE_GAMEPLAY` (3) | **[VERIFIED]** |
| `1002` | `OP_PAUSE_OPTIONS` | Escape Key / Pause Button | Transitions to `STATE_PAUSE_OPTIONS` (4) | **[VERIFIED]** |
| `1003` | `OP_RESUME_GAMEPLAY` | Resume / Return Button | Returns to `STATE_GAMEPLAY` (3) | **[VERIFIED]** |
| `1004` | `OP_OPEN_MARKET` | Market HUD Button | Transitions to `STATE_SHOP_MARKET` (5) | **[VERIFIED]** |
| `1005` | `OP_BUY_SEEDS` | Seed Stall Click | Mutates `DAT_004a86a4 -= 20` | **[VERIFIED]** |
| `1006` | `OP_SELL_HARVEST` | Crop Basket Sell Click | Mutates `DAT_004a86a4 += 50` | **[VERIFIED]** |
| `1007` | `OP_EXIT_APP` | Window Close / Quit Button | Requests clean application shutdown | **[VERIFIED]** |
