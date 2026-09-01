# Alice Greenfingers — Comprehensive Forensic Preservation Dossier (Phase 15)

## 1. Original Binary Artifact Identity
- **File Name:** `AliceGreenfingers_unpacked.exe`
- **File Size:** 732,733 bytes
- **SHA-256 Digest:** `caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1`
- **Integrity Status:** **100% Read-Only (0 modified bytes across all phases)**

## 2. Reconstructed Scope Summary
- **Total Binary Functions Cataloged:** 1,847 (100%)
- **Group A Functions Reconstructed:** 1,194 (64.6%)
- **Runtime-Verified Functions:** 406 (22.0%)
- **Resolved Indirect-Call Targets:** 406
- **Probable Dispatch Targets:** 65
- **Isolated Secondary Indirect Calls:** 124 (Proven bounded-unreachable from campaign path)
- **Recovered Static Globals:** 175
- **Verified Campaign States:** 6 (`STATE_STARTUP` through `STATE_SHOP_MARKET`)
- **Asset Containers:** 10 PopCap LBTC containers (`.gfx`)
- **Extracted Atlases:** 15 PNG image files
- **Audio Resources:** 71 audio files (3 OXM tracker modules + 68 OGG sound effects)

## 3. Behavioral, Differential & Symbolic Validation
- **Master Regression Scenarios:** 55/55 PASS (100% Equivalence)
- **Differential Execution-Trace Scenarios:** 12/12 MATCH (31/31 observable semantic events match)
- **Bounded Symbolic Paths:** 12 paths (9 SAT, 3 UNSAT, 0 UNKNOWN)
- **Concrete Symbolic Model Replays:** 9/9 MATCH (100% Replay Fidelity)
- **Controlled Experiments:** 20/20 PASS (10 Phase 13 + 10 Phase 14)
- **Reproducibility Gates:** 10/10 GATES PASS
