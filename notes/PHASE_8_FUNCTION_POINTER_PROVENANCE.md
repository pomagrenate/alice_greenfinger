# ALICE GREENFINGERS - FUNCTION POINTER PROVENANCE (STEP 3)

*Generated on 2026-09-01 17:56:55*

## 1. DISPATCH MECHANISM PROVENANCE CHAINS

| Cluster | Provenance Mechanism | Origin Source | Target Resolution Chain | Evidence |
| --- | --- | --- | --- | :---: |
| **Cluster E** | PE Import Address Table (IAT) | `Kernel32 / User32 / GDI32 / WinMM Import Section` | PE Header Import Descriptor -> IAT Pointer -> Direct Platform API Call | **[VERIFIED (E1/E2)]** |
| **Cluster B** | ADLIBREGISTER / Script Callback Table | `Static string token registry matched in FUN_00404170` | Opcode Integer / String Token -> Table Lookup -> Target Handler RVA | **[VERIFIED (E1/E3)]** |
| **Cluster F** | State Transition Jump Table | `DAT_004974f4 state register index (0..5)` | State Index -> Switch / Jump Table -> State Entry / Tick Handler | **[VERIFIED (E1/E3)]** |
| **Cluster A** | VTable Pointer Initialization | `Object Constructor writing VTABLE_00497000 address to [ECX+0x00]` | Object Construction -> vptr assigned -> Indirect Call [vptr + slot] | **[VERIFIED (E1/E2)]** |
| **Cluster D** | Resource Archive Decoders | `FUN_004033c0 LBTC magic header parser` | File Header -> Buffer Offset Table -> Sprite Sub-Allocation Decoder | **[VERIFIED (E1/E4)]** |
