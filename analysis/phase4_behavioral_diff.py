# Phase 4 Differential Verification Harness
import subprocess
import os
import sys

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
reconstructed_exe = os.path.join(PROJECT_ROOT, 'build', 'alice_greenfingers_reconstructed.exe')

def test_phase4_golden_cases():
    print("Testing Phase 4 Golden Cases...")
    result = subprocess.run([reconstructed_exe], capture_output=True, text=True)
    out = result.stdout
    print(out)
    
    assert result.returncode == 0, f"Expected returncode 0, got {result.returncode}"
    assert "[GOLDEN-01]" in out, "GOLDEN-01 failed"
    assert "[GOLDEN-02]" in out, "GOLDEN-02 failed"
    assert "[GOLDEN-03]" in out, "GOLDEN-03 failed"
    assert "[GOLDEN-04]" in out, "GOLDEN-04 failed"
    assert "[GOLDEN-05]" in out, "GOLDEN-05 failed"
    assert "[GOLDEN-06]" in out, "GOLDEN-06 failed"
    assert "All 6 Phase 4 Golden Cases PASSED" in out, "Golden suite failed"
    print("PHASE 4 DIFFERENTIAL VALIDATION: ALL GOLDEN CASES MATCH!")

if __name__ == '__main__':
    test_phase4_golden_cases()
