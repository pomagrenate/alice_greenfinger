import os
import re

with open('notes/FUNCTION_RECOVERY_MATRIX.md', 'r', encoding='utf-8') as f:
    content = f.read()

rows_raw = re.split(r'\n(?=\|\s*`0x[0-9a-fA-F]{8}`)', content)
table_rows = [r for r in rows_raw if r.strip().startswith('| `0x')]

mismatches = []
for idx, row in enumerate(table_rows):
    flat = ' '.join(row.splitlines())
    parts = [p.strip().replace('`', '').replace('*', '') for p in flat.split('|')[1:-1]]
    if len(parts) >= 8:
        fid = parts[1]
        rva = parts[0]
        expected_fid = f"FUN_{rva.replace('0x00', '00').replace('0x', '')}"
        if fid != expected_fid:
            mismatches.append((idx, rva, fid, expected_fid))

print(f"Total mismatches: {len(mismatches)}")
for m in mismatches:
    print(f"  Row {m[0]}: RVA {m[1]} has FID {m[2]}, expected {m[3]}")
