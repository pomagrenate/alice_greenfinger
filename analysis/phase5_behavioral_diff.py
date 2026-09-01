# Phase 5 Behavioral Differential Verification Harness
import subprocess
import os
import sys

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
reconstructed_exe = os.path.join(PROJECT_ROOT, 'build', 'alice_greenfingers_reconstructed.exe')

def test_phase5_scenarios():
    print("Testing Phase 5 Golden Scenarios...")
    result = subprocess.run([reconstructed_exe], capture_output=True, text=True)
    out = result.stdout
    print(out)
    
    assert result.returncode == 0, f"Expected returncode 0, got {result.returncode}"
    for i in range(1, 15):
        tag = f"[GOLDEN-{i:02d}]"
        assert tag in out, f"Scenario {tag} missing in output!"
    assert "All 14 Phase 5 Golden Scenarios PASSED" in out, "Golden suite failed"
    print("PHASE 5 DIFFERENTIAL VALIDATION: ALL 14 SCENARIOS MATCH!")

if __name__ == '__main__':
    test_phase5_scenarios()
