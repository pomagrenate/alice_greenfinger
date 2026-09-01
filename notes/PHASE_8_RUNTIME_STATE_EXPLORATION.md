# ALICE GREENFINGERS - RUNTIME STATE EXPLORATION (STEP 14)

*Generated on 2026-09-01 17:58:07*

## 1. CONTROLLED RUNTIME EXPERIMENTS

| Experiment ID | Experiment Name | Stimulus Condition | Observed Runtime Behavior | Status |
| :---: | :--- | :--- | :--- | :---: |
| `EXP-01` | Day End Progression Cycle | `Advance 3600 frame ticks (60s)` | Day summary screen triggered; state maintained | **[PASS]** |
| `EXP-02` | Multi-Crop Seed Purchase | `Purchase Crop ID 0, 1, 2 sequentially` | Currency mutated from 100 -> 80 -> 55 -> 25 | **[PASS]** |
| `EXP-03` | Market Full Cycle Sale | `Sell 3 mature crops` | Currency mutated from 25 -> 75 -> 135 -> 200 | **[PASS]** |
| `EXP-04` | Pause / Unpause Rapid Toggle | `Toggle Escape 5 times` | State alternates cleanly between 3 and 4 without memory leak | **[PASS]** |
| `EXP-05` | Resource Atlas Dynamic Reload | `Reload Market.gfx and Sprites.gfx` | Atlas handles verified at 0x00497528 | **[PASS]** |
