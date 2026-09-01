# ALICE GREENFINGERS - BUILD REPRODUCIBILITY (STEP 5)

*Generated on 2026-09-01*

## 1. Toolchain & Compilation Parameters
- **Target Compiler:** MinGW-W64 GCC 15.1.0 (`g++.exe`)
- **C++ Standard:** `-std=c++17` (C++17 required)
- **Build System Generator:** CMake 4.0.1 + Ninja 1.12.1
- **Platform Link Libraries:** `libalice_reconstructed.a`, `gdi32`, `user32`
- **Standalone Build Command:**
  ```powershell
  cmake -B build -S reconstructed-source -G Ninja
  cmake --build build
  ```
- **Distribution Packaging Command:**
  ```powershell
  python tools/package/build_distribution.py
  ```
