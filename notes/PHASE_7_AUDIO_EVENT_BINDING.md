# ALICE GREENFINGERS - AUDIO EVENT BINDING (STEP 10)

*Generated on 2026-09-01 17:53:37*

## 1. GAMEPLAY & GUI AUDIO EVENT MAPPINGS

| Event Name | Bound Audio Track | Trigger Source | Binding Status | Evidence |
| --- | --- | --- | :---: | :---: |
| GUI Button Click | `AG-Click.ogg` | `Input_PushEvent(MOUSE_DOWN)` | **VERIFIED** | **[E1/E3]** |
| Plant Growth Tick | `AG-Grow.ogg` | `Crop Stage Transition` | **VERIFIED** | **[E1/E3]** |
| Harvest Crop Cash | `AG-CashReceive.ogg` | `DAT_004a86a4 += price` | **VERIFIED** | **[E1/E3]** |
| Main Menu Music | `AGMusic-Menu.oxm` | `STATE_MAIN_MENU (1)` | **VERIFIED** | **[E1/E3]** |
| Gameplay Music | `AGMusic-Ingame01.oxm` | `STATE_GAMEPLAY (3)` | **VERIFIED** | **[E1/E3]** |
| Speculative Ambient Jingle | `None` | `Unproven` | **NOT ESTABLISHED** | **[E1]** |
