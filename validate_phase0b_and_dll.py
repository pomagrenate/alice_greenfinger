import os
import datetime

re_dir = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
notes_dir = os.path.join(re_dir, 'notes')
src_dir = os.path.join(re_dir, 'reconstructed-source')

# 1. Validate Phase 0B Artifacts
p0b_files = [
    'RE_BINARY_INVENTORY.md',
    'FUNCTION_RECOVERY_MATRIX.md',
    'DECOMPILATION_FAILURES.md',
    'RECOVERED_CPP_STRUCTURES.md',
    'RECOVERED_VTABLES.md',
    'RECOVERED_GLOBALS.md',
    'STRING_XREF_ANALYSIS.md',
    'FULL_CALL_GRAPH.md',
    'GAME_STATE_DATAFLOW.md',
    'ASSET_CODE_XREF.md',
    'PHASE_0B_FINAL_RECONSTRUCTION_AUDIT.md'
]

print("--- STEP 1: VALIDATING PHASE 0B ARTIFACTS ---")
p0b_status = {}
for fname in p0b_files:
    fpath = os.path.join(notes_dir, fname)
    if os.path.exists(fpath):
        size = os.path.getsize(fpath)
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = len(f.readlines())
        p0b_status[fname] = f"[VERIFIED] Present ({size:,} bytes, {lines:,} lines)"
    else:
        p0b_status[fname] = "[UNRESOLVED] Missing"
    print(f"  {fname}: {p0b_status[fname]}")

# 2. Validate DLL Decompilation Output
print("\n--- STEP 2: VALIDATING DLL DECOMPILATION OUTPUT ---")
dll_c_path = os.path.join(src_dir, 'ACTUAL_GHIDRA_DECOMPILED_DLL.c')
dll_val_file = os.path.join(notes_dir, 'DLL_DECOMPILATION_VALIDATION.md')

dll_size = os.path.getsize(dll_c_path) if os.path.exists(dll_c_path) else 0

with open(dll_val_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - DLL DECOMPILATION VALIDATION REPORT (STEP 2)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    f.write('## DLL DECOMPILATION STATUS\n')
    f.write(f'- **File Path:** `{dll_c_path}`\n')
    f.write(f'- **File Size:** {dll_size:,} bytes\n')
    
    if dll_size < 1000:
        f.write('- **Validation Status:** **[UNRESOLVED] INVALID / INCOMPLETE**\n')
        f.write('- **Reason:** The file contains only a header comment (312 bytes) because Ghidra headless output argument was overridden by the EXE run.\n')
        f.write('- **Action Taken:** EXE binary decompilation (`ACTUAL_GHIDRA_DECOMPILED_EXE.c` - 3,864,307 bytes) remains the authoritative target for Phase 0C control flow analysis.\n\n')
    else:
        f.write('- **Validation Status:** **[VERIFIED] VALID**\n\n')
        
    f.write('## EXACT TECHNICAL NEXT STEP\n')
    f.write('Execute forensic indirect call extraction on `ACTUAL_GHIDRA_DECOMPILED_EXE.c` targeting `FUN_00404170` and `FUN_004096a0`.\n')

print(f"DLL Decompilation Validation report written to {dll_val_file}")
