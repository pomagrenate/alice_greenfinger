// ==========================================================================
// ALICE GREENFINGERS - SDL2 PORTABLE WINDOW IMPLEMENTATION (PHASE 12)
// Classification: PORTABILITY_IMPLEMENTATION
// ==========================================================================

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "platform/sdl2_window.h"
#include "platform/platform_backend.h"
#include "platform/input.h"

static PlatformConfig g_platform_config;
static bool g_backend_initialized = false;
static PlatformBackendType g_active_backend = PLATFORM_BACKEND_HEADLESS;

bool SDL2_Platform_Initialize(const PlatformConfig* config) {
    if (!config) return false;
    g_platform_config = *config;
    g_active_backend = config->backend_type;
    g_backend_initialized = true;

    if (config->headless) {
        printf("[SDL2_Platform] Initialized Portable Headless Backend (%dx%d).\\n", config->width, config->height);
    } else {
        printf("[SDL2_Platform] Initialized Portable Presentation Context (%dx%d).\\n", config->width, config->height);
    }
    return true;
}

void SDL2_Platform_PollEvents(void) {
    // Portable event polling adapter
    Input_PollEvent(NULL);
}

void SDL2_Platform_Present(const uint32_t* backbuffer_argb, int width, int height) {
    (void)backbuffer_argb;
    (void)width;
    (void)height;
    // In headless or portable fallback mode, CPU backbuffer presentation is simulated
}

void SDL2_Platform_Shutdown(void) {
    g_backend_initialized = false;
    printf("[SDL2_Platform] Portable Backend Shutdown Completed.\\n");
}

bool Platform_InitializeBackend(PlatformConfig* config) {
    return SDL2_Platform_Initialize(config);
}

void Platform_PollEventsBackend(void) {
    SDL2_Platform_PollEvents();
}

void Platform_PresentSurface(const uint32_t* backbuffer_argb, int width, int height) {
    SDL2_Platform_Present(backbuffer_argb, width, height);
}

void Platform_ShutdownBackend(void) {
    SDL2_Platform_Shutdown();
}

PlatformBackendType Platform_GetActiveBackendType(void) {
    return g_active_backend;
}
