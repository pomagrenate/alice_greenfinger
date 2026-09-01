# ALICE GREENFINGERS - PLATFORM DEPENDENCY AUDIT (STEP 2)

*Generated on 2026-09-01 18:51:21*

## 1. SOURCE CODE DEPENDENCY CLASSIFICATION

| Source Module | Win32 APIs / Headers | Architectural Classification |
| :--- | :--- | :---: |
| `src/platform/win32_boundary.cpp` | windows.h, GetModuleHandleA, MessageBoxA | **`WIN32_REFERENCE`** |
| `src/platform/window.cpp` | RegisterClassExA, CreateWindowExA, SetDIBitsToDevice | **`WIN32_REFERENCE`** |
| `src/platform/input.cpp` | WM_MOUSEMOVE, WM_LBUTTONDOWN, WM_KEYDOWN | **`SAFE_PLATFORM_ABSTRACTION`** |
| `src/rendering/renderer.cpp` | None (Raw 32-bit ARGB Memory backbuffer) | **`CORE_RUNTIME`** |
| `src/state/game_state.cpp` | None | **`CORE_RUNTIME`** |
| `src/events/event_dispatcher.cpp` | None | **`CORE_RUNTIME`** |
| `src/engine/game_loop.cpp` | None (60 Hz deterministic clock DAT_004a7f54) | **`CORE_RUNTIME`** |
| `src/resources/resource_loader.cpp` | fopen, fread (C Standard I/O) | **`SAFE_PLATFORM_ABSTRACTION`** |

## 2. AUDIT SUMMARY
- The Core Game Engine, Simulation Loop, Farm Grid, Economy, and Software Renderer are 100% free of direct Win32 dependencies.
- Platform window creation and backbuffer blitting are isolated in `src/platform/window.cpp`.
