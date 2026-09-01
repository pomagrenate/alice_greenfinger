# ALICE GREENFINGERS - SUBSYSTEM DEPENDENCY GRAPH (STEP 3)

*Generated on 2026-09-01*

## 1. Unified Campaign Dependency Diagram
```text
[Platform Window]
       │
       ▼
 [Input Queue] ──► [Event Dispatcher (FUN_00404170)] ──► [Audio System (FMOD)]
                         │
                         ▼
             [Game State Machine (0..5)]
                         │
        ┌────────────────┴────────────────┬────────────────┐
        ▼                                 ▼                ▼
[Simulation Clock]              [Market & Shop State]  [Software Renderer]
 (60Hz DAT_004a7f54)             (STATE_SHOP_MARKET)    (3-Layer Backbuffer)
        │                                 ▲                ▲
        ▼                                 │                │
[Farm Grid & Crops] ─────────────► [Economy Ledger] ───────┤
 (5-Stage Animation)              (DAT_004a86a4)           │
        ▲                                                  │
        └────────────────── [Resource Loader (LBTC)] ──────┘
```
