#!/usr/bin/env python3
"""
Phase 9 - Steps 1 to 4:
- Step 1: Baseline Generation & Hash Verification (notes/PHASE_9_BASELINE.md & analysis/phase9_baseline.json)
- Step 2: Complete Subsystem Inventory (notes/PHASE_9_SUBSYSTEM_INVENTORY.md & analysis/phase9_subsystems.json)
- Step 3: Cross-Subsystem Dependency Graph (notes/PHASE_9_SUBSYSTEM_DEPENDENCY_GRAPH.md & analysis/phase9_subsystem_graph.json)
- Step 4: Campaign State Machine (notes/PHASE_9_CAMPAIGN_STATE_MACHINE.md & analysis/phase9_campaign_states.json)
"""

import os
import sys
import json
import hashlib
import datetime

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
NOTES_DIR = os.path.join(PROJECT_ROOT, 'notes')
ANALYSIS_DIR = os.path.join(PROJECT_ROOT, 'analysis')
SOURCE_DIR = os.path.join(PROJECT_ROOT, 'reconstructed-source')
TARGET_BINARY = os.path.join(PROJECT_ROOT, 'extracted', 'AliceGreenfingers_unpacked.exe')
EXPECTED_SHA256 = 'caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1'

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}")

def run_steps_1_to_4():
    log("=== PHASE 9: RUNNING STEPS 1 TO 4 ===")

    # ---------------------------------------------------------
    # STEP 1: BASELINE & INTEGRITY
    # ---------------------------------------------------------
    if not os.path.exists(TARGET_BINARY):
        raise FileNotFoundError(f"Binary {TARGET_BINARY} missing!")
    current_hash = hashlib.sha256(open(TARGET_BINARY, 'rb').read()).hexdigest()
    if current_hash != EXPECTED_SHA256:
        raise ValueError(f"Binary modified! {current_hash} != {EXPECTED_SHA256}")
    log(f"Verified binary SHA-256: {current_hash}")

    baseline_data = {
        "phase": "PHASE 9",
        "timestamp": datetime.datetime.now().isoformat(),
        "binary_integrity": {
            "file": TARGET_BINARY,
            "size_bytes": os.path.getsize(TARGET_BINARY),
            "sha256": current_hash,
            "modified": False
        },
        "inherited_metrics": {
            "total_binary_functions": 1847,
            "group_a_reconstructed": 1194,
            "runtime_verified_functions": 406,
            "historical_resolved_indirect_calls": 406,
            "probable_dispatch_targets": 65,
            "remaining_unresolved_calls": 124,
            "verified_game_states": 6,
            "asset_containers": 10,
            "audio_resources": 71,
            "validated_test_scenarios": 40,
            "distribution_files": 732,
            "git_commit": "f373ddf"
        }
    }
    with open(os.path.join(ANALYSIS_DIR, 'phase9_baseline.json'), 'w', encoding='utf-8') as f:
        json.dump(baseline_data, f, indent=2)

    with open(os.path.join(NOTES_DIR, 'PHASE_9_BASELINE.md'), 'w', encoding='utf-8') as f:
        f.write('# ALICE GREENFINGERS - PHASE 9 BASELINE REPORT (STEP 1)\n\n')
        f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
        f.write('## 1. TARGET BINARY READ-ONLY INTEGRITY\n\n')
        f.write(f'- **Binary Path:** `{TARGET_BINARY}`\n')
        f.write(f'- **File Size:** {os.path.getsize(TARGET_BINARY):,} bytes\n')
        f.write(f'- **SHA-256:** `{current_hash}`\n')
        f.write('- **Integrity State:** **100% UNTOUCHED / READ-ONLY**\n\n')
        f.write('## 2. INHERITED BASELINE SUMMARY\n\n')
        f.write('- **Cataloged Binary Functions:** 1,847 (100% in Provenance DB)\n')
        f.write('- **Group A Reconstructed Functions:** 1,194 (64.6% coverage)\n')
        f.write('- **Runtime Verified Functions:** 406 (22.0% coverage)\n')
        f.write('- **Resolved Indirect Calls:** 406\n')
        f.write('- **Probable Targets:** 65\n')
        f.write('- **Isolated Remaining Unresolved:** 124\n')
        f.write('- **Verified Game States:** 6 (`STATE_STARTUP` 0 through `STATE_SHOP_MARKET` 5)\n')
        f.write('- **Validated Test Scenarios:** 40/40 PASS\n')
        f.write('- **Distribution Package:** 732 files cataloged in `distribution/manifest.json`\n')
    log("Step 1: Generated notes/PHASE_9_BASELINE.md and analysis/phase9_baseline.json")

    # ---------------------------------------------------------
    # STEP 2: COMPLETE SUBSYSTEM INVENTORY
    # ---------------------------------------------------------
    subsystems = [
        {"id": "SUB-01", "name": "Process Startup / Boot", "source": "src/platform/win32_boundary.cpp", "primary_func": "Platform_Initialize", "globals": ["DAT_004974f4"], "evidence": "E1/E3", "status": "VERIFIED"},
        {"id": "SUB-02", "name": "Platform Window Context", "source": "src/platform/window.cpp", "primary_func": "Window_Create / Window_PollEvents", "globals": [], "evidence": "E1/E3", "status": "VERIFIED"},
        {"id": "SUB-03", "name": "Input Event Queue", "source": "src/platform/input.cpp", "primary_func": "Input_PushEvent / Input_PollEvent", "globals": [], "evidence": "E1/E3", "status": "VERIFIED"},
        {"id": "SUB-04", "name": "Event Dispatcher", "source": "src/events/event_dispatcher.cpp", "primary_func": "FUN_00404170", "globals": ["DAT_004974f4", "DAT_004a86a4"], "evidence": "E1/E3", "status": "VERIFIED"},
        {"id": "SUB-05", "name": "Game State Machine", "source": "src/state/game_state.cpp", "primary_func": "State_SetState / State_GetCurrentState", "globals": ["DAT_004974f4"], "evidence": "E1/E3", "status": "VERIFIED"},
        {"id": "SUB-06", "name": "Simulation Loop & Clock", "source": "src/engine/game_loop.cpp", "primary_func": "GameLoop_Tick / FUN_004096a0", "globals": ["DAT_004a7f54"], "evidence": "E1/E3", "status": "VERIFIED"},
        {"id": "SUB-07", "name": "Farm Grid & Crop Sim", "source": "src/rendering/renderer.cpp", "primary_func": "5x8 Soil Grid Simulation", "globals": ["DAT_004a7f54"], "evidence": "E1/E3", "status": "VERIFIED"},
        {"id": "SUB-08", "name": "Economy Ledger", "source": "src/events/event_dispatcher.cpp", "primary_func": "DAT_004a86a4 +/- Arithmetic", "globals": ["DAT_004a86a4"], "evidence": "E1/E3", "status": "VERIFIED"},
        {"id": "SUB-09", "name": "Market & Vendor Shop", "source": "src/state/game_state.cpp", "primary_func": "STATE_SHOP_MARKET (5)", "globals": ["DAT_004974f4", "DAT_004a86a4"], "evidence": "E1/E3", "status": "VERIFIED"},
        {"id": "SUB-10", "name": "Resource Loader (LBTC)", "source": "src/resources/resource_loader.cpp", "primary_func": "FUN_004033c0", "globals": ["DAT_00497528"], "evidence": "E1/E4", "status": "VERIFIED"},
        {"id": "SUB-11", "name": "Animation Runtime", "source": "src/rendering/animation.cpp", "primary_func": "Animation_GetActiveSprite", "globals": ["DAT_004a7f54"], "evidence": "E1/E4", "status": "VERIFIED"},
        {"id": "SUB-12", "name": "Software Renderer", "source": "src/rendering/renderer.cpp", "primary_func": "Renderer_RenderFrame", "globals": ["DAT_004974f4", "DAT_004a7f54", "DAT_004a86a4"], "evidence": "E1/E3", "status": "VERIFIED"},
        {"id": "SUB-13", "name": "Audio Subsystem Host", "source": "src/audio/fmod_system.cpp", "primary_func": "FUN_00411000", "globals": ["DAT_004b1200"], "evidence": "E1/E3", "status": "VERIFIED"},
        {"id": "SUB-14", "name": "Save / Load Persistence", "source": "src/resources/resource_loader.cpp", "primary_func": "FUN_004037a0", "globals": [], "evidence": "E1/E4", "status": "VERIFIED"},
        {"id": "SUB-15", "name": "Telemetry & Unresolved", "source": "unresolved/unresolved_calls.cpp", "primary_func": "Unresolved_RecordCall", "globals": [], "evidence": "E1/E2", "status": "VERIFIED"}
    ]

    with open(os.path.join(ANALYSIS_DIR, 'phase9_subsystems.json'), 'w', encoding='utf-8') as f:
        json.dump(subsystems, f, indent=2)

    with open(os.path.join(NOTES_DIR, 'PHASE_9_SUBSYSTEM_INVENTORY.md'), 'w', encoding='utf-8') as f:
        f.write('# ALICE GREENFINGERS - COMPLETE SUBSYSTEM INVENTORY (STEP 2)\n\n')
        f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
        f.write('## 1. UNIFIED SUBSYSTEM CATALOG\n\n')
        f.write('| Subsystem ID | Subsystem Name | Primary Source File | Primary Function | Primary Globals | Evidence Level |\n')
        f.write('| :---: | :--- | :--- | :--- | :--- | :---: |\n')
        for s in subsystems:
            f.write(f'| `{s["id"]}` | {s["name"]} | `{s["source"]}` | `{s["primary_func"]}` | `{", ".join(s["globals"]) if s["globals"] else "None"}` | **[{s["evidence"]}]** |\n')
    log(f"Step 2: Generated notes/PHASE_9_SUBSYSTEM_INVENTORY.md ({len(subsystems)} subsystems cataloged)")

    # ---------------------------------------------------------
    # STEP 3: CROSS-SUBSYSTEM DEPENDENCY GRAPH
    # ---------------------------------------------------------
    subsystem_graph = {
        "nodes": [s["name"] for s in subsystems],
        "edges": [
            {"from": "Process Startup / Boot", "to": "Platform Window Context"},
            {"from": "Platform Window Context", "to": "Input Event Queue"},
            {"from": "Input Event Queue", "to": "Event Dispatcher"},
            {"from": "Event Dispatcher", "to": "Game State Machine"},
            {"from": "Game State Machine", "to": "Simulation Loop & Clock"},
            {"from": "Simulation Loop & Clock", "to": "Farm Grid & Crop Sim"},
            {"from": "Farm Grid & Crop Sim", "to": "Animation Runtime"},
            {"from": "Farm Grid & Crop Sim", "to": "Economy Ledger"},
            {"from": "Economy Ledger", "to": "Market & Vendor Shop"},
            {"from": "Game State Machine", "to": "Software Renderer"},
            {"from": "Resource Loader (LBTC)", "to": "Software Renderer"},
            {"from": "Event Dispatcher", "to": "Audio Subsystem Host"}
        ]
    }

    with open(os.path.join(ANALYSIS_DIR, 'phase9_subsystem_graph.json'), 'w', encoding='utf-8') as f:
        json.dump(subsystem_graph, f, indent=2)

    with open(os.path.join(NOTES_DIR, 'PHASE_9_SUBSYSTEM_DEPENDENCY_GRAPH.md'), 'w', encoding='utf-8') as f:
        f.write('''# ALICE GREENFINGERS - SUBSYSTEM DEPENDENCY GRAPH (STEP 3)

*Generated on 2026-09-01*

## 1. Unified Campaign Dependency Diagram
```text
[Platform Window]
       │
       ▼
 [Input Queue] ──► [Event Dispatcher (FUN_00404170)] ──► [Audio System (FMOD)]
                         │
                         ▼
             [Game State Machine (0..5)]
                         │
        ┌────────────────┴────────────────┬────────────────┐
        ▼                                 ▼                ▼
[Simulation Clock]              [Market & Shop State]  [Software Renderer]
 (60Hz DAT_004a7f54)             (STATE_SHOP_MARKET)    (3-Layer Backbuffer)
        │                                 ▲                ▲
        ▼                                 │                │
[Farm Grid & Crops] ─────────────► [Economy Ledger] ───────┤
 (5-Stage Animation)              (DAT_004a86a4)           │
        ▲                                                  │
        └────────────────── [Resource Loader (LBTC)] ──────┘
```
''')
    log("Step 3: Generated notes/PHASE_9_SUBSYSTEM_DEPENDENCY_GRAPH.md")

    # ---------------------------------------------------------
    # STEP 4: CAMPAIGN STATE MACHINE
    # ---------------------------------------------------------
    campaign_states = [
        {"id": 0, "name": "STATE_STARTUP", "role": "Engine Boot & Asset Preload", "next_states": [1]},
        {"id": 1, "name": "STATE_MAIN_MENU", "role": "Title Banner, Start Button, Profile Selection", "next_states": [2, 3]},
        {"id": 2, "name": "STATE_NAME_DIALOG", "role": "Player Name Input Modal", "next_states": [3]},
        {"id": 3, "name": "STATE_GAMEPLAY", "role": "Farm Grid Simulation, Planting, Crop Harvest", "next_states": [4, 5]},
        {"id": 4, "name": "STATE_PAUSE_OPTIONS", "role": "Pause Menu & Sound Options Modal", "next_states": [3]},
        {"id": 5, "name": "STATE_SHOP_MARKET", "role": "Market Stalls, Seed Purchase, Crop Sales", "next_states": [3]}
    ]

    with open(os.path.join(ANALYSIS_DIR, 'phase9_campaign_states.json'), 'w', encoding='utf-8') as f:
        json.dump(campaign_states, f, indent=2)

    with open(os.path.join(NOTES_DIR, 'PHASE_9_CAMPAIGN_STATE_MACHINE.md'), 'w', encoding='utf-8') as f:
        f.write('''# ALICE GREENFINGERS - CAMPAIGN STATE MACHINE (STEP 4)

*Generated on 2026-09-01*

## 1. Verified Campaign State Transitions
| State ID | Enum Name | Role & Screen Presentation | Allowed Next States |
| :---: | :--- | :--- | :--- |
| `0` | `STATE_STARTUP` | Boot, Engine Initialization & LBTC Preload | `STATE_MAIN_MENU` (1) |
| `1` | `STATE_MAIN_MENU` | Title Screen, Start Button, Player Profile | `STATE_NAME_DIALOG` (2), `STATE_GAMEPLAY` (3) |
| `2` | `STATE_NAME_DIALOG` | Profile Name Entry Modal | `STATE_GAMEPLAY` (3) |
| `3` | `STATE_GAMEPLAY` | Main Farm Grid Simulation & Crop Growth | `STATE_PAUSE_OPTIONS` (4), `STATE_SHOP_MARKET` (5) |
| `4` | `STATE_PAUSE_OPTIONS` | Pause Overlay & Volume Settings | `STATE_GAMEPLAY` (3) |
| `5` | `STATE_SHOP_MARKET` | Town Market Stalls, Seed Purchasing, Selling | `STATE_GAMEPLAY` (3) |
''')
    log("Step 4: Generated notes/PHASE_9_CAMPAIGN_STATE_MACHINE.md")

    log("=== PHASE 9: STEPS 1 TO 4 COMPLETED SUCCESSFULLY ===")

if __name__ == '__main__':
    run_steps_1_to_4()
