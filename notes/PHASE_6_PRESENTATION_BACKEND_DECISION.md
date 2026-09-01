# ALICE GREENFINGERS - PRESENTATION BACKEND SELECTION (STEP 3)

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
