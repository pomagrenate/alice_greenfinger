#!/usr/bin/env python3
"""
Alice Greenfingers - Differential Trace Correlation Engine (Phase 13)
Compares normalized original vs reconstructed event sequences.
"""
import os
import json

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
PHASE13_DIR = os.path.join(PROJECT_ROOT, 'analysis', 'phase13')
NORM_DIR = os.path.join(PHASE13_DIR, 'normalized')
CORR_DIR = os.path.join(PHASE13_DIR, 'correlations')

def correlate_scenario(sc_id):
    orig_path = os.path.join(NORM_DIR, f"norm_original_{sc_id}.json")
    recon_path = os.path.join(NORM_DIR, f"norm_reconstructed_{sc_id}.json")

    with open(orig_path, 'r', encoding='utf-8') as f: orig_data = json.load(f)
    with open(recon_path, 'r', encoding='utf-8') as f: recon_data = json.load(f)

    orig_events = orig_data.get("events", [])
    recon_events = recon_data.get("events", [])

    matched = 0
    total = max(len(orig_events), len(recon_events))
    event_diffs = []

    for i in range(total):
        o_ev = orig_events[i] if i < len(orig_events) else None
        r_ev = recon_events[i] if i < len(recon_events) else None

        if o_ev and r_ev:
            # Semantic equivalence check
            eq_type = (o_ev["event_type"] == r_ev["event_type"])
            eq_tick = (o_ev["sim_tick"] == r_ev["sim_tick"])
            eq_state = (o_ev["state_id"] == r_ev["state_id"])
            eq_opcode = (o_ev["opcode_id"] == r_ev["opcode_id"])
            eq_glob = (o_ev["global_address"] == r_ev["global_address"])
            eq_new_val = (o_ev["new_value"] == r_ev["new_value"])

            if eq_type and eq_tick and eq_state and eq_opcode and eq_glob and eq_new_val:
                status = "EXACT_MATCH"
                matched += 1
            elif eq_type and eq_state:
                status = "PARTIAL_MATCH"
                matched += 1
            else:
                status = "MISMATCH"
        else:
            status = "MISMATCH"

        event_diffs.append({
            "event_index": i + 1,
            "status": status,
            "original_event": o_ev,
            "reconstructed_event": r_ev
        })

    match_rate = (matched / total * 100.0) if total > 0 else 100.0
    verdict = "MATCH" if match_rate == 100.0 else ("PARTIAL_MATCH" if match_rate >= 80.0 else "MISMATCH")

    result = {
        "scenario_id": sc_id,
        "total_events": total,
        "matched_events": matched,
        "match_percentage": round(match_rate, 2),
        "verdict": verdict,
        "evidence_level": "E4 (Differential Correlation)",
        "event_comparisons": event_diffs
    }

    out_path = os.path.join(CORR_DIR, f"{sc_id}.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)

    return result

def main():
    os.makedirs(CORR_DIR, exist_ok=True)
    scenarios = [
        "startup", "title_menu", "farm_init", "seed_purchase", "sowing",
        "crop_growth", "harvest", "market_entry", "crop_sale", "day_transition",
        "save", "load"
    ]
    results = []
    for sc in scenarios:
        r = correlate_scenario(sc)
        results.append(r)
        print(f"Scenario [{sc}]: {r['verdict']} ({r['match_percentage']}%)")

if __name__ == '__main__':
    main()
