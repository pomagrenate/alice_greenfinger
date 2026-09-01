# ALICE GREENFINGERS - TIMING & PROGRESSION RECONSTRUCTION (STEP 9)

*Completed on 2026-09-01*

## 1. Clock Source & Tick Mechanics
- **Main Loop Clock:** Synchronized 60 Hz frame tick in `FUN_004096a0`.
- **Global Tick Register:** `DAT_004a7f54` (32-bit unsigned integer, incremented once per frame).
- **Time Elapsed Calculation:** `delta_time = current_tick - last_tick;`
- **Threshold Triggers:** Tile growth stages advance every `N` frame ticks (e.g. 60 ticks = 1 second of simulation time).
