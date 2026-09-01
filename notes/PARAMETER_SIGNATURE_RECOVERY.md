# ALICE GREENFINGERS - PARAMETER SIGNATURE RECOVERY (STEP 4)

*Generated on 2026-09-01 13:41:00*

| Function Identifier | Recovered Signature | ABI Classification | Evidence Rationale | Confidence |
| --- | --- | --- | --- | --- |
| `FUN_00404170` | `int __stdcall FUN_00404170(int cmd_id, void* ctx)` | `__stdcall` | Stack arguments cleaned up by callee (`ret 0x08`) | **[HIGH-CONFIDENCE]** |
| `FUN_004096a0` | `void __thiscall FUN_004096a0(void* this, int delta_t)` | `__thiscall` | `ECX` contains instance pointer before entry | **[HIGH-CONFIDENCE]** |
| `FUN_004033c0` | `int __cdecl FUN_004033c0(char* path, int mode)` | `__cdecl` | Caller cleans stack (`add esp, 0x08`) | **[VERIFIED]** |
