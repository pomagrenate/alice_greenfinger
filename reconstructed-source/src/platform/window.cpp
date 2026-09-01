// ==========================================================================
// ALICE GREENFINGERS - WINDOW LIFECYCLE IMPLEMENTATION (WIN32 / HEADLESS)
// ==========================================================================

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include "platform/window.h"

struct PlatformWindow {
    HWND hwnd;
    HDC hdc;
    HDC mem_dc;
    HBITMAP mem_bitmap;
    int width;
    int height;
    bool is_running;
    bool is_headless;
};

static LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    PlatformWindow* win = (PlatformWindow*)GetWindowLongPtr(hwnd, GWLP_USERDATA);
    switch (uMsg) {
        case WM_CLOSE:
        case WM_DESTROY:
            if (win) win->is_running = false;
            PostQuitMessage(0);
            return 0;
        case WM_KEYDOWN:
            if (wParam == VK_ESCAPE) {
                if (win) win->is_running = false;
            }
            return 0;
        default:
            return DefWindowProc(hwnd, uMsg, wParam, lParam);
    }
}

PlatformWindow* Window_Create(const WindowConfig* config) {
    PlatformWindow* win = (PlatformWindow*)calloc(1, sizeof(PlatformWindow));
    if (!win) return nullptr;

    win->width = config ? config->width : 800;
    win->height = config ? config->height : 600;
    win->is_headless = config ? config->headless : false;
    win->is_running = true;

    if (win->is_headless) {
        printf("[PlatformWindow] Initialized Headless Window Context (%dx%d).\n", win->width, win->height);
        return win;
    }

    HINSTANCE hInstance = GetModuleHandle(nullptr);
    WNDCLASSEX wc = {0};
    wc.cbSize = sizeof(WNDCLASSEX);
    wc.style = CS_HREDRAW | CS_VREDRAW;
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.hCursor = LoadCursor(nullptr, IDC_ARROW);
    wc.lpszClassName = "AliceGreenfingersReconstructedWindow";

    RegisterClassEx(&wc);

    RECT wr = {0, 0, win->width, win->height};
    AdjustWindowRect(&wr, WS_OVERLAPPEDWINDOW, FALSE);

    win->hwnd = CreateWindowEx(
        0,
        wc.lpszClassName,
        config && config->title ? config->title : "Alice Greenfingers (Reconstructed)",
        WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_MINIMIZEBOX,
        CW_USEDEFAULT, CW_USEDEFAULT,
        wr.right - wr.left, wr.bottom - wr.top,
        nullptr, nullptr, hInstance, nullptr
    );

    if (!win->hwnd) {
        printf("[PlatformWindow] Failed to create Win32 window. Falling back to headless.\n");
        win->is_headless = true;
        return win;
    }

    SetWindowLongPtr(win->hwnd, GWLP_USERDATA, (LONG_PTR)win);
    win->hdc = GetDC(win->hwnd);
    win->mem_dc = CreateCompatibleDC(win->hdc);
    win->mem_bitmap = CreateCompatibleBitmap(win->hdc, win->width, win->height);
    SelectObject(win->mem_dc, win->mem_bitmap);

    ShowWindow(win->hwnd, SW_SHOW);
    UpdateWindow(win->hwnd);
    printf("[PlatformWindow] Initialized Win32 Window Context (%dx%d).\n", win->width, win->height);
    return win;
}

void Window_Destroy(PlatformWindow* window) {
    if (!window) return;
    if (!window->is_headless && window->hwnd) {
        if (window->mem_bitmap) DeleteObject(window->mem_bitmap);
        if (window->mem_dc) DeleteDC(window->mem_dc);
        if (window->hdc) ReleaseDC(window->hwnd, window->hdc);
        DestroyWindow(window->hwnd);
    }
    free(window);
}

bool Window_PollEvents(PlatformWindow* window) {
    if (!window) return false;
    if (window->is_headless) {
        return window->is_running;
    }

    MSG msg;
    while (PeekMessage(&msg, nullptr, 0, 0, PM_REMOVE)) {
        if (msg.message == WM_QUIT) {
            window->is_running = false;
            return false;
        }
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    return window->is_running;
}

bool Window_IsRunning(const PlatformWindow* window) {
    return window && window->is_running;
}

void Window_RequestClose(PlatformWindow* window) {
    if (window) window->is_running = false;
}

void Window_PresentBuffer(PlatformWindow* window, const uint32_t* pixel_buffer, int width, int height) {
    if (!window || window->is_headless || !pixel_buffer) return;

    BITMAPINFO bmi = {0};
    bmi.bmiHeader.biSize = sizeof(BITMAPINFOHEADER);
    bmi.bmiHeader.biWidth = width;
    bmi.bmiHeader.biHeight = -height; // Top-down DIB
    bmi.bmiHeader.biPlanes = 1;
    bmi.bmiHeader.biBitCount = 32;
    bmi.bmiHeader.biCompression = BI_RGB;

    SetDIBitsToDevice(
        window->hdc,
        0, 0, width, height,
        0, 0, 0, height,
        pixel_buffer,
        &bmi,
        DIB_RGB_COLORS
    );
}
