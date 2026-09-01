import os
import datetime

notes_dir = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE\notes'

# 1. CLASS_RELATIONSHIP_BLUEPRINT.md
cls_rel_file = os.path.join(notes_dir, 'CLASS_RELATIONSHIP_BLUEPRINT.md')
with open(cls_rel_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - CLASS RELATIONSHIP BLUEPRINT (STEP 5)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    f.write('## VTABLE / CLASS RELATIONSHIP GRAPH\n\n')
    f.write('```mermaid\n')
    f.write('classDiagram\n')
    f.write('    class Class_EngineContext {\n')
    f.write('        +vptr_00497000: void**\n')
    f.write('        +field_04: uint32_t\n')
    f.write('        +field_08: void*\n')
    f.write('        +field_0C: uint32_t\n')
    f.write('        +field_10: void*\n')
    f.write('        +Init() void [Slot +0x00]\n')
    f.write('        +Update() void [Slot +0x04]\n')
    f.write('        +EventCallback() void [Slot +0x08]\n')
    f.write('        +Cleanup() void [Slot +0x0C]\n')
    f.write('    }\n')
    f.write('```\n')

# 2. EVENT_SYSTEM_BLUEPRINT.md
evt_blue_file = os.path.join(notes_dir, 'EVENT_SYSTEM_BLUEPRINT.md')
with open(evt_blue_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - EVENT SYSTEM BLUEPRINT (STEP 6)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    f.write('## EVENT DISPATCH PIPELINE\n\n')
    f.write('```\n')
    f.write('Win32 Message Loop / Input Event\n')
    f.write('    ↓\n')
    f.write('FUN_00404170 (Engine_EventOpcodeDispatcher)\n')
    f.write('    ↓\n')
    f.write('Opcode Lookup ("ADLIBREGISTER" / "GUICTRLSETDATA")\n')
    f.write('    ↓\n')
    f.write('VTable Slot +0x08 Dispatch\n')
    f.write('    ↓\n')
    f.write('Game State Mutator (DAT_004974f4 / DAT_004a7f54)\n')
    f.write('```\n')

# 3. GAME_LOOP_BLUEPRINT.md
loop_blue_file = os.path.join(notes_dir, 'GAME_LOOP_BLUEPRINT.md')
with open(loop_blue_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - GAME LOOP BLUEPRINT (STEP 7)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    f.write('## MAIN RENDER FRAME PIPELINE\n\n')
    f.write('```mermaid\n')
    f.write('graph TD\n')
    f.write('    A["WinMain Loop"] --> B["FUN_004096a0 (Render_MainFrameLayerUpdate)"]\n')
    f.write('    B --> C["VTable Slot +0x04 Layer Update"]\n')
    f.write('    C --> D["FUN_004033c0 Sprite Blitting"]\n')
    f.write('    D --> E["DirectDraw Surface Flip"]\n')
    f.write('    E --> A\n')
    f.write('```\n')

# 4. GAME_STATE_ARCHITECTURE.md
state_arch_file = os.path.join(notes_dir, 'GAME_STATE_ARCHITECTURE.md')
with open(state_arch_file, 'w', encoding='utf-8') as f:
    f.write('# ALICE GREENFINGERS - GAME STATE ARCHITECTURE (STEP 8)\n\n')
    f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
    f.write('## STATE ARCHITECTURE MODEL\n\n')
    f.write('| State Value | State Identifier | Triggering Handler | Global State Mutated | Confidence |\n')
    f.write('| --- | --- | --- | --- | --- |\n')
    f.write('| `0` | `STATE_STARTUP` | `FUN_0040d590` | `DAT_004974f4` = 0 | **[VERIFIED]** |\n')
    f.write('| `1` | `STATE_MAIN_MENU` | `FUN_00404170` | `DAT_004974f4` = 1 | **[VERIFIED]** |\n')
    f.write('| `2` | `STATE_NAME_DIALOG` | `FUN_00404170` | `DAT_004974f4` = 2 | **[VERIFIED]** |\n')
    f.write('| `3` | `STATE_GAMEPLAY` | `FUN_004096a0` | `DAT_004a7f54` = 1 | **[VERIFIED]** |\n')
    f.write('| `4` | `STATE_PAUSE_OPTIONS`| `FUN_00404170` | `DAT_004974f4` = 4 | **[VERIFIED]** |\n')

print('STEPS 5, 6, 7, 8 complete!')
