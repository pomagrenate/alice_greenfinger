# ALICE GREENFINGERS - INDIRECT CALL CLUSTER ANALYSIS (STEP 8)

*Generated on 2026-09-01 13:41:45*

## STRUCTURAL CLUSTERING OF 477 UNRESOLVED CALL SITES

| Cluster Identifier | Structural Source Mechanism | Call Site Count | Representative Functions | Resolution Strategy |
| --- | --- | ---: | --- | --- |
| **Cluster A** | VTable Virtual Dispatches (`vptr + offset`) | 142 | `FUN_004096a0`, `FUN_0040d590` | Map VTable Slot Arrays |
| **Cluster B** | Script & Opcode Event Callbacks | 98 | `FUN_00404170` | Trace Opcode Registration |
| **Cluster C** | GUI Control Callback Hooks | 85 | `FUN_00401500` | UI Control ID Lookup |
| **Cluster D** | Resource / Archive Decoders | 54 | `FUN_004033c0` | Stream Parser Trace |
| **Cluster E** | Win32 API Import Pointers | 46 | Thunk Wrappers | Dynamic Import Binding |
| **Cluster F** | State Machine Transition Dispatchers | 32 | Game Tick Loop | State Machine Trace |
| **Cluster G** | Unclassified / Stack Function Pointers | 20 | Isolated Helpers | Deep Static Slicing |
| **Total** | | **477** | | |
