# ALICE GREENFINGERS — PHASE 16 BASELINE AUDIT

*Generated on 2026-09-01 19:08:08*

## 1. TARGET BINARY IMMUTABILITY VERIFICATION
- **Path:** `C:\Users\Admin\Downloads\AliceGreenfingers_RE\extracted\AliceGreenfingers_unpacked.exe`
- **SHA-256:** `caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1`
- **Modified Bytes:** **0 bytes (100% Read-Only)**

## 2. RECONSTRUCTED SUBSYSTEM READINESS AUDIT
| Subsystem | Existing Reconstruction State | Playable Readiness | Evidence Level |
| :--- | :--- | :---: | :---: |
| **Windowing / Presentation** | Win32 GDI (800x600) + SDL2 Portable Backend | **READY** | E5 (Experimental) |
| **Input Queue** | Circular FIFO Queue + Normalized Mouse/Key Events | **READY** | E5 (Experimental) |
| **Software Renderer** | 32-bit ARGB 3-Layer Backbuffer Compositor | **READY** | E4 (Differential) |
| **Game State Machine** | 6 States (`STATE_STARTUP`..`STATE_SHOP_MARKET`) | **READY** | E4 (Differential) |
| **Farm Simulation** | 5x8 Grid, 5-Stage Timers, Crop Catalog | **READY** | E4 (Differential) |
| **Economy Ledger** | `DAT_004a86a4` Currency Arithmetic | **READY** | E6 (Symbolic) |
| **Market / Stalls** | Fixed 4-Slot Customer Stall Model | **READY** | E4 (Differential) |
| **Save / Load** | `AGSV` Binary Stream Persistence | **READY** | E4 (Differential) |
| **Audio Subsystem** | FMOD Dynamic Hook + Silent Safe Fallback | **READY** | E5 (Experimental) |
| **Secondary Calls** | 124 Isolated Calls behind Telemetry Stubs | **ISOLATED** | E6 (Symbolic) |

## 3. PLAYABILITY CLASSIFICATION HIERARCHY
- `E1` = Static Binary Evidence
- `E2` = Reconstructed Source Evidence
- `E3` = Runtime Observation
- `E4` = Differential Correlation
- `E5` = Reproducible Experiment
- `E6` = Automated Symbolic / Constraint Evidence
- `E7` = Playable Runtime Verification (assigned upon verified human/interactive play)
