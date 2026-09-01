#!/usr/bin/env python3
"""
Alice Greenfingers - Master Reproduction & Verification Pipeline (Phase 14)
8 Rigorous Quality, Forensic & Symbolic Verification Gates.
"""

import os
import sys
import json
import hashlib
import subprocess
import datetime

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
TARGET_BINARY = os.path.join(PROJECT_ROOT, 'extracted', 'AliceGreenfingers_unpacked.exe')
EXPECTED_SHA256 = 'caf0c6f745f56579ac830f8a2ff8210042f40afdda479128521a398e19a2a8d1'

def run_reproduce():
    print("============================================================")
    print("ALICE GREENFINGERS - MASTER REPRODUCIBILITY PIPELINE (PHASE 14)")
    print("============================================================\n")

    results = []

    # Gate 1: Binary SHA-256 Integrity
    current_sha = hashlib.sha256(open(TARGET_BINARY, 'rb').read()).hexdigest()
    bin_ok = (current_sha == EXPECTED_SHA256)
    results.append({"gate": "Gate 1: Binary SHA-256 Integrity", "passed": bin_ok})
    print(f"[Gate 1] Binary Integrity: {'PASS' if bin_ok else 'FAIL'}")

    # Gate 2: Reconstructed Source Build
    build_res = subprocess.run(['cmake', '--build', 'build'], cwd=PROJECT_ROOT, capture_output=True, text=True)
    build_ok = (build_res.returncode == 0)
    results.append({"gate": "Gate 2: Reconstructed Source Build", "passed": build_ok})
    print(f"[Gate 2] Standalone Build: {'PASS' if build_ok else 'FAIL'}")

    # Gate 3: Distribution Packaging
    pkg_res = subprocess.run(['python', os.path.join(PROJECT_ROOT, 'tools', 'package', 'build_distribution.py')], capture_output=True, text=True)
    pkg_ok = (pkg_res.returncode == 0)
    results.append({"gate": "Gate 3: Distribution Packaging", "passed": pkg_ok})
    print(f"[Gate 3] Distribution Packaging: {'PASS' if pkg_ok else 'FAIL'}")

    # Gate 4: 55-Scenario Regression Suite
    diff_res = subprocess.run(['python', os.path.join(PROJECT_ROOT, 'analysis', 'phase12_portability_tests.py')], capture_output=True, text=True)
    diff_ok = (diff_res.returncode == 0 and "ALL 55 SCENARIOS PASSED" in diff_res.stdout)
    results.append({"gate": "Gate 4: 55-Scenario Master Regression Suite", "passed": diff_ok})
    print(f"[Gate 4] Regression Suite (55/55): {'PASS' if diff_ok else 'FAIL'}")

    # Gate 5: Consistency Audit
    audit_res = subprocess.run(['python', os.path.join(PROJECT_ROOT, 'analysis', 'phase12_consistency_audit.py')], capture_output=True, text=True)
    audit_ok = (audit_res.returncode == 0 and "12/12 CHECKS PASSED" in audit_res.stdout)
    results.append({"gate": "Gate 5: Consistency Audit", "passed": audit_ok})
    print(f"[Gate 5] Consistency Audit: {'PASS' if audit_ok else 'FAIL'}")

    # Gate 6: Phase 13 Differential Trace & Memory Audit
    trace_audit_res = subprocess.run(['python', os.path.join(PROJECT_ROOT, 'analysis', 'phase13', 'phase13_differential_audit.py')], capture_output=True, text=True)
    trace_audit_ok = (trace_audit_res.returncode == 0 and "12/12 DIFFERENTIAL GATES PASSED" in trace_audit_res.stdout)
    results.append({"gate": "Gate 6: Execution Trace Forensics Audit", "passed": trace_audit_ok})
    print(f"[Gate 6] Execution Trace Audit (12/12): {'PASS' if trace_audit_ok else 'FAIL'}")

    # Gate 7: Phase 14 Symbolic Execution & State-Space Audit
    sym_audit_file = os.path.join(PROJECT_ROOT, 'analysis', 'phase14', 'solver', 'solver_audit.json')
    with open(sym_audit_file, 'r', encoding='utf-8') as f: sym_audit = json.load(f)
    sym_ok = (sym_audit.get("model_replay_mismatches") == 0 and sym_audit.get("sat_results", 0) > 0)
    results.append({"gate": "Gate 7: Symbolic Execution & State-Space Audit", "passed": sym_ok})
    print(f"[Gate 7] Symbolic Execution Audit: {'PASS' if sym_ok else 'FAIL'}")

    # Gate 8: Post-Execution Read-Only Verification
    post_sha = hashlib.sha256(open(TARGET_BINARY, 'rb').read()).hexdigest()
    post_ok = (post_sha == EXPECTED_SHA256)
    results.append({"gate": "Gate 8: Post-Execution Read-Only Verification", "passed": post_ok})
    print(f"[Gate 8] Post-Execution Binary Check: {'PASS' if post_ok else 'FAIL'}")

    all_passed = all(r["passed"] for r in results)
    print(f"\nOVERALL REPRODUCIBILITY STATUS: {'PASS' if all_passed else 'FAIL'}\n")

if __name__ == '__main__':
    run_reproduce()
