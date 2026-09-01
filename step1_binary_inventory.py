import pefile
import os
import datetime

exe_unpacked_path = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE\extracted\AliceGreenfingers_unpacked.exe'
dll_path = r'e:\Program Files\Games for Windows\Alice Greenfingers [PopCap]\AliceGreenfingers.dll'
fmod_path = r'e:\Program Files\Games for Windows\Alice Greenfingers [PopCap]\fmod.dll'

out_file = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE\notes\RE_BINARY_INVENTORY.md'

def analyze_pe(path, name):
    pe = pefile.PE(path)
    info = {}
    info['name'] = name
    info['size'] = os.path.getsize(path)
    info['arch'] = 'x86 (32-bit)' if pe.FILE_HEADER.Machine == 0x14c else 'x64 (64-bit)'
    info['image_base'] = hex(pe.OPTIONAL_HEADER.ImageBase)
    info['entry_point'] = hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint)
    info['subsystem'] = pe.OPTIONAL_HEADER.Subsystem
    
    # Sections
    sections = []
    for s in pe.sections:
        s_name = s.Name.decode('utf-8', errors='ignore').rstrip('\x00')
        sections.append({
            'name': s_name,
            'virtual_address': hex(s.VirtualAddress),
            'virtual_size': hex(s.Misc_VirtualSize),
            'raw_size': hex(s.SizeOfRawData),
            'characteristics': hex(s.Characteristics),
            'is_exec': bool(s.Characteristics & 0x20000000),
            'is_read': bool(s.Characteristics & 0x40000000),
            'is_write': bool(s.Characteristics & 0x80000000)
        })
    info['sections'] = sections
    
    # Imports
    imports = {}
    if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            dll_name = entry.dll.decode('utf-8', errors='ignore')
            func_names = []
            for imp in entry.imports:
                if imp.name:
                    func_names.append(imp.name.decode('utf-8', errors='ignore'))
                else:
                    func_names.append(f'Ordinal_{imp.ordinal}')
            imports[dll_name] = func_names
    info['imports'] = imports
    
    # Exports
    exports = []
    if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            exp_name = exp.name.decode('utf-8', errors='ignore') if exp.name else f'Ordinal_{exp.ordinal}'
            exports.append((exp_name, hex(exp.address)))
    info['exports'] = exports
    
    # TLS
    info['tls'] = hasattr(pe, 'DIRECTORY_ENTRY_TLS')
    
    # Relocations
    info['relocations'] = hasattr(pe, 'DIRECTORY_ENTRY_BASERELOC')
    
    # Resources
    res_count = 0
    if hasattr(pe, 'DIRECTORY_ENTRY_RESOURCE'):
        for type_dir in pe.DIRECTORY_ENTRY_RESOURCE.entries:
            if hasattr(type_dir, 'directory'):
                res_count += len(type_dir.directory.entries)
    info['resources_count'] = res_count

    return info

print('Analyzing binary PE structures...')
inv_unpacked = analyze_pe(exe_unpacked_path, 'AliceGreenfingers.exe (Unpacked Executable)')
inv_dll = analyze_pe(dll_path, 'AliceGreenfingers.dll (Core Engine DLL)')
inv_fmod = analyze_pe(fmod_path, 'fmod.dll (Audio Subsystem DLL)')

with open(out_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - COMPLETE BINARY INVENTORY (STEP 1)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    
    for inv in [inv_unpacked, inv_dll, inv_fmod]:
        f.write(f'## {inv["name"]}\n')
        f.write(f'- **File Size:** {inv["size"]:,} bytes\n')
        f.write(f'- **Architecture:** {inv["arch"]}\n')
        f.write(f'- **Image Base:** `{inv["image_base"]}`\n')
        f.write(f'- **Address of Entry Point (RVA):** `{inv["entry_point"]}`\n')
        f.write(f'- **TLS Directory Present:** `{inv["tls"]}`\n')
        f.write(f'- **Base Relocations Present:** `{inv["relocations"]}`\n')
        f.write(f'- **Resource Directory Entry Count:** {inv["resources_count"]}\n')
        f.write(f'- **Imported DLL Count:** {len(inv["imports"])}\n')
        f.write(f'- **Exported Symbol Count:** {len(inv["exports"])}\n\n')
        
        f.write('### Memory Sections & Characteristics\n')
        f.write('| Section Name | Virtual Address | Virtual Size | Raw Size | Executable | Readable | Writable | Characteristics |\n')
        f.write('| --- | --- | --- | --- | --- | --- | --- | --- |\n')
        for s in inv['sections']:
            f.write(f'| `{s["name"]}` | `{s["virtual_address"]}` | `{s["virtual_size"]}` | `{s["raw_size"]}` | `{s["is_exec"]}` | `{s["is_read"]}` | `{s["is_write"]}` | `{s["characteristics"]}` |\n')
        f.write('\n')
        
        f.write('### Imported Libraries & Functions (Summary)\n')
        for dll_n, funcs in list(inv['imports'].items())[:15]:
            f.write(f'- **`{dll_n}`** ({len(funcs)} functions imported): `{", ".join(funcs[:6])}{"..." if len(funcs)>6 else ""}`\n')
        f.write('\n')
        
        if inv['exports']:
            f.write('### Exported Functions\n')
            for exp_name, exp_addr in inv['exports'][:20]:
                f.write(f'- `{exp_name}` at `{exp_addr}`\n')
            f.write('\n')
        f.write('---\n\n')

print(f'STEP 1 Binary Inventory complete! Written to {out_file}')
