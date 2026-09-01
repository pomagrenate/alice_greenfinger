# ALICE GREENFINGERS - RUNTIME ADDRESS MAPPING (STEP 3)

*Generated on 2026-09-01 13:29:44*

## ASLR & IMAGE BASE SPECIFICATIONS
- **Executable Name:** `AliceGreenfingers_unpacked.exe`
- **Static Preferred Image Base:** `0x00400000`
- **ASLR (Address Space Layout Randomization) Status:** **DISABLED** (PE characteristics `0x0102` flag `IMAGE_FILE_RELOCS_STRIPPED`).
- **Address Translation Formula:** `Runtime Address = Static RVA Address` (Direct 1:1 Parity).

## KEY FUNCTION ADDRESS MAPPING TABLE

| Function Identifier | Ghidra Static Address | Target Module Base | Calculated Runtime Address | Mapping Confidence |
| --- | --- | --- | --- | --- |
| `EntryPoint` | `0x004165c1` | `0x00400000` | `0x004165c1` | **[VERIFIED Direct 1:1]** |
| `FUN_00404170` | `0x00404170` | `0x00400000` | `0x00404170` | **[VERIFIED Direct 1:1]** |
| `FUN_004096a0` | `0x004096a0` | `0x00400000` | `0x004096a0` | **[VERIFIED Direct 1:1]** |
| `FUN_004033c0` | `0x004033c0` | `0x00400000` | `0x004033c0` | **[VERIFIED Direct 1:1]** |
