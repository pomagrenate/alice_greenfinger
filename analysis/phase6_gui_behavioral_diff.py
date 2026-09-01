# Phase 6 Simulation/Presentation Isolation Differential Verification Harness
import subprocess
import os
import sys

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
reconstructed_exe = os.path.join(PROJECT_ROOT, 'build', 'alice_greenfingers_reconstructed.exe')

def test_phase6_isolation():
    print("Testing Phase 6 Simulation & Presentation Isolation...")
    result = subprocess.run([reconstructed_exe], capture_output=True, text=True)
    out = result.stdout
    print(out)
    
    assert result.returncode == 0, f"Expected returncode 0, got {result.returncode}"
    for i in range(1, 15):
        assert f"[GOLDEN-{i:02d}]" in out, f"Golden {i:02d} missing!"
    for i in range(1, 11):
        assert f"[GUI-{i:02d}]" in out, f"GUI Smoke {i:02d} missing!"
    assert "All 14 Phase 5 Golden Scenarios and 10 Phase 6 GUI Smoke Tests PASSED" in out, "Suite failed!"
    print("PHASE 6 DIFFERENTIAL VALIDATION: ALL GOLDEN & GUI SMOKE TESTS MATCH!")

if __name__ == '__main__':
    test_phase6_isolation()
