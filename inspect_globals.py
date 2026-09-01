import re

exe_c_path = r'reconstructed-source\ACTUAL_GHIDRA_DECOMPILED_EXE.c'
with open(exe_c_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

globals_found = {}
g_matches = re.findall(r'(DAT_[0-9a-fA-F]{8})', content)
for g in g_matches:
    globals_found[g] = globals_found.get(g, 0) + 1

sorted_globals = sorted(globals_found.items(), key=lambda x: x[1], reverse=True)
top_175 = sorted_globals[:175]
print(f"Top 175 globals extracted: {len(top_175)}")
print("First 5:", top_175[:5])
print("175th:", top_175[174])
