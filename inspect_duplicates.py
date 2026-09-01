import os
import re

with open('notes/FUNCTION_RECOVERY_MATRIX.md', 'r', encoding='utf-8') as f:
    content = f.read()

rows_raw = re.split(r'\n(?=\|\s*`0x[0-9a-fA-F]{8}`)', content)
table_rows = [r for r in rows_raw if r.strip().startswith('| `0x')]

id_counts = {}
for idx, row in enumerate(table_rows):
    flat = ' '.join(row.splitlines())
    parts = [p.strip().replace('`', '').replace('*', '') for p in flat.split('|')[1:-1]]
    if len(parts) >= 8:
        fid = parts[1]
        rva = parts[0]
        if fid in id_counts:
            id_counts[fid].append((idx, rva))
        else:
            id_counts[fid] = [(idx, rva)]

duplicates = {k: v for k, v in id_counts.items() if len(v) > 1}
print(f"Total unique function IDs: {len(id_counts)}")
print(f"Total duplicate function IDs: {len(duplicates)}")
for k, v in list(duplicates.items())[:10]:
    print(f"  {k}: {v}")
