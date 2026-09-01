# ALICE GREENFINGERS - RUNTIME STATE EXPLORATION MAP (STEP 3)

*Generated on 2026-09-01 13:35:53*

## EVIDENCE-BASED STATE TRANSITION GRAPH

| State Identifier | Entrance Trigger | Observable UI / Engine Anchor | Status Classification |
| --- | --- | --- | --- |
| `STATE_STARTUP` | Executable Launch | `EntryPoint` (`0x004165c1`) | **[VERIFIED]** |
| `STATE_MAIN_MENU` | Engine Initialization | Title Screen Render Loop (`FUN_004096a0`) | **[VERIFIED]** |
| `STATE_NAME_DIALOG` | Click "New Game" | Dialog Window (`FUN_00404170` anchor) | **[VERIFIED]** |
| `STATE_GAMEPLAY` | Submit Player Name | Grid Render & Tile Update | **[VERIFIED]** |
| `STATE_SHOP_MARKET` | Click Market Icon | Item Catalog Overlay | **[HYPOTHESIS]** |
| `STATE_PAUSE_OPTIONS` | Press Escape Key | Options Menu Overlay | **[VERIFIED]** |
