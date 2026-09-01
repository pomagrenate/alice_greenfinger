# ALICE GREENFINGERS - ECONOMY & INVENTORY RECONSTRUCTION (STEP 8)

*Completed on 2026-09-01*

## 1. Verified Arithmetic & Mutations
- **Currency Mutation:**
  - Selling crops/flowers triggers an addition to global register `DAT_004a86a4`:
    `DAT_004a86a4 = DAT_004a86a4 + item_price;`
  - Purchasing seeds/tools subtracts from `DAT_004a86a4`:
    `DAT_004a86a4 = DAT_004a86a4 - cost;`
- **Inventory Bounds:**
  - Basket/inventory capacity is checked before harvest events in `FUN_00404170`.
