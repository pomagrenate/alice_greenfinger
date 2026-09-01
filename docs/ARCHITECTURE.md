# Alice Greenfingers - Reconstructed System Architecture

## 1. High-Level Architecture Overview
```
+-------------------------------------------------------------------------+
|                              Platform Layer                             |
|        (Win32 Window / GDI Backbuffer Blit / Headless Automation)       |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                           Input & Event Layer                           |
|        (Circular FIFO Queue -> FUN_00404170 Opcode Dispatcher)          |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                        Game State Machine (0..5)                        |
|   0: STARTUP | 1: MAIN_MENU | 2: NAME_DIALOG | 3: GAMEPLAY | ...        |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                     Deterministic 60 Hz Simulation                      |
|         (Frame Clock DAT_004a7f54 -> Farm Grid -> Economy Ledger)       |
+-------------------+--------------------------------+--------------------+
                    |                                |
                    v                                v
+------------------------------------+ +----------------------------------+
|          Rendering Layer           | |          Audio Subsystem         |
|  (3-Layer Software ARGB Compositor)| | (FMOD Host Host Wrapper Boundary)|
+------------------------------------+ +----------------------------------+
```
