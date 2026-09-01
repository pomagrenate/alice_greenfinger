import os
import re

exe_c_path = r'reconstructed-source\ACTUAL_GHIDRA_DECOMPILED_EXE.c'
with open(exe_c_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Let's locate specific functions
target_fids = ['FUN_00404170', 'FUN_004096a0', 'FUN_00401500', 'FUN_004033c0', 'FUN_0040d590', 'FUN_00411000', 'entry']
for fid in target_fids:
    pos = content.find(fid)
    if pos != -1:
        # Find enclosing function definition
        start = content.rfind('\n', 0, pos)
        func_chunk = content[start:start+2500]
        print(f"=== Found {fid} at offset {pos} ===")
        print(func_chunk[:300] + "\n...\n")
    else:
        print(f"=== {fid} NOT found ===")
