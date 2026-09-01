import re

with open('notes/STRING_XREF_ANALYSIS.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's count table rows
table_lines = [l for l in text.splitlines() if l.strip().startswith('|') and ('`0x' in l or '"' in l)]
print(f"String lines in STRING_XREF_ANALYSIS.md: {len(table_lines)}")

# Let's also extract unique string literals from Ghidra C dump
exe_c_path = r'reconstructed-source\ACTUAL_GHIDRA_DECOMPILED_EXE.c'
with open(exe_c_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

strings_found = set(re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', content))
print(f"Unique string literals in Ghidra C: {len(strings_found)}")
