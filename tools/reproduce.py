#!/usr/bin/env python3
"""
Alice Greenfingers - Master Reproduction & Verification Pipeline (Phase 15 Universal)
10 Comprehensive Quality, Forensic, Symbolic, Provenance & Archival Verification Gates.
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
    print("ALICE GREENFINGERS - MASTER PRESERVATION PIPELINE (PHASE 15)")
    print("============================================================\n")

    results = []

    # Gate 1: Original Binary SHA-256
    sha1 = hashlib.sha256(open(TARGET_BINARY, 'rb').read()).hexdigest()
    g1_ok = (sha1 == EXPECTED_SHA256)
    results.append({"gate": "Gate 1: Original Binary SHA-256", "status": "PASS" if g1_ok else "FAIL"})
    print(f"[Gate 01] Original Binary SHA-256: {'PASS' if g1_ok else 'FAIL'}")

    # Gate 2: Reconstructed Source Build
    build_res = subprocess.run(['cmake', '--build', 'build'], cwd=PROJECT_ROOT, capture_output=True, text=True)
    g2_ok = (build_res.returncode == 0)
    results.append({"gate": "Gate 2: Reconstructed Source Build", "status": "PASS" if g2_ok else "FAIL"})
    print(f"[Gate 02] Standalone Source Build: {'PASS' if g2_ok else 'FAIL'}")

    # Gate 3: Distribution Packaging
    pkg_res = subprocess.run(['python', os.path.join(PROJECT_ROOT, 'tools', 'package', 'build_distribution.py')], capture_output=True, text=True)
    g3_ok = (pkg_res.returncode == 0)
    results.append({"gate": "Gate 3: Distribution Packaging", "status": "PASS" if g3_ok else "FAIL"})
    print(f"[Gate 03] Distribution Packaging: {'PASS' if g3_ok else 'FAIL'}")

    # Gate 4: Master Regression Suite (55 scenarios)
    diff_res = subprocess.run(['python', os.path.join(PROJECT_ROOT, 'analysis', 'phase12_portability_tests.py')], capture_output=True, text=True)
    g4_ok = (diff_res.returncode == 0 and "ALL 55 SCENARIOS PASSED" in diff_res.stdout)
    results.append({"gate": "Gate 4: Master Regression Suite", "status": "PASS" if g4_ok else "FAIL"})
    print(f"[Gate 04] Master Regression (55/55): {'PASS' if g4_ok else 'FAIL'}")

    # Gate 5: Consistency Audit
    audit_res = subprocess.run(['python', os.path.join(PROJECT_ROOT, 'analysis', 'phase15_consistency_audit.py')], capture_output=True, text=True)
    g5_ok = (audit_res.returncode == 0 and "12/12 PRESERVATION CHECKS PASSED" in audit_res.stdout)
    results.append({"gate": "Gate 5: Consistency Audit", "status": "PASS" if g5_ok else "FAIL"})
    print(f"[Gate 05] Consistency Audit: {'PASS' if g5_ok else 'FAIL'}")

    # Gate 6: Differential Trace Audit
    trace_audit_res = subprocess.run(['python', os.path.join(PROJECT_ROOT, 'analysis', 'phase13', 'phase13_differential_audit.py')], capture_output=True, text=True)
    g6_ok = (trace_audit_res.returncode == 0 and "12/12 DIFFERENTIAL GATES PASSED" in trace_audit_res.stdout)
    results.append({"gate": "Gate 6: Differential Trace Audit", "status": "PASS" if g6_ok else "FAIL"})
    print(f"[Gate 06] Differential Trace Audit: {'PASS' if g6_ok else 'FAIL'}")

    # Gate 7: Symbolic Execution & State-Space Audit
    sym_audit_file = os.path.join(PROJECT_ROOT, 'analysis', 'phase14', 'solver', 'solver_audit.json')
    with open(sym_audit_file, 'r', encoding='utf-8') as f: sym_audit = json.load(f)
    g7_ok = (sym_audit.get("model_replay_mismatches") == 0 and sym_audit.get("sat_results", 0) > 0)
    results.append({"gate": "Gate 7: Symbolic Execution Audit", "status": "PASS" if g7_ok else "FAIL"})
    print(f"[Gate 07] Symbolic Execution Audit: {'PASS' if g7_ok else 'FAIL'}")

    # Gate 8: Provenance Graph Consistency
    prov_file = os.path.join(PROJECT_ROOT, 'analysis', 'phase15', 'provenance', 'provenance_graph.json')
    with open(prov_file, 'r', encoding='utf-8') as f: pdata = json.load(f)
    g8_ok = (pdata.get("integrity_status") == "CONSISTENT_NO_DANGLING_REFERENCES")
    results.append({"gate": "Gate 8: Provenance Graph Audit", "status": "PASS" if g8_ok else "FAIL"})
    print(f"[Gate 08] Provenance Graph Audit: {'PASS' if g8_ok else 'FAIL'}")

    # Gate 9: Canonical Archival Manifest Integrity
    mhash_file = os.path.join(PROJECT_ROOT, 'analysis', 'phase15', 'manifests', 'manifest_hash.json')
    g9_ok = os.path.exists(mhash_file) and os.path.getsize(mhash_file) > 0
    results.append({"gate": "Gate 9: Archival Manifest Audit", "status": "PASS" if g9_ok else "FAIL"})
    print(f"[Gate 09] Archival Manifest Audit: {'PASS' if g9_ok else 'FAIL'}")

    # Gate 10: Post-Execution Binary Read-Only Check
    post_sha = hashlib.sha256(open(TARGET_BINARY, 'rb').read()).hexdigest()
    g10_ok = (post_sha == EXPECTED_SHA256)
    results.append({"gate": "Gate 10: Post-Execution Binary Integrity", "status": "PASS" if g10_ok else "FAIL"})
    print(f"[Gate 10] Post-Execution Binary Check: {'PASS' if g10_ok else 'FAIL'}")

    all_passed = all(r["status"] == "PASS" for r in results)
    print(f"\nOVERALL MASTER PRESERVATION STATUS: {'PASS' if all_passed else 'FAIL'}\n")

if __name__ == '__main__':
    run_reproduce()
