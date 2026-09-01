import os
import re

with open('notes/FUNCTION_RECOVERY_MATRIX.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find all row starts
rows_raw = re.split(r'\n(?=\|\s*`0x[0-9a-fA-F]{8}`)', content)
table_rows = [r for r in rows_raw if r.strip().startswith('| `0x')]

print(f"Total multi-line table rows found: {len(table_rows)}")

parsed_funcs = []
for idx, row in enumerate(table_rows):
    # Flatten newlines within the row
    flat = ' '.join(row.splitlines())
    parts = [p.strip().replace('`', '').replace('*', '') for p in flat.split('|')[1:-1]]
    if len(parts) >= 8:
        parsed_funcs.append(parts)
    else:
        print(f"Row {idx} still has {len(parts)} parts: {flat[:100]}...")

print(f"Total parsed functions: {len(parsed_funcs)}")
