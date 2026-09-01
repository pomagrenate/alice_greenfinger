# ALICE GREENFINGERS - PHASE 6 BASELINE REPORT (STEP 1)

*Generated on 2026-09-01 17:47:12*

## 1. TARGET BINARY READ-ONLY INTEGRITY

- **Binary Path:** `C:\Users\Admin\Downloads\AliceGreenfingers_RE\extracted\AliceGreenfingers_unpacked.exe`
- **File Size:** 732,733 bytes
- **SHA-256:** `caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1`
- **Integrity State:** **100% UNMODIFIED / READ-ONLY**

## 2. INHERITED RECONSTRUCTION BASELINE

- **Cataloged Functions:** 1,847 (100% in Provenance Database)
- **Group A Reconstructed Functions:** 1,194 (64.6% coverage)
- **Runtime Verified Functions:** 170 (9.2% execution verified)
- **Unresolved Indirect Call Sites:** 425 (Triaged into Clusters A–G)
- **Verified Game States:** 6 (`STATE_STARTUP` 0 through `STATE_SHOP_MARKET` 5)
- **Asset Containers:** 10 PopCap LBTC containers cataloged with SHA-256 hashes
- **Golden Scenarios:** 14/14 Passing deterministic behavioral scenarios
- **Runtime Checkpoint System:** 7 telemetry checkpoints operational
- **Standalone Build Target:** `alice_greenfingers_reconstructed.exe` compiled via CMake / Ninja

## 3. PHASE 6 OBJECTIVES
1. Construct an interactive application window with real-time frame loop.
2. Connect mouse and keyboard inputs to the reconstructed event dispatcher.
3. Present reconstructed game state across all 6 verified states.
4. Preserve headless deterministic simulation independence (14 Golden Scenarios intact).
