# ALICE GREENFINGERS - RENDERING ARCHITECTURE (STEP 10)

*Generated on 2026-09-01 13:47:51*

## RENDERING SUBSYSTEM SPECIFICATION

- **Entry Point:** `FUN_004096a0` (Render_MainFrameLayerUpdate)
- **Surface Target:** DirectDraw Surface Backbuffer
- **Frame Rate:** 60 Hz Synchronized Loop
- **Render Layer Stack:**
  1. Background Terrain Layer (`TileSets/` blitter)
  2. Plant & Grid Object Layer (`Graphics/*.gfx` sprite atlas)
  3. GUI Overlay & Cursor Layer (`FUN_00404170` widget blitter)
