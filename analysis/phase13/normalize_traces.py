#!/usr/bin/env python3
"""
Alice Greenfingers - Trace Normalization Engine (Phase 13)
Filters non-deterministic host addresses, timestamps, and path separators.
"""
import os
import json

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
PHASE13_DIR = os.path.join(PROJECT_ROOT, 'analysis', 'phase13')
TRACES_DIR = os.path.join(PHASE13_DIR, 'traces')
NORM_DIR = os.path.join(PHASE13_DIR, 'normalized')

def normalize_file(src_path, dst_path):
    with open(src_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    norm_events = []
    for ev in data.get("events", []):
        norm_ev = {
            "event_id": ev.get("event_id"),
            "sim_tick": ev.get("sim_tick"),
            "event_type": ev.get("event_type"),
            "state_id": ev.get("state_id"),
            "opcode_id": ev.get("opcode_id"),
            "global_address": ev.get("global_address"),
            "previous_value": ev.get("previous_value"),
            "new_value": ev.get("new_value"),
            "resource_id": ev.get("resource_id").replace('\\', '/') if ev.get("resource_id") else None,
            "evidence_level": ev.get("evidence_level")
        }
        norm_events.append(norm_ev)

    out_data = {
        "scenario_id": data.get("scenario_id"),
        "origin": data.get("origin"),
        "normalized": True,
        "event_count": len(norm_events),
        "events": norm_events
    }
    with open(dst_path, 'w', encoding='utf-8') as f:
        json.dump(out_data, f, indent=2)

def main():
    os.makedirs(NORM_DIR, exist_ok=True)
    for fname in os.listdir(TRACES_DIR):
        if fname.endswith('.json'):
            src = os.path.join(TRACES_DIR, fname)
            dst = os.path.join(NORM_DIR, f"norm_{fname}")
            normalize_file(src, dst)
    print("Trace normalization complete.")

if __name__ == '__main__':
    main()
