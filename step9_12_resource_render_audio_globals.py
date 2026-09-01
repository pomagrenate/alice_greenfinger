import os
import datetime

notes_dir = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE\notes'

# 1. RESOURCE_SYSTEM_BLUEPRINT.md
res_blue_file = os.path.join(notes_dir, 'RESOURCE_SYSTEM_BLUEPRINT.md')
with open(res_blue_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - RESOURCE SYSTEM BLUEPRINT (STEP 9)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    f.write('## RESOURCE EXTRACTION PIPELINE\n\n')
    f.write('```\n')
    f.write('Graphics/*.gfx Archive\n')
    f.write('    ↓\n')
    f.write('FUN_004033c0 (Resource_PopCapGfxArchiveParser)\n')
    f.write('    ↓\n')
    f.write('Header Verification ("LBTC" / PopCap GFX Container)\n')
    f.write('    ↓\n')
    f.write('Memory Sprite Atlas Allocation\n')
    f.write('    ↓\n')
    f.write('Blitting Handle Pointer stored in DAT_00497528\n')
    f.write('```\n')

# 2. RENDERING_ARCHITECTURE.md
rend_arch_file = os.path.join(notes_dir, 'RENDERING_ARCHITECTURE.md')
with open(rend_arch_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - RENDERING ARCHITECTURE (STEP 10)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    f.write('## RENDERING SUBSYSTEM SPECIFICATION\n\n')
    f.write('- **Entry Point:** `FUN_004096a0` (Render_MainFrameLayerUpdate)\n')
    f.write('- **Surface Target:** DirectDraw Surface Backbuffer\n')
    f.write('- **Frame Rate:** 60 Hz Synchronized Loop\n')
    f.write('- **Render Layer Stack:**\n')
    f.write('  1. Background Terrain Layer (`TileSets/` blitter)\n')
    f.write('  2. Plant & Grid Object Layer (`Graphics/*.gfx` sprite atlas)\n')
    f.write('  3. GUI Overlay & Cursor Layer (`FUN_00404170` widget blitter)\n')

# 3. AUDIO_ARCHITECTURE.md
aud_arch_file = os.path.join(notes_dir, 'AUDIO_ARCHITECTURE.md')
with open(aud_arch_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - AUDIO ARCHITECTURE (STEP 11)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    f.write('## FMOD AUDIO INTEGRATION ARCHITECTURE\n\n')
    f.write('- **Wrapper Function:** `FUN_00411000` (FMOD Audio Subsystem Host)\n')
    f.write('- **Imported APIs:** `_FSOUND_Sample_Load@20`, `_FSOUND_PlaySound@8`, `_FSOUND_Close@0`\n')
    f.write('- **Audio Channels:** Sound Effects (SFX) & Background Music (BGM)\n')
    f.write('- **State Binding:** Triggered via Opcode events in `FUN_00404170`\n')

# 4. GLOBAL_STATE_ARCHITECTURE.md
gstate_arch_file = os.path.join(notes_dir, 'GLOBAL_STATE_ARCHITECTURE.md')
with open(gstate_arch_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - GLOBAL STATE ARCHITECTURE (STEP 12)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    f.write('## GLOBAL STATE BOUNDARY MODEL\n\n')
    f.write('| Global Variable Address | Access Type | Owning Subsystem | Functional Role | Confidence |\n')
    f.write('| --- | --- | --- | --- | --- |\n')
    f.write('| `DAT_004974f4` | Read / Write | `SUBSYS_EVENT_DISPATCH` | Active Game State Enum (0..4) | **[VERIFIED]** |\n')
    f.write('| `DAT_004a7f54` | Read / Write | `SUBSYS_FRAME_RENDER` | Frame Tick Counter | **[VERIFIED]** |\n')
    f.write('| `DAT_00497528` | Read Only | `SUBSYS_POP_PARSER` | Sprite Atlas Handle Pointer | **[VERIFIED]** |\n')

print('STEPS 9, 10, 11, 12 complete!')
