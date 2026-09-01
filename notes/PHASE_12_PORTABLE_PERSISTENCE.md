# ALICE GREENFINGERS - PORTABLE PERSISTENCE LAYER (STEP 12)

*Generated on 2026-09-01*

## 1. Portable Save File Specification
- **Filename:** `savegame.dat` (located in user profile directory or executable root).
- **Format:** Unencrypted binary stream with `AGSV` header (`0x41475356`).
- **Classification:** `SAVE_ENCRYPTION_NOT_ESTABLISHED` (Maintained).
- **Endianness:** Little-endian across all fields (standard x86/x86_64).
