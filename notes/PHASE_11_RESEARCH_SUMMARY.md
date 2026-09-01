# ALICE GREENFINGERS - PHASE 11 RESEARCH SUMMARY (STEP 18)

*Generated on 2026-09-01*

## 1. Executive Summary of Unresolved Boundary Investigations
During Phase 11, rigorous static disassembly, control flow analysis, PE import inspection, and controlled experiments (`EXP11-001` through `EXP11-005`) were conducted on the five primary unresolved boundaries.

### A. Reachability of 124 Isolated Indirect Calls
- **Result:** **100% Isolated in Non-Blocking Secondary Paths**.
- **Evidence:** Analysis of all 124 call sites confirms they reside in secondary modal popups, error handling routines, and optional unlock branches. Zero calls lie on the core campaign progression pathway.

### B. Customer AI Priority Queue Investigation
- **Result:** **`PRIORITY_QUEUE_NOT_ESTABLISHED`**.
- **Evidence:** Disassembly of `STATE_SHOP_MARKET` reveals a fixed array of 4 customer stall structures polled sequentially. No heap or priority sorting algorithms exist in the binary.

### C. Plant Genetics & Hybridization Investigation
- **Result:** **`PLANT_GENETICS_NOT_ESTABLISHED`**.
- **Evidence:** Crop species (Carrot, Tomato, Cabbage, Flower, Corn, Melon) are discrete catalog entries in `Graphics/Sprites.gfx` with table-driven 5-stage timers. No Mendelian trait blending or allele inheritance code exists.

### D. Save File Cryptography Investigation
- **Result:** **`SAVE_ENCRYPTION_NOT_ESTABLISHED`**.
- **Evidence:** Save routine `FUN_004037a0` and load routine `FUN_00403910` perform unencrypted direct binary stream serialization with an `AGSV` magic header. No cipher transformations or key scheduling exist.

### E. Scripted Story Ending Cutscene Investigation
- **Result:** **`ENDGAME_CINEMATIC_NOT_ESTABLISHED`**.
- **Evidence:** PE imports contain no video codecs (Bink, AVI, MPEG). The game is structured as an endless casual time-management simulation advancing daily quotas with audio-visual trophy dialogs.
