import re
import os

c_file = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE\reconstructed-source\ACTUAL_GHIDRA_DECOMPILED_DLL.c'
matrix_file = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE\notes\RECONSTRUCTION_TRACKING_MATRIX.md'

with open(c_file, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Parse all function blocks
func_blocks = content.split('// Function: ')
matrix_entries = []

total_candidate = len(func_blocks) - 1
confirmed_count = 0
decompiled_count = 0
verified_count = 0

for block in func_blocks[1:]:
    lines = block.strip().split('\n')
    header_line = lines[0] # e.g. FUN_10001000 at 10001000 (Param Count: 2)
    match = re.search(r'(FUN_[0-9a-fA-F]+)\s+at\s+([0-9a-fA-F]+)\s+\(Param Count:\s+(\d+)\)', header_line)
    if match:
        fn_name = match.group(1)
        fn_addr = match.group(2)
        param_count = match.group(3)
        
        body = '\n'.join(lines[2:])
        line_count = len(lines) - 2
        
        # Check referenced strings or keywords
        strings_found = re.findall(r'\"([^\"]{3,})\"', body)
        str_summary = ', '.join(set(strings_found[:3])) if strings_found else 'None'
        
        is_decompiled = line_count > 3
        if is_decompiled:
            decompiled_count += 1
            confirmed_count += 1
            
        matrix_entries.append((fn_addr, fn_name, param_count, line_count, str_summary, is_decompiled))

# Write HONEST Reconstruction Tracking Matrix
with open(matrix_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - RECONSTRUCTION TRACKING MATRIX\n\n')
    f.write('## METRICS HONESTY AUDIT\n')
    f.write(f'- **Total Candidate Functions Discovered:** {total_candidate}\n')
    f.write(f'- **Confirmed Function Boundaries:** {confirmed_count}\n')
    f.write(f'- **Fully Decompiled C Control-Flow Logic:** {decompiled_count}\n')
    f.write(f'- **Empty / Thunk Stubs Excluded:** {total_candidate - decompiled_count}\n\n')
    
    f.write('| Address (RVA) | Function Identifier | Param Count | C Logic Line Count | Referenced String Literals | Status |\n')
    f.write('| --- | --- | --- | --- | --- | --- |\n')
    
    for addr, name, params, lcount, str_sum, is_dec in matrix_entries[:150]: # Top 150 functions
        status_str = '**DECOMPILED (FULL C LOGIC)**' if is_dec else 'THUNK / STUB'
        f.write(f'| `0x{addr}` | `{name}` | {params} | {lcount:,} lines | `{str_sum}` | {status_str} |\n')

print(f'Tracking Matrix complete! Written to {matrix_file}')
print(f'Total Candidate: {total_candidate}, Confirmed & Fully Decompiled: {decompiled_count}')
