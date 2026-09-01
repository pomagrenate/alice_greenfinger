# ALICE GREENFINGERS - PLATFORM ARCHITECTURE DESIGN (STEP 3)

*Generated on 2026-09-01*

## 1. Unified Platform Abstraction Layer
```text
                  +--------------------------------+
                  |       Core Game Engine         |
                  |  (Simulation, State, Economy)  |
                  +---------------+----------------+
                                  |
                  +---------------v----------------+
                  |    Platform Backend Wrapper    |
                  |     (platform_backend.h)       |
                  +-------+--------------+---------+
                          |              |
           +--------------v-+          +-v--------------+
           | Win32/GDI Ref  |          | SDL2 Portable  |
           |  (window.cpp)  |          | (sdl2_window)  |
           +----------------+          +----------------+
```
- **Win32/GDI Backend:** Forensic Reference implementation preserving exact original PE behavior.
- **SDL2 Portable Backend:** Portable cross-platform reimplementation for POSIX/Linux.
- **Headless Backend:** High-speed automated headless test driver.
