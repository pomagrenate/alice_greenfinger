#!/usr/bin/env python3
import subprocess
import os
import sys

PROJECT_ROOT = r'C:\Users\Admin\Downloads\AliceGreenfingers_RE'
dist_exe = os.path.join(PROJECT_ROOT, 'distribution', 'AliceGreenfingers_Reconstructed.exe')

def test_play_e2e():
    print("Testing Phase 16 Playable E2E Scenarios (PLAY-E2E-001..010)...")
    res = subprocess.run([dist_exe], cwd=os.path.dirname(dist_exe), capture_output=True, text=True)
    out = res.stdout
    print(out)

    assert res.returncode == 0, f"Execution failed with code {res.returncode}"
    for i in range(1, 11):
        assert f"[PLAY-E2E-{i:03d}]" in out, f"Scenario PLAY-E2E-{i:03d} failed!"

    assert "PLAYABLE GAME RELEASE VALIDATED" in out
    print("ALL 10 PLAYABLE E2E SCENARIOS PASSED (100% PLAYABLE STATUS)!")

if __name__ == '__main__':
    test_play_e2e()
