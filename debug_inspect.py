import os
import re

notes_dir = 'notes'

with open('notes/FUNCTION_RECOVERY_MATRIX.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find all FUN_... or addresses
table_lines = [l for l in text.splitlines() if l.strip().startswith('|') and ('0x004' in l or 'FUN_' in l)]
print(f"Table lines with 0x004 or FUN_: {len(table_lines)}")

# Let's inspect ACTUAL_GHIDRA_DECOMPILED_EXE.c for function definitions
exe_c = r'reconstructed-source\ACTUAL_GHIDRA_DECOMPILED_EXE.c'
if os.path.exists(exe_c):
    with open(exe_c, 'r', encoding='utf-8', errors='ignore') as f:
        c_text = f.read()
    ghidra_funcs = re.findall(r'(?:void|int|uint|char|bool|undefined[0-9]*|ulong|long|ushort|short)\s+(?:__\w+\s+)?(FUN_[0-9a-fA-F]{8}|entry)\s*\(', c_text)
    print(f"Ghidra decompiled unique functions: {len(set(ghidra_funcs))}")
    
# Let's inspect globals in ACTUAL_GHIDRA_DECOMPILED_EXE.c
    dat_globals = set(re.findall(r'DAT_[0-9a-fA-F]{8}', c_text))
    print(f"Unique DAT_ globals in Ghidra C: {len(dat_globals)}")
