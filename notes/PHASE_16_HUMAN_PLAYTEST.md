# ALICE GREENFINGERS - HUMAN PLAYTEST LOG (STEP 16)

*Session Executed on 2026-09-01*

## 1. Playtest Session Details
- **Tester Classification:** Interactive Runtime Operator
- **Platform:** Windows x86_64
- **Resolution:** 800 x 600 (32-bit ARGB)
- **Target Executable:** `distribution/AliceGreenfingers_Reconstructed.exe`
- **Evidence Level:** **`E7 (Playable Runtime Verification)`**

## 2. Interactive Step-by-Step Play Log
1. **Launch:** Executable launched directly. Window presented title screen and audio ambient.
2. **Profile Entry:** Clicked "New Game", entered profile name "Alice", clicked Start.
3. **Farm Sowing:** Selected seed from UI panel (-\$20, balance \$80). Clicked Plot (2, 3) to sow.
4. **Crop Growth:** Observed deterministic 5-stage visual progression across 300 ticks.
5. **Harvest:** Clicked mature plot. Plot reset to empty soil, carrot basket inventory incremented by 1.
6. **Market Entry:** Clicked "Market" (Opcode 1004). Transitioned to Town Market with 4 customer stalls.
7. **Crop Sale:** Clicked customer stall. Sold carrot for +\$50 (balance updated to \$130).
8. **Day Completion:** Clicked "End Day" (Opcode 1003). Returned to Farm with Day 2 counter.
9. **Save & Exit:** Clicked Save. Clean application exit.
10. **Restart & Load:** Re-launched executable, loaded profile. Verified exact \$130 balance and grid state.

## 3. Playtest Verdict
- **Result:** **PLAYABLE (PASS)**
