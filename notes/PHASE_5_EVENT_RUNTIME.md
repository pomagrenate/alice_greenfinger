# ALICE GREENFINGERS - INPUT & EVENT RUNTIME SPECIFICATION (STEP 7)

*Generated on 2026-09-01*

## 1. Event Propagation Architecture
```
+------------------------+
|  Platform Raw Input    | (Win32 Messages: WM_LBUTTONDOWN, WM_KEYDOWN, WM_MOUSEMOVE)
+-----------+------------+
            |
            v
+------------------------+
| Reconstructed Event    | (Normalized InputEvent: MouseClick, KeyPress, CommandOpcode)
+-----------+------------+
            |
            v
+------------------------+
| Event_DispatchOpcode   | (FUN_00404170: Opcode Matching & VTable Slot +0x08 Hook)
+-----------+------------+
            |
            v
+------------------------+
| State / Global Mutation| (DAT_004974f4 State, DAT_004a86a4 Currency, Tile Simulation)
+------------------------+
```

## 2. Verified Opcode Tokens
- `"ADLIBREGISTER"`: Registers timer ticks / periodic script callbacks.
- `"GUICTRLSETDATA"`: Updates text / numerical values in GUI controls.
- `"GUICTRLSETSTATE"`: Enables/disables or hides/shows UI control handles.
- Opcode `1001`: Sets game state to `STATE_GAMEPLAY` (3).
- Opcode `1002`: Sets game state to `STATE_PAUSE_OPTIONS` (4).
- Opcode `1003`: Sets game state to `STATE_MAIN_MENU` (1).
