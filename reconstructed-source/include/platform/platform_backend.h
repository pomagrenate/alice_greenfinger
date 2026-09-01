// ==========================================================================
// ALICE GREENFINGERS - UNIFIED PLATFORM BACKEND INTERFACE (PHASE 12)
// Decouples Game Runtime from Win32 / SDL2 Platform Specifics
// ==========================================================================

#ifndef PLATFORM_BACKEND_H
#define PLATFORM_BACKEND_H

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
    PLATFORM_BACKEND_WIN32 = 0,    // Forensic Win32/GDI Reference Backend
    PLATFORM_BACKEND_SDL2  = 1,    // Portable Cross-Platform SDL2 Backend
    PLATFORM_BACKEND_HEADLESS = 2  // Headless Automated Test Backend
} PlatformBackendType;

typedef struct {
    const char* title;
    int width;
    int height;
    bool fullscreen;
    bool headless;
    PlatformBackendType backend_type;
} PlatformConfig;

// Unified Platform Lifecycle
bool Platform_InitializeBackend(PlatformConfig* config);
void Platform_PollEventsBackend(void);
void Platform_PresentSurface(const uint32_t* backbuffer_argb, int width, int height);
void Platform_ShutdownBackend(void);
PlatformBackendType Platform_GetActiveBackendType(void);

#ifdef __cplusplus
}
#endif

#endif // PLATFORM_BACKEND_H
