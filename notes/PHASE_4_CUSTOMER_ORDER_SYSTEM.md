# ALICE GREENFINGERS - CUSTOMER & ORDER QUEUE ANALYSIS (STEP 7)

*Completed on 2026-09-01*

## 1. Forensic Investigation Findings
- **Observed Order Mechanics:**
  - Customer purchase requests are triggered during `STATE_SHOP_MARKET` (State 5) and `STATE_GAMEPLAY` (State 3) via UI opcode events in `FUN_00404170`.
  - Market item assets are loaded from `Graphics/Market.gfx` (199 sub-sprites).
- **Complex Queue Data Structure Status:**
  - **STANDALONE QUEUE CLASS:** **[NOT ESTABLISHED]**
  - The binary does not utilize an explicit linked-list priority queue for customers. Instead, active customer requests are managed as fixed-size array state registers updated per game tick.
