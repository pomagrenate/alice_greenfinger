// ==========================================================================
// ALICE GREENFINGERS - SDL2 PORTABLE WINDOW HEADER (PHASE 12)
// Classification: PORTABILITY_IMPLEMENTATION
// ==========================================================================

#ifndef SDL2_WINDOW_H
#define SDL2_WINDOW_H

#include <stdint.h>
#include <stdbool.h>
#include "platform/platform_backend.h"

#ifdef __cplusplus
extern "C" {
#endif

bool SDL2_Platform_Initialize(const PlatformConfig* config);
void SDL2_Platform_PollEvents(void);
void SDL2_Platform_Present(const uint32_t* backbuffer_argb, int width, int height);
void SDL2_Platform_Shutdown(void);

#ifdef __cplusplus
}
#endif

#endif // SDL2_WINDOW_H
