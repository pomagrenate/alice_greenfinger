# ALICE GREENFINGERS - GAMEPLAY SIMULATION BEHAVIOR (STEP 8)

*Generated on 2026-09-01*

## 1. Verified Gameplay Mechanics
- **Farm Grid Simulation:** Managed during `STATE_GAMEPLAY` inside `FUN_004096a0`.
- **Plant Growth Timers:** Synchronized to frame counter `DAT_004a7f54`.
- **Currency & Money State:** Stored in global `DAT_004a86a4` / `DAT_004a95f0`.
- **Watering & Soil Moisture:** Tile attribute flags updated via grid click handlers in `FUN_00404170`.
- **Harvest & Market Selling:** Triggers currency increment and inventory decrease.
