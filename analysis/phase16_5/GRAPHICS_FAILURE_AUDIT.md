# ALICE GREENFINGERS — GRAPHICS RUNTIME AUDIT (PHASE 16.5)

*Generated on 2026-09-01 19:55:15*

## 1. TARGET BINARY IMMUTABILITY
- **Path:** `C:\Users\Admin\Downloads\AliceGreenfingers_RE\extracted\AliceGreenfingers_unpacked.exe`
- **SHA-256:** `caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1`
- **Modified Bytes:** **0 bytes**

## 2. ROOT-CAUSE FAILURE ANALYSIS OF PLACEHOLDER RENDERING
| Subsystem | Symptom | Root Cause | Evidence | Remediation Strategy |
| :--- | :--- | :--- | :---: | :--- |
| **Title Screen** | Solid SeaGreen fill + basic text boxes | `Renderer_RenderFrame` did not blit `TitleBG.png` and `TitleSprites.png` | E2 | Load `TitleBG.bin` / `TitleSprites.bin` and composit directly |
| **Farm Background** | Solid OliveGreen canvas fill | Terrain tiles in `Tiles.png` not mapped to grid | E2/E4 | Blit 64x64 terrain tiles from `Tiles.bin` across 5x8 grid |
| **Crop Sprites** | Solid geometric color boxes (orange/green) | `Sprites.png` sub-rectangles not mapped to growth stages | E2/E4 | Map Stages 1..4 to actual recovered crop sprites in `Sprites.bin` |
| **Player Avatar** | No Alice sprite drawn | `Alice.png` animation frames unreferenced in renderer | E2 | Sample Alice idle frame from `Alice.bin` onto farm canvas |
| **GUI HUD** | Flat solid dark rectangle top bar | `Interface.png` buttons/coin frames unreferenced | E2 | Blit interface frame and currency coin badges from `Interface.bin` |
| **Market Screen** | Brown background with plain text boxes | `Market.png` building/stall art unreferenced | E2 | Blit actual town market scene from `Market.bin` |
