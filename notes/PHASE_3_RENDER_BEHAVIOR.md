# ALICE GREENFINGERS - RENDERING PIPELINE BEHAVIOR (STEP 10)

*Generated on 2026-09-01*

## 1. Render Ordering & Frame Pipeline
- **Frame Rate:** 60 Hz frame render tick loop in `FUN_004096a0`.
- **Layer 1:** Background Terrain Surface (`Render_BlitTerrainLayer`).
- **Layer 2:** Plant / Flower / Crop Sprite Atlas (`Render_BlitSpriteLayer`).
- **Layer 3:** GUI Overlay, Cash, Tools, Cursor (`Render_BlitGuiOverlay`).
- **Surface Flip:** DirectDraw double-buffering page flip (`Render_FlipSurface`).
