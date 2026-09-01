# ALICE GREENFINGERS - ANIMATION RUNTIME (STEP 12)

*Generated on 2026-09-01*

## 1. Deterministic Animation Engine
- **Header:** `include/rendering/animation.h`
- **Implementation:** `src/rendering/animation.cpp`
- **Determinism:** Frame selection is a pure function of `current_simulation_tick` (`DAT_004a7f54`).
- **Equation:** `active_frame = (tick / frame_duration_ticks) % total_frames;`
