# ALICE GREENFINGERS - ASSET PIPELINE ARCHITECTURE (STEP 4)

*Generated on 2026-09-01 17:39:54*

## RECOVERED ASSET CONTAINERS INVENTORY

| Container Name | Metadata Source | Format Specification | Sub-Sprite Entries | Pipeline Status |
| --- | --- | --- | ---: | --- |
| `Alice.gfx` | `Alice_metadata.txt` | `PopCap LBTC Container (Version 1)` | 174 sub-sprites | **[PARSED & VALIDATED]** |
| `Interface.gfx` | `Interface_metadata.txt` | `PopCap LBTC Container (Version 1)` | 47 sub-sprites | **[PARSED & VALIDATED]** |
| `Loading.gfx` | `Loading_metadata.txt` | `PopCap LBTC Container (Version 1)` | 5 sub-sprites | **[PARSED & VALIDATED]** |
| `Market.gfx` | `Market_metadata.txt` | `PopCap LBTC Container (Version 1)` | 199 sub-sprites | **[PARSED & VALIDATED]** |
| `OptionSprites.gfx` | `OptionSprites_metadata.txt` | `PopCap LBTC Container (Version 1)` | 252 sub-sprites | **[PARSED & VALIDATED]** |
| `Sprites.gfx` | `Sprites_metadata.txt` | `PopCap LBTC Container (Version 1)` | 622 sub-sprites | **[PARSED & VALIDATED]** |
| `System.gfx` | `System_metadata.txt` | `PopCap LBTC Container (Version 1)` | 1186 sub-sprites | **[PARSED & VALIDATED]** |
| `Tiles.gfx` | `Tiles_metadata.txt` | `PopCap LBTC Container (Version 1)` | 320 sub-sprites | **[PARSED & VALIDATED]** |
| `TitleSprites.gfx` | `TitleSprites_metadata.txt` | `PopCap LBTC Container (Version 1)` | 296 sub-sprites | **[PARSED & VALIDATED]** |
| `TrialSprites.gfx` | `TrialSprites_metadata.txt` | `PopCap LBTC Container (Version 1)` | 11 sub-sprites | **[PARSED & VALIDATED]** |

## ASSET LOADING PIPELINE ARCHITECTURE

1. **Archive Locate:** Searches `Graphics/` and `TileSets/` for target `.gfx` containers.
2. **Header Verify:** `Resource_ValidateLBTCHeader()` validates `"LBTC"` magic (0x4354424C) and version 1.
3. **TOC Indexing:** Parses `PopCap_Sprite_Entry` array (`src_x`, `src_y`, `width`, `height`, `dest_x_offset`, `dest_y_offset`).
4. **Handle Assignment:** Assigns sprite atlas handle to global `DAT_00497528`.
5. **Renderer Binding:** Supplies sprite sub-rectangles to Layer 2/3 rendering compositors.
