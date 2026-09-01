# ALICE GREENFINGERS - DETERMINISTIC SIMULATION RUNTIME (STEP 9)

*Generated on 2026-09-01*

## 1. Deterministic Simulation Clock
- **Clock Source:** Fixed 60 Hz simulation timestep (16.67 ms per tick) in `FUN_004096a0`.
- **Global Frame Register:** `DAT_004a7f54` (monotonically increasing 32-bit unsigned integer).
- **Determinism Guarantee:** Every simulation frame executes with a fixed delta time (`16` ms), guaranteeing reproducible state mutations across runs.
- **Snapshot & Replay:** State snapshots record `DAT_004974f4` (State), `DAT_004a7f54` (Ticks), and `DAT_004a86a4` (Currency).
