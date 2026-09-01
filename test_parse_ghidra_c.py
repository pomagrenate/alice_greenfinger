import os
import re

exe_c_path = r'reconstructed-source\ACTUAL_GHIDRA_DECOMPILED_EXE.c'
with open(exe_c_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

func_headers = list(re.finditer(r'// -+\n// Function:\s+(\w+)\s+at\s+([0-9a-fA-F]+)\s+\(Param Count:\s+(\d+)\)\n// -+', content))
print(f"Total function headers in Ghidra C: {len(func_headers)}")

functions_code = {}
for i, m in enumerate(func_headers):
    fn_name = m.group(1)
    fn_rva = "0x00" + m.group(2) if len(m.group(2)) == 6 else "0x" + m.group(2)
    params = int(m.group(3))
    start_pos = m.end()
    end_pos = func_headers[i+1].start() if i + 1 < len(func_headers) else len(content)
    code_body = content[start_pos:end_pos].strip()
    functions_code[fn_name] = {
        'rva': fn_rva,
        'params': params,
        'code': code_body
    }

print("Sample parsed:", list(functions_code.keys())[:10])
print("FUN_00404170 present:", 'FUN_00404170' in functions_code)
if 'FUN_00404170' in functions_code:
    print("FUN_00404170 code length:", len(functions_code['FUN_00404170']['code']))
