# Alice Greenfingers — Software Backbuffer Rendering Runtime (Phase 16)

## 1. Compositing Pipeline Specification
1. **Layer 0 (Background):** Renders soil background and grid tiles into the 800x600 32-bit ARGB frame.
2. **Layer 1 (Entities & Crops):** Blits crop growth stages (1..4) according to simulation plot timers.
3. **Layer 2 (GUI & Cursor):** Draws player currency display (`DAT_004a86a4`), day counter, seed buttons, and active cursor.
4. **Presentation:** Copies the frame buffer to the OS window via native GDI (`SetDIBitsToDevice`) or portable SDL2 texture.
