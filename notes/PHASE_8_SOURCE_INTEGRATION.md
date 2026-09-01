# ALICE GREENFINGERS - SOURCE INTEGRATION REPORT (STEP 16)

*Generated on 2026-09-01*

## 1. Concrete Source Reconstructions & Dispatch Bindings
- **Win32 IAT Calls (Cluster E - 46 Calls):** Linked directly against `user32` and `gdi32`.
- **Opcode Event Registry (Cluster B - 98 Calls):** Integrated opcodes `1001` through `1007` into `src/events/event_dispatcher.cpp`.
- **State Machine Transitions (Cluster F - 32 Calls):** Integrated into `src/state/game_state.cpp`.
- **VTable Slots (Cluster A - 4 Slots):** Bound directly to `VTABLE_00497000`.
- **Remaining Unresolved Sites (124 Sites):** Isolated behind telemetry logger `Unresolved_RecordCall`.
