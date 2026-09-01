// ==========================================================================
// ALICE GREENFINGERS - MAIN WORLD FRAME RENDER & GAME LOOP
// Target: FUN_004096a0
// Evidence: notes/FUN_004096A0_DEEP_AUDIT.md & GAME_LOOP_BLUEPRINT.md
// Confidence: [VERIFIED]
// ==========================================================================

#pragma once
#ifndef GAME_LOOP_H
#define GAME_LOOP_H

#include "generated/recovered_types.h"

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Original RVA: 0x004096a0
 * Subsystem:    SUBSYS_FRAME_RENDER
 * Role:         60 Hz Main Frame Render & Tile/Layer Update Loop
 */
int FUN_004096a0(void* renderer_ctx, int delta_time, int render_flags, void* input_queue);

void GameLoop_Tick(void* renderer_ctx, int delta_ms);

#ifdef __cplusplus
}
#endif

#endif // GAME_LOOP_H
