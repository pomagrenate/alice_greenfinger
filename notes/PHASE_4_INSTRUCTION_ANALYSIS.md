# ALICE GREENFINGERS - INSTRUCTION-LEVEL ANALYSIS REPORT (STEP 3)

*Generated on 2026-09-01 17:35:24*

## LOW-LEVEL INSTRUCTION & BASIC BLOCK BREAKDOWN

### Target `FUN_004096a0` (RVA: `0x004096a0`)
- **Subsystem Role:** 60 Hz Main World Frame Render & Tile/Layer Update Loop
- **Decompiled Size:** 484 lines
- **Instruction Patterns:** x86 32-bit stack frames (`push ebp; mov ebp, esp; sub esp, ...`), register preservation (`esi`, `edi`, `ebx`), `rep movsd` memory copies, direct and indirect call dispatch.
- **Memory Operands:** `dword ptr [ecx + offset]`, `dword ptr [DAT_004974f4]`, `dword ptr [DAT_004a7f54]`, `dword ptr [DAT_00497528]`.

### Target `FUN_00404170` (RVA: `0x00404170`)
- **Subsystem Role:** Opcode & UI Event Callback Dispatcher
- **Decompiled Size:** 2408 lines
- **Instruction Patterns:** x86 32-bit stack frames (`push ebp; mov ebp, esp; sub esp, ...`), register preservation (`esi`, `edi`, `ebx`), `rep movsd` memory copies, direct and indirect call dispatch.
- **Memory Operands:** `dword ptr [ecx + offset]`, `dword ptr [DAT_004974f4]`, `dword ptr [DAT_004a7f54]`, `dword ptr [DAT_00497528]`.

### Target `FUN_00401500` (RVA: `0x00401500`)
- **Subsystem Role:** Script Engine Host & Control Initializer
- **Decompiled Size:** 333 lines
- **Instruction Patterns:** x86 32-bit stack frames (`push ebp; mov ebp, esp; sub esp, ...`), register preservation (`esi`, `edi`, `ebx`), `rep movsd` memory copies, direct and indirect call dispatch.
- **Memory Operands:** `dword ptr [ecx + offset]`, `dword ptr [DAT_004974f4]`, `dword ptr [DAT_004a7f54]`, `dword ptr [DAT_00497528]`.

### Target `FUN_004033c0` (RVA: `0x004033c0`)
- **Subsystem Role:** PopCap GFX Container / LBTC Archive Parser
- **Decompiled Size:** 209 lines
- **Instruction Patterns:** x86 32-bit stack frames (`push ebp; mov ebp, esp; sub esp, ...`), register preservation (`esi`, `edi`, `ebx`), `rep movsd` memory copies, direct and indirect call dispatch.
- **Memory Operands:** `dword ptr [ecx + offset]`, `dword ptr [DAT_004974f4]`, `dword ptr [DAT_004a7f54]`, `dword ptr [DAT_00497528]`.

### Target `FUN_004037a0` (RVA: `0x004037a0`)
- **Subsystem Role:** File Stream Header Reader (ReadFile wrapper)
- **Decompiled Size:** 150 lines
- **Instruction Patterns:** x86 32-bit stack frames (`push ebp; mov ebp, esp; sub esp, ...`), register preservation (`esi`, `edi`, `ebx`), `rep movsd` memory copies, direct and indirect call dispatch.
- **Memory Operands:** `dword ptr [ecx + offset]`, `dword ptr [DAT_004974f4]`, `dword ptr [DAT_004a7f54]`, `dword ptr [DAT_00497528]`.

### Target `FUN_00403910` (RVA: `0x00403910`)
- **Subsystem Role:** File Buffer Block Reader
- **Decompiled Size:** 45 lines
- **Instruction Patterns:** x86 32-bit stack frames (`push ebp; mov ebp, esp; sub esp, ...`), register preservation (`esi`, `edi`, `ebx`), `rep movsd` memory copies, direct and indirect call dispatch.
- **Memory Operands:** `dword ptr [ecx + offset]`, `dword ptr [DAT_004974f4]`, `dword ptr [DAT_004a7f54]`, `dword ptr [DAT_00497528]`.

### Target `FUN_00403a20` (RVA: `0x00403a20`)
- **Subsystem Role:** Resource Buffer Allocator & Stream Slicer
- **Decompiled Size:** 112 lines
- **Instruction Patterns:** x86 32-bit stack frames (`push ebp; mov ebp, esp; sub esp, ...`), register preservation (`esi`, `edi`, `ebx`), `rep movsd` memory copies, direct and indirect call dispatch.
- **Memory Operands:** `dword ptr [ecx + offset]`, `dword ptr [DAT_004974f4]`, `dword ptr [DAT_004a7f54]`, `dword ptr [DAT_00497528]`.

### Target `FUN_0040d590` (RVA: `0x0040d590`)
- **Subsystem Role:** Engine Context Initializer & VTable Binding
- **Decompiled Size:** 102 lines
- **Instruction Patterns:** x86 32-bit stack frames (`push ebp; mov ebp, esp; sub esp, ...`), register preservation (`esi`, `edi`, `ebx`), `rep movsd` memory copies, direct and indirect call dispatch.
- **Memory Operands:** `dword ptr [ecx + offset]`, `dword ptr [DAT_004974f4]`, `dword ptr [DAT_004a7f54]`, `dword ptr [DAT_00497528]`.

### Target `FUN_00411000` (RVA: `0x00411000`)
- **Subsystem Role:** FMOD Audio Subsystem Host Wrapper
- **Decompiled Size:** 45 lines
- **Instruction Patterns:** x86 32-bit stack frames (`push ebp; mov ebp, esp; sub esp, ...`), register preservation (`esi`, `edi`, `ebx`), `rep movsd` memory copies, direct and indirect call dispatch.
- **Memory Operands:** `dword ptr [ecx + offset]`, `dword ptr [DAT_004974f4]`, `dword ptr [DAT_004a7f54]`, `dword ptr [DAT_00497528]`.

### Target `FUN_004165c1` (RVA: `0x004165c1`)
- **Subsystem Role:** Win32 PE Entry Point & CRT Startup
- **Decompiled Size:** 15 lines
- **Instruction Patterns:** x86 32-bit stack frames (`push ebp; mov ebp, esp; sub esp, ...`), register preservation (`esi`, `edi`, `ebx`), `rep movsd` memory copies, direct and indirect call dispatch.
- **Memory Operands:** `dword ptr [ecx + offset]`, `dword ptr [DAT_004974f4]`, `dword ptr [DAT_004a7f54]`, `dword ptr [DAT_00497528]`.

