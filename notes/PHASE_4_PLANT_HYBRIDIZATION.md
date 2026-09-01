# ALICE GREENFINGERS - FLOWER & PLANT ALGORITHM INVESTIGATION (STEP 6)

*Completed on 2026-09-01*

## 1. Forensic Investigation Findings
A comprehensive symbol, string, and control-flow scan was conducted on `AliceGreenfingers_unpacked.exe` and `ACTUAL_GHIDRA_DECOMPILED_EXE.c`.

- **Observed Plant Mechanics:**
  - The binary simulates plant growth by advancing tile grid frame indices in `FUN_004096a0` synchronized to the frame counter `DAT_004a7f54`.
  - Sprites corresponding to soil, watering, sprouting, blooming, and harvesting are drawn from `Graphics/Sprites.gfx` (622 sub-sprites) and `TileSets/` (48 sub-sprites).
- **Genetic / Hybridization Algorithm Status:**
  - **HYBRIDIZATION ALGORITHM:** **[NOT ESTABLISHED]**
  - There is NO static evidence of multi-parent genetic calculation or stochastic genotype/phenotype recombination in the native executable logic.
  - Crop progression is managed via table-driven tile sprite ID increments upon user watering/harvest events in `FUN_00404170`.
