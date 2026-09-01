# ALICE GREENFINGERS - RENDER STATE MODEL (STEP 9)

*Generated on 2026-09-01*

## 1. Decoupled Render State Boundary
- **Header:** `include/rendering/render_state.h`
- **Design:** The renderer never queries arbitrary global registers directly. Instead, `Render_ExtractState()` captures a point-in-time snapshot of proven game variables.
- **Snapshot Properties:**
  - `current_state`: Active game state (`DAT_004974f4`)
  - `simulation_tick`: Frame counter (`DAT_004a7f54`)
  - `currency_balance`: Money register (`DAT_004a86a4`)
  - `sprite_atlas_handle`: Asset pointer (`DAT_00497528`)
  - `audio_active`: FMOD status (`DAT_004b1200`)
  - `cursor_x`, `cursor_y`, `is_cursor_down`: Current mouse position
