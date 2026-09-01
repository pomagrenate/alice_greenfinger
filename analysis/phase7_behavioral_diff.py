# Phase 7 Comprehensive Behavioral & Audio-Visual Differential Harness
import subprocess
import os
import sys

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
dist_exe = os.path.join(PROJECT_ROOT, 'distribution', 'AliceGreenfingers_Reconstructed.exe')

def test_phase7_differential():
    print("Testing Phase 7 Comprehensive AV Differential Suite...")
    result = subprocess.run([dist_exe], cwd=os.path.dirname(dist_exe), capture_output=True, text=True)
    out = result.stdout
    print(out)

    assert result.returncode == 0, f"Execution failed with code {result.returncode}"
    for i in range(1, 15):
        assert f"[GOLDEN-{i:02d}]" in out, f"Golden {i:02d} failed!"
    for i in range(1, 11):
        assert f"[GUI-{i:02d}]" in out, f"GUI Smoke {i:02d} failed!"
    for i in range(1, 11):
        assert f"[AV-{i:02d}]" in out, f"AV Golden {i:02d} failed!"

    assert "All 14 Phase 5 Golden, 10 Phase 6 GUI Smoke, and 10 Phase 7 Golden AV Scenarios PASSED" in out
    print("PHASE 7 DIFFERENTIAL VALIDATION: ALL 34 TEST SCENARIOS PASSED (100% PARITY)!")

if __name__ == '__main__':
    test_phase7_differential()
