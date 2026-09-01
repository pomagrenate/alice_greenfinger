# ALICE GREENFINGERS - SAVE / LOAD ROUND-TRIP PERSISTENCE (STEP 12)

*Generated on 2026-09-01 18:00:53*

## 1. SERIALIZATION PAYLOAD SPECIFICATION

| Persisted State Field | Data Type | Forensic Verification |
| :--- | :--- | :---: |
| Profile Name | `char[32]` | **[VERIFIED]** |
| Currency Balance (DAT_004a86a4) | `uint32_t` | **[VERIFIED]** |
| Day Counter | `uint32_t` | **[VERIFIED]** |
| Farm Grid Plot States (5x8) | `uint8_t[40]` | **[VERIFIED]** |
| Unlocked Crop Bitmask | `uint32_t` | **[VERIFIED]** |

## 2. CRYPTOGRAPHIC FINDING
- Stream serializer uses direct binary byte fields via `FUN_004037a0` / `FUN_00403910`.
- Custom cryptographic save-profile encryption: **[NOT ESTABLISHED]**.
