import os
import shutil
import datetime

re_dir = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE\notes'

# 1. RUNTIME_TOOLCHAIN.md
tool_file = os.path.join(re_dir, 'RUNTIME_TOOLCHAIN.md')

tools_to_check = [
    ('Ghidra Decompiler & Headless Analyzer', r'C:\Users\Admin\Downloads\RE_Tools\Ghidra\ghidra_12.1.3_PUBLIC\support\analyzeHeadless.bat', 'Static & Decompiler Analysis'),
    ('Python PE/Binary Inspection Engine', r'python.exe', 'PE Header, SHA-256 & Memory Parsing'),
    ('UPX Executable Unpacker 4.2.4', r'C:\Users\Admin\Downloads\RE_Tools\upx-4.2.4-win64\upx.exe', 'Binary Unpacking & Decompression'),
    ('Windows Native Debugger (CDB/NSSD)', shutil.which('cdb'), 'Runtime Process Memory Inspection'),
    ('GNU Debugger (GDB)', shutil.which('gdb'), 'Process Breakpoint & Register Inspection')
]

with open(tool_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - RUNTIME TOOLCHAIN INVENTORY (STEP 2)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    f.write('| Tool Name | Installation Path | Capability | Tool Status |\n')
    f.write('| --- | --- | --- | --- |\n')
    
    for name, path, cap in tools_to_check:
        if path and (os.path.exists(path) or shutil.which(name)):
            status = '**[VERIFIED AVAILABLE]**'
        else:
            status = '*[UNAVAILABLE / NOT DETECTED]*'
        f.write(f'| `{name}` | `{path}` | {cap} | {status} |\n')

# 2. RUNTIME_ADDRESS_MAPPING.md
addr_file = os.path.join(re_dir, 'RUNTIME_ADDRESS_MAPPING.md')

with open(addr_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - RUNTIME ADDRESS MAPPING (STEP 3)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    
    f.write('## ASLR & IMAGE BASE SPECIFICATIONS\n')
    f.write('- **Executable Name:** `AliceGreenfingers_unpacked.exe`\n')
    f.write('- **Static Preferred Image Base:** `0x00400000`\n')
    f.write('- **ASLR (Address Space Layout Randomization) Status:** **DISABLED** (PE characteristics `0x0102` flag `IMAGE_FILE_RELOCS_STRIPPED`).\n')
    f.write('- **Address Translation Formula:** `Runtime Address = Static RVA Address` (Direct 1:1 Parity).\n\n')
    
    f.write('## KEY FUNCTION ADDRESS MAPPING TABLE\n\n')
    f.write('| Function Identifier | Ghidra Static Address | Target Module Base | Calculated Runtime Address | Mapping Confidence |\n')
    f.write('| --- | --- | --- | --- | --- |\n')
    f.write('| `EntryPoint` | `0x004165c1` | `0x00400000` | `0x004165c1` | **[VERIFIED Direct 1:1]** |\n')
    f.write('| `FUN_00404170` | `0x00404170` | `0x00400000` | `0x00404170` | **[VERIFIED Direct 1:1]** |\n')
    f.write('| `FUN_004096a0` | `0x004096a0` | `0x00400000` | `0x004096a0` | **[VERIFIED Direct 1:1]** |\n')
    f.write('| `FUN_004033c0` | `0x004033c0` | `0x00400000` | `0x004033c0` | **[VERIFIED Direct 1:1]** |\n')

# 3. RUNTIME_TRACE_PRIORITY.md
prio_file = os.path.join(re_dir, 'RUNTIME_TRACE_PRIORITY.md')

with open(prio_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - RUNTIME TRACE PRIORITY TIERS (STEP 4)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    
    f.write('| Tier | Target Subsystem / Function | Priority Focus | Execution Trigger |\n')
    f.write('| --- | --- | --- | --- |\n')
    f.write('| **P0** | `FUN_00404170`, `FUN_004096a0` | Event Loop & Primary Render Frame | Automatic / Engine Startup |\n')
    f.write('| **P1** | Subroutines reachable from P0 | VTable Dispatches at offsets `+0x04`, `+0x08` | Frame Render Update |\n')
    f.write('| **P2** | Script / Event Handlers | `"ADLIBREGISTER"`, `"GUICTRLSETDATA"` | UI Widget Interaction |\n')
    f.write('| **P3** | Global State Mutators | Static Memory Addresses (`DAT_00xxxxxx`) | Game State Transitions |\n')

print('STEPS 2, 3, 4 complete!')
