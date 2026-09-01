# Alice Greenfingers - Forensic Reverse Engineering Methodology

## 1. Evidence Hierarchy (Levels E1 to E5)
- **E1 (Direct Binary Disassembly):** Unambiguous machine instructions recovered from Ghidra decompilation of `AliceGreenfingers_unpacked.exe`.
- **E2 (Static Cross-Reference & Call-Graph Analysis):** XREFs correlating functions, static globals, and string literals.
- **E3 (Controlled Dynamic Runtime Observation):** Live runtime traces and checkpoint state capture.
- **E4 (Asset Format & Metadata Extraction):** Struct declarations decoded from PopCap LBTC `.gfx` binary containers.
- **E5 (Differential Behavioral Verification):** Automated comparison asserting parity between original binary observations and reconstructed code.

## 2. Non-Modification Rule
The original unpacked executable (`extracted/AliceGreenfingers_unpacked.exe`, SHA-256 `caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1`) is strictly read-only and has 0 modified bytes across all phases.
