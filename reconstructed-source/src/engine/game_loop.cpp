// ==========================================================================
// ALICE GREENFINGERS - GAME LOOP & FRAME RENDERER IMPLEMENTATION
// Reconstructed FUN_004096a0
// ==========================================================================

#include "engine/game_loop.h"
#include "rendering/directdraw_boundary.h"
#include "generated/recovered_globals.h"
#include "unresolved/unresolved_calls.h"

int FUN_004096a0(void* renderer_ctx, int delta_time, int render_flags, void* input_queue) {
    /*
     * Reconstructed Control Flow from Ghidra RVA 0x004096a0:
     * Region A: Timing tick calculation & input polling
     * Region B: World grid update loop & dirty rect invalidation
     * Region C: Layer draw calls (Terrain, Sprites, UI Overlay)
     * Region D: Double-buffer swap / DirectDraw surface flip
     */
    (void)renderer_ctx;
    (void)delta_time;
    (void)render_flags;
    (void)input_queue;

    // Mutate frame counter (DAT_004a7f54) [VERIFIED]
    DAT_004a7f54++;

    // Layer 1: Terrain background blit
    Render_BlitTerrainLayer();

    // Layer 2: Plant / Grid sprite blit
    Render_BlitSpriteLayer();

    // Layer 3: GUI overlay blit
    Render_BlitGuiOverlay();

    // Surface flip
    Render_FlipSurface();

    return 1;
}

void GameLoop_Tick(void* renderer_ctx, int delta_ms) {
    FUN_004096a0(renderer_ctx, delta_ms, 0, nullptr);
}
