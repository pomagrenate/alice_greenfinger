// ==========================================================================
// ALICE GREENFINGERS - WINDOW LIFECYCLE ABSTRACTION
// ==========================================================================

#pragma once
#ifndef PLATFORM_WINDOW_H
#define PLATFORM_WINDOW_H

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct WindowConfig {
    const char* title;
    int width;
    int height;
    bool fullscreen;
    bool headless;
} WindowConfig;

typedef struct PlatformWindow PlatformWindow;

PlatformWindow* Window_Create(const WindowConfig* config);
void Window_Destroy(PlatformWindow* window);
bool Window_PollEvents(PlatformWindow* window);
bool Window_IsRunning(const PlatformWindow* window);
void Window_RequestClose(PlatformWindow* window);
void Window_PresentBuffer(PlatformWindow* window, const uint32_t* pixel_buffer, int width, int height);

#ifdef __cplusplus
}
#endif

#endif // PLATFORM_WINDOW_H
