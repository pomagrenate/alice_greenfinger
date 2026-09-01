# ALICE GREENFINGERS - GUI SMOKE TESTS SPECIFICATION (STEP 15)

*Generated on 2026-09-01 17:48:21*

## INTERACTIVE GUI SMOKE TEST SCENARIOS

| Test ID | Scenario Description | Stimulus Input | Expected State | Validation Result |
| --- | --- | --- | :---: | :---: |
| `GUI-01` | Application Window & Context Initialization | `Window_Create(800x600)` | `0` | **[PASS]** |
| `GUI-02` | Main Menu Mouse Move & Hover | `Input_PushEvent(MOUSE_MOVE 400, 300)` | `1` | **[PASS]** |
| `GUI-03` | Name Dialog Modal Interaction | `Input_PushEvent(MOUSE_DOWN Dialog_Bounds)` | `2` | **[PASS]** |
| `GUI-04` | Enter Gameplay Transition | `Input_PushEvent(MOUSE_DOWN Start_Button)` | `3` | **[PASS]** |
| `GUI-05` | Gameplay Grid Mouse Click | `Input_PushEvent(MOUSE_DOWN Tile_Plot[2][3])` | `3` | **[PASS]** |
| `GUI-06` | Pause / Options Trigger | `Input_PushEvent(KEY_DOWN VK_ESCAPE)` | `4` | **[PASS]** |
| `GUI-07` | Shop / Market Trigger | `Input_PushEvent(MOUSE_DOWN Market_Button)` | `5` | **[PASS]** |
| `GUI-08` | Return From Market / Pause to Farm | `Input_PushEvent(MOUSE_DOWN Return_Button)` | `3` | **[PASS]** |
| `GUI-09` | Window Close Request Handling | `Window_RequestClose()` | `3` | **[PASS]** |
| `GUI-10` | Full Application Lifecycle Restart | `Platform_Initialize()` | `0` | **[PASS]** |
