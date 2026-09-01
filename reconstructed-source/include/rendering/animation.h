// ==========================================================================
// ALICE GREENFINGERS - ANIMATION RUNTIME ABSTRACTION
// ==========================================================================

#pragma once
#ifndef ANIMATION_RUNTIME_H
#define ANIMATION_RUNTIME_H

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct SpriteAnimation {
    uint32_t start_sprite_id;
    uint32_t total_frames;
    uint32_t frame_duration_ticks;
    bool loop;
} SpriteAnimation;

uint32_t Animation_GetActiveSprite(const SpriteAnimation* anim, uint32_t current_simulation_tick);

#ifdef __cplusplus
}
#endif

#endif // ANIMATION_RUNTIME_H
