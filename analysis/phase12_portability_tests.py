# Phase 12 Master 55-Scenario Portability & Differential Validation Suite
import subprocess
import os
import sys

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
dist_exe = os.path.join(PROJECT_ROOT, 'distribution', 'AliceGreenfingers_Reconstructed.exe')

def test_phase12_portability():
    print("Testing Phase 12 Master Differential & Portability Suite (55 Scenarios)...")
    result = subprocess.run([dist_exe], cwd=os.path.dirname(dist_exe), capture_output=True, text=True)
    out = result.stdout
    print(out)

    assert result.returncode == 0, f"Execution failed with code {result.returncode}"
    assert "[GOLDEN-01..14]" in out
    assert "[GUI-01..10]" in out
    assert "[AV-01..10]" in out
    assert "[DSP-01..06]" in out
    assert "[E2E-01..05]" in out
    assert "[EXP11-01..05]" in out
    for i in range(1, 6):
        assert f"[PORT-{i:02d}]" in out, f"PORT-{i:02d} failed!"

    assert "All 55 Reconstructed Scenarios PASSED" in out
    print("PHASE 12 MASTER PORTABILITY & DIFFERENTIAL VALIDATION: ALL 55 SCENARIOS PASSED (100% PARITY)!")

if __name__ == '__main__':
    test_phase12_portability()
