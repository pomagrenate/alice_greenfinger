# ALICE GREENFINGERS - RENDERING BACKEND SPECIFICATION (STEP 10)

*Generated on 2026-09-01*

## 1. 3-Layer Rendering Pipeline
```
+--------------------------------------------------------+
| Layer 3: GUI & HUD Overlay                             | (Score, Money DAT_004a86a4, Tools, Mouse Cursor)
+--------------------------------------------------------+
| Layer 2: World Simulation & Plant Sprite Atlas         | (Grid Tiles, Flowers, Weeds, Sprites.gfx)
+--------------------------------------------------------+
| Layer 1: Terrain Background Surface                    | (TileSets/ Soil, Grass, Paths)
+--------------------------------------------------------+
                           |
                           v
+--------------------------------------------------------+
| Backbuffer Surface Swap (DirectDraw / Modern Blitter)  | (Double-buffer page flip)
+--------------------------------------------------------+
```

## 2. Rendering Order & Invariants
- **Layer 1 (Background):** Blitted first; provides full 800x600 canvas background.
- **Layer 2 (Simulation):** Iterates over active tile grid coordinates; draws plant growth sprites according to `DAT_004a7f54` tick phase.
- **Layer 3 (Overlay):** Blitted last; draws HUD panels, button states, floating coin text, and system mouse cursor.
