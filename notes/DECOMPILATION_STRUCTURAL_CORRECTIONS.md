# ALICE GREENFINGERS - DECOMPILATION STRUCTURAL CORRECTIONS (STEP 13)

*Generated on 2026-09-01 13:43:38*

| Function Identifier | Ghidra Decompiler Misinterpretation | Corrected Assembly Interpretation | Evidence Basis |
| --- | --- | --- | --- |
| `FUN_00404170` | `(*code)(param_1)` | `__stdcall` dispatch table jump | Callee stack cleanup `ret 0x08` |
| `FUN_004096a0` | `(*(code *)(*param_1 + 4))()` | `__thiscall` VTable Slot `+0x04` dispatch | `ECX` contains instance pointer |
