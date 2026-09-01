# Alice Greenfingers — Cryptographic Provenance Model

This document specifies the unidirectional, cryptographically verifiable lineage from the original read-only binary to the final preservation dossier.

```text
[Original Target Binary] (SHA-256 caf0c6f7...)
           │ (Static Disassembly E1)
           ▼
   [Function Catalog]
           │ (Decompilation & Module Structuring E2)
           ▼
  [Reconstructed Source]
           │ (CMake / GCC 15.1.0 Compilation E2)
           ▼
   [Standalone Build]
     │       │       │
     ▼       ▼       ▼
 [Runtime] [Diff] [Symbolic]
   (E3)    (E4)     (E6)
     │       │       │
     └───────┼───────┘
             │ (Archival Manifest & 10 Verification Gates E5)
             ▼
[Forensic Preservation Dossier]
```
