# ALICE GREENFINGERS - INDIRECT CALL REASSESSMENT (STEP 12)

*Generated on 2026-09-01*

## 1. Triage Breakdown for 425 Unresolved Call Sites
| Cluster | Source Mechanism | Call Count | Resolution Strategy | Status |
| :--- | :--- | ---: | :--- | :--- |
| **Cluster A** | VTable Virtual Dispatches (`vptr + offset`) | 142 | Map VTable Slot Arrays | **[ISOLATED]** |
| **Cluster B** | Script & Opcode Event Callbacks | 98 | Trace Opcode Registration | **[ISOLATED]** |
| **Cluster C** | GUI Control Callback Hooks | 85 | UI Control ID Lookup | **[ISOLATED]** |
| **Cluster D** | Resource / Archive Decoders | 54 | Stream Parser Trace | **[ISOLATED]** |
| **Cluster E** | Win32 API Import Pointers | 46 | Dynamic Import Binding | **[ISOLATED]** |
| **Cluster F** | State Machine Transition Dispatchers | 32 | State Machine Trace | **[ISOLATED]** |
| **Cluster G** | Isolated Stack Function Pointers | 20 | Assembly Slicing | **[ISOLATED]** |
| **Total** | | **425** | | |
