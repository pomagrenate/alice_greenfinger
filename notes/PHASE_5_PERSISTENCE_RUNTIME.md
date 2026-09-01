# ALICE GREENFINGERS - PERSISTENCE RUNTIME SPECIFICATION (STEP 12)

*Generated on 2026-09-01*

## 1. File Persistence Architecture
- **I/O Subroutines:** `FUN_004037a0` (ReadFile stream parser), `FUN_00403910` (Block reader), `__write_nolock` (WriteFile).
- **Profile Format:** Key-value structured binary/text streams storing player name, high scores, cash, unlocked tools, and day progression.
- **Encryption Status:** **[NOT-ESTABLISHED]** (Unencrypted standard configuration serialization).
