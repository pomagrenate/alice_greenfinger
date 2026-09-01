# ALICE GREENFINGERS - VTABLE DISPATCH RESOLUTION MATRIX (STEP 9)

*Generated on 2026-09-01 13:24:48*

## OBJECT MEMORY & VTABLE LAYOUT GRAPH

```
Object Instance Pointer (param_1 / ECX)
    |
    +--> Offset +0x00: VTable Pointer (vptr)
              |
              +--> Slot +0x00: (*vptr[0])() -> Object Constructor / Init (FUN_0040d590) [HIGH-CONFIDENCE]
              +--> Slot +0x04: (*vptr[1])() -> Frame Update Dispatcher (FUN_004096a0) [VERIFIED]
              +--> Slot +0x08: (*vptr[2])() -> Event Listener Callback (FUN_00404170) [VERIFIED]
              +--> Slot +0x0C: (*vptr[3])() -> Resource Destructor / Release [HIGH-CONFIDENCE]
```

## CONFIRMED VTABLE DISPATCH SITES

| Address RVA | Target Expression | VTable Slot Offset | Referencing Function | Target Subsystem | Evidence Classification |
| --- | --- | --- | --- | --- | --- |
| `0x004096a0` | `(**(code **)*param_1)(param_1)` | `0x00` | `FUN_004096a0` | Init Dispatch | **[VERIFIED]** |
| `0x004097f0` | `(**(code **)(*param_1 + 4))(param_1)` | `0x04` | `FUN_004096a0` | Frame Update | **[VERIFIED]** |
| `0x00404210` | `(**(code **)(*param_1 + 8))(param_1)` | `0x08` | `FUN_00404170` | Event Dispatch | **[VERIFIED]** |
