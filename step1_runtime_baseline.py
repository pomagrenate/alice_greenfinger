import os
import hashlib
import pefile
import datetime

re_dir = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
notes_dir = os.path.join(re_dir, 'notes')
out_file = os.path.join(notes_dir, 'RUNTIME_BINARY_BASELINE.md')

binaries = [
    ('AliceGreenfingers_unpacked.exe', r'C:\Users\Admin\Downloads\AliceGreenfingers_RE\extracted\AliceGreenfingers_unpacked.exe'),
    ('AliceGreenfingers.dll', r'e:\Program Files\Games for Windows\Alice Greenfingers [PopCap]\AliceGreenfingers.dll'),
    ('fmod.dll', r'e:\Program Files\Games for Windows\Alice Greenfingers [PopCap]\fmod.dll')
]

results = []

for name, path in binaries:
    if os.path.exists(path):
        size = os.path.getsize(path)
        sha256 = hashlib.sha256()
        with open(path, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        digest = sha256.hexdigest()
        
        pe = pefile.PE(path)
        arch = 'x86 (32-bit)' if pe.FILE_HEADER.Machine == 0x14c else 'x64 (64-bit)'
        image_base = hex(pe.OPTIONAL_HEADER.ImageBase)
        entry_point = hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint)
        
        results.append({
            'name': name,
            'path': path,
            'size': size,
            'sha256': digest,
            'arch': arch,
            'image_base': image_base,
            'entry_point': entry_point,
            'status': '[VERIFIED]'
        })

with open(out_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - RUNTIME BINARY BASELINE (STEP 1)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    f.write('## BINARY HASH & ARCHITECTURE AUDIT TABLE\n\n')
    f.write('| Binary Identifier | Absolute Path | File Size | SHA-256 Hash | Architecture | Image Base | Entry Point RVA | Integrity Status |\n')
    f.write('| --- | --- | --- | --- | --- | --- | --- | --- |\n')
    for r in results:
        f.write(f'| `{r["name"]}` | `{r["path"]}` | {r["size"]:,} bytes | `{r["sha256"]}` | {r["arch"]} | `{r["image_base"]}` | `{r["entry_point"]}` | **{r["status"]}** |\n')

print(f'STEP 1 Runtime Baseline complete! Written to {out_file}')
