# ALICE GREENFINGERS - PHASE 11 OBJECT MODEL & VTABLE REPORT (STEP 3)

*Generated on 2026-09-01 18:47:14*

## 1. RECOVERED OBJECT MEMORY LAYOUTS

### EngineContext (128 Bytes)
- **VTable Address:** `0x00497000` (4 Slots: Init `0x00401500`, Tick `0x004096a0`, Event `0x00404170`, Shutdown `0x0040d590`)
- **Status:** **[VERIFIED (E1/E3)]**

### UIWidgetContainer (64 Bytes)
- **VTable Address:** `0x00497100` (3 Slots: MouseEnter, MouseLeave, Click)
- **Status:** **[VERIFIED (E1/E3)]**

## 2. INHERITANCE HIERARCHY FINDING
- Deep polymorphic inheritance hierarchies: **[NOT ESTABLISHED]** (PopCap game architecture uses flat structs with table dispatch).
