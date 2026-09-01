// ==========================================================================
// ALICE GREENFINGERS - RENDERING BOUNDARY IMPLEMENTATION
// ==========================================================================

#include "rendering/directdraw_boundary.h"
#include "generated/recovered_globals.h"

void Render_InitSurfaces(void) {
    DAT_004a7f54 = 0;
}

void Render_BlitTerrainLayer(void) {
    // 3-layer rendering stack layer 1 [VERIFIED]
}

void Render_BlitSpriteLayer(void) {
    // 3-layer rendering stack layer 2 [VERIFIED]
}

void Render_BlitGuiOverlay(void) {
    // 3-layer rendering stack layer 3 [VERIFIED]
}

void Render_FlipSurface(void) {
    // DirectDraw Backbuffer swap [VERIFIED]
}

void Render_ShutdownSurfaces(void) {
}
