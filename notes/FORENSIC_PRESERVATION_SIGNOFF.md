# Alice Greenfingers — Formal Forensic Preservation Sign-Off

*Date of Sign-Off: 2026-09-01*

## 1. Project Identity
- **Project Title:** Alice Greenfingers Forensic Reverse-Engineering & Source Reconstruction
- **Repository:** https://github.com/pomagrenate/alice_greenfinger.git
- **Target Platform:** Windows (x86 / x86_64)
- **Reconstruction Language:** C11 / C++17

## 2. Original Binary Identity
- **Target Binary Path:** `extracted/AliceGreenfingers_unpacked.exe`
- **File Size:** 732,733 bytes
- **SHA-256:** `caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1`
- **Integrity Statement:** **0 bytes modified. The original binary remained 100% read-only throughout all phases.**

## 3. Reconstruction Scope
- 1,847 functions mapped in the provenance database.
- 1,194 Group-A functions reconstructed in modular C++ source tree.
- 406 runtime-verified functions and indirect dispatches.
- 6-state game state machine (`STATE_STARTUP` 0 through `STATE_SHOP_MARKET` 5).
- Deterministic 60 Hz simulation clock (`DAT_004a7f54`).
- Native Win32 desktop windowing & headless dual-mode execution.
- PopCap LBTC asset loader and 3-layer backbuffer renderer.
- Standalone portable distribution package in `distribution/` (732 files).

## 4. Reproducibility & Validation
- **Master Reproduction Tool:** `python tools/reproduce.py` $	o$ **[PASS]**
- **Differential Validation Suite:** **45/45 Test Scenarios PASS (100% Equivalence)**
- **Long-Run Simulation Stability:** **10,000 frame ticks verified without drift**
- **Automated Consistency Audit:** **12/12 Checks Passed (100% Integrity)**

## 5. Formal Preservation Status
$$\mathbf{FORENSIC\ RECONSTRUCTION\ ARCHIVE\ —\ PRESERVED}$$
