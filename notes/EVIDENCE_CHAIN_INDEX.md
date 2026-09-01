# ALICE GREENFINGERS - EVIDENCE CHAIN INDEX (STEP 13)

*Updated on 2026-09-01 13:37:17*

## FORENSIC EVIDENCE CHAIN

```
BINARY: AliceGreenfingers_unpacked.exe (732 KB PE)
  ↓
STATIC FUNCTION: FUN_00404170 (RVA 0x00404170, 2,408 C Lines)
  ↓
CALL SITE: 0x00404210
  ↓
DATA FLOW: (**(code **)(*param_1 + 8))(param_1)
  ↓
RUNTIME ADDRESS: 0x00404170 (ASLR Disabled)
  ↓
ACTUAL TARGET: UI Event Handler Callback (VTable Slot +0x08)
  ↓
OBSERVED STATE: Start Dialog Open Event
  ↓
BEHAVIOR: Name Input Dialog Trigger [VERIFIED]
```
