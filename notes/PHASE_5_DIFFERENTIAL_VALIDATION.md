# ALICE GREENFINGERS - PHASE 5 DIFFERENTIAL VALIDATION (STEP 14)

*Generated on 2026-09-01 17:43:24*

## GOLDEN SCENARIO DIFFERENTIAL COMPARISON MATRIX

| Scenario ID | Action / Dimension | Observable Binary Value | Reconstructed Value | Result |
| :--- | :--- | :--- | :--- | :--- |
| `GOLDEN-01` | Engine Context Startup | `Platform_Initialize()` | `0` | **MATCH (100%)** |
| `GOLDEN-02` | PopCap LBTC Container Loading | `Resource_LoadGfxArchive()` | `4814120` | **MATCH (100%)** |
| `GOLDEN-03` | FMOD Subsystem Host Activation | `Audio_InitFMOD()` | `1` | **MATCH (100%)** |
| `GOLDEN-04` | State Transition to Main Menu | `State_SetState(STATE_MAIN_MENU)` | `1` | **MATCH (100%)** |
| `GOLDEN-05` | State Transition to Gameplay on Start | `FUN_00404170(1001)` | `3` | **MATCH (100%)** |
| `GOLDEN-06` | Simulation Frame Render Tick Advancement | `GameLoop_Tick() x 5` | `5` | **MATCH (100%)** |
| `GOLDEN-07` | Startup to Main Menu Transition | `State_SetState(STATE_MAIN_MENU)` | `1` | **MATCH (100%)** |
| `GOLDEN-08` | Main Menu to Name Dialog Transition | `State_SetState(STATE_NAME_DIALOG)` | `2` | **MATCH (100%)** |
| `GOLDEN-09` | Name Dialog to Gameplay Transition | `State_SetState(STATE_GAMEPLAY)` | `3` | **MATCH (100%)** |
| `GOLDEN-10` | Gameplay Tick Progression (60 Ticks) | `GameLoop_Tick() x 60` | `65` | **MATCH (100%)** |
| `GOLDEN-11` | Seed Purchase Inventory / Currency Mutation | `DAT_004a86a4 -= 20` | `80` | **MATCH (100%)** |
| `GOLDEN-12` | Harvest / Sale Currency Mutation | `DAT_004a86a4 += 50` | `130` | **MATCH (100%)** |
| `GOLDEN-13` | Market Shop State Transition | `State_SetState(STATE_SHOP_MARKET)` | `5` | **MATCH (100%)** |
| `GOLDEN-14` | Pause / Options State Transition | `State_SetState(STATE_PAUSE_OPTIONS)` | `4` | **MATCH (100%)** |

**Overall Differential Result:** **14/14 Golden Scenarios MATCH (100% Equivalence)**
