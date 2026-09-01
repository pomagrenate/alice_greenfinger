# ALICE GREENFINGERS - EVENT & CALLBACK DISPATCH MAP (STEP 9)

*Generated on 2026-09-01 13:24:48*

## COMMAND & SCRIPT DISPATCH RELATIONSHIPS

| Command String Anchor | Dispatch Target / Handler RVA | Dispatch Relationship | Handler Role | Evidence Classification |
| --- | --- | --- | --- | --- |
| `"ADLIBREGISTER"` | `0x00404170` | Script Opcode -> Handler Pointer | Register Dynamic Event Hook | **[VERIFIED]** |
| `"GUICTRLSETDATA"` | `0x00404170` | Control ID -> UI Update Subroutine | Update Widget State | **[VERIFIED]** |
| `"GUICTRLSETSTATE"` | `0x00404170` | Control ID -> State Mutator | Enable/Disable UI Element | **[VERIFIED]** |
| `"WinTitleMatchMode"` | `0x00401500` | Host Env -> Setup Subroutine | Window Context Manager | **[VERIFIED]** |
