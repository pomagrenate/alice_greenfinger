// ==========================================================================
// ALICE GREENFINGERS - SOFTWARE BACKBUFFER RENDERER IMPLEMENTATION
// ==========================================================================

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "rendering/renderer.h"
#include "generated/recovered_globals.h"
#include "platform/input.h"

static uint32_t s_backbuffer[RENDER_WIDTH * RENDER_HEIGHT];
static uint32_t s_frames_rendered = 0;

RenderState Render_ExtractState(void) {
    const MouseState* ms = Input_GetMouseState();
    RenderState rs;
    rs.current_state = (RecoveredGameState)DAT_004974f4;
    rs.simulation_tick = DAT_004a7f54;
    rs.currency_balance = DAT_004a86a4;
    rs.sprite_atlas_handle = DAT_00497528;
    rs.audio_active = DAT_004b1200;
    rs.cursor_x = ms ? ms->x : 0;
    rs.cursor_y = ms ? ms->y : 0;
    rs.is_cursor_down = ms ? ms->left_down : false;
    return rs;
}

void Renderer_Initialize(void) {
    memset(s_backbuffer, 0, sizeof(s_backbuffer));
    s_frames_rendered = 0;
}

void Renderer_Shutdown(void) {
    // No-op for static backbuffer
}

static void DrawRect(int x0, int y0, int w, int h, uint32_t color) {
    for (int y = y0; y < y0 + h && y < RENDER_HEIGHT; y++) {
        if (y < 0) continue;
        for (int x = x0; x < x0 + w && x < RENDER_WIDTH; x++) {
            if (x < 0) continue;
            s_backbuffer[y * RENDER_WIDTH + x] = color;
        }
    }
}

void Renderer_RenderFrame(const RenderState* state) {
    if (!state) return;

    // Layer 1: Background Fill based on State
    uint32_t bg_color = 0xFF2E8B57; // Default SeaGreen
    switch (state->current_state) {
        case STATE_STARTUP:       bg_color = 0xFF1C1C1C; break; // Dark Gray
        case STATE_MAIN_MENU:     bg_color = 0xFF2E8B57; break; // SeaGreen
        case STATE_NAME_DIALOG:   bg_color = 0xFF3CB371; break; // Medium SeaGreen
        case STATE_GAMEPLAY:      bg_color = 0xFF556B2F; break; // Dark Olive Green (Farm Soil)
        case STATE_PAUSE_OPTIONS: bg_color = 0xFF4A4A4A; break; // Dim Gray
        case STATE_SHOP_MARKET:   bg_color = 0xFF8B4513; break; // Saddle Brown
    }

    for (int i = 0; i < RENDER_WIDTH * RENDER_HEIGHT; i++) {
        s_backbuffer[i] = bg_color;
    }

    // Layer 2: World / Farm Simulation Grid (State 3)
    if (state->current_state == STATE_GAMEPLAY) {
        for (int r = 0; r < 5; r++) {
            for (int c = 0; c < 8; c++) {
                int px = 100 + c * 75;
                int py = 120 + r * 75;
                DrawRect(px, py, 70, 70, 0xFF8B5A2B); // Brown soil plot
                // Crop sprout
                DrawRect(px + 25, py + 25, 20, 20, 0xFF32CD32); // Green sprout
            }
        }
    }

    // Layer 3: GUI & HUD Overlay
    // Top HUD Bar
    DrawRect(0, 0, RENDER_WIDTH, 40, 0xFF202020);

    // Render interactive cursor indicator
    if (state->cursor_x >= 0 && state->cursor_x < RENDER_WIDTH &&
        state->cursor_y >= 0 && state->cursor_y < RENDER_HEIGHT) {
        DrawRect(state->cursor_x - 2, state->cursor_y - 2, 5, 5, state->is_cursor_down ? 0xFFFF0000 : 0xFFFFFFFF);
    }

    s_frames_rendered++;
}

const uint32_t* Renderer_GetBackbuffer(void) {
    return s_backbuffer;
}

uint32_t Renderer_GetTotalFramesRendered(void) {
    return s_frames_rendered;
}
