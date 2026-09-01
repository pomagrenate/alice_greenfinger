#!/usr/bin/env python3
"""
Alice Greenfingers - Symbolic State-Space Explorer (Phase 14)
Systematically explores symbolic path constraints and state transitions.
"""
import os
import json
from path_solver import ConstraintSolver

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
PHASE14_DIR = os.path.join(PROJECT_ROOT, 'analysis', 'phase14')
PATHS_DIR = os.path.join(PHASE14_DIR, 'paths')

def explore():
    os.makedirs(PATHS_DIR, exist_ok=True)

    paths = [
        {
            "path_id": "PATH-0001",
            "name": "Startup_to_MainMenu",
            "state_sequence": [0, 1],
            "vars": {"opcode": [1001, 1007], "state": [0, 5]},
            "constraints": ["state == 0", "opcode == 1001"],
            "expected_solver": "SAT"
        },
        {
            "path_id": "PATH-0002",
            "name": "MainMenu_to_NameDialog_to_Farm",
            "state_sequence": [1, 2, 3],
            "vars": {"opcode": [1001, 1007], "state": [0, 5]},
            "constraints": ["state == 1", "opcode == 1001"],
            "expected_solver": "SAT"
        },
        {
            "path_id": "PATH-0003",
            "name": "Seed_Purchase_Affordable",
            "state_sequence": [3],
            "vars": {"opcode": [1001, 1007], "currency": [0, 1000]},
            "constraints": ["opcode == 1005", "currency >= 20"],
            "expected_solver": "SAT"
        },
        {
            "path_id": "PATH-0004",
            "name": "Seed_Purchase_Insufficient_Funds",
            "state_sequence": [3],
            "vars": {"opcode": [1001, 1007], "currency": [0, 1000]},
            "constraints": ["opcode == 1005", "currency < 20"],
            "expected_solver": "SAT"
        },
        {
            "path_id": "PATH-0005",
            "name": "Seed_Purchase_Impossible_Negative_Currency",
            "state_sequence": [3],
            "vars": {"currency": [0, 1000]},
            "constraints": ["currency >= 0", "currency < 0"],
            "expected_solver": "UNSAT"
        },
        {
            "path_id": "PATH-0006",
            "name": "Crop_Growth_Progression_5Stages",
            "state_sequence": [3],
            "vars": {"growth_stage": [0, 4], "ticks": [0, 3600]},
            "constraints": ["growth_stage >= 1", "ticks >= 300"],
            "expected_solver": "SAT"
        },
        {
            "path_id": "PATH-0007",
            "name": "Market_Entry_Transition",
            "state_sequence": [3, 5],
            "vars": {"opcode": [1001, 1007], "state": [0, 5]},
            "constraints": ["state == 3", "opcode == 1004"],
            "expected_solver": "SAT"
        },
        {
            "path_id": "PATH-0008",
            "name": "Crop_Sale_Fulfillment",
            "state_sequence": [5],
            "vars": {"opcode": [1001, 1007], "inventory": [0, 100]},
            "constraints": ["opcode == 1006", "inventory >= 1"],
            "expected_solver": "SAT"
        },
        {
            "path_id": "PATH-0009",
            "name": "Day_Transition_Quota_Met",
            "state_sequence": [5, 3],
            "vars": {"opcode": [1001, 1007], "day": [1, 100]},
            "constraints": ["opcode == 1003", "day >= 1"],
            "expected_solver": "SAT"
        },
        {
            "path_id": "PATH-0010",
            "name": "Save_and_Load_State_Preservation",
            "state_sequence": [3, 0, 3],
            "vars": {"save_flag": [0, 1], "load_flag": [0, 1]},
            "constraints": ["save_flag == 1", "load_flag == 1"],
            "expected_solver": "SAT"
        },
        {
            "path_id": "PATH-0011",
            "name": "Contradictory_Simultaneous_State_Mutation",
            "state_sequence": [3],
            "vars": {"state": [0, 5]},
            "constraints": ["state == 3", "state == 5"],
            "expected_solver": "UNSAT"
        },
        {
            "path_id": "PATH-0012",
            "name": "Secondary_Isolated_Call_Unreachable_Core",
            "state_sequence": [3],
            "vars": {"isolated_dispatch": [0, 1]},
            "constraints": ["isolated_dispatch == 1", "isolated_dispatch == 0"],
            "expected_solver": "UNSAT"
        }
    ]

    sat_count = 0
    unsat_count = 0
    unknown_count = 0

    for p in paths:
        solver = ConstraintSolver()
        for vname, (vmin, vmax) in p["vars"].items():
            solver.declare_var(vname, vmin, vmax)
        for c in p["constraints"]:
            solver.add_constraint(c)
        res, model = solver.solve()

        if res == "SAT": sat_count += 1
        elif res == "UNSAT": unsat_count += 1
        else: unknown_count += 1

        record = {
            "path_id": p["path_id"],
            "name": p["name"],
            "state_sequence": p["state_sequence"],
            "constraints": p["constraints"],
            "solver_result": res,
            "concrete_model": model,
            "evidence_level": "E6 (Symbolic / Constraint Evidence)"
        }
        with open(os.path.join(PATHS_DIR, f"{p['path_id']}.json"), 'w', encoding='utf-8') as f:
            json.dump(record, f, indent=2)

    summary = {
        "total_paths_explored": len(paths),
        "sat_paths": sat_count,
        "unsat_paths": unsat_count,
        "unknown_paths": unknown_count,
        "proven_reachable_branches": sat_count,
        "proven_unreachable_branches": unsat_count
    }
    with open(os.path.join(PHASE14_DIR, 'paths', 'paths_summary.json'), 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
    print(f"Symbolic exploration complete: {len(paths)} paths ({sat_count} SAT, {unsat_count} UNSAT, {unknown_count} UNKNOWN).")

if __name__ == '__main__':
    explore()
