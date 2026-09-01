# ALICE GREENFINGERS - INDIRECT CALL ABI & CALLING CONVENTION ANALYSIS (STEP 9)

*Generated on 2026-09-01 13:24:48*

## CALLING CONVENTION CLASSIFICATION MATRIX

| Calling Convention | Register / Stack Mechanics | Evidence Indicators | Primary Usage Area | Confidence |
| --- | --- | --- | --- | --- |
| `__thiscall` | `ECX` passes `this` pointer, caller pushes args right-to-left | `param_1` accessed via `*(this + offset)` | C++ Object VTable Methods | **[HIGH-CONFIDENCE]** |
| `__cdecl` | Arguments on stack right-to-left, caller cleans up stack | C++ global helpers, CRT utility functions | Memory allocation & File I/O | **[VERIFIED]** |
| `__stdcall` | Arguments on stack right-to-left, callee cleans up stack (`ret N`) | Win32 API imports (`USER32.dll`, `KERNEL32.dll`) | Win32 Host & OS Interop | **[VERIFIED]** |
