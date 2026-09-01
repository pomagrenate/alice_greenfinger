#!/usr/bin/env python3
"""
Alice Greenfingers - Unified Master Reproduction & Verification Pipeline (Phase 11)
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
PHASE11_DIR = os.path.join(PROJECT_ROOT, 'analysis', 'phase11')
NOTES_DIR = os.path.join(PROJECT_ROOT, 'notes')

def run_reproduce():
    print("============================================================")
    print("ALICE GREENFINGERS - MASTER REPRODUCIBILITY PIPELINE (PHASE 11)")
    print("============================================================\n")

    results = []

    # 1. Binary Integrity Check
    current_sha = hashlib.sha256(open(TARGET_BINARY, 'rb').read()).hexdigest()
    bin_ok = (current_sha == EXPECTED_SHA256)
    results.append({"step": "Binary SHA-256 Integrity", "passed": bin_ok})
    print(f"[01] Binary Integrity: {'PASS' if bin_ok else 'FAIL'}")

    # 2. Build Reconstructed Source
    build_res = subprocess.run(['cmake', '--build', 'build'], cwd=PROJECT_ROOT, capture_output=True, text=True)
    build_ok = (build_res.returncode == 0)
    results.append({"step": "Reconstructed Source Build", "passed": build_ok})
    print(f"[02] Standalone Build: {'PASS' if build_ok else 'FAIL'}")

    # 3. Packaging Distribution
    pkg_res = subprocess.run(['python', os.path.join(PROJECT_ROOT, 'tools', 'package', 'build_distribution.py')], capture_output=True, text=True)
    pkg_ok = (pkg_res.returncode == 0)
    results.append({"step": "Distribution Packaging", "passed": pkg_ok})
    print(f"[03] Distribution Packaging: {'PASS' if pkg_ok else 'FAIL'}")

    # 4. Differential Test Suite (50 Scenarios)
    diff_res = subprocess.run(['python', os.path.join(PROJECT_ROOT, 'analysis', 'phase11_behavioral_diff.py')], capture_output=True, text=True)
    diff_ok = (diff_res.returncode == 0 and "ALL 50 SCENARIOS PASSED" in diff_res.stdout)
    results.append({"step": "50-Scenario Master Differential Suite", "passed": diff_ok})
    print(f"[04] Differential Suite (50/50): {'PASS' if diff_ok else 'FAIL'}")

    # 5. Consistency Audit
    audit_res = subprocess.run(['python', os.path.join(PROJECT_ROOT, 'analysis', 'phase10_consistency_audit.py')], capture_output=True, text=True)
    audit_ok = (audit_res.returncode == 0 and "12/12 CHECKS PASSED" in audit_res.stdout)
    results.append({"step": "12/12 Consistency Audit", "passed": audit_ok})
    print(f"[05] Consistency Audit: {'PASS' if audit_ok else 'FAIL'}")

    # 6. Final Read-Only Verification
    post_sha = hashlib.sha256(open(TARGET_BINARY, 'rb').read()).hexdigest()
    post_ok = (post_sha == EXPECTED_SHA256)
    results.append({"step": "Final Binary Non-Modification", "passed": post_ok})
    print(f"[06] Post-Execution Binary Check: {'PASS' if post_ok else 'FAIL'}")

    all_passed = all(r["passed"] for r in results)
    print(f"\nOVERALL REPRODUCIBILITY STATUS: {'PASS' if all_passed else 'FAIL'}\n")

    repro_data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "status": "PASS" if all_passed else "FAIL",
        "results": results
    }
    with open(os.path.join(PHASE11_DIR, 'reproduction_result.json'), 'w', encoding='utf-8') as f:
        json.dump(repro_data, f, indent=2)

    with open(os.path.join(NOTES_DIR, 'PHASE_11_REPRODUCTION_RESULT.md'), 'w', encoding='utf-8') as f:
        f.write('# ALICE GREENFINGERS - PHASE 11 REPRODUCIBILITY RESULTS\n\n')
        f.write(f'*Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
        f.write(f'## REPRODUCIBILITY STATUS: **{"PASS" if all_passed else "FAIL"}**\n\n')
        f.write('| Step Description | Result |\n')
        f.write('| :--- | :---: |\n')
        for r in results:
            f.write(f'| {r["step"]} | **{"[PASS]" if r["passed"] else "[FAIL]"}** |\n')

if __name__ == '__main__':
    run_reproduce()
