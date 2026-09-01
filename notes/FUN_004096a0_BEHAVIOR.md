# FUN_004096a0 DEEP BEHAVIORAL FORENSIC AUDIT (STEP 4)

*Generated on 2026-09-01*

## 1. Binary Identification & Metadata
- **Function RVA:** `0x004096a0`
- **Subsystem:** `SUBSYS_FRAME_RENDER` (Main World Frame Render & Tile/Layer Update Loop)
- **ABI:** `__thiscall` (`ECX` = Engine Context, `param_1` = Delta Time ms, `param_2` = Render Flags)
- **Classification:** **[VERIFIED]**

## 2. Call Relationships
- **Callers (2):** `WinMain` message loop tick, `VTABLE_00497000` Slot `+0x04`
- **Direct Callees (15):** `FUN_004033c0`, `FUN_00401b10`, `FUN_00408f40`, `FUN_00431d7f`, `FUN_00436565`

## 3. Control Flow & Rendering Architecture
- **60 Hz Tick Synchronization:** Increments global frame tick counter `DAT_004a7f54`.
- **3-Layer Rendering Stack:**
  1. Layer 1 (Background): Blits terrain tile atlas from `TileSets/`.
  2. Layer 2 (Simulation Grid): Blits plant, flower, weed, water, and soil sprites from `Graphics/*.gfx`.
  3. Layer 3 (GUI & Cursor): Renders UI buttons, coins, gold, inventory overlay, and mouse cursor.
- **Double-Buffer Flip:** Invokes DirectDraw surface flip backbuffer swap.

## 4. Evidence Classification
- Frame render loop & layer order: **[VERIFIED]**
- DirectDraw surface swap: **[RUNTIME-OBSERVED]**
