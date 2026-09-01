# ALICE GREENFINGERS - CAMPAIGN STATE MACHINE (STEP 4)

*Generated on 2026-09-01*

## 1. Verified Campaign State Transitions
| State ID | Enum Name | Role & Screen Presentation | Allowed Next States |
| :---: | :--- | :--- | :--- |
| `0` | `STATE_STARTUP` | Boot, Engine Initialization & LBTC Preload | `STATE_MAIN_MENU` (1) |
| `1` | `STATE_MAIN_MENU` | Title Screen, Start Button, Player Profile | `STATE_NAME_DIALOG` (2), `STATE_GAMEPLAY` (3) |
| `2` | `STATE_NAME_DIALOG` | Profile Name Entry Modal | `STATE_GAMEPLAY` (3) |
| `3` | `STATE_GAMEPLAY` | Main Farm Grid Simulation & Crop Growth | `STATE_PAUSE_OPTIONS` (4), `STATE_SHOP_MARKET` (5) |
| `4` | `STATE_PAUSE_OPTIONS` | Pause Overlay & Volume Settings | `STATE_GAMEPLAY` (3) |
| `5` | `STATE_SHOP_MARKET` | Town Market Stalls, Seed Purchasing, Selling | `STATE_GAMEPLAY` (3) |
