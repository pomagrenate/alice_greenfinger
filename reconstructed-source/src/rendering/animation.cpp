// ==========================================================================
// ALICE GREENFINGERS - ANIMATION RUNTIME IMPLEMENTATION
// ==========================================================================

#include "rendering/animation.h"

uint32_t Animation_GetActiveSprite(const SpriteAnimation* anim, uint32_t current_simulation_tick) {
    if (!anim || anim->total_frames == 0) return 0;
    if (anim->frame_duration_ticks == 0) return anim->start_sprite_id;

    uint32_t frame_index = (current_simulation_tick / anim->frame_duration_ticks);
    if (anim->loop) {
        frame_index = frame_index % anim->total_frames;
    } else {
        if (frame_index >= anim->total_frames) {
            frame_index = anim->total_frames - 1;
        }
    }
    return anim->start_sprite_id + frame_index;
}
