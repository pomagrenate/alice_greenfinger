# FUN_004033c0 DEEP BEHAVIORAL FORENSIC AUDIT (STEP 4)

*Generated on 2026-09-01*

## 1. Binary Identification & Metadata
- **Function RVA:** `0x004033c0`
- **Subsystem:** `SUBSYS_POP_PARSER` (PopCap GFX Container / LBTC Archive Parser)
- **ABI:** `__cdecl`
- **Classification:** **[VERIFIED]**

## 2. Behavioral Role
- Parses container files located in `Graphics/*.gfx` and `TileSets/`.
- Verifies archive magic identifier `"LBTC"` (PopCap container header).
- Reads table of contents (TOC), sprite sub-image bounds, and pixel formats.
- Allocates memory sprite surfaces and writes handle pointer into `DAT_00497528`.
