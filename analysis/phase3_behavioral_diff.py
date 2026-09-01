# Phase 3 Behavioral Differential Verification Harness
import subprocess
import os
import sys

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
reconstructed_exe = os.path.join(PROJECT_ROOT, 'build', 'alice_greenfingers_reconstructed.exe')

def test_reconstructed_behavior():
    print("Testing Reconstructed Program Behavior...")
    result = subprocess.run([reconstructed_exe], capture_output=True, text=True)
    out = result.stdout
    print("Program Output:")
    print(out)
    
    assert result.returncode == 0, f"Expected returncode 0, got {result.returncode}"
    assert "State: 0" in out, "Failed to verify Initial State 0"
    assert "PopCap GFX archive loaded" in out, "Failed to verify Resource Loading"
    assert "FMOD Audio Subsystem active: 1" in out, "Failed to verify Audio Subsystem"
    assert "Frame Counter: 5" in out, "Failed to verify Frame Tick Update"
    assert "Unresolved Call Sites Triaged: 425" in out, "Failed to verify 425 unresolved call sites"
    print("ALL BEHAVIORAL ASSERTIONS PASSED!")

if __name__ == '__main__':
    test_reconstructed_behavior()
