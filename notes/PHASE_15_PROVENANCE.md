# ALICE GREENFINGERS - CRYPTOGRAPHIC PROVENANCE MODEL (STEP 2)

*Generated on 2026-09-01*

## 1. Provenance Graph Architecture
```text
[Original Binary (SHA-256 caf0c6f7...)]
               │
               ▼
       [Static Disassembly (E1)]
               │
               ▼
     [Reconstructed Source (E2)]
               │
               ▼
      [Standalone Build (E2)]
         │          │          │
         ▼          ▼          ▼
   [Regression] [Diff Trace] [Symbolic]
      (E3)        (E4)         (E6)
         │          │          │
         └──────────┼──────────┘
                    │
                    ▼
     [Long-Term Preservation Dossier]
```
- **Total Provenance Nodes:** 9
- **Total Provenance Edges:** 12
- **Dangling References:** 0 (100% Verified)
