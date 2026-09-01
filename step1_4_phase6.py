#!/usr/bin/env python3
"""
Phase 6 - Steps 1 to 4:
- Step 1: Baseline Generation & Hash Verification
- Step 2: Existing Runtime Architecture Audit
- Step 3: Presentation Backend Decision Document
- Step 4: Window Lifecycle Abstraction Implementation & Documentation
"""

import os
import sys
import json
import hashlib
import datetime

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
NOTES_DIR = os.path.join(PROJECT_ROOT, 'notes')
ANALYSIS_DIR = os.path.join(PROJECT_ROOT, 'analysis')
SOURCE_DIR = os.path.join(PROJECT_ROOT, 'reconstructed-source')
TARGET_BINARY = os.path.join(PROJECT_ROOT, 'extracted', 'AliceGreenfingers_unpacked.exe')
EXPECTED_SHA256 = 'caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1'

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}")

def run_steps_1_to_4():
    log("=== PHASE 6: RUNNING STEPS 1 TO 4 ===")

    # ---------------------------------------------------------
    # STEP 1: BASELINE & INTEGRITY
    # ---------------------------------------------------------
    if not os.path.exists(TARGET_BINARY):
        raise FileNotFoundError(f"Binary {TARGET_BINARY} missing!")
    current_hash = hashlib.sha256(open(TARGET_BINARY, 'rb').read()).hexdigest()
    if current_hash != EXPECTED_SHA256:
        raise ValueError(f"Binary modified! {current_hash} != {EXPECTED_SHA256}")
    log(f"Verified binary SHA-256: {current_hash}")

    baseline_data = {
        "phase": "PHASE 6",
        "timestamp": datetime.datetime.now().isoformat(),
        "binary_integrity": {
            "file": TARGET_BINARY,
            "size_bytes": os.path.getsize(TARGET_BINARY),
            "sha256": current_hash,
            "modified": False
        },
        "phase5_inherited_metrics": {
            "total_binary_functions": 1847,
            "group_a_reconstructed": 1194,
            "runtime_verified_functions": 170,
            "unresolved_indirect_calls": 425,
            "vtable_slots": 4,
            "recovered_globals": 175,
            "extracted_strings": 874,
            "verified_states": 6,
            "golden_scenarios": 14,
            "asset_containers": 10,
            "runtime_checkpoints": 7
        }
    }
    with open(os.path.join(ANALYSIS_DIR, 'phase6_baseline.json'), 'w', encoding='utf-8') as f:
        json.dump(baseline_data, f, indent=2)

    with open(os.path.join(NOTES_DIR, 'PHASE_6_BASELINE.md'), 'w', encoding='utf-8') as f:
        f.write('# ALICE GREENFINGERS - PHASE 6 BASELINE REPORT (STEP 1)\n\n')
        f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
        f.write('## 1. TARGET BINARY READ-ONLY INTEGRITY\n\n')
        f.write(f'- **Binary Path:** `{TARGET_BINARY}`\n')
        f.write(f'- **File Size:** {os.path.getsize(TARGET_BINARY):,} bytes\n')
        f.write(f'- **SHA-256:** `{current_hash}`\n')
        f.write('- **Integrity State:** **100% UNMODIFIED / READ-ONLY**\n\n')
        f.write('## 2. INHERITED RECONSTRUCTION BASELINE\n\n')
        f.write('- **Cataloged Functions:** 1,847 (100% in Provenance Database)\n')
        f.write('- **Group A Reconstructed Functions:** 1,194 (64.6% coverage)\n')
        f.write('- **Runtime Verified Functions:** 170 (9.2% execution verified)\n')
        f.write('- **Unresolved Indirect Call Sites:** 425 (Triaged into Clusters A–G)\n')
        f.write('- **Verified Game States:** 6 (`STATE_STARTUP` 0 through `STATE_SHOP_MARKET` 5)\n')
        f.write('- **Asset Containers:** 10 PopCap LBTC containers cataloged with SHA-256 hashes\n')
        f.write('- **Golden Scenarios:** 14/14 Passing deterministic behavioral scenarios\n')
        f.write('- **Runtime Checkpoint System:** 7 telemetry checkpoints operational\n')
        f.write('- **Standalone Build Target:** `alice_greenfingers_reconstructed.exe` compiled via CMake / Ninja\n\n')
        f.write('## 3. PHASE 6 OBJECTIVES\n')
        f.write('1. Construct an interactive application window with real-time frame loop.\n')
        f.write('2. Connect mouse and keyboard inputs to the reconstructed event dispatcher.\n')
        f.write('3. Present reconstructed game state across all 6 verified states.\n')
        f.write('4. Preserve headless deterministic simulation independence (14 Golden Scenarios intact).\n')
    log("Step 1: Generated notes/PHASE_6_BASELINE.md and analysis/phase6_baseline.json")

    # ---------------------------------------------------------
    # STEP 2: EXISTING RUNTIME AUDIT
    # ---------------------------------------------------------
    with open(os.path.join(NOTES_DIR, 'PHASE_6_RUNTIME_ARCHITECTURE_AUDIT.md'), 'w', encoding='utf-8') as f:
        f.write('''# ALICE GREENFINGERS - RUNTIME ARCHITECTURE AUDIT (STEP 2)

*Generated on 2026-09-01*

## 1. Runtime Subsystem Inventory
- **Platform Layer (`src/platform/win32_boundary.cpp`):** Handles Win32 initialization and engine context lifecycle.
- **Engine Context (`src/objects/engine_context.cpp`):** Manages primary object layout and `VTABLE_00497000` binding.
- **State Machine (`src/state/game_state.cpp`):** Encapsulates the 6 verified states (`0..5`) and transition rules.
- **Event Dispatcher (`src/events/event_dispatcher.cpp`):** Reconstructs `FUN_00404170` opcode string matching and VTable slot `+0x08` callback dispatch.
- **Game Loop (`src/engine/game_loop.cpp`):** Implements `FUN_004096a0` 60 Hz frame render tick and simulation advancement (`DAT_004a7f54++`).
- **Resource Pipeline (`src/resources/resource_loader.cpp`):** Reconstructs `FUN_004033c0` with `PopCap_LBTC_Header` and `PopCap_Sprite_Entry` parsing.
- **Rendering Boundary (`src/rendering/directdraw_boundary.cpp`):** Provides 3-layer compositing abstraction (Background, Simulation Sprites, GUI Overlay).
- **Audio Boundary (`src/audio/fmod_system.cpp`):** Reconstructs `FUN_00411000` host wrapper and `DAT_004b1200` status flag.
- **Telemetry & Checkpoints:** 425 unresolved calls isolated behind `Unresolved_RecordCall`; structured checkpoint logging in `analysis/runtime_checkpoints/`.
''')
    log("Step 2: Generated notes/PHASE_6_RUNTIME_ARCHITECTURE_AUDIT.md")

    # ---------------------------------------------------------
    # STEP 3: PRESENTATION BACKEND DECISION
    # ---------------------------------------------------------
    with open(os.path.join(NOTES_DIR, 'PHASE_6_PRESENTATION_BACKEND_DECISION.md'), 'w', encoding='utf-8') as f:
        f.write('''# ALICE GREENFINGERS - PRESENTATION BACKEND SELECTION (STEP 3)

*Generated on 2026-09-01*

## 1. Evaluated Options
- **Option A: Native Win32 + GDI / Software Double-Buffer Blitter:**
  - Standard Windows API (`CreateWindowExW`, `RegisterClassExW`, `GetDC`, `BitBlt` / `SetDIBitsToDevice`).
  - Zero external library dependencies (natively provided by MinGW-W64 toolchain).
  - Matches the original binary's native Win32 message loop and DirectDraw software surface architecture.
  - Seamlessly supports dual-mode operation: headless automated testing and interactive windowed execution.
- **Option B: SDL2 Framework:**
  - Requires external dynamic libraries and header installation not bundled in the standalone toolchain.

## 2. Architectural Decision
**Selected Backend:** **Native Win32 Software Double-Buffer Surface Blitter (Option A)**.
- **Rationale:** Minimizes external dependency risk, guarantees 100% compatibility with the existing MinGW-W64 GCC 15.1.0 environment, and directly mirrors the original binary's window lifecycle and input event pipeline.
''')
    log("Step 3: Generated notes/PHASE_6_PRESENTATION_BACKEND_DECISION.md")

    # ---------------------------------------------------------
    # STEP 4: WINDOW LIFECYCLE IMPLEMENTATION
    # ---------------------------------------------------------
    # Create include/platform/window.h
    window_h = os.path.join(SOURCE_DIR, 'include', 'platform', 'window.h')
    with open(window_h, 'w', encoding='utf-8') as f:
        f.write('''// ==========================================================================
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
''')

    # Create src/platform/window.cpp
    window_cpp = os.path.join(SOURCE_DIR, 'src', 'platform', 'window.cpp')
    with open(window_cpp, 'w', encoding='utf-8') as f:
        f.write('''// ==========================================================================
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
        printf("[PlatformWindow] Initialized Headless Window Context (%dx%d).\\n", win->width, win->height);
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
        printf("[PlatformWindow] Failed to create Win32 window. Falling back to headless.\\n");
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
    printf("[PlatformWindow] Initialized Win32 Window Context (%dx%d).\\n", win->width, win->height);
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
''')

    with open(os.path.join(NOTES_DIR, 'PHASE_6_WINDOW_LIFECYCLE.md'), 'w', encoding='utf-8') as f:
        f.write('''# ALICE GREENFINGERS - WINDOW LIFECYCLE SPECIFICATION (STEP 4)

*Generated on 2026-09-01*

## 1. Platform Window Abstraction
- **Header:** `include/platform/window.h`
- **Implementation:** `src/platform/window.cpp`
- **Lifecycle API:**
  - `Window_Create()`: Initializes Win32 window (800x600 standard casual resolution) or headless fallback.
  - `Window_PollEvents()`: Pumps Win32 message queue (`PeekMessage`, `TranslateMessage`, `DispatchMessage`).
  - `Window_PresentBuffer()`: Blits 32-bit software backbuffer directly to display DC via `SetDIBitsToDevice`.
  - `Window_Destroy()`: Cleans up GDC/DIB handles and window instance.
''')
    log("Step 4: Created window.h/cpp and generated notes/PHASE_6_WINDOW_LIFECYCLE.md")

    log("=== PHASE 6: STEPS 1 TO 4 COMPLETED SUCCESSFULLY ===")

if __name__ == '__main__':
    run_steps_1_to_4()
