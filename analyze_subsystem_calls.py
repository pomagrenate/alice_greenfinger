import re
import os

c_file = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE\reconstructed-source\ACTUAL_GHIDRA_DECOMPILED_DLL.c'
call_graph_file = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE\notes\SUBSYSTEM_CALL_GRAPHS.md'

with open(c_file, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

func_blocks = content.split('// Function: ')
large_funcs = []

for block in func_blocks[1:]:
    lines = block.strip().split('\n')
    header_line = lines[0]
    match = re.search(r'(FUN_[0-9a-fA-F]+)\s+at\s+([0-9a-fA-F]+)\s+\(Param Count:\s+(\d+)\)', header_line)
    if match:
        fn_name = match.group(1)
        fn_addr = match.group(2)
        param_count = match.group(3)
        body = '\n'.join(lines[2:])
        line_count = len(lines) - 2
        
        # Extract function calls inside body
        calls_made = re.findall(r'(FUN_[0-9a-fA-F]+)\s*\(', body)
        unique_calls = list(set(calls_made))
        
        # Extract strings
        strings_found = re.findall(r'\"([^\"]{3,})\"', body)
        
        if line_count > 100:
            large_funcs.append((fn_addr, fn_name, param_count, line_count, strings_found, unique_calls))

with open(call_graph_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - SUBSYSTEM CALL GRAPHS & RECONSTRUCTED ARCHITECTURE\n\n')
    f.write('This document maps major high-complexity C functions (>100 lines of C control flow) decompiled from `AliceGreenfingers.dll`.\n\n')
    
    for addr, name, params, lcount, str_list, calls in large_funcs:
        f.write(f'### Function `{name}` (RVA: `0x{addr}`, {lcount:,} Lines of C Code)\n')
        f.write(f'- **Parameters:** `{params}`\n')
        f.write(f'- **Referenced Strings:** `{", ".join(str_list[:5]) if str_list else "None"}`\n')
        f.write(f'- **Direct Subroutines Called:** `{", ".join(calls[:8]) if calls else "None"}`\n\n')

print(f'Subsystem Call Graph written to {call_graph_file} ({len(large_funcs)} major subsystems cataloged)')
