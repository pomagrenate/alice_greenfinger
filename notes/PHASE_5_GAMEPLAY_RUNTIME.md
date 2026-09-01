# ALICE GREENFINGERS - GAMEPLAY SIMULATION RUNTIME SPECIFICATION (STEP 8)

*Generated on 2026-09-01*

## 1. Verified Gameplay Mechanics
- **Tile Grid State:** Managed inside `FUN_004096a0`; tile attributes store moisture (watered/dry), soil type, and growth phase index.
- **Plant Growth Timing:** Synchronized to 60 Hz frame counter `DAT_004a7f54`; crop growth advances through sprite frames defined in `Graphics/Sprites.gfx`.
- **Currency & Economy:** Stored in global `DAT_004a86a4`; sales add revenue, seed purchases subtract cost.
- **Customer Order State:** Active market purchase requests evaluated in State 5 (`STATE_SHOP_MARKET`).

## 2. Non-Hallucination Boundaries
- **Plant Hybridization Genetics:** **[NOT-ESTABLISHED]** (No stochastic genetic recombination logic in binary).
- **Customer AI Decision Trees:** **[NOT-ESTABLISHED]** (Orders operate on static item request arrays).
- **Economy Balancing Inflation:** **[NOT-ESTABLISHED]** (Fixed lookup prices per crop item).
