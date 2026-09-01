#!/usr/bin/env python3
"""
Alice Greenfingers - Universal Master Reproduction & Verification Pipeline (Phase 12)
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
    print("ALICE GREENFINGERS - MASTER REPRODUCIBILITY PIPELINE (PHASE 12)")
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

    # 4. Master 55-Scenario Differential & Portability Suite
    diff_res = subprocess.run(['python', os.path.join(PROJECT_ROOT, 'analysis', 'phase12_portability_tests.py')], capture_output=True, text=True)
    diff_ok = (diff_res.returncode == 0 and "ALL 55 SCENARIOS PASSED" in diff_res.stdout)
    results.append({"step": "55-Scenario Master Test Suite", "passed": diff_ok})
    print(f"[04] Differential & Portability Suite (55/55): {'PASS' if diff_ok else 'FAIL'}")

    # 5. Consistency Audit
    audit_res = subprocess.run(['python', os.path.join(PROJECT_ROOT, 'analysis', 'phase12_consistency_audit.py')], capture_output=True, text=True)
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

if __name__ == '__main__':
    run_reproduce()
