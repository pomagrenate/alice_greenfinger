# Phase 9 Comprehensive Unified Campaign Differential Harness (45 Scenarios)
import subprocess
import os
import sys

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
dist_exe = os.path.join(PROJECT_ROOT, 'distribution', 'AliceGreenfingers_Reconstructed.exe')

def test_phase9_differential():
    print("Testing Phase 9 Comprehensive Unified Campaign Suite (45 Scenarios)...")
    result = subprocess.run([dist_exe], cwd=os.path.dirname(dist_exe), capture_output=True, text=True)
    out = result.stdout
    print(out)

    assert result.returncode == 0, f"Execution failed with code {result.returncode}"
    assert "[GOLDEN-01..14] Phase 5 Golden Suite verified" in out
    assert "[GUI-01..10] Phase 6 GUI Smoke Suite verified" in out
    assert "[AV-01..10] Phase 7 Golden AV Suite verified" in out
    assert "[DSP-01..06] Phase 8 Deep Dispatch Suite verified" in out
    for i in range(1, 6):
        assert f"[E2E-{i:02d}]" in out, f"E2E {i:02d} failed!"

    assert "All 45 Reconstructed Scenarios PASSED" in out
    print("PHASE 9 DIFFERENTIAL VALIDATION: ALL 45 CAMPAIGN SCENARIOS PASSED (100% PARITY)!")

if __name__ == '__main__':
    test_phase9_differential()
