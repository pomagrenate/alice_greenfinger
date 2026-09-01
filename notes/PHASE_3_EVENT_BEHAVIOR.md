# ALICE GREENFINGERS - EVENT SYSTEM BEHAVIOR (STEP 7)

*Generated on 2026-09-01*

## 1. Event Propagation Pipeline
1. **Win32 Message Hook (`WinMain`):** Intercepts mouse clicks, keyboard presses, window focus.
2. **Opcode Dispatcher (`FUN_00404170`):** Compares event tokens (`ADLIBREGISTER`, `GUICTRLSETDATA`, `GUICTRLSETSTATE`).
3. **VTable Slot `+0x08` Dispatch:** Dispatches to registered UI element listener.
4. **State / Global Mutation:** Mutates `DAT_004974f4` (State) and `DAT_004a86a4` (UI flag).
