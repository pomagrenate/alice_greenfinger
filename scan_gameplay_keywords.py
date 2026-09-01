import os
import re

exe_c_path = r'reconstructed-source\ACTUAL_GHIDRA_DECOMPILED_EXE.c'
with open(exe_c_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Let's search for keywords in function bodies
keywords = {
    'plant_flower': ['plant', 'flower', 'hybrid', 'seed', 'water', 'grow', 'harvest'],
    'customer_order': ['customer', 'order', 'queue', 'buyer', 'market', 'shop'],
    'economy': ['money', 'gold', 'coin', 'price', 'cash', 'cost', 'reward'],
    'persistence': ['CreateFile', 'ReadFile', 'WriteFile', 'fopen', 'fread', 'fwrite', 'RegOpenKey', 'profile', 'save', 'score'],
    'asset_decoding': ['LBTC', 'GFX', 'atlas', 'sprite', 'decomp', 'compress']
}

func_headers = list(re.finditer(r'// -+\n// Function:\s+(\w+)\s+at\s+([0-9a-fA-F]+)\s+\(Param Count:\s+(\d+)\)\n// -+', content))

findings = {k: [] for k in keywords}
for i, m in enumerate(func_headers):
    fn_name = m.group(1)
    fn_rva = "0x00" + m.group(2) if len(m.group(2)) == 6 else "0x" + m.group(2)
    start_pos = m.end()
    end_pos = func_headers[i+1].start() if i + 1 < len(func_headers) else len(content)
    code_body = content[start_pos:end_pos]
    
    for cat, kw_list in keywords.items():
        matched_kws = [kw for kw in kw_list if re.search(r'\b' + re.escape(kw) + r'\b', code_body, re.IGNORECASE)]
        if matched_kws:
            findings[cat].append((fn_name, fn_rva, matched_kws, len(code_body.splitlines())))

for cat, lst in findings.items():
    print(f"=== Category: {cat} (Matches: {len(lst)}) ===")
    for item in lst[:5]:
        print(f"  {item[0]} ({item[1]}): Keywords {item[2]}, Lines: {item[3]}")
