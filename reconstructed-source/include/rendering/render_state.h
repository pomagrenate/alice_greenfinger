// ==========================================================================
// ALICE GREENFINGERS - RENDER STATE EXTRACTION MODEL
// ==========================================================================

#pragma once
#ifndef RENDER_STATE_H
#define RENDER_STATE_H

#include <stdint.h>
#include <stdbool.h>
#include "state/game_state.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef struct RenderState {
    RecoveredGameState current_state; // DAT_004974f4 (0..5) [VERIFIED]
    uint32_t simulation_tick;          // DAT_004a7f54 [VERIFIED]
    uint32_t currency_balance;        // DAT_004a86a4 [VERIFIED]
    uint32_t sprite_atlas_handle;     // DAT_00497528 [VERIFIED]
    uint32_t audio_active;            // DAT_004b1200 [VERIFIED]
    int cursor_x;
    int cursor_y;
    bool is_cursor_down;
} RenderState;

RenderState Render_ExtractState(void);

#ifdef __cplusplus
}
#endif

#endif // RENDER_STATE_H
