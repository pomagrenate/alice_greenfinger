# Alice Greenfingers — Playability Specification (Phase 16)

## 1. Playable Lifecycle Definition
The standalone executable provides a complete, interactive, end-to-end playable loop:
```text
[Launch Application]
        │
        ▼
[Title / Main Menu]
        │ (Click New Game)
        ▼
[Player Name Profile Dialog]
        │ (Submit Profile)
        ▼
[Interactive 5x8 Farm Grid]
        │ (Buy Seeds -20 / Sow Tile / 300-Tick Growth / Harvest Carrot)
        ▼
[Market Entry (Opcode 1004)]
        │ (Sell Crop +50 to 4-Slot Customer Stalls)
        ▼
[Day Transition Summary (Opcode 1003)]
        │ (Advance Day Counter / Ledger Persistence)
        ▼
[Save Game (AGSV Binary Stream) / Clean Exit]
```

## 2. Playable Quality Requirements
1. **Interactive Boot:** Window opens immediately at 800x600 resolution without crashes or unhandled exceptions.
2. **Deterministic Simulation:** 60.0 Hz simulation clock (`DAT_004a7f54`) runs continuously with 0 tick drift.
3. **Responsive Input:** Mouse movement and clicks trigger corresponding UI and plot interactions.
4. **Economic Stability:** Currency ledger (`DAT_004a86a4`) enforces non-negative arithmetic.
5. **Persistence Round-Trip:** Game saves and reloads exact grid and economic state.
