import re

exe_c_path = r'reconstructed-source\ACTUAL_GHIDRA_DECOMPILED_EXE.c'
with open(exe_c_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

globals_found = {}
g_matches = re.findall(r'(DAT_[0-9a-fA-F]{8})', content)
for g in g_matches:
    globals_found[g] = globals_found.get(g, 0) + 1

print("DAT_00497528 in Ghidra C:", 'DAT_00497528' in globals_found, globals_found.get('DAT_00497528'))
print("DAT_004b1200 in Ghidra C:", 'DAT_004b1200' in globals_found, globals_found.get('DAT_004b1200'))
