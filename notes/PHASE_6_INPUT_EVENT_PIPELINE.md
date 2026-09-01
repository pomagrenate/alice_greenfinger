# ALICE GREENFINGERS - INPUT EVENT PIPELINE INTEGRATION (STEP 6)

*Generated on 2026-09-01*

## 1. Input-to-Dispatcher Routing
```
+--------------------------+
| OS Window Message        | (WM_LBUTTONDOWN, WM_KEYDOWN)
+------------+-------------+
             |
             v
+--------------------------+
| Input_PushEvent()        | (Normalized InputEvent queued)
+------------+-------------+
             |
             v
+--------------------------+
| Event_ProcessInput()     | (Evaluates active game state)
+------------+-------------+
             |
             v
+--------------------------+
| FUN_00404170 Dispatcher  | (Opcode matching, VTable slot +0x08 callback)
+------------+-------------+
             |
             v
+--------------------------+
| State / Global Mutation  | (State_SetState, DAT_004974f4, DAT_004a86a4)
+--------------------------+
```

## 2. Interactive Click Handlers per State
- **State 1 (MAIN_MENU):** Left click on "Start" bounds triggers Opcode `1001` (`STATE_GAMEPLAY`).
- **State 2 (NAME_DIALOG):** Left click on "OK" bounds triggers transition to `STATE_GAMEPLAY`.
- **State 3 (GAMEPLAY):** Left click on farm grid advances tile interaction; click on "Pause" triggers `STATE_PAUSE_OPTIONS` (Opcode `1002`); click on "Market" triggers `STATE_SHOP_MARKET`.
- **State 4 (PAUSE_OPTIONS):** Left click on "Resume" returns to `STATE_GAMEPLAY`.
- **State 5 (SHOP_MARKET):** Left click on "Return" returns to `STATE_GAMEPLAY`.
