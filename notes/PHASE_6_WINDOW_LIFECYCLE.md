# ALICE GREENFINGERS - WINDOW LIFECYCLE SPECIFICATION (STEP 4)

*Generated on 2026-09-01*

## 1. Platform Window Abstraction
- **Header:** `include/platform/window.h`
- **Implementation:** `src/platform/window.cpp`
- **Lifecycle API:**
  - `Window_Create()`: Initializes Win32 window (800x600 standard casual resolution) or headless fallback.
  - `Window_PollEvents()`: Pumps Win32 message queue (`PeekMessage`, `TranslateMessage`, `DispatchMessage`).
  - `Window_PresentBuffer()`: Blits 32-bit software backbuffer directly to display DC via `SetDIBitsToDevice`.
  - `Window_Destroy()`: Cleans up GDC/DIB handles and window instance.
