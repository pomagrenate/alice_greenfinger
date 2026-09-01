#!/usr/bin/env python3
"""
Phase 13 - Steps 1 to 4:
- Step 1: Baseline Generation & Hash Verification (notes/PHASE_13_BASELINE.md & analysis/phase13_baseline.json)
- Step 2: Execution Trace Infrastructure Setup (analysis/phase13/ subdirectories)
- Step 3: Execution Event Schema Definition (analysis/phase13/trace_schema.json)
- Step 4: Trace Schema Documentation (analysis/phase13/TRACE_SCHEMA.md)
"""

import os
import sys
import json
import hashlib
import datetime

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
NOTES_DIR = os.path.join(PROJECT_ROOT, 'notes')
ANALYSIS_DIR = os.path.join(PROJECT_ROOT, 'analysis')
PHASE13_DIR = os.path.join(ANALYSIS_DIR, 'phase13')
TARGET_BINARY = os.path.join(PROJECT_ROOT, 'extracted', 'AliceGreenfingers_unpacked.exe')
EXPECTED_SHA256 = 'caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1'

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}")

def run_steps_1_to_4():
    log("=== PHASE 13: RUNNING STEPS 1 TO 4 ===")

    # ---------------------------------------------------------
    # STEP 1: BASELINE & INTEGRITY
    # ---------------------------------------------------------
    if not os.path.exists(TARGET_BINARY):
        raise FileNotFoundError(f"Binary {TARGET_BINARY} missing!")
    current_hash = hashlib.sha256(open(TARGET_BINARY, 'rb').read()).hexdigest()
    if current_hash != EXPECTED_SHA256:
        raise ValueError(f"Binary modified! {current_hash} != {EXPECTED_SHA256}")
    log(f"Verified target binary SHA-256: {current_hash}")

    baseline_data = {
        "phase": "PHASE 13 (EXECUTION TRACE FORENSICS & BINARY-RUNTIME DIFFERENTIAL VALIDATION)",
        "timestamp": datetime.datetime.now().isoformat(),
        "binary_integrity": {
            "file": TARGET_BINARY,
            "size_bytes": os.path.getsize(TARGET_BINARY),
            "sha256": current_hash,
            "modified_bytes": 0,
            "read_only": True
        },
        "inherited_metrics": {
            "total_binary_functions": 1847,
            "group_a_reconstructed": 1194,
            "runtime_verified_functions": 406,
            "resolved_indirect_calls": 406,
            "probable_dispatch_targets": 65,
            "isolated_unresolved_calls": 124,
            "recovered_static_globals": 175,
            "verified_game_states": 6,
            "popcap_lbtc_containers": 10,
            "graphics_atlases": 15,
            "audio_resources": 71,
            "validated_test_scenarios": 55,
            "platform_backends": 2,
            "distribution_files": 732,
            "git_commit": "ed8d875"
        },
        "phase_13_mission": "Establish execution-level forensic equivalence via deterministic trace capture, trace normalization, differential correlation, and semantic memory state differentials."
    }

    with open(os.path.join(ANALYSIS_DIR, 'phase13_baseline.json'), 'w', encoding='utf-8') as f:
        json.dump(baseline_data, f, indent=2)

    with open(os.path.join(NOTES_DIR, 'PHASE_13_BASELINE.md'), 'w', encoding='utf-8') as f:
        f.write('# ALICE GREENFINGERS - PHASE 13 BASELINE & INTEGRITY REPORT (STEP 1)\n\n')
        f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
        f.write('## 1. TARGET BINARY READ-ONLY INTEGRITY\n\n')
        f.write(f'- **Binary Path:** `{TARGET_BINARY}`\n')
        f.write(f'- **File Size:** {os.path.getsize(TARGET_BINARY):,} bytes\n')
        f.write(f'- **SHA-256:** `{current_hash}`\n')
        f.write('- **Modified Bytes:** **0 bytes (100% Read-Only)**\n\n')
        f.write('## 2. INHERITED FORENSIC BASELINE\n\n')
        f.write('| Metric Item | Baseline Count | Target Status |\n')
        f.write('| --- | ---: | :--- |\n')
        f.write('| **Total Cataloged Functions** | 1,847 | Preserved in Database |\n')
        f.write('| **Group A Reconstructed** | 1,194 | Maintained in Reconstructed Source |\n')
        f.write('| **Runtime Verified Functions** | 406 | 22.0% Execution Coverage |\n')
        f.write('| **Resolved Indirect Calls** | 406 | Target Provenance Verified |\n')
        f.write('| **Isolated Unresolved Calls** | 124 | Maintained behind Telemetry Stubs |\n')
        f.write('| **Validated Test Scenarios** | 55 | 55/55 PASS (100% Equivalence) |\n')
        f.write('| **Platform Backends** | 2 | Win32/GDI Reference + SDL2 Portable |\n')
    log("Step 1: Generated notes/PHASE_13_BASELINE.md and analysis/phase13_baseline.json")

    # ---------------------------------------------------------
    # STEP 2: DIRECTORY INFRASTRUCTURE
    # ---------------------------------------------------------
    subdirs = ['traces', 'normalized', 'correlations', 'memory', 'experiments', 'reports', 'manifests']
    for sd in subdirs:
        os.makedirs(os.path.join(PHASE13_DIR, sd), exist_ok=True)
    log(f"Step 2: Initialized execution trace infrastructure in analysis/phase13/ ({len(subdirs)} subdirectories)")

    # ---------------------------------------------------------
    # STEP 3: TRACE SCHEMA DEFINITION
    # ---------------------------------------------------------
    trace_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "AliceGreenfingers_ExecutionEvent",
        "type": "object",
        "required": ["event_id", "sim_tick", "event_type", "state_id"],
        "properties": {
            "event_id": {"type": "integer", "description": "Monotonically increasing sequence number within scenario"},
            "sim_tick": {"type": "integer", "description": "Deterministic 60 Hz simulation frame counter (DAT_004a7f54)"},
            "timestamp_ms": {"type": ["integer", "null"], "description": "Normalized timestamp in milliseconds"},
            "rva": {"type": ["string", "null"], "description": "Original binary RVA where observable (e.g. 0x00404170)"},
            "function_symbol": {"type": ["string", "null"], "description": "Recovered function identifier"},
            "event_type": {
                "type": "string",
                "enum": [
                    "STATE_TRANSITION",
                    "OPCODE_DISPATCH",
                    "GLOBAL_MUTATION",
                    "INPUT_EVENT",
                    "RESOURCE_ACCESS",
                    "AUDIO_EVENT",
                    "PERSISTENCE_EVENT",
                    "RENDER_SNAPSHOT"
                ]
            },
            "state_id": {"type": "integer", "minimum": 0, "maximum": 5, "description": "Active game state (0..5)"},
            "opcode_id": {"type": ["integer", "null"], "description": "Opcode event constant (1001..1007)"},
            "global_address": {"type": ["string", "null"], "description": "Semantic global symbol or address (e.g. DAT_004a86a4)"},
            "previous_value": {"type": ["integer", "string", "null"], "description": "Value prior to mutation"},
            "new_value": {"type": ["integer", "string", "null"], "description": "Value after mutation"},
            "resource_id": {"type": ["string", "null"], "description": "Asset container or atlas identifier"},
            "evidence_level": {
                "type": "string",
                "enum": ["E1", "E2", "E3", "E4", "E5"],
                "description": "Formal project evidence level"
            }
        }
    }
    with open(os.path.join(PHASE13_DIR, 'trace_schema.json'), 'w', encoding='utf-8') as f:
        json.dump(trace_schema, f, indent=2)
    log("Step 3: Created analysis/phase13/trace_schema.json")

    # ---------------------------------------------------------
    # STEP 4: TRACE SCHEMA DOCUMENTATION
    # ---------------------------------------------------------
    with open(os.path.join(PHASE13_DIR, 'TRACE_SCHEMA.md'), 'w', encoding='utf-8') as f:
        f.write('''# ALICE GREENFINGERS - EXECUTION TRACE SCHEMA SPECIFICATION (PHASE 13)

*Generated on 2026-09-01*

## 1. Schema Field Definitions
| Field Name | Type | Description | Mandatory |
| :--- | :--- | :--- | :---: |
| `event_id` | `integer` | Sequence index within the captured execution trace | **YES** |
| `sim_tick` | `integer` | Value of 60 Hz frame counter (`DAT_004a7f54`) | **YES** |
| `event_type` | `string` | Classification (`STATE_TRANSITION`, `OPCODE_DISPATCH`, etc.) | **YES** |
| `state_id` | `integer` | Verified active game state (`0` to `5`) | **YES** |
| `rva` | `string` | Original PE relative virtual address (e.g., `0x00404170`) | *Optional* |
| `function_symbol`| `string` | Recovered symbolic name (e.g., `FUN_00404170`) | *Optional* |
| `opcode_id` | `integer` | Script/event opcode (`1001` Start, `1004` Market, etc.) | *Optional* |
| `global_address` | `string` | Global variable symbol (e.g., `DAT_004a86a4`) | *Optional* |
| `previous_value` | `any` | Value prior to state or memory mutation | *Optional* |
| `new_value` | `any` | Value following state or memory mutation | *Optional* |
| `resource_id` | `string` | Asset container or sprite identifier | *Optional* |
| `evidence_level` | `string` | `E1` (Static), `E2` (Reconstruction), `E3` (Runtime), `E4` (Differential), `E5` (Reproducible Experiment) | **YES** |
''')
    log("Step 4: Generated analysis/phase13/TRACE_SCHEMA.md")

    log("=== PHASE 13: STEPS 1 TO 4 COMPLETED SUCCESSFULLY ===")

if __name__ == '__main__':
    run_steps_1_to_4()
