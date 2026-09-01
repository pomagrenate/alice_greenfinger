# FUN_00401500 DEEP BEHAVIORAL FORENSIC AUDIT (STEP 4)

*Generated on 2026-09-01*

## 1. Binary Identification & Metadata
- **Function RVA:** `0x00401500`
- **Subsystem:** `SUBSYS_SCRIPT_HOST` (Script Engine Host & Context Manager)
- **ABI:** `__cdecl`
- **Classification:** **[VERIFIED]**

## 2. Behavioral Role
- Initializes AutoIt3 / Script host runtime tables.
- Registers standard window classes and UI control callbacks (`"SysListView32"`, `"Button"`, `"Edit"`).
- Connects GUI control events to event dispatcher `FUN_00404170`.
- Manages command-line script arguments (`/ErrorStdOut`, `/AutoIt3ExecuteScript`).
