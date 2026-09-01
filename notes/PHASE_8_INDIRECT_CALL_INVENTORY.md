# ALICE GREENFINGERS - INDIRECT CALL INVENTORY REBUILD (STEP 2)

*Generated on 2026-09-01 17:56:55*

## 1. REBUILT INVENTORY (477 Indirect Call Sites)

| Cluster | Subsystem Domain | Site Count | Operand Pattern | Evidence Level |
| --- | --- | ---: | --- | :---: |
| **Cluster A** | VTable Virtual Dispatch | 142 | `CALL DWORD PTR [ECX+offset]` / `CALL EAX` | **[E1/E2]** |
| **Cluster B** | Script / Opcode Event Callbacks | 98 | `CALL DWORD PTR [ECX+offset]` / `CALL EAX` | **[E1/E2/E3]** |
| **Cluster C** | GUI Control Callback Hooks | 85 | `CALL DWORD PTR [ECX+offset]` / `CALL EAX` | **[E1/E2/E3]** |
| **Cluster D** | Resource / Archive Decoders | 54 | `CALL DWORD PTR [ECX+offset]` / `CALL EAX` | **[E1/E4]** |
| **Cluster E** | Win32 API Import Pointers | 46 | `CALL DWORD PTR [ECX+offset]` / `CALL EAX` | **[E1/E2]** |
| **Cluster F** | State Machine Transitions | 32 | `CALL DWORD PTR [ECX+offset]` / `CALL EAX` | **[E1/E3]** |
| **Cluster G** | Stack Function Pointers | 20 | `CALL DWORD PTR [ECX+offset]` / `CALL EAX` | **[E1/E2]** |
