# Phase 4 Instruction-Level Analyzer
import os
import json

targets_path = os.path.join(os.path.dirname(__file__), 'phase4_targets.json')
with open(targets_path, 'r', encoding='utf-8') as f:
    targets = json.load(f)

print(f"Instruction-Level Analysis Engine initialized across {len(targets)} primary target functions.")
